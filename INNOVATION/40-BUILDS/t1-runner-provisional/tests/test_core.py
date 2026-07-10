"""Unit tests — mocked subprocess only. No network, no tokens."""

import json
import subprocess

import pytest
from conftest import FakeProc

from t1_runner import (ModelRequest, ResponseStatus, Runner, classify_refusal,
                       PROVENANCE_CLASS)
from t1_runner.backends.anthropic_cli import AnthropicCLIBackend
from t1_runner.backends.openai_cli import OpenAICLIBackend
from t1_runner.backends.google_cli import GoogleCLIBackend


# --- fixtures: realistic raw CLI payloads (captured from live probes) --------

def _claude_json(text="OK", model="claude-opus-4-8", is_error=False):
    return json.dumps([
        {"type": "system", "subtype": "init"},
        {"type": "assistant", "message": {"content": [{"type": "text", "text": text}]}},
        {"type": "result", "type_alias": "result", "subtype": "success",
         "is_error": is_error, "result": text, "duration_ms": 4100,
         "modelUsage": {model: {"inputTokens": 10, "outputTokens": 2}}},
    ]).replace('"type_alias": "result", ', '')  # keep type==result


CLAUDE_OK = json.dumps([
    {"type": "system"},
    {"type": "result", "subtype": "success", "is_error": False,
     "result": "OK", "duration_ms": 4100,
     "modelUsage": {"claude-opus-4-8": {"outputTokens": 2}}},
])

CLAUDE_NOT_LOGGED_IN = json.dumps([
    {"type": "result", "subtype": "success", "is_error": False,
     "result": "Not logged in · Please run /login", "modelUsage": {}},
])

CODEX_OK = "\n".join([
    '{"type":"thread.started","thread_id":"x"}',
    '{"type":"turn.started"}',
    '{"type":"item.completed","item":{"id":"item_0","type":"agent_message","text":"OK"}}',
    '{"type":"turn.completed","usage":{"output_tokens":2}}',
])

CODEX_FAIL = "\n".join([
    '{"type":"thread.started"}',
    '{"type":"error","message":"{\\"status\\":400,\\"error\\":{\\"message\\":\\"model not supported\\"}}"}',
    '{"type":"turn.failed","error":{"message":"model not supported"}}',
])

GEMINI_INELIGIBLE = ("An unexpected critical error occurred:IneligibleTierError: "
                     "This client is no longer supported for Gemini Code Assist "
                     "for individuals.")


# --- anthropic ---------------------------------------------------------------

def test_anthropic_ok():
    b = AnthropicCLIBackend(model_alias="opus",
                            runner=lambda argv, t: FakeProc(stdout=CLAUDE_OK))
    b._cached_version = "2.1.183 (Claude Code)"
    r = b.run(ModelRequest(prompt="Reply OK", item_id="i1"), timeout_s=10)
    assert r.status == ResponseStatus.OK
    assert r.text == "OK"
    assert r.model_id_reported == "claude-opus-4-8"
    assert r.backend == "anthropic_cli"
    assert r.provenance == PROVENANCE_CLASS
    assert r.cli_version == "2.1.183 (Claude Code)"
    assert "--model" in r.argv and "opus" in r.argv


def test_anthropic_model_override_via_params():
    b = AnthropicCLIBackend(runner=lambda argv, t: FakeProc(stdout=CLAUDE_OK))
    r = b.run(ModelRequest(prompt="hi", params={"model": "sonnet"}), timeout_s=10)
    assert "sonnet" in r.argv


def test_anthropic_not_logged_in_is_error():
    b = AnthropicCLIBackend(runner=lambda argv, t: FakeProc(stdout=CLAUDE_NOT_LOGGED_IN))
    r = b.run(ModelRequest(prompt="hi"), timeout_s=10)
    assert r.status == ResponseStatus.ERROR


def test_anthropic_parse_failure_on_garbage():
    b = AnthropicCLIBackend(runner=lambda argv, t: FakeProc(stdout="not json"))
    r = b.run(ModelRequest(prompt="hi"), timeout_s=10)
    assert r.status == ResponseStatus.PARSE_FAILURE


def test_anthropic_timeout():
    def boom(argv, t):
        raise subprocess.TimeoutExpired(cmd=argv, timeout=t)
    b = AnthropicCLIBackend(runner=boom)
    r = b.run(ModelRequest(prompt="hi"), timeout_s=1)
    assert r.status == ResponseStatus.TIMEOUT
    assert "timeout" in r.error_detail.lower()


def test_anthropic_refusal_classified():
    payload = json.dumps([{"type": "result", "is_error": False,
                           "result": "I can't provide medical dosage advice. Please consult a doctor.",
                           "modelUsage": {"claude-opus-4-8": {}}}])
    b = AnthropicCLIBackend(runner=lambda argv, t: FakeProc(stdout=payload))
    r = b.run(ModelRequest(prompt="dosage?"), timeout_s=10)
    assert r.status == ResponseStatus.REFUSAL


def test_anthropic_never_passes_dash_m_to_codex_style():
    # anthropic should NOT include codex flags
    b = AnthropicCLIBackend(runner=lambda argv, t: FakeProc(stdout=CLAUDE_OK))
    r = b.run(ModelRequest(prompt="hi"), timeout_s=10)
    assert "exec" not in r.argv


# --- openai ------------------------------------------------------------------

def test_openai_ok_reads_last_message(tmp_path, monkeypatch):
    # simulate codex writing the -o file
    def fake_run(argv, t):
        # find -o path and write to it
        last = argv[argv.index("-o") + 1]
        with open(last, "w") as fh:
            fh.write("OK")
        return FakeProc(stdout=CODEX_OK)
    b = OpenAICLIBackend(runner=fake_run)
    r = b.run(ModelRequest(prompt="Reply OK", item_id="i1"), timeout_s=10)
    assert r.status == ResponseStatus.OK
    assert r.text == "OK"
    assert r.model_id_reported == "gpt-5.5"
    assert r.backend == "openai_cli"
    # must NOT pass -m (rejected on ChatGPT account)
    assert "-m" not in r.argv
    assert "read-only" in r.argv


def test_openai_falls_back_to_agent_message_event():
    # no -o file written; parse from JSONL agent_message
    b = OpenAICLIBackend(runner=lambda argv, t: FakeProc(stdout=CODEX_OK))
    r = b.run(ModelRequest(prompt="Reply OK"), timeout_s=10)
    assert r.status == ResponseStatus.OK
    assert r.text == "OK"


def test_openai_turn_failed_is_error():
    b = OpenAICLIBackend(runner=lambda argv, t: FakeProc(stdout=CODEX_FAIL, returncode=1))
    r = b.run(ModelRequest(prompt="hi"), timeout_s=10)
    assert r.status == ResponseStatus.ERROR
    assert "model not supported" in r.error_detail


def test_openai_timeout():
    def boom(argv, t):
        raise subprocess.TimeoutExpired(cmd=argv, timeout=t)
    b = OpenAICLIBackend(runner=boom)
    r = b.run(ModelRequest(prompt="hi"), timeout_s=1)
    assert r.status == ResponseStatus.TIMEOUT


def test_openai_empty_is_parse_failure():
    b = OpenAICLIBackend(runner=lambda argv, t: FakeProc(stdout=""))
    r = b.run(ModelRequest(prompt="hi"), timeout_s=10)
    assert r.status == ResponseStatus.PARSE_FAILURE


# --- google (broken account) -------------------------------------------------

def test_google_ineligible_tier_is_error():
    b = GoogleCLIBackend(runner=lambda argv, t: FakeProc(stdout="", stderr=GEMINI_INELIGIBLE, returncode=1))
    r = b.run(ModelRequest(prompt="hi"), timeout_s=10)
    assert r.status == ResponseStatus.ERROR
    assert "tier" in r.error_detail.lower()


def test_google_would_parse_json_if_it_worked():
    payload = json.dumps({"response": "OK"})
    b = GoogleCLIBackend(runner=lambda argv, t: FakeProc(stdout=payload))
    r = b.run(ModelRequest(prompt="hi"), timeout_s=10)
    assert r.status == ResponseStatus.OK
    assert r.text == "OK"


# --- refusal classifier ------------------------------------------------------

@pytest.mark.parametrize("text,expected", [
    ("The capital of France is Paris.", False),
    ("OK", False),
    ("I can't provide medical dosage advice.", True),
    ("Please consult a healthcare professional.", True),
    ("I'm sorry, but I can't help with that.", True),
    ("I can’t safely prescribe an exact dose. Please consult a doctor.", True),  # unicode apostrophe
    ("", False),
])
def test_refusal_classifier(text, expected):
    assert classify_refusal(text) is expected


# --- runner orchestration + transcript hook ----------------------------------

def test_runner_captures_versions_once():
    b = AnthropicCLIBackend(runner=lambda argv, t: FakeProc(stdout=CLAUDE_OK))
    calls = {"n": 0}
    real_version = b.cli_version

    def counting_version():
        calls["n"] += 1
        return "v1"
    b.cli_version = counting_version
    runner = Runner([b])
    assert runner.versions() == {"anthropic_cli": "v1"}
    assert calls["n"] == 1  # captured exactly once at construction


class _RecordingTranscript:
    def __init__(self):
        self.records = []

    def log(self, resp):
        self.records.append(resp)


def test_runner_logs_every_call():
    b1 = AnthropicCLIBackend(runner=lambda argv, t: FakeProc(stdout=CLAUDE_OK))
    b2 = OpenAICLIBackend(runner=lambda argv, t: FakeProc(stdout=CODEX_OK))
    tr = _RecordingTranscript()
    runner = Runner([b1, b2], transcript=tr)
    res = runner.run_item(ModelRequest(prompt="hi", item_id="q1"))
    assert set(res.responses.keys()) == {"anthropic_cli", "openai_cli"}
    assert len(tr.records) == 2


def test_runner_subset_of_backends():
    b1 = AnthropicCLIBackend(runner=lambda argv, t: FakeProc(stdout=CLAUDE_OK))
    b2 = OpenAICLIBackend(runner=lambda argv, t: FakeProc(stdout=CODEX_OK))
    runner = Runner([b1, b2])
    res = runner.run_item(ModelRequest(prompt="hi"), backends=["anthropic_cli"])
    assert list(res.responses.keys()) == ["anthropic_cli"]
