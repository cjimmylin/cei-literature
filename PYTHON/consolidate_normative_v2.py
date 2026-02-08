#!/usr/bin/env python3
"""
Consolidate normative ethics v2 classification results from 10 agents.

Reads results_agent_01.json through results_agent_10.json, validates
completeness, reconciles with the previous round (63 papers), and
produces consolidated output files.

Output:
  - logs/20260207-normative_v2_all_classifications.json  (all 266 entries)
  - logs/20260207-normative_v2_decisions.json            (only Yes + Borderline)
"""

import json
import sys
from pathlib import Path
from collections import Counter

sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))
from config import LOGS_DIR, PAPERS_DIR

BATCHES_DIR = LOGS_DIR / "normative_v2_batches"
REQUIRED_FIELDS = {"filename", "decision", "normative_frameworks",
                   "data_artifact", "llms_tested", "reasoning"}
VALID_DECISIONS = {"Yes", "Borderline", "Exclude"}


def load_batch_filenames():
    """Load all filenames from the 10 batch files for validation."""
    all_filenames = []
    for i in range(1, 11):
        batch_path = BATCHES_DIR / "batch_{:02d}.json".format(i)
        with open(batch_path, "r", encoding="utf-8") as f:
            batch = json.load(f)
        all_filenames.extend(entry["filename"] for entry in batch)
    return all_filenames


def load_agent_results():
    """Load and validate all 10 agent result files."""
    all_results = []
    per_agent = {}

    for i in range(1, 11):
        result_path = BATCHES_DIR / "results_agent_{:02d}.json".format(i)
        if not result_path.exists():
            print("ERROR: Missing result file: {}".format(result_path.name))
            sys.exit(1)

        with open(result_path, "r", encoding="utf-8") as f:
            results = json.load(f)

        # Validate fields
        for entry in results:
            missing = REQUIRED_FIELDS - set(entry.keys())
            if missing:
                print("ERROR: Agent {:02d}, paper '{}': missing fields {}".format(
                    i, entry.get("filename", "?"), missing))
                sys.exit(1)

            if entry["decision"] not in VALID_DECISIONS:
                print("ERROR: Agent {:02d}, paper '{}': invalid decision '{}'".format(
                    i, entry.get("filename", "?"), entry["decision"]))
                sys.exit(1)

        per_agent[i] = results
        all_results.extend(results)
        print("  Agent {:02d}: {} papers loaded".format(i, len(results)))

    return all_results, per_agent


def validate_completeness(all_results, expected_filenames):
    """Ensure exactly 266 unique papers, no duplicates, no missing."""
    result_filenames = [r["filename"] for r in all_results]

    # Check duplicates
    counts = Counter(result_filenames)
    duplicates = {f: c for f, c in counts.items() if c > 1}
    if duplicates:
        print("ERROR: Duplicate filenames found:")
        for f, c in duplicates.items():
            print("  {} (appears {} times)".format(f, c))
        sys.exit(1)

    # Check missing
    result_set = set(result_filenames)
    expected_set = set(expected_filenames)

    missing = expected_set - result_set
    if missing:
        print("ERROR: {} papers missing from results:".format(len(missing)))
        for f in sorted(missing):
            print("  {}".format(f))
        sys.exit(1)

    extra = result_set - expected_set
    if extra:
        print("WARNING: {} unexpected filenames in results:".format(len(extra)))
        for f in sorted(extra):
            print("  {}".format(f))

    print("  Validation: {} unique papers, no duplicates ✓".format(len(result_set)))


def reconcile_with_previous(all_results):
    """Compare with the previous round's classifications."""
    prev_path = LOGS_DIR / "20260207-normative_ethics_all_classifications_20260207.json"
    if not prev_path.exists():
        print("\n  Previous classification file not found — skipping reconciliation")
        return

    with open(prev_path, "r", encoding="utf-8") as f:
        prev_results = json.load(f)

    prev_by_name = {r["filename"]: r["decision"] for r in prev_results}
    prev_filenames = set(prev_by_name.keys())

    v2_by_name = {r["filename"]: r["decision"] for r in all_results}

    print("\n=== RECONCILIATION WITH PREVIOUS ROUND ===")
    print("Previous round: {} papers classified".format(len(prev_results)))

    # Compare decisions for papers in both rounds
    same = 0
    upgraded = []
    downgraded = []

    for fname in sorted(prev_filenames):
        if fname not in v2_by_name:
            continue
        old_d = prev_by_name[fname]
        new_d = v2_by_name[fname]

        if old_d == new_d:
            same += 1
        else:
            rank = {"Yes": 3, "Borderline": 2, "Exclude": 1}
            if rank.get(new_d, 0) > rank.get(old_d, 0):
                upgraded.append((fname, old_d, new_d))
            else:
                downgraded.append((fname, old_d, new_d))

    print("  Consistent: {}".format(same))
    print("  Upgraded:   {}".format(len(upgraded)))
    print("  Downgraded: {}".format(len(downgraded)))

    if upgraded:
        print("\n  UPGRADED (more inclusive in v2):")
        for fname, old_d, new_d in upgraded:
            print("    {} → {} : {}".format(old_d, new_d, fname))

    if downgraded:
        print("\n  DOWNGRADED (more restrictive in v2):")
        for fname, old_d, new_d in downgraded:
            print("    {} → {} : {}".format(old_d, new_d, fname))

    # New discoveries: papers NOT in previous 63 that scored Yes/Borderline
    new_discoveries = []
    for r in all_results:
        if r["filename"] not in prev_filenames and r["decision"] in ("Yes", "Borderline"):
            new_discoveries.append(r)

    print("\n  NEW DISCOVERIES (not in previous 63, scored Yes/Borderline): {}".format(
        len(new_discoveries)))
    for r in sorted(new_discoveries, key=lambda x: (-{"Yes": 2, "Borderline": 1}.get(x["decision"], 0), x["filename"])):
        print("    [{}] {} — {}".format(r["decision"], r["filename"],
                                        r["normative_frameworks"]))


def main():
    print("=== CONSOLIDATING NORMATIVE ETHICS V2 RESULTS ===\n")

    # Load expected filenames from batches
    expected = load_batch_filenames()
    print("Expected papers: {}\n".format(len(expected)))

    # Load all agent results
    all_results, per_agent = load_agent_results()

    # Validate completeness
    print()
    validate_completeness(all_results, expected)

    # Sort by filename for consistent output
    all_results.sort(key=lambda r: r["filename"])

    # Count decisions
    decision_counts = Counter(r["decision"] for r in all_results)
    print("\n=== DECISION SUMMARY ===")
    print("  Yes:        {}".format(decision_counts.get("Yes", 0)))
    print("  Borderline: {}".format(decision_counts.get("Borderline", 0)))
    print("  Exclude:    {}".format(decision_counts.get("Exclude", 0)))
    print("  Total:      {}".format(sum(decision_counts.values())))

    # Per-agent breakdown
    print("\n=== PER-AGENT BREAKDOWN ===")
    for i in sorted(per_agent.keys()):
        agent_counts = Counter(r["decision"] for r in per_agent[i])
        print("  Agent {:02d}: {} papers — Yes={}, Borderline={}, Exclude={}".format(
            i, len(per_agent[i]),
            agent_counts.get("Yes", 0),
            agent_counts.get("Borderline", 0),
            agent_counts.get("Exclude", 0)))

    # Write consolidated output
    all_path = LOGS_DIR / "20260207-normative_v2_all_classifications.json"
    with open(all_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print("\nAll classifications: {} ({} entries)".format(all_path, len(all_results)))

    # Write decisions only (Yes + Borderline)
    decisions = [r for r in all_results if r["decision"] in ("Yes", "Borderline")]
    decisions_path = LOGS_DIR / "20260207-normative_v2_decisions.json"
    with open(decisions_path, "w", encoding="utf-8") as f:
        json.dump(decisions, f, indent=2, ensure_ascii=False)
    print("Decisions (Yes+Borderline): {} ({} entries)".format(decisions_path, len(decisions)))

    # Reconcile with previous round
    reconcile_with_previous(all_results)

    print("\n=== DONE ===")


if __name__ == "__main__":
    main()
