"""Fail-closed validation for human-anchored judge approval artifacts.

The validator consumes strict JSON (or a mapping that can be represented as
strict JSON), verifies it against the caller's current design and input hashes,
and returns a deeply immutable record.  It never supplies defaults, coerces
values, repairs identifiers, or treats synthetic evidence as live approval.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from collections.abc import Collection, Mapping
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
from types import MappingProxyType
from typing import Any, Union

try:
    from .judge_evidence import ComputedJudgeEvidence
except ImportError:  # direct-module script compatibility
    from judge_evidence import ComputedJudgeEvidence


SUPPORTED_SCHEMA_VERSION = "1.0"
_SHA256_RE = re.compile(r"[0-9a-fA-F]{64}\Z")
_JUDGE_ID_RE = re.compile(r"J[0-9]{2}\Z")
_REQUIRED_TOP_LEVEL = frozenset(
    {
        "schema_version",
        "design",
        "approved_for_live",
        "label_set_sha256",
        "human_label_set_sha256",
        "calibration_evidence_sha256",
        "prompt_hashes",
        "policy",
        "human_human",
        "judges",
        "human_availability",
        "completed_at",
    }
)
_REQUIRED_JUDGE_METRICS = frozenset(
    {"macro_f1", "auprc", "worst_class_f1", "agreement"}
)
_REQUIRED_HUMAN_METRICS = frozenset({"agreement"})
_REQUIRED_JUDGE_CLASS_METRICS = frozenset({"f1", "auprc"})
_REQUIRED_HUMAN_CLASS_METRICS = frozenset({"agreement"})
_REQUIRED_JUDGE_FIELDS = frozenset(
    {
        "judge_id",
        "model_id",
        "canonical_snapshot",
        "vendor",
        "family",
        "metrics",
        "thresholds",
        "by_class",
        "calibration_n",
        "refusal_rate",
        "max_refusal_rate",
    }
)
_PROMPT_LAYERS = frozenset({"layer_e", "layer_r"})
_POLICY_FIELDS = frozenset(
    {
        "human_human_thresholds",
        "human_by_class_thresholds",
        "judge_thresholds",
        "judge_by_class_thresholds",
        "minimum_calibration_n",
        "maximum_refusal_rate",
    }
)


class JudgeValidationError(ValueError):
    """The artifact cannot authorize a live judge stack."""


_VALIDATION_ATTESTATION = object()


@dataclass(frozen=True)
class ValidatedJudgeValidation:
    """Immutable validated JSON record and SHA-256 of its source artifact."""

    record: Mapping[str, Any]
    artifact_sha256: str
    calibration_evidence_sha256: str = ""
    evidence_verified: bool = False
    _attestation: object = field(default=None, repr=False, compare=False)

    def __post_init__(self) -> None:
        if self._attestation is not _VALIDATION_ATTESTATION:
            raise TypeError(
                "ValidatedJudgeValidation can be created only by the artifact validator"
            )


ArtifactSource = Union[str, bytes, bytearray, Path, Mapping[str, Any]]


def _fail(message: str) -> JudgeValidationError:
    return JudgeValidationError(message)


def _validate_mapping_json_types(value: Any, path: str = "artifact") -> None:
    if isinstance(value, Mapping):
        for key, child in value.items():
            if not isinstance(key, str):
                raise _fail(f"{path} has a non-string JSON key")
            _validate_mapping_json_types(child, f"{path}.{key}")
        return
    if isinstance(value, (list, tuple)):
        for index, child in enumerate(value):
            _validate_mapping_json_types(child, f"{path}[{index}]")
        return
    if value is None or isinstance(value, (str, bool, int)):
        return
    if isinstance(value, float):
        if not math.isfinite(value):
            raise _fail(f"{path} must contain finite numeric values")
        return
    raise _fail(f"{path} contains a non-JSON value")


def _source_bytes(source: ArtifactSource) -> bytes:
    if isinstance(source, Path):
        try:
            return source.read_bytes()
        except OSError as exc:
            raise _fail(f"cannot read judge-validation artifact: {source}") from exc
    if isinstance(source, bytes):
        return source
    if isinstance(source, bytearray):
        return bytes(source)
    if isinstance(source, Mapping):
        _validate_mapping_json_types(source)
        try:
            return json.dumps(
                source,
                sort_keys=True,
                separators=(",", ":"),
                ensure_ascii=False,
                allow_nan=False,
            ).encode("utf-8")
        except (TypeError, ValueError) as exc:
            raise _fail("artifact mapping is not strict JSON") from exc
    if isinstance(source, str):
        if source.lstrip().startswith("{"):
            return source.encode("utf-8")
        try:
            return Path(source).read_bytes()
        except OSError as exc:
            raise _fail(f"cannot read judge-validation artifact: {source}") from exc
    raise _fail("artifact source must be JSON text, bytes, a path, or a mapping")


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key, value in pairs:
        if key in output:
            raise _fail(f"duplicate JSON key {key!r}")
        output[key] = value
    return output


def _reject_constant(value: str) -> None:
    raise _fail(f"non-standard numeric constant {value!r} is forbidden")


def _parse_json(raw: bytes) -> dict[str, Any]:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise _fail("judge-validation artifact is not UTF-8") from exc
    try:
        value = json.loads(
            text,
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
        )
    except JudgeValidationError:
        raise
    except json.JSONDecodeError as exc:
        raise _fail("judge-validation artifact is not valid JSON") from exc
    if not isinstance(value, dict):
        raise _fail("judge-validation artifact must be a JSON object")
    return value


def _exact_text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise _fail(f"{field} must be an exact non-blank string")
    return value


def _sha256(value: Any, field: str) -> str:
    if not isinstance(value, str) or _SHA256_RE.fullmatch(value) is None:
        raise _fail(f"{field} must be exactly 64 hexadecimal characters")
    return value


def _same_hash(actual: str, expected: str, field: str) -> None:
    if actual.casefold() != expected.casefold():
        raise _fail(f"{field} does not match the current expected hash")


def _mapping(value: Any, field: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise _fail(f"{field} must be an object")
    return value


def _finite_number(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise _fail(f"{field} must be a finite numeric value")
    numeric = float(value)
    if not math.isfinite(numeric):
        raise _fail(f"{field} must be a finite numeric value")
    return numeric


def _metric_block(
    block: Any,
    field: str,
    *,
    required_metrics: frozenset[str] = frozenset(),
    bounds: tuple[float, float] | None = None,
) -> None:
    value = _mapping(block, field)
    missing_parts = {"metrics", "thresholds"} - set(value)
    if missing_parts:
        raise _fail(f"{field} missing {sorted(missing_parts)}")
    metrics = _mapping(value["metrics"], f"{field}.metrics")
    thresholds = _mapping(value["thresholds"], f"{field}.thresholds")
    if not metrics or not thresholds:
        raise _fail(f"{field} metrics and thresholds must be non-empty")
    missing_metrics = required_metrics - set(metrics)
    missing_thresholds = required_metrics - set(thresholds)
    if missing_metrics:
        raise _fail(f"{field}.metrics missing {sorted(missing_metrics)}")
    if missing_thresholds:
        raise _fail(f"{field}.thresholds missing {sorted(missing_thresholds)}")
    if set(metrics) != set(thresholds):
        raise _fail(f"{field} metrics and thresholds must name exactly the same fields")

    for name in metrics:
        _exact_text(name, f"{field} metric name")
        metric = _finite_number(metrics[name], f"{field}.metrics.{name}")
        threshold = _finite_number(
            thresholds[name], f"{field}.thresholds.{name}"
        )
        if bounds is not None and not (
            bounds[0] <= metric <= bounds[1]
            and bounds[0] <= threshold <= bounds[1]
        ):
            raise _fail(f"{field}.{name} must be within {bounds}")
        if metric < threshold:
            raise _fail(f"{field}.{name} is below threshold")


def _class_metric_blocks(
    parent: Mapping[str, Any],
    field: str,
    *,
    required_metrics: frozenset[str],
) -> tuple[frozenset[str], dict[str, Mapping[str, Any]]]:
    if "by_class" not in parent:
        raise _fail(f"{field} missing by_class metrics")
    by_class = _mapping(parent["by_class"], f"{field}.by_class")
    if not by_class:
        raise _fail(f"{field}.by_class must be non-empty")
    validated: dict[str, Mapping[str, Any]] = {}
    for label, block in by_class.items():
        class_label = _exact_text(label, f"{field}.by_class label")
        class_field = f"{field}.by_class.{class_label}"
        _metric_block(
            block,
            class_field,
            required_metrics=required_metrics,
            bounds=(0.0, 1.0),
        )
        validated[class_label] = _mapping(block, class_field)
    return frozenset(validated), validated


def _validate_completed_at(value: Any) -> None:
    text = _exact_text(value, "completed_at")
    if "T" not in text or not text.endswith("Z"):
        raise _fail("completed_at must be an explicit UTC timestamp ending in Z")
    try:
        parsed = datetime.fromisoformat(text[:-1] + "+00:00")
    except ValueError as exc:
        raise _fail("completed_at must be a valid UTC timestamp") from exc
    if parsed.utcoffset() != timedelta(0):
        raise _fail("completed_at must be UTC")


def _validate_identity_text(value: Any, field: str, *, model: bool = False) -> str:
    text = _exact_text(value, field)
    if model and ("/" not in text or "*" in text):
        raise _fail(f"{field} must be an exact provider/model identifier")
    if model and any(
        segment.casefold() in {"latest", "auto"} for segment in text.split("/")
    ):
        raise _fail(f"{field} must identify an exact snapshot, not an alias")
    return text


def _validate_expected_judge_identities(
    value: Any,
) -> dict[str, dict[str, str]]:
    identities = _mapping(value, "expected_judge_identities")
    if len(identities) < 2:
        raise _fail("expected_judge_identities must contain at least two judges")
    expected: dict[str, dict[str, str]] = {}
    required = {"model_id", "canonical_snapshot", "vendor", "family"}
    for judge_id, raw in identities.items():
        exact_id = _exact_text(judge_id, "expected_judge_identities judge_id")
        if _JUDGE_ID_RE.fullmatch(exact_id) is None:
            raise _fail("expected_judge_identities keys must be opaque J## identifiers")
        identity = _mapping(raw, f"expected_judge_identities.{exact_id}")
        if set(identity) != required:
            raise _fail(
                f"expected_judge_identities.{exact_id} must contain exactly "
                f"{sorted(required)}"
            )
        expected[exact_id] = {
            "model_id": _validate_identity_text(
                identity["model_id"],
                f"expected_judge_identities.{exact_id}.model_id",
                model=True,
            ),
            "canonical_snapshot": _validate_identity_text(
                identity["canonical_snapshot"],
                f"expected_judge_identities.{exact_id}.canonical_snapshot",
                model=True,
            ),
            "vendor": _validate_identity_text(
                identity["vendor"],
                f"expected_judge_identities.{exact_id}.vendor",
            ),
            "family": _validate_identity_text(
                identity["family"],
                f"expected_judge_identities.{exact_id}.family",
            ),
        }
    return expected


def _validate_expected_class_labels(value: Any) -> frozenset[str]:
    if (
        not isinstance(value, Collection)
        or isinstance(value, (str, bytes, bytearray, Mapping))
        or not value
    ):
        raise _fail("expected_class_labels must be a non-empty collection")
    labels = [
        _exact_text(label, "expected_class_labels entry")
        for label in value
    ]
    if len(set(labels)) != len(labels):
        raise _fail("expected_class_labels must be unique")
    return frozenset(labels)


def _canonical_mapping_sha256(value: Mapping[str, Any]) -> str:
    _validate_mapping_json_types(value, "policy")
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _policy_thresholds(
    value: Any,
    field: str,
    required_names: frozenset[str],
) -> dict[str, float]:
    thresholds = _mapping(value, field)
    if set(thresholds) != required_names:
        raise _fail(f"policy {field} must contain exactly {sorted(required_names)}")
    result: dict[str, float] = {}
    for name, raw in thresholds.items():
        numeric = _finite_number(raw, f"policy.{field}.{name}")
        if not 0.0 <= numeric <= 1.0:
            raise _fail(f"policy.{field}.{name} must be within [0, 1]")
        result[name] = numeric
    return result


def _validate_policy(
    value: Any,
    *,
    expected_sha256: str,
    expected_classes: frozenset[str],
) -> dict[str, Any]:
    policy = _mapping(value, "policy")
    if set(policy) != _POLICY_FIELDS:
        raise _fail(f"policy must contain exactly {sorted(_POLICY_FIELDS)}")
    actual_hash = _canonical_mapping_sha256(policy)
    if actual_hash.casefold() != expected_sha256.casefold():
        raise _fail("policy hash does not match expected_policy_sha256")

    human_top_raw = _mapping(
        policy["human_human_thresholds"], "policy.human_human_thresholds"
    )
    if "agreement" not in human_top_raw:
        raise _fail("policy.human_human_thresholds must include agreement")
    human_top = _policy_thresholds(
        human_top_raw,
        "human_human_thresholds",
        frozenset(human_top_raw),
    )
    judge_top = _policy_thresholds(
        policy["judge_thresholds"],
        "judge_thresholds",
        _REQUIRED_JUDGE_METRICS,
    )

    def by_class(
        raw: Any, field: str, required: frozenset[str]
    ) -> dict[str, dict[str, float]]:
        blocks = _mapping(raw, f"policy.{field}")
        if set(blocks) != expected_classes:
            raise _fail(f"policy.{field} must match expected_class_labels")
        return {
            label: _policy_thresholds(
                blocks[label], f"{field}.{label}", required
            )
            for label in expected_classes
        }

    minimum_n = policy["minimum_calibration_n"]
    if isinstance(minimum_n, bool) or not isinstance(minimum_n, int) or minimum_n <= 0:
        raise _fail("policy.minimum_calibration_n must be a positive integer")
    maximum_refusal = _finite_number(
        policy["maximum_refusal_rate"], "policy.maximum_refusal_rate"
    )
    if not 0.0 <= maximum_refusal <= 1.0:
        raise _fail("policy.maximum_refusal_rate must be within [0, 1]")
    return {
        "human_human_thresholds": human_top,
        "human_by_class_thresholds": by_class(
            policy["human_by_class_thresholds"],
            "human_by_class_thresholds",
            _REQUIRED_HUMAN_CLASS_METRICS,
        ),
        "judge_thresholds": judge_top,
        "judge_by_class_thresholds": by_class(
            policy["judge_by_class_thresholds"],
            "judge_by_class_thresholds",
            _REQUIRED_JUDGE_CLASS_METRICS,
        ),
        "minimum_calibration_n": minimum_n,
        "maximum_refusal_rate": maximum_refusal,
    }


def _require_thresholds_match(
    actual: Any, expected: Mapping[str, float], field: str
) -> None:
    thresholds = _mapping(actual, field)
    if set(thresholds) != set(expected):
        raise _fail(f"{field} does not match policy thresholds")
    for name, expected_value in expected.items():
        actual_value = _finite_number(thresholds[name], f"{field}.{name}")
        if not math.isclose(actual_value, expected_value, abs_tol=1e-12):
            raise _fail(f"{field}.{name} does not match policy threshold")


def _validate_judges(
    raw_judges: Any,
    expected_identities: Mapping[str, Mapping[str, str]],
    policy: Mapping[str, Any],
) -> frozenset[str]:
    if not isinstance(raw_judges, list) or len(raw_judges) < 2:
        raise _fail("judges must contain at least two validated judges")
    seen = {field: set() for field in (
        "judge_id", "model_id", "canonical_snapshot", "vendor", "family"
    )}
    observed_ids: set[str] = set()
    shared_classes: frozenset[str] | None = None
    for index, raw in enumerate(raw_judges):
        field = f"judges[{index}]"
        judge = _mapping(raw, field)
        missing = _REQUIRED_JUDGE_FIELDS - set(judge)
        if missing:
            raise _fail(f"{field} missing {sorted(missing)}")

        judge_id = _exact_text(judge["judge_id"], f"{field}.judge_id")
        if _JUDGE_ID_RE.fullmatch(judge_id) is None:
            raise _fail(f"{field}.judge_id must be an opaque J## identifier")
        identity = {
            "judge_id": judge_id,
            "model_id": _validate_identity_text(
                judge["model_id"], f"{field}.model_id", model=True
            ),
            "canonical_snapshot": _validate_identity_text(
                judge["canonical_snapshot"],
                f"{field}.canonical_snapshot",
                model=True,
            ),
            "vendor": _validate_identity_text(judge["vendor"], f"{field}.vendor"),
            "family": _validate_identity_text(judge["family"], f"{field}.family"),
        }
        if any("openai" in value.casefold() for value in identity.values()):
            raise _fail(f"{field} must identify a non-OpenAI judge")
        for name, value in identity.items():
            canonical = value.casefold()
            if canonical in seen[name]:
                raise _fail(f"overlapping judge identity field {name}: {value!r}")
            seen[name].add(canonical)
        expected = expected_identities.get(judge_id)
        if expected is None:
            raise _fail(
                f"{field}.judge_id is absent from expected_judge_identities"
            )
        for name in ("model_id", "canonical_snapshot", "vendor", "family"):
            if identity[name] != expected[name]:
                raise _fail(
                    f"{field}.{name} does not match the expected catalog identity"
                )
        observed_ids.add(judge_id)

        _metric_block(
            judge,
            field,
            required_metrics=_REQUIRED_JUDGE_METRICS,
            bounds=(0.0, 1.0),
        )
        _require_thresholds_match(
            judge["thresholds"],
            policy["judge_thresholds"],
            f"{field}.thresholds",
        )
        class_names, class_blocks = _class_metric_blocks(
            judge,
            field,
            required_metrics=_REQUIRED_JUDGE_CLASS_METRICS,
        )
        if shared_classes is None:
            shared_classes = class_names
        elif class_names != shared_classes:
            raise _fail("all judges must report the same by_class labels")
        for label in class_names:
            _require_thresholds_match(
                class_blocks[label]["thresholds"],
                policy["judge_by_class_thresholds"][label],
                f"{field}.by_class.{label}.thresholds",
            )
        observed_worst = min(
            _finite_number(
                class_blocks[label]["metrics"]["f1"],
                f"{field}.by_class.{label}.metrics.f1",
            )
            for label in class_names
        )
        declared_worst = _finite_number(
            judge["metrics"]["worst_class_f1"],
            f"{field}.metrics.worst_class_f1",
        )
        if not math.isclose(declared_worst, observed_worst, abs_tol=1e-12):
            raise _fail(
                f"{field}.worst_class_f1 must equal the observed by_class minimum"
            )
        calibration_n = judge["calibration_n"]
        if (
            isinstance(calibration_n, bool)
            or not isinstance(calibration_n, int)
            or calibration_n <= 0
        ):
            raise _fail(f"{field}.calibration_n must be a positive integer")
        if calibration_n < policy["minimum_calibration_n"]:
            raise _fail(
                f"{field}.calibration_n is below policy minimum_calibration_n"
            )
        refusal = _finite_number(judge["refusal_rate"], f"{field}.refusal_rate")
        maximum = _finite_number(
            judge["max_refusal_rate"], f"{field}.max_refusal_rate"
        )
        if not 0.0 <= refusal <= 1.0 or not 0.0 <= maximum <= 1.0:
            raise _fail(f"{field} refusal rates must be within [0, 1]")
        if refusal > maximum:
            raise _fail(f"{field} refusal_rate exceeds its declared maximum")
        if maximum > policy["maximum_refusal_rate"]:
            raise _fail(
                f"{field}.max_refusal_rate exceeds policy maximum_refusal_rate"
            )
    if observed_ids != set(expected_identities):
        raise _fail(
            "judges must match expected_judge_identities exactly"
        )
    if shared_classes is None:
        raise _fail("judges require by_class results")
    return shared_classes


def _validate_human_availability(value: Any) -> None:
    availability = _mapping(value, "human_availability")
    for field in ("available_for_live", "verified", "declaration"):
        if field not in availability:
            raise _fail(f"human_availability missing {field}")
    if availability["available_for_live"] is not True:
        raise _fail("human_availability.available_for_live must be true")
    if availability["verified"] is not True:
        raise _fail("human_availability.verified must be true")
    _exact_text(availability["declaration"], "human_availability.declaration")


def _deep_freeze(value: Any) -> Any:
    if isinstance(value, dict):
        return MappingProxyType({key: _deep_freeze(child) for key, child in value.items()})
    if isinstance(value, list):
        return tuple(_deep_freeze(child) for child in value)
    return value


def _same_number(actual: Any, expected: Any, field: str) -> None:
    left = _finite_number(actual, field)
    right = _finite_number(expected, f"computed {field}")
    if abs(left - right) > 1e-12:
        raise _fail(f"{field} does not match recomputed calibration evidence")


def _compare_metric_values(
    artifact_block: Mapping[str, Any],
    computed_block: Mapping[str, Any],
    field: str,
) -> None:
    artifact_metrics = _mapping(artifact_block.get("metrics"), f"{field}.metrics")
    computed_metrics = _mapping(computed_block.get("metrics"), f"computed {field}.metrics")
    if set(artifact_metrics) != set(computed_metrics):
        raise _fail(f"{field}.metrics do not match recomputed metric names")
    for name in artifact_metrics:
        _same_number(
            artifact_metrics[name],
            computed_metrics[name],
            f"{field}.metrics.{name}",
        )


def _compare_computed_evidence(
    record: Mapping[str, Any], evidence: ComputedJudgeEvidence
) -> None:
    if not isinstance(evidence, ComputedJudgeEvidence):
        raise _fail("computed_evidence must be an attested ComputedJudgeEvidence")
    _compare_metric_values(record["human_human"], evidence.human_human, "human_human")
    artifact_human_classes = _mapping(
        record["human_human"].get("by_class"), "human_human.by_class"
    )
    computed_human_classes = _mapping(
        evidence.human_human.get("by_class"), "computed human_human.by_class"
    )
    if set(artifact_human_classes) != set(computed_human_classes):
        raise _fail("human_human.by_class does not match recomputed class coverage")
    for label in artifact_human_classes:
        _compare_metric_values(
            artifact_human_classes[label],
            computed_human_classes[label],
            f"human_human.by_class.{label}",
        )

    artifact_judges = {
        judge["judge_id"]: judge for judge in record["judges"]
    }
    computed_judges = {
        judge["judge_id"]: judge for judge in evidence.judges
    }
    if set(artifact_judges) != set(computed_judges):
        raise _fail("judges do not match recomputed judge coverage")
    for judge_id, artifact_judge in artifact_judges.items():
        computed_judge = computed_judges[judge_id]
        _compare_metric_values(
            artifact_judge,
            computed_judge,
            f"judges.{judge_id}",
        )
        if artifact_judge["calibration_n"] != computed_judge["calibration_n"]:
            raise _fail(
                f"judges.{judge_id}.calibration_n does not match recomputed evidence"
            )
        _same_number(
            artifact_judge["refusal_rate"],
            computed_judge["refusal_rate"],
            f"judges.{judge_id}.refusal_rate",
        )
        artifact_classes = _mapping(
            artifact_judge.get("by_class"), f"judges.{judge_id}.by_class"
        )
        computed_classes = _mapping(
            computed_judge.get("by_class"), f"computed judges.{judge_id}.by_class"
        )
        if set(artifact_classes) != set(computed_classes):
            raise _fail(
                f"judges.{judge_id}.by_class does not match recomputed coverage"
            )
        for label in artifact_classes:
            _compare_metric_values(
                artifact_classes[label],
                computed_classes[label],
                f"judges.{judge_id}.by_class.{label}",
            )


def validate_judge_validation_artifact(
    source: ArtifactSource,
    *,
    expected_design: str,
    expected_label_set_sha256: str,
    expected_human_label_set_sha256: str,
    expected_prompt_hashes: Mapping[str, str],
    expected_judge_identities: Mapping[str, Mapping[str, str]],
    expected_class_labels: Collection[str],
    expected_policy_sha256: str,
    computed_evidence: ComputedJudgeEvidence | None = None,
) -> ValidatedJudgeValidation:
    """Validate a human judge artifact against current immutable inputs.

    Hash expectations are mandatory: without them an old but internally valid
    artifact could silently approve a new label set or prompt layer.
    """

    expected_design = _exact_text(expected_design, "expected_design")
    expected_label = _sha256(
        expected_label_set_sha256, "expected_label_set_sha256"
    )
    expected_human_label = _sha256(
        expected_human_label_set_sha256, "expected_human_label_set_sha256"
    )
    prompts = _mapping(expected_prompt_hashes, "expected_prompt_hashes")
    if set(prompts) != _PROMPT_LAYERS:
        raise _fail("expected_prompt_hashes must contain exactly layer_e and layer_r")
    expected_prompts = {
        name: _sha256(prompts[name], f"expected_prompt_hashes.{name}")
        for name in _PROMPT_LAYERS
    }
    expected_identities = _validate_expected_judge_identities(
        expected_judge_identities
    )
    expected_classes = _validate_expected_class_labels(expected_class_labels)
    expected_policy_hash = _sha256(
        expected_policy_sha256, "expected_policy_sha256"
    )

    raw = _source_bytes(source)
    record = _parse_json(raw)
    missing = _REQUIRED_TOP_LEVEL - set(record)
    if missing:
        raise _fail(f"artifact missing required top-level field(s): {sorted(missing)}")
    if record["schema_version"] != SUPPORTED_SCHEMA_VERSION:
        raise _fail(
            f"schema_version must be exactly {SUPPORTED_SCHEMA_VERSION!r}"
        )
    if _exact_text(record["design"], "design") != expected_design:
        raise _fail("design does not match the expected design")
    if record["approved_for_live"] is not True:
        raise _fail("approved_for_live must be exactly true")
    policy = _validate_policy(
        record["policy"],
        expected_sha256=expected_policy_hash,
        expected_classes=expected_classes,
    )

    label_hash = _sha256(record["label_set_sha256"], "label_set_sha256")
    human_label_hash = _sha256(
        record["human_label_set_sha256"], "human_label_set_sha256"
    )
    calibration_evidence_hash = _sha256(
        record["calibration_evidence_sha256"],
        "calibration_evidence_sha256",
    )
    _same_hash(label_hash, expected_label, "label_set_sha256")
    _same_hash(
        human_label_hash, expected_human_label, "human_label_set_sha256"
    )

    artifact_prompts = _mapping(record["prompt_hashes"], "prompt_hashes")
    if set(artifact_prompts) != _PROMPT_LAYERS:
        raise _fail("prompt_hashes must contain exactly layer_e and layer_r")
    for name in _PROMPT_LAYERS:
        actual = _sha256(artifact_prompts[name], f"prompt_hashes.{name}")
        _same_hash(actual, expected_prompts[name], f"prompt_hashes.{name}")

    _metric_block(
        record["human_human"],
        "human_human",
        required_metrics=_REQUIRED_HUMAN_METRICS,
        bounds=(-1.0, 1.0),
    )
    _require_thresholds_match(
        record["human_human"]["thresholds"],
        policy["human_human_thresholds"],
        "human_human.thresholds",
    )
    human_classes, _human_blocks = _class_metric_blocks(
        _mapping(record["human_human"], "human_human"),
        "human_human",
        required_metrics=_REQUIRED_HUMAN_CLASS_METRICS,
    )
    for label in human_classes:
        _require_thresholds_match(
            _human_blocks[label]["thresholds"],
            policy["human_by_class_thresholds"][label],
            f"human_human.by_class.{label}.thresholds",
        )
    judge_classes = _validate_judges(
        record["judges"], expected_identities, policy
    )
    if human_classes != expected_classes or judge_classes != expected_classes:
        raise _fail(
            "human and judge by_class coverage must equal expected_class_labels"
        )
    _validate_human_availability(record["human_availability"])
    _validate_completed_at(record["completed_at"])

    evidence_verified = computed_evidence is not None
    if computed_evidence is not None:
        if calibration_evidence_hash != computed_evidence.evidence_sha256:
            raise _fail(
                "calibration_evidence_sha256 does not match recomputed evidence"
            )
        _compare_computed_evidence(record, computed_evidence)

    return ValidatedJudgeValidation(
        record=_deep_freeze(record),
        artifact_sha256=hashlib.sha256(raw).hexdigest(),
        calibration_evidence_sha256=calibration_evidence_hash,
        evidence_verified=evidence_verified,
        _attestation=_VALIDATION_ATTESTATION,
    )
