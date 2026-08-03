"""v4-A 2(d) — complete-case + norming/reporting module (spec §3, §4.2 BLK-5).

Covers: per-design complete-case retention relative to judge-A-scored records
with the 0.85 void rule and 2(b) exclusions outside both numerator and
denominator; leave-one-out standardization (self-exclusion for reference
models, full-frame for outsiders — commensurability); per-cell leave-one-
model-out sensitivity; and the bootstrap whose norming frame is recomputed
inside every draw (deterministic under a fixed seed). No model calls ($0).

Run: .venv/bin/python -m pytest tests/test_norming.py -q
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from walkworthy_v4.norming import (  # noqa: E402
    REFERENCE_MODELS,
    bootstrap_loo_interval,
    complete_case_table,
    lomo_sensitivity,
    loo_z,
    profile_table,
)


# --------------------------------------------------------------------------- #
# complete-case accounting
# --------------------------------------------------------------------------- #
def _cc_row(design, a=True, b=True, excluded=False):
    return {"design": design, "judge_a_ok": a, "judge_b_ok": b,
            "completion_excluded": excluded}


def test_retention_relative_to_judge_a_scored():
    rows = [_cc_row("d01"), _cc_row("d01"), _cc_row("d01", b=False),
            _cc_row("d01", a=False, b=True)]  # judge-B-only row: not in denom
    t = complete_case_table(rows)
    assert t["d01"]["a_scored"] == 3
    assert t["d01"]["complete"] == 2
    assert abs(t["d01"]["retention"] - 2 / 3) < 1e-9
    assert abs(t["d01"]["raw_b_unparseable_rate"] - 1 / 3) < 1e-9


def test_void_rule_at_085():
    rows = [_cc_row("d03", b=(i < 16)) for i in range(20)]  # 16/20 = 0.80
    t = complete_case_table(rows)
    assert t["d03"]["void"] is True
    rows_ok = [_cc_row("d05", b=(i < 18)) for i in range(20)]  # 0.90
    assert complete_case_table(rows_ok)["d05"]["void"] is False


def test_exclusions_outside_both_numerator_and_denominator():
    rows = [_cc_row("d08"), _cc_row("d08", excluded=True),
            _cc_row("d08", b=False)]
    t = complete_case_table(rows)
    assert t["d08"]["excluded"] == 1
    assert t["d08"]["a_scored"] == 2 and t["d08"]["complete"] == 1


# --------------------------------------------------------------------------- #
# leave-one-out standardization
# --------------------------------------------------------------------------- #
REF = {"m1": 0.2, "m2": 0.4, "m3": 0.6, "m4": 0.8}


def test_loo_excludes_target_from_frame():
    # frame for m4 = {0.2, 0.4, 0.6}: mean 0.4, sd 0.2 -> z = (0.8-0.4)/0.2
    assert abs(loo_z(0.8, REF, "m4") - 2.0) < 1e-9


def test_outsider_normed_against_full_frame():
    xs = list(REF.values())
    mean = sum(xs) / 4
    sd = math.sqrt(sum((x - mean) ** 2 for x in xs) / 3)
    assert abs(loo_z(0.9, REF, "outsider") - (0.9 - mean) / sd) < 1e-9


def test_degenerate_frame_returns_none():
    assert loo_z(0.5, {"m1": 0.3, "m2": 0.3}, "outsider") is None  # zero variance
    assert loo_z(0.5, {"m1": 0.3}, "outsider") is None             # < 2 models


def test_lomo_sensitivity_flags_frame_driver():
    # one extreme reference model should dominate the sensitivity
    ref = {"m1": 0.50, "m2": 0.52, "m3": 0.48, "driver": 0.95}
    s = lomo_sensitivity(0.7, ref, "outsider")
    reduced = {m: v for m, v in ref.items() if m != "driver"}
    expected = abs(loo_z(0.7, reduced, "outsider") - loo_z(0.7, ref, "outsider"))
    assert abs(s - expected) < 1e-9  # dropping the driver IS the max delta


def test_profile_table_shape_and_reference_set():
    scores = {"P-ALLOCATION": {m: 0.1 * i for i, m in enumerate(REFERENCE_MODELS)}}
    scores["P-ALLOCATION"]["newcomer"] = 0.9
    t = profile_table(scores)
    cells = t["P-ALLOCATION"]
    assert set(cells) == set(REFERENCE_MODELS) | {"newcomer"}
    for cell in cells.values():
        assert "z" in cell and "lomo_sensitivity" in cell


# --------------------------------------------------------------------------- #
# frame-inside-bootstrap
# --------------------------------------------------------------------------- #
ITEMS = {
    "gpt-5":              [0.9, 0.8, 1.0, 0.7, 0.9],
    "claude-sonnet-4.5":  [0.8, 0.7, 0.9, 0.8, 0.6],
    "gemini-2.5-pro":     [0.6, 0.7, 0.5, 0.8, 0.6],
    "deepseek-r1":        [0.5, 0.4, 0.6, 0.5, 0.7],
    "gpt-4.1-mini":       [0.4, 0.5, 0.3, 0.6, 0.4],
    "deepseek-chat":      [0.3, 0.4, 0.5, 0.2, 0.3],
    "mistral-small-3.2":  [0.2, 0.3, 0.1, 0.4, 0.2],
}


def test_bootstrap_deterministic_under_seed():
    a = bootstrap_loo_interval(ITEMS, "gpt-5", n_boot=200, seed=7)
    b = bootstrap_loo_interval(ITEMS, "gpt-5", n_boot=200, seed=7)
    assert a == b


def test_bootstrap_interval_brackets_point():
    r = bootstrap_loo_interval(ITEMS, "gpt-5", n_boot=500, seed=1)
    assert r["ci_low"] <= r["z"] <= r["ci_high"]
    assert r["n_items"] == 5


def test_bootstrap_requires_aligned_items():
    bad = dict(ITEMS)
    bad["gpt-5"] = [0.9, 0.8]
    try:
        bootstrap_loo_interval(bad, "gpt-5", n_boot=10, seed=0)
    except ValueError as e:
        assert "aligned" in str(e)
    else:
        raise AssertionError("misaligned item_scores must raise")


def test_bootstrap_unknown_target_returns_none():
    assert bootstrap_loo_interval(ITEMS, "nope", n_boot=10, seed=0) is None
