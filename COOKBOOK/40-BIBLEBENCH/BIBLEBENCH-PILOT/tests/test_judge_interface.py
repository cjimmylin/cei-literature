from __future__ import annotations

from copy import deepcopy
import hashlib
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re

from jsonschema import Draft202012Validator
import pytest
import yaml


PACKAGE_ROOT = Path(__file__).parents[1]
PACKET_PATH = PACKAGE_ROOT / "adjudication" / "provisional-gold-review.yaml"
SCHEMA_PATH = PACKAGE_ROOT / "schemas" / "judge-draft.schema.json"


class _EmbeddedJsonParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.current_id: str | None = None
        self.values: dict[str, str] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "script" and attributes.get("type") == "application/json":
            self.current_id = attributes.get("id")
            if self.current_id:
                self.values[self.current_id] = ""

    def handle_data(self, data: str) -> None:
        if self.current_id:
            self.values[self.current_id] += data

    def handle_endtag(self, tag: str) -> None:
        if tag == "script":
            self.current_id = None


def _module():
    import biblebench_pilot.judge_ui as judge_ui

    return judge_ui


def _embedded_json(html: str, element_id: str) -> dict:
    parser = _EmbeddedJsonParser()
    parser.feed(html)
    return json.loads(parser.values[element_id])


def _complete_draft(draft: dict, source: dict) -> dict:
    by_id = {record["episode_id"]: record for record in source["records"]}
    completed = deepcopy(draft)
    for record in completed["records"]:
        source_record = by_id[record["episode_id"]]
        behavior_applicable = (
            source_record["behavioral_attribution"] == "applicable"
        )
        interpretive_applicable = source_record["stratum"] == "christian_facing"
        record.update(
            {
                "owner_behavior_decision": (
                    "APPROVE" if behavior_applicable else "NOT_APPLICABLE"
                ),
                "owner_interpretive_decision": (
                    "APPROVE" if interpretive_applicable else "NOT_APPLICABLE"
                ),
                "owner_behavior_rationale": (
                    "The behavior-track judgment is recorded for this test fixture."
                ),
                "owner_interpretive_rationale": (
                    "The interpretation-track judgment is recorded for this test fixture."
                ),
                "owner_confidence": "high",
                "owner_contestability": "clear",
                "owner_issues": [],
                "owner_issues_editor": "[]",
                "owner_judge_id": "jimmy_lin",
                "owner_notes": None,
                "owner_reviewed_at": "2026-07-13T17:00:00Z",
            }
        )
    return _module().normalize_draft(completed, source)


def test_loads_frozen_pending_packet_and_binds_exact_source_hash() -> None:
    judge_ui = _module()

    packet, source_hash = judge_ui.load_pending_packet(PACKAGE_ROOT)

    assert len(packet["records"]) == 48
    assert len({record["episode_id"] for record in packet["records"]}) == 48
    assert source_hash == hashlib.sha256(PACKET_PATH.read_bytes()).hexdigest()


def test_refuses_packet_with_any_precompleted_owner_field(tmp_path: Path) -> None:
    judge_ui = _module()
    packet = yaml.safe_load(PACKET_PATH.read_text(encoding="utf-8"))
    packet["records"][0]["owner_review_status"] = "reviewed"
    packet["records"][0]["owner_behavior_decision"] = "APPROVE"
    path = tmp_path / "precompleted.yaml"
    path.write_text(yaml.safe_dump(packet, sort_keys=False), encoding="utf-8")

    with pytest.raises(ValueError, match="precompleted owner"):
        judge_ui.load_pending_packet(PACKAGE_ROOT, path)


def test_closed_draft_schema_contains_only_binding_and_owner_fields() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    assert schema["additionalProperties"] is False
    assert set(schema["properties"]) == {
        "draft_version",
        "status",
        "source_packet_sha256",
        "records",
    }
    record = schema["$defs"]["draftRecord"]
    assert record["additionalProperties"] is False
    assert set(record["properties"]) == {
        "episode_id",
        "status",
        "owner_behavior_decision",
        "owner_interpretive_decision",
        "owner_record_decision",
        "owner_behavior_rationale",
        "owner_interpretive_rationale",
        "owner_confidence",
        "owner_contestability",
        "owner_issues",
        "owner_issues_editor",
        "owner_judge_id",
        "owner_notes",
        "owner_reviewed_at",
    }
    assert schema["$defs"]["ownerIssue"]["additionalProperties"] is False
    completed_timestamp = schema["$defs"]["draftRecord"]["allOf"][0]["then"][
        "properties"
    ]["owner_reviewed_at"]
    assert completed_timestamp["format"] == "date-time"


def test_initial_draft_has_48_unique_visibly_pending_records() -> None:
    judge_ui = _module()
    packet, source_hash = judge_ui.load_pending_packet(PACKAGE_ROOT)
    draft = judge_ui.initial_draft(packet, source_hash)
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

    Draft202012Validator(schema).validate(draft)
    assert draft["status"] == "DRAFT_INCOMPLETE"
    assert draft["source_packet_sha256"] == source_hash
    assert len(draft["records"]) == 48
    assert len({record["episode_id"] for record in draft["records"]}) == 48
    for record in draft["records"]:
        assert record["status"] == "DRAFT_INCOMPLETE"
        for key, value in record.items():
            if key == "owner_issues_editor":
                assert value == ""
            elif key not in {"episode_id", "status"}:
                assert value is None


def test_closed_schema_preserves_partial_owner_text_as_an_incomplete_draft() -> None:
    judge_ui = _module()
    packet, source_hash = judge_ui.load_pending_packet(PACKAGE_ROOT)
    source = judge_ui.build_source_payload(packet, source_hash)
    draft = judge_ui.initial_draft(packet, source_hash)
    draft["records"][0]["owner_behavior_rationale"] = "partial"
    normalized = judge_ui.normalize_draft(draft, source)
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

    Draft202012Validator(schema).validate(normalized)
    assert normalized["records"][0]["status"] == "DRAFT_INCOMPLETE"


def test_interface_build_is_deterministic_and_embeds_only_blinded_source_fields(
    tmp_path: Path,
) -> None:
    judge_ui = _module()
    first = tmp_path / "first.html"
    second = tmp_path / "second.html"

    judge_ui.write_judge_interface(PACKAGE_ROOT, output_path=first)
    judge_ui.write_judge_interface(PACKAGE_ROOT, output_path=second)

    first_bytes = first.read_bytes()
    assert first_bytes == second.read_bytes()
    html = first_bytes.decode("utf-8")
    source = _embedded_json(html, "judge-source")
    draft = _embedded_json(html, "judge-draft-template")
    assert len(source["records"]) == 48
    assert len({row["episode_id"] for row in source["records"]}) == 48
    assert source["source_packet_sha256"] == draft["source_packet_sha256"]

    forbidden_keys = {
        "owner_review_status",
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
        "track_applicability",
        "judge_confidence",
        "contestability",
        "cue_surfaces",
        "forecast_payload",
        "decoding",
        "blinded_repeat_procedure",
        "repeat_membership",
        "model",
        "provider",
        "actor",
        "run_order",
        "analysis",
    }

    def keys(value: object) -> set[str]:
        if isinstance(value, dict):
            return set(value) | set().union(*(keys(v) for v in value.values()))
        if isinstance(value, list):
            return set().union(*(keys(v) for v in value)) if value else set()
        return set()

    assert forbidden_keys.isdisjoint(keys(source))


def test_html_is_self_contained_network_closed_and_has_required_workflow() -> None:
    judge_ui = _module()
    html = judge_ui.build_interface_document(PACKAGE_ROOT)
    folded = html.casefold()

    csp = (
        "default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; "
        "img-src data:; connect-src 'none'; form-action 'none'; "
        "frame-ancestors 'none'; base-uri 'none'"
    )
    assert csp in html
    assert "http://" not in folded and "https://" not in folded
    assert not re.search(r"<(?:script|link)\b[^>]+\bsrc=", html, re.I)
    assert "<form" not in folded
    for forbidden in (
        "fetch(",
        "xmlhttprequest",
        "websocket",
        "eventsource",
        "sendbeacon",
        "analytics",
    ):
        assert forbidden not in folded
    for required in (
        'id="module-filter"',
        'id="role-filter"',
        'id="record-index"',
        'id="previous-record"',
        'id="next-record"',
        'id="progress"',
        'id="import-draft"',
        'id="export-draft"',
        "localStorage.getItem(STORAGE_KEY)",
        "localStorage.setItem(STORAGE_KEY",
        'event.key === "ArrowLeft"',
        'event.key === "ArrowRight"',
    ):
        assert required in html
    assert "biblebench-pass-one:" in html


def test_browser_validator_covers_registered_issue_bounds() -> None:
    judge_ui = _module()
    html = judge_ui.build_interface_document(PACKAGE_ROOT)

    assert "record.owner_issues.length>32" in html
    assert "issue.affected_fields.length>32" in html
    assert "typeof value!==\"string\"||value.length<2||value.length>512" in html


def test_browser_semantically_validates_exact_utc_timestamps() -> None:
    html = _module().build_interface_document(PACKAGE_ROOT)

    assert "function isUtcTimestamp(value)" in html
    assert "Date.UTC(year,month-1,day,hour,minute,second)" in html
    assert "date.getUTCFullYear()===year" in html
    assert "isUtcTimestamp(record.owner_reviewed_at)" in html
    assert "isUtcTimestamp(row.owner_reviewed_at)" in html


def test_browser_storage_failures_degrade_visibly_without_gating_export() -> None:
    html = _module().build_interface_document(PACKAGE_ROOT)

    assert 'id="storage-status"' in html
    assert "function markStorageUnavailable(error)" in html
    assert "Storage unavailable; using in-memory draft only." in html
    assert "try{return localStorage.getItem(STORAGE_KEY);}" in html
    assert "try{localStorage.setItem(STORAGE_KEY,JSON.stringify(draft));return true;}" in html
    assert "catch(error){markStorageUnavailable(error);return false;}" in html
    export_handler = re.search(
        r'\$\("export-draft"\)\.addEventListener\("click",\(\)=>\{(.+?)\}\);',
        html,
    )
    assert export_handler is not None
    body = export_handler.group(1)
    assert "persist();" in body
    assert "new Blob" in body
    assert body.index("persist();") < body.index("new Blob")
    assert "if(!persist())" not in body


def test_safe_json_embedding_cannot_close_script_element() -> None:
    judge_ui = _module()
    embedded = judge_ui._json_for_html({"value": "</script><script>alert(1)</script>"})

    assert "</script" not in embedded.casefold()
    assert "\\u003c" in embedded


def test_json_export_import_is_lossless_after_normalization() -> None:
    judge_ui = _module()
    packet, source_hash = judge_ui.load_pending_packet(PACKAGE_ROOT)
    source = judge_ui.build_source_payload(packet, source_hash)
    draft = judge_ui.initial_draft(packet, source_hash)
    draft["records"][0]["owner_notes"] = "A bounded optional note for round-trip testing."
    normalized = judge_ui.normalize_draft(draft, source)

    exported = judge_ui.serialize_draft(normalized)
    imported = judge_ui.normalize_imported_draft(exported, source)

    assert imported == normalized
    assert judge_ui.serialize_draft(imported) == exported


def test_reversed_import_is_canonicalized_to_source_identity_order() -> None:
    judge_ui = _module()
    packet, source_hash = judge_ui.load_pending_packet(PACKAGE_ROOT)
    source = judge_ui.build_source_payload(packet, source_hash)
    draft = judge_ui.initial_draft(packet, source_hash)
    for record in draft["records"]:
        record["owner_notes"] = (
            f"Owner note bound only to episode {record['episode_id']}."
        )
    draft["records"].reverse()

    imported = judge_ui.normalize_imported_draft(json.dumps(draft), source)

    source_ids = [record["episode_id"] for record in source["records"]]
    assert [record["episode_id"] for record in imported["records"]] == source_ids
    for source_record, draft_record in zip(source["records"], imported["records"]):
        assert source_record["episode_id"] == draft_record["episode_id"]
        assert draft_record["owner_notes"].endswith(
            f"{source_record['episode_id']}."
        )
    warnings = judge_ui.mechanical_warnings(imported, source)
    assert all(
        warning.startswith(tuple(source_ids))
        or warning.startswith("Draft ")
        or warning.startswith("records")
        for warning in warnings
    )
    exported = json.loads(judge_ui.serialize_draft(imported))
    assert [record["episode_id"] for record in exported["records"]] == source_ids


def test_browser_canonicalizes_import_before_pairing_display_and_draft() -> None:
    html = _module().build_interface_document(PACKAGE_ROOT)

    assert "next.records=SOURCE.records.map" in html
    assert "importedById.get(sourceRow.episode_id)" in html
    assert (
        'const record=currentRecord(),source=SOURCE.records[currentIndex]' in html
    )


def _partial_issue_draft(raw: str) -> tuple[object, dict, dict]:
    judge_ui = _module()
    packet, source_hash = judge_ui.load_pending_packet(PACKAGE_ROOT)
    source = judge_ui.build_source_payload(packet, source_hash)
    draft = judge_ui.initial_draft(packet, source_hash)
    draft["records"][0]["owner_issues_editor"] = raw
    return judge_ui, source, judge_ui.normalize_draft(draft, source)


def test_partial_issue_text_survives_record_navigation() -> None:
    raw = '[{"issue_id":"PARTIAL"'
    _, source, draft = _partial_issue_draft(raw)
    first_id = source["records"][0]["episode_id"]

    _ = draft["records"][1]
    returned = next(row for row in draft["records"] if row["episode_id"] == first_id)

    assert returned["owner_issues_editor"] == raw
    assert returned["owner_issues"] is None
    assert returned["status"] == "DRAFT_INCOMPLETE"


def test_partial_issue_text_survives_local_storage_reload_normalization() -> None:
    raw = "  [\n  {\"issue_id\": \"PARTIAL\""
    judge_ui, source, draft = _partial_issue_draft(raw)

    reloaded = judge_ui.normalize_imported_draft(json.dumps(draft), source)

    assert reloaded["records"][0]["owner_issues_editor"] == raw
    assert reloaded["records"][0]["status"] == "DRAFT_INCOMPLETE"


def test_partial_issue_text_is_preserved_exactly_in_export() -> None:
    raw = "{\n  partial issue editor text\t"
    judge_ui, _, draft = _partial_issue_draft(raw)

    exported = judge_ui.serialize_draft(draft)

    assert json.loads(exported)["records"][0]["owner_issues_editor"] == raw


def test_partial_issue_text_survives_explicit_import() -> None:
    raw = "[ { \"issue_id\": \"PARTIAL\", \"priority\": "
    judge_ui, source, draft = _partial_issue_draft(raw)

    imported = judge_ui.normalize_imported_draft(
        judge_ui.serialize_draft(draft), source
    )

    assert imported["records"][0]["owner_issues_editor"] == raw
    assert imported["records"][0]["owner_issues"] is None


def test_browser_persists_raw_issue_editor_on_every_keystroke() -> None:
    html = _module().build_interface_document(PACKAGE_ROOT)

    assert "r.owner_issues_editor=fields.issues.value" in html
    assert "fields.issues.value=record.owner_issues_editor" in html
    assert "persist();" in html


def test_complete_draft_merges_to_packet_accepted_by_existing_validation() -> None:
    judge_ui = _module()
    from biblebench_pilot.adjudication import validate_review_packet

    packet, source_hash = judge_ui.load_pending_packet(PACKAGE_ROOT)
    source = judge_ui.build_source_payload(packet, source_hash)
    draft = _complete_draft(judge_ui.initial_draft(packet, source_hash), source)

    assert draft["status"] == "DRAFT_COMPLETE"
    assert judge_ui.mechanical_warnings(draft, source) == []
    merged = judge_ui.merge_complete_draft(draft, packet, PACKAGE_ROOT)
    validate_review_packet(merged, PACKAGE_ROOT)
    assert all(record["owner_review_status"] == "reviewed" for record in merged["records"])


def test_impossible_calendar_timestamp_remains_incomplete_and_bridge_refuses_it(
    tmp_path: Path,
) -> None:
    judge_ui = _module()
    packet, source_hash = judge_ui.load_pending_packet(PACKAGE_ROOT)
    source = judge_ui.build_source_payload(packet, source_hash)
    draft = _complete_draft(judge_ui.initial_draft(packet, source_hash), source)
    draft["records"][0]["owner_reviewed_at"] = "2026-02-30T17:00:00Z"

    normalized = judge_ui.normalize_draft(draft, source)

    assert normalized["status"] == "DRAFT_INCOMPLETE"
    assert normalized["records"][0]["status"] == "DRAFT_INCOMPLETE"
    assert any(
        "owner_reviewed_at contains an invalid value" in warning
        for warning in judge_ui.mechanical_warnings(normalized, source)
    )

    draft_path = tmp_path / "impossible-date.json"
    output_path = tmp_path / "reviewed.yaml"
    draft_path.write_text(judge_ui.serialize_draft(draft), encoding="utf-8")
    with pytest.raises(
        ValueError, match="closed draft schema|incomplete or contradictory"
    ):
        judge_ui.bridge_draft_to_reviewed_packet(
            PACKAGE_ROOT,
            draft_path=draft_path,
            output_path=output_path,
        )
    assert not output_path.exists()


def test_custodian_bridge_emits_reviewed_input_without_mutating_source(
    tmp_path: Path,
) -> None:
    judge_ui = _module()
    from biblebench_pilot.adjudication import validate_review_packet

    packet, source_hash = judge_ui.load_pending_packet(PACKAGE_ROOT)
    source = judge_ui.build_source_payload(packet, source_hash)
    draft = _complete_draft(judge_ui.initial_draft(packet, source_hash), source)
    draft_path = tmp_path / "owner-draft.json"
    draft_path.write_text(judge_ui.serialize_draft(draft), encoding="utf-8")
    output_path = tmp_path / "custodian-reviewed-input.yaml"
    source_before = PACKET_PATH.read_bytes()

    result = judge_ui.bridge_draft_to_reviewed_packet(
        PACKAGE_ROOT, draft_path=draft_path, output_path=output_path
    )

    assert result == output_path
    reviewed = yaml.safe_load(output_path.read_text(encoding="utf-8"))
    validate_review_packet(reviewed, PACKAGE_ROOT)
    assert reviewed["owner_review_status"] == "pending"
    assert all(
        record["owner_review_status"] == "reviewed"
        for record in reviewed["records"]
    )
    assert PACKET_PATH.read_bytes() == source_before
    assert os.stat(output_path).st_mode & 0o777 == 0o600


def test_custodian_bridge_refuses_incomplete_draft_and_existing_output(
    tmp_path: Path,
) -> None:
    judge_ui = _module()
    packet, source_hash = judge_ui.load_pending_packet(PACKAGE_ROOT)
    incomplete_path = tmp_path / "incomplete.json"
    incomplete_path.write_text(
        judge_ui.serialize_draft(judge_ui.initial_draft(packet, source_hash)),
        encoding="utf-8",
    )
    output_path = tmp_path / "reviewed.yaml"

    with pytest.raises(ValueError, match="incomplete or contradictory"):
        judge_ui.bridge_draft_to_reviewed_packet(
            PACKAGE_ROOT,
            draft_path=incomplete_path,
            output_path=output_path,
        )
    assert not output_path.exists()

    source = judge_ui.build_source_payload(packet, source_hash)
    complete = _complete_draft(judge_ui.initial_draft(packet, source_hash), source)
    complete_path = tmp_path / "complete.json"
    complete_path.write_text(judge_ui.serialize_draft(complete), encoding="utf-8")
    output_path.write_text("custodian-owned\n", encoding="utf-8")
    with pytest.raises(FileExistsError, match="refusing to overwrite"):
        judge_ui.bridge_draft_to_reviewed_packet(
            PACKAGE_ROOT,
            draft_path=complete_path,
            output_path=output_path,
        )
    assert output_path.read_text(encoding="utf-8") == "custodian-owned\n"


def test_cli_bridge_is_custodian_only_and_absent_from_browser(
    tmp_path: Path,
) -> None:
    judge_ui = _module()
    packet, source_hash = judge_ui.load_pending_packet(PACKAGE_ROOT)
    source = judge_ui.build_source_payload(packet, source_hash)
    complete = _complete_draft(judge_ui.initial_draft(packet, source_hash), source)
    draft_path = tmp_path / "complete.json"
    output_path = tmp_path / "reviewed.yaml"
    draft_path.write_text(judge_ui.serialize_draft(complete), encoding="utf-8")

    assert (
        judge_ui.main(
            [
                "--package-root",
                str(PACKAGE_ROOT),
                "--draft-json",
                str(draft_path),
                "--reviewed-packet-output",
                str(output_path),
            ]
        )
        == 0
    )
    assert output_path.is_file()
    html = judge_ui.build_interface_document(PACKAGE_ROOT)
    assert "reviewed-packet-output" not in html
    assert "bridge_draft_to_reviewed_packet" not in html


def test_readme_documents_custodian_bridge_and_finalizer_boundary() -> None:
    readme = (
        PACKAGE_ROOT / "adjudication" / "JUDGE-INTERFACE-README.md"
    ).read_text(encoding="utf-8").casefold()

    assert "custodian-only bridge" in readme
    assert "--draft-json" in readme
    assert "--reviewed-packet-output" in readme
    assert "exclusive-create" in readme
    assert "does not finalize" in readme


def test_draft_state_and_warnings_are_mechanical_and_neutral() -> None:
    judge_ui = _module()
    packet, source_hash = judge_ui.load_pending_packet(PACKAGE_ROOT)
    source = judge_ui.build_source_payload(packet, source_hash)
    draft = _complete_draft(judge_ui.initial_draft(packet, source_hash), source)
    draft["records"][0]["owner_confidence"] = "low"
    normalized = judge_ui.normalize_draft(draft, source)

    warnings = judge_ui.mechanical_warnings(normalized, source)
    message = " ".join(warnings).casefold()
    assert normalized["status"] == "DRAFT_INCOMPLETE"
    assert "owner_confidence" in message
    assert "conflicts" in message
    for advisory in (
        "you should",
        "we recommend",
        "choose approve",
        "choose revise",
        "choose reject",
        "choose defer",
        "set to approve",
        "set to revise",
        "set to reject",
        "set to defer",
    ):
        assert advisory not in message


def test_import_rejects_wrong_hash_duplicate_ids_and_extra_fields() -> None:
    judge_ui = _module()
    packet, source_hash = judge_ui.load_pending_packet(PACKAGE_ROOT)
    source = judge_ui.build_source_payload(packet, source_hash)
    draft = judge_ui.initial_draft(packet, source_hash)

    wrong_hash = deepcopy(draft)
    wrong_hash["source_packet_sha256"] = "0" * 64
    with pytest.raises(ValueError, match="source packet hash mismatch"):
        judge_ui.normalize_imported_draft(json.dumps(wrong_hash), source)

    duplicate = deepcopy(draft)
    duplicate["records"][1]["episode_id"] = duplicate["records"][0]["episode_id"]
    with pytest.raises(ValueError, match="exactly cover"):
        judge_ui.normalize_imported_draft(json.dumps(duplicate), source)

    extra = deepcopy(draft)
    extra["records"][0]["suggested_decision"] = "APPROVE"
    with pytest.raises(ValueError, match="closed draft schema"):
        judge_ui.normalize_imported_draft(json.dumps(extra), source)
