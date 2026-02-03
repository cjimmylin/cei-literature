#!/usr/bin/env python3
"""
Extract PDF text from AI Labs folder.

Creates markdown extracts in 'PDF Extracts/AI Labs/' for all unique PDFs.
Handles duplicates by preferring model-specific folders over Papers/ folders.
"""

import os
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Error: PyMuPDF not installed. Run: pip install pymupdf")
    sys.exit(1)

# Directories - use vault_config
from vault_config import AI_LAB_PDFS_DIR, PDF_EXTRACTS_DIR
EXTRACT_DIR = PDF_EXTRACTS_DIR / "AI Labs"


def find_unique_pdfs():
    """Find all unique PDFs, preferring model-specific folders over Papers folders."""
    pdf_map = defaultdict(list)  # filename -> list of full paths

    for root, dirs, files in os.walk(AI_LAB_PDFS_DIR):
        for f in files:
            if f.lower().endswith('.pdf'):
                full_path = Path(root) / f
                pdf_map[f].append(full_path)

    # For duplicates, prefer paths that don't contain "Papers"
    unique_pdfs = {}
    for filename, paths in pdf_map.items():
        if len(paths) == 1:
            unique_pdfs[filename] = paths[0]
        else:
            # Prefer non-Papers paths
            non_papers = [p for p in paths if 'Papers' not in str(p)]
            unique_pdfs[filename] = non_papers[0] if non_papers else paths[0]

    return unique_pdfs


def extract_company_model(pdf_path):
    """Extract company and model name from path."""
    parts = pdf_path.parts
    # Check for old structure (AI Labs in path)
    if 'AI Labs' in parts:
        idx = parts.index('AI Labs')
        company = parts[idx + 1] if len(parts) > idx + 1 else "Unknown"
        model = parts[idx + 2] if len(parts) > idx + 2 and parts[idx + 2] != 'Papers' else None
        return company, model
    # New structure: AI-Lab-PDFs at root
    elif 'AI-Lab-PDFs' in parts:
        idx = parts.index('AI-Lab-PDFs')
        company = parts[idx + 1] if len(parts) > idx + 1 else "Unknown"
        model = parts[idx + 2] if len(parts) > idx + 2 and parts[idx + 2] != 'Papers' else None
        return company, model
    return "Unknown", None


def create_markdown_extract(pdf_path, text_content, num_pages, company, model):
    """Create a markdown file for the PDF extract."""
    title = pdf_path.stem.replace('_', ' ').replace('-', ' ')

    model_info = f"\n**Model:** {model}" if model else ""

    markdown = f"""---
title: "{title}"
source_pdf: "{pdf_path}"
company: "{company}"
pages: {num_pages}
extracted_at: "{datetime.now().isoformat()}"
type: "ai_lab_paper"
---

# {title}

**Company/Lab:** {company}{model_info}
**Source PDF:** {pdf_path}
**Total Pages:** {num_pages}

---

## Content

```
"""
    markdown += text_content
    markdown += "\n```\n"

    return markdown


def extract_pdf(pdf_path, output_path, verbose=True):
    """Extract text from a single PDF."""
    try:
        doc = fitz.open(pdf_path)
        text_parts = []

        for i, page in enumerate(doc, 1):
            text_parts.append(f"--- Page {i} ---\n")
            text_parts.append(page.get_text())

        num_pages = len(doc)
        doc.close()

        text = "\n".join(text_parts)

        company, model = extract_company_model(pdf_path)
        markdown_content = create_markdown_extract(pdf_path, text, num_pages, company, model)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        if verbose:
            print(f"✓ Extracted: {pdf_path.name} ({len(text):,} chars, {num_pages} pages)")

        return True

    except Exception as e:
        print(f"✗ Error processing {pdf_path.name}: {e}")
        return False


def main():
    """Main extraction function."""
    print("=" * 60)
    print("AI Labs PDF Extraction")
    print("=" * 60)

    # Find unique PDFs
    unique_pdfs = find_unique_pdfs()
    print(f"\nFound {len(unique_pdfs)} unique PDFs in AI Labs/")

    # Ensure output directory exists
    EXTRACT_DIR.mkdir(parents=True, exist_ok=True)

    # Track stats
    extracted = 0
    skipped = 0
    errors = 0

    for filename, pdf_path in sorted(unique_pdfs.items()):
        # Output path preserves some structure
        company, model = extract_company_model(pdf_path)
        output_filename = f"{company}-{filename.replace('.pdf', '.md')}"
        output_path = EXTRACT_DIR / output_filename

        # Skip if already exists
        if output_path.exists():
            print(f"  Skipping {filename} - extract exists")
            skipped += 1
            continue

        if extract_pdf(pdf_path, output_path):
            extracted += 1
        else:
            errors += 1

    # Summary
    print("\n" + "=" * 60)
    print("EXTRACTION SUMMARY")
    print("=" * 60)
    print(f"Total unique PDFs: {len(unique_pdfs)}")
    print(f"Extracted: {extracted}")
    print(f"Skipped (already exist): {skipped}")
    print(f"Errors: {errors}")
    print(f"\nExtracts saved to: {EXTRACT_DIR}/")


if __name__ == "__main__":
    main()
