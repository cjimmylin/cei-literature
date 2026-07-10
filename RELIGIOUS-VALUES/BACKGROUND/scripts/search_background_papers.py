#!/usr/bin/env python3
"""
search_background_papers.py — Systematic literature search for BACKGROUND folder.

Searches Semantic Scholar, arXiv, and OpenAlex for ~120-150 scholarly papers
across 12 thematic domains supporting an academic paper on religious values
alignment benchmarks for AI.

Unlike the benchmark search (which requires religious + benchmark keywords),
this search uses per-folder relevance criteria to find broader scholarly context.

Output: RELIGIOUS-VALUES/BACKGROUND/data/YYYYMMDD-background-search-results.json

Usage:
    python search_background_papers.py                    # All folders
    python search_background_papers.py --folder 01        # Single folder (prefix match)
    python search_background_papers.py --dry-run           # Print queries only
    python search_background_papers.py --seeds-only        # Write seeds without API calls
"""
from __future__ import annotations

import functools
import json
import os
import re
import sys
import time
import urllib.request
import urllib.parse
import urllib.error
from datetime import date
from pathlib import Path

print = functools.partial(print, flush=True)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
BACKGROUND_DIR = SCRIPT_DIR.parent
PROJECT_DIR = BACKGROUND_DIR.parent
WS_ROOT = PROJECT_DIR.parent
PAPERS_DIR = WS_ROOT / "papers"
DATA_DIR = BACKGROUND_DIR / "data"

TODAY = date.today().strftime("%Y%m%d")

# ---------------------------------------------------------------------------
# API configuration
# ---------------------------------------------------------------------------
S2_API = "https://api.semanticscholar.org/graph/v1"
S2_FIELDS = "paperId,title,year,citationCount,url,isOpenAccess,openAccessPdf,authors,venue,abstract"
S2_DELAY = 20  # seconds between requests (rate limit — 12s still triggers 429)

ARXIV_API = "http://export.arxiv.org/api/query"
ARXIV_DELAY = 5

OPENALEX_API = "https://api.openalex.org/works"
OPENALEX_DELAY = 0.2  # 10 req/s allowed with polite pool

# ---------------------------------------------------------------------------
# 12 Thematic Search Configurations
# ---------------------------------------------------------------------------
SEARCH_CONFIGS = {
    "01-ai-values-alignment": {
        "queries": [
            "AI values alignment benchmark evaluation",
            "HELM holistic evaluation language models",
            "MMLU massive multitask language understanding",
            "human values alignment LLM measurement",
            "AI alignment evaluation methodology survey",
            "value alignment evaluation large language models",
            "benchmark design AI ethics evaluation",
            "reinforcement learning human feedback alignment",
        ],
        "relevance_keywords": {"alignment", "values", "benchmark", "evaluation", "HELM", "MMLU", "ethics", "LLM", "language model"},
        "min_keywords": 2,
    },
    "02-religious-nlp": {
        "queries": [
            "computational theology natural language processing",
            "religious text mining NLP",
            "sacred text computational analysis",
            "digital humanities religion corpus",
            "scripture natural language processing",
            "religious corpus linguistics computational",
        ],
        "relevance_keywords": {"religious", "theology", "sacred", "scripture", "NLP", "computational", "corpus", "text mining", "digital humanities"},
        "min_keywords": 2,
    },
    "03-cultural-values-ai": {
        "queries": [
            "WEIRD bias artificial intelligence evaluation",
            "World Values Survey AI alignment",
            "Hofstede cultural dimensions language models",
            "cultural alignment AI benchmark",
            "cross-cultural AI ethics survey",
            "CValues Chinese moral values benchmark",
            "GlobalOpinionQA cultural values LLM",
            "cultural bias large language models evaluation",
        ],
        "relevance_keywords": {"cultural", "cross-cultural", "WEIRD", "values", "Hofstede", "Schwartz", "AI", "LLM", "bias", "alignment"},
        "min_keywords": 2,
    },
    "04-islamic-ai-ethics": {
        "queries": [
            "Islamic ethics artificial intelligence Maqasid",
            "Quranic NLP Arabic language model",
            "fatwa artificial intelligence Islamic law",
            "Islamic jurisprudence AI evaluation",
            "halal artificial intelligence framework",
            "Arabic Islamic text processing NLP",
            "Maqasid al-Shariah AI technology",
            "Islamic bioethics artificial intelligence",
        ],
        "relevance_keywords": {"islamic", "islam", "quran", "quranic", "maqasid", "shariah", "sharia", "fatwa", "fiqh", "halal", "arabic", "AI", "ethics"},
        "min_keywords": 2,
    },
    "05-christian-ethics-ai": {
        "queries": [
            "Christian ethics artificial intelligence theology",
            "Vatican AI ethics papal encyclical",
            "natural law theory artificial intelligence",
            "theological anthropology AI machine learning",
            "Christian theological benchmark LLM",
            "FaithBench Christian theology evaluation",
            "Catholic social teaching artificial intelligence",
            "Protestant theology technology ethics",
        ],
        "relevance_keywords": {"christian", "theology", "theological", "vatican", "catholic", "protestant", "church", "faith", "AI", "ethics", "natural law"},
        "min_keywords": 2,
    },
    "06-dharmic-ethics-ai": {
        "queries": [
            "Hindu ethics artificial intelligence dharma karma",
            "Buddhist ethics AI compassion karuna",
            "Jain ahimsa nonviolence AI technology",
            "dharmic values artificial intelligence alignment",
            "Bhagavad Gita AI ethics framework",
            "Buddhist interdependence AI evaluation",
            "Sikh ethics artificial intelligence sewa",
            "yoga philosophy artificial intelligence ethics",
        ],
        "relevance_keywords": {"hindu", "buddhist", "jain", "sikh", "dharma", "karma", "ahimsa", "karuna", "vedic", "gita", "AI", "ethics"},
        "min_keywords": 2,
    },
    "07-comparative-religious-ethics": {
        "queries": [
            "comparative religious ethics methodology",
            "moral philosophy across religious traditions",
            "religious pluralism ethics artificial intelligence",
            "interfaith ethics AI governance",
            "religion science technology ethics",
            "comparative ethics AI alignment multiple traditions",
            "global ethics religious diversity artificial intelligence",
        ],
        "relevance_keywords": {"comparative", "religious", "interfaith", "pluralism", "ethics", "moral", "traditions", "philosophy", "AI"},
        "min_keywords": 2,
    },
    "08-benchmark-psychometrics": {
        "queries": [
            "construct validity AI benchmark evaluation",
            "psychometric properties LLM benchmark",
            "measurement invariance cross-cultural evaluation",
            "item response theory natural language processing",
            "annotator agreement benchmark quality NLP",
            "benchmark design methodology NLP evaluation",
            "AI evaluation test reliability validity",
            "benchmark saturation LLM evaluation survey",
        ],
        "relevance_keywords": {"benchmark", "psychometric", "validity", "reliability", "measurement", "evaluation", "NLP", "LLM", "construct", "IRT"},
        "min_keywords": 2,
    },
    "09-ai-bias-religion": {
        "queries": [
            "religious bias large language models",
            "LLM stereotyping religion Islam Christianity",
            "religious discrimination AI fairness",
            "hate speech religion detection benchmark",
            "Islamophobia antisemitism AI detection",
            "anti-Muslim bias GPT language model",
            "religious sentiment analysis bias NLP",
        ],
        "relevance_keywords": {"bias", "religious", "religion", "discrimination", "fairness", "stereotype", "hate speech", "islamophobia", "antisemitism", "LLM", "AI"},
        "min_keywords": 2,
    },
    "10-indigenous-african-ai": {
        "queries": [
            "Ubuntu philosophy artificial intelligence ethics",
            "African ethics AI communitarian",
            "Indigenous knowledge systems AI technology",
            "decolonial artificial intelligence",
            "data sovereignty Indigenous AI",
            "tikanga Maori AI evaluation",
            "African philosophy technology governance",
            "Indigenous data governance CARE principles",
        ],
        "relevance_keywords": {"ubuntu", "african", "indigenous", "decolonial", "maori", "tikanga", "communitarian", "data sovereignty", "AI", "ethics"},
        "min_keywords": 2,
    },
    "11-jewish-ethics-ai": {
        "queries": [
            "Jewish ethics artificial intelligence halakha",
            "Talmud computational analysis reasoning",
            "rabbinical ethics AI technology",
            "Hebrew NLP religious text processing",
            "computational Talmudics Responsa project",
            "Jewish law technology artificial intelligence",
        ],
        "relevance_keywords": {"jewish", "judaism", "talmud", "talmudic", "halakha", "rabbin", "hebrew", "torah", "responsa", "AI", "ethics", "computational"},
        "min_keywords": 2,
    },
    "12-east-asian-philosophy-ai": {
        "queries": [
            "Confucian ethics artificial intelligence ren",
            "Taoist philosophy technology wu wei",
            "Shinto robotics ethics Japanese AI",
            "Chinese moral values AI alignment CValues",
            "East Asian philosophy AI governance",
            "Japanese roboethics robot ethics Shinto",
            "Confucian role ethics technology",
        ],
        "relevance_keywords": {"confucian", "taoist", "taoism", "shinto", "japanese", "chinese", "east asian", "ren", "li", "AI", "ethics", "robot"},
        "min_keywords": 2,
    },
}

# ---------------------------------------------------------------------------
# Expert Seeds — known important papers that API search may miss
# ---------------------------------------------------------------------------
EXPERT_SEEDS = [
    # 01 - AI Values Alignment
    {
        "title": "Holistic Evaluation of Language Models",
        "authors": ["Liang, Percy", "et al."],
        "year": "2023",
        "doi": "10.1162/tacl_a_00595",
        "url": "https://arxiv.org/abs/2211.09110",
        "source": "TACL",
        "type": "journal_article",
        "priority": "must_read",
        "expert_source": [7],
        "topic_tags": ["HELM", "LLM_evaluation", "benchmark_design"],
        "relevance_note": "Foundational multi-metric LLM evaluation framework. Defines the benchmark harness paradigm this paper builds on.",
        "folder": "01-ai-values-alignment",
    },
    {
        "title": "Measuring Massive Multitask Language Understanding",
        "authors": ["Hendrycks, Dan", "et al."],
        "year": "2021",
        "doi": "10.48550/arXiv.2009.03300",
        "url": "https://arxiv.org/abs/2009.03300",
        "source": "ICLR",
        "type": "conference_paper",
        "priority": "must_read",
        "expert_source": [7],
        "topic_tags": ["MMLU", "LLM_evaluation", "knowledge_benchmark"],
        "relevance_note": "Canonical knowledge evaluation benchmark. Religious values benchmarks extend this paradigm to theological domains.",
        "folder": "01-ai-values-alignment",
    },
    {
        "title": "Artificial Intelligence, Values, and Alignment",
        "authors": ["Gabriel, Iason"],
        "year": "2020",
        "doi": "10.1007/s11023-020-09539-2",
        "url": "https://link.springer.com/article/10.1007/s11023-020-09539-2",
        "source": "Minds and Machines",
        "type": "journal_article",
        "priority": "must_read",
        "expert_source": [9],
        "topic_tags": ["values_alignment", "AI_ethics", "normative_theory"],
        "relevance_note": "Defines the value alignment problem and argues for principled approaches to encoding human values.",
        "folder": "01-ai-values-alignment",
    },
    {
        "title": "Training language models to follow instructions with human feedback",
        "authors": ["Ouyang, Long", "et al."],
        "year": "2022",
        "doi": "10.48550/arXiv.2203.02155",
        "url": "https://arxiv.org/abs/2203.02155",
        "source": "NeurIPS",
        "type": "conference_paper",
        "priority": "must_read",
        "expert_source": [7],
        "topic_tags": ["RLHF", "alignment", "instruction_following"],
        "relevance_note": "InstructGPT -- defines RLHF paradigm. Religious values alignment evaluation tests what RLHF-trained models actually learn.",
        "folder": "01-ai-values-alignment",
    },
    {
        "title": "What Are Human Values? And How Do We Align AI If We Don't Know?",
        "authors": ["Klingefjord, Oscar", "et al."],
        "year": "2024",
        "doi": "10.48550/arXiv.2404.10636",
        "url": "https://arxiv.org/abs/2404.10636",
        "source": "arXiv",
        "type": "working_paper",
        "priority": "must_read",
        "expert_source": [9],
        "topic_tags": ["values_alignment", "value_pluralism", "survey"],
        "relevance_note": "Surveys the philosophical problem of defining 'values' for alignment -- directly motivates why religious values need separate benchmarks.",
        "folder": "01-ai-values-alignment",
    },
    # 03 - Cultural Values in AI
    {
        "title": "The weirdest people in the world?",
        "authors": ["Henrich, Joseph", "Heine, Steven J.", "Norenzayan, Ara"],
        "year": "2010",
        "doi": "10.1017/S0140525X0999152X",
        "url": "https://doi.org/10.1017/S0140525X0999152X",
        "source": "Behavioral and Brain Sciences",
        "type": "journal_article",
        "priority": "must_read",
        "expert_source": [8],
        "topic_tags": ["WEIRD", "cross-cultural", "psychology", "sampling_bias"],
        "relevance_note": "Foundational WEIRD critique. Religious values benchmarks must address the same sampling bias in AI evaluation.",
        "folder": "03-cultural-values-ai",
    },
    {
        "title": "Towards Measuring the Representation of Subjective Global Opinions in Language Models",
        "authors": ["Durmus, Esin", "et al."],
        "year": "2024",
        "doi": "10.48550/arXiv.2306.16388",
        "url": "https://arxiv.org/abs/2306.16388",
        "source": "arXiv",
        "type": "working_paper",
        "priority": "must_read",
        "expert_source": [8],
        "topic_tags": ["GlobalOpinionQA", "cultural_values", "LLM_alignment"],
        "relevance_note": "GlobalOpinionQA -- tests LLM alignment with World Values Survey across countries. Direct precedent for religious values alignment.",
        "folder": "03-cultural-values-ai",
    },
    # 07 - Comparative Religious Ethics
    {
        "title": "Comparative Religious Ethics: A Narrative Approach",
        "authors": ["Twiss, Sumner B.", "Grelle, Bruce"],
        "year": "1998",
        "source": "Blackwell",
        "type": "book_chapter",
        "priority": "must_read",
        "expert_source": [9, 12],
        "topic_tags": ["comparative_ethics", "methodology", "religious_ethics"],
        "relevance_note": "Foundational methodology for comparing ethical frameworks across religious traditions.",
        "folder": "07-comparative-religious-ethics",
    },
    # 08 - Benchmark Psychometrics
    {
        "title": "AI and the Everything in the Whole Wide World Benchmark",
        "authors": ["Raji, Inioluwa Deborah", "et al."],
        "year": "2021",
        "doi": "10.48550/arXiv.2111.15366",
        "url": "https://arxiv.org/abs/2111.15366",
        "source": "NeurIPS",
        "type": "conference_paper",
        "priority": "must_read",
        "expert_source": [13],
        "topic_tags": ["benchmark_critique", "AI_evaluation", "construct_validity"],
        "relevance_note": "Critical analysis of benchmark proliferation and validity. Directly relevant to whether religious values benchmarks measure what they claim.",
        "folder": "08-benchmark-psychometrics",
    },
    {
        "title": "What Will it Take to Fix Benchmarking in Natural Language Understanding?",
        "authors": ["Bowman, Samuel R.", "Dahl, George E."],
        "year": "2021",
        "doi": "10.48550/arXiv.2104.02145",
        "url": "https://arxiv.org/abs/2104.02145",
        "source": "arXiv",
        "type": "working_paper",
        "priority": "must_read",
        "expert_source": [7, 13],
        "topic_tags": ["benchmark_design", "NLU", "evaluation_methodology"],
        "relevance_note": "Identifies fundamental problems with NLU benchmarks -- annotation artifacts, ceiling effects, construct validity. Religious benchmarks must avoid these.",
        "folder": "08-benchmark-psychometrics",
    },
    # 09 - AI Bias & Religion
    {
        "title": "Persistent Anti-Muslim Bias in Large Language Models",
        "authors": ["Abid, Abubakar", "Farooqi, Maheen", "Zou, James"],
        "year": "2021",
        "doi": "10.1145/3461702.3462624",
        "url": "https://dl.acm.org/doi/10.1145/3461702.3462624",
        "source": "AIES",
        "type": "conference_paper",
        "priority": "must_read",
        "expert_source": [10, 11],
        "topic_tags": ["anti-Muslim_bias", "GPT-3", "religious_discrimination", "LLM"],
        "relevance_note": "Demonstrates systematic anti-Muslim bias in GPT-3. Motivates why religious values alignment evaluation is urgent.",
        "folder": "09-ai-bias-religion",
    },
    # 10 - Indigenous & African AI
    {
        "title": "From Rationality to Relationality: Ubuntu as an Ethical and Human Rights Framework for Artificial Intelligence Governance",
        "authors": ["Mhlambi, Sabelo"],
        "year": "2020",
        "url": "https://carrcenter.hks.harvard.edu/publications/rationality-relationality-ubuntu-ethical-and-human-rights-framework-artificial",
        "source": "Carr Center Discussion Paper",
        "type": "working_paper",
        "priority": "must_read",
        "expert_source": [5],
        "topic_tags": ["ubuntu", "AI_governance", "relational_ethics", "African_philosophy"],
        "relevance_note": "Proposes Ubuntu as governance framework for AI. Foundational for understanding why African philosophical traditions need representation in AI benchmarks.",
        "folder": "10-indigenous-african-ai",
    },
    {
        "title": "Algorithmic injustice: a relational ethics approach",
        "authors": ["Birhane, Abeba"],
        "year": "2021",
        "doi": "10.1016/j.patter.2020.100205",
        "url": "https://doi.org/10.1016/j.patter.2020.100205",
        "source": "Patterns",
        "type": "journal_article",
        "priority": "must_read",
        "expert_source": [11],
        "topic_tags": ["relational_ethics", "algorithmic_justice", "African_philosophy"],
        "relevance_note": "Applies relational ethics (with Ubuntu roots) to algorithmic justice. Frames why individualist benchmark paradigms fail for communal traditions.",
        "folder": "10-indigenous-african-ai",
    },
]

# ---------------------------------------------------------------------------
# Top venues for priority heuristic
# ---------------------------------------------------------------------------
TOP_VENUES = {
    "neurips", "icml", "iclr", "acl", "emnlp", "naacl", "aaai",
    "nature", "science", "behavioral and brain sciences", "minds and machines",
    "ai and ethics", "journal of religious ethics", "aies", "facct",
}

# ---------------------------------------------------------------------------
# Vault dedup utilities
# ---------------------------------------------------------------------------
def load_vault_titles() -> set:
    """Load all paper titles from vault for dedup."""
    titles: set[str] = set()
    if not PAPERS_DIR.is_dir():
        return titles
    for pf in PAPERS_DIR.iterdir():
        if pf.suffix != ".md":
            continue
        try:
            content = pf.read_text(encoding="utf-8")[:3000]
            m = re.search(r'^short_title:\s*"?(.*?)"?\s*$', content, re.MULTILINE)
            if m:
                titles.add(normalize_title(m.group(1).strip()))
        except Exception:
            pass
    return titles


def normalize_title(title: str) -> str:
    """Normalize title for comparison."""
    return re.sub(r"[^a-z0-9\s]", "", title.lower()).strip()[:80]


# ---------------------------------------------------------------------------
# Semantic Scholar API
# ---------------------------------------------------------------------------
def search_semantic_scholar(query: str, limit: int = 15) -> list[dict]:
    """Search Semantic Scholar for papers matching query."""
    params = urllib.parse.urlencode({
        "query": query,
        "limit": limit,
        "fields": S2_FIELDS,
    })
    url = f"{S2_API}/paper/search?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": "CEI-Literature-Vault/2.0"})

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("data", [])
    except (urllib.error.HTTPError, urllib.error.URLError) as e:
        print(f"  [S2 ERROR] {e}")
        return []
    except Exception as e:
        print(f"  [S2 ERROR] {e}")
        return []


# ---------------------------------------------------------------------------
# arXiv API
# ---------------------------------------------------------------------------
def search_arxiv(query: str, max_results: int = 10) -> list[dict]:
    """Search arXiv for papers."""
    params = urllib.parse.urlencode({
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": max_results,
        "sortBy": "relevance",
    })
    url = f"{ARXIV_API}?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": "CEI-Literature-Vault/2.0"})

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            xml = resp.read().decode("utf-8")
            entries: list[dict] = []
            for entry_match in re.finditer(r"<entry>(.*?)</entry>", xml, re.DOTALL):
                entry_xml = entry_match.group(1)
                title_m = re.search(r"<title>(.*?)</title>", entry_xml, re.DOTALL)
                summary_m = re.search(r"<summary>(.*?)</summary>", entry_xml, re.DOTALL)
                id_m = re.search(r"<id>(.*?)</id>", entry_xml)
                published_m = re.search(r"<published>(.*?)</published>", entry_xml)

                # Extract authors
                authors: list[str] = []
                for author_m in re.finditer(r"<author>.*?<name>(.*?)</name>.*?</author>", entry_xml, re.DOTALL):
                    authors.append(author_m.group(1).strip())
                    if len(authors) >= 5:
                        break

                if title_m:
                    title = re.sub(r"\s+", " ", title_m.group(1)).strip()
                    abstract = re.sub(r"\s+", " ", summary_m.group(1)).strip() if summary_m else ""
                    arxiv_url = id_m.group(1).strip() if id_m else ""
                    year = published_m.group(1)[:4] if published_m else ""

                    entries.append({
                        "title": title,
                        "abstract": abstract[:500],
                        "url": arxiv_url,
                        "year": year,
                        "source": "arXiv",
                        "authors": authors,
                        "citations": 0,
                        "venue": "",
                        "doi": "",
                    })
            return entries
    except Exception as e:
        print(f"  [arXiv ERROR] {e}")
        return []


# ---------------------------------------------------------------------------
# OpenAlex API
# ---------------------------------------------------------------------------
def search_openalex(query: str, limit: int = 15) -> list[dict]:
    """Search OpenAlex for papers."""
    params = urllib.parse.urlencode({
        "search": query,
        "per_page": limit,
        "select": "id,title,publication_year,cited_by_count,doi,primary_location,authorships",
        "mailto": "research@cei-literature.org",
    })
    url = f"{OPENALEX_API}?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": "CEI-Literature-Vault/2.0"})

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            results: list[dict] = []
            for work in data.get("results", []):
                title = work.get("title", "")
                if not title:
                    continue
                authors: list[str] = []
                for auth in (work.get("authorships") or [])[:5]:
                    name = auth.get("author", {}).get("display_name", "")
                    if name:
                        authors.append(name)
                doi_raw = work.get("doi", "") or ""
                doi_clean = doi_raw.replace("https://doi.org/", "") if doi_raw else ""
                loc = work.get("primary_location") or {}
                venue = ""
                if loc.get("source"):
                    venue = loc["source"].get("display_name", "")
                results.append({
                    "title": title,
                    "year": str(work.get("publication_year", "")),
                    "url": doi_raw or work.get("id", ""),
                    "doi": doi_clean,
                    "source": "OpenAlex",
                    "citations": work.get("cited_by_count", 0),
                    "venue": venue,
                    "authors": authors,
                    "abstract": "",  # inverted index reconstruction omitted for simplicity
                })
            return results
    except Exception as e:
        print(f"  [OpenAlex ERROR] {e}")
        return []


# ---------------------------------------------------------------------------
# Per-folder relevance check
# ---------------------------------------------------------------------------
def is_relevant_for_folder(title: str, abstract: str, config: dict) -> bool:
    """Check if a paper is relevant for a specific thematic folder."""
    text = f"{title} {abstract}".lower()
    keywords = config["relevance_keywords"]
    min_kw = config.get("min_keywords", 2)
    hits = sum(1 for kw in keywords if kw.lower() in text)
    return hits >= min_kw


# ---------------------------------------------------------------------------
# Priority heuristic
# ---------------------------------------------------------------------------
def assign_priority(paper: dict) -> str:
    """Assign priority based on citations, venue, and recency."""
    citations = paper.get("citations", 0) or 0
    year = 0
    try:
        year = int(paper.get("year", 0) or 0)
    except (ValueError, TypeError):
        pass
    venue = (paper.get("venue") or "").lower()

    if citations > 100 or any(v in venue for v in TOP_VENUES):
        return "must_read"
    if citations > 20 or year >= 2024:
        return "important"
    return "supplementary"


# ---------------------------------------------------------------------------
# Normalize S2 paper to common format
# ---------------------------------------------------------------------------
def normalize_s2_paper(paper: dict) -> dict:
    """Convert Semantic Scholar API result to common format."""
    return {
        "title": paper.get("title", ""),
        "abstract": (paper.get("abstract") or "")[:500],
        "year": str(paper.get("year", "")),
        "url": paper.get("url", ""),
        "doi": "",
        "source": "Semantic Scholar",
        "citations": paper.get("citationCount", 0),
        "venue": paper.get("venue", ""),
        "authors": [a.get("name", "") for a in (paper.get("authors") or [])[:5]],
        "is_open_access": paper.get("isOpenAccess", False),
        "s2_paper_id": paper.get("paperId", ""),
    }


# ---------------------------------------------------------------------------
# CLI argument parsing
# ---------------------------------------------------------------------------
def parse_args() -> dict:
    """Parse command-line arguments."""
    opts: dict = {
        "folder": None,
        "dry_run": False,
        "seeds_only": False,
    }
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--folder" and i + 1 < len(args):
            opts["folder"] = args[i + 1]
            i += 2
        elif args[i].startswith("--folder="):
            opts["folder"] = args[i].split("=", 1)[1]
            i += 1
        elif args[i] == "--dry-run":
            opts["dry_run"] = True
            i += 1
        elif args[i] == "--seeds-only":
            opts["seeds_only"] = True
            i += 1
        else:
            print(f"Unknown argument: {args[i]}")
            i += 1
    return opts


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    opts = parse_args()
    dry_run = opts["dry_run"]
    seeds_only = opts["seeds_only"]
    folder_filter = opts["folder"]

    print(f"=== Background Literature Search ===")
    print(f"Date: {TODAY}")
    print(f"Folder filter: {folder_filter or 'ALL'}")
    print(f"Dry run: {dry_run}")
    print(f"Seeds only: {seeds_only}")
    print()

    # Load vault titles for dedup
    vault_titles = load_vault_titles()
    print(f"Loaded {len(vault_titles)} vault titles for dedup")

    # Determine which folders to search
    folders_to_search: list[str] = []
    for folder_name in SEARCH_CONFIGS:
        if folder_filter is None:
            folders_to_search.append(folder_name)
        elif folder_name.startswith(folder_filter):
            folders_to_search.append(folder_name)

    if not folders_to_search:
        print(f"ERROR: No folders matched filter '{folder_filter}'")
        print(f"Available: {', '.join(SEARCH_CONFIGS.keys())}")
        sys.exit(1)

    print(f"Searching {len(folders_to_search)} folder(s): {', '.join(folders_to_search)}")
    print()

    all_results: list[dict] = []
    seen_titles: set[str] = set()
    query_log: list[dict] = []
    folder_counts: dict[str, int] = {}

    # -----------------------------------------------------------------------
    # Phase 1: Add expert seeds
    # -----------------------------------------------------------------------
    print(f"{'='*60}")
    print(f"PHASE 1: Expert Seeds")
    print(f"{'='*60}")

    seeds_added = 0
    for seed in EXPERT_SEEDS:
        folder = seed.get("folder", "")
        if folder not in folders_to_search:
            continue

        title = seed.get("title", "")
        norm = normalize_title(title)

        if norm in vault_titles:
            print(f"  [SKIP-VAULT] {title[:60]}")
            continue
        if norm in seen_titles:
            print(f"  [SKIP-DUP] {title[:60]}")
            continue

        seen_titles.add(norm)

        result = {
            "title": title,
            "abstract": seed.get("relevance_note", ""),
            "year": seed.get("year", ""),
            "url": seed.get("url", ""),
            "doi": seed.get("doi", ""),
            "source": "expert_seed",
            "citations": 0,
            "venue": seed.get("source", ""),
            "authors": seed.get("authors", []),
            "folder": folder,
            "priority": seed.get("priority", "must_read"),
            "type": seed.get("type", ""),
            "expert_source": seed.get("expert_source", []),
            "topic_tags": seed.get("topic_tags", []),
            "relevance_note": seed.get("relevance_note", ""),
        }
        all_results.append(result)
        folder_counts[folder] = folder_counts.get(folder, 0) + 1
        seeds_added += 1
        print(f"  [SEED] {folder}: {title[:60]}")

    print(f"\nSeeds added: {seeds_added}")

    if seeds_only:
        # Skip API searches, go straight to output
        print("\n--seeds-only: skipping API searches")
    else:
        # -------------------------------------------------------------------
        # Phase 2: API searches per folder
        # -------------------------------------------------------------------
        print(f"\n{'='*60}")
        print(f"PHASE 2: API Searches")
        print(f"{'='*60}")

        for folder_name in folders_to_search:
            config = SEARCH_CONFIGS[folder_name]
            queries = config["queries"]

            print(f"\n{'─'*50}")
            print(f"FOLDER: {folder_name} ({len(queries)} queries)")
            print(f"{'─'*50}")

            folder_added = 0

            for qi, query in enumerate(queries, 1):
                query_log.append({
                    "folder": folder_name,
                    "query": query,
                    "query_index": qi,
                })

                if dry_run:
                    print(f"  [{qi}/{len(queries)}] [DRY] {query}")
                    continue

                print(f"  [{qi}/{len(queries)}] {query}")

                # --- Semantic Scholar ---
                print(f"    S2...", end=" ")
                s2_results = search_semantic_scholar(query, limit=15)
                s2_added = 0

                for paper in s2_results:
                    if not paper or not paper.get("title"):
                        continue
                    title = paper["title"]
                    norm = normalize_title(title)
                    abstract = paper.get("abstract", "") or ""

                    if norm in seen_titles or norm in vault_titles:
                        continue
                    if not is_relevant_for_folder(title, abstract, config):
                        continue

                    seen_titles.add(norm)
                    result = normalize_s2_paper(paper)
                    result["folder"] = folder_name
                    result["query"] = query
                    result["priority"] = assign_priority(result)
                    all_results.append(result)
                    s2_added += 1
                    folder_added += 1

                print(f"{len(s2_results)} returned, {s2_added} added")
                time.sleep(S2_DELAY)

                # --- arXiv ---
                print(f"    arXiv...", end=" ")
                arxiv_results = search_arxiv(query, max_results=10)
                arxiv_added = 0

                for paper in arxiv_results:
                    if not paper.get("title"):
                        continue
                    title = paper["title"]
                    norm = normalize_title(title)
                    abstract = paper.get("abstract", "") or ""

                    if norm in seen_titles or norm in vault_titles:
                        continue
                    if not is_relevant_for_folder(title, abstract, config):
                        continue

                    seen_titles.add(norm)
                    paper["folder"] = folder_name
                    paper["query"] = query
                    paper["priority"] = assign_priority(paper)
                    all_results.append(paper)
                    arxiv_added += 1
                    folder_added += 1

                print(f"{len(arxiv_results)} returned, {arxiv_added} added")
                time.sleep(ARXIV_DELAY)

                # --- OpenAlex ---
                print(f"    OpenAlex...", end=" ")
                oa_results = search_openalex(query, limit=15)
                oa_added = 0

                for paper in oa_results:
                    if not paper.get("title"):
                        continue
                    title = paper["title"]
                    norm = normalize_title(title)
                    # OpenAlex returns no abstract in this mode
                    abstract = paper.get("abstract", "") or ""

                    if norm in seen_titles or norm in vault_titles:
                        continue
                    if not is_relevant_for_folder(title, abstract, config):
                        continue

                    seen_titles.add(norm)
                    paper["folder"] = folder_name
                    paper["query"] = query
                    paper["priority"] = assign_priority(paper)
                    all_results.append(paper)
                    oa_added += 1
                    folder_added += 1

                print(f"{len(oa_results)} returned, {oa_added} added")
                time.sleep(OPENALEX_DELAY)

            folder_counts[folder_name] = folder_counts.get(folder_name, 0) + folder_added
            print(f"  -> {folder_name}: {folder_added} new papers (total in folder: {folder_counts.get(folder_name, 0)})")

    # -----------------------------------------------------------------------
    # Summary
    # -----------------------------------------------------------------------
    print(f"\n{'='*60}")
    print(f"SEARCH RESULTS SUMMARY")
    print(f"{'='*60}")
    print(f"Total unique results: {len(all_results)}")

    # By folder
    print(f"\nBy folder:")
    for folder in sorted(folder_counts.keys()):
        print(f"  {folder:40s} {folder_counts[folder]}")

    # By source
    source_counts: dict[str, int] = {}
    for r in all_results:
        src = r.get("source", "Unknown")
        source_counts[src] = source_counts.get(src, 0) + 1
    print(f"\nBy source:")
    for src, count in sorted(source_counts.items(), key=lambda x: -x[1]):
        print(f"  {src:25s} {count}")

    # By priority
    priority_counts: dict[str, int] = {}
    for r in all_results:
        pri = r.get("priority", "unset")
        priority_counts[pri] = priority_counts.get(pri, 0) + 1
    print(f"\nBy priority:")
    for pri, count in sorted(priority_counts.items(), key=lambda x: -x[1]):
        print(f"  {pri:25s} {count}")

    # Top results by citations
    cited = sorted(all_results, key=lambda x: -(x.get("citations", 0) or 0))
    print(f"\nTop 20 by citations:")
    for i, r in enumerate(cited[:20], 1):
        cites = r.get("citations", 0) or 0
        print(f"  {i:2d}. [{r.get('source', '?')[:5]:5s}] "
              f"[{r.get('folder', '?')[:25]:25s}] "
              f"cit={cites:5d}  "
              f"{r.get('year', '?'):4s} {r.get('title', '?')[:55]}")

    # -----------------------------------------------------------------------
    # Write output JSON
    # -----------------------------------------------------------------------
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    out_path = DATA_DIR / f"{TODAY}-background-search-results.json"

    output = {
        "generated": TODAY,
        "search_type": "background_literature",
        "total_results": len(all_results),
        "seeds_count": seeds_added,
        "queries_executed": len(query_log),
        "vault_titles_for_dedup": len(vault_titles),
        "folders_searched": folders_to_search,
        "folder_distribution": folder_counts,
        "source_distribution": source_counts,
        "priority_distribution": priority_counts,
        "query_log": query_log if dry_run else [],
        "results": all_results,
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nOutput written: {out_path}")
    print(f"Done.")


if __name__ == "__main__":
    main()
