#!/usr/bin/env python3
"""
Fix year field corruption: YAML year doesn't match filename year.

Many papers were imported with a default `year: 2025` instead of the actual
publication year encoded in the filename (format: YYYY-Author-Title.md).

Uses safe regex replacement (no parse/rebuild round-trip).
Skips 0000-prefix papers (no year data).

Usage:
    python fix_year_fields.py --dry-run    # Preview changes
    python fix_year_fields.py              # Apply changes
"""

import re
import sys
import functools
from pathlib import Path

print = functools.partial(print, flush=True)

SCRIPT_DIR = Path(__file__).parent
WS_ROOT = SCRIPT_DIR.parent
PAPERS_DIR = WS_ROOT / "papers"


def fix_year_fields(dry_run=False):
    """Fix year fields where YAML year != filename year."""
    fixed = 0
    skipped_no_year = 0
    skipped_0000 = 0
    already_correct = 0
    errors = []

    # Use iterdir() for safety (rglob breaks on brackets in filenames)
    paper_files = sorted(
        f for f in PAPERS_DIR.iterdir()
        if f.suffix == ".md" and f.is_file()
    )

    print(f"Scanning {len(paper_files)} paper files...")

    for paper_path in paper_files:
        stem = paper_path.stem

        # Extract year from filename
        match = re.match(r"^(\d{4})-", stem)
        if not match:
            skipped_no_year += 1
            continue

        fn_year = int(match.group(1))
        if fn_year == 0:
            skipped_0000 += 1
            continue

        # Read file content
        try:
            content = paper_path.read_text(encoding="utf-8")
        except Exception as e:
            errors.append(f"READ ERROR: {paper_path.name}: {e}")
            continue

        # Find year in YAML frontmatter
        year_match = re.search(r"^year:\s*(\d+)\s*$", content, re.MULTILINE)
        if not year_match:
            skipped_no_year += 1
            continue

        yaml_year = int(year_match.group(1))

        if yaml_year == fn_year:
            already_correct += 1
            continue

        # Fix the year field
        new_content, count = re.subn(
            r"^year:\s*\d+\s*$",
            f"year: {fn_year}",
            content,
            count=1,
            flags=re.MULTILINE,
        )

        if count == 0:
            errors.append(f"REGEX FAILED: {paper_path.name}")
            continue

        if dry_run:
            print(f"  WOULD FIX: {paper_path.name}: year {yaml_year} -> {fn_year}")
        else:
            paper_path.write_text(new_content, encoding="utf-8")
            print(f"  FIXED: {paper_path.name}: year {yaml_year} -> {fn_year}")

        fixed += 1

    # Summary
    print(f"\n{'DRY RUN ' if dry_run else ''}Summary:")
    print(f"  Total paper files: {len(paper_files)}")
    print(f"  Already correct:   {already_correct}")
    print(f"  Fixed:             {fixed}")
    print(f"  Skipped (no year): {skipped_no_year}")
    print(f"  Skipped (0000):    {skipped_0000}")
    print(f"  Errors:            {len(errors)}")

    if errors:
        print("\nErrors:")
        for e in errors:
            print(f"  {e}")

    return fixed, errors


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("=== DRY RUN MODE ===\n")
    else:
        print("=== APPLYING FIXES ===\n")

    fixed, errors = fix_year_fields(dry_run=dry_run)

    if not dry_run and errors:
        sys.exit(1)
