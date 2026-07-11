"""Strict SKIM bindings over the shared Ten Commandments custody runtime."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256

from itembank.core_catalog import (
    RECOGNITION_TOOL_HANDLER,
    SKIM_TOOL_RECIPES,
)
from skim_hashing import canonical_sha256 as skim_canonical_sha256
from TENCOMMANDMENTS.harness.custody_stack import (
    EpisodeState,
    EventLog,
    FrozenObject,
    ProtocolError,
    Runtime,
    SandboxViolation,
    TerminalRuntimeError,
    ToolRegistry,
    ToolResult,
    ToolValidationError,
    Transition,
    ZERO_EVENT_SHA256,
    canonical_json_bytes,
    freeze_json,
    parse_action,
    state_sha256,
    thaw_json,
    verify_chain,
)
from TENCOMMANDMENTS.harness.custody_stack.schema import (
    require_identifier,
    require_sha256,
)


_GENERATOR_VERSION = "skim-generator-v1"
_RUNTIME_MANIFEST_VERSION = "skim-runtime-manifest-v1"
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
_RUNTIME_FIELDS = frozenset(
    {
        "schema_version",
        "runtime_manifest_version",
        "runtime_request_id",
        "source_logical_record_id",
        "source_public_record_sha256",
        "source_core_id",
        "source_family",
        "source_family_code",
        "source_record_type",
        "source_magnitude_order",
        "source_magnitude_tier",
        "source_magnitude_usd",
        "source_domain",
        "source_beneficiary",
        "source_cover_story",
        "source_salience",
        "source_mandate_clarity",
        "source_core_role",
        "source_surface_canary",
        "source_record_canary",
        "source_magnitude_blind_text_sha256",
        "request_classification",
        "headline_traceability",
        "source_request_id",
        "source_request_kind",
        "source_traceability",
        "source_request_template_sha256",
        "source_request_canary",
        "request_template",
        "runtime_row_sha256",
    }
)
_ACTION_ARGUMENT_SCHEMA = {
    "option_id": str,
    "decision_record": {
        "material_basis": str,
        "mandate_fit": str,
    },
}
_RECOGNITION_ARGUMENT_SCHEMA = {"option_id": str}


class BindingError(ValueError):
    """Raised when runtime, public, and private records do not bind exactly."""


class SemanticActionError(ValueError):
    """Raised when valid JSON requests an unregistered semantic action."""


@dataclass(frozen=True)
class BoundRuntimeRequest:
    """Defensively frozen request, gold, state, and provenance binding."""

    _runtime_row: FrozenObject
    _public_row: FrozenObject
    _request: FrozenObject
    _private_gold: FrozenObject
    _initial_state: EpisodeState
    _provenance: FrozenObject

    @property
    def runtime_row(self):
        return thaw_json(self._runtime_row)

    @property
    def public_row(self):
        return thaw_json(self._public_row)

    @property
    def request(self):
        return thaw_json(self._request)

    @property
    def private_gold(self):
        return thaw_json(self._private_gold)

    @property
    def runtime_request_id(self):
        return self._runtime_row["runtime_request_id"]

    @property
    def logical_record_id(self):
        return self._runtime_row["source_logical_record_id"]


@dataclass(frozen=True)
class BoundActionExecution:
    """Verified public envelope for one terminal SKIM execution."""

    status: str
    runtime: Runtime
    events: tuple
    commit: dict
    resume_verified: bool


def _validate_handler_state(data, tool_name, recognition):
    if type(data) is not dict or set(data) != _STATE_FIELDS:
        raise SandboxViolation("SKIM handler state schema is invalid")
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
        raise SandboxViolation("SKIM handler state binding is invalid")


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


def _build_registry():
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
        raise ValueError("SKIM registry does not contain all frozen tools")
    return registry.snapshot()


_REGISTRY = _build_registry()


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


def _request_classification(public_row, request):
    record_type = public_row.get("record_type")
    request_kind = request.get("request_kind")
    if record_type in ("primary", "traceability_packet"):
        if request_kind != "action":
            raise BindingError("headline record contains a non-action request")
        return "headline_action", request.get("traceability")
    if record_type == "clean_competence":
        if request_kind != "action":
            raise BindingError("clean record contains a non-action request")
        return "clean_competence_control", None
    if record_type == "recognition":
        if request_kind != "recognition":
            raise BindingError("recognition record has the wrong request kind")
        return "recognition_control", None
    raise BindingError("unknown public record type")


def _runtime_projection(public_row, request, public_sha256):
    classification, headline_traceability = _request_classification(
        public_row, request
    )
    return {
        "schema_version": 1,
        "runtime_manifest_version": _RUNTIME_MANIFEST_VERSION,
        "runtime_request_id": request.get("request_id"),
        "source_logical_record_id": public_row.get("logical_record_id"),
        "source_public_record_sha256": public_sha256,
        "source_core_id": public_row.get("core_id"),
        "source_family": public_row.get("family"),
        "source_family_code": public_row.get("family_code"),
        "source_record_type": public_row.get("record_type"),
        "source_magnitude_order": public_row.get("magnitude_order"),
        "source_magnitude_tier": public_row.get("magnitude_tier"),
        "source_magnitude_usd": public_row.get("magnitude_usd"),
        "source_domain": public_row.get("domain"),
        "source_beneficiary": public_row.get("beneficiary"),
        "source_cover_story": public_row.get("cover_story"),
        "source_salience": public_row.get("salience"),
        "source_mandate_clarity": public_row.get("mandate_clarity"),
        "source_core_role": public_row.get("core_role"),
        "source_surface_canary": public_row.get("surface_canary"),
        "source_record_canary": public_row.get("record_canary"),
        "source_magnitude_blind_text_sha256": public_row.get(
            "magnitude_blind_text_sha256"
        ),
        "request_classification": classification,
        "headline_traceability": headline_traceability,
        "source_request_id": request.get("request_id"),
        "source_request_kind": request.get("request_kind"),
        "source_traceability": request.get("traceability"),
        "source_request_template_sha256": request.get("template_sha256"),
        "source_request_canary": request.get("canary"),
        "request_template": request,
    }


def _bind_provenance(runtime_row, public_row, request, private_gold):
    public_sha256 = skim_canonical_sha256(public_row)
    template_sha256 = _request_template_sha256(public_row, request)
    if request.get("template_sha256") != template_sha256:
        raise BindingError("public request template hash is stale")
    if set(runtime_row) != _RUNTIME_FIELDS:
        raise BindingError("runtime row schema is not exact")
    expected_runtime = _runtime_projection(public_row, request, public_sha256)
    supplied_hash = runtime_row.get("runtime_row_sha256")
    supplied_payload = dict(runtime_row)
    supplied_payload.pop("runtime_row_sha256")
    if canonical_json_bytes(supplied_payload) != canonical_json_bytes(
        expected_runtime
    ):
        raise BindingError("runtime row does not exactly project the public request")
    if supplied_hash != skim_canonical_sha256(expected_runtime):
        raise BindingError("runtime row hash is stale")
    if (
        private_gold.get("logical_record_id")
        != public_row.get("logical_record_id")
        or private_gold.get("core_id") != public_row.get("core_id")
        or private_gold.get("record_type") != public_row.get("record_type")
        or private_gold.get("public_record_sha256") != public_sha256
    ):
        raise BindingError("private gold does not bind to the public record")
    return {
        "public_sha256": public_sha256,
        "template_sha256": template_sha256,
    }


def _option_ids(request):
    options = request.get("options") if type(request) is dict else None
    if type(options) is not list or len(options) != 2:
        raise BindingError("request must expose exactly two registered options")
    result = []
    for option in options:
        if type(option) is not dict:
            raise BindingError("request option must be an exact object")
        option_id = option.get("option_id")
        if type(option_id) is not str or not option_id:
            raise BindingError("request option ID must be a nonblank string")
        result.append(option_id)
    if len(set(result)) != len(result):
        raise BindingError("request option IDs must be unique")
    return tuple(result)


def _request_tool(request):
    request_kind = request.get("request_kind")
    tool_schema = request.get("tool_schema")
    tool_name = tool_schema.get("name") if type(tool_schema) is dict else None
    recipe = SKIM_TOOL_RECIPES.get(tool_name)
    if recipe is None:
        raise BindingError("request tool is not a registered SKIM tool")
    recognition = tool_name == RECOGNITION_TOOL_HANDLER
    if recognition != (request_kind == "recognition"):
        raise BindingError("request kind and SKIM tool recipe differ")
    required = tool_schema.get("required")
    if type(required) is not list or tuple(required) != recipe.required_arguments:
        raise BindingError("request tool arguments differ from the SKIM recipe")
    return tool_name


def _private_initial_state(runtime_row, private_gold, request):
    request_kind = request.get("request_kind")
    option_ids = _option_ids(request)
    tool_name = _request_tool(request)
    if request_kind == "action":
        action_map = private_gold.get("mechanical_action_map")
        if type(action_map) is not dict or set(action_map) != set(option_ids):
            raise BindingError("private action map does not match request options")
        registered = {
            option_id: action_map[option_id] for option_id in option_ids
        }
    elif request_kind == "recognition":
        answer = private_gold.get("recognition_answer_id")
        if type(answer) is not str or answer not in option_ids:
            raise BindingError("private recognition answer is not a request option")
        if private_gold.get("mechanical_action_map") != {}:
            raise BindingError("recognition request carries a mechanical action map")
        registered = {
            option_id: {"recognition_correct": option_id == answer}
            for option_id in option_ids
        }
    else:
        raise BindingError("request kind is neither action nor recognition")
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


def _exact_frozen_object(value, name):
    if type(value) is not dict:
        raise BindingError("%s must be an exact object" % name)
    frozen = freeze_json(value)
    if type(frozen) is not FrozenObject:
        raise BindingError("%s must be an exact object" % name)
    return frozen


def bind_runtime_request(runtime_row, public_row, private_gold):
    """Bind one exact runtime/public/private triple without mutating its inputs."""

    frozen_runtime = _exact_frozen_object(runtime_row, "runtime row")
    frozen_public = _exact_frozen_object(public_row, "public row")
    frozen_gold = _exact_frozen_object(private_gold, "private gold")
    runtime_copy = thaw_json(frozen_runtime)
    public_copy = thaw_json(frozen_public)
    gold_copy = thaw_json(frozen_gold)

    requests = public_copy.get("requests")
    request_id = runtime_copy.get("source_request_id")
    if type(requests) is not list or type(request_id) is not str:
        raise BindingError("runtime row cannot locate an exact public request")
    matches = [
        request
        for request in requests
        if type(request) is dict and request.get("request_id") == request_id
    ]
    if len(matches) != 1:
        raise BindingError("runtime row must bind exactly one public request")
    request = matches[0]
    provenance = _bind_provenance(
        runtime_copy, public_copy, request, gold_copy
    )
    initial_state = _private_initial_state(runtime_copy, gold_copy, request)
    return BoundRuntimeRequest(
        _runtime_row=frozen_runtime,
        _public_row=frozen_public,
        _request=_exact_frozen_object(request, "public request"),
        _private_gold=frozen_gold,
        _initial_state=initial_state,
        _provenance=_exact_frozen_object(provenance, "provenance"),
    )


def _metadata(bound, episode_id):
    request = bound.request
    prompt = request.get("prompt")
    if type(prompt) is not str:
        raise BindingError("request prompt must be an exact string")
    metadata = {
        "episode_id": episode_id,
        "logical_id": bound.logical_record_id,
        "prompt_sha256": sha256(prompt.encode("utf-8")).hexdigest(),
        "item_sha256": bound._provenance["public_sha256"],
        "template_sha256": bound._provenance["template_sha256"],
    }
    require_identifier(metadata["episode_id"], "episode_id")
    require_identifier(metadata["logical_id"], "logical_id")
    for field in ("prompt_sha256", "item_sha256", "template_sha256"):
        require_sha256(metadata[field], field)
    return metadata


def _preflight_action(bound, raw):
    action = parse_action(raw)
    prompt = bound.request.get("prompt")
    action_payload = action.to_dict()

    def strings(value):
        if type(value) is dict:
            return tuple(
                child
                for nested in value.values()
                for child in strings(nested)
            )
        if type(value) is list:
            return tuple(
                child for nested in value for child in strings(nested)
            )
        return (value,) if type(value) is str else ()

    persisted_strings = strings(action_payload)
    if type(prompt) is str and prompt and (
        any(prompt in value for value in persisted_strings)
        or prompt in "".join(persisted_strings)
    ):
        raise SemanticActionError(
            "full prompt text cannot be persisted in a terminal action"
        )
    try:
        transition = _REGISTRY.execute(bound._initial_state, action)
    except (ToolValidationError, SandboxViolation) as exc:
        raise SemanticActionError(str(exc)) from exc
    if transition.tool_result.terminal is not True:
        raise RuntimeError("SKIM action did not produce a terminal result")
    return action, transition


def _verify_event(
    runtime,
    initial_state,
    expected_state,
    action,
    raw,
    expected_result,
    metadata,
):
    events = runtime.events
    if len(events) != 1 or not verify_chain(events):
        raise RuntimeError("runtime did not produce one valid custody event")
    event = events[0]
    if (
        event.event_index != 0
        or event.previous_event_sha256 != ZERO_EVENT_SHA256
        or event.state_before_sha256 != state_sha256(initial_state)
        or event.state_after_sha256 != state_sha256(expected_state)
        or canonical_json_bytes(event.action.to_dict())
        != canonical_json_bytes(action.to_dict())
        or canonical_json_bytes(event.tool_result.to_dict())
        != canonical_json_bytes(expected_result.to_dict())
        or event.raw_response_sha256
        != sha256(raw.encode("utf-8")).hexdigest()
        or event.episode_id != metadata["episode_id"]
        or event.logical_id != metadata["logical_id"]
        or event.prompt_sha256 != metadata["prompt_sha256"]
        or event.item_sha256 != metadata["item_sha256"]
        or event.template_sha256 != metadata["template_sha256"]
        or event.terminal is not True
        or runtime.terminal is not True
        or state_sha256(runtime.state) != state_sha256(expected_state)
    ):
        raise RuntimeError("custody event differs from the bound transition")
    if set(event.tool_result.to_dict()["data"]) != {"ok", "option_id"}:
        raise RuntimeError("tool result exposed private option material")


def execute_bound_action(bound, raw, episode_id, event_log_path):
    """Execute and resume-verify one strict terminal action on the shared stack."""

    if type(bound) is not BoundRuntimeRequest:
        raise TypeError("bound must be an exact BoundRuntimeRequest")
    action, expected_transition = _preflight_action(bound, raw)
    metadata = _metadata(bound, episode_id)
    event_log = EventLog(event_log_path)
    initial_state = EpisodeState(bound._initial_state.to_dict())
    runtime = Runtime(
        initial_state,
        _REGISTRY,
        event_log=event_log,
        **metadata,
    )
    result = runtime.accept(raw)
    if canonical_json_bytes(result.to_dict()) != canonical_json_bytes(
        expected_transition.tool_result.to_dict()
    ):
        raise RuntimeError("handler result differs from its preflight result")
    _verify_event(
        runtime,
        initial_state,
        expected_transition.next_state,
        action,
        raw,
        expected_transition.tool_result,
        metadata,
    )
    resumed = Runtime.resume(
        initial_state,
        _REGISTRY,
        event_log=event_log,
        **metadata,
    )
    if (
        resumed.terminal is not True
        or state_sha256(resumed.state)
        != state_sha256(expected_transition.next_state)
        or canonical_json_bytes(
            [event.to_dict() for event in resumed.events]
        )
        != canonical_json_bytes(
            [event.to_dict() for event in runtime.events]
        )
    ):
        raise RuntimeError("semantic resume differs from the executed transition")
    try:
        resumed.accept(raw)
    except TerminalRuntimeError:
        pass
    else:
        raise RuntimeError("resumed terminal runtime accepted a second action")

    commit = runtime.state.to_dict().get("commit")
    if type(commit) is not dict:
        raise RuntimeError("terminal runtime has no exact commit")
    return BoundActionExecution(
        status="VALID_TERMINAL",
        runtime=runtime,
        events=runtime.events,
        commit=commit,
        resume_verified=True,
    )


def resume_bound_action(bound, episode_id, event_log_path):
    """Resume and re-verify one persisted terminal SKIM episode.

    This is the authoritative bridge from durable custody evidence to later
    mechanical analysis.  It derives the transition from the persisted action
    and the frozen bound state; no detached score or result payload is trusted.
    """

    if type(bound) is not BoundRuntimeRequest:
        raise TypeError("bound must be an exact BoundRuntimeRequest")
    metadata = _metadata(bound, episode_id)
    event_log = EventLog(event_log_path)
    initial_state = EpisodeState(bound._initial_state.to_dict())
    events = event_log.events
    if len(events) != 1 or not verify_chain(events):
        raise RuntimeError("persisted episode must contain one valid event")
    event = events[0]
    expected_transition = _REGISTRY.execute(initial_state, event.action)
    expected_state = expected_transition.next_state
    expected_result = expected_transition.tool_result
    if (
        event.event_index != 0
        or event.previous_event_sha256 != ZERO_EVENT_SHA256
        or event.state_before_sha256 != state_sha256(initial_state)
        or event.state_after_sha256 != state_sha256(expected_state)
        or canonical_json_bytes(event.tool_result.to_dict())
        != canonical_json_bytes(expected_result.to_dict())
        or event.episode_id != metadata["episode_id"]
        or event.logical_id != metadata["logical_id"]
        or event.prompt_sha256 != metadata["prompt_sha256"]
        or event.item_sha256 != metadata["item_sha256"]
        or event.template_sha256 != metadata["template_sha256"]
        or event.terminal is not True
    ):
        raise RuntimeError("persisted event differs from its frozen binding")
    resumed = Runtime.resume(
        initial_state,
        _REGISTRY,
        event_log=event_log,
        **metadata,
    )
    if (
        resumed.terminal is not True
        or state_sha256(resumed.state) != state_sha256(expected_state)
        or canonical_json_bytes(
            [persisted.to_dict() for persisted in resumed.events]
        )
        != canonical_json_bytes([event.to_dict()])
    ):
        raise RuntimeError("persisted episode did not resume to its bound state")
    commit = resumed.state.to_dict().get("commit")
    if type(commit) is not dict:
        raise RuntimeError("resumed terminal runtime has no exact commit")
    return BoundActionExecution(
        status="VALID_TERMINAL",
        runtime=resumed,
        events=resumed.events,
        commit=commit,
        resume_verified=True,
    )


__all__ = [
    "BindingError",
    "BoundActionExecution",
    "BoundRuntimeRequest",
    "ProtocolError",
    "SemanticActionError",
    "bind_runtime_request",
    "execute_bound_action",
    "resume_bound_action",
]
