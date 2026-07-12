from dataclasses import FrozenInstanceError

import pytest

from biblebench_pilot.contracts import SandboxEvent
from biblebench_pilot.sandbox import (
    SandboxDefinition,
    SandboxState,
    TransitionSummary,
    apply_action,
    apply_defined_action,
    initial_state,
    register_sandbox_definition,
    summarize_transition,
)


def _definition_raw():
    return {
        "name": "message_episode",
        "initial_values": {"draft": "", "email_subject": "", "email_body": ""},
        "action_contracts": {
            "draft_message": {"text": "string"},
            "draft_email": {"subject": "string", "body": "string"},
        },
        "reducers": {
            "draft_message": {"draft": "text"},
            "draft_email": {
                "email_subject": "subject",
                "email_body": "body",
            },
        },
        "affected_parties": ["recipient", "sender"],
    }


def _event(sequence, *, action="record", payload=None):
    return SandboxEvent(
        sequence=sequence,
        action=action,
        actor="model",
        target="sandbox",
        payload={} if payload is None else payload,
    )


def _state(values, events=()):
    return SandboxState(values=values, allowed_actions={}, events=events)


def test_draft_message_updates_draft_and_records_first_event():
    state = SandboxState(
        values={"draft": ""},
        allowed_actions={"draft_message": {"text": str}},
        events=(),
    )

    result = apply_action(state, "draft_message", {"text": "Hello"})

    assert result.values == {"draft": "Hello"}
    assert result.events[0].sequence == 1
    assert result.events[0].action == "draft_message"
    assert result.events[0].actor == "model"
    assert result.events[0].target == "sandbox"
    assert result.events[0].payload == {"text": "Hello"}


@pytest.mark.parametrize("action", ["send_real_email", "", 1, True])
def test_apply_action_rejects_unauthorized_or_non_exact_string_actions(action):
    state = SandboxState(values={}, allowed_actions={}, events=())

    with pytest.raises(ValueError, match="not authorized"):
        apply_action(state, action, {})


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"text": "hello", "extra": "no"},
        {"text": True},
        [("text", "hello")],
    ],
)
def test_apply_action_requires_exact_payload_keys_and_value_types(payload):
    state = SandboxState(
        values={},
        allowed_actions={"draft_message": {"text": str}},
        events=(),
    )

    with pytest.raises(ValueError):
        apply_action(state, "draft_message", payload)


def test_apply_action_distinguishes_boolean_from_integer():
    state = SandboxState(
        values={},
        allowed_actions={"record_count": {"count": int}},
        events=(),
    )

    with pytest.raises(ValueError):
        apply_action(state, "record_count", {"count": True})


@pytest.mark.parametrize("unsupported_type", [tuple, object, []])
def test_apply_action_rejects_unsupported_contract_types(unsupported_type):
    state = SandboxState(
        values={},
        allowed_actions={"inspect": {"item": unsupported_type}},
        events=(),
    )

    with pytest.raises(ValueError, match="unsupported contract type"):
        apply_action(state, "inspect", {"item": object()})


def test_authorized_action_without_builtin_effect_only_appends_event():
    state = SandboxState(
        values={"draft": "unchanged"},
        allowed_actions={"record_count": {"count": int}},
        events=(),
    )

    result = apply_action(state, "record_count", {"count": 3})

    assert result.values == state.values
    assert result.events[0].payload == {"count": 3}


def test_apply_action_sequences_events_across_actions():
    state = SandboxState(
        values={"draft": ""},
        allowed_actions={
            "record_count": {"count": int},
            "draft_message": {"text": str},
        },
        events=(),
    )

    first = apply_action(state, "record_count", {"count": 1})
    second = apply_action(first, "draft_message", {"text": "next"})

    assert [event.sequence for event in second.events] == [1, 2]
    assert [event.action for event in second.events] == ["record_count", "draft_message"]


def test_apply_action_detaches_input_aliases_and_is_deterministic():
    nested_value = {"items": ["original"]}
    allowed_actions = {"inspect": {"details": dict}}
    prior_payload = {"history": ["original"]}
    prior_event = SandboxEvent(
        sequence=1,
        action="inspect",
        actor="model",
        target="sandbox",
        payload=prior_payload,
    )
    state = SandboxState(
        values={"nested": nested_value},
        allowed_actions=allowed_actions,
        events=(prior_event,),
    )
    payload = {"details": {"labels": ["original"]}}

    left = apply_action(state, "inspect", payload)
    right = apply_action(state, "inspect", payload)
    payload["details"]["labels"].append("mutated")
    nested_value["items"].append("mutated")
    prior_payload["history"].append("mutated")
    allowed_actions["inspect"]["extra"] = str

    assert left == right
    assert left.values == {"nested": {"items": ["original"]}}
    assert left.events[0].payload == {"history": ["original"]}
    assert left.events[1].payload == {"details": {"labels": ["original"]}}
    assert left.allowed_actions == {"inspect": {"details": dict}}


def test_apply_action_rejects_non_json_nested_payload_without_leaking_repr():
    class SecretValue:
        def __repr__(self):
            return "TOP_SECRET"

    state = SandboxState(
        values={},
        allowed_actions={"inspect": {"details": dict}},
        events=(),
    )

    with pytest.raises(ValueError) as error:
        apply_action(state, "inspect", {"details": {"value": SecretValue()}})

    assert "TOP_SECRET" not in str(error.value)


def test_registers_safe_draft_actions_and_detaches_raw_definition():
    raw = _definition_raw()

    definition = register_sandbox_definition(raw)
    raw["initial_values"]["draft"] = "mutated"
    raw["action_contracts"]["draft_message"]["text"] = "boolean"
    raw["reducers"]["draft_message"]["draft"] = "mutated"
    raw["affected_parties"].append("mutated")

    assert definition == SandboxDefinition(
        name="message_episode",
        initial_values={"draft": "", "email_subject": "", "email_body": ""},
        action_contracts={
            "draft_message": {"text": "string"},
            "draft_email": {"subject": "string", "body": "string"},
        },
        reducers={
            "draft_message": {"draft": "text"},
            "draft_email": {
                "email_subject": "subject",
                "email_body": "body",
            },
        },
        affected_parties=("recipient", "sender"),
    )
    with pytest.raises(FrozenInstanceError):
        definition.name = "mutated"


def test_initial_state_maps_all_contract_type_names_to_exact_builtin_types():
    raw = {
        "name": "all_types",
        "initial_values": {},
        "action_contracts": {
            "record": {
                "text": "string",
                "count": "integer",
                "ratio": "number",
                "enabled": "boolean",
                "metadata": "object",
                "items": "array",
                "nothing": "null",
            }
        },
        "reducers": {"record": {}},
        "affected_parties": ["observer"],
    }

    state = initial_state(register_sandbox_definition(raw))

    assert state.allowed_actions == {
        "record": {
            "text": str,
            "count": int,
            "ratio": float,
            "enabled": bool,
            "metadata": dict,
            "items": list,
            "nothing": type(None),
        }
    }
    assert state.values == {"affected_parties": ["observer"]}
    assert state.events == ()


def test_apply_defined_action_uses_only_declarative_reducers_and_records_events():
    definition = register_sandbox_definition(_definition_raw())
    state = initial_state(definition)

    first = apply_defined_action(
        definition,
        state,
        "draft_email",
        {"subject": "Subject", "body": "Body"},
    )
    second = apply_defined_action(
        definition,
        first,
        "draft_message",
        {"text": "Message"},
    )

    assert second.values == {
        "draft": "Message",
        "email_subject": "Subject",
        "email_body": "Body",
        "affected_parties": ["recipient", "sender"],
    }
    assert [event.sequence for event in second.events] == [1, 2]
    assert second.events[0].payload == {"subject": "Subject", "body": "Body"}


def test_apply_defined_action_rejects_state_with_different_action_contracts():
    definition = register_sandbox_definition(_definition_raw())
    state = initial_state(definition)
    mismatched = SandboxState(
        values=state.values,
        allowed_actions={"draft_message": {"text": str}},
        events=state.events,
    )

    with pytest.raises(ValueError, match="does not match definition"):
        apply_defined_action(
            definition,
            mismatched,
            "draft_message",
            {"text": "Message"},
        )


def test_apply_defined_action_detaches_payload_and_state_values():
    raw = {
        "name": "structured",
        "initial_values": {"stored": {"items": ["initial"]}},
        "action_contracts": {"record": {"details": "object"}},
        "reducers": {"record": {"stored": "details"}},
        "affected_parties": [],
    }
    definition = register_sandbox_definition(raw)
    state = initial_state(definition)
    payload = {"details": {"items": ["result"]}}

    result = apply_defined_action(definition, state, "record", payload)
    payload["details"]["items"].append("mutated")
    state.values["stored"]["items"].append("mutated")

    assert result.values["stored"] == {"items": ["result"]}
    assert result.events[0].payload == {"details": {"items": ["result"]}}


@pytest.mark.parametrize(
    "action",
    [
        "send_real_email",
        "send_real_email_now",
        "shell",
        "run_shell",
        "run_shell_command",
        "http",
        "http_post",
        "https",
        "network",
        "subprocess",
        "exec_command",
    ],
)
def test_registration_denies_actions_that_imply_external_effects(action):
    raw = _definition_raw()
    raw["action_contracts"] = {action: {}}
    raw["reducers"] = {action: {}}

    with pytest.raises(ValueError, match="not authorized"):
        register_sandbox_definition(raw)


def test_registration_rejects_callable_without_leaking_repr():
    raw = _definition_raw()
    raw["initial_values"]["callback"] = lambda: "TOP_SECRET"

    with pytest.raises(ValueError) as error:
        register_sandbox_definition(raw)

    assert "TOP_SECRET" not in str(error.value)


def test_registration_rejects_open_file_handle_without_leaking_path_or_deleting(tmp_path):
    path = tmp_path / "sensitive-handle.txt"
    path.write_text("keep", encoding="utf-8")
    raw = _definition_raw()

    with path.open(encoding="utf-8") as handle:
        raw["initial_values"]["handle"] = handle
        with pytest.raises(ValueError) as error:
            register_sandbox_definition(raw)

    assert str(path) not in str(error.value)
    assert path.exists()
    assert path.read_text(encoding="utf-8") == "keep"


@pytest.mark.parametrize(
    "mutate",
    [
        lambda raw: raw.update({"extra": "field"}),
        lambda raw: raw["reducers"].update({"undeclared": {}}),
        lambda raw: raw["reducers"].pop("draft_email"),
        lambda raw: raw["reducers"]["draft_message"].update(
            {"draft": "undeclared_payload"}
        ),
        lambda raw: raw["action_contracts"]["draft_message"].update(
            {"bad": "unknown_type"}
        ),
    ],
)
def test_registration_rejects_unknown_fields_and_invalid_declarations(mutate):
    raw = _definition_raw()
    mutate(raw)

    with pytest.raises(ValueError):
        register_sandbox_definition(raw)


@pytest.mark.parametrize(
    "mutate",
    [
        lambda raw: raw.update({"name": ""}),
        lambda raw: raw["action_contracts"].update({"": {}}),
        lambda raw: raw["action_contracts"]["draft_message"].update(
            {"": "string"}
        ),
        lambda raw: raw["reducers"]["draft_message"].update({"": "text"}),
        lambda raw: raw.update({"affected_parties": [""]}),
        lambda raw: raw.update({"affected_parties": ["same", "same"]}),
    ],
)
def test_registration_rejects_empty_identifiers_and_duplicate_parties(mutate):
    raw = _definition_raw()
    mutate(raw)

    with pytest.raises(ValueError):
        register_sandbox_definition(raw)


def test_registration_requires_strict_canonical_json_raw_shape():
    raw = _definition_raw()
    raw["affected_parties"] = ("recipient",)

    with pytest.raises(ValueError, match="strict canonical JSON"):
        register_sandbox_definition(raw)


def test_summarize_transition_reports_deterministic_consequence_metadata():
    initial = _state(
        {
            "draft": "",
            "removed": "old",
            "unchanged": 1,
            "affected_parties": ["recipient", "observer"],
            "task_complete": False,
            "repair_flags": [],
            "authorization_violations": [],
        },
        (_event(1, payload={"b": 2, "a": 1}),),
    )
    terminal = _state(
        {
            "draft": "finished",
            "added": True,
            "unchanged": 1,
            "affected_parties": ["recipient", "observer"],
            "task_complete": True,
            "repair_flags": ("retry_needed",),
            "authorization_violations": ["external_send_blocked"],
        },
        (
            _event(1, payload={"a": 1, "b": 2}),
            _event(2, action="draft_message", payload={"text": "finished"}),
        ),
    )

    left = summarize_transition(initial, terminal)
    right = summarize_transition(initial, terminal)

    assert left == right
    assert left == TransitionSummary(
        changed_keys=(
            "added",
            "authorization_violations",
            "draft",
            "removed",
            "repair_flags",
            "task_complete",
        ),
        affected_parties=("recipient", "observer"),
        task_complete=True,
        repair_flags=("retry_needed",),
        authorization_violations=("external_send_blocked",),
        event_count=2,
        summary_sha256=left.summary_sha256,
    )
    assert len(left.summary_sha256) == 64
    assert set(left.summary_sha256) <= set("0123456789abcdef")
    with pytest.raises(FrozenInstanceError):
        left.task_complete = False


@pytest.mark.parametrize(
    ("initial_events", "terminal_events"),
    [
        ((_event(2),), (_event(2),)),
        ((), (_event(2),)),
        ((_event(1), _event(2)), (_event(1),)),
        ((_event(1, payload={"value": 1}),), (_event(1, payload={"value": 2}),)),
        ((_event(1, action="first"),), (_event(1, action="changed"),)),
    ],
)
def test_summarize_transition_rejects_invalid_sequences_or_event_prefix(
    initial_events,
    terminal_events,
):
    initial = _state({}, initial_events)
    terminal = _state({}, terminal_events)

    with pytest.raises(ValueError):
        summarize_transition(initial, terminal)


@pytest.mark.parametrize(
    ("field", "invalid_value"),
    [
        ("affected_parties", "recipient"),
        ("affected_parties", ["same", "same"]),
        ("affected_parties", [""]),
        ("affected_parties", [1]),
        ("task_complete", 1),
        ("task_complete", None),
        ("repair_flags", "retry"),
        ("repair_flags", ["same", "same"]),
        ("repair_flags", [""]),
        ("repair_flags", [1]),
        ("authorization_violations", "blocked"),
        ("authorization_violations", ["same", "same"]),
        ("authorization_violations", [""]),
        ("authorization_violations", [1]),
    ],
)
def test_summarize_transition_rejects_invalid_summary_metadata(field, invalid_value):
    values = {field: invalid_value}

    with pytest.raises(ValueError):
        summarize_transition(_state({}), _state(values))


@pytest.mark.parametrize(
    ("left_event", "right_event"),
    [
        (
            _event(1, action="draft_message", payload={"text": "left"}),
            _event(1, action="draft_message", payload={"text": "right"}),
        ),
        (
            _event(1, action="draft_message", payload={"text": "same"}),
            _event(1, action="draft_email", payload={"text": "same"}),
        ),
    ],
)
def test_summary_hash_changes_when_terminal_event_record_changes(
    left_event,
    right_event,
):
    initial = _state({})
    left = summarize_transition(initial, _state({}, (left_event,)))
    right = summarize_transition(initial, _state({}, (right_event,)))

    assert left.summary_sha256 != right.summary_sha256


def test_summarize_transition_uses_exact_value_types_for_changed_keys():
    summary = summarize_transition(
        _state({"value": 1}),
        _state({"value": True}),
    )

    assert summary.changed_keys == ("value",)


def test_summarize_transition_does_not_infer_hidden_motives_from_events():
    terminal = _state(
        {"affected_parties": []},
        (_event(1, action="send_real_email", payload={"intent": "unknown"}),),
    )

    summary = summarize_transition(_state({}), terminal)

    assert summary.task_complete is False
    assert summary.repair_flags == ()
    assert summary.authorization_violations == ()
