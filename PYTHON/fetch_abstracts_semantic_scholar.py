#!/usr/bin/env python3
"""
Fetch Abstracts via Semantic Scholar API - Priority 2 Strategy

Uses Semantic Scholar API to fetch abstracts for papers that:
1. Don't have local PDFs
2. Don't have abstracts yet
3. Have URLs with resolvable metadata

This is more effective than trying to download paywalled PDFs.

Usage:
    python3 fetch_abstracts_semantic_scholar.py                  # Process all
    python3 fetch_abstracts_semantic_scholar.py --dry-run        # Preview
    python3 fetch_abstracts_semantic_scholar.py --verbose        # Show progress
    python3 fetch_abstracts_semantic_scholar.py "2016-Amodei"    # Specific paper
"""

import os
import sys
import argparse
import re
import time
import logging
import requests
from pathlib import Path

logger = logging.getLogger(__name__)

# Import utilities
from yaml_frontmatter_utils import (
    extract_frontmatter,
    parse_frontmatter,
    rebuild_frontmatter,
    write_paper,
    validate_frontmatter,
)


# Directories
PAPER_DIR = "papers"
SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/v1/paper"
API_TIMEOUT = 10
RATE_LIMIT_DELAY = 0.5  # seconds between requests


class FetchStats:
    """Track fetch statistics."""
    def __init__(self):
        self.processed = 0
        self.already_have = 0
        self.fetched_via_doi = 0
        self.fetched_via_arxiv = 0
        self.fetched_via_title = 0
        self.errors = []
        self.no_url = 0

    def report(self):
        logger.info("\n" + "=" * 60)
        logger.info("ABSTRACT FETCH SUMMARY (Semantic Scholar API)")
        logger.info("=" * 60)
        logger.info(f"Papers processed: {self.processed}")
        logger.info(f"Already had abstracts: {self.already_have}")
        logger.info(f"Fetched via DOI: {self.fetched_via_doi}")
        logger.info(f"Fetched via arXiv: {self.fetched_via_arxiv}")
        logger.info(f"Fetched via Title: {self.fetched_via_title}")
        total_fetched = (self.fetched_via_doi + self.fetched_via_arxiv +
                        self.fetched_via_title)
        logger.info(f"TOTAL FETCHED: {total_fetched}")
        logger.info(f"Fetch rate: {(total_fetched/max(self.processed, 1)*100):.1f}%")
        logger.info(f"Errors: {len(self.errors)}")
        logger.info(f"No URL: {self.no_url}")

        if self.errors:
            logger.info("\nSample errors:")
            for paper, error in self.errors[:5]:
                logger.info(f"  - {paper}: {error}")


stats = FetchStats()


def extract_arxiv_id(url):
    """Extract arXiv ID from URL."""
    patterns = [
        r'arxiv\.org/abs/(\d{4}\.\d{4,5})',
        r'arxiv\.org/pdf/(\d{4}\.\d{4,5})',
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def extract_doi(url):
    """Extract DOI from URL."""
    patterns = [
        r'doi\.org/(10\.\S+)',
        r'doi\.apa\.org/doi/(10\.\S+)',
        r'(10\.\d+/\S+)',
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1).rstrip('/;?')
    return None


def fetch_from_semantic_scholar(identifier, id_type, paper_stem, dry_run=False, verbose=False):
    """
    Fetch paper metadata from Semantic Scholar API.

    Args:
        identifier: DOI, arXiv ID, or title
        id_type: "doi", "arxiv_id", or "title"
        paper_stem: Paper filename stem
        dry_run: If True, don't write files
        verbose: If True, show details

    Returns: Abstract text or None
    """
    try:
        # Build query URL
        if id_type == "doi":
            query_url = f"{SEMANTIC_SCHOLAR_API}/{identifier}"
        elif id_type == "arxiv_id":
            query_url = f"{SEMANTIC_SCHOLAR_API}/arXiv:{identifier}"
        elif id_type == "title":
            # Title search is different
            query_url = "https://api.semanticscholar.org/graph/v1/paper/search"
            params = {"query": identifier, "limit": 1}
            response = requests.get(query_url, params=params, timeout=API_TIMEOUT)
            if response.status_code == 200:
                data = response.json()
                if data.get('data') and len(data['data']) > 0:
                    return data['data'][0].get('abstract')
            return None
        else:
            return None

        # Make request
        response = requests.get(query_url, timeout=API_TIMEOUT)

        if response.status_code == 200:
            data = response.json()
            abstract = data.get('abstract')
            if abstract:
                # Clean up abstract
                abstract = abstract.strip()
                abstract = re.sub(r'\s+', ' ', abstract)
                abstract = abstract.replace('"', "'")
                abstract = abstract[:500]  # Limit length
                return abstract

        return None

    except Exception as e:
        if verbose:
            logger.warning(f"  API error: {e}")
        return None


def fetch_abstract(paper_path, dry_run=False, verbose=False):
    """
    Fetch abstract for a paper.

    Returns: (success, source)
    """
    paper_stem = os.path.splitext(os.path.basename(paper_path))[0]

    try:
        # Read paper metadata
        content = paper_path.read_text(encoding='utf-8')
        fm, body = extract_frontmatter(content)

        # Validate YAML
        is_valid, issues = validate_frontmatter(fm)
        if not is_valid:
            stats.errors.append((paper_stem, "Invalid YAML"))
            return False, "invalid_yaml"

        fields = parse_frontmatter(fm)

        # Check if already have abstract
        if fields.get('abstract'):
            stats.already_have += 1
            if verbose:
                logger.debug(f"  {paper_stem}: Already has abstract")
            return False, "already_have"

        # Get URL
        url = fields.get('url', '').strip()
        if not url:
            stats.no_url += 1
            if verbose:
                logger.debug(f"  {paper_stem}: No URL")
            return False, "no_url"

        stats.processed += 1

        # Strategy 1: Try DOI
        doi = extract_doi(url)
        if doi:
            abstract = fetch_from_semantic_scholar(doi, "doi", paper_stem, dry_run, verbose)
            if abstract:
                if not dry_run:
                    fields['abstract'] = abstract
                    new_fm = rebuild_frontmatter(fields)
                    is_valid, issues = validate_frontmatter(new_fm)
                    if is_valid:
                        write_paper(paper_path, new_fm, body, validate=True)
                    else:
                        stats.errors.append((paper_stem, f"YAML validation failed"))
                        return False, "yaml_error"

                stats.fetched_via_doi += 1
                if verbose:
                    logger.info(f"  {paper_stem}: Fetched from Semantic Scholar (DOI)")
                return True, "doi"

        # Strategy 2: Try arXiv
        arxiv_id = extract_arxiv_id(url)
        if arxiv_id:
            abstract = fetch_from_semantic_scholar(arxiv_id, "arxiv_id", paper_stem, dry_run, verbose)
            if abstract:
                if not dry_run:
                    fields['abstract'] = abstract
                    new_fm = rebuild_frontmatter(fields)
                    is_valid, issues = validate_frontmatter(new_fm)
                    if is_valid:
                        write_paper(paper_path, new_fm, body, validate=True)
                    else:
                        stats.errors.append((paper_stem, "YAML validation failed"))
                        return False, "yaml_error"

                stats.fetched_via_arxiv += 1
                if verbose:
                    logger.info(f"  {paper_stem}: Fetched from Semantic Scholar (arXiv)")
                return True, "arxiv"

        if verbose:
            logger.debug(f"  {paper_stem}: No abstract found via API")

        stats.errors.append((paper_stem, "Not found in Semantic Scholar"))
        return False, "not_found"

    except Exception as e:
        stats.errors.append((paper_stem, str(e)))
        if verbose:
            logger.error(f"  {paper_stem}: Error - {e}")
        return False, "error"


def fetch_all_missing(target_paper=None, dry_run=False, verbose=False):
    """
    Fetch abstracts for papers that need them.

    Args:
        target_paper: Optional paper stem to process
        dry_run: If True, don't write files
        verbose: If True, show detailed progress
    """
    if not os.path.exists(PAPER_DIR):
        logger.error(f"Error: Papers directory '{PAPER_DIR}' not found")
        sys.exit(1)

    if target_paper:
        # Process single paper
        paper_path = Path(PAPER_DIR) / (target_paper + ".md")
        if not paper_path.exists():
            logger.error(f"Error: Paper '{target_paper}.md' not found")
            sys.exit(1)

        logger.info(f"Fetching abstract for: {target_paper}\n")
        fetch_abstract(paper_path, dry_run, verbose)
    else:
        # Process all papers
        papers = sorted(Path(PAPER_DIR).glob("*.md"))
        total = len(papers)

        logger.info(f"Found {total} papers to check for abstracts\n")
        logger.info("Attempting to fetch via Semantic Scholar API:")
        logger.info("  - DOI lookup")
        logger.info("  - arXiv lookup")
        logger.info("  - Title search (if needed)")
        logger.info("")

        for i, paper_path in enumerate(papers, 1):
            if verbose or i % 50 == 0:
                logger.info(f"[{i}/{total}] {paper_path.name}")

            fetch_abstract(paper_path, dry_run, verbose)

            # Rate limiting
            time.sleep(RATE_LIMIT_DELAY)

    stats.report()


def main():
    parser = argparse.ArgumentParser(
        description="Fetch abstracts via Semantic Scholar API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 fetch_abstracts_semantic_scholar.py                # Fetch all
  python3 fetch_abstracts_semantic_scholar.py --dry-run      # Preview
  python3 fetch_abstracts_semantic_scholar.py --verbose      # Show progress
  python3 fetch_abstracts_semantic_scholar.py "2016-Amodei"  # Fetch specific
        """
    )
    parser.add_argument('paper', nargs='?', help='Specific paper stem')
    parser.add_argument('--dry-run', '-n', action='store_true',
                        help="Don't write files, just show what would happen")
    parser.add_argument('--verbose', '-v', action='store_true',
                        help="Show detailed progress information")

    args = parser.parse_args()

    if args.dry_run:
        logger.info("=" * 60)
        logger.info("DRY RUN MODE - No files will be modified")
        logger.info("=" * 60 + "\n")

    fetch_all_missing(
        target_paper=args.paper,
        dry_run=args.dry_run,
        verbose=args.verbose
    )


if __name__ == "__main__":
    main()
