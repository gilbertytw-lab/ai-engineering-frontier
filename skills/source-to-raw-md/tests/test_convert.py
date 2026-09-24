import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "scripts" / "convert.py"
spec = importlib.util.spec_from_file_location("source_to_raw_convert", MODULE_PATH)
converter = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = converter
spec.loader.exec_module(converter)
sys.path.insert(0, str(MODULE_PATH.parent))
VALIDATOR_PATH = MODULE_PATH.parent / "validate.py"
validator_spec = importlib.util.spec_from_file_location("source_to_raw_validate", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(validator_spec)
validator_spec.loader.exec_module(validator)


class ConvertTests(unittest.TestCase):
    def test_long_text_is_not_truncated_and_original_is_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "notes.txt"
            source.write_text("Beginning\n" + "A" * 20000 + "\nThe end.\n", encoding="utf-8")
            output = converter.convert(str(source), root / "inbox", root / "raw")
            result = output.read_text(encoding="utf-8")
            self.assertIn('conversion_method: "programmatic"', result)
            self.assertIn('source_name: "notes.txt"', result)
            self.assertIn("Beginning", result)
            self.assertIn("The end.", result)
            self.assertEqual(result.count("A" * 20000), 1)
            self.assertEqual(len(list((root / "inbox").iterdir())), 1)
            self.assertEqual(converter.convert(str(source), root / "inbox", root / "raw"), output)
            self.assertEqual(validator.validate_file(output, root)[0], output.stem)
            output.write_text(result.replace("The end.", "Missing ending."), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "正文與來源抽取結果不一致"):
                validator.validate_file(output, root)

    def test_ithome_article_excludes_navigation_and_preserves_code(self):
        html = b'''<html><body><nav>Site menu</nav><h2 class="qa-header__title ir-article__title">Day 5</h2><div class="markdown__style"><h2>Section</h2><p>Keep this paragraph.</p><pre><code>if ready:\n    run()\n</code></pre><a href="/spec">Spec</a></div><footer>Other articles</footer></body></html>'''
        source = converter.Source(html, "https://ithelp.ithome.com.tw/articles/1", "web", "html", ".html", url="https://ithelp.ithome.com.tw/articles/1")
        result = converter.extract(source)
        self.assertIn("# Day 5", result.body)
        self.assertIn("## Section", result.body)
        self.assertIn("```\nif ready:\n    run()\n```", result.body)
        self.assertIn("https://ithelp.ithome.com.tw/spec", result.body)
        self.assertNotIn("Site menu", result.body)
        self.assertNotIn("Other articles", result.body)
        newer = converter.Source(html.replace(b"Site menu", b"New site menu"), source.name, source.kind, source.format, source.suffix, url=source.url)
        self.assertEqual(converter.document_id(source, result.identity_text), converter.document_id(newer, converter.extract(newer).identity_text))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            original = root / "page.html"
            original.write_bytes(html)
            out = converter.convert(str(original), root / "inbox", root / "raw")
            self.assertIn("```\nif ready:", out.read_text())

    def test_two_page_pdf_extracts_both_pages_and_blank_page_fails(self):
        from pypdf import PdfWriter
        from pypdf.generic import DecodedStreamObject, DictionaryObject, NameObject

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readable = root / "readable.pdf"
            writer = PdfWriter()
            font = writer._add_object(DictionaryObject({NameObject("/Type"): NameObject("/Font"), NameObject("/Subtype"): NameObject("/Type1"), NameObject("/BaseFont"): NameObject("/Helvetica")}))
            for label in (b"First page", b"Last page"):
                page = writer.add_blank_page(width=300, height=300)
                page[NameObject("/Resources")] = DictionaryObject({NameObject("/Font"): DictionaryObject({NameObject("/F1"): font})})
                stream = DecodedStreamObject()
                stream.set_data(b"BT /F1 12 Tf 50 250 Td (" + label + b") Tj ET")
                page[NameObject("/Contents")] = writer._add_object(stream)
            with readable.open("wb") as target:
                writer.write(target)
            out = converter.convert(str(readable), root / "inbox", root / "raw")
            text = out.read_text()
            self.assertIn('pdf_pages: 2', text)
            self.assertIn('## 第 1 頁\n\nFirst page', text)
            self.assertIn('## 第 2 頁\n\nLast page', text)
            self.assertLess(text.index('First page'), text.index('Last page'))
            self.assertEqual(validator.validate_file(out, root), (out.stem, 2))

            blank = root / "blank.pdf"
            writer = PdfWriter()
            writer.add_blank_page(width=300, height=300)
            with blank.open("wb") as target:
                writer.write(target)
            with self.assertRaisesRegex(ValueError, "OCR"):
                converter.convert(str(blank), root / "inbox", root / "raw")
            self.assertEqual(len(list((root / "raw").glob("*.md"))), 1)


if __name__ == "__main__":
    unittest.main()
