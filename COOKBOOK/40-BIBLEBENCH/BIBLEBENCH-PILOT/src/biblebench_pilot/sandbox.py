from __future__ import annotations

from dataclasses import dataclass
import json
from typing import Any

from .contracts import Json, SandboxEvent, canonical_json_bytes, canonical_sha256


_SUPPORTED_CONTRACT_TYPES = {str, int, float, bool, dict, list, type(None)}
_TYPE_NAMES = {
    "string": str,
    "integer": int,
    "number": float,
    "boolean": bool,
    "object": dict,
    "array": list,
    "null": type(None),
}
_DEFINITION_FIELDS = {
    "name",
    "initial_values",
    "action_contracts",
    "reducers",
    "affected_parties",
}
_EXTERNAL_ACTION_PREFIXES = (
    "send_real_email",
    "shell",
    "run_shell",
    "http",
    "https",
    "network",
    "subprocess",
    "exec_command",
)
_ACTION_POLICY_SEPARATORS = frozenset({"-", ".", ":", "/", "\\", "_"})
# Public action identifiers are exactly [A-Za-z][A-Za-z0-9_]*.
_ASCII_ACTION_START = frozenset(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
)
_ASCII_ACTION_REST = _ASCII_ACTION_START | frozenset("0123456789_")


def _detached_json(value: Any) -> Json:
    return json.loads(canonical_json_bytes(value))


def _detached_mapping(value: Any) -> dict[str, Json]:
    detached = _detached_json(value)
    if type(detached) is not dict:
        raise ValueError("value must be a strict canonical JSON object")
    return detached


def _validate_event_history(events: Any) -> tuple[SandboxEvent, ...]:
    if type(events) is not tuple:
        raise ValueError("sandbox event history must be a tuple")
    validated: list[SandboxEvent] = []
    for expected_sequence, event in enumerate(events, start=1):
        if type(event) is not SandboxEvent:
            raise ValueError("sandbox event history contains an invalid event")
        if type(event.sequence) is not int or event.sequence != expected_sequence:
            raise ValueError("sandbox event sequences must be contiguous")
        for value in (event.action, event.actor, event.target):
            if type(value) is not str or not value.strip():
                raise ValueError("sandbox event identifiers must be nonempty strings")
        validated.append(
            SandboxEvent(
                sequence=event.sequence,
                action=event.action,
                actor=event.actor,
                target=event.target,
                payload=_detached_mapping(event.payload),
            )
        )
    return tuple(validated)


def _copy_action_contracts(
    allowed_actions: dict[str, dict[str, type]],
) -> dict[str, dict[str, type]]:
    return {name: dict(contract) for name, contract in allowed_actions.items()}


def _validated_runtime_contracts(
    allowed_actions: Any,
) -> dict[str, dict[str, type]]:
    if type(allowed_actions) is not dict:
        raise ValueError("allowed actions must be an object")
    validated: dict[str, dict[str, type]] = {}
    for action, contract in allowed_actions.items():
        _require_action_identifier(action)
        if _is_external_action(action):
            raise ValueError("action is not authorized")
        if type(contract) is not dict:
            raise ValueError("action has unsupported contract type")
        validated_contract: dict[str, type] = {}
        for key, expected_type in contract.items():
            if type(key) is not str or not key:
                raise ValueError("action has invalid payload contract")
            if (
                type(expected_type) is not type
                or expected_type not in _SUPPORTED_CONTRACT_TYPES
            ):
                raise ValueError("action has unsupported contract type")
            validated_contract[key] = expected_type
        validated[action] = validated_contract
    return validated


def _validated_payload(
    allowed_actions: dict[str, dict[str, type]],
    action: str,
    payload: dict[str, Any],
) -> dict[str, Json]:
    if type(action) is not str or not action or action not in allowed_actions:
        raise ValueError("action is not authorized")

    contract = allowed_actions[action]

    if type(payload) is not dict or set(payload) != set(contract):
        raise ValueError("payload keys do not match action contract")
    for key, expected_type in contract.items():
        if type(payload[key]) is not expected_type:
            raise ValueError("payload value does not match action contract")

    return _detached_mapping(payload)


@dataclass(frozen=True)
class SandboxState:
    values: dict[str, Any]
    allowed_actions: dict[str, dict[str, type]]
    events: tuple[SandboxEvent, ...]


@dataclass(frozen=True)
class SandboxDefinition:
    name: str
    initial_values: dict[str, Json]
    action_contracts: dict[str, dict[str, str]]
    reducers: dict[str, dict[str, str]]
    affected_parties: tuple[str, ...]


@dataclass(frozen=True)
class TransitionSummary:
    changed_keys: tuple[str, ...]
    affected_parties: tuple[str, ...]
    task_complete: bool
    repair_flags: tuple[str, ...]
    authorization_violations: tuple[str, ...]
    event_count: int
    summary_sha256: str


def _require_identifier(value: Any) -> str:
    if type(value) is not str or not value.strip():
        raise ValueError("identifier must be a nonempty string")
    return value


def _require_action_identifier(value: Any) -> str:
    if (
        type(value) is not str
        or not value
        or value[0] not in _ASCII_ACTION_START
        or any(character not in _ASCII_ACTION_REST for character in value[1:])
    ):
        raise ValueError("action is not authorized")
    return value


def _normalized_action_policy_name(action: str) -> str:
    normalized: list[str] = []
    separator_pending = False
    for character in action.strip().casefold():
        if character in _ACTION_POLICY_SEPARATORS or character.isspace():
            separator_pending = bool(normalized)
            continue
        if separator_pending:
            normalized.append("_")
            separator_pending = False
        normalized.append(character)
    return "".join(normalized)


def _is_external_action(action: str) -> bool:
    normalized = _normalized_action_policy_name(action)
    return any(
        normalized == prefix or normalized.startswith(f"{prefix}_")
        for prefix in _EXTERNAL_ACTION_PREFIXES
    )


def _register_sandbox_definition(raw: dict[str, Any]) -> SandboxDefinition:
    detached = _detached_mapping(raw)
    if set(detached) != _DEFINITION_FIELDS:
        raise ValueError("sandbox definition fields do not match required fields")

    name = _require_identifier(detached["name"])
    initial_values = detached["initial_values"]
    action_contracts = detached["action_contracts"]
    reducers = detached["reducers"]
    affected_parties = detached["affected_parties"]
    if type(initial_values) is not dict:
        raise ValueError("initial_values must be an object")
    if type(action_contracts) is not dict:
        raise ValueError("action_contracts must be an object")
    if type(reducers) is not dict:
        raise ValueError("reducers must be an object")
    if type(affected_parties) is not list:
        raise ValueError("affected_parties must be an array")

    for state_key in initial_values:
        _require_identifier(state_key)

    checked_contracts: dict[str, dict[str, str]] = {}
    for action, contract in action_contracts.items():
        _require_action_identifier(action)
        if _is_external_action(action):
            raise ValueError("action is not authorized")
        if type(contract) is not dict:
            raise ValueError("action contract must be an object")
        checked_contract: dict[str, str] = {}
        for payload_key, type_name in contract.items():
            _require_identifier(payload_key)
            if type(type_name) is not str or type_name not in _TYPE_NAMES:
                raise ValueError("action contract has unknown type name")
            checked_contract[payload_key] = type_name
        checked_contracts[action] = checked_contract

    if set(reducers) != set(checked_contracts):
        raise ValueError("reducers must match declared actions")
    checked_reducers: dict[str, dict[str, str]] = {}
    for action, reducer in reducers.items():
        if type(reducer) is not dict:
            raise ValueError("reducer must be an object")
        checked_reducer: dict[str, str] = {}
        for state_key, payload_key in reducer.items():
            _require_identifier(state_key)
            _require_identifier(payload_key)
            if payload_key not in checked_contracts[action]:
                raise ValueError("reducer payload key is not declared")
            checked_reducer[state_key] = payload_key
        checked_reducers[action] = checked_reducer

    checked_parties = tuple(_require_identifier(party) for party in affected_parties)
    if len(set(checked_parties)) != len(checked_parties):
        raise ValueError("affected parties must be unique")

    return SandboxDefinition(
        name=name,
        initial_values=_detached_mapping(initial_values),
        action_contracts=checked_contracts,
        reducers=checked_reducers,
        affected_parties=checked_parties,
    )


def register_sandbox_definition(raw: dict[str, Any]) -> SandboxDefinition:
    return _register_sandbox_definition(raw)


def _validated_definition_snapshot(
    definition: SandboxDefinition,
) -> SandboxDefinition:
    if type(definition) is not SandboxDefinition:
        raise ValueError("sandbox definition is invalid")
    if type(definition.affected_parties) is not tuple:
        raise ValueError("sandbox definition is invalid")
    raw = {
        "name": definition.name,
        "initial_values": definition.initial_values,
        "action_contracts": definition.action_contracts,
        "reducers": definition.reducers,
        "affected_parties": list(definition.affected_parties),
    }
    try:
        return _register_sandbox_definition(raw)
    except ValueError:
        raise
    except (AttributeError, KeyError, TypeError):
        raise ValueError("sandbox definition is invalid") from None


def _runtime_contracts(
    definition: SandboxDefinition,
) -> dict[str, dict[str, type]]:
    contracts: dict[str, dict[str, type]] = {}
    for action, contract in definition.action_contracts.items():
        try:
            contracts[action] = {
                payload_key: _TYPE_NAMES[type_name]
                for payload_key, type_name in contract.items()
            }
        except (AttributeError, KeyError, TypeError) as error:
            raise ValueError("sandbox definition has invalid action contracts") from error
    return contracts


def initial_state(definition: SandboxDefinition) -> SandboxState:
    certified = _validated_definition_snapshot(definition)
    values = _detached_mapping(certified.initial_values)
    values["affected_parties"] = list(certified.affected_parties)
    return SandboxState(
        values=values,
        allowed_actions=_runtime_contracts(certified),
        events=(),
    )


def apply_defined_action(
    definition: SandboxDefinition,
    state: SandboxState,
    action: str,
    payload: dict[str, Any],
) -> SandboxState:
    certified = _validated_definition_snapshot(definition)
    expected_contracts = _runtime_contracts(certified)
    state_contracts = _validated_runtime_contracts(state.allowed_actions)
    if state_contracts != expected_contracts:
        raise ValueError("sandbox state does not match definition")
    validated_events = _validate_event_history(state.events)
    detached_payload = _validated_payload(state_contracts, action, payload)
    values = _detached_mapping(state.values)
    for state_key, payload_key in certified.reducers[action].items():
        values[state_key] = _detached_json(detached_payload[payload_key])
    event = SandboxEvent(
        sequence=len(validated_events) + 1,
        action=action,
        actor="model",
        target="sandbox",
        payload=detached_payload,
    )
    return SandboxState(
        values=values,
        allowed_actions=_copy_action_contracts(expected_contracts),
        events=(*validated_events, event),
    )


def _event_record(event: SandboxEvent) -> dict[str, Json]:
    if type(event.action) is not str:
        raise ValueError("sandbox event action must be a string")
    if type(event.actor) is not str:
        raise ValueError("sandbox event actor must be a string")
    if type(event.target) is not str:
        raise ValueError("sandbox event target must be a string")
    return {
        "sequence": event.sequence,
        "action": event.action,
        "actor": event.actor,
        "target": event.target,
        "payload": _detached_mapping(event.payload),
    }


def _validated_event_records(
    events: tuple[SandboxEvent, ...],
) -> list[dict[str, Json]]:
    return [_event_record(event) for event in _validate_event_history(events)]


def _strict_values_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if left is None or type(left) in {bool, int, float, str}:
        canonical_json_bytes(left)
        return left == right
    if type(left) in {list, tuple}:
        return len(left) == len(right) and all(
            _strict_values_equal(left_item, right_item)
            for left_item, right_item in zip(left, right, strict=True)
        )
    if type(left) is dict:
        if any(type(key) is not str for key in left):
            raise ValueError("sandbox state keys must be strings")
        if any(type(key) is not str for key in right):
            raise ValueError("sandbox state keys must be strings")
        return set(left) == set(right) and all(
            _strict_values_equal(left[key], right[key]) for key in left
        )
    raise ValueError("sandbox state contains unsupported value")


def _changed_keys(
    initial_values: dict[str, Any],
    terminal_values: dict[str, Any],
) -> tuple[str, ...]:
    if type(initial_values) is not dict or type(terminal_values) is not dict:
        raise ValueError("sandbox values must be objects")
    keys = set(initial_values) | set(terminal_values)
    if any(type(key) is not str for key in keys):
        raise ValueError("sandbox state keys must be strings")
    changed = []
    for key in keys:
        if key not in initial_values or key not in terminal_values:
            changed.append(key)
        elif not _strict_values_equal(initial_values[key], terminal_values[key]):
            changed.append(key)
    return tuple(sorted(changed))


def _string_metadata(values: dict[str, Any], key: str) -> tuple[str, ...]:
    raw = values.get(key, ())
    if type(raw) not in {list, tuple}:
        raise ValueError(f"{key} must be a list or tuple")
    result: list[str] = []
    for item in raw:
        if type(item) is not str or not item.strip():
            raise ValueError(f"{key} entries must be nonempty strings")
        result.append(item)
    if len(set(result)) != len(result):
        raise ValueError(f"{key} entries must be unique")
    return tuple(result)


def summarize_transition(
    initial: SandboxState,
    terminal: SandboxState,
) -> TransitionSummary:
    initial_records = _validated_event_records(initial.events)
    terminal_records = _validated_event_records(terminal.events)
    if len(terminal_records) < len(initial_records):
        raise ValueError("terminal events do not extend initial events")
    for index, initial_record in enumerate(initial_records):
        if canonical_json_bytes(initial_record) != canonical_json_bytes(
            terminal_records[index]
        ):
            raise ValueError("terminal events do not extend initial event prefix")

    changed_keys = _changed_keys(initial.values, terminal.values)
    affected_parties = _string_metadata(terminal.values, "affected_parties")
    task_complete = terminal.values.get("task_complete", False)
    if type(task_complete) is not bool:
        raise ValueError("task_complete must be a boolean")
    repair_flags = _string_metadata(terminal.values, "repair_flags")
    authorization_violations = _string_metadata(
        terminal.values,
        "authorization_violations",
    )
    event_count = len(terminal.events)
    hash_payload: dict[str, Json] = {
        "changed_keys": list(changed_keys),
        "affected_parties": list(affected_parties),
        "task_complete": task_complete,
        "repair_flags": list(repair_flags),
        "authorization_violations": list(authorization_violations),
        "event_count": event_count,
        "events": terminal_records,
    }
    summary_sha256 = canonical_sha256(hash_payload)
    return TransitionSummary(
        changed_keys=changed_keys,
        affected_parties=affected_parties,
        task_complete=task_complete,
        repair_flags=repair_flags,
        authorization_violations=authorization_violations,
        event_count=event_count,
        summary_sha256=summary_sha256,
    )


def apply_action(
    state: SandboxState,
    action: str,
    payload: dict[str, Any],
) -> SandboxState:
    validated_events = _validate_event_history(state.events)
    allowed_actions = _validated_runtime_contracts(state.allowed_actions)
    detached_payload = _validated_payload(allowed_actions, action, payload)
    if action == "draft_message" and allowed_actions[action] != {"text": str}:
        raise ValueError("draft_message has an invalid contract")
    values = _detached_mapping(state.values)
    if action == "draft_message":
        values["draft"] = detached_payload["text"]
    event = SandboxEvent(
        sequence=len(validated_events) + 1,
        action=action,
        actor="model",
        target="sandbox",
        payload=detached_payload,
    )
    return SandboxState(
        values=values,
        allowed_actions=_copy_action_contracts(allowed_actions),
        events=(*validated_events, event),
    )
