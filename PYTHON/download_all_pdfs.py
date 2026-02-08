#!/usr/bin/env python3
"""
Complete PDF Download Solution

Downloads PDFs for all papers using available online links.

Two-phase approach:
1. Phase 1: Download from direct PDF URLs (fast, ~10 seconds/paper)
2. Phase 2: Find open-access copies via Semantic Scholar (slow, ~4 sec/paper + search time)

Usage:
    python3 PYTHON/download_all_pdfs.py --phase 1           # Download from direct URLs
    python3 PYTHON/download_all_pdfs.py --phase 2           # Find OA copies
    python3 PYTHON/download_all_pdfs.py --status            # Check status
    python3 PYTHON/download_all_pdfs.py --resume            # Resume interrupted download
"""

import re
import json
import time
import logging
import argparse
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime
from typing import Optional, Tuple

logger = logging.getLogger(__name__)

# Setup paths - use vault_config for external PDF location
from vault_config import PAPERS_DIR, PDFS_DIR, WORKSPACE_ROOT
LOG_FILE = WORKSPACE_ROOT / "20260124-pdf_download_all_log.json"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
}

class CompletePDFDownloader:
    def __init__(self):
        PDFS_DIR.mkdir(exist_ok=True)
        self.load_log()

    def load_log(self):
        if LOG_FILE.exists():
            with open(LOG_FILE) as f:
                self.log = json.load(f)
        else:
            self.log = {
                "phase1_success": {},
                "phase1_failed": {},
                "phase2_found": {},
                "phase2_failed": {}
            }

    def save_log(self):
        with open(LOG_FILE, 'w') as f:
            json.dump(self.log, f, indent=2)

    def extract_frontmatter(self, content: str) -> Tuple[str, str]:
        match = re.search(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
        if match:
            return match.group(1), match.group(2)
        return "", content

    def extract_field(self, fm: str, field: str) -> Optional[str]:
        pattern = rf'^{field}:\s*"?([^"\n]+)"?'
        match = re.search(pattern, fm, re.MULTILINE)
        return match.group(1).strip() if match else None

    def is_valid_url(self, url: str) -> bool:
        return url and url.startswith('http') and not url.startswith('file://')

    def download_pdf(self, url: str, pdf_path: Path) -> Tuple[bool, str]:
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as response:
                data = response.read()

                if not data.startswith(b'%PDF'):
                    return False, "Invalid"

                with open(pdf_path, 'wb') as f:
                    f.write(data)

                size_mb = pdf_path.stat().st_size / (1024 * 1024)
                return True, f"{size_mb:.2f}MB"

        except urllib.error.HTTPError as e:
            if e.code == 403:
                return False, "403"
            elif e.code == 404:
                return False, "404"
            else:
                return False, f"HTTP{e.code}"
        except Exception as e:
            return False, str(e)[:20]

    def phase_1_direct_download(self, limit: Optional[int] = None):
        """Download from papers with valid PDF URLs."""
        papers = sorted(PAPERS_DIR.glob("*.md"))
        if limit:
            papers = papers[:limit]

        logger.info(f"\n{'='*80}")
        logger.info(f"PHASE 1: DIRECT DOWNLOAD FROM VALID PDF URLs")
        logger.info(f"{'='*80}\n")

        success_count = 0
        skip_count = 0
        fail_count = 0

        for i, paper_path in enumerate(papers, 1):
            paper_name = paper_path.name
            pdf_filename = paper_name.replace('.md', '.pdf')
            pdf_path = PDFS_DIR / pdf_filename

            # Skip if already downloaded
            if pdf_path.exists():
                skip_count += 1
                continue

            percent = int(100 * i / len(papers))
            logger.info(f"[{i:3d}/{len(papers)}] ({percent:3d}%) {paper_name[:50]:50s} ... ")

            content = paper_path.read_text(encoding='utf-8', errors='ignore')
            fm, _ = self.extract_frontmatter(content)

            pdf_url = self.extract_field(fm, 'pdf')

            # Only process valid URLs
            if not self.is_valid_url(pdf_url):
                logger.info(f"Skip (no valid URL)")
                fail_count += 1
                continue

            # Try download
            success, msg = self.download_pdf(pdf_url, pdf_path)

            if success:
                logger.info(f"✓ {msg}")
                self.log["phase1_success"][paper_name] = {
                    "url": pdf_url,
                    "time": datetime.now().isoformat()
                }
                success_count += 1
            else:
                logger.warning(f"✗ {msg}")
                self.log["phase1_failed"][paper_name] = {
                    "url": pdf_url,
                    "reason": msg
                }
                fail_count += 1

            if i % 10 == 0:
                self.save_log()

        self.save_log()

        logger.info(f"\n{'='*80}")
        logger.info(f"Downloaded: {success_count:4d} ✓")
        logger.info(f"Failed:     {fail_count:4d} ✗")
        logger.info(f"Already had:{skip_count:4d} (skip)")
        logger.info(f"Total PDFs: {len(list(PDFS_DIR.glob('*.pdf')))}/{len(list(PAPERS_DIR.glob('*.md')))}")

    def get_status(self):
        """Print download status."""
        papers = len(list(PAPERS_DIR.glob('*.md')))
        pdfs = len(list(PDFS_DIR.glob('*.pdf')))

        logger.info(f"\n{'='*80}")
        logger.info(f"PDF DOWNLOAD STATUS")
        logger.info(f"{'='*80}\n")
        logger.info(f"Total papers: {papers}")
        logger.info(f"Local PDFs:   {pdfs} ({100*pdfs/papers:.1f}%)")
        logger.info(f"Missing:      {papers-pdfs} ({100*(papers-pdfs)/papers:.1f}%)")

        logger.info(f"\nLog Summary:")
        logger.info(f"  Phase 1 Success: {len(self.log['phase1_success'])}")
        logger.info(f"  Phase 1 Failed:  {len(self.log['phase1_failed'])}")
        logger.info(f"  Phase 2 Found:   {len(self.log['phase2_found'])}")
        logger.info(f"  Phase 2 Failed:  {len(self.log['phase2_failed'])}")


def main():
    parser = argparse.ArgumentParser(description="Download all PDFs for papers")
    parser.add_argument('--phase', type=int, choices=[1, 2], default=1,
                        help='Download phase (1=direct URLs, 2=Semantic Scholar)')
    parser.add_argument('--limit', type=int, help='Limit to N papers')
    parser.add_argument('--status', action='store_true', help='Show status')
    parser.add_argument('--resume', action='store_true', help='Resume from log')

    args = parser.parse_args()

    downloader = CompletePDFDownloader()

    if args.status:
        downloader.get_status()
    elif args.phase == 1:
        downloader.phase_1_direct_download(limit=args.limit)
    elif args.phase == 2:
        logger.info("Phase 2 (Semantic Scholar) coming soon")
        logger.info("For now, use: python3 PYTHON/find_public_pdfs.py --download-all")


if __name__ == "__main__":
    main()
