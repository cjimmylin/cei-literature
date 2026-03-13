#!/usr/bin/env python3
"""Mine PDF extracts for 2025-2026 to find implementation details:
task types, data formats, splits, metrics, URLs, dataset sizes, prompt hints.

Output: logs/20260312-pdf-impl-details-2025-2026.json
"""

import functools
import json
import re
from datetime import datetime, timezone
from pathlib import Path

print = functools.partial(print, flush=True)

# --- Paths ---
WORKSPACE = Path(__file__).resolve().parent.parent  # CEI-Lit-WS/
EXTRACTS_DIR = WORKSPACE / "PDF Extracts"
LOGS_DIR = WORKSPACE / "logs"

YEARS = ["2025", "2026"]
MAX_CHARS = 10_000

# --- Patterns ---

TASK_TYPES = {
    "multiple_choice": re.compile(
        r"multiple[- ]?choice|multi[- ]?choice|MCQ|MCQA", re.IGNORECASE
    ),
    "qa": re.compile(
        r"\bQA\b|question[- ]?answer(?:ing)?|reading comprehension", re.IGNORECASE
    ),
    "classification": re.compile(
        r"\bclassification\b|\bclassif(?:y|ied|ier)\b|sentiment analysis|text classification",
        re.IGNORECASE,
    ),
    "generate_until": re.compile(
        r"generat(?:e|ion)\b.*(?:until|open[- ]ended|free[- ]form)|open[- ]ended generation",
        re.IGNORECASE,
    ),
    "loglikelihood": re.compile(
        r"log[- ]?likelihood|perplexity scoring|token probability", re.IGNORECASE
    ),
}

DATA_FORMATS = {
    "JSONL": re.compile(r"\bJSONL\b|\.jsonl\b", re.IGNORECASE),
    "JSON": re.compile(r"\bJSON\b|\.json\b", re.IGNORECASE),
    "CSV": re.compile(r"\bCSV\b|\.csv\b", re.IGNORECASE),
    "TSV": re.compile(r"\bTSV\b|\.tsv\b", re.IGNORECASE),
    "Parquet": re.compile(r"\bParquet\b|\.parquet\b", re.IGNORECASE),
    "HuggingFace": re.compile(
        r"Hugging\s*Face|HuggingFace|datasets\.load_dataset|load_dataset\s*\(",
        re.IGNORECASE,
    ),
}

SPLITS = {
    "train": re.compile(r"\btrain(?:ing)?\s+(?:set|split|data)\b|\btrain\b", re.IGNORECASE),
    "test": re.compile(r"\btest\s+(?:set|split|data)\b|\btest\b", re.IGNORECASE),
    "val": re.compile(r"\bval(?:idation)?\s+(?:set|split|data)\b|\bval\b", re.IGNORECASE),
    "dev": re.compile(r"\bdev(?:elopment)?\s+(?:set|split|data)\b|\bdev\b", re.IGNORECASE),
}

METRICS = {
    "accuracy": re.compile(r"\baccuracy\b", re.IGNORECASE),
    "F1": re.compile(r"\bF1\b|\bF1[- ]score\b", re.IGNORECASE),
    "exact_match": re.compile(r"\bexact[_ ]match\b|\bEM\b", re.IGNORECASE),
    "BLEU": re.compile(r"\bBLEU\b", re.IGNORECASE),
    "ROUGE": re.compile(r"\bROUGE\b", re.IGNORECASE),
    "perplexity": re.compile(r"\bperplexity\b|\bPPL\b", re.IGNORECASE),
    "AUC": re.compile(r"\bAUC\b|\bAUROC\b", re.IGNORECASE),
    "precision": re.compile(r"\bprecision\b", re.IGNORECASE),
    "recall": re.compile(r"\brecall\b", re.IGNORECASE),
    "pass@k": re.compile(r"\bpass@k\b|\bpass@\d+\b", re.IGNORECASE),
}

RE_HF_URL = re.compile(r"huggingface\.co/datasets/[\w\-/]+")
RE_GH_URL = re.compile(r"github\.com/[\w\-/]+")
RE_DATASET_SIZE = re.compile(
    r"(\d[\d,]*)\s+(?:examples?|instances?|samples?|questions?|items?)\b", re.IGNORECASE
)
RE_PROMPT_HINT = re.compile(
    r"prompt\s+template|instruction\s+template|system\s+prompt|few[- ]shot\s+prompt|"
    r"zero[- ]shot\s+prompt|chain[- ]of[- ]thought|CoT\s+prompt",
    re.IGNORECASE,
)


def mine_extract(filepath: Path, year: str) -> dict:
    """Mine a single PDF extract file."""
    text = filepath.read_text(encoding="utf-8", errors="replace")[:MAX_CHARS]

    entry = {
        "filename": filepath.name,
        "year": year,
        "task_type": [],
        "data_format": [],
        "splits": [],
        "metrics": [],
        "hf_urls": [],
        "github_urls": [],
        "dataset_size": [],
        "prompt_hints": [],
    }

    for name, pat in TASK_TYPES.items():
        if pat.search(text):
            entry["task_type"].append(name)

    for name, pat in DATA_FORMATS.items():
        if pat.search(text):
            entry["data_format"].append(name)

    for name, pat in SPLITS.items():
        if pat.search(text):
            entry["splits"].append(name)

    for name, pat in METRICS.items():
        if pat.search(text):
            entry["metrics"].append(name)

    entry["hf_urls"] = sorted(set(RE_HF_URL.findall(text)))
    entry["github_urls"] = sorted(set(RE_GH_URL.findall(text)))

    size_matches = RE_DATASET_SIZE.findall(text)
    if size_matches:
        # Deduplicate and keep up to 5
        entry["dataset_size"] = sorted(set(size_matches))[:5]

    prompt_matches = RE_PROMPT_HINT.findall(text)
    if prompt_matches:
        entry["prompt_hints"] = sorted(set(m.strip() for m in prompt_matches))[:5]

    return entry


def main():
    print(f"[mine_pdf_extracts_2025_2026] Starting at {datetime.now(timezone.utc).isoformat()}")

    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    entries = []
    for year in YEARS:
        year_dir = EXTRACTS_DIR / year
        if not year_dir.is_dir():
            print(f"  Skipping {year}: directory does not exist")
            continue

        # Use iterdir() to avoid glob metacharacter issues with [ ] in filenames
        md_files = sorted(f for f in year_dir.iterdir() if f.suffix == ".md")
        print(f"  {year}: found {len(md_files)} extract files")

        for fp in md_files:
            try:
                entry = mine_extract(fp, year)
                entries.append(entry)
            except Exception as exc:
                print(f"  ERROR processing {fp.name}: {exc}")

    # Build output
    output = {
        "agent": "pdf_miner_2025_2026",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "count": len(entries),
        "entries": entries,
    }

    out_path = LOGS_DIR / "20260312-pdf-impl-details-2025-2026.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n  Wrote {len(entries)} entries to {out_path}")

    # Summary stats
    has_task = sum(1 for e in entries if e["task_type"])
    has_metric = sum(1 for e in entries if e["metrics"])
    has_hf = sum(1 for e in entries if e["hf_urls"])
    has_gh = sum(1 for e in entries if e["github_urls"])
    has_size = sum(1 for e in entries if e["dataset_size"])
    has_prompt = sum(1 for e in entries if e["prompt_hints"])

    print(f"\n  Summary ({len(entries)} total extracts):")
    print(f"    task_type found:   {has_task}")
    print(f"    metrics found:     {has_metric}")
    print(f"    hf_urls found:     {has_hf}")
    print(f"    github_urls found: {has_gh}")
    print(f"    dataset_size:      {has_size}")
    print(f"    prompt_hints:      {has_prompt}")
    print(f"\n[mine_pdf_extracts_2025_2026] Done.")


if __name__ == "__main__":
    main()
