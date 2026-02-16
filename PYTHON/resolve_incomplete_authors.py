#!/usr/bin/env python3
"""
Resolve Incomplete Author Lists

Scans all 69 papers with `authors_incomplete: true` and attempts to resolve
the full author list using CrossRef, arXiv, and Semantic Scholar APIs.

When a full author list is found:
  - Replaces the `authors:` line with wikilinked author names
  - Sets `authors_incomplete: false`
  - Updates `first_author:` and `last_author:` fields
  - Updates the body's "## Authors" section and "**Authors:**" metadata line

YAML SAFETY: Uses safe regex replacement — never parse/rebuild round-trip.

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/resolve_incomplete_authors.py
    ../.venv/bin/python PYTHON/resolve_incomplete_authors.py --dry-run
"""

import functools
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Force flush for progress output
print = functools.partial(print, flush=True)

# --- Path setup ---
SCRIPT_DIR = Path(__file__).parent.resolve()
WORKSPACE_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from vault_config import PAPERS_DIR, LOGS_DIR

# --- Constants ---
DATE_PREFIX = date.today().strftime("%Y%m%d")
OUTPUT_JSON = LOGS_DIR / f"{DATE_PREFIX}-incomplete_authors_resolved.json"

CROSSREF_API = "https://api.crossref.org/works"
SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/graph/v1/paper"
ARXIV_API = "http://export.arxiv.org/api/query"

USER_AGENT = "CEI-Literature-Vault/1.0 (mailto:cei-vault@example.com)"

# Rate limits (seconds)
CROSSREF_DELAY = 1.0
SEMANTIC_SCHOLAR_DELAY = 3.0
ARXIV_DELAY = 3.0


# =============================================================================
# YAML FIELD PARSING (read-only, regex-based)
# =============================================================================

def extract_yaml_field(content: str, field: str) -> str:
    """Extract a single YAML field value from file content. Returns empty string if not found."""
    m = re.search(rf'^{re.escape(field)}:\s*(.*)', content, re.MULTILINE)
    if m:
        val = m.group(1).strip().strip('"')
        return val
    return ""


def extract_frontmatter_text(content: str) -> Tuple[str, str]:
    """Split content into frontmatter and body. Returns (frontmatter, body)."""
    m = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if m:
        return m.group(1), content[m.end():]
    return "", content


# =============================================================================
# AUTHOR NAME FORMATTING
# =============================================================================

def clean_author_for_yaml(name: str) -> str:
    """
    Clean an author name for use in YAML wikilink fields.
    Removes artifacts from API responses and normalizes.
    """
    name = re.sub(r'\[\[|\]\]', '', name).strip()
    # Remove "and " prefix
    name = re.sub(r'^and\s+', '', name, flags=re.IGNORECASE)
    # Remove double-period artifacts
    name = name.replace('..', '.')
    # Remove trailing period (but NOT on abbreviations like "J.")
    if name.endswith('.') and len(name) > 2 and name[-2] != ' ':
        name = name.rstrip('.')
    # Remove trailing comma/semicolon
    name = name.rstrip(',;')
    # Replace double quotes with single quotes (YAML safety)
    name = name.replace('"', "'")
    # Collapse multiple spaces
    name = re.sub(r'\s+', ' ', name).strip()
    return name


def format_author_for_wikilink(name: str) -> str:
    """
    Format an API-returned author name as a wikilink: [[Last, First]].

    API sources return "First Last" format.
    CrossRef returns "Given Family" (already converted) or "Family, Given".
    We convert to "Last, First" format for consistency with vault convention.
    """
    name = clean_author_for_yaml(name)
    if not name:
        return ""

    # If already in "Last, First" format (has comma), keep it
    if ',' in name:
        return f"[[{name}]]"

    # Convert "First Middle Last" → "Last, First Middle"
    parts = name.split()
    if len(parts) >= 2:
        last = parts[-1]
        first_middle = ' '.join(parts[:-1])
        return f"[[{last}, {first_middle}]]"

    # Single name — use as-is
    return f"[[{name}]]"


def format_authors_yaml(author_names: List[str]) -> str:
    """
    Format a list of author names into the YAML authors field value.
    Returns: "[[Last, First]]; [[Last, First]]; ..."
    """
    wikilinks = []
    for name in author_names:
        wl = format_author_for_wikilink(name)
        if wl:
            wikilinks.append(wl)
    return "; ".join(wikilinks)


def format_authors_body(author_names: List[str]) -> str:
    """
    Format author names for the body's ## Authors section.
    Returns: "[[Last, First]], [[Last, First]], ..."
    """
    wikilinks = []
    for name in author_names:
        wl = format_author_for_wikilink(name)
        if wl:
            wikilinks.append(wl)
    return ", ".join(wikilinks)


def format_authors_metadata(author_names: List[str]) -> str:
    """
    Format author names for the **Authors:** metadata line in the body.
    Returns: "Last, First; Last, First; ..."
    """
    formatted = []
    for name in author_names:
        clean = clean_author_for_yaml(name)
        if not clean:
            continue
        # Convert "First Last" → "Last, First" if not already
        if ',' not in clean:
            parts = clean.split()
            if len(parts) >= 2:
                clean = f"{parts[-1]}, {' '.join(parts[:-1])}"
        formatted.append(clean)
    return "; ".join(formatted)


def extract_last_from_wikilink(wikilink: str) -> str:
    """Extract last name from a wikilink like '[[Last, First]]' or '[[First Last]]'."""
    name = re.sub(r'\[\[|\]\]', '', wikilink).strip()
    if ',' in name:
        return name.split(',')[0].strip()
    parts = name.split()
    return parts[-1] if parts else name


def validate_first_author_match(existing_first: str, resolved_authors: List[str]) -> bool:
    """
    Safety check: verify the existing first_author last name appears somewhere
    in the resolved author list. Prevents applying wrong authors when arXiv IDs
    point to different papers.

    Returns True if match found (safe to apply), False if mismatch.
    """
    existing_last = extract_last_from_wikilink(existing_first).lower().strip('.')
    if not existing_last or existing_last in ('unknown', 'various', 'anonymous', 'project',
                                               'consortium', 'center', 'institute', 'jigsaw',
                                               'mlcommons', 'thedevastator', 'aakanksha'):
        # Generic/placeholder names — skip validation
        return True

    for author in resolved_authors:
        clean = clean_author_for_yaml(author).lower()
        # Check if the existing last name appears as a word in any resolved author
        if re.search(rf'\b{re.escape(existing_last)}\b', clean):
            return True
    return False


# =============================================================================
# API: CrossRef
# =============================================================================

def fetch_crossref_authors(doi: str) -> Optional[List[str]]:
    """Fetch authors from CrossRef API by DOI. Returns list of 'First Last' names."""
    if not doi or doi == "N/A":
        return None
    try:
        url = f"{CROSSREF_API}/{urllib.parse.quote(doi, safe='')}"
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=15) as resp:
            if resp.status != 200:
                return None
            data = json.loads(resp.read().decode("utf-8"))

        message = data.get("message", {})
        cr_authors = message.get("author", [])
        if not cr_authors:
            return None

        authors = []
        for a in cr_authors:
            given = a.get("given", "").strip()
            family = a.get("family", "").strip()
            if family:
                if given:
                    authors.append(f"{given} {family}")
                else:
                    authors.append(family)

        return authors if authors else None
    except Exception as e:
        print(f"    CrossRef error for {doi}: {e}")
        return None


# =============================================================================
# API: Semantic Scholar
# =============================================================================

def fetch_semantic_scholar_by_title(title: str) -> Optional[List[str]]:
    """Fetch authors from Semantic Scholar by title search. Returns 'First Last' names."""
    if not title or len(title) < 5:
        return None
    try:
        # Clean title: remove parenthetical qualifiers, quotes, punctuation artifacts
        clean_title = re.sub(r'\(.*?\)', '', title).strip()
        clean_title = re.sub(r'["\']', '', clean_title).strip()
        # Remove trailing "et al." patterns
        clean_title = re.sub(r'\s+et\s+al\.?\s*$', '', clean_title, flags=re.IGNORECASE)

        encoded = urllib.parse.quote(clean_title)
        url = f"{SEMANTIC_SCHOLAR_API}/search?query={encoded}&limit=3&fields=authors,title"
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=15) as resp:
            if resp.status != 200:
                return None
            data = json.loads(resp.read().decode("utf-8"))

        if "data" not in data or not data["data"]:
            return None

        # Find best matching result by title similarity
        best_match = None
        best_sim = 0.0
        for paper in data["data"]:
            sim = title_similarity(clean_title, paper.get("title", ""))
            if sim > best_sim:
                best_sim = sim
                best_match = paper

        if best_match and best_sim >= 0.5:
            authors = []
            for a in best_match.get("authors", []):
                name = a.get("name", "").strip()
                if name:
                    authors.append(name)
            return authors if authors else None

        return None
    except Exception as e:
        print(f"    Semantic Scholar title search error: {e}")
        return None


# =============================================================================
# API: arXiv
# =============================================================================

def extract_arxiv_id(url: str) -> Optional[str]:
    """Extract arXiv ID from a URL. Only matches arxiv.org URLs to avoid DOI false matches."""
    if not url:
        return None
    if "arxiv.org" not in url:
        return None
    m = re.search(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})', url)
    if m:
        arxiv_id = m.group(1)
        # Validate YYMM prefix (years 07-26, months 01-12)
        yy = int(arxiv_id[:2])
        mm = int(arxiv_id[2:4])
        if 7 <= yy <= 26 and 1 <= mm <= 12:
            return arxiv_id
    return None


def fetch_arxiv_authors(arxiv_id: str) -> Optional[List[str]]:
    """Fetch authors from arXiv API using id_list parameter. Returns 'First Last' names."""
    if not arxiv_id:
        return None
    try:
        url = f"{ARXIV_API}?id_list={arxiv_id}&max_results=1"
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=15) as resp:
            if resp.status != 200:
                return None
            xml_data = resp.read()

        root = ET.fromstring(xml_data)
        ns = {"atom": "http://www.w3.org/2005/Atom"}

        authors = []
        for entry in root.findall("atom:entry", ns):
            for author_elem in entry.findall("atom:author", ns):
                name_elem = author_elem.find("atom:name", ns)
                if name_elem is not None and name_elem.text:
                    authors.append(name_elem.text.strip())

        return authors if authors else None
    except Exception as e:
        print(f"    arXiv API error for {arxiv_id}: {e}")
        return None


# =============================================================================
# TITLE SIMILARITY
# =============================================================================

def title_similarity(a: str, b: str) -> float:
    """Simple word-overlap title similarity (Jaccard)."""
    words_a = set(re.findall(r'\w+', a.lower()))
    words_b = set(re.findall(r'\w+', b.lower()))
    if not words_a or not words_b:
        return 0.0
    intersection = words_a & words_b
    union = words_a | words_b
    return len(intersection) / len(union)


# =============================================================================
# PAPER SCANNING
# =============================================================================

def find_incomplete_papers() -> List[Dict]:
    """Find all papers with authors_incomplete: true."""
    papers = []
    for paper_path in sorted(PAPERS_DIR.glob("*.md")):
        content = paper_path.read_text(encoding="utf-8")
        if "authors_incomplete: true" not in content:
            continue

        papers.append({
            "filename": paper_path.name,
            "path": str(paper_path),
            "short_title": extract_yaml_field(content, "short_title"),
            "authors": extract_yaml_field(content, "authors"),
            "first_author": extract_yaml_field(content, "first_author"),
            "last_author": extract_yaml_field(content, "last_author"),
            "doi": extract_yaml_field(content, "doi"),
            "url": extract_yaml_field(content, "url"),
            "external_pdf": extract_yaml_field(content, "external_pdf"),
        })

    return papers


# =============================================================================
# RESOLUTION PIPELINE
# =============================================================================

def resolve_paper(paper: Dict) -> Dict:
    """
    Try to resolve full author list for a paper via APIs.

    Returns result dict with status, resolved authors, and source.
    """
    result = {
        "filename": paper["filename"],
        "original_authors": paper["authors"],
        "resolved_authors": [],
        "source": "unresolved",
        "status": "unresolved",
        "error": "",
    }

    # --- Strategy 1: CrossRef (if DOI exists) ---
    doi = paper.get("doi", "")
    if doi and doi != "N/A":
        print(f"    [CrossRef] Querying DOI: {doi} ...")
        authors = fetch_crossref_authors(doi)
        if authors and len(authors) >= 2:
            result["resolved_authors"] = authors
            result["source"] = "crossref"
            result["status"] = "resolved"
            print(f"    [CrossRef] Found {len(authors)} authors")
            time.sleep(CROSSREF_DELAY)
            return result
        time.sleep(CROSSREF_DELAY)

    # --- Strategy 1.5: CrossRef with ACL-derived DOI ---
    acl_doi = paper.get("acl_derived_doi", "")
    if acl_doi and acl_doi != doi:
        print(f"    [CrossRef/ACL] Querying derived DOI: {acl_doi} ...")
        authors = fetch_crossref_authors(acl_doi)
        if authors and len(authors) >= 2:
            result["resolved_authors"] = authors
            result["source"] = "crossref_acl"
            result["status"] = "resolved"
            print(f"    [CrossRef/ACL] Found {len(authors)} authors")
            time.sleep(CROSSREF_DELAY)
            return result
        time.sleep(CROSSREF_DELAY)

    # --- Strategy 2: arXiv (if arXiv URL exists) ---
    arxiv_id = extract_arxiv_id(paper.get("url", ""))
    if not arxiv_id:
        arxiv_id = extract_arxiv_id(paper.get("external_pdf", ""))
    if arxiv_id:
        print(f"    [arXiv] Querying ID: {arxiv_id} ...")
        authors = fetch_arxiv_authors(arxiv_id)
        if authors and len(authors) >= 2:
            result["resolved_authors"] = authors
            result["source"] = "arxiv"
            result["status"] = "resolved"
            print(f"    [arXiv] Found {len(authors)} authors")
            time.sleep(ARXIV_DELAY)
            return result
        time.sleep(ARXIV_DELAY)

    # --- Strategy 3: Semantic Scholar (by title) ---
    title = paper.get("short_title", "")
    if title:
        print(f"    [S2] Searching title: {title[:60]} ...")
        authors = fetch_semantic_scholar_by_title(title)
        if authors and len(authors) >= 2:
            result["resolved_authors"] = authors
            result["source"] = "semantic_scholar"
            result["status"] = "resolved"
            print(f"    [S2] Found {len(authors)} authors")
            time.sleep(SEMANTIC_SCHOLAR_DELAY)
            return result
        time.sleep(SEMANTIC_SCHOLAR_DELAY)

    # --- Unresolved ---
    result["error"] = "All API strategies exhausted"
    return result


# =============================================================================
# SAFE YAML + BODY UPDATE
# =============================================================================

def apply_resolution(paper_path: Path, author_names: List[str], dry_run: bool = False) -> bool:
    """
    Apply resolved author list to a paper file using safe regex replacement.

    Updates:
    - authors: field (wikilinked)
    - authors_incomplete: true → false
    - first_author: field
    - last_author: field
    - Body ## Authors section
    - Body **Authors:** metadata line

    Returns True if changes were applied (or would be in dry-run).
    """
    content = paper_path.read_text(encoding="utf-8")

    # --- 1. Replace authors: line ---
    authors_yaml_value = format_authors_yaml(author_names)
    # The authors field may or may not be quoted in the original
    new_authors_line = f'authors: "{authors_yaml_value}"'
    content, n1 = re.subn(
        r'^authors:.*$',
        new_authors_line,
        content, count=1, flags=re.MULTILINE
    )
    if n1 == 0:
        print(f"    WARNING: Could not find authors: line in {paper_path.name}")
        return False

    # --- 2. Replace authors_incomplete: true → false ---
    content, n2 = re.subn(
        r'^authors_incomplete:.*$',
        'authors_incomplete: false',
        content, count=1, flags=re.MULTILINE
    )
    if n2 == 0:
        print(f"    WARNING: Could not find authors_incomplete: line in {paper_path.name}")

    # --- 3. Update first_author: field ---
    first_wikilink = format_author_for_wikilink(author_names[0])
    new_first = f'first_author: "{first_wikilink}"'
    content, _ = re.subn(
        r'^first_author:.*$',
        new_first,
        content, count=1, flags=re.MULTILINE
    )

    # --- 4. Update last_author: field ---
    last_wikilink = format_author_for_wikilink(author_names[-1])
    new_last = f'last_author: "{last_wikilink}"'
    content, _ = re.subn(
        r'^last_author:.*$',
        new_last,
        content, count=1, flags=re.MULTILINE
    )

    # --- 5. Update body ## Authors section ---
    # Pattern: "## Authors\n\n<one or more wikilink lines>\n"
    authors_body = format_authors_body(author_names)
    content = re.sub(
        r'(## Authors\n\n).*?(\n\n)',
        rf'\g<1>{authors_body}\g<2>',
        content, count=1, flags=re.DOTALL
    )

    # --- 6. Update body **Authors:** metadata line ---
    authors_meta = format_authors_metadata(author_names)
    content = re.sub(
        r'(\*\*Authors:\*\*\s*).*',
        rf'\g<1>{authors_meta}',
        content, count=1
    )

    # --- Write ---
    if dry_run:
        print(f"    [DRY-RUN] Would update {paper_path.name}")
        # Show preview
        first_name = extract_last_from_wikilink(first_wikilink)
        last_name = extract_last_from_wikilink(last_wikilink)
        print(f"      first_author: {first_wikilink}, last_author: {last_wikilink}")
        print(f"      {len(author_names)} authors total")
        return True

    paper_path.write_text(content, encoding="utf-8")
    return True


# =============================================================================
# JSON LOG I/O
# =============================================================================

def load_log() -> Dict[str, Dict]:
    """Load existing resolution log from JSON."""
    if OUTPUT_JSON.exists():
        try:
            with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
                data = json.load(f)
            return {item["filename"]: item for item in data}
        except (json.JSONDecodeError, KeyError):
            return {}
    return {}


def save_log(log_map: Dict[str, Dict]):
    """Save resolution log to JSON (atomic write)."""
    output_list = sorted(log_map.values(), key=lambda x: x["filename"])
    tmp = OUTPUT_JSON.parent / f".incomplete_authors_resolved.tmp.{os.getpid()}"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(output_list, f, indent=2, ensure_ascii=False)
    os.replace(str(tmp), str(OUTPUT_JSON))


# =============================================================================
# BATCH FILE LOADING (for parallel execution)
# =============================================================================

def load_papers_from_batch(batch_file: str) -> List[Dict]:
    """Load papers from a batch JSON file instead of scanning all papers."""
    batch_path = Path(batch_file)
    if not batch_path.exists():
        # Try relative to LOGS_DIR
        batch_path = LOGS_DIR / batch_file
    if not batch_path.exists():
        print(f"ERROR: Batch file not found: {batch_file}")
        sys.exit(1)

    with open(batch_path, "r", encoding="utf-8") as f:
        batch_entries = json.load(f)

    papers = []
    for entry in batch_entries:
        paper_path = PAPERS_DIR / entry["filename"]
        if not paper_path.exists():
            print(f"  WARNING: Paper not found: {entry['filename']}")
            continue

        content = paper_path.read_text(encoding="utf-8")
        if "authors_incomplete: true" not in content:
            print(f"  SKIP: {entry['filename']} — already resolved")
            continue

        papers.append({
            "filename": entry["filename"],
            "path": str(paper_path),
            "short_title": entry.get("short_title", ""),
            "authors": extract_yaml_field(content, "authors"),
            "first_author": entry.get("first_author", extract_yaml_field(content, "first_author")),
            "last_author": extract_yaml_field(content, "last_author"),
            "doi": entry.get("doi", ""),
            "url": entry.get("url", ""),
            "external_pdf": entry.get("external_pdf", ""),
            "acl_derived_doi": entry.get("acl_derived_doi", ""),
        })

    print(f"Loaded {len(papers)} papers from batch file ({len(batch_entries)} entries)")
    return papers


# =============================================================================
# FUZZY AUTHOR MATCHING
# =============================================================================

def levenshtein_distance(s1: str, s2: str) -> int:
    """Compute Levenshtein edit distance between two strings."""
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)

    prev_row = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        curr_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = prev_row[j + 1] + 1
            deletions = curr_row[j] + 1
            substitutions = prev_row[j] + (c1 != c2)
            curr_row.append(min(insertions, deletions, substitutions))
        prev_row = curr_row
    return prev_row[-1]


def fuzzy_match_last_name(existing_last: str, resolved_authors: List[str]) -> bool:
    """
    Fuzzy matching for first-author validation.

    Strategies:
    1. Hyphen/space normalization (e.g. "García-López" matches "Garcia Lopez")
    2. Substring containment (e.g. "Wang" matches "Wang-Chen")
    3. Levenshtein distance ≤ 2 for names ≥ 4 chars (handles typos/transliterations)
    """
    existing_norm = re.sub(r'[-\s]', '', existing_last.lower()).strip('.')

    for author in resolved_authors:
        clean = clean_author_for_yaml(author).lower()
        # Extract last name from the resolved author
        if ',' in clean:
            resolved_last = clean.split(',')[0].strip()
        else:
            parts = clean.split()
            resolved_last = parts[-1] if parts else clean

        resolved_norm = re.sub(r'[-\s]', '', resolved_last).strip('.')

        # Strategy 1: normalized exact match
        if existing_norm == resolved_norm:
            return True

        # Strategy 2: substring containment (either direction)
        if len(existing_norm) >= 3 and len(resolved_norm) >= 3:
            if existing_norm in resolved_norm or resolved_norm in existing_norm:
                return True

        # Strategy 3: Levenshtein distance ≤ 2 for longer names
        if len(existing_norm) >= 4 and len(resolved_norm) >= 4:
            if levenshtein_distance(existing_norm, resolved_norm) <= 2:
                return True

    return False


# =============================================================================
# MAIN
# =============================================================================

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Resolve incomplete author lists")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be changed without writing files")
    parser.add_argument("--batch-file", type=str, default="",
                        help="Path to batch JSON file (for parallel execution)")
    parser.add_argument("--agent-id", type=str, default="",
                        help="Agent identifier for log filename (e.g., '01')")
    parser.add_argument("--relaxed-match", action="store_true",
                        help="Use fuzzy first-author validation (edit distance)")
    args = parser.parse_args()

    # Override OUTPUT_JSON when agent-id is provided
    global OUTPUT_JSON
    if args.agent_id:
        OUTPUT_JSON = LOGS_DIR / f"{DATE_PREFIX}-incomplete_authors_agent_{args.agent_id}.json"

    print("=" * 80)
    print("RESOLVE INCOMPLETE AUTHOR LISTS")
    print(f"Date: {DATE_PREFIX}")
    print(f"Dry run: {args.dry_run}")
    if args.batch_file:
        print(f"Batch file: {args.batch_file}")
    if args.agent_id:
        print(f"Agent ID: {args.agent_id}")
    if args.relaxed_match:
        print(f"Relaxed matching: enabled")
    print("=" * 80)

    # Step 1: Find papers — from batch file or by scanning
    if args.batch_file:
        papers = load_papers_from_batch(args.batch_file)
    else:
        papers = find_incomplete_papers()
    print(f"\nFound {len(papers)} papers with authors_incomplete: true")

    if not papers:
        print("Nothing to do.")
        return

    # Step 2: Load existing log (for crash recovery / re-runs)
    log_map = load_log()

    # Step 3: Process each paper
    resolved_count = 0
    skipped_count = 0
    failed_count = 0
    applied_count = 0

    for i, paper in enumerate(papers, 1):
        filename = paper["filename"]
        print(f"\n[{i}/{len(papers)}] {filename}")
        print(f"    Current authors: {paper['authors'][:80]}")

        # Skip if already resolved in this session's log
        if filename in log_map and log_map[filename]["status"] == "resolved":
            prev = log_map[filename]
            print(f"    [SKIP] Already resolved via {prev['source']} "
                  f"({len(prev['resolved_authors'])} authors)")
            skipped_count += 1

            # If dry-run, just skip. Otherwise, check if file still needs updating
            if not args.dry_run:
                file_content = Path(paper["path"]).read_text(encoding="utf-8")
                if "authors_incomplete: true" in file_content:
                    # Safety: validate first author matches before re-applying
                    if not validate_first_author_match(paper["first_author"],
                                                       prev["resolved_authors"]):
                        existing_last = extract_last_from_wikilink(paper["first_author"]).lower().strip('.')
                        if not (args.relaxed_match and fuzzy_match_last_name(existing_last, prev["resolved_authors"])):
                            print(f"    [RE-APPLY BLOCKED] First author mismatch — skipping")
                            continue
                        print(f"    [FUZZY RE-APPLY] Relaxed matching accepted")
                    print(f"    [RE-APPLY] File still has authors_incomplete: true, re-applying...")
                    success = apply_resolution(
                        Path(paper["path"]),
                        prev["resolved_authors"],
                        dry_run=False
                    )
                    if success:
                        applied_count += 1
                        print(f"    [DONE] Re-applied {len(prev['resolved_authors'])} authors")
            continue

        # Resolve via APIs
        result = resolve_paper(paper)
        log_map[filename] = result
        save_log(log_map)

        if result["status"] == "resolved":
            authors = result["resolved_authors"]

            # Safety: validate first author matches
            if not validate_first_author_match(paper["first_author"], authors):
                # Try fuzzy matching if --relaxed-match is enabled
                existing_last = extract_last_from_wikilink(paper["first_author"]).lower().strip('.')
                if args.relaxed_match and fuzzy_match_last_name(existing_last, authors):
                    print(f"    [FUZZY MATCH] Relaxed matching accepted: '{paper['first_author']}'")
                else:
                    print(f"    MISMATCH: Existing first_author '{paper['first_author']}' "
                          f"not found in resolved list (first={authors[0]})")
                    print(f"    SKIPPED to avoid applying wrong authors")
                    result["status"] = "mismatch"
                    result["error"] = (f"First author mismatch: existing='{paper['first_author']}', "
                                       f"resolved_first='{authors[0]}'")
                    log_map[filename] = result
                    save_log(log_map)
                    failed_count += 1
                    continue

            resolved_count += 1
            print(f"    RESOLVED via {result['source']}: {len(authors)} authors")
            print(f"      First: {authors[0]}, Last: {authors[-1]}")

            # Apply changes to the file
            success = apply_resolution(
                Path(paper["path"]),
                authors,
                dry_run=args.dry_run
            )
            if success:
                applied_count += 1
            else:
                print(f"    WARNING: Failed to apply changes to {filename}")
        else:
            failed_count += 1
            print(f"    FAILED: {result['error']}")

    # Step 4: Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total papers scanned: {len(papers)}")
    print(f"Resolved (this run):  {resolved_count}")
    print(f"Skipped (prev run):   {skipped_count}")
    print(f"Failed:               {failed_count}")
    print(f"Files {'would be ' if args.dry_run else ''}updated: {applied_count}")
    print(f"Log: {OUTPUT_JSON}")

    # Source breakdown
    sources = {}
    for r in log_map.values():
        src = r.get("source", "unresolved")
        sources[src] = sources.get(src, 0) + 1
    print(f"\nResolution sources:")
    for src, count in sorted(sources.items(), key=lambda x: -x[1]):
        print(f"  {src}: {count}")

    # List unresolved papers
    unresolved = [r for r in log_map.values() if r["status"] != "resolved"]
    if unresolved:
        print(f"\nUnresolved papers ({len(unresolved)}):")
        for r in sorted(unresolved, key=lambda x: x["filename"]):
            print(f"  - {r['filename']}")
            if r.get("error"):
                print(f"    Reason: {r['error']}")

    if not args.dry_run and applied_count > 0:
        print(f"\n>>> {applied_count} files updated. Run validation:")
        print(f"    ../.venv/bin/python PYTHON/validate_all_papers.py")


if __name__ == "__main__":
    main()
