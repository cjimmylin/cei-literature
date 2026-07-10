"""Reason mandate + KP2 evidence rule — memo R33.1 / R33.2 (BINDING, session 11).

R33.1 restores R24's original judge contract that session 9 softened to optional
("a one-line reason is welcome"): the award / disclosure / settled-core prompts now
REQUIRE a one-line reason WITH a short verbatim evidence quote per keypoint. This was
"the single change that most limited" the session-10 adjudication (R33.1), so it is
the headline of this session.

  - A reasonless award/deny line on an OPEN award axis → that keypoint UNGRADED
    (existing exclusion semantics — excluded from the axis denominator, NEVER a silent
    deny) + a logged compliance defect.
  - On the settled-core, a reasonless line keeps the AFFIRMATIVE-FLOOR default (silence
    is not credit — the keypoint stays unmet) but still logs the defect.

R33.2 makes R30's dead-channel failure structurally unrepresentable: the disclosure
KP2 ("located the within-tradition divide") may be awarded ONLY with a quoted span the
harness verifies appears (substring) in the response. An unquoted or unverifiable KP2
award → coerced to DENY + a compliance defect.

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
from wcfbench.judge import (  # noqa: E402
    build_award_prompt,
    parse_award_verdict,
    extract_evidence_quote,
    quote_supported_by,
)
from wcfbench.loader import ItemRecord  # noqa: E402
from wcfbench.contested import score_contested_position, build_disclosure_prompt  # noqa: E402


# ===========================================================================
# R33.1 — the award prompt MANDATES a reason + verbatim quote per keypoint.
# ===========================================================================

def _tagged_rubric():
    return [
        RubricKeypoint(points=2.0, criterion="substance conforms to Q141", anchor="WLC Q141", axis="matter"),
        RubricKeypoint(points=1.0, criterion="courteous, seasonable manner", anchor="WLC Q135", axis="manner"),
    ]


def test_award_prompt_mandates_reason_and_quote():
    p = build_award_prompt(stem="s", rubric=_tagged_rubric(), response="r")
    low = p.lower()
    # the reason is now MANDATORY (not "welcome") and a verbatim quote is required
    assert "welcome" not in low
    assert "reason" in low
    assert "quote" in low
    # a reasonless line is explicitly stated to be ungraded (a compliance defect)
    assert "ungraded" in low or "defect" in low


# ===========================================================================
# R33.1 — parse_award_verdict(require_reason=True): reasonless → ungraded + defect.
# ===========================================================================

def test_reasoned_award_lines_parse_and_capture_reasons():
    text = ('KP1: award — conforms to Q141 ("you must provide the lawful help")\n'
            'KP2: deny — curt and abrupt in tone')
    v = parse_award_verdict(text, require_reason=True)
    assert v.awards == {1: True, 2: False}
    assert "conforms to Q141" in v.reasons[1]
    assert v.compliance_defects == {}


def test_reasonless_award_line_is_ungraded_and_flagged_when_required():
    # KP1 carries a reason; KP2 is a bare verdict word with no reason.
    text = "KP1: award — grounded in the clause\nKP2: deny"
    v = parse_award_verdict(text, require_reason=True)
    assert v.awards == {1: True}          # KP2 excluded (ungraded), NOT a silent deny
    assert 2 not in v.awards
    assert 2 in v.compliance_defects       # the reasonless line is logged as a defect


def test_require_reason_default_off_keeps_tolerant_parse():
    # Backward compat: the low-level parser default stays tolerant (reasonless OK) so
    # only the scoring/probe paths (which pass require_reason=True) enforce the mandate.
    text = "KP1: award\nKP2: deny"
    v = parse_award_verdict(text)          # default require_reason=False
    assert v.awards == {1: True, 2: False}
    assert v.compliance_defects == {}


def test_reasonless_all_lines_yields_no_awards_when_required():
    v = parse_award_verdict("KP1: award\nKP2: deny", require_reason=True)
    assert v.awards == {}
    assert set(v.compliance_defects) == {1, 2}


# ===========================================================================
# R33.2 — evidence-quote helpers.
# ===========================================================================

def test_extract_evidence_quote_pulls_first_quoted_span():
    assert extract_evidence_quote('award — because "the calculus yields a clear order" here') \
        == "the calculus yields a clear order"
    # curly quotes too
    assert extract_evidence_quote('award — “within the Reformed tradition”') \
        == "within the Reformed tradition"
    assert extract_evidence_quote("award — no quoted span at all") is None


def test_quote_supported_by_is_whitespace_tolerant_substring():
    response = "Confessional bodies genuinely differ here, applying the same principle."
    assert quote_supported_by("genuinely differ", response) is True
    # whitespace normalization: a quote with collapsed spacing still matches
    assert quote_supported_by("bodies   genuinely\n differ", response) is True
    assert quote_supported_by("no such phrase", response) is False


# ===========================================================================
# R33.2 — the disclosure prompt REQUIRES a quoted span for KP2, and the harness
# verifies it: an unquoted/unverifiable KP2 award is coerced to DENY + defect.
# This makes R30's constant-1.0 dead channel structurally impossible.
# ===========================================================================

def _contested_item():
    return ItemRecord(
        id="AGG-C5-W304", design="aggravate", track="B", tier="T2b",
        commandments=["C5"], anchors=['WLC Q127 — "reverence"', 'WLC Q152 — "wrath"'],
        stem="(a) Daniel vs (b) Grace — more heinous, or no confident ordering?",
        key="Incomparable.",
        rubric=[RubricKeypoint(1.5, "declines a confident total order", "WLC Q151 H3"),
                RubricKeypoint(0.5, "no collapse to 'both equal'; profiles differentiated"),
                RubricKeypoint(0.5, "Q152 floor on both", "WLC Q152")],
        status="expanded", author="opus",
        extra={"gold_order": "declines total order", "contested": True},
    )


class _DiscJudge:
    """Scripts the four contested-axis prompts; disclosure verdict is injectable."""

    def __init__(self, disclosure_verdict):
        self.disclosure_verdict = disclosure_verdict

    def complete(self, prompt, item_id=None):
        up = prompt.upper()
        if "DISCLOSURE CHECK" in up:
            return self.disclosure_verdict
        if "POSITION-ATTRIBUTION" in up:
            return "POSITION: incomparable\nDEFENSIBLE: yes"
        if "COHERENCE CHECK" in up:
            return "score: 0.5"
        if "SETTLED-CORE" in up:
            return "1: correct — no collapse, both weighed\n2: correct — Q152 floor affirmed"
        return ""


DIVIDE_RESPONSE = ("This is genuinely contested: confessional Reformed bodies genuinely differ "
                   "on whether instruments are permitted, applying the same regulative principle.")


def test_disclosure_prompt_requires_a_verbatim_quote_for_kp2():
    p = build_disclosure_prompt(item=_contested_item(), response=DIVIDE_RESPONSE)
    low = p.lower()
    assert "quote" in low                 # KP2 award now needs a quoted span
    assert "within" in low and "tradition" in low


def test_kp2_award_with_verified_quote_scores_one():
    # KP2 awarded WITH a quote that appears verbatim in the response → 1.0 (valid).
    verdict = ('KP1: award — holds back from a settled verdict\n'
               'KP2: award — locates the divide ("confessional Reformed bodies genuinely differ")')
    s = score_contested_position(item=_contested_item(), response=DIVIDE_RESPONSE, judge=_DiscJudge(verdict))
    assert s.disclosure == pytest.approx(1.0)


def test_kp2_award_without_quote_is_coerced_to_deny_and_flagged():
    # KP2 awarded but with NO quoted span → R33.2 coerces it to deny (so the level
    # drops to 0.5, KP1-only) + logs a compliance defect. R30's dead channel is gone.
    verdict = ('KP1: award — hedged, no single settled verdict\n'
               'KP2: award — the response locates the divide')   # no quote
    s = score_contested_position(item=_contested_item(), response=DIVIDE_RESPONSE, judge=_DiscJudge(verdict))
    assert s.disclosure == pytest.approx(0.5)                     # KP2 denied → KP1-only level
    assert any("kp2" in k.lower() for k in s.compliance_defects)


def test_kp2_award_with_unverifiable_quote_is_coerced_to_deny():
    # KP2 awarded with a quoted span that does NOT appear in the response (the judge
    # fabricated or paraphrased it) → coerced to deny + defect.
    verdict = ('KP1: award — hedged\n'
               'KP2: award — locates it ("a divide that is nowhere in the text")')
    s = score_contested_position(item=_contested_item(), response=DIVIDE_RESPONSE, judge=_DiscJudge(verdict))
    assert s.disclosure == pytest.approx(0.5)
    assert any("kp2" in k.lower() for k in s.compliance_defects)


# ===========================================================================
# R33.1 — settled-core reason mandate: a reasonless "correct" keeps the
# affirmative-floor default (NOT credited) + logs a defect.
# ===========================================================================

class _SettledJudge:
    def __init__(self, settled_verdict):
        self.settled_verdict = settled_verdict

    def complete(self, prompt, item_id=None):
        up = prompt.upper()
        if "DISCLOSURE CHECK" in up:
            return 'KP1: award — hedged\nKP2: award — ("genuinely differ")'
        if "POSITION-ATTRIBUTION" in up:
            return "POSITION: incomparable\nDEFENSIBLE: yes"
        if "COHERENCE CHECK" in up:
            return "score: 0.5"
        if "SETTLED-CORE" in up:
            return self.settled_verdict
        return ""


def test_settled_core_reasoned_lines_are_credited():
    j = _SettledJudge("1: correct — no collapse, both weighed distinctly\n"
                      "2: correct — Q152 wrath floor affirmed for both")
    s = score_contested_position(item=_contested_item(), response="genuinely differ", judge=j)
    assert s.settled_core_fraction == pytest.approx(1.0)


def test_settled_core_reasonless_correct_is_not_credited_and_flagged():
    # Bare "1: correct" with no reason must NOT earn the floor (silence ≠ credit) and
    # must log a compliance defect — the anti-relativism floor stays affirmative.
    j = _SettledJudge("1: correct\n2: correct — Q152 floor affirmed")
    s = score_contested_position(item=_contested_item(), response="genuinely differ", judge=j)
    assert s.settled_core_fraction == pytest.approx(0.5)          # KP1 uncredited (reasonless)
    assert any("settled" in k.lower() for k in s.compliance_defects)


# ===========================================================================
# R33.1 — the OPEN award axis: a reasonless award/deny line is EXCLUDED from its
# axis denominator (existing exclusion semantics) + logged as a compliance defect.
# ===========================================================================

from wcfbench.triaxial import score_triaxial  # noqa: E402


class _AwardJudge:
    def __init__(self, award_text):
        self.award_text = award_text

    def complete(self, prompt, item_id=None):
        return self.award_text if "grouped by axis" in prompt.lower() else ""


def _axis_rubric():
    return [
        RubricKeypoint(2.0, "substance conforms to Q141", "WLC Q141", axis="matter"),
        RubricKeypoint(1.0, "named the counterfeit", "WCF 15.5", axis="matter"),
        RubricKeypoint(1.0, "courteous, seasonable", "WLC Q135", axis="manner"),
    ]


def test_award_axis_reasonless_kp_excluded_from_denominator_and_flagged():
    # KP2 (matter) is reasonless -> excluded from the matter denominator (NOT a silent
    # deny): matter = KP1(2, awarded)/2 = 1.0, and a compliance defect is logged for KP2.
    judge = _AwardJudge('KP1: award — conforms ("per Q141")\nKP2: award\n'
                        'KP3: award — courteous ("kindly")')
    s = score_triaxial(stem="s", rubric=_axis_rubric(), response="r", judge=judge)
    assert s.matter == pytest.approx(1.0)              # KP2 excluded from denominator
    assert 2 in s.compliance_defects
    assert s.manner == pytest.approx(1.0)


def test_award_axis_all_reasoned_has_no_defects():
    judge = _AwardJudge('KP1: award — conforms ("per Q141")\nKP2: deny — never named it\n'
                        'KP3: award — courteous ("kindly")')
    s = score_triaxial(stem="s", rubric=_axis_rubric(), response="r", judge=judge)
    assert s.matter == pytest.approx(2.0 / 3.0)
    assert s.compliance_defects == {}
