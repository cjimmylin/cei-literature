#!/usr/bin/env python3
"""
Rename 4 papers that have [[Unknown]] in filenames but real authors in YAML.
Renames: paper file, extract file, and updates YAML local_pdf/pdf_extract fields.
"""

import re
from pathlib import Path

PAPERS_DIR = Path("papers")
PDF_DIR = Path("PDFs")
EXTRACT_DIR = Path("PDF Extracts")

# The 4 papers to fix: (old_stem, year, new_last_name)
PAPERS = [
    ("2025-[[Unknown]]-Alif Advancing Urdu Large Language Models", "2025", "Shafique"),
    ("2025-[[Unknown]]-Creating and Evaluating Code-Mixed Nepali-English and", "2025", "Pandey"),
    ("2026-[[Unknown]]-Qalb Largest State-of-the-Art Urdu Large Language", "2026", "Hassan"),
    ("2026-[[Unknown]]-UrduBench An Urdu Reasoning Benchmark using", "2026", "Shafique"),
]


def make_new_stem(old_stem: str, new_last_name: str) -> str:
    """Replace [[Unknown]] with the author's last name."""
    return old_stem.replace("[[Unknown]]", new_last_name)


def update_yaml_field(content: str, field: str, old_val: str, new_val: str) -> str:
    """Safe regex replacement of a YAML field value."""
    old_escaped = re.escape(old_val)
    pattern = rf'^({re.escape(field)}:\s*).*{old_escaped}.*$'
    # Build the new line
    new_line_val = new_val
    replacement = rf'\g<1>"{new_line_val}"'
    result, count = re.subn(pattern, replacement, content, count=1, flags=re.MULTILINE)
    if count == 0:
        print(f"  WARNING: Could not find {field} containing '{old_val}'")
    return result


def main():
    for old_stem, year, new_last_name in PAPERS:
        new_stem = make_new_stem(old_stem, new_last_name)
        print(f"\n{'='*60}")
        print(f"  {old_stem}")
        print(f"  → {new_stem}")
        print(f"{'='*60}")

        # 1. Rename paper file
        old_paper = PAPERS_DIR / f"{old_stem}.md"
        new_paper = PAPERS_DIR / f"{new_stem}.md"
        if old_paper.exists():
            old_paper.rename(new_paper)
            print(f"  Paper: renamed")
        else:
            print(f"  Paper: NOT FOUND - {old_paper}")
            continue

        # 2. Rename extract file
        old_extract = EXTRACT_DIR / year / f"{old_stem}.md"
        new_extract = EXTRACT_DIR / year / f"{new_stem}.md"
        if old_extract.exists():
            old_extract.rename(new_extract)
            print(f"  Extract: renamed")
        else:
            print(f"  Extract: NOT FOUND (skipping)")

        # 3. Rename PDF file (if exists)
        old_pdf = PDF_DIR / year / f"{old_stem}.pdf"
        new_pdf = PDF_DIR / year / f"{new_stem}.pdf"
        if old_pdf.exists():
            old_pdf.rename(new_pdf)
            print(f"  PDF: renamed")
        else:
            print(f"  PDF: not present (expected)")

        # 4. Update YAML fields in the new paper file
        content = new_paper.read_text(encoding='utf-8')

        # Update local_pdf
        old_pdf_wikilink = f"[[Lit-WS-PDFs/{year}/{old_stem}.pdf]]"
        new_pdf_wikilink = f"[[Lit-WS-PDFs/{year}/{new_stem}.pdf]]"
        content = update_yaml_field(content, "local_pdf", old_stem, new_pdf_wikilink)

        # Update pdf_extract
        old_extract_path = f"PDF Extracts/{year}/{old_stem}.md"
        new_extract_path = f"PDF Extracts/{year}/{new_stem}.md"
        content = update_yaml_field(content, "pdf_extract", old_stem, new_extract_path)

        new_paper.write_text(content, encoding='utf-8')
        print(f"  YAML: updated local_pdf + pdf_extract")

    print(f"\nDone! Renamed {len(PAPERS)} papers.")


if __name__ == "__main__":
    main()
