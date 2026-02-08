#!/usr/bin/env python3
"""
Discover Unknown Authors — Script 1 of 2

Scans all papers for placeholder authors (Unknown, Authors, etc.),
resolves via arXiv API, Semantic Scholar API, and PDF extract parsing,
writes results to logs/unknown_authors_resolved.json for human review.

Usage:
    # Full run (sequential)
    python discover_unknown_authors.py

    # Parallel batches
    python discover_unknown_authors.py --start 1 --end 20
    python discover_unknown_authors.py --start 20 --end 40
    ...

    # Mop-up pass (processes any still-unresolved)
    python discover_unknown_authors.py --mopup
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
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Force flush for parallel batch processing
print = functools.partial(print, flush=True)

# --- Path setup ---
SCRIPT_DIR = Path(__file__).parent.resolve()
WORKSPACE_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(WORKSPACE_ROOT / ".agent"))

from vault_config import PAPERS_DIR, PDF_EXTRACTS_DIR, PDFS_DIR, LOGS_DIR

# --- Constants ---
ARXIV_API_BASE = "http://export.arxiv.org/api/query"
SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/graph/v1/paper"
OUTPUT_JSON = LOGS_DIR / "unknown_authors_resolved.json"

PLACEHOLDER_PATTERNS = [
    "Unknown",
    "Authors",
    "[Authors]",
    "[Authors from Kurt Gray Lab]",
    "Authors not fully specified in search results",
]


# ============================================================
# Detection
# ============================================================

def is_placeholder_author(authors_str: str) -> bool:
    """Check if an authors field value is a placeholder."""
    cleaned = authors_str.strip().strip('"').strip("'")
    if not cleaned:
        return True
    for pat in PLACEHOLDER_PATTERNS:
        if cleaned == pat:
            return True
    if cleaned.startswith("[Authors"):
        return True
    if "not fully specified" in cleaned.lower():
        return True
    return False


def is_placeholder_filename(filename: str) -> bool:
    """Check if filename contains a placeholder author token."""
    # Matches: YYYY-Unknown-..., YYYY-Authors-..., YYYY-results-...
    m = re.match(r'^\d{4}-(Unknown|Authors|results)-', filename)
    return bool(m)


def find_affected_papers() -> List[Dict]:
    """Find all papers that need author resolution."""
    papers = []
    for paper_path in sorted(PAPERS_DIR.glob("*.md")):
        content = paper_path.read_text(encoding="utf-8")

        # Extract frontmatter
        fm_match = re.match(r"---\n(.*?)\n---\n", content, re.DOTALL)
        if not fm_match:
            continue

        frontmatter = fm_match.group(1)
        body = content[fm_match.end():]

        # Parse key fields
        fields = {}
        for line in frontmatter.split("\n"):
            if ":" in line and not line.startswith("  "):
                m = re.match(r'^([^:]+):\s*(.*)', line)
                if m:
                    fields[m.group(1).strip()] = m.group(2).strip().strip('"')

        authors_val = fields.get("authors", "")
        filename = paper_path.name

        has_placeholder_author = is_placeholder_author(authors_val)
        has_placeholder_filename = is_placeholder_filename(filename)

        if has_placeholder_author or has_placeholder_filename:
            papers.append({
                "filename": filename,
                "path": str(paper_path),
                "authors_field": authors_val,
                "has_placeholder_author": has_placeholder_author,
                "has_placeholder_filename": has_placeholder_filename,
                "url": fields.get("url", ""),
                "external_pdf": fields.get("external_pdf", ""),
                "doi": fields.get("doi", ""),
                "pdf_extract": fields.get("pdf_extract", ""),
                "short_title": fields.get("short_title", ""),
                "first_author": fields.get("first_author", ""),
                "year": fields.get("year", ""),
            })

    return papers


# ============================================================
# arXiv API
# ============================================================

def extract_arxiv_id(url: str) -> Optional[str]:
    """Extract arXiv ID from URL."""
    if not url:
        return None
    m = re.search(r"arxiv\.org/(?:abs|pdf)/(\d+\.\d+)", url)
    if m:
        return m.group(1)
    # Try external_pdf pattern
    m = re.search(r"arxiv\.org/pdf/(\d+\.\d+)", url)
    if m:
        return m.group(1)
    return None


def fetch_arxiv_authors(arxiv_id: str) -> Optional[List[str]]:
    """Fetch authors from arXiv API. Returns None on failure."""
    try:
        url = f"{ARXIV_API_BASE}?id_list={arxiv_id}&max_results=1"
        req = urllib.request.Request(url, headers={"User-Agent": "CEI-Vault/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
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


# ============================================================
# Semantic Scholar API
# ============================================================

def fetch_semantic_scholar_authors(doi: str) -> Optional[List[str]]:
    """Fetch authors from Semantic Scholar API. Returns None on failure."""
    try:
        url = f"{SEMANTIC_SCHOLAR_API}/DOI:{doi}?fields=authors"
        req = urllib.request.Request(url, headers={"User-Agent": "CEI-Vault/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.status != 200:
                return None
            data = json.loads(resp.read().decode())

        authors = []
        if "authors" in data:
            for a in data["authors"]:
                if "name" in a and a["name"]:
                    authors.append(a["name"])
        return authors if authors else None
    except Exception as e:
        print(f"    Semantic Scholar API error for DOI {doi}: {e}")
        return None


# ============================================================
# PDF Extract parsing
# ============================================================

def parse_authors_from_extract(extract_path: Path) -> Optional[List[str]]:
    """
    Try to extract author names from the first page of a PDF extract.

    Heuristic: authors appear between the title and "Abstract" keyword,
    before affiliation/email lines.
    """
    if not extract_path.exists():
        return None

    try:
        content = extract_path.read_text(encoding="utf-8")
    except Exception:
        return None

    # Get the body after YAML frontmatter (if any) in the extract
    fm_match = re.match(r"---\n.*?\n---\n", content, re.DOTALL)
    if fm_match:
        text = content[fm_match.end():]
    else:
        text = content

    # Take first ~3000 chars (page 1)
    first_page = text[:3000]

    # Strategy 1: Look for lines between title heading and "Abstract"
    # Extract title lines tend to be "# Title" or the first heading
    abstract_pos = -1
    for kw in ["Abstract", "ABSTRACT", "Introduction", "INTRODUCTION"]:
        idx = first_page.find(kw)
        if idx != -1:
            abstract_pos = idx
            break

    if abstract_pos == -1:
        abstract_pos = len(first_page)

    candidate_region = first_page[:abstract_pos]

    # Remove markdown headings and source info
    lines = candidate_region.split("\n")
    author_candidate_lines = []
    seen_heading = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        # Skip markdown headings
        if stripped.startswith("#"):
            seen_heading = True
            continue
        # Skip obvious non-author lines
        if any(kw in stripped.lower() for kw in [
            "source_pdf", "page_range", "extracted_on", "http",
            "university", "department", "institute", "laboratory",
            "school of", "college of", "faculty of",
            "@", ".edu", ".com", ".org",
            "correspondence", "equal contribution",
        ]):
            continue
        # Skip very short lines (page numbers, etc.)
        if len(stripped) < 5:
            continue
        # Skip lines that look like affiliations (start with number)
        if re.match(r"^\d+\s", stripped):
            continue
        if seen_heading:
            author_candidate_lines.append(stripped)

    if not author_candidate_lines:
        return None

    # Try to parse authors from the candidate lines
    # Common patterns: "Name1, Name2, Name3" or "Name1 Name2 Name3" (one per line)
    # or "Name1∗, Name2†, Name3‡" (with affiliation markers)
    authors = []
    for line in author_candidate_lines[:5]:  # Only first few lines
        # Remove affiliation markers: *, †, ‡, §, 1, 2, superscript chars
        cleaned = re.sub(r'[∗†‡§¶♯♮⋆✦✧★⊕⊗▽△▲▼♦♣♠♥]', '', line)
        cleaned = re.sub(r'[\u00B9\u00B2\u00B3\u2070-\u209F]', '', cleaned)  # superscripts
        cleaned = re.sub(r'\s*\d+\s*$', '', cleaned)  # trailing numbers
        cleaned = re.sub(r',\s*\d+', ',', cleaned)  # "Name1,2" → "Name1,"
        cleaned = cleaned.strip()

        if not cleaned:
            continue

        # Split on commas, semicolons, or " and "
        parts = re.split(r'\s*[,;]\s*|\s+and\s+', cleaned)
        for part in parts:
            part = part.strip()
            if not part:
                continue
            # A valid author name should have at least 2 words and start with uppercase
            words = part.split()
            if len(words) >= 2 and words[0][0].isupper():
                # Additional check: all words should be mostly alphabetic
                if all(re.match(r'^[A-Za-z\.\-\']+$', w) for w in words):
                    authors.append(part)

    return authors if authors else None


# ============================================================
# Surname extraction
# ============================================================

def extract_surname(full_name: str) -> str:
    """Extract surname from a full name (last whitespace-delimited token)."""
    parts = full_name.strip().split()
    if not parts:
        return "Unknown"
    return parts[-1]


def build_new_filename(old_filename: str, first_author_surname: str) -> str:
    """
    Replace the placeholder token in filename with first author surname.
    E.g.: 2024-Unknown-Title.md → 2024-Liu-Title.md
          2024-results-Title.md → 2024-Liu-Title.md
    """
    m = re.match(r'^(\d{4})-(Unknown|Authors|results)-(.*)', old_filename)
    if m:
        return f"{m.group(1)}-{first_author_surname}-{m.group(3)}"
    return old_filename


# ============================================================
# Resolution pipeline
# ============================================================

def resolve_paper(paper: Dict) -> Dict:
    """
    Attempt to resolve authors for a single paper.
    Returns a result dict with resolved info or unresolved status.
    """
    filename = paper["filename"]
    result = {
        "filename": filename,
        "resolved_authors": [],
        "first_author_surname": "",
        "resolution_source": "unresolved",
        "new_filename": filename,
        "status": "unresolved",
        "notes": "",
    }

    # --- Case 1: Already has real authors in YAML (rename-only) ---
    if not paper["has_placeholder_author"] and paper["has_placeholder_filename"]:
        authors_str = paper["authors_field"]
        # Parse semicolon-separated authors
        author_list = [a.strip() for a in re.split(r';\s*', authors_str) if a.strip()]
        # Clean "et al." entries
        author_list = [a for a in author_list if a.lower() not in ("et al", "et al.", "others")]
        if author_list:
            result["resolved_authors"] = author_list
            result["first_author_surname"] = extract_surname(author_list[0])
            result["resolution_source"] = "existing_yaml"
            result["new_filename"] = build_new_filename(filename, result["first_author_surname"])
            result["status"] = "resolved"
            print(f"  [YAML] {filename} → {result['first_author_surname']} (rename-only)")
            return result

    # --- Case 2: Try arXiv API ---
    arxiv_id = extract_arxiv_id(paper.get("url", ""))
    if not arxiv_id:
        arxiv_id = extract_arxiv_id(paper.get("external_pdf", ""))

    if arxiv_id:
        print(f"  [arXiv] Querying {arxiv_id} ...")
        authors = fetch_arxiv_authors(arxiv_id)
        if authors:
            result["resolved_authors"] = authors
            result["first_author_surname"] = extract_surname(authors[0])
            result["resolution_source"] = "arxiv_api"
            result["new_filename"] = build_new_filename(filename, result["first_author_surname"])
            result["status"] = "resolved"
            print(f"  [arXiv] {filename} → {authors[0]} + {len(authors)-1} others")
            return result
        time.sleep(3)  # arXiv rate limit

    # --- Case 3: Try Semantic Scholar API ---
    doi = paper.get("doi", "")
    if doi:
        print(f"  [S2] Querying DOI {doi} ...")
        authors = fetch_semantic_scholar_authors(doi)
        if authors:
            result["resolved_authors"] = authors
            result["first_author_surname"] = extract_surname(authors[0])
            result["resolution_source"] = "semantic_scholar"
            result["new_filename"] = build_new_filename(filename, result["first_author_surname"])
            result["status"] = "resolved"
            print(f"  [S2] {filename} → {authors[0]} + {len(authors)-1} others")
            return result
        time.sleep(10)  # S2 aggressive rate limit

    # --- Case 4: Try PDF extract parsing ---
    extract_rel = paper.get("pdf_extract", "")
    if extract_rel:
        extract_path = WORKSPACE_ROOT / extract_rel
        print(f"  [PDF] Parsing extract for {filename} ...")
        authors = parse_authors_from_extract(extract_path)
        if authors:
            result["resolved_authors"] = authors
            result["first_author_surname"] = extract_surname(authors[0])
            result["resolution_source"] = "pdf_extract"
            result["new_filename"] = build_new_filename(filename, result["first_author_surname"])
            result["status"] = "resolved"
            print(f"  [PDF] {filename} → {authors[0]} + {len(authors)-1} others")
            return result

    # --- Case 5: Unresolved ---
    print(f"  [FAIL] Could not resolve: {filename}")
    result["notes"] = "No arXiv URL, no DOI, and PDF extract parsing failed"
    return result


# ============================================================
# JSON I/O (merge-safe for parallel writes)
# ============================================================

def load_existing_results() -> Dict[str, Dict]:
    """Load existing results from JSON, keyed by filename."""
    if OUTPUT_JSON.exists():
        try:
            with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
                data = json.load(f)
            return {item["filename"]: item for item in data}
        except (json.JSONDecodeError, KeyError):
            return {}
    return {}


def save_results(results_map: Dict[str, Dict]):
    """Save results to JSON (atomic write, PID-scoped temp to avoid races)."""
    output_list = sorted(results_map.values(), key=lambda x: x["filename"])
    tmp = OUTPUT_JSON.parent / f".unknown_authors_resolved.tmp.{os.getpid()}"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(output_list, f, indent=2, ensure_ascii=False)
    os.replace(str(tmp), str(OUTPUT_JSON))  # atomic on POSIX, works even if target exists


# ============================================================
# Main
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Discover unknown authors")
    parser.add_argument("--start", type=int, default=None, help="Start index (1-based)")
    parser.add_argument("--end", type=int, default=None, help="End index (1-based, exclusive)")
    parser.add_argument("--mopup", action="store_true", help="Only process still-unresolved papers")
    args = parser.parse_args()

    print("=" * 80)
    print("DISCOVER UNKNOWN AUTHORS")
    print("=" * 80)

    # Step 1: Find all affected papers
    all_papers = find_affected_papers()
    print(f"Found {len(all_papers)} papers with placeholder authors/filenames")

    # Step 2: Determine which slice to process
    if args.mopup:
        # Only process papers that are still unresolved in the JSON
        existing = load_existing_results()
        papers = [p for p in all_papers
                  if p["filename"] not in existing
                  or existing[p["filename"]].get("status") == "unresolved"]
        print(f"Mop-up: {len(papers)} still unresolved")
    elif args.start is not None and args.end is not None:
        # 1-based indexing
        papers = all_papers[args.start - 1 : args.end - 1]
        print(f"Processing slice [{args.start}, {args.end}): {len(papers)} papers")
    else:
        papers = all_papers
        print(f"Processing all {len(papers)} papers")

    if not papers:
        print("Nothing to process.")
        return

    # Step 3: Load existing results for merge
    results_map = load_existing_results()

    # Step 4: Resolve each paper
    resolved_count = 0
    unresolved_count = 0

    for i, paper in enumerate(papers, 1):
        print(f"\n[{i}/{len(papers)}] {paper['filename']}")

        # Skip if already resolved (unless mopup mode)
        if not args.mopup and paper["filename"] in results_map:
            existing = results_map[paper["filename"]]
            if existing.get("status") == "resolved":
                print(f"  [SKIP] Already resolved → {existing.get('first_author_surname', '?')}")
                resolved_count += 1
                continue

        result = resolve_paper(paper)
        results_map[paper["filename"]] = result

        if result["status"] == "resolved":
            resolved_count += 1
        else:
            unresolved_count += 1

        # Save after each paper (crash-safe, merge-safe)
        save_results(results_map)

    # Step 5: Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    total_in_json = len(results_map)
    total_resolved = sum(1 for r in results_map.values() if r["status"] == "resolved")
    total_unresolved = sum(1 for r in results_map.values() if r["status"] == "unresolved")

    print(f"This run:  resolved={resolved_count}, unresolved={unresolved_count}")
    print(f"Total JSON: {total_in_json} entries, {total_resolved} resolved, {total_unresolved} unresolved")
    print(f"Output: {OUTPUT_JSON}")

    # List unresolved
    if total_unresolved > 0:
        print(f"\nUnresolved papers ({total_unresolved}):")
        for r in sorted(results_map.values(), key=lambda x: x["filename"]):
            if r["status"] == "unresolved":
                print(f"  - {r['filename']}")

    # Source breakdown
    sources = {}
    for r in results_map.values():
        src = r.get("resolution_source", "unresolved")
        sources[src] = sources.get(src, 0) + 1
    print(f"\nResolution sources: {json.dumps(sources, indent=2)}")


if __name__ == "__main__":
    main()
