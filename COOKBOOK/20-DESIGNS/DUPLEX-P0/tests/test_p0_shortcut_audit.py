"""X2 shortcut audit: lexical baseline ~ chance, fine-tune probe interface, combined verdict."""
import pytest

from analysis.shortcut_audit import (
    lexical_length_baseline,
    FineTuneProbe,
    combined_shortcut_verdict,
)


def test_lexical_baseline_near_chance_on_balanced_bank():
    # length is uncorrelated with label -> best single-threshold accuracy ~ chance
    items = [
        {"text": "x " * 10, "label": 0},
        {"text": "x " * 10, "label": 1},
        {"text": "x " * 40, "label": 0},
        {"text": "x " * 40, "label": 1},
        {"text": "x " * 25, "label": 0},
        {"text": "x " * 25, "label": 1},
    ]
    res = lexical_length_baseline(items, tol=0.2)
    assert res["chance"] == 0.5
    assert res["near_chance"] is True


def test_lexical_baseline_detects_length_leak():
    # length perfectly predicts the label -> lexical baseline BEATS chance -> not near chance
    items = [
        {"text": "short", "label": 0},
        {"text": "short", "label": 0},
        {"text": "a very very very long leaking item text", "label": 1},
        {"text": "a very very very long leaking item text", "label": 1},
    ]
    res = lexical_length_baseline(items, tol=0.1)
    assert res["lexical_accuracy"] > res["chance"]
    assert res["near_chance"] is False


def test_fine_tune_probe_run_is_not_implemented():
    probe = FineTuneProbe(fraction=0.10)
    with pytest.raises(NotImplementedError):
        probe.run([{"text": "x", "label": 0}])


def test_fine_tune_probe_verdict_rule():
    probe = FineTuneProbe(parity_margin=0.02)
    below = probe.verdict_from_accuracies(probe_accuracy=0.60, sota_accuracy=0.85)
    assert below["below_parity"] is True
    at_parity = probe.verdict_from_accuracies(probe_accuracy=0.86, sota_accuracy=0.85)
    assert at_parity["below_parity"] is False


def test_combined_verdict_requires_both():
    assert combined_shortcut_verdict(True, True)["pass"] is True
    assert combined_shortcut_verdict(True, False)["pass"] is False
    assert combined_shortcut_verdict(False, True)["pass"] is False
    # probe not yet run -> incomplete, never silently True
    incomplete = combined_shortcut_verdict(True, None)
    assert incomplete["pass"] is None
    assert "incomplete" in incomplete["status"]
