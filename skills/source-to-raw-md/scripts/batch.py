#!/usr/bin/env python3
"""Convert a project's pending knowledge/inbox/ files to verified raw Markdown."""

from __future__ import annotations

import argparse
import sys
import hashlib
import os
import shutil
from pathlib import Path

from convert import convert
from validate import validate_file

SUPPORTED = {".txt", ".md", ".markdown", ".pdf", ".html", ".htm"}


def processed_path(source: Path, inbox: Path, processed: Path) -> tuple[Path, bool]:
    relative = source.relative_to(inbox)
    destination = processed / relative
    if destination.exists() and destination.read_bytes() != source.read_bytes():
        digest = hashlib.sha256(source.read_bytes()).hexdigest()[:12]
        destination = processed / digest / relative
    if destination.exists() and destination.read_bytes() != source.read_bytes():
        raise RuntimeError(f"已處理目錄有同名且內容不同的檔案：{destination}")
    return destination, destination.exists()


def convert_inbox(root: Path) -> int:
    inbox = root / "knowledge" / "inbox"
    raw = root / "knowledge" / "raw"
    processed = inbox / "processed"
    if not inbox.is_dir():
        print(f"找不到原始資料夾：{inbox}", file=sys.stderr)
        return 1
    sources = sorted(path for path in inbox.rglob("*")
                     if path.is_file() and not path.is_relative_to(processed)
                     and not path.name.startswith("."))
    if not sources:
        print("knowledge/inbox/ 目前沒有來源檔。")
        return 0

    converted = skipped = failed = 0
    for source in sources:
        label = source.relative_to(inbox)
        if source.suffix.lower() not in SUPPORTED:
            print(f"不支援，未轉換：{label}", file=sys.stderr)
            skipped += 1
            continue
        destination = None
        copied = False
        output = None
        try:
            if source.is_symlink():
                raise ValueError("來源是符號連結；請放入實際檔案")
            destination, already_saved = processed_path(source, inbox, processed)
            if not already_saved:
                destination.parent.mkdir(parents=True, exist_ok=True)
                temporary = destination.with_name(destination.name + ".tmp")
                try:
                    shutil.copy2(source, temporary)
                    os.replace(temporary, destination)
                finally:
                    temporary.unlink(missing_ok=True)
                copied = True
                if destination.read_bytes() != source.read_bytes():
                    raise RuntimeError("保存到 processed/ 的副本與原檔不同")
            output = convert(str(destination), inbox, raw)
            validate_file(output, root)
        except (OSError, UnicodeError, ValueError, RuntimeError) as error:
            if copied and destination is not None:
                destination.unlink(missing_ok=True)
                if output is not None:
                    try:
                        convert(str(source), inbox, raw)
                    except (OSError, UnicodeError, ValueError, RuntimeError):
                        pass
            print(f"轉換失敗：{label}：{error}", file=sys.stderr)
            failed += 1
        else:
            source.unlink()
            print(f"OK {label} → {output.relative_to(root)}")
            converted += 1
    print(f"完成：{converted} 份成功，{skipped} 份格式不支援，{failed} 份失敗。")
    return 1 if skipped or failed else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="批次轉換 knowledge/inbox/，成功原檔移到 processed/。")
    parser.add_argument("--project-root", type=Path, default=Path.cwd(), help="包含 knowledge/ 的專案根目錄")
    args = parser.parse_args()
    return convert_inbox(args.project_root.resolve())


if __name__ == "__main__":
    raise SystemExit(main())
