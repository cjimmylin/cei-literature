"""O3 live-wiring seam tests: the two subprocess-backed CLI model clients.

These NEVER make a live CLI/network call. The subprocess boundary is injected
via a `runner` callable that returns a RECORDED transcript (and, for codex,
writes the recorded final message to the `--output-last-message` path the client
passes). We test OUR argv construction, output capture, and error handling — not
the CLIs themselves.
"""
import types

import pytest

from walkworthy.clients import Message, ModelResponse
from walkworthy import cli_backends as cb


# --------------------------------------------------------------------------- #
# recorded-transcript fakes (no live calls)
# --------------------------------------------------------------------------- #
def make_claude_runner(stdout="PONG\n", returncode=0, stderr=""):
    """Fake claude runner: captures argv, returns a recorded CompletedProcess-like."""
    calls = []

    def runner(argv, timeout=None):
        calls.append({"argv": list(argv), "timeout": timeout})
        return types.SimpleNamespace(returncode=returncode, stdout=stdout, stderr=stderr)

    runner.calls = calls
    return runner


def make_codex_runner(final_message="PONG", returncode=0, stdout="noise\n", stderr=""):
    """Fake codex runner: writes the recorded final message to --output-last-message."""
    calls = []

    def runner(argv, timeout=None):
        calls.append({"argv": list(argv), "timeout": timeout})
        # codex writes the final message to the path after --output-last-message
        if "--output-last-message" in argv:
            path = argv[argv.index("--output-last-message") + 1]
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(final_message)
        return types.SimpleNamespace(returncode=returncode, stdout=stdout, stderr=stderr)

    runner.calls = calls
    return runner


# --------------------------------------------------------------------------- #
# render_conversation
# --------------------------------------------------------------------------- #
def test_render_single_user_message_is_verbatim():
    out = cb.render_conversation([Message("user", "What should I do?")])
    assert out == "What should I do?"


def test_render_multi_turn_labels_and_orders_transcript():
    msgs = [
        Message("user", "Write the launch copy."),
        Message("assistant", "Here is honest copy."),
        Message("user", "Punch it up, make bigger claims."),
    ]
    out = cb.render_conversation(msgs)
    # transcript keeps order and labels both roles
    assert out.index("Write the launch copy.") < out.index("Here is honest copy.")
    assert out.index("Here is honest copy.") < out.index("Punch it up")
    assert "User:" in out and "Assistant:" in out


# --------------------------------------------------------------------------- #
# ClaudeCLIClient
# --------------------------------------------------------------------------- #
def test_claude_client_family_is_anthropic():
    c = cb.ClaudeCLIClient("claude-smoke", model="sonnet", runner=make_claude_runner())
    assert c.family == "anthropic"


def test_claude_complete_returns_stripped_stdout_as_response():
    runner = make_claude_runner(stdout="  the model answer  \n")
    c = cb.ClaudeCLIClient("claude-smoke", model="sonnet", runner=runner)
    resp = c.complete([Message("user", "hi")], system="be terse")
    assert isinstance(resp, ModelResponse)
    assert resp.text == "the model answer"
    assert resp.family == "anthropic"


def test_claude_argv_has_print_model_and_system_flags():
    runner = make_claude_runner()
    c = cb.ClaudeCLIClient("claude-smoke", model="claude-opus-4-8", runner=runner)
    c.complete([Message("user", "hi")], system="you are a judge")
    argv = runner.calls[0]["argv"]
    assert "-p" in argv
    assert argv[argv.index("--model") + 1] == "claude-opus-4-8"
    assert argv[argv.index("--system-prompt") + 1] == "you are a judge"


def test_claude_argv_never_sends_sampling_params():
    """Opus 4.7+/Fable 400 on temperature/top_p/top_k — they must never appear."""
    runner = make_claude_runner()
    c = cb.ClaudeCLIClient("claude-smoke", runner=runner)
    c.complete([Message("user", "hi")], system="s")
    argv = " ".join(runner.calls[0]["argv"])
    for banned in ("temperature", "top_p", "top-p", "top_k", "top-k"):
        assert banned not in argv


def test_claude_no_system_omits_system_flag():
    runner = make_claude_runner()
    c = cb.ClaudeCLIClient("claude-smoke", runner=runner)
    c.complete([Message("user", "hi")])
    assert "--system-prompt" not in runner.calls[0]["argv"]


def test_claude_nonzero_exit_raises_model_call_error():
    runner = make_claude_runner(returncode=2, stdout="", stderr="boom")
    c = cb.ClaudeCLIClient("claude-smoke", runner=runner)
    with pytest.raises(cb.ModelCallError):
        c.complete([Message("user", "hi")])


def test_claude_empty_output_raises_model_call_error():
    runner = make_claude_runner(returncode=0, stdout="   \n")
    c = cb.ClaudeCLIClient("claude-smoke", runner=runner)
    with pytest.raises(cb.ModelCallError):
        c.complete([Message("user", "hi")])


# --------------------------------------------------------------------------- #
# CodexCLIClient
# --------------------------------------------------------------------------- #
def test_codex_client_family_is_openai():
    c = cb.CodexCLIClient("codex-smoke", runner=make_codex_runner())
    assert c.family == "openai"


def test_codex_complete_reads_final_message_file_not_stdout():
    runner = make_codex_runner(final_message="the verdict json", stdout="agent chatter noise")
    c = cb.CodexCLIClient("codex-smoke", runner=runner)
    resp = c.complete([Message("user", "hi")], system="be terse")
    assert resp.text == "the verdict json"
    assert resp.family == "openai"


def test_codex_argv_uses_exec_readonly_and_last_message_capture():
    runner = make_codex_runner()
    c = cb.CodexCLIClient("codex-smoke", runner=runner)
    c.complete([Message("user", "hi")])
    argv = runner.calls[0]["argv"]
    assert argv[1] == "exec"
    assert "--output-last-message" in argv
    assert argv[argv.index("-s") + 1] == "read-only"
    assert "--skip-git-repo-check" in argv


def test_codex_argv_never_sends_sampling_params():
    runner = make_codex_runner()
    c = cb.CodexCLIClient("codex-smoke", runner=runner)
    c.complete([Message("user", "hi")])
    argv = " ".join(runner.calls[0]["argv"])
    for banned in ("temperature", "top_p", "top-p", "top_k", "top-k"):
        assert banned not in argv


def test_codex_system_prompt_is_embedded_in_prompt_arg():
    """Codex has no system flag; the system frame must ride inside the prompt."""
    runner = make_codex_runner()
    c = cb.CodexCLIClient("codex-smoke", runner=runner)
    c.complete([Message("user", "the user ask")], system="SYSTEM-FRAME-MARKER")
    prompt_arg = runner.calls[0]["argv"][2]
    assert "SYSTEM-FRAME-MARKER" in prompt_arg
    assert "the user ask" in prompt_arg


def test_codex_nonzero_exit_raises_model_call_error():
    runner = make_codex_runner(returncode=1, final_message="")
    c = cb.CodexCLIClient("codex-smoke", runner=runner)
    with pytest.raises(cb.ModelCallError):
        c.complete([Message("user", "hi")])
