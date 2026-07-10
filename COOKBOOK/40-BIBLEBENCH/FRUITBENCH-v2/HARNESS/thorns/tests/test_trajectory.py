from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from types import SimpleNamespace

import pytest


HARNESS = Path(__file__).resolve().parents[1]
if str(HARNESS) not in sys.path:
    sys.path.insert(0, str(HARNESS))

import model_adapters  # noqa: E402
import run_pilot  # noqa: E402
from synthetic_reference import SyntheticModel  # noqa: E402
from trajectory import BRANCH_BY_LABEL, execute_trajectory  # noqa: E402


def _spec(**overrides):
    values = {
        "name": "scripted",
        "family": "test-family",
        "vendor": "test-vendor",
        "adapter": "synthetic",
        "role": "evaluation",
        "model_id": "test/scripted-v1",
        "actor_id": "A91",
    }
    values.update(overrides)
    return model_adapters.ModelSpec(**values)


class ScriptedModel(model_adapters.ModelAdapter):
    def __init__(self, outputs, *, spec=None):
        super().__init__(spec or _spec())
        self.outputs = list(outputs)
        self.calls = []

    def generate_messages(
        self,
        messages,
        *,
        item,
        gold,
        system=None,
        rollout=0,
        turn=1,
    ):
        self.calls.append(
            {
                "messages": [dict(message) for message in messages],
                "system": system,
                "rollout": rollout,
                "turn": turn,
            }
        )
        text = self.outputs[len(self.calls) - 1]
        return {
            "text": text,
            "intended_path": None,
            "response_id": f"resp-{turn}",
            "request_id": f"req-{turn}",
            "generation_id": f"gen-{turn}",
            "returned_model": "test/scripted-v1",
            "usage": {"input_tokens": turn * 10, "output_tokens": turn},
            "attempt_ledger": [{"attempt": 1, "status_code": 200}],
        }


def _gold():
    return {
        "id": "thorns-unit-003",
        "paths": {
            "fruit": {"label": "Fi", "markers": ["fruit marker"]},
            "vice": {"label": "Wj", "markers": ["vice marker"]},
            "cft": {"label": "CFT", "markers": ["counterfeit marker"]},
        },
    }


def _arc(branches=None):
    branch_map = branches or {
        "fruit_path": "authored fruit follow-up",
        "vice_path": "authored vice follow-up",
        "cft_path": "authored counterfeit follow-up",
    }
    return {
        "id": "thorns-unit-003",
        "format": "escalation_arc",
        "prompt": "Initial context that must persist.",
        "turns": [
            {"beat": 1, "user": "Beat one."},
            {"beat": 2, "user": "Beat two.", "branches": branch_map},
            {"beat": 3, "user": "Beat three."},
            {"beat": 4, "user": "Beat four."},
        ],
    }


def test_single_shot_is_one_message_first_request_with_complete_provenance():
    model = ScriptedModel(["fruit marker"])
    item = {
        "id": "thorns-unit-001",
        "format": "single_shot",
        "prompt": "Single prompt.",
    }

    result = execute_trajectory(
        model,
        item,
        _gold(),
        actor_id="A91",
        model_id="test/scripted-v1",
        system="actor system",
        rollout=7,
    )

    assert model.calls == [
        {
            "messages": [{"role": "user", "content": "Single prompt."}],
            "system": "actor system",
            "rollout": 7,
            "turn": 1,
        }
    ]
    assert len(result.turn_rows) == 1
    row = result.turn_rows[0]
    assert row["actor_id"] == "A91"
    assert row["model_id"] == "test/scripted-v1"
    assert row["turn"] == 1
    assert row["response_id"] == "resp-1"
    assert row["request_id"] == "req-1"
    assert row["generation_id"] == "gen-1"
    assert row["returned_model"] == "test/scripted-v1"
    assert row["usage"] == {"input_tokens": 10, "output_tokens": 1}
    assert row["attempt_ledger"] == [{"attempt": 1, "status_code": 200}]
    assert row["request_messages"] == [
        {"role": "user", "content": "Single prompt."}
    ]
    assert re.fullmatch(r"[0-9a-f]{64}", row["prompt_hash"])
    assert re.fullmatch(r"[0-9a-f]{64}", row["request_hash"])
    assert result.terminal_row["status"] == "completed"
    assert result.terminal_row["turns_completed"] == 1
    assert result.terminal_row["trajectory_id"] == row["trajectory_id"]
    assert result.terminal_output["text"] == "fruit marker"


@pytest.mark.parametrize(
    ("actor_id", "model_id", "match"),
    [
        ("A90", "test/scripted-v1", "actor_id"),
        ("A91", "test/different-v1", "model_id"),
    ],
)
def test_executor_rejects_identity_that_disagrees_with_bound_adapter(
    actor_id, model_id, match
):
    model = ScriptedModel(["fruit marker"])

    with pytest.raises(ValueError, match=match):
        execute_trajectory(
            model,
            {"id": "thorns-unit-001", "format": "single_shot", "prompt": "Prompt."},
            _gold(),
            actor_id=actor_id,
            model_id=model_id,
        )

    assert model.calls == []


def test_four_beat_arc_makes_four_sequential_requests_without_future_leakage():
    model = ScriptedModel(
        ["neutral first reply", "fruit marker", "neutral third reply", "fruit marker"]
    )

    result = execute_trajectory(
        model,
        _arc(),
        _gold(),
        actor_id="A91",
        model_id="test/scripted-v1",
        rollout=0,
    )

    assert result.terminal_row["status"] == "completed"
    assert len(model.calls) == 4
    assert len(result.turn_rows) == 4
    request_texts = [
        "\n".join(message["content"] for message in call["messages"])
        for call in model.calls
    ]
    assert "Initial context that must persist." in request_texts[0]
    assert "Beat one." in request_texts[0]
    assert "Beat two." not in request_texts[0]
    assert "Beat three." not in request_texts[1]
    assert "Beat four." not in request_texts[2]
    assert "neutral first reply" in request_texts[1]
    assert "fruit marker" in request_texts[2]
    assert "authored fruit follow-up" in request_texts[2]
    assert "authored vice follow-up" not in request_texts[2]
    assert "authored counterfeit follow-up" not in request_texts[2]
    assert model.calls[3]["messages"][-2] == {
        "role": "assistant",
        "content": "neutral third reply",
    }


def test_branch_on_first_beat_is_inserted_before_second_beat_only():
    item = _arc()
    item["turns"][0]["branches"] = item["turns"][1].pop("branches")
    model = ScriptedModel(
        ["vice marker", "neutral second reply", "neutral third reply", "fruit marker"]
    )

    result = execute_trajectory(
        model,
        item,
        _gold(),
        actor_id="A91",
        model_id="test/scripted-v1",
    )

    assert result.terminal_row["status"] == "completed"
    assert result.turn_rows[0]["branch_selected"] == "vice_path"
    second_request = "\n".join(
        message["content"] for message in model.calls[1]["messages"]
    )
    assert "authored vice follow-up" in second_request
    assert "Beat two." in second_request
    assert "Beat three." not in second_request


@pytest.mark.parametrize(
    ("response", "branch_key"),
    [
        ("fruit marker", "fruit_path"),
        ("vice marker", "vice_path"),
        ("counterfeit marker", "cft_path"),
        ("fruit marker vice marker", "cft_path"),
    ],
)
def test_declared_branch_rules_select_only_an_explicit_authored_branch(
    response, branch_key
):
    model = ScriptedModel(["neutral", response, "neutral", "fruit marker"])

    result = execute_trajectory(
        model,
        _arc(),
        _gold(),
        actor_id="A91",
        model_id="test/scripted-v1",
    )

    assert BRANCH_BY_LABEL == {
        "Fi": "fruit_path",
        "Wj": "vice_path",
        "CFT": "cft_path",
        "mixed": "cft_path",
    }
    assert result.terminal_row["status"] == "completed"
    assert result.turn_rows[1]["branch_selected"] == branch_key
    next_request = "\n".join(
        message["content"] for message in model.calls[2]["messages"]
    )
    selected = _arc()["turns"][1]["branches"][branch_key]
    assert selected in next_request
    for key, authored in _arc()["turns"][1]["branches"].items():
        if key != branch_key:
            assert authored not in next_request


@pytest.mark.parametrize(
    ("branches", "reason"),
    [
        ({"vice_path": "v", "cft_path": "c"}, "missing_authored_branch"),
        ({"fruit_path": "", "vice_path": "v", "cft_path": "c"}, "malformed_authored_branch"),
        ("not-a-map", "malformed_branches"),
    ],
)
def test_missing_or_malformed_branch_stops_before_another_model_call(branches, reason):
    model = ScriptedModel(["neutral", "fruit marker", "must not be requested"])
    item = _arc()
    item["turns"][1]["branches"] = branches

    result = execute_trajectory(
        model,
        item,
        _gold(),
        actor_id="A91",
        model_id="test/scripted-v1",
    )

    assert len(model.calls) == 2
    assert len(result.turn_rows) == 2
    assert result.terminal_row["status"] == "stopped"
    assert result.terminal_row["stop_reason"] == reason
    assert result.terminal_row["turns_completed"] == 2


def test_unresolved_branch_response_stops_and_fresh_rollouts_have_no_state_leak():
    model = ScriptedModel(
        [
            "neutral one",
            "unclassifiable reply",
            "neutral two",
            "unclassifiable reply",
        ]
    )

    first = execute_trajectory(
        model,
        _arc(),
        _gold(),
        actor_id="A91",
        model_id="test/scripted-v1",
        rollout=0,
    )
    second = execute_trajectory(
        model,
        _arc(),
        _gold(),
        actor_id="A91",
        model_id="test/scripted-v1",
        rollout=1,
    )

    assert first.terminal_row["stop_reason"] == "unresolved_branch"
    assert second.terminal_row["stop_reason"] == "unresolved_branch"
    assert len(model.calls) == 4
    assert model.calls[0]["messages"] == model.calls[2]["messages"]
    assert model.calls[2]["rollout"] == 1
    assert first.terminal_row["trajectory_id"] != second.terminal_row["trajectory_id"]


def test_surface_and_assignment_identity_prevent_counterbalanced_cue_collisions():
    model = ScriptedModel(["first", "second"])
    item = {"id": "thorns-unit-001", "format": "single_shot", "prompt": "Prompt."}
    first = execute_trajectory(
        model,
        item,
        _gold(),
        actor_id="A91",
        model_id="test/scripted-v1",
        rollout=0,
        surface_id="thorns-unit-001-C0",
        assignment_id="asg-001",
    )
    second = execute_trajectory(
        model,
        item,
        _gold(),
        actor_id="A91",
        model_id="test/scripted-v1",
        rollout=0,
        surface_id="thorns-unit-001-C1",
        assignment_id="asg-002",
    )
    assert first.terminal_row["trajectory_id"] != second.terminal_row["trajectory_id"]
    assert first.terminal_row["surface_id"] == "thorns-unit-001-C0"
    assert second.turn_rows[0]["assignment_id"] == "asg-002"


def test_marker_branch_routing_is_rejected_for_live_adapters_before_any_call():
    live = ScriptedModel(
        ["fruit marker"],
        spec=_spec(adapter="openrouter", model_id="test/live-v1"),
    )

    with pytest.raises(ValueError, match="synthetic-only"):
        execute_trajectory(
            live,
            _arc(),
            _gold(),
            actor_id="A91",
            model_id="test/live-v1",
            branch_strategy="synthetic_marker",
        )

    assert live.calls == []


def test_live_counterbalanced_branches_are_response_independent_and_rollout_balanced():
    selected = []
    for rollout in range(6):
        live = ScriptedModel(
            ["fruit marker", "fruit marker", "fruit marker", "fruit marker"],
            spec=_spec(adapter="openrouter", model_id="test/live-v1"),
        )
        result = execute_trajectory(
            live,
            _arc(),
            _gold(),
            actor_id="A91",
            model_id="test/live-v1",
            rollout=rollout,
            branch_strategy="counterbalanced",
        )
        selected.append(result.turn_rows[1]["branch_selected"])
        next_request = "\n".join(
            message["content"] for message in live.calls[2]["messages"]
        )
        expected_text = _arc()["turns"][1]["branches"][selected[-1]]
        assert expected_text in next_request

    assert {key: selected.count(key) for key in set(selected)} == {
        "fruit_path": 2,
        "vice_path": 2,
        "cft_path": 2,
    }


def test_unknown_branch_strategy_fails_before_any_actor_request():
    model = ScriptedModel(["fruit marker"])
    with pytest.raises(ValueError, match="branch_strategy"):
        execute_trajectory(
            model,
            _arc(),
            _gold(),
            actor_id="A91",
            model_id="test/scripted-v1",
            branch_strategy="adaptive_magic",
        )
    assert model.calls == []


@dataclass(frozen=True)
class FakeAttempt:
    attempt: int = 1
    status_code: int = 200
    error_type: str | None = None


class FakeOpenRouterClient:
    def __init__(self):
        self.calls = []

    def responses(self, **kwargs):
        self.calls.append(kwargs)
        return SimpleNamespace(
            text="wrapper response",
            response_id="or-resp",
            request_id="or-req",
            generation_id="or-gen",
            requested_model=kwargs["model_id"],
            returned_model="openai/gpt-5.4",
            usage={"input_tokens": 11, "output_tokens": 3},
            attempt_ledger=(FakeAttempt(),),
            router_metadata={"provider": "OpenAI"},
            routing_headers={"x-openrouter-provider": "OpenAI"},
            attempts=1,
            latency_ms=12.5,
            service_tier="default",
        )


def test_openrouter_adapter_uses_shared_responses_client_and_maps_provenance():
    client = FakeOpenRouterClient()
    spec = _spec(
        adapter="openrouter",
        model_id="openai/gpt-5.4",
        params={
            "max_output_tokens": 900,
            "reasoning_effort": "medium",
            "provider_order": ["OpenAI"],
            "expected_canonical_slug": "openai/gpt-5.4",
        },
    )
    model = model_adapters.OpenRouterModel(spec, client=client)

    output = model.generate_messages(
        [{"role": "user", "content": "current"}],
        item={"id": "thorns-unit-001"},
        gold=_gold(),
        system="system text",
        rollout=2,
        turn=3,
    )

    assert client.calls == [
        {
            "model_id": "openai/gpt-5.4",
            "messages": [
                {"role": "system", "content": "system text"},
                {"role": "user", "content": "current"},
            ],
            "max_output_tokens": 900,
            "reasoning_effort": "medium",
            "provider_order": ["OpenAI"],
            "expected_canonical_slug": "openai/gpt-5.4",
            "service_tier": "default",
        }
    ]
    assert output["text"] == "wrapper response"
    assert output["response_id"] == "or-resp"
    assert output["request_id"] == "or-req"
    assert output["generation_id"] == "or-gen"
    assert output["returned_model"] == "openai/gpt-5.4"
    assert output["attempt_ledger"] == [
        {"attempt": 1, "status_code": 200, "error_type": None}
    ]


def test_synthetic_model_is_message_first_deterministic_and_scores_terminal_only():
    cfg = run_pilot.load_config(HARNESS / "pilot_config.json")
    bank, gold = run_pilot.load_items(cfg)
    item = bank["thorns-craving-003"]
    spec = model_adapters.ModelSpec(
        name="synthetic-test",
        family="synthetic-test-family",
        vendor="synthetic-test-vendor",
        adapter="synthetic",
        role="evaluation",
        profile="aligned_high",
        actor_id="A92",
        model_id="synthetic/aligned-high",
        params={
            "seed": 20260710,
            "reference_path": cfg["paths"]["synthetic_reference"],
        },
    )
    model = SyntheticModel(spec)

    result = execute_trajectory(
        model,
        item,
        gold[item["id"]],
        actor_id="A92",
        model_id="synthetic/aligned-high",
        rollout=4,
    )

    assert result.terminal_row["status"] == "completed"
    assert len(result.turn_rows) == 4
    assert result.terminal_output["intended_path"] in {"Fi", "Wj", "CFT", "mixed"}
    assert {
        row["intended_path"] for row in result.turn_rows
    } == {result.terminal_output["intended_path"]}


def test_pilot_retains_opaque_actor_identity_in_evaluation_aggregation():
    cfg = run_pilot.load_config(HARNESS / "pilot_config.json")

    result = run_pilot.run(cfg)

    first = result["ev"][sorted(result["ev"])[0]]
    assert set(first["by_actor"]) == {"A05", "A06", "A07"}
    assert all(
        re.fullmatch(r"A[0-9]{2}", actor_id) for actor_id in first["by_actor"]
    )
    assert all(
        details["model_id"].startswith("synthetic/")
        for details in first["by_actor"].values()
    )
    assert len(result["actor_rows"]) > result["scorer_self_check"]["n"]
    assert len(result["terminal_rows"]) == result["scorer_self_check"]["n"]
    assert all("actor_id" in row and "model_id" in row for row in result["actor_rows"])
    assert result["scorer_self_check"] == {"n": 3300, "agreement": 1.0}


def test_request_hash_is_canonical_and_changes_with_history():
    model = ScriptedModel(["neutral", "fruit marker", "neutral", "fruit marker"])
    result = execute_trajectory(
        model,
        _arc(),
        _gold(),
        actor_id="A91",
        model_id="test/scripted-v1",
    )

    request_hashes = [row["request_hash"] for row in result.turn_rows]
    assert len(set(request_hashes)) == 4
    assert json.dumps(result.terminal_row, sort_keys=True)


def test_request_hash_binds_generation_controls_not_just_visible_messages():
    item = {"id": "thorns-unit-001", "format": "single_shot", "prompt": "Same."}
    first = execute_trajectory(
        ScriptedModel(["fruit marker"], spec=_spec(params={"temperature": 0})),
        item,
        _gold(),
        actor_id="A91",
        model_id="test/scripted-v1",
    )
    second = execute_trajectory(
        ScriptedModel(["fruit marker"], spec=_spec(params={"temperature": 1})),
        item,
        _gold(),
        actor_id="A91",
        model_id="test/scripted-v1",
    )

    assert first.turn_rows[0]["request_hash"] != second.turn_rows[0]["request_hash"]
