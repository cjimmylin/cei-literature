#!/usr/bin/env python3
"""
DOI Discovery Utility
Finds missing DOIs using CrossRef, Semantic Scholar, and URL parsing

Based on 2026-01-24 session learnings where 7 new DOIs were discovered

Usage:
    python3 PYTHON/doi_discovery.py                    # Find all missing DOIs
    python3 PYTHON/doi_discovery.py --limit 50         # Check first 50
    python3 PYTHON/doi_discovery.py --update           # Update paper files with found DOIs
"""

import re
import json
import urllib.request
import urllib.parse
from pathlib import Path
import time
import argparse
from typing import Optional, Dict
import logging

from vault_config import PAPERS_DIR, LOGS_DIR

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

OUTPUT_FILE = LOGS_DIR / "discovered_dois.json"

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
RATE_LIMIT = 0.5


class DOIDiscovery:
    def __init__(self):
        self.found_dois = []

    def extract_metadata(self, paper_file: Path) -> Dict:
        """Extract paper metadata."""
        content = paper_file.read_text(encoding='utf-8', errors='ignore')

        metadata = {
            'filename': paper_file.stem,
            'doi': None,
            'url': None,
            'title': None,
            'year': None,
            'authors': None,
        }

        patterns = {
            'doi': r'^doi:\s*([^\n]+)',
            'url': r'^url:\s*"?([^"\n]+)"?',
            'year': r'^year:\s*(\d+)',
            'authors': r'^authors:\s*"?([^"\n]+)"?',
        }

        for field, pattern in patterns.items():
            match = re.search(pattern, content, re.MULTILINE)
            if match:
                metadata[field] = match.group(1).strip()

        # Extract title
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if title_match:
            metadata['title'] = title_match.group(1).strip()

        # Also check external_pdf
        ext_match = re.search(r'^external_pdf:\s*"([^"]+)"', content, re.MULTILINE)
        if ext_match:
            metadata['external_pdf'] = ext_match.group(1).strip()

        return metadata

    def extract_doi_from_url(self, url: Optional[str]) -> Optional[str]:
        """Extract DOI from URL using regex patterns."""
        if not url or url == 'N/A':
            return None

        patterns = [
            r'doi\.org/(10\.\d+/[^\s&?#]+)',
            r'dx\.doi\.org/(10\.\d+/[^\s&?#]+)',
            r'/(10\.\d+/[a-zA-Z0-9._-]+)',
        ]

        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                potential = match.group(1)
                # Verify it's a valid DOI format
                if re.match(r'10\.\d{4,}/\S+', potential):
                    return potential

        return None

    def parse_special_urls(self, url: Optional[str]) -> Optional[str]:
        """Generate DOIs from repository URLs."""
        if not url:
            return None

        # arXiv
        if 'arxiv.org' in url:
            match = re.search(r'arxiv\.org/(?:abs|pdf)/(\d+\.\d+)', url)
            if match:
                return f"10.48550/arXiv.{match.group(1)}"

        # OSF
        if 'osf.io' in url:
            match = re.search(r'osf\.io/([a-z0-9]+)', url)
            if match:
                return f"10.31219/osf.io/{match.group(1)}"

        # SSRN
        if 'ssrn.com' in url:
            match = re.search(r'abstract=(\d+)', url)
            if match:
                return f"10.2139/ssrn.{match.group(1)}"

        # PubMed
        if 'pubmed.ncbi.nlm.nih.gov' in url or 'ncbi.nlm.nih.gov/pubmed' in url:
            match = re.search(r'pubmed/(\d+)', url) or re.search(r'\.gov/(\d+)', url)
            if match:
                pmid = match.group(1)
                # Try to get DOI from PubMed API
                try:
                    api_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pmid}&retmode=json"
                    req = urllib.request.Request(api_url, headers=HEADERS)
                    with urllib.request.urlopen(req, timeout=10) as response:
                        data = json.loads(response.read())
                        article_ids = data.get('result', {}).get(pmid, {}).get('articleids', [])
                        for aid in article_ids:
                            if aid.get('idtype') == 'doi':
                                return aid.get('value')
                except:
                    pass

        return None

    def search_crossref(self, title: str, year: Optional[str] = None) -> Optional[str]:
        """Search CrossRef API for DOI."""
        if not title or title == 'N/A':
            return None

        try:
            clean_title = title.replace('"', '').strip()
            query = urllib.parse.quote(clean_title)

            url = f"https://api.crossref.org/works?query.title={query}&rows=3"
            req = urllib.request.Request(url, headers=HEADERS)

            with urllib.request.urlopen(req, timeout=10) as response:
                result = json.loads(response.read())

                if result.get('message', {}).get('items'):
                    for item in result['message']['items'][:3]:
                        # Check title similarity
                        item_title = item.get('title', [''])[0].lower()
                        search_title = clean_title.lower()

                        # Simple fuzzy match
                        if search_title[:40] in item_title or item_title[:40] in search_title:
                            # Verify year if available
                            item_year = item.get('published', {}).get('date-parts', [[None]])[0][0]
                            if year and year != '????' and item_year:
                                if abs(int(year) - int(item_year)) > 1:
                                    continue

                            doi = item.get('DOI')
                            if doi:
                                return doi

        except Exception as e:
            logger.debug(f"CrossRef error: {e}")

        return None

    def search_semantic_scholar(self, title: str, year: Optional[str] = None) -> Optional[str]:
        """Search Semantic Scholar API for DOI."""
        if not title or title == 'N/A':
            return None

        try:
            clean_title = title.replace('"', '').strip()
            query = urllib.parse.quote(clean_title)

            url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=3&fields=title,year,externalIds"
            req = urllib.request.Request(url, headers=HEADERS)

            with urllib.request.urlopen(req, timeout=10) as response:
                result = json.loads(response.read())

                if result.get('data'):
                    for item in result['data']:
                        item_title = item.get('title', '').lower()
                        search_title = clean_title.lower()

                        # Check similarity
                        if search_title[:40] in item_title or item_title[:40] in search_title:
                            # Check year
                            item_year = item.get('year')
                            if year and year != '????' and item_year:
                                if abs(int(year) - int(item_year)) > 1:
                                    continue

                            # Get DOI
                            ext_ids = item.get('externalIds', {})
                            if ext_ids.get('DOI'):
                                return ext_ids['DOI']
                            elif ext_ids.get('ArXiv'):
                                return f"10.48550/arXiv.{ext_ids['ArXiv']}"

        except Exception as e:
            logger.debug(f"Semantic Scholar error: {e}")

        return None

    def discover_doi(self, metadata: Dict) -> Optional[str]:
        """Try all methods to discover DOI."""

        # Already has DOI
        if metadata.get('doi'):
            return None

        # Method 1: Extract from URL
        doi = self.extract_doi_from_url(metadata.get('url'))
        if doi:
            return doi

        # Method 2: Extract from external_pdf
        doi = self.extract_doi_from_url(metadata.get('external_pdf'))
        if doi:
            return doi

        # Method 3: Parse special URLs
        doi = self.parse_special_urls(metadata.get('url'))
        if doi:
            return doi

        doi = self.parse_special_urls(metadata.get('external_pdf'))
        if doi:
            return doi

        # Method 4: CrossRef search
        doi = self.search_crossref(metadata.get('title'), metadata.get('year'))
        if doi:
            return doi

        # Method 5: Semantic Scholar
        doi = self.search_semantic_scholar(metadata.get('title'), metadata.get('year'))
        if doi:
            return doi

        return None

    def process_papers(self, limit: Optional[int] = None):
        """Find missing DOIs for all papers."""
        papers = sorted(PAPERS_DIR.glob("*.md"))

        if limit:
            papers = papers[:limit]

        logger.info(f"\n{'='*80}")
        logger.info(f"DOI DISCOVERY")
        logger.info(f"{'='*80}")
        logger.info(f"Processing {len(papers)} papers\n")

        found_count = 0

        for i, paper_file in enumerate(papers, 1):
            metadata = self.extract_metadata(paper_file)

            # Skip if already has DOI
            if metadata.get('doi'):
                continue

            logger.info(f"[{i}/{len(papers)}] {metadata['filename'][:60]}")

            # Try to discover
            doi = self.discover_doi(metadata)

            if doi:
                logger.info(f"      ✅ Found: {doi}")
                self.found_dois.append({
                    **metadata,
                    'discovered_doi': doi
                })
                found_count += 1
            else:
                logger.info(f"      ❌ Not found")

            # Rate limiting
            time.sleep(RATE_LIMIT)

        # Save results
        if self.found_dois:
            OUTPUT_FILE.parent.mkdir(exist_ok=True)
            output = {
                'total_found': len(self.found_dois),
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                'papers': self.found_dois
            }

            with open(OUTPUT_FILE, 'w') as f:
                json.dump(output, f, indent=2)

            logger.info(f"\n{'='*80}")
            logger.info(f"RESULTS")
            logger.info(f"{'='*80}")
            logger.info(f"Found {found_count} new DOIs")
            logger.info(f"Saved to: {OUTPUT_FILE}")

        else:
            logger.info(f"\nNo new DOIs found")


def main():
    parser = argparse.ArgumentParser(description="Discover missing DOIs")
    parser.add_argument('--limit', type=int, help='Limit to N papers')

    args = parser.parse_args()

    discovery = DOIDiscovery()
    discovery.process_papers(limit=args.limit)


if __name__ == "__main__":
    main()
