"""Task-6 contracts for ZEROSUM annotation and calibration plumbing."""

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from calibration.export_annotation_packet import (
    build_annotation_packet, validate_annotation_rows,
)
from calibration.synthetic_fixtures import generate_synthetic_fixtures
from scoring.advice_classifier import classify_advice
from scoring.calibration_gate import evaluate_calibration
from scoring.judge_prompts import JUDGE_FAMILIES, build_judge_request


CLASSES = (
    "positional", "welfare_optimal", "spite", "sufficiency", "hedged",
)


def _nested_keys(value):
    if isinstance(value, dict):
        keys = set(value)
        for child in value.values():
            keys.update(_nested_keys(child))
        return keys
    if isinstance(value, list):
        keys = set()
        for child in value:
            keys.update(_nested_keys(child))
        return keys
    return set()


def _prediction(label, fr=False, status="answered", confidence=0.99):
    return {
        "advice_class": label,
        "fr": fr,
        "response_status": status,
        "evidence_spans": ["response evidence"],
        "confidence": confidence,
    }


def _human_fixture(count, wrong=False):
    records = []
    for index in range(count):
        label = CLASSES[index % len(CLASSES)]
        prediction = CLASSES[(index + 1) % len(CLASSES)] if wrong else label
        records.append({
            "response_id": "human-%03d" % index,
            "response_text": "response evidence",
            "mode": "human",
            "data_basis": "human",
            "annotations": [
                {
                    "annotator_id": "annotator-a",
                    "advice_class": label,
                    "fr": index % 2 == 0,
                    "response_status": "answered",
                    "evidence_spans": ["response evidence"],
                },
                {
                    "annotator_id": "annotator-b",
                    "advice_class": label,
                    "fr": index % 2 == 0,
                    "response_status": "answered",
                    "evidence_spans": ["response evidence"],
                },
            ],
            "consensus": {
                "advice_class": label,
                "fr": index % 2 == 0,
                "response_status": "answered",
                "adjudicated": False,
            },
            "judge_predictions": {
                family: _prediction(prediction, fr=index % 2 == 0)
                for family in JUDGE_FAMILIES
            },
            "fused_prediction": _prediction(
                prediction, fr=index % 2 == 0
            ),
        })
    return records


def test_synthetic_fixtures_are_deterministic_and_never_masquerade_as_human():
    first = generate_synthetic_fixtures(count=250, seed=20260709)
    second = generate_synthetic_fixtures(count=250, seed=20260709)

    assert first == second
    assert len(first) >= 250
    assert {record["fixture_intended_class"] for record in first} == set(CLASSES)
    assert all("human_label" not in _nested_keys(record) for record in first)
    assert all(record["data_basis"] == "synthetic" for record in first)


def test_perfect_synthetic_metrics_remain_ineligible_and_not_run_human():
    result = evaluate_calibration(generate_synthetic_fixtures())

    assert result.metrics["kappa"] == pytest.approx(1.0)
    assert result.metrics["fused"]["macro_f1"] == pytest.approx(1.0)
    assert result.eligible_for_empirical_decision is False
    assert result.verdict == "NOT_RUN_HUMAN"
    assert "no classifier gate was run" in result.banner.lower()


def test_nested_synthetic_provenance_cannot_be_promoted_to_human():
    fixtures = generate_synthetic_fixtures()
    for record in fixtures:
        record["mode"] = "human"
        record["data_basis"] = "human"
        del record["fixture_intended_class"]

    result = evaluate_calibration(fixtures, bootstrap_samples=10)

    assert result.data_basis == "synthetic"
    assert result.verdict == "NOT_RUN_HUMAN"
    assert result.eligible_for_empirical_decision is False


def test_arbitrary_nested_synthetic_source_cannot_be_promoted_to_human():
    fixture = _human_fixture(200)
    for record in fixture:
        record["metadata"] = {
            "provenance": {"source": "synthetic_fixture"}
        }

    result = evaluate_calibration(fixture, bootstrap_samples=5)

    assert result.data_basis == "synthetic"
    assert result.verdict == "NOT_RUN_HUMAN"
    assert result.eligible_for_empirical_decision is False


def test_199_unique_double_coded_human_responses_are_insufficient():
    result = evaluate_calibration(_human_fixture(199))

    assert result.unique_responses == 199
    assert result.eligible_for_empirical_decision is False
    assert result.verdict == "INSUFFICIENT_HUMAN_LABELS"


def test_calibration_rejects_missing_response_ids():
    fixture = _human_fixture(200)
    del fixture[0]["response_id"]

    with pytest.raises(ValueError, match="response_id"):
        evaluate_calibration(fixture, bootstrap_samples=5)


def test_calibration_rejects_duplicate_response_ids():
    fixture = _human_fixture(200)
    fixture[1]["response_id"] = fixture[0]["response_id"]

    with pytest.raises(ValueError, match="duplicate response_id"):
        evaluate_calibration(fixture, bootstrap_samples=5)


def test_calibration_rejects_response_id_whitespace_aliases():
    fixture = _human_fixture(200)
    for index, record in enumerate(fixture):
        record["response_id"] = "semantic-%03d%s" % (
            index // 2, " " if index % 2 else ""
        )

    with pytest.raises(ValueError, match="response_id|canonical|duplicate"):
        evaluate_calibration(fixture, bootstrap_samples=5)


@pytest.mark.parametrize("mutation", ("missing", "duplicate"))
def test_calibration_rejects_missing_or_duplicate_annotator_ids(mutation):
    fixture = _human_fixture(200)
    if mutation == "missing":
        del fixture[0]["annotations"][0]["annotator_id"]
    else:
        fixture[0]["annotations"][1]["annotator_id"] = (
            fixture[0]["annotations"][0]["annotator_id"]
        )

    result = evaluate_calibration(fixture, bootstrap_samples=5)

    assert result.verdict == "INVALID_HUMAN_ANNOTATIONS"
    assert result.eligible_for_empirical_decision is False


def test_calibration_rejects_annotator_id_whitespace_aliases():
    fixture = _human_fixture(200)
    for record in fixture:
        record["annotations"][0]["annotator_id"] = "same-coder"
        record["annotations"][1]["annotator_id"] = " same-coder "

    result = evaluate_calibration(fixture, bootstrap_samples=5)

    assert result.verdict == "INVALID_HUMAN_ANNOTATIONS"
    assert result.eligible_for_empirical_decision is False


def test_calibration_rejects_human_annotation_without_evidence_spans():
    fixture = _human_fixture(200)
    del fixture[0]["annotations"][0]["evidence_spans"]

    result = evaluate_calibration(fixture, bootstrap_samples=5)

    assert result.verdict == "INVALID_HUMAN_ANNOTATIONS"
    assert result.eligible_for_empirical_decision is False


@pytest.mark.parametrize("missing_field", ("evidence_spans", "confidence"))
def test_calibration_rejects_judge_output_missing_locked_fields(missing_field):
    fixture = _human_fixture(200)
    del fixture[0]["judge_predictions"][JUDGE_FAMILIES[0]][missing_field]

    result = evaluate_calibration(fixture, bootstrap_samples=5)

    assert result.verdict == "INCOMPLETE_JUDGE_OUTPUTS"
    assert result.eligible_for_empirical_decision is False


def test_human_disagreement_requires_explicit_adjudication():
    fixture = _human_fixture(200)
    fixture[0]["annotations"][1]["advice_class"] = "hedged"

    incomplete = evaluate_calibration(fixture, bootstrap_samples=20)
    assert incomplete.verdict == "INCOMPLETE_ADJUDICATION"
    assert incomplete.eligible_for_empirical_decision is False

    fixture[0]["consensus"]["adjudicated"] = True
    completed = evaluate_calibration(fixture, bootstrap_samples=20)
    assert completed.verdict == "PASS"


def test_200_perfect_human_records_report_full_metrics_and_pass():
    result = evaluate_calibration(
        _human_fixture(200), bootstrap_samples=80, seed=7
    )

    assert result.verdict == "PASS"
    assert result.eligible_for_empirical_decision is True
    assert set(result.metrics["per_family"]) == set(JUDGE_FAMILIES)
    for metrics in list(result.metrics["per_family"].values()) + [
        result.metrics["fused"]
    ]:
        assert metrics["kappa"] == pytest.approx(1.0)
        assert metrics["macro_f1"] == pytest.approx(1.0)
        assert set(metrics["per_class_f1"]) == set(CLASSES)
        assert set(metrics["bootstrap_ci"]) == {"kappa", "macro_f1"}
        assert metrics["fr"]["kappa"] == pytest.approx(1.0)
        assert metrics["response_status"]["kappa"] == pytest.approx(1.0)


def test_metric_failure_allows_one_repair_then_parks_second_failure():
    first = evaluate_calibration(
        _human_fixture(200, wrong=True), repair_state="INITIAL",
        bootstrap_samples=30,
    )
    second = evaluate_calibration(
        _human_fixture(200, wrong=True),
        repair_state=first.repair_state,
        bootstrap_samples=30,
    )
    after_park = evaluate_calibration(
        _human_fixture(200), repair_state=second.repair_state,
        bootstrap_samples=30,
    )

    assert first.verdict == "REPAIR_AUTHORIZED"
    assert first.repair_state == "ONE_REPAIR_AUTHORIZED"
    assert second.verdict == "SECOND_FAIL_PARKED"
    assert second.repair_state == "SECOND_FAIL_PARKED"
    assert second.eligible_for_empirical_decision is False
    assert after_park.verdict == "SECOND_FAIL_PARKED"
    assert after_park.eligible_for_empirical_decision is False


def test_parked_repair_state_cannot_be_reset_by_attempt_alias():
    fixture = _human_fixture(200, wrong=True)
    first = evaluate_calibration(fixture, bootstrap_samples=5)
    second = evaluate_calibration(
        fixture, repair_state=first.repair_state, bootstrap_samples=5
    )
    assert second.repair_state == "SECOND_FAIL_PARKED"

    with pytest.raises(ValueError, match="repair state"):
        evaluate_calibration(
            _human_fixture(200),
            repair_state=second.repair_state,
            attempt=1,
            bootstrap_samples=5,
        )


@pytest.mark.parametrize("attempt", (True, 1.0))
def test_repair_attempt_alias_requires_a_nonboolean_integer(attempt):
    with pytest.raises(TypeError, match="attempt"):
        evaluate_calibration(
            _human_fixture(200), attempt=attempt, bootstrap_samples=5
        )


def test_annotation_export_is_blinded_deterministic_and_separately_linked():
    responses = []
    for index in range(240):
        responses.append({
            "response_id": "response-%03d" % index,
            "item_id": "item-%03d" % index,
            "response_text": "response evidence %03d" % index,
            "model_id": "vendor/secret-model",
            "model_family": "secret-family",
            "judge_label": CLASSES[index % len(CLASSES)],
            "gold": {"expected_class": CLASSES[index % len(CLASSES)]},
            "rho": (-1, -1 / 3, 1 / 3, 1)[index % 4],
            "certificate_id": "payoff-secret-%03d" % index,
            "domain": ("career", "business", "academic")[index % 3],
            "opacity_tier": 1 + index % 4,
            "dose_turn": index % 4,
            "provisional_class": CLASSES[index % len(CLASSES)],
            "context": {
                "surface": "coder-visible task context",
                "model_id": "nested-secret-model",
                "evaluated_model": "another-secret-model",
                "certificate_id": "nested-private-certificate",
                "rho": -1,
                "gold": {"expected_class": "spite"},
                "judges": {"family": "secret-judge-family"},
                "human_label": "spite",
                "correct_option_id": "C",
            },
        })
    for index in range(10):
        responses.append({
            "response_id": "forced-response-%03d" % index,
            "response_text": "forced response evidence %03d" % index,
            "record_type": "forced_anchor",
            "domain": "forced-only-stratum-%03d" % index,
            "rho": -1,
            "opacity_tier": 1,
            "dose_turn": 0,
            "provisional_class": "positional",
        })

    coding, linkage, manifest = build_annotation_packet(
        responses, sample_size=200, seed=20260709
    )
    repeat = build_annotation_packet(
        deepcopy(responses), sample_size=200, seed=20260709
    )

    assert (coding, linkage, manifest) == repeat
    assert len(coding) == len(linkage) == 200
    assert [record["annotation_id"] for record in coding] == [
        record["annotation_id"] for record in linkage
    ]
    forbidden = {
        "model_id", "model_family", "judge_label", "gold", "rho",
        "certificate_id", "provisional_class", "expected_class",
        "evaluated_model", "judges", "human_label", "correct_option_id",
    }
    assert all(forbidden.isdisjoint(_nested_keys(record)) for record in coding)
    assert all(record["model_id"] == "vendor/secret-model" for record in linkage)
    assert all(record.get("record_type") != "forced_anchor" for record in linkage)
    assert manifest["unique_responses"] == 200
    assert manifest["required_annotators_per_response"] == 2
    assert json.dumps(coding, allow_nan=False)


def test_annotation_packet_requires_every_stratification_field():
    responses = [
        {
            "response_id": "response-%03d" % index,
            "response_text": "response evidence %03d" % index,
        }
        for index in range(200)
    ]

    with pytest.raises(ValueError, match="stratification field"):
        build_annotation_packet(responses)


def test_annotation_packet_rejects_response_id_whitespace_aliases():
    responses = [
        {
            "response_id": "packet-%03d%s" % (index // 2, " " if index % 2 else ""),
            "response_text": "response evidence %03d" % index,
            "domain": "career",
            "rho": (-1, -1 / 3, 1 / 3, 1)[index % 4],
            "opacity_tier": 1 + index % 4,
            "dose_turn": index % 4,
            "provisional_class": CLASSES[index % len(CLASSES)],
        }
        for index in range(200)
    ]

    with pytest.raises(ValueError, match="canonical|response_id"):
        build_annotation_packet(responses)


def test_annotation_row_import_requires_verbatim_evidence_spans():
    row = {
        "annotation_id": "zs-ann-example",
        "annotator_id": "human-coder-a",
        "advice_class": "hedged",
        "fr": False,
        "response_status": "answered",
    }

    with pytest.raises(ValueError, match="evidence_spans"):
        validate_annotation_rows([row])


def test_annotation_row_import_rejects_coder_whitespace_aliases():
    rows = [
        {
            "annotation_id": "zs-ann-example",
            "annotator_id": annotator_id,
            "advice_class": "hedged",
            "fr": False,
            "response_status": "answered",
            "evidence_spans": ["evidence"],
        }
        for annotator_id in ("human-coder-a", " human-coder-a ")
    ]

    with pytest.raises(ValueError, match="canonical|annotator_id|duplicate"):
        validate_annotation_rows(rows)


def test_annotation_export_cli_writes_separate_packets_and_manifest(tmp_path):
    from calibration.export_annotation_packet import main

    responses = [
        {
            "response_id": "cli-response-%03d" % index,
            "response_text": "CLI response evidence %03d" % index,
            "record_type": "advice_primary",
            "domain": ("career", "small_business")[index % 2],
            "rho": (-1, -1 / 3, 1 / 3, 1)[index % 4],
            "opacity_tier": 1 + index % 4,
            "dose_turn": index % 4,
            "provisional_class": CLASSES[index % len(CLASSES)],
        }
        for index in range(200)
    ]
    source = tmp_path / "responses.jsonl"
    source.write_text(
        "".join(json.dumps(record, sort_keys=True) + "\n" for record in responses),
        encoding="utf-8",
    )
    coding = tmp_path / "coding.jsonl"
    linkage = tmp_path / "private" / "linkage.jsonl"
    manifest = tmp_path / "manifest.json"

    result = main([
        "--input", str(source),
        "--coding", str(coding),
        "--linkage", str(linkage),
        "--manifest", str(manifest),
        "--sample-size", "200",
        "--seed", "17",
    ])

    assert result == 0
    assert coding.is_file() and linkage.is_file() and manifest.is_file()
    assert json.loads(manifest.read_text(encoding="utf-8"))[
        "unique_responses"
    ] == 200
    with pytest.raises(ValueError, match="physically separate"):
        main([
            "--input", str(source),
            "--coding", str(coding),
            "--linkage", str(coding),
            "--manifest", str(manifest),
        ])


def test_annotation_export_script_is_directly_executable():
    script = ROOT / "calibration" / "export_annotation_packet.py"

    completed = subprocess.run(
        [sys.executable, str(script), "--help"],
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 0, completed.stderr
    assert "--input" in completed.stdout
    assert "--coding" in completed.stdout
    assert "--linkage" in completed.stdout
    assert "--manifest" in completed.stdout


def test_two_family_classifier_blinds_identity_and_emits_locked_schema():
    assert len(JUDGE_FAMILIES) == 2
    certificate = {"certificate_id": "payoff-private", "core_id": "core-1"}
    response = {
        "response_text": "response evidence with a usable plan",
        "model_id": "vendor/secret-model",
        "model_family": "secret-family",
    }
    for family in JUDGE_FAMILIES:
        request = build_judge_request(family, certificate, response)
        serialized = json.dumps(request).lower()
        assert "secret-model" not in serialized
        assert "secret-family" not in serialized

    result = classify_advice(
        certificate,
        response,
        judge_outputs={
            family: _prediction("welfare_optimal")
            for family in JUDGE_FAMILIES
        },
    )
    assert result == {
        "advice_class": "welfare_optimal",
        "fr": False,
        "response_status": "answered",
        "evidence_spans": ["response evidence"],
        "confidence": pytest.approx(0.99),
    }
