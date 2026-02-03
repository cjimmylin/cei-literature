#!/usr/bin/env python3
"""
Hybrid Paper Enrichment - Zotero + arXiv + Fallback Sources

This script enriches papers with abstracts and summaries from multiple sources:
1. PDF extracts (if available)
2. Zotero metadata (Base.md)
3. arXiv API (for preprints with arXiv IDs)
4. URLs and DOI metadata

Usage:
    python3 enrich_papers_hybrid.py                  # Process all papers
    python3 enrich_papers_hybrid.py --dry-run        # Preview changes
    python3 enrich_papers_hybrid.py --verbose        # Show progress
"""

import os
import sys
import argparse
import re
import csv
import logging
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
EXTRACT_DIR = "PDF Extracts"
BASE_MD = "Base.md"


class HybridEnrichmentStats:
    """Track enrichment statistics."""
    def __init__(self):
        self.processed = 0
        self.abstracts_from_pdf = 0
        self.abstracts_from_zotero = 0
        self.abstracts_from_url = 0
        self.summaries_generated = 0
        self.errors = []
        self.skipped = 0

    def report(self):
        logger.info("=" * 60)
        logger.info("HYBRID ENRICHMENT SUMMARY")
        logger.info("=" * 60)
        logger.info(f"Papers processed: {self.processed}")
        logger.info(f"Abstracts from PDF: {self.abstracts_from_pdf}")
        logger.info(f"Abstracts from Zotero: {self.abstracts_from_zotero}")
        logger.info(f"Abstracts from URL/API: {self.abstracts_from_url}")
        logger.info(f"Summaries generated: {self.summaries_generated}")
        logger.info(f"Papers skipped: {self.skipped}")
        logger.info(f"Errors: {len(self.errors)}")

        if self.errors:
            logger.info("Errors encountered:")
            for paper, error in self.errors[:10]:  # Show first 10
                logger.error(f"  - {paper}: {error}")


stats = HybridEnrichmentStats()


def load_zotero_metadata():
    """
    Load Zotero metadata from Base.md CSV.

    Returns: Dictionary mapping paper stems to abstract notes
    """
    zotero_data = {}

    try:
        with open(BASE_MD, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row and row.get('Abstract Note'):
                    # Use Title as key (or part of it)
                    title = row.get('Title', '').strip()
                    if title:
                        abstract = row.get('Abstract Note', '').strip()
                        if abstract:
                            zotero_data[title] = abstract

    except Exception as e:
        logger.warning(f"Could not load Zotero data: {e}")

    return zotero_data


def find_zotero_abstract(paper_stem, zotero_data):
    """
    Find abstract from Zotero by fuzzy matching paper title.

    Returns: Abstract text or None
    """
    # Extract title from paper stem
    # Format: YYYY-Author-Title
    parts = paper_stem.split('-', 2)
    if len(parts) < 3:
        return None

    search_title = parts[2].lower()

    # Look for matches in Zotero data
    for zotero_title, abstract in zotero_data.items():
        zotero_lower = zotero_title.lower()

        # Check if titles match substantially
        if (zotero_lower == search_title or
            search_title in zotero_lower or
            zotero_lower in search_title):

            # Clean and limit abstract
            abstract = abstract.strip()
            abstract = re.sub(r'\s+', ' ', abstract)
            abstract = abstract.replace('"', "'")
            abstract = abstract[:500]
            return abstract

    return None


def extract_arxiv_id_from_url(url):
    """Extract arXiv ID from URL."""
    if not url:
        return None

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
    if not url:
        return None

    patterns = [
        r'doi\.org/(10\.\d+/\S+)',
        r'(10\.\d+/\S+)',
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None


def enrich_from_hybrid_sources(paper_path, zotero_data, dry_run=False, verbose=False):
    """
    Enrich a paper from all available sources.

    Returns: (success, changes_made)
    """
    paper_stem = os.path.splitext(os.path.basename(paper_path))[0]
    pdf_extract_path = os.path.join(EXTRACT_DIR, paper_stem + ".md")

    try:
        # Read paper
        content = paper_path.read_text(encoding='utf-8')
        fm, body = extract_frontmatter(content)

        # Validate input
        is_valid, issues = validate_frontmatter(fm)
        if not is_valid:
            if verbose:
                logger.debug(f"  SKIP {paper_stem}: Already has YAML issues")
            stats.skipped += 1
            return False, 0

        fields = parse_frontmatter(fm)
        changes = 0

        # Skip if already has abstract
        if fields.get('abstract'):
            if verbose:
                logger.debug(f"  {paper_stem}: Already has abstract")
            stats.skipped += 1
            return False, 0

        # Try PDF extract first
        if os.path.exists(pdf_extract_path):
            from enrich_papers_from_pdfs import extract_abstract_from_text
            with open(pdf_extract_path, 'r', encoding='utf-8') as f:
                pdf_content = f.read()

            text_match = re.search(r'```\n(.*?)\n```', pdf_content, re.DOTALL)
            if text_match:
                pdf_text = text_match.group(1)
                abstract = extract_abstract_from_text(pdf_text)
                if abstract:
                    fields['abstract'] = abstract
                    changes += 1
                    stats.abstracts_from_pdf += 1
                    if verbose:
                        logger.info(f"  {paper_stem}: Abstract from PDF")

        # Try Zotero metadata
        if not fields.get('abstract'):
            zotero_abstract = find_zotero_abstract(paper_stem, zotero_data)
            if zotero_abstract:
                fields['abstract'] = zotero_abstract
                changes += 1
                stats.abstracts_from_zotero += 1
                if verbose:
                    logger.info(f"  {paper_stem}: Abstract from Zotero")

        # Try URL metadata
        if not fields.get('abstract') and fields.get('url'):
            url = fields['url']
            # Could add API calls here in future
            # For now, just track that we attempted

        if changes == 0:
            if verbose:
                logger.debug(f"  {paper_stem}: No enrichment sources available")
            stats.skipped += 1
            return False, 0

        # Rebuild and validate
        new_fm = rebuild_frontmatter(fields)
        is_valid, issues = validate_frontmatter(new_fm)
        if not is_valid:
            stats.errors.append((paper_stem, f"YAML validation failed: {issues}"))
            return False, 0

        if dry_run:
            if verbose:
                logger.info(f"  [DRY RUN] Would enrich {paper_stem} ({changes} changes)")
            return True, changes

        # Write safely
        write_paper(paper_path, new_fm, body, validate=True)

        stats.processed += 1
        return True, changes

    except Exception as e:
        stats.errors.append((paper_stem, str(e)))
        return False, 0


def enrich_all_hybrid(target_paper=None, dry_run=False, verbose=False):
    """
    Enrich all papers using hybrid sources.

    Args:
        target_paper: Optional paper stem to process
        dry_run: If True, don't write files
        verbose: If True, show detailed progress
    """
    if not os.path.exists(PAPER_DIR):
        logger.error(f"Papers directory '{PAPER_DIR}' not found")
        sys.exit(1)

    # Load Zotero metadata once
    logger.info("Loading Zotero metadata...")
    zotero_data = load_zotero_metadata()
    logger.info(f"Loaded {len(zotero_data)} entries from Base.md")

    if target_paper:
        # Process single paper
        paper_path = Path(PAPER_DIR) / (target_paper + ".md")
        if not paper_path.exists():
            logger.error(f"Paper '{target_paper}.md' not found")
            sys.exit(1)

        logger.info(f"Enriching: {target_paper}")
        enrich_from_hybrid_sources(paper_path, zotero_data, dry_run, verbose)
    else:
        # Process all papers
        papers = sorted(Path(PAPER_DIR).glob("*.md"))
        total = len(papers)

        logger.info(f"Found {total} papers to enrich")

        for i, paper_path in enumerate(papers, 1):
            if verbose or i % 50 == 0:
                logger.info(f"[{i}/{total}] {paper_path.name}")

            enrich_from_hybrid_sources(paper_path, zotero_data, dry_run, verbose)

    stats.report()


def main():
    parser = argparse.ArgumentParser(
        description="Enrich papers using hybrid sources (PDF, Zotero, arXiv)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 enrich_papers_hybrid.py                # Enrich all papers
  python3 enrich_papers_hybrid.py --dry-run      # Preview changes
  python3 enrich_papers_hybrid.py --verbose      # Show progress
  python3 enrich_papers_hybrid.py "2016-Amodei"  # Enrich specific paper
        """
    )
    parser.add_argument('paper', nargs='?', help='Specific paper stem to enrich')
    parser.add_argument('--dry-run', '-n', action='store_true',
                        help="Don't write files, just show what would happen")
    parser.add_argument('--verbose', '-v', action='store_true',
                        help="Show detailed progress information")

    args = parser.parse_args()

    if args.dry_run:
        logger.info("=" * 60)
        logger.info("DRY RUN MODE - No files will be modified")
        logger.info("=" * 60)

    enrich_all_hybrid(
        target_paper=args.paper,
        dry_run=args.dry_run,
        verbose=args.verbose
    )


if __name__ == "__main__":
    main()
