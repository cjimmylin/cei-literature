#!/usr/bin/env python3
"""
Organize PDFs by Ethical Framework into Subfolders

Reads the 73 normative-ethics papers from V3 (R1 report + R2 JSON),
classifies each by ethical framework using keyword matching, then
copies PDFs (or PDF extracts as fallback) into framework subfolders.

Target structure:
  PDFs/
  ├── Deontological Ethics/
  │   ├── Confirmed/
  │   └── Borderline/
  ├── Utilitarian Ethics/
  │   ├── Confirmed/
  │   └── Borderline/
  └── Virtue Ethics/
      ├── Confirmed/
      └── Borderline/

Read-only on YAML files — only copies PDFs.
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path
from datetime import date
from collections import defaultdict
from typing import Optional, Tuple

# ---------------------------------------------------------------------------
# Path setup & imports
# ---------------------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))
from config import PAPERS_DIR, PDFS_DIR, PDF_EXTRACTS_DIR, LOGS_DIR
from yaml_utils import extract_frontmatter, parse_frontmatter

# Import functions from the V3 report generator
sys.path.insert(0, str(Path(__file__).parent))
from generate_normative_v3_report import (
    parse_r1_report,
    load_r2_json,
    deduplicate,
    match_frameworks,
    R1_REPORT,
    R2_JSON,
)

# ---------------------------------------------------------------------------
# Framework → folder name mapping (subset of FRAMEWORK_KEYWORDS)
# ---------------------------------------------------------------------------
TARGET_FRAMEWORKS = {
    "Deontological": "Deontological Ethics",
    "Utilitarian / Consequentialist": "Utilitarian Ethics",
    "Virtue Ethics": "Virtue Ethics",
}


def get_pdf_path(paper_filename: str) -> tuple[Path | None, str]:
    """Resolve the PDF path for a paper by reading its YAML frontmatter.

    Returns:
        (path_to_file, source_type) where source_type is 'pdf', 'extract', or 'missing'.
    """
    paper_path = PAPERS_DIR / paper_filename
    pdf_name = None
    extract_name = None

    if paper_path.exists():
        try:
            content = paper_path.read_text(encoding="utf-8")
            fm_text, _ = extract_frontmatter(content)
            fm = parse_frontmatter(fm_text)

            # Get local_pdf — strip [[ ]] and quotes
            raw_pdf = fm.get("local_pdf", "")
            if raw_pdf:
                raw_pdf = raw_pdf.strip('"').strip("'")
                raw_pdf = raw_pdf.replace("[[", "").replace("]]", "")
                pdf_name = Path(raw_pdf).name  # e.g. "2024-Yu-CMoralEval.pdf"

            # Get pdf_extract — strip quotes
            raw_extract = fm.get("pdf_extract", "")
            if raw_extract:
                raw_extract = raw_extract.strip('"').strip("'")
                extract_name = Path(raw_extract).name
        except (ValueError, OSError):
            pass

    # Fallback: derive PDF name from paper filename
    if not pdf_name:
        pdf_name = paper_filename.replace(".md", ".pdf")

    # Try PDF first
    pdf_path = PDFS_DIR / pdf_name
    if pdf_path.exists():
        return pdf_path, "pdf"

    # Fallback to extract
    if extract_name:
        extract_path = PDF_EXTRACTS_DIR / extract_name
        if extract_path.exists():
            return extract_path, "extract"

    # Also try derived extract name
    derived_extract = paper_filename  # .md files in PDF Extracts/
    extract_path = PDF_EXTRACTS_DIR / derived_extract
    if extract_path.exists():
        return extract_path, "extract"

    return None, "missing"


def main():
    # ------------------------------------------------------------------
    # Load and deduplicate papers (same logic as V3 report)
    # ------------------------------------------------------------------
    print("Loading R1 report...")
    r1_papers = parse_r1_report(R1_REPORT)
    print(f"  R1: {len(r1_papers)} papers")

    print("Loading R2 JSON...")
    r2_papers = load_r2_json(R2_JSON)
    print(f"  R2: {len(r2_papers)} papers")

    print("Deduplicating...")
    papers = deduplicate(r1_papers, r2_papers)
    yes_count = sum(1 for p in papers if p["decision"] == "Yes")
    bl_count = sum(1 for p in papers if p["decision"] == "Borderline")
    print(f"  Combined: {yes_count} Yes + {bl_count} Borderline = {len(papers)} papers")

    # ------------------------------------------------------------------
    # Classify each paper by framework
    # ------------------------------------------------------------------
    fw_assignments = defaultdict(list)  # fw_key → list of (paper, decision)

    for p in papers:
        fw_text = p.get("normative_frameworks", "") + " " + p.get("reasoning", "")
        matched = match_frameworks(fw_text)
        for fw_key in matched:
            if fw_key in TARGET_FRAMEWORKS:
                fw_assignments[fw_key].append(p)

    print("\nFramework assignment counts:")
    for fw_key, folder_name in TARGET_FRAMEWORKS.items():
        assigned = fw_assignments[fw_key]
        y = sum(1 for p in assigned if p["decision"] == "Yes")
        b = sum(1 for p in assigned if p["decision"] == "Borderline")
        print(f"  {folder_name}: {y} Confirmed + {b} Borderline = {len(assigned)} total")

    # ------------------------------------------------------------------
    # Create folder structure and copy files
    # ------------------------------------------------------------------
    print("\nCreating folders and copying files...\n")

    copied_log = []   # (framework, subfolder, source_file, dest_file, source_type)
    missing_log = []   # (framework, paper_filename, decision)

    for fw_key, folder_name in TARGET_FRAMEWORKS.items():
        for subfolder in ("Confirmed", "Borderline"):
            dest_dir = PDFS_DIR / folder_name / subfolder
            dest_dir.mkdir(parents=True, exist_ok=True)

        for p in fw_assignments[fw_key]:
            fname = p["filename"]
            decision = p["decision"]
            subfolder = "Confirmed" if decision == "Yes" else "Borderline"

            source_path, source_type = get_pdf_path(fname)

            if source_path is None:
                missing_log.append((folder_name, fname, decision))
                print(f"  MISSING: {fname} → {folder_name}/{subfolder}/")
                continue

            dest_dir = PDFS_DIR / folder_name / subfolder
            dest_file = dest_dir / source_path.name
            shutil.copy2(source_path, dest_file)
            copied_log.append((folder_name, subfolder, str(source_path), str(dest_file), source_type))
            tag = " (extract)" if source_type == "extract" else ""
            print(f"  OK: {source_path.name}{tag} → {folder_name}/{subfolder}/")

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")

    total_copied = len(copied_log)
    total_missing = len(missing_log)
    pdf_count = sum(1 for c in copied_log if c[4] == "pdf")
    extract_count = sum(1 for c in copied_log if c[4] == "extract")

    print(f"  Files copied:  {total_copied} ({pdf_count} PDFs + {extract_count} extracts)")
    print(f"  Missing:       {total_missing}")

    for fw_key, folder_name in TARGET_FRAMEWORKS.items():
        fw_copied = [c for c in copied_log if c[0] == folder_name]
        fw_missing = [m for m in missing_log if m[0] == folder_name]
        confirmed = sum(1 for c in fw_copied if c[1] == "Confirmed")
        borderline = sum(1 for c in fw_copied if c[1] == "Borderline")
        print(f"\n  {folder_name}:")
        print(f"    Confirmed:  {confirmed} files")
        print(f"    Borderline: {borderline} files")
        if fw_missing:
            print(f"    Missing:    {len(fw_missing)}")

    # ------------------------------------------------------------------
    # Write log file
    # ------------------------------------------------------------------
    log_path = LOGS_DIR / "20260207-organize_pdfs_by_framework_log.md"
    log_lines = [
        f"# PDF Organization by Framework — Log",
        f"",
        f"**Date:** {date.today().isoformat()}",
        f"**Source papers:** {len(papers)} (from V3 normative ethics classification)",
        f"**Target:** `{PDFS_DIR}/` subfolders",
        f"",
        f"## Summary",
        f"",
        f"| Framework | Confirmed | Borderline | Missing | Total |",
        f"|-----------|----------:|-----------:|--------:|------:|",
    ]

    for fw_key, folder_name in TARGET_FRAMEWORKS.items():
        fw_copied = [c for c in copied_log if c[0] == folder_name]
        fw_missing = [m for m in missing_log if m[0] == folder_name]
        confirmed = sum(1 for c in fw_copied if c[1] == "Confirmed")
        borderline = sum(1 for c in fw_copied if c[1] == "Borderline")
        total = confirmed + borderline + len(fw_missing)
        log_lines.append(
            f"| {folder_name} | {confirmed} | {borderline} | {len(fw_missing)} | {total} |"
        )

    log_lines.append(f"")
    log_lines.append(f"**Total files copied:** {total_copied} ({pdf_count} PDFs + {extract_count} extracts)")
    log_lines.append(f"**Total missing:** {total_missing}")
    log_lines.append(f"")

    # Copied files detail
    log_lines.append(f"## Copied Files ({total_copied})")
    log_lines.append(f"")
    for fw_key, folder_name in TARGET_FRAMEWORKS.items():
        fw_copied = [c for c in copied_log if c[0] == folder_name]
        if not fw_copied:
            continue
        log_lines.append(f"### {folder_name}")
        log_lines.append(f"")
        for c in sorted(fw_copied, key=lambda x: (x[1], x[2])):
            tag = " *(extract)*" if c[4] == "extract" else ""
            log_lines.append(f"- `{Path(c[3]).name}`{tag} → {c[1]}/")
        log_lines.append(f"")

    # Missing files detail
    if missing_log:
        log_lines.append(f"## Missing Files ({total_missing})")
        log_lines.append(f"")
        for folder_name, fname, decision in sorted(missing_log):
            log_lines.append(f"- `{fname}` ({decision}) — {folder_name}")
        log_lines.append(f"")

    log_lines.append(f"---")
    log_lines.append(f"*Generated by `PYTHON/organize_pdfs_by_framework.py`*")

    log_path.write_text("\n".join(log_lines), encoding="utf-8")
    print(f"\nLog written: {log_path}")
    print("Done.")


if __name__ == "__main__":
    main()
