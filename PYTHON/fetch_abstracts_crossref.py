#!/usr/bin/env python3
"""
Fetch abstracts from CrossRef API for papers missing abstracts.

CrossRef API is authoritative for DOI metadata and has better coverage
than Semantic Scholar. Falls back to OpenAlex for papers without DOIs.

Usage:
    python3 PYTHON/fetch_abstracts_crossref.py [--dry-run] [--verbose]

Rate Limiting:
    - CrossRef: 1 request/second (respectful crawling)
    - OpenAlex: No official limit but 1 request/second to be safe
"""

import re
import sys
import time
import json
import logging
import requests
from pathlib import Path
from yaml_frontmatter_utils import read_paper, write_paper, validate_frontmatter, parse_frontmatter, rebuild_frontmatter

logger = logging.getLogger(__name__)

# Configuration
PAPERS_DIR = Path("papers")
BASE_CSV = Path("Base.md")
DRY_RUN = "--dry-run" in sys.argv
VERBOSE = "--verbose" in sys.argv

# API endpoints
CROSSREF_API = "https://api.crossref.org/works"
OPENALEX_API = "https://api.openalex.org/works"

def extract_doi(frontmatter):
    """Extract DOI from frontmatter."""
    for field in ["DOI", "doi", "Doi"]:
        if field in frontmatter:
            doi = frontmatter[field].strip()
            # Clean DOI format
            doi = re.sub(r'^https?://doi\.org/', '', doi)
            doi = re.sub(r'^doi:', '', doi, flags=re.IGNORECASE)
            return doi
    return None

def extract_arxiv_id(frontmatter):
    """Extract arXiv ID from frontmatter."""
    url = frontmatter.get("URL", "")
    arxiv_match = re.search(r'arxiv\.org/abs/(\d+\.\d+)', url)
    if arxiv_match:
        return arxiv_match.group(1)
    return None

def fetch_from_crossref(doi):
    """Fetch abstract from CrossRef API using DOI."""
    try:
        params = {
            "mailto": "user@example.com",  # CrossRef polite pool
            "select": "title,abstract,author,published"
        }
        response = requests.get(f"{CROSSREF_API}/{doi}", params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        if data.get("status") == "ok" and "message" in data:
            msg = data["message"]
            abstract = msg.get("abstract")
            if abstract:
                # Clean up abstract
                abstract = abstract.strip()
                # Limit to reasonable length
                if len(abstract) > 1000:
                    abstract = abstract[:997] + "..."
                return abstract
    except Exception as e:
        if VERBOSE:
            logger.debug(f"    CrossRef error for {doi}: {e}")
    return None

def fetch_from_openalex(title, author=None):
    """Fetch abstract from OpenAlex API using title."""
    try:
        # Query by title
        params = {
            "filter": f"title.search:{title}",
            "select": "id,title,abstract,author_names"
        }
        response = requests.get(OPENALEX_API, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            # Get first result
            result = data["results"][0]
            abstract = result.get("abstract")
            if abstract:
                abstract = abstract.strip()
                if len(abstract) > 1000:
                    abstract = abstract[:997] + "..."
                return abstract
    except Exception as e:
        if VERBOSE:
            logger.debug(f"    OpenAlex error for '{title}': {e}")
    return None

def fetch_abstract(paper_path, dry_run=False):
    """Fetch abstract from APIs for a single paper."""
    fm_text, body = read_paper(paper_path)
    frontmatter = parse_frontmatter(fm_text)
    paper_stem = paper_path.stem

    # Skip if already has abstract
    if frontmatter.get("Abstract Note"):
        return None

    # Try CrossRef first (DOI)
    doi = extract_doi(frontmatter)
    if doi:
        abstract = fetch_from_crossref(doi)
        if abstract:
            if not dry_run:
                frontmatter["Abstract Note"] = abstract
                fm_rebuilt = rebuild_frontmatter(frontmatter)
                is_valid, issues = validate_frontmatter(fm_rebuilt)
                if is_valid:
                    write_paper(paper_path, fm_rebuilt, body, validate=True)
                    if VERBOSE:
                        logger.info(f"  ✓ Fetched via CrossRef: {paper_stem}")
                    return "crossref"
                else:
                    if VERBOSE:
                        logger.error(f"  ✗ YAML invalid: {paper_stem}")
                    return None
            return "crossref"
        time.sleep(1)  # Rate limit: 1 req/sec

    # Try OpenAlex by title
    title = frontmatter.get("Title", "")
    if title and len(title) > 3:
        abstract = fetch_from_openalex(title)
        if abstract:
            if not dry_run:
                frontmatter["Abstract Note"] = abstract
                fm_rebuilt = rebuild_frontmatter(frontmatter)
                is_valid, issues = validate_frontmatter(fm_rebuilt)
                if is_valid:
                    write_paper(paper_path, fm_rebuilt, body, validate=True)
                    if VERBOSE:
                        logger.info(f"  ✓ Fetched via OpenAlex: {paper_stem}")
                    return "openalex"
                else:
                    if VERBOSE:
                        logger.error(f"  ✗ YAML invalid: {paper_stem}")
                    return None
            return "openalex"
        time.sleep(1)  # Rate limit: 1 req/sec

    return None

def main():
    """Process all papers."""
    papers = sorted([p for p in PAPERS_DIR.glob("*.md")])

    logger.info("=" * 60)
    logger.info("ABSTRACT FETCH VIA CROSSREF & OPENALEX")
    logger.info("=" * 60)
    logger.info(f"\nFound {len(papers)} papers to check for abstracts")
    logger.info(f"Mode: {'DRY-RUN' if DRY_RUN else 'EXECUTION'}")
    logger.info("\nAttempting to fetch via:")
    logger.info("  - CrossRef API (DOI lookup)")
    logger.info("  - OpenAlex API (Title search)")
    logger.info("")

    stats = {
        "processed": 0,
        "already_had": 0,
        "fetched_crossref": 0,
        "fetched_openalex": 0,
        "total_fetched": 0,
        "errors": 0,
        "no_identifier": 0
    }

    for i, paper_path in enumerate(papers, 1):
        fm_text, _ = read_paper(paper_path)
        frontmatter = parse_frontmatter(fm_text)
        paper_stem = paper_path.stem

        # Progress indicator every 50 papers
        if i % 50 == 0:
            logger.info(f"[{i}/{len(papers)}] {paper_stem}")

        # Check if already has abstract
        if frontmatter.get("Abstract Note"):
            stats["already_had"] += 1
            stats["processed"] += 1
            continue

        # Try to fetch
        result = fetch_abstract(paper_path, dry_run=DRY_RUN)
        stats["processed"] += 1

        if result == "crossref":
            stats["fetched_crossref"] += 1
            stats["total_fetched"] += 1
        elif result == "openalex":
            stats["fetched_openalex"] += 1
            stats["total_fetched"] += 1
        else:
            stats["errors"] += 1

    # Print summary
    logger.info("\n" + "=" * 60)
    logger.info("ABSTRACT FETCH SUMMARY (CrossRef & OpenAlex)")
    logger.info("=" * 60)
    logger.info(f"Papers processed: {stats['processed']}")
    logger.info(f"Already had abstracts: {stats['already_had']}")
    logger.info(f"Fetched via CrossRef: {stats['fetched_crossref']}")
    logger.info(f"Fetched via OpenAlex: {stats['fetched_openalex']}")
    logger.info(f"TOTAL FETCHED: {stats['total_fetched']}")

    if stats['processed'] > stats['already_had']:
        attempted = stats['processed'] - stats['already_had']
        fetch_rate = (stats['total_fetched'] / attempted * 100) if attempted > 0 else 0
        logger.info(f"Fetch rate: {fetch_rate:.1f}%")

    logger.info(f"Errors: {stats['errors']}")
    logger.info(f"Mode: {'DRY-RUN (no papers modified)' if DRY_RUN else 'EXECUTED (papers modified)'}")
    logger.info("")

if __name__ == "__main__":
    main()
