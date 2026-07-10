"""Targeted gap search for Pacific Island and Buddhist AI ethics papers.

Searches Semantic Scholar API for specific gap categories identified
by the CULTURAL-GLOBAL project analysis.

Output: LITERATURE-SEARCH/20260403-targeted-gap-search-results.json
"""
from __future__ import annotations

import functools
import json
import os
import re
import string
import time
from pathlib import Path
from urllib.parse import quote

import requests

print = functools.partial(print, flush=True)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
WS_ROOT = Path(__file__).resolve().parent.parent.parent  # CEI-Lit-WS
PAPERS_DIR = WS_ROOT / "papers"
OUTPUT_DIR = WS_ROOT / "CULTURAL-GLOBAL" / "LITERATURE-SEARCH"
OUTPUT_FILE = OUTPUT_DIR / "20260403-targeted-gap-search-results.json"

# ---------------------------------------------------------------------------
# Search queries
# ---------------------------------------------------------------------------
PACIFIC_QUERIES = [
    "Pacific Island AI ethics governance",
    "Tongan values technology artificial intelligence",
    "Samoan ethics digital governance",
    "Fijian cultural values AI",
    "Papua New Guinea technology ethics governance",
    "Hawaiian indigenous AI data sovereignty",
    "Pasifika digital ethics",
    "Pacific cultural values artificial intelligence",
]

BUDDHIST_QUERIES = [
    "Buddhist ethics artificial intelligence",
    "Thai Buddhist ethics technology",
    "Sri Lankan Buddhist digital ethics",
    "Tibetan Buddhist AI alignment",
    "Buddhist mindfulness AI machine ethics",
    "Buddhist compassion artificial intelligence alignment",
    "engaged Buddhism technology ethics",
    "Buddhist robot ethics autonomous systems",
]

API_DELAY = 15  # seconds between requests
SS_ENDPOINT = "https://api.semanticscholar.org/graph/v1/paper/search"
SS_FIELDS = "title,authors,year,url,abstract,externalIds"

# ---------------------------------------------------------------------------
# Load vault titles for dedup
# ---------------------------------------------------------------------------

def load_vault_titles() -> set[str]:
    """Return set of normalised title prefixes (first 30 chars, lower, no punct)."""
    titles: set[str] = set()
    if not PAPERS_DIR.exists():
        print(f"WARNING: papers dir not found at {PAPERS_DIR}")
        return titles
    for md in PAPERS_DIR.iterdir():
        if not md.name.endswith(".md"):
            continue
        try:
            text = md.read_text(errors="replace")
        except Exception:
            continue
        m = re.search(r'^short_title:\s*["\']?(.+?)["\']?\s*$', text[:3000], re.MULTILINE)
        if m:
            titles.add(_normalise(m.group(1)))
        # also try title: field
        m2 = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', text[:3000], re.MULTILINE)
        if m2:
            titles.add(_normalise(m2.group(1)))
    return titles


def _normalise(t: str) -> str:
    t = t.lower().translate(str.maketrans("", "", string.punctuation))
    return t[:30].strip()


def check_in_vault(title: str, vault_titles: set[str]) -> bool:
    return _normalise(title) in vault_titles


# ---------------------------------------------------------------------------
# Semantic Scholar search
# ---------------------------------------------------------------------------

def search_semantic_scholar(query: str) -> list[dict]:
    """Run one query against Semantic Scholar, return list of paper dicts."""
    params = {
        "query": query,
        "limit": 10,
        "fields": SS_FIELDS,
    }
    try:
        resp = requests.get(SS_ENDPOINT, params=params, timeout=30)
        if resp.status_code == 429:
            print(f"  HTTP 429 — rate limited. Waiting 60s and retrying...")
            time.sleep(60)
            resp = requests.get(SS_ENDPOINT, params=params, timeout=30)
            if resp.status_code == 429:
                print(f"  Still 429 after retry. Waiting 90s for second retry...")
                time.sleep(90)
                resp = requests.get(SS_ENDPOINT, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        return data.get("data", [])
    except Exception as e:
        print(f"  ERROR: {e}")
        return []


def format_authors(authors_list: list[dict]) -> str:
    if not authors_list:
        return "Unknown"
    first = authors_list[0].get("name", "Unknown")
    if len(authors_list) > 1:
        return f"{first} et al."
    return first


def format_paper(raw: dict, gap_category: str, vault_titles: set[str]) -> dict | None:
    title = raw.get("title")
    if not title:
        return None
    abstract = raw.get("abstract") or ""
    description = abstract[:200].strip()
    if len(abstract) > 200:
        description += "..."

    url = raw.get("url") or ""
    ext_ids = raw.get("externalIds") or {}
    if not url and ext_ids.get("DOI"):
        url = f"https://doi.org/{ext_ids['DOI']}"
    if not url and ext_ids.get("ArXiv"):
        url = f"https://arxiv.org/abs/{ext_ids['ArXiv']}"

    return {
        "title": title,
        "authors": format_authors(raw.get("authors", [])),
        "year": raw.get("year"),
        "url": url,
        "source": "Semantic Scholar",
        "gap_category": gap_category,
        "in_vault": check_in_vault(title, vault_titles),
        "description": description,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("Loading vault titles for dedup check...")
    vault_titles = load_vault_titles()
    print(f"  Loaded {len(vault_titles)} normalised title variants from vault")

    all_papers: list[dict] = []
    seen_titles: set[str] = set()  # dedup across queries

    query_groups = [
        ("Pacific Island", PACIFIC_QUERIES),
        ("Buddhist-specific AI ethics", BUDDHIST_QUERIES),
    ]

    total_queries = len(PACIFIC_QUERIES) + len(BUDDHIST_QUERIES)
    query_num = 0

    for gap_category, queries in query_groups:
        for query in queries:
            query_num += 1
            print(f"[{query_num}/{total_queries}] Searching: {query!r}  ({gap_category})")
            results = search_semantic_scholar(query)
            print(f"  Got {len(results)} results")

            added = 0
            for raw in results:
                paper = format_paper(raw, gap_category, vault_titles)
                if paper is None:
                    continue
                norm = _normalise(paper["title"])
                if norm in seen_titles:
                    continue
                seen_titles.add(norm)
                all_papers.append(paper)
                added += 1
            print(f"  Added {added} new (after dedup)")

            if query_num < total_queries:
                print(f"  Waiting {API_DELAY}s (rate limit)...")
                time.sleep(API_DELAY)

    # Tally
    by_region: dict[str, int] = {}
    for p in all_papers:
        cat = p["gap_category"]
        by_region[cat] = by_region.get(cat, 0) + 1

    output = {
        "date": "20260403",
        "total_found": len(all_papers),
        "search_queries_executed": total_queries,
        "by_region": by_region,
        "papers": all_papers,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    tmp_path = OUTPUT_FILE.with_suffix(f".tmp.{os.getpid()}.json")
    with open(tmp_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    os.replace(tmp_path, OUTPUT_FILE)
    print(f"\nWrote {len(all_papers)} papers to {OUTPUT_FILE}")

    # Summary
    in_vault = sum(1 for p in all_papers if p["in_vault"])
    not_in_vault = len(all_papers) - in_vault
    print(f"\n=== SUMMARY ===")
    print(f"Total unique papers found: {len(all_papers)}")
    print(f"Already in vault: {in_vault}")
    print(f"NEW (not in vault): {not_in_vault}")
    for cat, count in by_region.items():
        cat_new = sum(1 for p in all_papers if p["gap_category"] == cat and not p["in_vault"])
        print(f"  {cat}: {count} total, {cat_new} new")


if __name__ == "__main__":
    main()
