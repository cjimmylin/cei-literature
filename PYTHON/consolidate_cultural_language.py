#!/usr/bin/env python3
"""
Consolidate LLM-based cultural & language classification results and apply to papers.

Reads agent output JSON files, validates entries against allowed cultural categories,
and applies national_ethnic_cultural, cultures_nationalities_list, and languages_list
YAML field updates via safe regex replacement.

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/consolidate_cultural_language.py --dry-run
    ../.venv/bin/python PYTHON/consolidate_cultural_language.py
    ../.venv/bin/python PYTHON/consolidate_cultural_language.py --manifest logs/20260312-cultural_language_manifest.json
    ../.venv/bin/python PYTHON/consolidate_cultural_language.py --confidence-threshold medium
    ../.venv/bin/python PYTHON/consolidate_cultural_language.py --fields cultural
    ../.venv/bin/python PYTHON/consolidate_cultural_language.py --fields language

Output:
    logs/YYYYMMDD-cultural_language_consolidation.json  — full audit log
    logs/YYYYMMDD-cultural_language_comparison.md       — human-readable before/after summary
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

# Allowed cultural categories (24 total: 22 specific + 2 meta)
ALLOWED_CULTURES = {
    # East Asian
    "Chinese", "Japanese", "Korean",
    # South/Southeast Asian
    "Indian", "Indonesian", "Filipino", "Thai", "Vietnamese",
    # Middle Eastern
    "Arabic", "Iranian",
    # African
    "African/Ubuntu",
    # European
    "French", "German", "Italian", "Spanish", "Dutch", "Russian",
    # Americas
    "American", "Brazilian", "Latin American",
    # Other
    "Hebrew/Israeli", "Australian/Aboriginal", "Singaporean",
    # Meta
    "Western", "Multicultural/Cross-cultural",
    # N/A
    "N/A",
}

# Normalize common agent output variations to canonical names
CULTURAL_ALIASES = {
    "China": "Chinese",
    "Japan": "Japanese",
    "Korea": "Korean",
    "South Korea": "Korean",
    "Indonesia": "Indonesian",
    "India": "Indian",
    "Philippines": "Filipino",
    "Philippine": "Filipino",
    "Thailand": "Thai",
    "Vietnam": "Vietnamese",
    "Arab": "Arabic",
    "Iran": "Iranian",
    "Persia": "Iranian",
    "Persian": "Iranian",
    "Africa": "African/Ubuntu",
    "African": "African/Ubuntu",
    "Ubuntu": "African/Ubuntu",
    "France": "French",
    "Germany": "German",
    "Italy": "Italian",
    "Spain": "Spanish",
    "Netherlands": "Dutch",
    "Russia": "Russian",
    "United States": "American",
    "US": "American",
    "U.S.": "American",
    "USA": "American",
    "Brazil": "Brazilian",
    "Israel": "Hebrew/Israeli",
    "Israeli": "Hebrew/Israeli",
    "Hebrew": "Hebrew/Israeli",
    "Aboriginal": "Australian/Aboriginal",
    "Australian": "Australian/Aboriginal",
    "Australia": "Australian/Aboriginal",
    "Singapore": "Singaporean",
    "Cross-cultural": "Multicultural/Cross-cultural",
    "Multicultural": "Multicultural/Cross-cultural",
    "Cross-Cultural": "Multicultural/Cross-cultural",
    "Multi-cultural": "Multicultural/Cross-cultural",
    "Latin America": "Latin American",
    "none": "N/A",
    "None": "N/A",
    "n/a": "N/A",
}

CONFIDENCE_LEVELS = {"high": 3, "medium": 2, "low": 1}

REQUIRED_FIELDS = {
    "filename", "national_ethnic_cultural", "cultures_nationalities_list",
    "languages_list", "confidence", "reasoning",
}


def normalize_cultural_value(value):
    """Normalize a cultural/national field value to canonical category names."""
    if not value or value == "N/A":
        return value or "N/A"

    categories = [c.strip() for c in value.split(",")]
    normalized = []
    for cat in categories:
        canonical = CULTURAL_ALIASES.get(cat, cat)
        if canonical not in normalized:
            normalized.append(canonical)
    return ", ".join(normalized)


def load_manifest(manifest_path=None):
    """Load manifest to find agent result files."""
    if manifest_path:
        mpath = Path(manifest_path)
    else:
        manifests = sorted(
            LOGS_DIR.glob("*-cultural_language_manifest.json"), reverse=True)
        if not manifests:
            print("ERROR: No manifest file found. "
                  "Run generate_cultural_language_batches.py first.")
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
        result_name = "{}-cultural_language_agent_{:02d}.json".format(date, i)
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

            # Normalize cultural category names
            if "national_ethnic_cultural" in entry:
                entry["national_ethnic_cultural"] = normalize_cultural_value(
                    entry["national_ethnic_cultural"])
            if "cultures_nationalities_list" in entry:
                entry["cultures_nationalities_list"] = normalize_cultural_value(
                    entry["cultures_nationalities_list"])

            # Enforce parallel field sync: cultures_nationalities_list must
            # match national_ethnic_cultural
            nec = entry.get("national_ethnic_cultural", "N/A")
            cnl = entry.get("cultures_nationalities_list", "N/A")
            if nec != cnl:
                print("WARN: Agent {:02d}, paper '{}': "
                      "parallel field mismatch — forcing sync "
                      "(nec='{}', cnl='{}')".format(
                          i, entry.get("filename", "?"), nec, cnl))
                entry["cultures_nationalities_list"] = nec

        all_results.extend(results)
        print("  Agent {:02d}: {} papers loaded".format(i, len(results)))

    if missing_batches:
        print("\nWARNING: {} missing agent result files:".format(
            len(missing_batches)))
        for mb in missing_batches:
            print("  {}".format(mb))

    return all_results


def validate_cultural_categories(value):
    """Validate that a cultural value contains only allowed categories."""
    if not value or value == "N/A":
        return True, []

    issues = []
    categories = [c.strip() for c in value.split(",")]
    for cat in categories:
        if cat not in ALLOWED_CULTURES:
            issues.append("Unknown culture: '{}'".format(cat))
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

    # Validate cultural categories and confidence
    issues = []
    for r in all_results:
        nec = r.get("national_ethnic_cultural", "")
        valid, cat_issues = validate_cultural_categories(nec)
        if not valid:
            for ci in cat_issues:
                issues.append("{}: {}".format(r["filename"], ci))

        # Validate parallel fields match
        cnl = r.get("cultures_nationalities_list", "")
        if nec != cnl:
            issues.append("{}: parallel field mismatch: nec='{}' != cnl='{}'".format(
                r["filename"], nec, cnl))

        conf = r.get("confidence", "")
        if conf not in CONFIDENCE_LEVELS:
            issues.append("{}: Invalid confidence '{}'".format(
                r["filename"], conf))

    if issues:
        print("\nVALIDATION ISSUES ({} issues):".format(len(issues)))
        for issue in issues[:30]:
            print("  {}".format(issue))
        if len(issues) > 30:
            print("  ... and {} more".format(len(issues) - 30))

    print("\nValidation: {} unique papers, {} issues".format(
        len(set(filenames)), len(issues)))
    return issues


def apply_to_paper(paper_path, entry, dry_run=False, update_fields=None):
    """
    Apply cultural/language reclassification to a single paper.

    Uses safe regex replacement — NEVER parse->rebuild round-trip.

    Args:
        paper_path: Path to the paper file
        entry: Dict with new field values
        dry_run: If True, preview without writing
        update_fields: Set of field groups to update ('cultural', 'language').
                       None means update all.
    """
    if update_fields is None:
        update_fields = {"cultural", "language"}

    try:
        content = paper_path.read_text(encoding="utf-8")
        fm_text, body = extract_frontmatter(content)
    except (ValueError, UnicodeDecodeError) as e:
        return {"status": "error", "error": str(e)}

    # Get current values for audit
    fields = parse_frontmatter(fm_text)
    old_nec = fields.get("national_ethnic_cultural", "").strip("\"'")
    old_cnl = fields.get("cultures_nationalities_list", "").strip("\"'")
    old_lang = fields.get("languages_list", "").strip("\"'")

    new_nec = entry.get("national_ethnic_cultural", "N/A").strip()
    new_cnl = entry.get("cultures_nationalities_list", "N/A").strip()
    new_lang = entry.get("languages_list", "").strip()

    # Safe YAML value (replace internal double quotes with single)
    new_nec_safe = new_nec.replace('"', "'")
    new_cnl_safe = new_cnl.replace('"', "'")
    new_lang_safe = new_lang.replace('"', "'")

    new_fm = fm_text

    # Update cultural fields
    if "cultural" in update_fields:
        # Update national_ethnic_cultural
        new_fm, count = re.subn(
            r'^national_ethnic_cultural:.*$',
            'national_ethnic_cultural: "{}"'.format(new_nec_safe),
            new_fm, count=1, flags=re.MULTILINE)
        if count == 0:
            # Field doesn't exist — append after languages_list or at end
            new_fm, count = re.subn(
                r'^(languages_list:.*?)$',
                r'\1\nnational_ethnic_cultural: "{}"'.format(new_nec_safe),
                new_fm, count=1, flags=re.MULTILINE)

        # Update cultures_nationalities_list
        new_fm, count = re.subn(
            r'^cultures_nationalities_list:.*$',
            'cultures_nationalities_list: "{}"'.format(new_cnl_safe),
            new_fm, count=1, flags=re.MULTILINE)
        if count == 0:
            new_fm, count = re.subn(
                r'^(national_ethnic_cultural:.*?)$',
                r'\1\ncultures_nationalities_list: "{}"'.format(new_cnl_safe),
                new_fm, count=1, flags=re.MULTILINE)

    # Update language field
    if "language" in update_fields:
        new_fm, count = re.subn(
            r'^languages_list:.*$',
            'languages_list: "{}"'.format(new_lang_safe),
            new_fm, count=1, flags=re.MULTILINE)
        if count == 0:
            # Append after cultures_nationalities_list or national_ethnic_cultural
            new_fm, count = re.subn(
                r'^(cultures_nationalities_list:.*?)$',
                r'\1\nlanguages_list: "{}"'.format(new_lang_safe),
                new_fm, count=1, flags=re.MULTILINE)

    # Validate YAML before writing
    is_valid, yaml_issues = validate_frontmatter(new_fm)
    if not is_valid:
        return {"status": "error",
                "error": "YAML validation failed: {}".format(yaml_issues)}

    result = {
        "old_national_ethnic_cultural": old_nec,
        "old_cultures_nationalities_list": old_cnl,
        "old_languages_list": old_lang,
        "new_national_ethnic_cultural": new_nec,
        "new_cultures_nationalities_list": new_cnl,
        "new_languages_list": new_lang,
    }

    if dry_run:
        changed = (old_nec != new_nec or old_cnl != new_cnl
                   or old_lang != new_lang)
        result["status"] = "dry_run"
        result["would_change"] = changed
        return result

    # Atomic write: PID-scoped temp file + os.replace()
    reconstructed = "---\n{}\n---\n{}".format(new_fm.rstrip(), body)
    tmp_path = paper_path.parent / ".tmp.{}.{}".format(
        os.getpid(), paper_path.name)
    tmp_path.write_text(reconstructed, encoding="utf-8")
    os.replace(str(tmp_path), str(paper_path))

    result["status"] = "updated"
    return result


def generate_comparison_report(log_entries, output_path):
    """Generate a human-readable before/after comparison report."""
    lines = [
        "# Cultural & Language Reclassification — Comparison Report",
        "",
        "Generated: {}".format(datetime.now().strftime("%Y-%m-%d %H:%M")),
        "",
    ]

    # Summary statistics
    changed = [e for e in log_entries
               if e["status"] in ("updated", "dry_run")
               and (e.get("old_national_ethnic_cultural") !=
                    e.get("new_national_ethnic_cultural")
                    or e.get("old_languages_list") !=
                    e.get("new_languages_list"))]
    unchanged = [e for e in log_entries
                 if e["status"] in ("updated", "dry_run")
                 and e.get("old_national_ethnic_cultural") ==
                 e.get("new_national_ethnic_cultural")
                 and e.get("old_languages_list") ==
                 e.get("new_languages_list")]

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

    # Cultural distribution comparison
    old_cult = Counter()
    new_cult = Counter()
    old_lang = Counter()
    new_lang = Counter()
    for e in log_entries:
        ov = e.get("old_national_ethnic_cultural", "") or "(empty)"
        old_cult[ov] += 1
        nv = e.get("new_national_ethnic_cultural", "") or "(empty)"
        new_cult[nv] += 1
        ol = e.get("old_languages_list", "") or "(empty)"
        old_lang[ol] += 1
        nl = e.get("new_languages_list", "") or "(empty)"
        new_lang[nl] += 1

    all_cult_cats = sorted(set(old_cult.keys()) | set(new_cult.keys()))
    lines.append("## Cultural Distribution Comparison")
    lines.append("")
    lines.append("| Category | Before | After | Delta |")
    lines.append("|----------|--------|-------|-------|")
    for cat in all_cult_cats:
        before = old_cult.get(cat, 0)
        after = new_cult.get(cat, 0)
        delta = after - before
        delta_str = "+{}".format(delta) if delta > 0 else str(delta)
        lines.append("| {} | {} | {} | {} |".format(cat, before, after, delta_str))
    lines.append("")

    # Language distribution comparison (top 30)
    all_lang_cats = sorted(set(old_lang.keys()) | set(new_lang.keys()),
                           key=lambda x: -(new_lang.get(x, 0)))
    lines.append("## Language Distribution Comparison (top 30)")
    lines.append("")
    lines.append("| Language | Before | After | Delta |")
    lines.append("|----------|--------|-------|-------|")
    for i, lang in enumerate(all_lang_cats):
        if i >= 30:
            break
        before = old_lang.get(lang, 0)
        after = new_lang.get(lang, 0)
        delta = after - before
        delta_str = "+{}".format(delta) if delta > 0 else str(delta)
        lines.append("| {} | {} | {} | {} |".format(lang, before, after, delta_str))
    lines.append("")

    # Papers that lost cultural tags
    lost = [e for e in changed
            if e.get("old_national_ethnic_cultural")
            and e["old_national_ethnic_cultural"] != "N/A"
            and (not e.get("new_national_ethnic_cultural")
                 or e["new_national_ethnic_cultural"] == "N/A")]
    if lost:
        lines.append("## Papers That Lost Cultural Tags ({})".format(len(lost)))
        lines.append("")
        for e in sorted(lost, key=lambda x: x["filename"]):
            lines.append("- **{}**: {} -> N/A".format(
                e["filename"], e["old_national_ethnic_cultural"]))
            if e.get("reasoning"):
                lines.append("  - Reason: {}".format(e["reasoning"]))
        lines.append("")

    # Papers that gained cultural tags
    gained = [e for e in changed
              if (not e.get("old_national_ethnic_cultural")
                  or e["old_national_ethnic_cultural"] == "N/A")
              and e.get("new_national_ethnic_cultural")
              and e["new_national_ethnic_cultural"] != "N/A"]
    if gained:
        lines.append("## Papers That Gained Cultural Tags ({})".format(len(gained)))
        lines.append("")
        for e in sorted(gained, key=lambda x: x["filename"]):
            lines.append("- **{}**: N/A -> {}".format(
                e["filename"], e["new_national_ethnic_cultural"]))
            if e.get("reasoning"):
                lines.append("  - Reason: {}".format(e["reasoning"]))
        lines.append("")

    # Papers with changed cultural tags (had one, now different)
    tag_changed = [e for e in changed
                   if e.get("old_national_ethnic_cultural")
                   and e["old_national_ethnic_cultural"] != "N/A"
                   and e.get("new_national_ethnic_cultural")
                   and e["new_national_ethnic_cultural"] != "N/A"
                   and e["old_national_ethnic_cultural"] !=
                   e["new_national_ethnic_cultural"]]
    if tag_changed:
        lines.append("## Papers With Changed Cultural Tags ({})".format(
            len(tag_changed)))
        lines.append("")
        for e in sorted(tag_changed, key=lambda x: x["filename"]):
            lines.append("- **{}**: {} -> {}".format(
                e["filename"],
                e["old_national_ethnic_cultural"],
                e["new_national_ethnic_cultural"]))
            if e.get("reasoning"):
                lines.append("  - Reason: {}".format(e["reasoning"]))
        lines.append("")

    # Papers that gained/changed language tags
    lang_changed = [e for e in changed
                    if e.get("old_languages_list", "") !=
                    e.get("new_languages_list", "")]
    if lang_changed:
        lines.append("## Papers With Language Changes ({})".format(
            len(lang_changed)))
        lines.append("")
        for e in sorted(lang_changed, key=lambda x: x["filename"]):
            old_l = e.get("old_languages_list", "") or "(empty)"
            new_l = e.get("new_languages_list", "") or "(empty)"
            lines.append("- **{}**: {} -> {}".format(
                e["filename"], old_l, new_l))
        lines.append("")

    # Low-confidence classifications
    low_conf = [e for e in log_entries if e.get("confidence") == "low"]
    if low_conf:
        lines.append("## Low-Confidence Classifications ({})".format(
            len(low_conf)))
        lines.append("")
        for e in sorted(low_conf, key=lambda x: x["filename"]):
            lines.append("- **{}**: {} / lang={}".format(
                e["filename"],
                e.get("new_national_ethnic_cultural", "?"),
                e.get("new_languages_list", "?")))
            if e.get("reasoning"):
                lines.append("  - Reason: {}".format(e["reasoning"]))
        lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Consolidate cultural & language reclassification results")
    parser.add_argument("--manifest", type=str, default="",
                        help="Path to manifest JSON (default: most recent)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview mode: validate without writing")
    parser.add_argument("--confidence-threshold", type=str, default="",
                        choices=["", "low", "medium", "high"],
                        help="Only apply results at or above this confidence "
                             "(default: apply all)")
    parser.add_argument("--fields", type=str, default="cultural,language",
                        help="Comma-separated field groups to update: "
                             "'cultural' (nec+cnl), 'language' (languages_list), "
                             "or both (default: cultural,language)")
    args = parser.parse_args()

    conf_threshold = CONFIDENCE_LEVELS.get(args.confidence_threshold, 0)
    update_fields = set(f.strip() for f in args.fields.split(","))
    valid_field_groups = {"cultural", "language"}
    invalid = update_fields - valid_field_groups
    if invalid:
        print("ERROR: Invalid field groups: {}. Use 'cultural' and/or 'language'.".format(
            invalid))
        sys.exit(1)

    print("=== CONSOLIDATING CULTURAL & LANGUAGE RESULTS ===\n")
    print("Update fields: {}".format(", ".join(sorted(update_fields))))

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
    nec_counts = Counter()
    lang_counts = Counter()
    conf_counts = Counter()
    for r in all_results:
        nec = r.get("national_ethnic_cultural", "N/A")
        if nec and nec != "N/A":
            for cat in nec.split(","):
                nec_counts[cat.strip()] += 1
        else:
            nec_counts["N/A"] += 1

        lang = r.get("languages_list", "")
        lang_key = lang if lang else "(empty)"
        lang_counts[lang_key] += 1

        conf_counts[r.get("confidence", "unknown")] += 1

    print("\n=== CLASSIFICATION SUMMARY ===")
    print("  Total papers: {}".format(len(all_results)))
    print("\n  Cultural category distribution (new):")
    for cat, count in sorted(nec_counts.items(), key=lambda x: -x[1]):
        print("    {}: {}".format(cat, count))
    print("\n  Language distribution (new, top 15):")
    for i, (lang, count) in enumerate(
            sorted(lang_counts.items(), key=lambda x: -x[1])):
        if i >= 15:
            print("    ... and {} more".format(len(lang_counts) - 15))
            break
        print("    {}: {}".format(lang, count))
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
                "national_ethnic_cultural": entry.get(
                    "national_ethnic_cultural", ""),
                "languages_list": entry.get("languages_list", ""),
            })
            status_counts["skipped_confidence"] += 1
            continue

        paper_path = PAPERS_DIR / entry["filename"]
        if not paper_path.exists():
            print("  MISSING: {}".format(entry["filename"]))
            log.append({"filename": entry["filename"], "status": "missing"})
            status_counts["missing"] += 1
            continue

        result = apply_to_paper(paper_path, entry,
                                dry_run=args.dry_run,
                                update_fields=update_fields)
        status = result["status"]
        status_counts[status] += 1

        log_entry = {
            "filename": entry["filename"],
            "status": status,
            "old_national_ethnic_cultural": result.get(
                "old_national_ethnic_cultural", ""),
            "old_cultures_nationalities_list": result.get(
                "old_cultures_nationalities_list", ""),
            "old_languages_list": result.get("old_languages_list", ""),
            "new_national_ethnic_cultural": entry.get(
                "national_ethnic_cultural", ""),
            "new_cultures_nationalities_list": entry.get(
                "cultures_nationalities_list", ""),
            "new_languages_list": entry.get("languages_list", ""),
            "confidence": entry.get("confidence", ""),
            "reasoning": entry.get("reasoning", ""),
        }
        log.append(log_entry)

        if status == "error":
            print("  ERROR: {} — {}".format(
                entry["filename"], result.get("error", "")))

    if skipped_confidence > 0:
        print("\n  Skipped (below confidence threshold): {}".format(
            skipped_confidence))

    print("\n=== RESULTS ===")
    for status, count in sorted(status_counts.items()):
        print("  {}: {}".format(status, count))

    # Write consolidation log
    consolidation = {
        "date": DATE_PREFIX,
        "manifest": manifest_path.name,
        "total_processed": len(all_results),
        "confidence_threshold": args.confidence_threshold or "none",
        "update_fields": sorted(update_fields),
        "dry_run": args.dry_run,
        "status_counts": dict(status_counts),
        "new_cultural_distribution": dict(nec_counts),
        "new_language_distribution": dict(lang_counts),
        "confidence_distribution": dict(conf_counts),
        "entries": log,
    }

    out_path = LOGS_DIR / "{}-cultural_language_consolidation.json".format(
        DATE_PREFIX)
    tmp_path = out_path.parent / ".tmp.{}.json".format(os.getpid())
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(consolidation, f, indent=2, ensure_ascii=False)
    os.replace(str(tmp_path), str(out_path))
    print("\nConsolidation log: {}".format(out_path.name))

    # Generate comparison report
    comparison_path = LOGS_DIR / "{}-cultural_language_comparison.md".format(
        DATE_PREFIX)
    generate_comparison_report(log, comparison_path)
    print("Comparison report: {}".format(comparison_path.name))

    if args.dry_run:
        print("\n(Dry run — no paper files modified)")

    print("\n=== DONE ===")


if __name__ == "__main__":
    main()
