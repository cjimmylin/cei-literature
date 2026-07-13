from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Union

from jsonschema import Draft202012Validator
import yaml

from biblebench_pilot import adjudication


_MAPPING_KEYS = {
    "mapping_version",
    "source_adjudicated_packet_sha256",
    "sample_size",
    "stratification",
    "entries",
}
_MAPPING_ENTRY_KEYS = {
    "repeat_id",
    "module",
    "role",
    "episode_id",
    "selection_digest",
}
_FORBIDDEN_VISIBLE_KEYS = {
    "episode_id",
    "core_id",
    "module",
    "source_artifacts",
    "source_banks",
    "source_adjudicated_packet_sha256",
    "selection_digest",
    "selected_episode_ids",
    "selected_mapping",
    "repeat_id_mapping",
}


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _load_yaml_object(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected YAML object: {path}")
    return value


def _load_json_object(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def _all_keys(value: object) -> set[str]:
    if isinstance(value, dict):
        keys = set(value)
        for child in value.values():
            keys.update(_all_keys(child))
        return keys
    if isinstance(value, list):
        keys: set[str] = set()
        for child in value:
            keys.update(_all_keys(child))
        return keys
    return set()


def _state_entries(state: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {"name": name, "value": value}
        for name, value in sorted(state.items())
    ]


def _response_fields(response_schema: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "name": name,
            "type": specification["type"],
            "min_length": specification["minLength"],
        }
        for name, specification in sorted(response_schema["properties"].items())
    ]


def _review_content(episode: dict[str, Any]) -> dict[str, Any]:
    capability_twin = episode["capability_twin"]
    execution_contract = episode["execution_contract"]
    response_schema = episode["response_schema"]
    return {
        "role": episode["role"],
        "stratum": episode["stratum"],
        "mode": episode["mode"],
        "passage_anchors": episode["passage_anchors"],
        "affected_parties": episode["affected_parties"],
        "authority_boundary": episode["authority_boundary"],
        "scenario": episode["shared_body"],
        "cue_surfaces": episode["cue_surfaces"],
        "forecast": episode["forecast_payload"],
        "task": episode["task_semantics"],
        "answer_contract": {
            "required_fields": episode["answer_semantics"]["required_fields"],
            "allowed_outcomes": episode["answer_semantics"]["allowed_outcomes"],
            "response_type": response_schema["type"],
            "additional_properties": response_schema["additionalProperties"],
            "fields": _response_fields(response_schema),
        },
        "tool_actions": episode["tool_schema"]["actions"],
        "semantic_response_tokens": episode["semantic_response_tokens"],
        "acceptable_action_band": episode["acceptable_action_band"],
        "prohibited_actions": episode["prohibited_actions"],
        "deficient_pole": episode["deficient_pole"],
        "counterfeit_pole": episode["counterfeit_pole"],
        "red_line_classes": episode["red_line_classes"],
        "capability_twin": {
            "neutral_objective": capability_twin["neutral_objective"],
            "success_condition": capability_twin["success_condition"],
            "shared_tools": capability_twin["shared_tools"],
            "shared_answer_contract": capability_twin["shared_answer_contract"],
        },
        "execution_contract": {
            "kind": execution_contract["kind"],
            "initial_state": _state_entries(execution_contract["initial_state"]),
            "allowed_actions": execution_contract["allowed_actions"],
            "terminal_observables": execution_contract["terminal_observables"],
        },
        "probe": episode["probe_payload"],
        "repair_expectations": episode["repair_expectations"],
        "behavioral_attribution": episode["behavioral_attribution"],
        "authored_judge_confidence": episode["judge_confidence"],
        "authored_contestability": episode["contestability"],
    }


def _pending_repeat_record(repeat_id: str, content: dict[str, Any]) -> dict[str, Any]:
    return {
        "repeat_id": repeat_id,
        "review_content_sha256": _canonical_sha256(content),
        "review_content": content,
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
        "notes": None,
        "reviewed_at": None,
    }


def _validate_schema(packet: dict[str, Any], root: Path) -> None:
    schema_path = root / "schemas" / "repeat-review.schema.json"
    schema = _load_json_object(schema_path)
    Draft202012Validator.check_schema(schema)
    errors = sorted(
        Draft202012Validator(schema).iter_errors(packet),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    if errors:
        detail = "; ".join(error.message for error in errors)
        raise ValueError(f"schema validation failed for {schema_path}: {detail}")


def _validate_utc_timestamp(value: str, *, field: str) -> None:
    try:
        datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except (TypeError, ValueError) as error:
        raise ValueError(f"{field} must be a valid UTC timestamp") from error


def _parse_utc_timestamp(value: str, *, field: str) -> datetime:
    _validate_utc_timestamp(value, field=field)
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")


def _validate_reviewed_record(record: dict[str, Any]) -> None:
    if record.get("review_status") != "reviewed":
        return
    repeat_id = record.get("repeat_id")
    for track in ("behavior", "interpretive"):
        applicability_decision = record.get(f"{track}_applicability_decision")
        decision = record.get(f"{track}_decision")
        if applicability_decision == "NOT_APPLICABLE":
            if decision != "NOT_APPLICABLE":
                raise ValueError(
                    f"{repeat_id}: {track} decision must be NOT_APPLICABLE"
                )
        elif decision == "NOT_APPLICABLE":
            raise ValueError(
                f"{repeat_id}: applicable {track} track cannot be NOT_APPLICABLE"
            )

    expected_rollup = adjudication.roll_up_owner_decisions(
        record["behavior_decision"], record["interpretive_decision"]
    )
    if record.get("record_decision") != expected_rollup:
        raise ValueError(
            f"{repeat_id}: record_decision must be {expected_rollup}"
        )
    record_decision = record["record_decision"]
    if record.get("confidence") == "low" and record_decision not in {
        "REVISE",
        "DEFER",
    }:
        raise ValueError(
            f"{repeat_id}: low confidence requires record decision REVISE or DEFER"
        )
    if (
        record.get("contestability") == "outside_competence"
        and record_decision != "DEFER"
    ):
        raise ValueError(
            f"{repeat_id}: outside competence requires record decision DEFER"
        )

    issues = record.get("issues") or []
    issue_ids = [issue.get("issue_id") for issue in issues]
    if len(issue_ids) != len(set(issue_ids)):
        raise ValueError(f"{repeat_id}: duplicate repeat issue ID")
    for issue in issues:
        priority = issue.get("priority")
        issue_track = issue.get("track")
        if issue_track in {"behavior", "interpretive"}:
            affected_decision = record[f"{issue_track}_decision"]
        else:
            affected_decision = record_decision
        if priority == "P0" and affected_decision != "DEFER":
            raise ValueError(
                f"{repeat_id}: P0 {issue_track} issue requires affected decision DEFER"
            )
        if priority == "P1" and affected_decision not in {"REVISE", "DEFER"}:
            raise ValueError(
                f"{repeat_id}: P1 {issue_track} issue requires affected decision "
                "REVISE or DEFER"
            )
    priorities = {issue.get("priority") for issue in issues}
    if "P0" in priorities and record_decision != "DEFER":
        raise ValueError(f"{repeat_id}: P0 requires record decision DEFER")
    if "P1" in priorities and record_decision == "APPROVE":
        raise ValueError(f"{repeat_id}: P1 cannot have record decision APPROVE")
    _validate_utc_timestamp(record["reviewed_at"], field=f"{repeat_id}.reviewed_at")


def validate_repeat_packet(
    packet: dict[str, Any], package_root: Union[str, Path]
) -> None:
    root = Path(package_root).resolve()
    _validate_schema(packet, root)
    if _FORBIDDEN_VISIBLE_KEYS.intersection(_all_keys(packet)):
        raise ValueError("repeat packet contains a forbidden judge-visible field")
    repeat_ids = [record.get("repeat_id") for record in packet.get("records", [])]
    if repeat_ids != [f"RPT-{index:03d}" for index in range(1, 11)]:
        raise ValueError("repeat packet must contain exactly RPT-001 through RPT-010")
    for record in packet["records"]:
        expected_hash = _canonical_sha256(record["review_content"])
        if record.get("review_content_sha256") != expected_hash:
            raise ValueError(
                f"{record.get('repeat_id')}: review content hash mismatch"
            )
        _validate_reviewed_record(record)
    if packet.get("review_status") == "completed":
        if any(record.get("review_status") != "reviewed" for record in packet["records"]):
            raise ValueError("completed repeat packet requires all 10 records reviewed")
        judge_id = packet["judge"]["judge_id"]
        if any(record.get("judge_id") != judge_id for record in packet["records"]):
            raise ValueError("completed repeat packet judge identity is not stable")
        _validate_utc_timestamp(packet["completed_at"], field="completed_at")


def build_repeat_packet(
    package_root: Union[str, Path],
    adjudicated_packet_path: Union[str, Path],
    mapping_path: Union[str, Path],
) -> dict[str, Any]:
    root = Path(package_root).resolve()
    packet_path = Path(adjudicated_packet_path).resolve()
    mapping_file = Path(mapping_path).resolve()
    packet_bytes = packet_path.read_bytes()
    pass_one = _load_yaml_object(packet_path)
    adjudication.validate_review_packet(pass_one, root)
    if pass_one.get("owner_review_status") != "completed":
        raise ValueError("repeat packet requires a completed pass-one adjudication")

    mapping = _load_yaml_object(mapping_file)
    if set(mapping) != _MAPPING_KEYS:
        raise ValueError("repeat mapping contains unknown or missing fields")
    entries = mapping.get("entries")
    if not isinstance(entries, list) or any(
        not isinstance(entry, dict) or set(entry) != _MAPPING_ENTRY_KEYS
        for entry in entries
    ):
        raise ValueError("repeat mapping entries contain unknown or missing fields")
    packet_sha256 = hashlib.sha256(packet_bytes).hexdigest()
    if mapping.get("source_adjudicated_packet_sha256") != packet_sha256:
        raise ValueError("repeat mapping source hash does not match pass one")
    expected_mapping = adjudication.build_repeat_mapping(pass_one, packet_sha256)
    if mapping != expected_mapping:
        raise ValueError("repeat mapping does not match registered sample geometry")

    repeat_packet = _assemble_repeat_packet(root, pass_one, mapping)

    records_by_id = {record["episode_id"]: record for record in pass_one["records"]}
    serialized = json.dumps(repeat_packet, sort_keys=True, ensure_ascii=False)
    for entry in entries:
        original = records_by_id[entry["episode_id"]]
        forbidden_values = {
            original["episode_id"],
            original["core_id"],
            original["module"],
            *(
                artifact["path"]
                for artifact in original["review_payload"]["source_artifacts"]
            ),
        }
        if any(value in serialized for value in forbidden_values):
            raise ValueError("repeat packet leaks an original record identifier")
    return repeat_packet


def _assemble_repeat_packet(
    root: Path, pass_one: dict[str, Any], mapping: dict[str, Any]
) -> dict[str, Any]:
    records_by_id = {record["episode_id"]: record for record in pass_one["records"]}
    repeat_records = []
    for entry in mapping["entries"]:
        original = records_by_id.get(entry["episode_id"])
        if original is None:
            raise ValueError("repeat mapping contains an unknown pass-one entry")
        content = _review_content(original["review_payload"])
        repeat_records.append(_pending_repeat_record(entry["repeat_id"], content))

    repeat_packet = {
        "packet_version": "blinded-repeat-review-v1",
        "classification": "single_expert_provisional_gold_repeat",
        "review_status": "pending",
        "judge": None,
        "completed_at": None,
        "records": repeat_records,
        "record_rollup_rule": {
            "version": "dual-track-rollup-v1",
            "behavior_decision_field": "behavior_decision",
            "interpretive_decision_field": "interpretive_decision",
            "record_decision_field": "record_decision",
            "applicable_track_decisions": [
                "APPROVE",
                "REVISE",
                "REJECT",
                "DEFER",
            ],
            "not_applicable_value": "NOT_APPLICABLE",
            "not_applicable_handling": "ignored",
            "precedence": ["DEFER", "REJECT", "REVISE", "APPROVE"],
            "no_applicable_tracks_result": "DEFER",
        },
    }
    validate_repeat_packet(repeat_packet, root)
    return repeat_packet


def _file_entry_from_bytes(content: bytes, *, relative_path: str) -> dict[str, Any]:
    return {
        "path": relative_path,
        "sha256": hashlib.sha256(content).hexdigest(),
        "bytes": len(content),
    }


def _json_bytes(value: dict[str, Any]) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def _applicability_agreement(
    pass_one: dict[str, Any],
    mapping: dict[str, Any],
    repeat_packet: dict[str, Any],
) -> dict[str, Any]:
    pass_one_by_id = {
        record["episode_id"]: record for record in pass_one["records"]
    }
    repeat_by_id = {
        record["repeat_id"]: record for record in repeat_packet["records"]
    }
    counts = {"behavior": 0, "interpretive": 0}
    for entry in mapping["entries"]:
        pass_record = pass_one_by_id[entry["episode_id"]]
        repeat_record = repeat_by_id[entry["repeat_id"]]
        for track in counts:
            pass_one_applicability = (
                "NOT_APPLICABLE"
                if pass_record[f"owner_{track}_decision"] == "NOT_APPLICABLE"
                else "APPLICABLE"
            )
            if (
                repeat_record[f"{track}_applicability_decision"]
                == pass_one_applicability
            ):
                counts[track] += 1
    return {
        "basis": "pass_one_track_decision_vs_fresh_repeat_applicability_v1",
        "behavior": {"exact_agreement_count": counts["behavior"], "denominator": 10},
        "interpretive": {
            "exact_agreement_count": counts["interpretive"],
            "denominator": 10,
        },
        "overall": {
            "exact_agreement_count": counts["behavior"] + counts["interpretive"],
            "denominator": 20,
        },
    }


def _yaml_bytes(value: dict[str, Any]) -> bytes:
    return yaml.safe_dump(
        value, allow_unicode=True, sort_keys=False, width=88
    ).encode("utf-8")


def _write_exclusive_outputs(
    outputs: tuple[tuple[Path, bytes], ...], *, error_prefix: str
) -> None:
    if any(path.exists() for path, _ in outputs):
        raise FileExistsError(f"{error_prefix}: {outputs[0][0].parent}")
    for path, content in outputs:
        with path.open("xb") as stream:
            stream.write(content)


def export_repeat_packet(
    package_root: Union[str, Path],
    adjudicated_packet_path: Union[str, Path],
    mapping_path: Union[str, Path],
    output_dir: Union[str, Path],
) -> tuple[Path, Path]:
    root = Path(package_root).resolve()
    packet = build_repeat_packet(root, adjudicated_packet_path, mapping_path)
    packet_bytes = _yaml_bytes(packet)
    destination = Path(output_dir)
    if not destination.is_absolute():
        destination = root / destination
    destination.mkdir(parents=True, exist_ok=True)
    packet_path = destination / "blinded-repeat-review.yaml"
    manifest_path = destination / "blinded-repeat-packet-manifest.json"

    schema_path = root / "schemas" / "repeat-review.schema.json"
    schema_bytes = schema_path.read_bytes()
    manifest = {
        "manifest_version": "blinded-repeat-packet-manifest-v1",
        "classification": "single_expert_provisional_gold_repeat",
        "review_status": "pending",
        "record_count": 10,
        "inputs": {
            "repeat_review_schema": _file_entry_from_bytes(
                schema_bytes, relative_path="schemas/repeat-review.schema.json"
            )
        },
        "artifacts": [
            _file_entry_from_bytes(packet_bytes, relative_path=packet_path.name)
        ],
    }
    manifest_bytes = _json_bytes(manifest)
    _write_exclusive_outputs(
        ((packet_path, packet_bytes), (manifest_path, manifest_bytes)),
        error_prefix="immutable repeat output already exists",
    )
    return packet_path, manifest_path


def finalize_repeat_packet(
    package_root: Union[str, Path],
    reviewed_packet_path: Union[str, Path],
    output_dir: Union[str, Path],
    *,
    source_packet_path: Union[str, Path],
    source_manifest_path: Union[str, Path],
    completed_pass_one_path: Union[str, Path],
    judge: dict[str, str],
    completed_at: str,
) -> tuple[Path, Path]:
    root = Path(package_root).resolve()
    source_path = Path(source_packet_path).resolve()
    source_manifest_file = Path(source_manifest_path).resolve()
    pass_one_path = Path(completed_pass_one_path).resolve()
    pass_one_bytes = pass_one_path.read_bytes()
    pass_one = _load_yaml_object(pass_one_path)
    adjudication.validate_review_packet(pass_one, root)
    if pass_one.get("owner_review_status") != "completed":
        raise ValueError("repeat finalization requires a completed pass-one packet")

    source_bytes = source_path.read_bytes()
    source_packet = _load_yaml_object(source_path)
    validate_repeat_packet(source_packet, root)
    mapping = adjudication.build_repeat_mapping(
        pass_one, hashlib.sha256(pass_one_bytes).hexdigest()
    )
    expected_source = _assemble_repeat_packet(root, pass_one, mapping)
    schema_path = root / "schemas" / "repeat-review.schema.json"
    expected_manifest = {
        "manifest_version": "blinded-repeat-packet-manifest-v1",
        "classification": "single_expert_provisional_gold_repeat",
        "review_status": "pending",
        "record_count": 10,
        "inputs": {
            "repeat_review_schema": _file_entry_from_bytes(
                schema_path.read_bytes(),
                relative_path="schemas/repeat-review.schema.json",
            )
        },
        "artifacts": [
            _file_entry_from_bytes(
                source_bytes, relative_path="blinded-repeat-review.yaml"
            )
        ],
    }
    source_manifest = _load_json_object(source_manifest_file)
    if source_packet != expected_source or source_manifest != expected_manifest:
        raise ValueError(
            "immutable exported repeat packet or manifest does not authenticate"
        )

    input_path = Path(reviewed_packet_path).resolve()
    reviewed_packet = _load_yaml_object(input_path)
    validate_repeat_packet(reviewed_packet, root)
    immutable_top_fields = {
        "packet_version",
        "classification",
        "record_rollup_rule",
    }
    if any(
        reviewed_packet.get(field) != source_packet.get(field)
        for field in immutable_top_fields
    ) or len(reviewed_packet.get("records", [])) != len(source_packet["records"]):
        raise ValueError("review submission differs from immutable exported repeat packet")
    for reviewed_record, source_record in zip(
        reviewed_packet["records"], source_packet["records"]
    ):
        for field in ("repeat_id", "review_content_sha256", "review_content"):
            if reviewed_record.get(field) != source_record.get(field):
                raise ValueError(
                    "review submission differs from immutable exported repeat packet"
                )
    if reviewed_packet.get("review_status") != "pending":
        raise ValueError("finalization requires a pending repeat submission")
    if len(reviewed_packet.get("records", [])) != 10 or any(
        record.get("review_status") != "reviewed"
        for record in reviewed_packet.get("records", [])
    ):
        raise ValueError("all 10 fresh repeat judgments must be reviewed")
    if judge != pass_one.get("owner_judge"):
        raise ValueError("repeat judge must exactly match the completed pass-one judge")
    judge_id = judge.get("judge_id")
    if any(
        record.get("judge_id") != judge_id
        for record in reviewed_packet["records"]
    ):
        raise ValueError("judge identity must be stable across all repeat records")
    pass_one_completed_at = _parse_utc_timestamp(
        pass_one["owner_completed_at"], field="pass_one.owner_completed_at"
    )
    repeat_completed_at = _parse_utc_timestamp(completed_at, field="completed_at")
    for record in reviewed_packet["records"]:
        reviewed_at = _parse_utc_timestamp(
            record["reviewed_at"], field=f"{record['repeat_id']}.reviewed_at"
        )
        if reviewed_at <= pass_one_completed_at:
            raise ValueError("each repeat judgment must occur strictly after pass one")
        if reviewed_at > repeat_completed_at:
            raise ValueError(
                "repeat completion must occur at or after repeat judgment timestamps"
            )

    completed_packet = json.loads(json.dumps(reviewed_packet, ensure_ascii=False))
    completed_packet["review_status"] = "completed"
    completed_packet["judge"] = judge
    completed_packet["completed_at"] = completed_at
    validate_repeat_packet(completed_packet, root)
    packet_bytes = _yaml_bytes(completed_packet)

    destination = Path(output_dir)
    if not destination.is_absolute():
        destination = root / destination
    destination.mkdir(parents=True, exist_ok=True)
    packet_path = destination / "frozen-blinded-repeat-review.yaml"
    manifest_path = destination / "frozen-blinded-repeat-manifest.json"
    input_bytes = input_path.read_bytes()
    manifest = {
        "manifest_version": "frozen-blinded-repeat-manifest-v1",
        "classification": "single_expert_provisional_gold_repeat",
        "review_status": "completed",
        "judge": judge,
        "completed_at": completed_at,
        "record_count": 10,
        "applicability_agreement": _applicability_agreement(
            pass_one, mapping, completed_packet
        ),
        "source_repeat_packet": _file_entry_from_bytes(
            input_bytes, relative_path="submitted-blinded-repeat-review.yaml"
        ),
        "artifacts": [
            _file_entry_from_bytes(packet_bytes, relative_path=packet_path.name)
        ],
    }
    manifest_bytes = _json_bytes(manifest)
    _write_exclusive_outputs(
        ((packet_path, packet_bytes), (manifest_path, manifest_bytes)),
        error_prefix="immutable frozen repeat output already exists",
    )
    return packet_path, manifest_path
