"""R40.3 / R39(e)(4) — settled-core keypoint TIE → UNGRADED, never a silent False.

The `AGG-C8` aggregate 0.0 was PARTLY mechanical: grok's JSONDecodeError drop left an even
2-judge settled-core panel, and the old rule ``sum(votes) > len(votes)/2`` resolved a 1–1
tie to **False** (a floor break). R39(e)(4) ABOLISHES tie→False for settled-core keypoints:
an even eligible-judge split is UNGRADED (``None``) + an escalation flag in the aggregate
detail — never a silent False. Odd-panel majorities are UNCHANGED.

Tests drive :meth:`JudgePanel._aggregate_contested` directly with hand-built
``ContestedScore`` objects (no network, no judge calls) — the aggregation rule is the unit
under test.
"""

from __future__ import annotations

import os
import sys

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)

from wcfbench.judge_panel import JudgePanel, SETTLED_CORE  # noqa: E402
from wcfbench.contested import ContestedScore  # noqa: E402

KP1 = "no collapse to 'both equal'; profiles differentiated"
KP2 = "Q152 floor on both"


def _core_score(**core):
    """A ContestedScore carrying only settled-core keypoints."""
    s = ContestedScore()
    s.settled_core = dict(core)
    return s


def _agg(*scores):
    """Aggregate a list of (ContestedScore) all eligible for SETTLED_CORE."""
    return JudgePanel._aggregate_contested([(s, {SETTLED_CORE}) for s in scores])


# ---------------------------------------------------------------------------
# 1–1 tie (even 2-judge panel — the exact grok-dropped AGG-C8 shape).
# ---------------------------------------------------------------------------

def test_1_1_tie_is_ungraded_not_false():
    agg = _agg(
        _core_score(**{KP1: True, KP2: True}),   # gpt: both correct
        _core_score(**{KP1: False, KP2: True}),  # gemini: kp1 wrong, kp2 correct
    )
    # KP2 unanimous True -> True. KP1 is a 1-1 tie -> UNGRADED (None), NOT False.
    assert agg.settled_core[KP2] is True
    assert agg.settled_core.get(KP1) is None
    assert "escalate" in agg.detail.get("settled_core_escalation", "").lower()
    assert KP1 in agg.detail.get("settled_core_escalation", "")


def test_1_1_tie_does_not_count_as_floor_break_in_fraction():
    # settled_core_fraction must treat an UNGRADED (None) keypoint as NOT a False —
    # a tie is not a credited-zero. A single unanimous-True kp with one tied kp -> 1.0.
    agg = _agg(
        _core_score(**{KP1: True, KP2: True}),
        _core_score(**{KP1: False, KP2: True}),
    )
    # fraction over GRADED keypoints only (None excluded); KP2 True of 1 graded -> 1.0.
    assert agg.settled_core_fraction == 1.0


# ---------------------------------------------------------------------------
# 2–2 tie (even 4-judge panel).
# ---------------------------------------------------------------------------

def test_2_2_tie_is_ungraded_not_false():
    agg = _agg(
        _core_score(**{KP1: True}),
        _core_score(**{KP1: True}),
        _core_score(**{KP1: False}),
        _core_score(**{KP1: False}),
    )
    assert agg.settled_core.get(KP1) is None
    assert "escalate" in agg.detail.get("settled_core_escalation", "").lower()


# ---------------------------------------------------------------------------
# Odd-panel majority is UNCHANGED (2-1 True -> True; 1-2 True -> False, credit-when-earned).
# ---------------------------------------------------------------------------

def test_odd_panel_majority_true_unchanged():
    agg = _agg(
        _core_score(**{KP1: True}),
        _core_score(**{KP1: True}),
        _core_score(**{KP1: False}),
    )
    assert agg.settled_core[KP1] is True           # 2-1 majority correct


def test_odd_panel_majority_false_is_real_floor_miss():
    # 1-2: a genuine majority-wrong keypoint is a REAL False (R39(e)(3) credit-when-earned),
    # not softened to None — the floor's validity is that reported misses are real.
    agg = _agg(
        _core_score(**{KP1: True}),
        _core_score(**{KP1: False}),
        _core_score(**{KP1: False}),
    )
    assert agg.settled_core[KP1] is False
    assert "escalate" not in agg.detail.get("settled_core_escalation", "").lower()


def test_unanimous_no_escalation_flag():
    agg = _agg(
        _core_score(**{KP1: True, KP2: True}),
        _core_score(**{KP1: True, KP2: True}),
    )
    assert agg.settled_core[KP1] is True and agg.settled_core[KP2] is True
    assert agg.detail.get("settled_core_escalation", "") == ""
