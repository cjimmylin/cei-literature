#!/usr/bin/env python3
"""
Sync updated author-name filenames across papers, PDFs, and PDF extracts.

Scope:
- Only papers listed as changed in a repair log (default: 20260214 author repair log).
- Only high-confidence cases where:
  - Filename author token is placeholder-like (e.g., authors, Unknown, results]]).
  - first_author is concrete and yields a usable surname token.
  - paper/local_pdf/pdf_extract stems match and target names do not collide.

Behavior:
- Dry run by default.
- In apply mode:
  1) Rename paper, PDF, and extract files.
  2) Update paper frontmatter local_pdf/pdf_extract fields.
  3) Update extract metadata/header source references.
  4) Propagate path and stem wikilink references across markdown files.
  5) Validate updated assets and produce JSON/CSV reports.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

from vault_config import LOGS_DIR, PAPERS_DIR, PDFS_DIR, PDF_EXTRACTS_DIR, WORKSPACE_ROOT


PLACEHOLDER_AUTHOR_RE = re.compile(
    r"\bunknown\b|\bauthors?\b|not fully|results\]\]|^\s*na\s*$",
    re.IGNORECASE,
)

PLACEHOLDER_FILENAME_SLUGS = {
    "authors",
    "unknown",
    "[[unknown]]",
    "results]]",
    "search",
    "retrieved",
    "available",
    "initiative",
    "paper",
    "group)",
    "at",
    "with.pdf",
}

WIKILINK_RE = re.compile(r"^\[\[(.+?)\]\]$")


@dataclass
class Candidate:
    paper_filename: str
    old_stem: str
    new_stem: str
    old_slug: str
    new_slug: str
    old_paper_path: Path
    new_paper_path: Path
    old_pdf_rel: str
    new_pdf_rel: str
    old_pdf_path: Path
    new_pdf_path: Path
    old_extract_rel: str
    new_extract_rel: str
    old_extract_path: Path
    new_extract_path: Path


def split_frontmatter(content: str) -> Optional[Tuple[str, str]]:
    if not content.startswith("---\n"):
        return None
    end = content.find("\n---\n", 4)
    if end == -1:
        return None
    frontmatter = content[4:end]
    body = content[end + 5 :]
    return frontmatter, body


def extract_field(frontmatter: str, key: str) -> Optional[str]:
    prefix = f"{key}:"
    for line in frontmatter.splitlines():
        if line.startswith(prefix):
            return line[len(prefix) :].strip()
    return None


def parse_link_or_plain(raw_value: str) -> str:
    value = raw_value.strip().strip('"').strip("'")
    if not value:
        return ""

    wiki_match = WIKILINK_RE.fullmatch(value)
    if wiki_match:
        value = wiki_match.group(1)

    value = value.split("|", 1)[0].strip()
    return value


def parse_first_author_slug(raw_value: Optional[str]) -> Optional[str]:
    if raw_value is None:
        return None

    value = raw_value.strip().strip('"').strip("'")
    if not value:
        return None

    wiki_match = WIKILINK_RE.fullmatch(value)
    if wiki_match:
        value = wiki_match.group(1).strip()

    if PLACEHOLDER_AUTHOR_RE.search(value):
        return None

    if "," in value:
        surname = value.split(",", 1)[0].strip()
    else:
        parts = value.split()
        if not parts:
            return None
        surname = parts[-1].strip()

    if not surname:
        return None

    slug = "-".join(surname.split()).strip("-")
    if not slug:
        return None

    if any(ch in slug for ch in ("/", "\\", ":")):
        return None
    return slug


def set_or_add_field(frontmatter: str, key: str, value: str) -> str:
    lines = frontmatter.splitlines()
    prefix = f"{key}:"
    replaced = False

    for idx, line in enumerate(lines):
        if line.startswith(prefix):
            lines[idx] = f"{prefix} {value}"
            replaced = True
            break

    if not replaced:
        lines.append(f"{prefix} {value}")

    return "\n".join(lines)


def resolve_pdf_path(local_pdf_rel: str) -> Optional[Path]:
    if not local_pdf_rel.startswith("Lit-WS-PDFs/"):
        return None
    suffix = local_pdf_rel[len("Lit-WS-PDFs/") :]
    return PDFS_DIR / suffix


def resolve_extract_path(extract_rel: str) -> Optional[Path]:
    if not extract_rel.startswith("PDF Extracts/"):
        return None
    return WORKSPACE_ROOT / extract_rel


def rel_pdf_from_path(pdf_path: Path) -> str:
    return f"Lit-WS-PDFs/{pdf_path.relative_to(PDFS_DIR).as_posix()}"


def rel_extract_from_path(extract_path: Path) -> str:
    return f"PDF Extracts/{extract_path.relative_to(PDF_EXTRACTS_DIR).as_posix()}"


def rel_paper_from_path(paper_path: Path) -> str:
    return f"papers/{paper_path.name}"


def load_changed_papers(input_log: Path) -> List[str]:
    data = json.loads(input_log.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or "results" not in data:
        raise ValueError("Input log missing expected top-level 'results' list")

    out: List[str] = []
    for item in data["results"]:
        if not isinstance(item, dict):
            continue
        if item.get("changed") is True and isinstance(item.get("paper"), str):
            out.append(item["paper"])
    return out


def build_candidate(paper_filename: str) -> Tuple[Optional[Candidate], str]:
    paper_path = PAPERS_DIR / paper_filename
    if not paper_path.exists():
        return None, "paper_missing"

    old_stem = paper_path.stem
    parts = old_stem.split("-", 2)
    if len(parts) < 3:
        return None, "bad_stem_format"

    year, old_slug, _title_part = parts
    if old_slug.lower() not in PLACEHOLDER_FILENAME_SLUGS:
        return None, "old_slug_not_placeholder"

    split = split_frontmatter(paper_path.read_text(encoding="utf-8", errors="ignore"))
    if split is None:
        return None, "frontmatter_unparseable"

    frontmatter, _body = split
    new_slug = parse_first_author_slug(extract_field(frontmatter, "first_author"))
    if not new_slug:
        return None, "first_author_not_concrete"
    if new_slug.lower() == old_slug.lower():
        return None, "already_matches"

    marker = f"{year}-{old_slug}-"
    if marker not in old_stem:
        return None, "old_slug_pattern_not_found"

    new_stem = old_stem.replace(marker, f"{year}-{new_slug}-", 1)

    local_pdf_value = extract_field(frontmatter, "local_pdf")
    extract_value = extract_field(frontmatter, "pdf_extract")
    if local_pdf_value is None or extract_value is None:
        return None, "missing_link_fields"

    old_pdf_rel = parse_link_or_plain(local_pdf_value)
    old_extract_rel = parse_link_or_plain(extract_value)
    if not old_pdf_rel.startswith("Lit-WS-PDFs/") or not old_extract_rel.startswith("PDF Extracts/"):
        return None, "nonlocal_or_blank_links"

    old_pdf_path = resolve_pdf_path(old_pdf_rel)
    old_extract_path = resolve_extract_path(old_extract_rel)
    if old_pdf_path is None or old_extract_path is None:
        return None, "path_resolution_failed"
    if not old_pdf_path.exists() or not old_extract_path.exists():
        return None, "linked_file_missing"

    if old_pdf_path.stem != old_stem or old_extract_path.stem != old_stem:
        return None, "linked_stem_mismatch"

    new_paper_path = paper_path.with_name(f"{new_stem}.md")
    new_pdf_path = old_pdf_path.with_name(f"{new_stem}.pdf")
    new_extract_path = old_extract_path.with_name(f"{new_stem}.md")

    target_conflicts = (
        (new_paper_path.exists() and new_paper_path != paper_path)
        or (new_pdf_path.exists() and new_pdf_path != old_pdf_path)
        or (new_extract_path.exists() and new_extract_path != old_extract_path)
    )
    if target_conflicts:
        return None, "target_collision"

    candidate = Candidate(
        paper_filename=paper_filename,
        old_stem=old_stem,
        new_stem=new_stem,
        old_slug=old_slug,
        new_slug=new_slug,
        old_paper_path=paper_path,
        new_paper_path=new_paper_path,
        old_pdf_rel=old_pdf_rel,
        new_pdf_rel=rel_pdf_from_path(new_pdf_path),
        old_pdf_path=old_pdf_path,
        new_pdf_path=new_pdf_path,
        old_extract_rel=old_extract_rel,
        new_extract_rel=rel_extract_from_path(new_extract_path),
        old_extract_path=old_extract_path,
        new_extract_path=new_extract_path,
    )
    return candidate, "candidate"


def update_renamed_paper_frontmatter(candidate: Candidate) -> None:
    content = candidate.new_paper_path.read_text(encoding="utf-8", errors="ignore")
    split = split_frontmatter(content)
    if split is None:
        raise RuntimeError(f"Frontmatter unparseable after rename: {candidate.new_paper_path.name}")

    frontmatter, body = split
    frontmatter = set_or_add_field(frontmatter, "local_pdf", f'"[[{candidate.new_pdf_rel}]]"')
    frontmatter = set_or_add_field(frontmatter, "pdf_extract", f'"{candidate.new_extract_rel}"')
    candidate.new_paper_path.write_text(f"---\n{frontmatter}\n---\n{body}", encoding="utf-8")


def update_renamed_extract_metadata(candidate: Candidate) -> None:
    text = candidate.new_extract_path.read_text(encoding="utf-8", errors="ignore")
    old_pdf_name = f"{candidate.old_stem}.pdf"
    new_pdf_name = f"{candidate.new_stem}.pdf"

    patterns = [
        (
            rf'(?m)^title:\s*"{re.escape(candidate.old_stem)} - PDF Extract"\s*$',
            f'title: "{candidate.new_stem} - PDF Extract"',
        ),
        (
            rf'(?m)^source_pdf:\s*"{re.escape(old_pdf_name)}"\s*$',
            f'source_pdf: "{new_pdf_name}"',
        ),
        (
            rf"(?m)^# PDF Extract: {re.escape(candidate.old_stem)}\s*$",
            f"# PDF Extract: {candidate.new_stem}",
        ),
        (
            rf"(?m)^\*\*Source PDF:\*\* {re.escape(old_pdf_name)}\s*$",
            f"**Source PDF:** {new_pdf_name}",
        ),
    ]

    new_text = text
    for pattern, replacement in patterns:
        new_text = re.sub(pattern, replacement, new_text, count=1)

    candidate.new_extract_path.write_text(new_text, encoding="utf-8")


def apply_candidate(candidate: Candidate) -> None:
    for old_path, new_path in (
        (candidate.old_paper_path, candidate.new_paper_path),
        (candidate.old_pdf_path, candidate.new_pdf_path),
        (candidate.old_extract_path, candidate.new_extract_path),
    ):
        if not old_path.exists():
            raise RuntimeError(f"Missing source path: {old_path}")
        if new_path.exists() and new_path != old_path:
            raise RuntimeError(f"Target collision: {new_path}")

    rollback_ops: List[Tuple[Path, Path]] = []
    try:
        candidate.old_paper_path.rename(candidate.new_paper_path)
        rollback_ops.append((candidate.new_paper_path, candidate.old_paper_path))

        candidate.old_pdf_path.rename(candidate.new_pdf_path)
        rollback_ops.append((candidate.new_pdf_path, candidate.old_pdf_path))

        candidate.old_extract_path.rename(candidate.new_extract_path)
        rollback_ops.append((candidate.new_extract_path, candidate.old_extract_path))
    except Exception as exc:
        for src, dst in reversed(rollback_ops):
            if src.exists() and not dst.exists():
                src.rename(dst)
        raise RuntimeError(f"Rename step failed and was rolled back: {exc}") from exc

    update_renamed_paper_frontmatter(candidate)
    update_renamed_extract_metadata(candidate)


def replace_with_count(text: str, old: str, new: str) -> Tuple[str, int]:
    count = text.count(old)
    if count == 0:
        return text, 0
    return text.replace(old, new), count


def propagate_references(candidates: Iterable[Candidate], apply: bool) -> Dict[str, object]:
    markdown_files = sorted(WORKSPACE_ROOT.rglob("*.md"))
    files_changed = 0
    replacements = 0
    changed_paths: List[str] = []

    for md_file in markdown_files:
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        new_text = text
        file_changes = 0

        for c in candidates:
            old_paper_rel = rel_paper_from_path(c.old_paper_path)
            new_paper_rel = rel_paper_from_path(c.new_paper_path)

            for old_value, new_value in (
                (old_paper_rel, new_paper_rel),
                (c.old_paper_path.name, c.new_paper_path.name),
                (c.old_pdf_rel, c.new_pdf_rel),
                (c.old_extract_rel, c.new_extract_rel),
                (f"[[{c.old_stem}]]", f"[[{c.new_stem}]]"),
                (f"[[{c.old_stem}|", f"[[{c.new_stem}|"),
                (f"[[{old_paper_rel}]]", f"[[{new_paper_rel}]]"),
                (f"[[{old_paper_rel}|", f"[[{new_paper_rel}|"),
                (f"[[{c.old_pdf_rel}]]", f"[[{c.new_pdf_rel}]]"),
                (f"[[{c.old_pdf_rel}|", f"[[{c.new_pdf_rel}|"),
            ):
                new_text, count = replace_with_count(new_text, old_value, new_value)
                file_changes += count

        if file_changes > 0:
            files_changed += 1
            replacements += file_changes
            changed_paths.append(md_file.relative_to(WORKSPACE_ROOT).as_posix())
            if apply:
                md_file.write_text(new_text, encoding="utf-8")

    return {
        "files_scanned": len(markdown_files),
        "files_changed": files_changed,
        "replacement_count": replacements,
        "changed_files": changed_paths,
    }


def validate_applied_changes(candidates: Iterable[Candidate], changed_files: Iterable[str]) -> List[str]:
    issues: List[str] = []
    changed_set = set(changed_files)

    for c in candidates:
        if not c.new_paper_path.exists():
            issues.append(f"missing_new_paper:{c.new_paper_path}")
        if not c.new_pdf_path.exists():
            issues.append(f"missing_new_pdf:{c.new_pdf_path}")
        if not c.new_extract_path.exists():
            issues.append(f"missing_new_extract:{c.new_extract_path}")

        if c.old_paper_path.exists():
            issues.append(f"old_paper_still_exists:{c.old_paper_path}")
        if c.old_pdf_path.exists():
            issues.append(f"old_pdf_still_exists:{c.old_pdf_path}")
        if c.old_extract_path.exists():
            issues.append(f"old_extract_still_exists:{c.old_extract_path}")

        paper_text = c.new_paper_path.read_text(encoding="utf-8", errors="ignore")
        split = split_frontmatter(paper_text)
        if split is None:
            issues.append(f"frontmatter_unparseable_after_apply:{c.new_paper_path.name}")
            continue

        frontmatter, _body = split
        local_pdf_value = extract_field(frontmatter, "local_pdf") or ""
        extract_value = extract_field(frontmatter, "pdf_extract") or ""
        if c.new_pdf_rel not in local_pdf_value:
            issues.append(f"paper_local_pdf_not_updated:{c.new_paper_path.name}")
        if c.new_extract_rel not in extract_value:
            issues.append(f"paper_pdf_extract_not_updated:{c.new_paper_path.name}")

    stale_patterns = []
    for c in candidates:
        stale_patterns.extend(
            [
                f"papers/{c.old_stem}.md",
                c.old_pdf_rel,
                c.old_extract_rel,
                f"[[{c.old_stem}]]",
                f"[[{c.old_stem}|",
            ]
        )

    for rel_path in sorted(changed_set):
        path = WORKSPACE_ROOT / rel_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in stale_patterns:
            if pattern in text:
                issues.append(f"stale_reference:{rel_path}:{pattern}")

    return issues


def make_record(
    paper: str,
    status: str,
    reason: str,
    candidate: Optional[Candidate] = None,
) -> Dict[str, str]:
    record: Dict[str, str] = {
        "paper": paper,
        "status": status,
        "reason": reason,
        "old_stem": "",
        "new_stem": "",
        "old_slug": "",
        "new_slug": "",
        "old_paper_rel": "",
        "new_paper_rel": "",
        "old_pdf_rel": "",
        "new_pdf_rel": "",
        "old_extract_rel": "",
        "new_extract_rel": "",
    }
    if candidate is not None:
        record.update(
            {
                "old_stem": candidate.old_stem,
                "new_stem": candidate.new_stem,
                "old_slug": candidate.old_slug,
                "new_slug": candidate.new_slug,
                "old_paper_rel": rel_paper_from_path(candidate.old_paper_path),
                "new_paper_rel": rel_paper_from_path(candidate.new_paper_path),
                "old_pdf_rel": candidate.old_pdf_rel,
                "new_pdf_rel": candidate.new_pdf_rel,
                "old_extract_rel": candidate.old_extract_rel,
                "new_extract_rel": candidate.new_extract_rel,
            }
        )
    return record


def write_csv(records: List[Dict[str, str]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "paper",
        "status",
        "reason",
        "old_stem",
        "new_stem",
        "old_slug",
        "new_slug",
        "old_paper_rel",
        "new_paper_rel",
        "old_pdf_rel",
        "new_pdf_rel",
        "old_extract_rel",
        "new_extract_rel",
    ]
    with out_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in records:
            writer.writerow(row)


def summarize_records(records: List[Dict[str, str]]) -> Dict[str, int]:
    summary = {
        "records_total": len(records),
        "candidate_rows": 0,
        "applied": 0,
        "skipped": 0,
        "errors": 0,
    }
    for row in records:
        status = row["status"]
        if status == "candidate":
            summary["candidate_rows"] += 1
        elif status == "applied":
            summary["applied"] += 1
        elif status == "skip":
            summary["skipped"] += 1
        elif status == "error":
            summary["errors"] += 1
    return summary


def default_report_paths(date_str: str) -> Tuple[Path, Path]:
    json_path = LOGS_DIR / f"{date_str}-author-asset-sync-report.json"
    csv_path = LOGS_DIR / f"{date_str}-author-asset-sync-candidates.csv"
    return json_path, csv_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sync updated author names in papers/Lit-WS-PDFs/PDF extracts.")
    parser.add_argument(
        "--input-log",
        type=Path,
        default=LOGS_DIR / "20260214-author-frontmatter-repair.json",
        help="Repair log JSON to scope changed papers.",
    )
    parser.add_argument("--apply", action="store_true", help="Apply changes. Default is dry-run.")
    parser.add_argument("--report-json", type=Path, default=None, help="Output JSON report path.")
    parser.add_argument("--report-csv", type=Path, default=None, help="Output CSV report path.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    dry_run = not args.apply
    now = dt.datetime.now()
    date_str = now.strftime("%Y%m%d")

    report_json, report_csv = default_report_paths(date_str)
    if args.report_json is not None:
        report_json = args.report_json
    if args.report_csv is not None:
        report_csv = args.report_csv

    if not args.input_log.exists():
        print(f"ERROR: input log not found: {args.input_log}")
        return 1

    for required in (PAPERS_DIR, PDFS_DIR, PDF_EXTRACTS_DIR, LOGS_DIR):
        if not required.exists():
            print(f"ERROR: required directory missing: {required}")
            return 1

    changed_papers = load_changed_papers(args.input_log)
    records: List[Dict[str, str]] = []
    candidates: List[Candidate] = []
    skip_reasons: Dict[str, int] = {}

    for paper_name in changed_papers:
        candidate, reason = build_candidate(paper_name)
        if candidate is None:
            records.append(make_record(paper_name, "skip", reason))
            skip_reasons[reason] = skip_reasons.get(reason, 0) + 1
            continue
        candidates.append(candidate)
        records.append(make_record(paper_name, "candidate", "rename_ready", candidate))

    discovered_candidates = len(candidates)
    apply_errors: List[str] = []
    applied_candidates: List[Candidate] = []

    if not dry_run:
        record_by_old_stem = {row["old_stem"]: row for row in records if row["old_stem"]}
        for candidate in candidates:
            try:
                apply_candidate(candidate)
                applied_candidates.append(candidate)
                row = record_by_old_stem.get(candidate.old_stem)
                if row is not None:
                    row["status"] = "applied"
                    row["reason"] = "renamed_and_updated"
            except Exception as exc:
                msg = f"{candidate.paper_filename}: {exc}"
                apply_errors.append(msg)
                row = record_by_old_stem.get(candidate.old_stem)
                if row is not None:
                    row["status"] = "error"
                    row["reason"] = str(exc)

    propagation = {
        "files_scanned": 0,
        "files_changed": 0,
        "replacement_count": 0,
        "changed_files": [],
    }
    validation_issues: List[str] = []
    if dry_run:
        propagation = propagate_references(candidates, apply=False)
    elif applied_candidates:
        propagation = propagate_references(applied_candidates, apply=True)
        validation_issues = validate_applied_changes(applied_candidates, propagation["changed_files"])

    summary = summarize_records(records)
    report = {
        "generated_at": now.isoformat(timespec="seconds"),
        "dry_run": dry_run,
        "input_log": str(args.input_log),
        "scope_changed_papers": len(changed_papers),
        "discovered_candidates": discovered_candidates,
        "summary": summary,
        "skip_reasons": skip_reasons,
        "apply_errors": apply_errors,
        "validation_issues": validation_issues,
        "propagation": propagation,
        "records": records,
    }

    report_json.parent.mkdir(parents=True, exist_ok=True)
    report_json.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_csv(records, report_csv)

    print("=" * 80)
    print(f"Author Asset Sync {'(DRY RUN)' if dry_run else '(APPLY)'}")
    print("=" * 80)
    print(f"Scope changed papers: {len(changed_papers)}")
    print(f"Discovered candidates: {discovered_candidates}")
    print(f"Candidate rows remaining: {summary['candidate_rows']}")
    print(f"Applied: {summary['applied']}")
    print(f"Skipped: {summary['skipped']}")
    print(f"Errors: {summary['errors']}")
    print(
        "Propagation: "
        f"{propagation['files_changed']} files changed, "
        f"{propagation['replacement_count']} replacements"
    )
    print(f"Report JSON: {report_json}")
    print(f"Report CSV:  {report_csv}")

    if apply_errors:
        print("\nApply errors:")
        for item in apply_errors:
            print(f"  - {item}")

    if validation_issues:
        print("\nValidation issues:")
        for item in validation_issues:
            print(f"  - {item}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
