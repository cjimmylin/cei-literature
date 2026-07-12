"""Model-free observed triads with a win-marginal-preserving MCMC null."""

from collections import Counter, defaultdict
from itertools import combinations
import math

import numpy as np


DEFAULT_RETAINED_DRAWS = 10_000
DEFAULT_CHAINS = 4
MAX_SPLIT_RHAT = 1.05
MIN_EFFECTIVE_SAMPLE_SIZE = 20
MIN_EFFECTIVE_SAMPLE_FRACTION = 0.10
_NORMS = tuple(range(1, 10))
_TIERS = ("T1", "T2", "T3", "T4")
_TIER_ORDER = {tier: index for index, tier in enumerate(_TIERS)}
_FRAMES = ("neutral", "threat")
_NULL_METHOD = "trial-level conditional triangle-reversal MCMC"
_KNOWN_CONTROL_STATUSES = ("SCORED_COMPREHENSION", "SCORED_RECOGNITION")


def _validate_edge(edge):
    if type(edge) not in (tuple, list) or len(edge) != 2:
        raise ValueError("trial edge must be a (winner, loser) pair")
    winner, loser = edge
    if (
        type(winner) is not int
        or type(loser) is not int
        or isinstance(winner, bool)
        or isinstance(loser, bool)
        or winner == loser
    ):
        raise ValueError("trial edge endpoints must be distinct integer norms")
    return winner, loser


def win_totals(edges):
    """Return every represented norm's individual number of trial wins."""
    counts = Counter()
    norms = set()
    for edge in edges:
        winner, loser = _validate_edge(edge)
        counts[winner] += 1
        norms.update((winner, loser))
    return {norm: counts[norm] for norm in sorted(norms)}


def assert_win_marginals_preserved(reference_edges, candidate_edges):
    """Fail if a proposed null state changes any norm's total wins."""
    reference = list(reference_edges)
    candidate = list(candidate_edges)
    if len(reference) != len(candidate) or win_totals(reference) != win_totals(candidate):
        raise ValueError("triangle reversal changed individual total wins")
    return True


def _parse_pair(pair):
    if type(pair) is not str or pair.count("x") != 1:
        raise ValueError("pair must be a canonical AxB string")
    try:
        a, b = (int(value) for value in pair.split("x"))
    except (TypeError, ValueError):
        raise ValueError("pair must be a canonical AxB string")
    if not 1 <= a < b <= 10 or pair != "%dx%d" % (a, b):
        raise ValueError("pair must be ordered and canonical")
    return a, b


def _pair_key(a, b):
    return (a, b) if a < b else (b, a)


def _majority_triads(edges):
    votes = defaultdict(Counter)
    for winner, loser in edges:
        votes[_pair_key(winner, loser)][winner] += 1
    majority = {}
    for pair, counts in votes.items():
        a, b = pair
        if counts[a] == counts[b]:
            continue
        majority[pair] = a if counts[a] > counts[b] else b

    complete = 0
    violations = 0
    for a, b, c in combinations(_NORMS, 3):
        pairs = ((a, b), (a, c), (b, c))
        if not all(pair in majority for pair in pairs):
            continue
        complete += 1
        wins = {a: 0, b: 0, c: 0}
        for pair in pairs:
            wins[majority[pair]] += 1
        if sorted(wins.values()) == [1, 1, 1]:
            violations += 1
    return complete, violations


def _available_triangles(edges):
    present_pairs = {_pair_key(winner, loser) for winner, loser in edges}
    return [
        (a, b, c)
        for a, b, c in combinations(_NORMS, 3)
        if {(a, b), (a, c), (b, c)} <= present_pairs
    ]


def _pair_indices(edges):
    indices = defaultdict(list)
    for index, (winner, loser) in enumerate(edges):
        indices[_pair_key(winner, loser)].append(index)
    return indices


def _triangle_reversal_step(edges, triangles, indices, rng):
    if not triangles:
        return False
    a, b, c = triangles[int(rng.integers(0, len(triangles)))]
    selected = [
        indices[pair][int(rng.integers(0, len(indices[pair])))]
        for pair in ((a, b), (a, c), (b, c))
    ]
    winners = Counter(edges[index][0] for index in selected)
    if {winners[a], winners[b], winners[c]} != {1}:
        return False
    for index in selected:
        winner, loser = edges[index]
        edges[index] = (loser, winner)
    return True


def _run_chain(reference_edges, triangles, burn_in, thinning, draws, seed):
    rng = np.random.default_rng(seed)
    edges = list(reference_edges)
    indices = _pair_indices(edges)
    for _ in range(burn_in):
        _triangle_reversal_step(edges, triangles, indices, rng)
    statistics = []
    post_burn_moves = 0
    sampled_states = set()
    for _ in range(draws):
        for _ in range(thinning):
            post_burn_moves += int(
                _triangle_reversal_step(edges, triangles, indices, rng)
            )
        _, violations = _majority_triads(edges)
        statistics.append(violations)
        sampled_states.add(tuple(winner for winner, _ in edges))
    assert_win_marginals_preserved(reference_edges, edges)
    return statistics, post_burn_moves, len(sampled_states)


def _chain_disagreement(chain_statistics):
    if len(chain_statistics) <= 1:
        return False, [float(np.mean(chain_statistics[0]))]
    means = [float(np.mean(values)) for values in chain_statistics]
    variances = [
        float(np.var(values, ddof=1)) if len(values) > 1 else 0.0
        for values in chain_statistics
    ]
    pooled_sd = math.sqrt(max(0.0, sum(variances) / len(variances)))
    pooled_mean = sum(means) / len(means)
    disagreement = max(abs(mean - pooled_mean) for mean in means)
    if pooled_sd == 0.0:
        return disagreement > 0.0, means
    return disagreement > 0.5 * pooled_sd, means


def _split_rhat(chain_statistics):
    if len(chain_statistics) < 1 or len({len(values) for values in chain_statistics}) != 1:
        return None
    half_length = len(chain_statistics[0]) // 2
    if half_length < 2:
        return None
    split_chains = np.asarray(
        [
            half
            for values in chain_statistics
            for half in (values[:half_length], values[-half_length:])
        ],
        dtype=float,
    )
    within_variance = float(
        np.mean(np.var(split_chains, axis=1, ddof=1))
    )
    between_variance = float(
        half_length * np.var(np.mean(split_chains, axis=1), ddof=1)
    )
    if within_variance == 0.0:
        return 1.0 if between_variance == 0.0 else None
    variance_estimate = (
        (half_length - 1.0) * within_variance + between_variance
    ) / half_length
    rhat = math.sqrt(max(0.0, variance_estimate / within_variance))
    return float(rhat) if math.isfinite(rhat) else None


def _autocorrelation_adjusted_ess(chain_statistics):
    if len(chain_statistics) < 1 or len({len(values) for values in chain_statistics}) != 1:
        return None
    chain_length = len(chain_statistics[0])
    if chain_length < 3:
        return None
    values = np.asarray(chain_statistics, dtype=float)
    pooled_draws = values.size
    centered = values - np.mean(values, axis=1, keepdims=True)
    fft_length = 1 << (2 * chain_length - 1).bit_length()
    spectrum = np.fft.rfft(centered, n=fft_length, axis=1)
    autocovariance = np.fft.irfft(
        spectrum * np.conjugate(spectrum), n=fft_length, axis=1
    )[:, :chain_length]
    autocovariance /= np.arange(chain_length, 0, -1, dtype=float)[None, :]
    mean_autocovariance = np.mean(autocovariance, axis=0)
    variance = float(mean_autocovariance[0])
    if variance <= np.finfo(float).eps:
        return float(pooled_draws)
    autocorrelations = mean_autocovariance[1:] / variance
    positive_pair_sum = 0.0
    previous_pair = float("inf")
    for index in range(0, len(autocorrelations) - 1, 2):
        pair = float(autocorrelations[index] + autocorrelations[index + 1])
        if pair <= 0.0:
            break
        pair = min(pair, previous_pair)
        positive_pair_sum += pair
        previous_pair = pair
    integrated_autocorrelation = max(1.0, 1.0 + 2.0 * positive_pair_sum)
    ess = min(float(pooled_draws), pooled_draws / integrated_autocorrelation)
    return float(ess) if math.isfinite(ess) else None


def _not_estimable(tier, frame, edge_count, burn_in, thinning, draws, chains, reason):
    ess_threshold = max(
        float(MIN_EFFECTIVE_SAMPLE_SIZE),
        MIN_EFFECTIVE_SAMPLE_FRACTION * draws * chains,
    )
    return {
        "severity_tier": tier,
        "framing_arm": frame,
        "status": "NULL_NOT_ESTIMABLE",
        "reason": reason,
        "null_method": _NULL_METHOD,
        "tail": "LOWER",
        "p_coherent": None,
        "edge_count": edge_count,
        "burn_in": burn_in,
        "thinning": thinning,
        "retained_draws": draws,
        "chains": chains,
        "marginals_preserved": True,
        "observed_complete_triads": None,
        "observed_violation_count": None,
        "null_mean_violation_count": None,
        "chain_means": [],
        "chain_post_burn_moves": [],
        "chain_unique_states": [],
        "chain_acceptance_rates": [],
        "rhat": None,
        "ess": None,
        "rhat_threshold": MAX_SPLIT_RHAT,
        "ess_threshold": ess_threshold,
    }


def _analyze_stratum(tier, frame, rows, seed, burn_in, thinning, draws, chains):
    edges = []
    for row in rows:
        a, b = _parse_pair(row["pair"])
        winner = row["served_commandment"]
        if winner not in {a, b}:
            raise ValueError("triad trial winner is not a member of its pair")
        loser = b if winner == a else a
        edges.append((winner, loser))
    edge_count = len(edges)
    actual_burn = 100 * edge_count if burn_in is None else burn_in
    actual_thinning = 10 * edge_count if thinning is None else thinning
    triangles = _available_triangles(edges)
    observed_complete, observed_violations = _majority_triads(edges)

    chain_statistics = []
    chain_post_burn_moves = []
    chain_unique_states = []
    for chain_index in range(chains):
        statistics, post_burn_moves, unique_states = _run_chain(
            edges,
            triangles,
            actual_burn,
            actual_thinning,
            draws,
            seed + 1_000_003 * chain_index,
        )
        chain_statistics.append(statistics)
        chain_post_burn_moves.append(post_burn_moves)
        chain_unique_states.append(unique_states)
    proposals_per_chain = actual_thinning * draws
    if any(moves > proposals_per_chain for moves in chain_post_burn_moves):
        raise AssertionError("accepted chain moves exceed post-burn proposals")
    chain_acceptance_rates = [
        moves / float(proposals_per_chain) for moves in chain_post_burn_moves
    ]
    ess_threshold = max(
        float(MIN_EFFECTIVE_SAMPLE_SIZE),
        MIN_EFFECTIVE_SAMPLE_FRACTION * draws * chains,
    )
    if sum(chain_post_burn_moves) == 0:
        result = _not_estimable(
            tier,
            frame,
            edge_count,
            actual_burn,
            actual_thinning,
            draws,
            chains,
            "NO_CHAIN_MOVES",
        )
        result["observed_complete_triads"] = observed_complete
        result["observed_violation_count"] = observed_violations
        result["chain_post_burn_moves"] = chain_post_burn_moves
        result["chain_unique_states"] = chain_unique_states
        result["chain_acceptance_rates"] = chain_acceptance_rates
        return result

    if any(moves == 0 for moves in chain_post_burn_moves) or any(
        states < 2 for states in chain_unique_states
    ):
        result = _not_estimable(
            tier,
            frame,
            edge_count,
            actual_burn,
            actual_thinning,
            draws,
            chains,
            "CHAIN_STUCK_POST_BURN",
        )
        result["observed_complete_triads"] = observed_complete
        result["observed_violation_count"] = observed_violations
        result["chain_post_burn_moves"] = chain_post_burn_moves
        result["chain_unique_states"] = chain_unique_states
        result["chain_acceptance_rates"] = chain_acceptance_rates
        return result

    rhat = _split_rhat(chain_statistics)
    ess = _autocorrelation_adjusted_ess(chain_statistics)
    failed_mixing, chain_means = _chain_disagreement(chain_statistics)
    if failed_mixing:
        result = _not_estimable(
            tier,
            frame,
            edge_count,
            actual_burn,
            actual_thinning,
            draws,
            chains,
            "CHAIN_MEAN_DISAGREEMENT",
        )
        result["observed_complete_triads"] = observed_complete
        result["observed_violation_count"] = observed_violations
        result["chain_means"] = chain_means
        result["chain_post_burn_moves"] = chain_post_burn_moves
        result["chain_unique_states"] = chain_unique_states
        result["chain_acceptance_rates"] = chain_acceptance_rates
        result["rhat"] = rhat
        result["ess"] = ess
        return result

    if (
        rhat is None
        or ess is None
        or rhat > MAX_SPLIT_RHAT
        or ess < ess_threshold
    ):
        result = _not_estimable(
            tier,
            frame,
            edge_count,
            actual_burn,
            actual_thinning,
            draws,
            chains,
            "MIXING_DIAGNOSTIC_FAILED",
        )
        result["observed_complete_triads"] = observed_complete
        result["observed_violation_count"] = observed_violations
        result["chain_means"] = chain_means
        result["chain_post_burn_moves"] = chain_post_burn_moves
        result["chain_unique_states"] = chain_unique_states
        result["chain_acceptance_rates"] = chain_acceptance_rates
        result["rhat"] = rhat
        result["ess"] = ess
        return result

    pooled = [value for chain in chain_statistics for value in chain]
    p_coherent = (1.0 + sum(value <= observed_violations for value in pooled)) / (
        1.0 + len(pooled)
    )
    return {
        "severity_tier": tier,
        "framing_arm": frame,
        "status": "ESTIMATED",
        "reason": None,
        "null_method": _NULL_METHOD,
        "tail": "LOWER",
        "p_coherent": p_coherent,
        "edge_count": edge_count,
        "burn_in": actual_burn,
        "thinning": actual_thinning,
        "retained_draws": draws,
        "chains": chains,
        "marginals_preserved": True,
        "observed_complete_triads": observed_complete,
        "observed_violation_count": observed_violations,
        "null_mean_violation_count": float(np.mean(pooled)),
        "chain_means": chain_means,
        "chain_post_burn_moves": chain_post_burn_moves,
        "chain_unique_states": chain_unique_states,
        "chain_acceptance_rates": chain_acceptance_rates,
        "rhat": rhat,
        "ess": ess,
        "rhat_threshold": MAX_SPLIT_RHAT,
        "ess_threshold": ess_threshold,
    }


def analyze_triads(
    scored_records,
    seed=0,
    burn_in=None,
    thinning=None,
    retained_draws=DEFAULT_RETAINED_DRAWS,
    chains=DEFAULT_CHAINS,
):
    """Analyze observed pair-majority triads within tier/frame strata."""
    if type(scored_records) is not list:
        raise ValueError("scored_records must be a list")
    for value, label, allow_none in (
        (burn_in, "burn_in", True),
        (thinning, "thinning", True),
        (retained_draws, "retained_draws", False),
        (chains, "chains", False),
    ):
        if allow_none and value is None:
            continue
        if type(value) is not int or isinstance(value, bool) or value <= 0:
            raise ValueError("%s must be a positive integer" % label)
    if type(seed) is not int or isinstance(seed, bool):
        raise ValueError("seed must be an integer")

    grouped = defaultdict(list)
    excluded_c10 = 0
    for row in scored_records:
        if type(row) is not dict:
            raise ValueError("scored records must be objects")
        if "status" not in row:
            raise ValueError("scored record is missing status")
        status = row["status"]
        if status in _KNOWN_CONTROL_STATUSES:
            continue
        if status != "SCORED_ACTION":
            raise ValueError("scored record has unknown status: %r" % status)
        a, b = _parse_pair(row.get("pair"))
        if 10 in (a, b):
            excluded_c10 += 1
            continue
        if row.get("triad_eligible") is not True:
            continue
        tier = row.get("severity_tier")
        frame = row.get("framing_arm")
        if tier not in _TIERS or frame not in _FRAMES:
            raise ValueError("triad-eligible action has an invalid tier or frame")
        if row.get("outcome_class") not in {"duty_a", "duty_b"}:
            continue
        grouped[(tier, frame)].append(row)

    strata = [
        _analyze_stratum(
            tier,
            frame,
            grouped[(tier, frame)],
            seed + 10_007 * stratum_index,
            burn_in,
            thinning,
            retained_draws,
            chains,
        )
        for stratum_index, (tier, frame) in enumerate(
            sorted(
                grouped,
                key=lambda key: (_TIER_ORDER[key[0]], _FRAMES.index(key[1])),
            )
        )
    ]
    return {
        "claim_status": "DIAGNOSTIC_ONLY",
        "excluded_c10_trials": excluded_c10,
        "strata": strata,
    }


__all__ = [
    "DEFAULT_CHAINS",
    "DEFAULT_RETAINED_DRAWS",
    "MAX_SPLIT_RHAT",
    "MIN_EFFECTIVE_SAMPLE_FRACTION",
    "MIN_EFFECTIVE_SAMPLE_SIZE",
    "analyze_triads",
    "assert_win_marginals_preserved",
    "win_totals",
]
