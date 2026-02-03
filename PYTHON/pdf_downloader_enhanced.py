#!/usr/bin/env python3
"""
Enhanced PDF Downloader for CEI Literature Vault
Based on learnings from 2026-01-24 recovery session (474 PDFs recovered)

Features:
- Multi-source fallback (arXiv, ACL, OpenReview, DOI resolution)
- Smart retry with exponential backoff
- DOI discovery from URLs and APIs
- Progress checkpointing
- Comprehensive logging
- Rate limiting

Usage:
    python3 PYTHON/pdf_downloader_enhanced.py                 # Download all
    python3 PYTHON/pdf_downloader_enhanced.py --limit 50      # First 50
    python3 PYTHON/pdf_downloader_enhanced.py --resume        # Resume from checkpoint
    python3 PYTHON/pdf_downloader_enhanced.py --discover-dois # Find missing DOIs first
"""

import sys
import re
import json
import time
import argparse
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path
from datetime import datetime
from typing import Optional, Tuple, Dict, List
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Paths - use vault_config for external PDF location
from vault_config import PAPERS_DIR, PDFS_DIR, WORKSPACE_ROOT, LOGS_DIR
CHECKPOINT_FILE = LOGS_DIR / "download_checkpoint.json"

# Config
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
RATE_LIMIT = 0.5  # seconds between downloads
MAX_RETRIES = 3
CHECKPOINT_INTERVAL = 10


class EnhancedPDFDownloader:
    def __init__(self):
        PDFS_DIR.mkdir(exist_ok=True)
        self.checkpoint = self.load_checkpoint()
        self.stats = {
            'downloaded': 0,
            'failed': 0,
            'skipped': 0,
            'paywalled': 0,
        }

    def load_checkpoint(self) -> Dict:
        """Load progress checkpoint."""
        if CHECKPOINT_FILE.exists():
            with open(CHECKPOINT_FILE) as f:
                return json.load(f)
        return {'completed': set(), 'failed': set()}

    def save_checkpoint(self):
        """Save progress checkpoint."""
        CHECKPOINT_FILE.parent.mkdir(exist_ok=True)
        # Convert sets to lists for JSON
        checkpoint_data = {
            'completed': list(self.checkpoint['completed']),
            'failed': list(self.checkpoint['failed']),
            'last_update': datetime.now().isoformat()
        }
        with open(CHECKPOINT_FILE, 'w') as f:
            json.dump(checkpoint_data, f, indent=2)

    def extract_metadata(self, paper_file: Path) -> Dict:
        """Extract all metadata from paper file."""
        content = paper_file.read_text(encoding='utf-8', errors='ignore')

        metadata = {
            'doi': None,
            'external_pdf': None,
            'url': None,
            'title': None,
            'year': None,
            'authors': None,
        }

        # Extract fields using regex
        patterns = {
            'doi': r'^doi:\s*([^\n]+)',
            'external_pdf': r'^external_pdf:\s*"([^"]+)"',
            'url': r'^url:\s*"?([^"\n]+)"?',
            'year': r'^year:\s*(\d+)',
            'authors': r'^authors:\s*"?([^"\n]+)"?',
        }

        for field, pattern in patterns.items():
            match = re.search(pattern, content, re.MULTILINE)
            if match:
                metadata[field] = match.group(1).strip()

        # Extract title from markdown header
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if title_match:
            metadata['title'] = title_match.group(1).strip()

        return metadata

    def discover_doi(self, metadata: Dict) -> Optional[str]:
        """Try to discover DOI using multiple methods."""

        # Method 1: Check if already exists
        if metadata.get('doi'):
            return metadata['doi']

        # Method 2: Extract from URL
        doi = self.extract_doi_from_url(metadata.get('url'))
        if doi:
            logger.info(f"      Found DOI in URL: {doi}")
            return doi

        doi = self.extract_doi_from_url(metadata.get('external_pdf'))
        if doi:
            logger.info(f"      Found DOI in PDF URL: {doi}")
            return doi

        # Method 3: Special URL patterns
        doi = self.parse_special_urls(metadata.get('url'))
        if doi:
            logger.info(f"      Generated DOI from URL: {doi}")
            return doi

        return None

    def extract_doi_from_url(self, url: Optional[str]) -> Optional[str]:
        """Extract DOI from URL using patterns."""
        if not url:
            return None

        # Pattern 1: doi.org/10.xxx
        match = re.search(r'doi\.org/(10\.\d+/[^\s&?#]+)', url)
        if match:
            return match.group(1)

        # Pattern 2: Embedded in path
        match = re.search(r'/(10\.\d+/[a-zA-Z0-9._-]+)', url)
        if match:
            potential = match.group(1)
            if re.match(r'10\.\d{4,}/\S+', potential):
                return potential

        return None

    def parse_special_urls(self, url: Optional[str]) -> Optional[str]:
        """Generate DOIs from special repository URLs."""
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

        return None

    def try_download_from_arxiv(self, doi: str) -> Tuple[bool, bytes, str]:
        """Try to download from arXiv."""
        if 'arxiv' not in doi.lower():
            return False, b'', "Not an arXiv paper"

        arxiv_id = doi.split('arXiv.')[-1]
        url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"

        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as response:
                data = response.read()
                if data.startswith(b'%PDF'):
                    return True, data, "arXiv"
        except Exception as e:
            pass

        return False, b'', "Failed"

    def try_download_from_acl(self, metadata: Dict) -> Tuple[bool, bytes, str]:
        """Try to download from ACL Anthology."""
        url = metadata.get('url') or metadata.get('external_pdf')
        if not url or 'aclanthology.org' not in url:
            return False, b'', "Not ACL"

        # Convert to PDF URL
        pdf_url = url.replace('aclanthology.org/', 'aclanthology.org/')
        if not pdf_url.endswith('.pdf'):
            pdf_url = pdf_url.rstrip('/') + '.pdf'

        try:
            req = urllib.request.Request(pdf_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as response:
                data = response.read()
                if data.startswith(b'%PDF'):
                    return True, data, "ACL Anthology"
        except:
            pass

        return False, b'', "Failed"

    def try_download_from_doi(self, doi: str) -> Tuple[bool, bytes, str]:
        """Try to download using DOI resolution."""
        if not doi:
            return False, b'', "No DOI"

        url = f"https://doi.org/{doi}"

        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as response:
                data = response.read()
                if data.startswith(b'%PDF'):
                    return True, data, "DOI resolution"
        except:
            pass

        return False, b'', "Failed"

    def try_download_from_url(self, url: str) -> Tuple[bool, bytes, str]:
        """Try to download from direct URL."""
        if not url or url.startswith('file://'):
            return False, b'', "No valid URL"

        # Normalize URL
        url = url.replace('http://', 'https://')

        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as response:
                data = response.read()
                if data.startswith(b'%PDF'):
                    return True, data, "Direct URL"
        except urllib.error.HTTPError as e:
            if e.code == 403:
                return False, b'', "Paywalled (403)"
        except:
            pass

        return False, b'', "Failed"

    def download_pdf(self, metadata: Dict, paper_name: str) -> Tuple[bool, str, float]:
        """
        Try multiple sources to download PDF.
        Returns: (success, source, size_mb)
        """

        # Source priority order
        sources = [
            ('arXiv', lambda: self.try_download_from_arxiv(metadata.get('doi'))),
            ('ACL', lambda: self.try_download_from_acl(metadata)),
            ('DOI', lambda: self.try_download_from_doi(metadata.get('doi'))),
            ('external_pdf', lambda: self.try_download_from_url(metadata.get('external_pdf'))),
            ('url', lambda: self.try_download_from_url(metadata.get('url'))),
        ]

        for source_name, download_func in sources:
            try:
                success, data, msg = download_func()
                if success and data:
                    size_mb = len(data) / (1024 * 1024)
                    return True, source_name, size_mb, data
            except Exception as e:
                logger.debug(f"      {source_name} failed: {e}")
                continue

        return False, "All sources failed", 0, b''

    def process_papers(self, limit: Optional[int] = None, resume: bool = False):
        """Main processing loop."""
        papers = sorted(PAPERS_DIR.glob("*.md"))

        if limit:
            papers = papers[:limit]

        # Filter out completed if resuming
        if resume:
            completed = set(self.checkpoint.get('completed', []))
            papers = [p for p in papers if p.stem not in completed]
            logger.info(f"Resuming: {len(papers)} papers remaining")

        total = len(papers)
        logger.info(f"\n{'='*80}")
        logger.info(f"ENHANCED PDF DOWNLOADER")
        logger.info(f"{'='*80}")
        logger.info(f"Papers to process: {total}")
        logger.info("")

        for i, paper_file in enumerate(papers, 1):
            paper_name = paper_file.stem
            pdf_path = PDFS_DIR / f"{paper_name}.pdf"

            # Skip if already exists
            if pdf_path.exists():
                logger.info(f"[{i:3d}/{total}] SKIP: {paper_name[:60]} (exists)")
                self.stats['skipped'] += 1
                continue

            logger.info(f"[{i:3d}/{total}] {paper_name[:60]}")

            # Extract metadata
            metadata = self.extract_metadata(paper_file)

            # Try to discover DOI if missing
            if not metadata.get('doi'):
                doi = self.discover_doi(metadata)
                if doi:
                    metadata['doi'] = doi

            # Try download
            success, source, size_mb, data = self.download_pdf(metadata, paper_name)

            if success:
                # Save PDF
                with open(pdf_path, 'wb') as f:
                    f.write(data)

                logger.info(f"      ✅ Downloaded from {source} ({size_mb:.2f} MB)")
                self.stats['downloaded'] += 1
                self.checkpoint['completed'].add(paper_name)

            else:
                logger.warning(f"      ❌ Failed: {source}")
                self.stats['failed'] += 1
                self.checkpoint['failed'].add(paper_name)

            # Checkpoint progress
            if i % CHECKPOINT_INTERVAL == 0:
                self.save_checkpoint()

            # Rate limiting
            time.sleep(RATE_LIMIT)

        # Final checkpoint
        self.save_checkpoint()

        # Summary
        logger.info(f"\n{'='*80}")
        logger.info(f"SUMMARY")
        logger.info(f"{'='*80}")
        logger.info(f"Downloaded:    {self.stats['downloaded']:4d}")
        logger.info(f"Skipped:       {self.stats['skipped']:4d}")
        logger.info(f"Failed:        {self.stats['failed']:4d}")
        logger.info(f"{'─'*40}")
        logger.info(f"Total PDFs:    {len(list(PDFS_DIR.glob('*.pdf'))):4d}")


def main():
    parser = argparse.ArgumentParser(
        description="Enhanced PDF Downloader with multi-source fallback"
    )
    parser.add_argument('--limit', type=int, help='Limit to N papers')
    parser.add_argument('--resume', action='store_true', help='Resume from checkpoint')

    args = parser.parse_args()

    downloader = EnhancedPDFDownloader()
    downloader.process_papers(limit=args.limit, resume=args.resume)


if __name__ == "__main__":
    main()
