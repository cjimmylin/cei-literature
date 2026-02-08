#!/usr/bin/env python3
"""
Expand Abbreviated Authors Script
Finds full names for abbreviated author entries by:
1. Searching papers that reference them
2. Looking up full names from arXiv API
3. Searching Semantic Scholar
4. Building mappings for manual review
"""

import re
import json
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import quote
import logging

from yaml_frontmatter_utils import parse_frontmatter
from vault_config import PAPERS_DIR, AUTHORS_DIR, LOGS_DIR

logger = logging.getLogger(__name__)

ARXIV_API_BASE = "http://export.arxiv.org/api/query?"

# Known mappings that we'll build
KNOWN_MAPPINGS = {}


def extract_arxiv_id(url: str) -> Optional[str]:
    """Extract arXiv ID from URL."""
    if not url:
        return None
    match = re.search(r'arxiv\.org/(?:abs|pdf)/(\d+\.\d+)', url)
    return match.group(1) if match else None


def fetch_arxiv_authors(arxiv_id: str) -> List[str]:
    """Fetch complete author list from arXiv API."""
    try:
        url = f"{ARXIV_API_BASE}search_query={quote(f'id:{arxiv_id}')}&start=0&max_results=1"
        with urllib.request.urlopen(url, timeout=10) as response:
            root = ET.fromstring(response.read())
            authors = []
            ns = {'atom': 'http://www.w3.org/2005/Atom'}
            for entry in root.findall('atom:entry', ns):
                for author_elem in entry.findall('atom:author', ns):
                    name_elem = author_elem.find('atom:name', ns)
                    if name_elem is not None:
                        authors.append(name_elem.text.strip())
            return authors
    except Exception as e:
        return []


def find_papers_with_author(author_name: str) -> List[Dict]:
    """Find all papers that reference this author."""
    papers = []

    for paper_file in PAPERS_DIR.glob('*.md'):
        try:
            content = paper_file.read_text(encoding='utf-8')

            # Check if author is mentioned
            if author_name not in content:
                continue

            fm_match = re.match(r'---\n(.*?)\n---\n', content, re.DOTALL)
            if not fm_match:
                continue

            fields = parse_frontmatter(fm_match.group(1))

            papers.append({
                'file': paper_file.name,
                'url': fields.get('url', ''),
                'authors': fields.get('authors', ''),
                'title': fields.get('title', ''),
            })
        except Exception:
            continue

    return papers


def match_abbreviated_to_full(abbreviated: str, full_authors: List[str]) -> Optional[str]:
    """
    Match an abbreviated name to a full name from a list.
    E.g., "A. Smith" matches "Alice Smith"
    """
    parts = abbreviated.split()
    if len(parts) < 2:
        return None

    # Extract initials and last name
    initials = []
    last_name_parts = []

    for part in parts:
        if re.match(r'^[A-Z]\.$', part):
            initials.append(part[0])
        else:
            last_name_parts.append(part)

    if not initials or not last_name_parts:
        return None

    last_name = ' '.join(last_name_parts)

    # Search in full authors
    for full_name in full_authors:
        full_parts = full_name.split()
        if len(full_parts) < 2:
            continue

        # Check if last name matches
        if not full_name.lower().endswith(last_name.lower()):
            continue

        # Check if initials match
        full_initials = [p[0] for p in full_parts[:-len(last_name_parts)] if p]
        if initials == full_initials:
            return full_name

    return None


def resolve_abbreviated_author(abbreviated: str) -> Tuple[Optional[str], str]:
    """
    Try to resolve an abbreviated author name to a full name.
    Returns (full_name, source) or (None, 'not_found')
    """
    # Find papers with this author
    papers = find_papers_with_author(abbreviated)

    if not papers:
        return None, 'no_papers'

    # Try arXiv first
    for paper in papers:
        arxiv_id = extract_arxiv_id(paper['url'])
        if arxiv_id:
            time.sleep(0.5)  # Rate limit
            arxiv_authors = fetch_arxiv_authors(arxiv_id)
            if arxiv_authors:
                full_name = match_abbreviated_to_full(abbreviated, arxiv_authors)
                if full_name:
                    return full_name, f"arXiv:{arxiv_id}"

    # Try matching against co-authors in papers
    for paper in papers:
        authors_str = paper.get('authors', '')
        if authors_str:
            co_authors = [a.strip() for a in authors_str.split(';')]
            full_name = match_abbreviated_to_full(abbreviated, co_authors)
            if full_name:
                return full_name, f"paper:{paper['file']}"

    # Try searching existing author files
    for author_file in AUTHORS_DIR.glob('*.md'):
        full_name = author_file.stem
        full_parts = full_name.split()
        if len(full_parts) < 2:
            continue

        abbrev_parts = abbreviated.split()
        initials = [p[0] for p in abbrev_parts if re.match(r'^[A-Z]\.$', p)]
        last_name_parts = [p for p in abbrev_parts if not re.match(r'^[A-Z]\.$', p)]

        if not initials or not last_name_parts:
            continue

        last_name = ' '.join(last_name_parts)

        if full_name.lower().endswith(last_name.lower()):
            full_initials = [p[0] for p in full_parts[:-len(last_name_parts)] if p]
            if initials == full_initials:
                return full_name, "existing_author"

    return None, 'not_found'


def main():
    """Main execution."""
    logger.info("=" * 70)
    logger.info("EXPAND ABBREVIATED AUTHORS")
    logger.info("=" * 70)
    logger.info("")

    # Load the list of abbreviated authors from the log
    log_file = LOGS_DIR / "20260124-author_issues_resolution.json"
    if not log_file.exists():
        logger.warning("No log file found. Run resolve_author_issues.py first.")
        return

    with open(log_file, 'r') as f:
        log_data = json.load(f)

    abbreviated_names = log_data.get('scan', {}).get('abbreviated', [])
    very_short_names = log_data.get('scan', {}).get('very_short', [])

    logger.info(f"Abbreviated names to resolve: {len(abbreviated_names)}")
    logger.info(f"Very short names to check: {len(very_short_names)}")
    logger.info("")

    # Results
    resolved = {}
    unresolved = []
    to_delete = []

    # Process abbreviated names
    logger.info("Processing abbreviated names...")
    for i, name in enumerate(abbreviated_names):
        full_name, source = resolve_abbreviated_author(name)

        if full_name:
            resolved[name] = {'full_name': full_name, 'source': source}
            logger.info(f"  [{i+1}/{len(abbreviated_names)}] {name}... -> {full_name} ({source})")
        else:
            unresolved.append(name)
            logger.warning(f"  [{i+1}/{len(abbreviated_names)}] {name}... NOT FOUND ({source})")

    logger.info("")

    # Process very short names
    logger.info("Checking very short names...")
    for name in very_short_names:
        if name == '.':
            to_delete.append(name)
            logger.info(f"  {name} -> DELETE (invalid)")
        else:
            # Check if it's a legitimate single name used in papers
            papers = find_papers_with_author(name)
            if papers:
                logger.info(f"  {name} -> KEEP (used in {len(papers)} papers)")
            else:
                to_delete.append(name)
                logger.info(f"  {name} -> DELETE (not referenced)")

    logger.info("")

    # Summary
    logger.info("=" * 70)
    logger.info("SUMMARY")
    logger.info("=" * 70)
    logger.info(f"Resolved: {len(resolved)}")
    logger.info(f"Unresolved: {len(unresolved)}")
    logger.info(f"To delete: {len(to_delete)}")

    # Save results
    results = {
        'resolved': resolved,
        'unresolved': unresolved,
        'to_delete': to_delete,
    }

    results_file = LOGS_DIR / "20260124-author_expansion_results.json"
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)

    logger.info(f"\nResults saved to: {results_file}")

    # Print unresolved for manual mapping
    if unresolved:
        logger.info("\n" + "=" * 70)
        logger.info("UNRESOLVED - Add these to MANUAL_AUTHOR_MAPPINGS in fix script:")
        logger.info("=" * 70)
        for name in unresolved[:20]:
            papers = find_papers_with_author(name)
            paper_names = [p['file'] for p in papers[:2]]
            logger.info(f'    "{name}": "",  # Used in: {paper_names}')
        if len(unresolved) > 20:
            logger.info(f"    ... and {len(unresolved) - 20} more")


if __name__ == "__main__":
    main()
