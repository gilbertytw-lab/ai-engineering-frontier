import importlib.util
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "knowledge" / "retrieve.py"
spec = importlib.util.spec_from_file_location("day10_retrieve", SCRIPT)
retrieve = importlib.util.module_from_spec(spec)
spec.loader.exec_module(retrieve)


def fts5_available() -> bool:
    try:
        with sqlite3.connect(":memory:") as connection:
            connection.execute("CREATE VIRTUAL TABLE probe USING fts5(text)")
    except sqlite3.OperationalError:
        return False
    return True


@unittest.skipUnless(fts5_available(), "本機 SQLite 沒有啟用 FTS5")
class Day10RetrieveTests(unittest.TestCase):
    def manifest(self):
        return {
            "manifest_version": "0.1.0",
            "tokenizer": "fake-tokenizer",
            "chunking": {"max_tokens": 10, "overlap_tokens": 2},
            "documents": [
                {
                    "document_id": "doc-release",
                    "source_name": "release-policy.md",
                    "raw_path": "knowledge/raw/release-policy.md",
                    "chunks": [
                        {
                            "chunk_id": "doc-release-chunk-0001",
                            "start_line": 10,
                            "end_line": 16,
                            "token_count": 8,
                            "text_sha256": "hash-release",
                            "text": "release owner checks CI and staging health",
                        },
                        {
                            "chunk_id": "doc-release-chunk-0002",
                            "start_line": 18,
                            "end_line": 22,
                            "token_count": 7,
                            "text_sha256": "hash-rollback",
                            "text": "production canary and rollback target",
                        },
                    ],
                },
                {
                    "document_id": "doc-config",
                    "source_name": "service-config.md",
                    "raw_path": "knowledge/raw/service-config.md",
                    "chunks": [
                        {
                            "chunk_id": "doc-config-chunk-0001",
                            "start_line": 8,
                            "end_line": 14,
                            "token_count": 6,
                            "text_sha256": "hash-config",
                            "text": "production worker count and retry defaults",
                        }
                    ],
                },
            ],
        }

    def write_manifest(self, root: Path) -> Path:
        path = root / "manifest.json"
        path.write_text(json.dumps(self.manifest()), encoding="utf-8")
        return path

    def test_build_and_search_preserves_source_location(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest_path = self.write_manifest(root)
            database_path = root / "retrieval.sqlite"

            result = retrieve.build_index(manifest_path, database_path)
            matches = retrieve.search(database_path, "production rollback", limit=5)

            self.assertEqual(result["document_count"], 2)
            self.assertEqual(result["chunk_count"], 3)
            self.assertEqual([match["chunk_id"] for match in matches], ["doc-release-chunk-0002"])
            self.assertEqual(matches[0]["source_name"], "release-policy.md")
            self.assertEqual(matches[0]["start_line"], 18)
            self.assertGreater(matches[0]["bm25"], 0)

    def test_rebuild_replaces_removed_chunks(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest_path = self.write_manifest(root)
            database_path = root / "retrieval.sqlite"
            retrieve.build_index(manifest_path, database_path)

            manifest = self.manifest()
            manifest["documents"][0]["chunks"] = manifest["documents"][0]["chunks"][:1]
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            result = retrieve.build_index(manifest_path, database_path)

            self.assertEqual(result["chunk_count"], 2)
            self.assertEqual(retrieve.search(database_path, "rollback"), [])

    def test_query_operators_are_not_executed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest_path = self.write_manifest(root)
            database_path = root / "retrieval.sqlite"
            retrieve.build_index(manifest_path, database_path)

            matches = retrieve.search(database_path, 'production OR rollback')

            self.assertEqual(matches, [])

    def test_cjk_phrase_is_searchable(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = self.manifest()
            manifest["documents"][1]["chunks"][0]["text"] = "部署檢查與 production worker count"
            manifest_path = root / "manifest.json"
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            database_path = root / "retrieval.sqlite"
            retrieve.build_index(manifest_path, database_path)

            matches = retrieve.search(database_path, "部署檢查")

            self.assertEqual([match["chunk_id"] for match in matches], ["doc-config-chunk-0001"])

    def test_empty_query_is_rejected(self):
        with self.assertRaises(ValueError):
            retrieve._match_query("---")


if __name__ == "__main__":
    unittest.main()
