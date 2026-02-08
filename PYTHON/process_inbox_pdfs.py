#!/usr/bin/env python3
"""Process manually-downloaded PDFs from PDFs/INBOX/ into the vault.

For each PDF:
1. Rename & move from INBOX to PDFs/
2. Add local_pdf field to paper YAML (safe regex insertion)
3. Create PDF extract in PDF Extracts/
4. Add pdf_extract field to paper YAML (safe regex insertion)

Usage:
    cd CEI-Lit-WS && ../.venv/bin/python PYTHON/process_inbox_pdfs.py
"""

import re
import shutil
from datetime import datetime
from pathlib import Path

import fitz  # PyMuPDF


# ── Configuration ──────────────────────────────────────────────────────

BASE = Path(".")
PAPERS_DIR = BASE / "papers"
PDFS_DIR = BASE / ".." / "PDFs"        # PDFs live one level above CEI-Lit-WS
INBOX_DIR = PDFS_DIR / "INBOX"
EXTRACTS_DIR = BASE / "PDF Extracts"
RECYCLE_BIN = BASE / "RECYCLE-BIN"

# Mapping: INBOX filename → (paper stem, expected PDF name)
# Paper stem is the .md filename without extension
INBOX_MAP = [
    {
        "inbox_file": "3746252.3760884.pdf",
        "paper_stem": "2025-Gao-MIST Moral Inference through Storytelling with Text and Images",
        "pdf_name": "2025-Gao-MIST Moral Inference through Storytelling with Text and Images.pdf",
    },
    {
        "inbox_file": "A Companion to Applied Philosophy of AI -- Martin Hähnel & Regina Müller -- 1, 2025.pdf",
        "paper_stem": "2025-Hähnel-A Companion to Applied Philosophy of AI",
        "pdf_name": "2025-Hähnel-A Companion to Applied Philosophy of AI.pdf",
    },
    {
        "inbox_file": "Automated_Ethical_Practical_Reasoning_Th.pdf",
        "paper_stem": "2025-Sullins-Automated Ethical Practical Reasoning",
        "pdf_name": "2025-Sullins-Automated Ethical Practical Reasoning.pdf",
    },
    {
        "inbox_file": "JoersDeLuca_EudAImonia_CHI1 (1).pdf",
        "paper_stem": "2024-Jörs-Through Eudaimonia's Lenses",
        "pdf_name": "2024-Jörs-Through Eudaimonia's Lenses.pdf",
    },
    {
        "inbox_file": "SHTI-329-SHTI250854.pdf",
        "paper_stem": "2025-Ebara-Corpus-Based Medical Ethics Decision-Making Evaluation",
        "pdf_name": "2025-Ebara-Corpus-Based Medical Ethics Decision-Making Evaluation.pdf",
    },
]

# Duplicate to recycle
DUPLICATE = "Virtues_for_AI.pdf"


# ── YAML Field Insertion (safe regex, no parse/rebuild) ────────────────

def add_local_pdf_field(paper_path: Path, pdf_filename: str) -> bool:
    """Add local_pdf field to paper YAML using safe regex insertion."""
    content = paper_path.read_text(encoding="utf-8")

    if "local_pdf:" in content:
        print(f"  ⚠ local_pdf already exists, skipping")
        return False

    local_pdf_line = f'local_pdf: "[[PDFs/{pdf_filename}]]"'

    if "external_pdf:" in content:
        content = re.sub(
            r'(external_pdf:\s*"[^"]*"\n)',
            r"\1" + local_pdf_line + "\n",
            content,
            count=1,
        )
    elif "url:" in content:
        content = re.sub(
            r'(url:\s*"[^"]*"\n)',
            r"\1" + local_pdf_line + "\n",
            content,
            count=1,
        )
    elif "doi:" in content:
        content = re.sub(
            r"(doi:\s*[^\n]*\n)",
            r"\1" + local_pdf_line + "\n",
            content,
            count=1,
        )
    else:
        content = content.replace(
            "DATE_ADDED:", local_pdf_line + "\nDATE_ADDED:"
        )

    paper_path.write_text(content, encoding="utf-8")
    return True


def add_pdf_extract_field(paper_path: Path, extract_filename: str) -> bool:
    """Add pdf_extract field to paper YAML using safe regex insertion."""
    content = paper_path.read_text(encoding="utf-8")

    if "pdf_extract:" in content and "PDF Extracts/" in content:
        print(f"  ⚠ pdf_extract already exists, skipping")
        return False

    extract_line = f'pdf_extract: "PDF Extracts/{extract_filename}"'

    if "local_pdf:" in content:
        content = re.sub(
            r'(local_pdf:\s*"?\[\[[^\]]*\]\]"?\n)',
            r"\1" + extract_line + "\n",
            content,
            count=1,
        )
    elif "external_pdf:" in content:
        content = re.sub(
            r'(external_pdf:\s*"[^"]*"\n)',
            r"\1" + extract_line + "\n",
            content,
            count=1,
        )
    else:
        content = content.replace(
            "DATE_ADDED:", extract_line + "\nDATE_ADDED:"
        )

    paper_path.write_text(content, encoding="utf-8")
    return True


# ── PDF Text Extraction ───────────────────────────────────────────────

def extract_pdf_text(pdf_path: Path, output_path: Path) -> int:
    """Extract text from PDF and write markdown extract file.

    Returns the number of pages.
    """
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

    output_path.write_text(content, encoding="utf-8")
    return num_pages


# ── Main Processing ───────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("Processing INBOX PDFs into Vault")
    print("=" * 60)

    # Verify directories exist
    for d in [INBOX_DIR, PDFS_DIR, EXTRACTS_DIR, RECYCLE_BIN, PAPERS_DIR]:
        if not d.exists():
            print(f"ERROR: Directory not found: {d}")
            return

    processed = 0
    errors = 0

    # Process each mapped PDF
    for entry in INBOX_MAP:
        inbox_file = entry["inbox_file"]
        paper_stem = entry["paper_stem"]
        pdf_name = entry["pdf_name"]

        print(f"\n{'─' * 60}")
        print(f"Processing: {inbox_file}")
        print(f"  → Paper: {paper_stem}")

        inbox_path = INBOX_DIR / inbox_file
        paper_path = PAPERS_DIR / f"{paper_stem}.md"
        pdf_dest = PDFS_DIR / pdf_name
        extract_path = EXTRACTS_DIR / f"{paper_stem}.md"

        # Verify source PDF exists
        if not inbox_path.exists():
            print(f"  ✗ INBOX PDF not found: {inbox_path}")
            errors += 1
            continue

        # Verify paper profile exists
        if not paper_path.exists():
            print(f"  ✗ Paper profile not found: {paper_path}")
            errors += 1
            continue

        # Step 1: Move & rename PDF
        if pdf_dest.exists():
            print(f"  ⚠ PDF already exists at destination, skipping move")
        else:
            shutil.move(str(inbox_path), str(pdf_dest))
            print(f"  ✓ Moved PDF → PDFs/{pdf_name}")

        # Step 2: Add local_pdf field
        if add_local_pdf_field(paper_path, pdf_name):
            print(f"  ✓ Added local_pdf field")

        # Step 3: Create PDF extract
        if extract_path.exists():
            print(f"  ⚠ Extract already exists, skipping")
        else:
            num_pages = extract_pdf_text(pdf_dest, extract_path)
            print(f"  ✓ Created extract ({num_pages} pages)")

        # Step 4: Add pdf_extract field
        extract_filename = f"{paper_stem}.md"
        if add_pdf_extract_field(paper_path, extract_filename):
            print(f"  ✓ Added pdf_extract field")

        processed += 1

    # Handle duplicate
    print(f"\n{'─' * 60}")
    print(f"Handling duplicate: {DUPLICATE}")
    dup_path = INBOX_DIR / DUPLICATE
    if dup_path.exists():
        recycle_dest = RECYCLE_BIN / DUPLICATE
        shutil.move(str(dup_path), str(recycle_dest))
        print(f"  ✓ Moved to RECYCLE-BIN/{DUPLICATE}")
    else:
        print(f"  ⚠ Duplicate not found in INBOX (already handled?)")

    # Summary
    print(f"\n{'=' * 60}")
    print(f"SUMMARY: {processed} papers processed, {errors} errors")
    print(f"{'=' * 60}")

    # Check INBOX is empty
    remaining = list(INBOX_DIR.iterdir())
    remaining = [f for f in remaining if not f.name.startswith(".")]
    if remaining:
        print(f"\n⚠ INBOX still has {len(remaining)} file(s):")
        for f in remaining:
            print(f"  - {f.name}")
    else:
        print(f"\n✓ INBOX is empty")


if __name__ == "__main__":
    main()
