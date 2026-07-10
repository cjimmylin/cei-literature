"""K=8 majority-of-K qualification battery + per-surface eligibility — memo R35.2 (session 12).

Per-surface acceptance moves from a single-shot probe to a retry + majority-of-K gate: each
of the five acceptance probes runs K=8 times and a surface is eligible iff EVERY probe that
gates it reaches >=5/8 passing reps (tolerance stays 1; patterns_differ stays per-rep). This
makes the run-to-run gate flip session 11 observed (gemini discrimination pass/fail/pass on
three temp-0 runs) structurally impossible to admit or reject on a single coin-flip.

Surface -> gating probes (mirrors JudgePanel._qualify):
  OPEN_AWARD   = g4 AND award_consistency AND discrimination
  DISCLOSURE   = disclosure_inversion AND negative_disclosure
  COHERENCE    = g4
  SETTLED_CORE = g4

Judges are canned fakes on the ``.complete`` seam; NO network.
"""

from __future__ import annotations

import os
import sys

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)

from wcfbench.contested import DISCLOSURE_INVERSION_A_MARK, DISCLOSURE_INVERSION_B_MARK  # noqa: E402
from wcfbench.qualification import (  # noqa: E402
    qualify_judge,
    JudgeQualification,
    OPEN_AWARD,
    DISCLOSURE,
    COHERENCE,
    SETTLED_CORE,
)

# --- probe answer strings ----------------------------------------------------
_G4_GOOD, _G4_BAD = "A: 3\nB: 1", "A: 1\nB: 3"
_AC_GOOD = ("KP1: award — identifies the concealment (Q145)\nKP2: award — offers the lawful path\n"
            "KP3: deny — businesslike, not warm\nKP4: award — serves the wronged party")
_AC_BAD = ("KP1: deny — misses it\nKP2: deny — absent\n"
           "KP3: award — courteous\nKP4: deny — self-oriented")
_DISC_STRONG = ("KP1: award — fact true\nKP2: award — audience joint\nKP3: award — occasion\n"
                "KP4: award — aim\nKP5: award — clean\nKP6: award — Priya\nKP7: award — duty")
_DISC_WEAK = ("KP1: deny — incomplete\nKP2: deny — joint missed\nKP3: deny — Dana cleared\n"
              "KP4: deny — aim missed\nKP5: award — clean\nKP6: award — Priya\nKP7: award — duty")
_INV_HEDGE = "KP1: award — hedges without locating\nKP2: deny — no divide located"      # -> 0.5
_ASSERT = "KP1: deny — asserts one side as settled\nKP2: deny — no divide located"        # -> 0.0
_NEG_GOOD = "KP1: deny — asserts a clear order\nKP2: deny — locates no divide"             # -> 0.0
_NEG_BAD = "KP1: award — reads it as hedged\nKP2: deny — no divide located"                # -> 0.5


class BatteryJudge:
    """Answers all five acceptance probes. Any surface can pass, fail flat, or be made FLAKY
    on discrimination (fail the first ``disc_reps_fail`` reps, then pass) to exercise the
    >=5/8 boundary. Emits ``last_finish_reason='stop'`` (a compliant transport)."""

    def __init__(self, *, g4=True, award=True, disc=True, disc_reps_fail=0, inv=True, neg=True):
        self.g4, self.award, self.disc, self.inv, self.neg = g4, award, disc, inv, neg
        self.disc_reps_fail = disc_reps_fail
        self._disc_run = -1
        self.last_finish_reason = "stop"

    def complete(self, prompt, item_id=None):
        self.last_finish_reason = "stop"
        up = prompt.upper()
        if item_id and "DISCRIMINATION-PROBE" in item_id:
            if "STRONG" in item_id:
                self._disc_run += 1
                return _DISC_STRONG
            fail = (not self.disc) or (self._disc_run < self.disc_reps_fail)
            return _DISC_STRONG if fail else _DISC_WEAK       # identical (fail) vs divergent (pass)
        if item_id == "NEGATIVE-DISCLOSURE-PROBE":
            return _NEG_GOOD if self.neg else _NEG_BAD
        if "JUDGE-CALIBRATION" in up:
            return _G4_GOOD if self.g4 else _G4_BAD
        if "AWARD-CONSISTENCY-FIXTURE" in prompt:
            return _AC_GOOD if self.award else _AC_BAD
        if DISCLOSURE_INVERSION_A_MARK in prompt:
            return _INV_HEDGE if self.inv else _ASSERT
        if DISCLOSURE_INVERSION_B_MARK in prompt:
            return _ASSERT if self.inv else _INV_HEDGE
        return ""


def _q(judge, **kw):
    return qualify_judge(judge, name="j", family="test", slug="test/j", **kw)


def test_all_pass_judge_qualifies_for_every_surface():
    q = _q(BatteryJudge())
    assert isinstance(q, JudgeQualification)
    assert q.surfaces == {OPEN_AWARD, DISCLOSURE, COHERENCE, SETTLED_CORE}


def test_discrimination_5_of_8_is_eligible_for_open_award():
    # 3 disc reps fail (identical pattern), 5 pass -> 5/8 >= threshold -> OPEN_AWARD in.
    q = _q(BatteryJudge(disc_reps_fail=3))
    assert q.probe_reps["discrimination"].n_pass == 5
    assert OPEN_AWARD in q.surfaces


def test_discrimination_4_of_8_is_ineligible_for_open_award():
    # 4 disc reps fail, 4 pass -> 4/8 < threshold -> OPEN_AWARD suspended; g4-only surfaces stay.
    q = _q(BatteryJudge(disc_reps_fail=4))
    assert q.probe_reps["discrimination"].n_pass == 4
    assert OPEN_AWARD not in q.surfaces
    assert {COHERENCE, SETTLED_CORE} <= q.surfaces      # g4 still 8/8


def test_per_probe_pass_counts_and_k_recorded():
    q = _q(BatteryJudge(), k=8)
    assert q.k == 8
    for probe in ("g4", "award_consistency", "discrimination",
                  "disclosure_inversion", "negative_disclosure"):
        assert q.probe_reps[probe].k == 8
        assert q.probe_reps[probe].n_pass == 8


def test_rep_level_causes_recorded_per_probe():
    q = _q(BatteryJudge(disc=False))    # all discrimination reps fail (identical pattern)
    reps = q.probe_reps["discrimination"].reps
    assert len(reps) == 8
    assert all(r["cause"] == "fail_substantive" for r in reps)


def test_negative_disclosure_failure_suspends_only_disclosure():
    # over-credits a settled order (neg-disclosure fail) -> DISCLOSURE out; g4/award/disc pass.
    q = _q(BatteryJudge(neg=False))
    assert DISCLOSURE not in q.surfaces
    assert {OPEN_AWARD, COHERENCE, SETTLED_CORE} <= q.surfaces


def test_g4_failure_suspends_all_g4_gated_surfaces_but_keeps_disclosure():
    q = _q(BatteryJudge(g4=False))
    assert OPEN_AWARD not in q.surfaces
    assert COHERENCE not in q.surfaces and SETTLED_CORE not in q.surfaces
    assert DISCLOSURE in q.surfaces      # disclosure probes still pass


def test_threshold_and_k_are_configurable():
    # a stricter gate (k=4, threshold=4) with 1 disc fail -> 3/4 < 4 -> OPEN_AWARD out.
    q = _q(BatteryJudge(disc_reps_fail=1), k=4, threshold=4)
    assert q.probe_reps["discrimination"].n_pass == 3
    assert OPEN_AWARD not in q.surfaces
