import importlib.util
import io
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "knowledge" / "convert.py"
spec = importlib.util.spec_from_file_location("day08_batch", SCRIPT)
batch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(batch)


class Day08BatchTests(unittest.TestCase):
    def test_converts_whole_inbox_without_a_model(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            inbox = root / "knowledge" / "inbox"
            inbox.mkdir(parents=True)
            (inbox / "notes.txt").write_text("First line\nLast line\n", encoding="utf-8")
            (inbox / "guide.md").write_text("# Guide\n\nComplete body.\n", encoding="utf-8")
            (inbox / "day05.html").write_text(
                '<html><head><meta property="og:url" content="https://ithelp.ithome.com.tw/articles/10413625"></head>'
                '<body><nav>Site menu</nav><h2 class="qa-header__title">Day 5</h2>'
                '<div class="markdown__style"><p>Article body.</p><pre><code>print(42)</code></pre></div></body></html>',
                encoding="utf-8",
            )
            repeated = io.StringIO()
            with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                self.assertEqual(batch.convert_inbox(root), 0)
            with redirect_stdout(repeated), redirect_stderr(io.StringIO()):
                self.assertEqual(batch.convert_inbox(root), 0)
            self.assertIn("沒有來源檔", repeated.getvalue())
            self.assertFalse((inbox / "notes.txt").exists())
            self.assertTrue((inbox / "processed" / "notes.txt").exists())
            self.assertTrue((inbox / "processed" / "guide.md").exists())
            self.assertTrue((inbox / "processed" / "day05.html").exists())
            outputs = list((root / "knowledge" / "raw").glob("*.md"))
            self.assertEqual(len(outputs), 3)
            bodies = [path.read_text(encoding="utf-8") for path in outputs]
            self.assertTrue(any("Last line" in body for body in bodies))
            self.assertTrue(any("Complete body." in body for body in bodies))
            article = next(body for body in bodies if "Article body." in body)
            self.assertIn("# Day 5", article)
            self.assertIn("print(42)", article)
            self.assertNotIn("Site menu", article)

    def test_unsupported_file_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            inbox = root / "knowledge" / "inbox"
            inbox.mkdir(parents=True)
            (inbox / "report.docx").write_bytes(b"unsupported")
            errors = io.StringIO()
            with redirect_stdout(io.StringIO()), redirect_stderr(errors):
                self.assertEqual(batch.convert_inbox(root), 1)
            self.assertIn("不支援", errors.getvalue())
            self.assertTrue((inbox / "report.docx").exists())
            self.assertFalse((root / "knowledge" / "raw").exists())

    def test_failed_source_stays_in_inbox(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            inbox = root / "knowledge" / "inbox"
            inbox.mkdir(parents=True)
            bad = inbox / "broken.pdf"
            bad.write_bytes(b"not a PDF")
            with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                self.assertEqual(batch.convert_inbox(root), 1)
            self.assertTrue(bad.exists())
            self.assertFalse((inbox / "processed" / "broken.pdf").exists())


if __name__ == "__main__":
    unittest.main()
