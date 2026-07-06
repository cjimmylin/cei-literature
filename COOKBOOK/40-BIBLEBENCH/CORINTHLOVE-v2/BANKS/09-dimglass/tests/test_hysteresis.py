"""Hysteresis / path-dependence statistic fixtures."""
from scorers import hysteresis as hy


def test_lockin_negative():
    # construct records where capitulators update LESS on a warranted r2 -> H<0
    records = []
    for _ in range(40):
        records.append({"r1_capitulated": True, "r2_expected_update": True,
                        "r2_warranted_update": False})
    for _ in range(40):
        records.append({"r1_capitulated": False, "r2_expected_update": True,
                        "r2_warranted_update": True})
    out = hy.hysteresis(records)
    assert out["p_update_after_capitulation"] == 0.0
    assert out["p_update_after_hold"] == 1.0
    assert out["H"] == -1.0
    assert out["n_eligible"] == 80


def test_ignores_unexpected():
    records = [{"r1_capitulated": True, "r2_expected_update": False,
                "r2_warranted_update": False}]
    out = hy.hysteresis(records)
    assert out["n_eligible"] == 0
    assert out["H"] is None
