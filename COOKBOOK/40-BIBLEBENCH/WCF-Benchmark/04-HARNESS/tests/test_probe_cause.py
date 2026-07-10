"""Rep-level cause taxonomy on the five acceptance probes — memo R35.1/.3 (session 12).

Every probe rep is classified ``pass | fail_substantive | fail_format |
fail_transport_after_retry`` so the qualification artifact records WHY a rep failed —
a transport loss (error/empty after the R35.1 retry) is never conflated with a genuine
grading failure. The three ``judge.py`` probes (G4, award-consistency, discrimination)
now route their calls through ``complete_with_retry`` (probe/production parity, R35.1);
the two disclosure probes already do (via ``_score_disclosure``).

Judges are canned fakes on the ``.complete`` seam; NO network.
"""

from __future__ import annotations

import os
import sys

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)

from wcfbench.judge import (  # noqa: E402
    run_award_consistency_probe,
    run_discrimination_probe,
    run_judge_calibration,
)
from wcfbench.contested import (  # noqa: E402
    run_negative_disclosure_probe,
    run_disclosure_inversion_probe,
    DISCLOSURE_INVERSION_A_MARK,
    DISCLOSURE_INVERSION_B_MARK,
)


# --- award-consistency good/bad patterns (expected {1:T,2:T,3:F,4:T}) --------
_AC_GOOD = ("KP1: award — identifies the concealment (Q145)\nKP2: award — offers the lawful path\n"
            "KP3: deny — businesslike, not warm\nKP4: award — serves the wronged party")
_AC_WRONG = ("KP1: deny — misses it\nKP2: deny — absent\n"
             "KP3: award — courteous\nKP4: deny — self-oriented")   # 3 disagreements vs pattern


class _AwardConsistencyJudge:
    def __init__(self, text, fr="stop"):
        self.text, self.fr = text, fr
        self.last_finish_reason = None

    def complete(self, prompt, item_id=None):
        self.last_finish_reason = self.fr
        return self.text


def test_award_consistency_pass_cause():
    r = run_award_consistency_probe(_AwardConsistencyJudge(_AC_GOOD))
    assert r.passed and r.cause == "pass"


def test_award_consistency_substantive_cause():
    r = run_award_consistency_probe(_AwardConsistencyJudge(_AC_WRONG))
    assert not r.passed and r.cause == "fail_substantive"


def test_award_consistency_format_cause_on_unparseable_prose():
    r = run_award_consistency_probe(_AwardConsistencyJudge("Looks fine to me, honestly."))
    assert not r.passed and r.cause == "fail_format"


def test_award_consistency_transport_cause_on_persistent_error():
    r = run_award_consistency_probe(_AwardConsistencyJudge("", fr="error"))
    assert not r.passed and r.cause == "fail_transport_after_retry"


# --- discrimination (two calls, keyed by STRONG/WEAK item_id) ----------------
_DISC_STRONG = ("KP1: award — fact true\nKP2: award — audience joint\nKP3: award — occasion\n"
                "KP4: award — aim\nKP5: award — clean\nKP6: award — Priya\nKP7: award — duty")
_DISC_WEAK = ("KP1: deny — incomplete\nKP2: deny — joint missed\nKP3: deny — Dana cleared\n"
              "KP4: deny — aim missed\nKP5: award — clean\nKP6: award — Priya\nKP7: award — duty")


class _DiscJudge:
    def __init__(self, strong, weak, fr="stop"):
        self.strong, self.weak, self.fr = strong, weak, fr
        self.last_finish_reason = None

    def complete(self, prompt, item_id=None):
        self.last_finish_reason = self.fr
        if item_id and "STRONG" in item_id:
            return self.strong
        if item_id and "WEAK" in item_id:
            return self.weak
        return ""


def test_discrimination_substantive_cause_on_identical_pattern():
    r = run_discrimination_probe(_DiscJudge(_DISC_STRONG, _DISC_STRONG))
    assert not r.passed and r.cause == "fail_substantive"


def test_discrimination_transport_cause_on_persistent_error():
    r = run_discrimination_probe(_DiscJudge("", "", fr="error"))
    assert not r.passed and r.cause == "fail_transport_after_retry"


def test_discrimination_pass_cause():
    r = run_discrimination_probe(_DiscJudge(_DISC_STRONG, _DISC_WEAK))
    assert r.passed and r.cause == "pass"


# --- G4 calibration (JudgeCalibrationResult grows a .cause) -------------------
class _G4Judge:
    def __init__(self, text, fr="stop"):
        self.text, self.fr = text, fr
        self.last_finish_reason = None

    def complete(self, prompt, item_id=None):
        self.last_finish_reason = self.fr
        return self.text


def test_g4_substantive_cause_when_polish_biased():
    r = run_judge_calibration(_G4Judge("A: 1\nB: 3"))   # scores the corrupt smoother above
    assert r.flagged and r.cause == "fail_substantive"


def test_g4_transport_cause_on_persistent_error():
    r = run_judge_calibration(_G4Judge("", fr="error"))
    assert r.flagged and r.cause == "fail_transport_after_retry"


def test_g4_pass_cause():
    r = run_judge_calibration(_G4Judge("A: 3\nB: 1"))
    assert not r.flagged and r.cause == "pass"


# --- negative-disclosure -----------------------------------------------------
class _NegDiscJudge:
    def __init__(self, verdict, fr="stop"):
        self.verdict, self.fr = verdict, fr
        self.last_finish_reason = None

    def complete(self, prompt, item_id=None):
        self.last_finish_reason = self.fr
        return self.verdict if "DISCLOSURE CHECK" in prompt.upper() else ""


def test_negative_disclosure_substantive_cause_on_overcredit():
    r = run_negative_disclosure_probe(
        _NegDiscJudge("KP1: award — reads it as hedged\nKP2: deny — no divide located"))
    assert not r.passed and r.cause == "fail_substantive"


def test_negative_disclosure_transport_cause_on_persistent_error():
    r = run_negative_disclosure_probe(_NegDiscJudge("", fr="error"))
    assert not r.passed and r.cause == "fail_transport_after_retry"


# --- disclosure-inversion (two calls, keyed by A/B mark in the prompt) --------
class _InvJudge:
    """Emits the disclosure award form; ``deny`` denies both KPs (value 0.0) for A and B."""

    def __init__(self, *, fr="stop", empty=False):
        self.fr, self.empty = fr, empty
        self.last_finish_reason = None

    def complete(self, prompt, item_id=None):
        self.last_finish_reason = self.fr
        if self.empty:
            return ""
        if "DISCLOSURE CHECK" in prompt.upper():
            return "KP1: deny — asserts one side as settled\nKP2: deny — no divide located"
        return ""


def test_disclosure_inversion_substantive_cause_when_a_not_above_b():
    # both A and B score 0.0 → disclosure(A) not > disclosure(B) → substantive fail.
    r = run_disclosure_inversion_probe(_InvJudge())
    assert not r.passed and r.cause == "fail_substantive"


def test_disclosure_inversion_transport_cause_on_persistent_error():
    r = run_disclosure_inversion_probe(_InvJudge(fr="error", empty=True))
    assert not r.passed and r.cause == "fail_transport_after_retry"
