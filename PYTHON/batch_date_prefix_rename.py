#!/usr/bin/env python3
"""Batch-rename files in STATISTICS/ and logs/ to add YYYYMMDD- date prefix.

Usage:
    python batch_date_prefix_rename.py              # dry-run (default)
    python batch_date_prefix_rename.py --execute    # actually rename
"""

import argparse
import datetime
import json
import os
import re
import sys
from pathlib import Path
from typing import List, Optional, Tuple

# Working dir should be CEI-Lit-WS/
BASE = Path(__file__).resolve().parent.parent  # CEI-Lit-WS/

DIRS_TO_PROCESS = [
    BASE / "STATISTICS",
    BASE / "logs",
]

SKIP_NAMES = {".DS_Store", "README.md"}
ALREADY_PREFIXED = re.compile(r"^\d{8}-")

# Patterns to extract embedded dates from filenames (tried in order)
DATE_PATTERNS = [
    # YYYY-MM-DD or YYYY_MM_DD (e.g. 2026_02_07, 2026-01-31)
    re.compile(r"(\d{4})[-_](\d{2})[-_](\d{2})"),
    # YYYYMMDD run together (e.g. 20260124 in code_quality_20260124_171131)
    re.compile(r"(\d{4})(\d{2})(\d{2})"),
]


def extract_date_from_name(filename: str) -> Optional[str]:
    """Try to extract a YYYYMMDD date string from the filename."""
    for pat in DATE_PATTERNS:
        m = pat.search(filename)
        if m:
            y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
            # Sanity check: valid date in reasonable range
            if 2020 <= y <= 2030 and 1 <= mo <= 12 and 1 <= d <= 31:
                try:
                    datetime.date(y, mo, d)
                    return f"{y:04d}{mo:02d}{d:02d}"
                except ValueError:
                    continue
    return None


def get_birthtime(filepath: Path) -> str:
    """Get file birth time as YYYYMMDD (macOS st_birthtime)."""
    st = os.stat(filepath)
    ts = getattr(st, "st_birthtime", st.st_mtime)
    dt = datetime.datetime.fromtimestamp(ts)
    return dt.strftime("%Y%m%d")


def compute_renames(directory: Path) -> List[Tuple[str, str, str]]:
    """Compute (old_name, new_name) pairs for one directory."""
    renames = []
    for entry in sorted(directory.iterdir()):
        if not entry.is_file():
            continue
        name = entry.name
        if name in SKIP_NAMES:
            continue
        if ALREADY_PREFIXED.match(name):
            continue

        # Try embedded date first, fall back to birth time
        date_str = extract_date_from_name(name)
        source = "embedded"
        if date_str is None:
            date_str = get_birthtime(entry)
            source = "birthtime"

        new_name = f"{date_str}-{name}"
        renames.append((name, new_name, source))
    return renames


def main():
    parser = argparse.ArgumentParser(description="Add YYYYMMDD- prefix to logs/ and STATISTICS/ files")
    parser.add_argument("--execute", action="store_true", help="Actually rename (default is dry-run)")
    args = parser.parse_args()

    mapping = {}  # {dir_name: {old: new, ...}}
    total = 0

    for d in DIRS_TO_PROCESS:
        dir_key = d.name  # "STATISTICS" or "logs"
        renames = compute_renames(d)
        if not renames:
            print(f"\n{dir_key}/: nothing to rename")
            continue

        print(f"\n{'=' * 60}")
        print(f"{dir_key}/: {len(renames)} files to rename")
        print(f"{'=' * 60}")

        dir_mapping = {}
        for old_name, new_name, source in renames:
            print(f"  {old_name}")
            print(f"    → {new_name}  [{source}]")
            dir_mapping[old_name] = new_name

            if args.execute:
                old_path = d / old_name
                new_path = d / new_name
                if new_path.exists():
                    print(f"    ⚠ SKIP: target already exists!")
                    continue
                os.rename(old_path, new_path)

        mapping[dir_key] = dir_mapping
        total += len(renames)

    # Write mapping JSON
    today = datetime.date.today().strftime("%Y%m%d")
    mapping_filename = f"{today}-date_prefix_rename_mapping.json"
    mapping_path = BASE / "logs" / mapping_filename
    # If we just renamed logs files, the mapping goes into the renamed logs dir
    # Write to the current logs dir (which is still the same path)
    with open(mapping_path, "w") as f:
        json.dump(mapping, f, indent=2)
    print(f"\nMapping written to: logs/{mapping_filename}")

    mode = "EXECUTED" if args.execute else "DRY-RUN"
    print(f"\n{'=' * 60}")
    print(f"SUMMARY ({mode}): {total} files across {len(DIRS_TO_PROCESS)} directories")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
