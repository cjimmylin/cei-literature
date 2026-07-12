import math

import pytest

from analysis.consistency import path_consistency


def record(model, group, skin, path="p1", outcome_type="resolved",
           evasion_reason=None):
    row = {
        "model_id": model,
        "consistency_group": group,
        "skin_id": skin,
        "outcome_type": outcome_type,
        "selected_path": path,
    }
    if outcome_type == "evasion":
        row["selected_path"] = None
        row["evasion_reason"] = evasion_reason or "fork_window_expired"
    if outcome_type == "ambiguous":
        row["selected_path"] = None
    return row


def test_consistency_uses_pairwise_canonical_outcomes_across_three_skins():
    rows = [
        record("m", "g1", "a", "p1"),
        record("m", "g1", "b", "p1"),
        record("m", "g1", "c", "p1"),
        record("m", "g2", "a", "p2"),
        record("m", "g2", "b", "p2"),
        record("m", "g2", "c", "p3"),
    ]
    model = path_consistency(rows, bootstrap_draws=200, seed=4)["models"]["m"]
    assert math.isclose(model["score"], (1 + 1 / 3) / 2)
    assert model["n_groups"] == 2
    assert model["minimum_skins"] == 3
    assert model["ci"] is None
    assert model["estimable"] is False
    assert model["gate_pass"] is None


def test_evasion_is_an_explicit_canonical_outcome_and_reason_is_reported():
    rows = [
        record("m", "g", "a", outcome_type="evasion", evasion_reason="late_action"),
        record("m", "g", "b", outcome_type="evasion", evasion_reason="invalid_action"),
        record("m", "g", "c", outcome_type="evasion", evasion_reason="late_action"),
    ]
    model = path_consistency(rows, bootstrap_draws=100)["models"]["m"]
    assert model["score"] == 1.0
    assert model["n_evasions"] == 3
    assert model["evasion_reasons"] == {"invalid_action": 1, "late_action": 2}
    assert model["ci"] is None
    assert model["estimable"] is False


def test_ambiguous_outcome_fails_loud_instead_of_becoming_a_path():
    rows = [
        record("m", "g", "a"), record("m", "g", "b"),
        record("m", "g", "c", outcome_type="ambiguous"),
    ]
    with pytest.raises(ValueError, match="ambiguous.*consistency incomplete"):
        path_consistency(rows)


def test_eight_groups_are_required_before_ci_or_gate_interpretation():
    rows = []
    for index in range(8):
        rows.extend(record("m", f"g{index}", skin, "p1")
                    for skin in ("a", "b", "c"))
    model = path_consistency(rows, bootstrap_draws=100, seed=2)["models"]["m"]
    assert model["estimable"] is True
    assert model["ci"] == [1.0, 1.0]
    assert model["gate_pass"] is True


def test_fewer_than_three_skins_and_duplicate_skin_fail_loud():
    with pytest.raises(ValueError, match="at least 3 skins"):
        path_consistency([
            record("m", "g", "a"), record("m", "g", "b")
        ])
    with pytest.raises(ValueError, match="duplicate skin"):
        path_consistency([
            record("m", "g", "a"), record("m", "g", "a"),
            record("m", "g", "c"),
        ])
