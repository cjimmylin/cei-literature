from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys

from jsonschema import Draft202012Validator, ValidationError
import pytest
import yaml

import biblebench_pilot.adjudication as adjudication
from biblebench_pilot.adjudication import (
    build_review_packet,
    export_review_packet,
    roll_up_owner_decisions,
    validate_review_packet,
)


PACKAGE_ROOT = Path(__file__).parents[1]
SCHEMA_PATH = PACKAGE_ROOT / "schemas" / "provisional-gold-review.schema.json"
MODULES = (
    "fruitbench",
    "corinthlove",
    "tencommandments",
    "sermonmount",
)


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _load_banks() -> dict[str, dict]:
    return {
        module: yaml.safe_load(
            (PACKAGE_ROOT / "modules" / module / "episodes.yaml").read_text(
                encoding="utf-8"
            )
        )
        for module in MODULES
    }


def test_build_review_packet_validates_four_banks_and_links_48_records() -> None:
    packet = build_review_packet(PACKAGE_ROOT)
    banks = _load_banks()
    authored_by_id = {
        row["episode_id"]: row
        for bank in banks.values()
        for row in bank["episodes"]
    }

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(packet)

    records = packet["records"]
    assert len(records) == 48
    assert len({record["episode_id"] for record in records}) == 48
    assert {record["module"] for record in records} == set(MODULES)
    for record in records:
        authored = authored_by_id[record["episode_id"]]
        assert record["authored_episode_sha256"] == _canonical_sha256(authored)


def test_review_surfaces_are_lossless_pending_and_pre_model() -> None:
    packet = build_review_packet(PACKAGE_ROOT)
    banks = _load_banks()
    authored_by_id = {
        row["episode_id"]: row
        for bank in banks.values()
        for row in bank["episodes"]
    }

    assert packet["classification"] == "single_expert_provisional_gold"
    assert packet["owner_review_status"] == "pending"
    for record in packet["records"]:
        authored = authored_by_id[record["episode_id"]]
        assert record["provenance"] == {
            "passage_anchors": authored["passage_anchors"],
            "source_artifacts": authored["source_artifacts"],
        }
        assert record["observable_criteria"] == {
            "affected_parties": authored["affected_parties"],
            "authority_boundary": authored["authority_boundary"],
            "acceptable_action_band": authored["acceptable_action_band"],
            "prohibited_actions": authored["prohibited_actions"],
            "deficient_pole": authored["deficient_pole"],
            "counterfeit_pole": authored["counterfeit_pole"],
            "red_line_classes": authored["red_line_classes"],
            "terminal_observables": authored["execution_contract"][
                "terminal_observables"
            ],
            "repair_expectations": authored["repair_expectations"],
        }
        assert record["behavioral_attribution"] == authored["behavioral_attribution"]
        assert record["judge_confidence"] == authored["judge_confidence"]
        assert record["contestability"] == authored["contestability"]
        assert record["review_payload"] == authored
        assert record["review_payload_sha256"] == _canonical_sha256(authored)
        assert record["review_payload_sha256"] == record["authored_episode_sha256"]
        assert record["classification"] == "single_expert_provisional_gold"
        assert record["owner_review_status"] == "pending"
        assert record["owner_behavior_decision"] is None
        assert record["owner_interpretive_decision"] is None
        assert record["owner_record_decision"] is None
        assert record["owner_behavior_rationale"] is None
        assert record["owner_interpretive_rationale"] is None
        assert record["owner_confidence"] is None
        assert record["owner_contestability"] is None
        assert record["owner_issues"] is None
        assert record["owner_judge_id"] is None
        assert record["owner_notes"] is None
        assert record["owner_reviewed_at"] is None
        assert "owner_label" not in record

    assert packet["owner_judge"] is None
    assert packet["owner_completed_at"] is None

    serialized = json.dumps(packet, sort_keys=True).casefold()
    assert "model_output" not in serialized
    assert "model_response" not in serialized


def test_dual_track_routing_is_explicit_without_prefilling_owner_decisions() -> None:
    records = {
        record["episode_id"]: record
        for record in build_review_packet(PACKAGE_ROOT)["records"]
    }

    common_life = records["F01-TARGET-01"]
    assert common_life["track_applicability"] == {
        "behavior": "applicable",
        "interpretive": "not_applicable",
    }

    interpretive_only = records["T01-TARGET-01"]
    assert interpretive_only["behavioral_attribution"] == (
        "not_behaviorally_attributable"
    )
    assert interpretive_only["track_applicability"] == {
        "behavior": "not_applicable",
        "interpretive": "applicable",
    }

    dual_track = records["L04-NULL-01"]
    assert dual_track["track_applicability"] == {
        "behavior": "applicable",
        "interpretive": "applicable",
    }

    for record in records.values():
        assert record["owner_behavior_decision"] is None
        assert record["owner_interpretive_decision"] is None
        assert record["owner_record_decision"] is None


def test_packet_registers_immutable_dual_track_rollup_rule() -> None:
    packet = build_review_packet(PACKAGE_ROOT)

    assert packet["owner_record_rollup_rule"] == {
        "version": "dual-track-rollup-v1",
        "behavior_decision_field": "owner_behavior_decision",
        "interpretive_decision_field": "owner_interpretive_decision",
        "record_decision_field": "owner_record_decision",
        "applicable_track_decisions": ["APPROVE", "REVISE", "REJECT", "DEFER"],
        "not_applicable_value": "NOT_APPLICABLE",
        "not_applicable_handling": "ignored",
        "precedence": ["DEFER", "REJECT", "REVISE", "APPROVE"],
        "no_applicable_tracks_result": "DEFER",
    }


def test_schema_rejects_prefilled_owner_decision_while_record_is_pending() -> None:
    packet = build_review_packet(PACKAGE_ROOT)
    packet["records"][0]["owner_behavior_decision"] = "APPROVE"
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

    with pytest.raises(ValidationError):
        Draft202012Validator(schema).validate(packet)


def test_validation_rejects_tampered_embedded_review_payload() -> None:
    packet = build_review_packet(PACKAGE_ROOT)
    packet["records"][0]["review_payload"]["scenario"] = "tampered"

    with pytest.raises(ValueError, match="review_payload.*frozen authored episode"):
        validate_review_packet(packet, PACKAGE_ROOT)


def test_validation_rejects_coordinated_payload_and_hash_tamper() -> None:
    packet = build_review_packet(PACKAGE_ROOT)
    record = packet["records"][0]
    record["review_payload"]["scenario"] = (
        "Coordinated tamper that changes the frozen scenario."
    )
    tampered_sha256 = _canonical_sha256(record["review_payload"])
    record["review_payload_sha256"] = tampered_sha256
    record["authored_episode_sha256"] = tampered_sha256

    with pytest.raises(ValueError, match="frozen authored episode"):
        validate_review_packet(packet, PACKAGE_ROOT)


def test_validation_rejects_source_schema_hash_tamper() -> None:
    packet = build_review_packet(PACKAGE_ROOT)
    packet["source_bank_schema_sha256"] = "0" * 64

    with pytest.raises(ValueError, match="source_bank_schema_sha256"):
        validate_review_packet(packet, PACKAGE_ROOT)


@pytest.mark.parametrize(
    ("field", "tampered_value"),
    [
        ("module", "sermonmount"),
        ("path", "modules/sermonmount/episodes.yaml"),
        ("file_sha256", "0" * 64),
        ("canonical_sha256", "1" * 64),
    ],
)
def test_validation_rejects_source_bank_metadata_tamper(
    field: str, tampered_value: str
) -> None:
    packet = build_review_packet(PACKAGE_ROOT)
    packet["source_banks"][0][field] = tampered_value

    with pytest.raises(ValueError, match="source_banks metadata"):
        validate_review_packet(packet, PACKAGE_ROOT)


@pytest.mark.parametrize(
    ("field", "tampered_value"),
    [("module", "sermonmount"), ("episode_id", "F02-NULL-01")],
)
def test_validation_rejects_record_identity_tamper(
    field: str, tampered_value: str
) -> None:
    packet = build_review_packet(PACKAGE_ROOT)
    packet["records"][0][field] = tampered_value

    with pytest.raises(ValueError, match="frozen authored episode identity"):
        validate_review_packet(packet, PACKAGE_ROOT)


def test_validation_rejects_outer_observable_criteria_tamper() -> None:
    packet = build_review_packet(PACKAGE_ROOT)
    packet["records"][0]["observable_criteria"]["authority_boundary"] = (
        "Tampered outer authority boundary that leaves the frozen payload unchanged."
    )

    with pytest.raises(ValueError, match="non-owner field.*observable_criteria"):
        validate_review_packet(packet, PACKAGE_ROOT)


def test_validation_rejects_outer_track_routing_tamper() -> None:
    packet = build_review_packet(PACKAGE_ROOT)
    packet["records"][0]["track_applicability"]["behavior"] = "not_applicable"

    with pytest.raises(ValueError, match="non-owner field.*track_applicability"):
        validate_review_packet(packet, PACKAGE_ROOT)


def _complete_record_review(record: dict) -> None:
    record["owner_review_status"] = "reviewed"
    record["owner_behavior_decision"] = (
        "APPROVE"
        if record["track_applicability"]["behavior"] == "applicable"
        else "NOT_APPLICABLE"
    )
    record["owner_interpretive_decision"] = (
        "APPROVE"
        if record["track_applicability"]["interpretive"] == "applicable"
        else "NOT_APPLICABLE"
    )
    record["owner_record_decision"] = roll_up_owner_decisions(
        record["owner_behavior_decision"], record["owner_interpretive_decision"]
    )
    record["owner_behavior_rationale"] = "Behavior routing and geometry are adequate."
    record["owner_interpretive_rationale"] = (
        "Interpretive routing and geometry are adequate."
    )
    record["owner_confidence"] = "high"
    record["owner_contestability"] = "clear"
    record["owner_issues"] = []
    record["owner_judge_id"] = "jimmy_lin"
    record["owner_reviewed_at"] = "2026-07-13T17:00:00Z"


def _complete_all_record_reviews(packet: dict) -> None:
    for record in packet["records"]:
        _complete_record_review(record)


def test_reviewed_record_requires_rationales_confidence_contestability_and_identity() -> None:
    packet = build_review_packet(PACKAGE_ROOT)
    _complete_record_review(packet["records"][0])

    validate_review_packet(packet, PACKAGE_ROOT)


def test_p1_issue_prevents_owner_record_approval() -> None:
    packet = build_review_packet(PACKAGE_ROOT)
    record = packet["records"][0]
    _complete_record_review(record)
    record["owner_issues"] = [
        {
            "issue_id": "F01-P1-AUTHORITY",
            "priority": "P1",
            "track": "behavior",
            "summary": "Authority boundary may change the expected action.",
            "affected_fields": ["authority_boundary"],
            "repair_condition": "Narrow the authority boundary and re-review the episode.",
        }
    ]

    with pytest.raises(ValueError, match="P1.*behavior.*REVISE or DEFER"):
        validate_review_packet(packet, PACKAGE_ROOT)


@pytest.mark.parametrize(
    (
        "priority",
        "issue_track",
        "behavior_decision",
        "interpretive_decision",
        "record_decision",
    ),
    [
        ("P0", "behavior", "APPROVE", "DEFER", "DEFER"),
        ("P0", "interpretive", "DEFER", "APPROVE", "DEFER"),
        ("P1", "behavior", "APPROVE", "REVISE", "REVISE"),
        ("P1", "interpretive", "REVISE", "APPROVE", "REVISE"),
        ("P1", "record", "REJECT", "APPROVE", "REJECT"),
        ("P1", "custody", "REJECT", "APPROVE", "REJECT"),
    ],
)
def test_issue_priority_constrains_affected_track_before_rollup(
    priority: str,
    issue_track: str,
    behavior_decision: str,
    interpretive_decision: str,
    record_decision: str,
) -> None:
    packet = build_review_packet(PACKAGE_ROOT)
    record = next(
        record
        for record in packet["records"]
        if record["track_applicability"]
        == {"behavior": "applicable", "interpretive": "applicable"}
    )
    _complete_record_review(record)
    record["owner_behavior_decision"] = behavior_decision
    record["owner_interpretive_decision"] = interpretive_decision
    record["owner_record_decision"] = record_decision
    record["owner_issues"] = [
        {
            "issue_id": f"TRACK-{priority}-{issue_track.upper()}",
            "priority": priority,
            "track": issue_track,
            "summary": "Material issue on the specifically affected adjudication track.",
            "affected_fields": ["authority_boundary"],
            "repair_condition": "Repair the affected track and re-review the frozen episode.",
        }
    ]

    with pytest.raises(ValueError, match=f"{priority}.*{issue_track}.*decision"):
        validate_review_packet(packet, PACKAGE_ROOT)


@pytest.mark.parametrize(
    (
        "owner_confidence",
        "owner_contestability",
        "behavior_decision",
        "interpretive_decision",
        "record_decision",
        "message",
    ),
    [
        ("low", "clear", "APPROVE", "APPROVE", "APPROVE", "low confidence"),
        ("low", "clear", "REJECT", "APPROVE", "REJECT", "low confidence"),
        (
            "high",
            "outside_competence",
            "REVISE",
            "APPROVE",
            "REVISE",
            "outside competence",
        ),
    ],
)
def test_owner_uncertainty_constrains_record_decision(
    owner_confidence: str,
    owner_contestability: str,
    behavior_decision: str,
    interpretive_decision: str,
    record_decision: str,
    message: str,
) -> None:
    packet = build_review_packet(PACKAGE_ROOT)
    record = next(
        record
        for record in packet["records"]
        if record["track_applicability"]
        == {"behavior": "applicable", "interpretive": "applicable"}
    )
    _complete_record_review(record)
    record["owner_confidence"] = owner_confidence
    record["owner_contestability"] = owner_contestability
    record["owner_behavior_decision"] = behavior_decision
    record["owner_interpretive_decision"] = interpretive_decision
    record["owner_record_decision"] = record_decision

    with pytest.raises(ValueError, match=message):
        validate_review_packet(packet, PACKAGE_ROOT)


def test_reviewed_revise_can_be_saved_while_packet_remains_pending() -> None:
    packet = build_review_packet(PACKAGE_ROOT)
    record = packet["records"][0]
    _complete_record_review(record)
    record["owner_behavior_decision"] = "REVISE"
    record["owner_record_decision"] = "REVISE"
    record["owner_issues"] = [
        {
            "issue_id": "F01-P1-REPAIR",
            "priority": "P1",
            "track": "behavior",
            "summary": "The action band needs a material bounded revision.",
            "affected_fields": ["acceptable_action_band"],
            "repair_condition": "Revise the band and present a new frozen version.",
        }
    ]

    validate_review_packet(packet, PACKAGE_ROOT)
    assert packet["owner_review_status"] == "pending"
    assert record["owner_review_status"] == "reviewed"
    assert record["owner_record_decision"] == "REVISE"


def test_finalize_freezes_completed_packet_with_judge_and_custody_manifest(
    tmp_path,
) -> None:
    packet = build_review_packet(PACKAGE_ROOT)
    _complete_all_record_reviews(packet)
    input_path = tmp_path / "owner-reviewed.yaml"
    input_bytes = yaml.safe_dump(
        packet, allow_unicode=True, sort_keys=False, width=88
    ).encode("utf-8")
    input_path.write_bytes(input_bytes)
    output_dir = tmp_path / "frozen"
    judge = {
        "judge_id": "jimmy_lin",
        "display_name": "Jimmy Lin",
        "role": "founding_theologian_technical_judge",
    }

    packet_path, manifest_path = adjudication.finalize_review_packet(
        PACKAGE_ROOT,
        input_path,
        output_dir,
        judge=judge,
        completed_at="2026-07-13T18:00:00Z",
    )

    completed = yaml.safe_load(packet_path.read_text(encoding="utf-8"))
    assert completed["owner_review_status"] == "completed"
    assert completed["owner_judge"] == judge
    assert completed["owner_completed_at"] == "2026-07-13T18:00:00Z"
    assert all(
        record["owner_review_status"] == "reviewed"
        and record["owner_judge_id"] == judge["judge_id"]
        and record["owner_behavior_rationale"]
        and record["owner_interpretive_rationale"]
        for record in completed["records"]
    )
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["manifest_version"] == "adjudicated-packet-manifest-v1"
    assert manifest["owner_review_status"] == "completed"
    assert manifest["judge"] == judge
    assert manifest["completed_at"] == "2026-07-13T18:00:00Z"
    assert manifest["source_review_packet"] == {
        "path": input_path.name,
        "sha256": hashlib.sha256(input_bytes).hexdigest(),
        "bytes": len(input_bytes),
    }
    completed_bytes = packet_path.read_bytes()
    assert manifest["artifacts"] == [
        {
            "path": "adjudicated-provisional-gold-review.yaml",
            "sha256": hashlib.sha256(completed_bytes).hexdigest(),
            "bytes": len(completed_bytes),
        }
    ]

    with pytest.raises(FileExistsError, match="immutable adjudicated output"):
        adjudication.finalize_review_packet(
            PACKAGE_ROOT,
            input_path,
            output_dir,
            judge=judge,
            completed_at="2026-07-13T18:00:00Z",
        )
    assert packet_path.read_bytes() == completed_bytes


def test_review_schema_requires_semantic_rfc3339_timestamps() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

    assert schema["$defs"]["utcTimestamp"] == {
        "type": "string",
        "format": "date-time",
        "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$",
    }


def test_finalizer_rejects_impossible_calendar_completion_timestamp(tmp_path) -> None:
    packet = build_review_packet(PACKAGE_ROOT)
    _complete_all_record_reviews(packet)
    input_path = tmp_path / "owner-reviewed.yaml"
    input_path.write_text(
        yaml.safe_dump(packet, allow_unicode=True, sort_keys=False, width=88),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="schema validation failed"):
        adjudication.finalize_review_packet(
            PACKAGE_ROOT,
            input_path,
            tmp_path / "frozen",
            judge={
                "judge_id": "jimmy_lin",
                "display_name": "Jimmy Lin",
                "role": "founding_theologian_technical_judge",
            },
            completed_at="2026-02-30T18:00:00Z",
        )

    assert not (tmp_path / "frozen" / "adjudicated-provisional-gold-review.yaml").exists()


def test_finalize_rejects_packet_with_pending_records(tmp_path) -> None:
    packet = build_review_packet(PACKAGE_ROOT)
    input_path = tmp_path / "pending.yaml"
    input_path.write_text(
        yaml.safe_dump(packet, allow_unicode=True, sort_keys=False, width=88),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="all records must be reviewed"):
        adjudication.finalize_review_packet(
            PACKAGE_ROOT,
            input_path,
            tmp_path / "frozen",
            judge={
                "judge_id": "jimmy_lin",
                "display_name": "Jimmy Lin",
                "role": "founding_theologian_technical_judge",
            },
            completed_at="2026-07-13T18:00:00Z",
        )


@pytest.mark.parametrize(
    ("behavior", "interpretive", "expected"),
    [
        ("DEFER", "REJECT", "DEFER"),
        ("REJECT", "REVISE", "REJECT"),
        ("REVISE", "APPROVE", "REVISE"),
        ("APPROVE", "NOT_APPLICABLE", "APPROVE"),
        ("NOT_APPLICABLE", "NOT_APPLICABLE", "DEFER"),
    ],
)
def test_owner_decision_rollup_uses_registered_precedence(
    behavior: str, interpretive: str, expected: str
) -> None:
    assert roll_up_owner_decisions(behavior, interpretive) == expected


@pytest.mark.parametrize(
    ("behavior", "interpretive", "incorrect_record"),
    [
        ("DEFER", "REJECT", "REJECT"),
        ("REJECT", "REVISE", "REVISE"),
        ("REVISE", "APPROVE", "APPROVE"),
    ],
)
def test_validation_rejects_inconsistent_reviewed_rollup(
    behavior: str, interpretive: str, incorrect_record: str
) -> None:
    packet = build_review_packet(PACKAGE_ROOT)
    record = next(
        record
        for record in packet["records"]
        if record["track_applicability"]
        == {"behavior": "applicable", "interpretive": "applicable"}
    )
    _complete_record_review(record)
    record["owner_behavior_decision"] = behavior
    record["owner_interpretive_decision"] = interpretive
    record["owner_record_decision"] = incorrect_record

    with pytest.raises(ValueError, match="owner_record_decision|schema validation"):
        validate_review_packet(packet, PACKAGE_ROOT)


def test_repeat_is_registered_for_later_blinded_selection_without_mapping() -> None:
    procedure = build_review_packet(PACKAGE_ROOT)["blinded_repeat_procedure"]

    assert procedure["timing"] == "post_pass_one"
    assert procedure["target_fraction"] == 0.2
    assert procedure["sample_size"] == 10
    assert procedure["stratification"] == ["module", "role"]
    assert procedure["module_minimum"] == 2
    assert procedure["role_minimum"] == 3
    assert procedure["seed_domain"] == "repeat_sampling_v1"
    assert procedure["digest_input"] == (
        "UTF-8(repeat_sampling_v1) + NUL + ASCII(adjudicated_packet_sha256) "
        "+ NUL + UTF-8(episode_id)"
    )
    assert procedure["ranking_rule"] == (
        "Sort by digest ascending, then episode_id Unicode-code-point ascending."
    )
    assert procedure["skip_rule"] == (
        "Skip a ranked candidate exactly when accepting it would leave no "
        "10-record completion satisfying every module and role minimum."
    )
    assert procedure["backfill_rule"] == (
        "Continue the same ranked feasibility scan until 10 records are selected; "
        "there is no discretionary backfill."
    )
    assert procedure["tie_break"] == (
        "Digest ties are resolved by episode_id Unicode-code-point ascending."
    )
    assert procedure["opaque_repeat_id_format"] == "RPT-{ordinal:03d}"
    assert procedure["unblinding"] == "after_repeat_submission"
    forbidden_mapping_keys = {
        "selected_episode_ids",
        "selected_mapping",
        "repeat_id_mapping",
    }
    assert forbidden_mapping_keys.isdisjoint(procedure)


def test_repeat_selector_is_deterministic_stratified_and_mapping_is_held() -> None:
    packet = build_review_packet(PACKAGE_ROOT)
    _complete_all_record_reviews(packet)
    packet["owner_review_status"] = "completed"
    packet["owner_judge"] = {
        "judge_id": "jimmy_lin",
        "display_name": "Jimmy Lin",
        "role": "founding_theologian_technical_judge",
    }
    packet["owner_completed_at"] = "2026-07-13T18:00:00Z"
    frozen_bytes = yaml.safe_dump(
        packet, allow_unicode=True, sort_keys=False, width=88
    ).encode("utf-8")
    frozen_sha256 = hashlib.sha256(frozen_bytes).hexdigest()

    first = adjudication.build_repeat_mapping(packet, frozen_sha256)
    second = adjudication.build_repeat_mapping(packet, frozen_sha256)

    assert first == second
    assert first["mapping_version"] == "blinded-repeat-mapping-v1"
    assert first["source_adjudicated_packet_sha256"] == frozen_sha256
    entries = first["entries"]
    assert len(entries) == 10
    assert [entry["repeat_id"] for entry in entries] == [
        f"RPT-{index:03d}" for index in range(1, 11)
    ]
    assert len({entry["episode_id"] for entry in entries}) == 10
    assert all(
        sum(entry["module"] == module for entry in entries) >= 2
        for module in MODULES
    )
    assert all(
        sum(entry["role"] == role for entry in entries) >= 3
        for role in ("target", "null", "restraint")
    )
    assert "repeat_id_mapping" not in json.dumps(packet, sort_keys=True)


def test_repeat_mapping_writer_uses_separate_immutable_custody_file(tmp_path) -> None:
    packet = build_review_packet(PACKAGE_ROOT)
    _complete_all_record_reviews(packet)
    packet["owner_review_status"] = "completed"
    packet["owner_judge"] = {
        "judge_id": "jimmy_lin",
        "display_name": "Jimmy Lin",
        "role": "founding_theologian_technical_judge",
    }
    packet["owner_completed_at"] = "2026-07-13T18:00:00Z"
    packet_path = tmp_path / "adjudicated.yaml"
    packet_path.write_text(
        yaml.safe_dump(packet, allow_unicode=True, sort_keys=False, width=88),
        encoding="utf-8",
    )
    mapping_path = tmp_path / "custodian" / "repeat-mapping.yaml"

    written = adjudication.write_repeat_mapping(
        PACKAGE_ROOT, packet_path, mapping_path
    )

    assert written == mapping_path
    mapping = yaml.safe_load(mapping_path.read_text(encoding="utf-8"))
    assert len(mapping["entries"]) == 10
    with pytest.raises(FileExistsError, match="repeat mapping already exists"):
        adjudication.write_repeat_mapping(PACKAGE_ROOT, packet_path, mapping_path)


def test_export_is_deterministic_and_manifest_hashes_emitted_packet(tmp_path) -> None:
    first_dir = tmp_path / "first"
    second_dir = tmp_path / "second"

    first_packet_path, first_manifest_path = export_review_packet(
        PACKAGE_ROOT, first_dir
    )
    second_packet_path, second_manifest_path = export_review_packet(
        PACKAGE_ROOT, second_dir
    )

    assert first_packet_path.read_bytes() == second_packet_path.read_bytes()
    assert first_manifest_path.read_bytes() == second_manifest_path.read_bytes()
    manifest = json.loads(first_manifest_path.read_text(encoding="utf-8"))
    packet_bytes = first_packet_path.read_bytes()
    assert manifest["manifest_version"] == "packet-manifest-v1"
    assert manifest["classification"] == "single_expert_provisional_gold"
    assert manifest["record_count"] == 48
    assert manifest["artifacts"] == [
        {
            "path": "provisional-gold-review.yaml",
            "sha256": hashlib.sha256(packet_bytes).hexdigest(),
            "bytes": len(packet_bytes),
        }
    ]
    assert len(manifest["inputs"]["episode_banks"]) == 4
    assert set(manifest["inputs"]) == {
        "authored_episode_bank_schema",
        "provisional_gold_review_schema",
        "episode_banks",
    }


def test_export_is_idempotent_when_existing_outputs_are_pristine(tmp_path) -> None:
    output_dir = tmp_path / "idempotent"
    packet_path, manifest_path = export_review_packet(PACKAGE_ROOT, output_dir)
    original_packet = packet_path.read_bytes()
    original_manifest = manifest_path.read_bytes()

    repeated_packet_path, repeated_manifest_path = export_review_packet(
        PACKAGE_ROOT, output_dir
    )

    assert repeated_packet_path == packet_path
    assert repeated_manifest_path == manifest_path
    assert packet_path.read_bytes() == original_packet
    assert manifest_path.read_bytes() == original_manifest


def test_cli_refuses_to_overwrite_reviewed_packet_and_preserves_both_files(
    tmp_path,
) -> None:
    output_dir = tmp_path / "reviewed"
    packet_path, manifest_path = export_review_packet(PACKAGE_ROOT, output_dir)
    packet = yaml.safe_load(packet_path.read_text(encoding="utf-8"))
    record = packet["records"][0]
    _complete_record_review(record)
    validate_review_packet(packet, PACKAGE_ROOT)
    packet_path.write_text(
        yaml.safe_dump(packet, allow_unicode=True, sort_keys=False, width=88),
        encoding="utf-8",
    )
    reviewed_packet = packet_path.read_bytes()
    original_manifest = manifest_path.read_bytes()

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "biblebench_pilot.adjudication",
            "--package-root",
            str(PACKAGE_ROOT),
            "--output-dir",
            str(output_dir),
        ],
        cwd=PACKAGE_ROOT,
        check=False,
        capture_output=True,
        text=True,
        env={"PYTHONPATH": str(PACKAGE_ROOT / "src")},
    )

    assert result.returncode != 0
    assert result.stdout == ""
    assert "refusing to overwrite modified output" in result.stderr
    assert packet_path.read_bytes() == reviewed_packet
    assert manifest_path.read_bytes() == original_manifest
    surviving_packet = yaml.safe_load(packet_path.read_text(encoding="utf-8"))
    assert surviving_packet["records"][0]["owner_behavior_decision"] == "APPROVE"


def test_module_cli_writes_requested_offline_packet(tmp_path) -> None:
    output_dir = tmp_path / "cli-output"
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "biblebench_pilot.adjudication",
            "--package-root",
            str(PACKAGE_ROOT),
            "--output-dir",
            str(output_dir),
        ],
        cwd=PACKAGE_ROOT,
        check=False,
        capture_output=True,
        text=True,
        env={"PYTHONPATH": str(PACKAGE_ROOT / "src")},
    )

    assert result.returncode == 0, result.stderr
    assert result.stderr == ""
    assert result.stdout == (
        f"wrote {output_dir / 'provisional-gold-review.yaml'}\n"
        f"wrote {output_dir / 'packet-manifest.json'}\n"
    )
    assert (output_dir / "provisional-gold-review.yaml").is_file()
    assert (output_dir / "packet-manifest.json").is_file()
