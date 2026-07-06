"""Tests for the portfolio-wide X2 shortcut/gaming audit (KB04 §6 item 5).

Mandatory for any published procedural generator: a lexical/length/word-
averaging baseline must sit ~ chance, and a 10%-fine-tune probe must NOT reach
parity (parity => exploitable template surface). Both are pre-registered
go/no-go gates. This tooling is built once and reused by every CRUX-family
design.
"""
import pytest

from crux import shortcut_audit as sa


def _clean_items():
    # Label is INDEPENDENT of surface: identical text, alternating labels.
    return [{"text": "a neutral vignette of fixed length", "label": i % 2}
            for i in range(20)]


def _length_leaky_items():
    # Label is PERFECTLY encoded by length / vocabulary — an exploitable shortcut.
    short = [{"text": "tiny short quick word", "label": 0} for _ in range(10)]
    long = [{"text": "enormous verbose elaborate paragraph " * 8, "label": 1}
            for _ in range(10)]
    return short + long


def test_chance_level_is_majority_class_proportion():
    labels = [0, 0, 0, 1]
    assert sa.chance_level(labels) == pytest.approx(0.75)


def test_lexical_baseline_sits_at_chance_on_clean_items():
    res = sa.lexical_length_baseline(_clean_items())
    assert res.near_chance
    assert res.accuracy == pytest.approx(res.chance, abs=res.tolerance)


def test_lexical_baseline_catches_a_length_leaky_shortcut():
    res = sa.lexical_length_baseline(_length_leaky_items())
    assert not res.near_chance
    assert res.accuracy > res.chance + res.tolerance


def test_fine_tune_probe_requires_a_trainer_by_default():
    probe = sa.FineTuneProbe()  # no trainer wired
    with pytest.raises(NotImplementedError):
        probe.run(_clean_items(), full_model_accuracy=0.8)


def test_fine_tune_probe_uses_injected_trainer_and_flags_parity():
    # trainer that reports the probe reaching the full model's accuracy = parity
    at_parity = sa.FineTuneProbe(trainer=lambda items, frac: 0.80)
    r1 = at_parity.run(_clean_items(), full_model_accuracy=0.80)
    assert not r1.below_parity

    below = sa.FineTuneProbe(trainer=lambda items, frac: 0.55)
    r2 = below.run(_clean_items(), full_model_accuracy=0.80)
    assert r2.below_parity


def test_x2_gate_passes_only_when_lexical_chance_and_probe_below_parity():
    clean = sa.lexical_length_baseline(_clean_items())
    below = sa.FineTuneProbe(trainer=lambda items, frac: 0.55).run(
        _clean_items(), full_model_accuracy=0.80)
    assert sa.x2_gate(clean, below)["pass"] is True

    leaky = sa.lexical_length_baseline(_length_leaky_items())
    assert sa.x2_gate(leaky, below)["pass"] is False

    at_parity = sa.FineTuneProbe(trainer=lambda items, frac: 0.80).run(
        _clean_items(), full_model_accuracy=0.80)
    assert sa.x2_gate(clean, at_parity)["pass"] is False
