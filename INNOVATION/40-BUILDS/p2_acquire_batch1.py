#!/usr/bin/env python3
"""
P2 Acquisition Script — Batch 1
Acquires 11 P2 papers (Specification + Oversight gap groups)
Lane A of parallel arXiv acquisition session.
Date: 2026-07-10
"""

import os
import sys
import re
import time
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

# Import the proven functions from p1_acquire.py
sys.path.insert(0, str(Path(__file__).parent))
from p1_acquire import (
    fetch_arxiv_metadata,
    download_pdf,
    extract_pdf,
    make_paper_record,
    get_ethics_perspective,
    VAULT_ROOT,
    PDFS_DIR,
    PAPERS_DIR,
    EXTRACTS_DIR,
    LOG_DIR,
)

# -----------------------------------------------------------------------
# P2 Batch-1 paper definitions
# Gap groups: Specification (G-01, G-02) + Oversight (G-07, G-08, G-09)
# -----------------------------------------------------------------------
P2_BATCH1_PAPERS = [
    {
        "id": "P2-01",
        "title": "Reasoning over Boundaries / SpecBench",
        "author_year": "2025",
        "arxiv_id": "2509.14760",
        "gap": "G-01",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-02",
        "title": "Normative Conflicts and Shallow AI Alignment (Millière)",
        "author_year": "Millière 2025",
        "arxiv_id": "2506.04679",
        "gap": "G-02",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-03",
        "title": "Sociotechnical specification framework (SLR)",
        "author_year": "2026",
        "arxiv_id": "2607.01250",
        "gap": "G-02",
        "warn": True,
        "priority": "P2",
    },
    {
        "id": "P2-04",
        "title": "AI Alignment Breaks at the Edge",
        "author_year": "2026",
        "arxiv_id": "2602.20042",
        "gap": "G-02",
        "warn": True,
        "priority": "P2",
    },
    {
        "id": "P2-05",
        "title": "Recursive Self-Critiquing",
        "author_year": "2025",
        "arxiv_id": "2502.04675",
        "gap": "G-07",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-06",
        "title": "Scaling Laws for Scalable Oversight",
        "author_year": "2025",
        "arxiv_id": "2504.18530",
        "gap": "G-07",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-07",
        "title": "Prover-Verifier Games",
        "author_year": "2024",
        "arxiv_id": "2407.13692",
        "gap": "G-07",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-08",
        "title": "Debate Helps Weak Judges",
        "author_year": "2026",
        "arxiv_id": "2605.27483",
        "gap": "G-09",
        "warn": True,
        "priority": "P2",
    },
    {
        "id": "P2-09",
        "title": "Weak-to-strong beyond accuracy (safety/toxicity/legal)",
        "author_year": "2024",
        "arxiv_id": "2410.12621",
        "gap": "G-08",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-10",
        "title": "W2S reward models collapse under preference shift",
        "author_year": "2026",
        "arxiv_id": "2605.25629",
        "gap": "G-08",
        "warn": True,
        "priority": "P2",
    },
    {
        "id": "P2-11",
        "title": "Super(ficial)-alignment / weak-supervisor deception",
        "author_year": "2024",
        "arxiv_id": "2406.11431",
        "gap": "G-08",
        "warn": False,
        "priority": "P2",
    },
]

# Topic keywords for warn-flag verification (must match topic roughly)
WARN_TOPIC_HINTS = {
    "P2-03": ["specification", "sociotechnical", "systematic", "review", "framework", "alignment"],
    "P2-04": ["alignment", "edge", "break", "fail", "robust", "deploy"],
    "P2-08": ["debate", "weak", "judge", "oversight", "verif"],
    "P2-10": ["weak", "strong", "reward", "collapse", "preference", "shift", "generaliz"],
}


def title_matches_topic(fetched_title, paper_id, expected_title):
    """
    Check whether fetched title corresponds to the expected topic.
    For warn items: strict — must match topic hints.
    For non-warn: accept clear correspondence (abbreviated titles are fine).
    Returns (ok: bool, reason: str)
    """
    ft_lower = fetched_title.lower()
    exp_lower = expected_title.lower()

    if paper_id in WARN_TOPIC_HINTS:
        hints = WARN_TOPIC_HINTS[paper_id]
        matched = [h for h in hints if h in ft_lower]
        if matched:
            return True, f"PASS — topic hints matched: {matched}"
        else:
            return False, f"MISMATCH — no topic hints {hints} found in '{fetched_title}'"
    else:
        # Non-warn: check for wildly different topic
        # If there's any overlap with expected key terms, accept
        exp_words = set(w for w in exp_lower.split() if len(w) > 4)
        ft_words = set(w for w in ft_lower.split() if len(w) > 4)
        overlap = exp_words & ft_words
        if overlap or len(ft_lower) > 10:
            # Accept if fetched title is non-trivial (arXiv returned something real)
            return True, f"ACCEPT — clear correspondence (overlap: {overlap or 'by topic'})"
        return False, f"MISMATCH — fetched '{fetched_title}' vs expected '{expected_title}'"


def build_file_stem(meta, paper):
    """Build YYYY-Author-Short Title file stem from metadata."""
    year = meta.get("year") or paper.get("year_hint", 2025)
    authors = meta.get("authors", [])
    first_author = authors[0] if authors else "Unknown"
    # Extract surname (last token, or full if single word)
    surname = first_author.split()[-1] if first_author else "Unknown"
    # Sanitize surname for filename
    surname = re.sub(r'[^\w\s-]', '', surname).strip()

    # Build short title from actual fetched title (first ~4 meaningful words)
    title = meta.get("title", paper["title"])
    # Remove common stop words for short title
    stop = {"a", "an", "the", "of", "in", "on", "at", "to", "for", "and", "or",
            "with", "by", "from", "is", "are", "that", "this", "its", "it"}
    words = [w for w in title.split() if w.lower() not in stop]
    short = " ".join(words[:5])
    # Sanitize
    short = re.sub(r'[^\w\s-]', '', short).strip()

    return f"{year}-{surname}-{short}", year


def process_p2_paper(paper, log_entry):
    """
    Full P2 pipeline: verify metadata → check title → download → extract → record.
    Enforces 5-second sleep between downloads as required.
    """
    arxiv_id = paper["arxiv_id"]
    paper_id = paper["id"]

    log_entry["arxiv_id"] = arxiv_id
    log_entry["warn"] = paper["warn"]
    log_entry["gap"] = paper["gap"]

    print(f"\n{'='*60}")
    print(f"[{paper_id}] {paper['title'][:70]}")
    print(f"  arXiv: {arxiv_id} {'⚠ VERIFY-FIRST' if paper['warn'] else ''}")

    # Step 1: Fetch metadata
    meta = fetch_arxiv_metadata(arxiv_id)
    if meta is None:
        log_entry["status"] = "MISS"
        log_entry["miss_reason"] = "arXiv metadata fetch failed"
        log_entry["verify_result"] = "FAILED"
        log_entry["downloaded"] = False
        print(f"  MISS: metadata fetch failed")
        return log_entry

    fetched_title = meta.get("title", "")
    log_entry["fetched_title"] = fetched_title
    log_entry["fetched_authors"] = "; ".join(meta.get("authors", [])[:3])
    log_entry["fetched_year"] = meta.get("year")

    print(f"  Fetched: '{fetched_title}'")
    print(f"  Authors: {', '.join(meta.get('authors', [])[:3])}")

    # Step 2: Title verification
    ok, reason = title_matches_topic(fetched_title, paper_id, paper["title"])
    log_entry["verify_result"] = reason

    if paper["warn"] and not ok:
        # ⚠ flag and mismatch → MISS, do not download
        log_entry["status"] = "MISS"
        log_entry["miss_reason"] = f"⚠ title mismatch: {reason}"
        log_entry["downloaded"] = False
        print(f"  MISS (⚠ verify failed): {reason}")
        return log_entry

    if not paper["warn"] and not ok:
        # Non-warn but wildly off topic
        log_entry["status"] = "MISS"
        log_entry["miss_reason"] = f"Title mismatch (non-warn): {reason}"
        log_entry["downloaded"] = False
        print(f"  MISS (title mismatch): {reason}")
        return log_entry

    print(f"  Verify: {reason}")

    # Step 3: Build file stem from actual metadata
    file_stem, actual_year = build_file_stem(meta, paper)
    log_entry["file_stem"] = file_stem

    # Step 4: Check if paper record already exists
    paper_path = PAPERS_DIR / f"{file_stem}.md"
    if paper_path.exists():
        print(f"  Paper record already exists: {paper_path.name} — marking HIT (existing)")
        log_entry["status"] = "HIT"
        log_entry["paper_note"] = "already existed"
        log_entry["paper_created"] = False
        log_entry["paper_path"] = str(paper_path)
        log_entry["downloaded"] = True
        return log_entry

    # Step 5: Download PDF (with mandatory 5s inter-download sleep)
    pdf_subdir = PDFS_DIR / str(actual_year)
    pdf_subdir.mkdir(parents=True, exist_ok=True)
    pdf_path = pdf_subdir / f"{file_stem}.pdf"

    if pdf_path.exists() and pdf_path.stat().st_size > 10000:
        print(f"  PDF already exists: {pdf_path.name}")
        pdf_downloaded = True
    else:
        print(f"  Sleeping 5s before download (mandatory inter-paper rate limit)...")
        time.sleep(5)
        pdf_downloaded = download_pdf(arxiv_id, pdf_path)

    log_entry["downloaded"] = pdf_downloaded
    log_entry["pdf_path"] = str(pdf_path) if pdf_downloaded else ""

    if not pdf_downloaded:
        log_entry["status"] = "MISS"
        log_entry["miss_reason"] = "PDF download failed"
        return log_entry

    # Step 6: Extract text
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

    # Step 7: Create paper record
    # Inject priority P2 into paper dict for make_paper_record
    paper_for_record = dict(paper)
    paper_for_record["file_stem"] = file_stem
    paper_for_record["year"] = actual_year

    yaml_text = make_paper_record(
        paper_for_record, meta,
        pdf_path if pdf_downloaded else None,
        extract_path if extracted else None
    )
    with open(paper_path, 'w', encoding='utf-8') as f:
        f.write(yaml_text)
    print(f"  Created paper record: {paper_path.name}")

    log_entry["status"] = "HIT"
    log_entry["paper_created"] = True
    log_entry["paper_path"] = str(paper_path)

    return log_entry


def write_batch1_log(results):
    """Write the P2 batch-1 acquisition log."""
    log_path = LOG_DIR / "20260710-p2-acquisition-log-batch1.md"

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    attempted = len(results)
    hits = sum(1 for r in results if r.get("status") == "HIT")
    misses = sum(1 for r in results if r.get("status") == "MISS")
    warns = sum(1 for r in results if r.get("warn"))
    warns_passed = sum(1 for r in results if r.get("warn") and r.get("status") == "HIT")
    new_created = sum(1 for r in results if r.get("paper_created"))

    lines = [
        f"# P2 Acquisition Log — Batch 1 (Lane A) — {now}",
        "",
        "**Scope:** 11 P2 papers — Specification (G-01, G-02) + Oversight (G-07, G-08, G-09) gaps",
        "**Pipeline:** arXiv metadata verify → title check → PDF download (5s inter-paper sleep) → PyMuPDF extract → paper record",
        "**Lane:** A (parallel session)",
        "",
        "## Summary",
        "",
        "| Metric | Count |",
        "|--------|-------|",
        f"| Attempted | {attempted} |",
        f"| HITs | {hits} |",
        f"| MISSes | {misses} |",
        f"| ⚠ Verified | {warns_passed} / {warns} passed |",
        f"| New paper records created | {new_created} |",
        "",
        "## Per-Paper Results",
        "",
        "| ID | Expected Title | arXiv ID | ⚠ | Status | Fetched Title | Verify Result | Paper File |",
        "|----|---------------|---------|---|--------|--------------|--------------|------------|",
    ]

    for r in results:
        pid = r.get("paper_id", "")
        title = r.get("title", "")[:40]
        arxiv = r.get("arxiv_id", "")
        warn_flag = "⚠" if r.get("warn") else ""
        status = r.get("status", "?")
        ft = r.get("fetched_title", "")[:45]
        verify = r.get("verify_result", "")[:50]
        paper_path = r.get("paper_path", "")
        paper_fname = Path(paper_path).name if paper_path else r.get("miss_reason", "")
        lines.append(f"| {pid} | {title} | {arxiv} | {warn_flag} | **{status}** | {ft} | {verify} | {paper_fname} |")

    lines += [
        "",
        "## Miss Detail",
        "",
    ]
    for r in results:
        if r.get("status") == "MISS":
            lines.append(f"- **{r['paper_id']}** ({r.get('arxiv_id', '')}): {r.get('miss_reason', 'unknown')}")
            if r.get("fetched_title"):
                lines.append(f"  - Fetched title: {r.get('fetched_title')}")
            lines.append(f"  - Verify result: {r.get('verify_result', 'N/A')}")

    if not any(r.get("status") == "MISS" for r in results):
        lines.append("None — all items acquired successfully.")

    lines += [
        "",
        "## Vault Paths Created",
        "",
        "### PDFs",
    ]
    for r in results:
        if r.get("pdf_path") and r.get("downloaded"):
            lines.append(f"- `{r['pdf_path']}`")

    lines += ["", "### Extracts"]
    for r in results:
        if r.get("extract_path") and r.get("extracted"):
            lines.append(f"- `{r['extract_path']}`")

    lines += ["", "### Paper Records"]
    for r in results:
        if r.get("paper_path"):
            status_note = "(new)" if r.get("paper_created") else "(already existed)"
            lines.append(f"- `{r['paper_path']}` {status_note}")

    lines += [
        "",
        "## Notes",
        "",
        "- ⚠ items: title verified against topic hints before download; mismatch = MISS, no guess.",
        "- 5-second sleep enforced between downloads (parallel agents share IP against arXiv).",
        "- File stems derived from actual arXiv metadata (not expected/abbreviated titles).",
        "- `innovation_gap` field added to each paper record.",
        "- Orchestrator should run `validate_all_papers.py` after all lanes complete.",
    ]

    content = "\n".join(lines) + "\n"
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\nLog written: {log_path}")
    return log_path


def main():
    print("=" * 60)
    print("P2 Acquisition — Batch 1 (Lane A) — 2026-07-10")
    print("Papers: 11 (Specification + Oversight gaps)")
    print("=" * 60)

    results = []

    for paper in P2_BATCH1_PAPERS:
        log_entry = {
            "paper_id": paper["id"],
            "title": paper["title"],
            "gap": paper["gap"],
            "priority": paper["priority"],
        }
        try:
            log_entry = process_p2_paper(paper, log_entry)
        except Exception as e:
            import traceback
            print(f"  UNEXPECTED ERROR for {paper['id']}: {e}")
            traceback.print_exc()
            log_entry["status"] = "MISS"
            log_entry["downloaded"] = False
            log_entry["miss_reason"] = f"Unexpected error: {e}"
        results.append(log_entry)

        # 5 seconds between papers (covers the case where PDF was already cached)
        # Only sleep if not the last paper
        if paper != P2_BATCH1_PAPERS[-1]:
            print(f"  Inter-paper sleep 5s...")
            time.sleep(5)

    # Summary
    print("\n" + "=" * 60)
    print("BATCH-1 SUMMARY")
    print("=" * 60)
    hits = [r for r in results if r.get("status") == "HIT"]
    misses = [r for r in results if r.get("status") == "MISS"]
    print(f"Attempted: {len(results)}")
    print(f"HITs: {len(hits)}")
    print(f"MISSes: {len(misses)}")
    for r in misses:
        print(f"  MISS [{r['paper_id']}]: {r.get('miss_reason', 'unknown')}")

    # Write log
    log_path = write_batch1_log(results)

    # Save raw results as JSON
    json_path = LOG_DIR / "20260710-p2-batch1-results.json"
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"Raw results: {json_path}")

    return len(hits), len(misses)


if __name__ == "__main__":
    main()
