"""R40.2 — the judge-panel scoring-call retry seam (memo R38–R41, session 14).

The grok `AGG-C8` drop that produced the settled-core floor divergence was a downstream
**JSONDecodeError** raised inside the OpenRouter client (a malformed HTTP response body) —
a transport-class event the `complete_with_retry` finish_reason/empty seam does NOT catch,
because it surfaces as an *exception* out of the whole scoring function, not a bad text.

R40.2: a judge scoring call that raises a retryable transport error —
  (i) a `JSONDecodeError` / unparseable-verdict error, or
  (ii) an OpenRouter HTTP 402 / 403 / 429 transport error —
is retried ONCE with a short backoff; a post-retry failure is recorded as
``fail_transport_after_retry`` in the ``judges_discarded`` record — NEVER a silent drop.
A NON-transport exception (a programming bug, a 500) keeps the existing single-attempt
``call error`` survival (one judge dropped, panel survives) — it is not a transport retry.

Judges are canned fakes on the ``.complete`` seam; NO network. Backoff is monkeypatched to
zero so the suite stays fast.
"""

from __future__ import annotations

import json
import os
import sys

import pytest

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)

from wcfbench import judge_panel as jp  # noqa: E402
from wcfbench.judge_panel import (  # noqa: E402
    JudgePanel,
    is_retryable_transport_error,
)
from wcfbench.openrouter_client import OpenRouterError  # noqa: E402

from test_judge_panel import FakeJudgeClient, _open_item, _contested_item  # noqa: E402


@pytest.fixture(autouse=True)
def _no_backoff(monkeypatch):
    """Zero the retry backoff so the suite stays fast; assert it is actually called."""
    calls = {"n": 0}

    def _fake_sleep(_secs):
        calls["n"] += 1

    monkeypatch.setattr(jp.time, "sleep", _fake_sleep)
    return calls


# ---------------------------------------------------------------------------
# The transport-error classifier (unit).
# ---------------------------------------------------------------------------

def test_jsondecodeerror_is_retryable():
    err = json.JSONDecodeError("Expecting value", "not json", 0)
    assert is_retryable_transport_error(err) is True


def test_http_402_403_429_are_retryable():
    for code in (402, 403, 429):
        err = OpenRouterError(f"OpenRouter HTTP {code} (Forbidden) for model 'x': Key limit")
        assert is_retryable_transport_error(err) is True, code


def test_malformed_response_openrouter_error_is_retryable():
    # the client raises OpenRouterError on an unparseable/malformed reply body.
    err = OpenRouterError("malformed OpenRouter response for 'x-ai/grok-4.20': {...}")
    assert is_retryable_transport_error(err) is True


def test_generic_500_and_valueerror_are_not_transport_retryable():
    assert is_retryable_transport_error(OpenRouterError("OpenRouter HTTP 500 (Server Error)")) is False
    assert is_retryable_transport_error(ValueError("a real bug")) is False
    assert is_retryable_transport_error(RuntimeError("simulated judge upstream 500")) is False


# ---------------------------------------------------------------------------
# A client that raises a scripted exception on the first N calls, then succeeds.
# ---------------------------------------------------------------------------

class _FlakyJudge(FakeJudgeClient):
    """Wraps FakeJudgeClient: after ``arm()``, raises ``exc`` on the first ``fail_attempts``
    scoring ATTEMPTS, then delegates to the normal FakeJudgeClient path (a valid grade).

    A scoring call (``score_contested_position`` / ``score_triaxial``) issues its FIRST
    ``.complete`` (disclosure / matter axis) at the top; a transport failure raises there and
    aborts the whole attempt, and the retry wrapper re-enters from the top. So a failing
    attempt is exactly "raise on the first ``.complete`` of the attempt". We count an attempt
    each time a ``.complete`` follows a prior raise (or the arm), and fail while
    ``attempt <= fail_attempts``. ``arm()`` excludes construction-time calibration probes.

    ``fail_attempts=1`` → first attempt raises, retry succeeds (recovers).
    ``fail_attempts=99`` → both attempts raise (post-retry transport loss)."""

    def __init__(self, *, exc, fail_attempts=1, **kw):
        super().__init__(**kw)
        self._exc = exc
        self._fail_attempts = fail_attempts
        self._armed = False
        self._attempt = 0
        self._prev_raised = True   # the next .complete starts a fresh attempt

    def arm(self):
        self._armed = True
        return self

    def complete(self, prompt, item_id=None):
        if not self._armed:
            return super().complete(prompt, item_id=item_id)   # calibration phase — never fails
        if self._prev_raised:
            self._attempt += 1
            self._prev_raised = False
        if self._attempt <= self._fail_attempts:
            self._prev_raised = True                            # this attempt aborts here
            raise self._exc
        return super().complete(prompt, item_id=item_id)


def _grok_jsondecode():
    return json.JSONDecodeError("Expecting value", "", 0)


# ---------------------------------------------------------------------------
# CONTESTED path — the grok AGG-C8 signature.
# ---------------------------------------------------------------------------

def test_contested_transport_error_is_retried_then_recovers(_no_backoff):
    # First scoring call raises a JSONDecodeError; the retry succeeds -> judge NOT dropped.
    flaky = _FlakyJudge(exc=_grok_jsondecode(), fail_attempts=1)
    panel = JudgePanel([
        {"name": "gpt", "family": "openai", "client": FakeJudgeClient()},
        {"name": "grok", "family": "x-ai", "client": flaky},
    ])
    flaky.arm()
    v = panel.score_contested(_contested_item(), "a disclosed, coherent answer")
    assert len(v.per_judge) == 2                         # grok recovered on retry
    assert {"gpt", "grok"} == {j["name"] for j in v.per_judge}
    assert panel.discarded == []                         # no discard on a recovered retry
    assert _no_backoff["n"] == 1                          # exactly one backoff slept


def test_contested_transport_error_post_retry_records_fail_transport(_no_backoff):
    # Both attempts raise -> judge dropped, recorded as fail_transport_after_retry (NOT silent).
    flaky = _FlakyJudge(exc=_grok_jsondecode(), fail_attempts=99)
    panel = JudgePanel([
        {"name": "gpt", "family": "openai", "client": FakeJudgeClient()},
        {"name": "gemini", "family": "google", "client": FakeJudgeClient()},
        {"name": "grok", "family": "x-ai", "client": flaky},
    ], k=3)
    flaky.arm()
    v = panel.score_contested(_contested_item(), "response")
    assert "grok" not in {j["name"] for j in v.per_judge}
    hits = [(n, r) for n, r in panel.discarded if n == "grok"]
    assert len(hits) == 1
    assert "fail_transport_after_retry" in hits[0][1]
    assert _no_backoff["n"] == 1


def test_contested_http_403_is_retried(_no_backoff):
    flaky = _FlakyJudge(exc=OpenRouterError("OpenRouter HTTP 403 (Forbidden): Key limit"),
                        fail_attempts=1)
    panel = JudgePanel([
        {"name": "gpt", "family": "openai", "client": FakeJudgeClient()},
        {"name": "grok", "family": "x-ai", "client": flaky},
    ])
    flaky.arm()
    v = panel.score_contested(_contested_item(), "response")
    assert len(v.per_judge) == 2
    assert _no_backoff["n"] == 1


# ---------------------------------------------------------------------------
# OPEN path — same seam.
# ---------------------------------------------------------------------------

def test_open_transport_error_is_retried_then_recovers(_no_backoff):
    flaky = _FlakyJudge(exc=_grok_jsondecode(), fail_attempts=1)
    panel = JudgePanel([
        {"name": "gpt", "family": "openai", "client": FakeJudgeClient()},
        {"name": "grok", "family": "x-ai", "client": flaky},
    ])
    flaky.arm()
    v = panel.score_open(_open_item(), "a courteous, substantive refusal")
    assert len(v.per_judge) == 2
    assert _no_backoff["n"] == 1


def test_open_transport_error_post_retry_records_fail_transport(_no_backoff):
    flaky = _FlakyJudge(exc=_grok_jsondecode(), fail_attempts=99)
    panel = JudgePanel([
        {"name": "gpt", "family": "openai", "client": FakeJudgeClient()},
        {"name": "gemini", "family": "google", "client": FakeJudgeClient()},
        {"name": "grok", "family": "x-ai", "client": flaky},
    ], k=3)
    flaky.arm()
    v = panel.score_open(_open_item(), "response")
    assert "grok" not in {j["name"] for j in v.per_judge}
    hits = [(n, r) for n, r in panel.discarded if n == "grok"]
    assert len(hits) == 1 and "fail_transport_after_retry" in hits[0][1]


# ---------------------------------------------------------------------------
# A NON-transport exception keeps the existing single-attempt survival (no retry).
# ---------------------------------------------------------------------------

def test_non_transport_error_is_not_retried(_no_backoff):
    # RuntimeError("...500") is NOT a retryable transport class -> single attempt, dropped
    # with the legacy "call error" reason, no backoff slept.
    panel = JudgePanel([
        {"name": "gpt", "family": "openai", "client": FakeJudgeClient()},
        {"name": "gemini", "family": "google", "client": FakeJudgeClient(raise_on="CATEGORY:")},
    ])
    v = panel.score_open(_open_item(), "response")
    assert len(v.per_judge) == 1
    assert v.per_judge[0]["family"] == "openai"
    assert any(n == "gemini" and "call error" in r for n, r in panel.discarded)
    assert _no_backoff["n"] == 0                          # never slept — not a transport retry
