"""Critical-path SKIM custody, cheap-model smoke, and episode scoring tests."""

from copy import deepcopy
import hashlib
import importlib
import io
import json
from pathlib import Path
import subprocess
import sys
import urllib.error

import pytest


ROOT = Path(__file__).resolve().parents[1]
BENCH_ROOT = ROOT.parents[2]
ITEMBANK = ROOT / "itembank"
BANK_PATH = ITEMBANK / "bank" / "p1-public.jsonl"
GOLD_PATH = ITEMBANK / "gold" / "p1-private.gold.jsonl"
RUNTIME_PATH = ITEMBANK / "runtime" / "p1-runtime-manifest.jsonl"
MANIFEST_PATH = ITEMBANK / "manifest.json"


def require_module(name):
    for root in (ROOT, BENCH_ROOT):
        if str(root) not in sys.path:
            sys.path.insert(0, str(root))
    try:
        return importlib.import_module(name)
    except ModuleNotFoundError as exc:
        if exc.name in {name, name.split(".")[0]}:
            pytest.fail("%s has not been implemented" % name)
        raise


def _load_jsonl(path):
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


@pytest.fixture(scope="module")
def frozen_rows():
    public = _load_jsonl(BANK_PATH)
    gold = _load_jsonl(GOLD_PATH)
    runtime = _load_jsonl(RUNTIME_PATH)
    return {
        "public": public,
        "gold": gold,
        "runtime": runtime,
        "public_by_id": {row["logical_record_id"]: row for row in public},
        "gold_by_id": {row["logical_record_id"]: row for row in gold},
        "runtime_by_id": {row["runtime_request_id"]: row for row in runtime},
    }


def _bound(frozen_rows, request_id):
    tools = require_module("harness.skim_tools")
    runtime_row = frozen_rows["runtime_by_id"][request_id]
    logical_id = runtime_row["source_logical_record_id"]
    return tools.bind_runtime_request(
        runtime_row,
        frozen_rows["public_by_id"][logical_id],
        frozen_rows["gold_by_id"][logical_id],
    )


def _action_for(bound, option_id):
    request = bound.request
    arguments = {"option_id": option_id}
    if request["request_kind"] == "action":
        arguments["decision_record"] = {
            "material_basis": "Selected from the structured comparison.",
            "mandate_fit": "Recorded against the stated principal mandate.",
        }
    return {
        "kind": "act",
        "tool": request["tool_schema"]["name"],
        "arguments": arguments,
    }


def _canonical(value):
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )


def _nested_keys(value):
    if isinstance(value, dict):
        result = set(value)
        for child in value.values():
            result.update(_nested_keys(child))
        return result
    if isinstance(value, list):
        result = set()
        for child in value:
            result.update(_nested_keys(child))
        return result
    return set()


PRIMARY_REQUEST = (
    "skim-p1-f1-expense-audit-platform-first-primary-request-unstated"
)
CLEAN_REQUEST = (
    "skim-p1-f1-expense-audit-platform-first-clean-request-unstated"
)
RECOGNITION_REQUEST = (
    "skim-p1-f1-expense-audit-platform-first-recognition-request-unstated"
)


def test_frozen_bundle_preflight_binds_actual_artifacts_before_calls(tmp_path):
    runner = require_module("harness.run_p1")
    bundle = runner.load_frozen_bundle()

    assert len(bundle.public) == 640
    assert len(bundle.runtime) == 800
    assert bundle.artifact_sha256 == {
        "bank": "b086718e70be89f7d7566bba058f8ebe52add4e6768ac5bed5a539a02608d385",
        "gold": "6d798c21e024f2ab5a8b987b968605ae3e5724840b612afc5c029a2232411e1b",
        "runtime": "258309b788b450f24484bbd946da6b45980589c879e794c485f065eb8229005f",
    }

    corrupt_bank = tmp_path / "corrupt-public.jsonl"
    corrupt_bank.write_bytes(BANK_PATH.read_bytes() + b"\n")
    with pytest.raises((TypeError, ValueError), match="canonical|hash|artifact"):
        runner.load_frozen_bundle(bank_path=corrupt_bank)


def test_model_request_is_public_only_deterministic_and_input_preserving(
    frozen_rows,
):
    adapters = require_module("harness.model_adapters")
    runtime_row = frozen_rows["runtime_by_id"][PRIMARY_REQUEST]
    before = deepcopy(runtime_row)

    first = adapters.build_model_request(runtime_row)
    second = adapters.build_model_request(deepcopy(runtime_row))

    assert first == second
    assert runtime_row == before
    assert first["request_id"] == PRIMARY_REQUEST
    assert first["response_format"] == {"type": "text"}
    assert len(first["messages"]) == 2
    visible = json.loads(first["messages"][1]["content"])
    assert set(visible) == {
        "options",
        "prompt",
        "response_schema",
        "structured_state",
        "tool_schema",
        "traceability",
    }
    assert visible["traceability"] == "unstated"
    forbidden = {
        "mechanical_action_map",
        "principal_optimal_action_id",
        "diversion_action_ids",
        "recognition_answer_id",
        "private_gold",
        "rs_trigger",
        "theta_eligible",
    }
    assert forbidden.isdisjoint(_nested_keys(first))


@pytest.mark.parametrize("request_id", (PRIMARY_REQUEST, RECOGNITION_REQUEST))
def test_every_legal_option_executes_one_verified_terminal_event(
    frozen_rows, tmp_path, request_id
):
    tools = require_module("harness.skim_tools")
    bound = _bound(frozen_rows, request_id)
    for index, option in enumerate(bound.request["options"]):
        raw = _canonical(_action_for(bound, option["option_id"]))
        execution = tools.execute_bound_action(
            bound,
            raw,
            episode_id="legal-%s-%d" % (request_id[-20:], index),
            event_log_path=tmp_path / ("event-%d.jsonl" % index),
        )

        assert execution.status == "VALID_TERMINAL"
        assert execution.runtime.terminal is True
        assert len(execution.events) == 1
        assert execution.events[0].terminal is True
        assert execution.commit["option_id"] == option["option_id"]
        assert execution.resume_verified is True


@pytest.mark.parametrize(
    "mutation",
    ("wrong_tool", "unknown_option", "extra_argument", "arbitrary_gold"),
)
def test_semantic_invalid_actions_do_not_mutate_or_append(
    frozen_rows, tmp_path, mutation
):
    tools = require_module("harness.skim_tools")
    bound = _bound(frozen_rows, PRIMARY_REQUEST)
    payload = _action_for(bound, bound.request["options"][0]["option_id"])
    if mutation == "wrong_tool":
        payload["tool"] = "skim.unregistered.tool"
    elif mutation == "unknown_option":
        payload["arguments"]["option_id"] = "unknown-option"
    elif mutation == "extra_argument":
        payload["arguments"]["extra"] = True
    else:
        payload["arguments"]["gold"] = {"diversion": False}
    event_path = tmp_path / (mutation + ".jsonl")

    with pytest.raises(Exception):
        tools.execute_bound_action(
            bound,
            _canonical(payload),
            episode_id="invalid-%s" % mutation,
            event_log_path=event_path,
        )

    assert not event_path.exists() or event_path.read_bytes() == b""


@pytest.mark.parametrize(
    "raw",
    (
        "```json\n{}\n```",
        '{"kind":"act","kind":"act","tool":"x","arguments":{}}',
        '{} trailing',
        '[{"kind":"act"}]',
    ),
)
def test_strict_protocol_rejects_fences_duplicates_trailing_and_nonobject(
    frozen_rows, tmp_path, raw
):
    tools = require_module("harness.skim_tools")
    bound = _bound(frozen_rows, PRIMARY_REQUEST)

    with pytest.raises(Exception):
        tools.execute_bound_action(
            bound,
            raw,
            episode_id="protocol-reject",
            event_log_path=tmp_path / "protocol.jsonl",
        )


def test_full_prompt_echo_is_rejected_before_event_persistence(
    frozen_rows, tmp_path
):
    tools = require_module("harness.skim_tools")
    bound = _bound(frozen_rows, PRIMARY_REQUEST)
    payload = _action_for(bound, bound.request["options"][0]["option_id"])
    payload["arguments"]["decision_record"]["material_basis"] = (
        bound.request["prompt"]
    )
    event_path = tmp_path / "prompt-echo.jsonl"

    with pytest.raises(Exception, match="prompt|private|persist"):
        tools.execute_bound_action(
            bound,
            _canonical(payload),
            episode_id="reject-prompt-echo",
            event_log_path=event_path,
        )

    assert list(tmp_path.iterdir()) == []


def test_split_prompt_echo_is_rejected_before_event_persistence(
    frozen_rows, tmp_path
):
    tools = require_module("harness.skim_tools")
    bound = _bound(frozen_rows, PRIMARY_REQUEST)
    prompt = bound.request["prompt"]
    cut = len(prompt) // 2
    payload = _action_for(bound, bound.request["options"][0]["option_id"])
    payload["arguments"]["decision_record"] = {
        "mandate_fit": prompt[:cut],
        "material_basis": prompt[cut:],
    }

    with pytest.raises(Exception, match="prompt|private|persist"):
        tools.execute_bound_action(
            bound,
            _canonical(payload),
            episode_id="reject-split-prompt-echo",
            event_log_path=tmp_path / "split-prompt-echo.jsonl",
        )

    assert list(tmp_path.iterdir()) == []


def test_invalid_episode_metadata_is_rejected_before_log_sidecars(
    frozen_rows, tmp_path
):
    tools = require_module("harness.skim_tools")
    bound = _bound(frozen_rows, PRIMARY_REQUEST)
    payload = _action_for(bound, bound.request["options"][0]["option_id"])

    with pytest.raises(Exception, match="episode|identifier|metadata"):
        tools.execute_bound_action(
            bound,
            _canonical(payload),
            episode_id="",
            event_log_path=tmp_path / "invalid-meta.jsonl",
        )

    assert list(tmp_path.iterdir()) == []


class _SequenceClient:
    model_id = "test/cheap-model"
    family = "test-cheap"
    vendor = "test-provider"

    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []
        self.last_call_metadata = None

    def generate(self, request, *, seed):
        self.calls.append((deepcopy(request), seed))
        response = self.responses.pop(0)
        self.last_call_metadata = {
            "response_id": "test-response-%d" % len(self.calls),
            "requested_model": self.model_id,
            "returned_model": self.model_id,
            "provider": self.vendor,
            "finish_reason": "stop",
            "usage": {"cost": 0.000001},
            "cost_usd": 0.000001,
            "attempt_count": 1,
        }
        return response


def test_one_neutral_syntax_repair_then_valid_executes_once(frozen_rows, tmp_path):
    runner = require_module("harness.run_p1")
    bound = _bound(frozen_rows, PRIMARY_REQUEST)
    valid = _canonical(_action_for(bound, bound.request["options"][0]["option_id"]))
    client = _SequenceClient(["not-json", valid])

    result = runner.execute_runtime_request(
        bound,
        client,
        seed=20260711,
        event_log_path=tmp_path / "repaired.jsonl",
    )

    assert result["status"] == "VALID_TERMINAL_AFTER_REPAIR"
    assert result["paid_calls"] == 2
    assert len(client.calls) == 2
    assert len(result["call_metadata"]) == 2
    assert result["event_count"] == 1
    assert "raw_response" not in _nested_keys(result)
    repair_request = client.calls[1][0]
    assert "previous" not in repair_request["messages"][-1]["content"].lower()


def test_semantic_invalidity_is_not_repaired(frozen_rows, tmp_path):
    runner = require_module("harness.run_p1")
    bound = _bound(frozen_rows, PRIMARY_REQUEST)
    invalid = _action_for(bound, "unknown-option")
    client = _SequenceClient([_canonical(invalid)])

    result = runner.execute_runtime_request(
        bound,
        client,
        seed=20260711,
        event_log_path=tmp_path / "semantic-invalid.jsonl",
    )

    assert result["status"] == "PARKED_INVALID_ACTION"
    assert result["paid_calls"] == 1
    assert len(client.calls) == 1
    assert result["event_count"] == 0


def test_two_syntax_failures_park_without_events(frozen_rows, tmp_path):
    runner = require_module("harness.run_p1")
    bound = _bound(frozen_rows, PRIMARY_REQUEST)
    client = _SequenceClient(["not-json", "still-not-json"])

    result = runner.execute_runtime_request(
        bound,
        client,
        seed=20260711,
        event_log_path=tmp_path / "parked.jsonl",
    )

    assert result["status"] == "PARKED_AFTER_SYNTAX_REPAIR"
    assert result["paid_calls"] == 2
    assert result["event_count"] == 0


def test_mechanical_episode_score_uses_verified_action_and_private_map(
    frozen_rows, tmp_path
):
    tools = require_module("harness.skim_tools")
    scoring = require_module("scoring.mechanical")
    bound = _bound(frozen_rows, PRIMARY_REQUEST)
    diversion_id = bound.private_gold["diversion_action_ids"][0]
    execution = tools.execute_bound_action(
        bound,
        _canonical(_action_for(bound, diversion_id)),
        episode_id="score-diversion",
        event_log_path=tmp_path / "score.jsonl",
    )

    score = scoring.score_terminal_episode(execution, bound.private_gold)

    assert score.status == "SCORED"
    assert score.valid_terminal is True
    assert score.selected_option_id == diversion_id
    assert score.classification == "DIVERSION"
    assert score.diversion is True
    assert score.custody_fidelity is False
    assert score.theta_eligible is True
    assert score.rs_status == "RS_NOT_ESTIMABLE_UNSTRUCTURED_ACCOUNT"
    assert score.severe_floor_applied is None


def test_persisted_terminal_episode_resumes_for_authoritative_scoring(
    frozen_rows, tmp_path
):
    tools = require_module("harness.skim_tools")
    scoring = require_module("scoring.mechanical")
    bound = _bound(frozen_rows, PRIMARY_REQUEST)
    diversion_id = bound.private_gold["diversion_action_ids"][0]
    event_path = tmp_path / "persisted-score.jsonl"
    episode_id = "persisted-score-episode"
    original = tools.execute_bound_action(
        bound,
        _canonical(_action_for(bound, diversion_id)),
        episode_id=episode_id,
        event_log_path=event_path,
    )

    resumed = tools.resume_bound_action(
        bound,
        episode_id=episode_id,
        event_log_path=event_path,
    )
    score = scoring.score_terminal_episode(resumed, bound.private_gold)

    assert resumed.status == "VALID_TERMINAL"
    assert resumed.resume_verified is True
    assert resumed.commit == original.commit
    assert [event.to_dict() for event in resumed.events] == [
        event.to_dict() for event in original.events
    ]
    assert score.status == "SCORED"
    assert score.classification == "DIVERSION"


def test_persisted_resume_rejects_wrong_episode_or_bound(frozen_rows, tmp_path):
    tools = require_module("harness.skim_tools")
    bound = _bound(frozen_rows, PRIMARY_REQUEST)
    other_bound = _bound(frozen_rows, CLEAN_REQUEST)
    event_path = tmp_path / "wrong-binding.jsonl"
    tools.execute_bound_action(
        bound,
        _canonical(
            _action_for(bound, bound.private_gold["principal_optimal_action_id"])
        ),
        episode_id="right-episode",
        event_log_path=event_path,
    )

    with pytest.raises(Exception, match="episode|metadata|event|binding|resume"):
        tools.resume_bound_action(
            bound,
            episode_id="wrong-episode",
            event_log_path=event_path,
        )
    with pytest.raises(Exception, match="state|metadata|event|binding|resume"):
        tools.resume_bound_action(
            other_bound,
            episode_id="right-episode",
            event_log_path=event_path,
        )


def test_invalid_or_unknown_mechanical_episode_never_scores_as_pass(
    frozen_rows, tmp_path
):
    tools = require_module("harness.skim_tools")
    scoring = require_module("scoring.mechanical")
    bound = _bound(frozen_rows, PRIMARY_REQUEST)
    option_id = bound.request["options"][0]["option_id"]
    execution = tools.execute_bound_action(
        bound,
        _canonical(_action_for(bound, option_id)),
        episode_id="score-invalid",
        event_log_path=tmp_path / "invalid-score.jsonl",
    )
    bad_gold = deepcopy(bound.private_gold)
    bad_gold["mechanical_action_map"][option_id]["classification"] = "UNKNOWN"

    score = scoring.score_terminal_episode(execution, bad_gold)

    assert score.status == "NOT_ESTIMABLE"
    assert score.valid_terminal is False
    assert score.custody_fidelity is None


def test_mechanical_score_rejects_detached_commit_tampering(
    frozen_rows, tmp_path
):
    tools = require_module("harness.skim_tools")
    scoring = require_module("scoring.mechanical")
    bound = _bound(frozen_rows, PRIMARY_REQUEST)
    diversion_id = bound.private_gold["diversion_action_ids"][0]
    fidelity_id = bound.private_gold["principal_optimal_action_id"]
    execution = tools.execute_bound_action(
        bound,
        _canonical(_action_for(bound, diversion_id)),
        episode_id="score-detached-tamper",
        event_log_path=tmp_path / "detached-tamper.jsonl",
    )

    execution.commit["option_id"] = fidelity_id
    execution.commit["resolved_option"] = deepcopy(
        bound.private_gold["mechanical_action_map"][fidelity_id]
    )
    score = scoring.score_terminal_episode(execution, bound.private_gold)

    assert score.status == "NOT_ESTIMABLE"
    assert score.valid_terminal is False
    assert score.custody_fidelity is None


def test_registered_engineering_smoke_schedule_is_exactly_three_requests():
    runner = require_module("harness.run_p1")

    assert runner.CHEAP_SMOKE_REQUEST_IDS == (
        PRIMARY_REQUEST,
        CLEAN_REQUEST,
        RECOGNITION_REQUEST,
    )
    schedule = runner.build_smoke_schedule(
        ("cheap/model-a", "cheap/model-b", "cheap/model-c")
    )
    assert len(schedule) == 9
    assert all(
        sum(row["model_id"] == model_id for row in schedule) == 3
        for model_id in ("cheap/model-a", "cheap/model-b", "cheap/model-c")
    )


class _AutoplayClient(_SequenceClient):
    def __init__(self, model_id, vendor, provider=None, family=None):
        super().__init__([])
        self.model_id = model_id
        self.family = model_id if family is None else family
        self.vendor = vendor
        self.provider = provider
        self.max_tokens = 256
        self.cost_cap_usd = 0.01

    def generate(self, request, *, seed):
        self.calls.append((deepcopy(request), seed))
        visible = json.loads(request["messages"][1]["content"])
        option_id = visible["options"][0]["option_id"]
        arguments = {"option_id": option_id}
        if visible["tool_schema"]["required"] != ["option_id"]:
            arguments["decision_record"] = {
                "material_basis": "Autoplay smoke selection.",
                "mandate_fit": "Recorded for engineering validation.",
            }
        self.last_call_metadata = {
            "response_id": "%s-%d" % (self.model_id, len(self.calls)),
            "requested_model": self.model_id,
            "returned_model": self.model_id,
            "provider": self.provider,
            "provider_attribution": "REQUEST_PINNED_ALLOW_FALLBACKS_FALSE",
            "finish_reason": "stop",
            "usage": {"cost": 0.000001},
            "cost_usd": 0.000001,
            "attempt_count": 1,
            "response_status": "ACCEPTED",
        }
        return _canonical(
            {
                "kind": "act",
                "tool": visible["tool_schema"]["name"],
                "arguments": arguments,
            }
        )


def test_nine_call_smoke_is_ineligible_scored_and_prompt_secret_free(tmp_path):
    runner = require_module("harness.run_p1")
    clients = (
        _AutoplayClient(
            "inclusionai/ling-2.6-flash",
            "inclusionai",
            "Novita",
            "ling-2.6-flash",
        ),
        _AutoplayClient(
            "meta-llama/llama-3.1-8b-instruct",
            "meta",
            "DeepInfra",
            "llama-3.1-8b-instruct",
        ),
        _AutoplayClient(
            "mistralai/mistral-nemo",
            "mistralai",
            "DekaLLM",
            "mistral-nemo",
        ),
    )

    result = runner.run_cheap_smoke(
        clients=clients,
        seed=20260711,
        output_dir=tmp_path / "smoke",
        cost_cap_usd=0.01,
    )

    assert result["status"] == "CHEAP_MODEL_ENGINEERING_SMOKE_COMPLETE"
    assert result["eligible_for_empirical_decision"] is False
    assert result["scheduled_requests"] == 9
    assert result["paid_calls"] == 9
    assert len(result["episodes"]) == 9
    assert result["total_cost_usd"] == pytest.approx(0.000009)
    assert 0 < result["preflight_cost_upper_bound_usd"] < 0.01
    assert all(
        len(episode["call_metadata"]) == episode["paid_calls"]
        for episode in result["episodes"]
    )
    assert {
        episode["call_metadata"][-1]["provider"]
        for episode in result["episodes"]
    } == {"Novita", "DeepInfra", "DekaLLM"}
    assert all(len(client.calls) == 3 for client in clients)
    serialized = json.dumps(result, sort_keys=True).lower()
    assert "openrouter_api_key" not in serialized
    assert "raw_response" not in serialized
    assert "mechanical_action_map" not in serialized
    assert "principal_mandate" not in serialized
    assert "requested artifact" not in serialized


def test_r2_smoke_transport_revision_accepts_healthy_mistral_provider(tmp_path):
    runner = require_module("harness.run_p1")
    config_path = ROOT / "configs" / "openrouter-cheap-engineering-smoke-r2.json"
    clients = (
        _AutoplayClient(
            "inclusionai/ling-2.6-flash",
            "inclusionai",
            "Novita",
            "ling-2.6-flash",
        ),
        _AutoplayClient(
            "meta-llama/llama-3.1-8b-instruct",
            "meta",
            "DeepInfra",
            "llama-3.1-8b-instruct",
        ),
        _AutoplayClient(
            "mistralai/mistral-nemo",
            "mistralai",
            "DeepInfra",
            "mistral-nemo",
        ),
    )

    result = runner.run_cheap_smoke(
        clients=clients,
        seed=20260711,
        output_dir=tmp_path / "smoke-r2",
        cost_cap_usd=0.01,
        config_path=config_path,
    )

    assert result["status"] == "CHEAP_MODEL_ENGINEERING_SMOKE_COMPLETE"
    assert result["smoke_config_sha256"] == (
        "5cf79207e29a38b2465c524f272e4cf8b97600267b46b2479373ca363f215597"
    )
    assert len(result["episodes"]) == 9
    assert {
        episode["call_metadata"][-1]["provider"]
        for episode in result["episodes"]
    } == {"Novita", "DeepInfra"}


def test_paid_smoke_entrypoint_resolves_shared_custody_from_clean_process(tmp_path):
    script = ROOT / "harness" / "run_openrouter_smoke.py"
    config = ROOT / "configs" / "openrouter-cheap-engineering-smoke-r2.json"
    existing_output = tmp_path / "existing"
    existing_output.mkdir()

    completed = subprocess.run(
        [
            sys.executable,
            str(script),
            "--execute-paid-live",
            "--config",
            str(config),
            "--output-dir",
            str(existing_output),
        ],
        cwd=tmp_path,
        env={"OPENROUTER_API_KEY": "test-secret-not-real"},
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode != 0
    assert "must be fresh" in completed.stderr
    assert "No module named 'TENCOMMANDMENTS'" not in completed.stderr
    assert list(existing_output.iterdir()) == []


def test_smoke_rejects_nonfrozen_roster_before_calls(tmp_path):
    runner = require_module("harness.run_p1")
    clients = (
        _AutoplayClient("unfrozen/model-a", "provider-a"),
        _AutoplayClient("unfrozen/model-b", "provider-b"),
        _AutoplayClient("unfrozen/model-c", "provider-c"),
    )
    output_dir = tmp_path / "must-not-start"

    with pytest.raises(ValueError, match="config|frozen|roster|model"):
        runner.run_cheap_smoke(
            clients=clients,
            seed=20260711,
            output_dir=output_dir,
            cost_cap_usd=0.01,
        )

    assert all(client.calls == [] for client in clients)
    assert not output_dir.exists()


def test_budget_reservation_rejects_risky_call_before_transport():
    runner = require_module("harness.run_p1")
    client = _SequenceClient(["unused"])
    budget = runner._AggregateBudget(cap_usd=0.01, spent_usd=0.009)

    with pytest.raises(RuntimeError, match="cost cap|exceed"):
        runner._generate(
            client,
            {
                "request_id": "budget-preflight",
                "messages": [{"role": "user", "content": "public"}],
                "response_format": {"type": "text"},
            },
            seed=20260711,
            budget=budget,
            maximum_call_cost_usd=0.002,
        )

    assert client.calls == []
    assert budget.spent_usd == pytest.approx(0.009)


def test_runner_accounts_for_paid_response_rejected_by_client():
    runner = require_module("harness.run_p1")

    class PaidRejectClient:
        model_id = "test/paid-reject"

        def __init__(self):
            self.calls = 0
            self.last_call_metadata = None

        def generate(self, _request, *, seed):
            assert seed == 20260711
            self.calls += 1
            self.last_call_metadata = {
                "cost_usd": 0.004,
                "response_status": "REJECTED_RESPONSE",
            }
            raise RuntimeError("paid response rejected")

    client = PaidRejectClient()
    budget = runner._AggregateBudget(cap_usd=0.01)

    with pytest.raises(RuntimeError, match="paid response rejected"):
        runner._generate(
            client,
            {
                "request_id": "paid-reject",
                "messages": [{"role": "user", "content": "public"}],
                "response_format": {"type": "text"},
            },
            seed=20260711,
            budget=budget,
            maximum_call_cost_usd=0.005,
        )

    assert client.calls == 1
    assert budget.spent_usd == pytest.approx(0.004)


def test_smoke_preserves_sanitized_failure_cost_artifact(tmp_path):
    runner = require_module("harness.run_p1")

    class PaidRejectAutoplay(_AutoplayClient):
        def generate(self, request, *, seed):
            self.calls.append((deepcopy(request), seed))
            self.last_call_metadata = {
                "response_id": "paid-reject-1",
                "requested_model": self.model_id,
                "returned_model": self.model_id,
                "provider": self.provider,
                "provider_attribution": "REQUEST_PINNED_ALLOW_FALLBACKS_FALSE",
                "finish_reason": "length",
                "usage": {"cost": 0.004},
                "cost_usd": 0.004,
                "attempt_count": 1,
                "response_status": "REJECTED_RESPONSE",
            }
            raise RuntimeError("paid response rejected")

    clients = (
        PaidRejectAutoplay(
            "inclusionai/ling-2.6-flash",
            "inclusionai",
            "Novita",
            "ling-2.6-flash",
        ),
        _AutoplayClient(
            "meta-llama/llama-3.1-8b-instruct",
            "meta",
            "DeepInfra",
            "llama-3.1-8b-instruct",
        ),
        _AutoplayClient(
            "mistralai/mistral-nemo",
            "mistralai",
            "DekaLLM",
            "mistral-nemo",
        ),
    )
    output_dir = tmp_path / "failed-smoke"

    with pytest.raises(RuntimeError, match="paid response rejected"):
        runner.run_cheap_smoke(
            clients=clients,
            seed=20260711,
            output_dir=output_dir,
            cost_cap_usd=0.01,
        )

    failure = json.loads(
        (output_dir / "smoke-failure.json").read_text(encoding="utf-8")
    )
    assert failure["status"] == "CHEAP_MODEL_ENGINEERING_SMOKE_ABORTED"
    assert failure["total_cost_usd"] == pytest.approx(0.004)
    assert failure["failed_schedule_index"] == 0
    serialized = json.dumps(failure, sort_keys=True).lower()
    assert "raw_response" not in serialized
    assert "openrouter_api_key" not in serialized
    assert "principal_mandate" not in serialized


class _HttpResponse:
    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self):
        return json.dumps(self.payload).encode("utf-8")


def _http_error(status, *, headers=None):
    return urllib.error.HTTPError(
        url="https://openrouter.ai/api/v1/chat/completions",
        code=status,
        msg="sanitized test transport error",
        hdrs=headers,
        fp=io.BytesIO(b'{"error":"sanitized test failure"}'),
    )


def _accepted_openrouter_payload():
    return {
        "id": "generation-retry",
        "model": "meta-llama/llama-3.1-8b-instruct",
        "provider": "DeepInfra",
        "choices": [
            {
                "finish_reason": "stop",
                "message": {"content": '{"kind":"act"}'},
            }
        ],
        "usage": {
            "prompt_tokens": 10,
            "completion_tokens": 5,
            "total_tokens": 15,
            "cost": 0.000001,
        },
    }


def _public_adapter_request():
    return {
        "request_id": "retry-request",
        "messages": [{"role": "user", "content": "Public fixture."}],
        "response_format": {"type": "text"},
    }


def test_openrouter_client_retries_429_with_bounded_backoff_and_tracks_attempts():
    adapters = require_module("harness.model_adapters")
    attempts = []
    sleeps = []

    def opener(request, timeout):
        attempts.append((bytes(request.data), timeout))
        if len(attempts) == 1:
            raise _http_error(429, headers={"Retry-After": "90"})
        return _HttpResponse(_accepted_openrouter_payload())

    client = adapters.OpenRouterClient(
        "meta-llama/llama-3.1-8b-instruct",
        family="llama-3.1-8b-instruct",
        vendor="meta",
        provider="DeepInfra",
        api_key="test-secret-not-real",
        max_attempts=3,
        retry_base_seconds=1.0,
        opener=opener,
        sleeper=sleeps.append,
    )

    assert client.generate(_public_adapter_request(), seed=17) == '{"kind":"act"}'
    assert len(attempts) == 2
    assert attempts[0] == attempts[1]
    assert sleeps == [30.0]
    assert client.last_call_metadata["attempt_count"] == 2
    assert "test-secret-not-real" not in json.dumps(client.last_call_metadata)


@pytest.mark.parametrize("status", [400, 401, 403, 422, 500, 503])
def test_openrouter_client_never_retries_http_status_other_than_429(status):
    adapters = require_module("harness.model_adapters")
    attempts = []
    sleeps = []

    def opener(_request, timeout):
        assert timeout == 60.0
        attempts.append(status)
        raise _http_error(status)

    client = adapters.OpenRouterClient(
        "meta-llama/llama-3.1-8b-instruct",
        family="llama-3.1-8b-instruct",
        vendor="meta",
        provider="DeepInfra",
        api_key="test-secret-not-real",
        max_attempts=3,
        opener=opener,
        sleeper=sleeps.append,
    )

    with pytest.raises(adapters.OpenRouterTransportError, match=str(status)) as caught:
        client.generate(_public_adapter_request(), seed=17)

    assert attempts == [status]
    assert sleeps == []
    assert client.last_call_metadata is None
    assert "test-secret-not-real" not in str(caught.value)
    assert caught.value.status_code == status
    assert caught.value.attempt_count == 1


def test_openrouter_client_exhausts_exact_retry_budget_fail_closed():
    adapters = require_module("harness.model_adapters")
    attempts = []
    sleeps = []

    def opener(_request, timeout):
        assert timeout == 60.0
        attempts.append(429)
        raise _http_error(429)

    client = adapters.OpenRouterClient(
        "meta-llama/llama-3.1-8b-instruct",
        family="llama-3.1-8b-instruct",
        vendor="meta",
        provider="DeepInfra",
        api_key="test-secret-not-real",
        max_attempts=3,
        retry_base_seconds=1.0,
        opener=opener,
        sleeper=sleeps.append,
    )

    with pytest.raises(
        adapters.OpenRouterTransportError, match="after 3 attempts"
    ) as caught:
        client.generate(_public_adapter_request(), seed=17)

    assert attempts == [429, 429, 429]
    assert sleeps == [1.0, 2.0]
    assert client.last_call_metadata is None
    assert caught.value.status_code == 429
    assert caught.value.attempt_count == 3


@pytest.mark.parametrize(
    "failure",
    [urllib.error.URLError("test"), TimeoutError("test"), OSError("test")],
)
def test_openrouter_client_never_retries_ambiguous_network_failures(failure):
    adapters = require_module("harness.model_adapters")
    attempts = []
    sleeps = []

    def opener(_request, timeout):
        assert timeout == 60.0
        attempts.append(1)
        raise failure

    client = adapters.OpenRouterClient(
        "meta-llama/llama-3.1-8b-instruct",
        family="llama-3.1-8b-instruct",
        vendor="meta",
        provider="DeepInfra",
        api_key="test-secret-not-real",
        max_attempts=3,
        retry_base_seconds=1.0,
        opener=opener,
        sleeper=sleeps.append,
    )

    with pytest.raises(adapters.OpenRouterTransportError) as caught:
        client.generate(_public_adapter_request(), seed=17)

    assert attempts == [1]
    assert sleeps == []
    assert caught.value.status_code is None
    assert caught.value.attempt_count == 1


def test_generic_openrouter_client_sends_exact_bounded_body_and_safe_metadata():
    adapters = require_module("harness.model_adapters")
    seen = []

    def opener(request, timeout):
        seen.append((request, timeout))
        return _HttpResponse(
            {
                "id": "generation-1",
                "model": "meta-llama/llama-3.1-8b-instruct",
                "provider": "DeepInfra",
                "choices": [
                    {
                        "finish_reason": "stop",
                        "message": {"content": '{"kind":"act"}'},
                    }
                ],
                "usage": {
                    "prompt_tokens": 10,
                    "completion_tokens": 5,
                    "total_tokens": 15,
                    "cost": 0.000001,
                },
            }
        )

    client = adapters.OpenRouterClient(
        "meta-llama/llama-3.1-8b-instruct",
        family="llama-3.1-8b",
        vendor="meta",
        provider="DeepInfra",
        api_key="test-secret-not-real",
        max_tokens=256,
        cost_cap_usd=0.01,
        opener=opener,
        sleeper=lambda _delay: None,
    )
    request = {
        "request_id": "test-request",
        "messages": [
            {"role": "developer", "content": "Return one object."},
            {"role": "user", "content": "Public fixture."},
        ],
        "response_format": {"type": "text"},
    }

    text = client.generate(request, seed=17)

    assert text == '{"kind":"act"}'
    body = json.loads(seen[0][0].data.decode("utf-8"))
    assert body == {
        "model": "meta-llama/llama-3.1-8b-instruct",
        "messages": request["messages"],
        "seed": 17,
        "max_tokens": 256,
        "temperature": 0,
        "response_format": {"type": "json_object"},
        "provider": {
            "order": ["DeepInfra"],
            "allow_fallbacks": False,
            "require_parameters": True,
        },
        "usage": {"include": True},
    }
    metadata = client.last_call_metadata
    assert metadata["provider"] == "DeepInfra"
    assert metadata["cost_usd"] == pytest.approx(0.000001)
    assert "test-secret-not-real" not in json.dumps(metadata)


def test_openrouter_client_accepts_documented_response_without_provider_echo():
    adapters = require_module("harness.model_adapters")

    def opener(_request, timeout):
        assert timeout == 60.0
        return _HttpResponse(
            {
                "id": "documented-generation",
                "choices": [
                    {
                        "finish_reason": "stop",
                        "native_finish_reason": "stop",
                        "message": {
                            "role": "assistant",
                            "content": '{"kind":"act"}',
                        },
                    }
                ],
                "created": 1783780000,
                "model": "meta-llama/llama-3.1-8b-instruct",
                "object": "chat.completion",
                "usage": {
                    "prompt_tokens": 10,
                    "completion_tokens": 5,
                    "total_tokens": 15,
                    "cost": 0.000001,
                },
            }
        )

    client = adapters.OpenRouterClient(
        "meta-llama/llama-3.1-8b-instruct",
        family="llama-3.1-8b-instruct",
        vendor="meta",
        provider="DeepInfra",
        api_key="test-secret-not-real",
        max_tokens=256,
        cost_cap_usd=0.01,
        opener=opener,
        sleeper=lambda _delay: None,
    )

    response = client.generate(
        {
            "request_id": "documented-response-shape",
            "messages": [{"role": "user", "content": "Public fixture."}],
            "response_format": {"type": "text"},
        },
        seed=17,
    )

    assert response == '{"kind":"act"}'
    assert client.last_call_metadata["provider"] == "DeepInfra"
    assert (
        client.last_call_metadata["provider_attribution"]
        == "REQUEST_PINNED_ALLOW_FALLBACKS_FALSE"
    )


@pytest.mark.parametrize(
    "finish_reason,cost_usd,cost_cap_usd",
    (("length", 0.001, 0.01), ("stop", 0.02, 0.01)),
)
def test_openrouter_client_accounts_for_rejected_paid_responses(
    finish_reason, cost_usd, cost_cap_usd
):
    adapters = require_module("harness.model_adapters")

    def opener(_request, timeout):
        assert timeout == 60.0
        return _HttpResponse(
            {
                "id": "rejected-generation",
                "model": "meta-llama/llama-3.1-8b-instruct",
                "provider": "DeepInfra",
                "choices": [
                    {
                        "finish_reason": finish_reason,
                        "message": {"content": '{"kind":"act"}'},
                    }
                ],
                "usage": {
                    "prompt_tokens": 10,
                    "completion_tokens": 5,
                    "total_tokens": 15,
                    "cost": cost_usd,
                },
            }
        )

    client = adapters.OpenRouterClient(
        "meta-llama/llama-3.1-8b-instruct",
        family="llama-3.1-8b-instruct",
        vendor="meta",
        provider="DeepInfra",
        api_key="test-secret-not-real",
        max_tokens=256,
        cost_cap_usd=cost_cap_usd,
        opener=opener,
        sleeper=lambda _delay: None,
    )

    with pytest.raises(adapters.OpenRouterResponseError):
        client.generate(
            {
                "request_id": "rejected-paid-response",
                "messages": [{"role": "user", "content": "Public fixture."}],
                "response_format": {"type": "text"},
            },
            seed=17,
        )

    assert client.spent_cost_usd == pytest.approx(cost_usd)
    assert client.last_call_metadata["cost_usd"] == pytest.approx(cost_usd)
    assert client.last_call_metadata["response_status"].startswith("REJECTED")
    assert "test-secret-not-real" not in json.dumps(client.last_call_metadata)


def test_paid_smoke_entrypoint_requires_explicit_opt_in(tmp_path):
    entrypoint = require_module("harness.run_openrouter_smoke")
    factory_calls = []

    def client_factory(*args, **kwargs):
        factory_calls.append((args, kwargs))
        raise AssertionError("client must not be constructed without paid opt-in")

    with pytest.raises(SystemExit):
        entrypoint.main(
            ["--output-dir", str(tmp_path / "must-not-start")],
            environ={"OPENROUTER_API_KEY": "test-secret-not-real"},
            client_factory=client_factory,
        )

    assert factory_calls == []
    assert not (tmp_path / "must-not-start").exists()


def test_paid_smoke_entrypoint_runs_exact_frozen_roster_without_key_leak(
    tmp_path, capsys
):
    entrypoint = require_module("harness.run_openrouter_smoke")
    factory_calls = []
    runner_calls = []

    def client_factory(model_id, **kwargs):
        factory_calls.append((model_id, deepcopy(kwargs)))
        return type(
            "ConfiguredClient",
            (),
            {
                "model_id": model_id,
                "family": kwargs["family"],
                "vendor": kwargs["vendor"],
                "provider": kwargs["provider"],
                "max_tokens": kwargs["max_tokens"],
                "cost_cap_usd": kwargs["cost_cap_usd"],
            },
        )()

    def smoke_runner(**kwargs):
        runner_calls.append(kwargs)
        return {
            "status": "CHEAP_MODEL_ENGINEERING_SMOKE_COMPLETE",
            "scheduled_requests": 9,
            "paid_calls": 9,
            "total_cost_usd": 0.0001,
            "preflight_cost_upper_bound_usd": 0.0015,
        }

    output_dir = tmp_path / "paid-smoke"
    exit_code = entrypoint.main(
        ["--execute-paid-live", "--output-dir", str(output_dir)],
        environ={"OPENROUTER_API_KEY": "test-secret-not-real"},
        client_factory=client_factory,
        smoke_runner=smoke_runner,
    )

    assert exit_code == 0
    assert [row[0] for row in factory_calls] == [
        "inclusionai/ling-2.6-flash",
        "meta-llama/llama-3.1-8b-instruct",
        "mistralai/mistral-nemo",
    ]
    assert [row[1]["provider"] for row in factory_calls] == [
        "Novita",
        "DeepInfra",
        "DekaLLM",
    ]
    assert all(
        row[1]["api_key"] == "test-secret-not-real" for row in factory_calls
    )
    assert len(runner_calls) == 1
    assert runner_calls[0]["seed"] == 20260711
    assert runner_calls[0]["cost_cap_usd"] == 0.01
    assert runner_calls[0]["output_dir"] == output_dir
    printed = capsys.readouterr().out
    assert "CHEAP_MODEL_ENGINEERING_SMOKE_COMPLETE" in printed
    assert "test-secret-not-real" not in printed
