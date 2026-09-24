import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).parents[1] / "knowledge" / "measure.py"
spec = importlib.util.spec_from_file_location("day09_measure", SCRIPT)
measure = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = measure
spec.loader.exec_module(measure)


class FakeTokenizer:
    def count(self, text):
        return len(text.split())

    def chat_count(self, messages):
        return sum(self.count(message["content"]) for message in messages)


class Day09MeasureTests(unittest.TestCase):
    def manifest(self):
        return {
            "documents": [
                {
                    "document_id": "doc-one",
                    "chunks": [
                        {"chunk_id": "doc-one-chunk-0001", "token_count": 3, "text": "one two three"},
                        {"chunk_id": "doc-one-chunk-0002", "token_count": 3, "text": "four five six"},
                    ],
                }
            ]
        }

    def test_select_chunks_stops_at_evidence_budget(self):
        selected = measure.select_chunks(
            self.manifest(), document_id="doc-one", evidence_tokens=5
        )
        self.assertEqual([chunk["chunk_id"] for chunk in selected], ["doc-one-chunk-0001"])

    def test_dry_run_counts_input_without_calling_runtime(self):
        with patch.object(measure, "call_local_model") as call:
            result = measure.measure_once(
                question="What?",
                chunks=self.manifest()["documents"][0]["chunks"][:1],
                tokenizer=FakeTokenizer(),
                base_url="http://127.0.0.1:8081/v1",
                model=None,
                system_prompt="Rules",
                max_tokens=16,
                dry_run=True,
                enable_thinking=False,
            )
        self.assertEqual(result["status"], "planned")
        self.assertEqual(result["evidence_tokens"], 3)
        self.assertGreater(result["input_tokens"], result["evidence_tokens"])
        call.assert_not_called()

    def test_live_measurement_records_elapsed_time(self):
        with patch.object(measure, "call_local_model", return_value="answer text") as call, patch.object(
            measure.time, "perf_counter", side_effect=[1.0, 1.125]
        ):
            result = measure.measure_once(
                question="What?",
                chunks=self.manifest()["documents"][0]["chunks"][:1],
                tokenizer=FakeTokenizer(),
                base_url="test",
                model="test-model",
                system_prompt="Rules",
                max_tokens=16,
                dry_run=False,
                enable_thinking=False,
            )
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["elapsed_ms"], 125.0)
        self.assertEqual(result["output_tokens_estimate"], 2)
        self.assertEqual(
            call.call_args.kwargs["chat_template_kwargs"],
            {"enable_thinking": False},
        )


if __name__ == "__main__":
    unittest.main()
