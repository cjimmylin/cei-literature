#!/usr/bin/env python3
"""
Consolidate per-agent incomplete author resolution results.

Since resolve_incomplete_authors.py already writes YAML directly to papers,
this consolidator only merges per-agent result JSONs with the previous log,
deduplicates, and reports statistics.

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/consolidate_incomplete_authors.py
    ../.venv/bin/python PYTHON/consolidate_incomplete_authors.py --manifest logs/20260216-incomplete_author_manifest.json

Output:
    logs/YYYYMMDD-incomplete_authors_resolved.json
"""

import argparse
import functools
import json
import os
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

print = functools.partial(print, flush=True)

sys.path.insert(0, str(Path(__file__).parent))
from vault_config import LOGS_DIR

DATE_PREFIX = datetime.now().strftime("%Y%m%d")


def load_manifest(manifest_path=None):
    """Load manifest to find agent result files."""
    if manifest_path:
        mpath = Path(manifest_path)
    else:
        manifests = sorted(LOGS_DIR.glob("*-incomplete_author_manifest.json"), reverse=True)
        if not manifests:
            print("ERROR: No manifest file found. Run generate_incomplete_author_batches.py first.")
            sys.exit(1)
        mpath = manifests[0]

    print(f"Loading manifest: {mpath.name}")
    with open(mpath, "r", encoding="utf-8") as f:
        return json.load(f), mpath


def main():
    parser = argparse.ArgumentParser(description="Consolidate incomplete author resolution results")
    parser.add_argument("--manifest", type=str, default="",
                        help="Path to manifest JSON (default: most recent)")
    parser.add_argument("--previous-log", type=str, default="",
                        help="Path to previous resolution log to merge with")
    args = parser.parse_args()

    print("=== CONSOLIDATING INCOMPLETE AUTHOR RESULTS ===\n")

    # Load manifest
    manifest, manifest_path = load_manifest(args.manifest or None)
    date = manifest["date"]
    num_batches = manifest["num_batches"]
    print(f"Date: {date}, Batches: {num_batches}, Papers: {manifest['total_papers']}")

    # Load previous log for merging
    prev_map = {}
    if args.previous_log:
        prev_path = Path(args.previous_log)
    else:
        # Find most recent previous log (not today's)
        prev_logs = sorted(LOGS_DIR.glob("*-incomplete_authors_resolved.json"), reverse=True)
        prev_path = None
        for p in prev_logs:
            if not p.name.startswith(DATE_PREFIX):
                prev_path = p
                break

    if prev_path and prev_path.exists():
        print(f"\nMerging with previous log: {prev_path.name}")
        with open(prev_path, "r", encoding="utf-8") as f:
            prev_data = json.load(f)
        for entry in prev_data:
            prev_map[entry["filename"]] = entry
        print(f"  Previous entries: {len(prev_map)}")

    # Load per-agent result files
    print("\nLoading agent results:")
    agent_map = {}
    agents_found = 0
    agents_missing = 0

    for i in range(1, num_batches + 1):
        result_name = f"{date}-incomplete_authors_agent_{i:02d}.json"
        result_path = LOGS_DIR / result_name
        if not result_path.exists():
            print(f"  WARNING: Missing agent result file: {result_name}")
            agents_missing += 1
            continue

        with open(result_path, "r", encoding="utf-8") as f:
            results = json.load(f)

        agents_found += 1
        for entry in results:
            fname = entry.get("filename", "")
            if fname:
                agent_map[fname] = entry

        status_counts = Counter(e.get("status", "?") for e in results)
        print(f"  Agent {i:02d}: {len(results)} papers — {dict(status_counts)}")

    print(f"\n  Agents found: {agents_found}, missing: {agents_missing}")
    print(f"  Total agent entries: {len(agent_map)}")

    # Merge: agent results override previous log (last entry wins)
    merged = dict(prev_map)
    for fname, entry in agent_map.items():
        merged[fname] = entry

    # Statistics
    status_totals = Counter()
    source_totals = Counter()
    for entry in merged.values():
        status_totals[entry.get("status", "unknown")] += 1
        if entry.get("status") == "resolved":
            source_totals[entry.get("source", "unknown")] += 1

    print("\n=== MERGED RESULTS ===")
    print(f"  Total entries: {len(merged)}")
    for status, count in sorted(status_totals.items(), key=lambda x: -x[1]):
        print(f"    {status}: {count}")

    if source_totals:
        print(f"\n  Resolution sources:")
        for src, count in sorted(source_totals.items(), key=lambda x: -x[1]):
            print(f"    {src}: {count}")

    # New resolutions from this run
    new_resolved = 0
    for fname, entry in agent_map.items():
        if entry.get("status") == "resolved":
            prev = prev_map.get(fname, {})
            if prev.get("status") != "resolved":
                new_resolved += 1

    print(f"\n  New resolutions this run: {new_resolved}")

    # Write merged log
    output_list = sorted(merged.values(), key=lambda x: x.get("filename", ""))
    out_path = LOGS_DIR / f"{DATE_PREFIX}-incomplete_authors_resolved.json"
    tmp_path = out_path.parent / f".tmp.{os.getpid()}.json"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(output_list, f, indent=2, ensure_ascii=False)
    os.replace(str(tmp_path), str(out_path))

    print(f"\nConsolidation log: {out_path.name}")

    # List unresolved
    unresolved = [e for e in merged.values() if e.get("status") != "resolved"]
    if unresolved:
        print(f"\nUnresolved papers ({len(unresolved)}):")
        for e in sorted(unresolved, key=lambda x: x.get("filename", "")):
            print(f"  - {e.get('filename', '?')} ({e.get('status', '?')}: {e.get('error', '')})")

    print("\n=== DONE ===")


if __name__ == "__main__":
    main()
