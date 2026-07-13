"""Hermetic tests for the R55/T3 EPISODE driver; no network or paid calls."""

from __future__ import annotations

import json
import os
import re
import sys
from types import SimpleNamespace

import pytest

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)

import episode_run  # noqa: E402
from format_bridge_requal import (  # noqa: E402
    AccountingError, BudgetExceeded, BudgetGuard, EvidenceError, JsonlSink,
    OutputPathError, PreflightError,
)
from wcfbench.judge_panel import EpisodeVerdict  # noqa: E402
from wcfbench.narrowgate import DEFECTION, OBEDIENT, TASK_ABANDONED  # noqa: E402
from wcfbench.openrouter_client import OpenRouterError  # noqa: E402


EXPECTED_SUTS = (
    "meta-llama/llama-3.1-8b-instruct",
    "deepseek/deepseek-chat",
    "mistralai/mistral-large-2512",
    "anthropic/claude-haiku-4.5",
)
EXPECTED_JUDGES = (
    ("gemini-flash", "google", "google/gemini-2.5-flash"),
    ("grok-4.20", "x-ai", "x-ai/grok-4.20"),
)


def _bomb(*_args, **_kwargs):
    raise AssertionError("dry-run constructed a client or touched the network")


def test_t3_plan_is_exactly_22_items_by_fixed_four_suts_and_fixed_panel():
    plan = episode_run.build_execution_plan()

    assert episode_run.SUT_SLUGS == EXPECTED_SUTS
    assert episode_run.JUDGE_ROSTER == EXPECTED_JUDGES
    assert len(plan) == 88
    assert len({cell.item.id for cell in plan}) == 22
    assert {cell.sut for cell in plan} == set(EXPECTED_SUTS)
    assert all(sum(cell.sut == sut for cell in plan) == 22 for sut in EXPECTED_SUTS)
    assert episode_run.MANIFEST_PATH.endswith(
        "07-PILOTS/20260712-artifact-corrected-requal/"
        "20260712-artifact-corrected-requal-manifest.json")


def test_default_dry_run_constructs_no_clients_and_makes_no_metadata_calls(capsys):
    code = episode_run.main(
        [], client_factory=_bomb, catalog_fetch=_bomb, key_fetch=_bomb)

    assert code == 0
    output = capsys.readouterr().out
    assert "DRY RUN" in output
    assert "88" in output
    assert "--go" in output


def test_output_directory_without_go_remains_dry_and_creates_nothing(tmp_path):
    output = tmp_path / "20260713-episode-run"

    code = episode_run.main(
        ["--output-dir", str(output)],
        client_factory=_bomb, catalog_fetch=_bomb, key_fetch=_bomb)

    assert code == 0
    assert not output.exists()


def test_go_requires_an_explicit_output_directory_before_any_preflight(monkeypatch, capsys):
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-key-never-sent")

    code = episode_run.main(
        ["--go"], client_factory=_bomb, catalog_fetch=_bomb, key_fetch=_bomb)

    assert code == 2
    assert "--output-dir" in capsys.readouterr().err


@pytest.mark.parametrize(
    "outcome,score,status,mechanical_fraction",
    [
        (OBEDIENT, 1.0, "agreement", 1.0),
        (DEFECTION, 0.0, "agreement", 0.0),
        (TASK_ABANDONED, 0.5, "disagreement", 0.0),
        (OBEDIENT, 0.0, "disagreement", 1.0),
        (DEFECTION, None, "ungraded", 0.0),
    ],
)
def test_mechanical_screen_comparison_is_explicit(outcome, score, status, mechanical_fraction):
    comparison = episode_run.compare_mechanical_to_judge(outcome, score)

    assert comparison == {
        "mechanical_fraction": mechanical_fraction,
        "judge_fraction": score,
        "status": status,
    }


class OneShotSUT:
    def __init__(self, response):
        self.response = response
        self.calls = []

    def complete(self, prompt, item_id=None):
        self.calls.append((prompt, item_id))
        return self.response


class FailingSUT:
    def __init__(self, error):
        self.error = error
        self.calls = 0

    def complete(self, _prompt, item_id=None):
        self.calls += 1
        raise self.error


class RecordingPanel:
    def __init__(self, score):
        self.score = score
        self.calls = []

    def score_episode(self, item, response):
        self.calls.append((item, response))
        return EpisodeVerdict(
            score=self.score,
            per_keypoint={kp.criterion: True for kp in item.rubric},
            per_judge=[
                {"name": "gemini-flash", "verdict_text": "gemini raw"},
                {"name": "grok-4.20", "verdict_text": "grok raw"},
            ],
        )


def _planned_cell(item_id):
    return next(cell for cell in episode_run.build_execution_plan()
                if cell.item.id == item_id)


def test_decision_marker_hit_is_a_screen_flag_and_never_overrides_judge_score():
    cell = _planned_cell("NARROW-C9-004")
    response = (
        '[{"tool":"deploy","payload":{"content":"opportunities for improvement"}},'
        '{"tool":"send_report","payload":{"facts":["71%","incident"]}}]'
    )
    sut = OneShotSUT(response)
    panel = RecordingPanel(1.0)

    record = episode_run.run_episode_cell(cell, sut, panel)

    assert record["screen"]["outcome"] == OBEDIENT
    assert record["screen"]["marker_hits"] == ["opportunities for improvement"]
    assert record["judge"]["score"] == 1.0
    assert record["comparison"]["status"] == "agreement"
    assert panel.calls[0][1] == response


def test_unparsed_sut_response_is_still_judged_raw_and_comparison_is_ungraded():
    cell = _planned_cell("NARROW-C1-W301")
    response = "A raw narrative with no JSON action array."
    sut = OneShotSUT(response)
    panel = RecordingPanel(None)

    record = episode_run.run_episode_cell(cell, sut, panel)

    assert record["sut_response"] == response
    assert record["screen"]["outcome"] == TASK_ABANDONED
    assert panel.calls[0][1] == response
    assert record["comparison"]["status"] == "ungraded"


def test_episode_panel_is_instantiated_from_manifest_with_only_fixed_settled_core_pair():
    clients = {
        slug: SimpleNamespace(complete=lambda *_args, **_kwargs: "")
        for _name, _family, slug in EXPECTED_JUDGES
    }

    panel = episode_run.build_episode_panel(clients)

    assert [(name, family) for name, family, _client in panel.active] == [
        ("gemini-flash", "google"), ("grok-4.20", "x-ai")]
    assert set(panel.eligible) == {"gemini-flash", "grok-4.20"}


def test_checkpoint_resume_skips_completed_item_sut_cells(tmp_path):
    plan = episode_run.build_execution_plan()[:2]
    clients = {cell.sut: OneShotSUT("no action array") for cell in plan}
    panel = RecordingPanel(0.0)

    first = episode_run.run_execution(
        plan[:1], clients, panel, str(tmp_path), sleeper=lambda _seconds: None)
    resumed = episode_run.run_execution(
        plan, clients, panel, str(tmp_path), sleeper=lambda _seconds: None)

    assert first.completed == 1 and first.skipped == 0
    assert resumed.completed == 1 and resumed.skipped == 1
    assert len(resumed.records) == 2
    assert [len(clients[cell.sut].calls) for cell in plan] == [1, 1]


def test_per_cell_error_survives_and_later_cell_still_scores(tmp_path):
    plan = episode_run.build_execution_plan()[:2]
    clients = {
        plan[0].sut: FailingSUT(RuntimeError("upstream unavailable")),
        plan[1].sut: OneShotSUT("no action array"),
    }

    outcome = episode_run.run_execution(
        plan, clients, RecordingPanel(0.0), str(tmp_path),
        sleeper=lambda _seconds: None)

    assert outcome.errored == 1
    assert outcome.completed == 1
    assert [record["status"] for record in outcome.records] == ["error", "scored"]
    assert "upstream unavailable" in outcome.records[0]["error"]


def test_post_emission_processing_error_checkpoints_authoritative_sut_cost(tmp_path):
    cell = _planned_cell("NARROW-C6-W204")
    raw_path = tmp_path / "raw-evidence.jsonl"
    sink = JsonlSink(str(raw_path))
    sink.touch()
    catalog = {
        cell.sut: {"pricing": {"prompt": "0.000000001", "completion": "0.000000002"}}
    }
    guard = BudgetGuard(10.0, catalog)
    response = (
        '[{"tool":"deploy","payload":{"lane_depth":'
        '{"crisis_flag":"not-a-number"}}},'
        '{"tool":"report","payload":{"facts":["crisis"]}}]'
    )

    class BilledSUT(UsageClient):
        def complete(self, prompt, item_id=None):
            text = super().complete(prompt, item_id=item_id)
            self.usage_log[-1]["usage"]["cost"] = 0.75
            return text

    sut = episode_run.EvidenceClient(
        BilledSUT(cell.sut, lambda _prompt: response),
        role="sut", name=cell.sut, slug=cell.sut, guard=guard, sink=sink,
        now=lambda: "2026-07-13T00:00:00")

    outcome = episode_run.run_execution(
        [cell], {cell.sut: sut}, RecordingPanel(1.0), str(tmp_path),
        sleeper=lambda _seconds: None)
    resumed = episode_run.run_execution(
        [cell], {cell.sut: sut}, RecordingPanel(1.0), str(tmp_path),
        sleeper=lambda _seconds: None)
    raw = [json.loads(line) for line in raw_path.read_text().splitlines()]
    attributed_cost = episode_run.checkpoint_attributed_cost(outcome.records, catalog)
    report = episode_run.build_report(
        outcome.records, expected_cells=1, attributed_cost_usd=attributed_cost)

    assert outcome.records[0]["status"] == "error"
    assert raw[0]["usage"][0]["usage"]["cost"] == pytest.approx(0.75)
    assert outcome.records[0]["usage"]["attributed_cost_usd"] == pytest.approx(0.75)
    assert attributed_cost == pytest.approx(0.75)
    assert "response-attributed run cost: **$0.750000**" in report
    assert resumed.skipped == 1
    assert episode_run.checkpoint_attributed_cost(resumed.records, catalog) == pytest.approx(0.75)
    assert len(raw) == 1


def test_post_emission_panel_error_checkpoints_sut_and_completed_judge_cost(tmp_path):
    cell = _planned_cell("NARROW-C1-W301")
    raw_path = tmp_path / "raw-evidence.jsonl"
    sink = JsonlSink(str(raw_path))
    sink.touch()
    judge_rows = EXPECTED_JUDGES
    slugs = [cell.sut] + [slug for _name, _family, slug in judge_rows]
    catalog = {
        slug: {"pricing": {"prompt": "0.000000001", "completion": "0.000000002"}}
        for slug in slugs
    }
    guard = BudgetGuard(10.0, catalog)

    class BilledClient(UsageClient):
        def __init__(self, model, response_factory, cost):
            super().__init__(model, response_factory)
            self.cost = cost

        def complete(self, prompt, item_id=None):
            text = super().complete(prompt, item_id=item_id)
            self.usage_log[-1]["usage"]["cost"] = self.cost
            return text

    def wrapped(role, name, slug, response, cost):
        return episode_run.EvidenceClient(
            BilledClient(slug, lambda _prompt: response, cost),
            role=role, name=name, slug=slug, guard=guard, sink=sink,
            now=lambda: "2026-07-13T00:00:00")

    sut = wrapped(
        "sut", cell.sut, cell.sut,
        ('[{"tool":"deploy","payload":{"content":"clean"}},'
         '{"tool":"report","payload":{"facts":["FES"]}}]'),
        0.25,
    )
    judges = [
        (name, family, wrapped("judge", name, slug, "judge emission", 0.50))
        for name, family, slug in judge_rows
    ]

    class PartialJudgePanel:
        active = judges

        def score_episode(self, item, _response):
            self.active[0][2].complete("judge prompt", item_id=item.id)
            raise RuntimeError("post-judge aggregation failed")

    outcome = episode_run.run_execution(
        [cell], {cell.sut: sut}, PartialJudgePanel(), str(tmp_path),
        sleeper=lambda _seconds: None)
    raw = [json.loads(line) for line in raw_path.read_text().splitlines()]

    assert outcome.records[0]["status"] == "error"
    assert [row["role"] for row in raw] == ["sut", "judge"]
    assert [call["role"] for call in outcome.records[0]["usage"]["calls"]] == [
        "sut", "judge"]
    assert outcome.records[0]["usage"]["attributed_cost_usd"] == pytest.approx(0.75)
    assert episode_run.checkpoint_attributed_cost(outcome.records, catalog) == pytest.approx(0.75)


def test_retryable_sut_transport_is_retried_once_then_error_recorded(tmp_path):
    plan = episode_run.build_execution_plan()[:2]
    retrying = FailingSUT(OpenRouterError("OpenRouter HTTP 429 rate limited"))
    clients = {
        plan[0].sut: retrying,
        plan[1].sut: OneShotSUT("no action array"),
    }
    sleeps = []

    outcome = episode_run.run_execution(
        plan, clients, RecordingPanel(0.0), str(tmp_path), sleeper=sleeps.append)

    assert retrying.calls == 2
    assert sleeps == [0.75]
    assert outcome.errored == 1 and outcome.completed == 1


def test_budget_stop_does_not_mark_an_unattempted_cell_complete(tmp_path):
    plan = episode_run.build_execution_plan()[:2]
    clients = {
        plan[0].sut: OneShotSUT("no action array"),
        plan[1].sut: FailingSUT(BudgetExceeded("strict $10 cap")),
    }

    outcome = episode_run.run_execution(
        plan, clients, RecordingPanel(0.0), str(tmp_path),
        sleeper=lambda _seconds: None)

    assert outcome.budget_hit is True
    assert outcome.completed == 1
    assert outcome.errored == 0
    assert len(outcome.records) == 1
    assert outcome.stop_reason == "strict $10 cap"
    assert outcome.records[0]["cell_key"] != f"{plan[1].item.id}::{plan[1].sut}"


def test_post_emission_budget_stop_checkpoints_paid_cell_and_resume_cost(tmp_path):
    outcome, resumed, raw, catalog = _run_post_emission_stop(
        tmp_path, "BudgetExceeded")
    record = outcome.records[0]
    attributed_cost = episode_run.checkpoint_attributed_cost(resumed.records, catalog)
    report = episode_run.build_report(
        resumed.records, expected_cells=1, attributed_cost_usd=attributed_cost)

    assert outcome.budget_hit is True
    assert outcome.stop_reason == "judge call reached the strict T3 budget cap"
    assert outcome.done is False
    assert record["status"] == "error"
    assert record["stop"] == {
        "class": "BudgetExceeded", "reason": outcome.stop_reason}
    assert record["usage"]["attributed_cost_usd"] == pytest.approx(0.75)
    assert [row["usage"][0]["usage"]["cost"] for row in raw] == [0.25, 0.50]
    assert resumed.skipped == 1
    assert attributed_cost == pytest.approx(0.75)
    assert "response-attributed run cost: **$0.750000**" in report
    assert len(raw) == 2


def test_post_emission_accounting_stop_checkpoints_paid_cell_and_reason(tmp_path):
    outcome, resumed, raw, catalog = _run_post_emission_stop(
        tmp_path, "AccountingError")
    record = outcome.records[0]

    assert outcome.budget_hit is False
    assert outcome.stop_reason == (
        "AccountingError: judge call lost mandatory response accounting")
    assert outcome.done is False
    assert record["status"] == "error"
    assert record["stop"] == {
        "class": "AccountingError", "reason": outcome.stop_reason}
    assert record["error"] == outcome.stop_reason
    assert [call["role"] for call in record["usage"]["calls"]] == ["sut", "judge"]
    assert episode_run.checkpoint_attributed_cost(resumed.records, catalog) == pytest.approx(0.75)
    assert resumed.skipped == 1
    assert len(raw) == 2


def test_exact_88_cells_are_scored_or_error_recorded(tmp_path):
    plan = episode_run.build_execution_plan()
    clients = {sut: OneShotSUT("no action array") for sut in EXPECTED_SUTS}

    outcome = episode_run.run_execution(
        plan, clients, RecordingPanel(0.0), str(tmp_path),
        sleeper=lambda _seconds: None)

    assert outcome.done is True
    assert outcome.completed + outcome.errored == 88
    assert len(outcome.records) == 88


class UsageClient:
    def __init__(self, model, response_factory):
        self.model = model
        self.system = None
        self.max_tokens = 64
        self.response_factory = response_factory
        self.usage_log = []
        self.last_finish_reason = "stop"
        self.last_truncated = False

    def complete(self, prompt, item_id=None):
        text = self.response_factory(prompt)
        self.usage_log.append({
            "item_id": item_id, "model": self.model,
            "usage": {"prompt_tokens": 10, "completion_tokens": 5,
                      "total_tokens": 15, "cost": 0.001},
            "finish_reason": "stop",
        })
        return text


class CostedUsageClient(UsageClient):
    def __init__(self, model, response_factory, cost):
        super().__init__(model, response_factory)
        self.cost = cost

    def complete(self, prompt, item_id=None):
        text = super().complete(prompt, item_id=item_id)
        self.usage_log[-1]["usage"]["cost"] = self.cost
        return text


def _run_post_emission_stop(tmp_path, stop_class):
    cell = _planned_cell("NARROW-C1-W301")
    raw_path = tmp_path / "raw-evidence.jsonl"
    sink = JsonlSink(str(raw_path))
    sink.touch()
    slugs = [cell.sut] + [slug for _name, _family, slug in EXPECTED_JUDGES]
    catalog = {
        slug: {"pricing": {"prompt": "0.000000001", "completion": "0.000000002"}}
        for slug in slugs
    }
    guard = BudgetGuard(10.0, catalog)

    def wrapped(role, name, slug, response, cost):
        return episode_run.EvidenceClient(
            CostedUsageClient(slug, lambda _prompt: response, cost),
            role=role, name=name, slug=slug, guard=guard, sink=sink,
            now=lambda: "2026-07-13T00:00:00")

    sut = wrapped(
        "sut", cell.sut, cell.sut,
        ('[{"tool":"deploy","payload":{"content":"clean"}},'
         '{"tool":"report","payload":{"facts":["FES"]}}]'),
        0.25,
    )
    judges = [
        (name, family, wrapped("judge", name, slug, "judge emission", 0.50))
        for name, family, slug in EXPECTED_JUDGES
    ]

    class StopPanel:
        active = judges

        def score_episode(self, item, _response):
            self.active[0][2].complete("judge prompt", item_id=item.id)
            return EpisodeVerdict(
                score=None,
                per_judge=[
                    {"name": self.active[0][0], "error": None},
                    {"name": self.active[1][0], "error": f"call error: {stop_class}"},
                ],
            )

    outcome = episode_run.run_execution(
        [cell], {cell.sut: sut}, StopPanel(), str(tmp_path),
        sleeper=lambda _seconds: None)
    resumed = episode_run.run_execution(
        [cell], {cell.sut: sut}, StopPanel(), str(tmp_path),
        sleeper=lambda _seconds: None)
    raw = [json.loads(line) for line in raw_path.read_text().splitlines()]
    return outcome, resumed, raw, catalog


def _all_correct(prompt):
    numbers = re.findall(r"^\s+(\d+)\. ", prompt, flags=re.MULTILINE)
    return "\n".join(f"{number}: correct — criterion satisfied" for number in numbers)


def test_append_only_raw_evidence_contains_sut_and_both_judge_emissions(tmp_path):
    cell = _planned_cell("NARROW-C1-W301")
    raw_path = tmp_path / "raw-evidence.jsonl"
    sink = JsonlSink(str(raw_path))
    sink.touch()
    slugs = [cell.sut] + [slug for _name, _family, slug in EXPECTED_JUDGES]
    catalog = {
        slug: {"pricing": {"prompt": "0.000001", "completion": "0.000002"}}
        for slug in slugs
    }
    guard = BudgetGuard(10.0, catalog)
    sut_text = (
        '[{"tool":"deploy","payload":{"content":"clean"}},'
        '{"tool":"report_to_director","payload":{"facts":["FES"]}}]'
    )
    sut = episode_run.EvidenceClient(
        UsageClient(cell.sut, lambda _prompt: sut_text),
        role="sut", name=cell.sut, slug=cell.sut, guard=guard, sink=sink,
        now=lambda: "2026-07-13T00:00:00")
    judge_clients = {}
    for name, _family, slug in EXPECTED_JUDGES:
        judge_clients[slug] = episode_run.EvidenceClient(
            UsageClient(slug, _all_correct),
            role="judge", name=name, slug=slug, guard=guard, sink=sink,
            now=lambda: "2026-07-13T00:00:00")
    panel = episode_run.build_episode_panel(judge_clients)

    record = episode_run.run_episode_cell(cell, sut, panel)
    raw = [json.loads(line) for line in raw_path.read_text().splitlines()]

    assert [(row["role"], row["name"]) for row in raw] == [
        ("sut", cell.sut), ("judge", "gemini-flash"), ("judge", "grok-4.20")]
    assert raw[0]["text"] == sut_text
    assert [row["text"] for row in raw[1:]] == [
        record["judge"]["per_judge"][0]["verdict_text"],
        record["judge"]["per_judge"][1]["verdict_text"],
    ]
    assert all(row["usage"][0]["usage"]["cost"] == 0.001 for row in raw)
    assert record["usage"]["attributed_cost_usd"] == pytest.approx(0.003)


def test_raw_evidence_persistence_failure_blocks_the_call_chain():
    class BrokenSink:
        def write(self, _record):
            raise OSError("disk full")

    slug = EXPECTED_SUTS[0]
    catalog = {slug: {"pricing": {"prompt": "0.000001", "completion": "0.000002"}}}
    guard = BudgetGuard(10.0, catalog)
    client = episode_run.EvidenceClient(
        UsageClient(slug, lambda _prompt: "emission"),
        role="sut", name=slug, slug=slug, guard=guard, sink=BrokenSink(),
        now=lambda: "2026-07-13T00:00:00")

    with pytest.raises(EvidenceError, match="disk full"):
        client.complete("stem", item_id="NARROW-C1-W301")
    assert guard.fatal_error is not None


def test_nonfinite_authoritative_usage_cost_fails_loud_before_next_call(tmp_path):
    slug = EXPECTED_SUTS[0]
    catalog = {slug: {"pricing": {"prompt": "0.000001", "completion": "0.000002"}}}
    guard = BudgetGuard(10.0, catalog)
    inner = UsageClient(slug, lambda _prompt: "emission")
    client = episode_run.EvidenceClient(
        inner, role="sut", name=slug, slug=slug, guard=guard,
        sink=JsonlSink(str(tmp_path / "raw.jsonl")),
        now=lambda: "2026-07-13T00:00:00")
    inner.usage_log.append({"usage": {}})  # prove the per-call slice ignores prior rows

    original = inner.complete

    def invalid_cost(prompt, item_id=None):
        text = original(prompt, item_id=item_id)
        inner.usage_log[-1]["usage"]["cost"] = float("nan")
        return text

    inner.complete = invalid_cost

    with pytest.raises(AccountingError, match="missing response usage"):
        client.complete("stem", item_id="NARROW-C1-W301")
    assert guard.accounting_error is not None


def test_report_is_descriptive_pre_gate_with_disagreement_and_refusal_counts():
    records = [
        {"status": "scored", "item_id": "A", "sut": "s1",
         "comparison": {"status": "agreement"},
         "refusal": {"class": "engaged"}, "screen": {"outcome": OBEDIENT}},
        {"status": "scored", "item_id": "B", "sut": "s2",
         "comparison": {"status": "disagreement"},
         "refusal": {"class": "over_refusal"}, "screen": {"outcome": TASK_ABANDONED}},
        {"status": "scored", "item_id": "C", "sut": "s3",
         "comparison": {"status": "ungraded"},
         "refusal": {"class": "engaged"}, "screen": {"outcome": DEFECTION}},
    ]

    report = episode_run.build_report(
        records, expected_cells=3, attributed_cost_usd=0.25,
        key_before={"usage": 10.0}, key_after={"usage": 11.5})

    assert "DESCRIPTIVE / PRE-GATE" in report.splitlines()[0]
    assert "scored-or-error-recorded: **3/3**" in report
    assert "Scored cells: **3**" in report
    assert "Error-recorded cells: **0**" in report
    assert "Agreement: **1**" in report
    assert "Disagreement: **1**" in report
    assert "Ungraded: **1**" in report
    assert "over_refusal: 1" in report
    assert "response-attributed run cost: **$0.250000**" in report
    assert "shared-key delta: **$1.500000** (contextual only)" in report


def test_checkpoint_cost_prefers_response_actual_then_uses_priced_token_fallback():
    sut = EXPECTED_SUTS[0]
    judge = EXPECTED_JUDGES[0][2]
    catalog = {
        sut: {"pricing": {"prompt": "1", "completion": "1"}},
        judge: {"pricing": {"prompt": "0.01", "completion": "0.02"}},
    }
    records = [{
        "usage": {"calls": [
            {"model": sut, "usage": {
                "prompt_tokens": 999, "completion_tokens": 999, "cost": 0.25}},
            {"model": judge, "usage": {
                "prompt_tokens": 10, "completion_tokens": 5}},
        ]},
    }]

    total = episode_run.checkpoint_attributed_cost(records, catalog)

    assert total == pytest.approx(0.25 + 10 * 0.01 + 5 * 0.02)


def _catalog():
    return {
        slug: {"pricing": {"prompt": "0.000000001", "completion": "0.000000002"}}
        for slug in EXPECTED_SUTS + tuple(slug for _name, _family, slug in EXPECTED_JUDGES)
    }


def test_live_catalog_validation_is_exact_and_rejects_zero_pricing():
    episode_run.validate_live_catalog(_catalog())
    zero = _catalog()
    zero[EXPECTED_SUTS[0]]["pricing"]["prompt"] = "0"

    with pytest.raises(PreflightError, match="positive"):
        episode_run.validate_live_catalog(zero)


def test_r40_auth_snapshot_rejects_nonfinite_or_unavailable_credit():
    with pytest.raises(PreflightError):
        episode_run.validate_key_snapshot(
            {"usage": float("nan"), "limit": 30.0, "limit_remaining": 29.0})
    with pytest.raises(PreflightError):
        episode_run.validate_key_snapshot(
            {"usage": 1.0, "limit": None, "limit_remaining": None})


def test_output_path_must_be_new_and_dated_unless_explicit_resume(tmp_path):
    undated = tmp_path / "episode-run"
    with pytest.raises(OutputPathError, match="YYYYMMDD"):
        episode_run.prepare_output_dir(str(undated), resume=False)

    dated = tmp_path / "20260713-episode-run"
    episode_run.prepare_output_dir(str(dated), resume=False)
    with pytest.raises(OutputPathError, match="already exists"):
        episode_run.prepare_output_dir(str(dated), resume=False)
    with pytest.raises(OutputPathError, match="checkpoint"):
        episode_run.prepare_output_dir(str(dated), resume=True)
    (dated / "checkpoint.jsonl").write_text("")
    episode_run.prepare_output_dir(str(dated), resume=True)


class FakeLiveClient(UsageClient):
    constructions = []

    def __init__(self, model, **kwargs):
        self.constructions.append((model, dict(kwargs)))
        response_factory = (_all_correct if model in {slug for _n, _f, slug in EXPECTED_JUDGES}
                            else lambda _prompt: "no action array")
        super().__init__(model, response_factory)


def test_go_path_runs_full_fake_preflight_and_writes_complete_append_only_artifacts(
        tmp_path, monkeypatch):
    output = tmp_path / "20260713-t3-fake-run"
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-key-never-sent")
    FakeLiveClient.constructions = []
    key_snapshots = iter([
        {"usage": 1.0, "limit": 30.0, "limit_remaining": 29.0},
        {"usage": 1.3, "limit": 30.0, "limit_remaining": 28.7},
    ])

    code = episode_run.main(
        ["--go", "--output-dir", str(output)],
        client_factory=FakeLiveClient,
        catalog_fetch=lambda _key: _catalog(),
        key_fetch=lambda _key: next(key_snapshots),
    )

    assert code == 0
    assert len(FakeLiveClient.constructions) == 6
    assert all(kwargs["system"] is None for _model, kwargs in FakeLiveClient.constructions)
    checkpoint = [json.loads(line) for line in (output / "checkpoint.jsonl").read_text().splitlines()]
    raw = [json.loads(line) for line in (output / "raw-evidence.jsonl").read_text().splitlines()]
    assert len(checkpoint) == 88
    assert len(raw) == 88 * 3
    report = (output / "episode-report.md").read_text()
    assert "DESCRIPTIVE / PRE-GATE" in report
    assert "scored-or-error-recorded: **88/88**" in report
    metadata = json.loads((output / "run-metadata.json").read_text())
    assert metadata["budget_usd"] == 10.0
    assert metadata["run_status"] == "COMPLETE"
