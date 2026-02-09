#!/usr/bin/env python3
"""
Phase 1: Build Comprehensive Author-Paper Map

Reads all papers, extracts author lists, identifies first/last authors,
resolves "et al." via APIs, and captures affiliations from PDF extracts.

USAGE:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/build_author_paper_map.py
    ../.venv/bin/python PYTHON/build_author_paper_map.py --dry-run
    ../.venv/bin/python PYTHON/build_author_paper_map.py --skip-api  # local only, no API calls
"""

import re
import json
import sys
import os
import time
import functools
from pathlib import Path
from typing import List, Optional, Dict, Tuple

# Force flush for parallel/background usage
import builtins
print = functools.partial(builtins.print, flush=True)

sys.path.insert(0, str(Path(__file__).parent))
from vault_config import PAPERS_DIR, LOGS_DIR, PDF_EXTRACTS_DIR

# Import API fetchers
from expand_author_lists import ArxivAuthorFetcher, CrossrefAuthorFetcher, PubmedAuthorFetcher

# Date prefix for output files
from datetime import date
DATE_PREFIX = date.today().strftime("%Y%m%d")

# Output files
MAP_OUTPUT = LOGS_DIR / f"{DATE_PREFIX}-author_paper_map.json"
AFFILIATIONS_OUTPUT = LOGS_DIR / f"{DATE_PREFIX}-author_affiliations.json"


# =============================================================================
# AUTHOR PARSING
# =============================================================================

def parse_authors_field(authors_str: str) -> List[str]:
    """
    Parse the authors YAML field into a list of individual author names.

    Handles:
    - Semicolon-separated: "Author A; Author B; Author C"
    - "et al." truncation: "Author A et al."
    - Wikilink syntax: "[[Author A]]"
    - "LastName, FirstName" format from CrossRef
    """
    if not authors_str or not authors_str.strip():
        return []

    raw = authors_str.strip().strip('"')

    # Check for "et al." — return what we have, flagging as incomplete
    has_et_al = bool(re.search(r'\bet\s*al\.?\b', raw, re.IGNORECASE))

    # Remove "et al." for parsing the known authors
    cleaned = re.sub(r',?\s*\bet\s*al\.?\b', '', raw, flags=re.IGNORECASE).strip()
    # Remove trailing punctuation from cleanup
    cleaned = cleaned.rstrip(',;').strip()

    # Split by semicolons (primary separator in this vault)
    if ';' in cleaned:
        parts = [p.strip() for p in cleaned.split(';')]
    else:
        # Fallback: comma-separated, but be careful with "LastName, FirstName" format
        # If we see a pattern like "Name, N." or "Name, Name" repeated, treat commas as separators
        parts = smart_comma_split(cleaned)

    # Clean each author name
    authors = []
    for part in parts:
        name = clean_author_name(part)
        if name and name.lower() not in ('unknown', 'et al', 'et al.', 'others', 'n/a'):
            authors.append(name)

    return authors


def smart_comma_split(text: str) -> List[str]:
    """
    Split comma-separated author list, handling "LastName, FirstName" patterns.

    Heuristic: If the text has the pattern "Word, Word; Word, Word" it's semicolon-separated
    (already handled). For comma-only, check if it looks like "Last, First, Last, First"
    or "First Last, First Last".
    """
    parts = [p.strip() for p in text.split(',')]

    if len(parts) <= 1:
        return parts

    # Check if this looks like "LastName, FirstName" pairs
    # Pattern: short-word, short-word-or-initial, short-word, ...
    # If alternating parts look like (surname, given-name), merge them
    looks_like_pairs = True
    if len(parts) >= 2:
        # Check first pair: if parts[1] looks like a first name (short, not capitalized surname-like)
        for i in range(0, len(parts) - 1, 2):
            surname = parts[i].strip()
            given = parts[i + 1].strip() if i + 1 < len(parts) else ""
            # If the "given" part starts with a capital and is short, likely a first name
            if given and re.match(r'^[A-Z][a-z]', given):
                continue
            # If it has initials
            if given and re.match(r'^[A-Z]\.', given):
                continue
            looks_like_pairs = False
            break

    if looks_like_pairs and len(parts) >= 2 and len(parts) % 2 == 0:
        # Merge pairs: "LastName, FirstName" → "FirstName LastName"
        merged = []
        for i in range(0, len(parts), 2):
            surname = parts[i].strip()
            given = parts[i + 1].strip() if i + 1 < len(parts) else ""
            if given:
                merged.append(f"{given} {surname}")
            else:
                merged.append(surname)
        return merged

    # Otherwise treat each comma-separated item as a separate author
    return parts


def clean_author_name(name: str) -> str:
    """Clean and normalize a single author name."""
    if not name:
        return ""

    # Remove wikilink syntax
    name = re.sub(r'\[\[|\]\]', '', name)

    # Remove leading/trailing quotes
    name = name.strip().strip('"\'')

    # Remove invalid filename chars
    name = re.sub(r'[<>:"/\\|?*]', '', name)

    # Collapse multiple spaces
    name = re.sub(r'\s+', ' ', name).strip()

    # If format is "LastName, FirstName" and not an initial-only pattern, normalize
    # But preserve the original format in the map — normalization happens in Phase 2

    return name


def has_et_al(authors_str: str) -> bool:
    """Check if an authors string contains 'et al.' truncation."""
    if not authors_str:
        return False
    return bool(re.search(r'\bet\s*al\.?\b', authors_str, re.IGNORECASE))


# =============================================================================
# API RESOLUTION FOR "ET AL." PAPERS
# =============================================================================

def extract_doi_from_url(url: str) -> Optional[str]:
    """Extract DOI from a URL."""
    if not url:
        return None
    # Match DOI patterns in URLs
    match = re.search(r'(?:doi\.org/|doi:\s*)(10\.\d{4,}/[^\s]+)', url)
    if match:
        return match.group(1).rstrip('.')
    return None


def extract_arxiv_id_from_url(url: str) -> Optional[str]:
    """Extract arXiv ID from a URL, avoiding DOI substring false matches."""
    if not url:
        return None
    # Only match in arxiv.org URLs to avoid DOI substring matches
    if 'arxiv.org' not in url:
        return None
    return ArxivAuthorFetcher.extract_arxiv_id(url)


def normalize_api_author_name(name: str, source: str) -> str:
    """
    Normalize an author name from API results.

    CrossRef returns "Family, Given" format.
    arXiv/Semantic Scholar return "Given Family" format.
    """
    name = name.strip()

    if source == 'crossref':
        # CrossRef: "Family, Given" → keep as-is for now, disambiguation handles normalization
        # Actually, convert to "Given Family" for consistency with vault convention
        if ',' in name:
            parts = [p.strip() for p in name.split(',', 1)]
            if len(parts) == 2 and parts[1]:
                return f"{parts[1]} {parts[0]}"
        return name

    # arXiv and Semantic Scholar already return "Given Family" format
    return name


def resolve_et_al_via_apis(paper_info: Dict, skip_api: bool = False) -> Optional[Dict]:
    """
    Attempt to resolve "et al." for a paper using multiple API sources.

    Returns dict with 'authors' and 'source' keys, or None if all fail.
    """
    if skip_api:
        return None

    url = paper_info.get('url', '')
    doi = paper_info.get('doi', '') or extract_doi_from_url(url)

    # Strategy 1: arXiv API
    arxiv_id = extract_arxiv_id_from_url(url)
    if not arxiv_id:
        # Try external_pdf
        arxiv_id = extract_arxiv_id_from_url(paper_info.get('external_pdf', ''))
    if arxiv_id:
        print(f"  Trying arXiv API ({arxiv_id})...", end=" ")
        result = ArxivAuthorFetcher.fetch_authors(arxiv_id)
        if result and result.authors:
            authors = [normalize_api_author_name(a, 'arxiv') for a in result.authors]
            print(f"Found {len(authors)} authors")
            time.sleep(ArxivAuthorFetcher.RATE_LIMIT)
            return {'authors': authors, 'source': 'arxiv'}
        print("failed")
        time.sleep(ArxivAuthorFetcher.RATE_LIMIT)

    # Strategy 2: CrossRef API (via DOI)
    if doi:
        print(f"  Trying CrossRef API ({doi})...", end=" ")
        result = CrossrefAuthorFetcher.fetch_authors(doi)
        if result and result.authors:
            authors = [normalize_api_author_name(a, 'crossref') for a in result.authors]
            print(f"Found {len(authors)} authors")
            time.sleep(CrossrefAuthorFetcher.RATE_LIMIT)
            return {'authors': authors, 'source': 'crossref'}
        print("failed")
        time.sleep(CrossrefAuthorFetcher.RATE_LIMIT)

    # Strategy 3: Semantic Scholar API
    if doi:
        print(f"  Trying Semantic Scholar ({doi})...", end=" ")
        authors = fetch_semantic_scholar_authors(doi)
        if authors:
            print(f"Found {len(authors)} authors")
            return {'authors': authors, 'source': 'semantic_scholar'}
        print("failed")

    # Strategy 4: Try Semantic Scholar by title
    title = paper_info.get('short_title', '')
    if title and len(title) > 10:
        print(f"  Trying Semantic Scholar by title...", end=" ")
        authors = fetch_semantic_scholar_by_title(title)
        if authors:
            print(f"Found {len(authors)} authors")
            return {'authors': authors, 'source': 'semantic_scholar_title'}
        print("failed")

    return None


def fetch_semantic_scholar_authors(doi: str) -> Optional[List[str]]:
    """Fetch authors from Semantic Scholar API by DOI."""
    import urllib.request
    import urllib.error

    try:
        url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=authors"
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'CEI-Literature-Vault/1.0')

        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))

        if 'authors' in data:
            return [a['name'] for a in data['authors'] if a.get('name')]

        return None
    except Exception:
        return None
    finally:
        time.sleep(10)  # Aggressive rate limit


def fetch_semantic_scholar_by_title(title: str) -> Optional[List[str]]:
    """Fetch authors from Semantic Scholar API by title search."""
    import urllib.request
    import urllib.error
    import urllib.parse

    try:
        encoded = urllib.parse.quote(title)
        url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={encoded}&limit=1&fields=authors,title"
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'CEI-Literature-Vault/1.0')

        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))

        if 'data' in data and data['data']:
            paper = data['data'][0]
            # Verify title similarity
            if title_similarity(title, paper.get('title', '')) > 0.6:
                if 'authors' in paper:
                    return [a['name'] for a in paper['authors'] if a.get('name')]

        return None
    except Exception:
        return None
    finally:
        time.sleep(10)  # Aggressive rate limit


def title_similarity(a: str, b: str) -> float:
    """Simple word-overlap title similarity."""
    words_a = set(re.findall(r'\w+', a.lower()))
    words_b = set(re.findall(r'\w+', b.lower()))
    if not words_a or not words_b:
        return 0.0
    intersection = words_a & words_b
    union = words_a | words_b
    return len(intersection) / len(union)


# =============================================================================
# PDF EXTRACT AFFILIATION PARSING
# =============================================================================

def parse_affiliations_from_extract(extract_path: Path) -> Optional[Dict]:
    """
    Parse affiliations and emails from the first ~3000 chars of a PDF extract.

    Returns dict with 'affiliations' list and 'emails' list, or None.
    """
    if not extract_path or not Path(extract_path).exists():
        return None

    try:
        text = Path(extract_path).read_text(encoding='utf-8')[:3000]
    except Exception:
        return None

    result = {'affiliations': [], 'emails': []}

    # Extract emails
    emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.]+', text)
    result['emails'] = list(set(emails))

    # Extract affiliations: look for university/institute/lab patterns
    affil_patterns = [
        r'(?:University|Institute|College|School|Lab(?:oratory)?|Department|Centre|Center|'
        r'Faculty|Academy|Research\s+(?:Group|Center|Institute))'
        r'[^.\n]{0,100}',
    ]
    for pattern in affil_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for m in matches:
            cleaned = m.strip().rstrip(',;.')
            if len(cleaned) > 10 and cleaned not in result['affiliations']:
                result['affiliations'].append(cleaned)

    if result['affiliations'] or result['emails']:
        return result
    return None


# =============================================================================
# MAIN PIPELINE
# =============================================================================

def extract_frontmatter_fields(content: str) -> Dict[str, str]:
    """Extract key YAML frontmatter fields from paper content."""
    fields = {}

    # Extract frontmatter block
    if not content.startswith('---'):
        return fields

    match = re.search(r'\n---\s*\n', content[3:])
    if not match:
        return fields

    fm_text = content[3:match.start() + 3]

    # Parse key fields
    for key in ['authors', 'first_author', 'short_title', 'url', 'external_pdf',
                'doi', 'pdf_extract', 'year', 'local_pdf']:
        pattern = rf'^{re.escape(key)}:\s*(.+)$'
        m = re.search(pattern, fm_text, re.MULTILINE)
        if m:
            val = m.group(1).strip().strip('"')
            fields[key] = val

    return fields


def build_extract_path(pdf_extract_field: str) -> Optional[Path]:
    """Convert pdf_extract YAML field to actual file path."""
    if not pdf_extract_field or pdf_extract_field in ('N/A', 'PENDING'):
        return None

    # Sanity check: must look like a path, not an abstract or other text
    if len(pdf_extract_field) > 300 or '\n' in pdf_extract_field:
        return None
    if not pdf_extract_field.strip().startswith('PDF Extracts'):
        return None

    # Remove wikilink syntax
    path_str = re.sub(r'\[\[|\]\]', '', pdf_extract_field)

    # Build full path relative to workspace
    try:
        full_path = PAPERS_DIR.parent / path_str
        if full_path.exists():
            return full_path
    except (OSError, ValueError):
        return None

    return None


def build_author_paper_map(skip_api: bool = False, dry_run: bool = False):
    """Main function: build the comprehensive author-paper map."""

    papers = sorted(PAPERS_DIR.glob('*.md'))
    print(f"Found {len(papers)} papers to process")

    author_paper_map = {}
    et_al_papers = []
    affiliations_map = {}

    # =========================================================================
    # PASS 1: Parse all papers
    # =========================================================================
    print("\n=== PASS 1: Parsing all papers ===")

    for paper_file in papers:
        stem = paper_file.stem
        content = paper_file.read_text(encoding='utf-8')
        fields = extract_frontmatter_fields(content)

        authors_str = fields.get('authors', '')
        first_author_str = fields.get('first_author', '')
        short_title = fields.get('short_title', stem)

        # Parse authors
        authors = parse_authors_field(authors_str)
        is_et_al = has_et_al(authors_str)

        # Determine first/last author
        first_author = None
        last_author = None

        if first_author_str:
            first_author = clean_author_name(first_author_str)

        if authors:
            if not first_author:
                first_author = authors[0]
            last_author = authors[-1] if len(authors) > 1 else authors[0]

        entry = {
            'authors': authors,
            'first_author': first_author,
            'last_author': last_author,
            'short_title': short_title,
            'et_al_original': is_et_al,
            'et_al_resolved': False,
            'resolution_source': None,
            'authors_str_original': authors_str,
        }

        # Carry forward fields needed for API resolution
        if is_et_al:
            entry['_url'] = fields.get('url', '')
            entry['_external_pdf'] = fields.get('external_pdf', '')
            entry['_doi'] = fields.get('doi', '')
            et_al_papers.append((stem, entry))

        author_paper_map[stem] = entry

        # Parse affiliations from PDF extract
        extract_path = build_extract_path(fields.get('pdf_extract', ''))
        if extract_path:
            affils = parse_affiliations_from_extract(extract_path)
            if affils:
                affiliations_map[stem] = affils

    print(f"  Parsed {len(author_paper_map)} papers")
    print(f"  Found {len(et_al_papers)} papers with 'et al.' to resolve")
    print(f"  Found {len(affiliations_map)} papers with affiliations/emails")

    # =========================================================================
    # PASS 2: Resolve "et al." papers via APIs
    # =========================================================================
    if et_al_papers and not skip_api:
        print(f"\n=== PASS 2: Resolving {len(et_al_papers)} 'et al.' papers via APIs ===")

        resolved = 0
        failed = 0

        for i, (stem, entry) in enumerate(et_al_papers, 1):
            print(f"\n[{i}/{len(et_al_papers)}] {stem}")

            paper_info = {
                'url': entry.get('_url', ''),
                'external_pdf': entry.get('_external_pdf', ''),
                'doi': entry.get('_doi', ''),
                'short_title': entry.get('short_title', ''),
            }

            result = resolve_et_al_via_apis(paper_info, skip_api=dry_run)

            if result:
                new_authors = result['authors']
                entry['authors'] = new_authors
                entry['first_author'] = new_authors[0] if new_authors else entry['first_author']
                entry['last_author'] = new_authors[-1] if len(new_authors) > 1 else (new_authors[0] if new_authors else entry['last_author'])
                entry['et_al_resolved'] = True
                entry['resolution_source'] = result['source']
                resolved += 1
            else:
                failed += 1

        print(f"\n  Resolved: {resolved}, Failed: {failed}")
    elif et_al_papers:
        print(f"\n=== PASS 2: Skipping API resolution (--skip-api mode) ===")

    # =========================================================================
    # CLEANUP: Remove internal fields before saving
    # =========================================================================
    for stem, entry in author_paper_map.items():
        for key in list(entry.keys()):
            if key.startswith('_'):
                del entry[key]

    # =========================================================================
    # SAVE OUTPUTS
    # =========================================================================
    print(f"\n=== Saving outputs ===")

    # Save author-paper map
    tmp_map = MAP_OUTPUT.parent / f".tmp.{os.getpid()}.map.json"
    with open(tmp_map, 'w', encoding='utf-8') as f:
        json.dump(author_paper_map, f, indent=2, ensure_ascii=False)
    os.replace(tmp_map, MAP_OUTPUT)
    print(f"  Author-paper map: {MAP_OUTPUT.name} ({len(author_paper_map)} papers)")

    # Save affiliations
    if affiliations_map:
        tmp_aff = AFFILIATIONS_OUTPUT.parent / f".tmp.{os.getpid()}.aff.json"
        with open(tmp_aff, 'w', encoding='utf-8') as f:
            json.dump(affiliations_map, f, indent=2, ensure_ascii=False)
        os.replace(tmp_aff, AFFILIATIONS_OUTPUT)
        print(f"  Affiliations: {AFFILIATIONS_OUTPUT.name} ({len(affiliations_map)} papers)")

    # =========================================================================
    # SUMMARY STATISTICS
    # =========================================================================
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    total = len(author_paper_map)
    with_authors = sum(1 for e in author_paper_map.values() if e['authors'])
    et_al_total = sum(1 for e in author_paper_map.values() if e['et_al_original'])
    et_al_resolved = sum(1 for e in author_paper_map.values() if e['et_al_resolved'])
    with_first = sum(1 for e in author_paper_map.values() if e['first_author'])
    with_last = sum(1 for e in author_paper_map.values() if e['last_author'])

    # Count unique authors
    all_authors = set()
    for entry in author_paper_map.values():
        for author in entry['authors']:
            all_authors.add(author)

    print(f"Total papers:          {total}")
    print(f"Papers with authors:   {with_authors}")
    print(f"Papers with et al.:    {et_al_total}")
    print(f"  Resolved via API:    {et_al_resolved}")
    print(f"  Still unresolved:    {et_al_total - et_al_resolved}")
    print(f"Papers with first_author: {with_first}")
    print(f"Papers with last_author:  {with_last}")
    print(f"Unique author names:   {len(all_authors)}")
    print(f"Affiliations found:    {len(affiliations_map)}")
    print("=" * 60)


def main():
    skip_api = '--skip-api' in sys.argv
    dry_run = '--dry-run' in sys.argv

    if dry_run:
        print("=== DRY RUN MODE (API calls skipped) ===\n")
        skip_api = True

    build_author_paper_map(skip_api=skip_api, dry_run=dry_run)


if __name__ == '__main__':
    main()
