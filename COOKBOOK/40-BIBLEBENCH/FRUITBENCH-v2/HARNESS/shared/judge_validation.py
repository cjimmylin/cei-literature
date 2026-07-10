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
from collections.abc import Mapping
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from types import MappingProxyType
from typing import Any, Union


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
        "prompt_hashes",
        "human_human",
        "judges",
        "human_availability",
        "completed_at",
    }
)
_REQUIRED_JUDGE_METRICS = frozenset(
    {"macro_f1", "worst_class_f1", "agreement"}
)
_REQUIRED_HUMAN_METRICS = frozenset({"agreement"})
_REQUIRED_JUDGE_FIELDS = frozenset(
    {
        "judge_id",
        "model_id",
        "canonical_snapshot",
        "vendor",
        "family",
        "metrics",
        "thresholds",
        "calibration_n",
        "refusal_rate",
        "max_refusal_rate",
    }
)
_PROMPT_LAYERS = frozenset({"layer_e", "layer_r"})


class JudgeValidationError(ValueError):
    """The artifact cannot authorize a live judge stack."""


@dataclass(frozen=True)
class ValidatedJudgeValidation:
    """Immutable validated JSON record and SHA-256 of its source artifact."""

    record: Mapping[str, Any]
    artifact_sha256: str


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


def _validate_judges(raw_judges: Any) -> None:
    if not isinstance(raw_judges, list) or len(raw_judges) < 2:
        raise _fail("judges must contain at least two validated judges")
    seen = {field: set() for field in (
        "judge_id", "model_id", "canonical_snapshot", "vendor", "family"
    )}
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

        _metric_block(
            judge,
            field,
            required_metrics=_REQUIRED_JUDGE_METRICS,
            bounds=(0.0, 1.0),
        )
        calibration_n = judge["calibration_n"]
        if (
            isinstance(calibration_n, bool)
            or not isinstance(calibration_n, int)
            or calibration_n <= 0
        ):
            raise _fail(f"{field}.calibration_n must be a positive integer")
        refusal = _finite_number(judge["refusal_rate"], f"{field}.refusal_rate")
        maximum = _finite_number(
            judge["max_refusal_rate"], f"{field}.max_refusal_rate"
        )
        if not 0.0 <= refusal <= 1.0 or not 0.0 <= maximum <= 1.0:
            raise _fail(f"{field} refusal rates must be within [0, 1]")
        if refusal > maximum:
            raise _fail(f"{field} refusal_rate exceeds its declared maximum")


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


def validate_judge_validation_artifact(
    source: ArtifactSource,
    *,
    expected_design: str,
    expected_label_set_sha256: str,
    expected_human_label_set_sha256: str,
    expected_prompt_hashes: Mapping[str, str],
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

    label_hash = _sha256(record["label_set_sha256"], "label_set_sha256")
    human_label_hash = _sha256(
        record["human_label_set_sha256"], "human_label_set_sha256"
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
    _validate_judges(record["judges"])
    _validate_human_availability(record["human_availability"])
    _validate_completed_at(record["completed_at"])

    return ValidatedJudgeValidation(
        record=_deep_freeze(record),
        artifact_sha256=hashlib.sha256(raw).hexdigest(),
    )
