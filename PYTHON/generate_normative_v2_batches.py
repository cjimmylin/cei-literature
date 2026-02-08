#!/usr/bin/env python3
"""
Generate batch files for normative ethics v2 deep-read classification.

Scans all 266 EXSR papers, resolves PDF extract paths, and splits into
10 balanced batches for parallel agent processing.

Output: logs/normative_v2_batches/batch_01.json through batch_10.json
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))
from yaml_utils import extract_frontmatter, parse_frontmatter
from config import PAPERS_DIR, PDF_EXTRACTS_DIR, LOGS_DIR


def resolve_extract_path(paper_path, fm_text):
    """Resolve the PDF extract path for a paper, return relative path or None."""
    fields = parse_frontmatter(fm_text)
    extract_ref = fields.get("pdf_extract", "").strip("\"'")
    if extract_ref:
        extract_path = PAPERS_DIR.parent / extract_ref
        if extract_path.exists():
            return extract_ref

    # Fallback: try matching filename
    candidate = PDF_EXTRACTS_DIR / "{}.md".format(paper_path.stem)
    if candidate.exists():
        return "PDF Extracts/{}.md".format(paper_path.stem)

    return None


def main():
    # Collect all EXSR papers
    papers = []
    for paper_path in sorted(PAPERS_DIR.glob("*.md")):
        try:
            content = paper_path.read_text(encoding="utf-8")
        except Exception:
            continue

        if "key: EXSR" not in content:
            continue

        try:
            fm_text, _ = extract_frontmatter(content)
        except ValueError:
            print("WARN: Bad frontmatter: {}".format(paper_path.name))
            continue

        extract_ref = resolve_extract_path(paper_path, fm_text)
        papers.append({
            "filename": paper_path.name,
            "pdf_extract_path": extract_ref or "",
            "has_extract": extract_ref is not None,
        })

    print("Total EXSR papers found: {}".format(len(papers)))
    print("  With PDF extract: {}".format(sum(1 for p in papers if p["has_extract"])))
    print("  Without PDF extract: {}".format(sum(1 for p in papers if not p["has_extract"])))

    if len(papers) != 266:
        print("WARNING: Expected 266 papers, found {}".format(len(papers)))

    # Split into 10 batches: batches 1-6 get 27, batches 7-10 get 26
    batches_dir = LOGS_DIR / "normative_v2_batches"
    batches_dir.mkdir(parents=True, exist_ok=True)

    batch_sizes = [27] * 6 + [26] * 4  # 27*6 + 26*4 = 162 + 104 = 266
    idx = 0
    for batch_num, size in enumerate(batch_sizes, 1):
        batch = papers[idx:idx + size]
        idx += size

        out_path = batches_dir / "batch_{:02d}.json".format(batch_num)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(batch, f, indent=2, ensure_ascii=False)

        print("  Batch {:02d}: {} papers → {}".format(batch_num, len(batch), out_path.name))

    print("\nBatch files written to: {}".format(batches_dir))


if __name__ == "__main__":
    main()
