#!/usr/bin/env python3
"""
enrich_paper_identifiers.py — Find DOIs and URLs for BACKGROUND registry entries.

Uses a cascading API lookup:
  1. CrossRef title search (best for DOIs, 1s delay)
  2. OpenAlex title search (fallback, 0.5s delay)
  3. Semantic Scholar title search (last resort, 10s delay)

Skips books (no downloadable PDFs) and already-enriched entries.

Usage:
    python3 scripts/enrich_paper_identifiers.py              # Enrich all
    python3 scripts/enrich_paper_identifiers.py --dry-run     # Preview only
    python3 scripts/enrich_paper_identifiers.py --report       # Show current status

Run from CULTURAL-GLOBAL/BACKGROUND/ or CEI-Lit-WS/ directory.
"""

from __future__ import annotations

import functools
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

print = functools.partial(print, flush=True)

BACKGROUND_DIR = Path(__file__).resolve().parent.parent
REGISTRY_PATH = BACKGROUND_DIR / "BACKGROUND-registry.json"

HEADERS = {
    "User-Agent": "CEI-Literature-Vault/2.0 (Academic Research; mailto:research@cei-literature.org)"
}

# ── Helpers ──────────────────────────────────────────────────────────────────

def normalize_title(title: str) -> str:
    """Lowercase, strip punctuation, collapse whitespace for fuzzy matching."""
    t = title.lower().strip()
    t = re.sub(r"[^\w\s]", "", t)
    t = re.sub(r"\s+", " ", t)
    return t


def titles_match(a: str, b: str, min_chars: int = 40) -> bool:
    """Check if two titles match on their first min_chars normalized characters."""
    na = normalize_title(a)
    nb = normalize_title(b)
    if not na or not nb:
        return False
    # Use min of actual length and min_chars
    cmp_len = min(min_chars, len(na), len(nb))
    return na[:cmp_len] == nb[:cmp_len]


def api_get(url: str, timeout: int = 30) -> dict | None:
    """GET JSON from an API endpoint. Returns None on error."""
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError,
            TimeoutError, OSError) as e:
        print(f"    API error: {e}")
        return None


# ── CrossRef ─────────────────────────────────────────────────────────────────

def search_crossref(title: str, year: str) -> dict | None:
    """Search CrossRef for a DOI by title + year. Returns {doi, url, source} or None."""
    encoded = urllib.parse.quote(title)
    url = f"https://api.crossref.org/works?query.title={encoded}&rows=3&mailto=research@cei-literature.org"
    data = api_get(url)
    if not data or "message" not in data:
        return None

    items = data["message"].get("items", [])
    for item in items:
        item_title = " ".join(item.get("title", []))
        if not item_title:
            continue

        # Check title match
        if not titles_match(title, item_title):
            continue

        # Check year if available
        issued = item.get("issued", {}).get("date-parts", [[]])
        item_year = str(issued[0][0]) if issued and issued[0] else ""
        if year and item_year and year != item_year:
            # Allow +/- 1 year for preprints vs published
            try:
                if abs(int(year) - int(item_year)) > 1:
                    continue
            except ValueError:
                continue

        doi = item.get("DOI", "")
        cr_url = item.get("URL", "")
        venue = " ".join(item.get("container-title", []))

        if doi:
            return {"doi": doi, "url": cr_url, "source": venue, "api": "crossref"}

    return None


# ── OpenAlex ─────────────────────────────────────────────────────────────────

def search_openalex(title: str, year: str) -> dict | None:
    """Search OpenAlex for a DOI by title. Returns {doi, url, source} or None."""
    encoded = urllib.parse.quote(title)
    url = f"https://api.openalex.org/works?search={encoded}&per_page=3&mailto=research@cei-literature.org"
    data = api_get(url)
    if not data or "results" not in data:
        return None

    for item in data["results"]:
        item_title = item.get("title", "")
        if not item_title or not titles_match(title, item_title):
            continue

        item_year = str(item.get("publication_year", ""))
        if year and item_year and year != item_year:
            try:
                if abs(int(year) - int(item_year)) > 1:
                    continue
            except ValueError:
                continue

        doi_url = item.get("doi", "")  # OpenAlex returns full URL like https://doi.org/10.xxx
        doi = doi_url.replace("https://doi.org/", "") if doi_url else ""

        oa_url = ""
        oa = item.get("open_access", {})
        if oa:
            oa_url = oa.get("oa_url", "") or ""

        # Primary location URL
        loc = item.get("primary_location", {}) or {}
        venue = ""
        src = loc.get("source", {}) or {}
        if src:
            venue = src.get("display_name", "")

        best_url = oa_url or doi_url or ""

        if doi:
            return {"doi": doi, "url": best_url, "source": venue, "api": "openalex"}

    return None


# ── Semantic Scholar ─────────────────────────────────────────────────────────

def search_semantic_scholar(title: str, year: str) -> dict | None:
    """Search Semantic Scholar for a DOI by title. Returns {doi, url, source} or None."""
    encoded = urllib.parse.quote(title)
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={encoded}&limit=3&fields=title,year,externalIds,url,venue"
    data = api_get(url)
    if not data or "data" not in data:
        return None

    for item in data["data"]:
        item_title = item.get("title", "")
        if not item_title or not titles_match(title, item_title):
            continue

        item_year = str(item.get("year", ""))
        if year and item_year and year != item_year:
            try:
                if abs(int(year) - int(item_year)) > 1:
                    continue
            except ValueError:
                continue

        ext = item.get("externalIds", {}) or {}
        doi = ext.get("DOI", "")
        s2_url = item.get("url", "")
        venue = item.get("venue", "")

        if doi:
            return {"doi": doi, "url": s2_url, "source": venue, "api": "semantic_scholar"}

    return None


# ── Main Pipeline ────────────────────────────────────────────────────────────

def enrich_entry(entry: dict, dry_run: bool = False) -> dict | None:
    """Try to find DOI/URL for an entry. Returns enrichment dict or None."""
    title = entry.get("title", "")
    year = entry.get("year", "")

    if not title:
        return None

    # 1. CrossRef (best for DOIs)
    print(f"  [CrossRef] Searching...")
    result = search_crossref(title, year)
    time.sleep(1.0)
    if result:
        return result

    # 2. OpenAlex (fallback)
    print(f"  [OpenAlex] Searching...")
    result = search_openalex(title, year)
    time.sleep(0.5)
    if result:
        return result

    # 3. Semantic Scholar (last resort)
    print(f"  [S2] Searching...")
    result = search_semantic_scholar(title, year)
    time.sleep(10.0)
    if result:
        return result

    return None


def main():
    dry_run = "--dry-run" in sys.argv
    report_only = "--report" in sys.argv

    if not REGISTRY_PATH.exists():
        print(f"ERROR: Registry not found at {REGISTRY_PATH}")
        sys.exit(1)

    with open(REGISTRY_PATH) as f:
        registry = json.load(f)

    print(f"Loaded {len(registry)} entries from registry")

    # Identify targets: missing DOI, not a book
    targets = []
    for i, entry in enumerate(registry):
        doi = entry.get("doi", "").strip()
        url = entry.get("url", "").strip()
        etype = entry.get("type", "")

        if etype == "book":
            continue

        # Target if missing DOI (primary goal)
        if not doi:
            targets.append((i, entry))

    print(f"Enrichment targets: {len(targets)} entries missing DOI (excluding books)")

    if report_only:
        has_doi = sum(1 for e in registry if e.get("doi", "").strip())
        has_url = sum(1 for e in registry if e.get("url", "").strip())
        books = sum(1 for e in registry if e.get("type") == "book")
        acquired = sum(1 for e in registry if e.get("document_acquired") is True)
        print(f"\n--- Registry Status ---")
        print(f"Total entries:     {len(registry)}")
        print(f"With DOI:          {has_doi}")
        print(f"With URL:          {has_url}")
        print(f"Books (skip):      {books}")
        print(f"PDFs acquired:     {acquired}")
        print(f"Need enrichment:   {len(targets)}")
        return

    if dry_run:
        print("\n--- DRY RUN: Would search for these entries ---")
        for idx, entry in targets:
            print(f"  [{idx+1}] [{entry.get('year')}] {entry.get('title','')[:80]}")
        return

    # Run enrichment
    stats = {"crossref": 0, "openalex": 0, "semantic_scholar": 0, "failed": 0, "skipped": 0}
    enriched_entries = []

    for count, (idx, entry) in enumerate(targets, 1):
        title = entry.get("title", "")[:80]
        print(f"\n[{count}/{len(targets)}] {entry.get('year', '?')} — {title}")

        result = enrich_entry(entry)

        if result:
            api_name = result["api"]
            stats[api_name] = stats.get(api_name, 0) + 1

            old_doi = registry[idx].get("doi", "")
            new_doi = result["doi"]
            registry[idx]["doi"] = new_doi

            # Only update URL if we found a better one (not empty)
            if result.get("url") and not registry[idx].get("url", "").strip():
                registry[idx]["url"] = result["url"]

            # Update source/venue if it was empty
            if result.get("source") and not registry[idx].get("source", "").strip():
                registry[idx]["source"] = result["source"]

            enriched_entries.append({
                "title": entry.get("title", ""),
                "doi": new_doi,
                "api": api_name
            })

            print(f"  FOUND via {api_name}: {new_doi}")
        else:
            stats["failed"] += 1
            print(f"  NOT FOUND")

    # Write updated registry (PID-scoped temp file + atomic replace)
    tmp_path = REGISTRY_PATH.with_suffix(f".tmp.{os.getpid()}.json")
    with open(tmp_path, "w") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
        f.write("\n")
    os.replace(str(tmp_path), str(REGISTRY_PATH))
    print(f"\nRegistry updated: {REGISTRY_PATH}")

    # Summary
    total_found = stats["crossref"] + stats["openalex"] + stats["semantic_scholar"]
    print(f"\n{'='*60}")
    print(f"ENRICHMENT SUMMARY")
    print(f"{'='*60}")
    print(f"Targets searched:     {len(targets)}")
    print(f"DOIs found:           {total_found}")
    print(f"  via CrossRef:       {stats['crossref']}")
    print(f"  via OpenAlex:       {stats['openalex']}")
    print(f"  via Semantic Scholar:{stats['semantic_scholar']}")
    print(f"Not found:            {stats['failed']}")

    # Count total DOIs now
    total_doi = sum(1 for e in registry if e.get("doi", "").strip())
    print(f"\nTotal entries with DOI: {total_doi}/{len(registry)}")

    # Write enrichment log
    log_path = BACKGROUND_DIR / "scripts" / "enrichment-log.json"
    log = {
        "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "targets": len(targets),
        "found": total_found,
        "by_api": {k: v for k, v in stats.items() if k != "failed" and k != "skipped"},
        "failed": stats["failed"],
        "entries": enriched_entries
    }
    with open(log_path, "w") as f:
        json.dump(log, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Log written: {log_path}")


if __name__ == "__main__":
    main()
