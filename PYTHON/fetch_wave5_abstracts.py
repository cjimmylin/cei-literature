#!/usr/bin/env python3
"""
fetch_wave5_abstracts.py - Fetch abstracts for Wave 5 papers (LSRC0599-0848)

Phase A: Mine abstracts from existing PDF extracts (118 papers with extracts)
Phase B: Fetch from arXiv/CrossRef/OpenAlex APIs (remaining papers)

Usage:
  ../.venv/bin/python PYTHON/fetch_wave5_abstracts.py [--phase A|B|both] [--dry-run]

Run from CEI-Lit-WS/ directory.
"""

import re
import sys
import json
import time
import ssl
import urllib.request
import urllib.parse
import urllib.error
import functools
from pathlib import Path
from xml.etree import ElementTree
from typing import Optional, Dict, List, Tuple

# Force stdout flushing for monitoring
print = functools.partial(print, flush=True)

# Setup imports
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from yaml_frontmatter_utils import read_paper, write_paper, validate_frontmatter, parse_frontmatter
from vault_config import PAPERS_DIR, PDF_EXTRACTS_DIR

# Rate limits
ARXIV_DELAY = 3.0
CROSSREF_DELAY = 0.5
OPENALEX_DELAY = 0.5

ssl_context = ssl.create_default_context()


# =============================================================================
# PAPER DISCOVERY
# =============================================================================

def get_wave5_papers_needing_abstracts() -> List[Path]:
    """Find Wave 5 papers (LSRC0599+) with empty abstract field."""
    papers = []
    for p in sorted(PAPERS_DIR.glob("*.md")):
        content = p.read_text(encoding='utf-8')
        m = re.search(r'key: LSRC(\d+)', content)
        if not m or int(m.group(1)) < 599:
            continue
        # Check if abstract is empty or missing
        abst_m = re.search(r'^abstract:\s*"(.+)"', content, re.MULTILINE)
        if abst_m and len(abst_m.group(1).strip()) > 10:
            continue  # Already has an abstract
        papers.append(p)
    return papers


# =============================================================================
# PHASE A: PDF EXTRACT MINING (reused from batch_abstract_and_classify.py)
# =============================================================================

def extract_abstract_from_pdf_extract(paper_path: Path) -> Optional[str]:
    """Extract abstract from the corresponding PDF extract file."""
    content = paper_path.read_text(encoding='utf-8')

    match = re.search(r'^pdf_extract:\s*"?([^"\n]+)"?', content, re.MULTILINE)
    if not match or not match.group(1).strip():
        return None

    extract_rel_path = match.group(1).strip()
    extract_path = PAPERS_DIR.parent / extract_rel_path

    if not extract_path.exists():
        return None

    extract_content = extract_path.read_text(encoding='utf-8')

    # Get first ~3 pages of content
    pages_text = ""
    for page_num in range(1, 4):
        pattern = rf'--- Page {page_num} ---\n(.*?)(?=--- Page {page_num + 1} ---|\Z)'
        page_match = re.search(pattern, extract_content, re.DOTALL)
        if page_match:
            pages_text += page_match.group(1)

    if not pages_text:
        return None

    return _extract_abstract_from_text(pages_text)


def _extract_abstract_from_text(pages_text: str) -> Optional[str]:
    """Extract abstract from raw PDF text."""
    # Find "Abstract" marker
    match = re.search(
        r'(?:^|\n)\s*(?:Abstract|ABSTRACT)\s*[:\.\-—]?\s*\n',
        pages_text
    )
    if not match:
        match = re.search(
            r'(?:^|\n)\s*(?:Abstract|ABSTRACT)\s*[:\.\-—]+\s*',
            pages_text
        )
    if not match:
        match = re.search(
            r'(?:^|\n)\s*(?:Abstract|ABSTRACT)\s*\n',
            pages_text,
            re.IGNORECASE
        )
    if not match:
        return None

    after_abstract = pages_text[match.end():]

    # Find end of abstract (section heading, keywords, etc.)
    end_match = re.search(
        r'\n\s*(?:1[\.\s]+Introduction|Keywords?\s*[:\.]|'
        r'(?:I\.\s+)?Introduction|Index Terms|'
        r'CCS Concepts|Categories|'
        r'\d+\.\s+[A-Z]|'
        r'§\s*\d+|'
        r'ACM Reference)',
        after_abstract,
        re.IGNORECASE
    )

    if end_match:
        abstract_text = after_abstract[:end_match.start()]
    else:
        # Take first ~2000 chars as fallback
        abstract_text = after_abstract[:2000]

    # Clean up
    abstract_text = re.sub(r'-\n(\w)', r'\1', abstract_text)  # Fix hyphenated line breaks
    abstract_text = re.sub(r'\n', ' ', abstract_text)          # Join lines
    abstract_text = re.sub(r'\s+', ' ', abstract_text)         # Normalize whitespace
    abstract_text = abstract_text.strip()

    # Validate length
    if len(abstract_text) < 50 or len(abstract_text) > 5000:
        return None

    return abstract_text


# =============================================================================
# PHASE B: API FETCHING
# =============================================================================

def extract_arxiv_id(content: str) -> Optional[str]:
    """Extract arXiv ID from paper content."""
    m = re.search(r'arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})', content)
    if m:
        return m.group(1)
    m = re.search(r'arXiv:\s*(\d{4}\.\d{4,5})', content)
    if m:
        return m.group(1)
    return None


def extract_doi(content: str) -> Optional[str]:
    """Extract DOI from paper content."""
    m = re.search(r'^doi:\s*"?(10\.\d+/[^"\s]+)"?', content, re.MULTILINE)
    if m:
        return m.group(1).rstrip('"')
    m = re.search(r'doi\.org/(10\.\d+/[^\s"]+)', content)
    if m:
        return m.group(1).rstrip('"')
    return None


def extract_title(content: str) -> Optional[str]:
    """Extract title from paper YAML."""
    m = re.search(r'^short_title:\s*"(.+)"', content, re.MULTILINE)
    if m:
        return m.group(1)
    return None


def fetch_arxiv_abstract(arxiv_id: str) -> Optional[str]:
    """Fetch abstract from arXiv API."""
    try:
        url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'CEI-Literature-Vault/1.0 (Academic Research)')

        with urllib.request.urlopen(req, timeout=30) as response:
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

        return None
    except Exception as e:
        print(f"    arXiv error for {arxiv_id}: {e}")
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

        abstract = data.get('message', {}).get('abstract', '')
        if abstract:
            abstract = re.sub(r'<[^>]+>', '', abstract).strip()
            return abstract
        return None
    except urllib.error.HTTPError as e:
        if e.code != 404:
            print(f"    CrossRef HTTP error for {doi}: {e.code}")
        return None
    except Exception as e:
        print(f"    CrossRef error for {doi}: {e}")
        return None


def fetch_openalex_abstract(title: str, doi: Optional[str] = None) -> Optional[str]:
    """Fetch abstract from OpenAlex API."""
    try:
        if doi:
            encoded_doi = urllib.parse.quote(f"https://doi.org/{doi}", safe='')
            url = f"https://api.openalex.org/works/{encoded_doi}"
        else:
            encoded_title = urllib.parse.quote(title)
            url = f"https://api.openalex.org/works?filter=title.search:{encoded_title}&per-page=1"

        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'CEI-Literature-Vault/1.0 (mailto:research@example.edu)')

        with urllib.request.urlopen(req, context=ssl_context, timeout=30) as response:
            data = json.loads(response.read().decode('utf-8'))

        if 'results' in data:
            results = data.get('results', [])
            work = results[0] if results else None
        else:
            work = data

        if not work:
            return None

        abstract_inverted = work.get('abstract_inverted_index', {})
        if abstract_inverted:
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
            print(f"    OpenAlex HTTP error: {e.code}")
        return None
    except Exception as e:
        print(f"    OpenAlex error: {e}")
        return None


# =============================================================================
# YAML + BODY UPDATE
# =============================================================================

def update_paper_abstract(paper_path: Path, abstract: str) -> bool:
    """Update a paper's abstract in YAML frontmatter and ## Abstract body section."""
    try:
        content = paper_path.read_text(encoding='utf-8')

        # Split at --- boundaries
        parts = content.split('---', 2)
        if len(parts) < 3:
            print(f"    ERROR: Can't parse frontmatter for {paper_path.name}")
            return False

        frontmatter = parts[1]
        body = parts[2]

        # Clean abstract for YAML: replace double quotes with single quotes
        safe_abstract = abstract.replace('"', "'").replace('\n', ' ').strip()
        # Truncate if extremely long
        if len(safe_abstract) > 3000:
            safe_abstract = safe_abstract[:2997] + "..."

        # Update YAML abstract field using safe regex replacement
        if re.search(r'^abstract:', frontmatter, re.MULTILINE):
            new_fm, n = re.subn(
                r'^abstract:.*$',
                f'abstract: "{safe_abstract}"',
                frontmatter,
                count=1,
                flags=re.MULTILINE
            )
            if n == 0:
                print(f"    WARN: abstract field regex didn't match for {paper_path.name}")
                return False
        else:
            # Add abstract field before closing ---
            new_fm = frontmatter.rstrip() + f'\nabstract: "{safe_abstract}"\n'

        # Validate frontmatter
        is_valid, issues = validate_frontmatter(new_fm)
        if not is_valid:
            print(f"    VALIDATION FAILED for {paper_path.name}: {issues}")
            return False

        # Update ## Abstract body section
        new_body = re.sub(
            r'(## Abstract\s*\n).*?(?=\n## |\Z)',
            rf'\1\n{abstract}\n',
            body,
            count=1,
            flags=re.DOTALL
        )

        # Write back
        new_content = f'---{new_fm}---{new_body}'
        paper_path.write_text(new_content, encoding='utf-8')
        return True

    except Exception as e:
        print(f"    ERROR updating {paper_path.name}: {e}")
        return False


# =============================================================================
# MAIN
# =============================================================================

def main():
    args = sys.argv[1:]
    dry_run = '--dry-run' in args

    phase = 'both'
    for i, arg in enumerate(args):
        if arg == '--phase' and i + 1 < len(args):
            phase = args[i + 1].upper()

    print("=" * 60)
    print(f"Fetch Wave 5 Abstracts — Phase: {phase}, Dry-run: {dry_run}")
    print("=" * 60)

    papers = get_wave5_papers_needing_abstracts()
    print(f"\nFound {len(papers)} Wave 5 papers needing abstracts\n")

    stats = {
        'pdf_extract': 0,
        'arxiv': 0,
        'crossref': 0,
        'openalex': 0,
        'failed': 0,
        'skipped': 0,
    }

    # Phase A: PDF extract mining
    if phase in ('A', 'BOTH'):
        print("--- PHASE A: PDF Extract Mining ---")
        phase_a_remaining = []
        for i, p in enumerate(papers, 1):
            content = p.read_text(encoding='utf-8')
            has_extract = re.search(r'^pdf_extract:\s*"(PDF Extracts/.{5,})"', content, re.MULTILINE)

            if not has_extract:
                phase_a_remaining.append(p)
                continue

            abstract = extract_abstract_from_pdf_extract(p)
            if abstract:
                print(f"  [{i}/{len(papers)}] PDF_EXTRACT: {p.name[:60]}...")
                if not dry_run:
                    if update_paper_abstract(p, abstract):
                        stats['pdf_extract'] += 1
                    else:
                        stats['failed'] += 1
                else:
                    stats['pdf_extract'] += 1
            else:
                phase_a_remaining.append(p)

        print(f"\nPhase A: {stats['pdf_extract']} from PDF extracts, {len(phase_a_remaining)} remaining\n")
    else:
        phase_a_remaining = papers

    # Phase B: API fetching
    if phase in ('B', 'BOTH'):
        print("--- PHASE B: API Fetching ---")
        # Re-check which papers still need abstracts (Phase A may have updated some)
        if phase == 'BOTH':
            remaining = []
            for p in phase_a_remaining:
                content = p.read_text(encoding='utf-8')
                abst_m = re.search(r'^abstract:\s*"(.{10,})"', content, re.MULTILINE)
                if not abst_m:
                    remaining.append(p)
            print(f"  {len(remaining)} papers still need abstracts after Phase A\n")
        else:
            remaining = get_wave5_papers_needing_abstracts()
            print(f"  {len(remaining)} papers need abstracts\n")

        for i, p in enumerate(remaining, 1):
            content = p.read_text(encoding='utf-8')
            title = extract_title(content) or p.stem
            arxiv_id = extract_arxiv_id(content)
            doi = extract_doi(content)

            abstract = None
            source = None

            # Try arXiv first
            if arxiv_id:
                abstract = fetch_arxiv_abstract(arxiv_id)
                if abstract:
                    source = 'arxiv'
                time.sleep(ARXIV_DELAY)

            # Try CrossRef
            if not abstract and doi:
                abstract = fetch_crossref_abstract(doi)
                if abstract:
                    source = 'crossref'
                time.sleep(CROSSREF_DELAY)

            # Try OpenAlex
            if not abstract:
                abstract = fetch_openalex_abstract(title, doi)
                if abstract:
                    source = 'openalex'
                time.sleep(OPENALEX_DELAY)

            if abstract:
                print(f"  [{i}/{len(remaining)}] {source.upper()}: {p.name[:55]}...")
                if not dry_run:
                    if update_paper_abstract(p, abstract):
                        stats[source] += 1
                    else:
                        stats['failed'] += 1
                else:
                    stats[source] += 1
            else:
                print(f"  [{i}/{len(remaining)}] FAILED: {p.name[:55]}...")
                stats['failed'] += 1

    # Summary
    total_success = stats['pdf_extract'] + stats['arxiv'] + stats['crossref'] + stats['openalex']
    print("\n" + "=" * 60)
    print("SUMMARY")
    print(f"  PDF Extract: {stats['pdf_extract']}")
    print(f"  arXiv:       {stats['arxiv']}")
    print(f"  CrossRef:    {stats['crossref']}")
    print(f"  OpenAlex:    {stats['openalex']}")
    print(f"  Failed:      {stats['failed']}")
    print(f"  TOTAL:       {total_success}/{total_success + stats['failed']}")
    print("=" * 60)

    # Save log
    if not dry_run:
        log_path = Path("logs/20260213-wave5_abstracts_log.json")
        log_path.write_text(json.dumps(stats, indent=2))
        print(f"\nLog saved to {log_path}")


if __name__ == '__main__':
    main()
