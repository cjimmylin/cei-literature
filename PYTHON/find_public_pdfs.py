#!/usr/bin/env python3
"""
Find and Download Public PDFs for All Papers

Strategy:
1. For papers with valid http(s) PDF URLs -> download directly
2. For papers with DOI or invalid file:// URLs -> use Semantic Scholar API to find open access PDFs
3. Update metadata with valid online links
4. Download found PDFs

Usage:
    python3 PYTHON/find_public_pdfs.py --download-all   # Find and download all
    python3 PYTHON/find_public_pdfs.py --find-links      # Just find online links
    python3 PYTHON/find_public_pdfs.py --report          # Show status
"""

import re
import json
import time
import logging
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path
from typing import Optional, Dict, Tuple

logger = logging.getLogger(__name__)

# Setup paths - use vault_config for external PDF location
from vault_config import PAPERS_DIR, PDFS_DIR, WORKSPACE_ROOT
LOG_FILE = WORKSPACE_ROOT / "20260124-pdf_sources_log.json"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
}

class PublicPDFFinder:
    def __init__(self):
        PDFS_DIR.mkdir(exist_ok=True)
        self.load_log()
        self.rate_limit_count = 0

    def load_log(self):
        """Load progress from log."""
        if LOG_FILE.exists():
            with open(LOG_FILE) as f:
                self.log = json.load(f)
        else:
            self.log = {"found": {}, "no_oa": {}, "downloaded": {}, "failed": {}}

    def save_log(self):
        """Save progress to log."""
        with open(LOG_FILE, 'w') as f:
            json.dump(self.log, f, indent=2)

    def extract_frontmatter(self, content: str) -> Tuple[str, str]:
        """Extract YAML frontmatter."""
        match = re.search(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
        if match:
            return match.group(1), match.group(2)
        return "", content

    def extract_field(self, frontmatter: str, field: str) -> Optional[str]:
        """Extract field from YAML."""
        pattern = rf'^{field}:\s*"?([^"\n]+)"?'
        match = re.search(pattern, frontmatter, re.MULTILINE)
        return match.group(1).strip() if match else None

    def is_valid_pdf_url(self, url: str) -> bool:
        """Check if URL is a valid HTTP(S) PDF URL."""
        if not url:
            return False
        return url.startswith('http') and not url.startswith('file://')

    def extract_doi(self, url: str) -> Optional[str]:
        """Extract DOI from URL."""
        if not url:
            return None
        match = re.search(r'(?:doi\.org/|doi:)?(10\.\S+?)(?:\s|$|/)', url)
        return match.group(1) if match else None

    def extract_arxiv_id(self, url: str) -> Optional[str]:
        """Extract arXiv ID from URL."""
        if not url:
            return None
        match = re.search(r'arxiv\.org/(?:abs|pdf)/(\d+\.\d+)', url)
        return match.group(1) if match else None

    def search_semantic_scholar(self, title: str, doi: Optional[str] = None, arxiv_id: Optional[str] = None) -> Optional[Dict]:
        """Search Semantic Scholar for paper and OA PDF."""
        time.sleep(4.0)  # Rate limit to 1 req/4 sec

        try:
            # Try by DOI first
            if doi:
                url = f"https://api.semanticscholar.org/v1/paper/{urllib.parse.quote(doi)}"
            elif arxiv_id:
                url = f"https://api.semanticscholar.org/v1/paper/arXiv:{arxiv_id}"
            else:
                # Search by title
                search_query = title.split('(')[0].split(':')[0].strip()[:100]
                url = f"https://api.semanticscholar.org/v1/paper/search?query={urllib.parse.quote(search_query)}&limit=1&fields=openAccessPdf,url,paperId,title"

            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())

                # Handle search results
                if 'results' in data:
                    if data['results']:
                        paper = data['results'][0]
                    else:
                        return None
                else:
                    paper = data

                # Check for OA PDF
                if paper.get('openAccessPdf') and paper['openAccessPdf'].get('url'):
                    return {
                        'url': paper['openAccessPdf']['url'],
                        'source': 'SemanticScholar',
                        'paperId': paper.get('paperId')
                    }

                return None

        except Exception as e:
            return None

    def download_from_url(self, url: str, pdf_path: Path) -> Tuple[bool, str]:
        """Download PDF from URL."""
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as response:
                data = response.read()

                if not data.startswith(b'%PDF'):
                    return False, "Not a valid PDF"

                with open(pdf_path, 'wb') as f:
                    f.write(data)

                size_mb = pdf_path.stat().st_size / (1024 * 1024)
                return True, f"{size_mb:.2f} MB"

        except urllib.error.HTTPError as e:
            if e.code == 403:
                return False, "Forbidden (403)"
            elif e.code == 404:
                return False, "Not found (404)"
            else:
                return False, f"HTTP {e.code}"

        except Exception as e:
            return False, str(e)[:50]

    def find_and_download_all(self):
        """Find public PDFs for all papers and download them."""
        papers = sorted(PAPERS_DIR.glob("*.md"))

        logger.info(f"\n{'='*80}")
        logger.info(f"FIND & DOWNLOAD PUBLIC PDFs")
        logger.info(f"{'='*80}\n")

        found_count = 0
        downloaded_count = 0
        no_oa_count = 0
        failed_count = 0

        for i, paper_path in enumerate(papers, 1):
            paper_name = paper_path.name
            pdf_filename = paper_name.replace('.md', '.pdf')
            pdf_path = PDFS_DIR / pdf_filename

            # Skip if already downloaded
            if pdf_path.exists():
                continue

            percent = int(100 * i / len(papers))
            logger.info(f"[{i:3d}/{len(papers)}] ({percent:3d}%) {paper_name[:55]:55s} ... ")

            content = paper_path.read_text(encoding='utf-8', errors='ignore')
            fm, _ = self.extract_frontmatter(content)

            # Get current metadata
            pdf_url = self.extract_field(fm, 'pdf')
            url = self.extract_field(fm, 'url')

            # Check if we already have a valid URL
            if self.is_valid_pdf_url(pdf_url):
                success, msg = self.download_from_url(pdf_url, pdf_path)
                if success:
                    logger.info(f"✓ Direct ({msg})")
                    self.log['downloaded'][paper_name] = {"source": "Direct", "url": pdf_url}
                    downloaded_count += 1
                else:
                    logger.warning(f"✗ Direct failed ({msg})")
                    failed_count += 1
                self.save_log()
                continue

            # Try Semantic Scholar
            title = self.extract_field(fm, 'short_title')
            doi = self.extract_doi(url) if url else None
            arxiv_id = self.extract_arxiv_id(url) if url else None

            oa_result = self.search_semantic_scholar(title, doi, arxiv_id)

            if oa_result:
                success, msg = self.download_from_url(oa_result['url'], pdf_path)
                if success:
                    logger.info(f"✓ SS OA ({msg})")
                    self.log['found'][paper_name] = oa_result
                    self.log['downloaded'][paper_name] = {
                        "source": "SemanticScholar",
                        "url": oa_result['url']
                    }
                    downloaded_count += 1
                    found_count += 1
                else:
                    logger.warning(f"⚠ SS found but download failed ({msg})")
                    failed_count += 1
            else:
                logger.warning(f"⚠ No open access PDF found")
                self.log['no_oa'][paper_name] = {
                    "url": url,
                    "doi": doi
                }
                no_oa_count += 1

            self.save_log()

        logger.info(f"\n{'='*80}")
        logger.info(f"SUMMARY")
        logger.info(f"{'='*80}")
        logger.info(f"Downloaded:     {downloaded_count:4d} ✓")
        logger.info(f"Found (SS):     {found_count:4d} (from Semantic Scholar)")
        logger.info(f"No OA:          {no_oa_count:4d} ⚠")
        logger.info(f"Failed:         {failed_count:4d} ✗")
        logger.info(f"\nTotal PDFs: {len(list(PDFS_DIR.glob('*.pdf')))}/{len(papers)}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Find and download public PDFs")
    parser.add_argument('--download-all', action='store_true', help='Find and download all PDFs')
    parser.add_argument('--report', action='store_true', help='Show status')

    args = parser.parse_args()

    finder = PublicPDFFinder()

    if args.report:
        logger.info(f"\nFound: {len(finder.log['found'])}")
        logger.info(f"Downloaded: {len(finder.log['downloaded'])}")
        logger.info(f"No OA: {len(finder.log['no_oa'])}")
        logger.info(f"Failed: {len(finder.log['failed'])}")

    elif args.download_all:
        finder.find_and_download_all()
    else:
        logger.info("Use --download-all or --report")


if __name__ == "__main__":
    main()
