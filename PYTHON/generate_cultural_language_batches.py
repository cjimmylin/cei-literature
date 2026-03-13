#!/usr/bin/env python3
"""
Generate batch files for LLM-based cultural & language reclassification.

Scans all papers, records current values of national_ethnic_cultural,
cultures_nationalities_list, and languages_list for audit, resolves PDF
extract paths, and splits into balanced batches for parallel agent processing.

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/generate_cultural_language_batches.py
    ../.venv/bin/python PYTHON/generate_cultural_language_batches.py --pilot 50
    ../.venv/bin/python PYTHON/generate_cultural_language_batches.py --num-batches 10

Output:
    logs/YYYYMMDD-cultural_language_batch_01.json through batch_NN.json
    logs/YYYYMMDD-cultural_language_manifest.json
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
    # Use iterdir() instead of rglob() — rglob breaks on [ ] in filenames
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


def get_abstract(fm_text, body):
    """Extract abstract from YAML field or body section."""
    fields = parse_frontmatter(fm_text)
    abstract = fields.get("abstract", "").strip("\"'")
    if abstract and len(abstract) > 50:
        return abstract

    # Try body section
    import re
    match = re.search(r'## Abstract\s*\n\n(.*?)(?=\n## |\Z)', body, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""


def main():
    parser = argparse.ArgumentParser(
        description="Generate cultural & language reclassification batches")
    parser.add_argument("--pilot", type=int, default=0,
                        help="Pilot mode: process only N papers (default: all)")
    parser.add_argument("--num-batches", type=int, default=0,
                        help="Number of batches (default: auto — 5 for pilot, 20 for full)")
    args = parser.parse_args()

    # Collect all papers
    papers = []
    errors = 0
    cultural_counts = {}
    language_counts = {}

    for paper_path in sorted(PAPERS_DIR.glob("*.md")):
        try:
            content = paper_path.read_text(encoding="utf-8")
        except Exception as e:
            print("ERROR: Cannot read {}: {}".format(paper_path.name, e))
            errors += 1
            continue

        try:
            fm_text, body = extract_frontmatter(content)
        except ValueError:
            print("WARN: Bad frontmatter: {}".format(paper_path.name))
            errors += 1
            continue

        fields = parse_frontmatter(fm_text)
        current_nec = fields.get("national_ethnic_cultural", "").strip("\"'")
        current_cnl = fields.get("cultures_nationalities_list", "").strip("\"'")
        current_lang = fields.get("languages_list", "").strip("\"'")

        # Track distribution of current values
        nec_key = current_nec if current_nec else "(empty)"
        cultural_counts[nec_key] = cultural_counts.get(nec_key, 0) + 1

        lang_key = current_lang if current_lang else "(empty)"
        language_counts[lang_key] = language_counts.get(lang_key, 0) + 1

        extract_ref = resolve_extract_path(paper_path, fm_text)
        abstract = get_abstract(fm_text, body)

        papers.append({
            "filename": paper_path.name,
            "pdf_extract_path": extract_ref or "",
            "has_extract": extract_ref is not None,
            "has_abstract": len(abstract) > 50,
            "current_national_ethnic_cultural": current_nec,
            "current_cultures_nationalities_list": current_cnl,
            "current_languages_list": current_lang,
        })

    print("=== CULTURAL & LANGUAGE BATCH GENERATION ===\n")
    print("Total papers scanned: {}".format(len(papers) + errors))
    print("  Valid papers: {}".format(len(papers)))
    print("  Errors (bad frontmatter): {}".format(errors))
    print("  With PDF extract: {}".format(sum(1 for p in papers if p["has_extract"])))
    print("  Without PDF extract: {}".format(
        sum(1 for p in papers if not p["has_extract"])))
    print("  With abstract: {}".format(sum(1 for p in papers if p["has_abstract"])))

    print("\nCurrent national_ethnic_cultural distribution:")
    for cat, count in sorted(cultural_counts.items(), key=lambda x: -x[1]):
        print("  {}: {}".format(cat, count))

    print("\nCurrent languages_list distribution (top 20):")
    for i, (lang, count) in enumerate(
            sorted(language_counts.items(), key=lambda x: -x[1])):
        if i >= 20:
            remaining = len(language_counts) - 20
            print("  ... and {} more unique values".format(remaining))
            break
        print("  {}: {}".format(lang, count))

    if not papers:
        print("\nNo papers found. Exiting.")
        return

    # Apply pilot limit
    if args.pilot > 0:
        # Select a mix: prioritize papers WITH extracts, include some without
        with_extract = [p for p in papers if p["has_extract"]]
        without_extract = [p for p in papers if not p["has_extract"]]

        pilot_with = min(len(with_extract),
                         max(0, args.pilot - min(5, len(without_extract))))
        pilot_without = min(len(without_extract), args.pilot - pilot_with)

        papers = with_extract[:pilot_with] + without_extract[:pilot_without]
        print("\nPILOT MODE: Selected {} papers ({} with extract, {} without)".format(
            len(papers), pilot_with, pilot_without))

    # Determine number of batches
    if args.num_batches > 0:
        num_batches = args.num_batches
    elif args.pilot > 0:
        num_batches = 5
    else:
        num_batches = 20

    # Calculate batch sizes (balanced distribution)
    base_size = len(papers) // num_batches
    remainder = len(papers) % num_batches
    batch_sizes = [base_size + (1 if i < remainder else 0)
                   for i in range(num_batches)]

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

        out_name = "{}-cultural_language_batch_{:02d}.json".format(
            DATE_PREFIX, batch_num)
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
        "current_cultural_distribution": cultural_counts,
        "current_language_distribution": language_counts,
    }
    manifest_path = LOGS_DIR / "{}-cultural_language_manifest.json".format(
        DATE_PREFIX)
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print("\nManifest: {}".format(manifest_path.name))
    print("\n=== DONE ===")


if __name__ == "__main__":
    main()
