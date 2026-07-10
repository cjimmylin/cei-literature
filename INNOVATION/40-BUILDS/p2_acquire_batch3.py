#!/usr/bin/env python3
"""
P2 Batch-3 Paper Acquisition Script
Acquires 12 P2 papers (CoT/Eval-Validity + Agentic/Multi-Agent gap groups)
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

# Import reusable functions from p1_acquire
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
# P2 Batch-3 papers definition
# -----------------------------------------------------------------------
P2_BATCH3_PAPERS = [
    {
        "id": "P2-B3-01",
        "title": "Faithfulness + Verbosity decomposition",
        "author_year": "2025",
        "arxiv_id": "2510.27378",
        "gap": "G-13",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-B3-02",
        "title": "Pragmatic CoT monitorability",
        "author_year": "2025",
        "arxiv_id": "2510.23966",
        "gap": "G-13",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-B3-03",
        "title": "Obfuscated reasoning",
        "author_year": "2025",
        "arxiv_id": "2510.19851",
        "gap": "G-13",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-B3-04",
        "title": "Covert sandbagging vs CoT monitors",
        "author_year": "2025",
        "arxiv_id": "2508.00943",
        "gap": "G-13",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-B3-05",
        "title": "Alignment Faking in Large Language Models",
        "author_year": "2024",
        "arxiv_id": "2412.14093",
        "gap": "G-15",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-B3-06",
        "title": "Sleeper Agents",
        "author_year": "2024",
        "arxiv_id": "2401.05566",
        "gap": "G-15",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-B3-07",
        "title": "Emergent Social Conventions",
        "author_year": "2024",
        "arxiv_id": "2410.08948",
        "gap": "G-17",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-B3-08",
        "title": "Institutional AI / Cournot collusion",
        "author_year": "2026",
        "arxiv_id": "2601.11369",
        "gap": "G-17",
        "warn": True,   # ⚠ verify-first
        "priority": "P2",
    },
    {
        "id": "P2-B3-09",
        "title": "SCHEMEs coordinated sabotage",
        "author_year": "2026",
        "arxiv_id": "2605.29178",
        "gap": "G-17",
        "warn": True,   # ⚠ verify-first
        "priority": "P2",
    },
    {
        "id": "P2-B3-10",
        "title": "Sabotage Evaluations for Frontier Models",
        "author_year": "2024",
        "arxiv_id": "2410.21514",
        "gap": "G-16",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-B3-11",
        "title": "Agent-ValueBench",
        "author_year": "2025",
        "arxiv_id": "2605.10365",
        "gap": "G-18",
        "warn": True,   # ⚠ verify-first
        "priority": "P2",
    },
    {
        "id": "P2-B3-12",
        "title": "Insider-risk mitigations (66k-sample)",
        "author_year": "2025",
        "arxiv_id": "2510.05192",
        "gap": "G-16",
        "warn": False,
        "priority": "P2",
    },
]

# Expected-title keywords for rough matching (non-⚠ items — abbreviated titles need correspondence check)
EXPECTED_KEYWORDS = {
    "P2-B3-01": ["faithfulness", "verbosity"],
    "P2-B3-02": ["pragmatic", "cot", "monitorab"],
    "P2-B3-03": ["obfuscat", "reasoning"],
    "P2-B3-04": ["sandbagging", "cot", "monitor"],
    "P2-B3-05": ["alignment faking"],
    "P2-B3-06": ["sleeper"],
    "P2-B3-07": ["emergent", "social", "convention"],
    "P2-B3-10": ["sabotage", "evaluat"],
    "P2-B3-12": ["insider", "risk", "mitigation"],
}

# For ⚠ items, matching keywords that confirm correct paper
WARN_CONFIRM_KEYWORDS = {
    "P2-B3-08": ["cournot", "collusion", "institutional", "market", "competition"],
    "P2-B3-09": ["scheme", "sabotage", "coordinated", "agent"],
    "P2-B3-11": ["agent", "value", "bench", "benchmark"],
}


def title_matches_expected(paper_id, fetched_title):
    """Check if fetched title corresponds to expected topic (non-⚠ items)."""
    keywords = EXPECTED_KEYWORDS.get(paper_id, [])
    if not keywords:
        return True  # No check defined → accept
    title_lower = fetched_title.lower()
    return any(kw in title_lower for kw in keywords)


def warn_title_ok(paper_id, fetched_title):
    """Check if ⚠ item's fetched title matches any of the confirm keywords."""
    keywords = WARN_CONFIRM_KEYWORDS.get(paper_id, [])
    if not keywords:
        return False
    title_lower = fetched_title.lower()
    return any(kw in title_lower for kw in keywords)


def make_file_stem(meta, paper):
    """Build YYYY-FirstAuthor-Short Title stem from metadata."""
    year = meta.get("year") or paper.get("arxiv_id", "")[:2]
    authors = meta.get("authors", [])
    if authors:
        # Extract last name of first author
        first_auth = authors[0].strip()
        # Handle "Last, First" format
        if "," in first_auth:
            last_name = first_auth.split(",")[0].strip()
        else:
            parts = first_auth.split()
            last_name = parts[-1] if parts else "Unknown"
    else:
        last_name = "Unknown"

    # Build short title from actual fetched title (max ~5 words for key terms)
    title = meta.get("title", paper["title"])
    # Sanitize
    safe_title = re.sub(r'[<>:"/\\|?*]', '', title)
    # Use first ~50 chars as short title component
    short = safe_title[:55].rstrip()
    # Remove trailing punctuation
    short = short.rstrip(".,;:- ")

    return f"{year}-{last_name}-{short}"


def process_paper_b3(paper, log_entry):
    """Full pipeline for batch-3: verify → (⚠ check) → download → extract → record."""
    arxiv_id = paper["arxiv_id"]
    paper_id = paper["id"]

    log_entry["arxiv_id"] = arxiv_id
    log_entry["warn"] = paper["warn"]

    print(f"\n[{paper_id}] {paper['title'][:60]}")
    print(f"  arXiv: {arxiv_id} {'⚠ VERIFY' if paper['warn'] else ''}")

    # Step 1: Fetch metadata (always)
    meta = fetch_arxiv_metadata(arxiv_id)
    if meta is None:
        log_entry["verify_result"] = "FAILED — could not fetch metadata"
        log_entry["status"] = "MISS"
        log_entry["miss_reason"] = "arXiv metadata fetch failed"
        return log_entry

    fetched_title = meta.get("title", "")
    log_entry["fetched_title"] = fetched_title
    log_entry["fetched_authors"] = "; ".join(meta.get("authors", [])[:3])
    log_entry["fetched_year"] = meta.get("year")

    print(f"  Title: '{fetched_title}'")
    print(f"  Authors: {meta.get('authors', [])[:2]}")

    # Step 2: Title verification
    if paper["warn"]:
        # ⚠ items: strict check — mismatch = MISS, no guessing
        ok = warn_title_ok(paper_id, fetched_title)
        if ok:
            log_entry["verify_result"] = f"⚠ RESOLVED — '{fetched_title}' matches expected topic"
            print(f"  ⚠ RESOLVED: title matches expected keywords")
        else:
            log_entry["verify_result"] = f"⚠ MISMATCH — '{fetched_title}' does not match expected topic"
            log_entry["status"] = "MISS"
            log_entry["miss_reason"] = f"⚠ title mismatch: got '{fetched_title}'"
            print(f"  ⚠ MISMATCH: logging MISS, skipping download")
            return log_entry
    else:
        # Non-⚠ items: check rough correspondence
        if title_matches_expected(paper_id, fetched_title):
            log_entry["verify_result"] = f"OK — '{fetched_title}'"
            print(f"  Title check: PASS")
        else:
            # Wildly different topic
            log_entry["verify_result"] = f"TOPIC MISMATCH — '{fetched_title}'"
            log_entry["status"] = "MISS"
            log_entry["miss_reason"] = f"topic mismatch: got '{fetched_title}'"
            print(f"  Title check: FAIL (wildly different topic)")
            return log_entry

    # Build file stem from actual metadata
    actual_year = meta.get("year") or int(paper["arxiv_id"][:2]) + 2000
    file_stem = make_file_stem(meta, paper)

    log_entry["file_stem"] = file_stem

    # Step 3: Download PDF (5-second sleep between downloads as required)
    pdf_subdir = PDFS_DIR / str(actual_year)
    pdf_subdir.mkdir(parents=True, exist_ok=True)
    pdf_path = pdf_subdir / f"{file_stem}.pdf"

    if pdf_path.exists() and pdf_path.stat().st_size > 10000:
        print(f"  PDF already exists: {pdf_path.name}")
        pdf_downloaded = True
    else:
        print(f"  Sleeping 5s before download (rate-limit)...")
        time.sleep(5)
        pdf_downloaded = download_pdf(arxiv_id, pdf_path)

    log_entry["downloaded"] = pdf_downloaded
    log_entry["pdf_path"] = str(pdf_path) if pdf_downloaded else ""

    if not pdf_downloaded:
        log_entry["status"] = "MISS"
        log_entry["miss_reason"] = "PDF download failed"
        return log_entry

    # Step 4: Extract text
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

    # Step 5: Create paper record
    paper_path = PAPERS_DIR / f"{file_stem}.md"

    if paper_path.exists():
        print(f"  Paper record already exists: {paper_path.name}")
        log_entry["paper_created"] = False
        log_entry["paper_path"] = str(paper_path)
        log_entry["paper_note"] = "already existed"
    else:
        # Build a paper dict compatible with make_paper_record
        paper_compat = {
            "id": paper_id.replace("P2-B3-", "P2B3-"),
            "arxiv_id": arxiv_id,
            "title": paper["title"],
            "year": actual_year,
            "gap": paper["gap"],
            "priority": paper["priority"],
        }
        yaml_text = make_paper_record(
            paper_compat, meta,
            pdf_path if pdf_downloaded else None,
            extract_path if extracted else None
        )
        # Inject priority field after innovation_gap
        yaml_text = yaml_text.replace(
            f'innovation_gap: "{paper["gap"]}"',
            f'innovation_gap: "{paper["gap"]}"\npriority: "{paper["priority"]}"'
        )
        with open(paper_path, 'w', encoding='utf-8') as f:
            f.write(yaml_text)
        print(f"  Created paper record: {paper_path.name}")
        log_entry["paper_created"] = True
        log_entry["paper_path"] = str(paper_path)

    log_entry["status"] = "HIT"
    return log_entry


def write_batch3_log(results):
    """Write the batch-3 acquisition log."""
    log_path = LOG_DIR / "20260710-p2-acquisition-log-batch3.md"

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    attempted = len(results)
    hits = sum(1 for r in results if r.get("status") == "HIT")
    misses = sum(1 for r in results if r.get("status") == "MISS")
    warn_resolved = sum(1 for r in results if r.get("warn") and "RESOLVED" in r.get("verify_result", ""))
    warn_missed = sum(1 for r in results if r.get("warn") and "MISMATCH" in r.get("verify_result", ""))
    downloaded = sum(1 for r in results if r.get("downloaded"))
    extracted = sum(1 for r in results if r.get("extracted"))
    created = sum(1 for r in results if r.get("paper_created"))

    lines = [
        f"# P2 Batch-3 Acquisition Log — {now}",
        "",
        "**Lane:** A — CoT/Eval-Validity (G-13, G-15) + Agentic/Multi-Agent (G-16, G-17, G-18)",
        "**Papers:** 12 (9 non-⚠ + 3 ⚠ verify-first)",
        "**Pipeline:** arXiv metadata verify → title check → PDF download → PyMuPDF extract → paper record",
        "**Script:** `INNOVATION/40-BUILDS/p2_acquire_batch3.py`",
        "",
        "## Summary",
        "",
        "| Metric | Count |",
        "|--------|-------|",
        f"| Attempted | {attempted} |",
        f"| HITs | {hits} |",
        f"| MISSes | {misses} |",
        f"| ⚠ Verified (resolved) | {warn_resolved} |",
        f"| ⚠ Verified (mismatch → MISS) | {warn_missed} |",
        f"| Downloaded | {downloaded} |",
        f"| Extracted | {extracted} |",
        f"| Paper records created | {created} |",
        "",
        "## Per-Paper Results",
        "",
        "| ID | Expected Title | arXiv ID | Gap | ⚠ | Status | Fetched Title | Paper File |",
        "|----|---------------|---------|-----|---|--------|--------------|------------|",
    ]

    for r in results:
        pid = r.get("paper_id", "")
        exp_title = r.get("title", "")[:35]
        arxiv = r.get("arxiv_id", "")
        gap = r.get("gap", "")
        warn_flag = "⚠" if r.get("warn") else ""
        status = r.get("status", "?")
        fetched = r.get("fetched_title", "")[:45]
        paper_path = r.get("paper_path", "")
        paper_fname = Path(paper_path).name if paper_path else ""
        lines.append(f"| {pid} | {exp_title} | {arxiv} | {gap} | {warn_flag} | {status} | {fetched} | {paper_fname} |")

    lines += [
        "",
        "## Verification Details (⚠ Items)",
        "",
    ]
    for r in results:
        if r.get("warn"):
            lines.append(f"- **{r['paper_id']}** ({r.get('arxiv_id', '')}): {r.get('verify_result', 'N/A')}")

    lines += [
        "",
        "## Miss Details",
        "",
    ]
    for r in results:
        if r.get("status") == "MISS":
            lines.append(f"- **{r['paper_id']}** ({r.get('arxiv_id', '')}): {r.get('miss_reason', 'unknown')}")
            lines.append(f"  - Fetched title: {r.get('fetched_title', 'N/A')}")

    lines += [
        "",
        "## Vault Paths Created",
        "",
        "### PDFs",
    ]
    for r in results:
        if r.get("pdf_path"):
            lines.append(f"- `{r['pdf_path']}`")

    lines += ["", "### Extracts"]
    for r in results:
        if r.get("extract_path"):
            lines.append(f"- `{r['extract_path']}`")

    lines += ["", "### Paper Records"]
    for r in results:
        if r.get("paper_path"):
            status = "(new)" if r.get("paper_created") else "(existing)"
            lines.append(f"- `{r['paper_path']}` {status}")

    content = "\n".join(lines) + "\n"
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\nBatch-3 log written: {log_path}")
    return log_path


def main():
    print("=" * 70)
    print("P2 Batch-3 Paper Acquisition — Lane A (CoT/Eval + Agentic/Multi-Agent)")
    print("2026-07-10")
    print("=" * 70)

    results = []

    for i, paper in enumerate(P2_BATCH3_PAPERS):
        log_entry = {
            "paper_id": paper["id"],
            "title": paper["title"],
            "gap": paper["gap"],
            "warn": paper["warn"],
        }
        try:
            log_entry = process_paper_b3(paper, log_entry)
        except Exception as e:
            print(f"  UNEXPECTED ERROR for {paper['id']}: {e}")
            import traceback
            traceback.print_exc()
            log_entry["status"] = "MISS"
            log_entry["miss_reason"] = f"Unexpected error: {e}"
        results.append(log_entry)

        # 5-second inter-paper sleep (non-negotiable per brief)
        if i < len(P2_BATCH3_PAPERS) - 1:
            print(f"  [Inter-paper sleep 5s]")
            time.sleep(5)

    # Summary
    print("\n" + "=" * 70)
    print("BATCH-3 SUMMARY")
    print("=" * 70)
    hits = [r for r in results if r.get("status") == "HIT"]
    misses = [r for r in results if r.get("status") == "MISS"]
    print(f"Attempted: {len(results)}")
    print(f"HITs:      {len(hits)}")
    print(f"MISSes:    {len(misses)}")
    for r in misses:
        print(f"  MISS [{r['paper_id']}]: {r.get('miss_reason', 'unknown')}")

    # Write log
    log_path = write_batch3_log(results)

    # Save raw results as JSON
    json_path = LOG_DIR / "20260710-p2-acquisition-batch3-results.json"
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"Raw results: {json_path}")

    return len(hits), len(misses)


if __name__ == "__main__":
    main()
