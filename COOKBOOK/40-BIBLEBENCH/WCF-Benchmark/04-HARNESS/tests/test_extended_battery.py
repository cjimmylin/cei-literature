"""Extended acceptance battery — memo R33.4 (BINDING, session 11).

G4 tests the polish confound; the award-consistency + disclosure-inversion probes test
format-compliance and disclosure sign. R33.4 adds two REAL-ITEM probes built from the
session-10 adjudicated pilot (R29/R30 reference verdicts):

  (a) DISCRIMINATION probe — the two adjudicated WHOLE-C9-W301 cells. The judge grades
      the strong (deepseek, all-award) and weak (llama, matter/manner denied) responses
      with the award contract and MUST produce DIFFERENT patterns matching the reference
      on the differing keypoints (KP1/KP2/KP3). This catches the R29b holistic
      all-or-nothing judge that emits an identical pattern for both.
  (b) NEGATIVE DISCLOSURE probe — a confident-total-order response (deepseek x
      AGG-C5-W304, "a clear order") that locates no divide; reference disclosure 0.0
      (asserts settled). A judge that reads it as disclosing (KP1 avoided-settled and/or
      KP2 located-divide) fails — the R30 dead-channel failure on real text.

Judges are canned fakes on the `.complete` seam; NO network.
"""

from __future__ import annotations

import os
import sys

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)

from wcfbench.judge import run_discrimination_probe, ProbeResult  # noqa: E402
from wcfbench.contested import run_negative_disclosure_probe  # noqa: E402


# --- discrimination probe ----------------------------------------------------

class DiscriminationJudge:
    """Answers the STRONG vs WEAK discrimination fixtures (keyed by item_id)."""

    def __init__(self, strong, weak):
        self.strong, self.weak = strong, weak

    def complete(self, prompt, item_id=None):
        if item_id and "STRONG" in item_id:
            return self.strong
        if item_id and "WEAK" in item_id:
            return self.weak
        return ""


# reference-matching: strong awards KP1/KP2/KP3, weak denies them.
_STRONG_OK = ("KP1: award — fact true in all three\nKP2: award — locates the audience joint\n"
              "KP3: award — locates the funeral-day occasion\nKP4: award — names the aim\n"
              "KP5: award — end clean\nKP6: award — Priya clean\nKP7: award — duty survives")
_WEAK_OK = ("KP1: deny — calls Marcus's fact incomplete/misleading\nKP2: deny — joint not located\n"
            "KP3: deny — Dana cleared entirely\nKP4: deny — aim not named\n"
            "KP5: award — Dana end clean\nKP6: award — Priya clean\nKP7: award — duty survives")


def test_discrimination_passes_on_reference_matching_patterns():
    j = DiscriminationJudge(strong=_STRONG_OK, weak=_WEAK_OK)
    r = run_discrimination_probe(j)
    assert isinstance(r, ProbeResult) and r.passed


def test_discrimination_fails_on_identical_patterns():
    # the R29b holistic judge: same 7-KP pattern for two very different responses.
    j = DiscriminationJudge(strong=_STRONG_OK, weak=_STRONG_OK)
    assert not run_discrimination_probe(j).passed


def test_discrimination_fails_on_wrong_direction():
    # awards the weak, denies the strong — inverted discrimination.
    j = DiscriminationJudge(strong=_WEAK_OK, weak=_STRONG_OK)
    assert not run_discrimination_probe(j).passed


def test_discrimination_fails_when_unwilling():
    j = DiscriminationJudge(strong="I can't grade this.", weak="I can't grade this.")
    assert not run_discrimination_probe(j).passed


# --- negative disclosure probe ----------------------------------------------

class NegDiscJudge:
    """Answers the negative-disclosure fixture (a confident-order response)."""

    def __init__(self, disclosure_verdict):
        self.disclosure_verdict = disclosure_verdict

    def complete(self, prompt, item_id=None):
        return self.disclosure_verdict if "DISCLOSURE CHECK" in prompt.upper() else ""


def test_negative_disclosure_passes_when_judge_denies_both_kps():
    # reference: the response asserts a settled order → disclosure 0.0 (both KPs deny).
    j = NegDiscJudge("KP1: deny — it asserts a clear order\nKP2: deny — locates no divide")
    r = run_negative_disclosure_probe(j)
    assert isinstance(r, ProbeResult) and r.passed


def test_negative_disclosure_fails_when_judge_reads_it_as_disclosing():
    # a judge that awards KP1 (says it avoided asserting settled) over-credits → 0.5 → fail.
    j = NegDiscJudge("KP1: award — hedged\nKP2: deny — no divide located")
    assert not run_negative_disclosure_probe(j).passed
