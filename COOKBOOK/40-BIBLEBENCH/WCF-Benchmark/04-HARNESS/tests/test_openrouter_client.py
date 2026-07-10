"""OpenRouterModelClient tests — the real cross-family backend behind the seam.

Run:
    /Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest \
        COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/04-HARNESS/tests/ -q

OpenRouter is an OpenAI-compatible Chat Completions endpoint that fronts many
model families behind ONE key — the natural substrate for the spine's
≥2-cross-family-judge / ≥3-frontier-family requirements. This client implements
the same `.complete(prompt, item_id=None) -> str` seam the scorers call.

Every test here MOCKS `urllib.request.urlopen` — NO real network call is made.
"""

from __future__ import annotations

import io
import json
import os
import sys
import urllib.error
import urllib.request

import pytest

HARNESS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS_ROOT not in sys.path:
    sys.path.insert(0, HARNESS_ROOT)

from wcfbench.openrouter_client import OpenRouterModelClient, OpenRouterError  # noqa: E402


class _FakeResp:
    def __init__(self, payload):
        self._b = json.dumps(payload).encode()

    def read(self):
        return self._b

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def _canned(content="hello", usage=None, model="test/model"):
    return {
        "id": "gen-x",
        "model": model,
        "choices": [{"message": {"role": "assistant", "content": content}}],
        "usage": usage or {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15},
    }


def _patch_urlopen(monkeypatch, payload, capture=None):
    def fake_urlopen(req, timeout=None):
        if capture is not None:
            capture["req"] = req
            capture["body"] = json.loads(req.data.decode())
            capture["headers"] = dict(req.header_items())
        return _FakeResp(payload)
    monkeypatch.setattr(urllib.request, "urlopen", fake_urlopen)


def test_complete_returns_assistant_content(monkeypatch):
    _patch_urlopen(monkeypatch, _canned("the answer"))
    c = OpenRouterModelClient(model="openai/gpt-4o-mini", api_key="sk-or-test")
    assert c.complete("what is 2+2?", item_id="X1") == "the answer"


def test_payload_carries_model_prompt_and_sampling(monkeypatch):
    cap = {}
    _patch_urlopen(monkeypatch, _canned(), capture=cap)
    c = OpenRouterModelClient(model="anthropic/claude-3.5-haiku", api_key="sk-or-test",
                              temperature=0.0, max_tokens=256)
    c.complete("rank these", item_id="X2")
    assert cap["body"]["model"] == "anthropic/claude-3.5-haiku"
    assert cap["body"]["temperature"] == 0.0
    assert cap["body"]["max_tokens"] == 256
    # the user prompt is the last message
    assert cap["body"]["messages"][-1] == {"role": "user", "content": "rank these"}
    # bearer auth header present
    assert any(k.lower() == "authorization" and v == "Bearer sk-or-test" for k, v in cap["headers"].items())


def test_system_prompt_included_when_set(monkeypatch):
    cap = {}
    _patch_urlopen(monkeypatch, _canned(), capture=cap)
    c = OpenRouterModelClient(model="m", api_key="sk-or-test", system="You are a Westminster examinee.")
    c.complete("q")
    assert cap["body"]["messages"][0] == {"role": "system", "content": "You are a Westminster examinee."}


def test_missing_api_key_fails_loud(monkeypatch):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(OpenRouterError):
        OpenRouterModelClient(model="m")   # no key anywhere


def test_api_key_read_from_env(monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or-env")
    _patch_urlopen(monkeypatch, _canned("ok"))
    c = OpenRouterModelClient(model="m")   # picks up env key
    assert c.complete("q") == "ok"


def test_http_error_is_wrapped(monkeypatch):
    def raise_http(req, timeout=None):
        raise urllib.error.HTTPError(url="u", code=429, msg="Too Many Requests",
                                     hdrs=None, fp=io.BytesIO(b'{"error":"rate limited"}'))
    monkeypatch.setattr(urllib.request, "urlopen", raise_http)
    c = OpenRouterModelClient(model="m", api_key="sk-or-test")
    with pytest.raises(OpenRouterError) as ei:
        c.complete("q")
    assert "429" in str(ei.value)


def test_malformed_response_fails_loud(monkeypatch):
    _patch_urlopen(monkeypatch, {"id": "x", "choices": []})   # no message
    c = OpenRouterModelClient(model="m", api_key="sk-or-test")
    with pytest.raises(OpenRouterError):
        c.complete("q")


def test_usage_is_logged(monkeypatch):
    _patch_urlopen(monkeypatch, _canned(usage={"prompt_tokens": 100, "completion_tokens": 20, "total_tokens": 120}))
    c = OpenRouterModelClient(model="m", api_key="sk-or-test")
    c.complete("q", item_id="ITEM-9")
    assert c.call_count == 1
    assert c.usage_log[-1]["usage"]["total_tokens"] == 120
    assert c.usage_log[-1]["item_id"] == "ITEM-9"
    assert c.total_tokens == 120
