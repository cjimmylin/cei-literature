#!/usr/bin/env python3
"""
extract_background_pdfs.py — Extract text from BACKGROUND PDFs into markdown files.

For each PDF in Documents/:
  1. Extract text via PyMuPDF into EXTRACT/{basename}.md
  2. Move original PDF to ORIG/{basename}.pdf
  3. Update BACKGROUND-registry.json (local_document → ORIG/, add text_extract → EXTRACT/)

Usage:
    python3 scripts/extract_background_pdfs.py              # Extract all
    python3 scripts/extract_background_pdfs.py --dry-run    # Preview only

IMPORTANT: Future analysis should ONLY use EXTRACT/ files, never ORIG/.
ORIG/ is git-ignored to keep the repository small.
"""
from __future__ import annotations

import functools
import json
import os
import shutil
import sys
from datetime import date
from pathlib import Path

print = functools.partial(print, flush=True)

try:
    import fitz  # PyMuPDF
except ImportError:
    print("ERROR: PyMuPDF (fitz) not installed. Install with: pip install PyMuPDF")
    sys.exit(1)

BACKGROUND_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BACKGROUND_DIR / "Documents"
ORIG_DIR = BACKGROUND_DIR / "ORIG"
EXTRACT_DIR = BACKGROUND_DIR / "EXTRACT"
REGISTRY_PATH = BACKGROUND_DIR / "BACKGROUND-registry.json"
TODAY = date.today().strftime("%Y-%m-%d")


def extract_pdf_to_markdown(pdf_path: Path) -> tuple[str, int]:
    """Extract text from PDF, return (markdown_text, page_count)."""
    doc = fitz.open(str(pdf_path))
    page_count = len(doc)
    parts = []

    # Title from filename
    stem = pdf_path.stem
    parts.append(f"# {stem}\n")
    parts.append(f"**Source:** {pdf_path.name}")
    parts.append(f"**Pages:** {page_count}")
    parts.append(f"**Extracted:** {TODAY}")
    parts.append("\n---\n")

    for i, page in enumerate(doc, 1):
        text = page.get_text("text")
        if text.strip():
            parts.append(f"## Page {i}\n")
            parts.append(text.strip())
            parts.append("")  # blank line between pages

    doc.close()
    return "\n".join(parts), page_count


def main():
    dry_run = "--dry-run" in sys.argv

    # Ensure output dirs exist
    ORIG_DIR.mkdir(exist_ok=True)
    EXTRACT_DIR.mkdir(exist_ok=True)

    # Find PDFs in Documents/
    pdfs = sorted(DOCS_DIR.glob("*.pdf"))
    if not pdfs:
        print("No PDFs found in Documents/")
        return

    print(f"Found {len(pdfs)} PDFs in Documents/")

    # Load registry
    registry = []
    if REGISTRY_PATH.exists():
        with open(REGISTRY_PATH) as f:
            registry = json.load(f)

    # Build filename → registry index map
    reg_by_doc = {}
    for i, entry in enumerate(registry):
        local_doc = entry.get("local_document", "")
        basename = Path(local_doc).name if local_doc else ""
        if basename:
            reg_by_doc[basename] = i

    extracted = 0
    failed = 0
    total_pages = 0

    for pdf_path in pdfs:
        basename = pdf_path.name
        stem = pdf_path.stem
        extract_path = EXTRACT_DIR / f"{stem}.md"
        orig_path = ORIG_DIR / basename

        print(f"\n[{extracted + failed + 1}/{len(pdfs)}] {basename}")

        if dry_run:
            print(f"  DRY RUN: Would extract → {extract_path.name}")
            print(f"  DRY RUN: Would move → ORIG/{basename}")
            extracted += 1
            continue

        # Extract text
        try:
            markdown_text, page_count = extract_pdf_to_markdown(pdf_path)
            total_pages += page_count

            # Write extract
            with open(extract_path, "w", encoding="utf-8") as f:
                f.write(markdown_text)

            print(f"  Extracted {page_count} pages → {extract_path.name}")

            # Move original to ORIG/
            shutil.move(str(pdf_path), str(orig_path))
            print(f"  Moved → ORIG/{basename}")

            # Update registry
            if basename in reg_by_doc:
                idx = reg_by_doc[basename]
                registry[idx]["local_document"] = f"ORIG/{basename}"
                registry[idx]["text_extract"] = f"EXTRACT/{stem}.md"
                registry[idx]["extract_pages"] = page_count

            extracted += 1

        except Exception as e:
            print(f"  ERROR: {e}")
            failed += 1

    if not dry_run:
        # Save updated registry atomically
        tmp_path = REGISTRY_PATH.with_suffix(f".tmp.{os.getpid()}.json")
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(registry, f, indent=2, ensure_ascii=False)
            f.write("\n")
        os.replace(str(tmp_path), str(REGISTRY_PATH))
        print(f"\nRegistry updated: {REGISTRY_PATH}")

    # Summary
    print(f"\n{'='*60}")
    print(f"EXTRACTION SUMMARY")
    print(f"{'='*60}")
    print(f"PDFs processed:  {extracted + failed}")
    print(f"Extracted:       {extracted}")
    print(f"Failed:          {failed}")
    print(f"Total pages:     {total_pages}")
    print(f"Extracts in:     EXTRACT/")
    print(f"Originals in:    ORIG/")
    if not dry_run:
        print(f"Documents/ should now be empty (PDFs moved to ORIG/)")


if __name__ == "__main__":
    main()
