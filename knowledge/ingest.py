#!/usr/bin/env python3
"""Build a deterministic, source-linked chunk manifest from canonical raw Markdown."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RAW_DIR = PROJECT_ROOT / "knowledge" / "raw"
DEFAULT_MANIFEST = PROJECT_ROOT / "knowledge" / "index" / "manifest.json"
DEFAULT_TOKENIZER = "mlx-community/Qwen3.8-27B-4bit"
MANIFEST_VERSION = "0.1.0"


@dataclass(frozen=True)
class RawDocument:
    path: Path
    metadata: dict[str, str]
    body: str
    body_start_line: int
    raw_sha256: str


@dataclass(frozen=True)
class LinePiece:
    text: str
    start_line: int
    end_line: int


class Tokenizer:
    """Small wrapper so ingest and measurement use exactly the same counter."""

    def __init__(
        self, name: str, *, chat_template_kwargs: dict[str, Any] | None = None
    ) -> None:
        try:
            from transformers import AutoTokenizer
        except ImportError as error:  # pragma: no cover - environment failure
            raise RuntimeError(
                "找不到 transformers；請先用 uv sync 安裝專案依賴。"
            ) from error

        try:
            self._tokenizer = AutoTokenizer.from_pretrained(
                name,
                local_files_only=True,
                trust_remote_code=True,
                use_fast=True,
            )
        except Exception as error:  # transformers raises several model-specific types
            raise RuntimeError(
                f"無法從本機快取載入 tokenizer：{name}；"
                "本命令不會自動下載模型，請確認快取或用 --tokenizer 指定路徑。"
            ) from error
        self.name = name
        self.chat_template_kwargs = dict(chat_template_kwargs or {})

    def encode(self, text: str) -> list[int]:
        return list(self._tokenizer.encode(text, add_special_tokens=False))

    def count(self, text: str) -> int:
        return len(self.encode(text))

    def chat_count(self, messages: list[dict[str, str]]) -> int:
        try:
            encoded = self._tokenizer.apply_chat_template(
                messages,
                tokenize=True,
                add_generation_prompt=True,
                **self.chat_template_kwargs,
            )
            if hasattr(encoded, "get") and encoded.get("input_ids") is not None:
                input_ids = encoded["input_ids"]
                if input_ids and isinstance(input_ids[0], list):
                    return len(input_ids[0])
                return len(input_ids)
            return len(encoded)
        except (AttributeError, TypeError, ValueError):
            return sum(self.count(message["content"]) for message in messages)

    def decode(self, tokens: list[int]) -> str:
        return self._tokenizer.decode(tokens, skip_special_tokens=False)


def parse_raw_document(path: Path) -> RawDocument:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"raw 檔缺少 YAML frontmatter：{path}")

    closing_marker = text.find("\n---\n", 4)
    if closing_marker < 0:
        raise ValueError(f"raw 檔的 frontmatter 沒有結束標記：{path}")

    header = text[4:closing_marker]
    metadata: dict[str, str] = {}
    for line in header.splitlines():
        match = re.fullmatch(r"([A-Za-z0-9_]+): \"(.*)\"", line)
        if not match:
            raise ValueError(f"raw frontmatter 格式不支援：{path}：{line}")
        metadata[match.group(1)] = match.group(2)

    body_start = closing_marker + len("\n---\n")
    body = text[body_start:]
    if not body.strip():
        raise ValueError(f"raw 檔沒有正文：{path}")

    required = {"document_id", "source_name", "source_snapshot"}
    missing = sorted(required - metadata.keys())
    if missing:
        raise ValueError(f"raw frontmatter 缺少欄位：{path}：{', '.join(missing)}")

    body_start_line = text[:body_start].count("\n") + 1
    return RawDocument(
        path=path,
        metadata=metadata,
        body=body,
        body_start_line=body_start_line,
        raw_sha256=hashlib.sha256(text.encode("utf-8")).hexdigest(),
    )


def _line_pieces(document: RawDocument) -> list[LinePiece]:
    lines = document.body.splitlines(keepends=True)
    if not lines:
        lines = [document.body]
    pieces: list[LinePiece] = []
    for offset, line in enumerate(lines):
        pieces.append(
            LinePiece(
                text=line,
                start_line=document.body_start_line + offset,
                end_line=document.body_start_line + offset,
            )
        )
    return pieces


def _split_long_piece(piece: LinePiece, tokenizer: Tokenizer, max_tokens: int) -> list[LinePiece]:
    tokens = tokenizer.encode(piece.text)
    if len(tokens) <= max_tokens:
        return [piece]
    result: list[LinePiece] = []
    for offset in range(0, len(tokens), max_tokens):
        result.append(
            LinePiece(
                text=tokenizer.decode(tokens[offset : offset + max_tokens]),
                start_line=piece.start_line,
                end_line=piece.end_line,
            )
        )
    return result


def chunk_document(
    document: RawDocument,
    tokenizer: Tokenizer,
    *,
    max_tokens: int,
    overlap_tokens: int,
) -> list[dict[str, Any]]:
    if max_tokens <= 0:
        raise ValueError("max_tokens 必須大於 0")
    if overlap_tokens < 0 or overlap_tokens >= max_tokens:
        raise ValueError("overlap_tokens 必須介於 0 和 max_tokens - 1 之間")

    pieces: list[LinePiece] = []
    for piece in _line_pieces(document):
        pieces.extend(_split_long_piece(piece, tokenizer, max_tokens))

    chunks: list[dict[str, Any]] = []
    cursor = 0
    while cursor < len(pieces):
        start = cursor
        total = 0
        while cursor < len(pieces):
            piece_tokens = tokenizer.count(pieces[cursor].text)
            if total and total + piece_tokens > max_tokens:
                break
            total += piece_tokens
            cursor += 1

        selected = pieces[start:cursor]
        text = "".join(piece.text for piece in selected)
        chunks.append(
            {
                "chunk_id": f"{document.metadata['document_id']}-chunk-{len(chunks) + 1:04d}",
                "start_line": selected[0].start_line,
                "end_line": selected[-1].end_line,
                "token_count": tokenizer.count(text),
                "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
                "text": text,
            }
        )

        if cursor >= len(pieces):
            break
        if overlap_tokens == 0:
            continue

        overlap = 0
        overlap_start = cursor
        while overlap_start > start:
            candidate = tokenizer.count(pieces[overlap_start - 1].text)
            if overlap + candidate > overlap_tokens:
                break
            overlap += candidate
            overlap_start -= 1
        cursor = max(start + 1, overlap_start)

    return chunks


def build_manifest(
    raw_dir: Path,
    output: Path,
    *,
    tokenizer_name: str = DEFAULT_TOKENIZER,
    max_tokens: int = 256,
    overlap_tokens: int = 32,
) -> dict[str, Any]:
    tokenizer = Tokenizer(tokenizer_name)
    raw_paths = sorted(raw_dir.glob("*.md"))
    if not raw_paths:
        raise ValueError(f"找不到 raw Markdown：{raw_dir}")

    documents: list[dict[str, Any]] = []
    for path in raw_paths:
        document = parse_raw_document(path)
        chunks = chunk_document(
            document,
            tokenizer,
            max_tokens=max_tokens,
            overlap_tokens=overlap_tokens,
        )
        documents.append(
            {
                "document_id": document.metadata["document_id"],
                "source_name": document.metadata["source_name"],
                "source_snapshot": document.metadata["source_snapshot"],
                "raw_path": path.relative_to(PROJECT_ROOT).as_posix()
                if path.is_relative_to(PROJECT_ROOT)
                else path.as_posix(),
                "raw_sha256": document.raw_sha256,
                "source_sha256": document.metadata.get("source_sha256"),
                "chunk_count": len(chunks),
                "chunks": chunks,
            }
        )

    manifest = {
        "manifest_version": MANIFEST_VERSION,
        "tokenizer": tokenizer_name,
        "chunking": {
            "max_tokens": max_tokens,
            "overlap_tokens": overlap_tokens,
            "boundary": "line_then_token_slice",
        },
        "documents": documents,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    rendered = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    output.write_text(rendered, encoding="utf-8", newline="\n")
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="將 knowledge/raw 的來源 Markdown 分成有來源位置的 deterministic chunks。"
    )
    parser.add_argument("--raw-dir", type=Path, default=DEFAULT_RAW_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--tokenizer", default=DEFAULT_TOKENIZER)
    parser.add_argument("--max-tokens", type=int, default=256)
    parser.add_argument("--overlap-tokens", type=int, default=32)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        manifest = build_manifest(
            args.raw_dir,
            args.output,
            tokenizer_name=args.tokenizer,
            max_tokens=args.max_tokens,
            overlap_tokens=args.overlap_tokens,
        )
    except (OSError, RuntimeError, ValueError) as error:
        print(f"ingest 失敗：{error}", file=sys.stderr)
        return 1

    document_count = len(manifest["documents"])
    chunk_count = sum(document["chunk_count"] for document in manifest["documents"])
    print(f"建立 {args.output}：{document_count} 份文件、{chunk_count} 個 chunks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
