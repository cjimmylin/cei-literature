#!/usr/bin/env python3
"""
Vault-Wide Religious Values Distribution Analysis

Reads all ~2,043 paper files from the CEI-Lit-WS papers/ directory,
extracts 14 rv_* fields from YAML frontmatter using regex (no yaml.load),
and computes:

1. rv_* distributions: mean, median, max, std, count>=50 per field
2. Tradition co-occurrence: 14x14 matrix + Jaccard similarity for papers with 2+ rv_* >= 50
3. Temporal trends: papers per year x tradition (rv_* >= 50), year-over-year growth
4. Benchmark intersection: papers with (is_benchmark=true OR is_eval=true OR is_dataset=true) AND any rv_* >= 50

Output: RELIGIOUS-VALUES/data/20260404-vault-rv-distributions.json
"""
from __future__ import annotations

import functools
import json
import re
import statistics
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

print = functools.partial(print, flush=True)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
WS_DIR = SCRIPT_DIR.parent.parent  # CEI-Lit-WS/
PAPERS_DIR = WS_DIR / "papers"
OUTPUT_DIR = SCRIPT_DIR.parent / "data"
OUTPUT_FILE = OUTPUT_DIR / "20260404-vault-rv-distributions.json"

# ---------------------------------------------------------------------------
# The 14 rv_* fields
# ---------------------------------------------------------------------------
RV_FIELDS = [
    "rv_islam",
    "rv_christianity",
    "rv_buddhism",
    "rv_judaism",
    "rv_hinduism",
    "rv_sikhism",
    "rv_confucianism",
    "rv_taoism",
    "rv_shinto",
    "rv_jainism",
    "rv_bahai",
    "rv_zoroastrianism",
    "rv_ubuntu",
    "rv_indigenous",
]

# Benchmark/eval/dataset fields (boolean)
BENCHMARK_FIELDS = ["is_benchmark", "is_eval", "is_dataset"]


def extract_rv_value(content: str, field: str) -> int | None:
    """Extract an rv_* integer value from YAML frontmatter using regex."""
    m = re.search(rf'^{re.escape(field)}:\s*(\d+)', content, re.MULTILINE)
    if m:
        return int(m.group(1))
    return None


def extract_bool_field(content: str, field: str) -> bool:
    """Extract a boolean YAML field (true/false/yes/no)."""
    m = re.search(rf'^{re.escape(field)}:\s*(true|false|yes|no)', content, re.MULTILINE | re.IGNORECASE)
    if m:
        val = m.group(1).lower()
        return val in ("true", "yes")
    return False


def extract_year(content: str, filename: str) -> str | None:
    """Extract year from YAML frontmatter or filename."""
    m = re.search(r'^year:\s*["\']?(\d{4})', content, re.MULTILINE)
    if m:
        return m.group(1)
    # Fallback: extract from filename
    m2 = re.match(r'^(\d{4})-', filename)
    if m2:
        return m2.group(1)
    return None


def compute_jaccard(set_a: set, set_b: set) -> float:
    """Compute Jaccard similarity between two sets."""
    if not set_a and not set_b:
        return 0.0
    intersection = len(set_a & set_b)
    union = len(set_a | set_b)
    return intersection / union if union > 0 else 0.0


def main() -> None:
    print(f"Vault-Wide Religious Values Analysis")
    print(f"Date: {date.today().isoformat()}")
    print(f"Papers dir: {PAPERS_DIR}")
    print()

    if not PAPERS_DIR.is_dir():
        print(f"ERROR: Papers directory not found: {PAPERS_DIR}")
        sys.exit(1)

    # ---------------------------------------------------------------------------
    # Read all paper files
    # ---------------------------------------------------------------------------
    paper_files = sorted(PAPERS_DIR.iterdir())
    paper_files = [f for f in paper_files if f.suffix == ".md" and f.is_file()]
    print(f"Found {len(paper_files)} paper files")

    # ---------------------------------------------------------------------------
    # Extract data from all papers
    # ---------------------------------------------------------------------------
    # Per-field value lists
    field_values: dict[str, list[int]] = {f: [] for f in RV_FIELDS}

    # Per-paper: which traditions are >= 50
    paper_traditions: list[tuple[str, str | None, set[str]]] = []  # (filename, year, set of active traditions)

    # Benchmark intersection tracking
    benchmark_and_rv_count = 0
    benchmark_and_rv_papers: list[str] = []

    # Temporal tracking
    year_tradition_counts: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))

    papers_with_rv = 0
    papers_without_rv = 0

    for pf in paper_files:
        try:
            content = pf.read_text(encoding="utf-8")
        except Exception as e:
            print(f"  WARN: Could not read {pf.name}: {e}")
            continue

        # Extract rv_* values
        active_traditions: set[str] = set()
        has_any_rv = False

        for field in RV_FIELDS:
            val = extract_rv_value(content, field)
            if val is not None:
                field_values[field].append(val)
                has_any_rv = True
                if val >= 50:
                    active_traditions.add(field)

        if has_any_rv:
            papers_with_rv += 1
        else:
            papers_without_rv += 1

        # Extract year
        year = extract_year(content, pf.name)

        paper_traditions.append((pf.name, year, active_traditions))

        # Track temporal trends
        if year and active_traditions:
            for trad in active_traditions:
                year_tradition_counts[year][trad] += 1

        # Benchmark intersection
        if active_traditions:
            is_bench = any(extract_bool_field(content, bf) for bf in BENCHMARK_FIELDS)
            if is_bench:
                benchmark_and_rv_count += 1
                benchmark_and_rv_papers.append(pf.name)

    print(f"Papers with rv_* fields: {papers_with_rv}")
    print(f"Papers without rv_* fields: {papers_without_rv}")
    print()

    # ---------------------------------------------------------------------------
    # 1. rv_* distributions
    # ---------------------------------------------------------------------------
    print("=== 1. rv_* Field Distributions ===")
    distributions: dict[str, dict] = {}

    for field in RV_FIELDS:
        vals = field_values[field]
        if not vals:
            distributions[field] = {
                "count": 0,
                "mean": 0.0,
                "median": 0.0,
                "max": 0,
                "std": 0.0,
                "count_gte_50": 0,
                "pct_gte_50": 0.0,
            }
            continue

        mean_val = statistics.mean(vals)
        median_val = statistics.median(vals)
        max_val = max(vals)
        std_val = statistics.stdev(vals) if len(vals) > 1 else 0.0
        count_gte_50 = sum(1 for v in vals if v >= 50)
        pct_gte_50 = (count_gte_50 / len(vals)) * 100 if vals else 0.0

        distributions[field] = {
            "count": len(vals),
            "mean": round(mean_val, 2),
            "median": round(median_val, 2),
            "max": max_val,
            "std": round(std_val, 2),
            "count_gte_50": count_gte_50,
            "pct_gte_50": round(pct_gte_50, 2),
        }

        print(f"  {field}: n={len(vals)}, mean={mean_val:.2f}, median={median_val:.1f}, "
              f"max={max_val}, std={std_val:.2f}, >=50: {count_gte_50} ({pct_gte_50:.1f}%)")

    print()

    # ---------------------------------------------------------------------------
    # 2. Tradition co-occurrence (papers with 2+ rv_* >= 50)
    # ---------------------------------------------------------------------------
    print("=== 2. Tradition Co-occurrence ===")

    # Build per-tradition paper sets (for Jaccard)
    tradition_paper_sets: dict[str, set[str]] = {f: set() for f in RV_FIELDS}
    multi_tradition_papers = 0

    for filename, year, active in paper_traditions:
        for trad in active:
            tradition_paper_sets[trad].add(filename)
        if len(active) >= 2:
            multi_tradition_papers += 1

    print(f"Papers with 2+ traditions >= 50: {multi_tradition_papers}")

    # Co-occurrence matrix (count of papers where both traditions >= 50)
    cooccurrence: dict[str, dict[str, int]] = {f: {g: 0 for g in RV_FIELDS} for f in RV_FIELDS}

    for filename, year, active in paper_traditions:
        active_list = sorted(active)
        for i, t1 in enumerate(active_list):
            for t2 in active_list[i:]:
                cooccurrence[t1][t2] += 1
                if t1 != t2:
                    cooccurrence[t2][t1] += 1

    # Jaccard similarity matrix
    jaccard: dict[str, dict[str, float]] = {f: {} for f in RV_FIELDS}
    for i, t1 in enumerate(RV_FIELDS):
        for t2 in RV_FIELDS[i:]:
            j = compute_jaccard(tradition_paper_sets[t1], tradition_paper_sets[t2])
            jaccard[t1][t2] = round(j, 4)
            if t1 != t2:
                jaccard[t2][t1] = round(j, 4)

    # Print top co-occurring pairs
    pairs: list[tuple[str, str, int]] = []
    for i, t1 in enumerate(RV_FIELDS):
        for t2 in RV_FIELDS[i + 1:]:
            if cooccurrence[t1][t2] > 0:
                pairs.append((t1, t2, cooccurrence[t1][t2]))

    pairs.sort(key=lambda x: -x[2])
    print("Top co-occurring tradition pairs:")
    for t1, t2, count in pairs[:15]:
        j = jaccard[t1][t2]
        print(f"  {t1} + {t2}: {count} papers (Jaccard={j:.4f})")
    print()

    # ---------------------------------------------------------------------------
    # 3. Temporal trends
    # ---------------------------------------------------------------------------
    print("=== 3. Temporal Trends ===")

    all_years = sorted(year_tradition_counts.keys())
    temporal_data: dict[str, dict[str, int]] = {}
    for yr in all_years:
        temporal_data[yr] = dict(year_tradition_counts[yr])

    # Year-over-year growth (total papers with any rv_* >= 50 per year)
    year_totals: dict[str, int] = {}
    for filename, year, active in paper_traditions:
        if year and active:
            year_totals[year] = year_totals.get(year, 0) + 1

    yoy_growth: dict[str, float | None] = {}
    sorted_years = sorted(year_totals.keys())
    for i, yr in enumerate(sorted_years):
        if i == 0:
            yoy_growth[yr] = None
        else:
            prev = year_totals[sorted_years[i - 1]]
            curr = year_totals[yr]
            if prev > 0:
                yoy_growth[yr] = round(((curr - prev) / prev) * 100, 1)
            else:
                yoy_growth[yr] = None

    print(f"Years with religious values papers: {len(sorted_years)}")
    for yr in sorted_years:
        count = year_totals[yr]
        growth = yoy_growth.get(yr)
        growth_str = f" (YoY: {growth:+.1f}%)" if growth is not None else ""
        print(f"  {yr}: {count} papers{growth_str}")

    # Per-tradition temporal breakdown
    tradition_temporal: dict[str, dict[str, int]] = {f: {} for f in RV_FIELDS}
    for yr in all_years:
        for trad, count in year_tradition_counts[yr].items():
            tradition_temporal[trad][yr] = count

    print()

    # ---------------------------------------------------------------------------
    # 4. Benchmark intersection
    # ---------------------------------------------------------------------------
    print("=== 4. Benchmark / Eval / Dataset Intersection ===")
    print(f"Papers with (is_benchmark OR is_eval OR is_dataset) AND any rv_* >= 50: {benchmark_and_rv_count}")
    if benchmark_and_rv_papers:
        print("Papers:")
        for p in sorted(benchmark_and_rv_papers)[:30]:
            print(f"  {p}")
        if len(benchmark_and_rv_papers) > 30:
            print(f"  ... and {len(benchmark_and_rv_papers) - 30} more")
    print()

    # ---------------------------------------------------------------------------
    # Assemble output
    # ---------------------------------------------------------------------------
    output = {
        "generated": date.today().strftime("%Y%m%d"),
        "total_papers_scanned": len(paper_files),
        "papers_with_rv_fields": papers_with_rv,
        "papers_without_rv_fields": papers_without_rv,
        "rv_distributions": distributions,
        "co_occurrence": {
            "multi_tradition_paper_count": multi_tradition_papers,
            "matrix": cooccurrence,
            "jaccard_similarity": jaccard,
            "top_pairs": [
                {"tradition_1": t1, "tradition_2": t2, "count": c, "jaccard": jaccard[t1][t2]}
                for t1, t2, c in pairs[:20]
            ],
        },
        "temporal_trends": {
            "year_totals": {yr: year_totals.get(yr, 0) for yr in sorted_years},
            "year_over_year_growth_pct": yoy_growth,
            "tradition_by_year": tradition_temporal,
            "per_year_detail": temporal_data,
        },
        "benchmark_intersection": {
            "count": benchmark_and_rv_count,
            "papers": sorted(benchmark_and_rv_papers),
        },
    }

    # Write output
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Output written to: {OUTPUT_FILE}")
    print("Done.")


if __name__ == "__main__":
    main()
