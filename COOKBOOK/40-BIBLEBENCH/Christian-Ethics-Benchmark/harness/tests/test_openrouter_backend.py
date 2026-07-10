"""Seam tests for the OpenRouter model backend. NO live HTTP — the transport is
injected and returns RECORDED responses. We test OUR payload construction, response
parsing, family routing, key loading/redaction, and retry/backoff logic.
"""
import json

import pytest

from walkworthy.clients import Message, ModelResponse
from walkworthy.cli_backends import ModelCallError
from walkworthy import openrouter_backend as orb


# --------------------------------------------------------------------------- #
# recorded-transport fakes
# --------------------------------------------------------------------------- #
def make_transport(*responses):
    """Each response is (status, data_dict). Records calls; cycles last if exhausted."""
    calls = []
    seq = list(responses)

    def transport(url, headers, payload, timeout=None):
        calls.append({"url": url, "headers": headers, "payload": payload})
        return seq.pop(0) if len(seq) > 1 else seq[0]

    transport.calls = calls
    return transport


def ok(content="hi", model="x/y", usage=None):
    return (200, {"choices": [{"message": {"content": content}}],
                  "model": model, "usage": usage or {"total_tokens": 5}})


NOSLEEP = lambda *_a, **_k: None


# --------------------------------------------------------------------------- #
# family routing
# --------------------------------------------------------------------------- #
def test_family_from_slug():
    assert orb.family_from_slug("anthropic/claude-sonnet-5") == "anthropic"
    assert orb.family_from_slug("openai/gpt-5.6-terra") == "openai"
    assert orb.family_from_slug("google/gemini-3.5-flash") == "google"
    assert orb.family_from_slug("meta-llama/llama-3.3-70b-instruct") == "meta-llama"


# --------------------------------------------------------------------------- #
# key loading + redaction
# --------------------------------------------------------------------------- #
def test_load_key_prefers_env(monkeypatch, tmp_path):
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or-fromenv")
    f = tmp_path / "k.env"; f.write_text("sk-or-fromfile")
    assert orb.load_openrouter_key(str(f)) == "sk-or-fromenv"


def test_load_key_from_raw_token_file(monkeypatch, tmp_path):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    f = tmp_path / "k.env"; f.write_text("sk-or-rawtoken\n")
    assert orb.load_openrouter_key(str(f)) == "sk-or-rawtoken"


def test_load_key_from_keyvalue_file(monkeypatch, tmp_path):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    f = tmp_path / "k.env"; f.write_text("export OPENROUTER_API_KEY=sk-or-kv\n")
    assert orb.load_openrouter_key(str(f)) == "sk-or-kv"


def test_response_raw_never_contains_the_key():
    c = orb.OpenRouterClient("sut", model="meta-llama/llama-3.3-70b-instruct",
                             api_key="sk-or-SECRET", transport=make_transport(ok()),
                             sleep=NOSLEEP)
    resp = c.complete([Message("user", "hi")])
    assert "sk-or-SECRET" not in json.dumps(resp.raw)


# --------------------------------------------------------------------------- #
# payload construction
# --------------------------------------------------------------------------- #
def test_payload_maps_system_then_messages_in_order():
    t = make_transport(ok())
    c = orb.OpenRouterClient("j", model="openai/gpt-5.6-terra", api_key="k",
                             transport=t, sleep=NOSLEEP)
    c.complete([Message("user", "u1"), Message("assistant", "a1"), Message("user", "u2")],
               system="SYS")
    msgs = t.calls[0]["payload"]["messages"]
    assert [m["role"] for m in msgs] == ["system", "user", "assistant", "user"]
    assert msgs[0]["content"] == "SYS"
    assert msgs[-1]["content"] == "u2"


def test_payload_has_model_and_no_sampling_params():
    t = make_transport(ok())
    c = orb.OpenRouterClient("j", model="anthropic/claude-sonnet-5", api_key="k",
                             transport=t, sleep=NOSLEEP)
    c.complete([Message("user", "hi")])
    payload = t.calls[0]["payload"]
    assert payload["model"] == "anthropic/claude-sonnet-5"
    for banned in ("temperature", "top_p", "top_k"):
        assert banned not in payload


def test_auth_header_carries_bearer_key():
    t = make_transport(ok())
    c = orb.OpenRouterClient("j", model="openai/gpt-5.6-terra", api_key="k123",
                             transport=t, sleep=NOSLEEP)
    c.complete([Message("user", "hi")])
    assert t.calls[0]["headers"]["Authorization"] == "Bearer k123"


# --------------------------------------------------------------------------- #
# response parsing
# --------------------------------------------------------------------------- #
def test_complete_returns_content_family_and_usage():
    t = make_transport(ok(content="the answer", model="meta-llama/llama-3.3-70b-instruct",
                          usage={"total_tokens": 42}))
    c = orb.OpenRouterClient("sut", model="meta-llama/llama-3.3-70b-instruct",
                             api_key="k", transport=t, sleep=NOSLEEP)
    resp = c.complete([Message("user", "hi")])
    assert isinstance(resp, ModelResponse)
    assert resp.text == "the answer"
    assert resp.family == "meta-llama"
    assert resp.usage.get("total_tokens") == 42


def test_empty_content_raises():
    t = make_transport((200, {"choices": [{"message": {"content": ""}}], "model": "x/y"}))
    c = orb.OpenRouterClient("sut", model="x/y", api_key="k", transport=t, sleep=NOSLEEP)
    with pytest.raises(ModelCallError):
        c.complete([Message("user", "hi")])


def test_content_as_parts_list_is_joined():
    t = make_transport((200, {"choices": [{"message": {"content":
        [{"type": "text", "text": "part1 "}, {"type": "text", "text": "part2"}]}}],
        "model": "x/y"}))
    c = orb.OpenRouterClient("sut", model="x/y", api_key="k", transport=t, sleep=NOSLEEP)
    assert c.complete([Message("user", "hi")]).text == "part1 part2"


# --------------------------------------------------------------------------- #
# retry / backoff
# --------------------------------------------------------------------------- #
def test_retries_on_429_then_succeeds():
    t = make_transport((429, {"error": "rate"}), ok(content="recovered"))
    c = orb.OpenRouterClient("sut", model="x/y", api_key="k", transport=t,
                             sleep=NOSLEEP, max_retries=3)
    resp = c.complete([Message("user", "hi")])
    assert resp.text == "recovered"
    assert len(t.calls) == 2


def test_retries_exhausted_on_5xx_raises():
    t = make_transport((503, {"error": "unavailable"}))
    c = orb.OpenRouterClient("sut", model="x/y", api_key="k", transport=t,
                             sleep=NOSLEEP, max_retries=2)
    with pytest.raises(ModelCallError):
        c.complete([Message("user", "hi")])
    assert len(t.calls) == 3   # initial + 2 retries


def test_400_raises_immediately_without_retry():
    t = make_transport((400, {"error": "bad request"}))
    c = orb.OpenRouterClient("sut", model="x/y", api_key="k", transport=t,
                             sleep=NOSLEEP, max_retries=3)
    with pytest.raises(ModelCallError):
        c.complete([Message("user", "hi")])
    assert len(t.calls) == 1   # no retry on a 4xx client error


# --------------------------------------------------------------------------- #
# PR-5 (a): empty-200 retry (capped exponential, N attempts) — the qwen F-2 lesson
# --------------------------------------------------------------------------- #
def _empty():
    return (200, {"choices": [{"message": {"content": ""}}], "model": "x/y"})


def test_empty_200_retries_then_recovers():
    t = make_transport(_empty(), _empty(), ok(content="recovered"))
    c = orb.OpenRouterClient("sut", model="x/y", api_key="k", transport=t,
                             sleep=NOSLEEP, empty_retries=3)
    assert c.complete([Message("user", "hi")]).text == "recovered"
    assert len(t.calls) == 3


def test_empty_200_exhausted_raises_after_n_attempts():
    t = make_transport(_empty())   # cycles empty forever
    c = orb.OpenRouterClient("sut", model="x/y", api_key="k", transport=t,
                             sleep=NOSLEEP, empty_retries=3)
    with pytest.raises(ModelCallError):
        c.complete([Message("user", "hi")])
    assert len(t.calls) == 4       # initial + 3 empty retries


# --------------------------------------------------------------------------- #
# PR-5 (b): OpenRouter provider preferences + fallback routing
# --------------------------------------------------------------------------- #
def test_provider_prefs_sent_in_payload():
    t = make_transport(ok())
    prefs = {"allow_fallbacks": True, "sort": "throughput"}
    c = orb.OpenRouterClient("sut", model="x/y", api_key="k", transport=t,
                             sleep=NOSLEEP, provider_prefs=prefs)
    c.complete([Message("user", "hi")])
    assert t.calls[0]["payload"]["provider"] == prefs


def test_default_allows_provider_fallbacks():
    t = make_transport(ok())
    c = orb.OpenRouterClient("sut", model="x/y", api_key="k", transport=t, sleep=NOSLEEP)
    c.complete([Message("user", "hi")])
    assert t.calls[0]["payload"]["provider"]["allow_fallbacks"] is True
