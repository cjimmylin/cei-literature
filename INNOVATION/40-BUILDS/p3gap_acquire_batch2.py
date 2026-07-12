#!/usr/bin/env python3
"""
P3 Gap-Fill Acquisition — Batch 2 (2026-07-11)
Non-arXiv items that have verifiable open-access arXiv PDFs:
  S8a  = 2312.00886 (NLHF — Nash Learning from Human Feedback)
  S8b  = 2501.19266 (Jackpot! Alignment as Maximal Lottery)
  S13  = 2506.18032 (Sheshadri et al., compliance-gap / alignment-faking)
  S3a  = 2604.26130 (reward-lens library)
  S3b  = 2506.07326 (optimal/pessimal token probing of RMs)

Note on S3: the S3 ledger row bundles SAFER + reward-lens + token-probing.
SAFER (2507.00665) is already ingested. Acquiring S3a+S3b completes the bundle.

CRITICAL: tags field must be empty scalar `tags:` — NOT a block list.
"""

import os
import sys
import re
import time
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

VAULT_ROOT = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS")
PDFS_DIR = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs")
PAPERS_DIR = VAULT_ROOT / "papers"
EXTRACTS_DIR = VAULT_ROOT / "PDF Extracts"
LOG_DIR = VAULT_ROOT / "INNOVATION" / "40-BUILDS"

try:
    import requests
    import fitz
except ImportError as e:
    print(f"Missing dependency: {e}")
    sys.exit(1)

GAP_CODES = {
    "G-04": "AI Safety & Alignment",
    "G-10": "Preference Aggregation & Social Choice",
    "G-15": "AI Safety & Alignment",
}

P3_BATCH2_PAPERS = [
    {
        "id": "P3G-S8a",
        "row": "S8",
        "arxiv_id": "2312.00886",
        "ledger_claim": "NLHF — Nash Learning from Human Feedback (D · G-10)",
        "claim_keywords": ["nash", "learning", "human", "feedback", "reward", "preference", "align"],
        "gap": "G-10",
        "ethics_perspective_override": "Preference Aggregation & Social Choice",
    },
    {
        "id": "P3G-S8b",
        "row": "S8",
        "arxiv_id": "2501.19266",
        "ledger_claim": "Jackpot! Alignment as Maximal Lottery (D · G-10)",
        "claim_keywords": ["maximal", "lottery", "align", "social choice", "preference", "nash"],
        "gap": "G-10",
        "ethics_perspective_override": "Preference Aggregation & Social Choice",
    },
    {
        "id": "P3G-S13",
        "row": "S13",
        "arxiv_id": "2506.18032",
        "ledger_claim": "Sheshadri et al. 2025 compliance-gap across frontier models (E · G-15)",
        "claim_keywords": ["compliance", "gap", "frontier", "model", "align", "faking", "fake"],
        "gap": "G-15",
        "ethics_perspective_override": "AI Safety & Alignment",
    },
    {
        "id": "P3G-S3a",
        "row": "S3",
        "arxiv_id": "2604.26130",
        "ledger_claim": "reward-lens — mechanistic interpretability library for reward models (B · G-04)",
        "claim_keywords": ["reward", "lens", "mechanistic", "interpret", "reward model", "scalar"],
        "gap": "G-04",
        "ethics_perspective_override": "AI Safety & Alignment",
    },
    {
        "id": "P3G-S3b",
        "row": "S3",
        "arxiv_id": "2506.07326",
        "ledger_claim": "optimal/pessimal token probing of reward models (B · G-04)",
        "claim_keywords": ["optimal", "pessimal", "token", "reward", "probing", "probe", "interpret"],
        "gap": "G-04",
        "ethics_perspective_override": "AI Safety & Alignment",
    },
]


def fetch_arxiv_metadata(arxiv_id):
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    print(f"  Fetching metadata: {url}")
    try:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        ns = {"atom": "http://www.w3.org/2005/Atom"}
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
        return {"title": title, "authors": authors, "abstract": abstract, "year": year}
    except Exception as e:
        print(f"  ERROR fetching metadata: {e}")
        return None
    finally:
        time.sleep(3)


def verify_claim(fetched_title, abstract, claim_keywords):
    combined = (fetched_title + " " + abstract).lower()
    matched = [kw for kw in claim_keywords if kw.lower() in combined]
    if len(matched) >= 2:
        return True, matched, f"PASS — matched {len(matched)}/{len(claim_keywords)}: {matched}"
    else:
        return False, matched, f"MISMATCH — only {len(matched)}/{len(claim_keywords)}: {matched} in '{fetched_title}'"


def download_pdf(arxiv_id, dest_path):
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
                    print(f"  Saved PDF: {dest_path.name} ({len(content)//1024}KB)")
                    return True
                else:
                    print(f"  WARN: Not a PDF")
                    return False
            elif resp.status_code in (429, 503):
                wait = 2 ** attempt * 5
                print(f"  Rate-limited, waiting {wait}s...")
                time.sleep(wait)
            else:
                print(f"  HTTP error {resp.status_code}")
                return False
        except Exception as e:
            wait = 2 ** attempt * 3
            print(f"  Error (attempt {attempt+1}): {e}, retry in {wait}s")
            time.sleep(wait)
    return False


def extract_pdf(pdf_path, extract_path):
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
    """CRITICAL: tags must be empty scalar `tags:` — no block list."""
    arxiv_id = paper["arxiv_id"]
    year = meta.get("year") or 2025
    gap = paper["gap"]
    ethics_perspective = paper.get("ethics_perspective_override", "AI Safety & Alignment")
    authors_list = meta.get("authors", [])
    first_author = authors_list[0] if authors_list else "Unknown"
    authors_str = "; ".join(authors_list) if authors_list else "Unknown"
    title = meta.get("title", "")
    abstract = meta.get("abstract", "")
    pdf_wikilink = f"[[Lit-WS-PDFs/{year}/{pdf_path.name}]]" if pdf_path else ""
    extract_rel = f"PDF Extracts/{year}/{extract_path.name}" if extract_path else ""

    return f"""---
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


def process_paper(paper):
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
    print(f"[{paper_id} / row {row}] {paper['ledger_claim'][:60]}")
    print(f"  arXiv: {arxiv_id}")

    meta = fetch_arxiv_metadata(arxiv_id)
    if meta is None:
        log_entry.update({"status": "MISS", "miss_reason": "arXiv metadata fetch failed", "verify_result": "FAILED", "downloaded": False})
        print(f"  MISS: metadata fetch failed")
        return log_entry

    fetched_title = meta.get("title", "")
    log_entry["fetched_title"] = fetched_title
    log_entry["fetched_authors"] = "; ".join(meta.get("authors", [])[:3])
    log_entry["fetched_year"] = meta.get("year")

    print(f"  Title: '{fetched_title}'")
    print(f"  Authors: {', '.join(meta.get('authors', [])[:3])}")
    print(f"  Year: {meta.get('year')}")

    ok, matched, reason = verify_claim(fetched_title, meta.get("abstract", ""), paper["claim_keywords"])
    log_entry["verify_result"] = reason

    if not ok:
        log_entry.update({"status": "MISS", "miss_reason": f"Title/claim divergence: {reason}", "downloaded": False})
        print(f"  MISS (verify failed): {reason}")
        return log_entry

    print(f"  Verify: {reason}")

    file_stem, actual_year = build_file_stem(meta, paper)
    log_entry["file_stem"] = file_stem
    log_entry["actual_year"] = actual_year

    paper_path = PAPERS_DIR / f"{file_stem}.md"
    if paper_path.exists():
        print(f"  Paper record exists: {paper_path.name}")
        log_entry.update({"status": "HIT", "paper_note": "already existed", "paper_created": False, "paper_path": str(paper_path), "downloaded": True})
        return log_entry

    pdf_subdir = PDFS_DIR / str(actual_year)
    pdf_subdir.mkdir(parents=True, exist_ok=True)
    pdf_path = pdf_subdir / f"{file_stem}.pdf"

    if pdf_path.exists() and pdf_path.stat().st_size > 10000:
        print(f"  PDF exists: {pdf_path.name}")
        pdf_downloaded = True
    else:
        print(f"  Sleeping 5s before download...")
        time.sleep(5)
        pdf_downloaded = download_pdf(arxiv_id, pdf_path)

    log_entry["downloaded"] = pdf_downloaded
    log_entry["pdf_path"] = str(pdf_path) if pdf_downloaded else ""

    if not pdf_downloaded:
        log_entry.update({"status": "MISS", "miss_reason": "PDF download failed"})
        return log_entry

    extract_subdir = EXTRACTS_DIR / str(actual_year)
    extract_subdir.mkdir(parents=True, exist_ok=True)
    extract_path = extract_subdir / f"{file_stem}.md"

    if extract_path.exists():
        extracted = True
    else:
        extracted = extract_pdf(pdf_path, extract_path)

    log_entry["extracted"] = extracted
    log_entry["extract_path"] = str(extract_path) if extracted else ""

    yaml_text = make_paper_record(
        paper, meta,
        pdf_path if pdf_downloaded else None,
        extract_path if extracted else None
    )
    with open(paper_path, 'w', encoding='utf-8') as f:
        f.write(yaml_text)
    print(f"  Created paper record: {paper_path.name}")
    log_entry.update({"status": "HIT", "paper_created": True, "paper_path": str(paper_path)})
    return log_entry


def main():
    print("=" * 60)
    print("P3 Gap-Fill Acquisition Batch 2 — 2026-07-11")
    print("Items: S8a, S8b, S13, S3a, S3b")
    print("=" * 60)

    results = []
    for i, paper in enumerate(P3_BATCH2_PAPERS):
        try:
            result = process_paper(paper)
        except Exception as e:
            import traceback
            traceback.print_exc()
            result = {
                "paper_id": paper["id"], "row": paper["row"],
                "arxiv_id": paper["arxiv_id"], "status": "MISS",
                "downloaded": False, "miss_reason": f"Error: {e}",
            }
        results.append(result)
        if i < len(P3_BATCH2_PAPERS) - 1:
            print(f"  Inter-paper sleep 5s...")
            time.sleep(5)

    print("\n" + "=" * 60)
    print("BATCH 2 SUMMARY")
    print("=" * 60)
    hits = [r for r in results if r.get("status") == "HIT"]
    misses = [r for r in results if r.get("status") == "MISS"]
    print(f"Attempted: {len(results)}")
    print(f"HITs: {len(hits)}")
    print(f"MISSes: {len(misses)}")
    for r in misses:
        print(f"  MISS [{r['paper_id']}]: {r.get('miss_reason', '?')}")
        if r.get("fetched_title"):
            print(f"    Title: {r['fetched_title']}")

    json_path = LOG_DIR / "20260711-p3-gapfill-batch2-results.json"
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nRaw results: {json_path}")
    return results


if __name__ == "__main__":
    main()
