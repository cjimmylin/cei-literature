#!/usr/bin/env python3
"""
Comprehensive PDF Finder — 15-Strategy Waterfall for Missing Papers

Finds and downloads PDFs for the 52+ non-arXiv papers from the exhaustive
search import (DATE_ADDED=20260207) that lack local PDFs.

Strategies (cascading waterfall):
  Tier 1: Direct download, Unpaywall, EuropePMC, ACL Anthology, OpenReview,
          Semantic Scholar
  Tier 2: arXiv title search, OpenAlex (incl. preprint locations), CrossRef,
          DBLP, NeurIPS direct URL
  Tier 3: DOI publisher scrape (incl. MDPI d_attachment), CORE, PhilArchive,
          Manual URL generation

Usage:
    python3 PYTHON/comprehensive_pdf_finder.py 1 53             # Full run
    python3 PYTHON/comprehensive_pdf_finder.py 1 53 --dry-run   # Discovery only
    python3 PYTHON/comprehensive_pdf_finder.py --retry-failed    # Retry prev failures
    python3 PYTHON/comprehensive_pdf_finder.py --report          # Show results

Run from CEI-Lit-WS/ directory.
"""

import functools
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Force flush for parallel batch monitoring
print = functools.partial(print, flush=True)

# ═══════════════════════════════════════════════════════════════════════════════
# Configuration
# ═══════════════════════════════════════════════════════════════════════════════

PAPERS_DIR = Path("papers")
VAULT_CONFIG = Path(".vault-config.json")
LOG_DIR = Path("logs")
LOG_FILE = None  # Set dynamically in main() based on --date arg
CURL_TIMEOUT = 60
MAX_RETRIES = 2
UNPAYWALL_EMAIL = "research@cei-literature.org"

HEADERS = {
    "User-Agent": "CEI-Literature-Vault/2.0 (Academic Research; mailto:research@cei-literature.org)"
}

# Rate limits (seconds between requests per source)
RATE_LIMITS = {
    "unpaywall": 1.0,
    "europepmc": 1.0,
    "acl": 1.0,
    "openreview": 1.0,
    "semantic_scholar": 4.0,
    "arxiv": 3.0,
    "openalex": 0.1,  # 10 req/s allowed
    "crossref": 0.02,  # 50 req/s allowed
    "dblp": 1.0,
    "core": 1.0,
    "philarchive": 1.0,
    "doi_scrape": 1.0,
    "download": 1.0,
}

# Strategy ordering per category
STRATEGY_ORDER = {
    "A": [  # Has DOI
        "direct_download", "unpaywall", "europepmc",
        "semantic_scholar", "crossref", "arxiv_title",
        "openalex", "doi_scrape", "manual_urls"
    ],
    "B": [  # Known conference, no DOI
        "direct_download", "acl_anthology", "openreview",
        "neurips_direct", "arxiv_title", "semantic_scholar",
        "dblp", "openalex", "europepmc", "manual_urls"
    ],
    "C": [  # Minimal metadata
        "direct_download", "arxiv_title", "semantic_scholar",
        "openalex", "europepmc", "core", "philarchive",
        "dblp", "manual_urls"
    ],
}


# ═══════════════════════════════════════════════════════════════════════════════
# Helpers
# ═══════════════════════════════════════════════════════════════════════════════


def get_pdfs_dir() -> Path:
    """Get PDF storage directory from vault config."""
    config = json.loads(VAULT_CONFIG.read_text())
    return Path(config["pdf_path"])


def api_get(url: str, source: str, timeout: int = 15) -> Optional[dict]:
    """Make a rate-limited GET request and return parsed JSON, or None."""
    _rate_limit(source)
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception:
        return None


def api_get_xml(url: str, source: str, timeout: int = 15) -> Optional[str]:
    """Make a rate-limited GET request and return raw XML string, or None."""
    _rate_limit(source)
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8")
    except Exception:
        return None


_last_request_time: Dict[str, float] = {}


def _rate_limit(source: str):
    """Enforce per-source rate limiting."""
    global _last_request_time
    limit = RATE_LIMITS.get(source, 1.0)
    now = time.time()
    if source in _last_request_time:
        elapsed = now - _last_request_time[source]
        if elapsed < limit:
            time.sleep(limit - elapsed)
    _last_request_time[source] = time.time()


def normalize_title(title: str) -> str:
    """Normalize a title for fuzzy matching."""
    t = title.lower().strip()
    t = re.sub(r"[^a-z0-9\s]", "", t)
    t = re.sub(r"\s+", " ", t)
    return t


def titles_match(t1: str, t2: str) -> bool:
    """Check if two titles are similar enough to be the same paper."""
    n1 = normalize_title(t1)
    n2 = normalize_title(t2)
    if not n1 or not n2:
        return False
    # Exact match after normalization
    if n1 == n2:
        return True
    # One contains the other (handles subtitle differences)
    if n1 in n2 or n2 in n1:
        return True
    # Check word overlap (>80% of shorter title's words present in longer)
    words1 = set(n1.split())
    words2 = set(n2.split())
    if not words1 or not words2:
        return False
    shorter = min(words1, words2, key=len)
    longer = max(words1, words2, key=len)
    overlap = len(shorter & longer) / len(shorter)
    return overlap >= 0.80


# ═══════════════════════════════════════════════════════════════════════════════
# Paper discovery & classification
# ═══════════════════════════════════════════════════════════════════════════════


def extract_paper_metadata(paper_path: Path) -> dict:
    """Extract metadata from a paper's YAML frontmatter."""
    content = paper_path.read_text(encoding="utf-8")
    meta = {
        "path": paper_path,
        "filename": paper_path.name,
        "pdf_filename": paper_path.stem + ".pdf",
    }

    def field(name):
        m = re.search(rf"^{name}:\s*\"?([^\"\n]+?)\"?\s*$", content, re.MULTILINE)
        return m.group(1).strip() if m else ""

    meta["short_title"] = field("short_title")
    meta["title"] = meta["short_title"] or paper_path.stem
    meta["year"] = field("year")
    meta["authors"] = field("authors")
    meta["first_author"] = field("first_author").strip("[]").replace("[[", "").replace("]]", "")
    meta["url"] = field("url")
    meta["doi"] = field("doi")
    meta["publication"] = field("publication")
    meta["external_pdf"] = field("external_pdf")
    meta["type"] = field("type")

    # Extract DOI from url if doi field empty
    if not meta["doi"] and meta["url"]:
        doi_m = re.search(r"doi\.org/(10\.\S+)", meta["url"])
        if doi_m:
            meta["doi"] = doi_m.group(1).rstrip("/")

    return meta


def classify_paper(meta: dict) -> str:
    """Classify paper into category A (DOI), B (conference), or C (minimal)."""
    if meta["doi"]:
        return "A"
    pub = meta["publication"].lower()
    conf_keywords = [
        "acl", "emnlp", "naacl", "coling", "eacl", "neurips", "icml", "iclr",
        "aaai", "ijcai", "aies", "facct", "chi", "www", "sigir", "workshop",
        "findings", "tacl", "colm",
    ]
    if any(kw in pub for kw in conf_keywords):
        return "B"
    return "C"


def parse_date_arg(argv, default="20260207"):
    """Extract --date YYYYMMDD from argv, or return default."""
    for i, arg in enumerate(argv):
        if arg == '--date' and i + 1 < len(argv):
            return argv[i + 1]
    return default


# Module-level date filter, set in main()
_DATE_ADDED = "20260207"


def get_papers_needing_pdfs() -> List[dict]:
    """Find all EXSR papers without local PDFs."""
    papers = []
    for f in sorted(PAPERS_DIR.glob("*.md")):
        content = f.read_text(encoding="utf-8")
        if f"DATE_ADDED: {_DATE_ADDED}" not in content:
            continue
        # Skip if already has local_pdf wikilink
        if re.search(r'local_pdf:\s*"\[\[', content):
            continue
        meta = extract_paper_metadata(f)
        meta["category"] = classify_paper(meta)
        papers.append(meta)
    return papers


# ═══════════════════════════════════════════════════════════════════════════════
# Download & Validation (from batch_download_pdfs.py)
# ═══════════════════════════════════════════════════════════════════════════════


def download_pdf(url: str, output_path: Path, retries: int = MAX_RETRIES) -> Tuple[bool, str]:
    """Download a PDF using curl with retry logic and %PDF- validation."""
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
                        output_path.unlink()
                        return False, "Not a PDF (HTML error page?)"
                elif output_path.exists():
                    size = output_path.stat().st_size
                    output_path.unlink()
                    return False, f"File too small ({size} bytes)"

            elif http_code == "429":
                if attempt < retries:
                    wait = 10 * (attempt + 1)
                    time.sleep(wait)
                    continue
                return False, f"HTTP 429 (rate limited after {retries} retries)"

            else:
                if output_path.exists():
                    output_path.unlink()
                return False, f"HTTP {http_code}"

        except subprocess.TimeoutExpired:
            if attempt < retries:
                time.sleep(5)
                continue
            return False, "Timeout"
        except Exception as e:
            return False, str(e)

    return False, "Max retries exceeded"


# ═══════════════════════════════════════════════════════════════════════════════
# Safe YAML Updates (from batch_download_pdfs.py — regex insertion, NEVER parse/rebuild)
# ═══════════════════════════════════════════════════════════════════════════════


def safe_update_external_pdf(paper_path: Path, pdf_url: str):
    """Add or update external_pdf field using safe regex insertion."""
    content = paper_path.read_text(encoding="utf-8")
    safe_url = pdf_url.replace('"', "'")
    new_line = f'external_pdf: "{safe_url}"'

    if "external_pdf:" in content:
        # Replace existing line
        content = re.sub(
            r'^external_pdf:.*$',
            new_line,
            content,
            count=1,
            flags=re.MULTILINE,
        )
    elif "url:" in content:
        # Insert after url line
        content = re.sub(
            r'(url:\s*"[^"]*"\n)',
            r'\1' + new_line + '\n',
            content,
            count=1,
        )
    else:
        # Insert before DATE_ADDED
        content = content.replace(
            "DATE_ADDED:",
            new_line + "\nDATE_ADDED:",
        )

    paper_path.write_text(content, encoding="utf-8")


def safe_update_local_pdf(paper_path: Path, pdf_filename: str):
    """Add or update local_pdf field using safe regex insertion."""
    content = paper_path.read_text(encoding="utf-8")
    new_line = f'local_pdf: "[[PDFs/{pdf_filename}]]"'

    if re.search(r'^local_pdf:\s*$', content, re.MULTILINE):
        # Replace empty local_pdf: line
        content = re.sub(
            r'^local_pdf:\s*$',
            new_line,
            content,
            count=1,
            flags=re.MULTILINE,
        )
    elif "local_pdf:" in content:
        # Replace existing line
        content = re.sub(
            r'^local_pdf:.*$',
            new_line,
            content,
            count=1,
            flags=re.MULTILINE,
        )
    elif "external_pdf:" in content:
        # Insert after external_pdf line
        content = re.sub(
            r'(external_pdf:.*\n)',
            r'\1' + new_line + '\n',
            content,
            count=1,
        )
    elif "url:" in content:
        # Insert after url line
        content = re.sub(
            r'(url:\s*"[^"]*"\n)',
            r'\1' + new_line + '\n',
            content,
            count=1,
        )
    else:
        # Insert before DATE_ADDED
        content = content.replace(
            "DATE_ADDED:",
            new_line + "\nDATE_ADDED:",
        )

    paper_path.write_text(content, encoding="utf-8")


# ═══════════════════════════════════════════════════════════════════════════════
# 15 Acquisition Strategies
# ═══════════════════════════════════════════════════════════════════════════════


def strategy_direct_download(meta: dict) -> Optional[str]:
    """Strategy 1: If external_pdf already set, use it directly."""
    if meta["external_pdf"] and meta["external_pdf"].startswith("http"):
        return meta["external_pdf"]
    return None


def strategy_unpaywall(meta: dict) -> Optional[str]:
    """Strategy 2: Unpaywall API — official OA lookup via DOI."""
    doi = meta["doi"]
    if not doi:
        return None

    url = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi, safe='')}?email={UNPAYWALL_EMAIL}"
    data = api_get(url, "unpaywall")
    if not data:
        return None

    if data.get("is_oa") and data.get("oa_locations"):
        for loc in data["oa_locations"]:
            pdf_url = loc.get("url_for_pdf") or loc.get("pdf_url")
            if pdf_url:
                return pdf_url
    return None


def strategy_europepmc(meta: dict) -> Optional[str]:
    """Strategy: EuropePMC — broader OA coverage via PMC-deposited papers.

    Queries EuropePMC REST API by DOI, checks for OA PDF URLs, and falls back
    to PMCID-based ptpmcrender endpoint for PMC-deposited papers (covers
    PNAS, Wiley, Nature, etc. that deposit to PMC after embargo).
    """
    doi = meta["doi"]
    if not doi:
        return None

    encoded = urllib.parse.quote(doi, safe="")
    url = (
        f"https://www.ebi.ac.uk/europepmc/webservices/rest/search"
        f"?query=DOI:{encoded}&format=json&resultType=core"
    )
    data = api_get(url, "europepmc")
    if not data:
        return None

    results = data.get("resultList", {}).get("result", [])
    for r in results:
        # Check fullTextUrlList for direct OA PDF
        ft_urls = r.get("fullTextUrlList", {}).get("fullTextUrl", [])
        for ft in ft_urls:
            if ft.get("documentStyle") == "pdf" and ft.get("availability") == "Open access":
                return ft.get("url")
        # Fallback: use PMCID to construct ptpmcrender URL
        pmcid = r.get("pmcid")
        if pmcid:
            return f"https://europepmc.org/backend/ptpmcrender.fcgi?accid={pmcid}&blobtype=pdf"
    return None


def strategy_acl_anthology(meta: dict) -> Optional[str]:
    """Strategy 3: ACL Anthology search for ACL/EMNLP/NAACL/COLING papers."""
    title = meta["title"]
    if not title:
        return None

    # Check if this is likely an ACL venue paper
    pub = meta["publication"].lower()
    doi = meta["doi"]
    acl_venues = ["acl", "emnlp", "naacl", "coling", "eacl", "tacl", "findings"]
    is_acl = any(v in pub for v in acl_venues) or (doi and "18653" in doi)
    if not is_acl:
        return None

    # ACL Anthology search API
    query = urllib.parse.quote(title[:100])
    url = f"https://aclanthology.org/api/search?q={query}"
    data = api_get(url, "acl")

    # Fallback: try to construct ACL URL from DOI
    if not data and doi and "18653" in doi:
        # DOI pattern: 10.18653/v1/2024.findings-emnlp.928
        parts = doi.split("/")
        if len(parts) >= 3:
            acl_id = parts[-1]  # e.g., 2024.findings-emnlp.928
            return f"https://aclanthology.org/{acl_id}.pdf"

    if data and isinstance(data, list):
        for entry in data[:3]:
            entry_title = entry.get("title", "")
            if titles_match(title, entry_title):
                acl_id = entry.get("id", "")
                if acl_id:
                    return f"https://aclanthology.org/{acl_id}.pdf"

    # Construct from DOI even without search results
    if doi and "18653" in doi:
        parts = doi.split("/")
        if len(parts) >= 3:
            acl_id = parts[-1]
            return f"https://aclanthology.org/{acl_id}.pdf"

    return None


def strategy_openreview(meta: dict) -> Optional[str]:
    """Strategy 4: OpenReview API for NeurIPS/ICML/ICLR papers."""
    title = meta["title"]
    if not title:
        return None

    pub = meta["publication"].lower()
    or_venues = ["neurips", "icml", "iclr", "colm"]
    if not any(v in pub for v in or_venues):
        return None

    query = urllib.parse.quote(title[:120])
    url = f"https://api2.openreview.net/notes/search?query={query}&limit=3"
    data = api_get(url, "openreview")
    if not data or "notes" not in data:
        return None

    for note in data["notes"][:3]:
        note_title = note.get("content", {}).get("title", {})
        if isinstance(note_title, dict):
            note_title = note_title.get("value", "")
        if titles_match(title, str(note_title)):
            note_id = note.get("id", "")
            if note_id:
                return f"https://openreview.net/pdf?id={note_id}"

    return None


def strategy_neurips_direct(meta: dict) -> Optional[str]:
    """Strategy: NeurIPS direct URL pattern — convert proceedings page to PDF.

    NeurIPS proceedings pages use predictable URL patterns:
      .../hash-Abstract-Conference.html  → .../hash-Paper-Conference.pdf
      .../hash-Abstract-Datasets_and_Benchmarks.html → .../hash-Paper-...pdf
    No API call needed — pure URL manipulation.
    """
    url = meta.get("url", "")
    if not url or "neurips.cc" not in url:
        return None

    # Handle all NeurIPS abstract page patterns
    # Pattern: -Abstract-{track}.html → -Paper-{track}.pdf
    pdf_url = re.sub(
        r"-Abstract(-[^.]+)?\.html$",
        lambda m: f"-Paper{m.group(1) or ''}.pdf",
        url,
    )
    if pdf_url != url:
        return pdf_url

    return None


def strategy_semantic_scholar(meta: dict) -> Optional[str]:
    """Strategy 5: Semantic Scholar open access PDF search."""
    title = meta["title"]
    if not title:
        return None

    query = urllib.parse.quote(title[:200])
    url = (
        f"https://api.semanticscholar.org/graph/v1/paper/search"
        f"?query={query}&fields=title,openAccessPdf,externalIds&limit=3"
    )
    data = api_get(url, "semantic_scholar")
    if not data or not data.get("data"):
        return None

    for paper in data["data"][:3]:
        paper_title = paper.get("title", "")
        if titles_match(title, paper_title):
            oa_pdf = paper.get("openAccessPdf")
            if oa_pdf and oa_pdf.get("url"):
                return oa_pdf["url"]
            # Check for arXiv ID as fallback
            ext_ids = paper.get("externalIds", {})
            arxiv_id = ext_ids.get("ArXiv")
            if arxiv_id:
                return f"https://arxiv.org/pdf/{arxiv_id}.pdf"

    return None


def strategy_arxiv_title(meta: dict) -> Optional[str]:
    """Strategy 6: arXiv title search for preprint versions."""
    title = meta["title"]
    if not title:
        return None

    # Clean title for arXiv search
    search_title = title.split("(")[0].split(" -- ")[0].strip()[:120]
    query = urllib.parse.quote(f'ti:"{search_title}"')
    url = f"http://export.arxiv.org/api/query?search_query={query}&start=0&max_results=3&sortBy=relevance"

    xml_str = api_get_xml(url, "arxiv")
    if not xml_str:
        return None

    try:
        root = ET.fromstring(xml_str)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        entries = root.findall("atom:entry", ns)

        for entry in entries[:3]:
            entry_title_el = entry.find("atom:title", ns)
            if entry_title_el is None:
                continue
            entry_title = entry_title_el.text.strip().replace("\n", " ")
            if titles_match(title, entry_title):
                id_el = entry.find("atom:id", ns)
                if id_el is not None:
                    arxiv_id = id_el.text.split("/abs/")[-1].strip()
                    if re.match(r"\d{4}\.\d{4,5}", arxiv_id):
                        return f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    except ET.ParseError:
        pass

    return None


def strategy_openalex(meta: dict) -> Optional[str]:
    """Strategy 7: OpenAlex works search (incl. alternate OA locations).

    Enhanced to check ALL locations (not just primary_location), which catches
    preprints on Research Square, SSRN, bioRxiv, institutional repositories, etc.
    Also does a follow-up OA-only search if the matched work is not itself OA.
    """
    title = meta["title"]
    if not title:
        return None

    search_title = title[:150]
    url = (
        f"https://api.openalex.org/works"
        f"?filter=title.search:{urllib.parse.quote(search_title)}"
        f"&select=id,title,open_access,primary_location,locations"
        f"&per_page=3"
    )
    data = api_get(url, "openalex")
    if not data or not data.get("results"):
        return None

    for work in data["results"][:3]:
        work_title = work.get("title", "")
        if not titles_match(title, work_title):
            continue

        # Check primary OA URL first
        oa = work.get("open_access", {})
        oa_url = oa.get("oa_url")
        if oa_url and oa_url.endswith(".pdf"):
            return oa_url

        # Check primary_location
        loc = work.get("primary_location") or {}
        pdf_url = loc.get("pdf_url")
        if pdf_url:
            return pdf_url

        # Check ALL locations for alternate OA versions (preprints, repos)
        for location in work.get("locations", []):
            if location.get("is_oa"):
                loc_pdf = location.get("pdf_url")
                if loc_pdf:
                    return loc_pdf

        # Return oa_url as last resort (might redirect to PDF)
        if oa_url:
            return oa_url

        # If matched work is not OA, try a follow-up OA-filtered search
        if not oa.get("is_oa"):
            oa_url2 = (
                f"https://api.openalex.org/works"
                f"?filter=title.search:{urllib.parse.quote(search_title)},is_oa:true"
                f"&select=id,title,open_access,primary_location,locations"
                f"&per_page=3"
            )
            data2 = api_get(oa_url2, "openalex")
            if data2 and data2.get("results"):
                for w2 in data2["results"][:3]:
                    if titles_match(title, w2.get("title", "")):
                        oa2 = w2.get("open_access", {})
                        if oa2.get("oa_url"):
                            loc2 = w2.get("primary_location") or {}
                            if loc2.get("pdf_url"):
                                return loc2["pdf_url"]
                            for loc2alt in w2.get("locations", []):
                                if loc2alt.get("is_oa") and loc2alt.get("pdf_url"):
                                    return loc2alt["pdf_url"]
                            return oa2["oa_url"]

    return None


def strategy_crossref(meta: dict) -> Optional[str]:
    """Strategy 8: CrossRef metadata for DOI papers — finds license/link info."""
    doi = meta["doi"]
    if not doi:
        return None

    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='')}"
    data = api_get(url, "crossref")
    if not data or "message" not in data:
        return None

    msg = data["message"]
    # Check for open-access links
    links = msg.get("link", [])
    for link in links:
        if link.get("content-type") == "application/pdf":
            return link.get("URL")
        if "unspecified" in link.get("content-type", ""):
            link_url = link.get("URL", "")
            if ".pdf" in link_url.lower():
                return link_url

    return None


def strategy_dblp(meta: dict) -> Optional[str]:
    """Strategy 9: DBLP search for CS conference papers."""
    title = meta["title"]
    if not title:
        return None

    query = urllib.parse.quote(title[:100])
    url = f"https://dblp.org/search/publ/api?q={query}&format=json&h=3"
    data = api_get(url, "dblp")
    if not data:
        return None

    hits = data.get("result", {}).get("hits", {}).get("hit", [])
    for hit in hits[:3]:
        info = hit.get("info", {})
        hit_title = info.get("title", "").rstrip(".")
        if titles_match(title, hit_title):
            # DBLP provides ee (electronic edition) links
            ee = info.get("ee")
            if isinstance(ee, str) and ee.endswith(".pdf"):
                return ee
            if isinstance(ee, list):
                for link in ee:
                    if isinstance(link, str) and link.endswith(".pdf"):
                        return link

    return None


def strategy_doi_scrape(meta: dict) -> Optional[str]:
    """Strategy 10: Follow DOI redirect and look for PDF link on publisher page."""
    doi = meta["doi"]
    if not doi:
        return None

    _rate_limit("doi_scrape")
    try:
        doi_url = f"https://doi.org/{doi}"
        req = urllib.request.Request(doi_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            final_url = resp.geturl()
            html = resp.read().decode("utf-8", errors="ignore")

        # Nature pattern: content/pdf links
        if "nature.com" in final_url:
            m = re.search(r'href="(/articles/[^"]+\.pdf)"', html)
            if m:
                return "https://www.nature.com" + m.group(1)

        # PLOS pattern
        if "plosone.org" in final_url or "plos.org" in final_url:
            m = re.search(r'(https://journals\.plos\.org/[^"]+representation=PDF)', html)
            if m:
                return m.group(1)

        # Springer pattern
        if "springer.com" in final_url or "link.springer.com" in final_url:
            m = re.search(r'href="(/content/pdf/[^"]+\.pdf)"', html)
            if m:
                return "https://link.springer.com" + m.group(1)

        # Royal Society pattern
        if "royalsocietypublishing.org" in final_url:
            m = re.search(r'href="(/doi/pdf/[^"]+)"', html)
            if m:
                return "https://royalsocietypublishing.org" + m.group(1)

        # MDPI pattern (enhanced with d_attachment)
        if "mdpi.com" in final_url:
            # Check for d_attachment / mdpi-res.com links (most reliable)
            m_att = re.search(r'href="(https?://mdpi-res\.com/d_attachment/[^"]+)"', html)
            if m_att:
                return m_att.group(1)
            m_att2 = re.search(r'href="([^"]*d_attachment[^"]*\.pdf[^"]*)"', html)
            if m_att2:
                link = m_att2.group(1)
                if link.startswith("http"):
                    return link
                return "https://mdpi-res.com" + link
            # Standard MDPI PDF path
            m = re.search(r'href="(/\d+/\d+/\d+/pdf)"', html)
            if m:
                return "https://www.mdpi.com" + m.group(1)
            # MDPI direct PDF pattern
            if "/pdf" not in final_url:
                return final_url.rstrip("/") + "/pdf"

        # ScienceDirect / Elsevier
        if "sciencedirect.com" in final_url:
            m = re.search(r'"pdfLink":"([^"]+)"', html)
            if m:
                return m.group(1).replace("\\u002F", "/")

        # PNAS pattern
        if "pnas.org" in final_url:
            m = re.search(r'href="([^"]+\.full\.pdf)"', html)
            if m:
                if m.group(1).startswith("http"):
                    return m.group(1)
                return "https://www.pnas.org" + m.group(1)

        # IOS Press (SHTI series)
        if "iospress.com" in final_url or "content.iospress" in final_url:
            m = re.search(r'href="([^"]+/pdf)"', html)
            if m:
                return m.group(1)

        # ACM DL pattern
        if "dl.acm.org" in final_url:
            m = re.search(r'href="(/doi/pdf/[^"]+)"', html)
            if m:
                return "https://dl.acm.org" + m.group(1)

        # Generic: look for PDF link on the page
        pdf_links = re.findall(r'href="([^"]*\.pdf[^"]*)"', html)
        if pdf_links:
            link = pdf_links[0]
            if link.startswith("http"):
                return link
            if link.startswith("/"):
                # Reconstruct base URL
                from urllib.parse import urlparse
                parsed = urlparse(final_url)
                return f"{parsed.scheme}://{parsed.netloc}{link}"

    except Exception:
        pass

    return None


def strategy_core(meta: dict) -> Optional[str]:
    """Strategy 11: CORE.ac.uk search for open access papers."""
    title = meta["title"]
    if not title:
        return None

    query = urllib.parse.quote(title[:120])
    url = f"https://api.core.ac.uk/v3/search/works?q={query}&limit=3"
    data = api_get(url, "core")
    if not data or not data.get("results"):
        return None

    for work in data["results"][:3]:
        work_title = work.get("title", "")
        if titles_match(title, work_title):
            dl_url = work.get("downloadUrl")
            if dl_url:
                return dl_url

    return None


def strategy_philarchive(meta: dict) -> Optional[str]:
    """Strategy 12: PhilArchive/PhilPapers search for philosophy papers."""
    title = meta["title"]
    if not title:
        return None

    # Only try for papers that look like philosophy/ethics
    pub = meta["publication"].lower()
    title_lower = title.lower()
    phil_indicators = [
        "moral", "ethic", "virtue", "deontol", "utilitarian", "coherent",
        "philosophy", "normative", "value", "philarchive", "philpapers",
    ]
    if not any(ind in title_lower or ind in pub for ind in phil_indicators):
        return None

    query = urllib.parse.quote(title[:100])
    url = f"https://philpapers.org/s/{query}"
    _rate_limit("philarchive")

    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="ignore")

        # Look for direct PDF links
        pdf_links = re.findall(r'href="(https?://[^"]*\.pdf[^"]*)"', html)
        for link in pdf_links[:3]:
            if "philarchive.org" in link or "philpapers.org" in link:
                return link

    except Exception:
        pass

    return None


def strategy_manual_urls(meta: dict) -> Optional[str]:
    """Strategy 13: Generate manual search URLs (no download, just logging)."""
    # This strategy never returns a download URL — it logs search suggestions
    # The caller handles this specially
    return None


def generate_manual_search_urls(meta: dict) -> List[dict]:
    """Generate manual search URLs for human follow-up."""
    urls = []
    title = meta["title"]
    author = meta["first_author"]

    if title:
        q = urllib.parse.quote(f'"{title}"')

        urls.append({
            "source": "Google Scholar",
            "url": f"https://scholar.google.com/scholar?q={q}",
        })
        urls.append({
            "source": "ResearchGate",
            "url": f"https://www.researchgate.net/search?q={q}",
        })

    if author and title:
        q = urllib.parse.quote(f"{title} {author}")
        urls.append({
            "source": "Google (site:pdf)",
            "url": f"https://www.google.com/search?q={q}+filetype:pdf",
        })

    return urls


# ═══════════════════════════════════════════════════════════════════════════════
# Waterfall Engine
# ═══════════════════════════════════════════════════════════════════════════════

STRATEGIES = {
    "direct_download": strategy_direct_download,
    "unpaywall": strategy_unpaywall,
    "europepmc": strategy_europepmc,
    "acl_anthology": strategy_acl_anthology,
    "openreview": strategy_openreview,
    "neurips_direct": strategy_neurips_direct,
    "semantic_scholar": strategy_semantic_scholar,
    "arxiv_title": strategy_arxiv_title,
    "openalex": strategy_openalex,
    "crossref": strategy_crossref,
    "dblp": strategy_dblp,
    "doi_scrape": strategy_doi_scrape,
    "core": strategy_core,
    "philarchive": strategy_philarchive,
    "manual_urls": strategy_manual_urls,
}


def run_waterfall(meta: dict, dry_run: bool = False) -> dict:
    """Run the strategy waterfall for a single paper.

    Returns a result dict with:
        found: bool
        strategy: str (winning strategy name)
        pdf_url: str
        manual_urls: list (if no strategy found a PDF)
        error: str (if download failed)
    """
    category = meta["category"]
    order = STRATEGY_ORDER.get(category, STRATEGY_ORDER["C"])
    result = {
        "found": False,
        "strategy": None,
        "pdf_url": None,
        "manual_urls": [],
        "error": None,
    }

    for strat_name in order:
        strat_fn = STRATEGIES.get(strat_name)
        if not strat_fn:
            continue

        if strat_name == "manual_urls":
            # Special: doesn't return a URL, just logs
            result["manual_urls"] = generate_manual_search_urls(meta)
            continue

        try:
            pdf_url = strat_fn(meta)
        except Exception as e:
            print(f"         [{strat_name}] ERROR: {e}")
            continue

        if pdf_url:
            result["found"] = True
            result["strategy"] = strat_name
            result["pdf_url"] = pdf_url
            return result

    return result


# ═══════════════════════════════════════════════════════════════════════════════
# JSON Logging
# ═══════════════════════════════════════════════════════════════════════════════


def load_log() -> dict:
    """Load progress log."""
    if LOG_FILE.exists():
        return json.loads(LOG_FILE.read_text())
    return {"results": {}, "summary": {}, "timestamp": ""}


def save_log(log: dict):
    """Save progress log."""
    LOG_DIR.mkdir(exist_ok=True)
    log["timestamp"] = datetime.now().isoformat()
    LOG_FILE.write_text(json.dumps(log, indent=2))


# ═══════════════════════════════════════════════════════════════════════════════
# Main Runner
# ═══════════════════════════════════════════════════════════════════════════════


def run_report():
    """Show results from previous runs."""
    log = load_log()
    results = log.get("results", {})

    if not results:
        print("No results yet. Run the finder first.")
        return

    downloaded = [k for k, v in results.items() if v.get("status") == "downloaded"]
    found_only = [k for k, v in results.items() if v.get("status") == "found"]
    failed = [k for k, v in results.items() if v.get("status") == "failed"]
    not_found = [k for k, v in results.items() if v.get("status") == "not_found"]

    print(f"\n{'='*70}")
    print("COMPREHENSIVE PDF FINDER — RESULTS REPORT")
    print(f"{'='*70}")
    print(f"  Downloaded:   {len(downloaded):3d}")
    print(f"  Found (URL):  {len(found_only):3d}")
    print(f"  Failed DL:    {len(failed):3d}")
    print(f"  Not found:    {len(not_found):3d}")
    print(f"  Total:        {len(results):3d}")

    # Strategy breakdown
    strat_counts: Dict[str, int] = {}
    for v in results.values():
        s = v.get("strategy", "none")
        strat_counts[s] = strat_counts.get(s, 0) + 1

    print(f"\nStrategy breakdown:")
    for s, c in sorted(strat_counts.items(), key=lambda x: -x[1]):
        print(f"  {s:25s}: {c:3d}")

    # Not found details
    if not_found:
        print(f"\nPapers still missing ({len(not_found)}):")
        for name in sorted(not_found):
            r = results[name]
            print(f"  - {name}")
            for mu in r.get("manual_urls", [])[:2]:
                print(f"    {mu['source']}: {mu['url']}")

    print(f"\n{'='*70}")


def main():
    global _DATE_ADDED, LOG_FILE
    # Parse args
    args = sys.argv[1:]
    _DATE_ADDED = parse_date_arg(sys.argv)
    LOG_FILE = LOG_DIR / f"{_DATE_ADDED}-comprehensive_pdf_finder_log.json"
    print(f"Filtering by DATE_ADDED: {_DATE_ADDED}")

    if "--report" in args:
        run_report()
        return

    retry_failed = "--retry-failed" in args
    dry_run = "--dry-run" in args

    if retry_failed:
        # Re-process papers that failed in previous runs
        log = load_log()
        old_results = log.get("results", {})
        failed_names = {k for k, v in old_results.items() if v.get("status") in ("failed", "not_found")}
        if not failed_names:
            print("No failed papers to retry.")
            return
        print(f"Retrying {len(failed_names)} previously failed papers...")
        all_papers = get_papers_needing_pdfs()
        all_papers = [p for p in all_papers if p["filename"] in failed_names]
        start = 1
        end = len(all_papers)
    else:
        # Positional START END (skip --date and its value)
        skip_next = False
        num_args = []
        for a in args:
            if skip_next:
                skip_next = False
                continue
            if a == '--date':
                skip_next = True
                continue
            if not a.startswith("--"):
                num_args.append(a)
        if len(num_args) < 2:
            print("Usage: python3 PYTHON/comprehensive_pdf_finder.py START END [--dry-run] [--date YYYYMMDD]")
            print("       python3 PYTHON/comprehensive_pdf_finder.py --retry-failed [--date YYYYMMDD]")
            print("       python3 PYTHON/comprehensive_pdf_finder.py --report")
            sys.exit(1)

        start = int(num_args[0])
        end = int(num_args[1])
        all_papers = get_papers_needing_pdfs()

    pdfs_dir = get_pdfs_dir()
    if not pdfs_dir.exists():
        print(f"ERROR: PDF directory not found: {pdfs_dir}")
        sys.exit(1)

    print(f"Total papers needing PDFs: {len(all_papers)}")

    if not retry_failed:
        batch = all_papers[start - 1:end]
    else:
        batch = all_papers

    print(f"Processing positions {start}-{end} ({len(batch)} papers)")
    if dry_run:
        print("*** DRY RUN MODE — no downloads ***")
    print()

    # Category breakdown
    cats = {"A": 0, "B": 0, "C": 0}
    for p in batch:
        cats[p["category"]] = cats.get(p["category"], 0) + 1
    print(f"Categories: A(DOI)={cats['A']}  B(Conference)={cats['B']}  C(Minimal)={cats['C']}")
    print()

    # Load existing log
    log = load_log()
    results = log.get("results", {})

    downloaded = 0
    found_only = 0
    failed = 0
    not_found = 0
    skipped = 0

    for i, meta in enumerate(batch):
        pos = start + i if not retry_failed else i + 1
        pdf_path = pdfs_dir / meta["pdf_filename"]

        # Skip if PDF already exists on disk
        if pdf_path.exists() and pdf_path.stat().st_size > 1000:
            print(f"  [{pos:3d}] SKIP (exists): {meta['pdf_filename']}")
            skipped += 1
            results[meta["filename"]] = {
                "status": "skipped",
                "strategy": "existing",
                "category": meta["category"],
            }
            continue

        print(f"  [{pos:3d}] [{meta['category']}] {meta['filename'][:60]}")
        print(f"         Title: {meta['title'][:65]}")
        if meta["doi"]:
            print(f"         DOI:   {meta['doi']}")

        # Run waterfall
        wf_result = run_waterfall(meta, dry_run=dry_run)

        if wf_result["found"]:
            print(f"         FOUND via {wf_result['strategy']}: {wf_result['pdf_url'][:80]}")

            if dry_run:
                found_only += 1
                results[meta["filename"]] = {
                    "status": "found",
                    "strategy": wf_result["strategy"],
                    "pdf_url": wf_result["pdf_url"],
                    "category": meta["category"],
                }
            else:
                # Download
                _rate_limit("download")
                ok, msg = download_pdf(wf_result["pdf_url"], pdf_path)

                if ok:
                    size_kb = pdf_path.stat().st_size / 1024
                    print(f"         DOWNLOADED ({size_kb:.0f}KB)")
                    downloaded += 1

                    # Update YAML
                    try:
                        safe_update_external_pdf(meta["path"], wf_result["pdf_url"])
                        safe_update_local_pdf(meta["path"], meta["pdf_filename"])
                    except Exception as e:
                        print(f"         WARNING: YAML update failed: {e}")

                    results[meta["filename"]] = {
                        "status": "downloaded",
                        "strategy": wf_result["strategy"],
                        "pdf_url": wf_result["pdf_url"],
                        "size_kb": size_kb,
                        "category": meta["category"],
                    }
                else:
                    print(f"         DOWNLOAD FAILED: {msg}")
                    failed += 1
                    results[meta["filename"]] = {
                        "status": "failed",
                        "strategy": wf_result["strategy"],
                        "pdf_url": wf_result["pdf_url"],
                        "error": msg,
                        "category": meta["category"],
                    }
        else:
            print(f"         NOT FOUND (tried {len(STRATEGY_ORDER[meta['category']])} strategies)")
            not_found += 1
            results[meta["filename"]] = {
                "status": "not_found",
                "manual_urls": wf_result["manual_urls"],
                "category": meta["category"],
            }

        # Save progress every 5 papers
        if (i + 1) % 5 == 0:
            log["results"] = results
            save_log(log)

        print()

    # Final save
    log["results"] = results
    log["summary"] = {
        "batch": f"{start}-{end}",
        "downloaded": downloaded,
        "found_only": found_only,
        "failed": failed,
        "not_found": not_found,
        "skipped": skipped,
        "total": len(batch),
    }
    save_log(log)

    print(f"{'='*70}")
    print(f"BATCH {start}-{end} SUMMARY")
    print(f"  Downloaded:   {downloaded}")
    print(f"  Found (dry):  {found_only}")
    print(f"  Failed DL:    {failed}")
    print(f"  Not found:    {not_found}")
    print(f"  Skipped:      {skipped}")
    print(f"  Total:        {len(batch)}")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
