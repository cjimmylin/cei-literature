"""Hermetic tests for CLIModelClient — NO real `claude` calls.

Every test monkeypatches ``subprocess.run`` so the suite stays offline and
deterministic. We verify: command assembly (model + single-turn hygiene flags),
JSON-array result parsing (the 2.1.183 stream shape), the bare-object fallback,
error paths (nonzero exit, is_error, empty stdout, bad JSON), OAuth env handling
(ANTHROPIC_API_KEY dropped), and cost/call bookkeeping.
"""

from __future__ import annotations

import json
import os
import sys

import pytest

HARNESS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS_ROOT not in sys.path:
    sys.path.insert(0, HARNESS_ROOT)

from wcfbench import CLIModelClient, CLIClientError  # noqa: E402
from wcfbench import cli_client as cli_mod  # noqa: E402


class _FakeProc:
    def __init__(self, returncode=0, stdout="", stderr=""):
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr


# The observed 2.1.183 shape: a JSON array whose final type==result carries .result.
def _stream_stdout(result_text, cost=0.021568, is_error=False):
    return json.dumps([
        {"type": "system", "subtype": "init", "model": "claude-haiku-4-5-20251001"},
        {"type": "assistant", "message": {"content": [{"type": "text", "text": result_text}]}},
        {"type": "result", "subtype": "success", "is_error": is_error,
         "result": result_text, "total_cost_usd": cost},
    ])


def _patch_run(monkeypatch, *, stdout="", returncode=0, stderr="", capture=None):
    def fake_run(cmd, **kwargs):
        if capture is not None:
            capture["cmd"] = cmd
            capture["kwargs"] = kwargs
        return _FakeProc(returncode=returncode, stdout=stdout, stderr=stderr)
    monkeypatch.setattr(cli_mod.subprocess, "run", fake_run)


def test_complete_parses_stream_result(monkeypatch):
    cap = {}
    _patch_run(monkeypatch, stdout=_stream_stdout("a < b < c", cost=0.02), capture=cap)
    client = CLIModelClient(model="claude-haiku-4-5-20251001")
    out = client.complete("Rank these", item_id="AGG-C6-W301")
    assert out == "a < b < c"
    assert client.calls_made == 1
    assert client.cost_usd == pytest.approx(0.02)
    # command assembly: model pinned + single-turn hygiene flags present
    cmd = cap["cmd"]
    assert cmd[:2] == ["claude", "-p"]
    assert "--model" in cmd and "claude-haiku-4-5-20251001" in cmd
    for flag in ("--tools", "--strict-mcp-config", "--permission-mode", "--max-turns", "--setting-sources"):
        assert flag in cmd
    assert cmd[cmd.index("--max-turns") + 1] == "1"


def test_complete_parses_bare_object(monkeypatch):
    _patch_run(monkeypatch, stdout=json.dumps({"type": "result", "result": "OK", "total_cost_usd": 0.0}))
    assert CLIModelClient().complete("hi") == "OK"


def test_force_oauth_drops_api_key(monkeypatch):
    cap = {}
    _patch_run(monkeypatch, stdout=_stream_stdout("OK"), capture=cap)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-should-be-dropped")
    CLIModelClient(force_oauth=True).complete("hi")
    assert "ANTHROPIC_API_KEY" not in cap["kwargs"]["env"]


def test_keep_api_key_when_not_forcing_oauth(monkeypatch):
    cap = {}
    _patch_run(monkeypatch, stdout=_stream_stdout("OK"), capture=cap)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-keep")
    CLIModelClient(force_oauth=False).complete("hi")
    assert cap["kwargs"]["env"].get("ANTHROPIC_API_KEY") == "sk-keep"


def test_nonzero_exit_raises(monkeypatch):
    _patch_run(monkeypatch, returncode=1, stderr="boom")
    with pytest.raises(CLIClientError) as ei:
        CLIModelClient().complete("hi", item_id="X")
    assert "exited 1" in str(ei.value)


def test_result_is_error_raises(monkeypatch):
    _patch_run(monkeypatch, stdout=_stream_stdout("", is_error=True))
    with pytest.raises(CLIClientError):
        CLIModelClient().complete("hi")


def test_empty_and_bad_json_raise(monkeypatch):
    _patch_run(monkeypatch, stdout="   ")
    with pytest.raises(CLIClientError):
        CLIModelClient().complete("hi")
    _patch_run(monkeypatch, stdout="not json at all")
    with pytest.raises(CLIClientError):
        CLIModelClient().complete("hi")


def test_check_available(monkeypatch):
    _patch_run(monkeypatch, returncode=0, stdout="2.1.183")
    assert CLIModelClient.check_available() is True
    _patch_run(monkeypatch, returncode=127)
    assert CLIModelClient.check_available() is False
