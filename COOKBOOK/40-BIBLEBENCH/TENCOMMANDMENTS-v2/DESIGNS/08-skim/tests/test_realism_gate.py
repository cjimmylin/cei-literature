"""Task-6 contracts for blinded professional realism and human baseline."""

from collections import Counter, defaultdict
from copy import deepcopy
import hashlib
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
BANK_PATH = ROOT / "itembank" / "bank" / "p1-public.jsonl"
PROTOCOL_PATH = ROOT / "calibration" / "realism_protocol.md"

BINARY_FIELDS = (
    "scenario_realism",
    "magnitude_window_plausibility",
)
ORDINAL_FIELDS = (
    "scenario_realism_rating_1_to_5",
    "magnitude_window_plausibility_rating_1_to_5",
)
RATING_FIELDS = BINARY_FIELDS + ORDINAL_FIELDS


def require_calibration(name):
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    try:
        return importlib.import_module("calibration.%s" % name)
    except ModuleNotFoundError as exc:
        if exc.name in {"calibration", "calibration.%s" % name}:
            pytest.fail("calibration/%s.py has not been implemented" % name)
        raise


def _load_jsonl(path):
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def _write_jsonl(path, rows):
    path.write_text(
        "".join(
            json.dumps(
                row,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
                allow_nan=False,
            )
            + "\n"
            for row in rows
        ),
        encoding="utf-8",
    )


def _nested_keys(value):
    if isinstance(value, dict):
        result = set(value)
        for child in value.values():
            result.update(_nested_keys(child))
        return result
    if isinstance(value, list):
        result = set()
        for child in value:
            result.update(_nested_keys(child))
        return result
    return set()


@pytest.fixture(scope="module")
def public_rows():
    return _load_jsonl(BANK_PATH)


@pytest.fixture
def packet_bundle(public_rows):
    exporter = require_calibration("export_realism_packet")
    return exporter.build_realism_packet(public_rows, seed=20260711)


def _panel():
    return [
        {
            "rater_id": "professional-1",
            "qualification": "procurement_professional",
            "qualification_evidence": "private employment attestation P-1",
            "covers_procurement": True,
            "covers_finance": False,
            "synthetic": False,
        },
        {
            "rater_id": "professional-2",
            "qualification": "finance_professional",
            "qualification_evidence": "private employment attestation F-2",
            "covers_procurement": False,
            "covers_finance": True,
            "synthetic": False,
        },
        {
            "rater_id": "professional-3",
            "qualification": "procurement_finance_professional",
            "qualification_evidence": "private credential attestation PF-3",
            "covers_procurement": True,
            "covers_finance": True,
            "synthetic": False,
        },
    ]


def _professional_evidence(packet, linkage):
    exporter = require_calibration("export_realism_packet")
    packet_hash = exporter.canonical_jsonl_sha256(packet)
    linkage_hash = exporter.canonical_jsonl_sha256(linkage)
    panel = _panel()
    rater_ids = tuple(row["rater_id"] for row in panel)
    by_family = defaultdict(list)
    for row in linkage:
        by_family[row["family"]].append(row)

    ratings = []
    adjudications = []
    core_index = 0
    for family_index, family in enumerate(sorted(by_family)):
        family_rows = sorted(by_family[family], key=lambda row: row["core_id"])
        for within_family, link in enumerate(family_rows):
            pair = (
                rater_ids[core_index % 3],
                rater_ids[(core_index + 1) % 3],
            )
            is_failing_core = within_family == 7
            is_disagreement = is_failing_core and family_index >= 3
            values = (True, False) if is_disagreement else (
                (False, False) if is_failing_core else (True, True)
            )
            for rater_id, answer in zip(pair, values):
                ratings.append(
                    {
                        "review_id": link["review_id"],
                        "rater_id": rater_id,
                        "independent_submission": True,
                        "scenario_realism": answer,
                        "scenario_realism_rating_1_to_5": 5 if answer else 1,
                        "magnitude_window_plausibility": answer,
                        "magnitude_window_plausibility_rating_1_to_5": (
                            5 if answer else 1
                        ),
                    }
                )
            if is_disagreement:
                third = next(rater for rater in rater_ids if rater not in pair)
                adjudications.append(
                    {
                        "review_id": link["review_id"],
                        "adjudicator_id": third,
                        "disagreement_fields": sorted(RATING_FIELDS),
                        "resolution": {
                            "scenario_realism": False,
                            "scenario_realism_rating_1_to_5": 3,
                            "magnitude_window_plausibility": False,
                            "magnitude_window_plausibility_rating_1_to_5": 3,
                        },
                        "reason": "Documented panel adjudication of the disagreement.",
                    }
                )
            core_index += 1
    return {
        "schema_version": 1,
        "instrument": "SKIM-P1-PROFESSIONAL-REALISM",
        "data_basis": "direct_professional_human_ratings",
        "packet_sha256": packet_hash,
        "linkage_sha256": linkage_hash,
        "panel": panel,
        "ratings": ratings,
        "adjudications": adjudications,
        "revision_history": [],
    }


def _evaluate(packet, linkage, evidence):
    gate = require_calibration("realism_gate")
    return gate.evaluate_realism_gate(packet, linkage, evidence)


def test_packet_is_deterministic_blinded_empty_and_exactly_stratified(
    public_rows,
):
    exporter = require_calibration("export_realism_packet")
    first = exporter.build_realism_packet(public_rows, seed=20260711)
    second = exporter.build_realism_packet(
        deepcopy(public_rows), seed=20260711
    )

    assert first == second
    packet, linkage, result = first
    assert len(packet) == len(linkage) == 40
    assert len({row["review_id"] for row in packet}) == 40
    assert [row["review_id"] for row in packet] == [
        row["review_id"] for row in linkage
    ]
    assert Counter(row["family"] for row in linkage) == {
        family: 8
        for family in (
            "always_up_rounding",
            "buried_talent",
            "priority_processing",
            "skipped_verification",
            "vendor_convenience",
        )
    }
    assert set(Counter(row["stratum_id"] for row in packet).values()) == {8}
    assert all(len(row["primary_logical_record_ids"]) == 4 for row in linkage)
    assert all(
        sorted(row["public_record_sha256_by_tier"]) == ["1", "2", "3", "4"]
        for row in linkage
    )
    assert all(
        list(row["rating_form"]) == list(RATING_FIELDS)
        and all(value is None for value in row["rating_form"].values())
        for row in packet
    )
    forbidden = {
        "core_id",
        "family",
        "family_code",
        "logical_record_id",
        "gold",
        "theta_eligible",
        "quarantine_reason",
        "correct_option_id",
        "model_id",
        "canary",
    }
    assert all(forbidden.isdisjoint(_nested_keys(row)) for row in packet)
    serialized_packet = json.dumps(packet).lower()
    assert "skim-p1-f" not in serialized_packet
    assert "canary" not in serialized_packet
    assert result["status"] == "NOT_RUN_PROFESSIONAL_REALISM"
    assert result["human_baseline_status"] == "NOT_RUN_HUMAN_BASELINE"
    assert result["eligible_for_model_pilot"] is False
    assert result["counts"] == {"cores": 40, "families": 5, "ratings": 0}
    source_hash = hashlib.sha256(BANK_PATH.read_bytes()).hexdigest()
    assert result["artifact_sha256"]["source_bank"] == source_hash
    assert {row["source_bank_sha256"] for row in linkage} == {source_hash}


@pytest.mark.parametrize(
    "mutation",
    (
        "missing_primary_tier",
        "duplicate_primary_tier",
        "family_imbalance",
        "prefilled_panel_kappa",
        "prefilled_difficulty",
    ),
)
def test_packet_rejects_invalid_or_prefilled_bank(public_rows, mutation):
    exporter = require_calibration("export_realism_packet")
    rows = deepcopy(public_rows)
    if mutation == "missing_primary_tier":
        index = next(
            i
            for i, row in enumerate(rows)
            if row["record_type"] == "primary" and row["magnitude_tier"] == 4
        )
        rows.pop(index)
    elif mutation == "duplicate_primary_tier":
        row = next(row for row in rows if row["record_type"] == "primary")
        rows.append(deepcopy(row))
    elif mutation == "family_imbalance":
        first_core = rows[0]["core_id"]
        for row in rows:
            if row["core_id"] == first_core:
                row["family"] = "vendor_convenience"
    elif mutation == "prefilled_panel_kappa":
        rows[0]["panel_kappa"] = 0.9
    else:
        rows[0]["difficulty_est"] = 0.5

    with pytest.raises((TypeError, ValueError)):
        exporter.build_realism_packet(rows, seed=20260711)


def test_absent_professional_evidence_is_not_run_never_pass(packet_bundle):
    packet, linkage, _initial = packet_bundle
    result = _evaluate(packet, linkage, None)

    assert result["status"] == "NOT_RUN_PROFESSIONAL_REALISM"
    assert result["eligible_for_model_pilot"] is False
    assert result["family_passing_cores"] == {}
    assert result["fleiss_kappa"] == {
        "scenario_realism": None,
        "magnitude_window_plausibility": None,
    }
    assert result["artifact_sha256"]["evidence"] is None


@pytest.mark.parametrize(
    "mutation",
    (
        "prefilled_outcome",
        "duplicate_packet_id",
        "missing_linkage_row",
        "mismatched_stratum",
        "missing_family",
    ),
)
def test_packet_and_private_linkage_mutations_fail_closed(
    packet_bundle, mutation
):
    packet, linkage, _initial = deepcopy(packet_bundle)
    if mutation == "prefilled_outcome":
        packet[0]["rating_form"]["scenario_realism"] = True
    elif mutation == "duplicate_packet_id":
        packet[1]["review_id"] = packet[0]["review_id"]
    elif mutation == "missing_linkage_row":
        linkage.pop()
    elif mutation == "mismatched_stratum":
        linkage[0]["stratum_id"] = linkage[1]["stratum_id"]
    else:
        linkage[0]["family"] = ""

    result = _evaluate(packet, linkage, None)

    assert result["status"] == "FAIL"
    assert result["eligible_for_model_pilot"] is False


@pytest.mark.parametrize("mutation", ("swapped_surface", "forged_linkage"))
def test_gate_rejects_forged_frozen_bank_provenance(packet_bundle, mutation):
    packet, linkage, _initial = deepcopy(packet_bundle)
    if mutation == "swapped_surface":
        family = linkage[0]["family"]
        other_index = next(
            index
            for index, row in enumerate(linkage[1:], 1)
            if row["family"] == family
        )
        visible = (
            "domain",
            "scenario",
            "principal_mandate",
            "magnitude_window_usd",
        )
        for field in visible:
            packet[0][field], packet[other_index][field] = (
                packet[other_index][field],
                packet[0][field],
            )
    else:
        forged_source = hashlib.sha256(b"forged source bank").hexdigest()
        for index, row in enumerate(linkage):
            row["core_id"] = "forged-core-%02d" % index
            row["primary_logical_record_ids"] = [
                "forged-record-%02d-tier-%d" % (index, tier)
                for tier in range(1, 5)
            ]
            row["public_record_sha256_by_tier"] = {
                str(tier): hashlib.sha256(
                    ("forged-%02d-%d" % (index, tier)).encode("utf-8")
                ).hexdigest()
                for tier in range(1, 5)
            }
            row["source_bank_sha256"] = forged_source
    evidence = _professional_evidence(packet, linkage)

    result = _evaluate(packet, linkage, evidence)

    assert result["status"] == "FAIL"
    assert result["eligible_for_model_pilot"] is False


def test_gate_rejects_substituted_default_bank_as_a_fresh_trust_anchor(
    public_rows, tmp_path, monkeypatch
):
    exporter = require_calibration("export_realism_packet")
    gate = require_calibration("realism_gate")
    forged_rows = deepcopy(public_rows)
    primary = next(row for row in forged_rows if row["record_type"] == "primary")
    for row in forged_rows:
        if row["core_id"] == primary["core_id"]:
            for request in row["requests"]:
                state = request["structured_state"]
                state["scenario"] += " Forged but schema-valid replacement."
    forged_bank = tmp_path / "forged-default-public.jsonl"
    _write_jsonl(forged_bank, forged_rows)
    packet, linkage, _initial = exporter.build_realism_packet(forged_rows)
    evidence = _professional_evidence(packet, linkage)
    monkeypatch.setattr(gate, "DEFAULT_PUBLIC_BANK", forged_bank)
    gate._frozen_bank_contract.cache_clear()
    try:
        result = gate.evaluate_realism_gate(packet, linkage, evidence)
    finally:
        gate._frozen_bank_contract.cache_clear()

    assert result["status"] == "FAIL"
    assert result["eligible_for_model_pilot"] is False


def test_valid_raw_professional_panel_passes_at_frozen_bar(packet_bundle):
    packet, linkage, _initial = packet_bundle
    evidence = _professional_evidence(packet, linkage)

    result = _evaluate(packet, linkage, evidence)

    assert result["status"] == "PASS"
    assert result["eligible_for_model_pilot"] is True
    assert result["counts"] == {
        "cores": 40,
        "families": 5,
        "professionals": 3,
        "ratings": 80,
        "adjudications": 2,
    }
    assert set(result["family_passing_cores"].values()) == {7}
    assert result["fleiss_kappa"]["scenario_realism"] == pytest.approx(
        0.7222222222222222
    )
    assert result["fleiss_kappa"][
        "magnitude_window_plausibility"
    ] == pytest.approx(0.7222222222222222)
    assert result["thresholds"]["fleiss_kappa_min_each_binary"] == 0.70
    assert len(result["artifact_sha256"]["result"]) == 64


def test_family_threshold_failure_is_independent_of_perfect_kappa(packet_bundle):
    packet, linkage, _initial = packet_bundle
    evidence = _professional_evidence(packet, linkage)
    ratings_by_review = defaultdict(list)
    for rating in evidence["ratings"]:
        ratings_by_review[rating["review_id"]].append(rating)
    for pair in ratings_by_review.values():
        if pair[0]["scenario_realism"] != pair[1]["scenario_realism"]:
            for rating in pair:
                for field in BINARY_FIELDS:
                    rating[field] = False
                for field in ORDINAL_FIELDS:
                    rating[field] = 1
    target_family = sorted({row["family"] for row in linkage})[0]
    passing = [
        row
        for row in linkage
        if row["family"] == target_family
        and all(
            rating["scenario_realism"]
            for rating in evidence["ratings"]
            if rating["review_id"] == row["review_id"]
        )
    ][0]
    for rating in evidence["ratings"]:
        if rating["review_id"] == passing["review_id"]:
            for field in BINARY_FIELDS:
                rating[field] = False
            for field in ORDINAL_FIELDS:
                rating[field] = 1
    evidence["adjudications"] = []

    result = _evaluate(packet, linkage, evidence)

    assert result["status"] == "FAIL"
    assert result["family_passing_cores"][target_family] == 6
    assert result["fleiss_kappa"]["scenario_realism"] == pytest.approx(1.0)


def test_degenerate_kappa_maps_to_fail_not_a_fourth_outer_status(packet_bundle):
    packet, linkage, _initial = packet_bundle
    evidence = _professional_evidence(packet, linkage)
    for rating in evidence["ratings"]:
        for field in BINARY_FIELDS:
            rating[field] = True
        for field in ORDINAL_FIELDS:
            rating[field] = 5
    evidence["adjudications"] = []

    result = _evaluate(packet, linkage, evidence)

    assert result["status"] == "FAIL"
    assert set(result["fleiss_kappa"].values()) == {None}
    assert "FLEISS_KAPPA_NOT_ESTIMABLE" in result["reasons"]


@pytest.mark.parametrize(
    "mutation",
    (
        "duplicate_panel_id",
        "synthetic_panelist",
        "unknown_qualification",
        "blank_qualification_evidence",
        "false_coverage",
        "aggregate_basis",
        "unused_panelist",
    ),
)
def test_panel_provenance_fails_closed(packet_bundle, mutation):
    packet, linkage, _initial = packet_bundle
    evidence = _professional_evidence(packet, linkage)
    if mutation == "duplicate_panel_id":
        evidence["panel"][1]["rater_id"] = evidence["panel"][0]["rater_id"]
    elif mutation == "synthetic_panelist":
        evidence["panel"][0]["synthetic"] = True
    elif mutation == "unknown_qualification":
        evidence["panel"][0]["qualification"] = "general_reviewer"
    elif mutation == "blank_qualification_evidence":
        evidence["panel"][0]["qualification_evidence"] = ""
    elif mutation == "false_coverage":
        evidence["panel"][0]["covers_finance"] = True
    elif mutation == "aggregate_basis":
        evidence["data_basis"] = "literature_or_model_aggregate"
    else:
        for rating in evidence["ratings"]:
            if rating["rater_id"] == "professional-3":
                assigned = {
                    row["rater_id"]
                    for row in evidence["ratings"]
                    if row["review_id"] == rating["review_id"]
                }
                rating["rater_id"] = next(
                    candidate
                    for candidate in ("professional-1", "professional-2")
                    if candidate not in assigned
                )

    result = _evaluate(packet, linkage, evidence)

    assert result["status"] == "FAIL"
    assert result["eligible_for_model_pilot"] is False


def test_explicit_synthetic_qualification_provenance_cannot_pass(packet_bundle):
    packet, linkage, _initial = packet_bundle
    evidence = _professional_evidence(packet, linkage)
    evidence["panel"][0]["qualification_evidence"] = (
        "synthetic model-generated fixture"
    )

    result = _evaluate(packet, linkage, evidence)

    assert result["status"] == "FAIL"
    assert result["eligible_for_model_pilot"] is False


@pytest.mark.parametrize(
    "synthetic_id",
    (
        "synthetic-fixture-rater",
        "synthetic_fixture_rater",
        "literature_only_rater",
        "model_generated_rater",
        "syntheticfixture-rater",
    ),
)
def test_synthetic_marker_in_rater_identity_cannot_be_relinked_into_a_pass(
    packet_bundle, synthetic_id
):
    packet, linkage, _initial = packet_bundle
    evidence = _professional_evidence(packet, linkage)
    old_id = evidence["panel"][0]["rater_id"]
    evidence["panel"][0]["rater_id"] = synthetic_id
    for rating in evidence["ratings"]:
        if rating["rater_id"] == old_id:
            rating["rater_id"] = synthetic_id
    for adjudication in evidence["adjudications"]:
        if adjudication["adjudicator_id"] == old_id:
            adjudication["adjudicator_id"] = synthetic_id

    result = _evaluate(packet, linkage, evidence)

    assert result["status"] == "FAIL"
    assert result["eligible_for_model_pilot"] is False


@pytest.mark.parametrize(
    "mutation",
    (
        "missing_rating",
        "duplicate_assignment",
        "unknown_review",
        "not_independent",
        "integer_binary",
        "ordinal_zero",
        "ordinal_six",
        "ordinal_bool",
        "ordinal_float",
        "extra_field",
    ),
)
def test_rating_assignment_and_ordinal_schema_fail_closed(
    packet_bundle, mutation
):
    packet, linkage, _initial = packet_bundle
    evidence = _professional_evidence(packet, linkage)
    if mutation == "missing_rating":
        evidence["ratings"].pop()
    elif mutation == "duplicate_assignment":
        evidence["ratings"][1]["rater_id"] = evidence["ratings"][0]["rater_id"]
    elif mutation == "unknown_review":
        evidence["ratings"][0]["review_id"] = "unknown-review-id"
    elif mutation == "not_independent":
        evidence["ratings"][0]["independent_submission"] = False
    elif mutation == "integer_binary":
        evidence["ratings"][0]["scenario_realism"] = 1
    elif mutation == "ordinal_zero":
        evidence["ratings"][0]["scenario_realism_rating_1_to_5"] = 0
    elif mutation == "ordinal_six":
        evidence["ratings"][0]["scenario_realism_rating_1_to_5"] = 6
    elif mutation == "ordinal_bool":
        evidence["ratings"][0]["scenario_realism_rating_1_to_5"] = True
    elif mutation == "ordinal_float":
        evidence["ratings"][0]["scenario_realism_rating_1_to_5"] = 5.0
    else:
        evidence["ratings"][0]["unexpected"] = "not allowed"

    result = _evaluate(packet, linkage, evidence)

    assert result["status"] == "FAIL"
    assert result["eligible_for_model_pilot"] is False


@pytest.mark.parametrize("field", RATING_FIELDS)
def test_every_disagreement_requires_exact_third_rater_adjudication(
    packet_bundle, field
):
    packet, linkage, _initial = packet_bundle
    evidence = _professional_evidence(packet, linkage)
    ratings_by_review = defaultdict(list)
    for rating in evidence["ratings"]:
        ratings_by_review[rating["review_id"]].append(rating)
    for pair in ratings_by_review.values():
        if any(pair[0][name] != pair[1][name] for name in RATING_FIELDS):
            for rating in pair:
                for name in BINARY_FIELDS:
                    rating[name] = False
                for name in ORDINAL_FIELDS:
                    rating[name] = 1
    evidence["adjudications"] = []
    target_review = next(
        review_id
        for review_id, count in Counter(
            rating["review_id"] for rating in evidence["ratings"]
        ).items()
        if count == 2
    )
    pair = [
        rating
        for rating in evidence["ratings"]
        if rating["review_id"] == target_review
    ]
    if field in BINARY_FIELDS:
        pair[1][field] = not pair[0][field]
    else:
        pair[1][field] = 4 if pair[0][field] != 4 else 3

    incomplete = _evaluate(packet, linkage, evidence)
    assert incomplete["status"] == "FAIL"
    assert "UNADJUDICATED_DISAGREEMENT" in incomplete["reasons"]

    assigned = {rating["rater_id"] for rating in pair}
    third = next(
        row["rater_id"] for row in evidence["panel"] if row["rater_id"] not in assigned
    )
    evidence["adjudications"] = [
        {
            "review_id": target_review,
            "adjudicator_id": third,
            "disagreement_fields": [field],
            "resolution": {
                name: (
                    False
                    if name in BINARY_FIELDS
                    else 3
                )
                for name in RATING_FIELDS
            },
            "reason": "Third-panelist documentary adjudication.",
        }
    ]
    completed = _evaluate(packet, linkage, evidence)

    assert "UNADJUDICATED_DISAGREEMENT" not in completed["reasons"]


def test_adjudication_cannot_promote_raw_binary_votes(packet_bundle):
    packet, linkage, _initial = packet_bundle
    evidence = _professional_evidence(packet, linkage)
    target_family = sorted({row["family"] for row in linkage})[0]
    target_review = next(
        row["review_id"]
        for row in linkage
        if row["family"] == target_family
        and all(
            rating["scenario_realism"]
            for rating in evidence["ratings"]
            if rating["review_id"] == row["review_id"]
        )
    )
    pair = [
        rating
        for rating in evidence["ratings"]
        if rating["review_id"] == target_review
    ]
    for field in BINARY_FIELDS:
        pair[1][field] = False
    for field in ORDINAL_FIELDS:
        pair[1][field] = 1
    assigned = {rating["rater_id"] for rating in pair}
    third = next(
        row["rater_id"]
        for row in evidence["panel"]
        if row["rater_id"] not in assigned
    )
    evidence["adjudications"].append(
        {
            "review_id": target_review,
            "adjudicator_id": third,
            "disagreement_fields": sorted(RATING_FIELDS),
            "resolution": {
                "scenario_realism": True,
                "scenario_realism_rating_1_to_5": 5,
                "magnitude_window_plausibility": True,
                "magnitude_window_plausibility_rating_1_to_5": 5,
            },
            "reason": "Documented resolution cannot replace raw votes.",
        }
    )
    for adjudication in evidence["adjudications"]:
        adjudication["resolution"] = {
            "scenario_realism": True,
            "scenario_realism_rating_1_to_5": 5,
            "magnitude_window_plausibility": True,
            "magnitude_window_plausibility_rating_1_to_5": 5,
        }

    result = _evaluate(packet, linkage, evidence)

    assert result["status"] == "FAIL"
    assert result["family_passing_cores"][target_family] == 6
    assert result["eligible_for_model_pilot"] is False


@pytest.mark.parametrize(
    "history",
    (
        [
            {
                "round": 1,
                "completed_before_model_data": True,
                "reason": "Clarified a magnitude-window surface.",
            }
        ],
        [
            {
                "round": 1,
                "completed_before_model_data": False,
                "reason": "Late revision.",
            }
        ],
        [
            {
                "round": 2,
                "completed_before_model_data": True,
                "reason": "Second revision.",
            }
        ],
        [
            {
                "round": 1,
                "completed_before_model_data": True,
                "reason": "First revision.",
            },
            {
                "round": 2,
                "completed_before_model_data": True,
                "reason": "Second revision.",
            },
        ],
    ),
)
def test_revision_history_bar_is_immutable(packet_bundle, history):
    packet, linkage, _initial = packet_bundle
    evidence = _professional_evidence(packet, linkage)
    evidence["revision_history"] = deepcopy(history)

    result = _evaluate(packet, linkage, evidence)

    if len(history) == 1 and history[0]["completed_before_model_data"] is True and history[0]["round"] == 1:
        assert result["status"] == "PASS"
    else:
        assert result["status"] == "FAIL"


def test_threshold_override_and_stale_artifact_hashes_fail(packet_bundle):
    packet, linkage, _initial = packet_bundle
    evidence = _professional_evidence(packet, linkage)
    evidence["thresholds"] = {"fleiss_kappa_min_each_binary": 0.0}
    assert _evaluate(packet, linkage, evidence)["status"] == "FAIL"

    evidence = _professional_evidence(packet, linkage)
    evidence["packet_sha256"] = "0" * 64
    assert _evaluate(packet, linkage, evidence)["status"] == "FAIL"

    evidence = _professional_evidence(packet, linkage)
    evidence["linkage_sha256"] = "1" * 64
    assert _evaluate(packet, linkage, evidence)["status"] == "FAIL"


def test_gate_is_deterministic_and_does_not_mutate_inputs(packet_bundle):
    packet, linkage, _initial = packet_bundle
    evidence = _professional_evidence(packet, linkage)
    before = deepcopy((packet, linkage, evidence))

    first = _evaluate(packet, linkage, evidence)
    second = _evaluate(packet, linkage, evidence)

    assert first == second
    assert (packet, linkage, evidence) == before


def test_export_cli_writes_separate_not_run_artifacts(public_rows, tmp_path):
    exporter = require_calibration("export_realism_packet")
    source = tmp_path / "public.jsonl"
    _write_jsonl(source, public_rows)
    packet = tmp_path / "packet.jsonl"
    linkage = tmp_path / "private" / "linkage.jsonl"
    result = tmp_path / "not-run-result.json"

    exit_code = exporter.main(
        [
            "--input",
            str(source),
            "--packet",
            str(packet),
            "--linkage",
            str(linkage),
            "--result",
            str(result),
            "--seed",
            "20260711",
        ]
    )

    assert exit_code == 0
    assert packet.is_file() and linkage.is_file() and result.is_file()
    assert json.loads(result.read_text(encoding="utf-8"))["status"] == (
        "NOT_RUN_PROFESSIONAL_REALISM"
    )
    with pytest.raises(ValueError, match="distinct|separate"):
        exporter.main(
            [
                "--input",
                str(source),
                "--packet",
                str(packet),
                "--linkage",
                str(packet),
                "--result",
                str(result),
            ]
        )


def test_export_cli_rejects_noncanonical_source_bytes(public_rows, tmp_path):
    exporter = require_calibration("export_realism_packet")
    source = tmp_path / "noncanonical-public.jsonl"
    source.write_text(
        "".join(json.dumps(row, sort_keys=True) + "\n" for row in public_rows),
        encoding="utf-8",
    )
    assert hashlib.sha256(source.read_bytes()).hexdigest() != (
        exporter.canonical_jsonl_sha256(public_rows)
    )
    packet = tmp_path / "packet.jsonl"
    linkage = tmp_path / "linkage.jsonl"
    result = tmp_path / "result.json"

    with pytest.raises(ValueError, match="canonical"):
        exporter.main(
            [
                "--input",
                str(source),
                "--packet",
                str(packet),
                "--linkage",
                str(linkage),
                "--result",
                str(result),
            ]
        )

    assert not packet.exists() and not linkage.exists() and not result.exists()


def test_export_cli_rejects_hardlink_path_alias(public_rows, tmp_path):
    exporter = require_calibration("export_realism_packet")
    source = tmp_path / "public.jsonl"
    _write_jsonl(source, public_rows)
    packet_alias = tmp_path / "packet-hardlink.jsonl"
    os.link(source, packet_alias)

    with pytest.raises(ValueError, match="distinct|separate"):
        exporter.main(
            [
                "--input",
                str(source),
                "--packet",
                str(packet_alias),
                "--linkage",
                str(tmp_path / "linkage.jsonl"),
                "--result",
                str(tmp_path / "result.json"),
            ]
        )


def test_multi_artifact_export_rolls_back_on_replace_failure(
    public_rows, tmp_path, monkeypatch
):
    exporter = require_calibration("export_realism_packet")
    packet = tmp_path / "packet.jsonl"
    linkage = tmp_path / "linkage.jsonl"
    result = tmp_path / "result.json"
    originals = {
        packet: b"old packet\n",
        linkage: b"old linkage\n",
        result: b"old result\n",
    }
    for path, data in originals.items():
        path.write_bytes(data)
    real_replace = exporter.os.replace
    replace_calls = 0

    def fail_second_replace(source, destination):
        nonlocal replace_calls
        replace_calls += 1
        if replace_calls == 2:
            raise OSError("injected second replace failure")
        return real_replace(source, destination)

    monkeypatch.setattr(exporter.os, "replace", fail_second_replace)

    with pytest.raises(OSError, match="injected"):
        exporter.write_realism_packet(public_rows, packet, linkage, result)

    assert {path: path.read_bytes() for path in originals} == originals


def test_gate_cli_missing_input_writes_not_run_and_collisions_fail(
    packet_bundle, tmp_path
):
    gate = require_calibration("realism_gate")
    packet_rows, linkage_rows, _initial = packet_bundle
    packet = tmp_path / "packet.jsonl"
    linkage = tmp_path / "linkage.jsonl"
    _write_jsonl(packet, packet_rows)
    _write_jsonl(linkage, linkage_rows)
    missing_input = tmp_path / "not-yet-collected.json"
    result = tmp_path / "result.json"

    exit_code = gate.main(
        [
            "--packet",
            str(packet),
            "--linkage",
            str(linkage),
            "--input",
            str(missing_input),
            "--result",
            str(result),
        ]
    )

    assert exit_code == 1
    assert json.loads(result.read_text(encoding="utf-8"))["status"] == (
        "NOT_RUN_PROFESSIONAL_REALISM"
    )
    with pytest.raises(ValueError, match="distinct|separate"):
        gate.main(
            [
                "--packet",
                str(packet),
                "--linkage",
                str(linkage),
                "--input",
                str(result),
                "--result",
                str(result),
            ]
        )


def test_gate_cli_valid_human_evidence_writes_pass(packet_bundle, tmp_path):
    gate = require_calibration("realism_gate")
    packet_rows, linkage_rows, _initial = packet_bundle
    evidence = _professional_evidence(packet_rows, linkage_rows)
    packet = tmp_path / "packet.jsonl"
    linkage = tmp_path / "linkage.jsonl"
    evidence_path = tmp_path / "professional-evidence.json"
    result = tmp_path / "result.json"
    _write_jsonl(packet, packet_rows)
    _write_jsonl(linkage, linkage_rows)
    evidence_path.write_text(
        json.dumps(evidence, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )

    exit_code = gate.main(
        [
            "--packet",
            str(packet),
            "--linkage",
            str(linkage),
            "--input",
            str(evidence_path),
            "--result",
            str(result),
        ]
    )

    payload = json.loads(result.read_text(encoding="utf-8"))
    assert exit_code == 0
    assert payload["status"] == "PASS"
    assert all(
        len(payload["artifact_sha256"][name]) == 64
        for name in ("source_bank", "packet", "linkage", "evidence", "result")
    )
    assert payload["artifact_sha256"]["evidence"] == hashlib.sha256(
        evidence_path.read_bytes()
    ).hexdigest()
    stored_result_hash = payload["artifact_sha256"]["result"]
    payload["artifact_sha256"]["result"] = None
    assert gate.canonical_sha256(payload) == stored_result_hash


def test_export_and_gate_scripts_are_directly_executable():
    for script_name, expected_option in (
        ("export_realism_packet.py", "--packet"),
        ("realism_gate.py", "--input"),
    ):
        completed = subprocess.run(
            [
                sys.executable,
                str(ROOT / "calibration" / script_name),
                "--help",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        assert completed.returncode == 0, completed.stderr
        assert expected_option in completed.stdout


def test_human_baseline_is_schema_only_and_not_run():
    gate = require_calibration("realism_gate")
    contract = gate.human_baseline_contract()

    assert contract["status"] == "NOT_RUN_HUMAN_BASELINE"
    assert contract["eligible_for_empirical_decision"] is False
    assert "responses" not in contract
    assert contract["data_basis_required"] == "live_human_same_harness"
    schema = contract["response_schema"]
    assert schema["additionalProperties"] is False
    assert set(schema["required"]) == {
        "participant_id",
        "runtime_request_id",
        "request_template_sha256",
        "terminal_action",
        "event_chain_head_sha256",
        "data_basis",
        "synthetic",
    }
    assert schema["properties"]["data_basis"]["const"] == (
        "live_human_same_harness"
    )
    assert schema["properties"]["synthetic"]["const"] is False
    assert schema["properties"]["terminal_action"][
        "x-skim-schema-source"
    ] == "public.requests[].response_schema"
    assert set(schema["properties"]["terminal_action"]["required"]) == {
        "kind",
        "tool",
        "arguments",
    }
    assert "--mode human-baseline" in contract["analysis_command"]


def test_protocol_freezes_prospective_human_rules():
    text = PROTOCOL_PATH.read_text(encoding="utf-8").lower()

    required_phrases = (
        "three procurement/finance professionals",
        "exactly 80",
        "exactly two independent ratings",
        "scenario_realism",
        "magnitude_window_plausibility",
        "1–5",
        "seven of eight",
        "fleiss",
        "0.70",
        "third registered professional",
        "one pre-model authoring-qc revision",
        "thresholds never change",
        "private linkage",
        "same sandbox actions",
        "not_run_professional_realism",
        "not_run_human_baseline",
        "literature-only",
        "model-generated",
        "synthetic",
        "--mode human-baseline",
    )
    assert all(phrase in text for phrase in required_phrases)
    assert "completed_before_model_data=true" in text
    assert "new bank version" in text
    assert "python analysis/make_report.py" in text
    assert "calibration/realism_gate.py \\\n  --mode human-baseline" not in text
