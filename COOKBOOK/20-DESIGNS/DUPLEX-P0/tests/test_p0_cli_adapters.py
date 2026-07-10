"""SMOKE-ONLY `claude -p` adapter — all mocked (no live calls). The adapter is deliberately kept
out of the validity path (V-2 prohibits `claude -p` for the real P0); these tests pin its
subprocess contract and its F-1-style admin-error / refusal semantics."""
from types import SimpleNamespace

import pytest

from runner.cli_adapters import AnthropicCLIAdapter, SMOKE_ONLY
from runner.adapters import AdministrationError


def _fake_claude_runner(response_text, returncode=0):
    def runner(cmd, capture_output=None, text=None, timeout=None, cwd=None, **_):
        return SimpleNamespace(returncode=returncode, stdout=response_text, stderr="")
    return runner


def _no_sleep(_seconds):
    return None


def test_module_is_marked_smoke_only():
    """Guardrail: the module advertises SMOKE_ONLY so no caller mistakes it for a valid backend."""
    assert SMOKE_ONLY is True


def test_claude_cli_builds_print_command_and_reads_stdout():
    """`claude -p <prompt> --model <id> --output-format text`; the response is stdout text."""
    ad = AnthropicCLIAdapter(claude_bin="claude",
                             runner=_fake_claude_runner("Utilitarian: divert.\n"))
    res = ad.administer("dilemma?", "claude-haiku-4-5", temperature=0.7, seed=1)
    assert res.text == "Utilitarian: divert."
    cmd = res.raw["cmd"]
    assert "-p" in cmd and "--model" in cmd
    assert cmd[cmd.index("--model") + 1] == "claude-haiku-4-5"
    assert "dilemma?" in cmd                       # prompt passed on the command line
    assert res.raw["smoke_only"] is True and res.raw["backend"] == "claude -p"


def test_claude_cli_refusal_flag_is_always_false():
    """Like Codex, `claude -p` has no structured refusal signal (no stop_reason, V-2) — refusal_flag
    is ALWAYS False; a content refusal is decided downstream by the scorer returning no stance."""
    ad = AnthropicCLIAdapter(claude_bin="claude",
                             runner=_fake_claude_runner("No, I can't do that."))
    res = ad.administer("d?", "claude-haiku-4-5", temperature=0.7, seed=1)
    assert res.refusal_flag is False


def test_claude_cli_nonzero_exit_is_admin_error_not_refusal():
    """A non-zero exit is an administration failure (auth/CLI crash), NOT a refusal — bounded retry
    then RAISE fail-loud (F-1 semantics carried into the smoke backend)."""
    ad = AnthropicCLIAdapter(claude_bin="claude",
                             runner=_fake_claude_runner("", returncode=1),
                             max_retries=2, sleep=_no_sleep)
    with pytest.raises(AdministrationError):
        ad.administer("d?", "claude-haiku-4-5", temperature=0.7, seed=1)


def test_claude_cli_unavailable_raises(monkeypatch):
    monkeypatch.setattr("runner.cli_adapters.shutil.which", lambda name: None)
    ad = AnthropicCLIAdapter(claude_bin=None, runner=_fake_claude_runner("x"))
    assert ad.available() is False
    with pytest.raises(RuntimeError):
        ad.administer("d?", "claude-haiku-4-5", temperature=0.7, seed=1)


def test_claude_cli_ignores_sampling_and_thinking_kwargs():
    """V-2: `claude -p` has no sampling/thinking control — the adapter absorbs those kwargs
    (omit_sampling_params, thinking, max_tokens) without error and never puts them on the cmd."""
    ad = AnthropicCLIAdapter(claude_bin="claude",
                             runner=_fake_claude_runner("ok"))
    res = ad.administer("d?", "claude-haiku-4-5", temperature=0.7, seed=1,
                        omit_sampling_params=True, thinking={"type": "adaptive"}, max_tokens=4096)
    assert res.text == "ok"
    assert "--temperature" not in res.raw["cmd"] and "--thinking" not in res.raw["cmd"]
