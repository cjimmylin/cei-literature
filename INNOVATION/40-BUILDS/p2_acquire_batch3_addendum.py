#!/usr/bin/env python3
"""
P2 Batch-3 Addendum — Acquire arXiv 2510.05192 (Gomez, G-16)

This paper was logged as MISS in batch-3 because the fetched title
("From surveillance to signalling: escalation channels as environmental
controls for agentic AI", v2/Apr 2026) did not match the expected keyword
"insider risk mitigation" (v1/Oct 2025 title: "Adapting Insider Risk
mitigations for Agentic Misalignment: an empirical study"). The
orchestrator verified via arxiv.org/abs/2510.05192 that this IS the
correct paper — same arXiv ID, same author (Francesca Gomez), same topic
(insider-risk management + Situational Crime Prevention + escalation
channels). Acquisition proceeds with match settled.

Date: 2026-07-10
"""

import sys
import re
import time
import json
from pathlib import Path
from datetime import datetime

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

ARXIV_ID = "2510.05192"
GAP = "G-16"
PRIORITY = "P2"
# Year 2025 = v1 submission year, consistent with arXiv metadata (published 2025-10-07)
INTENDED_YEAR = 2025

# v1 title (Oct 2025): "Adapting Insider Risk mitigations for Agentic Misalignment: an empirical study"
# v2 title (Apr 2026): "From surveillance to signalling: escalation channels as environmental controls for agentic AI"
V1_TITLE = "Adapting Insider Risk mitigations for Agentic Misalignment: an empirical study"

def make_file_stem(meta):
    """Build YYYY-FirstAuthor-Short Title stem."""
    year = meta.get("year") or INTENDED_YEAR
    authors = meta.get("authors", [])
    if authors:
        first_auth = authors[0].strip()
        if "," in first_auth:
            last_name = first_auth.split(",")[0].strip()
        else:
            parts = first_auth.split()
            last_name = parts[-1] if parts else "Unknown"
    else:
        last_name = "Unknown"

    title = meta.get("title", "")
    safe_title = re.sub(r'[<>:"/\\|?*]', '', title)
    short = safe_title[:55].rstrip().rstrip(".,;:- ")
    return f"{year}-{last_name}-{short}"


def run_addendum():
    print("=" * 70)
    print("P2 Batch-3 Addendum — Acquire 2510.05192 (Gomez, G-16, P2)")
    print("2026-07-10")
    print("=" * 70)

    result = {
        "paper_id": "P2-B3-12-ADDENDUM",
        "arxiv_id": ARXIV_ID,
        "gap": GAP,
        "priority": PRIORITY,
        "v1_title": V1_TITLE,
        "match_reason": "orchestrator-verified: same arXiv ID, same author (Gomez), retitled v1→v2 (Oct 2025→Apr 2026); insider-risk + SCP + escalation channels confirmed from abs page",
    }

    # Step 1: Fetch metadata
    print(f"\nFetching metadata for {ARXIV_ID}...")
    meta = fetch_arxiv_metadata(ARXIV_ID)
    if meta is None:
        print("ERROR: Could not fetch metadata")
        result["status"] = "FAIL"
        result["miss_reason"] = "arXiv metadata fetch failed"
        return result, None, None, None

    fetched_title = meta.get("title", "")
    actual_year = meta.get("year") or INTENDED_YEAR
    result["fetched_title"] = fetched_title
    result["fetched_authors"] = "; ".join(meta.get("authors", [])[:5])
    result["fetched_year"] = actual_year

    print(f"  Title (v2): '{fetched_title}'")
    print(f"  Authors: {meta.get('authors', [])[:3]}")
    print(f"  Year (arXiv published): {actual_year}")

    # Use v1 submission year for filing (2025), but note: arXiv "published" may return 2025
    # The file stem should use the year arXiv returns (should be 2025 for v1 submission date)
    file_stem = make_file_stem(meta)
    # Override year to 2025 if arXiv returns something different (shouldn't happen, but be explicit)
    if not file_stem.startswith("2025-"):
        # Force 2025 per brief (v1 submission year)
        file_stem = "2025-" + file_stem.split("-", 1)[1] if "-" in file_stem else f"2025-{file_stem}"
        actual_year = 2025

    result["file_stem"] = file_stem
    print(f"  File stem: {file_stem}")

    # Step 2: Download PDF
    pdf_subdir = PDFS_DIR / str(actual_year)
    pdf_subdir.mkdir(parents=True, exist_ok=True)
    pdf_path = pdf_subdir / f"{file_stem}.pdf"

    if pdf_path.exists() and pdf_path.stat().st_size > 10000:
        print(f"  PDF already exists: {pdf_path}")
        pdf_downloaded = True
    else:
        print(f"  Sleeping 5s before download (rate-limit)...")
        time.sleep(5)
        pdf_downloaded = download_pdf(ARXIV_ID, pdf_path)

    result["downloaded"] = pdf_downloaded
    result["pdf_path"] = str(pdf_path) if pdf_downloaded else ""

    if not pdf_downloaded:
        print("ERROR: PDF download failed")
        result["status"] = "FAIL"
        result["miss_reason"] = "PDF download failed"
        return result, None, None, None

    # Verify %PDF magic bytes
    with open(pdf_path, 'rb') as f:
        magic = f.read(4)
    if magic != b'%PDF':
        print(f"ERROR: Not a valid PDF (magic bytes: {magic!r})")
        result["status"] = "FAIL"
        result["miss_reason"] = f"Not a valid PDF: magic={magic!r}"
        return result, pdf_path, None, None

    print(f"  PDF magic bytes: OK (%PDF)")
    result["pdf_magic_ok"] = True

    # Step 3: Extract text
    extract_subdir = EXTRACTS_DIR / str(actual_year)
    extract_subdir.mkdir(parents=True, exist_ok=True)
    extract_path = extract_subdir / f"{file_stem}.md"

    if extract_path.exists():
        print(f"  Extract already exists: {extract_path}")
        extracted = True
    else:
        extracted = extract_pdf(pdf_path, extract_path)

    result["extracted"] = extracted
    result["extract_path"] = str(extract_path) if extracted else ""

    # Verify page-1 text contains current title keywords
    if extracted:
        try:
            import fitz
            doc = fitz.open(str(pdf_path))
            page1_text = doc[0].get_text().lower()
            doc.close()
            # Current v2 title words to verify
            title_words = ["surveillance", "signalling", "escalation", "channels", "environmental"]
            matched = [w for w in title_words if w in page1_text]
            result["page1_title_check"] = {
                "checked_words": title_words,
                "matched": matched,
                "pass": len(matched) >= 2,
            }
            if len(matched) >= 2:
                print(f"  Page-1 title check: PASS (matched: {matched})")
            else:
                print(f"  Page-1 title check: WARN — only matched {matched}")
        except Exception as e:
            print(f"  Page-1 title check: ERROR ({e})")
            result["page1_title_check"] = {"error": str(e)}

    # Step 4: Create paper record
    paper_path = PAPERS_DIR / f"{file_stem}.md"

    if paper_path.exists():
        print(f"  Paper record already exists: {paper_path}")
        result["paper_created"] = False
        result["paper_path"] = str(paper_path)
        result["paper_note"] = "already existed"
    else:
        paper_compat = {
            "id": "P2B312-ADDENDUM",
            "arxiv_id": ARXIV_ID,
            "title": fetched_title,
            "year": actual_year,
            "gap": GAP,
            "priority": PRIORITY,
        }

        yaml_text = make_paper_record(
            paper_compat, meta,
            pdf_path if pdf_downloaded else None,
            extract_path if extracted else None,
        )

        # Inject priority field after innovation_gap
        yaml_text = yaml_text.replace(
            f'innovation_gap: "{GAP}"',
            f'innovation_gap: "{GAP}"\npriority: "{PRIORITY}"'
        )

        # Append v1 former title note to the body (after Abstract section)
        v1_note = f"""
## Former Title (v1)

**v1 title (Oct 2025):** {V1_TITLE}

*Note: The paper was retitled between v1 (Oct 2025) and v2 (Apr 2026). The v1 title
"Adapting Insider Risk mitigations for Agentic Misalignment: an empirical study"
caused a keyword-match MISS during Batch-3 acquisition (2026-07-10). The paper was
subsequently verified by the orchestrator via arxiv.org/abs/{ARXIV_ID} and acquired
as this addendum. The topic (insider-risk management + Situational Crime Prevention +
escalation channels for agentic AI) is confirmed as gap G-16 (Multi-Agent Value Dynamics).*
"""
        yaml_text = yaml_text + v1_note

        with open(paper_path, 'w', encoding='utf-8') as f:
            f.write(yaml_text)
        print(f"  Created paper record: {paper_path}")
        result["paper_created"] = True
        result["paper_path"] = str(paper_path)

    result["status"] = "HIT"
    print(f"\nAcquisition COMPLETE: {file_stem}")
    return result, pdf_path, extract_path, paper_path


def write_addendum_log(result, pdf_path, extract_path, paper_path):
    """Write the addendum log as a new file (append-style new file, per brief)."""
    log_path = LOG_DIR / "20260710-p2-acquisition-log-batch3-addendum.md"

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    status = result.get("status", "UNKNOWN")

    lines = [
        f"# P2 Batch-3 Addendum — arXiv 2510.05192 — {now}",
        "",
        "## Background: Original MISS",
        "",
        "**Batch run:** 2026-07-09 20:51 (`p2_acquire_batch3.py`, P2-B3-12)",
        "**arXiv ID:** 2510.05192",
        "**Expected title keywords:** insider, risk, mitigation",
        "**Fetched title:** \"From surveillance to signalling: escalation channels as environmental controls for agentic AI\"",
        "**MISS reason logged:** topic mismatch — fetched title did not match keywords",
        "",
        "## Orchestrator Verification Evidence",
        "",
        "The orchestrator verified via https://arxiv.org/abs/2510.05192 and web search that",
        "this IS the correct paper:",
        "",
        "- **arXiv ID confirmed:** 2510.05192 maps unambiguously to a single paper",
        "- **Author confirmed:** Francesca Gomez (sole author, consistent with gap G-16 P2 record)",
        "- **Retitle event:** v1 title (Oct 2025): \"Adapting Insider Risk mitigations for",
        "  Agentic Misalignment: an empirical study\" → v2 title (Apr 2026): \"From surveillance",
        "  to signalling: escalation channels as environmental controls for agentic AI\"",
        "- **Abstract match:** confirms insider-risk management + Situational Crime Prevention",
        "  (SCP) + escalation channels — all core G-16 content",
        "- **Match verdict:** SETTLED — do not re-adjudicate",
        "",
        "## Acquisition Outcome",
        "",
        f"| Field | Value |",
        f"|-------|-------|",
        f"| Status | {status} |",
        f"| arXiv ID | {result.get('arxiv_id', '')} |",
        f"| Fetched title (v2) | {result.get('fetched_title', '')} |",
        f"| v1 title | {result.get('v1_title', '')} |",
        f"| Authors | {result.get('fetched_authors', '')} |",
        f"| Year filed under | {result.get('fetched_year', '')} |",
        f"| File stem | {result.get('file_stem', '')} |",
        f"| Gap | {result.get('gap', '')} |",
        f"| Priority | {result.get('priority', '')} |",
        f"| PDF magic OK | {result.get('pdf_magic_ok', False)} |",
        f"| Page-1 title check | {result.get('page1_title_check', 'N/A')} |",
        "",
        "## Vault Paths Created",
        "",
        f"- **PDF:** `{result.get('pdf_path', 'N/A')}`",
        f"- **Extract:** `{result.get('extract_path', 'N/A')}`",
        f"- **Paper record:** `{result.get('paper_path', 'N/A')}`",
        "",
        "## Notes",
        "",
        "- Paper record body includes a '## Former Title (v1)' section so future title-greps",
        "  on the v1 string will hit this file.",
        "- This addendum log is a NEW file per the project rule (no overwrite of existing",
        "  batch-3 log `20260710-p2-acquisition-log-batch3.md`).",
        "- Script: `INNOVATION/40-BUILDS/p2_acquire_batch3_addendum.py`",
        "",
    ]

    content = "\n".join(lines)
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\nAddendum log written: {log_path}")
    return log_path


if __name__ == "__main__":
    result, pdf_path, extract_path, paper_path = run_addendum()
    log_path = write_addendum_log(result, pdf_path, extract_path, paper_path)

    print("\n" + "=" * 70)
    print(f"STATUS: {result.get('status', 'UNKNOWN')}")
    if result.get("status") == "HIT":
        print(f"  PDF:    {result.get('pdf_path')}")
        print(f"  Extract:{result.get('extract_path')}")
        print(f"  Paper:  {result.get('paper_path')}")
    print(f"  Log:    {log_path}")
    print("=" * 70)
