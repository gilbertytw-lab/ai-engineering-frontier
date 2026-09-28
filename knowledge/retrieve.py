#!/usr/bin/env python3
"""Build and query a deterministic SQLite FTS5 index from the chunk manifest."""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from contextlib import closing
from pathlib import Path
from typing import Any, Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = PROJECT_ROOT / "knowledge" / "index" / "manifest.json"
DEFAULT_DATABASE = PROJECT_ROOT / "knowledge" / "index" / "retrieval.sqlite"
INDEX_VERSION = "0.1.0"


def load_manifest(path: Path) -> dict[str, Any]:
    """Read a manifest without modifying the source documents."""

    manifest = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict) or not isinstance(manifest.get("documents"), list):
        raise ValueError(f"manifest 格式不支援：{path}")
    return manifest


def iter_chunks(manifest: dict[str, Any]) -> Iterable[dict[str, Any]]:
    """Yield chunks with the document metadata needed by the retriever."""

    for document in manifest["documents"]:
        required_document = ("document_id", "source_name", "raw_path")
        if any(key not in document for key in required_document):
            raise ValueError("manifest 文件層缺少必要欄位")
        for chunk in document.get("chunks", []):
            required_chunk = (
                "chunk_id",
                "start_line",
                "end_line",
                "token_count",
                "text_sha256",
                "text",
            )
            if any(key not in chunk for key in required_chunk):
                raise ValueError("manifest chunk 缺少必要欄位")
            yield {
                "chunk_id": chunk["chunk_id"],
                "document_id": document["document_id"],
                "source_name": document["source_name"],
                "raw_path": document["raw_path"],
                "start_line": chunk["start_line"],
                "end_line": chunk["end_line"],
                "token_count": chunk["token_count"],
                "text_sha256": chunk["text_sha256"],
                "text": chunk["text"],
            }


def _create_schema(connection: sqlite3.Connection) -> None:
    connection.executescript(
        """
        DROP TABLE IF EXISTS chunks_fts;
        DROP TABLE IF EXISTS index_meta;

        CREATE VIRTUAL TABLE chunks_fts USING fts5(
            chunk_id UNINDEXED,
            document_id UNINDEXED,
            source_name,
            raw_path UNINDEXED,
            start_line UNINDEXED,
            end_line UNINDEXED,
            token_count UNINDEXED,
            text_sha256 UNINDEXED,
            text,
            search_text,
            tokenize = 'unicode61 remove_diacritics 2'
        );

        CREATE TABLE index_meta (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );
        """
    )


def _searchable_text(text: str) -> str:
    """Add boundaries between CJK characters for SQLite's unicode61 tokenizer."""

    return re.sub(r"([\u3400-\u9fff])", r" \1 ", text)


def build_index(manifest_path: Path, database_path: Path) -> dict[str, Any]:
    """Rebuild the SQLite FTS5 database from one manifest."""

    manifest = load_manifest(manifest_path)
    chunks = list(iter_chunks(manifest))
    database_path.parent.mkdir(parents=True, exist_ok=True)

    with closing(sqlite3.connect(database_path)) as connection, connection:
        _create_schema(connection)
        connection.executemany(
            """
            INSERT INTO chunks_fts (
                chunk_id, document_id, source_name, raw_path,
                start_line, end_line, token_count, text_sha256, text, search_text
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                (
                    chunk["chunk_id"],
                    chunk["document_id"],
                    chunk["source_name"],
                    chunk["raw_path"],
                    chunk["start_line"],
                    chunk["end_line"],
                    chunk["token_count"],
                    chunk["text_sha256"],
                    chunk["text"],
                    _searchable_text(f"{chunk['source_name']}\n{chunk['text']}"),
                )
                for chunk in chunks
            ],
        )
        connection.executemany(
            "INSERT INTO index_meta (key, value) VALUES (?, ?)",
            [
                ("index_version", INDEX_VERSION),
                ("manifest_version", str(manifest.get("manifest_version", ""))),
                ("tokenizer", str(manifest.get("tokenizer", ""))),
                ("chunking", json.dumps(manifest.get("chunking", {}), sort_keys=True)),
                ("chunk_count", str(len(chunks))),
            ],
        )
        connection.execute("INSERT INTO chunks_fts(chunks_fts) VALUES ('optimize')")

    return {
        "database": database_path,
        "manifest": manifest_path,
        "chunk_count": len(chunks),
        "document_count": len(manifest["documents"]),
    }


def _match_query(query: str) -> str:
    """Turn user text into a small, parameter-safe FTS5 AND query.

    Operators are intentionally not exposed in this first retriever. A query is
    treated as a list of words or CJK runs, and every term must be present.
    """

    terms = re.findall(r"[A-Za-z0-9_]+|[\u3400-\u9fff]+", query)
    if not terms:
        raise ValueError("query 必須包含至少一個可搜尋的字詞")
    rendered_terms = []
    for term in terms:
        if re.fullmatch(r"[\u3400-\u9fff]+", term):
            term = " ".join(term)
        rendered_terms.append('"' + term.replace('"', '""') + '"')
    return " AND ".join(rendered_terms)


def search(database_path: Path, query: str, *, limit: int = 5) -> list[dict[str, Any]]:
    """Return BM25-ranked chunks, with source locations preserved."""

    if limit <= 0:
        raise ValueError("limit 必須大於 0")
    match_query = _match_query(query)
    with closing(sqlite3.connect(database_path)) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            """
            SELECT
                chunk_id, document_id, source_name, raw_path,
                start_line, end_line, token_count, text_sha256, text,
                bm25(chunks_fts) AS rank
            FROM chunks_fts
            WHERE chunks_fts MATCH ?
            ORDER BY rank ASC, chunk_id ASC
            LIMIT ?
            """,
            (match_query, limit),
        ).fetchall()

    return [
        {
            "chunk_id": row["chunk_id"],
            "document_id": row["document_id"],
            "source_name": row["source_name"],
            "raw_path": row["raw_path"],
            "start_line": int(row["start_line"]),
            "end_line": int(row["end_line"]),
            "token_count": int(row["token_count"]),
            "text_sha256": row["text_sha256"],
            "text": row["text"],
            "bm25": round(-float(row["rank"]), 8),
        }
        for row in rows
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="從 chunk manifest 建立 SQLite FTS5 關鍵字索引並查詢。"
    )
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    parser.add_argument("--query", help="要搜尋的關鍵字；多個字詞會以 AND 查詢")
    parser.add_argument("--limit", type=int, default=5)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        result = build_index(args.manifest, args.database)
        print(
            f"建立 {args.database}：{result['document_count']} 份文件、"
            f"{result['chunk_count']} 個 chunks"
        )
        if args.query:
            matches = search(args.database, args.query, limit=args.limit)
            print(f"查詢：{args.query}")
            print(f"命中 {len(matches)} 個 chunks")
            for number, match in enumerate(matches, start=1):
                location = f"第 {match['start_line']}–{match['end_line']} 行"
                print(
                    f"{number}. {match['source_name']}（{location}，"
                    f"bm25={match['bm25']:.6f}，{match['chunk_id']}）"
                )
    except (OSError, ValueError, sqlite3.Error) as error:
        print(f"retrieval 失敗：{error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
