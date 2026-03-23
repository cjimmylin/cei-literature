#!/usr/bin/env python3
"""
Sort root-level PDFs into year-based subdirectories and update paper YAML.

Moves PDFs directly in Lit-WS-PDFs/ (not in year subdirs) into Lit-WS-PDFs/YYYY/ based on
the filename prefix, and updates the corresponding paper's local_pdf wikilink.

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/sort_root_pdfs.py --dry-run
    ../.venv/bin/python PYTHON/sort_root_pdfs.py
"""

import argparse
import functools
import re
import shutil
import sys
from pathlib import Path

print = functools.partial(print, flush=True)

sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))
from config import PAPERS_DIR, PDFS_DIR


def extract_year(filename):
    """Extract the leading 4-digit year from a PDF filename."""
    m = re.match(r'^(\d{4})-', filename)
    return m.group(1) if m else None


def main():
    parser = argparse.ArgumentParser(description="Sort root PDFs into year subdirs")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview mode: show what would happen without changes")
    args = parser.parse_args()

    if args.dry_run:
        print("=== DRY RUN — no files will be modified ===\n")

    # Collect root-level PDFs (only direct children, not subdirs)
    root_pdfs = []
    for item in sorted(PDFS_DIR.iterdir()):
        if item.is_file() and item.suffix.lower() == ".pdf":
            root_pdfs.append(item)

    print("Found {} root-level PDFs in {}".format(len(root_pdfs), PDFS_DIR))

    if not root_pdfs:
        print("Nothing to do.")
        return

    moved = 0
    yaml_updated = 0
    errors = 0

    for pdf_path in root_pdfs:
        filename = pdf_path.name
        year = extract_year(filename)

        if not year:
            print("  SKIP (no year prefix): {}".format(filename))
            errors += 1
            continue

        # Target directory and path
        target_dir = PDFS_DIR / year
        target_path = target_dir / filename

        # Collision check
        if target_path.exists():
            print("  SKIP (collision): {} already exists in {}/".format(filename, year))
            errors += 1
            continue

        # Find matching paper
        stem = pdf_path.stem
        paper_path = PAPERS_DIR / "{}.md".format(stem)
        if not paper_path.exists():
            print("  WARN (no paper): {}".format(filename))

        # Move PDF
        if not args.dry_run:
            target_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(pdf_path), str(target_path))

        print("  MOVED: {} -> {}/{}".format(filename, year, filename))
        moved += 1

        # Update paper YAML local_pdf field
        if paper_path.exists():
            content = paper_path.read_text(encoding="utf-8")

            # Match local_pdf pointing to root: "[[Lit-WS-PDFs/filename.pdf]]"
            old_wikilink = '"[[Lit-WS-PDFs/{}]]"'.format(filename)
            new_wikilink = '"[[Lit-WS-PDFs/{}/{}]]"'.format(year, filename)

            # Safe regex: replace the local_pdf line
            new_content, n = re.subn(
                r'^(local_pdf:\s*)' + re.escape(old_wikilink) + r'$',
                r'\g<1>' + new_wikilink,
                content,
                count=1,
                flags=re.MULTILINE,
            )

            if n > 0:
                if not args.dry_run:
                    paper_path.write_text(new_content, encoding="utf-8")
                print("    YAML: local_pdf -> {}".format(new_wikilink))
                yaml_updated += 1
            else:
                # Try broader match (local_pdf may have different format)
                new_content2, n2 = re.subn(
                    r'^(local_pdf:\s*)[^\n]*$',
                    r'\g<1>' + new_wikilink,
                    content,
                    count=1,
                    flags=re.MULTILINE,
                )
                if n2 > 0:
                    if not args.dry_run:
                        paper_path.write_text(new_content2, encoding="utf-8")
                    print("    YAML (broad match): local_pdf -> {}".format(new_wikilink))
                    yaml_updated += 1
                else:
                    print("    WARN: Could not update local_pdf for {}".format(paper_path.name))

    print("\n=== SUMMARY ===")
    print("  PDFs moved: {}".format(moved))
    print("  YAML updated: {}".format(yaml_updated))
    print("  Errors/skips: {}".format(errors))

    if args.dry_run:
        print("\n(Dry run — no files were modified)")


if __name__ == "__main__":
    main()
