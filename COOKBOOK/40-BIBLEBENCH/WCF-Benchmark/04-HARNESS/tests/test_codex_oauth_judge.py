from __future__ import annotations

import json
import os
import sys

import pytest


HARNESS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS_ROOT not in sys.path:
    sys.path.insert(0, HARNESS_ROOT)

import wcfbench.codex_oauth_judge as judge_module  # noqa: E402
from wcfbench.codex_oauth_judge import CodexOAuthJudge, JudgeAdapterError  # noqa: E402


class _Proc:
    def __init__(self, stdout, returncode=0, stderr=""):
        self.stdout = stdout
        self.returncode = returncode
        self.stderr = stderr


def _events(*, item_type="agent_message"):
    return "\n".join(json.dumps(row) for row in [
        {"type": "thread.started", "thread_id": "ephemeral"},
        {"type": "turn.started"},
        {"type": "item.completed", "item": {"id": "i1", "type": item_type}},
        {"type": "turn.completed", "usage": {}},
    ])


def _write_result(command, payload):
    output = command[command.index("-o") + 1]
    with open(output, "w", encoding="utf-8") as handle:
        json.dump(payload, handle)


def _verdict(criterion_id, *, route="open", satisfied=True):
    if route == "contested":
        return {
            "criterion_id": criterion_id,
            "verdict": "satisfied" if satisfied else "not_satisfied",
            "reason": "bounded reason",
        }
    return {
        "criterion_id": criterion_id,
        "satisfied": satisfied,
        "reason": "bounded reason",
    }


def _records(route="open"):
    return [
        {"record_id": "r1", "sut": "minimax/minimax-m3", "route": route,
         "payload": {"criterion_id": "c1", "response": "one"}},
        {"record_id": "r2", "sut": "minimax/minimax-m3", "route": route,
         "payload": {"criterion_id": "c2", "response": "two"}},
    ]


def test_command_is_ephemeral_oauth_isolated_read_only_and_tool_observable(monkeypatch):
    captured = {}

    def runner(command, **kwargs):
        captured["command"] = command
        captured["kwargs"] = kwargs
        assert os.listdir(kwargs["cwd"]) == []
        _write_result(command, {"records": [
            {"record_id": "r1", "verdict": _verdict("c1")},
            {"record_id": "r2", "verdict": _verdict("c2", satisfied=False)},
        ]})
        return _Proc(_events())

    monkeypatch.setenv("OPENAI_API_KEY", "must-not-be-used")
    monkeypatch.setenv("CODEX_API_KEY", "must-not-be-used")
    monkeypatch.setenv("OPENROUTER_API_KEY", "must-not-be-used")
    monkeypatch.setenv("GITHUB_TOKEN", "must-not-be-used")
    monkeypatch.setenv("DATABASE_SECRET", "must-not-be-used")
    monkeypatch.setenv("SERVICE_PASSWORD", "must-not-be-used")
    monkeypatch.setenv("UNRELATED_CONFIG", "must-not-be-used")
    monkeypatch.setenv("PATH", "/safe/bin")
    monkeypatch.setenv("HOME", "/safe/home")
    monkeypatch.setenv("TMPDIR", "/safe/tmp")
    monkeypatch.setenv("LANG", "C.UTF-8")
    monkeypatch.setenv("SSL_CERT_FILE", "/safe/cert.pem")
    monkeypatch.setenv("CODEX_HOME", "/safe/codex-home")
    persisted = []
    result = CodexOAuthJudge(runner=runner, persist=persisted.append).judge(_records())
    assert result == {"records": persisted, "missing_record_ids": [], "attempts": 1}
    command = captured["command"]
    assert command[:2] == ["codex", "exec"]
    for flag in (
        "--ephemeral", "--ignore-user-config", "--ignore-rules", "--sandbox",
        "read-only", "--skip-git-repo-check", "--output-schema", "--json", "-o", "-C",
    ):
        assert flag in command
    assert command[command.index("--model") + 1] == "gpt-5.6-sol"
    assert 'model_reasoning_effort="medium"' in command
    assert 'web_search="disabled"' in command
    assert "features.multi_agent=false" in command
    assert command[command.index("-C") + 1] == captured["kwargs"]["cwd"]
    assert os.path.dirname(command[command.index("--output-schema") + 1]) != captured["kwargs"]["cwd"]
    assert os.path.dirname(command[command.index("-o") + 1]) != captured["kwargs"]["cwd"]
    assert "OPENAI_API_KEY" not in captured["kwargs"]["env"]
    assert "CODEX_API_KEY" not in captured["kwargs"]["env"]
    assert captured["kwargs"]["env"] == {
        "PATH": "/safe/bin",
        "HOME": "/safe/home",
        "TMPDIR": "/safe/tmp",
        "LANG": "C.UTF-8",
        "SSL_CERT_FILE": "/safe/cert.pem",
        "CODEX_HOME": "/safe/codex-home",
    }


def test_any_tool_event_rejects_the_judge_attempt():
    persisted = []

    def runner(command, **_kwargs):
        _write_result(command, {"records": [
            {"record_id": "r1", "verdict": _verdict("c1")},
            {"record_id": "r2", "verdict": _verdict("c2", satisfied=False)},
        ]})
        return _Proc(_events(item_type="command_execution"))

    with pytest.raises(JudgeAdapterError, match="tool event"):
        CodexOAuthJudge(runner=runner, persist=persisted.append).judge(_records())
    assert persisted == []


def test_valid_records_persist_immediately_and_only_missing_records_retry():
    prompts = []
    persisted = []

    def runner(command, **_kwargs):
        prompt = command[-1]
        prompts.append(prompt)
        if len(prompts) == 1:
            payload = {"records": [
                {"record_id": "r1", "verdict": _verdict("c1")},
                {"record_id": "r2"},
            ]}
        else:
            payload = {"records": [
                {"record_id": "r2", "verdict": _verdict("c2", satisfied=False)},
            ]}
        _write_result(command, payload)
        return _Proc(_events())

    result = CodexOAuthJudge(runner=runner, persist=persisted.append).judge(_records())
    assert [row["record_id"] for row in persisted] == ["r1", "r2"]
    assert result["attempts"] == 2
    assert '"record_id": "r1"' in prompts[0]
    assert '"record_id": "r1"' not in prompts[1]
    assert '"record_id": "r2"' in prompts[1]


def test_missing_record_gets_only_two_retries_then_remains_missing():
    attempts = []

    def runner(command, **_kwargs):
        attempts.append(command[-1])
        _write_result(command, {"records": [{"record_id": "r1"}]})
        return _Proc(_events())

    result = CodexOAuthJudge(runner=runner, persist=lambda _row: None).judge([_records()[0]])
    assert len(attempts) == 3
    assert result == {"records": [], "missing_record_ids": ["r1"], "attempts": 3}


def test_input_ids_must_be_unique_and_batch_must_not_mix_route_or_sut():
    adapter = CodexOAuthJudge(runner=lambda *_a, **_k: None, persist=lambda _row: None)
    duplicate = [_records()[0], dict(_records()[0])]
    with pytest.raises(JudgeAdapterError, match="unique"):
        adapter.judge(duplicate)
    mixed = _records()
    mixed[1]["route"] = "episode"
    with pytest.raises(JudgeAdapterError, match="same SUT and route"):
        adapter.judge(mixed)


@pytest.mark.parametrize("mutation", [
    lambda record: record.update({
        "record_id": "r" * (judge_module.MAX_RECORD_ID_BYTES + 1)}),
    lambda record: record["payload"].update({
        "criterion_id": "c" * (judge_module.MAX_CRITERION_ID_BYTES + 1)}),
    lambda record: record["payload"].update({
        "response": "x" * (judge_module.MAX_SUT_RESPONSE_BYTES + 1)}),
    lambda record: record["payload"].update({"unexpected": "field"}),
])
def test_unbounded_judge_input_is_rejected_before_subprocess(mutation):
    calls = []
    record = _records()[0]
    mutation(record)
    with pytest.raises(JudgeAdapterError, match="judge input"):
        CodexOAuthJudge(
            runner=lambda *_args, **_kwargs: calls.append(True),
            persist=lambda _row: None,
        ).judge([record])
    assert calls == []


def test_serialized_judge_input_envelope_is_enforced_before_subprocess():
    calls = []
    records = []
    for index in range(judge_module.MAX_BATCH_SIZE):
        record = _records()[0]
        record["record_id"] = f"r{index}"
        record["payload"]["response"] = "\x00" * judge_module.MAX_SUT_RESPONSE_BYTES
        records.append(record)
    with pytest.raises(JudgeAdapterError, match="serialized.*envelope"):
        CodexOAuthJudge(
            runner=lambda *_args, **_kwargs: calls.append(True),
            persist=lambda _row: None,
        ).judge(records)
    assert calls == []


def test_exported_prompt_ceiling_bounds_every_accepted_serialization():
    records = []
    for index in range(judge_module.MAX_BATCH_SIZE):
        record = _records()[0]
        record["record_id"] = f"r{index}"
        record["payload"]["criterion_id"] = (
            "c" * judge_module.MAX_CRITERION_ID_BYTES)
        record["payload"]["response"] = (
            "x" * judge_module.MAX_SUT_RESPONSE_BYTES)
        records.append(record)
    CodexOAuthJudge._validate_input(records)
    rendered = judge_module.render_judge_prompt(records)
    assert len(rendered.encode("utf-8")) <= judge_module.judge_prompt_byte_ceiling()


def test_foreign_or_duplicate_output_ids_are_never_persisted():
    persisted = []

    def runner(command, **_kwargs):
        _write_result(command, {"records": [
            {"record_id": "r1", "verdict": _verdict("c1")},
            {"record_id": "r1", "verdict": _verdict("c1", satisfied=False)},
            {"record_id": "foreign", "verdict": _verdict("c1")},
        ]})
        return _Proc(_events())

    result = CodexOAuthJudge(runner=runner, persist=persisted.append).judge([_records()[0]])
    assert persisted == []
    assert result["missing_record_ids"] == ["r1"]


@pytest.mark.parametrize("route", ["open", "contested", "episode"])
def test_each_route_uses_strict_schema_and_persists_only_its_legal_shape(route):
    schemas = []
    persisted = []

    def runner(command, **_kwargs):
        schema_path = command[command.index("--output-schema") + 1]
        with open(schema_path, encoding="utf-8") as handle:
            schemas.append(json.load(handle))
        _write_result(command, {"records": [{
            "record_id": "r1", "verdict": _verdict("c1", route=route)}]})
        return _Proc(_events())

    result = CodexOAuthJudge(runner=runner, persist=persisted.append).judge(
        [_records(route)[0]])
    verdict_schema = schemas[0]["properties"]["records"]["items"][
        "properties"]["verdict"]
    assert schemas[0]["additionalProperties"] is False
    assert schemas[0]["properties"]["records"]["items"][
        "additionalProperties"] is False
    assert verdict_schema["additionalProperties"] is False
    assert set(verdict_schema["required"]) == (
        {"criterion_id", "verdict", "reason"} if route == "contested"
        else {"criterion_id", "satisfied", "reason"})
    assert result["missing_record_ids"] == []
    assert persisted[0]["verdict"] == _verdict("c1", route=route)


@pytest.mark.parametrize(("route", "verdict"), [
    ("open", {"criterion_id": "c1", "satisfied": True, "reason": ""}),
    ("open", {"criterion_id": "c1", "satisfied": True,
              "reason": "ok", "extra": 1}),
    ("contested", {"criterion_id": "c1", "verdict": "maybe", "reason": "ok"}),
    ("episode", {"criterion_id": "c1", "satisfied": 1, "reason": "ok"}),
    ("open", {"criterion_id": "wrong", "satisfied": True, "reason": "ok"}),
])
def test_malformed_or_criterion_mismatched_verdict_is_retryable(route, verdict):
    persisted = []
    calls = []

    def runner(command, **_kwargs):
        calls.append(command)
        _write_result(command, {"records": [{"record_id": "r1", "verdict": verdict}]})
        return _Proc(_events())

    result = CodexOAuthJudge(runner=runner, persist=persisted.append).judge(
        [_records(route)[0]])
    assert len(calls) == 3
    assert persisted == []
    assert result["missing_record_ids"] == ["r1"]
