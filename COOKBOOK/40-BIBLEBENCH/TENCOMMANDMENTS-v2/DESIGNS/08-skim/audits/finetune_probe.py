#!/usr/bin/env python3
"""Core-grouped 10% SKIM X2 LLM probe and ineligible surrogate diagnostic."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from pathlib import Path
import random
import sys
from typing import Any, Dict

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from audits.lexical_baseline import (  # noqa: E402
    normalized_prose_style_text,
    source_records_sha256,
    validate_primary_records,
)
from skim_constants import (  # noqa: E402
    GATE_THRESHOLDS,
    MAGNITUDE_TIERS,
    SCENARIO_CORES,
    X2_PROBE_RULES,
)
from skim_hashing import canonical_json, canonical_sha256  # noqa: E402


_PREDICTION_KEYS = frozenset(("item_id", "predicted_magnitude_tier"))

PREREGISTERED_PROBE_SEED = 2026071001
PREREGISTERED_SOURCE_RECORDS_SHA256 = (
    "21c0031062348e9c753a72cdf45147e8b3f1ffa378acfc805ba61803a44f2886"
)
PREREGISTERED_MANIFEST_SHA256 = (
    "236db36b29c0555634a0c41f7bdf20c9774c0b7d9d3908396e3b1cb8313caebf"
)


def build_probe_manifest(
    records: Sequence[Mapping[str, Any]], *, seed: int
) -> Dict[str, Any]:
    """Freeze exactly 10% of scenario cores as the fine-tune partition."""

    rows = validate_primary_records(records)
    if type(seed) is not int or seed != PREREGISTERED_PROBE_SEED:
        raise ValueError("seed must equal the preregistered probe seed")
    source_hash = source_records_sha256(rows)
    if source_hash != PREREGISTERED_SOURCE_RECORDS_SHA256:
        raise ValueError("records do not match the preregistered source hash")
    cores = sorted({row["core_id"] for row in rows})
    if len(cores) != SCENARIO_CORES:
        raise ValueError("probe manifest requires exactly 40 cores")
    shuffled = list(cores)
    random.Random(seed).shuffle(shuffled)
    train_core_count = int(
        SCENARIO_CORES * X2_PROBE_RULES["finetune_training_fraction"]
    )
    if train_core_count != 4:
        raise AssertionError("frozen 10% core partition does not select four cores")
    train_cores = sorted(shuffled[:train_core_count])
    heldout_cores = sorted(shuffled[train_core_count:])
    train_ids = sorted(
        row["logical_record_id"]
        for row in rows
        if row["core_id"] in train_cores
    )
    heldout_ids = sorted(
        row["logical_record_id"]
        for row in rows
        if row["core_id"] in heldout_cores
    )
    if set(train_cores).intersection(heldout_cores):
        raise AssertionError("fine-tune manifest leaked a scenario core")
    if set(train_ids).intersection(heldout_ids):
        raise AssertionError("fine-tune manifest leaked an item")
    by_id = {row["logical_record_id"]: row for row in rows}
    manifest = {
        "schema_version": 1,
        "study_id": "SKIM-P1",
        "probe": "X2_10_PERCENT_FINETUNE",
        "seed": seed,
        "target": "magnitude_tier",
        "target_classes": list(MAGNITUDE_TIERS),
        "split_unit": X2_PROBE_RULES["finetune_split_unit"],
        "group_key": "core_id",
        "train_fraction_by_core": float(
            X2_PROBE_RULES["finetune_training_fraction"]
        ),
        "source_records_sha256": source_hash,
        "train_core_ids": train_cores,
        "heldout_core_ids": heldout_cores,
        "train_item_ids": train_ids,
        "heldout_item_ids": heldout_ids,
        "heldout_target_by_item": {
            item_id: by_id[item_id]["magnitude_tier"]
            for item_id in heldout_ids
        },
        "synthetic": False,
    }
    manifest["manifest_sha256"] = canonical_sha256(manifest)
    if manifest["manifest_sha256"] != PREREGISTERED_MANIFEST_SHA256:
        raise AssertionError("derived probe manifest differs from preregistration")
    return manifest


def _prediction_map(
    predictions: Sequence[Mapping[str, Any]],
) -> Dict[str, int]:
    if (
        not isinstance(predictions, Sequence)
        or isinstance(predictions, (str, bytes, bytearray))
    ):
        raise ValueError("predictions must be a sequence")
    result: Dict[str, int] = {}
    for row in predictions:
        if not isinstance(row, Mapping) or set(row) != _PREDICTION_KEYS:
            raise ValueError("prediction schema mismatch")
        item_id = row.get("item_id")
        predicted = row.get("predicted_magnitude_tier")
        if not isinstance(item_id, str) or not item_id.strip():
            raise ValueError("prediction is missing item_id")
        if item_id in result:
            raise ValueError("prediction item IDs must be unique")
        if type(predicted) is not int or predicted not in MAGNITUDE_TIERS:
            raise ValueError(
                "predicted_magnitude_tier is outside the registered grid"
            )
        result[item_id] = predicted
    return result


def prediction_sha256(predictions: Sequence[Mapping[str, Any]]) -> str:
    """Hash exactly the submitted item/tier prediction artifact."""

    by_id = _prediction_map(predictions)
    canonical = [
        {
            "item_id": item_id,
            "predicted_magnitude_tier": by_id[item_id],
        }
        for item_id in sorted(by_id)
    ]
    return canonical_sha256(canonical)


def _validate_manifest(
    manifest: Mapping[str, Any],
    source_records: Sequence[Mapping[str, Any]],
) -> Mapping[str, int]:
    if not isinstance(manifest, Mapping):
        raise ValueError("probe manifest must be an object")
    required = {
        "schema_version",
        "study_id",
        "probe",
        "seed",
        "target",
        "target_classes",
        "split_unit",
        "group_key",
        "train_fraction_by_core",
        "source_records_sha256",
        "train_core_ids",
        "heldout_core_ids",
        "train_item_ids",
        "heldout_item_ids",
        "heldout_target_by_item",
        "synthetic",
        "manifest_sha256",
    }
    if set(manifest) != required:
        raise ValueError("probe manifest schema mismatch")
    payload = {
        key: manifest[key]
        for key in manifest
        if key != "manifest_sha256"
    }
    if manifest.get("manifest_sha256") != canonical_sha256(payload):
        raise ValueError("probe manifest hash mismatch")
    seed = manifest.get("seed")
    if type(seed) is not int or seed < 0:
        raise ValueError("probe manifest seed is invalid")
    expected = build_probe_manifest(source_records, seed=seed)
    if canonical_json(dict(manifest)) != canonical_json(expected):
        raise ValueError(
            "probe manifest does not match canonical source records and seed"
        )
    return expected["heldout_target_by_item"]


def _prediction_accuracy(
    predictions: Sequence[Mapping[str, Any]],
    expected_targets: Mapping[str, int],
) -> float:
    by_id = _prediction_map(predictions)
    if set(by_id) != set(expected_targets):
        raise ValueError("predictions must exactly cover heldout item IDs")
    return sum(
        by_id[item_id] == expected_targets[item_id]
        for item_id in expected_targets
    ) / len(expected_targets)


def evaluate_llm_probe(
    manifest: Mapping[str, Any],
    pre_predictions: Sequence[Mapping[str, Any]],
    post_predictions: Sequence[Mapping[str, Any]],
    *,
    evidence: Mapping[str, Any],
    source_records: Sequence[Mapping[str, Any]],
) -> Dict[str, Any]:
    """Evaluate candidate arrays without asserting that an LLM run occurred.

    Plain mappings cannot prove model/provider identity, transport calls,
    training, or event-chain custody. Until a real execution-bundle verifier is
    implemented, this function is diagnostic and always returns NOT_RUN_LLM.
    """

    targets = _validate_manifest(manifest, source_records)
    if not isinstance(evidence, Mapping):
        raise ValueError("probe evidence must be an object")
    canonical_json(dict(evidence))
    pre_accuracy = _prediction_accuracy(pre_predictions, targets)
    post_accuracy = _prediction_accuracy(post_predictions, targets)
    lift = post_accuracy - pre_accuracy
    pre_hash = prediction_sha256(pre_predictions)
    post_hash = prediction_sha256(post_predictions)
    lift_park_min = float(GATE_THRESHOLDS["x2_finetune_lift_park_min"])
    return {
        "schema_version": 1,
        "study_id": "SKIM-P1",
        "probe": "X2_10_PERCENT_FINETUNE",
        "data_basis": "unverified_candidate_arrays",
        "synthetic": None,
        "eligible_for_empirical_decision": False,
        "eligible_for_x2_finetune_gate": False,
        "evidence_status": (
            "CANDIDATE_ARRAYS_ONLY_NO_EXECUTION_BUNDLE_VERIFIER"
        ),
        "blockers": ["NO_EXECUTION_BUNDLE_VERIFIER"],
        "manifest_sha256": manifest["manifest_sha256"],
        "source_records_sha256": manifest["source_records_sha256"],
        "pre_predictions_sha256": pre_hash,
        "post_predictions_sha256": post_hash,
        "pre_accuracy": pre_accuracy,
        "post_accuracy": post_accuracy,
        "lift": lift,
        "lift_park_min": lift_park_min,
        "verdict": "NOT_RUN_LLM",
        "candidate_claims": dict(evidence),
    }


def run_surrogate_probe(
    records: Sequence[Mapping[str, Any]], *, seed: int
) -> Dict[str, Any]:
    """Validate grouped split/statistic plumbing with a non-gating classifier."""

    rows = validate_primary_records(records)
    manifest = build_probe_manifest(rows, seed=seed)
    by_id = {row["logical_record_id"]: row for row in rows}
    train = [by_id[item_id] for item_id in manifest["train_item_ids"]]
    heldout = [by_id[item_id] for item_id in manifest["heldout_item_ids"]]
    pipeline = make_pipeline(
        CountVectorizer(lowercase=True, ngram_range=(1, 2), min_df=1),
        LogisticRegression(max_iter=2000, random_state=seed, C=1.0),
    )
    pipeline.fit(
        [normalized_prose_style_text(row) for row in train],
        [str(row["magnitude_tier"]) for row in train],
    )
    predictions = pipeline.predict(
        [normalized_prose_style_text(row) for row in heldout]
    )
    accuracy = sum(
        str(prediction) == str(row["magnitude_tier"])
        for prediction, row in zip(predictions, heldout)
    ) / len(heldout)
    return {
        "schema_version": 1,
        "study_id": "SKIM-P1",
        "probe": "X2_10_PERCENT_FINETUNE_SURROGATE",
        "data_basis": "classical_surrogate",
        "synthetic": True,
        "diagnostic_only": True,
        "eligible_for_empirical_decision": False,
        "eligible_for_x2_finetune_gate": False,
        "llm_probe_status": "NOT_RUN_LLM",
        "surrogate_role": "SPLIT_AND_STATISTIC_PLUMBING_ONLY",
        "manifest": manifest,
        "heldout_accuracy": float(accuracy),
        "chance_accuracy": float(
            GATE_THRESHOLDS["x2_lexical_chance_accuracy"]
        ),
        "lift_park_min": float(
            GATE_THRESHOLDS["x2_finetune_lift_park_min"]
        ),
    }


__all__ = [
    "PREREGISTERED_MANIFEST_SHA256",
    "PREREGISTERED_PROBE_SEED",
    "PREREGISTERED_SOURCE_RECORDS_SHA256",
    "build_probe_manifest",
    "evaluate_llm_probe",
    "prediction_sha256",
    "run_surrogate_probe",
]
