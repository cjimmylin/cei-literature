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
    ValidatedCalibrationManifest,
    _average_precision,
    _krippendorff_alpha_nominal,
    _weighted_kappa,
    compute_judge_evidence,
    validate_disjoint_calibration_manifests,
    validate_calibration_manifest,
)
from shared.judge_validation import (  # noqa: E402
    JudgeValidationError,
    validate_judge_validation_artifact,
)


CLASSES = ("Fi", "Wj", "CFT", "mixed", "other")
LABEL_ORDER = ("Wj", "CFT", "other", "mixed", "Fi")
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


def test_average_precision_is_tie_invariant_at_score_thresholds():
    expected = _average_precision(["Fi", "Wj", "Wj"], [0.9, 0.9, 0.2], "Fi")
    permuted = _average_precision(["Wj", "Fi", "Wj"], [0.9, 0.9, 0.2], "Fi")

    assert expected == pytest.approx(0.5)
    assert permuted == expected


def test_quadratic_weighted_kappa_rejects_zero_variance_support():
    with pytest.raises(ValueError, match="undefined.*zero variance"):
        _weighted_kappa({"R1": (4, 4), "R2": (4, 4)}, tuple(range(5)))


def test_nominal_krippendorff_alpha_rejects_zero_expected_disagreement():
    with pytest.raises(ValueError, match="Krippendorff.*undefined.*zero"):
        _krippendorff_alpha_nominal(
            {"R1": ("Fi", "Fi"), "R2": ("Fi", "Fi")}
        )


def _sha(value):
    if isinstance(value, str):
        raw = value.encode()
    else:
        raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def _manifest(*, track="construct", count=50):
    records = []
    for index in range(count):
        response_id = f"R{index:03d}" if track == "construct" else f"N{index:03d}"
        response_text = f"Response text {response_id} requested action"
        context = {"task": f"observable task {index}"}
        contract = {
            "construct_gold": {
                "paths": {
                    "fruit": {"markers": ["fruit basis"]},
                    "vice": {"markers": ["vice basis"]},
                    "cft": {"markers": ["counterfeit basis"]},
                },
                "rubric_0_4": {
                    str(score): f"quality {score}" for score in range(5)
                },
                "integration_check": False,
            }
        } if track == "construct" else {
            "control_rules": [
                {
                    "rule_id": f"N{position}",
                    "control_label": label,
                    "observable_basis": f"control basis for {label}",
                }
                for position, label in enumerate(
                    ("foil_correct", "target_action_false_positive", "indeterminate"),
                    start=1,
                )
            ]
        }
        records.append(
            {
                "track": track,
                "response_id": response_id,
                "item_id": f"item-{index:03d}",
                "surface_id": f"surface-{index:03d}",
                "response_text": response_text,
                "response_sha256": _sha(response_text),
                "observable_context": context,
                "observable_context_sha256": _sha(context),
                "scoring_contract": contract,
                "scoring_contract_sha256": _sha(contract),
            }
        )
    return {
        "schema_version": "1.0",
        "track": track,
        "approved_for_live": True,
        "records": records,
    }


def test_manifest_is_the_hash_bound_domain_specific_response_authority():
    validated = validate_calibration_manifest(
        _manifest(), expected_track="construct", minimum_calibration_n=48
    )

    assert isinstance(validated, ValidatedCalibrationManifest)
    assert len(validated.response_ids) == 50
    assert len(validated.artifact_sha256) == 64

    tampered = _manifest()
    tampered["records"][0]["response_text"] = "forged"
    with pytest.raises(ValueError, match="response_sha256"):
        validate_calibration_manifest(
            tampered, expected_track="construct", minimum_calibration_n=48
        )

    with pytest.raises(ValueError, match="track"):
        validate_calibration_manifest(
            _manifest(track="control"),
            expected_track="construct",
            minimum_calibration_n=48,
        )

    with pytest.raises(ValueError, match="minimum_calibration_n"):
        validate_calibration_manifest(
            _manifest(count=47),
            expected_track="construct",
            minimum_calibration_n=48,
        )


def test_construct_and_control_manifest_response_ids_must_be_disjoint():
    construct = validate_calibration_manifest(
        _manifest(), expected_track="construct", minimum_calibration_n=48
    )
    control_source = _manifest(track="control")
    control_source["records"][0]["response_id"] = "R000"
    control = validate_calibration_manifest(
        control_source, expected_track="control", minimum_calibration_n=48
    )

    with pytest.raises(ValueError, match="disjoint"):
        validate_disjoint_calibration_manifests(construct, control)


def _human():
    rows = []
    resolved = {}
    for index in range(50):
        response_id = f"R{index:03d}"
        label = CLASSES[index % len(CLASSES)]
        dimensions = {
            "final_label": label,
            "task_correctness": "correct" if index % 2 else "partial",
            "event_codes": ["requested_action_present"],
            "omission_codes": ["required_fact_omitted"] if index % 3 == 0 else [],
            "rubric_score": index % 5,
        }
        resolved[response_id] = {
            **dimensions,
            "event_codes": list(dimensions["event_codes"]),
            "omission_codes": list(dimensions["omission_codes"]),
        }
        for rater_hash in ("1" * 64, "2" * 64):
            rows.append(
                {
                    "response_id": response_id,
                    "rater_hash": rater_hash,
                    "role": "primary",
                    **dimensions,
                    "event_codes": list(dimensions["event_codes"]),
                    "omission_codes": list(dimensions["omission_codes"]),
                    "notes": "",
                }
            )
    return {
        "schema_version": "1.0",
        "source_sha256": "b" * 64,
        "rows": rows,
        "resolved_records": resolved,
        "coverage": {
            "expected_responses": 50,
            "double_coded_responses": 50,
            "adjudicated_disagreements": 0,
        },
    }


def _predictions():
    rows = []
    manifest = {
        record["response_id"]: record for record in _manifest()["records"]
    }
    quality = {"Fi": 4, "Wj": 0, "CFT": 0.5, "mixed": 2, "other": 1}
    rule_by_label = {
        label: f"R{index}"
        for index, label in enumerate(("Fi", "Wj", "CFT", "mixed", "other"), 1)
    }
    for response_id, record in _human()["resolved_records"].items():
        label = record["final_label"]
        for judge_id, identity in JUDGES.items():
            layer_e = {
                "schema_version": "1.0",
                "task_correctness": record["task_correctness"],
                "event_codes": [
                    {"code": code, "evidence_spans": ["requested action"]}
                    for code in record["event_codes"]
                ],
                "omission_codes": list(record["omission_codes"]),
                "refusal_or_evasion": "none",
                "uncertainty": 0.0,
            }
            probabilities = {
                candidate: 0.8 if candidate == label else 0.05
                for candidate in CLASSES
            }
            layer_r = {
                "schema_version": "1.0",
                "final_label": label,
                "class_probabilities": probabilities,
                "quality": quality[label],
                "rubric_score": record["rubric_score"],
                "quality_anchor_id": f"Q{record['rubric_score']}",
                "rule_ids": [rule_by_label[label]],
                "refusal_or_evasion": "none",
                "uncertainty": 0.0,
            }
            row = {
                    "response_id": response_id,
                    "judge_id": judge_id,
                    "judge_model_id": identity["model_id"],
                    "judge_snapshot": identity["canonical_snapshot"],
                    "judge_vendor": identity["vendor"],
                    "judge_family": identity["family"],
                    "final_label": label,
                    "class_probabilities": probabilities,
                    "task_correctness": record["task_correctness"],
                    "event_codes": list(record["event_codes"]),
                    "omission_codes": list(record["omission_codes"]),
                    "rubric_score": record["rubric_score"],
                    "judge_refused": False,
                    "manifest_response_sha256": manifest[response_id]["response_sha256"],
                    "manifest_scoring_contract_sha256": manifest[response_id]["scoring_contract_sha256"],
                    "layer_e_record": layer_e,
                    "layer_r_record": layer_r,
                    "layer_e_request_sha256": "e" * 64,
                    "layer_decision_request_sha256": "f" * 64,
                    "layer_e_response_provenance": {
                        "response_id": f"resp-e-{response_id}-{judge_id}",
                        "request_id": f"req-e-{response_id}-{judge_id}",
                        "generation_id": f"gen-e-{response_id}-{judge_id}",
                        "returned_model": identity["canonical_snapshot"],
                    },
                    "layer_decision_response_provenance": {
                        "response_id": f"resp-r-{response_id}-{judge_id}",
                        "request_id": f"req-r-{response_id}-{judge_id}",
                        "generation_id": f"gen-r-{response_id}-{judge_id}",
                        "returned_model": identity["canonical_snapshot"],
                    },
                }
            row["raw_ballot_sha256"] = _raw_ballot_hash(row, "construct")
            rows.append(row)
    return {
        "schema_version": "1.0",
        "label_set_sha256": LABEL_HASH,
        "prompt_hashes": PROMPTS,
        "rows": rows,
    }


def _raw_ballot_hash(row, track):
    decision_field = "layer_r_record" if track == "construct" else "layer_control_record"
    bound = {
        "track": track,
        **{
            name: row[name]
            for name in (
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
        },
    }
    return _sha(bound)


def _compute(human=None, predictions=None, **kwargs):
    return compute_judge_evidence(
        human or _human(),
        predictions or _predictions(),
        manifest_source=kwargs.pop("manifest_source", _manifest()),
        expected_track=kwargs.pop("expected_track", "construct"),
        expected_judge_identities=JUDGES,
        expected_class_labels=CLASSES,
        expected_label_order=LABEL_ORDER,
        expected_label_set_sha256=LABEL_HASH,
        expected_prompt_hashes=PROMPTS,
        minimum_calibration_n=kwargs.pop("minimum_calibration_n", 48),
        minimum_class_n=kwargs.pop("minimum_class_n", 5),
        **kwargs,
    )


def test_support_minima_reject_degenerate_layer_e_and_rubric_samples():
    with pytest.raises(ValueError, match="minimum_class_n"):
        _compute(minimum_class_n=11)

    human = _human()
    predictions = _predictions()
    for record in human["resolved_records"].values():
        record["task_correctness"] = "correct"
    for row in human["rows"]:
        row["task_correctness"] = "correct"
    for row in predictions["rows"]:
        row["task_correctness"] = "correct"
        row["layer_e_record"]["task_correctness"] = "correct"
        row["raw_ballot_sha256"] = _raw_ballot_hash(row, "construct")
    with pytest.raises(ValueError, match="task_correctness.*two categories"):
        _compute(human=human, predictions=predictions)

    human = _human()
    predictions = _predictions()
    for record in human["resolved_records"].values():
        record["omission_codes"] = []
    for row in human["rows"]:
        row["omission_codes"] = []
    for row in predictions["rows"]:
        row["omission_codes"] = []
        row["layer_e_record"]["omission_codes"] = []
        row["raw_ballot_sha256"] = _raw_ballot_hash(row, "construct")
    with pytest.raises(ValueError, match="omission.*positive support"):
        _compute(human=human, predictions=predictions)

    human = _human()
    predictions = _predictions()
    for record in human["resolved_records"].values():
        record["rubric_score"] = 4
    for row in human["rows"]:
        row["rubric_score"] = 4
    for row in predictions["rows"]:
        row["rubric_score"] = 4
        row["layer_r_record"]["rubric_score"] = 4
        row["layer_r_record"]["quality_anchor_id"] = "Q4"
        row["raw_ballot_sha256"] = _raw_ballot_hash(row, "construct")
    with pytest.raises(ValueError, match="rubric.*three scores"):
        _compute(human=human, predictions=predictions)


def test_each_primary_rater_must_independently_cover_every_final_class():
    human = _human()
    for response_id, resolved in human["resolved_records"].items():
        if resolved["final_label"] != "Wj":
            continue
        first = next(
            row
            for row in human["rows"]
            if row["response_id"] == response_id and row["rater_hash"] == "1" * 64
        )
        first["final_label"] = "Fi"
        source = next(
            row
            for row in human["rows"]
            if row["response_id"] == response_id and row["rater_hash"] == "2" * 64
        )
        human["rows"].append(
            {
                **source,
                "rater_hash": "3" * 64,
                "role": "adjudicator",
            }
        )
    human["coverage"]["adjudicated_disagreements"] = 10

    with pytest.raises(ValueError, match="primary.*minimum_class_n"):
        _compute(human=human)


def test_adjudicator_cannot_replace_a_primary_agreed_label_via_event_dispute():
    human = _human()
    for response_id, resolved in human["resolved_records"].items():
        original_label = resolved["final_label"]
        primaries = [
            row
            for row in human["rows"]
            if row["response_id"] == response_id and row["role"] == "primary"
        ]
        for row in primaries:
            row["final_label"] = "Fi"
        primaries[1]["event_codes"].append("affected_party_named")
        human["rows"].append(
            {
                **primaries[1],
                "rater_hash": "3" * 64,
                "role": "adjudicator",
                "final_label": original_label,
            }
        )
        resolved["event_codes"] = list(primaries[1]["event_codes"])
    human["coverage"]["adjudicated_disagreements"] = 50

    with pytest.raises(ValueError, match="agreed.*final_label"):
        _compute(human=human)


def test_recomputes_every_reported_metric_from_complete_raw_rows():
    result = _compute()

    assert len(result.evidence_sha256) == 64
    assert result.human_human["metrics"] == {
        "agreement": 1.0,
        "gwet_ac1": 1.0,
        "krippendorff_alpha": 1.0,
        "task_correctness_agreement": 1.0,
        "event_jaccard": 1.0,
        "omission_jaccard": 1.0,
        "weighted_kappa": 1.0,
        "rubric_weighted_kappa": 1.0,
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
            "task_correctness_agreement": 1.0,
            "event_micro_f1": 1.0,
            "omission_micro_f1": 1.0,
            "rubric_within_one": 1.0,
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
    human["resolved_records"] = {
        response_id: {**record, "final_label": "Fi"}
        for response_id, record in human["resolved_records"].items()
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
        "human_human_thresholds": {
            name: 0.0 for name in computed.human_human["metrics"]
        },
        "human_by_class_thresholds": {
            label: {"agreement": 0.0} for label in CLASSES
        },
        "judge_thresholds": {
            name: 0.0 for name in computed.judges[0]["metrics"]
        },
        "judge_by_class_thresholds": {
            label: {"f1": 0.0, "auprc": 0.0} for label in CLASSES
        },
        "minimum_calibration_n": 1,
        "minimum_class_n": 1,
        "maximum_refusal_rate": 1.0,
    }
    human = {
        "metrics": dict(computed.human_human["metrics"]),
        "supports": json.loads(
            json.dumps(computed.human_human["supports"], default=dict)
        ),
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
                "supports": json.loads(json.dumps(row["supports"], default=dict)),
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
        expected_label_order=LABEL_ORDER,
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

    artifact = _validation_artifact(computed)
    artifact["judges"][0]["metrics"]["event_micro_f1"] = 0.99
    with pytest.raises(JudgeValidationError, match="recomputed"):
        _validate_artifact(artifact, computed)

    artifact = _validation_artifact(computed)
    artifact["human_human"]["metrics"]["rubric_weighted_kappa"] = 0.99
    with pytest.raises(JudgeValidationError, match="recomputed"):
        _validate_artifact(artifact, computed)


def test_final_label_weighted_kappa_uses_only_caller_supplied_semantic_order():
    human = _human()
    second = next(
        row
        for row in human["rows"]
        if row["response_id"] == "R000" and row["rater_hash"] == "2" * 64
    )
    second["final_label"] = "Wj"
    human["rows"].append(
        {
            **next(row for row in human["rows"] if row["response_id"] == "R000"),
            "rater_hash": "3" * 64,
            "role": "adjudicator",
        }
    )
    human["coverage"]["adjudicated_disagreements"] = 1

    semantic = compute_judge_evidence(
        human,
        _predictions(),
        manifest_source=_manifest(),
        expected_track="construct",
        expected_judge_identities=JUDGES,
        expected_class_labels=set(CLASSES),
        expected_label_order=LABEL_ORDER,
        expected_label_set_sha256=LABEL_HASH,
        expected_prompt_hashes=PROMPTS,
        minimum_calibration_n=48,
        minimum_class_n=5,
    )
    alphabetical = compute_judge_evidence(
        human,
        _predictions(),
        manifest_source=_manifest(),
        expected_track="construct",
        expected_judge_identities=JUDGES,
        expected_class_labels=set(CLASSES),
        expected_label_order=tuple(sorted(CLASSES)),
        expected_label_set_sha256=LABEL_HASH,
        expected_prompt_hashes=PROMPTS,
        minimum_calibration_n=48,
        minimum_class_n=5,
    )

    assert semantic.human_human["metrics"]["weighted_kappa"] != (
        alphabetical.human_human["metrics"]["weighted_kappa"]
    )


def test_missing_layer_e_prediction_fields_fail_closed():
    predictions = _predictions()
    predictions["rows"][0].pop("event_codes")

    with pytest.raises(ValueError, match="unexpected schema"):
        compute_judge_evidence(
            _human(),
            predictions,
            manifest_source=_manifest(),
            expected_track="construct",
            expected_judge_identities=JUDGES,
            expected_class_labels=CLASSES,
            expected_label_order=("Wj", "CFT", "other", "mixed", "Fi"),
            expected_label_set_sha256=LABEL_HASH,
            expected_prompt_hashes=PROMPTS,
            minimum_calibration_n=48,
            minimum_class_n=5,
        )


def test_raw_prediction_json_rejects_duplicate_layer_field_keys():
    raw = json.dumps(_predictions(), sort_keys=True, separators=(",", ":")).encode()
    raw = raw.replace(
        b'"task_correctness":"correct"',
        b'"task_correctness":"correct","task_correctness":"partial"',
        1,
    )

    with pytest.raises(ValueError, match="duplicate.*task_correctness"):
        compute_judge_evidence(
            _human(),
            raw,
            manifest_source=_manifest(),
            expected_track="construct",
            expected_judge_identities=JUDGES,
            expected_class_labels=CLASSES,
            expected_label_order=LABEL_ORDER,
            expected_label_set_sha256=LABEL_HASH,
            expected_prompt_hashes=PROMPTS,
            minimum_calibration_n=48,
            minimum_class_n=5,
        )


def test_raw_ballot_provenance_is_required_and_summary_must_match_raw_layers():
    predictions = _predictions()
    predictions["rows"][0]["event_codes"] = []
    with pytest.raises(ValueError, match="summary.*event_codes"):
        _compute(predictions=predictions)

    predictions = _predictions()
    predictions["rows"][0]["layer_e_response_provenance"]["request_id"] = ""
    predictions["rows"][0]["raw_ballot_sha256"] = _raw_ballot_hash(
        predictions["rows"][0], "construct"
    )
    with pytest.raises(ValueError, match="provenance.*request_id"):
        _compute(predictions=predictions)

    predictions = _predictions()
    predictions["rows"][0]["raw_ballot_sha256"] = "0" * 64
    with pytest.raises(ValueError, match="raw_ballot_sha256"):
        _compute(predictions=predictions)


def test_control_domain_has_no_ordinal_or_rubric_metric_and_requires_null_rubric():
    classes = ("foil_correct", "target_action_false_positive", "indeterminate")
    human_rows = []
    resolved = {}
    prediction_rows = []
    control_manifest = _manifest(track="control", count=6)
    manifest_by_id = {
        record["response_id"]: record for record in control_manifest["records"]
    }
    rule_by_label = {
        label: f"N{index}" for index, label in enumerate(classes, start=1)
    }
    for index in range(6):
        response_id = f"N{index:03d}"
        label = classes[index % len(classes)]
        dimensions = {
            "final_label": label,
            "task_correctness": "correct" if index % 2 else "partial",
            "event_codes": ["requested_action_present"],
            "omission_codes": ["required_fact_omitted"] if index % 2 else [],
            "rubric_score": None,
        }
        resolved[response_id] = dict(dimensions)
        for rater_hash in ("1" * 64, "2" * 64):
            human_rows.append(
                {
                    "response_id": response_id,
                    "rater_hash": rater_hash,
                    "role": "primary",
                    **dimensions,
                    "notes": "",
                }
            )
        for judge_id, identity in JUDGES.items():
            probabilities = {
                candidate: 0.8 if candidate == label else 0.1
                for candidate in classes
            }
            layer_e = {
                "schema_version": "1.0",
                "task_correctness": dimensions["task_correctness"],
                "event_codes": [
                    {
                        "code": "requested_action_present",
                        "evidence_spans": ["requested action"],
                    }
                ],
                "omission_codes": list(dimensions["omission_codes"]),
                "refusal_or_evasion": "none",
                "uncertainty": 0.0,
            }
            layer_control = {
                "schema_version": "1.0",
                "final_label": label,
                "class_probabilities": probabilities,
                "rule_ids": [rule_by_label[label]],
                "refusal_or_evasion": "none",
                "uncertainty": 0.0,
            }
            row = {
                    "response_id": response_id,
                    "judge_id": judge_id,
                    "judge_model_id": identity["model_id"],
                    "judge_snapshot": identity["canonical_snapshot"],
                    "judge_vendor": identity["vendor"],
                    "judge_family": identity["family"],
                    **dimensions,
                    "class_probabilities": probabilities,
                    "judge_refused": False,
                    "manifest_response_sha256": manifest_by_id[response_id]["response_sha256"],
                    "manifest_scoring_contract_sha256": manifest_by_id[response_id]["scoring_contract_sha256"],
                    "layer_e_record": layer_e,
                    "layer_control_record": layer_control,
                    "layer_e_request_sha256": "e" * 64,
                    "layer_decision_request_sha256": "f" * 64,
                    "layer_e_response_provenance": {
                        "response_id": f"resp-e-{response_id}-{judge_id}",
                        "request_id": f"req-e-{response_id}-{judge_id}",
                        "generation_id": f"gen-e-{response_id}-{judge_id}",
                        "returned_model": identity["canonical_snapshot"],
                    },
                    "layer_decision_response_provenance": {
                        "response_id": f"resp-c-{response_id}-{judge_id}",
                        "request_id": f"req-c-{response_id}-{judge_id}",
                        "generation_id": f"gen-c-{response_id}-{judge_id}",
                        "returned_model": identity["canonical_snapshot"],
                    },
                }
            row["raw_ballot_sha256"] = _raw_ballot_hash(row, "control")
            prediction_rows.append(row)
    human = {
        "schema_version": "1.0",
        "source_sha256": "b" * 64,
        "rows": human_rows,
        "resolved_records": resolved,
        "coverage": {
            "expected_responses": 6,
            "double_coded_responses": 6,
            "adjudicated_disagreements": 0,
        },
    }
    predictions = {
        "schema_version": "1.0",
        "label_set_sha256": LABEL_HASH,
        "prompt_hashes": PROMPTS,
        "rows": prediction_rows,
    }

    result = compute_judge_evidence(
        human,
        predictions,
        manifest_source=control_manifest,
        expected_track="control",
        expected_judge_identities=JUDGES,
        expected_class_labels=classes,
        expected_label_order=None,
        expected_label_set_sha256=LABEL_HASH,
        expected_prompt_hashes=PROMPTS,
        minimum_calibration_n=6,
        minimum_class_n=2,
    )

    assert "weighted_kappa" not in result.human_human["metrics"]
    assert "rubric_weighted_kappa" not in result.human_human["metrics"]
    assert all("rubric_within_one" not in judge["metrics"] for judge in result.judges)

    human["rows"][0]["rubric_score"] = 1
    with pytest.raises(ValueError, match="control rubric_score"):
        compute_judge_evidence(
            human,
            predictions,
            manifest_source=_manifest(track="control", count=6),
            expected_track="control",
            expected_judge_identities=JUDGES,
            expected_class_labels=classes,
            expected_label_order=None,
            expected_label_set_sha256=LABEL_HASH,
            expected_prompt_hashes=PROMPTS,
            minimum_calibration_n=6,
            minimum_class_n=2,
        )


def test_forged_layer_fields_fail_and_every_raw_layer_field_changes_digest():
    forged = _human()
    forged["rows"][0]["event_codes"] = ["invented_event"]
    with pytest.raises(ValueError, match="unregistered"):
        _compute(human=forged)

    cross_domain = _human()
    cross_domain["rows"][0]["rubric_score"] = None
    with pytest.raises(ValueError, match="rubric_score"):
        _compute(human=cross_domain)

    baseline = _compute()
    human = _human()
    predictions = _predictions()
    human["resolved_records"]["R000"]["event_codes"].append("affected_party_named")
    for row in human["rows"]:
        if row["response_id"] == "R000":
            row["event_codes"].append("affected_party_named")
    for row in predictions["rows"]:
        if row["response_id"] == "R000":
            row["event_codes"].append("affected_party_named")
            row["layer_e_record"]["event_codes"].append(
                {
                    "code": "affected_party_named",
                    "evidence_spans": ["requested action"],
                }
            )
            row["raw_ballot_sha256"] = _raw_ballot_hash(row, "construct")

    changed = _compute(human=human, predictions=predictions)

    assert changed.evidence_sha256 != baseline.evidence_sha256
    assert changed.human_human["metrics"] == baseline.human_human["metrics"]
