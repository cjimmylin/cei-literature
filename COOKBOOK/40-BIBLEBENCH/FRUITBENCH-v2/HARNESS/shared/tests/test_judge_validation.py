from __future__ import annotations

import hashlib
import json
import sys
from dataclasses import FrozenInstanceError
from pathlib import Path

import pytest


HARNESS = Path(__file__).resolve().parents[2]
if str(HARNESS) not in sys.path:
    sys.path.insert(0, str(HARNESS))

from shared.judge_validation import (  # noqa: E402
    JudgeValidationError,
    ValidatedJudgeValidation,
    validate_judge_validation_artifact,
)


LABEL_HASH = "a" * 64
HUMAN_LABEL_HASH = "b" * 64
LAYER_E_HASH = "c" * 64
LAYER_R_HASH = "d" * 64
EXPECTED_PROMPTS = {"layer_e": LAYER_E_HASH, "layer_r": LAYER_R_HASH}
EXPECTED_CLASSES = ("Fi", "Wj")
POLICY = {
    "human_human_thresholds": {"agreement": 0.85, "weighted_kappa": 0.80},
    "human_by_class_thresholds": {
        "Fi": {"agreement": 0.85},
        "Wj": {"agreement": 0.80},
    },
    "judge_thresholds": {
        "macro_f1": 0.85,
        "auprc": 0.80,
        "worst_class_f1": 0.75,
        "agreement": 0.80,
    },
    "judge_by_class_thresholds": {
        "Fi": {"f1": 0.75, "auprc": 0.75},
        "Wj": {"f1": 0.75, "auprc": 0.75},
    },
    "minimum_calibration_n": 48,
    "maximum_refusal_rate": 0.05,
}
POLICY_HASH = hashlib.sha256(
    json.dumps(POLICY, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()
EVIDENCE_HASH = "e" * 64
EXPECTED_JUDGES = {
    "J01": {
        "model_id": "anthropic/claude-sonnet-4.6",
        "canonical_snapshot": "anthropic/claude-sonnet-4.6-20260618",
        "vendor": "Anthropic",
        "family": "Claude-Sonnet",
    },
    "J02": {
        "model_id": "google/gemini-3-pro",
        "canonical_snapshot": "google/gemini-3-pro-20260601",
        "vendor": "Google",
        "family": "Gemini-Pro",
    },
}


def _judge(
    judge_id: str,
    *,
    model_id: str,
    canonical_snapshot: str,
    vendor: str,
    family: str,
) -> dict:
    return {
        "judge_id": judge_id,
        "model_id": model_id,
        "canonical_snapshot": canonical_snapshot,
        "vendor": vendor,
        "family": family,
        "metrics": {
            "macro_f1": 0.91,
            "auprc": 0.89,
            "worst_class_f1": 0.82,
            "agreement": 0.88,
        },
        "thresholds": {
            "macro_f1": 0.85,
            "auprc": 0.80,
            "worst_class_f1": 0.75,
            "agreement": 0.80,
        },
        "by_class": {
            "Fi": {
                "metrics": {"f1": 0.92, "auprc": 0.90},
                "thresholds": {"f1": 0.75, "auprc": 0.75},
            },
            "Wj": {
                "metrics": {"f1": 0.82, "auprc": 0.84},
                "thresholds": {"f1": 0.75, "auprc": 0.75},
            },
        },
        "calibration_n": 48,
        "refusal_rate": 0.02,
        "max_refusal_rate": 0.05,
    }


def _artifact() -> dict:
    return {
        "schema_version": "1.0",
        "design": "vinedresser",
        "approved_for_live": True,
        "label_set_sha256": LABEL_HASH,
        "human_label_set_sha256": HUMAN_LABEL_HASH,
        "calibration_evidence_sha256": EVIDENCE_HASH,
        "prompt_hashes": dict(EXPECTED_PROMPTS),
        "policy": json.loads(json.dumps(POLICY)),
        "human_human": {
            "metrics": {"agreement": 0.91, "weighted_kappa": 0.84},
            "thresholds": {"agreement": 0.85, "weighted_kappa": 0.80},
            "by_class": {
                "Fi": {
                    "metrics": {"agreement": 0.94},
                    "thresholds": {"agreement": 0.85},
                },
                "Wj": {
                    "metrics": {"agreement": 0.88},
                    "thresholds": {"agreement": 0.80},
                },
            },
        },
        "judges": [
            _judge(
                "J01",
                model_id="anthropic/claude-sonnet-4.6",
                canonical_snapshot="anthropic/claude-sonnet-4.6-20260618",
                vendor="Anthropic",
                family="Claude-Sonnet",
            ),
            _judge(
                "J02",
                model_id="google/gemini-3-pro",
                canonical_snapshot="google/gemini-3-pro-20260601",
                vendor="Google",
                family="Gemini-Pro",
            ),
        ],
        "human_availability": {
            "available_for_live": True,
            "verified": True,
            "declaration": "Two trained human adjudicators are available for live review.",
        },
        "completed_at": "2026-07-09T18:30:00Z",
    }


def _validate(source):
    return validate_judge_validation_artifact(
        source,
        expected_design="vinedresser",
        expected_label_set_sha256=LABEL_HASH,
        expected_human_label_set_sha256=HUMAN_LABEL_HASH,
        expected_prompt_hashes=EXPECTED_PROMPTS,
        expected_judge_identities=EXPECTED_JUDGES,
        expected_class_labels=EXPECTED_CLASSES,
        expected_policy_sha256=POLICY_HASH,
    )


def _json_bytes(value: dict) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def test_valid_artifact_returns_exact_digest_and_deeply_immutable_record(tmp_path: Path) -> None:
    raw = _json_bytes(_artifact())
    path = tmp_path / "judge-validation.json"
    path.write_bytes(raw)

    validated = _validate(path)

    assert validated.artifact_sha256 == hashlib.sha256(raw).hexdigest()
    assert validated.record["design"] == "vinedresser"
    assert validated.record["judges"][0]["judge_id"] == "J01"
    with pytest.raises(TypeError):
        validated.record["design"] = "changed"
    with pytest.raises(TypeError):
        validated.record["judges"][0]["metrics"]["macro_f1"] = 0.0
    with pytest.raises(FrozenInstanceError):
        validated.artifact_sha256 = "0" * 64


def test_validated_record_cannot_be_forged_by_direct_dataclass_construction() -> None:
    with pytest.raises(TypeError, match="validator"):
        ValidatedJudgeValidation(
            record={"approved_for_live": True},
            artifact_sha256="a" * 64,
        )


@pytest.mark.parametrize(
    "field",
    [
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
    ],
)
def test_rejects_every_missing_required_top_level_field(field: str) -> None:
    artifact = _artifact()
    artifact.pop(field)

    with pytest.raises(JudgeValidationError, match=field):
        _validate(artifact)


def test_rejects_false_live_approval_and_unsupported_schema() -> None:
    artifact = _artifact()
    artifact["approved_for_live"] = False
    with pytest.raises(JudgeValidationError, match="approved_for_live"):
        _validate(artifact)

    artifact = _artifact()
    artifact["schema_version"] = "2.0"
    with pytest.raises(JudgeValidationError, match="schema_version"):
        _validate(artifact)


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda value: value.update(label_set_sha256="short"), "label_set_sha256"),
        (
            lambda value: value.update(human_label_set_sha256="z" * 64),
            "human_label_set_sha256",
        ),
        (
            lambda value: value["prompt_hashes"].update(layer_e="e" * 64),
            "prompt_hashes.layer_e",
        ),
        (
            lambda value: value.update(prompt_hashes={"layer_e": LAYER_E_HASH}),
            "prompt_hashes",
        ),
    ],
)
def test_rejects_malformed_stale_or_mismatched_hashes(mutation, message: str) -> None:
    artifact = _artifact()
    mutation(artifact)

    with pytest.raises(JudgeValidationError, match=message):
        _validate(artifact)


def test_thresholds_sample_size_and_refusal_ceiling_are_policy_bound() -> None:
    artifact = _artifact()
    artifact["judges"][0]["thresholds"]["macro_f1"] = 0.0
    with pytest.raises(JudgeValidationError, match="policy.*threshold"):
        _validate(artifact)

    artifact = _artifact()
    artifact["judges"][0]["calibration_n"] = 1
    with pytest.raises(JudgeValidationError, match="minimum_calibration_n"):
        _validate(artifact)

    artifact = _artifact()
    artifact["judges"][0]["max_refusal_rate"] = 1.0
    with pytest.raises(JudgeValidationError, match="maximum_refusal_rate"):
        _validate(artifact)

    artifact = _artifact()
    artifact["policy"]["minimum_calibration_n"] = 1
    with pytest.raises(JudgeValidationError, match="policy.*hash"):
        _validate(artifact)


@pytest.mark.parametrize(
    "metric", ["macro_f1", "auprc", "worst_class_f1", "agreement"]
)
def test_rejects_missing_judge_metric_or_threshold(metric: str) -> None:
    artifact = _artifact()
    artifact["judges"][0]["metrics"].pop(metric)
    with pytest.raises(JudgeValidationError, match=metric):
        _validate(artifact)

    artifact = _artifact()
    artifact["judges"][0]["thresholds"].pop(metric)
    with pytest.raises(JudgeValidationError, match=metric):
        _validate(artifact)


def test_requires_per_class_human_and_judge_metrics() -> None:
    artifact = _artifact()
    artifact["judges"][0].pop("by_class")
    with pytest.raises(JudgeValidationError, match="by_class"):
        _validate(artifact)

    artifact = _artifact()
    artifact["human_human"].pop("by_class")
    with pytest.raises(JudgeValidationError, match="human_human.*by_class"):
        _validate(artifact)

    artifact = _artifact()
    artifact["judges"][0]["by_class"]["Wj"]["metrics"]["auprc"] = 0.70
    with pytest.raises(JudgeValidationError, match="by_class.*below threshold"):
        _validate(artifact)


def test_worst_class_f1_must_equal_observed_class_minimum() -> None:
    artifact = _artifact()
    artifact["judges"][0]["metrics"]["worst_class_f1"] = 0.90

    with pytest.raises(JudgeValidationError, match="worst_class_f1.*minimum"):
        _validate(artifact)


def test_judge_snapshot_and_identity_are_bound_to_expected_catalog_values() -> None:
    artifact = _artifact()
    artifact["judges"][0]["canonical_snapshot"] = "anthropic/claude-sonnet-4.6"

    with pytest.raises(JudgeValidationError, match="canonical_snapshot.*expected"):
        _validate(artifact)

    incomplete_expected = {"J01": EXPECTED_JUDGES["J01"]}
    with pytest.raises(JudgeValidationError, match="expected_judge_identities"):
        validate_judge_validation_artifact(
            _artifact(),
            expected_design="vinedresser",
            expected_label_set_sha256=LABEL_HASH,
            expected_human_label_set_sha256=HUMAN_LABEL_HASH,
            expected_prompt_hashes=EXPECTED_PROMPTS,
            expected_judge_identities=incomplete_expected,
            expected_class_labels=EXPECTED_CLASSES,
            expected_policy_sha256=POLICY_HASH,
        )


def test_per_class_coverage_is_bound_to_expected_label_set() -> None:
    artifact = _artifact()
    artifact["human_human"]["by_class"].pop("Wj")
    for judge in artifact["judges"]:
        judge["by_class"].pop("Wj")
        judge["metrics"]["worst_class_f1"] = 0.92

    with pytest.raises(JudgeValidationError, match="expected_class_labels"):
        _validate(artifact)

def test_rejects_unmet_judge_or_human_thresholds() -> None:
    artifact = _artifact()
    artifact["judges"][0]["metrics"]["macro_f1"] = 0.84
    with pytest.raises(JudgeValidationError, match="below threshold"):
        _validate(artifact)

    artifact = _artifact()
    artifact["human_human"]["metrics"]["agreement"] = 0.84
    with pytest.raises(JudgeValidationError, match="human_human.*below threshold"):
        _validate(artifact)


def test_human_human_block_must_include_declared_agreement() -> None:
    artifact = _artifact()
    artifact["human_human"]["metrics"].pop("agreement")
    artifact["human_human"]["thresholds"].pop("agreement")

    with pytest.raises(JudgeValidationError, match="human_human.*agreement"):
        _validate(artifact)


@pytest.mark.parametrize("bad_value", [True, float("nan"), float("inf")])
def test_rejects_boolean_nan_or_infinite_metrics(bad_value) -> None:
    artifact = _artifact()
    artifact["judges"][0]["metrics"]["agreement"] = bad_value

    with pytest.raises(JudgeValidationError, match="finite numeric"):
        _validate(artifact)


def test_rejects_nonstandard_nan_json_constant() -> None:
    raw = _json_bytes(_artifact()).replace(b'"agreement":0.88', b'"agreement":NaN', 1)

    with pytest.raises(JudgeValidationError, match="non-standard numeric constant"):
        _validate(raw)


@pytest.mark.parametrize("calibration_n", [0, -1, True, 2.5])
def test_rejects_nonpositive_or_noninteger_calibration_n(calibration_n) -> None:
    artifact = _artifact()
    artifact["judges"][0]["calibration_n"] = calibration_n

    with pytest.raises(JudgeValidationError, match="calibration_n"):
        _validate(artifact)


@pytest.mark.parametrize(
    ("refusal_rate", "maximum"),
    [(-0.01, 0.05), (1.01, 1.0), (0.06, 0.05), (True, 0.05), (0.01, False)],
)
def test_rejects_invalid_or_excessive_refusal_rate(refusal_rate, maximum) -> None:
    artifact = _artifact()
    artifact["judges"][0]["refusal_rate"] = refusal_rate
    artifact["judges"][0]["max_refusal_rate"] = maximum

    with pytest.raises(JudgeValidationError, match="refusal"):
        _validate(artifact)


def test_requires_two_judges_with_opaque_ids_and_non_openai_identity() -> None:
    artifact = _artifact()
    artifact["judges"] = artifact["judges"][:1]
    with pytest.raises(JudgeValidationError, match="at least two"):
        _validate(artifact)

    artifact = _artifact()
    artifact["judges"][0]["judge_id"] = "claude-judge"
    with pytest.raises(JudgeValidationError, match="opaque J##"):
        _validate(artifact)

    artifact = _artifact()
    artifact["judges"][0]["vendor"] = "OpenAI"
    artifact["judges"][0]["model_id"] = "openai/gpt-5.5"
    artifact["judges"][0]["canonical_snapshot"] = "openai/gpt-5.5-20260601"
    with pytest.raises(JudgeValidationError, match="non-OpenAI"):
        _validate(artifact)


@pytest.mark.parametrize(
    "field",
    ["judge_id", "model_id", "canonical_snapshot", "vendor", "family"],
)
def test_rejects_overlapping_judge_identity(field: str) -> None:
    artifact = _artifact()
    artifact["judges"][1][field] = artifact["judges"][0][field]

    with pytest.raises(JudgeValidationError, match="overlapping.*" + field):
        _validate(artifact)


def test_rejects_missing_or_unverified_human_availability() -> None:
    artifact = _artifact()
    artifact["human_availability"]["verified"] = False
    with pytest.raises(JudgeValidationError, match="human_availability.*verified"):
        _validate(artifact)

    artifact = _artifact()
    artifact["human_availability"]["available_for_live"] = False
    with pytest.raises(JudgeValidationError, match="human_availability.*available_for_live"):
        _validate(artifact)

    artifact = _artifact()
    artifact["human_availability"]["declaration"] = "   "
    with pytest.raises(JudgeValidationError, match="human_availability.*declaration"):
        _validate(artifact)


@pytest.mark.parametrize(
    "completed_at",
    [
        "2026-07-09T18:30:00",
        "2026-07-09T18:30:00+00:00",
        "2026-07-09",
        "not-a-timestamp",
    ],
)
def test_requires_completed_at_to_be_an_explicit_utc_z_timestamp(completed_at: str) -> None:
    artifact = _artifact()
    artifact["completed_at"] = completed_at

    with pytest.raises(JudgeValidationError, match="completed_at"):
        _validate(artifact)


def test_rejects_duplicate_json_keys_instead_of_accepting_last_value() -> None:
    raw = _json_bytes(_artifact())
    raw = raw.replace(b'{"approved_for_live":true,', b'{"approved_for_live":true,"approved_for_live":false,', 1)

    with pytest.raises(JudgeValidationError, match="duplicate JSON key"):
        _validate(raw)
