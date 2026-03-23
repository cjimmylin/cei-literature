#!/usr/bin/env python3
"""
Advanced PDF Finder — Targeted Multi-Strategy Acquisition for 19 Missing Papers

Goes beyond the 13 strategies in comprehensive_pdf_finder.py with:
  Phase 1: Direct downloads from confirmed/researched URLs (9 papers)
  Phase 2: Creative API strategies not in the original waterfall (5 papers)
  Phase 3: Manual research report for books/hard paywall (5 papers)

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/advanced_pdf_finder.py              # Full run
    ../.venv/bin/python PYTHON/advanced_pdf_finder.py --dry-run    # Discovery only
    ../.venv/bin/python PYTHON/advanced_pdf_finder.py --phase 1    # Phase 1 only
    ../.venv/bin/python PYTHON/advanced_pdf_finder.py --phase 2    # Phase 2 only
    ../.venv/bin/python PYTHON/advanced_pdf_finder.py --phase 3    # Phase 3 only
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

# Force flush for monitoring
print = functools.partial(print, flush=True)

# ═══════════════════════════════════════════════════════════════════════════════
# Configuration
# ═══════════════════════════════════════════════════════════════════════════════

PAPERS_DIR = Path("papers")
VAULT_CONFIG = Path(".vault-config.json")
LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "20260208-advanced_pdf_finder_log.json"
REPORT_FILE = LOG_DIR / "20260208-manual_pdf_research_report.md"
CURL_TIMEOUT = 60
MAX_RETRIES = 2
UNPAYWALL_EMAIL = "research@cei-literature.org"

HEADERS = {
    "User-Agent": "CEI-Literature-Vault/2.0 (Academic Research; mailto:research@cei-literature.org)"
}

# Rate limits (seconds between requests per source)
RATE_LIMITS = {
    "unpaywall": 1.0,
    "acl": 1.0,
    "semantic_scholar": 4.0,
    "arxiv": 3.0,
    "openalex": 0.1,
    "crossref": 0.02,
    "europepmc": 1.0,
    "pubmed": 0.5,
    "researchgate": 3.0,
    "acm_dl": 2.0,
    "google_scholar": 5.0,
    "institutional": 2.0,
    "aaai": 2.0,
    "doi_scrape": 1.0,
    "download": 1.0,
    "general": 1.0,
}


# ═══════════════════════════════════════════════════════════════════════════════
# The 19 Target Papers — exact filenames and metadata
# ═══════════════════════════════════════════════════════════════════════════════

PHASE1_PAPERS = [
    {
        "id": 1,
        "filename": "2025-Bryan-Virtue Ethics and Postponing Human Extinction.md",
        "title": "Virtue Ethics and Postponing Human Extinction",
        "doi": "10.1001/amajethics.2025.611",
        "url": "https://journalofethics.ama-assn.org/article/virtue-ethics-and-postponing-human-extinction/2025-08",
        "strategy": "ama_joe_oa",
        "notes": "AMA Journal of Ethics is 100% OA but Cloudflare-blocked. Try PubMed/EuropePMC.",
    },
    {
        "id": 2,
        "filename": "2025-Wilders-The Socratic Dialogue as a Method for Virtue Ethics in AI.md",
        "title": "The Socratic Dialogue as a Method for Virtue Ethics in AI",
        "doi": None,
        "url": "https://aies-conference.com/2025/",
        "strategy": "acl_anthology_direct",
        "direct_pdf": "https://ojs.aaai.org/index.php/AIES/article/download/36748/38886/40823",
        "notes": "AAAI/AIES 2025 — verified direct OJS download link",
    },
    {
        "id": 3,
        "filename": "2025-Authors-IslamicEval 2025 - Shared Task on Capturing LLM Hallucination in.md",
        "title": "IslamicEval 2025 -- Shared Task on Capturing LLM Hallucination in Islamic Content",
        "doi": None,
        "url": None,
        "strategy": "acl_anthology_direct",
        "direct_pdf": "https://aclanthology.org/2025.arabicnlp-sharedtasks.67.pdf",
        "notes": "ArabicNLP 2025 shared task — ACL Anthology 2025.arabicnlp-sharedtasks.67",
    },
    {
        "id": 4,
        "filename": "2025-Authors-QIAS 2025 - Shared Task on Islamic Inheritance Reasoning and.md",
        "title": "QIAS 2025 -- Shared Task on Islamic Inheritance Reasoning and Knowledge Assessment",
        "doi": None,
        "url": None,
        "strategy": "acl_anthology_direct",
        "direct_pdf": "https://aclanthology.org/2025.arabicnlp-sharedtasks.117.pdf",
        "notes": "ArabicNLP 2025 shared task — ACL Anthology 2025.arabicnlp-sharedtasks.117",
    },
    {
        "id": 5,
        "filename": "2025-Authors-Saudi-Alignment Benchmark - Assessing LLMs Alignment with Saudi.md",
        "title": "Saudi-Alignment Benchmark -- Assessing LLMs Alignment with Saudi Cultural and Ethical Norms",
        "doi": None,
        "url": None,
        "strategy": "acl_anthology_direct",
        "direct_pdf": "https://aclanthology.org/2025.arabicnlp-main.11.pdf",
        "notes": "ArabicNLP 2025 main conference — ACL Anthology 2025.arabicnlp-main.11",
    },
    {
        "id": 6,
        "filename": "2025-Nay-Aligning AI Agents with Humans through Law as Information.md",
        "title": "Aligning AI Agents with Humans through Law as Information",
        "doi": None,
        "url": "https://law.stanford.edu/publications/aligning-ai-agents-with-humans-through-law-as-information/",
        "strategy": "stanford_codex",
        "notes": "Stanford CodeX whitepaper — extract PDF from publication page",
    },
    {
        "id": 7,
        "filename": "2025-Sullins-Automated Ethical Practical Reasoning.md",
        "title": "Automated Ethical Practical Reasoning",
        "doi": None,
        "url": "https://mitpress.mit.edu/9780262549721/robophilosophy/",
        "strategy": "author_search",
        "notes": "Book chapter in Robophilosophy (MIT Press) — check author pages, Academia.edu",
    },
    {
        "id": 8,
        "filename": "2019-Kreutz-GermEval 2019 Task 2.md",
        "title": "GermEval 2019 Task 2",
        "doi": None,
        "url": "https://germevalmp2023.github.io/data/",
        "strategy": "konvens_proceedings",
        "notes": "KONVENS 2019 / GermEval proceedings — search for proceedings PDF",
    },
    {
        "id": 9,
        "filename": "2025-Unknown-Awesome-LLM-Eval Repository Meta-Resource.md",
        "title": "Awesome-LLM-Eval Repository (Meta-Resource)",
        "doi": None,
        "url": None,
        "strategy": "no_pdf_applicable",
        "notes": "GitHub repository, not a paper — mark as no_pdf_applicable",
    },
]

PHASE2_PAPERS = [
    {
        "id": 10,
        "filename": "2024-Jörs-Through Eudaimonia's Lenses.md",
        "title": "Through Eudaimonia's Lenses: EudAImonic Well-Being Variables As Guiding Principles For AI Design",
        "doi": None,
        "url": "https://www.researchgate.net/publication/380938771_Through_Eudaimonia's_Lenses_EudAImonic_Well-Being_Variables_As_Guiding_Principles_For_AI_Design",
        "first_author": "Julian Marvin Jörs",
        "institution": "FH Potsdam",
        "strategies": ["researchgate", "semantic_scholar", "google_scholar_pdf", "institutional_repo"],
    },
    {
        "id": 11,
        "filename": "2025-Muntean-Moral Coherentism Theoretical Framework Muntean.md",
        "title": "Moral Coherentism: Theoretical Framework",
        "doi": None,
        "url": None,
        "first_author": "I. Muntean",
        "institution": "UTRGV",
        "strategies": ["semantic_scholar", "philpapers", "google_scholar_pdf", "institutional_repo"],
    },
    {
        "id": 12,
        "filename": "2025-Ebara-Corpus-Based Medical Ethics Decision-Making Evaluation.md",
        "title": "Corpus-Based Medical Ethics Decision-Making Evaluation",
        "doi": "10.3233/SHTI250854",
        "url": "https://doi.org/10.3233/SHTI250854",
        "first_author": "Memi Ebara",
        "institution": None,
        "strategies": ["europepmc", "pubmed_central", "unpaywall", "doi_scrape_enhanced"],
    },
    {
        "id": 13,
        "filename": "2025-Gao-MIST Moral Inference through Storytelling with Text and Images.md",
        "title": "MIST: Moral Inference through Storytelling with Text and Images",
        "doi": "10.1145/3746252.3760884",
        "url": "https://doi.org/10.1145/3746252.3760884",
        "first_author": "C. Gao",
        "institution": "Tsinghua",
        "strategies": ["acm_dl_direct", "semantic_scholar", "arxiv_title", "google_scholar_pdf"],
    },
    {
        "id": 14,
        "filename": "2024-Muyskens-Can an AI-carebot be filial.md",
        "title": "Can an AI-carebot be filial? Reflections from Confucian ethics",
        "doi": "10.1177/09697330241238332",
        "url": "https://journals.sagepub.com/doi/10.1177/09697330241238332",
        "first_author": "Kathryn Muyskens",
        "institution": "NTU",
        "strategies": ["europepmc", "pubmed_central", "unpaywall", "semantic_scholar"],
    },
]

PHASE3_PAPERS = [
    {
        "id": 15,
        "filename": "2025-Sameer-Insights into Moral Reasoning of AI.md",
        "title": "Insights into Moral Reasoning of AI: A Comparative Study",
        "doi": "10.1080/23736992.2025.2553146",
        "url": "https://doi.org/10.1080/23736992.2025.2553146",
        "type": "journalArticle",
        "publisher": "Taylor & Francis",
        "first_author": "Ahmed Sameer",
        "isbn": None,
        "notes": "Journal of Media Ethics — paywalled T&F journal",
    },
    {
        "id": 16,
        "filename": "2025-Elder-The Ethics of Digital Ghosts.md",
        "title": "The Ethics of Digital Ghosts",
        "doi": "10.4324/9781003632658",
        "url": "https://www.taylorfrancis.com/books/mono/10.4324/9781003632658/ethics-digital-ghosts-alexis-elder",
        "type": "book",
        "publisher": "Routledge",
        "first_author": "Alexis M. Elder",
        "isbn": "9781041058410",
        "notes": "Commercial book ($48)",
    },
    {
        "id": 17,
        "filename": "2025-Hähnel-A Companion to Applied Philosophy of AI.md",
        "title": "A Companion to Applied Philosophy of AI",
        "doi": "10.1002/9781119809449",
        "url": "https://www.wiley.com/en-us/A+Companion+to+Applied+Philosophy+of+AI-p-9781119809",
        "type": "book",
        "publisher": "Wiley",
        "first_author": "Martin Hähnel",
        "isbn": None,
        "notes": "Commercial book ($195)",
    },
    {
        "id": 18,
        "filename": "2024-Vallor-The AI Mirror.md",
        "title": "The AI Mirror: How to Reclaim Our Humanity in an Age of Machine Thinking",
        "doi": "10.1093/oso/9780197759080.001.0001",
        "url": "https://global.oup.com/academic/product/the-ai-mirror-9780197759066",
        "type": "book",
        "publisher": "Oxford University Press",
        "first_author": "Shannon Vallor",
        "isbn": "9780197759066",
        "notes": "Commercial book ($30)",
    },
    {
        "id": 19,
        "filename": "2025-Rourke-Mind Crime.md",
        "title": "Mind Crime: The Moral Frontier of Artificial Intelligence",
        "doi": None,
        "url": "https://www.goodreads.com/book/show/226055728-mind-crime",
        "type": "book",
        "publisher": "Self-published",
        "first_author": "Nathan Rourke",
        "isbn": None,
        "notes": "Self-published (Goodreads only)",
    },
]


# ═══════════════════════════════════════════════════════════════════════════════
# Helpers (reused from comprehensive_pdf_finder.py)
# ═══════════════════════════════════════════════════════════════════════════════


def get_pdfs_dir() -> Path:
    """Get PDF storage directory from vault config."""
    config = json.loads(VAULT_CONFIG.read_text())
    return Path(config["pdf_path"])


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


def api_get(url: str, source: str, timeout: int = 15) -> Optional[dict]:
    """Make a rate-limited GET request and return parsed JSON, or None."""
    _rate_limit(source)
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        return None


def api_get_html(url: str, source: str, timeout: int = 15) -> Optional[str]:
    """Make a rate-limited GET request and return raw HTML, or None."""
    _rate_limit(source)
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="ignore")
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
    if n1 == n2:
        return True
    if n1 in n2 or n2 in n1:
        return True
    words1 = set(n1.split())
    words2 = set(n2.split())
    if not words1 or not words2:
        return False
    shorter = min(words1, words2, key=len)
    longer = max(words1, words2, key=len)
    overlap = len(shorter & longer) / len(shorter)
    return overlap >= 0.80


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


def download_pdf_browser(url: str, output_path: Path, retries: int = MAX_RETRIES) -> Tuple[bool, str]:
    """Download a PDF using curl with browser-like headers (bypasses some WAFs)."""
    for attempt in range(retries + 1):
        try:
            result = subprocess.run(
                [
                    "curl", "-sS", "-L",
                    "-o", str(output_path),
                    "-w", "%{http_code}",
                    "--max-time", str(CURL_TIMEOUT),
                    "--connect-timeout", "15",
                    "-H", "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
                    "-H", "Accept: application/pdf,text/html,application/xhtml+xml",
                    "-H", "Accept-Language: en-US,en;q=0.9",
                    "-H", f"Referer: {url.split('/')[0]}//{url.split('/')[2]}/",
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
                    time.sleep(10 * (attempt + 1))
                    continue
                return False, f"HTTP 429 after {retries} retries"
            else:
                if output_path.exists():
                    output_path.unlink()
                if attempt < retries:
                    time.sleep(3)
                    continue
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
# Safe YAML Updates (regex insertion — NEVER parse/rebuild)
# ═══════════════════════════════════════════════════════════════════════════════


def safe_update_external_pdf(paper_path: Path, pdf_url: str):
    """Add or update external_pdf field using safe regex insertion."""
    content = paper_path.read_text(encoding="utf-8")
    safe_url = pdf_url.replace('"', "'")
    new_line = f'external_pdf: "{safe_url}"'

    if "external_pdf:" in content:
        content = re.sub(
            r'^external_pdf:.*$', new_line, content, count=1, flags=re.MULTILINE,
        )
    elif "url:" in content:
        content = re.sub(
            r'(url:\s*"[^"]*"\n)', r'\1' + new_line + '\n', content, count=1,
        )
    else:
        content = content.replace("DATE_ADDED:", new_line + "\nDATE_ADDED:")

    paper_path.write_text(content, encoding="utf-8")


def safe_update_local_pdf(paper_path: Path, pdf_filename: str):
    """Add or update local_pdf field using safe regex insertion."""
    content = paper_path.read_text(encoding="utf-8")
    new_line = f'local_pdf: "[[Lit-WS-PDFs/{pdf_filename}]]"'

    if re.search(r'^local_pdf:\s*$', content, re.MULTILINE):
        content = re.sub(
            r'^local_pdf:\s*$', new_line, content, count=1, flags=re.MULTILINE,
        )
    elif "local_pdf:" in content:
        content = re.sub(
            r'^local_pdf:.*$', new_line, content, count=1, flags=re.MULTILINE,
        )
    elif "external_pdf:" in content:
        content = re.sub(
            r'(external_pdf:.*\n)', r'\1' + new_line + '\n', content, count=1,
        )
    elif "url:" in content:
        content = re.sub(
            r'(url:\s*"[^"]*"\n)', r'\1' + new_line + '\n', content, count=1,
        )
    else:
        content = content.replace("DATE_ADDED:", new_line + "\nDATE_ADDED:")

    paper_path.write_text(content, encoding="utf-8")


def safe_add_yaml_field(paper_path: Path, field_name: str, field_value: str):
    """Add a new YAML field before the closing --- using safe regex insertion."""
    content = paper_path.read_text(encoding="utf-8")
    safe_val = field_value.replace('"', "'")

    if f"{field_name}:" in content:
        # Replace existing
        content = re.sub(
            rf'^{re.escape(field_name)}:.*$',
            f'{field_name}: "{safe_val}"',
            content,
            count=1,
            flags=re.MULTILINE,
        )
    else:
        # Insert before the closing ---
        # Find the second --- which closes the frontmatter
        parts = content.split("---", 2)
        if len(parts) >= 3:
            parts[1] = parts[1].rstrip("\n") + f'\n{field_name}: "{safe_val}"\n'
            content = "---".join(parts)

    paper_path.write_text(content, encoding="utf-8")


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 2: New Strategy Functions
# ═══════════════════════════════════════════════════════════════════════════════


def strategy_europepmc(doi: str) -> Optional[str]:
    """EuropePMC — broader OA coverage than PMC. Returns PDF URL or None."""
    if not doi:
        return None
    encoded = urllib.parse.quote(doi, safe="")
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:{encoded}&format=json&resultType=core"
    data = api_get(url, "europepmc")
    if not data:
        return None

    results = data.get("resultList", {}).get("result", [])
    for r in results:
        # Check fullTextUrlList
        ft_urls = r.get("fullTextUrlList", {}).get("fullTextUrl", [])
        for ft in ft_urls:
            if ft.get("documentStyle") == "pdf" and ft.get("availability") == "Open access":
                return ft.get("url")
        # Check pmcid for PMC PDF
        pmcid = r.get("pmcid")
        if pmcid:
            return f"https://europepmc.org/backend/ptpmcrender.fcgi?accid={pmcid}&blobtype=pdf"
    return None


def strategy_pubmed_central(doi: str) -> Optional[str]:
    """Query NCBI E-utilities for PMC free full text PDF."""
    if not doi:
        return None

    # First: convert DOI to PMCID via ID converter
    encoded = urllib.parse.quote(doi, safe="")
    url = f"https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids={encoded}&format=json"
    data = api_get(url, "pubmed")
    if not data:
        return None

    records = data.get("records", [])
    for rec in records:
        pmcid = rec.get("pmcid")
        if pmcid:
            return f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/pdf/"

    return None


def strategy_unpaywall(doi: str) -> Optional[str]:
    """Unpaywall API — re-check with our email for OA status."""
    if not doi:
        return None
    encoded = urllib.parse.quote(doi, safe="")
    url = f"https://api.unpaywall.org/v2/{encoded}?email={UNPAYWALL_EMAIL}"
    data = api_get(url, "unpaywall")
    if not data:
        return None

    if data.get("is_oa") and data.get("oa_locations"):
        for loc in data["oa_locations"]:
            pdf_url = loc.get("url_for_pdf") or loc.get("pdf_url")
            if pdf_url:
                return pdf_url
    return None


def strategy_semantic_scholar(title: str) -> Optional[str]:
    """Semantic Scholar open access PDF search by title."""
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
            ext_ids = paper.get("externalIds", {})
            arxiv_id = ext_ids.get("ArXiv")
            if arxiv_id:
                return f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    return None


def strategy_arxiv_title(title: str) -> Optional[str]:
    """arXiv title search for preprint versions."""
    if not title:
        return None
    search_title = title.split("(")[0].split(" -- ")[0].strip()[:120]
    query = urllib.parse.quote(f'ti:"{search_title}"')
    url = f"http://export.arxiv.org/api/query?search_query={query}&start=0&max_results=3&sortBy=relevance"
    xml_str = api_get_xml(url, "arxiv")
    if not xml_str:
        return None
    try:
        root = ET.fromstring(xml_str)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        for entry in root.findall("atom:entry", ns)[:3]:
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


def strategy_acm_dl_direct(doi: str) -> Optional[str]:
    """ACM DL — try direct PDF download (many 2024+ papers are OA)."""
    if not doi or "10.1145" not in doi:
        return None
    return f"https://dl.acm.org/doi/pdf/{doi}"


def strategy_doi_scrape_enhanced(doi: str) -> Optional[str]:
    """Enhanced DOI scrape — follow DOI redirect, parse publisher page for PDF."""
    if not doi:
        return None
    _rate_limit("doi_scrape")
    try:
        doi_url = f"https://doi.org/{doi}"
        req = urllib.request.Request(doi_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            final_url = resp.geturl()
            html = resp.read().decode("utf-8", errors="ignore")

        # IOS Press (SHTI series — Ebara)
        if "iospress.com" in final_url or "content.iospress" in final_url:
            m = re.search(r'href="([^"]*\.pdf[^"]*)"', html)
            if m:
                link = m.group(1)
                if link.startswith("http"):
                    return link
                return f"https://ebooks.iospress.nl{link}" if link.startswith("/") else None
            # Try /pdf suffix
            if "/pdf" not in final_url:
                return final_url.rstrip("/") + "/pdf"

        # ACM DL
        if "dl.acm.org" in final_url:
            m = re.search(r'href="(/doi/pdf/[^"]+)"', html)
            if m:
                return "https://dl.acm.org" + m.group(1)

        # Sage
        if "sagepub.com" in final_url:
            m = re.search(r'href="(/doi/pdf/[^"]+)"', html)
            if m:
                return "https://journals.sagepub.com" + m.group(1)
            # Try epub pattern
            m = re.search(r'href="(/doi/epub/[^"]+)"', html)
            if m:
                pdf_url = m.group(1).replace("/epub/", "/pdf/")
                return "https://journals.sagepub.com" + pdf_url

        # Generic: look for PDF link
        pdf_links = re.findall(r'href="([^"]*\.pdf[^"]*)"', html)
        if pdf_links:
            link = pdf_links[0]
            if link.startswith("http"):
                return link
            if link.startswith("/"):
                from urllib.parse import urlparse
                parsed = urlparse(final_url)
                return f"{parsed.scheme}://{parsed.netloc}{link}"

    except Exception:
        pass
    return None


def strategy_philpapers(title: str) -> Optional[str]:
    """PhilPapers/PhilArchive search for philosophy/ethics papers."""
    if not title:
        return None
    query = urllib.parse.quote(title[:100])
    url = f"https://philpapers.org/s/{query}"
    _rate_limit("general")
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
        pdf_links = re.findall(r'href="(https?://[^"]*\.pdf[^"]*)"', html)
        for link in pdf_links[:3]:
            if "philarchive.org" in link or "philpapers.org" in link:
                return link
    except Exception:
        pass
    return None


def strategy_google_scholar_pdf(title: str) -> Optional[str]:
    """Google Scholar — search for [PDF] links. Very aggressive rate limiting."""
    if not title:
        return None
    query = urllib.parse.quote(f'"{title[:100]}"')
    url = f"https://scholar.google.com/scholar?q={query}&num=3"
    _rate_limit("google_scholar")
    try:
        req = urllib.request.Request(url, headers={
            **HEADERS,
            "Accept": "text/html,application/xhtml+xml",
            "Accept-Language": "en-US,en;q=0.9",
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
        # Look for [PDF] links — they appear as direct PDF hrefs
        pdf_links = re.findall(r'href="(https?://[^"]+\.pdf[^"]*)"', html)
        for link in pdf_links[:3]:
            # Skip Google's own cached links
            if "google.com" not in link and "googleapis.com" not in link:
                return link
    except Exception:
        pass
    return None


def strategy_institutional_repo(author: str, institution: str, title: str) -> Optional[str]:
    """Search known institutional repositories."""
    if not author or not institution:
        return None

    inst = institution.lower()

    # UTRGV ScholarWorks
    if "utrgv" in inst:
        query = urllib.parse.quote(title[:100])
        url = f"https://scholarworks.utrgv.edu/do/search/?q={query}&start=0&context=1577618&facet="
        html = api_get_html(url, "institutional")
        if html:
            pdf_links = re.findall(r'href="(https://scholarworks\.utrgv\.edu/[^"]*\.pdf[^"]*)"', html)
            if pdf_links:
                return pdf_links[0]

    # NTU DR-NTU
    if "ntu" in inst:
        query = urllib.parse.quote(title[:100])
        url = f"https://dr.ntu.edu.sg/simple-search?query={query}"
        html = api_get_html(url, "institutional")
        if html:
            pdf_links = re.findall(r'href="(/bitstream/[^"]*\.pdf[^"]*)"', html)
            if pdf_links:
                return f"https://dr.ntu.edu.sg{pdf_links[0]}"

    # Tsinghua
    if "tsinghua" in inst:
        # Try arXiv — Tsinghua authors very often put preprints on arXiv
        return strategy_arxiv_title(title)

    return None


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 1: Direct Downloads
# ═══════════════════════════════════════════════════════════════════════════════


def discover_phase1_url(paper: dict) -> Optional[str]:
    """Discover the actual PDF URL for a Phase 1 paper."""
    strategy = paper["strategy"]
    title = paper["title"]

    if strategy == "no_pdf_applicable":
        return "NO_PDF_APPLICABLE"

    if strategy == "acl_anthology_direct":
        # Pre-researched ACL Anthology direct PDF URL
        return paper.get("direct_pdf")

    if strategy == "ama_joe_oa":
        # AMA Journal of Ethics — 100% OA but Cloudflare blocks curl.
        # Try PubMed Central first (PMID 40748281)
        if paper.get("doi"):
            pmc_url = strategy_pubmed_central(paper["doi"])
            if pmc_url:
                return pmc_url
            epmc_url = strategy_europepmc(paper["doi"])
            if epmc_url:
                return epmc_url
        # Try Semantic Scholar for cached copy
        pdf_url = strategy_semantic_scholar(title)
        if pdf_url:
            return pdf_url
        # Fallback: try the direct article page PDF link
        article_url = paper["url"]
        html = api_get_html(article_url, "general")
        if html:
            m = re.search(r'href="([^"]*\.pdf[^"]*)"', html)
            if m:
                link = m.group(1)
                if link.startswith("/"):
                    return f"https://journalofethics.ama-assn.org{link}"
                return link
        # Last resort: construct known AMA JoE PDF path
        if paper.get("doi"):
            return f"https://journalofethics.ama-assn.org/sites/default/files/{paper['doi'].split('.')[-1]}.pdf"

    if strategy == "aaai_aies":
        # AIES 2025 — try AAAI Digital Library / OJS
        # First try Semantic Scholar
        pdf_url = strategy_semantic_scholar(title)
        if pdf_url:
            return pdf_url
        # Try arXiv
        pdf_url = strategy_arxiv_title(title)
        if pdf_url:
            return pdf_url
        # Try AAAI proceedings search
        query = urllib.parse.quote(title[:100])
        url = f"https://ojs.aaai.org/index.php/AIES/search/search?query={query}"
        html = api_get_html(url, "aaai")
        if html:
            # Look for article links then construct PDF URL
            m = re.search(r'href="(https://ojs\.aaai\.org/index\.php/AIES/article/view/\d+)"', html)
            if m:
                article_url = m.group(1)
                # AAAI OJS PDF = article/download/{id}/{id}
                article_id = article_url.rstrip("/").split("/")[-1]
                return f"https://ojs.aaai.org/index.php/AIES/article/download/{article_id}/{article_id}"
        return None

    if strategy == "acl_anthology_search":
        # ACL Anthology search for ArabicNLP 2025 papers
        # Clean title: remove " -- " and everything after for search
        search_title = title.replace(" -- ", ": ").split(":")[0].strip()
        query = urllib.parse.quote(search_title[:100])

        # Try the ACL Anthology search API
        url = f"https://aclanthology.org/api/search?q={query}"
        data = api_get(url, "acl")
        if data and isinstance(data, list):
            for entry in data[:5]:
                entry_title = entry.get("title", "")
                if titles_match(title, entry_title) or titles_match(search_title, entry_title):
                    acl_id = entry.get("id", "")
                    if acl_id:
                        return f"https://aclanthology.org/{acl_id}.pdf"

        # Broader search with full title
        query = urllib.parse.quote(title[:120])
        url = f"https://aclanthology.org/api/search?q={query}"
        data = api_get(url, "acl")
        if data and isinstance(data, list):
            for entry in data[:5]:
                entry_title = entry.get("title", "")
                if titles_match(title, entry_title):
                    acl_id = entry.get("id", "")
                    if acl_id:
                        return f"https://aclanthology.org/{acl_id}.pdf"

        # Try Semantic Scholar as fallback
        pdf_url = strategy_semantic_scholar(title)
        if pdf_url:
            return pdf_url

        return None

    if strategy == "stanford_codex":
        # Stanford CodeX publication page — look for PDF link
        html = api_get_html(paper["url"], "general")
        if html:
            # Look for PDF download links
            pdf_patterns = [
                r'href="([^"]*\.pdf[^"]*)"',
                r'href="(https://[^"]*stanford\.edu[^"]*\.pdf[^"]*)"',
                r'data-src="([^"]*\.pdf[^"]*)"',
            ]
            for pat in pdf_patterns:
                m = re.search(pat, html)
                if m:
                    link = m.group(1)
                    if link.startswith("/"):
                        return f"https://law.stanford.edu{link}"
                    return link

        # Try arXiv (Nay has published on arXiv before)
        pdf_url = strategy_arxiv_title(title)
        if pdf_url:
            return pdf_url
        # Try Semantic Scholar
        pdf_url = strategy_semantic_scholar(title)
        if pdf_url:
            return pdf_url
        # Try SSRN (Stanford researchers often use SSRN)
        query = urllib.parse.quote(f'"{title[:80]}"')
        url = f"https://papers.ssrn.com/sol3/results.cfm?txtKey_Words={query}"
        html = api_get_html(url, "general")
        if html:
            m = re.search(r'href="(https://papers\.ssrn\.com/sol3/papers\.cfm\?abstract_id=\d+)"', html)
            if m:
                # SSRN paper page — the PDF URL
                ssrn_url = m.group(1)
                abstract_id = ssrn_url.split("abstract_id=")[-1]
                return f"https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID{abstract_id}.pdf?abstractid={abstract_id}&type=2"
        return None

    if strategy == "author_search":
        # Sullins — book chapter in MIT Press Robophilosophy
        # Try Semantic Scholar
        pdf_url = strategy_semantic_scholar(title)
        if pdf_url:
            return pdf_url
        # Try PhilPapers (philosophy paper)
        pdf_url = strategy_philpapers(title)
        if pdf_url:
            return pdf_url
        # Try Google Scholar
        pdf_url = strategy_google_scholar_pdf(title)
        if pdf_url:
            return pdf_url
        return None

    if strategy == "konvens_proceedings":
        # GermEval 2019 — KONVENS proceedings
        # The overview paper URL: try known proceedings locations
        known_urls = [
            "https://corpora.linguistik.uni-erlangen.de/data/konvens/proceedings/papers/germeval/GermEvalSharedTask2019_Overview.pdf",
            "https://konvens.org/proceedings/2019/germeval/GermEvalSharedTask2019_Overview.pdf",
        ]
        for url in known_urls:
            # Just return the first candidate URL — download_pdf will validate
            return url

        # Try Semantic Scholar
        pdf_url = strategy_semantic_scholar("GermEval 2019 Task 2 Identification of Offensive Language")
        if pdf_url:
            return pdf_url
        return None

    return None


def run_phase1(dry_run: bool = False) -> List[dict]:
    """Phase 1: Direct downloads from confirmed/researched URLs."""
    print("\n" + "=" * 70)
    print("PHASE 1: Direct Downloads (9 papers — confirmed/high-confidence URLs)")
    print("=" * 70)

    pdfs_dir = get_pdfs_dir()
    results = []

    for paper in PHASE1_PAPERS:
        paper_path = PAPERS_DIR / paper["filename"]
        pdf_filename = Path(paper["filename"]).stem + ".pdf"
        pdf_path = pdfs_dir / pdf_filename

        print(f"\n  [{paper['id']:2d}] {paper['filename'][:65]}")
        print(f"       Strategy: {paper['strategy']}")

        if not paper_path.exists():
            print(f"       ERROR: Paper file not found!")
            results.append({"id": paper["id"], "status": "error", "msg": "File not found"})
            continue

        # Check if PDF already exists
        if pdf_path.exists() and pdf_path.stat().st_size > 1000:
            print(f"       SKIP: PDF already exists ({pdf_path.stat().st_size / 1024:.0f}KB)")
            results.append({"id": paper["id"], "status": "skip", "msg": "Already exists"})
            continue

        # Special: no_pdf_applicable
        if paper["strategy"] == "no_pdf_applicable":
            print(f"       Marking as no_pdf_applicable (GitHub repo, not a paper)")
            if not dry_run:
                safe_add_yaml_field(paper_path, "no_pdf_applicable", "true")
            results.append({"id": paper["id"], "status": "marked_no_pdf", "msg": "GitHub repo"})
            continue

        # Discover URL
        pdf_url = discover_phase1_url(paper)

        if pdf_url:
            print(f"       FOUND: {pdf_url[:80]}")

            if dry_run:
                results.append({"id": paper["id"], "status": "found", "url": pdf_url})
            else:
                _rate_limit("download")
                ok, msg = download_pdf(pdf_url, pdf_path)
                if not ok and ("403" in msg or "Not a PDF" in msg):
                    print(f"       Retrying with browser headers...")
                    _rate_limit("download")
                    ok, msg = download_pdf_browser(pdf_url, pdf_path)
                if ok:
                    size_kb = pdf_path.stat().st_size / 1024
                    print(f"       DOWNLOADED ({size_kb:.0f}KB)")
                    try:
                        safe_update_external_pdf(paper_path, pdf_url)
                        safe_update_local_pdf(paper_path, pdf_filename)
                    except Exception as e:
                        print(f"       WARNING: YAML update failed: {e}")
                    results.append({"id": paper["id"], "status": "downloaded", "url": pdf_url, "size_kb": size_kb})
                else:
                    print(f"       DOWNLOAD FAILED: {msg}")
                    results.append({"id": paper["id"], "status": "dl_failed", "url": pdf_url, "msg": msg})
        else:
            print(f"       NOT FOUND")
            results.append({"id": paper["id"], "status": "not_found"})

    return results


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 2: Creative API Strategies
# ═══════════════════════════════════════════════════════════════════════════════

# Map strategy names to functions
PHASE2_STRATEGY_MAP = {
    "europepmc": lambda p: strategy_europepmc(p.get("doi")),
    "pubmed_central": lambda p: strategy_pubmed_central(p.get("doi")),
    "unpaywall": lambda p: strategy_unpaywall(p.get("doi")),
    "semantic_scholar": lambda p: strategy_semantic_scholar(p["title"]),
    "arxiv_title": lambda p: strategy_arxiv_title(p["title"]),
    "acm_dl_direct": lambda p: strategy_acm_dl_direct(p.get("doi")),
    "doi_scrape_enhanced": lambda p: strategy_doi_scrape_enhanced(p.get("doi")),
    "philpapers": lambda p: strategy_philpapers(p["title"]),
    "google_scholar_pdf": lambda p: strategy_google_scholar_pdf(p["title"]),
    "researchgate": lambda p: None,  # ResearchGate blocks automated access; skip
    "institutional_repo": lambda p: strategy_institutional_repo(
        p.get("first_author", ""), p.get("institution", ""), p["title"]
    ),
}


def run_phase2(dry_run: bool = False) -> List[dict]:
    """Phase 2: Creative API strategies for 5 harder papers."""
    print("\n" + "=" * 70)
    print("PHASE 2: Creative API Strategies (5 papers — strong leads)")
    print("=" * 70)

    pdfs_dir = get_pdfs_dir()
    results = []

    for paper in PHASE2_PAPERS:
        paper_path = PAPERS_DIR / paper["filename"]
        pdf_filename = Path(paper["filename"]).stem + ".pdf"
        pdf_path = pdfs_dir / pdf_filename

        print(f"\n  [{paper['id']:2d}] {paper['filename'][:65]}")
        print(f"       DOI: {paper.get('doi', 'N/A')}")
        print(f"       Strategies: {', '.join(paper['strategies'])}")

        if not paper_path.exists():
            print(f"       ERROR: Paper file not found!")
            results.append({"id": paper["id"], "status": "error", "msg": "File not found"})
            continue

        if pdf_path.exists() and pdf_path.stat().st_size > 1000:
            print(f"       SKIP: PDF already exists ({pdf_path.stat().st_size / 1024:.0f}KB)")
            results.append({"id": paper["id"], "status": "skip"})
            continue

        # Run strategies in order until one succeeds
        found_url = None
        winning_strategy = None

        for strat_name in paper["strategies"]:
            strat_fn = PHASE2_STRATEGY_MAP.get(strat_name)
            if not strat_fn:
                print(f"       [{strat_name}] Unknown strategy, skipping")
                continue

            try:
                pdf_url = strat_fn(paper)
            except Exception as e:
                print(f"       [{strat_name}] ERROR: {e}")
                continue

            if pdf_url:
                print(f"       [{strat_name}] FOUND: {pdf_url[:80]}")
                found_url = pdf_url
                winning_strategy = strat_name
                break
            else:
                print(f"       [{strat_name}] No result")

        if found_url:
            if dry_run:
                results.append({
                    "id": paper["id"], "status": "found",
                    "url": found_url, "strategy": winning_strategy,
                })
            else:
                _rate_limit("download")
                ok, msg = download_pdf(found_url, pdf_path)
                if not ok and ("403" in msg or "Not a PDF" in msg):
                    print(f"       Retrying with browser headers...")
                    _rate_limit("download")
                    ok, msg = download_pdf_browser(found_url, pdf_path)
                if ok:
                    size_kb = pdf_path.stat().st_size / 1024
                    print(f"       DOWNLOADED ({size_kb:.0f}KB) via {winning_strategy}")
                    try:
                        safe_update_external_pdf(paper_path, found_url)
                        safe_update_local_pdf(paper_path, pdf_filename)
                    except Exception as e:
                        print(f"       WARNING: YAML update failed: {e}")
                    results.append({
                        "id": paper["id"], "status": "downloaded",
                        "url": found_url, "strategy": winning_strategy, "size_kb": size_kb,
                    })
                else:
                    print(f"       DOWNLOAD FAILED: {msg}")
                    results.append({
                        "id": paper["id"], "status": "dl_failed",
                        "url": found_url, "strategy": winning_strategy, "msg": msg,
                    })
        else:
            print(f"       NOT FOUND (tried {len(paper['strategies'])} strategies)")
            results.append({"id": paper["id"], "status": "not_found"})

    return results


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 3: Manual Research Report
# ═══════════════════════════════════════════════════════════════════════════════


def generate_research_links(paper: dict) -> List[dict]:
    """Generate research links for a book/paywalled paper."""
    links = []
    title = paper["title"]
    author = paper["first_author"]
    doi = paper.get("doi")
    isbn = paper.get("isbn")

    # Google Books
    if title:
        q = urllib.parse.quote(f"{title} {author}")
        links.append({"source": "Google Books", "url": f"https://books.google.com/books?q={q}"})

    # Internet Archive
    if title:
        q = urllib.parse.quote(title)
        links.append({"source": "Internet Archive", "url": f"https://archive.org/search?query={q}"})

    # Open Library (by ISBN)
    if isbn:
        links.append({"source": "Open Library", "url": f"https://openlibrary.org/isbn/{isbn}"})

    # Google Scholar
    if title:
        q = urllib.parse.quote(f'"{title}"')
        links.append({"source": "Google Scholar", "url": f"https://scholar.google.com/scholar?q={q}"})

    # SSRN
    if title:
        q = urllib.parse.quote(title[:80])
        links.append({"source": "SSRN", "url": f"https://papers.ssrn.com/sol3/results.cfm?txtKey_Words={q}"})

    # PhilSci-Archive
    if title:
        q = urllib.parse.quote(title[:80])
        links.append({"source": "PhilSci-Archive", "url": f"https://philsci-archive.pitt.edu/cgi/search/simple?q={q}"})

    # OSF Preprints
    if title:
        q = urllib.parse.quote(title[:80])
        links.append({"source": "OSF Preprints", "url": f"https://osf.io/preprints/discover?q={q}"})

    # ORCID (author)
    if author:
        q = urllib.parse.quote(author)
        links.append({"source": "ORCID", "url": f"https://orcid.org/orcid-search/search?searchQuery={q}"})

    # Author institutional page (generic Google search)
    if author:
        q = urllib.parse.quote(f"{author} publications homepage")
        links.append({"source": "Author homepage", "url": f"https://www.google.com/search?q={q}"})

    # Publisher page
    if paper.get("url"):
        links.append({"source": "Publisher page", "url": paper["url"]})

    # DOI
    if doi:
        links.append({"source": "DOI", "url": f"https://doi.org/{doi}"})

    return links


def run_phase3(dry_run: bool = False) -> List[dict]:
    """Phase 3: Generate manual research report for books/paywalled papers.

    Also tries Unpaywall / EuropePMC as a last-chance check for each DOI paper.
    """
    print("\n" + "=" * 70)
    print("PHASE 3: Manual Research Report (5 papers — books/hard paywall)")
    print("=" * 70)

    pdfs_dir = get_pdfs_dir()
    results = []
    report_entries = []

    for paper in PHASE3_PAPERS:
        paper_path = PAPERS_DIR / paper["filename"]
        pdf_filename = Path(paper["filename"]).stem + ".pdf"
        pdf_path = pdfs_dir / pdf_filename

        print(f"\n  [{paper['id']:2d}] {paper['filename'][:65]}")
        print(f"       Type: {paper['type']} | Publisher: {paper['publisher']}")
        print(f"       Notes: {paper['notes']}")

        if not paper_path.exists():
            print(f"       ERROR: Paper file not found!")
            results.append({"id": paper["id"], "status": "error"})
            continue

        if pdf_path.exists() and pdf_path.stat().st_size > 1000:
            print(f"       SKIP: PDF already exists")
            results.append({"id": paper["id"], "status": "skip"})
            continue

        # Last-chance automated check for DOI papers
        found_url = None
        if paper.get("doi"):
            print(f"       Trying last-chance automated check...")
            for strat_name, strat_fn in [
                ("unpaywall", lambda: strategy_unpaywall(paper["doi"])),
                ("europepmc", lambda: strategy_europepmc(paper["doi"])),
                ("semantic_scholar", lambda: strategy_semantic_scholar(paper["title"])),
            ]:
                try:
                    url = strat_fn()
                    if url:
                        print(f"       [{strat_name}] SURPRISE FIND: {url[:80]}")
                        found_url = url
                        break
                    else:
                        print(f"       [{strat_name}] No result")
                except Exception:
                    pass

        if found_url and not dry_run:
            _rate_limit("download")
            ok, msg = download_pdf(found_url, pdf_path)
            if not ok and ("403" in msg or "Not a PDF" in msg):
                print(f"       Retrying with browser headers...")
                _rate_limit("download")
                ok, msg = download_pdf_browser(found_url, pdf_path)
            if ok:
                size_kb = pdf_path.stat().st_size / 1024
                print(f"       DOWNLOADED ({size_kb:.0f}KB)")
                try:
                    safe_update_external_pdf(paper_path, found_url)
                    safe_update_local_pdf(paper_path, pdf_filename)
                except Exception as e:
                    print(f"       WARNING: YAML update failed: {e}")
                results.append({"id": paper["id"], "status": "downloaded", "url": found_url, "size_kb": size_kb})
                continue
            else:
                print(f"       DOWNLOAD FAILED: {msg}")

        if found_url and dry_run:
            results.append({"id": paper["id"], "status": "found", "url": found_url})
            continue

        # Generate research links for manual follow-up
        links = generate_research_links(paper)
        print(f"       Generated {len(links)} research links for manual report")
        results.append({"id": paper["id"], "status": "manual_report", "links": links})

        report_entries.append({
            "paper": paper,
            "links": links,
        })

    # Write manual research report
    if report_entries:
        write_manual_report(report_entries)

    return results


def write_manual_report(entries: List[dict]):
    """Write the manual PDF research report."""
    LOG_DIR.mkdir(exist_ok=True)
    lines = [
        "# Manual PDF Research Report",
        f"",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Papers:** {len(entries)} requiring manual acquisition",
        "",
        "These papers could not be automatically downloaded because they are",
        "commercially published books or paywalled journal articles.",
        "",
        "---",
        "",
    ]

    for entry in entries:
        p = entry["paper"]
        lines.append(f"## {p['id']}. {p['title']}")
        lines.append(f"")
        lines.append(f"- **Author:** {p['first_author']}")
        lines.append(f"- **Type:** {p['type']}")
        lines.append(f"- **Publisher:** {p['publisher']}")
        if p.get("doi"):
            lines.append(f"- **DOI:** `{p['doi']}`")
        if p.get("isbn"):
            lines.append(f"- **ISBN:** `{p['isbn']}`")
        lines.append(f"- **Notes:** {p['notes']}")
        lines.append(f"- **Vault file:** `papers/{p['filename']}`")
        lines.append(f"")
        lines.append(f"### Research Links")
        lines.append(f"")
        for link in entry["links"]:
            lines.append(f"- [{link['source']}]({link['url']})")
        lines.append(f"")
        lines.append(f"### Acquisition Suggestions")
        lines.append(f"")
        if p["type"] == "book":
            lines.append(f"1. Check Internet Archive lending library for borrowable copy")
            lines.append(f"2. Check if author has posted sample chapters on their website")
            lines.append(f"3. Check university library access (institutional subscription)")
            lines.append(f"4. Check if preprint/draft exists on SSRN, PhilSci-Archive, or OSF")
        else:
            lines.append(f"1. Check institutional library access (T&F / Sage subscription)")
            lines.append(f"2. Contact author directly for a preprint copy")
            lines.append(f"3. Check ResearchGate for author-deposited version")
            lines.append(f"4. Check if PubMed Central has an embargo-lifted version")
        lines.append(f"")
        lines.append(f"---")
        lines.append(f"")

    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n  Manual report written to: {REPORT_FILE}")


# ═══════════════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════════════


def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args

    # Parse --phase N
    phase_filter = None
    if "--phase" in args:
        idx = args.index("--phase")
        if idx + 1 < len(args):
            phase_filter = int(args[idx + 1])

    print("=" * 70)
    print("ADVANCED PDF FINDER — Targeted Multi-Strategy Acquisition")
    print(f"  19 papers | 3 phases | {'DRY RUN' if dry_run else 'LIVE DOWNLOAD'}")
    if phase_filter:
        print(f"  Running Phase {phase_filter} only")
    print("=" * 70)

    all_results = {}

    # Phase 1
    if phase_filter is None or phase_filter == 1:
        p1_results = run_phase1(dry_run=dry_run)
        all_results["phase1"] = p1_results

    # Phase 2
    if phase_filter is None or phase_filter == 2:
        p2_results = run_phase2(dry_run=dry_run)
        all_results["phase2"] = p2_results

    # Phase 3
    if phase_filter is None or phase_filter == 3:
        p3_results = run_phase3(dry_run=dry_run)
        all_results["phase3"] = p3_results

    # Summary
    print("\n" + "=" * 70)
    print("FINAL SUMMARY")
    print("=" * 70)

    total_downloaded = 0
    total_found = 0
    total_not_found = 0
    total_failed = 0
    total_skip = 0
    total_marked = 0
    total_manual = 0

    for phase_name, phase_results in all_results.items():
        print(f"\n  {phase_name.upper()}:")
        for r in phase_results:
            status = r["status"]
            tag = f"  [{r['id']:2d}]"
            if status == "downloaded":
                print(f"    {tag} DOWNLOADED ({r.get('size_kb', 0):.0f}KB)")
                total_downloaded += 1
            elif status == "found":
                print(f"    {tag} FOUND (dry-run): {r.get('url', '')[:60]}")
                total_found += 1
            elif status == "not_found":
                print(f"    {tag} NOT FOUND")
                total_not_found += 1
            elif status == "dl_failed":
                print(f"    {tag} DOWNLOAD FAILED: {r.get('msg', '')}")
                total_failed += 1
            elif status == "skip":
                print(f"    {tag} SKIPPED (exists)")
                total_skip += 1
            elif status == "marked_no_pdf":
                print(f"    {tag} MARKED no_pdf_applicable")
                total_marked += 1
            elif status == "manual_report":
                print(f"    {tag} MANUAL REPORT")
                total_manual += 1
            elif status == "error":
                print(f"    {tag} ERROR: {r.get('msg', '')}")

    print(f"\n  {'─' * 40}")
    print(f"  Downloaded:       {total_downloaded}")
    print(f"  Found (dry-run):  {total_found}")
    print(f"  Download failed:  {total_failed}")
    print(f"  Not found:        {total_not_found}")
    print(f"  Skipped (exist):  {total_skip}")
    print(f"  Marked no-PDF:    {total_marked}")
    print(f"  Manual report:    {total_manual}")
    print(f"  {'─' * 40}")
    total = total_downloaded + total_found + total_marked
    print(f"  Resolved:         {total} / 19")
    print("=" * 70)

    # Save log
    LOG_DIR.mkdir(exist_ok=True)
    log = {
        "timestamp": datetime.now().isoformat(),
        "dry_run": dry_run,
        "results": all_results,
        "summary": {
            "downloaded": total_downloaded,
            "found": total_found,
            "not_found": total_not_found,
            "failed": total_failed,
            "skip": total_skip,
            "marked": total_marked,
            "manual": total_manual,
        },
    }
    LOG_FILE.write_text(json.dumps(log, indent=2, default=str), encoding="utf-8")
    print(f"\nLog saved to: {LOG_FILE}")


if __name__ == "__main__":
    main()
