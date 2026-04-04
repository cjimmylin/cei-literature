#!/usr/bin/env python3
"""Generate data.js for the NormEval dashboard.

Reads all JSON data files from STATISTICS/ and pre-computes all chart data
structures, emitting DASHBOARD/data.js as JS constants.

Architecture: "fat data, thin client" — browser does zero computation.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

NORM_DIR = Path(__file__).resolve().parent.parent
STATS_DIR = NORM_DIR / "STATISTICS"
DASH_DIR = NORM_DIR / "DASHBOARD"


def load_json(name: str) -> dict | list:
    with open(STATS_DIR / name) as f:
        return json.load(f)


def build_data_js() -> str:
    # ── Load all sources ──────────────────────────────────────────────
    benchmarks = load_json("20260402-normative-benchmark-feature-matrix.json")
    v2_features = load_json("20260404-normeval-v2-feature-scores.json")
    corr = load_json("20260404-normeval-correlation-matrix.json")
    pca = load_json("20260404-normeval-pca-clusters.json")
    sensitivity = load_json("20260404-normeval-sensitivity-analysis.json")
    hypothesis = load_json("20260404-normeval-hypothesis-tests.json")
    temporal = load_json("20260404-normeval-temporal-trends.json")
    anomaly = load_json("20260404-normeval-anomaly-detection.json")
    data_avail = load_json("20260404-normeval-data-availability-audit.json")
    vault_mining = load_json("20260404-normeval-vault-mining-results.json")
    external = load_json("20260404-normeval-external-search-results.json")

    # ── Tab 1: Overview KPIs ──────────────────────────────────────────
    n_total = len(benchmarks)
    n_pass = sum(1 for b in benchmarks if b["passes_gates"])
    n_fail = n_total - n_pass

    # Gate fail reasons
    fail_nd = sum(1 for b in benchmarks if not b.get("gate_ND", True))
    fail_data = sum(1 for b in benchmarks if not b.get("gate_data", True))
    fail_both = sum(1 for b in benchmarks if not b.get("gate_ND", True) and not b.get("gate_data", True))

    traditions_set = ["virtue_ethics", "deontological_ethics", "utilitarian_ethics",
                      "care_ethics", "contractarian_ethics"]
    tradition_labels = ["Virtue", "Deontological", "Utilitarian", "Care", "Contractarian"]

    # Tradition frequency: how many benchmarks have tradition >= 50
    tradition_freq = []
    for t, label in zip(traditions_set, tradition_labels):
        count = sum(1 for b in benchmarks if b["A1_traditions"].get(t, 0) >= 50)
        tradition_freq.append({"name": label, "count": count})

    # 5 claims
    claims = [
        {
            "id": "C1",
            "title": "Ceiling Effect",
            "description": "Current benchmarks produce ceiling accuracy on frontier LLMs",
            "status": "Confirmed",
            "detail": f"Binomial test: p < 1e-15 (50/50 perfect on ETHICS). "
                      f"C1 p = {hypothesis['C1_ceiling']['p_value']:.2e}"
        },
        {
            "id": "C2",
            "title": "Utilitarian Bias",
            "description": "Benchmarks over-represent utilitarian frameworks vs deontological",
            "status": "Confirmed",
            "detail": f"Two-proportion z-test: z = {hypothesis['C2_bias']['z_statistic']:.2f}, "
                      f"p = {hypothesis['C2_bias']['p_value']:.4f}, Cohen's h = {hypothesis['C2_bias']['cohens_h']:.2f}"
        },
        {
            "id": "C3",
            "title": "Care/Contractarian Void",
            "description": "Care ethics and contractarian ethics have near-zero representation",
            "status": "Revised",
            "detail": f"Care as primary: {hypothesis['C3_void']['care_as_primary']}/37. "
                      f"Contractarian above 50: 1/37. Statistical test inconclusive (p = {hypothesis['C3_void']['p_never_primary']:.4f})"
        },
        {
            "id": "C4",
            "title": "Judgment-Only Testing",
            "description": "Most benchmarks test moral judgment, not moral reasoning process",
            "status": "Revised",
            "detail": f"Proportion testing judgment only: {hypothesis['C4_judgment']['proportion']:.1%} "
                      f"(p = {hypothesis['C4_judgment']['p_value']:.3f}, not significant)"
        },
        {
            "id": "C5",
            "title": "Data Bottleneck",
            "description": "Data unavailability prevents replication of high-ND benchmarks",
            "status": "Challenged",
            "detail": f"Mann-Whitney U: no significant ND difference between available and unavailable "
                      f"(p = {hypothesis['C5_bottleneck']['p_value']:.3f})"
        }
    ]

    # v2 feature summary stats
    e1_scored = [v.get("E1_discriminative_power") for v in v2_features if v.get("E1_discriminative_power") is not None]
    a10_single = sum(1 for v in v2_features if v.get("A10_temporal_depth", 0) == 25)
    b10_high = sum(1 for v in v2_features if (v.get("B10_contamination_risk") or 0) >= 67)
    nw_any = sum(1 for v in v2_features if any(val > 0 for val in v.get("A1_plus_non_western", {}).values()))

    overview = {
        "n_total": n_total,
        "n_pass": n_pass,
        "n_fail": n_fail,
        "n_traditions": 5,
        "n_features": 26,
        "fail_reasons": {
            "nd_only": fail_nd - fail_both,
            "data_only": fail_data - fail_both,
            "both": fail_both
        },
        "claims": claims,
        "tradition_freq": tradition_freq,
        "v2_highlights": {
            "e1_avg": round(sum(e1_scored) / len(e1_scored), 1) if e1_scored else 0,
            "e1_count": len(e1_scored),
            "a10_single_turn": a10_single,
            "a10_total": len(v2_features),
            "b10_high_risk": b10_high,
            "nw_engaged": nw_any,
        }
    }

    # ── Build v2 feature lookup by id ──────────────────────────────────
    v2_by_id = {v["id"]: v for v in v2_features}

    # ── Tab 2: All Papers Ranking ─────────────────────────────────────
    # Sort by composite descending
    sorted_benchmarks = sorted(benchmarks, key=lambda b: b["COMPOSITE"], reverse=True)
    papers_table = []
    for rank, b in enumerate(sorted_benchmarks, 1):
        traditions_dots = []
        for t, label in zip(traditions_set, tradition_labels):
            val = b["A1_traditions"].get(t, 0)
            traditions_dots.append({"name": label, "score": val, "active": val >= 50})

        # v2 feature data for this benchmark
        v2 = v2_by_id.get(b["id"], {})
        e1 = v2.get("E1_discriminative_power")
        e1_rat = v2.get("E1_rationale", "")
        b10 = v2.get("B10_contamination_risk")
        a10 = v2.get("A10_temporal_depth")
        a11 = v2.get("A11_scenario_realism")
        a1_nw = v2.get("A1_plus_non_western", {})
        nw_engaged = [k.replace("_", " ").title() for k, v in a1_nw.items() if v > 0]

        papers_table.append({
            "rank": rank,
            "id": b["id"],
            "short_title": b["short_title"],
            "year": b["year"],
            "nd": b["ND_score"],
            "pe": b["PE_score"],
            "ci": b["CI_score"],
            "composite": b["COMPOSITE"],
            "passes_gates": b["passes_gates"],
            "gate_nd": b.get("gate_ND", False),
            "gate_data": b.get("gate_data", False),
            "traditions": traditions_dots,
            "size": b["B2_dataset_size"],
            "format": b["B1_format"],
            "a6": b["A6_grounding"],
            "depth": b.get("A2_depth", ""),
            "reasoning": b.get("A3_reasoning", ""),
            "uncertainty": b.get("A4_uncertainty", ""),
            "pluralism": b.get("A5_pluralism", ""),
            "domain": b.get("D2_domain", ""),
            "venue": b.get("C3_venue", ""),
            "venue_tier": b.get("C3_venue_tier", ""),
            "citations": b.get("C1_citation_count", 0),
            "license": b.get("B5_license", ""),
            "availability": b.get("B3_data_availability", ""),
            "rationale": b.get("normative_depth_rationale", ""),
            "cultural": b.get("A7_cultural", ""),
            "languages": b.get("A8_multilingual", {}).get("languages", []),
            "scorer_type": b.get("B8_scorer_type", ""),
            "annotators": b.get("D4_annotators", ""),
            "implementability": b.get("B7_implementability", 0),
            # v2 feature highlights
            "e1_discriminative": e1,
            "e1_rationale": e1_rat,
            "b10_contamination": b10,
            "a10_temporal": a10,
            "a11_realism": a11,
            "nw_traditions": nw_engaged,
            "a9_metaethical": v2.get("A9_metaethical_stance", ""),
        })

    # ── Tab 3: Feature Matrix ─────────────────────────────────────────
    # Heatmap data: rows = benchmarks, columns = key features
    feature_cols = [
        {"key": "A1_count", "label": "Traditions", "axis": "ND"},
        {"key": "A6_grounding", "label": "Grounding", "axis": "ND"},
        {"key": "ND_score", "label": "ND Score", "axis": "ND"},
        {"key": "B2_dataset_size_log", "label": "Size (log)", "axis": "PE"},
        {"key": "B7_implementability", "label": "Implement.", "axis": "PE"},
        {"key": "PE_score", "label": "PE Score", "axis": "PE"},
        {"key": "C1_citation_count_log", "label": "Citations (log)", "axis": "CI"},
        {"key": "C4_downstream_adoption", "label": "Adoption", "axis": "CI"},
        {"key": "CI_score", "label": "CI Score", "axis": "CI"},
    ]

    import math
    heatmap_data = []
    heatmap_names = []
    for b in sorted_benchmarks:
        row = []
        for col in feature_cols:
            key = col["key"]
            if key == "B2_dataset_size_log":
                raw = b.get("B2_dataset_size") or 1
                val = round(math.log10(max(raw, 1)), 2)
            elif key == "C1_citation_count_log":
                raw = b.get("C1_citation_count") or 1
                val = round(math.log10(max(raw, 1)), 2)
            else:
                val = b.get(key, 0)
                if val is None:
                    val = 0
            row.append(val)
        heatmap_data.append(row)
        heatmap_names.append(b["short_title"][:40])

    feature_matrix = {
        "columns": [c["label"] for c in feature_cols],
        "column_axes": [c["axis"] for c in feature_cols],
        "row_names": heatmap_names,
        "data": heatmap_data,
        "passes_gates": [b["passes_gates"] for b in sorted_benchmarks]
    }

    # ── Tab 4: Tradition Coverage ─────────────────────────────────────
    tradition_heatmap = []
    tradition_benchmark_names = []
    tradition_entropies = []
    for b in sorted_benchmarks:
        row = [b["A1_traditions"].get(t, 0) for t in traditions_set]
        tradition_heatmap.append(row)
        tradition_benchmark_names.append(b["short_title"][:40])
        # Shannon entropy
        scores = [max(v / 100.0, 0.001) for v in row]
        total = sum(scores)
        probs = [s / total for s in scores]
        entropy = -sum(p * math.log2(p) for p in probs if p > 0)
        tradition_entropies.append(round(entropy, 3))

    tradition_coverage = {
        "traditions": tradition_labels,
        "benchmark_names": tradition_benchmark_names,
        "heatmap": tradition_heatmap,
        "entropies": tradition_entropies,
        "frequency": tradition_freq,
        "passes_gates": [b["passes_gates"] for b in sorted_benchmarks]
    }

    # ── Tab 5: Composite Scoring ──────────────────────────────────────
    scatter_data = []
    for b in sorted_benchmarks:
        scatter_data.append({
            "name": b["short_title"][:40],
            "nd": b["ND_score"],
            "pe": b["PE_score"],
            "ci": b["CI_score"],
            "composite": b["COMPOSITE"],
            "passes": b["passes_gates"]
        })

    # Sensitivity: stable vs never in top 15
    stable_names = [s["name"][:40] for s in sensitivity["stable_always_top15"]]
    never_names = [s["name"][:40] for s in sensitivity["never_top15"]]
    borderline_names = [s["name"][:40] for s in sensitivity.get("borderline", [])]

    # Gate threshold sensitivity
    gate_sens = {}
    for key in ["ND_gate_30", "ND_gate_35", "ND_gate_40", "ND_gate_45", "ND_gate_50"]:
        if key in sensitivity.get("gate_threshold_sensitivity", {}):
            gate_sens[key] = sensitivity["gate_threshold_sensitivity"][key]["passing_count"]

    composite_scoring = {
        "scatter": scatter_data,
        "weights": sensitivity["current_weights"],
        "stable": stable_names,
        "never": never_names,
        "borderline": borderline_names,
        "weight_triplets_tested": sensitivity["weight_triplets_tested"],
        "gate_threshold": gate_sens,
        "nd_pe_regression": pca.get("nd_pe_regression", {})
    }

    # ── Tab 6: Implementation Trials ──────────────────────────────────
    # Extract from trial reports — hardcoded key metrics from reports
    trials = [
        {"id": "T1", "name": "ETHICS", "accuracy": 100, "items": 100, "framework_difficulty": "Easy",
         "discriminative": 0, "refusal_rate": 0, "notes": "Ceiling effect on expanded 100 items"},
        {"id": "T2", "name": "MoReBench", "accuracy": 78, "items": 30, "framework_difficulty": "Hard",
         "discriminative": 72, "refusal_rate": 0, "notes": "Theory subsection most challenging"},
        {"id": "T3", "name": "MoralReason", "accuracy": 85, "items": 100, "framework_difficulty": "Medium",
         "discriminative": 55, "refusal_rate": 2, "notes": "Expanded: U>V>D difficulty hierarchy"},
        {"id": "T4", "name": "MoralLens", "accuracy": 88, "items": 30, "framework_difficulty": "Medium",
         "discriminative": 45, "refusal_rate": 0, "notes": "Consequentialist vs deontological"},
        {"id": "T5", "name": "DailyDilemmas", "accuracy": 82, "items": 30, "framework_difficulty": "Hard",
         "discriminative": 60, "refusal_rate": 5, "notes": "Value preference alignment"},
        {"id": "T6", "name": "PrinciplismQA", "accuracy": 76, "items": 30, "framework_difficulty": "Hard",
         "discriminative": 68, "refusal_rate": 0, "notes": "Medical ethics domain-specific"},
        {"id": "T7", "name": "MoralPersuasion", "accuracy": 91, "items": 30, "framework_difficulty": "Easy",
         "discriminative": 30, "refusal_rate": 0, "notes": "Persuasion detection"},
        {"id": "T8", "name": "AMAEval", "accuracy": 73, "items": 30, "framework_difficulty": "Hard",
         "discriminative": 75, "refusal_rate": 3, "notes": "Professional medical ethics"},
        {"id": "T9", "name": "JETHICS", "accuracy": 87, "items": 30, "framework_difficulty": "Medium",
         "discriminative": 40, "refusal_rate": 0, "notes": "Japanese ethics cross-cultural"},
        {"id": "T10", "name": "PluralMoralGap", "accuracy": 79, "items": 30, "framework_difficulty": "Hard",
         "discriminative": 65, "refusal_rate": 8, "notes": "Pluralistic value alignment"},
        {"id": "T11", "name": "MedEthicsQA", "accuracy": 81, "items": 30, "framework_difficulty": "Medium",
         "discriminative": 50, "refusal_rate": 0, "notes": "Medical ethics QA"},
        {"id": "T12", "name": "UniMoral", "accuracy": 84, "items": 30, "framework_difficulty": "Medium",
         "discriminative": 48, "refusal_rate": 0, "notes": "Multilingual moral reasoning"},
        {"id": "T13", "name": "GreatestGood", "accuracy": 72, "items": 30, "framework_difficulty": "Hard",
         "discriminative": 70, "refusal_rate": 10, "notes": "Utilitarian tradeoffs"},
        {"id": "T14", "name": "CognitiveBiases", "accuracy": 90, "items": 22, "framework_difficulty": "Easy",
         "discriminative": 25, "refusal_rate": 0, "notes": "Bias amplification detection"},
        {"id": "T15", "name": "ProMoralBench", "accuracy": 80, "items": 30, "framework_difficulty": "Medium",
         "discriminative": 55, "refusal_rate": 0, "notes": "Prompting strategy evaluation"},
    ]

    # Framework difficulty distribution
    diff_dist = {"Easy": 0, "Medium": 0, "Hard": 0}
    for t in trials:
        diff_dist[t["framework_difficulty"]] += 1

    trial_data = {
        "trials": trials,
        "difficulty_distribution": diff_dist,
        "avg_accuracy": round(sum(t["accuracy"] for t in trials) / len(trials), 1),
        "avg_discriminative": round(sum(t["discriminative"] for t in trials) / len(trials), 1),
    }

    # ── Tab 7: Data Availability ──────────────────────────────────────
    audit_entries = data_avail.get("audit", data_avail) if isinstance(data_avail, dict) else data_avail
    if isinstance(audit_entries, dict):
        audit_entries = audit_entries.get("audit", [])

    host_counts = {}
    license_counts = {}
    for a in audit_entries:
        host = a.get("host_type", "Unknown")
        host_counts[host] = host_counts.get(host, 0) + 1
        lic = a.get("license", "Unspecified")
        license_counts[lic] = license_counts.get(lic, 0) + 1

    availability = {
        "host_distribution": [{"name": k, "count": v} for k, v in sorted(host_counts.items(), key=lambda x: -x[1])],
        "license_distribution": [{"name": k, "count": v} for k, v in sorted(license_counts.items(), key=lambda x: -x[1])],
        "entries": [
            {
                "name": a.get("name", ""),
                "host": a.get("host_type", "Unknown"),
                "license": a.get("license", "Unspecified"),
                "url": a.get("url", ""),
                "passes_gates": a.get("passes_gates", False),
                "gate_data": a.get("gate_data", False),
                "size": a.get("dataset_size", 0),
            }
            for a in audit_entries
        ]
    }

    # ── Tab 8: Cross-Model (placeholder) ──────────────────────────────
    cross_model = {
        "status": "pending",
        "message": "Cross-model replication pending. Requires GPT-4o, Llama-3, DeepSeek API keys.",
        "baseline": {
            "model": "Claude Opus 4.6",
            "trials_completed": 15,
            "avg_accuracy": trial_data["avg_accuracy"]
        }
    }

    # ── Tab 9: Gaps & Recommendations ─────────────────────────────────
    mining_include = [m for m in vault_mining if m.get("recommendation") == "INCLUDE"]
    mining_review = [m for m in vault_mining if m.get("recommendation") == "REVIEW"]
    external_add = [e for e in external if e.get("recommendation") == "ADD_TO_VAULT"]
    external_monitor = [e for e in external if e.get("recommendation") == "MONITOR"]

    # Care ethics prototype findings (from care-ethics-prototype.md)
    care_prototype = {
        "overall_score": "448/480 (93.3%)",
        "dimensions": [
            {"name": "Attentiveness", "mean": 3.97, "pct": 99.2},
            {"name": "Responsibility", "mean": 3.77, "pct": 94.2},
            {"name": "Competence", "mean": 3.53, "pct": 88.3},
            {"name": "Responsiveness", "mean": 3.67, "pct": 91.7},
        ],
        "key_insight": "The void is methodological, not philosophical. Care ethics evaluation is possible but requires multi-turn, rubric-scored formats structurally absent from all 37 benchmarks.",
        "competence_finding": "Competence (88.3%) is the most discriminative dimension -- the gap between noticing needs (attentiveness) and knowing what to do (competence) is where care-ethical benchmarks could differentiate models.",
        "scenarios": 10,
        "turns_per_scenario": 3,
        "categories": ["Healthcare", "Education", "Family", "Workplace", "Community"],
        "format": "Multi-turn dialogue with Tronto 4-dimension rubric (0-4 per dimension per turn)",
    }

    gaps = {
        "tradition_voids": [
            {"tradition": "Care Ethics", "count_above_50": tradition_freq[3]["count"],
             "status": "critical" if tradition_freq[3]["count"] <= 2 else "warning"},
            {"tradition": "Contractarian", "count_above_50": tradition_freq[4]["count"],
             "status": "critical" if tradition_freq[4]["count"] <= 2 else "warning"},
        ],
        "care_prototype": care_prototype,
        "vault_mining": {
            "total": len(vault_mining),
            "include": len(mining_include),
            "review": len(mining_review),
            "candidates": [
                {"filename": m.get("filename", ""), "reason": m.get("reason", ""), "recommendation": m["recommendation"]}
                for m in mining_include[:12]
            ]
        },
        "external_search": {
            "total": len(external),
            "add": len(external_add),
            "monitor": len(external_monitor),
            "candidates": [
                {"title": e.get("title", ""), "year": e.get("year", ""), "source": e.get("source", ""),
                 "recommendation": e["recommendation"], "reason": e.get("recommendation_reason", "")}
                for e in external_add
            ]
        },
        "peer_review_concerns": [
            {"concern": "Western-centric tradition coverage", "status": "acknowledged", "severity": "major"},
            {"concern": "Small sample size (n=37)", "status": "mitigated", "severity": "major"},
            {"concern": "Single-rater scoring reliability", "status": "acknowledged", "severity": "major"},
            {"concern": "Sensitivity to weight choice", "status": "resolved", "severity": "minor"},
            {"concern": "Temporal bias toward recent papers", "status": "acknowledged", "severity": "moderate"},
            {"concern": "Missing cross-model replication", "status": "pending", "severity": "major"},
        ]
    }

    # ── PCA data for composite tab ────────────────────────────────────
    pca_data = {
        "benchmarks": pca["pca_benchmarks"],
        "loadings": pca["loadings"],
        "cumulative_variance": pca["cumulative_variance"],
        "centroid_distance": pca["centroid_distance_top15_bottom22"],
    }

    # ── Temporal data ─────────────────────────────────────────────────
    temporal_data = {
        "year_distribution": temporal["year_distribution"],
        "trend_correlations": temporal["trend_correlations"],
        "benchmarks": temporal["benchmarks"],
    }

    # ── Correlation data ──────────────────────────────────────────────
    corr_data = {
        "features": corr["features"],
        "near_redundant": corr["near_redundant_pairs"],
        "anti_correlations": corr["anti_correlations"],
    }

    # ── Anomaly data ──────────────────────────────────────────────────
    anomaly_data = {
        "scores": anomaly["anomaly_scores"][:10],
    }

    # ── Assemble all data ─────────────────────────────────────────────
    all_data = {
        "overview": overview,
        "papers_table": papers_table,
        "feature_matrix": feature_matrix,
        "tradition_coverage": tradition_coverage,
        "composite_scoring": composite_scoring,
        "trial_data": trial_data,
        "availability": availability,
        "cross_model": cross_model,
        "gaps": gaps,
        "pca_data": pca_data,
        "temporal_data": temporal_data,
        "corr_data": corr_data,
        "anomaly_data": anomaly_data,
    }

    # ── Emit data.js ──────────────────────────────────────────────────
    lines = ["// NormEval Dashboard — data.js",
             "// Auto-generated by generate_normeval_dashboard.py",
             f"// Generated: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}",
             "// Architecture: fat data, thin client — browser does zero computation",
             ""]
    for key, value in all_data.items():
        js_name = "DATA_" + key.upper()
        lines.append(f"const {js_name} = {json.dumps(value, indent=2)};")
        lines.append("")

    return "\n".join(lines)


def main():
    DASH_DIR.mkdir(parents=True, exist_ok=True)
    content = build_data_js()
    out_path = DASH_DIR / "data.js"
    with open(out_path, "w") as f:
        f.write(content)
    print(f"Wrote {out_path} ({len(content):,} bytes)")


if __name__ == "__main__":
    main()
