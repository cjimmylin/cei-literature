#!/usr/bin/env python3
"""Fix duplicate YAML fields in paper frontmatter.

During the 2026-02-13 import, batch_download_pdfs.py inserted new pdf_extract:
lines without removing the original empty placeholders, leaving 200 papers with
duplicate pdf_extract: fields. This script removes the stale duplicates.

Usage:
    python fix_duplicate_yaml_fields.py --dry-run --date 20260213
    python fix_duplicate_yaml_fields.py --date 20260213
"""

import argparse
import re
import sys
from pathlib import Path

PAPERS_DIR = Path(__file__).resolve().parent.parent / "papers"


def find_papers_by_date(date_str: str) -> list[Path]:
    """Return all paper files with matching DATE_ADDED."""
    papers = []
    for p in sorted(PAPERS_DIR.glob("*.md")):
        content = p.read_text(encoding="utf-8")
        if f"DATE_ADDED: {date_str}" in content:
            papers.append(p)
    return papers


def fix_duplicate_fields(filepath: Path, dry_run: bool = True) -> dict:
    """Remove duplicate YAML fields, keeping the valid (non-empty) occurrence.

    Returns dict with 'fixed_fields' list and 'removed_lines' count, or empty
    dict if no duplicates found.
    """
    content = filepath.read_text(encoding="utf-8")

    # Extract frontmatter between --- delimiters
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}

    fm_lines = parts[1].split("\n")

    # Find all field names and their line indices (within frontmatter)
    field_occurrences: dict[str, list[int]] = {}
    for i, line in enumerate(fm_lines):
        m = re.match(r'^([a-zA-Z_][a-zA-Z0-9_]*)\s*:', line)
        if m:
            field_name = m.group(1)
            field_occurrences.setdefault(field_name, []).append(i)

    # Find fields with duplicates
    duplicates = {k: v for k, v in field_occurrences.items() if len(v) > 1}
    if not duplicates:
        return {}

    lines_to_remove: set[int] = set()
    fixed_fields = []

    for field_name, indices in duplicates.items():
        # Determine which line to keep: prefer the one with a meaningful value
        keep_idx = indices[0]  # default: keep first
        for idx in indices:
            line = fm_lines[idx]
            value = line.split(":", 1)[1].strip() if ":" in line else ""
            # A "valid" value contains actual content (not empty, not "N/A", not just quotes)
            stripped = value.strip('" \'')
            if stripped and stripped != "N/A":
                keep_idx = idx
                break  # prefer first valid occurrence

        # Mark all other occurrences for removal
        for idx in indices:
            if idx != keep_idx:
                lines_to_remove.add(idx)
                fixed_fields.append(field_name)

    if not lines_to_remove:
        return {}

    # Remove stale lines
    new_fm_lines = [line for i, line in enumerate(fm_lines) if i not in lines_to_remove]
    new_content = "---".join([parts[0], "\n".join(new_fm_lines), parts[2]])

    if not dry_run:
        filepath.write_text(new_content, encoding="utf-8")

    return {
        "fixed_fields": fixed_fields,
        "removed_lines": len(lines_to_remove),
    }


def main():
    parser = argparse.ArgumentParser(description="Fix duplicate YAML fields in papers")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing")
    parser.add_argument("--date", default="20260213", help="DATE_ADDED filter (default: 20260213)")
    args = parser.parse_args()

    print(f"Scanning papers with DATE_ADDED: {args.date} ...")
    papers = find_papers_by_date(args.date)
    print(f"Found {len(papers)} papers")

    total_fixed = 0
    total_lines_removed = 0
    field_counts: dict[str, int] = {}

    for p in papers:
        result = fix_duplicate_fields(p, dry_run=args.dry_run)
        if result:
            total_fixed += 1
            total_lines_removed += result["removed_lines"]
            for f in result["fixed_fields"]:
                field_counts[f] = field_counts.get(f, 0) + 1
            if args.dry_run:
                print(f"  WOULD FIX: {p.name} — remove {result['removed_lines']} duplicate line(s): {result['fixed_fields']}")
            else:
                print(f"  FIXED: {p.name} — removed {result['removed_lines']} duplicate line(s): {result['fixed_fields']}")

    mode = "DRY RUN" if args.dry_run else "APPLIED"
    print(f"\n=== SUMMARY ({mode}) ===")
    print(f"Papers scanned:  {len(papers)}")
    print(f"Papers fixed:    {total_fixed}")
    print(f"Lines removed:   {total_lines_removed}")
    if field_counts:
        print(f"Fields fixed:    {field_counts}")
    print("Done.")


if __name__ == "__main__":
    main()
