from itertools import combinations

import pytest

import analysis.triads as triads
from analysis.triads import (
    DEFAULT_CHAINS,
    DEFAULT_RETAINED_DRAWS,
    analyze_triads,
    assert_win_marginals_preserved,
    win_totals,
)


def _row(pair, winner):
    a, b = (int(value) for value in pair.split("x"))
    return {
        "status": "SCORED_ACTION",
        "pair": pair,
        "severity_tier": "T1",
        "framing_arm": "neutral",
        "served_commandment": winner,
        "bt_eligible": 10 not in (a, b),
        "triad_eligible": 10 not in (a, b),
        "outcome_class": "duty_a" if winner == a else "duty_b",
        "paralysis": False,
    }


def _moving_rows():
    rows = []
    for a, b in combinations(range(1, 10), 2):
        rows.extend([_row(f"{a}x{b}", a), _row(f"{a}x{b}", b)])
    rows.extend([_row("1x2", 1), _row("2x3", 2), _row("1x3", 3)])
    return rows


def test_triangle_reversal_null_is_deterministic_model_free_and_marginal_preserving():
    first = analyze_triads(
        _moving_rows(), seed=17, burn_in=40, thinning=5, retained_draws=80, chains=4
    )
    second = analyze_triads(
        _moving_rows(), seed=17, burn_in=40, thinning=5, retained_draws=80, chains=4
    )
    assert first == second
    assert DEFAULT_RETAINED_DRAWS == 10_000
    assert DEFAULT_CHAINS == 4
    result = first["strata"][0]
    assert result["null_method"] == "trial-level conditional triangle-reversal MCMC"
    assert result["status"] == "ESTIMATED"
    assert result["tail"] == "LOWER"
    assert 0.0 < result["p_coherent"] <= 1.0
    assert result["burn_in"] == 40
    assert result["thinning"] == 5
    assert result["marginals_preserved"] is True
    assert all(moves > 0 for moves in result["chain_post_burn_moves"])
    assert all(states >= 2 for states in result["chain_unique_states"])
    assert result["rhat"] <= result["rhat_threshold"] == 1.05
    assert result["ess"] >= result["ess_threshold"] == 32.0
    assert len(result["chain_acceptance_rates"]) == 4
    assert all(0.0 <= rate <= 1.0 for rate in result["chain_acceptance_rates"])
    assert "bt_probability" not in result


def test_default_contract_scales_burnin_and_thinning_by_trial_edges():
    result = analyze_triads(
        _moving_rows(), seed=3, retained_draws=2, chains=1
    )["strata"][0]
    assert result["burn_in"] == 100 * result["edge_count"]
    assert result["thinning"] == 10 * result["edge_count"]


def test_nonmoving_null_and_c10_leakage_fail_closed():
    transitive = []
    for a, b in combinations(range(1, 10), 2):
        transitive.extend([_row(f"{a}x{b}", a) for _ in range(2)])
    result = analyze_triads(
        transitive, seed=1, burn_in=5, thinning=1, retained_draws=10, chains=2
    )["strata"][0]
    assert result["status"] == "NULL_NOT_ESTIMABLE"
    assert result["reason"] == "NO_CHAIN_MOVES"

    c10 = _row("1x10", 10)
    c10["bt_eligible"] = c10["triad_eligible"] = True
    report = analyze_triads(
        _moving_rows() + [c10], seed=2, burn_in=10, thinning=2,
        retained_draws=10, chains=2,
    )
    assert report["excluded_c10_trials"] == 1
    assert report["strata"][0]["edge_count"] == len(_moving_rows())


def test_broken_marginal_preservation_is_rejected():
    reference = [(1, 2), (2, 3), (3, 1)]
    valid_reversal = [(2, 1), (3, 2), (1, 3)]
    assert win_totals(reference) == win_totals(valid_reversal)
    assert assert_win_marginals_preserved(reference, valid_reversal) is True
    with pytest.raises(ValueError, match="individual total wins"):
        assert_win_marginals_preserved(reference, [(1, 2), (2, 3), (1, 3)])


def test_one_stuck_chain_fails_closed_even_when_another_chain_moves(monkeypatch):
    chain_results = iter(
        [
            ([0, 1, 0], 3, 2),
            ([0, 0, 0], 0, 1),
        ]
    )
    monkeypatch.setattr(triads, "_run_chain", lambda *args, **kwargs: next(chain_results))

    result = analyze_triads(
        _moving_rows(), seed=41, burn_in=2, thinning=1, retained_draws=3, chains=2
    )["strata"][0]

    assert result["status"] == "NULL_NOT_ESTIMABLE"
    assert result["reason"] == "CHAIN_STUCK_POST_BURN"
    assert result["chain_post_burn_moves"] == [3, 0]
    assert result["chain_unique_states"] == [2, 1]


def test_triads_reject_malformed_or_unknown_scored_statuses_and_skip_known_controls():
    for records, message in (
        ([None], "objects"),
        ([{}], "missing status"),
        ([{"status": "SCORED_FUTURE_KIND"}], "unknown status"),
    ):
        with pytest.raises(ValueError, match=message):
            analyze_triads(records)

    report = analyze_triads(
        [
            {"status": "SCORED_COMPREHENSION"},
            {"status": "SCORED_RECOGNITION"},
        ]
    )
    assert report["strata"] == []


def test_high_split_rhat_fails_the_mixing_diagnostic(monkeypatch):
    low_half = [0, 1] * 10
    high_half = [4, 5] * 10
    chain_results = iter(
        [
            (low_half + high_half, 20, 2),
            (low_half + high_half, 20, 2),
            (high_half + low_half, 20, 2),
            (high_half + low_half, 20, 2),
        ]
    )
    monkeypatch.setattr(triads, "_run_chain", lambda *args, **kwargs: next(chain_results))

    result = analyze_triads(
        _moving_rows(), seed=51, burn_in=2, thinning=1, retained_draws=40, chains=4
    )["strata"][0]

    assert result["status"] == "NULL_NOT_ESTIMABLE"
    assert result["reason"] == "MIXING_DIAGNOSTIC_FAILED"
    assert result["rhat"] > result["rhat_threshold"] == 1.05
    assert result["ess_threshold"] == 20.0
    assert result["chain_acceptance_rates"] == [0.5, 0.5, 0.5, 0.5]


def test_low_autocorrelation_adjusted_ess_fails_even_with_acceptable_rhat(monkeypatch):
    sticky_sequence = ([0] * 25 + [1] * 25) * 4
    chain_results = iter(
        [(sticky_sequence, 100, 2) for _ in range(4)]
    )
    monkeypatch.setattr(triads, "_run_chain", lambda *args, **kwargs: next(chain_results))

    result = analyze_triads(
        _moving_rows(), seed=53, burn_in=2, thinning=1, retained_draws=200, chains=4
    )["strata"][0]

    assert result["status"] == "NULL_NOT_ESTIMABLE"
    assert result["reason"] == "MIXING_DIAGNOSTIC_FAILED"
    assert result["rhat"] <= result["rhat_threshold"] == 1.05
    assert result["ess"] < result["ess_threshold"] == 80.0
    assert result["chain_acceptance_rates"] == [0.5, 0.5, 0.5, 0.5]
