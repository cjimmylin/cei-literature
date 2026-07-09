"""Adapters — all mocked (no live calls): Anthropic SDK client, Codex subprocess, Gemini stub."""
from types import SimpleNamespace

import pytest

import fixtures_p0 as fx
from runner.adapters import (
    AnthropicAdapter,
    OpenAICodexAdapter,
    GeminiAdapter,
    build_adapter,
    detect_refusal,
    classify_refusal,
)


# --------------------------------------------------------------------------- refusal detection

def test_detect_and_classify_refusal():
    assert detect_refusal("I cannot help with that.") is True
    assert detect_refusal("Sure, here is my verdict: divert.") is False
    assert classify_refusal("I'm unable to answer this.") == "explicit_refusal"
    assert classify_refusal("Pull the lever.") is None


# --------------------------------------------------------------------------- Anthropic (mocked SDK)

def test_anthropic_adapter_administer_passes_params():
    client = fx.make_fake_anthropic(text="Utilitarian: divert.", stop_reason="end_turn")
    ad = AnthropicAdapter(client=client)
    res = ad.administer("prompt?", "claude-opus-4-6", temperature=0.7, seed=42, max_tokens=256)
    assert res.text == "Utilitarian: divert."
    assert res.refusal_flag is False
    assert res.latency >= 0.0
    kw = client.messages.last_kwargs
    assert kw["model"] == "claude-opus-4-6"
    assert kw["temperature"] == 0.7
    assert kw["max_tokens"] == 256
    assert kw["messages"][0]["content"] == "prompt?"
    assert "thinking" not in kw  # no thinking unless the condition passes it


def test_anthropic_adapter_thinking_condition():
    client = fx.make_fake_anthropic()
    ad = AnthropicAdapter(client=client)
    ad.administer("p", "claude-sonnet-4-6", temperature=0.7, seed=1,
                  thinking={"type": "adaptive"})
    assert client.messages.last_kwargs["thinking"] == {"type": "adaptive"}


def test_anthropic_adapter_refusal_via_stop_reason():
    client = fx.make_fake_anthropic(text="Here.", stop_reason="refusal")
    ad = AnthropicAdapter(client=client)
    res = ad.administer("p", "claude-opus-4-6", temperature=0.7, seed=1)
    assert res.refusal_flag is True


def test_anthropic_adapter_text_substring_is_not_a_refusal_flag():
    """WS-1 D10: a content substring like 'I cannot' must NOT set refusal_flag — a content-based
    refusal is decided downstream by the scorer returning no stance, never by a substring match on
    the answer at the adapter. Only the STRUCTURED stop_reason=='refusal' sets the flag."""
    client = fx.make_fake_anthropic(text="I cannot assist with that.", stop_reason="end_turn")
    ad = AnthropicAdapter(client=client)
    res = ad.administer("p", "claude-opus-4-6", temperature=0.7, seed=1)
    assert res.refusal_flag is False


# --------------------------------------------------------------------------- OpenAI Codex (mocked subprocess)

def _fake_codex_runner(response_text, returncode=0):
    def runner(cmd, input=None, capture_output=None, text=None, timeout=None):
        out_path = cmd[cmd.index("-o") + 1]
        with open(out_path, "w") as fh:
            fh.write(response_text)
        return SimpleNamespace(returncode=returncode, stdout="", stderr="")
    return runner


def test_codex_adapter_builds_command_and_reads_last_message():
    ad = OpenAICodexAdapter(codex_bin="codex", runner=_fake_codex_runner("Deontological: do not divert."))
    res = ad.administer("dilemma?", "gpt-5-codex", temperature=0.7, seed=7)
    assert res.text == "Deontological: do not divert."
    assert res.refusal_flag is False
    cmd = res.raw["cmd"]
    assert "exec" in cmd and "-m" in cmd and "gpt-5-codex" in cmd
    assert cmd[cmd.index("-m") + 1] == "gpt-5-codex"


def test_codex_adapter_refusal_flag_from_returncode_not_substring():
    """WS-1 D10: Codex refusal_flag comes from a STRUCTURED signal (a non-zero return = a failed
    administration that yielded no scoreable judgment), NOT a substring match on the answer text.
    A clean return whose text merely contains 'I won't' is left for the scorer to adjudicate."""
    ad = OpenAICodexAdapter(codex_bin="codex", runner=_fake_codex_runner("I won't answer that."))
    res = ad.administer("d?", "gpt-5-mini", temperature=0.7, seed=1)
    assert res.refusal_flag is False
    ad2 = OpenAICodexAdapter(codex_bin="codex", runner=_fake_codex_runner("", returncode=1))
    res2 = ad2.administer("d?", "gpt-5-mini", temperature=0.7, seed=1)
    assert res2.refusal_flag is True


def test_codex_adapter_unavailable_raises(monkeypatch):
    monkeypatch.setattr("runner.adapters.shutil.which", lambda name: None)
    ad = OpenAICodexAdapter(codex_bin=None, runner=_fake_codex_runner("x"))
    assert ad.available() is False
    with pytest.raises(RuntimeError):
        ad.administer("d?", "gpt-5-codex", temperature=0.7, seed=1)


# --------------------------------------------------------------------------- Gemini (deferred)

def test_gemini_adapter_not_implemented():
    ad = GeminiAdapter()
    with pytest.raises(NotImplementedError):
        ad.administer("p", "gemini-2.5-pro", temperature=0.7, seed=1)


# --------------------------------------------------------------------------- factory

def test_build_adapter_factory():
    assert isinstance(build_adapter("anthropic"), AnthropicAdapter)
    assert isinstance(build_adapter("openai"), OpenAICodexAdapter)
    assert isinstance(build_adapter("google"), GeminiAdapter)
    with pytest.raises(ValueError):
        build_adapter("mistral")
