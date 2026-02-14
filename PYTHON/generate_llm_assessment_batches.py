#!/usr/bin/env python3
"""
Generate batch files for LLM assessment & data description enrichment.

Scans all papers, filters those missing the LLM_assessed field, resolves
PDF extract paths, and splits into balanced batches for parallel agent processing.

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/generate_llm_assessment_batches.py
    ../.venv/bin/python PYTHON/generate_llm_assessment_batches.py --pilot 50

Output:
    logs/YYYYMMDD-llm_assessment_batch_01.json through batch_NN.json
"""

import argparse
import functools
import json
import sys
from datetime import datetime
from pathlib import Path

print = functools.partial(print, flush=True)

sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))
from yaml_utils import extract_frontmatter, parse_frontmatter
from config import PAPERS_DIR, PDF_EXTRACTS_DIR, LOGS_DIR

DATE_PREFIX = datetime.now().strftime("%Y%m%d")


def resolve_extract_path(paper_path, fm_text):
    """Resolve the PDF extract path for a paper, return relative path or None."""
    fields = parse_frontmatter(fm_text)
    extract_ref = fields.get("pdf_extract", "").strip("\"'")
    if extract_ref:
        extract_path = PAPERS_DIR.parent / extract_ref
        if extract_path.exists():
            return extract_ref

    # Fallback: try matching filename in year-based subdirs
    stem = paper_path.stem
    for subdir in PDF_EXTRACTS_DIR.iterdir():
        if subdir.is_dir():
            candidate = subdir / "{}.md".format(stem)
            if candidate.exists():
                return "PDF Extracts/{}/{}".format(subdir.name, candidate.name)

    # Fallback: try root of PDF Extracts
    candidate = PDF_EXTRACTS_DIR / "{}.md".format(stem)
    if candidate.exists():
        return "PDF Extracts/{}.md".format(stem)

    return None


def has_llm_assessed(fm_text):
    """Check if the paper already has a non-empty LLM_assessed field."""
    fields = parse_frontmatter(fm_text)
    return bool(fields.get("LLM_assessed", "").strip())


def main():
    parser = argparse.ArgumentParser(description="Generate LLM assessment batches")
    parser.add_argument("--pilot", type=int, default=0,
                        help="Pilot mode: process only N papers (default: all)")
    parser.add_argument("--num-batches", type=int, default=0,
                        help="Number of batches (default: auto — 10 for pilot, 20 for full)")
    parser.add_argument("--keys", type=str, default="",
                        help="Filter by LSRC key range, e.g. LSRC0428:LSRC0551")
    args = parser.parse_args()

    # Parse key range filter
    key_start = key_end = None
    if args.keys:
        parts = args.keys.split(":")
        if len(parts) == 2:
            key_start, key_end = parts[0].strip(), parts[1].strip()
            print("Key filter: {} to {}".format(key_start, key_end))
        else:
            print("ERROR: --keys must be in format START:END (e.g. LSRC0428:LSRC0551)")
            sys.exit(1)

    # Collect all papers needing processing
    papers = []
    skipped = 0
    errors = 0

    for paper_path in sorted(PAPERS_DIR.glob("*.md")):
        try:
            content = paper_path.read_text(encoding="utf-8")
        except Exception as e:
            print("ERROR: Cannot read {}: {}".format(paper_path.name, e))
            errors += 1
            continue

        try:
            fm_text, _ = extract_frontmatter(content)
        except ValueError:
            print("WARN: Bad frontmatter: {}".format(paper_path.name))
            errors += 1
            continue

        # Skip papers already processed (idempotent)
        if has_llm_assessed(fm_text):
            skipped += 1
            continue

        # Apply key range filter if specified
        if key_start and key_end:
            fields = parse_frontmatter(fm_text)
            paper_key = fields.get("key", "").strip()
            if not paper_key or paper_key < key_start or paper_key > key_end:
                skipped += 1
                continue

        extract_ref = resolve_extract_path(paper_path, fm_text)
        papers.append({
            "filename": paper_path.name,
            "pdf_extract_path": extract_ref or "",
            "has_extract": extract_ref is not None,
        })

    total_in_vault = skipped + len(papers) + errors
    print("=== LLM ASSESSMENT BATCH GENERATION ===\n")
    print("Total papers in vault: {}".format(total_in_vault))
    print("  Already processed (has LLM_assessed): {}".format(skipped))
    print("  Needing processing: {}".format(len(papers)))
    print("  Errors (bad frontmatter): {}".format(errors))
    print("  With PDF extract: {}".format(sum(1 for p in papers if p["has_extract"])))
    print("  Without PDF extract: {}".format(sum(1 for p in papers if not p["has_extract"])))

    if not papers:
        print("\nNo papers need processing. Exiting.")
        return

    # Apply pilot limit
    if args.pilot > 0:
        # Select a mix: prioritize papers WITH extracts, include some without
        with_extract = [p for p in papers if p["has_extract"]]
        without_extract = [p for p in papers if not p["has_extract"]]

        pilot_with = min(len(with_extract), args.pilot - min(5, len(without_extract)))
        pilot_without = min(len(without_extract), args.pilot - pilot_with)

        papers = with_extract[:pilot_with] + without_extract[:pilot_without]
        print("\nPILOT MODE: Selected {} papers ({} with extract, {} without)".format(
            len(papers), pilot_with, pilot_without))

    # Determine number of batches
    if args.num_batches > 0:
        num_batches = args.num_batches
    elif args.pilot > 0:
        num_batches = 10
    else:
        num_batches = 20

    # Calculate batch sizes
    base_size = len(papers) // num_batches
    remainder = len(papers) % num_batches
    # First 'remainder' batches get base_size+1, rest get base_size
    batch_sizes = [base_size + (1 if i < remainder else 0) for i in range(num_batches)]

    # Remove empty trailing batches
    batch_sizes = [s for s in batch_sizes if s > 0]
    num_batches = len(batch_sizes)

    print("\nSplitting {} papers into {} batches".format(len(papers), num_batches))

    # Write batch files
    idx = 0
    batch_files = []
    for batch_num, size in enumerate(batch_sizes, 1):
        batch = papers[idx:idx + size]
        idx += size

        out_name = "{}-llm_assessment_batch_{:02d}.json".format(DATE_PREFIX, batch_num)
        out_path = LOGS_DIR / out_name
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(batch, f, indent=2, ensure_ascii=False)

        batch_files.append(out_name)
        has_count = sum(1 for p in batch if p["has_extract"])
        print("  Batch {:02d}: {} papers ({} with extract) -> {}".format(
            batch_num, len(batch), has_count, out_name))

    # Write manifest
    manifest = {
        "date": DATE_PREFIX,
        "total_papers": len(papers),
        "num_batches": num_batches,
        "pilot": args.pilot > 0,
        "batch_files": batch_files,
        "papers_with_extract": sum(1 for p in papers if p["has_extract"]),
        "papers_without_extract": sum(1 for p in papers if not p["has_extract"]),
    }
    manifest_path = LOGS_DIR / "{}-llm_assessment_manifest.json".format(DATE_PREFIX)
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print("\nManifest: {}".format(manifest_path.name))
    print("\n=== DONE ===")


if __name__ == "__main__":
    main()
