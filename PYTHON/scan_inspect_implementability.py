#!/usr/bin/env python3
"""
scan_inspect_implementability.py — Score vault papers on implementability
for the UK AISI's Inspect AI eval framework.

Key difference from scan_lm_eval_implementability.py: Inspect's model_graded_qa()
scorer makes rubric-based papers (moral dilemmas, ethical reasoning, vignettes)
viable candidates that lm-eval-harness cannot handle.  This adds a unique
MODEL_GRADED_CANDIDATE tier for such papers.

Usage:
    cd CEI-Lit-WS && ../.venv/bin/python PYTHON/scan_inspect_implementability.py

Author: CEI Literature Vault automation
Date: 2026-03-12
"""

import functools
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# Flushed print for progress reporting
print = functools.partial(print, flush=True)

# ---------------------------------------------------------------------------
# Path setup — ensure PYTHON/ is importable
# ---------------------------------------------------------------------------
_script_dir = Path(__file__).resolve().parent
if str(_script_dir) not in sys.path:
    sys.path.insert(0, str(_script_dir))

from vault_config import PAPERS_DIR, PDF_EXTRACTS_DIR, STATISTICS_DIR, LOGS_DIR

# Import known Inspect evals
try:
    from inspect_known_evals import KNOWN_INSPECT_EVALS, get_all_aliases as get_inspect_aliases
except ImportError:
    print("[WARN] inspect_known_evals module not found — Inspect matching disabled")
    KNOWN_INSPECT_EVALS = {}
    get_inspect_aliases = lambda: {}

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SURVEY_JSON = LOGS_DIR / "20260216-benchmark_survey_candidates.json"
LM_EVAL_JSON = LOGS_DIR / "20260312-lm-eval-implementability-data.json"

REPORT_PATH = STATISTICS_DIR / "20260312-inspect-eval-implementability-report.md"
OUTPUT_JSON = LOGS_DIR / "20260312-inspect-eval-implementability-data.json"

# ---------------------------------------------------------------------------
# Regex patterns — shared with lm-eval scanner
# ---------------------------------------------------------------------------
MC_PATTERNS = re.compile(
    r"multiple.?choice|multi.?choice|MCQ|MCQA|answer selection|"
    r"choose the (?:best|correct)|pick the (?:best|correct)|"
    r"n-way classification|forced.?choice",
    re.IGNORECASE,
)
QA_PATTERNS = re.compile(
    r"question.?answer|QA\b|reading comprehension|"
    r"extractive QA|open.?book|closed.?book",
    re.IGNORECASE,
)
CLASSIFICATION_PATTERNS = re.compile(
    r"\bclassif(?:ication|y|ied|ier)\b|sentiment analysis|"
    r"binary label|label prediction|text categori",
    re.IGNORECASE,
)
OPEN_GEN_PATTERNS = re.compile(
    r"open.?ended generat|free.?form|text generation|"
    r"generative evaluation|story generation|dialogue generation",
    re.IGNORECASE,
)
STANDARD_METRICS = re.compile(
    r"\b(?:accuracy|F1[\s-]?score|F1\b|BLEU|ROUGE|exact.?match|"
    r"perplexity|AUC|precision|recall|MCC|Matthews|BERTScore)\b",
    re.IGNORECASE,
)
SPLIT_PATTERNS = re.compile(
    r"\b(?:train(?:ing)?[\s/]+test|test[\s/]+train|train[\s/]+val|"
    r"validation split|dev(?:elopment)? set|test set|train set|"
    r"data split|k-fold)\b",
    re.IGNORECASE,
)
HF_URL_RE = re.compile(r"https?://huggingface\.co/datasets/[\w\-\.]+/[\w\-\.]+", re.IGNORECASE)
GITHUB_URL_RE = re.compile(r"https?://github\.com/[\w\-\.]+/[\w\-\.]+", re.IGNORECASE)
DATASET_SIZE_RE = re.compile(
    r"(\d[\d,\.]*)\s*(?:examples|instances|samples|questions|items|prompts|rows|entries|datapoints|data points)",
    re.IGNORECASE,
)
DATA_FORMAT_RE = re.compile(r"\b(?:JSONL|JSON|CSV|TSV|Parquet|HDF5|XML|YAML)\b", re.IGNORECASE)
PROMPT_HINT_RE = re.compile(r"(?:prompt|template|instruction)[\s:]+[\"'](.{10,120})[\"']", re.IGNORECASE)

# ---------------------------------------------------------------------------
# Inspect-specific regex patterns
# ---------------------------------------------------------------------------
RUBRIC_PATTERNS = re.compile(
    r"\brubric\b|scoring guide|annotation guide|inter.?annotator|"
    r"\bkappa\b|Cohen.?s?\s+kappa|grading criteria|evaluation rubric|"
    r"rating scheme|coding scheme|assessment criteria",
    re.IGNORECASE,
)
LIKERT_PATTERNS = re.compile(
    r"\blikert\b|1[\s-]to[\s-][57]\b|[57][\s-]point\s+scale|rating scale|"
    r"strongly (?:agree|disagree)|agree[\s/]+disagree|ordinal scale|"
    r"semantic differential",
    re.IGNORECASE,
)
VIGNETTE_PATTERNS = re.compile(
    r"\bvignette\b|moral (?:scenario|dilemma)|ethical (?:scenario|dilemma)|"
    r"\btrolley\b|thought experiment|hypothetical scenario|"
    r"moral judgment|value judgment|normative judgment|"
    r"moral (?:permissibility|impermissibility)|ethical vignette",
    re.IGNORECASE,
)
DIALOGUE_PATTERNS = re.compile(
    r"multi[\s-]?turn|dialogue|conversation(?:al)?\s+(?:eval|agent|AI)|"
    r"agent[\s-]?based|tool[\s-]?use|agentic\b",
    re.IGNORECASE,
)
LLM_BASELINE_RE = re.compile(
    r"\bGPT[\s-]?4\b|\bGPT[\s-]?3\.5\b|\bClaude\b|\bLlama[\s-]?\d\b|"
    r"\bGemini\b|\bChatGPT\b|\bPaLM\b|\bMistral\b|"
    r"large language model(?:s)?(?:\s+baseline)?",
    re.IGNORECASE,
)
HUMAN_BASELINE_RE = re.compile(
    r"human (?:baseline|performance|evaluation|judgment|judges?|annotator)|"
    r"crowd[\s-]?worker|MTurk|Mechanical Turk|Prolific\b|"
    r"expert[\s-]?annotator|human[\s-]?rater",
    re.IGNORECASE,
)

# ---------------------------------------------------------------------------
# Eval pattern classification
# ---------------------------------------------------------------------------
EVAL_PATTERNS = {
    "MULTIPLE_CHOICE": {
        "detect": MC_PATTERNS,
        "solver": "multiple_choice()",
        "scorer": "choice()",
    },
    "CLASSIFICATION": {
        "detect": CLASSIFICATION_PATTERNS,
        "solver": "generate()",
        "scorer": "match()",
    },
    "OPEN_QA": {
        "detect": QA_PATTERNS,
        "solver": "[chain_of_thought(), generate()]",
        "scorer": "model_graded_fact()",
    },
    "RUBRIC_GRADED": {
        "detect": RUBRIC_PATTERNS,
        "solver": "generate()",
        "scorer": "model_graded_qa()",
    },
    "LIKERT_SCALE": {
        "detect": LIKERT_PATTERNS,
        "solver": "generate()",
        "scorer": 'pattern(r"\\d")',
    },
    "MULTI_TURN_AGENT": {
        "detect": DIALOGUE_PATTERNS,
        "solver": "[use_tools(...), generate()]",
        "scorer": "custom_scorer",
    },
}


# =========================================================================
# 1. Load benchmark survey
# =========================================================================
def load_benchmark_survey():
    """Load survey JSON, return dict keyed by filename."""
    if not SURVEY_JSON.exists():
        print(f"[ERROR] Survey JSON not found: {SURVEY_JSON}")
        return {}
    data = json.loads(SURVEY_JSON.read_text(encoding="utf-8"))
    return {entry["filename"]: entry for entry in data if entry.get("decision") == "Yes"}


# =========================================================================
# 2. Load lm-eval cross-reference data
# =========================================================================
def load_lm_eval_scores():
    """Load lm-eval JSON for cross-reference, return dict keyed by filename."""
    if not LM_EVAL_JSON.exists():
        print(f"[WARN] lm-eval JSON not found: {LM_EVAL_JSON} — cross-reference disabled")
        return {}
    data = json.loads(LM_EVAL_JSON.read_text(encoding="utf-8"))
    # Handle both flat list and nested {papers: [...]} formats
    papers = data.get("papers", data) if isinstance(data, dict) else data
    return {p["filename"]: p for p in papers}


# =========================================================================
# 3. Parse frontmatter (safe line parser — NO PyYAML)
# =========================================================================
def parse_frontmatter(filepath):
    """Return (metadata_dict, full_content_string)."""
    content = filepath.read_text(encoding="utf-8")
    metadata = {}
    lines = content.split("\n")
    if lines and lines[0].strip() == "---":
        for line in lines[1:]:
            if line.strip() == "---":
                break
            if ":" in line:
                key, val = line.split(":", 1)
                metadata[key.strip()] = val.strip().strip('"')
    return metadata, content


# =========================================================================
# 4. Get PDF extract content
# =========================================================================
def get_pdf_content(year, author_last, title_short):
    """Find and return PDF extract text, searching within the year subdir."""
    year_str = str(year)
    year_dir = PDF_EXTRACTS_DIR / year_str
    if not year_dir.is_dir():
        candidates = list(PDF_EXTRACTS_DIR.glob(f"{year_str}*{author_last}*"))
    else:
        candidates = list(year_dir.glob(f"{year_str}*{author_last}*"))
    for c in candidates:
        if title_short.lower() in c.name.lower():
            try:
                return c.read_text(encoding="utf-8")
            except Exception:
                return ""
    return ""


# =========================================================================
# 5. Match to known Inspect evals
# =========================================================================
def match_to_inspect(meta, survey_entry):
    """
    Fuzzy-match benchmark_name and title against KNOWN_INSPECT_EVALS.
    Returns (eval_name, eval_info) or (None, None).
    """
    if not KNOWN_INSPECT_EVALS:
        return None, None

    bench_name = (survey_entry or {}).get("benchmark_name", "").lower().strip()
    title = meta.get("title", "").lower().strip()
    data_url = meta.get("DATA_URL", "").lower().strip()

    alias_map = get_inspect_aliases()

    # Direct alias match on benchmark name
    if bench_name:
        if bench_name in alias_map:
            key = alias_map[bench_name]
            return key, KNOWN_INSPECT_EVALS[key]
        # Partial match
        for alias, key in alias_map.items():
            if alias in bench_name or bench_name in alias:
                return key, KNOWN_INSPECT_EVALS[key]

    # Alias match on title
    if title:
        for alias, key in alias_map.items():
            if len(alias) >= 4 and alias in title:
                return key, KNOWN_INSPECT_EVALS[key]

    return None, None


# =========================================================================
# 6. Detect eval pattern
# =========================================================================
def detect_eval_pattern(search_text):
    """
    Classify the recommended Inspect implementation pattern.
    Returns (pattern_name, pattern_info) for the best match.
    Priority: MULTIPLE_CHOICE > CLASSIFICATION > OPEN_QA > RUBRIC_GRADED > LIKERT > MULTI_TURN
    But RUBRIC_GRADED can override if vignette patterns also match.
    """
    matches = []
    for pattern_name, info in EVAL_PATTERNS.items():
        if info["detect"].search(search_text):
            matches.append(pattern_name)

    if not matches:
        return None, None

    # If we have RUBRIC_GRADED and VIGNETTE_PATTERNS also match, prefer rubric
    has_vignette = VIGNETTE_PATTERNS.search(search_text) is not None
    has_rubric = "RUBRIC_GRADED" in matches

    if has_rubric and has_vignette and "MULTIPLE_CHOICE" not in matches:
        return "RUBRIC_GRADED", EVAL_PATTERNS["RUBRIC_GRADED"]

    # Priority ordering
    priority = ["MULTIPLE_CHOICE", "CLASSIFICATION", "OPEN_QA",
                "RUBRIC_GRADED", "LIKERT_SCALE", "MULTI_TURN_AGENT"]
    for p in priority:
        if p in matches:
            return p, EVAL_PATTERNS[p]

    return matches[0], EVAL_PATTERNS[matches[0]]


# =========================================================================
# 7. Score implementability (0-100, 6 dimensions)
# =========================================================================
def score_implementability(meta, survey_entry, content):
    """
    Score a paper 0-100 on Inspect AI implementability.
    Returns (total_score, dimension_scores_dict, signals_list).
    """
    signals = []
    dims = {
        "dataset": 0,       # 0-30
        "task_structure": 0, # 0-20
        "scoring": 0,        # 0-15
        "code_repro": 0,     # 0-15
        "baselines": 0,      # 0-10
        "cei_relevance": 0,  # 0-10
    }

    data_url = meta.get("DATA_URL", "").strip()
    abstract = meta.get("abstract", "")
    how_measures = (survey_entry or {}).get("how_measures", "")
    what_measures = (survey_entry or {}).get("what_measures", "")
    availability = (survey_entry or {}).get("availability", "")
    dataset_size = (survey_entry or {}).get("dataset_size", "")
    search_text = f"{abstract} {how_measures} {what_measures} {content[:3000]}"

    # ── Dimension 1: Dataset Availability (0-30) ─────────────────────────
    if data_url and "huggingface.co/datasets" in data_url.lower():
        dims["dataset"] += 15
        signals.append("HuggingFace dataset URL (+15)")
    if data_url and GITHUB_URL_RE.search(data_url):
        dims["dataset"] += 10
        signals.append("GitHub URL in DATA_URL (+10)")
    elif data_url and data_url.lower() not in ("", "n/a", "na", "none", "not available"):
        dims["dataset"] += 8
        signals.append("Has DATA_URL (+8)")

    avail_lower = (availability or "").lower()
    if "public" in avail_lower:
        dims["dataset"] += 5
        signals.append("Public availability (+5)")

    # ── Dimension 2: Task Structure (0-20) ───────────────────────────────
    structure_scored = False
    if MC_PATTERNS.search(search_text):
        dims["task_structure"] += 15
        signals.append("MC format (+15)")
        structure_scored = True
    elif CLASSIFICATION_PATTERNS.search(search_text):
        dims["task_structure"] += 12
        signals.append("Classification format (+12)")
        structure_scored = True
    elif QA_PATTERNS.search(search_text):
        dims["task_structure"] += 12
        signals.append("QA format (+12)")
        structure_scored = True

    # Inspect-specific: Likert and vignette/scenario formats
    if LIKERT_PATTERNS.search(search_text):
        bonus = 10 if not structure_scored else 5
        dims["task_structure"] += bonus
        signals.append(f"Likert/rating scale (+{bonus})")
        structure_scored = True
    if VIGNETTE_PATTERNS.search(search_text):
        bonus = 8 if not structure_scored else 4
        dims["task_structure"] += bonus
        signals.append(f"Vignette/scenario format (+{bonus})")
        structure_scored = True

    # Open-ended with rubric
    if not structure_scored and OPEN_GEN_PATTERNS.search(search_text):
        if RUBRIC_PATTERNS.search(search_text):
            dims["task_structure"] += 8
            signals.append("Open-ended with rubric (+8)")
        else:
            dims["task_structure"] += 4
            signals.append("Open-ended generation (+4)")

    # Cap dimension
    dims["task_structure"] = min(dims["task_structure"], 20)

    # ── Dimension 3: Scoring Feasibility (0-15) ──────────────────────────
    if STANDARD_METRICS.search(search_text):
        dims["scoring"] += 10
        signals.append("Standard metrics mentioned (+10)")
    if RUBRIC_PATTERNS.search(search_text):
        bonus = 8 if dims["scoring"] == 0 else 3
        dims["scoring"] += bonus
        signals.append(f"Rubric/scoring guide described (+{bonus})")
    if re.search(r"\bbinary\b.*\bjudg", search_text, re.IGNORECASE):
        dims["scoring"] += 3
        signals.append("Binary judgment format (+3)")
    if re.search(r"inter[\s-]?annotator|IAA\b|kappa", search_text, re.IGNORECASE):
        dims["scoring"] += 5
        signals.append("IAA/kappa reported (+5)")

    dims["scoring"] = min(dims["scoring"], 15)

    # ── Dimension 4: Code & Reproducibility (0-15) ───────────────────────
    if GITHUB_URL_RE.search(search_text):
        dims["code_repro"] += 10
        signals.append("GitHub repo mentioned (+10)")
    if dataset_size and dataset_size.lower() not in (
        "", "n/a", "na", "none", "not stated", "not explicitly stated",
        "not specified", "unknown",
    ):
        dims["code_repro"] += 5
        signals.append("Dataset size stated (+5)")
    if SPLIT_PATTERNS.search(search_text):
        dims["code_repro"] += 5
        signals.append("Data splits mentioned (+5)")

    dims["code_repro"] = min(dims["code_repro"], 15)

    # ── Dimension 5: Baseline Results (0-10) ─────────────────────────────
    if LLM_BASELINE_RE.search(search_text):
        dims["baselines"] += 7
        signals.append("LLM baselines reported (+7)")
    if not LLM_BASELINE_RE.search(search_text) and STANDARD_METRICS.search(search_text):
        # Non-LLM baselines (has metrics but no LLM mention)
        dims["baselines"] += 5
        signals.append("Non-LLM baselines (+5)")
    if HUMAN_BASELINE_RE.search(search_text):
        dims["baselines"] += 3
        signals.append("Human baseline reported (+3)")

    dims["baselines"] = min(dims["baselines"], 10)

    # ── Dimension 6: CEI Mission Relevance (0-10) ────────────────────────
    ethics = meta.get("ethics", "").strip().lower()
    if ethics == "yes":
        dims["cei_relevance"] += 3
        signals.append("ethics=Yes (+3)")

    # Check for moral psychology / cultural / religious tags
    tags_text = f"{meta.get('moral_psychology', '')} {meta.get('tags', '')} {meta.get('topic', '')}".lower()
    content_lower = content[:5000].lower()

    if any(kw in tags_text or kw in content_lower for kw in
           ["moral foundations", "mft", "moral psychology", "kohlberg", "moral development"]):
        dims["cei_relevance"] += 3
        signals.append("Moral psychology topic (+3)")
    if any(kw in tags_text or kw in content_lower for kw in
           ["cultural", "cross-cultural", "religious", "religion", "faith"]):
        dims["cei_relevance"] += 2
        signals.append("Cultural/religious topic (+2)")

    # Gap area bonus: trolley, non-Western ethics, religious values
    gap_keywords = ["trolley", "moral machine", "autonomous vehicle dilemma",
                    "confucian", "buddhist", "islamic ethics", "hindu ethics",
                    "african ethics", "ubuntu", "indigenous"]
    if any(kw in content_lower for kw in gap_keywords):
        dims["cei_relevance"] += 2
        signals.append("Gap area (underrepresented in evals) (+2)")

    dims["cei_relevance"] = min(dims["cei_relevance"], 10)

    total = sum(dims.values())
    return min(total, 100), dims, signals


# =========================================================================
# 8. Extract implementation details from PDF extract
# =========================================================================
def extract_impl_details_from_pdf(meta):
    """For high-scoring papers, mine the PDF extract for implementation hints."""
    year = meta.get("year", "")
    authors = meta.get("authors", meta.get("author", ""))
    title = meta.get("title", "")

    author_last = ""
    if authors:
        first_author = authors.split(";")[0].strip()
        parts = first_author.split(",")
        author_last = parts[0].strip().split()[-1] if parts else ""

    title_short = title[:15] if title else ""

    pdf_text = get_pdf_content(year, author_last, title_short)
    if not pdf_text:
        return {}

    # Limit to first 8000 chars for deep scan
    pdf_text = pdf_text[:8000]

    details = {}

    # Data format
    formats_found = DATA_FORMAT_RE.findall(pdf_text)
    if formats_found:
        details["data_format"] = list(set(f.upper() for f in formats_found))

    # Splits
    splits = set()
    for m in re.finditer(r"\b(train|test|val(?:idation)?|dev(?:elopment)?)\b", pdf_text, re.IGNORECASE):
        normalized = m.group(1).lower()
        if normalized.startswith("val"):
            normalized = "validation"
        elif normalized.startswith("dev"):
            normalized = "dev"
        splits.add(normalized)
    if splits:
        details["splits"] = sorted(splits)

    # Metrics
    metrics_found = STANDARD_METRICS.findall(pdf_text)
    if metrics_found:
        details["metrics"] = list(set(m.lower() for m in metrics_found))

    # HuggingFace URLs
    hf_urls = HF_URL_RE.findall(pdf_text)
    if hf_urls:
        details["hf_urls"] = list(set(hf_urls))

    # GitHub URLs
    gh_urls = GITHUB_URL_RE.findall(pdf_text)
    if gh_urls:
        details["github_urls"] = list(set(gh_urls))

    # Dataset size mentions
    sizes = DATASET_SIZE_RE.findall(pdf_text)
    if sizes:
        details["dataset_size"] = list(set(sizes[:5]))

    # Prompt hints
    hints = PROMPT_HINT_RE.findall(pdf_text)
    if hints:
        details["prompt_hints"] = list(set(hints[:3]))

    # Inspect-specific: rubric text snippets
    rubric_hits = RUBRIC_PATTERNS.findall(pdf_text) if hasattr(RUBRIC_PATTERNS, 'findall') else []
    if RUBRIC_PATTERNS.search(pdf_text):
        details["has_rubric"] = True

    # Vignette/scenario detection
    if VIGNETTE_PATTERNS.search(pdf_text):
        details["has_vignettes"] = True

    # Likert scale detection
    if LIKERT_PATTERNS.search(pdf_text):
        details["has_likert"] = True

    # LLM baselines
    llm_matches = LLM_BASELINE_RE.findall(pdf_text)
    if llm_matches:
        details["llm_baselines"] = list(set(llm_matches[:5]))

    # Human baselines
    if HUMAN_BASELINE_RE.search(pdf_text):
        details["has_human_baseline"] = True

    return details


# =========================================================================
# 9. Classify tier
# =========================================================================
def classify_tier(score, in_inspect, has_public_dataset, has_rubric_or_vignette):
    """Assign a tier label. MODEL_GRADED_CANDIDATE is unique to Inspect."""
    if in_inspect:
        return "ALREADY_IN_INSPECT"
    if score >= 60 and (has_public_dataset or score >= 75):
        return "READY_TO_IMPLEMENT"
    if score >= 45 and has_rubric_or_vignette:
        return "MODEL_GRADED_CANDIDATE"
    if score >= 35:
        return "NEEDS_DATASET_WORK"
    if score >= 20:
        return "NEEDS_MORE_INFO"
    return "NOT_IMPLEMENTABLE"


# =========================================================================
# 10. Generate Inspect eval sketch
# =========================================================================
def generate_inspect_sketch(paper_info):
    """Generate a Python Inspect eval sketch for a paper."""
    meta = paper_info["meta"]
    survey = paper_info.get("survey", {}) or {}
    details = paper_info.get("impl_details", {})
    eval_pattern = paper_info.get("eval_pattern")
    pattern_info = paper_info.get("eval_pattern_info", {}) or {}
    bench = survey.get("benchmark_name", meta.get("title", "unknown"))

    # Derive task name
    task_name = re.sub(r"[^a-z0-9]+", "_", bench.lower()).strip("_")

    # Dataset loader
    hf_urls = details.get("hf_urls", [])
    data_url = meta.get("DATA_URL", "")
    if hf_urls:
        dataset_path = hf_urls[0].replace("https://huggingface.co/datasets/", "")
        dataset_loader = f'hf_dataset("{dataset_path}")'
    elif "huggingface.co/datasets" in (data_url or ""):
        dataset_path = data_url.split("huggingface.co/datasets/")[-1].split("?")[0]
        dataset_loader = f'hf_dataset("{dataset_path}")'
    elif data_url and data_url.lower() not in ("", "n/a", "na", "none"):
        dataset_loader = f'csv_dataset("{data_url}")  # TODO: verify format'
    else:
        dataset_loader = f'csv_dataset("<NEEDS_HOSTING>")  # TODO: host dataset'

    # Solver and scorer from pattern
    solver = pattern_info.get("solver", "generate()")
    scorer = pattern_info.get("scorer", "model_graded_qa()")

    sketch = f'''from inspect_ai import task, Task
from inspect_ai.dataset import hf_dataset, csv_dataset
from inspect_ai.scorer import choice, match, model_graded_qa, model_graded_fact, pattern
from inspect_ai.solver import multiple_choice, generate, chain_of_thought

@task
def {task_name}():
    """
    {bench}
    Paper: {meta.get('title', 'N/A')[:80]}
    What it measures: {survey.get('what_measures', 'N/A')[:100]}
    """
    return Task(
        dataset={dataset_loader},
        solver={solver},
        scorer={scorer},
    )'''

    return sketch


# =========================================================================
# 11. Generate markdown report
# =========================================================================
def generate_report(results, lm_eval_scores):
    """Write the tiered markdown report."""
    tier_order = [
        "ALREADY_IN_INSPECT",
        "READY_TO_IMPLEMENT",
        "MODEL_GRADED_CANDIDATE",
        "NEEDS_DATASET_WORK",
        "NEEDS_MORE_INFO",
        "NOT_IMPLEMENTABLE",
    ]
    tiers = {t: [] for t in tier_order}
    for r in results:
        tiers[r["tier"]].append(r)

    lines = []
    lines.append("# Inspect AI Eval Implementability Report")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")

    # ── Executive Summary ─────────────────────────────────────────────────
    lines.append("## Executive Summary")
    lines.append("")
    tier_labels = {
        "ALREADY_IN_INSPECT": "Already in Inspect",
        "READY_TO_IMPLEMENT": "Ready to Implement",
        "MODEL_GRADED_CANDIDATE": "Model-Graded Candidate (Inspect-unique)",
        "NEEDS_DATASET_WORK": "Needs Dataset Work",
        "NEEDS_MORE_INFO": "Needs More Info",
        "NOT_IMPLEMENTABLE": "Not Implementable",
    }
    lines.append("| Tier | Count |")
    lines.append("|------|-------|")
    total_scored = sum(len(v) for v in tiers.values())
    for tier_key in tier_order:
        lines.append(f"| {tier_labels[tier_key]} | {len(tiers[tier_key])} |")
    lines.append(f"| **Total scored** | **{total_scored}** |")
    lines.append("")

    # Comparison with lm-eval
    if lm_eval_scores:
        lines.append("### Comparison with lm-eval-harness Scanner")
        lines.append("")
        both_ready = 0
        inspect_only = 0
        lm_eval_only = 0
        inspect_ready_set = set()
        for r in tiers["READY_TO_IMPLEMENT"] + tiers["MODEL_GRADED_CANDIDATE"]:
            inspect_ready_set.add(r["filename"])
        for r in tiers["READY_TO_IMPLEMENT"] + tiers["MODEL_GRADED_CANDIDATE"]:
            lm = lm_eval_scores.get(r["filename"], {})
            lm_tier = lm.get("tier", "")
            if lm_tier == "READY_TO_IMPLEMENT":
                both_ready += 1
            else:
                inspect_only += 1
        for fn, lm in lm_eval_scores.items():
            if lm.get("tier") == "READY_TO_IMPLEMENT" and fn not in inspect_ready_set:
                lm_eval_only += 1
        lines.append(f"- Papers viable in **both** frameworks: {both_ready}")
        lines.append(f"- Papers viable **only in Inspect** (model-graded): {inspect_only}")
        lines.append(f"- Papers viable **only in lm-eval**: {lm_eval_only}")
        lines.append("")

    # ── Section 1: Already in Inspect ─────────────────────────────────────
    lines.append("## 1. Already in Inspect")
    lines.append("")
    if tiers["ALREADY_IN_INSPECT"]:
        lines.append("| Paper | Inspect Eval | Category | Scorer |")
        lines.append("|-------|-------------|----------|--------|")
        for r in tiers["ALREADY_IN_INSPECT"]:
            eval_name = r.get("inspect_match", "?")
            eval_info = r.get("inspect_info", {}) or {}
            cat = eval_info.get("category", "?")
            scorer = eval_info.get("scorer", "?")
            lines.append(f"| {r['filename']} | {eval_name} | {cat} | {scorer} |")
    else:
        lines.append("No papers matched known Inspect evals.")
    lines.append("")

    # ── Section 2: Ready to Implement ─────────────────────────────────────
    ready = sorted(tiers["READY_TO_IMPLEMENT"], key=lambda x: x["score"], reverse=True)
    lines.append("## 2. Ready to Implement (score >= 60 + public data)")
    lines.append("")
    if ready:
        lines.append("| Paper | Benchmark | Score | Eval Pattern | Data URL | Key Signals |")
        lines.append("|-------|-----------|-------|-------------|----------|-------------|")
        for r in ready:
            bench = (r.get("survey", {}) or {}).get("benchmark_name", "—")
            data_url = r["meta"].get("DATA_URL", "—")
            sigs = ", ".join(s.split(" (+")[0] for s in r.get("signals", [])[:5])
            ep = r.get("eval_pattern", "?")
            lines.append(f"| {r['filename']} | {bench} | {r['score']} | {ep} | {data_url} | {sigs} |")
        lines.append("")

        # Implementation sketches for top 10
        lines.append("### Implementation Sketches (Top 10)")
        lines.append("")
        for r in ready[:10]:
            sketch = generate_inspect_sketch(r)
            lines.append(f"#### {r['filename']}")
            lines.append("")
            lines.append("```python")
            lines.append(sketch)
            lines.append("```")
            lines.append("")
    else:
        lines.append("No papers in this tier.")
    lines.append("")

    # ── Section 3: Model-Graded Candidates ────────────────────────────────
    model_graded = sorted(tiers["MODEL_GRADED_CANDIDATE"], key=lambda x: x["score"], reverse=True)
    lines.append("## 3. Model-Graded Candidates (Inspect-unique tier)")
    lines.append("")
    lines.append("> These papers have rubrics, vignettes, or moral scenarios that Inspect's")
    lines.append("> `model_graded_qa()` scorer can handle, but lm-eval-harness cannot.")
    lines.append("")
    if model_graded:
        lines.append("| Paper | Benchmark | Score | Pattern | Why Model-Graded | lm-eval Score |")
        lines.append("|-------|-----------|-------|---------|-----------------|---------------|")
        for r in model_graded:
            bench = (r.get("survey", {}) or {}).get("benchmark_name", "—")
            ep = r.get("eval_pattern", "?")
            # Extract rubric/vignette signals
            mg_reasons = [s.split(" (+")[0] for s in r.get("signals", [])
                          if any(kw in s.lower() for kw in ("rubric", "vignette", "likert", "scenario"))]
            mg_str = ", ".join(mg_reasons) or "rubric/scenario detected"
            lm_score = lm_eval_scores.get(r["filename"], {}).get("score", "—")
            lines.append(f"| {r['filename']} | {bench} | {r['score']} | {ep} | {mg_str} | {lm_score} |")
    else:
        lines.append("No papers in this tier.")
    lines.append("")

    # ── Section 4: Gap Analysis ───────────────────────────────────────────
    lines.append("## 4. Gap Analysis — CEI Focus Areas")
    lines.append("")
    lines.append("Which CEI focus areas have Inspect evals vs. gaps?")
    lines.append("")

    focus_areas = {
        "Moral Foundations Theory (MFT)": ["moral foundations", "mft", "haidt", "moral foundation"],
        "Trolley Problems / Moral Machine": ["trolley", "moral machine", "autonomous vehicle dilemma"],
        "Kohlberg Moral Development": ["kohlberg", "moral development", "moral reasoning stage"],
        "Cultural Values": ["cross-cultural", "cultural values", "hofstede", "world values survey", "inglehart"],
        "Religious Values": ["religious", "religion", "faith", "theological", "confucian", "buddhist", "islamic", "hindu"],
        "Normative Ethics": ["deontolog", "utilitari", "virtue ethics", "consequential"],
        "Moral Psychology": ["moral psychology", "moral judgment", "moral cognition", "moral emotion"],
    }

    all_viable = tiers["READY_TO_IMPLEMENT"] + tiers["MODEL_GRADED_CANDIDATE"] + tiers["ALREADY_IN_INSPECT"]

    lines.append("| Focus Area | Viable Papers | Already in Inspect | Gap? |")
    lines.append("|-----------|--------------|-------------------|------|")
    for area, keywords in focus_areas.items():
        viable = []
        already = []
        for r in all_viable:
            text = f"{r['meta'].get('title', '')} {r['meta'].get('abstract', '')} {(r.get('survey') or {}).get('what_measures', '')}".lower()
            if any(kw in text for kw in keywords):
                viable.append(r["filename"])
                if r["tier"] == "ALREADY_IN_INSPECT":
                    already.append(r["filename"])
        gap = "YES — GAP" if not already and len(viable) <= 1 else ("Partial" if not already else "Covered")
        lines.append(f"| {area} | {len(viable)} | {len(already)} | {gap} |")
    lines.append("")

    # ── Section 5: Needs Dataset Work ─────────────────────────────────────
    dataset_work = sorted(tiers["NEEDS_DATASET_WORK"], key=lambda x: x["score"], reverse=True)
    lines.append("## 5. Needs Dataset Work (score 35-59)")
    lines.append("")
    if dataset_work:
        lines.append("| Paper | Score | What's Missing |")
        lines.append("|-------|-------|----------------|")
        for r in dataset_work[:30]:  # Cap at 30 rows
            present = set(s.split(" (+")[0] for s in r.get("signals", []))
            missing = []
            if not any("HuggingFace" in s for s in r.get("signals", [])):
                missing.append("No HF dataset")
            if not any("split" in s.lower() for s in r.get("signals", [])):
                missing.append("No splits info")
            if not any("size" in s.lower() for s in r.get("signals", [])):
                missing.append("Size unknown")
            lines.append(f"| {r['filename']} | {r['score']} | {'; '.join(missing) or '—'} |")
        if len(dataset_work) > 30:
            lines.append(f"| ... and {len(dataset_work) - 30} more | | |")
    else:
        lines.append("No papers in this tier.")
    lines.append("")

    # ── Section 6: Needs More Info ────────────────────────────────────────
    more_info = tiers["NEEDS_MORE_INFO"]
    lines.append("## 6. Needs More Info (score 20-34)")
    lines.append(f"\n{len(more_info)} papers in this tier (summary only).")
    lines.append("")

    # ── Section 7: Not Implementable ──────────────────────────────────────
    not_impl = tiers["NOT_IMPLEMENTABLE"]
    lines.append("## 7. Not Implementable (score < 20)")
    lines.append(f"\n{len(not_impl)} papers in this tier (summary only).")
    lines.append("")

    report_text = "\n".join(lines)
    REPORT_PATH.write_text(report_text, encoding="utf-8")
    print(f"Report written: {REPORT_PATH}")


# =========================================================================
# 12. Save JSON
# =========================================================================
def save_json(results, lm_eval_scores):
    """Write structured JSON output."""
    tier_counts = {}
    for r in results:
        tier_counts[r["tier"]] = tier_counts.get(r["tier"], 0) + 1

    out_papers = []
    for r in results:
        lm_data = lm_eval_scores.get(r["filename"], {})
        entry = {
            "filename": r["filename"],
            "score": r["score"],
            "tier": r["tier"],
            "eval_pattern": r.get("eval_pattern"),
            "dimensions": r.get("dimensions", {}),
            "signals": r.get("signals", []),
            "inspect_match": r.get("inspect_match"),
            "lm_eval_score": lm_data.get("score"),
            "lm_eval_tier": lm_data.get("tier"),
            "benchmark_name": (r.get("survey") or {}).get("benchmark_name"),
            "data_url": r["meta"].get("DATA_URL", ""),
            "impl_details": r.get("impl_details", {}),
            "inspect_sketch": r.get("sketch"),
            "year": r["meta"].get("year", ""),
        }
        out_papers.append(entry)

    output = {
        "generated": datetime.now().isoformat(),
        "summary": {
            "total_scored": len(results),
            "tier_counts": tier_counts,
            "known_inspect_evals": len(KNOWN_INSPECT_EVALS),
        },
        "papers": out_papers,
    }
    OUTPUT_JSON.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"JSON written: {OUTPUT_JSON}")


# =========================================================================
# Main
# =========================================================================
def main():
    print("=" * 60)
    print("Inspect AI Eval Implementability Scanner")
    print("=" * 60)
    print()

    # 1. Load survey
    print("Loading benchmark survey...")
    survey = load_benchmark_survey()
    print(f"  Survey entries (decision=Yes): {len(survey)}")

    # 2. Load lm-eval cross-reference
    print("Loading lm-eval cross-reference data...")
    lm_eval_scores = load_lm_eval_scores()
    print(f"  lm-eval entries loaded: {len(lm_eval_scores)}")

    # 3. Known Inspect evals
    print(f"  Known Inspect evals: {len(KNOWN_INSPECT_EVALS)}")
    print()

    # 4. Scan all papers
    paper_files = sorted(PAPERS_DIR.glob("*.md"))
    paper_files = [f for f in paper_files if f.name not in ("README.md", "TEMPLATE.md")]
    print(f"Scanning {len(paper_files)} papers...")
    print()

    results = []

    for i, filepath in enumerate(paper_files, 1):
        if i % 200 == 0:
            print(f"  ... processed {i}/{len(paper_files)} papers")

        meta, content = parse_frontmatter(filepath)
        filename = filepath.name
        survey_entry = survey.get(filename)

        # Match to Inspect
        inspect_match, inspect_info = match_to_inspect(meta, survey_entry)
        in_inspect = inspect_match is not None

        # Score
        score, dims, signals = score_implementability(meta, survey_entry, content)

        # Detect eval pattern
        abstract = meta.get("abstract", "")
        how_measures = (survey_entry or {}).get("how_measures", "")
        what_measures = (survey_entry or {}).get("what_measures", "")
        search_text = f"{abstract} {how_measures} {what_measures}"
        eval_pattern, eval_pattern_info = detect_eval_pattern(search_text)

        # Determine tier
        data_url = meta.get("DATA_URL", "")
        has_public_dataset = (
            ("huggingface.co/datasets" in (data_url or "").lower())
            or ("public" in (survey_entry or {}).get("availability", "").lower())
        )
        has_rubric_or_vignette = (
            RUBRIC_PATTERNS.search(search_text) is not None
            or VIGNETTE_PATTERNS.search(search_text) is not None
        )
        tier = classify_tier(score, in_inspect, has_public_dataset, has_rubric_or_vignette)

        result = {
            "filename": filename,
            "meta": meta,
            "survey": survey_entry,
            "score": score,
            "dimensions": dims,
            "signals": signals,
            "tier": tier,
            "eval_pattern": eval_pattern,
            "eval_pattern_info": eval_pattern_info,
            "inspect_match": inspect_match,
            "inspect_info": inspect_info,
            "impl_details": {},
            "sketch": None,
        }
        results.append(result)

    print(f"Scored {len(results)} papers.")
    print()

    # 5. Extract impl details for candidates scoring >= 40
    high_scorers = [r for r in results if r["score"] >= 40]
    print(f"Extracting implementation details for {len(high_scorers)} papers (score >= 40)...")
    for r in high_scorers:
        r["impl_details"] = extract_impl_details_from_pdf(r["meta"])

    # 6. Generate sketches for score >= 50
    sketch_candidates = [r for r in results if r["score"] >= 50 and r["tier"] != "ALREADY_IN_INSPECT"]
    print(f"Generating Inspect eval sketches for {len(sketch_candidates)} papers (score >= 50)...")
    for r in sketch_candidates:
        r["sketch"] = generate_inspect_sketch(r)

    # 7. Sort by score descending
    results.sort(key=lambda x: x["score"], reverse=True)

    # Summary
    tier_counts = {}
    for r in results:
        tier_counts[r["tier"]] = tier_counts.get(r["tier"], 0) + 1
    print()
    print("Tier Summary:")
    tier_order = [
        "ALREADY_IN_INSPECT", "READY_TO_IMPLEMENT", "MODEL_GRADED_CANDIDATE",
        "NEEDS_DATASET_WORK", "NEEDS_MORE_INFO", "NOT_IMPLEMENTABLE",
    ]
    for tier_name in tier_order:
        print(f"  {tier_name}: {tier_counts.get(tier_name, 0)}")
    print()

    # Eval pattern distribution
    pattern_counts = {}
    for r in results:
        p = r.get("eval_pattern") or "NONE"
        pattern_counts[p] = pattern_counts.get(p, 0) + 1
    print("Eval Pattern Distribution:")
    for p, c in sorted(pattern_counts.items(), key=lambda x: -x[1]):
        print(f"  {p}: {c}")
    print()

    # 8. Generate report and JSON
    generate_report(results, lm_eval_scores)
    save_json(results, lm_eval_scores)

    print()
    print("Done.")


if __name__ == "__main__":
    main()
