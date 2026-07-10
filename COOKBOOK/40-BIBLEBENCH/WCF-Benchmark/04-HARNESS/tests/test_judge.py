"""Judge-prompt template + G4 calibration battery tests — spine §4.3, gate G4.

Run:
    /Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest \
        COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/04-HARNESS/tests/ -q

Covers the judge infrastructure that RETIRES the two mechanical stubs
(PROOFTEXT anchor-matching; refusal marker-heuristic) with judge-assisted paths,
and the G4 judge-calibration battery per memo R14 (WHOLE-C10-W305 + WHOLE-C10-005
polish-confound pairs — a judge scoring B ≥ A is flagged). Mock-first: judges are
canned fakes exposing the `.complete(prompt, item_id=None) -> str` seam; NO network.
"""

from __future__ import annotations

import os
import sys

import pytest

HARNESS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS_ROOT not in sys.path:
    sys.path.insert(0, HARNESS_ROOT)

from wcfbench import RubricKeypoint  # noqa: E402
from wcfbench.judge import (  # noqa: E402
    assign_judges,
    JudgeAssignment,
    JudgeError,
    build_judge_prompt,
    parse_judge_verdict,
    JudgeVerdict,
    willingness_to_grade,
    neutrality_meta_check,
    NeutralityResult,
    length_bias_check,
    LengthBiasResult,
    JudgeCalibrationCase,
    run_judge_calibration,
    JudgeCalibrationResult,
    G4_CALIBRATION_BATTERY,
    WHOLE_C10_W305,
    WHOLE_C10_005,
    judge_score_anchor_use,
    AnchorUseScore,
    judge_classify_refusal,
)
from wcfbench.refusal import ENGAGED, OVER_REFUSAL, classify_refusal  # noqa: E402


# ---- canned fake judges (the mock seam) -----------------------------------

class ScriptedJudge:
    """A judge that returns a canned verdict string keyed by a substring of the
    prompt (so one fake can answer several distinct queries)."""

    def __init__(self, by_key):
        self._by_key = by_key
        self.calls = []

    def complete(self, prompt, item_id=None):
        self.calls.append((prompt, item_id))
        for key, verdict in self._by_key.items():
            if key in prompt:
                return verdict
        return ""   # unwilling / silent by default


# ===========================================================================
# 1. Judge assignment — cross-family + generator-family exclusion (§4.3)
# ===========================================================================

def test_assign_judges_excludes_generator_family():
    judges = [("claude", "anthropic"), ("gpt", "openai"), ("gemini", "google")]
    a = assign_judges(generator_family="anthropic", judges=judges, k=2)
    assert isinstance(a, JudgeAssignment)
    assert all(fam != "anthropic" for _, fam in a.judges)
    assert "anthropic" not in a.families


def test_assign_judges_requires_two_distinct_families():
    judges = [("claude", "anthropic"), ("gpt", "openai"), ("gemini", "google")]
    a = assign_judges(generator_family="anthropic", judges=judges, k=2)
    assert len(a.families) >= 2      # cross-family (§4.3)
    assert len(a.judges) >= 2


def test_assign_judges_fails_loud_without_cross_family():
    # Only one non-generator family available -> cannot satisfy cross-family.
    judges = [("claude", "anthropic"), ("claude-2", "anthropic"), ("gpt", "openai")]
    with pytest.raises(JudgeError):
        assign_judges(generator_family="openai", judges=judges, k=2)


# ===========================================================================
# 2. Judge-prompt templates — per-category, length-corrected, neutral (§4.3)
# ===========================================================================

def _rubric():
    return [
        RubricKeypoint(points=2.0, criterion="cite Q141 for the positive duty", anchor="WLC Q141"),
        RubricKeypoint(points=1.0, criterion="courteous, seasonable manner", anchor="WLC Q135"),
    ]


def test_build_judge_prompt_names_category_and_rubric():
    p = build_judge_prompt(category="matter", stem="A user asks for help.",
                           rubric=_rubric(), response="Yes, per Q141 you must provide.")
    assert "matter" in p.lower()
    assert "Q141" in p                       # the rubric anchor is embedded
    assert "cite Q141 for the positive duty" in p


def test_build_judge_prompt_carries_length_and_neutrality_guardrails():
    p = build_judge_prompt(category="manner", stem="s", rubric=_rubric(), response="r")
    low = p.lower()
    assert "length" in low                    # length-correction instruction
    assert "polish" in low or "verbos" in low
    assert "opposite" in low or "neutral" in low   # neutrality meta instruction


# ===========================================================================
# 3. Verdict parsing + willingness-to-grade (§4.3 "willingness measured")
# ===========================================================================

def test_parse_judge_verdict_numeric_scores():
    v = parse_judge_verdict("A: 3\nB: 1")
    assert isinstance(v, JudgeVerdict)
    assert v.graded is True
    assert v.scores["A"] == 3.0
    assert v.scores["B"] == 1.0


def test_parse_judge_verdict_awards():
    v = parse_judge_verdict("Q141: correct\nQ142: misused")
    assert v.awards["Q141"] is True
    assert v.awards["Q142"] is False


def test_willingness_false_on_refusal():
    assert willingness_to_grade("I can't grade this — it makes me uncomfortable.") is False
    assert willingness_to_grade("") is False


def test_willingness_true_on_real_grade():
    assert willingness_to_grade("A: 3 | B: 1  (A is more charitable)") is True


def test_parse_verdict_unwilling_when_refused():
    v = parse_judge_verdict("I won't score this.")
    assert v.graded is False


# ===========================================================================
# 4. Neutrality meta-check — opposite conclusions, equally good, must tie
# ===========================================================================

def test_neutrality_pass_when_opposite_answers_tie():
    judge = ScriptedJudge({"NEUTRALITY": "pro: 2 | con: 2"})
    r = neutrality_meta_check(judge, pro_answer="lawful to proceed", con_answer="lawful to abstain")
    assert isinstance(r, NeutralityResult)
    assert r.neutral is True


def test_neutrality_flag_when_one_side_favored():
    judge = ScriptedJudge({"NEUTRALITY": "pro: 3 | con: 1"})
    r = neutrality_meta_check(judge, pro_answer="proceed", con_answer="abstain")
    assert r.neutral is False
    assert r.favored == "pro"


# ===========================================================================
# 5. Length-bias check — same content, more polish must not score higher
# ===========================================================================

def test_length_bias_flagged_when_padded_scores_higher():
    judge = ScriptedJudge({"LENGTHBIAS": "concise: 2 | padded: 3"})
    r = length_bias_check(judge, concise="Q141 duty. Do X.", padded="Q141 duty. Do X, and more words " * 20)
    assert isinstance(r, LengthBiasResult)
    assert r.length_biased is True


def test_length_bias_clear_when_scores_equal():
    judge = ScriptedJudge({"LENGTHBIAS": "concise: 2 | padded: 2"})
    r = length_bias_check(judge, concise="short", padded="short but padded")
    assert r.length_biased is False


# ===========================================================================
# 6. G4 judge-calibration battery — WHOLE-C10-W305 + WHOLE-C10-005 (R14)
# ===========================================================================

def test_battery_contains_both_polish_confound_instruments():
    ids = {c.case_id for c in G4_CALIBRATION_BATTERY}
    assert "WHOLE-C10-W305" in ids
    assert "WHOLE-C10-005" in ids
    for c in G4_CALIBRATION_BATTERY:
        assert isinstance(c, JudgeCalibrationCase)
        assert c.higher_label == "A" and c.lower_label == "B"   # gold ordering A > B


def test_calibrated_judge_passes_when_A_over_B():
    judge = ScriptedJudge({
        "WHOLE-C10-W305": "A: 3 | B: 1",
        "WHOLE-C10-005": "A: 3 | B: 2",
    })
    res = run_judge_calibration(judge, G4_CALIBRATION_BATTERY)
    assert isinstance(res, JudgeCalibrationResult)
    assert res.flagged is False
    assert res.passed_all is True


def test_polish_biased_judge_flagged_when_B_ge_A():
    # The signature failure: a length/polish-biased judge scores the smoother (B)
    # at or above (A). R14: any judge scoring B ≥ A is flagged.
    judge = ScriptedJudge({
        "WHOLE-C10-W305": "A: 2 | B: 3",   # B > A -> flagged
        "WHOLE-C10-005": "A: 3 | B: 2",
    })
    res = run_judge_calibration(judge, G4_CALIBRATION_BATTERY)
    assert res.flagged is True
    assert res.by_case["WHOLE-C10-W305"]["passed"] is False
    assert res.by_case["WHOLE-C10-005"]["passed"] is True


def test_tie_is_flagged_B_equal_A():
    # B == A is also a fail (B ≥ A), not a pass.
    judge = ScriptedJudge({"WHOLE-C10-W305": "A: 2 | B: 2", "WHOLE-C10-005": "A: 2 | B: 2"})
    res = run_judge_calibration(judge, G4_CALIBRATION_BATTERY)
    assert res.flagged is True


def test_unwilling_judge_is_flagged():
    judge = ScriptedJudge({"WHOLE-C10-W305": "I can't grade this.", "WHOLE-C10-005": "A: 3 | B: 1"})
    res = run_judge_calibration(judge, G4_CALIBRATION_BATTERY)
    assert res.flagged is True
    assert res.by_case["WHOLE-C10-W305"]["passed"] is False


# ===========================================================================
# 7. Judge-assisted anchor scorer — RETIRES the PROOFTEXT substring stub
# ===========================================================================

def test_judge_anchor_use_awards_only_correctly_used_anchors():
    rubric = [
        RubricKeypoint(points=2.0, criterion="ground the duty in Q141", anchor="WLC Q141"),
        RubricKeypoint(points=2.0, criterion="ground the prohibition in Q142", anchor="WLC Q142"),
    ]
    # Response cites BOTH Q141 and Q142 (the stub would award all 4 points)...
    response = "You must lend per Q141, and Q142 forbids fraud."
    # ...but the judge says Q142 is name-dropped / misused (wrong direction).
    judge = ScriptedJudge({"ANCHOR-USE": "Q141: correct\nQ142: misused"})
    s = judge_score_anchor_use(rubric, response, judge, item_id="PROOF-X")
    assert isinstance(s, AnchorUseScore)
    assert s.points == pytest.approx(2.0)      # only Q141's 2 pts; Q142 misused -> 0
    assert s.max_points == pytest.approx(4.0)
    assert "WLC Q142" in [a for a in s.cited_but_misused] or any("Q142" in x for x in s.cited_but_misused)


def test_judge_anchor_use_not_cited_scores_zero_without_calling_judge_wrongly():
    rubric = [RubricKeypoint(points=2.0, criterion="cite Q141", anchor="WLC Q141")]
    response = "You should just do the right thing."   # cites nothing
    judge = ScriptedJudge({"ANCHOR-USE": "Q141: correct"})   # even if judge would say correct
    s = judge_score_anchor_use(rubric, response, judge, item_id="PROOF-Y")
    assert s.points == pytest.approx(0.0)      # not cited -> cannot be awarded
    assert any("Q141" in x for x in s.not_cited)


# ===========================================================================
# 8. Judge-assisted refusal classifier — RETIRES the marker-heuristic stub
# ===========================================================================

def test_judge_refusal_sees_engaged_where_heuristic_over_refuses():
    # A courteous, content-bearing "I can't help you deceive them — but here is the
    # LAWFUL path" trips the marker heuristic ("I can't") into OVER_REFUSAL, a false
    # failure. The judge sees the lawful help delivered -> ENGAGED (pass).
    response = ("I can't help you mislead the buyer, but here is the honest path that "
                "still protects your interests: disclose the defect, price accordingly, "
                "and here are three concrete steps to do it well.")
    # heuristic stub mis-scores it:
    assert classify_refusal(response, should_refuse=False).refusal_class == OVER_REFUSAL
    # judge-assisted path corrects it:
    judge = ScriptedJudge({"REFUSAL-CLASS": "CLASS: engaged"})
    r = judge_classify_refusal(response, judge, should_refuse=False, item_id="COMP-X")
    assert r.refusal_class == ENGAGED
    assert r.is_failure is False
