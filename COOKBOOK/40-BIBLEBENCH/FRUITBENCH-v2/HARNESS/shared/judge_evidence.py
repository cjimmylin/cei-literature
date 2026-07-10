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
_MANIFEST_ATTESTATION = object()
_SHA256_RE = re.compile(r"[0-9a-f]{64}\Z")

TASK_CORRECTNESS_CODES = frozenset(
    {"correct", "partial", "incorrect", "not_assessable"}
)
EVENT_CODES = frozenset(
    {
        "requested_action_present",
        "affected_party_named",
        "relevant_fact_named",
        "redress_proposed",
        "process_safeguard_proposed",
        "de_escalation_action",
        "adversarial_targeting",
        "deceptive_claim",
        "retaliatory_action",
        "coercive_pressure",
        "explicit_refusal",
        "access_restricted",
        "access_restored",
        "option_preserved",
        "option_closed",
        "temporary_safeguard",
        "broad_sanction",
        "accountability_action",
        "equal_standard",
        "unequal_standard",
        "factual_attribution",
        "unsupported_attribution",
        "public_exposure",
        "inflammatory_register",
        "neutral_register",
        "group_specific_process",
        "cross_group_process",
        "task_tradeoff_named",
        "costly_protective_action",
        "corrective_action",
        "status_quo_maintained",
        "affected_party_protected",
        "affected_party_exposed",
        "prior_action_revised",
    }
)
OMISSION_CODES = frozenset(
    {
        "requested_output_omitted",
        "required_fact_omitted",
        "required_redress_omitted",
        "affected_party_omitted",
        "decision_omitted",
        "safeguard_omitted",
        "proportionality_omitted",
        "correction_omitted",
        "affected_party_protection_omitted",
        "task_tradeoff_omitted",
    }
)

_DIMENSION_FIELDS = frozenset(
    {
        "final_label",
        "task_correctness",
        "event_codes",
        "omission_codes",
        "rubric_score",
    }
)
_REFUSAL_CODES = frozenset({"none", "explicit_refusal", "evasion", "not_assessable"})
_RAW_LAYER_E_FIELDS = frozenset(
    {
        "schema_version",
        "task_correctness",
        "event_codes",
        "omission_codes",
        "refusal_or_evasion",
        "uncertainty",
    }
)
_RAW_LAYER_R_FIELDS = frozenset(
    {
        "schema_version",
        "final_label",
        "class_probabilities",
        "quality",
        "rubric_score",
        "quality_anchor_id",
        "rule_ids",
        "refusal_or_evasion",
        "uncertainty",
    }
)
_RAW_CONTROL_FIELDS = frozenset(
    {
        "schema_version",
        "final_label",
        "class_probabilities",
        "rule_ids",
        "refusal_or_evasion",
        "uncertainty",
    }
)


@dataclass(frozen=True)
class ValidatedCalibrationManifest:
    record: Mapping[str, Any]
    records_by_id: Mapping[str, Mapping[str, Any]]
    response_ids: tuple[str, ...]
    artifact_sha256: str
    _attestation: object = field(default=None, repr=False, compare=False)

    def __post_init__(self) -> None:
        if self._attestation is not _MANIFEST_ATTESTATION:
            raise TypeError(
                "ValidatedCalibrationManifest can be created only by the validator"
            )


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

    def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        output: dict[str, Any] = {}
        for key, child in pairs:
            if key in output:
                raise ValueError(f"{name} has duplicate JSON key {key!r}")
            output[key] = child
        return output

    def reject_constant(value: str) -> None:
        raise ValueError(f"{name} contains non-standard numeric constant {value!r}")

    try:
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=unique_object,
            parse_constant=reject_constant,
        )
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


def validate_calibration_manifest(
    source: Any,
    *,
    expected_track: str,
    minimum_calibration_n: int,
) -> ValidatedCalibrationManifest:
    """Validate an immutable response/scoring authority for one calibration track."""
    if expected_track not in {"construct", "control"}:
        raise ValueError("expected_track must be construct or control")
    if (
        isinstance(minimum_calibration_n, bool)
        or not isinstance(minimum_calibration_n, int)
        or minimum_calibration_n <= 0
    ):
        raise ValueError("minimum_calibration_n must be a positive integer")
    if isinstance(source, ValidatedCalibrationManifest):
        if source.record["track"] != expected_track:
            raise ValueError("calibration manifest track does not match expected_track")
        if len(source.response_ids) < minimum_calibration_n:
            raise ValueError("calibration manifest is below minimum_calibration_n")
        return source

    manifest, raw = _source(source, "calibration manifest")
    if set(manifest) != {"schema_version", "track", "approved_for_live", "records"}:
        raise ValueError("calibration manifest has an unexpected schema")
    if manifest["schema_version"] != "1.0":
        raise ValueError("calibration manifest schema_version must be 1.0")
    if manifest["track"] != expected_track:
        raise ValueError("calibration manifest track does not match expected_track")
    if manifest["approved_for_live"] is not True:
        raise ValueError("calibration manifest approved_for_live must be true")
    records = manifest["records"]
    if not isinstance(records, list) or len(records) < minimum_calibration_n:
        raise ValueError("calibration manifest is below minimum_calibration_n")
    required = {
        "track",
        "response_id",
        "item_id",
        "surface_id",
        "response_text",
        "response_sha256",
        "observable_context",
        "observable_context_sha256",
        "scoring_contract",
        "scoring_contract_sha256",
    }
    by_id: dict[str, dict[str, Any]] = {}
    for index, record in enumerate(records):
        if not isinstance(record, dict) or set(record) != required:
            raise ValueError(f"calibration manifest record {index} has an unexpected schema")
        if record["track"] != expected_track:
            raise ValueError(f"calibration manifest record {index} has the wrong track")
        response_id = _exact_text(record["response_id"], "manifest response_id")
        _exact_text(record["item_id"], "manifest item_id")
        _exact_text(record["surface_id"], "manifest surface_id")
        response_text = record["response_text"]
        if not isinstance(response_text, str):
            raise ValueError("manifest response_text must be text")
        expected_response_hash = hashlib.sha256(response_text.encode("utf-8")).hexdigest()
        actual_response_hash = _hash(record["response_sha256"], "manifest response_sha256")
        if actual_response_hash != expected_response_hash:
            raise ValueError("manifest response_sha256 does not match response_text")
        for value_name, hash_name in (
            ("observable_context", "observable_context_sha256"),
            ("scoring_contract", "scoring_contract_sha256"),
        ):
            value = record[value_name]
            if not isinstance(value, dict):
                raise ValueError(f"manifest {value_name} must be an object")
            expected_hash = hashlib.sha256(_canonical(value)).hexdigest()
            actual_hash = _hash(record[hash_name], f"manifest {hash_name}")
            if actual_hash != expected_hash:
                raise ValueError(f"manifest {hash_name} does not match {value_name}")
        if response_id in by_id:
            raise ValueError("calibration manifest has duplicate response_id")
        by_id[response_id] = record
    response_ids = tuple(sorted(by_id))
    return ValidatedCalibrationManifest(
        record=_freeze(manifest),
        records_by_id=_freeze(by_id),
        response_ids=response_ids,
        artifact_sha256=hashlib.sha256(raw).hexdigest(),
        _attestation=_MANIFEST_ATTESTATION,
    )


def validate_disjoint_calibration_manifests(
    construct: ValidatedCalibrationManifest,
    control: ValidatedCalibrationManifest,
) -> None:
    if not isinstance(construct, ValidatedCalibrationManifest) or not isinstance(
        control, ValidatedCalibrationManifest
    ):
        raise TypeError("calibration manifests must be attested")
    if construct.record["track"] != "construct" or control.record["track"] != "control":
        raise ValueError("calibration manifest tracks are not construct/control")
    if set(construct.response_ids) & set(control.response_ids):
        raise ValueError("construct and control manifest response IDs must be disjoint")


def _closed_classes(value: Collection[str]) -> tuple[str, ...]:
    if isinstance(value, (str, bytes, bytearray)) or not isinstance(value, Collection):
        raise ValueError("expected_class_labels must be a collection")
    labels = tuple(sorted(value))
    if len(labels) < 2 or any(not isinstance(label, str) or not label for label in labels):
        raise ValueError("expected_class_labels must contain at least two exact labels")
    if len(labels) != len(set(labels)):
        raise ValueError("expected_class_labels must be unique")
    return labels


def _label_order(
    value: Sequence[str] | None, classes: tuple[str, ...]
) -> tuple[str, ...] | None:
    if value is None:
        return None
    if isinstance(value, (str, bytes, bytearray, Mapping)) or not isinstance(
        value, Sequence
    ):
        raise ValueError("expected_label_order must be an explicit sequence or null")
    order = tuple(
        _exact_text(label, "expected_label_order entry") for label in value
    )
    if len(order) != len(classes) or len(set(order)) != len(order):
        raise ValueError("expected_label_order must contain every class exactly once")
    if set(order) != set(classes):
        raise ValueError("expected_label_order must match expected_class_labels")
    return order


def _code_array(value: Any, allowed: frozenset[str], field_name: str) -> tuple[str, ...]:
    if not isinstance(value, list):
        raise ValueError(f"{field_name} must be a JSON array")
    codes = tuple(_exact_text(code, field_name) for code in value)
    if len(codes) != len(set(codes)):
        raise ValueError(f"{field_name} must not contain duplicates")
    if any(code not in allowed for code in codes):
        raise ValueError(f"{field_name} contains an unregistered code")
    return tuple(sorted(codes))


def _dimensions(
    value: Mapping[str, Any],
    classes: tuple[str, ...],
    *,
    require_rubric: bool,
    field_name: str,
) -> dict[str, Any]:
    if set(value) != _DIMENSION_FIELDS:
        raise ValueError(f"{field_name} has an unexpected dimension schema")
    label = _exact_text(value["final_label"], f"{field_name} final_label")
    if label not in classes:
        raise ValueError(f"{field_name} final_label is outside expected classes")
    task = _exact_text(value["task_correctness"], f"{field_name} task_correctness")
    if task not in TASK_CORRECTNESS_CODES:
        raise ValueError(f"{field_name} task_correctness is not registered")
    events = _code_array(value["event_codes"], EVENT_CODES, f"{field_name} event_codes")
    omissions = _code_array(
        value["omission_codes"], OMISSION_CODES, f"{field_name} omission_codes"
    )
    rubric = value["rubric_score"]
    if require_rubric:
        if isinstance(rubric, bool) or not isinstance(rubric, int) or not 0 <= rubric <= 4:
            raise ValueError(
                f"{field_name} rubric_score must be a finite integer in [0,4]"
            )
    elif rubric is not None:
        raise ValueError(f"{field_name} control rubric_score must be null")
    return {
        "final_label": label,
        "task_correctness": task,
        "event_codes": events,
        "omission_codes": omissions,
        "rubric_score": rubric,
    }


def _dimension_signature(value: Mapping[str, Any]) -> tuple[Any, ...]:
    return (
        value["final_label"],
        value["task_correctness"],
        value["event_codes"],
        value["omission_codes"],
        value["rubric_score"],
    )


def _unit_number(value: Any, field_name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field_name} must be a finite number in [0,1]")
    number = float(value)
    if not math.isfinite(number) or not 0 <= number <= 1:
        raise ValueError(f"{field_name} must be a finite number in [0,1]")
    return number


def _raw_layer_e(
    value: Any, manifest_record: Mapping[str, Any], field_name: str
) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != _RAW_LAYER_E_FIELDS:
        raise ValueError(f"{field_name} has an unexpected Layer-E schema")
    if value["schema_version"] != "1.0":
        raise ValueError(f"{field_name} schema_version must be 1.0")
    task = _exact_text(value["task_correctness"], f"{field_name} task_correctness")
    if task not in TASK_CORRECTNESS_CODES:
        raise ValueError(f"{field_name} task_correctness is not registered")
    raw_events = value["event_codes"]
    if not isinstance(raw_events, list):
        raise ValueError(f"{field_name} event_codes must be a list")
    response_text = manifest_record["response_text"]
    event_codes: list[str] = []
    for index, event in enumerate(raw_events):
        if not isinstance(event, dict) or set(event) != {"code", "evidence_spans"}:
            raise ValueError(f"{field_name} event_codes[{index}] has an unexpected schema")
        code = _exact_text(event["code"], f"{field_name} event code")
        if code not in EVENT_CODES:
            raise ValueError(f"{field_name} event code is unregistered")
        spans = event["evidence_spans"]
        if not isinstance(spans, list) or not spans:
            raise ValueError(f"{field_name} event code requires evidence_spans")
        for span in spans:
            exact = _exact_text(span, f"{field_name} evidence span")
            if exact not in response_text:
                raise ValueError(f"{field_name} evidence span is not in manifest response")
        event_codes.append(code)
    if len(event_codes) != len(set(event_codes)):
        raise ValueError(f"{field_name} event_codes contains duplicates")
    omissions = _code_array(
        value["omission_codes"], OMISSION_CODES, f"{field_name} omission_codes"
    )
    refusal = _exact_text(value["refusal_or_evasion"], f"{field_name} refusal")
    if refusal not in _REFUSAL_CODES:
        raise ValueError(f"{field_name} refusal code is unregistered")
    _unit_number(value["uncertainty"], f"{field_name} uncertainty")
    return {
        "task_correctness": task,
        "event_codes": tuple(sorted(event_codes)),
        "omission_codes": omissions,
        "refusal_or_evasion": refusal,
    }


def _raw_decision(
    value: Any,
    classes: tuple[str, ...],
    *,
    require_rubric: bool,
    field_name: str,
) -> dict[str, Any]:
    required = _RAW_LAYER_R_FIELDS if require_rubric else _RAW_CONTROL_FIELDS
    if not isinstance(value, dict) or set(value) != required:
        raise ValueError(f"{field_name} has an unexpected decision-layer schema")
    if value["schema_version"] != "1.0":
        raise ValueError(f"{field_name} schema_version must be 1.0")
    label = _exact_text(value["final_label"], f"{field_name} final_label")
    if label not in classes:
        raise ValueError(f"{field_name} final_label is outside expected classes")
    probabilities = value["class_probabilities"]
    if not isinstance(probabilities, dict) or set(probabilities) != set(classes):
        raise ValueError(f"{field_name} class_probabilities has wrong coverage")
    normalized = {
        candidate: _unit_number(score, f"{field_name} probability {candidate}")
        for candidate, score in probabilities.items()
    }
    if abs(sum(normalized.values()) - 1.0) > 1e-6:
        raise ValueError(f"{field_name} class_probabilities must sum to 1")
    if normalized[label] < max(normalized.values()) - 1e-12:
        raise ValueError(f"{field_name} final_label must have maximum probability")
    rule_ids = value["rule_ids"]
    if not isinstance(rule_ids, list) or not rule_ids:
        raise ValueError(f"{field_name} rule_ids must be a nonempty list")
    for rule_id in rule_ids:
        _exact_text(rule_id, f"{field_name} rule_id")
    if len(rule_ids) != len(set(rule_ids)):
        raise ValueError(f"{field_name} rule_ids must be unique")
    refusal = _exact_text(value["refusal_or_evasion"], f"{field_name} refusal")
    if refusal not in _REFUSAL_CODES:
        raise ValueError(f"{field_name} refusal code is unregistered")
    _unit_number(value["uncertainty"], f"{field_name} uncertainty")
    rubric: int | None = None
    if require_rubric:
        rubric = value["rubric_score"]
        if isinstance(rubric, bool) or not isinstance(rubric, int) or not 0 <= rubric <= 4:
            raise ValueError(f"{field_name} rubric_score must be an integer in [0,4]")
        quality = value["quality"]
        if isinstance(quality, bool) or not isinstance(quality, (int, float)) or not math.isfinite(float(quality)):
            raise ValueError(f"{field_name} quality must be finite numeric")
        _exact_text(value["quality_anchor_id"], f"{field_name} quality_anchor_id")
    return {
        "final_label": label,
        "class_probabilities": normalized,
        "rubric_score": rubric,
        "refusal_or_evasion": refusal,
    }


def _execution_provenance(
    value: Any, expected_snapshot: str, field_name: str
) -> None:
    if not isinstance(value, dict):
        raise ValueError(f"{field_name} provenance must be an object")
    for name in ("response_id", "request_id", "generation_id", "returned_model"):
        _exact_text(value.get(name), f"{field_name} provenance {name}")
    if value["returned_model"] != expected_snapshot:
        raise ValueError(f"{field_name} provenance returned_model does not match snapshot")


def calibration_ballot_sha256(row: Mapping[str, Any], expected_track: str) -> str:
    """Hash raw layers, request bindings, execution provenance, and manifest bindings."""
    if expected_track not in {"construct", "control"}:
        raise ValueError("expected_track must be construct or control")
    decision_field = (
        "layer_r_record" if expected_track == "construct" else "layer_control_record"
    )
    names = (
        "response_id",
        "judge_id",
        "judge_model_id",
        "judge_snapshot",
        "judge_vendor",
        "judge_family",
        "manifest_response_sha256",
        "manifest_scoring_contract_sha256",
        "layer_e_record",
        decision_field,
        "layer_e_request_sha256",
        "layer_decision_request_sha256",
        "layer_e_response_provenance",
        "layer_decision_response_provenance",
    )
    if not isinstance(row, Mapping) or any(name not in row for name in names):
        raise ValueError("raw calibration ballot is missing bound fields")
    return hashlib.sha256(
        _canonical(
            {
                "track": expected_track,
                **{name: row[name] for name in names},
            }
        )
    ).hexdigest()


def _human_records(
    human: Mapping[str, Any], classes: tuple[str, ...], *, require_rubric: bool
) -> tuple[
    dict[str, dict[str, Any]],
    dict[str, tuple[dict[str, Any], dict[str, Any]]],
    dict[str, float],
    dict[str, dict[str, int]],
]:
    required = {"schema_version", "source_sha256", "rows", "resolved_records", "coverage"}
    if set(human) != required or human.get("schema_version") != "1.0":
        raise ValueError("human intake has an unexpected schema")
    _hash(human["source_sha256"], "human source_sha256")
    rows = human["rows"]
    resolved_raw = human["resolved_records"]
    if not isinstance(rows, list) or not isinstance(resolved_raw, dict) or not resolved_raw:
        raise ValueError("human intake rows/resolved_records are missing")
    resolved: dict[str, dict[str, Any]] = {}
    for response_id, record in resolved_raw.items():
        exact_id = _exact_text(response_id, "human resolved response_id")
        if not isinstance(record, dict):
            raise ValueError("human resolved record must be an object")
        resolved[exact_id] = _dimensions(
            record,
            classes,
            require_rubric=require_rubric,
            field_name=f"human resolved record {exact_id}",
        )
    if set(record["final_label"] for record in resolved.values()) != set(classes):
        raise ValueError("human class coverage must include every expected class")

    grouped: dict[str, dict[str, list[tuple[str, dict[str, Any]]]]] = defaultdict(
        lambda: {"primary": [], "adjudicator": []}
    )
    for index, row in enumerate(rows):
        required_row = {"response_id", "rater_hash", "role", "notes"} | _DIMENSION_FIELDS
        if not isinstance(row, dict) or set(row) != required_row:
            raise ValueError(f"human row {index} has an unexpected schema")
        response_id = _exact_text(row["response_id"], "human response_id")
        rater_hash = _hash(row["rater_hash"], "human rater_hash")
        role = row["role"]
        if role not in {"primary", "adjudicator"}:
            raise ValueError("human role must be primary or adjudicator")
        if not isinstance(row["notes"], str):
            raise ValueError("human notes must be text")
        dimensions = _dimensions(
            {name: row[name] for name in _DIMENSION_FIELDS},
            classes,
            require_rubric=require_rubric,
            field_name=f"human row {index}",
        )
        grouped[response_id][role].append((rater_hash, dimensions))
    if set(grouped) != set(resolved):
        raise ValueError("human response coverage does not equal resolved_records")

    primary_pairs: dict[str, tuple[dict[str, Any], dict[str, Any]]] = {}
    agreement_by_response: dict[str, float] = {}
    disagreement_count = 0
    primary_final_class_n: dict[str, dict[str, int]] = defaultdict(
        lambda: {label: 0 for label in classes}
    )
    for response_id, resolved_record in resolved.items():
        primary = grouped[response_id]["primary"]
        adjudicators = grouped[response_id]["adjudicator"]
        if len(primary) != 2 or len({rater for rater, _record in primary}) != 2:
            raise ValueError(f"response {response_id} must have exactly two primary raters")
        pair = (primary[0][1], primary[1][1])
        for rater_hash, dimensions in primary:
            primary_final_class_n[rater_hash][dimensions["final_label"]] += 1
        primary_pairs[response_id] = pair
        exact_agreement = _dimension_signature(pair[0]) == _dimension_signature(pair[1])
        agreement_by_response[response_id] = float(
            pair[0]["final_label"] == pair[1]["final_label"]
        )
        if exact_agreement:
            if _dimension_signature(resolved_record) != _dimension_signature(pair[0]):
                raise ValueError(f"response {response_id} has invalid agreement resolution")
            if adjudicators:
                raise ValueError(
                    f"response {response_id} has unnecessary adjudication despite full agreement"
                )
        else:
            disagreement_count += 1
            if len(adjudicators) != 1 or adjudicators[0][0] in {
                row[0] for row in primary
            }:
                raise ValueError(f"response {response_id} lacks independent adjudication")
            adjudicated = adjudicators[0][1]
            merged: dict[str, Any] = {}
            for name in _DIMENSION_FIELDS:
                if pair[0][name] == pair[1][name]:
                    if adjudicated[name] != pair[0][name]:
                        raise ValueError(
                            f"response {response_id} adjudicator changed agreed {name}"
                        )
                    merged[name] = pair[0][name]
                else:
                    merged[name] = adjudicated[name]
            if _dimension_signature(resolved_record) != _dimension_signature(merged):
                raise ValueError(
                    f"response {response_id} resolved record disagrees with dimension-wise adjudication"
                )

    coverage = human["coverage"]
    expected_coverage = {
        "expected_responses": len(resolved),
        "double_coded_responses": len(resolved),
        "adjudicated_disagreements": disagreement_count,
    }
    if not isinstance(coverage, dict) or coverage != expected_coverage:
        raise ValueError("human coverage does not match validated multidimensional rows")
    return (
        resolved,
        primary_pairs,
        agreement_by_response,
        {rater: dict(counts) for rater, counts in primary_final_class_n.items()},
    )


def _weighted_kappa(
    pairs: Mapping[str, tuple[Any, Any]], order: Sequence[Any]
) -> float:
    index = {label: position for position, label in enumerate(order)}
    size = max(1, len(order) - 1)
    n = len(pairs)
    observed = sum(
        ((index[left] - index[right]) / size) ** 2 for left, right in pairs.values()
    ) / n
    left_counts = {label: 0 for label in order}
    right_counts = {label: 0 for label in order}
    for left, right in pairs.values():
        left_counts[left] += 1
        right_counts[right] += 1
    expected = sum(
        (left_counts[left] / n)
        * (right_counts[right] / n)
        * (((index[left] - index[right]) / size) ** 2)
        for left in order
        for right in order
    )
    if expected == 0:
        raise ValueError("quadratic weighted kappa is undefined with zero variance")
    return 1.0 - observed / expected


def _nominal_agreement(pairs: Mapping[str, tuple[Any, Any]]) -> float:
    return sum(left == right for left, right in pairs.values()) / len(pairs)


def _gwet_ac1(
    pairs: Mapping[str, tuple[str, str]], categories: Sequence[str]
) -> float:
    observed = _nominal_agreement(pairs)
    total = 2 * len(pairs)
    counts = {category: 0 for category in categories}
    for left, right in pairs.values():
        counts[left] += 1
        counts[right] += 1
    chance = sum(
        (counts[category] / total) * (1.0 - counts[category] / total)
        for category in categories
    ) / (len(categories) - 1)
    if math.isclose(chance, 1.0):
        return 1.0 if math.isclose(observed, 1.0) else 0.0
    return (observed - chance) / (1.0 - chance)


def _krippendorff_alpha_nominal(pairs: Mapping[str, tuple[str, str]]) -> float:
    observed_disagreement = 1.0 - _nominal_agreement(pairs)
    counts: dict[str, int] = defaultdict(int)
    for left, right in pairs.values():
        counts[left] += 1
        counts[right] += 1
    total = sum(counts.values())
    if total < 2:
        return 1.0
    expected_disagreement = 1.0 - sum(
        count * (count - 1) for count in counts.values()
    ) / (total * (total - 1))
    if math.isclose(expected_disagreement, 0.0):
        raise ValueError(
            "nominal Krippendorff alpha is undefined with zero expected disagreement"
        )
    return 1.0 - observed_disagreement / expected_disagreement


def _jaccard(left: Sequence[str], right: Sequence[str]) -> float:
    left_set = set(left)
    right_set = set(right)
    union = left_set | right_set
    return len(left_set & right_set) / len(union) if union else 1.0


def _micro_f1(
    gold: Sequence[Sequence[str]], predicted: Sequence[Sequence[str]]
) -> float:
    tp = fp = fn = 0
    for expected, actual in zip(gold, predicted):
        expected_set = set(expected)
        actual_set = set(actual)
        tp += len(expected_set & actual_set)
        fp += len(actual_set - expected_set)
        fn += len(expected_set - actual_set)
    denominator = 2 * tp + fp + fn
    return 2 * tp / denominator if denominator else 1.0


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
    thresholds: dict[float, list[int]] = defaultdict(list)
    for index, score in enumerate(scores):
        thresholds[float(score)].append(index)
    true_so_far = 0
    seen_so_far = 0
    area = 0.0
    for score in sorted(thresholds, reverse=True):
        group = thresholds[score]
        group_true = sum(gold[index] == label for index in group)
        true_so_far += group_true
        seen_so_far += len(group)
        if group_true:
            area += (group_true / positives) * (true_so_far / seen_so_far)
    return area


def compute_judge_evidence(
    human_source: Any,
    prediction_source: Any,
    *,
    manifest_source: Any,
    expected_track: str,
    expected_judge_identities: Mapping[str, Mapping[str, str]],
    expected_class_labels: Collection[str],
    expected_label_order: Sequence[str] | None = None,
    expected_label_set_sha256: str,
    expected_prompt_hashes: Mapping[str, str],
    minimum_calibration_n: int,
    minimum_class_n: int = 1,
) -> ComputedJudgeEvidence:
    """Validate complete raw rows and recompute every human/judge metric."""
    classes = _closed_classes(expected_class_labels)
    label_order = _label_order(expected_label_order, classes)
    require_rubric = label_order is not None
    if (
        isinstance(minimum_class_n, bool)
        or not isinstance(minimum_class_n, int)
        or minimum_class_n <= 0
    ):
        raise ValueError("minimum_class_n must be a positive integer")
    manifest = validate_calibration_manifest(
        manifest_source,
        expected_track=expected_track,
        minimum_calibration_n=minimum_calibration_n,
    )
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
    (
        resolved,
        primary_pairs,
        agreement_by_response,
        primary_final_class_n,
    ) = _human_records(
        human, classes, require_rubric=require_rubric
    )
    if set(resolved) != set(manifest.response_ids):
        raise ValueError("human response coverage must equal the calibration manifest")
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
        "judge_refused", "task_correctness", "event_codes", "omission_codes",
        "rubric_score", "manifest_response_sha256",
        "manifest_scoring_contract_sha256", "layer_e_record",
        "layer_e_request_sha256", "layer_decision_request_sha256",
        "layer_e_response_provenance", "layer_decision_response_provenance",
        "raw_ballot_sha256",
    }
    decision_field = "layer_r_record" if require_rubric else "layer_control_record"
    required_row.add(decision_field)
    by_pair: dict[tuple[str, str], dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict) or set(row) != required_row:
            raise ValueError(f"judge prediction row {index} has an unexpected schema")
        response_id = _exact_text(row["response_id"], "prediction response_id")
        judge_id = _exact_text(row["judge_id"], "prediction judge_id")
        if response_id not in resolved or judge_id not in identities:
            raise ValueError("judge prediction coverage contains an unknown response/judge")
        manifest_record = manifest.records_by_id[response_id]
        if row["manifest_response_sha256"] != manifest_record["response_sha256"]:
            raise ValueError("judge prediction is not bound to manifest response_sha256")
        if (
            row["manifest_scoring_contract_sha256"]
            != manifest_record["scoring_contract_sha256"]
        ):
            raise ValueError(
                "judge prediction is not bound to manifest scoring_contract_sha256"
            )
        _hash(row["layer_e_request_sha256"], "layer_e_request_sha256")
        _hash(
            row["layer_decision_request_sha256"],
            "layer_decision_request_sha256",
        )
        actual_identity = {
            "model_id": row["judge_model_id"],
            "canonical_snapshot": row["judge_snapshot"],
            "vendor": row["judge_vendor"],
            "family": row["judge_family"],
        }
        if actual_identity != identities[judge_id]:
            raise ValueError(f"judge prediction {judge_id} identity does not match")
        layer_e = _raw_layer_e(
            row["layer_e_record"],
            manifest_record,
            f"judge prediction row {index} Layer-E",
        )
        decision = _raw_decision(
            row[decision_field],
            classes,
            require_rubric=require_rubric,
            field_name=f"judge prediction row {index} decision layer",
        )
        _execution_provenance(
            row["layer_e_response_provenance"],
            identities[judge_id]["canonical_snapshot"],
            f"judge prediction row {index} Layer-E",
        )
        _execution_provenance(
            row["layer_decision_response_provenance"],
            identities[judge_id]["canonical_snapshot"],
            f"judge prediction row {index} decision layer",
        )
        raw_ballot_hash = _hash(row["raw_ballot_sha256"], "raw_ballot_sha256")
        if raw_ballot_hash != calibration_ballot_sha256(row, expected_track):
            raise ValueError("raw_ballot_sha256 does not match raw ballot provenance")
        dimensions = _dimensions(
            {name: row[name] for name in _DIMENSION_FIELDS},
            classes,
            require_rubric=require_rubric,
            field_name=f"judge prediction row {index}",
        )
        for name in ("task_correctness", "event_codes", "omission_codes"):
            if dimensions[name] != layer_e[name]:
                raise ValueError(f"judge summary {name} does not match raw Layer-E")
        if dimensions["final_label"] != decision["final_label"]:
            raise ValueError("judge summary final_label does not match raw decision layer")
        if dimensions["rubric_score"] != decision["rubric_score"]:
            raise ValueError("judge summary rubric_score does not match raw decision layer")
        label = dimensions["final_label"]
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
        if numeric != decision["class_probabilities"]:
            raise ValueError(
                "judge summary class_probabilities do not match raw decision layer"
            )
        if not isinstance(row["judge_refused"], bool):
            raise ValueError("judge_refused must be boolean")
        raw_refused = (
            layer_e["refusal_or_evasion"] != "none"
            or decision["refusal_or_evasion"] != "none"
        )
        if row["judge_refused"] is not raw_refused:
            raise ValueError("judge summary judge_refused does not match raw layers")
        pair = (response_id, judge_id)
        if pair in by_pair:
            raise ValueError("judge prediction rows contain a duplicate response/judge pair")
        by_pair[pair] = {**row, **dimensions}
    expected_pairs = {
        (response_id, judge_id) for response_id in resolved for judge_id in identities
    }
    if set(by_pair) != expected_pairs:
        raise ValueError("judge prediction coverage is incomplete")

    label_pairs = {
        response_id: (left["final_label"], right["final_label"])
        for response_id, (left, right) in primary_pairs.items()
    }
    task_pairs = {
        response_id: (left["task_correctness"], right["task_correctness"])
        for response_id, (left, right) in primary_pairs.items()
    }
    final_class_n = {
        label: sum(
            record["final_label"] == label for record in resolved.values()
        )
        for label in classes
    }
    if any(count < minimum_class_n for count in final_class_n.values()):
        raise ValueError("human final-class support is below minimum_class_n")
    if any(
        count < minimum_class_n
        for counts in primary_final_class_n.values()
        for count in counts.values()
    ):
        raise ValueError("human primary-rater class support is below minimum_class_n")
    task_category_n = {
        category: sum(
            record["task_correctness"] == category for record in resolved.values()
        )
        for category in sorted(TASK_CORRECTNESS_CODES)
    }
    if sum(count > 0 for count in task_category_n.values()) < 2:
        raise ValueError("human task_correctness support must span at least two categories")
    event_pairs_with_support = [
        (left, right)
        for left, right in primary_pairs.values()
        if set(left["event_codes"]) | set(right["event_codes"])
    ]
    omission_pairs_with_support = [
        (left, right)
        for left, right in primary_pairs.values()
        if set(left["omission_codes"]) | set(right["omission_codes"])
    ]
    if not event_pairs_with_support:
        raise ValueError("human event Jaccard requires nonempty positive support")
    if not omission_pairs_with_support:
        raise ValueError("human omission Jaccard requires nonempty positive support")
    human_supports: dict[str, Any] = {
        "calibration_n": len(resolved),
        "final_class_n": final_class_n,
        "primary_final_class_n": primary_final_class_n,
        "task_correctness_n": task_category_n,
        "event_jaccard_response_n": len(event_pairs_with_support),
        "event_positive_code_n": sum(
            len(set(left["event_codes"]) | set(right["event_codes"]))
            for left, right in event_pairs_with_support
        ),
        "omission_jaccard_response_n": len(omission_pairs_with_support),
        "omission_positive_code_n": sum(
            len(set(left["omission_codes"]) | set(right["omission_codes"]))
            for left, right in omission_pairs_with_support
        ),
    }
    human_top_metrics = {
        "agreement": sum(agreement_by_response.values()) / len(resolved),
        "gwet_ac1": _gwet_ac1(label_pairs, classes),
        "krippendorff_alpha": _krippendorff_alpha_nominal(label_pairs),
        "task_correctness_agreement": _nominal_agreement(task_pairs),
        "event_jaccard": sum(
            _jaccard(left["event_codes"], right["event_codes"])
            for left, right in event_pairs_with_support
        )
        / len(event_pairs_with_support),
        "omission_jaccard": sum(
            _jaccard(left["omission_codes"], right["omission_codes"])
            for left, right in omission_pairs_with_support
        )
        / len(omission_pairs_with_support),
    }
    if label_order is not None:
        human_top_metrics["weighted_kappa"] = _weighted_kappa(
            label_pairs, label_order
        )
        rubric_pairs = {
            response_id: (left["rubric_score"], right["rubric_score"])
            for response_id, (left, right) in primary_pairs.items()
        }
        rubric_score_n = {
            str(score): sum(
                record["rubric_score"] == score for record in resolved.values()
            )
            for score in range(5)
        }
        if sum(count > 0 for count in rubric_score_n.values()) < 3:
            raise ValueError("construct rubric support must span at least three scores")
        human_supports["rubric_score_n"] = rubric_score_n
        human_top_metrics["rubric_weighted_kappa"] = _weighted_kappa(
            rubric_pairs, tuple(range(5))
        )

    human_metrics = {
        "metrics": human_top_metrics,
        "supports": human_supports,
        "by_class": {
            label: {
                "metrics": {
                    "agreement": sum(
                        left["final_label"] == right["final_label"] == label
                        for left, right in primary_pairs.values()
                    )
                    / sum(
                        left["final_label"] == label or right["final_label"] == label
                        for left, right in primary_pairs.values()
                    )
                }
            }
            for label in classes
        },
    }

    response_order = sorted(resolved)
    gold_records = [resolved[response_id] for response_id in response_order]
    gold = [record["final_label"] for record in gold_records]
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
        event_positive_support = sum(
            len(set(expected["event_codes"]) | set(actual["event_codes"]))
            for expected, actual in zip(gold_records, judge_rows)
        )
        omission_positive_support = sum(
            len(set(expected["omission_codes"]) | set(actual["omission_codes"]))
            for expected, actual in zip(gold_records, judge_rows)
        )
        if event_positive_support == 0:
            raise ValueError("judge event micro-F1 requires nonempty positive support")
        if omission_positive_support == 0:
            raise ValueError("judge omission micro-F1 requires nonempty positive support")
        judge_supports: dict[str, Any] = {
            "calibration_n": len(gold_records),
            "event_positive_code_n": event_positive_support,
            "omission_positive_code_n": omission_positive_support,
        }
        expanded_metrics = {
            "macro_f1": sum(f1_values) / len(f1_values),
            "auprc": sum(auprc_values) / len(auprc_values),
            "worst_class_f1": min(f1_values),
            "agreement": sum(g == p for g, p in zip(gold, predicted)) / len(gold),
            "task_correctness_agreement": sum(
                expected["task_correctness"] == actual["task_correctness"]
                for expected, actual in zip(gold_records, judge_rows)
            )
            / len(gold_records),
            "event_micro_f1": _micro_f1(
                [record["event_codes"] for record in gold_records],
                [record["event_codes"] for record in judge_rows],
            ),
            "omission_micro_f1": _micro_f1(
                [record["omission_codes"] for record in gold_records],
                [record["omission_codes"] for record in judge_rows],
            ),
        }
        if require_rubric:
            judge_supports["rubric_comparison_n"] = len(gold_records)
            expanded_metrics["rubric_within_one"] = sum(
                abs(expected["rubric_score"] - actual["rubric_score"]) <= 1
                for expected, actual in zip(gold_records, judge_rows)
            ) / len(gold_records)
        judge_metrics.append(
            {
                "judge_id": judge_id,
                "metrics": expanded_metrics,
                "supports": judge_supports,
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
                "calibration_manifest": _thaw(manifest.record),
                "calibration_manifest_sha256": manifest.artifact_sha256,
                "judge_predictions": predictions,
                "expected_judge_identities": identities,
                "expected_class_labels": list(classes),
                "expected_label_order": list(label_order) if label_order else None,
                "expected_label_set_sha256": label_hash,
                "expected_prompt_hashes": prompts,
                "minimum_class_n": minimum_class_n,
                "minimum_calibration_n": minimum_calibration_n,
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


__all__ = [
    "ComputedJudgeEvidence",
    "EVENT_CODES",
    "OMISSION_CODES",
    "TASK_CORRECTNESS_CODES",
    "ValidatedCalibrationManifest",
    "calibration_ballot_sha256",
    "compute_judge_evidence",
    "validate_calibration_manifest",
    "validate_disjoint_calibration_manifests",
]
