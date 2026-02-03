#!/usr/bin/env python3
"""
Enhanced Paper Cleanup Script - Phase 2
Fixes remaining issues after initial cleanup
"""

import re
import sys
import logging
from pathlib import Path
from collections import defaultdict

logger = logging.getLogger(__name__)

sys.path.insert(0, str(Path(__file__).parent))
from yaml_frontmatter_utils import extract_frontmatter
from vault_config import PAPERS_DIR


def fix_duplicate_citations_aggressive(body):
    """Remove ALL duplicate citation entries, keeping unique ones"""
    # Find the Citation Info section
    citation_match = re.search(r'(## Citation Info\s*\n+)(.*?)(?=\n##|\Z)', body, re.DOTALL)
    if not citation_match:
        return body, 0

    section_header = citation_match.group(1)
    citation_content = citation_match.group(2).strip()

    # Extract all citation entries
    all_citations = re.findall(r'(\d+ citations \([^)]+\) \[\d{4}-\d{2}-\d{2}\])', citation_content)

    if len(all_citations) <= 1:
        return body, 0

    # Get unique citations preserving order
    seen = set()
    unique_citations = []
    for c in all_citations:
        if c not in seen:
            seen.add(c)
            unique_citations.append(c)

    if len(unique_citations) == len(all_citations):
        return body, 0  # No duplicates

    # Rebuild citation section with unique entries
    new_citation_content = ' '.join(unique_citations)

    # Replace in body
    start = citation_match.start()
    end = citation_match.end()
    new_body = body[:start] + section_header + new_citation_content + '\n' + body[end:].lstrip('\n')

    return new_body, len(all_citations) - len(unique_citations)


def fix_na_local_pdf(frontmatter_text):
    """Remove local_pdf: N/A (make it empty or remove line)"""
    # Check if local_pdf is N/A
    if re.search(r'local_pdf:\s*["\']?N/A["\']?\s*\n', frontmatter_text):
        # Remove the line entirely
        new_frontmatter = re.sub(r'local_pdf:\s*["\']?N/A["\']?\s*\n', '', frontmatter_text)
        return new_frontmatter, True
    return frontmatter_text, False


def fix_broken_author_wikilinks(body):
    """Fix broken author wikilinks in body (e.g., [[Name, First]] -> [[First Name]])"""
    changes = 0

    # Pattern 1: Fix nested/broken wikilinks like [[Jiahao [[Wang]]]] -> [[Jiahao Wang]]
    def fix_nested(match):
        nonlocal changes
        text = match.group(0)
        # Remove nested [[ ]] and clean up
        cleaned = re.sub(r'\[\[', '', text)
        cleaned = re.sub(r'\]\]', '', cleaned)
        cleaned = cleaned.strip()
        if cleaned != text.strip('[]'):
            changes += 1
        return f'[[{cleaned}]]'

    # Find patterns like [[X [[Y]]]]
    body = re.sub(r'\[\[([^\[\]]*)\[\[([^\]]+)\]\]([^\[\]]*)\]\]', fix_nested, body)

    # Pattern 2: Fix incomplete wikilinks like [[Zhao, Jieyu (missing closing)
    # These show up in the Authors section
    author_section = re.search(r'(## Authors\s*\n)(.*?)(?=\n##|\Z)', body, re.DOTALL)
    if author_section:
        section_text = author_section.group(2)

        # Fix LastName, FirstName format
        def fix_lastfirst(m):
            nonlocal changes
            last = m.group(1).strip()
            first = m.group(2).strip()
            changes += 1
            return f'[[{first} {last}]]'

        fixed_section = re.sub(r'\[\[([^,\]]+),\s*([^\]]+)\]\]', fix_lastfirst, section_text)

        if fixed_section != section_text:
            start = author_section.start(2)
            end = author_section.end(2)
            body = body[:start] + fixed_section + body[end:]

    return body, changes


def clean_paper(filepath, dry_run=False):
    """Clean a single paper file - phase 2"""
    changes = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return [], f"Cannot read: {e}"

    try:
        frontmatter_text, body = extract_frontmatter(content)
    except Exception as e:
        return [], f"YAML error: {e}"

    new_frontmatter = frontmatter_text
    new_body = body
    modified = False

    # Fix 1: Aggressive duplicate citation removal
    new_body, dup_count = fix_duplicate_citations_aggressive(new_body)
    if dup_count > 0:
        changes.append(f"Removed {dup_count} duplicate citation(s)")
        modified = True

    # Fix 2: Remove N/A from local_pdf
    new_frontmatter, changed = fix_na_local_pdf(new_frontmatter)
    if changed:
        changes.append("Removed N/A local_pdf")
        modified = True

    # Fix 3: Fix broken author wikilinks
    new_body, author_changes = fix_broken_author_wikilinks(new_body)
    if author_changes > 0:
        changes.append(f"Fixed {author_changes} author wikilink(s)")
        modified = True

    # Write changes
    if modified and not dry_run:
        new_content = f"---\n{new_frontmatter.strip()}\n---\n{new_body}"
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
        except Exception as e:
            return changes, f"Write error: {e}"

    return changes, None


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Enhanced paper cleanup - phase 2')
    parser.add_argument('--dry-run', action='store_true', help='Show changes without applying')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    args = parser.parse_args()

    logger.info("=" * 60)
    logger.info("ENHANCED PAPER CLEANUP - PHASE 2")
    logger.info("=" * 60)

    if args.dry_run:
        logger.info("DRY RUN - No changes will be saved")

    paper_files = list(PAPERS_DIR.glob("*.md"))
    total = len(paper_files)

    logger.info(f"Processing {total} papers...")

    stats = {
        'papers_cleaned': 0,
        'papers_unchanged': 0,
        'papers_error': 0,
        'changes_by_type': defaultdict(int)
    }

    for i, filepath in enumerate(paper_files, 1):
        if i % 100 == 0:
            logger.info(f"  Progress: {i}/{total}")

        changes, error = clean_paper(filepath, dry_run=args.dry_run)

        if error:
            stats['papers_error'] += 1
            if args.verbose:
                logger.error(f"  ERROR {filepath.name}: {error}")
        elif changes:
            stats['papers_cleaned'] += 1
            for change in changes:
                change_type = change.split()[0]
                stats['changes_by_type'][change_type] += 1
            if args.verbose:
                logger.info(f"  CLEANED {filepath.name}:")
                for c in changes:
                    logger.info(f"    - {c}")
        else:
            stats['papers_unchanged'] += 1

    logger.info(f"  Progress: {total}/{total}")

    logger.info("=" * 60)
    logger.info("CLEANUP SUMMARY")
    logger.info("=" * 60)
    logger.info(f"Papers cleaned:   {stats['papers_cleaned']}")
    logger.info(f"Papers unchanged: {stats['papers_unchanged']}")
    logger.info(f"Papers with errors: {stats['papers_error']}")

    if stats['changes_by_type']:
        logger.info("Changes by type:")
        for change_type, count in sorted(stats['changes_by_type'].items(), key=lambda x: -x[1]):
            logger.info(f"  - {change_type}: {count}")

    if args.dry_run:
        logger.info("[DRY RUN] No changes were saved.")
    else:
        logger.info("All changes have been saved.")

    logger.info("=" * 60)


if __name__ == "__main__":
    main()
