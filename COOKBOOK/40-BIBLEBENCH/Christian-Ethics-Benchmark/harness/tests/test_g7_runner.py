import copy
import json
import multiprocessing
from decimal import Decimal
from pathlib import Path

import pytest

from walkworthy.g7_runner import (
    EXCLUSION_MANIFEST_SHA256,
    HARD_NTE_USD,
    L7_INVENTORY_SHA256,
    MAX_CONCURRENCY,
    MAX_POSTS,
    PLANNED_LOGICAL_CALLS,
    PRODUCTION_MANIFEST_SHA256,
    REPLAY_RESERVE_CALLS,
    ROLE_MANIFEST_SHA256,
    AttemptLedger,
    BudgetStop,
    ContractStop,
    ThreadStop,
    default_transport_request_bytes,
    make_client,
    spec_for,
    write_once_json,
)
from walkworthy.cli_backends import ModelCallError
from walkworthy.clients import Message


EXPECTED_SPECS = {
    ("sut", "openai/gpt-4.1"): (32768, "2.00", "8.00", "0.310144000"),
    ("sut", "google/gemini-2.5-pro"): (32768, "1.25", "10.00", "0.357680000"),
    ("sut", "anthropic/claude-sonnet-4"): (32768, "3.00", "15.00", "0.563520000"),
    ("sut", "deepseek/deepseek-chat"): (32768, "0.2002", "0.8001", "0.031022477"),
    ("sut", "mistralai/mistral-large-2512"): (32768, "0.50", "1.50", "0.061152000"),
    ("sut", "meta-llama/llama-3.3-70b-instruct"): (32768, "0.10", "0.32", "0.012885760"),
    ("judge", "openai/gpt-4.1-mini"): (256, "0.40", "1.60", "0.010009600"),
    ("judge", "google/gemini-2.5-flash"): (256, "0.30", "2.50", "0.007840000"),
    ("classifier", "openai/gpt-5.6-terra"): (16, "2.50", "15.00", "0.005360000"),
    ("paraphrase_author", "mistralai/mistral-large-2512"): (4096, "0.50", "1.50", "0.018144000"),
    ("tie_breaker", "mistralai/mistral-large-2512"): (256, "0.50", "1.50", "0.012384000"),
}


def response(model, cost=0.001, text="ok"):
    return {
        "model": model,
        "usage": {"cost": cost},
        "choices": [{"message": {"content": text}}],
    }


def request(spec, marker="request"):
    return {
        "model": spec.slug,
        "max_tokens": spec.max_tokens,
        "provider": spec.provider_prefs,
        "messages": [{"role": "user", "content": marker}],
    }


def _concurrent_begin(path, expected_keys, logical_key, barrier, queue):
    spec = spec_for("classifier", "openai/gpt-5.6-terra")
    ledger = AttemptLedger(path, expected_keys=expected_keys)
    barrier.wait()
    try:
        queue.put(("ok", ledger.begin(logical_key, spec, request(spec, logical_key))))
    except Exception as exc:  # pragma: no cover - surfaced in the parent assertion
        queue.put(("error", type(exc).__name__, str(exc)))


def _write_once_worker(path, payload, barrier, queue):
    barrier.wait()
    try:
        queue.put(("ok", write_once_json(path, payload)))
    except Exception as exc:  # pragma: no cover - surfaced in the parent assertion
        queue.put((type(exc).__name__, str(exc)))


def test_exact_authorized_constants_and_decimal_role_specs():
    assert PRODUCTION_MANIFEST_SHA256 == "616d2e93491adcb8da9fc00664693cd8c4685a95fc36b6fc09816c32414edf0e"
    assert ROLE_MANIFEST_SHA256 == "013600bd2f1c34b7353319e98395aa8b1b5b921796d73a840e5ddc2138027480"
    assert L7_INVENTORY_SHA256 == "73711dd6ae89989ae0dfdad67a7a9516b84518eff0366e30fa061c70496b70b0"
    assert EXCLUSION_MANIFEST_SHA256 == "a6ebbe8f81f236033779c9d6113923ba7419de16e2d142ca622bc37c98fa0366"
    assert (PLANNED_LOGICAL_CALLS, REPLAY_RESERVE_CALLS, MAX_POSTS) == (9709, 971, 10680)
    assert MAX_CONCURRENCY == 2
    assert HARD_NTE_USD == Decimal("30.00")

    for key, (cap, input_rate, output_rate, maximum) in EXPECTED_SPECS.items():
        spec = spec_for(*key)
        assert spec.max_tokens == cap
        assert spec.input_envelope == (2048 if key[0] == "classifier" else 24000)
        assert spec.input_per_m == Decimal(input_rate)
        assert spec.output_per_m == Decimal(output_rate)
        assert spec.max_missing_cost == Decimal(maximum)
        assert spec.provider_prefs == {
            "sort": "price",
            "require_parameters": True,
            "allow_fallbacks": True,
            "max_price": {"prompt": float(Decimal(input_rate)),
                          "completion": float(Decimal(output_rate))},
        }


def test_make_client_disables_all_hidden_retries():
    spec = spec_for("sut", "openai/gpt-4.1")
    client = make_client(spec, "not-a-real-key", lambda *_args, **_kwargs: None)
    assert client.max_retries == 0
    assert client.empty_retries == 0
    assert client.max_tokens == 32768
    assert client.provider_prefs == spec.provider_prefs


def test_make_client_makes_only_one_underlying_call_on_http_failure():
    calls = []

    def transport(_url, _headers, payload, timeout=None):
        calls.append((payload, timeout))
        return 503, {"error": "offline fake"}

    spec = spec_for("sut", "openai/gpt-4.1")
    client = make_client(spec, "not-a-real-key", transport)
    with pytest.raises(ModelCallError):
        client.complete([Message("user", "offline")])
    assert len(calls) == 1


def test_begin_is_append_only_and_persists_payload_hash_not_prompt(tmp_path):
    path = tmp_path / "attempts.jsonl"
    spec = spec_for("sut", "openai/gpt-4.1")
    payload = request(spec, "SECRET PROMPT")
    ledger = AttemptLedger(path, expected_keys=("battery1/item1/sut",))
    attempt = ledger.begin("battery1/item1/sut", spec, payload)
    ledger.finish(attempt, 200, response(spec.slug, text="SECRET RESPONSE CONTENT"))

    persisted = path.read_text()
    event = json.loads(persisted.splitlines()[-2])
    assert event["event"] == "attempt_started"
    assert len(event["payload_sha256"]) == 64
    assert "SECRET PROMPT" not in persisted
    assert "SECRET RESPONSE CONTENT" not in persisted
    assert "messages" not in persisted


@pytest.mark.parametrize("field", ["model", "max_tokens", "provider"])
def test_begin_rejects_model_cap_or_provider_contract_mismatch(tmp_path, field):
    spec = spec_for("sut", "openai/gpt-4.1")
    payload = request(spec)
    if field == "model":
        payload[field] = "wrong/model"
    elif field == "max_tokens":
        payload[field] -= 1
    else:
        payload[field] = {**payload[field], "max_price": {"prompt": 999,
                                                           "completion": 999}}
    ledger = AttemptLedger(tmp_path / f"{field}.jsonl", expected_keys=("key",))
    with pytest.raises(ContractStop, match="payload contract"):
        ledger.begin("key", spec, payload)


def test_begin_rejects_request_content_over_conservative_input_envelope(tmp_path):
    spec = spec_for("classifier", "openai/gpt-5.6-terra")
    payload = request(spec, "x" * (spec.input_envelope + 1))
    ledger = AttemptLedger(tmp_path / "attempts.jsonl", expected_keys=("key",))
    with pytest.raises(ContractStop, match="input envelope"):
        ledger.begin("key", spec, payload)


def test_request_bytes_match_openrouter_default_transport_exactly():
    spec = spec_for("sut", "openai/gpt-4.1")
    payload = request(spec, "non-ASCII café")
    assert default_transport_request_bytes(payload) == json.dumps(payload).encode("utf-8")


def test_finish_requires_exact_returned_model_and_numeric_usage_cost(tmp_path):
    spec = spec_for("sut", "openai/gpt-4.1")
    ledger = AttemptLedger(
        tmp_path / "attempts.jsonl",
        expected_keys=("valid", "wrong-model", "non-numeric-cost"),
    )

    first = ledger.begin("valid", spec, request(spec, "a"))
    assert ledger.finish(first, 200, response(spec.slug, Decimal("0.0123"))) == "complete"
    assert ledger.actual_usd == Decimal("0.0123")

    second = ledger.begin("wrong-model", spec, request(spec, "b"))
    assert ledger.finish(second, 200, response("wrong/model", 0.01)) == "replay_required"
    third = ledger.begin("non-numeric-cost", spec, request(spec, "c"))
    assert ledger.finish(third, 200, response(spec.slug, "0.01")) == "replay_required"
    assert ledger.reserved_usd == spec.max_missing_cost
    assert json.loads((tmp_path / "attempts.jsonl").read_text().splitlines()[-1])["failure"] == "model_or_cost"


def test_reported_cost_above_role_max_is_failed_but_books_actual(tmp_path):
    spec = spec_for("classifier", "openai/gpt-5.6-terra")
    path = tmp_path / "attempts.jsonl"
    ledger = AttemptLedger(path, expected_keys=("key",), hard_nte_usd=Decimal("0.02"))
    attempt = ledger.begin("key", spec, request(spec))
    reported = spec.max_missing_cost + Decimal("0.001")
    assert ledger.finish(attempt, 200, response(spec.slug, reported)) == "replay_required"
    finish = json.loads(path.read_text().splitlines()[-1])
    assert finish["failure"] == "model_or_cost"
    assert finish["cost_basis"] == "reported"
    assert Decimal(finish["booked_usd"]) == reported


def test_over_max_reported_cost_appends_custody_then_stops_on_nte(tmp_path):
    spec = spec_for("classifier", "openai/gpt-5.6-terra")
    path = tmp_path / "attempts.jsonl"
    ledger = AttemptLedger(path, expected_keys=("key",), hard_nte_usd=Decimal("0.006"))
    attempt = ledger.begin("key", spec, request(spec))
    with pytest.raises(BudgetStop, match="hard NTE"):
        ledger.finish(attempt, 200, response(spec.slug, Decimal("0.007")))
    finish = json.loads(path.read_text().splitlines()[-1])
    assert finish["event"] == "attempt_finished"
    assert finish["failure"] == "model_or_cost"
    assert finish["booked_usd"] == "0.007"


def test_missing_cost_books_registered_maximum_and_requires_identical_replay(tmp_path):
    spec = spec_for("judge", "google/gemini-2.5-flash")
    ledger = AttemptLedger(tmp_path / "attempts.jsonl", expected_keys=("cell",))
    payload = request(spec, "rubric")
    first = ledger.begin("cell", spec, payload)
    assert ledger.finish(first, 200, response(spec.slug, cost=None)) == "replay_required"
    assert ledger.reserved_usd == Decimal("0.007840000")

    with pytest.raises(ContractStop, match="identical payload"):
        ledger.begin("cell", spec, request(spec, "changed rubric"))
    with pytest.raises(ContractStop, match="identical payload/model/role"):
        ledger.begin("cell", spec_for("judge", "openai/gpt-4.1-mini"),
                     request(spec_for("judge", "openai/gpt-4.1-mini"), "rubric"))
    with pytest.raises(ContractStop, match="identical payload"):
        ledger.begin("cell", spec, dict(reversed(list(payload.items()))))
    second = ledger.begin("cell", spec, copy.deepcopy(payload))
    with pytest.raises(ThreadStop, match="second failure"):
        ledger.finish(second, 200, response(spec.slug, cost=None))
    with pytest.raises(ThreadStop, match="exhausted"):
        ledger.begin("cell", spec, payload)


@pytest.mark.parametrize(
    ("status", "body"),
    [
        (503, {"error": "down"}),
        (200, response("openai/gpt-4.1", 0.01, "")),
        (200, {"model": "openai/gpt-4.1", "usage": {"cost": 0.01}}),
    ],
)
def test_failed_empty_and_malformed_results_each_allow_one_replay(tmp_path, status, body):
    spec = spec_for("sut", "openai/gpt-4.1")
    payload = request(spec, "same")
    ledger = AttemptLedger(tmp_path / "attempts.jsonl", expected_keys=("key",))
    first = ledger.begin("key", spec, payload)
    assert ledger.finish(first, status, body) == "replay_required"
    assert ledger.begin("key", spec, payload) == 2


def test_nte_includes_actual_reserved_inflight_and_next_with_decimal_math(tmp_path):
    spec = spec_for("sut", "meta-llama/llama-3.3-70b-instruct")
    ledger = AttemptLedger(
        tmp_path / "attempts.jsonl",
        expected_keys=("actual", "reserved", "inflight", "next"),
        hard_nte_usd=Decimal("0.039"),
    )
    actual = ledger.begin("actual", spec, request(spec, "actual"))
    ledger.finish(actual, 200, response(spec.slug, 0.001))
    reserved = ledger.begin("reserved", spec, request(spec, "reserved"))
    ledger.finish(reserved, 503, {})
    ledger.begin("inflight", spec, request(spec, "inflight"))

    assert ledger.actual_usd == Decimal("0.001")
    assert ledger.reserved_usd == spec.max_missing_cost
    assert ledger.inflight_usd == spec.max_missing_cost
    with pytest.raises(BudgetStop, match="hard NTE"):
        ledger.begin("next", spec, request(spec, "next"))


def test_planned_replay_and_total_post_caps_are_independent(tmp_path):
    spec = spec_for("classifier", "openai/gpt-5.6-terra")
    ledger = AttemptLedger(
        tmp_path / "attempts.jsonl",
        expected_keys=("one", "two"),
        planned_cap=1,
        replay_cap=1,
        post_cap=2,
    )
    first = ledger.begin("one", spec, request(spec, "one"))
    ledger.finish(first, 500, {})
    second = ledger.begin("one", spec, request(spec, "one"))
    ledger.finish(second, 200, response(spec.slug, 0.0))
    with pytest.raises(BudgetStop, match="planned logical"):
        ledger.begin("two", spec, request(spec, "two"))

    ledger2 = AttemptLedger(
        tmp_path / "other.jsonl",
        expected_keys=("one",), planned_cap=1, replay_cap=0, post_cap=1,
    )
    attempt = ledger2.begin("one", spec, request(spec, "one"))
    ledger2.finish(attempt, 500, {})
    with pytest.raises(BudgetStop, match="replay reserve"):
        ledger2.begin("one", spec, request(spec, "one"))

    ledger3 = AttemptLedger(
        tmp_path / "post.jsonl",
        expected_keys=("one",), planned_cap=1, replay_cap=1, post_cap=1,
    )
    attempt = ledger3.begin("one", spec, request(spec, "one"))
    ledger3.finish(attempt, 500, {})
    with pytest.raises(BudgetStop, match="POST cap"):
        ledger3.begin("one", spec, request(spec, "one"))


def test_registration_binds_exact_keys_caps_budget_and_concurrency(tmp_path):
    path = tmp_path / "attempts.jsonl"
    kwargs = {
        "hard_nte_usd": Decimal("0.50"),
        "planned_cap": 2,
        "replay_cap": 1,
        "post_cap": 3,
        "max_concurrency": 1,
    }
    AttemptLedger(path, expected_keys=("one", "two"), **kwargs)
    assert json.loads(path.read_text().splitlines()[0]) == {
        "event": "ledger_registered",
        "expected_keys": ["one", "two"],
        "hard_nte_usd": "0.50",
        "max_concurrency": 1,
        "planned_cap": 2,
        "post_cap": 3,
        "replay_cap": 1,
    }

    for field, value in {
        "hard_nte_usd": Decimal("0.49"),
        "planned_cap": 1,
        "replay_cap": 0,
        "post_cap": 2,
        "max_concurrency": 2,
    }.items():
        changed = dict(kwargs)
        changed[field] = value
        with pytest.raises(ContractStop, match="registration contract"):
            AttemptLedger(path, expected_keys=("one", "two"), **changed)


def test_process_safe_begin_assigns_unique_ids_and_caps_two_inflight(tmp_path):
    path = tmp_path / "attempts.jsonl"
    expected = ("one", "two", "three")
    AttemptLedger(path, expected_keys=expected)
    context = multiprocessing.get_context("fork")
    barrier = context.Barrier(2)
    queue = context.Queue()
    processes = [
        context.Process(target=_concurrent_begin,
                        args=(path, expected, key, barrier, queue))
        for key in ("one", "two")
    ]
    for process in processes:
        process.start()
    results = [queue.get(timeout=10) for _ in processes]
    for process in processes:
        process.join(timeout=10)
        assert process.exitcode == 0

    assert sorted(results) == [("ok", 1), ("ok", 2)]
    resumed = AttemptLedger(path, expected_keys=expected)
    spec = spec_for("classifier", "openai/gpt-5.6-terra")
    with pytest.raises(BudgetStop, match="in-flight concurrency"):
        resumed.begin("three", spec, request(spec, "three"))


def test_loader_rejects_finish_before_start(tmp_path):
    path = tmp_path / "attempts.jsonl"
    spec = spec_for("classifier", "openai/gpt-5.6-terra")
    ledger = AttemptLedger(path, expected_keys=("one",))
    attempt = ledger.begin("one", spec, request(spec))
    ledger.finish(attempt, 200, response(spec.slug))
    registration, start, finish = path.read_text().splitlines()
    path.write_text("\n".join((registration, finish, start)) + "\n")

    with pytest.raises(ContractStop, match="chronological"):
        AttemptLedger(path, expected_keys=("one",))


def test_loader_rejects_replay_start_before_first_failure(tmp_path):
    path = tmp_path / "attempts.jsonl"
    spec = spec_for("classifier", "openai/gpt-5.6-terra")
    ledger = AttemptLedger(path, expected_keys=("one",))
    first = ledger.begin("one", spec, request(spec))
    ledger.finish(first, 500, {})
    ledger.begin("one", spec, request(spec))
    registration, start1, finish1, start2 = path.read_text().splitlines()
    path.write_text("\n".join((registration, start1, start2, finish1)) + "\n")

    with pytest.raises(ContractStop, match="chronological"):
        AttemptLedger(path, expected_keys=("one",))


def test_resume_accepts_exact_keys_and_rejects_duplicates_or_extras(tmp_path):
    path = tmp_path / "attempts.jsonl"
    spec = spec_for("classifier", "openai/gpt-5.6-terra")
    ledger = AttemptLedger(path, expected_keys=("done", "remaining"))
    attempt = ledger.begin("done", spec, request(spec, "done"))
    ledger.finish(attempt, 200, response(spec.slug, 0.001))

    resumed = AttemptLedger(path, expected_keys=("done", "remaining"))
    with pytest.raises(ContractStop, match="duplicate completed key"):
        resumed.begin("done", spec, request(spec, "done"))
    with pytest.raises(ContractStop, match="unregistered logical key"):
        resumed.begin("extra", spec, request(spec, "extra"))
    with pytest.raises(ContractStop, match="expected key set"):
        AttemptLedger(path, expected_keys=("done",))


def test_resume_preserves_reported_reserved_and_pending_replay_state(tmp_path):
    path = tmp_path / "attempts.jsonl"
    spec = spec_for("classifier", "openai/gpt-5.6-terra")
    original = request(spec, "same")
    ledger = AttemptLedger(path, expected_keys=("actual", "retry"))
    actual = ledger.begin("actual", spec, request(spec, "actual"))
    ledger.finish(actual, 200, response(spec.slug, 0.001))
    failed = ledger.begin("retry", spec, original)
    ledger.finish(failed, 503, {})

    resumed = AttemptLedger(path, expected_keys=("actual", "retry"))
    assert resumed.actual_usd == Decimal("0.001")
    assert resumed.reserved_usd == spec.max_missing_cost
    with pytest.raises(ContractStop, match="identical payload"):
        resumed.begin("retry", spec, request(spec, "changed"))
    assert resumed.begin("retry", spec, copy.deepcopy(original)) == 3


def test_snapshot_refreshes_a_preexisting_coordinator_instance(tmp_path):
    path = tmp_path / "attempts.jsonl"
    spec = spec_for("classifier", "openai/gpt-5.6-terra")
    coordinator = AttemptLedger(path, expected_keys=("key",))
    writer = AttemptLedger(path, expected_keys=("key",))
    attempt = writer.begin("key", spec, request(spec))

    assert coordinator.snapshot() == {
        "planned": 1,
        "replay": 0,
        "posts": 1,
        "actual": Decimal("0"),
        "reserved": Decimal("0"),
        "inflight": spec.max_missing_cost,
    }
    writer.finish(attempt, 200, response(spec.slug, Decimal("0.001")))
    assert coordinator.actual_usd == Decimal("0.001")
    assert coordinator.inflight_usd == Decimal("0")


def test_resume_rejects_duplicate_attempt_events(tmp_path):
    path = tmp_path / "attempts.jsonl"
    spec = spec_for("classifier", "openai/gpt-5.6-terra")
    ledger = AttemptLedger(path, expected_keys=("one",))
    ledger.begin("one", spec, request(spec, "one"))
    first_line = path.read_text().splitlines()[1]
    with path.open("a", encoding="utf-8") as handle:
        handle.write(first_line + "\n")
    with pytest.raises(ContractStop, match="duplicate attempt"):
        AttemptLedger(path, expected_keys=("one",))


def test_resume_rejects_tampered_finish_cost(tmp_path):
    path = tmp_path / "attempts.jsonl"
    spec = spec_for("classifier", "openai/gpt-5.6-terra")
    ledger = AttemptLedger(path, expected_keys=("one",))
    attempt = ledger.begin("one", spec, request(spec, "one"))
    ledger.finish(attempt, 200, response(spec.slug, 0.001))
    lines = path.read_text().splitlines()
    finish = json.loads(lines[-1])
    finish["booked_usd"] = "-1"
    lines[-1] = json.dumps(finish)
    path.write_text("\n".join(lines) + "\n")

    with pytest.raises(ContractStop, match="finish contract"):
        AttemptLedger(path, expected_keys=("one",))


@pytest.mark.parametrize(
    "changes",
    [
        {"status": 500},
        {"returned_model": "wrong/model"},
        {"failure": "http_failure", "status": 200},
        {"failure": "missing_cost", "cost_basis": "reported"},
        {"failure": "empty", "returned_model": "wrong/model"},
        {"failure": "malformed", "cost_basis": "registered_max"},
        {"failure": "model_or_cost", "status": 503},
    ],
)
def test_resume_rejects_impossible_finish_combinations(tmp_path, changes):
    path = tmp_path / "attempts.jsonl"
    spec = spec_for("classifier", "openai/gpt-5.6-terra")
    ledger = AttemptLedger(path, expected_keys=("one",))
    attempt = ledger.begin("one", spec, request(spec))
    ledger.finish(attempt, 200, response(spec.slug, 0.001))
    lines = path.read_text().splitlines()
    finish = json.loads(lines[-1])
    finish.update(changes)
    if finish["cost_basis"] == "registered_max":
        finish["booked_usd"] = str(spec.max_missing_cost)
    lines[-1] = json.dumps(finish)
    path.write_text("\n".join(lines) + "\n")

    with pytest.raises(ContractStop, match="finish contract"):
        AttemptLedger(path, expected_keys=("one",))


def test_write_once_json_is_immutable_and_idempotent(tmp_path):
    path = tmp_path / "checkpoint.json"
    payload = {"stage": "cheap-first", "attempts": 4}
    assert write_once_json(path, payload) == payload
    assert write_once_json(path, payload) == payload
    with pytest.raises(ContractStop, match="immutable"):
        write_once_json(path, {"stage": "changed"})
    assert json.loads(path.read_text()) == payload


def test_write_once_json_serializes_concurrent_identical_and_conflicting_writers(tmp_path):
    context = multiprocessing.get_context("fork")
    identical_path = tmp_path / "identical.json"
    barrier = context.Barrier(2)
    queue = context.Queue()
    processes = [context.Process(target=_write_once_worker,
                                 args=(identical_path, {"value": 1}, barrier, queue))
                 for _ in range(2)]
    for process in processes:
        process.start()
    results = [queue.get(timeout=10) for _ in processes]
    for process in processes:
        process.join(timeout=10)
        assert process.exitcode == 0
    assert results == [("ok", {"value": 1}), ("ok", {"value": 1})]
    assert Path(str(identical_path) + ".lock").exists()

    conflict_path = tmp_path / "conflict.json"
    barrier = context.Barrier(2)
    queue = context.Queue()
    processes = [
        context.Process(target=_write_once_worker,
                        args=(conflict_path, {"value": value}, barrier, queue))
        for value in (1, 2)
    ]
    for process in processes:
        process.start()
    results = [queue.get(timeout=10) for _ in processes]
    for process in processes:
        process.join(timeout=10)
        assert process.exitcode == 0
    assert sorted(result[0] for result in results) == ["ContractStop", "ok"]
