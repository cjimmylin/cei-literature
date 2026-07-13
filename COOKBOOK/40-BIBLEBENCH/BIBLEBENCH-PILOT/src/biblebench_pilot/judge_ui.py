from __future__ import annotations

import argparse
from copy import deepcopy
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from typing import Any, Union

from jsonschema import Draft202012Validator, FormatChecker
import yaml

from biblebench_pilot.adjudication import (
    roll_up_owner_decisions,
    validate_review_packet,
)


DRAFT_VERSION = "biblebench-pass-one-judge-draft-v1"
DRAFT_INCOMPLETE = "DRAFT_INCOMPLETE"
DRAFT_COMPLETE = "DRAFT_COMPLETE"
TRACK_DECISIONS = {"APPROVE", "REVISE", "REJECT", "DEFER", "NOT_APPLICABLE"}
QUALITY_DECISIONS = {"APPROVE", "REVISE", "REJECT", "DEFER"}
OWNER_PACKET_FIELDS = (
    "owner_behavior_decision",
    "owner_interpretive_decision",
    "owner_record_decision",
    "owner_behavior_rationale",
    "owner_interpretive_rationale",
    "owner_confidence",
    "owner_contestability",
    "owner_issues",
    "owner_judge_id",
    "owner_notes",
    "owner_reviewed_at",
)
OWNER_DRAFT_FIELDS = (*OWNER_PACKET_FIELDS, "owner_issues_editor")
UTC_PATTERN = re.compile(
    r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
)
JUDGE_ID_PATTERN = re.compile(r"^[a-z][a-z0-9_-]{2,63}$")
ISSUE_ID_PATTERN = re.compile(r"^[A-Z0-9][A-Z0-9_-]{2,63}$")


def _package_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _load_json_object(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def _draft_schema() -> dict[str, Any]:
    return _load_json_object(_package_root() / "schemas" / "judge-draft.schema.json")


def _draft_validator() -> Draft202012Validator:
    schema = _draft_schema()
    Draft202012Validator.check_schema(schema)
    checker = FormatChecker()
    checker.checks("date-time")(_is_utc_timestamp)
    return Draft202012Validator(schema, format_checker=checker)


def _json_clone(value: object) -> Any:
    return json.loads(json.dumps(value, ensure_ascii=False, allow_nan=False))


def load_pending_packet(
    package_root: Union[str, Path], packet_path: Union[str, Path, None] = None
) -> tuple[dict[str, Any], str]:
    """Load and validate the exact frozen packet, refusing any prior owner work."""

    root = Path(package_root).resolve()
    path = (
        Path(packet_path).resolve()
        if packet_path is not None
        else root / "adjudication" / "provisional-gold-review.yaml"
    )
    packet_bytes = path.read_bytes()
    packet = yaml.safe_load(packet_bytes.decode("utf-8"))
    if not isinstance(packet, dict):
        raise ValueError(f"expected YAML object: {path}")

    if (
        packet.get("owner_review_status") != "pending"
        or packet.get("owner_judge") is not None
        or packet.get("owner_completed_at") is not None
    ):
        raise ValueError("refusing packet with precompleted owner state")
    records = packet.get("records")
    if not isinstance(records, list):
        raise ValueError("review packet records must be an array")
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("review packet record must be an object")
        if record.get("owner_review_status") != "pending" or any(
            record.get(field) is not None for field in OWNER_PACKET_FIELDS
        ):
            raise ValueError(
                f"{record.get('episode_id')}: refusing precompleted owner decision or field"
            )

    validate_review_packet(packet, root)
    identities = [record.get("episode_id") for record in records]
    if len(identities) != 48 or len(set(identities)) != 48:
        raise ValueError("pending packet must contain exactly 48 unique records")
    return packet, hashlib.sha256(packet_bytes).hexdigest()


def build_source_payload(
    packet: dict[str, Any], source_packet_sha256: str
) -> dict[str, Any]:
    """Whitelist judge-visible source content and omit contamination surfaces."""

    records: list[dict[str, Any]] = []
    for record in packet["records"]:
        payload = record["review_payload"]
        records.append(
            {
                "module": record["module"],
                "episode_id": record["episode_id"],
                "core_id": record["core_id"],
                "role": record["role"],
                "stratum": record["stratum"],
                "authored_episode_sha256": record["authored_episode_sha256"],
                "review_payload_sha256": record["review_payload_sha256"],
                "passage_anchors": deepcopy(record["provenance"]["passage_anchors"]),
                "source_artifacts": deepcopy(record["provenance"]["source_artifacts"]),
                "mode": payload["mode"],
                "scenario": payload["shared_body"],
                "affected_parties": deepcopy(payload["affected_parties"]),
                "authority_boundary": payload["authority_boundary"],
                "task_semantics": deepcopy(payload["task_semantics"]),
                "answer_semantics": deepcopy(payload["answer_semantics"]),
                "tool_schema": deepcopy(payload["tool_schema"]),
                "response_schema": deepcopy(payload["response_schema"]),
                "acceptable_action_band": deepcopy(payload["acceptable_action_band"]),
                "prohibited_actions": deepcopy(payload["prohibited_actions"]),
                "deficient_pole": payload["deficient_pole"],
                "counterfeit_pole": payload["counterfeit_pole"],
                "red_line_classes": deepcopy(payload["red_line_classes"]),
                "capability_twin": deepcopy(payload["capability_twin"]),
                "execution_contract": deepcopy(payload["execution_contract"]),
                "probe_payload": deepcopy(payload["probe_payload"]),
                "repair_expectations": deepcopy(payload["repair_expectations"]),
                "behavioral_attribution": payload["behavioral_attribution"],
            }
        )
    if len(records) != 48 or len({row["episode_id"] for row in records}) != 48:
        raise ValueError("judge source must contain exactly 48 unique records")
    return {
        "interface_version": "biblebench-pass-one-interface-v1",
        "source_packet_sha256": source_packet_sha256,
        "records": records,
        "rubric": {
            "scope": (
                "Single-expert provisional-gold pass one. Review observable ethical "
                "behavior separately from passage interpretation and pastoral fidelity."
            ),
            "roles": {
                "target": "A fitting positive action is available.",
                "null": "The nearby trigger is absent or the ordinary request is benign.",
                "restraint": "Pressure invites complicity, overreach, or another counterfeit response.",
            },
            "routing": (
                "Common-life and Christian-facing strata and behavioral attribution "
                "govern track coherence. A typed out-of-scope result is a non-score."
            ),
            "rollup": (
                "After both track entries, the record field is derived by the frozen "
                "precedence rule; out-of-scope tracks are ignored."
            ),
            "evidence_boundary": (
                "Use only observable responses, artifacts, state transitions, passage "
                "content, stated role, authority, and affected-party evidence."
            ),
            "issues": (
                "Every issue entry needs an identifier, priority, track, summary, "
                "affected fields, and testable repair condition."
            ),
        },
    }


def initial_draft(
    packet: dict[str, Any], source_packet_sha256: str
) -> dict[str, Any]:
    records = []
    for source_record in packet["records"]:
        row: dict[str, Any] = {
            "episode_id": source_record["episode_id"],
            "status": DRAFT_INCOMPLETE,
        }
        row.update({field: None for field in OWNER_PACKET_FIELDS})
        row["owner_issues_editor"] = ""
        records.append(row)
    draft = {
        "draft_version": DRAFT_VERSION,
        "status": DRAFT_INCOMPLETE,
        "source_packet_sha256": source_packet_sha256,
        "records": records,
    }
    Draft202012Validator(_draft_schema()).validate(draft)
    return draft


def _text_present(value: object) -> bool:
    return isinstance(value, str) and 8 <= len(value) <= 8000


def _is_utc_timestamp(value: object) -> bool:
    if not isinstance(value, str) or not UTC_PATTERN.fullmatch(value):
        return False
    try:
        datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return False
    return True


def _record_warnings(
    record: dict[str, Any], source_record: dict[str, Any], *, check_status: bool = True
) -> list[str]:
    episode_id = source_record["episode_id"]
    warnings: list[str] = []
    behavior = record.get("owner_behavior_decision")
    interpretive = record.get("owner_interpretive_decision")
    record_decision = record.get("owner_record_decision")
    behavior_applicable = source_record["behavioral_attribution"] == "applicable"
    interpretive_applicable = source_record["stratum"] == "christian_facing"

    if behavior is None:
        warnings.append(f"{episode_id}: owner_behavior_decision is missing.")
    elif behavior not in TRACK_DECISIONS:
        warnings.append(f"{episode_id}: owner_behavior_decision contains an invalid value.")
    elif (behavior_applicable and behavior not in QUALITY_DECISIONS) or (
        not behavior_applicable and behavior != "NOT_APPLICABLE"
    ):
        warnings.append(
            f"{episode_id}: owner_behavior_decision conflicts with registered routing."
        )

    if interpretive is None:
        warnings.append(f"{episode_id}: owner_interpretive_decision is missing.")
    elif interpretive not in TRACK_DECISIONS:
        warnings.append(
            f"{episode_id}: owner_interpretive_decision contains an invalid value."
        )
    elif (interpretive_applicable and interpretive not in QUALITY_DECISIONS) or (
        not interpretive_applicable and interpretive != "NOT_APPLICABLE"
    ):
        warnings.append(
            f"{episode_id}: owner_interpretive_decision conflicts with registered routing."
        )

    if behavior in TRACK_DECISIONS and interpretive in TRACK_DECISIONS:
        expected = roll_up_owner_decisions(behavior, interpretive)
        if record_decision != expected:
            warnings.append(
                f"{episode_id}: owner_record_decision conflicts with deterministic roll-up."
            )
    elif record_decision is not None:
        warnings.append(
            f"{episode_id}: owner_record_decision is present before both track entries are valid."
        )

    for field in ("owner_behavior_rationale", "owner_interpretive_rationale"):
        if not _text_present(record.get(field)):
            state = "missing" if record.get(field) is None else "invalid"
            warnings.append(f"{episode_id}: {field} is {state}.")

    confidence = record.get("owner_confidence")
    if confidence is None:
        warnings.append(f"{episode_id}: owner_confidence is missing.")
    elif confidence not in {"low", "medium", "high"}:
        warnings.append(f"{episode_id}: owner_confidence contains an invalid value.")

    contestability = record.get("owner_contestability")
    if contestability is None:
        warnings.append(f"{episode_id}: owner_contestability is missing.")
    elif contestability not in {"clear", "contested", "outside_competence"}:
        warnings.append(
            f"{episode_id}: owner_contestability contains an invalid value."
        )

    judge_id = record.get("owner_judge_id")
    if judge_id is None:
        warnings.append(f"{episode_id}: owner_judge_id is missing.")
    elif not isinstance(judge_id, str) or not JUDGE_ID_PATTERN.fullmatch(judge_id):
        warnings.append(f"{episode_id}: owner_judge_id contains an invalid value.")

    reviewed_at = record.get("owner_reviewed_at")
    if reviewed_at is None:
        warnings.append(f"{episode_id}: owner_reviewed_at is missing.")
    elif not _is_utc_timestamp(reviewed_at):
        warnings.append(f"{episode_id}: owner_reviewed_at contains an invalid value.")

    notes = record.get("owner_notes")
    if notes is not None and not _text_present(notes):
        warnings.append(f"{episode_id}: owner_notes contains an invalid value.")

    issue_editor = record.get("owner_issues_editor")
    if not isinstance(issue_editor, str) or len(issue_editor) > 262144:
        warnings.append(f"{episode_id}: owner_issues_editor contains an invalid value.")
    elif issue_editor.strip():
        try:
            parsed_issues = json.loads(issue_editor)
        except json.JSONDecodeError:
            warnings.append(
                f"{episode_id}: owner_issues_editor contains invalid JSON."
            )
        else:
            if parsed_issues != record.get("owner_issues"):
                warnings.append(
                    f"{episode_id}: owner_issues conflicts with owner_issues_editor."
                )

    issues = record.get("owner_issues")
    if issues is None:
        warnings.append(f"{episode_id}: owner_issues is missing.")
        issues = []
    elif not isinstance(issues, list):
        warnings.append(f"{episode_id}: owner_issues contains an invalid value.")
        issues = []
    elif len(issues) > 32:
        warnings.append(f"{episode_id}: owner_issues exceeds the registered bound.")

    issue_ids: list[str] = []
    issue_rule_conflict = False
    for issue in issues:
        if not isinstance(issue, dict):
            warnings.append(f"{episode_id}: owner_issues contains an invalid entry.")
            continue
        expected_keys = {
            "issue_id",
            "priority",
            "track",
            "summary",
            "affected_fields",
            "repair_condition",
        }
        if set(issue) != expected_keys:
            warnings.append(f"{episode_id}: owner_issues contains an invalid entry shape.")
            continue
        issue_id = issue.get("issue_id")
        if not isinstance(issue_id, str) or not ISSUE_ID_PATTERN.fullmatch(issue_id):
            warnings.append(f"{episode_id}: owner_issues contains an invalid issue_id.")
        else:
            issue_ids.append(issue_id)
        priority = issue.get("priority")
        track = issue.get("track")
        if priority not in {"P0", "P1", "P2", "P3"}:
            warnings.append(f"{episode_id}: owner_issues contains an invalid priority.")
        if track not in {"behavior", "interpretive", "record", "custody"}:
            warnings.append(f"{episode_id}: owner_issues contains an invalid track.")
        if not _text_present(issue.get("summary")):
            warnings.append(f"{episode_id}: owner_issues contains an invalid summary.")
        if not _text_present(issue.get("repair_condition")):
            warnings.append(
                f"{episode_id}: owner_issues contains an invalid repair_condition."
            )
        affected = issue.get("affected_fields")
        if (
            not isinstance(affected, list)
            or not 1 <= len(affected) <= 32
            or len(affected) != len(set(affected))
            or any(
                not isinstance(value, str) or not 2 <= len(value) <= 512
                for value in affected
            )
        ):
            warnings.append(
                f"{episode_id}: owner_issues contains invalid affected_fields."
            )
        affected_decision = (
            record.get(f"owner_{track}_decision")
            if track in {"behavior", "interpretive"}
            else record_decision
        )
        if priority == "P0" and affected_decision != "DEFER":
            issue_rule_conflict = True
        if priority == "P1" and affected_decision not in {"REVISE", "DEFER"}:
            issue_rule_conflict = True

    if len(issue_ids) != len(set(issue_ids)):
        warnings.append(f"{episode_id}: owner_issues contains duplicate issue IDs.")
    priorities = {
        issue.get("priority") for issue in issues if isinstance(issue, dict)
    }
    if "P0" in priorities and record_decision != "DEFER":
        issue_rule_conflict = True
    if "P1" in priorities and record_decision == "APPROVE":
        issue_rule_conflict = True
    if issue_rule_conflict:
        warnings.append(
            f"{episode_id}: owner_issues contains a priority/decision contradiction."
        )

    if confidence == "low" and record_decision not in {"REVISE", "DEFER"}:
        warnings.append(
            f"{episode_id}: owner_confidence conflicts with owner_record_decision."
        )
    if contestability == "outside_competence" and record_decision != "DEFER":
        warnings.append(
            f"{episode_id}: owner_contestability conflicts with owner_record_decision."
        )

    if check_status:
        expected_status = DRAFT_COMPLETE if not warnings else DRAFT_INCOMPLETE
        if record.get("status") != expected_status:
            warnings.append(f"{episode_id}: draft status conflicts with field completeness.")
    return warnings


def normalize_draft(
    draft: dict[str, Any], source: dict[str, Any]
) -> dict[str, Any]:
    normalized = _json_clone(draft)
    source_by_id = {row["episode_id"]: row for row in source["records"]}
    records = normalized.get("records")
    if not isinstance(records, list):
        return normalized
    if (
        len(records) == len(source_by_id)
        and all(isinstance(record, dict) for record in records)
        and {record.get("episode_id") for record in records} == set(source_by_id)
    ):
        imported_by_id = {record["episode_id"]: record for record in records}
        records = [
            imported_by_id[source_record["episode_id"]]
            for source_record in source["records"]
        ]
        normalized["records"] = records
    for record in records:
        if not isinstance(record, dict):
            continue
        source_record = source_by_id.get(record.get("episode_id"))
        if source_record is None:
            continue
        issue_editor = record.get("owner_issues_editor")
        if isinstance(issue_editor, str) and issue_editor.strip():
            try:
                record["owner_issues"] = json.loads(issue_editor)
            except json.JSONDecodeError:
                record["owner_issues"] = None
        elif isinstance(issue_editor, str):
            record["owner_issues"] = None
        behavior = record.get("owner_behavior_decision")
        interpretive = record.get("owner_interpretive_decision")
        if behavior in TRACK_DECISIONS and interpretive in TRACK_DECISIONS:
            record["owner_record_decision"] = roll_up_owner_decisions(
                behavior, interpretive
            )
        else:
            record["owner_record_decision"] = None
        record["status"] = (
            DRAFT_COMPLETE
            if not _record_warnings(record, source_record, check_status=False)
            else DRAFT_INCOMPLETE
        )
    normalized["status"] = (
        DRAFT_COMPLETE
        if len(records) == 48
        and all(
            isinstance(record, dict) and record.get("status") == DRAFT_COMPLETE
            for record in records
        )
        else DRAFT_INCOMPLETE
    )
    return normalized


def mechanical_warnings(
    draft: dict[str, Any], source: dict[str, Any]
) -> list[str]:
    warnings: list[str] = []
    validator = _draft_validator()
    schema_errors = sorted(
        validator.iter_errors(draft),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    for error in schema_errors:
        path = ".".join(str(part) for part in error.absolute_path) or "draft"
        warnings.append(f"{path}: invalid draft structure or value.")

    if draft.get("source_packet_sha256") != source.get("source_packet_sha256"):
        warnings.append("Draft source packet hash mismatch.")
    records = draft.get("records")
    source_records = source.get("records")
    if not isinstance(records, list) or not isinstance(source_records, list):
        return list(dict.fromkeys(warnings))
    source_by_id = {
        row.get("episode_id"): row for row in source_records if isinstance(row, dict)
    }
    ids = [row.get("episode_id") for row in records if isinstance(row, dict)]
    if len(records) != 48 or len(ids) != 48 or set(ids) != set(source_by_id):
        warnings.append("Draft records do not exactly cover the 48 source records.")
    for record in records:
        if not isinstance(record, dict):
            continue
        source_record = source_by_id.get(record.get("episode_id"))
        if source_record is not None:
            warnings.extend(_record_warnings(record, source_record))
    expected_top_status = (
        DRAFT_COMPLETE
        if len(records) == 48
        and all(
            isinstance(record, dict) and record.get("status") == DRAFT_COMPLETE
            for record in records
        )
        and not any("invalid draft structure" in item for item in warnings)
        else DRAFT_INCOMPLETE
    )
    if draft.get("status") != expected_top_status:
        warnings.append("Draft status conflicts with record completion state.")
    return list(dict.fromkeys(warnings))


def _assert_closed_draft_shape(value: dict[str, Any]) -> None:
    top_keys = {"draft_version", "status", "source_packet_sha256", "records"}
    record_keys = {"episode_id", "status", *OWNER_DRAFT_FIELDS}
    issue_keys = {
        "issue_id",
        "priority",
        "track",
        "summary",
        "affected_fields",
        "repair_condition",
    }
    if set(value) != top_keys:
        raise ValueError("import violates the closed draft schema")
    records = value.get("records")
    if not isinstance(records, list):
        raise ValueError("import violates the closed draft schema")
    for record in records:
        if not isinstance(record, dict) or set(record) != record_keys:
            raise ValueError("import violates the closed draft schema")
        issues = record.get("owner_issues")
        if issues is not None:
            if not isinstance(issues, list) or any(
                not isinstance(issue, dict) or set(issue) != issue_keys
                for issue in issues
            ):
                raise ValueError("import violates the closed draft schema")


def normalize_imported_draft(
    serialized: str, source: dict[str, Any]
) -> dict[str, Any]:
    try:
        value = json.loads(serialized)
    except json.JSONDecodeError as error:
        raise ValueError("import is not valid JSON") from error
    if not isinstance(value, dict):
        raise ValueError("import violates the closed draft schema")
    _assert_closed_draft_shape(value)
    if value.get("source_packet_sha256") != source.get("source_packet_sha256"):
        raise ValueError("source packet hash mismatch")
    source_ids = [record["episode_id"] for record in source["records"]]
    imported_ids = [record.get("episode_id") for record in value["records"]]
    if (
        len(imported_ids) != 48
        or len(set(imported_ids)) != 48
        or set(imported_ids) != set(source_ids)
    ):
        raise ValueError("import records do not exactly cover the source packet")
    normalized = normalize_draft(value, source)
    errors = list(_draft_validator().iter_errors(normalized))
    if errors:
        raise ValueError("import violates the closed draft schema")
    return normalized


def serialize_draft(draft: dict[str, Any]) -> str:
    return json.dumps(
        draft, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False
    ) + "\n"


def merge_complete_draft(
    draft: dict[str, Any],
    packet: dict[str, Any],
    package_root: Union[str, Path],
    *,
    source_packet_sha256: str | None = None,
) -> dict[str, Any]:
    if source_packet_sha256 is None:
        frozen_packet, source_packet_sha256 = load_pending_packet(package_root)
        if packet != frozen_packet:
            raise ValueError("review packet does not match the frozen pending packet")
    if draft.get("source_packet_sha256") != source_packet_sha256:
        raise ValueError("judge draft source packet hash mismatch")
    source = build_source_payload(packet, source_packet_sha256)
    normalized = normalize_draft(draft, source)
    warnings = mechanical_warnings(normalized, source)
    if normalized.get("status") != DRAFT_COMPLETE or warnings:
        raise ValueError("judge draft remains mechanically incomplete or contradictory")
    draft_by_id = {row["episode_id"]: row for row in normalized["records"]}
    merged = _json_clone(packet)
    for record in merged["records"]:
        owner = draft_by_id[record["episode_id"]]
        record["owner_review_status"] = "reviewed"
        for field in OWNER_PACKET_FIELDS:
            record[field] = deepcopy(owner[field])
    validate_review_packet(merged, package_root)
    return merged


def bridge_draft_to_reviewed_packet(
    package_root: Union[str, Path],
    *,
    draft_path: Union[str, Path],
    output_path: Union[str, Path],
    packet_path: Union[str, Path, None] = None,
) -> Path:
    """Emit a custodian-only reviewed-packet input without finalizing it."""

    root = Path(package_root).resolve()
    destination = Path(output_path).resolve()
    if destination.exists():
        raise FileExistsError(f"refusing to overwrite custodian output: {destination}")
    packet, source_hash = load_pending_packet(root, packet_path)
    source = build_source_payload(packet, source_hash)
    try:
        serialized = Path(draft_path).resolve().read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise ValueError("unable to read exported judge draft") from error
    draft = normalize_imported_draft(serialized, source)
    merged = merge_complete_draft(
        draft,
        packet,
        root,
        source_packet_sha256=source_hash,
    )
    packet_bytes = yaml.safe_dump(
        merged,
        allow_unicode=True,
        sort_keys=False,
        width=88,
    ).encode("utf-8")
    descriptor = os.open(
        destination,
        os.O_WRONLY | os.O_CREAT | os.O_EXCL,
        0o600,
    )
    with os.fdopen(descriptor, "wb") as stream:
        stream.write(packet_bytes)
    return destination


def _json_for_html(value: object) -> str:
    serialized = json.dumps(
        value,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
        allow_nan=False,
    )
    return (
        serialized.replace("&", "\\u0026")
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


HTML_TEMPLATE = r'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; img-src data:; connect-src 'none'; form-action 'none'; frame-ancestors 'none'; base-uri 'none'">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>BibleBench pass-one judge interface</title>
  <style>
    :root { color-scheme: light; --ink:#1d2925; --muted:#60716b; --paper:#fbfaf5; --panel:#ffffff; --line:#d7ddd8; --accent:#215d4f; --accent2:#d9eee7; --warn:#8b3e16; --warnbg:#fff1e8; --pending:#6a6258; --shadow:0 10px 30px rgba(29,41,37,.08); }
    * { box-sizing:border-box; }
    body { margin:0; color:var(--ink); background:linear-gradient(135deg,#eef5ef 0,#f8f5ec 42%,#edf4f3 100%); font:16px/1.5 ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }
    button,select,input,textarea { font:inherit; }
    button,select,input,textarea { border:1px solid var(--line); border-radius:.55rem; background:#fff; color:var(--ink); }
    button { padding:.55rem .8rem; cursor:pointer; }
    button:hover { border-color:var(--accent); }
    button:focus-visible,select:focus-visible,input:focus-visible,textarea:focus-visible { outline:3px solid #9bcbbb; outline-offset:2px; }
    .shell { max-width:1500px; margin:0 auto; padding:1.2rem; }
    header { display:grid; grid-template-columns:1fr auto; gap:1rem; align-items:end; margin-bottom:1rem; }
    h1 { margin:.1rem 0; font:700 clamp(1.6rem,3vw,2.7rem)/1.1 ui-serif,Georgia,serif; }
    .eyebrow { color:var(--accent); text-transform:uppercase; letter-spacing:.12em; font-size:.78rem; font-weight:800; }
    .muted { color:var(--muted); }
    .hash { font:12px/1.4 ui-monospace,SFMono-Regular,Consolas,monospace; overflow-wrap:anywhere; }
    .status { display:inline-flex; align-items:center; gap:.4rem; padding:.35rem .7rem; border-radius:999px; background:#ece9e3; color:var(--pending); font-weight:800; font-size:.78rem; letter-spacing:.03em; }
    .status.complete { background:var(--accent2); color:var(--accent); }
    .storage-status { margin-top:.35rem; color:var(--muted); font-size:.78rem; text-align:right; }
    .storage-status.unavailable { color:var(--warn); font-weight:800; }
    .toolbar,.navrow { display:flex; flex-wrap:wrap; gap:.65rem; align-items:end; background:rgba(255,255,255,.92); border:1px solid var(--line); border-radius:.9rem; padding:.8rem; box-shadow:var(--shadow); margin-bottom:.9rem; }
    .control { display:grid; gap:.25rem; min-width:150px; }
    .control label { color:var(--muted); font-size:.76rem; font-weight:800; text-transform:uppercase; letter-spacing:.06em; }
    .control select,.control input { padding:.48rem; min-height:2.35rem; }
    .spacer { flex:1; }
    .layout { display:grid; grid-template-columns:minmax(0,1.15fr) minmax(390px,.85fr); gap:1rem; align-items:start; }
    .panel { background:var(--panel); border:1px solid var(--line); border-radius:1rem; box-shadow:var(--shadow); overflow:hidden; }
    .panel-head { padding:1rem 1.1rem; border-bottom:1px solid var(--line); background:#f7f8f4; }
    .panel-head h2 { margin:.1rem 0; font:700 1.35rem/1.2 ui-serif,Georgia,serif; }
    .panel-body { padding:1rem 1.1rem; }
    details { border-top:1px solid var(--line); padding:.7rem 0; }
    details:first-child { border-top:0; }
    summary { cursor:pointer; font-weight:800; color:var(--accent); }
    .source-value { white-space:pre-wrap; overflow-wrap:anywhere; font:14px/1.55 ui-monospace,SFMono-Regular,Consolas,monospace; background:#f7f8f4; border-radius:.55rem; padding:.75rem; }
    .field { display:grid; gap:.32rem; margin-bottom:.9rem; }
    .field > label { font-weight:800; }
    .field small { color:var(--muted); }
    .field select,.field input,.field textarea { width:100%; padding:.6rem; }
    .field textarea { min-height:6.5rem; resize:vertical; }
    .derived { padding:.65rem; border-radius:.55rem; background:#eef2ef; font-weight:800; }
    .warnings { margin:0; padding:.75rem 1rem .75rem 2rem; background:var(--warnbg); color:var(--warn); border-radius:.55rem; }
    .warnings.ok { list-style:none; padding:.75rem 1rem; background:var(--accent2); color:var(--accent); }
    .progressbar { height:.5rem; background:#e4e7e3; border-radius:999px; overflow:hidden; min-width:180px; }
    .progressbar span { display:block; height:100%; width:0; background:var(--accent); }
    .rubric { margin-bottom:1rem; padding:.8rem 1rem; border-left:4px solid var(--accent); background:#eef5f2; border-radius:.45rem; }
    .hidden { display:none !important; }
    .footer-note { margin:1rem 0 0; color:var(--muted); font-size:.85rem; }
    @media (max-width:900px) { .layout { grid-template-columns:1fr; } header { grid-template-columns:1fr; } }
  </style>
</head>
<body>
  <main class="shell">
    <header>
      <div><div class="eyebrow">Offline · pass one · owner-authored</div><h1>BibleBench judge interface</h1><div class="muted">One frozen episode at a time. No server, network, suggested judgment, prior decision, or repeat membership.</div></div>
      <div><span id="draft-status" class="status">DRAFT_INCOMPLETE</span><div id="storage-status" class="storage-status" role="status" aria-live="polite">Autosave available in this browser.</div><div id="packet-hash" class="hash"></div></div>
    </header>
    <section class="toolbar" aria-label="Filters and draft controls">
      <div class="control"><label for="module-filter">Module filter</label><select id="module-filter"><option value="all">All modules</option><option value="fruitbench">FruitBench</option><option value="corinthlove">CORINTHLOVE</option><option value="tencommandments">10CBench</option><option value="sermonmount">SermonMount</option></select></div>
      <div class="control"><label for="role-filter">Role filter</label><select id="role-filter"><option value="all">All roles</option><option value="target">Target</option><option value="null">Null</option><option value="restraint">Restraint</option></select></div>
      <div class="control"><label for="record-index">Record index</label><input id="record-index" type="number" min="1" max="48" value="1" inputmode="numeric"></div>
      <div class="spacer"></div>
      <button id="import-draft" type="button">Import JSON</button><input id="import-file" class="hidden" type="file" accept="application/json,.json">
      <button id="export-draft" type="button">Export JSON</button>
    </section>
    <section class="navrow" aria-label="Record navigation">
      <button id="previous-record" type="button">← Previous</button><button id="next-record" type="button">Next →</button>
      <strong id="record-position"></strong><div class="spacer"></div><span id="progress"></span><div class="progressbar" aria-hidden="true"><span id="progress-fill"></span></div>
    </section>
    <div class="layout">
      <article class="panel"><div class="panel-head"><div id="record-meta" class="eyebrow"></div><h2 id="record-title"></h2></div><div class="panel-body"><div id="rubric" class="rubric"></div><div id="source-content"></div></div></article>
      <aside class="panel"><div class="panel-head"><div class="eyebrow">Owner draft · all fields pending initially</div><h2>Pass-one entries</h2></div><div class="panel-body">
        <div class="field"><label for="behavior-decision">Behavior decision</label><select id="behavior-decision"><option value="">Pending</option><option>APPROVE</option><option>REVISE</option><option>REJECT</option><option>DEFER</option><option>NOT_APPLICABLE</option></select></div>
        <div class="field"><label for="behavior-rationale">Behavior rationale</label><textarea id="behavior-rationale" placeholder="Pending"></textarea></div>
        <div class="field"><label for="interpretive-decision">Interpretive decision</label><select id="interpretive-decision"><option value="">Pending</option><option>APPROVE</option><option>REVISE</option><option>REJECT</option><option>DEFER</option><option>NOT_APPLICABLE</option></select></div>
        <div class="field"><label for="interpretive-rationale">Interpretive rationale</label><textarea id="interpretive-rationale" placeholder="Pending"></textarea></div>
        <div class="field"><label>Derived record decision</label><output id="record-decision" class="derived">Pending</output><small>Computed only after both owner track entries; deterministic finalizer roll-up.</small></div>
        <div class="field"><label for="confidence">Owner confidence</label><select id="confidence"><option value="">Pending</option><option value="low">low</option><option value="medium">medium</option><option value="high">high</option></select></div>
        <div class="field"><label for="contestability">Owner contestability</label><select id="contestability"><option value="">Pending</option><option value="clear">clear</option><option value="contested">contested</option><option value="outside_competence">outside_competence</option></select></div>
        <div class="field"><label for="issues">Owner issues (JSON array)</label><textarea id="issues" placeholder="Pending. Enter [] only after explicitly finding no issue entries."></textarea><small>Each object: issue_id, priority, track, summary, affected_fields, repair_condition.</small></div>
        <div class="field"><label for="judge-id">Stable judge ID</label><input id="judge-id" placeholder="Pending" autocomplete="off"></div>
        <div class="field"><label for="reviewed-at">Reviewed at (UTC)</label><input id="reviewed-at" placeholder="YYYY-MM-DDTHH:MM:SSZ" autocomplete="off"></div>
        <div class="field"><label for="notes">Optional notes</label><textarea id="notes" placeholder="Pending / optional"></textarea></div>
        <div class="field"><label>Mechanical validation</label><ul id="warnings" class="warnings"></ul></div>
      </div></aside>
    </div>
    <p class="footer-note">When browser storage is available, autosave remains under the exact source packet hash. If storage is unavailable, the visible in-memory draft can still be exported. Exported JSON is a draft only; this page cannot write authoritative YAML or finalize gold. Keyboard: ←/→ or k/j outside editing fields.</p>
  </main>
  <script id="judge-source" type="application/json">__SOURCE_JSON__</script>
  <script id="judge-draft-template" type="application/json">__DRAFT_JSON__</script>
  <script>
  "use strict";
  const SOURCE = JSON.parse(document.getElementById("judge-source").textContent);
  const TEMPLATE = JSON.parse(document.getElementById("judge-draft-template").textContent);
  const STORAGE_KEY = "biblebench-pass-one:" + SOURCE.source_packet_sha256;
  const TRACK = new Set(["APPROVE","REVISE","REJECT","DEFER","NOT_APPLICABLE"]);
  const QUALITY = new Set(["APPROVE","REVISE","REJECT","DEFER"]);
  const RECORD_KEYS = ["episode_id","status","owner_behavior_decision","owner_interpretive_decision","owner_record_decision","owner_behavior_rationale","owner_interpretive_rationale","owner_confidence","owner_contestability","owner_issues","owner_issues_editor","owner_judge_id","owner_notes","owner_reviewed_at"];
  const ISSUE_KEYS = ["issue_id","priority","track","summary","affected_fields","repair_condition"];
  const byId = new Map(SOURCE.records.map((row) => [row.episode_id,row]));
  let currentIndex = 0;
  const $ = (id) => document.getElementById(id);
  let storageAvailable = true;
  let draft = restoreDraft();
  const fields = {
    behaviorDecision: $("behavior-decision"), behaviorRationale: $("behavior-rationale"),
    interpretiveDecision: $("interpretive-decision"), interpretiveRationale: $("interpretive-rationale"),
    confidence: $("confidence"), contestability: $("contestability"), issues: $("issues"),
    judgeId: $("judge-id"), reviewedAt: $("reviewed-at"), notes: $("notes")
  };

  function clone(value) { return JSON.parse(JSON.stringify(value)); }
  function textOrNull(value) { const trimmed=value.trim(); return trimmed ? trimmed : null; }
  function isUtcTimestamp(value) { if(typeof value!=="string"||!/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/.test(value))return false; const parts=value.match(/\d+/g).map(Number),[year,month,day,hour,minute,second]=parts; const date=new Date(Date.UTC(year,month-1,day,hour,minute,second)); return date.getUTCFullYear()===year&&date.getUTCMonth()===month-1&&date.getUTCDate()===day&&date.getUTCHours()===hour&&date.getUTCMinutes()===minute&&date.getUTCSeconds()===second; }
  function rollup(behavior,interpretive) { const values=[behavior,interpretive].filter((v)=>v!=="NOT_APPLICABLE"); if(!values.length)return "DEFER"; for(const value of ["DEFER","REJECT","REVISE","APPROVE"])if(values.includes(value))return value; return null; }
  function sameKeys(value,expected) { return value && typeof value==="object" && !Array.isArray(value) && Object.keys(value).sort().join("|")===expected.slice().sort().join("|"); }
  function validText(value) { return typeof value==="string" && value.length>=8 && value.length<=8000; }
  function recordWarnings(record,source) {
    const out=[]; const id=source.episode_id; const b=record.owner_behavior_decision; const i=record.owner_interpretive_decision; const r=record.owner_record_decision;
    const bApplicable=source.behavioral_attribution==="applicable"; const iApplicable=source.stratum==="christian_facing";
    if(b===null)out.push(`${id}: owner_behavior_decision is missing.`); else if(!TRACK.has(b))out.push(`${id}: owner_behavior_decision contains an invalid value.`); else if((bApplicable&&!QUALITY.has(b))||(!bApplicable&&b!=="NOT_APPLICABLE"))out.push(`${id}: owner_behavior_decision conflicts with registered routing.`);
    if(i===null)out.push(`${id}: owner_interpretive_decision is missing.`); else if(!TRACK.has(i))out.push(`${id}: owner_interpretive_decision contains an invalid value.`); else if((iApplicable&&!QUALITY.has(i))||(!iApplicable&&i!=="NOT_APPLICABLE"))out.push(`${id}: owner_interpretive_decision conflicts with registered routing.`);
    if(TRACK.has(b)&&TRACK.has(i)&&r!==rollup(b,i))out.push(`${id}: owner_record_decision conflicts with deterministic roll-up.`);
    for(const key of ["owner_behavior_rationale","owner_interpretive_rationale"])if(!validText(record[key]))out.push(`${id}: ${key} is ${record[key]===null?"missing":"invalid"}.`);
    if(!["low","medium","high"].includes(record.owner_confidence))out.push(`${id}: owner_confidence is ${record.owner_confidence===null?"missing":"invalid"}.`);
    if(!["clear","contested","outside_competence"].includes(record.owner_contestability))out.push(`${id}: owner_contestability is ${record.owner_contestability===null?"missing":"invalid"}.`);
    if(typeof record.owner_judge_id!=="string"||!/^[a-z][a-z0-9_-]{2,63}$/.test(record.owner_judge_id))out.push(`${id}: owner_judge_id is ${record.owner_judge_id===null?"missing":"invalid"}.`);
    if(!isUtcTimestamp(record.owner_reviewed_at))out.push(`${id}: owner_reviewed_at is ${record.owner_reviewed_at===null?"missing":"invalid"}.`);
    if(record.owner_notes!==null&&!validText(record.owner_notes))out.push(`${id}: owner_notes contains an invalid value.`);
    if(typeof record.owner_issues_editor!=="string"||record.owner_issues_editor.length>262144)out.push(`${id}: owner_issues_editor contains an invalid value.`); else if(record.owner_issues_editor.trim()){try{if(JSON.stringify(JSON.parse(record.owner_issues_editor))!==JSON.stringify(record.owner_issues))out.push(`${id}: owner_issues conflicts with owner_issues_editor.`);}catch(error){out.push(`${id}: owner_issues_editor contains invalid JSON.`);}}
    if(record.owner_issues===null)out.push(`${id}: owner_issues is missing.`); else if(!Array.isArray(record.owner_issues))out.push(`${id}: owner_issues contains an invalid value.`); else {
      if(record.owner_issues.length>32)out.push(`${id}: owner_issues exceeds the registered bound.`);
      const ids=[]; let conflict=false;
      for(const issue of record.owner_issues){
        if(!sameKeys(issue,ISSUE_KEYS)){out.push(`${id}: owner_issues contains an invalid entry shape.`);continue;}
        if(typeof issue.issue_id!=="string"||!/^[A-Z0-9][A-Z0-9_-]{2,63}$/.test(issue.issue_id))out.push(`${id}: owner_issues contains an invalid issue_id.`); else ids.push(issue.issue_id);
        if(!["P0","P1","P2","P3"].includes(issue.priority))out.push(`${id}: owner_issues contains an invalid priority.`);
        if(!["behavior","interpretive","record","custody"].includes(issue.track))out.push(`${id}: owner_issues contains an invalid track.`);
        if(!validText(issue.summary))out.push(`${id}: owner_issues contains an invalid summary.`); if(!validText(issue.repair_condition))out.push(`${id}: owner_issues contains an invalid repair_condition.`);
        if(!Array.isArray(issue.affected_fields)||!issue.affected_fields.length||issue.affected_fields.length>32||new Set(issue.affected_fields).size!==issue.affected_fields.length||issue.affected_fields.some((value)=>typeof value!=="string"||value.length<2||value.length>512))out.push(`${id}: owner_issues contains invalid affected_fields.`);
        const affected=["behavior","interpretive"].includes(issue.track)?record[`owner_${issue.track}_decision`]:r;
        if((issue.priority==="P0"&&affected!=="DEFER")||(issue.priority==="P1"&&!['REVISE','DEFER'].includes(affected)))conflict=true;
      }
      if(new Set(ids).size!==ids.length)out.push(`${id}: owner_issues contains duplicate issue IDs.`);
      const priorities=new Set(record.owner_issues.map((issue)=>issue.priority)); if((priorities.has("P0")&&r!=="DEFER")||(priorities.has("P1")&&r==="APPROVE"))conflict=true;
      if(conflict)out.push(`${id}: owner_issues contains a priority/decision contradiction.`);
    }
    if(record.owner_confidence==="low"&&!['REVISE','DEFER'].includes(r))out.push(`${id}: owner_confidence conflicts with owner_record_decision.`);
    if(record.owner_contestability==="outside_competence"&&r!=="DEFER")out.push(`${id}: owner_contestability conflicts with owner_record_decision.`);
    return [...new Set(out)];
  }
  function normaliseDraft(value) {
    const next=clone(value); const importedById=new Map(next.records.map((row)=>[row.episode_id,row]));
    if(importedById.size===SOURCE.records.length&&SOURCE.records.every((sourceRow)=>importedById.has(sourceRow.episode_id)))next.records=SOURCE.records.map((sourceRow)=>importedById.get(sourceRow.episode_id));
    for(const record of next.records){ const source=byId.get(record.episode_id); if(!source)continue; if(typeof record.owner_issues_editor==="string"&&record.owner_issues_editor.trim()){try{record.owner_issues=JSON.parse(record.owner_issues_editor);}catch(error){record.owner_issues=null;}}else if(typeof record.owner_issues_editor==="string"){record.owner_issues=null;} const b=record.owner_behavior_decision,i=record.owner_interpretive_decision; record.owner_record_decision=TRACK.has(b)&&TRACK.has(i)?rollup(b,i):null; record.status=recordWarnings(record,source).length?"DRAFT_INCOMPLETE":"DRAFT_COMPLETE"; }
    next.status=next.records.length===48&&next.records.every((r)=>r.status==="DRAFT_COMPLETE")?"DRAFT_COMPLETE":"DRAFT_INCOMPLETE"; return next;
  }
  function validateClosed(value) {
    if(!sameKeys(value,["draft_version","status","source_packet_sha256","records"]))throw new Error("Closed draft shape mismatch.");
    if(value.draft_version!==TEMPLATE.draft_version||value.source_packet_sha256!==SOURCE.source_packet_sha256||!Array.isArray(value.records)||value.records.length!==48)throw new Error("Draft binding mismatch.");
    if(!["DRAFT_INCOMPLETE","DRAFT_COMPLETE"].includes(value.status))throw new Error("Draft status value is invalid.");
    const ids=value.records.map((row)=>row.episode_id); if(new Set(ids).size!==48||ids.some((id)=>!byId.has(id)))throw new Error("Draft records do not exactly cover this packet.");
    for(const row of value.records){
      if(!sameKeys(row,RECORD_KEYS))throw new Error("Closed record shape mismatch.");
      if(!["DRAFT_INCOMPLETE","DRAFT_COMPLETE"].includes(row.status))throw new Error("Record status value is invalid.");
      if(row.owner_behavior_decision!==null&&!TRACK.has(row.owner_behavior_decision))throw new Error("Behavior decision value is invalid.");
      if(row.owner_interpretive_decision!==null&&!TRACK.has(row.owner_interpretive_decision))throw new Error("Interpretive decision value is invalid.");
      if(row.owner_record_decision!==null&&!QUALITY.has(row.owner_record_decision))throw new Error("Record decision value is invalid.");
      for(const key of ["owner_behavior_rationale","owner_interpretive_rationale","owner_notes"]){const entry=row[key];if(entry!==null&&(typeof entry!=="string"||entry.length>8000))throw new Error("Draft text value is invalid.");}
      if(row.owner_confidence!==null&&!["low","medium","high"].includes(row.owner_confidence))throw new Error("Confidence value is invalid.");
      if(row.owner_contestability!==null&&!["clear","contested","outside_competence"].includes(row.owner_contestability))throw new Error("Contestability value is invalid.");
      if(row.owner_judge_id!==null&&(typeof row.owner_judge_id!=="string"||row.owner_judge_id.length>64))throw new Error("Judge ID value is invalid.");
      if(row.owner_reviewed_at!==null&&!isUtcTimestamp(row.owner_reviewed_at))throw new Error("Review time value is invalid.");
      if(typeof row.owner_issues_editor!=="string"||row.owner_issues_editor.length>262144)throw new Error("Issue editor value is invalid.");
      if(row.owner_issues!==null){
        if(!Array.isArray(row.owner_issues)||row.owner_issues.length>32||row.owner_issues.some((issue)=>!sameKeys(issue,ISSUE_KEYS)))throw new Error("Closed issue shape mismatch.");
        for(const issue of row.owner_issues){
          if(typeof issue.issue_id!=="string"||issue.issue_id.length>64)throw new Error("Issue ID value is invalid.");
          if(issue.priority!==null&&!["P0","P1","P2","P3"].includes(issue.priority))throw new Error("Issue priority value is invalid.");
          if(issue.track!==null&&!["behavior","interpretive","record","custody"].includes(issue.track))throw new Error("Issue track value is invalid.");
          if(typeof issue.summary!=="string"||issue.summary.length>8000||typeof issue.repair_condition!=="string"||issue.repair_condition.length>8000)throw new Error("Issue text value is invalid.");
          if(!Array.isArray(issue.affected_fields)||issue.affected_fields.length>32||new Set(issue.affected_fields).size!==issue.affected_fields.length||issue.affected_fields.some((entry)=>typeof entry!=="string"||entry.length>512))throw new Error("Issue affected_fields value is invalid.");
        }
      }
    }
    return normaliseDraft(value);
  }
  function markStorageUnavailable(error) { storageAvailable=false; const status=$("storage-status"); status.textContent="Storage unavailable; using in-memory draft only."; status.className="storage-status unavailable"; status.title=error&&error.name?error.name:"StorageError"; }
  function readStoredDraft() { try{return localStorage.getItem(STORAGE_KEY);}catch(error){markStorageUnavailable(error);return null;} }
  function restoreDraft() { const saved=readStoredDraft(); if(!saved)return clone(TEMPLATE); try{return validateClosed(JSON.parse(saved));}catch(error){return clone(TEMPLATE);} }
  function persist() { if(!storageAvailable)return false; try{localStorage.setItem(STORAGE_KEY,JSON.stringify(draft));return true;}catch(error){markStorageUnavailable(error);return false;} }
  function visibleIndices() { const module=$("module-filter").value,role=$("role-filter").value; return SOURCE.records.map((row,index)=>({row,index})).filter(({row})=>(module==="all"||row.module===module)&&(role==="all"||row.role===role)).map(({index})=>index); }
  function sourceSection(title,value,open=false) { const details=document.createElement("details"); details.open=open; const summary=document.createElement("summary"); summary.textContent=title; const body=document.createElement("div"); body.className="source-value"; body.textContent=typeof value==="string"?value:JSON.stringify(value,null,2); details.append(summary,body); return details; }
  function renderSource(source) { $("record-meta").textContent=`${source.module} · ${source.role} · ${source.stratum} · ${source.mode}`; $("record-title").textContent=`${source.episode_id} · ${source.core_id}`; $("rubric").textContent=SOURCE.rubric.scope+" "+SOURCE.rubric.evidence_boundary; const content=$("source-content"); content.replaceChildren(); const sections=[["Scenario",source.scenario,true],["Identity and custody",{authored_episode_sha256:source.authored_episode_sha256,review_payload_sha256:source.review_payload_sha256,passage_anchors:source.passage_anchors,source_artifacts:source.source_artifacts},true],["Task and answer semantics",{task_semantics:source.task_semantics,answer_semantics:source.answer_semantics,tool_schema:source.tool_schema,response_schema:source.response_schema},false],["Authority and affected parties",{affected_parties:source.affected_parties,authority_boundary:source.authority_boundary},true],["Two-sided observable geometry",{acceptable_action_band:source.acceptable_action_band,prohibited_actions:source.prohibited_actions,deficient_pole:source.deficient_pole,counterfeit_pole:source.counterfeit_pole,red_line_classes:source.red_line_classes},true],["Capability twin, execution, and probe",{capability_twin:source.capability_twin,execution_contract:source.execution_contract,probe_payload:source.probe_payload},false],["Repair expectations",source.repair_expectations,false],["Behavioral attribution input",source.behavioral_attribution,false]]; for(const section of sections)content.append(sourceSection(...section)); }
  function renderEditor(record) { fields.behaviorDecision.value=record.owner_behavior_decision||""; fields.behaviorRationale.value=record.owner_behavior_rationale||""; fields.interpretiveDecision.value=record.owner_interpretive_decision||""; fields.interpretiveRationale.value=record.owner_interpretive_rationale||""; fields.confidence.value=record.owner_confidence||""; fields.contestability.value=record.owner_contestability||""; fields.issues.value=record.owner_issues_editor; fields.judgeId.value=record.owner_judge_id||""; fields.reviewedAt.value=record.owner_reviewed_at||""; fields.notes.value=record.owner_notes||""; updateVisibleState(); }
  function currentRecord(){return draft.records[currentIndex];}
  function updateVisibleState(extraWarning=null) { const record=currentRecord(),source=SOURCE.records[currentIndex]; $("record-decision").textContent=record.owner_record_decision||"Pending"; const warnings=recordWarnings(record,source); if(extraWarning)warnings.unshift(extraWarning); const list=$("warnings"); list.replaceChildren(); if(warnings.length){list.className="warnings"; for(const warning of warnings){const item=document.createElement("li");item.textContent=warning;list.append(item);}}else{list.className="warnings ok";const item=document.createElement("li");item.textContent="No mechanical warning for this record.";list.append(item);} const complete=draft.records.filter((row)=>row.status==="DRAFT_COMPLETE").length; $("progress").textContent=`${complete} / 48 complete`; $("progress-fill").style.width=`${complete/48*100}%`; $("draft-status").textContent=draft.status; $("draft-status").className=draft.status==="DRAFT_COMPLETE"?"status complete":"status"; }
  function updateRecord(mutator,extraWarning=null){mutator(currentRecord()); draft=normaliseDraft(draft); persist(); updateVisibleState(extraWarning);}
  function renderRecord(index) { currentIndex=Math.max(0,Math.min(47,index)); const source=SOURCE.records[currentIndex],record=currentRecord(); renderSource(source); renderEditor(record); const visible=visibleIndices(),position=visible.indexOf(currentIndex); $("record-position").textContent=position>=0?`Filtered ${position+1} / ${visible.length} · overall ${currentIndex+1} / 48`:`Overall ${currentIndex+1} / 48 · hidden by filter`; $("record-index").value=String(currentIndex+1); $("previous-record").disabled=!visible.length||position<=0; $("next-record").disabled=!visible.length||position<0||position>=visible.length-1; }
  function navigate(delta){const visible=visibleIndices();if(!visible.length)return;let position=visible.indexOf(currentIndex);if(position<0)position=delta>0?-1:visible.length;position=Math.max(0,Math.min(visible.length-1,position+delta));renderRecord(visible[position]);}
  fields.behaviorDecision.addEventListener("change",()=>updateRecord((r)=>{r.owner_behavior_decision=fields.behaviorDecision.value||null;}));
  fields.interpretiveDecision.addEventListener("change",()=>updateRecord((r)=>{r.owner_interpretive_decision=fields.interpretiveDecision.value||null;}));
  fields.behaviorRationale.addEventListener("input",()=>updateRecord((r)=>{r.owner_behavior_rationale=textOrNull(fields.behaviorRationale.value);}));
  fields.interpretiveRationale.addEventListener("input",()=>updateRecord((r)=>{r.owner_interpretive_rationale=textOrNull(fields.interpretiveRationale.value);}));
  fields.confidence.addEventListener("change",()=>updateRecord((r)=>{r.owner_confidence=fields.confidence.value||null;}));
  fields.contestability.addEventListener("change",()=>updateRecord((r)=>{r.owner_contestability=fields.contestability.value||null;}));
  fields.judgeId.addEventListener("input",()=>updateRecord((r)=>{r.owner_judge_id=textOrNull(fields.judgeId.value);}));
  fields.reviewedAt.addEventListener("input",()=>updateRecord((r)=>{r.owner_reviewed_at=textOrNull(fields.reviewedAt.value);}));
  fields.notes.addEventListener("input",()=>updateRecord((r)=>{r.owner_notes=textOrNull(fields.notes.value);}));
  fields.issues.addEventListener("input",()=>updateRecord((r)=>{r.owner_issues_editor=fields.issues.value;}));
  $("previous-record").addEventListener("click",()=>navigate(-1)); $("next-record").addEventListener("click",()=>navigate(1));
  $("module-filter").addEventListener("change",()=>{const visible=visibleIndices();if(visible.length)renderRecord(visible[0]);else renderRecord(currentIndex);}); $("role-filter").addEventListener("change",()=>{const visible=visibleIndices();if(visible.length)renderRecord(visible[0]);else renderRecord(currentIndex);});
  $("record-index").addEventListener("change",()=>renderRecord(Number($("record-index").value)-1));
  document.addEventListener("keydown",(event)=>{const tag=document.activeElement&&document.activeElement.tagName;if(["INPUT","TEXTAREA","SELECT"].includes(tag))return;if(event.key === "ArrowLeft"||event.key==="k"){event.preventDefault();navigate(-1);}if(event.key === "ArrowRight"||event.key==="j"){event.preventDefault();navigate(1);}});
  $("export-draft").addEventListener("click",()=>{draft=normaliseDraft(draft);persist();const blob=new Blob([JSON.stringify(draft,null,2)+"\n"],{type:"application/json;charset=utf-8"});const anchor=document.createElement("a");anchor.href=URL.createObjectURL(blob);anchor.download=`biblebench-pass-one-draft-${SOURCE.source_packet_sha256.slice(0,12)}.json`;anchor.click();URL.revokeObjectURL(anchor.href);});
  $("import-draft").addEventListener("click",()=>$("import-file").click());
  $("import-file").addEventListener("change",()=>{const file=$("import-file").files[0];if(!file)return;const reader=new FileReader();reader.onload=()=>{try{draft=validateClosed(JSON.parse(String(reader.result)));persist();renderRecord(0);}catch(error){window.alert("Import rejected: "+error.message);}finally{$("import-file").value="";}};reader.readAsText(file,"utf-8");});
  $("packet-hash").textContent="Source SHA-256: "+SOURCE.source_packet_sha256;
  renderRecord(0);
  </script>
</body>
</html>
'''


def build_interface_document(
    package_root: Union[str, Path], packet_path: Union[str, Path, None] = None
) -> str:
    packet, source_hash = load_pending_packet(package_root, packet_path)
    source = build_source_payload(packet, source_hash)
    draft = initial_draft(packet, source_hash)
    return (
        HTML_TEMPLATE.replace("__SOURCE_JSON__", _json_for_html(source))
        .replace("__DRAFT_JSON__", _json_for_html(draft))
        .rstrip()
        + "\n"
    )


def write_judge_interface(
    package_root: Union[str, Path],
    *,
    output_path: Union[str, Path, None] = None,
    packet_path: Union[str, Path, None] = None,
) -> Path:
    root = Path(package_root).resolve()
    destination = (
        Path(output_path).resolve()
        if output_path is not None
        else root / "adjudication" / "judge-interface.html"
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        build_interface_document(root, packet_path), encoding="utf-8", newline="\n"
    )
    return destination


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build the deterministic offline BibleBench pass-one judge interface."
    )
    parser.add_argument("--package-root", default=str(_package_root()))
    parser.add_argument("--packet")
    parser.add_argument("--output")
    parser.add_argument(
        "--draft-json",
        help="Custodian-only exported judge draft to validate and merge.",
    )
    parser.add_argument(
        "--reviewed-packet-output",
        help="Exclusive-create reviewed-packet input for the existing finalizer.",
    )
    return parser


def main(argv: Union[list[str], None] = None) -> int:
    arguments = _parser().parse_args(argv)
    try:
        bridge_requested = bool(
            arguments.draft_json or arguments.reviewed_packet_output
        )
        if bridge_requested:
            if not arguments.draft_json or not arguments.reviewed_packet_output:
                raise ValueError(
                    "custodian bridge requires --draft-json and "
                    "--reviewed-packet-output together"
                )
            if arguments.output:
                raise ValueError("custodian bridge does not accept --output")
            path = bridge_draft_to_reviewed_packet(
                arguments.package_root,
                draft_path=arguments.draft_json,
                output_path=arguments.reviewed_packet_output,
                packet_path=arguments.packet,
            )
        else:
            path = write_judge_interface(
                arguments.package_root,
                output_path=arguments.output,
                packet_path=arguments.packet,
            )
    except (OSError, ValueError, yaml.YAMLError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
