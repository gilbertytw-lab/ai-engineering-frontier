import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "knowledge" / "wiki.py"
spec = importlib.util.spec_from_file_location("day11_wiki", SCRIPT)
wiki = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wiki)


class Day11WikiTests(unittest.TestCase):
    def write_raw(self, root: Path, name: str, document_id: str, title: str) -> None:
        raw_dir = root / "knowledge" / "raw"
        raw_dir.mkdir(parents=True, exist_ok=True)
        content = (
            "---\n"
            f'document_id: "{document_id}"\n'
            f'source_name: "{name}"\n'
            f'source_snapshot: "knowledge/inbox/processed/{name}"\n'
            'source_sha256: "source-hash"\n'
            'extracted_sha256: "extracted-hash"\n'
            'conversion_method: "programmatic"\n'
            'converter_version: "0.3.0"\n'
            "---\n\n"
            f"# {title}\n\n"
            "A source document.\n"
        )
        (raw_dir / name).write_text(content, encoding="utf-8")

    def snapshot(self, output_dir: Path) -> dict[str, str]:
        return {
            path.relative_to(output_dir).as_posix(): path.read_text(encoding="utf-8")
            for path in sorted(output_dir.rglob("*.md"))
        }

    def test_build_is_deterministic_and_keeps_provenance(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_raw(root, "api-spec.md", "doc-api", "Harbor API Specification")
            self.write_raw(root, "release-policy.md", "doc-release", "Harbor API Release Policy")
            raw_dir = root / "knowledge" / "raw"
            output_dir = root / "knowledge" / "wiki"

            first = wiki.build_source_catalog(raw_dir, output_dir)
            first_snapshot = self.snapshot(output_dir)
            second = wiki.build_source_catalog(raw_dir, output_dir)

            self.assertEqual(first["document_count"], 2)
            self.assertEqual(first["source_page_count"], 2)
            self.assertEqual(first["document_count"], second["document_count"])
            self.assertEqual(first_snapshot, self.snapshot(output_dir))

            page = (output_dir / "sources" / "doc-release.md").read_text(encoding="utf-8")
            self.assertIn('page_type: "source"', page)
            self.assertIn('document_id: "doc-release"', page)
            self.assertIn("../../raw/release-policy.md", page)
            self.assertIn(
                'source_snapshot: "knowledge/inbox/processed/release-policy.md"',
                page,
            )

            index = (output_dir / "index.md").read_text(encoding="utf-8")
            self.assertIn('source_count: "2"', index)
            self.assertIn("sources/doc-release.md", index)

    def test_rebuild_removes_stale_generated_pages_but_keeps_manual_pages(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_raw(root, "api-spec.md", "doc-api", "Harbor API Specification")
            raw_dir = root / "knowledge" / "raw"
            output_dir = root / "knowledge" / "wiki"
            wiki.build_source_catalog(raw_dir, output_dir)

            stale = output_dir / "sources" / "doc-stale.md"
            stale.write_text(
                '---\ngenerated_by: "knowledge/wiki.py"\n---\n# Stale\n',
                encoding="utf-8",
            )
            manual = output_dir / "sources" / "manual.md"
            manual.write_text("# Manual note\n", encoding="utf-8")

            wiki.build_source_catalog(raw_dir, output_dir)

            self.assertFalse(stale.exists())
            self.assertTrue(manual.exists())

    def test_duplicate_document_id_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_raw(root, "api-spec.md", "doc-same", "API")
            self.write_raw(root, "release-policy.md", "doc-same", "Release")

            with self.assertRaises(ValueError):
                wiki.build_source_catalog(root / "knowledge" / "raw", root / "wiki")


if __name__ == "__main__":
    unittest.main()
