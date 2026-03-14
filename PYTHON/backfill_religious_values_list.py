#!/usr/bin/env python3
"""
Backfill rv_* confidence score fields to all existing papers.

Uses the religious_scoring.py engine to compute 14 rv_* integer scores
(0-100) for each paper, then inserts them into YAML frontmatter.
Also updates the derived religious_values and religious_values_list strings.

Reads title + abstract from each paper, optionally also scans PDF extract
for deeper coverage. Uses safe regex insertion (NOT parse/rebuild round-trip).

Usage:
  ../.venv/bin/python PYTHON/backfill_religious_values_list.py [--dry-run]

Run from CEI-Lit-WS/ directory.

Updated 2026-03-13: Computes and sets rv_* integer score fields instead of
just the religious_values_list string.
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
from religious_scoring import (
    RV_FIELDS, FIELD_DISPLAY_NAMES,
    compute_all_rv_scores, is_rv_detected,
    derive_religious_values_string, derive_religious_values_list_string,
    insert_rv_fields_between_religious_values, update_existing_rv_fields,
    DEFAULT_THRESHOLD,
)


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
    """Compute and set rv_* score fields for a paper.

    Returns: (status, detected_traditions)
      status: 'added', 'updated', 'skipped' (scores unchanged), 'error'
    """
    frontmatter, body = read_paper(paper_path)

    # Extract title + abstract from body
    title_match = re.search(r'^# (.+)$', body, re.MULTILINE)
    title = title_match.group(1) if title_match else ''

    abstract_match = re.search(r'## Abstract\s*\n\n(.*?)(?=\n## |\Z)', body, re.DOTALL)
    abstract = abstract_match.group(1).strip() if abstract_match else ''

    # Also get PDF extract text for deeper coverage
    extract_text = get_pdf_extract_text(paper_path, frontmatter)

    # Compute rv_* scores using religious_scoring engine
    rv_scores = compute_all_rv_scores(title, abstract, extract_text)

    # Determine detected traditions for reporting
    detected = [FIELD_DISPLAY_NAMES[f] for f in RV_FIELDS
                if rv_scores[f] >= DEFAULT_THRESHOLD]

    if dry_run:
        return 'added', detected

    # Check if rv_* fields already exist in frontmatter
    has_rv_fields = re.search(r'^rv_islam:', frontmatter, re.MULTILINE)

    if has_rv_fields:
        # Update existing rv_* fields
        new_fm = update_existing_rv_fields(frontmatter, rv_scores)
        status = 'updated'
    else:
        # Insert rv_* fields between religious_values and religious_values_list
        new_fm, success = insert_rv_fields_between_religious_values(frontmatter, rv_scores)
        if not success:
            # Fallback: try to add after religious_values line
            derived_rv = derive_religious_values_string(rv_scores)
            derived_list = derive_religious_values_list_string(rv_scores)

            rv_block_lines = [f"{field}: {rv_scores[field]}" for field in RV_FIELDS]
            rv_block = "\n".join(rv_block_lines)

            # Try inserting after religious_values:
            new_fm, n = re.subn(
                r'^(religious_values:.*)$',
                r'\1\n' + rv_block + f'\nreligious_values_list: "{derived_list}"',
                frontmatter, count=1, flags=re.MULTILINE,
            )
            if n == 0:
                # No religious_values field at all — append everything
                new_fm = frontmatter.rstrip()
                new_fm += f'\nreligious_values: "{derived_rv}"'
                for field in RV_FIELDS:
                    new_fm += f'\n{field}: {rv_scores[field]}'
                new_fm += f'\nreligious_values_list: "{derived_list}"'
        status = 'added'

    # Validate and write
    is_valid, issues = validate_frontmatter(new_fm)
    if not is_valid:
        print(f"  WARN: {paper_path.name}: {issues}")

    write_paper(paper_path, new_fm, body, validate=True)

    return status, detected


def main():
    dry_run = '--dry-run' in sys.argv

    papers = sorted(PAPERS_DIR.glob('*.md'))
    total = len(papers)
    print(f"Total papers: {total}")
    if dry_run:
        print("DRY RUN: No files will be modified")
    print()

    added = 0
    updated = 0
    skipped = 0
    errors = 0
    religious_counts = {}

    for i, paper_path in enumerate(papers, 1):
        try:
            status, detected = process_paper(paper_path, dry_run=dry_run)

            if status == 'added':
                added += 1
            elif status == 'updated':
                updated += 1
            elif status == 'skipped':
                skipped += 1

            # Count detected traditions
            for t in detected:
                religious_counts[t] = religious_counts.get(t, 0) + 1

            if i % 100 == 0:
                print(f"  Progress: {i}/{total} (added={added}, updated={updated}, skipped={skipped})")

        except Exception as e:
            errors += 1
            print(f"  ERROR: {paper_path.name}: {e}")

    # Summary
    print()
    print("=" * 60)
    print("BACKFILL SUMMARY")
    print("=" * 60)
    print(f"  Total papers:   {total}")
    print(f"  Added rv_* fields:  {added}")
    print(f"  Updated rv_* fields: {updated}")
    print(f"  Skipped:        {skipped}")
    print(f"  Errors:         {errors}")
    print()
    print("DETECTED TRADITIONS (score >= {}):" .format(DEFAULT_THRESHOLD))
    for religion, count in sorted(religious_counts.items(), key=lambda x: -x[1]):
        print(f"  {religion}: {count}")
    print("=" * 60)


if __name__ == '__main__':
    main()
