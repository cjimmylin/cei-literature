#!/usr/bin/env python3
"""
Triage Cat A Abbreviated Author Names

Reads the audit report and classifies each Cat A entry into actionable
sub-groups for efficient resolution:

  Group 1  — No action (full name + middle initial, e.g., "Noah A. Smith")
  Group 2a — Format fix only (reversed, complete, e.g., "Holyoak, Keith J.")
  Group 2b — Expand + format fix (reversed, abbreviated, e.g., "Sanguinetti, M.")
  Group 3  — API expansion (initials-only given name, e.g., "W. Wang")
  Group 4  — Manual review (edge cases)

USAGE:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/triage_cat_a_authors.py
"""

import functools
import json
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import builtins
print = functools.partial(builtins.print, flush=True)

sys.path.insert(0, str(Path(__file__).parent))
from vault_config import LOGS_DIR

DATE_PREFIX = datetime.now().strftime("%Y%m%d")
OUTPUT_FILE = LOGS_DIR / f"{DATE_PREFIX}-cat_a_triage.json"

INITIAL = re.compile(r'^[A-Z]\.$')


def classify_entry(entry: dict) -> tuple:
    """Classify a Cat A entry into a group.

    Returns: (group, fix_info) where group is one of:
      "1_no_action", "2a_format_fix", "2b_expand_and_format",
      "3_expand", "4_manual"
    """
    name = entry["author_name"]
    parts = name.split()

    # --- Reversed names (contain comma) ---
    if ',' in name:
        comma_parts = [p.strip() for p in name.split(',', 1)]
        if len(comma_parts) != 2 or not comma_parts[1].strip():
            return "4_manual", {"reason": "malformed reversed name"}

        surname = comma_parts[0].strip()
        given = comma_parts[1].strip()
        given_parts = given.split()

        # Are ALL given name parts initials?
        all_initials = all(INITIAL.match(p) for p in given_parts)

        if all_initials:
            # Reversed AND abbreviated — needs API expansion + format fix
            unreversed = f"{given} {surname}"
            return "2b_expand_and_format", {
                "reversed_name": name,
                "unreversed_name": unreversed,
                "surname": surname,
                "given": given,
            }
        else:
            # Reversed but has full given name — just un-reverse
            unreversed = f"{given} {surname}"
            return "2a_format_fix", {
                "reversed_name": name,
                "unreversed_name": unreversed,
                "surname": surname,
                "given": given,
            }

    # --- Non-reversed names ---
    initial_parts = [p for p in parts if INITIAL.match(p)]
    full_parts = [p for p in parts if not INITIAL.match(p)]

    if len(full_parts) >= 2:
        # Has at least 2 non-initial parts (e.g., "Noah A. Smith")
        # This is a complete name with middle initial — no action needed
        return "1_no_action", {"reason": "full name with middle initial"}

    if len(full_parts) == 1 and len(initial_parts) >= 1:
        # Only one full part + initials (e.g., "W. Wang", "A. B. Smith")
        return "3_expand", {
            "initials": [p for p in parts if INITIAL.match(p)],
            "full_parts": full_parts,
        }

    # Edge case: all initials, no full parts, or unexpected structure
    return "4_manual", {"reason": "unexpected name structure"}


def main():
    # Find the most recent audit report
    candidates = sorted(LOGS_DIR.glob("*-author_audit_report.json"), reverse=True)
    if not candidates:
        print("ERROR: No audit report found. Run audit_author_entries.py first.")
        sys.exit(1)

    report_path = candidates[0]
    print(f"Loading audit report: {report_path.name}")

    with open(report_path, 'r', encoding='utf-8') as f:
        report = json.load(f)

    cat_a = report["categories"]["A"]
    print(f"Total Cat A entries: {len(cat_a)}")

    # Classify each entry
    groups = defaultdict(list)
    for entry in cat_a:
        group, fix_info = classify_entry(entry)
        entry_out = {
            "author_name": entry["author_name"],
            "paper": entry["paper"],
            "filename": entry["filename"],
            "url": entry.get("url", ""),
            "doi": entry.get("doi", ""),
            "group": group,
            "fix_info": fix_info,
        }
        groups[group].append(entry_out)

    # Deduplicate: for Groups 2a/2b, count unique reversed names
    unique_2a = set(e["author_name"] for e in groups["2a_format_fix"])
    unique_2b = set(e["author_name"] for e in groups["2b_expand_and_format"])
    unique_3 = set(e["author_name"] for e in groups["3_expand"])

    # Print summary
    print(f"\n=== TRIAGE RESULTS ===")
    print(f"  Group 1  (no action, full+initial):     {len(groups['1_no_action']):>4} entries")
    print(f"  Group 2a (format fix, reversed-complete):{len(groups['2a_format_fix']):>4} entries ({len(unique_2a)} unique names)")
    print(f"  Group 2b (expand+format, reversed-abbr): {len(groups['2b_expand_and_format']):>3} entries ({len(unique_2b)} unique names)")
    print(f"  Group 3  (expand, initials-only):        {len(groups['3_expand']):>3} entries ({len(unique_3)} unique names)")
    print(f"  Group 4  (manual review):                {len(groups['4_manual']):>3} entries")

    # Build output
    output = {
        "metadata": {
            "date": datetime.now().isoformat(),
            "source_report": report_path.name,
            "total_entries": len(cat_a),
        },
        "summary": {
            "1_no_action": len(groups["1_no_action"]),
            "2a_format_fix": len(groups["2a_format_fix"]),
            "2a_unique_names": len(unique_2a),
            "2b_expand_and_format": len(groups["2b_expand_and_format"]),
            "2b_unique_names": len(unique_2b),
            "3_expand": len(groups["3_expand"]),
            "3_unique_names": len(unique_3),
            "4_manual": len(groups["4_manual"]),
        },
        "groups": dict(groups),
    }

    # Print samples for each actionable group
    print(f"\n--- Group 2a samples (format fix) ---")
    seen = set()
    for e in groups["2a_format_fix"]:
        if e["author_name"] not in seen:
            seen.add(e["author_name"])
            print(f"  {e['author_name']!r} → {e['fix_info']['unreversed_name']!r}")
            if len(seen) >= 5:
                break

    print(f"\n--- Group 2b samples (need API expansion) ---")
    seen = set()
    for e in groups["2b_expand_and_format"]:
        if e["author_name"] not in seen:
            seen.add(e["author_name"])
            print(f"  {e['author_name']!r} → needs expansion (unreversed: {e['fix_info']['unreversed_name']!r})")
            if len(seen) >= 5:
                break

    print(f"\n--- Group 3 samples (need API expansion) ---")
    seen = set()
    for e in groups["3_expand"]:
        if e["author_name"] not in seen:
            seen.add(e["author_name"])
            print(f"  {e['author_name']!r}")
            if len(seen) >= 5:
                break

    # Save
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nTriage saved: {OUTPUT_FILE.name}")


if __name__ == "__main__":
    main()
