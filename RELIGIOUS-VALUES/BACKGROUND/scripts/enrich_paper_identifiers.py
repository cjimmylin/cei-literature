#!/usr/bin/env python3
"""
enrich_paper_identifiers.py — Enrich BACKGROUND paper markdown files with DOIs and URLs.

Scans paper .md files in numbered subdirectories. For papers missing DOI or URL,
queries CrossRef, OpenAlex, Semantic Scholar, and arXiv to find identifiers.
Updates frontmatter in-place using safe regex replacement.

Adapted from religion/GLOBAL-ORG-APPROACH/BACKGROUND/scripts/enrich_identifiers.py.

Usage:
    python3 scripts/enrich_paper_identifiers.py              # All papers needing enrichment
    python3 scripts/enrich_paper_identifiers.py 1 20         # Range (1-indexed)
    python3 scripts/enrich_paper_identifiers.py --report     # Show enrichment status
    python3 scripts/enrich_paper_identifiers.py --dry-run    # Show what would be enriched

Run from BACKGROUND/ directory.
"""
from __future__ import annotations

import functools
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
from pathlib import Path

print = functools.partial(print, flush=True)

BACKGROUND_DIR = Path(__file__).resolve().parent.parent
UNPAYWALL_EMAIL = "research@cei-literature.org"
HEADERS = {
    "User-Agent": "CEI-Literature-Vault/2.0 (Academic Research; mailto:research@cei-literature.org)"
}

RATE_LIMITS = {
    "crossref": 0.5,
    "openalex": 0.2,
    "semantic_scholar": 20.0,  # conservative — 12s still triggers 429
    "arxiv": 5.0,
}
_last_request: dict = {}


def _rate_limit(source: str):
    limit = RATE_LIMITS.get(source, 1.0)
    now = time.time()
    if source in _last_request:
        elapsed = now - _last_request[source]
        if elapsed < limit:
            time.sleep(limit - elapsed)
    _last_request[source] = time.time()


def api_get(url: str, source: str, timeout: int = 15) -> dict | None:
    _rate_limit(source)
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"    [{source} ERROR] {e}")
        return None


# ═══════════════════════════════════════════════════════════════════════════════
# Title matching
# ═══════════════════════════════════════════════════════════════════════════════

def _normalize_title(t: str) -> str:
    t = t.lower().strip()
    t = re.sub(r"[^a-z0-9\s]", "", t)
    return re.sub(r"\s+", " ", t)


def _titles_match(t1: str, t2: str) -> bool:
    n1 = _normalize_title(t1)
    n2 = _normalize_title(t2)
    if not n1 or not n2:
        return False
    if n1 == n2 or n1 in n2 or n2 in n1:
        return True
    words1 = set(n1.split())
    words2 = set(n2.split())
    shorter = min(words1, words2, key=len)
    longer = max(words1, words2, key=len)
    return len(shorter & longer) / max(len(shorter), 1) >= 0.85


def _validate_arxiv_id(arxiv_id: str) -> bool:
    m = re.match(r"^(\d{2})(\d{2})\.\d{4,5}$", arxiv_id)
    if not m:
        return False
    year = int(m.group(1))
    month = int(m.group(2))
    return 7 <= year <= 99 and 1 <= month <= 12


# ═══════════════════════════════════════════════════════════════════════════════
# API Search Functions
# ═══════════════════════════════════════════════════════════════════════════════

def search_crossref(title: str) -> str | None:
    """Search CrossRef for a DOI by title."""
    encoded = urllib.parse.quote(title)
    url = (
        f"https://api.crossref.org/works"
        f"?query.title={encoded}&rows=3&select=DOI,title,author,published"
    )
    data = api_get(url, "crossref")
    if not data:
        return None
    items = data.get("message", {}).get("items", [])
    for item in items:
        raw_title = item.get("title", [])
        candidate = raw_title[0] if isinstance(raw_title, list) and raw_title else str(raw_title)
        if candidate and _titles_match(title, candidate):
            doi = item.get("DOI", "")
            if doi:
                return doi
    return None


def search_openalex(title: str) -> tuple[str | None, str | None]:
    """Search OpenAlex. Returns (doi, oa_url) or (None, None)."""
    encoded = urllib.parse.quote(title)
    url = (
        f"https://api.openalex.org/works"
        f"?filter=title.search:{encoded}"
        f"&select=doi,title,open_access&per-page=3&mailto={UNPAYWALL_EMAIL}"
    )
    data = api_get(url, "openalex")
    if not data:
        return None, None
    for item in data.get("results", []):
        candidate = item.get("title", "") or ""
        if not _titles_match(title, candidate):
            continue
        doi = item.get("doi", "") or ""
        doi = re.sub(r"^https?://doi\.org/", "", doi).strip()
        oa = item.get("open_access", {}) or {}
        oa_url = oa.get("oa_url") or None
        return doi or None, oa_url
    return None, None


def search_semantic_scholar(title: str) -> tuple[str | None, str | None, str | None]:
    """Search S2. Returns (doi, arxiv_id, pdf_url) or (None, None, None)."""
    encoded = urllib.parse.quote(title)
    url = (
        f"https://api.semanticscholar.org/graph/v1/paper/search"
        f"?query={encoded}&limit=3&fields=title,externalIds,openAccessPdf"
    )
    data = api_get(url, "semantic_scholar")
    if not data:
        return None, None, None
    for paper in data.get("data", []):
        candidate = paper.get("title", "") or ""
        if not _titles_match(title, candidate):
            continue
        ext_ids = paper.get("externalIds", {}) or {}
        doi = ext_ids.get("DOI") or None
        arxiv_raw = ext_ids.get("ArXiv") or None
        arxiv_id = arxiv_raw if arxiv_raw and _validate_arxiv_id(arxiv_raw) else None
        oa_pdf = paper.get("openAccessPdf", {}) or {}
        pdf_url = oa_pdf.get("url") or None
        return doi, arxiv_id, pdf_url
    return None, None, None


def search_arxiv(title: str) -> str | None:
    """Search arXiv by title. Returns arXiv ID or None."""
    encoded = urllib.parse.quote(title)
    url = f"http://export.arxiv.org/api/query?search_query=ti:{encoded}&max_results=3"
    _rate_limit("arxiv")
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            xml = resp.read().decode("utf-8")
    except Exception:
        return None
    for entry in re.findall(r"<entry>(.*?)</entry>", xml, re.DOTALL):
        title_m = re.search(r"<title>(.*?)</title>", entry, re.DOTALL)
        if not title_m:
            continue
        candidate = title_m.group(1).strip()
        if not _titles_match(title, candidate):
            continue
        id_m = re.search(r"<id>http://arxiv\.org/abs/(\d{4}\.\d{4,5})(v\d+)?</id>", entry)
        if id_m and _validate_arxiv_id(id_m.group(1)):
            return id_m.group(1)
    return None


# ═══════════════════════════════════════════════════════════════════════════════
# Paper file operations
# ═══════════════════════════════════════════════════════════════════════════════

def _get_subdirs() -> list[Path]:
    return sorted(
        d for d in BACKGROUND_DIR.iterdir()
        if d.is_dir() and re.match(r'^\d{2}-', d.name)
    )


def _field(content: str, name: str) -> str:
    m = re.search(rf'^{re.escape(name)}:\s*"?([^\"\n]+?)"?\s*$', content, re.MULTILINE)
    return m.group(1).strip() if m else ""


def update_paper_field(paper_path: Path, field: str, value: str):
    """Update a YAML field in a paper file using safe regex replacement."""
    content = paper_path.read_text(encoding="utf-8")
    line = f"{field}: {value}" if value in ("true", "false") else f'{field}: "{value}"'

    if re.search(rf'^{re.escape(field)}:', content, re.MULTILINE):
        new_content = re.sub(
            rf'^{re.escape(field)}:.*$',
            line,
            content,
            count=1,
            flags=re.MULTILINE,
        )
    else:
        # Insert before closing ---
        m = re.search(r'^---\s*$', content[3:], re.MULTILINE)
        if m:
            insert_pos = 3 + m.start()
            new_content = content[:insert_pos] + line + "\n" + content[insert_pos:]
        else:
            new_content = content.rstrip() + f"\n{line}\n"

    paper_path.write_text(new_content, encoding="utf-8")


def load_papers_needing_enrichment() -> list[dict]:
    """Find papers missing DOI or URL."""
    papers = []
    for subdir in _get_subdirs():
        for f in sorted(subdir.iterdir()):
            if f.suffix != ".md":
                continue
            content = f.read_text(encoding="utf-8")

            # Skip already acquired
            if "document_acquired: true" in content:
                continue

            title = _field(content, "title")
            doi = _field(content, "doi")
            url = _field(content, "url")

            # Skip if both DOI and URL are present
            if doi and url:
                continue

            papers.append({
                "path": f,
                "stem": f.stem,
                "title": title,
                "doi": doi,
                "url": url,
                "folder": subdir.name,
            })
    return papers


def enrich_paper(paper: dict, idx: int, total: int, dry_run: bool = False) -> dict:
    """Enrich a single paper. Returns dict of new fields found."""
    title = paper["title"]
    if not title:
        return {}

    current_doi = paper["doi"]
    current_url = paper["url"]
    needs_doi = not current_doi
    needs_url = not current_url
    path = paper["path"]

    print(f"[{idx}/{total}] {title[:70]}...")

    if dry_run:
        print(f"  DRY RUN — needs: {'DOI ' if needs_doi else ''}{'URL' if needs_url else ''}")
        return {}

    found = {}

    # Strategy 1: CrossRef (fast, good for DOIs)
    if needs_doi:
        doi = search_crossref(title)
        if doi:
            found["doi"] = doi
            current_doi = doi
            needs_doi = False
            update_paper_field(path, "doi", doi)
            print(f"  + CrossRef DOI: {doi}")

    # Strategy 2: OpenAlex (DOI + OA URL)
    if needs_doi or needs_url:
        oa_doi, oa_url = search_openalex(title)
        if needs_doi and oa_doi:
            found["doi"] = oa_doi
            current_doi = oa_doi
            needs_doi = False
            update_paper_field(path, "doi", oa_doi)
            print(f"  + OpenAlex DOI: {oa_doi}")
        if needs_url and oa_url:
            found["url"] = oa_url
            current_url = oa_url
            needs_url = False
            update_paper_field(path, "url", oa_url)
            print(f"  + OpenAlex URL: {oa_url}")

    # Strategy 3: Semantic Scholar (DOI + arXiv + PDF URL)
    if needs_doi or needs_url:
        s2_doi, s2_arxiv, s2_pdf = search_semantic_scholar(title)
        if needs_doi and s2_doi:
            found["doi"] = s2_doi
            current_doi = s2_doi
            needs_doi = False
            update_paper_field(path, "doi", s2_doi)
            print(f"  + S2 DOI: {s2_doi}")
        if s2_arxiv:
            found["arxiv_id"] = s2_arxiv
            # Also set URL to arXiv if we had no URL
            if needs_url:
                arxiv_url = f"https://arxiv.org/abs/{s2_arxiv}"
                found["url"] = arxiv_url
                update_paper_field(path, "url", arxiv_url)
                needs_url = False
                print(f"  + S2 arXiv URL: {arxiv_url}")
        if needs_url and s2_pdf:
            found["url"] = s2_pdf
            update_paper_field(path, "url", s2_pdf)
            needs_url = False
            print(f"  + S2 PDF URL: {s2_pdf}")

    # Strategy 4: arXiv title search (last resort for CS/ML papers)
    if needs_doi or needs_url:
        arxiv_id = search_arxiv(title)
        if arxiv_id:
            found["arxiv_id"] = arxiv_id
            arxiv_url = f"https://arxiv.org/abs/{arxiv_id}"
            if needs_url:
                found["url"] = arxiv_url
                update_paper_field(path, "url", arxiv_url)
                needs_url = False
                print(f"  + arXiv URL: {arxiv_url}")

    # If we enriched anything, clear manual-download-required so re-download can try
    if found:
        content = path.read_text(encoding="utf-8")
        if 'download_status: "manual-download-required"' in content:
            update_paper_field(path, "download_status", "pending")
            print(f"  ~ Reset download_status to pending")
    else:
        print(f"  - no identifiers found")

    return found


# ═══════════════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════════════

def show_report():
    papers_total = 0
    acquired = 0
    has_doi = 0
    has_url = 0
    no_identifiers = 0
    manual = 0

    for subdir in _get_subdirs():
        for f in sorted(subdir.iterdir()):
            if f.suffix != ".md":
                continue
            content = f.read_text(encoding="utf-8")
            papers_total += 1
            doi = _field(content, "doi")
            url = _field(content, "url")
            if "document_acquired: true" in content:
                acquired += 1
            if doi:
                has_doi += 1
            if url:
                has_url += 1
            if not doi and not url:
                no_identifiers += 1
            if 'download_status: "manual-download-required"' in content:
                manual += 1

    print(f"=== BACKGROUND Enrichment Report ===")
    print(f"Total papers:        {papers_total}")
    print(f"  Acquired (PDF):    {acquired} ({100*acquired//papers_total}%)")
    print(f"  With DOI:          {has_doi} ({100*has_doi//papers_total}%)")
    print(f"  With URL:          {has_url} ({100*has_url//papers_total}%)")
    print(f"  No identifiers:    {no_identifiers} ({100*no_identifiers//papers_total}%)")
    print(f"  Manual-required:   {manual}")


def main():
    args = sys.argv[1:]

    if "--report" in args:
        show_report()
        return

    dry_run = "--dry-run" in args
    remaining = [a for a in args if not a.startswith("--")]

    start = int(remaining[0]) if remaining and remaining[0].isdigit() else 1
    end = int(remaining[1]) if len(remaining) > 1 and remaining[1].isdigit() else None

    papers = load_papers_needing_enrichment()
    total = len(papers)
    print(f"Found {total} papers needing enrichment")

    if end is None:
        end = total
    batch = papers[start - 1:end]
    print(f"Processing papers {start}-{end} ({len(batch)} papers)\n")

    enriched_doi = 0
    enriched_url = 0
    enriched_arxiv = 0

    for i, paper in enumerate(batch, start):
        found = enrich_paper(paper, i, end, dry_run=dry_run)
        if "doi" in found:
            enriched_doi += 1
        if "url" in found:
            enriched_url += 1
        if "arxiv_id" in found:
            enriched_arxiv += 1

    print(f"\n{'='*50}")
    print(f"Enriched: {enriched_doi} DOIs, {enriched_url} URLs, {enriched_arxiv} arXiv IDs")


if __name__ == "__main__":
    main()
