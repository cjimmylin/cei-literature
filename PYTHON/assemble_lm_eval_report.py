#!/usr/bin/env python3
"""
Assemble lm-eval-harness Implementability Report.

Merges outputs from Phase A agents (3-9), classifies papers into tiers,
and generates a markdown report + JSON data file.

Agent 10 (Report Assembler)
"""

import json
import re
import functools
from pathlib import Path
from datetime import date

print = functools.partial(print, flush=True)

# ── Paths ────────────────────────────────────────────────────────────────────
BASE = Path(__file__).resolve().parent.parent  # CEI-Lit-WS/
LOGS = BASE / "logs"
STATS = BASE / "STATISTICS"

INPUT_FILES = {
    "harness":    LOGS / "20260312-harness-matches.json",
    "pdf_2016":   LOGS / "20260312-pdf-impl-details-2016-2021.json",
    "pdf_2022":   LOGS / "20260312-pdf-impl-details-2022-2023.json",
    "pdf_2024":   LOGS / "20260312-pdf-impl-details-2024.json",
    "pdf_2025":   LOGS / "20260312-pdf-impl-details-2025-2026.json",
    "scores_al":  LOGS / "20260312-scores-a-l.json",
    "scores_mz":  LOGS / "20260312-scores-m-z.json",
    "survey":     LOGS / "20260216-benchmark_survey_candidates.json",
}

REPORT_PATH = STATS / "20260312-lm-eval-implementability-report.md"
JSON_PATH   = LOGS / "20260312-lm-eval-implementability-data.json"

TODAY = "2026-03-12"


# ── Helpers ──────────────────────────────────────────────────────────────────

def load_json(path):
    with open(path) as f:
        return json.load(f)


def slugify(name):
    """Convert benchmark name to a plausible lm-eval task slug."""
    if not name:
        return "unknown_task"
    s = name.lower().strip()
    s = re.sub(r'[^a-z0-9]+', '_', s)
    s = s.strip('_')
    return s[:60] if s else "unknown_task"


def paper_display(filename):
    """Convert filename to readable display name."""
    return filename.replace('.md', '')


def extract_year(filename):
    m = re.match(r'^(\d{4})-', filename)
    return m.group(1) if m else "????"


def has_hf_url(data_url, pdf_detail):
    """Check if paper has a HuggingFace URL anywhere."""
    if data_url and 'huggingface' in str(data_url).lower():
        return True
    if pdf_detail and pdf_detail.get('hf_urls'):
        return True
    return False


def get_missing_items(score_entry, pdf_detail):
    """List what's missing for a paper to be implementable."""
    missing = []
    if not score_entry.get('data_url'):
        missing.append("no DATA_URL")
    avail = score_entry.get('availability', '')
    if avail not in ('Public',) and not str(avail).startswith('Public'):
        missing.append("no public availability")
    if pdf_detail:
        if not pdf_detail.get('task_type'):
            missing.append("no task type detected")
        if not pdf_detail.get('metrics'):
            missing.append("no metrics found")
        if not pdf_detail.get('splits'):
            missing.append("no data splits")
    else:
        missing.append("no PDF extract details")
    return missing


def top_signals(signals, n=3):
    """Return comma-separated top N signals."""
    if not signals:
        return ""
    return ", ".join(s.split(" (+")[0] for s in signals[:n])


# ── 1. Load all inputs ──────────────────────────────────────────────────────

print("Loading input files...")

# Scores: merge A-L + M-Z
scores_al = load_json(INPUT_FILES["scores_al"])
scores_mz = load_json(INPUT_FILES["scores_mz"])
scores = {}
for entry in scores_al["entries"] + scores_mz["entries"]:
    scores[entry["filename"]] = entry

print(f"  Scores loaded: {len(scores)} papers")

# Harness matches: only entries with actual matches
harness_data = load_json(INPUT_FILES["harness"])
harness_matches = {}
for entry in harness_data["entries"]:
    if entry.get("harness_match"):
        harness_matches[entry["filename"]] = entry

print(f"  Harness matches loaded: {len(harness_matches)} matched papers")

# PDF details: merge all year ranges
pdf_details = {}
pdf_count = 0
for key in ["pdf_2016", "pdf_2022", "pdf_2024", "pdf_2025"]:
    data = load_json(INPUT_FILES[key])
    for entry in data["entries"]:
        pdf_details[entry["filename"]] = entry
        pdf_count += 1

print(f"  PDF extract details loaded: {pdf_count} entries")

# Survey data
survey_raw = load_json(INPUT_FILES["survey"])
survey = {e["filename"]: e for e in survey_raw}
print(f"  Survey candidates loaded: {len(survey)} entries")

# Known harness tasks count (from the module)
import importlib.util
spec = importlib.util.spec_from_file_location(
    "lm_eval_known_tasks",
    BASE / "PYTHON" / "lm_eval_known_tasks.py"
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
KNOWN_HARNESS_TASKS = mod.KNOWN_HARNESS_TASKS
KNOWN_TASKS_COUNT = len(KNOWN_HARNESS_TASKS)
all_aliases = mod.get_all_aliases()  # lowercased alias -> task key
print(f"  Known harness tasks: {KNOWN_TASKS_COUNT}")

# ── 1b. Filename-based harness matching (catches papers not in survey) ─────
print("\nRunning filename-based harness matching fallback...")
filename_matches = 0
for filename in scores:
    if filename in harness_matches:
        continue  # already matched via survey
    # Extract title portion from filename: YYYY-Author-Title.md
    parts = filename.replace('.md', '').split('-', 2)
    if len(parts) >= 3:
        title_part = parts[2].lower()
    elif len(parts) == 2:
        title_part = parts[1].lower()
    else:
        title_part = filename.lower()
    # Also try the full filename minus year and extension
    full_name = filename.replace('.md', '').lower()
    # Check against all aliases — only match specific benchmark names, not generic terms
    GENERIC_BLOCKLIST = {
        'machinelearning', 'philosophy', 'medicalethics', 'businessethics',
        'professionallaw', 'jurisprudence', 'moralscenarios', 'moraldisputes',
    }
    for alias, task_key in all_aliases.items():
        # Require alias length >= 6 to avoid false positives
        if len(alias) < 6:
            continue
        alias_clean = re.sub(r'[^a-z0-9]', '', alias)
        if alias_clean in GENERIC_BLOCKLIST:
            continue
        title_clean = re.sub(r'[^a-z0-9]', '', title_part)
        full_clean = re.sub(r'[^a-z0-9]', '', full_name)
        if alias_clean and len(alias_clean) >= 6:
            if (alias_clean in title_clean or alias_clean in full_clean
                    or (len(title_clean) >= 8 and title_clean in alias_clean)):
                harness_matches[filename] = {
                    "filename": filename,
                    "harness_match": task_key,
                    "match_method": "filename",
                    "availability": scores[filename].get("availability", ""),
                    "benchmark_name": parts[2] if len(parts) >= 3 else filename,
                }
                filename_matches += 1
                break
print(f"  Filename-based matches added: {filename_matches}")
print(f"  Total harness matches: {len(harness_matches)}")


# ── 2. Classify tiers ───────────────────────────────────────────────────────

print("\nClassifying tiers...")

tiers = {
    "ALREADY_IN_HARNESS":   [],
    "READY_TO_IMPLEMENT":   [],
    "NEEDS_DATASET_HOSTING":[],
    "NEEDS_MORE_INFO":      [],
    "NOT_IMPLEMENTABLE":    [],
}

for filename, se in scores.items():
    score = se.get("score", 0)
    pd = pdf_details.get(filename, {})
    avail = se.get("availability", "")
    is_public = avail == "Public" or str(avail).startswith("Public")
    has_hf = has_hf_url(se.get("data_url"), pd)

    if filename in harness_matches:
        tier = "ALREADY_IN_HARNESS"
    elif score >= 65 and (is_public or has_hf):
        tier = "READY_TO_IMPLEMENT"
    elif score >= 45 and filename not in harness_matches and not has_hf:
        tier = "NEEDS_DATASET_HOSTING"
    elif 30 <= score <= 44:
        tier = "NEEDS_MORE_INFO"
    elif score < 30:
        tier = "NOT_IMPLEMENTABLE"
    else:
        # score >= 45 but doesn't fit READY or HOSTING — put in HOSTING
        tier = "NEEDS_DATASET_HOSTING"

    tiers[tier].append(filename)

# Sort each tier by score descending
for tier_name in tiers:
    tiers[tier_name].sort(key=lambda f: scores[f].get("score", 0), reverse=True)

total_scored = len(scores)

print("Tier distribution:")
for t, papers in tiers.items():
    pct = len(papers) / total_scored * 100 if total_scored else 0
    print(f"  {t}: {len(papers)} ({pct:.1f}%)")


# ── 3. Build implementation sketches for top-10 Ready to Implement ───────────

print("\nBuilding implementation sketches for top-10 Ready to Implement...")

sketches = []
for filename in tiers["READY_TO_IMPLEMENT"][:10]:
    se = scores[filename]
    pd = pdf_details.get(filename, {})
    sv = survey.get(filename, {})
    hm = harness_matches.get(filename)

    bench_name = sv.get("benchmark_name", paper_display(filename))
    task_slug = slugify(bench_name)

    # Dataset path
    data_url = se.get("data_url", "")
    hf_urls = pd.get("hf_urls", []) if pd else []
    if hf_urls:
        dataset_path = hf_urls[0]
    elif data_url and 'huggingface' in str(data_url).lower():
        dataset_path = data_url
    elif data_url:
        dataset_path = data_url
    else:
        dataset_path = "needs upload to HuggingFace"

    task_type = pd.get("task_type", "unknown") if pd else "unknown"
    metrics = pd.get("metrics", []) if pd else []
    prompt_hints = pd.get("prompt_hints", []) if pd else []
    github_urls = pd.get("github_urls", []) if pd else []

    # What's missing
    gaps = []
    if not metrics:
        gaps.append("No metrics defined in extract")
    if not pd.get("splits"):
        gaps.append("Data splits not identified")
    if dataset_path == "needs upload to HuggingFace":
        gaps.append("Dataset not on HuggingFace yet")
    if not prompt_hints:
        gaps.append("No prompt template hints found")
    if not gaps:
        gaps.append("Appears ready — verify dataset format compatibility")

    sketch = {
        "filename": filename,
        "bench_name": bench_name,
        "task_slug": task_slug,
        "dataset_path": dataset_path,
        "task_type": task_type,
        "metrics": metrics,
        "prompt_hints": prompt_hints,
        "gaps": gaps,
        "score": se.get("score", 0),
    }
    sketches.append(sketch)

print(f"  Built {len(sketches)} sketches")


# ── 4. Generate Markdown Report ─────────────────────────────────────────────

print(f"\nGenerating markdown report: {REPORT_PATH}")

lines = []
L = lines.append

L("# lm-eval-harness Implementability Report")
L(f"Generated: {TODAY}")
L("")
L("## Executive Summary")
L("")
L("| Tier | Count | % of Scored |")
L("|------|-------|-------------|")

tier_display = [
    ("Already in Harness",     "ALREADY_IN_HARNESS"),
    ("Ready to Implement",     "READY_TO_IMPLEMENT"),
    ("Needs Dataset Hosting",  "NEEDS_DATASET_HOSTING"),
    ("Needs More Info",        "NEEDS_MORE_INFO"),
    ("Not Implementable",      "NOT_IMPLEMENTABLE"),
]

for display, key in tier_display:
    cnt = len(tiers[key])
    pct = cnt / total_scored * 100 if total_scored else 0
    L(f"| {display} | {cnt} | {pct:.1f}% |")

L(f"| **Total Scored** | **{total_scored}** | |")
L("")
L(f"**PDF Extracts Analyzed:** {pdf_count} across 2016-2026")
L(f"**Survey Entries Cross-Referenced:** {len(survey)} ({len(harness_matches)} matched to harness)")
L(f"**Known Harness Tasks:** {KNOWN_TASKS_COUNT}")
L("")

# ── Section 1: Already in Harness ───────────────────────────────────────────
n1 = len(tiers["ALREADY_IN_HARNESS"])
L(f"## 1. Already in lm-eval-harness ({n1} papers)")
L("")
L("| Paper | Year | Harness Task | Match Method | Availability |")
L("|-------|------|-------------|--------------|--------------|")

for fn in tiers["ALREADY_IN_HARNESS"]:
    hm = harness_matches.get(fn, {})
    year = extract_year(fn)
    task = hm.get("harness_match", "?")
    method = hm.get("match_method", "?")
    avail = hm.get("availability", scores.get(fn, {}).get("availability", "?"))
    L(f"| {paper_display(fn)} | {year} | `{task}` | {method} | {avail} |")

L("")

# ── Section 2: Ready to Implement ──────────────────────────────────────────
n2 = len(tiers["READY_TO_IMPLEMENT"])
L(f"## 2. Ready to Implement ({n2} papers, score >= 65)")
L("")
L("| # | Paper | Score | Benchmark | Type | Data URL | Key Signals |")
L("|---|-------|-------|-----------|------|----------|-------------|")

for i, fn in enumerate(tiers["READY_TO_IMPLEMENT"], 1):
    se = scores[fn]
    sv = survey.get(fn, {})
    pd_ = pdf_details.get(fn, {})
    bench = sv.get("benchmark_name", "—")
    ttype = pd_.get("task_type", "—") if pd_ else "—"
    durl = se.get("data_url", "—") or "—"
    if len(str(durl)) > 50:
        durl_display = str(durl)[:47] + "..."
    else:
        durl_display = durl
    sigs = top_signals(se.get("signals", []))
    L(f"| {i} | {paper_display(fn)} | {se['score']} | {bench} | {ttype} | {durl_display} | {sigs} |")

L("")
L("### Implementation Sketches (Top 10)")
L("")

for sk in sketches:
    L(f"### {paper_display(sk['filename'])} (score: {sk['score']})")
    L(f"- **Suggested task name:** `{sk['task_slug']}`")
    L(f"- **Dataset path:** `{sk['dataset_path']}`")
    L(f"- **Task type:** `{sk['task_type']}`")
    L(f"- **Metrics:** {', '.join(sk['metrics']) if sk['metrics'] else 'not determined'}")
    L(f"- **Prompt template notes:** {'; '.join(sk['prompt_hints'][:3]) if sk['prompt_hints'] else 'none found'}")
    L(f"- **What's missing:** {'; '.join(sk['gaps'])}")
    L("")

# ── Section 3: Needs Dataset Hosting ────────────────────────────────────────
n3 = len(tiers["NEEDS_DATASET_HOSTING"])
L(f"## 3. Needs Dataset Hosting ({n3} papers, score 45-64)")
L("")
L("| # | Paper | Score | Data URL | What's Missing |")
L("|---|-------|-------|----------|----------------|")

for i, fn in enumerate(tiers["NEEDS_DATASET_HOSTING"], 1):
    se = scores[fn]
    pd_ = pdf_details.get(fn, {})
    durl = se.get("data_url", "—") or "—"
    if len(str(durl)) > 40:
        durl = str(durl)[:37] + "..."
    missing = get_missing_items(se, pd_)
    L(f"| {i} | {paper_display(fn)} | {se['score']} | {durl} | {', '.join(missing)} |")

L("")

# ── Section 4: Needs More Info ──────────────────────────────────────────────
n4 = len(tiers["NEEDS_MORE_INFO"])
L(f"## 4. Needs More Info ({n4} papers, score 30-44)")
L("")
L("| # | Paper | Score | Missing Items |")
L("|---|-------|-------|---------------|")

CAP = 50
for i, fn in enumerate(tiers["NEEDS_MORE_INFO"][:CAP], 1):
    se = scores[fn]
    pd_ = pdf_details.get(fn, {})
    missing = get_missing_items(se, pd_)
    L(f"| {i} | {paper_display(fn)} | {se['score']} | {', '.join(missing)} |")

if n4 > CAP:
    L(f"\n... and {n4 - CAP} more papers in this tier.")

L("")

# ── Section 5: Not Implementable ────────────────────────────────────────────
n5 = len(tiers["NOT_IMPLEMENTABLE"])
L(f"## 5. Not Implementable ({n5} papers, score < 30)")
L("")
L(f"{n5} papers scored below 30 — primarily theoretical/philosophical papers, surveys, and position papers without associated datasets.")
L("")
L("---")
L("*Generated by lm-eval-harness Implementability Scanner*")
L(f"*Data sources: 2,034 vault papers, {len(survey)} benchmark survey entries, {pdf_count} PDF extracts*")

report_text = "\n".join(lines) + "\n"
STATS.mkdir(parents=True, exist_ok=True)
REPORT_PATH.write_text(report_text, encoding="utf-8")
print(f"  Report written: {len(lines)} lines")


# ── 5. Generate JSON ────────────────────────────────────────────────────────

print(f"\nGenerating JSON: {JSON_PATH}")

# Build per-paper records
paper_records = []
for filename, se in scores.items():
    # Determine tier
    for tier_name, tier_files in tiers.items():
        if filename in tier_files:
            tier = tier_name
            break
    else:
        tier = "UNKNOWN"

    pd_ = pdf_details.get(filename)
    hm = harness_matches.get(filename)
    sv = survey.get(filename)

    record = {
        "filename": filename,
        "score": se.get("score", 0),
        "tier": tier,
        "signals": se.get("signals", []),
        "harness_match": hm.get("harness_match") if hm else None,
        "impl_details": pd_ if pd_ else None,
        "survey_data": {
            "benchmark_name": sv.get("benchmark_name"),
            "what_measures": sv.get("what_measures"),
            "availability": sv.get("availability"),
        } if sv else None,
    }
    paper_records.append(record)

# Sort by score descending
paper_records.sort(key=lambda r: r["score"], reverse=True)

output = {
    "generated": TODAY,
    "summary": {
        "total_scored": total_scored,
        "tier_counts": {t: len(fs) for t, fs in tiers.items()},
        "pdf_extracts_analyzed": pdf_count,
        "survey_entries": len(survey),
        "harness_matches": len(harness_matches),
        "known_harness_tasks": KNOWN_TASKS_COUNT,
    },
    "papers": paper_records,
}

LOGS.mkdir(parents=True, exist_ok=True)
tmp_path = JSON_PATH.with_suffix(f".tmp.{__import__('os').getpid()}.json")
with open(tmp_path, "w") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)
import os
os.replace(tmp_path, JSON_PATH)

print(f"  JSON written: {len(paper_records)} paper records")


# ── 6. Summary ──────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("ASSEMBLY COMPLETE")
print("=" * 60)
print(f"  Report: {REPORT_PATH}")
print(f"  JSON:   {JSON_PATH}")
print(f"  Total scored papers: {total_scored}")
for display, key in tier_display:
    print(f"  {display}: {len(tiers[key])}")
print(f"  Top Ready-to-Implement: {paper_display(tiers['READY_TO_IMPLEMENT'][0]) if tiers['READY_TO_IMPLEMENT'] else 'none'}")
