"""Tests for the causal-graph scenario generator (CRUX §3.1).

Spec facts encoded here:
- Causal-graph templates guarantee the conflict is REAL: each option provably
  sacrifices one value (no option satisfies both).
- Fresh-per-run instances: surface text varies by instance seed; structure does
  not.
- Matched triads for CO (transitivity) are drawn ONLY from commensurable-
  structure cells; declared-incomparable pairs are excluded (M3).
- Minimal-pair factor edits for AMCE change exactly one factor.
"""
import itertools

from crux import factorial, generator, values


def _a_cell(**overrides):
    cell = {
        "value_pair": values.value_pairs()[0],
        "stakes": "serious",
        "uncertainty": "complete_info",
        "beneficiary": "other",
        "relationship": "out_group",
        "reversibility": "reversible",
    }
    cell.update(overrides)
    return cell


def test_scenario_has_exactly_two_options():
    s = generator.generate_scenario(_a_cell())
    assert len(s.options) == 2


def test_each_option_sacrifices_the_other_value():
    cell = _a_cell()
    va, vb = cell["value_pair"]
    s = generator.generate_scenario(cell)
    honored = {o.honors for o in s.options}
    sacrificed = {o.sacrifices for o in s.options}
    assert honored == {va, vb}
    assert sacrificed == {va, vb}
    for o in s.options:
        assert o.honors != o.sacrifices  # a real conflict, never both


def test_causal_graph_records_satisfy_and_violate_per_action():
    s = generator.generate_scenario(_a_cell())
    va, vb = s.value_a, s.value_b
    # every action node satisfies one value and violates the other
    for action, effect in s.causal_graph.items():
        assert effect["satisfies"] in (va, vb)
        assert effect["violates"] in (va, vb)
        assert effect["satisfies"] != effect["violates"]


def test_fresh_per_run_surface_varies_but_structure_is_stable():
    cell = _a_cell()
    s1 = generator.generate_scenario(cell, instance_seed=1)
    s2 = generator.generate_scenario(cell, instance_seed=2)
    assert s1.surface != s2.surface           # fresh instance
    assert s1.value_a == s2.value_a
    assert s1.value_b == s2.value_b
    assert {o.honors for o in s1.options} == {o.honors for o in s2.options}


def test_same_seed_reproduces_the_same_surface():
    cell = _a_cell()
    assert (
        generator.generate_scenario(cell, instance_seed=5).surface
        == generator.generate_scenario(cell, instance_seed=5).surface
    )


def test_commensurability_excludes_irreducible_uncertainty():
    assert generator.is_commensurable(_a_cell(uncertainty="complete_info"))
    assert not generator.is_commensurable(_a_cell(uncertainty="irreducible"))


def test_minimal_pair_changes_exactly_one_factor():
    cell = _a_cell()
    base, edited = generator.minimal_pair(cell, factor="beneficiary", new_level="group")
    differing = [k for k in factorial.FACTORS if base.cell[k] != edited.cell[k]]
    assert differing == ["beneficiary"]
    assert edited.cell["beneficiary"] == "group"


def test_matched_triad_covers_three_pairwise_conflicts_all_commensurable():
    triple = ("welfare", "autonomy", "order")
    triad = generator.matched_triad(triple, seed=0)
    assert len(triad.items) == 3
    got_pairs = {frozenset((s.value_a, s.value_b)) for s in triad.items}
    expected = {frozenset(p) for p in itertools.combinations(triple, 2)}
    assert got_pairs == expected
    assert all(generator.is_commensurable(s.cell) for s in triad.items)


def test_matched_triad_rejects_non_distinct_values():
    import pytest

    with pytest.raises(ValueError):
        generator.matched_triad(("welfare", "welfare", "order"))
