#!/usr/bin/env python3
"""
Generate batch files for languages_list enrichment.

Scans all papers, filters those missing the languages_list field (or blank),
includes culture hint fields, and splits into balanced batches
for parallel agent processing.

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/generate_language_list_batches.py
    ../.venv/bin/python PYTHON/generate_language_list_batches.py --pilot 50
    ../.venv/bin/python PYTHON/generate_language_list_batches.py --num-batches 10

Output:
    logs/YYYYMMDD-language_list_batch_01.json through batch_NN.json
    logs/YYYYMMDD-language_list_manifest.json
"""

import argparse
import functools
import json
import re
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
            candidate = subdir / f"{stem}.md"
            if candidate.exists():
                return f"PDF Extracts/{subdir.name}/{candidate.name}"

    # Fallback: try root of PDF Extracts
    candidate = PDF_EXTRACTS_DIR / f"{stem}.md"
    if candidate.exists():
        return f"PDF Extracts/{stem}.md"

    return None


def has_language_list(fm_text):
    """Check if the paper already has a non-empty languages_list field."""
    fields = parse_frontmatter(fm_text)
    value = fields.get("languages_list", "").strip()
    return bool(value)


def extract_abstract_snippet(fm_text, body, max_chars=500):
    """Extract abstract text from YAML field or body section."""
    fields = parse_frontmatter(fm_text)
    abstract = fields.get("abstract", "").strip("\"'").strip()
    if abstract and len(abstract) > 20:
        return abstract[:max_chars]

    # Try body ## Abstract section
    match = re.search(r'## Abstract\s*\n+(.*?)(\n## |\Z)', body, re.DOTALL)
    if match:
        text = match.group(1).strip()
        if text and text != '*(To be fetched)*':
            return text[:max_chars]

    return ""


def main():
    parser = argparse.ArgumentParser(description="Generate language list enrichment batches")
    parser.add_argument("--pilot", type=int, default=0,
                        help="Pilot mode: process only N papers (default: all)")
    parser.add_argument("--num-batches", type=int, default=20,
                        help="Number of batches (default: 20)")
    parser.add_argument("--since", type=str, default="",
                        help="Only include papers created on or after this date (YYYY-MM-DD)")
    args = parser.parse_args()

    # Parse --since date filter
    since_date = None
    if args.since:
        since_date = datetime.strptime(args.since, "%Y-%m-%d")
        print(f"Date filter: created on or after {args.since}")

    # Collect all papers needing processing
    papers = []
    skipped = 0
    errors = 0

    for paper_path in sorted(PAPERS_DIR.glob("*.md")):
        try:
            content = paper_path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"ERROR: Cannot read {paper_path.name}: {e}")
            errors += 1
            continue

        try:
            fm_text, body = extract_frontmatter(content)
        except ValueError:
            print(f"WARN: Bad frontmatter: {paper_path.name}")
            errors += 1
            continue

        # Skip papers already processed (idempotent)
        if has_language_list(fm_text):
            skipped += 1
            continue

        # Apply date filter if specified
        if since_date:
            try:
                created = datetime.fromtimestamp(paper_path.stat().st_birthtime)
                if created < since_date:
                    skipped += 1
                    continue
            except AttributeError:
                pass  # st_birthtime not available on all platforms

        fields = parse_frontmatter(fm_text)
        nat_ethnic = fields.get("national_ethnic_cultural", "").strip("\"'").strip()
        cultures_list = fields.get("cultures_nationalities_list", "").strip("\"'").strip()
        title = fields.get("short_title", "").strip("\"'").strip()
        if not title:
            title = paper_path.stem

        abstract_snippet = extract_abstract_snippet(fm_text, body)
        extract_ref = resolve_extract_path(paper_path, fm_text)

        papers.append({
            "filename": paper_path.name,
            "title": title,
            "national_ethnic_cultural": nat_ethnic,
            "cultures_nationalities_list": cultures_list,
            "abstract_snippet": abstract_snippet,
            "pdf_extract_path": extract_ref or "",
            "has_extract": extract_ref is not None,
        })

    total_in_vault = skipped + len(papers) + errors
    print("=== LANGUAGE LIST BATCH GENERATION ===\n")
    print(f"Total papers in vault: {total_in_vault}")
    print(f"  Already has languages_list: {skipped}")
    print(f"  Needing processing: {len(papers)}")
    print(f"  Errors (bad frontmatter): {errors}")
    print(f"  With PDF extract: {sum(1 for p in papers if p['has_extract'])}")
    print(f"  Without PDF extract: {sum(1 for p in papers if not p['has_extract'])}")

    if not papers:
        print("\nNo papers need processing. Exiting.")
        return

    # Apply pilot limit
    if args.pilot > 0:
        papers = papers[:args.pilot]
        print(f"\nPILOT MODE: Selected {len(papers)} papers")

    # Determine number of batches
    num_batches = args.num_batches
    if num_batches <= 0:
        num_batches = max(1, len(papers) // 65)
        if len(papers) % 65 > 0:
            num_batches += 1

    # Cap batches at paper count
    num_batches = min(num_batches, len(papers))

    # Calculate batch sizes
    base_size = len(papers) // num_batches
    remainder = len(papers) % num_batches
    batch_sizes = [base_size + (1 if i < remainder else 0) for i in range(num_batches)]

    # Remove empty trailing batches
    batch_sizes = [s for s in batch_sizes if s > 0]
    num_batches = len(batch_sizes)

    print(f"\nSplitting {len(papers)} papers into {num_batches} batches")

    # Write batch files
    idx = 0
    batch_files = []
    for batch_num, size in enumerate(batch_sizes, 1):
        batch = papers[idx:idx + size]
        idx += size

        out_name = f"{DATE_PREFIX}-language_list_batch_{batch_num:02d}.json"
        out_path = LOGS_DIR / out_name
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(batch, f, indent=2, ensure_ascii=False)

        batch_files.append(out_name)
        has_count = sum(1 for p in batch if p["has_extract"])
        print(f"  Batch {batch_num:02d}: {len(batch)} papers ({has_count} with extract) -> {out_name}")

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
    manifest_path = LOGS_DIR / f"{DATE_PREFIX}-language_list_manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"\nManifest: {manifest_path.name}")
    print("\n=== DONE ===")


if __name__ == "__main__":
    main()
