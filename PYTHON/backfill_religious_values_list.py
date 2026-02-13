#!/usr/bin/env python3
"""
Backfill religious_values_list field to all existing papers.

Uses the updated classify_religious_list() from classify_cultural_religious.py
with expanded RELIGIOUS_PATTERNS (including Confucianism, Taoism, Shinto, etc.)
to populate the new field.

Reads title + abstract from each paper, optionally also scans PDF extract
for deeper coverage. Inserts the field after existing religious_values: line
using safe regex insertion (NOT parse/rebuild round-trip).

Usage:
  ../.venv/bin/python PYTHON/backfill_religious_values_list.py [--dry-run]

Run from CEI-Lit-WS/ directory.
"""

import sys
import re
import functools
from pathlib import Path

# Force stdout flushing
print = functools.partial(print, flush=True)

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from yaml_frontmatter_utils import read_paper, write_paper, validate_frontmatter
from vault_config import PAPERS_DIR, PDF_EXTRACTS_DIR
import classify_cultural_religious as ccr


def get_pdf_extract_text(paper_path, frontmatter):
    """Read PDF extract text for deeper religion classification.

    Returns first ~5000 chars of extract, or empty string if unavailable.
    """
    match = re.search(r'^pdf_extract:\s*"?([^"\n]+)"?', frontmatter, re.MULTILINE)
    if not match or not match.group(1).strip():
        return ""

    extract_rel_path = match.group(1).strip()
    # Handle wikilink format
    extract_rel_path = extract_rel_path.strip('[]')
    extract_path = PAPERS_DIR.parent / extract_rel_path

    if not extract_path.exists():
        return ""

    try:
        text = extract_path.read_text(encoding='utf-8')
        # Return first ~5000 chars (enough for abstract + intro)
        return text[:5000]
    except Exception:
        return ""


def process_paper(paper_path, dry_run=False):
    """Add religious_values_list field to a paper.

    Returns: (status, religious_list_value)
      status: 'added', 'skipped' (already has field), 'error'
    """
    frontmatter, body = read_paper(paper_path)

    # Check if field already exists
    if re.search(r'^religious_values_list:', frontmatter, re.MULTILINE):
        return 'skipped', ''

    # Extract title + abstract from body
    title_match = re.search(r'^# (.+)$', body, re.MULTILINE)
    title = title_match.group(1) if title_match else ''

    abstract_match = re.search(r'## Abstract\s*\n\n(.*?)(?=\n## |\Z)', body, re.DOTALL)
    abstract = abstract_match.group(1).strip() if abstract_match else ''

    # Also get PDF extract text for deeper coverage
    extract_text = get_pdf_extract_text(paper_path, frontmatter)

    # Combine all text for classification
    full_text = f"{title} {abstract} {extract_text}".strip()

    # Classify using expanded patterns
    religious_list = ccr.classify_religious_list(title, full_text)

    # Also re-classify religious_values with expanded patterns
    religious = ccr.classify_religious(title, full_text)

    if dry_run:
        return 'added', religious_list

    # Safe regex insertion: insert religious_values_list after religious_values line
    # Use the value with single quotes replacing double quotes (YAML safety)
    safe_religious_list = religious_list.replace('"', "'")
    safe_religious = religious.replace('"', "'")

    # Update religious_values with expanded patterns too
    new_fm, count = re.subn(
        r'^(religious_values:).*$',
        rf'\1 "{safe_religious}"',
        frontmatter, count=1, flags=re.MULTILINE
    )

    if count == 0:
        # No religious_values field found — append both at end
        new_fm = frontmatter.rstrip() + f'\nreligious_values: "{safe_religious}"'
        new_fm += f'\nreligious_values_list: "{safe_religious_list}"'
    else:
        # Insert religious_values_list after religious_values line
        new_fm = re.sub(
            r'^(religious_values: .*)$',
            rf'\1\nreligious_values_list: "{safe_religious_list}"',
            new_fm, count=1, flags=re.MULTILINE
        )

    # Validate and write
    is_valid, issues = validate_frontmatter(new_fm)
    if not is_valid:
        print(f"  WARN: {paper_path.name}: {issues}")

    write_paper(paper_path, new_fm, body, validate=True)

    return 'added', religious_list


def main():
    dry_run = '--dry-run' in sys.argv

    papers = sorted(PAPERS_DIR.glob('*.md'))
    total = len(papers)
    print(f"Total papers: {total}")
    if dry_run:
        print("DRY RUN: No files will be modified")
    print()

    added = 0
    skipped = 0
    errors = 0
    religious_counts = {}

    for i, paper_path in enumerate(papers, 1):
        try:
            status, religious_list = process_paper(paper_path, dry_run=dry_run)

            if status == 'added':
                added += 1
                # Count religions
                for r in religious_list.split(', '):
                    r = r.strip()
                    if r:
                        religious_counts[r] = religious_counts.get(r, 0) + 1
            elif status == 'skipped':
                skipped += 1

            if i % 100 == 0:
                print(f"  Progress: {i}/{total} (added={added}, skipped={skipped})")

        except Exception as e:
            errors += 1
            print(f"  ERROR: {paper_path.name}: {e}")

    # Summary
    print()
    print("=" * 60)
    print("BACKFILL SUMMARY")
    print("=" * 60)
    print(f"  Total papers:   {total}")
    print(f"  Added field:    {added}")
    print(f"  Already existed: {skipped}")
    print(f"  Errors:         {errors}")
    print()
    print("RELIGIOUS VALUES LIST DISTRIBUTION:")
    for religion, count in sorted(religious_counts.items(), key=lambda x: -x[1]):
        print(f"  {religion}: {count}")
    print("=" * 60)


if __name__ == '__main__':
    main()
