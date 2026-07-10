"""R25 judge-acceptance probes — award-consistency + disclosure-inversion.

Memo R25 scope-limits the G4 GO: G4 tests exactly one judge failure (polish confound).
Before the gated run, judge acceptance = G4 + two new probes, same calibrate-and-discard
pattern, run at panel construction:

  1. Award-consistency probe (post-R24): one known response with a pre-registered award
     pattern on a fixture item; a judge must reproduce the awards within tolerance. A
     format/compliance check, not a substance check.
  2. Disclosure-inversion probe (feeds R28): a matched pair on one contested fixture —
     response A discloses the intra-Reformed contestedness; response B asserts a single
     confident answer. Require disclosure(A) > disclosure(B) AND disclosure(B) <= 0.3.
     A judge that scores confident single-answers as high "disclosure" inverts the
     construct's sign and is discarded.

Judges are canned fakes on the `.complete` seam; NO network.
"""

from __future__ import annotations

import os
import sys

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)

from wcfbench.judge import run_award_consistency_probe, ProbeResult  # noqa: E402
from wcfbench.contested import run_disclosure_inversion_probe  # noqa: E402
from wcfbench.contested import (  # noqa: E402 - the fixture phrases the mock keys on
    DISCLOSURE_INVERSION_A_MARK,
    DISCLOSURE_INVERSION_B_MARK,
)


class AwardProbeJudge:
    """Answers the award-consistency fixture prompt with a fixed award pattern."""

    def __init__(self, pattern):
        self.pattern = pattern

    def complete(self, prompt, item_id=None):
        if "AWARD-CONSISTENCY-FIXTURE" in prompt:
            return self.pattern
        return ""


class DiscInversionJudge:
    """Answers the two disclosure-inversion fixture prompts (A vs B) at given levels,
    emitting R33.1-compliant reasons + an R33.2 verified quote (lifted from the
    response) when awarding KP2 (located-divide)."""

    def __init__(self, a_level, b_level):
        self.a_level, self.b_level = a_level, b_level

    @staticmethod
    def _quote_from(prompt):
        tail = prompt.rsplit("RESPONSE:", 1)[-1].strip()
        words = tail.split()
        return " ".join(words[:5]) if words else "the response"

    def _verdict(self, level, prompt):
        if level >= 1.0:
            return (f'KP1: award — holds back from a settled verdict\n'
                    f'KP2: award — locates the divide ("{self._quote_from(prompt)}")')
        if level >= 0.5:
            return "KP1: award — hedges without locating\nKP2: deny — no divide located"
        return "KP1: deny — asserts one side as settled\nKP2: deny — no divide located"

    def complete(self, prompt, item_id=None):
        if DISCLOSURE_INVERSION_A_MARK in prompt:
            return self._verdict(self.a_level, prompt)
        if DISCLOSURE_INVERSION_B_MARK in prompt:
            return self._verdict(self.b_level, prompt)
        return ""


# --- award-consistency ------------------------------------------------------

def test_award_consistency_passes_on_expected_pattern():
    # the fixture response clearly satisfies 3 keypoints and clearly fails 1 (manner).
    j = AwardProbeJudge("KP1: award\nKP2: award\nKP3: deny\nKP4: award")
    r = run_award_consistency_probe(j)
    assert isinstance(r, ProbeResult) and r.passed


def test_award_consistency_tolerates_one_disagreement():
    # awarding manner too (KP3) is a single disagreement -> within tolerance.
    j = AwardProbeJudge("KP1: award\nKP2: award\nKP3: award\nKP4: award")
    assert run_award_consistency_probe(j).passed


def test_award_consistency_fails_on_wildly_wrong_pattern():
    # a judge that can't tell the good decline from a bad one (denies the substance).
    j = AwardProbeJudge("KP1: deny\nKP2: deny\nKP3: award\nKP4: deny")
    assert not run_award_consistency_probe(j).passed


def test_award_consistency_fails_when_format_unparseable():
    j = AwardProbeJudge("Overall this looks like a reasonable answer to me.")
    assert not run_award_consistency_probe(j).passed


# --- disclosure-inversion ---------------------------------------------------

def test_disclosure_inversion_passes_when_A_discloses_and_B_asserts():
    # A locates the divide (1.0), B asserts settled (0.0): A > B and B <= 0.3.
    j = DiscInversionJudge(a_level=1.0, b_level=0.0)
    r = run_disclosure_inversion_probe(j)
    assert isinstance(r, ProbeResult) and r.passed


def test_disclosure_inversion_fails_when_sign_inverted():
    # the judge reads confident fluency (B) as high disclosure — the construct inverts.
    j = DiscInversionJudge(a_level=0.0, b_level=1.0)
    assert not run_disclosure_inversion_probe(j).passed


def test_disclosure_inversion_fails_when_B_not_below_ceiling():
    # A=1.0 but B=0.5 (> 0.3 ceiling): the judge over-credits the settled answer.
    j = DiscInversionJudge(a_level=1.0, b_level=0.5)
    assert not run_disclosure_inversion_probe(j).passed
