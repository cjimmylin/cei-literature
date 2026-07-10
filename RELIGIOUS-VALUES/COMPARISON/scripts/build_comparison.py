#!/usr/bin/env python3
from __future__ import annotations

import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT.parent
MANIFEST = ROOT / "inputs" / "model-manifest.json"
RESULTS = ROOT / "results"


def load_json(path: Path) -> dict:
    return json.load(open(path, encoding="utf-8"))


def existing_paths(model_id: str, source_root: Path, has_existing_rubric: bool) -> tuple[Path, Path, Path]:
    if source_root.name == "data":
        short = {
            "claude-opus-4-6": "opus",
            "claude-sonnet-4-20250514": "sonnet",
            "claude-haiku-4-5-20251001": "haiku",
        }[model_id]
        scoring = source_root / f"20260404-trial-scoring-results-{short}.json"
        rubric = source_root / ("20260404-trial-rubric-summary.json" if short == "opus" else f"20260404-trial-rubric-summary-{short}.json")
        t2 = source_root / f"20260404-t2-results-{short}.json"
        return scoring, rubric, t2
    if source_root.name == "results":
        scoring = source_root / f"20260404-trial-scoring-results-{model_id}.json"
        rubric = source_root / f"20260404-trial-rubric-summary-{model_id}.json"
        t2 = source_root / f"20260404-t2-results-{model_id}.json"
        return scoring, rubric, t2
    derived = ROOT / "derived" / model_id
    return (
        derived / f"20260404-trial-scoring-results-{model_id}.json",
        derived / f"20260404-trial-rubric-summary-{model_id}.json",
        derived / f"20260404-t2-results-{model_id}.json",
    )


def mean_or_none(values: list[float]) -> float | None:
    vals = [v for v in values if v is not None]
    return round(statistics.mean(vals), 4) if vals else None


def main() -> int:
    manifest = load_json(MANIFEST)["models"]
    model_rows = []
    vendor_groups: dict[str, list[dict]] = {}

    for spec in manifest:
        model_id = spec["model_id"]
        vendor = spec["vendor"]
        source_root = Path(spec["source_root"])
        scoring_path, rubric_path, t2_path = existing_paths(model_id, source_root, spec["has_existing_rubric"])
        scoring = load_json(scoring_path)
        rubric = load_json(rubric_path)
        t2 = load_json(t2_path)

        row = {
            "model": model_id,
            "vendor": vendor,
            "family": spec["family"],
            "source_root": str(source_root),
            "rubric_origin": "original" if spec["has_existing_rubric"] else "backfilled",
            "gradient_holds": scoring["gradient_test"]["gradient_holds"],
            "knowledge_mean_length": scoring["gradient_test"]["knowledge_mean"],
            "reasoning_mean_length": scoring["gradient_test"]["reasoning_mean"],
            "values_mean_length": scoring["gradient_test"]["values_mean"],
            "bias_values_r": scoring["bias_values_independence"]["pearson_r"],
            "bias_values_independent": scoring["bias_values_independence"]["constructs_independent"],
            "rubric_knowledge": rubric["type_summary"].get("knowledge", {}).get("mean_normalized"),
            "rubric_reasoning": rubric["type_summary"].get("reasoning", {}).get("mean_normalized"),
            "rubric_values": rubric["type_summary"].get("values", {}).get("mean_normalized"),
            "rubric_bias": rubric["type_summary"].get("bias", {}).get("mean_normalized"),
            "rubric_values_paired": rubric["type_summary"].get("values_paired", {}).get("mean_normalized"),
            "t2_accuracy": t2["summary"]["accuracy"],
            "t2_beginner_accuracy": round(t2["summary"]["beginner_correct"] / t2["summary"]["beginner_total"], 4),
            "t2_advanced_accuracy": round(t2["summary"]["advanced_correct"] / t2["summary"]["advanced_total"], 4),
        }
        model_rows.append(row)
        vendor_groups.setdefault(vendor, []).append(row)

    vendor_rows = []
    for vendor, rows in sorted(vendor_groups.items()):
        vendor_rows.append({
            "vendor": vendor,
            "models": [r["model"] for r in rows],
            "n_models": len(rows),
            "gradient_holds_all": all(r["gradient_holds"] for r in rows),
            "mean_knowledge_length": mean_or_none([r["knowledge_mean_length"] for r in rows]),
            "mean_reasoning_length": mean_or_none([r["reasoning_mean_length"] for r in rows]),
            "mean_values_length": mean_or_none([r["values_mean_length"] for r in rows]),
            "mean_bias_values_r": mean_or_none([r["bias_values_r"] for r in rows]),
            "mean_rubric_knowledge": mean_or_none([r["rubric_knowledge"] for r in rows]),
            "mean_rubric_reasoning": mean_or_none([r["rubric_reasoning"] for r in rows]),
            "mean_rubric_values": mean_or_none([r["rubric_values"] for r in rows]),
            "mean_t2_accuracy": mean_or_none([r["t2_accuracy"] for r in rows]),
            "max_t2_accuracy": max(r["t2_accuracy"] for r in rows),
            "min_t2_accuracy": min(r["t2_accuracy"] for r in rows),
        })

    model_json = {
        "generated": "2026-04-04",
        "title": "All-model comparison across Anthropic, OpenAI/Codex, and Gemini",
        "models": model_rows,
    }
    vendor_json = {
        "generated": "2026-04-04",
        "title": "Vendor-level comparison across Anthropic, OpenAI/Codex, and Gemini",
        "vendors": vendor_rows,
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    json.dump(model_json, open(RESULTS / "model-comparison.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    json.dump(vendor_json, open(RESULTS / "vendor-comparison.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    def md_table(rows: list[dict], headers: list[str]) -> str:
        lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
        for row in rows:
            lines.append("| " + " | ".join(str(row.get(h, "")) for h in headers) + " |")
        return "\n".join(lines)

    model_headers = [
        "model", "vendor", "rubric_origin", "gradient_holds",
        "knowledge_mean_length", "reasoning_mean_length", "values_mean_length",
        "bias_values_r", "rubric_values", "t2_accuracy"
    ]
    vendor_headers = [
        "vendor", "n_models", "gradient_holds_all", "mean_values_length",
        "mean_rubric_values", "mean_t2_accuracy", "max_t2_accuracy", "min_t2_accuracy"
    ]
    (RESULTS / "model-comparison.md").write_text(
        "# Model Comparison\n\n" + md_table(model_rows, model_headers) + "\n",
        encoding="utf-8",
    )
    (RESULTS / "vendor-comparison.md").write_text(
        "# Vendor Comparison\n\n" + md_table(vendor_rows, vendor_headers) + "\n",
        encoding="utf-8",
    )
    print("Wrote comparison outputs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
