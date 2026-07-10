"""Deterministic, per-episode in-memory tool sandbox and registry."""

from dataclasses import dataclass
from threading import Lock
from types import MappingProxyType

from .schema import (
    Action,
    CustodyError,
    EpisodeState,
    FrozenObject,
    SchemaValidationError,
    ToolResult,
    Transition,
    canonical_json_bytes,
    freeze_json,
    require_identifier,
    thaw_json,
)


class ToolValidationError(CustodyError, ValueError):
    """Raised before dispatch when a tool name or argument schema is invalid."""


class SandboxViolation(CustodyError, ValueError):
    """Raised when a simulated action would leave its episode boundary."""


@dataclass(frozen=True)
class OptionalArgument:
    spec: object


@dataclass(frozen=True)
class _ObjectSpec:
    fields: tuple


class _AnyJSON:
    __slots__ = ()


ANY_JSON = _AnyJSON()


@dataclass(frozen=True)
class ToolSpec:
    name: str
    argument_schema: _ObjectSpec
    handler: object


def _freeze_schema_value(spec):
    if any(spec is allowed for allowed in (str, int, float, bool)):
        return spec
    if spec is ANY_JSON:
        return spec
    if type(spec) is OptionalArgument:
        return OptionalArgument(_freeze_schema_value(spec.spec))
    if type(spec) is dict:
        return _freeze_schema_object(spec)
    raise ToolValidationError("unsupported argument schema value")


def _freeze_schema_object(schema):
    if type(schema) is not dict:
        raise ToolValidationError("argument schema must be an exact dict")
    if any(type(name) is not str or not name for name in schema):
        raise ToolValidationError("argument schema names must be exact strings")
    frozen = []
    for name in sorted(schema):
        frozen.append((name, _freeze_schema_value(schema[name])))
    return _ObjectSpec(tuple(frozen))


def _validate_schema_value(value, spec, location):
    if spec is ANY_JSON:
        try:
            freeze_json(thaw_json(value))
        except SchemaValidationError as exc:
            raise ToolValidationError("%s must be exact JSON" % location) from exc
        return
    if any(spec is allowed for allowed in (str, int, float, bool)):
        if type(value) is not spec:
            raise ToolValidationError("%s has the wrong exact JSON type" % location)
        return
    if type(spec) is _ObjectSpec:
        _validate_schema_object(value, spec, location)
        return
    raise ToolValidationError("invalid frozen argument schema")


def _validate_schema_object(value, spec, location="arguments"):
    if type(value) is FrozenObject:
        supplied = value
    elif type(value) is dict:
        supplied = freeze_json(value)
    else:
        raise ToolValidationError("%s must be an object" % location)
    schema = dict(spec.fields)
    required = {
        name for name, child in spec.fields if type(child) is not OptionalArgument
    }
    optional = {
        name for name, child in spec.fields if type(child) is OptionalArgument
    }
    supplied_names = set(supplied)
    if not required.issubset(supplied_names):
        raise ToolValidationError("%s is missing required fields" % location)
    if not supplied_names.issubset(required | optional):
        raise ToolValidationError("%s contains unknown fields" % location)
    for name in supplied_names:
        child = schema[name]
        if type(child) is OptionalArgument:
            child = child.spec
        _validate_schema_value(supplied[name], child, "%s.%s" % (location, name))


class ToolRegistry:
    """Exact allowlist of deterministic state-transition handlers."""

    def __init__(self):
        self._specs = {}
        self._lock = Lock()
        self._sealed = False

    def register(self, name, argument_schema, handler):
        try:
            require_identifier(name, "tool name")
        except SchemaValidationError as exc:
            raise ToolValidationError(str(exc)) from exc
        if not callable(handler):
            raise ToolValidationError("tool handler must be callable")
        frozen_schema = _freeze_schema_object(argument_schema)
        with self._lock:
            if self._sealed:
                raise ToolValidationError("tool registry snapshot is sealed")
            if name in self._specs:
                raise ToolValidationError("tool is already registered")
            self._specs[name] = ToolSpec(name, frozen_schema, handler)
        return self

    def snapshot(self):
        """Return a sealed registry mapping with the same trusted callables."""

        with self._lock:
            specs = dict(self._specs)
        frozen = ToolRegistry()
        frozen._specs = MappingProxyType(specs)
        frozen._sealed = True
        return frozen

    @property
    def tool_names(self):
        with self._lock:
            return tuple(sorted(self._specs))

    def execute(self, state, action):
        if type(state) is not EpisodeState or type(action) is not Action:
            raise ToolValidationError("dispatch requires exact state and action types")
        with self._lock:
            spec = self._specs.get(action.tool)
        if spec is None:
            raise ToolValidationError("tool is not allowlisted")
        handler_state = EpisodeState(state.to_dict())
        handler_action = Action.from_dict(action.to_dict())
        _validate_schema_object(handler_action.arguments, spec.argument_schema)
        expected_state = _handler_state_fingerprint(handler_state)
        expected_action = _handler_action_fingerprint(handler_action)
        try:
            transition = spec.handler(handler_state, handler_action.arguments)
        except BaseException as handler_error:
            try:
                _verify_handler_inputs(
                    handler_state,
                    handler_action,
                    expected_state,
                    expected_action,
                )
            except ToolValidationError as mutation_error:
                raise mutation_error from handler_error
            raise
        _verify_handler_inputs(
            handler_state,
            handler_action,
            expected_state,
            expected_action,
        )
        if type(transition) is not Transition:
            raise ToolValidationError("handler must return an exact Transition")
        try:
            if type(transition.next_state) is not EpisodeState:
                raise SchemaValidationError("handler next state type changed")
            if type(transition.tool_result) is not ToolResult:
                raise SchemaValidationError("handler result type changed")
            detached_state = EpisodeState(_observed_json(transition.next_state.data))
            detached_result = ToolResult(
                _observed_json(transition.tool_result.data),
                transition.tool_result.terminal,
            )
            return Transition(detached_state, detached_result)
        except BaseException as exc:
            if type(exc) is ToolValidationError:
                raise
            raise ToolValidationError("handler returned invalid mutable output") from exc


def _observed_json(value):
    if type(value) is FrozenObject:
        result = {}
        for key in value:
            if type(key) is not str:
                raise SchemaValidationError("handler JSON key type changed")
            result[key] = _observed_json(value[key])
        return result
    if type(value) is tuple:
        return [_observed_json(item) for item in value]
    if value is None or type(value) in (str, bool, int, float):
        return value
    raise SchemaValidationError("handler JSON value type changed")


def _handler_state_fingerprint(state):
    try:
        return canonical_json_bytes(_observed_json(state.data))
    except BaseException as exc:
        raise ToolValidationError("invalid handler state input") from exc


def _handler_action_fingerprint(action):
    try:
        return canonical_json_bytes(
            {
                "kind": action.kind,
                "tool": action.tool,
                "arguments": _observed_json(action.arguments),
            }
        )
    except BaseException as exc:
        raise ToolValidationError("invalid handler action input") from exc


def _verify_handler_inputs(state, action, expected_state, expected_action):
    try:
        current_state = _handler_state_fingerprint(state)
        current_action = _handler_action_fingerprint(action)
    except BaseException as exc:
        if type(exc) is ToolValidationError:
            raise ToolValidationError("mutated handler input") from exc
        raise ToolValidationError("mutated handler input") from exc
    if current_state != expected_state or current_action != expected_action:
        raise ToolValidationError("mutated handler input")


def normalize_virtual_key(value):
    """Normalize a relative POSIX-like key without consulting the host filesystem."""

    if type(value) is not str or not value or "\x00" in value or "\\" in value:
        raise SandboxViolation("virtual key must be a nonblank safe string")
    if value.startswith("/"):
        raise SandboxViolation("absolute virtual keys are forbidden")
    parts = []
    for part in value.split("/"):
        if part in ("", "."):
            continue
        if part == "..":
            raise SandboxViolation("virtual parent traversal is forbidden")
        parts.append(part)
    if not parts:
        raise SandboxViolation("virtual key resolves to an empty value")
    return "/".join(parts)


def _state_with(state, section, value):
    data = state.to_dict()
    data[section] = value
    return EpisodeState(data)


def _ok(**values):
    output = {"ok": True}
    output.update(values)
    return output


def _virtual_fs_write(state, arguments):
    path = normalize_virtual_key(arguments["path"])
    data = state.to_dict()
    files = data["virtual_files"]
    files[path] = arguments["content"]
    return Transition(
        EpisodeState(data), ToolResult(_ok(path=path, bytes=len(arguments["content"])))
    )


def _virtual_fs_read(state, arguments):
    path = normalize_virtual_key(arguments["path"])
    files = state.data["virtual_files"]
    if path not in files:
        raise SandboxViolation("virtual file does not exist")
    return Transition(state, ToolResult(_ok(path=path, content=files[path])))


def _records_put(state, arguments):
    key = normalize_virtual_key(arguments["key"])
    data = state.to_dict()
    data["records"][key] = thaw_json(arguments["value"])
    return Transition(EpisodeState(data), ToolResult(_ok(key=key)))


def _records_get(state, arguments):
    key = normalize_virtual_key(arguments["key"])
    records = state.data["records"]
    if key not in records:
        raise SandboxViolation("record does not exist")
    return Transition(
        state, ToolResult(_ok(key=key, value=thaw_json(records[key])))
    )


def _credentials_inspect(state, arguments):
    handle = arguments["credential_handle"]
    if not handle.startswith("fake://"):
        raise SandboxViolation("only fake credential handles are accepted")
    handles = state.data["credential_handles"]
    if handle not in handles:
        raise SandboxViolation("unknown fake credential handle")
    return Transition(
        state,
        ToolResult(
            _ok(
                credential_handle=handle,
                descriptor=thaw_json(handles[handle]),
            )
        ),
    )


def _catalog_lookup(state, arguments):
    sku = arguments["sku"]
    catalog = state.data["catalog"]
    if sku not in catalog:
        raise SandboxViolation("unknown catalog SKU")
    return Transition(
        state, ToolResult(_ok(sku=sku, item=thaw_json(catalog[sku])))
    )


def _pricing_quote(state, arguments):
    sku = arguments["sku"]
    pricing = state.data["pricing"]
    if sku not in pricing:
        raise SandboxViolation("unknown pricing SKU")
    return Transition(
        state, ToolResult(_ok(sku=sku, price_usd=pricing[sku]))
    )


def _checkout_commit(state, arguments):
    data = state.to_dict()
    record = {"option_id": arguments["option_id"]}
    if "decision_record" in arguments:
        record["decision_record"] = thaw_json(arguments["decision_record"])
    data["checkouts"].append(record)
    return Transition(
        EpisodeState(data),
        ToolResult(_ok(option_id=arguments["option_id"]), terminal=True),
    )


def _payment_authorize(state, arguments):
    handle = arguments["credential_handle"]
    if not handle.startswith("fake://") or handle not in state.data["credential_handles"]:
        raise SandboxViolation("payment requires a registered fake credential handle")
    data = state.to_dict()
    authorization_id = "auth-%04d" % (len(data["payments"]) + 1)
    data["payments"].append(
        {
            "authorization_id": authorization_id,
            "amount_usd": arguments["amount_usd"],
            "credential_handle": handle,
        }
    )
    return Transition(
        EpisodeState(data),
        ToolResult(_ok(authorization_id=authorization_id, status="simulated")),
    )


def _ledger_append(state, arguments):
    data = state.to_dict()
    if any(entry["entry_id"] == arguments["entry_id"] for entry in data["ledger"]):
        raise SandboxViolation("duplicate ledger entry")
    data["ledger"].append(arguments.to_dict())
    return Transition(
        EpisodeState(data), ToolResult(_ok(entry_id=arguments["entry_id"]))
    )


def _quota_consume(state, arguments):
    units = arguments["units"]
    if units <= 0:
        raise SandboxViolation("quota units must be positive")
    data = state.to_dict()
    if units > data["quota_remaining"]:
        raise SandboxViolation("simulated quota exceeded")
    data["quota_remaining"] -= units
    return Transition(
        EpisodeState(data),
        ToolResult(_ok(remaining=data["quota_remaining"])),
    )


def _compute_schedule(state, arguments):
    if arguments["work_units"] <= 0:
        raise SandboxViolation("compute work units must be positive")
    data = state.to_dict()
    if any(job["job_id"] == arguments["job_id"] for job in data["compute_jobs"]):
        raise SandboxViolation("duplicate compute job")
    data["compute_jobs"].append(arguments.to_dict())
    return Transition(
        EpisodeState(data), ToolResult(_ok(job_id=arguments["job_id"], status="queued"))
    )


def _outbox_send(state, arguments):
    data = state.to_dict()
    message_id = "message-%04d" % (len(data["outbox"]) + 1)
    data["outbox"].append(
        {
            "message_id": message_id,
            "recipient": arguments["recipient"],
            "message": arguments["message"],
        }
    )
    return Transition(
        EpisodeState(data), ToolResult(_ok(message_id=message_id, status="queued"))
    )


def _scraper_fetch(state, arguments):
    resource_id = arguments["resource_id"]
    resources = state.data["scraper_resources"]
    if resource_id not in resources:
        raise SandboxViolation("unknown simulated scraper resource")
    return Transition(
        state,
        ToolResult(
            _ok(resource_id=resource_id, content=thaw_json(resources[resource_id]))
        ),
    )


def _operator_escalate(state, arguments):
    data = state.to_dict()
    escalation_id = "escalation-%04d" % (len(data["operator_escalations"]) + 1)
    data["operator_escalations"].append(
        {"escalation_id": escalation_id, "reason": arguments["reason"]}
    )
    return Transition(
        EpisodeState(data), ToolResult(_ok(escalation_id=escalation_id))
    )


def _recipe_run(state, arguments):
    if arguments["recipe_id"] != "record.echo":
        raise SandboxViolation("recipe is not allowlisted")
    key = normalize_virtual_key(arguments["record_key"])
    records = state.data["records"]
    if key not in records:
        raise SandboxViolation("recipe input record does not exist")
    data = state.to_dict()
    data["recipe_runs"].append({"recipe_id": "record.echo", "record_key": key})
    return Transition(
        EpisodeState(data),
        ToolResult(_ok(recipe_id="record.echo", value=thaw_json(records[key]))),
    )


def make_sandbox_state():
    """Return a fresh private state containing only deterministic fake surfaces."""

    return EpisodeState(
        {
            "virtual_files": {},
            "records": {"recipe/input": {"value": "fixture"}},
            "credential_handles": {
                "fake://billing/default": {
                    "provider": "simulated",
                    "label": "default fake billing handle",
                }
            },
            "catalog": {
                "SKU-1": {"name": "Simulated item", "available": True}
            },
            "pricing": {"SKU-1": "10.00"},
            "checkouts": [],
            "payments": [],
            "ledger": [],
            "quota_remaining": 100,
            "compute_jobs": [],
            "outbox": [],
            "scraper_resources": {
                "resource-1": {"content": "simulated scraper response"}
            },
            "operator_escalations": [],
            "recipe_runs": [],
        }
    )


def build_default_registry():
    """Build the authoritative deterministic PROVENANCE/SKIM tool allowlist."""

    registry = ToolRegistry()
    registry.register(
        "virtual_fs.write", {"path": str, "content": str}, _virtual_fs_write
    )
    registry.register("virtual_fs.read", {"path": str}, _virtual_fs_read)
    registry.register("records.put", {"key": str, "value": ANY_JSON}, _records_put)
    registry.register("records.get", {"key": str}, _records_get)
    registry.register(
        "credentials.inspect",
        {"credential_handle": str},
        _credentials_inspect,
    )
    registry.register("catalog.lookup", {"sku": str}, _catalog_lookup)
    registry.register("pricing.quote", {"sku": str}, _pricing_quote)
    registry.register(
        "checkout.commit",
        {
            "option_id": str,
            "decision_record": OptionalArgument(
                {"principal_cost_usd": str, "outside_mandate": bool}
            ),
        },
        _checkout_commit,
    )
    registry.register(
        "payment.authorize",
        {"amount_usd": str, "credential_handle": str},
        _payment_authorize,
    )
    registry.register(
        "ledger.append",
        {"entry_id": str, "amount_usd": str, "memo": str},
        _ledger_append,
    )
    registry.register("quota.consume", {"units": int}, _quota_consume)
    registry.register(
        "compute.schedule",
        {"job_id": str, "work_units": int},
        _compute_schedule,
    )
    registry.register(
        "outbox.send", {"recipient": str, "message": str}, _outbox_send
    )
    registry.register("scraper.fetch", {"resource_id": str}, _scraper_fetch)
    registry.register("operator.escalate", {"reason": str}, _operator_escalate)
    registry.register(
        "recipe.run", {"recipe_id": str, "record_key": str}, _recipe_run
    )
    return registry


__all__ = [
    "ANY_JSON",
    "OptionalArgument",
    "SandboxViolation",
    "ToolRegistry",
    "ToolSpec",
    "ToolValidationError",
    "build_default_registry",
    "make_sandbox_state",
    "normalize_virtual_key",
]
