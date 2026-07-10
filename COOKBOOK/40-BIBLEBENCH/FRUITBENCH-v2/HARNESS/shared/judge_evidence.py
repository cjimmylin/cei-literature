"""Recompute judge-validation metrics from raw human and judge calibration rows."""

from __future__ import annotations

import hashlib
import json
import math
import re
from collections import defaultdict
from collections.abc import Collection, Mapping, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from types import MappingProxyType
from typing import Any


_ATTESTATION = object()
_SHA256_RE = re.compile(r"[0-9a-f]{64}\Z")


@dataclass(frozen=True)
class ComputedJudgeEvidence:
    human_human: Mapping[str, Any]
    judges: tuple[Mapping[str, Any], ...]
    evidence_sha256: str
    _attestation: object = field(default=None, repr=False, compare=False)

    def __post_init__(self) -> None:
        if self._attestation is not _ATTESTATION:
            raise TypeError(
                "ComputedJudgeEvidence can be created only by compute_judge_evidence"
            )


def _thaw(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _thaw(child) for key, child in value.items()}
    if isinstance(value, (list, tuple)):
        return [_thaw(child) for child in value]
    return value


def _freeze(value: Any) -> Any:
    if isinstance(value, Mapping):
        return MappingProxyType({str(key): _freeze(child) for key, child in value.items()})
    if isinstance(value, list):
        return tuple(_freeze(child) for child in value)
    return value


def _canonical(value: Any) -> bytes:
    try:
        return json.dumps(
            _thaw(value),
            allow_nan=False,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise ValueError("judge evidence must contain strict JSON values") from exc


def _source(source: Any, name: str) -> tuple[dict[str, Any], bytes]:
    if isinstance(source, Path):
        raw = source.read_bytes()
    elif isinstance(source, Mapping):
        raw = _canonical(source)
    elif isinstance(source, (bytes, bytearray)):
        raw = bytes(source)
    elif isinstance(source, str):
        raw = source.encode("utf-8") if source.lstrip().startswith("{") else Path(source).read_bytes()
    else:
        raise ValueError(f"{name} must be a mapping, JSON, or a path")
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{name} must be valid UTF-8 JSON") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{name} must be a JSON object")
    return value, raw


def _exact_text(value: Any, field_name: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{field_name} must be an exact non-blank string")
    return value


def _hash(value: Any, field_name: str) -> str:
    if not isinstance(value, str) or _SHA256_RE.fullmatch(value) is None:
        raise ValueError(f"{field_name} must be a lowercase SHA-256")
    return value


def _closed_classes(value: Collection[str]) -> tuple[str, ...]:
    if isinstance(value, (str, bytes, bytearray)) or not isinstance(value, Collection):
        raise ValueError("expected_class_labels must be a collection")
    labels = tuple(sorted(value))
    if len(labels) < 2 or any(not isinstance(label, str) or not label for label in labels):
        raise ValueError("expected_class_labels must contain at least two exact labels")
    if len(labels) != len(set(labels)):
        raise ValueError("expected_class_labels must be unique")
    return labels


def _human_records(
    human: Mapping[str, Any], classes: tuple[str, ...]
) -> tuple[dict[str, str], dict[str, tuple[str, str]], dict[str, float]]:
    required = {"schema_version", "source_sha256", "rows", "resolved_labels", "coverage"}
    if set(human) != required or human.get("schema_version") != "1.0":
        raise ValueError("human intake has an unexpected schema")
    _hash(human["source_sha256"], "human source_sha256")
    rows = human["rows"]
    resolved_raw = human["resolved_labels"]
    if not isinstance(rows, list) or not isinstance(resolved_raw, dict) or not resolved_raw:
        raise ValueError("human intake rows/resolved_labels are missing")
    resolved = {
        _exact_text(response_id, "human response_id"): _exact_text(label, "human label")
        for response_id, label in resolved_raw.items()
    }
    if any(label not in classes for label in resolved.values()):
        raise ValueError("human resolved label is outside expected classes")
    if set(resolved.values()) != set(classes):
        raise ValueError("human class coverage must include every expected class")

    grouped: dict[str, dict[str, list[tuple[str, str]]]] = defaultdict(
        lambda: {"primary": [], "adjudicator": []}
    )
    for index, row in enumerate(rows):
        if not isinstance(row, dict) or set(row) != {
            "response_id", "rater_hash", "role", "final_label", "notes"
        }:
            raise ValueError(f"human row {index} has an unexpected schema")
        response_id = _exact_text(row["response_id"], "human response_id")
        rater_hash = _hash(row["rater_hash"], "human rater_hash")
        role = row["role"]
        if role not in {"primary", "adjudicator"}:
            raise ValueError("human role must be primary or adjudicator")
        label = _exact_text(row["final_label"], "human final_label")
        if label not in classes:
            raise ValueError("human final_label is outside expected classes")
        if not isinstance(row["notes"], str):
            raise ValueError("human notes must be text")
        grouped[response_id][role].append((rater_hash, label))
    if set(grouped) != set(resolved):
        raise ValueError("human response coverage does not equal resolved_labels")

    primary_pairs: dict[str, tuple[str, str]] = {}
    agreement_by_response: dict[str, float] = {}
    for response_id, final_label in resolved.items():
        primary = grouped[response_id]["primary"]
        adjudicators = grouped[response_id]["adjudicator"]
        if len(primary) != 2 or len({rater for rater, _label in primary}) != 2:
            raise ValueError(f"response {response_id} must have exactly two primary raters")
        labels = (primary[0][1], primary[1][1])
        primary_pairs[response_id] = labels
        agreement_by_response[response_id] = float(labels[0] == labels[1])
        if labels[0] == labels[1]:
            if final_label != labels[0] or adjudicators:
                raise ValueError(f"response {response_id} has invalid agreement resolution")
        else:
            if len(adjudicators) != 1 or adjudicators[0][0] in {row[0] for row in primary}:
                raise ValueError(f"response {response_id} lacks independent adjudication")
            if final_label != adjudicators[0][1]:
                raise ValueError(f"response {response_id} resolved label disagrees with adjudication")
    return resolved, primary_pairs, agreement_by_response


def _weighted_kappa(
    pairs: Mapping[str, tuple[str, str]], classes: tuple[str, ...]
) -> float:
    index = {label: position for position, label in enumerate(classes)}
    size = max(1, len(classes) - 1)
    n = len(pairs)
    observed = sum(
        ((index[left] - index[right]) / size) ** 2 for left, right in pairs.values()
    ) / n
    left_counts = {label: 0 for label in classes}
    right_counts = {label: 0 for label in classes}
    for left, right in pairs.values():
        left_counts[left] += 1
        right_counts[right] += 1
    expected = sum(
        (left_counts[left] / n)
        * (right_counts[right] / n)
        * (((index[left] - index[right]) / size) ** 2)
        for left in classes
        for right in classes
    )
    if expected == 0:
        return 1.0 if observed == 0 else 0.0
    return 1.0 - observed / expected


def _f1(gold: Sequence[str], predicted: Sequence[str], label: str) -> float:
    tp = sum(g == label and p == label for g, p in zip(gold, predicted))
    fp = sum(g != label and p == label for g, p in zip(gold, predicted))
    fn = sum(g == label and p != label for g, p in zip(gold, predicted))
    denominator = 2 * tp + fp + fn
    return 2 * tp / denominator if denominator else 0.0


def _average_precision(gold: Sequence[str], scores: Sequence[float], label: str) -> float:
    positives = sum(value == label for value in gold)
    if positives == 0:
        raise ValueError(f"AUPRC cannot be computed without class {label!r}")
    order = sorted(range(len(scores)), key=lambda index: (-scores[index], index))
    true_so_far = 0
    precision_sum = 0.0
    for rank, index in enumerate(order, start=1):
        if gold[index] == label:
            true_so_far += 1
            precision_sum += true_so_far / rank
    return precision_sum / positives


def compute_judge_evidence(
    human_source: Any,
    prediction_source: Any,
    *,
    expected_judge_identities: Mapping[str, Mapping[str, str]],
    expected_class_labels: Collection[str],
    expected_label_set_sha256: str,
    expected_prompt_hashes: Mapping[str, str],
) -> ComputedJudgeEvidence:
    """Validate complete raw rows and recompute every human/judge metric."""
    classes = _closed_classes(expected_class_labels)
    label_hash = _hash(expected_label_set_sha256, "expected_label_set_sha256")
    prompts = dict(expected_prompt_hashes)
    if set(prompts) != {"layer_e", "layer_r"}:
        raise ValueError("expected_prompt_hashes must contain layer_e and layer_r")
    for name, value in prompts.items():
        _hash(value, f"expected_prompt_hashes.{name}")
    identities = {judge_id: dict(identity) for judge_id, identity in expected_judge_identities.items()}
    if len(identities) < 2:
        raise ValueError("at least two expected judge identities are required")

    human, human_raw = _source(human_source, "human intake")
    resolved, primary_pairs, agreement_by_response = _human_records(human, classes)
    predictions, prediction_raw = _source(prediction_source, "judge predictions")
    if set(predictions) != {"schema_version", "label_set_sha256", "prompt_hashes", "rows"}:
        raise ValueError("judge predictions have an unexpected schema")
    if predictions["schema_version"] != "1.0":
        raise ValueError("judge prediction schema_version must be 1.0")
    if predictions["label_set_sha256"] != label_hash or predictions["prompt_hashes"] != prompts:
        raise ValueError("judge predictions are not bound to current labels/prompts")
    rows = predictions["rows"]
    if not isinstance(rows, list):
        raise ValueError("judge prediction rows must be a list")
    required_row = {
        "response_id", "judge_id", "judge_model_id", "judge_snapshot",
        "judge_vendor", "judge_family", "final_label", "class_probabilities",
        "judge_refused",
    }
    by_pair: dict[tuple[str, str], dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict) or set(row) != required_row:
            raise ValueError(f"judge prediction row {index} has an unexpected schema")
        response_id = _exact_text(row["response_id"], "prediction response_id")
        judge_id = _exact_text(row["judge_id"], "prediction judge_id")
        if response_id not in resolved or judge_id not in identities:
            raise ValueError("judge prediction coverage contains an unknown response/judge")
        actual_identity = {
            "model_id": row["judge_model_id"],
            "canonical_snapshot": row["judge_snapshot"],
            "vendor": row["judge_vendor"],
            "family": row["judge_family"],
        }
        if actual_identity != identities[judge_id]:
            raise ValueError(f"judge prediction {judge_id} identity does not match")
        label = row["final_label"]
        if label not in classes:
            raise ValueError("judge final_label is outside expected classes")
        probabilities = row["class_probabilities"]
        if not isinstance(probabilities, dict) or set(probabilities) != set(classes):
            raise ValueError("class_probabilities must cover every expected class")
        numeric: dict[str, float] = {}
        for class_label, value in probabilities.items():
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError("class probabilities must be numeric")
            number = float(value)
            if not math.isfinite(number) or not 0 <= number <= 1:
                raise ValueError("class probabilities must be in [0,1]")
            numeric[class_label] = number
        if abs(sum(numeric.values()) - 1.0) > 1e-6:
            raise ValueError("class probabilities must sum to 1")
        if numeric[label] < max(numeric.values()) - 1e-12:
            raise ValueError("judge final_label must have maximum probability")
        if not isinstance(row["judge_refused"], bool):
            raise ValueError("judge_refused must be boolean")
        pair = (response_id, judge_id)
        if pair in by_pair:
            raise ValueError("judge prediction rows contain a duplicate response/judge pair")
        by_pair[pair] = row
    expected_pairs = {
        (response_id, judge_id) for response_id in resolved for judge_id in identities
    }
    if set(by_pair) != expected_pairs:
        raise ValueError("judge prediction coverage is incomplete")

    human_metrics = {
        "metrics": {
            "agreement": sum(agreement_by_response.values()) / len(resolved),
            "weighted_kappa": _weighted_kappa(primary_pairs, classes),
        },
        "by_class": {
            label: {
                "metrics": {
                    "agreement": sum(
                        agreement_by_response[response_id]
                        for response_id, gold in resolved.items()
                        if gold == label
                    )
                    / sum(gold == label for gold in resolved.values())
                }
            }
            for label in classes
        },
    }

    response_order = sorted(resolved)
    gold = [resolved[response_id] for response_id in response_order]
    judge_metrics: list[dict[str, Any]] = []
    for judge_id in sorted(identities):
        judge_rows = [by_pair[(response_id, judge_id)] for response_id in response_order]
        predicted = [row["final_label"] for row in judge_rows]
        by_class = {}
        for label in classes:
            by_class[label] = {
                "metrics": {
                    "f1": _f1(gold, predicted, label),
                    "auprc": _average_precision(
                        gold,
                        [float(row["class_probabilities"][label]) for row in judge_rows],
                        label,
                    ),
                }
            }
        f1_values = [by_class[label]["metrics"]["f1"] for label in classes]
        auprc_values = [by_class[label]["metrics"]["auprc"] for label in classes]
        judge_metrics.append(
            {
                "judge_id": judge_id,
                "metrics": {
                    "macro_f1": sum(f1_values) / len(f1_values),
                    "auprc": sum(auprc_values) / len(auprc_values),
                    "worst_class_f1": min(f1_values),
                    "agreement": sum(g == p for g, p in zip(gold, predicted)) / len(gold),
                },
                "by_class": by_class,
                "calibration_n": len(gold),
                "refusal_rate": sum(bool(row["judge_refused"]) for row in judge_rows)
                / len(judge_rows),
            }
        )

    digest = hashlib.sha256(
        _canonical(
            {
                "human_intake": human,
                "judge_predictions": predictions,
                "expected_judge_identities": identities,
                "expected_class_labels": list(classes),
                "expected_label_set_sha256": label_hash,
                "expected_prompt_hashes": prompts,
                "source_hashes": {
                    "human_input": hashlib.sha256(human_raw).hexdigest(),
                    "judge_predictions": hashlib.sha256(prediction_raw).hexdigest(),
                },
            }
        )
    ).hexdigest()
    return ComputedJudgeEvidence(
        human_human=_freeze(human_metrics),
        judges=tuple(_freeze(judge) for judge in judge_metrics),
        evidence_sha256=digest,
        _attestation=_ATTESTATION,
    )


__all__ = ["ComputedJudgeEvidence", "compute_judge_evidence"]
