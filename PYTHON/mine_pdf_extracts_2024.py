#!/usr/bin/env python3
"""Mine PDF extracts for year 2024 — extract implementation details from benchmark/dataset papers."""

import functools
import json
import re
from datetime import datetime, timezone
from pathlib import Path

print = functools.partial(print, flush=True)

EXTRACT_DIR = Path("PDF Extracts/2024")
OUTPUT_PATH = Path("logs/20260312-pdf-impl-details-2024.json")
MAX_CHARS = 10000

# --- Pattern definitions ---

TASK_TYPE_PATTERNS = [
    ("multiple_choice", re.compile(r"multiple[\s\-]choice", re.IGNORECASE)),
    ("qa", re.compile(r"question[\s\-]answering|(?<!\w)QA(?!\w)", re.IGNORECASE)),
    ("classification", re.compile(r"\bclassification\b|\bbinary\b", re.IGNORECASE)),
    ("generate_until", re.compile(r"\bgeneration\b|\bopen[\s\-]ended\b", re.IGNORECASE)),
    ("loglikelihood", re.compile(r"\bfill[\s\-]in\b|\bcloze\b|\bperplexity\b", re.IGNORECASE)),
]

DATA_FORMAT_PATTERNS = {
    "JSONL": re.compile(r"\bJSONL\b", re.IGNORECASE),
    "JSON": re.compile(r"\bJSON\b(?!L)", re.IGNORECASE),
    "CSV": re.compile(r"\bCSV\b", re.IGNORECASE),
    "TSV": re.compile(r"\bTSV\b", re.IGNORECASE),
    "Parquet": re.compile(r"\bParquet\b", re.IGNORECASE),
    "HuggingFace": re.compile(r"\bHugging\s*Face\b|\bhf\b|\bdatasets\s+library\b", re.IGNORECASE),
}

SPLIT_PATTERNS = {
    "train": re.compile(r"\btrain(?:ing)?\s+(?:set|split|data)\b|\btrain\b", re.IGNORECASE),
    "test": re.compile(r"\btest\s+(?:set|split|data)\b|\btest\b", re.IGNORECASE),
    "val": re.compile(r"\bval(?:idation)?\s+(?:set|split|data)\b|\bval(?:idation)?\b", re.IGNORECASE),
    "dev": re.compile(r"\bdev(?:elopment)?\s+(?:set|split|data)\b|\bdev\b", re.IGNORECASE),
}

METRIC_PATTERNS = {
    "accuracy": re.compile(r"\baccuracy\b", re.IGNORECASE),
    "F1": re.compile(r"\bF1\b(?:\s*-?\s*score)?", re.IGNORECASE),
    "exact_match": re.compile(r"\bexact[\s_]match\b", re.IGNORECASE),
    "BLEU": re.compile(r"\bBLEU\b", re.IGNORECASE),
    "ROUGE": re.compile(r"\bROUGE\b", re.IGNORECASE),
    "perplexity": re.compile(r"\bperplexity\b", re.IGNORECASE),
    "AUC": re.compile(r"\bAUC\b", re.IGNORECASE),
    "precision": re.compile(r"\bprecision\b", re.IGNORECASE),
    "recall": re.compile(r"\brecall\b", re.IGNORECASE),
    "pass@k": re.compile(r"\bpass@k\b|\bpass@\d+\b", re.IGNORECASE),
}

HF_URL_RE = re.compile(r"huggingface\.co/datasets/[\w\-/]+")
GITHUB_URL_RE = re.compile(r"github\.com/[\w\-/]+")
DATASET_SIZE_RE = re.compile(
    r"(\d[\d,\.]*\s*(?:K|M|k|m)?\s*(?:examples?|instances?|samples?|questions?|items?|entries|rows|pairs?|sentences?))",
    re.IGNORECASE,
)
PROMPT_HINT_RE = re.compile(
    r"((?:prompt|template|instruction|system\s+message)[\s:]+[^\n]{10,80})",
    re.IGNORECASE,
)


def detect_task_type(text):
    for task_type, pattern in TASK_TYPE_PATTERNS:
        if pattern.search(text):
            return task_type
    return None


def detect_list(text, patterns):
    return sorted(k for k, p in patterns.items() if p.search(text))


def mine_extract(filepath: Path) -> dict:
    text = filepath.read_text(encoding="utf-8", errors="replace")[:MAX_CHARS]

    entry = {
        "filename": filepath.name,
        "year": "2024",
        "task_type": detect_task_type(text),
        "data_format": detect_list(text, DATA_FORMAT_PATTERNS),
        "splits": detect_list(text, SPLIT_PATTERNS),
        "metrics": detect_list(text, METRIC_PATTERNS),
        "hf_urls": sorted(set(HF_URL_RE.findall(text))),
        "github_urls": sorted(set(GITHUB_URL_RE.findall(text))),
        "dataset_size": None,
        "prompt_hints": [],
    }

    size_match = DATASET_SIZE_RE.search(text)
    if size_match:
        entry["dataset_size"] = size_match.group(1).strip()

    prompt_matches = PROMPT_HINT_RE.findall(text)
    if prompt_matches:
        entry["prompt_hints"] = list(dict.fromkeys(prompt_matches))[:5]  # dedupe, max 5

    return entry


def main():
    if not EXTRACT_DIR.is_dir():
        print(f"ERROR: Directory not found: {EXTRACT_DIR}")
        return

    md_files = sorted(EXTRACT_DIR.iterdir())
    md_files = [f for f in md_files if f.suffix == ".md"]
    print(f"Found {len(md_files)} extract files in {EXTRACT_DIR}")

    entries = []
    for i, filepath in enumerate(md_files, 1):
        if i % 100 == 0:
            print(f"  Processed {i}/{len(md_files)}...")
        try:
            entry = mine_extract(filepath)
            entries.append(entry)
        except Exception as e:
            print(f"  ERROR on {filepath.name}: {e}")

    output = {
        "agent": "pdf_miner_2024",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "count": len(entries),
        "entries": entries,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nWrote {len(entries)} entries to {OUTPUT_PATH}")

    # Summary stats
    has_task = sum(1 for e in entries if e["task_type"])
    has_fmt = sum(1 for e in entries if e["data_format"])
    has_metrics = sum(1 for e in entries if e["metrics"])
    has_hf = sum(1 for e in entries if e["hf_urls"])
    has_gh = sum(1 for e in entries if e["github_urls"])
    has_size = sum(1 for e in entries if e["dataset_size"])
    has_prompts = sum(1 for e in entries if e["prompt_hints"])

    print(f"\n=== Summary ===")
    print(f"  task_type:    {has_task}/{len(entries)}")
    print(f"  data_format:  {has_fmt}/{len(entries)}")
    print(f"  metrics:      {has_metrics}/{len(entries)}")
    print(f"  hf_urls:      {has_hf}/{len(entries)}")
    print(f"  github_urls:  {has_gh}/{len(entries)}")
    print(f"  dataset_size: {has_size}/{len(entries)}")
    print(f"  prompt_hints: {has_prompts}/{len(entries)}")


if __name__ == "__main__":
    main()
