#!/usr/bin/env python3
"""
Phase 2: External Search for Religious Values Benchmarks

Queries Semantic Scholar, arXiv, and HuggingFace Datasets for religious values
benchmarks not yet in the CEI Literature Vault.

Organized by tradition family to ensure coverage of underrepresented traditions.

Output: RELIGIOUS-VALUES/data/YYYYMMDD-external-search-results.json

Usage:
    python search_external_religious_benchmarks.py [--family FAMILY] [--dry-run]

    --family: Abrahamic, Dharmic, EastAsian, African, Multi (default: all)
    --dry-run: Print queries without executing
"""
from __future__ import annotations

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

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
WS_ROOT = PROJECT_DIR.parent
PAPERS_DIR = WS_ROOT / "papers"
DATA_DIR = PROJECT_DIR / "data"

TODAY = date.today().strftime("%Y%m%d")

# ---------------------------------------------------------------------------
# Search queries organized by tradition family
# ---------------------------------------------------------------------------
SEARCH_QUERIES = {
    "Abrahamic": {
        "Islam": [
            "Islamic ethics benchmark LLM evaluation",
            "Quran question answering dataset",
            "hadith classification NLP dataset",
            "fatwa classification AI benchmark",
            "Islamic jurisprudence AI evaluation",
            "Arabic religious NLP benchmark",
            "Quranic text understanding benchmark",
            "Islamic finance AI evaluation dataset",
        ],
        "Christianity": [
            "theology benchmark LLM evaluation",
            "Bible question answering NLP dataset",
            "Christian ethics AI benchmark evaluation",
            "FaithBench Christian theology benchmark",
            "biblical exegesis NLP dataset",
            "Christian apologetics AI evaluation",
            "religious knowledge benchmark LLM",
        ],
        "Judaism": [
            "Jewish ethics AI benchmark evaluation",
            "Torah NLP computational dataset",
            "Talmud reasoning AI benchmark",
            "rabbinical reasoning computational",
            "Hebrew religious text NLP",
            "Jewish law halakha AI evaluation",
        ],
    },
    "Dharmic": {
        "Hinduism": [
            "Hindu ethics AI benchmark evaluation",
            "Vedic text NLP dataset Sanskrit",
            "Bhagavad Gita dataset AI evaluation",
            "Sanskrit NLP benchmark religious",
            "Dharmic values AI benchmark",
            "Hindu philosophy AI evaluation",
        ],
        "Buddhism": [
            "Buddhist ethics AI evaluation benchmark",
            "BuddhismEval benchmark LLM",
            "Pali NLP Buddhist text dataset",
            "Buddhist philosophy AI benchmark",
            "DharmaBench Buddhist evaluation",
            "Zen koans AI evaluation dataset",
        ],
        "Jainism": [
            "Jain ethics AI benchmark evaluation",
            "Jainism NLP dataset benchmark",
            "ahimsa non-violence AI evaluation",
            "Jain philosophy computational analysis",
        ],
        "Sikhism": [
            "Sikh AI benchmark evaluation",
            "Gurbani NLP dataset benchmark",
            "Guru Granth Sahib dataset AI",
            "Sikh ethics AI evaluation",
            "Punjabi religious text NLP",
        ],
    },
    "EastAsian": {
        "Confucianism": [
            "Confucian ethics AI benchmark evaluation",
            "CValues Chinese moral values benchmark",
            "Chinese Confucian values LLM evaluation",
            "Analects NLP dataset computational",
            "East Asian values AI benchmark",
        ],
        "Taoism": [
            "Taoist philosophy AI dataset benchmark",
            "Tao Te Ching NLP dataset evaluation",
            "Daoist values AI evaluation benchmark",
            "Chinese philosophy AI benchmark religious",
        ],
        "Shinto": [
            "Shinto values AI benchmark evaluation",
            "Japanese religious values AI benchmark",
            "Shinto NLP dataset evaluation",
        ],
    },
    "African": {
        "Ubuntu": [
            "Ubuntu ethics AI benchmark evaluation",
            "African philosophy AI benchmark dataset",
            "Ubuntu philosophy LLM evaluation",
            "African moral values AI benchmark",
            "communitarian ethics AI evaluation",
        ],
        "Indigenous": [
            "Indigenous knowledge AI benchmark evaluation",
            "decolonial AI evaluation benchmark dataset",
            "tikanga Maori AI evaluation",
            "Indigenous spirituality AI benchmark",
            "First Nations values AI evaluation",
            "Aboriginal knowledge NLP dataset",
        ],
    },
    "Multi": {
        "Multi-religion": [
            "religious values LLM benchmark evaluation",
            "interfaith AI evaluation benchmark dataset",
            "spiritual values alignment benchmark LLM",
            "world religions AI evaluation benchmark",
            "cross-cultural religious values benchmark",
            "religion bias LLM evaluation benchmark",
            "comparative religion AI benchmark",
        ],
    },
}

# ---------------------------------------------------------------------------
# Existing vault titles for deduplication
# ---------------------------------------------------------------------------
def load_vault_titles() -> set:
    """Load all paper titles from vault for dedup."""
    titles = set()
    for pf in PAPERS_DIR.iterdir():
        if pf.suffix != ".md":
            continue
        try:
            content = pf.read_text(encoding="utf-8")[:3000]
            m = re.search(r'^short_title:\s*"?(.*?)"?\s*$', content, re.MULTILINE)
            if m:
                titles.add(m.group(1).strip().lower()[:80])
        except Exception:
            pass
    return titles


def normalize_title(title: str) -> str:
    """Normalize title for comparison."""
    return re.sub(r'[^a-z0-9\s]', '', title.lower()).strip()[:80]


# ---------------------------------------------------------------------------
# Semantic Scholar API
# ---------------------------------------------------------------------------
S2_API = "https://api.semanticscholar.org/graph/v1"
S2_FIELDS = "paperId,title,year,citationCount,url,isOpenAccess,openAccessPdf,authors,venue,abstract"
S2_DELAY = 12  # seconds between requests (rate limit)


def search_semantic_scholar(query: str, limit: int = 20) -> list[dict]:
    """Search Semantic Scholar for papers matching query."""
    params = urllib.parse.urlencode({
        "query": query,
        "limit": limit,
        "fields": S2_FIELDS,
    })
    url = f"{S2_API}/paper/search?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": "CEI-Literature-Vault/1.0"})

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("data", [])
    except (urllib.error.HTTPError, urllib.error.URLError, Exception) as e:
        print(f"  [S2 ERROR] {e}")
        return []


# ---------------------------------------------------------------------------
# arXiv API
# ---------------------------------------------------------------------------
ARXIV_API = "http://export.arxiv.org/api/query"
ARXIV_DELAY = 5


def search_arxiv(query: str, max_results: int = 15) -> list[dict]:
    """Search arXiv for papers."""
    params = urllib.parse.urlencode({
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": max_results,
        "sortBy": "relevance",
    })
    url = f"{ARXIV_API}?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": "CEI-Literature-Vault/1.0"})

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            xml = resp.read().decode("utf-8")
            # Simple XML parsing for arXiv entries
            entries = []
            for entry_match in re.finditer(r'<entry>(.*?)</entry>', xml, re.DOTALL):
                entry_xml = entry_match.group(1)
                title_m = re.search(r'<title>(.*?)</title>', entry_xml, re.DOTALL)
                summary_m = re.search(r'<summary>(.*?)</summary>', entry_xml, re.DOTALL)
                id_m = re.search(r'<id>(.*?)</id>', entry_xml)
                published_m = re.search(r'<published>(.*?)</published>', entry_xml)

                if title_m:
                    title = re.sub(r'\s+', ' ', title_m.group(1)).strip()
                    abstract = re.sub(r'\s+', ' ', summary_m.group(1)).strip() if summary_m else ""
                    arxiv_url = id_m.group(1).strip() if id_m else ""
                    year = published_m.group(1)[:4] if published_m else ""

                    entries.append({
                        "title": title,
                        "abstract": abstract,
                        "url": arxiv_url,
                        "year": year,
                        "source": "arXiv",
                    })
            return entries
    except Exception as e:
        print(f"  [arXiv ERROR] {e}")
        return []


# ---------------------------------------------------------------------------
# HuggingFace Datasets API
# ---------------------------------------------------------------------------
HF_API = "https://huggingface.co/api/datasets"
HF_DELAY = 3


def search_huggingface_datasets(query: str, limit: int = 10) -> list[dict]:
    """Search HuggingFace for datasets matching query."""
    params = urllib.parse.urlencode({
        "search": query,
        "limit": limit,
        "sort": "downloads",
        "direction": -1,
    })
    url = f"{HF_API}?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": "CEI-Literature-Vault/1.0"})

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            datasets = json.loads(resp.read().decode("utf-8"))
            results = []
            for ds in datasets:
                results.append({
                    "title": ds.get("id", ""),
                    "abstract": ds.get("description", "")[:500] if ds.get("description") else "",
                    "url": f"https://huggingface.co/datasets/{ds.get('id', '')}",
                    "year": "",
                    "source": "HuggingFace",
                    "downloads": ds.get("downloads", 0),
                    "tags": ds.get("tags", []),
                })
            return results
    except Exception as e:
        print(f"  [HF ERROR] {e}")
        return []


# ---------------------------------------------------------------------------
# Relevance filter
# ---------------------------------------------------------------------------
RELIGIOUS_KEYWORDS = {
    "religion", "religious", "theology", "theological", "faith", "spiritual",
    "scripture", "scriptural", "sacred", "divine",
    "quran", "quranic", "bible", "biblical", "torah", "talmud", "hadith",
    "fatwa", "fiqh", "sharia", "islamic", "muslim",
    "christian", "church", "gospel", "jesus", "christ",
    "jewish", "judaism", "hebrew", "rabbin",
    "hindu", "vedic", "vedanta", "dharma", "gita", "krishna",
    "buddhist", "buddhism", "pali", "zen", "sutra", "dharma",
    "sikh", "gurbani", "guru granth",
    "confucian", "analects", "mencius",
    "taoist", "taoism", "tao",
    "shinto",
    "jain", "jainism", "ahimsa",
    "ubuntu",
    "indigenous", "aboriginal", "maori", "decolonial",
    "interfaith", "inter-faith", "pluralism",
    "moral values", "ethical values", "values alignment",
}

BENCHMARK_KEYWORDS = {
    "benchmark", "dataset", "evaluation", "eval", "test set", "shared task",
    "leaderboard", "question answering", "classification", "NLP",
    "LLM", "language model", "GPT", "BERT", "transformer",
}


def is_relevant(title: str, abstract: str) -> bool:
    """Check if a paper/dataset is relevant to religious values benchmarks."""
    text = f"{title} {abstract}".lower()
    has_religious = any(kw in text for kw in RELIGIOUS_KEYWORDS)
    has_benchmark = any(kw in text for kw in BENCHMARK_KEYWORDS)
    return has_religious and has_benchmark


# ---------------------------------------------------------------------------
# Main search loop
# ---------------------------------------------------------------------------
def main():
    dry_run = "--dry-run" in sys.argv
    target_family = None
    for arg in sys.argv[1:]:
        if arg.startswith("--family="):
            target_family = arg.split("=")[1]
        elif arg == "--family" and sys.argv.index(arg) + 1 < len(sys.argv):
            target_family = sys.argv[sys.argv.index(arg) + 1]

    print(f"=== Phase 2: External Search for Religious Values Benchmarks ===")
    print(f"Target family: {target_family or 'ALL'}")
    print(f"Dry run: {dry_run}")
    print()

    vault_titles = load_vault_titles()
    print(f"Loaded {len(vault_titles)} vault titles for dedup")

    all_results = []
    seen_titles = set()
    query_log = []

    families_to_search = SEARCH_QUERIES.keys() if not target_family else [target_family]

    for family in families_to_search:
        if family not in SEARCH_QUERIES:
            print(f"Unknown family: {family}")
            continue

        print(f"\n{'='*60}")
        print(f"FAMILY: {family}")
        print(f"{'='*60}")

        for tradition, queries in SEARCH_QUERIES[family].items():
            print(f"\n  --- {tradition} ---")

            for query in queries:
                query_log.append({"family": family, "tradition": tradition, "query": query})

                if dry_run:
                    print(f"    [DRY] {query}")
                    continue

                print(f"    Searching: {query}")

                # Semantic Scholar
                s2_results = search_semantic_scholar(query, limit=15)
                time.sleep(S2_DELAY)

                for paper in s2_results:
                    if not paper or not paper.get("title"):
                        continue
                    title = paper["title"]
                    norm = normalize_title(title)
                    abstract = paper.get("abstract", "") or ""

                    if norm in seen_titles or norm in vault_titles:
                        continue
                    if not is_relevant(title, abstract):
                        continue

                    seen_titles.add(norm)
                    all_results.append({
                        "title": title,
                        "abstract": abstract[:500],
                        "year": str(paper.get("year", "")),
                        "url": paper.get("url", ""),
                        "source": "Semantic Scholar",
                        "tradition": tradition,
                        "family": family,
                        "query": query,
                        "citations": paper.get("citationCount", 0),
                        "is_open_access": paper.get("isOpenAccess", False),
                        "venue": paper.get("venue", ""),
                        "s2_paper_id": paper.get("paperId", ""),
                        "authors": [a.get("name", "") for a in (paper.get("authors") or [])[:5]],
                    })

                # arXiv (less frequently to avoid rate limits)
                if "benchmark" in query or "dataset" in query:
                    arxiv_results = search_arxiv(query, max_results=10)
                    time.sleep(ARXIV_DELAY)

                    for paper in arxiv_results:
                        if not paper.get("title"):
                            continue
                        title = paper["title"]
                        norm = normalize_title(title)

                        if norm in seen_titles or norm in vault_titles:
                            continue
                        if not is_relevant(title, paper.get("abstract", "")):
                            continue

                        seen_titles.add(norm)
                        paper["tradition"] = tradition
                        paper["family"] = family
                        paper["query"] = query
                        all_results.append(paper)

                # HuggingFace (targeted)
                if any(kw in query for kw in ["dataset", "benchmark", "NLP"]):
                    hf_short = query.replace("benchmark", "").replace("evaluation", "").strip()
                    hf_results = search_huggingface_datasets(hf_short, limit=5)
                    time.sleep(HF_DELAY)

                    for ds in hf_results:
                        if not ds.get("title"):
                            continue
                        title = ds["title"]
                        norm = normalize_title(title)

                        if norm in seen_titles:
                            continue
                        # HF datasets are all relevant if they come back for religious queries
                        seen_titles.add(norm)
                        ds["tradition"] = tradition
                        ds["family"] = family
                        ds["query"] = query
                        all_results.append(ds)

            print(f"    Results so far: {len(all_results)}")

    # --- Summary ---
    print(f"\n{'='*60}")
    print(f"EXTERNAL SEARCH RESULTS")
    print(f"{'='*60}")
    print(f"Total unique results: {len(all_results)}")

    # By tradition
    trad_counts = {}
    for r in all_results:
        trad = r.get("tradition", "Unknown")
        trad_counts[trad] = trad_counts.get(trad, 0) + 1
    print(f"\nBy tradition:")
    for trad, count in sorted(trad_counts.items(), key=lambda x: -x[1]):
        print(f"  {trad:25s} {count}")

    # By source
    source_counts = {}
    for r in all_results:
        src = r.get("source", "Unknown")
        source_counts[src] = source_counts.get(src, 0) + 1
    print(f"\nBy source:")
    for src, count in sorted(source_counts.items(), key=lambda x: -x[1]):
        print(f"  {src:25s} {count}")

    # Top results
    print(f"\nTop 30 results:")
    for i, r in enumerate(all_results[:30], 1):
        print(f"  {i:2d}. [{r.get('source', '?')[:3]:3s}] [{r.get('tradition', '?'):15s}] "
              f"{r.get('year', '?'):4s} {r.get('title', '?')[:70]}")

    # --- Write output ---
    output = {
        "generated": TODAY,
        "total_results": len(all_results),
        "queries_executed": len(query_log),
        "vault_titles_for_dedup": len(vault_titles),
        "tradition_distribution": trad_counts,
        "source_distribution": source_counts,
        "query_log": query_log if dry_run else [],
        "results": all_results,
    }

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    out_path = DATA_DIR / f"{TODAY}-external-search-results.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nOutput: {out_path}")


if __name__ == "__main__":
    main()
