from __future__ import annotations

import copy
import os
import sys
import threading
from concurrent.futures import ThreadPoolExecutor

import pytest


HARNESS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS_ROOT not in sys.path:
    sys.path.insert(0, HARNESS_ROOT)

import open_first_mvp_preflight as preflight  # noqa: E402
import open_first_mvp_run as run  # noqa: E402

from test_open_first_mvp_preflight import (  # noqa: E402
    _catalog, _endpoints, _prompt_ceilings,
)


def _manifest():
    return preflight.build_manifest(
        _catalog(), _endpoints(), _prompt_ceilings(),
        catalog_retrieved_at="2026-07-14T00:00:00Z",
    )


def _budget_kwargs(cap_usd=1.0):
    return {
        "budget": run.BudgetController(cap_usd=cap_usd),
        "maximum_cost_usd": lambda _sut, _item_id: 0.0,
        "actual_cost_usd": lambda _outcome: 0.0,
    }


def test_sut_request_uses_exact_model_parameters_and_provider_policy():
    manifest = _manifest()
    slug = preflight.SUTS[0]
    request = run.build_sut_request(
        manifest, slug, [{"role": "user", "content": "blind prompt"}])
    model = next(row for row in manifest["models"] if row["slug"] == slug)
    assert request == {
        "model": slug,
        "messages": [{"role": "user", "content": "blind prompt"}],
        "temperature": 0,
        "max_tokens": 2048,
        "reasoning": {"enabled": False},
        "provider": model["provider_policy"],
    }
    llama = run.build_sut_request(
        manifest, preflight.SUTS[-1], [{"role": "user", "content": "blind"}])
    assert "reasoning" not in llama
    assert "tools" not in request and "models" not in request and "plugins" not in request


def test_runtime_price_above_frozen_catalog_ceiling_stops():
    manifest = _manifest()
    current = _catalog()
    run.validate_runtime_catalog(manifest, current)
    current[preflight.SUTS[0]]["pricing"]["completion"] = "0.1"
    with pytest.raises(run.TerminalStop, match="price ceiling"):
        run.validate_runtime_catalog(manifest, current)


@pytest.mark.parametrize("response", [
    {"usage": {"completion_tokens_details": {"reasoning_tokens": 1}}},
    {"ignored_parameters": ["reasoning.effort"]},
    {"warnings": [{"code": "ignored_parameter", "parameter": "temperature"}]},
])
def test_first_live_cell_guard_stops_on_reasoning_or_ignored_parameter(response):
    with pytest.raises(run.TerminalStop):
        run.validate_first_live_cell(response)


def test_first_live_cell_guard_accepts_zero_reasoning_and_no_parameter_warning():
    run.validate_first_live_cell({
        "usage": {"completion_tokens_details": {"reasoning_tokens": 0}},
        "warnings": [],
    })


def test_first_response_is_persisted_before_mark_and_validate_exactly_once():
    state = {}
    persisted = []
    sut = preflight.SUTS[0]
    response = {
        "id": "response-1",
        "usage": {"completion_tokens_details": {"reasoning_tokens": 0}},
        "warnings": [],
    }

    def persist(record):
        assert sut not in state
        persisted.append(record)

    record = run.custody_first_sut_response(
        sut=sut, response=response, persist=persist, state=state)
    assert persisted == [record]
    assert state[sut]["status"] == "PERSISTED_AND_VALIDATED"
    response["warnings"].append({"code": "ignored_parameter"})
    assert persisted[0]["response"]["warnings"] == []
    with pytest.raises(run.TerminalStop, match="already recorded"):
        run.custody_first_sut_response(
            sut=sut, response={"warnings": []}, persist=persist, state=state)
    assert len(persisted) == 1


def test_first_response_persists_once_even_when_guard_stops():
    state = {}
    persisted = []
    sut = preflight.SUTS[1]
    response = {"usage": {"completion_tokens_details": {"reasoning_tokens": 1}}}
    with pytest.raises(run.TerminalStop, match="reasoning tokens"):
        run.custody_first_sut_response(
            sut=sut, response=response, persist=persisted.append, state=state)
    assert len(persisted) == 1
    assert state[sut]["status"] == "PERSISTED_TERMINAL_GUARD_FAILURE"
    with pytest.raises(run.TerminalStop, match="already recorded"):
        run.custody_first_sut_response(
            sut=sut, response={"warnings": []}, persist=persisted.append, state=state)
    assert len(persisted) == 1


def test_subsequent_schedule_requires_validated_first_response():
    state = {}
    sut = preflight.SUTS[2]
    with pytest.raises(run.TerminalStop, match="first response"):
        run.require_validated_first_response(sut, state)
    run.custody_first_sut_response(
        sut=sut, response={"warnings": []}, persist=lambda _record: None,
        state=state)
    run.require_validated_first_response(sut, state)


def test_three_deterministic_shards_are_sequential_inside_each_worker():
    shards = run.build_sut_shards(preflight.SUTS)
    assert shards == (
        (preflight.SUTS[0], preflight.SUTS[3]),
        (preflight.SUTS[1], preflight.SUTS[4]),
        (preflight.SUTS[2], preflight.SUTS[5]),
    )
    submitted = []
    calls = []

    class ImmediateFuture:
        def __init__(self, fn, args):
            self.fn, self.args = fn, args

        def result(self):
            return self.fn(*self.args)

    class CapturingExecutor:
        def __init__(self, max_workers):
            assert max_workers == 3

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return False

        def submit(self, fn, *args):
            submitted.append(args[0])
            return ImmediateFuture(fn, args)

    def run_cell(sut, item, acknowledge_start):
        acknowledge_start()
        calls.append((sut, item))

    run.execute_sut_shards(
        shards, ("I1", "I2"),
        run_cell,
        executor_factory=CapturingExecutor,
        **_budget_kwargs(),
    )
    assert submitted == list(shards)
    assert calls == [
        (preflight.SUTS[0], "I1"), (preflight.SUTS[0], "I2"),
        (preflight.SUTS[3], "I1"), (preflight.SUTS[3], "I2"),
        (preflight.SUTS[1], "I1"), (preflight.SUTS[1], "I2"),
        (preflight.SUTS[4], "I1"), (preflight.SUTS[4], "I2"),
        (preflight.SUTS[2], "I1"), (preflight.SUTS[2], "I2"),
        (preflight.SUTS[5], "I1"), (preflight.SUTS[5], "I2"),
    ]


def test_start_acknowledgement_closes_cancellation_check_to_call_race():
    shards = tuple((sut,) for sut in preflight.SUTS[:3])
    cancellation = threading.Event()
    second_cell_entered = threading.Event()
    terminal_raising = threading.Event()
    calls = []
    calls_lock = threading.Lock()

    def run_cell(sut, item_id, acknowledge_start):
        with calls_lock:
            calls.append((sut, item_id))
        if sut == preflight.SUTS[0]:
            acknowledge_start()
            assert second_cell_entered.wait(timeout=2)
            terminal_raising.set()
            raise run.TerminalStop("registered stop")
        if sut == preflight.SUTS[1] and item_id == "I2":
            second_cell_entered.set()
            assert terminal_raising.wait(timeout=2)
            assert not cancellation.is_set()
            acknowledge_start()
            assert cancellation.wait(timeout=2)
            return (sut, item_id)
        acknowledge_start()
        if sut == preflight.SUTS[2]:
            assert cancellation.wait(timeout=2)
        return (sut, item_id)

    with pytest.raises(run.TerminalStop, match="registered stop"):
        run.execute_sut_shards(
            shards, ("I1", "I2"), run_cell,
            cancellation_event=cancellation,
            **_budget_kwargs(),
        )
    assert not any(cancellation.is_set() and item_id == "I2"
                   for sut, item_id in calls if sut == preflight.SUTS[2])


def test_reservation_failure_publishes_cancellation_before_releasing_start_lock():
    cancellation = threading.Event()
    release_states = []

    class ObservedLock:
        def acquire(self):
            return True

        def release(self):
            release_states.append(cancellation.is_set())

        def __enter__(self):
            self.acquire()
            return self

        def __exit__(self, *_args):
            self.release()

    class RejectingBudget:
        def reserve(self, _maximum_usd):
            raise run.TerminalStop("strict cap stop")

    with pytest.raises(run.TerminalStop, match="strict cap stop"):
        run._run_shard(
            (preflight.SUTS[0],), ("I1",),
            lambda *_args: pytest.fail("cell must not start"),
            cancellation, ObservedLock(), RejectingBudget(),
            lambda _sut, _item_id: 1.0, lambda _outcome: 0.0,
        )

    assert cancellation.is_set()
    assert release_states == [True]


def test_settlement_failure_overrides_cell_error_and_releases_reservation():
    cancellation = threading.Event()
    budget = run.BudgetController(cap_usd=10.0)
    cell_error = RuntimeError("cell transport failed")

    def run_cell(_sut, _item_id, acknowledge_start):
        acknowledge_start()
        raise cell_error

    with pytest.raises(run.TerminalStop, match="budget settlement failed") as caught:
        run.execute_sut_shards(
            ((preflight.SUTS[0],), (), ()), ("I1",), run_cell,
            budget=budget,
            maximum_cost_usd=lambda _sut, _item_id: 1.0,
            actual_cost_usd=lambda _outcome: 2.0,
            cancellation_event=cancellation,
        )

    assert cancellation.is_set()
    assert caught.value.__cause__ is cell_error
    assert budget.spent_usd == 0.0
    assert budget.reserved_usd == 0.0


def test_judge_batches_are_max_eight_and_never_mix_sut_or_route():
    decisions = []
    schedule = preflight.build_schedule(
        preflight.load_items(str(preflight.BANK_DIR)))
    route_counts = {"open": 310, "contested": 16, "episode": 22}
    for sut in preflight.SUTS:
        for route, count in route_counts.items():
            decisions.extend({
                "record_id": f"{sut}:{route}:{index}",
                "sut": sut,
                "route": route,
                "item_id": schedule["judge_route_item_ids"][route][
                    index % len(schedule["judge_route_item_ids"][route])],
            } for index in range(count))
    batches = run.build_judge_batches(decisions)
    assert len(batches) == 264
    assert all(1 <= len(batch) <= 8 for batch in batches)
    assert all(len({row["sut"] for row in batch}) == 1 for batch in batches)
    assert all(len({row["route"] for row in batch}) == 1 for batch in batches)
    assert sum(map(len, batches)) == 2088


@pytest.mark.parametrize("item_id", [None, "NOT-IN-BANK", "LIB-C2-W305"])
def test_judge_batches_reject_missing_foreign_or_dev_item_ids(item_id):
    with pytest.raises(run.TerminalStop, match="item"):
        run.build_judge_batches([{
            "record_id": "r1", "sut": preflight.SUTS[0], "route": "open",
            "item_id": item_id,
        }])


def test_scalar_aggregation_keeps_errors_missing_and_diagnostics_out():
    schedule = preflight.build_schedule(
        preflight.load_items(str(preflight.BANK_DIR)))
    scalar_ids = schedule["scalar_eligible_item_ids"]
    records = [
        {"sut": preflight.SUTS[0], "item_id": scalar_ids[index], "route": "open",
         "diagnostic": False, "score": 1.0 if index < 100 else 0.0,
         "error": None}
        for index in range(200)
    ]
    records.extend([
        {"sut": preflight.SUTS[0], "item_id": scalar_ids[200], "route": "open",
         "diagnostic": False, "score": None, "error": "transport"},
        {"sut": preflight.SUTS[0], "item_id": schedule["dev_set_only_item_ids"][0],
         "route": "open", "diagnostic": False, "score": 0.0, "error": None},
        {"sut": preflight.SUTS[0], "item_id": schedule["contested_item_ids"][0],
         "route": "open", "diagnostic": False, "score": 0.0, "error": None},
        {"sut": preflight.SUTS[0], "item_id": "NOT-IN-BANK", "route": "open",
         "diagnostic": False, "score": 0.0, "error": None},
    ])
    aggregate = run.aggregate_scalar_scores(records, preflight.SUTS[0])
    assert aggregate == {
        "eligible": True, "numeric": 200, "denominator": 222,
        "missing": 22, "mean": 0.5,
    }
    assert run.aggregate_scalar_scores(records[:199], preflight.SUTS[0])["eligible"] is False


def test_scalar_duplicates_cannot_inflate_numeric_sufficiency():
    schedule = preflight.build_schedule(
        preflight.load_items(str(preflight.BANK_DIR)))
    records = [{
        "sut": preflight.SUTS[0], "item_id": item_id,
        "score": 1.0, "error": None,
    } for item_id in schedule["scalar_eligible_item_ids"][:199]]
    records.extend(dict(records[0]) for _index in range(30))
    aggregate = run.aggregate_scalar_scores(records, preflight.SUTS[0])
    assert aggregate["numeric"] == 199
    assert aggregate["eligible"] is False


def test_execution_identity_resume_and_budget_stop_are_fail_closed():
    manifest = _manifest()
    identity = run.build_execution_identity(manifest, execution_id="open-first-001")
    run.validate_resume_identity(identity, copy.deepcopy(identity))
    changed = copy.deepcopy(identity)
    changed["suts"] = list(reversed(changed["suts"]))
    with pytest.raises(run.ResumeError):
        run.validate_resume_identity(identity, changed)

    budget = run.BudgetController(cap_usd=1.0)
    assert not hasattr(budget, "authorize")
    assert not hasattr(budget, "record")


def test_sut_runner_has_no_unbudgeted_execution_path():
    calls = []

    def run_cell(sut, item_id, *_args):
        calls.append((sut, item_id))

    with pytest.raises(TypeError):
        run.execute_sut_shards(
            tuple((sut,) for sut in preflight.SUTS[:3]), ("I1",),
            run_cell,
        )
    assert calls == []


def test_concurrent_budget_reservations_count_against_availability_atomically():
    budget = run.BudgetController(cap_usd=1.0)
    ready = threading.Barrier(3)

    def reserve():
        ready.wait()
        try:
            return budget.reserve(0.51)
        except run.TerminalStop:
            return None

    with ThreadPoolExecutor(max_workers=3) as executor:
        reservations = list(executor.map(lambda _index: reserve(), range(3)))
    accepted = [reservation for reservation in reservations if reservation is not None]
    assert len(accepted) == 1
    assert budget.spent_usd == 0.0
    assert budget.reserved_usd == pytest.approx(0.51)

    budget.settle(accepted[0], 0.25)
    assert budget.spent_usd == pytest.approx(0.25)
    assert budget.reserved_usd == 0.0
    second = budget.reserve(0.75)
    budget.settle(second, 0.75)
    assert budget.spent_usd == pytest.approx(1.0)
    assert budget.reserved_usd == 0.0


def test_sut_runner_reserves_maximum_cost_and_settles_actual_cost():
    shards = tuple((sut,) for sut in preflight.SUTS[:3])
    budget = run.BudgetController(cap_usd=3.0)
    calls = []

    results = run.execute_sut_shards(
        shards, ("I1",),
        lambda sut, item_id, acknowledge_start: (
            acknowledge_start() or calls.append((sut, item_id)) or {
                "sut": sut, "item_id": item_id, "actual_cost_usd": 0.25}),
        budget=budget,
        maximum_cost_usd=lambda _sut, _item_id: 0.75,
        actual_cost_usd=lambda result: result["actual_cost_usd"],
    )
    assert len(results) == 3
    assert len(calls) == 3
    assert budget.spent_usd == pytest.approx(0.75)
    assert budget.reserved_usd == 0.0
