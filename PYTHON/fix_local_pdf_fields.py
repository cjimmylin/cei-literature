#!/usr/bin/env python3
"""
Fix blank and broken local_pdf fields across the vault.

Three categories of issues:
  A) Blank local_pdf: field is empty → check if PDF exists, set wikilink or N/A
  B) Quote mismatch: wikilink uses wrong quote style → fix to match actual PDF
  C) Author name mismatch: PDF on disk still has [[Unknown]] → rename PDF

Uses safe regex replacement for YAML fields (no parse/rebuild round-trip).
"""

import os
import re
import shutil
import functools
from pathlib import Path

print = functools.partial(print, flush=True)

SCRIPT_DIR = Path(__file__).parent
WS_ROOT = SCRIPT_DIR.parent
PAPERS_DIR = WS_ROOT / "papers"
PDFS_DIR = WS_ROOT.parent / "PDFs"

# ── Build PDF index ──────────────────────────────────────────────────────────
def build_pdf_index():
    """Build a mapping of PDF basename → full path, scanning all year dirs."""
    index = {}
    for pdf in PDFS_DIR.rglob("*.pdf"):
        index[pdf.name] = pdf
    return index


def make_wikilink(pdf_path):
    """Construct a local_pdf YAML wikilink value from a PDF Path."""
    # Get relative path from PDFs root: e.g. 2024/filename.pdf
    try:
        rel = pdf_path.relative_to(PDFS_DIR)
    except ValueError:
        rel = pdf_path.name
    return f'"[[Lit-WS-PDFs/{rel}]]"'


def safe_set_local_pdf(paper_path, new_value):
    """Safely set the local_pdf field using regex replacement."""
    content = paper_path.read_text(encoding="utf-8")

    # Match local_pdf: <anything> (possibly empty)
    # Use [^\n]* instead of .* to avoid crossing line boundaries
    new_content, n = re.subn(
        r'^(local_pdf:\s*)[^\n]*$',
        rf'\g<1>{new_value}',
        content,
        count=1,
        flags=re.MULTILINE,
    )

    if n > 0:
        paper_path.write_text(new_content, encoding="utf-8")
        return True
    return False


# ── Category A: Blank local_pdf ──────────────────────────────────────────────
def fix_blank_local_pdf(pdf_index):
    """Find papers with blank local_pdf and set wikilink or N/A."""
    print("\n=== Category: Blank local_pdf ===")
    fixed = 0
    set_na = 0

    for paper in sorted(PAPERS_DIR.glob("*.md")):
        content = paper.read_text(encoding="utf-8")

        # Match local_pdf: followed by empty/whitespace only
        m = re.search(r'^local_pdf:\s*$', content, re.MULTILINE)
        if not m:
            continue

        # Try to find matching PDF by converting paper name to PDF name
        stem = paper.stem  # e.g. "2024-Author-Title"
        pdf_name = stem + ".pdf"

        if pdf_name in pdf_index:
            wikilink = make_wikilink(pdf_index[pdf_name])
            if safe_set_local_pdf(paper, wikilink):
                print(f"  LINKED: {paper.name} → {wikilink}")
                fixed += 1
        else:
            if safe_set_local_pdf(paper, '"N/A"'):
                print(f"  SET N/A: {paper.name}")
                set_na += 1

    print(f"  Summary: {fixed} linked, {set_na} set to N/A")
    return fixed + set_na


# ── Category B: Quote mismatches ─────────────────────────────────────────────
# Papers where local_pdf uses wrong quote style vs actual PDF filename.
# Based on detailed audit: the wikilink replaced double curly quotes with
# single curly quotes, but the actual PDF has double curly quotes.

QUOTE_FIX_MAP = {
    # Paper filename → correct PDF filename (on disk)
    "2025-Unknown-1 Decolonizing NLP for \u201cLow-resource Languages\u201d.md":
        "2025-Unknown-1 Decolonizing NLP for \u201cLow-resource Languages\u201d.pdf",
    "2022-Hu-\u201cI\u2019m sorry to hear that\u201d.md":
        "2022-Hu-\u201cI\u2019m sorry to hear that\u201d.pdf",
    "2024-Grezes-\u201cIt\u2019s how you do things that matters\u201d Attending to Process to Better.md":
        "2024-Grezes-\u201cIt\u2019s how you do things that matters\u201d Attending to Process to Better.pdf",
    "2023-Shen-\u201cDo Anything Now\u201d.md":
        "2023-Shen-\u201cDo Anything Now\u201d.pdf",
}

# Papers where curly apostrophe in wikilink matches PDF but audit fails
# (encoding issue in audit script, not actual mismatch). Verify & re-link.
APOSTROPHE_VERIFY = [
    "2025-Cognitive-Evolution of Meta\u2019s LLaMA Models and Parameter-Efficient Fine-Tuning.md",
    "2025-LaCroix-Metaethical perspectives on \u2018benchmarking\u2019 AI.md",
    "2025-Unknown-Evaluating LLMs\u2019 Language Confusion in Code-switching Context Juhyun.md",
    "2025-Pretrained-MiLiC-Eval Benchmarking Multilingual LLMs for China\u2019s Minority.md",
    "2025-Masood-From Words to Proverbs Evaluating LLMs\u2019 Linguistic and Cultural.md",
]


def fix_quote_mismatches(pdf_index):
    """Fix local_pdf wikilinks with wrong quote characters."""
    print("\n=== Category B: Quote mismatches ===")
    fixed = 0

    for paper_name, correct_pdf in QUOTE_FIX_MAP.items():
        paper_path = PAPERS_DIR / paper_name
        if not paper_path.exists():
            print(f"  SKIP (not found): {paper_name}")
            continue

        if correct_pdf in pdf_index:
            wikilink = make_wikilink(pdf_index[correct_pdf])
            if safe_set_local_pdf(paper_path, wikilink):
                print(f"  FIXED: {paper_name}")
                fixed += 1
        else:
            print(f"  WARN: PDF not found: {correct_pdf}")

    # Verify and re-link apostrophe papers
    for paper_name in APOSTROPHE_VERIFY:
        paper_path = PAPERS_DIR / paper_name
        if not paper_path.exists():
            print(f"  SKIP (not found): {paper_name}")
            continue

        stem = paper_path.stem
        pdf_name = stem + ".pdf"
        if pdf_name in pdf_index:
            wikilink = make_wikilink(pdf_index[pdf_name])
            if safe_set_local_pdf(paper_path, wikilink):
                print(f"  RE-LINKED: {paper_name}")
                fixed += 1
        else:
            print(f"  WARN: PDF not found for: {paper_name}")

    print(f"  Summary: {fixed} fixed")
    return fixed


# ── Category C: Author name mismatch (PDF has [[Unknown]], paper was renamed) ──

AUTHOR_RENAME_MAP = {
    # paper_name → (old PDF name with [[Unknown]], new PDF name with author)
    "2026-Ali-UrduLM A Resource-Efficient Monolingual Urdu Language.md": (
        "2026-[[Unknown]]-UrduLM A Resource-Efficient Monolingual Urdu Language.pdf",
        "2026-Ali-UrduLM A Resource-Efficient Monolingual Urdu Language.pdf",
    ),
    "2025-Pudasaini-NepaliGPT A Generative Language Model for.md": (
        "2025-[[Unknown]]-NepaliGPT A Generative Language Model for.pdf",
        "2025-Pudasaini-NepaliGPT A Generative Language Model for.pdf",
    ),
    "2023-Sabane-Breaking Language Barriers A Question-Answering Dataset.md": (
        "2023-[[Unknown]]-Breaking Language Barriers A Question-Answering Dataset.pdf",
        "2023-Sabane-Breaking Language Barriers A Question-Answering Dataset.pdf",
    ),
    "2024-Nyachhyon-Consolidating and Developing Benchmarking Datasets for.md": (
        "2024-[[Unknown]]-Consolidating and Developing Benchmarking Datasets for.pdf",
        "2024-Nyachhyon-Consolidating and Developing Benchmarking Datasets for.pdf",
    ),
    "2024-Chouhan-HindiLLM Large Language Model for Hindi.md": (
        "2024-[[Unknown]]-HindiLLM Large Language Model for Hindi.pdf",
        "2024-Chouhan-HindiLLM Large Language Model for Hindi.pdf",
    ),
    "2024-Gala-Airavata Introducing Hindi Instruction-tuned LLM.md": (
        "2024-[[Unknown]]-Airavata Introducing Hindi Instruction-tuned LLM.pdf",
        "2024-Gala-Airavata Introducing Hindi Instruction-tuned LLM.pdf",
    ),
}


def fix_author_mismatches(pdf_index):
    """Rename PDFs from [[Unknown]] to correct author and update wikilinks."""
    print("\n=== Category C: Author name mismatches (rename PDFs) ===")
    fixed = 0

    for paper_name, (old_pdf, new_pdf) in AUTHOR_RENAME_MAP.items():
        paper_path = PAPERS_DIR / paper_name
        if not paper_path.exists():
            print(f"  SKIP (paper not found): {paper_name}")
            continue

        # Find old PDF on disk
        if old_pdf not in pdf_index:
            print(f"  SKIP (old PDF not found): {old_pdf}")
            continue

        old_path = pdf_index[old_pdf]
        new_path = old_path.parent / new_pdf

        # Rename PDF
        if not new_path.exists():
            os.rename(old_path, new_path)
            print(f"  RENAMED PDF: {old_pdf} → {new_pdf}")

            # Also rename extract if it exists
            old_extract_name = old_pdf.replace(".pdf", ".md")
            extract_dir = WS_ROOT / "PDF Extracts"
            for ext_file in extract_dir.rglob(old_extract_name):
                new_ext_path = ext_file.parent / new_pdf.replace(".pdf", ".md")
                if not new_ext_path.exists():
                    os.rename(ext_file, new_ext_path)
                    print(f"  RENAMED EXTRACT: {ext_file.name} → {new_ext_path.name}")

                    # Update pdf_extract field too
                    content = paper_path.read_text(encoding="utf-8")
                    year_match = re.match(r'^(\d{4})-', new_pdf)
                    year = year_match.group(1) if year_match else ""
                    new_extract_val = f'"PDF Extracts/{year}/{new_ext_path.name}"'
                    content, n = re.subn(
                        r'^(pdf_extract:\s*)[^\n]*$',
                        rf'\g<1>{new_extract_val}',
                        content,
                        count=1,
                        flags=re.MULTILINE,
                    )
                    if n > 0:
                        paper_path.write_text(content, encoding="utf-8")
        else:
            print(f"  PDF already exists at new name: {new_pdf}")

        # Update local_pdf wikilink
        wikilink = make_wikilink(new_path)
        if safe_set_local_pdf(paper_path, wikilink):
            print(f"  LINKED: {paper_name} → {wikilink}")
            fixed += 1

        # Update pdf_index for future lookups
        pdf_index[new_pdf] = new_path
        if old_pdf in pdf_index:
            del pdf_index[old_pdf]

    print(f"  Summary: {fixed} fixed")
    return fixed


def main():
    print("Building PDF index...")
    pdf_index = build_pdf_index()
    print(f"  {len(pdf_index)} PDFs indexed")

    total = 0
    total += fix_blank_local_pdf(pdf_index)
    total += fix_quote_mismatches(pdf_index)
    total += fix_author_mismatches(pdf_index)

    print(f"\n=== TOTAL: {total} papers fixed ===")


if __name__ == "__main__":
    main()
