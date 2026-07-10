"""Runnable-harness contract tests for ZEROSUM P1."""

from collections import Counter
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _bank():
    from itembank.build_bank import build_bank

    return build_bank(seed=20260709)[:2]


def _passing_calibration_report():
    return _genuine_calibration_report()


def _genuine_calibration_report():
    from scoring.calibration_gate import evaluate_calibration
    from scoring.judge_prompts import JUDGE_FAMILIES
    from zerosum_common import ADVICE_CLASSES

    records = []
    for index in range(200):
        label = ADVICE_CLASSES[index % len(ADVICE_CLASSES)]
        evidence = "human calibration evidence %03d" % index
        prediction = {
            "advice_class": label,
            "fr": index % 2 == 0,
            "response_status": "answered",
            "evidence_spans": [evidence],
            "confidence": 0.99,
        }
        annotation = {
            "advice_class": label,
            "fr": index % 2 == 0,
            "response_status": "answered",
            "evidence_spans": [evidence],
        }
        records.append({
            "response_id": "human-calibration-%03d" % index,
            "response_text": evidence,
            "mode": "human",
            "data_basis": "human",
            "annotations": [
                {**annotation, "annotator_id": "human-a"},
                {**annotation, "annotator_id": "human-b"},
            ],
            "consensus": {
                "advice_class": label,
                "fr": index % 2 == 0,
                "response_status": "answered",
                "adjudicated": False,
            },
            "judge_predictions": {
                family: dict(prediction) for family in JUDGE_FAMILIES
            },
            "fused_prediction": dict(prediction),
        })
    return evaluate_calibration(
        records, bootstrap_samples=5, seed=17
    ).to_dict()


def test_adapter_request_is_strictly_model_facing():
    from harness.model_adapters import build_model_request

    bank, gold = _bank()
    request = build_model_request(bank[0], gold[0], turn_index=0)
    serialized = json.dumps(request).lower()
    for forbidden in (
        "certificate", "expected_class", "expected_fr_direction",
        "proof_checks", "paired_observations", "rho", "frame_alignment",
    ):
        assert forbidden not in serialized
    assert set(request) == {"request_id", "messages", "response_format"}
    assert request["messages"][-1]["role"] == "user"


def test_trajectory_requests_have_four_cumulative_turns_and_twins_one():
    from harness.model_adapters import build_requests_for_record

    bank, gold = _bank()
    private = {record["id"]: record for record in gold}
    primary = next(record for record in bank if record["record_type"] == "advice_primary")
    twin = next(record for record in bank if record["record_type"] != "advice_primary")
    primary_requests = build_requests_for_record(primary, private[primary["id"]])
    twin_requests = build_requests_for_record(twin, private[twin["id"]])
    assert [request["request_id"].rsplit("--t", 1)[-1] for request in primary_requests] == [
        "0", "1", "2", "3"
    ]
    lengths = [len(request["messages"][-1]["content"]) for request in primary_requests]
    assert lengths == sorted(lengths)
    assert len(set(lengths)) == 4
    assert len(twin_requests) == 1


def test_live_preconditions_fail_closed_on_calibration_roster_and_hashes(tmp_path):
    from harness.model_adapters import PreconditionError, validate_live_preconditions

    prereg = tmp_path / "preregistration.md"
    prereg.write_text("frozen protocol\n", encoding="utf-8")
    digest = hashlib.sha256(prereg.read_bytes()).hexdigest()
    valid = {
        "mode": "live",
        "seeds": [101, 102, 103],
        "model_roster": [
            {"model_id": "a-1", "family": "family-a", "vendor": "vendor-a"},
            {"model_id": "b-1", "family": "family-b", "vendor": "vendor-b"},
            {"model_id": "b-2", "family": "family-b2", "vendor": "vendor-b"},
        ],
        "judge_families": ["judge-c", "judge-d"],
        "provenance": {"preregistration_sha256": digest},
    }
    calibration = _genuine_calibration_report()
    assert calibration["verdict"] == "PASS"
    assert calibration["data_basis"] == "human"
    assert validate_live_preconditions(
        valid, calibration, preregistration_path=prereg,
        credential_vendors={"vendor-a", "vendor-b"},
    )["eligible"] is True

    cases = []
    cases.append(({**valid, "model_roster": valid["model_roster"][:1]}, calibration))
    cases.append((valid, {"verdict": "NOT_RUN_HUMAN", "eligible_for_empirical_decision": False}))
    cases.append(({**valid, "provenance": {"preregistration_sha256": "0" * 64}}, calibration))
    overlap = json.loads(json.dumps(valid))
    overlap["judge_families"] = ["family-a", "judge-d"]
    cases.append((overlap, calibration))
    whitespace_overlap = json.loads(json.dumps(valid))
    whitespace_overlap["model_roster"][0]["family"] = "family-a "
    cases.append((whitespace_overlap, calibration))
    fabricated_status_shell = {
        "verdict": "PASS",
        "eligible_for_empirical_decision": True,
        "data_basis": "human",
        "repair_state": "PASSED",
        "unique_responses": 200,
        "double_coded_responses": 200,
    }
    cases.append((valid, fabricated_status_shell))
    below_bar_metrics = deepcopy(calibration)
    family = next(iter(below_bar_metrics["metrics"]["per_family"]))
    below_bar_metrics["metrics"]["per_family"][family]["kappa"] = 0.0
    below_bar_metrics["metrics"]["judges"][family]["kappa"] = 0.0
    cases.append((valid, below_bar_metrics))
    for config, report in cases:
        with pytest.raises(PreconditionError):
            validate_live_preconditions(
                config, report, preregistration_path=prereg,
                credential_vendors={"vendor-a", "vendor-b"},
            )
    with pytest.raises(PreconditionError, match="credential"):
        validate_live_preconditions(
            valid, calibration, preregistration_path=prereg,
            credential_vendors={"vendor-a"},
        )


def test_live_runner_preflights_all_clients_before_first_call(tmp_path):
    from harness.model_adapters import PreconditionError
    from harness.run_p1 import run_live

    prereg = tmp_path / "preregistration.md"
    prereg.write_text("frozen protocol\n", encoding="utf-8")
    config = {
        "mode": "live",
        "seeds": [101, 102, 103],
        "model_roster": [
            {"model_id": "a-1", "family": "family-a", "vendor": "vendor-a"},
            {"model_id": "b-1", "family": "family-b", "vendor": "vendor-b"},
            {"model_id": "b-2", "family": "family-b2", "vendor": "vendor-b"},
        ],
        "judge_families": ["judge-c", "judge-d"],
        "provenance": {
            "preregistration_sha256": hashlib.sha256(prereg.read_bytes()).hexdigest()
        },
    }
    calibration = _passing_calibration_report()

    class FakeClient:
        def __init__(self, model_id, family, vendor):
            self.model_id = model_id
            self.family = family
            self.vendor = vendor
            self.calls = 0

        def generate(self, request, *, seed):
            self.calls += 1
            return "live response %s seed %d" % (request["request_id"], seed)

    clients = [FakeClient(**row) for row in config["model_roster"]]
    bank, _ = _bank()
    small_bank = [
        next(record for record in bank if record["record_type"] == "advice_primary"),
        next(record for record in bank if record["record_type"] == "comprehension_twin"),
    ]
    result = run_live(
        small_bank, clients=clients, config=config, calibration_report=calibration,
        preregistration_path=prereg, credential_vendors={"vendor-a", "vendor-b"},
    )
    assert result["status"] == "LIVE_RESPONSES_COLLECTED_UNSCORED"
    assert len(result["responses"]) == 3 * 3 * 5
    assert all(client.calls == 3 * 5 for client in clients)
    assert {row["seed"] for row in result["responses"]} == {101, 102, 103}

    bad_clients = [FakeClient(**row) for row in config["model_roster"]]
    bad_clients[-1].family = "wrong-family"
    with pytest.raises(PreconditionError, match="client roster"):
        run_live(
            small_bank, clients=bad_clients, config=config,
            calibration_report=calibration, preregistration_path=prereg,
            credential_vendors={"vendor-a", "vendor-b"},
        )
    assert all(client.calls == 0 for client in bad_clients)


def test_live_runner_isolates_request_objects_between_clients_and_seeds(tmp_path):
    from harness.run_p1 import run_live

    prereg = tmp_path / "preregistration.md"
    prereg.write_text("frozen protocol\n", encoding="utf-8")
    config = {
        "mode": "live",
        "seeds": [11, 12, 13],
        "model_roster": [
            {"model_id": "mutator", "family": "family-a", "vendor": "vendor-a"},
            {"model_id": "observer", "family": "family-b", "vendor": "vendor-b"},
            {"model_id": "observer-2", "family": "family-c", "vendor": "vendor-b"},
        ],
        "judge_families": ["judge-x", "judge-y"],
        "provenance": {
            "preregistration_sha256": hashlib.sha256(prereg.read_bytes()).hexdigest()
        },
    }

    class Client:
        def __init__(self, row, mutate=False):
            self.model_id = row["model_id"]
            self.family = row["family"]
            self.vendor = row["vendor"]
            self.mutate = mutate
            self.seen = []

        def generate(self, request, *, seed):
            content = request["messages"][0]["content"]
            self.seen.append((seed, content))
            if self.mutate:
                request["messages"][0]["content"] = "MUTATED"
            return "ok"

    clients = [
        Client(config["model_roster"][0], mutate=True),
        Client(config["model_roster"][1]),
        Client(config["model_roster"][2]),
    ]
    bank, _ = _bank()
    primary = next(record for record in bank if record["record_type"] == "advice_primary")
    run_live(
        [primary], clients=clients, config=config,
        calibration_report=_passing_calibration_report(),
        preregistration_path=prereg, credential_vendors={"vendor-a", "vendor-b"},
    )
    assert all(content != "MUTATED" for _, content in clients[1].seen + clients[2].seen)
    assert {seed for seed, _ in clients[1].seen} == {11, 12, 13}


def test_synthetic_harness_runs_registered_profiles_deterministically():
    from harness.run_p1 import run_synthetic

    bank, gold = _bank()
    profiles = [
        "structure_sensitive", "flat_positional", "perverse_harmony",
        "null_fr", "gr_floor",
    ]
    first = run_synthetic(bank, gold, profiles=profiles, seed=17)
    second = run_synthetic(bank, gold, profiles=profiles, seed=17)
    assert first == second
    assert len(first["responses"]) == 1112 * len(profiles)
    assert first["status"] == "HARNESS_VALIDATION_ONLY"
    assert first["eligible_for_empirical_decision"] is False
    assert first["live_pilot_status"] == "BLOCKED_PRECONDITIONS"
    assert all(row["data_basis"] == "synthetic" for row in first["responses"])
    assert {row["seed"] for row in first["responses"]} == {17}
    assert all("human_label" not in row for row in first["responses"])
    per_profile = Counter(row["model_id"] for row in first["responses"])
    assert per_profile == {name: 1112 for name in profiles}
    primary_turns = Counter(
        (row["model_id"], row["item_id"])
        for row in first["responses"] if row["record_type"] == "advice_primary"
    )
    assert set(primary_turns.values()) == {4}


def test_synthetic_forced_intent_matches_private_mechanical_option_class():
    from harness.run_p1 import run_synthetic
    from scoring.forced_choice import build_choice_key, score_forced_rows

    bank, gold = _bank()
    result = run_synthetic(
        bank, gold,
        profiles=["structure_sensitive", "flat_positional", "perverse_harmony", "gr_floor"],
        seed=43,
    )
    forced = [
        row for row in result["responses"] if row["record_type"] == "forced_anchor"
    ]
    scored = score_forced_rows(forced, build_choice_key(bank, gold))

    assert scored
    assert all(row["fixture_class_mismatch"] is False for row in scored)
    assert all(row["advice_class"] == row["fixture_intended_class"] for row in scored)


def test_choice_fixture_rejects_missing_private_option_class_key():
    from harness.synthetic_profiles import fixture_response

    bank, gold = _bank()
    forced_index = next(
        index for index, row in enumerate(bank) if row["record_type"] == "forced_anchor"
    )
    with pytest.raises(ValueError, match="option-class key"):
        fixture_response(
            "gr_floor", bank[forced_index], gold[forced_index],
            turn_index=0, seed=43,
        )


def test_planted_profiles_have_registered_endpoint_order_and_gr_floor():
    from harness.run_p1 import run_synthetic

    bank, gold = _bank()
    result = run_synthetic(
        bank, gold,
        profiles=["structure_sensitive", "flat_positional", "perverse_harmony", "gr_floor"],
        seed=31,
    )
    primary = [
        row for row in result["responses"]
        if row["record_type"] == "advice_primary" and row["turn_index"] == 3
    ]

    def endpoint_delta(profile):
        rows = [row for row in primary if row["model_id"] == profile]
        neg = [row["fixture_intended_class"] == "positional" for row in rows if row["rho"] == -1]
        pos = [row["fixture_intended_class"] == "positional" for row in rows if row["rho"] == 1]
        return sum(neg) / len(neg) - sum(pos) / len(pos)

    assert endpoint_delta("structure_sensitive") > endpoint_delta("flat_positional")
    assert endpoint_delta("flat_positional") > endpoint_delta("perverse_harmony")
    gr_rows = [
        row for row in result["responses"]
        if row["model_id"] == "gr_floor"
        and row["record_type"] == "advice_primary"
        and row["turn_index"] == 3
    ]
    assert sum(row["fixture_intended_class"] == "spite" for row in gr_rows) >= 20
    assert all(
        row["fixture_gr"] is (row["fixture_intended_class"] == "spite")
        for row in gr_rows
    )
