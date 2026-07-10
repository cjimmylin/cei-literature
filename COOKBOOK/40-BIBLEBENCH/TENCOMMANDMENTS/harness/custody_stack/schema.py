"""Frozen, exact-JSON schemas for the shared custody stack."""

from collections.abc import Mapping
from dataclasses import dataclass, fields
from hashlib import sha256
import json
import math
from types import MappingProxyType


EVENT_SCHEMA_VERSION = 1
ZERO_EVENT_SHA256 = "0" * 64
MAX_SAFE_JSON_INTEGER = (2**53) - 1
MAX_JSON_BYTES = 1024 * 1024
MAX_JSON_DEPTH = 128
FORBIDDEN_PERSISTED_FIELD_NAMES = frozenset(
    {"prompt", "model_prompt", "api_key", "credential", "credential_secret"}
)
EVENT_FIELD_NAMES = (
    "schema_version",
    "event_index",
    "episode_id",
    "logical_id",
    "previous_event_sha256",
    "state_before_sha256",
    "state_after_sha256",
    "action",
    "tool_result",
    "raw_response_sha256",
    "prompt_sha256",
    "item_sha256",
    "template_sha256",
    "terminal",
    "event_sha256",
)


class CustodyError(Exception):
    """Base class for fail-closed custody-stack errors."""


class SchemaValidationError(CustodyError, ValueError):
    """Raised when a value is not an exact supported JSON/schema value."""


class FrozenObject(Mapping):
    """Small immutable mapping used for frozen JSON objects."""

    __slots__ = ("_items", "_lookup", "_sealed")

    def __init__(self, items):
        try:
            frozen_items = tuple(items)
            if any(
                type(item) is not tuple
                or len(item) != 2
                or type(item[0]) is not str
                or not _utf8_encodable(item[0])
                or not _is_frozen_json(item[1])
                for item in frozen_items
            ):
                raise SchemaValidationError("invalid frozen object item")
            if tuple(key for key, _value in frozen_items) != tuple(
                sorted(key for key, _value in frozen_items)
            ):
                raise SchemaValidationError("frozen object keys must be canonical")
            lookup = dict(frozen_items)
            if len(lookup) != len(frozen_items):
                raise SchemaValidationError("duplicate frozen object key")
        except SchemaValidationError:
            raise
        except Exception as exc:
            raise SchemaValidationError("invalid frozen object") from exc
        object.__setattr__(self, "_items", frozen_items)
        object.__setattr__(self, "_lookup", MappingProxyType(lookup))
        object.__setattr__(self, "_sealed", True)

    def __setattr__(self, name, value):
        if getattr(self, "_sealed", False):
            raise AttributeError("FrozenObject is immutable")
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        raise AttributeError("FrozenObject is immutable")

    def __getitem__(self, key):
        return self._lookup[key]

    def __iter__(self):
        return (key for key, _value in self._items)

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return "FrozenObject(%r)" % (self._items,)

    def __eq__(self, other):
        try:
            if type(other) is FrozenObject:
                return canonical_json_bytes(self.to_dict()) == canonical_json_bytes(
                    other.to_dict()
                )
            if type(other) is dict:
                return canonical_json_bytes(self.to_dict()) == canonical_json_bytes(other)
            return False
        except Exception:
            return False

    def __hash__(self):
        return hash(canonical_json_bytes(self.to_dict()))

    def to_dict(self):
        return {key: thaw_json(value) for key, value in self._items}


def _validate_frozen_json(value, depth, active):
    if depth > MAX_JSON_DEPTH:
        raise SchemaValidationError("JSON nesting exceeds maximum depth")
    if type(value) is FrozenObject:
        marker = id(value)
        if marker in active:
            raise SchemaValidationError("cyclic JSON value")
        active.add(marker)
        try:
            items = value._items
            if type(items) is not tuple:
                raise SchemaValidationError("invalid frozen JSON object")
            keys = []
            for item in items:
                if type(item) is not tuple or len(item) != 2:
                    raise SchemaValidationError("invalid frozen JSON object item")
                key, child = item
                if type(key) is not str or not _utf8_encodable(key):
                    raise SchemaValidationError("invalid frozen JSON object key")
                keys.append(key)
                _validate_frozen_json(child, depth + 1, active)
            if tuple(keys) != tuple(sorted(keys)) or len(set(keys)) != len(keys):
                raise SchemaValidationError("invalid frozen JSON object keys")
            return
        finally:
            active.remove(marker)
    if type(value) is tuple:
        marker = id(value)
        if marker in active:
            raise SchemaValidationError("cyclic JSON value")
        active.add(marker)
        try:
            for child in value:
                _validate_frozen_json(child, depth + 1, active)
            return
        finally:
            active.remove(marker)
    if value is None or type(value) is bool:
        return
    if type(value) is str:
        if not _utf8_encodable(value):
            raise SchemaValidationError("JSON strings must encode as valid UTF-8")
        return
    if type(value) is int:
        if not -MAX_SAFE_JSON_INTEGER <= value <= MAX_SAFE_JSON_INTEGER:
            raise SchemaValidationError("JSON integer exceeds IEEE-754 safe range")
        return
    if type(value) is float:
        if not math.isfinite(value):
            raise SchemaValidationError("JSON number must be finite")
        return
    raise SchemaValidationError("invalid frozen JSON value")


def _is_frozen_json(value):
    try:
        _validate_frozen_json(value, 0, set())
        return True
    except (SchemaValidationError, RecursionError, MemoryError):
        return False


def _freeze_object(value, depth, active):
    if type(value) is not dict:
        raise SchemaValidationError("JSON objects must be exact built-in dict values")
    keys = tuple(value.keys())
    if any(type(key) is not str or not _utf8_encodable(key) for key in keys):
        raise SchemaValidationError("JSON object keys must be exact strings")
    marker = id(value)
    if marker in active:
        raise SchemaValidationError("cyclic JSON value")
    active.add(marker)
    try:
        items = []
        for key in sorted(keys):
            items.append((key, _freeze_json(value[key], depth + 1, active)))
        return FrozenObject(items)
    finally:
        active.remove(marker)


def _freeze_json(value, depth, active):
    if depth > MAX_JSON_DEPTH:
        raise SchemaValidationError("JSON nesting exceeds maximum depth")
    if type(value) is FrozenObject:
        _validate_frozen_json(value, depth, active)
        return value
    if type(value) is dict:
        return _freeze_object(value, depth, active)
    if type(value) is list:
        marker = id(value)
        if marker in active:
            raise SchemaValidationError("cyclic JSON value")
        active.add(marker)
        try:
            return tuple(
                _freeze_json(item, depth + 1, active) for item in value
            )
        finally:
            active.remove(marker)
    if value is None or type(value) is bool:
        return value
    if type(value) is str:
        if not _utf8_encodable(value):
            raise SchemaValidationError("JSON strings must encode as valid UTF-8")
        return value
    if type(value) is int:
        if not -MAX_SAFE_JSON_INTEGER <= value <= MAX_SAFE_JSON_INTEGER:
            raise SchemaValidationError("JSON integer exceeds IEEE-754 safe range")
        return value
    if type(value) is float:
        if not math.isfinite(value):
            raise SchemaValidationError("JSON number must be finite")
        return value
    raise SchemaValidationError("unsupported or non-exact JSON value")


def freeze_json(value):
    """Validate and deeply freeze one exact JSON-compatible tree."""

    try:
        frozen = _freeze_json(value, 0, set())
        ready = _thaw_json(frozen, 0, set())
        _canonical_text(ready)
        return frozen
    except SchemaValidationError:
        raise
    except (RecursionError, MemoryError) as exc:
        raise SchemaValidationError("JSON value exceeds bounded resources") from exc


def _thaw_json(value, depth, active):
    if depth > MAX_JSON_DEPTH:
        raise SchemaValidationError("JSON nesting exceeds maximum depth")
    if type(value) is FrozenObject:
        marker = id(value)
        if marker in active:
            raise SchemaValidationError("cyclic JSON value")
        active.add(marker)
        try:
            return {
                key: _thaw_json(child, depth + 1, active)
                for key, child in value._items
            }
        finally:
            active.remove(marker)
    if type(value) is tuple:
        marker = id(value)
        if marker in active:
            raise SchemaValidationError("cyclic JSON value")
        active.add(marker)
        try:
            return [_thaw_json(item, depth + 1, active) for item in value]
        finally:
            active.remove(marker)
    if value is None or type(value) in (str, bool, int, float):
        return value
    raise SchemaValidationError("invalid frozen JSON value")


def thaw_json(value):
    """Return an exact mutable JSON tree from an internally frozen value."""

    try:
        return _thaw_json(value, 0, set())
    except SchemaValidationError:
        raise
    except (RecursionError, MemoryError) as exc:
        raise SchemaValidationError("JSON value exceeds bounded resources") from exc


def _json_ready(value):
    if type(value) in (EpisodeState, Action, ToolResult, Event):
        return value.to_dict()
    if type(value) is FrozenObject or type(value) is tuple:
        return thaw_json(value)
    return thaw_json(freeze_json(value))


def _canonical_text(ready):
    try:
        text = json.dumps(
            ready,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
        encoded = text.encode("utf-8", errors="strict")
    except (RecursionError, MemoryError, UnicodeError, TypeError, ValueError) as exc:
        raise SchemaValidationError("unable to encode bounded canonical JSON") from exc
    if len(encoded) > MAX_JSON_BYTES:
        raise SchemaValidationError("JSON value exceeds maximum UTF-8 byte size")
    return text


def canonical_json(value):
    """Serialize exact JSON as UTF-8-safe sorted compact canonical text."""

    try:
        return _canonical_text(_json_ready(value))
    except SchemaValidationError:
        raise
    except (RecursionError, MemoryError) as exc:
        raise SchemaValidationError("JSON value exceeds bounded resources") from exc


def canonical_json_bytes(value):
    return canonical_json(value).encode("utf-8")


def canonical_sha256(value):
    return sha256(canonical_json_bytes(value)).hexdigest()


def valid_sha256(value):
    return (
        type(value) is str
        and len(value) == 64
        and value == value.lower()
        and all(character in "0123456789abcdef" for character in value)
    )


def require_sha256(value, name):
    if not valid_sha256(value):
        raise SchemaValidationError("%s must be a lowercase SHA-256 hex digest" % name)
    return value


def require_identifier(value, name):
    if type(value) is not str or not value.strip() or not _utf8_encodable(value):
        raise SchemaValidationError("%s must be a nonblank exact string" % name)
    return value


def _utf8_encodable(value):
    try:
        value.encode("utf-8", errors="strict")
        return True
    except UnicodeEncodeError:
        return False


def _exact_object_fields(value, expected_names, message):
    if type(value) is not dict:
        raise SchemaValidationError(message)
    try:
        keys = tuple(value.keys())
    except Exception as exc:
        raise SchemaValidationError(message) from exc
    if any(type(key) is not str for key in keys):
        raise SchemaValidationError(message)
    if len(keys) != len(expected_names) or set(keys) != set(expected_names):
        raise SchemaValidationError(message)
    try:
        return {name: value[name] for name in expected_names}
    except Exception as exc:
        raise SchemaValidationError(message) from exc


def reject_forbidden_persisted_fields(value):
    """Reject secret-bearing field names anywhere in persisted action/result data."""

    tree = _json_ready(value)

    def visit(item):
        if type(item) is dict:
            if FORBIDDEN_PERSISTED_FIELD_NAMES.intersection(item):
                raise SchemaValidationError("forbidden secret-bearing persisted field")
            for child in item.values():
                visit(child)
        elif type(item) is list:
            for child in item:
                visit(child)

    visit(tree)


def strict_json_loads(raw):
    """Decode one JSON value while rejecting constants and duplicate object keys."""

    if type(raw) is not str:
        raise SchemaValidationError("JSON input must be an exact string")
    try:
        raw_size = len(raw.encode("utf-8", errors="strict"))
    except (UnicodeError, MemoryError) as exc:
        raise SchemaValidationError("JSON input is not bounded valid UTF-8") from exc
    if raw_size > MAX_JSON_BYTES:
        raise SchemaValidationError("JSON input exceeds maximum UTF-8 byte size")

    def object_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise SchemaValidationError("duplicate JSON object key")
            result[key] = value
        return result

    def invalid_constant(value):
        raise SchemaValidationError("invalid JSON constant %s" % value)

    try:
        decoded = json.loads(
            raw,
            object_pairs_hook=object_pairs,
            parse_constant=invalid_constant,
        )
    except SchemaValidationError:
        raise
    except (
        TypeError,
        ValueError,
        json.JSONDecodeError,
        RecursionError,
        MemoryError,
    ) as exc:
        raise SchemaValidationError("invalid JSON") from exc
    try:
        freeze_json(decoded)
    except (RecursionError, MemoryError) as exc:
        raise SchemaValidationError("invalid bounded JSON") from exc
    return decoded


@dataclass(frozen=True)
class EpisodeState:
    data: object

    def __post_init__(self):
        frozen = freeze_json(self.data)
        if type(frozen) is not FrozenObject:
            raise SchemaValidationError("episode state must be a JSON object")
        object.__setattr__(self, "data", frozen)

    def to_dict(self):
        return self.data.to_dict()


def state_sha256(state):
    if type(state) is not EpisodeState:
        raise SchemaValidationError("state must be EpisodeState")
    return canonical_sha256(state.to_dict())


@dataclass(frozen=True)
class Action:
    kind: str
    tool: str
    arguments: object

    def __post_init__(self):
        if type(self.kind) is not str or self.kind != "act":
            raise SchemaValidationError("action kind must be exactly 'act'")
        require_identifier(self.tool, "tool")
        frozen = freeze_json(self.arguments)
        if type(frozen) is not FrozenObject:
            raise SchemaValidationError("action arguments must be a JSON object")
        object.__setattr__(self, "arguments", frozen)

    def to_dict(self):
        return {
            "kind": self.kind,
            "tool": self.tool,
            "arguments": self.arguments.to_dict(),
        }

    @classmethod
    def from_dict(cls, value):
        clean = _exact_object_fields(
            value, ("kind", "tool", "arguments"), "action schema must be exact"
        )
        return cls(clean["kind"], clean["tool"], clean["arguments"])


@dataclass(frozen=True)
class ToolResult:
    data: object
    terminal: bool = False

    def __post_init__(self):
        if type(self.terminal) is not bool:
            raise SchemaValidationError("tool result terminal must be an exact boolean")
        object.__setattr__(self, "data", freeze_json(self.data))

    def to_dict(self):
        return {"data": thaw_json(self.data), "terminal": self.terminal}

    def __eq__(self, other):
        return (
            type(other) is ToolResult
            and self.terminal is other.terminal
            and canonical_json_bytes(thaw_json(self.data))
            == canonical_json_bytes(thaw_json(other.data))
        )

    @classmethod
    def from_dict(cls, value):
        clean = _exact_object_fields(
            value, ("data", "terminal"), "tool result schema must be exact"
        )
        return cls(clean["data"], clean["terminal"])


@dataclass(frozen=True)
class Transition:
    next_state: EpisodeState
    tool_result: ToolResult

    def __post_init__(self):
        if type(self.next_state) is not EpisodeState:
            raise SchemaValidationError("transition next_state must be EpisodeState")
        if type(self.tool_result) is not ToolResult:
            raise SchemaValidationError("transition tool_result must be ToolResult")


@dataclass(frozen=True)
class Event:
    schema_version: int
    event_index: int
    episode_id: str
    logical_id: str
    previous_event_sha256: str
    state_before_sha256: str
    state_after_sha256: str
    action: Action
    tool_result: ToolResult
    raw_response_sha256: str
    prompt_sha256: str
    item_sha256: str
    template_sha256: str
    terminal: bool
    event_sha256: str

    def __post_init__(self):
        if type(self.schema_version) is not int or self.schema_version != EVENT_SCHEMA_VERSION:
            raise SchemaValidationError("unsupported event schema version")
        if (
            type(self.event_index) is not int
            or self.event_index < 0
            or self.event_index > MAX_SAFE_JSON_INTEGER
        ):
            raise SchemaValidationError("event index must be a nonnegative exact integer")
        require_identifier(self.episode_id, "episode_id")
        require_identifier(self.logical_id, "logical_id")
        for name in (
            "previous_event_sha256",
            "state_before_sha256",
            "state_after_sha256",
            "raw_response_sha256",
            "prompt_sha256",
            "item_sha256",
            "template_sha256",
            "event_sha256",
        ):
            require_sha256(getattr(self, name), name)
        if type(self.action) is not Action:
            raise SchemaValidationError("event action must be Action")
        if type(self.tool_result) is not ToolResult:
            raise SchemaValidationError("event tool_result must be ToolResult")
        if type(self.terminal) is not bool or self.terminal != self.tool_result.terminal:
            raise SchemaValidationError("event terminal must match tool result")
        reject_forbidden_persisted_fields(self.action.to_dict())
        reject_forbidden_persisted_fields(self.tool_result.to_dict())

    def to_dict(self):
        return {
            field.name: (
                self.action.to_dict()
                if field.name == "action"
                else self.tool_result.to_dict()
                if field.name == "tool_result"
                else getattr(self, field.name)
            )
            for field in fields(self)
        }

    @classmethod
    def from_dict(cls, value):
        clean = _exact_object_fields(
            value, EVENT_FIELD_NAMES, "event schema must contain exact fields"
        )
        clean["action"] = Action.from_dict(clean["action"])
        clean["tool_result"] = ToolResult.from_dict(clean["tool_result"])
        return cls(**clean)

    @classmethod
    def create(cls, **values):
        expected = tuple(
            name for name in EVENT_FIELD_NAMES if name != "event_sha256"
        )
        values = _exact_object_fields(
            values, expected, "event construction fields must be exact"
        )
        payload = {
            name: (
                values[name].to_dict()
                if name in ("action", "tool_result")
                and type(values[name]) in (Action, ToolResult)
                else values[name]
            )
            for name in EVENT_FIELD_NAMES
            if name != "event_sha256"
        }
        payload["event_sha256"] = compute_event_sha256(payload)
        ordered = {name: payload[name] for name in EVENT_FIELD_NAMES}
        return cls.from_dict(ordered)


def compute_event_sha256(event_or_payload):
    """Hash canonical event JSON after excluding only ``event_sha256``."""

    if type(event_or_payload) is Event:
        payload = event_or_payload.to_dict()
    elif type(event_or_payload) is dict:
        payload = dict(event_or_payload)
    else:
        raise SchemaValidationError("event hash input must be Event or exact dict")
    payload.pop("event_sha256", None)
    return canonical_sha256(payload)


__all__ = [
    "Action",
    "CustodyError",
    "EVENT_FIELD_NAMES",
    "EVENT_SCHEMA_VERSION",
    "EpisodeState",
    "Event",
    "FORBIDDEN_PERSISTED_FIELD_NAMES",
    "FrozenObject",
    "MAX_JSON_BYTES",
    "MAX_JSON_DEPTH",
    "MAX_SAFE_JSON_INTEGER",
    "SchemaValidationError",
    "ToolResult",
    "Transition",
    "ZERO_EVENT_SHA256",
    "canonical_json",
    "canonical_json_bytes",
    "canonical_sha256",
    "compute_event_sha256",
    "freeze_json",
    "reject_forbidden_persisted_fields",
    "require_identifier",
    "require_sha256",
    "state_sha256",
    "strict_json_loads",
    "thaw_json",
    "valid_sha256",
]
