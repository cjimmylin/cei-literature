"""Task 4 format bridge + requalification runner (R43/R44), hermetic."""

from __future__ import annotations

import os
import importlib
import json
import re
import sys


HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)

from wcfbench import probe_fixtures  # noqa: E402
from wcfbench.judge import build_award_prompt  # noqa: E402
from wcfbench.loader import RubricKeypoint  # noqa: E402
from wcfbench import qualification  # noqa: E402
from wcfbench import mvp  # noqa: E402
from wcfbench.judge_panel import JudgePanel  # noqa: E402
from test_qualification import BatteryJudge  # noqa: E402


def _runner():
    return importlib.import_module("format_bridge_requal")


def _probe_reps(probe, n_pass=8):
    return qualification.ProbeReps(
        probe=probe, k=8, n_pass=n_pass,
        reps=[{"rep": i, "passed": i < n_pass,
               "cause": "pass" if i < n_pass else "fail_substantive", "detail": "mock"}
              for i in range(8)],
    )


def _full_qualification(name, family, slug):
    reps = {probe: _probe_reps(probe) for probe in qualification.PROBES}
    return qualification.JudgeQualification(
        name=name, family=family, slug=slug, k=8, threshold=5,
        probe_reps=reps, surfaces=set(qualification.SURFACES),
    )


def _all_pass_results(runner):
    resolved = (
        ("cohere-command-a", "cohere", "cohere/command-a"),
        ("amazon-nova-pro", "amazon", "amazon/nova-pro-v1"),
    )
    return runner.run_batteries(
        resolved, client_factory=lambda _n, _f, slug: slug,
        qualify_fn=lambda _client, *, name, family, slug, k, threshold:
            _full_qualification(name, family, slug),
        probe_fn=lambda _client, probe, *, k: _probe_reps(probe),
    )


def _execute_mock_live(runner, out_dir):
    snapshots = iter([
        {"usage": 2.0, "limit": 30.0, "limit_remaining": 28.0},
        {"usage": 2.0, "limit": 30.0, "limit_remaining": 28.0},
    ])
    slugs = {
        "google/gemini-2.5-flash", "x-ai/grok-4.20",
        "cohere/command-a", "amazon/nova-pro-v1",
    }
    catalog = {slug: {"pricing": {"prompt": "0.001", "completion": "0.002"}}
               for slug in slugs}

    class FakeLiveClient:
        def __init__(self, model, **kwargs):
            self.model = model
            self.max_tokens = kwargs["max_tokens"]
            self.usage_log = []
            self.last_finish_reason = "stop"
            self.last_truncated = False

    outcome = runner.execute_live(
        "secret-not-printed", out_dir=str(out_dir), budget=10.0,
        key_fetch=lambda _key: next(snapshots),
        catalog_fetch=lambda _key: catalog,
        client_builder=FakeLiveClient,
        qualify_fn=lambda _client, *, name, family, slug, k, threshold:
            _full_qualification(name, family, slug),
        probe_fn=lambda _client, probe, *, k: _probe_reps(probe),
        now=lambda: "2026-07-11T12:00:00",
    )
    return outcome, slugs


def test_format_bridge_exemplar_is_frozen_neutral_grounded_and_arithmetically_exact():
    block = probe_fixtures.FORMAT_BRIDGE_EXEMPLAR_BLOCK
    response = probe_fixtures.FORMAT_BRIDGE_EXEMPLAR_RESPONSE

    forbidden = (
        "westminster", "catechism", "confession", "commandment", "theology",
        "family", "ethic", "harm", "sin", "matter", "manner", "rubric",
        "gold", "anchor", "bank", "holdout",
    )
    assert qualification.CANARY not in block
    assert not any(word in block.lower() for word in forbidden)

    verdict_lines = re.findall(
        r'^KP\d+: (award|deny) — [^\n]+, "([^"]+)"$', block, re.MULTILINE)
    assert {decision for decision, _quote in verdict_lines} == {"award", "deny"}
    assert all(quote in response for _decision, quote in verdict_lines)

    score_match = re.search(r"^SCORE:\s*([0-9.]+)$", block, re.MULTILINE)
    assert score_match is not None
    assert block.splitlines()[-1] == score_match.group(0)
    n_awards = sum(decision == "award" for decision, _quote in verdict_lines)
    assert float(score_match.group(1)) == n_awards / len(verdict_lines)


def test_format_bridge_exemplar_appears_verbatim_once_in_every_award_prompt():
    prompt = build_award_prompt(
        stem="A neutral test stem.",
        rubric=[RubricKeypoint(1.0, "mentions the requested time", axis="matter")],
        response="The requested time is 2:00.",
    )
    block = probe_fixtures.FORMAT_BRIDGE_EXEMPLAR_BLOCK
    assert prompt.count(block) == 1


def test_exemplar_bearing_prompt_is_covered_by_both_award_template_hashes(monkeypatch):
    original = qualification.build_award_prompt
    rendered = []

    def spy(**kwargs):
        prompt = original(**kwargs)
        rendered.append(prompt)
        return prompt

    monkeypatch.setattr(qualification, "build_award_prompt", spy)
    before = qualification.current_template_hashes()
    assert len(rendered) == 3
    assert all(probe_fixtures.FORMAT_BRIDGE_EXEMPLAR_BLOCK in p for p in rendered)

    def changed(**kwargs):
        return original(**kwargs).replace(
            probe_fixtures.FORMAT_BRIDGE_EXEMPLAR_BLOCK,
            probe_fixtures.FORMAT_BRIDGE_EXEMPLAR_BLOCK + "\nFORMAT-DRIFT",
        )

    monkeypatch.setattr(qualification, "build_award_prompt", changed)
    after = qualification.current_template_hashes()
    assert after["award_consistency"] != before["award_consistency"]
    assert after["discrimination"] != before["discrimination"]
    assert {k: v for k, v in after.items() if k not in {"award_consistency", "discrimination"}} == {
        k: v for k, v in before.items() if k not in {"award_consistency", "discrimination"}
    }


def test_task4_roster_is_exactly_gemini_and_grok_with_no_gpt():
    runner = _runner()
    assert runner.INCUMBENT_JUDGES == (
        ("gemini-flash", "google", "google/gemini-2.5-flash"),
        ("grok-4.20", "x-ai", "x-ai/grok-4.20"),
    )
    assert "gpt" not in repr(runner.INCUMBENT_JUDGES).lower()


def test_same_model_candidate_alias_resolution_is_strict():
    runner = _runner()
    catalog = {
        "cohere/command-a-03-2025": {},
        "amazon/nova-pro-v1": {},
        "cohere/command-r-plus": {},
        "amazon/nova-premier-v1": {},
    }
    assert runner.resolve_candidate_slugs(catalog) == (
        ("cohere-command-a", "cohere", "cohere/command-a-03-2025"),
        ("amazon-nova-pro", "amazon", "amazon/nova-pro-v1"),
    )
    with __import__("pytest").raises(mvp.SlugValidationError):
        runner.resolve_candidate_slugs({
            "cohere/command-r-plus": {}, "amazon/nova-premier-v1": {}})


def test_mock_battery_matrix_reuses_grok_and_screens_all_candidates():
    runner = _runner()
    full_calls = []
    partial_calls = []
    clients = []

    def client_factory(name, family, slug):
        client = {"name": name, "family": family, "slug": slug}
        clients.append(client)
        return client

    def qualify_fn(client, *, name, family, slug, k, threshold):
        full_calls.append((name, family, slug, k, threshold, id(client)))
        return _full_qualification(name, family, slug)

    def probe_fn(client, probe, *, k):
        partial_calls.append((client["name"], probe, k, id(client)))
        return _probe_reps(probe)

    resolved = (
        ("cohere-command-a", "cohere", "cohere/command-a"),
        ("amazon-nova-pro", "amazon", "amazon/nova-pro-v1"),
    )
    results = runner.run_batteries(
        resolved, client_factory=client_factory,
        qualify_fn=qualify_fn, probe_fn=probe_fn,
    )

    assert [(n, f, s, k, t) for n, f, s, k, t, _client in full_calls] == [
        ("gemini-flash", "google", "google/gemini-2.5-flash", 8, 5),
        ("grok-4.20", "x-ai", "x-ai/grok-4.20", 8, 5),
    ]
    assert [(name, probe, k) for name, probe, k, _client in partial_calls] == [
        (name, probe, 8)
        for name in ("cohere-command-a", "amazon-nova-pro")
        for probe in ("g4", "award_consistency", "discrimination")
    ]
    assert len({client_id for name, _probe, _k, client_id in partial_calls
                if name == "cohere-command-a"}) == 1
    assert len({client_id for name, _probe, _k, client_id in partial_calls
                if name == "amazon-nova-pro"}) == 1
    assert tuple(results.candidates) == (
        "grok-4.20", "cohere-command-a", "amazon-nova-pro")
    assert results.candidates["grok-4.20"] is results.incumbents["grok-4.20"]
    assert len(clients) == 4  # two incumbents + two new-family clients; no second Grok client


def test_task4_manifest_has_current_hashes_expected_eligibility_and_builds_panel(monkeypatch):
    runner = _runner()
    resolved = (
        ("cohere-command-a", "cohere", "cohere/command-a"),
        ("amazon-nova-pro", "amazon", "amazon/nova-pro-v1"),
    )

    def qualify_fn(_client, *, name, family, slug, k, threshold):
        return _full_qualification(name, family, slug)

    def probe_fn(client, probe, *, k):
        # Cohere misses discrimination at 4/8; Nova meets the unchanged 5/8 bar.
        n_pass = 4 if client == "cohere/command-a" and probe == "discrimination" else 8
        if client == "amazon/nova-pro-v1" and probe == "discrimination":
            n_pass = 5
        return _probe_reps(probe, n_pass=n_pass)

    results = runner.run_batteries(
        resolved, client_factory=lambda _n, _f, slug: slug,
        qualify_fn=qualify_fn, probe_fn=probe_fn,
    )
    manifest = runner.build_task4_manifest(
        results, timestamp="2026-07-11T12:00:00",
        run_dir="07-PILOTS/20260711-format-bridge-requal",
    )
    encoded = json.dumps(manifest).lower()
    assert "gpt" not in encoded and "openai/gpt-4o-mini" not in encoded
    assert manifest["source"] == "live Task 4 pass table (no carried-forward counts)"
    assert manifest["template_hashes"] == qualification.current_template_hashes()
    by_name = {row["name"]: row for row in manifest["judges"]}
    assert set(by_name["gemini-flash"]["eligible_surfaces"]) == set(qualification.SURFACES)
    assert set(by_name["grok-4.20"]["eligible_surfaces"]) == set(qualification.SURFACES)
    assert set(by_name["cohere-command-a"]["eligible_surfaces"]) == {qualification.COHERENCE}
    assert set(by_name["amazon-nova-pro"]["eligible_surfaces"]) == {
        qualification.OPEN_AWARD, qualification.COHERENCE}
    assert by_name["cohere-command-a"]["battery_scope"] == list(runner.CANDIDATE_PROBES)
    assert by_name["amazon-nova-pro"]["battery_scope"] == list(runner.CANDIDATE_PROBES)

    class NoCallClient:
        def __init__(self, model, **_kwargs):
            self.model = model

        def complete(self, *_args, **_kwargs):
            raise AssertionError("manifest panel construction must not requalify")

    monkeypatch.setattr(mvp, "OpenRouterModelClient", NoCallClient)
    panel = mvp.build_panel(manifest)
    assert isinstance(panel, JudgePanel)
    assert {name for name, _family, _client in panel.active} == set(by_name)


def test_budget_guard_is_actual_first_with_fail_loud_pricing_and_enforces_cap():
    runner = _runner()

    class Client:
        usage_log = [
            {"usage": {"prompt_tokens": 10, "completion_tokens": 20, "cost": 0.75}},
            {"usage": {"prompt_tokens": 100, "completion_tokens": 50}},
        ]

    catalog = {"vendor/model": {"pricing": {"prompt": "0.001", "completion": "0.002"}}}
    guard = runner.BudgetGuard(1.0, catalog)
    guard.register("vendor/model", Client())
    assert guard.total_usd() == 0.95  # 0.75 actual + 0.20 strict-price fallback
    guard.before_call()
    Client.usage_log.append({"usage": {"prompt_tokens": 100, "completion_tokens": 0}})
    guard.after_call()
    with __import__("pytest").raises(runner.BudgetExceeded):
        guard.before_call()

    bad = runner.BudgetGuard(10.0, {"vendor/model": {"pricing": {}}})
    bad.register("vendor/model", Client())
    with __import__("pytest").raises(mvp.PricingError):
        bad.total_usd()

    class EmptyClient:
        usage_log = []

    reserve_catalog = {
        "vendor/model": {"pricing": {"prompt": "0", "completion": "0.001"}}}
    reserve_guard = runner.BudgetGuard(1.0, reserve_catalog)
    reserve_guard.register("vendor/model", EmptyClient())
    with __import__("pytest").raises(runner.BudgetExceeded):
        reserve_guard.before_call("vendor/model", "short prompt", max_tokens=2048)


def test_exact_budget_completion_is_valid_but_positive_cost_next_call_is_blocked():
    runner = _runner()

    class Client:
        usage_log = [{"usage": {
            "prompt_tokens": 1, "completion_tokens": 1, "cost": 1.0}}]

    catalog = {
        "vendor/model": {"pricing": {"prompt": "0.1", "completion": "0.1"}}}
    guard = runner.BudgetGuard(1.0, catalog)
    guard.register("vendor/model", Client())
    guard.after_call()
    assert guard.hit is False
    with __import__("pytest").raises(runner.BudgetExceeded):
        guard.before_call("vendor/model", "next", max_tokens=1)


def test_live_preflight_stops_before_catalog_clients_or_output(tmp_path):
    runner = _runner()
    touched = []
    out_dir = tmp_path / "20260711-format-bridge-requal"

    def forbidden(*_args, **_kwargs):
        touched.append(True)
        raise AssertionError("must stop before catalog/client work")

    with __import__("pytest").raises(runner.PreflightError):
        runner.execute_live(
            "secret-not-printed", out_dir=str(out_dir), budget=10.0,
            key_fetch=lambda _key: {"usage": 4.0, "limit": 9.0, "limit_remaining": 5.0},
            catalog_fetch=forbidden, client_builder=forbidden,
        )
    assert touched == []
    assert not out_dir.exists()


def test_metadata_get_uses_exactly_two_retries():
    runner = _runner()
    calls = []
    sleeps = []

    def flaky(_key):
        calls.append(len(calls))
        if len(calls) < 3:
            raise OSError("transient")
        return {"ok": True}

    assert runner.fetch_with_two_retries(
        flaky, "secret-not-printed", sleeper=sleeps.append) == {"ok": True}
    assert len(calls) == 3
    assert sleeps == [2.0, 4.0]

    failed = []
    with __import__("pytest").raises(OSError):
        runner.fetch_with_two_retries(
            lambda _key: failed.append(True) or (_ for _ in ()).throw(OSError("still down")),
            "secret-not-printed", sleeper=lambda _seconds: None,
        )
    assert len(failed) == 3


def test_mock_live_run_writes_exact_outputs_and_one_reconciliation_line(tmp_path):
    runner = _runner()
    out_dir = tmp_path / "20260711-format-bridge-requal"
    outcome, slugs = _execute_mock_live(runner, out_dir)
    assert {os.path.basename(path) for path in outcome.paths.values()} == {
        "raw_verdicts.jsonl",
        "20260711-format-bridge-requal-manifest.json",
        "20260711-format-bridge-requal-report.md",
    }
    assert all(path.startswith(str(out_dir)) for path in outcome.paths.values())
    report = open(outcome.paths["report"], encoding="utf-8").read()
    assert report.count("Cost reconciliation:") == 1
    assert "within ±20%: YES" in report
    assert "not directly comparable to the pre-bridge MVP" in report
    assert "CROSS-FAMILY" in report
    assert all(slug in report for slug in slugs)


def test_open_outcome_uses_actual_family_count_and_does_not_close_after_non_google_pass():
    runner = _runner()
    results = _all_pass_results(runner)
    manifest = runner.build_task4_manifest(
        results, timestamp="2026-07-11T12:00:00",
        run_dir="07-PILOTS/20260711-format-bridge-requal",
    )
    # Exceptional complete outcome: Gemini loses OPEN, Grok passes OPEN, and the two new
    # families fail it. The actual OPEN family set is therefore exactly {x-ai}.
    for row in manifest["judges"]:
        surfaces = set(row["eligible_surfaces"])
        if row["name"] != "grok-4.20":
            surfaces.discard(qualification.OPEN_AWARD)
        row["eligible_surfaces"] = sorted(surfaces)

    report = runner.build_report(
        results, manifest, timestamp="2026-07-11T12:00:00", internal_total=1.0,
        key_before={"usage": 2.0}, key_after={"usage": 3.0}, budget=10.0,
    )
    assert "SINGLE-FAMILY" in report
    assert "NON-GOOGLE-ONLY" in report
    assert "x-ai" in report
    assert "CROSS-FAMILY" not in report
    assert "CLOSED" not in report
    assert "escalation" in report.lower()


def test_complete_finalization_validates_then_publishes_report_and_manifest_last(
        tmp_path, monkeypatch):
    runner = _runner()
    out_dir = tmp_path / "20260711-format-bridge-requal"
    events = []
    real_rename = runner.os.rename
    real_validate = runner._load_and_validate_manifest

    def validate(path):
        events.append(("validate", os.path.basename(path)))
        return real_validate(path)

    def publish(source, destination):
        events.append(("publish", os.path.basename(destination)))
        if os.path.basename(destination) == runner.MANIFEST_NAME:
            assert (out_dir / runner.REPORT_NAME).exists()
        return real_rename(source, destination)

    monkeypatch.setattr(runner, "_load_and_validate_manifest", validate)
    monkeypatch.setattr(runner.os, "rename", publish)
    outcome, _slugs = _execute_mock_live(runner, out_dir)
    assert outcome.partial_reason is None
    assert events == [
        ("validate", runner.MANIFEST_NAME + ".pending"),
        ("publish", runner.REPORT_NAME),
        ("publish", runner.MANIFEST_NAME),
    ]


def test_post_live_report_write_failure_yields_partial_report_and_no_manifest(
        tmp_path, monkeypatch):
    runner = _runner()
    out_dir = tmp_path / "20260711-format-bridge-requal"
    writes = []

    def fail_first_write(path, text):
        writes.append(path)
        if len(writes) == 1:
            raise OSError("simulated report write failure")
        with open(path, "x", encoding="utf-8") as fh:
            fh.write(text)

    monkeypatch.setattr(runner, "_write_text_new", fail_first_write, raising=False)
    outcome, _slugs = _execute_mock_live(runner, out_dir)
    assert outcome.partial_reason is not None
    assert "OSError" in outcome.partial_reason
    assert set(outcome.paths) == {"raw", "report"}
    assert not (out_dir / runner.MANIFEST_NAME).exists()
    report = (out_dir / runner.REPORT_NAME).read_text(encoding="utf-8")
    assert "PARTIAL / STOPPED" in report
    assert "qualification_complete=false" in report
    assert "OPEN outcome: UNDETERMINED" in report


def test_raw_sink_initialization_failure_yields_partial_report_and_no_manifest(
        tmp_path, monkeypatch):
    runner = _runner()
    out_dir = tmp_path / "20260711-format-bridge-requal"
    monkeypatch.setattr(
        runner.JsonlSink, "touch",
        lambda _self: (_ for _ in ()).throw(OSError("simulated raw sink failure")),
    )
    outcome, _slugs = _execute_mock_live(runner, out_dir)
    assert outcome.partial_reason is not None
    assert "OSError" in outcome.partial_reason
    assert set(outcome.paths) == {"report"}
    assert not (out_dir / runner.RAW_NAME).exists()
    assert not (out_dir / runner.MANIFEST_NAME).exists()
    report = (out_dir / runner.REPORT_NAME).read_text(encoding="utf-8")
    assert "PARTIAL / STOPPED" in report
    assert "qualification_complete=false" in report
    assert "OPEN outcome: UNDETERMINED" in report


def test_mid_run_raw_sink_failure_latches_guard_stops_spend_and_recovers_accounting(
        tmp_path, monkeypatch):
    runner = _runner()
    out_dir = tmp_path / "20260711-format-bridge-requal"
    snapshots = iter([
        {"usage": 2.0, "limit": 30.0, "limit_remaining": 28.0},
        {"usage": 2.25, "limit": 30.0, "limit_remaining": 27.75},
    ])
    slugs = {
        "google/gemini-2.5-flash", "x-ai/grok-4.20",
        "cohere/command-a", "amazon/nova-pro-v1",
    }
    catalog = {slug: {"pricing": {"prompt": "0", "completion": "0"}}
               for slug in slugs}

    class PaidBatteryClient(BatteryJudge):
        paid_calls = 0

        def __init__(self, model, **kwargs):
            super().__init__()
            self.model = model
            self.max_tokens = kwargs["max_tokens"]
            self.usage_log = []
            self.last_truncated = False

        def complete(self, prompt, item_id=None):
            type(self).paid_calls += 1
            text = super().complete(prompt, item_id=item_id)
            self.usage_log.append({
                "item_id": item_id,
                "usage": {"prompt_tokens": 1, "completion_tokens": 1, "cost": 0.25},
            })
            return text

    sink_writes = []
    real_sink_write = runner.JsonlSink.write

    def fail_first_sink_write(sink, record):
        sink_writes.append(record)
        if len(sink_writes) == 1:
            raise OSError("simulated raw write failure")
        return real_sink_write(sink, record)

    def call_once_then_full(client, *, name, family, slug, k, threshold):
        try:
            client.complete("mock paid qualification call", item_id="MOCK")
        except Exception:
            pass
        return _full_qualification(name, family, slug)

    def blocked_candidate_probe(client, probe, *, k):
        try:
            client.complete("mock paid candidate call", item_id="MOCK")
        except Exception:
            pass
        return _probe_reps(probe)

    monkeypatch.setattr(runner.JsonlSink, "write", fail_first_sink_write)
    outcome = runner.execute_live(
        "secret-not-printed", out_dir=str(out_dir), budget=10.0,
        key_fetch=lambda _key: next(snapshots),
        catalog_fetch=lambda _key: catalog,
        client_builder=PaidBatteryClient,
        qualify_fn=call_once_then_full,
        probe_fn=blocked_candidate_probe,
        now=lambda: "2026-07-11T12:00:00",
    )
    assert PaidBatteryClient.paid_calls == 1
    assert outcome.partial_reason is not None
    assert outcome.internal_total_usd == 0.25
    assert set(outcome.paths) == {"raw", "report"}
    assert not (out_dir / runner.MANIFEST_NAME).exists()
    report = (out_dir / runner.REPORT_NAME).read_text(encoding="utf-8")
    assert "PARTIAL / STOPPED" in report
    assert "internal total **$0.2500**" in report
    assert "key-side usage delta **$0.2500**" in report


def test_budget_stop_writes_partial_evidence_without_operational_manifest_or_outcome(tmp_path):
    runner = _runner()
    out_dir = tmp_path / "20260711-format-bridge-requal"
    snapshots = iter([
        {"usage": 2.0, "limit": 30.0, "limit_remaining": 28.0},
        {"usage": 2.01, "limit": 30.0, "limit_remaining": 27.99},
    ])
    slugs = {
        "google/gemini-2.5-flash", "x-ai/grok-4.20",
        "cohere/command-a", "amazon/nova-pro-v1",
    }
    catalog = {slug: {"pricing": {"prompt": "0", "completion": "0"}}
               for slug in slugs}

    class CostedBatteryClient(BatteryJudge):
        def __init__(self, model, **kwargs):
            super().__init__()
            self.model = model
            self.max_tokens = kwargs["max_tokens"]
            self.usage_log = []
            self.last_truncated = False

        def complete(self, prompt, item_id=None):
            text = super().complete(prompt, item_id=item_id)
            self.usage_log.append({
                "item_id": item_id,
                "usage": {"prompt_tokens": 1, "completion_tokens": 1, "cost": 0.01},
            })
            return text

    outcome = runner.execute_live(
        "secret-not-printed", out_dir=str(out_dir), budget=0.01,
        key_fetch=lambda _key: next(snapshots),
        catalog_fetch=lambda _key: catalog,
        client_builder=CostedBatteryClient,
        now=lambda: "2026-07-11T12:00:00",
    )
    assert outcome.budget_hit is True
    assert set(outcome.paths) == {"raw", "report"}
    assert not (out_dir / runner.MANIFEST_NAME).exists()
    report = open(outcome.paths["report"], encoding="utf-8").read()
    assert "PARTIAL / STOPPED" in report
    assert "qualification_complete=false" in report
    assert "OPEN outcome: UNDETERMINED" in report
    assert "CROSS-FAMILY" not in report
    assert "SINGLE-FAMILY" not in report
    assert "CLOSED" not in report


def test_dry_run_and_invalid_bounds_create_no_pilot_directory(tmp_path, monkeypatch):
    runner = _runner()
    out_dir = tmp_path / "20260711-format-bridge-requal"
    monkeypatch.setattr(runner, "OUT_DIR", str(out_dir))
    monkeypatch.setattr(runner.mvp, "fetch_key_snapshot", lambda *_a, **_k: 1 / 0)
    monkeypatch.setattr(runner.mvp, "fetch_model_catalog", lambda *_a, **_k: 1 / 0)

    assert runner.main([]) == 0
    assert runner.main(["--k", "7"]) == 2
    assert runner.main(["--budget", "10.01"]) == 2
    assert not out_dir.exists()
