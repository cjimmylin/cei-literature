"""W2 judge-family home-advantage test (frozen §E; PR-14).

This is a label-free, offline analysis of the two frozen record-level
``scalar_by_judge`` values.  For each judge and design, the observed statistic is the
mean ``score_J - score_other`` on that judge's own-family SUT cells minus the mean on
all other SUT cells.  The null shuffles the single own-family indicator independently
within each public item's six-SUT block.
"""
from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path

import numpy as np


FROZEN_JUDGES = ("openai/gpt-4.1-mini", "google/gemini-2.5-flash")
N_SUTS = 6
PERM_RESAMPLES = 10_000
PERM_SEED = 20260710
ALPHA = 0.01


def _family(model: str) -> str:
    return str(model).split("/", 1)[0] if "/" in str(model) else str(model)


def _normalise_judge_name(name: str) -> str:
    return str(name).removeprefix("or:")


def _validate_judges(judge1_model: str, judge2_model: str) -> tuple[str, str]:
    judges = (judge1_model, judge2_model)
    if judges != FROZEN_JUDGES:
        raise ValueError(
            "W2 judge order must be the explicit frozen pair: "
            f"{FROZEN_JUDGES[0]} then {FROZEN_JUDGES[1]}")
    if _family(judges[0]) == _family(judges[1]):
        raise ValueError("W2 frozen judges must be cross-family")
    return judges


def _validated_blocks(records: list, judges: tuple[str, str]) -> dict:
    if not records:
        raise ValueError("W2 requires public panel records")

    grouped = defaultdict(dict)
    expected_order = tuple(judges)
    for record in records:
        try:
            design = str(record["design"])
            item_id = str(record["item_id"])
            model = str(record["model"])
        except KeyError as exc:
            raise ValueError(f"W2 record missing required field: {exc.args[0]}") from exc

        scalars = record.get("scalar_by_judge")
        if not isinstance(scalars, list) or len(scalars) != 2:
            raise ValueError(f"{item_id}/{model}: scalar_by_judge must contain 2 values")
        if any(isinstance(value, bool) or not isinstance(value, (int, float))
               or not math.isfinite(float(value)) for value in scalars):
            raise ValueError(f"{item_id}/{model}: scalar_by_judge values must be finite numbers")

        verdicts = ((record.get("judge_report") or {}).get("verdicts") or [])
        actual_order = tuple(_normalise_judge_name(v.get("judge", ""))
                             for v in verdicts[:2])
        if len(verdicts) < 2 or actual_order != expected_order:
            raise ValueError(
                f"{item_id}/{model}: judge order {actual_order} does not match "
                f"explicit frozen order {expected_order}")

        key = (design, item_id)
        if model in grouped[key]:
            raise ValueError(f"{design}/{item_id}: duplicate SUT cell for {model}")
        grouped[key][model] = tuple(float(value) for value in scalars)

    blocks = defaultdict(list)
    for (design, item_id), cells_by_model in sorted(grouped.items()):
        if len(cells_by_model) != N_SUTS:
            raise ValueError(
                f"{design}/{item_id}: expected exactly 6 unique SUT cells, "
                f"got {len(cells_by_model)}")
        cells = [(model, cells_by_model[model]) for model in sorted(cells_by_model)]
        for judge in judges:
            count = sum(_family(model) == _family(judge) for model, _ in cells)
            if count != 1:
                raise ValueError(
                    f"{design}/{item_id}/{_family(judge)}: expected exactly one "
                    f"own-family SUT cell, got {count}")
        blocks[design].append((item_id, cells))
    return dict(blocks)


def _per_judge_design(blocks: list, judge_index: int, judge_model: str) -> dict:
    own_family = _family(judge_model)
    difference_blocks = []
    own_indices = []
    for _, cells in blocks:
        differences = [scores[judge_index] - scores[1 - judge_index]
                       for _, scores in cells]
        own = [index for index, (model, _) in enumerate(cells)
               if _family(model) == own_family]
        difference_blocks.append(differences)
        own_indices.append(own[0])

    values = np.asarray(difference_blocks, dtype=float)
    n_items = values.shape[0]
    item_rows = np.arange(n_items)
    own_values = values[item_rows, np.asarray(own_indices)]
    own_mean = float(np.mean(own_values))
    other_mean = float((np.sum(values) - np.sum(own_values)) / (n_items * (N_SUTS - 1)))
    observed = own_mean - other_mean

    rng = np.random.default_rng(PERM_SEED)
    choices = rng.integers(0, N_SUTS, size=(PERM_RESAMPLES, n_items))
    permuted_own = values[item_rows[None, :], choices]
    permuted_own_sums = np.sum(permuted_own, axis=1)
    permuted = (permuted_own_sums / n_items
                - (np.sum(values) - permuted_own_sums)
                / (n_items * (N_SUTS - 1)))
    hits = int(np.count_nonzero(permuted >= observed))
    p_value = (1 + hits) / (PERM_RESAMPLES + 1)
    flagged = p_value < ALPHA
    return {
        "judge_index": judge_index,
        "judge_model": judge_model,
        "judge_family": own_family,
        "n_items": n_items,
        "n_cells": n_items * N_SUTS,
        "own_family_cells": n_items,
        "own_mean_difference": own_mean,
        "other_mean_difference": other_mean,
        "delta": observed,
        "permutation_p": p_value,
        "flagged": flagged,
        "action": "disqualify_own_family_cells" if flagged else "none",
    }


def compute_home_advantage(records: list, judge1_model: str, judge2_model: str) -> dict:
    """Return the exact PR-14 W2 test for every frozen judge × design row."""
    judges = _validate_judges(judge1_model, judge2_model)
    blocks_by_design = _validated_blocks(records, judges)
    results = []
    for judge_index, judge_model in enumerate(judges):
        for design in sorted(blocks_by_design):
            row = _per_judge_design(blocks_by_design[design], judge_index, judge_model)
            row["design"] = design
            results.append(row)
    return {
        "method": {
            "score_field": "scalar_by_judge",
            "exchangeability_unit": "within_item_six_sut_cells",
            "resamples": PERM_RESAMPLES,
            "seed": PERM_SEED,
            "tail": "one_sided_positive_inflation",
            "p_value": "(1 + count(permuted >= observed)) / 10001",
            "alpha": ALPHA,
        },
        "judges": list(judges),
        "results": results,
    }


def _public_input_path(benchmark_root: str, run: str) -> Path:
    run_part = Path(run)
    if (run_part.is_absolute() or len(run_part.parts) != 1 or run in (".", "..")
            or "HOLDOUT" in run.upper()):
        raise ValueError("W2 input is restricted to PUBLIC runs/<name> directories")
    root = Path(benchmark_root).resolve()
    if any(part.upper() == "HOLDOUT" for part in root.parts):
        raise ValueError("W2 input is restricted to PUBLIC runs/<name> directories")
    runs_root = (root / "runs").resolve()
    scored = (runs_root / run / "scored_items.jsonl").resolve()
    if runs_root not in scored.parents or any(part.upper() == "HOLDOUT" for part in scored.parts):
        raise ValueError("W2 input is restricted to PUBLIC runs/<name> directories")
    if not scored.is_file():
        raise ValueError(f"W2 scored input does not exist: {scored}")
    return scored


def _read_jsonl(path: Path) -> list:
    records = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_no}: invalid JSON") from exc
    return records


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="WALKWORTHY W2 frozen-judge home-advantage permutation test")
    parser.add_argument("--benchmark-root", default="..")
    parser.add_argument("--run", required=True,
                        help="PUBLIC run directory name under <benchmark-root>/runs")
    parser.add_argument("--out", required=True, help="new JSON result path")
    parser.add_argument("--judge1-model", required=True)
    parser.add_argument("--judge2-model", required=True)
    args = parser.parse_args(argv)

    try:
        input_path = _public_input_path(args.benchmark_root, args.run)
        out_path = Path(args.out)
        if any(part.upper() == "HOLDOUT" for part in out_path.resolve().parts):
            raise ValueError("W2 output cannot be placed under HOLDOUT")
        if out_path.exists():
            raise ValueError(f"W2 output already exists: {out_path}")
        records = _read_jsonl(input_path)
        report = compute_home_advantage(records, args.judge1_model, args.judge2_model)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc

    report["input"] = {"run": args.run, "records": len(records),
                       "scored_items": str(input_path)}
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")
    print(json.dumps({"out": str(out_path), "rows": len(report["results"]),
                      "flags": sum(row["flagged"] for row in report["results"])}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
