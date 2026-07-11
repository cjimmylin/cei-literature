#!/usr/bin/env python3
"""Core-grouped X2 lexical, prose/style, and length baselines for SKIM P1."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Mapping, Sequence
import json
import math
from pathlib import Path
import re
import sys
from typing import Any, Dict, Final, List, Optional

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from skim_constants import (  # noqa: E402
    GATE_THRESHOLDS,
    MAGNITUDE_TIERS,
    SCENARIO_CORES,
    X2_PROBE_RULES,
)
from skim_hashing import canonical_json, canonical_sha256  # noqa: E402


_PUBLIC_REQUEST_KEYS = (
    "options",
    "prompt",
    "response_schema",
    "structured_state",
    "tool_schema",
    "traceability",
)
_NUMBER = re.compile(
    r"(?<![A-Za-z0-9_])[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"
)
_PUNCTUATION_AFTER_SPACE = re.compile(r"\s+([,;:.!?])")
PREREGISTERED_X2_SOURCE_RECORDS_SHA256: Final[str] = (
    "21c0031062348e9c753a72cdf45147e8b3f1ffa378acfc805ba61803a44f2886"
)
PREREGISTERED_LEXICAL_CLASSIFIER_SEED: Final[int] = 2026071001
AUTHORIZED_REVISED_SOURCE_SHA256: Final[Optional[str]] = None
_PREREGISTERED_BANK_PATH = ROOT / "itembank" / "bank" / "p1-public.jsonl"
_LEXICAL_RESULT_KEYS = frozenset(
    {
        "schema_version",
        "study_id",
        "audit",
        "data_basis",
        "synthetic",
        "eligible_for_empirical_decision",
        "eligible_for_x2_lexical_gate",
        "source_records_sha256",
        "source_status",
        "authorized_revised_source_sha256",
        "revision_authorization_status",
        "target",
        "target_classes",
        "split_unit",
        "group_key",
        "folds",
        "fold_test_core_ids",
        "n_records",
        "n_cores",
        "classifier_seed",
        "chance_accuracy",
        "normalized_style_max_accuracy",
        "baselines",
        "normalized_style_status",
        "surface_rework_count",
        "surface_rework_max",
        "second_failure_action",
        "prior_result_sha256",
        "result_sha256",
    }
)


def normalize_numbers(text: str) -> str:
    """Replace standalone numeric surface forms while retaining prose/style."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    normalized = " ".join(_NUMBER.sub(" NUM ", text).split())
    return _PUNCTUATION_AFTER_SPACE.sub(r"\1", normalized)


def _request_projection(record: Mapping[str, Any]) -> Dict[str, Any]:
    requests = record.get("requests")
    if (
        not isinstance(requests, Sequence)
        or isinstance(requests, (str, bytes, bytearray))
        or len(requests) != 1
        or not isinstance(requests[0], Mapping)
    ):
        raise ValueError("each primary record must contain exactly one request")
    request = requests[0]
    if request.get("request_kind") != "action":
        raise ValueError("primary X2 records must contain an action request")
    missing = [key for key in _PUBLIC_REQUEST_KEYS if key not in request]
    if missing:
        raise ValueError("primary request is missing public projection fields")
    return {key: request[key] for key in _PUBLIC_REQUEST_KEYS}


def validate_primary_records(
    records: Sequence[Mapping[str, Any]],
) -> List[Mapping[str, Any]]:
    """Validate the exact 40-core by four-tier SKIM primary corpus."""

    if (
        not isinstance(records, Sequence)
        or isinstance(records, (str, bytes, bytearray))
        or not records
    ):
        raise ValueError("records must be a nonempty sequence")
    rows: List[Mapping[str, Any]] = []
    for record in records:
        if not isinstance(record, Mapping) or record.get("record_type") != "primary":
            raise ValueError("X2 accepts SKIM primary records only")
        record_id = record.get("logical_record_id")
        core_id = record.get("core_id")
        tier = record.get("magnitude_tier")
        if not isinstance(record_id, str) or not record_id.strip():
            raise ValueError("primary record is missing logical_record_id")
        if not isinstance(core_id, str) or not core_id.strip():
            raise ValueError("primary record is missing core_id")
        if type(tier) is not int or tier not in MAGNITUDE_TIERS:
            raise ValueError("primary magnitude tier is outside the registered grid")
        _request_projection(record)
        rows.append(record)

    if len(rows) != SCENARIO_CORES * len(MAGNITUDE_TIERS):
        raise ValueError("X2 requires exactly 160 primary records")
    record_ids = [row["logical_record_id"] for row in rows]
    if len(set(record_ids)) != len(record_ids):
        raise ValueError("primary logical_record_id values must be unique")

    by_core: Dict[str, List[int]] = defaultdict(list)
    for row in rows:
        by_core[row["core_id"]].append(row["magnitude_tier"])
    if len(by_core) != SCENARIO_CORES:
        raise ValueError("X2 requires exactly 40 cores")
    registered = list(MAGNITUDE_TIERS)
    if any(sorted(tiers) != registered for tiers in by_core.values()):
        raise ValueError("each core must contain every registered magnitude tier once")
    return rows


def source_records_sha256(records: Sequence[Mapping[str, Any]]) -> str:
    """Bind a source corpus independent of its incoming row order."""

    rows = validate_primary_records(records)
    canonical = sorted(
        (dict(row) for row in rows),
        key=lambda row: row["logical_record_id"],
    )
    return canonical_sha256(canonical)


def grouped_splits(
    records: Sequence[Mapping[str, Any]], *, group_key: str, folds: int = 5
) -> List[Dict[str, Any]]:
    """Return deterministic folds that keep every scenario core intact."""

    rows = validate_primary_records(records)
    if not isinstance(group_key, str) or not group_key.strip():
        raise ValueError("group_key must be nonblank text")
    if type(folds) is not int or folds < 2:
        raise ValueError("folds must be an integer of at least two")
    groups = [row.get(group_key) for row in rows]
    if any(not isinstance(group, str) or not group.strip() for group in groups):
        raise ValueError("group_key must resolve to nonblank strings")
    if len(set(groups)) < folds:
        raise ValueError("number of groups must be at least folds")
    # Freeze GroupKFold's stable equal-weight tie behavior explicitly.  Older
    # scikit-learn releases used an unstable NumPy argsort here, so the same
    # 40 equal-sized cores landed in different folds across environments.
    group_counts = {group: groups.count(group) for group in sorted(set(groups))}
    ordered_groups = sorted(
        group_counts,
        key=lambda group: (group_counts[group], group),
        reverse=True,
    )
    fold_sizes = [0] * folds
    group_to_fold: Dict[str, int] = {}
    for group in ordered_groups:
        lightest = min(range(folds), key=lambda index: (fold_sizes[index], index))
        group_to_fold[group] = lightest
        fold_sizes[lightest] += group_counts[group]

    result: List[Dict[str, Any]] = []
    for fold in range(folds):
        test_indices = [
            index for index, group in enumerate(groups) if group_to_fold[group] == fold
        ]
        train_indices = [
            index for index, group in enumerate(groups) if group_to_fold[group] != fold
        ]
        train_groups = sorted({groups[index] for index in train_indices})
        test_groups = sorted({groups[index] for index in test_indices})
        if set(train_groups).intersection(test_groups):
            raise AssertionError("grouped split leaked a scenario core")
        result.append(
            {
                "train_indices": train_indices,
                "test_indices": test_indices,
                "train_groups": train_groups,
                "test_groups": test_groups,
            }
        )
    return result


def _string_leaves(value: Any) -> List[str]:
    if isinstance(value, Mapping):
        result: List[str] = []
        for key in sorted(value):
            result.extend(_string_leaves(value[key]))
        return result
    if isinstance(value, Sequence) and not isinstance(
        value, (str, bytes, bytearray)
    ):
        result = []
        for child in value:
            result.extend(_string_leaves(child))
        return result
    return [value] if isinstance(value, str) else []


def raw_structured_text(record: Mapping[str, Any]) -> str:
    """Return exact public structured request JSON for the diagnostic baseline."""

    return canonical_json(_request_projection(record))


def normalized_prose_style_text(record: Mapping[str, Any]) -> str:
    """Return only public string leaves, with standalone numbers normalized."""

    projection = _request_projection(record)
    return normalize_numbers("\n".join(_string_leaves(projection)))


def _evaluate_text_baseline(
    texts: Sequence[str],
    labels: Sequence[str],
    splits: Sequence[Mapping[str, Any]],
    *,
    seed: int,
) -> float:
    guesses: List[Any] = [None] * len(texts)
    for split in splits:
        train = split["train_indices"]
        test = split["test_indices"]
        pipeline = make_pipeline(
            CountVectorizer(lowercase=True, ngram_range=(1, 2), min_df=1),
            LogisticRegression(max_iter=2000, random_state=seed, C=1.0),
        )
        pipeline.fit(
            [texts[index] for index in train],
            [labels[index] for index in train],
        )
        predictions = pipeline.predict([texts[index] for index in test])
        for index, prediction in zip(test, predictions):
            guesses[index] = str(prediction)
    if any(value is None for value in guesses):
        raise AssertionError("cross-validation did not predict every record")
    return float(accuracy_score(labels, guesses))


def _evaluate_length_baseline(
    texts: Sequence[str],
    labels: Sequence[str],
    splits: Sequence[Mapping[str, Any]],
    *,
    seed: int,
) -> float:
    features = np.asarray(
        [[len(text), len(text.split())] for text in texts], dtype=float
    )
    guesses: List[Any] = [None] * len(texts)
    for split in splits:
        train = split["train_indices"]
        test = split["test_indices"]
        pipeline = make_pipeline(
            StandardScaler(),
            LogisticRegression(max_iter=2000, random_state=seed),
        )
        pipeline.fit(
            features[train],
            [labels[index] for index in train],
        )
        predictions = pipeline.predict(features[test])
        for index, prediction in zip(test, predictions):
            guesses[index] = str(prediction)
    if any(value is None for value in guesses):
        raise AssertionError("cross-validation did not predict every record")
    return float(accuracy_score(labels, guesses))


def _preregistered_primary_records() -> List[Mapping[str, Any]]:
    rows = []
    for line in _PREREGISTERED_BANK_PATH.read_text(
        encoding="utf-8"
    ).splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if not isinstance(row, Mapping):
            raise ValueError("preregistered bank row must be an object")
        if row.get("record_type") == "primary":
            rows.append(row)
    validate_primary_records(rows)
    if source_records_sha256(rows) != PREREGISTERED_X2_SOURCE_RECORDS_SHA256:
        raise ValueError("preregistered lexical source hash mismatch")
    return rows


def _validate_surface_only_revision(
    revised_records: Sequence[Mapping[str, Any]],
) -> None:
    """Allow prompt prose changes while holding every other public field fixed."""

    frozen = _preregistered_primary_records()
    frozen_by_id = {row["logical_record_id"]: row for row in frozen}
    revised_by_id = {
        row["logical_record_id"]: row
        for row in validate_primary_records(revised_records)
    }
    if set(frozen_by_id) != set(revised_by_id):
        raise ValueError("revision is not an exact surface-only revision")
    changed = False
    sentinel = "SKIM-X2-PERMITTED-SURFACE-PROMPT"
    for record_id in sorted(frozen_by_id):
        before = json.loads(canonical_json(frozen_by_id[record_id]))
        after = json.loads(canonical_json(revised_by_id[record_id]))
        before_prompt = before["requests"][0]["prompt"]
        after_prompt = after["requests"][0]["prompt"]
        if (
            not isinstance(after_prompt, str)
            or not after_prompt.strip()
            or after_prompt != after_prompt.strip()
        ):
            raise ValueError("revision prompt is not valid surface prose")
        changed = changed or before_prompt != after_prompt
        before["requests"][0]["prompt"] = sentinel
        after["requests"][0]["prompt"] = sentinel
        if canonical_json(before) != canonical_json(after):
            raise ValueError("revision is not an exact surface-only revision")
    if not changed:
        raise ValueError("surface-only revision must change at least one prompt")


def _validate_prior_result(prior_result: Any, *, seed: int) -> str:
    if not isinstance(prior_result, Mapping) or set(prior_result) != _LEXICAL_RESULT_KEYS:
        raise ValueError("prior result schema mismatch")
    payload = dict(prior_result)
    supplied_hash = payload.pop("result_sha256")
    if (
        not isinstance(supplied_hash, str)
        or supplied_hash != canonical_sha256(payload)
    ):
        raise ValueError("prior result hash mismatch")
    baseline_map = prior_result.get("baselines")
    normalized = (
        baseline_map.get("normalized_prose_style_bag_of_words", {})
        if isinstance(baseline_map, Mapping)
        else {}
    )
    prior_accuracy = (
        normalized.get("accuracy") if isinstance(normalized, Mapping) else None
    )
    maximum = float(GATE_THRESHOLDS["x2_normalized_style_accuracy_max"])
    if not (
        prior_result.get("schema_version") == 1
        and prior_result.get("study_id") == "SKIM-P1"
        and prior_result.get("audit") == "X2_LEXICAL_LENGTH"
        and prior_result.get("source_records_sha256")
        == PREREGISTERED_X2_SOURCE_RECORDS_SHA256
        and prior_result.get("source_status") == "PREREGISTERED_SOURCE"
        and prior_result.get("classifier_seed") == seed
        and prior_result.get("eligible_for_x2_lexical_gate") is True
        and prior_result.get("authorized_revised_source_sha256")
        == AUTHORIZED_REVISED_SOURCE_SHA256
        and prior_result.get("revision_authorization_status")
        == "FROZEN_EXACT_HASH"
        and prior_result.get("normalized_style_status")
        == "REWORK_AUTHORIZED_FROZEN_REVISION"
        and prior_result.get("surface_rework_count") == 0
        and prior_result.get("surface_rework_max") == 1
        and prior_result.get("prior_result_sha256") is None
        and type(prior_accuracy) in (int, float)
        and not isinstance(prior_accuracy, bool)
        and math.isfinite(prior_accuracy)
        and prior_accuracy > maximum
    ):
        raise ValueError("prior result is not an authorized first failure")
    preregistered_rows = _preregistered_primary_records()
    expected = run_lexical_audit(preregistered_rows, seed=seed)
    if canonical_json(dict(prior_result)) != canonical_json(expected):
        raise ValueError(
            "prior result does not match the deterministic preregistered audit"
        )
    return supplied_hash


def run_lexical_audit(
    records: Sequence[Mapping[str, Any]],
    *,
    prior_result: Optional[Mapping[str, Any]] = None,
    seed: int = PREREGISTERED_LEXICAL_CLASSIFIER_SEED,
) -> Dict[str, Any]:
    """Run the three X2 baselines and adjudicate normalized prose/style only."""

    rows = validate_primary_records(records)
    max_reworks = X2_PROBE_RULES["surface_rework_max"]
    if (
        type(seed) is not int
        or seed != PREREGISTERED_LEXICAL_CLASSIFIER_SEED
    ):
        raise ValueError("seed must equal the preregistered classifier seed")
    if AUTHORIZED_REVISED_SOURCE_SHA256 is not None and not (
        isinstance(AUTHORIZED_REVISED_SOURCE_SHA256, str)
        and len(AUTHORIZED_REVISED_SOURCE_SHA256) == 64
        and all(
            character in "0123456789abcdef"
            for character in AUTHORIZED_REVISED_SOURCE_SHA256
        )
        and AUTHORIZED_REVISED_SOURCE_SHA256
        != PREREGISTERED_X2_SOURCE_RECORDS_SHA256
    ):
        raise ValueError("authorized revised source hash is invalid")

    source_hash = source_records_sha256(rows)
    registered_source = source_hash == PREREGISTERED_X2_SOURCE_RECORDS_SHA256
    if prior_result is None:
        prior_result_sha256 = None
        surface_rework_count = 0
        eligible = registered_source
        source_status = (
            "PREREGISTERED_SOURCE"
            if registered_source
            else "UNREGISTERED_DIAGNOSTIC_ONLY"
        )
    else:
        if AUTHORIZED_REVISED_SOURCE_SHA256 is None:
            raise ValueError("no revised source hash is frozen")
        prior_result_sha256 = _validate_prior_result(prior_result, seed=seed)
        if source_hash != AUTHORIZED_REVISED_SOURCE_SHA256:
            raise ValueError("records do not match the frozen revised source hash")
        _validate_surface_only_revision(rows)
        surface_rework_count = 1
        eligible = True
        source_status = "AUTHORIZED_SURFACE_REWORK"

    splits = grouped_splits(rows, group_key="core_id", folds=5)
    labels = [str(row["magnitude_tier"]) for row in rows]
    raw = [raw_structured_text(row) for row in rows]
    normalized = [normalized_prose_style_text(row) for row in rows]
    baselines = {
        "raw_structured_bag_of_words": {
            "accuracy": _evaluate_text_baseline(
                raw, labels, splits, seed=seed
            ),
            "input": "exact_public_structured_request",
            "decision_role": "DIAGNOSTIC_ONLY",
            "interpretation": (
                "STRUCTURED_MAGNITUDE_MANIPULATION_SANITY_CHECK"
            ),
        },
        "normalized_prose_style_bag_of_words": {
            "accuracy": _evaluate_text_baseline(
                normalized, labels, splits, seed=seed
            ),
            "input": "number_normalized_public_string_leaves",
            "decision_role": "REGISTERED_GATE",
            "interpretation": "SURFACE_LEAKAGE_REGISTERED_GATE",
        },
        "length_only": {
            "accuracy": _evaluate_length_baseline(
                normalized, labels, splits, seed=seed
            ),
            "input": "number_normalized_prose_style_length",
            "decision_role": "DIAGNOSTIC_ONLY",
            "interpretation": "PROSE_STYLE_LENGTH_DIAGNOSTIC",
        },
    }
    maximum = float(GATE_THRESHOLDS["x2_normalized_style_accuracy_max"])
    chance = float(GATE_THRESHOLDS["x2_lexical_chance_accuracy"])
    passed = (
        baselines["normalized_prose_style_bag_of_words"]["accuracy"]
        <= maximum
    )
    if not eligible:
        status = (
            "NOT_ELIGIBLE_UNREGISTERED_SOURCE"
            if passed
            else "PARK_UNREGISTERED_SOURCE"
        )
    elif passed:
        status = "PASS"
    elif surface_rework_count == 0:
        status = (
            "REWORK_PENDING_FROZEN_REVISION"
            if AUTHORIZED_REVISED_SOURCE_SHA256 is None
            else "REWORK_AUTHORIZED_FROZEN_REVISION"
        )
    else:
        status = X2_PROBE_RULES["second_failure"]

    if not eligible:
        revision_authorization_status = "INELIGIBLE_UNREGISTERED_SOURCE"
    elif surface_rework_count == 1:
        revision_authorization_status = "FROZEN_EXACT_HASH_VERIFIED"
    elif passed:
        revision_authorization_status = "NOT_NEEDED_BANK_PASSES"
    elif AUTHORIZED_REVISED_SOURCE_SHA256 is None:
        revision_authorization_status = "PENDING_SEPARATE_FREEZE"
    else:
        revision_authorization_status = "FROZEN_EXACT_HASH"

    result = {
        "schema_version": 1,
        "study_id": "SKIM-P1",
        "audit": "X2_LEXICAL_LENGTH",
        "data_basis": (
            "public_bank_construction_audit"
            if eligible
            else "unregistered_construction_diagnostic"
        ),
        "synthetic": False if eligible else None,
        "eligible_for_empirical_decision": False,
        "eligible_for_x2_lexical_gate": eligible,
        "source_records_sha256": source_hash,
        "source_status": source_status,
        "authorized_revised_source_sha256": AUTHORIZED_REVISED_SOURCE_SHA256,
        "revision_authorization_status": revision_authorization_status,
        "target": "magnitude_tier",
        "target_classes": list(MAGNITUDE_TIERS),
        "split_unit": X2_PROBE_RULES["split_unit"],
        "group_key": "core_id",
        "folds": len(splits),
        "fold_test_core_ids": [split["test_groups"] for split in splits],
        "n_records": len(rows),
        "n_cores": len({row["core_id"] for row in rows}),
        "classifier_seed": seed,
        "chance_accuracy": chance,
        "normalized_style_max_accuracy": maximum,
        "baselines": baselines,
        "normalized_style_status": status,
        "surface_rework_count": surface_rework_count,
        "surface_rework_max": max_reworks,
        "second_failure_action": X2_PROBE_RULES["second_failure"],
        "prior_result_sha256": prior_result_sha256,
    }
    result["result_sha256"] = canonical_sha256(result)
    if set(result) != _LEXICAL_RESULT_KEYS:
        raise AssertionError("lexical result schema drift")
    return result


__all__ = [
    "AUTHORIZED_REVISED_SOURCE_SHA256",
    "PREREGISTERED_LEXICAL_CLASSIFIER_SEED",
    "PREREGISTERED_X2_SOURCE_RECORDS_SHA256",
    "grouped_splits",
    "normalize_numbers",
    "normalized_prose_style_text",
    "raw_structured_text",
    "run_lexical_audit",
    "source_records_sha256",
    "validate_primary_records",
]
