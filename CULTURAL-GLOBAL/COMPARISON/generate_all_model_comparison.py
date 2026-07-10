#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from collections import defaultdict
from itertools import combinations
from pathlib import Path


BASE = Path(__file__).resolve().parent.parent
OUT_DIR = Path(__file__).resolve().parent
DATE_PREFIX = "20260404"

SUMMARY_PATH = OUT_DIR / f"{DATE_PREFIX}-all-model-comparison-summary.json"
DETAIL_PATH = OUT_DIR / f"{DATE_PREFIX}-all-model-comparison-details.json"
REPORT_PATH = OUT_DIR / f"{DATE_PREFIX}-all-model-comparison-report.md"

TRIAL_IDS = [f"CC{i}" for i in range(1, 11)]
NUMERIC_TRIALS = ["CC1", "CC2", "CC3", "CC4", "CC5"]
QUALITATIVE_TRIALS = ["CC6", "CC7", "CC8", "CC9", "CC10"]
TARGET_COUNTRIES = [
    "US", "China", "India", "Nigeria", "Brazil",
    "Saudi_Arabia", "Japan", "Germany",
]


DISCOVERY_SPECS = [
    {
        "provider": "Anthropic",
        "provenance": "original project trial corpus",
        "glob": BASE / "TRIALS" / "20260404-trial-CC*.json",
    },
    {
        "provider": "OpenAI",
        "provenance": "Codex offline agent-authored corpus",
        "glob": BASE / "Codex" / "20260404-trial-CC*.json",
    },
    {
        "provider": "OpenAI",
        "provenance": "Codex offline agent-authored corpus",
        "glob": BASE / "Codex-Mini" / "20260404-trial-CC*.json",
    },
    {
        "provider": "Gemini",
        "provenance": "template-derived simulated corpus",
        "glob": BASE / "TRIALS" / "gemini-*" / "20260404-trial-CC*.json",
    },
]


def mean(vals: list[float]) -> float:
    return sum(vals) / len(vals) if vals else 0.0


def safe_float(v) -> float | None:
    if v is None:
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def pearson_r(xs: list[float], ys: list[float]) -> float | None:
    n = len(xs)
    if n < 3 or len(ys) != n:
        return None
    mx, my = mean(xs), mean(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    dy = math.sqrt(sum((y - my) ** 2 for y in ys))
    if dx == 0 or dy == 0:
        return None
    return round(num / (dx * dy), 4)


def cohens_kappa(xs: list[int], ys: list[int], k: int = 6) -> float | None:
    n = len(xs)
    if n < 3 or len(ys) != n:
        return None
    matrix = [[0] * k for _ in range(k)]
    for x, y in zip(xs, ys):
        xi = max(0, min(k - 1, int(x)))
        yi = max(0, min(k - 1, int(y)))
        matrix[xi][yi] += 1
    po = sum(matrix[i][i] for i in range(k)) / n
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(matrix[r][c] for r in range(k)) for c in range(k)]
    pe = sum(row_sums[i] * col_sums[i] for i in range(k)) / (n * n)
    if pe == 1.0:
        return 1.0
    return round((po - pe) / (1 - pe), 4)


def discover_trials() -> tuple[dict[str, dict[str, dict]], dict[str, dict]]:
    models: dict[str, dict[str, dict]] = defaultdict(dict)
    meta: dict[str, dict] = {}

    for spec in DISCOVERY_SPECS:
        for path in sorted(pathlib_glob(spec["glob"])):
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            model = data["model"]
            trial_id = data["trial_id"]
            models[model][trial_id] = data
            meta.setdefault(model, {
                "provider": spec["provider"],
                "provenance": spec["provenance"],
                "root": str(path.parent),
                "files": [],
            })
            meta[model]["files"].append(str(path))
    return models, meta


def pathlib_glob(pattern: Path):
    return Path(pattern.anchor or "/").glob(str(pattern)[1:]) if pattern.is_absolute() else Path().glob(str(pattern))


def validate_inventory(models: dict[str, dict[str, dict]], baseline_ids: dict[str, list[int]]) -> dict:
    out = {"models": {}, "all_complete": True}
    for model, trials in sorted(models.items()):
        missing = [tid for tid in TRIAL_IDS if tid not in trials]
        mismatches = {}
        for tid, expected_ids in baseline_ids.items():
            if tid not in trials:
                continue
            actual = [item.get("id") for item in trials[tid].get("items", [])]
            if actual != expected_ids:
                mismatches[tid] = {
                    "expected_count": len(expected_ids),
                    "actual_count": len(actual),
                }
        out["models"][model] = {
            "trial_count": len(trials),
            "missing_trials": missing,
            "item_id_mismatches": mismatches,
        }
        if missing or mismatches:
            out["all_complete"] = False
    return out


def compute_country_distances(cc1: dict) -> dict[str, float]:
    countries: dict[str, list[tuple[float, float]]] = defaultdict(list)
    for item in cc1.get("items", []):
        resp = safe_float(item.get("response_numeric"))
        if resp is None:
            continue
        for country, baseline in item.get("human_baselines", {}).items():
            bl = safe_float(baseline)
            if bl is not None:
                countries[country].append((resp, bl))
    result = {}
    for country, pairs in countries.items():
        result[country] = round(mean([abs(r - b) for r, b in pairs]), 3)
    return dict(sorted(result.items(), key=lambda kv: kv[1]))


def compute_mfq_profile(cc2: dict) -> dict:
    foundation_items: dict[str, list[float]] = defaultdict(list)
    for item in cc2.get("items", []):
        val = safe_float(item.get("response_numeric"))
        if val is None:
            continue
        domain = item.get("domain", "")
        if "Care" in domain or "Harm" in domain:
            foundation_items["Care_Harm"].append(val)
        elif "Fairness" in domain or "Cheating" in domain:
            foundation_items["Fairness_Cheating"].append(val)
        elif "Loyalty" in domain or "Betrayal" in domain:
            foundation_items["Loyalty_Betrayal"].append(val)
        elif "Authority" in domain or "Subversion" in domain:
            foundation_items["Authority_Subversion"].append(val)
        elif "Sanctity" in domain or "Degradation" in domain:
            foundation_items["Sanctity_Degradation"].append(val)

    scores = {k: round(mean(v), 2) for k, v in foundation_items.items()}
    summary_scores = cc2.get("summary", {}).get("foundation_scores", {})
    if summary_scores:
        scores = {k: round(v, 2) for k, v in summary_scores.items()}
    indiv = mean([scores.get("Care_Harm", 0), scores.get("Fairness_Cheating", 0)])
    binding = mean([
        scores.get("Loyalty_Betrayal", 0),
        scores.get("Authority_Subversion", 0),
        scores.get("Sanctity_Degradation", 0),
    ])
    return {
        "foundation_scores": scores,
        "individualizing": round(indiv, 2),
        "binding": round(binding, 2),
        "ratio": round(indiv / binding, 2) if binding > 0 else None,
    }


RLHF_THEMES = {
    "individual_autonomy_default": ["autonomy", "individual", "choice", "self-determination", "rights-based"],
    "secular_epistemology": ["secular", "revelation", "divine", "scientific", "empirical"],
    "consequentialist_optimization": ["utilitarian", "consequential", "efficiency", "maximize", "cost-benefit"],
    "gender_equality_lock": ["gender equality", "gender", "feminist", "patriarch", "lgbtq"],
    "anti_authority_bias": ["anti-authority", "authority", "hierarchy", "deference", "elder respect"],
    "harm_principle_absolutism": ["harm principle", "harm-avoidance", "harm reduction", "purity", "sanctity"],
}


def count_rlhf_conflicts(trials: dict[str, dict]) -> dict:
    all_conflicts: list[str] = []
    for trial in trials.values():
        for conflict in trial.get("summary", {}).get("rlhf_conflicts_identified", []):
            all_conflicts.append(conflict)
        for item in trial.get("items", []):
            for field in ("rlhf_conflict", "rlhf_tension", "rlhf_pulls_toward"):
                val = item.get(field)
                if isinstance(val, str) and val.strip():
                    all_conflicts.append(val)
    theme_counts: dict[str, int] = defaultdict(int)
    for text in all_conflicts:
        lower = text.lower()
        matched = False
        for theme, keywords in RLHF_THEMES.items():
            if any(keyword in lower for keyword in keywords):
                theme_counts[theme] += 1
                matched = True
        if not matched:
            theme_counts["other"] += 1
    return {"total": len(all_conflicts), "by_theme": dict(sorted(theme_counts.items()))}


def score_engagement_depth(trials: dict[str, dict]) -> dict[str, float]:
    tradition_trials = {
        "CC4": "Islamic",
        "CC5": "Confucian",
        "CC6": "Ubuntu",
        "CC7": "Buddhist",
        "CC9": "Dharmic",
    }
    results = {}
    for tid, tradition in tradition_trials.items():
        if tid not in trials:
            continue
        items = trials[tid].get("items", [])
        n = len(items) if items else 1
        limitation_count = 0
        perspective_count = 0
        applied_count = 0
        for item in items:
            text = " ".join(str(item.get(field, "")) for field in (
                "response", "reasoning", "cultural_notes", "tradition_perspective",
                "knowledge_vs_expression_gap", "rlhf_tension", "rlhf_conflict",
            )).lower()
            if any(s in text for s in ["cannot", "structurally incapable", "cannot fully", "structural limitation", "ontological gap"]):
                limitation_count += 1
            if any(s in text for s in ["from an ubuntu perspective", "from a confucian perspective", "from an islamic perspective", "from a buddhist perspective", "from a dharmic perspective", "within this framework", "ubuntu perspective", "buddhist perspective", "dharmic perspective"]):
                perspective_count += 1
            if any(s in text for s in ["the tradition holds", "this means", "in practice", "the logic", "role-bound duty", "mutual care"]):
                applied_count += 1
        lim_pct = limitation_count / n
        per_pct = perspective_count / n
        app_pct = applied_count / n
        if lim_pct > 0.5:
            score = 4.0
        elif lim_pct > 0.2 and per_pct > 0.3:
            score = 3.5
        elif per_pct > 0.3:
            score = 3.0
        elif app_pct > 0.3:
            score = 2.0
        else:
            score = 1.0
        results[tradition] = score
    return results


def compute_response_lengths(trials: dict[str, dict]) -> dict[str, float]:
    result = {}
    for tid, trial in trials.items():
        lengths = [len(item.get("response", "")) for item in trial.get("items", []) if item.get("response")]
        result[tid] = round(mean(lengths), 1) if lengths else 0.0
    return result


def extract_numeric_responses(trials: dict[str, dict]) -> dict[str, dict[int, float]]:
    result = {}
    for tid in NUMERIC_TRIALS:
        if tid not in trials:
            continue
        result[tid] = {}
        for item in trials[tid].get("items", []):
            val = safe_float(item.get("response_numeric"))
            if val is not None:
                result[tid][int(item["id"])] = val
    return result


def build_pairwise_agreement(models: dict[str, dict[str, dict]]) -> tuple[dict, dict]:
    numeric_by_model = {model: extract_numeric_responses(trials) for model, trials in models.items()}
    pairwise = {}
    matrix = {metric: defaultdict(dict) for metric in ("pearson_r", "mean_abs_diff", "cohens_kappa")}
    model_names = sorted(models)
    for m in model_names:
        matrix["pearson_r"][m][m] = 1.0
        matrix["mean_abs_diff"][m][m] = 0.0
        matrix["cohens_kappa"][m][m] = 1.0

    for m1, m2 in combinations(model_names, 2):
        all_xs: list[float] = []
        all_ys: list[float] = []
        per_trial = {}
        for tid in NUMERIC_TRIALS:
            d1 = numeric_by_model[m1].get(tid, {})
            d2 = numeric_by_model[m2].get(tid, {})
            common = sorted(set(d1) & set(d2))
            if not common:
                continue
            xs = [d1[i] for i in common]
            ys = [d2[i] for i in common]
            all_xs.extend(xs)
            all_ys.extend(ys)
            per_trial[tid] = {
                "n_items": len(common),
                "pearson_r": pearson_r(xs, ys),
                "mean_abs_diff": round(mean([abs(x - y) for x, y in zip(xs, ys)]), 3),
                "cohens_kappa": cohens_kappa([int(x) for x in xs], [int(y) for y in ys]),
            }
        overall = {
            "n_items": len(all_xs),
            "pearson_r": pearson_r(all_xs, all_ys),
            "mean_abs_diff": round(mean([abs(x - y) for x, y in zip(all_xs, all_ys)]), 3),
            "cohens_kappa": cohens_kappa([int(x) for x in all_xs], [int(y) for y in all_ys]),
        }
        key = f"{m1}__vs__{m2}"
        pairwise[key] = {"model_a": m1, "model_b": m2, "overall": overall, "per_trial": per_trial}
        for metric in ("pearson_r", "mean_abs_diff", "cohens_kappa"):
            matrix[metric][m1][m2] = overall[metric]
            matrix[metric][m2][m1] = overall[metric]
    return pairwise, {metric: dict(rows) for metric, rows in matrix.items()}


def build_numeric_divergence(models: dict[str, dict[str, dict]]) -> list[dict]:
    item_map: dict[tuple[str, int], dict[str, float]] = defaultdict(dict)
    question_map: dict[tuple[str, int], str] = {}
    domain_map: dict[tuple[str, int], str] = {}
    for model, trials in models.items():
        for tid in NUMERIC_TRIALS:
            trial = trials.get(tid)
            if not trial:
                continue
            for item in trial.get("items", []):
                val = safe_float(item.get("response_numeric"))
                if val is None:
                    continue
                key = (tid, int(item["id"]))
                item_map[key][model] = val
                question_map[key] = item.get("question", "")
                domain_map[key] = item.get("domain", "")
    rows = []
    for key, values in item_map.items():
        if len(values) < 3:
            continue
        vals = list(values.values())
        rows.append({
            "trial_id": key[0],
            "item_id": key[1],
            "domain": domain_map[key],
            "question": question_map[key],
            "models_present": len(values),
            "min_response": min(vals),
            "max_response": max(vals),
            "range": round(max(vals) - min(vals), 3),
            "variance": round(mean([(v - mean(vals)) ** 2 for v in vals]), 4),
            "responses_by_model": dict(sorted(values.items())),
        })
    rows.sort(key=lambda r: (r["variance"], r["range"], r["trial_id"], r["item_id"]), reverse=True)
    return rows[:25]


def build_trial_group_comparison(models: dict[str, dict[str, dict]], per_model: dict[str, dict]) -> dict:
    out = {}
    for tid in TRIAL_IDS:
        by_model = {}
        for model, trials in models.items():
            trial = trials.get(tid)
            if not trial:
                continue
            entry = {
                "benchmark": trial.get("benchmark"),
                "items_count": trial.get("items_count"),
                "mean_response_length": per_model[model]["trial_response_lengths"].get(tid),
            }
            if tid in NUMERIC_TRIALS:
                vals = [safe_float(item.get("response_numeric")) for item in trial.get("items", [])]
                vals = [v for v in vals if v is not None]
                entry["mean_numeric_response"] = round(mean(vals), 3) if vals else None
            else:
                entry["qualitative_mean_length"] = per_model[model]["trial_response_lengths"].get(tid)
            by_model[model] = entry
        out[tid] = by_model
    return out


def compute_per_model(models: dict[str, dict[str, dict]], meta: dict[str, dict]) -> dict:
    per_model = {}
    for model, trials in sorted(models.items()):
        lengths = compute_response_lengths(trials)
        country_distances = compute_country_distances(trials["CC1"])
        mfq = compute_mfq_profile(trials["CC2"])
        conflicts = count_rlhf_conflicts(trials)
        depth = score_engagement_depth(trials)
        per_model[model] = {
            "provider": meta[model]["provider"],
            "provenance": meta[model]["provenance"],
            "trial_count": len(trials),
            "items_total": sum(trial.get("items_count", 0) for trial in trials.values()),
            "mean_response_length": round(mean(list(lengths.values())), 1),
            "trial_response_lengths": lengths,
            "country_distances": country_distances,
            "closest_country": next(iter(country_distances.items())) if country_distances else None,
            "farthest_country": next(reversed(country_distances.items())) if country_distances else None,
            "mfq_profile": mfq,
            "rlhf_conflicts": conflicts,
            "engagement_depth": depth,
        }
    return per_model


def build_report(summary: dict, details: dict) -> str:
    per_model = summary["per_model"]
    pairwise = details["pairwise_agreement"]
    divergence = details["top_numeric_divergence_items"]
    strongest_pair = max(pairwise.values(), key=lambda x: x["overall"]["pearson_r"] or -1)
    weakest_pair = min(pairwise.values(), key=lambda x: x["overall"]["pearson_r"] if x["overall"]["pearson_r"] is not None else 99)
    ratio_rank = sorted(
        ((m, v["mfq_profile"]["ratio"]) for m, v in per_model.items() if v["mfq_profile"]["ratio"] is not None),
        key=lambda x: x[1],
        reverse=True,
    )
    length_rank = sorted(((m, v["mean_response_length"]) for m, v in per_model.items()), key=lambda x: x[1], reverse=True)

    lines = [
        "# All-Model Cross-Cultural Benchmark Comparison",
        "",
        f"Date: {summary['date']}",
        "",
        "## Coverage",
        f"- Models compared: {summary['inventory']['model_count']}",
        f"- Trials per model expected: {len(TRIAL_IDS)}",
        f"- Inventory complete: {summary['inventory_validation']['all_complete']}",
        "- Providers represented: Anthropic, OpenAI, Gemini",
        "",
        "## Provenance Note",
        "- Anthropic runs come from the original tri-model corpus under `TRIALS/`.",
        "- OpenAI runs come from the Codex-authored corpora under `Codex/` and `Codex-Mini/`.",
        "- Gemini runs already existed under `TRIALS/gemini-*` and are template-derived simulations, as indicated by `simulate_trials.py` in those directories.",
        "",
        "## High-Level Findings",
        f"- Strongest numeric agreement pair: `{strongest_pair['model_a']}` vs `{strongest_pair['model_b']}` with Pearson r = {strongest_pair['overall']['pearson_r']}.",
        f"- Weakest numeric agreement pair: `{weakest_pair['model_a']}` vs `{weakest_pair['model_b']}` with Pearson r = {weakest_pair['overall']['pearson_r']}.",
        f"- Highest MFQ individualizing/binding ratio: `{ratio_rank[0][0]}` at {ratio_rank[0][1]}.",
        f"- Lowest MFQ individualizing/binding ratio: `{ratio_rank[-1][0]}` at {ratio_rank[-1][1]}.",
        f"- Longest average responses: `{length_rank[0][0]}` at {length_rank[0][1]} chars.",
        f"- Shortest average responses: `{length_rank[-1][0]}` at {length_rank[-1][1]} chars.",
        "",
        "## Per-Model Summary",
    ]
    for model, metrics in sorted(per_model.items()):
        closest = metrics["closest_country"]
        lines.append(
            f"- `{model}` ({metrics['provider']}): closest country = {closest[0]} ({closest[1]}), MFQ ratio = {metrics['mfq_profile']['ratio']}, RLHF conflict count = {metrics['rlhf_conflicts']['total']}, mean response length = {metrics['mean_response_length']}."
        )
    lines.extend([
        "",
        "## Highest-Divergence Numeric Items",
    ])
    for row in divergence[:10]:
        lines.append(
            f"- `{row['trial_id']}` item {row['item_id']} (`{row['domain']}`): variance = {row['variance']}, range = {row['range']}. Question: {row['question']}"
        )
    lines.extend([
        "",
        "## Output Files",
        f"- Summary JSON: `{SUMMARY_PATH.name}`",
        f"- Detail JSON: `{DETAIL_PATH.name}`",
        f"- Report: `{REPORT_PATH.name}`",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    models, meta = discover_trials()
    baseline_ids = {
        tid: [item.get("id") for item in models["claude-opus-4-6"][tid].get("items", [])]
        for tid in TRIAL_IDS
    }
    inventory_validation = validate_inventory(models, baseline_ids)
    per_model = compute_per_model(models, meta)
    pairwise_agreement, pairwise_matrices = build_pairwise_agreement(models)
    top_numeric_divergence_items = build_numeric_divergence(models)
    trial_group_comparison = build_trial_group_comparison(models, per_model)

    summary = {
        "date": DATE_PREFIX,
        "inventory": {
            "model_count": len(models),
            "model_names": sorted(models),
            "providers": sorted({m["provider"] for m in meta.values()}),
            "trials_per_model_expected": len(TRIAL_IDS),
        },
        "inventory_validation": inventory_validation,
        "per_model": per_model,
    }
    details = {
        "date": DATE_PREFIX,
        "pairwise_agreement": pairwise_agreement,
        "pairwise_matrices": pairwise_matrices,
        "top_numeric_divergence_items": top_numeric_divergence_items,
        "trial_group_comparison": trial_group_comparison,
    }
    report = build_report(summary, details)

    with open(SUMMARY_PATH, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
        f.write("\n")
    with open(DETAIL_PATH, "w", encoding="utf-8") as f:
        json.dump(details, f, indent=2, ensure_ascii=False)
        f.write("\n")
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report)


if __name__ == "__main__":
    main()
