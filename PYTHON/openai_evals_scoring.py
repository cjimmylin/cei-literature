#!/usr/bin/env python3
"""
openai_evals_scoring.py — Shared scoring module for OpenAI Evals implementability.

Scores vault papers on 9 dimensions (0-10 scale) measuring how feasible
each paper's benchmark/dataset is to implement as an OpenAI Evals evaluation.

OpenAI Evals uses JSONL data + YAML registry configs with template types:
Match, FuzzyMatch, Includes, JsonMatch, ModelBasedClassify.
ModelBasedClassify is especially relevant for ethics papers with open-ended
moral reasoning (uses an LLM judge with a rubric).

Used by: scan_openai_evals_implementability.py, generate_openai_evals_report.py
"""

import re

# ── Dimension definitions ────────────────────────────────────────────────────

DIMENSIONS = [
    {"id": "D1", "name": "Dataset exists",          "weight": 1.5, "max": 1.0},
    {"id": "D2", "name": "Data publicly available",  "weight": 1.5, "max": 1.0},
    {"id": "D3", "name": "JSONL-convertible format", "weight": 1.5, "max": 1.0},
    {"id": "D4", "name": "Code/repo available",      "weight": 1.0, "max": 1.0},
    {"id": "D5", "name": "Clear eval metrics",       "weight": 1.0, "max": 1.0},
    {"id": "D6", "name": "Quantified data size",     "weight": 0.5, "max": 1.0},
    {"id": "D7", "name": "LLM evaluation exists",    "weight": 0.5, "max": 1.0},
    {"id": "D8", "name": "Eval template mappable",   "weight": 1.5, "max": 1.0},
    {"id": "D9", "name": "Full text available",      "weight": 1.0, "max": 1.0},
]

TOTAL_WEIGHT = sum(d["weight"] for d in DIMENSIONS)  # 10.0

# ── Tier thresholds ──────────────────────────────────────────────────────────

TIERS = [
    ("Ready",             8.0, 10.01),
    ("Possible",          5.0,  8.0),
    ("Barriers",          2.0,  5.0),
    ("Not Implementable", 0.0,  2.0),
]


def classify_tier(score: float) -> str:
    for name, lo, hi in TIERS:
        if lo <= score < hi:
            return name
    return "Not Implementable"


# ── Signal normalization helpers ─────────────────────────────────────────────

def _norm_signal(s: str) -> str:
    """Strip score suffix like '(+25)' and normalize whitespace."""
    return re.sub(r'\s*\(\+\d+\)', '', s).strip()


def _signals_set(paper: dict) -> set:
    """Return normalized signal strings as a set."""
    return {_norm_signal(s) for s in paper.get("signals", [])}


def _has_signal(signals: set, *patterns: str) -> bool:
    """Check if any signal matches any of the given substrings (case-insensitive)."""
    for sig in signals:
        sl = sig.lower()
        for pat in patterns:
            if pat.lower() in sl:
                return True
    return False


# ── Task type detection patterns (reused from scan_lm_eval) ─────────────────

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
RUBRIC_PATTERNS = re.compile(
    r"\brubric\b|scoring (?:guide|criteria)|evaluation criteria|"
    r"grading scheme|annotation (?:guide|scheme)|judgment criteria|"
    r"likert scale|rating scale|\b[1-5]\s*[-=]\s*\w+",
    re.IGNORECASE,
)
ETHICS_SCENARIO_PATTERNS = re.compile(
    r"moral (?:dilemma|scenario|vignette|judgment)|ethical (?:dilemma|scenario|judgment)|"
    r"trolley problem|value alignment|moral reasoning",
    re.IGNORECASE,
)
OPEN_GEN_PATTERNS = re.compile(
    r"open.?ended generat|free.?form|text generation|"
    r"generative evaluation|story generation|dialogue generation",
    re.IGNORECASE,
)


# ── Dimension scorers ────────────────────────────────────────────────────────

def _score_d1(paper: dict, signals: set) -> float:
    """D1: Dataset exists (is_benchmark/is_dataset or benchmark/dataset signals)."""
    if _has_signal(signals, "is_benchmark"):
        return 1.0
    if _has_signal(signals, "is_dataset"):
        return 1.0
    if _has_signal(signals, "benchmark", "dataset"):
        return 0.5
    sd = paper.get("survey_data")
    if sd and sd.get("benchmark_name"):
        return 0.5
    return 0.0


def _score_d2(paper: dict, signals: set) -> float:
    """D2: Data publicly available (DATA_URL + availability)."""
    has_url = _has_signal(signals, "data_url", "has data_url", "any data_url")
    has_public = _has_signal(signals, "public availability", "availability = public")

    sd = paper.get("survey_data")
    if sd:
        if (sd.get("availability") or "").lower() in ("public", "public (open-source)"):
            has_public = True

    if has_url and has_public:
        return 1.0
    if has_url or has_public:
        return 0.5
    return 0.0


def _score_d3(paper: dict, signals: set) -> float:
    """D3: JSONL-convertible format — structured data that maps to input/ideal JSONL.

    MCQ and QA formats are directly convertible (score 1.0).
    Classification tasks are straightforward (0.85).
    Ethics scenarios with rubrics can be converted with some effort (0.6).
    Open-ended generation needs significant work (0.3).
    """
    impl = paper.get("impl_details")
    task_types = []
    if impl:
        tt = impl.get("task_type")
        if tt:
            task_types = tt if isinstance(tt, list) else [tt]

    types_lower = [t.lower() for t in task_types if t]

    # MCQ / QA → directly convertible to input/ideal pairs
    if any(t in ("multiple_choice", "multichoice") for t in types_lower):
        return 1.0
    if "qa" in types_lower:
        return 1.0

    # Classification → straightforward conversion
    if "classification" in types_lower:
        return 0.85

    # Signal-based fallback
    if _has_signal(signals, "multiple-choice", "mcq"):
        return 1.0
    if _has_signal(signals, "qa format"):
        return 1.0
    if _has_signal(signals, "classification format"):
        return 0.85

    # Ethics scenarios (rubric-based) → convertible with rubric extraction
    if _has_signal(signals, "ethics scenario", "moral scenario", "rubric"):
        return 0.6

    # Open-ended generation → harder but possible with ModelBasedClassify
    if any(t in ("generate_until", "generation") for t in types_lower):
        return 0.4
    if _has_signal(signals, "open-ended generation"):
        return 0.3

    # Has a dataset but format unclear
    if _has_signal(signals, "is_dataset", "is_benchmark"):
        return 0.3

    return 0.0


def _score_d4(paper: dict, signals: set) -> float:
    """D4: Code/repo available."""
    if _has_signal(signals, "code available"):
        return 1.0
    impl = paper.get("impl_details")
    if impl:
        gh = impl.get("github_urls", [])
        if gh and any(gh):
            return 1.0
    sd = paper.get("survey_data")
    if sd and "code" in (sd.get("availability") or "").lower():
        return 1.0
    return 0.0


def _score_d5(paper: dict, signals: set) -> float:
    """D5: Clear eval metrics."""
    has_eval = _has_signal(signals, "is_eval")
    has_metrics = _has_signal(signals, "standard metrics", "data_metrics")

    impl = paper.get("impl_details")
    if impl:
        metrics = impl.get("metrics", [])
        if metrics and any(metrics):
            has_metrics = True

    if has_eval and has_metrics:
        return 1.0
    if has_eval or has_metrics:
        return 0.5
    return 0.0


def _score_d6(paper: dict, signals: set) -> float:
    """D6: Quantified data size."""
    if _has_signal(signals, "dataset size"):
        return 1.0
    impl = paper.get("impl_details")
    if impl:
        ds = impl.get("dataset_size")
        if ds and ds not in (None, [], ""):
            return 1.0
    return 0.0


def _score_d7(paper: dict, signals: set) -> float:
    """D7: LLM evaluation exists."""
    if _has_signal(signals, "llm_assessed"):
        return 1.0
    return 0.0


def _score_d8(paper: dict, signals: set) -> float:
    """D8: Eval template mappable — maps to OpenAI Evals template type.

    Template mapping:
      MCQ / forced-choice         → Match          → 1.0
      QA with exact answers       → Match/FuzzyMatch → 1.0
      Classification (binary/multi) → Match/Includes → 0.85
      Ethics scenarios with rubrics → ModelBasedClassify → 0.75
      Open-ended moral reasoning  → ModelBasedClassify → 0.6
      Free-form generation (rubric) → ModelBasedClassify → 0.4
      No clear task structure     → N/A            → 0.0
    """
    impl = paper.get("impl_details")
    task_types = []
    if impl:
        tt = impl.get("task_type")
        if tt:
            task_types = tt if isinstance(tt, list) else [tt]

    types_lower = [t.lower() for t in task_types if t]

    # MCQ → Match template
    if any(t in ("multiple_choice", "multichoice") for t in types_lower):
        return 1.0
    # QA → Match/FuzzyMatch
    if "qa" in types_lower:
        return 1.0
    # Classification → Match/Includes
    if "classification" in types_lower:
        return 0.85

    # Signal-based detection
    if _has_signal(signals, "multiple-choice", "mcq"):
        return 1.0
    if _has_signal(signals, "qa format"):
        return 1.0
    if _has_signal(signals, "classification format"):
        return 0.85

    # Ethics scenarios + rubric → ModelBasedClassify (strong match)
    has_rubric = _has_signal(signals, "rubric", "scoring criteria")
    has_ethics = _has_signal(signals, "ethics scenario", "moral scenario")
    if has_ethics and has_rubric:
        return 0.75
    if has_ethics:
        return 0.6

    # Open-ended generation with rubric → ModelBasedClassify (weaker)
    if _has_signal(signals, "open-ended generation"):
        return 0.4 if has_rubric else 0.3

    # General generation tasks
    if any(t in ("generate_until", "generation") for t in types_lower):
        return 0.4 if has_rubric else 0.3

    return 0.0


def _score_d9(paper: dict, signals: set) -> float:
    """D9: Full text available (PDF extract exists with methodology details)."""
    if paper.get("impl_details") is not None:
        return 1.0
    return 0.0


_SCORERS = [_score_d1, _score_d2, _score_d3, _score_d4, _score_d5,
            _score_d6, _score_d7, _score_d8, _score_d9]


# ── OpenAI Evals template mapping ───────────────────────────────────────────

def map_oai_eval_template(paper: dict) -> str:
    """Map paper to the most appropriate OpenAI Evals template type."""
    impl = paper.get("impl_details")
    task_types = []
    if impl:
        tt = impl.get("task_type")
        if tt:
            task_types = tt if isinstance(tt, list) else [tt]

    types_lower = [t.lower() for t in task_types if t]

    # MCQ → Match
    if any(t in ("multiple_choice", "multichoice") for t in types_lower):
        return "Match"

    # QA → FuzzyMatch (allows minor variations)
    if "qa" in types_lower:
        return "FuzzyMatch"

    # Classification → Match (exact label matching)
    if "classification" in types_lower:
        return "Match"

    signals = _signals_set(paper)

    if _has_signal(signals, "multiple-choice", "mcq"):
        return "Match"
    if _has_signal(signals, "qa format"):
        return "FuzzyMatch"
    if _has_signal(signals, "classification format"):
        return "Match"

    # Ethics/moral reasoning → ModelBasedClassify
    has_ethics = _has_signal(signals, "ethics scenario", "moral scenario")
    has_rubric = _has_signal(signals, "rubric", "scoring criteria")
    if has_ethics or has_rubric:
        return "ModelBasedClassify"

    # Open-ended generation → ModelBasedClassify (needs LLM judge)
    if _has_signal(signals, "open-ended generation"):
        return "ModelBasedClassify"
    if any(t in ("generate_until", "generation") for t in types_lower):
        return "ModelBasedClassify"

    return "unknown"


# ── Main scoring function ───────────────────────────────────────────────────

def score_paper(paper: dict) -> dict:
    """Score a single paper on all 9 dimensions for OpenAI Evals.

    Returns dict with:
        filename, dimensions (list of {id, name, weight, raw, weighted}),
        total_score, tier, oai_eval_template, whats_missing, whats_present
    """
    signals = _signals_set(paper)

    dims = []
    total = 0.0
    for dim_def, scorer in zip(DIMENSIONS, _SCORERS):
        raw = scorer(paper, signals)
        weighted = raw * dim_def["weight"]
        total += weighted
        dims.append({
            "id": dim_def["id"],
            "name": dim_def["name"],
            "weight": dim_def["weight"],
            "raw": round(raw, 2),
            "weighted": round(weighted, 2),
        })

    total = round(total, 2)
    tier = classify_tier(total)
    template = map_oai_eval_template(paper)
    missing = _whats_missing(dims)
    present = _whats_present(dims)

    return {
        "filename": paper["filename"],
        "dimensions": dims,
        "total_score": total,
        "tier": tier,
        "oai_eval_template": template,
        "whats_missing": missing,
        "whats_present": present,
    }


# ── What's missing / present ────────────────────────────────────────────────

def _whats_missing(dims: list) -> list:
    """Return list of dimension names that scored 0."""
    return [d["name"] for d in dims if d["raw"] == 0.0]


def _whats_present(dims: list) -> list:
    """Return list of dimension names that scored > 0."""
    return [d["name"] for d in dims if d["raw"] > 0.0]


# ── Markdown formatters ─────────────────────────────────────────────────────

def format_paper_detail(result: dict, paper: dict) -> str:
    """Format a single paper as a detailed markdown section."""
    fn = result["filename"].replace(".md", "")
    lines = [
        f"### {fn}",
        "",
        f"**Score: {result['total_score']}/10.0** | Tier: **{result['tier']}** | "
        f"Template: `{result['oai_eval_template']}`",
        "",
    ]

    # Dimension table
    lines.append("| # | Dimension | Weight | Raw | Weighted |")
    lines.append("|---|-----------|--------|-----|----------|")
    for d in result["dimensions"]:
        raw_icon = "+" if d["raw"] >= 1.0 else ("~" if d["raw"] > 0 else "-")
        lines.append(
            f"| {d['id']} | {d['name']} | {d['weight']} | "
            f"{raw_icon} {d['raw']} | {d['weighted']} |"
        )
    lines.append(f"| | **Total** | **{TOTAL_WEIGHT}** | | **{result['total_score']}** |")
    lines.append("")

    # What's present / missing
    if result["whats_present"]:
        lines.append("**Present:** " + ", ".join(result["whats_present"]))
    if result["whats_missing"]:
        lines.append("**Missing:** " + ", ".join(result["whats_missing"]))
    lines.append("")

    # Data details from paper
    impl = paper.get("impl_details")
    if impl:
        if impl.get("github_urls"):
            lines.append("**GitHub:** " + ", ".join(impl["github_urls"]))
        if impl.get("hf_urls"):
            lines.append("**HF URLs:** " + ", ".join(impl["hf_urls"]))
        if impl.get("metrics"):
            lines.append("**Metrics:** " + ", ".join(impl["metrics"]))
        if impl.get("dataset_size"):
            ds = impl["dataset_size"]
            if isinstance(ds, list):
                ds = ", ".join(str(x) for x in ds)
            lines.append(f"**Dataset size:** {ds}")
        if impl.get("data_format"):
            fmt = impl["data_format"]
            if isinstance(fmt, list):
                fmt = ", ".join(fmt)
            lines.append(f"**Data format:** {fmt}")

    sd = paper.get("survey_data")
    if sd:
        if sd.get("benchmark_name"):
            lines.append(f"**Benchmark:** {sd['benchmark_name']}")
        if sd.get("what_measures"):
            lines.append(f"**Measures:** {sd['what_measures']}")
        if sd.get("availability"):
            lines.append(f"**Availability:** {sd['availability']}")

    lines.append("")

    # Suggested next steps
    steps = suggest_steps(result, paper)
    if steps:
        lines.append("**Next steps:**")
        for step in steps:
            lines.append(f"- {step}")
        lines.append("")

    # Skeleton config for Ready-tier papers
    if result["tier"] == "Ready":
        lines.append("**Skeleton YAML registry config:**")
        lines.append("")
        lines.append("```yaml")
        lines.append(_skeleton_yaml(result, paper))
        lines.append("```")
        lines.append("")

    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def _skeleton_yaml(result: dict, paper: dict) -> str:
    """Generate a skeleton OpenAI Evals YAML registry config."""
    sd = paper.get("survey_data") or {}
    bench = sd.get("benchmark_name", result["filename"].replace(".md", ""))
    task_name = re.sub(r"[^a-z0-9]+", "_", bench.lower()).strip("_")
    template = result["oai_eval_template"]

    impl = paper.get("impl_details") or {}
    data_url = paper.get("meta", {}).get("DATA_URL", "")

    yaml_lines = [
        f"# Eval: {bench}",
        f"# Paper: {result['filename'].replace('.md', '')}",
        f"# Auto-generated skeleton - review and customize before use",
        f"",
        f"{task_name}:",
        f"  id: {task_name}",
        f"  metrics: [accuracy]",
    ]

    if template == "Match":
        yaml_lines.append(f"  description: Exact-match evaluation for {bench}")
        yaml_lines.append(f"  eval_class: evals.elsuite.basic.match:Match")
    elif template == "FuzzyMatch":
        yaml_lines.append(f"  description: Fuzzy-match evaluation for {bench}")
        yaml_lines.append(f"  eval_class: evals.elsuite.basic.fuzzy_match:FuzzyMatch")
    elif template == "Includes":
        yaml_lines.append(f"  description: Includes-check evaluation for {bench}")
        yaml_lines.append(f"  eval_class: evals.elsuite.basic.includes:Includes")
    elif template == "ModelBasedClassify":
        yaml_lines.append(f"  description: Model-graded evaluation for {bench}")
        yaml_lines.append(f"  eval_class: evals.elsuite.modelgraded.classify:ModelBasedClassify")
    else:
        yaml_lines.append(f"  description: Evaluation for {bench}")
        yaml_lines.append(f"  eval_class: evals.elsuite.basic.match:Match")

    yaml_lines.append(f"  # Data: {data_url or 'URL needed'}")
    yaml_lines.append(f"  # JSONL format: {{\"input\": [...], \"ideal\": \"...\"}}")

    return "\n".join(yaml_lines)


def suggest_steps(result: dict, paper: dict) -> list:
    """Generate actionable next steps based on what's missing."""
    steps = []
    missing = set(result["whats_missing"])

    if "JSONL-convertible format" in missing:
        steps.append("Determine data structure and convert to JSONL (input/ideal pairs)")
    if "Eval template mappable" in missing:
        steps.append("Identify task type to select OpenAI Evals template (Match/FuzzyMatch/ModelBasedClassify)")
    if "Data publicly available" in missing:
        steps.append("Locate and verify public download URL for the dataset")
    if "Dataset exists" in missing:
        steps.append("Confirm whether paper introduces a reusable dataset/benchmark")
    if "Code/repo available" in missing:
        steps.append("Find or request code repository with data loading scripts")
    if "Clear eval metrics" in missing:
        steps.append("Identify standard evaluation metrics (accuracy, F1, etc.)")
    if "Full text available" in missing:
        steps.append("Obtain and extract PDF for implementation details")

    if not missing:
        steps.append("Ready for OpenAI Evals implementation - write JSONL data + YAML registry config")

    return steps


def format_paper_summary_line(result: dict) -> str:
    """One-line summary for appendix."""
    fn = result["filename"].replace(".md", "")
    return (
        f"| {fn} | {result['total_score']} | {result['tier']} | "
        f"{result['oai_eval_template']} | {len(result['whats_missing'])} missing |"
    )
