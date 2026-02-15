#!/usr/bin/env python3
"""
Consolidate culture list agent results and apply to papers.

Reads agent output JSON files, validates entries, and inserts the
cultures_nationalities_list YAML field after national_ethnic_cultural
in each paper's frontmatter.

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/consolidate_culture_lists.py
    ../.venv/bin/python PYTHON/consolidate_culture_lists.py --dry-run
    ../.venv/bin/python PYTHON/consolidate_culture_lists.py --manifest logs/20260215-culture_list_manifest.json

Output:
    logs/YYYYMMDD-culture_list_consolidation.json
"""

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

sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))
from yaml_utils import extract_frontmatter, validate_frontmatter, parse_frontmatter
from config import PAPERS_DIR, LOGS_DIR

DATE_PREFIX = datetime.now().strftime("%Y%m%d")

REQUIRED_FIELDS = {"filename", "cultures_nationalities_list"}


def load_manifest(manifest_path=None):
    """Load manifest to find agent result files."""
    if manifest_path:
        mpath = Path(manifest_path)
    else:
        # Find most recent manifest
        manifests = sorted(LOGS_DIR.glob("*-culture_list_manifest.json"), reverse=True)
        if not manifests:
            print("ERROR: No manifest file found. Run generate_culture_list_batches.py first.")
            sys.exit(1)
        mpath = manifests[0]

    print(f"Loading manifest: {mpath.name}")
    with open(mpath, "r", encoding="utf-8") as f:
        return json.load(f), mpath


def load_agent_results(manifest):
    """Load all agent result JSON files."""
    all_results = []
    date = manifest["date"]
    num_batches = manifest["num_batches"]

    for i in range(1, num_batches + 1):
        result_name = f"{date}-culture_list_agent_{i:02d}.json"
        result_path = LOGS_DIR / result_name
        if not result_path.exists():
            print(f"WARNING: Missing agent result file: {result_name} (skipping)")
            continue

        with open(result_path, "r", encoding="utf-8") as f:
            results = json.load(f)

        # Validate required fields
        valid_entries = []
        for entry in results:
            missing = REQUIRED_FIELDS - set(entry.keys())
            if missing:
                print(f"  WARNING: Agent {i:02d}, paper '{entry.get('filename', '?')}': missing fields {missing}")
                continue
            valid_entries.append(entry)

        all_results.extend(valid_entries)
        print(f"  Agent {i:02d}: {len(valid_entries)} papers loaded")

    return all_results


def validate_results(all_results):
    """Validate completeness and quality of results."""
    # Check for duplicates
    filenames = [r["filename"] for r in all_results]
    counts = Counter(filenames)
    duplicates = {f: c for f, c in counts.items() if c > 1}
    if duplicates:
        print("WARNING: Duplicate filenames (last entry wins):")
        for f, c in duplicates.items():
            print(f"  {f} (appears {c} times)")

    # Deduplicate: keep last entry for each filename
    seen = {}
    for r in all_results:
        seen[r["filename"]] = r
    deduped = list(seen.values())

    # Validate values
    issues = []
    for r in deduped:
        value = r.get("cultures_nationalities_list", "")
        if not value:
            issues.append(f"{r['filename']}: Empty cultures_nationalities_list")

    if issues:
        print(f"\nWARNINGS ({len(issues)} issues):")
        for issue in issues[:20]:
            print(f"  {issue}")
        if len(issues) > 20:
            print(f"  ... and {len(issues) - 20} more")

    print(f"\nValidation: {len(deduped)} unique papers, {len(issues)} issues")
    return deduped, issues


def safe_yaml_value(value):
    """Sanitize a value for safe YAML insertion (replace double quotes with single)."""
    return str(value).replace('"', "'")


def insert_culture_list_field(fm_text, cultures_value):
    """
    Insert or replace cultures_nationalities_list field in frontmatter.

    Strategy:
    1. If field already exists, replace in-place (idempotent)
    2. Otherwise, insert after national_ethnic_cultural line
    3. Fallback: append to end of frontmatter

    Uses safe regex - NEVER parse/rebuild round-trip.
    """
    safe_value = safe_yaml_value(cultures_value)
    new_fm = fm_text

    # Strategy 1: Replace existing field in-place (idempotent)
    new_fm, count = re.subn(
        r'^cultures_nationalities_list:.*$',
        f'cultures_nationalities_list: "{safe_value}"',
        new_fm,
        count=1,
        flags=re.MULTILINE,
    )
    if count > 0:
        return new_fm

    # Strategy 2: Insert after national_ethnic_cultural line
    new_fm, count = re.subn(
        r'^(national_ethnic_cultural:.*?)$',
        rf'\1\ncultures_nationalities_list: "{safe_value}"',
        fm_text,
        count=1,
        flags=re.MULTILINE,
    )
    if count > 0:
        return new_fm

    # Strategy 3: Fallback — append to end of frontmatter
    new_fm = fm_text.rstrip() + f'\ncultures_nationalities_list: "{safe_value}"'
    return new_fm


def apply_to_paper(paper_path, entry, dry_run=False):
    """Apply cultures_nationalities_list to a single paper."""
    try:
        content = paper_path.read_text(encoding="utf-8")
        fm_text, body = extract_frontmatter(content)
    except (ValueError, UnicodeDecodeError) as e:
        return {"status": "error", "error": str(e)}

    # Check if already has a real (non-placeholder) value (idempotent)
    fields = parse_frontmatter(fm_text)
    existing = fields.get("cultures_nationalities_list", "").strip()
    if existing and existing.upper() not in ("NA", "N/A", ""):
        return {"status": "skipped", "reason": "already has cultures_nationalities_list"}

    cultures_value = entry["cultures_nationalities_list"]

    # Insert YAML field
    new_fm = insert_culture_list_field(fm_text, cultures_value)

    # Validate YAML before writing
    is_valid, issues = validate_frontmatter(new_fm)
    if not is_valid:
        return {"status": "error", "error": f"YAML validation failed: {issues}"}

    if dry_run:
        return {"status": "dry_run", "would_update": True}

    # Write back
    reconstructed = f"---\n{new_fm.rstrip()}\n---\n{body}"
    paper_path.write_text(reconstructed, encoding="utf-8")

    return {"status": "updated"}


def main():
    parser = argparse.ArgumentParser(description="Consolidate culture list results")
    parser.add_argument("--manifest", type=str, default="",
                        help="Path to manifest JSON (default: most recent)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview mode: validate without writing")
    args = parser.parse_args()

    print("=== CONSOLIDATING CULTURE LIST RESULTS ===\n")

    # Load manifest
    manifest, manifest_path = load_manifest(args.manifest or None)
    print(f"Date: {manifest['date']}, Batches: {manifest['num_batches']}, Papers: {manifest['total_papers']}")

    # Load all agent results
    print("\nLoading agent results:")
    all_results = load_agent_results(manifest)

    # Validate and deduplicate
    print()
    deduped, issues = validate_results(all_results)

    # Sort for consistent processing
    deduped.sort(key=lambda r: r["filename"])

    # Content summary
    culture_counts = Counter()
    has_na = 0
    for r in deduped:
        value = r.get("cultures_nationalities_list", "N/A")
        if value.upper() in ("N/A", "NA"):
            has_na += 1
        else:
            for c in value.split(","):
                culture_counts[c.strip()] += 1

    print("\n=== CONTENT SUMMARY ===")
    print(f"  Papers with culture data: {len(deduped) - has_na} / {len(deduped)}")
    print(f"  Papers with N/A: {has_na}")

    if culture_counts:
        print(f"\n  Top 20 cultures:")
        for culture, count in culture_counts.most_common(20):
            print(f"    {culture}: {count}")

    # Apply to papers
    print(f"\n=== APPLYING TO PAPERS{' (DRY RUN)' if args.dry_run else ''} ===")
    log = []
    status_counts = Counter()

    for entry in deduped:
        paper_path = PAPERS_DIR / entry["filename"]
        if not paper_path.exists():
            print(f"  MISSING: {entry['filename']}")
            log.append({"filename": entry["filename"], "status": "missing"})
            status_counts["missing"] += 1
            continue

        result = apply_to_paper(paper_path, entry, dry_run=args.dry_run)
        status = result["status"]
        status_counts[status] += 1

        log.append({
            "filename": entry["filename"],
            "status": status,
            "cultures_nationalities_list": entry.get("cultures_nationalities_list", ""),
        })

        if status == "error":
            print(f"  ERROR: {entry['filename']} -- {result.get('error', '')}")

    print(f"\n=== RESULTS ===")
    for status, count in sorted(status_counts.items()):
        print(f"  {status}: {count}")

    # Write consolidation log
    consolidation = {
        "date": DATE_PREFIX,
        "manifest": manifest_path.name,
        "total_processed": len(deduped),
        "status_counts": dict(status_counts),
        "top_cultures": dict(culture_counts.most_common(50)),
        "papers_with_data": len(deduped) - has_na,
        "papers_na": has_na,
        "entries": log,
    }

    if not args.dry_run:
        out_path = LOGS_DIR / f"{DATE_PREFIX}-culture_list_consolidation.json"
        tmp_path = out_path.parent / f".tmp.{os.getpid()}.json"
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(consolidation, f, indent=2, ensure_ascii=False)
        os.replace(str(tmp_path), str(out_path))
        print(f"\nConsolidation log: {out_path.name}")
    else:
        print("\n(Dry run -- no files modified)")

    print("\n=== DONE ===")


if __name__ == "__main__":
    main()
