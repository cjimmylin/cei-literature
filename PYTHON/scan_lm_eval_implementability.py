#!/usr/bin/env python3
"""
scan_lm_eval_implementability.py — Score vault papers on implementability
for EleutherAI's lm-evaluation-harness.

Reads the benchmark survey JSON and paper frontmatter, scores each benchmark
paper on how feasible it is to add as an lm-eval-harness task, and generates
a tiered report with implementation sketches for top candidates.

Usage:
    cd CEI-Lit-WS && ../.venv/bin/python PYTHON/scan_lm_eval_implementability.py

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

# Try to import known harness tasks; fall back to empty dict if not yet created
try:
    from lm_eval_known_tasks import KNOWN_TASKS  # dict: task_name -> {dataset, type, ...}
except ImportError:
    print("[WARN] lm_eval_known_tasks module not found — harness matching disabled")
    KNOWN_TASKS = {}

# ---------------------------------------------------------------------------
# Survey JSON path
# ---------------------------------------------------------------------------
SURVEY_JSON = LOGS_DIR / "20260216-benchmark_survey_candidates.json"

# Output paths
REPORT_PATH = STATISTICS_DIR / "20260312-lm-eval-implementability-report.md"
OUTPUT_JSON = LOGS_DIR / "20260312-lm-eval-implementability-data.json"

# ---------------------------------------------------------------------------
# Constants
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

TASK_TYPE_MAP = {
    "multiple_choice": MC_PATTERNS,
    "generate_until": OPEN_GEN_PATTERNS,
    "loglikelihood": re.compile(r"loglikelihood|perplexity|log.?prob", re.IGNORECASE),
    "classification": CLASSIFICATION_PATTERNS,
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
# 2. Parse frontmatter (safe line parser — NO PyYAML)
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
# 3. Get PDF extract content
# =========================================================================
def get_pdf_content(year, author_last, title_short):
    """Find and return PDF extract text, searching within the year subdir."""
    year_str = str(year)
    year_dir = PDF_EXTRACTS_DIR / year_str
    if not year_dir.is_dir():
        # Fallback: try top-level glob
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
# 4. Match to harness known tasks
# =========================================================================
def match_to_harness(meta, survey_entry):
    """
    Fuzzy-match benchmark_name and DATA_URL against KNOWN_TASKS.
    Returns (task_name, task_info) or (None, None).
    """
    if not KNOWN_TASKS:
        return None, None

    bench_name = (survey_entry or {}).get("benchmark_name", "").lower().strip()
    data_url = meta.get("DATA_URL", "").lower().strip()

    for task_name, task_info in KNOWN_TASKS.items():
        task_lower = task_name.lower()
        # Direct name match
        if bench_name and (
            bench_name == task_lower
            or bench_name.replace(" ", "_") == task_lower
            or bench_name.replace("-", "_") == task_lower
            or task_lower in bench_name
            or bench_name in task_lower
        ):
            return task_name, task_info
        # Dataset URL match
        task_dataset = task_info.get("dataset", "").lower()
        if data_url and task_dataset and (
            task_dataset in data_url or data_url in task_dataset
        ):
            return task_name, task_info

    return None, None


# =========================================================================
# 5. Score implementability (0-100, additive)
# =========================================================================
def score_implementability(meta, survey_entry):
    """Score a paper 0-100 on how feasible it is to implement in lm-eval-harness."""
    score = 0
    signals = []

    data_url = meta.get("DATA_URL", "").strip()
    abstract = meta.get("abstract", "")
    how_measures = (survey_entry or {}).get("how_measures", "")
    what_measures = (survey_entry or {}).get("what_measures", "")
    availability = (survey_entry or {}).get("availability", "")
    dataset_size = (survey_entry or {}).get("dataset_size", "")
    search_text = f"{abstract} {how_measures} {what_measures}"

    # HuggingFace dataset URL (+25)
    if data_url and "huggingface.co/datasets" in data_url.lower():
        score += 25
        signals.append("HF dataset URL")

    # Any DATA_URL (+15)
    if data_url and data_url.lower() not in ("", "n/a", "na", "none", "not available"):
        score += 15
        signals.append("Has DATA_URL")

    # Availability: Public (+15) or Code available (+8)
    avail_lower = availability.lower()
    if "public" in avail_lower:
        score += 15
        signals.append("Public data")
    elif "code" in avail_lower:
        score += 8
        signals.append("Code available")

    # Task format detection (take highest matching)
    format_scored = False
    if MC_PATTERNS.search(search_text):
        score += 15
        signals.append("MC format")
        format_scored = True
    elif QA_PATTERNS.search(search_text):
        score += 12
        signals.append("QA format")
        format_scored = True
    elif CLASSIFICATION_PATTERNS.search(search_text):
        score += 10
        signals.append("Classification format")
        format_scored = True
    if not format_scored and OPEN_GEN_PATTERNS.search(search_text):
        score += 5
        signals.append("Open-ended generation")

    # Dataset size stated (+10)
    if dataset_size and dataset_size.lower() not in (
        "", "n/a", "na", "none", "not stated", "not explicitly stated",
        "not specified", "unknown",
    ):
        score += 10
        signals.append("Size stated")

    # LLM_assessed populated (+10)
    llm_assessed = meta.get("LLM_assessed", "").strip()
    if llm_assessed and llm_assessed.lower() not in ("", "n/a", "na", "none"):
        score += 10
        signals.append("LLM assessed")

    # data_metrics populated (+5)
    data_metrics = meta.get("data_metrics", "").strip()
    if data_metrics and data_metrics.lower() not in (
        "", "n/a", "na", "none", "not specified",
    ):
        score += 5
        signals.append("Has metrics field")

    # Standard metrics mentioned (+5)
    if STANDARD_METRICS.search(abstract):
        score += 5
        signals.append("Standard metrics")

    # Data splits mentioned (+10)
    if SPLIT_PATTERNS.search(search_text):
        score += 10
        signals.append("Splits mentioned")

    # is_benchmark = Yes (+5)
    if meta.get("is_benchmark", "").strip().lower() == "yes":
        score += 5
        signals.append("is_benchmark")

    return min(score, 100), signals


# =========================================================================
# 6. Extract implementation details from PDF
# =========================================================================
def extract_impl_details_from_pdf(meta):
    """For high-scoring papers, mine the PDF extract for implementation hints."""
    year = meta.get("year", "")
    authors = meta.get("authors", meta.get("author", ""))
    title = meta.get("title", "")

    # Derive author_last and title_short for lookup
    author_last = ""
    if authors:
        # Take first author's last name
        first_author = authors.split(";")[0].strip()
        parts = first_author.split(",")
        author_last = parts[0].strip().split()[-1] if parts else ""

    title_short = title[:15] if title else ""

    pdf_text = get_pdf_content(year, author_last, title_short)
    if not pdf_text:
        return {}

    details = {}

    # Task type
    for ttype, pattern in TASK_TYPE_MAP.items():
        if pattern.search(pdf_text):
            details.setdefault("task_type", []).append(ttype)

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

    return details


# =========================================================================
# 7. Classify tier
# =========================================================================
def classify_tier(score, in_harness, has_hf_data):
    """Assign a tier label based on score and data availability."""
    if in_harness:
        return "ALREADY_IN_HARNESS"
    if score >= 65 and (has_hf_data or score >= 75):
        return "READY_TO_IMPLEMENT"
    if score >= 45:
        return "NEEDS_DATASET_HOSTING"
    if score >= 30:
        return "NEEDS_MORE_INFO"
    return "NOT_IMPLEMENTABLE"


# =========================================================================
# 8. Generate implementation sketch
# =========================================================================
def generate_impl_sketch(paper_info):
    """Generate a suggested lm-eval YAML config sketch for a paper."""
    meta = paper_info["meta"]
    survey = paper_info.get("survey", {}) or {}
    details = paper_info.get("impl_details", {})
    bench = survey.get("benchmark_name", meta.get("title", "unknown"))

    # Derive task name
    task_name = re.sub(r"[^a-z0-9]+", "_", bench.lower()).strip("_")

    # Best guess at task type
    task_types = details.get("task_type", [])
    if "multiple_choice" in task_types:
        output_type = "multiple_choice"
    elif "generate_until" in task_types:
        output_type = "generate_until"
    elif "classification" in task_types:
        output_type = "multiple_choice"  # classification often maps to MC
    else:
        output_type = "generate_until"

    # Dataset path
    hf_urls = details.get("hf_urls", [])
    data_url = meta.get("DATA_URL", "")
    if hf_urls:
        dataset_path = hf_urls[0].replace("https://huggingface.co/datasets/", "")
    elif "huggingface.co/datasets" in data_url:
        dataset_path = data_url.split("huggingface.co/datasets/")[-1].split("?")[0]
    else:
        dataset_path = f"<NEEDS_HOSTING: {data_url or 'no URL'}>"

    # Metrics
    metrics = details.get("metrics", [])
    if not metrics:
        if output_type == "multiple_choice":
            metrics = ["acc", "acc_norm"]
        else:
            metrics = ["exact_match"]

    sketch = f"""# Task: {bench}
# Paper: {meta.get('title', 'N/A')}
# Auto-generated sketch — review and customize before use

task: {task_name}
dataset_path: {dataset_path}
output_type: {output_type}
test_split: test
metric_list:
{chr(10).join(f'  - metric: {m}' for m in metrics)}
# Prompt template notes:
#   what_measures: {survey.get('what_measures', 'N/A')[:100]}
#   how_measures: {survey.get('how_measures', 'N/A')[:100]}"""

    if details.get("prompt_hints"):
        sketch += f"\n#   prompt_hint: {details['prompt_hints'][0][:80]}"

    return sketch


# =========================================================================
# 9. Generate markdown report
# =========================================================================
def generate_report(results):
    """Write the tiered markdown report."""
    tiers = {
        "ALREADY_IN_HARNESS": [],
        "READY_TO_IMPLEMENT": [],
        "NEEDS_DATASET_HOSTING": [],
        "NEEDS_MORE_INFO": [],
        "NOT_IMPLEMENTABLE": [],
    }
    for r in results:
        tiers[r["tier"]].append(r)

    lines = []
    lines.append("# lm-eval-harness Implementability Report")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")

    # Executive Summary
    lines.append("## Executive Summary")
    lines.append("")
    lines.append("| Tier | Count |")
    lines.append("|------|-------|")
    tier_labels = {
        "ALREADY_IN_HARNESS": "Already in Harness",
        "READY_TO_IMPLEMENT": "Ready to Implement",
        "NEEDS_DATASET_HOSTING": "Needs Dataset Hosting",
        "NEEDS_MORE_INFO": "Needs More Info",
        "NOT_IMPLEMENTABLE": "Not Implementable",
    }
    total_scored = sum(len(v) for v in tiers.values())
    for tier_key, label in tier_labels.items():
        lines.append(f"| {label} | {len(tiers[tier_key])} |")
    lines.append(f"| **Total scored** | **{total_scored}** |")
    lines.append("")

    # Section 1: Already in harness
    lines.append("## 1. Already in lm-eval-harness")
    lines.append("")
    if tiers["ALREADY_IN_HARNESS"]:
        lines.append("| Paper | Harness Task | Type | HF Dataset |")
        lines.append("|-------|-------------|------|------------|")
        for r in tiers["ALREADY_IN_HARNESS"]:
            harness_task = r.get("harness_task", "?")
            harness_info = r.get("harness_info", {}) or {}
            htype = harness_info.get("type", "?")
            hds = harness_info.get("dataset", "?")
            lines.append(f"| {r['filename']} | {harness_task} | {htype} | {hds} |")
    else:
        lines.append("No papers matched known harness tasks.")
    lines.append("")

    # Section 2: Ready to Implement
    ready = sorted(tiers["READY_TO_IMPLEMENT"], key=lambda x: x["score"], reverse=True)
    lines.append("## 2. Ready to Implement (score >= 65)")
    lines.append("")
    if ready:
        lines.append("| Paper | Benchmark | Score | Type | Data URL | Key Signals |")
        lines.append("|-------|-----------|-------|------|----------|-------------|")
        for r in ready:
            bench = (r.get("survey", {}) or {}).get("benchmark_name", "—")
            data_url = r["meta"].get("DATA_URL", "—")
            sigs = ", ".join(r.get("signals", []))
            task_types = ", ".join(r.get("impl_details", {}).get("task_type", ["?"]))
            lines.append(
                f"| {r['filename']} | {bench} | {r['score']} | "
                f"{task_types} | {data_url} | {sigs} |"
            )
        lines.append("")

        # Implementation sketches for top 10
        lines.append("### Implementation Sketches")
        lines.append("")
        for r in ready[:10]:
            sketch = generate_impl_sketch(r)
            lines.append(f"#### {r['filename']}")
            lines.append("")
            lines.append("```yaml")
            lines.append(sketch)
            lines.append("```")
            lines.append("")
    else:
        lines.append("No papers in this tier.")
    lines.append("")

    # Section 3: Needs Dataset Hosting
    hosting = sorted(tiers["NEEDS_DATASET_HOSTING"], key=lambda x: x["score"], reverse=True)
    lines.append("## 3. Needs Dataset Hosting (score 45-64, no HF)")
    lines.append("")
    if hosting:
        lines.append("| Paper | Benchmark | Score | Data URL | What's Missing |")
        lines.append("|-------|-----------|-------|----------|----------------|")
        for r in hosting:
            bench = (r.get("survey", {}) or {}).get("benchmark_name", "—")
            data_url = r["meta"].get("DATA_URL", "—")
            missing = []
            if "HF dataset URL" not in r.get("signals", []):
                missing.append("No HF dataset")
            if "Splits mentioned" not in r.get("signals", []):
                missing.append("No splits info")
            lines.append(
                f"| {r['filename']} | {bench} | {r['score']} | "
                f"{data_url} | {'; '.join(missing) or '—'} |"
            )
    else:
        lines.append("No papers in this tier.")
    lines.append("")

    # Section 4: Needs More Info
    more_info = sorted(tiers["NEEDS_MORE_INFO"], key=lambda x: x["score"], reverse=True)
    lines.append("## 4. Needs More Info (score 30-44)")
    lines.append("")
    if more_info:
        lines.append("| Paper | Score | Missing Items |")
        lines.append("|-------|-------|---------------|")
        for r in more_info:
            present = set(r.get("signals", []))
            missing = []
            if "Has DATA_URL" not in present:
                missing.append("No data URL")
            if "Public data" not in present and "Code available" not in present:
                missing.append("Availability unclear")
            if not any(s in present for s in ("MC format", "QA format", "Classification format", "Open-ended generation")):
                missing.append("Format unknown")
            if "Size stated" not in present:
                missing.append("Size unknown")
            lines.append(
                f"| {r['filename']} | {r['score']} | {'; '.join(missing) or '—'} |"
            )
    else:
        lines.append("No papers in this tier.")
    lines.append("")

    # Section 5: Not Implementable
    not_impl = tiers["NOT_IMPLEMENTABLE"]
    lines.append("## 5. Not Implementable (score < 30)")
    lines.append("")
    lines.append(f"{len(not_impl)} papers in this tier (summary only).")
    lines.append("")

    report_text = "\n".join(lines)
    REPORT_PATH.write_text(report_text, encoding="utf-8")
    print(f"Report written: {REPORT_PATH}")


# =========================================================================
# 10. Save JSON
# =========================================================================
def save_json(results):
    """Write structured JSON output."""
    # Strip non-serializable bits and write
    out = []
    for r in results:
        entry = {
            "filename": r["filename"],
            "score": r["score"],
            "tier": r["tier"],
            "signals": r.get("signals", []),
            "harness_task": r.get("harness_task"),
            "benchmark_name": (r.get("survey") or {}).get("benchmark_name"),
            "data_url": r["meta"].get("DATA_URL", ""),
            "availability": (r.get("survey") or {}).get("availability", ""),
            "impl_details": r.get("impl_details", {}),
            "year": r["meta"].get("year", ""),
        }
        out.append(entry)
    OUTPUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"JSON written: {OUTPUT_JSON}")


# =========================================================================
# Main
# =========================================================================
def main():
    print("=" * 60)
    print("lm-eval-harness Implementability Scanner")
    print("=" * 60)
    print()

    # 1. Load survey
    print("Loading benchmark survey...")
    survey = load_benchmark_survey()
    print(f"  Survey entries (decision=Yes): {len(survey)}")

    # 2. Known harness tasks
    print(f"  Known harness tasks: {len(KNOWN_TASKS)}")
    print()

    # 3. Scan all papers
    paper_files = sorted(PAPERS_DIR.glob("*.md"))
    paper_files = [f for f in paper_files if f.name not in ("README.md", "TEMPLATE.md")]
    print(f"Scanning {len(paper_files)} papers...")
    print()

    results = []
    scored_count = 0

    for i, filepath in enumerate(paper_files, 1):
        if i % 200 == 0:
            print(f"  ... processed {i}/{len(paper_files)} papers")

        meta, content = parse_frontmatter(filepath)
        filename = filepath.name
        survey_entry = survey.get(filename)

        # Match to harness
        harness_task, harness_info = match_to_harness(meta, survey_entry)
        in_harness = harness_task is not None

        # Score
        score, signals = score_implementability(meta, survey_entry)
        scored_count += 1

        # Determine if paper has HF data
        data_url = meta.get("DATA_URL", "")
        has_hf_data = "huggingface.co/datasets" in data_url.lower() if data_url else False

        # Classify tier
        tier = classify_tier(score, in_harness, has_hf_data)

        result = {
            "filename": filename,
            "meta": meta,
            "survey": survey_entry,
            "score": score,
            "signals": signals,
            "tier": tier,
            "harness_task": harness_task,
            "harness_info": harness_info,
            "impl_details": {},
        }
        results.append(result)

    print(f"Scored {scored_count} papers.")
    print()

    # 5. Extract impl details for top candidates (score >= 45)
    high_scorers = [r for r in results if r["score"] >= 45]
    print(f"Extracting implementation details for {len(high_scorers)} papers (score >= 45)...")
    for r in high_scorers:
        r["impl_details"] = extract_impl_details_from_pdf(r["meta"])

    # 6. Sort by score descending
    results.sort(key=lambda x: x["score"], reverse=True)

    # Summary
    tier_counts = {}
    for r in results:
        tier_counts[r["tier"]] = tier_counts.get(r["tier"], 0) + 1
    print()
    print("Tier Summary:")
    for tier_name in (
        "ALREADY_IN_HARNESS", "READY_TO_IMPLEMENT",
        "NEEDS_DATASET_HOSTING", "NEEDS_MORE_INFO", "NOT_IMPLEMENTABLE",
    ):
        print(f"  {tier_name}: {tier_counts.get(tier_name, 0)}")
    print()

    # 7. Generate report and JSON
    generate_report(results)
    save_json(results)

    print()
    print("Done.")


if __name__ == "__main__":
    main()
