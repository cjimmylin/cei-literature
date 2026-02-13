#!/usr/bin/env python3
"""
Consolidate LLM assessment agent results and apply to papers.

Reads agent output JSON files, validates entries, and applies:
  - LLM_assessed YAML field (after data_metrics)
  - DATA_URL YAML field (after LLM_assessed)
  - ## Data Description body section (after ## Dataset Information or before ## Notes)

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/consolidate_llm_assessments.py
    ../.venv/bin/python PYTHON/consolidate_llm_assessments.py --dry-run
    ../.venv/bin/python PYTHON/consolidate_llm_assessments.py --manifest logs/20260212-llm_assessment_manifest.json

Output:
    logs/YYYYMMDD-llm_assessment_consolidation.json
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

REQUIRED_FIELDS = {"filename", "LLM_assessed", "DATA_URL", "data_description"}


def load_manifest(manifest_path=None):
    """Load manifest to find agent result files."""
    if manifest_path:
        mpath = Path(manifest_path)
    else:
        # Find most recent manifest
        manifests = sorted(LOGS_DIR.glob("*-llm_assessment_manifest.json"), reverse=True)
        if not manifests:
            print("ERROR: No manifest file found. Run generate_llm_assessment_batches.py first.")
            sys.exit(1)
        mpath = manifests[0]

    print("Loading manifest: {}".format(mpath.name))
    with open(mpath, "r", encoding="utf-8") as f:
        return json.load(f), mpath


def load_agent_results(manifest):
    """Load all agent result JSON files."""
    all_results = []
    date = manifest["date"]
    num_batches = manifest["num_batches"]

    for i in range(1, num_batches + 1):
        result_name = "{}-llm_assessment_agent_{:02d}.json".format(date, i)
        result_path = LOGS_DIR / result_name
        if not result_path.exists():
            print("ERROR: Missing agent result file: {}".format(result_name))
            sys.exit(1)

        with open(result_path, "r", encoding="utf-8") as f:
            results = json.load(f)

        # Validate required fields
        for entry in results:
            missing = REQUIRED_FIELDS - set(entry.keys())
            if missing:
                print("ERROR: Agent {:02d}, paper '{}': missing fields {}".format(
                    i, entry.get("filename", "?"), missing))
                sys.exit(1)

        all_results.extend(results)
        print("  Agent {:02d}: {} papers loaded".format(i, len(results)))

    return all_results


def validate_results(all_results, manifest):
    """Validate completeness and quality of results."""
    # Check for duplicates
    filenames = [r["filename"] for r in all_results]
    counts = Counter(filenames)
    duplicates = {f: c for f, c in counts.items() if c > 1}
    if duplicates:
        print("ERROR: Duplicate filenames:")
        for f, c in duplicates.items():
            print("  {} (appears {} times)".format(f, c))
        sys.exit(1)

    # Validate values
    issues = []
    for r in all_results:
        llm = r.get("LLM_assessed", "")
        url = r.get("DATA_URL", "")
        desc = r.get("data_description", "")

        # LLM_assessed should be "NA" or comma-separated model names
        if not llm:
            issues.append("{}: Empty LLM_assessed".format(r["filename"]))

        # DATA_URL should be "NA" or a valid URL
        if url and url != "NA" and not url.startswith("http"):
            issues.append("{}: Invalid DATA_URL: {}".format(r["filename"], url))

        # data_description should not be empty
        if not desc:
            issues.append("{}: Empty data_description".format(r["filename"]))

    if issues:
        print("\nWARNINGS ({} issues):".format(len(issues)))
        for issue in issues[:20]:
            print("  {}".format(issue))
        if len(issues) > 20:
            print("  ... and {} more".format(len(issues) - 20))

    print("\nValidation: {} unique papers, {} issues".format(len(filenames), len(issues)))
    return issues


def safe_yaml_value(value):
    """Sanitize a value for safe YAML insertion (replace double quotes with single)."""
    return str(value).replace('"', "'")


def insert_yaml_fields(fm_text, llm_assessed, data_url):
    """
    Insert LLM_assessed and DATA_URL fields after data_metrics in frontmatter.

    Uses safe regex insertion — NEVER parse/rebuild round-trip.
    """
    llm_safe = safe_yaml_value(llm_assessed)
    url_safe = safe_yaml_value(data_url)

    # Insert after data_metrics line
    new_fm, count = re.subn(
        r'^(data_metrics:.*?)$',
        r'\1\nLLM_assessed: "' + llm_safe + r'"\nDATA_URL: "' + url_safe + r'"',
        fm_text,
        count=1,
        flags=re.MULTILINE,
    )

    if count == 0:
        # Fallback: append to end of frontmatter if data_metrics not found
        new_fm = fm_text.rstrip() + '\nLLM_assessed: "{}"\nDATA_URL: "{}"'.format(
            llm_safe, url_safe)

    return new_fm


def insert_data_description(body, description_text):
    """
    Insert ## Data Description section into the paper body.

    Insertion strategy:
    1. After ## Dataset Information section (before next ## heading)
    2. If no ## Dataset Information, before ## Notes
    3. If no ## Notes, append before ## Citation Info
    4. Last resort: append to end
    """
    section = "\n## Data Description\n\n{}\n".format(description_text.strip())

    # Strategy 1: Insert after ## Dataset Information, before next ## heading
    pattern = r'(## Dataset Information\n(?:.*?\n)*?)(\n## )'
    match = re.search(pattern, body, re.DOTALL)
    if match:
        insert_pos = match.end(1)
        return body[:insert_pos] + section + body[insert_pos:]

    # Strategy 2: Before ## Notes
    pattern = r'\n(## Notes)'
    match = re.search(pattern, body)
    if match:
        insert_pos = match.start()
        return body[:insert_pos] + section + "\n" + body[insert_pos:]

    # Strategy 3: Before ## Citation Info
    pattern = r'\n(## Citation Info)'
    match = re.search(pattern, body)
    if match:
        insert_pos = match.start()
        return body[:insert_pos] + section + "\n" + body[insert_pos:]

    # Strategy 4: Append to end
    return body.rstrip() + "\n" + section + "\n"


def apply_to_paper(paper_path, entry, dry_run=False):
    """Apply LLM_assessed, DATA_URL, and Data Description to a single paper."""
    try:
        content = paper_path.read_text(encoding="utf-8")
        fm_text, body = extract_frontmatter(content)
    except (ValueError, UnicodeDecodeError) as e:
        return {"status": "error", "error": str(e)}

    # Check if already has LLM_assessed (idempotent)
    fields = parse_frontmatter(fm_text)
    if "LLM_assessed" in fields:
        return {"status": "skipped", "reason": "already has LLM_assessed"}

    # Insert YAML fields
    new_fm = insert_yaml_fields(fm_text, entry["LLM_assessed"], entry["DATA_URL"])

    # Validate YAML before writing
    is_valid, issues = validate_frontmatter(new_fm)
    if not is_valid:
        return {"status": "error", "error": "YAML validation failed: {}".format(issues)}

    # Insert body section (only if there's a description and no existing ## Data Description)
    new_body = body
    desc = entry.get("data_description", "")
    if desc and "## Data Description" not in body:
        new_body = insert_data_description(body, desc)

    if dry_run:
        return {"status": "dry_run", "would_update": True}

    # Write back
    reconstructed = "---\n{}\n---\n{}".format(new_fm.rstrip(), new_body)
    paper_path.write_text(reconstructed, encoding="utf-8")

    return {"status": "updated"}


def main():
    parser = argparse.ArgumentParser(description="Consolidate LLM assessment results")
    parser.add_argument("--manifest", type=str, default="",
                        help="Path to manifest JSON (default: most recent)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview mode: validate without writing")
    args = parser.parse_args()

    print("=== CONSOLIDATING LLM ASSESSMENT RESULTS ===\n")

    # Load manifest
    manifest, manifest_path = load_manifest(args.manifest or None)
    print("Date: {}, Batches: {}, Papers: {}".format(
        manifest["date"], manifest["num_batches"], manifest["total_papers"]))

    # Load all agent results
    print("\nLoading agent results:")
    all_results = load_agent_results(manifest)

    # Validate
    print()
    issues = validate_results(all_results, manifest)

    # Sort for consistent processing
    all_results.sort(key=lambda r: r["filename"])

    # Summary statistics
    llm_counts = Counter()
    has_llm = 0
    has_url = 0
    has_desc = 0

    for r in all_results:
        llm = r.get("LLM_assessed", "NA")
        if llm and llm != "NA":
            has_llm += 1
            for model in llm.split(","):
                llm_counts[model.strip()] += 1
        if r.get("DATA_URL", "NA") != "NA":
            has_url += 1
        if r.get("data_description", "") and r["data_description"] != "NA":
            has_desc += 1

    print("\n=== CONTENT SUMMARY ===")
    print("  Papers with LLM models: {} / {}".format(has_llm, len(all_results)))
    print("  Papers with data URL: {} / {}".format(has_url, len(all_results)))
    print("  Papers with description: {} / {}".format(has_desc, len(all_results)))

    if llm_counts:
        print("\n  Top 15 LLM models:")
        for model, count in llm_counts.most_common(15):
            print("    {}: {}".format(model, count))

    # Apply to papers
    print("\n=== APPLYING TO PAPERS{} ===".format(" (DRY RUN)" if args.dry_run else ""))
    log = []
    status_counts = Counter()

    for entry in all_results:
        paper_path = PAPERS_DIR / entry["filename"]
        if not paper_path.exists():
            print("  MISSING: {}".format(entry["filename"]))
            log.append({"filename": entry["filename"], "status": "missing"})
            status_counts["missing"] += 1
            continue

        result = apply_to_paper(paper_path, entry, dry_run=args.dry_run)
        status = result["status"]
        status_counts[status] += 1

        log.append({
            "filename": entry["filename"],
            "status": status,
            "LLM_assessed": entry.get("LLM_assessed", ""),
            "DATA_URL": entry.get("DATA_URL", ""),
            "has_description": bool(entry.get("data_description")),
        })

        if status == "error":
            print("  ERROR: {} — {}".format(entry["filename"], result.get("error", "")))

    print("\n=== RESULTS ===")
    for status, count in sorted(status_counts.items()):
        print("  {}: {}".format(status, count))

    # Write consolidation log
    consolidation = {
        "date": DATE_PREFIX,
        "manifest": manifest_path.name,
        "total_processed": len(all_results),
        "status_counts": dict(status_counts),
        "top_models": dict(llm_counts.most_common(30)),
        "papers_with_llm": has_llm,
        "papers_with_url": has_url,
        "papers_with_desc": has_desc,
        "entries": log,
    }

    if not args.dry_run:
        out_path = LOGS_DIR / "{}-llm_assessment_consolidation.json".format(DATE_PREFIX)
        tmp_path = out_path.parent / ".tmp.{}.json".format(os.getpid())
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(consolidation, f, indent=2, ensure_ascii=False)
        os.replace(str(tmp_path), str(out_path))
        print("\nConsolidation log: {}".format(out_path.name))
    else:
        print("\n(Dry run — no files modified)")

    print("\n=== DONE ===")


if __name__ == "__main__":
    main()
