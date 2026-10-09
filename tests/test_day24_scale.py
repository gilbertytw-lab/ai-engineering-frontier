import argparse
import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


KNOWLEDGE = Path(__file__).parents[1] / "knowledge"
sys.path.insert(0, str(KNOWLEDGE))
import ingest

spec = importlib.util.spec_from_file_location("day24_scale", KNOWLEDGE / "benchmark_scale.py")
scale = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scale)


class FakeTokenizer:
    def __init__(self, name):
        pass

    def encode(self, text):
        return text.split()

    def count(self, text):
        return len(self.encode(text))

    def decode(self, tokens):
        return " ".join(tokens)


class Day24ScaleTests(unittest.TestCase):
    def raw_files(self, root):
        raw = root / "raw"
        raw.mkdir()
        for name in ["c", "a", "b"]:
            (raw / f"{name}.md").write_text(
                f'---\ndocument_id: "doc-{name}"\nsource_name: "{name}.md"\n'
                'source_snapshot: "source.md"\n---\n\nPod selector\r\n',
                encoding="utf-8", newline="",
            )
        return raw

    def test_crlf_hash_matches_actual_raw_bytes(self):
        with tempfile.TemporaryDirectory() as temporary:
            raw = self.raw_files(Path(temporary))
            path = raw / "a.md"
            document = ingest.parse_raw_document(path)
            self.assertEqual(document.raw_sha256, hashlib.sha256(path.read_bytes()).hexdigest())
            self.assertIn("\r\n", document.body)

    def test_prefix_limit_is_sorted_and_does_not_modify_raw(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            raw = self.raw_files(root)
            before = {p.name: p.read_bytes() for p in raw.glob("*.md")}
            with mock.patch.object(ingest, "Tokenizer", FakeTokenizer):
                manifest = ingest.build_manifest(raw, root / "manifest.json", document_limit=2)
            self.assertEqual([d["document_id"] for d in manifest["documents"]], ["doc-a", "doc-b"])
            self.assertEqual(before, {p.name: p.read_bytes() for p in raw.glob("*.md")})
            with self.assertRaises(ValueError):
                ingest.build_manifest(raw, root / "bad.json", document_limit=0)

    def test_percentiles_use_median_and_nearest_rank(self):
        stats = scale.latency_stats(list(range(1, 21)))
        self.assertEqual(stats["p50_ms"], 10.5)
        self.assertEqual(stats["p95_ms"], 19)
        self.assertEqual(stats["samples"], 20)

    def test_query_rounds_reuse_index_and_exclude_warmups(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            raw = self.raw_files(root)
            queries = root / "queries.json"
            queries.write_text(json.dumps([
                {"id": "hit", "query": "Pod"},
                {"id": "miss", "query": "missingword"},
            ]))
            args = argparse.Namespace(
                raw_dir=raw, workspace_root=root, tokenizer="fake", max_tokens=160,
                overlap_tokens=24, queries=queries, rounds=3, limit=5,
            )
            with (
                mock.patch.object(ingest, "Tokenizer", FakeTokenizer),
                mock.patch.object(scale, "build_index", wraps=scale.build_index) as build,
                mock.patch.object(scale, "search", wraps=scale.search) as search,
            ):
                result = scale.measure_size(args, 2)
            self.assertEqual(build.call_count, 1)
            self.assertEqual(search.call_count, 8)
            self.assertEqual(result["query_latency"]["samples"], 6)
            self.assertEqual([q["returned_chunks"] for q in result["queries"]], [2, 0])
            self.assertTrue(result["raw_unchanged"])
            self.assertEqual(result["integrity_check"], "ok")
            self.assertEqual(result["fts_integrity_check"], "ok")
            with self.assertRaises(FileExistsError):
                scale.measure_size(args, 2)

    def test_invalid_query_set_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "queries.json"
            for data in [[], [{"id": "x", "query": "---"}],
                         [{"id": "x", "query": "Pod"}, {"id": "x", "query": "Service"}]]:
                path.write_text(json.dumps(data))
                with self.assertRaises(ValueError):
                    scale.load_queries(path)

    def test_oversized_run_fails_before_creating_workspace(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            raw = self.raw_files(root)
            args = argparse.Namespace(
                raw_dir=raw, workspace_root=root / "outputs", rounds=3, limit=5,
                max_tokens=160, overlap_tokens=24, worker_size=None, sizes=[4],
            )
            with mock.patch.object(scale, "parse_args", return_value=args):
                self.assertEqual(scale.main(), 1)
            self.assertFalse(args.workspace_root.exists())


if __name__ == "__main__":
    unittest.main()
