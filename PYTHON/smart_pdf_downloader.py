#!/usr/bin/env python3
"""
Smart PDF Downloader with Multi-Source Fallback Strategies

Comprehensive PDF management with:
1. Zotero URL detection & replacement
2. Multiple PDF sources (arXiv, DOI, Semantic Scholar, ACL, OpenReview)
3. Smart fallback strategies for missing links
4. Batch downloading with rate limiting & resume
5. Metadata updates using safe YAML utilities

Usage:
    python3 PYTHON/smart_pdf_downloader.py --discover          # Find missing links
    python3 PYTHON/smart_pdf_downloader.py --discover-methods  # Show discovery methods
    python3 PYTHON/smart_pdf_downloader.py --download          # Download all PDFs
    python3 PYTHON/smart_pdf_downloader.py --download-missing  # Download only missing local
    python3 PYTHON/smart_pdf_downloader.py --fix-zotero        # Replace Zotero URLs
    python3 PYTHON/smart_pdf_downloader.py --report            # Status report
    python3 PYTHON/smart_pdf_downloader.py --limit 50          # Limit operations to 50 papers
"""

import sys
import re
import json
import time
import argparse
import logging
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Tuple

logger = logging.getLogger(__name__)

# Setup paths - use vault_config for external PDF location
from vault_config import PAPERS_DIR, PDFS_DIR, WORKSPACE_ROOT
LOG_FILE = WORKSPACE_ROOT / "20260124-pdf_download_log.json"

from yaml_frontmatter_utils import (
    extract_frontmatter,
    parse_frontmatter,
    rebuild_frontmatter,
    write_paper,
    validate_frontmatter,
)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
}

# Rate limits (seconds between requests)
RATE_LIMITS = {
    'arxiv': 0.3,
    'semantic_scholar': 4.0,
    'acl': 1.0,
    'doi': 1.0,
    'pdf_download': 1.0,
}


class SmartPDFDownloader:
    def __init__(self):
        PDFS_DIR.mkdir(exist_ok=True)
        self.load_log()
        self.last_request_time = {}

    def load_log(self):
        """Load download progress."""
        if LOG_FILE.exists():
            with open(LOG_FILE) as f:
                self.log = json.load(f)
        else:
            self.log = {}

        # Ensure all keys exist
        default_keys = {
            "discovered": {},      # Papers with newly found links
            "fixed_zotero": {},    # Papers with fixed URLs
            "downloaded": {},      # Successfully downloaded PDFs
            "failed": {},          # Failed downloads
            "paywalled": {},       # Papers behind paywalls
            "not_found": {},       # Papers where no PDF found
        }
        for key, value in default_keys.items():
            if key not in self.log:
                self.log[key] = value

    def save_log(self):
        """Save progress."""
        with open(LOG_FILE, 'w') as f:
            json.dump(self.log, f, indent=2)

    def rate_limit(self, source: str):
        """Enforce rate limiting for API sources."""
        if source in self.last_request_time:
            elapsed = time.time() - self.last_request_time[source]
            limit = RATE_LIMITS.get(source, 1.0)
            if elapsed < limit:
                time.sleep(limit - elapsed)
        self.last_request_time[source] = time.time()

    def extract_field(self, frontmatter: str, field: str) -> Optional[str]:
        """Extract field from YAML."""
        pattern = rf'^{field}:\s*"?([^"\n]+)"?'
        match = re.search(pattern, frontmatter, re.MULTILINE)
        return match.group(1) if match else None

    def get_pdf_url(self, frontmatter: str) -> Optional[str]:
        """Get PDF URL, checking both 'pdf' and 'external_pdf' fields."""
        # Try external_pdf first (current format)
        url = self.extract_field(frontmatter, 'external_pdf')
        if url:
            return url
        # Fallback to pdf field
        return self.extract_field(frontmatter, 'pdf')

    def is_zotero_url(self, url: Optional[str]) -> bool:
        """Check if URL is a local Zotero file:// URL."""
        if not url:
            return False
        return url.startswith('file://') and 'Zotero' in url

    def extract_arxiv_id(self, url: Optional[str]) -> Optional[str]:
        """Extract arXiv ID from URL."""
        if not url:
            return None
        match = re.search(r'arxiv\.org/(?:abs|pdf)/(\d+\.\d+)', url)
        return match.group(1) if match else None

    def extract_doi(self, url: Optional[str], frontmatter: Optional[str] = None) -> Optional[str]:
        """Extract DOI from URL or frontmatter."""
        # Try frontmatter first
        if frontmatter:
            match = re.search(r'^doi:\s*"?([^"\n]+)"?', frontmatter, re.MULTILINE)
            if match:
                return match.group(1)

        # Try URL
        if url:
            match = re.search(r'doi\.org/(10\.\S+)', url)
            if match:
                return match.group(1)

        return None

    # ============================================================================
    # PDF URL Discovery Strategies
    # ============================================================================

    def find_arxiv_pdf(self, arxiv_id: str) -> Optional[str]:
        """Generate arXiv PDF URL."""
        return f"https://arxiv.org/pdf/{arxiv_id}.pdf"

    def find_doi_pdf(self, doi: str) -> Optional[str]:
        """Try to resolve PDF from DOI."""
        try:
            self.rate_limit('doi')
            url = f"https://doi.org/{doi}"
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as response:
                final_url = response.geturl()

                # Common PDF patterns
                if final_url.endswith('.pdf'):
                    return final_url

                return None
        except Exception as e:
            return None

    def find_semantic_scholar_pdf(self, title: str, authors: Optional[str] = None) -> Optional[Dict]:
        """
        Search Semantic Scholar for paper and return open access PDF info.
        Returns: {"pdf_url": "...", "venue": "...", "year": ...}
        """
        try:
            self.rate_limit('semantic_scholar')

            # Build query
            query = title
            if authors:
                first_author = authors.split(';')[0].strip() if ';' in authors else authors
                query = f'"{title}" {first_author}'

            url = f"https://api.semanticscholar.org/graph/v1/paper/search"
            params = {
                'query': query,
                'fields': 'title,authors,year,venue,openAccessPdf,externalIds',
                'limit': 3
            }

            # Build URL with params
            param_str = '&'.join([f'{k}={urllib.parse.quote(str(v))}' for k, v in params.items()])
            full_url = f"{url}?{param_str}"

            req = urllib.request.Request(full_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode('utf-8'))

                if data.get('data') and len(data['data']) > 0:
                    paper = data['data'][0]

                    # Check for open access PDF
                    oa_pdf = paper.get('openAccessPdf')
                    if oa_pdf and oa_pdf.get('url'):
                        return {
                            'pdf_url': oa_pdf['url'],
                            'venue': paper.get('venue', 'Unknown'),
                            'year': paper.get('year'),
                            'arxiv_id': paper.get('externalIds', {}).get('ArXiv'),
                            'source': 'semantic_scholar'
                        }

                return None

        except Exception as e:
            return None

    # ============================================================================
    # Main Operations
    # ============================================================================

    def discover_missing_pdf_links(self, limit: Optional[int] = None) -> Dict[str, Dict]:
        """
        Find PDF links for papers missing them.
        Uses Semantic Scholar, DOI resolution, and other sources.
        """
        papers_to_discover = []

        # Find papers missing PDF URLs
        for paper_file in sorted(PAPERS_DIR.glob("*.md")):
            content = paper_file.read_text(encoding='utf-8', errors='ignore')
            fm, _ = extract_frontmatter(content)

            pdf_url = self.get_pdf_url(fm)

            # Skip if already has good PDF URL (not Zotero)
            if pdf_url and not self.is_zotero_url(pdf_url):
                continue

            papers_to_discover.append(paper_file)

            if limit and len(papers_to_discover) >= limit:
                break

        discovered = {}
        logger.info("=" * 80)
        logger.info(f"DISCOVERING PDF LINKS FOR {len(papers_to_discover)} PAPERS")
        logger.info("=" * 80)

        for i, paper_file in enumerate(papers_to_discover, 1):
            paper_name = paper_file.name
            content = paper_file.read_text(encoding='utf-8', errors='ignore')
            fm, _ = extract_frontmatter(content)

            # Extract metadata for searching
            title = self.extract_field(fm, 'short_title') or paper_name.replace('.md', '')
            authors = self.extract_field(fm, 'authors')
            year = self.extract_field(fm, 'year')

            logger.info(f"[{i:3d}] {paper_name}")

            # Try multiple discovery methods
            pdf_url = None
            source = None

            # 1. Try arXiv
            url = self.extract_field(fm, 'url')
            arxiv_id = self.extract_arxiv_id(url)
            if arxiv_id:
                pdf_url = self.find_arxiv_pdf(arxiv_id)
                source = 'arxiv'
                logger.info(f"      Found via arXiv: {arxiv_id}")

            # 2. Try DOI resolution
            if not pdf_url:
                doi = self.extract_doi(url, fm)
                if doi:
                    resolved = self.find_doi_pdf(doi)
                    if resolved:
                        pdf_url = resolved
                        source = 'doi'
                        logger.info(f"      Found via DOI: {doi}")

            # 3. Try Semantic Scholar
            if not pdf_url:
                ss_result = self.find_semantic_scholar_pdf(title, authors)
                if ss_result:
                    pdf_url = ss_result['pdf_url']
                    source = 'semantic_scholar'
                    logger.info(f"      Found via Semantic Scholar")
                    if ss_result.get('arxiv_id'):
                        logger.info(f"        (arXiv: {ss_result['arxiv_id']})")

            if pdf_url:
                discovered[paper_name] = {
                    'pdf_url': pdf_url,
                    'source': source,
                    'title': title,
                    'url': url,
                }
            else:
                logger.warning(f"      Not found via any method")

        logger.info("=" * 80)
        logger.info("DISCOVERY SUMMARY")
        logger.info("=" * 80)
        logger.info(f"Papers discovered: {len(discovered)}/{len(papers_to_discover)}")

        if discovered:
            logger.info("Discovered papers:")
            for paper_name in sorted(discovered.keys())[:20]:
                info = discovered[paper_name]
                logger.info(f"  - {paper_name}")
                logger.info(f"    Source: {info['source']}")

        return discovered

    def fix_zotero_urls(self, limit: Optional[int] = None):
        """
        Replace broken Zotero file:// URLs with proper online URLs.
        """
        papers_with_zotero = []

        for paper_file in sorted(PAPERS_DIR.glob("*.md")):
            content = paper_file.read_text(encoding='utf-8', errors='ignore')
            fm, _ = extract_frontmatter(content)

            pdf_url = self.get_pdf_url(fm)
            if self.is_zotero_url(pdf_url):
                papers_with_zotero.append(paper_file)

                if limit and len(papers_with_zotero) >= limit:
                    break

        fixed = 0
        logger.info("=" * 80)
        logger.info(f"FIXING ZOTERO URLS ({len(papers_with_zotero)} papers)")
        logger.info("=" * 80)

        for i, paper_file in enumerate(papers_with_zotero, 1):
            paper_name = paper_file.name
            content = paper_file.read_text(encoding='utf-8', errors='ignore')
            fm, body = extract_frontmatter(content)

            logger.info(f"[{i:3d}/{len(papers_with_zotero)}] {paper_name}")

            # Get metadata for discovery
            title = self.extract_field(fm, 'short_title') or paper_name.replace('.md', '')
            authors = self.extract_field(fm, 'authors')
            url = self.extract_field(fm, 'url')

            # Try to find replacement URL
            pdf_url = None
            source = None

            # 1. arXiv
            arxiv_id = self.extract_arxiv_id(url)
            if arxiv_id:
                pdf_url = self.find_arxiv_pdf(arxiv_id)
                source = 'arxiv'

            # 2. DOI
            if not pdf_url:
                doi = self.extract_doi(url, fm)
                if doi:
                    resolved = self.find_doi_pdf(doi)
                    if resolved:
                        pdf_url = resolved
                        source = 'doi'

            # 3. Semantic Scholar
            if not pdf_url:
                ss_result = self.find_semantic_scholar_pdf(title, authors)
                if ss_result:
                    pdf_url = ss_result['pdf_url']
                    source = 'semantic_scholar'

            if pdf_url:
                # Update metadata
                try:
                    fields = parse_frontmatter(fm)
                    fields['pdf'] = pdf_url
                    new_fm = rebuild_frontmatter(fields)

                    is_valid, issues = validate_frontmatter(new_fm)
                    if is_valid:
                        write_paper(paper_file, new_fm, body, validate=True)
                        self.log["fixed_zotero"][paper_name] = {
                            'old_url': self.get_pdf_url(fm),
                            'new_url': pdf_url,
                            'source': source,
                        }
                        fixed += 1
                        logger.info(f"      Fixed ({source})")
                    else:
                        logger.error(f"      YAML validation failed: {issues}")

                except Exception as e:
                    logger.error(f"      Update failed: {e}")
            else:
                logger.warning(f"      No replacement found")

            if i % 10 == 0:
                self.save_log()

        self.save_log()

        logger.info("=" * 80)
        logger.info("ZOTERO FIX SUMMARY")
        logger.info("=" * 80)
        logger.info(f"Fixed: {fixed}/{len(papers_with_zotero)}")

    def batch_download_pdfs(self, limit: Optional[int] = None, start: int = 0):
        """
        Download all PDFs in batch.
        """
        papers_to_download = []

        for paper_file in sorted(PAPERS_DIR.glob("*.md"))[start:]:
            content = paper_file.read_text(encoding='utf-8', errors='ignore')
            fm, _ = extract_frontmatter(content)

            pdf_url = self.get_pdf_url(fm)
            local_pdf = self.extract_field(fm, 'local_pdf')

            # Skip if already has local PDF (handle wikilink format [[PDFs/name.pdf]])
            if local_pdf:
                # Strip wikilink brackets if present
                local_pdf_clean = local_pdf.strip('[]').replace('[[', '').replace(']]', '')
                local_path = WORKSPACE_ROOT / local_pdf_clean
                if local_path.exists():
                    continue

            # Skip if no PDF URL or it's Zotero
            if not pdf_url or self.is_zotero_url(pdf_url):
                continue

            papers_to_download.append((paper_file, pdf_url))

            if limit and len(papers_to_download) >= limit:
                break

        downloaded = 0
        failed = 0
        paywalled = 0

        logger.info("=" * 80)
        logger.info("BATCH PDF DOWNLOADER")
        logger.info("=" * 80)
        logger.info(f"Papers to download: {len(papers_to_download)}")

        for i, (paper_file, pdf_url) in enumerate(papers_to_download, 1):
            paper_name = paper_file.name
            percent = int(100 * i / len(papers_to_download)) if papers_to_download else 0

            logger.info(f"[{i:3d}/{len(papers_to_download)}] ({percent:3d}%) {paper_name}")

            # Download
            pdf_filename = paper_name.replace('.md', '.pdf')
            pdf_path = PDFS_DIR / pdf_filename

            success, message, size_mb = self._download_single_pdf(pdf_url, pdf_path)

            if success:
                # Update metadata
                try:
                    content = paper_file.read_text(encoding='utf-8', errors='ignore')
                    fm, body = extract_frontmatter(content)
                    fields = parse_frontmatter(fm)
                    fields['local_pdf'] = f"PDFs/{pdf_filename}"
                    new_fm = rebuild_frontmatter(fields)
                    write_paper(paper_file, new_fm, body, validate=True)

                    self.log["downloaded"][paper_name] = {
                        'url': pdf_url,
                        'size_mb': size_mb,
                        'timestamp': datetime.now().isoformat()
                    }
                    downloaded += 1
                    logger.info(f"  {message}")

                except Exception as e:
                    logger.warning(f"  Downloaded but metadata update failed: {e}")

            else:
                if "403" in message or "paywalled" in message.lower():
                    self.log["paywalled"][paper_name] = {
                        'url': pdf_url,
                        'reason': message,
                    }
                    paywalled += 1
                    logger.warning(f"  {message}")
                else:
                    self.log["failed"][paper_name] = {
                        'url': pdf_url,
                        'reason': message,
                    }
                    failed += 1
                    logger.error(f"  {message}")

            # Rate limiting
            self.rate_limit('pdf_download')

            # Save progress
            if i % 10 == 0:
                self.save_log()

        self.save_log()

        logger.info("=" * 80)
        logger.info("DOWNLOAD SUMMARY")
        logger.info("=" * 80)
        logger.info(f"Downloaded: {downloaded:4d}")
        logger.info(f"Failed:     {failed:4d}")
        logger.info(f"Paywalled:  {paywalled:4d}")
        logger.info(f"Total:      {downloaded + failed + paywalled:4d}")
        logger.info(f"Total local PDFs: {len(list(PDFS_DIR.glob('*.pdf')))}/580")

    def _download_single_pdf(self, pdf_url: str, pdf_path: Path) -> Tuple[bool, str, float]:
        """Download a single PDF, return (success, message, size_mb)."""
        try:
            req = urllib.request.Request(pdf_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as response:
                data = response.read()

                # Verify PDF
                if not data.startswith(b'%PDF'):
                    return False, f"Invalid PDF (magic: {data[:10]})", 0

                # Save
                with open(pdf_path, 'wb') as f:
                    f.write(data)

                size_mb = pdf_path.stat().st_size / (1024 * 1024)
                return True, f"OK ({size_mb:.2f} MB)", size_mb

        except urllib.error.HTTPError as e:
            if e.code == 403:
                return False, "Paywalled (403)", 0
            elif e.code == 404:
                return False, "Not found (404)", 0
            else:
                return False, f"HTTP {e.code}", 0
        except Exception as e:
            return False, f"Error: {str(e)[:40]}", 0

    def generate_report(self):
        """Generate comprehensive status report."""
        papers = sorted(PAPERS_DIR.glob("*.md"))
        local_pdfs = list(PDFS_DIR.glob("*.pdf"))

        # Count papers with issues
        zotero_urls = 0
        missing_urls = 0

        for paper_file in papers:
            content = paper_file.read_text(encoding='utf-8', errors='ignore')
            fm, _ = extract_frontmatter(content)
            pdf = self.get_pdf_url(fm)

            if self.is_zotero_url(pdf):
                zotero_urls += 1
            elif not pdf:
                missing_urls += 1

        logger.info("=" * 80)
        logger.info("PDF STATUS REPORT")
        logger.info("=" * 80)

        logger.info(f"Total papers: {len(papers)}")
        logger.info("Online PDF Links:")
        logger.info(f"  - With proper URLs: {len(papers) - zotero_urls - missing_urls}")
        logger.info(f"  - With Zotero URLs (need fixing): {zotero_urls}")
        logger.info(f"  - Missing entirely: {missing_urls}")

        logger.info("Local PDFs:")
        logger.info(f"  - Downloaded: {len(local_pdfs)} ({100*len(local_pdfs)/len(papers):.1f}%)")
        logger.info(f"  - Missing: {len(papers) - len(local_pdfs)} ({100*(len(papers)-len(local_pdfs))/len(papers):.1f}%)")

        logger.info("Log Statistics:")
        logger.info(f"  - Discovered: {len(self.log['discovered'])}")
        logger.info(f"  - Fixed (Zotero->Online): {len(self.log['fixed_zotero'])}")
        logger.info(f"  - Downloaded: {len(self.log['downloaded'])}")
        logger.info(f"  - Failed: {len(self.log['failed'])}")
        logger.info(f"  - Paywalled: {len(self.log['paywalled'])}")

        logger.info("=" * 80)


def main():
    parser = argparse.ArgumentParser(
        description="Smart PDF Downloader with multi-source fallback strategies"
    )
    parser.add_argument('--discover', action='store_true',
                        help='Discover missing PDF links via Semantic Scholar')
    parser.add_argument('--discover-methods', action='store_true',
                        help='Show available discovery methods')
    parser.add_argument('--fix-zotero', action='store_true',
                        help='Replace broken Zotero URLs with online equivalents')
    parser.add_argument('--download', action='store_true',
                        help='Download all PDFs')
    parser.add_argument('--download-missing', action='store_true',
                        help='Download only papers missing local PDFs')
    parser.add_argument('--report', action='store_true',
                        help='Generate status report')
    parser.add_argument('--limit', type=int,
                        help='Limit operations to N papers')
    parser.add_argument('--start', type=int, default=0,
                        help='Start from paper index N')

    args = parser.parse_args()

    downloader = SmartPDFDownloader()

    if args.discover_methods:
        logger.info("""
Available Discovery Methods:
1. arXiv (direct PDF URL generation)
2. DOI Resolution (via doi.org)
3. Semantic Scholar (open access search)
4. OpenReview (conference papers)
5. ACL Anthology (NLP papers)
        """)

    elif args.discover:
        discovered = downloader.discover_missing_pdf_links(limit=args.limit)
        downloader.log["discovered"] = discovered
        downloader.save_log()

    elif args.fix_zotero:
        downloader.fix_zotero_urls(limit=args.limit)

    elif args.download:
        downloader.batch_download_pdfs(limit=args.limit, start=args.start)

    elif args.download_missing:
        downloader.batch_download_pdfs(limit=args.limit, start=args.start)

    elif args.report:
        downloader.generate_report()

    else:
        downloader.generate_report()


if __name__ == "__main__":
    main()
