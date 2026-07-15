from __future__ import annotations

import copy
import os
import sys

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
        "reasoning": {"effort": "none"},
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

    run.execute_sut_shards(
        shards, ("I1", "I2"),
        lambda sut, item: calls.append((sut, item)),
        executor_factory=CapturingExecutor,
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
    budget.authorize(0.75)
    budget.record(0.75)
    with pytest.raises(run.TerminalStop, match="budget"):
        budget.authorize(0.26)
