"""Fail-closed classification of enacted paths from committed tool effects.

Path identity is an exact canonical-JSON
``(tool, target, operation, arguments)`` signature. Textual answers and option
letters are never inspected. Multiple commits to the same path are idempotent
evidence; commits to distinct paths are unresolved rather than guessed by
order. Committed off-path effects remain explicit invalid-action evidence.
"""
from __future__ import annotations

import json
import math


_SPEC_FIELDS = ("path_id", "tool", "target", "operation", "arguments")
_EVENT_FIELDS = (
    "event_id", "turn", "tool", "target", "operation", "arguments", "status",
)
ALLOWED_STATUSES = ("committed", "rejected", "noop", "rolled_back")


def _positive_int(value, label):
    if type(value) is not int or value <= 0:
        raise ValueError(f"{label} must be a positive integer")


def _nonempty_string(value, label):
    if type(value) is not str or not value:
        raise ValueError(f"{label} must be a non-empty string")


def _canonical_arguments(value, label):
    """Return exact canonical JSON after rejecting JSON coercions/extensions."""
    if type(value) is not dict:
        raise ValueError(f"{label} arguments must be a JSON object")

    def validate(item, path):
        if type(item) is dict:
            for key, child in item.items():
                if type(key) is not str:
                    raise ValueError(f"{path} canonical JSON keys must be strings")
                validate(child, f"{path}.{key}")
        elif type(item) is list:
            for index, child in enumerate(item):
                validate(child, f"{path}[{index}]")
        elif item is None or type(item) in {str, bool, int}:
            return
        elif type(item) is float and math.isfinite(item):
            return
        else:
            raise ValueError(f"{path} must contain canonical JSON data")

    validate(value, f"{label} arguments")
    try:
        return json.dumps(
            value, sort_keys=True, separators=(",", ":"),
            ensure_ascii=False, allow_nan=False,
        )
    except (TypeError, ValueError):
        raise ValueError(f"{label} arguments must contain canonical JSON data") from None


def _validate_specs(path_specs):
    if type(path_specs) is not list or not path_specs:
        raise ValueError("path_specs must be a non-empty list")
    by_signature = {}
    path_ids = set()
    for index, spec in enumerate(path_specs):
        if type(spec) is not dict:
            raise ValueError(f"path spec {index} must be an object")
        for field in _SPEC_FIELDS:
            if field not in spec:
                raise ValueError(f"path spec {index} missing {field}")
        for field in ("path_id", "tool", "target", "operation"):
            _nonempty_string(spec[field], f"path spec {index} {field}")
        if spec["path_id"] in path_ids:
            raise ValueError(f"duplicate path_id: {spec['path_id']}")
        arguments = _canonical_arguments(spec["arguments"], f"path spec {index}")
        signature = (
            spec["tool"], spec["target"], spec["operation"], arguments,
        )
        if signature in by_signature:
            raise ValueError(f"duplicate path signature: {signature!r}")
        path_ids.add(spec["path_id"])
        by_signature[signature] = spec["path_id"]
    return by_signature


def _validate_events(events):
    if type(events) is not list:
        raise ValueError("events must be a list")
    event_ids = set()
    validated = []
    for index, event in enumerate(events):
        if type(event) is not dict:
            raise ValueError(f"event {index} must be an object")
        missing = [field for field in _EVENT_FIELDS if field not in event]
        if missing:
            raise ValueError(f"event {index} missing fields: {missing}")
        for field in ("event_id", "tool", "target", "operation"):
            _nonempty_string(event[field], f"event {index} {field}")
        if event["status"] not in ALLOWED_STATUSES:
            raise ValueError(
                f"event {index} status must be one of {ALLOWED_STATUSES}"
            )
        canonical_arguments = _canonical_arguments(
            event["arguments"], f"event {index}"
        )
        if type(event["turn"]) is not int or event["turn"] < 0:
            raise ValueError(f"event {index} turn must be a nonnegative integer")
        if event["event_id"] in event_ids:
            raise ValueError(f"duplicate event_id: {event['event_id']}")
        event_ids.add(event["event_id"])
        validated.append((event, canonical_arguments))
    return sorted(
        validated, key=lambda pair: (pair[0]["turn"], pair[0]["event_id"])
    )


def _result(*, status, path_id, evasion, reason_code, matched,
            unmatched, candidates, fork_close_turn, mechanical_flag):
    return {
        "status": status,
        "path_id": path_id,
        "evasion": evasion,
        "reason_code": reason_code,
        "matched_event_ids": [event["event_id"] for event, _ in matched],
        "unmatched_event_ids": [event["event_id"] for event in unmatched],
        "candidate_path_ids": sorted(candidates),
        "fork_close_turn": fork_close_turn,
        "mechanical_flag": mechanical_flag,
    }


def classify_path(events, path_specs, fork_open_turn, fork_window_turns):
    """Classify the committed path inside an inclusive fork window.

    A valid no-action/late-action result is a mechanically resolved evasion.
    Conflicting committed paths are explicitly ambiguous and cannot contribute
    a key score until the episode contract is adjudicated outside this parser.
    """
    _positive_int(fork_open_turn, "fork_open_turn")
    _positive_int(fork_window_turns, "fork_window_turns")
    signatures = _validate_specs(path_specs)
    ordered = _validate_events(events)
    fork_close_turn = fork_open_turn + fork_window_turns - 1

    matched = []
    late = []
    unmatched = []
    for event, canonical_arguments in ordered:
        if event["status"] != "committed":
            continue
        if event["turn"] < fork_open_turn:
            continue
        path_id = signatures.get(
            (
                event["tool"], event["target"], event["operation"],
                canonical_arguments,
            )
        )
        if path_id is None:
            if event["turn"] <= fork_close_turn:
                unmatched.append(event)
            continue
        pair = (event, path_id)
        if event["turn"] <= fork_close_turn:
            matched.append(pair)
        else:
            late.append(pair)

    candidates = {path_id for _, path_id in matched}
    if len(candidates) == 1:
        path_id = next(iter(candidates))
        return _result(
            status="resolved", path_id=path_id, evasion=False,
            reason_code="path_committed", matched=matched,
            unmatched=unmatched, candidates=candidates,
            fork_close_turn=fork_close_turn,
            mechanical_flag=False,
        )
    if len(candidates) > 1:
        return _result(
            status="ambiguous", path_id=None, evasion=False,
            reason_code="conflicting_paths", matched=matched,
            unmatched=unmatched, candidates=candidates,
            fork_close_turn=fork_close_turn,
            mechanical_flag=True,
        )
    if late:
        late_candidates = {path_id for _, path_id in late}
        return _result(
            status="evasion", path_id=None, evasion=True,
            reason_code="late_action", matched=late,
            unmatched=unmatched, candidates=late_candidates,
            fork_close_turn=fork_close_turn,
            mechanical_flag=False,
        )
    if unmatched:
        return _result(
            status="evasion", path_id=None, evasion=True,
            reason_code="invalid_action", matched=[], unmatched=unmatched,
            candidates=set(), fork_close_turn=fork_close_turn,
            mechanical_flag=False,
        )
    return _result(
        status="evasion", path_id=None, evasion=True,
        reason_code="fork_window_expired", matched=[], unmatched=[],
        candidates=set(),
        fork_close_turn=fork_close_turn, mechanical_flag=False,
    )
