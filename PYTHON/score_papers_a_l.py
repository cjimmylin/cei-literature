#!/usr/bin/env python3
"""Agent 8: Score papers (A-L authors) on implementability for lm-eval-harness."""

import json
import functools
import re
from datetime import datetime, timezone
from pathlib import Path

print = functools.partial(print, flush=True)

PAPERS_DIR = Path("papers")
SURVEY_PATH = Path("logs/20260216-benchmark_survey_candidates.json")
OUTPUT_PATH = Path("logs/20260312-scores-a-l.json")

SKIP_FILES = {"README.md", "TEMPLATE.md"}


def load_survey():
    """Load benchmark survey as dict keyed by filename."""
    with open(SURVEY_PATH, "r", encoding="utf-8") as f:
        entries = json.load(f)
    return {e["filename"]: e for e in entries}


def parse_frontmatter(filepath):
    """Simple line-based YAML frontmatter parser (no PyYAML)."""
    try:
        content = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        print(f"  WARN: cannot read {filepath.name}: {e}")
        return {}
    metadata = {}
    lines = content.split("\n")
    if lines and lines[0].strip() == "---":
        for line in lines[1:]:
            if line.strip() == "---":
                break
            if ":" in line:
                key, val = line.split(":", 1)
                metadata[key.strip()] = val.strip().strip('"')
    return metadata


def extract_author_letter(filename):
    """Extract the first letter of the author name from YYYY-Author-Title.md pattern."""
    m = re.match(r"^\d{4}-([A-Za-z])", filename)
    if m:
        return m.group(1).upper()
    return None


def is_a_to_l(filename):
    """Check if paper's author starts with A-L, or file starts with 0000-."""
    if filename.startswith("0000-"):
        return True
    letter = extract_author_letter(filename)
    if letter and "A" <= letter <= "L":
        return True
    return False


def score_paper(meta, survey_entry):
    score = 0
    signals = []

    data_url = meta.get("DATA_URL", "")
    if "huggingface.co" in data_url.lower():
        score += 25
        signals.append("HuggingFace dataset URL (+25)")
    if data_url and data_url not in ("", "N/A", "n/a", "Not specified"):
        score += 15
        signals.append("Has DATA_URL (+15)")

    if survey_entry:
        avail = survey_entry.get("availability", "")
        if "Public" in avail:
            score += 15
            signals.append("Public availability (+15)")
        elif "Code" in avail:
            score += 8
            signals.append("Code available (+8)")

        how = (
            survey_entry.get("how_measures", "")
            + " "
            + survey_entry.get("what_measures", "")
        ).lower()
        if any(k in how for k in ["multiple choice", "multiple-choice", "mcq"]):
            score += 15
            signals.append("Multiple-choice format (+15)")
        elif any(k in how for k in ["question answering", "qa ", "q&a"]):
            score += 12
            signals.append("QA format (+12)")
        elif any(k in how for k in ["classification", "binary", "categoriz"]):
            score += 10
            signals.append("Classification format (+10)")
        elif any(k in how for k in ["generation", "open-ended", "free-text"]):
            score += 5
            signals.append("Open-ended generation (+5)")

        ds_size = survey_entry.get("dataset_size", "")
        if ds_size and ds_size not in (
            "Not stated",
            "Not explicitly stated",
            "N/A",
            "",
        ):
            score += 10
            signals.append("Dataset size stated (+10)")

    abstract = meta.get("abstract", "").lower()

    llm = meta.get("LLM_assessed", "")
    if llm and llm not in ("", "N/A", "n/a", "Not specified"):
        score += 10
        signals.append("LLM_assessed populated (+10)")

    dm = meta.get("data_metrics", "")
    if dm and dm not in ("", "N/A", "Not specified"):
        score += 5
        signals.append("data_metrics populated (+5)")

    if any(
        m in abstract
        for m in ["accuracy", " f1 ", "bleu", "rouge", "exact match", "perplexity"]
    ):
        score += 5
        signals.append("Standard metrics mentioned (+5)")

    combined = abstract + " " + (
        survey_entry.get("how_measures", "") if survey_entry else ""
    )
    if any(
        s in combined
        for s in ["train", "test set", "test split", "validation", "dev set"]
    ):
        score += 10
        signals.append("Data splits mentioned (+10)")

    if meta.get("is_benchmark", "") == "Yes":
        score += 5
        signals.append("is_benchmark=Yes (+5)")

    return min(score, 100), signals


def main():
    print("Loading benchmark survey...")
    survey = load_survey()
    print(f"  Survey entries: {len(survey)}")

    print("Scanning papers/ for A-L authors...")
    all_papers = sorted(PAPERS_DIR.glob("*.md"))
    papers = [
        p
        for p in all_papers
        if p.name not in SKIP_FILES and is_a_to_l(p.name)
    ]
    print(f"  Total .md files: {len(all_papers)}, A-L filtered: {len(papers)}")

    entries = []
    for i, paper in enumerate(papers):
        if (i + 1) % 100 == 0:
            print(f"  Scored {i + 1}/{len(papers)}...")

        meta = parse_frontmatter(paper)
        survey_entry = survey.get(paper.name)
        sc, signals = score_paper(meta, survey_entry)

        entries.append(
            {
                "filename": paper.name,
                "score": sc,
                "signals": signals,
                "is_benchmark": meta.get("is_benchmark", ""),
                "is_dataset": meta.get("is_dataset", ""),
                "data_url": meta.get("DATA_URL", ""),
                "has_survey": survey_entry is not None,
                "availability": survey_entry.get("availability", "")
                if survey_entry
                else "",
            }
        )

    # Sort by score descending
    entries.sort(key=lambda e: e["score"], reverse=True)

    output = {
        "agent": "scorer_a_l",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "count": len(entries),
        "entries": entries,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nDone. Scored {len(entries)} papers.")
    print(f"Output: {OUTPUT_PATH}")

    # Quick summary
    buckets = {"80+": 0, "60-79": 0, "40-59": 0, "20-39": 0, "1-19": 0, "0": 0}
    for e in entries:
        s = e["score"]
        if s >= 80:
            buckets["80+"] += 1
        elif s >= 60:
            buckets["60-79"] += 1
        elif s >= 40:
            buckets["40-59"] += 1
        elif s >= 20:
            buckets["20-39"] += 1
        elif s >= 1:
            buckets["1-19"] += 1
        else:
            buckets["0"] += 1
    print("\nScore distribution:")
    for bucket, count in buckets.items():
        print(f"  {bucket}: {count}")


if __name__ == "__main__":
    main()
