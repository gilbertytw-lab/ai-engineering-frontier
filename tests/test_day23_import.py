import json
import tempfile
import unittest
from pathlib import Path

from knowledge.import_corpus import corpus_checksum, import_corpus


class CorpusImportTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.sources = self.root / "sources"
        self.sources.mkdir()
        self.workspace = self.root / "workspace"

    def write(self, name, data):
        path = self.sources / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def run_import(self, checksum=None):
        return import_corpus(self.sources, self.workspace, "https://example.com/fixed/docs",
                             checksum or corpus_checksum(self.sources)[1])

    def test_same_name_and_body_in_different_directories_keep_separate_sources(self):
        body = b'---\ntitle: Example\n---\n\n{{< note >}}\nSame body.\n{{< /note >}}\n'
        self.write("a/_index.md", body)
        self.write("b/_index.md", body)
        report = self.run_import()
        self.assertEqual(report["converted"], 2)
        self.assertEqual(report["raw_files"], 2)
        for record in report["files"]:
            output = self.workspace / record["raw_path"]
            self.assertIn(body.decode(), output.read_text(encoding="utf-8"))
            saved = self.workspace / "knowledge/inbox/processed/corpus" / record["source_path"]
            self.assertEqual(saved.read_bytes(), body)
            self.assertFalse((self.workspace / "knowledge/inbox/corpus" / record["source_path"]).exists())
            metadata = json.loads(saved.with_name(saved.name + ".source.json").read_text())
            self.assertEqual(metadata["source_name"], record["source_path"])
            self.assertEqual(metadata["source_url"], "https://example.com/fixed/docs/" + record["source_path"])

    def test_rerun_validates_without_rewriting_outputs(self):
        self.write("guide.md", b"# Guide\n\nComplete body.\n")
        first = self.run_import()
        output = self.workspace / first["files"][0]["raw_path"]
        modified = output.stat().st_mtime_ns
        second = self.run_import()
        self.assertEqual((second["converted"], second["reused"], second["failed"]), (0, 1, 0))
        self.assertEqual(output.stat().st_mtime_ns, modified)

    def test_crlf_body_is_preserved_and_can_be_reimported(self):
        body = b"# Guide\r\n\r\nFirst line.\r\nLast line.\r\n"
        self.write("guide.md", body)
        first = self.run_import()
        self.assertEqual((first["converted"], first["failed"]), (1, 0))
        output = self.workspace / first["files"][0]["raw_path"]
        # The converter canonicalizes trailing newlines, preserving inner CRLF.
        self.assertEqual(output.read_bytes().split(b"\n---\n\n", 1)[1],
                         body.rstrip(b"\n") + b"\n")
        second = self.run_import()
        self.assertEqual((second["reused"], second["failed"]), (1, 0))
        # Exercise convert()'s existing-output branch, too: re-stage the same file.
        saved = self.workspace / "knowledge/inbox/processed/corpus/guide.md"
        pending = self.workspace / "knowledge/inbox/corpus/guide.md"
        saved.replace(pending)
        saved.with_name(saved.name + ".source.json").replace(
            pending.with_name(pending.name + ".source.json"))
        third = self.run_import()
        self.assertEqual((third["converted"], third["failed"]), (1, 0))

    def test_bad_utf8_stays_pending_and_does_not_stop_good_file(self):
        self.write("bad.md", b"\xff\xfe")
        self.write("good.md", b"# Good\n")
        report = self.run_import()
        self.assertEqual((report["converted"], report["failed"]), (1, 1))
        self.assertEqual(report["success_rate"], 0.5)
        self.assertTrue((self.workspace / "knowledge/inbox/corpus/bad.md").exists())
        self.assertFalse((self.workspace / "knowledge/inbox/processed/corpus/bad.md").exists())
        self.assertIn("error", report["files"][0])

    def test_checksum_mismatch_writes_nothing(self):
        self.write("guide.md", b"# Guide\n")
        with self.assertRaisesRegex(ValueError, "checksum 不符"):
            self.run_import("wrong-checksum")
        self.assertFalse(self.workspace.exists())

    def test_changed_saved_source_is_rejected_and_preserved(self):
        self.write("guide.md", b"# Guide\n")
        self.run_import()
        saved = self.workspace / "knowledge/inbox/processed/corpus/guide.md"
        saved.write_bytes(b"local edit\n")
        report = self.run_import()
        self.assertEqual(report["failed"], 1)
        self.assertEqual(saved.read_bytes(), b"local edit\n")

    def test_tampered_raw_is_rejected_on_rerun(self):
        self.write("guide.md", b"# Guide\n")
        first = self.run_import()
        output = self.workspace / first["files"][0]["raw_path"]
        output.write_text(output.read_text() + "extra text\n")
        second = self.run_import()
        self.assertEqual((second["reused"], second["failed"]), (0, 1))

    def test_overlapping_workspace_is_rejected(self):
        self.write("guide.md", b"# Guide\n")
        with self.assertRaisesRegex(ValueError, "互相包含"):
            import_corpus(self.sources, self.sources / "workspace", "https://example.com/docs",
                          corpus_checksum(self.sources)[1])

    def test_empty_corpus_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "沒有 Markdown"):
            corpus_checksum(self.sources)


if __name__ == "__main__":
    unittest.main()
