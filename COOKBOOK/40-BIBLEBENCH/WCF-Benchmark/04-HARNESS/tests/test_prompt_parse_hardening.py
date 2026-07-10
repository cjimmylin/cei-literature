"""Prompt / parse hardening — memo R33.7 / R33.8 (BINDING, session 11).

R33.7 (clause-gloss): the award prompt states that a bracketed ``[anchor]`` in a
criterion is the grader's GLOSS — the keypoint is satisfied by SUBSTANCE unless the
criterion text itself demands naming the clause (fixes R29(c)'s shared manner
under-credit without touching any criterion). Plus an optional reported-not-scored
``CITEFLAG:`` line for fabricated/irrelevant clause citations (llama's "WCF 1.4/1.10").

R33.8:
  (a) parse-and-report the ``RANKING:`` line on CONTESTED items (R31b) — it feeds the
      position map + the incoherence record (llama's malformed ``(b) < (a) < (most)``).
  (b) markdown-tolerant numeric parse + pinned levels on contested coherence (R32i) —
      ``**Score**: 0.5`` must parse (the PF-4 parse-None was a markdown-bold value).

Judges are canned fakes on the `.complete` seam; NO network.
"""

from __future__ import annotations

import os
import sys

import pytest

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)

from wcfbench import RubricKeypoint  # noqa: E402
from wcfbench.judge import build_award_prompt, parse_award_verdict  # noqa: E402
from wcfbench.loader import ItemRecord  # noqa: E402
from wcfbench.contested import score_contested_position  # noqa: E402


# ===========================================================================
# R33.7 — clause-gloss instruction + CITEFLAG.
# ===========================================================================

def _rubric():
    return [RubricKeypoint(2.0, "substance conforms to Q141", "WLC Q141", axis="matter"),
            RubricKeypoint(1.0, "courteous manner", "WLC Q135", axis="manner")]


def test_award_prompt_states_bracketed_anchor_is_a_gloss():
    p = build_award_prompt(stem="s", rubric=_rubric(), response="r")
    low = p.lower()
    assert "gloss" in low
    assert "substance" in low
    # CITEFLAG escape hatch offered (reported, not scored)
    assert "CITEFLAG" in p


def test_parse_award_captures_citeflag_but_does_not_score_it():
    text = ('KP1: award — conforms ("per Q141")\nKP2: deny — curt\n'
            'CITEFLAG: cites "WCF 1.4" (a Scripture clause) for a ninth-commandment point')
    v = parse_award_verdict(text)
    assert v.awards == {1: True, 2: False}          # CITEFLAG is not a KP verdict
    assert len(v.citeflags) == 1 and "WCF 1.4" in v.citeflags[0]


# ===========================================================================
# R33.8(a) — parse-and-report the RANKING line on CONTESTED items.
# ===========================================================================

def _contested_item():
    return ItemRecord(
        id="AGG-C8-W305", design="aggravate", track="B", tier="T2b",
        commandments=["C8"], anchors=['WLC Q151', 'WLC Q152'],
        stem="(a) Sam vs (b) Renu — more heinous, or no confident ordering?", key="contested.",
        rubric=[RubricKeypoint(1.5, "declines a confident total order", "WLC Q151 H3"),
                RubricKeypoint(0.5, "no collapse to 'both equal'; profiles differentiated"),
                RubricKeypoint(0.5, "Q152 floor on both", "WLC Q152")],
        status="expanded", author="opus",
        extra={"gold_order": "declines total order", "contested": True},
    )


class _CJudge:
    def complete(self, prompt, item_id=None):
        up = prompt.upper()
        if "DISCLOSURE CHECK" in up:
            return 'KP1: award — hedged\nKP2: deny — no divide'
        if "POSITION-ATTRIBUTION" in up:
            return "POSITION: incomparable\nDEFENSIBLE: yes"
        if "COHERENCE CHECK" in up:
            return "score: 0.5"
        if "SETTLED-CORE" in up:
            return "1: correct — no collapse\n2: correct — Q152 floor"
        return ""


def test_contested_reports_clean_ranking_line():
    resp = "I weigh both. RANKING: a < b"
    s = score_contested_position(item=_contested_item(), response=resp, judge=_CJudge())
    assert s.ranking_parsed == ["a", "b"]
    assert s.ranking_malformed is False
    assert "a < b" in s.ranking_line


def test_contested_flags_malformed_ranking_line():
    # llama's real malformed line on a two-option item: a stray '(most)' token.
    resp = "It does not yield a confident ordering. RANKING: (b) < (a) < (most)"
    s = score_contested_position(item=_contested_item(), response=resp, judge=_CJudge())
    assert s.ranking_malformed is True          # parse-and-report flags it (not scored)
    assert "RANKING:" in s.ranking_line


def test_contested_no_ranking_line_is_none():
    resp = "A prose answer with no ranking line at all."
    s = score_contested_position(item=_contested_item(), response=resp, judge=_CJudge())
    assert s.ranking_line is None
    assert s.ranking_malformed is False


# ===========================================================================
# R33.8(b) — markdown-tolerant coherence parse + pinned levels.
# ===========================================================================

class _MarkdownCoherenceJudge(_CJudge):
    def complete(self, prompt, item_id=None):
        if "COHERENCE CHECK" in prompt.upper():
            return "The reasoning is partly grounded.\n**Score**: 0.5"   # markdown-bold value
        return super().complete(prompt, item_id)


def test_contested_coherence_tolerates_markdown_bold_score():
    # PF-4: `**Score**: 0.5` surfaced ungraded before (letter-initial _SCORE_RE missed it).
    s = score_contested_position(item=_contested_item(), response="RANKING: a < b",
                                 judge=_MarkdownCoherenceJudge())
    assert s.coherence == pytest.approx(0.5)
    assert s.graded["coherence"] is True


def test_contested_coherence_prompt_pins_levels():
    # the coherence prompt must offer the pinned 0.0/0.25/0.5/0.75/1.0 levels.
    from wcfbench.contested import score_contested_position as _s  # noqa: F401
    captured = {}

    class _Capture(_CJudge):
        def complete(self, prompt, item_id=None):
            if "COHERENCE CHECK" in prompt.upper():
                captured["p"] = prompt
            return super().complete(prompt, item_id)

    score_contested_position(item=_contested_item(), response="RANKING: a < b", judge=_Capture())
    assert "0.25" in captured["p"] and "0.75" in captured["p"]
