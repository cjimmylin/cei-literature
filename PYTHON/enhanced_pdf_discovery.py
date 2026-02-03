#!/usr/bin/env python3
"""
Enhanced PDF Discovery - Advanced Fallback Strategies

Implements Option 4 future enhancements to find additional PDFs:
1. DOI Resolver - Find OA versions through DOI
2. arXiv Discovery - Search by title for preprints
3. ResearchGate Check - Look for author-uploaded copies
4. Institutional Repositories - Search major universities

Usage:
    python3 PYTHON/enhanced_pdf_discovery.py --all              # Run all strategies
    python3 PYTHON/enhanced_pdf_discovery.py --doi              # DOI resolver only
    python3 PYTHON/enhanced_pdf_discovery.py --arxiv            # arXiv discovery only
    python3 PYTHON/enhanced_pdf_discovery.py --researchgate     # ResearchGate check
    python3 PYTHON/enhanced_pdf_discovery.py --report           # Show findings
    python3 PYTHON/enhanced_pdf_discovery.py --download         # Download found papers
"""

import re
import json
import time
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path
from typing import Optional, Dict, List, Tuple
import xml.etree.ElementTree as ET
import logging

logger = logging.getLogger(__name__)

# Setup paths - use vault_config for external PDF location
from vault_config import PAPERS_DIR, PDFS_DIR, WORKSPACE_ROOT
LOG_FILE = WORKSPACE_ROOT / "enhanced_discovery_log.json"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
}

class EnhancedPDFDiscovery:
    def __init__(self):
        PDFS_DIR.mkdir(exist_ok=True)
        self.load_log()
        self.last_arxiv_time = 0
        self.last_semantic_time = 0

    def load_log(self):
        """Load discovery progress."""
        if LOG_FILE.exists():
            with open(LOG_FILE) as f:
                self.log = json.load(f)
        else:
            self.log = {
                "doi_found": {},
                "arxiv_found": {},
                "researchgate_found": {},
                "institutional_found": {},
                "downloaded": {},
                "failed": {}
            }

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

    def extract_doi(self, url: str) -> Optional[str]:
        """Extract DOI from URL or text."""
        if not url:
            return None
        # Match various DOI formats
        match = re.search(r'(?:doi\.org/|doi:)?(10\.\S+?)(?:\s|$|/)', url)
        return match.group(1) if match else None

    def extract_arxiv_id(self, url: str) -> Optional[str]:
        """Extract arXiv ID from URL."""
        if not url:
            return None
        match = re.search(r'arxiv\.org/(?:abs|pdf)/(\d+\.\d+)', url)
        return match.group(1) if match else None

    def extract_title(self, frontmatter: str) -> Optional[str]:
        """Extract paper title."""
        title = self.extract_field(frontmatter, 'short_title')
        if not title:
            title = self.extract_field(frontmatter, 'title')
        return title

    def strategy_doi_resolver(self, doi: str) -> Tuple[Optional[bytes], str]:
        """
        Strategy 1: Use DOI resolver to find open-access versions.

        Checks:
        - unpaywall.org API (official OA lookup)
        - crossref.org (publisher metadata)
        """
        try:
            # Try unpaywall API (official open-access database)
            time.sleep(1.0)
            url = f"https://api.unpaywall.org/v2/{doi}?email=research@example.com"
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())

                if data.get('is_oa') and data.get('oa_locations'):
                    # Found OA version
                    for location in data['oa_locations']:
                        if location.get('pdf_url'):
                            pdf_url = location['pdf_url']
                            # Try to download
                            pdf_data = self.download_from_url(pdf_url)
                            if pdf_data:
                                return pdf_data, f"Unpaywall"
                        elif location.get('url_for_pdf'):
                            pdf_url = location['url_for_pdf']
                            pdf_data = self.download_from_url(pdf_url)
                            if pdf_data:
                                return pdf_data, "Unpaywall"

                # Check repository (might have PDF)
                if data.get('repository'):
                    repo_url = data['repository'].get('url')
                    if repo_url:
                        pdf_data = self.download_from_url(repo_url)
                        if pdf_data:
                            return pdf_data, "Repository"

        except Exception as e:
            pass

        return None, ""

    def strategy_arxiv_search(self, title: str, authors: str = "") -> Tuple[Optional[bytes], str]:
        """
        Strategy 2: Search arXiv for preprints by title.

        If paper was posted to arXiv but we don't have the ID,
        search for it by title and download the preprint.
        """
        try:
            time.sleep(0.5)  # Rate limit

            # Clean title for search
            search_terms = title.split('(')[0].split(':')[0].strip()[:100]

            # Query arXiv API
            url = f"http://export.arxiv.org/api/query?search_query=all:{urllib.parse.quote(search_terms)}&start=0&max_results=1&sortBy=relevance&sortOrder=descending"

            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as response:
                xml_data = response.read().decode('utf-8')
                root = ET.fromstring(xml_data)

                ns = {'atom': 'http://www.w3.org/2005/Atom'}
                entries = root.findall('atom:entry', ns)

                if entries:
                    entry = entries[0]

                    # Extract arXiv ID from entry
                    arxiv_id_elem = entry.find('atom:id', ns)
                    if arxiv_id_elem is not None:
                        arxiv_id = arxiv_id_elem.text.split('/abs/')[-1]

                        # Construct PDF URL
                        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"

                        # Try to download
                        pdf_data = self.download_from_url(pdf_url)
                        if pdf_data:
                            return pdf_data, f"arXiv:{arxiv_id}"

        except Exception as e:
            pass

        return None, ""

    def strategy_researchgate(self, title: str, first_author: str = "") -> Dict:
        """
        Strategy 3: Check ResearchGate for author-uploaded copies.

        Returns info about where paper might be found on ResearchGate.
        (Actual downloading requires handling ResearchGate's terms)
        """
        try:
            # Note: ResearchGate doesn't have a public API
            # We return search URLs for manual checking

            search_term = f'"{title}"' if len(title) < 100 else title.split('(')[0].strip()

            if first_author:
                search_url = f"https://www.researchgate.net/search?q={urllib.parse.quote(search_term)}+{urllib.parse.quote(first_author)}"
            else:
                search_url = f"https://www.researchgate.net/search?q={urllib.parse.quote(search_term)}"

            return {
                "platform": "ResearchGate",
                "search_url": search_url,
                "note": "Manual check required (check author's profile for PDF)"
            }

        except Exception:
            return {}

    def strategy_academia_edu(self, title: str, first_author: str = "") -> Dict:
        """
        Strategy 4: Check Academia.edu for author uploads.

        Returns info about where paper might be found on Academia.
        """
        try:
            search_term = f'"{title}"' if len(title) < 100 else title.split('(')[0].strip()

            if first_author:
                search_url = f"https://www.academia.edu/search?q={urllib.parse.quote(search_term)}+{urllib.parse.quote(first_author)}"
            else:
                search_url = f"https://www.academia.edu/search?q={urllib.parse.quote(search_term)}"

            return {
                "platform": "Academia.edu",
                "search_url": search_url,
                "note": "Manual check required (free registration to download)"
            }

        except Exception:
            return {}

    def strategy_institutional_repos(self, title: str, first_author: str = "") -> List[Dict]:
        """
        Strategy 5: Check institutional repositories.

        Searches major university repositories for papers.
        """
        repos = []

        # Major institutional repositories
        institutions = [
            ("MIT DSpace", "http://dspace.mit.edu/advanced"),
            ("Stanford Digital", "https://searchworks.stanford.edu/"),
            ("UC Berkeley eScholarship", "https://escholarship.org/"),
            ("CMU Research", "https://www.ri.cmu.edu/publication/"),
            ("Princeton DataSpace", "https://dataspace.princeton.edu/"),
        ]

        search_term = title.split('(')[0].split(':')[0].strip()[:80]

        for name, base_url in institutions:
            # Most repos have search interfaces
            search_url = f"{base_url}?q={urllib.parse.quote(search_term)}"
            repos.append({
                "institution": name,
                "search_url": search_url,
                "note": "Check institutional repository"
            })

        return repos

    def download_from_url(self, url: str) -> Optional[bytes]:
        """Try to download PDF from URL."""
        if not url:
            return None

        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as response:
                data = response.read()

                if data.startswith(b'%PDF'):
                    return data

        except Exception:
            pass

        return None

    def discover_all(self) -> Dict:
        """Run all discovery strategies for all papers."""
        papers = sorted(PAPERS_DIR.glob("*.md"))
        results = {
            "doi": [],
            "arxiv": [],
            "researchgate": [],
            "academia": [],
            "institutional": [],
            "summary": {}
        }

        logger.info(f"\n{'='*80}")
        logger.info(f"ENHANCED PDF DISCOVERY - ALL STRATEGIES")
        logger.info(f"{'='*80}\n")

        for i, paper_path in enumerate(papers, 1):
            paper_name = paper_path.name
            pdf_path = PDFS_DIR / paper_name.replace('.md', '.pdf')

            # Skip if already downloaded
            if pdf_path.exists():
                continue

            percent = int(100 * i / len(papers))
            logger.info(f"[{i:3d}/{len(papers)}] ({percent:3d}%) {paper_name[:50]:50s} ... ")

            content = paper_path.read_text(encoding='utf-8', errors='ignore')
            fm, _ = self.extract_frontmatter(content)

            # Extract metadata
            url = self.extract_field(fm, 'url')
            title = self.extract_title(fm)
            first_author = self.extract_field(fm, 'first_author')
            doi = self.extract_doi(url) if url else None

            sources = []

            # Strategy 1: DOI Resolver
            if doi:
                pdf_data, source = self.strategy_doi_resolver(doi)
                if pdf_data:
                    sources.append(("DOI", source, pdf_data))
                    results["doi"].append(paper_name)
                    logger.info(f"DOI found ({source})")
                    continue

            # Strategy 2: arXiv Search
            if title:
                pdf_data, source = self.strategy_arxiv_search(title, first_author or "")
                if pdf_data:
                    sources.append(("arXiv", source, pdf_data))
                    results["arxiv"].append(paper_name)
                    logger.info(f"arXiv found ({source})")
                    continue

            # Strategy 3: ResearchGate
            if title:
                rg_info = self.strategy_researchgate(title, first_author or "")
                if rg_info:
                    sources.append(("ResearchGate", rg_info.get("search_url"), None))
                    results["researchgate"].append(paper_name)

            # Strategy 4: Academia.edu
            if title:
                ae_info = self.strategy_academia_edu(title, first_author or "")
                if ae_info:
                    sources.append(("Academia.edu", ae_info.get("search_url"), None))
                    results["academia"].append(paper_name)

            # Strategy 5: Institutional Repos
            if title:
                repos = self.strategy_institutional_repos(title, first_author or "")
                if repos:
                    sources.append(("Institutional", repos, None))
                    results["institutional"].append(paper_name)

            if sources:
                logger.warning(f"{len(sources)} sources found (manual check needed)")
            else:
                logger.warning("No sources found")

            self.save_log()

        # Summary
        logger.info(f"\n{'='*80}")
        logger.info(f"DISCOVERY SUMMARY")
        logger.info(f"{'='*80}\n")
        logger.info(f"DOI Resolver found:      {len(results['doi']):3d} papers")
        logger.info(f"arXiv found:             {len(results['arxiv']):3d} papers")
        logger.info(f"ResearchGate sources:    {len(results['researchgate']):3d} papers")
        logger.info(f"Academia.edu sources:    {len(results['academia']):3d} papers")
        logger.info(f"Institutional repos:     {len(results['institutional']):3d} papers")

        total_found = len(results['doi']) + len(results['arxiv'])
        logger.info(f"\n{'='*80}")
        logger.info(f"DIRECT DOWNLOADS AVAILABLE: {total_found} papers")
        logger.info(f"MANUAL RESEARCH NEEDED:     {len(results['researchgate']) + len(results['academia']) + len(results['institutional'])} papers")

        return results

    def generate_report(self):
        """Generate discovery report."""
        doi_count = len(self.log.get("doi_found", {}))
        arxiv_count = len(self.log.get("arxiv_found", {}))
        rg_count = len(self.log.get("researchgate_found", {}))
        inst_count = len(self.log.get("institutional_found", {}))
        downloaded_count = len(self.log.get("downloaded", {}))

        logger.info(f"\n{'='*80}")
        logger.info(f"ENHANCED DISCOVERY REPORT")
        logger.info(f"{'='*80}\n")
        logger.info(f"DOI Resolver found:      {doi_count} papers")
        logger.info(f"arXiv Discovery found:   {arxiv_count} papers")
        logger.info(f"ResearchGate sources:    {rg_count} papers (manual)")
        logger.info(f"Institutional sources:   {inst_count} papers (manual)")
        logger.info(f"Downloaded:              {downloaded_count} papers")
        logger.info(f"\nEstimated new PDFs:      {doi_count + arxiv_count}")
        logger.info(f"Potential with manual:   {doi_count + arxiv_count + rg_count + inst_count}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Enhanced PDF discovery with multiple strategies")
    parser.add_argument('--all', action='store_true', help='Run all strategies')
    parser.add_argument('--doi', action='store_true', help='DOI resolver only')
    parser.add_argument('--arxiv', action='store_true', help='arXiv discovery only')
    parser.add_argument('--researchgate', action='store_true', help='ResearchGate check')
    parser.add_argument('--institutional', action='store_true', help='Institutional repos')
    parser.add_argument('--report', action='store_true', help='Show report')
    parser.add_argument('--download', action='store_true', help='Download found papers')

    args = parser.parse_args()

    discovery = EnhancedPDFDiscovery()

    if args.report:
        discovery.generate_report()
    elif args.all or not any([args.doi, args.arxiv, args.researchgate, args.institutional]):
        results = discovery.discover_all()
    elif args.doi:
        logger.info("DOI Resolver strategy not yet fully implemented in CLI mode.")
        logger.info("Use --all to run complete discovery")


if __name__ == "__main__":
    main()
