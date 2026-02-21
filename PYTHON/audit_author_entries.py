#!/usr/bin/env python3
"""
Comprehensive Author Entry Audit

Scans all papers, cross-references with author profiles, and produces
a detailed issues report in 6 categories:

  A - Abbreviated/initials-only names in authors field
  B - first_author mismatch (doesn't match first entry in authors list)
  C - last_author mismatch or missing (doesn't match last entry in authors list)
  D - [[Unknown]] authors or authors_incomplete: true
  E - Author has no matching profile in Authors/
  F - Format issues (wikilinks in YAML, commas, Last-First order)

Pure read-only — no files are modified.

USAGE:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/audit_author_entries.py
    ../.venv/bin/python PYTHON/audit_author_entries.py --verbose
"""

import argparse
import functools
import json
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Force flush for parallel/background usage
import builtins
print = functools.partial(builtins.print, flush=True)

# --- Path setup ---
sys.path.insert(0, str(Path(__file__).parent))
from vault_config import PAPERS_DIR, AUTHORS_DIR, LOGS_DIR

# --- Date prefix ---
DATE_PREFIX = datetime.now().strftime("%Y%m%d")
OUTPUT_FILE = LOGS_DIR / f"{DATE_PREFIX}-author_audit_report.json"


# =============================================================================
# FRONTMATTER EXTRACTION
# =============================================================================

def extract_frontmatter(content: str) -> Optional[str]:
    """Extract raw frontmatter text between --- markers."""
    if not content.startswith('---'):
        return None
    match = re.search(r'\n---\s*\n', content[3:])
    if not match:
        return None
    return content[3:match.start() + 3]


def extract_field(fm_text: str, key: str) -> str:
    """Extract a single YAML field value from frontmatter text."""
    pattern = rf'^{re.escape(key)}:\s*(.+)$'
    m = re.search(pattern, fm_text, re.MULTILINE)
    if m:
        return m.group(1).strip().strip('"')
    return ""


def extract_field_raw(fm_text: str, key: str) -> str:
    """Extract raw YAML field value (preserving quotes) from frontmatter."""
    pattern = rf'^{re.escape(key)}:\s*(.+)$'
    m = re.search(pattern, fm_text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return ""


# =============================================================================
# AUTHOR PARSING (adapted from build_author_paper_map.py)
# =============================================================================

def clean_author_name(name: str) -> str:
    """Clean and normalize a single author name."""
    if not name:
        return ""
    name = re.sub(r'\[\[|\]\]', '', name)
    name = name.strip().strip('"\'')
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name


def smart_comma_split(text: str) -> List[str]:
    """Split comma-separated author list, handling 'LastName, FirstName' patterns.

    Conservative heuristic: only detect "Last, First" pairs when the "given name"
    parts are initials (e.g., "K.", "A. B.") or single short words — genuine
    APA-style citations like "Vida, K." NOT multi-word full names like
    "Jensen, Anders Blok" which are two separate authors.
    """
    parts = [p.strip() for p in text.split(',')]
    if len(parts) <= 1:
        return parts

    # Check for APA-style "Last, Initial" pairs:
    # Only merge if ALL given-name parts (odd indices) are:
    # - A single initial like "K" or "K." or "Y"
    # - A short initial pattern like "A. B." or "J. K."
    # - A single short word (≤3 chars) that looks like an initial
    INITIAL_LIKE = re.compile(r'^[A-Z]\.?(\s+[A-Z]\.?)*$')

    looks_like_apa_pairs = True
    if len(parts) >= 2 and len(parts) % 2 == 0:
        for i in range(0, len(parts) - 1, 2):
            given = parts[i + 1].strip() if i + 1 < len(parts) else ""
            # Remove ampersand/and prefixes
            given_clean = re.sub(r'^[&]\s*', '', given).strip()
            if not given_clean:
                looks_like_apa_pairs = False
                break
            if not INITIAL_LIKE.match(given_clean):
                looks_like_apa_pairs = False
                break
    else:
        looks_like_apa_pairs = False

    if looks_like_apa_pairs:
        merged = []
        for i in range(0, len(parts), 2):
            surname = parts[i].strip()
            given = parts[i + 1].strip() if i + 1 < len(parts) else ""
            # Remove ampersand prefix from given names
            given = re.sub(r'^[&]\s*', '', given).strip()
            if given:
                merged.append(f"{given} {surname}")
            else:
                merged.append(surname)
        return merged

    # Default: treat commas as simple separators between authors
    return parts


def parse_authors_field(authors_str: str) -> List[str]:
    """Parse the authors YAML field into a list of individual author names."""
    if not authors_str or not authors_str.strip():
        return []

    raw = authors_str.strip().strip('"')

    # Remove "et al." for parsing
    cleaned = re.sub(r',?\s*\bet\s*al\.?\b', '', raw, flags=re.IGNORECASE).strip()
    cleaned = cleaned.rstrip(',;').strip()

    # Split by semicolons (primary separator)
    if ';' in cleaned:
        parts = [p.strip() for p in cleaned.split(';')]
    else:
        parts = smart_comma_split(cleaned)

    authors = []
    for part in parts:
        name = clean_author_name(part)
        if name and name.lower() not in ('unknown', 'et al', 'et al.', 'others', 'n/a'):
            authors.append(name)

    return authors


# =============================================================================
# NAME NORMALIZATION (adapted from detect_orphaned_authors.py)
# =============================================================================

def normalize_name(name: str) -> str:
    """Create canonical form of a name for fuzzy matching.
    Lowercases, strips commas, sorts word tokens alphabetically."""
    cleaned = name.replace(',', ' ').strip()
    cleaned = re.sub(r'\s+', ' ', cleaned)
    words = sorted(cleaned.lower().split())
    return ' '.join(words)


def strip_wikilink(text: str) -> str:
    """Remove wikilink syntax from a string: [[Name]] -> Name, [[Name|Alias]] -> Name."""
    m = re.match(r'^\[\[([^\]|]+?)(?:\|[^\]]+?)?\]\]$', text.strip())
    if m:
        return m.group(1).strip()
    return re.sub(r'\[\[|\]\]', '', text).strip()


# =============================================================================
# CATEGORY A: ABBREVIATED/INITIALS-ONLY NAMES
# =============================================================================

# Regex for initial patterns: single initial like "M." or "J."
INITIAL_PATTERN = re.compile(r'^[A-Z]\.$')


def is_abbreviated_name(name: str) -> bool:
    """Check if a name contains abbreviated/initials-only parts.
    Mononyms (single-word names without periods) are NOT flagged."""
    parts = name.split()
    if len(parts) < 2:
        # Single word with no period — mononym, not abbreviated
        return False

    # Check if any part is an initial (e.g., "M.", "J.")
    for part in parts:
        if INITIAL_PATTERN.match(part):
            return True

    return False


def get_abbreviated_parts(name: str) -> List[str]:
    """Return the abbreviated parts of a name."""
    return [p for p in name.split() if INITIAL_PATTERN.match(p)]


# =============================================================================
# CATEGORY B/C: FIRST/LAST AUTHOR MISMATCH
# =============================================================================

def names_match(name_a: str, name_b: str) -> bool:
    """Check if two names match after normalization.
    Handles wikilinks, "Last, First" flip, case differences."""
    a = clean_author_name(strip_wikilink(name_a))
    b = clean_author_name(strip_wikilink(name_b))

    if not a or not b:
        return False

    # Exact match
    if a == b:
        return True

    # Case-insensitive match
    if a.lower() == b.lower():
        return True

    # Normalized (order-independent) match
    if normalize_name(a) == normalize_name(b):
        return True

    return False


# =============================================================================
# CATEGORY D: UNKNOWN/INCOMPLETE
# =============================================================================

UNKNOWN_PATTERNS = re.compile(
    r'^\[\[Unknown\]\]$|^Unknown$|^\[\[Authors\]\]$|^Authors not fully specified',
    re.IGNORECASE
)


def is_unknown_author(authors_str: str) -> bool:
    """Check if authors field indicates unknown authorship."""
    if not authors_str:
        return True
    return bool(UNKNOWN_PATTERNS.search(authors_str.strip().strip('"')))


# =============================================================================
# CATEGORY E: MISSING AUTHOR PROFILES
# =============================================================================

def build_profile_lookup(authors_dir: Path) -> Tuple[set, dict]:
    """Build sets for fast author profile lookup.
    Returns (exact_stems, normalized_to_stems) where normalized_to_stems
    maps normalized names to lists of actual file stems."""
    exact_stems = set()
    normalized_to_stems = defaultdict(list)

    for f in authors_dir.iterdir():
        if f.suffix == '.md' and f.name not in ('README.md', 'TEMPLATE.md'):
            stem = f.stem
            exact_stems.add(stem)
            normalized_to_stems[normalize_name(stem)].append(stem)

    return exact_stems, normalized_to_stems


def author_has_profile(name: str, exact_stems: set, normalized_to_stems: dict) -> bool:
    """Check if an author has a matching profile (exact or normalized)."""
    cleaned = clean_author_name(name)
    if not cleaned:
        return True  # Don't flag empty names

    # Exact match
    if cleaned in exact_stems:
        return True

    # Normalized match
    norm = normalize_name(cleaned)
    if norm in normalized_to_stems:
        return True

    return False


# =============================================================================
# CATEGORY F: FORMAT ISSUES
# =============================================================================

def detect_format_issues(authors_raw: str, authors_field_raw: str) -> List[str]:
    """Detect format issues in the authors YAML field.

    Returns list of issue codes:
    - wikilinked_yaml: authors field contains [[ ]] wikilink syntax
    - comma_separated: uses commas instead of semicolons as separator
    - last_first_format: contains "Last, First" ordering
    - empty: field is blank/missing
    - et_al_truncated: contains "et al."
    """
    issues = []

    if not authors_raw or not authors_raw.strip():
        issues.append("empty")
        return issues

    text = authors_raw.strip().strip('"')

    # Wikilinks in authors field
    if '[[' in text or ']]' in text:
        issues.append("wikilinked_yaml")

    # "et al." truncation
    if re.search(r'\bet\s*al\.?\b', text, re.IGNORECASE):
        issues.append("et_al_truncated")

    # No semicolons but has commas — detect APA-style "Last, Init." vs plain comma-separated
    if ';' not in text and ',' in text:
        parts = text.split(',')
        if len(parts) >= 2:
            # Only detect "Last, Initial" APA-style pairs when ALL given-name parts
            # are initials (e.g., "K.", "A. B.") — NOT multi-word full names
            INITIAL_LIKE = re.compile(r'^[&]?\s*[A-Z]\.?(\s+[A-Z]\.?)*$')
            if len(parts) % 2 == 0:
                is_apa = True
                for i in range(0, len(parts) - 1, 2):
                    given = parts[i + 1].strip()
                    if not given or not INITIAL_LIKE.match(given):
                        is_apa = False
                        break
                if is_apa:
                    issues.append("last_first_format")
                else:
                    issues.append("comma_separated")
            else:
                issues.append("comma_separated")

    return issues


# =============================================================================
# MAIN AUDIT
# =============================================================================

def run_audit(verbose: bool = False):
    """Run the comprehensive author entry audit."""
    print(f"=== Author Entry Audit ===")
    print(f"Papers dir: {PAPERS_DIR}")
    print(f"Authors dir: {AUTHORS_DIR}")

    # Build author profile lookup
    print("Building author profile index...")
    exact_stems, normalized_to_stems = build_profile_lookup(AUTHORS_DIR)
    print(f"  {len(exact_stems)} author profiles indexed")

    # Collect all papers
    papers = sorted(PAPERS_DIR.glob('*.md'))
    print(f"  {len(papers)} papers to scan\n")

    # Issue accumulators
    cat_a = []  # Abbreviated names
    cat_b = []  # first_author mismatch
    cat_c = []  # last_author mismatch
    cat_d = []  # Unknown/incomplete
    cat_e_map = defaultdict(list)  # Missing profiles: name -> [papers]
    cat_f = []  # Format issues

    # Per-paper scan
    for i, paper_file in enumerate(papers, 1):
        stem = paper_file.stem
        content = paper_file.read_text(encoding='utf-8')
        fm_text = extract_frontmatter(content)

        if not fm_text:
            if verbose:
                print(f"  SKIP (no frontmatter): {stem}")
            continue

        # Extract fields
        authors_str = extract_field(fm_text, 'authors')
        authors_raw = extract_field_raw(fm_text, 'authors')
        first_author_str = extract_field(fm_text, 'first_author')
        last_author_str = extract_field(fm_text, 'last_author')
        authors_incomplete = extract_field(fm_text, 'authors_incomplete')
        short_title = extract_field(fm_text, 'short_title')
        url = extract_field(fm_text, 'url')
        doi_field = extract_field(fm_text, 'doi')

        # Parse authors list
        authors_list = parse_authors_field(authors_str)

        # === Category D: Unknown/Incomplete ===
        is_unknown = is_unknown_author(authors_str)
        is_incomplete = authors_incomplete.lower() == 'true' if authors_incomplete else False

        if is_unknown or is_incomplete:
            cat_d.append({
                "paper": stem,
                "filename": paper_file.name,
                "authors_raw": authors_str,
                "is_unknown": is_unknown,
                "is_incomplete": is_incomplete,
                "short_title": short_title,
                "url": url,
                "doi": doi_field,
            })
            # Don't check B/C for unknown papers — they're fundamentally broken
            if is_unknown:
                continue

        # === Category A: Abbreviated Names ===
        for author_name in authors_list:
            if is_abbreviated_name(author_name):
                cat_a.append({
                    "paper": stem,
                    "filename": paper_file.name,
                    "author_name": author_name,
                    "abbreviated_parts": get_abbreviated_parts(author_name),
                    "short_title": short_title,
                    "url": url,
                    "doi": doi_field,
                })

        # === Category B: first_author mismatch ===
        if authors_list and first_author_str:
            first_in_list = authors_list[0]
            if not names_match(first_author_str, first_in_list):
                cat_b.append({
                    "paper": stem,
                    "filename": paper_file.name,
                    "first_author_field": first_author_str,
                    "first_in_list": first_in_list,
                    "authors_list": authors_list,
                })
        elif authors_list and not first_author_str:
            cat_b.append({
                "paper": stem,
                "filename": paper_file.name,
                "first_author_field": "(missing)",
                "first_in_list": authors_list[0],
                "authors_list": authors_list,
            })

        # === Category C: last_author mismatch ===
        if authors_list and last_author_str:
            last_in_list = authors_list[-1]
            if not names_match(last_author_str, last_in_list):
                cat_c.append({
                    "paper": stem,
                    "filename": paper_file.name,
                    "last_author_field": last_author_str,
                    "last_in_list": last_in_list,
                    "authors_list": authors_list,
                })
        elif authors_list and not last_author_str:
            cat_c.append({
                "paper": stem,
                "filename": paper_file.name,
                "last_author_field": "(missing)",
                "last_in_list": authors_list[-1],
                "authors_list": authors_list,
            })

        # === Category E: Missing author profiles ===
        for author_name in authors_list:
            cleaned = clean_author_name(author_name)
            if cleaned and not author_has_profile(cleaned, exact_stems, normalized_to_stems):
                cat_e_map[cleaned].append({
                    "paper": stem,
                    "filename": paper_file.name,
                })

        # === Category F: Format issues ===
        format_issues = detect_format_issues(authors_str, authors_raw)
        if format_issues:
            cat_f.append({
                "paper": stem,
                "filename": paper_file.name,
                "issues": format_issues,
                "authors_raw": authors_str,
                "authors_parsed": authors_list,
            })

        if verbose and i % 200 == 0:
            print(f"  Scanned {i}/{len(papers)}...")

    # Convert Category E from map to list (deduplicated by author)
    cat_e = []
    for author_name, paper_refs in sorted(cat_e_map.items()):
        cat_e.append({
            "author_name": author_name,
            "paper_count": len(paper_refs),
            "papers": paper_refs,
        })

    # Build report
    report = {
        "metadata": {
            "date": datetime.now().isoformat(),
            "papers_scanned": len(papers),
            "profiles_indexed": len(exact_stems),
        },
        "summary": {
            "A_abbreviated_names": len(cat_a),
            "B_first_author_mismatch": len(cat_b),
            "C_last_author_mismatch": len(cat_c),
            "D_unknown_incomplete": len(cat_d),
            "E_missing_profiles": len(cat_e),
            "E_missing_profiles_total_refs": sum(e["paper_count"] for e in cat_e),
            "F_format_issues": len(cat_f),
        },
        "categories": {
            "A": cat_a,
            "B": cat_b,
            "C": cat_c,
            "D": cat_d,
            "E": cat_e,
            "F": cat_f,
        },
    }

    # Print summary
    print(f"\n=== AUDIT RESULTS ===")
    print(f"Papers scanned: {len(papers)}")
    print(f"Profiles indexed: {len(exact_stems)}")
    print()
    print(f"  A. Abbreviated names:       {len(cat_a):>5} entries ({len(set(e['author_name'] for e in cat_a))} unique names)")
    print(f"  B. first_author mismatch:   {len(cat_b):>5} papers")
    print(f"  C. last_author mismatch:    {len(cat_c):>5} papers")
    print(f"  D. Unknown/incomplete:      {len(cat_d):>5} papers")
    print(f"  E. Missing profiles:        {len(cat_e):>5} unique authors ({sum(e['paper_count'] for e in cat_e)} paper refs)")
    print(f"  F. Format issues:           {len(cat_f):>5} papers")

    # Category breakdown for F
    if cat_f:
        f_types = defaultdict(int)
        for entry in cat_f:
            for issue in entry["issues"]:
                f_types[issue] += 1
        print(f"\n  F breakdown:")
        for ftype, count in sorted(f_types.items(), key=lambda x: -x[1]):
            print(f"    {ftype}: {count}")

    # Save report
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\nReport saved: {OUTPUT_FILE.name}")

    return report


# =============================================================================
# CLI
# =============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Audit author entries across all papers")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    args = parser.parse_args()

    run_audit(verbose=args.verbose)
