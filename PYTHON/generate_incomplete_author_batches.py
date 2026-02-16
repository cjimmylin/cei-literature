#!/usr/bin/env python3
"""
Generate batch files for incomplete author resolution (parallel execution).

Scans all papers with authors_incomplete: true and splits into batches
for parallel resolve_incomplete_authors.py invocations.

Includes ACL Anthology DOI derivation: if a paper's URL matches
aclanthology.org/XXXX-YYYY/, derives DOI 10.18653/v1/XXXX-YYYY to
unlock CrossRef lookups for papers that previously had no DOI.

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/generate_incomplete_author_batches.py
    ../.venv/bin/python PYTHON/generate_incomplete_author_batches.py --num-batches 5

Output:
    logs/YYYYMMDD-incomplete_author_batch_01.json through batch_NN.json
    logs/YYYYMMDD-incomplete_author_manifest.json
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


def derive_acl_doi(url):
    """
    Derive DOI from ACL Anthology URL.
    e.g. https://aclanthology.org/2023.acl-long.100/ -> 10.18653/v1/2023.acl-long.100
    """
    if not url:
        return ""
    m = re.search(r'aclanthology\.org/([A-Za-z0-9.\-]+)/?', url)
    if m:
        acl_id = m.group(1)
        return f"10.18653/v1/{acl_id}"
    return ""


def resolve_extract_path(paper_path):
    """Find PDF extract path for a paper."""
    stem = paper_path.stem
    for subdir in PDF_EXTRACTS_DIR.iterdir():
        if subdir.is_dir():
            candidate = subdir / f"{stem}.md"
            if candidate.exists():
                return f"PDF Extracts/{subdir.name}/{candidate.name}"
    candidate = PDF_EXTRACTS_DIR / f"{stem}.md"
    if candidate.exists():
        return f"PDF Extracts/{stem}.md"
    return ""


def main():
    parser = argparse.ArgumentParser(description="Generate incomplete author resolution batches")
    parser.add_argument("--num-batches", type=int, default=7,
                        help="Number of batches (default: 7)")
    args = parser.parse_args()

    # Collect all papers with authors_incomplete: true
    papers = []
    total_scanned = 0

    for paper_path in sorted(PAPERS_DIR.glob("*.md")):
        total_scanned += 1
        try:
            content = paper_path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"ERROR: Cannot read {paper_path.name}: {e}")
            continue

        if "authors_incomplete: true" not in content:
            continue

        try:
            fm_text, body = extract_frontmatter(content)
        except ValueError:
            print(f"WARN: Bad frontmatter: {paper_path.name}")
            continue

        fields = parse_frontmatter(fm_text)
        title = fields.get("short_title", "").strip("\"'").strip()
        first_author = fields.get("first_author", "").strip("\"'").strip()
        doi = fields.get("doi", "").strip("\"'").strip()
        url = fields.get("url", "").strip("\"'").strip()
        external_pdf = fields.get("external_pdf", "").strip("\"'").strip()
        extract_path = resolve_extract_path(paper_path)

        # Derive ACL Anthology DOI if applicable
        acl_doi = derive_acl_doi(url)
        if not acl_doi:
            acl_doi = derive_acl_doi(external_pdf)

        papers.append({
            "filename": paper_path.name,
            "short_title": title or paper_path.stem,
            "first_author": first_author,
            "doi": doi,
            "url": url,
            "external_pdf": external_pdf,
            "pdf_extract_path": extract_path,
            "acl_derived_doi": acl_doi,
        })

    print("=== INCOMPLETE AUTHOR BATCH GENERATION ===\n")
    print(f"Total papers scanned: {total_scanned}")
    print(f"Papers with authors_incomplete: true: {len(papers)}")
    acl_count = sum(1 for p in papers if p["acl_derived_doi"])
    print(f"Papers with ACL-derived DOI: {acl_count}")

    if not papers:
        print("\nNo papers need processing. Exiting.")
        return

    # Determine number of batches
    num_batches = min(args.num_batches, len(papers))

    # Calculate batch sizes
    base_size = len(papers) // num_batches
    remainder = len(papers) % num_batches
    batch_sizes = [base_size + (1 if i < remainder else 0) for i in range(num_batches)]
    batch_sizes = [s for s in batch_sizes if s > 0]
    num_batches = len(batch_sizes)

    print(f"\nSplitting {len(papers)} papers into {num_batches} batches")

    # Write batch files
    idx = 0
    batch_files = []
    for batch_num, size in enumerate(batch_sizes, 1):
        batch = papers[idx:idx + size]
        idx += size

        out_name = f"{DATE_PREFIX}-incomplete_author_batch_{batch_num:02d}.json"
        out_path = LOGS_DIR / out_name
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(batch, f, indent=2, ensure_ascii=False)

        batch_files.append(out_name)
        acl_in_batch = sum(1 for p in batch if p["acl_derived_doi"])
        print(f"  Batch {batch_num:02d}: {len(batch)} papers ({acl_in_batch} with ACL DOI) -> {out_name}")

    # Write manifest
    manifest = {
        "date": DATE_PREFIX,
        "total_papers": len(papers),
        "num_batches": num_batches,
        "batch_files": batch_files,
        "papers_with_acl_doi": acl_count,
    }
    manifest_path = LOGS_DIR / f"{DATE_PREFIX}-incomplete_author_manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"\nManifest: {manifest_path.name}")
    print("\n=== DONE ===")


if __name__ == "__main__":
    main()
