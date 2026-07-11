"""Contract tests for exact preflight and paid-response spend custody."""

import pytest


def api():
    import TENCOMMANDMENTS.harness.openrouter as openrouter

    return openrouter


def test_preflight_proves_exact_schedule_upper_bound_is_under_cap():
    module = api()
    preflight = module.preflight_spend(
        [
            module.CallEstimate("call-a", "0.010"),
            module.CallEstimate("call-b", "0.020"),
        ],
        cost_cap_usd="0.050",
    )

    assert preflight.to_dict() == {
        "schema_version": 1,
        "scheduled_call_count": 2,
        "cost_cap_usd": "0.05",
        "cost_upper_bound_usd": "0.03",
        "remaining_margin_usd": "0.02",
        "calls": [
            {"call_id": "call-a", "max_cost_usd": "0.01"},
            {"call_id": "call-b", "max_cost_usd": "0.02"},
        ],
    }


@pytest.mark.parametrize(
    "estimates, cap, message",
    [
        ([('call-a', '0.01'), ('call-a', '0.01')], "0.10", "duplicate"),
        ([('call-a', '0.11')], "0.10", "exceeds"),
        ([('call-a', 'NaN')], "0.10", "finite"),
        ([('call-a', '-0.01')], "0.10", "nonnegative"),
    ],
)
def test_preflight_fails_closed_on_invalid_or_over_cap_schedules(
    estimates, cap, message
):
    module = api()
    rows = [module.CallEstimate(call_id, amount) for call_id, amount in estimates]

    with pytest.raises(module.SpendPreflightError, match=message):
        module.preflight_spend(rows, cost_cap_usd=cap)


def test_ledger_records_exact_paid_costs_and_resumes_without_double_counting():
    module = api()
    preflight = module.preflight_spend(
        [
            module.CallEstimate("call-a", "0.02"),
            module.CallEstimate("call-b", "0.03"),
        ],
        cost_cap_usd="0.05",
    )
    first = module.SpendLedger(preflight)

    assert first.record_paid_call("call-a", "0.015").to_dict() == {
        "call_id": "call-a",
        "cost_usd": "0.015",
        "cumulative_cost_usd": "0.015",
    }
    with pytest.raises(module.SpendLedgerError, match="already recorded"):
        first.record_paid_call("call-a", "0.001")

    resumed = module.SpendLedger(
        preflight,
        prior_records=[record.to_dict() for record in first.records],
    )
    resumed.record_paid_call("call-b", "0.025")
    assert resumed.spent_cost_usd == "0.04"
    assert resumed.remaining_cost_usd == "0.01"
    assert resumed.completed_call_ids == ("call-a", "call-b")


def test_ledger_custodies_paid_cost_before_raising_on_bound_violation():
    module = api()
    preflight = module.preflight_spend(
        [module.CallEstimate("call-a", "0.01")],
        cost_cap_usd="0.01",
    )
    ledger = module.SpendLedger(preflight)

    with pytest.raises(module.SpendCapExceeded, match="exceeded"):
        ledger.record_paid_call("call-a", "0.012")
    assert ledger.spent_cost_usd == "0.012"
    assert ledger.records[-1].cost_usd == "0.012"


def test_authorization_atomically_reserves_call_until_paid_or_released():
    module = api()
    preflight = module.preflight_spend(
        [module.CallEstimate("call-a", "0.01")],
        cost_cap_usd="0.01",
    )
    ledger = module.SpendLedger(preflight)

    ledger.authorize_call("call-a")
    assert ledger.inflight_call_ids == ("call-a",)
    with pytest.raises(module.SpendLedgerError, match="reserved|authorized|in.flight"):
        ledger.authorize_call("call-a")

    ledger.release_call("call-a")
    assert ledger.inflight_call_ids == ()
    ledger.authorize_call("call-a")
    ledger.record_paid_call("call-a", "0.005")
    assert ledger.inflight_call_ids == ()
    assert ledger.completed_call_ids == ("call-a",)
