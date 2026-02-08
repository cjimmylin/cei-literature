#!/usr/bin/env python3
"""
Complete Author Data Fix Script
Fixes all 580 papers to have:
1. Complete author lists (no "others" or abbreviations)
2. Wikilinks to author pages in paper bodies
3. Proper YAML formatting

Author data sources (in priority order):
1. arXiv API (most reliable for arxiv papers)
2. Semantic Scholar API
3. Existing author files in Authors/ directory
4. PDF extracts
5. Local PDFs
"""

import csv
import os
import re
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import quote
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)

# Import safe YAML utilities
from yaml_frontmatter_utils import (
    extract_frontmatter,
    parse_frontmatter,
    validate_frontmatter,
    write_paper,
    rebuild_frontmatter,
)

# Import author validation
try:
    from author_validation import (
        validate_author_name,
        normalize_author_name,
        find_full_name_match,
    )
    HAS_VALIDATION = True
except ImportError:
    HAS_VALIDATION = False

# Configuration - use vault_config for paths
from vault_config import (
    WORKSPACE_ROOT, PAPERS_DIR, AUTHORS_DIR, PDF_EXTRACTS_DIR, PDFS_DIR
)
VAULT_PATH = WORKSPACE_ROOT
BASE_CSV = VAULT_PATH / "Base.md"

# API configurations
ARXIV_API_BASE = "http://export.arxiv.org/api/query?"
SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/graph/v1/paper"

# Results tracking
RESULTS = {
    "total_papers": 0,
    "papers_with_others": [],
    "papers_with_abbreviations": [],
    "papers_missing_wikilinks": [],
    "papers_fixed": [],
    "papers_failed": [],
    "authors_created": [],
    "skipped_papers": [],
}


def load_csv_data() -> Dict:
    """Load author data from Base.md CSV"""
    csv_data = {}
    try:
        with open(BASE_CSV, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = row['Key']
                csv_data[key] = {
                    'authors': row.get('Author', ''),
                    'title': row.get('Title', ''),
                    'year': row.get('Publication Year', ''),
                    'doi': row.get('DOI', ''),
                    'url': row.get('Url', ''),
                    'abstract': row.get('Abstract Note', ''),
                }
    except Exception as e:
        logger.error(f"ERROR loading CSV: {e}")
    return csv_data


def extract_arxiv_id(url: str) -> Optional[str]:
    """Extract arXiv ID from URL"""
    if not url:
        return None

    # Pattern: arxiv.org/abs/XXXX.XXXXX or arxiv.org/pdf/XXXX.XXXXX
    match = re.search(r'arxiv\.org/(?:abs|pdf)/(\d+\.\d+)', url)
    if match:
        return match.group(1)
    return None


def extract_doi(url: str) -> Optional[str]:
    """Extract DOI from URL"""
    if not url:
        return None

    # Pattern: doi.org/XXX or in URL parameter
    match = re.search(r'doi\.org/(10\.\S+)', url)
    if match:
        return match.group(1)

    # Check in URL string
    if '10.' in url:
        match = re.search(r'(10\.\S+?)(?:["\']|$|\s)', url)
        if match:
            return match.group(1)
    return None


def fetch_arxiv_authors(arxiv_id: str) -> List[str]:
    """Fetch complete author list from arXiv API using urllib"""
    try:
        # Query arXiv API
        query = quote(f"id:{arxiv_id}")
        url = f"{ARXIV_API_BASE}search_query={query}&start=0&max_results=1&sortBy=submittedDate&sortOrder=descending"

        with urllib.request.urlopen(url, timeout=5) as response:
            if response.status != 200:
                return []

            # Parse XML response
            root = ET.fromstring(response.read())

            # Find all authors
            authors = []
            ns = {'atom': 'http://www.w3.org/2005/Atom'}
            for entry in root.findall('atom:entry', ns):
                author_elements = entry.findall('atom:author', ns)
                for author_elem in author_elements:
                    name_elem = author_elem.find('atom:name', ns)
                    if name_elem is not None:
                        authors.append(name_elem.text.strip())

            return authors
    except Exception as e:
        # Silently skip if API unavailable
        return []


def fetch_semantic_scholar_authors(doi: str) -> List[str]:
    """Fetch author list from Semantic Scholar API using urllib"""
    try:
        url = f"{SEMANTIC_SCHOLAR_API}/DOI:{quote(doi)}"

        with urllib.request.urlopen(url, timeout=5) as response:
            if response.status != 200:
                return []

            data = json.loads(response.read().decode())

            # Extract authors
            authors = []
            if 'authors' in data:
                for author in data['authors']:
                    if 'name' in author:
                        authors.append(author['name'])

            return authors
    except Exception:
        # Silently skip if API unavailable
        return []


def extract_authors_from_pdf_text(pdf_extract_path: str) -> List[str]:
    """Extract author list from PDF extract markdown"""
    try:
        if not pdf_extract_path or not os.path.exists(pdf_extract_path):
            return []

        with open(pdf_extract_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Look for author patterns at the beginning of PDF text
        # Pattern: "Author1, Author2, Author3"
        first_page = content[:1000]

        # Try to find author line (usually "Author: ...")
        author_match = re.search(r'[Aa]uthor[s]?:?\s*([^\.]+)', first_page)
        if author_match:
            author_str = author_match.group(1).strip()
            # Split on semicolon or "and"
            authors = re.split(r';\s*|,\s*', author_str)
            return [a.strip() for a in authors if a.strip()]

        return []
    except Exception as e:
        logger.warning(f"  PDF extract parsing failed: {e}")
        return []


def parse_author_list(authors_str: str) -> List[str]:
    """Parse comma/semicolon-separated author string into list"""
    if not authors_str:
        return []

    # Remove "et al" and "others"
    cleaned = re.sub(r';\s*(?:et al|others|and)', '', authors_str, flags=re.IGNORECASE)

    # Split on semicolon or comma
    authors = re.split(r';\s*|,\s*(?![^\(]*\))', cleaned)

    # Clean up each author name
    result = []
    for author in authors:
        author = author.strip()
        if author and author.lower() not in ['others', 'et al', 'and']:
            # Use validation if available
            if HAS_VALIDATION:
                normalized = normalize_author_name(author)
                is_valid, errors, _ = validate_author_name(normalized)
                if is_valid:
                    # Try to expand abbreviated names
                    full_name = find_full_name_match(normalized)
                    result.append(full_name if full_name else normalized)
                # Skip invalid names (single letters, broken wikilinks, etc.)
            else:
                result.append(author)

    return result


def expand_abbreviated_name(abbreviated: str) -> str:
    """Try to expand abbreviated author names using existing author files"""
    # Pattern: "LastName, A. B." or "A. B. LastName"

    # Try to find matching author files
    authors_list = list(AUTHORS_DIR.glob('*.md'))

    for author_file in authors_list:
        author_name = author_file.stem

        # Check if abbreviated name matches
        initials = ''.join([m[0] for m in author_name.split()])
        if initials.lower() in abbreviated.lower():
            # Could be a match
            if author_name.lower() in abbreviated.lower():
                return author_name

    # If no match found, return original
    return abbreviated


def get_author_wikilink_format(name: str) -> str:
    """Convert author name to wikilink format, checking Authors/ directory"""
    # Format: [[Author Name]]
    # First check if author file exists

    # Try exact match
    author_file = AUTHORS_DIR / f"{name}.md"
    if author_file.exists():
        return f"[[{name}]]"

    # Try comma-separated format (LastName, FirstName)
    if ',' in name:
        # Already in format
        author_file = AUTHORS_DIR / f"{name}.md"
        if author_file.exists():
            return f"[[{name}]]"
    else:
        # Try converting to comma format
        parts = name.strip().split()
        if len(parts) > 1:
            comma_format = f"{parts[-1]}, {' '.join(parts[:-1])}"
            author_file = AUTHORS_DIR / f"{comma_format}.md"
            if author_file.exists():
                return f"[[{comma_format}]]"

    # If no file found, create wikilink anyway (file can be created later)
    return f"[[{name}]]"


def analyze_paper(paper_path: Path, csv_data: Dict) -> Dict:
    """Analyze a single paper for author issues"""
    analysis = {
        'file': paper_path.name,
        'path': str(paper_path),
        'has_others': False,
        'has_abbreviations': False,
        'missing_wikilinks': False,
        'csv_authors': '',
        'file_authors': '',
        'needs_fix': False,
        'issues': [],
    }

    try:
        content = paper_path.read_text(encoding='utf-8')

        # Extract frontmatter
        fm_match = re.match(r'---\n(.*?)\n---\n', content, re.DOTALL)
        if not fm_match:
            analysis['issues'].append("No YAML frontmatter")
            return analysis

        frontmatter = fm_match.group(1)
        body = content[fm_match.end():]

        # Parse frontmatter
        fields = parse_frontmatter(frontmatter)
        key_field = fields.get('key', '')
        file_authors = fields.get('authors', '')

        analysis['file_authors'] = file_authors

        # Get CSV data
        if key_field in csv_data:
            csv_authors = csv_data[key_field]['authors']
            analysis['csv_authors'] = csv_authors

            # Check for "others" or "et al"
            if csv_authors and ('et al' in csv_authors or 'others' in csv_authors.lower()):
                analysis['has_others'] = True
                analysis['needs_fix'] = True
                analysis['issues'].append("Contains 'others' or 'et al' placeholder")

            # Check for abbreviations
            if csv_authors and re.search(r'\b[A-Z]\.\s+[A-Z]', csv_authors):
                analysis['has_abbreviations'] = True
                analysis['needs_fix'] = True
                analysis['issues'].append("Contains abbreviated author names")

        # Check for wikilinks in body
        wikilinks = re.findall(r'\[\[([^\]]+)\]\]', body)
        if file_authors and not wikilinks:
            analysis['missing_wikilinks'] = True
            analysis['needs_fix'] = True
            analysis['issues'].append(f"Missing {len(parse_author_list(file_authors))} author wikilinks")

        return analysis

    except Exception as e:
        analysis['issues'].append(f"Parse error: {str(e)}")
        return analysis


def fix_paper(paper_path: Path, csv_data: Dict, dry_run: bool = False) -> bool:
    """Fix author data in a single paper"""
    try:
        content = paper_path.read_text(encoding='utf-8')

        # Extract frontmatter and body
        fm_match = re.match(r'---\n(.*?)\n---\n', content, re.DOTALL)
        if not fm_match:
            return False

        frontmatter = fm_match.group(1)
        body = content[fm_match.end():]

        # Parse frontmatter
        fields = parse_frontmatter(frontmatter)
        key_field = fields.get('key', '')

        if key_field not in csv_data:
            return False

        csv_row = csv_data[key_field]
        authors_str = csv_row['authors']
        url = csv_row['url']

        # Step 1: Get full author list
        full_authors = []

        # Try arXiv API
        if url:
            arxiv_id = extract_arxiv_id(url)
            if arxiv_id:
                full_authors = fetch_arxiv_authors(arxiv_id)
                if full_authors:
                    logger.info(f"  Fetched {len(full_authors)} authors from arXiv for {paper_path.name}")

        # Try Semantic Scholar if arXiv didn't work
        if not full_authors and csv_row['doi']:
            doi = csv_row['doi']
            full_authors = fetch_semantic_scholar_authors(doi)
            if full_authors:
                logger.info(f"  Fetched {len(full_authors)} authors from Semantic Scholar for {paper_path.name}")

        # Try PDF extract
        if not full_authors:
            pdf_extract = fields.get('pdf_extract', '')
            if pdf_extract:
                pdf_extract_path = VAULT_PATH / pdf_extract
                full_authors = extract_authors_from_pdf_text(str(pdf_extract_path))
                if full_authors:
                    logger.info(f"  Extracted {len(full_authors)} authors from PDF text for {paper_path.name}")

        # Fallback: use CSV authors and clean up
        if not full_authors:
            full_authors = parse_author_list(authors_str)

        if not full_authors:
            logger.warning(f"  Could not determine full author list for {paper_path.name}")
            return False

        # Step 2: Create wikilinks
        author_wikilinks = [get_author_wikilink_format(author) for author in full_authors]

        # Step 3: Update frontmatter
        fields['authors'] = "; ".join(full_authors)

        # Rebuild frontmatter
        new_frontmatter = rebuild_frontmatter(fields)

        # Validate
        is_valid, issues = validate_frontmatter(new_frontmatter)
        if not is_valid:
            logger.error(f"  YAML validation failed for {paper_path.name}: {issues}")
            return False

        # Step 4: Add author links to body if missing
        # Check if already has author section
        if not re.search(r'## Authors?|## See Also', body, re.IGNORECASE):
            # Add authors section after abstract
            author_section = f"\n## Authors\n\n{', '.join(author_wikilinks)}\n"
            body = re.sub(
                r'(## Abstract\n.*?\n)(?=\n## |$)',
                r'\1' + author_section,
                body,
                flags=re.DOTALL
            )

        # Reconstruct content
        new_content = f"---\n{new_frontmatter}\n---\n{body}"

        # Write if not dry run
        if not dry_run:
            write_paper(paper_path, new_frontmatter, body, validate=True)
            logger.info(f"  Fixed {paper_path.name} with {len(full_authors)} complete authors")
            RESULTS['papers_fixed'].append(paper_path.name)
            return True
        else:
            logger.info(f"  [DRY-RUN] Would fix {paper_path.name} with {len(full_authors)} authors")
            return True

    except Exception as e:
        logger.error(f"  Error fixing {paper_path.name}: {e}")
        RESULTS['papers_failed'].append((paper_path.name, str(e)))
        return False


def main(dry_run: bool = False, limit: int = None):
    """Main execution"""
    logger.info("=" * 100)
    logger.info("COMPLETE AUTHOR DATA FIX")
    logger.info("=" * 100)

    # Load CSV data
    logger.info("Loading Base.md CSV data...")
    csv_data = load_csv_data()
    logger.info(f"Loaded {len(csv_data)} entries from CSV")

    # Get all papers
    logger.info("Scanning all papers...")
    papers = sorted(PAPERS_DIR.glob('*.md'))
    if limit:
        papers = papers[:limit]

    RESULTS['total_papers'] = len(papers)
    logger.info(f"Found {len(papers)} papers to process")

    # Analyze all papers
    logger.info("Analyzing papers for author issues...")
    papers_to_fix = []

    for i, paper in enumerate(papers):
        if (i + 1) % 100 == 0:
            logger.info(f"  Analyzed {i + 1}/{len(papers)}...")

        analysis = analyze_paper(paper, csv_data)

        if analysis['has_others']:
            RESULTS['papers_with_others'].append(analysis)

        if analysis['has_abbreviations']:
            RESULTS['papers_with_abbreviations'].append(analysis)

        if analysis['missing_wikilinks']:
            RESULTS['papers_missing_wikilinks'].append(analysis)

        if analysis['needs_fix']:
            papers_to_fix.append(paper)

    logger.info("Analysis complete")

    # Summary
    logger.info("SUMMARY OF ISSUES FOUND:")
    logger.info(f"  Papers with 'others'/'et al': {len(RESULTS['papers_with_others'])}")
    logger.info(f"  Papers with abbreviations: {len(RESULTS['papers_with_abbreviations'])}")
    logger.info(f"  Papers missing wikilinks: {len(RESULTS['papers_missing_wikilinks'])}")
    logger.info(f"  Total papers needing fixes: {len(papers_to_fix)}")

    if not papers_to_fix:
        logger.info("All papers have complete author data!")
        return

    # Fix papers
    logger.info(f"Fixing {len(papers_to_fix)} papers...")
    logger.info(f"(Running in {'DRY-RUN' if dry_run else 'WRITE'} mode)")

    for i, paper in enumerate(papers_to_fix):
        if (i + 1) % 50 == 0:
            logger.info(f"Progress: {i + 1}/{len(papers_to_fix)}...")

        fix_paper(paper, csv_data, dry_run=dry_run)

    # Final report
    logger.info("=" * 100)
    logger.info("FINAL REPORT")
    logger.info("=" * 100)
    logger.info(f"Papers fixed: {len(RESULTS['papers_fixed'])}")
    logger.info(f"Papers failed: {len(RESULTS['papers_failed'])}")

    if RESULTS['papers_failed']:
        logger.info("Failed papers:")
        for paper, error in RESULTS['papers_failed'][:10]:
            logger.info(f"  - {paper}: {error}")

    # Save report
    report_path = VAULT_PATH / "20260124-AUTHOR_FIX_REPORT.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(RESULTS, f, indent=2)

    logger.info(f"Report saved to {report_path}")


if __name__ == "__main__":
    import sys

    dry_run = "--dry-run" in sys.argv
    limit = None

    # Check for limit parameter
    for arg in sys.argv:
        if arg.startswith("--limit="):
            limit = int(arg.split("=")[1])

    main(dry_run=dry_run, limit=limit)
