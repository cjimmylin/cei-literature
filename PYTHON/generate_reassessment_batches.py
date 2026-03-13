#!/usr/bin/env python3
"""
Phase B.1: Generate batch files for LLM re-assessment.

Unlike the original generate_llm_assessment_batches.py, this targets ALL papers
(not just those missing fields) and includes current field values so agents can
compare/correct. Papers are tiered by data availability:
  - Tier 1: Has PDF extract + non-NA LLM_assessed (most correctable errors)
  - Tier 2: Has PDF extract + LLM_assessed=NA (may find missed models)
  - Tier 3: No PDF extract (abstract-only, lower confidence)

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/generate_reassessment_batches.py --pilot 50
    ../.venv/bin/python PYTHON/generate_reassessment_batches.py --tier 1 --num-batches 30
    ../.venv/bin/python PYTHON/generate_reassessment_batches.py --tier all

Output:
    logs/YYYYMMDD-reassessment_batch_01.json through batch_NN.json
    logs/YYYYMMDD-reassessment_manifest.json
"""

from __future__ import annotations

import argparse
import functools
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

print = functools.partial(print, flush=True)

sys.path.insert(0, str(Path(__file__).parent.parent / ".agent"))
from lib.config import LOGS_DIR, PAPERS_DIR, PDF_EXTRACTS_DIR  # noqa: E402
from lib.yaml_utils import extract_frontmatter, parse_frontmatter  # noqa: E402

DATE_PREFIX = datetime.now().strftime("%Y%m%d")

NA_VALUES = {"", "NA", "N/A", "NONE", "NULL"}


def clean_scalar(value: str | None) -> str:
    """Strip quotes and whitespace from a YAML scalar value."""
    s = (value or "").strip()
    if len(s) >= 2 and ((s.startswith('"') and s.endswith('"')) or
                         (s.startswith("'") and s.endswith("'"))):
        s = s[1:-1].strip()
    return s


def resolve_extract_path(paper_path: Path, fm_text: str) -> str | None:
    """Resolve the PDF extract path for a paper, return relative path or None."""
    fields = parse_frontmatter(fm_text)
    extract_ref = fields.get("pdf_extract", "").strip("\"'")
    if extract_ref:
        extract_path = PAPERS_DIR.parent / extract_ref
        if extract_path.exists():
            return extract_ref

    # Fallback: try matching filename in year-based subdirs
    stem = paper_path.stem
    for subdir in sorted(PDF_EXTRACTS_DIR.iterdir()):
        if subdir.is_dir():
            candidate = subdir / f"{stem}.md"
            if candidate.exists():
                return f"PDF Extracts/{subdir.name}/{candidate.name}"

    # Fallback: try root of PDF Extracts
    candidate = PDF_EXTRACTS_DIR / f"{stem}.md"
    if candidate.exists():
        return f"PDF Extracts/{stem}.md"

    return None


def extract_abstract_snippet(body: str, max_chars: int = 500) -> str:
    """Extract first paragraph or abstract from paper body."""
    # Try to find ## Abstract section
    abstract_match = re.search(
        r"(?ms)^## Abstract\s*\n(.*?)(?=^## |\Z)", body
    )
    if abstract_match:
        text = abstract_match.group(1).strip()
        if len(text) > max_chars:
            text = text[:max_chars] + "..."
        return text

    # Fallback: first non-empty paragraph
    for para in body.split("\n\n"):
        text = para.strip()
        if text and not text.startswith("#") and len(text) > 50:
            if len(text) > max_chars:
                text = text[:max_chars] + "..."
            return text

    return ""


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate reassessment batches")
    parser.add_argument("--pilot", type=int, default=0,
                        help="Pilot mode: select N papers (mixed tiers)")
    parser.add_argument("--num-batches", type=int, default=0,
                        help="Number of batches (default: auto)")
    parser.add_argument("--batch-size", type=int, default=45,
                        help="Target batch size (default: 45)")
    parser.add_argument("--tier", type=str, default="all",
                        choices=["1", "2", "3", "all"],
                        help="Which tier(s) to include (default: all)")
    args = parser.parse_args()

    print("=" * 60)
    print("Phase B.1: Reassessment Batch Generation")
    print("=" * 60)
    print()

    # ── Scan all papers ──────────────────────────────────────────────────
    tier1: list[dict] = []  # Has extract + non-NA LLM_assessed
    tier2: list[dict] = []  # Has extract + LLM_assessed=NA
    tier3: list[dict] = []  # No extract
    errors = 0

    paper_paths = sorted(PAPERS_DIR.glob("*.md"))
    print(f"Scanning {len(paper_paths)} papers...")

    for paper_path in paper_paths:
        try:
            content = paper_path.read_text(encoding="utf-8")
            fm_text, body = extract_frontmatter(content)
        except (ValueError, UnicodeDecodeError) as e:
            print(f"  ERROR: {paper_path.name}: {e}")
            errors += 1
            continue

        fields = parse_frontmatter(fm_text)
        extract_ref = resolve_extract_path(paper_path, fm_text)
        has_extract = extract_ref is not None

        llm_raw = clean_scalar(fields.get("LLM_assessed"))
        data_url_raw = clean_scalar(fields.get("DATA_URL"))
        is_benchmark_raw = clean_scalar(fields.get("is_benchmark"))
        is_eval_raw = clean_scalar(fields.get("is_eval"))
        is_dataset_raw = clean_scalar(fields.get("is_dataset"))
        data_desc_raw = clean_scalar(fields.get("data_description"))

        abstract_snippet = extract_abstract_snippet(body)

        entry = {
            "filename": paper_path.name,
            "pdf_extract_path": extract_ref or "",
            "has_extract": has_extract,
            "current_LLM_assessed": llm_raw if llm_raw else "NA",
            "current_DATA_URL": data_url_raw if data_url_raw else "NA",
            "current_is_benchmark": is_benchmark_raw if is_benchmark_raw else "NA",
            "current_is_eval": is_eval_raw if is_eval_raw else "NA",
            "current_is_dataset": is_dataset_raw if is_dataset_raw else "NA",
            "current_data_description": data_desc_raw if data_desc_raw else "NA",
            "abstract_snippet": abstract_snippet,
        }

        llm_is_na = llm_raw.upper() in NA_VALUES if llm_raw else True

        if has_extract and not llm_is_na:
            entry["tier"] = 1
            tier1.append(entry)
        elif has_extract and llm_is_na:
            entry["tier"] = 2
            tier2.append(entry)
        else:
            entry["tier"] = 3
            tier3.append(entry)

    print(f"\nTier distribution:")
    print(f"  Tier 1 (extract + LLM models): {len(tier1)}")
    print(f"  Tier 2 (extract + LLM=NA):     {len(tier2)}")
    print(f"  Tier 3 (no extract):           {len(tier3)}")
    print(f"  Errors:                        {errors}")
    print(f"  Total:                         {len(tier1) + len(tier2) + len(tier3)}")

    # ── Select papers based on tier filter ────────────────────────────────
    if args.tier == "1":
        papers = tier1
    elif args.tier == "2":
        papers = tier2
    elif args.tier == "3":
        papers = tier3
    else:
        papers = tier1 + tier2 + tier3

    print(f"\nSelected tier(s): {args.tier} → {len(papers)} papers")

    if not papers:
        print("No papers to process. Exiting.")
        return

    # ── Apply pilot limit ─────────────────────────────────────────────────
    if args.pilot > 0:
        # Select a mix from all tiers proportionally
        pilot_n = min(args.pilot, len(papers))

        # If we have all tiers, sample proportionally
        if args.tier == "all" and tier1 and tier2 and tier3:
            total = len(tier1) + len(tier2) + len(tier3)
            n1 = max(1, round(pilot_n * len(tier1) / total))
            n2 = max(1, round(pilot_n * len(tier2) / total))
            n3 = max(1, pilot_n - n1 - n2)
            # Clamp to available
            n1 = min(n1, len(tier1))
            n2 = min(n2, len(tier2))
            n3 = min(n3, len(tier3))
            papers = tier1[:n1] + tier2[:n2] + tier3[:n3]
        else:
            papers = papers[:pilot_n]

        print(f"\nPILOT MODE: Selected {len(papers)} papers")
        tier_counts = {}
        for p in papers:
            t = p.get("tier", "?")
            tier_counts[t] = tier_counts.get(t, 0) + 1
        for t, c in sorted(tier_counts.items()):
            print(f"  Tier {t}: {c}")

    # ── Determine batch count ─────────────────────────────────────────────
    if args.num_batches > 0:
        num_batches = args.num_batches
    elif args.pilot > 0:
        num_batches = max(1, len(papers) // 10)
        if num_batches < 1:
            num_batches = 1
    else:
        num_batches = max(1, -(-len(papers) // args.batch_size))  # ceil division

    # Calculate batch sizes
    base_size = len(papers) // num_batches
    remainder = len(papers) % num_batches
    batch_sizes = [base_size + (1 if i < remainder else 0) for i in range(num_batches)]
    batch_sizes = [s for s in batch_sizes if s > 0]
    num_batches = len(batch_sizes)

    print(f"\nSplitting {len(papers)} papers into {num_batches} batches")

    # ── Write batch files ─────────────────────────────────────────────────
    idx = 0
    batch_files = []
    for batch_num, size in enumerate(batch_sizes, 1):
        batch = papers[idx:idx + size]
        idx += size

        out_name = f"{DATE_PREFIX}-reassessment_batch_{batch_num:02d}.json"
        out_path = LOGS_DIR / out_name

        tmp_path = out_path.parent / f".tmp.{os.getpid()}.{batch_num}.json"
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(batch, f, indent=2, ensure_ascii=False)
        os.replace(str(tmp_path), str(out_path))

        batch_files.append(out_name)
        has_count = sum(1 for p in batch if p["has_extract"])
        tier_dist = {}
        for p in batch:
            t = p.get("tier", "?")
            tier_dist[t] = tier_dist.get(t, 0) + 1
        tier_str = ", ".join(f"T{t}:{c}" for t, c in sorted(tier_dist.items()))
        print(f"  Batch {batch_num:02d}: {len(batch)} papers ({has_count} with extract, {tier_str}) → {out_name}")

    # ── Write manifest ────────────────────────────────────────────────────
    manifest = {
        "date": DATE_PREFIX,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "total_papers": len(papers),
        "num_batches": num_batches,
        "batch_size_target": args.batch_size,
        "pilot": args.pilot > 0,
        "pilot_n": args.pilot if args.pilot > 0 else None,
        "tier_filter": args.tier,
        "tier_counts": {
            "tier1": sum(1 for p in papers if p.get("tier") == 1),
            "tier2": sum(1 for p in papers if p.get("tier") == 2),
            "tier3": sum(1 for p in papers if p.get("tier") == 3),
        },
        "batch_files": batch_files,
    }

    manifest_path = LOGS_DIR / f"{DATE_PREFIX}-reassessment_manifest.json"
    tmp_path = manifest_path.parent / f".tmp.{os.getpid()}.manifest.json"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    os.replace(str(tmp_path), str(manifest_path))

    print(f"\nManifest: {manifest_path.name}")

    # ── Print agent prompt template ───────────────────────────────────────
    print("\n" + "=" * 60)
    print("AGENT PROMPT TEMPLATE")
    print("=" * 60)
    print("""
Each agent should receive a batch JSON file and produce output in this format:

[{
  "filename": "2024-Author-Title.md",
  "LLM_assessed": "GPT-4, Llama-3, Claude",
  "DATA_URL": "https://github.com/...",
  "data_description": "Benchmark for evaluating...",
  "is_benchmark": "Yes",
  "is_eval": "Yes",
  "is_dataset": "No",
  "confidence": "high",
  "notes": "Changed LLM_assessed: removed BERT (only cited, not tested)"
}]

Key instructions for agents:
1. LLM_assessed: Only models the paper ACTUALLY tests/evaluates/benchmarks
   (not merely cited in related work). Use ONLY canonical names.
2. is_benchmark: Paper introduces a named benchmark or systematically
   compares models on a standardized test
3. is_eval: Paper evaluates model outputs using metrics, human judgment,
   or automated scoring
4. is_dataset: Paper releases a new dataset or constructs a novel
   data collection
5. DATA_URL: URL to actual dataset/benchmark resource (GitHub, HuggingFace,
   Zenodo, etc.), not just the paper URL
6. confidence: "high" if PDF extract was available and clear,
   "medium" if some ambiguity, "low" if abstract-only or unclear
""")
    print("=" * 60)
    print("\nDone.")


if __name__ == "__main__":
    main()
