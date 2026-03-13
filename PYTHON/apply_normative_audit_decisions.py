#!/usr/bin/env python3
"""
Apply normative ethics audit decisions from exported JSON.

Reads a decisions JSON file (exported from the tier review HTML pages)
and applies YAML field changes to paper files using safe regex replacement.

Safety protocol:
  1. For each decision: read paper → apply via re.subn() (no parse→rebuild)
  2. Update Human View fields with audit metadata
  3. Run validate_all_papers.py after all changes
  4. Output detailed log

Usage:
    python apply_normative_audit_decisions.py <decisions.json>
    python apply_normative_audit_decisions.py <decisions.json> --dry-run

Input JSON format:
{
    "audit_tier": "tier1",
    "audit_date": "2026-03-12",
    "decisions": [
        {
            "filename": "2012-Gippert-The Encoding of Avestan.md",
            "changes": { "virtue_ethics": "No" },
            "note": "Avestan script encoding, not ethics"
        }
    ]
}
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))

from config import PAPERS_DIR, LOGS_DIR

# Fields that this script is allowed to modify
ALLOWED_FIELDS = {
    "ethics_overall", "virtue_ethics", "deontological_ethics", "utilitarian_ethics",
}
ALLOWED_VALUES = {"Yes", "No"}


def safe_yaml_replace(frontmatter_text, field, new_value):
    """
    Replace a YAML field value using safe regex (no parse→rebuild).
    Returns (new_frontmatter, was_replaced).

    Per CLAUDE.md rule #2: re.subn() with count=1, re.MULTILINE.
    """
    pattern = rf'^{re.escape(field)}:.*$'
    replacement = f'{field}: "{new_value}"'
    new_fm, count = re.subn(pattern, replacement, frontmatter_text, count=1, flags=re.MULTILINE)
    return new_fm, count > 0


def update_human_view(frontmatter_text, tier, note):
    """Update Human View fields with audit metadata."""
    audit_date = "2026-03-12"
    view_note = f"{tier}: {note}" if note else tier

    # Truncate note to avoid YAML line-length issues
    if len(view_note) > 120:
        view_note = view_note[:117] + "..."

    fm = frontmatter_text

    # Update Human View to "Yes" (or true for consistency with existing data)
    fm, _ = re.subn(r'^Human View:.*$', 'Human View: true', fm, count=1, flags=re.MULTILINE)
    fm, _ = re.subn(r'^Human View Date:.*$', f'Human View Date: {audit_date}', fm, count=1, flags=re.MULTILINE)

    # Escape quotes in note for YAML safety
    safe_note = view_note.replace('"', "'")
    fm, count = re.subn(r'^Human View note:.*$', f'Human View note: "{safe_note}"', fm, count=1, flags=re.MULTILINE)

    # If Human View note field doesn't exist, add it after Human View Date
    if count == 0:
        fm, _ = re.subn(
            r'^(Human View Date:.*)$',
            rf'\1\nHuman View note: "{safe_note}"',
            fm, count=1, flags=re.MULTILINE
        )

    return fm


def apply_decisions(decisions_path, dry_run=False):
    """Apply all decisions from the JSON file."""
    with open(decisions_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    tier = data.get("audit_tier", "unknown")
    audit_date = data.get("audit_date", "2026-03-12")
    decisions_list = data.get("decisions", [])

    print(f"Audit tier: {tier}")
    print(f"Audit date: {audit_date}")
    print(f"Decisions to apply: {len(decisions_list)}")
    if dry_run:
        print("** DRY RUN — no files will be modified **\n")
    print()

    log = {
        "tier": tier,
        "audit_date": audit_date,
        "applied_at": datetime.now().isoformat(),
        "dry_run": dry_run,
        "total_decisions": len(decisions_list),
        "applied": [],
        "skipped": [],
        "errors": [],
        "field_changes": {
            "ethics_overall": {"Yes_to_No": 0, "No_to_Yes": 0},
            "virtue_ethics": {"Yes_to_No": 0, "No_to_Yes": 0},
            "deontological_ethics": {"Yes_to_No": 0, "No_to_Yes": 0},
            "utilitarian_ethics": {"Yes_to_No": 0, "No_to_Yes": 0},
        },
    }

    for dec in decisions_list:
        filename = dec.get("filename", "")
        changes = dec.get("changes", {})
        note = dec.get("note", "")

        paper_path = PAPERS_DIR / filename
        if not paper_path.exists():
            print(f"  ERROR: File not found: {filename}")
            log["errors"].append({"filename": filename, "error": "File not found"})
            continue

        # Validate changes
        invalid_fields = [f for f in changes if f not in ALLOWED_FIELDS]
        if invalid_fields:
            print(f"  ERROR: Invalid fields {invalid_fields} in {filename}")
            log["errors"].append({"filename": filename, "error": f"Invalid fields: {invalid_fields}"})
            continue

        invalid_values = [(f, v) for f, v in changes.items() if v not in ALLOWED_VALUES]
        if invalid_values:
            print(f"  ERROR: Invalid values {invalid_values} in {filename}")
            log["errors"].append({"filename": filename, "error": f"Invalid values: {invalid_values}"})
            continue

        # Read file
        try:
            content = paper_path.read_text(encoding="utf-8")
        except Exception as e:
            log["errors"].append({"filename": filename, "error": str(e)})
            continue

        # Split frontmatter
        if not content.startswith("---"):
            log["errors"].append({"filename": filename, "error": "No frontmatter delimiter"})
            continue

        end_idx = content.find("---", 3)
        if end_idx == -1:
            log["errors"].append({"filename": filename, "error": "No closing frontmatter delimiter"})
            continue

        fm = content[3:end_idx]
        rest = content[end_idx:]

        # Track what actually changed
        actual_changes = {}
        for field, new_val in changes.items():
            # Check current value
            match = re.search(rf'^{re.escape(field)}:\s*"?(\w+)"?', fm, re.MULTILINE)
            old_val = match.group(1) if match else "(missing)"

            if old_val == new_val:
                continue  # No change needed

            fm_new, was_replaced = safe_yaml_replace(fm, field, new_val)
            if was_replaced:
                fm = fm_new
                actual_changes[field] = {"from": old_val, "to": new_val}
                direction = f"{old_val}_to_{new_val}"
                if direction in log["field_changes"].get(field, {}):
                    log["field_changes"][field][direction] += 1

        if not actual_changes:
            log["skipped"].append({"filename": filename, "reason": "No actual changes needed"})
            continue

        # Update Human View
        change_desc = "; ".join(f"{f}: {c['from']}→{c['to']}" for f, c in actual_changes.items())
        full_note = f"{change_desc}" + (f" | {note}" if note else "")
        fm = update_human_view(fm, tier, full_note)

        # Reconstruct file
        new_content = "---" + fm + rest

        if not dry_run:
            paper_path.write_text(new_content, encoding="utf-8")

        action_str = "WOULD APPLY" if dry_run else "APPLIED"
        print(f"  {action_str}: {filename}")
        for f, c in actual_changes.items():
            print(f"    {f}: {c['from']} → {c['to']}")

        log["applied"].append({
            "filename": filename,
            "changes": actual_changes,
            "note": note,
        })

    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"  Applied: {len(log['applied'])}")
    print(f"  Skipped (no change): {len(log['skipped'])}")
    print(f"  Errors: {len(log['errors'])}")

    for field, counts in log["field_changes"].items():
        y2n = counts.get("Yes_to_No", 0)
        n2y = counts.get("No_to_Yes", 0)
        if y2n or n2y:
            print(f"  {field}: {y2n} Yes→No, {n2y} No→Yes")

    # Write log
    LOGS_DIR.mkdir(exist_ok=True)
    suffix = "-dryrun" if dry_run else ""
    log_path = LOGS_DIR / f"20260312-normative-audit-{tier}-applied{suffix}.json"
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(log, f, indent=2, ensure_ascii=False)
    print(f"\nLog: {log_path}")

    # Run validation (unless dry run)
    if not dry_run and log["applied"]:
        print("\nRunning validate_all_papers.py...")
        venv_python = Path(__file__).parent.parent.parent / ".venv" / "bin" / "python"
        validate_script = Path(__file__).parent / "validate_all_papers.py"
        try:
            result = subprocess.run(
                [str(venv_python), str(validate_script)],
                capture_output=True, text=True, timeout=120,
                cwd=str(Path(__file__).parent.parent),
            )
            if result.returncode == 0:
                print("  Validation passed")
            else:
                print(f"  Validation issues:\n{result.stdout[-500:]}")
                if result.stderr:
                    print(f"  Stderr: {result.stderr[-300:]}")
        except Exception as e:
            print(f"  Validation error: {e}")

    return log


def main():
    parser = argparse.ArgumentParser(description="Apply normative ethics audit decisions")
    parser.add_argument("decisions_json", type=Path, help="Path to decisions JSON file")
    parser.add_argument("--dry-run", action="store_true", help="Show what would change without modifying files")
    args = parser.parse_args()

    if not args.decisions_json.exists():
        print(f"Error: {args.decisions_json} not found")
        sys.exit(1)

    apply_decisions(args.decisions_json, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
