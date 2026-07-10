#!/usr/bin/env python3
"""
extract_background_pdfs.py — Extract text from BACKGROUND PDFs into markdown files.

Reads PDFs from Documents/, extracts text page-by-page using PyMuPDF (fitz),
writes markdown files to EXTRACT/, then moves originals to ORIG/.

Extract format follows the vault standard (PDF Extracts/):
  - YAML frontmatter: title, source_pdf, pages, extracted_at
  - Page-by-page text with --- Page N --- separators

Usage:
    python3 scripts/extract_background_pdfs.py                # All PDFs
    python3 scripts/extract_background_pdfs.py 1 20           # Range (1-indexed)
    python3 scripts/extract_background_pdfs.py --report       # Status report
    python3 scripts/extract_background_pdfs.py --dry-run      # Preview only
    python3 scripts/extract_background_pdfs.py --no-move      # Extract without moving originals

Run from BACKGROUND/ directory.
"""
from __future__ import annotations

import functools
import re
import shutil
import sys
import time
from datetime import datetime
from pathlib import Path

print = functools.partial(print, flush=True)

try:
    import fitz  # PyMuPDF
except ImportError:
    print("ERROR: PyMuPDF not installed. Run: pip install pymupdf")
    sys.exit(1)

BACKGROUND_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BACKGROUND_DIR / "Documents"
EXTRACT_DIR = BACKGROUND_DIR / "EXTRACT"
ORIG_DIR = BACKGROUND_DIR / "ORIG"


def extract_pdf_text(pdf_path: Path) -> tuple[list[str], int]:
    """Extract text from each page of a PDF. Returns (page_texts, total_pages)."""
    pages = []
    try:
        doc = fitz.open(str(pdf_path))
        total = len(doc)
        for page_num in range(total):
            page = doc[page_num]
            text = page.get_text("text")
            pages.append(text)
        doc.close()
        return pages, total
    except Exception as e:
        print(f"  ERROR extracting {pdf_path.name}: {e}")
        return [], 0


def write_extract(pdf_name: str, page_texts: list[str], total_pages: int,
                  output_dir: Path) -> Path:
    """Write extracted text as markdown file following vault format."""
    stem = Path(pdf_name).stem
    extract_path = output_dir / f"{stem}.md"

    # Build title from filename: "2024-Author-Short Title" -> "Short Title"
    parts = stem.split("-", 2)
    title = parts[2] if len(parts) >= 3 else stem
    title = title.replace("-", " ").strip()

    now = datetime.now().isoformat()

    lines = [
        "---",
        f'title: "{title} - PDF Extract"',
        f'source_pdf: "{pdf_name}"',
        f"pages: {total_pages}",
        f'extracted_at: "{now}"',
        "---",
        "",
        f"# PDF Extract: {title}",
        "",
        f"**Source PDF:** {pdf_name}",
        f"**Total Pages:** {total_pages}",
        "",
        "---",
        "",
        "## Content",
        "",
    ]

    for i, text in enumerate(page_texts, 1):
        lines.append(f"--- Page {i} ---")
        lines.append("")
        # Clean up text: normalize whitespace, remove null chars
        cleaned = text.replace("\x00", "").strip()
        if cleaned:
            lines.append(cleaned)
        else:
            lines.append("*[Page appears blank or contains only images]*")
        lines.append("")

    extract_path.write_text("\n".join(lines), encoding="utf-8")
    return extract_path


def get_pdfs_to_process() -> list[Path]:
    """Get sorted list of PDFs in Documents/ that haven't been extracted yet."""
    if not DOCS_DIR.exists():
        return []
    pdfs = sorted(DOCS_DIR.glob("*.pdf"))
    # Filter out already-extracted (check if extract exists)
    to_process = []
    for pdf in pdfs:
        extract = EXTRACT_DIR / f"{pdf.stem}.md"
        if not extract.exists():
            to_process.append(pdf)
    return to_process


def show_report():
    """Show extraction status."""
    pdfs = sorted(DOCS_DIR.glob("*.pdf")) if DOCS_DIR.exists() else []
    extracts = sorted(EXTRACT_DIR.glob("*.md")) if EXTRACT_DIR.exists() else []
    origs = sorted(ORIG_DIR.glob("*.pdf")) if ORIG_DIR.exists() else []

    # Also count PDFs that were already moved to ORIG
    all_pdfs = set(p.stem for p in pdfs) | set(p.stem for p in origs)
    extracted_stems = set(p.stem for p in extracts)
    not_extracted = all_pdfs - extracted_stems

    print(f"=== BACKGROUND PDF Extraction Report ===")
    print(f"PDFs in Documents/:    {len(pdfs)}")
    print(f"PDFs in ORIG/:         {len(origs)}")
    print(f"Extracts in EXTRACT/:  {len(extracts)}")
    print(f"Not yet extracted:     {len(not_extracted)}")

    if extracts:
        # Sample sizes
        sizes = [e.stat().st_size for e in extracts]
        avg_kb = sum(sizes) / len(sizes) / 1024
        total_mb = sum(sizes) / 1024 / 1024
        print(f"\nExtract sizes:")
        print(f"  Average:  {avg_kb:.1f} KB")
        print(f"  Total:    {total_mb:.1f} MB")

    if not_extracted:
        print(f"\nPending extraction:")
        for stem in sorted(not_extracted)[:10]:
            print(f"  {stem}")
        if len(not_extracted) > 10:
            print(f"  ... and {len(not_extracted) - 10} more")


def main():
    args = sys.argv[1:]

    if "--report" in args:
        show_report()
        return

    dry_run = "--dry-run" in args
    no_move = "--no-move" in args
    remaining = [a for a in args if not a.startswith("--")]

    start = int(remaining[0]) if remaining and remaining[0].isdigit() else 1
    end_arg = int(remaining[1]) if len(remaining) > 1 and remaining[1].isdigit() else None

    # Ensure output dirs exist
    EXTRACT_DIR.mkdir(exist_ok=True)
    ORIG_DIR.mkdir(exist_ok=True)

    pdfs = get_pdfs_to_process()
    total = len(pdfs)
    print(f"Found {total} PDFs to extract")

    if total == 0:
        print("Nothing to do.")
        return

    end = end_arg if end_arg is not None else total
    batch = pdfs[start - 1:end]
    print(f"Processing PDFs {start}-{end} ({len(batch)} PDFs)\n")

    extracted = 0
    moved = 0
    errors = 0

    for i, pdf_path in enumerate(batch, start):
        print(f"[{i}/{end}] {pdf_path.name}")

        if dry_run:
            size_kb = pdf_path.stat().st_size / 1024
            print(f"  DRY RUN — {size_kb:.0f} KB")
            continue

        # Extract
        page_texts, total_pages = extract_pdf_text(pdf_path)
        if not page_texts:
            print(f"  SKIP — extraction failed or empty")
            errors += 1
            continue

        # Write extract
        extract_path = write_extract(pdf_path.name, page_texts, total_pages, EXTRACT_DIR)
        extract_size = extract_path.stat().st_size / 1024
        print(f"  OK {total_pages} pages -> EXTRACT/{extract_path.name} ({extract_size:.0f} KB)")
        extracted += 1

        # Move original to ORIG (unless --no-move)
        if not no_move:
            orig_dest = ORIG_DIR / pdf_path.name
            shutil.move(str(pdf_path), str(orig_dest))
            moved += 1

    print(f"\n{'='*50}")
    print(f"Extracted: {extracted}  |  Moved to ORIG: {moved}  |  Errors: {errors}")


if __name__ == "__main__":
    main()
