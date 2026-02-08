#!/usr/bin/env python3
"""
Batch PDF Downloader for CEI Literature Vault

Downloads PDFs for all papers with online links in parallel with:
- Resume capability (skip already downloaded)
- Rate limiting
- Progress tracking
- Detailed error logging
- Metadata updates

Usage:
    python3 PYTHON/batch_pdf_downloader.py                    # Download all missing PDFs
    python3 PYTHON/batch_pdf_downloader.py --start 100       # Start from paper 100
    python3 PYTHON/batch_pdf_downloader.py --limit 50        # Download only 50 papers
    python3 PYTHON/batch_pdf_downloader.py --report           # Show download status
    python3 PYTHON/batch_pdf_downloader.py --retry-failed     # Retry papers that failed
"""

import sys
import re
import json
import time
import argparse
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Tuple
import logging

logger = logging.getLogger(__name__)

# Setup paths - use vault_config for external PDF location
from vault_config import PAPERS_DIR, PDFS_DIR, WORKSPACE_ROOT
LOG_FILE = WORKSPACE_ROOT / "20260124-pdf_download_log.json"

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
RATE_LIMIT = 1.0  # seconds between downloads


class BatchPDFDownloader:
    def __init__(self):
        PDFS_DIR.mkdir(exist_ok=True)
        self.load_log()

    def load_log(self):
        """Load download progress from log file."""
        if LOG_FILE.exists():
            with open(LOG_FILE) as f:
                self.log = json.load(f)
        else:
            self.log = {
                "downloaded": {},
                "failed": {},
                "skipped": {},
                "paywalled": {}
            }

    def save_log(self):
        """Save progress to log file."""
        with open(LOG_FILE, 'w') as f:
            json.dump(self.log, f, indent=2)

    def extract_frontmatter(self, content: str) -> Tuple[str, str]:
        """Extract YAML frontmatter and body."""
        match = re.search(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
        if match:
            return match.group(1), match.group(2)
        return "", content

    def extract_field(self, frontmatter: str, field: str) -> Optional[str]:
        """Extract field from YAML."""
        pattern = rf'^{field}:\s*"?([^"\n]+)"?'
        match = re.search(pattern, frontmatter, re.MULTILINE)
        return match.group(1) if match else None

    def get_all_papers_to_download(self) -> List[Tuple[Path, str, str]]:
        """Get list of (paper_path, pdf_url) tuples for papers needing downloads."""
        papers_to_download = []

        for paper_file in sorted(PAPERS_DIR.glob("*.md")):
            paper_name = paper_file.name
            content = paper_file.read_text(encoding='utf-8', errors='ignore')
            fm, _ = self.extract_frontmatter(content)

            # Skip if already downloaded
            if paper_name in self.log["downloaded"]:
                continue

            # Skip if marked as paywalled
            if paper_name in self.log["paywalled"]:
                continue

            # Get PDF URL
            pdf_url = self.extract_field(fm, 'pdf')
            if not pdf_url:
                continue

            # Check if local PDF already exists
            local_pdf_field = self.extract_field(fm, 'local_pdf')
            if local_pdf_field:
                local_path = REPO_ROOT / local_pdf_field
                if local_path.exists():
                    continue

            papers_to_download.append((paper_file, paper_name, pdf_url))

        return papers_to_download

    def download_pdf(self, pdf_url: str, pdf_path: Path) -> Tuple[bool, str, int]:
        """
        Download a single PDF.
        Returns: (success, message, size_mb)
        """
        try:
            req = urllib.request.Request(pdf_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as response:
                data = response.read()

                # Verify it's a PDF
                if not data.startswith(b'%PDF'):
                    return False, f"Invalid PDF (magic: {data[:10]})", 0

                # Save file
                with open(pdf_path, 'wb') as f:
                    f.write(data)

                size_mb = pdf_path.stat().st_size / (1024 * 1024)
                return True, f"OK ({size_mb:.2f} MB)", size_mb

        except urllib.error.HTTPError as e:
            if e.code == 403:
                return False, "Forbidden (403) - Likely paywalled", 0
            elif e.code == 404:
                return False, "Not found (404)", 0
            elif e.code == 410:
                return False, "Gone (410) - URL no longer valid", 0
            else:
                return False, f"HTTP error {e.code}", 0

        except urllib.error.URLError as e:
            return False, f"URL error: {str(e)[:50]}", 0

        except Exception as e:
            return False, f"Error: {str(e)[:50]}", 0

    def update_metadata(self, paper_path: Path, pdf_url: str, pdf_filename: str) -> bool:
        """Update paper metadata with PDF links."""
        try:
            # Use the YAML utilities
            sys.path.insert(0, str(REPO_ROOT / "PYTHON"))
            from yaml_frontmatter_utils import (
                extract_frontmatter,
                parse_frontmatter,
                rebuild_frontmatter,
                write_paper,
            )

            content = paper_path.read_text(encoding='utf-8', errors='ignore')
            fm, body = extract_frontmatter(content)
            fields = parse_frontmatter(fm)

            # Update fields
            fields['pdf'] = pdf_url
            fields['local_pdf'] = f"PDFs/{pdf_filename}"

            # Rebuild and write
            new_fm = rebuild_frontmatter(fields)
            write_paper(paper_path, new_fm, body, validate=True)

            return True

        except Exception as e:
            logger.warning(f"      Metadata update failed: {e}")
            return False

    def batch_download(self, start: int = 0, limit: Optional[int] = None):
        """Download all missing PDFs in batch."""
        papers = self.get_all_papers_to_download()

        if limit:
            papers = papers[start:start+limit]
        else:
            papers = papers[start:]

        total = len(papers)
        logger.info(f"\n{'='*80}")
        logger.info(f"BATCH PDF DOWNLOADER")
        logger.info(f"{'='*80}")
        logger.info(f"Papers to download: {total}")
        logger.info(f"Already downloaded (from log): {len(self.log['downloaded'])}")
        logger.info(f"Already paywalled (from log): {len(self.log['paywalled'])}")
        logger.info("")

        if total == 0:
            logger.info("All papers already have local PDFs!")
            return

        downloaded = 0
        failed = 0
        paywalled = 0

        for i, (paper_path, paper_name, pdf_url) in enumerate(papers, 1):
            # Progress indicator
            percent = int(100 * i / total)
            status = f"[{i:3d}/{total}] ({percent:3d}%) {paper_name}"
            logger.info(f"{status} ... ")

            # Prepare output path
            pdf_filename = paper_name.replace('.md', '.pdf')
            pdf_path = PDFS_DIR / pdf_filename

            # Download
            success, message, size_mb = self.download_pdf(pdf_url, pdf_path)

            if success:
                # Update metadata
                self.update_metadata(paper_path, pdf_url, pdf_filename)
                self.log["downloaded"][paper_name] = {
                    "url": pdf_url,
                    "size_mb": size_mb,
                    "timestamp": datetime.now().isoformat()
                }
                downloaded += 1
                logger.info(f"{message}")

            else:
                # Log failure
                if "paywalled" in message.lower() or "403" in message:
                    self.log["paywalled"][paper_name] = {
                        "url": pdf_url,
                        "reason": message,
                        "timestamp": datetime.now().isoformat()
                    }
                    paywalled += 1
                    logger.warning(f"{message}")
                else:
                    self.log["failed"][paper_name] = {
                        "url": pdf_url,
                        "reason": message,
                        "timestamp": datetime.now().isoformat()
                    }
                    failed += 1
                    logger.error(f"{message}")

            # Rate limiting
            time.sleep(RATE_LIMIT)

            # Save progress every 10 papers
            if i % 10 == 0:
                self.save_log()

        # Final save
        self.save_log()

        # Summary
        logger.info(f"\n{'='*80}")
        logger.info(f"DOWNLOAD SUMMARY")
        logger.info(f"{'='*80}")
        logger.info(f"Downloaded:     {downloaded:4d}")
        logger.info(f"Failed:         {failed:4d}")
        logger.info(f"Paywalled:      {paywalled:4d}")
        logger.info(f"{'─'*40}")
        logger.info(f"Total:          {downloaded + failed + paywalled:4d}")
        logger.info(f"\nTotal local PDFs: {len(list(PDFS_DIR.glob('*.pdf')))}")

    def print_report(self):
        """Print download status report."""
        logger.info(f"\n{'='*80}")
        logger.info(f"PDF DOWNLOAD STATUS REPORT")
        logger.info(f"{'='*80}\n")

        papers = sorted(PAPERS_DIR.glob("*.md"))
        total = len(papers)

        # Count local PDFs
        local_pdf_count = len(list(PDFS_DIR.glob("*.pdf")))

        logger.info(f"Total papers: {total}")
        logger.info(f"Local PDFs: {local_pdf_count} ({100*local_pdf_count/total:.1f}%)")
        logger.info(f"Missing local PDFs: {total - local_pdf_count} ({100*(total-local_pdf_count)/total:.1f}%)")

        logger.info(f"\nDownload Log:")
        logger.info(f"  Downloaded: {len(self.log['downloaded'])}")
        logger.info(f"  Failed: {len(self.log['failed'])}")
        logger.info(f"  Paywalled: {len(self.log['paywalled'])}")

        # Show some failures
        if self.log['failed']:
            logger.info(f"\nRecent failures (first 10):")
            for i, (paper, info) in enumerate(list(self.log['failed'].items())[:10], 1):
                logger.info(f"  {i}. {paper}")
                logger.info(f"     Reason: {info['reason']}")

        if self.log['paywalled']:
            logger.info(f"\nPaywalled papers (first 10):")
            for i, (paper, info) in enumerate(list(self.log['paywalled'].items())[:10], 1):
                logger.info(f"  {i}. {paper}")

    def retry_failed(self):
        """Retry papers that previously failed."""
        if not self.log['failed']:
            logger.info("No failed papers to retry.")
            return

        logger.info(f"Retrying {len(self.log['failed'])} failed papers...\n")

        # Move failed back to pending
        failed_papers = list(self.log['failed'].keys())
        for paper in failed_papers:
            del self.log['failed'][paper]

        self.save_log()

        # Re-run batch download
        self.batch_download(limit=len(failed_papers))


def main():
    parser = argparse.ArgumentParser(
        description="Batch download PDFs for CEI Literature Vault"
    )
    parser.add_argument('--start', type=int, default=0,
                        help='Start from paper index N')
    parser.add_argument('--limit', type=int,
                        help='Limit to N papers')
    parser.add_argument('--report', action='store_true',
                        help='Print download status report')
    parser.add_argument('--retry-failed', action='store_true',
                        help='Retry papers that previously failed')

    args = parser.parse_args()

    downloader = BatchPDFDownloader()

    if args.report:
        downloader.print_report()
    elif args.retry_failed:
        downloader.retry_failed()
    else:
        downloader.batch_download(start=args.start, limit=args.limit)


if __name__ == "__main__":
    main()
