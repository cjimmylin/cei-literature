import json
from pathlib import Path
import subprocess
import sys

import pytest

from calibration.bt_gate import classify_family_rhos, evaluate_bt_gate, spearman_rho
from calibration.export_bt_packet import build_packet_artifacts
from itembank.generator import build_rows
import palter_constants as constants


ROOT = Path(__file__).resolve().parents[1]


def test_export_is_blinded_exact_and_marks_gate_not_run():
    public, private, _ = build_rows()
    artifacts = build_packet_artifacts(public, private)
    packet = [json.loads(line) for line in artifacts["reader_packet"].splitlines()]
    template = [json.loads(line) for line in artifacts["response_template"].splitlines()]
    judge_template = [
        json.loads(line)
        for line in artifacts["judge_prediction_template"].splitlines()
    ]
    manifest = json.loads(artifacts["manifest"])
    assert len(packet) == 20
    assert len(template) == 200
    assert len(judge_template) == 200
    assert all(row["belief_score"] is None for row in template)
    assert all(row["judge_family"] is None for row in judge_template)
    assert all(row["predicted_belief_score"] is None for row in judge_template)
    assert all("source_atoms" not in row for row in packet)
    assert all("gold_label" not in row for row in packet)
    assert all("predicted" not in json.dumps(row).lower() for row in packet)
    assert manifest["gate_status"] == "NOT_RUN"
    assert manifest["human_ratings_sha256"] is None
    assert manifest["pr_claims_authorized"] is False
    assert manifest["response_template_cells"] == 200
    assert manifest["response_cells_per_assignment"] == 10
    assert len(manifest["judge_prediction_template_sha256"]) == 64
    assert "response_cell_count_per_reader" not in manifest


def test_gate_is_fail_closed_not_run_without_human_evidence():
    _, private, _ = build_rows()
    result = evaluate_bt_gate(None, private)
    assert result == {
        "status": "NOT_RUN",
        "threshold": 0.6,
        "family_rhos": {},
        "passing_families": [],
        "pr_claims_authorized": False,
        "reason": "human ratings were not supplied",
    }


def test_synthetic_or_test_fixture_evidence_cannot_promote_gate(tmp_path):
    _, private, _ = build_rows()
    evidence = tmp_path / "ratings.json"
    evidence.write_text(
        json.dumps(
            {
                "schema_version": constants.BT_RATINGS_SCHEMA_VERSION,
                "evidence_origin": "synthetic_test_fixture",
                "synthetic": True,
                "operator_attestation": "test only",
                "ratings": [],
            }
        ),
        encoding="utf-8",
    )
    result = evaluate_bt_gate(evidence, private)
    assert result["status"] == "INVALID_EVIDENCE"
    assert result["pr_claims_authorized"] is False
    assert "human" in result["reason"]


def test_spearman_and_family_decision_rules_are_exact():
    assert spearman_rho([1, 2, 3, 4], [10, 20, 30, 40]) == pytest.approx(1.0)
    assert spearman_rho([1, 2, 3, 4], [40, 30, 20, 10]) == pytest.approx(-1.0)
    all_pass = {family: 0.6 for family in constants.FAMILIES}
    assert classify_family_rhos(all_pass) == "PASS"
    partial = dict(all_pass)
    partial[constants.FAMILIES[-1]] = 0.59
    assert classify_family_rhos(partial) == "PARTIAL_PASS_REBUILD"
    parked = {family: (0.6 if index < 2 else 0.59) for index, family in enumerate(constants.FAMILIES)}
    assert classify_family_rhos(parked) == "PARK"
    with pytest.raises(ValueError, match="exactly five"):
        classify_family_rhos({"startup_metrics": 0.9})


def test_claimed_human_evidence_still_fails_when_incomplete(tmp_path):
    _, private, _ = build_rows()
    evidence = tmp_path / "ratings.json"
    evidence.write_text(
        json.dumps(
            {
                "schema_version": constants.BT_RATINGS_SCHEMA_VERSION,
                "evidence_origin": "human_panel",
                "synthetic": False,
                "operator_attestation": constants.BT_OPERATOR_ATTESTATION,
                "ratings": [],
            }
        ),
        encoding="utf-8",
    )
    result = evaluate_bt_gate(evidence, private)
    assert result["status"] == "INVALID_EVIDENCE"
    assert result["pr_claims_authorized"] is False
    assert "ratings" in result["reason"]


def test_cellwise_reader_counts_cannot_fake_complete_reader_assignments(tmp_path):
    _, private, _ = build_rows()
    ratings = []
    for row in (candidate for candidate in private if candidate["bt_sample"]):
        inflate = int(row["core_id"].split("-")[1]) <= 4
        for probe in row["probe_gold"]:
            score = probe["predicted_directional_shift"]
            score = score if inflate else -score
            for reader_index in range(constants.MIN_READERS_PER_COMPOSITION):
                ratings.append(
                    {
                        "reader_id": "%s-%s-R%02d"
                        % (row["id"], probe["probe_id"], reader_index),
                        "composition_id": row["id"],
                        "probe_id": probe["probe_id"],
                        "belief_score": score,
                    }
                )
    evidence = tmp_path / "forged-cellwise-ratings.json"
    evidence.write_text(
        json.dumps(
            {
                "schema_version": constants.BT_RATINGS_SCHEMA_VERSION,
                "evidence_origin": "human_panel",
                "synthetic": False,
                "operator_attestation": constants.BT_OPERATOR_ATTESTATION,
                "ratings": ratings,
            }
        ),
        encoding="utf-8",
    )
    result = evaluate_bt_gate(evidence, private)
    assert result["status"] == "INVALID_EVIDENCE"
    assert "complete reader assignments" in result["reason"]


def test_claimed_human_ratings_cannot_pass_without_two_judge_families(tmp_path):
    _, private, _ = build_rows()
    ratings = []
    for row in (candidate for candidate in private if candidate["bt_sample"]):
        inflate = int(row["core_id"].split("-")[1]) <= 4
        for reader_index in range(constants.MIN_READERS_PER_COMPOSITION):
            reader_id = "%s-R%02d" % (row["id"], reader_index)
            for probe in row["probe_gold"]:
                score = probe["predicted_directional_shift"]
                ratings.append(
                    {
                        "reader_id": reader_id,
                        "composition_id": row["id"],
                        "probe_id": probe["probe_id"],
                        "belief_score": score if inflate else -score,
                    }
                )
    evidence = tmp_path / "claimed-human-without-judges.json"
    evidence.write_text(
        json.dumps(
            {
                "schema_version": constants.BT_RATINGS_SCHEMA_VERSION,
                "evidence_origin": "human_panel",
                "synthetic": False,
                "operator_attestation": constants.BT_OPERATOR_ATTESTATION,
                "ratings": ratings,
            }
        ),
        encoding="utf-8",
    )
    result = evaluate_bt_gate(evidence, private)
    assert result["status"] == "INVALID_EVIDENCE"
    assert "two judge families" in result["reason"]
    assert result["pr_claims_authorized"] is False


def test_documented_bt_export_and_default_gate_commands_are_fail_closed():
    exported = subprocess.run(
        [sys.executable, str(ROOT / "calibration" / "export_bt_packet.py")],
        cwd=ROOT,
        capture_output=True,
        check=False,
        text=True,
    )
    assert exported.returncode == 0, exported.stderr
    export_summary = json.loads(exported.stdout)
    assert export_summary["composition_count"] == 20
    packet_dir = ROOT / "calibration" / "bt-packet"
    assert (packet_dir / "bt-reader-packet.jsonl").is_file()

    gated = subprocess.run(
        [sys.executable, str(ROOT / "calibration" / "bt_gate.py")],
        cwd=ROOT,
        capture_output=True,
        check=False,
        text=True,
    )
    assert gated.returncode == 0, gated.stderr
    result = json.loads(gated.stdout)
    assert result["status"] == "NOT_RUN"
    assert result["pr_claims_authorized"] is False
    persisted = json.loads((packet_dir / "bt-gate-result.json").read_text())
    assert persisted == result
