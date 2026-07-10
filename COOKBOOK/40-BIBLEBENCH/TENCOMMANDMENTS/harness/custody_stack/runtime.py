"""Append-before-swap custody runtime with deterministic replay and resume."""

from dataclasses import dataclass
from hashlib import sha256
from threading import Lock

from .event_log import EventLog, EventLogError, verify_chain
from .protocol import parse_action
from .sandbox import ToolRegistry
from .schema import (
    CustodyError,
    EVENT_SCHEMA_VERSION,
    EpisodeState,
    Event,
    FORBIDDEN_PERSISTED_FIELD_NAMES,
    SchemaValidationError,
    ZERO_EVENT_SHA256,
    canonical_json_bytes,
    require_identifier,
    require_sha256,
    state_sha256,
)


EMPTY_SHA256 = sha256(b"").hexdigest()


class ReplayError(CustodyError, ValueError):
    """Raised when deterministic replay differs from persisted custody evidence."""


class TerminalRuntimeError(CustodyError, RuntimeError):
    """Raised when an action is offered after a terminal transition."""


class RuntimeStateError(CustodyError, RuntimeError):
    """Raised when a shared log has advanced beyond this runtime's private state."""


@dataclass(frozen=True)
class _RuntimeSnapshot:
    state: EpisodeState
    terminal: bool
    event_count: int
    event_head_sha256: str


def _all_strings(value):
    if type(value) is str:
        return (value,)
    if type(value) is dict:
        strings = []
        for key, child in value.items():
            strings.append(key)
            strings.extend(_all_strings(child))
        return tuple(strings)
    if type(value) is list:
        strings = []
        for child in value:
            strings.extend(_all_strings(child))
        return tuple(strings)
    return ()


def _private_strings(value):
    if type(value) is list:
        secrets = []
        for child in value:
            secrets.extend(_private_strings(child))
        return tuple(secrets)
    if type(value) is not dict:
        return ()
    secrets = []
    for key, child in value.items():
        if key in FORBIDDEN_PERSISTED_FIELD_NAMES:
            secrets.extend(item for item in _all_strings(child) if item)
        else:
            secrets.extend(_private_strings(child))
    return tuple(secrets)


def _reject_private_material(states, action, tool_result):
    secrets = []
    for state in states:
        secrets.extend(_private_strings(state.to_dict()))
    if not secrets:
        return
    persisted_strings = _all_strings(action.to_dict()) + _all_strings(
        tool_result.to_dict()
    )
    if any(secret in candidate for secret in secrets for candidate in persisted_strings):
        raise SchemaValidationError("private material cannot be persisted")


def _validated_metadata(
    episode_id,
    logical_id,
    prompt_sha256,
    item_sha256,
    template_sha256,
    error_type=SchemaValidationError,
):
    try:
        require_identifier(episode_id, "episode_id")
        require_identifier(logical_id, "logical_id")
        require_sha256(prompt_sha256, "prompt_sha256")
        require_sha256(item_sha256, "item_sha256")
        require_sha256(template_sha256, "template_sha256")
    except SchemaValidationError as exc:
        raise error_type(str(exc)) from exc
    return (
        episode_id,
        logical_id,
        prompt_sha256,
        item_sha256,
        template_sha256,
    )


class Runtime:
    """Execute exact allowlisted actions against one private episode state."""

    def __init__(
        self,
        initial_state,
        handlers,
        event_log=None,
        episode_id="episode",
        logical_id="logical",
        prompt_sha256=EMPTY_SHA256,
        item_sha256=EMPTY_SHA256,
        template_sha256=EMPTY_SHA256,
    ):
        if type(initial_state) is not EpisodeState:
            raise SchemaValidationError("initial_state must be an exact EpisodeState")
        if type(handlers) is not ToolRegistry:
            raise SchemaValidationError("handlers must be an exact ToolRegistry")
        if event_log is None:
            event_log = EventLog()
        if type(event_log) is not EventLog:
            raise SchemaValidationError("event_log must be an exact EventLog")
        try:
            live_head = event_log.live_head()
        except EventLogError as exc:
            raise SchemaValidationError("unable to verify initial event-log head") from exc
        if event_log.events or live_head != (0, ZERO_EVENT_SHA256):
            raise SchemaValidationError("nonempty logs must be opened with Runtime.resume")
        metadata = _validated_metadata(
            episode_id,
            logical_id,
            prompt_sha256,
            item_sha256,
            template_sha256,
        )
        self._publication_lock = Lock()
        self._snapshot = _RuntimeSnapshot(
            initial_state, False, 0, ZERO_EVENT_SHA256
        )
        self._handlers = handlers
        self._event_log = event_log
        (
            self._episode_id,
            self._logical_id,
            self._prompt_sha256,
            self._item_sha256,
            self._template_sha256,
        ) = metadata

    @property
    def state(self):
        with self._publication_lock:
            return self._snapshot.state

    @property
    def events(self):
        return self._event_log.events

    @property
    def event_log(self):
        return self._event_log

    @property
    def terminal(self):
        with self._publication_lock:
            return self._snapshot.terminal

    def _published_snapshot(self):
        with self._publication_lock:
            snapshot = self._snapshot
            return (
                snapshot.state,
                snapshot.terminal,
                (
                    snapshot.event_count,
                    snapshot.event_head_sha256,
                ),
            )

    def _capture_accept_snapshot(self):
        with self._publication_lock:
            snapshot = self._snapshot
            if snapshot.terminal:
                raise TerminalRuntimeError("runtime is already terminal")
            return (
                snapshot.state,
                (
                    snapshot.event_count,
                    snapshot.event_head_sha256,
                ),
                (
                    self._episode_id,
                    self._logical_id,
                    self._prompt_sha256,
                    self._item_sha256,
                    self._template_sha256,
                ),
            )

    @staticmethod
    def _next_snapshot(expected_generation, event, transition):
        return _RuntimeSnapshot(
            transition.next_state,
            transition.tool_result.terminal,
            expected_generation[0] + 1,
            event.event_sha256,
        )

    def _publish_transition(
        self, starting_state, expected_generation, event, transition
    ):
        with self._publication_lock:
            snapshot = self._snapshot
            current_generation = (
                snapshot.event_count,
                snapshot.event_head_sha256,
            )
            if (
                snapshot.terminal
                or snapshot.state is not starting_state
                or current_generation != expected_generation
            ):
                raise RuntimeStateError(
                    "runtime publication diverged after event-log append"
                )
            self._snapshot = self._next_snapshot(
                expected_generation, event, transition
            )

    def _reconcile_committed_transition(
        self, starting_state, expected_generation, event, transition
    ):
        intended = self._next_snapshot(expected_generation, event, transition)
        with self._publication_lock:
            snapshot = self._snapshot
            current_generation = (
                snapshot.event_count,
                snapshot.event_head_sha256,
            )
            if (
                snapshot.state is starting_state
                and not snapshot.terminal
                and current_generation == expected_generation
            ):
                self._snapshot = intended
                return
            if snapshot == intended:
                return
            raise RuntimeStateError(
                "committed event cannot be reconciled with runtime publication"
            )

    def _assert_expected_log_head(self, expected_generation):
        try:
            live_head = self._event_log.live_head()
        except EventLogError as exc:
            raise RuntimeStateError("unable to verify live event-log head") from exc
        if live_head != expected_generation:
            raise RuntimeStateError("event log generation changed outside this runtime")

    def accept(self, raw_response):
        """Validate, simulate, durably append, and only then swap runtime state."""

        (
            starting_state,
            expected_generation,
            provenance_metadata,
        ) = self._capture_accept_snapshot()
        self._assert_expected_log_head(expected_generation)
        before_sha256 = state_sha256(starting_state)
        existing_events = self._event_log.events
        if existing_events:
            last_event = existing_events[-1]
            if last_event.terminal:
                raise TerminalRuntimeError("event log is already terminal")
            if last_event.state_after_sha256 != before_sha256:
                raise RuntimeStateError("event log advanced beyond runtime state")
            if (
                last_event.episode_id,
                last_event.logical_id,
                last_event.prompt_sha256,
                last_event.item_sha256,
                last_event.template_sha256,
            ) != provenance_metadata:
                raise RuntimeStateError("event log belongs to different provenance metadata")
        action = parse_action(raw_response)
        raw_response_sha256 = sha256(raw_response.encode("utf-8")).hexdigest()
        transition = self._handlers.execute(starting_state, action)
        _reject_private_material(
            (starting_state, transition.next_state), action, transition.tool_result
        )
        after_sha256 = state_sha256(transition.next_state)
        (
            episode_id,
            logical_id,
            prompt_sha256,
            item_sha256,
            template_sha256,
        ) = provenance_metadata
        event = Event.create(
            schema_version=EVENT_SCHEMA_VERSION,
            event_index=expected_generation[0],
            episode_id=episode_id,
            logical_id=logical_id,
            previous_event_sha256=expected_generation[1],
            state_before_sha256=before_sha256,
            state_after_sha256=after_sha256,
            action=action,
            tool_result=transition.tool_result,
            raw_response_sha256=raw_response_sha256,
            prompt_sha256=prompt_sha256,
            item_sha256=item_sha256,
            template_sha256=template_sha256,
            terminal=transition.tool_result.terminal,
        )
        try:
            self._event_log.append(event, expected_generation=expected_generation)
            self._publish_transition(
                starting_state, expected_generation, event, transition
            )
        except BaseException:
            if self._event_log._committed_event(event, expected_generation):
                self._reconcile_committed_transition(
                    starting_state, expected_generation, event, transition
                )
            raise
        return transition.tool_result

    @classmethod
    def resume(
        cls,
        initial_state,
        handlers,
        events=None,
        event_log=None,
        episode_id=None,
        logical_id=None,
        prompt_sha256=None,
        item_sha256=None,
        template_sha256=None,
    ):
        """Replay verified events from caller-supplied private state and resume."""

        if type(initial_state) is not EpisodeState:
            raise ReplayError("initial_state must be an exact EpisodeState")
        if type(handlers) is not ToolRegistry:
            raise ReplayError("handlers must be an exact ToolRegistry")
        if events is not None and event_log is not None:
            raise ReplayError("provide events or event_log, not both")
        try:
            if event_log is not None:
                if type(event_log) is not EventLog:
                    raise ReplayError("event_log must be an exact EventLog")
                log = event_log
            else:
                if events is None:
                    events = ()
                log = EventLog(events=events)
        except EventLogError as exc:
            raise ReplayError("event chain is structurally invalid") from exc
        persisted = log.events
        if not verify_chain(persisted):
            raise ReplayError("event chain is structurally invalid")
        expected_head = (
            len(persisted),
            persisted[-1].event_sha256 if persisted else ZERO_EVENT_SHA256,
        )
        try:
            live_head = log.live_head()
        except EventLogError as exc:
            raise ReplayError("unable to verify current event-log head") from exc
        if live_head != expected_head:
            raise ReplayError("event log changed before replay could bind its head")

        supplied_metadata = (
            episode_id,
            logical_id,
            prompt_sha256,
            item_sha256,
            template_sha256,
        )
        if persisted:
            first = persisted[0]
            stored_metadata = (
                first.episode_id,
                first.logical_id,
                first.prompt_sha256,
                first.item_sha256,
                first.template_sha256,
            )
            effective = tuple(
                stored if supplied is None else supplied
                for supplied, stored in zip(supplied_metadata, stored_metadata)
            )
            _validated_metadata(*effective, error_type=ReplayError)
            if effective != stored_metadata:
                raise ReplayError("resume metadata does not match persisted metadata")
        else:
            defaults = ("episode", "logical", EMPTY_SHA256, EMPTY_SHA256, EMPTY_SHA256)
            effective = tuple(
                default if supplied is None else supplied
                for supplied, default in zip(supplied_metadata, defaults)
            )
            _validated_metadata(*effective, error_type=ReplayError)

        state = initial_state
        terminal = False
        for event in persisted:
            if terminal:
                raise ReplayError("event appears after a terminal transition")
            if (
                event.episode_id,
                event.logical_id,
                event.prompt_sha256,
                event.item_sha256,
                event.template_sha256,
            ) != effective:
                raise ReplayError("event provenance metadata changed within the chain")
            if event.state_before_sha256 != state_sha256(state):
                raise ReplayError("state-before hash mismatch")
            try:
                transition = handlers.execute(state, event.action)
            except Exception as exc:
                raise ReplayError("deterministic handler replay failed") from exc
            try:
                _reject_private_material(
                    (state, transition.next_state), event.action, event.tool_result
                )
            except SchemaValidationError as exc:
                raise ReplayError("persisted event contains private material") from exc
            if canonical_json_bytes(transition.tool_result.to_dict()) != canonical_json_bytes(
                event.tool_result.to_dict()
            ):
                raise ReplayError("stored tool result differs from deterministic replay")
            if state_sha256(transition.next_state) != event.state_after_sha256:
                raise ReplayError("state-after hash differs from deterministic replay")
            if transition.tool_result.terminal != event.terminal:
                raise ReplayError("stored terminal semantics differ from replay")
            state = transition.next_state
            terminal = transition.tool_result.terminal

        runtime = cls.__new__(cls)
        runtime._publication_lock = Lock()
        runtime._snapshot = _RuntimeSnapshot(
            state, terminal, expected_head[0], expected_head[1]
        )
        runtime._handlers = handlers
        runtime._event_log = log
        (
            runtime._episode_id,
            runtime._logical_id,
            runtime._prompt_sha256,
            runtime._item_sha256,
            runtime._template_sha256,
        ) = effective
        return runtime


__all__ = [
    "EMPTY_SHA256",
    "ReplayError",
    "Runtime",
    "RuntimeStateError",
    "TerminalRuntimeError",
]
