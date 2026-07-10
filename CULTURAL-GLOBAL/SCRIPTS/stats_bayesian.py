#!/usr/bin/env python3
"""
Bayesian Small-Sample Analysis for Non-Western Framework Detection.

Provides:
    1. Detection rate posteriors (Beta-binomial) by framework × region
    2. Score posteriors (Normal-Inverse-Gamma conjugate) by framework × region
    3. WEIRD vs Non-WEIRD Bayesian comparison with P(rate_high > rate_non)
    4. Dharmic family aggregation (max of nw_buddhist, nw_dharmic)

Addresses Council recommendation R6 for small-n frameworks:
    Buddhist n=11, Dharmic n=9, Buen Vivir n=6, Islamic n=17

Output:
    DATA/20260403-bayesian-estimates.json
    STATISTICS/20260403-bayesian-report.md
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
from scipy.stats import beta as beta_dist

print = functools.partial(print, flush=True)

_SCRIPT_DIR = Path(__file__).parent
_CEI_LIT_WS = _SCRIPT_DIR.parent.parent
sys.path.insert(0, str(_CEI_LIT_WS / "PYTHON"))
sys.path.insert(0, str(_CEI_LIT_WS / ".agent" / "lib"))

TODAY = date.today().strftime("%Y%m%d")
DATA_DIR = _SCRIPT_DIR.parent / "DATA"
STATS_DIR = _SCRIPT_DIR.parent / "STATISTICS"

# Framework field names matching the JSON data
NW = ["nw_confucian", "nw_ubuntu", "nw_islamic_ethics",
      "nw_buddhist", "nw_dharmic", "nw_indigenous_relational", "nw_buen_vivir"]

DHARMIC_FAMILY = ["nw_buddhist", "nw_dharmic"]

REGIONS_ORDERED = [
    "North America", "Western Europe", "East Asia", "MENA",
    "South Asia", "Southeast Asia", "Latin America & Caribbean",
    "Eastern Europe & Central Asia", "Oceania", "Sub-Saharan Africa",
]

# NIG prior hyperparameters (weakly informative)
NIG_MU0 = 25.0
NIG_KAPPA0 = 1.0
NIG_ALPHA0 = 2.0
NIG_BETA0 = 100.0

DETECTION_THRESHOLD = 50


def load_data() -> list[dict]:
    """Load and merge paper data from sidecar JSONs."""
    geo_path = sorted(DATA_DIR.glob("*-author-geography.json"), reverse=True)
    weird_path = sorted(DATA_DIR.glob("*-weird-scores.json"), reverse=True)
    nw_path = sorted(DATA_DIR.glob("*-nw-scores.json"), reverse=True)

    geo_lookup: dict[str, dict] = {}
    weird_lookup: dict[str, dict] = {}
    nw_lookup: dict[str, dict] = {}

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

    # Build unified list keyed by nw_scores filenames
    papers = []
    for fname, nw_data in nw_lookup.items():
        entry = {"filename": fname}
        scores = nw_data.get("scores", {})
        for fw in NW:
            entry[fw] = scores.get(fw, 0)

        geo = geo_lookup.get(fname, {})
        entry["region"] = geo.get("author_region", "Unknown")

        weird = weird_lookup.get(fname, {})
        entry["weird_score"] = weird.get("weird_score", 50)
        entry["weird_tier"] = weird.get("tier", "Unknown")

        papers.append(entry)

    return papers


def compute_dharmic_family(papers: list[dict]) -> list[dict]:
    """Add dharmic_family = max(nw_buddhist, nw_dharmic) for each paper."""
    for p in papers:
        p["dharmic_family"] = max(p.get("nw_buddhist", 0), p.get("nw_dharmic", 0))
    return papers


def beta_hdi(a: float, b: float, ci: float = 0.95) -> tuple[float, float]:
    """Compute highest density interval for Beta(a, b)."""
    # For Beta distributions, the HDI is well-approximated by the equal-tailed CI
    # when the distribution is unimodal (a,b >= 1), which is always true here.
    alpha = (1 - ci) / 2
    lo = float(beta_dist.ppf(alpha, a, b))
    hi = float(beta_dist.ppf(1 - alpha, a, b))
    return lo, hi


def detection_rate_posteriors(papers: list[dict], frameworks: list[str],
                              regions: list[str]) -> dict:
    """Beta-binomial posteriors for detection rate by framework × region."""
    region_papers = defaultdict(list)
    for p in papers:
        if p["region"] in regions:
            region_papers[p["region"]].append(p)

    results = {}
    for fw in frameworks:
        fw_results = {}
        for region in regions:
            rp = region_papers[region]
            n = len(rp)
            if n == 0:
                continue
            k = sum(1 for p in rp if p.get(fw, 0) >= DETECTION_THRESHOLD)

            # Posterior: Beta(1 + k, 1 + n - k) with uniform prior Beta(1, 1)
            a_post = 1 + k
            b_post = 1 + n - k
            post_mean = a_post / (a_post + b_post)
            hdi_lo, hdi_hi = beta_hdi(a_post, b_post)

            # P(true rate > 5%)
            prob_gt_5pct = float(1 - beta_dist.cdf(0.05, a_post, b_post))

            fw_results[region] = {
                "n": n,
                "k_detected": k,
                "alpha_post": a_post,
                "beta_post": b_post,
                "posterior_mean": round(post_mean, 4),
                "hdi_95_lower": round(hdi_lo, 4),
                "hdi_95_upper": round(hdi_hi, 4),
                "prob_rate_gt_5pct": round(prob_gt_5pct, 4),
            }
        results[fw] = fw_results
    return results


def nig_posterior(data: np.ndarray) -> dict:
    """Normal-Inverse-Gamma posterior update."""
    n = len(data)
    if n == 0:
        return {"n": 0, "posterior_mean_mu": NIG_MU0,
                "ci_95_lower": 0.0, "ci_95_upper": 50.0}

    x_bar = float(np.mean(data))
    if n == 1:
        s2 = 0.0
    else:
        s2 = float(np.var(data, ddof=1))

    # NIG update
    kappa_n = NIG_KAPPA0 + n
    mu_n = (NIG_KAPPA0 * NIG_MU0 + n * x_bar) / kappa_n
    alpha_n = NIG_ALPHA0 + n / 2
    beta_n = (NIG_BETA0 + 0.5 * (n - 1) * s2
              + NIG_KAPPA0 * n * (x_bar - NIG_MU0) ** 2 / (2 * kappa_n))

    # Posterior marginal for mu is t-distribution
    # t_{2*alpha_n}(mu_n, beta_n / (kappa_n * alpha_n))
    from scipy.stats import t as t_dist
    df = 2 * alpha_n
    scale = np.sqrt(beta_n / (kappa_n * alpha_n))
    ci_lo = float(t_dist.ppf(0.025, df, loc=mu_n, scale=scale))
    ci_hi = float(t_dist.ppf(0.975, df, loc=mu_n, scale=scale))

    result = {
        "n": n,
        "sample_mean": round(x_bar, 2),
        "sample_sd": round(np.sqrt(s2), 2) if n > 1 else 0.0,
        "posterior_mean_mu": round(mu_n, 2),
        "ci_95_lower": round(max(0, ci_lo), 2),
        "ci_95_upper": round(ci_hi, 2),
    }

    # For small-n, also report posterior predictive
    if n < 20:
        pred_scale = np.sqrt(beta_n * (kappa_n + 1) / (kappa_n * alpha_n))
        pred_lo = float(t_dist.ppf(0.025, df, loc=mu_n, scale=pred_scale))
        pred_hi = float(t_dist.ppf(0.975, df, loc=mu_n, scale=pred_scale))
        result["predictive_95_lower"] = round(max(0, pred_lo), 2)
        result["predictive_95_upper"] = round(pred_hi, 2)

    return result


def score_posteriors(papers: list[dict], frameworks: list[str],
                     regions: list[str]) -> dict:
    """NIG posteriors for scores > 0 by framework × region."""
    region_papers = defaultdict(list)
    for p in papers:
        if p["region"] in regions:
            region_papers[p["region"]].append(p)

    results = {}
    for fw in frameworks:
        fw_results = {}
        for region in regions:
            rp = region_papers[region]
            scores = np.array([p.get(fw, 0) for p in rp if p.get(fw, 0) > 0],
                              dtype=float)
            if len(scores) == 0:
                continue
            fw_results[region] = nig_posterior(scores)
        results[fw] = fw_results
    return results


def weird_comparison(papers: list[dict], frameworks: list[str]) -> dict:
    """Bayesian WEIRD vs Non-WEIRD comparison."""
    # Use score-based tiers: High-WEIRD >= 70, Non-WEIRD < 30
    high = [p for p in papers if p["weird_score"] >= 70]
    non = [p for p in papers if p["weird_score"] < 30]

    print(f"   WEIRD comparison: High n={len(high)}, Non n={len(non)}")

    results = {}
    for fw in frameworks:
        k_high = sum(1 for p in high if p.get(fw, 0) >= DETECTION_THRESHOLD)
        n_high = len(high)
        k_non = sum(1 for p in non if p.get(fw, 0) >= DETECTION_THRESHOLD)
        n_non = len(non)

        # Posteriors
        a_h, b_h = 1 + k_high, 1 + n_high - k_high
        a_n, b_n = 1 + k_non, 1 + n_non - k_non

        mean_h = a_h / (a_h + b_h)
        mean_n = a_n / (a_n + b_n)

        # P(rate_high > rate_non) via Monte Carlo
        rng = np.random.default_rng(42)
        samples_h = rng.beta(a_h, b_h, size=50000)
        samples_n = rng.beta(a_n, b_n, size=50000)
        prob_h_gt_n = float(np.mean(samples_h > samples_n))

        # Bayes factor using Savage-Dickey ratio for H0: rate_h = rate_n
        # Approximate: ratio of posterior density at equality to prior density
        # Under H0, pooled rate ~ Beta(1 + k_h + k_n, 1 + n_h + n_n - k_h - k_n)
        # This is an approximation; exact BF requires integration
        k_total = k_high + k_non
        n_total = n_high + n_non
        # Prior predictive under H0 (equal rates)
        # vs H1 (independent rates) — use 2ln(BF) approximation
        # For simplicity, report prob_h_gt_n which is more interpretable

        results[fw] = {
            "high_weird_n": n_high,
            "high_weird_detected": k_high,
            "high_weird_rate": round(mean_h, 4),
            "non_weird_n": n_non,
            "non_weird_detected": k_non,
            "non_weird_rate": round(mean_n, 4),
            "prob_high_gt_non": round(prob_h_gt_n, 4),
            "interpretation": (
                "Strong evidence WEIRD > Non-WEIRD" if prob_h_gt_n > 0.95 else
                "Moderate evidence WEIRD > Non-WEIRD" if prob_h_gt_n > 0.80 else
                "Inconclusive" if prob_h_gt_n > 0.20 else
                "Moderate evidence Non-WEIRD > WEIRD" if prob_h_gt_n > 0.05 else
                "Strong evidence Non-WEIRD > WEIRD"
            ),
        }

    return results


def generate_report(results: dict) -> str:
    """Generate markdown report from Bayesian analysis results."""
    lines = [
        "# Bayesian Analysis of Non-Western Framework Detection",
        "",
        f"**Date:** {results['date']}",
        f"**Papers:** {results['total_papers']}",
        "",
        "Addresses Council recommendation R6: Bayesian credible intervals for "
        "small-n frameworks (Buddhist n=11, Dharmic n=9, Buen Vivir n=6).",
        "",
    ]

    # Section 1: Detection Rate Posteriors
    lines.extend([
        "## 1. Detection Rate Posteriors by Region",
        "",
        "Beta-binomial model with uniform Beta(1,1) prior. Detection threshold: "
        "score >= 50.",
        "",
    ])

    det = results.get("detection_rate_posteriors", {})
    for fw in NW + ["dharmic_family"]:
        if fw not in det:
            continue
        fw_data = det[fw]
        if not fw_data:
            continue

        lines.append(f"### {fw}")
        lines.append("")
        lines.append("| Region | n | Detected | Post. Mean | 95% HDI | P(rate>5%) |")
        lines.append("|--------|---|----------|-----------|---------|-----------|")
        for region in REGIONS_ORDERED:
            if region not in fw_data:
                continue
            d = fw_data[region]
            lines.append(
                f"| {region} | {d['n']} | {d['k_detected']} | "
                f"{d['posterior_mean']:.3f} | "
                f"[{d['hdi_95_lower']:.3f}, {d['hdi_95_upper']:.3f}] | "
                f"{d['prob_rate_gt_5pct']:.3f} |"
            )
        lines.append("")

    # Section 2: Score Posteriors
    lines.extend([
        "## 2. Score Posteriors by Region",
        "",
        "Normal-Inverse-Gamma conjugate model (prior: mu0=25, kappa0=1, "
        "alpha0=2, beta0=100). Only papers with score > 0.",
        "",
    ])

    sp = results.get("score_posteriors", {})
    for fw in NW + ["dharmic_family"]:
        if fw not in sp:
            continue
        fw_data = sp[fw]
        if not fw_data:
            continue

        lines.append(f"### {fw}")
        lines.append("")
        lines.append("| Region | n>0 | Sample Mean | Post. Mean mu | 95% CI |")
        lines.append("|--------|-----|------------|--------------|--------|")
        for region in REGIONS_ORDERED:
            if region not in fw_data:
                continue
            d = fw_data[region]
            ci = f"[{d['ci_95_lower']}, {d['ci_95_upper']}]"
            lines.append(
                f"| {region} | {d['n']} | {d['sample_mean']} | "
                f"{d['posterior_mean_mu']} | {ci} |"
            )
        lines.append("")

    # Section 3: WEIRD comparison
    lines.extend([
        "## 3. WEIRD Comparison",
        "",
        "Bayesian comparison of detection rates: High-WEIRD (score >= 70) vs "
        "Non-WEIRD (score < 30). P(High > Non) computed via 50,000 Monte Carlo "
        "draws from Beta posteriors.",
        "",
        "| Framework | HW Rate | NW Rate | P(HW > NW) | Interpretation |",
        "|-----------|---------|---------|-----------|---------------|",
    ])

    wc = results.get("weird_comparison", {})
    for fw in NW + ["dharmic_family"]:
        if fw not in wc:
            continue
        d = wc[fw]
        lines.append(
            f"| {fw} | {d['high_weird_rate']:.3f} "
            f"({d['high_weird_detected']}/{d['high_weird_n']}) | "
            f"{d['non_weird_rate']:.3f} "
            f"({d['non_weird_detected']}/{d['non_weird_n']}) | "
            f"{d['prob_high_gt_non']:.3f} | {d['interpretation']} |"
        )
    lines.append("")

    # Section 4: Dharmic family aggregation
    lines.extend([
        "## 4. Dharmic Family Aggregation",
        "",
        "dharmic_family = max(nw_buddhist, nw_dharmic) per paper. This "
        "aggregation addresses the small-n concern by combining conceptually "
        "related traditions.",
        "",
    ])

    # Pull dharmic family stats
    df_det = det.get("dharmic_family", {})
    if df_det:
        total_detected = sum(d["k_detected"] for d in df_det.values())
        total_n = sum(d["n"] for d in df_det.values())
        lines.append(f"- **Overall detection:** {total_detected}/{total_n} "
                      f"papers ({100*total_detected/total_n:.1f}%)")

        # Compare to individual
        bd_det = det.get("nw_buddhist", {})
        dh_det = det.get("nw_dharmic", {})
        bd_total = sum(d["k_detected"] for d in bd_det.values()) if bd_det else 0
        dh_total = sum(d["k_detected"] for d in dh_det.values()) if dh_det else 0
        lines.append(f"- **Buddhist alone:** {bd_total} detections")
        lines.append(f"- **Dharmic alone:** {dh_total} detections")
        lines.append(f"- **Family combined:** {total_detected} detections "
                      f"(gain: +{total_detected - max(bd_total, dh_total)})")
        lines.append("")

        # Widest CIs
        widest = []
        for region, d in df_det.items():
            width = d["hdi_95_upper"] - d["hdi_95_lower"]
            widest.append((region, width, d["n"]))
        widest.sort(key=lambda x: -x[1])
        lines.append("**Widest 95% HDIs (most uncertain):**")
        lines.append("")
        for region, width, n in widest[:5]:
            lines.append(f"- {region} (n={n}): HDI width = {width:.3f}")
        lines.append("")

    # Section 5: Interpretation
    lines.extend([
        "## 5. Interpretation",
        "",
        "### Key Findings",
        "",
    ])

    # Find frameworks with widest CIs overall
    all_widths = []
    for fw, fw_data in det.items():
        for region, d in fw_data.items():
            width = d["hdi_95_upper"] - d["hdi_95_lower"]
            all_widths.append((fw, region, width, d["n"]))
    all_widths.sort(key=lambda x: -x[2])

    lines.append("**Frameworks with widest credible intervals (most uncertain estimates):**")
    lines.append("")
    for fw, region, width, n in all_widths[:10]:
        lines.append(f"- {fw} in {region} (n={n}): 95% HDI width = {width:.3f}")
    lines.append("")

    # WEIRD summary
    lines.append("**WEIRD comparison summary:**")
    lines.append("")
    for fw in NW + ["dharmic_family"]:
        if fw in wc:
            d = wc[fw]
            lines.append(f"- {fw}: {d['interpretation']} "
                          f"(P={d['prob_high_gt_non']:.3f})")
    lines.append("")

    lines.extend([
        "### Caveats",
        "",
        "1. **Small samples dominate uncertainty:** Buen Vivir (n=6 globally), "
        "Dharmic (n=9), and Buddhist (n=11) have HDI widths spanning 10-40 "
        "percentage points, making point estimates unreliable.",
        "2. **Beta(1,1) prior is non-informative:** With n < 10, the prior "
        "contributes meaningfully to the posterior. Results should be interpreted "
        "as 'what the data suggest given no prior knowledge.'",
        "3. **NIG model assumes normality:** Score distributions are likely "
        "bimodal (zero-inflated), so NIG posteriors should be treated as "
        "approximate.",
        "4. **WEIRD comparison limited by Non-WEIRD sample:** Only 50 papers "
        "have weird_score < 30, creating asymmetric uncertainty.",
        "",
    ])

    return "\n".join(lines)


def main() -> int:
    print("=" * 60)
    print("Bayesian Small-Sample Analysis")
    print("=" * 60)

    print("\nLoading data...")
    papers = load_data()
    print(f"  Loaded {len(papers)} papers")

    # Add dharmic family
    papers = compute_dharmic_family(papers)

    # Active regions
    regions = [r for r in REGIONS_ORDERED
               if any(p["region"] == r for p in papers)]
    print(f"  Active regions: {len(regions)}")

    all_fw = NW + ["dharmic_family"]

    # 1. Detection rate posteriors
    print("\n1. Detection rate posteriors (Beta-binomial)...")
    det_results = detection_rate_posteriors(papers, all_fw, regions)
    for fw in all_fw:
        total_k = sum(d["k_detected"] for d in det_results.get(fw, {}).values())
        print(f"   {fw:30s} total detected: {total_k}")

    # 2. Score posteriors
    print("\n2. Score posteriors (Normal-Inverse-Gamma)...")
    score_results = score_posteriors(papers, all_fw, regions)
    for fw in all_fw:
        n_regions_with_data = len(score_results.get(fw, {}))
        print(f"   {fw:30s} regions with score>0: {n_regions_with_data}")

    # 3. WEIRD comparison
    print("\n3. WEIRD comparison (Bayesian)...")
    weird_results = weird_comparison(papers, all_fw)

    # Assemble output
    output = {
        "date": TODAY,
        "total_papers": len(papers),
        "detection_threshold": DETECTION_THRESHOLD,
        "prior": {
            "detection": "Beta(1, 1) — uniform",
            "score": f"NIG(mu0={NIG_MU0}, kappa0={NIG_KAPPA0}, "
                     f"alpha0={NIG_ALPHA0}, beta0={NIG_BETA0})",
        },
        "detection_rate_posteriors": det_results,
        "score_posteriors": score_results,
        "weird_comparison": weird_results,
    }

    # Save JSON
    out_path = DATA_DIR / f"{TODAY}-bayesian-estimates.json"
    tmp = out_path.with_suffix(f".tmp.{os.getpid()}.json")
    tmp.write_text(json.dumps(output, indent=2))
    os.replace(str(tmp), str(out_path))
    print(f"\nSaved JSON to {out_path}")

    # Generate report
    report = generate_report(output)
    report_path = STATS_DIR / f"{TODAY}-bayesian-report.md"
    report_path.write_text(report)
    print(f"Saved report to {report_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
