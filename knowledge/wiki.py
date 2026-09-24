#!/usr/bin/env python3
"""Build a deterministic, source-linked catalog for canonical raw Markdown."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RAW_DIR = PROJECT_ROOT / "knowledge" / "raw"
DEFAULT_WIKI_DIR = PROJECT_ROOT / "knowledge" / "wiki"
WIKI_VERSION = "0.1.0"
GENERATED_BY = "knowledge/wiki.py"


def parse_raw_document(path: Path) -> dict[str, Any]:
    """Read raw frontmatter and the first Markdown heading."""

    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"raw 檔缺少 YAML frontmatter：{path}")

    closing_marker = text.find("\n---\n", 4)
    if closing_marker < 0:
        raise ValueError(f"raw 檔的 frontmatter 沒有結束標記：{path}")

    metadata: dict[str, str] = {}
    for line in text[4:closing_marker].splitlines():
        match = re.fullmatch(r"([A-Za-z0-9_]+): \"(.*)\"", line)
        if not match:
            raise ValueError(f"raw frontmatter 格式不支援：{path}：{line}")
        metadata[match.group(1)] = match.group(2)

    required = {"document_id", "source_name", "source_snapshot"}
    missing = sorted(required - metadata.keys())
    if missing:
        raise ValueError(f"raw frontmatter 缺少欄位：{path}：{', '.join(missing)}")

    body = text[closing_marker + len("\n---\n") :]
    heading = next(
        (match.group(1).strip() for line in body.splitlines() if (match := re.match(r"^#\s+(.+?)\s*$", line))),
        metadata["source_name"],
    )
    return {
        "path": path,
        "metadata": metadata,
        "title": heading,
    }


def _relative_project_path(path: Path) -> str:
    if path.is_relative_to(PROJECT_ROOT):
        return path.relative_to(PROJECT_ROOT).as_posix()
    return path.as_posix()


def _yaml_value(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _frontmatter(fields: list[tuple[str, str]]) -> str:
    lines = ["---"]
    lines.extend(f"{key}: {_yaml_value(value)}" for key, value in fields)
    lines.extend(["---", ""])
    return "\n".join(lines)


def _page_filename(document_id: str) -> str:
    safe_name = re.sub(r"[^A-Za-z0-9._-]+", "-", document_id).strip("-")
    if not safe_name:
        raise ValueError(f"document_id 無法轉成頁面檔名：{document_id}")
    return f"{safe_name}.md"


def _render_source_page(document: dict[str, Any], page_filename: str) -> str:
    metadata = document["metadata"]
    raw_path = document["path"]
    raw_link = f"../../raw/{raw_path.name}"
    fields = [
        ("page_type", "source"),
        ("generated_by", GENERATED_BY),
        ("generator_version", WIKI_VERSION),
        ("document_id", metadata["document_id"]),
        ("source_name", metadata["source_name"]),
        ("raw_path", _relative_project_path(raw_path)),
        ("source_snapshot", metadata["source_snapshot"]),
    ]
    for key in ("source_sha256", "extracted_sha256", "conversion_method", "converter_version"):
        if key in metadata:
            fields.append((key, metadata[key]))

    return (
        _frontmatter(fields)
        + f"# {document['title']}\n\n"
        + "這是一頁由 `knowledge/wiki.py` 根據 `knowledge/raw/` 自動產生的來源索引。"
        + "原始內容與證據仍以 raw 文件為準。\n\n"
        + "## 來源\n\n"
        + f"- 文件名稱：`{metadata['source_name']}`\n"
        + f"- 文件 ID：`{metadata['document_id']}`\n"
        + f"- 原始文件：[開啟 raw 文件]({raw_link})\n"
        + f"- 原始快照：`{metadata['source_snapshot']}`\n"
        + "\n"
        + "這個頁面只提供導覽與 provenance，不複製 raw 正文，也不要求使用者另外分類文件。\n"
    )


def _is_generated(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return False
    return f'generated_by: "{GENERATED_BY}"' in text.split("\n---\n", 1)[0]


def _render_index(documents: list[dict[str, Any]]) -> str:
    fields = [
        ("page_type", "index"),
        ("generated_by", GENERATED_BY),
        ("generator_version", WIKI_VERSION),
        ("source_count", str(len(documents))),
    ]
    lines = [
        _frontmatter(fields),
        "# Knowledge source index",
        "",
        "這份索引由 `knowledge/wiki.py` 根據 `knowledge/raw/` 自動產生。",
        "它只負責列出來源文件，不取代 raw、chunk manifest 或 FTS5 索引。",
        "",
        "## Sources",
        "",
    ]
    for document in documents:
        metadata = document["metadata"]
        filename = _page_filename(metadata["document_id"])
        lines.extend(
            [
                f"- [{document['title']}](sources/{filename})",
                f"  - source name：`{metadata['source_name']}`",
                f"  - document ID：`{metadata['document_id']}`",
                f"  - raw path：`{_relative_project_path(document['path'])}`",
            ]
        )
    return "\n".join(lines) + "\n"


def build_source_catalog(raw_dir: Path, output_dir: Path) -> dict[str, Any]:
    """Rebuild generated source pages and the source index from raw Markdown."""

    raw_paths = sorted(raw_dir.glob("*.md"))
    if not raw_paths:
        raise ValueError(f"找不到 raw Markdown：{raw_dir}")

    documents = [parse_raw_document(path) for path in raw_paths]
    document_ids = [document["metadata"]["document_id"] for document in documents]
    if len(document_ids) != len(set(document_ids)):
        raise ValueError("raw 文件含有重複的 document_id")

    source_dir = output_dir / "sources"
    source_dir.mkdir(parents=True, exist_ok=True)
    for path in source_dir.glob("*.md"):
        if _is_generated(path):
            path.unlink()

    for document in documents:
        page_filename = _page_filename(document["metadata"]["document_id"])
        (source_dir / page_filename).write_text(
            _render_source_page(document, page_filename),
            encoding="utf-8",
            newline="\n",
        )

    index_path = output_dir / "index.md"
    if index_path.exists() and not _is_generated(index_path):
        raise ValueError(f"不覆寫非 wiki.py 產生的索引：{index_path}")
    index_path.write_text(_render_index(documents), encoding="utf-8", newline="\n")
    return {
        "raw_dir": raw_dir,
        "output_dir": output_dir,
        "document_count": len(documents),
        "source_page_count": len(documents),
        "index": index_path,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="從 knowledge/raw 自動產生可回查來源的 wiki source catalog。"
    )
    parser.add_argument("--raw-dir", type=Path, default=DEFAULT_RAW_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_WIKI_DIR)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        result = build_source_catalog(args.raw_dir, args.output_dir)
    except (OSError, ValueError) as error:
        print(f"wiki 失敗：{error}", file=sys.stderr)
        return 1

    print(
        f"建立 {result['output_dir']}：{result['document_count']} 份來源、"
        f"{result['source_page_count']} 個 source pages、index.md"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
