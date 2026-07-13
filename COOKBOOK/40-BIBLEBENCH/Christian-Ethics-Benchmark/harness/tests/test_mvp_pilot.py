"""MVP-A1 mechanics tests. No credential or network access."""

import json

import pytest

from walkworthy import mvp_pilot as mvp
from walkworthy.clients import Message, MockModelClient
from walkworthy.executors import execute_item
from walkworthy.manifest import FIXED_PERMUTATION_SEEDS


def test_exact_mvp_selector_and_hash(benchmark_root):
    items = mvp.select_mvp_items(benchmark_root)
    assert len(items) == 60
    assert len({item.id for item in items}) == 60
    assert mvp.ordered_item_hash(items) == mvp.MANIFEST_SHA256
    assert [item.id for item in items[:6]] == [
        "WW-01-B03", "WW-01-D04", "WW-01-A01", "WW-01-A05",
        "WW-01-A05-P", "WW-01-B01",
    ]
    for design in mvp.DESIGN_CODES:
        selected = [item for item in items if item.design == design]
        assert [item.difficulty for item in selected] == [
            "easy", "easy", "hard", "hard", "hard", "hard",
        ]


def test_exact_roster_caps_and_price_sorted_provider_ceiling():
    seen = []

    def transport(url, headers, payload, timeout=None):
        seen.append(payload)
        return 200, {
            "choices": [{"message": {"content": "ok"}}],
            "model": payload["model"],
            "usage": {"cost": 0.000001, "prompt_tokens": 1,
                      "completion_tokens": 1},
        }

    for spec in mvp.ALL_MODEL_SPECS:
        client = mvp.make_client(spec, "secret", transport)
        payload = client.build_payload([Message("user", "probe")], None)
        assert payload["model"] == spec.slug
        assert payload["max_tokens"] == spec.max_tokens
        assert payload["provider"] == {
            "sort": "price",
            "require_parameters": True,
            "allow_fallbacks": True,
            "max_price": {"prompt": spec.input_per_m,
                          "completion": spec.output_per_m},
        }


def test_attempt_ledger_is_append_only_resume_safe_and_redacts_prompts(tmp_path):
    path = tmp_path / "attempts.jsonl"
    ledger = mvp.AttemptLedger(path)
    attempt = ledger.begin(
        model=mvp.SUT_SPECS[0].slug,
        role="sut",
        max_call_usd=mvp.SUT_SPECS[0].max_call_usd,
        payload={"model": mvp.SUT_SPECS[0].slug,
                 "messages": [{"role": "user", "content": "private prompt"}]},
    )
    ledger.finish(attempt, 200, {
        "model": mvp.SUT_SPECS[0].slug,
        "usage": {"cost": 0.0123, "prompt_tokens": 50,
                  "completion_tokens": 10},
    })
    resumed = mvp.AttemptLedger(path)
    assert resumed.snapshot()["attempts_started"] == 1
    assert resumed.snapshot()["completed_responses"] == 1
    assert resumed.snapshot()["actual_usd"] == pytest.approx(0.0123)
    raw = path.read_text()
    assert "private prompt" not in raw
    assert "payload_sha256" in raw


@pytest.mark.parametrize(
    ("event_index", "field", "value"),
    [
        (0, "requested_model", "other/model"),
        (0, "role", "judge"),
        (0, "max_call_usd", 0.0),
        (1, "requested_model", "other/model"),
        (1, "returned_model", "other/model"),
        (1, "actual_usd", -0.01),
        (1, "actual_usd", float("nan")),
        (1, "actual_usd", 5.01),
        (1, "prompt_tokens", -1),
        (1, "completion_tokens", 1.5),
    ],
)
def test_attempt_ledger_resume_rejects_tampered_persisted_events(
        tmp_path, event_index, field, value):
    path = tmp_path / f"tampered-{event_index}-{field}.jsonl"
    spec = mvp.SUT_SPECS[0]
    ledger = mvp.AttemptLedger(path)
    attempt = ledger.begin(
        model=spec.slug, role="sut", max_call_usd=spec.max_call_usd,
        payload={"model": spec.slug, "messages": []},
    )
    ledger.finish(attempt, 200, {
        "model": spec.slug,
        "usage": {"cost": 0.0001, "prompt_tokens": 10,
                  "completion_tokens": 2},
    })
    events = [json.loads(line) for line in path.read_text().splitlines()]
    events[event_index][field] = value
    path.write_text("".join(json.dumps(event) + "\n" for event in events))
    with pytest.raises(mvp.ContractStop, match="persisted attempt"):
        mvp.AttemptLedger(path)


def test_attempt_ledger_stops_before_cost_or_call_cap(tmp_path):
    ledger = mvp.AttemptLedger(tmp_path / "attempts.jsonl", hard_nte_usd=0.01,
                               max_attempts=1)
    first = ledger.begin(model="x/y", role="probe", max_call_usd=0.009,
                         payload={"model": "x/y", "messages": []})
    ledger.finish(first, 200, {"usage": {"cost": 0.009}})
    with pytest.raises(mvp.BudgetStop, match="call envelope"):
        ledger.begin(model="x/y", role="probe", max_call_usd=0.0001,
                     payload={"model": "x/y", "messages": []})

    money = mvp.AttemptLedger(tmp_path / "money.jsonl", hard_nte_usd=0.01,
                              max_attempts=10)
    attempt = money.begin(model="x/y", role="probe", max_call_usd=0.009,
                          payload={"model": "x/y", "messages": []})
    money.finish(attempt, 200, {"usage": {"cost": 0.009}})
    with pytest.raises(mvp.BudgetStop, match="hard NTE"):
        money.begin(model="x/y", role="probe", max_call_usd=0.002,
                    payload={"model": "x/y", "messages": []})


def test_attempt_ledger_reserves_unfinished_envelopes_and_rejects_weakened_caps(tmp_path):
    ledger = mvp.AttemptLedger(tmp_path / "attempts.jsonl", hard_nte_usd=0.01,
                               max_attempts=10)
    ledger.begin(model="x/y", role="probe", max_call_usd=0.009,
                 payload={"model": "x/y", "messages": []})
    with pytest.raises(mvp.BudgetStop, match="hard NTE"):
        ledger.begin(model="x/y", role="probe", max_call_usd=0.002,
                     payload={"model": "x/y", "messages": []})
    with pytest.raises(ValueError, match="cannot exceed authorized"):
        mvp.AttemptLedger(tmp_path / "weak-money.jsonl", hard_nte_usd=5.01)
    with pytest.raises(ValueError, match="cannot exceed authorized"):
        mvp.AttemptLedger(tmp_path / "weak-calls.jsonl", max_attempts=1835)


@pytest.mark.parametrize("bad_cost", [None, -0.01, float("nan")])
def test_attempt_ledger_never_accepts_unknown_negative_or_nonfinite_cost(
        tmp_path, bad_cost):
    ledger = mvp.AttemptLedger(tmp_path / f"bad-{repr(bad_cost)}.jsonl")
    attempt = ledger.begin(model="x/y", role="probe", max_call_usd=0.001,
                           payload={"model": "x/y", "messages": []})
    usage = {} if bad_cost is None else {"cost": bad_cost}
    with pytest.raises(mvp.ContractStop, match="usage.cost"):
        ledger.finish(attempt, 200, {"usage": usage})


def test_guarded_transport_records_then_rejects_returned_model_substitution(tmp_path):
    ledger = mvp.AttemptLedger(tmp_path / "attempts.jsonl")

    def base(url, headers, payload, timeout=None):
        return 200, {
            "choices": [{"message": {"content": "ok"}}],
            "model": "provider/returned-build",
            "usage": {"cost": 0.0002, "prompt_tokens": 10,
                      "completion_tokens": 2},
        }

    spec = mvp.SUT_SPECS[0]
    transport = mvp.guarded_transport(base, ledger, spec, "sut")
    client = mvp.make_client(spec, "secret", transport)
    with pytest.raises(mvp.ContractStop, match="returned model substitution"):
        client.complete([Message("user", "hello")])
    events = [json.loads(line) for line in (tmp_path / "attempts.jsonl").read_text().splitlines()]
    assert events[-1]["requested_model"] == spec.slug
    assert events[-1]["returned_model"] == "provider/returned-build"
    assert events[-1]["role"] == "sut"


def test_execution_roundtrip_preserves_full_transcript(benchmark_root):
    item = mvp.select_mvp_items(benchmark_root)[6]
    execution = execute_item(
        item, MockModelClient("mock-sut"), FIXED_PERMUTATION_SEEDS,
        state_classifier=lambda _text, states, _design: states[0],
    )
    restored = mvp.execution_from_dict(mvp.execution_to_dict(execution))
    assert restored == execution


def test_checkpoint_requires_six_of_six_per_design_and_sut():
    records = []
    by_design = {design: [] for design in mvp.DESIGN_CODES}
    for item_id in mvp.MVP_ITEM_IDS:
        design = next(d for d in mvp.DESIGN_CODES if item_id.startswith(
            f"WW-{d.split('-', 1)[0]}-"))
        by_design[design].append(item_id)
    for design in mvp.DESIGN_CODES:
        for sut in mvp.SUT_SPECS:
            for item_id in by_design[design]:
                records.append({"design": design, "model": sut.slug,
                                "item_id": item_id})
    coverage = mvp.coverage_table(records)
    assert len(coverage) == 30
    assert all(row["registered"] == 6 and row["complete"] == 6
               and row["status"] == "COMPLETE" for row in coverage)

    incomplete = mvp.coverage_table(records[:-1])
    assert incomplete[-1]["complete"] == 5
    assert incomplete[-1]["percent"] == pytest.approx(83.333333, rel=1e-5)
    assert incomplete[-1]["status"] == "INCOMPLETE"

    wrong = list(records)
    wrong[-1] = {**wrong[-1], "item_id": "WW-10-NOT-AUTHORIZED"}
    with pytest.raises(mvp.ContractStop, match="execution key"):
        mvp.coverage_table(wrong)


def test_pre_meta_checkpoint_includes_unused_reserve(tmp_path):
    ledger = mvp.AttemptLedger(tmp_path / "attempts.jsonl")
    checkpoint = mvp.write_pre_meta_checkpoint(
        tmp_path / "checkpoint.json", ledger, [], [], probe_records=[], errors=[],
    )
    assert checkpoint["remaining_meta_envelope_usd"] == pytest.approx(1.1913216)
    assert checkpoint["unused_reserve_usd"] == pytest.approx(0.62455328)
    assert checkpoint["projected_total_usd"] <= mvp.HARD_NTE_USD
    assert checkpoint["continue_meta"] is False
    assert checkpoint["prerequisites"]["five_probes"] is False
    assert checkpoint["prerequisites"]["executions_180"] is False
    assert checkpoint["prerequisites"]["openai_units_480"] is False


def test_pre_meta_checkpoint_consumes_reserve_after_pre_meta_baseline(tmp_path):
    class FakeLedger:
        hard_nte_usd = 5.0

        @staticmethod
        def snapshot():
            return {"attempts_started": 1188, "completed_responses": 1188,
                    "actual_usd": 0.25, "unresolved_attempts": []}

    executions = [
        {"design": design, "model": sut.slug, "item_id": item_id}
        for design in mvp.DESIGN_CODES
        for sut in mvp.SUT_SPECS
        for item_id in mvp.MVP_IDS_BY_DESIGN[design]
    ]
    verdicts = [
        {"judge": mvp.JUDGE_SPECS[0].slug, "call_units": 480}
    ]
    probes = [{"model": spec.slug, "ok": True} for spec in mvp.ALL_MODEL_SPECS]
    checkpoint = mvp.write_pre_meta_checkpoint(
        tmp_path / "checkpoint.json", FakeLedger(), executions, verdicts,
        probe_records=probes, errors=[],
    )
    assert checkpoint["unused_reserve_calls"] == 166
    assert checkpoint["prerequisites"] == {
        "five_probes": True,
        "executions_180": True,
        "openai_units_480": True,
        "openai_judge_defects_zero": True,
        "no_unresolved_attempts": True,
        "no_errors": True,
        "remaining_call_capacity": True,
    }
    assert checkpoint["continue_meta"] is True

    before = (tmp_path / "checkpoint.json").read_bytes()
    assert mvp.write_pre_meta_checkpoint(
        tmp_path / "checkpoint.json", FakeLedger(), executions, verdicts,
        probe_records=probes, errors=[],
    ) == checkpoint
    assert (tmp_path / "checkpoint.json").read_bytes() == before


def test_pre_meta_checkpoint_requires_capacity_for_all_meta_calls(tmp_path):
    class FakeLedger:
        hard_nte_usd = 5.0
        max_attempts = mvp.MAX_ATTEMPTS

        @staticmethod
        def snapshot():
            return {
                "attempts_started": mvp.MAX_ATTEMPTS - mvp.META_JUDGE_CALLS + 1,
                "completed_responses": mvp.MAX_ATTEMPTS - mvp.META_JUDGE_CALLS + 1,
                "actual_usd": 0.25,
                "unresolved_attempts": [],
            }

    executions = [
        {"design": design, "model": sut.slug, "item_id": item_id}
        for design in mvp.DESIGN_CODES
        for sut in mvp.SUT_SPECS
        for item_id in mvp.MVP_IDS_BY_DESIGN[design]
    ]
    verdicts = [{
        "judge": mvp.JUDGE_SPECS[0].slug,
        "call_units": mvp.META_JUDGE_CALLS,
        "defects": [],
    }]
    probes = [{"model": spec.slug, "ok": True} for spec in mvp.ALL_MODEL_SPECS]
    checkpoint = mvp.write_pre_meta_checkpoint(
        tmp_path / "capacity.json", FakeLedger(), executions, verdicts,
        probe_records=probes, errors=[],
    )
    assert checkpoint["available_attempts"] == mvp.META_JUDGE_CALLS - 1
    assert checkpoint["prerequisites"]["remaining_call_capacity"] is False
    assert checkpoint["continue_meta"] is False


def test_openai_judge_defect_fails_pre_meta_checkpoint(tmp_path):
    class FakeLedger:
        hard_nte_usd = 5.0
        max_attempts = mvp.MAX_ATTEMPTS

        @staticmethod
        def snapshot():
            return {"attempts_started": 1187, "completed_responses": 1187,
                    "actual_usd": 0.25, "unresolved_attempts": []}

    executions = [
        {"design": design, "model": sut.slug, "item_id": item_id}
        for design in mvp.DESIGN_CODES
        for sut in mvp.SUT_SPECS
        for item_id in mvp.MVP_IDS_BY_DESIGN[design]
    ]
    verdicts = [{
        "judge": mvp.JUDGE_SPECS[0].slug,
        "call_units": mvp.META_JUDGE_CALLS,
        "defects": ["malformed verdict"],
    }]
    probes = [{"model": spec.slug, "ok": True} for spec in mvp.ALL_MODEL_SPECS]
    checkpoint = mvp.write_pre_meta_checkpoint(
        tmp_path / "defect.json", FakeLedger(), executions, verdicts,
        probe_records=probes, errors=[],
    )
    assert checkpoint["openai_judge_defects"] == 1
    assert checkpoint["prerequisites"]["openai_judge_defects_zero"] is False
    assert checkpoint["continue_meta"] is False


def test_probe_specs_use_256_token_cap_and_guarded_transport_rejects_payload_drift(
        tmp_path):
    probe = mvp.probe_spec(mvp.SUT_SPECS[0])
    assert probe.max_tokens == 256
    assert probe.input_envelope == 1024

    ledger = mvp.AttemptLedger(tmp_path / "attempts.jsonl")
    called = []

    def base(*args, **kwargs):
        called.append(True)
        return 200, {"usage": {"cost": 0.000001}, "model": probe.slug,
                     "choices": [{"message": {"content": "ok"}}]}

    transport = mvp.guarded_transport(base, ledger, probe, "probe")
    payload = {"model": probe.slug, "messages": [], "max_tokens": 2048,
               "provider": probe.provider_prefs}
    with pytest.raises(mvp.ContractStop, match="payload contract"):
        transport("url", {}, payload)
    assert called == []


def test_selector_retains_holdout_refusal(benchmark_root):
    from walkworthy.loader import HoldoutAccessError
    with pytest.raises(HoldoutAccessError):
        mvp.select_mvp_items(benchmark_root / "HOLDOUT")
