import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "knowledge" / "context.py"
spec = importlib.util.spec_from_file_location("day13_context", SCRIPT)
context = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = context
spec.loader.exec_module(context)


class FakeTokenizer:
    def count(self, text):
        return len(text.split())

    def chat_count(self, messages):
        return sum(self.count(message["content"]) + 1 for message in messages)


def candidate(
    chunk_id,
    *,
    document_id="doc-release",
    source_name="release-policy.md",
    start_line=10,
    end_line=20,
    text="release owner checks rollback",
    bm25=3.0,
):
    return {
        "chunk_id": chunk_id,
        "document_id": document_id,
        "source_name": source_name,
        "raw_path": f"knowledge/raw/{source_name}",
        "start_line": start_line,
        "end_line": end_line,
        "token_count": len(text.split()),
        "text_sha256": f"hash-{chunk_id}",
        "text": text,
        "bm25": bm25,
    }


class Day13ContextTests(unittest.TestCase):
    def test_overlapping_chunks_keep_the_better_ranked_candidate(self):
        first = candidate("chunk-1", start_line=10, end_line=20, bm25=4.0)
        overlap = candidate("chunk-2", start_line=18, end_line=28, bm25=2.0)
        adjacent = candidate("chunk-3", start_line=29, end_line=35, bm25=1.0)

        kept, rejected = context.deduplicate_candidates([first, overlap, adjacent])

        self.assertEqual([item["chunk_id"] for item in kept], ["chunk-1", "chunk-3"])
        self.assertEqual(rejected[0]["chunk_id"], "chunk-2")
        self.assertIn("overlapping_lines_with:chunk-1", rejected[0]["rejection_reason"])

    def test_budget_counts_history_and_tool_schema(self):
        chunks = [candidate("chunk-1", text="one two three four five", bm25=3.0)]
        result = context.build_context(
            tokenizer=FakeTokenizer(),
            candidates=chunks,
            question="what should I check",
            history=[{"role": "user", "content": "earlier question"}],
            tool_schemas=[{"name": "list_sources", "read_only": True}],
            context_window=60,
            output_reserve=10,
        )

        self.assertGreater(result.base_input_tokens, 0)
        self.assertLessEqual(result.input_tokens + result.output_reserve, 60)
        self.assertIn("list_sources", result.messages[0]["content"])
        self.assertEqual(result.messages[1]["content"], "earlier question")

    def test_budget_rejection_is_recorded_and_result_is_reproducible(self):
        chunks = [
            candidate("chunk-1", text="one two three", bm25=3.0),
            candidate("chunk-2", text="four five six", start_line=30, end_line=35, bm25=2.0),
        ]

        first = context.build_context(
            tokenizer=FakeTokenizer(),
            candidates=chunks,
            question="question",
            context_window=20,
            output_reserve=8,
        )
        second = context.build_context(
            tokenizer=FakeTokenizer(),
            candidates=list(reversed(chunks)),
            question="question",
            context_window=20,
            output_reserve=8,
        )

        self.assertEqual(
            [item["chunk_id"] for item in first.selected_chunks],
            [item["chunk_id"] for item in second.selected_chunks],
        )
        self.assertTrue(first.rejected_chunks)
        self.assertEqual(first.rejected_chunks[0]["rejection_reason"], "context_budget")


if __name__ == "__main__":
    unittest.main()
