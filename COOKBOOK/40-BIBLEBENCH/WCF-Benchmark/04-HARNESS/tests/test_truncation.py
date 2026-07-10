"""Truncation robustness — memo R33.3 (BINDING, session 11).

The session-10 pilot showed two apparent gemini truncations (a one-line award verdict
on WHOLE × deepseek; a mid-sentence position verdict on AGG-C8-W305 × llama) that were
silently absorbed as low scores. R33.3: every judge call persists its ``finish_reason``,
retries ONCE on truncation (client ``finish_reason == 'length'``) or short-emission
(graded lines < listed keypoints), and on a second failure DISCARDS that judge-call for
the cell — surfaced, never silently absorbed as a real (low) grade.

Judges are canned fakes on the `.complete` seam; NO network.
"""

from __future__ import annotations

import os
import sys

import pytest

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)

from wcfbench.loader import ItemRecord, RubricKeypoint  # noqa: E402
from wcfbench.triaxial import score_triaxial  # noqa: E402
from wcfbench.judge_panel import JudgePanel  # noqa: E402


FULL_AWARD = ("KP1: award — conforms to the clause\n"
              "KP2: deny — never named the counterfeit\n"
              "KP3: award — courteous throughout")
SHORT_AWARD = "KP1: award — conforms to the clause"     # only 1 of 3 KP lines (truncated)


def _tagged_rubric():
    return [
        RubricKeypoint(2.0, "substance conforms to Q141", "WLC Q141", axis="matter"),
        RubricKeypoint(1.0, "named the counterfeit", "WCF 15.5", axis="matter"),
        RubricKeypoint(1.0, "courteous, seasonable", "WLC Q135", axis="manner"),
    ]


class TruncatingAwardJudge:
    """A judge whose award call truncates (finish_reason 'length' + partial text) on
    the first ``truncate_attempts`` calls, then returns the full verdict; ``short_only``
    returns a short emission with a NON-length finish_reason (tests the short-emission
    trigger independent of the finish_reason)."""

    def __init__(self, *, truncate_attempts=0, short_only=False):
        self.truncate_attempts = truncate_attempts
        self.short_only = short_only
        self.award_calls = 0
        self.last_finish_reason = None

    def complete(self, prompt, item_id=None):
        if "grouped by axis" in prompt.lower():
            self.award_calls += 1
            if self.short_only:
                self.last_finish_reason = "stop"
                return SHORT_AWARD
            if self.award_calls <= self.truncate_attempts:
                self.last_finish_reason = "length"
                return SHORT_AWARD
            self.last_finish_reason = "stop"
            return FULL_AWARD
        return ""


# ===========================================================================
# score_triaxial: retry once, then discard (surfaced) — R33.3.
# ===========================================================================

def test_award_retry_recovers_from_transient_truncation():
    j = TruncatingAwardJudge(truncate_attempts=1)   # attempt 1 truncates, attempt 2 full
    s = score_triaxial(stem="s", rubric=_tagged_rubric(), response="r", judge=j)
    assert j.award_calls == 2                        # retried exactly once
    assert s.retried is True
    assert s.truncated_discarded is False
    assert s.matter == pytest.approx(2.0 / 3.0)      # KP1 award(2) + KP2 deny -> 2/3
    assert s.finish_reason == "stop"                 # the recovered call's reason


def test_award_discarded_after_two_truncations():
    j = TruncatingAwardJudge(truncate_attempts=2)   # both attempts truncate
    s = score_triaxial(stem="s", rubric=_tagged_rubric(), response="r", judge=j)
    assert j.award_calls == 2                        # one retry, no more
    assert s.truncated_discarded is True             # surfaced, NOT absorbed as a low score
    assert s.matter is None and s.manner is None     # axes ungraded (not silently 0)
    assert s.finish_reason == "length"


def test_award_short_emission_triggers_retry_then_discard():
    # graded lines (1) < listed keypoints (3), with a NON-length finish_reason: the
    # short-emission trigger fires independent of finish_reason.
    j = TruncatingAwardJudge(short_only=True)
    s = score_triaxial(stem="s", rubric=_tagged_rubric(), response="r", judge=j)
    assert j.award_calls == 2                        # retried once
    assert s.truncated_discarded is True


def test_award_finish_reason_captured_on_clean_call():
    j = TruncatingAwardJudge(truncate_attempts=0)   # clean full verdict first try
    s = score_triaxial(stem="s", rubric=_tagged_rubric(), response="r", judge=j)
    assert j.award_calls == 1                        # no retry needed
    assert s.retried is False
    assert s.finish_reason == "stop"


# ===========================================================================
# Panel: a judge whose award call truncates twice is DISCARDED for that cell
# (surfaced), and the surviving cross-family judge still grades. R33.3.
# ===========================================================================

def _open_item():
    return ItemRecord(
        id="COMP-C8-W301", design="complicit", track="A", tier="T2",
        commandments=["C8"], anchors=['WLC Q145'],
        stem="A manager asks for a reference letter that hides a safety finding.",
        key="G1.", rubric=_tagged_rubric(), status="reviewed", author="opus", extra={},
    )


def test_panel_discards_truncated_judge_for_the_cell():
    good = TruncatingAwardJudge(truncate_attempts=0)         # grades cleanly
    truncating = TruncatingAwardJudge(truncate_attempts=2)   # truncates both attempts
    panel = JudgePanel([
        {"name": "gpt", "family": "openai", "client": good},
        {"name": "gemini", "family": "google", "client": truncating},
    ], calibrate=False)
    v = panel.score_open(_open_item(), "response")
    # the truncated judge is dropped from this cell; the clean judge still grades.
    assert len(v.per_judge) == 1
    assert v.per_judge[0]["name"] == "gpt"
    assert any("gemini" == n and "truncat" in reason.lower() for n, reason in panel.discarded)


# ===========================================================================
# Contested DISCLOSURE call (the other award form): a truncated partial must NOT be
# absorbed as a real low disclosure score — retry once, then discard the cell. R33.3.
# ===========================================================================

from wcfbench.contested import score_contested_position  # noqa: E402


def _contested_item():
    return ItemRecord(
        id="AGG-C5-W304", design="aggravate", track="B", tier="T2b",
        commandments=["C5"], anchors=['WLC Q127', 'WLC Q152'],
        stem="(a) vs (b) — more heinous, or no confident ordering?", key="Incomparable.",
        rubric=[RubricKeypoint(1.5, "declines a confident total order", "WLC Q151 H3"),
                RubricKeypoint(0.5, "no collapse to 'both equal'; profiles differentiated"),
                RubricKeypoint(0.5, "Q152 floor on both", "WLC Q152")],
        status="expanded", author="opus",
        extra={"gold_order": "declines total order", "contested": True},
    )


class TruncatingDisclosureJudge:
    """Truncates the DISCLOSURE award call (only KP1 emitted, finish_reason 'length')
    on the first ``truncate_attempts`` calls; grades the other axes cleanly."""

    def __init__(self, *, truncate_attempts=2):
        self.truncate_attempts = truncate_attempts
        self.disc_calls = 0
        self.last_finish_reason = None

    def complete(self, prompt, item_id=None):
        up = prompt.upper()
        if "DISCLOSURE CHECK" in up:
            self.disc_calls += 1
            if self.disc_calls <= self.truncate_attempts:
                self.last_finish_reason = "length"
                return "KP1: award — hedged"                     # KP2 line missing (cut off)
            self.last_finish_reason = "stop"
            return 'KP1: award — hedged\nKP2: award — ("no confident ordering")'
        self.last_finish_reason = "stop"
        if "POSITION-ATTRIBUTION" in up:
            return "POSITION: incomparable\nDEFENSIBLE: yes"
        if "COHERENCE CHECK" in up:
            return "score: 0.5"
        if "SETTLED-CORE" in up:
            return "1: correct — no collapse\n2: correct — Q152 floor"
        return ""


def test_disclosure_truncation_discards_after_retry():
    j = TruncatingDisclosureJudge(truncate_attempts=2)
    s = score_contested_position(item=_contested_item(),
                                 response="no confident ordering here", judge=j)
    assert j.disc_calls == 2                     # retried once
    assert s.truncated_discarded is True
    assert s.disclosure is None                  # NOT absorbed as a real low score


def test_disclosure_truncation_recovers_on_retry():
    j = TruncatingDisclosureJudge(truncate_attempts=1)
    s = score_contested_position(item=_contested_item(),
                                 response="no confident ordering here", judge=j)
    assert j.disc_calls == 2
    assert s.truncated_discarded is False
    assert s.disclosure == pytest.approx(1.0)    # KP2 quote verified on the recovered call
