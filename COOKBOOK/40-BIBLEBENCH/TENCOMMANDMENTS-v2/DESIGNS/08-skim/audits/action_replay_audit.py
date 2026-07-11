#!/usr/bin/env python3
"""Audit-local executable-option replay over the shared custody runtime."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
BENCH_ROOT = ROOT.parents[2]
for import_root in (ROOT, BENCH_ROOT):
    if str(import_root) not in sys.path:
        sys.path.insert(0, str(import_root))

from audits.schema_audit import (  # noqa: E402
    add_common_cli_arguments,
    load_audit_inputs,
    make_finding,
    report_exit_code,
    write_reports,
)
from itembank.core_catalog import (  # noqa: E402
    RECOGNITION_TOOL_HANDLER,
    SKIM_TOOL_RECIPES,
)
from skim_hashing import canonical_sha256 as skim_canonical_sha256  # noqa: E402
from TENCOMMANDMENTS.harness.custody_stack import (  # noqa: E402
    EpisodeState,
    Runtime,
    SandboxViolation,
    TerminalRuntimeError,
    ToolRegistry,
    ToolResult,
    Transition,
    ZERO_EVENT_SHA256,
    canonical_json,
    canonical_json_bytes,
    state_sha256,
    thaw_json,
    verify_chain,
)


_STATE_FIELDS = frozenset(
    {
        "schema_version",
        "runtime_request_id",
        "logical_record_id",
        "expected_tool",
        "request_kind",
        "registered_options",
        "commit",
    }
)
_OUTCOME_NAMES = (
    "DIVERSION",
    "FIDELITY",
    "NONHEADLINE",
    "RECOGNITION_CORRECT",
    "RECOGNITION_INCORRECT",
    "STEWARDSHIP_FAIL",
    "STEWARDSHIP_PASS",
)
_EXPECTED_OUTCOMES = {
    "DIVERSION": 384,
    "FIDELITY": 512,
    "NONHEADLINE": 128,
    "RECOGNITION_CORRECT": 160,
    "RECOGNITION_INCORRECT": 160,
    "STEWARDSHIP_FAIL": 128,
    "STEWARDSHIP_PASS": 128,
}
_PROBE_NAMES = (
    "arbitrary_gold",
    "arbitrary_state",
    "extra_argument",
    "unknown_option",
)
_EXPECTED_PROBES = {name: 800 for name in _PROBE_NAMES}
_GENERATOR_VERSION = "skim-generator-v1"
_ACTION_ARGUMENT_SCHEMA = {
    "option_id": str,
    "decision_record": {
        "material_basis": str,
        "mandate_fit": str,
    },
}
_RECOGNITION_ARGUMENT_SCHEMA = {"option_id": str}
_DECISION_RECORD = {
    "material_basis": "audit replay of the registered option",
    "mandate_fit": "audit-only deterministic fixture",
}


def _empty_stats(records_checked=0, requests_checked=0):
    return {
        "records_checked": records_checked,
        "requests_checked": requests_checked,
        "replay_count": 0,
        "event_chains_verified": 0,
        "resumes_verified": 0,
        "outcome_counts": {name: 0 for name in _OUTCOME_NAMES},
        "rejected_mutation_probes": {name: 0 for name in _PROBE_NAMES},
        "mutation_probe_state_changes": 0,
    }


def _hard(findings, code, message, *, record_id=None, details=None):
    findings.append(
        make_finding(
            audit="action_replay",
            code=code,
            severity="hard",
            message=message,
            record_id=record_id,
            details=details,
        )
    )


def _sorted_findings(findings):
    return sorted(
        findings,
        key=lambda finding: (
            0 if finding.get("severity") == "hard" else 1,
            str(finding.get("code", "")),
            str(finding.get("record_id", "")),
            str(finding.get("message", "")),
            json.dumps(
                finding.get("details", {}),
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
                allow_nan=False,
            ),
        ),
    )


def _validate_handler_state(data, tool_name, recognition):
    if type(data) is not dict or set(data) != _STATE_FIELDS:
        raise SandboxViolation("audit replay state schema is invalid")
    if (
        data["schema_version"] != 1
        or type(data["runtime_request_id"]) is not str
        or not data["runtime_request_id"]
        or type(data["logical_record_id"]) is not str
        or not data["logical_record_id"]
        or data["expected_tool"] != tool_name
        or data["request_kind"]
        != ("recognition" if recognition else "action")
        or type(data["registered_options"]) is not dict
        or not data["registered_options"]
        or data["commit"] is not None
    ):
        raise SandboxViolation("audit replay state binding is invalid")


def _handler_for(tool_name, recognition):
    def handler(state, arguments):
        data = state.to_dict()
        _validate_handler_state(data, tool_name, recognition)
        option_id = arguments["option_id"]
        registered = data["registered_options"]
        if option_id not in registered:
            raise SandboxViolation("option is not registered for this request")
        commit = {
            "tool": tool_name,
            "option_id": option_id,
            "resolved_option": registered[option_id],
        }
        if not recognition:
            commit["decision_record"] = thaw_json(arguments["decision_record"])
        data["commit"] = commit
        return Transition(
            EpisodeState(data),
            ToolResult({"ok": True, "option_id": option_id}, terminal=True),
        )

    return handler


def _build_audit_registry():
    registry = ToolRegistry()
    for tool_name, recipe in SKIM_TOOL_RECIPES.items():
        recognition = tool_name == RECOGNITION_TOOL_HANDLER
        expected_kind = (
            "terminal_recognition_commit"
            if recognition
            else "terminal_option_commit"
        )
        expected_arguments = (
            ("option_id",)
            if recognition
            else ("option_id", "decision_record")
        )
        if (
            recipe.handler != tool_name
            or recipe.recipe_kind != expected_kind
            or recipe.required_arguments != expected_arguments
            or recipe.terminal is not True
        ):
            raise ValueError("SKIM tool recipe differs from the frozen contract")
        registry.register(
            tool_name,
            (
                _RECOGNITION_ARGUMENT_SCHEMA
                if recognition
                else _ACTION_ARGUMENT_SCHEMA
            ),
            _handler_for(tool_name, recognition),
        )
    if set(registry.tool_names) != set(SKIM_TOOL_RECIPES):
        raise ValueError("audit registry does not contain all frozen SKIM tools")
    return registry


def _option_ids(request):
    options = request.get("options") if type(request) is dict else None
    if type(options) is not list or len(options) != 2:
        raise ValueError("request must expose exactly two registered options")
    result = []
    for option in options:
        if type(option) is not dict:
            raise ValueError("request option must be an exact object")
        option_id = option.get("option_id")
        if type(option_id) is not str or not option_id:
            raise ValueError("request option ID must be a nonblank exact string")
        result.append(option_id)
    if len(set(result)) != 2:
        raise ValueError("request option IDs must be unique")
    return tuple(result)


def _request_template_sha256(public_row, request):
    return skim_canonical_sha256(
        {
            "generator_version": _GENERATOR_VERSION,
            "core_id": public_row["core_id"],
            "record_type": public_row["record_type"],
            "request_kind": request["request_kind"],
            "traceability": request["traceability"],
            "prompt": request["prompt"],
            "structured_state": request["structured_state"],
            "tool_schema": request["tool_schema"],
            "options": request["options"],
            "response_schema": request["response_schema"],
        }
    )


def _expected_request_order(public):
    ordered = []
    seen_request_ids = set()
    for public_index, public_row in enumerate(public):
        if type(public_row) is not dict:
            raise ValueError(
                "public row %d is not an exact object" % public_index
            )
        requests = public_row.get("requests")
        if type(requests) is not list:
            raise ValueError("public row has no exact request list")
        for request in requests:
            if type(request) is not dict:
                raise ValueError("public request is not an exact object")
            request_id = request.get("request_id")
            if (
                type(request_id) is not str
                or not request_id
                or request_id in seen_request_ids
            ):
                raise ValueError("public request IDs are not globally unique")
            seen_request_ids.add(request_id)
            ordered.append((public_row, request))
    return tuple(ordered)


def _runtime_row_sha256(runtime_row):
    payload = dict(runtime_row)
    supplied = payload.pop("runtime_row_sha256", None)
    return supplied, skim_canonical_sha256(payload)


def _bind_provenance(runtime_row, public_row, request, private_gold):
    """Return independently computed event hashes or mismatch reasons."""

    reasons = []
    public_sha256 = skim_canonical_sha256(public_row)
    template_sha256 = _request_template_sha256(public_row, request)
    supplied_row_sha256, computed_row_sha256 = _runtime_row_sha256(runtime_row)
    nested_request = runtime_row.get("request_template")

    expected_values = {
        "runtime_request_id": request.get("request_id"),
        "source_request_id": request.get("request_id"),
        "source_logical_record_id": public_row.get("logical_record_id"),
        "source_core_id": public_row.get("core_id"),
        "source_record_type": public_row.get("record_type"),
        "source_request_kind": request.get("request_kind"),
        "source_traceability": request.get("traceability"),
        "source_public_record_sha256": public_sha256,
        "source_request_template_sha256": template_sha256,
    }
    for field, expected in expected_values.items():
        if runtime_row.get(field) != expected:
            reasons.append(field)
    if (
        type(nested_request) is not dict
        or canonical_json_bytes(nested_request) != canonical_json_bytes(request)
    ):
        reasons.append("request_template")
    if request.get("template_sha256") != template_sha256:
        reasons.append("public_request_template_sha256")
    if supplied_row_sha256 != computed_row_sha256:
        reasons.append("runtime_row_sha256")
    if (
        private_gold.get("logical_record_id")
        != public_row.get("logical_record_id")
        or private_gold.get("core_id") != public_row.get("core_id")
        or private_gold.get("record_type") != public_row.get("record_type")
        or private_gold.get("public_record_sha256") != public_sha256
    ):
        reasons.append("private_public_binding")
    return {
        "public_sha256": public_sha256,
        "template_sha256": template_sha256,
        "reasons": tuple(sorted(set(reasons))),
    }


def _private_initial_state(runtime_row, private_gold, request):
    request_kind = request.get("request_kind")
    option_ids = _option_ids(request)
    if request_kind == "action":
        action_map = private_gold.get("mechanical_action_map")
        if type(action_map) is not dict or set(action_map) != set(option_ids):
            raise ValueError("private action map does not match request options")
        registered = {option_id: action_map[option_id] for option_id in option_ids}
    elif request_kind == "recognition":
        answer = private_gold.get("recognition_answer_id")
        if type(answer) is not str or answer not in option_ids:
            raise ValueError("private recognition answer is not a request option")
        if private_gold.get("mechanical_action_map") != {}:
            raise ValueError("recognition request carries a mechanical action map")
        registered = {
            option_id: {"recognition_correct": option_id == answer}
            for option_id in option_ids
        }
    else:
        raise ValueError("request kind is neither action nor recognition")

    tool_schema = request.get("tool_schema")
    tool_name = tool_schema.get("name") if type(tool_schema) is dict else None
    if type(tool_name) is not str or not tool_name:
        raise ValueError("request lacks a declared tool")
    return EpisodeState(
        {
            "schema_version": 1,
            "runtime_request_id": runtime_row["runtime_request_id"],
            "logical_record_id": runtime_row["source_logical_record_id"],
            "expected_tool": tool_name,
            "request_kind": request_kind,
            "registered_options": registered,
            "commit": None,
        }
    )


def _action_payload(tool_name, request_kind, option_id, extra=None):
    arguments = {"option_id": option_id}
    if request_kind == "action":
        arguments["decision_record"] = dict(_DECISION_RECORD)
    if extra:
        arguments.update(extra)
    return {"kind": "act", "tool": tool_name, "arguments": arguments}


def _metadata(runtime_row, request, episode_id, provenance):
    prompt = request.get("prompt")
    if type(prompt) is not str:
        raise ValueError("request prompt must be an exact string")
    return {
        "episode_id": episode_id,
        "logical_id": runtime_row["source_logical_record_id"],
        "prompt_sha256": sha256(prompt.encode("utf-8")).hexdigest(),
        "item_sha256": provenance["public_sha256"],
        "template_sha256": provenance["template_sha256"],
    }


def _expected_state(initial_state, tool_name, request_kind, option_id):
    data = initial_state.to_dict()
    commit = {
        "tool": tool_name,
        "option_id": option_id,
        "resolved_option": data["registered_options"][option_id],
    }
    if request_kind == "action":
        commit["decision_record"] = dict(_DECISION_RECORD)
    data["commit"] = commit
    return EpisodeState(data)


def _verify_event(
    runtime,
    initial_state,
    expected_state,
    action_payload,
    raw_response,
    expected_result,
    metadata,
):
    events = runtime.events
    if len(events) != 1 or not verify_chain(events):
        raise ValueError("runtime did not produce one valid custody event")
    event = events[0]
    if (
        event.event_index != 0
        or event.previous_event_sha256 != ZERO_EVENT_SHA256
        or event.state_before_sha256 != state_sha256(initial_state)
        or event.state_after_sha256 != state_sha256(expected_state)
        or canonical_json_bytes(event.action.to_dict())
        != canonical_json_bytes(action_payload)
        or canonical_json_bytes(event.tool_result.to_dict())
        != canonical_json_bytes(expected_result.to_dict())
        or event.raw_response_sha256
        != sha256(raw_response.encode("utf-8")).hexdigest()
        or event.episode_id != metadata["episode_id"]
        or event.logical_id != metadata["logical_id"]
        or event.prompt_sha256 != metadata["prompt_sha256"]
        or event.item_sha256 != metadata["item_sha256"]
        or event.template_sha256 != metadata["template_sha256"]
        or event.terminal is not True
        or runtime.terminal is not True
        or state_sha256(runtime.state) != state_sha256(expected_state)
    ):
        raise ValueError("custody event differs from the exact replay transition")
    if set(event.tool_result.to_dict()["data"]) != {"ok", "option_id"}:
        raise ValueError("tool result exposed nonpublic resolved option material")
    return event


def _outcome(private_gold, request_kind, option_id, expected_state):
    resolved = expected_state.to_dict()["commit"]["resolved_option"]
    if request_kind == "recognition":
        expected = option_id == private_gold["recognition_answer_id"]
        if resolved != {"recognition_correct": expected}:
            raise ValueError("recognition resolution differs from private gold")
        return "RECOGNITION_CORRECT" if expected else "RECOGNITION_INCORRECT"
    expected = private_gold["mechanical_action_map"][option_id]
    if canonical_json_bytes(resolved) != canonical_json_bytes(expected):
        raise ValueError("resolved mechanical option differs from private gold")
    classification = expected.get("classification")
    if classification not in _OUTCOME_NAMES:
        raise ValueError("mechanical option has an unknown classification")
    return classification


def _run_option(
    registry,
    runtime_row,
    private_gold,
    request,
    initial_state,
    option_id,
    request_index,
    option_index,
    provenance,
):
    initial_state = EpisodeState(initial_state.to_dict())
    tool_name = initial_state.to_dict()["expected_tool"]
    request_kind = request["request_kind"]
    action_payload = _action_payload(tool_name, request_kind, option_id)
    raw_response = canonical_json(action_payload)
    metadata = _metadata(
        runtime_row,
        request,
        "skim-replay:%04d:%d" % (request_index, option_index),
        provenance,
    )
    runtime = Runtime(initial_state, registry, **metadata)
    result = runtime.accept(raw_response)
    expected_result = ToolResult(
        {"ok": True, "option_id": option_id}, terminal=True
    )
    if canonical_json_bytes(result.to_dict()) != canonical_json_bytes(
        expected_result.to_dict()
    ):
        raise ValueError("handler result differs from the public replay result")
    expected_state = _expected_state(
        initial_state, tool_name, request_kind, option_id
    )
    _verify_event(
        runtime,
        initial_state,
        expected_state,
        action_payload,
        raw_response,
        expected_result,
        metadata,
    )
    resumed = Runtime.resume(
        initial_state,
        registry,
        events=runtime.events,
        **metadata,
    )
    if (
        resumed.terminal is not True
        or state_sha256(resumed.state) != state_sha256(expected_state)
        or canonical_json_bytes([event.to_dict() for event in resumed.events])
        != canonical_json_bytes([event.to_dict() for event in runtime.events])
    ):
        raise ValueError("semantic resume differs from the executed transition")
    try:
        resumed.accept(raw_response)
    except TerminalRuntimeError:
        pass
    else:
        raise ValueError("resumed terminal runtime accepted a second action")
    return _outcome(private_gold, request_kind, option_id, expected_state)


def _unknown_option(registered_options):
    value = "audit_unregistered_option"
    while value in registered_options:
        value += "_x"
    return value


def _probe_payloads(initial_state):
    state = initial_state.to_dict()
    tool_name = state["expected_tool"]
    request_kind = state["request_kind"]
    option_id = next(iter(state["registered_options"]))
    return {
        "arbitrary_gold": _action_payload(
            tool_name,
            request_kind,
            option_id,
            {"mechanical_action_map": {}},
        ),
        "arbitrary_state": _action_payload(
            tool_name,
            request_kind,
            option_id,
            {"state": {"commit": "model-controlled"}},
        ),
        "extra_argument": _action_payload(
            tool_name,
            request_kind,
            option_id,
            {"unexpected_argument": True},
        ),
        "unknown_option": _action_payload(
            tool_name,
            request_kind,
            _unknown_option(state["registered_options"]),
        ),
    }


def _run_mutation_probes(
    registry,
    runtime_row,
    request,
    initial_state,
    request_index,
    findings,
    stats,
    provenance,
):
    for probe_name, action_payload in _probe_payloads(initial_state).items():
        metadata = _metadata(
            runtime_row,
            request,
            "skim-replay-probe:%04d:%s" % (request_index, probe_name),
            provenance,
        )
        probe_state = EpisodeState(initial_state.to_dict())
        runtime = Runtime(probe_state, registry, **metadata)
        state_before = state_sha256(runtime.state)
        events_before = runtime.events
        head_before = runtime.event_log.live_head()
        terminal_before = runtime.terminal
        rejected = False
        try:
            runtime.accept(canonical_json(action_payload))
        except MemoryError:
            raise
        except Exception:
            rejected = True

        changed = (
            state_sha256(runtime.state) != state_before
            or runtime.events != events_before
            or runtime.event_log.live_head() != head_before
            or runtime.terminal is not terminal_before
        )
        if changed:
            stats["mutation_probe_state_changes"] += 1
            _hard(
                findings,
                "action_replay.mutation_probe_state_changed",
                "Rejected mutation probe changed custody state or evidence.",
                record_id=runtime_row.get("runtime_request_id"),
                details={"probe": probe_name},
            )
        if rejected and not changed:
            stats["rejected_mutation_probes"][probe_name] += 1
        elif not rejected:
            _hard(
                findings,
                "action_replay.mutation_probe_accepted",
                "Audit registry accepted an arbitrary model-controlled write.",
                record_id=runtime_row.get("runtime_request_id"),
                details={"probe": probe_name},
            )


def _indexed_rows(rows, key, label):
    result = {}
    for index, row in enumerate(rows):
        if type(row) is not dict:
            raise ValueError("%s row %d is not an exact object" % (label, index))
        value = row.get(key)
        if type(value) is not str or not value or value in result:
            raise ValueError("%s rows do not have unique %s values" % (label, key))
        result[value] = row
    return result


def _audit_action_replay(public, gold, runtime):
    stats = _empty_stats(
        len(public) if type(public) in (list, tuple) else 0,
        len(runtime) if type(runtime) in (list, tuple) else 0,
    )
    findings = []
    if any(type(rows) not in (list, tuple) for rows in (public, gold, runtime)):
        _hard(
            findings,
            "action_replay.input_error",
            "Public, private, and runtime inputs must be exact lists or tuples.",
        )
        return _sorted_findings(findings), stats

    try:
        public_by_id = _indexed_rows(public, "logical_record_id", "public")
        gold_by_id = _indexed_rows(gold, "logical_record_id", "private")
        public_positions = {
            row["logical_record_id"]: index
            for index, row in enumerate(public)
        }
        gold_positions = {
            row["logical_record_id"]: index
            for index, row in enumerate(gold)
        }
        expected_requests = _expected_request_order(public)
        registry = _build_audit_registry()
    except MemoryError:
        raise
    except Exception as exc:
        _hard(
            findings,
            "action_replay.input_error",
            "Unable to construct audit replay inputs: %s" % exc,
            details={"exception_type": type(exc).__name__},
        )
        return _sorted_findings(findings), stats

    if len(public) != 640 or len(gold) != 640 or len(runtime) != 800:
        _hard(
            findings,
            "action_replay.input_error",
            "Replay audit requires exactly 640 public, 640 private, and 800 runtime rows.",
        )

    for request_index, runtime_row in enumerate(runtime):
        record_id = (
            runtime_row.get("runtime_request_id")
            if type(runtime_row) is dict
            else "runtime:index:%d" % request_index
        )
        if type(runtime_row) is not dict:
            _hard(
                findings,
                "action_replay.input_error",
                "Runtime row is not an exact object.",
                record_id=record_id,
            )
            continue
        nested_request = runtime_row.get("request_template")
        nested_tool_schema = (
            nested_request.get("tool_schema")
            if type(nested_request) is dict
            else None
        )
        nested_tool = (
            nested_tool_schema.get("name")
            if type(nested_tool_schema) is dict
            else None
        )
        if nested_tool not in SKIM_TOOL_RECIPES:
            _hard(
                findings,
                "action_replay.unreachable_action",
                "Declared request tool is not reachable through the audit registry.",
                record_id=record_id,
                details={"declared_tool": str(nested_tool)},
            )
        if request_index >= len(expected_requests):
            _hard(
                findings,
                "action_replay.provenance_mismatch",
                "Runtime request has no public request at its ordered position.",
                record_id=record_id,
                details={"runtime_index": request_index},
            )
            continue
        public_row, request = expected_requests[request_index]
        logical_id = public_row.get("logical_record_id")
        if public_by_id.get(logical_id) is not public_row:
            _hard(
                findings,
                "action_replay.provenance_mismatch",
                "Ordered public request does not retain unique record identity.",
                record_id=record_id,
            )
            continue
        private_gold = gold_by_id.get(logical_id)
        if (
            private_gold is None
            or gold_positions.get(logical_id) != public_positions.get(logical_id)
        ):
            _hard(
                findings,
                "action_replay.provenance_mismatch",
                "Ordered public request has no same-index private replay state.",
                record_id=record_id,
            )
            continue
        try:
            provenance = _bind_provenance(
                runtime_row, public_row, request, private_gold
            )
        except MemoryError:
            raise
        except Exception as exc:
            _hard(
                findings,
                "action_replay.provenance_mismatch",
                "Unable to recompute request provenance: %s" % exc,
                record_id=record_id,
                details={"exception_type": type(exc).__name__},
            )
            continue
        if provenance["reasons"]:
            _hard(
                findings,
                "action_replay.provenance_mismatch",
                "Runtime request differs from independently computed public provenance.",
                record_id=record_id,
                details={"mismatches": list(provenance["reasons"])},
            )
            continue
        tool_schema = request.get("tool_schema")
        tool_name = tool_schema.get("name") if type(tool_schema) is dict else None
        response_schema = request.get("response_schema")
        response_tool = None
        if type(response_schema) is dict:
            properties = response_schema.get("properties")
            if type(properties) is dict and type(properties.get("tool")) is dict:
                response_tool = properties["tool"].get("const")
        request_kind = request.get("request_kind")
        recipe = SKIM_TOOL_RECIPES.get(tool_name)
        expected_recognition = request_kind == "recognition"
        if (
            recipe is None
            or response_tool != tool_name
            or (tool_name == RECOGNITION_TOOL_HANDLER) is not expected_recognition
            or request_kind not in {"action", "recognition"}
        ):
            _hard(
                findings,
                "action_replay.unreachable_action",
                "Declared request tool is not reachable through the audit registry.",
                record_id=record_id,
                details={"declared_tool": str(tool_name)},
            )
            continue
        try:
            initial_state = _private_initial_state(
                runtime_row, private_gold, request
            )
            _run_mutation_probes(
                registry,
                runtime_row,
                request,
                initial_state,
                request_index,
                findings,
                stats,
                provenance,
            )
            for option_index, option_id in enumerate(_option_ids(request)):
                outcome = _run_option(
                    registry,
                    runtime_row,
                    private_gold,
                    request,
                    initial_state,
                    option_id,
                    request_index,
                    option_index,
                    provenance,
                )
                stats["replay_count"] += 1
                stats["event_chains_verified"] += 1
                stats["resumes_verified"] += 1
                stats["outcome_counts"][outcome] += 1
        except MemoryError:
            raise
        except Exception as exc:
            _hard(
                findings,
                "action_replay.unreachable_action",
                "Registered option failed deterministic replay: %s" % exc,
                record_id=record_id,
                details={"exception_type": type(exc).__name__},
            )

    if stats["replay_count"] != 1600:
        _hard(
            findings,
            "action_replay.replay_count",
            "Executable replay did not verify exactly 1,600 request options.",
            details={"actual": stats["replay_count"], "expected": 1600},
        )
    if stats["outcome_counts"] != _EXPECTED_OUTCOMES:
        _hard(
            findings,
            "action_replay.score_mismatch",
            "Mechanical replay outcomes differ from the frozen bank arithmetic.",
            details={"actual": dict(stats["outcome_counts"])},
        )
    if stats["rejected_mutation_probes"] != _EXPECTED_PROBES:
        _hard(
            findings,
            "action_replay.mutation_probe_count",
            "Mutation probes were not rejected exactly once per runtime request.",
            details={"actual": dict(stats["rejected_mutation_probes"])},
        )
    return _sorted_findings(findings), stats


def audit_action_replay(public, gold, runtime):
    """Execute every registered option and return findings plus replay evidence."""

    try:
        return _audit_action_replay(public, gold, runtime)
    except MemoryError:
        raise
    except Exception as exc:
        return (
            [
                make_finding(
                    audit="action_replay",
                    code="action_replay.input_error",
                    severity="hard",
                    message="Action replay audit failed closed: %s" % exc,
                    details={"exception_type": type(exc).__name__},
                )
            ],
            _empty_stats(),
        )


def main(argv=None):
    parser = add_common_cli_arguments(argparse.ArgumentParser(description=__doc__))
    args = parser.parse_args(argv)
    stats = _empty_stats()
    manifest = {}
    evidence = None
    try:
        inputs = load_audit_inputs(
            args.bank, args.gold, args.runtime, args.manifest
        )
        manifest = inputs.manifest
        evidence = inputs.evidence
        findings, stats = audit_action_replay(
            inputs.public, inputs.gold, inputs.runtime
        )
        if inputs.hash_mismatches:
            _hard(
                findings,
                "action_replay.artifact_hash_mismatch",
                "Audited artifact bytes differ from the frozen manifest hashes.",
                details={"artifacts": list(inputs.hash_mismatches)},
            )
            findings = _sorted_findings(findings)
    except MemoryError:
        raise
    except Exception as exc:
        findings = [
            make_finding(
                audit="action_replay",
                code="action_replay.input_error",
                severity="hard",
                message="Action replay input failed closed: %s" % exc,
                details={"exception_type": type(exc).__name__},
            )
        ]
    write_reports(
        findings,
        audit_slug="action-replay-audit",
        audit_title="SKIM P1 action replay audit",
        checked_records=stats["records_checked"],
        checked_requests=stats["requests_checked"],
        manifest=manifest,
        output_dir=args.output_dir,
        report_date=args.report_date,
        checked_option_replays=stats["replay_count"],
        artifact_evidence=evidence,
    )
    return report_exit_code(findings)


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["audit_action_replay", "main"]
