#!/usr/bin/env python3
"""
Consolidate LLM-based moral psychology classification results and apply to papers.

Reads agent output JSON files, validates entries against allowed categories,
and applies moral_psychology YAML field updates via safe regex replacement.

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/consolidate_moral_psych.py --dry-run
    ../.venv/bin/python PYTHON/consolidate_moral_psych.py
    ../.venv/bin/python PYTHON/consolidate_moral_psych.py --manifest logs/20260312-moral_psych_manifest.json
    ../.venv/bin/python PYTHON/consolidate_moral_psych.py --confidence-threshold medium

Output:
    logs/YYYYMMDD-moral_psych_consolidation.json  — full audit log
    logs/YYYYMMDD-moral_psych_comparison.md       — human-readable before/after summary
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

# Allowed moral_psychology categories
ALLOWED_CATEGORIES = {
    "Moral Foundations Theory",
    "Dual Process Theory",
    "Dyadic Morality",
    "Social Intuitionist Model",
    "Moral Identity",
    "Cognitive Developmental",
    "Value Pluralism / Schwartz",
    "Trolley / Dilemmas (Psych)",
    "N/A",
}

CONFIDENCE_LEVELS = {"high": 3, "medium": 2, "low": 1}

REQUIRED_FIELDS = {"filename", "moral_psychology", "confidence", "reasoning"}

# Normalize common agent output variations to canonical category names
CATEGORY_ALIASES = {
    "Dual Process Theory (Moral Cognition)": "Dual Process Theory",
    "Social Intuitionist": "Social Intuitionist Model",
    "Trolley / Dilemmas": "Trolley / Dilemmas (Psych)",
    "Trolley/Dilemmas (Psych)": "Trolley / Dilemmas (Psych)",
    "Value Pluralism/Schwartz": "Value Pluralism / Schwartz",
    "Schwartz": "Value Pluralism / Schwartz",
    "Kohlberg": "Cognitive Developmental",
}


def normalize_moral_psychology(value):
    """Normalize moral_psychology value to canonical category names."""
    if not value or value == "N/A":
        return value
    categories = [c.strip() for c in value.split(",")]
    normalized = []
    for cat in categories:
        canonical = CATEGORY_ALIASES.get(cat, cat)
        if canonical not in normalized:
            normalized.append(canonical)
    return ", ".join(normalized)


def load_manifest(manifest_path=None):
    """Load manifest to find agent result files."""
    if manifest_path:
        mpath = Path(manifest_path)
    else:
        manifests = sorted(LOGS_DIR.glob("*-moral_psych_manifest.json"), reverse=True)
        if not manifests:
            print("ERROR: No manifest file found. Run generate_moral_psych_batches.py first.")
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
    missing_batches = []

    for i in range(1, num_batches + 1):
        result_name = "{}-moral_psych_agent_{:02d}.json".format(date, i)
        result_path = LOGS_DIR / result_name
        if not result_path.exists():
            missing_batches.append(result_name)
            continue

        with open(result_path, "r", encoding="utf-8") as f:
            results = json.load(f)

        # Validate required fields and normalize categories
        for entry in results:
            missing = REQUIRED_FIELDS - set(entry.keys())
            if missing:
                print("WARN: Agent {:02d}, paper '{}': missing fields {}".format(
                    i, entry.get("filename", "?"), missing))
            # Normalize category names to canonical forms
            if "moral_psychology" in entry:
                entry["moral_psychology"] = normalize_moral_psychology(
                    entry["moral_psychology"])

        all_results.extend(results)
        print("  Agent {:02d}: {} papers loaded".format(i, len(results)))

    if missing_batches:
        print("\nWARNING: {} missing agent result files:".format(len(missing_batches)))
        for mb in missing_batches:
            print("  {}".format(mb))

    return all_results


def validate_categories(value):
    """Validate that a moral_psychology value contains only allowed categories."""
    if not value or value == "N/A":
        return True, []

    issues = []
    categories = [c.strip() for c in value.split(",")]
    for cat in categories:
        if cat not in ALLOWED_CATEGORIES:
            issues.append("Unknown category: '{}'".format(cat))
    return len(issues) == 0, issues


def validate_results(all_results):
    """Validate completeness and quality of results."""
    # Check for duplicates
    filenames = [r["filename"] for r in all_results]
    counts = Counter(filenames)
    duplicates = {f: c for f, c in counts.items() if c > 1}
    if duplicates:
        print("WARNING: Duplicate filenames (will use last occurrence):")
        for f, c in duplicates.items():
            print("  {} (appears {} times)".format(f, c))

    # Validate category names
    issues = []
    for r in all_results:
        mp = r.get("moral_psychology", "")
        valid, cat_issues = validate_categories(mp)
        if not valid:
            for ci in cat_issues:
                issues.append("{}: {}".format(r["filename"], ci))

        conf = r.get("confidence", "")
        if conf not in CONFIDENCE_LEVELS:
            issues.append("{}: Invalid confidence '{}'".format(r["filename"], conf))

    if issues:
        print("\nVALIDATION ISSUES ({} issues):".format(len(issues)))
        for issue in issues[:30]:
            print("  {}".format(issue))
        if len(issues) > 30:
            print("  ... and {} more".format(len(issues) - 30))

    print("\nValidation: {} unique papers, {} issues".format(
        len(set(filenames)), len(issues)))
    return issues


def apply_to_paper(paper_path, entry, dry_run=False):
    """
    Apply moral_psychology reclassification to a single paper.

    Uses safe regex replacement — NEVER parse→rebuild round-trip.
    """
    try:
        content = paper_path.read_text(encoding="utf-8")
        fm_text, body = extract_frontmatter(content)
    except (ValueError, UnicodeDecodeError) as e:
        return {"status": "error", "error": str(e)}

    # Get current value for audit
    fields = parse_frontmatter(fm_text)
    old_value = fields.get("moral_psychology", "").strip("\"'")

    new_value = entry["moral_psychology"].strip()

    # Safe YAML value (replace internal double quotes with single)
    new_value_safe = new_value.replace('"', "'")

    # Replace moral_psychology field via regex (safe — no parse→rebuild)
    new_fm, count = re.subn(
        r'^moral_psychology:.*$',
        'moral_psychology: "{}"'.format(new_value_safe),
        fm_text,
        count=1,
        flags=re.MULTILINE,
    )

    if count == 0:
        # Field doesn't exist — append after religious_values or at end
        new_fm, count = re.subn(
            r'^(religious_values_list:.*?)$',
            r'\1\nmoral_psychology: "{}"'.format(new_value_safe),
            fm_text,
            count=1,
            flags=re.MULTILINE,
        )
        if count == 0:
            # Last resort: append to end of frontmatter
            new_fm = fm_text.rstrip() + '\nmoral_psychology: "{}"'.format(new_value_safe)

    # Validate YAML before writing
    is_valid, yaml_issues = validate_frontmatter(new_fm)
    if not is_valid:
        return {"status": "error",
                "error": "YAML validation failed: {}".format(yaml_issues)}

    if dry_run:
        changed = old_value != new_value
        return {"status": "dry_run", "would_change": changed,
                "old_value": old_value, "new_value": new_value}

    # Atomic write: PID-scoped temp file + os.replace()
    reconstructed = "---\n{}\n---\n{}".format(new_fm.rstrip(), body)
    tmp_path = paper_path.parent / ".tmp.{}.{}".format(os.getpid(), paper_path.name)
    tmp_path.write_text(reconstructed, encoding="utf-8")
    os.replace(str(tmp_path), str(paper_path))

    return {"status": "updated", "old_value": old_value, "new_value": new_value}


def generate_comparison_report(log_entries, output_path):
    """Generate a human-readable before/after comparison report."""
    lines = [
        "# Moral Psychology Reclassification — Comparison Report",
        "",
        "Generated: {}".format(datetime.now().strftime("%Y-%m-%d %H:%M")),
        "",
    ]

    # Summary statistics
    changed = [e for e in log_entries if e.get("old_value") != e.get("new_value")
               and e["status"] in ("updated", "dry_run")]
    unchanged = [e for e in log_entries if e.get("old_value") == e.get("new_value")
                 and e["status"] in ("updated", "dry_run")]

    lines.append("## Summary")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("|--------|-------|")
    lines.append("| Total processed | {} |".format(len(log_entries)))
    lines.append("| Changed | {} |".format(len(changed)))
    lines.append("| Unchanged | {} |".format(len(unchanged)))
    lines.append("| Errors | {} |".format(
        sum(1 for e in log_entries if e["status"] == "error")))
    lines.append("")

    # Distribution comparison
    old_dist = Counter()
    new_dist = Counter()
    for e in log_entries:
        if "old_value" in e:
            old_val = e["old_value"] or "(empty)"
            old_dist[old_val] += 1
        if "new_value" in e:
            new_val = e["new_value"] or "(empty)"
            new_dist[new_val] += 1

    all_cats = sorted(set(old_dist.keys()) | set(new_dist.keys()))

    lines.append("## Distribution Comparison")
    lines.append("")
    lines.append("| Category | Before | After | Delta |")
    lines.append("|----------|--------|-------|-------|")
    for cat in all_cats:
        before = old_dist.get(cat, 0)
        after = new_dist.get(cat, 0)
        delta = after - before
        delta_str = "+{}".format(delta) if delta > 0 else str(delta)
        lines.append("| {} | {} | {} | {} |".format(cat, before, after, delta_str))
    lines.append("")

    # Papers that lost tags (had a theory, now N/A)
    lost = [e for e in changed
            if e.get("old_value") and e["old_value"] != "N/A"
            and e.get("new_value") == "N/A"]
    if lost:
        lines.append("## Papers That Lost Tags ({})".format(len(lost)))
        lines.append("")
        for e in sorted(lost, key=lambda x: x["filename"]):
            lines.append("- **{}**: {} -> N/A".format(
                e["filename"], e["old_value"]))
            if e.get("reasoning"):
                lines.append("  - Reason: {}".format(e["reasoning"]))
        lines.append("")

    # Papers that gained tags (was N/A, now has theory)
    gained = [e for e in changed
              if (not e.get("old_value") or e["old_value"] == "N/A")
              and e.get("new_value") and e["new_value"] != "N/A"]
    if gained:
        lines.append("## Papers That Gained Tags ({})".format(len(gained)))
        lines.append("")
        for e in sorted(gained, key=lambda x: x["filename"]):
            lines.append("- **{}**: N/A -> {}".format(
                e["filename"], e["new_value"]))
            if e.get("reasoning"):
                lines.append("  - Reason: {}".format(e["reasoning"]))
        lines.append("")

    # Papers that changed tags
    tag_changed = [e for e in changed
                   if e.get("old_value") and e["old_value"] != "N/A"
                   and e.get("new_value") and e["new_value"] != "N/A"
                   and e["old_value"] != e["new_value"]]
    if tag_changed:
        lines.append("## Papers With Changed Tags ({})".format(len(tag_changed)))
        lines.append("")
        for e in sorted(tag_changed, key=lambda x: x["filename"]):
            lines.append("- **{}**: {} -> {}".format(
                e["filename"], e["old_value"], e["new_value"]))
            if e.get("reasoning"):
                lines.append("  - Reason: {}".format(e["reasoning"]))
        lines.append("")

    # Low-confidence classifications
    low_conf = [e for e in log_entries if e.get("confidence") == "low"]
    if low_conf:
        lines.append("## Low-Confidence Classifications ({})".format(len(low_conf)))
        lines.append("")
        for e in sorted(low_conf, key=lambda x: x["filename"]):
            lines.append("- **{}**: {} (was: {})".format(
                e["filename"], e.get("new_value", "?"), e.get("old_value", "?")))
            if e.get("reasoning"):
                lines.append("  - Reason: {}".format(e["reasoning"]))
        lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Consolidate moral psychology reclassification results")
    parser.add_argument("--manifest", type=str, default="",
                        help="Path to manifest JSON (default: most recent)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview mode: validate without writing")
    parser.add_argument("--confidence-threshold", type=str, default="",
                        choices=["", "low", "medium", "high"],
                        help="Only apply results at or above this confidence "
                             "(default: apply all)")
    args = parser.parse_args()

    conf_threshold = CONFIDENCE_LEVELS.get(args.confidence_threshold, 0)

    print("=== CONSOLIDATING MORAL PSYCHOLOGY RESULTS ===\n")

    # Load manifest
    manifest, manifest_path = load_manifest(args.manifest or None)
    print("Date: {}, Batches: {}, Papers: {}".format(
        manifest["date"], manifest["num_batches"], manifest["total_papers"]))

    # Load all agent results
    print("\nLoading agent results:")
    all_results = load_agent_results(manifest)

    if not all_results:
        print("\nERROR: No agent results loaded. Exiting.")
        sys.exit(1)

    # Validate
    print()
    issues = validate_results(all_results)

    # De-duplicate: keep last occurrence (later agents may have re-processed)
    seen = {}
    for r in all_results:
        seen[r["filename"]] = r
    all_results = list(seen.values())

    # Sort for consistent processing
    all_results.sort(key=lambda r: r["filename"])

    # Summary statistics
    mp_counts = Counter()
    conf_counts = Counter()
    for r in all_results:
        mp = r.get("moral_psychology", "N/A")
        if mp and mp != "N/A":
            for cat in mp.split(","):
                mp_counts[cat.strip()] += 1
        else:
            mp_counts["N/A"] += 1
        conf_counts[r.get("confidence", "unknown")] += 1

    print("\n=== CLASSIFICATION SUMMARY ===")
    print("  Total papers: {}".format(len(all_results)))
    print("\n  Category distribution (new):")
    for cat, count in sorted(mp_counts.items(), key=lambda x: -x[1]):
        print("    {}: {}".format(cat, count))
    print("\n  Confidence distribution:")
    for conf, count in sorted(conf_counts.items(), key=lambda x: -x[1]):
        print("    {}: {}".format(conf, count))

    # Apply to papers
    mode_label = " (DRY RUN)" if args.dry_run else ""
    if conf_threshold > 0:
        mode_label += " (threshold: {})".format(args.confidence_threshold)
    print("\n=== APPLYING TO PAPERS{} ===".format(mode_label))

    log = []
    status_counts = Counter()
    skipped_confidence = 0

    for entry in all_results:
        # Apply confidence threshold
        entry_conf = CONFIDENCE_LEVELS.get(entry.get("confidence", ""), 0)
        if conf_threshold > 0 and entry_conf < conf_threshold:
            skipped_confidence += 1
            log.append({
                "filename": entry["filename"],
                "status": "skipped_confidence",
                "confidence": entry.get("confidence", ""),
                "moral_psychology": entry.get("moral_psychology", ""),
            })
            status_counts["skipped_confidence"] += 1
            continue

        paper_path = PAPERS_DIR / entry["filename"]
        if not paper_path.exists():
            print("  MISSING: {}".format(entry["filename"]))
            log.append({"filename": entry["filename"], "status": "missing"})
            status_counts["missing"] += 1
            continue

        result = apply_to_paper(paper_path, entry, dry_run=args.dry_run)
        status = result["status"]
        status_counts[status] += 1

        log_entry = {
            "filename": entry["filename"],
            "status": status,
            "old_value": result.get("old_value", ""),
            "new_value": entry.get("moral_psychology", ""),
            "confidence": entry.get("confidence", ""),
            "reasoning": entry.get("reasoning", ""),
        }
        log.append(log_entry)

        if status == "error":
            print("  ERROR: {} — {}".format(entry["filename"], result.get("error", "")))

    if skipped_confidence > 0:
        print("\n  Skipped (below confidence threshold): {}".format(skipped_confidence))

    print("\n=== RESULTS ===")
    for status, count in sorted(status_counts.items()):
        print("  {}: {}".format(status, count))

    # Write consolidation log
    consolidation = {
        "date": DATE_PREFIX,
        "manifest": manifest_path.name,
        "total_processed": len(all_results),
        "confidence_threshold": args.confidence_threshold or "none",
        "dry_run": args.dry_run,
        "status_counts": dict(status_counts),
        "new_category_distribution": dict(mp_counts),
        "confidence_distribution": dict(conf_counts),
        "entries": log,
    }

    out_path = LOGS_DIR / "{}-moral_psych_consolidation.json".format(DATE_PREFIX)
    tmp_path = out_path.parent / ".tmp.{}.json".format(os.getpid())
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(consolidation, f, indent=2, ensure_ascii=False)
    os.replace(str(tmp_path), str(out_path))
    print("\nConsolidation log: {}".format(out_path.name))

    # Generate comparison report
    comparison_path = LOGS_DIR / "{}-moral_psych_comparison.md".format(DATE_PREFIX)
    generate_comparison_report(log, comparison_path)
    print("Comparison report: {}".format(comparison_path.name))

    if args.dry_run:
        print("\n(Dry run — no paper files modified)")

    print("\n=== DONE ===")


if __name__ == "__main__":
    main()
