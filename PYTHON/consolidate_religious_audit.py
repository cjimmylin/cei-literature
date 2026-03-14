#!/usr/bin/env python3
"""
Consolidate religious tradition deep-read results from 10 agents.

Reads results_agent_01.json through results_agent_10.json from the
religious_audit_batches directory, validates completeness, and applies
reclassification decisions to paper YAML frontmatter using safe regex.

Output:
  - logs/20260215-religious_audit_all_classifications.json  (all entries)
  - logs/20260215-religious_audit_decisions.json            (Reclassify only)
  - Updates religious_values + religious_values_list YAML fields in papers/

YAML SAFETY: Uses safe regex replacement, never parse→rebuild round-trip.
"""

import json
import re
import sys
import functools
from pathlib import Path
from collections import Counter

print = functools.partial(print, flush=True)

sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))
sys.path.insert(0, str(Path(__file__).parent))
from config import LOGS_DIR, PAPERS_DIR
from yaml_utils import extract_frontmatter, validate_frontmatter
from religious_scoring import (
    RV_FIELDS, FIELD_DISPLAY_NAMES, DISPLAY_NAME_TO_FIELD, TRADITION_ALIASES,
    parse_rv_value, is_rv_detected, DEFAULT_THRESHOLD,
    derive_religious_values_string, derive_religious_values_list_string,
)
from ethics_scoring import safe_yaml_set_int

BATCHES_DIR = LOGS_DIR / "religious_audit_batches"
REQUIRED_FIELDS = {"filename", "decision", "religious_tradition", "confidence",
                   "evidence", "reasoning"}
VALID_DECISIONS = {"Reclassify", "Keep N/A", "Uncertain"}


def load_batch_filenames():
    """Load all filenames from the batch files for validation."""
    all_filenames = []
    batch_files = sorted(BATCHES_DIR.glob("batch_*.json"))
    for bf in batch_files:
        with open(bf, "r", encoding="utf-8") as f:
            batch = json.load(f)
        all_filenames.extend(entry["filename"] for entry in batch)
    return all_filenames


def load_agent_results():
    """Load and validate all agent result files."""
    all_results = []
    per_agent = {}

    result_files = sorted(BATCHES_DIR.glob("results_agent_*.json"))
    if not result_files:
        print("ERROR: No result files found in {}".format(BATCHES_DIR))
        sys.exit(1)

    for result_path in result_files:
        agent_num = result_path.stem.replace("results_agent_", "")

        with open(result_path, "r", encoding="utf-8") as f:
            results = json.load(f)

        # Validate fields
        for entry in results:
            missing = REQUIRED_FIELDS - set(entry.keys())
            if missing:
                print("WARN: Agent {}, paper '{}': missing fields {} — skipping".format(
                    agent_num, entry.get("filename", "?"), missing))
                continue

            if entry["decision"] not in VALID_DECISIONS:
                print("WARN: Agent {}, paper '{}': invalid decision '{}' — treating as Keep N/A".format(
                    agent_num, entry.get("filename", "?"), entry["decision"]))
                entry["decision"] = "Keep N/A"

        per_agent[agent_num] = results
        all_results.extend(results)
        print("  Agent {}: {} papers loaded".format(agent_num, len(results)))

    return all_results, per_agent


def validate_completeness(all_results, expected_filenames):
    """Check for duplicates and missing papers."""
    result_filenames = [r["filename"] for r in all_results]

    # Check duplicates
    counts = Counter(result_filenames)
    duplicates = {f: c for f, c in counts.items() if c > 1}
    if duplicates:
        print("WARNING: Duplicate filenames found (keeping first occurrence):")
        for f, c in duplicates.items():
            print("  {} (appears {} times)".format(f, c))
        # Deduplicate: keep first occurrence
        seen = set()
        deduped = []
        for r in all_results:
            if r["filename"] not in seen:
                seen.add(r["filename"])
                deduped.append(r)
        return deduped

    # Check missing
    result_set = set(result_filenames)
    expected_set = set(expected_filenames)

    missing = expected_set - result_set
    if missing:
        print("WARNING: {} papers missing from results:".format(len(missing)))
        for f in sorted(missing)[:20]:
            print("  {}".format(f))

    extra = result_set - expected_set
    if extra:
        print("WARNING: {} unexpected filenames in results:".format(len(extra)))
        for f in sorted(extra)[:10]:
            print("  {}".format(f))

    print("  Validation: {} unique papers".format(len(set(result_filenames))))
    return all_results


def _resolve_tradition_field(tradition):
    """Resolve a tradition name to its rv_* field name.

    Handles canonical display names, aliases, and direct field names.
    Returns (rv_field, display_name) or (None, None) if unresolvable.
    """
    # Direct field name
    if tradition in FIELD_DISPLAY_NAMES:
        return tradition, FIELD_DISPLAY_NAMES[tradition]

    # Canonical display name
    if tradition in DISPLAY_NAME_TO_FIELD:
        return DISPLAY_NAME_TO_FIELD[tradition], tradition

    # Alias
    canonical = TRADITION_ALIASES.get(tradition)
    if canonical and canonical in DISPLAY_NAME_TO_FIELD:
        return DISPLAY_NAME_TO_FIELD[canonical], canonical

    return None, None


def apply_reclassifications(decisions, dry_run=False):
    """Apply Reclassify decisions to paper YAML using safe regex replacement.

    Sets the relevant rv_* score field to 75 (confident detection) and
    updates derived religious_values + religious_values_list strings.

    YAML SAFETY: Uses line-level regex replacement — never parse->rebuild.
    """
    applied = 0
    errors = 0

    for entry in decisions:
        fname = entry["filename"]
        tradition = entry.get("religious_tradition", "").strip()
        if not tradition or tradition == "N/A":
            print("  SKIP {}: no tradition specified".format(fname))
            continue

        # Resolve tradition to rv_* field
        rv_field, display_name = _resolve_tradition_field(tradition)
        if not rv_field:
            print("  SKIP {}: unrecognized tradition '{}'".format(fname, tradition))
            errors += 1
            continue

        paper_path = PAPERS_DIR / fname
        if not paper_path.exists():
            print("  SKIP {}: file not found".format(fname))
            errors += 1
            continue

        content = paper_path.read_text(encoding="utf-8")

        try:
            fm_text, body = extract_frontmatter(content)
        except ValueError as e:
            print("  SKIP {}: bad frontmatter — {}".format(fname, e))
            errors += 1
            continue

        new_fm = fm_text

        # Read existing rv_* scores
        scores = {}
        for f in RV_FIELDS:
            # Parse existing value from frontmatter
            m = re.search(r'^' + re.escape(f) + r':\s*(.*)$', new_fm, re.MULTILINE)
            if m:
                scores[f] = parse_rv_value(m.group(1).strip())
            else:
                scores[f] = 0

        # Set the target tradition to 75 (confident agent-verified detection)
        scores[rv_field] = max(scores[rv_field], 75)

        # Update all rv_* fields using safe_yaml_set_int
        for f in RV_FIELDS:
            new_fm, _ = safe_yaml_set_int(new_fm, f, scores[f])

        # Derive and update string fields
        derived_rv = derive_religious_values_string(scores)
        derived_list = derive_religious_values_list_string(scores)

        new_fm, n1 = re.subn(
            r'^religious_values:.*$',
            'religious_values: "{}"'.format(derived_rv),
            new_fm, count=1, flags=re.MULTILINE
        )
        if n1 == 0:
            new_fm = new_fm.rstrip() + '\nreligious_values: "{}"'.format(derived_rv)

        new_fm, n2 = re.subn(
            r'^religious_values_list:.*$',
            'religious_values_list: "{}"'.format(derived_list),
            new_fm, count=1, flags=re.MULTILINE
        )
        if n2 == 0:
            new_fm = new_fm.rstrip() + '\nreligious_values_list: "{}"'.format(derived_list)

        # Validate before writing
        is_valid, issues = validate_frontmatter(new_fm)
        if not is_valid:
            print("  SKIP {}: validation failed — {}".format(fname, issues))
            errors += 1
            continue

        if dry_run:
            print("  DRY-RUN {}: {} → {} ({} = 75)".format(
                fname, "N/A", display_name, rv_field))
        else:
            # Reconstruct and write
            new_content = "---\n{}\n---\n{}".format(new_fm.rstrip(), body)
            paper_path.write_text(new_content, encoding="utf-8")
            print("  APPLIED {}: N/A → {} ({} = 75)".format(
                fname, display_name, rv_field))

        applied += 1

    return applied, errors


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Consolidate religious audit results")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be applied without modifying files")
    parser.add_argument("--apply", action="store_true",
                        help="Apply reclassification decisions to paper YAML")
    args = parser.parse_args()

    print("=== CONSOLIDATING RELIGIOUS AUDIT RESULTS ===\n")

    # Load expected filenames from batches
    expected = load_batch_filenames()
    print("Expected papers: {}\n".format(len(expected)))

    # Load all agent results
    all_results, per_agent = load_agent_results()

    # Validate completeness
    print()
    all_results = validate_completeness(all_results, expected)

    # Sort by filename
    all_results.sort(key=lambda r: r["filename"])

    # Count decisions
    decision_counts = Counter(r["decision"] for r in all_results)
    print("\n=== DECISION SUMMARY ===")
    print("  Reclassify: {}".format(decision_counts.get("Reclassify", 0)))
    print("  Keep N/A:   {}".format(decision_counts.get("Keep N/A", 0)))
    print("  Uncertain:  {}".format(decision_counts.get("Uncertain", 0)))
    print("  Total:      {}".format(sum(decision_counts.values())))

    # Per-agent breakdown
    print("\n=== PER-AGENT BREAKDOWN ===")
    for agent_id in sorted(per_agent.keys()):
        agent_counts = Counter(r["decision"] for r in per_agent[agent_id])
        print("  Agent {}: {} papers — Reclassify={}, Keep N/A={}, Uncertain={}".format(
            agent_id, len(per_agent[agent_id]),
            agent_counts.get("Reclassify", 0),
            agent_counts.get("Keep N/A", 0),
            agent_counts.get("Uncertain", 0)))

    # Tradition breakdown for Reclassify decisions
    reclassify = [r for r in all_results if r["decision"] == "Reclassify"]
    if reclassify:
        tradition_counts = Counter(r.get("religious_tradition", "?") for r in reclassify)
        print("\n=== RECLASSIFICATION TARGETS ===")
        for trad, count in tradition_counts.most_common():
            print("  {}: {}".format(trad, count))

    # Write consolidated output
    all_path = LOGS_DIR / "20260215-religious_audit_all_classifications.json"
    with open(all_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print("\nAll classifications: {} ({} entries)".format(all_path, len(all_results)))

    # Write decisions only (Reclassify)
    decisions_path = LOGS_DIR / "20260215-religious_audit_decisions.json"
    with open(decisions_path, "w", encoding="utf-8") as f:
        json.dump(reclassify, f, indent=2, ensure_ascii=False)
    print("Decisions (Reclassify): {} ({} entries)".format(decisions_path, len(reclassify)))

    # Apply if requested
    if args.apply or args.dry_run:
        print("\n=== {} RECLASSIFICATIONS ===".format(
            "DRY-RUN" if args.dry_run else "APPLYING"))
        applied, errors = apply_reclassifications(reclassify, dry_run=args.dry_run)
        print("\n  Applied: {}".format(applied))
        print("  Errors:  {}".format(errors))
        if not args.dry_run and applied > 0:
            print("\n  IMPORTANT: Run validate_all_papers.py to verify YAML integrity!")
    else:
        print("\nTo apply reclassifications, run with --apply (or --dry-run to preview)")

    print("\n=== DONE ===")


if __name__ == "__main__":
    main()
