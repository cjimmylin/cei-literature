#!/usr/bin/env python3
"""
advanced_download.py — 13 advanced PDF acquisition strategies for Religious Values BACKGROUND papers.

Targets papers with download_status: "manual-download-required" that survived the
original 13-strategy waterfall. Adds strategies 14-26:

  14. OpenAlex Full Locations     — iterate ALL locations[], not just best_oa_location
  15. CrossRef Link Extraction    — link[] with content-type:application/pdf
  16. Semantic Scholar Title      — title search (strategy 7 was DOI-only)
  17. arXiv Title Search          — Atom XML query by title
  18. PubMed Central ID Converter — DOI→PMCID→PMC PDF
  19. SSRN Playwright             — headless Chromium (--playwright flag required)
  20. Wayback Machine CDX API     — archived PDF snapshots
  21. Internet Archive Scholar    — scholar.archive.org title search
  22. BASE Search                 — Bielefeld Academic Search Engine (300M+ docs)
  23. Law Review Digital Commons  — viewcontent.cgi / download button scrape
  24. OECD/JRC Direct             — iLibrary PDF URL construction
  25. Browser User-Agent Retry    — Chrome headers for 403-blocked PDFs
  26. OSF Preprints               — Open Science Framework preprint search
  27. MDPI Direct                 — append /pdf to mdpi.com article URL

Usage:
    python3 scripts/advanced_download.py                      # All 75 manual papers
    python3 scripts/advanced_download.py 1 15                 # Range (1-indexed)
    python3 scripts/advanced_download.py --dry-run 1 5        # Dry run
    python3 scripts/advanced_download.py --report             # Status report
    python3 scripts/advanced_download.py --playwright         # SSRN + Law Commons only

Run from BACKGROUND/ directory.
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
DOCS_DIR = BACKGROUND_DIR / "Documents"
CURL_TIMEOUT = 60
MAX_RETRIES = 2
UNPAYWALL_EMAIL = "research@cei-literature.org"

HEADERS = {
    "User-Agent": "CEI-Literature-Vault/2.0 (Academic Research; mailto:research@cei-literature.org)"
}

BROWSER_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com/",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
}

RATE_LIMITS = {
    "crossref": 0.05,
    "openalex": 0.1,
    "semantic_scholar": 10.0,
    "arxiv": 3.0,
    "pmc": 0.5,
    "wayback": 1.0,
    "ia_scholar": 1.0,
    "base": 1.0,
    "law_commons": 2.0,
    "oecd": 2.0,
    "osf": 1.0,
    "ssrn_playwright": 5.0,
    "browser_retry": 3.0,
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


def api_get_text(url: str, source: str, timeout: int = 15, extra_headers: Optional[dict] = None) -> Optional[str]:
    """Fetch URL as raw text (for XML, HTML)."""
    _rate_limit(source)
    try:
        headers = dict(HEADERS)
        if extra_headers:
            headers.update(extra_headers)
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="ignore")
    except Exception:
        return None


# ═══════════════════════════════════════════════════════════════════════════════
# PDF Download
# ═══════════════════════════════════════════════════════════════════════════════

def download_pdf(url: str, output_path: Path, retries: int = MAX_RETRIES,
                 extra_headers: Optional[dict] = None) -> tuple[bool, str]:
    """Download a PDF using curl with retry and %PDF- header validation."""
    curl_headers = ["-H", f"User-Agent: {HEADERS['User-Agent']}"]
    if extra_headers:
        for k, v in extra_headers.items():
            curl_headers += ["-H", f"{k}: {v}"]

    for attempt in range(retries + 1):
        try:
            result = subprocess.run(
                [
                    "curl", "-sS", "-L",
                    "-o", str(output_path),
                    "-w", "%{http_code}",
                    "--max-time", str(CURL_TIMEOUT),
                    "--connect-timeout", "15",
                ] + curl_headers + [url],
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
                    time.sleep(15 * (attempt + 1))
                    continue
                return False, "HTTP 429 rate limited"

            output_path.unlink(missing_ok=True)
            return False, f"HTTP {http_code}"

        except subprocess.TimeoutExpired:
            output_path.unlink(missing_ok=True)
            if attempt < retries:
                continue
            return False, "Timeout"
        except Exception as e:
            return False, str(e)

    return False, "Max retries exceeded"


# ═══════════════════════════════════════════════════════════════════════════════
# Title matching (copied from download_background_pdfs.py)
# ═══════════════════════════════════════════════════════════════════════════════

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


# ═══════════════════════════════════════════════════════════════════════════════
# Strategy 14: OpenAlex Full Locations
# ═══════════════════════════════════════════════════════════════════════════════

def try_openalex_full_locations(doi: str, output_path: Path) -> tuple[bool, str]:
    """Strategy 14: Iterate ALL OpenAlex locations[], not just best_oa_location."""
    if not doi:
        return False, "No DOI"
    encoded_doi = urllib.parse.quote(doi)
    url = f"https://api.openalex.org/works/https://doi.org/{encoded_doi}?select=locations,open_access&mailto={UNPAYWALL_EMAIL}"
    data = api_get(url, "openalex")
    if not data:
        return False, "OpenAlex: no response"

    locations = data.get("locations") or []
    for loc in locations:
        if not loc.get("is_oa"):
            continue
        pdf_url = loc.get("pdf_url")
        if pdf_url:
            ok, msg = download_pdf(pdf_url, output_path)
            if ok:
                return True, f"OpenAlex location: {pdf_url[:80]}"

    # Also check top-level open_access.oa_url
    oa = data.get("open_access") or {}
    oa_url = oa.get("oa_url")
    if oa_url:
        ok, msg = download_pdf(oa_url, output_path)
        if ok:
            return True, f"OpenAlex OA URL: {oa_url[:80]}"

    return False, f"OpenAlex: no OA PDF in {len(locations)} locations"


# ═══════════════════════════════════════════════════════════════════════════════
# Strategy 15: CrossRef Link Extraction
# ═══════════════════════════════════════════════════════════════════════════════

def try_crossref_links(doi: str, output_path: Path) -> tuple[bool, str]:
    """Strategy 15: Parse CrossRef link[] for PDF content-type entries."""
    if not doi:
        return False, "No DOI"
    encoded_doi = urllib.parse.quote(doi, safe="")
    url = f"https://api.crossref.org/works/{encoded_doi}"
    data = api_get(url, "crossref")
    if not data:
        return False, "CrossRef: no response"

    message = data.get("message") or {}
    links = message.get("link") or []
    for link in links:
        content_type = link.get("content-type", "")
        link_url = link.get("URL", "")
        if "pdf" in content_type.lower() and link_url:
            ok, msg = download_pdf(link_url, output_path)
            if ok:
                return True, f"CrossRef link ({content_type}): {link_url[:80]}"

    # Check alternative-id for arXiv IDs
    alt_ids = message.get("alternative-id") or []
    for alt_id in alt_ids:
        arxiv_match = re.search(r'(\d{4}\.\d{4,5})', str(alt_id))
        if arxiv_match:
            arxiv_id = arxiv_match.group(1)
            arxiv_url = f"https://arxiv.org/pdf/{arxiv_id}"
            ok, msg = download_pdf(arxiv_url, output_path)
            if ok:
                return True, f"CrossRef alt-id arXiv: {arxiv_id}"

    return False, f"CrossRef: no PDF links in {len(links)} link entries"


# ═══════════════════════════════════════════════════════════════════════════════
# Strategy 16: Semantic Scholar Title Search
# ═══════════════════════════════════════════════════════════════════════════════

def try_semantic_scholar_title(title: str, output_path: Path) -> tuple[bool, str]:
    """Strategy 16: S2 title search (Strategy 7 was DOI-only lookup)."""
    if not title:
        return False, "No title"
    encoded = urllib.parse.quote(title[:150])
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={encoded}&fields=openAccessPdf,externalIds,title&limit=3"
    data = api_get(url, "semantic_scholar", timeout=20)
    if not data:
        return False, "S2 title: no response"

    for paper in (data.get("data") or []):
        result_title = paper.get("title", "")
        if not _titles_match(title, result_title):
            continue

        # Try openAccessPdf first
        oa_pdf = paper.get("openAccessPdf") or {}
        pdf_url = oa_pdf.get("url")
        if pdf_url:
            ok, msg = download_pdf(pdf_url, output_path)
            if ok:
                return True, f"S2 title search OA PDF: {pdf_url[:80]}"

        # Try arXiv if externalIds has one
        ext_ids = paper.get("externalIds") or {}
        arxiv_id = ext_ids.get("ArXiv")
        if arxiv_id:
            arxiv_url = f"https://arxiv.org/pdf/{arxiv_id}"
            ok, msg = download_pdf(arxiv_url, output_path)
            if ok:
                return True, f"S2 title → arXiv {arxiv_id}"

    return False, "S2 title: no matching paper with OA PDF"


# ═══════════════════════════════════════════════════════════════════════════════
# Strategy 17: arXiv Title Search
# ═══════════════════════════════════════════════════════════════════════════════

def try_arxiv_title(title: str, output_path: Path) -> tuple[bool, str]:
    """Strategy 17: Query arXiv Atom API by title."""
    if not title:
        return False, "No title"
    encoded = urllib.parse.quote(f'ti:"{title[:100]}"')
    url = f"http://export.arxiv.org/api/query?search_query={encoded}&max_results=3&sortBy=relevance"
    text = api_get_text(url, "arxiv", timeout=20)
    if not text:
        return False, "arXiv title: no response"

    # Parse Atom XML entries
    entries = re.findall(r'<entry>(.*?)</entry>', text, re.DOTALL)
    for entry in entries:
        # Extract title from entry
        m_title = re.search(r'<title>(.*?)</title>', entry, re.DOTALL)
        result_title = m_title.group(1).strip() if m_title else ""
        result_title = re.sub(r'\s+', ' ', result_title)

        if not _titles_match(title, result_title):
            continue

        # Extract arXiv ID from id field
        m_id = re.search(r'<id>.*?/abs/(\d{4}\.\d{4,5})</id>', entry)
        if m_id:
            arxiv_id = m_id.group(1)
            pdf_url = f"https://arxiv.org/pdf/{arxiv_id}"
            ok, msg = download_pdf(pdf_url, output_path)
            if ok:
                return True, f"arXiv title → {arxiv_id}"

    return False, "arXiv title: no matching paper found"


# ═══════════════════════════════════════════════════════════════════════════════
# Strategy 18: PubMed Central ID Converter
# ═══════════════════════════════════════════════════════════════════════════════

def try_pubmed_central(doi: str, output_path: Path) -> tuple[bool, str]:
    """Strategy 18: Convert DOI → PMCID → PMC PDF URL."""
    if not doi:
        return False, "No DOI"
    encoded_doi = urllib.parse.quote(doi, safe="")
    url = f"https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids={encoded_doi}&format=json"
    data = api_get(url, "pmc")
    if not data:
        return False, "PMC: no response"

    records = data.get("records") or []
    for record in records:
        pmcid = record.get("pmcid")
        if pmcid:
            pdf_url = f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/pdf/"
            ok, msg = download_pdf(pdf_url, output_path)
            if ok:
                return True, f"PMC {pmcid}: {pdf_url[:80]}"
            # Also try EuropePMC render endpoint
            europepmc_url = f"https://europepmc.org/articles/{pmcid}/pdf/render"
            ok2, msg2 = download_pdf(europepmc_url, output_path)
            if ok2:
                return True, f"EuropePMC render {pmcid}"

    return False, "PMC: DOI not in PubMed Central"


# ═══════════════════════════════════════════════════════════════════════════════
# Strategy 20: Wayback Machine CDX API
# ═══════════════════════════════════════════════════════════════════════════════

def try_wayback_machine(url: str, doi: str, output_path: Path) -> tuple[bool, str]:
    """Strategy 20: Find archived PDF snapshot via Wayback CDX API."""
    urls_to_check = []
    if url:
        urls_to_check.append(url)
    if doi:
        urls_to_check.append(f"https://doi.org/{doi}")

    for target_url in urls_to_check:
        encoded = urllib.parse.quote(target_url, safe="")
        cdx_url = f"https://web.archive.org/cdx/search/cdx?url={encoded}&output=json&limit=5&filter=mimetype:application/pdf&fl=timestamp,original"
        _rate_limit("wayback")
        try:
            req = urllib.request.Request(cdx_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as resp:
                rows = json.loads(resp.read().decode("utf-8"))
        except Exception:
            continue

        if not rows or len(rows) < 2:  # rows[0] is header
            continue

        for row in rows[1:]:
            if len(row) >= 2:
                timestamp, original = row[0], row[1]
                wayback_pdf_url = f"https://web.archive.org/web/{timestamp}id_/{original}"
                ok, msg = download_pdf(wayback_pdf_url, output_path)
                if ok:
                    return True, f"Wayback Machine: {wayback_pdf_url[:80]}"

    return False, "Wayback: no archived PDF snapshot found"


# ═══════════════════════════════════════════════════════════════════════════════
# Strategy 21: Internet Archive Scholar
# ═══════════════════════════════════════════════════════════════════════════════

def try_ia_scholar(title: str, output_path: Path) -> tuple[bool, str]:
    """Strategy 21: scholar.archive.org title search."""
    if not title:
        return False, "No title"
    encoded = urllib.parse.quote(title[:120])
    url = f"https://scholar.archive.org/search?q={encoded}&limit=3"
    _rate_limit("ia_scholar")
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception:
        return False, "IA Scholar: no response"

    hits = (data.get("hits") or {}).get("hits") or []
    for hit in hits:
        result_title = (hit.get("_source") or {}).get("title", "")
        if not _titles_match(title, result_title):
            continue
        access = (hit.get("_source") or {}).get("access_type", "")
        access_url = (hit.get("_source") or {}).get("access_url", "")
        if access_url and access in ("ia_file", "wayback"):
            ok, msg = download_pdf(access_url, output_path)
            if ok:
                return True, f"IA Scholar: {access_url[:80]}"

    return False, "IA Scholar: no matching accessible paper"


# ═══════════════════════════════════════════════════════════════════════════════
# Strategy 22: BASE (Bielefeld Academic Search Engine)
# ═══════════════════════════════════════════════════════════════════════════════

def try_base_search(title: str, output_path: Path) -> tuple[bool, str]:
    """Strategy 22: BASE — 300M+ docs from 10K+ institutional repositories."""
    if not title:
        return False, "No title"
    encoded = urllib.parse.quote(f'tit:"{title[:100]}"')
    url = f"https://api.base-search.net/cgi-bin/BaseHttpSearchInterface.fcgi?func=PerformSearch&query={encoded}&format=json&hits=3"
    _rate_limit("base")
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception:
        return False, "BASE: no response"

    docs = (data.get("response") or {}).get("docs") or []
    for doc in docs:
        result_title = doc.get("dctitle", "")
        if not _titles_match(title, result_title):
            continue
        doc_urls = doc.get("dcdocumenturl") or []
        if isinstance(doc_urls, str):
            doc_urls = [doc_urls]
        for doc_url in doc_urls:
            if doc_url and (doc_url.lower().endswith(".pdf") or "pdf" in doc_url.lower()):
                ok, msg = download_pdf(doc_url, output_path)
                if ok:
                    return True, f"BASE: {doc_url[:80]}"
            elif doc_url:
                # Scrape the page for a PDF link
                try:
                    req2 = urllib.request.Request(doc_url, headers=HEADERS)
                    with urllib.request.urlopen(req2, timeout=10) as resp2:
                        html = resp2.read().decode("utf-8", errors="ignore")
                    m = re.search(r'href="([^"]+\.pdf[^"]*)"', html, re.IGNORECASE)
                    if m:
                        pdf_url = m.group(1)
                        if not pdf_url.startswith("http"):
                            from urllib.parse import urljoin
                            pdf_url = urljoin(doc_url, pdf_url)
                        ok2, msg2 = download_pdf(pdf_url, output_path)
                        if ok2:
                            return True, f"BASE page → {pdf_url[:80]}"
                except Exception:
                    pass

    return False, "BASE: no matching paper with PDF link"


# ═══════════════════════════════════════════════════════════════════════════════
# Strategy 23: Law Review Digital Commons
# ═══════════════════════════════════════════════════════════════════════════════

def try_law_commons(url: str, output_path: Path) -> tuple[bool, str]:
    """Strategy 23: scholarship.law.* / digitalcommons.* — scrape viewcontent.cgi."""
    if not url:
        return False, "No URL"
    is_law_commons = any(x in url for x in [
        "scholarship.law.", "digitalcommons.", "lawreview", "repository.law"
    ])
    if not is_law_commons:
        return False, "Not a law commons URL"

    _rate_limit("law_commons")
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20) as resp:
            final_url = resp.geturl()
            content_type = resp.headers.get("Content-Type", "")
            if "application/pdf" in content_type:
                return download_pdf(final_url, output_path)
            html = resp.read().decode("utf-8", errors="ignore")
    except Exception as e:
        return False, f"Law commons fetch error: {e}"

    from urllib.parse import urljoin
    # Pattern 1: viewcontent.cgi download link
    m = re.search(r'href="([^"]*viewcontent\.cgi[^"]*)"', html, re.IGNORECASE)
    if m:
        pdf_url = m.group(1)
        if not pdf_url.startswith("http"):
            pdf_url = urljoin(final_url, pdf_url)
        ok, msg = download_pdf(pdf_url, output_path)
        if ok:
            return True, f"Law commons viewcontent: {pdf_url[:80]}"

    # Pattern 2: direct /download suffix
    download_url = url.rstrip("/") + "/download"
    ok, msg = download_pdf(download_url, output_path)
    if ok:
        return True, f"Law commons /download: {download_url[:80]}"

    # Pattern 3: any .pdf link on page
    m2 = re.search(r'href="([^"]+\.pdf[^"]*)"', html, re.IGNORECASE)
    if m2:
        pdf_url = m2.group(1)
        if not pdf_url.startswith("http"):
            pdf_url = urljoin(final_url, pdf_url)
        ok2, msg2 = download_pdf(pdf_url, output_path)
        if ok2:
            return True, f"Law commons PDF link: {pdf_url[:80]}"

    return False, "Law commons: no download link found"


# ═══════════════════════════════════════════════════════════════════════════════
# Strategy 24: OECD/JRC Direct
# ═══════════════════════════════════════════════════════════════════════════════

def try_oecd_jrc(doi: str, output_path: Path) -> tuple[bool, str]:
    """Strategy 24: Construct iLibrary PDF URL for OECD/JRC DOIs."""
    if not doi:
        return False, "No DOI"

    # OECD DOI pattern: 10.1787/IDENTIFIER
    if doi.startswith("10.1787/"):
        identifier = doi[len("10.1787/"):]
        # Try /deliver/ first (correct OECD iLibrary pattern)
        for pdf_url in [
            f"https://www.oecd-ilibrary.org/deliver/{identifier}.pdf",
            f"https://www.oecd-ilibrary.org/{identifier}/full.pdf",
            f"https://www.oecd-ilibrary.org/docserver/{identifier}.pdf",
        ]:
            _rate_limit("oecd")
            ok, msg = download_pdf(pdf_url, output_path)
            if ok:
                return True, f"OECD: {pdf_url[:80]}"
        return False, "OECD: all 3 URL patterns failed"

    # JRC DOI pattern: 10.2760/IDENTIFIER
    if doi.startswith("10.2760/"):
        encoded = urllib.parse.quote(doi, safe="")
        jrc_search = f"https://publications.jrc.ec.europa.eu/repository/rest/handle/JRC?doi={encoded}&format=json"
        _rate_limit("oecd")
        data = api_get(jrc_search, "oecd")
        if data:
            pdf_url = (data.get("bitstreams") or [{}])[0].get("retrieveLink")
            if pdf_url:
                ok, msg = download_pdf(pdf_url, output_path)
                if ok:
                    return True, f"JRC publications: {pdf_url[:80]}"
        # Fallback: follow doi.org redirect and scrape JRC page for PDF link
        _rate_limit("oecd")
        try:
            from urllib.parse import urljoin
            doi_url = f"https://doi.org/{doi}"
            req = urllib.request.Request(doi_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as resp:
                final_url = resp.geturl()
                html = resp.read().decode("utf-8", errors="ignore")
            m = re.search(r'href="([^"]+\.pdf[^"]*)"', html, re.IGNORECASE)
            if m:
                link = m.group(1)
                pdf_url = link if link.startswith("http") else urljoin(final_url, link)
                ok, msg = download_pdf(pdf_url, output_path)
                if ok:
                    return True, f"JRC doi scrape: {pdf_url[:80]}"
        except Exception:
            pass
        return False, "JRC: API + scrape both failed"

    return False, "Not an OECD/JRC DOI"


# ═══════════════════════════════════════════════════════════════════════════════
# Strategy 25: Browser User-Agent Retry
# ═══════════════════════════════════════════════════════════════════════════════

def try_browser_ua_retry(url: str, doi: str, output_path: Path) -> tuple[bool, str]:
    """Strategy 25: Retry blocked URLs with full Chrome-like headers."""
    urls_to_try = []
    if url and (url.lower().endswith(".pdf") or "pdf" in url.lower()):
        urls_to_try.append(url)
    if doi:
        # IOSCO pattern: use doi.org redirect
        if "iosco" in url.lower() if url else False:
            urls_to_try.append(f"https://doi.org/{doi}")

    if not urls_to_try:
        return False, "No applicable URL for browser retry"

    _rate_limit("browser_retry")
    for retry_url in urls_to_try:
        extra = {k: v for k, v in BROWSER_HEADERS.items() if k != "User-Agent"}
        ok, msg = download_pdf(retry_url, output_path, extra_headers=extra)
        if ok:
            return True, f"Browser UA retry: {retry_url[:80]}"

    return False, "Browser UA retry: still blocked"


# ═══════════════════════════════════════════════════════════════════════════════
# Strategy 26: OSF Preprints
# ═══════════════════════════════════════════════════════════════════════════════

def try_osf_preprints(title: str, output_path: Path) -> tuple[bool, str]:
    """Strategy 26: Open Science Framework preprint search."""
    if not title:
        return False, "No title"
    encoded = urllib.parse.quote(title[:100])
    url = f"https://api.osf.io/v2/preprints/?filter[title]={encoded}&page[size]=3"
    data = api_get(url, "osf")
    if not data:
        return False, "OSF: no response"

    for item in (data.get("data") or []):
        attrs = item.get("attributes") or {}
        result_title = attrs.get("title", "")
        if not _titles_match(title, result_title):
            continue
        links = item.get("links") or {}
        download_url = links.get("preprint_doi") or links.get("self")
        if download_url:
            # OSF download link pattern
            osf_id = item.get("id", "")
            pdf_url = f"https://osf.io/{osf_id}/download"
            ok, msg = download_pdf(pdf_url, output_path)
            if ok:
                return True, f"OSF preprint {osf_id}: {pdf_url[:80]}"

    return False, "OSF: no matching preprint found"


# ═══════════════════════════════════════════════════════════════════════════════
# Strategy 27: MDPI Direct PDF URL
# ═══════════════════════════════════════════════════════════════════════════════

def try_mdpi_direct(url: str, output_path: Path) -> tuple[bool, str]:
    """MDPI papers: append /pdf to the article URL directly."""
    if not url or "mdpi.com" not in url:
        return False, "Not an MDPI URL"
    pdf_url = url.rstrip("/") + "/pdf"
    ok, msg = download_pdf(pdf_url, output_path)
    if ok:
        return True, f"MDPI direct: {pdf_url[:80]}"
    return False, f"MDPI direct: {msg}"


# ═══════════════════════════════════════════════════════════════════════════════
# Strategy 19: SSRN Playwright (requires --playwright flag)
# ═══════════════════════════════════════════════════════════════════════════════

def try_ssrn_playwright(paper: dict, output_path: Path) -> tuple[bool, str]:
    """Strategy 19: Headless Chromium for Cloudflare-protected SSRN papers."""
    url = paper.get("url", "")
    if not url or "ssrn" not in url.lower():
        return False, "Not an SSRN URL"

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False, "Playwright not installed"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=BROWSER_HEADERS["User-Agent"],
            viewport={"width": 1280, "height": 800},
        )
        page = context.new_page()
        pdf_bytes = []

        def capture_pdf(response):
            ct = response.headers.get("content-type", "")
            if "application/pdf" in ct and response.status == 200:
                try:
                    pdf_bytes.append(response.body())
                except Exception:
                    pass

        page.on("response", capture_pdf)
        try:
            page.goto(url, wait_until="networkidle", timeout=30000)
        except Exception:
            time.sleep(3)

        page.remove_listener("response", capture_pdf)

        if pdf_bytes:
            data = pdf_bytes[0]
            if data[:5] == b"%PDF-" and len(data) > 1000:
                output_path.write_bytes(data)
                page.close()
                browser.close()
                return True, f"SSRN PDF captured ({len(data)} bytes)"

        # Look for delivery link
        try:
            btn = page.query_selector('a[href*="Delivery.cfm"], a[href*="delivery.cfm"]')
            if btn:
                pdf_url = btn.get_attribute("href")
                if pdf_url and not pdf_url.startswith("http"):
                    pdf_url = "https://papers.ssrn.com" + pdf_url
                if pdf_url:
                    req = urllib.request.Request(pdf_url, headers={"User-Agent": BROWSER_HEADERS["User-Agent"]})
                    with urllib.request.urlopen(req, timeout=30) as resp:
                        data = resp.read()
                    if data[:5] == b"%PDF-":
                        output_path.write_bytes(data)
                        page.close()
                        browser.close()
                        return True, f"SSRN delivery URL: {pdf_url[:80]}"
        except Exception as e:
            print(f"    SSRN delivery attempt: {e}")

        # Fallback: extract abstract_id from page HTML
        try:
            html = page.content()
            m = re.search(r'abstract[_-]?id[=\s]+(\d+)', html, re.IGNORECASE)
            if m:
                abstract_id = m.group(1)
                delivery_url = f"https://papers.ssrn.com/sol3/Delivery.cfm?abstractid={abstract_id}"
                req = urllib.request.Request(delivery_url, headers={"User-Agent": BROWSER_HEADERS["User-Agent"]})
                with urllib.request.urlopen(req, timeout=30) as resp:
                    data = resp.read()
                if data[:5] == b"%PDF-":
                    output_path.write_bytes(data)
                    page.close()
                    browser.close()
                    return True, f"SSRN abstract_id delivery ({len(data)} bytes)"
        except Exception as e:
            print(f"    SSRN fallback: {e}")

        page.close()
        browser.close()

    return False, "SSRN Playwright: no PDF found"


# ═══════════════════════════════════════════════════════════════════════════════
# Law Commons Playwright (part of --playwright mode)
# ═══════════════════════════════════════════════════════════════════════════════

def try_law_commons_playwright(paper: dict, output_path: Path) -> tuple[bool, str]:
    """Playwright scrape for law review digital commons."""
    url = paper.get("url", "")
    if not url:
        return False, "No URL"
    is_law = any(x in url for x in ["scholarship.law.", "digitalcommons.", "repository.law"])
    if not is_law:
        return False, "Not a law commons URL"

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False, "Playwright not installed"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=BROWSER_HEADERS["User-Agent"],
            viewport={"width": 1280, "height": 800},
        )
        page = context.new_page()
        pdf_bytes = []

        def capture(response):
            ct = response.headers.get("content-type", "")
            if ("application/pdf" in ct or "octet-stream" in ct) and response.status == 200:
                try:
                    data = response.body()
                    if data[:5] == b"%PDF-":
                        pdf_bytes.append(data)
                except Exception:
                    pass

        page.on("response", capture)
        try:
            page.goto(url, wait_until="networkidle", timeout=30000)
        except Exception:
            time.sleep(2)

        page.remove_listener("response", capture)

        if pdf_bytes:
            output_path.write_bytes(pdf_bytes[0])
            page.close()
            browser.close()
            return True, f"Law commons PDF captured ({len(pdf_bytes[0])} bytes)"

        # Try clicking download link
        try:
            pdf_links = page.evaluate("""
                () => Array.from(document.querySelectorAll('a[href]'))
                    .map(a => ({href: a.href, text: a.textContent.trim()}))
                    .filter(a => a.href.toLowerCase().includes('.pdf') ||
                                 a.href.toLowerCase().includes('viewcontent') ||
                                 a.href.toLowerCase().includes('download') ||
                                 /download|pdf/i.test(a.text))
            """)
            for link in (pdf_links or []):
                href = link.get("href", "")
                if href:
                    page.close()
                    browser.close()
                    ok, msg = download_pdf(href, output_path)
                    if ok:
                        return True, f"Law commons PW link: {href[:80]}"
                    return False, f"Law commons PW: found link but download failed: {msg}"
        except Exception as e:
            print(f"    Law commons page eval: {e}")

        page.close()
        browser.close()

    return False, "Law commons Playwright: no PDF found"


# ═══════════════════════════════════════════════════════════════════════════════
# Paper loading
# ═══════════════════════════════════════════════════════════════════════════════

def _get_subdirs() -> list[Path]:
    return sorted(
        d for d in BACKGROUND_DIR.iterdir()
        if d.is_dir() and re.match(r'^\d{2}-', d.name)
    )


def _extract_ssrn_id(doi: str, url: str) -> str:
    """Extract SSRN abstract ID from DOI (10.2139/ssrn.XXXXXXX) or URL."""
    if doi and doi.startswith("10.2139/ssrn."):
        return doi[len("10.2139/ssrn."):]
    if url:
        m = re.search(r'abstract[_-]?id[=_](\d+)', url, re.IGNORECASE)
        if m:
            return m.group(1)
    return ""


def load_manual_papers() -> tuple[list[dict], dict]:
    """Load papers with download_status: manual-download-required.

    Returns (papers_list, doi_to_paths) where doi_to_paths handles duplicate DOIs.
    """
    papers = []
    doi_to_paths: dict[str, list[Path]] = {}

    for subdir in _get_subdirs():
        for f in sorted(subdir.iterdir()):
            if f.suffix != ".md" or f.name.startswith("expert"):
                continue

            content = f.read_text(encoding="utf-8")
            if 'download_status: "manual-download-required"' not in content:
                continue

            def field(name: str, _content: str = content) -> str:
                m = re.search(rf'^{name}:\s*"?([^\"\n]+?)"?\s*$', _content, re.MULTILINE)
                return m.group(1).strip() if m else ""

            doi = field("doi")
            url = field("url")
            title = field("title")
            ssrn_id = _extract_ssrn_id(doi, url)

            paper = {
                "path": f,
                "stem": f.stem,
                "doi": doi,
                "url": url,
                "full_title": title,
                "ssrn_id": ssrn_id,
                "year": field("year"),
            }
            papers.append(paper)

            if doi:
                if doi not in doi_to_paths:
                    doi_to_paths[doi] = []
                doi_to_paths[doi].append(f)

    return papers, doi_to_paths


# ═══════════════════════════════════════════════════════════════════════════════
# YAML field helpers
# ═══════════════════════════════════════════════════════════════════════════════

def update_paper_field(paper_path: Path, field_name: str, value: str):
    """Update a YAML field using safe regex replacement."""
    content = paper_path.read_text(encoding="utf-8")
    line = f"{field_name}: {value}" if value in ("true", "false") else f'{field_name}: "{value}"'

    if re.search(rf'^{re.escape(field_name)}:', content, re.MULTILINE):
        new_content = re.sub(
            rf'^{re.escape(field_name)}:.*$',
            line, content, count=1, flags=re.MULTILINE,
        )
    else:
        m = re.search(r'^---\s*$', content[3:], re.MULTILINE)
        if m:
            insert_pos = 3 + m.start()
            new_content = content[:insert_pos] + line + "\n" + content[insert_pos:]
        else:
            new_content = content.rstrip() + f"\n{line}\n"

    paper_path.write_text(new_content, encoding="utf-8")


def remove_paper_field(paper_path: Path, field_name: str):
    """Remove a YAML field line entirely."""
    content = paper_path.read_text(encoding="utf-8")
    new_content = re.sub(
        rf'^{re.escape(field_name)}:.*\n?',
        "",
        content,
        count=1,
        flags=re.MULTILINE,
    )
    if new_content != content:
        paper_path.write_text(new_content, encoding="utf-8")


def on_success(paper: dict, pdf_filename: str, doi_to_paths: dict):
    """Update all files sharing this DOI on success."""
    doi = paper.get("doi", "")
    paths = doi_to_paths.get(doi, [paper["path"]]) if doi else [paper["path"]]
    for path in paths:
        update_paper_field(path, "local_document", f"Documents/{pdf_filename}")
        update_paper_field(path, "document_acquired", "true")
        remove_paper_field(path, "download_status")


# ═══════════════════════════════════════════════════════════════════════════════
# Main download runner
# ═══════════════════════════════════════════════════════════════════════════════

def run_downloads(start: int = 1, end: Optional[int] = None, dry_run: bool = False):
    DOCS_DIR.mkdir(exist_ok=True)
    papers, doi_to_paths = load_manual_papers()
    total = len(papers)
    print(f"Found {total} manual-download-required papers")

    if end is None:
        end = total
    batch = papers[start - 1:end]
    print(f"Processing papers {start}-{min(end, total)} ({len(batch)} papers)\n")

    success = 0
    failed = 0

    for i, paper in enumerate(batch, start):
        print(f"[{i}/{min(end, total)}] {paper['stem']}")

        if dry_run:
            doi_short = paper["doi"][:40] if paper["doi"] else "none"
            url_short = paper["url"][:50] if paper["url"] else "none"
            ssrn = f" SSRN:{paper['ssrn_id']}" if paper["ssrn_id"] else ""
            print(f"  DRY RUN — DOI:{doi_short} | URL:{url_short}{ssrn}")
            continue

        pdf_filename = paper["stem"] + ".pdf"
        output_path = DOCS_DIR / pdf_filename

        # Already on disk and valid
        if output_path.exists() and output_path.stat().st_size > 1000:
            with open(output_path, "rb") as fh:
                if fh.read(5) == b"%PDF-":
                    print(f"  OK Already on disk: {pdf_filename}")
                    on_success(paper, pdf_filename, doi_to_paths)
                    success += 1
                    continue

        doi = paper["doi"]
        url = paper["url"]
        title = paper["full_title"]

        strategies = [
            ("MDPI Direct",               lambda p=paper, o=output_path: try_mdpi_direct(p["url"], o)),
            ("OpenAlex Full Locations",   lambda p=paper, o=output_path: try_openalex_full_locations(p["doi"], o)),
            ("CrossRef Links",            lambda p=paper, o=output_path: try_crossref_links(p["doi"], o)),
            ("S2 Title Search",           lambda p=paper, o=output_path: try_semantic_scholar_title(p["full_title"], o)),
            ("arXiv Title",               lambda p=paper, o=output_path: try_arxiv_title(p["full_title"], o)),
            ("PubMed Central",            lambda p=paper, o=output_path: try_pubmed_central(p["doi"], o)),
            ("Wayback Machine",           lambda p=paper, o=output_path: try_wayback_machine(p["url"], p["doi"], o)),
            ("IA Scholar",                lambda p=paper, o=output_path: try_ia_scholar(p["full_title"], o)),
            ("BASE",                      lambda p=paper, o=output_path: try_base_search(p["full_title"], o)),
            ("Law Commons",               lambda p=paper, o=output_path: try_law_commons(p["url"], o)),
            ("OECD/JRC",                  lambda p=paper, o=output_path: try_oecd_jrc(p["doi"], o)),
            ("Browser UA Retry",          lambda p=paper, o=output_path: try_browser_ua_retry(p["url"], p["doi"], o)),
            ("OSF Preprints",             lambda p=paper, o=output_path: try_osf_preprints(p["full_title"], o)),
        ]

        downloaded = False
        for strategy_name, strategy_fn in strategies:
            ok, msg = strategy_fn()
            if ok:
                print(f"  OK [{strategy_name}] {pdf_filename}")
                on_success(paper, pdf_filename, doi_to_paths)
                downloaded = True
                success += 1
                break
            else:
                print(f"  X  [{strategy_name}] {msg}")

        if not downloaded:
            print(f"  -> Still manual-download-required")
            failed += 1

    print(f"\n{'='*50}")
    print(f"Downloaded: {success}  |  Still manual: {failed}")


def run_playwright_mode():
    """Strategy 19 + 23: Process SSRN and Law Commons papers with headless Chromium."""
    DOCS_DIR.mkdir(exist_ok=True)
    papers, doi_to_paths = load_manual_papers()

    playwright_papers = []
    for paper in papers:
        url = paper.get("url", "")
        if paper.get("ssrn_id") or "ssrn" in url.lower():
            playwright_papers.append((paper, "ssrn"))
        elif any(x in url for x in ["scholarship.law.", "digitalcommons.", "repository.law"]):
            playwright_papers.append((paper, "law_commons"))

    print(f"Playwright mode: {len(playwright_papers)} papers (SSRN + Law Commons)\n")

    success = 0
    for paper, strategy in playwright_papers:
        pdf_filename = paper["stem"] + ".pdf"
        output_path = DOCS_DIR / pdf_filename

        if output_path.exists() and output_path.stat().st_size > 1000:
            with open(output_path, "rb") as fh:
                if fh.read(5) == b"%PDF-":
                    print(f"OK Already on disk: {pdf_filename}")
                    on_success(paper, pdf_filename, doi_to_paths)
                    success += 1
                    continue

        print(f"[PW/{strategy}] {paper['stem']}")
        print(f"  URL: {paper.get('url', 'none')[:80]}")

        _rate_limit("ssrn_playwright")
        if strategy == "ssrn":
            ok, msg = try_ssrn_playwright(paper, output_path)
        else:
            ok, msg = try_law_commons_playwright(paper, output_path)

        if ok:
            print(f"  OK {msg}")
            on_success(paper, pdf_filename, doi_to_paths)
            success += 1
        else:
            print(f"  X  {msg}")

    print(f"\n{'='*50}")
    print(f"Playwright: {success}/{len(playwright_papers)} succeeded")


def show_report():
    subdirs = _get_subdirs()
    all_papers = []
    for subdir in subdirs:
        for f in sorted(subdir.iterdir()):
            if f.suffix == ".md" and not f.name.startswith("expert"):
                all_papers.append(f)

    total = len(all_papers)
    acquired = manual = 0
    for f in all_papers:
        content = f.read_text(encoding="utf-8")
        if "document_acquired: true" in content:
            acquired += 1
        elif 'download_status: "manual-download-required"' in content:
            manual += 1

    pending = total - acquired - manual
    print(f"Papers: {total}")
    print(f"  Acquired:      {acquired} ({100*acquired//total if total else 0}%)")
    print(f"  Manual needed: {manual}")
    print(f"  Pending:       {pending}")

    docs = list(DOCS_DIR.glob("*.pdf")) if DOCS_DIR.exists() else []
    print(f"\nDocuments in Documents/: {len(docs)}")


if __name__ == "__main__":
    args = sys.argv[1:]

    if "--report" in args:
        show_report()
    elif "--playwright" in args:
        run_playwright_mode()
    elif "--dry-run" in args:
        remaining = [a for a in args if a != "--dry-run"]
        start = int(remaining[0]) if remaining and remaining[0].isdigit() else 1
        end = int(remaining[1]) if len(remaining) > 1 and remaining[1].isdigit() else None
        run_downloads(start, end, dry_run=True)
    else:
        start = int(args[0]) if args and args[0].isdigit() else 1
        end = int(args[1]) if len(args) > 1 and args[1].isdigit() else None
        run_downloads(start, end, dry_run=False)
