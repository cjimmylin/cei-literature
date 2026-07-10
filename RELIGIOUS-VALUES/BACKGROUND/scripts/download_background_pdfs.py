#!/usr/bin/env python3
"""
download_background_pdfs.py — Waterfall PDF downloader for Religious Values BACKGROUND papers.

Adapted from ISIC-APPROACH/BACKGROUND/scripts/download_background_pdfs.py.

Download strategy (cascading waterfall — 13 steps):
  1.  arXiv direct (if arxiv_id present)
  2.  Preprint direct (medRxiv/bioRxiv/TechRxiv from DOI pattern)
  3.  Zenodo Records API (10.5281/zenodo.* DOIs)
  4.  Unpaywall API (via DOI)
  5.  EuropePMC REST API (medical/Springer OA PDFs via DOI)
  6.  OA Button API (author-deposited copies missed by Unpaywall)
  7.  Semantic Scholar PDF link
  8.  OpenAlex OA URL
  9.  Direct url field if ends in .pdf
  10. Handle.net (follow hdl.handle.net redirect to DSpace/ePrints, scrape bitstream)
  11. URL scrape (fetch paper URL as HTML, hunt for PDF link — grey literature)
  12. DOI scrape (follow doi.org redirect, parse publisher HTML)
  13. CORE.ac.uk title-based institutional repo search
  14. Mark as manual-download-required if all fail

Usage:
    python3 scripts/download_background_pdfs.py                     # All papers
    python3 scripts/download_background_pdfs.py 1 10               # Range (1-indexed)
    python3 scripts/download_background_pdfs.py --dry-run           # Show what would download
    python3 scripts/download_background_pdfs.py --dry-run 1 5       # Dry run on range
    python3 scripts/download_background_pdfs.py --report            # Show download status

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

RATE_LIMITS = {
    "unpaywall": 1.0,
    "semantic_scholar": 10.0,
    "arxiv": 3.0,
    "openalex": 0.1,
    "direct": 2.0,
    "preprint": 2.0,
    "zenodo": 1.0,
    "oa_button": 1.0,
    "doi_scrape": 3.0,
    "core": 1.0,
    "europepmc": 0.5,
    "handle_net": 1.0,
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
                    time.sleep(15 * (attempt + 1))
                    continue
                return False, "HTTP 429 rate limited"

            # Non-200 response — clean up the HTML error page curl wrote
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
# Download Strategies
# ═══════════════════════════════════════════════════════════════════════════════

def try_arxiv(arxiv_id: str, output_path: Path) -> tuple[bool, str]:
    """Strategy 1: Download from arXiv directly."""
    if not arxiv_id:
        return False, "No arXiv ID"
    if not re.match(r'^\d{4}\.\d{4,5}(v\d+)?$', arxiv_id):
        return False, f"Invalid arXiv ID: {arxiv_id}"
    url = f"https://arxiv.org/pdf/{arxiv_id}"
    _rate_limit("arxiv")
    return download_pdf(url, output_path)


def try_preprint_direct(doi: str, output_path: Path) -> tuple[bool, str]:
    """Strategy 2: Direct PDF URL for medRxiv/bioRxiv/TechRxiv preprints."""
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
            m2 = re.search(r'"downloadUrl"\s*:\s*"([^"]+)"', html)
            if m2:
                return download_pdf(m2.group(1), output_path)
        except Exception as e:
            return False, f"TechRxiv scrape failed: {e}"
    return False, "Preprint: DOI not a recognized preprint pattern"


def try_zenodo(doi: str, output_path: Path) -> tuple[bool, str]:
    """Strategy 3: Zenodo Records API for 10.5281/zenodo.* DOIs."""
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
    return False, "Zenodo: no PDF file found in record"


def try_unpaywall(doi: str, output_path: Path) -> tuple[bool, str]:
    """Strategy 4: Try Unpaywall API for open access PDF."""
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
    """Strategy 5: EuropePMC REST API — finds OA PDFs for medical/Springer journals."""
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
        return False, "EuropePMC: no OA PDF or PMC link found"
    return download_pdf(pdf_url, output_path)


def try_oa_button(doi: str, output_path: Path) -> tuple[bool, str]:
    """Strategy 6: OA Button API — finds author-deposited copies missed by Unpaywall."""
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
    """Strategy 7: Semantic Scholar PDF link."""
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
    """Strategy 8: OpenAlex OA URL."""
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
    """Strategy 9: Try direct URL if it looks like a PDF."""
    if not url:
        return False, "No URL"
    if url.lower().endswith(".pdf") or "pdf" in url.lower():
        return download_pdf(url, output_path)
    variants = [url + ".pdf", url.rstrip("/") + "/pdf"]
    for v in variants:
        ok, msg = download_pdf(v, output_path)
        if ok:
            return ok, msg
    return False, "Direct URL: not a PDF endpoint"


def try_handle_net(url: str, output_path: Path) -> tuple[bool, str]:
    """Strategy 10: Follow hdl.handle.net redirect to DSpace/ePrints page, scrape for PDF."""
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
        r"href='([^']*bitstream[^']*\.pdf[^']*)'",
        r'href="([^"]*bitstream[^"]*)"[^>]*>\s*(?:View|Download|PDF)',
        r'href="([^"]+\.pdf)"',
    ]:
        m = re.search(pattern, html, re.IGNORECASE)
        if m:
            link = m.group(1)
            pdf_url = link if link.startswith("http") else urljoin(final_url, link)
            ok, msg = download_pdf(pdf_url, output_path)
            if ok:
                return True, f"Handle.net DSpace -> {pdf_url[:80]}"
    return False, "Handle.net: no PDF bitstream link found on repository page"


def try_url_scrape(url: str, output_path: Path) -> tuple[bool, str]:
    """Strategy 11: Fetch the paper's URL as HTML and hunt for a PDF link on the page."""
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

    # Generic PDF link patterns
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

    # Domain-specific patterns
    if not pdf_url:
        if "rand.org" in final_url:
            m = re.search(r'href="(/pubs/[^"]+\.pdf)"', html)
            if m:
                pdf_url = "https://www.rand.org" + m.group(1)

        elif "weforum.org" in final_url:
            m = re.search(r'href="(https://www3?\.weforum\.org/docs/[^"]+\.pdf)"', html)
            if m:
                pdf_url = m.group(1)

        elif "oecd.org" in final_url or "oecd-ilibrary.org" in final_url:
            m = re.search(r'href="([^"]+/pdf[^"]*)"', html)
            if not m:
                m = re.search(r'"pdfUrl"\s*:\s*"([^"]+)"', html)
            if m:
                link = m.group(1)
                pdf_url = link if link.startswith("http") else base + link

        elif "stanford.edu" in final_url or "hai.stanford.edu" in final_url:
            m = re.search(r'href="([^"]+\.pdf)"', html)
            if m:
                link = m.group(1)
                pdf_url = link if link.startswith("http") else urljoin(final_url, link)

        elif "brookings.edu" in final_url:
            m = re.search(r'href="([^"]+\.pdf)"', html)
            if m:
                link = m.group(1)
                pdf_url = link if link.startswith("http") else urljoin(final_url, link)

        elif "ilo.org" in final_url:
            m = re.search(r'href="([^"]+\.pdf)"', html)
            if m:
                link = m.group(1)
                pdf_url = link if link.startswith("http") else urljoin(final_url, link)

        elif "ssrn.com" in final_url or "papers.ssrn.com" in final_url:
            m = re.search(r'href="(/sol3/Delivery\.cfm[^"]*)"', html)
            if not m:
                m = re.search(r'href="(https?://[^"]*ssrn[^"]*Delivery\.cfm[^"]*)"', html)
            if not m:
                m_id = re.search(r'abstract[_-]?id[=\s]+(\d+)', html, re.IGNORECASE)
                if m_id:
                    abstract_id = m_id.group(1)
                    pdf_url = f"https://papers.ssrn.com/sol3/Delivery.cfm?abstractid={abstract_id}"
            if m and not pdf_url:
                link = m.group(1)
                pdf_url = link if link.startswith("http") else "https://papers.ssrn.com" + link

        elif "harvard.edu" in final_url:
            m = re.search(r'href="([^"]+\.pdf)"', html)
            if m:
                link = m.group(1)
                pdf_url = link if link.startswith("http") else urljoin(final_url, link)

        elif "epi.org" in final_url:
            m = re.search(r'href="([^"]+\.pdf)"', html)
            if m:
                link = m.group(1)
                pdf_url = link if link.startswith("http") else urljoin(final_url, link)

        elif "nber.org" in final_url:
            m = re.search(r'href="([^"]+\.pdf)"', html)
            if m:
                link = m.group(1)
                pdf_url = link if link.startswith("http") else urljoin(final_url, link)

    if not pdf_url:
        return False, "URL scrape: no PDF link found on page"

    ok, msg = download_pdf(pdf_url, output_path)
    if not ok:
        return False, f"URL scrape: found {pdf_url[:80]}... but download failed: {msg}"
    return True, f"URL scrape -> {pdf_url[:80]}"


def try_doi_scrape(doi: str, output_path: Path) -> tuple[bool, str]:
    """Strategy 12: Follow DOI redirect and parse publisher page for PDF link."""
    if not doi:
        return False, "No DOI"

    _rate_limit("doi_scrape")
    try:
        doi_url = f"https://doi.org/{doi}"
        req = urllib.request.Request(doi_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            final_url = resp.geturl()
            html = resp.read().decode("utf-8", errors="ignore")

        pdf_url = None

        if "nature.com" in final_url:
            m = re.search(r'href="(/articles/[^"]+\.pdf)"', html)
            if m:
                pdf_url = "https://www.nature.com" + m.group(1)

        elif "springer.com" in final_url or "link.springer.com" in final_url:
            m = re.search(r'href="(/content/pdf/[^"]+\.pdf)"', html)
            if m:
                pdf_url = "https://link.springer.com" + m.group(1)

        elif "royalsocietypublishing.org" in final_url:
            m = re.search(r'href="(/doi/pdf/[^"]+)"', html)
            if m:
                pdf_url = "https://royalsocietypublishing.org" + m.group(1)

        elif "mdpi.com" in final_url:
            m_att = re.search(r'href="(https?://mdpi-res\.com/d_attachment/[^"]+)"', html)
            if m_att:
                pdf_url = m_att.group(1)
            else:
                m = re.search(r'href="(/\d+/\d+/\d+/pdf)"', html)
                if m:
                    pdf_url = "https://www.mdpi.com" + m.group(1)
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
    """Strategy 13: CORE.ac.uk title-based search in institutional repositories."""
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
# Paper loading — ISIC-specific (scans 10 numbered subdirectories)
# ═══════════════════════════════════════════════════════════════════════════════

def _get_subdirs() -> list[Path]:
    """Return sorted list of numbered subdirectories (01-* through 10-*)."""
    return sorted(
        d for d in BACKGROUND_DIR.iterdir()
        if d.is_dir() and re.match(r'^\d{2}-', d.name)
    )


def _extract_arxiv_id(doi: str, url: str) -> str:
    """Extract arXiv ID from DOI (10.48550/arXiv.XXXX.XXXXX) or URL (arxiv.org/abs/XXXX.XXXXX)."""
    # From DOI: 10.48550/arXiv.2208.12645 or 10.48550/arxiv.2501.11457
    if doi:
        m = re.search(r'10\.48550/arxiv\.(\d{4}\.\d{4,5})', doi, re.IGNORECASE)
        if m:
            return m.group(1)
    # From URL: https://arxiv.org/abs/2304.04914
    if url:
        m = re.search(r'arxiv\.org/abs/(\d{4}\.\d{4,5})', url)
        if m:
            return m.group(1)
    return ""


def load_papers_needing_pdfs() -> list[dict]:
    """Find all papers without document_acquired: true across all subdirectories."""
    papers = []
    for subdir in _get_subdirs():
        for f in sorted(subdir.iterdir()):
            if not f.suffix == ".md":
                continue
            # Skip expert summary/results files
            if f.name.startswith("expert"):
                continue

            content = f.read_text(encoding="utf-8")
            if "document_acquired: true" in content:
                continue
            if "download_status: \"manual-download-required\"" in content:
                continue

            def field(name, _content=content):
                m = re.search(rf'^{name}:\s*"?([^\"\n]+?)"?\s*$', _content, re.MULTILINE)
                return m.group(1).strip() if m else ""

            doi = field("doi")
            url = field("url")
            arxiv_id = _extract_arxiv_id(doi, url)

            papers.append({
                "path": f,
                "stem": f.stem,
                "doi": doi,
                "arxiv_id": arxiv_id,
                "ssrn_id": "",
                "pmc_id": "",
                "url": url,
                "year": field("year"),
                "full_title": field("title"),
            })
    return papers


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
        m = re.search(r'^---\s*$', content[3:], re.MULTILINE)
        if m:
            insert_pos = 3 + m.start()
            new_content = content[:insert_pos] + line + "\n" + content[insert_pos:]
        else:
            new_content = content.rstrip() + f"\n{line}\n"

    paper_path.write_text(new_content, encoding="utf-8")


# ═══════════════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════════════

def run_downloads(start: int = 1, end: Optional[int] = None, dry_run: bool = False):
    DOCS_DIR.mkdir(exist_ok=True)
    papers = load_papers_needing_pdfs()
    total = len(papers)
    print(f"Found {total} papers needing PDFs")

    if end is None:
        end = total
    batch = papers[start - 1:end]
    print(f"Processing papers {start}-{end} ({len(batch)} papers)\n")

    success = 0
    failed = 0
    manual = 0

    for i, paper in enumerate(batch, start):
        print(f"[{i}/{end}] {paper['stem']}")
        if dry_run:
            print(f"  DRY RUN - would try: arXiv({paper['arxiv_id']}) | DOI({paper['doi']}) | URL({paper['url'][:50] if paper['url'] else 'none'})")
            continue

        pdf_filename = paper["stem"] + ".pdf"
        output_path = DOCS_DIR / pdf_filename

        # If PDF already on disk and valid, just write metadata
        if output_path.exists() and output_path.stat().st_size > 1000:
            with open(output_path, "rb") as fh:
                if fh.read(5) == b"%PDF-":
                    print(f"  OK Already on disk: {pdf_filename}")
                    update_paper_field(paper["path"], "local_document", f"Documents/{pdf_filename}")
                    update_paper_field(paper["path"], "document_acquired", "true")
                    success += 1
                    continue

        # Waterfall (13 strategies)
        strategies = [
            ("arXiv",            lambda p=paper, o=output_path: try_arxiv(p["arxiv_id"], o)),
            ("Preprint Direct",  lambda p=paper, o=output_path: try_preprint_direct(p["doi"], o)),
            ("Zenodo",           lambda p=paper, o=output_path: try_zenodo(p["doi"], o)),
            ("Unpaywall",        lambda p=paper, o=output_path: try_unpaywall(p["doi"], o)),
            ("EuropePMC",        lambda p=paper, o=output_path: try_europepmc(p["doi"], o)),
            ("OA Button",        lambda p=paper, o=output_path: try_oa_button(p["doi"], o)),
            ("Semantic Scholar", lambda p=paper, o=output_path: try_semantic_scholar(p["doi"], p["arxiv_id"], o)),
            ("OpenAlex",         lambda p=paper, o=output_path: try_openalex(p["doi"], o)),
            ("Direct URL",       lambda p=paper, o=output_path: try_direct_url(p["url"], o)),
            ("Handle.net",       lambda p=paper, o=output_path: try_handle_net(p["url"], o)),
            ("URL Scrape",       lambda p=paper, o=output_path: try_url_scrape(p["url"], o)),
            ("DOI Scrape",       lambda p=paper, o=output_path: try_doi_scrape(p["doi"], o)),
            ("CORE",             lambda p=paper, o=output_path: try_core(p["full_title"], o)),
        ]

        downloaded = False
        for strategy_name, strategy_fn in strategies:
            ok, msg = strategy_fn()
            if ok:
                print(f"  OK {strategy_name}: {pdf_filename}")
                update_paper_field(paper["path"], "local_document", f"Documents/{pdf_filename}")
                update_paper_field(paper["path"], "document_acquired", "true")
                downloaded = True
                success += 1
                break
            else:
                print(f"  X  {strategy_name}: {msg}")

        if not downloaded:
            print(f"  -> MANUAL DOWNLOAD REQUIRED")
            update_paper_field(paper["path"], "download_status", "manual-download-required")
            manual += 1
            failed += 1

    print(f"\n{'='*50}")
    print(f"Downloaded: {success}  |  Manual required: {manual}  |  Failed: {failed}")


def show_report():
    subdirs = _get_subdirs()
    all_papers = []
    for subdir in subdirs:
        for f in sorted(subdir.iterdir()):
            if f.suffix == ".md" and not f.name.startswith("expert"):
                all_papers.append(f)

    total = len(all_papers)
    acquired = 0
    manual = 0
    for f in all_papers:
        content = f.read_text(encoding="utf-8")
        if "document_acquired: true" in content:
            acquired += 1
        elif 'download_status: "manual-download-required"' in content:
            manual += 1

    print(f"Papers: {total}")
    print(f"  Acquired:        {acquired} ({100*acquired//total if total else 0}%)")
    print(f"  Manual needed:   {manual}")
    print(f"  Pending:         {total - acquired - manual}")

    docs = list(DOCS_DIR.glob("*.pdf")) if DOCS_DIR.exists() else []
    print(f"\nDocuments in Documents/: {len(docs)}")


if __name__ == "__main__":
    args = sys.argv[1:]

    if "--report" in args:
        show_report()
    elif "--dry-run" in args:
        remaining = [a for a in args if a != "--dry-run"]
        start = int(remaining[0]) if remaining and remaining[0].isdigit() else 1
        end = int(remaining[1]) if len(remaining) > 1 and remaining[1].isdigit() else None
        run_downloads(start, end, dry_run=True)
    else:
        start = int(args[0]) if args and args[0].isdigit() else 1
        end = int(args[1]) if len(args) > 1 and args[1].isdigit() else None
        run_downloads(start, end, dry_run=False)
