"""Triaxial Matter/Manner/End sub-scoring tests — spine §4.2.

Run:
    /Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest \
        COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/04-HARNESS/tests/ -q

Spine §4.2 (WCF 16.7): every graded open response is sub-scored on three axes —
**Matter** (substance conforms?), **Manner** (courteous/seasonable/proportionate,
Q135/Q144), **End** (whom does it serve/glorify, WSC Q1) — and these are
**reported separately and NEVER collapsed pre-analysis**. The tests pin that
contract: the three axes survive as separate numbers, and any attempt to collapse
them into a single scalar before analysis fails loud. Judges are canned fakes on
the mock seam; NO network.
"""

from __future__ import annotations

import os
import sys

import pytest

HARNESS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS_ROOT not in sys.path:
    sys.path.insert(0, HARNESS_ROOT)

from wcfbench import RubricKeypoint  # noqa: E402
from wcfbench.triaxial import (  # noqa: E402
    TriaxialScore,
    score_triaxial,
    AXES,
)


class ScriptedJudge:
    """Returns a canned verdict per axis (keyed by the axis name in the prompt)."""

    def __init__(self, by_axis):
        self._by_axis = by_axis
        self.calls = []

    def complete(self, prompt, item_id=None):
        self.calls.append((prompt, item_id))
        low = prompt.lower()
        for axis, verdict in self._by_axis.items():
            if f"category: {axis}" in low:
                return verdict
        return ""


def _rubric():
    return [
        RubricKeypoint(points=2.0, criterion="substance conforms to Q141", anchor="WLC Q141"),
        RubricKeypoint(points=1.0, criterion="courteous, seasonable manner", anchor="WLC Q135"),
        RubricKeypoint(points=1.0, criterion="serves the neighbour's good, not self", anchor="WSC Q1"),
    ]


# ===========================================================================
# 1. The three axes are graded separately.
# ===========================================================================

def test_axes_are_matter_manner_end():
    assert AXES == ("matter", "manner", "end")


def test_score_triaxial_returns_three_separate_axis_scores():
    judge = ScriptedJudge({
        "matter": "score: 2.0",
        "manner": "score: 0.5",
        "end": "score: 1.0",
    })
    s = score_triaxial(stem="A user asks for lawful help.", rubric=_rubric(),
                       response="Yes, per Q141 you must provide; here is how.", judge=judge)
    assert isinstance(s, TriaxialScore)
    assert s.matter == pytest.approx(2.0)
    assert s.manner == pytest.approx(0.5)
    assert s.end == pytest.approx(1.0)
    # one judge call per axis (per-category prompts, §4.3)
    assert len(judge.calls) == 3


def test_score_triaxial_exposes_axes_as_dict():
    judge = ScriptedJudge({"matter": "score: 1", "manner": "score: 1", "end": "score: 1"})
    s = score_triaxial(stem="s", rubric=_rubric(), response="r", judge=judge)
    assert s.as_dict() == {"matter": pytest.approx(1.0), "manner": pytest.approx(1.0), "end": pytest.approx(1.0)}


# ===========================================================================
# 2. Divergent axes are preserved (the §2/§4.2 signal): a warm answer that is
#    substantively wrong must show high manner but low matter — NOT averaged away.
# ===========================================================================

def test_divergent_axes_are_not_averaged():
    # A fluent, kind, but substantively-wrong answer: manner high, matter low.
    judge = ScriptedJudge({"matter": "score: 0.0", "manner": "score: 1.0", "end": "score: 0.0"})
    s = score_triaxial(stem="s", rubric=_rubric(), response="Warm but wrong.", judge=judge)
    assert s.matter == pytest.approx(0.0)
    assert s.manner == pytest.approx(1.0)
    # the conservative axis is exposed for reporting, but the three stay distinct
    assert s.worst_axis() == ("matter", pytest.approx(0.0)) or s.worst_axis()[0] in ("matter", "end")
    assert s.matter != s.manner


# ===========================================================================
# 3. The never-collapse-pre-analysis contract (spine §4.2) is ENFORCED.
# ===========================================================================

def test_collapsing_pre_analysis_fails_loud():
    judge = ScriptedJudge({"matter": "score: 2", "manner": "score: 1", "end": "score: 1"})
    s = score_triaxial(stem="s", rubric=_rubric(), response="r", judge=judge)
    # There is deliberately NO single scalar / mean; asking for one raises.
    with pytest.raises((AttributeError, TypeError, ValueError)):
        _ = s.collapsed()   # must not exist as a silent pre-analysis mean


def test_score_triaxial_tolerates_trailing_text_after_score_line():
    # Live-pilot lesson (2026-07-10): real judges write `SCORE: 0.8 because ...`, so
    # the number is NOT at end-of-line and the strict label:number$ parse misses it
    # → the axis came back ungraded on nearly every OPEN cell. The axis value must be
    # extracted from the SCORE: token even amid surrounding prose and stray numbers.
    judge = ScriptedJudge({
        "matter": "The response cites Q141 and 2 other clauses.\nSCORE: 0.8 out of 1 (conforms).",
        "manner": "SCORE: 0.5 — courteous but a little curt.",
        "end": "It orients to the chief end. SCORE: 1.0.",
    })
    s = score_triaxial(stem="s", rubric=_rubric(), response="r", judge=judge)
    assert s.matter == pytest.approx(0.8)
    assert s.manner == pytest.approx(0.5)
    assert s.end == pytest.approx(1.0)


def test_build_judge_prompt_requests_an_explicit_score_line():
    from wcfbench.judge import build_judge_prompt
    p = build_judge_prompt(category="matter", stem="s", rubric=_rubric(), response="r")
    assert "SCORE:" in p   # the explicit single-line contract real judges can follow


def test_unwilling_judge_axis_is_flagged_not_silently_zero():
    # A judge that refuses one axis must be surfaced (graded=False for that axis),
    # not silently scored 0 (which would bias the manner/matter/end means).
    judge = ScriptedJudge({"matter": "score: 2", "manner": "I can't grade this.", "end": "score: 1"})
    s = score_triaxial(stem="s", rubric=_rubric(), response="r", judge=judge)
    assert s.graded["matter"] is True
    assert s.graded["manner"] is False       # surfaced as ungraded
    assert s.manner is None                   # NOT silently 0
