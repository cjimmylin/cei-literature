from __future__ import annotations

import sys
import hashlib
import json
from pathlib import Path

import pytest


HARNESS = Path(__file__).resolve().parents[2]
if str(HARNESS) not in sys.path:
    sys.path.insert(0, str(HARNESS))

from shared.judge_evidence import (  # noqa: E402
    ComputedJudgeEvidence,
    compute_judge_evidence,
)
from shared.judge_validation import (  # noqa: E402
    JudgeValidationError,
    validate_judge_validation_artifact,
)


CLASSES = ("Fi", "Wj", "CFT", "mixed", "other")
PROMPTS = {"layer_e": "c" * 64, "layer_r": "d" * 64}
LABEL_HASH = "a" * 64
JUDGES = {
    "J01": {
        "model_id": "anthropic/claude-sonnet-5",
        "canonical_snapshot": "anthropic/claude-sonnet-5-20260601",
        "vendor": "Anthropic",
        "family": "Claude-Sonnet",
    },
    "J02": {
        "model_id": "google/gemini-3.5-flash",
        "canonical_snapshot": "google/gemini-3.5-flash-20260615",
        "vendor": "Google",
        "family": "Gemini-Flash",
    },
}


def _human():
    rows = []
    resolved = {}
    for index in range(50):
        response_id = f"R{index:03d}"
        label = CLASSES[index % len(CLASSES)]
        resolved[response_id] = label
        for rater_hash in ("1" * 64, "2" * 64):
            rows.append(
                {
                    "response_id": response_id,
                    "rater_hash": rater_hash,
                    "role": "primary",
                    "final_label": label,
                    "notes": "",
                }
            )
    return {
        "schema_version": "1.0",
        "source_sha256": "b" * 64,
        "rows": rows,
        "resolved_labels": resolved,
        "coverage": {
            "expected_responses": 50,
            "double_coded_responses": 50,
            "adjudicated_disagreements": 0,
        },
    }


def _predictions():
    rows = []
    for response_id, label in _human()["resolved_labels"].items():
        for judge_id, identity in JUDGES.items():
            rows.append(
                {
                    "response_id": response_id,
                    "judge_id": judge_id,
                    "judge_model_id": identity["model_id"],
                    "judge_snapshot": identity["canonical_snapshot"],
                    "judge_vendor": identity["vendor"],
                    "judge_family": identity["family"],
                    "final_label": label,
                    "class_probabilities": {
                        candidate: 0.8 if candidate == label else 0.05
                        for candidate in CLASSES
                    },
                    "judge_refused": False,
                }
            )
    return {
        "schema_version": "1.0",
        "label_set_sha256": LABEL_HASH,
        "prompt_hashes": PROMPTS,
        "rows": rows,
    }


def _compute(human=None, predictions=None):
    return compute_judge_evidence(
        human or _human(),
        predictions or _predictions(),
        expected_judge_identities=JUDGES,
        expected_class_labels=CLASSES,
        expected_label_set_sha256=LABEL_HASH,
        expected_prompt_hashes=PROMPTS,
    )


def test_recomputes_every_reported_metric_from_complete_raw_rows():
    result = _compute()

    assert len(result.evidence_sha256) == 64
    assert result.human_human["metrics"] == {
        "agreement": 1.0,
        "weighted_kappa": 1.0,
    }
    assert set(result.human_human["by_class"]) == set(CLASSES)
    assert all(
        block["metrics"] == {"agreement": 1.0}
        for block in result.human_human["by_class"].values()
    )
    assert {judge["judge_id"] for judge in result.judges} == {"J01", "J02"}
    for judge in result.judges:
        assert judge["calibration_n"] == 50
        assert judge["refusal_rate"] == 0.0
        assert judge["metrics"] == {
            "macro_f1": 1.0,
            "auprc": 1.0,
            "worst_class_f1": 1.0,
            "agreement": 1.0,
        }
        assert all(
            block["metrics"] == {"f1": 1.0, "auprc": 1.0}
            for block in judge["by_class"].values()
        )


def test_rejects_missing_rows_identity_drift_and_probability_errors():
    missing = _predictions()
    missing["rows"].pop()
    with pytest.raises(ValueError, match="coverage"):
        _compute(predictions=missing)

    drift = _predictions()
    drift["rows"][0]["judge_vendor"] = "OpenAI"
    with pytest.raises(ValueError, match="identity"):
        _compute(predictions=drift)

    bad_probability = _predictions()
    bad_probability["rows"][0]["class_probabilities"]["Fi"] = 0.7
    with pytest.raises(ValueError, match="sum"):
        _compute(predictions=bad_probability)


def test_rejects_incomplete_human_double_coding_and_class_coverage():
    human = _human()
    human["rows"].pop()
    with pytest.raises(ValueError, match="two primary"):
        _compute(human=human)

    human = _human()
    human["resolved_labels"] = {
        response_id: "Fi" for response_id in human["resolved_labels"]
    }
    for row in human["rows"]:
        row["final_label"] = "Fi"
    predictions = _predictions()
    for row in predictions["rows"]:
        row["final_label"] = "Fi"
        row["class_probabilities"] = {
            label: 0.8 if label == "Fi" else 0.05 for label in CLASSES
        }
    with pytest.raises(ValueError, match="class coverage"):
        _compute(human=human, predictions=predictions)


def test_computed_evidence_cannot_be_forged_directly():
    with pytest.raises(TypeError, match="compute_judge_evidence"):
        ComputedJudgeEvidence(
            human_human={},
            judges=(),
            evidence_sha256="a" * 64,
        )


def _validation_artifact(computed):
    policy = {
        "human_human_thresholds": {"agreement": 0.0, "weighted_kappa": 0.0},
        "human_by_class_thresholds": {
            label: {"agreement": 0.0} for label in CLASSES
        },
        "judge_thresholds": {
            "macro_f1": 0.0,
            "auprc": 0.0,
            "worst_class_f1": 0.0,
            "agreement": 0.0,
        },
        "judge_by_class_thresholds": {
            label: {"f1": 0.0, "auprc": 0.0} for label in CLASSES
        },
        "minimum_calibration_n": 1,
        "maximum_refusal_rate": 1.0,
    }
    human = {
        "metrics": dict(computed.human_human["metrics"]),
        "thresholds": dict(policy["human_human_thresholds"]),
        "by_class": {
            label: {
                "metrics": dict(computed.human_human["by_class"][label]["metrics"]),
                "thresholds": dict(policy["human_by_class_thresholds"][label]),
            }
            for label in CLASSES
        },
    }
    judges = []
    computed_by_id = {row["judge_id"]: row for row in computed.judges}
    for judge_id, identity in JUDGES.items():
        row = computed_by_id[judge_id]
        judges.append(
            {
                "judge_id": judge_id,
                **identity,
                "metrics": dict(row["metrics"]),
                "thresholds": dict(policy["judge_thresholds"]),
                "by_class": {
                    label: {
                        "metrics": dict(row["by_class"][label]["metrics"]),
                        "thresholds": dict(policy["judge_by_class_thresholds"][label]),
                    }
                    for label in CLASSES
                },
                "calibration_n": row["calibration_n"],
                "refusal_rate": row["refusal_rate"],
                "max_refusal_rate": 1.0,
            }
        )
    return {
        "schema_version": "1.0",
        "design": "thorns",
        "approved_for_live": True,
        "label_set_sha256": LABEL_HASH,
        "human_label_set_sha256": "b" * 64,
        "calibration_evidence_sha256": computed.evidence_sha256,
        "prompt_hashes": PROMPTS,
        "policy": policy,
        "human_human": human,
        "judges": judges,
        "human_availability": {
            "available_for_live": True,
            "verified": True,
            "declaration": "Two trained humans are available for live adjudication.",
        },
        "completed_at": "2026-07-09T20:00:00Z",
    }


def _validate_artifact(artifact, computed):
    policy_hash = hashlib.sha256(
        json.dumps(
            artifact["policy"], sort_keys=True, separators=(",", ":")
        ).encode()
    ).hexdigest()
    return validate_judge_validation_artifact(
        artifact,
        expected_design="thorns",
        expected_label_set_sha256=LABEL_HASH,
        expected_human_label_set_sha256="b" * 64,
        expected_prompt_hashes=PROMPTS,
        expected_judge_identities=JUDGES,
        expected_class_labels=CLASSES,
        expected_policy_sha256=policy_hash,
        computed_evidence=computed,
    )


def test_live_attestation_requires_metrics_equal_recomputed_evidence():
    computed = _compute()
    artifact = _validation_artifact(computed)
    validated = _validate_artifact(artifact, computed)
    assert validated.evidence_verified is True
    assert validated.calibration_evidence_sha256 == computed.evidence_sha256

    artifact["judges"][0]["metrics"]["macro_f1"] = 0.99
    with pytest.raises(JudgeValidationError, match="recomputed"):
        _validate_artifact(artifact, computed)
