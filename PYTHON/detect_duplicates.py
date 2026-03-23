#!/usr/bin/env python3
"""
Detect Duplicate Papers in CEI Literature Vault

Scans all papers in papers/ and groups duplicates by matching:
  1. DOI (normalized, excluding arXiv DOIs)
  2. arXiv ID (extracted from url/external_pdf fields)
  3. Canonical URL (normalized)

For each group, scores "richness" of each paper to recommend a primary.

Output: logs/YYYYMMDD-duplicate_groups.json

Usage:
    python detect_duplicates.py
"""

import functools
import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Optional

# Force flush
print = functools.partial(print, flush=True)

# --- Path setup ---
SCRIPT_DIR = Path(__file__).parent.resolve()
WORKSPACE_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(WORKSPACE_ROOT / ".agent"))

from vault_config import PAPERS_DIR, PDFS_DIR, PDF_EXTRACTS_DIR, LOGS_DIR
from lib.yaml_utils import extract_frontmatter, parse_frontmatter


# ============================================================
# Identifier Extraction & Normalization
# ============================================================

ARXIV_ID_RE = re.compile(r'(\d{4}\.\d{4,5})')


def _is_valid_arxiv_id(candidate: str) -> bool:
    """Validate that a candidate arXiv ID has a plausible YYMM prefix."""
    yymm = candidate.split(".")[0]
    yy = int(yymm[:2])
    mm = int(yymm[2:])
    # arXiv new-format IDs started April 2007 (0704.xxxx)
    # Month must be 01-12, year 07-26 (current range)
    return 7 <= yy <= 26 and 1 <= mm <= 12


def normalize_doi(doi_str: str) -> Optional[str]:
    """Normalize DOI: lowercase, strip URL prefix, skip N/A and arXiv DOIs."""
    if not doi_str or doi_str.strip().upper() in ("N/A", ""):
        return None
    doi = doi_str.strip().lower()
    doi = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")
    doi = doi.replace("https://dx.doi.org/", "").replace("http://dx.doi.org/", "")
    doi = doi.strip('"').strip("'").strip()
    # Skip arXiv DOIs (10.48550/arXiv.*)
    if doi.startswith("10.48550/arxiv"):
        return None
    return doi if doi else None


def extract_arxiv_id(fields: dict) -> Optional[str]:
    """Extract arXiv ID from url, external_pdf, or doi fields.

    Only extracts from fields containing 'arxiv.org' or arXiv DOI prefix,
    and validates the YYMM prefix is plausible to avoid false matches
    from DOI substrings like 10.1145/3278721.3278753.
    """
    for field_name in ("url", "external_pdf", "doi"):
        value = fields.get(field_name, "")
        if not value:
            continue
        value_lower = value.lower()
        # Only extract arXiv IDs from arXiv-related URLs/DOIs
        if "arxiv.org" not in value_lower and "10.48550" not in value_lower:
            continue
        m = ARXIV_ID_RE.search(value)
        if m and _is_valid_arxiv_id(m.group(1)):
            return m.group(1)
    return None


def normalize_url(url_str: str) -> Optional[str]:
    """Normalize URL for comparison: https, lowercase host, strip trailing /."""
    if not url_str or url_str.strip().upper() in ("N/A", ""):
        return None
    url = url_str.strip().strip('"').strip("'")
    # Skip arXiv URLs (already captured by arXiv ID extraction)
    if "arxiv.org" in url.lower():
        return None
    # Normalize
    url = url.replace("http://", "https://")
    url = url.rstrip("/")
    # Lowercase the host part only
    if url.startswith("https://"):
        rest = url[8:]
        if "/" in rest:
            host, path = rest.split("/", 1)
            url = f"https://{host.lower()}/{path}"
        else:
            url = f"https://{rest.lower()}"
    return url if url else None


# ============================================================
# Richness Scoring
# ============================================================

def compute_richness(fields: dict, body: str, key: str) -> int:
    """
    Score how rich/complete a paper's metadata is.
    Higher = more metadata, prefer as primary.
    """
    score = 0

    # Content quality
    if fields.get("key_contribution", "").strip() and fields.get("key_contribution", "").strip().upper() != "N/A":
        score += 2
    if fields.get("significance", "").strip() and fields.get("significance", "").strip().upper() != "N/A":
        score += 2

    abstract = fields.get("abstract", "")
    if len(abstract) > 100:
        score += 2

    # Identifier quality
    doi = fields.get("doi", "")
    if doi and doi.strip().upper() != "N/A":
        score += 1

    if fields.get("publication", "").strip():
        score += 1

    # Check for pages
    pages = fields.get("pages", "")
    if pages and pages.strip().upper() != "N/A":
        score += 1
    elif "**Pages:**" in body:
        score += 1

    # PDF quality
    local_pdf = fields.get("local_pdf", "")
    if "[[" in local_pdf and "]]" in local_pdf:
        score += 1

    if fields.get("pdf_extract", "").strip():
        score += 1

    # Author quality
    first_author = fields.get("first_author", "")
    if "[[" in first_author and "]]" in first_author:
        score += 1

    # Body quality
    if "## Abstract" in body and len(body.split("## Abstract", 1)[-1].split("##")[0].strip()) > 50:
        score += 1
    if "## Citation Info" in body or "## Citation" in body:
        score += 1

    # EXSR penalty (imported papers tend to have less curated metadata)
    if key.startswith("EXSR"):
        score -= 2
    # AUTO penalty (auto-enriched)
    if key.startswith("AUTO_"):
        score -= 1

    return score


# ============================================================
# Main Detection
# ============================================================

def main():
    today = date.today().strftime("%Y%m%d")

    print("=" * 80)
    print("DUPLICATE PAPER DETECTION")
    print("=" * 80)

    # --- Load all papers ---
    papers = []
    for paper_path in sorted(PAPERS_DIR.glob("*.md")):
        try:
            content = paper_path.read_text(encoding="utf-8")
            fm_text, body = extract_frontmatter(content)
            fields = parse_frontmatter(fm_text)
            key = fields.get("key", "")
            papers.append({
                "filename": paper_path.name,
                "stem": paper_path.stem,
                "key": key,
                "fields": fields,
                "body": body,
                "richness": compute_richness(fields, body, key),
            })
        except Exception as e:
            print(f"  WARNING: Could not parse {paper_path.name}: {e}")

    print(f"Loaded {len(papers)} papers")

    # --- Build identifier indices ---
    # Maps: identifier_type:value → [paper_info, ...]
    doi_index = defaultdict(list)
    arxiv_index = defaultdict(list)
    url_index = defaultdict(list)

    for p in papers:
        fields = p["fields"]

        # DOI
        doi = normalize_doi(fields.get("doi", ""))
        if doi:
            doi_index[doi].append(p)

        # arXiv ID
        arxiv_id = extract_arxiv_id(fields)
        if arxiv_id:
            arxiv_index[arxiv_id].append(p)

        # URL
        url = normalize_url(fields.get("url", ""))
        if url:
            url_index[url].append(p)

    # --- Find groups with 2+ papers ---
    # Use Union-Find to merge papers sharing any identifier
    parent = {}

    def find(x):
        while parent.get(x, x) != x:
            parent[x] = parent.get(parent[x], parent[x])
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    # Initialize all papers
    for p in papers:
        parent[p["filename"]] = p["filename"]

    # Union by DOI
    for doi, group in doi_index.items():
        if len(group) >= 2:
            for i in range(1, len(group)):
                union(group[0]["filename"], group[i]["filename"])

    # Union by arXiv ID
    for arxiv_id, group in arxiv_index.items():
        if len(group) >= 2:
            for i in range(1, len(group)):
                union(group[0]["filename"], group[i]["filename"])

    # Union by URL
    for url, group in url_index.items():
        if len(group) >= 2:
            for i in range(1, len(group)):
                union(group[0]["filename"], group[i]["filename"])

    # Collect groups
    groups_map = defaultdict(list)
    for p in papers:
        root = find(p["filename"])
        groups_map[root].append(p)

    # Filter to groups with 2+ members
    dup_groups = {root: members for root, members in groups_map.items() if len(members) >= 2}

    print(f"Found {len(dup_groups)} duplicate groups ({sum(len(m) for m in dup_groups.values())} papers total)")

    # --- Determine shared identifiers for each group ---
    paper_by_name = {p["filename"]: p for p in papers}

    def get_shared_ids(members):
        """Find which identifiers are shared across group members."""
        filenames = {m["filename"] for m in members}
        shared = []

        # Check DOIs
        for doi, group in doi_index.items():
            group_fns = {p["filename"] for p in group}
            overlap = filenames & group_fns
            if len(overlap) >= 2:
                shared.append({"type": "doi", "value": doi})

        # Check arXiv IDs
        for arxiv_id, group in arxiv_index.items():
            group_fns = {p["filename"] for p in group}
            overlap = filenames & group_fns
            if len(overlap) >= 2:
                shared.append({"type": "arxiv", "value": arxiv_id})

        # Check URLs
        for url, group in url_index.items():
            group_fns = {p["filename"] for p in group}
            overlap = filenames & group_fns
            if len(overlap) >= 2:
                shared.append({"type": "url", "value": url})

        return shared

    # --- Build output ---
    output_groups = []
    group_id = 0

    for root, members in sorted(dup_groups.items()):
        group_id += 1

        # Sort by richness (descending), then by key prefix (non-EXSR first), then filename length
        members_sorted = sorted(
            members,
            key=lambda m: (
                -m["richness"],
                1 if m["key"].startswith("EXSR") else (0.5 if m["key"].startswith("AUTO_") else 0),
                len(m["filename"]),
            ),
        )

        # Mark primary (highest richness)
        shared_ids = get_shared_ids(members)

        group_entry = {
            "group_id": group_id,
            "shared_identifiers": shared_ids,
            "papers": [],
        }

        for i, m in enumerate(members_sorted):
            is_primary = (i == 0)
            fields = m["fields"]

            # Check if PDF and extract exist on disk
            local_pdf = fields.get("local_pdf", "")
            pdf_filename = local_pdf.strip('"').strip("[]").replace("Lit-WS-PDFs/", "")
            if pdf_filename:
                pdf_path = PDFS_DIR / pdf_filename
                has_pdf = pdf_path.exists()
            else:
                has_pdf = False

            extract_ref = fields.get("pdf_extract", "")
            if extract_ref:
                extract_path = PDF_EXTRACTS_DIR / extract_ref.strip('"').replace("PDF Extracts/", "")
                has_extract = extract_path.exists()
            else:
                has_extract = False

            group_entry["papers"].append({
                "filename": m["filename"],
                "key": m["key"],
                "richness_score": m["richness"],
                "is_primary": is_primary,
                "has_pdf_on_disk": has_pdf,
                "has_extract_on_disk": has_extract,
                "doi": fields.get("doi", ""),
                "year": fields.get("year", ""),
                "first_author": fields.get("first_author", ""),
            })

        output_groups.append(group_entry)

    # --- Print summary ---
    print(f"\n{'='*80}")
    print("DUPLICATE GROUPS FOUND")
    print(f"{'='*80}")

    for g in output_groups:
        primary = [p for p in g["papers"] if p["is_primary"]][0]
        duplicates = [p for p in g["papers"] if not p["is_primary"]]
        ids_str = ", ".join(f"{s['type']}:{s['value']}" for s in g["shared_identifiers"])

        print(f"\n  Group {g['group_id']}: {ids_str}")
        print(f"    PRIMARY: {primary['filename']} (key={primary['key']}, richness={primary['richness_score']}, pdf={primary['has_pdf_on_disk']}, extract={primary['has_extract_on_disk']})")
        for d in duplicates:
            print(f"    RECYCLE: {d['filename']} (key={d['key']}, richness={d['richness_score']}, pdf={d['has_pdf_on_disk']}, extract={d['has_extract_on_disk']})")

    # --- Save output ---
    output_path = LOGS_DIR / f"{today}-duplicate_groups.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_groups, f, indent=2, ensure_ascii=False)

    print(f"\n  Output: {output_path.relative_to(WORKSPACE_ROOT)}")
    print(f"\n  Total groups: {len(output_groups)}")
    print(f"  Total papers in groups: {sum(len(g['papers']) for g in output_groups)}")
    print(f"  Papers to recycle: {sum(len(g['papers']) - 1 for g in output_groups)}")


if __name__ == "__main__":
    main()
