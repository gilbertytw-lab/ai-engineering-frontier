import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPT = Path(__file__).parents[1] / "knowledge" / "ingest.py"
spec = importlib.util.spec_from_file_location("day09_ingest", SCRIPT)
ingest = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = ingest
spec.loader.exec_module(ingest)


class FakeTokenizer:
    name = "fake-tokenizer"

    def encode(self, text):
        return text.split()

    def count(self, text):
        return len(self.encode(text))

    def decode(self, tokens):
        return " ".join(tokens)


class Day09IngestTests(unittest.TestCase):
    def write_raw(self, root, name="doc-example.md"):
        raw = root / "knowledge" / "raw"
        raw.mkdir(parents=True)
        content = (
            '---\n'
            'document_id: "doc-example"\n'
            'source_name: "example.md"\n'
            'source_snapshot: "knowledge/inbox/processed/example.md"\n'
            'source_sha256: "source-hash"\n'
            '---\n\n'
            '# Example\n\n'
            'alpha beta gamma\n'
            'delta epsilon zeta\n'
            'eta theta iota\n'
        )
        path = raw / name
        path.write_text(content, encoding="utf-8")
        return raw, path

    def test_manifest_is_deterministic_and_keeps_source_location(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw, _ = self.write_raw(root)
            output = root / "knowledge" / "index" / "manifest.json"
            with mock.patch.object(ingest, "Tokenizer", return_value=FakeTokenizer()):
                first = ingest.build_manifest(
                    raw,
                    output,
                    tokenizer_name="fake",
                    max_tokens=5,
                    overlap_tokens=1,
                )
            first_text = output.read_text(encoding="utf-8")
            with mock.patch.object(ingest, "Tokenizer", return_value=FakeTokenizer()):
                second = ingest.build_manifest(
                    raw,
                    output,
                    tokenizer_name="fake",
                    max_tokens=5,
                    overlap_tokens=1,
                )
            self.assertEqual(first, second)
            self.assertEqual(first_text, output.read_text(encoding="utf-8"))
            document = first["documents"][0]
            self.assertEqual(document["document_id"], "doc-example")
            self.assertEqual(document["source_name"], "example.md")
            self.assertEqual(document["chunk_count"], len(document["chunks"]))
            self.assertEqual(document["chunks"][0]["start_line"], 7)
            self.assertLessEqual(max(c["token_count"] for c in document["chunks"]), 5)

    def test_long_line_is_split_without_exceeding_budget(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw, _ = self.write_raw(root)
            original = ingest.parse_raw_document(next(raw.glob("*.md")))
            document = ingest.RawDocument(
                path=original.path,
                metadata=original.metadata,
                body="one two three four five six\n",
                body_start_line=original.body_start_line,
                raw_sha256=original.raw_sha256,
            )
            chunks = ingest.chunk_document(
                document,
                FakeTokenizer(),
                max_tokens=3,
                overlap_tokens=0,
            )
            self.assertTrue(chunks)
            self.assertLessEqual(max(c["token_count"] for c in chunks), 3)

    def test_invalid_overlap_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw, _ = self.write_raw(root)
            with mock.patch.object(ingest, "Tokenizer", return_value=FakeTokenizer()):
                with self.assertRaises(ValueError):
                    ingest.build_manifest(
                        raw,
                        root / "manifest.json",
                        tokenizer_name="fake",
                        max_tokens=4,
                        overlap_tokens=4,
                    )


if __name__ == "__main__":
    unittest.main()
