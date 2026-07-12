from itertools import combinations
import math

import pytest

from analysis.bt import fit_bradley_terry, ladder_dispersion_100
from itembank.generator import build_rows
from scoring.mechanical import score_record


def _row(pair, winner, tier="T1", frame="neutral", direction="A_FIRST", **extra):
    a, b = (int(value) for value in pair.split("x"))
    row = {
        "status": "SCORED_ACTION",
        "pair": pair,
        "severity_tier": tier,
        "framing_arm": frame,
        "served_commandment": winner,
        "bt_eligible": 10 not in (a, b),
        "triad_eligible": 10 not in (a, b),
        "outcome_class": "duty_a" if winner == a else "duty_b",
        "paralysis": False,
        "direction_permutation": direction,
    }
    row.update(extra)
    return row


def _connected_rows(tier="T1", frame="neutral", reverse=False):
    rows = []
    for a, b in combinations(range(1, 10), 2):
        pair = f"{a}x{b}"
        winners = ([b, b, b, a] if reverse else [a, a, a, b])
        for index, winner in enumerate(winners):
            rows.append(
                _row(
                    pair,
                    winner,
                    tier=tier,
                    frame=frame,
                    direction="A_FIRST" if index % 2 == 0 else "B_FIRST",
                )
            )
    return rows


def test_bt_is_stratified_zero_sum_direction_adjusted_and_diagnostic_only():
    rows = _connected_rows("T1", "neutral") + _connected_rows("T4", "neutral", True)
    rows += [_row("1x10", 10, bt_eligible=True, triad_eligible=True)] * 5
    first = fit_bradley_terry(rows, seed_count=1)
    second = fit_bradley_terry(rows, seed_count=1)

    assert first == second
    assert first["claim_status"] == "DIAGNOSTIC_ONLY"
    assert first["pooled_ladder"] is None
    assert first["excluded_c10_trials"] == 5
    assert {(row["severity_tier"], row["framing_arm"]) for row in first["strata"]} == {
        ("T1", "neutral"),
        ("T4", "neutral"),
    }
    for stratum in first["strata"]:
        assert stratum["status"] == "ESTIMATED"
        assert sum(item["estimate"] for item in stratum["strengths"].values()) == pytest.approx(0.0)
        assert set(stratum["strengths"]) == {str(value) for value in range(1, 10)}
        assert math.isfinite(stratum["direction_covariate"]["estimate"])
        assert all(item["ci_low"] < item["ci_high"] for item in stratum["strengths"].values())


def test_bt_fail_closed_for_disconnection_separation_and_no_actions():
    disconnected = [_row("1x2", 1), _row("1x2", 2)]
    result = fit_bradley_terry(disconnected)
    assert result["strata"][0]["status"] == "NOT_ESTIMABLE"
    assert result["strata"][0]["reason"] == "DISCONNECTED_COMPARISON_GRAPH"

    separated = []
    for a, b in combinations(range(1, 10), 2):
        separated.extend([_row(f"{a}x{b}", a) for _ in range(3)])
    result = fit_bradley_terry(separated)
    assert result["strata"][0]["status"] == "NOT_ESTIMABLE"
    assert result["strata"][0]["reason"] == "COMPLETE_OR_QUASI_SEPARATION"

    no_actions = _connected_rows()
    for row in no_actions:
        row.update(served_commandment=None, outcome_class="paralysis", paralysis=True)
    result = fit_bradley_terry(no_actions)
    assert result["strata"][0]["status"] == "NOT_ESTIMABLE"
    assert result["strata"][0]["reason"] == "INSUFFICIENT_ACTIONS"


def test_one_unanimous_pair_does_not_separate_an_otherwise_mixed_tournament():
    rows = [row for row in _connected_rows() if row["pair"] != "1x2"]
    rows.extend(_row("1x2", 1, direction="A_FIRST" if index % 2 == 0 else "B_FIRST") for index in range(4))
    result = fit_bradley_terry(rows)
    assert result["strata"][0]["status"] == "ESTIMATED"


def test_real_scored_rows_carry_direction_metadata_into_bt_fit():
    public, private, _ = build_rows()
    scored = []
    per_pair_seen = {}
    for pub, gold in zip(public, private):
        if pub["record_type"] != "adjudication" or pub["severity_tier"] != "T1":
            continue
        a, b = pub["commandment"]
        index = per_pair_seen.get(pub["pair"], 0)
        per_pair_seen[pub["pair"]] = index + 1
        winner = a if index < 2 else b
        action_id = next(
            action_id
            for action_id, outcome in gold["choice_map"].items()
            if outcome["served_commandment"] == winner
        )
        scored.append(score_record(pub, gold, {"selected_action_id": action_id}))
    assert all(row["direction_permutation"] in {"A_FIRST", "B_FIRST"} for row in scored)
    result = fit_bradley_terry(scored)
    assert result["strata"][0]["status"] == "ESTIMATED"
    assert result["strata"][0]["direction_covariate"]["estimate"] is not None


def test_bt_reports_pair_by_tier_flip_without_a_pooled_claim():
    rows = []
    tier_winners = {
        "T1": [1, 1, 1, 2],
        "T2": [1, 1, 1, 2],
        "T3": [2, 2, 2, 1],
        "T4": [2, 2, 2, 1],
    }
    for tier, winners in tier_winners.items():
        rows.extend(_connected_rows(tier, "neutral"))
        rows = [row for row in rows if not (row["severity_tier"] == tier and row["pair"] == "1x2")]
        rows.extend(
            _row("1x2", winner, tier=tier, direction="A_FIRST" if i % 2 == 0 else "B_FIRST")
            for i, winner in enumerate(winners)
        )
    report = fit_bradley_terry(rows, seed_count=3)
    interaction = next(
        row for row in report["pair_tier_interactions"]
        if row["pair"] == "1x2" and row["framing_arm"] == "neutral"
    )
    assert interaction["status"] == "ESTIMATED"
    assert interaction["flip_threshold"] == pytest.approx(2.5)
    assert interaction["claim_scope"] == "PAIR_X_TIER_ONLY"
    assert "pooled_winner" not in interaction


def test_ladder_dispersion_uses_registered_zero_to_one_hundred_mapping():
    strengths = {"1": 1.0, "2": 0.0, "3": -1.0}
    expected = 100.0 * sum(
        abs(2.0 / (1.0 + math.exp(-(a - b))) - 1.0)
        for a, b in ((1.0, 0.0), (1.0, -1.0), (0.0, -1.0))
    ) / 3.0
    assert ladder_dispersion_100(strengths) == pytest.approx(expected)


def test_bt_rejects_malformed_or_unknown_scored_statuses_and_skips_known_controls():
    for records, message in (
        ([None], "objects"),
        ([{}], "missing status"),
        ([{"status": "SCORED_FUTURE_KIND"}], "unknown status"),
    ):
        with pytest.raises(ValueError, match=message):
            fit_bradley_terry(records)

    report = fit_bradley_terry(
        [
            {"status": "SCORED_COMPREHENSION"},
            {"status": "SCORED_RECOGNITION"},
        ]
    )
    assert report["strata"] == []
    assert report["pair_tier_interactions"] == []
