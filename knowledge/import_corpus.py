#!/usr/bin/env python3
"""Import a pinned Markdown corpus with the existing, model-free converter."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from pathlib import Path
from urllib.parse import quote, urlsplit

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "skills" / "source-to-raw-md" / "scripts"))

from batch import convert_selected_source  # noqa: E402
from convert import VERSION, document_id, extract, read_source  # noqa: E402
from validate import validate_file  # noqa: E402


def corpus_checksum(source_dir: Path) -> tuple[list[Path], str]:
    files = sorted(source_dir.rglob("*.md"))
    digest = hashlib.sha256()
    for path in files:
        if path.is_symlink() or not path.resolve().is_relative_to(source_dir.resolve()):
            raise ValueError(f"來源必須是目錄內的實際檔案：{path}")
        relative = path.relative_to(source_dir).as_posix().encode("utf-8")
        data = path.read_bytes()
        digest.update(len(relative).to_bytes(8, "big"))
        digest.update(relative)
        digest.update(len(data).to_bytes(8, "big"))
        digest.update(data)
    if not files:
        raise ValueError("來源目錄沒有 Markdown 檔")
    return files, digest.hexdigest()


def import_corpus(
    source_dir: Path, workspace_root: Path, source_base_url: str, expected_checksum: str
) -> dict:
    started = time.perf_counter()
    source_dir = source_dir.resolve()
    workspace_root = workspace_root.resolve()
    if (source_dir.is_relative_to(workspace_root)
            or workspace_root.is_relative_to(source_dir)):
        raise ValueError("來源目錄與匯入工作區不能互相包含")
    url = urlsplit(source_base_url)
    if url.scheme not in {"http", "https"} or not url.netloc or url.query or url.fragment:
        raise ValueError("來源網址須為不含 query 或 fragment 的 HTTP/HTTPS 目錄網址")
    files, checksum = corpus_checksum(source_dir)
    if checksum != expected_checksum:
        raise ValueError(f"語料 checksum 不符：預期 {expected_checksum}，實際 {checksum}")

    inbox = workspace_root / "knowledge" / "inbox"
    processed = inbox / "processed"
    raw_dir = workspace_root / "knowledge" / "raw"
    records = []
    outputs: set[Path] = set()
    for path in files:
        file_started = time.perf_counter()
        relative = path.relative_to(source_dir)
        data = path.read_bytes()
        metadata = json.dumps({
            "source_name": relative.as_posix(),
            "source_url": source_base_url.rstrip("/") + "/" + quote(relative.as_posix()),
            "charset": "utf-8",
        }, ensure_ascii=False, indent=2) + "\n"
        pending = inbox / "corpus" / relative
        saved = processed / "corpus" / relative
        record = {"source_path": relative.as_posix(), "source_bytes": len(data),
                  "source_sha256": hashlib.sha256(data).hexdigest()}
        try:
            if saved.exists():
                if saved.read_bytes() != data:
                    raise ValueError("已保存的原檔與本次語料不同，請另選工作區")
                sidecar = saved.with_name(saved.name + ".source.json")
                if sidecar.read_text(encoding="utf-8") != metadata:
                    raise ValueError("已保存的來源中繼資料與本次語料不同")
                source = read_source(str(saved))
                output = raw_dir / f"{document_id(source, extract(source).identity_text)}.md"
                validate_file(output, workspace_root)
                record["status"] = "reused"
            else:
                pending.parent.mkdir(parents=True, exist_ok=True)
                if pending.exists() and pending.read_bytes() != data:
                    raise ValueError("待處理原檔與本次語料不同")
                sidecar = pending.with_name(pending.name + ".source.json")
                if sidecar.exists() and sidecar.read_text(encoding="utf-8") != metadata:
                    raise ValueError("待處理來源中繼資料與本次語料不同")
                pending.write_bytes(data)
                sidecar.write_text(metadata, encoding="utf-8")
                output = convert_selected_source(pending, workspace_root)
                record["status"] = "converted"
            record["raw_path"] = output.relative_to(workspace_root).as_posix()
            outputs.add(output)
        except (OSError, UnicodeError, ValueError, RuntimeError) as error:
            record.update(status="failed", error=str(error))
        record["elapsed_seconds"] = time.perf_counter() - file_started
        records.append(record)

    converted = sum(row["status"] == "converted" for row in records)
    reused = sum(row["status"] == "reused" for row in records)
    report = {
        "source_dir": str(source_dir), "workspace_root": str(workspace_root),
        "source_base_url": source_base_url, "corpus_checksum": checksum,
        "converter_version": VERSION, "source_files": len(files),
        "source_bytes": sum(row["source_bytes"] for row in records),
        "converted": converted, "reused": reused,
        "failed": len(files) - converted - reused,
        "success_rate": (converted + reused) / len(files),
        "raw_files": len(outputs), "raw_bytes": sum(path.stat().st_size for path in outputs),
        "elapsed_seconds": time.perf_counter() - started, "files": records,
    }
    workspace_root.mkdir(parents=True, exist_ok=True)
    report_path = workspace_root / "import-report.json"
    temporary = report_path.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(report_path)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="固定 checksum 後批次匯入 Markdown，保存逐檔結果。")
    parser.add_argument("--source-dir", required=True, type=Path)
    parser.add_argument("--workspace-root", required=True, type=Path)
    parser.add_argument("--source-base-url", required=True)
    parser.add_argument("--expected-checksum", required=True)
    args = parser.parse_args()
    try:
        report = import_corpus(args.source_dir, args.workspace_root,
                               args.source_base_url, args.expected_checksum)
    except (OSError, ValueError, RuntimeError) as error:
        print(f"匯入失敗：{error}", file=sys.stderr)
        return 1
    print(f"完成：{report['converted']} 份新轉換，{report['reused']} 份沿用，{report['failed']} 份失敗。")
    print(f"成功率：{report['success_rate']:.2%}；耗時：{report['elapsed_seconds']:.3f} 秒。")
    print(f"逐檔紀錄：{args.workspace_root.resolve() / 'import-report.json'}")
    return 1 if report["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
