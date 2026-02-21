#!/usr/bin/env python3
"""
Consolidate Author Resolution Plans — Step 4 of the Author Verification Pipeline

Merges range-specific resolution JSON files from parallel agents into
a single consolidated plan.

Input:  logs/YYYYMMDD-author_resolution_plan_*.json (multiple range files)
Output: logs/YYYYMMDD-author_resolution_plan.json (merged)

USAGE:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/consolidate_author_resolutions.py
    ../.venv/bin/python PYTHON/consolidate_author_resolutions.py --date 20260220
    ../.venv/bin/python PYTHON/consolidate_author_resolutions.py --dry-run
"""

import argparse
import functools
import json
import os
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

# Force flush
import builtins
print = functools.partial(builtins.print, flush=True)

sys.path.insert(0, str(Path(__file__).parent))
from vault_config import LOGS_DIR

DATE_PREFIX = datetime.now().strftime("%Y%m%d")


def find_resolution_files(date_prefix: str) -> list:
    """Find all resolution plan files for the given date."""
    pattern = f"{date_prefix}-author_resolution_plan_*.json"
    files = sorted(LOGS_DIR.glob(pattern))
    # Exclude the final merged file if it exists
    merged_name = f"{date_prefix}-author_resolution_plan.json"
    return [f for f in files if f.name != merged_name]


def merge_category(all_items: list) -> list:
    """Merge items from multiple files, deduplicating by paper stem.
    Prefers resolved entries over unresolved ones."""
    best = {}  # key -> item
    for item in all_items:
        key = item.get("paper", "") + "|" + item.get("author_name", "") + "|" + item.get("original_name", "")
        if key not in best:
            best[key] = item
        else:
            # Prefer resolved over unresolved
            existing = best[key]
            if existing.get("status") != "resolved" and item.get("status") == "resolved":
                best[key] = item
    return list(best.values())


def consolidate(date_prefix: str, dry_run: bool = False):
    """Merge all resolution plan files into one."""
    files = find_resolution_files(date_prefix)

    if not files:
        # Check if a single full run exists (no range suffix)
        full_file = LOGS_DIR / f"{date_prefix}-author_resolution_plan_ABCDEF.json"
        if full_file.exists():
            print(f"Found single full-run file: {full_file.name}")
            # Just rename/copy it to the canonical name
            output = LOGS_DIR / f"{date_prefix}-author_resolution_plan.json"
            if dry_run:
                print(f"DRY RUN: Would copy {full_file.name} -> {output.name}")
                return
            with open(full_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            tmp = output.with_suffix(f".tmp.{os.getpid()}")
            with open(tmp, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            os.replace(str(tmp), str(output))
            print(f"Consolidated (single file): {output.name}")
            return

        print(f"No resolution files found for date {date_prefix}")
        return

    print(f"Found {len(files)} resolution files to merge:")
    for f in files:
        print(f"  {f.name}")

    # Merge all categories
    categories = defaultdict(list)
    metadata_parts = []

    for fpath in files:
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if "metadata" in data:
            metadata_parts.append(data["metadata"])

        for key in ('A', 'B', 'C', 'D', 'E', 'F'):
            if key in data and data[key]:
                categories[key].extend(data[key])

    # Deduplicate each category
    merged = {
        "metadata": {
            "date": datetime.now().isoformat(),
            "source_files": [f.name for f in files],
            "source_metadata": metadata_parts,
        }
    }

    total_items = 0
    for key in ('A', 'B', 'C', 'D', 'E', 'F'):
        items = categories.get(key, [])
        deduped = merge_category(items)
        merged[key] = deduped
        if deduped:
            resolved = sum(1 for r in deduped if r.get("status") == "resolved")
            print(f"  {key}: {len(deduped)} items ({resolved} resolved)")
            total_items += len(deduped)

    print(f"\nTotal: {total_items} items across all categories")

    if dry_run:
        print("DRY RUN: No file written.")
        return

    output = LOGS_DIR / f"{date_prefix}-author_resolution_plan.json"
    tmp = output.with_suffix(f".tmp.{os.getpid()}")
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(merged, f, indent=2, ensure_ascii=False)
    os.replace(str(tmp), str(output))
    print(f"\nConsolidated plan saved: {output.name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Consolidate author resolution plans")
    parser.add_argument("--date", default=DATE_PREFIX,
                        help=f"Date prefix to consolidate (default: {DATE_PREFIX})")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be merged without writing")
    args = parser.parse_args()

    consolidate(args.date, dry_run=args.dry_run)
