#!/usr/bin/env python3
"""Verify raw Markdown fields and body against its saved source snapshot."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from convert import Source, VERSION, document_id, extract

REQUIRED = {
    "document_id", "source_name", "source_type", "source_format", "source_sha256",
    "source_snapshot", "extracted_sha256", "conversion_method", "converter_version",
}
OPTIONAL = {"source_url", "source_charset", "pdf_pages", "extraction_scope"}
SUFFIX = {"txt": ".txt", "md": ".md", "markdown": ".markdown", "pdf": ".pdf", "html": ".html"}


def validate_file(path: Path, root: Path) -> tuple[str, int | None]:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---\n") or "\n---\n\n" not in raw[4:]:
        raise ValueError("缺少 YAML frontmatter 或 Markdown 正文")
    header, body = raw[4:].split("\n---\n\n", 1)
    fields: dict[str, object] = {}
    for line in header.splitlines():
        key, separator, value = line.partition(": ")
        if not separator or not key or key in fields:
            raise ValueError(f"來源欄位無法解析或重複：{line}")
        try:
            fields[key] = json.loads(value)
        except json.JSONDecodeError as error:
            raise ValueError(f"來源欄位不是可解析的值：{key}") from error
    if set(fields) - (REQUIRED | OPTIONAL) or REQUIRED - set(fields):
        raise ValueError("來源欄位與 raw 格式契約不符")
    for key in REQUIRED - {"conversion_method", "converter_version"}:
        if not isinstance(fields[key], str) or not fields[key]:
            raise ValueError(f"來源欄位不是非空字串：{key}")
    for key in ("source_url", "source_charset", "extraction_scope"):
        if key in fields and (not isinstance(fields[key], str) or not fields[key]):
            raise ValueError(f"來源欄位不是非空字串：{key}")
    if "pdf_pages" in fields and (type(fields["pdf_pages"]) is not int or fields["pdf_pages"] < 1):
        raise ValueError("PDF 頁數欄位不合法")
    if fields["conversion_method"] != "programmatic" or fields["converter_version"] != VERSION:
        raise ValueError("轉換方法或版本與現行工具不符")
    if fields["source_format"] not in SUFFIX:
        raise ValueError("來源格式不支援")
    expected_kind = "pdf" if fields["source_format"] == "pdf" else "web" if fields["source_format"] == "html" else "text"
    if fields["source_type"] != expected_kind:
        raise ValueError("來源類型與格式不一致")
    snapshot = Path(fields["source_snapshot"])
    if not snapshot.is_absolute():
        snapshot = root / snapshot
    if not snapshot.is_file():
        raise ValueError(f"找不到來源快照：{snapshot}")
    data = snapshot.read_bytes()
    source = Source(data, fields["source_name"], expected_kind, fields["source_format"],
                    SUFFIX[fields["source_format"]], fields.get("source_charset", "utf-8"),
                    fields.get("source_url"))
    extracted = extract(source)
    expected = {
        "source_sha256": hashlib.sha256(data).hexdigest(),
        "extracted_sha256": hashlib.sha256(extracted.identity_text.encode("utf-8")).hexdigest(),
        "document_id": document_id(source, extracted.identity_text),
    }
    for key, value in expected.items():
        if fields[key] != value:
            raise ValueError(f"{key} 與來源快照不一致")
    if path.name != f'{fields["document_id"]}.md':
        raise ValueError("檔名與 document_id 不一致")
    if body != extracted.body:
        raise ValueError("Markdown 正文與來源抽取結果不一致")
    if extracted.pages is not None:
        if fields.get("pdf_pages") != extracted.pages or not isinstance(fields.get("extraction_scope"), str):
            raise ValueError("PDF 頁數或抽取範圍欄位不符")
    elif "pdf_pages" in fields or "extraction_scope" in fields:
        raise ValueError("非 PDF 來源不應有 PDF 欄位")
    return fields["document_id"], extracted.pages


def main() -> int:
    parser = argparse.ArgumentParser(description="核對 raw Markdown 的格式、正文、欄位與保存原件。")
    parser.add_argument("raw_dir", type=Path, help="包含轉換後 Markdown 的目錄")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="解析相對來源快照路徑的根目錄")
    args = parser.parse_args()
    files = sorted(args.raw_dir.glob("*.md"))
    if not files:
        parser.error("raw 目錄沒有 Markdown 檔")
    failures = 0
    for path in files:
        try:
            doc_id, pages = validate_file(path, args.root)
        except (OSError, UnicodeError, ValueError, RuntimeError) as error:
            print(f"FAIL {path}: {error}", file=sys.stderr)
            failures += 1
        else:
            print(f"OK {doc_id}" + (f" ({pages} 頁)" if pages is not None else ""))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
