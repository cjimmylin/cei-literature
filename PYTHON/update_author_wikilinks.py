#!/usr/bin/env python3
"""
Update Author Wikilinks in Papers
This script adds proper author wikilinks to paper body sections.
Run this AFTER complete_author_data_fix.py has updated all author lists.
"""

import re
from pathlib import Path
from typing import List, Set

from yaml_frontmatter_utils import (
    extract_frontmatter,
    parse_frontmatter,
    validate_frontmatter,
    write_paper,
    rebuild_frontmatter,
)

# Import author validation
try:
    from author_validation import (
        validate_author_name,
        normalize_author_name,
        find_full_name_match,
    )
    HAS_VALIDATION = True
except ImportError:
    HAS_VALIDATION = False

from vault_config import PAPERS_DIR, AUTHORS_DIR

RESULTS = {
    "papers_updated": [],
    "papers_skipped": [],
    "papers_failed": [],
    "total_wikilinks_added": 0,
}


def get_existing_authors() -> Set[str]:
    """Get list of all existing author files"""
    authors = set()
    for author_file in AUTHORS_DIR.glob('*.md'):
        authors.add(author_file.stem)
    return authors


def parse_author_list(authors_str: str) -> List[str]:
    """Parse semicolon-separated author list"""
    if not authors_str:
        return []

    authors = authors_str.split(';')
    return [a.strip() for a in authors if a.strip()]


def create_author_wikilink(name: str, existing_authors: Set[str]) -> str:
    """Create wikilink for author name, checking if file exists"""
    name = name.strip()

    if not name:
        return ""

    # Use validation if available
    if HAS_VALIDATION:
        # Normalize the name first
        name = normalize_author_name(name)

        # Validate - skip invalid names
        is_valid, errors, _ = validate_author_name(name)
        if not is_valid:
            return ""  # Don't create wikilink for invalid names

        # Try to expand abbreviated names
        full_name = find_full_name_match(name)
        if full_name:
            name = full_name

    # Check exact match
    if name in existing_authors:
        return f"[[{name}]]"

    # Try variations
    # If "LastName, FirstName" format, try "FirstName LastName"
    if ',' in name:
        parts = [p.strip() for p in name.split(',')]
        if len(parts) == 2:
            reversed_name = f"{parts[1]} {parts[0]}"
            if reversed_name in existing_authors:
                return f"[[{reversed_name}]]"

    # Otherwise create wikilink anyway (author file can be created later)
    return f"[[{name}]]"


def update_paper_wikilinks(paper_path: Path, existing_authors: Set[str]) -> bool:
    """Add author wikilinks to a paper"""
    try:
        content = paper_path.read_text(encoding='utf-8')

        # Extract frontmatter
        fm_match = re.match(r'---\n(.*?)\n---\n', content, re.DOTALL)
        if not fm_match:
            return False

        frontmatter = fm_match.group(1)
        body = content[fm_match.end():]

        # Parse authors
        fields = parse_frontmatter(frontmatter)
        authors_str = fields.get('authors', '')

        if not authors_str:
            RESULTS['papers_skipped'].append((paper_path.name, "No authors field"))
            return False

        author_list = parse_author_list(authors_str)
        if not author_list:
            RESULTS['papers_skipped'].append((paper_path.name, "No authors to link"))
            return False

        # Create wikilinks
        wikilinks = [
            create_author_wikilink(author, existing_authors)
            for author in author_list
        ]
        wikilinks = [w for w in wikilinks if w]  # Remove empty strings

        if not wikilinks:
            return False

        # Check if paper already has an Authors section
        if re.search(r'## Authors?', body, re.IGNORECASE):
            # Update existing Authors section
            author_section_pattern = r'(## Authors?)\n\n[^\n]+'
            replacement = f"\\1\n\n{', '.join(wikilinks)}"
            new_body = re.sub(author_section_pattern, replacement, body, count=1)

            if new_body == body:
                # Section found but pattern didn't match, just replace the content
                new_body = re.sub(
                    r'(## Authors?)\n\n([^\n]+)',
                    f"\\1\n\n{', '.join(wikilinks)}",
                    body,
                    count=1
                )
        else:
            # Add new Authors section after the title/abstract area
            # Find a good insertion point (after Abstract or Notes section)
            insert_point = len(body)

            # Try to find ## section headers to insert before next section
            section_match = re.search(r'## (?!Notes|Citation)', body)
            if section_match:
                insert_point = section_match.start()

            new_body = (
                body[:insert_point].rstrip() +
                f"\n\n## Authors\n\n{', '.join(wikilinks)}\n" +
                body[insert_point:]
            )

        # Write back
        write_paper(paper_path, frontmatter, new_body, validate=True)

        RESULTS['papers_updated'].append(paper_path.name)
        RESULTS['total_wikilinks_added'] += len(wikilinks)

        return True

    except Exception as e:
        RESULTS['papers_failed'].append((paper_path.name, str(e)))
        return False


def main(limit: int = None):
    """Main execution"""
    print("=" * 100)
    print("UPDATE AUTHOR WIKILINKS IN PAPERS")
    print("=" * 100)
    print()

    # Get existing authors
    print("Loading existing author files...")
    existing_authors = get_existing_authors()
    print(f"✓ Found {len(existing_authors)} author files\n")

    # Get all papers
    print("Scanning papers...")
    papers = sorted(PAPERS_DIR.glob('*.md'))
    if limit:
        papers = papers[:limit]

    print(f"✓ Found {len(papers)} papers\n")

    # Update each paper
    print(f"Updating author wikilinks...")
    for i, paper in enumerate(papers):
        if (i + 1) % 100 == 0:
            print(f"  Progress: {i + 1}/{len(papers)}...")

        update_paper_wikilinks(paper, existing_authors)

    # Report
    print(f"\n" + "=" * 100)
    print("RESULTS")
    print("=" * 100)
    print(f"Papers updated: {len(RESULTS['papers_updated'])}")
    print(f"Papers skipped: {len(RESULTS['papers_skipped'])}")
    print(f"Papers failed: {len(RESULTS['papers_failed'])}")
    print(f"Total wikilinks added: {RESULTS['total_wikilinks_added']}")

    if RESULTS['papers_failed']:
        print("\nFirst 10 failures:")
        for paper, error in RESULTS['papers_failed'][:10]:
            print(f"  - {paper}: {error}")


if __name__ == "__main__":
    import sys

    limit = None
    for arg in sys.argv:
        if arg.startswith("--limit="):
            limit = int(arg.split("=")[1])

    main(limit=limit)
