#!/usr/bin/env python3
"""
Normalize local_pdf and pdf_extract metadata fields across paper files.

Policy:
- Ensure every paper has both local_pdf and pdf_extract keys.
- Convert missing/blank local_pdf to local_pdf: N/A.
- If local_pdf resolves to a valid local PDF, point pdf_extract to the
  canonical existing extract path for the same PDF stem.
- If local_pdf is N/A (or unresolved), clear pdf_extract to blank.

This script only edits frontmatter and only touches local_pdf/pdf_extract lines.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from vault_config import LOGS_DIR, PAPERS_DIR, PDF_EXTRACTS_DIR, PDFS_DIR

NA_VALUES = {"N/A", "NA", "NONE", "NULL"}


def split_frontmatter(content: str) -> Optional[Tuple[str, str]]:
    """Return (frontmatter_without_markers, body_after_closing_marker)."""
    if not content.startswith("---\n"):
        return None

    match = re.search(r"\n---[ \t]*\n", content[4:])
    if not match:
        return None

    close_start = 4 + match.start()
    close_end = 4 + match.end()
    frontmatter = content[4:close_start]
    body = content[close_end:]
    return frontmatter, body


def parse_wikilink_or_plain(raw_value: str) -> str:
    value = raw_value.strip().strip('"').strip("'")
    if not value:
        return ""

    wiki_match = re.fullmatch(r"\[\[(.+?)\]\]", value)
    path = wiki_match.group(1) if wiki_match else value
    return path.split("|", 1)[0].strip()


def normalize_local_path(raw_value: str, pdf_set: set[str]) -> Tuple[str, str, Optional[str]]:
    """
    Return (classification, normalized_line_value, resolved_pdf_path).

    classification:
      - blank, na, valid, unresolved
    normalized_line_value:
      - canonical local_pdf value to write when needed (without key prefix)
    resolved_pdf_path:
      - repo-relative PDF path (e.g., Lit-WS-PDFs/2025/x.pdf) if valid, else None
    """
    raw = raw_value.strip().strip('"').strip("'")
    if raw == "":
        return "blank", "N/A", None

    if raw.upper() in NA_VALUES:
        return "na", "N/A", None

    path = parse_wikilink_or_plain(raw_value)
    if not path.lower().endswith(".pdf"):
        return "unresolved", raw_value.strip(), None

    if not path.startswith("Lit-WS-PDFs/"):
        path = "Lit-WS-PDFs/" + path.lstrip("/")

    if path in pdf_set:
        return "valid", f'"[[{path}]]"', path

    return "unresolved", raw_value.strip(), None


def choose_extract_path(
    pdf_path: str,
    extract_by_stem: Dict[str, List[str]],
) -> Tuple[Optional[str], str]:
    stem = Path(pdf_path).stem
    candidates = sorted(extract_by_stem.get(stem, []))
    if not candidates:
        return None, "missing_extract_file"

    if len(candidates) == 1:
        return candidates[0], "single"

    parent = Path(pdf_path).parent.name
    year = parent if len(parent) == 4 and parent.isdigit() else None
    if year:
        preferred = f"PDF Extracts/{year}/{stem}.md"
        if preferred in candidates:
            return preferred, "preferred_year"

        year_candidates = [c for c in candidates if f"/{year}/" in c]
        if len(year_candidates) == 1:
            return year_candidates[0], "year_unique"

    return candidates[0], "ambiguous_first_sorted"


def build_indices() -> Tuple[set[str], Dict[str, List[str]]]:
    pdf_set = {p.relative_to(PDFS_DIR.parent).as_posix() for p in PDFS_DIR.rglob("*.pdf")}

    extract_by_stem: Dict[str, List[str]] = {}
    for extract in PDF_EXTRACTS_DIR.rglob("*.md"):
        rel = extract.relative_to(PDF_EXTRACTS_DIR.parent).as_posix()
        extract_by_stem.setdefault(extract.stem, []).append(rel)

    return pdf_set, extract_by_stem


def normalize_file(
    paper_path: Path,
    pdf_set: set[str],
    extract_by_stem: Dict[str, List[str]],
    write: bool = True,
) -> Tuple[bool, Dict]:
    content = paper_path.read_text(encoding="utf-8", errors="ignore")
    split = split_frontmatter(content)
    if split is None:
        return False, {"paper": paper_path.name, "error": "frontmatter_unparseable"}

    frontmatter, body = split
    lines = frontmatter.split("\n")

    local_idx = None
    extract_idx = None
    local_raw = ""
    extract_raw = ""

    for idx, line in enumerate(lines):
        if local_idx is None and line.startswith("local_pdf:"):
            local_idx = idx
            local_raw = line[len("local_pdf:") :].strip()
        if extract_idx is None and line.startswith("pdf_extract:"):
            extract_idx = idx
            extract_raw = line[len("pdf_extract:") :].strip()

    changes: Dict[str, Dict] = {}
    changed = False

    # Ensure local_pdf exists.
    if local_idx is None:
        local_insert_idx = len(lines)
        lines.insert(local_insert_idx, "local_pdf: N/A")
        local_idx = local_insert_idx
        local_raw = "N/A"
        changed = True
        changes["local_pdf"] = {"from": None, "to": "local_pdf: N/A", "reason": "missing_to_na"}

    local_class, _local_normalized, resolved_pdf = normalize_local_path(local_raw, pdf_set)

    # Normalize local_pdf values for blank / non-canonical N/A.
    if local_class in {"blank", "na"}:
        new_line = "local_pdf: N/A"
        if lines[local_idx] != new_line:
            changes.setdefault("local_pdf", {"from": lines[local_idx], "to": new_line, "reason": f"{local_class}_to_na"})
            lines[local_idx] = new_line
            changed = True
        resolved_pdf = None

    # Ensure pdf_extract exists.
    if extract_idx is None:
        insert_at = local_idx
        lines.insert(insert_at, "pdf_extract: ")
        extract_idx = insert_at
        if local_idx is not None and local_idx >= insert_at:
            local_idx += 1
        extract_raw = ""
        changed = True
        changes["pdf_extract"] = {"from": None, "to": "pdf_extract: ", "reason": "missing_field_added"}

    # Enforce extract policy.
    unresolved_extract = None
    if resolved_pdf:
        desired_extract, reason = choose_extract_path(resolved_pdf, extract_by_stem)
        if desired_extract is None:
            desired_line = "pdf_extract: "
            unresolved_extract = {"reason": reason, "pdf": resolved_pdf}
        else:
            desired_line = f'pdf_extract: "{desired_extract}"'

        if lines[extract_idx] != desired_line:
            changes["pdf_extract"] = {
                "from": lines[extract_idx],
                "to": desired_line,
                "reason": f"local_pdf_valid:{reason}",
            }
            lines[extract_idx] = desired_line
            changed = True
    else:
        # local_pdf is N/A (or unresolved): clear extract field.
        desired_line = "pdf_extract: "
        if lines[extract_idx] != desired_line:
            changes["pdf_extract"] = {
                "from": lines[extract_idx],
                "to": desired_line,
                "reason": "no_local_pdf_clear_extract",
            }
            lines[extract_idx] = desired_line
            changed = True

    # Ensure ordering: pdf_extract before local_pdf.
    if extract_idx > local_idx:
        extract_line = lines.pop(extract_idx)
        lines.insert(local_idx, extract_line)
        changed = True
        changes["field_order"] = {
            "reason": "moved_pdf_extract_before_local_pdf",
        }
        extract_idx = local_idx
        local_idx += 1

    if changed and write:
        new_frontmatter = "\n".join(lines)
        new_content = f"---\n{new_frontmatter}\n---\n{body}"
        paper_path.write_text(new_content, encoding="utf-8")

    result = {"paper": paper_path.name, "changed": changed}
    if changes:
        result["changes"] = changes
    if unresolved_extract:
        result["unresolved"] = unresolved_extract
    if local_class == "unresolved":
        result["unresolved_local_pdf"] = local_raw
    return changed, result


def summarize(results: List[Dict]) -> Dict[str, int]:
    summary = {
        "papers_scanned": len(results),
        "papers_changed": 0,
        "local_missing_to_na": 0,
        "local_blank_to_na": 0,
        "local_noncanonical_na_to_na": 0,
        "pdf_extract_missing_added": 0,
        "pdf_extract_set_from_valid_local_pdf": 0,
        "pdf_extract_cleared_without_local_pdf": 0,
        "field_order_adjusted": 0,
        "unresolved_extract_for_valid_local_pdf": 0,
        "unresolved_local_pdf_values": 0,
    }

    for item in results:
        if item.get("changed"):
            summary["papers_changed"] += 1
        if "changes" in item:
            local_change = item["changes"].get("local_pdf")
            if local_change:
                reason = local_change.get("reason", "")
                if reason == "missing_to_na":
                    summary["local_missing_to_na"] += 1
                elif reason == "blank_to_na":
                    summary["local_blank_to_na"] += 1
                elif reason == "na_to_na":
                    summary["local_noncanonical_na_to_na"] += 1

            extract_change = item["changes"].get("pdf_extract")
            if extract_change:
                reason = extract_change.get("reason", "")
                if reason == "missing_field_added":
                    summary["pdf_extract_missing_added"] += 1
                elif reason.startswith("local_pdf_valid:"):
                    summary["pdf_extract_set_from_valid_local_pdf"] += 1
                elif reason == "no_local_pdf_clear_extract":
                    summary["pdf_extract_cleared_without_local_pdf"] += 1

            if "field_order" in item["changes"]:
                summary["field_order_adjusted"] += 1

        if item.get("unresolved"):
            summary["unresolved_extract_for_valid_local_pdf"] += 1
        if item.get("unresolved_local_pdf"):
            summary["unresolved_local_pdf_values"] += 1

    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Normalize local_pdf/pdf_extract metadata fields.")
    parser.add_argument("--dry-run", action="store_true", help="Compute changes without writing files.")
    parser.add_argument("--log-path", type=Path, default=None, help="Optional path for JSON run log.")
    args = parser.parse_args()

    date_tag = dt.datetime.now().strftime("%Y%m%d")
    log_path = args.log_path or (LOGS_DIR / f"{date_tag}-normalize-pdf-metadata-fields.json")

    pdf_set, extract_by_stem = build_indices()
    results: List[Dict] = []

    for paper in sorted(PAPERS_DIR.glob("*.md")):
        if args.dry_run:
            changed, item = normalize_file(paper, pdf_set, extract_by_stem, write=False)
            item["changed"] = changed
            results.append(item)
            continue

        changed, item = normalize_file(paper, pdf_set, extract_by_stem)
        item["changed"] = changed
        results.append(item)

    summary = summarize(results)
    report = {
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "dry_run": args.dry_run,
        "summary": summary,
        "results": results,
    }
    log_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(f"log_path={log_path}")


if __name__ == "__main__":
    main()
