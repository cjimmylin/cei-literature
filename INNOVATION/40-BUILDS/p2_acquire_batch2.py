#!/usr/bin/env python3
"""
P2 Acquisition Script — Batch 2 (Lane A)
Social Choice/Aggregation + Reward-Model Science gap groups (14 papers)
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

# Paths (same as p1_acquire.py)
VAULT_ROOT = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS")
PDFS_DIR = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs")
PAPERS_DIR = VAULT_ROOT / "papers"
EXTRACTS_DIR = VAULT_ROOT / "PDF Extracts"
LOG_DIR = VAULT_ROOT / "INNOVATION" / "40-BUILDS"

try:
    import requests
    import fitz  # PyMuPDF
except ImportError as e:
    print(f"Missing dependency: {e}")
    sys.exit(1)

# Import reusable functions from p1_acquire (same directory)
sys.path.insert(0, str(LOG_DIR))
from p1_acquire import (
    fetch_arxiv_metadata,
    download_pdf,
    extract_pdf,
    make_paper_record,
    get_ethics_perspective,
    GAP_CODES,
)

# -----------------------------------------------------------------------
# P2 Batch-2 papers definition — 14 papers, Lane A
# -----------------------------------------------------------------------
P2_PAPERS = [
    {
        "id": "P2-01",
        "title": "Social Choice Should Guide AI (ICML position)",
        "author_year": "2024",
        "arxiv_id": "2404.10271",
        "gap": "G-10",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-02",
        "title": "Population-Proportional Alignment",
        "author_year": "2025",
        "arxiv_id": "2506.05619",
        "gap": "G-10",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-03",
        "title": "Pairwise Calibrated Rewards",
        "author_year": "2025",
        "arxiv_id": "2506.06298",
        "gap": "G-10",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-04",
        "title": "Distortion of AI Alignment",
        "author_year": "2025",
        "arxiv_id": "2505.23749",
        "gap": "G-10",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-05",
        "title": "Fair Consensus (token-level MDP)",
        "author_year": "2025",
        "arxiv_id": "2510.14106",
        "gap": "G-11",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-06",
        "title": "Democratic ICAI",
        "author_year": "2026",
        "arxiv_id": "2606.28294",
        "gap": "G-11",
        "warn": True,   # ⚠ verify-first
        "priority": "P2",
    },
    {
        "id": "P2-07",
        "title": "Democratic Ontology Deficit",
        "author_year": "2026",
        "arxiv_id": "2604.03865",
        "gap": "G-12",
        "warn": True,   # ⚠ verify-first
        "priority": "P2",
    },
    {
        "id": "P2-08",
        "title": "Bringing AI Participation Down to Scale",
        "author_year": "2024",
        "arxiv_id": "2407.11613",
        "gap": "G-12",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-09",
        "title": "Auditing Language Models for Hidden Objectives",
        "author_year": "2025",
        "arxiv_id": "2503.10965",
        "gap": "G-04",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-10",
        "title": "SAFER (reward-model mech interp)",
        "author_year": "2025",
        "arxiv_id": "2507.00665",
        "gap": "G-04",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-11",
        "title": "WIMHF (what annotators expressed, SAE)",
        "author_year": "2025",
        "arxiv_id": "2510.26202",
        "gap": "G-05",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-12",
        "title": "Preference-data curation / label noise",
        "author_year": "2025",
        "arxiv_id": "2511.10985",
        "gap": "G-05",
        "warn": False,
        "priority": "P2",
    },
    {
        "id": "P2-13",
        "title": "RLVR gaming",
        "author_year": "2026",
        "arxiv_id": "2604.15149",
        "gap": "G-06",
        "warn": True,   # ⚠ verify-first
        "priority": "P2",
    },
    {
        "id": "P2-14",
        "title": "Self-Preference Bias (LLM judge)",
        "author_year": "2024",
        "arxiv_id": "2410.21819",
        "gap": "G-09/G-04",
        "warn": False,
        "priority": "P2",
    },
]


def make_file_stem(year, authors, title_short):
    """Generate a safe file stem from year, first author surname, short title."""
    # Get first author surname (last word of first author)
    if authors:
        first_author = authors[0]
        # Take last name (last word)
        surname = first_author.strip().split()[-1] if first_author.strip() else "Unknown"
    else:
        surname = "Unknown"
    return f"{year}-{surname}-{title_short}"


def sanitize_filename(s):
    """Remove characters unsafe for filenames."""
    s = re.sub(r'[<>:"/\\|?*]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def title_match_ok(paper, fetched_title):
    """
    Check whether the fetched title reasonably matches the expected topic.
    For ⚠ items: strict — if clearly different topic, return False.
    For non-⚠ items: liberal — abbreviations OK, just check for wildly different topic.
    Returns (ok: bool, reason: str)
    """
    fetched_lower = fetched_title.lower()

    # Build topic keywords from the expected title
    expected = paper["title"].lower()

    # Topic-based heuristic checks
    # For each paper we do a quick sanity check that the topic hasn't flipped completely
    topic_checks = {
        "P2-01": ["social choice", "alignment", "ai"],
        "P2-02": ["alignment", "proportion", "population"],
        "P2-03": ["reward", "calibrat", "pairwise"],
        "P2-04": ["distortion", "alignment"],
        "P2-05": ["consensus", "fair", "token", "mdp", "generation"],
        "P2-06": ["democratic", "ai", "inclus"],  # ⚠
        "P2-07": ["democratic", "ontolog", "deficit"],  # ⚠
        "P2-08": ["participation", "scale", "ai"],
        "P2-09": ["audit", "hidden", "objective"],
        "P2-10": ["reward", "safer", "interp", "mechanis"],
        "P2-11": ["annotator", "expressed", "human feedback", "sae", "wimhf"],
        "P2-12": ["preference", "label", "noise", "curation"],
        "P2-13": ["rlvr", "gaming", "reward", "reinforcement"],  # ⚠
        "P2-14": ["self-preference", "bias", "llm", "judge", "self preference"],
    }

    keywords = topic_checks.get(paper["id"], [])
    matched = sum(1 for kw in keywords if kw in fetched_lower)

    if len(keywords) == 0:
        return True, "no keywords defined — accepted"

    # For ⚠ items: require ≥2 keyword matches OR at least 1 if there are ≤2 keywords
    threshold = 2 if (paper["warn"] and len(keywords) >= 3) else 1
    if matched >= threshold:
        return True, f"matched {matched}/{len(keywords)} topic keywords"
    else:
        return False, f"only {matched}/{len(keywords)} topic keywords matched in '{fetched_title}'"


def process_paper_p2(paper, log_entry):
    """Full pipeline for P2 papers: verify → download → extract → record."""
    arxiv_id = paper["arxiv_id"]
    gap = paper["gap"]

    log_entry["arxiv_id"] = arxiv_id
    log_entry["warn"] = paper["warn"]
    log_entry["gap"] = gap

    print(f"\n[{paper['id']}] {paper['title'][:60]}")
    print(f"  arXiv: {arxiv_id} {'⚠ VERIFY' if paper['warn'] else ''}")

    # Step 1: Fetch metadata (mandatory for all items per rules)
    meta = fetch_arxiv_metadata(arxiv_id)
    if meta is None:
        log_entry["status"] = "MISS"
        log_entry["verify_result"] = "FAILED - could not fetch metadata"
        log_entry["downloaded"] = False
        log_entry["miss_reason"] = "arXiv metadata fetch failed"
        return log_entry

    fetched_title = meta.get("title", "")
    log_entry["fetched_title"] = fetched_title
    log_entry["fetched_authors"] = "; ".join(meta.get("authors", [])[:3])
    log_entry["fetched_year"] = meta.get("year")

    print(f"  Title: '{fetched_title}'")
    print(f"  Authors: {meta.get('authors', [])[:2]}")

    # Step 2: Verify title match
    match_ok, match_reason = title_match_ok(paper, fetched_title)

    if paper["warn"]:
        if match_ok:
            log_entry["verify_result"] = f"⚠ RESOLVED — '{fetched_title}' ({match_reason})"
            print(f"  ⚠ RESOLVED: {match_reason}")
        else:
            log_entry["verify_result"] = f"⚠ MISMATCH — '{fetched_title}' ({match_reason})"
            log_entry["status"] = "MISS"
            log_entry["downloaded"] = False
            log_entry["miss_reason"] = f"⚠ title mismatch: {match_reason}. Fetched: '{fetched_title}'"
            print(f"  ⚠ MISMATCH — logging MISS and skipping. Reason: {match_reason}")
            return log_entry
    else:
        if match_ok:
            log_entry["verify_result"] = f"OK — '{fetched_title}' ({match_reason})"
        else:
            # Non-⚠ wildly different topic → MISS
            log_entry["verify_result"] = f"TOPIC MISMATCH — '{fetched_title}' ({match_reason})"
            log_entry["status"] = "MISS"
            log_entry["downloaded"] = False
            log_entry["miss_reason"] = f"Topic mismatch (non-⚠): {match_reason}. Fetched: '{fetched_title}'"
            print(f"  TOPIC MISMATCH — logging MISS. Reason: {match_reason}")
            return log_entry

    # Step 3: Determine file stem from actual metadata
    actual_year = meta.get("year") or int(paper["author_year"][:4])
    authors = meta.get("authors", [])
    first_author = authors[0] if authors else "Unknown"
    surname = first_author.strip().split()[-1] if first_author.strip() else "Unknown"
    surname = sanitize_filename(surname)

    # Derive a short title from the fetched title (max ~50 chars, safe for filename)
    # Use the expected short name as the guide, but build from actual title
    # Strategy: use abbreviated version of actual title, max 40 chars, strip unsafe chars
    title_safe = sanitize_filename(fetched_title)
    # Truncate at a word boundary ~40 chars
    if len(title_safe) > 50:
        words = title_safe.split()
        short = ""
        for w in words:
            candidate = (short + " " + w).strip()
            if len(candidate) <= 50:
                short = candidate
            else:
                break
        title_safe = short if short else title_safe[:50]

    file_stem = f"{actual_year}-{surname}-{title_safe}"
    log_entry["file_stem"] = file_stem

    # Step 4: Download PDF
    pdf_subdir = PDFS_DIR / str(actual_year)
    pdf_subdir.mkdir(parents=True, exist_ok=True)
    pdf_path = pdf_subdir / f"{file_stem}.pdf"

    # Idempotent: skip if already exists and non-trivial
    if pdf_path.exists() and pdf_path.stat().st_size > 10000:
        print(f"  PDF already exists: {pdf_path.name}")
        pdf_downloaded = True
    else:
        # 5-second inter-download sleep as required by rules
        print(f"  Sleeping 5s before download (rate limit)...")
        time.sleep(5)
        pdf_downloaded = download_pdf(arxiv_id, pdf_path)

    log_entry["downloaded"] = pdf_downloaded
    log_entry["pdf_path"] = str(pdf_path) if pdf_downloaded else ""

    if not pdf_downloaded:
        log_entry["status"] = "MISS"
        log_entry["miss_reason"] = "PDF download failed"
        return log_entry

    # Step 5: Extract text
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

    # Step 6: Create paper record
    paper_path = PAPERS_DIR / f"{file_stem}.md"

    if paper_path.exists():
        print(f"  Paper record already exists: {paper_path.name}")
        log_entry["paper_created"] = False
        log_entry["paper_path"] = str(paper_path)
        log_entry["paper_note"] = "already existed"
        log_entry["status"] = "HIT (existing)"
    else:
        # Build paper dict in format expected by make_paper_record
        paper_dict = {
            "id": paper["id"],
            "arxiv_id": arxiv_id,
            "title": paper["title"],
            "gap": gap,
            "year": actual_year,
            "file_stem": file_stem,
            "warn": paper["warn"],
            "priority": paper["priority"],
        }
        yaml_text = make_paper_record(
            paper_dict, meta,
            pdf_path if pdf_downloaded else None,
            extract_path if extracted else None
        )
        # make_paper_record uses paper['id'] prefixed with INNOVATION-
        # We override the key line to use P2 prefix
        yaml_text = yaml_text.replace(
            f"key: INNOVATION-{paper['id'].replace('-', '')}",
            f"key: INNOVATION-{paper['id'].replace('-', '')}"
        )
        with open(paper_path, 'w', encoding='utf-8') as f:
            f.write(yaml_text)
        print(f"  Created paper record: {paper_path.name}")
        log_entry["paper_created"] = True
        log_entry["paper_path"] = str(paper_path)
        log_entry["status"] = "HIT"

    return log_entry


def write_acquisition_log(results):
    """Write the P2 batch-2 acquisition log markdown file."""
    log_path = LOG_DIR / "20260710-p2-acquisition-log-batch2.md"

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    attempted = len(results)
    hits = sum(1 for r in results if r.get("status", "").startswith("HIT"))
    misses = sum(1 for r in results if r.get("status") == "MISS")
    downloaded = sum(1 for r in results if r.get("downloaded"))
    extracted = sum(1 for r in results if r.get("extracted"))
    created = sum(1 for r in results if r.get("paper_created"))
    warn_items = [r for r in results if r.get("warn")]
    warn_resolved = sum(1 for r in warn_items if "RESOLVED" in r.get("verify_result", ""))

    lines = [
        f"# P2 Acquisition Log — Batch 2 (Lane A) — {now}",
        "",
        "**Papers:** Social Choice/Aggregation (G-10/G-11/G-12) + Reward-Model Science (G-04/G-05/G-06/G-09)",
        "**Pipeline:** arXiv metadata verify → PDF download (5s sleep) → PyMuPDF extract → paper record",
        "**Script:** `INNOVATION/40-BUILDS/p2_acquire_batch2.py`",
        "",
        "## Summary",
        "",
        "| Metric | Count |",
        "|--------|-------|",
        f"| Attempted | {attempted} |",
        f"| HITs | {hits} |",
        f"| MISSes | {misses} |",
        f"| ⚠ Verified | {warn_resolved} / {len(warn_items)} |",
        f"| Downloaded | {downloaded} |",
        f"| Extracted | {extracted} |",
        f"| Paper records created | {created} |",
        "",
        "## ⚠ Verification Results",
        "",
        "| ID | arXiv ID | Fetched Title | Verdict |",
        "|----|---------|--------------|---------|",
    ]

    for r in results:
        if r.get("warn"):
            pid = r.get("paper_id", "")
            arxiv = r.get("arxiv_id", "")
            ftitle = r.get("fetched_title", "")[:60]
            verdict = r.get("verify_result", "")[:80]
            lines.append(f"| {pid} | {arxiv} | {ftitle} | {verdict} |")

    lines += [
        "",
        "## Per-Paper Results",
        "",
        "| ID | Expected Title | arXiv ID | Gap | Status | Paper File |",
        "|----|---------------|---------|-----|--------|-----------|",
    ]

    for r in results:
        pid = r.get("paper_id", "")
        title = r.get("title", "")[:40]
        arxiv = r.get("arxiv_id", "")
        gap = r.get("gap", "")
        status = r.get("status", "MISS")
        ppath = r.get("paper_path", "")
        pfname = Path(ppath).name if ppath else ""
        lines.append(f"| {pid} | {title} | {arxiv} | {gap} | {status} | {pfname} |")

    lines += [
        "",
        "## Miss Detail",
        "",
    ]

    for r in results:
        if r.get("status") == "MISS":
            lines.append(f"- **{r.get('paper_id', '')}** ({r.get('arxiv_id', '')}): {r.get('miss_reason', 'unknown')}")
            lines.append(f"  - Fetched title: {r.get('fetched_title', 'N/A')}")
            lines.append(f"  - Verify result: {r.get('verify_result', 'N/A')}")

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
            status = "(existing)" if not r.get("paper_created") else "(new)"
            lines.append(f"- `{r['paper_path']}` {status}")

    content = "\n".join(lines) + "\n"
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\nAcquisition log written: {log_path}")
    return log_path


def main():
    print("=" * 70)
    print("P2 Anchor Paper Acquisition — Batch 2 (Lane A) — 2026-07-10")
    print("14 papers: Social Choice + Reward-Model Science")
    print("=" * 70)

    results = []

    for i, paper in enumerate(P2_PAPERS):
        log_entry = {
            "paper_id": paper["id"],
            "title": paper["title"],
            "gap": paper["gap"],
            "priority": paper["priority"],
        }
        try:
            log_entry = process_paper_p2(paper, log_entry)
        except Exception as e:
            import traceback
            print(f"  UNEXPECTED ERROR for {paper['id']}: {e}")
            traceback.print_exc()
            log_entry["status"] = "MISS"
            log_entry["downloaded"] = False
            log_entry["miss_reason"] = f"Unexpected error: {e}"
        results.append(log_entry)

        # Inter-paper delay (additional buffer after the 5s pre-download sleep)
        if i < len(P2_PAPERS) - 1:
            print(f"  Inter-paper pause 3s...")
            time.sleep(3)

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    attempted = len(results)
    hits = sum(1 for r in results if r.get("status", "").startswith("HIT"))
    misses_list = [r for r in results if r.get("status") == "MISS"]
    print(f"Attempted: {attempted}")
    print(f"HITs: {hits}")
    print(f"MISSes: {len(misses_list)}")
    for r in misses_list:
        print(f"  MISS [{r['paper_id']}]: {r.get('miss_reason', 'unknown')}")

    # Write log
    log_path = write_acquisition_log(results)

    # Save raw results as JSON
    json_path = LOG_DIR / "20260710-p2-acquisition-results-batch2.json"
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"Raw results: {json_path}")

    return hits, len(misses_list)


if __name__ == "__main__":
    main()
