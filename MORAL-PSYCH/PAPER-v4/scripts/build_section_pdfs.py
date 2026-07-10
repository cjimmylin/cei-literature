#!/usr/bin/env python3
"""Build individual PDFs for each manuscript section using pandoc + typst.

Scans sections/ and supplementary/ directories for .md files,
runs pandoc with the typst backend, and outputs PDFs to PAPER-v4/.

Usage:
    python build_section_pdfs.py
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

# --- Configuration ---
PAPER_DIR = Path(__file__).resolve().parent.parent  # PAPER-v4/
SECTIONS_DIR = PAPER_DIR / "sections"
SUPPLEMENTARY_DIR = PAPER_DIR / "supplementary"
OUTPUT_DIR = PAPER_DIR  # PDFs go directly into PAPER-v4/

TITLE = "What Do Moral Psychology Benchmarks Actually Test?"
AUTHOR = "Jimmy Lin --- Center for Ethical Intelligence"
DATE = "April 2026 --- DRAFT v4.0"


def build_pdf(md_path: Path) -> tuple[bool, str, int]:
    """Convert a single .md file to PDF via pandoc+typst.

    Returns (success, output_path_or_error, file_size_bytes).
    """
    out_name = md_path.stem + ".pdf"
    out_path = OUTPUT_DIR / out_name

    cmd = [
        "pandoc",
        str(md_path),
        "-o", str(out_path),
        "--pdf-engine=typst",
        "--wrap=auto",
        f"--metadata=title:{TITLE}",
        f"--metadata=author:{AUTHOR}",
        f"--metadata=date:{DATE}",
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=120,
    )

    if result.returncode != 0:
        error_msg = (result.stderr or result.stdout or "unknown error").strip()
        return False, error_msg, 0

    size = out_path.stat().st_size if out_path.exists() else 0
    return True, str(out_path), size


def main() -> None:
    # Collect all markdown files from both directories
    md_files: list[Path] = []

    for src_dir in (SECTIONS_DIR, SUPPLEMENTARY_DIR):
        if src_dir.exists():
            md_files.extend(sorted(src_dir.glob("*.md")))

    if not md_files:
        print("No .md files found in sections/ or supplementary/.")
        sys.exit(1)

    print(f"Found {len(md_files)} markdown files to convert.\n")
    print(f"Output directory: {OUTPUT_DIR}\n")

    successes = []
    failures = []

    for md_path in md_files:
        rel = md_path.relative_to(PAPER_DIR)
        print(f"  Building {rel} ... ", end="", flush=True)

        ok, detail, size = build_pdf(md_path)

        if ok:
            size_kb = size / 1024
            print(f"OK  ({size_kb:.1f} KB)")
            successes.append((md_path.stem + ".pdf", size))
        else:
            print(f"FAILED")
            print(f"    Error: {detail[:200]}")
            failures.append((md_path.stem + ".pdf", detail))

    # --- Summary ---
    print("\n" + "=" * 60)
    print(f"SUMMARY: {len(successes)} succeeded, {len(failures)} failed")
    print("=" * 60)

    if successes:
        print("\nSuccessful PDFs:")
        total_size = 0
        for name, size in successes:
            size_kb = size / 1024
            total_size += size
            print(f"  {name:55s} {size_kb:7.1f} KB")
        print(f"  {'TOTAL':55s} {total_size / 1024:7.1f} KB")

    if failures:
        print("\nFailed conversions:")
        for name, err in failures:
            print(f"  {name}: {err[:120]}")

    sys.exit(0 if not failures else 1)


if __name__ == "__main__":
    main()
