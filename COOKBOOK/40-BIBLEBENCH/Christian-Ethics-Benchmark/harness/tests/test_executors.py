"""RED: per-design executors — single-turn, scripted multi-turn (branch tables),
paired-session isolation + order permutation."""
from walkworthy.clients import MockModelClient
from walkworthy.executors import execute_item, permuted_order
from walkworthy.loader import load_design
from walkworthy.manifest import FIXED_PERMUTATION_SEEDS


def _one(design, benchmark_root, pred=None):
    items = load_design(design, benchmark_root, include_exemplars=False)
    if pred:
        items = [it for it in items if pred(it)]
    return items[0]


def test_single_turn_execution(benchmark_root):
    it = _one("01-goodsamaritan", benchmark_root)
    ex = execute_item(it, MockModelClient("mock-a", seed=1), FIXED_PERMUTATION_SEEDS)
    assert len(ex.administrations) == 1
    ar = ex.administrations[0]
    assert len(ar.turns) == 1
    assert ar.turns[0].response.strip()
    assert ar.turns[0].user_text  # the actual prompt sent, recorded for audit


def test_paired_isolation_and_order(benchmark_root):
    it = _one("10-strangergate", benchmark_root)
    ex = execute_item(it, MockModelClient("mock-a", seed=1), FIXED_PERMUTATION_SEEDS)
    labels = {a.label for a in ex.administrations}
    assert labels == {"N", "U"}
    assert ex.isolation_used
    # isolation: the U administration's transcript must not contain N's cue text.
    n_ar = next(a for a in ex.administrations if a.label == "N")
    u_ar = next(a for a in ex.administrations if a.label == "U")
    assert n_ar.turns[0].user_text != u_ar.turns[0].user_text
    # order actually used is recorded (a permutation of the two labels)
    assert set(ex.order) == {"N", "U"}


def test_multiturn_02_branch_selection(benchmark_root):
    it = _one("02-twomasters", benchmark_root)
    ex = execute_item(it, MockModelClient("mock-a", seed=2), FIXED_PERMUTATION_SEEDS)
    main = next(a for a in ex.administrations if a.label == "main")
    assert main.kind == "scripted_multi_turn"
    assert len(main.turns) >= 5
    # every branchable turn recorded which branch state was administered
    branched = [t for t in main.turns if t.branch_state is not None]
    assert branched, "02 must select branches at branchable turns"
    assert all(t.branch_state in ("complied", "refused") for t in branched)


def test_multiturn_07_terminal(benchmark_root):
    it = _one("07-seventyseven", benchmark_root)
    ex = execute_item(it, MockModelClient("mock-a", seed=2), FIXED_PERMUTATION_SEEDS)
    main = next(a for a in ex.administrations if a.label == "main")
    assert main.terminal_response and main.terminal_response.strip()
    branched = [t for t in main.turns if t.branch_state is not None]
    assert all(t.branch_state in ("validated", "challenged", "deflected") for t in branched)


def test_permuted_order_is_deterministic_and_valid():
    labels = ["seat_A", "seat_B", "arbiter"]
    o1 = permuted_order(labels, 20260706, "WW-09-B01")
    o2 = permuted_order(labels, 20260706, "WW-09-B01")
    assert o1 == o2
    assert sorted(o1) == sorted(labels)
    # different item -> (generally) independent ordering, still a valid permutation
    o3 = permuted_order(labels, 20260706, "WW-09-C02")
    assert sorted(o3) == sorted(labels)


def test_09_arbiter_runs_as_isolated_admin(benchmark_root):
    items = load_design("09-doubleedge", benchmark_root, include_exemplars=False)
    with_arb = next(it for it in items if "arbiter" in {a.label for a in it.administrations})
    ex = execute_item(with_arb, MockModelClient("mock-a", seed=1), FIXED_PERMUTATION_SEEDS)
    assert "arbiter" in {a.label for a in ex.administrations}
