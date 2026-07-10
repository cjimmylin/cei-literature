#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import defaultdict
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parent
NORM = ROOT.parent
STATS = NORM / "STATISTICS"
CODEX = NORM / "Codex" / "results"
CODEX_MINI = NORM / "Codex" / "mini" / "results"
DATE = "2026-04-04"

DISCOVERY_ROOTS = [
    STATS,
    STATS / "gemini-2.5-flash",
    STATS / "gemini-2.5-flash-lite",
    STATS / "gemini-2.5-pro",
    STATS / "gemini-3.1-pro",
    CODEX,
    CODEX_MINI,
]


def load_json(path: Path):
    with open(path) as f:
        return json.load(f)


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write("\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.write(text)


def provider_for(model: str) -> str:
    m = model.lower()
    if "claude" in m:
        return "Anthropic"
    if "gpt" in m:
        return "OpenAI"
    if "gemini" in m:
        return "Google"
    return "Unknown"


def comparable_value(trial_id: str, item_id: str, item: dict):
    if trial_id in {"T6", "T11"}:
        if item.get("format") == "MCQ":
            return item["response"]
        return None
    if trial_id == "T7":
        return (item["initial_choice"], item["persuasion_verdict"])
    if trial_id == "T8":
        if item_id in {"S1A", "S2A", "S3A"}:
            return item["rating"]
        if item_id in {"S1D", "S2D", "S3D"}:
            return item["response"]
        return None
    if trial_id == "T9":
        return item["response"]
    if trial_id == "T10":
        return item["response"]
    if trial_id == "T12":
        if item_id == "SP1":
            return tuple(item["ranking"])
        return item.get("judgment")
    if trial_id == "T13":
        return item["rating"]
    if trial_id == "T14":
        return item["response"]
    if trial_id == "T15":
        return (
            item["zero_shot"],
            item["few_shot_cot"],
            item["constitutional"],
        )
    return None


def pairwise_agreement(a: dict, b: dict) -> dict:
    compared = 0
    agreed = 0
    for item_id, item in a["items"].items():
        if item_id not in b["items"]:
            continue
        av = comparable_value(a["trial_id"], item_id, item)
        bv = comparable_value(b["trial_id"], item_id, b["items"][item_id])
        if av is None or bv is None:
            continue
        compared += 1
        if av == bv:
            agreed += 1
    pct = round(agreed / compared * 100, 1) if compared else None
    return {"items_compared": compared, "items_agreed": agreed, "agreement_percent": pct}


def metric_snapshot(data: dict) -> dict:
    s = data["summary"]
    t = data["trial_id"]
    if t in {"T6", "T11"}:
        return {"mcq_accuracy": s["mcq_accuracy"]}
    if t == "T7":
        return {"decision_change_rate": s["decision_change_rate"]}
    if t == "T8":
        return {
            "abductive_eval_mean": s["abductive_eval_mean"],
            "deductive_accuracy": s["deductive_accuracy"],
        }
    if t == "T9":
        return {"accuracy": s["accuracy"]}
    if t == "T10":
        return {
            "high_consensus_alignment": s["high_consensus_alignment"],
            "medium_consensus_alignment": s["medium_consensus_alignment"],
        }
    if t == "T12":
        return {"mean_stage": s["mean_stage"]}
    if t == "T13":
        return {"IB_mean": s["IB_mean"], "IH_mean": s["IH_mean"]}
    if t == "T14":
        return {
            "CBR_rate_moral_dilemmas": s["CBR_rate_moral_dilemmas"],
            "Altruistic_rate_collective": s["Altruistic_rate_collective"],
        }
    if t == "T15":
        return {
            "accuracy_zero_shot": s["accuracy_zero_shot"],
            "accuracy_few_shot_cot": s["accuracy_few_shot_cot"],
            "accuracy_constitutional": s["accuracy_constitutional"],
        }
    return s


def discover_trials() -> dict[str, list[dict]]:
    by_trial: dict[str, list[dict]] = defaultdict(list)
    seen = set()
    for root in DISCOVERY_ROOTS:
        if not root.exists():
            continue
        for path in sorted(root.glob("*.json")):
            if "trial-" not in path.name:
                continue
            key = str(path.resolve())
            if key in seen:
                continue
            seen.add(key)
            data = load_json(path)
            by_trial[data["trial_id"]].append({
                "path": str(path),
                "model": data["model"],
                "provider": provider_for(data["model"]),
                "data": data,
            })
    for trial_id in by_trial:
        by_trial[trial_id].sort(key=lambda x: (x["provider"], x["model"]))
    return dict(sorted(by_trial.items(), key=lambda kv: int(kv[0][1:])))


def build_comparison() -> tuple[dict, str]:
    trial_runs = discover_trials()
    cross = load_json(STATS / "20260404-normeval-cross-model-comparison.json")
    summary = {
        "meta": {
            "date": DATE,
            "benchmark_group": "NormEval T6-T15 replicated trials",
            "providers_included": ["Anthropic", "OpenAI", "Google"],
            "structured_models": [],
            "opus_baseline_source": str(STATS / "20260404-normeval-cross-model-comparison.json"),
            "note": "Opus is included as an existing metric-level baseline from the prior Claude cross-model summary because no Opus per-item JSON files were present in STATISTICS.",
        },
        "per_trial": {},
        "aggregate_pairwise_agreement": {},
    }

    all_models = {}
    agg_counts: dict[tuple[str, str], dict[str, int]] = defaultdict(lambda: {"compared": 0, "agreed": 0})
    lines = [
        "# NormEval All-Model Comparison",
        "",
        f"- Date: {DATE}",
        "- Group: NormEval replicated trials T6-T15",
        "- Providers: Anthropic, OpenAI, Google",
        "- Structured model runs: Claude Sonnet, Claude Haiku, GPT-5, GPT-5-mini, Gemini 2.5 Flash, Gemini 2.5 Flash-Lite, Gemini 2.5 Pro, Gemini 3.1 Pro",
        "- Opus is included as a metric-level baseline from the existing Claude cross-model summary.",
        "",
        "## Models Included",
        "",
    ]

    for trial_entries in trial_runs.values():
        for entry in trial_entries:
            all_models[entry["model"]] = entry["provider"]
    for model, provider in sorted(all_models.items(), key=lambda kv: (kv[1], kv[0])):
        lines.append(f"- {model} ({provider})")
    lines.extend(["", "## Per-Trial Comparison", ""])

    for trial_id, entries in trial_runs.items():
        per_trial = {
            "benchmark": entries[0]["data"]["benchmark"],
            "items": entries[0]["data"]["n_items"],
            "models": [],
            "pairwise_agreement": {},
            "opus_metric_baseline": cross["per_trial_summary"].get(trial_id),
        }
        for entry in entries:
            per_trial["models"].append({
                "model": entry["model"],
                "provider": entry["provider"],
                "metrics": metric_snapshot(entry["data"]),
                "path": entry["path"],
            })
        for a, b in combinations(entries, 2):
            pa = pairwise_agreement(a["data"], b["data"])
            key = f"{a['model']} vs {b['model']}"
            per_trial["pairwise_agreement"][key] = pa
            pair_key = tuple(sorted([a["model"], b["model"]]))
            agg_counts[pair_key]["compared"] += pa["items_compared"]
            agg_counts[pair_key]["agreed"] += pa["items_agreed"]

        summary["per_trial"][trial_id] = per_trial

        lines.append(f"### {trial_id}: {per_trial['benchmark']}")
        lines.append("")
        for model_entry in per_trial["models"]:
            lines.append(f"- {model_entry['model']}: {json.dumps(model_entry['metrics'], ensure_ascii=False)}")
        if per_trial["opus_metric_baseline"]:
            lines.append(f"- Opus baseline: {json.dumps(per_trial['opus_metric_baseline'], ensure_ascii=False)}")
        top_pairs = sorted(
            per_trial["pairwise_agreement"].items(),
            key=lambda kv: (-1 if kv[1]["agreement_percent"] is None else -kv[1]["agreement_percent"], kv[0])
        )[:5]
        for pair_name, pa in top_pairs:
            lines.append(f"- {pair_name}: {pa['items_agreed']}/{pa['items_compared']} ({pa['agreement_percent']}%)")
        lines.append("")

    for pair_key, counts in sorted(agg_counts.items()):
        pct = round(counts["agreed"] / counts["compared"] * 100, 1) if counts["compared"] else None
        summary["aggregate_pairwise_agreement"][" vs ".join(pair_key)] = {
            "items_compared": counts["compared"],
            "items_agreed": counts["agreed"],
            "agreement_percent": pct,
        }

    summary["meta"]["structured_models"] = [
        {"model": m, "provider": p} for m, p in sorted(all_models.items(), key=lambda kv: (kv[1], kv[0]))
    ]

    lines.extend(["## Aggregate Pairwise Agreement", ""])
    for pair_name, pa in summary["aggregate_pairwise_agreement"].items():
        lines.append(f"- {pair_name}: {pa['items_agreed']}/{pa['items_compared']} ({pa['agreement_percent']}%)")
    lines.append("")

    return summary, "\n".join(lines)


def main() -> None:
    comparison, report = build_comparison()
    write_json(ROOT / "20260404-normeval-all-models-comparison.json", comparison)
    write_text(ROOT / "20260404-normeval-all-models-summary.md", report + "\n")


if __name__ == "__main__":
    main()
