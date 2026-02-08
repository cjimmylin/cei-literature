#!/usr/bin/env python3
"""Migrate PDFs and Extracts into year-based subdirectories.

Moves files from flat layout to YYYY/ subdirectories:
  PDFs/2024-Author-Title.pdf        → PDFs/2024/2024-Author-Title.pdf
  PDF Extracts/2024-Author-Title.md → PDF Extracts/2024/2024-Author-Title.md

Then updates all YAML references (local_pdf, pdf_extract) and body wikilinks
in paper markdown files.

This script is idempotent — safe to re-run.

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/migrate_pdfs_to_year_dirs.py --dry-run
    ../.venv/bin/python PYTHON/migrate_pdfs_to_year_dirs.py
"""

import argparse
import re
import shutil
from pathlib import Path

# ── Configuration ──────────────────────────────────────────────────────

BASE = Path(__file__).parent.parent.resolve()  # CEI-Lit-WS/
PDFS_DIR = BASE.parent / "PDFs"
EXTRACTS_DIR = BASE / "PDF Extracts"
PAPERS_DIR = BASE / "papers"

YEAR_RE = re.compile(r"^(\d{4})-")


# ── Step 1A & 1B: Move files into year subdirectories ──────────────────

def move_files_to_year_dirs(source_dir: Path, pattern: str, dry_run: bool) -> dict:
    """Move root-level files into YYYY/ subdirectories.

    Returns dict of {old_name: new_relative_path} for tracking.
    """
    moved = {}
    skipped = 0
    warnings = []

    # Only scan root-level files (not existing subdirs)
    for f in sorted(source_dir.glob(pattern)):
        if not f.is_file():
            continue

        m = YEAR_RE.match(f.name)
        if not m:
            warnings.append(f"  SKIP (no year prefix): {f.name}")
            skipped += 1
            continue

        year = m.group(1)
        year_dir = source_dir / year
        dest = year_dir / f.name

        if dest.exists():
            # Already migrated (idempotent)
            continue

        if dry_run:
            print(f"  [DRY] {f.name} → {year}/{f.name}")
        else:
            year_dir.mkdir(exist_ok=True)
            shutil.move(str(f), str(dest))

        moved[f.name] = f"{year}/{f.name}"

    for w in warnings:
        print(w)

    return moved


# ── Steps 1C-1E: Update paper YAML and body links ─────────────────────

def update_paper_references(dry_run: bool) -> dict:
    """Update local_pdf, pdf_extract, and body wikilinks in all papers.

    Returns dict of counters.
    """
    stats = {"local_pdf": 0, "pdf_extract": 0, "body_links": 0, "files_changed": 0}

    for paper in sorted(PAPERS_DIR.glob("*.md")):
        content = paper.read_text(encoding="utf-8")
        original = content

        # ── 1C: Update local_pdf field ──
        # Matches: local_pdf: "[[PDFs/2024-Author-Title.pdf]]"
        # Also:    local_pdf: [[PDFs/2024-Author-Title.pdf]]
        # Captures the year-prefixed filename at root level (no / before filename)
        content, n = re.subn(
            r'^(local_pdf:\s*"?\[\[PDFs/)(\d{4})(-[^\]/]+\.pdf\]\]"?)$',
            r"\g<1>\2/\2\3",
            content,
            flags=re.MULTILINE,
        )
        stats["local_pdf"] += n

        # ── 1D: Update pdf_extract field ──
        # Matches: pdf_extract: "PDF Extracts/2024-Author-Title.md"
        # Also:    pdf_extract: PDF Extracts/2024-Author-Title.md
        content, n = re.subn(
            r'^(pdf_extract:\s*"?PDF Extracts/)(\d{4})(-[^"\n]+\.md"?)$',
            r"\g<1>\2/\2\3",
            content,
            flags=re.MULTILINE,
        )
        stats["pdf_extract"] += n

        # ── 1E: Update body wikilinks ──
        # Matches: [[PDFs/2024-Author-Title.pdf|Open PDF]] or [[PDFs/2024-Author-Title.pdf]]
        content, n = re.subn(
            r"\[\[PDFs/(\d{4})(-[^\]/]+\.pdf)",
            r"[[PDFs/\1/\1\2",
            content,
        )
        stats["body_links"] += n

        if content != original:
            stats["files_changed"] += 1
            if dry_run:
                # Show first change for this file
                paper_name = paper.name
                changes = []
                if re.subn(r'^(local_pdf:\s*"?\[\[PDFs/)(\d{4})(-[^\]/]+\.pdf\]\]"?)$', '', original, flags=re.MULTILINE)[1]:
                    changes.append("local_pdf")
                if re.subn(r'^(pdf_extract:\s*"?PDF Extracts/)(\d{4})(-[^"\n]+\.md"?)$', '', original, flags=re.MULTILINE)[1]:
                    changes.append("pdf_extract")
                if re.subn(r"\[\[PDFs/(\d{4})(-[^\]/]+\.pdf)", '', original)[1]:
                    changes.append("body_links")
                print(f"  [DRY] {paper_name}: {', '.join(changes)}")
            else:
                paper.write_text(content, encoding="utf-8")

    return stats


# ── Main ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Migrate PDFs/Extracts to year-based subdirectories")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without applying them")
    args = parser.parse_args()

    dry_run = args.dry_run
    mode = "[DRY RUN]" if dry_run else "[LIVE]"

    print(f"{'=' * 60}")
    print(f"PDF & Extract Migration to Year Directories {mode}")
    print(f"{'=' * 60}")

    # Verify directories
    for d, name in [(PDFS_DIR, "PDFs"), (EXTRACTS_DIR, "PDF Extracts"), (PAPERS_DIR, "papers")]:
        if not d.exists():
            print(f"ERROR: {name} directory not found: {d}")
            return

    # Step 1A: Move PDFs
    print(f"\n── Step 1A: Move PDFs into year subdirectories ──")
    pdf_count_before = len(list(PDFS_DIR.glob("*.pdf")))
    print(f"  Root-level PDFs: {pdf_count_before}")
    pdf_moved = move_files_to_year_dirs(PDFS_DIR, "*.pdf", dry_run)
    print(f"  Moved: {len(pdf_moved)}")

    # Step 1B: Move Extracts
    print(f"\n── Step 1B: Move Extracts into year subdirectories ──")
    extract_count_before = len(list(EXTRACTS_DIR.glob("*.md")))
    print(f"  Root-level extracts: {extract_count_before}")
    extract_moved = move_files_to_year_dirs(EXTRACTS_DIR, "*.md", dry_run)
    print(f"  Moved: {len(extract_moved)}")

    # Steps 1C-1E: Update paper references
    print(f"\n── Steps 1C-1E: Update paper YAML + body links ──")
    ref_stats = update_paper_references(dry_run)
    print(f"  local_pdf fields updated:  {ref_stats['local_pdf']}")
    print(f"  pdf_extract fields updated: {ref_stats['pdf_extract']}")
    print(f"  Body wikilinks updated:    {ref_stats['body_links']}")
    print(f"  Papers modified:           {ref_stats['files_changed']}")

    # Summary
    print(f"\n{'=' * 60}")
    print(f"SUMMARY {mode}")
    print(f"  PDFs moved:       {len(pdf_moved)}")
    print(f"  Extracts moved:   {len(extract_moved)}")
    print(f"  Papers modified:  {ref_stats['files_changed']}")
    print(f"{'=' * 60}")

    if dry_run:
        print(f"\nTo apply changes, run without --dry-run")

    # Post-migration file count verification
    if not dry_run:
        total_pdfs = len(list(PDFS_DIR.rglob("*.pdf")))
        total_extracts = len(list(EXTRACTS_DIR.rglob("*.md")))
        remaining_root_pdfs = len(list(PDFS_DIR.glob("*.pdf")))
        remaining_root_extracts = len(list(EXTRACTS_DIR.glob("*.md")))
        print(f"\n── Verification ──")
        print(f"  Total PDFs (all subdirs):     {total_pdfs}")
        print(f"  Remaining root-level PDFs:    {remaining_root_pdfs}")
        print(f"  Total extracts (all subdirs): {total_extracts}")
        print(f"  Remaining root-level extracts: {remaining_root_extracts}")


if __name__ == "__main__":
    main()
