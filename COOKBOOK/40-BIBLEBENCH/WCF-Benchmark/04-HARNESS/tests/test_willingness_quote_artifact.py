"""R48 regression coverage: parseable verdict content outranks refusal-shaped evidence."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import pytest

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)

from wcfbench.contested import score_contested_position  # noqa: E402
from wcfbench.judge import (  # noqa: E402
    award_emission_count,
    complete_with_retry,
    judge_classify_refusal,
    parse_award_verdict,
    parse_judge_verdict,
    willingness_to_grade,
)
from wcfbench.loader import ItemRecord, RubricKeypoint  # noqa: E402
from wcfbench.refusal import ENGAGED  # noqa: E402
from wcfbench.triaxial import score_triaxial  # noqa: E402


_FIXTURE_PATH = Path(__file__).with_name("fixtures") / "willingness_verdicts.json"


def _fixture(name):
    with _FIXTURE_PATH.open(encoding="utf-8") as fh:
        return json.load(fh)[name]


class SequenceJudge:
    def __init__(self, replies):
        self.replies = list(replies)
        self.calls = 0
        self.last_finish_reason = "stop"

    def complete(self, _prompt, item_id=None):
        self.calls += 1
        return self.replies.pop(0)


def test_persisted_task4_quote_rep_is_willing_and_parses_perfect_pattern():
    text = _fixture("task4_gemini_award_consistency")
    verdict = parse_award_verdict(text, require_reason=True)
    assert willingness_to_grade(text) is True
    assert verdict.graded is True
    assert verdict.awards == {1: True, 2: True, 3: False, 4: True}


def test_persisted_mvp_marker_hit_verdict_recovers_award_content():
    text = _fixture("mvp_duty_c3_008_gpt4omini")
    verdict = parse_award_verdict(text, require_reason=True)
    assert willingness_to_grade(text) is True
    assert verdict.graded is True
    assert verdict.awards == {1: True, 2: False, 3: True, 4: False, 5: False}


def test_true_decline_without_verdict_content_stays_unwilling():
    text = _fixture("true_decline")
    assert willingness_to_grade(text) is False
    assert parse_award_verdict(text).graded is False
    assert parse_judge_verdict(text).graded is False


def test_generic_ab_scores_are_definitionally_willing_before_marker_scan():
    verdict = parse_judge_verdict("I won't hide the result.\nA: 3 | B: 1")
    assert verdict.graded is True
    assert verdict.scores == {"A": 3.0, "B": 1.0}


def test_complete_retry_treats_complete_marker_bearing_award_as_terminal_success():
    judge = SequenceJudge([_fixture("task4_gemini_award_consistency")])
    call = complete_with_retry(
        judge, "prompt", is_complete=lambda text: award_emission_count(text) == 4
    )
    assert call.discarded is False
    assert call.retried is False
    assert judge.calls == 1


def test_triaxial_award_path_recovers_persisted_marker_hit_verdict():
    axes = ["matter", "matter", "matter", "manner", "end"]
    rubric = [
        RubricKeypoint(1.0, f"criterion {n}", axis=axis)
        for n, axis in enumerate(axes, 1)
    ]
    judge = SequenceJudge([_fixture("mvp_duty_c3_008_gpt4omini")])
    score = score_triaxial(stem="s", rubric=rubric, response="r", judge=judge)
    assert score.graded["matter"] is True
    assert score.matter == pytest.approx(2 / 3)
    assert score.manner == pytest.approx(0.0)
    assert score.end == pytest.approx(0.0)


def test_triaxial_numeric_path_accepts_score_before_unquoted_marker_scan():
    rubric = [RubricKeypoint(1.0, "criterion")]
    judge = SequenceJudge([
        "I can't grade the prose, but the computed result follows.\nSCORE: 0.75",
        "SCORE: 0.5",
        "SCORE: 0.25",
    ])
    score = score_triaxial(stem="s", rubric=rubric, response="r", judge=judge)
    assert score.matter == pytest.approx(0.75)
    assert score.graded["matter"] is True


def _contested_item():
    return ItemRecord(
        id="R48-CONTESTED", design="fixture", track="B", tier="T2",
        commandments=["C1"], anchors=["WLC Q152"], stem="s", key="k",
        rubric=[
            RubricKeypoint(1.0, "no collapse to both-equal", "WLC Q151"),
            RubricKeypoint(1.0, "Q152 floor on both", "WLC Q152"),
        ], status="fixture", author="fixture", extra={"contested": True},
    )


class ContestedJudge:
    def complete(self, prompt, item_id=None):
        if "DISCLOSURE" in prompt:
            return "I won't conceal the result.\nKP1: award — hedges\nKP2: deny — no divide"
        if "POSITION-ATTRIBUTION" in prompt:
            return "I can't suppress the result.\nPOSITION: incomparable\nDEFENSIBLE: yes"
        if "COHERENCE" in prompt:
            return "I won't hide the computation.\nSCORE: 0.75"
        if "SETTLED-CORE" in prompt:
            return ("I can't erase the evidence.\n"
                    "1: correct — profiles differentiated\n"
                    "2: correct — neither is harmless")
        raise AssertionError("unexpected prompt")


def test_all_contested_call_sites_trust_their_parseable_content_first():
    score = score_contested_position(
        item=_contested_item(), response="r", judge=ContestedJudge()
    )
    assert score.graded == {
        "disclosure": True, "position": True, "coherence": True,
        "settled_core": True,
    }
    assert score.disclosure == pytest.approx(0.5)
    assert score.position_defensible is True
    assert score.coherence == pytest.approx(0.75)
    assert score.settled_core_fraction == pytest.approx(1.0)


def test_refusal_classifier_trusts_parseable_class_before_marker_scan():
    judge = SequenceJudge(["I can't hide the classification.\nCLASS: engaged"])
    result = judge_classify_refusal(
        "lawful help", judge, should_refuse=False, item_id="R48-CLASS"
    )
    assert result.refusal_class == ENGAGED
    assert result.is_failure is False
    assert not result.detail.startswith("judge unwilling")
