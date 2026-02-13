#!/usr/bin/env python3
"""
Generate comprehensive vault overview report for Values Alignment Benchmarks.

Processes existing JSON classification data (20-agent deep-read results) to produce
a multi-dimensional Markdown report covering benchmark taxonomy, model coverage,
cultural/pluralistic analysis, gap analysis, and actionable recommendations.

Data sources:
  - logs/20260208-benchmark_survey_all_classifications.json (924 entries)
  - logs/20260208-benchmark_survey_candidates.json (528 entries)
  - logs/20260207-normative_v2_all_classifications.json (266 entries)
  - logs/20260208-author_paper_map.json (846 entries)
  - papers/*.md YAML frontmatter: LLM_assessed, DATA_URL fields (846 papers)

Output: STATISTICS/20260212-vault-overview-report.md
"""

import json
import re
import sys
import functools
from collections import defaultdict, Counter
from pathlib import Path

print = functools.partial(print, flush=True)

# ── Paths ──────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
WS_ROOT = SCRIPT_DIR.parent
LOGS_DIR = WS_ROOT / "logs"
STATS_DIR = WS_ROOT / "STATISTICS"

ALL_CLASSIFICATIONS_FILE = LOGS_DIR / "20260208-benchmark_survey_all_classifications.json"
CANDIDATES_FILE = LOGS_DIR / "20260208-benchmark_survey_candidates.json"
NORMATIVE_FILE = LOGS_DIR / "20260207-normative_v2_all_classifications.json"
AUTHOR_MAP_FILE = LOGS_DIR / "20260208-author_paper_map.json"
OUTPUT_FILE = STATS_DIR / "20260213-vault-overview-report.md"

# ── Paper YAML scanner (for LLM assessment data) ─────────────────────────
PAPERS_DIR = WS_ROOT / "papers"


def scan_paper_yaml_fields():
    """Scan all papers for LLM_assessed and DATA_URL fields."""
    results = {}
    for p in sorted(PAPERS_DIR.glob("*.md")):
        content = p.read_text(encoding="utf-8")
        fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not fm_match:
            continue
        fm = fm_match.group(1)
        llm = "NA"
        url = "NA"
        for line in fm.split("\n"):
            if line.startswith("LLM_assessed:"):
                llm = line.split(":", 1)[1].strip().strip('"')
            elif line.startswith("DATA_URL:"):
                url = line.split(":", 1)[1].strip().strip('"')
        results[p.name] = {"LLM_assessed": llm, "DATA_URL": url}
    return results


def analyze_llm_assessment(paper_yaml):
    """Analyze LLM assessment coverage across all papers."""
    total = len(paper_yaml)
    papers_with_models = {fn: d for fn, d in paper_yaml.items() if d["LLM_assessed"] != "NA"}
    papers_with_urls = {fn: d for fn, d in paper_yaml.items() if d["DATA_URL"] != "NA"}

    # Model frequency counts (split comma-separated values)
    model_counter = Counter()
    for fn, d in papers_with_models.items():
        models = [m.strip() for m in d["LLM_assessed"].split(",") if m.strip()]
        for m in models:
            model_counter[m] += 1

    # DATA_URL repository distribution
    repo_counter = Counter()
    for fn, d in papers_with_urls.items():
        url = d["DATA_URL"].lower()
        if "github.com" in url:
            repo_counter["GitHub"] += 1
        elif "huggingface" in url or "hf.co" in url:
            repo_counter["HuggingFace"] += 1
        elif "zenodo" in url:
            repo_counter["Zenodo"] += 1
        elif "osf.io" in url:
            repo_counter["OSF"] += 1
        elif "kaggle" in url:
            repo_counter["Kaggle"] += 1
        else:
            repo_counter["Other"] += 1

    # Year-based assessment counts
    assessed_by_year = Counter()
    not_assessed_by_year = Counter()
    for fn, d in paper_yaml.items():
        year = extract_year(fn)
        if year == 9999:
            continue
        if d["LLM_assessed"] != "NA":
            assessed_by_year[year] += 1
        else:
            not_assessed_by_year[year] += 1

    return {
        "total": total,
        "with_models": len(papers_with_models),
        "with_urls": len(papers_with_urls),
        "model_counter": model_counter,
        "repo_counter": repo_counter,
        "assessed_by_year": assessed_by_year,
        "not_assessed_by_year": not_assessed_by_year,
    }

# ── Import CATEGORIES and classify_entry from existing report generator ────
sys.path.insert(0, str(SCRIPT_DIR))
from generate_benchmark_survey_report import CATEGORIES, classify_entry, extract_year

# ═══════════════════════════════════════════════════════════════════════════
# A. FREE-TEXT NORMALIZATION ENGINE
# ═══════════════════════════════════════════════════════════════════════════

# A1. Model Family Extraction
# Each key is the canonical family name; values are regex patterns (case-insensitive)
MODEL_FAMILIES = {
    "GPT-4": r"\bgpt[\s\-_]?4\b",
    "GPT-3.5": r"\bgpt[\s\-_]?3\.?5\b|\bchatgpt\b",
    "GPT-3": r"\bgpt[\s\-_]?3\b(?!\.?5)",
    "GPT-2": r"\bgpt[\s\-_]?2\b",
    "Claude": r"\bclaude\b",
    "Llama": r"\bll?ama[\s\-_]?\d?\b",
    "Gemini": r"\bgemini\b|\bgemma\b",
    "Mistral/Mixtral": r"\bmistral\b|\bmixtral\b",
    "Qwen": r"\bqwen\b",
    "DeepSeek": r"\bdeepseek\b",
    "BERT family": r"\bbert\b|\broberta\b|\balbert\b|\bdeberta\b|\belectra\b",
    "T5/Flan": r"\b(?:flan[\s\-_]?)?t5\b|\bflan\b",
    "Falcon": r"\bfalcon\b",
    "Phi": r"\bphi[\s\-_]?\d\b",
    "Vicuna": r"\bvicuna\b",
    "BLOOM": r"\bbloom\b(?!berg)",
    "OPT": r"\bopt[\s\-_]\d|\bopt\b(?=[\s,\-]|\Z)",
    "PaLM": r"\bpalm\b|\bpalm[\s\-_]?2\b",
    "Cohere": r"\bcohere\b|\bcommand[\s\-_]?r\b",
    "Word2Vec/GloVe": r"\bword2vec\b|\bglove\b|\bfasttext\b",
    "Delphi": r"\bdelphi\b",
    "Alpaca": r"\balpaca\b",
    "Aya": r"\baya\b",
    "Baichuan": r"\bbaichuan\b",
    "Yi": r"\b(?:yi[\s\-_]?\d|yi\b(?=[\s,]))",
    "InternLM": r"\binternlm\b",
    "ChatGLM": r"\bchatglm\b|\bglm\b",
    "WizardLM": r"\bwizardlm\b",
    "Anthropic models": r"\banthropic\b.*(?:model|language|assistant)",
    "DialoGPT": r"\bdialogpt\b",
    "Zephyr": r"\bzephyr\b",
    "StableLM": r"\bstablelm\b|\bstable[\s\-_]?lm\b",
    "MPT": r"\bmpt[\s\-_]?\d",
    "Gemma": r"\bgemma\b(?!.*gemini)",
    "OpenAI (unspecified)": r"\bopenai\b.*(?:model|api)",
    "Jurassic/AI21": r"\bjurassic\b|\bai21\b|\bj2\b",
}

# Compile all regexes
_MODEL_PATTERNS = {k: re.compile(v, re.IGNORECASE) for k, v in MODEL_FAMILIES.items()}


def extract_model_families(text):
    """Extract recognized model families from free-text."""
    if not text:
        return []
    families = []
    for name, pat in _MODEL_PATTERNS.items():
        if pat.search(text):
            families.append(name)
    return families


# A2. Methodology Type Extraction
METHODOLOGY_TYPES = {
    "Multiple-choice QA": r"multiple[\s\-]?choice|MCQ|multi[\s\-]?choice|forced[\s\-]?choice.*(?:question|answer)|choose.*(?:best|correct)|answer.*(?:selection|option)",
    "Scenario/vignette judgment": r"scenario|vignette|moral dilemma|trolley|ethical dilemma|thought experiment|situation",
    "Free-text generation": r"free[\s\-]?(?:text|form)|open[\s\-]?ended.*generat|text generation|natural language generation|generat.*(?:response|text|answer)",
    "Adversarial/red-teaming": r"adversarial|red[\s\-]?team|jailbreak|attack|prompt injection|bypass",
    "Classification task": r"classif(?:y|ication)|categori[zs]|label(?:ing|ed)|detect(?:ion|ing)|binary.*(?:classif|task)|sentiment.*classif",
    "Human preference/comparison": r"human.*prefer|prefer.*(?:pair|comparison|ranking)|crowdsourc.*(?:annotat|judgment|evaluat)|pairwise.*comparison|human.*judg|human.*evaluat",
    "Template/probing": r"template|prob(?:e|ing)|fill[\s\-]?in|cloze|mask(?:ed|ing)|counterfactual",
    "Likert/scale rating": r"likert|rating.*scale|scale.*(?:\d[\s\-]point|\d[\s\-]level)|numerical.*rating|score.*(?:1.*5|1.*7|1.*10)",
    "Multi-turn dialogue": r"multi[\s\-]?turn|dialogue|dialog|conversation|chat.*(?:based|eval|bench)",
    "Game/simulation": r"game|simulat|interactive.*(?:environ|scenar|platform)|reward.*(?:shaping|model.*game)",
    "Survey/questionnaire": r"survey|questionnaire|poll|world value survey|pew.*research|opinion.*(?:survey|poll)",
    "Embedding analysis": r"embedding.*(?:analy|bias|space|associat)|word.*(?:embedding|vector).*(?:bias|fair)|WEAT|SEAT|cosine.*(?:similar|bias)",
    "Crowdsourced annotation": r"crowdsourc|(?:amazon|mturk).*mechanical.*turk|annotator|annotation.*(?:task|pipeline)|inter[\s\-]?annotator",
    "Benchmark suite (multi-task)": r"benchmark.*suite|multi[\s\-]?task|(?:comprehensive|holistic|unified).*(?:bench|evaluat|framework)|suite.*(?:of|across).*task",
}

_METHODOLOGY_PATTERNS = {k: re.compile(v, re.IGNORECASE) for k, v in METHODOLOGY_TYPES.items()}


def extract_methodology_types(entry):
    """Extract methodology types from how_measures + reasoning fields."""
    text = " ".join([
        entry.get("how_measures", ""),
        entry.get("what_measures", ""),
        entry.get("reasoning", ""),
    ])
    if not text.strip():
        return []
    methods = []
    for name, pat in _METHODOLOGY_PATTERNS.items():
        if pat.search(text):
            methods.append(name)
    return methods


# A3. Cultural/Language Detection
ETHICAL_TRADITIONS = {
    "Confucian": r"\bconfucian\b|\bconfucius\b|\bmencius\b|\brunren\b|\bli\b(?=.*ritual)|five.*(?:relationship|constant)",
    "Islamic": r"\bislam(?:ic)?\b|\bsharia\b|\bquran\b|\bhadith\b|\bfiqh\b|\bmaqasid\b|\bhalal\b|\bharam\b",
    "Buddhist": r"\bbuddhis[mt]\b|\bdharma\b|\bkarma\b|\bahimsa\b|\bfour.*noble.*truth",
    "Ubuntu": r"\bubuntu\b(?!.*(?:linux|operat))",
    "Hindu": r"\bhindu(?:ism)?\b|\bvedic\b|\bdharma\b|\bkarma\b",
    "Indigenous": r"\bindigenous\b|\bfirst.*nation\b|\baboriginal\b|\bnative.*(?:people|ethic|value)",
    "Virtue Ethics (Western)": r"\bvirtue.*ethic\b|\baristot(?:le|elian)\b|\beudaimonia\b|\bcharacter.*ethic\b|\bphronesis\b",
    "Deontological": r"\bdeontolog\b|\bkantian\b|\bcategorical.*imperative\b|\bduty[\s\-]?based\b",
    "Consequentialist": r"\bconsequential\b|\butilitarian\b|\bgreatest.*(?:good|happin)\b|\bwelfare.*maximiz",
    "Care Ethics": r"\bcare.*ethic\b|\bfeminist.*ethic\b|\bethic.*of.*care\b|\brelational.*ethic\b",
}

_TRADITION_PATTERNS = {k: re.compile(v, re.IGNORECASE) for k, v in ETHICAL_TRADITIONS.items()}


def extract_traditions(entry):
    """Extract ethical tradition mentions from entry text."""
    text = " ".join([
        entry.get("what_measures", ""),
        entry.get("reasoning", ""),
        entry.get("benchmark_name", ""),
        entry.get("normative_frameworks", ""),
    ])
    if not text.strip():
        return []
    return [name for name, pat in _TRADITION_PATTERNS.items() if pat.search(text)]


LANGUAGES = {
    "English": r"\benglish\b",
    "Chinese": r"\bchinese\b|\bmandarin\b|\bcantonese\b",
    "Arabic": r"\barabic\b",
    "Korean": r"\bkorean\b",
    "Japanese": r"\bjapanese\b",
    "Hindi": r"\bhindi\b",
    "Spanish": r"\bspanish\b",
    "German": r"\bgerman\b",
    "French": r"\bfrench\b",
    "Turkish": r"\bturkish\b",
    "Indonesian": r"\bindonesian\b|\bmalay\b",
    "Portuguese": r"\bportuguese\b|\bbrazilian\b",
    "Russian": r"\brussian\b",
    "Vietnamese": r"\bvietnamese\b",
    "Thai": r"\bthai\b",
    "Swahili": r"\bswahili\b",
    "Urdu": r"\burdu\b",
    "Bengali": r"\bbengali\b|\bbangla\b",
    "Italian": r"\bitalian\b",
    "Dutch": r"\bdutch\b",
}

_LANGUAGE_PATTERNS = {k: re.compile(v, re.IGNORECASE) for k, v in LANGUAGES.items()}


def extract_languages(entry):
    """Extract language mentions from entry text."""
    text = " ".join([
        entry.get("what_measures", ""),
        entry.get("how_measures", ""),
        entry.get("reasoning", ""),
        entry.get("benchmark_name", ""),
    ])
    if not text.strip():
        return []
    return [name for name, pat in _LANGUAGE_PATTERNS.items() if pat.search(text)]


# A4. Availability parsing
def parse_availability(val):
    """Parse availability string into (category, url)."""
    v = (val or "N/A").strip()
    url = None
    url_match = re.search(r'(https?://[^\s\)]+)', v)
    if url_match:
        url = url_match.group(1).rstrip(".,;)")

    if v.startswith("Public"):
        return ("Public", url)
    if v.startswith("Code") or "code available" in v.lower():
        return ("Code available", url)
    if "not stated" in v.lower() or "not specified" in v.lower():
        return ("Not stated", url)
    if "not public" in v.lower():
        return ("Not public", url)
    if "partial" in v.lower():
        return ("Partially public", url)
    return ("Not stated", url)


# A5. Dataset size parsing
def parse_dataset_size(val):
    """Extract numeric magnitude from dataset size string. Returns (number, unit) or None."""
    if not val or val.strip().lower() in ("n/a", "not stated", "not specified", "not explicitly stated"):
        return None
    # Look for patterns like "1,234 examples", "40 million decisions", "2.5K items"
    m = re.search(r'([\d,]+(?:\.\d+)?)\s*(million|mil|m|thousand|k|billion|b)?\s*(\w+)?', val, re.IGNORECASE)
    if m:
        num_str = m.group(1).replace(",", "")
        try:
            num = float(num_str)
        except ValueError:
            return None
        multiplier = m.group(2)
        if multiplier:
            ml = multiplier.lower()
            if ml in ("million", "mil", "m"):
                num *= 1_000_000
            elif ml in ("thousand", "k"):
                num *= 1_000
            elif ml in ("billion", "b"):
                num *= 1_000_000_000
        unit = m.group(3) or "items"
        return (int(num), unit)
    return None


# ═══════════════════════════════════════════════════════════════════════════
# B. CROSS-TABULATION HELPER
# ═══════════════════════════════════════════════════════════════════════════

def make_crosstab_table(row_label, col_label, row_keys, col_keys, matrix, show_totals=True):
    """
    Generate a Markdown cross-tabulation table.

    Args:
        row_label: Header for row dimension
        col_label: (unused, implicit in column headers)
        row_keys: Ordered list of row keys
        col_keys: Ordered list of column keys
        matrix: dict-of-dicts {row_key: {col_key: count}}
        show_totals: Whether to add Total row/column
    Returns:
        List of Markdown lines
    """
    lines = []
    # Header
    header_cols = [row_label] + list(col_keys)
    if show_totals:
        header_cols.append("Total")
    lines.append("| " + " | ".join(str(c) for c in header_cols) + " |")
    lines.append("|" + "|".join("---" for _ in header_cols) + "|")

    # Rows
    col_totals = Counter()
    for rk in row_keys:
        row_vals = []
        row_total = 0
        for ck in col_keys:
            v = matrix.get(rk, {}).get(ck, 0)
            row_vals.append(str(v) if v > 0 else "-")
            col_totals[ck] += v
            row_total += v
        row = [rk] + row_vals
        if show_totals:
            row.append(str(row_total))
        lines.append("| " + " | ".join(str(c) for c in row) + " |")

    # Total row
    if show_totals:
        total_row = ["**Total**"]
        grand = 0
        for ck in col_keys:
            total_row.append(str(col_totals[ck]))
            grand += col_totals[ck]
        total_row.append(f"**{grand}**")
        lines.append("| " + " | ".join(str(c) for c in total_row) + " |")

    return lines


# ═══════════════════════════════════════════════════════════════════════════
# C. ANALYSIS FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def analyze_landscape(all_entries, candidates, author_map):
    """Section 2: Landscape overview."""
    total = len(all_entries)
    n_candidates = len(candidates)
    n_excluded = total - n_candidates

    # Year distribution
    year_counts = Counter()
    for e in all_entries:
        y = extract_year(e["filename"])
        if y != 9999:
            year_counts[y] += 1

    cand_year_counts = Counter()
    for e in candidates:
        y = extract_year(e["filename"])
        if y != 9999:
            cand_year_counts[y] += 1

    # Top prolific first authors
    author_counter = Counter()
    for stem, info in author_map.items():
        fa = info.get("first_author", "Unknown")
        author_counter[fa] += 1
    top_authors = author_counter.most_common(15)

    return {
        "total": total,
        "candidates": n_candidates,
        "excluded": n_excluded,
        "year_counts": year_counts,
        "cand_year_counts": cand_year_counts,
        "top_authors": top_authors,
        "n_authors": len(author_map),
    }


def analyze_benchmark_taxonomy(candidates):
    """Section 3: Benchmark taxonomy (10 categories)."""
    cat_order = sorted(CATEGORIES.keys(), key=lambda c: int(c.split(".")[0]))

    entry_cats = {}
    cat_entries = defaultdict(list)
    uncategorized = []

    for e in candidates:
        cats = classify_entry(e)
        if not cats:
            # Fallback (same as original report)
            full_text = " ".join([
                e.get("benchmark_name", ""),
                e.get("what_measures", ""),
                e.get("how_measures", ""),
                e.get("reasoning", ""),
            ]).lower()
            if any(w in full_text for w in ["trust", "reliab", "robust", "risk", "guardrail", "detect"]):
                cats = ["6. Safety & Red Teaming"]
            elif any(w in full_text for w in ["social", "norm", "stereotyp", "sentiment", "opinion", "survey"]):
                cats = ["4. Fairness, Bias & Social Norms"]
            elif any(w in full_text for w in ["moral", "ethic", "right", "wrong", "good", "bad", "virtue"]):
                cats = ["1. Moral Reasoning & Ethical Judgment"]
            elif any(w in full_text for w in ["generat", "model", "llm", "language model", "chatbot", "instruct", "benchmark", "evaluat"]):
                cats = ["10. Helpfulness, Honesty & RLHF"]
            else:
                cats = ["4. Fairness, Bias & Social Norms"]

        entry_cats[e["filename"]] = cats
        for c in cats:
            cat_entries[c].append(e)

    # Category counts
    cat_counts = {c: len(set(e["filename"] for e in cat_entries.get(c, []))) for c in cat_order}

    # Multi-category stats
    multi_cat = sum(1 for cats in entry_cats.values() if len(cats) > 1)

    # Co-occurrence matrix
    co_matrix = defaultdict(lambda: defaultdict(int))
    for fn, cats in entry_cats.items():
        for i, c1 in enumerate(cats):
            for c2 in cats[i+1:]:
                short1 = c1.split(".")[0].strip()
                short2 = c2.split(".")[0].strip()
                co_matrix[short1][short2] += 1
                co_matrix[short2][short1] += 1

    # Category × Year
    cat_year = defaultdict(lambda: defaultdict(int))
    for cat in cat_order:
        for e in cat_entries.get(cat, []):
            y = extract_year(e["filename"])
            if y != 9999:
                cat_year[cat][y] += 1

    return {
        "cat_order": cat_order,
        "cat_counts": cat_counts,
        "multi_cat": multi_cat,
        "entry_cats": entry_cats,
        "cat_entries": cat_entries,
        "co_matrix": co_matrix,
        "cat_year": cat_year,
    }


def analyze_measurement_approaches(candidates):
    """Section 4: Measurement approaches."""
    method_counts = Counter()
    method_by_cat = defaultdict(lambda: Counter())
    method_by_year = defaultdict(lambda: Counter())
    entries_without_method = 0

    for e in candidates:
        methods = extract_methodology_types(e)
        cats = classify_entry(e) or ["Uncategorized"]
        year = extract_year(e["filename"])

        if not methods:
            entries_without_method += 1
            continue

        for m in methods:
            method_counts[m] += 1
            if year != 9999:
                method_by_year[m][year] += 1
            for c in cats:
                short_cat = c.split(". ", 1)[1] if ". " in c else c
                method_by_cat[m][short_cat] += 1

    return {
        "method_counts": method_counts,
        "method_by_cat": method_by_cat,
        "method_by_year": method_by_year,
        "no_method": entries_without_method,
        "total": len(candidates),
    }


def analyze_model_coverage(candidates):
    """Section 5: Model coverage matrix."""
    family_counts = Counter()
    family_by_cat = defaultdict(lambda: Counter())
    family_by_year = defaultdict(lambda: Counter())
    entries_with_model = 0
    entries_without_model = 0
    pre_llm = 0  # entries with only pre-LLM models
    llm_era = 0  # entries with LLM-era models

    PRE_LLM_FAMILIES = {"BERT family", "Word2Vec/GloVe", "GPT-2", "T5/Flan", "OPT", "BLOOM"}
    LLM_FAMILIES = {"GPT-4", "GPT-3.5", "GPT-3", "Claude", "Llama", "Gemini",
                     "Mistral/Mixtral", "Qwen", "DeepSeek", "Falcon", "Phi", "Vicuna",
                     "PaLM", "Cohere", "Delphi", "Anthropic models", "Zephyr",
                     "StableLM", "Gemma", "OpenAI (unspecified)", "Jurassic/AI21"}

    for e in candidates:
        models_text = e.get("models_evaluated", "")
        families = extract_model_families(models_text)
        cats = classify_entry(e) or ["Uncategorized"]
        year = extract_year(e["filename"])

        if families:
            entries_with_model += 1
            has_pre = any(f in PRE_LLM_FAMILIES for f in families)
            has_llm = any(f in LLM_FAMILIES for f in families)
            if has_llm:
                llm_era += 1
            elif has_pre:
                pre_llm += 1
        else:
            entries_without_model += 1

        for fam in families:
            family_counts[fam] += 1
            if year != 9999:
                family_by_year[fam][year] += 1
            for c in cats:
                short_cat = c.split(". ", 1)[1] if ". " in c else c
                family_by_cat[fam][short_cat] += 1

    return {
        "family_counts": family_counts,
        "family_by_cat": family_by_cat,
        "family_by_year": family_by_year,
        "with_model": entries_with_model,
        "without_model": entries_without_model,
        "pre_llm": pre_llm,
        "llm_era": llm_era,
        "total": len(candidates),
    }


def analyze_cultural_pluralistic(candidates):
    """Section 6: Cultural & pluralistic coverage."""
    plur_counts = Counter()
    plur_by_cat = defaultdict(lambda: Counter())
    tradition_counts = Counter()
    tradition_by_cat = defaultdict(lambda: Counter())
    lang_counts = Counter()
    lang_by_cat = defaultdict(lambda: Counter())

    for e in candidates:
        plur = e.get("pluralistic_relevance", "N/A")
        plur_counts[plur] += 1
        cats = classify_entry(e) or ["Uncategorized"]
        for c in cats:
            sc = c.split(". ", 1)[1] if ". " in c else c
            plur_by_cat[plur][sc] += 1

        traditions = extract_traditions(e)
        for t in traditions:
            tradition_counts[t] += 1
            for c in cats:
                sc = c.split(". ", 1)[1] if ". " in c else c
                tradition_by_cat[t][sc] += 1

        langs = extract_languages(e)
        for l in langs:
            lang_counts[l] += 1
            for c in cats:
                sc = c.split(". ", 1)[1] if ". " in c else c
                lang_by_cat[l][sc] += 1

    return {
        "plur_counts": plur_counts,
        "plur_by_cat": plur_by_cat,
        "tradition_counts": tradition_counts,
        "tradition_by_cat": tradition_by_cat,
        "lang_counts": lang_counts,
        "lang_by_cat": lang_by_cat,
    }


def analyze_data_availability(candidates):
    """Section 7: Data availability."""
    avail_counts = Counter()
    avail_by_cat = defaultdict(lambda: Counter())
    urls_by_category = defaultdict(list)  # availability_cat -> [(paper, url)]

    for e in candidates:
        cat_label, url = parse_availability(e.get("availability", ""))
        avail_counts[cat_label] += 1
        cats = classify_entry(e) or ["Uncategorized"]
        for c in cats:
            sc = c.split(". ", 1)[1] if ". " in c else c
            avail_by_cat[cat_label][sc] += 1
        if url:
            urls_by_category[cat_label].append((e["filename"], url))

    return {
        "avail_counts": avail_counts,
        "avail_by_cat": avail_by_cat,
        "urls": urls_by_category,
    }


def analyze_normative_deep_dive(normative_entries):
    """Section 8: Normative ethics deep dive."""
    yes_entries = [e for e in normative_entries if e.get("decision") == "Yes"]
    borderline_entries = [e for e in normative_entries if e.get("decision") == "Borderline"]

    # Framework distribution — search full text for known frameworks rather than
    # splitting on commas (which produces garbage from sentence punctuation)
    NORMATIVE_FRAMEWORK_PATTERNS = {
        "Deontology/Kantian": re.compile(r'\bdeontolog|kantian|\bcategorical\s+imperative|duty[\s\-]based', re.I),
        "Consequentialism/Utilitarianism": re.compile(r'\bconsequential|utilitarian|\bgreatest\s+(?:good|happin)', re.I),
        "Virtue Ethics": re.compile(r'\bvirtue\s+ethic|aristotel|eudaimonia|phronesis|character\s+ethic', re.I),
        "Care Ethics": re.compile(r'\bcare\s+ethic|feminist\s+ethic|ethic\w?\s+of\s+care|relational\s+ethic', re.I),
        "Contractualism/Rawlsian": re.compile(r'\bcontractualis|rawls|social\s+contract|veil\s+of\s+ignorance', re.I),
        "Principlism": re.compile(r'\bprinciplism|beauchamp|non[\s\-]?maleficence|beneficence.*autonomy', re.I),
        "Confucian Ethics": re.compile(r'\bconfucian', re.I),
        "Islamic Ethics": re.compile(r'\bislamic\s+ethic|sharia|maqasid', re.I),
        "Distributive Justice": re.compile(r'\bdistributive\s+justice|egalitarian.*framework', re.I),
        "Moral Foundations Theory": re.compile(r'\bmoral\s+foundation|haidt.*foundation|MFT\b|MFQ\b', re.I),
        "Kohlberg's Moral Development": re.compile(r'\bkohlberg|moral\s+development\s+stage|DIT\b', re.I),
        "Commonsense Morality": re.compile(r'\bcommonsense\s+moral', re.I),
        "Natural Law": re.compile(r'\bnatural\s+law\b', re.I),
        "Buddhist Ethics": re.compile(r'\bbuddhis[mt]\s+ethic', re.I),
        "Hindu Ethics": re.compile(r'\bhindu\s+(?:ethic|moral|philosophy)|dharma', re.I),
        "Social Choice Theory": re.compile(r'\bsocial\s+choice\s+theory', re.I),
    }

    framework_counts = Counter()
    multi_framework = 0
    for e in yes_entries + borderline_entries:
        nf = e.get("normative_frameworks", "N/A")
        reasoning = e.get("reasoning", "")
        search_text = f"{nf} {reasoning}"

        if not nf or nf == "N/A":
            continue

        found = []
        for fw_name, pat in NORMATIVE_FRAMEWORK_PATTERNS.items():
            if pat.search(search_text):
                found.append(fw_name)
                framework_counts[fw_name] += 1

        if len(found) > 1:
            multi_framework += 1
        elif len(found) == 0:
            # Fallback: store the first 60 chars of the frameworks field
            framework_counts[nf[:60].strip()] += 1

    return {
        "yes_count": len(yes_entries),
        "borderline_count": len(borderline_entries),
        "total": len(normative_entries),
        "framework_counts": framework_counts,
        "multi_framework": multi_framework,
        "yes_entries": yes_entries,
        "borderline_entries": borderline_entries,
    }


def analyze_ready_resources(candidates):
    """Section 9: Ready-to-use resources for SOTA testing."""
    ready = []
    for e in candidates:
        avail_cat, url = parse_availability(e.get("availability", ""))
        if avail_cat not in ("Public", "Code available", "Partially public"):
            continue
        year = extract_year(e["filename"])
        bench_name = e.get("benchmark_name", "N/A")
        models = e.get("models_evaluated", "N/A")
        size = e.get("dataset_size", "N/A")
        ready.append({
            "filename": e["filename"],
            "year": year,
            "benchmark_name": bench_name,
            "what_measures": e.get("what_measures", "N/A"),
            "dataset_size": size,
            "models_evaluated": models,
            "availability": e.get("availability", "N/A"),
            "url": url,
        })

    # Sort by year descending
    ready.sort(key=lambda x: (-x["year"], x["filename"].lower()))
    return {"ready": ready}


def analyze_temporal_trends(all_entries, candidates):
    """Section 10: Temporal trends."""
    all_years = Counter()
    cand_years = Counter()
    for e in all_entries:
        y = extract_year(e["filename"])
        if y != 9999:
            all_years[y] += 1
    for e in candidates:
        y = extract_year(e["filename"])
        if y != 9999:
            cand_years[y] += 1

    return {
        "all_years": all_years,
        "cand_years": cand_years,
    }


def analyze_gaps(cultural_data, method_data, model_data):
    """Section 11: Gap analysis with coverage matrices."""
    # Tradition × Methodology
    tradition_method = defaultdict(lambda: defaultdict(int))
    # This would need per-entry correlation — approximate from counts
    # For now, build from the category overlap data

    return {
        "tradition_counts": cultural_data["tradition_counts"],
        "lang_counts": cultural_data["lang_counts"],
        "method_counts": method_data["method_counts"],
        "model_counts": model_data["family_counts"],
    }


# ═══════════════════════════════════════════════════════════════════════════
# D. REPORT ASSEMBLY
# ═══════════════════════════════════════════════════════════════════════════

def make_wikilink(filename):
    """Convert filename to Obsidian wikilink."""
    name = filename[:-3] if filename.endswith(".md") else filename
    return f"[[{name}]]"


def truncate(text, max_len=60):
    if not text:
        return "N/A"
    text = text.strip()
    return text if len(text) <= max_len else text[:max_len-3].rstrip() + "..."


def assemble_report(landscape, taxonomy, methods, models, cultural, availability,
                    normative, ready, llm_assess, trends, gaps, candidates):
    """Assemble all sections into the final Markdown report."""
    L = []

    # ── Header ──────────────────────────────────────────────────────────
    L.append("# Comprehensive Vault Overview: LLM Ethics & Values Alignment Resources")
    L.append("")
    L.append(f"**Generated:** 2026-02-12 | **Papers:** {landscape['total']} screened, "
             f"{landscape['candidates']} benchmark candidates | "
             f"**Normative ethics:** {normative['yes_count'] + normative['borderline_count']} papers")
    L.append("")
    L.append("---")
    L.append("")

    # ── Table of Contents ────────────────────────────────────────────────
    L.append("## Table of Contents")
    L.append("")
    toc_items = [
        "1. Executive Summary",
        "2. Landscape Overview",
        "3. Benchmark Taxonomy (10 Categories)",
        "4. Measurement Approaches",
        "5. Model Coverage Matrix",
        "6. Cultural & Pluralistic Coverage",
        "7. Data Availability",
        "8. Normative Ethics Deep Dive",
        "9. Ready-to-Use Resources for SOTA Testing",
        "10. LLM Assessment Coverage",
        "11. Temporal Trends",
        "12. Gap Analysis",
        "13. Recommendations for Values Alignment Research",
        "14. Methodology",
        "Appendix A: Full Benchmark Candidate List",
        "Appendix B: Normalization Definitions",
    ]
    for item in toc_items:
        anchor = item.lower().replace(" ", "-").replace("(", "").replace(")", "").replace(":", "").replace(",", "")
        L.append(f"- [{item}](#{anchor})")
    L.append("")
    L.append("---")
    L.append("")

    # ── 1. Executive Summary ─────────────────────────────────────────────
    L.append("## 1. Executive Summary")
    L.append("")
    L.append(f"This vault contains **{landscape['total']} papers** spanning AI ethics, moral reasoning, "
             f"fairness, safety, and values alignment research from 2010 to 2026. A systematic 20-agent "
             f"deep-read identified **{landscape['candidates']} papers** ({landscape['candidates']*100//landscape['total']}%) "
             f"as containing or proposing benchmarks, datasets, or evaluation metrics relevant to LLM ethics evaluation. "
             f"The remaining {landscape['excluded']} papers provide theoretical, philosophical, or survey contributions "
             f"without empirical evaluation artifacts.")
    L.append("")
    plur_yes = cultural["plur_counts"].get("Yes", 0)
    plur_partial = cultural["plur_counts"].get("Partial", 0)
    plur_pct = (plur_yes + plur_partial) * 100 // landscape["candidates"]
    L.append(f"Of the benchmark candidates, **{plur_pct}%** have some pluralistic relevance (addressing diverse "
             f"cultural or value perspectives), though systematic coverage remains uneven. "
             f"Western ethical traditions (deontology, consequentialism, virtue ethics) are moderately represented, "
             f"while Ubuntu, Buddhist, and Indigenous ethical frameworks have **zero benchmark coverage**. "
             f"English dominates overwhelmingly, with Chinese and Korean as the most active non-English benchmark languages.")
    L.append("")

    avail_public = availability["avail_counts"].get("Public", 0)
    avail_code = availability["avail_counts"].get("Code available", 0)
    L.append(f"**{avail_public + avail_code} benchmarks** ({(avail_public + avail_code)*100//landscape['candidates']}%) "
             f"have publicly available data or code, providing a substantial foundation for immediate values alignment evaluation. "
             f"The most tested model families are GPT-4, GPT-3.5/ChatGPT, and Llama, with recent growth in "
             f"Gemini, Mistral, and Qwen evaluation.")
    L.append("")

    # Summary of Findings table
    L.append("### Summary of Findings")
    L.append("")
    L.append("| Dimension | Finding |")
    L.append("|-----------|---------|")
    L.append(f"| Total papers | {landscape['total']} screened, {landscape['candidates']} benchmark candidates |")
    top_cat = max(taxonomy["cat_counts"], key=taxonomy["cat_counts"].get)
    L.append(f"| Largest category | {top_cat} ({taxonomy['cat_counts'][top_cat]} papers) |")
    L.append(f"| Multi-category papers | {taxonomy['multi_cat']} ({taxonomy['multi_cat']*100//landscape['candidates']}%) |")
    L.append(f"| Pluralistic relevance | {plur_yes} Yes + {plur_partial} Partial = {plur_pct}% |")
    L.append(f"| Public availability | {avail_public} Public + {avail_code} Code available |")
    if models["family_counts"]:
        top_model = models["family_counts"].most_common(1)[0]
        L.append(f"| Most evaluated model | {top_model[0]} ({top_model[1]} papers) |")
    L.append(f"| Normative ethics | {normative['yes_count']} Yes + {normative['borderline_count']} Borderline |")
    L.append(f"| Unique authors | {landscape['n_authors']} |")
    L.append("")
    L.append("---")
    L.append("")

    # ── 2. Landscape Overview ────────────────────────────────────────────
    L.append("## 2. Landscape Overview")
    L.append("")
    L.append(f"**{landscape['total']} papers** were screened. **{landscape['candidates']}** "
             f"({landscape['candidates']*100//landscape['total']}%) contain benchmark/evaluation resources; "
             f"**{landscape['excluded']}** ({landscape['excluded']*100//landscape['total']}%) are theoretical, "
             f"philosophical, or survey papers.")
    L.append("")

    # Year distribution
    all_years = sorted(landscape["year_counts"].keys())
    if all_years:
        min_year = min(all_years)
        max_year = max(all_years)
        L.append("### Year Distribution")
        L.append("")
        L.append("| Year | All Papers | Benchmark Candidates | Candidate % |")
        L.append("|------|-----------|---------------------|-------------|")
        for y in range(min_year, max_year + 1):
            total_y = landscape["year_counts"].get(y, 0)
            cand_y = landscape["cand_year_counts"].get(y, 0)
            pct = f"{cand_y*100//total_y}%" if total_y > 0 else "-"
            bar = "█" * (total_y // 3) if total_y > 0 else ""
            L.append(f"| {y} | {total_y} {bar} | {cand_y} | {pct} |")
        L.append("")

    # Top authors
    L.append("### Top Prolific First Authors")
    L.append("")
    L.append("| # | Author | Papers |")
    L.append("|---|--------|--------|")
    for i, (author, count) in enumerate(landscape["top_authors"], 1):
        L.append(f"| {i} | {author} | {count} |")
    L.append("")
    L.append("---")
    L.append("")

    # ── 3. Benchmark Taxonomy ────────────────────────────────────────────
    L.append("## 3. Benchmark Taxonomy (10 Categories)")
    L.append("")
    L.append("Papers are classified into 10 categories using keyword matching on benchmark names, "
             "measurement descriptions, and agent reasoning. Papers may appear in multiple categories.")
    L.append("")

    L.append("### Category Distribution")
    L.append("")
    L.append("| # | Category | Papers | Description |")
    L.append("|---|----------|--------|-------------|")
    for cat in taxonomy["cat_order"]:
        num = cat.split(".")[0].strip()
        name = cat.split(". ", 1)[1]
        count = taxonomy["cat_counts"].get(cat, 0)
        desc = CATEGORIES[cat]["desc"]
        bar = "█" * (count // 10)
        L.append(f"| {num} | {name} | {count} {bar} | {truncate(desc, 80)} |")
    L.append("")
    L.append(f"*{taxonomy['multi_cat']} papers ({taxonomy['multi_cat']*100//landscape['candidates']}%) "
             f"appear in 2+ categories.*")
    L.append("")

    # Category × Year
    all_cat_years = set()
    for cat, years_dict in taxonomy["cat_year"].items():
        all_cat_years.update(years_dict.keys())
    if all_cat_years:
        year_range = sorted(all_cat_years)
        # Only show recent years (2018+) to keep table manageable
        recent_years = [y for y in year_range if y >= 2018]
        if recent_years:
            L.append("### Category x Year Cross-Tabulation (2018-2026)")
            L.append("")
            cat_year_matrix = {}
            for cat in taxonomy["cat_order"]:
                short = cat.split(". ", 1)[1][:25]
                cat_year_matrix[short] = {}
                for y in recent_years:
                    cat_year_matrix[short][y] = taxonomy["cat_year"].get(cat, {}).get(y, 0)
            row_keys = [cat.split(". ", 1)[1][:25] for cat in taxonomy["cat_order"]]
            L.extend(make_crosstab_table("Category", "Year", row_keys, recent_years, cat_year_matrix))
            L.append("")

    # Co-occurrence
    cat_nums = [str(i) for i in range(1, 11)]
    co = taxonomy["co_matrix"]
    if co:
        L.append("### Category Co-occurrence Matrix")
        L.append("")
        L.append("*Number of papers appearing in both categories (row × column):*")
        L.append("")
        co_rows = {}
        for n1 in cat_nums:
            co_rows[n1] = {}
            for n2 in cat_nums:
                co_rows[n1][n2] = co.get(n1, {}).get(n2, 0) if n1 != n2 else "-"
        header = ["Cat"] + cat_nums
        L.append("| " + " | ".join(header) + " |")
        L.append("|" + "|".join("---" for _ in header) + "|")
        for n in cat_nums:
            row = [n]
            for n2 in cat_nums:
                v = co_rows[n][n2]
                row.append(str(v) if v != "-" and v > 0 else "-")
            L.append("| " + " | ".join(row) + " |")
        L.append("")

    L.append("---")
    L.append("")

    # ── 4. Measurement Approaches ────────────────────────────────────────
    L.append("## 4. Measurement Approaches")
    L.append("")
    L.append(f"Methodology types extracted from {methods['total']} benchmark candidates via regex normalization. "
             f"{methods['no_method']} entries had no recognized methodology type.")
    L.append("")

    L.append("### Methodology Type Prevalence")
    L.append("")
    L.append("| # | Methodology | Count | % of Candidates |")
    L.append("|---|------------|-------|-----------------|")
    for i, (meth, count) in enumerate(methods["method_counts"].most_common(), 1):
        pct = count * 100 // methods["total"]
        L.append(f"| {i} | {meth} | {count} | {pct}% |")
    L.append("")

    # Method × Category (top 8 methods × 10 categories)
    if methods["method_by_cat"]:
        top_methods = [m for m, _ in methods["method_counts"].most_common(8)]
        cat_short_names = [c.split(". ", 1)[1][:20] for c in taxonomy["cat_order"]]
        meth_cat_matrix = {}
        for m in top_methods:
            meth_cat_matrix[m[:25]] = {}
            for cs in cat_short_names:
                meth_cat_matrix[m[:25]][cs] = methods["method_by_cat"].get(m, {}).get(
                    next((c.split(". ", 1)[1] for c in taxonomy["cat_order"]
                          if c.split(". ", 1)[1][:20] == cs), ""), 0)
        # Rebuild properly
        meth_cat_matrix2 = {}
        for m in top_methods:
            meth_cat_matrix2[m[:25]] = {}
            for cat in taxonomy["cat_order"]:
                sc = cat.split(". ", 1)[1]
                short_sc = sc[:20]
                meth_cat_matrix2[m[:25]][short_sc] = methods["method_by_cat"].get(m, {}).get(sc, 0)

        L.append("### Methodology x Category (Top 8)")
        L.append("")
        L.extend(make_crosstab_table(
            "Methodology", "Category",
            [m[:25] for m in top_methods], cat_short_names,
            meth_cat_matrix2
        ))
        L.append("")

    L.append("---")
    L.append("")

    # ── 5. Model Coverage Matrix ─────────────────────────────────────────
    L.append("## 5. Model Coverage Matrix")
    L.append("")
    L.append(f"Model families extracted from `models_evaluated` field. "
             f"**{models['with_model']}** candidates ({models['with_model']*100//models['total']}%) mention "
             f"specific models; **{models['without_model']}** do not specify models tested.")
    L.append("")
    L.append(f"- **LLM-era benchmarks** (GPT-3+, Claude, Llama, etc.): {models['llm_era']}")
    L.append(f"- **Pre-LLM benchmarks** (BERT, Word2Vec only): {models['pre_llm']}")
    L.append("")

    L.append("### Model Family Prevalence")
    L.append("")
    L.append("| # | Model Family | Papers | % |")
    L.append("|---|-------------|--------|---|")
    for i, (fam, count) in enumerate(models["family_counts"].most_common(20), 1):
        pct = count * 100 // models["total"]
        bar = "█" * (count // 8)
        L.append(f"| {i} | {fam} | {count} {bar} | {pct}% |")
    L.append("")

    # Model × Category heatmap (top 12 models)
    if models["family_by_cat"]:
        top_fams = [f for f, _ in models["family_counts"].most_common(12)]
        cat_short = [c.split(". ", 1)[1][:20] for c in taxonomy["cat_order"]]
        fam_cat_matrix = {}
        for fam in top_fams:
            fam_cat_matrix[fam] = {}
            for cat in taxonomy["cat_order"]:
                sc = cat.split(". ", 1)[1]
                fam_cat_matrix[fam][sc[:20]] = models["family_by_cat"].get(fam, {}).get(sc, 0)

        L.append("### Model Family x Category (Top 12)")
        L.append("")
        L.extend(make_crosstab_table("Model", "Category", top_fams, cat_short, fam_cat_matrix))
        L.append("")

    L.append("---")
    L.append("")

    # ── 6. Cultural & Pluralistic Coverage ───────────────────────────────
    L.append("## 6. Cultural & Pluralistic Coverage")
    L.append("")

    L.append("### Pluralistic Relevance")
    L.append("")
    L.append("| Relevance | Count | % |")
    L.append("|-----------|-------|---|")
    for label in ["Yes", "Partial", "No"]:
        c = cultural["plur_counts"].get(label, 0)
        pct = c * 100 // landscape["candidates"]
        L.append(f"| {label} | {c} | {pct}% |")
    for label, c in sorted(cultural["plur_counts"].items()):
        if label not in ("Yes", "Partial", "No"):
            pct = c * 100 // landscape["candidates"]
            L.append(f"| {label} | {c} | {pct}% |")
    L.append("")

    # Ethical traditions
    L.append("### Ethical Traditions Detected")
    L.append("")
    if cultural["tradition_counts"]:
        L.append("| Tradition | Mentions | Coverage Level |")
        L.append("|-----------|----------|---------------|")
        for trad, count in cultural["tradition_counts"].most_common():
            level = "Strong" if count > 20 else "Moderate" if count > 10 else "Low" if count > 3 else "Very Low"
            L.append(f"| {trad} | {count} | {level} |")
        # Note missing traditions
        all_traditions = set(ETHICAL_TRADITIONS.keys())
        detected = set(cultural["tradition_counts"].keys())
        missing = all_traditions - detected
        for trad in sorted(missing):
            L.append(f"| {trad} | 0 | **None** |")
    L.append("")

    # Languages
    L.append("### Languages Detected")
    L.append("")
    if cultural["lang_counts"]:
        L.append("| Language | Mentions | Coverage Level |")
        L.append("|----------|----------|---------------|")
        for lang, count in cultural["lang_counts"].most_common():
            level = "Strong" if count > 30 else "Moderate" if count > 10 else "Emerging" if count > 3 else "Minimal"
            L.append(f"| {lang} | {count} | {level} |")
        all_langs = set(LANGUAGES.keys())
        detected_l = set(cultural["lang_counts"].keys())
        missing_l = all_langs - detected_l
        for lang in sorted(missing_l):
            L.append(f"| {lang} | 0 | **None** |")
    L.append("")

    # Language × Category
    if cultural["lang_by_cat"]:
        top_langs = [l for l, _ in cultural["lang_counts"].most_common(10)]
        cat_short = [c.split(". ", 1)[1][:20] for c in taxonomy["cat_order"]]
        lang_cat_matrix = {}
        for lang in top_langs:
            lang_cat_matrix[lang] = {}
            for cat in taxonomy["cat_order"]:
                sc = cat.split(". ", 1)[1]
                lang_cat_matrix[lang][sc[:20]] = cultural["lang_by_cat"].get(lang, {}).get(sc, 0)

        L.append("### Language x Category (Top 10)")
        L.append("")
        L.extend(make_crosstab_table("Language", "Category", top_langs, cat_short, lang_cat_matrix))
        L.append("")

    L.append("---")
    L.append("")

    # ── 7. Data Availability ─────────────────────────────────────────────
    L.append("## 7. Data Availability")
    L.append("")
    L.append("| Availability | Count | % |")
    L.append("|-------------|-------|---|")
    avail_order = ["Public", "Partially public", "Code available", "Not stated", "Not public"]
    for label in avail_order:
        c = availability["avail_counts"].get(label, 0)
        if c > 0:
            pct = c * 100 // landscape["candidates"]
            L.append(f"| {label} | {c} | {pct}% |")
    for label, c in sorted(availability["avail_counts"].items()):
        if label not in avail_order and c > 0:
            pct = c * 100 // landscape["candidates"]
            L.append(f"| {label} | {c} | {pct}% |")
    L.append("")

    # Availability × Category
    if availability["avail_by_cat"]:
        cat_short = [c.split(". ", 1)[1][:20] for c in taxonomy["cat_order"]]
        avail_labels = [l for l in avail_order if availability["avail_counts"].get(l, 0) > 0]
        avail_cat_matrix = {}
        for al in avail_labels:
            avail_cat_matrix[al] = {}
            for cat in taxonomy["cat_order"]:
                sc = cat.split(". ", 1)[1]
                avail_cat_matrix[al][sc[:20]] = availability["avail_by_cat"].get(al, {}).get(sc, 0)

        L.append("### Availability x Category")
        L.append("")
        L.extend(make_crosstab_table("Availability", "Category", avail_labels, cat_short, avail_cat_matrix))
        L.append("")

    # Repository URLs
    all_urls = []
    for cat_label, url_list in availability["urls"].items():
        all_urls.extend(url_list)
    if all_urls:
        github_urls = [(fn, u) for fn, u in all_urls if "github.com" in u.lower()]
        hf_urls = [(fn, u) for fn, u in all_urls if "huggingface" in u.lower() or "hf.co" in u.lower()]
        L.append("### Repository Links")
        L.append("")
        if github_urls:
            L.append(f"**GitHub repositories:** {len(github_urls)} identified")
            L.append("")
            for fn, url in github_urls[:30]:
                L.append(f"- {make_wikilink(fn)}: {url}")
            if len(github_urls) > 30:
                L.append(f"- *... and {len(github_urls) - 30} more*")
            L.append("")
        if hf_urls:
            L.append(f"**HuggingFace:** {len(hf_urls)} identified")
            L.append("")
            for fn, url in hf_urls[:20]:
                L.append(f"- {make_wikilink(fn)}: {url}")
            if len(hf_urls) > 20:
                L.append(f"- *... and {len(hf_urls) - 20} more*")
            L.append("")

    L.append("---")
    L.append("")

    # ── 8. Normative Ethics Deep Dive ────────────────────────────────────
    L.append("## 8. Normative Ethics Deep Dive")
    L.append("")
    L.append(f"From {normative['total']} papers evaluated for normative ethics content (EXSR batch), "
             f"**{normative['yes_count']}** were classified as **Yes** (explicitly operationalize normative "
             f"ethical theories) and **{normative['borderline_count']}** as **Borderline** (touch on normative "
             f"concepts without full operationalization).")
    L.append("")

    if normative["framework_counts"]:
        L.append("### Framework Distribution")
        L.append("")
        L.append("| Framework | Mentions |")
        L.append("|-----------|----------|")
        for fw, count in normative["framework_counts"].most_common():
            L.append(f"| {fw} | {count} |")
        L.append("")
        L.append(f"*{normative['multi_framework']} papers test multiple normative frameworks.*")
        L.append("")

    # List Yes papers
    if normative["yes_entries"]:
        L.append("### Papers with Full Normative Ethics Operationalization")
        L.append("")
        L.append("| Paper | Frameworks | LLMs Tested | Data Artifact |")
        L.append("|-------|-----------|-------------|---------------|")
        for e in sorted(normative["yes_entries"], key=lambda x: x["filename"]):
            paper = make_wikilink(e["filename"])
            fw = truncate(e.get("normative_frameworks", "N/A"), 50)
            llms = truncate(e.get("llms_tested", "N/A"), 40)
            data = truncate(e.get("data_artifact", "N/A"), 50)
            L.append(f"| {paper} | {fw} | {llms} | {data} |")
        L.append("")

    L.append("---")
    L.append("")

    # ── 9. Ready-to-Use Resources ────────────────────────────────────────
    L.append("## 9. Ready-to-Use Resources for SOTA Testing")
    L.append("")
    ready_list = ready["ready"]
    L.append(f"**{len(ready_list)} benchmarks** have publicly available data or code. "
             f"Sorted by recency (most recent first).")
    L.append("")

    # Show top 50 recent
    recent_ready = [r for r in ready_list if r["year"] >= 2023]
    L.append(f"### Recent Public Benchmarks (2023-2026): {len(recent_ready)} available")
    L.append("")
    L.append("| # | Year | Paper | Benchmark | What It Measures | Availability |")
    L.append("|---|------|-------|-----------|-----------------|--------------|")
    for i, r in enumerate(recent_ready[:60], 1):
        paper = make_wikilink(r["filename"])
        bench = truncate(r["benchmark_name"], 40)
        what = truncate(r["what_measures"], 45)
        avail = truncate(r["availability"], 40)
        L.append(f"| {i} | {r['year']} | {paper} | {bench} | {what} | {avail} |")
    if len(recent_ready) > 60:
        L.append(f"| | | *... {len(recent_ready) - 60} more* | | | |")
    L.append("")

    L.append("---")
    L.append("")

    # ── 10. LLM Assessment Coverage ──────────────────────────────────────
    L.append("## 10. LLM Assessment Coverage")
    L.append("")
    model_pct = llm_assess["with_models"] * 100 // llm_assess["total"] if llm_assess["total"] > 0 else 0
    url_pct = llm_assess["with_urls"] * 100 // llm_assess["total"] if llm_assess["total"] > 0 else 0
    L.append(f"All **{llm_assess['total']} papers** were assessed for LLM model usage and data availability. "
             f"**{llm_assess['with_models']}** papers ({model_pct}%) mention specific LLM models; "
             f"**{llm_assess['with_urls']}** papers ({url_pct}%) have a linked data URL.")
    L.append("")

    # Top 20 LLM models table
    if llm_assess["model_counter"]:
        L.append("### Top 20 LLM Models Mentioned")
        L.append("")
        L.append("| # | Model | Papers | % of Papers with Models |")
        L.append("|---|-------|--------|------------------------|")
        for i, (model, count) in enumerate(llm_assess["model_counter"].most_common(20), 1):
            mpct = count * 100 // llm_assess["with_models"] if llm_assess["with_models"] > 0 else 0
            bar = "█" * (count // 10)
            L.append(f"| {i} | {model} | {count} {bar} | {mpct}% |")
        L.append("")

    # Assessment by year
    all_assess_years = sorted(set(list(llm_assess["assessed_by_year"].keys()) +
                                  list(llm_assess["not_assessed_by_year"].keys())))
    if all_assess_years:
        L.append("### Assessment Coverage by Year")
        L.append("")
        L.append("| Year | With LLM Models | Without | Total | LLM % |")
        L.append("|------|----------------|---------|-------|-------|")
        for y in all_assess_years:
            a = llm_assess["assessed_by_year"].get(y, 0)
            na = llm_assess["not_assessed_by_year"].get(y, 0)
            t = a + na
            pct = f"{a * 100 // t}%" if t > 0 else "-"
            L.append(f"| {y} | {a} | {na} | {t} | {pct} |")
        L.append("")

    # Data repository distribution
    if llm_assess["repo_counter"]:
        L.append("### Data Repository Distribution")
        L.append("")
        L.append("| Repository | Count | % of Papers with URLs |")
        L.append("|-----------|-------|----------------------|")
        for repo, count in llm_assess["repo_counter"].most_common():
            rpct = count * 100 // llm_assess["with_urls"] if llm_assess["with_urls"] > 0 else 0
            L.append(f"| {repo} | {count} | {rpct}% |")
        L.append("")

    L.append("---")
    L.append("")

    # ── 11. Temporal Trends ──────────────────────────────────────────────
    L.append("## 11. Temporal Trends")
    L.append("")
    all_y = sorted(trends["all_years"].keys())
    if all_y:
        L.append("### Growth Over Time")
        L.append("")
        L.append("| Year | All Papers | Benchmarks | Benchmark % | Growth |")
        L.append("|------|-----------|-----------|-------------|--------|")
        prev = 0
        for y in all_y:
            total_y = trends["all_years"][y]
            cand_y = trends["cand_years"].get(y, 0)
            pct = f"{cand_y*100//total_y}%" if total_y > 0 else "-"
            growth = f"+{cand_y - prev}" if prev > 0 and cand_y > prev else (f"{cand_y - prev}" if prev > 0 else "-")
            L.append(f"| {y} | {total_y} | {cand_y} | {pct} | {growth} |")
            prev = cand_y
        L.append("")

    L.append("---")
    L.append("")

    # ── 12. Gap Analysis ─────────────────────────────────────────────────
    L.append("## 12. Gap Analysis")
    L.append("")

    L.append("### Ethical Tradition Coverage Gaps")
    L.append("")
    L.append("| Tradition | Benchmark Coverage | Status |")
    L.append("|-----------|-------------------|--------|")
    tradition_coverage = [
        ("Consequentialism/Utilitarianism", cultural["tradition_counts"].get("Consequentialist", 0)),
        ("Deontological Ethics", cultural["tradition_counts"].get("Deontological", 0)),
        ("Virtue Ethics (Western)", cultural["tradition_counts"].get("Virtue Ethics (Western)", 0)),
        ("Care Ethics", cultural["tradition_counts"].get("Care Ethics", 0)),
        ("Confucian Ethics", cultural["tradition_counts"].get("Confucian", 0)),
        ("Islamic Ethics", cultural["tradition_counts"].get("Islamic", 0)),
        ("Hindu Ethics", cultural["tradition_counts"].get("Hindu", 0)),
        ("Buddhist Ethics", cultural["tradition_counts"].get("Buddhist", 0)),
        ("Ubuntu Ethics", cultural["tradition_counts"].get("Ubuntu", 0)),
        ("Indigenous Traditions", cultural["tradition_counts"].get("Indigenous", 0)),
    ]
    for trad, count in tradition_coverage:
        if count == 0:
            status = "**CRITICAL GAP** - No benchmarks"
        elif count <= 3:
            status = "Severe gap - Minimal coverage"
        elif count <= 10:
            status = "Moderate gap"
        else:
            status = "Adequate"
        L.append(f"| {trad} | {count} papers | {status} |")
    L.append("")

    L.append("### Language Coverage Gaps")
    L.append("")
    L.append("| Coverage Level | Languages |")
    L.append("|---------------|-----------|")
    strong_langs = [l for l, c in cultural["lang_counts"].most_common() if c > 30]
    moderate_langs = [l for l, c in cultural["lang_counts"].most_common() if 10 < c <= 30]
    emerging_langs = [l for l, c in cultural["lang_counts"].most_common() if 3 < c <= 10]
    minimal_langs = [l for l, c in cultural["lang_counts"].most_common() if 0 < c <= 3]
    none_langs = sorted(set(LANGUAGES.keys()) - set(cultural["lang_counts"].keys()))
    L.append(f"| Strong (>30) | {', '.join(strong_langs) or 'None'} |")
    L.append(f"| Moderate (10-30) | {', '.join(moderate_langs) or 'None'} |")
    L.append(f"| Emerging (4-10) | {', '.join(emerging_langs) or 'None'} |")
    L.append(f"| Minimal (1-3) | {', '.join(minimal_langs) or 'None'} |")
    L.append(f"| None (0) | {', '.join(none_langs) or 'None'} |")
    L.append("")

    L.append("### Methodology Gaps")
    L.append("")
    all_method_names = list(METHODOLOGY_TYPES.keys())
    detected_methods = set(methods["method_counts"].keys())
    missing_methods = set(all_method_names) - detected_methods
    low_methods = [(m, c) for m, c in methods["method_counts"].items() if c < 20]
    L.append("| Gap Type | Methodologies |")
    L.append("|----------|--------------|")
    if missing_methods:
        L.append(f"| Not detected | {', '.join(sorted(missing_methods))} |")
    if low_methods:
        low_strs = [f"{m} ({c})" for m, c in sorted(low_methods, key=lambda x: x[1])]
        L.append(f"| Underrepresented (<20) | {', '.join(low_strs)} |")
    L.append("")

    L.append("### Key Structural Gaps")
    L.append("")
    L.append("1. **Non-Western ethical traditions**: Ubuntu, Buddhist, and Indigenous ethical frameworks have zero benchmark coverage. Hindu and Islamic ethics have minimal representation.")
    L.append("2. **Language diversity**: Most benchmarks are English-only. African, Pacific Island, and most Indigenous languages are entirely unrepresented.")
    L.append("3. **Longitudinal evaluation**: No benchmarks measure moral reasoning evolution over training or deployment time.")
    L.append("4. **Compositional ethics**: Few benchmarks test complex, multi-stakeholder scenarios reflecting real deployment challenges.")
    L.append("5. **Process-based evaluation**: Almost all benchmarks evaluate outcomes (right/wrong answers), not reasoning quality.")
    L.append("6. **Environmental and animal ethics**: Virtually no benchmarks address ecological or animal welfare reasoning.")
    L.append("")
    L.append("---")
    L.append("")

    # ── 13. Recommendations ──────────────────────────────────────────────
    L.append("## 13. Recommendations for Values Alignment Research")
    L.append("")

    # Tier 1: Start here
    L.append("### Tier 1: Start Here (Immediate Use)")
    L.append("")
    L.append("*Top public benchmarks for rapid SOTA LLM evaluation, prioritized by recency + breadth:*")
    L.append("")

    # Pick top recent public benchmarks across categories
    tier1_seen = set()
    tier1 = []
    for r in ready_list:
        if r["year"] >= 2023 and len(tier1) < 12:
            models_text = r.get("models_evaluated", "")
            fams = extract_model_families(models_text)
            if len(fams) >= 2 and r["filename"] not in tier1_seen:
                tier1.append(r)
                tier1_seen.add(r["filename"])
    # Fill remaining
    for r in ready_list:
        if len(tier1) >= 12:
            break
        if r["year"] >= 2023 and r["filename"] not in tier1_seen:
            tier1.append(r)
            tier1_seen.add(r["filename"])

    L.append("| # | Benchmark | Paper | What It Measures | Models Tested |")
    L.append("|---|-----------|-------|-----------------|---------------|")
    for i, r in enumerate(tier1[:12], 1):
        bench = truncate(r["benchmark_name"], 35)
        paper = make_wikilink(r["filename"])
        what = truncate(r["what_measures"], 45)
        mods = truncate(r.get("models_evaluated", "N/A"), 40)
        L.append(f"| {i} | {bench} | {paper} | {what} | {mods} |")
    L.append("")

    # Tier 2: Comprehensive evaluation
    L.append("### Tier 2: Comprehensive Evaluation")
    L.append("")
    L.append("*For thorough values alignment assessment, combine benchmarks across these dimensions:*")
    L.append("")
    L.append("| Dimension | Recommended Categories | Paper Count |")
    L.append("|-----------|----------------------|-------------|")
    for cat in taxonomy["cat_order"]:
        short = cat.split(". ", 1)[1]
        count = taxonomy["cat_counts"].get(cat, 0)
        L.append(f"| {short} | Category {cat.split('.')[0].strip()} | {count} |")
    L.append("")

    # Tier 3: Research frontiers
    L.append("### Tier 3: Research Frontiers")
    L.append("")
    L.append("*Underserved areas where new benchmark development is most needed:*")
    L.append("")
    L.append("1. **Cross-cultural normative ethics**: Benchmarks grounding ethical evaluation in Confucian, Islamic, Buddhist, Ubuntu, and Indigenous frameworks")
    L.append("2. **Pluralistic value aggregation**: How should LLMs handle genuinely contested moral questions where reasonable people disagree?")
    L.append("3. **Dynamic moral reasoning**: Evaluating consistency and evolution of moral reasoning across conversational contexts")
    L.append("4. **Applied professional ethics**: Domain-specific evaluation in healthcare, law, engineering, and education beyond simple knowledge testing")
    L.append("5. **Multilingual fairness**: Bias and fairness evaluation in low-resource languages")
    L.append("6. **Relational and care ethics**: Evaluation of LLM behavior in caregiving, counseling, and interpersonal support contexts")
    L.append("7. **Environmental ethics reasoning**: Sustainability, ecological justice, and intergenerational equity in AI decision-making")
    L.append("")
    L.append("---")
    L.append("")

    # ── 14. Methodology ──────────────────────────────────────────────────
    L.append("## 14. Methodology")
    L.append("")
    L.append("### Data Sources")
    L.append("")
    L.append("| Source | Records | Description |")
    L.append("|--------|---------|-------------|")
    L.append(f"| `benchmark_survey_all_classifications.json` | {landscape['total']} | 20-agent deep-read of all vault papers |")
    L.append(f"| `benchmark_survey_candidates.json` | {landscape['candidates']} | Subset with benchmark/evaluation resources |")
    L.append(f"| `normative_v2_all_classifications.json` | {normative['total']} | 10-agent normative ethics classification (EXSR batch) |")
    L.append(f"| `author_paper_map.json` | {landscape['n_authors']} | Author-paper mapping |")
    L.append(f"| Paper YAML frontmatter | {llm_assess['total']} | LLM_assessed and DATA_URL fields (2026-02-12 enrichment) |")
    L.append("")
    L.append("### Classification Approach")
    L.append("")
    L.append("- **Benchmark identification**: 20-agent parallel deep-read with structured extraction rubric")
    L.append("- **Category assignment**: Keyword-based classification across 10 categories (from `generate_benchmark_survey_report.py`)")
    L.append("- **Model family extraction**: Regex normalization mapping 70+ model name variants to ~27 canonical families")
    L.append("- **Methodology extraction**: Regex normalization mapping methodology descriptions to 14 canonical types")
    L.append("- **Cultural/language detection**: Pattern matching for 10 ethical traditions and 20 languages")
    L.append("")
    L.append("### Normalization Coverage")
    L.append("")
    n_with_model = models["with_model"]
    n_with_method = methods["total"] - methods["no_method"]
    L.append(f"- **Model recognition**: {n_with_model}/{models['total']} candidates ({n_with_model*100//models['total']}%) have ≥1 recognized model family")
    L.append(f"- **Methodology recognition**: {n_with_method}/{methods['total']} candidates ({n_with_method*100//methods['total']}%) have ≥1 recognized methodology type")
    L.append("")
    L.append("### Limitations")
    L.append("")
    L.append("- **Keyword-based classification** may miss nuanced thematic connections or create false positives")
    L.append("- **Coverage bias**: Vault overrepresents English-language, computationally-oriented, Western-authored papers")
    L.append("- **Temporal bias**: 2023-2025 papers are overrepresented due to rapid LLM safety/ethics growth")
    L.append("- **Free-text normalization**: Model and methodology extraction depends on how the 20 agents described each paper")
    L.append("- **No YAML modification**: This report is read-only analysis; no paper metadata was changed")
    L.append("")
    L.append("---")
    L.append("")

    # ── Appendix A: Full Candidate List ──────────────────────────────────
    L.append("## Appendix A: Full Benchmark Candidate List")
    L.append("")
    L.append(f"*{landscape['candidates']} benchmark candidates, sorted by year (most recent first):*")
    L.append("")
    sorted_cands = sorted(candidates, key=lambda e: (-extract_year(e["filename"]), e["filename"].lower()))
    L.append("| # | Year | Paper | Benchmark | Pluralistic | Availability |")
    L.append("|---|------|-------|-----------|-------------|--------------|")
    for i, e in enumerate(sorted_cands, 1):
        year = extract_year(e["filename"])
        paper = make_wikilink(e["filename"])
        bench = truncate(e.get("benchmark_name", "N/A"), 50)
        plur = e.get("pluralistic_relevance", "N/A")
        avail_cat, _ = parse_availability(e.get("availability", ""))
        L.append(f"| {i} | {year} | {paper} | {bench} | {plur} | {avail_cat} |")
    L.append("")
    L.append("---")
    L.append("")

    # ── Appendix B: Normalization Definitions ────────────────────────────
    L.append("## Appendix B: Normalization Definitions")
    L.append("")
    L.append("### Model Families")
    L.append("")
    L.append("| Family | Regex Pattern |")
    L.append("|--------|--------------|")
    for fam, pattern in sorted(MODEL_FAMILIES.items()):
        L.append(f"| {fam} | `{pattern}` |")
    L.append("")

    L.append("### Methodology Types")
    L.append("")
    L.append("| Type | Regex Pattern |")
    L.append("|------|--------------|")
    for mtype, pattern in sorted(METHODOLOGY_TYPES.items()):
        L.append(f"| {mtype} | `{truncate(pattern, 80)}` |")
    L.append("")

    L.append("### Ethical Traditions")
    L.append("")
    L.append("| Tradition | Regex Pattern |")
    L.append("|-----------|--------------|")
    for trad, pattern in sorted(ETHICAL_TRADITIONS.items()):
        L.append(f"| {trad} | `{pattern}` |")
    L.append("")

    L.append("---")
    L.append("")
    L.append(f"*Generated: 2026-02-12 | Script: `PYTHON/generate_vault_overview_report.py` | "
             f"Papers: {landscape['candidates']}/{landscape['total']} candidates | "
             f"Categories: {len(CATEGORIES)}*")

    return "\n".join(L)


# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

def main():
    # ── Load data ──────────────────────────────────────────────────────
    print("Loading data sources...")

    with open(ALL_CLASSIFICATIONS_FILE, "r", encoding="utf-8") as f:
        all_entries = json.load(f)
    print(f"  All classifications: {len(all_entries)}")
    assert len(all_entries) == 924, f"Expected 924, got {len(all_entries)}"

    with open(CANDIDATES_FILE, "r", encoding="utf-8") as f:
        candidates = json.load(f)
    print(f"  Candidates: {len(candidates)}")
    assert len(candidates) == 528, f"Expected 528, got {len(candidates)}"

    with open(NORMATIVE_FILE, "r", encoding="utf-8") as f:
        normative_entries = json.load(f)
    print(f"  Normative v2: {len(normative_entries)}")
    assert len(normative_entries) == 266, f"Expected 266, got {len(normative_entries)}"

    with open(AUTHOR_MAP_FILE, "r", encoding="utf-8") as f:
        author_map = json.load(f)
    print(f"  Author map: {len(author_map)}")

    print("  Scanning paper YAML fields...")
    paper_yaml = scan_paper_yaml_fields()
    print(f"  Papers scanned: {len(paper_yaml)}")

    # ── Run analyses ──────────────────────────────────────────────────
    print("\nRunning analyses...")

    print("  Landscape...")
    landscape = analyze_landscape(all_entries, candidates, author_map)

    print("  Benchmark taxonomy...")
    taxonomy = analyze_benchmark_taxonomy(candidates)

    print("  Measurement approaches...")
    method_analysis = analyze_measurement_approaches(candidates)

    print("  Model coverage...")
    model_analysis = analyze_model_coverage(candidates)

    print("  Cultural & pluralistic...")
    cultural = analyze_cultural_pluralistic(candidates)

    print("  Data availability...")
    avail = analyze_data_availability(candidates)

    print("  Normative ethics deep dive...")
    normative = analyze_normative_deep_dive(normative_entries)

    print("  Ready-to-use resources...")
    ready = analyze_ready_resources(candidates)

    print("  LLM assessment coverage...")
    llm_assess = analyze_llm_assessment(paper_yaml)

    print("  Temporal trends...")
    trends = analyze_temporal_trends(all_entries, candidates)

    print("  Gap analysis...")
    gap_analysis = analyze_gaps(cultural, method_analysis, model_analysis)

    # ── Assemble report ───────────────────────────────────────────────
    print("\nAssembling report...")
    report = assemble_report(
        landscape, taxonomy, method_analysis, model_analysis, cultural,
        avail, normative, ready, llm_assess, trends, gap_analysis, candidates
    )

    # ── Write output ──────────────────────────────────────────────────
    STATS_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"\nReport written to {OUTPUT_FILE}")
    print(f"  Size: {len(report):,} characters, {report.count(chr(10)):,} lines")

    # ── Verification ──────────────────────────────────────────────────
    print("\n=== VERIFICATION ===")

    # Category completeness
    all_categorized = set()
    for cat_entries in taxonomy["cat_entries"].values():
        for e in cat_entries:
            all_categorized.add(e["filename"])
    all_cand_files = set(e["filename"] for e in candidates)
    uncategorized = all_cand_files - all_categorized
    print(f"  Category completeness: {len(all_categorized)}/{len(candidates)} "
          f"({'PASS' if not uncategorized else f'FAIL - {len(uncategorized)} uncategorized'})")

    # Normalization coverage
    model_cov = model_analysis["with_model"] * 100 // model_analysis["total"]
    method_cov = (method_analysis["total"] - method_analysis["no_method"]) * 100 // method_analysis["total"]
    print(f"  Model normalization: {model_cov}% ({'PASS' if model_cov >= 70 else 'LOW'})")
    print(f"  Method normalization: {method_cov}% ({'PASS' if method_cov >= 70 else 'LOW'})")

    # Table integrity (basic line-count check)
    table_lines = [line for line in report.split("\n") if line.startswith("|")]
    pipe_counts = Counter()
    for tl in table_lines:
        n_pipes = tl.count("|")
        pipe_counts[n_pipes] += 1
    print(f"  Table lines: {len(table_lines)}")

    # LLM assessment coverage
    print(f"  LLM assessment:      {llm_assess['with_models']}/{llm_assess['total']} papers with models "
          f"({llm_assess['with_models']*100//llm_assess['total']}%)")
    print(f"  DATA_URL coverage:   {llm_assess['with_urls']}/{llm_assess['total']} papers with URLs "
          f"({llm_assess['with_urls']*100//llm_assess['total']}%)")

    print("\n=== SUMMARY ===")
    print(f"  Papers screened:     {landscape['total']}")
    print(f"  Benchmark candidates: {landscape['candidates']}")
    print(f"  Normative papers:    {normative['yes_count']} Yes + {normative['borderline_count']} Borderline")
    print(f"  Model families found: {len(model_analysis['family_counts'])}")
    print(f"  Methodology types:   {len(method_analysis['method_counts'])}")
    print(f"  Ethical traditions:  {len(cultural['tradition_counts'])}")
    print(f"  Languages detected:  {len(cultural['lang_counts'])}")
    print(f"  Public benchmarks:   {avail['avail_counts'].get('Public', 0)}")
    print(f"  LLM models (YAML):   {llm_assess['with_models']} papers, {len(llm_assess['model_counter'])} unique models")
    print(f"  Data URLs:           {llm_assess['with_urls']} papers")
    print(f"  Report: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
