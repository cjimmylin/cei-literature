"""Generate DATA_CROSS_VENDOR JavaScript constant for NormEval dashboard.

Reads the all-models comparison JSON and Opus baseline JSON,
produces DASHBOARD/data_cross_vendor.js with pre-computed analytics.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE = Path(__file__).resolve().parent.parent  # NORM-ETHICS/
COMPARISON_JSON = BASE / "COMPARISON" / "20260404-normeval-all-models-comparison.json"
OPUS_JSON = BASE / "STATISTICS" / "20260404-normeval-cross-model-comparison.json"
OUTPUT_JS = BASE / "DASHBOARD" / "data_cross_vendor.js"

# ---------------------------------------------------------------------------
# Model ordering (canonical)
# ---------------------------------------------------------------------------
MODEL_ORDER = [
    "claude-haiku-4-5",
    "claude-sonnet-4-6",
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-2.5-pro",
    "gemini-3.1-pro",
    "gpt-5 (Codex agent)",
    "gpt-5-mini (Codex agent)",
]

MODEL_META = [
    {"id": "claude-haiku-4-5",        "short": "Haiku",    "provider": "Anthropic", "color": "#a78bfa"},
    {"id": "claude-sonnet-4-6",       "short": "Sonnet",   "provider": "Anthropic", "color": "#c4b5fd"},
    {"id": "gemini-2.5-flash",        "short": "Gem-2.5F", "provider": "Google",    "color": "#5b8def"},
    {"id": "gemini-2.5-flash-lite",   "short": "Gem-2.5FL","provider": "Google",    "color": "#7ba8f5"},
    {"id": "gemini-2.5-pro",          "short": "Gem-2.5P", "provider": "Google",    "color": "#93bbf7"},
    {"id": "gemini-3.1-pro",          "short": "Gem-3.1P", "provider": "Google",    "color": "#aecef9"},
    {"id": "gpt-5 (Codex agent)",     "short": "GPT-5",    "provider": "OpenAI",    "color": "#4ecb71"},
    {"id": "gpt-5-mini (Codex agent)","short": "GPT-5m",   "provider": "OpenAI",    "color": "#7eda99"},
]

SHORT_LABELS = [m["short"] for m in MODEL_META]

PROVIDER_COLORS = {"Anthropic": "#a78bfa", "OpenAI": "#4ecb71", "Google": "#5b8def"}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _pair_key(a: str, b: str) -> str:
    """Build the pairwise key as it appears in the JSON."""
    return f"{a} vs {b}"


def _get_agreement(agg: dict, a: str, b: str) -> float:
    """Get agreement percent from aggregate dict, trying both orderings."""
    k1 = _pair_key(a, b)
    k2 = _pair_key(b, a)
    if k1 in agg:
        return agg[k1]["agreement_percent"]
    if k2 in agg:
        return agg[k2]["agreement_percent"]
    raise KeyError(f"Pair not found: {a} <-> {b}")


def _extract_number(val) -> float | None:
    """Extract first number from a value (string or numeric)."""
    if isinstance(val, (int, float)):
        return float(val)
    if isinstance(val, str):
        m = re.search(r"[\d.]+", val)
        if m:
            return float(m.group())
    return None


def _get_metric(trial_data: dict, model_id: str, metric_name: str) -> float | None:
    """Get a metric value for a specific model within a trial."""
    for entry in trial_data.get("models", []):
        if entry["model"] == model_id:
            return _extract_number(entry["metrics"].get(metric_name))
    return None


# ---------------------------------------------------------------------------
# Build heatmap (8x8 symmetric matrix)
# ---------------------------------------------------------------------------

def build_heatmap(agg: dict) -> dict:
    n = len(MODEL_ORDER)
    matrix = [[0.0] * n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 100.0
        for j in range(i + 1, n):
            val = _get_agreement(agg, MODEL_ORDER[i], MODEL_ORDER[j])
            matrix[i][j] = val
            matrix[j][i] = val
    return {"labels": SHORT_LABELS, "matrix": matrix}


# ---------------------------------------------------------------------------
# IH scaling (include Opus baseline)
# ---------------------------------------------------------------------------

def build_ih_scaling(comp: dict, opus: dict) -> dict:
    # Opus baseline from cross-model JSON
    opus_ih = opus["per_trial_summary"]["T13"]["IH_means"]["opus"]
    opus_ib = opus["per_trial_summary"]["T13"]["IB_means"]["opus"]

    models_list = ["Opus*"]
    providers = ["Anthropic"]
    ih_means = [opus_ih]
    ib_means = [opus_ib]

    t13 = comp["per_trial"]["T13"]
    for m in MODEL_META:
        mid = m["id"]
        ih = _get_metric(t13, mid, "IH_mean")
        ib = _get_metric(t13, mid, "IB_mean")
        models_list.append(m["short"])
        providers.append(m["provider"])
        ih_means.append(ih if ih is not None else 0.0)
        ib_means.append(ib if ib is not None else 0.0)

    return {
        "models": models_list,
        "providers": providers,
        "IH_means": ih_means,
        "IB_means": ib_means,
        "ref_philosopher_IH": 4.5,
        "ref_lay_IH": 3.1,
    }


# ---------------------------------------------------------------------------
# CBR rate (include Opus baseline)
# ---------------------------------------------------------------------------

def build_cbr_rate(comp: dict, opus: dict) -> dict:
    opus_cbr = opus["per_trial_summary"]["T14"]["CBR_rate_MD"]["opus"]

    models_list = ["Opus*"]
    providers = ["Anthropic"]
    cbr_percent = [opus_cbr]

    t14 = comp["per_trial"]["T14"]
    for m in MODEL_META:
        mid = m["id"]
        val = _get_metric(t14, mid, "CBR_rate_moral_dilemmas")
        models_list.append(m["short"])
        providers.append(m["provider"])
        cbr_percent.append(val if val is not None else 0.0)

    return {
        "models": models_list,
        "providers": providers,
        "cbr_percent": cbr_percent,
    }


# ---------------------------------------------------------------------------
# Knowledge vs Judgment — per-trial min/max agreement
# ---------------------------------------------------------------------------

def build_knowledge_judgment(comp: dict) -> dict:
    trial_info = [
        ("T6",  "PrinciplismQA",  "knowledge"),
        ("T9",  "JETHICS",        "knowledge"),
        ("T11", "MedEthicsQA",    "knowledge"),
        ("T15", "ProMoralBench",  "knowledge"),
        ("T8",  "AMAeval",        "mixed"),
        ("T12", "UniMoral",       "judgment"),
        ("T10", "Pluralistic Gap","judgment"),
        ("T13", "Greatest Good",  "judgment"),
        ("T14", "PNAS Biases",    "judgment"),
        ("T7",  "Persuasion",     "judgment"),
    ]

    trials_out = []
    for tid, name, ttype in trial_info:
        pw = comp["per_trial"][tid].get("pairwise_agreement", {})
        if not pw:
            trials_out.append({
                "id": tid, "name": name, "type": ttype,
                "min_agreement": 100.0, "max_agreement": 100.0,
            })
            continue
        percents = [v["agreement_percent"] for v in pw.values()]
        trials_out.append({
            "id": tid,
            "name": name,
            "type": ttype,
            "min_agreement": round(min(percents), 1),
            "max_agreement": round(max(percents), 1),
        })

    return {"trials": trials_out}


# ---------------------------------------------------------------------------
# Provider radar profiles
# ---------------------------------------------------------------------------

def build_provider_profiles(comp: dict, opus: dict) -> dict:
    """Build radar profiles for representative model per provider.

    Dimensions (all normalized 0-100):
      IH Acceptance:          (IH_mean - 1) / 6 * 100  (1-7 scale)
      CBR Rate:               already 0-100
      Persuasion Resistance:  100 - decision_change_rate
      Knowledge Acc.:         T6 mcq_accuracy (already 0-100)
      Kohlberg Stage:         (mean_stage - 1) / 5 * 100  (stages 1-6)
      Altruism Rate:          Altruistic_rate_collective (already 0-100)
    """
    dimensions = [
        "IH Acceptance", "CBR Rate", "Persuasion Resistance",
        "Knowledge Acc.", "Kohlberg Stage", "Altruism Rate",
    ]

    # Representative models: Sonnet for Anthropic, GPT-5 for OpenAI, gemini-2.5-flash for Google
    reps = {
        "Anthropic (Sonnet)": "claude-sonnet-4-6",
        "OpenAI (GPT-5)": "gpt-5 (Codex agent)",
        "Google (Gemini)": "gemini-2.5-flash",
    }

    profiles = {}
    for label, mid in reps.items():
        ih = _get_metric(comp["per_trial"]["T13"], mid, "IH_mean") or 0.0
        cbr = _get_metric(comp["per_trial"]["T14"], mid, "CBR_rate_moral_dilemmas") or 0.0
        dcr = _get_metric(comp["per_trial"]["T7"], mid, "decision_change_rate") or 0.0
        know = _get_metric(comp["per_trial"]["T6"], mid, "mcq_accuracy") or 0.0
        stage = _get_metric(comp["per_trial"]["T12"], mid, "mean_stage") or 0.0
        altruism = _get_metric(comp["per_trial"]["T14"], mid, "Altruistic_rate_collective") or 0.0

        profiles[label] = [
            round((ih - 1) / 6 * 100, 1),       # IH Acceptance
            round(cbr, 1),                        # CBR Rate
            round(100 - dcr, 1),                  # Persuasion Resistance
            round(know, 1),                        # Knowledge Acc.
            round((stage - 1) / 5 * 100, 1),     # Kohlberg Stage
            round(altruism, 1),                    # Altruism Rate
        ]

    return {"dimensions": dimensions, "profiles": profiles}


# ---------------------------------------------------------------------------
# Per-trial summary table
# ---------------------------------------------------------------------------

def build_per_trial(comp: dict) -> dict:
    trial_ids = ["T6", "T7", "T8", "T9", "T10", "T11", "T12", "T13", "T14", "T15"]
    trial_names = [
        "PrinciplismQA", "Persuasion", "AMAeval", "JETHICS",
        "Pluralistic Gap", "MedEthicsQA", "UniMoral",
        "Greatest Good", "PNAS Biases", "ProMoralBench",
    ]

    # Primary metric per trial
    metric_map = {
        "T6":  "mcq_accuracy",
        "T7":  "decision_change_rate",
        "T8":  "abductive_eval_mean",
        "T9":  "accuracy",
        "T10": "high_consensus_alignment",
        "T11": "mcq_accuracy",
        "T12": "mean_stage",
        "T13": "IH_mean",
        "T14": "CBR_rate_moral_dilemmas",
        "T15": "accuracy_zero_shot",
    }

    data = {}
    for tid in trial_ids:
        trial_data = comp["per_trial"][tid]
        row = {}
        for m in MODEL_META:
            val = _get_metric(trial_data, m["id"], metric_map[tid])
            if val is not None:
                row[m["short"]] = round(val, 1)
            else:
                row[m["short"]] = None
        data[tid] = row

    return {"trials": trial_ids, "trial_names": trial_names, "data": data}


# ---------------------------------------------------------------------------
# Findings cards
# ---------------------------------------------------------------------------

FINDINGS = [
    {
        "id": "F1", "title": "Three Ethical Profiles",
        "subtitle": "Conservative (GPT-5) -> Moderate (Sonnet) -> Permissive (Haiku/Gemini) gradient across vendors",
        "badge": "Cross-Vendor",
    },
    {
        "id": "F2", "title": "Gemini Identity",
        "subtitle": "All 4 Google models produce identical responses on 114/114 items",
        "badge": "Anomaly",
    },
    {
        "id": "F3", "title": "Universal Knowledge Ceiling",
        "subtitle": "8/8 models score 100% on factual ethics (T6/T9/T11/T15)",
        "badge": "Ceiling",
    },
    {
        "id": "F4", "title": "Knowledge-Judgment Divergence",
        "subtitle": "100% agreement on knowledge vs 57-100% on judgment across vendors",
        "badge": "Construct",
    },
    {
        "id": "F5", "title": "GPT-5 Most Conservative",
        "subtitle": "IH=2.93 below even Opus (3.0) — strongest deontological constraints",
        "badge": "OpenAI",
    },
    {
        "id": "F6", "title": "Cross-Vendor Agreement",
        "subtitle": "Sonnet <-> GPT-5 = 90.4% > Sonnet <-> Haiku = 74.6%",
        "badge": "Agreement",
    },
    {
        "id": "F7", "title": "Persuasion Resistance",
        "subtitle": "Sonnet + both GPTs resist; Haiku + all Gemini susceptible",
        "badge": "Safety",
    },
]


# ---------------------------------------------------------------------------
# KPIs
# ---------------------------------------------------------------------------

def build_kpis(agg: dict) -> dict:
    # Find highest and lowest cross-vendor pairs
    # Cross-vendor = different providers
    provider_of = {}
    for m in MODEL_META:
        provider_of[m["id"]] = m["provider"]
    short_of = {}
    for m in MODEL_META:
        short_of[m["id"]] = m["short"]

    best_cross = {"pair": "", "pct": 0.0}
    worst_cross = {"pair": "", "pct": 100.0}

    n = len(MODEL_ORDER)
    for i in range(n):
        for j in range(i + 1, n):
            a, b = MODEL_ORDER[i], MODEL_ORDER[j]
            if provider_of[a] == provider_of[b]:
                continue
            val = _get_agreement(agg, a, b)
            label = f"{short_of[a]} <-> {short_of[b]}"
            if val > best_cross["pct"]:
                best_cross = {"pair": label, "pct": val}
            if val < worst_cross["pct"]:
                worst_cross = {"pair": label, "pct": val}

    return {
        "highest_cross_vendor": best_cross,
        "lowest_cross_vendor": worst_cross,
        "gemini_identity": "4/4 Gemini models = 100% identical",
        "knowledge_ceiling": "4/10 trials at universal 100%",
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print(f"Reading {COMPARISON_JSON}")
    with open(COMPARISON_JSON, "r", encoding="utf-8") as f:
        comp = json.load(f)

    print(f"Reading {OPUS_JSON}")
    with open(OPUS_JSON, "r", encoding="utf-8") as f:
        opus = json.load(f)

    agg = comp["aggregate_pairwise_agreement"]

    data = {
        "n_models": 8,
        "n_providers": 3,
        "n_trials": 10,
        "n_items": 114,
        "models": MODEL_META,
        "provider_colors": PROVIDER_COLORS,
        "heatmap": build_heatmap(agg),
        "ih_scaling": build_ih_scaling(comp, opus),
        "cbr_rate": build_cbr_rate(comp, opus),
        "knowledge_judgment": build_knowledge_judgment(comp),
        "provider_profiles": build_provider_profiles(comp, opus),
        "per_trial": build_per_trial(comp),
        "findings": FINDINGS,
        "kpis": build_kpis(agg),
    }

    js_content = (
        "// Cross-Vendor comparison data — generated by generate_cross_vendor_dashboard_data.py\n"
        "const DATA_CROSS_VENDOR = "
        + json.dumps(data, indent=2, ensure_ascii=False)
        + ";\n"
    )

    OUTPUT_JS.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_JS, "w", encoding="utf-8") as f:
        f.write(js_content)

    print(f"Wrote {OUTPUT_JS} ({len(js_content):,} bytes)")
    print(f"  Heatmap: {len(data['heatmap']['matrix'])}x{len(data['heatmap']['matrix'][0])} matrix")
    print(f"  IH scaling: {len(data['ih_scaling']['models'])} models")
    print(f"  CBR rate: {len(data['cbr_rate']['models'])} models")
    print(f"  Knowledge/Judgment: {len(data['knowledge_judgment']['trials'])} trials")
    print(f"  Radar profiles: {len(data['provider_profiles']['profiles'])} providers")
    print(f"  Per-trial table: {len(data['per_trial']['trials'])} trials x 8 models")
    print(f"  Findings: {len(data['findings'])} cards")


if __name__ == "__main__":
    main()
