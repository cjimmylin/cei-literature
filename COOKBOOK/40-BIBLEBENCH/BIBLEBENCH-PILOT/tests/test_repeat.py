from __future__ import annotations

import hashlib
import json
from functools import lru_cache
from pathlib import Path

from jsonschema import Draft202012Validator
import pytest
import yaml

from biblebench_pilot import adjudication
import biblebench_pilot.repeat as repeat
from biblebench_pilot.repeat import build_repeat_packet


PACKAGE_ROOT = Path(__file__).parents[1]
SCHEMA_PATH = PACKAGE_ROOT / "schemas" / "repeat-review.schema.json"


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


@lru_cache(maxsize=1)
def _completed_pass_one_bytes() -> bytes:
    packet = adjudication.build_review_packet(PACKAGE_ROOT)
    judge = {
        "judge_id": "jimmy_lin",
        "display_name": "Jimmy Lin",
        "role": "founding_theologian_technical_judge",
    }
    for record in packet["records"]:
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
        record["owner_record_decision"] = adjudication.roll_up_owner_decisions(
            record["owner_behavior_decision"],
            record["owner_interpretive_decision"],
        )
        record["owner_behavior_rationale"] = "Pass-one behavior rationale."
        record["owner_interpretive_rationale"] = "Pass-one interpretation rationale."
        record["owner_confidence"] = "high"
        record["owner_contestability"] = "clear"
        record["owner_issues"] = []
        record["owner_judge_id"] = judge["judge_id"]
        record["owner_reviewed_at"] = "2026-07-13T17:00:00Z"
    packet["owner_review_status"] = "completed"
    packet["owner_judge"] = judge
    packet["owner_completed_at"] = "2026-07-13T18:00:00Z"
    return yaml.safe_dump(
        packet, allow_unicode=True, sort_keys=False, width=88
    ).encode("utf-8")


def _completed_pass_one(tmp_path: Path) -> tuple[Path, Path, dict]:
    packet_bytes = _completed_pass_one_bytes()
    packet = yaml.safe_load(packet_bytes)
    packet_path = tmp_path / "adjudicated.yaml"
    packet_path.write_bytes(packet_bytes)
    mapping = adjudication.build_repeat_mapping(
        packet, hashlib.sha256(packet_bytes).hexdigest()
    )
    mapping_path = tmp_path / "custodian" / "repeat-mapping.yaml"
    mapping_path.parent.mkdir(parents=True)
    mapping_path.write_text(
        yaml.safe_dump(mapping, allow_unicode=True, sort_keys=False, width=88),
        encoding="utf-8",
    )
    return packet_path, mapping_path, packet


def _authenticated_repeat_sources(
    tmp_path: Path,
) -> tuple[Path, Path, Path, Path, dict]:
    pass_one_path, mapping_path, pass_one = _completed_pass_one(tmp_path)
    source_packet_path, source_manifest_path = repeat.export_repeat_packet(
        PACKAGE_ROOT,
        pass_one_path,
        mapping_path,
        tmp_path / "immutable-source",
    )
    return (
        pass_one_path,
        mapping_path,
        source_packet_path,
        source_manifest_path,
        pass_one,
    )


def test_build_repeat_packet_is_schema_valid_hashed_and_blinded(tmp_path: Path) -> None:
    pass_one_path, mapping_path, pass_one = _completed_pass_one(tmp_path)

    packet = build_repeat_packet(PACKAGE_ROOT, pass_one_path, mapping_path)

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(packet)
    assert packet["packet_version"] == "blinded-repeat-review-v1"
    assert packet["review_status"] == "pending"
    assert [record["repeat_id"] for record in packet["records"]] == [
        f"RPT-{index:03d}" for index in range(1, 11)
    ]
    assert all(
        record["review_content_sha256"]
        == _canonical_sha256(record["review_content"])
        for record in packet["records"]
    )

    serialized = json.dumps(packet, sort_keys=True, ensure_ascii=False)
    mapping = yaml.safe_load(mapping_path.read_text(encoding="utf-8"))
    forbidden_keys = {
        "episode_id",
        "core_id",
        "module",
        "source_artifacts",
        "source_banks",
        "source_adjudicated_packet_sha256",
        "selection_digest",
    }
    assert forbidden_keys.isdisjoint(_all_keys(packet))
    for entry in mapping["entries"]:
        original = next(
            record
            for record in pass_one["records"]
            if record["episode_id"] == entry["episode_id"]
        )
        assert original["episode_id"] not in serialized
        assert original["core_id"] not in serialized
        assert original["module"] not in serialized
        for artifact in original["review_payload"]["source_artifacts"]:
            assert artifact["path"] not in serialized


def test_pending_repeat_records_reserve_fresh_applicability_judgments(
    tmp_path: Path,
) -> None:
    pass_one_path, mapping_path, _ = _completed_pass_one(tmp_path)

    packet = build_repeat_packet(PACKAGE_ROOT, pass_one_path, mapping_path)

    assert all(
        record["behavior_applicability_decision"] is None
        and record["interpretive_applicability_decision"] is None
        for record in packet["records"]
    )


def test_visible_repeat_records_do_not_expose_registered_track_applicability(
    tmp_path: Path,
) -> None:
    pass_one_path, mapping_path, pass_one = _completed_pass_one(tmp_path)

    packet = build_repeat_packet(PACKAGE_ROOT, pass_one_path, mapping_path)
    mapping = yaml.safe_load(mapping_path.read_text(encoding="utf-8"))
    pass_one_by_id = {
        record["episode_id"]: record for record in pass_one["records"]
    }

    assert "track_applicability" not in _all_keys(packet)
    for visible, mapping_entry in zip(packet["records"], mapping["entries"]):
        registered = pass_one_by_id[mapping_entry["episode_id"]][
            "track_applicability"
        ]
        assert "track_applicability" not in visible["review_content"]
        assert registered not in visible["review_content"].values()

    schema_text = SCHEMA_PATH.read_text(encoding="utf-8")
    assert "track_applicability" not in schema_text


def _all_keys(value: object) -> set[str]:
    if isinstance(value, dict):
        return set(value).union(
            *( _all_keys(child) for child in value.values())
        )
    if isinstance(value, list):
        return set().union(*(_all_keys(child) for child in value))
    return set()


def _write_yaml(path: Path, value: dict) -> None:
    path.write_text(
        yaml.safe_dump(value, allow_unicode=True, sort_keys=False, width=88),
        encoding="utf-8",
    )


def test_rejects_noncompleted_pass_one_before_using_mapping(tmp_path: Path) -> None:
    pass_one_path, mapping_path, packet = _completed_pass_one(tmp_path)
    packet["owner_review_status"] = "pending"
    packet["owner_judge"] = None
    packet["owner_completed_at"] = None
    _write_yaml(pass_one_path, packet)

    with pytest.raises(ValueError, match="completed pass-one"):
        build_repeat_packet(PACKAGE_ROOT, pass_one_path, mapping_path)


def test_rejects_mapping_source_hash_mismatch(tmp_path: Path) -> None:
    pass_one_path, mapping_path, _ = _completed_pass_one(tmp_path)
    mapping = yaml.safe_load(mapping_path.read_text(encoding="utf-8"))
    mapping["source_adjudicated_packet_sha256"] = "0" * 64
    _write_yaml(mapping_path, mapping)

    with pytest.raises(ValueError, match="source hash"):
        build_repeat_packet(PACKAGE_ROOT, pass_one_path, mapping_path)


@pytest.mark.parametrize("mutation", ["unknown", "duplicate", "geometry", "extra"])
def test_rejects_invalid_or_noncanonical_mapping_entries(
    tmp_path: Path, mutation: str
) -> None:
    pass_one_path, mapping_path, _ = _completed_pass_one(tmp_path)
    mapping = yaml.safe_load(mapping_path.read_text(encoding="utf-8"))
    if mutation == "unknown":
        mapping["entries"][0]["episode_id"] = "UNKNOWN-TARGET-01"
    elif mutation == "duplicate":
        mapping["entries"][1] = dict(mapping["entries"][0])
        mapping["entries"][1]["repeat_id"] = "RPT-002"
    elif mutation == "geometry":
        mapping["entries"][0]["role"] = "null"
    else:
        mapping["entries"][0]["original_index"] = 0
    _write_yaml(mapping_path, mapping)

    with pytest.raises(ValueError, match="mapping|sample geometry|unknown"):
        build_repeat_packet(PACKAGE_ROOT, pass_one_path, mapping_path)


def test_validate_rejects_hash_tamper_and_forbidden_visible_field(
    tmp_path: Path,
) -> None:
    pass_one_path, mapping_path, _ = _completed_pass_one(tmp_path)
    packet = build_repeat_packet(PACKAGE_ROOT, pass_one_path, mapping_path)
    packet["records"][0]["review_content"]["scenario"] = "Tampered scenario."

    with pytest.raises(ValueError, match="content hash mismatch"):
        repeat.validate_repeat_packet(packet, PACKAGE_ROOT)

    packet = build_repeat_packet(PACKAGE_ROOT, pass_one_path, mapping_path)
    packet["records"][0]["review_content"]["episode_id"] = "F01-TARGET-01"
    with pytest.raises(ValueError, match="schema validation|forbidden"):
        repeat.validate_repeat_packet(packet, PACKAGE_ROOT)


def test_export_is_exclusive_create_and_manifest_has_no_custody_join(
    tmp_path: Path,
) -> None:
    pass_one_path, mapping_path, pass_one = _completed_pass_one(tmp_path)
    output_dir = tmp_path / "judge"

    packet_path, manifest_path = repeat.export_repeat_packet(
        PACKAGE_ROOT, pass_one_path, mapping_path, output_dir
    )

    packet_bytes = packet_path.read_bytes()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert packet_path.name == "blinded-repeat-review.yaml"
    assert manifest["manifest_version"] == "blinded-repeat-packet-manifest-v1"
    assert manifest["record_count"] == 10
    assert manifest["artifacts"] == [
        {
            "path": packet_path.name,
            "sha256": hashlib.sha256(packet_bytes).hexdigest(),
            "bytes": len(packet_bytes),
        }
    ]
    serialized = packet_path.read_text(encoding="utf-8") + json.dumps(manifest)
    assert "source_adjudicated_packet_sha256" not in serialized
    assert "selection_digest" not in serialized
    visible_packet = yaml.safe_load(packet_path.read_text(encoding="utf-8"))
    assert not any("mapping" in key.casefold() for key in _all_keys(visible_packet))
    assert not any("mapping" in key.casefold() for key in _all_keys(manifest))
    for record in pass_one["records"]:
        assert record["episode_id"] not in serialized
        assert record["core_id"] not in serialized

    with pytest.raises(FileExistsError, match="immutable repeat output"):
        repeat.export_repeat_packet(
            PACKAGE_ROOT, pass_one_path, mapping_path, output_dir
        )
    assert packet_path.read_bytes() == packet_bytes


def _complete_repeat_reviews(
    packet: dict,
    *,
    judge_id: str = "jimmy_lin",
    reviewed_at: str = "2026-07-13T19:00:00Z",
) -> None:
    for record in packet["records"]:
        record["review_status"] = "reviewed"
        record["behavior_applicability_decision"] = "APPLICABLE"
        record["interpretive_applicability_decision"] = "APPLICABLE"
        record["behavior_decision"] = "APPROVE"
        record["interpretive_decision"] = "APPROVE"
        record["record_decision"] = adjudication.roll_up_owner_decisions(
            record["behavior_decision"], record["interpretive_decision"]
        )
        record["behavior_rationale"] = "Fresh repeat behavior judgment."
        record["interpretive_rationale"] = "Fresh repeat interpretation judgment."
        record["confidence"] = "high"
        record["contestability"] = "clear"
        record["issues"] = []
        record["judge_id"] = judge_id
        record["reviewed_at"] = reviewed_at


def _apply_private_pass_one_routing(
    packet: dict, pass_one: dict, mapping_path: Path
) -> None:
    mapping = yaml.safe_load(mapping_path.read_text(encoding="utf-8"))
    pass_one_by_id = {
        record["episode_id"]: record for record in pass_one["records"]
    }
    repeat_by_id = {record["repeat_id"]: record for record in packet["records"]}
    for entry in mapping["entries"]:
        private_record = pass_one_by_id[entry["episode_id"]]
        visible_record = repeat_by_id[entry["repeat_id"]]
        for track in ("behavior", "interpretive"):
            applicable = private_record[f"owner_{track}_decision"] != "NOT_APPLICABLE"
            visible_record[f"{track}_applicability_decision"] = (
                "APPLICABLE" if applicable else "NOT_APPLICABLE"
            )
            visible_record[f"{track}_decision"] = (
                "APPROVE" if applicable else "NOT_APPLICABLE"
            )
        visible_record["record_decision"] = adjudication.roll_up_owner_decisions(
            visible_record["behavior_decision"],
            visible_record["interpretive_decision"],
        )


def test_fresh_applicability_can_disagree_with_registered_routing(
    tmp_path: Path,
) -> None:
    pass_one_path, mapping_path, pass_one = _completed_pass_one(tmp_path)
    packet = build_repeat_packet(PACKAGE_ROOT, pass_one_path, mapping_path)
    _complete_repeat_reviews(packet)
    _apply_private_pass_one_routing(packet, pass_one, mapping_path)
    mapping = yaml.safe_load(mapping_path.read_text(encoding="utf-8"))
    pass_one_by_id = {
        row["episode_id"]: row for row in pass_one["records"]
    }
    entry = next(
        row
        for row in mapping["entries"]
        if pass_one_by_id[row["episode_id"]]["owner_behavior_decision"]
        != "NOT_APPLICABLE"
    )
    record = next(row for row in packet["records"] if row["repeat_id"] == entry["repeat_id"])
    record["behavior_applicability_decision"] = "NOT_APPLICABLE"
    record["behavior_decision"] = "NOT_APPLICABLE"
    record["record_decision"] = adjudication.roll_up_owner_decisions(
        record["behavior_decision"], record["interpretive_decision"]
    )

    repeat.validate_repeat_packet(packet, PACKAGE_ROOT)


def test_fresh_applicability_and_track_decision_must_be_semantically_consistent(
    tmp_path: Path,
) -> None:
    pass_one_path, mapping_path, _ = _completed_pass_one(tmp_path)
    packet = build_repeat_packet(PACKAGE_ROOT, pass_one_path, mapping_path)
    _complete_repeat_reviews(packet)
    record = packet["records"][0]
    record["behavior_applicability_decision"] = "NOT_APPLICABLE"
    record["behavior_decision"] = "APPROVE"

    with pytest.raises(ValueError, match="behavior decision must be NOT_APPLICABLE"):
        repeat.validate_repeat_packet(packet, PACKAGE_ROOT)


def test_finalizer_emits_exact_aggregate_applicability_agreement_only_after_freeze(
    tmp_path: Path,
) -> None:
    (
        pass_one_path,
        mapping_path,
        source_packet_path,
        source_manifest_path,
        pass_one,
    ) = _authenticated_repeat_sources(tmp_path)
    packet = yaml.safe_load(source_packet_path.read_text(encoding="utf-8"))
    _complete_repeat_reviews(packet)
    _apply_private_pass_one_routing(packet, pass_one, mapping_path)
    record = packet["records"][0]
    assert record["behavior_applicability_decision"] == "APPLICABLE"
    record["behavior_applicability_decision"] = "NOT_APPLICABLE"
    record["behavior_decision"] = "NOT_APPLICABLE"
    record["record_decision"] = adjudication.roll_up_owner_decisions(
        record["behavior_decision"], record["interpretive_decision"]
    )
    reviewed_path = tmp_path / "reviewed-for-agreement.yaml"
    _write_yaml(reviewed_path, packet)

    frozen_path, manifest_path = repeat.finalize_repeat_packet(
        PACKAGE_ROOT,
        reviewed_path,
        tmp_path / "agreement-frozen",
        source_packet_path=source_packet_path,
        source_manifest_path=source_manifest_path,
        completed_pass_one_path=pass_one_path,
        judge=pass_one["owner_judge"],
        completed_at="2026-07-13T20:00:00Z",
    )

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["applicability_agreement"] == {
        "basis": "pass_one_track_decision_vs_fresh_repeat_applicability_v1",
        "behavior": {"exact_agreement_count": 9, "denominator": 10},
        "interpretive": {"exact_agreement_count": 10, "denominator": 10},
        "overall": {"exact_agreement_count": 19, "denominator": 20},
    }
    serialized_manifest = json.dumps(manifest, sort_keys=True)
    frozen = yaml.safe_load(frozen_path.read_text(encoding="utf-8"))
    serialized_frozen = json.dumps(frozen, sort_keys=True)
    assert "owner_behavior_decision" not in serialized_manifest
    assert "owner_interpretive_decision" not in serialized_manifest
    assert all(record["episode_id"] not in serialized_manifest for record in pass_one["records"])
    assert "pass_one" not in serialized_frozen


def test_private_mapping_is_the_only_postfreeze_identity_join(
    tmp_path: Path,
) -> None:
    (
        pass_one_path,
        mapping_path,
        source_packet_path,
        source_manifest_path,
        pass_one,
    ) = _authenticated_repeat_sources(tmp_path)
    packet = yaml.safe_load(source_packet_path.read_text(encoding="utf-8"))
    _complete_repeat_reviews(packet)
    reviewed_path = tmp_path / "reviewed-for-private-join.yaml"
    _write_yaml(reviewed_path, packet)
    frozen_path, frozen_manifest_path = repeat.finalize_repeat_packet(
        PACKAGE_ROOT,
        reviewed_path,
        tmp_path / "private-join-frozen",
        source_packet_path=source_packet_path,
        source_manifest_path=source_manifest_path,
        completed_pass_one_path=pass_one_path,
        judge=pass_one["owner_judge"],
        completed_at="2026-07-13T20:00:00Z",
    )

    mapping = yaml.safe_load(mapping_path.read_text(encoding="utf-8"))
    frozen = yaml.safe_load(frozen_path.read_text(encoding="utf-8"))
    frozen_by_repeat_id = {
        record["repeat_id"]: record for record in frozen["records"]
    }
    joined = [
        (entry["episode_id"], frozen_by_repeat_id[entry["repeat_id"]])
        for entry in mapping["entries"]
    ]
    assert len(joined) == 10
    assert len({episode_id for episode_id, _ in joined}) == 10

    public_bytes = b"\n".join(
        path.read_bytes()
        for path in (
            source_packet_path,
            source_manifest_path,
            frozen_path,
            frozen_manifest_path,
        )
    )
    assert all(
        entry["episode_id"].encode("utf-8") not in public_bytes
        for entry in mapping["entries"]
    )
    assert b"selection_digest" not in public_bytes
    assert b"source_adjudicated_packet_sha256" not in public_bytes


def test_finalizer_freezes_all_fresh_judgments_with_manifest_and_rollup(
    tmp_path: Path,
) -> None:
    (
        pass_one_path,
        _,
        source_packet_path,
        source_manifest_path,
        pass_one,
    ) = _authenticated_repeat_sources(tmp_path)
    packet = yaml.safe_load(source_packet_path.read_text(encoding="utf-8"))
    _complete_repeat_reviews(packet)
    dual_track = packet["records"][0]
    dual_track["interpretive_decision"] = "REVISE"
    dual_track["record_decision"] = "REVISE"
    dual_track["confidence"] = "medium"
    dual_track["issues"] = [
        {
            "issue_id": "RPT-P1-INTERPRETATION",
            "priority": "P1",
            "track": "interpretive",
            "summary": "A material interpretive boundary requires revision.",
            "affected_fields": ["passage_anchors"],
            "repair_condition": "Revise the boundary and re-review this record.",
        }
    ]
    reviewed_path = tmp_path / "reviewed-repeat.yaml"
    _write_yaml(reviewed_path, packet)
    judge = pass_one["owner_judge"]
    output_dir = tmp_path / "frozen"

    frozen_path, manifest_path = repeat.finalize_repeat_packet(
        PACKAGE_ROOT,
        reviewed_path,
        output_dir,
        source_packet_path=source_packet_path,
        source_manifest_path=source_manifest_path,
        completed_pass_one_path=pass_one_path,
        judge=judge,
        completed_at="2026-07-13T20:00:00Z",
    )

    frozen = yaml.safe_load(frozen_path.read_text(encoding="utf-8"))
    assert frozen["review_status"] == "completed"
    assert frozen["judge"] == judge
    assert frozen["completed_at"] == "2026-07-13T20:00:00Z"
    assert len(frozen["records"]) == 10
    assert all(record["review_status"] == "reviewed" for record in frozen["records"])
    assert dual_track["record_decision"] == "REVISE"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["manifest_version"] == "frozen-blinded-repeat-manifest-v1"
    assert manifest["judge"] == judge
    assert manifest["completed_at"] == "2026-07-13T20:00:00Z"
    assert manifest["source_repeat_packet"]["path"] == (
        "submitted-blinded-repeat-review.yaml"
    )
    assert manifest["source_repeat_packet"]["sha256"] == hashlib.sha256(
        reviewed_path.read_bytes()
    ).hexdigest()

    frozen_bytes = frozen_path.read_bytes()
    with pytest.raises(FileExistsError, match="immutable frozen repeat output"):
        repeat.finalize_repeat_packet(
            PACKAGE_ROOT,
            reviewed_path,
            output_dir,
            source_packet_path=source_packet_path,
            source_manifest_path=source_manifest_path,
            completed_pass_one_path=pass_one_path,
            judge=judge,
            completed_at="2026-07-13T20:00:00Z",
        )
    assert frozen_path.read_bytes() == frozen_bytes


def test_finalizer_rejects_coordinated_review_content_and_self_hash_tamper(
    tmp_path: Path,
) -> None:
    (
        pass_one_path,
        _,
        source_packet_path,
        source_manifest_path,
        _,
    ) = _authenticated_repeat_sources(tmp_path)
    packet = yaml.safe_load(source_packet_path.read_text(encoding="utf-8"))
    packet["records"][0]["review_content"]["scenario"] = (
        "Coordinated post-export tamper with a newly computed self hash."
    )
    packet["records"][0]["review_content_sha256"] = _canonical_sha256(
        packet["records"][0]["review_content"]
    )
    _complete_repeat_reviews(packet)
    reviewed_path = tmp_path / "coordinated-tamper.yaml"
    _write_yaml(reviewed_path, packet)

    with pytest.raises(ValueError, match="immutable exported repeat packet"):
        repeat.finalize_repeat_packet(
            PACKAGE_ROOT,
            reviewed_path,
            tmp_path / "tamper-frozen",
            source_packet_path=source_packet_path,
            source_manifest_path=source_manifest_path,
            completed_pass_one_path=pass_one_path,
            judge={
                "judge_id": "jimmy_lin",
                "display_name": "Jimmy Lin",
                "role": "founding_theologian_technical_judge",
            },
            completed_at="2026-07-13T20:00:00Z",
        )


def test_finalizer_rejects_repeat_judge_who_is_not_the_pass_one_judge(
    tmp_path: Path,
) -> None:
    (
        pass_one_path,
        _,
        source_packet_path,
        source_manifest_path,
        _,
    ) = _authenticated_repeat_sources(tmp_path)
    packet = yaml.safe_load(source_packet_path.read_text(encoding="utf-8"))
    _complete_repeat_reviews(packet, judge_id="other_judge")
    reviewed_path = tmp_path / "other-judge.yaml"
    _write_yaml(reviewed_path, packet)

    with pytest.raises(ValueError, match="pass-one judge"):
        repeat.finalize_repeat_packet(
            PACKAGE_ROOT,
            reviewed_path,
            tmp_path / "other-judge-frozen",
            source_packet_path=source_packet_path,
            source_manifest_path=source_manifest_path,
            completed_pass_one_path=pass_one_path,
            judge={
                "judge_id": "other_judge",
                "display_name": "Other Judge",
                "role": "founding_theologian_technical_judge",
            },
            completed_at="2026-07-13T20:00:00Z",
        )


@pytest.mark.parametrize(
    ("reviewed_at", "completed_at", "message"),
    [
        ("2026-07-13T18:00:00Z", "2026-07-13T20:00:00Z", "after pass one"),
        ("2026-07-13T20:01:00Z", "2026-07-13T20:00:00Z", "after repeat judgment"),
    ],
)
def test_finalizer_enforces_pass_one_review_and_freeze_timestamp_order(
    tmp_path: Path, reviewed_at: str, completed_at: str, message: str
) -> None:
    (
        pass_one_path,
        _,
        source_packet_path,
        source_manifest_path,
        _,
    ) = _authenticated_repeat_sources(tmp_path)
    packet = yaml.safe_load(source_packet_path.read_text(encoding="utf-8"))
    _complete_repeat_reviews(packet, reviewed_at=reviewed_at)
    reviewed_path = tmp_path / f"time-{reviewed_at[11:16].replace(':', '')}.yaml"
    _write_yaml(reviewed_path, packet)

    with pytest.raises(ValueError, match=message):
        repeat.finalize_repeat_packet(
            PACKAGE_ROOT,
            reviewed_path,
            tmp_path / "time-frozen",
            source_packet_path=source_packet_path,
            source_manifest_path=source_manifest_path,
            completed_pass_one_path=pass_one_path,
            judge={
                "judge_id": "jimmy_lin",
                "display_name": "Jimmy Lin",
                "role": "founding_theologian_technical_judge",
            },
            completed_at=completed_at,
        )


def test_finalizer_rejects_an_already_frozen_repeat_submission(
    tmp_path: Path,
) -> None:
    (
        pass_one_path,
        _,
        source_packet_path,
        source_manifest_path,
        pass_one,
    ) = _authenticated_repeat_sources(tmp_path)
    packet = yaml.safe_load(source_packet_path.read_text(encoding="utf-8"))
    _complete_repeat_reviews(packet)
    packet["review_status"] = "completed"
    packet["judge"] = pass_one["owner_judge"]
    packet["completed_at"] = "2026-07-13T20:00:00Z"
    reviewed_path = tmp_path / "already-frozen.yaml"
    _write_yaml(reviewed_path, packet)

    with pytest.raises(ValueError, match="pending repeat submission"):
        repeat.finalize_repeat_packet(
            PACKAGE_ROOT,
            reviewed_path,
            tmp_path / "refrozen",
            source_packet_path=source_packet_path,
            source_manifest_path=source_manifest_path,
            completed_pass_one_path=pass_one_path,
            judge=packet["judge"],
            completed_at="2026-07-13T20:05:00Z",
        )


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        ("pending", "all 10"),
        ("judge", "judge identity"),
        ("rollup", "record_decision"),
        ("low_confidence", "low confidence"),
        ("outside_competence", "outside competence"),
        ("p1_approve", "P1"),
        ("fresh_applicability", "NOT_APPLICABLE"),
    ],
)
def test_finalizer_rejects_incomplete_or_semantically_invalid_judgments(
    tmp_path: Path, mutation: str, message: str
) -> None:
    (
        pass_one_path,
        _,
        source_packet_path,
        source_manifest_path,
        pass_one,
    ) = _authenticated_repeat_sources(tmp_path)
    packet = yaml.safe_load(source_packet_path.read_text(encoding="utf-8"))
    _complete_repeat_reviews(packet)
    record = packet["records"][0]
    if mutation == "pending":
        record.update(
            {
                "review_status": "pending",
                "behavior_applicability_decision": None,
                "interpretive_applicability_decision": None,
                "behavior_decision": None,
                "interpretive_decision": None,
                "record_decision": None,
                "behavior_rationale": None,
                "interpretive_rationale": None,
                "confidence": None,
                "contestability": None,
                "issues": None,
                "judge_id": None,
                "reviewed_at": None,
            }
        )
    elif mutation == "judge":
        record["judge_id"] = "different_judge"
    elif mutation == "rollup":
        record["record_decision"] = "DEFER"
    elif mutation == "low_confidence":
        record["confidence"] = "low"
    elif mutation == "outside_competence":
        record["contestability"] = "outside_competence"
    elif mutation == "p1_approve":
        record["issues"] = [
            {
                "issue_id": "RPT-P1-RECORD",
                "priority": "P1",
                "track": "record",
                "summary": "A material record issue remains open.",
                "affected_fields": ["scenario"],
                "repair_condition": "Repair and re-review the record.",
            }
        ]
    else:
        record["behavior_applicability_decision"] = "NOT_APPLICABLE"
        record["behavior_decision"] = "APPROVE"
    reviewed_path = tmp_path / f"{mutation}.yaml"
    _write_yaml(reviewed_path, packet)

    with pytest.raises(ValueError, match=message):
        repeat.finalize_repeat_packet(
            PACKAGE_ROOT,
            reviewed_path,
            tmp_path / f"frozen-{mutation}",
            source_packet_path=source_packet_path,
            source_manifest_path=source_manifest_path,
            completed_pass_one_path=pass_one_path,
            judge=pass_one["owner_judge"],
            completed_at="2026-07-13T20:00:00Z",
        )
