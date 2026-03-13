#!/usr/bin/env python3
"""
lighteval_scoring.py — Shared scoring module for lighteval implementability.

Scores vault papers on 9 dimensions (0-10 scale) measuring how feasible
each paper's benchmark/dataset is to implement as a lighteval task.

lighteval is HuggingFace-native: tasks use datasets.load_dataset(), so
HF dataset presence is the strongest signal (weight 2.0).

Used by: score_lighteval_batch.py, assemble_lighteval_report.py,
         generate_lighteval_paper_reports.py
"""

import re

# ── Dimension definitions ────────────────────────────────────────────────────

DIMENSIONS = [
    {"id": "D1", "name": "Dataset exists",         "weight": 1.5, "max": 1.0},
    {"id": "D2", "name": "Data publicly available", "weight": 1.5, "max": 1.0},
    {"id": "D3", "name": "HuggingFace presence",   "weight": 2.0, "max": 1.0},
    {"id": "D4", "name": "Code/repo available",    "weight": 1.0, "max": 1.0},
    {"id": "D5", "name": "Clear eval metrics",     "weight": 1.0, "max": 1.0},
    {"id": "D6", "name": "Quantified data size",   "weight": 0.5, "max": 1.0},
    {"id": "D7", "name": "LLM evaluation exists",  "weight": 0.5, "max": 1.0},
    {"id": "D8", "name": "Task type identifiable",  "weight": 1.0, "max": 1.0},
    {"id": "D9", "name": "Full text available",    "weight": 1.0, "max": 1.0},
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


# ── Dimension scorers ────────────────────────────────────────────────────────

def _score_d1(paper: dict, signals: set) -> float:
    """D1: Dataset exists (is_benchmark/is_dataset or benchmark/dataset signals)."""
    if _has_signal(signals, "is_benchmark"):
        return 1.0
    if _has_signal(signals, "is_dataset"):
        return 1.0
    if _has_signal(signals, "benchmark", "dataset"):
        return 0.5
    # survey_data with a benchmark_name also counts
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
        if (sd.get("availability") or "").lower() == "public":
            has_public = True

    if has_url and has_public:
        return 1.0
    if has_url or has_public:
        return 0.5
    return 0.0


def _score_d3(paper: dict, signals: set) -> float:
    """D3: HuggingFace presence — the #1 factor for lighteval."""
    # Direct HF dataset URL in signals
    if _has_signal(signals, "huggingface dataset url"):
        return 1.0

    impl = paper.get("impl_details")
    if impl:
        # HF URLs in impl_details
        hf_urls = impl.get("hf_urls", [])
        if hf_urls and any(hf_urls):
            return 1.0
        # HuggingFace in data_format
        fmt = impl.get("data_format", [])
        if isinstance(fmt, list) and any("huggingface" in str(f).lower() for f in fmt):
            return 1.0

    # HF org page (weaker signal)
    sd = paper.get("survey_data")
    if sd:
        bm = sd.get("benchmark_name", "")
        if bm and "huggingface" in bm.lower():
            return 0.5

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
    if sd and (sd.get("availability") or "").lower() == "code available":
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
    """D8: Task type identifiable — maps to lighteval task types."""
    # Check impl_details.task_type first
    impl = paper.get("impl_details")
    if impl:
        tt = impl.get("task_type")
        if tt:
            types = tt if isinstance(tt, list) else [tt]
            types_lower = [t.lower() for t in types if t]
            if any(t in ("multiple_choice", "multichoice") for t in types_lower):
                return 1.0
            if "qa" in types_lower:
                return 1.0
            if "classification" in types_lower:
                return 0.75
            if any(t in ("generate_until", "generation", "loglikelihood") for t in types_lower):
                return 0.5

    # Fall back to signal detection
    if _has_signal(signals, "multiple-choice", "mcq"):
        return 1.0
    if _has_signal(signals, "qa format"):
        return 1.0
    if _has_signal(signals, "classification format"):
        return 0.75
    if _has_signal(signals, "open-ended generation"):
        return 0.5
    return 0.0


def _score_d9(paper: dict, signals: set) -> float:
    """D9: Full text available (impl_details extracted from PDF)."""
    if paper.get("impl_details") is not None:
        return 1.0
    return 0.0


_SCORERS = [_score_d1, _score_d2, _score_d3, _score_d4, _score_d5,
            _score_d6, _score_d7, _score_d8, _score_d9]


# ── Main scoring function ───────────────────────────────────────────────────

def score_paper(paper: dict) -> dict:
    """Score a single paper on all 9 dimensions.

    Returns dict with:
        filename, dimensions (list of {id, name, weight, raw, weighted}),
        total_score, tier, lighteval_task_type, whats_missing, whats_present
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
    task_type = _map_lighteval_task_type(paper)
    missing = _whats_missing(dims)
    present = _whats_present(dims)

    return {
        "filename": paper["filename"],
        "dimensions": dims,
        "total_score": total,
        "tier": tier,
        "lighteval_task_type": task_type,
        "whats_missing": missing,
        "whats_present": present,
        "lm_eval_score": paper.get("score", 0),
        "lm_eval_tier": paper.get("tier", ""),
    }


# ── lighteval task type mapping ──────────────────────────────────────────────

def _map_lighteval_task_type(paper: dict) -> str:
    """Map paper to the most appropriate lighteval task type."""
    impl = paper.get("impl_details")
    if impl:
        tt = impl.get("task_type")
        if tt:
            types = tt if isinstance(tt, list) else [tt]
            types_lower = [t.lower() for t in types if t]
            if any(t in ("multiple_choice", "multichoice") for t in types_lower):
                return "multichoice"
            if "qa" in types_lower:
                return "generate_until"
            if "loglikelihood" in types_lower:
                return "loglikelihood"
            if any(t in ("classification", "generate_until", "generation") for t in types_lower):
                return "generate_until"

    signals = _signals_set(paper)
    if _has_signal(signals, "multiple-choice"):
        return "multichoice"
    if _has_signal(signals, "qa format"):
        return "generate_until"
    if _has_signal(signals, "classification"):
        return "generate_until"
    return "unknown"


# ── What's missing / present ─────────────────────────────────────────────────

def _whats_missing(dims: list) -> list:
    """Return list of dimension names that scored 0."""
    return [d["name"] for d in dims if d["raw"] == 0.0]


def _whats_present(dims: list) -> list:
    """Return list of dimension names that scored > 0."""
    return [d["name"] for d in dims if d["raw"] > 0.0]


# ── Markdown formatter ───────────────────────────────────────────────────────

def format_paper_detail(result: dict, paper: dict) -> str:
    """Format a single paper as a detailed markdown section."""
    fn = result["filename"].replace(".md", "")
    lines = [
        f"### {fn}",
        "",
        f"**Score: {result['total_score']}/10.0** | Tier: **{result['tier']}** | "
        f"lighteval type: `{result['lighteval_task_type']}`",
        "",
    ]

    # Dimension table
    lines.append("| # | Dimension | Weight | Raw | Weighted |")
    lines.append("|---|-----------|--------|-----|----------|")
    for d in result["dimensions"]:
        raw_icon = "✓" if d["raw"] >= 1.0 else ("◐" if d["raw"] > 0 else "✗")
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
        if impl.get("hf_urls"):
            lines.append("**HF URLs:** " + ", ".join(impl["hf_urls"]))
        if impl.get("github_urls"):
            lines.append("**GitHub:** " + ", ".join(impl["github_urls"]))
        if impl.get("metrics"):
            lines.append("**Metrics:** " + ", ".join(impl["metrics"]))
        if impl.get("dataset_size"):
            ds = impl["dataset_size"]
            if isinstance(ds, list):
                ds = ", ".join(str(x) for x in ds)
            lines.append(f"**Dataset size:** {ds}")
        if impl.get("splits"):
            lines.append("**Splits:** " + ", ".join(impl["splits"]))

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
    steps = _suggest_steps(result, paper)
    if steps:
        lines.append("**Next steps:**")
        for step in steps:
            lines.append(f"- {step}")
        lines.append("")

    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def _suggest_steps(result: dict, paper: dict) -> list:
    """Generate actionable next steps based on what's missing."""
    steps = []
    missing = set(result["whats_missing"])

    if "HuggingFace presence" in missing:
        steps.append("Upload dataset to HuggingFace Hub for `datasets.load_dataset()` access")
    if "Data publicly available" in missing:
        steps.append("Locate and verify public download URL for the dataset")
    if "Dataset exists" in missing:
        steps.append("Confirm whether paper introduces a reusable dataset/benchmark")
    if "Code/repo available" in missing:
        steps.append("Find or request code repository with data loading scripts")
    if "Clear eval metrics" in missing:
        steps.append("Identify standard evaluation metrics (accuracy, F1, etc.)")
    if "Task type identifiable" in missing:
        steps.append("Determine lighteval task type (multichoice, generate_until, loglikelihood)")
    if "Full text available" in missing:
        steps.append("Obtain and extract PDF for implementation details")

    if not missing:
        steps.append("Ready for lighteval task implementation — write prompt_function + LightevalTaskConfig")

    return steps


def format_paper_summary_line(result: dict) -> str:
    """One-line summary for appendix."""
    fn = result["filename"].replace(".md", "")
    return (
        f"| {fn} | {result['total_score']} | {result['tier']} | "
        f"{result['lighteval_task_type']} | {len(result['whats_missing'])} missing |"
    )
