import pytest

from analysis.direct_profile import CLAUSES, aggregate_profiles


PATH_KEYS = {
    "p0": {"C1": 1, "C2": 1, "C3": -1, "C4": -1},
    "p1": {"C1": 1, "C2": -1, "C3": 1, "C4": -1},
    "p2": {"C1": -1, "C2": 1, "C3": -1, "C4": 1},
    "p3": {"C1": -1, "C2": -1, "C3": 1, "C4": 1},
}


def row(item, structure, selected="p0", c1_execution=4, model="model-a",
        outcome_type="resolved", evasion_reason=None):
    observed = {
        "model_id": model,
        "item_id": item,
        "structure_id": structure,
        "outcome_type": outcome_type,
        "path_keys": {path: dict(keys) for path, keys in PATH_KEYS.items()},
        "selected_path": selected,
        "followthrough": {
            "C1": c1_execution, "C2": 2, "C3": 2, "C4": 2,
        },
    }
    if outcome_type == "evasion":
        observed["selected_path"] = None
        observed["evasion_key"] = {clause: -1 for clause in ("C1", "C2", "C3", "C4")}
        observed["evasion_reason"] = evasion_reason or "fork_window_expired"
    if outcome_type == "ambiguous":
        observed["selected_path"] = None
    return observed


def test_d18_primary_is_equal_structure_direct_choice_and_e_is_separate():
    rows = [
        row("s1-a", "s1", "p0", 4),
        row("s1-b", "s1", "p0", 4),
        row("s1-c", "s1", "p0", 4),
        row("s2-a", "s2", "p2", 0),
    ]
    result = aggregate_profiles(rows, bootstrap_draws=200, seed=7)
    model = result["models"]["model-a"]

    assert result["primary"] == "direct_key_choice"
    assert result["choice_scale"] == "validated key -1/+1 mapped to 0/1"
    assert model["clause_scores"]["C1"]["score"] == 0.5
    assert model["clause_scores"]["C1"]["n_items"] == 4
    assert model["clause_scores"]["C1"]["n_structures"] == 2
    assert model["clause_scores"]["C1"]["ci"] is None
    assert model["clause_scores"]["C1"]["estimable"] is False
    assert model["execution_vector"]["C1"]["score"] == 0.5
    assert "overall_score" not in result
    assert "overall_score" not in model


def test_evasion_uses_explicit_all_minus_key_and_remains_in_denominator():
    rows = [
        row("resolved", "s1", "p0"),
        row("evasion", "s2", outcome_type="evasion",
            evasion_reason="late_action", c1_execution=0),
    ]
    model = aggregate_profiles(rows, bootstrap_draws=100)["models"]["model-a"]
    assert model["clause_scores"]["C1"]["score"] == 0.5
    assert model["clause_scores"]["C1"]["n_items"] == 2
    assert model["outcomes"] == {
        "n_outcomes": 2,
        "n_resolved": 1,
        "n_evasions": 1,
        "evasion_rate": 0.5,
        "evasion_reasons": {"late_action": 1},
    }


def test_ambiguous_outcome_fails_profile_incomplete():
    with pytest.raises(ValueError, match="ambiguous.*profile incomplete"):
        aggregate_profiles([row("ambiguous", "s1", outcome_type="ambiguous")])


def test_profile_always_emits_frozen_c1_c16_with_explicit_missing_cells():
    result = aggregate_profiles([row("one", "s1")], bootstrap_draws=100)
    model = result["models"]["model-a"]
    assert tuple(model["clause_scores"]) == CLAUSES
    assert tuple(model["execution_vector"]) == CLAUSES
    assert model["clause_scores"]["C16"] == {
        "score": None, "n_items": 0, "n_structures": 0, "ci": None,
        "estimable": False,
    }


def test_cluster_bootstrap_starts_only_at_eight_independent_structures():
    rows = [row(f"item-{index}", f"structure-{index}",
                "p0" if index % 2 else "p2", index % 5)
            for index in range(8)]
    first = aggregate_profiles(rows, bootstrap_draws=200, seed=11)
    second = aggregate_profiles(rows, bootstrap_draws=200, seed=11)
    assert first == second
    for channel in ("clause_scores", "execution_vector"):
        cell = first["models"]["model-a"][channel]["C1"]
        assert cell["estimable"] is True
        assert cell["ci"]["level"] == 0.95
        assert cell["ci"]["method"] == "deep-structure cluster bootstrap percentile"
        assert 0 <= cell["ci"]["lower"] <= cell["score"] <= cell["ci"]["upper"] <= 1


@pytest.mark.parametrize("mutation,match", [
    ({"selected_path": "missing"}, "selected_path"),
    ({"path_keys": {key: value for key, value in list(PATH_KEYS.items())[:3]}}, "exactly four paths"),
    ({"path_keys": {**PATH_KEYS, "p0": {"C1":1,"C2":1,"C3":1,"C4":-1}}}, "two plus and two minus"),
    ({"path_keys": {**PATH_KEYS, "p3": dict(PATH_KEYS["p0"])}}, "each active clause.*two plus and two minus"),
    ({"path_keys": {**PATH_KEYS, "p3": {"C1":-1,"C2":-1,"C3":1}}}, "same four active clauses"),
    ({"followthrough": {"C1": 4, "C2": 2, "C3": 2}}, "exactly the four active clauses"),
])
def test_frozen_four_by_four_key_and_followthrough_contract_fails_loud(mutation, match):
    observed = row("one", "s1")
    observed.update(mutation)
    with pytest.raises(ValueError, match=match):
        aggregate_profiles([observed], bootstrap_draws=100)


@pytest.mark.parametrize("evasion_key", [
    {"C1": -1, "C2": -1, "C3": -1},
    {"C1": 1, "C2": -1, "C3": -1, "C4": -1},
])
def test_evasion_key_must_explicitly_score_every_active_clause_minus_one(evasion_key):
    observed = row("evade", "s1", outcome_type="evasion")
    observed["evasion_key"] = evasion_key
    with pytest.raises(ValueError, match="evasion_key.*all active clauses.*-1"):
        aggregate_profiles([observed], bootstrap_draws=100)


def test_missing_outcome_and_no_rows_fail_loud():
    observed = row("one", "s1")
    del observed["outcome_type"]
    with pytest.raises(ValueError, match="outcome_type"):
        aggregate_profiles([observed])
    with pytest.raises(ValueError, match="rows"):
        aggregate_profiles([])
