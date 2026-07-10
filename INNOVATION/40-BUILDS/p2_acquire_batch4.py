#!/usr/bin/env python3
"""
P2 Batch-4 Paper Acquisition Script — Lane A
Acquires 6 P2 papers (Value Formation gap groups) from INNOVATION gap table.
Date: 2026-07-10

Reuses p1_acquire.py functions; does NOT modify that file.
Adds mandatory 5-second inter-download sleep (multiple agents share IP).
"""

import sys
import time
import json
from pathlib import Path
from datetime import datetime

# Ensure p1_acquire functions are importable
sys.path.insert(0, str(Path(__file__).parent))
from p1_acquire import (
    fetch_arxiv_metadata,
    download_pdf,
    extract_pdf,
    make_paper_record,
    PDFS_DIR,
    PAPERS_DIR,
    EXTRACTS_DIR,
    LOG_DIR,
)

# -----------------------------------------------------------------------
# Batch-4 papers (Lane A — 6 items)
# -----------------------------------------------------------------------
P2_BATCH4 = [
    {
        "id": "P2-B4-01",
        "title": "Convergent Linear Representations of Emergent Misalignment",
        "author_year": "2025",
        "arxiv_id": "2506.11618",
        "gap": "G-20",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-B4-02",
        "title": "Model Organisms for Emergent Misalignment",
        "author_year": "2025",
        "arxiv_id": "2506.11613",
        "gap": "G-20",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-B4-03",
        "title": "Open Character Training",
        "author_year": "2025",
        "arxiv_id": "2511.01689",
        "gap": "G-22",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-B4-04",
        "title": "Emergent-misalignment prompt-sensitivity critique",
        "author_year": "2025",
        "arxiv_id": "2507.06253",
        "gap": "G-20",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-B4-05",
        "title": "Devil in the Details (format confounds)",
        "author_year": "2025",
        "arxiv_id": "2511.20104",
        "gap": "G-20",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-B4-06",
        "title": "Assistant Axis",
        "author_year": "2026",
        "arxiv_id": "2601.10387",
        "gap": "G-20",
        "warn": True,   # ⚠ verify-first: mismatch = MISS
        "priority": "P2",
    },
]

# Keywords that indicate G-20/G-22 relevance for non-warned items
EXPECTED_TOPIC_HINTS = {
    "2506.11618": ["emergent misalignment", "linear representations", "representation"],
    "2506.11613": ["emergent misalignment", "model organism"],
    "2511.01689": ["character", "training", "values", "persona"],
    "2507.06253": ["emergent misalignment", "prompt", "sensitivity"],
    "2511.20104": ["format", "confound", "emergent misalignment", "devil"],
    "2601.10387": ["assistant", "axis"],
}


def title_plausible(arxiv_id, fetched_title, expected_title, is_warn):
    """
    Check whether the fetched title is plausibly related to the expected.
    For ⚠ items: any topical mismatch → MISS.
    For non-⚠ items: wildly different topic → MISS; abbreviation OK.
    Returns (ok: bool, note: str)
    """
    ft = fetched_title.lower()
    et = expected_title.lower()
    hints = EXPECTED_TOPIC_HINTS.get(arxiv_id, [])

    # Direct substring match (abbreviated title is fine)
    words = [w for w in et.split() if len(w) > 4]
    overlap = sum(1 for w in words if w in ft)
    frac = overlap / max(len(words), 1)

    # Hint match
    hint_match = any(h in ft for h in hints)

    if frac >= 0.4 or hint_match:
        return True, "title corresponds"

    if is_warn:
        return False, f"⚠ mismatch — fetched: '{fetched_title}'"

    # Non-warn: be slightly more lenient (abbreviated title), but wildly different = MISS
    return False, f"wildly different topic — fetched: '{fetched_title}'"


def process_paper_b4(paper):
    """Full pipeline with mandatory 5-second inter-download sleep."""
    arxiv_id = paper["arxiv_id"]
    gap = paper["gap"]
    is_warn = paper["warn"]

    log_entry = {
        "paper_id": paper["id"],
        "title": paper["title"],
        "gap": gap,
        "arxiv_id": arxiv_id,
        "warn": is_warn,
        "priority": paper["priority"],
    }

    print(f"\n[{paper['id']}] {paper['title'][:65]}")
    print(f"  arXiv: {arxiv_id} {'⚠ VERIFY-FIRST' if is_warn else ''}")

    # Step 1: Fetch metadata (mandatory)
    meta = fetch_arxiv_metadata(arxiv_id)
    if meta is None:
        log_entry["verify_result"] = "FAILED — could not fetch metadata"
        log_entry["outcome"] = "MISS"
        log_entry["miss_reason"] = "arXiv metadata fetch failed"
        return log_entry

    fetched_title = meta.get("title", "")
    log_entry["fetched_title"] = fetched_title
    log_entry["fetched_authors"] = "; ".join(meta.get("authors", [])[:3])
    log_entry["fetched_year"] = meta.get("year")

    print(f"  Fetched title: '{fetched_title}'")

    # Step 1b: Title plausibility check
    ok, note = title_plausible(arxiv_id, fetched_title, paper["title"], is_warn)
    log_entry["verify_result"] = note

    if not ok:
        print(f"  MISS: {note}")
        log_entry["outcome"] = "MISS"
        log_entry["miss_reason"] = note
        log_entry["downloaded"] = False
        return log_entry

    print(f"  Title check: {note}")

    # Use fetched metadata for file naming
    actual_year = meta.get("year") or int(paper["author_year"])
    authors = meta.get("authors", [])
    first_author_full = authors[0] if authors else "Unknown"
    # Extract surname (last word of first author)
    first_author_surname = first_author_full.strip().split()[-1]

    # Build short title from fetched title (≤6 words, title-case)
    title_words = fetched_title.replace(":", " ").split()
    short_title_parts = title_words[:6]
    short_title = " ".join(short_title_parts)
    # Remove trailing punctuation
    short_title = short_title.rstrip(".,;:")

    file_stem = f"{actual_year}-{first_author_surname}-{short_title}"
    # Truncate if very long
    if len(file_stem) > 120:
        file_stem = file_stem[:120]

    log_entry["file_stem"] = file_stem

    # Step 2: Download PDF (mandatory 5s sleep before each download)
    pdf_subdir = PDFS_DIR / str(actual_year)
    pdf_subdir.mkdir(parents=True, exist_ok=True)
    pdf_path = pdf_subdir / f"{file_stem}.pdf"

    if pdf_path.exists() and pdf_path.stat().st_size > 10000:
        print(f"  PDF already exists: {pdf_path.name}")
        pdf_downloaded = True
    else:
        print(f"  Sleeping 5s before download (multi-agent IP share)...")
        time.sleep(5)
        pdf_downloaded = download_pdf(arxiv_id, pdf_path)

    log_entry["downloaded"] = pdf_downloaded
    log_entry["pdf_path"] = str(pdf_path) if pdf_downloaded else ""

    if not pdf_downloaded:
        log_entry["outcome"] = "MISS"
        log_entry["miss_reason"] = "PDF download failed"
        return log_entry

    # Step 3: Extract text
    extract_subdir = EXTRACTS_DIR / str(actual_year)
    extract_subdir.mkdir(parents=True, exist_ok=True)
    extract_path = extract_subdir / f"{file_stem}.md"

    if extract_path.exists():
        print(f"  Extract already exists: {extract_path.name}")
        extracted = True
    else:
        extracted = extract_pdf(pdf_path, extract_path)

    log_entry["extracted"] = extracted
    log_entry["extract_path"] = str(extract_path) if extracted else ""

    # Step 4: Create paper record
    # Build a paper dict compatible with make_paper_record
    paper_compat = {
        "id": paper["id"],
        "arxiv_id": arxiv_id,
        "title": paper["title"],
        "year": actual_year,
        "gap": gap,
        "warn": is_warn,
        "file_stem": file_stem,
    }

    paper_path = PAPERS_DIR / f"{file_stem}.md"

    if paper_path.exists():
        print(f"  Paper record already exists: {paper_path.name}")
        log_entry["paper_created"] = False
        log_entry["paper_path"] = str(paper_path)
        log_entry["paper_note"] = "already existed"
    else:
        yaml_text = make_paper_record(
            paper_compat, meta,
            pdf_path if pdf_downloaded else None,
            extract_path if extracted else None,
        )
        with open(paper_path, "w", encoding="utf-8") as f:
            f.write(yaml_text)
        print(f"  Created paper record: {paper_path.name}")
        log_entry["paper_created"] = True
        log_entry["paper_path"] = str(paper_path)

    log_entry["outcome"] = "HIT"
    return log_entry


def write_batch4_log(results):
    """Write acquisition log to new dated file."""
    log_path = LOG_DIR / "20260710-p2-acquisition-log-batch4.md"

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    attempted = len(results)
    hits = sum(1 for r in results if r.get("outcome") == "HIT")
    misses = sum(1 for r in results if r.get("outcome") == "MISS")
    verified_warns = sum(
        1 for r in results
        if r.get("warn") and r.get("outcome") == "HIT"
    )

    lines = [
        f"# P2 Batch-4 Acquisition Log — {now}",
        "",
        "**Lane:** A (parallel session)",
        "**Papers:** 6 P2 items (Value Formation gap groups G-20/G-22)",
        "**Pipeline:** arXiv metadata verify → 5s sleep → PDF download → PyMuPDF extract → paper record",
        "",
        "## Summary",
        "",
        "| Metric | Count |",
        "|--------|-------|",
        f"| Attempted | {attempted} |",
        f"| HITs | {hits} |",
        f"| MISSes | {misses} |",
        f"| ⚠ Verified (warn) | {verified_warns} / {sum(1 for r in results if r.get('warn'))} |",
        "",
        "## Per-Paper Results",
        "",
        "| ID | Expected Title | arXiv ID | Fetched Title | ⚠ | Outcome | Paper Record |",
        "|----|---------------|---------|--------------|---|---------|-------------|",
    ]

    for r in results:
        pid = r.get("paper_id", "")
        expected = r.get("title", "")[:40]
        arxiv = r.get("arxiv_id", "")
        fetched = r.get("fetched_title", "N/A")[:40]
        warn_flag = "⚠" if r.get("warn") else ""
        outcome = r.get("outcome", "?")
        paper_path = r.get("paper_path", "")
        paper_fname = Path(paper_path).name if paper_path else ""
        lines.append(
            f"| {pid} | {expected} | {arxiv} | {fetched} | {warn_flag} | {outcome} | {paper_fname} |"
        )

    lines += [
        "",
        "## HIT Detail",
        "",
    ]
    for r in results:
        if r.get("outcome") == "HIT":
            lines.append(f"### {r['paper_id']} — {r.get('fetched_title', '')}")
            lines.append(f"- **arXiv:** {r['arxiv_id']}")
            lines.append(f"- **Gap:** {r['gap']}")
            lines.append(f"- **Year:** {r.get('fetched_year', '?')}")
            lines.append(f"- **Authors:** {r.get('fetched_authors', '')}")
            lines.append(f"- **Verify:** {r.get('verify_result', '')}")
            lines.append(f"- **PDF:** `{r.get('pdf_path', '')}`")
            lines.append(f"- **Extract:** `{r.get('extract_path', '')}`")
            lines.append(f"- **Paper:** `{r.get('paper_path', '')}`")
            lines.append("")

    lines += [
        "## MISS Detail",
        "",
    ]
    for r in results:
        if r.get("outcome") == "MISS":
            lines.append(f"- **{r['paper_id']}** ({r.get('arxiv_id', '')}): {r.get('miss_reason', 'unknown')}")
            lines.append(f"  - Expected: '{r.get('title', '')}'")
            lines.append(f"  - Fetched: '{r.get('fetched_title', 'N/A')}'")
            lines.append(f"  - Verify note: {r.get('verify_result', '')}")

    content = "\n".join(lines) + "\n"
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\nAcquisition log written: {log_path}")
    return log_path


def main():
    print("=" * 65)
    print("P2 Batch-4 Acquisition — Lane A — 2026-07-10")
    print("=" * 65)

    results = []

    for i, paper in enumerate(P2_BATCH4):
        log_entry = {}
        try:
            log_entry = process_paper_b4(paper)
        except Exception as e:
            print(f"  UNEXPECTED ERROR for {paper['id']}: {e}")
            log_entry = {
                "paper_id": paper["id"],
                "title": paper["title"],
                "gap": paper["gap"],
                "arxiv_id": paper["arxiv_id"],
                "warn": paper["warn"],
                "outcome": "MISS",
                "miss_reason": f"Unexpected error: {e}",
                "downloaded": False,
            }
        results.append(log_entry)

        # Mandatory 5-second inter-paper delay (separate from download sleep)
        if i < len(P2_BATCH4) - 1:
            print(f"  Inter-paper sleep 5s...")
            time.sleep(5)

    # Summary
    print("\n" + "=" * 65)
    print("BATCH-4 SUMMARY")
    print("=" * 65)
    hits = [r for r in results if r.get("outcome") == "HIT"]
    misses = [r for r in results if r.get("outcome") == "MISS"]
    print(f"Attempted: {len(results)}")
    print(f"HITs: {len(hits)}")
    print(f"MISSes: {len(misses)}")
    for r in misses:
        print(f"  MISS [{r['paper_id']}]: {r.get('miss_reason', 'unknown')}")

    log_path = write_batch4_log(results)

    json_path = LOG_DIR / "20260710-p2-acquisition-results-batch4.json"
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"Raw results: {json_path}")

    return len(hits), len(misses)


if __name__ == "__main__":
    main()
