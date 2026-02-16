#!/usr/bin/env python3
"""
Generate batch files for comprehensive LLM ethics benchmark/dataset/metrics survey.

Scans papers in the vault, extracts metadata and body richness
indicators, and splits into 20 balanced batches for parallel agent processing.

Usage:
  python generate_benchmark_survey_batches.py               # All papers
  python generate_benchmark_survey_batches.py --unsurveyed   # Only papers NOT in existing survey

Output: logs/benchmark_survey_batches/batch_01.json through batch_20.json
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))
from yaml_utils import extract_frontmatter, parse_frontmatter
from config import PAPERS_DIR, PDF_EXTRACTS_DIR, LOGS_DIR

NUM_BATCHES = 11


def load_surveyed_filenames():
    """Load filenames already covered by previous benchmark survey."""
    # Try the latest all_classifications JSON
    for prefix in ["20260216", "20260215", "20260208"]:
        path = LOGS_DIR / "{}-benchmark_survey_all_classifications.json".format(prefix)
        if path.exists():
            data = json.loads(path.read_text(encoding="utf-8"))
            filenames = {entry["filename"] for entry in data}
            print("Loaded {} already-surveyed papers from {}".format(len(filenames), path.name))
            return filenames
    return set()


def resolve_extract_path(paper_path, fm_text):
    """Resolve the PDF extract path for a paper, return relative path or None."""
    fields = parse_frontmatter(fm_text)
    extract_ref = fields.get("pdf_extract", "").strip("\"'")
    if extract_ref and extract_ref != "N/A":
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

    # Fallback: try flat directory
    candidate = PDF_EXTRACTS_DIR / "{}.md".format(stem)
    if candidate.exists():
        return "PDF Extracts/{}.md".format(stem)

    return None


def assess_body_richness(body):
    """Assess how rich the paper body text is based on sections present."""
    sections_found = 0
    for section in ["## Detailed Summary", "## Methods Summary",
                    "## Artifact Contributions", "## Results Summary"]:
        if section in body:
            sections_found += 1

    if sections_found >= 3:
        return "rich"
    elif sections_found >= 1:
        return "minimal"
    else:
        return "thin"


def main():
    parser = argparse.ArgumentParser(description="Generate benchmark survey batches")
    parser.add_argument("--unsurveyed", action="store_true",
                        help="Only include papers NOT in existing survey")
    args = parser.parse_args()

    surveyed = load_surveyed_filenames() if args.unsurveyed else set()

    papers = []

    for paper_path in sorted(PAPERS_DIR.glob("*.md")):
        if paper_path.name in surveyed:
            continue
        try:
            content = paper_path.read_text(encoding="utf-8")
        except Exception:
            continue

        try:
            fm_text, body = extract_frontmatter(content)
        except ValueError:
            print("WARN: Bad frontmatter: {}".format(paper_path.name))
            continue

        fields = parse_frontmatter(fm_text)
        extract_ref = resolve_extract_path(paper_path, fm_text)
        richness = assess_body_richness(body)

        papers.append({
            "filename": paper_path.name,
            "pdf_extract_path": extract_ref or "",
            "has_extract": extract_ref is not None,
            "authors": fields.get("authors", "Unknown"),
            "year": fields.get("year", "Unknown"),
            "doi": fields.get("doi", ""),
            "url": fields.get("url", "").strip("\"'"),
            "body_richness": richness,
        })

    print("Total papers found: {}".format(len(papers)))
    print("  With PDF extract: {}".format(sum(1 for p in papers if p["has_extract"])))
    print("  Without PDF extract: {}".format(sum(1 for p in papers if not p["has_extract"])))
    print("  Body richness: rich={}, minimal={}, thin={}".format(
        sum(1 for p in papers if p["body_richness"] == "rich"),
        sum(1 for p in papers if p["body_richness"] == "minimal"),
        sum(1 for p in papers if p["body_richness"] == "thin"),
    ))

    # Split into 20 batches
    batches_dir = LOGS_DIR / "benchmark_survey_round3_batches"
    batches_dir.mkdir(parents=True, exist_ok=True)

    base_size = len(papers) // NUM_BATCHES
    remainder = len(papers) % NUM_BATCHES
    # First `remainder` batches get base_size+1, rest get base_size
    batch_sizes = [base_size + 1] * remainder + [base_size] * (NUM_BATCHES - remainder)

    assert sum(batch_sizes) == len(papers), "Batch sizes don't sum to total papers"

    idx = 0
    for batch_num, size in enumerate(batch_sizes, 1):
        batch = papers[idx:idx + size]
        idx += size

        out_path = batches_dir / "batch_{:02d}.json".format(batch_num)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(batch, f, indent=2, ensure_ascii=False)

        print("  Batch {:02d}: {} papers -> {}".format(batch_num, len(batch), out_path.name))

    print("\n{} batch files written to: {}".format(NUM_BATCHES, batches_dir))


if __name__ == "__main__":
    main()
