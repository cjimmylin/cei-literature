#!/usr/bin/env python3
"""
Consolidate language list agent results and apply to papers.

Reads agent output JSON files, validates entries, and inserts the
languages_list YAML field after cultures_nationalities_list
in each paper's frontmatter.

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/consolidate_language_lists.py
    ../.venv/bin/python PYTHON/consolidate_language_lists.py --dry-run
    ../.venv/bin/python PYTHON/consolidate_language_lists.py --manifest logs/20260216-language_list_manifest.json

Output:
    logs/YYYYMMDD-language_list_consolidation.json
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

REQUIRED_FIELDS = {"filename", "languages_list"}


def load_manifest(manifest_path=None):
    """Load manifest to find agent result files."""
    if manifest_path:
        mpath = Path(manifest_path)
    else:
        # Find most recent manifest
        manifests = sorted(LOGS_DIR.glob("*-language_list_manifest.json"), reverse=True)
        if not manifests:
            print("ERROR: No manifest file found. Run generate_language_list_batches.py first.")
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
        result_name = f"{date}-language_list_agent_{i:02d}.json"
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

    # Count blanks vs populated
    blank_count = 0
    populated_count = 0
    for r in deduped:
        value = r.get("languages_list", "")
        if value.strip():
            populated_count += 1
        else:
            blank_count += 1

    print(f"\nValidation: {len(deduped)} unique papers")
    print(f"  With language data: {populated_count}")
    print(f"  Blank (no language focus): {blank_count}")
    return deduped, []


def safe_yaml_value(value):
    """Sanitize a value for safe YAML insertion (replace double quotes with single)."""
    return str(value).replace('"', "'")


def insert_language_list_field(fm_text, languages_value):
    """
    Insert or replace languages_list field in frontmatter.

    Strategy:
    1. If field already exists, replace in-place (idempotent)
    2. Insert after cultures_nationalities_list line
    3. Insert after national_ethnic_cultural line (fallback)
    4. Append to end of frontmatter (last resort)

    Uses safe regex - NEVER parse/rebuild round-trip.
    """
    safe_value = safe_yaml_value(languages_value)
    new_fm = fm_text

    # Strategy 1: Replace existing field in-place (idempotent)
    new_fm, count = re.subn(
        r'^languages_list:.*$',
        f'languages_list: "{safe_value}"',
        new_fm,
        count=1,
        flags=re.MULTILINE,
    )
    if count > 0:
        return new_fm

    # Strategy 2: Insert after cultures_nationalities_list line
    new_fm, count = re.subn(
        r'^(cultures_nationalities_list:.*?)$',
        rf'\1\nlanguages_list: "{safe_value}"',
        fm_text,
        count=1,
        flags=re.MULTILINE,
    )
    if count > 0:
        return new_fm

    # Strategy 3: Insert after national_ethnic_cultural line
    new_fm, count = re.subn(
        r'^(national_ethnic_cultural:.*?)$',
        rf'\1\nlanguages_list: "{safe_value}"',
        fm_text,
        count=1,
        flags=re.MULTILINE,
    )
    if count > 0:
        return new_fm

    # Strategy 4: Fallback — append to end of frontmatter
    new_fm = fm_text.rstrip() + f'\nlanguages_list: "{safe_value}"'
    return new_fm


def apply_to_paper(paper_path, entry, dry_run=False):
    """Apply languages_list to a single paper."""
    try:
        content = paper_path.read_text(encoding="utf-8")
        fm_text, body = extract_frontmatter(content)
    except (ValueError, UnicodeDecodeError) as e:
        return {"status": "error", "error": str(e)}

    # Check if already has a non-empty value (idempotent — skip if populated)
    fields = parse_frontmatter(fm_text)
    existing = fields.get("languages_list", "").strip()
    if existing:
        return {"status": "skipped", "reason": "already has languages_list"}

    languages_value = entry["languages_list"]

    # Insert YAML field
    new_fm = insert_language_list_field(fm_text, languages_value)

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
    parser = argparse.ArgumentParser(description="Consolidate language list results")
    parser.add_argument("--manifest", type=str, default="",
                        help="Path to manifest JSON (default: most recent)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview mode: validate without writing")
    args = parser.parse_args()

    print("=== CONSOLIDATING LANGUAGE LIST RESULTS ===\n")

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
    language_counts = Counter()
    blank_count = 0
    for r in deduped:
        value = r.get("languages_list", "")
        if not value.strip():
            blank_count += 1
        else:
            for lang in value.split(","):
                language_counts[lang.strip()] += 1

    print("\n=== CONTENT SUMMARY ===")
    print(f"  Papers with language data: {len(deduped) - blank_count} / {len(deduped)}")
    print(f"  Papers with no language focus: {blank_count}")

    if language_counts:
        print(f"\n  Top 20 languages:")
        for lang, count in language_counts.most_common(20):
            print(f"    {lang}: {count}")

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
            "languages_list": entry.get("languages_list", ""),
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
        "top_languages": dict(language_counts.most_common(50)),
        "papers_with_data": len(deduped) - blank_count,
        "papers_blank": blank_count,
        "entries": log,
    }

    if not args.dry_run:
        out_path = LOGS_DIR / f"{DATE_PREFIX}-language_list_consolidation.json"
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
