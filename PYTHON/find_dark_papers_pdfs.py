#!/usr/bin/env python3
"""
Find, download, and extract PDFs for the 22 "dark" papers
(papers with neither local_pdf nor pdf_extract).

Strategy waterfall per paper:
  1. external_pdf field — direct download
  2. Source-specific OA patterns (MDPI, JMIR, PhilArchive, Duke Law, HF, INSS, ADL)
  3. Unpaywall API — DOI lookup
  4. arXiv title search
  5. Semantic Scholar title search
  6. OpenAlex DOI/title lookup

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/find_dark_papers_pdfs.py
    ../.venv/bin/python PYTHON/find_dark_papers_pdfs.py --dry-run
"""

import argparse
import json
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, Tuple

try:
    import fitz  # PyMuPDF
    HAS_FITZ = True
except ImportError:
    HAS_FITZ = False

# ─── Configuration ────────────────────────────────────────────────────────────

PAPERS_DIR = Path("papers")
EXTRACTS_DIR = Path("PDF Extracts")
VAULT_CONFIG = Path(".vault-config.json")

UNPAYWALL_EMAIL = "research@cei-literature.org"
CURL_TIMEOUT = 60
MAX_RETRIES = 2

RATE_LIMITS = {
    "arxiv": 3.0,
    "semantic_scholar": 10.0,
    "unpaywall": 1.0,
    "openalex": 1.0,
    "default": 1.5,
}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
    )
}

# ─── The 22 Dark Papers ───────────────────────────────────────────────────────

DARK_PAPERS = [
    # Group A — Direct arXiv
    {
        "file": "papers/2024-Wen-Yi-How Chinese are Chinese Language Models The Puzzling Lack of Language.md",
        "year": 2024,
        "title": "How Chinese are Chinese Language Models? The Puzzling Lack of Language Policy in China's LLMs",
        "url": "https://arxiv.org/abs/2407.09652",
        "doi": None,
        "external_pdf": "https://arxiv.org/pdf/2407.09652v1",
        "hf_url": None,
    },
    {
        "file": "papers/2025-Tenzer-Designing LLMs for Cultural Sensitivity Evidence from.md",
        "year": 2025,
        "title": "Designing LLMs for Cultural Sensitivity: Evidence from English-Japanese Translation",
        "url": "https://arxiv.org/abs/2509.11921",
        "doi": None,
        "external_pdf": "https://arxiv.org/pdf/2509.11921v1",
        "hf_url": None,
    },
    # Group B — Open Access journals
    {
        "file": "papers/2020-Carroll-The CARE Principles for Indigenous Data Governance.md",
        "year": 2020,
        "title": "The CARE Principles for Indigenous Data Governance",
        "url": "https://datascience.codata.org/articles/10.5334/dsj-2020-043",
        "doi": "10.5334/dsj-2020-043",
        "external_pdf": None,
        "hf_url": None,
    },
    {
        "file": "papers/2024-Lent-CreoleVal Multilingual Multitask Benchmarks for Creoles.md",
        "year": 2024,
        "title": "CreoleVal: Multilingual Multitask Benchmarks for Creoles",
        "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00682/124256/CreoleVal-Multilingual-Multitask-Benchmarks-for",
        "doi": "10.1162/tacl_a_00682",
        "external_pdf": "https://aclanthology.org/2024.tacl-1.54.pdf",  # verified in ACL Anthology
        "hf_url": None,
    },
    {
        "file": "papers/2025-Lee-Knowing the Words Missing the Meaning Evaluating LLMs' Cultural.md",
        "year": 2025,
        "title": "Knowing the Words, Missing the Meaning: Evaluating LLMs' Cultural Understanding Through Sino-Korean Words and Four-Character Idioms",
        "url": "https://www.mdpi.com/2076-3417/15/13/7561",
        "doi": "10.3390/app15137561",
        "external_pdf": None,
        "hf_url": None,
    },
    {
        "file": "papers/2024-Hadar-Shoval-Assessing the Alignment of Large Language Models With Human Values.md",
        "year": 2024,
        "title": "Assessing the Alignment of Large Language Models With Human Values for Mental Health Integration: Cross-Sectional Study Using Schwartz's Theory of Basic Values",
        "url": "https://mental.jmir.org/2024/1/e55988",
        "doi": "10.2196/55988",
        "external_pdf": None,
        "hf_url": None,
    },
    {
        "file": "papers/2024-Gaikwad-MoralBench A Multi-Faceted Benchmark for Ethical and Safety Alignment.md",
        "year": 2024,
        "title": "MoralBench: A Multi-Faceted Benchmark for Ethical and Safety Alignment in LLMs",
        "url": "https://philarchive.org/archive/GAIMAM",
        "doi": None,
        "external_pdf": None,
        "hf_url": None,
    },
    {
        "file": "papers/2024-Crepelle-Tribes and AI Possibilities for Tribal Sovereignty.md",
        "year": 2024,
        "title": "Tribes and AI: Possibilities for Tribal Sovereignty",
        "url": "https://scholarship.law.duke.edu/dltr/vol25/iss1/1/",
        "doi": None,
        "external_pdf": None,
        "hf_url": None,
    },
    # Group C — HuggingFace datasets
    {
        "file": "papers/2024-Nayak-CulturalVQA Evaluating VLMs' Geo-Diverse Cultural Understanding.md",
        "year": 2024,
        "title": "CulturalVQA: Evaluating VLMs' Geo-Diverse Cultural Understanding",
        "url": "https://huggingface.co/datasets/mair-lab/CulturalVQA",
        "doi": None,
        "external_pdf": None,
        "hf_url": "https://huggingface.co/datasets/mair-lab/CulturalVQA",
    },
    {
        "file": "papers/2024-Sagyndyk-Kazakh Dastur-MC Multiple Choice Benchmark.md",
        "year": 2024,
        "title": "Kazakh Dastur-MC: Multiple Choice Benchmark",
        "url": "https://huggingface.co/datasets/kz-transformers/kazakh-dastur-mc",
        "doi": None,
        "external_pdf": None,
        "hf_url": "https://huggingface.co/datasets/kz-transformers/kazakh-dastur-mc",
    },
    {
        "file": "papers/2024-Satar-Seeing Culture Benchmark Evaluating VLMs on Culturally Rich Images.md",
        "year": 2024,
        "title": "Seeing Culture Benchmark: Evaluating VLMs on Culturally Rich Images from Southeast Asia",
        "url": "https://huggingface.co/datasets/Multimedia-SMU/seeingculture-benchmark",
        "doi": None,
        "external_pdf": None,
        "hf_url": "https://huggingface.co/datasets/Multimedia-SMU/seeingculture-benchmark",
    },
    {
        "file": "papers/2024-Thu-MixCuBe When Tom Eats Kimchi - Evaluating Cultural Awareness of.md",
        "year": 2024,
        "title": "MixCuBe: When Tom Eats Kimchi - Evaluating Cultural Awareness of Multimodal Large Language Models in Cultural Mixture Contexts",
        "url": "https://huggingface.co/datasets/kyawyethu/MixCuBe",
        "doi": None,
        "external_pdf": None,
        "hf_url": "https://huggingface.co/datasets/kyawyethu/MixCuBe",
    },
    # Group D — Open institutional reports
    {
        "file": "papers/2020-Ema-Artificial Intelligence and Indigenous Perspectives Protecting and.md",
        "year": 2020,
        "title": "Artificial Intelligence and Indigenous Perspectives: Protecting and Empowering Intelligent Human Beings",
        "url": "https://dl.acm.org/doi/10.1145/3375627.3375845",
        "doi": "10.1145/3375627.3375845",
        "external_pdf": None,
        "hf_url": None,
    },
    {
        "file": "papers/2025-Gil-Does Israel Need a National Language Model.md",
        "year": 2025,
        "title": "Does Israel Need a National Language Model?",
        "url": "https://www.inss.org.il/publication/israel-ai/",
        "doi": None,
        "external_pdf": None,
        "hf_url": None,
    },
    {
        "file": "papers/2025-Society-Generating Hate Anti-Jewish and Anti-Israel Bias in Leading Large.md",
        "year": 2025,
        "title": "Generating Hate: Anti-Jewish and Anti-Israel Bias in Leading Large Language Models",
        "url": "https://www.adl.org/resources/report/generating-hate-anti-jewish-and-anti-israel-bias-leading-large-language-models",
        "doi": None,
        "external_pdf": None,
        "hf_url": None,
    },
    # Group E — Likely paywalled
    {
        "file": "papers/2024-Moshagen-Indigenous Language Technology in the Age of Machine Learning.md",
        "year": 2024,
        "title": "Indigenous Language Technology in the Age of Machine Learning",
        "url": "https://www.tandfonline.com/doi/full/10.1080/08003831.2024.2410124",
        "doi": "10.1080/08003831.2024.2410124",
        "external_pdf": None,
        "hf_url": None,
    },
    {
        "file": "papers/2024-Silano-Towards Abundant Intelligences Considerations for Indigenous.md",
        "year": 2024,
        "title": "Towards Abundant Intelligences: Considerations for Indigenous Perspectives in Adopting Artificial Intelligence Technology",
        "url": "https://journals.sagepub.com/doi/10.1177/08404704241257144",
        "doi": "10.1177/08404704241257144",
        "external_pdf": None,
        "hf_url": None,
    },
    {
        "file": "papers/2025-Jiang-Simulating social perception with large language models perceptions.md",
        "year": 2025,
        "title": "Simulating social perception with large language models: perceptions of China's common prosperity",
        "url": "https://www.tandfonline.com/doi/full/10.1080/23812346.2025.2603822",
        "doi": "10.1080/23812346.2025.2603822",
        "external_pdf": None,
        "hf_url": None,
    },
    {
        "file": "papers/2025-Rana-Indigenous Data Sovereignty A Catalyst for Ethical AI in Business.md",
        "year": 2025,
        "title": "Indigenous Data Sovereignty: A Catalyst for Ethical AI in Business",
        "url": "https://journals.sagepub.com/doi/full/10.1177/00076503241271143",
        "doi": "10.1177/00076503241271143",
        "external_pdf": None,
        "hf_url": None,
    },
    {
        "file": "papers/2025-Tran-Artificial intelligence ethics in authoritarian Vietnam governance.md",
        "year": 2025,
        "title": "Artificial intelligence ethics in authoritarian Vietnam: governance, trust, and societal tensions",
        "url": "https://www.tandfonline.com/doi/full/10.1080/25741292.2025.2529625",
        "doi": "10.1080/25741292.2025.2529625",
        "external_pdf": None,
        "hf_url": None,
    },
    {
        "file": "papers/2025-A.-Operationalizing Cultural Values in Language Models A Comparative.md",
        "year": 2025,
        "title": "Operationalizing Cultural Values in Language Models: A Comparative Analysis Using Hofstede's Dimensions",
        "url": "https://link.springer.com/chapter/10.1007/978-3-032-05545-3_10",
        "doi": "10.1007/978-3-032-05545-3_10",
        "external_pdf": "https://arxiv.org/pdf/2404.12464.pdf",  # preprint on arXiv
        "hf_url": None,
    },
    {
        "file": "papers/2025-Topal-How do LLMs perform on Turkish A multi-faceted multi-prompt evaluation.md",
        "year": 2025,
        "title": "How do LLMs perform on Turkish? A multi-faceted multi-prompt evaluation",
        "url": "https://www.sciencedirect.com/science/article/abs/pii/S0957417425010437",
        "doi": "10.1016/j.eswa.2025.127421",
        "external_pdf": None,
        "hf_url": None,
    },
]


# ─── Path helpers ─────────────────────────────────────────────────────────────

def get_pdfs_dir() -> Path:
    config = json.loads(VAULT_CONFIG.read_text())
    return Path(config["pdf_path"])


def pdf_name_from_paper_path(paper_file: str) -> str:
    """Derive PDF filename from paper .md path (same stem + .pdf)."""
    stem = Path(paper_file).stem
    return stem + ".pdf"


def make_pdf_wikilink(year: int, pdf_name: str) -> str:
    return f"[[Lit-WS-PDFs/{year}/{pdf_name}]]"


def make_extract_rel(year: int, extract_name: str) -> str:
    return f"PDF Extracts/{year}/{extract_name}"


# ─── Rate limiting ────────────────────────────────────────────────────────────

_last_request: Dict[str, float] = {}


def rate_limit(source: str):
    limit = RATE_LIMITS.get(source, RATE_LIMITS["default"])
    last = _last_request.get(source, 0)
    elapsed = time.time() - last
    if elapsed < limit:
        time.sleep(limit - elapsed)
    _last_request[source] = time.time()


# ─── HTTP helpers ─────────────────────────────────────────────────────────────

def http_get(url: str, source: str = "default", timeout: int = 30) -> Optional[bytes]:
    """GET a URL and return raw bytes, or None on error."""
    rate_limit(source)
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except Exception:
        return None


def http_get_json(url: str, source: str = "default") -> Optional[Dict]:
    """GET a URL and parse JSON response."""
    data = http_get(url, source)
    if data is None:
        return None
    try:
        return json.loads(data.decode("utf-8"))
    except Exception:
        return None


def http_get_text(url: str, source: str = "default") -> Optional[str]:
    """GET a URL and return text."""
    data = http_get(url, source)
    if data is None:
        return None
    try:
        return data.decode("utf-8", errors="replace")
    except Exception:
        return None


# ─── PDF download & validation ────────────────────────────────────────────────

def _curl_download(url: str, dest: Path, ua: str) -> str:
    """Run curl to download url → dest, return HTTP code string."""
    cmd = [
        "curl", "-sS", "-L",
        "-o", str(dest),
        "-w", "%{http_code}",
        "--max-time", str(CURL_TIMEOUT),
        "--connect-timeout", "15",
    ]
    if ua:
        cmd += ["-H", f"User-Agent: {ua}"]
    cmd.append(url)
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=CURL_TIMEOUT + 10)
    return result.stdout.strip()


def _check_pdf(dest: Path) -> tuple[bool, str]:
    """Validate downloaded file is a real PDF. Returns (ok, message)."""
    if not dest.exists():
        return False, "File not created"
    size = dest.stat().st_size
    if size < 1000:
        dest.unlink()
        return False, f"File too small ({size} bytes)"
    with open(dest, "rb") as fh:
        header = fh.read(5)
    if header == b"%PDF-":
        return True, f"OK ({size // 1024}KB)"
    dest.unlink()
    return False, "Not a valid PDF (HTML/error page?)"


def download_pdf(url: str, dest: Path, retries: int = MAX_RETRIES) -> tuple[bool, str]:
    """Download PDF via curl with %PDF- validation.

    Tries with browser User-Agent first, then without (handles BePress bot-blocking).
    Returns (success, message).
    """
    for ua in [HEADERS["User-Agent"], ""]:
        for attempt in range(retries + 1):
            try:
                http_code = _curl_download(url, dest, ua)

                if http_code in ("200", "202"):
                    ok, msg = _check_pdf(dest)
                    if ok:
                        return True, msg
                    elif "too small" in msg or "not created" in msg:
                        # Empty response — try without User-Agent
                        break  # inner loop, go to next UA variant
                    else:
                        return False, msg

                elif http_code == "429":
                    if attempt < retries:
                        wait = 15 * (attempt + 1)
                        print(f"      Rate limited — waiting {wait}s...")
                        time.sleep(wait)
                        continue
                    # Fall through to try next UA variant
                    break

                else:
                    if dest.exists():
                        dest.unlink()
                    if attempt < retries and http_code in ("500", "503"):
                        time.sleep(5)
                        continue
                    break  # Try next UA variant for non-retryable errors

            except subprocess.TimeoutExpired:
                if attempt < retries:
                    time.sleep(5)
                    continue
                break
            except Exception as exc:
                return False, str(exc)

    return False, f"HTTP {http_code}" if 'http_code' in dir() else "Failed"


# ─── Text extraction ──────────────────────────────────────────────────────────

def extract_pdf_text(pdf_path: Path, extract_path: Path) -> int:
    """Extract text from PDF with PyMuPDF. Returns page count."""
    if not HAS_FITZ:
        raise ImportError("PyMuPDF (fitz) is not installed")

    doc = fitz.open(pdf_path)
    num_pages = len(doc)
    page_texts = []
    for i in range(num_pages):
        text = doc[i].get_text()
        page_texts.append(f"--- Page {i + 1} ---\n\n{text}")
    doc.close()

    title = extract_path.stem
    now = datetime.now().isoformat()
    content = f"""---
title: "{title} - PDF Extract"
source_pdf: "{pdf_path.name}"
pages: {num_pages}
extracted_at: "{now}"
extractor: PyMuPDF
---

# PDF Extract: {title}

**Source PDF:** {pdf_path.name}
**Total Pages:** {num_pages}

---

## Content

```
{chr(10).join(page_texts)}
```
"""
    extract_path.parent.mkdir(parents=True, exist_ok=True)
    extract_path.write_text(content, encoding="utf-8")
    return num_pages


# ─── YAML updates (regex only — never parse/rebuild) ──────────────────────────

def update_paper_yaml(paper_path: Path, pdf_wikilink: str, extract_rel: str) -> bool:
    """Update local_pdf and insert pdf_extract in paper frontmatter."""
    content = paper_path.read_text(encoding="utf-8")

    # Replace the 2-line "local_pdf:\n\"N/A\"\n" pattern (or "local_pdf: \n\"N/A\"\n")
    new_local_pdf_line = f'local_pdf: "{pdf_wikilink}"'

    # Pattern: local_pdf: (with optional trailing space/value) then newline, then optional "N/A" line
    content, n1 = re.subn(
        r'^(local_pdf:.*)\n"N/A"\n',
        new_local_pdf_line + "\n",
        content, count=1, flags=re.MULTILINE
    )
    if n1 == 0:
        # Fallback: local_pdf: with value on same line
        content, n1 = re.subn(
            r'^local_pdf:.*$',
            new_local_pdf_line,
            content, count=1, flags=re.MULTILINE
        )

    if n1 == 0:
        print(f"      WARNING: Could not update local_pdf in {paper_path.name}")
        return False

    # Insert pdf_extract after local_pdf line
    extract_line = f'pdf_extract: "{extract_rel}"'
    if "pdf_extract:" in content:
        # Replace existing
        content, _ = re.subn(
            r'^pdf_extract:.*$',
            extract_line,
            content, count=1, flags=re.MULTILINE
        )
    else:
        # Insert after local_pdf
        content = re.sub(
            r'^(local_pdf:.*$)',
            rf'\1\n{extract_line}',
            content, count=1, flags=re.MULTILINE
        )

    paper_path.write_text(content, encoding="utf-8")
    return True


# ─── Title matching ───────────────────────────────────────────────────────────

def titles_match(t1: str, t2: str, threshold: float = 0.7) -> bool:
    """Fuzzy title match: word overlap ratio."""
    def words(s):
        return set(re.sub(r'[^\w\s]', '', s.lower()).split())
    w1, w2 = words(t1), words(t2)
    if not w1 or not w2:
        return False
    overlap = len(w1 & w2) / max(len(w1), len(w2))
    return overlap >= threshold


# ─── Acquisition strategies ───────────────────────────────────────────────────

def strategy_direct_external_pdf(paper: dict) -> Optional[str]:
    """S1: Use external_pdf field directly."""
    ep = paper.get("external_pdf")
    if ep and ep.startswith("http"):
        return ep
    return None


def strategy_mdpi(paper: dict) -> Optional[str]:
    """S2a: MDPI URLs → append /pdf."""
    url = paper.get("url", "")
    if "mdpi.com" in url:
        return url.rstrip("/") + "/pdf"
    return None


def strategy_jmir(paper: dict) -> Optional[str]:
    """S2b: JMIR URLs → append /PDF."""
    url = paper.get("url", "")
    if "jmir.org" in url:
        return url.rstrip("/") + "/PDF"
    return None


def strategy_scrape_page(paper: dict) -> Optional[str]:
    """S2c: Scrape paper URL for a PDF link.

    Handles: PhilArchive, Duke Law Review, INSS, ADL reports.
    Also handles HuggingFace dataset pages (finds arXiv paper link → PDF).
    """
    import html as html_module
    from urllib.parse import urlparse

    url = paper.get("url", "")
    if not url:
        return None

    # HuggingFace: search for arXiv paper link then follow to PDF
    if "huggingface.co" in url:
        return _scrape_huggingface(url, paper)

    # Generic: look for PDF links on the page
    html = http_get_text(url, "default")
    if not html:
        return None

    parsed_url = urlparse(url)
    page_domain = parsed_url.netloc  # e.g. "www.adl.org"

    def make_absolute(href: str) -> str:
        href = html_module.unescape(href)  # decode &amp; → & etc.
        if href.startswith("http"):
            return href
        elif href.startswith("/"):
            return f"{parsed_url.scheme}://{parsed_url.netloc}{href}"
        return href

    # Collect all PDF-like links (direct .pdf links AND BePress viewcontent.cgi)
    pdf_candidates = []

    for link in re.findall(r'href=["\']([^"\']*\.pdf)["\']', html, re.IGNORECASE):
        pdf_candidates.append(make_absolute(link))

    # BePress institutional repository pattern (no .pdf extension but delivers PDF)
    for link in re.findall(r'href=["\']([^"\']*cgi/viewcontent\.cgi[^"\']*)["\']', html):
        pdf_candidates.append(make_absolute(link))

    if not pdf_candidates:
        # Note: intentionally NOT searching for arXiv IDs on the page — institutional
        # report pages cite arXiv papers that are unrelated to the target document.
        # arXiv discovery is handled by S4-arxiv via title search.
        return None

    # Prefer same-domain links to avoid picking up unrelated external PDFs
    same_domain = [c for c in pdf_candidates if page_domain in c]
    return same_domain[0] if same_domain else None


def _scrape_huggingface(hf_url: str, paper: dict) -> Optional[str]:
    """Scrape HuggingFace dataset page for arXiv paper link → return PDF URL."""
    html = http_get_text(hf_url, "default")
    if not html:
        return None

    # Look for arXiv abs links
    arxiv_abs = re.findall(r'arxiv\.org/abs/(\d{4}\.\d{4,5})', html)
    if arxiv_abs:
        arxiv_id = arxiv_abs[0]
        return f"https://arxiv.org/pdf/{arxiv_id}.pdf"

    # Look for direct PDF links
    pdf_links = re.findall(r'href=["\']([^"\']*\.pdf)["\']', html, re.IGNORECASE)
    for link in pdf_links:
        if link.startswith("http"):
            return link

    # Try arXiv title search as fallback
    return strategy_arxiv_title(paper)


def strategy_unpaywall(paper: dict) -> Optional[str]:
    """S3: Unpaywall API via DOI."""
    doi = paper.get("doi")
    if not doi:
        return None
    encoded = urllib.parse.quote(doi, safe="")
    url = f"https://api.unpaywall.org/v2/{encoded}?email={UNPAYWALL_EMAIL}"
    data = http_get_json(url, "unpaywall")
    if not data:
        return None
    if data.get("is_oa") and data.get("oa_locations"):
        for loc in data["oa_locations"]:
            pdf_url = loc.get("url_for_pdf") or loc.get("pdf_url")
            if pdf_url:
                return pdf_url
    return None


def strategy_arxiv_title(paper: dict) -> Optional[str]:
    """S4: arXiv title search."""
    title = paper.get("title", "")
    if not title:
        return None
    search_title = title.split("(")[0].split(" -- ")[0].strip()[:120]
    query = urllib.parse.quote(f'ti:"{search_title}"')
    url = f"http://export.arxiv.org/api/query?search_query={query}&start=0&max_results=3&sortBy=relevance"

    rate_limit("arxiv")
    data = http_get(url, "arxiv")
    if not data:
        return None

    try:
        root = ET.fromstring(data)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        for entry in root.findall("atom:entry", ns):
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


def strategy_semantic_scholar(paper: dict) -> Optional[str]:
    """S5: Semantic Scholar open access PDF search."""
    title = paper.get("title", "")
    doi = paper.get("doi")

    # Try by DOI first (more precise)
    if doi:
        encoded_doi = urllib.parse.quote(doi, safe="")
        url = (
            f"https://api.semanticscholar.org/graph/v1/paper/DOI:{encoded_doi}"
            f"?fields=title,openAccessPdf,externalIds"
        )
        data = http_get_json(url, "semantic_scholar")
        if data:
            oa_pdf = data.get("openAccessPdf")
            if oa_pdf and oa_pdf.get("url"):
                return oa_pdf["url"]

    # Try by title
    if not title:
        return None
    query = urllib.parse.quote(title[:200])
    url = (
        f"https://api.semanticscholar.org/graph/v1/paper/search"
        f"?query={query}&fields=title,openAccessPdf,externalIds&limit=3"
    )
    data = http_get_json(url, "semantic_scholar")
    if not data or not data.get("data"):
        return None

    for item in data["data"][:3]:
        item_title = item.get("title", "")
        if titles_match(title, item_title):
            oa_pdf = item.get("openAccessPdf")
            if oa_pdf and oa_pdf.get("url"):
                return oa_pdf["url"]
            ext_ids = item.get("externalIds", {})
            arxiv_id = ext_ids.get("ArXiv")
            if arxiv_id:
                return f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    return None


def strategy_openalex(paper: dict) -> Optional[str]:
    """S6: OpenAlex DOI/title lookup for OA PDF."""
    doi = paper.get("doi")
    title = paper.get("title", "")

    # Try DOI lookup
    if doi:
        encoded = urllib.parse.quote(doi, safe="")
        url = f"https://api.openalex.org/works/doi:{encoded}?select=id,display_name,open_access,locations"
        data = http_get_json(url, "openalex")
        if data:
            pdf_url = _openalex_extract_pdf(data)
            if pdf_url:
                return pdf_url

    # Try title search
    if not title:
        return None
    search_title = title[:150]
    url = (
        f"https://api.openalex.org/works?search={urllib.parse.quote(search_title)}"
        f"&select=id,display_name,open_access,locations&per-page=5"
    )
    data = http_get_json(url, "openalex")
    if not data or not data.get("results"):
        return None

    for item in data["results"][:3]:
        item_title = item.get("display_name") or item.get("title") or ""
        if titles_match(title, item_title):
            pdf_url = _openalex_extract_pdf(item)
            if pdf_url:
                return pdf_url
    return None


def _openalex_extract_pdf(data: dict) -> Optional[str]:
    """Extract OA PDF URL from an OpenAlex work record."""
    # Check locations first (more specific pdf_url)
    for loc in data.get("locations", []):
        if loc.get("is_oa") and loc.get("pdf_url"):
            return loc["pdf_url"]

    # Fall back to open_access oa_url (may be a landing page, not direct PDF)
    oa = data.get("open_access", {})
    if oa.get("oa_url"):
        candidate = oa["oa_url"]
        # Only return if it looks like a direct PDF
        if candidate.endswith(".pdf") or "arxiv.org/pdf" in candidate or "/pdf" in candidate:
            return candidate

    return None


# ─── Main strategy waterfall ──────────────────────────────────────────────────

STRATEGIES = [
    ("S1-external_pdf", strategy_direct_external_pdf),
    ("S2-mdpi",         strategy_mdpi),
    ("S2-jmir",         strategy_jmir),
    ("S2-scrape",       strategy_scrape_page),
    ("S3-unpaywall",    strategy_unpaywall),
    ("S4-arxiv",        strategy_arxiv_title),
    ("S5-semscholar",   strategy_semantic_scholar),
    ("S6-openalex",     strategy_openalex),
]


def find_pdf_url(paper: dict) -> Tuple[Optional[str], str]:
    """Try each strategy in order. Returns (url, strategy_name)."""
    for name, fn in STRATEGIES:
        try:
            url = fn(paper)
        except Exception as exc:
            print(f"      {name}: ERROR — {exc}")
            url = None
        if url:
            return url, name
    return None, "none"


# ─── Process a single paper ───────────────────────────────────────────────────

def process_paper(paper: dict, pdfs_dir: Path, dry_run: bool) -> Dict:
    """Attempt to acquire PDF + extract for one paper. Returns result dict."""
    file_path = Path(paper["file"])
    year = paper["year"]
    pdf_name = pdf_name_from_paper_path(paper["file"])
    extract_name = Path(paper["file"]).stem + ".md"

    pdf_dest = pdfs_dir / str(year) / pdf_name
    extract_dest = EXTRACTS_DIR / str(year) / extract_name

    print(f"\n  {file_path.name}")

    # Find PDF URL
    pdf_url, strategy = find_pdf_url(paper)

    if not pdf_url:
        print(f"    ✗ No PDF URL found after all strategies")
        return {"paper": paper["file"], "success": False, "reason": "No PDF URL found"}

    print(f"    → {strategy}: {pdf_url[:80]}{'...' if len(pdf_url) > 80 else ''}")

    if dry_run:
        print(f"    [DRY RUN] Would download to {pdf_dest}")
        return {"paper": paper["file"], "success": True, "dry_run": True, "strategy": strategy}

    # Download PDF
    pdf_dest.parent.mkdir(parents=True, exist_ok=True)
    ok, msg = download_pdf(pdf_url, pdf_dest)
    if not ok:
        print(f"    ✗ Download failed: {msg}")
        return {"paper": paper["file"], "success": False, "reason": f"Download: {msg}", "strategy": strategy}

    print(f"    ✓ Downloaded: {msg}")

    # Extract text
    if not HAS_FITZ:
        print(f"    ✗ PyMuPDF not available — skipping extraction")
        return {"paper": paper["file"], "success": False, "reason": "fitz not installed", "strategy": strategy}

    try:
        pages = extract_pdf_text(pdf_dest, extract_dest)
        print(f"    ✓ Extracted: {pages} pages → {extract_dest}")
    except Exception as exc:
        print(f"    ✗ Extraction failed: {exc}")
        return {"paper": paper["file"], "success": False, "reason": f"Extract: {exc}", "strategy": strategy}

    # Update paper YAML
    wikilink = make_pdf_wikilink(year, pdf_name)
    extract_rel = make_extract_rel(year, extract_name)
    try:
        ok = update_paper_yaml(file_path, wikilink, extract_rel)
        if ok:
            print(f"    ✓ YAML updated: local_pdf + pdf_extract")
        else:
            print(f"    ✗ YAML update failed")
            return {"paper": paper["file"], "success": False, "reason": "YAML update failed", "strategy": strategy}
    except Exception as exc:
        print(f"    ✗ YAML update error: {exc}")
        return {"paper": paper["file"], "success": False, "reason": f"YAML: {exc}", "strategy": strategy}

    return {
        "paper": paper["file"],
        "success": True,
        "strategy": strategy,
        "pdf": str(pdf_dest),
        "extract": str(extract_dest),
        "pages": pages,
    }


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Find PDFs for 22 dark papers")
    parser.add_argument("--dry-run", action="store_true", help="Find URLs only, don't download")
    parser.add_argument("--only", type=str, default=None, help="Process only papers whose filename contains this string")
    args = parser.parse_args()

    if not VAULT_CONFIG.exists():
        print("ERROR: .vault-config.json not found. Run from CEI-Lit-WS/.")
        sys.exit(1)

    if not HAS_FITZ and not args.dry_run:
        print("WARNING: PyMuPDF (fitz) not installed — extraction will fail.")
        print("Install with: pip install PyMuPDF")

    pdfs_dir = get_pdfs_dir()
    print(f"PDFs directory: {pdfs_dir}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    print(f"Processing {len(DARK_PAPERS)} dark papers...\n")

    papers_to_process = DARK_PAPERS
    if args.only:
        papers_to_process = [p for p in DARK_PAPERS if args.only.lower() in p["file"].lower()]
        print(f"Filtered to {len(papers_to_process)} papers matching '{args.only}'")

    results = []
    for paper in papers_to_process:
        result = process_paper(paper, pdfs_dir, args.dry_run)
        results.append(result)

    # Summary
    successes = [r for r in results if r["success"]]
    failures = [r for r in results if not r["success"]]

    print("\n" + "=" * 70)
    print(f"SUMMARY: {len(successes)}/{len(results)} papers acquired")
    print("=" * 70)

    if successes:
        print(f"\nSuccessful ({len(successes)}):")
        for r in successes:
            dry = " [DRY RUN]" if r.get("dry_run") else ""
            strat = r.get("strategy", "?")
            pages = f" ({r['pages']}p)" if "pages" in r else ""
            print(f"  ✓ {Path(r['paper']).name[:70]}{pages} via {strat}{dry}")

    if failures:
        print(f"\nFailed ({len(failures)}):")
        for r in failures:
            reason = r.get("reason", "unknown")
            strat = r.get("strategy", "none tried")
            print(f"  ✗ {Path(r['paper']).name[:70]}")
            print(f"      reason: {reason}")

    print("\nDone.")
    if not args.dry_run and successes:
        print("\nNext step: run validate_all_papers.py to verify YAML integrity.")


if __name__ == "__main__":
    main()
