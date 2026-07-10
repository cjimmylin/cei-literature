"""Adapters — all mocked (no live calls): Anthropic SDK client, Codex subprocess, Gemini stub."""
from types import SimpleNamespace

import pytest

import fixtures_p0 as fx
from runner.adapters import (
    AnthropicAdapter,
    OpenAICodexAdapter,
    OpenAIAPIAdapter,
    GeminiAdapter,
    AdministrationError,
    build_adapter,
    detect_refusal,
    classify_refusal,
    resolve_auth_mode,
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


def test_anthropic_adapter_omits_temperature_on_v4_drop():
    """F-2 / SA-6: on a V-4 temperature drop the adapter must send NO sampling param — the current
    API rejects a modified temperature with extended thinking (and Opus 4.7+/Fable reject it
    outright). omit_sampling_params=True removes `temperature` from the request entirely."""
    client = fx.make_fake_anthropic()
    ad = AnthropicAdapter(client=client)
    ad.administer("p", "claude-opus-4-6", temperature=0.7, seed=1,
                  thinking={"type": "adaptive"}, omit_sampling_params=True)
    assert "temperature" not in client.messages.last_kwargs
    assert client.messages.last_kwargs["thinking"] == {"type": "adaptive"}
    # default path still sends temperature (roster models accept it on non-thinking calls)
    client2 = fx.make_fake_anthropic()
    ad2 = AnthropicAdapter(client=client2)
    ad2.administer("p", "claude-opus-4-6", temperature=0.7, seed=1)
    assert client2.messages.last_kwargs["temperature"] == 0.7


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


def _sequenced_codex_runner(returncodes, response_text="Verdict: divert."):
    """A runner whose returncode follows `returncodes` per successive call (for retry tests)."""
    seq = list(returncodes)
    calls = {"n": 0}

    def runner(cmd, input=None, capture_output=None, text=None, timeout=None):
        rc = seq[min(calls["n"], len(seq) - 1)]
        calls["n"] += 1
        out_path = cmd[cmd.index("-o") + 1]
        with open(out_path, "w") as fh:
            fh.write(response_text if rc == 0 else "")
        return SimpleNamespace(returncode=rc, stdout="", stderr="boom")
    runner.calls = calls
    return runner


def _no_sleep(_seconds):
    return None


def test_codex_adapter_builds_command_and_reads_last_message():
    ad = OpenAICodexAdapter(codex_bin="codex", runner=_fake_codex_runner("Deontological: do not divert."))
    res = ad.administer("dilemma?", "gpt-5-codex", temperature=0.7, seed=7)
    assert res.text == "Deontological: do not divert."
    assert res.refusal_flag is False
    cmd = res.raw["cmd"]
    assert "exec" in cmd and "-m" in cmd and "gpt-5-codex" in cmd
    assert cmd[cmd.index("-m") + 1] == "gpt-5-codex"


def test_codex_returncode_nonzero_is_admin_error_not_refusal():
    """F-1 / SA-5: 'Codex `returncode != 0` = administration error: bounded retry with exponential
    backoff, then RAISE fail-loud. Never a refusal; never checkpointed as complete.' A persistently
    non-zero return must raise AdministrationError after the retries are exhausted — it must NOT be
    reported as a refusal (the old returncode!=0 -> refusal_flag=True behavior is OVERTURNED)."""
    ad = OpenAICodexAdapter(
        codex_bin="codex", runner=_fake_codex_runner("", returncode=1),
        max_retries=2, sleep=_no_sleep,
    )
    with pytest.raises(AdministrationError):
        ad.administer("d?", "gpt-5-mini", temperature=0.7, seed=1)


def test_codex_refusal_flag_is_always_false_content_refusal_left_to_scorer():
    """F-1 / SA-5: 'Codex `refusal_flag` is always False; content refusal = scorer->None ->
    "no_stance".' A clean (returncode 0) return whose text contains 'I won't' is NOT a refusal at
    the adapter — the scorer decides downstream."""
    ad = OpenAICodexAdapter(codex_bin="codex", runner=_fake_codex_runner("I won't answer that."))
    res = ad.administer("d?", "gpt-5-mini", temperature=0.7, seed=1)
    assert res.refusal_flag is False


def test_codex_admin_error_bounded_retry_then_succeeds():
    """F-1 / SA-5: 'bounded retry with exponential backoff' — a transient non-zero return that
    recovers on a later attempt yields a normal scored administration (no refusal, no raise)."""
    runner = _sequenced_codex_runner([1, 1, 0], response_text="Deontological: hold.")
    ad = OpenAICodexAdapter(codex_bin="codex", runner=runner, max_retries=4, sleep=_no_sleep)
    res = ad.administer("d?", "gpt-5-mini", temperature=0.7, seed=1)
    assert res.text == "Deontological: hold."
    assert res.refusal_flag is False
    assert runner.calls["n"] == 3  # two failures + one success


def test_anthropic_adapter_bounded_retry_transient_then_succeeds():
    """F-1 / SA-5: 'Anthropic adapter gains the same bounded retry for transient API errors
    (rate-limit/overloaded/network); persistent errors raise.' A transient error that recovers
    yields a normal result; the structured refusal path is unchanged."""
    calls = {"n": 0}

    class RateLimitError(Exception):
        pass

    def create(**kwargs):
        calls["n"] += 1
        if calls["n"] < 3:
            raise RateLimitError("429 slow down")
        block = SimpleNamespace(type="text", text="Utilitarian: divert.")
        return SimpleNamespace(content=[block], stop_reason="end_turn")

    client = SimpleNamespace(messages=SimpleNamespace(create=create))
    ad = AnthropicAdapter(client=client, max_retries=4, sleep=_no_sleep)
    res = ad.administer("p", "claude-opus-4-6", temperature=0.7, seed=1)
    assert res.text == "Utilitarian: divert."
    assert res.refusal_flag is False
    assert calls["n"] == 3


def test_anthropic_adapter_retries_503_504_service_conditions():
    """F-1 / SA-5.3 (audit F-1.b): the transient set must cover the real anthropic 5xx service
    conditions — a 503 ServiceUnavailableError / 504 DeadlineExceededError is a transient
    'network'/overloaded condition that must be RETRIED, not raised on first occurrence."""
    for exc_name in ("ServiceUnavailableError", "DeadlineExceededError"):
        calls = {"n": 0}
        exc_type = type(exc_name, (Exception,), {})

        def create(**kwargs):
            calls["n"] += 1
            if calls["n"] < 2:
                raise exc_type("transient 5xx")
            block = SimpleNamespace(type="text", text="ok")
            return SimpleNamespace(content=[block], stop_reason="end_turn")

        client = SimpleNamespace(messages=SimpleNamespace(create=create))
        ad = AnthropicAdapter(client=client, max_retries=3, sleep=_no_sleep)
        res = ad.administer("p", "claude-opus-4-6", temperature=0.7, seed=1)
        assert res.text == "ok" and calls["n"] == 2, exc_name


def test_anthropic_adapter_persistent_transient_raises_admin_error():
    """F-1 / SA-5: persistent transient API errors 'raise' fail-loud (as an administration error),
    never a silent refusal or checkpointed cell."""

    class InternalServerError(Exception):
        pass

    def create(**kwargs):
        raise InternalServerError("529 overloaded")

    client = SimpleNamespace(messages=SimpleNamespace(create=create))
    ad = AnthropicAdapter(client=client, max_retries=2, sleep=_no_sleep)
    with pytest.raises(AdministrationError):
        ad.administer("p", "claude-opus-4-6", temperature=0.7, seed=1)


def test_anthropic_adapter_auth_error_is_not_retried():
    """F-1 / SA-5 addendum: 'fail loud only when the first call errors with an authentication
    error.' An authentication error is NOT transient — it must propagate immediately, unretried."""

    class AuthenticationError(Exception):
        pass

    calls = {"n": 0}

    def create(**kwargs):
        calls["n"] += 1
        raise AuthenticationError("401 invalid key")

    client = SimpleNamespace(messages=SimpleNamespace(create=create))
    ad = AnthropicAdapter(client=client, max_retries=5, sleep=_no_sleep)
    with pytest.raises(AuthenticationError):
        ad.administer("p", "claude-opus-4-6", temperature=0.7, seed=1)
    assert calls["n"] == 1  # no retry on a non-transient auth failure


def test_resolve_auth_mode_precedence_and_empty_key_edge():
    """F-1 / SA-5 addendum (OAuth credential path): the SDK credential chain resolves
    'API key -> ANTHROPIC_AUTH_TOKEN -> `ant auth login` profile'. Sharp edge: an EMPTY
    ANTHROPIC_API_KEY='' must NOT outrank the profile in our reported auth mode (an empty key is
    treated as unset)."""
    assert resolve_auth_mode({"ANTHROPIC_API_KEY": "sk-abc"}) == "api_key"
    assert resolve_auth_mode({"ANTHROPIC_AUTH_TOKEN": "oat-xyz"}) == "auth_token"
    assert resolve_auth_mode({}) == "profile"
    # empty API key is treated as unset -> falls through to the profile
    assert resolve_auth_mode({"ANTHROPIC_API_KEY": ""}) == "profile"
    assert resolve_auth_mode({"ANTHROPIC_API_KEY": "", "ANTHROPIC_AUTH_TOKEN": "oat"}) == "auth_token"


def test_anthropic_adapter_does_not_hard_require_api_key(monkeypatch):
    """F-1 / SA-5 addendum: 'The AnthropicAdapter must NOT hard-require ANTHROPIC_API_KEY.
    Construct a bare anthropic.Anthropic() and let the SDK credential chain resolve.' With no key
    in the env, constructing the live client must succeed (auth is deferred to the first call), and
    the resolved auth mode is recorded for run metadata."""
    import sys

    constructed = {"n": 0}

    class _FakeAnthropic:
        def __init__(self, *a, **k):
            constructed["n"] += 1  # NOTE: no api_key required

    fake_module = SimpleNamespace(Anthropic=_FakeAnthropic)
    monkeypatch.setitem(sys.modules, "anthropic", fake_module)
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.delenv("ANTHROPIC_AUTH_TOKEN", raising=False)

    ad = AnthropicAdapter()  # no client injected, no key in env
    _ = ad.client            # lazy construction must NOT raise "key not set"
    assert constructed["n"] == 1
    assert ad.auth_mode == "profile"  # resolved from the credential chain


def test_codex_adapter_sandbox_and_cwd_flags_optional_and_off_by_default():
    """Safety: `codex exec` is an agentic runner (defaults to danger-full-access). When constructed
    with sandbox/cwd (as the smoke does) the command must carry `--sandbox read-only` + `-C <dir>`
    so the subject cannot touch the vault; with the defaults (None) the command is UNCHANGED so the
    validity path (run_p0.py) and existing callers are unaffected."""
    default = OpenAICodexAdapter(codex_bin="codex").build_command("gpt-5-codex", "/tmp/out.txt")
    assert "--sandbox" not in default and "-C" not in default   # backward-compatible default

    hardened = OpenAICodexAdapter(
        codex_bin="codex", cwd="/tmp", sandbox="read-only"
    ).build_command("gpt-5-codex", "/tmp/out.txt")
    assert hardened[hardened.index("--sandbox") + 1] == "read-only"
    assert hardened[hardened.index("-C") + 1] == "/tmp"


def test_codex_adapter_unavailable_raises(monkeypatch):
    monkeypatch.setattr("runner.adapters.shutil.which", lambda name: None)
    ad = OpenAICodexAdapter(codex_bin=None, runner=_fake_codex_runner("x"))
    assert ad.available() is False
    with pytest.raises(RuntimeError):
        ad.administer("d?", "gpt-5-codex", temperature=0.7, seed=1)


# --------------------------------------------------------------------------- OpenAI API / OpenRouter (mocked SDK)
# §3.5 cross-family judging: the roster's OpenAI models are API-only (the ChatGPT-subscription
# `codex exec` refuses them, per the 2026-07-09 smoke). A VALID run needs a clean single-turn
# OpenAI-compatible backend both as the OpenAI subject AND as the cross-family judge for the
# Anthropic subjects. OpenRouter speaks the same Chat Completions API through the OpenAI SDK, so a
# single OpenAIAPIAdapter (base_url + key env parameterized) covers OpenAI-direct and OpenRouter.
# F-1 / SA-5 retry+refusal semantics mirror AnthropicAdapter exactly.

def test_openai_api_adapter_administer_passes_params_and_reads_content():
    client = fx.make_fake_openai(text="Utilitarian: divert.")
    ad = OpenAIAPIAdapter(client=client)
    res = ad.administer("prompt?", "gpt-5-mini", temperature=0.7, seed=42, max_tokens=256)
    assert res.text == "Utilitarian: divert."
    assert res.refusal_flag is False
    assert res.latency >= 0.0
    kw = client.chat.completions.last_kwargs
    assert kw["model"] == "gpt-5-mini"
    assert kw["temperature"] == 0.7
    assert kw["max_tokens"] == 256
    # single-turn: one user message carrying the prompt; no system unless passed
    assert kw["messages"] == [{"role": "user", "content": "prompt?"}]


def test_openai_api_adapter_prepends_system_message_when_given():
    client = fx.make_fake_openai()
    ad = OpenAIAPIAdapter(client=client)
    ad.administer("dilemma?", "gpt-5-mini", temperature=0.7, seed=1, system="You are a judge.")
    msgs = client.chat.completions.last_kwargs["messages"]
    assert msgs[0] == {"role": "system", "content": "You are a judge."}
    assert msgs[1] == {"role": "user", "content": "dilemma?"}


def test_openai_api_adapter_omits_temperature_on_v4_drop():
    """F-2 / SA-6: omit_sampling_params=True removes `temperature` from the request entirely (wired
    for symmetry with the Anthropic V-4 drop; inert for OpenAI roster models that accept it)."""
    client = fx.make_fake_openai()
    ad = OpenAIAPIAdapter(client=client)
    ad.administer("p", "gpt-5-mini", temperature=0.7, seed=1, omit_sampling_params=True)
    assert "temperature" not in client.chat.completions.last_kwargs
    # default path still sends temperature
    client2 = fx.make_fake_openai()
    OpenAIAPIAdapter(client=client2).administer("p", "gpt-5-mini", temperature=0.7, seed=1)
    assert client2.chat.completions.last_kwargs["temperature"] == 0.7


def test_openai_api_adapter_refusal_flag_is_always_false_content_refusal_left_to_scorer():
    """F-1 / SA-5: Chat Completions has no universal STRUCTURED refusal signal, so refusal_flag is
    ALWAYS False. A content refusal ("I won't ...") is decided downstream by the scorer returning no
    stance (no_stance, WS-1 D10) — never by a substring match on the answer at the adapter."""
    client = fx.make_fake_openai(text="I won't answer that.")
    res = OpenAIAPIAdapter(client=client).administer("d?", "gpt-5-mini", temperature=0.7, seed=1)
    assert res.refusal_flag is False


def _openai_client_from_create(create):
    """Wrap a bare create(**kwargs) callable in the chat.completions.create client shape."""
    return SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create)))


def test_openai_api_adapter_bounded_retry_transient_then_succeeds():
    """F-1 / SA-5: a transient OpenAI error (rate-limit/5xx/connection/timeout), matched by class
    NAME so the suite needs no SDK, is bounded-retried with exponential backoff; recovery yields a
    normal scored result."""
    calls = {"n": 0}

    class RateLimitError(Exception):
        pass

    def create(**kwargs):
        calls["n"] += 1
        if calls["n"] < 3:
            raise RateLimitError("429 slow down")
        message = SimpleNamespace(role="assistant", content="Deontological: hold.")
        return SimpleNamespace(choices=[SimpleNamespace(message=message, finish_reason="stop")])

    ad = OpenAIAPIAdapter(client=_openai_client_from_create(create), max_retries=4, sleep=_no_sleep)
    res = ad.administer("p", "gpt-5-mini", temperature=0.7, seed=1)
    assert res.text == "Deontological: hold."
    assert res.refusal_flag is False
    assert calls["n"] == 3


def test_openai_api_adapter_persistent_transient_raises_admin_error():
    """F-1 / SA-5: persistent transient errors 'raise' fail-loud as an AdministrationError — never a
    silent refusal or a checkpointed cell."""

    class InternalServerError(Exception):
        pass

    def create(**kwargs):
        raise InternalServerError("500 upstream")

    ad = OpenAIAPIAdapter(client=_openai_client_from_create(create), max_retries=2, sleep=_no_sleep)
    with pytest.raises(AdministrationError):
        ad.administer("p", "gpt-5-mini", temperature=0.7, seed=1)


def test_openai_api_adapter_auth_error_is_not_retried():
    """F-1 / SA-5 addendum: an authentication error is NOT transient — it must propagate immediately,
    unretried (assert the call happened exactly once)."""

    class AuthenticationError(Exception):
        pass

    calls = {"n": 0}

    def create(**kwargs):
        calls["n"] += 1
        raise AuthenticationError("401 invalid key")

    ad = OpenAIAPIAdapter(client=_openai_client_from_create(create), max_retries=5, sleep=_no_sleep)
    with pytest.raises(AuthenticationError):
        ad.administer("p", "gpt-5-mini", temperature=0.7, seed=1)
    assert calls["n"] == 1  # no retry on a non-transient auth failure


def test_openai_api_adapter_bad_request_error_is_not_retried():
    """F-1 / SA-5: a bad-request (400, e.g. an unknown model id on OpenRouter) is not transient —
    it must propagate immediately, unretried, so the operator fixes the id instead of hammering."""

    class BadRequestError(Exception):
        pass

    calls = {"n": 0}

    def create(**kwargs):
        calls["n"] += 1
        raise BadRequestError("400 model not found")

    ad = OpenAIAPIAdapter(client=_openai_client_from_create(create), max_retries=5, sleep=_no_sleep)
    with pytest.raises(BadRequestError):
        ad.administer("p", "openai/does-not-exist", temperature=0.7, seed=1)
    assert calls["n"] == 1


def test_openai_api_adapter_injected_client_reports_injected_auth_mode():
    ad = OpenAIAPIAdapter(client=fx.make_fake_openai())
    assert ad.auth_mode == "injected"


def test_openai_api_adapter_constructs_openrouter_client_with_base_url_and_key(monkeypatch):
    """OpenRouter wiring: with no client injected, the adapter must defer-import openai and
    construct openai.OpenAI(base_url=<openrouter>, api_key=<OPENROUTER_API_KEY>) — proving the same
    Chat Completions adapter targets OpenRouter by base_url + key env, no code fork. The key is NOT
    hard-required by our code; it is read from the configured env var and handed to the SDK."""
    import sys

    captured = {}

    class _FakeOpenAI:
        def __init__(self, *a, **k):
            captured.update(k)

    monkeypatch.setitem(sys.modules, "openai", SimpleNamespace(OpenAI=_FakeOpenAI))
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or-test")

    ad = OpenAIAPIAdapter(base_url="https://openrouter.ai/api/v1", api_key_env="OPENROUTER_API_KEY")
    _ = ad.client  # lazy construction
    assert captured["base_url"] == "https://openrouter.ai/api/v1"
    assert captured["api_key"] == "sk-or-test"
    assert ad.auth_mode == "api_key"


# --------------------------------------------------------------------------- Gemini (deferred)

def test_gemini_adapter_not_implemented():
    ad = GeminiAdapter()
    with pytest.raises(NotImplementedError):
        ad.administer("p", "gemini-2.5-pro", temperature=0.7, seed=1)


# --------------------------------------------------------------------------- factory

def test_build_adapter_factory():
    assert isinstance(build_adapter("anthropic"), AnthropicAdapter)
    # DEFAULT FLIPPED (was OpenAICodexAdapter): the OpenAI vendor now builds the clean Chat
    # Completions API adapter — the VALID-run backend — not the smoke-only `codex exec` wrapper.
    assert isinstance(build_adapter("openai"), OpenAIAPIAdapter)
    assert isinstance(build_adapter("google"), GeminiAdapter)
    with pytest.raises(ValueError):
        build_adapter("mistral")


def test_build_adapter_openai_backend_selector():
    """The smoke codex path stays reachable via backend='codex' (NOT deleted); backend='openrouter'
    presets the base_url + OPENROUTER_API_KEY env by construction; default/'api' = OpenAI-direct."""
    assert isinstance(build_adapter("openai", backend="api"), OpenAIAPIAdapter)
    assert isinstance(build_adapter("openai", backend="codex"), OpenAICodexAdapter)
    orouter = build_adapter("openai", backend="openrouter")
    assert isinstance(orouter, OpenAIAPIAdapter)
    assert orouter._base_url == "https://openrouter.ai/api/v1"
    assert orouter._api_key_env == "OPENROUTER_API_KEY"
    with pytest.raises(ValueError):
        build_adapter("openai", backend="bogus")
