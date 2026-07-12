#!/usr/bin/env python3
"""
P3 Gap-Fill Acquisition Script — 2026-07-11
Acquires 5 arXiv items that remained [⚠] after ledger-v1 phase-2 pass:
  S9  = 2501.09254 (clone-robustness)
  S15 = 2502.08640 (utility engineering, NeurIPS 2025 spotlight)
  W5  = 2510.06370 (EVALUESTEER, value+style profiles)
  W26 = 2602.20710 (counterfactual-simulation faithfulness training)
  W32 = 2604.09588 (identity-file architectures)

Non-negotiable rules:
- VERIFY METADATA FIRST: query arXiv API, compare title against ledger claim.
  On mismatch → log MISS, do NOT download, do NOT guess alternative IDs.
- 5-second sleep between downloads; exponential backoff on HTTP errors.
- PDFs go to ../Lit-WS-PDFs/YYYY/YYYY-Author-Short Title.pdf
- tags: YAML field must be an EMPTY SCALAR — `tags: ` with nothing after it.
  (Validator rejects block lists; lesson from 2026-07-10 batch failures.)
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
# Gap → ethics_perspective mapping
# -----------------------------------------------------------------------
GAP_CODES = {
    "G-04": "AI Safety & Alignment",
    "G-13": "AI Safety & Alignment",
    "G-14": "AI Safety & Alignment",
    "G-15": "AI Safety & Alignment",
    "G-18": "Multi-Agent Value Dynamics",
    "G-23": "Value Formation & Emergent Misalignment",
}


def get_ethics_perspective(gap_str):
    gaps = [g.strip() for g in gap_str.split("/")]
    for g in gaps:
        if not g.startswith("G-"):
            g = "G-" + g
        if g in GAP_CODES:
            return GAP_CODES[g]
    return "AI Safety & Alignment"


# -----------------------------------------------------------------------
# P3 gap items to acquire
# -----------------------------------------------------------------------
P3_GAP_PAPERS = [
    {
        "id": "P3G-S9",
        "row": "S9",
        "arxiv_id": "2501.09254",
        "ledger_claim": "clone-robustness (D · G-10)",
        "claim_keywords": ["clone", "robust", "alignment", "preference", "social choice", "aggregat"],
        "gap": "G-10",
        # G-10 = Preference Aggregation & Social Choice
        "ethics_perspective_override": "Preference Aggregation & Social Choice",
    },
    {
        "id": "P3G-S15",
        "row": "S15",
        "arxiv_id": "2502.08640",
        "ledger_claim": "utility engineering, NeurIPS 2025 spotlight (E · G-23)",
        "claim_keywords": ["utility", "engineer", "value", "behavior", "prefer", "misalign", "align"],
        "gap": "G-23",
        "ethics_perspective_override": "Value Formation & Emergent Misalignment",
    },
    {
        "id": "P3G-W5",
        "row": "W5",
        "arxiv_id": "2510.06370",
        "ledger_claim": "EVALUESTEER — value+style steering benchmark, <75% on profiles (B · G-04)",
        "claim_keywords": ["evaluesteer", "steer", "value", "style", "profile", "eval", "align"],
        "gap": "G-04",
        "ethics_perspective_override": "AI Safety & Alignment",
    },
    {
        "id": "P3G-W26",
        "row": "W26",
        "arxiv_id": "2602.20710",
        "ledger_claim": "counterfactual-simulation faithfulness training (E · G-13)",
        "claim_keywords": ["counterfactual", "faithful", "chain", "thought", "reasoning", "monit", "train", "simul"],
        "gap": "G-13",
        "ethics_perspective_override": "AI Safety & Alignment",
    },
    {
        "id": "P3G-W32",
        "row": "W32",
        "arxiv_id": "2604.09588",
        "ledger_claim": "identity-file architectures (F · G-18)",
        "claim_keywords": ["identity", "file", "architect", "agent", "memory", "persona", "character"],
        "gap": "G-18",
        "ethics_perspective_override": "Multi-Agent Value Dynamics",
    },
]


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
        title_el = entry.find("atom:title", ns)
        title = " ".join(title_el.text.split()) if title_el is not None else ""
        authors = []
        for auth_el in entry.findall("atom:author", ns):
            name_el = auth_el.find("atom:name", ns)
            if name_el is not None:
                authors.append(name_el.text.strip())
        summ_el = entry.find("atom:summary", ns)
        abstract = " ".join(summ_el.text.split()) if summ_el is not None else ""
        pub_el = entry.find("atom:published", ns)
        year = int(pub_el.text[:4]) if pub_el is not None else None
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
        time.sleep(3)


def verify_title_against_claim(fetched_title, abstract, claim_keywords):
    """
    Check whether fetched title+abstract match the ledger's claim keywords.
    Returns (ok: bool, matched_keywords: list, reason: str)
    """
    combined = (fetched_title + " " + abstract).lower()
    matched = [kw for kw in claim_keywords if kw.lower() in combined]
    if len(matched) >= 2:
        return True, matched, f"PASS — matched {len(matched)}/{len(claim_keywords)} keywords: {matched}"
    else:
        return False, matched, f"MISMATCH — only {len(matched)}/{len(claim_keywords)} keywords matched: {matched} in title '{fetched_title}'"


def download_pdf(arxiv_id, dest_path):
    """Download PDF from arXiv with retry/exponential backoff."""
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    print(f"  Downloading PDF: {url}")
    for attempt in range(4):
        try:
            resp = requests.get(url, timeout=60, stream=True)
            if resp.status_code == 200:
                content = resp.content
                if content[:4] == b'%PDF':
                    with open(dest_path, 'wb') as f:
                        f.write(content)
                    print(f"  Saved PDF: {dest_path} ({len(content)//1024}KB)")
                    return True
                else:
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


def build_file_stem(meta, paper):
    """Build YYYY-Author-Short Title file stem from metadata."""
    year = meta.get("year") or 2025
    authors = meta.get("authors", [])
    first_author = authors[0] if authors else "Unknown"
    surname = first_author.split()[-1] if first_author else "Unknown"
    surname = re.sub(r'[^\w\s-]', '', surname).strip()

    title = meta.get("title", "")
    stop = {"a", "an", "the", "of", "in", "on", "at", "to", "for", "and", "or",
            "with", "by", "from", "is", "are", "that", "this", "its", "it"}
    words = [w for w in title.split() if w.lower() not in stop]
    short = " ".join(words[:5])
    short = re.sub(r'[^\w\s-]', '', short).strip()

    return f"{year}-{surname}-{short}", year


def make_paper_record(paper, meta, pdf_path, extract_path):
    """
    Build a paper .md file with full YAML frontmatter.
    CRITICAL: tags: must be empty scalar (no block list) — validator rule 2026-07-10.
    """
    arxiv_id = paper["arxiv_id"]
    year = meta.get("year") or 2025
    gap = paper["gap"]
    ethics_perspective = paper.get("ethics_perspective_override") or get_ethics_perspective(gap)

    authors_list = meta.get("authors", [])
    first_author = authors_list[0] if authors_list else "Unknown"
    authors_str = "; ".join(authors_list) if authors_list else "Unknown"

    title = meta.get("title", "")
    abstract = meta.get("abstract", "")

    pdf_wikilink = f"[[Lit-WS-PDFs/{year}/{pdf_path.name}]]" if pdf_path else ""
    extract_rel = f"PDF Extracts/{year}/{extract_path.name}" if extract_path else ""

    # CRITICAL: tags must be an empty scalar (not a block list)
    # Correct form: `tags: ` (trailing space, nothing after)
    yaml_content = f"""---
key: INNOVATION-{paper['id'].replace('-', '')}
type: preprint
short_title: "{title.replace('"', "'")}"
year: {year}
first_author: "[[{first_author}]]"
authors: "{authors_str}"
url: "https://arxiv.org/abs/{arxiv_id}"
external_pdf: "https://arxiv.org/pdf/{arxiv_id}.pdf"
abstract: "{abstract.replace('"', "'")}"
ethics_overall: No
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
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Not specified"
data_metrics: "Not specified"
newtags: "{ethics_perspective}"
key_contribution:
significance:
paper_summary:
local_pdf: "{pdf_wikilink}"
pdf_extract: "{extract_rel}"
tags:
Human View:
Human View Date:
Human View note:
Not AI:
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


def process_p3_gap_paper(paper):
    """Full pipeline for one P3 gap item: verify → download → extract → record."""
    arxiv_id = paper["arxiv_id"]
    paper_id = paper["id"]
    row = paper["row"]

    log_entry = {
        "paper_id": paper_id,
        "row": row,
        "arxiv_id": arxiv_id,
        "ledger_claim": paper["ledger_claim"],
        "gap": paper["gap"],
    }

    print(f"\n{'='*60}")
    print(f"[{paper_id} / row {row}] {paper['ledger_claim']}")
    print(f"  arXiv: {arxiv_id}")

    # Step 1: Fetch metadata (MANDATORY — verify first)
    meta = fetch_arxiv_metadata(arxiv_id)
    if meta is None:
        log_entry["status"] = "MISS"
        log_entry["miss_reason"] = "arXiv metadata fetch failed — ID may not exist"
        log_entry["verify_result"] = "FAILED — no metadata returned"
        log_entry["downloaded"] = False
        print(f"  MISS: metadata fetch failed")
        return log_entry

    fetched_title = meta.get("title", "")
    log_entry["fetched_title"] = fetched_title
    log_entry["fetched_authors"] = "; ".join(meta.get("authors", [])[:3])
    log_entry["fetched_year"] = meta.get("year")

    print(f"  Fetched title: '{fetched_title}'")
    print(f"  Authors: {', '.join(meta.get('authors', [])[:3])}")
    print(f"  Year: {meta.get('year')}")

    # Step 2: Verify title/abstract against ledger claim
    ok, matched, reason = verify_title_against_claim(
        fetched_title, meta.get("abstract", ""), paper["claim_keywords"]
    )
    log_entry["verify_result"] = reason

    if not ok:
        log_entry["status"] = "MISS"
        log_entry["miss_reason"] = f"Title/claim divergence: {reason}"
        log_entry["downloaded"] = False
        print(f"  MISS (verification failed): {reason}")
        return log_entry

    print(f"  Verify: {reason}")

    # Step 3: Build file stem from actual metadata
    file_stem, actual_year = build_file_stem(meta, paper)
    log_entry["file_stem"] = file_stem
    log_entry["actual_year"] = actual_year

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

    # Step 5: Download PDF (5-second inter-download sleep)
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


def main():
    print("=" * 60)
    print("P3 Gap-Fill Acquisition — 2026-07-11")
    print("Target items: S9, S15, W5, W26, W32 (arXiv)")
    print("=" * 60)

    results = []
    papers = P3_GAP_PAPERS[:]

    for i, paper in enumerate(papers):
        try:
            result = process_p3_gap_paper(paper)
        except Exception as e:
            import traceback
            print(f"  UNEXPECTED ERROR for {paper['id']}: {e}")
            traceback.print_exc()
            result = {
                "paper_id": paper["id"],
                "row": paper["row"],
                "arxiv_id": paper["arxiv_id"],
                "status": "MISS",
                "downloaded": False,
                "miss_reason": f"Unexpected error: {e}",
            }
        results.append(result)

        # 5-second inter-paper sleep (except after last)
        if i < len(papers) - 1:
            print(f"  Inter-paper sleep 5s...")
            time.sleep(5)

    # Summary
    print("\n" + "=" * 60)
    print("P3 GAP-FILL SUMMARY")
    print("=" * 60)
    hits = [r for r in results if r.get("status") == "HIT"]
    misses = [r for r in results if r.get("status") == "MISS"]
    print(f"Attempted: {len(results)}")
    print(f"HITs: {len(hits)}")
    print(f"MISSes: {len(misses)}")
    for r in misses:
        print(f"  MISS [{r['paper_id']}] row {r.get('row', '?')}: {r.get('miss_reason', 'unknown')}")
        if r.get("fetched_title"):
            print(f"    Fetched title: {r['fetched_title']}")

    # Save raw results
    json_path = LOG_DIR / "20260711-p3-gapfill-results.json"
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nRaw results: {json_path}")

    return results


if __name__ == "__main__":
    main()
