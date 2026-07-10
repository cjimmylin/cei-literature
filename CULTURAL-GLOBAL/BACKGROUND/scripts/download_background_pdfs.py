#!/usr/bin/env python3
"""
download_background_pdfs.py — Waterfall PDF downloader for CULTURAL-GLOBAL BACKGROUND papers.

Adapted from RELIGIOUS-VALUES/BACKGROUND/scripts/download_background_pdfs.py.

Download strategy (cascading waterfall):
  1.  arXiv direct (if arxiv_id detected from DOI or URL)
  2.  Preprint direct (medRxiv/bioRxiv from DOI pattern)
  3.  Zenodo Records API (10.5281/zenodo.* DOIs)
  4.  Unpaywall API (via DOI)
  5.  EuropePMC REST API (via DOI)
  6.  OA Button API (via DOI)
  7.  Semantic Scholar PDF link (via DOI or arXiv ID)
  8.  OpenAlex OA URL (via DOI)
  9.  Direct URL if it looks like a PDF
  10. Handle.net (follow redirect, scrape bitstream)
  11. URL scrape (fetch paper URL as HTML, hunt for PDF link)
  12. DOI scrape (follow doi.org redirect, parse publisher page)
  13. Semantic Scholar URL scrape (if url is semanticscholar.org)
  14. CORE.ac.uk title-based search
  15. Mark as manual_required if all fail

Books and book_chapters are auto-marked manual_required without download attempts.

Usage:
    python3 scripts/download_background_pdfs.py                     # All papers
    python3 scripts/download_background_pdfs.py 1 10               # Range (1-indexed)
    python3 scripts/download_background_pdfs.py --dry-run           # Show what would download
    python3 scripts/download_background_pdfs.py --report            # Show download status

Run from CULTURAL-GLOBAL/BACKGROUND/ or CEI-Lit-WS/ directory.
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
REGISTRY_PATH = BACKGROUND_DIR / "BACKGROUND-registry.json"
DOCS_DIR = BACKGROUND_DIR / "Documents"
CURL_TIMEOUT = 60
MAX_RETRIES = 2
UNPAYWALL_EMAIL = "research@cei-literature.org"

HEADERS = {
    "User-Agent": "CEI-Literature-Vault/2.0 (Academic Research; mailto:research@cei-literature.org)"
}

RATE_LIMITS = {
    "unpaywall": 1.0,
    "semantic_scholar": 10.0,
    "arxiv": 3.0,
    "openalex": 0.5,
    "direct": 2.0,
    "preprint": 2.0,
    "zenodo": 1.0,
    "oa_button": 1.0,
    "doi_scrape": 3.0,
    "core": 1.0,
    "europepmc": 0.5,
    "handle_net": 1.0,
    "s2_scrape": 3.0,
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


# ═══════════════════════════════════════════════════════════════════════════════
# PDF Download
# ═══════════════════════════════════════════════════════════════════════════════

def download_pdf(url: str, output_path: Path, retries: int = MAX_RETRIES) -> tuple[bool, str]:
    """Download a PDF using curl with retry and %PDF- header validation."""
    for attempt in range(retries + 1):
        try:
            result = subprocess.run(
                [
                    "curl", "-sS", "-L",
                    "-o", str(output_path),
                    "-w", "%{http_code}",
                    "--max-time", str(CURL_TIMEOUT),
                    "--connect-timeout", "15",
                    "-H", f"User-Agent: {HEADERS['User-Agent']}",
                    url,
                ],
                capture_output=True, text=True, timeout=CURL_TIMEOUT + 10,
            )
            http_code = result.stdout.strip()

            if http_code == "200":
                if output_path.exists() and output_path.stat().st_size > 1000:
                    with open(output_path, "rb") as fh:
                        header = fh.read(5)
                    if header == b"%PDF-":
                        return True, "OK"
                    else:
                        output_path.unlink(missing_ok=True)
                        return False, "Not a valid PDF"
                elif output_path.exists():
                    size = output_path.stat().st_size
                    output_path.unlink(missing_ok=True)
                    return False, f"File too small ({size} bytes)"

            elif http_code == "429":
                output_path.unlink(missing_ok=True)
                if attempt < retries:
                    wait = 15 * (attempt + 1)
                    print(f"      HTTP 429 — waiting {wait}s before retry...")
                    time.sleep(wait)
                    continue
                return False, "HTTP 429 rate limited"

            # Non-200 response — clean up the HTML error page curl wrote
            if output_path.exists():
                output_path.unlink(missing_ok=True)
            return False, f"HTTP {http_code}"

        except subprocess.TimeoutExpired:
            if output_path.exists():
                output_path.unlink(missing_ok=True)
            if attempt < retries:
                continue
            return False, "Timeout"
        except Exception as e:
            return False, str(e)

    return False, "Max retries exceeded"


# ═══════════════════════════════════════════════════════════════════════════════
# Download Strategies
# ═══════════════════════════════════════════════════════════════════════════════

def _extract_arxiv_id(doi: str, url: str) -> str:
    """Extract arXiv ID from DOI or URL."""
    if doi:
        m = re.search(r'10\.48550/arxiv\.(\d{4}\.\d{4,5})', doi, re.IGNORECASE)
        if m:
            return m.group(1)
    if url:
        m = re.search(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})', url)
        if m:
            return m.group(1)
    return ""


def try_arxiv(arxiv_id: str, output_path: Path) -> tuple[bool, str]:
    if not arxiv_id:
        return False, "No arXiv ID"
    if not re.match(r'^\d{4}\.\d{4,5}(v\d+)?$', arxiv_id):
        return False, f"Invalid arXiv ID: {arxiv_id}"
    url = f"https://arxiv.org/pdf/{arxiv_id}"
    _rate_limit("arxiv")
    return download_pdf(url, output_path)


def try_preprint_direct(doi: str, output_path: Path) -> tuple[bool, str]:
    if not doi:
        return False, "No DOI"
    _rate_limit("preprint")
    if doi.startswith("10.1101/"):
        pdf_url = f"https://www.medrxiv.org/content/{doi}/full.pdf"
        ok, msg = download_pdf(pdf_url, output_path)
        if ok:
            return ok, msg
        pdf_url2 = f"https://www.biorxiv.org/content/{doi}/full.pdf"
        return download_pdf(pdf_url2, output_path)
    if doi.startswith("10.36227/techrxiv.") or "techrxiv" in doi:
        doi_url = f"https://doi.org/{doi}"
        try:
            req = urllib.request.Request(doi_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as resp:
                html = resp.read().decode("utf-8", errors="ignore")
            m = re.search(r'href="(https?://[^"]+\.pdf)"', html)
            if m:
                return download_pdf(m.group(1), output_path)
        except Exception as e:
            return False, f"TechRxiv scrape failed: {e}"
    return False, "Not a recognized preprint DOI pattern"


def try_zenodo(doi: str, output_path: Path) -> tuple[bool, str]:
    if not doi or not doi.startswith("10.5281/zenodo."):
        return False, "Not a Zenodo DOI"
    record_id = doi.split("zenodo.")[-1]
    url = f"https://zenodo.org/api/records/{record_id}"
    data = api_get(url, "zenodo")
    if not data:
        return False, "Zenodo: no response"
    files = data.get("files", [])
    for f in files:
        links = f.get("links", {})
        dl_url = links.get("self") or links.get("download")
        if dl_url and (dl_url.lower().endswith(".pdf") or f.get("type") == "pdf"):
            return download_pdf(dl_url, output_path)
    return False, "Zenodo: no PDF file found"


def try_unpaywall(doi: str, output_path: Path) -> tuple[bool, str]:
    if not doi:
        return False, "No DOI"
    encoded_doi = urllib.parse.quote(doi, safe="")
    url = f"https://api.unpaywall.org/v2/{encoded_doi}?email={UNPAYWALL_EMAIL}"
    data = api_get(url, "unpaywall")
    if not data:
        return False, "Unpaywall: no response"
    best = data.get("best_oa_location") or {}
    pdf_url = best.get("url_for_pdf") or best.get("url")
    if not pdf_url:
        return False, "Unpaywall: no OA PDF found"
    return download_pdf(pdf_url, output_path)


def try_europepmc(doi: str, output_path: Path) -> tuple[bool, str]:
    if not doi:
        return False, "No DOI"
    encoded_doi = urllib.parse.quote(doi, safe="")
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:{encoded_doi}&format=json&resultType=core"
    data = api_get(url, "europepmc")
    if not data:
        return False, "EuropePMC: no response"
    results = data.get("resultList", {}).get("result", [])
    if not results:
        return False, "EuropePMC: no results"
    result = results[0]
    full_text_list = result.get("fullTextUrlList", {}).get("fullTextUrl", [])
    pdf_url = None
    for entry in full_text_list:
        availability = entry.get("availabilityCode", "")
        doc_style = entry.get("documentStyle", "")
        url_val = entry.get("url", "")
        if doc_style == "pdf" and availability in ("OA", "F"):
            pdf_url = url_val
            break
        if doc_style == "html" and availability in ("OA", "F") and not pdf_url:
            pdf_url = url_val
    if not pdf_url:
        pmc_id = result.get("pmcid")
        if pmc_id:
            pdf_url = f"https://europepmc.org/articles/{pmc_id}/pdf/render"
    if not pdf_url:
        return False, "EuropePMC: no OA PDF found"
    return download_pdf(pdf_url, output_path)


def try_oa_button(doi: str, output_path: Path) -> tuple[bool, str]:
    if not doi:
        return False, "No DOI"
    encoded_doi = urllib.parse.quote(doi, safe="")
    url = f"https://api.openaccessbutton.org/find?id={encoded_doi}"
    data = api_get(url, "oa_button")
    if not data:
        return False, "OA Button: no response"
    pdf_url = data.get("url")
    if not pdf_url:
        return False, "OA Button: no URL found"
    return download_pdf(pdf_url, output_path)


def try_semantic_scholar(doi: str, arxiv_id: str, output_path: Path) -> tuple[bool, str]:
    if doi:
        encoded = urllib.parse.quote(f"DOI:{doi}")
    elif arxiv_id:
        encoded = urllib.parse.quote(f"ARXIV:{arxiv_id}")
    else:
        return False, "No DOI or arXiv ID"
    url = f"https://api.semanticscholar.org/graph/v1/paper/{encoded}?fields=openAccessPdf"
    data = api_get(url, "semantic_scholar")
    if not data:
        return False, "S2: no response"
    oa_pdf = data.get("openAccessPdf") or {}
    pdf_url = oa_pdf.get("url")
    if not pdf_url:
        return False, "S2: no OA PDF"
    return download_pdf(pdf_url, output_path)


def try_openalex(doi: str, output_path: Path) -> tuple[bool, str]:
    if not doi:
        return False, "No DOI"
    encoded_doi = urllib.parse.quote(doi)
    url = f"https://api.openalex.org/works/https://doi.org/{encoded_doi}?select=open_access&mailto={UNPAYWALL_EMAIL}"
    data = api_get(url, "openalex")
    if not data:
        return False, "OpenAlex: no response"
    oa = data.get("open_access") or {}
    pdf_url = oa.get("oa_url")
    if not pdf_url:
        return False, "OpenAlex: no OA URL"
    return download_pdf(pdf_url, output_path)


def try_direct_url(url: str, output_path: Path) -> tuple[bool, str]:
    if not url:
        return False, "No URL"
    if url.lower().endswith(".pdf") or "/pdf" in url.lower():
        _rate_limit("direct")
        return download_pdf(url, output_path)
    return False, "Direct URL: not a PDF endpoint"


def try_handle_net(url: str, output_path: Path) -> tuple[bool, str]:
    if not url or "hdl.handle.net" not in url:
        return False, "Not a handle.net URL"
    _rate_limit("handle_net")
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20) as resp:
            content_type = resp.headers.get("Content-Type", "")
            if "application/pdf" in content_type:
                return download_pdf(resp.geturl(), output_path)
            final_url = resp.geturl()
            html = resp.read().decode("utf-8", errors="ignore")
    except Exception as e:
        return False, f"Handle.net fetch error: {e}"

    from urllib.parse import urljoin
    for pattern in [
        r'href="([^"]*bitstream[^"]*\.pdf[^"]*)"',
        r'href="([^"]+\.pdf)"',
    ]:
        m = re.search(pattern, html, re.IGNORECASE)
        if m:
            link = m.group(1)
            pdf_url = link if link.startswith("http") else urljoin(final_url, link)
            ok, msg = download_pdf(pdf_url, output_path)
            if ok:
                return True, f"Handle.net -> {pdf_url[:80]}"
    return False, "Handle.net: no PDF link found"


def try_url_scrape(url: str, output_path: Path) -> tuple[bool, str]:
    if not url:
        return False, "No URL"
    if url.lower().endswith(".pdf"):
        return False, "URL scrape: already tried as direct PDF"

    _rate_limit("doi_scrape")
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20) as resp:
            content_type = resp.headers.get("Content-Type", "")
            if "application/pdf" in content_type:
                final_url = resp.geturl()
                return download_pdf(final_url, output_path)
            final_url = resp.geturl()
            html = resp.read().decode("utf-8", errors="ignore")
    except Exception as e:
        return False, f"URL scrape fetch error: {e}"

    from urllib.parse import urlparse, urljoin
    parsed_base = urlparse(final_url)
    base = f"{parsed_base.scheme}://{parsed_base.netloc}"

    pdf_url = None

    # Semantic Scholar paper page — look for PDF link
    if "semanticscholar.org" in final_url:
        for pattern in [
            r'"url":"(https?://[^"]+\.pdf[^"]*)"',
            r'href="(https?://[^"]+\.pdf[^"]*)"',
            r'"pdfUrl":"([^"]+)"',
        ]:
            m = re.search(pattern, html)
            if m:
                pdf_url = m.group(1)
                break

    # Generic PDF link patterns
    if not pdf_url:
        for pattern in [
            r'href="([^"]*\.pdf[^"]*)"',
            r"href='([^']*\.pdf[^']*)'",
            r'href="([^"]+)"[^>]*>\s*(?:Download|PDF|Full\s+Text)',
            r'"downloadUrl"\s*:\s*"([^"]+)"',
            r'"pdf_url"\s*:\s*"([^"]+)"',
            r'"pdfUrl"\s*:\s*"([^"]+)"',
        ]:
            m = re.search(pattern, html, re.IGNORECASE)
            if m:
                link = m.group(1)
                if link.startswith("http"):
                    pdf_url = link
                elif link.startswith("/"):
                    pdf_url = base + link
                else:
                    pdf_url = urljoin(final_url, link)
                break

    if not pdf_url:
        return False, "URL scrape: no PDF link found on page"

    ok, msg = download_pdf(pdf_url, output_path)
    if not ok:
        return False, f"URL scrape: found {pdf_url[:80]}... but download failed: {msg}"
    return True, f"URL scrape -> {pdf_url[:80]}"


def try_doi_scrape(doi: str, output_path: Path) -> tuple[bool, str]:
    if not doi:
        return False, "No DOI"

    _rate_limit("doi_scrape")
    try:
        doi_url = f"https://doi.org/{doi}"
        req = urllib.request.Request(doi_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            final_url = resp.geturl()
            html = resp.read().decode("utf-8", errors="ignore")

        from urllib.parse import urljoin

        pdf_url = None

        if "nature.com" in final_url:
            m = re.search(r'href="(/articles/[^"]+\.pdf)"', html)
            if m:
                pdf_url = "https://www.nature.com" + m.group(1)

        elif "springer.com" in final_url or "link.springer.com" in final_url:
            m = re.search(r'href="(/content/pdf/[^"]+\.pdf)"', html)
            if m:
                pdf_url = "https://link.springer.com" + m.group(1)

        elif "mdpi.com" in final_url:
            m_att = re.search(r'href="(https?://mdpi-res\.com/d_attachment/[^"]+)"', html)
            if m_att:
                pdf_url = m_att.group(1)
            elif "/pdf" not in final_url:
                pdf_url = final_url.rstrip("/") + "/pdf"

        elif "sciencedirect.com" in final_url:
            m = re.search(r'"pdfLink":"([^"]+)"', html)
            if m:
                pdf_url = m.group(1).replace("\\u002F", "/")

        elif "pnas.org" in final_url:
            m = re.search(r'href="([^"]+\.full\.pdf)"', html)
            if m:
                pdf_url = m.group(1) if m.group(1).startswith("http") else "https://www.pnas.org" + m.group(1)

        elif "dl.acm.org" in final_url:
            m = re.search(r'href="(/doi/pdf/[^"]+)"', html)
            if m:
                pdf_url = "https://dl.acm.org" + m.group(1)

        elif "sagepub.com" in final_url or "journals.sagepub.com" in final_url:
            m = re.search(r'href="(/doi/pdf/[^"]+)"', html)
            if m:
                pdf_url = "https://journals.sagepub.com" + m.group(1)

        elif "tandfonline.com" in final_url:
            m = re.search(r'href="(/doi/pdf/[^"]+)"', html)
            if m:
                pdf_url = "https://www.tandfonline.com" + m.group(1)

        elif "wiley.com" in final_url or "onlinelibrary.wiley.com" in final_url:
            m = re.search(r'href="(/doi/pdfdirect/[^"]+)"', html)
            if not m:
                m = re.search(r'href="(/doi/pdf/[^"]+)"', html)
            if m:
                pdf_url = "https://onlinelibrary.wiley.com" + m.group(1)

        elif "degruyter.com" in final_url:
            m = re.search(r'href="([^"]+/pdf[^"]*)"', html)
            if m:
                link = m.group(1)
                pdf_url = link if link.startswith("http") else "https://www.degruyter.com" + link

        elif "cambridge.org" in final_url:
            m = re.search(r'href="(/core/services/aop-cambridge-core/content/view/[^"]+)"', html)
            if m:
                pdf_url = "https://www.cambridge.org" + m.group(1)

        elif "plosone.org" in final_url or "plos.org" in final_url:
            m = re.search(r'(https://journals\.plos\.org/[^"]+representation=PDF)', html)
            if m:
                pdf_url = m.group(1)

        elif "frontiersin.org" in final_url:
            m = re.search(r'href="([^"]+/pdf)"', html)
            if m:
                link = m.group(1)
                pdf_url = link if link.startswith("http") else urljoin(final_url, link)

        elif "royalsocietypublishing.org" in final_url:
            m = re.search(r'href="(/doi/pdf/[^"]+)"', html)
            if m:
                pdf_url = "https://royalsocietypublishing.org" + m.group(1)

        # Generic fallback: first .pdf link on the page
        if not pdf_url:
            pdf_links = re.findall(r'href="([^"]*\.pdf[^"]*)"', html)
            if pdf_links:
                link = pdf_links[0]
                if link.startswith("http"):
                    pdf_url = link
                elif link.startswith("/"):
                    from urllib.parse import urlparse
                    parsed = urlparse(final_url)
                    pdf_url = f"{parsed.scheme}://{parsed.netloc}{link}"

        if not pdf_url:
            return False, "DOI scrape: no PDF link found on publisher page"

        return download_pdf(pdf_url, output_path)

    except Exception as e:
        return False, f"DOI scrape error: {e}"


def try_s2_paper_scrape(url: str, doi: str, title: str, output_path: Path) -> tuple[bool, str]:
    """Strategy 13: For Semantic Scholar URLs, use the S2 API to find the paper and its PDF."""
    # Extract S2 paper ID from URL
    s2_id = ""
    if url and "semanticscholar.org/paper/" in url:
        # URL like: https://www.semanticscholar.org/paper/9e908da74710ecdcac794a847564939390008374
        parts = url.rstrip("/").split("/")
        s2_id = parts[-1]
        # Sometimes the URL has title slug: .../paper/Title-Slug/hexid
        if not re.match(r'^[0-9a-f]{20,}$', s2_id):
            # The hex ID might be the last segment anyway
            pass

    if not s2_id:
        return False, "Not a Semantic Scholar URL"

    _rate_limit("semantic_scholar")
    api_url = f"https://api.semanticscholar.org/graph/v1/paper/{s2_id}?fields=openAccessPdf,externalIds"
    data = api_get(api_url, "semantic_scholar")
    if not data:
        return False, "S2 scrape: no API response"

    oa_pdf = data.get("openAccessPdf") or {}
    pdf_url = oa_pdf.get("url")
    if pdf_url:
        ok, msg = download_pdf(pdf_url, output_path)
        if ok:
            return True, f"S2 paper API -> {pdf_url[:80]}"

    # Try to get DOI from S2 and use Unpaywall
    ext_ids = data.get("externalIds") or {}
    s2_doi = ext_ids.get("DOI")
    if s2_doi and not doi:
        # Try Unpaywall with the discovered DOI
        encoded_doi = urllib.parse.quote(s2_doi, safe="")
        uw_url = f"https://api.unpaywall.org/v2/{encoded_doi}?email={UNPAYWALL_EMAIL}"
        uw_data = api_get(uw_url, "unpaywall")
        if uw_data:
            best = uw_data.get("best_oa_location") or {}
            pdf_url2 = best.get("url_for_pdf") or best.get("url")
            if pdf_url2:
                ok, msg = download_pdf(pdf_url2, output_path)
                if ok:
                    return True, f"S2->Unpaywall -> {pdf_url2[:80]}"

    return False, "S2 scrape: no PDF available"


def _normalize_title(title: str) -> str:
    t = title.lower().strip()
    t = re.sub(r"[^a-z0-9\s]", "", t)
    t = re.sub(r"\s+", " ", t)
    return t


def _titles_match(t1: str, t2: str) -> bool:
    n1 = _normalize_title(t1)
    n2 = _normalize_title(t2)
    if not n1 or not n2:
        return False
    if n1 == n2:
        return True
    if n1 in n2 or n2 in n1:
        return True
    words1 = set(n1.split())
    words2 = set(n2.split())
    if not words1 or not words2:
        return False
    shorter = words1 if len(words1) <= len(words2) else words2
    longer = words2 if len(words1) <= len(words2) else words1
    overlap = len(shorter & longer) / len(shorter)
    return overlap >= 0.85


def try_core(title: str, output_path: Path) -> tuple[bool, str]:
    if not title:
        return False, "No title"
    query = urllib.parse.quote(title[:120])
    url = f"https://api.core.ac.uk/v3/search/works?q={query}&limit=3"
    data = api_get(url, "core")
    if not data or not data.get("results"):
        return False, "CORE: no results"
    for work in data["results"][:3]:
        work_title = work.get("title", "")
        if _titles_match(title, work_title):
            dl_url = work.get("downloadUrl")
            if dl_url:
                return download_pdf(dl_url, output_path)
    return False, "CORE: no matching paper with download URL"


# ═══════════════════════════════════════════════════════════════════════════════
# Registry I/O
# ═══════════════════════════════════════════════════════════════════════════════

def load_registry() -> list[dict]:
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_registry(entries: list[dict]):
    tmp = REGISTRY_PATH.with_suffix(f".tmp.{__import__('os').getpid()}.json")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)
        f.write("\n")
    import os
    os.replace(str(tmp), str(REGISTRY_PATH))


# ═══════════════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════════════

def run_downloads(start: int = 1, end: Optional[int] = None, dry_run: bool = False):
    DOCS_DIR.mkdir(exist_ok=True)
    entries = load_registry()

    # Filter to entries needing download
    pending = [
        (i, e) for i, e in enumerate(entries)
        if e.get("document_acquired") == False  # noqa: E712
    ]
    total = len(pending)
    print(f"Found {total} papers needing PDFs (of {len(entries)} total)\n")

    if end is None:
        end = total
    batch = pending[start - 1:end]
    print(f"Processing papers {start}-{min(end, total)} ({len(batch)} papers)\n")

    success = 0
    failed = 0
    manual = 0
    skipped_books = 0

    for seq, (registry_idx, entry) in enumerate(batch, start):
        title = entry.get("title", "unknown")
        local_doc = entry.get("local_document", "")
        entry_type = entry.get("type", "")
        doi = entry.get("doi", "") or ""
        url = entry.get("url", "") or ""
        arxiv_id = _extract_arxiv_id(doi, url)

        print(f"[{seq}/{min(end, total)}] {title[:80]}")
        print(f"    Type: {entry_type} | DOI: {doi[:40] or 'none'} | URL: {url[:50] or 'none'}")

        # Auto-skip books and book chapters
        if entry_type in ("book", "book_chapter"):
            print(f"  -> SKIP (book/chapter — manual_required)")
            entries[registry_idx]["document_acquired"] = "manual_required"
            skipped_books += 1
            manual += 1
            continue

        if dry_run:
            print(f"  DRY RUN — would try waterfall")
            continue

        # Determine output filename from local_document field
        if local_doc:
            pdf_filename = Path(local_doc).name
        else:
            # Fallback: construct from entry data
            first_author = (entry.get("authors") or ["Unknown"])[0].split(",")[0].strip()
            short_title = re.sub(r'[^\w\s]', '', title)[:40].strip().title().replace(' ', ' ')
            words = short_title.split()[:6]
            short_title = ' '.join(words)
            pdf_filename = f"{entry.get('year', 'YYYY')}-{first_author}-{short_title}.pdf"

        output_path = DOCS_DIR / pdf_filename

        # If PDF already on disk and valid, just mark acquired
        if output_path.exists() and output_path.stat().st_size > 1000:
            with open(output_path, "rb") as fh:
                if fh.read(5) == b"%PDF-":
                    print(f"  OK Already on disk: {pdf_filename}")
                    entries[registry_idx]["document_acquired"] = True
                    success += 1
                    continue

        # Waterfall strategies
        strategies = [
            ("arXiv",             lambda: try_arxiv(arxiv_id, output_path)),
            ("Preprint Direct",   lambda: try_preprint_direct(doi, output_path)),
            ("Zenodo",            lambda: try_zenodo(doi, output_path)),
            ("Unpaywall",         lambda: try_unpaywall(doi, output_path)),
            ("EuropePMC",         lambda: try_europepmc(doi, output_path)),
            ("OA Button",         lambda: try_oa_button(doi, output_path)),
            ("Semantic Scholar",  lambda: try_semantic_scholar(doi, arxiv_id, output_path)),
            ("OpenAlex",          lambda: try_openalex(doi, output_path)),
            ("Direct URL",        lambda: try_direct_url(url, output_path)),
            ("Handle.net",        lambda: try_handle_net(url, output_path)),
            ("URL Scrape",        lambda: try_url_scrape(url, output_path)),
            ("DOI Scrape",        lambda: try_doi_scrape(doi, output_path)),
            ("S2 Paper Scrape",   lambda: try_s2_paper_scrape(url, doi, title, output_path)),
            ("CORE",              lambda: try_core(title, output_path)),
        ]

        downloaded = False
        for strategy_name, strategy_fn in strategies:
            ok, msg = strategy_fn()
            if ok:
                print(f"  OK {strategy_name}: {pdf_filename}")
                entries[registry_idx]["document_acquired"] = True
                downloaded = True
                success += 1
                break
            else:
                print(f"  X  {strategy_name}: {msg}")

        if not downloaded:
            print(f"  -> MANUAL DOWNLOAD REQUIRED")
            entries[registry_idx]["document_acquired"] = "manual_required"
            manual += 1
            failed += 1

        # Save registry periodically (every 10 papers)
        if (seq - start + 1) % 10 == 0:
            save_registry(entries)
            print(f"  [Registry saved at {seq}]")

    # Final save
    if not dry_run:
        save_registry(entries)
        print(f"\nRegistry saved to {REGISTRY_PATH}")

    print(f"\n{'='*60}")
    print(f"Results:")
    print(f"  Downloaded:       {success}")
    print(f"  Books (skipped):  {skipped_books}")
    print(f"  Manual required:  {manual}")
    print(f"  Failed:           {failed}")
    rate = (success / len(batch) * 100) if batch else 0
    print(f"  Acquisition rate: {rate:.1f}%")


def show_report():
    entries = load_registry()
    total = len(entries)
    acquired = sum(1 for e in entries if e.get("document_acquired") == True)  # noqa: E712
    manual = sum(1 for e in entries if e.get("document_acquired") == "manual_required")
    pending = total - acquired - manual

    print(f"Papers: {total}")
    print(f"  Acquired:        {acquired} ({100*acquired//total if total else 0}%)")
    print(f"  Manual needed:   {manual}")
    print(f"  Pending:         {pending}")

    docs = list(DOCS_DIR.glob("*.pdf")) if DOCS_DIR.exists() else []
    print(f"\nDocuments in Documents/: {len(docs)}")

    # Type breakdown
    types: dict[str, dict[str, int]] = {}
    for e in entries:
        t = e.get("type", "unknown")
        if t not in types:
            types[t] = {"total": 0, "acquired": 0, "manual": 0}
        types[t]["total"] += 1
        if e.get("document_acquired") == True:  # noqa: E712
            types[t]["acquired"] += 1
        elif e.get("document_acquired") == "manual_required":
            types[t]["manual"] += 1

    print(f"\nBy type:")
    for t, counts in sorted(types.items()):
        print(f"  {t:20s}: {counts['total']:3d} total | {counts['acquired']:3d} acquired | {counts['manual']:3d} manual")


if __name__ == "__main__":
    args = sys.argv[1:]

    if "--report" in args:
        show_report()
    elif "--dry-run" in args:
        remaining = [a for a in args if a != "--dry-run"]
        s = int(remaining[0]) if remaining and remaining[0].isdigit() else 1
        e = int(remaining[1]) if len(remaining) > 1 and remaining[1].isdigit() else None
        run_downloads(s, e, dry_run=True)
    else:
        s = int(args[0]) if args and args[0].isdigit() else 1
        e = int(args[1]) if len(args) > 1 and args[1].isdigit() else None
        run_downloads(s, e, dry_run=False)
