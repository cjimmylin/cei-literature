#!/usr/bin/env python3
"""Score M-Z papers on implementability for lm-eval-harness.

Agent 9 — Metadata Scorer for papers whose author last name starts M-Z.
"""

import functools
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

print = functools.partial(print, flush=True)

PAPERS_DIR = Path("papers")
SURVEY_PATH = Path("logs/20260216-benchmark_survey_candidates.json")
OUTPUT_PATH = Path("logs/20260312-scores-m-z.json")

SKIP_FILES = {"README.md", "TEMPLATE.md"}


def parse_frontmatter(text: str) -> dict:
    """Simple line-based YAML frontmatter parser (no PyYAML)."""
    fm = {}
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return fm
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = re.match(r'^([A-Za-z_][A-Za-z0-9_ -]*?):\s*(.*)', line)
        if m:
            key = m.group(1).strip()
            val = m.group(2).strip().strip('"').strip("'")
            fm[key] = val
    return fm


def extract_author(filename: str):
    """Extract author last name from YYYY-Author-Title.md pattern."""
    m = re.match(r'^\d{4}-([A-Za-z]+)-', filename)
    if m:
        return m.group(1)
    return None


def is_m_z(filename: str) -> bool:
    """Check if author name starts with M-Z."""
    if filename.startswith("0000-"):
        return False
    author = extract_author(filename)
    if not author:
        return False
    return author[0].upper() >= 'M'


def score_paper(fm, survey_entry):
    """Score a paper 0-100 on implementability. Returns (score, signals)."""
    score = 0
    signals = []

    # DATA_URL checks
    data_url = fm.get("DATA_URL", "").strip()
    if data_url and data_url.lower() not in ("n/a", "na", ""):
        if "huggingface" in data_url.lower():
            score += 25
            signals.append("HuggingFace dataset URL (+25)")
        score += 15
        signals.append("Any DATA_URL present (+15)")

    # Survey availability
    availability = ""
    if survey_entry:
        availability = survey_entry.get("availability", "")
    if "Public" in availability:
        score += 15
        signals.append(f"Survey availability = Public (+15)")
    elif "Code available" in availability:
        score += 8
        signals.append(f"Survey availability = Code available (+8)")

    # Format detection from survey and abstract
    abstract = fm.get("abstract", "").lower()
    data_desc = fm.get("data_description", "").lower()
    survey_how = ""
    if survey_entry:
        survey_how = survey_entry.get("how_measures", "").lower()
    combined_text = f"{abstract} {data_desc} {survey_how}"

    mc_patterns = ["multiple.choice", "mcq", "multi-choice", "multiple choice"]
    if any(p in combined_text for p in mc_patterns):
        score += 15
        signals.append("Multiple-choice format detected (+15)")

    qa_patterns = ["question.answer", "q&a", "reading comprehension", "qa pairs", "qa dataset"]
    if any(p in combined_text for p in qa_patterns):
        score += 12
        signals.append("QA format detected (+12)")

    cls_patterns = ["classification", "binary label", "sentiment analysis", "hate speech detection",
                    "offensive language", "toxicity detection", "categoriz"]
    if any(p in combined_text for p in cls_patterns):
        score += 10
        signals.append("Classification format detected (+10)")

    gen_patterns = ["open.ended", "generation", "free.text", "generative"]
    if any(p in combined_text for p in gen_patterns):
        score += 5
        signals.append("Open-ended generation (+5)")

    # Dataset size
    if survey_entry and survey_entry.get("dataset_size", ""):
        ds = survey_entry["dataset_size"].lower()
        if ds and "not" not in ds:
            score += 10
            signals.append("Dataset size stated (+10)")

    # LLM_assessed populated
    llm_val = fm.get("LLM_assessed", "").strip()
    if llm_val and llm_val.lower() not in ("na", "n/a", ""):
        score += 10
        signals.append("LLM_assessed populated (+10)")

    # data_metrics populated
    dm_val = fm.get("data_metrics", "").strip()
    if dm_val and dm_val.lower() not in ("not specified", "n/a", "na", ""):
        score += 5
        signals.append("data_metrics populated (+5)")

    # Standard metrics in abstract
    metric_patterns = ["accuracy", "f1", "precision", "recall", "bleu", "rouge",
                       "perplexity", "auc", "macro-f1", "micro-f1"]
    if any(m in abstract for m in metric_patterns):
        score += 5
        signals.append("Standard metrics in abstract (+5)")

    # Data splits mentioned
    split_patterns = ["train.*test", "training.*test", "train/dev/test", "train set",
                      "test set", "validation set", "dev set", "split"]
    if any(re.search(p, combined_text) for p in split_patterns):
        score += 10
        signals.append("Data splits mentioned (+10)")

    # is_benchmark
    if fm.get("is_benchmark", "").strip().lower() == "yes":
        score += 5
        signals.append("is_benchmark = Yes (+5)")

    return min(score, 100), signals


def main():
    print(f"Loading benchmark survey from {SURVEY_PATH}")
    survey_dict = {}
    if SURVEY_PATH.exists():
        with open(SURVEY_PATH, "r", encoding="utf-8") as f:
            survey_list = json.load(f)
        for entry in survey_list:
            fn = entry.get("filename", "")
            survey_dict[fn] = entry
        print(f"  Loaded {len(survey_dict)} survey entries")
    else:
        print("  WARNING: Survey file not found, proceeding without it")

    print(f"Scanning papers in {PAPERS_DIR}/")
    entries = []
    skipped = 0
    errors = 0

    for md_file in sorted(PAPERS_DIR.iterdir()):
        if not md_file.is_file() or md_file.suffix != ".md":
            continue
        if md_file.name in SKIP_FILES:
            continue
        if not is_m_z(md_file.name):
            skipped += 1
            continue

        try:
            text = md_file.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            print(f"  ERROR reading {md_file.name}: {e}")
            errors += 1
            continue

        fm = parse_frontmatter(text)
        survey_entry = survey_dict.get(md_file.name)

        paper_score, signals = score_paper(fm, survey_entry)

        entry = {
            "filename": md_file.name,
            "score": paper_score,
            "signals": signals,
            "is_benchmark": fm.get("is_benchmark", ""),
            "is_dataset": fm.get("is_dataset", ""),
            "data_url": fm.get("DATA_URL", ""),
            "has_survey": survey_entry is not None,
            "availability": survey_entry.get("availability", "") if survey_entry else "",
        }
        entries.append(entry)

    # Sort by score descending
    entries.sort(key=lambda e: e["score"], reverse=True)

    result = {
        "agent": "scorer_m_z",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "count": len(entries),
        "entries": entries,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"\nDone. Scored {len(entries)} M-Z papers (skipped {skipped} non-M-Z, {errors} errors)")
    print(f"Output: {OUTPUT_PATH}")

    # Quick summary
    if entries:
        scores = [e["score"] for e in entries]
        print(f"Score range: {min(scores)}-{max(scores)}, mean: {sum(scores)/len(scores):.1f}")
        top5 = entries[:5]
        print("Top 5:")
        for e in top5:
            print(f"  {e['score']:3d}  {e['filename']}")


if __name__ == "__main__":
    main()
