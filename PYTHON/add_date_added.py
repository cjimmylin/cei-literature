#!/usr/bin/env python3
"""
Add DATE_ADDED field to papers that lack it.

Uses macOS st_birthtime (file creation date) as the source.
Inserts DATE_ADDED: YYYYMMDD right before the ethics_overall: line.

Usage:
  python add_date_added.py --dry-run    # Preview changes
  python add_date_added.py              # Apply changes
"""

import functools
import os
import re
import sys
from datetime import datetime
from pathlib import Path

print = functools.partial(print, flush=True)

sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))
from config import PAPERS_DIR


def get_creation_date(filepath):
    """Get file creation date from macOS st_birthtime."""
    stat = os.stat(filepath)
    ctime = stat.st_birthtime
    return datetime.fromtimestamp(ctime).strftime("%Y%m%d")


def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("=== DRY RUN — no files will be modified ===\n")

    papers = sorted(PAPERS_DIR.glob("*.md"))
    updated = 0
    skipped = 0
    errors = 0

    for paper_path in papers:
        try:
            content = paper_path.read_text(encoding="utf-8")
        except Exception as e:
            print("ERROR: Cannot read {}: {}".format(paper_path.name, e))
            errors += 1
            continue

        # Check if DATE_ADDED already exists
        m = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not m:
            continue

        fm = m.group(1)
        if re.search(r"^DATE_ADDED:", fm, re.MULTILINE):
            skipped += 1
            continue

        # Get creation date
        date_str = get_creation_date(paper_path)

        # Insert DATE_ADDED before ethics_overall
        new_content, count = re.subn(
            r"^(ethics_overall:)",
            "DATE_ADDED: {}\n\\1".format(date_str),
            content,
            count=1,
            flags=re.MULTILINE,
        )

        if count == 0:
            print("WARN: No ethics_overall anchor in {} — skipping".format(paper_path.name))
            errors += 1
            continue

        if dry_run:
            if updated < 10:
                print("  Would add DATE_ADDED: {} to {}".format(date_str, paper_path.name))
        else:
            paper_path.write_text(new_content, encoding="utf-8")

        updated += 1

    print("\n=== SUMMARY ===")
    print("  Updated: {}".format(updated))
    print("  Already had DATE_ADDED: {}".format(skipped))
    print("  Errors: {}".format(errors))
    print("  Total papers: {}".format(len(papers)))

    if dry_run:
        print("\n  (Dry run — rerun without --dry-run to apply)")


if __name__ == "__main__":
    main()
