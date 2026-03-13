#!/usr/bin/env python3
"""
scan_openai_evals_implementability.py — Score vault papers on implementability
for the OpenAI Evals framework.

Reads paper frontmatter + PDF extracts, scores each on 9 dimensions measuring
how feasible it is to implement as an OpenAI Evals evaluation (JSONL + YAML
registry), and writes intermediate JSON for report generation.

Usage:
    cd CEI-Lit-WS && ../.venv/bin/python PYTHON/scan_openai_evals_implementability.py
    # Or with range for parallel batches:
    ../.venv/bin/python PYTHON/scan_openai_evals_implementability.py 1 500

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
# Path setup
# ---------------------------------------------------------------------------
_script_dir = Path(__file__).resolve().parent
if str(_script_dir) not in sys.path:
    sys.path.insert(0, str(_script_dir))

from vault_config import PAPERS_DIR, PDF_EXTRACTS_DIR, STATISTICS_DIR, LOGS_DIR
from openai_evals_scoring import (
    score_paper,
    MC_PATTERNS, QA_PATTERNS, CLASSIFICATION_PATTERNS,
    OPEN_GEN_PATTERNS, RUBRIC_PATTERNS, ETHICS_SCENARIO_PATTERNS,
)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SURVEY_JSON = LOGS_DIR / "20260216-benchmark_survey_candidates.json"
OUTPUT_JSON = LOGS_DIR / "20260312-openai-evals-implementability-data.json"

# Regex patterns reused from scan_lm_eval
STANDARD_METRICS = re.compile(
    r"\b(?:accuracy|F1[\s-]?score|F1\b|BLEU|ROUGE|exact.?match|"
    r"perplexity|AUC|precision|recall|MCC|Matthews|BERTScore)\b",
    re.IGNORECASE,
)
DATASET_SIZE_RE = re.compile(
    r"(\d[\d,\.]*)\s*(?:examples|instances|samples|questions|items|prompts|rows|entries|datapoints|data points)",
    re.IGNORECASE,
)
HF_URL_RE = re.compile(r"https?://huggingface\.co/datasets/[\w\-\.]+/[\w\-\.]+", re.IGNORECASE)
GITHUB_URL_RE = re.compile(r"https?://github\.com/[\w\-\.]+/[\w\-\.]+", re.IGNORECASE)
DATA_FORMAT_RE = re.compile(r"\b(?:JSONL|JSON|CSV|TSV|Parquet|HDF5|XML|YAML)\b", re.IGNORECASE)
SPLIT_PATTERNS = re.compile(
    r"\b(?:train(?:ing)?[\s/]+test|test[\s/]+train|train[\s/]+val|"
    r"validation split|dev(?:elopment)? set|test set|train set|"
    r"data split|k-fold)\b",
    re.IGNORECASE,
)

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
        print(f"[WARN] Survey JSON not found: {SURVEY_JSON}")
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
# 4. Extract implementation details from PDF
# =========================================================================
def extract_impl_details_from_pdf(meta):
    """Mine the PDF extract for implementation hints."""
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
        return None  # Distinguish "no extract" from "extract but no details"

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

    # Rubric detection (important for ModelBasedClassify)
    if RUBRIC_PATTERNS.search(pdf_text):
        details["has_rubric"] = True

    # Ethics scenario detection
    if ETHICS_SCENARIO_PATTERNS.search(pdf_text):
        details["has_ethics_scenarios"] = True

    return details


# =========================================================================
# 5. Build signals list for scoring
# =========================================================================
def build_signals(meta, survey_entry, impl_details):
    """Build a signals list from metadata, survey, and impl_details."""
    signals = []
    abstract = meta.get("abstract", "")
    how_measures = (survey_entry or {}).get("how_measures", "")
    what_measures = (survey_entry or {}).get("what_measures", "")
    search_text = f"{abstract} {how_measures} {what_measures}"

    # Frontmatter flags
    if meta.get("is_benchmark", "").strip().lower() == "yes":
        signals.append("is_benchmark")
    if meta.get("is_eval", "").strip().lower() == "yes":
        signals.append("is_eval")
    if meta.get("is_dataset", "").strip().lower() == "yes":
        signals.append("is_dataset")

    # DATA_URL
    data_url = meta.get("DATA_URL", "").strip()
    if data_url and data_url.lower() not in ("", "n/a", "na", "none", "not available"):
        signals.append("Has DATA_URL")
        if "huggingface.co/datasets" in data_url.lower():
            signals.append("HuggingFace dataset URL")
        if "github.com/" in data_url.lower():
            signals.append("Code available")

    # Availability
    availability = (survey_entry or {}).get("availability", "")
    avail_lower = availability.lower()
    if "public" in avail_lower:
        signals.append("Availability = Public")
    if "code" in avail_lower:
        signals.append("Code available")

    # LLM assessed
    llm_assessed = meta.get("LLM_assessed", "").strip()
    if llm_assessed and llm_assessed.lower() not in ("", "n/a", "na", "none"):
        signals.append("LLM_assessed")

    # data_metrics
    data_metrics = meta.get("data_metrics", "").strip()
    if data_metrics and data_metrics.lower() not in ("", "n/a", "na", "none", "not specified"):
        signals.append("Has data_metrics")

    # Standard metrics in abstract
    if STANDARD_METRICS.search(abstract):
        signals.append("Standard metrics in abstract")

    # Task format detection from search text
    if MC_PATTERNS.search(search_text):
        signals.append("Multiple-choice format")
    if QA_PATTERNS.search(search_text):
        signals.append("QA format")
    if CLASSIFICATION_PATTERNS.search(search_text):
        signals.append("Classification format")
    if OPEN_GEN_PATTERNS.search(search_text):
        signals.append("Open-ended generation")

    # Ethics/rubric detection from search text + impl_details
    if ETHICS_SCENARIO_PATTERNS.search(search_text):
        signals.append("Ethics scenario")
    if RUBRIC_PATTERNS.search(search_text):
        signals.append("Rubric")

    if impl_details:
        if impl_details.get("has_rubric"):
            if "Rubric" not in signals:
                signals.append("Rubric")
        if impl_details.get("has_ethics_scenarios"):
            if "Ethics scenario" not in signals:
                signals.append("Ethics scenario")
        if impl_details.get("dataset_size"):
            signals.append("Dataset size")
        if impl_details.get("github_urls"):
            if "Code available" not in signals:
                signals.append("Code available")

    # Dataset size from survey
    dataset_size = (survey_entry or {}).get("dataset_size", "")
    if dataset_size and dataset_size.lower() not in (
        "", "n/a", "na", "none", "not stated", "not explicitly stated",
        "not specified", "unknown",
    ):
        if "Dataset size" not in signals:
            signals.append("Dataset size")

    # Splits from search text
    if SPLIT_PATTERNS.search(search_text):
        signals.append("Splits mentioned")

    return signals


# =========================================================================
# 6. Main
# =========================================================================
def main():
    # Parse optional START END range args
    start_idx = 0
    end_idx = None
    if len(sys.argv) >= 3:
        start_idx = int(sys.argv[1]) - 1  # 1-based to 0-based
        end_idx = int(sys.argv[2])

    print("=" * 60)
    print("OpenAI Evals Implementability Scanner")
    print("=" * 60)
    print()

    # 1. Load survey
    print("Loading benchmark survey...")
    survey = load_benchmark_survey()
    print(f"  Survey entries (decision=Yes): {len(survey)}")
    print()

    # 2. Get all paper files
    paper_files = sorted(PAPERS_DIR.glob("*.md"))
    paper_files = [f for f in paper_files if f.name not in ("README.md", "TEMPLATE.md")]
    total = len(paper_files)

    # Apply range
    if end_idx is not None:
        paper_files = paper_files[start_idx:end_idx]
        print(f"Processing range {start_idx+1}-{end_idx} of {total} papers ({len(paper_files)} papers)")
    else:
        print(f"Processing all {total} papers")
    print()

    # 3. Score each paper
    results = []
    for i, filepath in enumerate(paper_files, 1):
        if i % 200 == 0:
            print(f"  ... processed {i}/{len(paper_files)} papers")

        meta, content = parse_frontmatter(filepath)
        filename = filepath.name
        survey_entry = survey.get(filename)

        # Extract impl details from PDF
        impl_details = extract_impl_details_from_pdf(meta)

        # Build signals
        signals = build_signals(meta, survey_entry, impl_details)

        # Build paper dict for scoring module
        paper_data = {
            "filename": filename,
            "signals": signals,
            "survey_data": survey_entry,
            "impl_details": impl_details if impl_details else {},
            "meta": meta,
        }

        # Score
        result = score_paper(paper_data)

        # Enrich result with extra context for report generation
        result["signals"] = signals
        result["survey_data"] = survey_entry
        result["impl_details"] = impl_details if impl_details else {}
        result["year"] = meta.get("year", "")
        result["data_url"] = meta.get("DATA_URL", "")
        result["is_benchmark"] = meta.get("is_benchmark", "").strip().lower() == "yes"
        result["is_eval"] = meta.get("is_eval", "").strip().lower() == "yes"
        result["is_dataset"] = meta.get("is_dataset", "").strip().lower() == "yes"

        results.append(result)

    # 4. Sort by score descending
    results.sort(key=lambda x: (-x["total_score"], x["filename"]))

    # 5. Summary
    from collections import Counter
    tier_counts = Counter(r["tier"] for r in results)
    template_counts = Counter(r["oai_eval_template"] for r in results)

    print()
    print(f"Scored {len(results)} papers.")
    print()
    print("Tier Summary:")
    for tier in ("Ready", "Possible", "Barriers", "Not Implementable"):
        print(f"  {tier}: {tier_counts.get(tier, 0)}")
    print()
    print("Template Distribution:")
    for template, count in template_counts.most_common():
        print(f"  {template}: {count}")
    print()

    # 6. Write JSON (PID-scoped temp file for safety)
    output = {
        "generated": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "total": len(results),
        "tier_counts": dict(tier_counts),
        "template_counts": dict(template_counts),
        "results": results,
    }

    tmp_path = OUTPUT_JSON.with_suffix(f".tmp.{os.getpid()}.json")
    tmp_path.write_text(json.dumps(output, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    os.replace(str(tmp_path), str(OUTPUT_JSON))
    print(f"JSON written: {OUTPUT_JSON}")
    print("Done.")


if __name__ == "__main__":
    main()
