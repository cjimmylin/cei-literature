#!/usr/bin/env python3
"""Mine PDF extracts for implementation-relevant details for lm-eval-harness.

Usage: python mine_pdf_extracts.py START_YEAR END_YEAR OUTPUT_FILE
"""

import functools
import json
import os
import re
import sys
from datetime import datetime, timezone

print = functools.partial(print, flush=True)

EXTRACTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "PDF Extracts")


def extract_task_type(text):
    """Detect task type from content keywords."""
    text_lower = text.lower()
    if re.search(r'multiple[\s-]choice', text_lower):
        return "multiple_choice"
    if re.search(r'\bquestion answering\b|\bQA\b', text):
        return "qa"
    if re.search(r'\b(?:binary\s+)?classification\b', text_lower):
        return "classification"
    if re.search(r'\bgenerat(?:ion|e)\b|\bopen[\s-]ended\b', text_lower):
        return "generate_until"
    if re.search(r'\bfill[\s-]in\b|\bcloze\b', text_lower):
        return "loglikelihood"
    return None


def extract_data_format(text):
    """Detect data format mentions."""
    formats = []
    text_upper = text.upper()
    for fmt in ["JSONL", "JSON", "CSV", "TSV", "Parquet"]:
        if fmt.upper() in text_upper:
            # JSONL before JSON to avoid double-counting
            if fmt == "JSON" and "JSONL" in text_upper:
                if re.search(r'\bJSON\b(?!L)', text):
                    formats.append(fmt)
            else:
                if re.search(rf'\b{fmt}\b', text, re.IGNORECASE):
                    formats.append(fmt)
    if re.search(r'\bHuggingFace\b|\bHugging\s+Face\b|\bhf\b', text, re.IGNORECASE):
        if "HuggingFace" not in formats:
            formats.append("HuggingFace")
    return formats


def extract_splits(text):
    """Detect dataset splits mentioned."""
    splits = set()
    text_lower = text.lower()
    if re.search(r'\b(?:training|train)\s+(?:set|split|data)\b', text_lower):
        splits.add("train")
    if re.search(r'\b(?:test)\s+(?:set|split|data)\b', text_lower):
        splits.add("test")
    if re.search(r'\b(?:validation|valid)\s+(?:set|split|data)\b', text_lower):
        splits.add("validation")
    if re.search(r'\b(?:dev|development)\s+(?:set|split|data)\b', text_lower):
        splits.add("dev")
    return sorted(splits)


def extract_metrics(text):
    """Detect evaluation metrics mentioned."""
    metrics = []
    patterns = [
        (r'\baccuracy\b', "accuracy"),
        (r'\bF1\b', "F1"),
        (r'\bexact match\b', "exact match"),
        (r'\bBLEU\b', "BLEU"),
        (r'\bROUGE\b', "ROUGE"),
        (r'\bperplexity\b', "perplexity"),
        (r'\bAUC\b', "AUC"),
        (r'\bprecision\b', "precision"),
        (r'\brecall\b', "recall"),
        (r'\bpass@k\b', "pass@k"),
        (r'\bwin rate\b', "win rate"),
        (r'\bLikert\b', "Likert"),
    ]
    for pat, name in patterns:
        if re.search(pat, text, re.IGNORECASE if name not in ("F1", "BLEU", "ROUGE", "AUC") else 0):
            metrics.append(name)
    return metrics


def extract_hf_urls(text):
    """Extract HuggingFace dataset URLs."""
    return list(set(re.findall(r'https?://huggingface\.co/datasets/[^\s\)\]\"\'<>]+', text)))


def extract_github_urls(text):
    """Extract GitHub URLs."""
    return list(set(re.findall(r'https?://github\.com/[^\s\)\]\"\'<>]+', text)))


def extract_dataset_size(text):
    """Extract dataset size mentions like 'N examples'."""
    pat = r'(?<![,\d])([1-9][\d,]*)\s+(?:examples|instances|samples|questions|items|scenarios|pairs|sentences|prompts|entries|data\s+points)'
    m = re.search(pat, text, re.IGNORECASE)
    if m:
        return m.group(0).replace('\n', ' ')
    return None


def extract_prompt_hints(text):
    """Look for template-like patterns with prompt structure keywords."""
    hints = []
    # Look for lines containing template markers
    for line in text.split('\n'):
        line_stripped = line.strip()
        if re.search(r'\b(?:Question|Answer|Context|Prompt|Input|Output|Instruction|Template)\s*:', line_stripped, re.IGNORECASE):
            # Only grab short-ish lines that look like templates
            if 10 < len(line_stripped) < 300:
                hints.append(line_stripped)
    # Deduplicate while preserving order, cap at 5
    seen = set()
    unique = []
    for h in hints:
        if h not in seen:
            seen.add(h)
            unique.append(h)
        if len(unique) >= 5:
            break
    return unique


def process_file(filepath, year_str):
    """Process a single PDF extract file."""
    filename = os.path.basename(filepath)
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            text = f.read(10000)
    except Exception as e:
        print(f"  ERROR reading {filename}: {e}")
        return None

    if not text.strip():
        return None

    entry = {
        "filename": filename,
        "year": year_str,
        "task_type": extract_task_type(text),
        "data_format": extract_data_format(text),
        "splits": extract_splits(text),
        "metrics": extract_metrics(text),
        "hf_urls": extract_hf_urls(text),
        "github_urls": extract_github_urls(text),
        "dataset_size": extract_dataset_size(text),
        "prompt_hints": extract_prompt_hints(text),
    }
    return entry


def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} START_YEAR END_YEAR OUTPUT_FILE")
        sys.exit(1)

    start_year = int(sys.argv[1])
    end_year = int(sys.argv[2])
    output_file = sys.argv[3]

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file) or '.', exist_ok=True)

    entries = []
    total_files = 0

    for year in range(start_year, end_year + 1):
        year_str = str(year)
        year_dir = os.path.join(EXTRACTS_DIR, year_str)

        if not os.path.isdir(year_dir):
            print(f"[{year_str}] Directory not found, skipping: {year_dir}")
            continue

        # Use iterdir pattern (avoid rglob/glob metacharacter issues)
        md_files = sorted([
            os.path.join(year_dir, f)
            for f in os.listdir(year_dir)
            if f.endswith('.md') and os.path.isfile(os.path.join(year_dir, f))
        ])

        print(f"[{year_str}] Found {len(md_files)} extract files")

        for filepath in md_files:
            total_files += 1
            entry = process_file(filepath, year_str)
            if entry is not None:
                entries.append(entry)

    # Build output
    output = {
        "agent": "pdf_miner_2016_2021",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "count": len(entries),
        "entries": entries,
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nDone. Processed {total_files} files, wrote {len(entries)} entries to {output_file}")


if __name__ == "__main__":
    main()
