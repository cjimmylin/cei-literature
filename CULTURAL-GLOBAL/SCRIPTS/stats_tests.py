#!/usr/bin/env python3
"""
Statistical Hypothesis Tests for Cross-Cultural AI Values Alignment.

Performs:
    1. Mann-Whitney U: High-WEIRD vs Non-WEIRD for each framework dimension
    2. Kruskal-Wallis: Global North vs South vs Ambiguous
    3. Chi-square: region × framework detection (binary ≥50)
    4. Effect sizes: Cohen's d, Cramér's V, η²
    5. BH-FDR correction for multiple comparisons
    6. Bootstrap CIs (1000 iterations) for regional mean scores

Output:
    DATA/20260403-statistical-tests.json
    STATISTICS/20260403-statistical-deepening-report.md
"""
from __future__ import annotations

import functools
import json
import os
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

import numpy as np

print = functools.partial(print, flush=True)

_SCRIPT_DIR = Path(__file__).parent
_CEI_LIT_WS = _SCRIPT_DIR.parent.parent
sys.path.insert(0, str(_CEI_LIT_WS / "PYTHON"))
sys.path.insert(0, str(_CEI_LIT_WS / ".agent" / "lib"))

TODAY = date.today().strftime("%Y%m%d")
DATA_DIR = _SCRIPT_DIR.parent / "DATA"
STATS_DIR = _SCRIPT_DIR.parent / "STATISTICS"

WESTERN = ["virtue_ethics", "deontological_ethics", "utilitarian_ethics",
           "care_ethics", "contractarian_ethics"]
NW = ["nw_confucian", "nw_ubuntu", "nw_islamic_ethics",
      "nw_buddhist", "nw_dharmic", "nw_indigenous_relational", "nw_buen_vivir"]
ALL_FW = WESTERN + NW

DHARMIC_FAMILY = ["nw_buddhist", "nw_dharmic"]

REGIONS_ORDERED = [
    "North America", "Western Europe", "East Asia", "MENA",
    "South Asia", "Southeast Asia", "Latin America & Caribbean",
    "Eastern Europe & Central Asia", "Oceania", "Sub-Saharan Africa",
]


def load_unified_data() -> list[dict]:
    """Load paper data from all sidecar JSONs."""
    import re
    from config import PAPERS_DIR

    geo_path = sorted(DATA_DIR.glob("*-author-geography.json"), reverse=True)
    weird_path = sorted(DATA_DIR.glob("*-weird-scores.json"), reverse=True)
    nw_path = sorted(DATA_DIR.glob("*-nw-scores.json"), reverse=True)

    geo_lookup, weird_lookup, nw_lookup = {}, {}, {}

    if geo_path:
        with open(geo_path[0]) as f:
            for p in json.load(f)["papers"]:
                geo_lookup[p["filename"]] = p
    if weird_path:
        with open(weird_path[0]) as f:
            for p in json.load(f)["papers"]:
                weird_lookup[p["filename"]] = p
    if nw_path:
        with open(nw_path[0]) as f:
            for p in json.load(f)["papers"]:
                nw_lookup[p["filename"]] = p

    papers = []
    for pf in sorted(PAPERS_DIR.glob("*.md")):
        content = pf.read_text(errors="replace")
        entry = {"filename": pf.name}

        for field in WESTERN + ["ethics_overall"]:
            m = re.search(rf'^{re.escape(field)}:\s*(\d+)', content, re.MULTILINE)
            entry[field] = int(m.group(1)) if m else 0

        geo = geo_lookup.get(pf.name, {})
        entry["region"] = geo.get("author_region", "Unknown")
        entry["north_south"] = geo.get("author_global_north_south", "Unknown")

        weird = weird_lookup.get(pf.name, {})
        entry["weird_score"] = weird.get("weird_score", 50)
        entry["weird_tier"] = weird.get("tier", "Unknown")

        nw = nw_lookup.get(pf.name, {})
        scores = nw.get("scores", {})
        for field in NW:
            entry[field] = scores.get(field, 0)

        papers.append(entry)

    return papers


def compute_dharmic_family(papers: list[dict]) -> list[dict]:
    """Add dharmic_family_max = max(nw_buddhist, nw_dharmic) for each paper."""
    for p in papers:
        p["dharmic_family"] = max(p.get("nw_buddhist", 0), p.get("nw_dharmic", 0))
    return papers


def cohens_d(group1: np.ndarray, group2: np.ndarray) -> float:
    """Compute Cohen's d effect size."""
    n1, n2 = len(group1), len(group2)
    if n1 < 2 or n2 < 2:
        return 0.0
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    if pooled_std == 0:
        return 0.0
    return float((np.mean(group1) - np.mean(group2)) / pooled_std)


def cramers_v(contingency_table: np.ndarray) -> float:
    """Compute Cramér's V from a contingency table."""
    from scipy.stats import chi2_contingency
    chi2, _, _, _ = chi2_contingency(contingency_table)
    n = contingency_table.sum()
    r, k = contingency_table.shape
    return float(np.sqrt(chi2 / (n * (min(r, k) - 1))))


def bh_fdr(pvalues: list[float], alpha: float = 0.05) -> list[bool]:
    """Benjamini-Hochberg FDR correction. Returns list of significant booleans."""
    n = len(pvalues)
    sorted_idx = np.argsort(pvalues)
    sorted_pvals = np.array(pvalues)[sorted_idx]
    thresholds = np.arange(1, n + 1) / n * alpha
    significant = np.zeros(n, dtype=bool)

    # Find largest k where p(k) <= k/n * alpha
    below = sorted_pvals <= thresholds
    if below.any():
        max_k = np.max(np.where(below)[0])
        significant[sorted_idx[:max_k + 1]] = True

    return significant.tolist()


def bootstrap_ci(data: np.ndarray, n_boot: int = 1000, ci: float = 0.95,
                 stat_fn=np.mean) -> tuple[float, float, float]:
    """Bootstrap confidence interval."""
    rng = np.random.default_rng(42)
    boot_stats = []
    for _ in range(n_boot):
        sample = rng.choice(data, size=len(data), replace=True)
        boot_stats.append(stat_fn(sample))
    boot_stats = np.array(boot_stats)
    alpha = (1 - ci) / 2
    lo = float(np.percentile(boot_stats, alpha * 100))
    hi = float(np.percentile(boot_stats, (1 - alpha) * 100))
    return float(stat_fn(data)), lo, hi


def main():
    from scipy.stats import mannwhitneyu, kruskal, chi2_contingency

    print("Loading data...")
    papers = load_unified_data()
    papers = compute_dharmic_family(papers)
    print(f"  Loaded {len(papers)} papers")

    results = {"date": TODAY, "total_papers": len(papers)}

    # ═══════════════════════════════════════════════════════════════════
    # TEST 1: Mann-Whitney U — High-WEIRD vs Non-WEIRD
    # ═══════════════════════════════════════════════════════════════════
    print("\n1. Mann-Whitney U: High-WEIRD vs Non-WEIRD...")

    high_weird = [p for p in papers if p["weird_score"] >= 70]
    non_weird = [p for p in papers if p["weird_score"] < 30]
    print(f"   High-WEIRD: {len(high_weird)}, Non-WEIRD: {len(non_weird)}")

    mw_results = []
    for fw in ALL_FW:
        g1 = np.array([p[fw] for p in high_weird])
        g2 = np.array([p[fw] for p in non_weird])

        if len(g1) < 2 or len(g2) < 2:
            continue

        stat, p_val = mannwhitneyu(g1, g2, alternative="two-sided")
        d = cohens_d(g1, g2)
        mw_results.append({
            "framework": fw,
            "high_weird_mean": round(float(np.mean(g1)), 2),
            "non_weird_mean": round(float(np.mean(g2)), 2),
            "U_statistic": round(float(stat), 1),
            "p_value": round(float(p_val), 6),
            "cohens_d": round(d, 3),
            "effect_size": "large" if abs(d) >= 0.8 else "medium" if abs(d) >= 0.5 else "small" if abs(d) >= 0.2 else "negligible",
        })

    # BH-FDR correction
    pvals = [r["p_value"] for r in mw_results]
    sig = bh_fdr(pvals)
    for i, r in enumerate(mw_results):
        r["significant_bh_fdr"] = sig[i]

    results["mann_whitney_weird"] = mw_results

    print("   Results:")
    for r in mw_results:
        star = "*" if r["significant_bh_fdr"] else ""
        print(f"   {r['framework']:30s} HW={r['high_weird_mean']:5.1f} NW={r['non_weird_mean']:5.1f} "
              f"d={r['cohens_d']:+.3f} p={r['p_value']:.4f}{star}")

    # ═══════════════════════════════════════════════════════════════════
    # TEST 2: Kruskal-Wallis — Global North vs South vs Ambiguous
    # ═══════════════════════════════════════════════════════════════════
    print("\n2. Kruskal-Wallis: North vs South vs Ambiguous...")

    ns_groups = defaultdict(list)
    for p in papers:
        ns = p["north_south"]
        if ns != "Unknown":
            ns_groups[ns].append(p)

    kw_results = []
    for fw in ALL_FW:
        groups = []
        group_labels = []
        for ns in ["Global North", "Global South", "Ambiguous"]:
            if ns in ns_groups:
                vals = np.array([p[fw] for p in ns_groups[ns]])
                groups.append(vals)
                group_labels.append(ns)

        if len(groups) < 2:
            continue

        stat, p_val = kruskal(*groups)

        # η² (eta-squared) = (H - k + 1) / (N - k)
        N = sum(len(g) for g in groups)
        k = len(groups)
        eta_sq = (stat - k + 1) / (N - k) if N > k else 0
        eta_sq = max(0, eta_sq)

        means = {gl: round(float(np.mean(g)), 2) for gl, g in zip(group_labels, groups)}

        kw_results.append({
            "framework": fw,
            "group_means": means,
            "H_statistic": round(float(stat), 2),
            "p_value": round(float(p_val), 6),
            "eta_squared": round(float(eta_sq), 4),
            "effect_size": "large" if eta_sq >= 0.14 else "medium" if eta_sq >= 0.06 else "small",
        })

    pvals = [r["p_value"] for r in kw_results]
    sig = bh_fdr(pvals)
    for i, r in enumerate(kw_results):
        r["significant_bh_fdr"] = sig[i]

    results["kruskal_wallis_ns"] = kw_results

    sig_count = sum(1 for r in kw_results if r["significant_bh_fdr"])
    print(f"   {sig_count}/{len(kw_results)} frameworks significant after BH-FDR")

    # ═══════════════════════════════════════════════════════════════════
    # TEST 3: Chi-square — Region × Framework Detection
    # ═══════════════════════════════════════════════════════════════════
    print("\n3. Chi-square: Region × Framework detection...")

    # Build contingency table (region × framework, binary ≥50)
    regions = [r for r in REGIONS_ORDERED if any(p["region"] == r for p in papers)]
    n_regions = len(regions)
    n_fw = len(ALL_FW)

    contingency = np.zeros((n_regions, n_fw), dtype=int)
    for p in papers:
        if p["region"] not in regions:
            continue
        i = regions.index(p["region"])
        for j, fw in enumerate(ALL_FW):
            if p[fw] >= 50:
                contingency[i, j] += 1

    # Remove columns with all zeros (chi-square needs non-zero)
    nonzero_cols = contingency.sum(axis=0) > 0
    contingency_clean = contingency[:, nonzero_cols]
    fw_clean = [ALL_FW[j] for j in range(n_fw) if nonzero_cols[j]]

    if contingency_clean.shape[1] >= 2:
        chi2, p_val, dof, expected = chi2_contingency(contingency_clean)
        cv = cramers_v(contingency_clean)

        results["chi_square_region_framework"] = {
            "chi2": round(float(chi2), 2),
            "p_value": round(float(p_val), 6),
            "dof": int(dof),
            "cramers_v": round(cv, 4),
            "effect_size": "large" if cv >= 0.5 else "medium" if cv >= 0.3 else "small",
            "contingency_table": {
                "regions": regions,
                "frameworks": fw_clean,
                "counts": contingency_clean.tolist(),
            },
        }
        print(f"   χ²={chi2:.1f}, df={dof}, p={p_val:.6f}, Cramér's V={cv:.4f}")

    # ═══════════════════════════════════════════════════════════════════
    # TEST 4: Bootstrap CIs for Regional Mean Scores
    # ═══════════════════════════════════════════════════════════════════
    print("\n4. Bootstrap CIs (1000 iterations) for regional mean scores...")

    region_papers = defaultdict(list)
    for p in papers:
        if p["region"] in regions:
            region_papers[p["region"]].append(p)

    bootstrap_results = {}
    for region in regions:
        rp = region_papers[region]
        if len(rp) < 5:
            continue

        region_cis = {}
        for fw in ALL_FW:
            vals = np.array([p[fw] for p in rp])
            mean, lo, hi = bootstrap_ci(vals)
            region_cis[fw] = {
                "mean": round(mean, 2),
                "ci_lower": round(lo, 2),
                "ci_upper": round(hi, 2),
            }

        bootstrap_results[region] = {
            "n": len(rp),
            "framework_cis": region_cis,
        }

    results["bootstrap_cis"] = bootstrap_results
    print(f"   Computed CIs for {len(bootstrap_results)} regions")

    # ═══════════════════════════════════════════════════════════════════
    # TEST 5: Dharmic Family Aggregation
    # ═══════════════════════════════════════════════════════════════════
    print("\n5. Dharmic family aggregation (max of nw_buddhist, nw_dharmic)...")

    dharmic_fw = ALL_FW + ["dharmic_family"]

    # Mann-Whitney for dharmic_family
    g1 = np.array([p["dharmic_family"] for p in high_weird])
    g2 = np.array([p["dharmic_family"] for p in non_weird])
    if len(g1) >= 2 and len(g2) >= 2:
        stat, p_val = mannwhitneyu(g1, g2, alternative="two-sided")
        d = cohens_d(g1, g2)
        results["dharmic_family_mann_whitney"] = {
            "high_weird_mean": round(float(np.mean(g1)), 2),
            "non_weird_mean": round(float(np.mean(g2)), 2),
            "U_statistic": round(float(stat), 1),
            "p_value": round(float(p_val), 6),
            "cohens_d": round(d, 3),
        }
        print(f"   dharmic_family MW: HW={np.mean(g1):.2f} NW={np.mean(g2):.2f} d={d:+.3f} p={p_val:.4f}")

    # Kruskal-Wallis for dharmic_family
    groups_df = []
    labels_df = []
    for ns in ["Global North", "Global South", "Ambiguous"]:
        if ns in ns_groups:
            vals = np.array([p["dharmic_family"] for p in ns_groups[ns]])
            groups_df.append(vals)
            labels_df.append(ns)
    if len(groups_df) >= 2:
        stat, p_val = kruskal(*groups_df)
        N = sum(len(g) for g in groups_df)
        k = len(groups_df)
        eta_sq = max(0, (stat - k + 1) / (N - k)) if N > k else 0
        results["dharmic_family_kruskal_wallis"] = {
            "group_means": {gl: round(float(np.mean(g)), 2) for gl, g in zip(labels_df, groups_df)},
            "H_statistic": round(float(stat), 2),
            "p_value": round(float(p_val), 6),
            "eta_squared": round(float(eta_sq), 4),
        }
        print(f"   dharmic_family KW: H={stat:.2f} p={p_val:.4f} eta2={eta_sq:.4f}")

    dharmic_detected = sum(1 for p in papers if p["dharmic_family"] >= 50)
    buddhist_detected = sum(1 for p in papers if p.get("nw_buddhist", 0) >= 50)
    dharmic_only_detected = sum(1 for p in papers if p.get("nw_dharmic", 0) >= 50)
    results["dharmic_family_summary"] = {
        "dharmic_family_detected": dharmic_detected,
        "buddhist_detected": buddhist_detected,
        "dharmic_detected": dharmic_only_detected,
        "family_gain": dharmic_detected - max(buddhist_detected, dharmic_only_detected),
    }
    print(f"   Family detected: {dharmic_detected} (Buddhist={buddhist_detected}, Dharmic={dharmic_only_detected})")

    # ═══════════════════════════════════════════════════════════════════
    # TEST 6: Within-Region Variance Analysis
    # ═══════════════════════════════════════════════════════════════════
    print("\n6. Within-region variance analysis...")

    within_region_stats = {}
    for region in regions:
        rp = region_papers[region]
        if len(rp) < 5:
            continue

        region_stats = {}
        for fw in dharmic_fw:
            vals = np.array([p[fw] for p in rp])
            sd = float(np.std(vals, ddof=1)) if len(vals) > 1 else 0.0
            q25, q75 = float(np.percentile(vals, 25)), float(np.percentile(vals, 75))
            iqr = q75 - q25
            region_stats[fw] = {
                "n": len(vals),
                "mean": round(float(np.mean(vals)), 2),
                "sd": round(sd, 2),
                "iqr": round(iqr, 2),
                "q25": round(q25, 2),
                "q75": round(q75, 2),
            }
        within_region_stats[region] = region_stats

    # Flag where within-region SD > between-region mean difference
    variance_flags = []
    for fw in dharmic_fw:
        region_means = []
        region_sds = []
        for region in regions:
            if region in within_region_stats and fw in within_region_stats[region]:
                rs = within_region_stats[region][fw]
                region_means.append(rs["mean"])
                region_sds.append(rs["sd"])

        if len(region_means) >= 2:
            between_diff = max(region_means) - min(region_means)
            mean_within_sd = float(np.mean(region_sds))
            flagged = mean_within_sd > between_diff

            variance_flags.append({
                "framework": fw,
                "between_region_range": round(between_diff, 2),
                "mean_within_region_sd": round(mean_within_sd, 2),
                "within_exceeds_between": flagged,
            })
            if flagged:
                print(f"   WARNING: {fw} within-SD ({mean_within_sd:.2f}) > between-range ({between_diff:.2f})")

    results["within_region_variance"] = within_region_stats
    results["variance_flags"] = variance_flags

    flagged_count = sum(1 for vf in variance_flags if vf["within_exceeds_between"])
    print(f"   {flagged_count}/{len(variance_flags)} frameworks have within-SD > between-range")

    # ═══════════════════════════════════════════════════════════════════
    # SAVE & REPORT
    # ═══════════════════════════════════════════════════════════════════
    out_path = DATA_DIR / f"{TODAY}-statistical-tests.json"
    tmp = out_path.with_suffix(f".tmp.{os.getpid()}.json")
    tmp.write_text(json.dumps(results, indent=2))
    os.replace(str(tmp), str(out_path))
    print(f"\nSaved to {out_path}")

    # Generate report
    report = generate_report(results)
    report_path = STATS_DIR / f"{TODAY}-statistical-deepening-report.md"
    report_path.write_text(report)
    print(f"Saved report to {report_path}")

    return 0


def generate_report(results: dict) -> str:
    lines = [
        "# Statistical Deepening Report",
        "",
        f"**Date:** {results['date']}",
        f"**Papers:** {results['total_papers']}",
        "",
        "## 1. Mann-Whitney U: High-WEIRD vs Non-WEIRD",
        "",
        "| Framework | High-WEIRD Mean | Non-WEIRD Mean | Cohen's d | p-value | Sig (BH-FDR) |",
        "|-----------|----------------|---------------|-----------|---------|-------------|",
    ]

    for r in results.get("mann_whitney_weird", []):
        sig = "Yes" if r["significant_bh_fdr"] else "No"
        lines.append(
            f"| {r['framework']} | {r['high_weird_mean']} | {r['non_weird_mean']} | "
            f"{r['cohens_d']:+.3f} | {r['p_value']:.4f} | {sig} |"
        )

    lines.extend([
        "",
        "## 2. Kruskal-Wallis: Global North vs South vs Ambiguous",
        "",
        "| Framework | North Mean | South Mean | Ambiguous Mean | η² | p-value | Sig |",
        "|-----------|-----------|-----------|---------------|-----|---------|-----|",
    ])

    for r in results.get("kruskal_wallis_ns", []):
        sig = "Yes" if r["significant_bh_fdr"] else "No"
        gm = r["group_means"]
        lines.append(
            f"| {r['framework']} | {gm.get('Global North', 0)} | {gm.get('Global South', 0)} | "
            f"{gm.get('Ambiguous', 0)} | {r['eta_squared']:.4f} | {r['p_value']:.4f} | {sig} |"
        )

    chi = results.get("chi_square_region_framework", {})
    if chi:
        lines.extend([
            "",
            "## 3. Chi-Square: Region × Framework Detection",
            "",
            f"- χ² = {chi['chi2']}, df = {chi['dof']}, p = {chi['p_value']}",
            f"- Cramér's V = {chi['cramers_v']} ({chi['effect_size']} effect)",
            "",
        ])

    lines.extend([
        "",
        "## 4. Bootstrap Confidence Intervals",
        "",
        "95% CIs for regional mean framework scores (1000 iterations).",
        "",
    ])

    for region, data in results.get("bootstrap_cis", {}).items():
        lines.append(f"### {region} (n={data['n']})")
        lines.append("")
        lines.append("| Framework | Mean | 95% CI |")
        lines.append("|-----------|------|--------|")
        for fw, ci in data["framework_cis"].items():
            if ci["mean"] > 0.5:  # Only show non-trivial
                lines.append(f"| {fw} | {ci['mean']} | [{ci['ci_lower']}, {ci['ci_upper']}] |")
        lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    sys.exit(main())
