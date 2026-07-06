"""Analysis synthetic-recovery: recover PLANTED beta0/beta1/ceiling/discernment
within tolerance BEFORE any real pilot (brief §11 item 5, D-16)."""
from analysis import fit, synth_recovery as sr


def test_recover_dose_response():
    valid_rows, matched, planted = sr.simulate(seed=20260706)
    doses = [r["dose"] for r in valid_rows]
    updates = [r["update"] for r in valid_rows]
    est = fit.fit_valid_arm(doses, updates)
    # clipping at [0,3] biases estimates slightly; use generous but real tolerances
    assert abs(est["beta0"] - planted["beta0"]) < 0.15, est
    assert abs(est["beta1"] - planted["beta1"]) < 0.12, est
    assert abs(est["ceiling"] - planted["ceiling"]) < 0.25, est


def test_recover_discernment():
    _, matched, planted = sr.simulate(seed=20260706)
    d = fit.discernment_differential(matched)
    assert abs(d["discernment"] - planted["discernment"]) < 0.12, d
    lo, hi = d["ci95"]
    assert lo < planted["discernment"] < hi, d


def test_zero_discernment_recovers_zero():
    _, matched, _ = sr.simulate(seed=7, discernment=0.0)
    d = fit.discernment_differential(matched)
    assert abs(d["discernment"]) < 0.10, d
    lo, hi = d["ci95"]
    assert lo < 0.0 < hi, d


def test_ceiling_flattens_slope():
    # with a strong negative ceiling, beta1 must NOT absorb the d4/d5 drop
    valid_rows, _, planted = sr.simulate(seed=11, ceiling=-0.8, beta1=0.5)
    est = fit.fit_valid_arm([r["dose"] for r in valid_rows],
                            [r["update"] for r in valid_rows])
    assert est["ceiling"] < -0.4, est
    assert abs(est["beta1"] - 0.5) < 0.15, est
