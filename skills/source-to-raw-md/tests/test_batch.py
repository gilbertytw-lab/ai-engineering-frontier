import io
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))
from batch import convert_inbox


class BatchTests(unittest.TestCase):
    def test_moves_successful_original_and_skips_it_next_time(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            inbox = root / "knowledge" / "inbox"
            inbox.mkdir(parents=True)
            (inbox / "notes.txt").write_text("First line\nLast line\n", encoding="utf-8")
            with redirect_stdout(io.StringIO()):
                self.assertEqual(convert_inbox(root), 0)
            self.assertFalse((inbox / "notes.txt").exists())
            self.assertEqual((inbox / "processed" / "notes.txt").read_text(encoding="utf-8"),
                             "First line\nLast line\n")
            self.assertEqual(len(list((root / "knowledge" / "raw").glob("*.md"))), 1)
            repeated = io.StringIO()
            with redirect_stdout(repeated):
                self.assertEqual(convert_inbox(root), 0)
            self.assertIn("沒有來源檔", repeated.getvalue())

    def test_failed_pdf_stays_pending(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            inbox = root / "knowledge" / "inbox"
            inbox.mkdir(parents=True)
            (inbox / "broken.pdf").write_bytes(b"not a PDF")
            with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                self.assertEqual(convert_inbox(root), 1)
            self.assertTrue((inbox / "broken.pdf").exists())
            self.assertFalse((inbox / "processed" / "broken.pdf").exists())


if __name__ == "__main__":
    unittest.main()
