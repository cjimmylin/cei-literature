#!/usr/bin/env python3
"""
Expand incomplete author lists using multiple online sources.

This script attempts to find complete author information from:
1. arXiv API (for arXiv papers)
2. CrossRef API (for DOI-based papers)
3. PubMed API (for medical papers)
4. URL parsing and web scraping

USAGE:
    python3 PYTHON/expand_author_lists.py              # Full run
    python3 PYTHON/expand_author_lists.py --dry-run    # Show what would be done
    python3 PYTHON/expand_author_lists.py --arxiv      # Only check arXiv papers
    python3 PYTHON/expand_author_lists.py --doi        # Only check DOI papers
"""

import re
import json
import sys
import time
import logging
from pathlib import Path
from typing import List, Optional
from dataclasses import dataclass
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)

sys.path.insert(0, str(Path(__file__).parent))

from yaml_frontmatter_utils import (
    extract_frontmatter,
    parse_frontmatter,
    rebuild_frontmatter,
    write_paper,
    validate_frontmatter,
)
from vault_config import PAPERS_DIR, AUTHORS_DIR

# Try to import requests, fall back gracefully
try:
    import urllib.request
    import urllib.error
    HAS_URLLIB = True
except ImportError:
    HAS_URLLIB = False


@dataclass
class AuthorLookupResult:
    """Result from looking up authors"""
    source: str  # 'arxiv', 'crossref', 'pubmed', 'url'
    authors: List[str]
    confidence: float  # 0.0-1.0
    raw_data: str = ""  # For debugging


class ArxivAuthorFetcher:
    """Fetch complete author lists from arXiv API"""

    BASE_URL = "http://export.arxiv.org/api/query?"
    RATE_LIMIT = 3  # seconds between requests

    @staticmethod
    def extract_arxiv_id(url: str) -> Optional[str]:
        """Extract arXiv ID from various URL formats"""
        if not url:
            return None

        # Match arXiv IDs: YYMM.NNNNN or older format arch-ph/YYMMNNN
        patterns = [
            r'arxiv\.org/abs/(\d{4}\.\d{5})',
            r'arxiv\.org/pdf/(\d{4}\.\d{5})',
            r'(\d{4}\.\d{5})',  # Direct ID
            r'arch-ph/(\d{7})',  # Older format
        ]

        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)

        return None

    @classmethod
    def fetch_authors(cls, arxiv_id: str) -> Optional[AuthorLookupResult]:
        """Fetch authors from arXiv API"""
        if not HAS_URLLIB:
            return None

        try:
            # Construct query URL
            query = f'search_query=arXiv:{arxiv_id}&start=0&max_results=1&sortBy=submittedDate&sortOrder=descending'
            url = f"{cls.BASE_URL}{query}"

            # Fetch with timeout
            with urllib.request.urlopen(url, timeout=10) as response:
                data = response.read().decode('utf-8')

            # Parse XML
            root = ET.fromstring(data)

            # Extract authors from first entry
            entries = root.findall('{http://www.w3.org/2005/Atom}entry')
            if not entries:
                return None

            entry = entries[0]
            authors = []

            for author in entry.findall('{http://www.w3.org/2005/Atom}author'):
                name_elem = author.find('{http://www.w3.org/2005/Atom}name')
                if name_elem is not None and name_elem.text:
                    authors.append(name_elem.text.strip())

            if authors:
                return AuthorLookupResult(
                    source='arxiv',
                    authors=authors,
                    confidence=1.0,
                    raw_data=f"arXiv ID: {arxiv_id}"
                )

            return None

        except Exception as e:
            return None


class CrossrefAuthorFetcher:
    """Fetch complete author lists from CrossRef API"""

    BASE_URL = "https://api.crossref.org/works/"
    RATE_LIMIT = 1  # seconds between requests

    @classmethod
    def fetch_authors(cls, doi: str) -> Optional[AuthorLookupResult]:
        """Fetch authors from CrossRef API"""
        if not HAS_URLLIB:
            return None

        try:
            # Construct URL
            url = f"{cls.BASE_URL}{doi}"
            headers = {'User-Agent': 'CEI-Literature-Vault/1.0'}

            # Fetch with timeout
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                data = response.read().decode('utf-8')

            # Parse JSON
            result = json.loads(data)

            if 'message' not in result:
                return None

            authors = []
            msg = result['message']

            # Extract authors
            if 'author' in msg:
                for author_obj in msg['author']:
                    name_parts = []
                    if 'family' in author_obj:
                        name_parts.append(author_obj['family'])
                    if 'given' in author_obj:
                        name_parts.append(author_obj['given'])

                    if name_parts:
                        # Format: "Family, Given"
                        if len(name_parts) == 2:
                            authors.append(f"{name_parts[0]}, {name_parts[1]}")
                        else:
                            authors.append(name_parts[0])

            if authors:
                return AuthorLookupResult(
                    source='crossref',
                    authors=authors,
                    confidence=1.0,
                    raw_data=f"DOI: {doi}"
                )

            return None

        except Exception as e:
            return None


class PubmedAuthorFetcher:
    """Fetch complete author lists from PubMed API"""

    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    RATE_LIMIT = 1  # seconds between requests

    @staticmethod
    def extract_pubmed_id(url: str) -> Optional[str]:
        """Extract PubMed ID from URL"""
        if not url:
            return None

        patterns = [
            r'pubmed\.ncbi\.nlm\.nih\.gov/(\d+)',
            r'ncbi\.nlm\.nih\.gov/pubmed/(\d+)',
            r'PMID: (\d+)',
            r'(\d+)(?=/|$)',  # Last resort: just numbers
        ]

        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)

        return None

    @classmethod
    def fetch_authors(cls, pubmed_id: str) -> Optional[AuthorLookupResult]:
        """Fetch authors from PubMed API"""
        if not HAS_URLLIB:
            return None

        try:
            # Construct URL
            url = f"{cls.BASE_URL}efetch.fcgi?db=pubmed&id={pubmed_id}&rettype=xml&retmode=text"

            # Fetch with timeout
            with urllib.request.urlopen(url, timeout=10) as response:
                data = response.read().decode('utf-8')

            # Parse XML
            root = ET.fromstring(data)

            authors = []
            # Navigate through PubmedArticle structure
            for author in root.findall('.//Author'):
                name_parts = []

                last_name = author.find('LastName')
                first_name = author.find('ForeName')

                if last_name is not None and last_name.text:
                    name_parts.append(last_name.text)
                if first_name is not None and first_name.text:
                    name_parts.append(first_name.text)

                if name_parts:
                    authors.append(', '.join(name_parts) if len(name_parts) > 1 else name_parts[0])

            if authors:
                return AuthorLookupResult(
                    source='pubmed',
                    authors=authors,
                    confidence=1.0,
                    raw_data=f"PubMed ID: {pubmed_id}"
                )

            return None

        except Exception as e:
            return None


class AuthorLookupEngine:
    """Orchestrate multi-source author lookups"""

    def __init__(self, papers_dir: Path, authors_dir: Path):
        self.papers_dir = papers_dir
        self.authors_dir = authors_dir
        self.stats = {
            'total_papers': 0,
            'arxiv_found': 0,
            'crossref_found': 0,
            'pubmed_found': 0,
            'papers_updated': 0,
            'authors_expanded': 0,
        }

    def process_all_incomplete_papers(self, dry_run: bool = False, source_filter: str = None):
        """Process all papers with incomplete authors"""

        papers = sorted(self.papers_dir.glob('*.md'))
        incomplete_papers = []

        logger.info("Scanning for papers with incomplete authors...\n")

        for filepath in papers:
            content = filepath.read_text(encoding='utf-8')
            try:
                fm, body = extract_frontmatter(content)
                fields = parse_frontmatter(fm)
            except Exception:
                continue

            authors = fields.get('authors', '')

            # Check if incomplete
            if any(marker in authors for marker in ['others', 'Unknown', 'et al']):
                incomplete_papers.append((filepath, authors))

        logger.info(f"Found {len(incomplete_papers)} papers with incomplete authors\n")

        for i, (filepath, authors) in enumerate(incomplete_papers, 1):
            logger.info(f"[{i}/{len(incomplete_papers)}] Processing {filepath.name}...")

            try:
                self.process_paper(filepath, dry_run=dry_run, source_filter=source_filter)
            except Exception as e:
                logger.error(f"  ERROR: {e}")

        self._print_stats()

    def process_paper(self, filepath: Path, dry_run: bool = False, source_filter: str = None):
        """Process a single paper to expand authors"""

        self.stats['total_papers'] += 1

        content = filepath.read_text(encoding='utf-8')
        fm, body = extract_frontmatter(content)
        fields = parse_frontmatter(fm)

        # Get identifiers
        url = fields.get('url', '')
        doi = fields.get('doi', '')
        current_authors = fields.get('authors', '')

        # Try to fetch from various sources
        result = None

        # Try arXiv
        if not source_filter or source_filter == 'arxiv':
            arxiv_id = ArxivAuthorFetcher.extract_arxiv_id(url)
            if arxiv_id:
                logger.info(f"  Trying arXiv ({arxiv_id})...")
                result = ArxivAuthorFetcher.fetch_authors(arxiv_id)
                if result:
                    logger.info(f"  Trying arXiv ({arxiv_id})... Found {len(result.authors)} authors")
                    self.stats['arxiv_found'] += 1
                else:
                    logger.warning(f"  Trying arXiv ({arxiv_id})... failed")
                time.sleep(ArxivAuthorFetcher.RATE_LIMIT)

        # Try CrossRef if arXiv didn't work
        if not result and (not source_filter or source_filter == 'doi'):
            if doi:
                logger.info(f"  Trying CrossRef ({doi})...")
                result = CrossrefAuthorFetcher.fetch_authors(doi)
                if result:
                    logger.info(f"  Trying CrossRef ({doi})... Found {len(result.authors)} authors")
                    self.stats['crossref_found'] += 1
                else:
                    logger.warning(f"  Trying CrossRef ({doi})... failed")
                time.sleep(CrossrefAuthorFetcher.RATE_LIMIT)

        # Try PubMed if others didn't work
        if not result and (not source_filter or source_filter == 'pubmed'):
            pubmed_id = PubmedAuthorFetcher.extract_pubmed_id(url)
            if pubmed_id:
                logger.info(f"  Trying PubMed ({pubmed_id})...")
                result = PubmedAuthorFetcher.fetch_authors(pubmed_id)
                if result:
                    logger.info(f"  Trying PubMed ({pubmed_id})... Found {len(result.authors)} authors")
                    self.stats['pubmed_found'] += 1
                else:
                    logger.warning(f"  Trying PubMed ({pubmed_id})... failed")
                time.sleep(PubmedAuthorFetcher.RATE_LIMIT)

        # Update paper if we found authors
        if result:
            # Create wikilinks
            wikilinks = []
            for author in result.authors:
                wikilinks.append(f"[[{author}]]")

            new_authors = "; ".join(wikilinks)

            if not dry_run:
                fields['authors'] = new_authors

                # Rebuild and validate YAML
                new_fm = rebuild_frontmatter(fields)
                is_valid, issues = validate_frontmatter(new_fm)

                if is_valid:
                    write_paper(filepath, new_fm, body, validate=True)
                    self.stats['papers_updated'] += 1
                    self.stats['authors_expanded'] += len(result.authors)
                    logger.info(f"  Updated paper with {len(result.authors)} authors")
                else:
                    logger.warning(f"  YAML validation failed: {issues}")
            else:
                logger.info(f"  [DRY RUN] Would update with {len(result.authors)} authors:")
                for author in result.authors[:3]:
                    logger.info(f"    - {author}")
                if len(result.authors) > 3:
                    logger.info(f"    ... and {len(result.authors) - 3} more")
        else:
            logger.warning(f"  Could not find authors from any source")

    def _print_stats(self):
        """Print statistics"""
        logger.info("\n" + "="*60)
        logger.info("AUTHOR LOOKUP STATISTICS")
        logger.info("="*60)
        logger.info(f"Total papers processed:    {self.stats['total_papers']}")
        logger.info(f"Authors found via arXiv:   {self.stats['arxiv_found']}")
        logger.info(f"Authors found via CrossRef:{self.stats['crossref_found']}")
        logger.info(f"Authors found via PubMed:  {self.stats['pubmed_found']}")
        logger.info(f"Papers updated:            {self.stats['papers_updated']}")
        logger.info(f"Total authors expanded:    {self.stats['authors_expanded']}")
        logger.info("="*60 + "\n")


def main():
    """Main entry point"""
    papers_dir = PAPERS_DIR
    authors_dir = AUTHORS_DIR

    # Parse arguments
    dry_run = '--dry-run' in sys.argv
    source_filter = None
    for arg in ['--arxiv', '--doi', '--pubmed']:
        if arg in sys.argv:
            source_filter = arg[2:]  # Remove '--'

    if dry_run:
        logger.info("Running in DRY RUN mode (no changes will be made)\n")

    # Create engine and process
    engine = AuthorLookupEngine(papers_dir, authors_dir)
    engine.process_all_incomplete_papers(dry_run=dry_run, source_filter=source_filter)


if __name__ == '__main__':
    main()
