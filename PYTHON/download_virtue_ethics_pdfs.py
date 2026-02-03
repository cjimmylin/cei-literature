#!/usr/bin/env python3
"""
Download PDFs for virtue ethics papers.
Discovers PDF URLs via Semantic Scholar, arXiv, and DOI resolution.
"""

import sys
import re
import json
import time
import logging
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Tuple

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)
logger = logging.getLogger(__name__)

# Paths - use vault_config for external PDF location
from vault_config import PAPERS_DIR, PDFS_DIR

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

# New virtue ethics papers (from create_virtue_ethics_papers.py)
NEW_PAPERS = [
    "2024-Farina-AI and Society - A Virtue Ethics Approach.md",
    "2020-Gabriel-Artificial Intelligence Values and Alignment.md",
    "2025-Unknown-AI Alignment as Fair Treatment of Claims.md",
    "2018-Unknown-The Virtuous Machine - Old Ethics for New.md",
    "2025-Unknown-Virtue in the Machine.md",
    "2024-Smith-Living Well with AI - Virtue Education and AI.md",
    "2024-Ober-AI Ethics with Aristotle.md",
    "2022-Unknown-A Virtue-Based Framework for AI Ethics in Practice.md",
    "2022-Unknown-Can Robotic AI Systems Be Virtuous.md",
    "2025-Unknown-LLM Ethics Benchmark - Three-Dimensional.md",
    "2024-Unknown-Ethical Reasoning and Moral Value Alignment.md",
    "2025-Unknown-Large Language Models Meet Moral Values.md",
    "2025-Unknown-AMULED - Addressing Moral Uncertainty with LLMs.md",
    "2024-Unknown-Moral Persuasion in Large Language Models.md",
    "2024-Unknown-Differences in Moral Foundations of LLMs.md",
    "2023-Stenseke-Artificial Virtuous Agents - Theory to.md",
    "2022-Unknown-Towards Artificial Virtuous Agents - Games and ML.md",
    "2020-Unknown-Machine Ethics - Creation of a Virtuous Machine.md",
    "2024-Unknown-Evaluating Computational Models of Ethics.md",
    "2024-Unknown-Computational Complexity of Ethics.md",
    "2025-Unknown-AI Practical Wisdom and Compassion.md",
    "2022-Unknown-Automated Ethical Practical Reasoning.md",
    "2021-Unknown-Artificial Phronesis - What It Is and Is Not.md",
    "2024-Unknown-Socratic Dialogue for Virtue Ethics in AI.md",
    "2024-Unknown-AI and Phronesis.md",
]


def extract_field(frontmatter: str, field: str) -> Optional[str]:
    """Extract field value from YAML."""
    pattern = rf'^{field}:\s*"?([^"\n]+)"?'
    match = re.search(pattern, frontmatter, re.MULTILINE)
    return match.group(1).strip() if match else None


def find_semantic_scholar_pdf(title: str, authors: Optional[str] = None) -> Optional[Dict]:
    """Search Semantic Scholar for PDF."""
    try:
        query = title
        if authors and authors != "Unknown":
            first_author = authors.split(';')[0].strip() if ';' in authors else authors
            query = f'"{title}" {first_author}'

        url = "https://api.semanticscholar.org/graph/v1/paper/search"
        params = {
            'query': query,
            'fields': 'title,authors,year,venue,openAccessPdf,externalIds',
            'limit': 5
        }
        param_str = '&'.join([f'{k}={urllib.parse.quote(str(v))}' for k, v in params.items()])
        full_url = f"{url}?{param_str}"

        req = urllib.request.Request(full_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as response:
            data = json.loads(response.read().decode('utf-8'))

            if data.get('data'):
                for paper in data['data']:
                    oa_pdf = paper.get('openAccessPdf')
                    if oa_pdf and oa_pdf.get('url'):
                        return {
                            'pdf_url': oa_pdf['url'],
                            'arxiv_id': paper.get('externalIds', {}).get('ArXiv'),
                            'source': 'semantic_scholar'
                        }
        return None
    except Exception as e:
        logger.warning(f"    Semantic Scholar search failed: {e}")
        return None


def convert_url_to_pdf(url: str) -> Optional[str]:
    """Convert various URL formats to direct PDF links."""
    if not url:
        return None

    # arXiv
    if 'arxiv.org/abs/' in url:
        arxiv_id = re.search(r'arxiv\.org/abs/(\d+\.\d+)', url)
        if arxiv_id:
            return f"https://arxiv.org/pdf/{arxiv_id.group(1)}.pdf"

    if 'arxiv.org/pdf/' in url:
        if not url.endswith('.pdf'):
            return url + '.pdf'
        return url

    # ACL Anthology
    if 'aclanthology.org' in url and not url.endswith('.pdf'):
        return url.rstrip('/') + '.pdf'

    # OpenReview
    if 'openreview.net/forum' in url:
        paper_id = re.search(r'id=([^&]+)', url)
        if paper_id:
            return f"https://openreview.net/pdf?id={paper_id.group(1)}"

    # Already a PDF
    if url.endswith('.pdf'):
        return url

    return None


def download_pdf(pdf_url: str, pdf_path: Path) -> Tuple[bool, str, float]:
    """Download a PDF file."""
    try:
        req = urllib.request.Request(pdf_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=60) as response:
            data = response.read()

            # Verify it's actually a PDF
            if not data.startswith(b'%PDF'):
                return False, f"Not a PDF (starts with: {data[:20]})", 0

            with open(pdf_path, 'wb') as f:
                f.write(data)

            size_mb = pdf_path.stat().st_size / (1024 * 1024)
            return True, f"Downloaded ({size_mb:.2f} MB)", size_mb

    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}", 0
    except Exception as e:
        return False, f"Error: {str(e)[:50]}", 0


def update_paper_metadata(paper_path: Path, pdf_url: str, local_pdf: str):
    """Update paper metadata with PDF info."""
    content = paper_path.read_text(encoding='utf-8', errors='ignore')
    fm, body = extract_frontmatter(content)
    fields = parse_frontmatter(fm)

    fields['external_pdf'] = pdf_url
    fields['local_pdf'] = f"[[{local_pdf}]]"

    new_fm = rebuild_frontmatter(fields)
    is_valid, issues = validate_frontmatter(new_fm)

    if is_valid:
        write_paper(paper_path, new_fm, body, validate=True)
        return True
    else:
        logger.error(f"    YAML validation failed: {issues}")
        return False


def main():
    """Process all new virtue ethics papers."""
    PDFS_DIR.mkdir(exist_ok=True)

    logger.info("=" * 70)
    logger.info("DOWNLOADING PDFs FOR VIRTUE ETHICS PAPERS")
    logger.info("=" * 70)

    downloaded = 0
    failed = 0
    skipped = 0

    for i, paper_name in enumerate(NEW_PAPERS, 1):
        paper_path = PAPERS_DIR / paper_name

        if not paper_path.exists():
            logger.warning(f"[{i:2d}] {paper_name}: NOT FOUND")
            continue

        content = paper_path.read_text(encoding='utf-8', errors='ignore')
        fm, _ = extract_frontmatter(content)

        # Check if already has local PDF
        local_pdf = extract_field(fm, 'local_pdf')
        if local_pdf:
            local_clean = local_pdf.strip('[]').replace('[[', '').replace(']]', '')
            if (REPO_ROOT / local_clean).exists():
                logger.info(f"[{i:2d}] {paper_name}: SKIPPED (already has PDF)")
                skipped += 1
                continue

        logger.info(f"[{i:2d}] {paper_name}")

        # Get title and URL
        title = extract_field(fm, 'short_title') or paper_name.replace('.md', '')
        url = extract_field(fm, 'url')
        authors = extract_field(fm, 'authors')
        external_pdf = extract_field(fm, 'external_pdf')

        pdf_url = None
        source = None

        # 1. Check if external_pdf is already set
        if external_pdf and external_pdf.endswith('.pdf'):
            pdf_url = external_pdf
            source = 'external_pdf'
            logger.info(f"    Using existing external_pdf")

        # 2. Try to convert URL to PDF
        if not pdf_url and url:
            pdf_url = convert_url_to_pdf(url)
            if pdf_url:
                source = 'url_conversion'
                logger.info(f"    Converted URL to PDF link")

        # 3. Try Semantic Scholar
        if not pdf_url:
            logger.info(f"    Searching Semantic Scholar...")
            time.sleep(4)  # Rate limit
            result = find_semantic_scholar_pdf(title, authors)
            if result:
                pdf_url = result['pdf_url']
                source = 'semantic_scholar'
                logger.info(f"    Found via Semantic Scholar")

        if not pdf_url:
            logger.warning(f"    No PDF URL found")
            failed += 1
            continue

        # Download
        pdf_filename = paper_name.replace('.md', '.pdf')
        pdf_path = PDFS_DIR / pdf_filename

        logger.info(f"    Downloading from: {pdf_url[:60]}...")
        success, message, size_mb = download_pdf(pdf_url, pdf_path)

        if success:
            # Update metadata
            if update_paper_metadata(paper_path, pdf_url, f"PDFs/{pdf_filename}"):
                logger.info(f"    SUCCESS: {message}")
                downloaded += 1
            else:
                logger.warning(f"    Downloaded but metadata update failed")
                downloaded += 1
        else:
            logger.warning(f"    FAILED: {message}")
            failed += 1

        time.sleep(1)  # Rate limit between downloads

    logger.info("=" * 70)
    logger.info("SUMMARY")
    logger.info("=" * 70)
    logger.info(f"Downloaded: {downloaded}")
    logger.info(f"Failed:     {failed}")
    logger.info(f"Skipped:    {skipped}")
    logger.info(f"Total PDFs in vault: {len(list(PDFS_DIR.glob('*.pdf')))}")


if __name__ == "__main__":
    main()
