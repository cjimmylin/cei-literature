#!/usr/bin/env python3
"""
Generate LLM Assessment & Data Availability Report.

Scans all 846 papers for exactly two YAML fields:
  - LLM_assessed: comma-separated canonical model names or "NA"
  - DATA_URL: URL string (possibly comma-separated) or "NA"

Produces a comprehensive Markdown report with model landscape analysis,
data availability breakdowns, co-occurrence matrix, and gap analysis.

Output: STATISTICS/20260212-llm-assessment-data-availability-report.md

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/generate_llm_assessment_report.py
"""

import functools
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

print = functools.partial(print, flush=True)

# ── Paths ──────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
WS_ROOT = SCRIPT_DIR.parent
PAPERS_DIR = WS_ROOT / "papers"
STATS_DIR = WS_ROOT / "STATISTICS"
OUTPUT_FILE = STATS_DIR / "20260216-llm-assessment-data-availability-report.md"

# ── Model Family Map ──────────────────────────────────────────────────────
# Keys = family name, values = list of canonical model names that belong
MODEL_FAMILY_MAP = {
    "OpenAI": [
        "GPT-4", "GPT-4o", "GPT-4o mini", "GPT-4 Turbo", "GPT-3.5",
        "GPT-3", "GPT-2", "ChatGPT", "o1", "o1-mini", "o1-preview",
        "o3", "o3-mini", "text-davinci", "text-davinci-002",
        "text-davinci-003", "InstructGPT", "CODEX", "GPT-5",
    ],
    "Anthropic": [
        "Claude", "Claude-2", "Claude-3", "Claude-3 Opus",
        "Claude-3 Sonnet", "Claude-3 Haiku", "Claude Instant",
    ],
    "Meta": [
        "Llama-3", "Llama-2", "Llama", "LLaMA", "CodeLlama", "OPT",
        "OPT-175B",
    ],
    "Google": [
        "Gemini", "Gemini Pro", "Gemini Ultra", "Gemini Flash",
        "Gemma", "Gemma-2", "PaLM-2", "PaLM", "Flan-T5", "Flan-UL2",
        "LaMDA", "T5", "BARD",
    ],
    "Mistral AI": ["Mistral", "Mixtral"],
    "Alibaba": ["Qwen", "Qwen-2", "Qwen-1.5"],
    "DeepSeek": ["DeepSeek", "DeepSeek-V2", "DeepSeek-Coder"],
    "Microsoft": ["Phi", "Phi-2", "Phi-3"],
    "xAI": ["Grok"],
    "Cohere": ["Cohere", "Command-R", "Command R+", "Aya"],
    "AI21": ["Jurassic", "Jurassic-2", "J2"],
    "Open-source (misc)": [
        "Vicuna", "Alpaca", "Falcon", "BLOOM", "Yi", "Dolly",
        "Zephyr", "WizardLM", "InternLM", "Baichuan", "ChatGLM",
        "GLM", "StableLM", "MPT", "DialoGPT", "Delphi", "ERNIE",
    ],
    "Pre-LLM / Encoder": [
        "BERT", "RoBERTa", "ALBERT", "DeBERTa", "DistilBERT",
        "XLNet", "ELECTRA", "ELMo", "BART",
    ],
    "Embeddings": ["Word2Vec", "GloVe", "FastText"],
}

# Build reverse lookup: model_name (lowercase) → family
_MODEL_TO_FAMILY = {}
for family, models in MODEL_FAMILY_MAP.items():
    for m in models:
        _MODEL_TO_FAMILY[m.lower()] = family

# Proprietary model names (lowercase)
PROPRIETARY_MODELS = {
    "gpt-4", "gpt-4o", "gpt-4o mini", "gpt-4 turbo", "gpt-3.5",
    "gpt-3", "chatgpt", "o1", "o1-mini", "o1-preview", "o3", "o3-mini",
    "text-davinci", "text-davinci-002", "text-davinci-003",
    "instructgpt", "gpt-5",
    "claude", "claude-2", "claude-3", "claude-3 opus", "claude-3 sonnet",
    "claude-3 haiku", "claude instant",
    "gemini", "gemini pro", "gemini ultra", "gemini flash",
    "palm", "palm-2", "lamda", "bard",
    "grok",
    "cohere", "command-r", "command r+",
    "jurassic", "jurassic-2", "j2",
    "ernie",
}

# URL platform classification rules (order matters — first match wins)
URL_PLATFORM_RULES = [
    ("github.com", "GitHub"),
    ("huggingface", "HuggingFace"),
    ("hf.co", "HuggingFace"),
    ("zenodo", "Zenodo"),
    ("osf.io", "OSF"),
    ("kaggle", "Kaggle"),
    ("gitlab", "GitLab"),
    ("doi.org", "DOI/Repository"),
    ("drive.google", "Google Drive"),
    ("figshare", "Figshare"),
    ("dataverse", "Dataverse"),
    ("mendeley", "Mendeley Data"),
    ("paperswithcode", "Papers With Code"),
    ("anonymous", "Anonymous (review)"),
]


# ═══════════════════════════════════════════════════════════════════════════
# SCANNING
# ═══════════════════════════════════════════════════════════════════════════

def scan_all_papers():
    """Read all papers and extract LLM_assessed and DATA_URL fields.

    Returns dict: {filename → {"LLM_assessed": str, "DATA_URL": str}}
    """
    results = {}
    for p in sorted(PAPERS_DIR.glob("*.md")):
        try:
            content = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"  WARN: skipping binary/corrupt file: {p.name}")
            continue

        fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not fm_match:
            continue

        fm = fm_match.group(1)
        llm = "NA"
        url = "NA"
        for line in fm.split("\n"):
            if line.startswith("LLM_assessed:"):
                val = line.split(":", 1)[1].strip()
                # Strip straight and curly quotes
                val = val.strip('"').strip('\u201c').strip('\u201d')
                llm = val if val else "NA"
            elif line.startswith("DATA_URL:"):
                val = line.split(":", 1)[1].strip()
                val = val.strip('"').strip('\u201c').strip('\u201d')
                url = val if val else "NA"

        results[p.name] = {"LLM_assessed": llm, "DATA_URL": url}

    return results


# ═══════════════════════════════════════════════════════════════════════════
# UTILITIES
# ═══════════════════════════════════════════════════════════════════════════

def parse_models(llm_assessed):
    """Split comma-separated model names, filtering NA/empty."""
    if not llm_assessed or llm_assessed.strip().upper() == "NA":
        return []
    models = [m.strip() for m in llm_assessed.split(",") if m.strip()]
    return [m for m in models if m.upper() != "NA"]


def classify_url_platform(url):
    """Classify a single URL string into a hosting platform."""
    lower = url.lower()
    for pattern, platform in URL_PLATFORM_RULES:
        if pattern in lower:
            return platform
    return "Other"


def get_model_family(model_name):
    """Look up the family for a model name (case-insensitive)."""
    return _MODEL_TO_FAMILY.get(model_name.lower(), "Other/Unknown")


def is_proprietary(model_name):
    """Check if a model is proprietary (closed-source)."""
    return model_name.lower() in PROPRIETARY_MODELS


def make_wikilink(filename):
    """Convert filename to Obsidian wikilink."""
    return f"[[{filename[:-3]}]]"


def extract_year(filename):
    """Extract year from filename like '2024-Author-Title.md'."""
    m = re.match(r'^(\d{4})-', filename)
    return int(m.group(1)) if m else 9999


def pct(n, total):
    """Format percentage."""
    if total == 0:
        return "0.0%"
    return f"{100 * n / total:.1f}%"


# ═══════════════════════════════════════════════════════════════════════════
# ANALYSIS FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def analyze_executive_summary(data):
    """Section 1: top-line counts and percentages."""
    total = len(data)
    with_models = sum(1 for d in data.values() if parse_models(d["LLM_assessed"]))
    with_urls = sum(1 for d in data.values() if d["DATA_URL"].strip().upper() != "NA")
    both = sum(
        1 for d in data.values()
        if parse_models(d["LLM_assessed"]) and d["DATA_URL"].strip().upper() != "NA"
    )
    neither = sum(
        1 for d in data.values()
        if not parse_models(d["LLM_assessed"]) and d["DATA_URL"].strip().upper() == "NA"
    )

    return {
        "total": total,
        "with_models": with_models,
        "with_urls": with_urls,
        "both": both,
        "neither": neither,
    }


def analyze_model_landscape(data):
    """Section 2: model frequency, families, proprietary/open, co-occurrence."""
    # 2.1 Model frequency
    model_counter = Counter()
    papers_per_model = defaultdict(list)  # model → [filenames]
    models_per_paper = []  # list of model counts per paper (only papers with models)

    for fn, d in data.items():
        models = parse_models(d["LLM_assessed"])
        if models:
            models_per_paper.append(len(models))
            for m in models:
                model_counter[m] += 1
                papers_per_model[m].append(fn)

    # 2.2 Model family grouping
    family_counter = Counter()
    family_papers = defaultdict(set)  # family → set of filenames
    for fn, d in data.items():
        models = parse_models(d["LLM_assessed"])
        for m in models:
            fam = get_model_family(m)
            family_counter[fam] += 1
            family_papers[fam].add(fn)

    # 2.3 Proprietary vs open-source
    proprietary_count = 0
    opensource_count = 0
    for model, count in model_counter.items():
        if is_proprietary(model):
            proprietary_count += count
        else:
            opensource_count += count

    # Papers that use at least one proprietary model
    papers_with_proprietary = set()
    papers_with_opensource = set()
    for fn, d in data.items():
        models = parse_models(d["LLM_assessed"])
        for m in models:
            if is_proprietary(m):
                papers_with_proprietary.add(fn)
            else:
                papers_with_opensource.add(fn)

    # 2.4 Models per paper distribution
    dist = Counter()
    for count in models_per_paper:
        if count == 1:
            dist["1"] += 1
        elif count <= 3:
            dist["2-3"] += 1
        elif count <= 6:
            dist["4-6"] += 1
        else:
            dist["7+"] += 1

    # 2.5 Co-occurrence matrix (top 12 models)
    top12 = [m for m, _ in model_counter.most_common(12)]
    cooccurrence = defaultdict(lambda: defaultdict(int))
    for fn, d in data.items():
        models = parse_models(d["LLM_assessed"])
        model_set = set(models)
        top_in_paper = [m for m in top12 if m in model_set]
        for i, a in enumerate(top_in_paper):
            for b in top_in_paper[i + 1:]:
                cooccurrence[a][b] += 1
                cooccurrence[b][a] += 1

    return {
        "model_counter": model_counter,
        "family_counter": family_counter,
        "family_papers": family_papers,
        "proprietary_count": proprietary_count,
        "opensource_count": opensource_count,
        "papers_with_proprietary": len(papers_with_proprietary),
        "papers_with_opensource": len(papers_with_opensource),
        "models_per_paper_dist": dist,
        "models_per_paper_raw": models_per_paper,
        "top12": top12,
        "cooccurrence": cooccurrence,
    }


def analyze_data_availability(data):
    """Section 3: URL presence, platforms, overlap with LLM models."""
    total = len(data)
    has_url = {}
    no_url = {}

    for fn, d in data.items():
        if d["DATA_URL"].strip().upper() != "NA":
            has_url[fn] = d
        else:
            no_url[fn] = d

    # Platform breakdown (handle comma-separated URLs)
    platform_counter = Counter()
    for fn, d in has_url.items():
        raw = d["DATA_URL"]
        urls = [u.strip() for u in raw.split(", ") if u.strip()]
        platforms_seen = set()
        for u in urls:
            plat = classify_url_platform(u)
            platforms_seen.add(plat)
        for plat in platforms_seen:
            platform_counter[plat] += 1

    # Overlap: papers with BOTH models AND URLs
    has_models_and_url = sum(
        1 for d in data.values()
        if parse_models(d["LLM_assessed"]) and d["DATA_URL"].strip().upper() != "NA"
    )

    return {
        "total": total,
        "has_url": len(has_url),
        "no_url": len(no_url),
        "platform_counter": platform_counter,
        "has_models_and_url": has_models_and_url,
    }


def analyze_gaps(data):
    """Section 4: gap analysis — models w/o URL, URLs w/o models, underrepresented."""
    models_no_url = []
    urls_no_models = []
    for fn, d in sorted(data.items()):
        has_models = bool(parse_models(d["LLM_assessed"]))
        has_url = d["DATA_URL"].strip().upper() != "NA"
        if has_models and not has_url:
            models_no_url.append(fn)
        elif has_url and not has_models:
            urls_no_models.append(fn)

    # Underrepresented model families (< 5 papers)
    family_paper_count = defaultdict(set)
    for fn, d in data.items():
        for m in parse_models(d["LLM_assessed"]):
            fam = get_model_family(m)
            family_paper_count[fam].add(fn)
    underrepresented = {
        fam: len(papers)
        for fam, papers in sorted(family_paper_count.items())
        if len(papers) < 5
    }

    return {
        "models_no_url": models_no_url,
        "urls_no_models": urls_no_models,
        "underrepresented_families": underrepresented,
    }


# ═══════════════════════════════════════════════════════════════════════════
# REPORT ASSEMBLY
# ═══════════════════════════════════════════════════════════════════════════

def assemble_report(data, summary, landscape, availability, gaps):
    """Join all sections into a complete Markdown report."""
    lines = []
    w = lines.append  # shorthand

    date_str = datetime.now().strftime("%Y-%m-%d")

    # ── Header ──
    w("# LLM Assessment & Data Availability Report")
    w("")
    w(f"> **Generated:** {date_str} | **Papers scanned:** {summary['total']}")
    w("")
    w("---")
    w("")

    # ── Table of Contents ──
    w("## Table of Contents")
    w("")
    w("1. [Executive Summary](#1-executive-summary)")
    w("2. [LLM Model Landscape](#2-llm-model-landscape)")
    w("   - 2.1 Model Frequency Table")
    w("   - 2.2 Model Family Grouping")
    w("   - 2.3 Proprietary vs Open-Source Breakdown")
    w("   - 2.4 Models Per Paper Distribution")
    w("   - 2.5 Model Co-Occurrence Matrix")
    w("3. [Data Availability Analysis](#3-data-availability-analysis)")
    w("   - 3.1 URL Presence Statistics")
    w("   - 3.2 Hosting Platform Breakdown")
    w("   - 3.3 Overlap: LLM Models AND Data URLs")
    w("4. [Gap Analysis](#4-gap-analysis)")
    w("   - 4.1 Papers with LLM Models but No Public Data URL")
    w("   - 4.2 Papers with Data URLs but No LLM Models Identified")
    w("   - 4.3 Underrepresented Model Families")
    w("- [Appendix A: Model Family Normalization Table](#appendix-a-model-family-normalization-table)")
    w("- [Appendix B: Methodology Notes](#appendix-b-methodology-notes)")
    w("")
    w("---")
    w("")

    # ══════════════════════════════════════════════════════════════════════
    # Section 1: Executive Summary
    # ══════════════════════════════════════════════════════════════════════
    w("## 1. Executive Summary")
    w("")
    total = summary["total"]
    w(f"This report analyzes **{total} papers** in the CEI Literature Vault for LLM model assessment")
    w("coverage and public data/benchmark availability.")
    w("")
    w("| Metric | Count | % of Total |")
    w("|--------|------:|:----------:|")
    w(f"| Papers with LLM models identified | {summary['with_models']} | {pct(summary['with_models'], total)} |")
    w(f"| Papers with no LLM models (NA) | {total - summary['with_models']} | {pct(total - summary['with_models'], total)} |")
    w(f"| Papers with public data URL | {summary['with_urls']} | {pct(summary['with_urls'], total)} |")
    w(f"| Papers with no data URL (NA) | {total - summary['with_urls']} | {pct(total - summary['with_urls'], total)} |")
    w(f"| Papers with **both** models + URL | {summary['both']} | {pct(summary['both'], total)} |")
    w(f"| Papers with **neither** | {summary['neither']} | {pct(summary['neither'], total)} |")
    w("")

    # Unique model count
    n_unique = len(landscape["model_counter"])
    n_families = len(landscape["family_counter"])
    w(f"- **{n_unique} unique model names** across **{n_families} model families** detected")
    if landscape["models_per_paper_raw"]:
        avg_models = sum(landscape["models_per_paper_raw"]) / len(landscape["models_per_paper_raw"])
        max_models = max(landscape["models_per_paper_raw"])
        w(f"- Average models per paper (among assessed papers): **{avg_models:.1f}** (max: {max_models})")
    w("")
    w("---")
    w("")

    # ══════════════════════════════════════════════════════════════════════
    # Section 2: LLM Model Landscape
    # ══════════════════════════════════════════════════════════════════════
    w("## 2. LLM Model Landscape")
    w("")

    # 2.1 Model Frequency Table
    w("### 2.1 Model Frequency Table")
    w("")
    w("All unique models ranked by number of papers mentioning them:")
    w("")
    w("| Rank | Model | Papers | Family |")
    w("|-----:|-------|-------:|--------|")
    for rank, (model, count) in enumerate(landscape["model_counter"].most_common(), 1):
        family = get_model_family(model)
        w(f"| {rank} | {model} | {count} | {family} |")
    w("")

    # 2.2 Model Family Grouping
    w("### 2.2 Model Family Grouping")
    w("")
    w("Papers per model family (a paper is counted once per family even if it uses multiple models from that family):")
    w("")
    w("| Rank | Family | Papers | % of Assessed |")
    w("|-----:|--------|-------:|--------------:|")
    papers_with_models = summary["with_models"]
    sorted_families = sorted(
        landscape["family_papers"].items(),
        key=lambda x: len(x[1]),
        reverse=True,
    )
    for rank, (fam, paper_set) in enumerate(sorted_families, 1):
        n = len(paper_set)
        w(f"| {rank} | {fam} | {n} | {pct(n, papers_with_models)} |")
    w("")

    # 2.3 Proprietary vs Open-Source
    w("### 2.3 Proprietary vs Open-Source Breakdown")
    w("")
    total_mentions = landscape["proprietary_count"] + landscape["opensource_count"]
    w("**By model mention count** (each model×paper counts once):")
    w("")
    w("| Category | Mentions | % |")
    w("|----------|--------:|---------:|")
    w(f"| Proprietary (closed-source) | {landscape['proprietary_count']} | {pct(landscape['proprietary_count'], total_mentions)} |")
    w(f"| Open-source / open-weight | {landscape['opensource_count']} | {pct(landscape['opensource_count'], total_mentions)} |")
    w(f"| **Total** | **{total_mentions}** | **100%** |")
    w("")
    w("**By paper count** (papers using at least one model of that type):")
    w("")
    w("| Category | Papers |")
    w("|----------|-------:|")
    w(f"| Uses at least one proprietary model | {landscape['papers_with_proprietary']} |")
    w(f"| Uses at least one open-source model | {landscape['papers_with_opensource']} |")
    w("")

    # 2.4 Models Per Paper Distribution
    w("### 2.4 Models Per Paper Distribution")
    w("")
    w(f"Among the {papers_with_models} papers with LLM models identified:")
    w("")
    w("| Models per paper | Papers | % |")
    w("|:----------------:|-------:|------:|")
    for bucket in ["1", "2-3", "4-6", "7+"]:
        n = landscape["models_per_paper_dist"].get(bucket, 0)
        w(f"| {bucket} | {n} | {pct(n, papers_with_models)} |")
    w("")

    # 2.5 Co-occurrence matrix
    w("### 2.5 Model Co-Occurrence Matrix (Top 12)")
    w("")
    w("How often the top 12 models appear together in the same paper:")
    w("")
    top12 = landscape["top12"]
    cooc = landscape["cooccurrence"]

    # Abbreviate names for header
    abbrev = []
    for m in top12:
        if len(m) > 8:
            abbrev.append(m[:7] + ".")
        else:
            abbrev.append(m)

    # Header row
    header = "| | " + " | ".join(abbrev) + " |"
    w(header)
    sep = "|---|" + "|".join(["---:" for _ in top12]) + "|"
    w(sep)
    for i, m in enumerate(top12):
        row_cells = []
        for j, n in enumerate(top12):
            if i == j:
                row_cells.append("—")
            else:
                val = cooc.get(m, {}).get(n, 0)
                row_cells.append(str(val) if val > 0 else "·")
        w(f"| **{abbrev[i]}** | " + " | ".join(row_cells) + " |")
    w("")

    w("---")
    w("")

    # ══════════════════════════════════════════════════════════════════════
    # Section 3: Data Availability Analysis
    # ══════════════════════════════════════════════════════════════════════
    w("## 3. Data Availability Analysis")
    w("")

    # 3.1 URL Presence
    w("### 3.1 URL Presence Statistics")
    w("")
    w("| Status | Papers | % |")
    w("|--------|-------:|------:|")
    w(f"| Has public data URL | {availability['has_url']} | {pct(availability['has_url'], total)} |")
    w(f"| No data URL (NA) | {availability['no_url']} | {pct(availability['no_url'], total)} |")
    w("")

    # 3.2 Hosting Platform Breakdown
    w("### 3.2 Hosting Platform Breakdown")
    w("")
    w("Among papers with data URLs, classified by hosting platform:")
    w("")
    w("| Platform | Papers | % of URLs |")
    w("|----------|-------:|----------:|")
    for platform, count in availability["platform_counter"].most_common():
        w(f"| {platform} | {count} | {pct(count, availability['has_url'])} |")
    w("")

    # 3.3 Overlap
    w("### 3.3 Overlap: LLM Models AND Data URLs")
    w("")
    w("| Combination | Papers | % |")
    w("|-------------|-------:|------:|")
    models_and_url = availability["has_models_and_url"]
    models_no_url = len(gaps["models_no_url"])
    urls_no_models = len(gaps["urls_no_models"])
    w(f"| LLM models + data URL | {models_and_url} | {pct(models_and_url, total)} |")
    w(f"| LLM models only (no URL) | {models_no_url} | {pct(models_no_url, total)} |")
    w(f"| Data URL only (no models) | {urls_no_models} | {pct(urls_no_models, total)} |")
    w(f"| Neither | {summary['neither']} | {pct(summary['neither'], total)} |")
    w("")
    w("---")
    w("")

    # ══════════════════════════════════════════════════════════════════════
    # Section 4: Gap Analysis
    # ══════════════════════════════════════════════════════════════════════
    w("## 4. Gap Analysis")
    w("")

    # 4.1 Models but no URL
    w("### 4.1 Papers with LLM Models but No Public Data URL")
    w("")
    w(f"**{len(gaps['models_no_url'])} papers** assess LLM models but have no publicly available data URL.")
    w("")
    if gaps["models_no_url"]:
        w("<details>")
        w(f"<summary>Click to expand ({len(gaps['models_no_url'])} papers)</summary>")
        w("")
        w("| # | Paper | Models |")
        w("|--:|-------|--------|")
        for i, fn in enumerate(gaps["models_no_url"], 1):
            models_str = data[fn]["LLM_assessed"]
            # Truncate long model lists for readability
            if len(models_str) > 60:
                models_str = models_str[:57] + "..."
            w(f"| {i} | {make_wikilink(fn)} | {models_str} |")
        w("")
        w("</details>")
    w("")

    # 4.2 URLs but no models
    w("### 4.2 Papers with Data URLs but No LLM Models Identified")
    w("")
    w(f"**{len(gaps['urls_no_models'])} papers** have public data URLs but no LLM model assessment.")
    w("")
    if gaps["urls_no_models"]:
        w("<details>")
        w(f"<summary>Click to expand ({len(gaps['urls_no_models'])} papers)</summary>")
        w("")
        w("| # | Paper | Data URL |")
        w("|--:|-------|----------|")
        for i, fn in enumerate(gaps["urls_no_models"], 1):
            url = data[fn]["DATA_URL"]
            if len(url) > 70:
                url = url[:67] + "..."
            w(f"| {i} | {make_wikilink(fn)} | {url} |")
        w("")
        w("</details>")
    w("")

    # 4.3 Underrepresented families
    w("### 4.3 Underrepresented Model Families (< 5 papers)")
    w("")
    underrep = gaps["underrepresented_families"]
    if underrep:
        w(f"**{len(underrep)} model families** appear in fewer than 5 papers:")
        w("")
        w("| Family | Papers |")
        w("|--------|-------:|")
        for fam, count in sorted(underrep.items(), key=lambda x: x[1], reverse=True):
            w(f"| {fam} | {count} |")
    else:
        w("All model families appear in 5 or more papers.")
    w("")
    w("---")
    w("")

    # ══════════════════════════════════════════════════════════════════════
    # Appendix A: Model Family Normalization Table
    # ══════════════════════════════════════════════════════════════════════
    w("## Appendix A: Model Family Normalization Table")
    w("")
    w("Canonical mapping used to group model names into families:")
    w("")
    w("| Family | Models |")
    w("|--------|--------|")
    for family, models in MODEL_FAMILY_MAP.items():
        w(f"| {family} | {', '.join(models)} |")
    w("")

    # ══════════════════════════════════════════════════════════════════════
    # Appendix B: Methodology Notes
    # ══════════════════════════════════════════════════════════════════════
    w("## Appendix B: Methodology Notes")
    w("")
    w("1. **Data source:** YAML frontmatter fields `LLM_assessed` and `DATA_URL` from all 846 papers in `papers/`")
    w("2. **Model extraction:** The `LLM_assessed` field contains comma-separated canonical model names assigned during")
    w("   the 40-agent deep-read enrichment pipeline (2026-02-12). Values are pre-canonicalized — this report")
    w("   performs no additional NLP extraction.")
    w("3. **Family grouping:** Models are mapped to families via a static lookup table (Appendix A). Models not")
    w("   found in the table are assigned to \"Other/Unknown\".")
    w("4. **Proprietary vs open-source:** Classification is based on model licensing at time of release.")
    w("   Some models (e.g., Llama) have evolving licenses; we classify based on the predominant usage pattern.")
    w("5. **URL classification:** DATA_URL values may contain multiple comma-separated URLs. Each paper is counted")
    w("   once per platform (even if multiple URLs point to the same platform).")
    w("6. **Co-occurrence matrix:** Counts how many papers test both Model A and Model B. Only the top 12 models")
    w("   by frequency are included to keep the matrix readable.")
    w("")

    return "\n".join(lines)


# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("LLM Assessment & Data Availability Report Generator")
    print("=" * 60)

    # Step 1: Scan papers
    print(f"\n[1/5] Scanning papers in {PAPERS_DIR} ...")
    data = scan_all_papers()
    print(f"  Scanned {len(data)} papers")

    # Step 2: Executive summary
    print("[2/5] Computing executive summary ...")
    summary = analyze_executive_summary(data)
    print(f"  With models: {summary['with_models']}/{summary['total']}")
    print(f"  With URLs:   {summary['with_urls']}/{summary['total']}")

    # Step 3: Model landscape
    print("[3/5] Analyzing model landscape ...")
    landscape = analyze_model_landscape(data)
    print(f"  Unique models: {len(landscape['model_counter'])}")
    print(f"  Top 5: {', '.join(m for m, _ in landscape['model_counter'].most_common(5))}")

    # Step 4: Data availability
    print("[4/5] Analyzing data availability ...")
    availability = analyze_data_availability(data)
    print(f"  Has URL: {availability['has_url']}/{availability['total']}")
    top_plat = availability["platform_counter"].most_common(3)
    print(f"  Top platforms: {', '.join(f'{p}({c})' for p, c in top_plat)}")

    # Step 5: Gap analysis
    print("[5/5] Running gap analysis ...")
    gaps = analyze_gaps(data)
    print(f"  Models but no URL: {len(gaps['models_no_url'])}")
    print(f"  URLs but no models: {len(gaps['urls_no_models'])}")
    print(f"  Underrepresented families: {len(gaps['underrepresented_families'])}")

    # Assemble report
    print("\nAssembling report ...")
    report = assemble_report(data, summary, landscape, availability, gaps)

    # Write output
    STATS_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(report, encoding="utf-8")
    line_count = report.count("\n") + 1
    print(f"\n{'=' * 60}")
    print(f"Report written to: {OUTPUT_FILE}")
    print(f"Lines: {line_count}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
