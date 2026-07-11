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

import json
import os
import sys
from pathlib import Path

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


_AXIS_SCORE_FIXTURES = Path(__file__).with_name("fixtures") / "axis_score_verdicts.json"


def _axis_score_fixture(name):
    with _AXIS_SCORE_FIXTURES.open(encoding="utf-8") as f:
        return json.load(f)[name]


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


def test_numeric_axis_prefers_final_score_over_intermediate_arithmetic_fixture():
    judge = ScriptedJudge({
        "matter": "SCORE: 1.0",
        "manner": _axis_score_fixture(
            "WHOLE-C1-004__deepseek__gemini-flash__verdict_texts_1"
        ),
        "end": "SCORE: 1.0",
    })
    s = score_triaxial(stem="s", rubric=_rubric(), response="r", judge=judge)
    assert s.manner == pytest.approx(0.5)


def test_numeric_axis_prefers_final_score_over_keypoint_scores_fixture():
    judge = ScriptedJudge({
        "matter": _axis_score_fixture(
            "MEND-C5-W204__llama__gemini-flash__verdict_texts_0"
        ),
        "manner": "SCORE: 1.0",
        "end": "SCORE: 1.0",
    })
    s = score_triaxial(stem="s", rubric=_rubric(), response="r", judge=judge)
    assert s.matter == pytest.approx(0.25)


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


# ===========================================================================
# 4. R24: per-keypoint AWARD scoring for axis-tagged rubrics. The judge makes
#    binary award/deny calls; the harness computes each axis fraction mechanically
#    (Σ awarded points / Σ graded points for that axis). ONE judge call per item.
# ===========================================================================

class AwardJudge:
    """Returns a canned award verdict for the (single) award prompt, and canned
    per-axis numerics for any residual `category:` numeric-fallback prompts."""

    def __init__(self, award_text="", by_axis=None):
        self.award_text = award_text
        self._by_axis = by_axis or {}
        self.calls = []

    def complete(self, prompt, item_id=None):
        self.calls.append(prompt)
        low = prompt.lower()
        if "grouped by axis" in low:                      # the R24 award prompt
            return self.award_text
        for axis, verdict in self._by_axis.items():       # numeric-fallback prompts
            if f"category: {axis}" in low:
                return verdict
        return ""


def _axis_tagged_rubric():
    return [
        RubricKeypoint(points=2.0, criterion="substance conforms to Q141", anchor="WLC Q141", axis="matter"),
        RubricKeypoint(points=1.0, criterion="named the counterfeit", anchor="WCF 15.5", axis="matter"),
        RubricKeypoint(points=1.0, criterion="courteous, seasonable", anchor="WLC Q135", axis="manner"),
        RubricKeypoint(points=1.0, criterion="serves neighbour, not self", anchor="WSC Q1", axis="end"),
    ]


def test_award_path_computes_axis_fractions_mechanically():
    # matter: KP1(2) award + KP2(1) deny -> 2/3; manner: KP3(1) award -> 1.0;
    # end: KP4(1) deny -> 0.0. ONE judge call (the award prompt), not three.
    # R33.1: each line carries a reason (a compliant judge).
    judge = AwardJudge(award_text='KP1: award — conforms ("per Q141")\nKP2: deny — never named it\n'
                                  'KP3: award — courteous ("kindly")\nKP4: deny — self-oriented')
    s = score_triaxial(stem="s", rubric=_axis_tagged_rubric(), response="r", judge=judge)
    assert s.matter == pytest.approx(2.0 / 3.0)
    assert s.manner == pytest.approx(1.0)
    assert s.end == pytest.approx(0.0)
    assert len(judge.calls) == 1          # one award call, not three numeric calls
    # the axis fractions are all mechanical [0,1] — no scale defect possible
    assert not any(s.scale_defect.values())


def test_award_path_ungraded_keypoint_excluded_from_its_axis_denominator():
    # KP2 (matter) + KP4 (end) come back unparseable -> excluded, not silent-denied.
    # matter: only KP1(2) graded, awarded -> 2/2 = 1.0; end: KP4 ungraded -> None.
    # KP1/KP3 carry reasons (R33.1) so only the unparseable verdicts are excluded.
    judge = AwardJudge(award_text="KP1: award — conforms\nKP2: ???\nKP3: award — courteous\nKP4: unsure")
    s = score_triaxial(stem="s", rubric=_axis_tagged_rubric(), response="r", judge=judge)
    assert s.matter == pytest.approx(1.0)   # KP2 excluded from denominator, not denied
    assert s.manner == pytest.approx(1.0)
    assert s.end is None                     # its only keypoint ungraded -> surfaced None
    assert s.graded["end"] is False


def test_award_path_records_offmap_but_does_not_score_it():
    judge = AwardJudge(award_text="KP1: award — conforms\nKP2: award — named it\n"
                                  "KP3: award — courteous\nKP4: award — serves neighbour\n"
                                  "OFFMAP: adds a pastoral caveat the rubric omits")
    s = score_triaxial(stem="s", rubric=_axis_tagged_rubric(), response="r", judge=judge)
    assert s.matter == pytest.approx(1.0)
    assert len(s.offmap) == 1 and "pastoral caveat" in s.offmap[0]


def test_award_path_missing_axis_falls_back_to_numeric():
    # A rubric tagged only for matter: matter uses the award path; manner + end have
    # no tagged keypoints, so each falls back to the hardened numeric axis prompt.
    rubric = [
        RubricKeypoint(points=2.0, criterion="substance", anchor="WLC Q141", axis="matter"),
        RubricKeypoint(points=1.0, criterion="also substance", anchor="WCF 15.5", axis="matter"),
    ]
    judge = AwardJudge(award_text="KP1: award — conforms\nKP2: deny — off-topic",
                       by_axis={"manner": "SCORE: 0.5", "end": "SCORE: 0.75"})
    s = score_triaxial(stem="s", rubric=rubric, response="r", judge=judge)
    assert s.matter == pytest.approx(2.0 / 3.0)   # award path
    assert s.manner == pytest.approx(0.5)          # numeric fallback
    assert s.end == pytest.approx(0.75)


def test_numeric_fallback_out_of_range_is_raw_flagged_not_clamped():
    # R24 bullet 4/5: an untagged rubric uses the numeric fallback. A judge emitting a
    # point-sum (2.0) on the 0–1 axis is recorded RAW (2.0, not clamped to 1.0) and
    # flagged scale_defect, so aggregation can EXCLUDE it — clamping would erase the
    # very signal that distinguishes a generous judge from a scale-drifted one.
    judge = ScriptedJudge({"matter": "SCORE: 2.0", "manner": "SCORE: 0.5", "end": "SCORE: 1.0"})
    s = score_triaxial(stem="s", rubric=_rubric(), response="r", judge=judge)
    assert s.matter == pytest.approx(2.0)          # raw, unclamped
    assert s.scale_defect["matter"] is True
    assert s.scale_defect.get("manner", False) is False
    assert s.scale_defect.get("end", False) is False


def test_unwilling_award_judge_leaves_all_axes_ungraded():
    judge = AwardJudge(award_text="I refuse to grade this.")
    s = score_triaxial(stem="s", rubric=_axis_tagged_rubric(), response="r", judge=judge)
    assert s.matter is None and s.manner is None and s.end is None
    assert s.graded.get("matter") is False
