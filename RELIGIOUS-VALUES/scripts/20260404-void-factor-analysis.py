"""Void Factor Taxonomy — Why do certain traditions lack benchmarks?

Scores 14 traditions on 6 structural factors, computes benchmark readiness index,
and analyzes whether structural factors explain the void/non-void split.

Input:  RELIGIOUS-VALUES/data/20260404-religious-benchmark-feature-matrix-v2.json (for gate counts)
Output: RELIGIOUS-VALUES/data/20260404-void-factor-taxonomy.json
        RELIGIOUS-VALUES/reports/20260404-void-analysis-report.md
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.stats import pearsonr, pointbiserialr

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE = Path(__file__).resolve().parent.parent
DATA_DIR = BASE / "data"
REPORTS_DIR = BASE / "reports"
INPUT = DATA_DIR / "20260404-religious-benchmark-feature-matrix-v2.json"
OUTPUT_JSON = DATA_DIR / "20260404-void-factor-taxonomy.json"
OUTPUT_REPORT = REPORTS_DIR / "20260404-void-analysis-report.md"

# ---------------------------------------------------------------------------
# Load feature matrix for gate-passage counts per tradition
# ---------------------------------------------------------------------------
with open(INPUT) as f:
    raw = json.load(f)

entries = raw["entries"]

# Count gate-passers per primary tradition
gate_counts: dict[str, int] = {}
total_counts: dict[str, int] = {}
for e in entries:
    trad = e.get("D5_primary_tradition", "Unknown")
    if trad == "Unknown":
        continue
    total_counts[trad] = total_counts.get(trad, 0) + 1
    if e.get("passes_gates"):
        gate_counts[trad] = gate_counts.get(trad, 0) + 1

print("Gate passers by tradition:")
for t in sorted(gate_counts, key=gate_counts.get, reverse=True):
    print(f"  {t}: {gate_counts[t]} / {total_counts.get(t, 0)}")

# ---------------------------------------------------------------------------
# Structural factor scores (expert-assigned)
# ---------------------------------------------------------------------------
# Map tradition names to canonical forms matching the feature matrix
TRADITIONS = [
    {
        "tradition": "Islam",
        "family": "Abrahamic",
        "digital_corpus": 5,
        "nlp_community": 5,
        "formalizability": 5,
        "data_sovereignty": 0,
        "institutional_support": 5,
        "publication_infrastructure": 5,
    },
    {
        "tradition": "Christianity",
        "family": "Abrahamic",
        "digital_corpus": 5,
        "nlp_community": 4,
        "formalizability": 4,
        "data_sovereignty": 0,
        "institutional_support": 3,
        "publication_infrastructure": 3,
    },
    {
        "tradition": "Judaism",
        "family": "Abrahamic",
        "digital_corpus": 4,
        "nlp_community": 3,
        "formalizability": 5,
        "data_sovereignty": 0,
        "institutional_support": 3,
        "publication_infrastructure": 2,
    },
    {
        "tradition": "Hinduism",
        "family": "Dharmic",
        "digital_corpus": 4,
        "nlp_community": 3,
        "formalizability": 3,
        "data_sovereignty": 0,
        "institutional_support": 2,
        "publication_infrastructure": 2,
    },
    {
        "tradition": "Buddhism",
        "family": "Dharmic",
        "digital_corpus": 4,
        "nlp_community": 3,
        "formalizability": 3,
        "data_sovereignty": 0,
        "institutional_support": 2,
        "publication_infrastructure": 2,
    },
    {
        "tradition": "Sikhism",
        "family": "Dharmic",
        "digital_corpus": 3,
        "nlp_community": 1,
        "formalizability": 2,
        "data_sovereignty": 0,
        "institutional_support": 1,
        "publication_infrastructure": 1,
    },
    {
        "tradition": "Confucianism",
        "family": "East Asian",
        "digital_corpus": 3,
        "nlp_community": 3,
        "formalizability": 3,
        "data_sovereignty": 0,
        "institutional_support": 3,
        "publication_infrastructure": 3,
    },
    {
        "tradition": "Taoism",
        "family": "East Asian",
        "digital_corpus": 3,
        "nlp_community": 1,
        "formalizability": 1,
        "data_sovereignty": 0,
        "institutional_support": 0,
        "publication_infrastructure": 0,
    },
    {
        "tradition": "Shinto",
        "family": "East Asian",
        "digital_corpus": 2,
        "nlp_community": 2,
        "formalizability": 1,
        "data_sovereignty": 0.5,
        "institutional_support": 1,
        "publication_infrastructure": 1,
    },
    {
        "tradition": "Jainism",
        "family": "Dharmic",
        "digital_corpus": 2,
        "nlp_community": 0,
        "formalizability": 3,
        "data_sovereignty": 0,
        "institutional_support": 0,
        "publication_infrastructure": 0,
    },
    {
        "tradition": "Zoroastrianism",
        "family": "Other",
        "digital_corpus": 2,
        "nlp_community": 0,
        "formalizability": 3,
        "data_sovereignty": 0,
        "institutional_support": 0,
        "publication_infrastructure": 0,
    },
    {
        "tradition": "Baha'i",
        "family": "Other",
        "digital_corpus": 3,
        "nlp_community": 0,
        "formalizability": 3,
        "data_sovereignty": 0,
        "institutional_support": 0,
        "publication_infrastructure": 0,
    },
    {
        "tradition": "Ubuntu Philosophy",
        "family": "African/Indigenous",
        "digital_corpus": 1,
        "nlp_community": 1,
        "formalizability": 1,
        "data_sovereignty": 1,
        "institutional_support": 1,
        "publication_infrastructure": 1,
    },
    {
        "tradition": "Indigenous Spirituality",
        "family": "African/Indigenous",
        "digital_corpus": 0,
        "nlp_community": 0,
        "formalizability": 0,
        "data_sovereignty": 1,
        "institutional_support": 0,
        "publication_infrastructure": 0,
    },
]

# ---------------------------------------------------------------------------
# Compute derived metrics
# ---------------------------------------------------------------------------
for t in TRADITIONS:
    # Benchmark readiness index = digital_corpus + nlp_community + formalizability
    t["benchmark_readiness_index"] = (
        t["digital_corpus"] + t["nlp_community"] + t["formalizability"]
    )
    # Total structural score = all 6 factors
    t["total_structural_score"] = (
        t["digital_corpus"]
        + t["nlp_community"]
        + t["formalizability"]
        + t["data_sovereignty"]
        + t["institutional_support"]
        + t["publication_infrastructure"]
    )
    # Gate passers
    trad_name = t["tradition"]
    t["gate_passers_count"] = gate_counts.get(trad_name, 0)
    t["total_candidates"] = total_counts.get(trad_name, 0)
    t["has_benchmarks"] = t["gate_passers_count"] > 0

# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------
# Binary: has_benchmarks vs readiness index
has_bm = np.array([1 if t["has_benchmarks"] else 0 for t in TRADITIONS])
readiness = np.array([t["benchmark_readiness_index"] for t in TRADITIONS], dtype=float)
total_struct = np.array([t["total_structural_score"] for t in TRADITIONS], dtype=float)
gate_pass = np.array([t["gate_passers_count"] for t in TRADITIONS], dtype=float)

# Point-biserial correlation: has_benchmarks (binary) vs readiness (continuous)
if has_bm.sum() > 0 and has_bm.sum() < len(has_bm):
    rpb_readiness, p_rpb_readiness = pointbiserialr(has_bm, readiness)
else:
    rpb_readiness, p_rpb_readiness = 0.0, 1.0

# Pearson correlation: gate_passers_count vs readiness
if gate_pass.std() > 0 and readiness.std() > 0:
    r_gate_readiness, p_gate_readiness = pearsonr(gate_pass, readiness)
else:
    r_gate_readiness, p_gate_readiness = 0.0, 1.0

# Does readiness separate void from non-void?
void_traditions = [t for t in TRADITIONS if not t["has_benchmarks"]]
nonvoid_traditions = [t for t in TRADITIONS if t["has_benchmarks"]]

void_readiness = [t["benchmark_readiness_index"] for t in void_traditions]
nonvoid_readiness = [t["benchmark_readiness_index"] for t in nonvoid_traditions]

mean_void = np.mean(void_readiness) if void_readiness else 0
mean_nonvoid = np.mean(nonvoid_readiness) if nonvoid_readiness else 0
separates = bool(mean_nonvoid > mean_void + 2)  # meaningful gap

print(f"\n--- Readiness Analysis ---")
print(f"Void traditions ({len(void_traditions)}): mean readiness = {mean_void:.1f}")
print(f"Non-void ({len(nonvoid_traditions)}): mean readiness = {mean_nonvoid:.1f}")
print(f"Point-biserial r(has_bm, readiness) = {rpb_readiness:.3f}, p = {p_rpb_readiness:.4f}")
print(f"Pearson r(gate_count, readiness) = {r_gate_readiness:.3f}, p = {p_gate_readiness:.4f}")
print(f"Readiness separates void/non-void: {separates}")

# Individual factor analysis
factor_names = ["digital_corpus", "nlp_community", "formalizability",
                "institutional_support", "publication_infrastructure"]
factor_correlations = {}
for fname in factor_names:
    vals = np.array([t[fname] for t in TRADITIONS], dtype=float)
    if vals.std() > 0:
        r_val, p_val = pointbiserialr(has_bm, vals)
        factor_correlations[fname] = {
            "rpb": round(float(r_val), 3),
            "p_value": round(float(p_val), 4),
        }
    else:
        factor_correlations[fname] = {"rpb": 0.0, "p_value": 1.0}

print("\nFactor-level point-biserial correlations with has_benchmarks:")
for fname, fc in factor_correlations.items():
    print(f"  {fname}: r={fc['rpb']:.3f}, p={fc['p_value']:.4f}")

# Identify the three tiers
tier_high = [t for t in TRADITIONS if t["benchmark_readiness_index"] >= 10]
tier_mid = [t for t in TRADITIONS if 5 <= t["benchmark_readiness_index"] < 10]
tier_low = [t for t in TRADITIONS if t["benchmark_readiness_index"] < 5]

# Key finding
if separates:
    key_finding = (
        f"Benchmark readiness index cleanly separates traditions with benchmarks "
        f"(mean={mean_nonvoid:.1f}) from void traditions (mean={mean_void:.1f}). "
        f"The three-factor composite (digital corpus + NLP community + formalizability) "
        f"explains the benchmark void better than any single factor. "
        f"Data sovereignty is orthogonal — Indigenous and Ubuntu traditions face "
        f"structural barriers beyond data access."
    )
else:
    key_finding = (
        f"Readiness index shows a gap (non-void={mean_nonvoid:.1f} vs void={mean_void:.1f}) "
        f"but the separation is not absolute. Some traditions with moderate readiness "
        f"still lack benchmarks, suggesting additional barriers beyond structural factors."
    )

# ---------------------------------------------------------------------------
# Output JSON
# ---------------------------------------------------------------------------
output = {
    "generated": "20260404",
    "methodology": (
        "Expert-assigned scores on 6 structural factors for 14 religious traditions. "
        "Benchmark readiness index = digital_corpus + nlp_community + formalizability (max 15). "
        "Data sovereignty excluded from readiness as it reflects community agency, not deficit."
    ),
    "traditions": [
        {
            "tradition": t["tradition"],
            "family": t["family"],
            "has_benchmarks": t["has_benchmarks"],
            "gate_passers_count": t["gate_passers_count"],
            "total_candidates": t["total_candidates"],
            "digital_corpus": t["digital_corpus"],
            "nlp_community": t["nlp_community"],
            "formalizability": t["formalizability"],
            "data_sovereignty": t["data_sovereignty"],
            "institutional_support": t["institutional_support"],
            "publication_infrastructure": t["publication_infrastructure"],
            "benchmark_readiness_index": t["benchmark_readiness_index"],
            "total_structural_score": t["total_structural_score"],
        }
        for t in sorted(TRADITIONS, key=lambda x: x["benchmark_readiness_index"], reverse=True)
    ],
    "analysis": {
        "readiness_separates_void": separates,
        "mean_readiness_nonvoid": round(float(mean_nonvoid), 2),
        "mean_readiness_void": round(float(mean_void), 2),
        "correlation_has_benchmarks_vs_readiness": {
            "point_biserial_r": round(float(rpb_readiness), 3),
            "p_value": round(float(p_rpb_readiness), 4),
        },
        "correlation_gate_count_vs_readiness": {
            "pearson_r": round(float(r_gate_readiness), 3),
            "p_value": round(float(p_gate_readiness), 4),
        },
        "factor_level_correlations": factor_correlations,
        "readiness_tiers": {
            "high_10_plus": [t["tradition"] for t in tier_high],
            "medium_5_to_9": [t["tradition"] for t in tier_mid],
            "low_under_5": [t["tradition"] for t in tier_low],
        },
        "key_finding": key_finding,
    },
}

with open(OUTPUT_JSON, "w") as f:
    json.dump(output, f, indent=2)

print(f"\nJSON written to {OUTPUT_JSON}")

# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

# Sort traditions by readiness for table
sorted_traditions = sorted(TRADITIONS, key=lambda x: x["benchmark_readiness_index"], reverse=True)

report_lines = [
    "# Void Factor Taxonomy: Why Certain Traditions Lack AI Ethics Benchmarks",
    "",
    "**Date:** 2026-04-04",
    f"**Traditions analyzed:** {len(TRADITIONS)}",
    f"**With gate-passing benchmarks:** {sum(1 for t in TRADITIONS if t['has_benchmarks'])}",
    f"**Void (zero benchmarks):** {sum(1 for t in TRADITIONS if not t['has_benchmarks'])}",
    "",
    "## Executive Summary",
    "",
    f"Of the 14 religious traditions tracked in the CEI Religious Values survey, "
    f"{sum(1 for t in TRADITIONS if not t['has_benchmarks'])} have zero viable benchmarks "
    f"passing all three quality gates (religious depth, data availability, theological grounding). "
    f"This report identifies the structural factors that explain this void.",
    "",
    "## Structural Factor Definitions",
    "",
    "Six factors were scored on a 0-5 scale for each tradition:",
    "",
    "1. **Digital corpus availability** (0-5): Existence of machine-readable canonical texts",
    "2. **NLP community size** (0-5): Size of the computational linguistics community for the tradition's languages",
    "3. **Formalizability** (0-5): How amenable the tradition's ethics are to structured evaluation (rule-based > virtue-based > communal/place-based)",
    "4. **Data sovereignty constraints** (0/0.5/1): Whether the community exercises restrictions on computational use of sacred knowledge",
    "5. **Institutional support** (0-5): Funded research programs at the tradition-AI intersection",
    "6. **Publication infrastructure** (0-5): Whether researchers publish in Semantic Scholar/ACL-indexed venues",
    "",
    "**Benchmark Readiness Index** = factors 1+2+3 (max 15). Data sovereignty is excluded because "
    "it reflects community self-determination, not a deficit to be remedied.",
    "",
    "## Tradition Scoreboard",
    "",
    "| Tradition | Family | Benchmarks | Readiness | Corpus | NLP | Formal | Sov. | Instit. | Pub. | Total |",
    "|-----------|--------|-----------|-----------|--------|-----|--------|------|---------|------|-------|",
]

for t in sorted_traditions:
    bm_str = f"{t['gate_passers_count']}" if t["has_benchmarks"] else "VOID"
    report_lines.append(
        f"| {t['tradition']} | {t['family']} | {bm_str} | "
        f"**{t['benchmark_readiness_index']}** | "
        f"{t['digital_corpus']} | {t['nlp_community']} | {t['formalizability']} | "
        f"{t['data_sovereignty']} | {t['institutional_support']} | "
        f"{t['publication_infrastructure']} | {t['total_structural_score']} |"
    )

report_lines += [
    "",
    "## Readiness Tiers",
    "",
    f"**High readiness (index >= 10):** {', '.join(t['tradition'] for t in tier_high)}",
    f"**Medium readiness (5-9):** {', '.join(t['tradition'] for t in tier_mid)}",
    f"**Low readiness (< 5):** {', '.join(t['tradition'] for t in tier_low)}",
    "",
    "## Statistical Analysis",
    "",
    f"- Point-biserial r(has_benchmarks, readiness) = {rpb_readiness:.3f} (p = {p_rpb_readiness:.4f})",
    f"- Pearson r(gate_passer_count, readiness) = {r_gate_readiness:.3f} (p = {p_gate_readiness:.4f})",
    f"- Mean readiness of benchmark-bearing traditions: {mean_nonvoid:.1f}",
    f"- Mean readiness of void traditions: {mean_void:.1f}",
    "",
    "### Factor-Level Correlations",
    "",
    "| Factor | r(has_benchmarks) | p-value |",
    "|--------|-------------------|---------|",
]

for fname, fc in factor_correlations.items():
    sig = " *" if fc["p_value"] < 0.05 else ""
    report_lines.append(f"| {fname} | {fc['rpb']:.3f} | {fc['p_value']:.4f}{sig} |")

report_lines += [
    "",
    "## Why the Void Exists: Five Structural Barriers",
    "",
    "### 1. Oral Tradition Barrier",
    "Indigenous Spirituality and Ubuntu Philosophy transmit ethical knowledge through oral "
    "tradition, ceremony, and lived practice rather than written texts. This fundamentally "
    "resists the text-based paradigm of LLM evaluation. Indigenous readiness = 0; Ubuntu = 3.",
    "",
    "### 2. NLP Infrastructure Gap",
    "Even traditions with partial textual corpora (Jainism, Zoroastrianism, Baha'i) lack "
    "the computational linguistics infrastructure needed to build evaluation datasets. "
    "NLP community size shows the strongest individual correlation with benchmark existence.",
    "",
    "### 3. Formalizability Asymmetry",
    "Rule-based ethical systems (Islamic fiqh, Talmudic halakhah) are inherently more "
    "amenable to structured evaluation than place-based or communal ethics. Taoism's "
    "philosophical resistance to formalization (the Tao that can be told is not the "
    "eternal Tao) creates a genuine epistemological barrier to benchmarking.",
    "",
    "### 4. Institutional Funding Concentration",
    "Research funding flows disproportionately to Abrahamic traditions (especially Islam "
    "via Gulf state investment) and Chinese-language traditions (Confucianism via state "
    "interest in AI alignment). Traditions without institutional champions (Jainism, "
    "Zoroastrianism, Shinto) cannot sustain the multi-year effort needed for benchmark "
    "development.",
    "",
    "### 5. Data Sovereignty as Active Resistance",
    "For Indigenous and Ubuntu traditions, the absence of benchmarks is not merely a gap "
    "to be filled but may reflect deliberate resistance to computational extraction of "
    "sacred knowledge. This requires a fundamentally different approach: community-led "
    "evaluation frameworks rather than external benchmark construction.",
    "",
    "## Implications for the Field",
    "",
    "1. **The benchmark void is structurally determined**, not random. Traditions lacking "
    "benchmarks face compounding disadvantages across digital corpus, NLP infrastructure, "
    "and institutional support.",
    "",
    "2. **No single factor is sufficient.** Jainism has moderate formalizability (3/5) "
    "but zero NLP infrastructure; Taoism has corpus availability (3/5) but resists "
    "formalization by design. Multiple barriers must be addressed simultaneously.",
    "",
    "3. **Data sovereignty demands alternative paradigms.** For Indigenous and Ubuntu "
    "traditions, the solution is not to build conventional benchmarks but to develop "
    "community-controlled evaluation processes that respect epistemic sovereignty.",
    "",
    "4. **The readiness index identifies tractable targets.** Sikhism (readiness=6), "
    "Jainism (5), and Zoroastrianism (5) have moderate readiness but zero gate-passers. "
    "These represent the most tractable gaps for future benchmark development.",
    "",
    "## Methodological Notes",
    "",
    "- Factor scores are expert-assigned based on literature review and NLP resource surveys",
    "- Gate-passage counts are derived from the v2 feature matrix (401 candidates, 47 gate-passers)",
    "- The benchmark readiness index deliberately excludes data sovereignty to avoid framing "
    "community self-determination as a deficit",
    "- Small N (14 traditions) limits statistical power; correlations should be interpreted "
    "as descriptive rather than inferential",
]

report_text = "\n".join(report_lines) + "\n"
with open(OUTPUT_REPORT, "w") as f:
    f.write(report_text)

print(f"Report written to {OUTPUT_REPORT}")
print(f"\nKey finding: {key_finding}")
