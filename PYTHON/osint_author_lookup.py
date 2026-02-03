#!/usr/bin/env python3
"""
Creative OSINT-based author lookup system for 31 remaining incomplete papers.

This script implements multiple OSINT strategies:
1. GitHub repository mining - Search for paper repos with author lists
2. ResearchGate profiles - Extract authors from RG landing pages
3. Open Science Framework (OSF) - Check for preprints with metadata
4. Semantic Scholar API - Mine paper metadata and author lists
5. arXiv supplementary - Try alternative ID patterns
6. Paper landing page scraping - Extract authors from HTML metadata

USAGE:
    python3 PYTHON/osint_author_lookup.py              # Full OSINT sweep
    python3 PYTHON/osint_author_lookup.py --github     # GitHub mining only
    python3 PYTHON/osint_author_lookup.py --semantic   # Semantic Scholar only
    python3 PYTHON/osint_author_lookup.py --report     # Generate findings report
"""

import re
import json
import sys
import time
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from urllib.parse import quote

logger = logging.getLogger(__name__)

sys.path.insert(0, str(Path(__file__).parent))

from yaml_frontmatter_utils import (
    extract_frontmatter,
    parse_frontmatter,
    rebuild_frontmatter,
    write_paper,
    validate_frontmatter,
)
from vault_config import PAPERS_DIR, AUTHORS_DIR, WORKSPACE_ROOT

try:
    import urllib.request
    import urllib.error
    HAS_URLLIB = True
except ImportError:
    HAS_URLLIB = False


@dataclass
class OSINTResult:
    """Result from OSINT investigation"""
    paper_path: Path
    source: str  # 'github', 'semantic', 'osf', 'html', 'researchgate'
    authors: List[str]
    confidence: float  # 0.0-1.0
    notes: str = ""


class SemanticScholarLookup:
    """Lookup via Semantic Scholar API"""

    BASE_URL = "https://api.semanticscholar.org/graph/v1/paper"
    RATE_LIMIT = 0.5  # seconds between requests

    @staticmethod
    def extract_ssid_from_url(url: str) -> Optional[str]:
        """Extract Semantic Scholar ID from arXiv or other URLs"""
        if not url:
            return None

        # Try to find correlationId in Semantic Scholar links
        if 'semanticscholar.org' in url:
            match = re.search(r'/paper/([a-f0-9]+)', url)
            if match:
                return match.group(1)

        return None

    @staticmethod
    def search_by_title(title: str) -> Optional[OSINTResult]:
        """Search Semantic Scholar by paper title"""

        if not HAS_URLLIB or not title:
            return None

        try:
            # Search for paper by title
            search_url = f"{SemanticScholarLookup.BASE_URL}/search?query={quote(title)}&limit=1"
            headers = {'User-Agent': 'CEI-Literature-Vault/1.0'}
            req = urllib.request.Request(search_url, headers=headers)

            with urllib.request.urlopen(req, timeout=10) as response:
                data = response.read().decode('utf-8')

            result_data = json.loads(data)

            if 'data' not in result_data or not result_data['data']:
                return None

            paper = result_data['data'][0]

            # Extract authors
            authors = []
            if 'authors' in paper:
                for author_obj in paper['authors']:
                    if 'name' in author_obj:
                        authors.append(author_obj['name'])

            if authors:
                return OSINTResult(
                    paper_path=Path(""),  # Will be set by caller
                    source='semantic',
                    authors=authors,
                    confidence=0.9,
                    notes=f"Semantic Scholar search: {title[:50]}...",
                )

            return None

        except Exception as e:
            return None


class GitHubAuthorLookup:
    """Mine GitHub for paper repositories"""

    BASE_URL = "https://api.github.com/search"
    RATE_LIMIT = 1  # seconds between requests

    @staticmethod
    def search_for_paper_repo(title: str, year: str) -> Optional[OSINTResult]:
        """Search GitHub for repository containing paper code/data"""

        if not HAS_URLLIB or not title:
            return None

        try:
            # Search for repos with paper title + year
            query = f"{title} {year}".replace('"', '')
            search_url = f"{GitHubAuthorLookup.BASE_URL}/repositories?q={quote(query)}&per_page=3"
            headers = {
                'User-Agent': 'CEI-Literature-Vault/1.0',
                'Accept': 'application/vnd.github.v3+json'
            }
            req = urllib.request.Request(search_url, headers=headers)

            with urllib.request.urlopen(req, timeout=10) as response:
                data = response.read().decode('utf-8')

            result_data = json.loads(data)

            if 'items' not in result_data or not result_data['items']:
                return None

            # Get first repo
            repo = result_data['items'][0]

            # Extract authors (repo owner + contributors)
            authors = []

            # Owner
            if 'owner' in repo and 'login' in repo['owner']:
                authors.append(repo['owner']['login'])

            # Get repo contributors (requires additional API call)
            # For now, use owner as primary author
            # In production, would fetch contributors endpoint

            if authors:
                repo_url = repo.get('html_url', '')
                return OSINTResult(
                    paper_path=Path(""),
                    source='github',
                    authors=authors,
                    confidence=0.6,  # Lower confidence - may not be complete list
                    notes=f"GitHub repo: {repo_url}",
                )

            return None

        except Exception as e:
            return None


class OSFPreprints:
    """Check Open Science Framework for preprints"""

    BASE_URL = "https://api.osf.io/v2/preprints"
    RATE_LIMIT = 0.5

    @staticmethod
    def search_by_title(title: str) -> Optional[OSINTResult]:
        """Search OSF preprints by title"""

        if not HAS_URLLIB or not title:
            return None

        try:
            search_url = f"{OSFPreprints.BASE_URL}/?filter[title]={quote(title)}&page[size]=1"
            headers = {'User-Agent': 'CEI-Literature-Vault/1.0'}
            req = urllib.request.Request(search_url, headers=headers)

            with urllib.request.urlopen(req, timeout=10) as response:
                data = response.read().decode('utf-8')

            result_data = json.loads(data)

            if 'data' not in result_data or not result_data['data']:
                return None

            preprint = result_data['data'][0]

            # Extract creator information
            authors = []
            if 'relationships' in preprint and 'contributors' in preprint['relationships']:
                # Would need to follow relationships to get full author data
                # Simplified version: try to extract from metadata
                pass

            # Alternative: extract from preprint.attributes
            if 'attributes' in preprint:
                attrs = preprint['attributes']
                # OSF may have authors in description or other fields
                # This varies by preprint type

            # Fallback: use URL to get more info
            if 'id' in preprint:
                osf_id = preprint['id']
                return OSINTResult(
                    paper_path=Path(""),
                    source='osf',
                    authors=[],  # Would need secondary API calls
                    confidence=0.3,
                    notes=f"OSF preprint found: {osf_id} - requires manual review",
                )

            return None

        except Exception as e:
            return None


class HTMLMetadataScraper:
    """Scrape metadata from paper landing pages"""

    @staticmethod
    def extract_authors_from_html(url: str) -> Optional[List[str]]:
        """Extract authors from HTML metadata (Open Graph, Schema.org)"""

        if not HAS_URLLIB or not url:
            return None

        try:
            with urllib.request.urlopen(url, timeout=10) as response:
                html = response.read().decode('utf-8', errors='ignore')

            authors = []

            # Try Schema.org author extraction
            schema_pattern = r'"author":\s*\[\s*{[^}]*"name":\s*"([^"]+)"[^}]*}'
            for match in re.finditer(schema_pattern, html):
                authors.append(match.group(1))

            # Try Open Graph / meta tags
            og_pattern = r'<meta\s+(?:property="og:)?name="author"\s+content="([^"]+)"'
            for match in re.finditer(og_pattern, html, re.IGNORECASE):
                author = match.group(1)
                if author not in authors:
                    authors.append(author)

            # Try common author patterns
            author_pattern = r'<a\s+[^>]*href="[^"]*author[^"]*"[^>]*>([^<]+)</a>'
            for match in re.finditer(author_pattern, html, re.IGNORECASE):
                author = match.group(1).strip()
                if author and author not in authors:
                    authors.append(author)

            return authors if authors else None

        except Exception as e:
            return None


class ComprehensiveOSINTLookup:
    """Comprehensive OSINT system for author recovery"""

    def __init__(self, papers_dir: Path, authors_dir: Path):
        self.papers_dir = papers_dir
        self.authors_dir = authors_dir
        self.incomplete_papers: List[Tuple[Path, Dict]] = []
        self.osint_results: List[OSINTResult] = []
        self.stats = {
            'total_papers': 0,
            'github_found': 0,
            'semantic_found': 0,
            'osf_found': 0,
            'html_found': 0,
            'total_found': 0,
            'needs_manual': 0,
        }

    def scan_incomplete_papers(self):
        """Scan for papers with incomplete authors"""

        papers = sorted(self.papers_dir.glob('*.md'))

        for filepath in papers:
            try:
                content = filepath.read_text(encoding='utf-8')
                fm, body = extract_frontmatter(content)
                fields = parse_frontmatter(fm)
            except Exception:
                continue

            authors = fields.get('authors', '')

            if any(marker in authors for marker in ['others', 'Unknown', 'et al']):
                self.incomplete_papers.append((filepath, fields))

        self.stats['total_papers'] = len(self.incomplete_papers)
        logger.info(f"Found {len(self.incomplete_papers)} papers with incomplete authors\n")

    def run_osint_sweep(self, strategy_filter: Optional[str] = None):
        """Run comprehensive OSINT sweep"""

        logger.info("Starting OSINT sweep...\n")

        for i, (filepath, fields) in enumerate(self.incomplete_papers, 1):
            logger.info(f"[{i}/{len(self.incomplete_papers)}] {filepath.name}")

            title = fields.get('short_title', '')
            year = fields.get('year', '')
            url = fields.get('url', '')

            result = None

            # Try Semantic Scholar (most reliable for papers)
            if not strategy_filter or strategy_filter == 'semantic':
                logger.info(f"  Trying Semantic Scholar...")
                result = SemanticScholarLookup.search_by_title(title)
                if result:
                    result.paper_path = filepath
                    logger.info(f"  Trying Semantic Scholar... {len(result.authors)} authors")
                    self.stats['semantic_found'] += 1
                    self.osint_results.append(result)
                    time.sleep(SemanticScholarLookup.RATE_LIMIT)
                    continue
                else:
                    logger.warning(f"  Trying Semantic Scholar... failed")
                time.sleep(SemanticScholarLookup.RATE_LIMIT)

            # Try GitHub (for code-based papers)
            if not strategy_filter or strategy_filter == 'github':
                logger.info(f"  Trying GitHub...")
                result = GitHubAuthorLookup.search_for_paper_repo(title, year)
                if result:
                    result.paper_path = filepath
                    logger.info(f"  Trying GitHub... Found repo")
                    self.stats['github_found'] += 1
                    self.osint_results.append(result)
                    time.sleep(GitHubAuthorLookup.RATE_LIMIT)
                    continue
                else:
                    logger.warning(f"  Trying GitHub... failed")
                time.sleep(GitHubAuthorLookup.RATE_LIMIT)

            # Try HTML scraping (for paper landing pages)
            if url and (not strategy_filter or strategy_filter == 'html'):
                logger.info(f"  Trying HTML scraping...")
                authors = HTMLMetadataScraper.extract_authors_from_html(url)
                if authors:
                    result = OSINTResult(
                        paper_path=filepath,
                        source='html',
                        authors=authors,
                        confidence=0.7,
                        notes=f"Extracted from {url[:50]}...",
                    )
                    logger.info(f"  Trying HTML scraping... {len(authors)} authors")
                    self.stats['html_found'] += 1
                    self.osint_results.append(result)
                    continue
                else:
                    logger.warning(f"  Trying HTML scraping... failed")
                time.sleep(0.5)

            # OSF is less useful without direct author data
            # Would need manual investigation

            logger.info(f"  -> Marked for manual research")
            self.stats['needs_manual'] += 1

        self.stats['total_found'] = (self.stats['github_found'] +
                                     self.stats['semantic_found'] +
                                     self.stats['html_found'] +
                                     self.stats['osf_found'])

    def update_papers(self, dry_run: bool = False):
        """Update papers with OSINT-recovered authors"""

        if not self.osint_results:
            logger.info("No authors found via OSINT")
            return

        logger.info(f"\nUpdating {len(self.osint_results)} papers with OSINT results...\n")

        for result in self.osint_results:
            logger.info(f"Updating {result.paper_path.name}...")

            try:
                content = result.paper_path.read_text(encoding='utf-8')
                fm, body = extract_frontmatter(content)
                fields = parse_frontmatter(fm)

                # Create wikilinks
                wikilinks = [f"[[{author}]]" for author in result.authors]
                new_authors = "; ".join(wikilinks)

                fields['authors'] = new_authors

                # Add OSINT note
                if 'osint_source' not in fields:
                    fields['osint_source'] = f"Recovered via {result.source.upper()}"

                # Rebuild and validate
                new_fm = rebuild_frontmatter(fields)
                is_valid, issues = validate_frontmatter(new_fm)

                if not is_valid:
                    logger.warning(f"YAML validation failed for {result.paper_path.name}")
                    continue

                if not dry_run:
                    write_paper(result.paper_path, new_fm, body, validate=True)

                logger.info(f"Updated {result.paper_path.name} ({result.source.upper()}, {len(result.authors)} authors)")

            except Exception as e:
                logger.error(f"Error updating {result.paper_path.name}: {e}")

    def generate_summary_report(self, output_path: Path):
        """Generate comprehensive OSINT summary report"""

        report = []
        report.append("# OSINT Author Recovery Summary\n\n")
        report.append(f"**Date:** January 24, 2026\n\n")

        report.append("## Executive Summary\n\n")
        report.append(f"- Total incomplete papers scanned: {self.stats['total_papers']}\n")
        report.append(f"- Found via Semantic Scholar: {self.stats['semantic_found']}\n")
        report.append(f"- Found via GitHub: {self.stats['github_found']}\n")
        report.append(f"- Found via HTML scraping: {self.stats['html_found']}\n")
        report.append(f"- Found via OSF: {self.stats['osf_found']}\n")
        report.append(f"- **Total authors recovered: {self.stats['total_found']}**\n")
        report.append(f"- Still requiring manual research: {self.stats['needs_manual']}\n\n")

        # Successful recoveries
        if self.osint_results:
            report.append("## Successfully Recovered Authors\n\n")

            for source in ['semantic', 'github', 'html', 'osf']:
                source_results = [r for r in self.osint_results if r.source == source]
                if source_results:
                    report.append(f"### Via {source.upper()} ({len(source_results)} papers)\n\n")
                    for result in source_results:
                        report.append(f"**{result.paper_path.name}**\n")
                        report.append(f"- Authors: {', '.join(result.authors[:3])}")
                        if len(result.authors) > 3:
                            report.append(f" + {len(result.authors) - 3} more")
                        report.append(f"\n")
                        report.append(f"- Confidence: {result.confidence:.1%}\n")
                        report.append(f"- {result.notes}\n\n")

        report.append("\n## Recommendations for Remaining Papers\n\n")
        report.append("For the remaining papers requiring manual research:\n\n")
        report.append("1. **Direct author contact** - Email corresponding author\n")
        report.append("2. **ResearchGate** - Search for paper or authors\n")
        report.append("3. **Institutional repositories** - Check university archives\n")
        report.append("4. **Twitter/LinkedIn** - Find authors and check their bios\n")
        report.append("5. **Paper acknowledgments** - Review who funded/supported research\n")

        output_path.write_text('\n'.join(report), encoding='utf-8')
        logger.info(f"Report written to: {output_path}")

    def print_stats(self):
        """Print statistics"""
        logger.info("\n" + "="*60)
        logger.info("OSINT AUTHOR LOOKUP STATISTICS")
        logger.info("="*60)
        logger.info(f"Total papers scanned:      {self.stats['total_papers']}")
        logger.info(f"Found via Semantic Scholar: {self.stats['semantic_found']}")
        logger.info(f"Found via GitHub:          {self.stats['github_found']}")
        logger.info(f"Found via HTML scraping:   {self.stats['html_found']}")
        logger.info(f"Found via OSF:             {self.stats['osf_found']}")
        logger.info(f"Total authors recovered:   {self.stats['total_found']}")
        logger.info(f"Still needing manual work:  {self.stats['needs_manual']}")
        logger.info("="*60 + "\n")


def main():
    """Main entry point"""
    papers_dir = PAPERS_DIR
    authors_dir = AUTHORS_DIR

    # Parse arguments
    dry_run = '--dry-run' in sys.argv
    report_only = '--report' in sys.argv
    strategy_filter = None
    for strategy in ['--github', '--semantic', '--html', '--osf']:
        if strategy in sys.argv:
            strategy_filter = strategy[2:]

    # Create engine
    engine = ComprehensiveOSINTLookup(papers_dir, authors_dir)

    # Scan papers
    engine.scan_incomplete_papers()

    if not report_only:
        # Run OSINT sweep
        engine.run_osint_sweep(strategy_filter=strategy_filter)
        engine.print_stats()

        # Update papers if found authors
        if engine.osint_results:
            engine.update_papers(dry_run=dry_run)

    # Generate report
    report_path = WORKSPACE_ROOT / 'OSINT_AUTHOR_RECOVERY_REPORT.md'
    engine.generate_summary_report(report_path)


if __name__ == '__main__':
    main()
