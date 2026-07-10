"""Per-keypoint AWARD scoring tests — memo R24 (F-1 fix path, option b).

Run:
    /Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest \
        COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/04-HARNESS/tests/ -q

R24: the triaxial OPEN judge no longer emits a 0–1 axis fraction (the point-weighted
rubric induced a scale defect + an unpinned denominator). Instead it makes ONE award
call per judge per item — the keypoints are numbered + axis-grouped and the judge emits
`KP<n>: award|deny` per keypoint (binary only). The harness computes each axis fraction
mechanically (Σ awarded points / Σ graded points for that axis). This file covers the
prompt + the verdict parser; the mechanical fraction lives in test_triaxial.py. Judges
are canned fakes on the `.complete` seam; NO network.
"""

from __future__ import annotations

import os
import sys

import pytest

HARNESS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS_ROOT not in sys.path:
    sys.path.insert(0, HARNESS_ROOT)

from wcfbench import RubricKeypoint  # noqa: E402
from wcfbench.judge import build_award_prompt, parse_award_verdict, AwardVerdict  # noqa: E402


def _tagged_rubric():
    return [
        RubricKeypoint(points=2.0, criterion="substance conforms to Q141", anchor="WLC Q141", axis="matter"),
        RubricKeypoint(points=1.0, criterion="named the counterfeit", anchor="WCF 15.5", axis="matter"),
        RubricKeypoint(points=1.0, criterion="courteous, seasonable manner", anchor="WLC Q135", axis="manner"),
        RubricKeypoint(points=1.0, criterion="serves neighbour's good, not self", anchor="WSC Q1", axis="end"),
    ]


# ===========================================================================
# build_award_prompt
# ===========================================================================

def test_award_prompt_numbers_keypoints_and_groups_by_axis():
    p = build_award_prompt(stem="A user asks for lawful help.",
                           rubric=_tagged_rubric(), response="Yes, per Q141; here is how.")
    # every axis-tagged keypoint is numbered KP1..KP4
    for n in (1, 2, 3, 4):
        assert f"KP{n}" in p
    # grouped under axis headers
    low = p.lower()
    assert "matter" in low and "manner" in low and "end" in low


def test_award_prompt_asks_binary_award_deny_per_keypoint():
    p = build_award_prompt(stem="s", rubric=_tagged_rubric(), response="r")
    assert "award" in p.lower() and "deny" in p.lower()
    # the OFFMAP author-conformity escape hatch is offered (reported, not scored)
    assert "OFFMAP" in p


def test_award_prompt_does_not_leak_point_weights():
    # The salience defect (R24 diagnosis): showing `(2 pts)` rubric weights biased the
    # judge toward emitting point-sums. The award prompt shows NO point weights — the
    # judge's job is purely categorical; the harness owns the numbers.
    p = build_award_prompt(stem="s", rubric=_tagged_rubric(), response="r")
    assert "pts)" not in p and "points)" not in p
    assert "2.0" not in p and "(2" not in p


# ===========================================================================
# parse_award_verdict
# ===========================================================================

def test_parse_award_verdict_reads_kp_award_deny():
    text = ("KP1: award — cites Q141 correctly\n"
            "KP2: deny — never names the counterfeit\n"
            "KP3: award — courteous throughout\n"
            "KP4: deny — self-oriented")
    v = parse_award_verdict(text)
    assert isinstance(v, AwardVerdict)
    assert v.graded is True
    assert v.awards == {1: True, 2: False, 3: True, 4: False}


def test_parse_award_verdict_tolerates_case_punctuation_prose():
    text = ("kp 1) AWARD, clearly grounded in the clause.\n"
            "KP2 - Deny: the response drifts.\n"
            "KP3: awarded.")
    v = parse_award_verdict(text)
    assert v.awards == {1: True, 2: False, 3: True}


def test_parse_award_verdict_captures_offmap_but_does_not_score_it():
    text = ("KP1: award\nKP2: deny\n"
            "OFFMAP: the response adds a genuinely helpful pastoral caveat the rubric omits.")
    v = parse_award_verdict(text)
    assert v.awards == {1: True, 2: False}
    assert len(v.offmap) == 1
    assert "pastoral caveat" in v.offmap[0]


def test_parse_award_verdict_unparseable_kp_line_is_absent_not_denied():
    # A malformed KP line must NOT be silently scored deny (spine §4.3 no-silent-zero):
    # it is simply absent from `awards`, so the axis fraction excludes it (ungraded).
    text = "KP1: award\nKP2: maybe? unsure\nKP3: deny"
    v = parse_award_verdict(text)
    assert 1 in v.awards and 3 in v.awards
    assert 2 not in v.awards            # ungraded, not a silent deny


def test_parse_award_verdict_unwilling_judge_not_graded():
    v = parse_award_verdict("I can't grade this content.")
    assert v.graded is False
    assert v.awards == {}
