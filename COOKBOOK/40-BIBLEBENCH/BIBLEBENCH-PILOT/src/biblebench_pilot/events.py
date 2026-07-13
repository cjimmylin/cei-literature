"""Lossless, condition-blind custody for observable benchmark evidence."""

from __future__ import annotations

from dataclasses import dataclass, replace
import hashlib
import json
import math
import re
import unicodedata
from typing import Any, Literal

from .artifacts import assert_judge_envelope_safe
from .contracts import Json, canonical_json_bytes


__all__ = (
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


_EVIDENCE_NUMBER = r"(?:00[1-9]|0[1-9][0-9]|[1-9][0-9]{2})"
_SEGMENT_ID = re.compile(rf"S({_EVIDENCE_NUMBER})\Z")
_MAX_SOURCE_BYTES = 1024 * 1024
_MAX_SEGMENTS = 999
_EVENT_FIELDS = frozenset(
    {
        "task_correctness",
        "registered_actions",
        "registered_omissions",
        "refusal",
        "evasion",
        "uncertainty",
        "consequence_summaries",
        "evidence_ids",
    }
)
_TASK_CORRECTNESS = frozenset({"correct", "partial", "incorrect", "not_assessable"})
_UNCERTAINTY = frozenset({"none", "expressed", "material_unresolved", "not_assessable"})
_ACTION_ID = re.compile(r"[a-z][a-z0-9_]{0,63}\Z")
_PRIVATE_CONCEPTS = frozenset(
    {
        "actor",
        "model",
        "provider",
        "route",
        "cue",
        "condition",
        "module",
        "core",
        "schedule",
        "bundle",
        "episode",
        "role",
        "gold",
        "expected",
        "private",
        "lens",
        "scorer",
        "forecast",
        "canary",
        "judge",
        "rubric",
    }
)
_PRIVATE_CONCEPT_PLURALS = frozenset(
    {f"{concept}s" for concept in _PRIVATE_CONCEPTS} | {"lenses"}
)
_COMPACT_METADATA_SUFFIXES = (
    "id",
    "identity",
    "name",
    "label",
    "score",
    "result",
    "value",
    "copy",
    "type",
    "key",
    "token",
    "target",
    "route",
    "model",
    "role",
)
_COMPACT_PRIVATE_IDENTIFIER = re.compile(
    "(?:"
    + "|".join(sorted(_PRIVATE_CONCEPTS, key=len, reverse=True))
    + ")(?:"
    + "|".join(_COMPACT_METADATA_SUFFIXES)
    + r")\Z"
)
_CAMEL_BOUNDARY = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")
_NON_ALNUM = re.compile(r"[^a-z0-9]+")
_EVIDENCE_ID = re.compile(rf"([SE])({_EVIDENCE_NUMBER})\Z")
_HASH = re.compile(r"[0-9a-f]{64}\Z")
_PRIVATE_ASSIGNMENT = re.compile(
    r"(?<![a-z0-9])(?:"
    r"actors?|models?|providers?|routes?|cues?|conditions?|modules?|cores?|"
    r"schedules?|bundles?|episodes?|roles?|gold|ground[\W_]*truth|"
    r"expected(?:[\W_]*labels?)?|privates?|lens(?:es)?|scorers?|forecasts?|"
    r"actormodel|goldlabel|modulename|lensscore|forecastresult|providerroute"
    r")(?:[\W_]*(?:ids?|identit(?:y|ies)|names?|labels?|scores?|results?|"
    r"values?|copies|types?|keys?|tokens?|targets?))?[ \t]*(?::|=|\bis\b)",
    re.IGNORECASE,
)
_MAX_JSON_DEPTH = 64
_MAX_JSON_NODES = 32768
_MAX_EVENT_JSON_BYTES = 512 * 1024


@dataclass(frozen=True)
class EvidenceSegment:
    segment_id: str
    source: Literal["response", "probe"]
    start_byte: int
    end_byte: int
    content: bytes
    content_sha256: str


@dataclass(frozen=True)
class ObservableEventRecord:
    """One mechanical observation with no actor, gold, cue, or lens metadata."""

    task_correctness: Literal["correct", "partial", "incorrect", "not_assessable"]
    registered_actions: tuple[str, ...]
    registered_omissions: tuple[str, ...]
    refusal: bool
    evasion: bool
    uncertainty: Literal["none", "expressed", "material_unresolved", "not_assessable"]
    consequence_summaries: tuple[str, ...]
    evidence_ids: tuple[str, ...]


@dataclass(frozen=True)
class SandboxEvidence:
    evidence_id: str
    sequence: int
    action: str
    target: str
    payload_canonical_json: bytes
    row_sha256: str


@dataclass(frozen=True)
class FrozenObservableEvidence:
    version: Literal["event-v1"]
    status: Literal["COMPLETE", "INCOMPLETE_EVIDENCE"]
    missing_evidence: tuple[str, ...]
    segments: tuple[EvidenceSegment, ...]
    sandbox_evidence: tuple[SandboxEvidence, ...]
    events: tuple[ObservableEventRecord, ...]
    response_sha256: str | None
    probe_sha256: str | None
    sandbox_log_sha256: str | None
    segment_table_sha256: str
    event_record_sha256: str
    evidence_bundle_sha256: str


def _segment_source(
    source: bytes,
    *,
    source_kind: Literal["response", "probe"],
    first_number: int,
) -> tuple[EvidenceSegment, ...]:
    if type(source) is not bytes or len(source) > _MAX_SOURCE_BYTES:
        raise ValueError("invalid response bytes")
    try:
        source.decode("utf-8", errors="strict")
    except UnicodeDecodeError:
        raise ValueError("invalid response bytes") from None
    segments: list[EvidenceSegment] = []
    start = 0
    while start < len(source):
        number = first_number + len(segments)
        if number > _MAX_SEGMENTS:
            raise ValueError("invalid response bytes")
        newline_run = source[start] in b"\r\n"
        end = start + 1
        while end < len(source) and (source[end] in b"\r\n") == newline_run:
            end += 1
        content = source[start:end]
        segments.append(
            EvidenceSegment(
                segment_id=f"S{number:03d}",
                source=source_kind,
                start_byte=start,
                end_byte=end,
                content=content,
                content_sha256=hashlib.sha256(content).hexdigest(),
            )
        )
        start = end
    return tuple(segments)


def segment_response(source: bytes) -> tuple[EvidenceSegment, ...]:
    """Split exact UTF-8 response bytes while retaining every byte."""

    return _segment_source(source, source_kind="response", first_number=1)


def reconstruct_segments(segments: tuple[EvidenceSegment, ...]) -> bytes:
    """Validate one source's canonical segment table and reconstruct its bytes."""

    if type(segments) is not tuple:
        raise ValueError("invalid evidence segments")
    if not segments:
        return b""

    first = segments[0]
    if type(first) is not EvidenceSegment or type(first.segment_id) is not str:
        raise ValueError("invalid evidence segments")
    first_match = _SEGMENT_ID.fullmatch(first.segment_id)
    if first_match is None:
        raise ValueError("invalid evidence segments")
    expected_number = int(first_match.group(1))
    expected_offset = 0
    source = first.source
    contents: list[bytes] = []
    for segment in segments:
        match = (
            _SEGMENT_ID.fullmatch(segment.segment_id)
            if type(segment) is EvidenceSegment and type(segment.segment_id) is str
            else None
        )
        if (
            match is None
            or int(match.group(1)) != expected_number
            or segment.source != source
            or source not in {"response", "probe"}
            or type(segment.start_byte) is not int
            or type(segment.end_byte) is not int
            or segment.start_byte != expected_offset
            or segment.end_byte <= segment.start_byte
            or segment.end_byte > _MAX_SOURCE_BYTES
            or type(segment.content) is not bytes
            or segment.end_byte - segment.start_byte != len(segment.content)
            or type(segment.content_sha256) is not str
            or segment.content_sha256 != hashlib.sha256(segment.content).hexdigest()
        ):
            raise ValueError("invalid evidence segments")
        try:
            segment.content.decode("utf-8", errors="strict")
        except UnicodeDecodeError:
            raise ValueError("invalid evidence segments") from None
        contents.append(segment.content)
        expected_offset = segment.end_byte
        expected_number += 1
    reconstructed = b"".join(contents)
    try:
        canonical = _segment_source(
            reconstructed,
            source_kind=source,
            first_number=int(first_match.group(1)),
        )
    except ValueError:
        raise ValueError("invalid evidence segments") from None
    if canonical != segments:
        raise ValueError("invalid evidence segments")
    return reconstructed


def _evidence_sort_key(value: str) -> tuple[int, int]:
    match = _EVIDENCE_ID.fullmatch(value)
    if match is None:
        raise ValueError("invalid observable event")
    return (0 if match.group(1) == "S" else 1, int(match.group(2)))


def _validated_registered_actions(value: Any) -> tuple[str, ...]:
    if type(value) is not tuple or len(value) > 256:
        raise ValueError("invalid observable evidence")
    if (
        any(type(item) is not str or not _action_id_is_public(item) for item in value)
        or len(set(value)) != len(value)
        or value != tuple(sorted(value))
    ):
        raise ValueError("invalid observable evidence")
    return value


def _action_id_is_public(value: str) -> bool:
    return bool(_ACTION_ID.fullmatch(value)) and not _identifier_is_private(value)


def _normalized_policy_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value)
    return _CAMEL_BOUNDARY.sub("_", normalized).casefold()


def _identifier_is_private(value: str) -> bool:
    normalized = _normalized_policy_text(value)
    components = tuple(
        component for component in _NON_ALNUM.split(normalized) if component
    )
    return bool(
        set(components) & (_PRIVATE_CONCEPTS | _PRIVATE_CONCEPT_PLURALS)
        or "groundtruth" in components
        or "expectedlabel" in components
        or any(
            left == "ground" and right == "truth"
            for left, right in zip(components, components[1:])
        )
        or any(
            _COMPACT_PRIVATE_IDENTIFIER.fullmatch(component)
            for component in components
        )
    )


def _contains_private_assignment(value: str) -> bool:
    return bool(_PRIVATE_ASSIGNMENT.search(_normalized_policy_text(value)))


def _identifier_is_public(value: str) -> bool:
    return not _identifier_is_private(value)


def _private_key_is_forbidden(value: str) -> bool:
    return _identifier_is_private(value)


def _validated_known_evidence_ids(value: Any) -> tuple[str, ...]:
    if type(value) is not tuple or len(value) > 1998 or len(set(value)) != len(value):
        raise ValueError("invalid observable event")
    expected = {"S": 1, "E": 1}
    previous_prefix = "S"
    for item in value:
        if type(item) is not str:
            raise ValueError("invalid observable event")
        match = _EVIDENCE_ID.fullmatch(item)
        if match is None:
            raise ValueError("invalid observable event")
        prefix = match.group(1)
        if previous_prefix == "E" and prefix == "S":
            raise ValueError("invalid observable event")
        number = int(match.group(2))
        if number != expected[prefix]:
            raise ValueError("invalid observable event")
        expected[prefix] += 1
        previous_prefix = prefix
    return value


def _assert_bounded_json(
    value: Any,
    *,
    depth: int,
    active: set[int],
    nodes: list[int],
    enforce_firewall: bool,
) -> None:
    nodes[0] += 1
    if nodes[0] > _MAX_JSON_NODES:
        raise ValueError("invalid observable evidence")
    if value is None or type(value) in {bool, int}:
        return
    if type(value) is float:
        if math.isfinite(value):
            return
        raise ValueError("invalid observable evidence")
    if type(value) is str:
        if (
            any(0xD800 <= ord(character) <= 0xDFFF for character in value)
            or enforce_firewall and _contains_private_assignment(value)
        ):
            raise ValueError("invalid observable evidence")
        return
    if type(value) not in {dict, list} or depth > _MAX_JSON_DEPTH:
        raise ValueError("invalid observable evidence")
    identity = id(value)
    if identity in active:
        raise ValueError("invalid observable evidence")
    active.add(identity)
    try:
        if type(value) is dict:
            for key, child in value.items():
                if type(key) is not str or (
                    enforce_firewall and _private_key_is_forbidden(key)
                ):
                    raise ValueError("invalid observable evidence")
                _assert_bounded_json(
                    key,
                    depth=depth + 1,
                    active=active,
                    nodes=nodes,
                    enforce_firewall=enforce_firewall,
                )
                _assert_bounded_json(
                    child,
                    depth=depth + 1,
                    active=active,
                    nodes=nodes,
                    enforce_firewall=enforce_firewall,
                )
        else:
            for child in value:
                _assert_bounded_json(
                    child,
                    depth=depth + 1,
                    active=active,
                    nodes=nodes,
                    enforce_firewall=enforce_firewall,
                )
    finally:
        active.remove(identity)


def _bounded_canonical_json_bytes(
    value: Any,
    *,
    max_bytes: int,
    enforce_firewall: bool = True,
) -> bytes:
    _assert_bounded_json(
        value,
        depth=0,
        active=set(),
        nodes=[0],
        enforce_firewall=enforce_firewall,
    )
    result = canonical_json_bytes(value)
    if len(result) > max_bytes:
        raise ValueError("invalid observable evidence")
    return result


def _canonical_string_list(
    value: Any,
    *,
    action_ids: bool = False,
    require_sorted: bool = True,
    max_items: int,
    max_utf8_bytes: int | None = None,
) -> tuple[str, ...]:
    if type(value) is not list:
        raise ValueError("invalid observable event")
    result = tuple(value)
    if len(result) > max_items or any(
        type(item) is not str or not item for item in result
    ):
        raise ValueError("invalid observable event")
    if max_utf8_bytes is not None:
        try:
            if any(len(item.encode("utf-8")) > max_utf8_bytes for item in result):
                raise ValueError("invalid observable event")
        except UnicodeEncodeError:
            raise ValueError("invalid observable event") from None
    if action_ids and any(not _action_id_is_public(item) for item in result):
        raise ValueError("invalid observable event")
    if len(set(result)) != len(result) or (
        require_sorted and result != tuple(sorted(result))
    ):
        raise ValueError("invalid observable event")
    return result


def validate_observable_event_record(
    raw: Any,
    *,
    known_evidence_ids: tuple[str, ...],
    registered_action_ids: tuple[str, ...],
) -> ObservableEventRecord:
    try:
        if type(raw) is ObservableEventRecord:
            raw = _event_projection(raw)
        if type(raw) is not dict or set(raw) != _EVENT_FIELDS:
            raise ValueError
        if (
            type(known_evidence_ids) is not tuple
            or type(registered_action_ids) is not tuple
        ):
            raise ValueError
        registered = _validated_registered_actions(registered_action_ids)
        known = _validated_known_evidence_ids(known_evidence_ids)

        task_correctness = raw["task_correctness"]
        uncertainty = raw["uncertainty"]
        if (
            type(task_correctness) is not str
            or task_correctness not in _TASK_CORRECTNESS
            or type(uncertainty) is not str
            or uncertainty not in _UNCERTAINTY
            or type(raw["refusal"]) is not bool
            or type(raw["evasion"]) is not bool
        ):
            raise ValueError
        actions = _canonical_string_list(
            raw["registered_actions"], action_ids=True, max_items=128
        )
        omissions = _canonical_string_list(
            raw["registered_omissions"], action_ids=True, max_items=128
        )
        if (
            not set(actions).issubset(registered)
            or not set(omissions).issubset(registered)
            or set(actions) & set(omissions)
        ):
            raise ValueError
        summaries = _canonical_string_list(
            raw["consequence_summaries"],
            require_sorted=False,
            max_items=32,
            max_utf8_bytes=1024,
        )
        if any(_contains_private_assignment(summary) for summary in summaries):
            raise ValueError
        evidence_ids = _canonical_string_list(
            raw["evidence_ids"], require_sorted=False, max_items=256
        )
        if (
            not evidence_ids
            or tuple(sorted(evidence_ids, key=_evidence_sort_key)) != evidence_ids
            or not set(evidence_ids).issubset(known)
        ):
            raise ValueError
        if (
            task_correctness == "not_assessable"
            and not actions
            and not omissions
            and not raw["refusal"]
            and not raw["evasion"]
            and uncertainty in {"none", "not_assessable"}
            and not summaries
        ):
            raise ValueError

        record = ObservableEventRecord(
            task_correctness=task_correctness,
            registered_actions=actions,
            registered_omissions=omissions,
            refusal=raw["refusal"],
            evasion=raw["evasion"],
            uncertainty=uncertainty,
            consequence_summaries=summaries,
            evidence_ids=evidence_ids,
        )
        assert_judge_envelope_safe(
            {
                "episode_token": "opaque-event",
                "rubric_version": "event-v1",
                "events": [_event_projection(record)],
            }
        )
        return record
    except (KeyError, TypeError, ValueError):
        raise ValueError("invalid observable event") from None


def _event_projection(record: ObservableEventRecord) -> dict[str, Json]:
    if type(record) is not ObservableEventRecord:
        raise ValueError("invalid observable event")
    return {
        "task_correctness": record.task_correctness,
        "registered_actions": list(record.registered_actions),
        "registered_omissions": list(record.registered_omissions),
        "refusal": record.refusal,
        "evasion": record.evasion,
        "uncertainty": record.uncertainty,
        "consequence_summaries": list(record.consequence_summaries),
        "evidence_ids": list(record.evidence_ids),
    }


def _structurally_valid_events(
    records: tuple[ObservableEventRecord, ...],
) -> tuple[tuple[ObservableEventRecord, ...], bytes]:
    if type(records) is not tuple or len(records) > 256:
        raise ValueError("invalid observable events")
    try:
        all_ids = [
            evidence_id
            for record in records
            for evidence_id in record.evidence_ids
        ]
        max_ids = {"S": 0, "E": 0}
        for evidence_id in all_ids:
            if type(evidence_id) is not str:
                raise ValueError
            match = _EVIDENCE_ID.fullmatch(evidence_id)
            if match is None:
                raise ValueError
            max_ids[match.group(1)] = max(
                max_ids[match.group(1)], int(match.group(2))
            )
        known_ids = tuple(
            [f"S{number:03d}" for number in range(1, max_ids["S"] + 1)]
            + [f"E{number:03d}" for number in range(1, max_ids["E"] + 1)]
        )
        registered_actions = tuple(
            sorted(
                {
                    action
                    for record in records
                    for action in (
                        *record.registered_actions,
                        *record.registered_omissions,
                    )
                }
            )
        )
        checked = tuple(
            validate_observable_event_record(
                _event_projection(record),
                known_evidence_ids=known_ids,
                registered_action_ids=registered_actions,
            )
            for record in records
        )
        if checked != records:
            raise ValueError
        rows = [_event_projection(record) for record in checked]
        serialized = canonical_json_bytes(rows)
        if len(serialized) > _MAX_EVENT_JSON_BYTES:
            raise ValueError
        return checked, serialized
    except (AttributeError, TypeError, ValueError):
        raise ValueError("invalid observable events") from None


def observable_event_to_json(record: ObservableEventRecord) -> dict[str, Json]:
    try:
        checked, _ = _structurally_valid_events((record,))
        return _event_projection(checked[0])
    except (IndexError, TypeError, ValueError):
        raise ValueError("invalid observable event") from None


def observable_events_sha256(records: tuple[ObservableEventRecord, ...]) -> str:
    try:
        _, serialized = _structurally_valid_events(records)
        return hashlib.sha256(serialized).hexdigest()
    except (TypeError, ValueError):
        raise ValueError("invalid observable events") from None


def _segment_to_json(segment: EvidenceSegment) -> dict[str, Json]:
    try:
        text = segment.content.decode("utf-8", errors="strict")
    except (AttributeError, UnicodeDecodeError):
        raise ValueError("invalid observable evidence") from None
    return {
        "segment_id": segment.segment_id,
        "source": segment.source,
        "start_byte": segment.start_byte,
        "end_byte": segment.end_byte,
        "text": text,
        "content_sha256": segment.content_sha256,
    }


def _sandbox_evidence_to_json(row: SandboxEvidence) -> dict[str, Json]:
    if type(row) is not SandboxEvidence:
        raise ValueError("invalid observable evidence")
    try:
        payload = json.loads(row.payload_canonical_json)
    except (TypeError, UnicodeDecodeError, json.JSONDecodeError):
        raise ValueError("invalid observable evidence") from None
    if type(payload) is not dict:
        raise ValueError("invalid observable evidence")
    return {
        "evidence_id": row.evidence_id,
        "sequence": row.sequence,
        "action": row.action,
        "target": row.target,
        "payload": payload,
        "row_sha256": row.row_sha256,
    }


def _freeze_sandbox_log(
    sandbox_log: tuple[Any, ...],
    *,
    registered_action_ids: tuple[str, ...],
) -> tuple[tuple[SandboxEvidence, ...], list[dict[str, Json]]]:
    from .contracts import SandboxEvent

    if type(sandbox_log) is not tuple or len(sandbox_log) > 999:
        raise ValueError("invalid observable evidence")
    evidence: list[SandboxEvidence] = []
    full_rows: list[dict[str, Json]] = []
    total_bytes = 0
    for expected_sequence, event in enumerate(sandbox_log, start=1):
        if (
            type(event) is not SandboxEvent
            or type(event.sequence) is not int
            or event.sequence != expected_sequence
            or type(event.action) is not str
            or not _action_id_is_public(event.action)
            or event.action not in registered_action_ids
            or event.actor != "model"
            or type(event.target) is not str
            or not event.target
            or not _identifier_is_public(event.target)
            or len(event.target.encode("utf-8", errors="strict")) > 256
            or type(event.payload) is not dict
        ):
            raise ValueError("invalid observable evidence")
        payload_bytes = _bounded_canonical_json_bytes(
            event.payload, max_bytes=_MAX_SOURCE_BYTES
        )
        total_bytes += len(payload_bytes)
        if total_bytes > _MAX_SOURCE_BYTES:
            raise ValueError("invalid observable evidence")
        payload = json.loads(payload_bytes)
        visible_base: dict[str, Json] = {
            "sequence": event.sequence,
            "action": event.action,
            "target": event.target,
            "payload": payload,
        }
        row_sha256 = hashlib.sha256(canonical_json_bytes(visible_base)).hexdigest()
        frozen = SandboxEvidence(
            evidence_id=f"E{expected_sequence:03d}",
            sequence=event.sequence,
            action=event.action,
            target=event.target,
            payload_canonical_json=payload_bytes,
            row_sha256=row_sha256,
        )
        assert_judge_envelope_safe(
            {
                "episode_token": "opaque-event",
                "rubric_version": "event-v1",
                "events": [_sandbox_evidence_to_json(frozen)],
            }
        )
        evidence.append(frozen)
        full_rows.append(
            {
                "sequence": event.sequence,
                "action": event.action,
                "actor": "model",
                "target": event.target,
                "payload": payload,
            }
        )
    return tuple(evidence), full_rows


def _bundle_hash_payload(bundle: FrozenObservableEvidence) -> dict[str, Json]:
    return {
        "version": bundle.version,
        "status": bundle.status,
        "missing_evidence": list(bundle.missing_evidence),
        "response_sha256": bundle.response_sha256,
        "probe_sha256": bundle.probe_sha256,
        "sandbox_log_sha256": bundle.sandbox_log_sha256,
        "segment_table_sha256": bundle.segment_table_sha256,
        "event_record_sha256": bundle.event_record_sha256,
    }


def freeze_observable_evidence(
    response_bytes: bytes | None,
    probe_bytes: bytes | None,
    sandbox_log: tuple[Any, ...] | None,
    event_rows: list[dict[str, Json]] | None,
    *,
    registered_action_ids: tuple[str, ...],
) -> FrozenObservableEvidence:
    """Freeze retained sources and located mechanical observations as one bundle."""

    try:
        registered_action_ids = _validated_registered_actions(
            registered_action_ids
        )
        missing: list[str] = []
        response_segments: tuple[EvidenceSegment, ...] = ()
        probe_segments: tuple[EvidenceSegment, ...] = ()
        if response_bytes is None:
            missing.append("response")
            response_sha256 = None
        else:
            response_segments = _segment_source(
                response_bytes, source_kind="response", first_number=1
            )
            response_sha256 = hashlib.sha256(response_bytes).hexdigest()
        if probe_bytes is None:
            missing.append("probe")
            probe_sha256 = None
        else:
            probe_segments = _segment_source(
                probe_bytes,
                source_kind="probe",
                first_number=len(response_segments) + 1,
            )
            probe_sha256 = hashlib.sha256(probe_bytes).hexdigest()
        segments = (*response_segments, *probe_segments)

        if sandbox_log is None:
            missing.append("sandbox_log")
            sandbox_evidence: tuple[SandboxEvidence, ...] = ()
            sandbox_log_sha256 = None
        else:
            sandbox_evidence, full_sandbox_rows = _freeze_sandbox_log(
                sandbox_log,
                registered_action_ids=registered_action_ids,
            )
            sandbox_log_sha256 = hashlib.sha256(
                _bounded_canonical_json_bytes(
                    full_sandbox_rows,
                    max_bytes=_MAX_SOURCE_BYTES,
                    enforce_firewall=False,
                )
            ).hexdigest()

        if event_rows is None or event_rows == []:
            if event_rows is not None and type(event_rows) is not list:
                raise ValueError
            missing.append("observable_events")
            events: tuple[ObservableEventRecord, ...] = ()
        else:
            if type(event_rows) is not list or len(event_rows) > 256:
                raise ValueError
            known_ids = tuple(
                [segment.segment_id for segment in segments]
                + [row.evidence_id for row in sandbox_evidence]
            )
            events = tuple(
                validate_observable_event_record(
                    row,
                    known_evidence_ids=known_ids,
                    registered_action_ids=registered_action_ids,
                )
                for row in event_rows
            )

        segment_rows = [_segment_to_json(segment) for segment in segments]
        segment_table_sha256 = hashlib.sha256(
            canonical_json_bytes(segment_rows)
        ).hexdigest()
        canonical_event_bytes = canonical_json_bytes(
            [observable_event_to_json(event) for event in events]
        )
        if len(canonical_event_bytes) > _MAX_EVENT_JSON_BYTES:
            raise ValueError
        event_record_sha256 = hashlib.sha256(canonical_event_bytes).hexdigest()
        status = "COMPLETE" if not missing else "INCOMPLETE_EVIDENCE"
        provisional = FrozenObservableEvidence(
            version="event-v1",
            status=status,
            missing_evidence=tuple(missing),
            segments=tuple(segments),
            sandbox_evidence=sandbox_evidence,
            events=events,
            response_sha256=response_sha256,
            probe_sha256=probe_sha256,
            sandbox_log_sha256=sandbox_log_sha256,
            segment_table_sha256=segment_table_sha256,
            event_record_sha256=event_record_sha256,
            evidence_bundle_sha256="",
        )
        evidence_bundle_sha256 = hashlib.sha256(
            canonical_json_bytes(_bundle_hash_payload(provisional))
        ).hexdigest()
        return replace(
            provisional,
            evidence_bundle_sha256=evidence_bundle_sha256,
        )
    except (AttributeError, KeyError, TypeError, ValueError):
        raise ValueError("invalid observable evidence") from None


def observable_evidence_to_json(bundle: FrozenObservableEvidence) -> dict[str, Json]:
    """Validate and project a frozen bundle to its closed public JSON contract."""

    if type(bundle) is not FrozenObservableEvidence:
        raise ValueError("invalid observable evidence")
    try:
        if (
            bundle.version != "event-v1"
            or type(bundle.missing_evidence) is not tuple
            or type(bundle.segments) is not tuple
            or type(bundle.sandbox_evidence) is not tuple
            or type(bundle.events) is not tuple
        ):
            raise ValueError

        response_segments = tuple(
            segment for segment in bundle.segments if segment.source == "response"
        )
        probe_segments = tuple(
            segment for segment in bundle.segments if segment.source == "probe"
        )
        if (*response_segments, *probe_segments) != bundle.segments:
            raise ValueError
        for expected_number, segment in enumerate(bundle.segments, start=1):
            if (
                type(segment) is not EvidenceSegment
                or segment.segment_id != f"S{expected_number:03d}"
            ):
                raise ValueError
        response = reconstruct_segments(response_segments)
        probe = reconstruct_segments(probe_segments)
        segment_rows = [_segment_to_json(segment) for segment in bundle.segments]

        sandbox_rows: list[dict[str, Json]] = []
        sandbox_public_rows: list[dict[str, Json]] = []
        if len(bundle.sandbox_evidence) > 999:
            raise ValueError
        for expected_sequence, row in enumerate(bundle.sandbox_evidence, start=1):
            public_row = _sandbox_evidence_to_json(row)
            if (
                row.evidence_id != f"E{expected_sequence:03d}"
                or type(row.sequence) is not int
                or row.sequence != expected_sequence
                or type(row.action) is not str
                or not _action_id_is_public(row.action)
                or type(row.target) is not str
                or not row.target
                or not _identifier_is_public(row.target)
                or len(row.target.encode("utf-8", errors="strict")) > 256
                or _bounded_canonical_json_bytes(
                    public_row["payload"], max_bytes=_MAX_SOURCE_BYTES
                )
                != row.payload_canonical_json
            ):
                raise ValueError
            visible_base: dict[str, Json] = {
                "sequence": row.sequence,
                "action": row.action,
                "target": row.target,
                "payload": public_row["payload"],
            }
            if row.row_sha256 != hashlib.sha256(
                canonical_json_bytes(visible_base)
            ).hexdigest():
                raise ValueError
            assert_judge_envelope_safe(
                {
                    "episode_token": "opaque-event",
                    "rubric_version": "event-v1",
                    "events": [public_row],
                }
            )
            sandbox_public_rows.append(public_row)
            sandbox_rows.append(
                {
                    "sequence": row.sequence,
                    "action": row.action,
                    "actor": "model",
                    "target": row.target,
                    "payload": public_row["payload"],
                }
            )

        known_ids = tuple(
            [segment.segment_id for segment in bundle.segments]
            + [row.evidence_id for row in bundle.sandbox_evidence]
        )
        inferred_actions = tuple(
            sorted(
                {
                    *(row.action for row in bundle.sandbox_evidence),
                    *(
                        action
                        for event in bundle.events
                        for action in (
                            *event.registered_actions,
                            *event.registered_omissions,
                        )
                    ),
                }
            )
        )
        if len(bundle.events) > 256:
            raise ValueError
        checked_events = tuple(
            validate_observable_event_record(
                observable_event_to_json(event),
                known_evidence_ids=known_ids,
                registered_action_ids=inferred_actions,
            )
            for event in bundle.events
        )
        if checked_events != bundle.events:
            raise ValueError
        event_rows = [observable_event_to_json(event) for event in checked_events]
        event_bytes = canonical_json_bytes(event_rows)
        if len(event_bytes) > _MAX_EVENT_JSON_BYTES:
            raise ValueError

        expected_missing: list[str] = []
        if bundle.response_sha256 is None:
            expected_missing.append("response")
            if response_segments:
                raise ValueError
        elif (
            _HASH.fullmatch(bundle.response_sha256) is None
            or hashlib.sha256(response).hexdigest() != bundle.response_sha256
        ):
            raise ValueError
        if bundle.probe_sha256 is None:
            expected_missing.append("probe")
            if probe_segments:
                raise ValueError
        elif (
            _HASH.fullmatch(bundle.probe_sha256) is None
            or hashlib.sha256(probe).hexdigest() != bundle.probe_sha256
        ):
            raise ValueError
        if bundle.sandbox_log_sha256 is None:
            expected_missing.append("sandbox_log")
            if sandbox_rows:
                raise ValueError
        elif (
            _HASH.fullmatch(bundle.sandbox_log_sha256) is None
            or hashlib.sha256(
                _bounded_canonical_json_bytes(
                    sandbox_rows,
                    max_bytes=_MAX_SOURCE_BYTES,
                    enforce_firewall=False,
                )
            ).hexdigest()
            != bundle.sandbox_log_sha256
        ):
            raise ValueError
        if not checked_events:
            expected_missing.append("observable_events")

        expected_status = "COMPLETE" if not expected_missing else "INCOMPLETE_EVIDENCE"
        if (
            bundle.status != expected_status
            or bundle.missing_evidence != tuple(expected_missing)
            or _HASH.fullmatch(bundle.segment_table_sha256) is None
            or bundle.segment_table_sha256
            != hashlib.sha256(canonical_json_bytes(segment_rows)).hexdigest()
            or _HASH.fullmatch(bundle.event_record_sha256) is None
            or bundle.event_record_sha256 != hashlib.sha256(event_bytes).hexdigest()
            or _HASH.fullmatch(bundle.evidence_bundle_sha256) is None
            or bundle.evidence_bundle_sha256
            != hashlib.sha256(
                canonical_json_bytes(_bundle_hash_payload(bundle))
            ).hexdigest()
        ):
            raise ValueError
        result = {
            "version": bundle.version,
            "status": bundle.status,
            "missing_evidence": list(bundle.missing_evidence),
            "segments": segment_rows,
            "sandbox_evidence": sandbox_public_rows,
            "events": event_rows,
            "response_sha256": bundle.response_sha256,
            "probe_sha256": bundle.probe_sha256,
            "sandbox_log_sha256": bundle.sandbox_log_sha256,
            "segment_table_sha256": bundle.segment_table_sha256,
            "event_record_sha256": bundle.event_record_sha256,
            "evidence_bundle_sha256": bundle.evidence_bundle_sha256,
        }
        canonical_json_bytes(result)
        return result
    except (AttributeError, KeyError, TypeError, UnicodeError, ValueError):
        raise ValueError("invalid observable evidence") from None


def validate_observable_evidence(
    bundle: FrozenObservableEvidence,
    *,
    response_bytes: bytes | None,
    probe_bytes: bytes | None,
    sandbox_log: tuple[Any, ...] | None,
    registered_action_ids: tuple[str, ...],
    require_complete: bool = False,
) -> FrozenObservableEvidence:
    """Rebuild a bundle from retained exact sources and reject any drift."""

    if type(bundle) is not FrozenObservableEvidence or type(require_complete) is not bool:
        raise ValueError("invalid observable evidence")
    try:
        event_rows = [observable_event_to_json(event) for event in bundle.events]
        rebuilt = freeze_observable_evidence(
            response_bytes,
            probe_bytes,
            sandbox_log,
            event_rows,
            registered_action_ids=registered_action_ids,
        )
    except (AttributeError, KeyError, TypeError, ValueError):
        raise ValueError("invalid observable evidence") from None
    if bundle != rebuilt:
        raise ValueError("invalid observable evidence")
    if require_complete and bundle.status != "COMPLETE":
        raise ValueError("incomplete observable evidence")
    return rebuilt
