#!/usr/bin/env python3
"""
Resolve Author Issues — Step 3 of the Author Verification Pipeline

Takes the audit report from audit_author_entries.py and resolves issues
using local heuristics and API lookups.

Categories:
  A - Abbreviated names: local profile match → Semantic Scholar → CrossRef → arXiv
  B - first_author mismatch: derive from authors list (local)
  C - last_author mismatch: derive from authors list (local)
  D - Unknown/incomplete: API waterfall (arXiv → CrossRef → Semantic Scholar)
  E - Missing profiles: validate name, plan stub creation (local)
  F - Format issues: parse → clean → rebuild as canonical format (local)

Supports parallel execution via --start/--end for API-bound categories.

USAGE:
    cd CEI-Lit-WS

    # Run all categories (local first, then API)
    ../.venv/bin/python PYTHON/resolve_author_issues.py

    # Run specific categories
    ../.venv/bin/python PYTHON/resolve_author_issues.py --categories A,D

    # Parallel agents for Category A
    ../.venv/bin/python PYTHON/resolve_author_issues.py --categories A --start 1 --end 100
    ../.venv/bin/python PYTHON/resolve_author_issues.py --categories A --start 101 --end 200

    # Dry run (no API calls)
    ../.venv/bin/python PYTHON/resolve_author_issues.py --dry-run
    ../.venv/bin/python PYTHON/resolve_author_issues.py --skip-api
"""

import argparse
import functools
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Force flush for parallel/background usage
import builtins
print = functools.partial(builtins.print, flush=True)

# --- Path setup ---
SCRIPT_DIR = Path(__file__).parent.resolve()
sys.path.insert(0, str(SCRIPT_DIR))
from vault_config import PAPERS_DIR, AUTHORS_DIR, LOGS_DIR

# Import API fetchers (only used for categories A, D)
try:
    from expand_author_lists import ArxivAuthorFetcher, CrossrefAuthorFetcher
    HAS_API_FETCHERS = True
except ImportError:
    HAS_API_FETCHERS = False
    print("WARNING: expand_author_lists not available — API categories disabled")

# Import author validation
from author_validation import validate_author_name, find_full_name_match, normalize_author_name

# --- Date prefix ---
DATE_PREFIX = datetime.now().strftime("%Y%m%d")


# =============================================================================
# HELPERS
# =============================================================================

def load_audit_report() -> Dict:
    """Load the most recent audit report."""
    candidates = sorted(LOGS_DIR.glob("*-author_audit_report.json"), reverse=True)
    if not candidates:
        print("ERROR: No audit report found. Run audit_author_entries.py first.")
        sys.exit(1)
    path = candidates[0]
    print(f"Loading audit report: {path.name}")
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def clean_author_name(name: str) -> str:
    """Clean and normalize a single author name."""
    if not name:
        return ""
    name = re.sub(r'\[\[|\]\]', '', name)
    name = name.strip().strip('"\'')
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name


def normalize_name(name: str) -> str:
    """Order-independent normalized form for matching."""
    cleaned = name.replace(',', ' ').strip()
    cleaned = re.sub(r'\s+', ' ', cleaned)
    words = sorted(cleaned.lower().split())
    return ' '.join(words)


def strip_wikilink(text: str) -> str:
    """Remove wikilink syntax: [[Name]] -> Name."""
    m = re.match(r'^\[\[([^\]|]+?)(?:\|[^\]]+?)?\]\]$', text.strip())
    if m:
        return m.group(1).strip()
    return re.sub(r'\[\[|\]\]', '', text).strip()


def extract_doi_from_url(url: str) -> Optional[str]:
    """Extract DOI from a URL."""
    if not url:
        return None
    match = re.search(r'(?:doi\.org/|doi:\s*)(10\.\d{4,}/[^\s]+)', url)
    if match:
        return match.group(1).rstrip('.')
    return None


def extract_arxiv_id_from_url(url: str) -> Optional[str]:
    """Extract arXiv ID from URL, only from arxiv.org domains."""
    if not url or 'arxiv.org' not in url:
        return None
    match = re.search(r'(\d{4}\.\d{4,5})', url)
    if match:
        return match.group(1)
    return None


def build_profile_lookup() -> Tuple[set, dict]:
    """Build profile lookup sets for fast matching."""
    from collections import defaultdict
    exact = set()
    normalized = defaultdict(list)
    for f in AUTHORS_DIR.iterdir():
        if f.suffix == '.md' and f.name not in ('README.md', 'TEMPLATE.md'):
            stem = f.stem
            exact.add(stem)
            normalized[normalize_name(stem)].append(stem)
    return exact, normalized


# =============================================================================
# SEMANTIC SCHOLAR / CROSSREF API HELPERS
# =============================================================================

def fetch_semantic_scholar_authors(doi: str) -> Optional[List[str]]:
    """Fetch full author list from Semantic Scholar by DOI."""
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
        time.sleep(10)


def fetch_semantic_scholar_by_title(title: str) -> Optional[List[str]]:
    """Fetch authors from Semantic Scholar by title search."""
    import urllib.request
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
        time.sleep(10)


def title_similarity(a: str, b: str) -> float:
    """Simple word-overlap title similarity."""
    words_a = set(re.findall(r'\w+', a.lower()))
    words_b = set(re.findall(r'\w+', b.lower()))
    if not words_a or not words_b:
        return 0.0
    intersection = words_a & words_b
    union = words_a | words_b
    return len(intersection) / len(union)


def find_full_name_from_api(abbreviated: str, doi: str = None,
                            title: str = None, url: str = None,
                            skip_api: bool = False) -> Optional[str]:
    """Try to resolve an abbreviated name via API lookups.

    Strategy: fetch the full author list, then find which author
    matches the abbreviated pattern (same last name + compatible initials).
    """
    if skip_api:
        return None

    full_authors = None
    source = None

    # Try DOI-based lookup first
    if doi:
        full_authors = fetch_semantic_scholar_authors(doi)
        source = "semantic_scholar_doi"

    if not full_authors and title and len(title) > 10:
        full_authors = fetch_semantic_scholar_by_title(title)
        source = "semantic_scholar_title"

    if not full_authors:
        # Try arXiv
        arxiv_id = extract_arxiv_id_from_url(url or "")
        if arxiv_id and HAS_API_FETCHERS:
            result = ArxivAuthorFetcher.fetch_authors(arxiv_id)
            if result and result.authors:
                full_authors = list(result.authors)
                source = "arxiv"
            time.sleep(3)

    if not full_authors:
        return None

    # Match abbreviated name to full name
    abbr_parts = abbreviated.split()
    # Extract initials and surname
    initials = [p[0] for p in abbr_parts if re.match(r'^[A-Z]\.$', p)]
    surname_parts = [p for p in abbr_parts if not re.match(r'^[A-Z]\.$', p)]
    surname = ' '.join(surname_parts).lower() if surname_parts else ''

    if not surname:
        return None

    for full_name in full_authors:
        full_parts = full_name.split()
        if not full_parts:
            continue

        # Check surname match (last word or last N words)
        full_lower = full_name.lower()
        if not full_lower.endswith(surname):
            continue

        # Check initials compatibility
        given_parts = full_parts[:len(full_parts) - len(surname_parts)]
        full_initials = [p[0].upper() for p in given_parts if p]

        if len(initials) <= len(full_initials):
            if all(initials[j] == full_initials[j] for j in range(len(initials))):
                return full_name

    return None


# =============================================================================
# CATEGORY RESOLVERS
# =============================================================================

def resolve_category_a(items: List[Dict], skip_api: bool = False) -> List[Dict]:
    """Resolve abbreviated names: local match → API waterfall."""
    results = []
    print(f"\n--- Category A: {len(items)} abbreviated name entries ---")

    # Deduplicate by (author_name) to avoid redundant API calls
    seen_names = {}  # name -> resolution

    for i, item in enumerate(items, 1):
        name = item["author_name"]
        paper = item["paper"]

        resolution = {
            "paper": paper,
            "filename": item["filename"],
            "original_name": name,
            "resolved_name": None,
            "source": None,
            "status": "unresolved",
        }

        # Check if we already resolved this name
        if name in seen_names:
            prev = seen_names[name]
            resolution["resolved_name"] = prev["resolved_name"]
            resolution["source"] = prev["source"]
            resolution["status"] = prev["status"]
            results.append(resolution)
            continue

        print(f"  [{i}/{len(items)}] {name} ({paper[:50]})", end=" ")

        # Strategy 1: Local profile match
        full_name = find_full_name_match(name)
        if full_name:
            print(f"-> LOCAL: {full_name}")
            resolution["resolved_name"] = full_name
            resolution["source"] = "local_profile"
            resolution["status"] = "resolved"
            seen_names[name] = resolution
            results.append(resolution)
            continue

        # Strategy 2: API waterfall (if enabled)
        if not skip_api:
            doi = item.get("doi") or extract_doi_from_url(item.get("url", ""))
            title = item.get("short_title", "")
            url = item.get("url", "")

            full_name = find_full_name_from_api(name, doi=doi, title=title, url=url)
            if full_name:
                print(f"-> API: {full_name}")
                resolution["resolved_name"] = full_name
                resolution["source"] = "api"
                resolution["status"] = "resolved"
                seen_names[name] = resolution
                results.append(resolution)
                continue

        print("-> UNRESOLVED")
        seen_names[name] = resolution
        results.append(resolution)

    resolved = sum(1 for r in results if r["status"] == "resolved")
    print(f"  Category A: {resolved}/{len(results)} resolved")
    return results


def resolve_category_b(items: List[Dict]) -> List[Dict]:
    """Resolve first_author mismatches: derive from authors list."""
    results = []
    print(f"\n--- Category B: {len(items)} first_author mismatches ---")

    for item in items:
        authors_list = item.get("authors_list", [])
        if not authors_list:
            results.append({
                "paper": item["paper"],
                "filename": item["filename"],
                "action": "skip",
                "reason": "empty authors list",
            })
            continue

        correct_first = authors_list[0]
        results.append({
            "paper": item["paper"],
            "filename": item["filename"],
            "action": "update_first_author",
            "old_value": item["first_author_field"],
            "new_value": correct_first,
            "status": "resolved",
        })

    print(f"  Category B: {sum(1 for r in results if r.get('status') == 'resolved')}/{len(results)} resolved")
    return results


def resolve_category_c(items: List[Dict]) -> List[Dict]:
    """Resolve last_author mismatches: derive from authors list."""
    results = []
    print(f"\n--- Category C: {len(items)} last_author mismatches ---")

    for item in items:
        authors_list = item.get("authors_list", [])
        if not authors_list:
            results.append({
                "paper": item["paper"],
                "filename": item["filename"],
                "action": "skip",
                "reason": "empty authors list",
            })
            continue

        correct_last = authors_list[-1]
        is_missing = item["last_author_field"] == "(missing)"

        results.append({
            "paper": item["paper"],
            "filename": item["filename"],
            "action": "add_last_author" if is_missing else "update_last_author",
            "old_value": item["last_author_field"],
            "new_value": correct_last,
            "status": "resolved",
        })

    print(f"  Category C: {sum(1 for r in results if r.get('status') == 'resolved')}/{len(results)} resolved")
    return results


def resolve_category_d(items: List[Dict], skip_api: bool = False) -> List[Dict]:
    """Resolve unknown/incomplete authors via API waterfall."""
    results = []
    print(f"\n--- Category D: {len(items)} unknown/incomplete papers ---")

    # Identify institutional papers (skip API for these)
    INSTITUTIONAL_PATTERNS = re.compile(
        r'(?:Foundation|Ministry|Commission|Committee|Council|Team|'
        r'Organization|Organisation|Project|Community|Government|'
        r'Working Group|Task Force)',
        re.IGNORECASE
    )

    for i, item in enumerate(items, 1):
        paper = item["paper"]
        authors_raw = item.get("authors_raw", "")

        resolution = {
            "paper": paper,
            "filename": item["filename"],
            "is_unknown": item.get("is_unknown", False),
            "is_incomplete": item.get("is_incomplete", False),
            "resolved_authors": None,
            "source": None,
            "status": "unresolved",
        }

        # Check for institutional authors
        if INSTITUTIONAL_PATTERNS.search(authors_raw) or INSTITUTIONAL_PATTERNS.search(paper):
            print(f"  [{i}/{len(items)}] {paper[:50]} -> INSTITUTIONAL (skip)")
            resolution["status"] = "skip_institutional"
            results.append(resolution)
            continue

        print(f"  [{i}/{len(items)}] {paper[:50]}", end=" ")

        if skip_api:
            print("-> SKIP (no API)")
            results.append(resolution)
            continue

        # Read paper to get URL/DOI/title
        paper_path = PAPERS_DIR / item["filename"]
        if not paper_path.exists():
            print("-> FILE NOT FOUND")
            results.append(resolution)
            continue

        content = paper_path.read_text(encoding='utf-8')
        # Extract fields
        url_match = re.search(r'^url:\s*(.+)$', content, re.MULTILINE)
        url = url_match.group(1).strip().strip('"') if url_match else ""
        doi_match = re.search(r'^doi:\s*(.+)$', content, re.MULTILINE)
        doi = doi_match.group(1).strip().strip('"') if doi_match else ""
        if not doi:
            doi = extract_doi_from_url(url)
        title_match = re.search(r'^short_title:\s*(.+)$', content, re.MULTILINE)
        title = title_match.group(1).strip().strip('"') if title_match else ""
        ext_pdf_match = re.search(r'^external_pdf:\s*(.+)$', content, re.MULTILINE)
        ext_pdf = ext_pdf_match.group(1).strip().strip('"') if ext_pdf_match else ""

        # API waterfall
        full_authors = None
        source = None

        # 1. arXiv
        arxiv_id = extract_arxiv_id_from_url(url)
        if not arxiv_id:
            arxiv_id = extract_arxiv_id_from_url(ext_pdf)
        if arxiv_id and HAS_API_FETCHERS:
            result = ArxivAuthorFetcher.fetch_authors(arxiv_id)
            if result and result.authors:
                full_authors = list(result.authors)
                source = "arxiv"
            time.sleep(3)

        # 2. CrossRef
        if not full_authors and doi and HAS_API_FETCHERS:
            result = CrossrefAuthorFetcher.fetch_authors(doi)
            if result and result.authors:
                full_authors = list(result.authors)
                source = "crossref"
            time.sleep(1)

        # 3. Semantic Scholar (DOI)
        if not full_authors and doi:
            full_authors = fetch_semantic_scholar_authors(doi)
            if full_authors:
                source = "semantic_scholar_doi"

        # 4. Semantic Scholar (title)
        if not full_authors and title and len(title) > 10:
            full_authors = fetch_semantic_scholar_by_title(title)
            if full_authors:
                source = "semantic_scholar_title"

        if full_authors:
            print(f"-> {source}: {len(full_authors)} authors")
            resolution["resolved_authors"] = full_authors
            resolution["source"] = source
            resolution["status"] = "resolved"
        else:
            print("-> UNRESOLVED")

        results.append(resolution)

    resolved = sum(1 for r in results if r["status"] == "resolved")
    skipped = sum(1 for r in results if r["status"] == "skip_institutional")
    print(f"  Category D: {resolved}/{len(results)} resolved, {skipped} institutional (skipped)")
    return results


def resolve_category_e(items: List[Dict]) -> List[Dict]:
    """Validate missing author names and plan stub creation."""
    results = []
    print(f"\n--- Category E: {len(items)} missing author profiles ---")

    for item in items:
        name = item["author_name"]
        is_valid, errors, warnings = validate_author_name(name)

        if is_valid:
            results.append({
                "author_name": name,
                "paper_count": item["paper_count"],
                "papers": item["papers"],
                "action": "create_stub",
                "status": "resolved",
                "warnings": warnings,
            })
        else:
            results.append({
                "author_name": name,
                "paper_count": item["paper_count"],
                "papers": item["papers"],
                "action": "skip",
                "status": "skip_invalid",
                "errors": errors,
            })

    valid = sum(1 for r in results if r["status"] == "resolved")
    invalid = sum(1 for r in results if r["status"] == "skip_invalid")
    print(f"  Category E: {valid} to create, {invalid} invalid (skipped)")
    return results


def resolve_category_f(items: List[Dict]) -> List[Dict]:
    """Resolve format issues: normalize to canonical format."""
    results = []
    print(f"\n--- Category F: {len(items)} format issue papers ---")

    for item in items:
        issues = item["issues"]
        authors_raw = item["authors_raw"]
        authors_parsed = item.get("authors_parsed", [])

        if not authors_parsed:
            results.append({
                "paper": item["paper"],
                "filename": item["filename"],
                "action": "skip",
                "reason": "no parseable authors",
                "status": "skip",
            })
            continue

        # Canonical format: "First Last; First Last" (no wikilinks, semicolons)
        canonical = "; ".join(authors_parsed)

        # Check if it actually changed
        raw_cleaned = authors_raw.strip().strip('"')
        if canonical == raw_cleaned:
            results.append({
                "paper": item["paper"],
                "filename": item["filename"],
                "action": "skip",
                "reason": "already canonical after parse",
                "status": "skip",
            })
            continue

        results.append({
            "paper": item["paper"],
            "filename": item["filename"],
            "action": "reformat",
            "old_value": authors_raw,
            "new_value": canonical,
            "issues_fixed": issues,
            "status": "resolved",
        })

    resolved = sum(1 for r in results if r.get("status") == "resolved")
    print(f"  Category F: {resolved}/{len(results)} to reformat")
    return results


# =============================================================================
# MAIN
# =============================================================================

def save_results(results: Dict, categories: str, start: int, end: int):
    """Save resolution results to JSON."""
    if start > 0 or end > 0:
        suffix = f"_{categories}_{start}_{end}"
    else:
        suffix = f"_{categories}" if categories != "A,B,C,D,E,F" else ""

    output_file = LOGS_DIR / f"{DATE_PREFIX}-author_resolution_plan{suffix}.json"

    # Atomic write
    tmp = output_file.with_suffix(f".tmp.{os.getpid()}")
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    os.replace(str(tmp), str(output_file))

    print(f"\nResults saved: {output_file.name}")
    return output_file


def main():
    parser = argparse.ArgumentParser(description="Resolve author issues from audit report")
    parser.add_argument("--categories", default="A,B,C,D,E,F",
                        help="Comma-separated categories to resolve (default: A,B,C,D,E,F)")
    parser.add_argument("--start", type=int, default=0,
                        help="Start index (1-based) for API-bound categories")
    parser.add_argument("--end", type=int, default=0,
                        help="End index (1-based, inclusive) for API-bound categories")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print plan without making API calls")
    parser.add_argument("--skip-api", action="store_true",
                        help="Skip all API calls (local resolution only)")
    args = parser.parse_args()

    cats = [c.strip().upper() for c in args.categories.split(',')]
    skip_api = args.dry_run or args.skip_api

    report = load_audit_report()
    all_results = {"metadata": {
        "date": datetime.now().isoformat(),
        "categories": cats,
        "start": args.start,
        "end": args.end,
        "skip_api": skip_api,
    }}

    for cat in cats:
        items = report["categories"].get(cat, [])

        # Apply range slicing for API-bound categories
        if args.start > 0 and args.end > 0:
            items = items[args.start - 1:args.end]
            print(f"Range [{args.start}-{args.end}]: {len(items)} items for category {cat}")

        if not items:
            print(f"\nCategory {cat}: no items")
            all_results[cat] = []
            continue

        if cat == 'A':
            all_results['A'] = resolve_category_a(items, skip_api=skip_api)
        elif cat == 'B':
            all_results['B'] = resolve_category_b(items)
        elif cat == 'C':
            all_results['C'] = resolve_category_c(items)
        elif cat == 'D':
            all_results['D'] = resolve_category_d(items, skip_api=skip_api)
        elif cat == 'E':
            all_results['E'] = resolve_category_e(items)
        elif cat == 'F':
            all_results['F'] = resolve_category_f(items)
        else:
            print(f"Unknown category: {cat}")

    # Summary
    print("\n=== RESOLUTION SUMMARY ===")
    for cat in cats:
        items = all_results.get(cat, [])
        if not items:
            continue
        resolved = sum(1 for r in items if r.get("status") == "resolved")
        total = len(items)
        print(f"  {cat}: {resolved}/{total} resolved")

    save_results(all_results, args.categories.replace(',', ''), args.start, args.end)


if __name__ == "__main__":
    main()
