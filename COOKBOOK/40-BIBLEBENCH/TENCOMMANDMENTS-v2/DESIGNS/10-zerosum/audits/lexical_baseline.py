#!/usr/bin/env python3
"""Core-grouped X2 lexical/style/length baselines for ZEROSUM P1."""

from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import date
import json
import math
from numbers import Real
from pathlib import Path
import re
import sys
from typing import Any, Dict, Mapping, Optional, Sequence

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GroupKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from zerosum_common import RHO_GRID, read_jsonl  # noqa: E402


CHANCE_ACCURACY = 0.25
NORMALIZED_STYLE_MAX_ACCURACY = 0.35
_NUMBER = re.compile(r"(?<![A-Za-z0-9_])[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?")


def _valid_rho(value: Any) -> bool:
    return (
        isinstance(value, Real)
        and not isinstance(value, bool)
        and math.isfinite(value)
        and any(value == registered for registered in RHO_GRID)
    )


def _validated_records(records: Sequence[Mapping[str, Any]]) -> Sequence[Mapping[str, Any]]:
    if not isinstance(records, Sequence) or isinstance(records, (str, bytes)) or not records:
        raise ValueError("records must be a nonempty sequence")
    result = []
    for record in records:
        if not isinstance(record, Mapping):
            raise ValueError("every lexical record must be an object")
        if record.get("record_type") != "advice_primary":
            raise ValueError("lexical audit accepts advice_primary records only")
        if not _valid_rho(record.get("rho")):
            raise ValueError("lexical target is outside the registered rho grid")
        if not isinstance(record.get("core_id"), str) or not record["core_id"].strip():
            raise ValueError("lexical record is missing core_id")
        if not isinstance(record.get("id"), str) or not record["id"].strip():
            raise ValueError("lexical record is missing id")
        if not isinstance(record.get("model_prompt"), str) or not record["model_prompt"].strip():
            raise ValueError("lexical record is missing model_prompt")
        result.append(record)
    if len({record["id"] for record in result}) != len(result):
        raise ValueError("lexical record IDs must be unique")
    if len(result) != 160:
        raise ValueError("lexical audit requires exactly 160 primary records")
    by_core: Dict[str, list] = defaultdict(list)
    for record in result:
        by_core[record["core_id"]].append(record["rho"])
    if len(by_core) != 40:
        raise ValueError("lexical audit requires exactly 40 cores")
    if any(
        len(rhos) != len(RHO_GRID)
        or any(sum(value == registered for value in rhos) != 1 for registered in RHO_GRID)
        for rhos in by_core.values()
    ):
        raise ValueError("each lexical core must contain exactly one record at every rho")
    return result


def grouped_splits(
    records: Sequence[Mapping[str, Any]], *, group_key: str, folds: int = 5
) -> Sequence[Dict[str, Any]]:
    """Return deterministic indices with whole groups assigned to folds."""

    rows = _validated_records(records)
    if type(folds) is not int or folds < 2:
        raise ValueError("folds must be an integer of at least two")
    groups = [record.get(group_key) for record in rows]
    if any(not isinstance(group, str) or not group for group in groups):
        raise ValueError("group key must resolve to nonempty strings")
    if len(set(groups)) < folds:
        raise ValueError("number of groups must be at least folds")
    labels = [str(record["rho"]) for record in rows]
    splitter = GroupKFold(n_splits=folds)
    result = []
    for train, test in splitter.split(np.zeros(len(rows)), labels, groups):
        train_indices = [int(value) for value in train]
        test_indices = [int(value) for value in test]
        train_groups = sorted({groups[index] for index in train_indices})
        test_groups = sorted({groups[index] for index in test_indices})
        if set(train_groups).intersection(test_groups):
            raise AssertionError("grouped split leaked a core")
        result.append({
            "train_indices": train_indices,
            "test_indices": test_indices,
            "train_groups": train_groups,
            "test_groups": test_groups,
        })
    return result


def normalize_numbers(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return " ".join(_NUMBER.sub(" NUM ", text).split())


def _evaluate_text_baseline(
    texts: Sequence[str], labels: Sequence[str], splits: Sequence[Mapping[str, Any]], *, seed: int
) -> float:
    guesses = [None] * len(texts)
    for split in splits:
        train = split["train_indices"]
        test = split["test_indices"]
        pipeline = make_pipeline(
            CountVectorizer(lowercase=True, ngram_range=(1, 2), min_df=1),
            LogisticRegression(max_iter=2000, random_state=seed, C=1.0),
        )
        pipeline.fit([texts[index] for index in train], [labels[index] for index in train])
        predictions = pipeline.predict([texts[index] for index in test])
        for index, prediction in zip(test, predictions):
            guesses[index] = str(prediction)
    if any(value is None for value in guesses):
        raise AssertionError("cross-validation did not predict every row")
    return float(accuracy_score(labels, guesses))


def _evaluate_length_baseline(
    texts: Sequence[str], labels: Sequence[str], splits: Sequence[Mapping[str, Any]], *, seed: int
) -> float:
    features = np.asarray(
        [[len(text), len(text.split()), text.count("\n")] for text in texts], dtype=float
    )
    guesses = [None] * len(texts)
    for split in splits:
        train = split["train_indices"]
        test = split["test_indices"]
        pipeline = make_pipeline(
            StandardScaler(),
            LogisticRegression(max_iter=2000, random_state=seed),
        )
        pipeline.fit(features[train], [labels[index] for index in train])
        predictions = pipeline.predict(features[test])
        for index, prediction in zip(test, predictions):
            guesses[index] = str(prediction)
    return float(accuracy_score(labels, guesses))


def run_lexical_audit(
    records: Sequence[Mapping[str, Any]], *, retry_count: int, seed: int = 20260709
) -> Dict[str, Any]:
    """Run all frozen baselines and adjudicate normalized style only."""

    rows = _validated_records(records)
    if type(retry_count) is not int or retry_count not in (0, 1):
        raise ValueError("retry_count must be 0 or 1")
    splits = grouped_splits(rows, group_key="core_id", folds=5)
    labels = [str(record["rho"]) for record in rows]
    raw = [record["model_prompt"] for record in rows]
    normalized = [normalize_numbers(text) for text in raw]
    results = {
        "raw_bag_of_words": {
            "accuracy": _evaluate_text_baseline(raw, labels, splits, seed=seed),
            "decision_role": "diagnostic",
        },
        "normalized_style_bag_of_words": {
            "accuracy": _evaluate_text_baseline(normalized, labels, splits, seed=seed),
            "decision_role": "registered_gate",
        },
        "length_only": {
            "accuracy": _evaluate_length_baseline(raw, labels, splits, seed=seed),
            "decision_role": "diagnostic",
        },
    }
    passed = results["normalized_style_bag_of_words"]["accuracy"] <= NORMALIZED_STYLE_MAX_ACCURACY
    status = "PASS" if passed else ("REWORK_AUTHORIZED" if retry_count == 0 else "PARK")
    return {
        "schema_version": 1,
        "audit": "X2 lexical/length",
        "target": "rho_class",
        "split_unit": "core_id",
        "folds": 5,
        "n_records": len(rows),
        "n_cores": len({record["core_id"] for record in rows}),
        "chance_accuracy": CHANCE_ACCURACY,
        "normalized_style_max_accuracy": NORMALIZED_STYLE_MAX_ACCURACY,
        "baselines": results,
        "normalized_style_status": status,
        "retry_count": retry_count,
        "eligible_for_x2_lexical_gate": True,
    }


def _write_reports(result: Mapping[str, Any], output_dir: Path, report_date: str) -> None:
    parsed = date.fromisoformat(report_date)
    output_dir.mkdir(parents=True, exist_ok=True)
    prefix = parsed.strftime("%Y%m%d") + "-x2-lexical"
    (output_dir / (prefix + ".json")).write_text(
        json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8"
    )
    lines = [
        "# ZEROSUM X2 lexical audit", "",
        "- Status: `%s`" % result["normalized_style_status"],
        "- Split unit: `core_id`", "- Chance: %.2f" % result["chance_accuracy"],
        "- Registered normalized-style maximum: %.2f" % result["normalized_style_max_accuracy"],
        "",
    ]
    for name, baseline in result["baselines"].items():
        lines.append("- %s accuracy: %.4f" % (name, baseline["accuracy"]))
    (output_dir / (prefix + ".md")).write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bank", type=Path, default=ROOT / "itembank/bank/p1-private.jsonl")
    parser.add_argument("--retry-count", type=int, default=0)
    parser.add_argument("--seed", type=int, default=20260709)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).parent / "reports")
    parser.add_argument("--report-date", default=date.today().isoformat())
    args = parser.parse_args(argv)
    records = [row for row in read_jsonl(args.bank) if row.get("record_type") == "advice_primary"]
    result = run_lexical_audit(records, retry_count=args.retry_count, seed=args.seed)
    _write_reports(result, args.output_dir, args.report_date)
    return 0 if result["normalized_style_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["grouped_splits", "normalize_numbers", "run_lexical_audit"]
