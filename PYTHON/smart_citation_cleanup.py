#!/usr/bin/env python3
"""
Smart Citation Cleanup
Removes redundant citation entries, keeping the highest count per source/date combination
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent.parent))
from PYTHON.yaml_frontmatter_utils import extract_frontmatter
from vault_config import PAPERS_DIR


def parse_citation(citation_str):
    """Parse citation string into (count, source, date)"""
    match = re.match(r'(\d+) citations \(([^)]+)\) \[(\d{4}-\d{2}-\d{2})\]', citation_str)
    if match:
        return {
            'count': int(match.group(1)),
            'source': match.group(2),
            'date': match.group(3),
            'full': citation_str
        }
    return None


def dedupe_citations(citations):
    """Keep only the highest count per (source, date) pair"""
    by_source_date = defaultdict(list)

    for c in citations:
        parsed = parse_citation(c)
        if parsed:
            key = (parsed['source'], parsed['date'])
            by_source_date[key].append(parsed)

    # Keep the highest count for each source/date
    result = []
    for key, entries in by_source_date.items():
        best = max(entries, key=lambda x: x['count'])
        result.append(best['full'])

    return result


def clean_citation_section(body):
    """Clean citation section, removing redundant entries"""
    citation_match = re.search(r'(## Citation Info\s*\n+)(.*?)(?=\n##|\Z)', body, re.DOTALL)
    if not citation_match:
        return body, 0

    section_header = citation_match.group(1)
    citation_content = citation_match.group(2).strip()

    # Extract all citation entries
    citations = re.findall(r'\d+ citations \([^)]+\) \[\d{4}-\d{2}-\d{2}\]', citation_content)

    if len(citations) <= 1:
        return body, 0

    # Dedupe
    deduped = dedupe_citations(citations)

    if len(deduped) == len(citations):
        return body, 0  # Nothing removed

    removed = len(citations) - len(deduped)

    # Rebuild
    new_citation_content = ' '.join(deduped)

    # Replace in body
    start = citation_match.start()
    end = citation_match.end()
    new_body = body[:start] + section_header + new_citation_content + '\n' + body[end:].lstrip('\n')

    return new_body, removed


def process_paper(filepath, dry_run=False):
    """Process a single paper"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return 0, f"Cannot read: {e}"

    try:
        frontmatter_text, body = extract_frontmatter(content)
    except Exception as e:
        return 0, f"YAML error: {e}"

    new_body, removed = clean_citation_section(body)

    if removed > 0 and not dry_run:
        new_content = f"---\n{frontmatter_text.strip()}\n---\n{new_body}"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return removed, None


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Smart citation cleanup')
    parser.add_argument('--dry-run', action='store_true', help='Preview only')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose')
    args = parser.parse_args()

    print("=" * 60)
    print("SMART CITATION CLEANUP")
    print("=" * 60)

    if args.dry_run:
        print("DRY RUN - No changes will be saved\n")

    papers = list(PAPERS_DIR.glob("*.md"))
    total = len(papers)

    cleaned = 0
    total_removed = 0

    for i, filepath in enumerate(papers, 1):
        if i % 100 == 0:
            print(f"  Progress: {i}/{total}")

        removed, error = process_paper(filepath, args.dry_run)

        if error:
            if args.verbose:
                print(f"  ERROR {filepath.name}: {error}")
        elif removed > 0:
            cleaned += 1
            total_removed += removed
            if args.verbose:
                print(f"  CLEANED {filepath.name}: removed {removed} redundant citations")

    print(f"  Progress: {total}/{total}")

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Papers cleaned: {cleaned}")
    print(f"Total redundant citations removed: {total_removed}")

    if args.dry_run:
        print("\n[DRY RUN] No changes saved.")
    else:
        print("\nAll changes saved.")

    print("=" * 60)


if __name__ == "__main__":
    main()
