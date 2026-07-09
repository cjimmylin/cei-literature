"""Null / naive baselines (§5.6 mandatory reporting; WS-1 D12) — each null must be BEATEN by the
observed gates, confirming an observed pass is not a scale/mix/noise artifact."""
import fixtures_p0 as fx
from analysis.baselines import (
    no_process_shift_null,
    majority_class_null,
    all_neutral_null,
    null_baselines,
)


def test_no_process_shift_null_fails_g1():
    """§5.6: 'no-process-shift null (the load-bearing null)'. With every resource condition set to
    the standard-condition mean, every per-item delta is 0 -> G1's process signature collapses ->
    the null must NOT pass G1 (the observed process axis has to beat it)."""
    res = no_process_shift_null(fx.p0_pass())
    assert res["g1_pass"] is False
    assert res["beaten_by_observed"] is True


def test_majority_class_null_fails_g2():
    """§5.6: majority-class — every model predicts the per-item modal stance, so there is no
    cross-model variance -> the null must NOT pass G2 (separation)."""
    res = majority_class_null(fx.p0_pass())
    assert res["g2_pass"] is False
    assert res["beaten_by_observed"] is True


def test_all_neutral_null_fails_both_gates():
    """§5.6: all-neutral — every response is the scale midpoint -> zero variance everywhere ->
    neither G1 nor G2 can pass on the null."""
    res = all_neutral_null(fx.p0_pass())
    assert res["g1_pass"] is False
    assert res["g2_pass"] is False


def test_null_baselines_reports_all_three():
    res = null_baselines(fx.p0_pass())
    assert set(res) == {"no_process_shift", "majority_class", "all_neutral"}
