#!/usr/bin/env python3
"""
Fetch Missing Abstracts for CEI Literature Vault

This script identifies papers missing abstracts and attempts to fetch them from:
1. arXiv API - for preprints with arXiv IDs
2. CrossRef API - for papers with DOIs
3. OpenAlex API - broader academic coverage

Uses yaml_frontmatter_utils.py for safe YAML operations.
"""

import re
import json
import time
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from xml.etree import ElementTree
import ssl
import logging

# Import YAML utilities
from yaml_frontmatter_utils import (
    read_paper, write_paper, parse_frontmatter,
    validate_frontmatter, extract_frontmatter
)
from vault_config import PAPERS_DIR, WORKSPACE_ROOT

logger = logging.getLogger(__name__)

# Rate limiting delays (seconds)
ARXIV_DELAY = 3.0  # arXiv requires 3s between requests
CROSSREF_DELAY = 0.5
OPENALEX_DELAY = 0.5

# SSL context for HTTPS requests
ssl_context = ssl.create_default_context()


def extract_abstract_from_body(body: str) -> Optional[str]:
    """Try to extract abstract from the markdown body content."""
    # Look for ## Abstract section
    match = re.search(r'##\s*Abstract\s*\n+(.+?)(?=\n##|\n\*\*|\Z)', body, re.DOTALL)
    if match:
        abstract = match.group(1).strip()
        # Skip if it's a placeholder
        if abstract and 'No abstract available' not in abstract and len(abstract) > 50:
            # Clean up markdown formatting
            abstract = re.sub(r'\*+', '', abstract)  # Remove bold/italic markers
            abstract = re.sub(r'\s+', ' ', abstract)  # Normalize whitespace
            return abstract.strip()
    return None


def get_papers_missing_abstracts() -> List[Tuple[Path, Dict, str]]:
    """Find all papers that are missing abstracts in YAML frontmatter."""
    missing = []

    for paper_path in PAPERS_DIR.glob("*.md"):
        try:
            frontmatter, body = read_paper(paper_path)
            fields = parse_frontmatter(frontmatter)

            # Check if abstract is missing or placeholder in YAML
            abstract = fields.get('abstract', '').strip()
            if not abstract or abstract in ['N/A', 'Unknown', '', '""']:
                missing.append((paper_path, fields, body))

        except Exception as e:
            logger.error(f"Error reading {paper_path.name}: {e}")

    return missing


def extract_arxiv_id(fields: Dict) -> Optional[str]:
    """Extract arXiv ID from paper metadata."""
    # Check URL field
    url = fields.get('url', '')

    # Pattern: arxiv.org/abs/XXXX.XXXXX or arxiv.org/pdf/XXXX.XXXXX
    match = re.search(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})', url)
    if match:
        return match.group(1)

    # Check for old-style arXiv IDs (e.g., cs.CL/0604106)
    match = re.search(r'arxiv\.org/(?:abs|pdf)/([\w-]+/\d+)', url)
    if match:
        return match.group(1)

    # Check extra field for arXiv ID
    extra = fields.get('extra', '')
    match = re.search(r'arXiv:\s*(\d{4}\.\d{4,5})', extra)
    if match:
        return match.group(1)

    return None


def extract_doi(fields: Dict) -> Optional[str]:
    """Extract DOI from paper metadata."""
    doi = fields.get('doi', '').strip()

    # Skip placeholder or invalid DOIs
    if doi and doi != 'N/A' and 'xxxxx' not in doi.lower() and 'XXXXX' not in doi:
        # Validate it looks like a real DOI
        if re.match(r'^10\.\d+/.+', doi):
            return doi

    # Try to extract from URL
    url = fields.get('url', '')
    match = re.search(r'doi\.org/(10\.\d+/[^\s]+)', url)
    if match:
        return match.group(1)

    return None


def fetch_arxiv_abstract(arxiv_id: str) -> Optional[str]:
    """Fetch abstract from arXiv API."""
    try:
        url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"

        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'CEI-Literature-Vault/1.0 (Academic Research)')

        with urllib.request.urlopen(req, timeout=30) as response:
            xml_data = response.read().decode('utf-8')

        # Parse XML
        root = ElementTree.fromstring(xml_data)

        # Find the entry
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        entry = root.find('atom:entry', ns)

        if entry is not None:
            summary = entry.find('atom:summary', ns)
            if summary is not None and summary.text:
                # Clean up the abstract
                abstract = summary.text.strip()
                abstract = re.sub(r'\s+', ' ', abstract)  # Normalize whitespace
                return abstract

        return None

    except Exception as e:
        logger.error(f"  arXiv error for {arxiv_id}: {e}")
        return None


def fetch_crossref_abstract(doi: str) -> Optional[str]:
    """Fetch abstract from CrossRef API."""
    try:
        encoded_doi = urllib.parse.quote(doi, safe='')
        url = f"https://api.crossref.org/works/{encoded_doi}"

        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'CEI-Literature-Vault/1.0 (mailto:research@example.edu)')

        with urllib.request.urlopen(req, context=ssl_context, timeout=30) as response:
            data = json.loads(response.read().decode('utf-8'))

        message = data.get('message', {})
        abstract = message.get('abstract', '')

        if abstract:
            # Clean up HTML tags that CrossRef sometimes includes
            abstract = re.sub(r'<[^>]+>', '', abstract)
            abstract = abstract.strip()
            return abstract

        return None

    except urllib.error.HTTPError as e:
        if e.code != 404:
            logger.error(f"  CrossRef HTTP error for {doi}: {e.code}")
        return None
    except Exception as e:
        logger.error(f"  CrossRef error for {doi}: {e}")
        return None


def fetch_openalex_abstract(title: str, doi: Optional[str] = None) -> Optional[str]:
    """Fetch abstract from OpenAlex API."""
    try:
        # Try DOI first if available
        if doi:
            encoded_doi = urllib.parse.quote(f"https://doi.org/{doi}", safe='')
            url = f"https://api.openalex.org/works/{encoded_doi}"
        else:
            # Search by title
            encoded_title = urllib.parse.quote(title)
            url = f"https://api.openalex.org/works?filter=title.search:{encoded_title}&per-page=1"

        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'CEI-Literature-Vault/1.0 (mailto:research@example.edu)')

        with urllib.request.urlopen(req, context=ssl_context, timeout=30) as response:
            data = json.loads(response.read().decode('utf-8'))

        # Handle direct lookup vs search results
        if 'results' in data:
            results = data.get('results', [])
            if results:
                work = results[0]
            else:
                return None
        else:
            work = data

        # Get abstract inverted index and reconstruct
        abstract_inverted = work.get('abstract_inverted_index', {})

        if abstract_inverted:
            # Reconstruct abstract from inverted index
            words = []
            for word, positions in abstract_inverted.items():
                for pos in positions:
                    words.append((pos, word))
            words.sort(key=lambda x: x[0])
            abstract = ' '.join(word for _, word in words)
            return abstract.strip()

        return None

    except urllib.error.HTTPError as e:
        if e.code != 404:
            logger.error(f"  OpenAlex HTTP error: {e.code}")
        return None
    except Exception as e:
        logger.error(f"  OpenAlex error: {e}")
        return None


def update_paper_abstract(paper_path: Path, abstract: str) -> bool:
    """Update a paper's abstract in the frontmatter."""
    try:
        content = paper_path.read_text(encoding='utf-8')
        frontmatter, body = extract_frontmatter(content)

        # Escape quotes in abstract for YAML
        safe_abstract = abstract.replace('"', '\\"')
        safe_abstract = safe_abstract.replace('\n', ' ')

        # Check if abstract field exists
        if 'abstract:' in frontmatter:
            # Replace existing abstract line
            lines = frontmatter.split('\n')
            new_lines = []
            for line in lines:
                if line.startswith('abstract:'):
                    new_lines.append(f'abstract: "{safe_abstract}"')
                else:
                    new_lines.append(line)
            new_frontmatter = '\n'.join(new_lines)
        else:
            # Add abstract field before the last line
            new_frontmatter = frontmatter.rstrip() + f'\nabstract: "{safe_abstract}"'

        # Validate before writing
        is_valid, issues = validate_frontmatter(new_frontmatter)
        if not is_valid:
            logger.error(f"  Validation failed: {issues}")
            return False

        # Write back
        write_paper(paper_path, new_frontmatter, body, validate=True)
        return True

    except Exception as e:
        logger.error(f"  Error updating {paper_path.name}: {e}")
        return False


def main():
    """Main function to fetch missing abstracts."""
    logger.info("=" * 60)
    logger.info("Fetching Missing Abstracts for CEI Literature Vault")
    logger.info("=" * 60)

    # Find papers missing abstracts
    logger.info("\nScanning papers for missing abstracts...")
    missing_papers = get_papers_missing_abstracts()
    logger.info(f"Found {len(missing_papers)} papers missing abstracts\n")

    # Track results
    results = {
        'body_success': [],
        'arxiv_success': [],
        'crossref_success': [],
        'openalex_success': [],
        'failed': []
    }

    for i, (paper_path, fields, body) in enumerate(missing_papers, 1):
        # Get title - try both 'title' and 'short_title' fields
        title = fields.get('title', '') or fields.get('short_title', 'Unknown')
        # Clean up title - remove quotes
        title = title.strip('"\'')
        logger.info(f"\n[{i}/{len(missing_papers)}] {paper_path.name}")
        logger.info(f"  Title: {title[:60]}...")

        arxiv_id = extract_arxiv_id(fields)
        doi = extract_doi(fields)

        abstract = None
        source = None

        # First, check if abstract is already in the body content
        body_abstract = extract_abstract_from_body(body)
        if body_abstract:
            abstract = body_abstract
            source = 'body'
            logger.info(f"  Found in body content ({len(abstract)} chars)")

        # Try arXiv
        if not abstract and arxiv_id:
            logger.info(f"  Trying arXiv ({arxiv_id})...")
            time.sleep(ARXIV_DELAY)
            abstract = fetch_arxiv_abstract(arxiv_id)
            if abstract:
                source = 'arxiv'
                logger.info(f"  Found via arXiv ({len(abstract)} chars)")

        # Try CrossRef
        if not abstract and doi:
            logger.info(f"  Trying CrossRef ({doi})...")
            time.sleep(CROSSREF_DELAY)
            abstract = fetch_crossref_abstract(doi)
            if abstract:
                source = 'crossref'
                logger.info(f"  Found via CrossRef ({len(abstract)} chars)")

        # Try OpenAlex
        if not abstract:
            logger.info(f"  Trying OpenAlex...")
            time.sleep(OPENALEX_DELAY)
            abstract = fetch_openalex_abstract(title, doi)
            if abstract:
                source = 'openalex'
                logger.info(f"  Found via OpenAlex ({len(abstract)} chars)")

        # Update paper if abstract found
        if abstract and source:
            if update_paper_abstract(paper_path, abstract):
                results[f'{source}_success'].append(paper_path.name)
                logger.info(f"  Updated paper metadata")
            else:
                results['failed'].append(paper_path.name)
        else:
            results['failed'].append(paper_path.name)
            logger.warning(f"  No abstract found")

    # Print summary
    logger.info("\n" + "=" * 60)
    logger.info("SUMMARY")
    logger.info("=" * 60)

    total_success = (len(results['body_success']) +
                     len(results['arxiv_success']) +
                     len(results['crossref_success']) +
                     len(results['openalex_success']))

    logger.info(f"\nTotal papers processed: {len(missing_papers)}")
    logger.info(f"Abstracts fetched: {total_success}")
    logger.info(f"  - from body: {len(results['body_success'])}")
    logger.info(f"  - via arXiv: {len(results['arxiv_success'])}")
    logger.info(f"  - via CrossRef: {len(results['crossref_success'])}")
    logger.info(f"  - via OpenAlex: {len(results['openalex_success'])}")
    logger.info(f"Failed: {len(results['failed'])}")

    if results['body_success']:
        logger.info(f"\nBody extraction successes:")
        for name in results['body_success'][:10]:
            logger.info(f"  - {name}")
        if len(results['body_success']) > 10:
            logger.info(f"  ... and {len(results['body_success']) - 10} more")

    if results['arxiv_success']:
        logger.info(f"\narXiv successes:")
        for name in results['arxiv_success'][:10]:
            logger.info(f"  - {name}")
        if len(results['arxiv_success']) > 10:
            logger.info(f"  ... and {len(results['arxiv_success']) - 10} more")

    if results['crossref_success']:
        logger.info(f"\nCrossRef successes:")
        for name in results['crossref_success'][:10]:
            logger.info(f"  - {name}")
        if len(results['crossref_success']) > 10:
            logger.info(f"  ... and {len(results['crossref_success']) - 10} more")

    if results['openalex_success']:
        logger.info(f"\nOpenAlex successes:")
        for name in results['openalex_success'][:10]:
            logger.info(f"  - {name}")
        if len(results['openalex_success']) > 10:
            logger.info(f"  ... and {len(results['openalex_success']) - 10} more")

    # Save detailed results
    results_file = WORKSPACE_ROOT / "ABSTRACT_FETCH_RESULTS.md"
    with open(results_file, 'w') as f:
        f.write("# Abstract Fetch Results\n\n")
        f.write(f"**Date:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"## Summary\n\n")
        f.write(f"- Total missing: {len(missing_papers)}\n")
        f.write(f"- Fetched: {total_success}\n")
        f.write(f"- Failed: {len(results['failed'])}\n\n")

        if results['body_success']:
            f.write(f"## Body Extraction Success ({len(results['body_success'])})\n\n")
            for name in results['body_success']:
                f.write(f"- {name}\n")
            f.write("\n")

        if results['arxiv_success']:
            f.write(f"## arXiv Success ({len(results['arxiv_success'])})\n\n")
            for name in results['arxiv_success']:
                f.write(f"- {name}\n")
            f.write("\n")

        if results['crossref_success']:
            f.write(f"## CrossRef Success ({len(results['crossref_success'])})\n\n")
            for name in results['crossref_success']:
                f.write(f"- {name}\n")
            f.write("\n")

        if results['openalex_success']:
            f.write(f"## OpenAlex Success ({len(results['openalex_success'])})\n\n")
            for name in results['openalex_success']:
                f.write(f"- {name}\n")
            f.write("\n")

        if results['failed']:
            f.write(f"## Still Missing ({len(results['failed'])})\n\n")
            for name in results['failed']:
                f.write(f"- {name}\n")

    logger.info(f"\nDetailed results saved to: {results_file}")

    return total_success


if __name__ == "__main__":
    main()
