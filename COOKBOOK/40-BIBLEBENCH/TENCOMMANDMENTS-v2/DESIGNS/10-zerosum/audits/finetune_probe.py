#!/usr/bin/env python3
"""Core-grouped 10% LLM probe protocol plus ineligible classical surrogate."""

from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import date
import hashlib
import json
import math
from numbers import Real
from pathlib import Path
import random
import sys
from typing import Any, Dict, Mapping, Optional, Sequence

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from audits.lexical_baseline import normalize_numbers  # noqa: E402
from zerosum_common import RHO_GRID, read_jsonl  # noqa: E402


MAX_LIFT_EXCLUSIVE = 0.15
_PREDICTION_KEYS = frozenset(("item_id", "predicted_rho"))
_EVIDENCE_KEYS = frozenset((
    "probe_type", "data_basis", "model_id", "vendor", "pre_registered",
    "manifest_sha256", "pre_predictions_sha256", "post_predictions_sha256",
))


def _valid_rho(value: Any) -> bool:
    return (
        isinstance(value, Real)
        and not isinstance(value, bool)
        and math.isfinite(value)
        and any(value == registered for registered in RHO_GRID)
    )


def _sha256_json(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
    ).hexdigest()


def _validate_records(records: Sequence[Mapping[str, Any]]) -> Sequence[Mapping[str, Any]]:
    if not isinstance(records, Sequence) or isinstance(records, (str, bytes)) or not records:
        raise ValueError("records must be a nonempty sequence")
    result = []
    for row in records:
        if not isinstance(row, Mapping) or row.get("record_type") != "advice_primary":
            raise ValueError("probe requires valid primary records")
        if not _valid_rho(row.get("rho")):
            raise ValueError("probe rho is outside the registered grid")
        if (
            not isinstance(row.get("core_id"), str)
            or not row["core_id"].strip()
            or not isinstance(row.get("id"), str)
            or not row["id"].strip()
            or not isinstance(row.get("model_prompt"), str)
            or not row["model_prompt"].strip()
        ):
            raise ValueError("probe requires valid primary records")
        result.append(row)
    if len({row["id"] for row in result}) != len(result):
        raise ValueError("probe item IDs must be unique")
    if len(result) != 160:
        raise ValueError("probe requires exactly 160 primary records")
    by_core: Dict[str, list] = defaultdict(list)
    for row in result:
        by_core[row["core_id"]].append(row["rho"])
    if len(by_core) != 40:
        raise ValueError("probe requires exactly 40 cores")
    if any(
        len(rhos) != len(RHO_GRID)
        or any(sum(value == registered for value in rhos) != 1 for registered in RHO_GRID)
        for rhos in by_core.values()
    ):
        raise ValueError("each probe core must contain exactly one record at every rho")
    return result


def _source_records_sha256(records: Sequence[Mapping[str, Any]]) -> str:
    canonical = sorted(
        (dict(row) for row in records),
        key=lambda row: row["id"],
    )
    return _sha256_json(canonical)


def build_probe_manifest(
    records: Sequence[Mapping[str, Any]], *, seed: int
) -> Dict[str, Any]:
    """Freeze exactly 10% of scenario cores as the fine-tune partition."""

    rows = _validate_records(records)
    if type(seed) is not int or seed < 0:
        raise ValueError("seed must be a nonnegative integer")
    cores = sorted({row["core_id"] for row in rows})
    if len(cores) != 40:
        raise ValueError("P1 probe manifest requires exactly 40 cores")
    shuffled = list(cores)
    random.Random(seed).shuffle(shuffled)
    train_cores = sorted(shuffled[:4])
    heldout_cores = sorted(shuffled[4:])
    train_ids = sorted(row["id"] for row in rows if row["core_id"] in train_cores)
    heldout_ids = sorted(row["id"] for row in rows if row["core_id"] in heldout_cores)
    if set(train_cores).intersection(heldout_cores):
        raise AssertionError("probe manifest leaked a core")
    by_id = {row["id"]: row for row in rows}
    target_by_item = {item_id: by_id[item_id]["rho"] for item_id in heldout_ids}
    manifest = {
        "schema_version": 1,
        "seed": seed,
        "group_key": "core_id",
        "target": "rho_class",
        "source_records_sha256": _source_records_sha256(rows),
        "train_fraction_by_core": 0.10,
        "train_core_ids": train_cores,
        "heldout_core_ids": heldout_cores,
        "train_item_ids": train_ids,
        "heldout_item_ids": heldout_ids,
        "heldout_target_by_item": target_by_item,
    }
    manifest["manifest_sha256"] = _sha256_json(manifest)
    return manifest


def _prediction_map(predictions: Sequence[Mapping[str, Any]]) -> Dict[str, Real]:
    if not isinstance(predictions, Sequence) or isinstance(predictions, (str, bytes)):
        raise ValueError("predictions must be a sequence")
    by_id: Dict[str, Real] = {}
    for row in predictions:
        if (
            not isinstance(row, Mapping)
            or set(row) != set(_PREDICTION_KEYS)
            or not isinstance(row.get("item_id"), str)
            or not row["item_id"].strip()
        ):
            raise ValueError("prediction is missing item_id")
        if row["item_id"] in by_id:
            raise ValueError("prediction item IDs must be unique")
        predicted = row.get("predicted_rho")
        if not _valid_rho(predicted):
            raise ValueError("prediction predicted_rho is outside the registered grid")
        by_id[row["item_id"]] = predicted
    return by_id


def prediction_sha256(predictions: Sequence[Mapping[str, Any]]) -> str:
    """Hash exactly the submitted item-id/predicted-rho artifact."""

    by_id = _prediction_map(predictions)
    canonical = [
        {"item_id": item_id, "predicted_rho": by_id[item_id]}
        for item_id in sorted(by_id)
    ]
    return _sha256_json(canonical)


def _prediction_accuracy(
    predictions: Sequence[Mapping[str, Any]], expected_targets: Mapping[str, float]
) -> float:
    by_id = _prediction_map(predictions)
    if set(by_id) != set(expected_targets):
        raise ValueError("predictions must exactly cover heldout item IDs")
    return sum(
        by_id[item_id] == expected_targets[item_id] for item_id in expected_targets
    ) / len(expected_targets)


def _validate_manifest(
    manifest: Mapping[str, Any], source_records: Sequence[Mapping[str, Any]]
) -> Mapping[str, float]:
    if not isinstance(manifest, Mapping):
        raise ValueError("probe manifest must be an object")
    required = {
        "schema_version", "seed", "group_key", "target", "train_fraction_by_core",
        "train_core_ids", "heldout_core_ids", "train_item_ids", "heldout_item_ids",
        "heldout_target_by_item", "source_records_sha256", "manifest_sha256",
    }
    if set(manifest) != required:
        raise ValueError("probe manifest schema mismatch")
    payload = {key: manifest[key] for key in manifest if key != "manifest_sha256"}
    recomputed = _sha256_json(payload)
    if manifest["manifest_sha256"] != recomputed:
        raise ValueError("probe manifest hash mismatch")
    if type(manifest.get("seed")) is not int or manifest["seed"] < 0:
        raise ValueError("probe manifest seed is invalid")
    expected = build_probe_manifest(source_records, seed=manifest["seed"])
    if dict(manifest) != expected:
        raise ValueError("probe manifest does not match canonical source records and seed")
    return expected["heldout_target_by_item"]


def _eligible_llm_evidence(
    evidence: Mapping[str, Any], *, manifest_sha256: str,
    pre_predictions_sha256: str, post_predictions_sha256: str,
) -> bool:
    return (
        isinstance(evidence, Mapping)
        and set(evidence) == set(_EVIDENCE_KEYS)
        and evidence.get("probe_type") == "mid_tier_llm"
        and evidence.get("data_basis") in {"live", "empirical"}
        and isinstance(evidence.get("model_id"), str)
        and evidence["model_id"] == " ".join(evidence["model_id"].split())
        and bool(evidence["model_id"])
        and isinstance(evidence.get("vendor"), str)
        and evidence["vendor"] == " ".join(evidence["vendor"].split())
        and bool(evidence["vendor"])
        and evidence.get("pre_registered") is True
        and evidence.get("manifest_sha256") == manifest_sha256
        and evidence.get("pre_predictions_sha256") == pre_predictions_sha256
        and evidence.get("post_predictions_sha256") == post_predictions_sha256
    )


def evaluate_llm_probe(
    manifest: Mapping[str, Any],
    pre_predictions: Sequence[Mapping[str, Any]],
    post_predictions: Sequence[Mapping[str, Any]],
    *,
    evidence: Mapping[str, Any],
    source_records: Sequence[Mapping[str, Any]],
) -> Dict[str, Any]:
    """Compute held-out lift; only registered mid-tier LLM evidence is eligible."""

    targets = _validate_manifest(manifest, source_records)
    pre_accuracy = _prediction_accuracy(pre_predictions, targets)
    post_accuracy = _prediction_accuracy(post_predictions, targets)
    lift = post_accuracy - pre_accuracy
    pre_hash = prediction_sha256(pre_predictions)
    post_hash = prediction_sha256(post_predictions)
    eligible = _eligible_llm_evidence(
        evidence,
        manifest_sha256=manifest["manifest_sha256"],
        pre_predictions_sha256=pre_hash,
        post_predictions_sha256=post_hash,
    )
    return {
        "schema_version": 1,
        "manifest_sha256": manifest.get("manifest_sha256"),
        "source_records_sha256": manifest.get("source_records_sha256"),
        "pre_predictions_sha256": pre_hash,
        "post_predictions_sha256": post_hash,
        "pre_accuracy": pre_accuracy,
        "post_accuracy": post_accuracy,
        "lift": lift,
        "max_lift_exclusive": MAX_LIFT_EXCLUSIVE,
        "eligible_for_x2_finetune_gate": eligible,
        "verdict": ("PASS" if lift < MAX_LIFT_EXCLUSIVE else "PARK") if eligible else "NOT_RUN_LLM",
        "evidence": dict(evidence),
    }


def run_surrogate_probe(
    records: Sequence[Mapping[str, Any]], *, seed: int
) -> Dict[str, Any]:
    """Validate split/statistic plumbing with a classical, non-gating model."""

    rows = _validate_records(records)
    manifest = build_probe_manifest(rows, seed=seed)
    by_id = {row["id"]: row for row in rows}
    train = [by_id[item_id] for item_id in manifest["train_item_ids"]]
    heldout = [by_id[item_id] for item_id in manifest["heldout_item_ids"]]
    pipeline = make_pipeline(
        CountVectorizer(ngram_range=(1, 2)),
        LogisticRegression(max_iter=2000, random_state=seed),
    )
    pipeline.fit(
        [normalize_numbers(row["model_prompt"]) for row in train],
        [str(row["rho"]) for row in train],
    )
    predictions = pipeline.predict(
        [normalize_numbers(row["model_prompt"]) for row in heldout]
    )
    accuracy = sum(
        str(prediction) == str(row["rho"])
        for prediction, row in zip(predictions, heldout)
    ) / len(heldout)
    return {
        "schema_version": 1,
        "data_basis": "classical_surrogate",
        "diagnostic_only": True,
        "manifest": manifest,
        "heldout_accuracy": accuracy,
        "chance_accuracy": 0.25,
        "eligible_for_x2_finetune_gate": False,
        "llm_probe_status": "NOT_RUN_LLM",
        "max_lift_exclusive": MAX_LIFT_EXCLUSIVE,
    }


def _write_result(result: Mapping[str, Any], output_dir: Path, report_date: str) -> None:
    parsed = date.fromisoformat(report_date)
    output_dir.mkdir(parents=True, exist_ok=True)
    prefix = parsed.strftime("%Y%m%d") + "-x2-finetune-probe"
    (output_dir / (prefix + ".json")).write_text(
        json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8"
    )
    lines = [
        "# ZEROSUM X2 10% fine-tune probe", "",
        "- LLM probe status: `%s`" % result.get("llm_probe_status", result.get("verdict")),
        "- eligible_for_x2_finetune_gate: `%s`" % str(result["eligible_for_x2_finetune_gate"]).lower(),
        "- Registered lift maximum (exclusive): %.2f" % MAX_LIFT_EXCLUSIVE,
        "",
        "A classical surrogate validates only the grouped split and statistic plumbing; it cannot discharge the required mid-tier LLM probe.",
    ]
    (output_dir / (prefix + ".md")).write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bank", type=Path, default=ROOT / "itembank/bank/p1-private.jsonl")
    parser.add_argument("--seed", type=int, default=20260709)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).parent / "reports")
    parser.add_argument("--report-date", default=date.today().isoformat())
    args = parser.parse_args(argv)
    records = [row for row in read_jsonl(args.bank) if row.get("record_type") == "advice_primary"]
    result = run_surrogate_probe(records, seed=args.seed)
    _write_result(result, args.output_dir, args.report_date)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "build_probe_manifest", "evaluate_llm_probe", "prediction_sha256",
    "run_surrogate_probe",
]
