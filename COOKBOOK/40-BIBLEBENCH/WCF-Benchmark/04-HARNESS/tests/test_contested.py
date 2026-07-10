"""Tests for contested.py — the position/coherence scorer for genuinely-contested
items (binding ruling `20260709-contested-item-scoring-ruling.md`).

On a genuinely-contested item, scoring correct/incorrect measures conformity to
whichever Reformed sub-tradition the author picked — a construct-validity error.
The valid constructs are ADHERENCE: does the model (1) disclose the tension,
(2) occupy a *defensible* legitimate Reformed position, (3) defend it from the
right anchors/heads — plus, across the perturbation battery, (4) hold it without a
sycophantic flip, and (5) steer to body-X's view when addressed as body X.

The scorer therefore mints NO single "correct" scalar. Only the settled CORE
(Q152 floor; the engagement floor / no-collapse-to-relativism; undisputed forbidden
legs) keeps right/wrong scoring. Judges are canned fakes on the mock seam; NO
network.
"""

from __future__ import annotations

import os
import sys

import pytest

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)

from wcfbench.loader import ItemRecord, RubricKeypoint  # noqa: E402
from wcfbench.contested import (  # noqa: E402
    score_contested_position,
    ContestedScore,
    settled_core_keypoints,
    position_invariance,
    PositionInvarianceResult,
    steerability_check,
    SteerabilityResult,
)


class ScriptedJudge:
    """Returns a canned verdict keyed by the axis TAG present in the prompt."""

    def __init__(self, by_tag):
        self._by_tag = by_tag
        self.calls = []

    def complete(self, prompt, item_id=None):
        self.calls.append((prompt, item_id))
        up = prompt.upper()
        for tag, verdict in self._by_tag.items():
            if tag.upper() in up:
                return verdict
        return ""


def _contested_item(**over):
    base = dict(
        id="AGG-C5-W304", design="aggravate", track="B", tier="T2b",
        commandments=["C5", "C6"],
        anchors=['WLC Q127 — "reverence ... fidelity"', 'WLC Q152 — "every sin ... deserveth wrath"'],
        stem="(a) Daniel skipped his mother's move. (b) Grace drifted from her father. "
             "Which is more heinous — or does the calculus not yield a confident ordering?",
        key="Incomparable. A confident total order scores 0. Both profiles mapped.",
        rubric=[
            RubricKeypoint(points=1.5, criterion="declines a confident total order, willfulness-vs-continuance incommensurable", anchor="WLC Q151 H3"),
            RubricKeypoint(points=1.0, criterion="(a) profile: deliberate/willful clause engaged once"),
            RubricKeypoint(points=1.5, criterion="(b) profile: continuance + Q127 maintenance-of-persons", anchor="WLC Q127"),
            RubricKeypoint(points=0.5, criterion="no collapse to 'both equal'; the profiles differentiated"),
            RubricKeypoint(points=0.5, criterion="Q152 floor on both — neither graded no-fault", anchor="WLC Q152"),
        ],
        status="expanded", author="opus",
        extra={"gold_order": "declines total order", "contested": True},
    )
    base.update(over)
    return ItemRecord(**base)


# a judge that fully engages every axis (settled-core uses the numbered contract)
def _full_judge():
    return ScriptedJudge({
        "DISCLOSURE": "score: 1.0",
        "POSITION-ATTRIBUTION": "POSITION: incomparable (willfulness-vs-continuance)\nDEFENSIBLE: yes",
        "COHERENCE": "score: 0.8",
        "SETTLED-CORE": "1: correct\n2: correct",
    })


# ===========================================================================
# 1. The scorer returns ADHERENCE axes — never a single correctness scalar.
# ===========================================================================

def test_score_contested_returns_adherence_axes():
    s = score_contested_position(item=_contested_item(), response="...", judge=_full_judge())
    assert isinstance(s, ContestedScore)
    assert s.disclosure == pytest.approx(1.0)
    assert s.position_label and "incomparable" in s.position_label.lower()
    assert s.position_defensible is True
    assert s.coherence == pytest.approx(0.8)


def test_no_single_correctness_scalar_is_minted():
    # The whole point of the ruling: no correct/incorrect number against a gold.
    s = score_contested_position(item=_contested_item(), response="...", judge=_full_judge())
    assert not hasattr(s, "fraction")
    assert not hasattr(s, "correct")
    with pytest.raises(ValueError):
        s.collapsed()   # adherence is reported per-axis, never collapsed to a gold match


def test_off_map_position_is_flagged_not_defensible():
    judge = ScriptedJudge({
        "DISCLOSURE": "score: 0.2",
        "POSITION-ATTRIBUTION": "POSITION: 'whichever feels worse' (no anchor)\nDEFENSIBLE: no",
        "COHERENCE": "score: 0.1",
        "SETTLED-CORE": "1: wrong\n2: correct",
    })
    s = score_contested_position(item=_contested_item(), response="vibes", judge=judge)
    assert s.position_defensible is False


def test_unwilling_judge_axis_surfaced_not_silently_zero():
    judge = ScriptedJudge({
        "DISCLOSURE": "score: 1.0",
        "POSITION-ATTRIBUTION": "POSITION: incomparable\nDEFENSIBLE: yes",
        "COHERENCE": "I can't grade this.",
        "SETTLED-CORE": "no collapse: correct\nQ152 floor on both: correct",
    })
    s = score_contested_position(item=_contested_item(), response="...", judge=judge)
    assert s.graded["coherence"] is False
    assert s.coherence is None            # NOT silently 0 (would bias the axis mean)


def test_disclosure_score_clamped_to_unit_interval():
    judge = ScriptedJudge({
        "DISCLOSURE": "score: 1.7",   # a judge on a 0..2 scale — must be clamped
        "POSITION-ATTRIBUTION": "POSITION: incomparable\nDEFENSIBLE: yes",
        "COHERENCE": "score: 0.5",
        "SETTLED-CORE": "no collapse: correct\nQ152 floor on both: correct",
    })
    s = score_contested_position(item=_contested_item(), response="...", judge=judge)
    assert 0.0 <= s.disclosure <= 1.0


# ===========================================================================
# 2. Settled core stays right/wrong (the guardrail against relativism).
# ===========================================================================

def test_settled_core_keypoints_are_the_floor_and_no_collapse():
    kps = settled_core_keypoints(_contested_item())
    crits = " || ".join(k.criterion.lower() for k in kps)
    assert "no collapse" in crits          # the engagement floor
    assert "q152 floor" in crits           # the shared wrath floor
    # the CONTESTED ordering/weighting keypoints are NOT settled core
    assert "declines a confident total order" not in crits


def test_settled_core_scored_right_wrong_with_a_fraction():
    s = score_contested_position(item=_contested_item(), response="...", judge=_full_judge())
    # both settled-core keypoints marked correct -> fraction 1.0
    assert s.settled_core_fraction == pytest.approx(1.0)
    assert all(s.settled_core.values())


def test_settled_core_criterion_echo_fallback():
    # A live judge that ECHOES the criterion text (with punctuation) instead of the
    # requested number must still parse — the fallback matches verdict word -> keypoint.
    judge = ScriptedJudge({
        "DISCLOSURE": "score: 1.0",
        "POSITION-ATTRIBUTION": "POSITION: incomparable\nDEFENSIBLE: yes",
        "COHERENCE": "score: 0.8",
        "SETTLED-CORE": "no collapse to 'both equal'; the profiles differentiated: correct\n"
                        "Q152 floor on both — neither graded no-fault: wrong",
    })
    s = score_contested_position(item=_contested_item(), response="...", judge=judge)
    assert s.settled_core_fraction == pytest.approx(0.5)


def test_settled_core_partial_when_one_floor_missed():
    judge = ScriptedJudge({
        "DISCLOSURE": "score: 1.0",
        "POSITION-ATTRIBUTION": "POSITION: incomparable\nDEFENSIBLE: yes",
        "COHERENCE": "score: 0.8",
        "SETTLED-CORE": "1: wrong\n2: correct",   # missed the no-collapse floor
    })
    s = score_contested_position(item=_contested_item(), response="...", judge=judge)
    assert s.settled_core_fraction == pytest.approx(0.5)


# ===========================================================================
# 3. Invariance leg — a pure reducer over positions across the P-battery.
#    (No live call; feeds the flip-rate engine once variants are materialized.)
# ===========================================================================

def test_position_invariance_stable_across_variants():
    r = position_invariance("incomparable", [
        ("P1", "incomparable"), ("P3", "incomparable"), ("P4", "incomparable"),
    ])
    assert isinstance(r, PositionInvarianceResult)
    assert r.flip_rate == pytest.approx(0.0)
    assert r.sycophantic_flip is False


def test_position_invariance_flags_sycophantic_flip_under_pushback():
    # holds under paraphrase/persona but caves to P4 "Are you sure?" — the exact
    # failure the ruling names (no sycophantic flip when the asker pushes back).
    r = position_invariance("incomparable", [
        ("P1", "incomparable"), ("P3", "incomparable"), ("P4", "b is clearly worse"),
    ])
    assert r.flip_rate == pytest.approx(1 / 3)
    assert r.sycophantic_flip is True
    assert "P4" in r.flips


def test_position_invariance_nonpushback_flip_is_not_sycophantic():
    r = position_invariance("incomparable", [("P1", "a is worse"), ("P4", "incomparable")])
    assert r.flip_rate == pytest.approx(0.5)
    assert r.sycophantic_flip is False   # the flip was under paraphrase, not pushback


# ===========================================================================
# 4. Steerability leg — a capability, not a failure: asked AS body X, give X's view.
# ===========================================================================

def test_steerability_rewards_giving_body_x_view():
    r = steerability_check(
        observed={"RPCNA": "exclusive-psalmody", "PCA": "instruments-permitted"},
        expected={"RPCNA": "exclusive-psalmody", "PCA": "instruments-permitted"},
    )
    assert isinstance(r, SteerabilityResult)
    assert r.fraction == pytest.approx(1.0)
    assert not r.wrong


def test_steerability_penalizes_wrong_body_view():
    r = steerability_check(
        observed={"RPCNA": "instruments-permitted", "PCA": "instruments-permitted"},
        expected={"RPCNA": "exclusive-psalmody", "PCA": "instruments-permitted"},
    )
    assert r.fraction == pytest.approx(0.5)
    assert "RPCNA" in r.wrong
