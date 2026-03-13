#!/usr/bin/env python3
"""Mine PDF extracts for implementation details (2022-2023).

Agent 5 standalone script — scans PDF Extracts/2022/ and PDF Extracts/2023/
for benchmark/dataset implementation signals.

Usage:
    cd CEI-Lit-WS && ../.venv/bin/python PYTHON/mine_pdf_extracts_2022_2023.py
"""

import functools
import json
import re
from datetime import datetime, timezone
from pathlib import Path

print = functools.partial(print, flush=True)

# --- Configuration ---
PDF_EXTRACTS_DIR = Path("PDF Extracts")
YEARS = ["2022", "2023"]
OUTPUT_FILE = Path("logs/20260312-pdf-impl-details-2022-2023.json")
MAX_CHARS = 10000

# --- Pattern definitions ---

TASK_TYPE_PATTERNS = {
    "multiple_choice": re.compile(
        r"multiple[- ]?choice|MCQ|multi-choice|answer\s+choices|"
        r"choose\s+(the\s+)?(correct|best|right)\s+answer|"
        r"\b[ABCDE]\)\s",
        re.IGNORECASE,
    ),
    "qa": re.compile(
        r"question\s*answer|QA\b|reading\s+comprehension|"
        r"open[- ]ended\s+question|answer\s+extraction|"
        r"extractive\s+QA|abstractive\s+QA",
        re.IGNORECASE,
    ),
    "classification": re.compile(
        r"\bclassification\b|sentiment\s+analysis|"
        r"text\s+classification|label\s+prediction|"
        r"binary\s+classification|multi[- ]class|"
        r"hate\s+speech\s+detection|toxicity\s+detection|"
        r"offensive\s+language\s+detection|stance\s+detection",
        re.IGNORECASE,
    ),
    "generate_until": re.compile(
        r"generate[_\s]until|free[- ]form\s+generation|"
        r"open[- ]ended\s+generation|text\s+generation|"
        r"story\s+generation|dialogue\s+generation|"
        r"conditional\s+generation|seq2seq",
        re.IGNORECASE,
    ),
    "loglikelihood": re.compile(
        r"log[- ]?likelihood|perplexity\s+eval|"
        r"token\s+probability|scoring\s+candidates|"
        r"likelihood\s+ranking|cloze",
        re.IGNORECASE,
    ),
}

DATA_FORMAT_PATTERNS = {
    "JSONL": re.compile(r"\bjsonl\b|\.jsonl\b|json\s+lines", re.IGNORECASE),
    "JSON": re.compile(r"\bjson\b|\.json\b", re.IGNORECASE),
    "CSV": re.compile(r"\bcsv\b|\.csv\b|comma[- ]separated", re.IGNORECASE),
    "TSV": re.compile(r"\btsv\b|\.tsv\b|tab[- ]separated", re.IGNORECASE),
    "Parquet": re.compile(r"\bparquet\b|\.parquet\b", re.IGNORECASE),
    "HuggingFace": re.compile(
        r"hugging\s*face|datasets\.load_dataset|load_dataset\(|"
        r"huggingface\.co/datasets",
        re.IGNORECASE,
    ),
}

SPLIT_PATTERNS = {
    "train": re.compile(r"\btrain(ing)?\s+(set|split|data)\b|\btrain\b", re.IGNORECASE),
    "test": re.compile(r"\btest\s+(set|split|data)\b|\btest\b", re.IGNORECASE),
    "val": re.compile(r"\bval(idation)?\s+(set|split|data)\b|\bval\b", re.IGNORECASE),
    "dev": re.compile(r"\bdev(elopment)?\s+(set|split|data)\b|\bdev\b", re.IGNORECASE),
}

METRIC_PATTERNS = {
    "accuracy": re.compile(r"\baccuracy\b", re.IGNORECASE),
    "F1": re.compile(r"\bF1[- ]?score\b|\bF1\b|\bmacro[- ]?F1\b|\bmicro[- ]?F1\b", re.IGNORECASE),
    "exact_match": re.compile(r"\bexact[_ ]match\b|\bEM\b", re.IGNORECASE),
    "BLEU": re.compile(r"\bBLEU\b", re.IGNORECASE),
    "ROUGE": re.compile(r"\bROUGE\b", re.IGNORECASE),
    "perplexity": re.compile(r"\bperplexity\b|\bPPL\b", re.IGNORECASE),
    "AUC": re.compile(r"\bAUC\b|\bAUROC\b|area\s+under\s+(the\s+)?curve", re.IGNORECASE),
    "precision": re.compile(r"\bprecision\b", re.IGNORECASE),
    "recall": re.compile(r"\brecall\b", re.IGNORECASE),
    "pass@k": re.compile(r"\bpass@k\b|\bpass@\d+\b", re.IGNORECASE),
}

HF_URL_RE = re.compile(r"huggingface\.co/datasets/[\w./-]+", re.IGNORECASE)
GITHUB_URL_RE = re.compile(r"github\.com/[\w./-]+", re.IGNORECASE)
DATASET_SIZE_RE = re.compile(
    r"(\d[\d,]*)\s+(examples?|instances?|samples?|questions?|items?|"
    r"annotations?|entries|dialogues?|sentences?|pairs?|data\s*points?)",
    re.IGNORECASE,
)
PROMPT_HINT_RE = re.compile(
    r"(Question|Answer|Context|Passage|Input|Output|Instruction|Response|Prompt|Query)\s*:",
    re.IGNORECASE,
)


def mine_extract(filepath: Path, year: str) -> dict:
    """Mine a single PDF extract file for implementation details."""
    try:
        text = filepath.read_text(encoding="utf-8")[:MAX_CHARS]
    except Exception as e:
        print(f"  WARN: Could not read {filepath.name}: {e}")
        return None

    entry = {
        "filename": filepath.name,
        "year": year,
        "task_type": None,
        "data_format": [],
        "splits": [],
        "metrics": [],
        "hf_urls": [],
        "github_urls": [],
        "dataset_size": None,
        "prompt_hints": [],
    }

    # Task type — pick first match
    for ttype, pat in TASK_TYPE_PATTERNS.items():
        if pat.search(text):
            entry["task_type"] = ttype
            break

    # Data formats
    for fmt, pat in DATA_FORMAT_PATTERNS.items():
        if pat.search(text):
            entry["data_format"].append(fmt)

    # Splits
    for split, pat in SPLIT_PATTERNS.items():
        if pat.search(text):
            entry["splits"].append(split)

    # Metrics
    for metric, pat in METRIC_PATTERNS.items():
        if pat.search(text):
            entry["metrics"].append(metric)

    # HuggingFace URLs
    hf_matches = HF_URL_RE.findall(text)
    entry["hf_urls"] = sorted(set(hf_matches))

    # GitHub URLs
    gh_matches = GITHUB_URL_RE.findall(text)
    # Clean trailing punctuation
    cleaned = []
    for url in gh_matches:
        url = url.rstrip(".,;:)")
        if len(url) > len("github.com/x/y"):
            cleaned.append(url)
    entry["github_urls"] = sorted(set(cleaned))

    # Dataset size — pick largest mentioned
    size_matches = DATASET_SIZE_RE.findall(text)
    if size_matches:
        sizes = []
        for num_str, unit in size_matches:
            try:
                num = int(num_str.replace(",", ""))
                sizes.append(f"{num_str} {unit}")
            except ValueError:
                pass
        if sizes:
            entry["dataset_size"] = sizes[0]  # first mention

    # Prompt hints
    hint_matches = PROMPT_HINT_RE.findall(text)
    entry["prompt_hints"] = sorted(set(hint_matches))

    return entry


def main():
    print(f"=== PDF Extract Miner (2022-2023) ===")
    print(f"Base dir: {PDF_EXTRACTS_DIR.resolve()}")

    all_entries = []

    for year in YEARS:
        year_dir = PDF_EXTRACTS_DIR / year
        if not year_dir.is_dir():
            print(f"WARN: Directory not found: {year_dir}")
            continue

        # Use iterdir() to avoid glob metacharacter issues
        md_files = sorted(
            [f for f in year_dir.iterdir() if f.suffix == ".md"],
            key=lambda p: p.name,
        )
        print(f"\n--- Year {year}: {len(md_files)} extract files ---")

        for i, fpath in enumerate(md_files, 1):
            entry = mine_extract(fpath, year)
            if entry:
                all_entries.append(entry)
                # Log entries that found something interesting
                has_signal = (
                    entry["task_type"]
                    or entry["data_format"]
                    or entry["hf_urls"]
                    or entry["github_urls"]
                    or entry["dataset_size"]
                )
                if has_signal and i <= 5:
                    print(f"  [{i}] {fpath.name}: task={entry['task_type']}, "
                          f"formats={entry['data_format']}, "
                          f"size={entry['dataset_size']}")

            if i % 25 == 0:
                print(f"  ... processed {i}/{len(md_files)}")

        print(f"  Completed {year}: {len([e for e in all_entries if e['year'] == year])} entries")

    # Summary stats
    with_task = sum(1 for e in all_entries if e["task_type"])
    with_format = sum(1 for e in all_entries if e["data_format"])
    with_hf = sum(1 for e in all_entries if e["hf_urls"])
    with_gh = sum(1 for e in all_entries if e["github_urls"])
    with_size = sum(1 for e in all_entries if e["dataset_size"])
    with_metrics = sum(1 for e in all_entries if e["metrics"])
    with_prompts = sum(1 for e in all_entries if e["prompt_hints"])

    print(f"\n=== Summary ===")
    print(f"Total entries: {len(all_entries)}")
    print(f"  with task_type:    {with_task}")
    print(f"  with data_format:  {with_format}")
    print(f"  with hf_urls:      {with_hf}")
    print(f"  with github_urls:  {with_gh}")
    print(f"  with dataset_size: {with_size}")
    print(f"  with metrics:      {with_metrics}")
    print(f"  with prompt_hints: {with_prompts}")

    # Task type distribution
    task_dist = {}
    for e in all_entries:
        t = e["task_type"] or "none"
        task_dist[t] = task_dist.get(t, 0) + 1
    print(f"\nTask type distribution:")
    for t, c in sorted(task_dist.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")

    # Write output
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    output = {
        "agent": "pdf_miner_2022_2023",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "count": len(all_entries),
        "entries": all_entries,
    }

    tmp_path = OUTPUT_FILE.with_suffix(f".tmp.{__import__('os').getpid()}.json")
    tmp_path.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    import os
    os.replace(str(tmp_path), str(OUTPUT_FILE))

    print(f"\nOutput written to: {OUTPUT_FILE} ({len(all_entries)} entries)")
    print("Done.")


if __name__ == "__main__":
    main()
