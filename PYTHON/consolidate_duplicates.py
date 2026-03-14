#!/usr/bin/env python3
"""
Consolidate Duplicate Papers in CEI Literature Vault

Processes the reviewed duplicate_groups.json and consolidates each group:
  A. Merge YAML fields from duplicate into primary (safe regex in-place)
  B. Move duplicate paper files to RECYCLE-BIN
  C. Handle duplicate PDFs (keep primary's, recycle others)
  D. Handle duplicate PDF extracts
  E. Update Author profiles (replace wikilinks)
  F. Update cross-references in STATISTICS/, Authors/, AI Labs/
  G. Generate consolidation report

Usage:
    # Dry run
    python consolidate_duplicates.py --dry-run

    # Apply changes
    python consolidate_duplicates.py

    # Custom input file
    python consolidate_duplicates.py --input logs/20260208-duplicate_groups.json
"""

import argparse
import functools
import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Force flush
print = functools.partial(print, flush=True)

# --- Path setup ---
SCRIPT_DIR = Path(__file__).parent.resolve()
WORKSPACE_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(WORKSPACE_ROOT / ".agent"))

from vault_config import (
    PAPERS_DIR, PDF_EXTRACTS_DIR, PDFS_DIR, AUTHORS_DIR,
    AI_LABS_DIR, STATISTICS_DIR, LOGS_DIR, RECYCLE_BIN_DIR,
    WORKSPACE_ROOT as WS_ROOT,
)
from lib.yaml_utils import extract_frontmatter, parse_frontmatter
from ethics_scoring import is_ethics_yes, parse_ethics_value
from religious_scoring import RV_FIELDS, parse_rv_value


# ============================================================
# A. YAML Field Merging (SAFE regex in-place)
# ============================================================

def safe_replace_field(frontmatter: str, key: str, new_value: str) -> Tuple[str, int]:
    """
    Safely replace a YAML field value in-place using regex.
    NEVER uses parse->rebuild round-trip.
    """
    safe_value = new_value.replace('"', "'")
    if any(c in safe_value for c in (':', '[', ']', '{', '}', '#', '&', '*', '!', '|', '>', "'", ',')):
        replacement = f'{key}: "{safe_value}"'
    else:
        replacement = f'{key}: {safe_value}'

    pattern = rf'^{re.escape(key)}:\s*.*$'
    result, count = re.subn(pattern, replacement, frontmatter, count=1, flags=re.MULTILINE)
    return result, count


def safe_add_field(frontmatter: str, key: str, value: str) -> str:
    """Add a field to frontmatter if it doesn't exist. Appends before last line."""
    # Check if field exists
    pattern = rf'^{re.escape(key)}:\s*'
    if re.search(pattern, frontmatter, re.MULTILINE):
        return frontmatter  # Already exists

    safe_value = value.replace('"', "'")
    if any(c in safe_value for c in (':', '[', ']', '{', '}', '#', '&', '*', '!', '|', '>', "'", ',')):
        new_line = f'{key}: "{safe_value}"'
    else:
        new_line = f'{key}: {safe_value}'

    # Append to end of frontmatter
    return frontmatter.rstrip() + "\n" + new_line


def is_empty_field(value: str) -> bool:
    """Check if a YAML field value is effectively empty."""
    if not value:
        return True
    v = value.strip().strip('"').strip("'").strip()
    return v in ("", "N/A", "n/a", "Not specified", "PENDING", "Unknown")


def merge_yaml_fields(primary_content: str, dup_fields: dict) -> str:
    """
    Merge useful YAML fields from duplicate into primary paper.
    Only adds fields that are missing or empty in the primary.
    """
    fm_match = re.match(r"---\n(.*?)\n---\n", primary_content, re.DOTALL)
    if not fm_match:
        return primary_content

    frontmatter = fm_match.group(1)
    body = primary_content[fm_match.end():]

    primary_fields = parse_frontmatter(frontmatter)

    # Fields worth merging from duplicate
    MERGE_FIELDS = [
        "doi", "publication", "key_contribution", "significance",
        "data_description", "data_metrics", "DATE_ADDED",
        "national_ethnic_cultural", "religious_values", "moral_psychology",
        "mp_mft", "mp_schwartz", "mp_trolley", "mp_kohlberg",
        "mp_dual_process", "mp_intuitionist", "mp_dyadic", "mp_identity",
    ] + list(RV_FIELDS)

    merged_count = 0
    for field in MERGE_FIELDS:
        dup_val = dup_fields.get(field, "")
        primary_val = primary_fields.get(field, "")

        if not is_empty_field(dup_val) and is_empty_field(primary_val):
            # Primary is missing this field — add from duplicate
            frontmatter, count = safe_replace_field(frontmatter, field, dup_val.strip('"').strip("'"))
            if count == 0:
                # Field doesn't exist in primary at all — add it
                frontmatter = safe_add_field(frontmatter, field, dup_val.strip('"').strip("'"))
            merged_count += 1

    # Special: prefer longer abstract
    dup_abstract = dup_fields.get("abstract", "")
    primary_abstract = primary_fields.get("abstract", "")
    if len(dup_abstract) > len(primary_abstract) + 50:
        frontmatter, _ = safe_replace_field(frontmatter, "abstract", dup_abstract.strip('"').strip("'"))
        merged_count += 1

    # Special: prefer higher ethics_overall score (supports both "Yes"/"No" and integer scores)
    dup_ethics_raw = dup_fields.get("ethics_overall", "").strip('"').strip("'").strip()
    primary_ethics_raw = primary_fields.get("ethics_overall", "").strip('"').strip("'").strip()
    dup_ethics_score = parse_ethics_value(dup_ethics_raw)
    primary_ethics_score = parse_ethics_value(primary_ethics_raw)
    if dup_ethics_score > primary_ethics_score:
        frontmatter, _ = safe_replace_field(frontmatter, "ethics_overall", str(dup_ethics_score))
        merged_count += 1

    # Special: prefer higher mp_* scores (0-100 integer)
    for mp_field in ("mp_mft", "mp_schwartz", "mp_trolley", "mp_kohlberg",
                      "mp_dual_process", "mp_intuitionist", "mp_dyadic", "mp_identity"):
        dup_val = dup_fields.get(mp_field, "").strip('"').strip("'").strip()
        primary_val = primary_fields.get(mp_field, "").strip('"').strip("'").strip()
        try:
            dup_score = int(dup_val) if dup_val else 0
        except ValueError:
            dup_score = 0
        try:
            primary_score = int(primary_val) if primary_val else 0
        except ValueError:
            primary_score = 0
        if dup_score > primary_score:
            frontmatter, _ = safe_replace_field(frontmatter, mp_field, str(dup_score))
            merged_count += 1

    # Special: prefer higher rv_* scores (0-100 integer)
    for rv_field in RV_FIELDS:
        dup_val = dup_fields.get(rv_field, "").strip('"').strip("'").strip()
        primary_val = primary_fields.get(rv_field, "").strip('"').strip("'").strip()
        dup_score = parse_rv_value(dup_val)
        primary_score = parse_rv_value(primary_val)
        if dup_score > primary_score:
            frontmatter, _ = safe_replace_field(frontmatter, rv_field, str(dup_score))
            merged_count += 1

    # Special: merge is_benchmark/is_eval/is_dataset if dup says Yes and primary says No
    for bool_field in ("is_benchmark", "is_eval", "is_dataset"):
        dup_val = dup_fields.get(bool_field, "").strip('"').strip("'").strip()
        primary_val = primary_fields.get(bool_field, "").strip('"').strip("'").strip()
        if dup_val.lower() == "yes" and primary_val.lower() == "no":
            frontmatter, _ = safe_replace_field(frontmatter, bool_field, "Yes")
            merged_count += 1

    if merged_count > 0:
        return f"---\n{frontmatter}\n---\n{body}"
    return primary_content


# ============================================================
# B-D. File Operations
# ============================================================

def recycle_file(file_path: Path, dry_run: bool) -> bool:
    """Move a file to RECYCLE-BIN. Returns True if moved."""
    if not file_path.exists():
        return False

    dest = RECYCLE_BIN_DIR / file_path.name
    # Handle name collisions in recycle bin
    if dest.exists():
        stem = file_path.stem
        suffix = file_path.suffix
        counter = 2
        while dest.exists():
            dest = RECYCLE_BIN_DIR / f"{stem}_dup{counter}{suffix}"
            counter += 1

    if dry_run:
        print(f"    [DRY] Recycle: {file_path.name}")
    else:
        shutil.move(str(file_path), str(dest))
        print(f"    Recycled: {file_path.name}")
    return True


def find_pdf_on_disk(fields: dict) -> Optional[Path]:
    """Find the PDF file on disk for a paper."""
    local_pdf = fields.get("local_pdf", "")
    if not local_pdf or local_pdf.strip('"').strip("'").upper() in ("N/A", "NO_PDF_APPLICABLE"):
        return None

    pdf_ref = local_pdf.strip('"').strip("'").strip("[]").replace("[[", "").replace("]]", "")
    pdf_ref = pdf_ref.replace("PDFs/", "")
    pdf_path = PDFS_DIR / pdf_ref
    if pdf_path.exists():
        return pdf_path
    return None


def find_extract_on_disk(fields: dict) -> Optional[Path]:
    """Find the PDF extract file on disk for a paper."""
    extract_ref = fields.get("pdf_extract", "")
    if not extract_ref:
        return None

    extract_ref = extract_ref.strip('"').strip("'").replace("PDF Extracts/", "")
    extract_path = PDF_EXTRACTS_DIR / extract_ref
    if extract_path.exists():
        return extract_path
    return None


def transfer_pdf_to_primary(primary_content: str, primary_fields: dict,
                            dup_pdf_path: Path, dry_run: bool) -> str:
    """
    If primary has no PDF but duplicate does, update primary's local_pdf
    to point to the duplicate's PDF (no rename needed, just update YAML).
    """
    # Primary already has a PDF — nothing to do
    if find_pdf_on_disk(primary_fields):
        return primary_content

    # Build wikilink for the duplicate's PDF (it stays in place)
    pdf_rel = dup_pdf_path.relative_to(PDFS_DIR)
    wikilink = f'"[[PDFs/{pdf_rel}]]"'

    fm_match = re.match(r"---\n(.*?)\n---\n", primary_content, re.DOTALL)
    if not fm_match:
        return primary_content

    frontmatter = fm_match.group(1)
    body = primary_content[fm_match.end():]

    frontmatter, count = safe_replace_field(frontmatter, "local_pdf", f"[[PDFs/{pdf_rel}]]")
    if count == 0:
        frontmatter = safe_add_field(frontmatter, "local_pdf", f"[[PDFs/{pdf_rel}]]")

    if not dry_run:
        print(f"    Transferred PDF reference: {dup_pdf_path.name}")
    else:
        print(f"    [DRY] Transfer PDF reference: {dup_pdf_path.name}")

    return f"---\n{frontmatter}\n---\n{body}"


def transfer_extract_to_primary(primary_content: str, primary_fields: dict,
                                dup_extract_path: Path, dry_run: bool) -> str:
    """
    If primary has no extract but duplicate does, update primary's pdf_extract.
    """
    if find_extract_on_disk(primary_fields):
        return primary_content

    extract_rel = dup_extract_path.relative_to(PDF_EXTRACTS_DIR)
    extract_value = f"PDF Extracts/{extract_rel}"

    fm_match = re.match(r"---\n(.*?)\n---\n", primary_content, re.DOTALL)
    if not fm_match:
        return primary_content

    frontmatter = fm_match.group(1)
    body = primary_content[fm_match.end():]

    frontmatter, count = safe_replace_field(frontmatter, "pdf_extract", extract_value)
    if count == 0:
        frontmatter = safe_add_field(frontmatter, "pdf_extract", extract_value)

    if not dry_run:
        print(f"    Transferred extract reference: {dup_extract_path.name}")
    else:
        print(f"    [DRY] Transfer extract reference: {dup_extract_path.name}")

    return f"---\n{frontmatter}\n---\n{body}"


# ============================================================
# E-F. Cross-Reference Updates
# ============================================================

def update_cross_references(rename_map: Dict[str, str], dry_run: bool) -> int:
    """
    Update wikilinks across all .md files (Authors, STATISTICS, AI Labs, papers).
    rename_map: {old_stem: primary_stem}

    Returns count of files modified.
    """
    if not rename_map:
        return 0

    files_modified = 0

    # Directories to scan
    scan_dirs = [AUTHORS_DIR, STATISTICS_DIR, AI_LABS_DIR, PAPERS_DIR]

    for scan_dir in scan_dirs:
        if not scan_dir.exists():
            continue
        for md_path in scan_dir.rglob("*.md"):
            # Skip RECYCLE-BIN
            try:
                rel = md_path.relative_to(WS_ROOT)
            except ValueError:
                continue
            if "RECYCLE-BIN" in str(rel):
                continue

            try:
                content = md_path.read_text(encoding="utf-8")
            except Exception:
                continue

            original = content

            for old_stem, new_stem in rename_map.items():
                if old_stem not in content:
                    continue

                # Replace [[old_stem]] -> [[new_stem]]
                content = content.replace(f"[[{old_stem}]]", f"[[{new_stem}]]")

                # Replace [[old_stem|display]] -> [[new_stem|display]]
                content = re.sub(
                    rf'\[\[{re.escape(old_stem)}\|([^\]]+)\]\]',
                    rf'[[{new_stem}|\1]]',
                    content
                )

            if content != original:
                if dry_run:
                    print(f"    [DRY] Update xrefs in: {rel}")
                else:
                    md_path.write_text(content, encoding="utf-8")
                    print(f"    Updated xrefs in: {rel}")
                files_modified += 1

    return files_modified


def deduplicate_author_wikilinks(authors_dir: Path, primary_stem: str,
                                  dup_stems: List[str], dry_run: bool) -> int:
    """
    After replacing dup wikilinks with primary, remove duplicate entries
    in author profile paper lists.
    Returns count of files cleaned.
    """
    cleaned = 0

    for author_path in authors_dir.glob("*.md"):
        if author_path.name in ("README.md", "TEMPLATE.md"):
            continue

        try:
            content = author_path.read_text(encoding="utf-8")
        except Exception:
            continue

        if f"[[{primary_stem}]]" not in content and f"[[{primary_stem}|" not in content:
            continue

        # Find and remove duplicate list entries pointing to primary
        lines = content.split("\n")
        seen_primary = False
        new_lines = []
        removed = False

        for line in lines:
            # Check if this line is a list entry referencing the primary
            is_primary_ref = (
                f"[[{primary_stem}]]" in line or f"[[{primary_stem}|" in line
            ) and line.strip().startswith("- ")

            if is_primary_ref:
                if seen_primary:
                    # Duplicate reference — skip
                    removed = True
                    continue
                seen_primary = True

            new_lines.append(line)

        if removed:
            new_content = "\n".join(new_lines)
            if not dry_run:
                author_path.write_text(new_content, encoding="utf-8")
            cleaned += 1

    return cleaned


# ============================================================
# Main
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Consolidate duplicate papers")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without applying")
    parser.add_argument("--input", type=str, default=None, help="Path to duplicate_groups.json")
    args = parser.parse_args()

    today = date.today().strftime("%Y%m%d")

    # Find input file
    if args.input:
        input_path = Path(args.input)
        if not input_path.is_absolute():
            input_path = WORKSPACE_ROOT / input_path
    else:
        # Auto-detect latest
        candidates = sorted(LOGS_DIR.glob("*-duplicate_groups.json"), reverse=True)
        if not candidates:
            print("ERROR: No duplicate_groups.json found. Run detect_duplicates.py first.")
            sys.exit(1)
        input_path = candidates[0]

    print("=" * 80)
    print(f"CONSOLIDATE DUPLICATES {'(DRY RUN)' if args.dry_run else '(LIVE)'}")
    print(f"Input: {input_path.name}")
    print("=" * 80)

    with open(input_path, "r", encoding="utf-8") as f:
        groups = json.load(f)

    print(f"Loaded {len(groups)} duplicate groups")

    # Ensure RECYCLE-BIN exists
    RECYCLE_BIN_DIR.mkdir(parents=True, exist_ok=True)

    # Track changes for report
    stats = {
        "groups_processed": 0,
        "papers_recycled": 0,
        "pdfs_recycled": 0,
        "extracts_recycled": 0,
        "fields_merged": 0,
        "xrefs_updated": 0,
        "author_deduped": 0,
        "pdfs_transferred": 0,
        "extracts_transferred": 0,
        "errors": 0,
        "skipped": 0,
    }

    # rename_map: dup_stem -> primary_stem (for cross-reference updates)
    rename_map = {}
    report_entries = []

    for g in groups:
        group_id = g["group_id"]
        papers = g["papers"]
        shared_ids = g.get("shared_identifiers", [])

        primary = [p for p in papers if p["is_primary"]][0]
        duplicates = [p for p in papers if not p["is_primary"]]

        ids_str = ", ".join(f"{s['type']}:{s['value']}" for s in shared_ids)
        print(f"\n  Group {group_id}: {ids_str}")
        print(f"    PRIMARY: {primary['filename']} (key={primary['key']}, richness={primary['richness_score']})")

        primary_path = PAPERS_DIR / primary["filename"]
        if not primary_path.exists():
            print(f"    ERROR: Primary paper not found: {primary['filename']}")
            stats["errors"] += 1
            continue

        # Read primary content
        primary_content = primary_path.read_text(encoding="utf-8")
        primary_fm, _ = extract_frontmatter(primary_content)
        primary_fields = parse_frontmatter(primary_fm)

        report_entry = {
            "group_id": group_id,
            "shared_identifiers": shared_ids,
            "primary": primary["filename"],
            "primary_key": primary["key"],
            "recycled": [],
            "fields_merged": [],
            "pdf_action": None,
            "extract_action": None,
        }

        for dup in duplicates:
            dup_path = PAPERS_DIR / dup["filename"]
            dup_stem = Path(dup["filename"]).stem
            primary_stem = Path(primary["filename"]).stem

            print(f"    RECYCLE: {dup['filename']} (key={dup['key']}, richness={dup['richness_score']})")

            if not dup_path.exists():
                print(f"    WARNING: Duplicate paper not found: {dup['filename']}")
                stats["skipped"] += 1
                continue

            # Read duplicate content for field merging
            try:
                dup_content = dup_path.read_text(encoding="utf-8")
                dup_fm, _ = extract_frontmatter(dup_content)
                dup_fields = parse_frontmatter(dup_fm)
            except Exception as e:
                print(f"    WARNING: Could not parse duplicate: {e}")
                dup_fields = {}

            # A. Merge YAML fields
            old_content = primary_content
            primary_content = merge_yaml_fields(primary_content, dup_fields)
            if primary_content != old_content:
                merged_fields = []
                # Determine which fields were actually merged
                new_fm, _ = extract_frontmatter(primary_content)
                new_fields = parse_frontmatter(new_fm)
                for k in new_fields:
                    old_v = primary_fields.get(k, "")
                    new_v = new_fields.get(k, "")
                    if old_v != new_v:
                        merged_fields.append(k)
                report_entry["fields_merged"].extend(merged_fields)
                stats["fields_merged"] += len(merged_fields)
                print(f"      Merged fields: {', '.join(merged_fields)}")

            # C. Handle PDF
            dup_pdf = find_pdf_on_disk(dup_fields)
            primary_pdf = find_pdf_on_disk(primary_fields)

            if dup_pdf:
                if primary_pdf:
                    # Both have PDFs — recycle duplicate's
                    recycle_file(dup_pdf, args.dry_run)
                    stats["pdfs_recycled"] += 1
                    report_entry["pdf_action"] = f"recycled {dup_pdf.name}"
                else:
                    # Primary lacks PDF, duplicate has one — transfer reference
                    primary_content = transfer_pdf_to_primary(
                        primary_content, primary_fields, dup_pdf, args.dry_run
                    )
                    stats["pdfs_transferred"] += 1
                    report_entry["pdf_action"] = f"transferred {dup_pdf.name} to primary"
                    # Re-parse primary fields after update
                    primary_fm, _ = extract_frontmatter(primary_content)
                    primary_fields = parse_frontmatter(primary_fm)

            # D. Handle extract
            dup_extract = find_extract_on_disk(dup_fields)
            primary_extract = find_extract_on_disk(primary_fields)

            if dup_extract:
                if primary_extract:
                    # Both have extracts — recycle duplicate's
                    recycle_file(dup_extract, args.dry_run)
                    stats["extracts_recycled"] += 1
                    report_entry["extract_action"] = f"recycled {dup_extract.name}"
                else:
                    # Primary lacks extract — transfer reference
                    primary_content = transfer_extract_to_primary(
                        primary_content, primary_fields, dup_extract, args.dry_run
                    )
                    stats["extracts_transferred"] += 1
                    report_entry["extract_action"] = f"transferred {dup_extract.name} to primary"
                    # Re-parse
                    primary_fm, _ = extract_frontmatter(primary_content)
                    primary_fields = parse_frontmatter(primary_fm)

            # B. Move duplicate paper to RECYCLE-BIN
            recycle_file(dup_path, args.dry_run)
            stats["papers_recycled"] += 1
            report_entry["recycled"].append(dup["filename"])

            # Track for cross-reference updates
            rename_map[dup_stem] = primary_stem

        # Write updated primary content
        if primary_content != primary_path.read_text(encoding="utf-8"):
            if not args.dry_run:
                primary_path.write_text(primary_content, encoding="utf-8")
            print(f"    Updated primary: {primary['filename']}")

        stats["groups_processed"] += 1
        report_entries.append(report_entry)

    # E-F. Cross-reference updates
    if rename_map:
        print(f"\n{'='*80}")
        print("CROSS-REFERENCE UPDATES")
        print(f"{'='*80}")
        print(f"  {len(rename_map)} stems to update")

        xref_count = update_cross_references(rename_map, args.dry_run)
        stats["xrefs_updated"] = xref_count
        print(f"  Updated {xref_count} files")

        # Deduplicate author wikilinks
        print(f"\n  Deduplicating author profile wikilinks...")
        author_dedup_count = 0
        for dup_stem, primary_stem in rename_map.items():
            count = deduplicate_author_wikilinks(
                AUTHORS_DIR, primary_stem, [dup_stem], args.dry_run
            )
            author_dedup_count += count
        stats["author_deduped"] = author_dedup_count
        print(f"  Cleaned {author_dedup_count} author profiles")

    # Summary
    print(f"\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    print(f"  Groups processed:      {stats['groups_processed']}")
    print(f"  Papers recycled:       {stats['papers_recycled']}")
    print(f"  PDFs recycled:         {stats['pdfs_recycled']}")
    print(f"  PDFs transferred:      {stats['pdfs_transferred']}")
    print(f"  Extracts recycled:     {stats['extracts_recycled']}")
    print(f"  Extracts transferred:  {stats['extracts_transferred']}")
    print(f"  Fields merged:         {stats['fields_merged']}")
    print(f"  Cross-refs updated:    {stats['xrefs_updated']}")
    print(f"  Author profiles deduped: {stats['author_deduped']}")
    print(f"  Errors:                {stats['errors']}")
    print(f"  Skipped:               {stats['skipped']}")

    # Expected new paper count
    current_papers = len(list(PAPERS_DIR.glob("*.md")))
    expected_after = current_papers - (0 if args.dry_run else stats["papers_recycled"])
    print(f"\n  Current papers: {current_papers}")
    print(f"  Expected after: {expected_after}")

    # Save report
    report = {
        "date": today,
        "mode": "dry_run" if args.dry_run else "live",
        "stats": stats,
        "rename_map": rename_map,
        "groups": report_entries,
    }

    report_json_path = LOGS_DIR / f"{today}-dedup_consolidation_log.json"
    with open(report_json_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\n  Report JSON: {report_json_path.relative_to(WORKSPACE_ROOT)}")

    # Generate markdown report
    if not args.dry_run:
        generate_markdown_report(report, report_entries, stats, rename_map, today)

    if not args.dry_run:
        print(f"\n  Next: ../.venv/bin/python PYTHON/validate_all_papers.py")


def generate_markdown_report(report: dict, entries: list, stats: dict,
                             rename_map: dict, today: str):
    """Generate a human-readable markdown report."""
    lines = [
        f"# Deduplication Consolidation Report",
        f"",
        f"**Date:** {today}",
        f"**Mode:** {'Dry Run' if report['mode'] == 'dry_run' else 'Live'}",
        f"",
        f"## Summary",
        f"",
        f"| Metric | Count |",
        f"|--------|-------|",
        f"| Groups processed | {stats['groups_processed']} |",
        f"| Papers recycled | {stats['papers_recycled']} |",
        f"| PDFs recycled | {stats['pdfs_recycled']} |",
        f"| PDFs transferred | {stats['pdfs_transferred']} |",
        f"| Extracts recycled | {stats['extracts_recycled']} |",
        f"| Extracts transferred | {stats['extracts_transferred']} |",
        f"| Fields merged | {stats['fields_merged']} |",
        f"| Cross-refs updated | {stats['xrefs_updated']} |",
        f"| Author profiles cleaned | {stats['author_deduped']} |",
        f"",
        f"## Per-Group Details",
        f"",
    ]

    for entry in entries:
        ids_str = ", ".join(f"{s['type']}:{s['value']}" for s in entry.get("shared_identifiers", []))
        lines.append(f"### Group {entry['group_id']}: {ids_str}")
        lines.append(f"")
        lines.append(f"- **Primary:** `{entry['primary']}` (key: {entry['primary_key']})")
        for r in entry.get("recycled", []):
            lines.append(f"- **Recycled:** `{r}`")
        if entry.get("fields_merged"):
            lines.append(f"- **Fields merged:** {', '.join(entry['fields_merged'])}")
        if entry.get("pdf_action"):
            lines.append(f"- **PDF:** {entry['pdf_action']}")
        if entry.get("extract_action"):
            lines.append(f"- **Extract:** {entry['extract_action']}")
        lines.append(f"")

    if rename_map:
        lines.append(f"## Cross-Reference Rename Map")
        lines.append(f"")
        lines.append(f"| Recycled Stem | Primary Stem |")
        lines.append(f"|---------------|--------------|")
        for old, new in sorted(rename_map.items()):
            lines.append(f"| `{old}` | `{new}` |")
        lines.append(f"")

    report_path = STATISTICS_DIR / f"{today}-dedup-consolidation-report.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  Report: {report_path.relative_to(WORKSPACE_ROOT)}")


if __name__ == "__main__":
    main()
