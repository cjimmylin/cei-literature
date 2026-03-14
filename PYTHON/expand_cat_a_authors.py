#!/usr/bin/env python3
"""
Expand Abbreviated Authors (Groups 2b + 3 from Cat A triage)

Resolves truly abbreviated names using multiple strategies:
  1. Existing author profiles — match initial+surname to full profile name
  2. Co-author context — check if same paper lists full name elsewhere
  3. arXiv API — fetch full author list by arXiv ID
  4. Semantic Scholar API — look up paper by DOI/title

Rate limits: arXiv 3s delay, Semantic Scholar 10s+ delay.

USAGE:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/expand_cat_a_authors.py
    ../.venv/bin/python PYTHON/expand_cat_a_authors.py --skip-api    # profiles-only
    ../.venv/bin/python PYTHON/expand_cat_a_authors.py --start 1 --end 50  # batch range
"""

import argparse
import functools
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Optional
from urllib.parse import quote

import builtins
print = functools.partial(builtins.print, flush=True)

sys.path.insert(0, str(Path(__file__).parent))
from vault_config import PAPERS_DIR, AUTHORS_DIR, LOGS_DIR

DATE_PREFIX = datetime.now().strftime("%Y%m%d")
OUTPUT_FILE = LOGS_DIR / f"{DATE_PREFIX}-cat_a_expansion_results.json"

INITIAL_RE = re.compile(r'^[A-Z]\.$')
ARXIV_API_BASE = "http://export.arxiv.org/api/query?"
S2_API_BASE = "https://api.semanticscholar.org/graph/v1"


# =============================================================================
# MATCHING LOGIC
# =============================================================================

def extract_initials_and_surname(name: str) -> tuple:
    """Extract (initials_list, surname_parts) from an abbreviated name.
    E.g., "A. B. Smith" → (["A", "B"], ["Smith"])
          "M. Sanguinetti" → (["M"], ["Sanguinetti"])
    """
    parts = name.split()
    initials = []
    surname_parts = []

    for part in parts:
        if INITIAL_RE.match(part):
            initials.append(part[0])
        else:
            surname_parts.append(part)

    return initials, surname_parts


def match_abbreviated_to_full(abbreviated: str, full_names: list) -> Optional[str]:
    """Match an abbreviated name to a full name from a list.
    E.g., "A. Smith" matches "Alice Smith" or "Alice B. Smith".

    Only matches when the surname is at the END of the candidate name
    (standard Western order). Does NOT match reverse-surname positions
    to avoid false positives like "Stephen C." → "Stephen Casper".
    """
    initials, surname_parts = extract_initials_and_surname(abbreviated)
    if not initials or not surname_parts:
        return None

    # Guard: if surname_parts look like a common first name and the initial
    # is at the end (e.g., "Kevin L."), this is a truncated name, not abbreviated.
    # Skip these — they need format fixing, not expansion.
    parts = abbreviated.split()
    if len(parts) >= 2 and INITIAL_RE.match(parts[-1]) and not INITIAL_RE.match(parts[0]):
        # "FirstName Initial." pattern — truncated, not abbreviated
        return None

    surname = ' '.join(surname_parts).lower()

    for full_name in full_names:
        full_parts = full_name.split()
        if len(full_parts) < 2:
            continue

        # Only match surname at end (standard Western name order)
        full_surname = ' '.join(full_parts[-len(surname_parts):]).lower()
        if full_surname != surname:
            continue

        given_parts = full_parts[:-len(surname_parts)]
        if not given_parts:
            continue

        # Extract initials from given parts (skip period-initials themselves)
        full_initials = [p[0].upper() for p in given_parts if p and not INITIAL_RE.match(p)]

        # Our abbreviated initials should match the beginning of full initials
        if len(initials) > len(full_initials):
            continue

        if initials == full_initials[:len(initials)]:
            # Verify the full name actually expands the initials
            has_expansion = any(
                len(p) > 2 and not INITIAL_RE.match(p)
                for p in given_parts
            )
            if has_expansion:
                return full_name

    return None


# =============================================================================
# STRATEGY 1: EXISTING AUTHOR PROFILES
# =============================================================================

def search_author_profiles(abbreviated: str) -> Optional[str]:
    """Search existing author profiles for a matching full name."""
    initials, surname_parts = extract_initials_and_surname(abbreviated)
    if not initials or not surname_parts:
        return None

    surname = ' '.join(surname_parts)

    # Use iterdir (not glob) to avoid metacharacter issues
    for author_file in AUTHORS_DIR.iterdir():
        if author_file.suffix != '.md':
            continue

        full_name = author_file.stem
        matched = match_abbreviated_to_full(abbreviated, [full_name])
        if matched:
            return matched

    return None


# =============================================================================
# STRATEGY 2: CO-AUTHOR CONTEXT
# =============================================================================

def search_coauthor_context(abbreviated: str, papers_data: list) -> Optional[str]:
    """Check if the full name appears in any paper's author list."""
    for paper in papers_data:
        authors_str = paper.get("authors_raw", "")
        if not authors_str:
            continue
        # Split by semicolons
        co_authors = [a.strip().strip('"') for a in authors_str.split(';')]
        matched = match_abbreviated_to_full(abbreviated, co_authors)
        if matched and matched != abbreviated:
            return matched

    return None


# =============================================================================
# STRATEGY 3: ARXIV API
# =============================================================================

def extract_arxiv_id(url: str) -> Optional[str]:
    """Extract arXiv ID from URL."""
    if not url:
        return None
    match = re.search(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})', url)
    return match.group(1) if match else None


def fetch_arxiv_authors(arxiv_id: str) -> list:
    """Fetch complete author list from arXiv API."""
    try:
        url = f"{ARXIV_API_BASE}id_list={arxiv_id}"
        req = urllib.request.Request(url, headers={"User-Agent": "CEI-Literature-Vault/1.0"})
        with urllib.request.urlopen(req, timeout=15) as response:
            root = ET.fromstring(response.read())
            authors = []
            ns = {'atom': 'http://www.w3.org/2005/Atom'}
            for entry in root.findall('atom:entry', ns):
                for author_elem in entry.findall('atom:author', ns):
                    name_elem = author_elem.find('atom:name', ns)
                    if name_elem is not None and name_elem.text:
                        authors.append(name_elem.text.strip())
            return authors
    except Exception as e:
        print(f"    arXiv error for {arxiv_id}: {e}")
        return []


# =============================================================================
# STRATEGY 4: SEMANTIC SCHOLAR API
# =============================================================================

def fetch_s2_authors_by_doi(doi: str) -> list:
    """Fetch authors from Semantic Scholar by DOI."""
    try:
        url = f"{S2_API_BASE}/paper/DOI:{quote(doi, safe='')}?fields=authors"
        req = urllib.request.Request(url, headers={"User-Agent": "CEI-Literature-Vault/1.0"})
        with urllib.request.urlopen(req, timeout=15) as response:
            data = json.loads(response.read())
            return [a["name"] for a in data.get("authors", []) if a.get("name")]
    except Exception as e:
        print(f"    S2 error for DOI {doi}: {e}")
        return []


# =============================================================================
# MAIN RESOLUTION
# =============================================================================

def gather_paper_info(entries: list) -> dict:
    """Read paper files to get URL/DOI/authors for the entries.
    Returns dict keyed by paper filename.
    """
    paper_cache = {}
    filenames = set(e["filename"] for e in entries)

    for filename in filenames:
        paper_path = PAPERS_DIR / filename
        if not paper_path.exists():
            continue

        content = paper_path.read_text(encoding='utf-8')
        fm_match = re.match(r'---\n(.*?)\n---\n', content, re.DOTALL)
        if not fm_match:
            continue

        fm = fm_match.group(1)

        def get_field(key):
            m = re.search(rf'^{re.escape(key)}:\s*(.+)$', fm, re.MULTILINE)
            return m.group(1).strip().strip('"') if m else ""

        paper_cache[filename] = {
            "url": get_field("url"),
            "doi": get_field("doi"),
            "authors_raw": get_field("authors"),
        }

    return paper_cache


def resolve_name(abbreviated: str, paper_entries: list, paper_cache: dict,
                 skip_api: bool = False, arxiv_cache: dict = None,
                 s2_cache: dict = None) -> tuple:
    """Try all strategies to resolve an abbreviated name.
    Returns (full_name, source) or (None, "not_found").
    """
    if arxiv_cache is None:
        arxiv_cache = {}
    if s2_cache is None:
        s2_cache = {}

    # For reversed names like "Logacheva, V.", un-reverse before matching
    search_name = abbreviated
    is_reversed = ',' in abbreviated
    if is_reversed:
        comma_parts = [p.strip() for p in abbreviated.split(',', 1)]
        if len(comma_parts) == 2 and comma_parts[1].strip():
            search_name = f"{comma_parts[1].strip()} {comma_parts[0].strip()}"

    # Strategy 1: Existing author profiles
    full_name = search_author_profiles(search_name)
    if full_name:
        return full_name, "author_profile"

    # Gather paper data for this name
    papers_data = [paper_cache.get(e["filename"], {}) for e in paper_entries]

    # Strategy 2: Co-author context (other authors in same paper list)
    full_name = search_coauthor_context(search_name, papers_data)
    if full_name:
        return full_name, "coauthor_context"

    if skip_api:
        return None, "skipped_api"

    # Strategy 3: arXiv API
    for paper_data in papers_data:
        arxiv_id = extract_arxiv_id(paper_data.get("url", ""))
        if not arxiv_id:
            continue

        if arxiv_id not in arxiv_cache:
            time.sleep(3)  # Rate limit
            arxiv_cache[arxiv_id] = fetch_arxiv_authors(arxiv_id)

        arxiv_authors = arxiv_cache[arxiv_id]
        if arxiv_authors:
            full_name = match_abbreviated_to_full(search_name, arxiv_authors)
            if full_name:
                return full_name, f"arxiv:{arxiv_id}"

    # Strategy 4: Semantic Scholar API (DOI lookup)
    for paper_data in papers_data:
        doi = paper_data.get("doi", "")
        if not doi:
            continue

        if doi not in s2_cache:
            time.sleep(10)  # Rate limit — S2 needs 10s+
            s2_cache[doi] = fetch_s2_authors_by_doi(doi)

        s2_authors = s2_cache[doi]
        if s2_authors:
            full_name = match_abbreviated_to_full(search_name, s2_authors)
            if full_name:
                return full_name, f"semantic_scholar:DOI:{doi}"

    return None, "not_found"


def main():
    parser = argparse.ArgumentParser(description="Expand abbreviated author names")
    parser.add_argument("--skip-api", action="store_true",
                        help="Skip API calls, only use profile/co-author strategies")
    parser.add_argument("--start", type=int, default=1,
                        help="Start index (1-based) for batch processing")
    parser.add_argument("--end", type=int, default=0,
                        help="End index (0 = all) for batch processing")
    args = parser.parse_args()

    # Load triage data
    candidates = sorted(LOGS_DIR.glob("*-cat_a_triage.json"), reverse=True)
    if not candidates:
        print("ERROR: No triage file found. Run triage_cat_a_authors.py first.")
        sys.exit(1)

    triage_path = candidates[0]
    print(f"Loading triage: {triage_path.name}")

    with open(triage_path, 'r', encoding='utf-8') as f:
        triage = json.load(f)

    # Combine Groups 2b and 3
    group2b = triage["groups"].get("2b_expand_and_format", [])
    group3 = triage["groups"].get("3_expand", [])
    all_entries = group2b + group3

    # Deduplicate by author name, keeping all paper references
    name_entries = defaultdict(list)
    for entry in all_entries:
        name_entries[entry["author_name"]].append(entry)

    unique_names = sorted(name_entries.keys())
    print(f"Total entries: {len(all_entries)} (Group 2b: {len(group2b)}, Group 3: {len(group3)})")
    print(f"Unique names to resolve: {len(unique_names)}")

    # Apply batch range
    if args.end > 0:
        unique_names = unique_names[args.start - 1:args.end]
    else:
        unique_names = unique_names[args.start - 1:]
    print(f"Processing range: {args.start}–{args.start + len(unique_names) - 1}")

    # Gather paper info
    print("Reading paper files...")
    paper_cache = gather_paper_info(all_entries)
    print(f"  Cached {len(paper_cache)} papers")

    # Resolve each name
    print(f"\nResolving {'(profiles-only)' if args.skip_api else '(all strategies)'}...")
    results = []
    arxiv_cache = {}
    s2_cache = {}
    stats = {"resolved": 0, "unresolved": 0, "by_source": defaultdict(int)}

    for i, name in enumerate(unique_names, args.start):
        entries = name_entries[name]
        group = entries[0]["group"]

        full_name, source = resolve_name(
            name, entries, paper_cache,
            skip_api=args.skip_api,
            arxiv_cache=arxiv_cache,
            s2_cache=s2_cache,
        )

        result = {
            "original_name": name,
            "group": group,
            "papers": [{"filename": e["filename"], "paper": e["paper"]} for e in entries],
            "resolved_name": full_name,
            "source": source,
            "status": "resolved" if full_name else "unresolved",
        }

        # For Group 2b, the name also needs un-reversing after expansion
        if group == "2b_expand_and_format" and full_name:
            # The full_name from API is already in "First Last" format
            result["note"] = "was reversed+abbreviated"

        results.append(result)

        if full_name:
            stats["resolved"] += 1
            stats["by_source"][source.split(":")[0]] += 1
            print(f"  [{i}] {name} → {full_name} ({source})")
        else:
            stats["unresolved"] += 1
            print(f"  [{i}] {name} → NOT FOUND ({source})")

    # Summary
    print(f"\n=== EXPANSION RESULTS ===")
    print(f"  Resolved: {stats['resolved']}")
    print(f"  Unresolved: {stats['unresolved']}")
    print(f"  By source:")
    for source, count in sorted(stats["by_source"].items(), key=lambda x: -x[1]):
        print(f"    {source}: {count}")

    # Save results
    output = {
        "metadata": {
            "date": datetime.now().isoformat(),
            "triage_source": triage_path.name,
            "skip_api": args.skip_api,
            "range": f"{args.start}-{args.start + len(unique_names) - 1}",
        },
        "summary": {
            "total": len(unique_names),
            "resolved": stats["resolved"],
            "unresolved": stats["unresolved"],
            "by_source": dict(stats["by_source"]),
        },
        "results": results,
    }

    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    tmp = OUTPUT_FILE.with_suffix(f".tmp.{os.getpid()}")
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    os.replace(str(tmp), str(OUTPUT_FILE))
    print(f"\nResults saved: {OUTPUT_FILE.name}")


if __name__ == "__main__":
    main()
