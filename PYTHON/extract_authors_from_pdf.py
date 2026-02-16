#!/usr/bin/env python3
"""
Extract author information from PDF extracts for papers with authors_incomplete: true.

Strategy (waterfall):
  1. Parse author names from the first ~40 lines of the PDF extract (title page)
  2. Fall back to Semantic Scholar API (10s delay to avoid HTTP 429)
  3. Fall back to arXiv API if URL is an arXiv paper

Does NOT auto-apply changes. Outputs a JSON review file for manual inspection.

Usage:
    python extract_authors_from_pdf.py                          # Process all 60
    python extract_authors_from_pdf.py --batch 1 --num-batches 4  # Batch 1 of 4
"""

import argparse
import functools
import json
import re
import sys
import time
import urllib.request
import urllib.parse
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree

# Force stdout flush for parallel execution
print = functools.partial(print, flush=True)

# Path setup
sys.path.insert(0, str(Path(__file__).parent))
from vault_config import PAPERS_DIR, PDF_EXTRACTS_DIR, LOGS_DIR


# =============================================================================
# PDF Extract Parsing
# =============================================================================

def parse_authors_from_extract(extract_path: Path) -> list:
    """
    Try to parse author names from a PDF extract's first pages.

    Heuristics for typical academic paper layout:
    - After the title, authors are listed before "Abstract"
    - Author names are on their own lines or comma/and-separated
    - Affiliations often follow with superscript numbers or on subsequent lines
    """
    if not extract_path.exists():
        return []

    try:
        content = extract_path.read_text(encoding='utf-8')
    except Exception:
        return []

    # Find the content block (between ``` markers after "## Content")
    content_match = re.search(r'## Content\s*\n```\s*\n(.*?)```', content, re.DOTALL)
    if not content_match:
        return []

    text_block = content_match.group(1)

    # Get first ~80 lines (covers title page and maybe page 2)
    lines = text_block.split('\n')[:80]

    # Find the region between title and abstract
    abstract_idx = None
    title_end_idx = None

    for i, line in enumerate(lines):
        stripped = line.strip()
        # Skip page markers
        if stripped.startswith('--- Page'):
            continue
        # Detect abstract keyword
        if re.match(r'^(Abstract|ABSTRACT)[.:\s—–-]', stripped) or stripped == 'Abstract':
            abstract_idx = i
            break

    if abstract_idx is None:
        # No abstract found — try first 40 lines anyway
        abstract_idx = min(40, len(lines))

    # Look for author-like lines between the title and abstract
    # Skip first few lines (page markers, arXiv IDs, title)
    candidates = []
    for i in range(2, abstract_idx):
        line = lines[i].strip()
        if not line:
            continue
        # Skip arXiv IDs, page markers, affiliations (starting with numbers), emails
        if re.match(r'^(arXiv:|--- Page|\d+\s|https?://|\S+@\S+|∗|†|‡|\*)', line):
            continue
        # Skip obvious non-author content
        if any(kw in line.lower() for kw in [
            'abstract', 'introduction', 'keywords', 'university', 'department',
            'institute', 'school of', 'faculty of', 'college of', 'laboratory',
            'research center', 'proceedings', 'conference', 'workshop',
            'copyright', 'published', 'license', 'acm', 'ieee', 'springer',
            'doi:', 'accepted', 'submitted', 'received', 'revised',
            'corresponding author', 'equal contribution', 'work done',
        ]):
            continue
        # Skip lines that are purely numeric or very short
        if len(line) < 3 or line.isdigit():
            continue
        # Skip lines that look like titles (all caps or very long)
        if len(line) > 100:
            continue

        # Check if this looks like an author line:
        # - Contains comma-separated names or
        # - Contains "and" between name-like words or
        # - Is a single name (2-4 capitalized words)
        if _looks_like_author_line(line):
            candidates.append(line)

    # Parse candidate lines into individual names
    authors = []
    for line in candidates:
        names = _split_author_line(line)
        authors.extend(names)

    # Deduplicate while preserving order
    seen = set()
    unique = []
    for name in authors:
        normalized = name.strip()
        if normalized and normalized.lower() not in seen:
            seen.add(normalized.lower())
            unique.append(normalized)

    return unique


def _looks_like_author_line(line: str) -> bool:
    """Heuristic: does this line look like it contains author names?"""
    # Remove superscript markers (1,2,*, †, etc.)
    cleaned = re.sub(r'[0-9,*†‡∗♠♣♦♥⋆]+$', '', line).strip()
    cleaned = re.sub(r'[,\s][0-9*†‡∗⋆]+([,\s])', r'\1', cleaned)

    if not cleaned:
        return False

    # Split by common separators
    parts = re.split(r'[,;]\s*|\s+and\s+', cleaned)
    parts = [p.strip() for p in parts if p.strip()]

    if not parts:
        return False

    # Check if most parts look like names (2-5 words, mostly capitalized)
    name_like_count = 0
    for part in parts:
        # Remove trailing digits/markers
        part = re.sub(r'\s*[0-9*†‡∗⋆]+$', '', part).strip()
        words = part.split()
        if 1 <= len(words) <= 5:
            # Check capitalization — at least first word capitalized
            if words[0][0].isupper():
                name_like_count += 1

    return name_like_count >= len(parts) * 0.6 and name_like_count >= 1


def _split_author_line(line: str) -> list:
    """Split an author line into individual names."""
    # Remove superscript markers
    cleaned = re.sub(r'[0-9*†‡∗⋆♠♣♦♥]+', '', line).strip()
    # Remove trailing/leading commas
    cleaned = cleaned.strip(',').strip()

    # Split by semicolons first (stronger separator), then commas, then "and"
    if ';' in cleaned:
        parts = [p.strip() for p in cleaned.split(';')]
    else:
        # Handle "Name1, Name2, and Name3" pattern
        # But also "Last, First" pattern — disambiguate by checking if parts are ~2 words
        parts_by_comma = [p.strip() for p in cleaned.split(',')]

        # If we have exactly 2 parts and each is 1-2 words, it's likely "Last, First"
        if len(parts_by_comma) == 2 and all(len(p.split()) <= 2 for p in parts_by_comma):
            # Probably "Last, First" format → treat as single name
            parts = [cleaned]
        else:
            # Split by " and " then by commas
            cleaned = re.sub(r'\s+and\s+', ', ', cleaned)
            parts = [p.strip() for p in cleaned.split(',')]

    # Clean up each name
    names = []
    for part in parts:
        name = part.strip().strip(',').strip()
        # Remove email addresses embedded in the name
        name = re.sub(r'\S+@\S+', '', name).strip()
        # Remove parenthetical content
        name = re.sub(r'\([^)]*\)', '', name).strip()
        if name and len(name) > 1 and not name.isdigit():
            names.append(name)

    return names


# =============================================================================
# Semantic Scholar Fallback
# =============================================================================

def query_semantic_scholar(title: str, delay: float = 10.0) -> list:
    """Query Semantic Scholar for paper authors by title."""
    time.sleep(delay)  # Rate limiting

    encoded_title = urllib.parse.quote(title)
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={encoded_title}&limit=3&fields=title,authors"

    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'CEI-Vault-Bot/1.0'})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        print(f"  Semantic Scholar error: {e}")
        return []

    if not data.get('data'):
        return []

    # Find best title match
    best = None
    for paper in data['data']:
        if paper.get('title', '').lower().strip() == title.lower().strip():
            best = paper
            break
    if not best:
        best = data['data'][0]

    authors = []
    for author in best.get('authors', []):
        name = author.get('name', '').strip()
        if name:
            authors.append(name)

    return authors


# =============================================================================
# arXiv Fallback
# =============================================================================

def query_arxiv(arxiv_url: str) -> list:
    """Query arXiv API for paper authors."""
    # Extract arXiv ID from URL
    match = re.search(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})', arxiv_url)
    if not match:
        return []

    arxiv_id = match.group(1)
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"

    time.sleep(3)  # arXiv rate limit

    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'CEI-Vault-Bot/1.0'})
        with urllib.request.urlopen(req, timeout=30) as resp:
            xml_content = resp.read().decode('utf-8')
    except Exception as e:
        print(f"  arXiv error: {e}")
        return []

    # Parse XML
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    try:
        root = ElementTree.fromstring(xml_content)
        entry = root.find('atom:entry', ns)
        if entry is None:
            return []
        authors = []
        for author in entry.findall('atom:author', ns):
            name = author.find('atom:name', ns)
            if name is not None and name.text:
                authors.append(name.text.strip())
        return authors
    except Exception as e:
        print(f"  arXiv XML parse error: {e}")
        return []


# =============================================================================
# Main Pipeline
# =============================================================================

def find_incomplete_papers(papers_dir: Path) -> list:
    """Find all papers with authors_incomplete: true."""
    incomplete = []
    for paper_path in sorted(papers_dir.iterdir()):
        if not paper_path.name.endswith('.md'):
            continue
        try:
            content = paper_path.read_text(encoding='utf-8')
        except Exception:
            continue

        if not content.startswith('---'):
            continue
        end = content.find('\n---\n', 4)
        if end == -1:
            continue
        frontmatter = content[4:end]

        # Check authors_incomplete field
        match = re.search(r'^authors_incomplete:\s*(.+)$', frontmatter, re.MULTILINE)
        if not match:
            continue
        if match.group(1).strip().lower() != 'true':
            continue

        # Extract metadata
        meta = {}
        for field in ['short_title', 'first_author', 'authors', 'url', 'pdf_extract']:
            fm = re.search(rf'^{re.escape(field)}:\s*(.+)$', frontmatter, re.MULTILINE)
            if fm:
                meta[field] = fm.group(1).strip().strip('"')

        incomplete.append({
            'path': str(paper_path),
            'filename': paper_path.name,
            'meta': meta,
        })

    return incomplete


def process_paper(paper: dict, extracts_dir: Path) -> dict:
    """Try to extract full author list for a single paper."""
    filename = paper['filename']
    meta = paper['meta']
    title = meta.get('short_title', '')
    current_authors = meta.get('authors', '')
    url = meta.get('url', '')

    print(f"\nProcessing: {filename}")
    print(f"  Current authors: {current_authors}")

    result = {
        'filename': filename,
        'title': title,
        'current_authors': current_authors,
        'url': url,
        'source': None,
        'proposed_authors': [],
        'confidence': 'none',
    }

    # Strategy 1: Parse from PDF extract
    pdf_extract_ref = meta.get('pdf_extract', '')
    if pdf_extract_ref:
        # Handle both with and without leading path
        extract_path = extracts_dir.parent / pdf_extract_ref
        if not extract_path.exists():
            # Try just the filename in year-based dirs
            parts = pdf_extract_ref.split('/')
            if len(parts) >= 2:
                extract_path = extracts_dir / parts[-2] / parts[-1]

        authors = parse_authors_from_extract(extract_path)
        if len(authors) >= 2:
            result['proposed_authors'] = authors
            result['source'] = 'pdf_extract'
            result['confidence'] = 'medium' if len(authors) <= 10 else 'low'
            print(f"  PDF extract → {len(authors)} authors: {authors[:5]}...")
            return result
        elif authors:
            print(f"  PDF extract → only {len(authors)} author(s), trying fallbacks...")

    # Strategy 2: arXiv API (if arXiv URL)
    if 'arxiv.org' in url:
        authors = query_arxiv(url)
        if len(authors) >= 2:
            result['proposed_authors'] = authors
            result['source'] = 'arxiv'
            result['confidence'] = 'high'
            print(f"  arXiv → {len(authors)} authors: {authors[:5]}...")
            return result

    # Strategy 3: Semantic Scholar
    if title:
        authors = query_semantic_scholar(title)
        if len(authors) >= 2:
            result['proposed_authors'] = authors
            result['source'] = 'semantic_scholar'
            result['confidence'] = 'high'
            print(f"  Semantic Scholar → {len(authors)} authors: {authors[:5]}...")
            return result

    print(f"  No authors found via any strategy")
    return result


def main():
    parser = argparse.ArgumentParser(description="Extract authors from PDF extracts")
    parser.add_argument('--batch', type=int, default=None,
                        help="Batch number (1-indexed)")
    parser.add_argument('--num-batches', type=int, default=1,
                        help="Total number of batches")
    args = parser.parse_args()

    # Find all incomplete papers
    incomplete = find_incomplete_papers(PAPERS_DIR)
    print(f"Found {len(incomplete)} papers with authors_incomplete: true")

    # Batch selection
    if args.batch is not None:
        batch_size = len(incomplete) // args.num_batches
        start = (args.batch - 1) * batch_size
        end = start + batch_size if args.batch < args.num_batches else len(incomplete)
        incomplete = incomplete[start:end]
        print(f"Batch {args.batch}/{args.num_batches}: processing papers {start+1}-{end}")

    # Process each paper
    results = []
    for paper in incomplete:
        result = process_paper(paper, PDF_EXTRACTS_DIR)
        results.append(result)

    # Summary
    found = [r for r in results if r['proposed_authors']]
    by_source = {}
    for r in found:
        src = r['source']
        by_source[src] = by_source.get(src, 0) + 1

    print(f"\n{'=' * 60}")
    print(f"SUMMARY")
    print(f"{'=' * 60}")
    print(f"  Processed: {len(results)}")
    print(f"  Authors found: {len(found)}")
    print(f"  No result: {len(results) - len(found)}")
    print(f"  By source: {by_source}")

    # Save results
    today = datetime.now().strftime('%Y%m%d')
    batch_suffix = f"_batch{args.batch:02d}" if args.batch else ""
    output_path = LOGS_DIR / f"{today}-author_extraction_results{batch_suffix}.json"
    output_path.write_text(json.dumps(results, indent=2, ensure_ascii=False),
                           encoding='utf-8')
    print(f"\nResults saved to: {output_path}")


if __name__ == "__main__":
    main()
