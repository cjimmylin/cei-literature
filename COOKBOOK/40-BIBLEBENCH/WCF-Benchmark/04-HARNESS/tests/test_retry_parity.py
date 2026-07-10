"""Probe-path retry parity + rep-level cause taxonomy — memo R34–R37 (BINDING, session 12).

R35.1: every acceptance-probe judge-call routes through the SAME retry semantics as the
production award path (``complete_with_retry``), which R35 widens to retry ONCE on
``finish_reason in {'length','error'}`` OR a short/empty emission — but NEVER on a genuine
(non-empty) refusal. A rep still bad after the retry is a FAILED rep with a recorded cause
``pass | fail_substantive | fail_format | fail_transport_after_retry`` (R35.3); a transport
loss is never an error silently dropped from the denominator (the gap that turned gemini's
3 transport errors into spurious qualification fails in the session-12 sweep).

Judges are canned fakes on the ``.complete`` seam; NO network.
"""

from __future__ import annotations

import os
import sys

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)

from wcfbench.judge import complete_with_retry  # noqa: E402


class _SeqJudge:
    """Returns a scripted (text, finish_reason) per call, exposing ``last_finish_reason``."""

    def __init__(self, seq):
        self.seq = list(seq)
        self.calls = 0
        self.last_finish_reason = None

    def complete(self, prompt, item_id=None):
        text, fr = self.seq[min(self.calls, len(self.seq) - 1)]
        self.calls += 1
        self.last_finish_reason = fr
        return text


_COMPLETE = "KP1: award — ok\nKP2: deny — no"


def _is_complete(t):
    from wcfbench.judge import award_emission_count
    return award_emission_count(t) >= 2


# --- transport (error finish_reason) is retried, then recovers ---------------

def test_error_finish_reason_is_retried_then_recovers():
    j = _SeqJudge([("", "error"), (_COMPLETE, "stop")])
    call = complete_with_retry(j, "p", is_complete=_is_complete)
    assert j.calls == 2                # retried exactly once
    assert call.retried is True
    assert call.discarded is False     # recovered
    assert call.text == _COMPLETE


def test_error_finish_reason_still_bad_is_discarded():
    j = _SeqJudge([("", "error"), ("", "error")])
    call = complete_with_retry(j, "p", is_complete=_is_complete)
    assert j.calls == 2                # one retry, no more
    assert call.discarded is True      # transport loss surfaced, NOT dropped from the denominator


# --- empty/silent emission is retried (it is transport, not a refusal) -------

def test_empty_emission_is_retried_then_recovers():
    j = _SeqJudge([("", "stop"), (_COMPLETE, "stop")])
    call = complete_with_retry(j, "p", is_complete=_is_complete)
    assert j.calls == 2
    assert call.retried is True
    assert call.discarded is False


# --- a genuine (non-empty) refusal is NOT retried ----------------------------

def test_nonempty_refusal_is_not_retried():
    j = _SeqJudge([("I can't grade this.", "stop"), (_COMPLETE, "stop")])
    call = complete_with_retry(j, "p", is_complete=_is_complete)
    assert j.calls == 1                # NOT retried — a refusal is a terminal state
    assert call.retried is False
    assert call.discarded is False     # not a transport loss; the caller surfaces the refusal


# --- length truncation still retried (R33.3 preserved) -----------------------

def test_length_truncation_still_retried():
    j = _SeqJudge([("KP1: award — ok", "length"), (_COMPLETE, "stop")])
    call = complete_with_retry(j, "p", is_complete=_is_complete)
    assert j.calls == 2
    assert call.retried is True
    assert call.discarded is False
