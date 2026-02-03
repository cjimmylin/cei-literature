#!/usr/bin/env python3
"""
Smart multi-source author lookup with fallback to search queries for manual research.

Strategy:
1. Use arXiv API (most reliable for CS papers)
2. Use CrossRef API for DOI-based papers
3. Generate search queries for manual research
4. Create a comprehensive report

USAGE:
    python3 PYTHON/smart_author_lookup.py              # Full run
    python3 PYTHON/smart_author_lookup.py --arxiv-only # Only arXiv papers
    python3 PYTHON/smart_author_lookup.py --report     # Generate report only
"""

import re
import json
import logging
import sys
import time
from pathlib import Path
from typing import List, Optional, Tuple
from urllib.parse import quote
from dataclasses import dataclass
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)

sys.path.insert(0, str(Path(__file__).parent.parent))

from PYTHON.yaml_frontmatter_utils import (
    extract_frontmatter,
    parse_frontmatter,
    rebuild_frontmatter,
    write_paper,
    validate_frontmatter,
)
from PYTHON.vault_config import PAPERS_DIR, AUTHORS_DIR, WORKSPACE_ROOT

# Try to import urllib
try:
    import urllib.request
    import urllib.error
    HAS_URLLIB = True
except ImportError:
    HAS_URLLIB = False


@dataclass
class PaperForLookup:
    """Paper with incomplete authors that needs research"""
    filepath: Path
    title: str
    year: str
    arxiv_id: Optional[str]
    doi: Optional[str]
    url: str
    current_authors: str


@dataclass
class AuthorLookupResult:
    """Result from author lookup"""
    paper_path: Path
    source: str  # 'arxiv', 'crossref', 'manual'
    authors: List[str]
    confidence: float
    notes: str = ""


class SmartAuthorLookup:
    """Smart author lookup system"""

    def __init__(self, papers_dir: Path, authors_dir: Path):
        self.papers_dir = papers_dir
        self.authors_dir = authors_dir
        self.incomplete_papers: List[PaperForLookup] = []
        self.results: List[AuthorLookupResult] = []
        self.stats = {
            'total_incomplete': 0,
            'found_arxiv': 0,
            'found_crossref': 0,
            'found_total': 0,
            'needs_manual_research': 0,
        }

    def scan_incomplete_papers(self):
        """Scan vault for papers with incomplete authors"""

        papers = sorted(self.papers_dir.glob('*.md'))

        for filepath in papers:
            try:
                content = filepath.read_text(encoding='utf-8')
                fm, body = extract_frontmatter(content)
                fields = parse_frontmatter(fm)
            except Exception:
                continue

            authors = fields.get('authors', '')

            # Check if incomplete
            if any(marker in authors for marker in ['others', 'Unknown', 'et al']):
                paper = PaperForLookup(
                    filepath=filepath,
                    title=fields.get('short_title', ''),
                    year=fields.get('year', ''),
                    arxiv_id=self._extract_arxiv_id(fields.get('url', '')),
                    doi=fields.get('doi', ''),
                    url=fields.get('url', ''),
                    current_authors=authors,
                )
                self.incomplete_papers.append(paper)

        self.stats['total_incomplete'] = len(self.incomplete_papers)
        logger.info(f"Found {len(self.incomplete_papers)} papers with incomplete authors")

    def lookup_all(self, arxiv_only: bool = False):
        """Look up all papers"""

        logger.info("Looking up author information...")

        for i, paper in enumerate(self.incomplete_papers, 1):
            logger.info(f"[{i}/{len(self.incomplete_papers)}] {paper.filepath.name}")

            result = None

            # Try arXiv first
            if paper.arxiv_id:
                logger.debug(f"  Trying arXiv ({paper.arxiv_id})...")
                result = self._lookup_arxiv(paper)
                if result:
                    logger.info(f"  arXiv ({paper.arxiv_id}): found {len(result.authors)} authors")
                    self.stats['found_arxiv'] += 1
                    self.results.append(result)
                    time.sleep(0.5)  # Rate limit
                    continue
                else:
                    logger.warning(f"  arXiv ({paper.arxiv_id}): not found")
                time.sleep(0.5)

            if arxiv_only:
                continue

            # Try CrossRef
            if paper.doi:
                logger.debug(f"  Trying CrossRef ({paper.doi})...")
                result = self._lookup_crossref(paper)
                if result:
                    logger.info(f"  CrossRef ({paper.doi}): found {len(result.authors)} authors")
                    self.stats['found_crossref'] += 1
                    self.results.append(result)
                    time.sleep(0.5)  # Rate limit
                    continue
                else:
                    logger.warning(f"  CrossRef ({paper.doi}): not found")
                time.sleep(0.5)

            # Mark for manual research
            logger.info(f"  Needs manual research")
            self.stats['needs_manual_research'] += 1

        self.stats['found_total'] = self.stats['found_arxiv'] + self.stats['found_crossref']

    def _lookup_arxiv(self, paper: PaperForLookup) -> Optional[AuthorLookupResult]:
        """Look up authors from arXiv"""

        if not paper.arxiv_id or not HAS_URLLIB:
            return None

        try:
            url = f"http://export.arxiv.org/api/query?search_query=arXiv:{paper.arxiv_id}&start=0&max_results=1"
            with urllib.request.urlopen(url, timeout=10) as response:
                data = response.read().decode('utf-8')

            root = ET.fromstring(data)
            entries = root.findall('{http://www.w3.org/2005/Atom}entry')

            if not entries:
                return None

            authors = []
            for author in entries[0].findall('{http://www.w3.org/2005/Atom}author'):
                name_elem = author.find('{http://www.w3.org/2005/Atom}name')
                if name_elem is not None and name_elem.text:
                    authors.append(name_elem.text.strip())

            if authors:
                return AuthorLookupResult(
                    paper_path=paper.filepath,
                    source='arxiv',
                    authors=authors,
                    confidence=1.0,
                    notes=f"ArXiv ID: {paper.arxiv_id}",
                )

            return None

        except Exception as e:
            return None

    def _lookup_crossref(self, paper: PaperForLookup) -> Optional[AuthorLookupResult]:
        """Look up authors from CrossRef"""

        if not paper.doi or not HAS_URLLIB:
            return None

        try:
            url = f"https://api.crossref.org/works/{paper.doi}"
            headers = {'User-Agent': 'CEI-Literature-Vault/1.0'}
            req = urllib.request.Request(url, headers=headers)

            with urllib.request.urlopen(req, timeout=10) as response:
                data = response.read().decode('utf-8')

            result_data = json.loads(data)

            if 'message' not in result_data:
                return None

            authors = []
            msg = result_data['message']

            if 'author' in msg:
                for author_obj in msg['author']:
                    name_parts = []
                    if 'family' in author_obj:
                        name_parts.append(author_obj['family'])
                    if 'given' in author_obj:
                        name_parts.append(author_obj['given'])

                    if name_parts:
                        if len(name_parts) == 2:
                            authors.append(f"{name_parts[0]}, {name_parts[1]}")
                        else:
                            authors.append(name_parts[0])

            if authors:
                return AuthorLookupResult(
                    paper_path=paper.filepath,
                    source='crossref',
                    authors=authors,
                    confidence=1.0,
                    notes=f"DOI: {paper.doi}",
                )

            return None

        except Exception as e:
            return None

    @staticmethod
    def _extract_arxiv_id(url: str) -> Optional[str]:
        """Extract arXiv ID from URL"""
        if not url:
            return None

        patterns = [
            r'arxiv\.org/abs/(\d{4}\.\d{5})',
            r'arxiv\.org/pdf/(\d{4}\.\d{5})',
            r'(\d{4}\.\d{5})',
        ]

        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)

        return None

    def update_papers(self, dry_run: bool = False):
        """Update papers with found authors"""

        if not self.results:
            logger.info("No authors found to update")
            return

        logger.info(f"Updating {len(self.results)} papers with found authors...")

        for result in self.results:
            logger.debug(f"Updating {result.paper_path.name}...")

            try:
                content = result.paper_path.read_text(encoding='utf-8')
                fm, body = extract_frontmatter(content)
                fields = parse_frontmatter(fm)

                # Create wikilinks
                wikilinks = [f"[[{author}]]" for author in result.authors]
                new_authors = "; ".join(wikilinks)

                fields['authors'] = new_authors

                # Rebuild and validate
                new_fm = rebuild_frontmatter(fields)
                is_valid, issues = validate_frontmatter(new_fm)

                if not is_valid:
                    logger.error(f"YAML validation failed for {result.paper_path.name}")
                    continue

                if not dry_run:
                    write_paper(result.paper_path, new_fm, body, validate=True)

                logger.info(f"Updated {result.paper_path.name} ({result.source}, {len(result.authors)} authors)")

            except Exception as e:
                logger.error(f"Error updating {result.paper_path.name}: {e}")

    def generate_research_report(self, output_path: Path):
        """Generate a report of findings and papers needing manual research"""

        report = []
        report.append("# Author Lookup Results & Research Tasks\n")
        report.append(f"**Generated:** 2026-01-24\n")
        report.append(f"**Total incomplete papers:** {self.stats['total_incomplete']}\n")
        report.append(f"**Found via arXiv:** {self.stats['found_arxiv']}\n")
        report.append(f"**Found via CrossRef:** {self.stats['found_crossref']}\n")
        report.append(f"**Found total:** {self.stats['found_total']}\n")
        report.append(f"**Needs manual research:** {self.stats['needs_manual_research']}\n\n")

        # Section 1: Successfully found authors
        report.append("## ✓ Papers with Authors Found\n\n")

        for source in ['arxiv', 'crossref']:
            source_results = [r for r in self.results if r.source == source]
            if source_results:
                report.append(f"### Via {source.upper()} ({len(source_results)} papers)\n\n")
                for result in source_results:
                    report.append(f"**{result.paper_path.stem}**\n")
                    report.append(f"- Authors found: {len(result.authors)}\n")
                    for author in result.authors[:3]:
                        report.append(f"  - {author}\n")
                    if len(result.authors) > 3:
                        report.append(f"  - ... and {len(result.authors) - 3} more\n")
                    report.append(f"- {result.notes}\n\n")

        # Section 2: Papers needing manual research
        report.append("\n## 🔍 Papers Needing Manual Research\n\n")

        manual_papers = [p for p in self.incomplete_papers
                        if not any(r.paper_path == p.filepath for r in self.results)]

        for paper in manual_papers:
            report.append(f"### {paper.filepath.stem}\n\n")
            report.append(f"- **Title:** {paper.title}\n")
            report.append(f"- **Year:** {paper.year}\n")
            report.append(f"- **Current authors:** {paper.current_authors[:60]}...\n")

            # Generate search queries
            queries = self._generate_search_queries(paper)

            if queries:
                report.append(f"\n**Search queries to try:**\n")
                for service, query in queries:
                    report.append(f"- **{service}:** {query}\n")

            report.append("\n")

        # Write report
        output_path.write_text('\n'.join(report), encoding='utf-8')
        logger.info(f"Report written to: {output_path}")

    @staticmethod
    def _generate_search_queries(paper: PaperForLookup) -> List[Tuple[str, str]]:
        """Generate search queries for manual research"""

        queries = []

        # Google Scholar
        gs_query = f'"{paper.title}" {paper.year}'
        queries.append(('Google Scholar', f"https://scholar.google.com/scholar?q={quote(gs_query)}"))

        # arXiv direct search
        arxiv_query = f'"{paper.title}"'
        queries.append(('arXiv', f"https://arxiv.org/search/?query={quote(arxiv_query)}&searchtype=all"))

        # CrossRef by title
        cr_query = f'"{paper.title}"'
        queries.append(('CrossRef', f"https://www.crossref.org/?q={quote(cr_query)}"))

        # Semantic Scholar
        ss_query = f'"{paper.title}"'
        queries.append(('Semantic Scholar', f"https://www.semanticscholar.org/search?q={quote(ss_query)}"))

        return queries

    def print_stats(self):
        """Print statistics"""
        logger.info("=" * 60)
        logger.info("SMART AUTHOR LOOKUP SUMMARY")
        logger.info("=" * 60)
        logger.info(f"Total incomplete papers:   {self.stats['total_incomplete']}")
        logger.info(f"Found via arXiv:           {self.stats['found_arxiv']}")
        logger.info(f"Found via CrossRef:        {self.stats['found_crossref']}")
        logger.info(f"Found total:               {self.stats['found_total']}")
        logger.info(f"Needs manual research:     {self.stats['needs_manual_research']}")
        logger.info("=" * 60)


def main():
    """Main entry point"""
    # Parse arguments
    arxiv_only = '--arxiv-only' in sys.argv
    report_only = '--report' in sys.argv
    dry_run = '--dry-run' in sys.argv

    # Create engine
    engine = SmartAuthorLookup(PAPERS_DIR, AUTHORS_DIR)

    # Scan incomplete papers
    engine.scan_incomplete_papers()

    if not report_only:
        # Perform lookups
        engine.lookup_all(arxiv_only=arxiv_only)
        engine.print_stats()

        # Update papers if found authors
        if engine.results:
            engine.update_papers(dry_run=dry_run)

    # Generate report
    report_path = WORKSPACE_ROOT / 'AUTHOR_LOOKUP_RESEARCH_TASKS.md'
    engine.generate_research_report(report_path)


if __name__ == '__main__':
    main()
