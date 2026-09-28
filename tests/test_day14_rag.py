import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from knowledge import ingest, rag


class FakeTokenizer:
    name = "test-tokenizer"

    def chat_count(self, messages):
        return sum(len(message["content"].split()) + 1 for message in messages)


def completion(answer, *, finish_reason="stop", prompt_tokens=None):
    result = {
        "choices": [{"message": {"content": json.dumps(answer)}, "finish_reason": finish_reason}],
        "usage": {},
    }
    if prompt_tokens is not None:
        result["usage"]["prompt_tokens"] = prompt_tokens
    return result


class Day14RagTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.database = root / "index.sqlite"
        self.manifest = root / "manifest.json"
        self.manifest.write_text(json.dumps({
            "documents": [{
                "document_id": "doc-config",
                "source_name": "service-config.md",
                "raw_path": "knowledge/raw/doc-config.md",
                "chunks": [{
                    "chunk_id": "config-1",
                    "start_line": 12,
                    "end_line": 18,
                    "token_count": 3,
                    "text_sha256": "config-hash",
                    "text": "production HARBOR_WORKER_COUNT 8",
                }],
            }],
        }), encoding="utf-8")
        rag.build_index(self.manifest, self.database)

    def run_query(self, completion_fn, **overrides):
        args = {
            "database": self.database,
            "tokenizer": FakeTokenizer(),
            "query": "production",
            "question": "production worker count?",
            "base_url": "http://127.0.0.1:8081/v1",
            "model": "test-model",
            "completion_fn": completion_fn,
        }
        args.update(overrides)
        return rag.run_query(**args)

    def test_citation_contract_rejects_unseen_ids_and_invalid_shapes(self):
        valid = {"answer": "8", "citations": ["config-1"], "no_answer": False}
        self.assertEqual(rag.parse_rag_answer(json.dumps(valid), {"config-1"}), valid)
        invalid = [
            {**valid, "citations": ["indexed-but-not-selected"]},
            {**valid, "citations": []},
            {**valid, "citations": ["config-1", "config-1"]},
            {**valid, "citations": [8]},
            {**valid, "no_answer": True},
            {**valid, "no_answer": 0},
            {**valid, "answer": " "},
            {**valid, "extra": "field"},
        ]
        for answer in invalid:
            with self.subTest(answer=answer), self.assertRaises(RuntimeError):
                rag.parse_rag_answer(json.dumps(answer), {"config-1"})
        for text in (
            '```json\n{"answer":"8","citations":["config-1"],"no_answer":false}\n```',
            '{"answer":"8","answer":"9","citations":["config-1"],"no_answer":false}',
            '{"answer":NaN,"citations":[],"no_answer":true}',
        ):
            with self.subTest(text=text), self.assertRaises(RuntimeError):
                rag.parse_rag_answer(text, {"config-1"})

    def test_empty_retrieval_skips_model_and_records_refusal(self):
        model = Mock(side_effect=AssertionError("must not call model"))
        record = self.run_query(model, query="absent")
        self.assertEqual(record["status"], "no_answer")
        self.assertFalse(record["model_called"])
        self.assertTrue(record["response"]["no_answer"])
        self.assertEqual(record["response"]["citations"], [])
        self.assertEqual(record["model_elapsed_ms"], 0.0)
        model.assert_not_called()

    def test_selected_evidence_is_sent_unchanged_and_sources_come_from_index(self):
        model = Mock(return_value=completion({"answer": "8", "citations": ["config-1"], "no_answer": False}))
        record = self.run_query(model)
        self.assertEqual(record["status"], "ok")
        self.assertEqual(model.call_args.args[0], record["context"]["messages"])
        self.assertEqual(model.call_args.kwargs["max_tokens"], 512)
        self.assertEqual(record["sources"][0]["raw_path"], "knowledge/raw/doc-config.md")
        self.assertEqual(record["sources"][0]["start_line"], 12)
        self.assertEqual(record["sources"][0]["end_line"], 18)

    def test_length_finish_is_failure_even_with_parseable_json(self):
        model = Mock(return_value=completion(
            {"answer": "8", "citations": ["config-1"], "no_answer": False},
            finish_reason="length",
        ))
        record = self.run_query(model)
        self.assertEqual(record["status"], "error")
        self.assertIn("finish_reason=length", record["error"])
        self.assertIn("completion", record)
        self.assertNotIn("response", record)

    def test_missing_fact_can_refuse_with_selected_evidence(self):
        model = Mock(return_value=completion({"answer": "不知道 retention。", "citations": [], "no_answer": True}))
        record = self.run_query(model)
        self.assertEqual(record["status"], "no_answer")
        self.assertTrue(record["model_called"])
        self.assertTrue(record["context"]["selected_chunks"])
        self.assertEqual(record["sources"], [])

    def test_base_budget_overflow_is_error_without_model_call(self):
        model = Mock(side_effect=AssertionError("must not call model"))
        record = self.run_query(model, context_window=2, output_reserve=1)
        self.assertEqual(record["status"], "error")
        self.assertIn("固定 prompt", record["error"])
        model.assert_not_called()

    def test_runtime_budget_overflow_is_error_and_keeps_raw_completion(self):
        model = Mock(return_value=completion(
            {"answer": "8", "citations": ["config-1"], "no_answer": False},
            prompt_tokens=2000,
        ))
        record = self.run_query(model)
        self.assertEqual(record["status"], "error")
        self.assertIn("runtime 回報", record["error"])
        self.assertIn("completion", record)

    def test_dry_run_counts_context_without_model_call(self):
        model = Mock(side_effect=AssertionError("must not call model"))
        record = self.run_query(model, dry_run=True)
        self.assertEqual(record["status"], "planned")
        self.assertTrue(record["context"]["selected_chunks"])
        model.assert_not_called()

    def test_http_payload_preserves_messages_and_template_options(self):
        expected = completion({"answer": "8", "citations": ["config-1"], "no_answer": False})
        response = Mock()
        response.read.return_value = json.dumps(expected).encode()
        response.__enter__ = Mock(return_value=response)
        response.__exit__ = Mock(return_value=False)
        messages = [{"role": "system", "content": "rules"}, {"role": "user", "content": "evidence"}]
        with patch.object(rag, "urlopen", return_value=response) as urlopen:
            result = rag.call_completion(messages, base_url="http://localhost/v1", model="test-model", max_tokens=512)
        self.assertEqual(result, expected)
        payload = json.loads(urlopen.call_args.args[0].data)
        self.assertEqual(payload["messages"], messages)
        self.assertEqual(payload["chat_template_kwargs"], {"enable_thinking": False})
        self.assertEqual(payload["max_tokens"], 512)

    def test_token_counter_passes_disabled_thinking_to_chat_template(self):
        fake = Mock()
        fake.apply_chat_template.return_value = {"input_ids": [1, 2, 3]}
        with patch("transformers.AutoTokenizer.from_pretrained", return_value=fake):
            tokenizer = ingest.Tokenizer("test-model", chat_template_kwargs={"enable_thinking": False})
        self.assertEqual(tokenizer.chat_count([{"role": "user", "content": "question"}]), 3)
        self.assertIs(fake.apply_chat_template.call_args.kwargs["enable_thinking"], False)

    def test_rebuilt_database_keeps_search_evidence_identical(self):
        before = rag.search(self.database, "production")
        self.database.unlink()
        rag.build_index(self.manifest, self.database)
        after = rag.search(self.database, "production")
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
