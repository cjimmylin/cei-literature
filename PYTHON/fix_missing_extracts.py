#!/usr/bin/env python3
"""
Fix papers with PDFs but missing/broken PDF extracts.

Three repair modes:
  Part A: Fix wikilink corruption in pdf_extract field ([[Author]] → Author)
          + create missing extract files from PDFs
  Part B: Fix wrong-year directory (0000/ → correct year/) for extract files
          + move extract files to correct year subdir
  Part C: Comprehensive gap check — find all papers with local_pdf but
          missing or non-existent extract

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/fix_missing_extracts.py --dry-run
    ../.venv/bin/python PYTHON/fix_missing_extracts.py

Safety:
    - NO deletions — uses shutil.move() for Part B
    - YAML edits use re.subn() — never parse→rebuild round-trip
    - Dry-run mode prints what would happen without modifying anything
"""

import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None

# Configuration — run from CEI-Lit-WS/
PAPERS_DIR = Path("papers")
EXTRACTS_DIR = Path("PDF Extracts")
VAULT_CONFIG = Path(".vault-config.json")


def get_pdfs_dir():
    """Get PDF storage directory from vault config."""
    config = json.loads(VAULT_CONFIG.read_text())
    return Path(config["pdf_path"])


def extract_pdf_text(pdf_path, output_path):
    """Extract text from a PDF and write to markdown extract file.

    Follows the same format as batch_extract_pdfs.py.
    """
    if fitz is None:
        raise ImportError("PyMuPDF (fitz) not installed")

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
    output_path.write_text(content, encoding='utf-8')
    return num_pages


def resolve_pdf_for_paper(paper_path, pdfs_dir):
    """Find the PDF file for a paper by reading its local_pdf field."""
    content = paper_path.read_text(encoding='utf-8')

    # Extract PDF filename from local_pdf wikilink
    m = re.search(r'local_pdf:\s*"?\[\[Lit-WS-PDFs/([^\]]+)\]\]', content)
    if not m:
        return None

    pdf_filename = m.group(1)

    # Try year-based subdir first
    year_m = re.match(r'^(\d{4})/', pdf_filename)
    if year_m:
        candidate = pdfs_dir / pdf_filename
        if candidate.exists():
            return candidate

    # Try flat
    candidate = pdfs_dir / Path(pdf_filename).name
    if candidate.exists():
        return candidate

    # Try year from paper stem
    year_m = re.match(r'^(\d{4})-', paper_path.stem)
    if year_m:
        candidate = pdfs_dir / year_m.group(1) / Path(pdf_filename).name
        if candidate.exists():
            return candidate

    return None


def fix_wikilink_corruption(dry_run=False):
    """Part A: Fix [[Author]] corruption in pdf_extract fields + create extracts."""
    print("=" * 60)
    print("PART A: Fix wikilink corruption in pdf_extract fields")
    print("=" * 60)

    pdfs_dir = get_pdfs_dir()
    fixed = 0
    extracted = 0
    errors = []

    for paper_path in sorted(PAPERS_DIR.glob("*.md")):
        content = paper_path.read_text(encoding='utf-8')

        # Check for [[ in pdf_extract field
        m = re.search(r'^pdf_extract:\s*"([^"]*\[\[[^\]]*\]\][^"]*)"', content, re.MULTILINE)
        if not m:
            continue

        corrupted_value = m.group(1)
        clean_value = corrupted_value.replace("[[", "").replace("]]", "")

        print(f"\n  Paper: {paper_path.name}")
        print(f"    Corrupted: {corrupted_value}")
        print(f"    Fixed:     {clean_value}")

        if not dry_run:
            # Fix YAML field using safe re.subn
            new_content, n = re.subn(
                r'^(pdf_extract:\s*")' + re.escape(corrupted_value) + '"',
                r'\g<1>' + clean_value + '"',
                content,
                count=1,
                flags=re.MULTILINE
            )
            if n > 0:
                paper_path.write_text(new_content, encoding='utf-8')
                fixed += 1
                print(f"    YAML fixed.")
            else:
                errors.append(f"Failed to fix YAML for {paper_path.name}")
                print(f"    ERROR: YAML fix failed!")
                continue
        else:
            fixed += 1

        # Check if extract file exists at the clean path
        extract_path = EXTRACTS_DIR / clean_value.replace("PDF Extracts/", "")
        if extract_path.exists():
            print(f"    Extract already exists: {extract_path}")
            continue

        # Need to create extract from PDF
        pdf_path = resolve_pdf_for_paper(paper_path, pdfs_dir)
        if not pdf_path:
            errors.append(f"No PDF found for {paper_path.name}")
            print(f"    WARNING: No PDF found — cannot create extract")
            continue

        print(f"    PDF: {pdf_path.name}")

        if not dry_run:
            try:
                extract_path.parent.mkdir(parents=True, exist_ok=True)
                num_pages = extract_pdf_text(pdf_path, extract_path)
                size_kb = extract_path.stat().st_size / 1024
                print(f"    Extracted: {num_pages} pages, {size_kb:.0f} KB")
                extracted += 1
            except Exception as e:
                errors.append(f"Extract failed for {paper_path.name}: {e}")
                print(f"    ERROR extracting: {e}")
        else:
            print(f"    DRY RUN: would extract from {pdf_path.name}")
            extracted += 1

    print(f"\n  Part A Summary: {fixed} YAML fixed, {extracted} extracts created")
    if errors:
        print(f"  Errors ({len(errors)}):")
        for e in errors:
            print(f"    - {e}")
    return errors


def fix_wrong_year_directory(dry_run=False):
    """Part B: Move extracts from 0000/ to correct year subdir + update YAML."""
    print("\n" + "=" * 60)
    print("PART B: Fix wrong-year directory (0000/ → correct year/)")
    print("=" * 60)

    moved = 0
    yaml_fixed = 0
    skipped = 0
    errors = []

    for paper_path in sorted(PAPERS_DIR.glob("*.md")):
        content = paper_path.read_text(encoding='utf-8')

        # Check for pdf_extract pointing to 0000/
        m = re.search(r'^pdf_extract:\s*"PDF Extracts/0000/([^"]+)"', content, re.MULTILINE)
        if not m:
            continue

        extract_filename = m.group(1)

        # Determine correct year from paper stem
        year_m = re.match(r'^(\d{4})-', paper_path.stem)
        if not year_m or year_m.group(1) == '0000':
            # Legitimate 0000- paper (e.g., 0000-project-*)
            skipped += 1
            continue

        correct_year = year_m.group(1)
        old_path = EXTRACTS_DIR / "0000" / extract_filename
        new_path = EXTRACTS_DIR / correct_year / extract_filename

        old_yaml_value = f"PDF Extracts/0000/{extract_filename}"
        new_yaml_value = f"PDF Extracts/{correct_year}/{extract_filename}"

        print(f"\n  Paper: {paper_path.name}")
        print(f"    Move: 0000/{extract_filename}")
        print(f"      →   {correct_year}/{extract_filename}")

        if not old_path.exists():
            # Check if it's already in the correct place
            if new_path.exists():
                print(f"    Already at correct path — just fixing YAML")
                if not dry_run:
                    new_content, n = re.subn(
                        r'^pdf_extract:\s*"' + re.escape(old_yaml_value) + '"',
                        f'pdf_extract: "{new_yaml_value}"',
                        content,
                        count=1,
                        flags=re.MULTILINE
                    )
                    if n > 0:
                        paper_path.write_text(new_content, encoding='utf-8')
                        yaml_fixed += 1
                        print(f"    YAML fixed.")
                    else:
                        errors.append(f"YAML fix failed for {paper_path.name}")
                else:
                    yaml_fixed += 1
                continue

            errors.append(f"Extract not found at {old_path} for {paper_path.name}")
            print(f"    WARNING: Extract file not found in 0000/ or {correct_year}/")
            continue

        if not dry_run:
            # Ensure target directory exists
            new_path.parent.mkdir(parents=True, exist_ok=True)

            # Move file (safe — no deletion)
            shutil.move(str(old_path), str(new_path))
            moved += 1
            print(f"    File moved.")

            # Update YAML
            # Re-read content in case Part A modified it
            content = paper_path.read_text(encoding='utf-8')
            new_content, n = re.subn(
                r'^pdf_extract:\s*"' + re.escape(old_yaml_value) + '"',
                f'pdf_extract: "{new_yaml_value}"',
                content,
                count=1,
                flags=re.MULTILINE
            )
            if n > 0:
                paper_path.write_text(new_content, encoding='utf-8')
                yaml_fixed += 1
                print(f"    YAML fixed.")
            else:
                errors.append(f"YAML fix failed for {paper_path.name}")
                print(f"    ERROR: YAML fix failed!")
        else:
            moved += 1
            yaml_fixed += 1
            print(f"    DRY RUN: would move + fix YAML")

    print(f"\n  Part B Summary: {moved} files moved, {yaml_fixed} YAML fixed, {skipped} skipped (legitimate 0000-)")
    if errors:
        print(f"  Errors ({len(errors)}):")
        for e in errors:
            print(f"    - {e}")
    return errors


def gap_check():
    """Part C: Find all papers with local_pdf but missing/non-existent extract."""
    print("\n" + "=" * 60)
    print("PART C: Comprehensive gap check")
    print("=" * 60)

    gaps = []
    total_with_pdf = 0

    for paper_path in sorted(PAPERS_DIR.glob("*.md")):
        content = paper_path.read_text(encoding='utf-8')

        # Must have local_pdf (not N/A)
        if 'local_pdf:' not in content:
            continue

        pdf_m = re.search(r'local_pdf:\s*"?\[\[Lit-WS-PDFs/', content)
        if not pdf_m:
            continue

        total_with_pdf += 1

        # Check pdf_extract field
        extract_m = re.search(r'^pdf_extract:\s*"([^"]+)"', content, re.MULTILINE)

        if not extract_m:
            gaps.append({
                'paper': paper_path.name,
                'issue': 'no pdf_extract field',
            })
            continue

        extract_value = extract_m.group(1)

        # Check if the referenced file exists on disk
        # Strip "PDF Extracts/" prefix if present, then resolve against EXTRACTS_DIR
        if extract_value.startswith("PDF Extracts/"):
            rel_path = extract_value[len("PDF Extracts/"):]
        else:
            rel_path = extract_value

        extract_path = EXTRACTS_DIR / rel_path

        if not extract_path.exists():
            gaps.append({
                'paper': paper_path.name,
                'issue': f'extract file not found: {extract_path}',
            })

    print(f"\n  Total papers with local_pdf: {total_with_pdf}")
    print(f"  Papers with gaps: {len(gaps)}")

    if gaps:
        print(f"\n  Remaining gaps:")
        for g in gaps:
            print(f"    {g['paper']}")
            print(f"      → {g['issue']}")
    else:
        print("  No gaps found — all papers with PDFs have valid extracts!")

    return gaps


def main():
    dry_run = '--dry-run' in sys.argv

    if dry_run:
        print("*** DRY RUN MODE — no files will be modified ***\n")
    else:
        print("*** LIVE MODE — files will be modified ***\n")

    # Verify we're in the right directory
    if not PAPERS_DIR.exists():
        print(f"ERROR: {PAPERS_DIR} not found. Run from CEI-Lit-WS/")
        sys.exit(1)
    if not EXTRACTS_DIR.exists():
        print(f"ERROR: {EXTRACTS_DIR} not found.")
        sys.exit(1)

    errors_a = fix_wikilink_corruption(dry_run)
    errors_b = fix_wrong_year_directory(dry_run)
    gaps = gap_check()

    # Final summary
    print("\n" + "=" * 60)
    print("FINAL SUMMARY")
    print("=" * 60)
    total_errors = len(errors_a) + len(errors_b)
    print(f"  Part A errors: {len(errors_a)}")
    print(f"  Part B errors: {len(errors_b)}")
    print(f"  Remaining gaps: {len(gaps)}")
    if total_errors > 0:
        print(f"\n  *** {total_errors} errors need attention ***")
    if not gaps and total_errors == 0:
        print("\n  All clear!")


if __name__ == '__main__':
    main()
