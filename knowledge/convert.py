#!/usr/bin/env python3
"""Day 8 entrypoint: convert pending files in this project's knowledge/inbox/."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "skills" / "source-to-raw-md" / "scripts"))

from batch import convert_inbox  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(convert_inbox(PROJECT_ROOT))
