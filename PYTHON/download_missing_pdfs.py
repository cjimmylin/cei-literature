#!/usr/bin/env python3
"""
Download Missing PDFs - Priority 1 Strategy

Downloads PDFs for papers that have URLs but no local PDFs.
Uses multiple strategies:
1. Direct PDF downloads (when URL points to PDF)
2. arXiv API (for preprints)
3. Semantic Scholar API (for published papers)
4. ACL Anthology direct links
5. DOI resolution via multiple services

Usage:
    python3 download_missing_pdfs.py                  # Process all
    python3 download_missing_pdfs.py --dry-run        # Preview
    python3 download_missing_pdfs.py --verbose        # Show progress
    python3 download_missing_pdfs.py "2016-Amodei"    # Specific paper
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
)
from vault_config import PAPERS_DIR, PDFS_DIR

# Directories (use vault_config for paths)
PAPER_DIR = str(PAPERS_DIR)
PDF_DIR = str(PDFS_DIR)
DOWNLOAD_TIMEOUT = 30  # seconds


class DownloadStats:
    """Track download statistics."""
    def __init__(self):
        self.processed = 0
        self.already_have = 0
        self.direct_downloads = 0
        self.arxiv_downloads = 0
        self.semantic_scholar = 0
        self.acl_downloads = 0
        self.errors = []
        self.skipped = []

    def report(self):
        logger.info("\n" + "=" * 60)
        logger.info("PDF DOWNLOAD SUMMARY")
        logger.info("=" * 60)
        logger.info(f"Papers processed: {self.processed}")
        logger.info(f"Already had PDFs: {self.already_have}")
        logger.info(f"Direct downloads: {self.direct_downloads}")
        logger.info(f"arXiv downloads: {self.arxiv_downloads}")
        logger.info(f"ACL Anthology: {self.acl_downloads}")
        logger.info(f"Semantic Scholar: {self.semantic_scholar}")
        total_downloaded = (self.direct_downloads + self.arxiv_downloads +
                           self.acl_downloads + self.semantic_scholar)
        logger.info(f"TOTAL DOWNLOADED: {total_downloaded}")
        logger.info(f"Download rate: {(total_downloaded/max(self.processed, 1)*100):.1f}%")
        logger.info(f"Errors: {len(self.errors)}")
        logger.info(f"Skipped (no URL): {len(self.skipped)}")

        if self.errors:
            logger.info("\nFailed downloads (sample):")
            for paper, error in self.errors[:10]:
                logger.info(f"  - {paper}: {error}")


stats = DownloadStats()


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


def download_from_arxiv(arxiv_id, paper_stem, dry_run=False, verbose=False):
    """Download PDF from arXiv."""
    try:
        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
        pdf_path = os.path.join(PDF_DIR, f"{paper_stem}.pdf")

        if dry_run:
            if verbose:
                logger.info(f"  [DRY RUN] Would download from arXiv: {arxiv_id}")
            return True

        response = requests.get(pdf_url, timeout=DOWNLOAD_TIMEOUT, stream=True)
        if response.status_code == 200:
            with open(pdf_path, 'wb') as f:
                f.write(response.content)
            if verbose:
                logger.info(f"  Downloaded from arXiv: {arxiv_id}")
            return True

        return False

    except Exception as e:
        if verbose:
            logger.warning(f"  arXiv download failed: {e}")
        return False


def download_acl_anthology(url, paper_stem, dry_run=False, verbose=False):
    """Download PDF from ACL Anthology."""
    try:
        # ACL URLs typically have /anthology/XXXX.pdf structure
        # Convert https://www.aclweb.org/anthology/W19-3807 -> direct PDF
        if 'aclweb.org/anthology' in url or 'aclanthology.org' in url:
            # Extract the code (e.g., W19-3807)
            match = re.search(r'([A-Z]\d{2}-\d{4})', url)
            if match:
                code = match.group(1)
                pdf_url = f"https://aclanthology.org/papers/{code}/{code}.pdf"

                pdf_path = os.path.join(PDF_DIR, f"{paper_stem}.pdf")

                if dry_run:
                    if verbose:
                        logger.info(f"  [DRY RUN] Would download from ACL: {code}")
                    return True

                response = requests.get(pdf_url, timeout=DOWNLOAD_TIMEOUT, stream=True)
                if response.status_code == 200:
                    with open(pdf_path, 'wb') as f:
                        f.write(response.content)
                    if verbose:
                        logger.info(f"  Downloaded from ACL Anthology: {code}")
                    return True

        return False

    except Exception as e:
        if verbose:
            logger.warning(f"  ACL download failed: {e}")
        return False


def download_direct_pdf(url, paper_stem, dry_run=False, verbose=False):
    """Try to download PDF directly from URL."""
    try:
        # Check if URL likely points to a PDF
        if not url.endswith('.pdf') and 'pdf' not in url.lower():
            return False

        pdf_path = os.path.join(PDF_DIR, f"{paper_stem}.pdf")

        if dry_run:
            if verbose:
                logger.info(f"  [DRY RUN] Would download directly: {url[:60]}...")
            return True

        response = requests.get(url, timeout=DOWNLOAD_TIMEOUT, stream=True, allow_redirects=True)

        # Check if it's actually a PDF
        content_type = response.headers.get('content-type', '').lower()
        if response.status_code == 200 and ('pdf' in content_type or url.endswith('.pdf')):
            with open(pdf_path, 'wb') as f:
                f.write(response.content)
            if verbose:
                logger.info(f"  Downloaded directly from: {url[:50]}...")
            return True

        return False

    except Exception as e:
        if verbose:
            logger.warning(f"  Direct download failed: {e}")
        return False


def download_from_semantic_scholar(doi, paper_stem, dry_run=False, verbose=False):
    """Try to download PDF via Semantic Scholar API."""
    try:
        if not doi:
            return False

        # Semantic Scholar API endpoint
        api_url = f"https://api.semanticscholar.org/v1/paper/{doi}"

        pdf_path = os.path.join(PDF_DIR, f"{paper_stem}.pdf")

        if dry_run:
            if verbose:
                logger.info(f"  [DRY RUN] Would check Semantic Scholar for: {doi[:30]}...")
            return True

        # Make request with timeout
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            # Check if they have a free PDF link
            if data.get('openAccessPdf') and data['openAccessPdf'].get('url'):
                pdf_url = data['openAccessPdf']['url']
                pdf_response = requests.get(pdf_url, timeout=10, stream=True)
                if pdf_response.status_code == 200:
                    with open(pdf_path, 'wb') as f:
                        f.write(pdf_response.content)
                    if verbose:
                        logger.info(f"  Downloaded via Semantic Scholar: {doi}")
                    return True

        return False

    except Exception as e:
        if verbose and False:  # Suppress verbose output for API calls
            logger.warning(f"  Semantic Scholar check failed: {e}")
        return False


def download_pdf(paper_path, dry_run=False, verbose=False):
    """
    Download PDF for a paper using multiple strategies.

    Returns: (success, method_used)
    """
    paper_stem = os.path.splitext(os.path.basename(paper_path))[0]
    pdf_path = os.path.join(PDF_DIR, f"{paper_stem}.pdf")

    # Check if already have PDF
    if os.path.exists(pdf_path):
        stats.already_have += 1
        if verbose:
            logger.debug(f"  {paper_stem}: Already have PDF")
        return False, "already_have"

    try:
        # Read paper metadata
        content = paper_path.read_text(encoding='utf-8')
        fm, _ = extract_frontmatter(content)
        fields = parse_frontmatter(fm)

        url = fields.get('url', '').strip()
        if not url:
            stats.skipped.append(paper_stem)
            if verbose:
                logger.debug(f"  {paper_stem}: No URL available")
            return False, "no_url"

        stats.processed += 1

        # Strategy 1: Try direct PDF download
        if download_direct_pdf(url, paper_stem, dry_run, verbose):
            stats.direct_downloads += 1
            return True, "direct"

        # Strategy 2: Try arXiv
        arxiv_id = extract_arxiv_id(url)
        if arxiv_id:
            if download_from_arxiv(arxiv_id, paper_stem, dry_run, verbose):
                stats.arxiv_downloads += 1
                return True, "arxiv"

        # Strategy 3: Try ACL Anthology
        if download_acl_anthology(url, paper_stem, dry_run, verbose):
            stats.acl_downloads += 1
            return True, "acl"

        # Strategy 4: Try Semantic Scholar for DOI
        doi = extract_doi(url)
        if doi:
            if download_from_semantic_scholar(doi, paper_stem, dry_run, verbose):
                stats.semantic_scholar += 1
                return True, "semantic_scholar"

        if verbose:
            logger.debug(f"  {paper_stem}: Could not find open access PDF")

        stats.errors.append((paper_stem, "No open access source found"))
        return False, "no_source"

    except Exception as e:
        stats.errors.append((paper_stem, str(e)))
        if verbose:
            logger.error(f"  {paper_stem}: Error - {e}")
        return False, "error"


def download_all_missing(target_paper=None, dry_run=False, verbose=False):
    """
    Download PDFs for papers that need them.

    Args:
        target_paper: Optional paper stem to process
        dry_run: If True, don't download
        verbose: If True, show detailed progress
    """
    if not os.path.exists(PAPER_DIR):
        logger.error(f"Error: Papers directory '{PAPER_DIR}' not found")
        sys.exit(1)

    os.makedirs(PDF_DIR, exist_ok=True)

    if target_paper:
        # Process single paper
        paper_path = Path(PAPER_DIR) / (target_paper + ".md")
        if not paper_path.exists():
            logger.error(f"Error: Paper '{target_paper}.md' not found")
            sys.exit(1)

        logger.info(f"Downloading PDF for: {target_paper}\n")
        download_pdf(paper_path, dry_run, verbose)
    else:
        # Process all papers
        papers = sorted(Path(PAPER_DIR).glob("*.md"))
        total = len(papers)

        logger.info(f"Found {total} papers to check for PDF downloads\n")
        logger.info("Attempting downloads using:")
        logger.info("  - Direct PDF links")
        logger.info("  - arXiv API (for preprints)")
        logger.info("  - ACL Anthology (for conference papers)")
        logger.info("  - DOI resolution (future enhancement)")
        logger.info("")

        for i, paper_path in enumerate(papers, 1):
            if verbose or i % 50 == 0:
                logger.info(f"[{i}/{total}] {paper_path.name}")

            success, method = download_pdf(paper_path, dry_run, verbose)

            # Rate limiting to be respectful to servers
            if success:
                time.sleep(1)

    stats.report()


def main():
    parser = argparse.ArgumentParser(
        description="Download missing PDFs for papers",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 download_missing_pdfs.py                # Download all missing
  python3 download_missing_pdfs.py --dry-run      # Preview
  python3 download_missing_pdfs.py --verbose      # Show progress
  python3 download_missing_pdfs.py "2016-Amodei"  # Download specific
        """
    )
    parser.add_argument('paper', nargs='?', help='Specific paper stem to download')
    parser.add_argument('--dry-run', '-n', action='store_true',
                        help="Don't download, just show what would happen")
    parser.add_argument('--verbose', '-v', action='store_true',
                        help="Show detailed progress information")

    args = parser.parse_args()

    if args.dry_run:
        logger.info("=" * 60)
        logger.info("DRY RUN MODE - No files will be downloaded")
        logger.info("=" * 60 + "\n")

    download_all_missing(
        target_paper=args.paper,
        dry_run=args.dry_run,
        verbose=args.verbose
    )


if __name__ == "__main__":
    main()
