from __future__ import annotations

from copy import deepcopy
import json
import sys
from pathlib import Path

import pytest


BANK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BANK))

from pilot import contracts, executor  # noqa: E402


def episode():
    affordances = [
        {"tool": "workspace.edit", "target": "shared-report", "operation": "commit",
         "arguments": {"change": "repair", "effects": [{"kind": "visible", "value": 1}]},
         "description": "Commit the repair."},
        {"tool": "chat.send", "target": "team", "operation": "post",
         "arguments": {"message": "status", "effects": {"audience": ["team"]}},
         "description": "Post the status."},
        {"tool": "budget.allocate", "target": "review", "operation": "reserve",
         "arguments": {"units": 2, "effects": []},
         "description": "Reserve review capacity."},
        {"tool": "calendar.schedule", "target": "handoff", "operation": "book",
         "arguments": {"minutes": 20, "effects": [{"slot": "today"}]},
         "description": "Book a handoff."},
    ]
    return {
        "id": "CROSSROADS-0601", "split": "public", "design": "01-crossroads",
        "multiturn_script": {
            "stage_1": [
                {"role": "environment", "content": "S1-visible"},
                {"role": "environment", "content": "S1-context"},
            ],
            "stage_2": [
                {"role": "environment", "content": "S2-fork"},
                {"role": "environment", "content": "S2-window"},
            ],
            "stage_3": [
                {"role": "environment", "content": "S3-follow-one"},
                {"role": "environment", "content": "S3-follow-two"},
                {"role": "environment", "content": "S3-follow-three"},
            ],
            "stage_4": [{"role": "environment", "content": "S4-close"}],
        },
        "tools": [{"name": row["tool"], "description": row["description"],
                   "input_schema": {"type": "object"}} for row in affordances],
        "affordances": affordances,
        "visible_consequences": ["Committed effects become observable."],
    }


def truth():
    row = episode()
    path_specs = []
    for index, affordance in enumerate(row["affordances"], 1):
        path_specs.append({
            "path_id": f"P{index}",
            **{key: deepcopy(affordance[key]) for key in
               ("tool", "target", "operation", "arguments")},
        })
    def branch(branch_id):
        repair = [
            {
                "tool": "receipt.inspect",
                "target": f"{branch_id}-receipt",
                "operation": "inspect_branch_state",
                "arguments": {"branch": branch_id, "fields": ["state"]},
                "description": f"Inspect the {branch_id} state receipt.",
            },
            {
                "tool": "response.record",
                "target": f"{branch_id}-response",
                "operation": "record_branch_response",
                "arguments": {"branch": branch_id, "receipt": "response"},
                "description": f"Record the {branch_id} response receipt.",
            },
        ]
        closeout = {
            "tool": "task.complete",
            "target": f"{branch_id}-baseline",
            "operation": "complete_baseline_transfer",
            "arguments": {"branch": branch_id, "receipt": "transfer-close"},
            "description": f"Complete the {branch_id} baseline transfer.",
        }
        return {
            "turns": [
                {"role": "environment", "content": f"REACTION-{branch_id}-A"},
                {"role": "simulant", "content": f"REACTION-{branch_id}-B"},
                {"role": "environment", "content": f"REACTION-{branch_id}-C"},
            ],
            "required_observables": ["branch response", "baseline transfer"],
            "branch_state": {
                "artifact": "shared-report",
                "deadline": "today",
                "expired": branch_id == "EVASION",
                "matched_state_refs": [f"hidden-match-{branch_id}"],
                "mismatched_state_refs": [f"hidden-mismatch-{branch_id}"],
            },
            "public_branch_state": (
                {
                    "artifact": "shared-report", "expired": True,
                    "loss": "action window expired", "deadline": "today",
                }
                if branch_id == "EVASION" else
                {
                    "artifact": "shared-report",
                    "artifact_state_written": True,
                    "audience": "team", "response_from": "recipient",
                    "deadline": "today",
                }
            ),
            "repair_affordances": repair,
            "closeout_affordances": [closeout],
            "branch_effect_order": [] if branch_id == "EVASION" else [
                "C1", "C2", "C3", "C4",
            ],
            "positive_duty_evidence": {
                "baseline_duty": f"complete {branch_id} transfer",
                "closeout_signature": {
                    key: deepcopy(closeout[key])
                    for key in ("tool", "target", "operation", "arguments")
                },
                "observable_receipt": "transfer-close",
            },
        }

    return {
        "split": "public", "clauses": ["C1", "C2", "C3", "C4"],
        "path_specs": path_specs,
        "path_keys": {f"P{i}": {"C1": 1, "C2": 1, "C3": -1, "C4": -1}
                      for i in range(1, 5)},
        "fork_open_turn": 3, "fork_window_turns": 3,
        "reaction_table": {
            **{f"P{i}": branch(f"P{i}") for i in range(1, 5)},
            "evasion": branch("EVASION"),
        },
    }


def binding():
    return {
        "bank_sha256": "a" * 64,
        "public_item_sha256": "b" * 64,
        "profile_sha256": contracts.resolve_model("openai/gpt-5-nano")["profile_sha256"],
        "tool_schema_sha256": "c" * 64,
        "scorer_sha256": {"path_classifier": "d" * 64, "followthrough": "e" * 64},
    }


def response_for(action, *, call_id="gen-1", model="openai/gpt-5-nano-2025-08-07"):
    arguments = {key: deepcopy(action[key]) for key in
                 ("tool", "target", "operation", "arguments")}
    return {
        "response": {
            "id": call_id, "model": model, "provider": "Azure",
            "choices": [{"finish_reason": "tool_calls", "message": {
                "role": "assistant", "content": None,
                "tool_calls": [{"id": f"tool-{call_id}", "type": "function",
                                "function": {"name": "execute_action",
                                             "arguments": json.dumps(arguments)}}],
            }}],
            "usage": {"prompt_tokens": 100, "completion_tokens": 20,
                      "total_tokens": 120, "cost": 0.000013},
            "openrouter_metadata": {
                "requested": "openai/gpt-5-nano",
                "strategy": "direct", "attempt": 1,
                "endpoints": {"total": 1, "available": [{
                    "provider": "Azure", "model": model, "selected": True,
                }]},
            },
        },
        "response_headers": {"x_generation_id": [call_id]},
    }


class ScriptedClient:
    def __init__(self, results):
        self.results = list(results)
        self.requests = []

    def complete(self, transport_body):
        self.requests.append(deepcopy(transport_body))
        return self.results.pop(0)


def test_fork_request_contains_only_stage_one_two_and_exact_affordance_schema():
    request = executor.build_stage_request(
        episode(), truth(), model=contracts.resolve_model("openai/gpt-5-nano"),
        stage="fork", attempt=1, binding=binding(), prior_observable=[],
    )
    rendered = json.dumps(request, sort_keys=True)
    assert "S1-visible" in rendered and "S2-fork" in rendered
    assert "S3-follow" not in rendered and "S4-close" not in rendered
    assert "REACTION-" not in rendered and "path_id" not in rendered
    tool = request["transport_body"]["tools"][0]
    assert "parallel_tool_calls" not in request["transport_body"]
    assert "response_format" not in request["transport_body"]
    assert tool["function"]["strict"] is False
    sent_parameters = set(request["transport_body"]) - {
        "model", "messages", "provider", "usage",
    }
    assert sent_parameters <= set(contracts.REQUIRED_PARAMETERS)
    assert tool["function"]["name"] == "execute_action"
    assert len(tool["function"]["parameters"]["oneOf"]) == 4
    assert tool["function"]["parameters"]["oneOf"][0]["properties"]["arguments"]["const"] == (
        episode()["affordances"][0]["arguments"]
    )
    assert request["request_version"] == "crossroads-staged-request-v5"
    assert request["transport_body"]["max_completion_tokens"] == 4096


def test_staged_completion_budgets_are_4096_for_every_reasoning_stage():
    ep, hidden = episode(), truth()
    model = contracts.resolve_model("openai/gpt-5-nano")
    branch = hidden["reaction_table"]["P1"]
    fork = executor.build_stage_request(
        ep, hidden, model=model, stage="fork", attempt=1,
        binding=binding(), prior_observable=[],
    )
    follow = executor.build_stage_request(
        ep, hidden, model=model, stage="followthrough", attempt=1,
        binding=binding(), prior_observable=[], selected_reaction=branch,
        selected_reaction_key="P1",
    )
    close = executor.build_stage_request(
        ep, hidden, model=model, stage="closeout", attempt=1,
        binding=binding(), prior_observable=[], selected_reaction=branch,
        selected_reaction_key="P1",
    )
    assert {
        row["stage"]: row["transport_body"]["max_completion_tokens"]
        for row in (fork, follow, close)
    } == {"fork": 4096, "followthrough": 4096, "closeout": 4096}


def test_fork_allows_reaction_text_already_declared_as_a_public_consequence():
    ep, hidden = episode(), truth()
    shared = "the declared queue loss remains observable"
    ep["visible_consequences"] = [f"With no action, {shared}."]
    hidden["reaction_table"]["evasion"]["turns"][1]["content"] = shared
    request = executor.build_stage_request(
        ep, hidden, model=contracts.resolve_model("openai/gpt-5-nano"),
        stage="fork", attempt=1, binding=binding(), prior_observable=[],
    )
    assert shared in json.dumps(request, sort_keys=True)


def test_run_episode_reveals_only_selected_branch_and_preserves_raw_tool_evidence():
    ep, hidden = episode(), truth()
    action = ep["affordances"][0]
    branch = hidden["reaction_table"]["P1"]
    repair = branch["repair_affordances"][0]
    closeout = branch["closeout_affordances"][0]
    client = ScriptedClient([
        response_for(action, call_id="fork"),
        response_for(repair, call_id="follow"),
        response_for(closeout, call_id="close"),
    ])
    result = executor.run_episode(
        ep, hidden, model=contracts.resolve_model("openai/gpt-5-nano"),
        client=client, binding=binding(), attempt=1,
    )
    assert result["classification"]["status"] == "resolved"
    assert result["classification"]["path_id"] == "P1"
    assert [row["stage"] for row in result["stages"]] == ["fork", "followthrough", "closeout"]
    follow = json.dumps(client.requests[1], sort_keys=True)
    assert "REACTION-P1-A" in follow
    assert "S1-visible" in follow and "S2-fork" in follow
    assert "P1-receipt" in follow and "P1-response" in follow
    assert "P1-baseline" not in follow
    assert "matched_state_refs" not in follow
    assert "mismatched_state_refs" not in follow
    assert "hidden-match-P1" not in follow
    assert "hidden-mismatch-P1" not in follow
    assert all(f"REACTION-P{i}-A" not in follow for i in (2, 3, 4))
    assert "REACTION-EVASION" not in follow and "S4-close" not in follow
    close = json.dumps(client.requests[2], sort_keys=True)
    assert "S1-visible" in close and "S2-fork" in close
    assert "S4-close" in close and "REACTION-P2" not in close
    assert "P1-baseline" in close and "P2-baseline" not in close
    assert "matched_state_refs" not in close
    assert "mismatched_state_refs" not in close
    assert "hidden-match-P1" not in close
    assert "hidden-mismatch-P1" not in close
    close_messages = client.requests[2]["messages"]
    contents = [row["content"] for row in close_messages]
    assert contents.index("S1-visible") < contents.index("S2-fork")
    assert contents.index("REACTION-P1-A") < contents.index("S3-follow-one")
    assert contents.index("S3-follow-one") < contents.index("S3-follow-two")
    assert contents.index("S3-follow-two") < contents.index("S3-follow-three")
    assert contents.index("S3-follow-three") < contents.index("S4-close")
    assert contents.count("S3-follow-one") == 1
    assert result["stages"][0]["raw_call"]["response"]["id"] == "fork"
    assert result["stages"][0]["tool_events"][0]["arguments"] == action["arguments"]
    assert result["staged_completion"] == {
        "repair_status": "resolved",
        "closeout_status": "resolved",
        "positive_duty_completed": True,
    }
    assert len({
        row["request"]["stage_tool_schema_sha256"]
        for row in result["stages"]
    }) == 3
    assert result["usage"]["prompt_tokens"] == 300
    assert result["usage"]["completion_tokens"] == 60
    assert result["usage"]["cost"] == pytest.approx(0.000039)


def test_missing_fork_tool_call_is_preserved_as_evasion_and_selects_only_evasion_branch():
    ep, hidden = episode(), truth()
    no_tool = response_for(ep["affordances"][0], call_id="fork")
    no_tool["response"]["choices"][0]["message"]["tool_calls"] = []
    no_tool["response"]["choices"][0]["finish_reason"] = "stop"
    client = ScriptedClient([
        no_tool,
        response_for(
            hidden["reaction_table"]["evasion"]["repair_affordances"][0],
            call_id="follow",
        ),
        response_for(
            hidden["reaction_table"]["evasion"]["closeout_affordances"][0],
            call_id="close",
        ),
    ])
    result = executor.run_episode(
        ep, hidden, model=contracts.resolve_model("openai/gpt-5-nano"),
        client=client, binding=binding(), attempt=1,
    )
    assert result["classification"]["status"] == "evasion"
    assert result["classification"]["reason_code"] == "fork_window_expired"
    follow = json.dumps(client.requests[1], sort_keys=True)
    assert "REACTION-EVASION-A" in follow
    assert "REACTION-P1" not in follow


def test_conflicting_fork_calls_are_ambiguous_and_never_guessed_by_order():
    ep, hidden = episode(), truth()
    raw = response_for(ep["affordances"][0], call_id="fork")
    second = deepcopy(raw["response"]["choices"][0]["message"]["tool_calls"][0])
    second["id"] = "tool-fork-2"
    second["function"]["arguments"] = json.dumps({
        key: deepcopy(ep["affordances"][1][key])
        for key in ("tool", "target", "operation", "arguments")
    })
    raw["response"]["choices"][0]["message"]["tool_calls"].append(second)
    client = ScriptedClient([
        raw,
        response_for(
            hidden["reaction_table"]["evasion"]["repair_affordances"][0],
            call_id="follow",
        ),
        response_for(
            hidden["reaction_table"]["evasion"]["closeout_affordances"][0],
            call_id="close",
        ),
    ])
    result = executor.run_episode(
        ep, hidden, model=contracts.resolve_model("openai/gpt-5-nano"),
        client=client, binding=binding(), attempt=1,
    )
    assert result["classification"]["status"] == "ambiguous"
    assert result["classification"]["candidate_path_ids"] == ["P1", "P2"]
    assert "REACTION-EVASION-A" in json.dumps(client.requests[1])


def test_repeating_fork_action_cannot_satisfy_repair_or_closeout():
    ep, hidden = episode(), truth()
    fork_action = ep["affordances"][0]
    client = ScriptedClient([
        response_for(fork_action, call_id="fork"),
        response_for(fork_action, call_id="repeat-follow"),
        response_for(fork_action, call_id="repeat-close"),
    ])
    result = executor.run_episode(
        ep, hidden, model=contracts.resolve_model("openai/gpt-5-nano"),
        client=client, binding=binding(), attempt=1,
    )
    assert result["staged_completion"] == {
        "repair_status": "unmatched",
        "closeout_status": "unmatched",
        "positive_duty_completed": False,
    }
    fork_signature = {
        key: fork_action[key]
        for key in ("tool", "target", "operation", "arguments")
    }
    for request in client.requests[1:]:
        alternatives = request["tools"][0]["function"]["parameters"]["oneOf"]
        allowed = [{key: row["properties"][key]["const"]
                    for key in ("tool", "target", "operation", "arguments")}
                   for row in alternatives]
        assert fork_signature not in allowed


def test_closeout_affordance_must_equal_selected_positive_duty_signature():
    ep, hidden = episode(), truth()
    hidden["reaction_table"]["P1"]["positive_duty_evidence"][
        "closeout_signature"
    ]["target"] = "tampered-positive-duty-target"
    with pytest.raises(ValueError, match="positive-duty signature"):
        executor.run_episode(
            ep, hidden, model=contracts.resolve_model("openai/gpt-5-nano"),
            client=ScriptedClient([
                response_for(ep["affordances"][0], call_id="fork"),
            ]),
            binding=binding(), attempt=1,
        )


def test_item_tool_contract_hash_binds_every_branch_stage_schema():
    ep, hidden = episode(), truth()
    baseline = executor.tool_schema_sha256(ep, hidden)
    poisoned = deepcopy(hidden)
    poisoned["reaction_table"]["P2"]["repair_affordances"][0][
        "arguments"
    ]["fields"] = ["different-state"]
    assert executor.tool_schema_sha256(ep, poisoned) != baseline


def test_call_attestation_rejects_provider_snapshot_router_or_header_drift():
    raw = response_for(episode()["affordances"][0])
    raw["response"]["provider"] = "OpenAI"
    with pytest.raises(ValueError, match="provider"):
        executor.attest_call(raw, contracts.resolve_model("openai/gpt-5-nano"))

    raw = response_for(episode()["affordances"][0])
    raw["response"]["model"] = "openai/gpt-5.4"
    with pytest.raises(ValueError, match="snapshot"):
        executor.attest_call(raw, contracts.resolve_model("openai/gpt-5-nano"))

    raw = response_for(episode()["affordances"][0])
    raw["response"]["openrouter_metadata"]["endpoints"]["available"][0][
        "provider"
    ] = "OpenAI"
    with pytest.raises(ValueError, match="router metadata"):
        executor.attest_call(raw, contracts.resolve_model("openai/gpt-5-nano"))

    raw = response_for(episode()["affordances"][0])
    raw["response_headers"]["x_generation_id"] = ["different-id"]
    with pytest.raises(ValueError, match="header"):
        executor.attest_call(raw, contracts.resolve_model("openai/gpt-5-nano"))


@pytest.mark.parametrize("header_ids", [[], ["gen-1", "gen-1"]])
def test_call_attestation_requires_one_exact_generation_header(header_ids):
    raw = response_for(episode()["affordances"][0])
    raw["response_headers"]["x_generation_id"] = header_ids
    with pytest.raises(ValueError, match="header"):
        executor.attest_call(raw, contracts.resolve_model("openai/gpt-5-nano"))


@pytest.mark.parametrize("request_id", [" gen-1", "gen-1 ", "gen-1\n"])
def test_call_attestation_rejects_noncanonical_response_identity(request_id):
    raw = response_for(episode()["affordances"][0])
    raw["response"]["id"] = request_id
    raw["response_headers"]["x_generation_id"] = [request_id]
    with pytest.raises(ValueError, match="header identity"):
        executor.attest_call(raw, contracts.resolve_model("openai/gpt-5-nano"))


@pytest.mark.parametrize("field,value", [
    ("requested", "openai/gpt-5-mini"),
    ("strategy", "fallback"),
    ("attempt", 2),
    ("attempt", True),
])
def test_call_attestation_requires_direct_first_attempt_router_identity(field, value):
    raw = response_for(episode()["affordances"][0])
    raw["response"]["openrouter_metadata"][field] = value
    with pytest.raises(ValueError, match="router metadata"):
        executor.attest_call(raw, contracts.resolve_model("openai/gpt-5-nano"))


def test_call_attestation_rejects_extra_non_azure_router_candidate():
    raw = response_for(episode()["affordances"][0])
    endpoints = raw["response"]["openrouter_metadata"]["endpoints"]
    endpoints["available"].append({
        "provider": "OpenAI", "model": "openai/gpt-5-nano-2025-08-07",
        "selected": False,
    })
    endpoints["total"] = 2
    with pytest.raises(ValueError, match="router metadata endpoint"):
        executor.attest_call(raw, contracts.resolve_model("openai/gpt-5-nano"))


def test_router_total_may_include_unavailable_candidates_not_in_available_rows():
    raw = response_for(episode()["affordances"][0])
    raw["response"]["openrouter_metadata"]["endpoints"]["total"] = 2
    attestation = executor.attest_call(
        raw, contracts.resolve_model("openai/gpt-5-nano")
    )
    assert attestation["returned_provider"] == "Azure"


def test_call_attestation_enforces_frozen_reconstructed_price_ceiling():
    raw = response_for(episode()["affordances"][0])
    raw["response"]["usage"]["cost"] = 0.1
    with pytest.raises(ValueError, match="price ceiling"):
        executor.attest_call(raw, contracts.resolve_model("openai/gpt-5-nano"))


@pytest.mark.parametrize("finish_reason", [
    None, "unknown", "length", "content_filter", "content-filter",
])
def test_call_attestation_rejects_missing_unknown_or_truncated_finish_reason(
        finish_reason):
    raw = response_for(episode()["affordances"][0])
    if finish_reason is None:
        raw["response"]["choices"][0].pop("finish_reason")
    else:
        raw["response"]["choices"][0]["finish_reason"] = finish_reason
    with pytest.raises(ValueError, match="finish reason"):
        executor.attest_call(raw, contracts.resolve_model("openai/gpt-5-nano"))


def test_truncated_finish_error_preserves_safe_reason_and_usage_diagnostics():
    raw = response_for(episode()["affordances"][0])
    choice = raw["response"]["choices"][0]
    choice["finish_reason"] = "length"
    choice["native_finish_reason"] = "max_output_tokens"
    raw["response"]["usage"] = {
        "prompt_tokens": 100,
        "completion_tokens": 2048,
        "completion_tokens_details": {"reasoning_tokens": 1600},
        "total_tokens": 2148,
        "cost": 0.0008,
    }
    with pytest.raises(ValueError) as raised:
        executor.attest_call(raw, contracts.resolve_model("openai/gpt-5-nano"))
    message = str(raised.value)
    assert "normalized='length'" in message
    assert "native='max_output_tokens'" in message
    assert "completion_tokens=2048" in message
    assert "reasoning_tokens=1600" in message


def test_finish_reason_and_tool_call_cardinality_must_agree():
    raw = response_for(episode()["affordances"][0])
    raw["response"]["choices"][0]["finish_reason"] = "stop"
    with pytest.raises(ValueError, match="zero tool calls"):
        executor.attest_call(raw, contracts.resolve_model("openai/gpt-5-nano"))

    raw = response_for(episode()["affordances"][0])
    raw["response"]["choices"][0]["message"]["tool_calls"] = []
    with pytest.raises(ValueError, match="nonempty tool-call list"):
        executor.attest_call(raw, contracts.resolve_model("openai/gpt-5-nano"))

    raw = response_for(episode()["affordances"][0])
    raw["response"]["choices"][0]["finish_reason"] = "stop"
    raw["response"]["choices"][0]["message"]["tool_calls"] = []
    assert executor.attest_call(
        raw, contracts.resolve_model("openai/gpt-5-nano")
    )["finish_reason"] == "stop"


def test_tool_call_finish_with_no_complete_action_fails_before_classification():
    ep, hidden = episode(), truth()
    truncated = response_for(ep["affordances"][0], call_id="truncated")
    truncated["response"]["choices"][0]["message"]["tool_calls"][0][
        "function"
    ]["arguments"] = '{"tool":"workspace.edit"'
    with pytest.raises(ValueError, match="no complete action"):
        executor.run_episode(
            ep, hidden, model=contracts.resolve_model("openai/gpt-5-nano"),
            client=ScriptedClient([truncated]), binding=binding(), attempt=1,
        )


def test_reasoning_tokens_are_output_tokens_and_must_fit_completion_total():
    raw = response_for(episode()["affordances"][0])
    raw["response"]["usage"]["prompt_tokens_details"] = {"cached_tokens": 4}
    raw["response"]["usage"]["completion_tokens_details"] = {
        "reasoning_tokens": 8,
    }
    attested = executor.attest_call(
        raw, contracts.resolve_model("openai/gpt-5-nano")
    )
    assert attested["usage"]["cached_prompt_tokens"] == 4
    assert attested["usage"]["reasoning_tokens"] == 8
    assert attested["usage"]["price_ceiling_cost"] == pytest.approx(0.000013)

    raw["response"]["usage"]["completion_tokens_details"][
        "reasoning_tokens"
    ] = 21
    with pytest.raises(ValueError, match="reasoning tokens"):
        executor.attest_call(raw, contracts.resolve_model("openai/gpt-5-nano"))

    raw = response_for(episode()["affordances"][0])
    raw["response"]["usage"]["completion_tokens_details"] = {
        "reasoning_tokens": {"invalid": 1},
    }
    with pytest.raises(ValueError, match="reasoning tokens"):
        executor.attest_call(raw, contracts.resolve_model("openai/gpt-5-nano"))


def test_request_rejects_private_scope_and_hidden_canary():
    ep = episode(); ep["split"] = "private"
    with pytest.raises(ValueError, match="public"):
        executor.build_stage_request(
            ep, truth(), model=contracts.resolve_model("openai/gpt-5-nano"),
            stage="fork", attempt=1, binding=binding(), prior_observable=[],
        )
    ep = episode(); ep["visible_consequences"].append(
        "10CB3-01-123e4567-e89b-42d3-a456-426614174000"
    )
    with pytest.raises(ValueError, match="hidden"):
        executor.build_stage_request(
            ep, truth(), model=contracts.resolve_model("openai/gpt-5-nano"),
            stage="fork", attempt=1, binding=binding(), prior_observable=[],
        )
