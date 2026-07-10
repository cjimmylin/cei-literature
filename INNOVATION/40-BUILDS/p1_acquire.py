#!/usr/bin/env python3
"""
P1 Anchor Paper Acquisition Script
Acquires 17 P1 papers from INNOVATION/04-missing-literature.md
into the vault: PDF → Extract → Paper record
Date: 2026-07-09
"""

import os
import sys
import re
import time
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

# Paths
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

# -----------------------------------------------------------------------
# P1 papers definition
# -----------------------------------------------------------------------
P1_PAPERS = [
    # (id, arxiv_id, title_short, gap, warn_flag)
    {
        "id": "P1-01",
        "title": "Emergent Misalignment (narrow finetune → broad misalignment)",
        "author_year": "Betley 2025",
        "arxiv_id": "2502.17424",
        "gap": "G-20",
        "warn": False,
        "file_stem": "2025-Betley-Emergent Misalignment",
        "year": 2025,
    },
    {
        "id": "P1-02",
        "title": "Persona Vectors",
        "author_year": "Anthropic 2025",
        "arxiv_id": "2507.21509",
        "gap": "G-20",
        "warn": False,
        "file_stem": "2025-Anthropic-Persona Vectors",
        "year": 2025,
    },
    {
        "id": "P1-03",
        "title": "Persona Features Control EM (OpenAI)",
        "author_year": "2025",
        "arxiv_id": "2506.19823",
        "gap": "G-20",
        "warn": False,
        "file_stem": "2025-OpenAI-Persona Features Control EM",
        "year": 2025,
    },
    {
        "id": "P1-04",
        "title": "Natural EM from Reward Hacking",
        "author_year": "Anthropic 2025",
        "arxiv_id": "2511.18397",
        "gap": "G-06/20",
        "warn": False,
        "file_stem": "2025-Anthropic-Natural EM from Reward Hacking",
        "year": 2025,
    },
    {
        "id": "P1-05",
        "title": "SpecEval (spec↔behavior consistency)",
        "author_year": "2025",
        "arxiv_id": "2509.02464",
        "gap": "G-01",
        "warn": False,
        "file_stem": "2025-SpecEval",
        "year": 2025,
    },
    {
        "id": "P1-06",
        "title": "Stress-Testing Model Specifications",
        "author_year": "2025",
        "arxiv_id": "2510.07686",
        "gap": "G-02",
        "warn": False,
        "file_stem": "2025-Stress-Testing Model Specifications",
        "year": 2025,
    },
    {
        "id": "P1-07",
        "title": "Peer-Prediction for scalable oversight",
        "author_year": "2026",
        "arxiv_id": "2601.20299",
        "gap": "G-07",
        "warn": False,
        "file_stem": "2026-Peer-Prediction Scalable Oversight",
        "year": 2026,
    },
    {
        "id": "P1-08",
        "title": "Confirmation Bias in oversight (judges)",
        "author_year": "2025",
        "arxiv_id": "2507.19486",
        "gap": "G-09",
        "warn": False,
        "file_stem": "2025-Confirmation Bias in LLM Oversight",
        "year": 2025,
    },
    {
        "id": "P1-09",
        "title": "AI Debaters' Own Beliefs bias",
        "author_year": "2025",
        "arxiv_id": "2510.13912",
        "gap": "G-09",
        "warn": False,
        "file_stem": "2025-AI Debaters Own Beliefs Bias",
        "year": 2025,
    },
    {
        "id": "P1-10",
        "title": "Social Choice for AI Alignment (survey)",
        "author_year": "2026",
        "arxiv_id": "2606.21550",
        "gap": "G-10",
        "warn": True,
        "file_stem": "2026-Social Choice for AI Alignment Survey",
        "year": 2026,
    },
    {
        "id": "P1-11",
        "title": "RMs Inherit Value Biases",
        "author_year": "Christian 2026",
        "arxiv_id": "2601.20838",
        "gap": "G-04",
        "warn": False,
        "file_stem": "2026-Christian-RMs Inherit Value Biases",
        "year": 2026,
    },
    {
        "id": "P1-12",
        "title": "CoT Monitorability (position paper)",
        "author_year": "2025",
        "arxiv_id": "2507.11473",
        "gap": "G-13",
        "warn": False,
        "file_stem": "2025-CoT Monitorability",
        "year": 2025,
    },
    {
        "id": "P1-13",
        "title": "Eval-design awareness → safer scores",
        "author_year": "2026",
        "arxiv_id": "2605.28591",
        "gap": "G-14",
        "warn": True,
        "file_stem": "2026-Eval-Design Awareness Safer Scores",
        "year": 2026,
    },
    {
        "id": "P1-14",
        "title": "Value-Conflict Diagnostics for faking",
        "author_year": "2026",
        "arxiv_id": "2604.20995",
        "gap": "G-15",
        "warn": True,
        "file_stem": "2026-Value-Conflict Diagnostics for Faking",
        "year": 2026,
    },
    {
        "id": "P1-15",
        "title": "Utility–Behavior Gap",
        "author_year": "2026",
        "arxiv_id": "2606.22974",
        "gap": "G-23",
        "warn": True,
        "file_stem": "2026-Utility-Behavior Gap",
        "year": 2026,
    },
    {
        "id": "P1-16",
        "title": "Subliminal Learning",
        "author_year": "2025",
        "arxiv_id": "2507.14805",
        "gap": "G-21",
        "warn": False,
        "file_stem": "2025-Subliminal Learning",
        "year": 2025,
    },
    {
        "id": "P1-17",
        "title": "SSGM memory-drift governance",
        "author_year": "2026",
        "arxiv_id": "2603.11768",
        "gap": "G-18",
        "warn": False,
        "file_stem": "2026-SSGM Memory-Drift Governance",
        "year": 2026,
    },
]

# Gap → ethics_perspective mapping (v1.5 codes)
GAP_CODES = {
    "G-01": "Specification & Compliance",
    "G-02": "Specification & Compliance",
    "G-03": "Specification & Compliance",
    "G-04": "AI Safety & Alignment",
    "G-05": "AI Safety & Alignment",
    "G-06": "Value Formation & Emergent Misalignment",
    "G-07": "Scalable Oversight",
    "G-08": "Scalable Oversight",
    "G-09": "Scalable Oversight",
    "G-10": "Preference Aggregation & Social Choice",
    "G-11": "Preference Aggregation & Social Choice",
    "G-12": "Preference Aggregation & Social Choice",
    "G-13": "AI Safety & Alignment",
    "G-14": "AI Safety & Alignment",
    "G-15": "AI Safety & Alignment",
    "G-16": "Multi-Agent Value Dynamics",
    "G-17": "Multi-Agent Value Dynamics",
    "G-18": "Multi-Agent Value Dynamics",
    "G-19": "Multi-Agent Value Dynamics",
    "G-20": "Value Formation & Emergent Misalignment",
    "G-21": "Value Formation & Emergent Misalignment",
    "G-22": "Value Formation & Emergent Misalignment",
    "G-23": "Value Formation & Emergent Misalignment",
}


def get_ethics_perspective(gap_str):
    """Get ethics_perspective code from gap IDs like 'G-06/20'."""
    gaps = [g.strip() for g in gap_str.split("/")]
    # Normalize partial IDs like '20' to 'G-20'
    normalized = []
    for g in gaps:
        if not g.startswith("G-"):
            g = "G-" + g
        normalized.append(g)
    # Return the first matching code
    for g in normalized:
        if g in GAP_CODES:
            return GAP_CODES[g]
    return "AI Safety & Alignment"


def fetch_arxiv_metadata(arxiv_id):
    """Fetch paper metadata from arXiv export API."""
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    print(f"  Fetching metadata: {url}")
    try:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        ns = {"atom": "http://www.w3.org/2005/Atom",
              "arxiv": "http://arxiv.org/schemas/atom"}
        root = ET.fromstring(resp.text)
        entries = root.findall("atom:entry", ns)
        if not entries:
            return None
        entry = entries[0]
        # title
        title_el = entry.find("atom:title", ns)
        title = " ".join(title_el.text.split()) if title_el is not None else ""
        # authors
        authors = []
        for auth_el in entry.findall("atom:author", ns):
            name_el = auth_el.find("atom:name", ns)
            if name_el is not None:
                authors.append(name_el.text.strip())
        # abstract
        summ_el = entry.find("atom:summary", ns)
        abstract = " ".join(summ_el.text.split()) if summ_el is not None else ""
        # published year
        pub_el = entry.find("atom:published", ns)
        year = int(pub_el.text[:4]) if pub_el is not None else None
        # categories
        cats = [c.get("term", "") for c in entry.findall("atom:category", ns)]
        return {
            "title": title,
            "authors": authors,
            "abstract": abstract,
            "year": year,
            "categories": cats,
        }
    except Exception as e:
        print(f"  ERROR fetching metadata: {e}")
        return None
    finally:
        time.sleep(3)  # rate limit


def download_pdf(arxiv_id, dest_path):
    """Download PDF from arXiv with retry/backoff."""
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    print(f"  Downloading PDF: {url}")
    for attempt in range(4):
        try:
            resp = requests.get(url, timeout=60, stream=True)
            if resp.status_code == 200:
                content = resp.content
                # Verify it's actually a PDF
                if content[:4] == b'%PDF':
                    with open(dest_path, 'wb') as f:
                        f.write(content)
                    print(f"  Saved PDF: {dest_path} ({len(content)//1024}KB)")
                    return True
                else:
                    # May be HTML redirect (e.g. "on hold" message)
                    print(f"  WARN: Response is not a PDF (got {content[:50]})")
                    return False
            elif resp.status_code in (429, 503):
                wait = 2 ** attempt * 5
                print(f"  Rate-limited ({resp.status_code}), waiting {wait}s...")
                time.sleep(wait)
            else:
                print(f"  HTTP error {resp.status_code}")
                return False
        except Exception as e:
            wait = 2 ** attempt * 3
            print(f"  Download error (attempt {attempt+1}): {e} — retry in {wait}s")
            time.sleep(wait)
    return False


def extract_pdf(pdf_path, extract_path):
    """Extract text from PDF using PyMuPDF."""
    try:
        doc = fitz.open(str(pdf_path))
        pages = len(doc)
        text_parts = [f"Page {i+1}:\n{doc[i].get_text()}\n" for i in range(pages)]
        content = f"""---
source_pdf: "[[Lit-WS-PDFs/{pdf_path.parent.name}/{pdf_path.name}]]"
extracted_date: "{datetime.now().strftime('%Y-%m-%d')}"
pages: {pages}
extractor: "PyMuPDF"
---

""" + "\n".join(text_parts)
        extract_path.parent.mkdir(parents=True, exist_ok=True)
        with open(extract_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Extracted: {extract_path.name} ({pages} pages)")
        return True
    except Exception as e:
        print(f"  Extraction error: {e}")
        return False


def make_paper_record(paper, meta, pdf_path, extract_path):
    """Build a paper .md file with full YAML frontmatter."""
    arxiv_id = paper["arxiv_id"]
    year = meta.get("year") or paper["year"]
    gap = paper["gap"]
    ethics_perspective = get_ethics_perspective(gap)

    # Authors
    authors_list = meta.get("authors", [])
    first_author = authors_list[0] if authors_list else "Unknown"
    authors_str = "; ".join(authors_list) if authors_list else "Unknown"

    # Safe title
    title = meta.get("title", paper["title"])
    abstract = meta.get("abstract", "")

    # local_pdf wikilink (year-based subdir)
    pdf_wikilink = f"[[Lit-WS-PDFs/{year}/{pdf_path.name}]]" if pdf_path else ""
    extract_rel = f"PDF Extracts/{year}/{extract_path.name}" if extract_path else ""

    # Determine type
    paper_type = "preprint"

    yaml_content = f"""---
key: INNOVATION-{paper['id'].replace('-', '')}
type: {paper_type}
short_title: "{title.replace('"', "'")}"
year: {year}
first_author: "[[{first_author}]]"
authors: "{authors_str}"
url: "https://arxiv.org/abs/{arxiv_id}"
external_pdf: "https://arxiv.org/pdf/{arxiv_id}.pdf"
abstract: "{abstract.replace('"', "'")}"
ethics_overall: 80
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
care_ethics: 0
contractarian_ethics: 0
ethics_perspective: "{ethics_perspective}"
national_ethnic_cultural: N/A
religious_values: N/A
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: N/A
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Not specified"
data_metrics: "Not specified"
newtags: "{ethics_perspective}"
key_contribution: ""
significance: ""
paper_summary: ""
local_pdf: "{pdf_wikilink}"
pdf_extract: "{extract_rel}"
tags:
  - AIAlignment
  - {gap.replace('/', '-')}
Human View: ""
Human View Date: ""
Human View note: ""
Not AI: ""
DATE_ADDED: {datetime.now().strftime('%Y%m%d')}
innovation_gap: "{gap}"
---

# {title}

## Metadata

**Authors:** {authors_str}

**Year:** {year}

**Type:** preprint

**arXiv:** https://arxiv.org/abs/{arxiv_id}

**Gap:** {gap} — {ethics_perspective}

## Abstract

{abstract}
"""
    return yaml_content


def process_paper(paper, log_entry):
    """Full pipeline: verify → download → extract → record."""
    arxiv_id = paper["arxiv_id"]
    year = paper["year"]
    file_stem = paper["file_stem"]

    log_entry["arxiv_id"] = arxiv_id
    log_entry["warn"] = paper["warn"]

    # Step 1: Fetch metadata (mandatory for ⚠ items, good practice for all)
    print(f"\n[{paper['id']}] {paper['title'][:60]}")
    print(f"  arXiv: {arxiv_id} {'⚠ VERIFY' if paper['warn'] else ''}")

    meta = fetch_arxiv_metadata(arxiv_id)
    if meta is None:
        log_entry["verify_result"] = "FAILED - could not fetch metadata"
        log_entry["downloaded"] = False
        log_entry["miss_reason"] = "arXiv metadata fetch failed"
        return log_entry

    log_entry["fetched_title"] = meta.get("title", "")
    log_entry["fetched_authors"] = "; ".join(meta.get("authors", [])[:3])
    log_entry["fetched_year"] = meta.get("year")

    if paper["warn"]:
        print(f"  ⚠ Verify: '{meta['title']}' by {meta['authors'][:2]}")
        log_entry["verify_result"] = f"RESOLVED → '{meta['title']}'"
    else:
        log_entry["verify_result"] = "N/A (no warn flag)"

    # Use fetched year if available
    actual_year = meta.get("year") or year

    # Step 2: Download PDF
    pdf_subdir = PDFS_DIR / str(actual_year)
    pdf_subdir.mkdir(parents=True, exist_ok=True)
    pdf_path = pdf_subdir / f"{file_stem}.pdf"

    # Don't re-download if already exists (idempotent)
    if pdf_path.exists() and pdf_path.stat().st_size > 10000:
        print(f"  PDF already exists: {pdf_path.name}")
        pdf_downloaded = True
    else:
        time.sleep(3)  # rate limit before download
        pdf_downloaded = download_pdf(arxiv_id, pdf_path)

    log_entry["downloaded"] = pdf_downloaded
    log_entry["pdf_path"] = str(pdf_path) if pdf_downloaded else ""

    if not pdf_downloaded:
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
    paper_path = PAPERS_DIR / f"{file_stem}.md"

    if paper_path.exists():
        print(f"  Paper record already exists: {paper_path.name}")
        log_entry["paper_created"] = False
        log_entry["paper_path"] = str(paper_path)
        log_entry["paper_note"] = "already existed"
    else:
        yaml_text = make_paper_record(
            paper, meta,
            pdf_path if pdf_downloaded else None,
            extract_path if extracted else None
        )
        with open(paper_path, 'w', encoding='utf-8') as f:
            f.write(yaml_text)
        print(f"  Created paper record: {paper_path.name}")
        log_entry["paper_created"] = True
        log_entry["paper_path"] = str(paper_path)

    return log_entry


def write_acquisition_log(results):
    """Write the acquisition log markdown file."""
    log_path = LOG_DIR / "20260709-p1-acquisition-log.md"

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    attempted = len(results)
    verified_warn = sum(1 for r in results if r.get("warn") and "RESOLVED" in r.get("verify_result", ""))
    downloaded = sum(1 for r in results if r.get("downloaded"))
    extracted = sum(1 for r in results if r.get("extracted"))
    created = sum(1 for r in results if r.get("paper_created"))
    misses = sum(1 for r in results if not r.get("downloaded"))

    lines = [
        f"# P1 Acquisition Log — {now}",
        "",
        "**Source:** `INNOVATION/04-missing-literature.md` — P1 anchor table (17 papers)",
        "**Pipeline:** arXiv metadata verify → PDF download → PyMuPDF extract → paper record",
        "",
        f"## Summary",
        "",
        f"| Metric | Count |",
        f"|--------|-------|",
        f"| Attempted | {attempted} |",
        f"| ⚠ Verified | {verified_warn} / {sum(1 for r in results if r.get('warn'))} |",
        f"| Downloaded | {downloaded} |",
        f"| Extracted | {extracted} |",
        f"| Paper records created | {created} |",
        f"| Misses | {misses} |",
        "",
        "## Per-Paper Results",
        "",
        "| ID | Title | arXiv ID | ⚠ Verify | Downloaded | Paper Path | Miss Reason |",
        "|----|----|---------|---------|-----------|-----------|-------------|",
    ]

    for r in results:
        pid = r.get("paper_id", "")
        title = r.get("title", "")[:45]
        arxiv = r.get("arxiv_id", "")
        verify = r.get("verify_result", "N/A")
        if len(verify) > 40:
            verify = verify[:40] + "…"
        dl = "YES" if r.get("downloaded") else "MISS"
        paper_path = r.get("paper_path", "")
        if paper_path:
            paper_fname = Path(paper_path).name
        else:
            paper_fname = ""
        miss = r.get("miss_reason", "")
        lines.append(f"| {pid} | {title} | {arxiv} | {verify} | {dl} | {paper_fname} | {miss} |")

    lines += [
        "",
        "## Miss Detail",
        "",
    ]

    for r in results:
        if not r.get("downloaded"):
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
            status = "(existing)" if not r.get("paper_created") else "(new)"
            lines.append(f"- `{r['paper_path']}` {status}")

    content = "\n".join(lines) + "\n"
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\nAcquisition log written: {log_path}")
    return log_path


def main():
    print("=" * 60)
    print("P1 Anchor Paper Acquisition — 2026-07-09")
    print("=" * 60)

    results = []

    for paper in P1_PAPERS:
        log_entry = {
            "paper_id": paper["id"],
            "title": paper["title"],
            "gap": paper["gap"],
        }
        try:
            log_entry = process_paper(paper, log_entry)
        except Exception as e:
            print(f"  UNEXPECTED ERROR for {paper['id']}: {e}")
            log_entry["downloaded"] = False
            log_entry["miss_reason"] = f"Unexpected error: {e}"
        results.append(log_entry)
        # Additional inter-paper delay
        time.sleep(2)

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    attempted = len(results)
    downloaded = sum(1 for r in results if r.get("downloaded"))
    misses = [r for r in results if not r.get("downloaded")]
    print(f"Attempted: {attempted}")
    print(f"Downloaded: {downloaded}")
    print(f"Misses: {len(misses)}")
    for r in misses:
        print(f"  MISS [{r['paper_id']}]: {r.get('miss_reason', 'unknown')}")

    # Write log
    log_path = write_acquisition_log(results)

    # Save raw results as JSON for reference
    json_path = LOG_DIR / "20260709-p1-acquisition-results.json"
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"Raw results: {json_path}")

    return downloaded, len(misses)


if __name__ == "__main__":
    main()
