#!/usr/bin/env python3
"""
Fix corrupted abstracts containing quantum physics text.

These abstracts were incorrectly populated with a quantum teleportation paper abstract:
"An unknown quantum state...Einstein-Podolsky-Rosen (EPR) correlations..."

Strategy:
1. Find all papers with corrupted abstract in frontmatter
2. Try to extract correct abstract from body (## Abstract section)
3. If body has "No abstract available", fetch from arXiv/Semantic Scholar
4. Update frontmatter with corrected abstract
"""

import re
import sys
import time
import logging
import urllib.request
import json
from pathlib import Path
from xml.etree import ElementTree

logger = logging.getLogger(__name__)

# Add the PYTHON directory to sys.path for importing yaml_frontmatter_utils
sys.path.insert(0, str(Path(__file__).parent))
from yaml_frontmatter_utils import read_paper, write_paper
from vault_config import PAPERS_DIR, WORKSPACE_ROOT

# The corrupted quantum physics text pattern
CORRUPTED_PATTERN = r"An unknown quantum state"

def get_arxiv_abstract(url_or_id):
    """Fetch abstract from arXiv API."""
    # Extract arxiv ID
    if 'arxiv.org' in url_or_id:
        match = re.search(r'(\d+\.\d+)', url_or_id)
        if match:
            arxiv_id = match.group(1)
        else:
            return None
    else:
        arxiv_id = url_or_id

    api_url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"

    try:
        req = urllib.request.Request(api_url, headers={'User-Agent': 'CEI-Literature-Vault/1.0'})
        with urllib.request.urlopen(req, timeout=15) as response:
            xml_data = response.read().decode('utf-8')

        root = ElementTree.fromstring(xml_data)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}

        entry = root.find('atom:entry', ns)
        if entry is not None:
            summary = entry.find('atom:summary', ns)
            if summary is not None and summary.text:
                abstract = summary.text.strip()
                abstract = re.sub(r'\s+', ' ', abstract)
                return abstract
    except Exception as e:
        logger.warning(f"    arXiv API error: {e}")
    return None

def get_semantic_scholar_abstract(doi_or_url):
    """Fetch abstract from Semantic Scholar API."""
    # Extract DOI or paper ID
    paper_id = None

    if 'doi.org' in doi_or_url or re.match(r'10\.\d+/', doi_or_url):
        # It's a DOI
        doi_match = re.search(r'(10\.\d+/[^\s]+)', doi_or_url)
        if doi_match:
            paper_id = doi_match.group(1)
    elif 'semanticscholar.org' in doi_or_url:
        match = re.search(r'/paper/[^/]+/([a-f0-9]+)', doi_or_url)
        if match:
            paper_id = match.group(1)

    if not paper_id:
        return None

    api_url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}?fields=abstract"

    try:
        req = urllib.request.Request(api_url, headers={'User-Agent': 'CEI-Literature-Vault/1.0'})
        with urllib.request.urlopen(req, timeout=15) as response:
            data = json.loads(response.read().decode('utf-8'))
            abstract = data.get('abstract')
            if abstract:
                return abstract.strip()
    except Exception as e:
        logger.warning(f"    Semantic Scholar API error: {e}")
    return None

def extract_body_abstract(body):
    """Extract abstract from markdown body (## Abstract section)."""
    if '## Abstract' not in body:
        return None

    try:
        parts = body.split('## Abstract')
        if len(parts) < 2:
            return None

        abstract_section = parts[1]
        # Find the next section header
        next_section = re.search(r'\n## ', abstract_section)
        if next_section:
            abstract_section = abstract_section[:next_section.start()]

        abstract = abstract_section.strip()

        # Check if it's a placeholder or corrupted
        if not abstract:
            return None
        if 'No abstract available' in abstract.lower():
            return None
        if 'An unknown quantum state' in abstract:
            return None
        if len(abstract) < 50:  # Too short to be valid
            return None

        return abstract
    except Exception:
        return None

def extract_urls_from_content(content):
    """Extract arXiv and DOI URLs from paper content."""
    urls = {
        'arxiv': None,
        'doi': None,
        'url': None
    }

    # ArXiv URL
    arxiv_match = re.search(r'(https?://arxiv\.org/(?:abs|pdf)/[\d\.v]+)', content)
    if arxiv_match:
        urls['arxiv'] = arxiv_match.group(1)

    # DOI
    doi_match = re.search(r'(10\.\d+/[^\s\n"]+)', content)
    if doi_match:
        urls['doi'] = doi_match.group(1).rstrip('.,)')

    # General URL from frontmatter
    url_match = re.search(r'^url:\s*"?([^"\n]+)"?', content, re.MULTILINE)
    if url_match:
        urls['url'] = url_match.group(1).strip()

    return urls

def update_frontmatter_abstract(frontmatter, new_abstract):
    """Update the abstract field in frontmatter."""
    lines = frontmatter.split('\n')
    new_lines = []
    abstract_updated = False

    for line in lines:
        if line.startswith('abstract:'):
            # Escape quotes in abstract
            safe_abstract = new_abstract.replace('"', '\\"')
            # Truncate very long abstracts for YAML
            if len(safe_abstract) > 3000:
                safe_abstract = safe_abstract[:3000] + "..."
            new_lines.append(f'abstract: "{safe_abstract}"')
            abstract_updated = True
        else:
            new_lines.append(line)

    if not abstract_updated:
        # Add abstract field if it didn't exist
        safe_abstract = new_abstract.replace('"', '\\"')
        new_lines.append(f'abstract: "{safe_abstract}"')

    return '\n'.join(new_lines)

def is_abstract_corrupted(content):
    """Check if the frontmatter abstract contains the corrupted quantum text."""
    # Look for abstract field in frontmatter
    match = re.search(r'^abstract:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
    if match:
        abstract = match.group(1)
        return CORRUPTED_PATTERN in abstract
    return False

def main():
    papers_dir = PAPERS_DIR

    stats = {
        'total_corrupted': 0,
        'fixed_from_body': 0,
        'fixed_from_arxiv': 0,
        'fixed_from_semanticscholar': 0,
        'still_corrupted': [],
        'errors': []
    }

    logger.info("=" * 60)
    logger.info("Fixing Corrupted Abstracts")
    logger.info("=" * 60)

    # Find all corrupted papers
    corrupted_papers = []
    for md_file in sorted(papers_dir.glob('*.md')):
        content = md_file.read_text(encoding='utf-8')
        if is_abstract_corrupted(content):
            corrupted_papers.append(md_file)

    logger.info(f"Found {len(corrupted_papers)} papers with corrupted abstracts.")
    stats['total_corrupted'] = len(corrupted_papers)

    for md_file in corrupted_papers:
        logger.info(f"Processing: {md_file.name[:55]}...")

        try:
            content = md_file.read_text(encoding='utf-8')
            frontmatter, body = read_paper(md_file)

            # Strategy 1: Extract from body
            body_abstract = extract_body_abstract(body)
            if body_abstract:
                new_frontmatter = update_frontmatter_abstract(frontmatter, body_abstract)
                write_paper(md_file, new_frontmatter, body, validate=True)
                logger.info(f"  Fixed from body abstract")
                stats['fixed_from_body'] += 1
                continue

            # Strategy 2: Fetch from arXiv
            urls = extract_urls_from_content(content)

            if urls['arxiv']:
                logger.info(f"  Trying arXiv: {urls['arxiv'][:40]}...")
                arxiv_abstract = get_arxiv_abstract(urls['arxiv'])
                time.sleep(0.3)  # Rate limit

                if arxiv_abstract:
                    new_frontmatter = update_frontmatter_abstract(frontmatter, arxiv_abstract)
                    write_paper(md_file, new_frontmatter, body, validate=True)
                    logger.info(f"  Fixed from arXiv")
                    stats['fixed_from_arxiv'] += 1
                    continue

            # Strategy 3: Fetch from Semantic Scholar via DOI
            if urls['doi']:
                logger.info(f"  Trying Semantic Scholar: {urls['doi'][:40]}...")
                ss_abstract = get_semantic_scholar_abstract(urls['doi'])
                time.sleep(0.5)  # Rate limit

                if ss_abstract:
                    new_frontmatter = update_frontmatter_abstract(frontmatter, ss_abstract)
                    write_paper(md_file, new_frontmatter, body, validate=True)
                    logger.info(f"  Fixed from Semantic Scholar")
                    stats['fixed_from_semanticscholar'] += 1
                    continue

            # Could not fix
            logger.warning(f"  Could not find correct abstract")
            stats['still_corrupted'].append(md_file.name)

        except Exception as e:
            logger.error(f"  ERROR: {e}")
            stats['errors'].append((md_file.name, str(e)))

    # Summary
    logger.info("=" * 60)
    logger.info("SUMMARY")
    logger.info("=" * 60)
    logger.info(f"Total corrupted papers: {stats['total_corrupted']}")
    logger.info(f"Fixed from body:        {stats['fixed_from_body']}")
    logger.info(f"Fixed from arXiv:       {stats['fixed_from_arxiv']}")
    logger.info(f"Fixed from S2:          {stats['fixed_from_semanticscholar']}")
    logger.info(f"Still corrupted:        {len(stats['still_corrupted'])}")
    logger.info(f"Errors:                 {len(stats['errors'])}")

    if stats['still_corrupted']:
        logger.info("--- Papers still needing manual fix ---")
        for name in stats['still_corrupted']:
            logger.warning(f"  - {name}")

    if stats['errors']:
        logger.info("--- Errors ---")
        for name, err in stats['errors']:
            logger.error(f"  - {name}: {err}")

    # Write report
    report_path = WORKSPACE_ROOT / 'corrupted_abstracts_report.txt'
    with open(report_path, 'w') as f:
        f.write("Corrupted Abstracts Fix Report\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Total corrupted: {stats['total_corrupted']}\n")
        f.write(f"Fixed from body: {stats['fixed_from_body']}\n")
        f.write(f"Fixed from arXiv: {stats['fixed_from_arxiv']}\n")
        f.write(f"Fixed from Semantic Scholar: {stats['fixed_from_semanticscholar']}\n")
        f.write(f"Still corrupted: {len(stats['still_corrupted'])}\n\n")

        if stats['still_corrupted']:
            f.write("Papers still needing manual fix:\n")
            for name in stats['still_corrupted']:
                f.write(f"  - {name}\n")

    logger.info(f"Report saved to: {report_path}")

if __name__ == "__main__":
    main()
