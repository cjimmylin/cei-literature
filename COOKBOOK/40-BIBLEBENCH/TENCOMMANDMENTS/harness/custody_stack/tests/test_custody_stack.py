"""Contract tests for the shared PROVENANCE/SKIM custody stack."""

from copy import deepcopy
from dataclasses import FrozenInstanceError, is_dataclass, replace
from decimal import Decimal
from fractions import Fraction
from hashlib import sha256
import importlib
import json
import os
from pathlib import Path
import stat
import threading

import pytest


ZERO_ROOT = "0" * 64
HASH_A = "a" * 64
HASH_B = "b" * 64
HASH_C = "c" * 64
FORBIDDEN_PERSISTED_FIELDS = {
    "prompt",
    "model_prompt",
    "api_key",
    "credential",
    "credential_secret",
}


def load_api():
    return importlib.import_module("TENCOMMANDMENTS.harness.custody_stack")


def fixture_state(api, count=0):
    return api.EpisodeState(
        {
            "counter": count,
            "private": {
                "prompt": "FULL PRIVATE PROMPT MUST NOT LEAK",
                "api_key": "sk-private-never-persist",
                "credential_secret": "private-credential-value",
            },
        }
    )


def fixture_handlers(api, calls=None):
    registry = api.ToolRegistry()

    def add(state, arguments):
        if calls is not None:
            calls.append("add")
        data = state.to_dict()
        data["counter"] += arguments["amount"]
        return api.Transition(
            next_state=api.EpisodeState(data),
            tool_result=api.ToolResult(
                data={"counter": data["counter"]}, terminal=False
            ),
        )

    def commit(state, arguments):
        if calls is not None:
            calls.append("commit")
        data = state.to_dict()
        data["committed_option"] = arguments["option_id"]
        return api.Transition(
            next_state=api.EpisodeState(data),
            tool_result=api.ToolResult(
                data={"committed_option": arguments["option_id"]}, terminal=True
            ),
        )

    registry.register("counter.add", {"amount": int}, add)
    registry.register("checkout.commit", {"option_id": str}, commit)
    return registry


def runtime_for(api, *, path=None, calls=None):
    log = api.EventLog(path=path)
    return api.Runtime(
        initial_state=fixture_state(api),
        handlers=fixture_handlers(api, calls),
        event_log=log,
        episode_id="episode-001",
        logical_id="logical-001",
        prompt_sha256=HASH_A,
        item_sha256=HASH_B,
        template_sha256=HASH_C,
    )


def rehashed_event(api, event, **updates):
    payload = event.to_dict()
    payload.update(updates)
    payload["event_sha256"] = api.compute_event_sha256(payload)
    return api.Event.from_dict(payload)


def nested_keys(value):
    if isinstance(value, dict):
        for key, item in value.items():
            yield key
            yield from nested_keys(item)
    elif isinstance(value, list):
        for item in value:
            yield from nested_keys(item)


def test_contract_module_exists_and_exports_shared_stack():
    api = load_api()
    expected = {
        "Action",
        "EpisodeState",
        "Event",
        "EventLog",
        "Runtime",
        "ToolRegistry",
        "ToolResult",
        "Transition",
        "build_default_registry",
        "canonical_json",
        "compute_event_sha256",
        "make_sandbox_state",
        "parse_action",
        "state_sha256",
        "verify_chain",
    }
    assert expected.issubset(set(api.__all__))


def test_schema_dataclasses_are_frozen_and_mutable_inputs_are_snapshotted():
    api = load_api()
    source = {"z": 1, "a": [True, None, {"x": "original"}]}
    state = api.EpisodeState(source)
    source["a"][2]["x"] = "mutated"
    action = api.Action("act", "counter.add", {"amount": 1})
    result = api.ToolResult({"counter": 1}, False)
    transition = api.Transition(state, result)
    runtime = api.Runtime(fixture_state(api), fixture_handlers(api))
    runtime.accept('{"kind":"act","tool":"counter.add","arguments":{"amount":1}}')
    event = runtime.events[0]

    assert state.to_dict()["a"][2]["x"] == "original"
    assert api.canonical_json(state.to_dict()) == (
        '{"a":[true,null,{"x":"original"}],"z":1}'
    )
    for value in (state, action, result, transition, event):
        assert is_dataclass(value)
        with pytest.raises(FrozenInstanceError):
            value.unexpected = True
    with pytest.raises(TypeError):
        state.data["z"] = 2
    with pytest.raises(TypeError):
        state.data._lookup["z"] = 2
    with pytest.raises(AttributeError):
        state.data._items = (("z", 2),)
    with pytest.raises(AttributeError):
        del state.data._items


class CustomInt(int):
    pass


class CustomFloat(float):
    pass


class CustomDict(dict):
    pass


@pytest.mark.parametrize(
    "bad_value",
    [
        Decimal("1.0"),
        Fraction(1, 2),
        CustomInt(1),
        CustomFloat(1.0),
        CustomDict(x=1),
        (1, 2),
        {1: "non-string-key"},
        2**53,
        -(2**53),
        float("nan"),
        float("inf"),
        object(),
    ],
)
def test_schema_rejects_nonexact_or_unsafe_json_values(bad_value):
    api = load_api()
    with pytest.raises(api.SchemaValidationError):
        api.EpisodeState({"value": bad_value})


def test_strict_action_parser_accepts_one_exact_nested_object():
    api = load_api()
    raw = (
        '{"kind":"act","tool":"checkout.commit","arguments":'
        '{"option_id":"A","decision_record":'
        '{"principal_cost_usd":"10.00","outside_mandate":false}}}'
    )
    action = api.parse_action(raw)
    assert action.to_dict() == json.loads(raw)


@pytest.mark.parametrize(
    "raw",
    [
        "[]",
        '"scalar"',
        "1",
        "null",
        '{"kind":"act","tool":"x","arguments":{}} trailing',
        '{"kind":"act","tool":"x","arguments":{"n":NaN}}',
        '{"kind":"act","tool":"x","arguments":{"n":Infinity}}',
        '{"kind":"act","kind":"act","tool":"x","arguments":{}}',
        '{"kind":"act","tool":"x","arguments":{"o":{"a":1,"a":2}}}',
        '{"kind":"act","tool":"x","arguments":{},"extra":true}',
        '{"kind":"act","tool":"x"}',
        '{"kind":"ACT","tool":"x","arguments":{}}',
        '{"kind":1,"tool":"x","arguments":{}}',
        '{"kind":"act","tool":1,"arguments":{}}',
        '{"kind":"act","tool":"x","arguments":[]}',
        '{"kind":"act","tool":"x","arguments":{"n":9007199254740992}}',
    ],
)
def test_strict_action_parser_rejects_noncanonical_protocol_shapes(raw):
    api = load_api()
    with pytest.raises(api.ProtocolError):
        api.parse_action(raw)


@pytest.mark.parametrize(
    "raw",
    [
        '{"kind":"act","tool":"unknown.tool","arguments":{}}',
        '{"kind":"act","tool":"counter.add","arguments":{}}',
        '{"kind":"act","tool":"counter.add","arguments":{"amount":true}}',
        '{"kind":"act","tool":"counter.add","arguments":{"amount":1,"x":2}}',
    ],
)
def test_unknown_or_invalid_tool_arguments_reject_before_handler_without_mutation(raw):
    api = load_api()
    calls = []
    runtime = runtime_for(api, calls=calls)
    before = runtime.state
    with pytest.raises(api.CustodyError):
        runtime.accept(raw)
    assert runtime.state == before
    assert runtime.events == ()
    assert runtime.terminal is False
    assert calls == []


def test_event_chain_uses_zero_root_monotone_indices_and_hashes_every_state():
    api = load_api()
    runtime = runtime_for(api)
    initial_hash = api.state_sha256(runtime.state)
    runtime.accept(
        '{"kind":"act","tool":"counter.add","arguments":{"amount":1}}'
    )
    runtime.accept(
        '{"kind":"act","tool":"counter.add","arguments":{"amount":2}}'
    )
    first, second = runtime.events

    assert [first.event_index, second.event_index] == [0, 1]
    assert first.previous_event_sha256 == ZERO_ROOT
    assert second.previous_event_sha256 == first.event_sha256
    assert first.state_before_sha256 == initial_hash
    assert first.state_after_sha256 == second.state_before_sha256
    assert second.state_after_sha256 == api.state_sha256(runtime.state)
    assert api.verify_chain(runtime.events) is True
    for event in runtime.events:
        payload = event.to_dict()
        stored = payload.pop("event_sha256")
        expected = sha256(api.canonical_json_bytes(payload)).hexdigest()
        assert stored == expected


def test_event_hash_excludes_only_event_sha256_and_schema_is_exact():
    api = load_api()
    runtime = runtime_for(api)
    runtime.accept(
        '{"kind":"act","tool":"counter.add","arguments":{"amount":1}}'
    )
    event = runtime.events[0]
    payload = event.to_dict()
    original = api.compute_event_sha256(payload)
    payload["event_sha256"] = "f" * 64
    assert api.compute_event_sha256(payload) == original
    payload["terminal"] = True
    assert api.compute_event_sha256(payload) != original
    assert set(event.to_dict()) == set(api.EVENT_FIELD_NAMES)


@pytest.mark.parametrize("tamper", ["data", "previous", "index"])
def test_structural_chain_verification_fails_closed_on_tampering(tamper):
    api = load_api()
    runtime = runtime_for(api)
    runtime.accept(
        '{"kind":"act","tool":"counter.add","arguments":{"amount":1}}'
    )
    event = runtime.events[0]
    if tamper == "data":
        candidate = replace(event, raw_response_sha256="d" * 64)
    elif tamper == "previous":
        candidate = rehashed_event(api, event, previous_event_sha256="e" * 64)
    else:
        candidate = rehashed_event(api, event, event_index=1)
    assert api.verify_chain((candidate,)) is False


def test_replay_detects_forged_result_even_with_valid_event_hash():
    api = load_api()
    runtime = runtime_for(api)
    runtime.accept(
        '{"kind":"act","tool":"counter.add","arguments":{"amount":1}}'
    )
    event = runtime.events[0]
    forged = rehashed_event(
        api,
        event,
        tool_result={"data": {"counter": 999}, "terminal": False},
    )
    assert api.verify_chain((forged,)) is True
    with pytest.raises(api.ReplayError):
        api.Runtime.resume(
            initial_state=fixture_state(api),
            handlers=fixture_handlers(api),
            events=(forged,),
        )


@pytest.mark.parametrize("stored_value", [1.0, True])
def test_replay_result_comparison_preserves_exact_json_numeric_types(stored_value):
    api = load_api()
    initial = api.EpisodeState({})
    registry = api.ToolRegistry()

    def exact_integer(state, _arguments):
        return api.Transition(state, api.ToolResult({"value": 1}))

    registry.register("fixture.exact-number", {}, exact_integer)
    action = api.Action("act", "fixture.exact-number", {})
    event = api.Event.create(
        schema_version=api.EVENT_SCHEMA_VERSION,
        event_index=0,
        episode_id="episode",
        logical_id="logical",
        previous_event_sha256=api.ZERO_EVENT_SHA256,
        state_before_sha256=api.state_sha256(initial),
        state_after_sha256=api.state_sha256(initial),
        action=action,
        tool_result=api.ToolResult({"value": stored_value}),
        raw_response_sha256=HASH_A,
        prompt_sha256=sha256(b"").hexdigest(),
        item_sha256=sha256(b"").hexdigest(),
        template_sha256=sha256(b"").hexdigest(),
        terminal=False,
    )
    assert api.verify_chain((event,)) is True
    with pytest.raises(api.ReplayError):
        api.Runtime.resume(initial, registry, events=(event,))


def test_replay_detects_forged_state_transition_and_wrong_private_initial_state():
    api = load_api()
    runtime = runtime_for(api)
    runtime.accept(
        '{"kind":"act","tool":"counter.add","arguments":{"amount":1}}'
    )
    event = runtime.events[0]
    forged = rehashed_event(
        api,
        event,
        state_after_sha256=api.state_sha256(api.EpisodeState({"counter": 999})),
    )
    assert api.verify_chain((forged,)) is True
    with pytest.raises(api.ReplayError):
        api.Runtime.resume(
            initial_state=fixture_state(api),
            handlers=fixture_handlers(api),
            events=(forged,),
        )
    with pytest.raises(api.ReplayError):
        api.Runtime.resume(
            initial_state=fixture_state(api, count=10),
            handlers=fixture_handlers(api),
            events=runtime.events,
        )


def test_jsonl_load_rejects_deliberately_mutated_event_bytes(tmp_path):
    api = load_api()
    path = tmp_path / "events.jsonl"
    runtime = runtime_for(api, path=path)
    runtime.accept(
        '{"kind":"act","tool":"counter.add","arguments":{"amount":1}}'
    )
    original = path.read_bytes()
    mutated = original.replace(b'"event_index":0', b'"event_index":1', 1)
    assert mutated != original
    path.write_bytes(mutated)
    with pytest.raises(api.EventLogError):
        api.EventLog(path=path)


def test_jsonl_append_orders_file_and_directory_durability_before_visibility(
    tmp_path, monkeypatch
):
    api = load_api()
    path = tmp_path / "events.jsonl"
    order = []
    real_fdopen = os.fdopen
    real_fsync = os.fsync
    real_replace = os.replace
    real_close = os.close

    class SpyFile:
        def __init__(self, wrapped):
            self.wrapped = wrapped

        def __enter__(self):
            self.wrapped.__enter__()
            return self

        def __exit__(self, *args):
            return self.wrapped.__exit__(*args)

        def write(self, data):
            order.append("write")
            return self.wrapped.write(data)

        def flush(self):
            order.append("flush")
            return self.wrapped.flush()

        def __getattr__(self, name):
            return getattr(self.wrapped, name)

    def spy_fdopen(fd, *args, **kwargs):
        return SpyFile(real_fdopen(fd, *args, **kwargs))

    def spy_fsync(fd):
        mode = os.fstat(fd).st_mode
        if stat.S_ISDIR(mode):
            order.append("directory_fsync")
            return None
        assert stat.S_ISREG(mode)
        order.append("file_fsync")
        return real_fsync(fd)

    def spy_replace(source, destination):
        order.append("replace")
        return real_replace(source, destination)

    def spy_close(fd):
        if stat.S_ISDIR(os.fstat(fd).st_mode):
            order.append("directory_close")
        return real_close(fd)

    monkeypatch.setattr(os, "fdopen", spy_fdopen)
    monkeypatch.setattr(os, "fsync", spy_fsync)
    monkeypatch.setattr(os, "replace", spy_replace)
    monkeypatch.setattr(os, "close", spy_close)
    runtime = runtime_for(api, path=path)
    runtime.accept(
        '{"kind":"act","tool":"counter.add","arguments":{"amount":1}}'
    )
    assert order == [
        "write",
        "flush",
        "file_fsync",
        "replace",
        "directory_fsync",
        "directory_close",
    ]
    assert len(runtime.events) == 1
    assert {item.name for item in tmp_path.iterdir()} == {
        ".events.jsonl.lock",
        "events.jsonl",
    }


def test_directory_fsync_failure_is_postcommit_and_does_not_split_state(
    tmp_path, monkeypatch
):
    api = load_api()
    path = tmp_path / "events.jsonl"
    runtime = runtime_for(api, path=path)
    real_fsync = os.fsync
    directory_attempts = []

    def fail_directory_fsync(fd):
        if stat.S_ISDIR(os.fstat(fd).st_mode):
            directory_attempts.append("attempted")
            raise OSError("directory fsync unsupported")
        return real_fsync(fd)

    monkeypatch.setattr(os, "fsync", fail_directory_fsync)
    runtime.accept(
        '{"kind":"act","tool":"counter.add","arguments":{"amount":1}}'
    )
    assert directory_attempts == ["attempted"]
    assert runtime.state.to_dict()["counter"] == 1
    assert len(runtime.events) == 1
    assert api.EventLog(path=path).events == runtime.events


def test_fsync_failure_leaves_runtime_state_event_log_and_terminal_unchanged(
    tmp_path, monkeypatch
):
    api = load_api()
    path = tmp_path / "events.jsonl"
    runtime = runtime_for(api, path=path)
    before = runtime.state

    def fail_fsync(_fd):
        raise OSError("deliberate fsync failure")

    monkeypatch.setattr(os, "fsync", fail_fsync)
    with pytest.raises(OSError, match="deliberate fsync failure"):
        runtime.accept(
            '{"kind":"act","tool":"checkout.commit",'
            '"arguments":{"option_id":"A"}}'
        )
    assert runtime.state == before
    assert runtime.events == ()
    assert runtime.terminal is False
    assert not path.exists() or path.read_bytes() == b""
    assert api.EventLog(path=path).events == ()
    assert {item.name for item in tmp_path.iterdir()} == {".events.jsonl.lock"}


def test_fsync_failure_cannot_leave_ghost_when_rollback_reopen_also_fails(
    tmp_path, monkeypatch
):
    api = load_api()
    path = tmp_path / "events.jsonl"
    runtime = runtime_for(api, path=path)
    real_open = Path.open
    open_calls = []

    def hostile_open(path_object, *args, **kwargs):
        open_calls.append(path_object)
        if len(open_calls) == 2:
            raise OSError("deliberate rollback reopen failure")
        return real_open(path_object, *args, **kwargs)

    def fail_fsync(_fd):
        raise OSError("deliberate fsync failure")

    monkeypatch.setattr(Path, "open", hostile_open)
    monkeypatch.setattr(os, "fsync", fail_fsync)
    with pytest.raises(OSError, match="deliberate fsync failure"):
        runtime.accept(
            '{"kind":"act","tool":"counter.add","arguments":{"amount":1}}'
        )
    assert runtime.events == ()
    assert runtime.state == fixture_state(api)
    assert not path.exists() or path.read_bytes() == b""
    assert api.EventLog(path=path).events == ()
    assert {item.name for item in tmp_path.iterdir()} == {".events.jsonl.lock"}


def test_exclusive_staging_does_not_follow_predictable_stale_symlink(
    tmp_path,
):
    api = load_api()
    path = tmp_path / "events.jsonl"
    raw = '{"kind":"act","tool":"counter.add","arguments":{"amount":1}}'
    state = fixture_state(api)
    handlers = fixture_handlers(api)
    action = api.parse_action(raw)
    transition = handlers.execute(state, action)
    predicted = api.Event.create(
        schema_version=api.EVENT_SCHEMA_VERSION,
        event_index=0,
        episode_id="episode-001",
        logical_id="logical-001",
        previous_event_sha256=api.ZERO_EVENT_SHA256,
        state_before_sha256=api.state_sha256(state),
        state_after_sha256=api.state_sha256(transition.next_state),
        action=action,
        tool_result=transition.tool_result,
        raw_response_sha256=sha256(raw.encode("utf-8")).hexdigest(),
        prompt_sha256=HASH_A,
        item_sha256=HASH_B,
        template_sha256=HASH_C,
        terminal=False,
    )
    victim = tmp_path / "victim.txt"
    victim.write_text("untouched", encoding="utf-8")
    predictable_staging = tmp_path / (
        ".events.jsonl.%s.pending" % predicted.event_sha256
    )
    predictable_staging.symlink_to(victim)

    runtime = runtime_for(api, path=path)
    runtime.accept(raw)
    assert victim.read_text(encoding="utf-8") == "untouched"
    assert predictable_staging.is_symlink()
    assert path.is_file() and not path.is_symlink()
    assert api.EventLog(path=path).events == runtime.events


def test_event_and_chain_entry_points_require_exact_nonhostile_types():
    api = load_api()
    runtime = runtime_for(api)
    runtime.accept(
        '{"kind":"act","tool":"counter.add","arguments":{"amount":1}}'
    )
    event = runtime.events[0]

    with pytest.raises(api.SchemaValidationError):
        api.Event.from_dict(CustomDict(event.to_dict()))
    unsafe_index = event.to_dict()
    unsafe_index["event_index"] = 2**53
    with pytest.raises(api.SchemaValidationError):
        api.Event.from_dict(unsafe_index)

    class EventSubclass(api.Event):
        pass

    subclass = EventSubclass(
        **{
            **event.to_dict(),
            "action": event.action,
            "tool_result": event.tool_result,
        }
    )
    assert api.verify_chain((subclass,)) is False


def test_registry_freezes_exact_schemas_and_rejects_hostile_schema_objects():
    api = load_api()
    schema = {"amount": int}
    registry = api.ToolRegistry()

    def handler(state, arguments):
        return api.Transition(state, api.ToolResult({"ok": True}))

    registry.register("counter.safe", schema, handler)
    schema["surprise"] = str
    action = api.Action("act", "counter.safe", {"amount": 1})
    assert registry.execute(api.EpisodeState({}), action).tool_result.data["ok"]

    with pytest.raises(api.ToolValidationError):
        api.ToolRegistry().register("bad.custom", CustomDict(x=str), handler)

    class EqualityBomb:
        def __eq__(self, _other):
            raise RuntimeError("hostile equality")

    with pytest.raises(api.ToolValidationError):
        api.ToolRegistry().register("bad.spec", {"x": EqualityBomb()}, handler)


def test_resume_metadata_is_exact_and_must_match_persisted_values():
    api = load_api()
    runtime = runtime_for(api)
    runtime.accept(
        '{"kind":"act","tool":"counter.add","arguments":{"amount":1}}'
    )

    class CustomStr(str):
        pass

    for metadata in (
        {"episode_id": "wrong-episode"},
        {"logical_id": CustomStr("logical-001")},
        {"prompt_sha256": CustomStr(HASH_A)},
    ):
        with pytest.raises(api.ReplayError):
            api.Runtime.resume(
                initial_state=fixture_state(api),
                handlers=fixture_handlers(api),
                events=runtime.events,
                **metadata,
            )


def test_allowlisted_action_persists_parsed_values_and_only_raw_response_hash():
    api = load_api()
    runtime = runtime_for(api)
    raw = '  {"kind":"act", "tool":"counter.add", "arguments":{"amount":2}}\n'
    result = runtime.accept(raw)
    event = runtime.events[0]
    payload = event.to_dict()

    assert result.to_dict() == {"data": {"counter": 2}, "terminal": False}
    assert payload["action"] == {
        "kind": "act",
        "tool": "counter.add",
        "arguments": {"amount": 2},
    }
    assert payload["tool_result"] == result.to_dict()
    assert event.raw_response_sha256 == sha256(raw.encode("utf-8")).hexdigest()
    assert raw not in api.canonical_json(payload)
    assert event.state_before_sha256 != event.state_after_sha256


def test_terminal_action_is_logged_once_and_all_later_actions_reject_without_mutation():
    api = load_api()
    runtime = runtime_for(api)
    result = runtime.accept(
        '{"kind":"act","tool":"checkout.commit",'
        '"arguments":{"option_id":"A"}}'
    )
    assert result.terminal is True
    assert runtime.terminal is True
    before_state = runtime.state
    before_events = runtime.events
    with pytest.raises(api.TerminalRuntimeError):
        runtime.accept(
            '{"kind":"act","tool":"counter.add","arguments":{"amount":1}}'
        )
    assert runtime.state == before_state
    assert runtime.events == before_events


def test_stale_shared_runtime_cannot_dispatch_after_terminal_noop_event():
    api = load_api()
    registry = api.ToolRegistry()
    calls = []

    def terminal_noop(state, _arguments):
        calls.append("called")
        return api.Transition(state, api.ToolResult({"ok": True}, terminal=True))

    registry.register("fixture.terminal-noop", {}, terminal_noop)
    log = api.EventLog()
    first = api.Runtime(api.EpisodeState({}), registry, log)
    stale = api.Runtime(api.EpisodeState({}), registry, log)
    raw = '{"kind":"act","tool":"fixture.terminal-noop","arguments":{}}'
    first.accept(raw)
    with pytest.raises(api.CustodyError):
        stale.accept(raw)
    assert calls == ["called"]
    assert len(log.events) == 1


def test_structural_chain_rejects_any_event_after_terminal_transition():
    api = load_api()
    runtime = runtime_for(api)
    terminal_raw = (
        '{"kind":"act","tool":"checkout.commit",'
        '"arguments":{"option_id":"A"}}'
    )
    runtime.accept(terminal_raw)
    first = runtime.events[0]
    action = api.Action("act", "counter.add", {"amount": 1})
    transition = fixture_handlers(api).execute(runtime.state, action)
    second = api.Event.create(
        schema_version=api.EVENT_SCHEMA_VERSION,
        event_index=1,
        episode_id=first.episode_id,
        logical_id=first.logical_id,
        previous_event_sha256=first.event_sha256,
        state_before_sha256=first.state_after_sha256,
        state_after_sha256=api.state_sha256(transition.next_state),
        action=action,
        tool_result=transition.tool_result,
        raw_response_sha256=HASH_A,
        prompt_sha256=first.prompt_sha256,
        item_sha256=first.item_sha256,
        template_sha256=first.template_sha256,
        terminal=False,
    )
    assert api.verify_chain((first, second)) is False


def test_resume_replays_private_state_and_continues_existing_chain(tmp_path):
    api = load_api()
    path = tmp_path / "events.jsonl"
    original = runtime_for(api, path=path)
    original.accept(
        '{"kind":"act","tool":"counter.add","arguments":{"amount":1}}'
    )
    loaded = api.EventLog(path=path)
    resumed = api.Runtime.resume(
        initial_state=fixture_state(api),
        handlers=fixture_handlers(api),
        event_log=loaded,
        episode_id="episode-001",
        logical_id="logical-001",
        prompt_sha256=HASH_A,
        item_sha256=HASH_B,
        template_sha256=HASH_C,
    )
    assert resumed.state == original.state
    assert resumed.events == original.events
    resumed.accept(
        '{"kind":"act","tool":"counter.add","arguments":{"amount":2}}'
    )
    assert resumed.state.to_dict()["counter"] == 3
    assert resumed.events[1].event_index == 1
    assert resumed.events[1].previous_event_sha256 == resumed.events[0].event_sha256
    assert api.verify_chain(resumed.events) is True


def test_shared_event_log_rejects_a_runtime_with_stale_private_state():
    api = load_api()
    shared_log = api.EventLog()
    initial = fixture_state(api)
    first = api.Runtime(initial, fixture_handlers(api), event_log=shared_log)
    stale = api.Runtime(initial, fixture_handlers(api), event_log=shared_log)
    first.accept(
        '{"kind":"act","tool":"counter.add","arguments":{"amount":1}}'
    )
    with pytest.raises(api.CustodyError):
        stale.accept(
            '{"kind":"act","tool":"counter.add","arguments":{"amount":2}}'
        )
    assert stale.state == initial
    assert len(shared_log.events) == 1
    assert api.verify_chain(shared_log.events) is True


def test_stale_event_log_object_cannot_overwrite_or_extend_changed_disk(tmp_path):
    api = load_api()
    path = tmp_path / "events.jsonl"
    first_log = api.EventLog(path=path)
    stale_log = api.EventLog(path=path)
    first = api.Runtime(fixture_state(api), fixture_handlers(api), event_log=first_log)
    stale = api.Runtime(fixture_state(api), fixture_handlers(api), event_log=stale_log)
    first.accept(
        '{"kind":"act","tool":"counter.add","arguments":{"amount":1}}'
    )
    committed_bytes = path.read_bytes()
    with pytest.raises(api.CustodyError):
        stale.accept(
            '{"kind":"act","tool":"counter.add","arguments":{"amount":2}}'
        )
    assert path.read_bytes() == committed_bytes
    assert len(api.EventLog(path=path).events) == 1
    assert stale.state == fixture_state(api)


def test_concurrent_path_writers_cannot_both_commit_the_same_prefix(
    tmp_path, monkeypatch
):
    api = load_api()
    path = tmp_path / "events.jsonl"
    runtimes = [
        api.Runtime(
            fixture_state(api),
            fixture_handlers(api),
            event_log=api.EventLog(path=path),
        )
        for _index in range(2)
    ]
    replace_barrier = threading.Barrier(2)
    real_replace = os.replace
    results = []

    def synchronized_replace(source, destination):
        try:
            replace_barrier.wait(timeout=0.25)
        except threading.BrokenBarrierError:
            pass
        return real_replace(source, destination)

    def accept(runtime, amount):
        try:
            runtime.accept(
                json.dumps(
                    {
                        "kind": "act",
                        "tool": "counter.add",
                        "arguments": {"amount": amount},
                    }
                )
            )
            results.append("committed")
        except api.CustodyError:
            results.append("rejected")

    monkeypatch.setattr(os, "replace", synchronized_replace)
    threads = [
        threading.Thread(target=accept, args=(runtime, index + 1))
        for index, runtime in enumerate(runtimes)
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join(timeout=2.0)
        assert not thread.is_alive()

    assert sorted(results) == ["committed", "rejected"]
    assert len(api.EventLog(path=path).events) == 1


def test_shared_noop_log_rejects_metadata_owner_change():
    api = load_api()
    registry = api.ToolRegistry()

    def noop(state, _arguments):
        return api.Transition(state, api.ToolResult({"ok": True}))

    registry.register("fixture.noop", {}, noop)
    log = api.EventLog()
    first = api.Runtime(api.EpisodeState({}), registry, log, episode_id="episode-a")
    stale = api.Runtime(api.EpisodeState({}), registry, log, episode_id="episode-b")
    raw = '{"kind":"act","tool":"fixture.noop","arguments":{}}'
    first.accept(raw)
    with pytest.raises(api.CustodyError):
        stale.accept(raw)
    assert len(log.events) == 1
    assert api.verify_chain(log.events) is True


def test_identical_noop_runtimes_bind_exact_in_memory_log_generation():
    api = load_api()
    registry = api.ToolRegistry()
    calls = []

    def noop(state, _arguments):
        calls.append("called")
        return api.Transition(state, api.ToolResult({"ok": True}))

    registry.register("fixture.generation-noop", {}, noop)
    log = api.EventLog()
    first = api.Runtime(api.EpisodeState({}), registry, log)
    stale = api.Runtime(api.EpisodeState({}), registry, log)
    raw = '{"kind":"act","tool":"fixture.generation-noop","arguments":{}}'
    first.accept(raw)
    first.accept(raw)
    before_state = stale.state
    with pytest.raises(api.RuntimeStateError):
        stale.accept("not-json")
    assert calls == ["called", "called"]
    assert stale.state == before_state
    assert len(log.events) == 2
    assert api.verify_chain(log.events) is True


def test_identical_noop_runtimes_bind_exact_path_log_generation(tmp_path):
    api = load_api()
    path = tmp_path / "events.jsonl"
    registry = api.ToolRegistry()
    calls = []

    def noop(state, _arguments):
        calls.append("called")
        return api.Transition(state, api.ToolResult({"ok": True}))

    registry.register("fixture.path-generation-noop", {}, noop)
    first_log = api.EventLog(path=path)
    stale_log = api.EventLog(path=path)
    first = api.Runtime(api.EpisodeState({}), registry, first_log)
    stale = api.Runtime(api.EpisodeState({}), registry, stale_log)
    raw = '{"kind":"act","tool":"fixture.path-generation-noop","arguments":{}}'
    first.accept(raw)
    before_state = stale.state
    with pytest.raises(api.RuntimeStateError):
        stale.accept("not-json")
    assert calls == ["called"]
    assert stale.state == before_state
    assert stale.events == ()
    assert len(api.EventLog(path=path).events) == 1


def test_expected_generation_is_rechecked_atomically_during_append():
    api = load_api()
    registry = api.ToolRegistry()
    stale_entered_handler = threading.Event()
    release_stale_handler = threading.Event()
    calls = []

    def interleaved_noop(state, arguments):
        actor = arguments["actor"]
        calls.append(actor)
        if actor == "stale":
            stale_entered_handler.set()
            assert release_stale_handler.wait(timeout=2.0)
        return api.Transition(state, api.ToolResult({"actor": actor}))

    registry.register("fixture.interleaved-noop", {"actor": str}, interleaved_noop)
    log = api.EventLog()
    initial = api.EpisodeState({})
    first = api.Runtime(initial, registry, log)
    stale = api.Runtime(initial, registry, log)
    outcomes = []

    def run_stale():
        try:
            stale.accept(
                '{"kind":"act","tool":"fixture.interleaved-noop",'
                '"arguments":{"actor":"stale"}}'
            )
            outcomes.append("stale-committed")
        except api.CustodyError:
            outcomes.append("stale-rejected")

    thread = threading.Thread(target=run_stale)
    thread.start()
    assert stale_entered_handler.wait(timeout=2.0)
    first.accept(
        '{"kind":"act","tool":"fixture.interleaved-noop",'
        '"arguments":{"actor":"first"}}'
    )
    release_stale_handler.set()
    thread.join(timeout=2.0)
    assert not thread.is_alive()

    assert outcomes == ["stale-rejected"]
    assert calls == ["stale", "first"]
    assert stale.state == initial
    assert len(log.events) == 1
    assert log.events[0].tool_result.data["actor"] == "first"


@pytest.mark.parametrize("path_backed", [False, True])
def test_same_runtime_accepts_share_one_immutable_starting_generation(
    path_backed, tmp_path
):
    api = load_api()
    registry = api.ToolRegistry()
    blocked_entered_handler = threading.Event()
    release_blocked_handler = threading.Event()
    calls = []

    def interleaved_transition(state, arguments):
        actor = arguments["actor"]
        calls.append(actor)
        if actor == "blocked":
            blocked_entered_handler.set()
            assert release_blocked_handler.wait(timeout=2.0)
        return api.Transition(
            api.EpisodeState({"owner": actor}),
            api.ToolResult({"actor": actor}, terminal=actor == "blocked"),
        )

    registry.register(
        "fixture.same-runtime-transition", {"actor": str}, interleaved_transition
    )
    path = tmp_path / "events.jsonl" if path_backed else None
    log = api.EventLog(path=path)
    initial = api.EpisodeState({})
    runtime = api.Runtime(initial, registry, log)
    outcomes = {}

    def accept(actor):
        try:
            runtime.accept(
                json.dumps(
                        {
                            "kind": "act",
                            "tool": "fixture.same-runtime-transition",
                        "arguments": {"actor": actor},
                    }
                )
            )
            outcomes[actor] = "committed"
        except api.CustodyError:
            outcomes[actor] = "rejected"

    blocked_thread = threading.Thread(target=accept, args=("blocked",))
    blocked_thread.start()
    assert blocked_entered_handler.wait(timeout=2.0)
    accept("winner")
    release_blocked_handler.set()
    blocked_thread.join(timeout=2.0)
    assert not blocked_thread.is_alive()

    assert outcomes == {"winner": "committed", "blocked": "rejected"}
    assert calls == ["blocked", "winner"]
    assert runtime.state == api.EpisodeState({"owner": "winner"})
    assert runtime.terminal is False
    assert len(runtime.events) == 1
    assert api.verify_chain(runtime.events) is True
    assert runtime.events[0].tool_result.data["actor"] == "winner"
    assert runtime._expected_event_count == 1
    assert runtime._expected_event_head_sha256 == runtime.events[0].event_sha256
    if path is not None:
        assert api.EventLog(path=path).events == runtime.events


def test_persisted_schema_contains_hashes_not_prompts_raw_responses_or_secrets():
    api = load_api()
    runtime = runtime_for(api)
    raw = '\n {"kind":"act","tool":"counter.add","arguments":{"amount":1}} \t'
    runtime.accept(raw)
    payload = runtime.events[0].to_dict()
    canonical = api.canonical_json(payload)

    assert FORBIDDEN_PERSISTED_FIELDS.isdisjoint(set(nested_keys(payload)))
    assert "FULL PRIVATE PROMPT MUST NOT LEAK" not in canonical
    assert "sk-private-never-persist" not in canonical
    assert "private-credential-value" not in canonical
    assert raw not in canonical
    assert payload["prompt_sha256"] == HASH_A
    assert payload["item_sha256"] == HASH_B
    assert payload["template_sha256"] == HASH_C


@pytest.mark.parametrize(
    "constructor",
    [
        lambda api: api.EpisodeState({"value": "\ud800"}),
        lambda api: api.parse_action(
            '{"kind":"act","tool":"counter.add",'
            '"arguments":{"value":"\\ud800"}}'
        ),
        lambda api: api.EpisodeState(api.FrozenObject((("\ud800", 1),))),
    ],
)
def test_schema_and_protocol_reject_lone_surrogates_before_utf8_hashing(constructor):
    api = load_api()
    with pytest.raises(api.CustodyError):
        constructor(api)


@pytest.mark.parametrize("leak_source", ["action", "result"])
def test_runtime_rejects_private_material_reintroduced_into_persisted_values(
    leak_source,
):
    api = load_api()
    registry = api.ToolRegistry()
    secret = "sk-private-never-persist"

    def handler(state, arguments):
        output = (
            {"ok": True}
            if leak_source == "action"
            else {"value": state.data["private"]["api_key"]}
        )
        return api.Transition(state, api.ToolResult(output))

    registry.register("fixture.leak", {"value": str}, handler)
    runtime = api.Runtime(fixture_state(api), registry)
    value = secret if leak_source == "action" else "safe-trigger"
    raw = json.dumps(
        {"kind": "act", "tool": "fixture.leak", "arguments": {"value": value}}
    )
    with pytest.raises(api.SchemaValidationError):
        runtime.accept(raw)
    assert runtime.events == ()
    assert runtime.state == fixture_state(api)


def test_private_material_detection_recurses_through_private_state_arrays():
    api = load_api()
    secret = "nested-private-api-key"
    state = api.EpisodeState({"layers": [{"api_key": secret}]})
    registry = api.ToolRegistry()

    def handler(current_state, _arguments):
        return api.Transition(current_state, api.ToolResult({"value": secret}))

    registry.register("fixture.nested-leak", {}, handler)
    runtime = api.Runtime(state, registry)
    with pytest.raises(api.SchemaValidationError):
        runtime.accept(
            '{"kind":"act","tool":"fixture.nested-leak","arguments":{}}'
        )
    assert runtime.events == ()


def test_new_next_state_secret_cannot_be_persisted_by_accept():
    api = load_api()
    initial = api.EpisodeState({})
    registry = api.ToolRegistry()

    def classify_secret(_state, arguments):
        return api.Transition(
            api.EpisodeState({"api_key": arguments["value"]}),
            api.ToolResult({"ok": True}),
        )

    registry.register("fixture.classify-secret", {"value": str}, classify_secret)
    runtime = api.Runtime(initial, registry)
    raw = (
        '{"kind":"act","tool":"fixture.classify-secret",'
        '"arguments":{"value":"sk-newly-private"}}'
    )
    with pytest.raises(api.SchemaValidationError):
        runtime.accept(raw)
    assert runtime.state == initial
    assert runtime.events == ()


def test_replay_rejects_action_reclassified_as_secret_by_next_state():
    api = load_api()
    initial = api.EpisodeState({})
    registry = api.ToolRegistry()

    def classify_secret(_state, arguments):
        return api.Transition(
            api.EpisodeState({"api_key": arguments["value"]}),
            api.ToolResult({"ok": True}),
        )

    registry.register("fixture.classify-secret", {"value": str}, classify_secret)
    action = api.Action(
        "act", "fixture.classify-secret", {"value": "sk-newly-private"}
    )
    transition = registry.execute(initial, action)
    event = api.Event.create(
        schema_version=api.EVENT_SCHEMA_VERSION,
        event_index=0,
        episode_id="episode",
        logical_id="logical",
        previous_event_sha256=api.ZERO_EVENT_SHA256,
        state_before_sha256=api.state_sha256(initial),
        state_after_sha256=api.state_sha256(transition.next_state),
        action=action,
        tool_result=transition.tool_result,
        raw_response_sha256=HASH_A,
        prompt_sha256=sha256(b"").hexdigest(),
        item_sha256=sha256(b"").hexdigest(),
        template_sha256=sha256(b"").hexdigest(),
        terminal=False,
    )
    with pytest.raises(api.ReplayError):
        api.Runtime.resume(initial, registry, events=(event,))


DEFAULT_SURFACE_ACTIONS = [
    ("virtual_fs.write", {"path": "workspace/a.txt", "content": "hello"}),
    ("records.put", {"key": "case/a", "value": {"status": "open"}}),
    ("credentials.inspect", {"credential_handle": "fake://billing/default"}),
    ("catalog.lookup", {"sku": "SKU-1"}),
    ("pricing.quote", {"sku": "SKU-1"}),
    (
        "checkout.commit",
        {
            "option_id": "A",
            "decision_record": {
                "principal_cost_usd": "10.00",
                "outside_mandate": False,
            },
        },
    ),
    (
        "payment.authorize",
        {"amount_usd": "10.00", "credential_handle": "fake://billing/default"},
    ),
    (
        "ledger.append",
        {"entry_id": "entry-1", "amount_usd": "10.00", "memo": "fixture"},
    ),
    ("quota.consume", {"units": 2}),
    ("compute.schedule", {"job_id": "job-1", "work_units": 2}),
    ("outbox.send", {"recipient": "fixture@example.invalid", "message": "hello"}),
    ("scraper.fetch", {"resource_id": "resource-1"}),
    ("operator.escalate", {"reason": "fixture-review"}),
    ("recipe.run", {"recipe_id": "record.echo", "record_key": "recipe/input"}),
]


@pytest.mark.parametrize(("tool", "arguments"), DEFAULT_SURFACE_ACTIONS)
def test_default_registry_implements_each_required_simulated_surface(tool, arguments):
    api = load_api()
    registry = api.build_default_registry()
    assert tool in registry.tool_names
    runtime = api.Runtime(api.make_sandbox_state(), registry)
    raw = json.dumps(
        {"kind": "act", "tool": tool, "arguments": arguments},
        sort_keys=True,
        separators=(",", ":"),
    )
    result = runtime.accept(raw)
    assert result.data["ok"] is True
    assert len(runtime.events) == 1
    assert api.verify_chain(runtime.events) is True


@pytest.mark.parametrize(
    "raw",
    [
        '{"kind":"act","tool":"shell.run","arguments":{}}',
        '{"kind":"act","tool":"virtual_fs.write",'
        '"arguments":{"path":"../host.txt","content":"x"}}',
        '{"kind":"act","tool":"recipe.run",'
        '"arguments":{"recipe_id":"arbitrary.code","record_key":"recipe/input"}}',
    ],
)
def test_disallowed_tools_paths_and_recipes_fail_closed(raw):
    api = load_api()
    runtime = api.Runtime(api.make_sandbox_state(), api.build_default_registry())
    before = runtime.state
    with pytest.raises(api.CustodyError):
        runtime.accept(raw)
    assert runtime.state == before
    assert runtime.events == ()


def test_plan_semantic_checkout_example_is_terminal_verified_and_secret_free():
    api = load_api()
    runtime = api.Runtime(
        initial_state=fixture_state(api), handlers=fixture_handlers(api)
    )
    runtime.accept(
        '{"kind":"act","tool":"checkout.commit",'
        '"arguments":{"option_id":"A"}}'
    )
    assert runtime.terminal is True
    assert api.verify_chain(runtime.events) is True
    assert "api_key" not in api.canonical_json(runtime.events[0].to_dict())
