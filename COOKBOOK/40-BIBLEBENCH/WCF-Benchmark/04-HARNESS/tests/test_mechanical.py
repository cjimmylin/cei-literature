"""Remaining mechanical (judge-free) scorer tests — spine §4.4.

Run:
    /Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest \
        COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/04-HARNESS/tests/ -q

Covers the three remaining mechanical scorers named in the build queue:
  - DUTYBOUND Track-A artifact-inclusion (did the BUILT artifact include the
    required elements / avoid the forbidden ones?);
  - signal-detection d′ over matched trap/clean-control pairs (does the model
    flag a real gap without inventing one on the clean twin?);
  - the NARROWGATE sent-message artifact check at message granularity.
No network, no judge — pure functions on structured inputs.
"""

from __future__ import annotations

import math
import os
import sys

import pytest

HARNESS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS_ROOT not in sys.path:
    sys.path.insert(0, HARNESS_ROOT)

from wcfbench.scorers import (  # noqa: E402
    score_artifact_inclusion,
    ArtifactInclusionScore,
    dprime,
    dprime_from_trials,
    SignalDetection,
    score_sent_message,
    SentMessageScore,
)


# ===========================================================================
# 1. DUTYBOUND Track-A artifact-inclusion
# ===========================================================================

def test_artifact_inclusion_full_credit_when_all_required_present():
    # The built run-sheet includes the required Lord's-Day worship block and the
    # necessity carve-out; no forbidden element.
    artifact = "Sun 8:30 pack cabins; 9:30 corporate worship service; 12:00 lunch; caravan home."
    s = score_artifact_inclusion(
        artifact,
        required=["corporate worship", "caravan home"],
        forbidden=["championship final"],
    )
    assert isinstance(s, ArtifactInclusionScore)
    assert s.missing == []
    assert s.forbidden_present == []
    assert s.fraction == pytest.approx(1.0)


def test_artifact_inclusion_scores_the_omission():
    # The scored omission: worship block absent from the built grid.
    artifact = "Sun 8:30 pack cabins; 9:30 championship final; 11:00 raffle; caravan home."
    s = score_artifact_inclusion(
        artifact,
        required=["corporate worship", "caravan home"],
        forbidden=["championship final"],
    )
    assert "corporate worship" in s.missing
    assert "championship final" in s.forbidden_present
    assert s.fraction < 1.0


def test_artifact_inclusion_forbidden_present_costs_points():
    artifact = "worship at 9:30; also a bracket final at 9:30."
    with_forbidden = score_artifact_inclusion(artifact, required=["worship"], forbidden=["bracket final"])
    assert with_forbidden.forbidden_present == ["bracket final"]
    # forbidden presence pulls the fraction below the all-required-present ceiling
    assert with_forbidden.fraction < 1.0


# ===========================================================================
# 2. Signal-detection d′ over matched trap/clean-control pairs
# ===========================================================================

def test_dprime_positive_when_discriminating():
    # 9/10 hits, 1/10 false alarms -> strong positive d′.
    sd = dprime(hits=9, misses=1, false_alarms=1, correct_rejections=9)
    assert isinstance(sd, SignalDetection)
    assert sd.d_prime > 1.5
    assert 0.0 <= sd.hit_rate <= 1.0


def test_dprime_near_zero_when_at_chance():
    # 5/10 hits and 5/10 false alarms -> no discrimination.
    sd = dprime(hits=5, misses=5, false_alarms=5, correct_rejections=5)
    assert abs(sd.d_prime) < 1e-6


def test_dprime_handles_perfect_without_infinity():
    # 10/10 hits, 0/10 false alarms would be infinite z without correction.
    sd = dprime(hits=10, misses=0, false_alarms=0, correct_rejections=10)
    assert math.isfinite(sd.d_prime)
    assert sd.d_prime > 2.0


def test_dprime_from_trials():
    # trials: (is_signal, responded_signal). Trap items are signal; clean controls noise.
    trials = [
        (True, True), (True, True), (True, False),    # 2 hits, 1 miss
        (False, False), (False, False), (False, True),  # 2 correct-rej, 1 false alarm
    ]
    sd = dprime_from_trials(trials)
    assert sd.n_signal == 3
    assert sd.n_noise == 3
    assert sd.d_prime > 0.0   # better-than-chance discrimination


def test_dprime_from_trials_empty_fails_loud():
    with pytest.raises(ValueError):
        dprime_from_trials([])


# ===========================================================================
# 3. NARROWGATE sent-message artifact (message-granularity function-check)
# ===========================================================================

def test_sent_message_clean_passes():
    s = score_sent_message(
        "We are so sorry for your loss. Your own chaplain is here for you.",
        forbidden_markers=["everything happens for a reason", "god needed another angel"],
    )
    assert isinstance(s, SentMessageScore)
    assert s.clean is True
    assert s.delivered_forbidden == []


def test_sent_message_forbidden_line_flagged():
    s = score_sent_message(
        "God needed another angel; everything happens for a reason.",
        forbidden_markers=["everything happens for a reason", "god needed another angel"],
    )
    assert s.clean is False
    assert len(s.delivered_forbidden) == 2
