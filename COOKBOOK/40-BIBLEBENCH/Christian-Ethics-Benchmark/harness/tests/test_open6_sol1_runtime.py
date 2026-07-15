"""Offline runtime seams for OPEN6-SOL1.  No HTTP or Codex call is live."""

from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor
from decimal import Decimal
from pathlib import Path
from types import SimpleNamespace

import pytest

from walkworthy.clients import Message


def _runtime():
    from walkworthy import open6_sol1_runtime

    return open6_sol1_runtime


def _ok(model, *, content="answer", cost=0.001):
    usage = {
        "cost": cost,
        "prompt_tokens": 10,
        "completion_tokens": 2,
    }
    return 200, {
        "model": model,
        "choices": [{"message": {"content": content}}],
        "usage": usage,
    }


def _transport(*responses):
    calls = []
    remaining = list(responses)

    def transport(url, headers, payload, timeout=None):
        calls.append({
            "url": url,
            "headers": headers,
            "payload": json.loads(json.dumps(payload)),
        })
        return remaining.pop(0)

    transport.calls = calls
    return transport


def test_exact_openrouter_specs_use_frozen_roster_and_pilot_limits():
    runtime = _runtime()
    specs = runtime.SUT_SPECS

    assert [spec.slug for spec in specs] == [
        "minimax/minimax-m3",
        "z-ai/glm-5.2",
        "deepseek/deepseek-v4-pro",
        "qwen/qwen3.5-397b-a17b",
        "google/gemma-4-31b-it",
        "meta-llama/llama-4-maverick",
    ]
    assert all(spec.max_tokens == 2048 for spec in specs)
    assert all(spec.input_envelope == 24_000 for spec in specs)
    assert all(spec.role == "sut" for spec in specs)
    for spec in specs:
        assert spec.provider_prefs == {
            "sort": "price",
            "require_parameters": True,
            "allow_fallbacks": True,
            "max_price": {
                "prompt": float(spec.ceiling_input_per_m),
                "completion": float(spec.ceiling_output_per_m),
            },
        }
        assert spec.max_call_usd == (
            Decimal(24_000) * spec.ceiling_input_per_m
            + Decimal(2048) * spec.ceiling_output_per_m
        ) / Decimal(1_000_000)


def test_openrouter_client_has_no_internal_retry_or_sampling_controls(tmp_path):
    runtime = _runtime()
    spec = runtime.SUT_SPECS[0]
    client = runtime.OpenRouterPilotClient(
        spec, "secret", runtime.OpenRouterAttemptLedger(tmp_path / "attempts.jsonl"),
        _transport(_ok(spec.slug)),
    )

    result = client.complete("item/model", [Message("user", "prompt")])

    base = client.base_client
    assert base.max_retries == 0
    assert base.empty_retries == 0
    assert base.max_tokens == 2048
    payload = result.payload
    assert payload["provider"] == spec.provider_prefs
    assert not ({"temperature", "top_p", "top_k", "reasoning"} & payload.keys())


def test_openrouter_valid_response_is_not_replayed_and_body_is_returned(tmp_path):
    runtime = _runtime()
    spec = runtime.SUT_SPECS[0]
    transport = _transport(_ok(spec.slug, content="full response"))
    custody = []
    ledger = runtime.OpenRouterAttemptLedger(tmp_path / "attempts.jsonl")
    client = runtime.OpenRouterPilotClient(
        spec, "sk-secret", ledger, transport, response_sink=custody.append,
    )

    result = client.complete("key", [Message("user", "private body")])

    assert result.response.text == "full response"
    assert result.body["usage"]["cost"] == 0.001
    assert len(transport.calls) == 1
    assert custody[0]["body"] == result.body
    persisted = ledger.path.read_text()
    assert "private body" not in persisted
    assert "full response" not in persisted
    assert "sk-secret" not in persisted
    assert "messages" not in persisted


def test_openrouter_defect_replays_the_exact_payload_once(tmp_path):
    runtime = _runtime()
    spec = runtime.SUT_SPECS[0]
    transport = _transport(
        (503, {"error": "temporary"}),
        _ok(spec.slug, content="recovered"),
    )
    ledger = runtime.OpenRouterAttemptLedger(tmp_path / "attempts.jsonl")
    client = runtime.OpenRouterPilotClient(spec, "k", ledger, transport)

    result = client.complete("key", [Message("user", "same")])

    assert result.response.text == "recovered"
    assert len(transport.calls) == 2
    assert transport.calls[0]["payload"] == transport.calls[1]["payload"]
    assert ledger.snapshot()["replays"] == 1


@pytest.mark.parametrize("bad_body", [
    {"model": "minimax/minimax-m3", "choices": [{"message": {"content": "ok"}}],
     "usage": {}},
    {"model": "wrong/model", "choices": [{"message": {"content": "ok"}}],
     "usage": {"cost": 0.001}},
])
def test_openrouter_second_custody_failure_stops_and_books_missing_cost(
        tmp_path, bad_body):
    runtime = _runtime()
    spec = runtime.SUT_SPECS[0]
    transport = _transport((200, bad_body), (200, bad_body))
    ledger = runtime.OpenRouterAttemptLedger(tmp_path / "attempts.jsonl")
    client = runtime.OpenRouterPilotClient(spec, "k", ledger, transport)

    with pytest.raises(runtime.ThreadStop):
        client.complete("key", [Message("user", "same")])

    snapshot = ledger.snapshot()
    assert snapshot["attempts"] == 2
    if bad_body["usage"] == {}:
        assert snapshot["reserved_usd"] == spec.max_call_usd * 2


def test_openrouter_caps_nte_retry_reserve_and_concurrency(tmp_path):
    runtime = _runtime()
    spec = runtime.SUT_SPECS[0]
    payload = runtime.make_openrouter_client(spec, "k", lambda *_a, **_k: None).build_payload(
        [Message("user", "x")], None)
    ledger = runtime.OpenRouterAttemptLedger(
        tmp_path / "attempts.jsonl",
        hard_nte_usd=spec.max_call_usd * 2,
        max_attempts=3,
        replay_cap=0,
        max_concurrency=2,
    )
    first = ledger.begin("one", spec, payload)
    second = ledger.begin("two", spec, payload)
    with pytest.raises(runtime.BudgetStop):
        ledger.begin("three", spec, payload)
    ledger.finish(first, 503, {"error": "x"})
    with pytest.raises(runtime.BudgetStop):
        ledger.begin("one", spec, payload)
    ledger.finish(second, *_ok(spec.slug))
    with pytest.raises(runtime.BudgetStop):
        ledger.begin("three", spec, payload)


def test_openrouter_preserves_nominal_calls_for_first_attempts(tmp_path):
    runtime = _runtime()
    spec = runtime.SUT_SPECS[0]
    payload = runtime.make_openrouter_client(spec, "k", lambda *_a, **_k: None).build_payload(
        [Message("user", "x")], None)
    ledger = runtime.OpenRouterAttemptLedger(
        tmp_path / "attempts.jsonl", planned_cap=1, max_attempts=2,
    )
    attempt = ledger.begin("one", spec, payload)
    ledger.finish(attempt, *_ok(spec.slug))
    with pytest.raises(runtime.BudgetStop, match="planned"):
        ledger.begin("two", spec, payload)


def test_openrouter_reserves_dynamic_byte_upper_bound_without_false_24k_rejection(
        tmp_path):
    runtime = _runtime()
    spec = runtime.SUT_SPECS[0]
    payload = runtime.make_openrouter_client(spec, "k", lambda *_a, **_k: None).build_payload(
        [Message("user", "é" * 13_000)], None)
    payload_bytes = len(json.dumps(payload).encode("utf-8"))
    assert payload_bytes > 24_000
    ledger = runtime.OpenRouterAttemptLedger(tmp_path / "attempts.jsonl")

    attempt = ledger.begin("unicode", spec, payload)

    start = ledger.attempt_snapshot(attempt)["start"]
    assert start["reserved_input_tokens"] == payload_bytes
    assert Decimal(start["ceiling_max_usd"]) == spec.max_call_usd_for_input(payload_bytes)
    ledger.finish(attempt, *_ok(spec.slug))


def test_openrouter_ledger_assigns_contiguous_ids_under_concurrency(tmp_path):
    runtime = _runtime()
    spec = runtime.SUT_SPECS[0]
    payload = runtime.make_openrouter_client(spec, "k", lambda *_a, **_k: None).build_payload(
        [Message("user", "x")], None)
    ledger = runtime.OpenRouterAttemptLedger(tmp_path / "attempts.jsonl")

    with ThreadPoolExecutor(max_workers=2) as pool:
        ids = list(pool.map(
            lambda key: ledger.begin(key, spec, payload), ("one", "two")
        ))

    assert sorted(ids) == [1, 2]
    for attempt in ids:
        ledger.finish(attempt, *_ok(spec.slug))


def test_openrouter_resume_rejects_unresolved_or_tampered_ledger(tmp_path):
    runtime = _runtime()
    spec = runtime.SUT_SPECS[0]
    path = tmp_path / "attempts.jsonl"
    ledger = runtime.OpenRouterAttemptLedger(path)
    payload = runtime.make_openrouter_client(spec, "k", lambda *_a, **_k: None).build_payload(
        [Message("user", "x")], None)
    attempt = ledger.begin("one", spec, payload)
    with pytest.raises(runtime.ContractStop, match="in-flight"):
        runtime.OpenRouterAttemptLedger(path)
    ledger.finish(attempt, *_ok(spec.slug))
    lines = path.read_text().splitlines()
    event = json.loads(lines[-1])
    event["booked_usd"] = "0"
    lines[-1] = json.dumps(event, sort_keys=True, separators=(",", ":"))
    path.write_text("\n".join(lines) + "\n")
    with pytest.raises(runtime.ContractStop, match="hash"):
        runtime.OpenRouterAttemptLedger(path)


def test_openrouter_transport_exception_is_closed_then_exactly_replayed(tmp_path):
    runtime = _runtime()
    spec = runtime.SUT_SPECS[0]
    calls = []

    def flaky(url, headers, payload, timeout=None):
        calls.append(json.loads(json.dumps(payload)))
        if len(calls) == 1:
            raise OSError("dns secret detail")
        return _ok(spec.slug, content="recovered")

    ledger = runtime.OpenRouterAttemptLedger(tmp_path / "attempts.jsonl")
    result = runtime.OpenRouterPilotClient(spec, "k", ledger, flaky).complete(
        "key", [Message("user", "same")]
    )

    assert result.response.text == "recovered"
    assert calls[0] == calls[1]
    assert ledger.snapshot()["inflight_usd"] == Decimal("0")
    persisted = ledger.path.read_text()
    assert "dns secret detail" not in persisted
    assert ledger.attempt_snapshot(1)["finish"]["failure"] == "http_failure"


def test_openrouter_second_transport_exception_stops_without_stranded_start(tmp_path):
    runtime = _runtime()
    spec = runtime.SUT_SPECS[0]

    def down(*_args, **_kwargs):
        raise TimeoutError("down")

    ledger = runtime.OpenRouterAttemptLedger(tmp_path / "attempts.jsonl")
    with pytest.raises(runtime.ThreadStop):
        runtime.OpenRouterPilotClient(spec, "k", ledger, down).complete(
            "key", [Message("user", "same")]
        )
    assert ledger.snapshot()["attempts"] == 2
    assert ledger.snapshot()["inflight_usd"] == Decimal("0")


def test_openrouter_explicit_crash_recovery_closes_inflight_and_consumes_replay(
        tmp_path):
    runtime = _runtime()
    path = tmp_path / "attempts.jsonl"
    spec = runtime.SUT_SPECS[0]
    payload = runtime.make_openrouter_client(spec, "k", lambda *_a, **_k: None).build_payload(
        [Message("user", "same")], None)
    ledger = runtime.OpenRouterAttemptLedger(path)
    ledger.begin("crashed", spec, payload)
    with pytest.raises(runtime.ContractStop, match="in-flight"):
        runtime.OpenRouterAttemptLedger(path)

    recovered = runtime.OpenRouterAttemptLedger.recover_inflight(path)
    replay = recovered.begin("crashed", spec, payload)
    other = recovered.begin("other", spec, payload)

    assert replay == 2
    assert other == 3
    assert recovered.snapshot()["replays"] == 1
    recovered.finish(replay, *_ok(spec.slug))
    recovered.finish(other, *_ok(spec.slug))


class RecordedCodexRunner:
    def __init__(self, finals, traces=None, returncodes=None):
        self.finals = list(finals)
        self.traces = list(traces or [
            '{"type":"turn.completed","usage":{"input_tokens":10,"output_tokens":2}}\n'
        ] * len(finals))
        self.returncodes = list(returncodes or [0] * len(finals))
        self.calls = []

    def __call__(self, argv, **kwargs):
        self.calls.append({"argv": list(argv), **kwargs})
        final_path = Path(argv[argv.index("--output-last-message") + 1])
        final_path.write_text(self.finals.pop(0), encoding="utf-8")
        return SimpleNamespace(
            returncode=self.returncodes.pop(0),
            stdout=self.traces.pop(0),
            stderr="",
        )


def test_sol_exec_exact_cli_is_ephemeral_isolated_and_schema_bound(
        tmp_path, monkeypatch):
    runtime = _runtime()
    monkeypatch.setenv("OPENAI_API_KEY", "must-not-leak")
    monkeypatch.setenv("OPENROUTER_API_KEY", "must-not-leak")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "must-not-leak")
    runner = RecordedCodexRunner(['{"state":"continue"}'])
    ledger = runtime.SolTaskLedger(tmp_path / "sol.jsonl")
    client = runtime.SolExecClient(
        ledger, runner=runner, cli_version="codex-cli 0.144.3"
    )

    result = client.classify_state(
        "route/1", "02-twomasters", "opaque-1",
        ("continue", "terminal"), "assistant text",
    )

    call = runner.calls[0]
    argv = call["argv"]
    assert argv[:4] == ["codex", "exec", "-m", "gpt-5.6-sol"]
    assert ['-c', 'model_reasoning_effort="medium"'] == argv[4:6]
    for flag in (
        "--ignore-user-config", "--ignore-rules", "--ephemeral",
        "--skip-git-repo-check", "--json", "--output-schema",
        "--output-last-message",
    ):
        assert flag in argv
    assert argv[argv.index("--sandbox") + 1] == "read-only"
    assert argv[-1] == "-"
    disabled = [argv[index + 1] for index, value in enumerate(argv)
                if value == "--disable"]
    assert disabled == list(runtime.DISABLED_CODEX_FEATURES)
    configs = [argv[index + 1] for index, value in enumerate(argv) if value == "-c"]
    for config in runtime.DISABLED_CONTEXT_CONFIGS:
        assert config in configs
    assert call["input"] == result.prompt
    assert Path(call["cwd"]).name.startswith("walkworthy-open6-sol1-")
    assert result.value == {"state": "continue"}
    assert result.cli_version == "codex-cli 0.144.3"
    assert result.final_text == '{"state":"continue"}'
    assert result.trace_jsonl.startswith("{")
    assert set(call["env"]).issubset(runtime.CODEX_ENV_WHITELIST)
    assert not ({"OPENAI_API_KEY", "OPENROUTER_API_KEY", "ANTHROPIC_API_KEY"}
                & set(call["env"]))


def test_sol_classifier_is_strict_and_has_no_heuristic_fallback(tmp_path):
    runtime = _runtime()
    runner = RecordedCodexRunner([
        '{"state":"not-allowed"}', '{"state":"not-allowed"}',
    ])
    client = runtime.SolExecClient(
        runtime.SolTaskLedger(tmp_path / "sol.jsonl"),
        runner=runner,
        cli_version="codex-cli test",
    )

    with pytest.raises(runtime.ThreadStop):
        client.classify_state(
            "route/1", "07-seventyseven", "opaque",
            ("continue", "terminal"), "contains the word terminal",
        )
    assert len(runner.calls) == 2
    assert runner.calls[0]["input"] == runner.calls[1]["input"]


def test_sol_rejects_tool_trace_and_replays_exact_task(tmp_path):
    runtime = _runtime()
    runner = RecordedCodexRunner(
        ['{"state":"continue"}', '{"state":"continue"}'],
        traces=[
            '{"type":"item.started","item":{"type":"command_execution"}}\n',
            '{"type":"turn.completed"}\n',
        ],
    )
    ledger = runtime.SolTaskLedger(tmp_path / "sol.jsonl")
    client = runtime.SolExecClient(
        ledger, runner=runner, cli_version="codex-cli test"
    )

    result = client.classify_state(
        "route/1", "02-twomasters", "opaque",
        ("continue", "terminal"), "text",
    )

    assert result.value["state"] == "continue"
    assert len(runner.calls) == 2
    assert runner.calls[0]["input"] == runner.calls[1]["input"]
    assert ledger.snapshot()["replays"] == 1


def test_sol_rejects_any_typed_tool_event(tmp_path):
    runtime = _runtime()
    runner = RecordedCodexRunner(
        ['{"state":"continue"}', '{"state":"continue"}'],
        traces=[
            '{"type":"item.started","item":{"type":"dynamic_tool_call"}}\n',
            '{"type":"turn.completed"}\n',
        ],
    )
    client = runtime.SolExecClient(
        runtime.SolTaskLedger(tmp_path / "sol.jsonl"),
        runner=runner, cli_version="codex-cli test",
    )
    result = client.classify_state(
        "route/1", "02-twomasters", "opaque",
        ("continue", "terminal"), "text",
    )
    assert result.attempt_ids == (1, 2)


def test_sol_ledger_rejects_non_usage_body_fields(tmp_path):
    runtime = _runtime()
    ledger = runtime.SolTaskLedger(tmp_path / "sol.jsonl")
    attempt = ledger.begin("one", "a" * 64, "b" * 64)
    with pytest.raises(runtime.ContractStop, match="usage"):
        ledger.finish(attempt, valid=False, error_class="malformed",
                      usage={"secret": "body"})


def test_sol_valid_result_has_no_replay_and_ledger_is_body_free(tmp_path):
    runtime = _runtime()
    runner = RecordedCodexRunner(['{"state":"terminal"}'])
    ledger = runtime.SolTaskLedger(tmp_path / "sol.jsonl")
    client = runtime.SolExecClient(
        ledger, runner=runner, cli_version="codex-cli test"
    )

    result = client.classify_state(
        "route/1", "02-twomasters", "opaque",
        ("continue", "terminal"), "secret response body",
    )

    assert result.value == {"state": "terminal"}
    assert len(runner.calls) == 1
    persisted = ledger.path.read_text()
    assert "secret response body" not in persisted
    assert '"state":"terminal"' not in persisted


def test_sol_ledger_caps_concurrency_replays_and_rejects_tamper(tmp_path):
    runtime = _runtime()
    path = tmp_path / "sol.jsonl"
    ledger = runtime.SolTaskLedger(
        path, max_attempts=3, replay_cap=0, max_concurrency=2
    )
    schema_hash = "a" * 64
    payload_hash = "b" * 64
    one = ledger.begin("one", payload_hash, schema_hash)
    two = ledger.begin("two", payload_hash, schema_hash)
    with pytest.raises(runtime.BudgetStop):
        ledger.begin("three", payload_hash, schema_hash)
    ledger.finish(one, valid=False, error_class="malformed")
    with pytest.raises(runtime.BudgetStop):
        ledger.begin("one", payload_hash, schema_hash)
    ledger.finish(two, valid=True, trace_sha256="c" * 64,
                  response_sha256="d" * 64, cli_version="codex-cli test")
    lines = path.read_text().splitlines()
    changed = json.loads(lines[-1])
    changed["cli_version"] = "tampered"
    lines[-1] = json.dumps(changed, sort_keys=True, separators=(",", ":"))
    path.write_text("\n".join(lines) + "\n")
    with pytest.raises(runtime.ContractStop, match="hash"):
        runtime.SolTaskLedger(path)


def test_sol_explicit_crash_recovery_closes_inflight_and_consumes_replay(tmp_path):
    runtime = _runtime()
    path = tmp_path / "sol.jsonl"
    ledger = runtime.SolTaskLedger(path)
    ledger.begin("crashed", "a" * 64, "b" * 64)
    with pytest.raises(runtime.ContractStop, match="in-flight"):
        runtime.SolTaskLedger(path)

    recovered = runtime.SolTaskLedger.recover_inflight(path)
    replay = recovered.begin("crashed", "a" * 64, "b" * 64)
    other = recovered.begin("other", "c" * 64, "d" * 64)

    assert replay == 2
    assert other == 3
    assert recovered.snapshot()["replays"] == 1
    recovered.finish(replay, valid=True, trace_sha256="e" * 64,
                     response_sha256="f" * 64, cli_version="codex-cli test")
    recovered.finish(other, valid=True, trace_sha256="e" * 64,
                     response_sha256="f" * 64, cli_version="codex-cli test")
