#!/usr/bin/env python3
"""
Consolidate benchmark survey results from 20 agents.

Reads results_agent_01.json through results_agent_20.json, validates
completeness, and produces consolidated output files.

Output:
  - logs/benchmark_survey_all_classifications.json  (all 924 entries)
  - logs/benchmark_survey_candidates.json           (only Yes candidates)
"""

import json
import sys
from pathlib import Path
from collections import Counter

sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))
from config import LOGS_DIR, PAPERS_DIR

NUM_AGENTS = 20
BATCHES_DIR = LOGS_DIR / "benchmark_survey_batches"
REQUIRED_FIELDS_YES = {"filename", "decision", "reasoning"}
REQUIRED_FIELDS_EXCLUDE = {"filename", "decision", "reasoning"}
VALID_DECISIONS = {"Yes", "Exclude"}


def load_batch_filenames():
    """Load all filenames from the 20 batch files for validation."""
    all_filenames = []
    for i in range(1, NUM_AGENTS + 1):
        batch_path = BATCHES_DIR / "batch_{:02d}.json".format(i)
        with open(batch_path, "r", encoding="utf-8") as f:
            batch = json.load(f)
        all_filenames.extend(entry["filename"] for entry in batch)
    return all_filenames


def load_agent_results():
    """Load and validate all 20 agent result files."""
    all_results = []
    per_agent = {}
    errors = []

    for i in range(1, NUM_AGENTS + 1):
        result_path = BATCHES_DIR / "results_agent_{:02d}.json".format(i)
        if not result_path.exists():
            print("ERROR: Missing result file: {}".format(result_path.name))
            errors.append(i)
            continue

        with open(result_path, "r", encoding="utf-8") as f:
            results = json.load(f)

        # Validate fields
        for entry in results:
            if entry.get("decision") not in VALID_DECISIONS:
                print("WARN: Agent {:02d}, paper '{}': invalid decision '{}' — treating as Exclude".format(
                    i, entry.get("filename", "?"), entry.get("decision", "?")))
                entry["decision"] = "Exclude"

            required = REQUIRED_FIELDS_YES if entry["decision"] == "Yes" else REQUIRED_FIELDS_EXCLUDE
            missing = required - set(entry.keys())
            if missing:
                print("WARN: Agent {:02d}, paper '{}': missing fields {}".format(
                    i, entry.get("filename", "?"), missing))

        per_agent[i] = results
        all_results.extend(results)
        print("  Agent {:02d}: {} papers loaded".format(i, len(results)))

    if errors:
        print("\nERROR: {} agent result files missing: {}".format(len(errors), errors))
        sys.exit(1)

    return all_results, per_agent


def validate_completeness(all_results, expected_filenames):
    """Ensure all expected papers are present, flag duplicates and missing."""
    result_filenames = [r["filename"] for r in all_results]

    # Check duplicates
    counts = Counter(result_filenames)
    duplicates = {f: c for f, c in counts.items() if c > 1}
    if duplicates:
        print("WARNING: Duplicate filenames found (keeping first occurrence):")
        for f, c in duplicates.items():
            print("  {} (appears {} times)".format(f, c))

    # Check missing
    result_set = set(result_filenames)
    expected_set = set(expected_filenames)

    missing = expected_set - result_set
    if missing:
        print("WARNING: {} papers missing from results:".format(len(missing)))
        for f in sorted(missing)[:20]:
            print("  {}".format(f))
        if len(missing) > 20:
            print("  ... and {} more".format(len(missing) - 20))

    extra = result_set - expected_set
    if extra:
        print("WARNING: {} unexpected filenames in results:".format(len(extra)))
        for f in sorted(extra):
            print("  {}".format(f))

    print("  Validation: {} unique papers".format(len(result_set)))
    return missing


def main():
    print("=== CONSOLIDATING BENCHMARK SURVEY RESULTS ===\n")

    # Load expected filenames from batches
    expected = load_batch_filenames()
    print("Expected papers: {}\n".format(len(expected)))

    # Load all agent results
    all_results, per_agent = load_agent_results()

    # Validate completeness
    print()
    missing = validate_completeness(all_results, expected)

    # Deduplicate (keep first occurrence)
    seen = set()
    deduped = []
    for r in all_results:
        if r["filename"] not in seen:
            seen.add(r["filename"])
            deduped.append(r)
    all_results = deduped

    # Sort by filename for consistent output
    all_results.sort(key=lambda r: r["filename"])

    # Count decisions
    decision_counts = Counter(r["decision"] for r in all_results)
    print("\n=== DECISION SUMMARY ===")
    print("  Yes:     {}".format(decision_counts.get("Yes", 0)))
    print("  Exclude: {}".format(decision_counts.get("Exclude", 0)))
    print("  Total:   {}".format(sum(decision_counts.values())))

    # Per-agent breakdown
    print("\n=== PER-AGENT BREAKDOWN ===")
    for i in sorted(per_agent.keys()):
        agent_counts = Counter(r["decision"] for r in per_agent[i])
        print("  Agent {:02d}: {} papers — Yes={}, Exclude={}".format(
            i, len(per_agent[i]),
            agent_counts.get("Yes", 0),
            agent_counts.get("Exclude", 0)))

    # Write consolidated output
    all_path = LOGS_DIR / "benchmark_survey_all_classifications.json"
    with open(all_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print("\nAll classifications: {} ({} entries)".format(all_path, len(all_results)))

    # Write candidates only (Yes)
    candidates = [r for r in all_results if r["decision"] == "Yes"]
    candidates_path = LOGS_DIR / "benchmark_survey_candidates.json"
    with open(candidates_path, "w", encoding="utf-8") as f:
        json.dump(candidates, f, indent=2, ensure_ascii=False)
    print("Candidates (Yes): {} ({} entries)".format(candidates_path, len(candidates)))

    # Print candidate summary
    if candidates:
        print("\n=== CANDIDATE BENCHMARKS/DATASETS ===")
        for c in candidates:
            name = c.get("benchmark_name", "Unnamed")
            what = c.get("what_measures", "")
            print("  [{}] {} — {}".format(name, c["filename"][:60], what[:80]))

    if missing:
        print("\nWARNING: {} papers were not classified — rerun missing agents".format(len(missing)))

    print("\n=== DONE ===")


if __name__ == "__main__":
    main()
