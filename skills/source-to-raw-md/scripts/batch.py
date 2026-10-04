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


def convert_selected_source(source: Path, root: Path) -> Path:
    """Convert one pending inbox file, preserving it and its optional metadata."""

    inbox = root / "knowledge" / "inbox"
    raw = root / "knowledge" / "raw"
    processed = inbox / "processed"
    if not source.is_file() or not source.resolve().is_relative_to(inbox.resolve()):
        raise ValueError("來源必須是 knowledge/inbox/ 裡的檔案")
    if source.resolve().is_relative_to(processed.resolve()):
        raise ValueError("來源已在 inbox/processed/，不應再次排入轉換")
    if source.suffix.lower() not in SUPPORTED:
        raise ValueError(f"來源格式不支援：{source.suffix}")
    if source.is_symlink():
        raise ValueError("來源是符號連結；請放入實際檔案")

    sidecar = source.with_name(source.name + ".source.json")
    destination, already_saved = processed_path(source, inbox, processed)
    destination_sidecar = destination.with_name(destination.name + ".source.json")
    copied = False
    sidecar_copied = False
    output = None
    try:
        if sidecar.is_symlink():
            raise ValueError("來源中繼資料是符號連結")
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
        if sidecar.is_file():
            if destination_sidecar.exists():
                if destination_sidecar.read_bytes() != sidecar.read_bytes():
                    raise RuntimeError(f"processed/ 中繼資料同名但內容不同：{destination_sidecar}")
            else:
                destination_sidecar.parent.mkdir(parents=True, exist_ok=True)
                temporary_sidecar = destination_sidecar.with_name(destination_sidecar.name + ".tmp")
                try:
                    shutil.copy2(sidecar, temporary_sidecar)
                    os.replace(temporary_sidecar, destination_sidecar)
                finally:
                    temporary_sidecar.unlink(missing_ok=True)
                sidecar_copied = True
        output = convert(str(destination), inbox, raw)
        validate_file(output, root)
    except (OSError, UnicodeError, ValueError, RuntimeError):
        if copied:
            destination.unlink(missing_ok=True)
        if sidecar_copied:
            destination_sidecar.unlink(missing_ok=True)
        if copied and output is not None:
            try:
                convert(str(source), inbox, raw)
            except (OSError, UnicodeError, ValueError, RuntimeError):
                pass
        raise
    source.unlink()
    sidecar.unlink(missing_ok=True)
    return output


def convert_inbox(root: Path) -> int:
    inbox = root / "knowledge" / "inbox"
    raw = root / "knowledge" / "raw"
    processed = inbox / "processed"
    if not inbox.is_dir():
        print(f"找不到原始資料夾：{inbox}", file=sys.stderr)
        return 1
    sources = sorted(path for path in inbox.rglob("*")
                     if path.is_file() and not path.is_relative_to(processed)
                     and not path.name.startswith(".")
                     and not path.name.endswith(".source.json"))
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
        try:
            output = convert_selected_source(source, root)
        except (OSError, UnicodeError, ValueError, RuntimeError) as error:
            print(f"轉換失敗：{label}：{error}", file=sys.stderr)
            failed += 1
        else:
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
