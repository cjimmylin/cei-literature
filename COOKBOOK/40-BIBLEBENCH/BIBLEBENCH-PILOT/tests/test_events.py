from __future__ import annotations

from dataclasses import FrozenInstanceError, replace
import hashlib
import json
from pathlib import Path
import re
import time
import traceback
import unicodedata

import pytest
from jsonschema import Draft202012Validator

import biblebench_pilot.events as events_module
from biblebench_pilot.contracts import SandboxEvent, canonical_json_bytes
from biblebench_pilot.events import reconstruct_segments, segment_response
from biblebench_pilot.events import (
    EvidenceSegment,
    FrozenObservableEvidence,
    ObservableEventRecord,
    SandboxEvidence,
    freeze_observable_evidence,
    observable_evidence_to_json,
    observable_event_to_json,
    observable_events_sha256,
    validate_observable_evidence,
    validate_observable_event_record,
)


REGISTERED_ACTIONS = ("draft_message", "request_review", "send_update")
COMPACT_PRIVATE_ALIASES = (
    "actorsid",
    "actorids",
    "modelsid",
    "modelids",
    "providersid",
    "lensesid",
    "expectedlabels",
    "goldlabels",
    "groundtruthid",
    "modelidentities",
    "canaries",
)


def _event_raw(**overrides):
    row = {
        "task_correctness": "partial",
        "registered_actions": ["draft_message"],
        "registered_omissions": ["request_review"],
        "refusal": False,
        "evasion": False,
        "uncertainty": "expressed",
        "consequence_summaries": ["A draft was retained for review."],
        "evidence_ids": ["S001", "E001"],
    }
    row.update(overrides)
    return row


def _sandbox_event(
    sequence: int = 1,
    *,
    action: str = "draft_message",
    payload=None,
) -> SandboxEvent:
    return SandboxEvent(
        sequence=sequence,
        action=action,
        actor="model",
        target="sandbox",
        payload={"text": "A draft"} if payload is None else payload,
    )


def test_event_module_exports_only_the_frozen_public_boundary() -> None:
    assert events_module.__all__ == (
        "EvidenceSegment",
        "SandboxEvidence",
        "ObservableEventRecord",
        "FrozenObservableEvidence",
        "segment_response",
        "reconstruct_segments",
        "validate_observable_event_record",
        "observable_event_to_json",
        "observable_events_sha256",
        "freeze_observable_evidence",
        "observable_evidence_to_json",
        "validate_observable_evidence",
    )
    assert "forecast" not in events_module.__all__


def test_segments_are_lossless_and_opaque() -> None:
    source = "First sentence.\n\nSecond sentence.".encode("utf-8")

    segments = segment_response(source)

    assert [segment.segment_id for segment in segments] == ["S001", "S002", "S003"]
    assert [segment.content for segment in segments] == [
        b"First sentence.",
        b"\n\n",
        b"Second sentence.",
    ]
    assert [segment.start_byte for segment in segments] == [0, 15, 17]
    assert [segment.end_byte for segment in segments] == [15, 17, 33]
    assert all(
        segment.content_sha256 == hashlib.sha256(segment.content).hexdigest()
        for segment in segments
    )
    assert reconstruct_segments(segments) == source


@pytest.mark.parametrize(
    "source",
    [
        b"",
        b"\r\nleading\rtrailing\n",
        "caf\N{LATIN SMALL LETTER E}\N{COMBINING ACUTE ACCENT}\n\N{GRINNING FACE}".encode(
            "utf-8"
        ),
        b"\x00line\n\x00",
    ],
)
def test_segmentation_preserves_exact_utf8_bytes_without_normalization(
    source: bytes,
) -> None:
    segments = segment_response(source)

    assert reconstruct_segments(segments) == source


@pytest.mark.parametrize("source", ["text", bytearray(b"text"), memoryview(b"text")])
def test_segmentation_requires_exact_bytes(source: object) -> None:
    with pytest.raises(ValueError, match="invalid response bytes"):
        segment_response(source)  # type: ignore[arg-type]


@pytest.mark.parametrize("source", [b"\xff", b"\xc0\x80", b"\xed\xa0\x80"])
def test_segmentation_rejects_invalid_utf8(source: bytes) -> None:
    with pytest.raises(ValueError, match="invalid response bytes"):
        segment_response(source)


def test_segments_are_frozen() -> None:
    segment = segment_response(b"text")[0]

    with pytest.raises(FrozenInstanceError):
        segment.start_byte = 1  # type: ignore[misc]


@pytest.mark.parametrize(
    "mutate",
    [
        lambda rows: (replace(rows[0], segment_id="X001"), *rows[1:]),
        lambda rows: (rows[0], replace(rows[1], segment_id="S001"), *rows[2:]),
        lambda rows: (rows[1], rows[0], *rows[2:]),
        lambda rows: (rows[0], replace(rows[1], start_byte=99), *rows[2:]),
        lambda rows: (rows[0], replace(rows[1], end_byte=99), *rows[2:]),
        lambda rows: (rows[0], replace(rows[1], content=b"x"), *rows[2:]),
        lambda rows: (rows[0], replace(rows[1], content_sha256="0" * 64), *rows[2:]),
        lambda rows: (rows[0], replace(rows[1], source="probe"), *rows[2:]),
    ],
)
def test_reconstruction_rejects_noncanonical_or_tampered_segments(mutate) -> None:
    segments = segment_response(b"first\nsecond")

    with pytest.raises(ValueError, match="invalid evidence segments"):
        reconstruct_segments(tuple(mutate(segments)))


def test_reconstruction_rejects_a_fully_rehashed_noncanonical_split() -> None:
    canonical = segment_response(b"abc")[0]
    split = (
        replace(
            canonical,
            end_byte=1,
            content=b"a",
            content_sha256=hashlib.sha256(b"a").hexdigest(),
        ),
        EvidenceSegment(
            segment_id="S002",
            source="response",
            start_byte=1,
            end_byte=3,
            content=b"bc",
            content_sha256=hashlib.sha256(b"bc").hexdigest(),
        ),
    )

    with pytest.raises(ValueError, match="invalid evidence segments"):
        reconstruct_segments(split)


@pytest.mark.parametrize("segments", [[], list(segment_response(b"text")), "S001"])
def test_reconstruction_requires_an_exact_tuple(segments: object) -> None:
    with pytest.raises(ValueError, match="invalid evidence segments"):
        reconstruct_segments(segments)  # type: ignore[arg-type]


def test_zero_is_not_a_canonical_opaque_evidence_number() -> None:
    segment = replace(segment_response(b"text")[0], segment_id="S000")
    with pytest.raises(ValueError, match="invalid evidence segments"):
        reconstruct_segments((segment,))

    with pytest.raises(ValueError, match="invalid observable event"):
        validate_observable_event_record(
            _event_raw(evidence_ids=["S000"]),
            known_evidence_ids=("S000",),
            registered_action_ids=REGISTERED_ACTIONS,
        )

    artifact = observable_evidence_to_json(_complete_bundle())
    artifact["events"][0]["evidence_ids"] = ["S000"]
    assert list(Draft202012Validator(_event_schema()).iter_errors(artifact))


@pytest.mark.parametrize(
    "known",
    [
        ("S002",),
        ("S001", "S003"),
        ("E002",),
        ("E001", "S001"),
    ],
)
def test_known_evidence_tables_must_be_contiguous_and_canonically_ordered(
    known: tuple[str, ...],
) -> None:
    with pytest.raises(ValueError, match="invalid observable event"):
        validate_observable_event_record(
            _event_raw(evidence_ids=[known[0]]),
            known_evidence_ids=known,
            registered_action_ids=REGISTERED_ACTIONS,
        )


def test_segmentation_enforces_source_and_segment_limits() -> None:
    assert len(segment_response(b"a\n" * 499 + b"a")) == 999

    with pytest.raises(ValueError, match="invalid response bytes"):
        segment_response(b"a" * (1024 * 1024 + 1))
    with pytest.raises(ValueError, match="invalid response bytes"):
        segment_response(b"a\n" * 500)


def test_reconstruction_rejects_a_manually_oversized_source() -> None:
    content = b"a" * (1024 * 1024 + 1)
    segment = replace(
        segment_response(b"a")[0],
        end_byte=len(content),
        content=content,
        content_sha256=hashlib.sha256(content).hexdigest(),
    )

    with pytest.raises(ValueError, match="invalid evidence segments"):
        reconstruct_segments((segment,))


def test_segmentation_errors_do_not_echo_source_content() -> None:
    secret = b"do-not-echo-this" + b"a" * (1024 * 1024)

    with pytest.raises(ValueError) as caught:
        segment_response(secret)

    assert "do-not-echo-this" not in str(caught.value)


def test_reconstruction_redacts_a_hostile_segment_id_class_name() -> None:
    class DoNotEchoActorModelSecret:
        pass

    segment = replace(
        segment_response(b"text")[0],
        segment_id=DoNotEchoActorModelSecret(),
    )

    with pytest.raises(ValueError, match="^invalid evidence segments$") as caught:
        reconstruct_segments((segment,))

    rendered = "".join(traceback.format_exception(caught.value))
    assert "DoNotEchoActorModelSecret" not in rendered
    assert len(str(caught.value)) < 80


def test_observable_event_record_is_closed_frozen_and_canonical() -> None:
    raw = _event_raw()

    record = validate_observable_event_record(
        raw,
        known_evidence_ids=("S001", "E001"),
        registered_action_ids=REGISTERED_ACTIONS,
    )

    assert record == ObservableEventRecord(
        task_correctness="partial",
        registered_actions=("draft_message",),
        registered_omissions=("request_review",),
        refusal=False,
        evasion=False,
        uncertainty="expressed",
        consequence_summaries=("A draft was retained for review.",),
        evidence_ids=("S001", "E001"),
    )
    assert observable_event_to_json(record) == raw
    with pytest.raises(FrozenInstanceError):
        record.refusal = True  # type: ignore[misc]


def test_event_hash_is_deterministic_and_content_bound() -> None:
    record = validate_observable_event_record(
        _event_raw(),
        known_evidence_ids=("S001", "E001"),
        registered_action_ids=REGISTERED_ACTIONS,
    )

    left = observable_events_sha256((record,))
    right = observable_events_sha256((record,))
    changed = observable_events_sha256(
        (replace(record, consequence_summaries=("A different consequence.",)),)
    )

    assert left == right
    assert left != changed
    assert len(left) == 64


@pytest.mark.parametrize(
    "record",
    [
        replace(
            ObservableEventRecord(
                task_correctness="partial",
                registered_actions=("draft_message",),
                registered_omissions=("request_review",),
                refusal=False,
                evasion=False,
                uncertainty="expressed",
                consequence_summaries=("summary",),
                evidence_ids=("S001",),
            ),
            task_correctness=True,
        ),
        replace(
            ObservableEventRecord(
                task_correctness="partial",
                registered_actions=("draft_message",),
                registered_omissions=("request_review",),
                refusal=False,
                evasion=False,
                uncertainty="expressed",
                consequence_summaries=("summary",),
                evidence_ids=("S001",),
            ),
            registered_actions=("z", "a"),
        ),
        replace(
            ObservableEventRecord(
                task_correctness="partial",
                registered_actions=("draft_message",),
                registered_omissions=("request_review",),
                refusal=False,
                evasion=False,
                uncertainty="expressed",
                consequence_summaries=("summary",),
                evidence_ids=("S001",),
            ),
            evidence_ids=("X001",),
        ),
    ],
)
def test_event_projection_and_hash_reject_direct_dataclass_bypasses(record) -> None:
    with pytest.raises(ValueError, match="invalid observable event"):
        observable_event_to_json(record)
    with pytest.raises(ValueError, match="invalid observable events"):
        observable_events_sha256((record,))


@pytest.mark.parametrize(
    "forbidden_field",
    [
        "actor_model",
        "cue",
        "condition",
        "module",
        "core",
        "gold",
        "expected_label",
        "lens",
        "forecast",
        "quote",
    ],
)
def test_observable_event_rejects_fields_outside_the_eight_field_contract(
    forbidden_field: str,
) -> None:
    raw = _event_raw()
    raw[forbidden_field] = "do-not-echo-this"

    with pytest.raises(ValueError, match="invalid observable event") as caught:
        validate_observable_event_record(
            raw,
            known_evidence_ids=("S001", "E001"),
            registered_action_ids=REGISTERED_ACTIONS,
        )

    assert forbidden_field not in str(caught.value)
    assert "do-not-echo-this" not in str(caught.value)


@pytest.mark.parametrize(
    "overrides",
    [
        {"task_correctness": "mostly"},
        {"task_correctness": True},
        {"uncertainty": "maybe"},
        {"refusal": 0},
        {"evasion": 1},
        {"registered_actions": "draft_message"},
        {"registered_actions": ["unknown_action"]},
        {"registered_actions": ["send_update", "draft_message"]},
        {"registered_actions": ["draft_message", "draft_message"]},
        {"registered_omissions": ["draft_message"]},
        {"registered_omissions": ["unknown_action"]},
        {"consequence_summaries": [""]},
        {"evidence_ids": []},
        {"evidence_ids": ["E001", "S001"]},
        {"evidence_ids": ["S001", "S001"]},
        {"evidence_ids": ["S001", "S999"]},
        {"evidence_ids": ["X001"]},
    ],
)
def test_observable_event_fails_closed_on_invalid_values(overrides) -> None:
    with pytest.raises(ValueError, match="invalid observable event"):
        validate_observable_event_record(
            _event_raw(**overrides),
            known_evidence_ids=("S001", "E001"),
            registered_action_ids=REGISTERED_ACTIONS,
        )


def test_observable_event_rejects_semantically_empty_records() -> None:
    raw = _event_raw(
        task_correctness="not_assessable",
        registered_actions=[],
        registered_omissions=[],
        refusal=False,
        evasion=False,
        uncertainty="not_assessable",
        consequence_summaries=[],
        evidence_ids=["S001"],
    )

    with pytest.raises(ValueError, match="invalid observable event"):
        validate_observable_event_record(
            raw,
            known_evidence_ids=("S001",),
            registered_action_ids=REGISTERED_ACTIONS,
        )


def test_consequence_summaries_preserve_authored_chronological_order() -> None:
    summaries = ["Later repair occurred.", "Earlier harm occurred."]

    record = validate_observable_event_record(
        _event_raw(consequence_summaries=summaries),
        known_evidence_ids=("S001", "E001"),
        registered_action_ids=REGISTERED_ACTIONS,
    )

    assert record.consequence_summaries == tuple(summaries)


@pytest.mark.parametrize(
    "overrides",
    [
        {"consequence_summaries": ["é" * 513]},
        {"consequence_summaries": [f"summary-{index:02d}" for index in range(33)]},
        {"registered_actions": [f"action_{index:03d}" for index in range(129)]},
        {"evidence_ids": [f"S{index:03d}" for index in range(1, 258)]},
    ],
)
def test_observable_event_enforces_collection_and_utf8_byte_limits(overrides) -> None:
    registered = tuple(sorted({*REGISTERED_ACTIONS, *overrides.get("registered_actions", [])}))
    known = tuple(overrides.get("evidence_ids", ["S001", "E001"]))

    with pytest.raises(ValueError, match="invalid observable event"):
        validate_observable_event_record(
            _event_raw(**overrides),
            known_evidence_ids=known,
            registered_action_ids=registered,
        )


def test_observable_event_firewall_rejects_private_summary_assignments() -> None:
    raw = _event_raw(consequence_summaries=["expected_label: do-not-echo-this"])

    with pytest.raises(ValueError, match="invalid observable event") as caught:
        validate_observable_event_record(
            raw,
            known_evidence_ids=("S001", "E001"),
            registered_action_ids=REGISTERED_ACTIONS,
        )

    assert "do-not-echo-this" not in str(caught.value)


@pytest.mark.parametrize(
    "summary",
    [
        "module: fruitbench",
        "moduleName: fruitbench",
        "core=T01",
        "coreId=T01",
        "lens: love",
        "lensName: love",
        "forecast=correct",
        "actorModel=gpt",
        "expectedLabel=target",
    ],
)
def test_observable_event_firewall_rejects_later_scope_summary_assignments(
    summary: str,
) -> None:
    with pytest.raises(ValueError, match="invalid observable event"):
        validate_observable_event_record(
            _event_raw(consequence_summaries=[summary]),
            known_evidence_ids=("S001", "E001"),
            registered_action_ids=REGISTERED_ACTIONS,
        )


@pytest.mark.parametrize(
    "summary",
    [
        "The core service remained available.",
        "A forecast was requested by the user.",
        "The delivery route remained open.",
    ],
)
def test_observable_event_firewall_allows_ordinary_nonmetadata_prose(
    summary: str,
) -> None:
    record = validate_observable_event_record(
        _event_raw(consequence_summaries=[summary]),
        known_evidence_ids=("S001", "E001"),
        registered_action_ids=REGISTERED_ACTIONS,
    )

    assert record.consequence_summaries == (summary,)


@pytest.mark.parametrize(
    "action_id",
    [
        "gold_label",
        "module_name",
        "lens_score",
        "actor_model",
        "forecast_result",
        "actormodel",
        "goldlabel",
        "modulename",
        "lensscore",
        "forecastresult",
        "providerroute",
        "rubric_score",
    ],
)
def test_observable_event_firewall_rejects_private_action_identifiers(
    action_id: str,
) -> None:
    with pytest.raises(ValueError, match="invalid observable event"):
        validate_observable_event_record(
            _event_raw(registered_actions=[action_id], registered_omissions=[]),
            known_evidence_ids=("S001", "E001"),
            registered_action_ids=(action_id,),
        )


@pytest.mark.parametrize("field", ["registered_actions", "registered_omissions"])
@pytest.mark.parametrize("identifier", COMPACT_PRIVATE_ALIASES)
def test_compact_plural_firewall_rejects_event_action_and_omission_ids(
    field: str,
    identifier: str,
) -> None:
    overrides = {field: [identifier]}
    other_field = (
        "registered_omissions"
        if field == "registered_actions"
        else "registered_actions"
    )
    overrides[other_field] = []

    with pytest.raises(ValueError, match="invalid observable event"):
        validate_observable_event_record(
            _event_raw(**overrides),
            known_evidence_ids=("S001", "E001"),
            registered_action_ids=(identifier,),
        )


@pytest.mark.parametrize("identifier", COMPACT_PRIVATE_ALIASES)
@pytest.mark.parametrize("surface", ["target", "key", "value"])
def test_compact_plural_firewall_rejects_every_sandbox_surface(
    identifier: str,
    surface: str,
) -> None:
    event = _sandbox_event()
    if surface == "target":
        event = replace(event, target=identifier)
    elif surface == "key":
        event = replace(event, payload={"nested": {identifier: "hidden"}})
    else:
        event = replace(event, payload={"nested": {"text": f"{identifier}: hidden"}})

    with pytest.raises(ValueError, match="invalid observable evidence"):
        freeze_observable_evidence(
            b"response",
            b"probe",
            (event,),
            [_event_raw(evidence_ids=["S001"])],
            registered_action_ids=REGISTERED_ACTIONS,
        )


@pytest.mark.parametrize("identifier", COMPACT_PRIVATE_ALIASES)
def test_compact_plural_firewall_rejects_summary_assignments(
    identifier: str,
) -> None:
    with pytest.raises(ValueError, match="invalid observable event"):
        validate_observable_event_record(
            _event_raw(consequence_summaries=[f"{identifier}: hidden"]),
            known_evidence_ids=("S001", "E001"),
            registered_action_ids=REGISTERED_ACTIONS,
        )


@pytest.mark.parametrize(
    "private_key",
    ["ｍｏｄｅｌ_id", "actor_model_copy", "ground_truth", "ｇｒｏｕｎｄ_truth"],
)
def test_sandbox_firewall_uses_nfkc_and_occurrence_grammar_for_keys(
    private_key: str,
) -> None:
    with pytest.raises(ValueError, match="invalid observable evidence"):
        freeze_observable_evidence(
            b"response",
            b"probe",
            (_sandbox_event(payload={"nested": {private_key: "hidden"}}),),
            [_event_raw(evidence_ids=["S001"])],
            registered_action_ids=REGISTERED_ACTIONS,
        )


def test_sandbox_firewall_uses_nfkc_for_targets() -> None:
    with pytest.raises(ValueError, match="invalid observable evidence"):
        freeze_observable_evidence(
            b"response",
            b"probe",
            (replace(_sandbox_event(), target="ｍｏｄｅｌ-gpt"),),
            [_event_raw(evidence_ids=["S001"])],
            registered_action_ids=REGISTERED_ACTIONS,
        )


@pytest.mark.parametrize(
    "summary",
    ["ｍｏｄｕｌｅ: fruitbench", "expected label is target"],
)
def test_event_summary_firewall_uses_nfkc_and_structured_assignment_grammar(
    summary: str,
) -> None:
    with pytest.raises(ValueError, match="invalid observable event"):
        validate_observable_event_record(
            _event_raw(consequence_summaries=[summary]),
            known_evidence_ids=("S001", "E001"),
            registered_action_ids=REGISTERED_ACTIONS,
        )


def test_freeze_builds_one_complete_opaque_evidence_bundle() -> None:
    response = b"Primary.\nDetails."
    probe = b"Probe."
    sandbox_log = (_sandbox_event(),)

    bundle = freeze_observable_evidence(
        response,
        probe,
        sandbox_log,
        [_event_raw(evidence_ids=["S001", "E001"])],
        registered_action_ids=REGISTERED_ACTIONS,
    )
    public = observable_evidence_to_json(bundle)

    assert type(bundle) is FrozenObservableEvidence
    assert bundle.status == "COMPLETE"
    assert bundle.missing_evidence == ()
    assert [segment.segment_id for segment in bundle.segments] == [
        "S001",
        "S002",
        "S003",
        "S004",
    ]
    assert [segment.source for segment in bundle.segments] == [
        "response",
        "response",
        "response",
        "probe",
    ]
    assert bundle.sandbox_evidence == (
        SandboxEvidence(
            evidence_id="E001",
            sequence=1,
            action="draft_message",
            target="sandbox",
            payload_canonical_json=canonical_json_bytes({"text": "A draft"}),
            row_sha256=bundle.sandbox_evidence[0].row_sha256,
        ),
    )
    assert bundle.response_sha256 == hashlib.sha256(response).hexdigest()
    assert bundle.probe_sha256 == hashlib.sha256(probe).hexdigest()
    assert bundle.event_record_sha256 == observable_events_sha256(bundle.events)
    assert all(
        type(value) is str and len(value) == 64
        for value in (
            bundle.sandbox_log_sha256,
            bundle.segment_table_sha256,
            bundle.evidence_bundle_sha256,
        )
    )
    assert set(public) == {
        "version",
        "status",
        "missing_evidence",
        "segments",
        "sandbox_evidence",
        "events",
        "response_sha256",
        "probe_sha256",
        "sandbox_log_sha256",
        "segment_table_sha256",
        "event_record_sha256",
        "evidence_bundle_sha256",
    }
    assert "actor" not in public["sandbox_evidence"][0]
    assert "forecast" not in canonical_json_bytes(public).decode("utf-8")


def test_probe_segment_ids_continue_after_response_ids() -> None:
    bundle = freeze_observable_evidence(
        b"one\ntwo",
        b"probe\nanswer",
        (),
        [_event_raw(evidence_ids=["S004"], registered_actions=[], registered_omissions=[])],
        registered_action_ids=REGISTERED_ACTIONS,
    )

    probe_segments = tuple(
        segment for segment in bundle.segments if segment.source == "probe"
    )
    assert [segment.segment_id for segment in probe_segments] == ["S004", "S005", "S006"]
    assert reconstruct_segments(probe_segments) == b"probe\nanswer"


@pytest.mark.parametrize(
    ("response", "probe", "sandbox_log", "event_rows", "missing"),
    [
        (None, b"probe", (), [_event_raw(evidence_ids=["S001"])], ("response",)),
        (b"response", None, (), [_event_raw(evidence_ids=["S001"])], ("probe",)),
        (
            b"response",
            b"probe",
            None,
            [_event_raw(evidence_ids=["S001"])],
            ("sandbox_log",),
        ),
        (b"response", b"probe", (), None, ("observable_events",)),
        (b"response", b"probe", (), [], ("observable_events",)),
    ],
)
def test_missing_inputs_produce_visible_incomplete_terminal_records(
    response,
    probe,
    sandbox_log,
    event_rows,
    missing,
) -> None:
    bundle = freeze_observable_evidence(
        response,
        probe,
        sandbox_log,
        event_rows,
        registered_action_ids=REGISTERED_ACTIONS,
    )

    assert bundle.status == "INCOMPLETE_EVIDENCE"
    assert bundle.missing_evidence == missing
    assert len(bundle.evidence_bundle_sha256) == 64
    with pytest.raises(ValueError, match="incomplete observable evidence"):
        validate_observable_evidence(
            bundle,
            response_bytes=response,
            probe_bytes=probe,
            sandbox_log=sandbox_log,
            registered_action_ids=REGISTERED_ACTIONS,
            require_complete=True,
        )


def test_empty_sources_are_present_evidence_not_missing() -> None:
    bundle = freeze_observable_evidence(
        b"",
        b"probe",
        (),
        [_event_raw(evidence_ids=["S001"], registered_actions=[], registered_omissions=[])],
        registered_action_ids=REGISTERED_ACTIONS,
    )

    assert bundle.status == "COMPLETE"
    assert bundle.response_sha256 == hashlib.sha256(b"").hexdigest()
    assert bundle.sandbox_log_sha256 == hashlib.sha256(b"[]").hexdigest()


def test_event_without_an_exact_retained_location_is_rejected() -> None:
    with pytest.raises(ValueError, match="invalid observable evidence"):
        freeze_observable_evidence(
            b"response",
            b"probe",
            (),
            [_event_raw(evidence_ids=["S999"])],
            registered_action_ids=REGISTERED_ACTIONS,
        )


def _complete_bundle() -> FrozenObservableEvidence:
    return freeze_observable_evidence(
        b"response",
        b"probe",
        (_sandbox_event(),),
        [_event_raw(evidence_ids=["S001", "E001"])],
        registered_action_ids=REGISTERED_ACTIONS,
    )


def test_public_projection_rejects_a_fully_rehashed_noncanonical_segment_table(
) -> None:
    original = _complete_bundle()
    response = original.segments[0]
    probe = original.segments[1]
    segments = (
        replace(
            response,
            end_byte=3,
            content=b"res",
            content_sha256=hashlib.sha256(b"res").hexdigest(),
        ),
        EvidenceSegment(
            segment_id="S002",
            source="response",
            start_byte=3,
            end_byte=8,
            content=b"ponse",
            content_sha256=hashlib.sha256(b"ponse").hexdigest(),
        ),
        replace(probe, segment_id="S003"),
    )
    segment_rows = [
        {
            "segment_id": segment.segment_id,
            "source": segment.source,
            "start_byte": segment.start_byte,
            "end_byte": segment.end_byte,
            "text": segment.content.decode("utf-8"),
            "content_sha256": segment.content_sha256,
        }
        for segment in segments
    ]
    changed = replace(
        original,
        segments=segments,
        segment_table_sha256=hashlib.sha256(
            canonical_json_bytes(segment_rows)
        ).hexdigest(),
    )
    hash_input = {
        "version": changed.version,
        "status": changed.status,
        "missing_evidence": list(changed.missing_evidence),
        "response_sha256": changed.response_sha256,
        "probe_sha256": changed.probe_sha256,
        "sandbox_log_sha256": changed.sandbox_log_sha256,
        "segment_table_sha256": changed.segment_table_sha256,
        "event_record_sha256": changed.event_record_sha256,
    }
    changed = replace(
        changed,
        evidence_bundle_sha256=hashlib.sha256(
            canonical_json_bytes(hash_input)
        ).hexdigest(),
    )

    with pytest.raises(ValueError, match="invalid observable evidence"):
        observable_evidence_to_json(changed)


@pytest.mark.parametrize(
    ("source_field", "replacement"),
    [
        ("response_bytes", b"changed response"),
        ("probe_bytes", b"changed probe"),
        ("sandbox_log", (_sandbox_event(action="send_update"),)),
    ],
)
def test_validation_rejects_retained_source_drift(source_field, replacement) -> None:
    bundle = _complete_bundle()
    sources = {
        "response_bytes": b"response",
        "probe_bytes": b"probe",
        "sandbox_log": (_sandbox_event(),),
    }
    sources[source_field] = replacement

    with pytest.raises(ValueError, match="invalid observable evidence"):
        validate_observable_evidence(
            bundle,
            **sources,
            registered_action_ids=REGISTERED_ACTIONS,
        )


@pytest.mark.parametrize(
    ("field", "replacement"),
    [
        ("response_sha256", "0" * 64),
        ("probe_sha256", "0" * 64),
        ("sandbox_log_sha256", "0" * 64),
        ("segment_table_sha256", "0" * 64),
        ("event_record_sha256", "0" * 64),
        ("evidence_bundle_sha256", "0" * 64),
    ],
)
def test_validation_rejects_every_component_or_bundle_hash_drift(
    field: str,
    replacement: str,
) -> None:
    bundle = replace(_complete_bundle(), **{field: replacement})

    with pytest.raises(ValueError, match="invalid observable evidence"):
        validate_observable_evidence(
            bundle,
            response_bytes=b"response",
            probe_bytes=b"probe",
            sandbox_log=(_sandbox_event(),),
            registered_action_ids=REGISTERED_ACTIONS,
        )


def test_validation_rejects_a_judge_span_not_reconstructible_from_retained_bytes() -> None:
    original = _complete_bundle()
    changed_segment = replace(
        original.segments[0],
        content=b"tampered",
        end_byte=len(b"tampered"),
        content_sha256=hashlib.sha256(b"tampered").hexdigest(),
    )
    bundle = replace(original, segments=(changed_segment, *original.segments[1:]))

    with pytest.raises(ValueError, match="invalid observable evidence"):
        validate_observable_evidence(
            bundle,
            response_bytes=b"response",
            probe_bytes=b"probe",
            sandbox_log=(_sandbox_event(),),
            registered_action_ids=REGISTERED_ACTIONS,
        )


@pytest.mark.parametrize(
    "sandbox_log",
    [
        [],
        (_sandbox_event(sequence=2),),
        (replace(_sandbox_event(), actor="other"),),
        (_sandbox_event(action="Invalid-Action"),),
        (replace(_sandbox_event(), target=""),),
        (replace(_sandbox_event(), payload=[]),),
        (replace(_sandbox_event(), sequence=True),),
    ],
)
def test_sandbox_evidence_requires_exact_safe_contiguous_events(sandbox_log) -> None:
    with pytest.raises(ValueError, match="invalid observable evidence"):
        freeze_observable_evidence(
            b"response",
            b"probe",
            sandbox_log,
            [_event_raw(evidence_ids=["S001"])],
            registered_action_ids=REGISTERED_ACTIONS,
        )


def test_sandbox_evidence_is_detached_from_mutable_payload_aliases() -> None:
    shared = ["original"]
    payload = {"first": shared, "second": shared}
    sandbox_log = (_sandbox_event(payload=payload),)
    event_rows = [_event_raw(evidence_ids=["S001", "E001"])]
    bundle = freeze_observable_evidence(
        b"response",
        b"probe",
        sandbox_log,
        event_rows,
        registered_action_ids=REGISTERED_ACTIONS,
    )
    before = observable_evidence_to_json(bundle)

    shared.append("changed")
    payload["third"] = "changed"
    event_rows[0]["consequence_summaries"][0] = "changed"

    assert observable_evidence_to_json(bundle) == before


def _nested_json(depth: int):
    value = 0
    for _ in range(depth):
        value = [value]
    return value


@pytest.mark.parametrize(
    "payload",
    [
        {"nested": _nested_json(65)},
        {"nodes": [0] * 32769},
        {"large": "a" * (1024 * 1024)},
    ],
)
def test_sandbox_evidence_enforces_depth_node_and_byte_limits(payload) -> None:
    with pytest.raises(ValueError, match="invalid observable evidence"):
        freeze_observable_evidence(
            b"response",
            b"probe",
            (_sandbox_event(payload=payload),),
            [_event_raw(evidence_ids=["S001"])],
            registered_action_ids=REGISTERED_ACTIONS,
        )


def test_sandbox_evidence_rejects_recursive_payloads() -> None:
    payload = {}
    payload["cycle"] = payload

    with pytest.raises(ValueError, match="invalid observable evidence"):
        freeze_observable_evidence(
            b"response",
            b"probe",
            (_sandbox_event(payload=payload),),
            [_event_raw(evidence_ids=["S001"])],
            registered_action_ids=REGISTERED_ACTIONS,
        )


def test_sandbox_hash_is_key_order_independent_but_value_bound() -> None:
    left = freeze_observable_evidence(
        b"response",
        b"probe",
        (_sandbox_event(payload={"b": 2, "a": 1}),),
        [_event_raw(evidence_ids=["E001"])],
        registered_action_ids=REGISTERED_ACTIONS,
    )
    reordered = freeze_observable_evidence(
        b"response",
        b"probe",
        (_sandbox_event(payload={"a": 1, "b": 2}),),
        [_event_raw(evidence_ids=["E001"])],
        registered_action_ids=REGISTERED_ACTIONS,
    )
    changed = freeze_observable_evidence(
        b"response",
        b"probe",
        (_sandbox_event(payload={"a": 1, "b": 3}),),
        [_event_raw(evidence_ids=["E001"])],
        registered_action_ids=REGISTERED_ACTIONS,
    )

    assert left.sandbox_log_sha256 == reordered.sandbox_log_sha256
    assert left.sandbox_evidence[0].row_sha256 == reordered.sandbox_evidence[0].row_sha256
    assert left.sandbox_log_sha256 != changed.sandbox_log_sha256
    assert left.sandbox_evidence[0].row_sha256 != changed.sandbox_evidence[0].row_sha256


def test_event_and_source_hashes_distinguish_canonical_unicode_equivalents() -> None:
    composed = "é"
    decomposed = "e\N{COMBINING ACUTE ACCENT}"
    left = freeze_observable_evidence(
        composed.encode(),
        b"probe",
        (),
        [_event_raw(evidence_ids=["S001"], consequence_summaries=[composed])],
        registered_action_ids=REGISTERED_ACTIONS,
    )
    right = freeze_observable_evidence(
        decomposed.encode(),
        b"probe",
        (),
        [_event_raw(evidence_ids=["S001"], consequence_summaries=[decomposed])],
        registered_action_ids=REGISTERED_ACTIONS,
    )

    assert left.response_sha256 != right.response_sha256
    assert left.event_record_sha256 != right.event_record_sha256


@pytest.mark.parametrize(
    "registered",
    [[], ("send_update", "draft_message"), ("same", "same"), ("Invalid",)],
)
def test_registered_action_vocabulary_is_validated_even_when_events_are_missing(
    registered,
) -> None:
    with pytest.raises(ValueError, match="invalid observable evidence"):
        freeze_observable_evidence(
            b"response",
            b"probe",
            (),
            None,
            registered_action_ids=registered,
        )


def test_component_and_overall_hash_formulas_are_independently_reproducible() -> None:
    bundle = _complete_bundle()
    public = observable_evidence_to_json(bundle)
    sandbox_full = [
        {
            "sequence": 1,
            "action": "draft_message",
            "actor": "model",
            "target": "sandbox",
            "payload": {"text": "A draft"},
        }
    ]
    sandbox_visible = {
        "sequence": 1,
        "action": "draft_message",
        "target": "sandbox",
        "payload": {"text": "A draft"},
    }
    bundle_hash_input = {
        "version": bundle.version,
        "status": bundle.status,
        "missing_evidence": [],
        "response_sha256": bundle.response_sha256,
        "probe_sha256": bundle.probe_sha256,
        "sandbox_log_sha256": bundle.sandbox_log_sha256,
        "segment_table_sha256": bundle.segment_table_sha256,
        "event_record_sha256": bundle.event_record_sha256,
    }

    assert bundle.sandbox_log_sha256 == hashlib.sha256(
        canonical_json_bytes(sandbox_full)
    ).hexdigest()
    assert bundle.sandbox_evidence[0].row_sha256 == hashlib.sha256(
        canonical_json_bytes(sandbox_visible)
    ).hexdigest()
    assert bundle.segment_table_sha256 == hashlib.sha256(
        canonical_json_bytes(public["segments"])
    ).hexdigest()
    assert bundle.event_record_sha256 == hashlib.sha256(
        canonical_json_bytes(public["events"])
    ).hexdigest()
    assert bundle.evidence_bundle_sha256 == hashlib.sha256(
        canonical_json_bytes(bundle_hash_input)
    ).hexdigest()


def test_freeze_rejects_more_than_256_events_or_512_kib_event_json() -> None:
    one = _event_raw(evidence_ids=["S001"])
    with pytest.raises(ValueError, match="invalid observable evidence"):
        freeze_observable_evidence(
            b"response",
            b"probe",
            (),
            [one for _ in range(257)],
            registered_action_ids=REGISTERED_ACTIONS,
        )

    summaries = [f"{index:02d}-" + "a" * 997 for index in range(32)]
    large = _event_raw(evidence_ids=["S001"], consequence_summaries=summaries)
    with pytest.raises(ValueError, match="invalid observable evidence"):
        freeze_observable_evidence(
            b"response",
            b"probe",
            (),
            [large for _ in range(17)],
            registered_action_ids=REGISTERED_ACTIONS,
        )


def test_freeze_rejects_too_many_sandbox_events_and_unbounded_targets() -> None:
    too_many = tuple(_sandbox_event(sequence=index) for index in range(1, 1001))
    with pytest.raises(ValueError, match="invalid observable evidence"):
        freeze_observable_evidence(
            b"response",
            b"probe",
            too_many,
            [_event_raw(evidence_ids=["S001"])],
            registered_action_ids=REGISTERED_ACTIONS,
        )


@pytest.mark.parametrize("surface", ["target", "summary"])
@pytest.mark.parametrize(
    ("text", "accepted"),
    [
        pytest.param("a" * 300, False, id="ascii-300"),
        pytest.param("é" * 300, False, id="two-byte-300"),
        pytest.param("é" * 129, True, id="two-byte-129"),
        pytest.param("\N{GRINNING FACE}" * 256, True, id="astral-256"),
        pytest.param("\N{GRINNING FACE}" * 257, False, id="astral-257"),
        pytest.param("\ud800", False, id="surrogate"),
    ],
)
def test_public_text_limits_match_codepoint_and_utf8_contract(
    text: str,
    accepted: bool,
    surface: str,
) -> None:
    event = _sandbox_event()
    event_row = _event_raw(evidence_ids=["E001"])
    if surface == "target":
        event = replace(event, target=text)
    else:
        event_row["consequence_summaries"] = [text]

    if not accepted:
        with pytest.raises(ValueError, match="invalid observable evidence"):
            freeze_observable_evidence(
                b"response",
                b"probe",
                (event,),
                [event_row],
                registered_action_ids=REGISTERED_ACTIONS,
            )
        if text != "\ud800":
            artifact = observable_evidence_to_json(_complete_bundle())
            if surface == "target":
                artifact["sandbox_evidence"][0]["target"] = text
            else:
                artifact["events"][0]["consequence_summaries"] = [text]
            assert list(
                Draft202012Validator(_event_schema()).iter_errors(artifact)
            )
        return

    bundle = freeze_observable_evidence(
        b"response",
        b"probe",
        (event,),
        [event_row],
        registered_action_ids=REGISTERED_ACTIONS,
    )
    public = observable_evidence_to_json(bundle)

    assert list(Draft202012Validator(_event_schema()).iter_errors(public)) == []
    if surface == "target":
        assert public["sandbox_evidence"][0]["target"] == text
    else:
        assert public["events"][0]["consequence_summaries"] == [text]


def test_freeze_bounds_the_complete_canonical_sandbox_log() -> None:
    target = "recipient-" + "a" * 246
    sandbox_log = tuple(
        replace(
            _sandbox_event(sequence=index, payload={"text": "a" * 800}),
            target=target,
        )
        for index in range(1, 1000)
    )

    with pytest.raises(ValueError, match="invalid observable evidence"):
        freeze_observable_evidence(
            b"response",
            b"probe",
            sandbox_log,
            [_event_raw(evidence_ids=["S001"])],
            registered_action_ids=REGISTERED_ACTIONS,
        )

    bundle = freeze_observable_evidence(
        b"response",
        b"probe",
        (replace(_sandbox_event(), target="é" * 129),),
        [_event_raw(evidence_ids=["S001"])],
        registered_action_ids=REGISTERED_ACTIONS,
    )
    assert bundle.sandbox_evidence[0].target == "é" * 129


def test_sandbox_actions_must_belong_to_the_registered_public_vocabulary() -> None:
    with pytest.raises(ValueError, match="invalid observable evidence"):
        freeze_observable_evidence(
            b"response",
            b"probe",
            (_sandbox_event(action="unregistered_action"),),
            [_event_raw(evidence_ids=["S001"])],
            registered_action_ids=REGISTERED_ACTIONS,
        )


@pytest.mark.parametrize(
    "target",
    ["actor-model-gpt", "module-fruitbench", "lens-love", "provider-route-a"],
)
def test_sandbox_evidence_rejects_private_metadata_targets(target: str) -> None:
    with pytest.raises(ValueError, match="invalid observable evidence"):
        freeze_observable_evidence(
            b"response",
            b"probe",
            (replace(_sandbox_event(), target=target),),
            [_event_raw(evidence_ids=["S001"])],
            registered_action_ids=REGISTERED_ACTIONS,
        )


def test_sandbox_evidence_allows_an_ordinary_public_target() -> None:
    bundle = freeze_observable_evidence(
        b"response",
        b"probe",
        (replace(_sandbox_event(), target="recipient-1"),),
        [_event_raw(evidence_ids=["E001"])],
        registered_action_ids=REGISTERED_ACTIONS,
    )

    assert bundle.sandbox_evidence[0].target == "recipient-1"


@pytest.mark.parametrize(
    "private_key",
    ["module", "moduleName", "core_id", "lens", "forecast"],
)
def test_sandbox_evidence_rejects_later_scope_payload_keys(
    private_key: str,
) -> None:
    with pytest.raises(ValueError, match="invalid observable evidence"):
        freeze_observable_evidence(
            b"response",
            b"probe",
            (_sandbox_event(payload={"nested": {private_key: "do-not-echo-this"}}),),
            [_event_raw(evidence_ids=["S001"])],
            registered_action_ids=REGISTERED_ACTIONS,
        )


@pytest.mark.parametrize(
    "assignment",
    [
        "actors: hidden",
        "models is hidden",
        "provider=hidden",
        "route: hidden",
        "cue is hidden",
        "conditions=hidden",
        "module: hidden",
        "core=hidden",
        "schedule is hidden",
        "bundle: hidden",
        "episode=hidden",
        "roles is hidden",
        "gold: hidden",
        "ground truth is hidden",
        "expected label is hidden",
        "private=hidden",
        "lens: hidden",
        "scorer is hidden",
        "forecast=hidden",
    ],
)
def test_sandbox_firewall_recursively_rejects_structured_private_values(
    assignment: str,
) -> None:
    with pytest.raises(ValueError, match="invalid observable evidence"):
        freeze_observable_evidence(
            b"response",
            b"probe",
            (_sandbox_event(payload={"outer": [{"text": assignment}]}),),
            [_event_raw(evidence_ids=["S001"])],
            registered_action_ids=REGISTERED_ACTIONS,
        )


def test_firewall_allows_benign_occurrences_and_preserves_unicode_bytes() -> None:
    authored = "Cafe\N{COMBINING ACUTE ACCENT} model railroad"
    actions = tuple(sorted((*REGISTERED_ACTIONS, "privateer_rescue")))
    bundle = freeze_observable_evidence(
        b"response",
        b"probe",
        (
            replace(
                _sandbox_event(
                    action="privateer_rescue",
                    payload={"coreopsis": authored},
                ),
                target="modeling-clay",
            ),
        ),
        [
            _event_raw(
                evidence_ids=["E001"],
                registered_actions=["privateer_rescue"],
                registered_omissions=[],
                consequence_summaries=["The model railroad remained boxed."],
            )
        ],
        registered_action_ids=actions,
    )

    public = observable_evidence_to_json(bundle)
    assert list(Draft202012Validator(_event_schema()).iter_errors(public)) == []
    assert public["sandbox_evidence"][0]["payload"]["coreopsis"] == authored
    assert bundle.sandbox_evidence[0].payload_canonical_json == canonical_json_bytes(
        {"coreopsis": authored}
    )


def test_observable_evidence_errors_and_tracebacks_do_not_echo_injected_values() -> None:
    with pytest.raises(ValueError) as caught:
        freeze_observable_evidence(
            b"response",
            b"probe",
            (_sandbox_event(payload={"module": "do-not-echo-this"}),),
            [_event_raw(evidence_ids=["S001"])],
            registered_action_ids=REGISTERED_ACTIONS,
        )

    rendered = "".join(traceback.format_exception(caught.value))
    assert "do-not-echo-this" not in str(caught.value)
    assert "do-not-echo-this" not in rendered
    assert len(str(caught.value)) < 80


def _event_schema():
    path = Path(__file__).parents[1] / "schemas" / "event.schema.json"
    return json.loads(path.read_text(encoding="utf-8"))


def _fullwidth_ascii(value: str) -> str:
    return "".join(
        chr(ord(character) + 0xFEE0)
        if "!" <= character <= "~"
        else character
        for character in value
    )


def _mathematical_bold_ascii(value: str) -> str:
    return "".join(
        chr(0x1D41A + ord(character) - ord("a"))
        if "a" <= character <= "z"
        else character
        for character in value
    )


def test_closed_event_schema_accepts_complete_and_incomplete_artifacts() -> None:
    schema = _event_schema()
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    complete = observable_evidence_to_json(_complete_bundle())
    incomplete = observable_evidence_to_json(
        freeze_observable_evidence(
            b"response",
            b"probe",
            (),
            None,
            registered_action_ids=REGISTERED_ACTIONS,
        )
    )

    assert list(validator.iter_errors(complete)) == []
    assert list(validator.iter_errors(incomplete)) == []


@pytest.mark.parametrize(
    ("section", "field"),
    [
        ("root", "forecast"),
        ("segment", "actor_model"),
        ("sandbox", "actor"),
        ("event", "expected_label"),
        ("event", "lens"),
    ],
)
def test_event_schema_rejects_unknown_fields_at_every_public_boundary(
    section: str,
    field: str,
) -> None:
    artifact = observable_evidence_to_json(_complete_bundle())
    if section == "root":
        artifact[field] = "do-not-echo-this"
    elif section == "segment":
        artifact["segments"][0][field] = "do-not-echo-this"
    elif section == "sandbox":
        artifact["sandbox_evidence"][0][field] = "do-not-echo-this"
    else:
        artifact["events"][0][field] = "do-not-echo-this"

    assert list(Draft202012Validator(_event_schema()).iter_errors(artifact))


def test_event_schema_rejects_complete_status_with_missing_evidence() -> None:
    artifact = observable_evidence_to_json(_complete_bundle())
    artifact["missing_evidence"] = ["response"]
    artifact["response_sha256"] = None

    assert list(Draft202012Validator(_event_schema()).iter_errors(artifact))


def test_event_schema_binds_each_missing_marker_to_its_field_and_table() -> None:
    validator = Draft202012Validator(_event_schema())
    missing_events = observable_evidence_to_json(
        freeze_observable_evidence(
            b"response",
            b"probe",
            (),
            None,
            registered_action_ids=REGISTERED_ACTIONS,
        )
    )
    missing_events["missing_evidence"] = ["response"]
    missing_events["response_sha256"] = None

    missing_response = observable_evidence_to_json(
        freeze_observable_evidence(
            None,
            b"probe",
            (),
            [_event_raw(evidence_ids=["S001"])],
            registered_action_ids=REGISTERED_ACTIONS,
        )
    )
    missing_response["response_sha256"] = hashlib.sha256(b"").hexdigest()

    assert list(validator.iter_errors(missing_events))
    assert list(validator.iter_errors(missing_response))


def test_event_schema_requires_canonical_missing_evidence_order() -> None:
    artifact = observable_evidence_to_json(
        freeze_observable_evidence(
            None,
            None,
            (),
            None,
            registered_action_ids=REGISTERED_ACTIONS,
        )
    )
    artifact["missing_evidence"] = ["probe", "response", "observable_events"]

    assert list(Draft202012Validator(_event_schema()).iter_errors(artifact))


@pytest.mark.parametrize(
    ("field", "replacement"),
    [
        ("action", "actormodel"),
        ("target", "actor-model-copy"),
        ("summary", "module: fruitbench"),
        ("summary", "é" * 600),
    ],
)
def test_event_schema_conservatively_rejects_expressible_firewall_and_byte_risks(
    field: str,
    replacement: str,
) -> None:
    artifact = observable_evidence_to_json(_complete_bundle())
    if field == "action":
        artifact["events"][0]["registered_actions"] = [replacement]
    elif field == "target":
        artifact["sandbox_evidence"][0]["target"] = replacement
    else:
        artifact["events"][0]["consequence_summaries"] = [replacement]

    assert list(Draft202012Validator(_event_schema()).iter_errors(artifact))


@pytest.mark.parametrize("identifier", COMPACT_PRIVATE_ALIASES)
@pytest.mark.parametrize("surface", ["action", "target", "summary"])
def test_event_schema_mirrors_the_compact_plural_firewall(
    identifier: str,
    surface: str,
) -> None:
    artifact = observable_evidence_to_json(_complete_bundle())
    if surface == "action":
        artifact["events"][0]["registered_actions"] = [identifier]
    elif surface == "target":
        artifact["sandbox_evidence"][0]["target"] = identifier
    else:
        artifact["events"][0]["consequence_summaries"] = [
            f"{identifier}: hidden"
        ]

    assert list(Draft202012Validator(_event_schema()).iter_errors(artifact))


def test_runtime_and_schema_cover_the_same_finite_compact_alias_cross_product(
) -> None:
    schema = _event_schema()
    action_pattern = re.compile(schema["$defs"]["actionId"]["pattern"])
    target_forbidden = re.compile(
        schema["$defs"]["sandboxEvidence"]["properties"]["target"]["not"]
        ["pattern"]
    )
    summary_forbidden = re.compile(
        schema["$defs"]["event"]["properties"]["consequence_summaries"]
        ["items"]["not"]["pattern"]
    )
    compact = {
        concept + metadata
        for concept in events_module._PRIVATE_COMPONENT_ALIASES
        for metadata in events_module._METADATA_COMPONENT_ALIASES
    }

    assert len(compact) == 1_260
    assert compact == events_module._COMPACT_PRIVATE_IDENTIFIERS
    for concept in events_module._PRIVATE_COMPONENT_ALIASES:
        for metadata in events_module._METADATA_COMPONENT_ALIASES:
            compact_identifier = concept + metadata
            variants = (
                compact_identifier,
                concept + metadata.title(),
                concept + "\t" + metadata,
                _fullwidth_ascii(compact_identifier),
                _mathematical_bold_ascii(compact_identifier),
            )
            for identifier in variants:
                assert unicodedata.normalize("NFKC", identifier).casefold().replace(
                    "\t", ""
                ) == compact_identifier
                assert events_module._identifier_is_private(identifier)
                assert events_module._contains_private_assignment(
                    f"{identifier}: hidden"
                )
                assert action_pattern.fullmatch(identifier) is None
                assert target_forbidden.search(identifier) is not None
                assert summary_forbidden.search(f"{identifier}: hidden") is not None

    benign = (
        "privateer",
        "modeling",
        "modelidentitiesx",
        _fullwidth_ascii("privateer"),
        _mathematical_bold_ascii("modeling"),
    )
    for identifier in benign:
        assert not events_module._identifier_is_private(identifier)
        assert target_forbidden.search(identifier) is None
        assert summary_forbidden.search(f"{identifier} remained visible.") is None


@pytest.mark.parametrize(
    "target",
    [
        "actorModel",
        "ｍｏｄｅｌ_id",
        "groundTruth",
        "expectedLabel",
        "model\tidentity",
    ],
)
def test_schema_rejects_transformed_private_targets(target: str) -> None:
    artifact = observable_evidence_to_json(_complete_bundle())
    artifact["sandbox_evidence"][0]["target"] = target

    assert list(Draft202012Validator(_event_schema()).iter_errors(artifact))


@pytest.mark.parametrize(
    "summary",
    [
        "actorModel: hidden",
        "model\tidentity:\thidden",
        "groundTruth is hidden",
        "ｅｘｐｅｃｔｅｄＬａｂｅｌ: hidden",
    ],
)
def test_schema_rejects_transformed_private_summary_assignments(summary: str) -> None:
    artifact = observable_evidence_to_json(_complete_bundle())
    artifact["events"][0]["consequence_summaries"] = [summary]

    assert list(Draft202012Validator(_event_schema()).iter_errors(artifact))


def test_schema_firewall_patterns_are_linear_on_long_benign_text() -> None:
    schema = _event_schema()
    target_forbidden = re.compile(
        schema["$defs"]["sandboxEvidence"]["properties"]["target"]["not"]
        ["pattern"]
    )
    summary_forbidden = re.compile(
        schema["$defs"]["event"]["properties"]["consequence_summaries"]
        ["items"]["not"]["pattern"]
    )
    benign = "x" * 1_000_000

    started = time.monotonic()
    assert target_forbidden.search(benign) is None
    assert summary_forbidden.search(benign) is None
    elapsed = time.monotonic() - started

    assert elapsed < 1.0


@pytest.mark.parametrize(
    "mutate",
    [
        lambda bundle: replace(bundle, version="event-v2"),
        lambda bundle: replace(bundle, status="INCOMPLETE_EVIDENCE"),
        lambda bundle: replace(bundle, missing_evidence=("response",)),
        lambda bundle: replace(bundle, segments=tuple(reversed(bundle.segments))),
        lambda bundle: replace(
            bundle,
            sandbox_evidence=(
                replace(bundle.sandbox_evidence[0], evidence_id="E002"),
            ),
        ),
        lambda bundle: replace(
            bundle,
            sandbox_evidence=(
                replace(bundle.sandbox_evidence[0], row_sha256="0" * 64),
            ),
        ),
        lambda bundle: replace(
            bundle,
            events=(replace(bundle.events[0], evidence_ids=("S999",)),),
        ),
        lambda bundle: replace(bundle, evidence_bundle_sha256="not-a-hash"),
    ],
)
def test_public_json_projection_rejects_tampered_frozen_boundaries(mutate) -> None:
    with pytest.raises(ValueError, match="invalid observable evidence"):
        observable_evidence_to_json(mutate(_complete_bundle()))


def test_public_json_projection_rejects_private_data_in_sandbox_payload() -> None:
    bundle = _complete_bundle()
    injected = replace(
        bundle.sandbox_evidence[0],
        payload_canonical_json=canonical_json_bytes(
            {"actor_model": "do-not-echo-this"}
        ),
    )

    with pytest.raises(ValueError, match="invalid observable evidence") as caught:
        observable_evidence_to_json(
            replace(bundle, sandbox_evidence=(injected,))
        )

    assert "do-not-echo-this" not in str(caught.value)


def test_public_projection_reapplies_runtime_firewall_to_fully_rehashed_payload(
) -> None:
    original = _complete_bundle()
    payload = {"text": "module: fruitbench"}
    visible_row = {
        "sequence": 1,
        "action": "draft_message",
        "target": "sandbox",
        "payload": payload,
    }
    sandbox_row = replace(
        original.sandbox_evidence[0],
        payload_canonical_json=canonical_json_bytes(payload),
        row_sha256=hashlib.sha256(canonical_json_bytes(visible_row)).hexdigest(),
    )
    full_log = [{**visible_row, "actor": "model"}]
    changed = replace(
        original,
        sandbox_evidence=(sandbox_row,),
        sandbox_log_sha256=hashlib.sha256(
            canonical_json_bytes(full_log)
        ).hexdigest(),
    )
    hash_input = {
        "version": changed.version,
        "status": changed.status,
        "missing_evidence": [],
        "response_sha256": changed.response_sha256,
        "probe_sha256": changed.probe_sha256,
        "sandbox_log_sha256": changed.sandbox_log_sha256,
        "segment_table_sha256": changed.segment_table_sha256,
        "event_record_sha256": changed.event_record_sha256,
    }
    changed = replace(
        changed,
        evidence_bundle_sha256=hashlib.sha256(
            canonical_json_bytes(hash_input)
        ).hexdigest(),
    )

    with pytest.raises(ValueError, match="invalid observable evidence"):
        observable_evidence_to_json(changed)
