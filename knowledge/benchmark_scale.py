#!/usr/bin/env python3
"""Measure existing ingest and FTS5 paths in a fresh process per corpus size."""

from __future__ import annotations

import argparse
import gc
import hashlib
import json
import math
import os
import platform
import resource
import sqlite3
import statistics
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from ingest import DEFAULT_TOKENIZER, PROJECT_ROOT, build_manifest
from retrieve import _match_query, build_index, search


def raw_fingerprint(paths: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in paths:
        digest.update(path.name.encode("utf-8") + b"\0")
        digest.update(hashlib.sha256(path.read_bytes()).digest())
    return digest.hexdigest()


def latency_stats(samples: list[float]) -> dict:
    ordered = sorted(samples)
    return {
        "samples": len(samples),
        "min_ms": ordered[0],
        "p50_ms": statistics.median(ordered),
        "p95_ms": ordered[math.ceil(0.95 * len(ordered)) - 1],
        "max_ms": ordered[-1],
    }


def peak_rss_bytes() -> int:
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform == "darwin":
        return peak
    if sys.platform.startswith("linux"):
        return peak * 1024
    raise RuntimeError("峰值 RSS 單位只支援 macOS 與 Linux")


def load_queries(path: Path) -> list[dict]:
    queries = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(queries, list) or not queries:
        raise ValueError("queries 必須是非空的 JSON array")
    ids = set()
    for item in queries:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            raise ValueError("每筆 query 需要字串 id")
        if not item["id"] or item["id"] in ids:
            raise ValueError("query id 必須非空且不可重複")
        if not isinstance(item.get("query"), str):
            raise ValueError("每筆 query 需要字串 query")
        _match_query(item["query"])
        ids.add(item["id"])
    return queries


def measure_size(args: argparse.Namespace, size: int) -> dict:
    selected = sorted(args.raw_dir.glob("*.md"))[:size]
    if len(selected) != size:
        raise ValueError("指定的文件數超過 raw 文件數")
    before = raw_fingerprint(selected)
    directory = args.workspace_root / f"documents-{size}"
    directory.mkdir(exist_ok=False)
    manifest_path = directory / "manifest.json"
    database_path = directory / "retrieval.sqlite"

    started = time.perf_counter()
    manifest = build_manifest(
        args.raw_dir, manifest_path, tokenizer_name=args.tokenizer,
        max_tokens=args.max_tokens, overlap_tokens=args.overlap_tokens,
        document_limit=size,
    )
    ingest_seconds = time.perf_counter() - started
    chunk_count = sum(doc["chunk_count"] for doc in manifest["documents"])
    # The next stage already reloads the manifest. Do not retain an extra copy.
    del manifest
    gc.collect()

    started = time.perf_counter()
    indexed = build_index(manifest_path, database_path)
    index_seconds = time.perf_counter() - started
    if indexed["document_count"] != size or indexed["chunk_count"] != chunk_count:
        raise ValueError("manifest 與 FTS5 文件／chunk 數不一致")

    queries = load_queries(args.queries)
    expected = {}
    for item in queries:
        expected[item["id"]] = search(database_path, item["query"], limit=args.limit)
    results = {item["id"]: [] for item in queries}
    for _ in range(args.rounds):
        for item in queries:
            started = time.perf_counter()
            matches = search(database_path, item["query"], limit=args.limit)
            elapsed_ms = (time.perf_counter() - started) * 1000
            if matches != expected[item["id"]]:
                raise ValueError("相同索引重查得到不同結果")
            results[item["id"]].append(elapsed_ms)

    with sqlite3.connect(database_path) as connection:
        if connection.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
            raise ValueError("SQLite integrity_check 失敗")
        connection.execute("INSERT INTO chunks_fts(chunks_fts) VALUES ('integrity-check')")
    if raw_fingerprint(selected) != before:
        raise ValueError("量測期間 raw 文件被修改")
    return {
        "document_count": size,
        "raw_bytes": sum(path.stat().st_size for path in selected),
        "selected_raw_files": [path.name for path in selected],
        "raw_fingerprint": before,
        "chunk_count": chunk_count,
        "ingest_seconds": ingest_seconds,
        "fts_build_seconds": index_seconds,
        "manifest_bytes": manifest_path.stat().st_size,
        "database_bytes": database_path.stat().st_size,
        "peak_rss_bytes": peak_rss_bytes(),
        "query_latency": latency_stats([v for samples in results.values() for v in samples]),
        "queries": [
            {
                **item,
                "returned_chunks": len(expected[item["id"]]),
                "top_chunk_ids": [match["chunk_id"] for match in expected[item["id"]]],
                "latency": latency_stats(results[item["id"]]),
                "samples_ms": results[item["id"]],
            }
            for item in queries
        ],
        "integrity_check": "ok",
        "fts_integrity_check": "ok",
        "raw_unchanged": True,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="量測固定 raw 語料的切塊、FTS5 建置與查詢。")
    parser.add_argument("--raw-dir", type=Path, default=PROJECT_ROOT / "data/day23/results/raw")
    parser.add_argument("--workspace-root", type=Path, default=PROJECT_ROOT / "data/day24/reproduction")
    parser.add_argument("--queries", type=Path, default=PROJECT_ROOT / "data/day24-queries.json")
    parser.add_argument("--sizes", type=int, nargs="+", default=[100, 500, 1720])
    parser.add_argument("--tokenizer", default=DEFAULT_TOKENIZER)
    parser.add_argument("--max-tokens", type=int, default=160)
    parser.add_argument("--overlap-tokens", type=int, default=24)
    parser.add_argument("--rounds", type=int, default=20)
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--worker-size", type=int, help=argparse.SUPPRESS)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.rounds <= 0 or args.limit <= 0:
            raise ValueError("rounds 與 limit 必須大於 0")
        if args.max_tokens <= 0 or not 0 <= args.overlap_tokens < args.max_tokens:
            raise ValueError("切塊設定不合法")
        if args.worker_size is not None:
            print(json.dumps(measure_size(args, args.worker_size), ensure_ascii=False))
            return 0
        raw_paths = sorted(args.raw_dir.glob("*.md"))
        if not args.sizes or len(set(args.sizes)) != len(args.sizes):
            raise ValueError("sizes 必須非空且不可重複")
        if any(size <= 0 or size > len(raw_paths) for size in args.sizes):
            raise ValueError("sizes 必須大於 0 且不可超過 raw 文件數")
        queries = load_queries(args.queries)
        before = raw_fingerprint(raw_paths)
        query_sha = hashlib.sha256(args.queries.read_bytes()).hexdigest()
        # Each run needs a new directory, so existing results cannot be overwritten.
        args.workspace_root.mkdir(parents=True, exist_ok=False)
        measurements = []
        for size in args.sizes:
            print(f"量測 {size} 份文件……", file=sys.stderr, flush=True)
            worker = subprocess.run(
                [
                    sys.executable, str(Path(__file__).resolve()),
                    "--worker-size", str(size), "--raw-dir", str(args.raw_dir.resolve()),
                    "--workspace-root", str(args.workspace_root.resolve()),
                    "--queries", str(args.queries.resolve()), "--tokenizer", args.tokenizer,
                    "--max-tokens", str(args.max_tokens), "--overlap-tokens", str(args.overlap_tokens),
                    "--rounds", str(args.rounds), "--limit", str(args.limit),
                ],
                env={**os.environ, "HF_HUB_OFFLINE": "1", "TOKENIZERS_PARALLELISM": "false"},
                capture_output=True, text=True, check=True,
            )
            measurement = json.loads(worker.stdout)
            measurements.append(measurement)
            print(
                f"{size} 份／{measurement['chunk_count']} chunks："
                f"切塊 {measurement['ingest_seconds']:.3f} 秒，"
                f"FTS5 {measurement['fts_build_seconds']:.3f} 秒，"
                f"查詢 p95 {measurement['query_latency']['p95_ms']:.3f} ms",
                flush=True,
            )
        if before != raw_fingerprint(raw_paths) or query_sha != hashlib.sha256(args.queries.read_bytes()).hexdigest():
            raise ValueError("量測期間輸入資料改變")
        report = {
            "measured_at_utc": datetime.now(timezone.utc).isoformat(),
            "environment": {
                "platform": platform.platform(), "python": platform.python_version(),
                "sqlite": sqlite3.sqlite_version,
            },
            "configuration": {
                "tokenizer": args.tokenizer, "max_tokens": args.max_tokens,
                "overlap_tokens": args.overlap_tokens, "sizes": args.sizes,
                "selection": "sorted raw filename prefixes",
                "query_rounds": args.rounds, "query_limit": args.limit,
                "warmups_per_query": 1, "queries_sha256": query_sha,
                "queries": queries, "raw_fingerprint": before,
                "build_repetitions_per_size": 1,
                "query_timing_scope": "search(): query parsing, new SQLite connection, MATCH, BM25 sort, fetch, Python result conversion, close",
                "p50_method": "statistics.median", "p95_method": "nearest rank: ceil(0.95 * N)",
                "rss_scope": "fresh worker lifetime; includes tokenizer, ingest, FTS build, queries, integrity checks",
            },
            "measurements": measurements,
            "inputs_unchanged": True,
        }
        report_path = args.workspace_root / "summary.json"
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"結果：{report_path}")
    except subprocess.CalledProcessError as error:
        print(error.stderr, file=sys.stderr)
        return 1
    except (OSError, RuntimeError, ValueError, sqlite3.Error) as error:
        print(f"量測失敗：{error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
