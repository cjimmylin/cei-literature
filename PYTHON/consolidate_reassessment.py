#!/usr/bin/env python3
"""
Phase B.4: Consolidate reassessment agent results and apply to papers.

Reads agent output JSON files, validates entries, and applies corrections to:
  - LLM_assessed (model names)
  - DATA_URL (data/benchmark URL)
  - data_description (1-2 sentence summary)
  - is_benchmark (Yes/No)
  - is_eval (Yes/No)
  - is_dataset (Yes/No)

Merge policy:
  - High-confidence agent values overwrite current values
  - Low-confidence values are flagged for review (not applied)
  - Prefer non-NA over NA (never downgrade a filled field to NA unless high-confidence)
  - Uses safe YAML regex pattern (never parse/rebuild round-trip)

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/consolidate_reassessment.py --dry-run
    ../.venv/bin/python PYTHON/consolidate_reassessment.py
    ../.venv/bin/python PYTHON/consolidate_reassessment.py --manifest logs/20260312-reassessment_manifest.json

Output:
    logs/YYYYMMDD-reassessment-consolidation.json
    logs/YYYYMMDD-reassessment-diff-report.md
"""

from __future__ import annotations

import argparse
import functools
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

print = functools.partial(print, flush=True)

sys.path.insert(0, str(Path(__file__).parent.parent / ".agent"))
from lib.config import LOGS_DIR, PAPERS_DIR  # noqa: E402
from lib.yaml_utils import extract_frontmatter, parse_frontmatter, validate_frontmatter  # noqa: E402

DATE_PREFIX = datetime.now().strftime("%Y%m%d")

# Fields managed by this consolidation script
MANAGED_FIELDS = ["LLM_assessed", "DATA_URL", "is_benchmark", "is_eval", "is_dataset"]
# YAML anchor fields for insertion ordering
FIELD_ANCHORS = {
    "LLM_assessed": ["data_metrics", "is_dataset", "is_eval", "is_benchmark"],
    "DATA_URL": ["LLM_assessed", "data_metrics", "is_dataset"],
    "is_benchmark": ["is_eval", "is_dataset", "data_metrics", "DATA_URL"],
    "is_eval": ["is_benchmark", "is_dataset", "data_metrics", "DATA_URL"],
    "is_dataset": ["is_eval", "is_benchmark", "data_metrics", "DATA_URL"],
}

NA_VALUES = {"", "NA", "N/A", "NONE", "NULL"}


def clean_scalar(value: str | None) -> str:
    """Strip quotes and whitespace from a YAML scalar value."""
    s = (value or "").strip()
    if len(s) >= 2 and ((s.startswith('"') and s.endswith('"')) or
                         (s.startswith("'") and s.endswith("'"))):
        s = s[1:-1].strip()
    return s


def is_na(value: str) -> bool:
    """Check if a value is NA/empty."""
    return value.strip().upper() in NA_VALUES


def yaml_scalar_line(key: str, value: str) -> str:
    """Format a YAML key: value line."""
    if value == "NA" or value in ("Yes", "No"):
        return f"{key}: {value}"
    safe = value.replace('"', "'")
    return f'{key}: "{safe}"'


def set_yaml_scalar(frontmatter: str, key: str, value: str) -> tuple[str, str]:
    """
    Safe regex-based replacement/insertion of a YAML scalar field.

    Returns: (new_frontmatter, operation)
    """
    line = yaml_scalar_line(key, value)
    pattern = r"^{}:.*$".format(re.escape(key))
    replaced, count = re.subn(pattern, line, frontmatter, count=1, flags=re.MULTILINE)
    if count > 0:
        return replaced, "replaced"

    # Field doesn't exist — insert after anchor
    anchors = FIELD_ANCHORS.get(key, [])
    for anchor in anchors:
        m = re.search(r"^{}:.*$".format(re.escape(anchor)), frontmatter, flags=re.MULTILINE)
        if m:
            insert_pos = m.end()
            inserted = frontmatter[:insert_pos] + "\n" + line + frontmatter[insert_pos:]
            return inserted, f"inserted_after_{anchor}"

    # Last resort: append
    appended = frontmatter.rstrip() + "\n" + line
    return appended, "appended"


def load_manifest(manifest_path: str | None = None) -> tuple[dict, Path]:
    """Load manifest to find agent result files."""
    if manifest_path:
        mpath = Path(manifest_path)
    else:
        manifests = sorted(LOGS_DIR.glob("*-reassessment_manifest.json"), reverse=True)
        if not manifests:
            print("ERROR: No reassessment manifest found. Run generate_reassessment_batches.py first.")
            sys.exit(1)
        mpath = manifests[0]

    print(f"Loading manifest: {mpath.name}")
    with open(mpath, "r", encoding="utf-8") as f:
        return json.load(f), mpath


def load_agent_results(manifest: dict) -> list[dict]:
    """Load all agent result JSON files."""
    all_results = []
    date = manifest["date"]
    num_batches = manifest["num_batches"]

    for i in range(1, num_batches + 1):
        result_name = f"{date}-reassessment_agent_{i:02d}.json"
        result_path = LOGS_DIR / result_name
        if not result_path.exists():
            print(f"  WARN: Missing agent result file: {result_name} (skipping)")
            continue

        with open(result_path, "r", encoding="utf-8") as f:
            results = json.load(f)

        # Handle both list and dict formats
        if isinstance(results, dict):
            results = results.get("results", results.get("papers", [results]))

        for entry in results:
            if "filename" not in entry:
                print(f"  WARN: Agent {i:02d} has entry without 'filename', skipping")
                continue
            entry["_source_agent"] = i

        all_results.extend(results)
        print(f"  Agent {i:02d}: {len(results)} papers loaded")

    return all_results


def should_apply(field: str, current_val: str, agent_val: str, confidence: str) -> tuple[bool, str]:
    """
    Determine whether an agent's value should overwrite the current value.

    Returns: (should_apply, reason)
    """
    current_is_na = is_na(current_val)
    agent_is_na = is_na(agent_val)

    # Never downgrade from filled to NA unless high confidence
    if not current_is_na and agent_is_na:
        if confidence == "high":
            return True, "high_confidence_clear"
        return False, "kept_existing_over_na"

    # Always upgrade from NA to non-NA
    if current_is_na and not agent_is_na:
        return True, "filled_from_na"

    # Both filled — only overwrite on high confidence
    if not current_is_na and not agent_is_na:
        if current_val.strip() == agent_val.strip():
            return False, "unchanged"
        if confidence in ("high", "medium"):
            return True, f"{confidence}_confidence_update"
        return False, "low_confidence_kept_existing"

    # Both NA — no change
    return False, "both_na"


def apply_to_paper(
    paper_path: Path,
    entry: dict,
    dry_run: bool = False,
) -> dict:
    """Apply reassessed values to a single paper."""
    try:
        content = paper_path.read_text(encoding="utf-8")
        fm_text, body = extract_frontmatter(content)
    except (ValueError, UnicodeDecodeError) as e:
        return {"status": "error", "error": str(e)}

    fields = parse_frontmatter(fm_text)
    confidence = entry.get("confidence", "medium")
    new_fm = fm_text
    field_ops: dict[str, dict] = {}
    any_changed = False

    for field in MANAGED_FIELDS:
        current_val = clean_scalar(fields.get(field))
        if not current_val:
            current_val = "NA"
        agent_val = entry.get(field, "").strip()
        if not agent_val:
            agent_val = "NA"

        apply, reason = should_apply(field, current_val, agent_val, confidence)

        field_ops[field] = {
            "current": current_val,
            "agent": agent_val,
            "applied": apply,
            "reason": reason,
        }

        if apply:
            new_fm, op = set_yaml_scalar(new_fm, field, agent_val)
            field_ops[field]["yaml_op"] = op
            any_changed = True

    # Handle data_description in body (not YAML field)
    desc = entry.get("data_description", "").strip()
    desc_op = "no_change"
    new_body = body
    if desc and desc.upper() != "NA":
        if "## Data Description" in body:
            # Replace existing content
            new_body = re.sub(
                r"(## Data Description\s*\n\n)(.*?)(\n\n## |\n\n---|\Z)",
                lambda m: m.group(1) + desc + "\n" + m.group(3),
                body,
                count=1,
                flags=re.DOTALL,
            )
            if new_body != body:
                desc_op = "updated_existing"
                any_changed = True
        else:
            # Insert new section
            section = f"\n## Data Description\n\n{desc}\n"
            for heading in ("## Notes", "## Citation Info"):
                m = re.search(r"(?m)^{}\s*$".format(re.escape(heading)), body)
                if m:
                    new_body = body[:m.start()] + section + "\n" + body[m.start():]
                    desc_op = f"inserted_before_{heading.replace('## ', '')}"
                    any_changed = True
                    break
            else:
                suffix = "\n" if body.endswith("\n") else "\n\n"
                new_body = body + suffix + section + "\n"
                desc_op = "appended"
                any_changed = True

    if not any_changed:
        return {
            "status": "unchanged",
            "field_ops": field_ops,
            "desc_op": desc_op,
        }

    # Validate YAML before writing
    is_valid, issues = validate_frontmatter(new_fm)
    if not is_valid:
        return {
            "status": "error",
            "error": f"YAML validation failed: {'; '.join(issues)}",
            "field_ops": field_ops,
        }

    if dry_run:
        return {
            "status": "dry_run",
            "would_update": True,
            "field_ops": field_ops,
            "desc_op": desc_op,
        }

    # Write back
    new_content = f"---\n{new_fm.rstrip()}\n---\n{new_body}"
    paper_path.write_text(new_content, encoding="utf-8")

    return {
        "status": "updated",
        "field_ops": field_ops,
        "desc_op": desc_op,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Consolidate reassessment results")
    parser.add_argument("--manifest", type=str, default="",
                        help="Path to manifest JSON (default: most recent)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview mode: validate without writing")
    args = parser.parse_args()

    print("=" * 60)
    print("Phase B.4: Reassessment Consolidation")
    print("=" * 60)
    print(f"Mode: {'dry-run' if args.dry_run else 'write'}")
    print()

    # Load manifest
    manifest, manifest_path = load_manifest(args.manifest or None)
    print(f"Date: {manifest['date']}, Batches: {manifest['num_batches']}, "
          f"Papers: {manifest['total_papers']}")

    # Load results
    print("\nLoading agent results:")
    all_results = load_agent_results(manifest)
    print(f"\nTotal entries loaded: {len(all_results)}")

    if not all_results:
        print("No results to process. Exiting.")
        return

    # Check for duplicates — keep highest confidence
    by_filename: dict[str, list[dict]] = {}
    for entry in all_results:
        fn = entry["filename"]
        by_filename.setdefault(fn, []).append(entry)

    deduped_results = []
    confidence_rank = {"high": 3, "medium": 2, "low": 1}
    for fn, entries in by_filename.items():
        if len(entries) == 1:
            deduped_results.append(entries[0])
        else:
            # Pick highest confidence
            best = max(entries, key=lambda e: confidence_rank.get(e.get("confidence", "low"), 0))
            deduped_results.append(best)
            print(f"  DEDUP: {fn} ({len(entries)} entries, kept {best.get('confidence', 'unknown')})")

    deduped_results.sort(key=lambda r: r["filename"])
    print(f"Unique papers: {len(deduped_results)}")

    # ── Content summary ───────────────────────────────────────────────────
    confidence_dist = Counter()
    for r in deduped_results:
        confidence_dist[r.get("confidence", "unknown")] += 1

    print("\nConfidence distribution:")
    for conf, count in confidence_dist.most_common():
        print(f"  {conf}: {count}")

    # ── Apply to papers ───────────────────────────────────────────────────
    print(f"\n{'=' * 60}")
    print(f"APPLYING TO PAPERS{' (DRY RUN)' if args.dry_run else ''}")
    print("=" * 60)

    log_entries: list[dict] = []
    status_counts = Counter()
    field_change_counts: dict[str, Counter] = {f: Counter() for f in MANAGED_FIELDS}
    diff_entries: list[dict] = []

    def resolve_paper_path(filename: str):
        """Try exact match first, then try curly-quote variants for agent ASCII output."""
        p = PAPERS_DIR / filename
        if p.exists():
            return p
        # Agent JSON may output ASCII quotes while disk filenames have Unicode curly quotes
        # Try replacing ASCII apostrophe/quote with Unicode variants
        curly = (
            filename
            .replace("'", "\u2019")   # ' → '  (most common: possessives)
        )
        if curly != filename:
            p2 = PAPERS_DIR / curly
            if p2.exists():
                return p2
        # Try open/close curly quote pairing for quoted phrases like 'benchmarking'
        import re
        def add_curly_quotes(s):
            # Replace pairs of 'x' with 'x' (open/close)
            result = re.sub(r"'([^']+)'", "\u2018\\1\u2019", s)
            return result
        curly2 = add_curly_quotes(filename)
        if curly2 != filename:
            p2 = PAPERS_DIR / curly2
            if p2.exists():
                return p2
        return p  # return original (not found) to trigger MISSING

    for entry in deduped_results:
        paper_path = resolve_paper_path(entry["filename"])
        if not paper_path.exists():
            print(f"  MISSING: {entry['filename']}")
            log_entries.append({"filename": entry["filename"], "status": "missing"})
            status_counts["missing"] += 1
            continue

        result = apply_to_paper(paper_path, entry, dry_run=args.dry_run)
        status = result["status"]
        status_counts[status] += 1

        log_entry = {
            "filename": entry["filename"],
            "status": status,
            "confidence": entry.get("confidence", "unknown"),
            "notes": entry.get("notes", ""),
        }
        if "field_ops" in result:
            log_entry["field_ops"] = result["field_ops"]
        if "desc_op" in result:
            log_entry["desc_op"] = result["desc_op"]
        if "error" in result:
            log_entry["error"] = result["error"]
            print(f"  ERROR: {entry['filename']} — {result['error']}")

        log_entries.append(log_entry)

        # Track field-level changes for the diff report
        if "field_ops" in result:
            for field, ops in result["field_ops"].items():
                field_change_counts[field][ops["reason"]] += 1
                if ops.get("applied"):
                    diff_entries.append({
                        "paper": entry["filename"],
                        "field": field,
                        "before": ops["current"],
                        "after": ops["agent"],
                        "confidence": entry.get("confidence", "unknown"),
                    })

    # ── Print results ─────────────────────────────────────────────────────
    print(f"\n{'=' * 60}")
    print("RESULTS")
    print("=" * 60)
    for status, count in sorted(status_counts.items()):
        print(f"  {status}: {count}")

    print("\nField-level change reasons:")
    for field in MANAGED_FIELDS:
        reasons = field_change_counts[field]
        if reasons:
            print(f"\n  {field}:")
            for reason, count in reasons.most_common():
                print(f"    {reason}: {count}")

    # ── Write consolidation log ───────────────────────────────────────────
    consolidation = {
        "date": DATE_PREFIX,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "manifest": manifest_path.name,
        "mode": "dry-run" if args.dry_run else "write",
        "total_processed": len(deduped_results),
        "status_counts": dict(status_counts),
        "confidence_distribution": dict(confidence_dist),
        "field_change_reasons": {f: dict(c) for f, c in field_change_counts.items()},
        "total_field_changes": len(diff_entries),
        "entries": log_entries,
    }

    consolidation_path = LOGS_DIR / f"{DATE_PREFIX}-reassessment-consolidation.json"
    tmp_path = consolidation_path.parent / f".tmp.{os.getpid()}.consolidation.json"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(consolidation, f, indent=2, ensure_ascii=False)
    os.replace(str(tmp_path), str(consolidation_path))
    print(f"\nConsolidation log: {consolidation_path.name}")

    # ── Write diff report ─────────────────────────────────────────────────
    diff_path = LOGS_DIR / f"{DATE_PREFIX}-reassessment-diff-report.md"
    diff_lines = [
        "# Reassessment Diff Report",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        f"Mode: `{'dry-run' if args.dry_run else 'write'}`",
        "",
        "## Summary",
        "",
        f"- Papers processed: **{len(deduped_results)}**",
        f"- Papers updated: **{status_counts.get('updated', 0) + status_counts.get('dry_run', 0)}**",
        f"- Papers unchanged: **{status_counts.get('unchanged', 0)}**",
        f"- Errors: **{status_counts.get('error', 0)}**",
        f"- Missing: **{status_counts.get('missing', 0)}**",
        f"- Total field-level changes: **{len(diff_entries)}**",
        "",
        "## Confidence Distribution",
        "",
        "| Confidence | Papers |",
        "|------------|-------:|",
    ]
    for conf, count in confidence_dist.most_common():
        diff_lines.append(f"| {conf} | {count} |")

    diff_lines.extend([
        "",
        "## Field Change Summary",
        "",
        "| Field | Changes |",
        "|-------|--------:|",
    ])
    for field in MANAGED_FIELDS:
        n_changes = sum(1 for d in diff_entries if d["field"] == field)
        diff_lines.append(f"| {field} | {n_changes} |")

    if diff_entries:
        diff_lines.extend([
            "",
            "## All Changes",
            "",
            "| Paper | Field | Before | After | Confidence |",
            "|-------|-------|--------|-------|:----------:|",
        ])
        for d in diff_entries[:500]:
            before = d["before"] if len(d["before"]) <= 40 else d["before"][:37] + "..."
            after = d["after"] if len(d["after"]) <= 40 else d["after"][:37] + "..."
            diff_lines.append(
                f"| `{d['paper']}` | {d['field']} | {before} | {after} | {d['confidence']} |"
            )
        if len(diff_entries) > 500:
            diff_lines.append(f"\n*... {len(diff_entries) - 500} more changes not shown*")

    diff_lines.append("")
    diff_path.write_text("\n".join(diff_lines), encoding="utf-8")
    print(f"Diff report: {diff_path.name}")

    print(f"\n{'=' * 60}")
    print("DONE")
    print("=" * 60)


if __name__ == "__main__":
    main()
