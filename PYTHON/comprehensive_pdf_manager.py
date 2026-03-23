#!/usr/bin/env python3
"""
Comprehensive PDF Manager for CEI Literature Vault

Ensures every paper has:
1. An online PDF link (`pdf` field)
2. A downloaded local PDF in Lit-WS-PDFs/

Features:
- Discovers PDFs from multiple sources (arXiv, ACL, Semantic Scholar, DOI)
- Batch downloads with rate limiting
- Updates metadata with both online and local links
- Resume capability for interrupted downloads
- Detailed progress reporting

Usage:
    python3 PYTHON/comprehensive_pdf_manager.py --discover   # Find missing links
    python3 PYTHON/comprehensive_pdf_manager.py --download    # Download all PDFs
    python3 PYTHON/comprehensive_pdf_manager.py --download-missing  # Download only missing
    python3 PYTHON/comprehensive_pdf_manager.py --report      # Generate status report
"""

import re
import json
import time
import argparse
import logging
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Tuple
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)

# Setup paths - use vault_config for external PDF location
from vault_config import PAPERS_DIR, PDFS_DIR, WORKSPACE_ROOT
LOG_FILE = WORKSPACE_ROOT / "20260124-pdf_download_log.json"

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
ARXIV_RATE_LIMIT = 0.5  # seconds between arXiv requests
SEMANTIC_SCHOLAR_RATE_LIMIT = 4.0  # seconds between Semantic Scholar requests


class PDFManager:
    def __init__(self):
        PDFS_DIR.mkdir(exist_ok=True)
        self.load_log()

    def load_log(self):
        """Load download progress from log file."""
        if LOG_FILE.exists():
            with open(LOG_FILE) as f:
                self.log = json.load(f)
        else:
            self.log = {"downloaded": {}, "failed": {}, "skipped": {}}

    def save_log(self):
        """Save download progress to log file."""
        with open(LOG_FILE, 'w') as f:
            json.dump(self.log, f, indent=2)

    def extract_frontmatter(self, content: str) -> Tuple[str, str]:
        """Extract YAML frontmatter from paper content."""
        match = re.search(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
        if match:
            return match.group(1), match.group(2)
        return "", content

    def extract_field(self, frontmatter: str, field: str) -> Optional[str]:
        """Extract a field value from YAML frontmatter."""
        pattern = rf'^{field}:\s*"?([^"\n]+)"?'
        match = re.search(pattern, frontmatter, re.MULTILINE)
        return match.group(1) if match else None

    def arxiv_pdf_url(self, arxiv_id: str) -> str:
        """Convert arXiv ID to PDF URL."""
        return f"https://arxiv.org/pdf/{arxiv_id}.pdf"

    def find_arxiv_abstract(self, arxiv_id: str) -> Optional[str]:
        """Get arXiv abstract to find paper metadata."""
        try:
            time.sleep(ARXIV_RATE_LIMIT)
            url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as response:
                data = response.read().decode('utf-8')
                root = ET.fromstring(data)
                ns = {'atom': 'http://www.w3.org/2005/Atom'}
                entry = root.find('atom:entry', ns)
                if entry:
                    return entry.find('atom:summary', ns).text if entry.find('atom:summary', ns) is not None else None
        except Exception as e:
            logger.warning(f"  arXiv fetch failed: {e}")
        return None

    def discover_missing_pdfs(self) -> Dict[str, Dict]:
        """Find all papers missing online PDF links."""
        missing = {}

        for paper_file in sorted(PAPERS_DIR.glob("*.md")):
            content = paper_file.read_text(encoding='utf-8', errors='ignore')
            fm, _ = self.extract_frontmatter(content)

            pdf_url = self.extract_field(fm, 'pdf')
            if pdf_url:
                continue  # Already has PDF URL

            # Try to find one from available fields
            url = self.extract_field(fm, 'url')
            arxiv_id = self.extract_arxiv_id(url)

            missing[paper_file.name] = {
                'url': url,
                'arxiv_id': arxiv_id,
                'type': 'missing_pdf_field',
            }

        return missing

    def extract_arxiv_id(self, url: Optional[str]) -> Optional[str]:
        """Extract arXiv ID from URL."""
        if not url:
            return None
        match = re.search(r'arxiv\.org/(?:abs|pdf)/(\d+\.\d+)', url)
        return match.group(1) if match else None

    def extract_doi(self, content: str) -> Optional[str]:
        """Extract DOI from paper content."""
        # Try frontmatter first
        fm, body = self.extract_frontmatter(content)
        doi = self.extract_field(fm, 'doi')
        if doi:
            return doi

        # Search body for DOI
        match = re.search(r'doi\.org/(10\.\S+)', body)
        return match.group(1) if match else None

    def convert_to_pdf_url(self, url: str) -> str:
        """Convert various URL formats to direct PDF URLs."""
        if not url:
            return None

        # arXiv PDF
        if 'arxiv.org/abs/' in url:
            arxiv_id = self.extract_arxiv_id(url)
            if arxiv_id:
                return self.arxiv_pdf_url(arxiv_id)

        # ACL Anthology
        if 'aclanthology.org/' in url:
            return url.rstrip('/') + '.pdf' if not url.endswith('.pdf') else url

        # OpenReview
        if 'openreview.net/forum' in url:
            return url.replace('/forum?', '/pdf?')

        # Semantic Scholar
        if 'semanticscholar.org/' in url:
            # Try to extract paper ID and construct PDF URL
            match = re.search(r'/(\w+)', url.split('/')[-1])
            if match:
                return f"https://api.semanticscholar.org/v1/papers/{match.group(1)}/corpus"

        return url if url.endswith('.pdf') else None

    def download_pdf(self, paper_name: str, pdf_url: str, skip_if_exists: bool = True) -> bool:
        """Download a single PDF and update metadata."""
        if skip_if_exists:
            # Check if local PDF exists
            pdf_path = PDFS_DIR / paper_name.replace('.md', '.pdf')
            if pdf_path.exists():
                return True

        try:
            logger.info(f"  Downloading from: {pdf_url}")
            req = urllib.request.Request(pdf_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as response:
                data = response.read()

                # Verify PDF
                if not data.startswith(b'%PDF'):
                    logger.warning(f"    Not a valid PDF (first bytes: {data[:10]})")
                    return False

                # Save
                pdf_path = PDFS_DIR / paper_name.replace('.md', '.pdf')
                with open(pdf_path, 'wb') as f:
                    f.write(data)

                size_mb = pdf_path.stat().st_size / (1024 * 1024)
                logger.info(f"    Downloaded {size_mb:.2f} MB")

                # Update metadata
                self.update_paper_metadata(PAPERS_DIR / paper_name, pdf_url, pdf_path.name)
                return True

        except urllib.error.HTTPError as e:
            if e.code == 403:
                logger.warning(f"    Forbidden (paywall)")
            elif e.code == 404:
                logger.warning(f"    Not found (404)")
            else:
                logger.error(f"    HTTP error {e.code}")
            return False
        except Exception as e:
            logger.error(f"    Error: {e}")
            return False

    def update_paper_metadata(self, paper_path: Path, pdf_url: str, pdf_filename: str):
        """Update paper metadata with PDF links."""
        from yaml_frontmatter_utils import (
            extract_frontmatter,
            parse_frontmatter,
            rebuild_frontmatter,
            write_paper,
        )

        try:
            content = paper_path.read_text(encoding='utf-8', errors='ignore')
            fm, body = extract_frontmatter(content)
            fields = parse_frontmatter(fm)

            # Update fields
            fields['pdf'] = pdf_url
            fields['local_pdf'] = f"Lit-WS-PDFs/{pdf_filename}"

            # Rebuild and write
            new_fm = rebuild_frontmatter(fields)
            write_paper(paper_path, new_fm, body, validate=True)

            logger.info(f"    Updated metadata")
        except Exception as e:
            logger.warning(f"    Metadata update failed: {e}")

    def batch_download(self, limit: Optional[int] = None, resume: bool = True):
        """Download all missing PDFs."""
        papers = sorted(PAPERS_DIR.glob("*.md"))

        if limit:
            papers = papers[:limit]

        downloaded = 0
        skipped = 0
        failed = 0

        logger.info("=" * 70)
        logger.info("BATCH PDF DOWNLOAD")
        logger.info("=" * 70)
        logger.info(f"Total papers: {len(papers)}")

        for i, paper_file in enumerate(papers, 1):
            paper_name = paper_file.name
            logger.info(f"[{i}/{len(papers)}] {paper_name}")

            content = paper_file.read_text(encoding='utf-8', errors='ignore')
            fm, _ = self.extract_frontmatter(content)

            # Check if already downloaded
            local_pdf_field = self.extract_field(fm, 'local_pdf')
            if local_pdf_field:
                local_path = REPO_ROOT / local_pdf_field
                if local_path.exists():
                    logger.info(f"  Already downloaded")
                    skipped += 1
                    continue

            # Get PDF URL
            pdf_url = self.extract_field(fm, 'pdf')
            if not pdf_url:
                logger.warning(f"  No PDF URL found")
                failed += 1
                continue

            # Try to download
            if self.download_pdf(paper_name, pdf_url, skip_if_exists=True):
                downloaded += 1
                self.log["downloaded"][paper_name] = datetime.now().isoformat()
            else:
                failed += 1
                self.log["failed"][paper_name] = datetime.now().isoformat()

            self.save_log()

        logger.info("=" * 70)
        logger.info("DOWNLOAD SUMMARY")
        logger.info("=" * 70)
        logger.info(f"Downloaded: {downloaded}")
        logger.info(f"Already had: {skipped}")
        logger.info(f"Failed: {failed}")

    def generate_report(self):
        """Generate status report."""
        missing_pdfs = self.discover_missing_pdfs()

        logger.info("=" * 70)
        logger.info("PDF & LINK STATUS REPORT")
        logger.info("=" * 70)

        # Papers with issues
        logger.info(f"Papers missing online PDF link: {len(missing_pdfs)}")
        if missing_pdfs:
            logger.info("Papers needing PDF URL discovery:")
            for paper_name, info in sorted(missing_pdfs.items())[:20]:
                logger.info(f"  - {paper_name}")
                if info['arxiv_id']:
                    logger.info(f"    arXiv: {info['arxiv_id']}")
                elif info['url']:
                    logger.info(f"    URL: {info['url']}")

        # Local PDFs
        local_pdfs = len(list(PDFS_DIR.glob("*.pdf")))
        logger.info(f"Local PDFs downloaded: {local_pdfs}/580")

        # Summary stats
        logger.info("=" * 70)
        stats = self.get_stats()
        for key, value in stats.items():
            logger.info(f"{key}: {value}")


    def get_stats(self) -> Dict:
        """Get comprehensive statistics."""
        stats = {
            "total_papers": len(list(PAPERS_DIR.glob("*.md"))),
            "local_pdfs": len(list(PDFS_DIR.glob("*.pdf"))),
            "downloaded_from_log": len(self.log["downloaded"]),
            "failed_from_log": len(self.log["failed"]),
        }
        return stats


def main():
    parser = argparse.ArgumentParser(
        description="Comprehensive PDF manager for CEI Literature Vault"
    )
    parser.add_argument('--discover', action='store_true',
                        help='Discover papers missing online PDF links')
    parser.add_argument('--download', action='store_true',
                        help='Download all PDFs')
    parser.add_argument('--download-missing', action='store_true',
                        help='Download only missing local PDFs')
    parser.add_argument('--report', action='store_true',
                        help='Generate status report')
    parser.add_argument('--limit', type=int,
                        help='Limit batch operations to N papers')
    parser.add_argument('--no-resume', action='store_true',
                        help='Do not resume from previous downloads')

    args = parser.parse_args()

    manager = PDFManager()

    if args.discover:
        missing = manager.discover_missing_pdfs()
        logger.info(f"Found {len(missing)} papers missing PDF URLs")
        for name, info in sorted(missing.items())[:10]:
            logger.info(f"{name}: {info}")

    elif args.download:
        manager.batch_download(limit=args.limit, resume=not args.no_resume)

    elif args.download_missing:
        # Download only papers without local PDF
        manager.batch_download(limit=args.limit, resume=not args.no_resume)

    elif args.report:
        manager.generate_report()

    else:
        manager.generate_report()


if __name__ == "__main__":
    main()
