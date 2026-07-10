#!/usr/bin/env python3
"""
download_papers.py — Download PDFs for moral psychology background papers.

Reads search-results.json from each thematic folder, attempts to download
each paper using a multi-strategy waterfall, and updates download status.

Adapted from RELIGIOUS-VALUES/BACKGROUND/scripts/download_background_pdfs.py.

Usage:
    cd CEI-Lit-WS/MORAL-PSYCH/BACKGROUND
    ../../../.venv/bin/python scripts/download_papers.py              # All folders
    ../../../.venv/bin/python scripts/download_papers.py --folder 02  # Single folder
    ../../../.venv/bin/python scripts/download_papers.py --dry-run    # Show plan
    ../../../.venv/bin/python scripts/download_papers.py --report     # Status report
"""
from __future__ import annotations

import functools
import json
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
from pathlib import Path
from typing import Optional

print = functools.partial(print, flush=True)

BACKGROUND_DIR = Path(__file__).resolve().parent.parent
CURL_TIMEOUT = 60
MAX_RETRIES = 2
UNPAYWALL_EMAIL = "research@cei-literature.org"

HEADERS = {
    "User-Agent": "CEI-Literature-Vault/2.0 (Academic Research; mailto:research@cei-literature.org)"
}

RATE_LIMITS = {
    "unpaywall": 1.0, "semantic_scholar": 10.0, "arxiv": 3.0,
    "openalex": 0.1, "direct": 2.0, "doi_scrape": 3.0,
}

_last_request_time: dict = {}


def _rate_limit(source: str):
    limit = RATE_LIMITS.get(source, 1.0)
    now = time.time()
    if source in _last_request_time:
        elapsed = now - _last_request_time[source]
        if elapsed < limit:
            time.sleep(limit - elapsed)
    _last_request_time[source] = time.time()


def api_get(url: str, source: str, timeout: int = 15) -> Optional[dict]:
    _rate_limit(source)
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception:
        return None


def download_pdf(url: str, output_path: Path) -> tuple[bool, str]:
    """Download a PDF using curl with %PDF- header validation."""
    for attempt in range(MAX_RETRIES + 1):
        try:
            result = subprocess.run(
                ["curl", "-sS", "-L", "-o", str(output_path),
                 "-w", "%{http_code}", "--max-time", str(CURL_TIMEOUT),
                 "--connect-timeout", "15",
                 "-H", f"User-Agent: {HEADERS['User-Agent']}", url],
                capture_output=True, text=True, timeout=CURL_TIMEOUT + 10,
            )
            code = result.stdout.strip()
            if code == "200" and output_path.exists() and output_path.stat().st_size > 1000:
                with open(output_path, "rb") as fh:
                    header = fh.read(5)
                if header == b"%PDF-":
                    return True, "OK"
                # Check if it's HTML (for HTML downloads)
                if header[:1] == b"<" or b"<!DOCTYPE" in fh.read(50):
                    return True, "HTML"
                output_path.unlink(missing_ok=True)
                return False, "Not a valid PDF"
            if code == "429":
                output_path.unlink(missing_ok=True)
                if attempt < MAX_RETRIES:
                    time.sleep(15 * (attempt + 1))
                    continue
            output_path.unlink(missing_ok=True)
            return False, f"HTTP {code}"
        except subprocess.TimeoutExpired:
            output_path.unlink(missing_ok=True)
        except Exception as e:
            return False, str(e)
    return False, "Max retries exceeded"


def download_html(url: str, output_path: Path) -> tuple[bool, str]:
    """Download HTML page as fallback."""
    try:
        result = subprocess.run(
            ["curl", "-sS", "-L", "-o", str(output_path),
             "-w", "%{http_code}", "--max-time", str(CURL_TIMEOUT),
             "-H", f"User-Agent: {HEADERS['User-Agent']}", url],
            capture_output=True, text=True, timeout=CURL_TIMEOUT + 10,
        )
        code = result.stdout.strip()
        if code == "200" and output_path.exists() and output_path.stat().st_size > 500:
            return True, "HTML"
        output_path.unlink(missing_ok=True)
        return False, f"HTTP {code}"
    except Exception as e:
        return False, str(e)


# ── Waterfall strategies ──────────────────────────────────────────────

def extract_arxiv_id(url: str) -> str:
    """Extract arXiv ID from URL."""
    if not url:
        return ""
    m = re.search(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})', url)
    return m.group(1) if m else ""


def extract_doi(url: str) -> str:
    """Extract DOI from URL or doi field."""
    if not url:
        return ""
    if url.startswith("10."):
        return url
    m = re.search(r'doi\.org/(10\.\d{4,}/[^\s]+)', url)
    return m.group(1) if m else ""


def try_download(paper: dict, output_dir: Path) -> tuple[bool, str, str]:
    """Try multiple strategies to download a paper. Returns (success, method, filepath)."""
    title = paper.get("title", "Unknown")
    authors = paper.get("authors", "Unknown")
    year = paper.get("year", 2025)
    url = paper.get("doi_or_url", "") or paper.get("download_url", "") or ""
    download_url = paper.get("download_url", "") or ""

    # Build filename
    first_author = authors.split(",")[0].split(" and ")[0].split(";")[0].strip()
    last_name = first_author.split()[-1] if first_author else "Unknown"
    short_title = re.sub(r'[^\w\s-]', '', title)[:40].strip().replace(" ", "-")
    filename = f"{year}-{last_name}-{short_title}"

    arxiv_id = extract_arxiv_id(url) or extract_arxiv_id(download_url)
    doi = extract_doi(url) if not arxiv_id else ""

    # Strategy 1: Direct download URL (if provided and looks like PDF)
    if download_url and download_url.lower().endswith(".pdf"):
        pdf_path = output_dir / f"{filename}.pdf"
        _rate_limit("direct")
        ok, msg = download_pdf(download_url, pdf_path)
        if ok:
            return True, "direct_pdf", str(pdf_path)

    # Strategy 2: arXiv
    if arxiv_id:
        pdf_path = output_dir / f"{filename}.pdf"
        _rate_limit("arxiv")
        ok, msg = download_pdf(f"https://arxiv.org/pdf/{arxiv_id}", pdf_path)
        if ok:
            return True, "arxiv", str(pdf_path)

    # Strategy 3: Unpaywall (via DOI)
    if doi:
        pdf_path = output_dir / f"{filename}.pdf"
        encoded_doi = urllib.parse.quote(doi, safe="")
        data = api_get(f"https://api.unpaywall.org/v2/{encoded_doi}?email={UNPAYWALL_EMAIL}", "unpaywall")
        if data:
            best = data.get("best_oa_location") or {}
            pdf_url = best.get("url_for_pdf") or best.get("url")
            if pdf_url:
                ok, msg = download_pdf(pdf_url, pdf_path)
                if ok:
                    return True, "unpaywall", str(pdf_path)

    # Strategy 4: Semantic Scholar
    if doi or arxiv_id:
        pdf_path = output_dir / f"{filename}.pdf"
        query = f"DOI:{doi}" if doi else f"ARXIV:{arxiv_id}"
        encoded = urllib.parse.quote(query)
        data = api_get(f"https://api.semanticscholar.org/graph/v1/paper/{encoded}?fields=openAccessPdf", "semantic_scholar")
        if data:
            oa = data.get("openAccessPdf") or {}
            pdf_url = oa.get("url")
            if pdf_url:
                ok, msg = download_pdf(pdf_url, pdf_path)
                if ok:
                    return True, "semantic_scholar", str(pdf_path)

    # Strategy 5: OpenAlex
    if doi:
        pdf_path = output_dir / f"{filename}.pdf"
        encoded_doi = urllib.parse.quote(doi)
        data = api_get(f"https://api.openalex.org/works/https://doi.org/{encoded_doi}?select=open_access&mailto={UNPAYWALL_EMAIL}", "openalex")
        if data:
            oa = data.get("open_access") or {}
            pdf_url = oa.get("oa_url")
            if pdf_url:
                ok, msg = download_pdf(pdf_url, pdf_path)
                if ok:
                    return True, "openalex", str(pdf_path)

    # Strategy 6: Direct URL as PDF
    if url and (".pdf" in url.lower() or "arxiv" in url.lower()):
        pdf_path = output_dir / f"{filename}.pdf"
        _rate_limit("direct")
        ok, msg = download_pdf(url, pdf_path)
        if ok:
            return True, "direct_url", str(pdf_path)

    # Strategy 7: HTML fallback
    if url:
        html_path = output_dir / f"{filename}.html"
        ok, msg = download_html(url, html_path)
        if ok:
            return True, "html_fallback", str(html_path)

    return False, "all_failed", ""


def load_search_results(folder_path: Path) -> list:
    """Load papers from a folder's search-results.json."""
    sr_path = folder_path / "search-results.json"
    if not sr_path.exists():
        return []
    with open(sr_path) as f:
        data = json.load(f)
    return data.get("papers", [])


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", help="Only process this folder number (e.g., 02)")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--report", action="store_true")
    args = parser.parse_args()

    folders = sorted([d for d in BACKGROUND_DIR.iterdir()
                      if d.is_dir() and d.name[:2].isdigit()])

    if args.folder:
        folders = [d for d in folders if d.name.startswith(args.folder)]

    total_found = 0
    total_downloaded = 0
    total_failed = 0
    registry = []

    for folder in folders:
        papers = load_search_results(folder)
        if not papers:
            print(f"  {folder.name}: no search-results.json found, skipping")
            continue

        print(f"\n{'='*60}")
        print(f"  {folder.name}: {len(papers)} papers")
        print(f"{'='*60}")

        for i, paper in enumerate(papers):
            total_found += 1
            title = paper.get("title", "?")[:60]

            if args.dry_run:
                print(f"  [{i+1}/{len(papers)}] Would download: {title}")
                continue

            if args.report:
                status = paper.get("download_status", "pending")
                print(f"  [{i+1}] {status}: {title}")
                continue

            print(f"  [{i+1}/{len(papers)}] {title}...")
            ok, method, filepath = try_download(paper, folder)

            paper["download_status"] = "success" if ok else "failed"
            paper["download_method"] = method
            paper["local_file"] = filepath

            if ok:
                total_downloaded += 1
                print(f"    ✓ {method}: {Path(filepath).name}")
            else:
                total_failed += 1
                print(f"    ✗ {method}")

            registry.append({
                "folder": folder.name,
                "title": paper.get("title", ""),
                "authors": paper.get("authors", ""),
                "year": paper.get("year", 0),
                "doi_or_url": paper.get("doi_or_url", ""),
                "download_status": paper.get("download_status"),
                "download_method": method,
                "local_file": filepath,
                "relevance": paper.get("relevance", "medium"),
            })

        # Write updated search-results back
        if not args.dry_run and not args.report:
            sr_path = folder / "search-results.json"
            if sr_path.exists():
                with open(sr_path) as f:
                    data = json.load(f)
                data["papers"] = papers
                sr_path.write_text(json.dumps(data, indent=2, ensure_ascii=False))

    # Write registry
    if not args.dry_run and not args.report and registry:
        registry_path = BACKGROUND_DIR / "20260403-background-registry.json"
        output = {
            "registry_date": "2026-04-03",
            "total_found": total_found,
            "total_downloaded": total_downloaded,
            "total_failed": total_failed,
            "by_folder": {},
            "papers": registry,
        }
        for folder in folders:
            fname = folder.name
            folder_papers = [p for p in registry if p["folder"] == fname]
            output["by_folder"][fname] = {
                "found": len(folder_papers),
                "downloaded": sum(1 for p in folder_papers if p["download_status"] == "success"),
            }
        registry_path.write_text(json.dumps(output, indent=2, ensure_ascii=False))
        print(f"\nRegistry: {registry_path}")

    print(f"\nTotal: {total_found} found, {total_downloaded} downloaded, {total_failed} failed")


if __name__ == "__main__":
    main()
