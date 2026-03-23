#!/usr/bin/env python3
"""
Download Discovered PDFs — Batch Download + Extract + YAML Update

Reads logs/20260216-missing_pdfs_discovered.json (found: true entries),
downloads each PDF, extracts text with PyMuPDF, and updates paper YAML.

Handles filename renames from Session 85 Priority 1 (apply_author_fixes.py)
by building an old→new filename mapping from the author resolution JSON.

Usage:
    # Dry run (preview downloads)
    python download_discovered_pdfs.py --dry-run

    # Download all
    python download_discovered_pdfs.py

    # Resume from a specific index (1-indexed)
    python download_discovered_pdfs.py --start 10

Run from CEI-Lit-WS/ directory.
"""

import argparse
import functools
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import fitz  # PyMuPDF
import requests

# Force flush
print = functools.partial(print, flush=True)

# --- Path setup ---
SCRIPT_DIR = Path(__file__).parent.resolve()
WORKSPACE_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(WORKSPACE_ROOT / ".agent"))

from vault_config import (
    PAPERS_DIR, PDF_EXTRACTS_DIR, PDFS_DIR,
    LOGS_DIR, WORKSPACE_ROOT as WS_ROOT,
)

DISCOVERY_JSON = LOGS_DIR / "20260216-missing_pdfs_discovered.json"
AUTHORS_JSON = LOGS_DIR / "20260216-unknown_authors_resolved.json"
RESULTS_JSON = LOGS_DIR / "20260216-pdf_download_results.json"

# Rate limits
ARXIV_DELAY = 3.0
DEFAULT_DELAY = 1.0

# HTTP headers
HEADERS = {
    "User-Agent": "CEI-Literature-Vault/1.0 (academic research; mailto:research@example.com)",
    "Accept": "application/pdf,*/*",
}


def build_rename_map() -> Dict[str, str]:
    """Build old→new filename map from author resolution JSON."""
    if not AUTHORS_JSON.exists():
        return {}

    with open(AUTHORS_JSON, "r", encoding="utf-8") as f:
        authors = json.load(f)

    rename_map = {}
    for a in authors:
        if not a.get("resolved"):
            continue
        old_fn = a["filename"]
        first_author = a.get("first_author", "")
        if ", " in first_author:
            surname = first_author.split(",")[0].strip()
        elif "(" in first_author:
            m = re.search(r'\(([^)]+)\)', first_author)
            surname = m.group(1) if m else first_author.split()[0]
        elif first_author:
            surname = first_author.split()[0]
        else:
            surname = "Unknown"

        parts = old_fn.split("-", 2)
        if len(parts) >= 3:
            new_fn = f"{parts[0]}-{surname}-{parts[2]}"
        else:
            new_fn = old_fn

        if old_fn != new_fn:
            rename_map[old_fn] = new_fn

    return rename_map


def resolve_paper_filename(original_fn: str, rename_map: Dict[str, str]) -> str:
    """Resolve original filename to current filename (after renames)."""
    return rename_map.get(original_fn, original_fn)


def get_year_from_stem(stem: str) -> str:
    """Extract year from paper stem (e.g. '2024-Author-Title' → '2024')."""
    m = re.match(r'^(\d{4})-', stem)
    return m.group(1) if m else "0000"


def download_pdf(url: str, dest: Path, timeout: int = 60) -> Tuple[bool, str]:
    """Download a PDF from URL. Returns (success, error_message)."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=timeout, stream=True,
                           allow_redirects=True)
        resp.raise_for_status()

        # Check content type
        ct = resp.headers.get("Content-Type", "")
        if "html" in ct.lower() and "pdf" not in ct.lower():
            # Might be a landing page, not a PDF
            first_bytes = resp.content[:5]
            if not first_bytes.startswith(b"%PDF-"):
                return False, f"HTML response (not PDF): {ct}"

        content = resp.content

        # Verify PDF header
        if not content[:5].startswith(b"%PDF-"):
            return False, f"Invalid PDF header: {content[:20]!r}"

        # Write file
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(content)
        size_kb = len(content) / 1024
        return True, f"{size_kb:.0f}KB"

    except requests.exceptions.Timeout:
        return False, "Timeout"
    except requests.exceptions.HTTPError as e:
        return False, f"HTTP {e.response.status_code}"
    except Exception as e:
        return False, str(e)[:100]


def extract_pdf_text(pdf_path: Path, output_path: Path) -> int:
    """Extract text from PDF and write markdown extract. Returns page count."""
    doc = fitz.open(pdf_path)
    num_pages = len(doc)

    page_texts = []
    for page_num in range(num_pages):
        page = doc[page_num]
        text = page.get_text()
        page_texts.append(f"--- Page {page_num + 1} ---\n\n{text}")
    doc.close()

    title = output_path.stem
    now = datetime.now().isoformat()
    content = f"""---
title: "{title} - PDF Extract"
source_pdf: "{pdf_path.name}"
pages: {num_pages}
extracted_at: "{now}"
---

# PDF Extract: {title}

**Source PDF:** {pdf_path.name}
**Total Pages:** {num_pages}

---

## Content

```
{chr(10).join(page_texts)}
```
"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    return num_pages


def update_paper_yaml(paper_path: Path, pdf_wikilink: str, extract_rel: str) -> bool:
    """Update local_pdf and pdf_extract fields in paper YAML. Returns success."""
    content = paper_path.read_text(encoding="utf-8")

    # Update local_pdf
    # Handle: local_pdf: N/A, local_pdf: "", local_pdf: (empty), or no field
    new_content, n = re.subn(
        r'^local_pdf:.*$',
        f'local_pdf: "{pdf_wikilink}"',
        content, count=1, flags=re.MULTILINE
    )
    if n == 0:
        # Insert after external_pdf if exists
        new_content, n = re.subn(
            r'^(external_pdf:.*$)',
            rf'\1\nlocal_pdf: "{pdf_wikilink}"',
            content, count=1, flags=re.MULTILINE
        )
    content = new_content

    # Update pdf_extract
    extract_line = f'pdf_extract: "{extract_rel}"'
    # Check if already has populated pdf_extract
    if 'PDF Extracts/' in content:
        content, n = re.subn(
            r'^pdf_extract:.*$',
            extract_line,
            content, count=1, flags=re.MULTILINE
        )
    else:
        content, n = re.subn(
            r'^pdf_extract:.*$',
            extract_line,
            content, count=1, flags=re.MULTILINE
        )
        if n == 0:
            # Insert after local_pdf
            content = re.sub(
                r'^(local_pdf:.*$)',
                rf'\1\n{extract_line}',
                content, count=1, flags=re.MULTILINE
            )

    paper_path.write_text(content, encoding="utf-8")
    return True


def get_delay_for_url(url: str) -> float:
    """Return appropriate delay based on URL domain."""
    if "arxiv.org" in url:
        return ARXIV_DELAY
    return DEFAULT_DELAY


def main():
    parser = argparse.ArgumentParser(description="Download discovered PDFs")
    parser.add_argument("--dry-run", action="store_true", help="Preview without downloading")
    parser.add_argument("--start", type=int, default=1, help="Start index (1-indexed)")
    parser.add_argument("--only", type=str, default=None, help="Only process this filename")
    args = parser.parse_args()

    print("=" * 80)
    print(f"DOWNLOAD DISCOVERED PDFs {'(DRY RUN)' if args.dry_run else '(LIVE)'}")
    print("=" * 80)

    if not DISCOVERY_JSON.exists():
        print(f"ERROR: {DISCOVERY_JSON} not found")
        sys.exit(1)

    # Load discovery data
    with open(DISCOVERY_JSON, "r", encoding="utf-8") as f:
        all_entries = json.load(f)

    found = [e for e in all_entries if e.get("found")]
    print(f"Total discovered: {len(found)} PDFs")

    # Build rename map for filename resolution
    rename_map = build_rename_map()
    if rename_map:
        print(f"Loaded {len(rename_map)} filename renames from author fixes")

    # Apply start index
    found = found[args.start - 1:]
    if args.only:
        found = [e for e in found if e["filename"] == args.only or
                 rename_map.get(e["filename"]) == args.only]

    print(f"Processing {len(found)} entries (starting at #{args.start})")
    print()

    # Load existing results for resume support
    results = []
    if RESULTS_JSON.exists():
        with open(RESULTS_JSON, "r", encoding="utf-8") as f:
            results = json.load(f)
    already_done = {r["filename"] for r in results if r.get("success")}

    stats = {"downloaded": 0, "extracted": 0, "skipped": 0, "failed": 0, "already_done": 0}

    for i, entry in enumerate(found, args.start):
        old_fn = entry["filename"]
        current_fn = resolve_paper_filename(old_fn, rename_map)
        stem = current_fn.rsplit(".", 1)[0]
        year = get_year_from_stem(stem)
        url = entry["pdf_url"]
        source = entry.get("source", "unknown")

        # Skip if already downloaded
        if old_fn in already_done:
            stats["already_done"] += 1
            continue

        print(f"[{i}/{len(all_entries)}] {stem[:70]}")
        print(f"  URL: {url[:80]}")
        print(f"  Source: {source} | Year: {year}")

        paper_path = PAPERS_DIR / current_fn
        if not paper_path.exists():
            print(f"  SKIP: Paper file not found: {current_fn}")
            stats["skipped"] += 1
            results.append({"filename": old_fn, "current_filename": current_fn,
                           "success": False, "error": "Paper file not found"})
            continue

        pdf_dest = PDFS_DIR / year / f"{stem}.pdf"
        extract_dest = PDF_EXTRACTS_DIR / year / f"{stem}.md"
        pdf_wikilink = f"[[Lit-WS-PDFs/{year}/{stem}.pdf]]"
        extract_rel = f"PDF Extracts/{year}/{stem}.md"

        # Check if PDF already exists
        if pdf_dest.exists():
            print(f"  SKIP: PDF already exists at {pdf_dest.relative_to(PDFS_DIR)}")
            stats["skipped"] += 1
            results.append({"filename": old_fn, "current_filename": current_fn,
                           "success": True, "note": "Already exists"})
            continue

        if args.dry_run:
            print(f"  [DRY] Would download → {pdf_dest.relative_to(PDFS_DIR)}")
            stats["downloaded"] += 1
            continue

        # Download
        success, msg = download_pdf(url, pdf_dest)
        if not success:
            print(f"  FAIL: {msg}")
            stats["failed"] += 1
            results.append({"filename": old_fn, "current_filename": current_fn,
                           "success": False, "error": msg, "url": url})
        else:
            print(f"  Downloaded: {msg}")
            stats["downloaded"] += 1

            # Extract text
            try:
                pages = extract_pdf_text(pdf_dest, extract_dest)
                print(f"  Extracted: {pages} pages → {extract_dest.relative_to(PDF_EXTRACTS_DIR)}")
                stats["extracted"] += 1
            except Exception as e:
                print(f"  Extract FAIL: {e}")
                pages = 0

            # Update paper YAML
            try:
                update_paper_yaml(paper_path, pdf_wikilink, extract_rel)
                print(f"  YAML updated: local_pdf + pdf_extract")
            except Exception as e:
                print(f"  YAML FAIL: {e}")

            results.append({"filename": old_fn, "current_filename": current_fn,
                           "success": True, "size": msg, "pages": pages,
                           "url": url, "source": source})

        # Save results incrementally
        with open(RESULTS_JSON, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

        # Rate limit
        delay = get_delay_for_url(url)
        time.sleep(delay)

    # Final summary
    print(f"\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    print(f"  Downloaded:    {stats['downloaded']}")
    print(f"  Extracted:     {stats['extracted']}")
    print(f"  Skipped:       {stats['skipped']}")
    print(f"  Failed:        {stats['failed']}")
    print(f"  Already done:  {stats['already_done']}")

    if not args.dry_run:
        print(f"\n  Results saved: {RESULTS_JSON}")
        print(f"  Run validation: ../.venv/bin/python PYTHON/validate_all_papers.py")


if __name__ == "__main__":
    main()
