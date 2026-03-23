#!/usr/bin/env python3
"""
Batch extract text from PDFs using PyMuPDF.

Extracts full text from downloaded PDFs and saves as markdown files
in the PDF Extracts/ directory, matching the existing vault format.
Also updates the paper's pdf_extract field in YAML.

Usage: python3 PYTHON/batch_extract_pdfs.py START END [--dry-run]
  START: 1-indexed position in the list of papers needing extraction
  END: 1-indexed position (inclusive)
  --dry-run: show what would be extracted without doing it

Run from CEI-Lit-WS/ directory.
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

import fitz  # PyMuPDF

# Configuration
PAPERS_DIR = Path("papers")
EXTRACTS_DIR = Path("PDF Extracts")
VAULT_CONFIG = Path(".vault-config.json")


def get_pdfs_dir():
    """Get PDF storage directory from vault config."""
    config = json.loads(VAULT_CONFIG.read_text())
    return Path(config["pdf_path"])


def parse_date_arg(argv, default="20260207"):
    """Extract --date YYYYMMDD from argv, or return default."""
    for i, arg in enumerate(argv):
        if arg == '--date' and i + 1 < len(argv):
            return argv[i + 1]
    return default


def get_papers_needing_extraction(date_added="20260207"):
    """Find papers with local_pdf but no pdf_extract."""
    papers = []

    for f in sorted(PAPERS_DIR.glob("*.md")):
        content = f.read_text(encoding='utf-8')

        # Only process papers matching the target DATE_ADDED
        if f'DATE_ADDED: {date_added}' not in content:
            continue

        # Must have local_pdf
        local_match = re.search(r'local_pdf:\s*"?\[\[Lit-WS-PDFs/([^\]]+)\]\]', content)
        if not local_match:
            continue

        pdf_filename = local_match.group(1)

        # Check if extract already exists (root or year-based subdir)
        extract_path = EXTRACTS_DIR / (f.stem + ".md")
        if extract_path.exists():
            continue
        year_m = re.match(r'^(\d{4})-', f.stem)
        if year_m:
            year_extract = EXTRACTS_DIR / year_m.group(1) / (f.stem + ".md")
            if year_extract.exists():
                continue

        papers.append({
            'paper_path': f,
            'paper_name': f.name,
            'paper_stem': f.stem,
            'pdf_filename': pdf_filename,
        })

    return papers


def extract_pdf_text(pdf_path, output_path):
    """Extract text from a PDF and write to markdown extract file."""
    doc = fitz.open(pdf_path)
    num_pages = len(doc)

    # Build page content
    page_texts = []
    for page_num in range(num_pages):
        page = doc[page_num]
        text = page.get_text()
        page_texts.append(f"--- Page {page_num + 1} ---\n\n{text}")

    doc.close()

    # Get paper title from filename
    title = output_path.stem

    # Build extract file matching existing vault format
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

    output_path.write_text(content, encoding='utf-8')
    return num_pages


def update_pdf_extract_field(paper_path, extract_filename):
    """Set pdf_extract field in paper's YAML frontmatter.

    Uses REPLACE-first approach: if a blank pdf_extract: line exists (from import
    template), replace it in-place. Only falls back to insertion if no existing
    pdf_extract: line is found. This prevents duplicate YAML fields.
    """
    content = paper_path.read_text(encoding='utf-8')

    # Skip if already has a populated pdf_extract
    if 'pdf_extract:' in content and 'PDF Extracts/' in content:
        return

    extract_line = f'pdf_extract: "PDF Extracts/{extract_filename}"'

    # Strategy 1: Replace existing blank pdf_extract: line
    new_content, n = re.subn(
        r'^pdf_extract:\s*$',
        extract_line,
        content,
        count=1,
        flags=re.MULTILINE
    )
    if n > 0:
        paper_path.write_text(new_content, encoding='utf-8')
        return

    # Strategy 2: Replace existing pdf_extract: with any value
    new_content, n = re.subn(
        r'^pdf_extract:.*$',
        extract_line,
        content,
        count=1,
        flags=re.MULTILINE
    )
    if n > 0:
        paper_path.write_text(new_content, encoding='utf-8')
        return

    # Strategy 3: No pdf_extract: line exists — insert after local_pdf
    if 'local_pdf:' in content:
        content = re.sub(
            r'(local_pdf:\s*"?\[\[[^\]]*\]\]"?\n)',
            r'\1' + extract_line + '\n',
            content,
            count=1
        )
    elif 'external_pdf:' in content:
        content = re.sub(
            r'(external_pdf:\s*"[^"]*"\n)',
            r'\1' + extract_line + '\n',
            content,
            count=1
        )
    else:
        content = content.replace(
            'DATE_ADDED:',
            extract_line + '\nDATE_ADDED:'
        )

    paper_path.write_text(content, encoding='utf-8')


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 PYTHON/batch_extract_pdfs.py START END [--dry-run] [--date YYYYMMDD]")
        sys.exit(1)

    date_added = parse_date_arg(sys.argv)
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    dry_run = '--dry-run' in sys.argv
    print(f"Filtering by DATE_ADDED: {date_added}")

    pdfs_dir = get_pdfs_dir()
    if not pdfs_dir.exists():
        print(f"ERROR: PDF directory not found: {pdfs_dir}")
        sys.exit(1)

    if not EXTRACTS_DIR.exists():
        print(f"ERROR: Extracts directory not found: {EXTRACTS_DIR}")
        sys.exit(1)

    # Get papers needing extraction
    all_papers = get_papers_needing_extraction(date_added)
    print(f"Total papers needing extraction: {len(all_papers)}")

    # Select batch
    batch = all_papers[start - 1:end]
    print(f"Processing positions {start}-{end} ({len(batch)} papers)")
    if dry_run:
        print("*** DRY RUN MODE ***")
    print()

    extracted = 0
    skipped = 0
    failed = 0

    for i, paper in enumerate(batch):
        pdf_path = pdfs_dir / paper['pdf_filename']
        # Write directly to year-based subdir if possible
        year_m = re.match(r'^(\d{4})-', paper['paper_stem'])
        if year_m:
            year_dir = EXTRACTS_DIR / year_m.group(1)
            year_dir.mkdir(exist_ok=True)
            extract_path = year_dir / (paper['paper_stem'] + ".md")
        else:
            extract_path = EXTRACTS_DIR / (paper['paper_stem'] + ".md")

        # Verify PDF exists
        if not pdf_path.exists():
            print(f"  [{start + i:3d}] SKIP (no PDF): {paper['pdf_filename']}")
            skipped += 1
            continue

        if dry_run:
            size_kb = pdf_path.stat().st_size / 1024
            print(f"  [{start + i:3d}] DRY RUN ({size_kb:.0f}KB): {paper['paper_stem']}")
            extracted += 1
            continue

        try:
            num_pages = extract_pdf_text(pdf_path, extract_path)
            extract_size_kb = extract_path.stat().st_size / 1024
            print(f"  [{start + i:3d}] OK ({num_pages}pp, {extract_size_kb:.0f}KB): {paper['paper_stem'][:70]}")
            extracted += 1

            # Update paper's pdf_extract field (use year-prefixed path)
            extract_rel = extract_path.relative_to(EXTRACTS_DIR)
            try:
                update_pdf_extract_field(paper['paper_path'], str(extract_rel))
            except Exception as e:
                print(f"         WARNING: YAML update failed: {e}")

        except Exception as e:
            print(f"  [{start + i:3d}] FAIL: {paper['paper_stem'][:50]}... — {e}")
            failed += 1

    print(f"\n{'='*50}")
    print(f"BATCH {start}-{end} SUMMARY")
    print(f"  Extracted: {extracted}")
    print(f"  Skipped:   {skipped}")
    print(f"  Failed:    {failed}")
    print(f"{'='*50}")


if __name__ == '__main__':
    main()
