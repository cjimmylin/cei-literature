#!/usr/bin/env python3
"""
Comprehensive Paper Cleanup Script
Fixes errors, duplicates, inconsistencies, and formatting issues
"""

import re
import sys
from pathlib import Path
from collections import defaultdict
import logging

# Add project root for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from PYTHON.yaml_frontmatter_utils import extract_frontmatter, parse_frontmatter
from PYTHON.vault_config import PAPERS_DIR, PDFS_DIR
from PYTHON.ethics_scoring import is_ethics_yes, parse_ethics_value

logger = logging.getLogger(__name__)

# Type mapping for normalization
TYPE_MAPPING = {
    'journal article': 'journalArticle',
    'journalarticle': 'journalArticle',
    'conference paper': 'conferencePaper',
    'conferencepaper': 'conferencePaper',
    'workshop paper': 'conferencePaper',  # Treat workshop papers as conference papers
    'book chapter': 'bookSection',
    'bookchapter': 'bookSection',
    'edited volume': 'book',
    'article': 'journalArticle',
}


def fix_duplicate_citations(body):
    """Remove duplicate citation entries in body"""
    # Find the Citation Info section
    citation_match = re.search(r'## Citation Info\s*\n+(.*?)(?=\n##|\Z)', body, re.DOTALL)
    if not citation_match:
        return body, 0

    citation_section = citation_match.group(1).strip()

    # Extract individual citation lines
    citations = re.findall(r'(\d+ citations \([^)]+\) \[\d{4}-\d{2}-\d{2}\])', citation_section)

    if len(citations) <= 1:
        return body, 0

    # Keep unique citations, preserving order
    seen = set()
    unique_citations = []
    for c in citations:
        if c not in seen:
            seen.add(c)
            unique_citations.append(c)

    if len(unique_citations) == len(citations):
        return body, 0  # No duplicates

    # Rebuild citation section with unique citations
    new_citation_content = ' '.join(unique_citations)

    # Replace the citation section
    new_body = body[:citation_match.start(1)] + new_citation_content + '\n' + body[citation_match.end(1):]

    return new_body, len(citations) - len(unique_citations)


def fix_local_pdf_format(frontmatter_text, frontmatter_dict):
    """Fix local_pdf to use wikilink format"""
    local_pdf = frontmatter_dict.get('local_pdf', '')
    if not local_pdf or local_pdf == 'N/A':
        return frontmatter_text, False

    # Skip if already in wikilink format
    if local_pdf.startswith('[[') and local_pdf.endswith(']]'):
        return frontmatter_text, False

    # Convert to wikilink format
    if local_pdf.startswith('PDFs/'):
        new_value = f'[[{local_pdf}]]'
    else:
        new_value = f'[[PDFs/{local_pdf}]]'

    # Replace in frontmatter
    pattern = rf'(local_pdf:\s*)["\']?{re.escape(local_pdf)}["\']?'
    new_frontmatter = re.sub(pattern, rf'\1"{new_value}"', frontmatter_text)

    if new_frontmatter == frontmatter_text:
        # Try simpler pattern
        new_frontmatter = re.sub(r'local_pdf:\s*.+', f'local_pdf: "{new_value}"', frontmatter_text)

    return new_frontmatter, new_frontmatter != frontmatter_text


def fix_type_value(frontmatter_text, frontmatter_dict):
    """Normalize type field to valid values"""
    item_type = frontmatter_dict.get('type', '')
    if not item_type:
        return frontmatter_text, False

    type_lower = item_type.lower().strip()
    if type_lower in TYPE_MAPPING:
        new_type = TYPE_MAPPING[type_lower]
        pattern = rf'(type:\s*)["\']?{re.escape(item_type)}["\']?'
        new_frontmatter = re.sub(pattern, rf'\1{new_type}', frontmatter_text)
        return new_frontmatter, new_frontmatter != frontmatter_text

    return frontmatter_text, False


def fix_ethics_consistency(frontmatter_text, frontmatter_dict):
    """Fix ethics_overall to be Yes/high-score if any specific ethics is Yes/high-score"""
    ethics_overall = frontmatter_dict.get('ethics_overall', '')
    virtue = frontmatter_dict.get('virtue_ethics', '')
    deonto = frontmatter_dict.get('deontological_ethics', '')
    util = frontmatter_dict.get('utilitarian_ethics', '')

    # If any specific ethics is Yes/>=50 but overall is No/<50, fix it
    overall_yes = is_ethics_yes(ethics_overall)
    any_specific_yes = (is_ethics_yes(virtue) or is_ethics_yes(deonto) or is_ethics_yes(util))

    if not overall_yes and any_specific_yes:
        # Determine the new value: use max of specific scores if numeric, else "Yes"
        specific_values = [parse_ethics_value(v) for v in [virtue, deonto, util]]
        new_val = max(specific_values) if any(isinstance(v, int) for v in [parse_ethics_value(virtue), parse_ethics_value(deonto), parse_ethics_value(util)]) else '"Yes"'
        if isinstance(new_val, int):
            new_frontmatter = re.sub(r'ethics_overall:\s*["\']?[^"\'\n]+["\']?', f'ethics_overall: {new_val}', frontmatter_text)
        else:
            new_frontmatter = re.sub(r'ethics_overall:\s*["\']?[^"\'\n]+["\']?', f'ethics_overall: {new_val}', frontmatter_text)
        return new_frontmatter, new_frontmatter != frontmatter_text

    return frontmatter_text, False


def fix_body_abstract_placeholder(body, abstract):
    """Remove 'No abstract available' placeholder if abstract exists"""
    if not abstract or abstract == 'N/A':
        return body, False

    # Check if body has placeholder
    if '*No abstract available in source.*' not in body:
        return body, False

    # Replace with actual abstract
    new_body = body.replace('*No abstract available in source.*', abstract)
    return new_body, new_body != body


def fix_author_wikilinks_format(body):
    """Fix author wikilinks that use 'LastName, FirstName' format"""
    # Pattern to find broken wikilinks like [[LastName, FirstName
    # These are missing the closing ]]

    # First, fix incomplete wikilinks
    # Pattern: [[Name, Name without closing ]]
    lines = body.split('\n')
    fixed_lines = []
    changes = 0

    for line in lines:
        # Find patterns like [[Name, Name]] and convert to [[FirstName LastName]]
        matches = re.findall(r'\[\[([^,\]]+),\s*([^\]]+)\]\]', line)
        for last, first in matches:
            old = f'[[{last}, {first}]]'
            new = f'[[{first.strip()} {last.strip()}]]'
            if old in line:
                line = line.replace(old, new)
                changes += 1

        fixed_lines.append(line)

    return '\n'.join(fixed_lines), changes


def clean_paper(filepath, dry_run=False):
    """Clean a single paper file"""
    changes = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return [], f"Cannot read: {e}"

    try:
        frontmatter_text, body = extract_frontmatter(content)
        frontmatter_dict = parse_frontmatter(frontmatter_text)
    except Exception as e:
        return [], f"YAML error: {e}"

    new_frontmatter = frontmatter_text
    new_body = body
    modified = False

    # Fix 1: Duplicate citations
    new_body, dup_count = fix_duplicate_citations(new_body)
    if dup_count > 0:
        changes.append(f"Removed {dup_count} duplicate citation(s)")
        modified = True

    # Fix 2: local_pdf format
    new_frontmatter, changed = fix_local_pdf_format(new_frontmatter, frontmatter_dict)
    if changed:
        changes.append("Fixed local_pdf wikilink format")
        modified = True

    # Fix 3: Type normalization
    new_frontmatter, changed = fix_type_value(new_frontmatter, frontmatter_dict)
    if changed:
        changes.append("Normalized type value")
        modified = True

    # Fix 4: Ethics consistency
    new_frontmatter, changed = fix_ethics_consistency(new_frontmatter, frontmatter_dict)
    if changed:
        changes.append("Fixed ethics_overall consistency")
        modified = True

    # Fix 5: Body abstract placeholder
    abstract = frontmatter_dict.get('abstract', '')
    new_body, changed = fix_body_abstract_placeholder(new_body, abstract)
    if changed:
        changes.append("Replaced abstract placeholder with actual abstract")
        modified = True

    # Fix 6: Author wikilink format
    new_body, author_changes = fix_author_wikilinks_format(new_body)
    if author_changes > 0:
        changes.append(f"Fixed {author_changes} author wikilink format(s)")
        modified = True

    # Write changes if not dry run
    if modified and not dry_run:
        new_content = f"---\n{new_frontmatter.strip()}\n---\n{new_body}"
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
        except Exception as e:
            return changes, f"Write error: {e}"

    return changes, None


def find_duplicate_papers():
    """Find papers that are likely duplicates"""
    papers_by_doi = defaultdict(list)
    papers_by_title = defaultdict(list)

    for filepath in PAPERS_DIR.glob("*.md"):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            frontmatter_text, _ = extract_frontmatter(content)
            fm = parse_frontmatter(frontmatter_text)

            doi = fm.get('doi', '').strip()
            title = (fm.get('short_title') or filepath.stem).lower()

            if doi and doi != 'N/A':
                papers_by_doi[doi].append(filepath.name)
            if title:
                papers_by_title[title].append(filepath.name)
        except Exception:
            pass  # Skip papers that cannot be read or parsed

    duplicates = {
        'doi': {k: v for k, v in papers_by_doi.items() if len(v) > 1},
        'title': {k: v for k, v in papers_by_title.items() if len(v) > 1}
    }

    return duplicates


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Clean paper files')
    parser.add_argument('--dry-run', action='store_true', help='Show changes without applying')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    args = parser.parse_args()

    logger.info("=" * 60)
    logger.info("COMPREHENSIVE PAPER CLEANUP")
    logger.info("=" * 60)

    if args.dry_run:
        logger.info("DRY RUN - No changes will be saved\n")

    # Clean all papers
    paper_files = list(PAPERS_DIR.glob("*.md"))
    total = len(paper_files)

    logger.info(f"Processing {total} papers...\n")

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
                change_type = change.split()[0] + change.split()[1] if len(change.split()) > 1 else change
                stats['changes_by_type'][change_type] += 1
            if args.verbose:
                logger.info(f"  CLEANED {filepath.name}:")
                for c in changes:
                    logger.info(f"    - {c}")
        else:
            stats['papers_unchanged'] += 1

    logger.info(f"  Progress: {total}/{total}")

    # Find duplicates (informational)
    logger.info("\nChecking for duplicate papers...")
    duplicates = find_duplicate_papers()

    # Print summary
    logger.info("\n" + "=" * 60)
    logger.info("CLEANUP SUMMARY")
    logger.info("=" * 60)
    logger.info(f"Papers cleaned:   {stats['papers_cleaned']}")
    logger.info(f"Papers unchanged: {stats['papers_unchanged']}")
    logger.info(f"Papers with errors: {stats['papers_error']}")

    if stats['changes_by_type']:
        logger.info("\nChanges by type:")
        for change_type, count in sorted(stats['changes_by_type'].items(), key=lambda x: -x[1]):
            logger.info(f"  - {change_type}: {count}")

    if duplicates['doi']:
        logger.info(f"\nDuplicate DOIs found ({len(duplicates['doi'])} sets):")
        for doi, files in list(duplicates['doi'].items())[:5]:
            logger.info(f"  - {doi}: {', '.join(files)}")

    if duplicates['title']:
        logger.info(f"\nDuplicate titles found ({len(duplicates['title'])} sets):")
        for title, files in list(duplicates['title'].items())[:5]:
            logger.info(f"  - {title[:40]}...: {', '.join(files)}")

    if args.dry_run:
        logger.info("\n[DRY RUN] No changes were saved. Run without --dry-run to apply changes.")
    else:
        logger.info("\nAll changes have been saved.")

    logger.info("=" * 60)


if __name__ == "__main__":
    main()
