#!/usr/bin/env python3
"""
Apply high-confidence author extraction results to paper YAML.

Reads from the extraction results JSON, converts author names to wikilink format,
and updates first_author, last_author, authors, and authors_incomplete fields.

Uses safe regex field replacement — no parse/rebuild round-trip.

Usage:
    python apply_author_extraction.py                    # Dry run
    python apply_author_extraction.py --execute          # Apply changes
    python apply_author_extraction.py --execute --file X # Apply from specific file
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vault_config import PAPERS_DIR, LOGS_DIR


def first_last_to_last_first(name: str) -> str:
    """Convert 'First Middle Last' to 'Last, First Middle'."""
    name = name.strip()
    if ',' in name:
        return name  # Already in Last, First format
    words = name.split()
    if len(words) == 1:
        return name
    return f"{words[-1]}, {' '.join(words[:-1])}"


def make_authors_wikilink(names: list) -> str:
    """Convert list of 'First Last' names to wikilink-formatted authors string."""
    parts = []
    for name in names:
        lf = first_last_to_last_first(name)
        parts.append(f"[[{lf}]]")
    return "; ".join(parts)


def safe_replace_field(content: str, field: str, new_value: str) -> str:
    """Replace a YAML field value using safe regex (no parse/rebuild)."""
    # Escape the value for YAML (replace " with ')
    safe_value = new_value.replace('"', "'")
    pattern = rf'^({re.escape(field)}:\s*).*$'
    replacement = rf'\g<1>"{safe_value}"'
    new_content, count = re.subn(pattern, replacement, content, count=1, flags=re.MULTILINE)
    if count == 0:
        raise ValueError(f"Field '{field}' not found in content")
    return new_content


def apply_to_paper(paper_path: Path, proposed_authors: list, dry_run: bool = True) -> bool:
    """Apply author extraction results to a single paper."""
    content = paper_path.read_text(encoding='utf-8')

    first_author_lf = first_last_to_last_first(proposed_authors[0])
    last_author_lf = first_last_to_last_first(proposed_authors[-1])
    authors_str = make_authors_wikilink(proposed_authors)

    if dry_run:
        print(f"  Would update:")
        print(f"    first_author → [[{first_author_lf}]]")
        print(f"    last_author  → [[{last_author_lf}]]")
        print(f"    authors      → {authors_str[:80]}...")
        print(f"    authors_incomplete → false")
        return True

    try:
        content = safe_replace_field(content, 'first_author', f"[[{first_author_lf}]]")
        content = safe_replace_field(content, 'last_author', f"[[{last_author_lf}]]")
        content = safe_replace_field(content, 'authors', authors_str)
        content = safe_replace_field(content, 'authors_incomplete', 'false')
    except ValueError as e:
        # For authors_incomplete, try without quotes (it's a boolean)
        if 'authors_incomplete' in str(e):
            content = re.sub(
                r'^(authors_incomplete:\s*).*$',
                r'\g<1>false',
                content, count=1, flags=re.MULTILINE
            )
        else:
            print(f"  ERROR: {e}")
            return False

    # Fix: authors_incomplete should not be quoted
    content = re.sub(
        r'^(authors_incomplete:\s*)"?false"?$',
        r'\g<1>false',
        content, count=1, flags=re.MULTILINE
    )

    paper_path.write_text(content, encoding='utf-8')
    return True


def main():
    parser = argparse.ArgumentParser(description="Apply author extraction results")
    parser.add_argument('--execute', action='store_true', help="Apply changes (default: dry run)")
    parser.add_argument('--file', type=str, default=None,
                        help="Results JSON file (default: latest extraction results)")
    args = parser.parse_args()

    # Load results
    results_files = []
    if args.file:
        results_files.append(Path(args.file))
    else:
        # Load main results + retry results
        main_path = LOGS_DIR / "20260216-author_extraction_results.json"
        retry_path = LOGS_DIR / "20260216-author_extraction_retry_results.json"
        if main_path.exists():
            results_files.append(main_path)
        if retry_path.exists():
            results_files.append(retry_path)

    all_results = []
    for f in results_files:
        data = json.loads(f.read_text())
        all_results.extend(data)
        print(f"Loaded {len(data)} results from {f.name}")

    # Filter to high-confidence only
    high_conf = [r for r in all_results if r.get('confidence') == 'high' and r.get('proposed_authors')]
    print(f"\nHigh-confidence results: {len(high_conf)}")

    if not high_conf:
        print("No high-confidence results to apply.")
        return

    applied = 0
    skipped = 0
    errors = 0

    for result in high_conf:
        filename = result['filename']
        paper_path = PAPERS_DIR / filename
        proposed = result['proposed_authors']

        print(f"\n{'─' * 60}")
        print(f"Paper: {filename}")
        print(f"  Source: {result.get('source', 'unknown')}")
        print(f"  Current: {result.get('current_authors', 'N/A')[:80]}")
        print(f"  Proposed ({len(proposed)}): {proposed[:5]}{'...' if len(proposed) > 5 else ''}")

        if not paper_path.exists():
            print(f"  SKIP: file not found")
            skipped += 1
            continue

        # Check if paper still has authors_incomplete: true
        content = paper_path.read_text(encoding='utf-8')
        if 'authors_incomplete: true' not in content:
            print(f"  SKIP: authors_incomplete is not true (already fixed?)")
            skipped += 1
            continue

        success = apply_to_paper(paper_path, proposed, dry_run=not args.execute)
        if success:
            applied += 1
            if args.execute:
                print(f"  APPLIED")
        else:
            errors += 1

    action = "Applied" if args.execute else "Would apply"
    print(f"\n{'=' * 60}")
    print(f"SUMMARY: {action} to {applied} papers, {skipped} skipped, {errors} errors")


if __name__ == "__main__":
    main()
