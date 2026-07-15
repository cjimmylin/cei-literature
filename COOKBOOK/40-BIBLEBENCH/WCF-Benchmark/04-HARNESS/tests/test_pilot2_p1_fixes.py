from __future__ import annotations

import copy
import csv
import json
import math
import os
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest


HARNESS_ROOT = Path(__file__).resolve().parent.parent
if str(HARNESS_ROOT) not in sys.path:
    sys.path.insert(0, str(HARNESS_ROOT))

import pilot2_analysis as analysis  # noqa: E402
import pilot2_live as live  # noqa: E402
import pilot2_oauth_canary as canary  # noqa: E402
import pilot2_preflight as preflight  # noqa: E402
import pilot2_report as report  # noqa: E402
from wcfbench import load_items, scorer_kind  # noqa: E402

from test_pilot2_protocol import (  # noqa: E402
    _catalog_and_endpoints, _manifest, _ok_response,
)


def _public_metadata(*, price_factor=1.0):
    catalog, endpoints = _catalog_and_endpoints()
    for spec in preflight.SUT_SPECS:
        catalog[spec.slug]["top_provider"]["context_length"] = 131072
        endpoint = endpoints[spec.slug][0]
        endpoint["context_length"] = 131072
        endpoint["max_completion_tokens"] = 16384
        endpoint["pricing"] = {
            "prompt": str(spec.prompt_price_per_token * price_factor),
            "completion": str(spec.completion_price_per_token * price_factor),
        }
    return catalog, endpoints


def test_public_fetch_uses_exact_six_unauthenticated_urls():
    catalog, endpoints = _public_metadata()
    calls = []

    def opener(url, api_key):
        calls.append((url, api_key))
        if url == preflight.MODELS_URL:
            return {"data": list(catalog.values())}
        slug = url.split("/models/", 1)[1].rsplit("/endpoints", 1)[0]
        return {"data": {"endpoints": endpoints[slug]}}

    observed_catalog, observed_endpoints = preflight.fetch_public_catalog(opener=opener)
    assert observed_catalog == catalog and observed_endpoints == endpoints
    assert len(calls) == 6
    assert all(api_key is None and "/auth/" not in url for url, api_key in calls)


def test_public_preflight_freezes_complete_packet_and_current_price_math(tmp_path):
    catalog, endpoints = _public_metadata(price_factor=0.5)
    output = tmp_path / "pilot2-preflight"
    result = preflight.run_public_preflight(
        output, metadata_fetch=lambda: (catalog, endpoints),
        now=lambda: "2026-07-15T12:00:00Z")
    assert result["status"] == "EXECUTABLE-MANIFEST-INPUT"
    expected_files = {
        "public-catalog-snapshot.json", "public-endpoint-snapshots.json",
        "prompt-judge-ceilings.json", "cost-plan.json", "cost-plan.csv",
        "pilot2-manifest.json", "preflight-report.md",
    }
    assert {path.name for path in output.iterdir()} == expected_files
    manifest = json.loads((output / "pilot2-manifest.json").read_text())
    assert manifest["auth_balance"]["status"] == (
        "NOT_CHECKED_CREDENTIAL_ACCESS_UNAUTHORIZED")
    assert manifest["authorization_gate"]["paid_inference"] is False
    assert manifest["canonical_slugs"] == {
        spec.slug: spec.slug + "-canonical" for spec in preflight.SUT_SPECS}
    assert len(manifest["public_snapshot_hash"]) == 64
    assert manifest["call_forecast"] == {
        "sut_initial": 1150, "sut_attempt_envelope": 1260,
        "provider_canary_initial": 5, "provider_canary_attempt_envelope": 10,
        "logical_judge_decisions": 1740,
        "expected_oauth_tasks": 220, "conservative_oauth_tasks": 590,
    }
    assert set(manifest["runtime_forecast_seconds"]) == {"minimum", "maximum"}
    costs = json.loads((output / "cost-plan.json").read_text())
    per_calls = []
    for row, spec in zip(costs["rows"], preflight.SUT_SPECS):
        per_call = (2221 * spec.prompt_price_per_token * 0.5
                    + 8192 * spec.completion_price_per_token * 0.5)
        per_calls.append(per_call)
        assert row["per_call_usd"] == pytest.approx(per_call)
        assert row["no_retry_230_calls_usd"] == pytest.approx(per_call * 230)
        assert row["attempt_envelope_252_calls_usd"] == pytest.approx(per_call * 252)
        assert row["provider_canary_one_attempt_usd"] == pytest.approx(per_call)
        assert row["provider_canary_two_attempt_usd"] == pytest.approx(per_call * 2)
    envelope = sum(per_calls) * (252 + 2)
    proposed = math.ceil((envelope / 0.8) * 100) / 100
    assert costs["totals"]["proposed_cap_usd"] == proposed
    assert manifest["planning_cost"] == costs["totals"]
    with (output / "cost-plan.csv").open(newline="", encoding="utf-8") as handle:
        assert list(csv.DictReader(handle))[-1]["slug"] == "TOTAL"


def test_public_preflight_writes_failed_packet_and_never_overwrites(tmp_path):
    catalog, endpoints = _public_metadata()
    endpoints[preflight.SUTS[0]][0]["max_completion_tokens"] = 4096
    output = tmp_path / "failed"
    result = preflight.run_public_preflight(
        output, metadata_fetch=lambda: (catalog, endpoints),
        now=lambda: "2026-07-15T12:00:00Z")
    assert result["status"] == "FAILED/NON-EXECUTABLE"
    failure = json.loads((output / "failed-preflight.json").read_text())
    assert any("completion" in blocker for blocker in failure["blockers"])
    assert not (output / "pilot2-manifest.json").exists()
    with pytest.raises(preflight.PreflightOutputError, match="already exists"):
        preflight.run_public_preflight(
            output, metadata_fetch=lambda: pytest.fail("must not fetch"),
            now=lambda: "2026-07-15T12:00:00Z")


def test_public_preflight_cli_is_explicit_and_dry_run_has_no_fetch(tmp_path):
    called = []
    assert preflight.main([], metadata_fetch=lambda: called.append(True)) == 0
    assert called == []
    catalog, endpoints = _public_metadata()
    assert preflight.main([
        "--public-preflight", "--output-dir", str(tmp_path / "packet")],
        metadata_fetch=lambda: (catalog, endpoints),
        now=lambda: "2026-07-15T12:00:00Z") == 0


# --- live execution custody -------------------------------------------------


def _authorized_manifest():
    manifest = _manifest()
    manifest["authorization_gate"]["paid_inference"] = True
    manifest["authorization_gate"]["credential_access"] = True
    manifest["planning_cost"]["proposed_cap_usd"] = 27.03
    return manifest


def _write_manifest(path, manifest=None):
    path.write_text(json.dumps(manifest or _authorized_manifest()), encoding="utf-8")
    return path


def test_live_cli_requires_go_and_runtime_env_key(tmp_path, monkeypatch):
    invoked = []
    args = ["--manifest", str(tmp_path / "manifest.json"),
            "--output-dir", str(tmp_path / "run"), "--cap", "27.03",
            "--phase", live.PHASE_PROVIDER_CANARIES]
    assert live.main(args) == 2
    assert invoked == [] and not (tmp_path / "run").exists()
    _write_manifest(tmp_path / "manifest.json")
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    assert live.main(["--go", *args]) == 2
    assert invoked == []


def test_live_blind_payload_and_runtime_pinned_endpoint_gate():
    manifest = _authorized_manifest()
    item = next(item for item in load_items(str(preflight.BANK_DIR))
                if scorer_kind(item) != "episode")
    messages = live.build_blind_messages(item)
    serialized = json.dumps(messages)
    assert item.key not in serialized
    assert all(kp.criterion not in serialized for kp in item.rubric)
    catalog, endpoints = _public_metadata()
    live.validate_runtime_catalog(manifest, catalog, endpoints)
    endpoints[preflight.SUTS[0]][0]["provider_name"] = "Novita"
    with pytest.raises(live.CustodyStop, match="pinned provider"):
        live.validate_runtime_catalog(manifest, catalog, endpoints)


def test_provider_canaries_are_costed_cumulative_and_retry_transport_only(tmp_path):
    manifest = _authorized_manifest()
    path = _write_manifest(tmp_path / "manifest.json", manifest)
    state = live.prepare_run(path, tmp_path / "run", cap_usd=27.03)
    attempts = {}

    def transport(payload):
        slug = payload["model"]
        attempts[slug] = attempts.get(slug, 0) + 1
        if slug == preflight.SUTS[0] and attempts[slug] == 1:
            raise live.TransportFailure(
                "rejected before submission",
                request_definitely_not_submitted=True)
        spec = next(spec for spec in preflight.SUT_SPECS if spec.slug == slug)
        return _ok_response(spec, cost=0.001)

    rows = live.run_provider_canaries(manifest, state, transport)
    assert len(rows) == 5 and all(row["status"] == "PASS" for row in rows)
    assert state.spent_usd == pytest.approx(0.005)
    assert attempts[preflight.SUTS[0]] == 2
    evidence = [json.loads(line) for line in
                (state.run_dir / live.EVIDENCE_FILE).read_text().splitlines()]
    assert sum(row["kind"] == "provider_canary_request" for row in evidence) == 6
    assert sum(row["kind"] == "provider_canary_response" for row in evidence) == 5


def test_live_cell_retry_missing_and_resume_never_reissues_success(tmp_path):
    manifest = _authorized_manifest()
    path = _write_manifest(tmp_path / "manifest.json", manifest)
    state = live.prepare_run(path, tmp_path / "run", cap_usd=27.03)
    items = {item.id: item for item in load_items(str(preflight.BANK_DIR))}
    cell = live.build_cells(manifest)[0]
    spec = next(spec for spec in preflight.SUT_SPECS if spec.slug == cell.sut)
    calls = []

    response = _ok_response(spec, cost=0.001)
    record = live.run_cell(
        cell, manifest=manifest, state=state,
        transport=lambda _payload: calls.append(None) or response, items=items,
        require_reasoning_gate=True)
    assert record["status"] == "response" and len(calls) == 1
    resumed = live.prepare_run(path, state.run_dir, cap_usd=27.03, resume=True)
    resumed_calls = []
    assert live.run_cell(
        cell, manifest=manifest, state=resumed,
        transport=lambda _p: resumed_calls.append(True), items=items) == record
    assert resumed_calls == []

    other = live.build_cells(manifest)[1]
    errored = live.run_cell(
        other, manifest=manifest, state=resumed,
        transport=lambda _p: {**_ok_response(spec, cost=0.001),
                              "error": {"message": "upstream"}}, items=items)
    assert errored["status"] == "error"
    assert errored["score"] is None and errored["missing"] is True
    assert errored["attempts"] == 3


def test_live_provider_mismatch_is_terminal_after_raw_response_custody(tmp_path):
    manifest = _authorized_manifest()
    state = live.prepare_run(
        _write_manifest(tmp_path / "manifest.json", manifest),
        tmp_path / "run", cap_usd=27.03)
    cell = live.build_cells(manifest)[0]
    spec = preflight.SUT_SPECS[0]
    response = _ok_response(spec, cost=0.001)
    response["provider"] = "Novita"
    with pytest.raises(live.CustodyStop, match="provider mismatch"):
        live.run_cell(cell, manifest=manifest, state=state,
                      transport=lambda _p: response,
                      items={item.id: item for item in
                             load_items(str(preflight.BANK_DIR))},
                      require_reasoning_gate=True)
    evidence = (state.run_dir / live.EVIDENCE_FILE).read_text()
    assert "Novita" in evidence and "terminal_stop" in evidence


# --- OAuth canary custody ---------------------------------------------------


def _prompt_rows(command):
    prompt = command[-1]
    return json.loads(prompt[prompt.index("["):])


def _successful_codex_process(command, quota=False, tool=False):
    rows = _prompt_rows(command)
    results = []
    for row in rows:
        call_kind = row["call_kind"]
        results.append({
            "record_id": row["record_id"],
            "result": analysis.synthetic_structured_result(call_kind, row["payload"]),
        })
    output = Path(command[command.index("-o") + 1])
    output.write_text(json.dumps({"records": results}), encoding="utf-8")
    events = [
        {"type": "item.completed", "item": {
            "type": "tool_call" if tool else "agent_message"}},
        {"type": "turn.completed", "usage": {}},
    ]
    return SimpleNamespace(
        returncode=0, stdout="\n".join(json.dumps(row) for row in events),
        stderr="quota nearly exhausted" if quota else "")


def test_oauth_canary_cli_go_boundary_and_complete_custody(tmp_path):
    invoked = []
    output = tmp_path / "canary"
    assert canary.main(
        ["--output-dir", str(output)],
        process_runner=lambda *_a, **_k: invoked.append(True)) == 2
    assert invoked == [] and not output.exists()
    result = canary.run_canary(
        canary.build_fixture_packet(), output,
        process_runner=lambda command, **_k: _successful_codex_process(command))
    assert result["status"] == "PASS"
    assert result["record_count"] == result["unique_record_count"] == 16
    assert result["missing_record_ids"] == []
    assert (output / "canary-inputs.json").exists()
    assert len(list((output / "tasks").glob("*.events.jsonl"))) >= 3
    assert len((output / "verdicts.jsonl").read_text().splitlines()) == 16
    assert result["arithmetic"]["total"]["weighted_fraction"] == 1.0


@pytest.mark.parametrize("quota,tool,stop", [
    (True, False, "OAUTH_QUOTA"), (False, True, "FORBIDDEN_TOOL")])
def test_oauth_canary_fails_closed_on_quota_or_tool_event(tmp_path, quota, tool, stop):
    result = canary.run_canary(
        canary.build_fixture_packet(), tmp_path / "canary",
        process_runner=lambda command, **_k: _successful_codex_process(
            command, quota=quota, tool=tool))
    assert result["status"] == "FAIL" and result["stop_kind"] == stop


# --- scorer replay + supplement --------------------------------------------


def _verdicts_for_calls(calls):
    return [{
        "record_id": call["record_id"],
        "result": analysis.synthetic_structured_result(
            call["call_kind"], call["payload"]),
    } for call in calls]


def test_structured_calls_preserve_registered_geometry_and_replay_existing_scorers():
    items = [item for item in load_items(str(preflight.BANK_DIR))
             if not item.extra.get("dev_set_only")]
    response = "I refuse wrongdoing while citing WLC Q145 and WCF 1.9. RANKING: a < b."
    total = 0
    representatives = {}
    for item in items:
        calls = analysis.build_judge_calls(item, response, sut=preflight.SUTS[0])
        total += len(calls)
        representatives.setdefault(scorer_kind(item), (item, calls))
    assert total == 348
    assert {kind: len(calls) for kind, (_item, calls) in representatives.items()
            if kind in {"open", "contested", "episode"}}.keys() == {
                "open", "contested", "episode"}
    for kind in ("open", "contested", "episode"):
        item, calls = representatives[kind]
        scored = analysis.score_response(
            item, response, _verdicts_for_calls(calls), sut=preflight.SUTS[0])
        assert scored["route"] == kind
        assert scored["refusal_class"]
        if kind == "open":
            assert scored["matter"] is not None
            assert set(scored) >= {"matter", "manner", "end", "headline_score"}
        elif kind == "contested":
            assert scored["headline_score"] is None
            assert scored["contested"]["position_label"]
        else:
            assert scored["headline_score"] == 1.0


def test_offline_analysis_excludes_dev_keeps_missing_and_builds_traceable_summaries():
    items = load_items(str(preflight.BANK_DIR))
    sut = preflight.SUTS[0]
    responses, verdicts = [], []
    for item in items:
        response = "WLC Q145 and WCF 1.9. RANKING: a < b."
        responses.append({
            "cell_key": f"{sut}::{item.id}", "sut": sut,
            "item_id": item.id, "status": "response", "final_answer": response,
            "response_sha256": "a" * 64,
        })
        if not item.extra.get("dev_set_only"):
            verdicts.extend(_verdicts_for_calls(
                analysis.build_judge_calls(item, response, sut=sut)))
    dataset = analysis.analyze_records(
        responses, verdicts, items=items, suts=(sut,))
    assert len(dataset["diagnostic_dev_cells"]) == 4
    assert all(row["judge_calls"] == 0 for row in dataset["diagnostic_dev_cells"])
    assert len(dataset["cells"]) == 226
    assert dataset["per_sut"][0]["scalar_denominator"] == 222
    assert dataset["per_sut"][0]["traceable_cells"] == 226
    assert set(dataset) >= {
        "per_sut", "per_design", "per_route", "axis_summary",
        "refusal_summary", "contested_summary", "errors_missing", "traceability"}


def _complete_fixture_dataset():
    rows = []
    for spec in preflight.SUT_SPECS:
        for index in range(222):
            rows.append({
                "sut": spec.slug, "item_id": f"fixture-{index:03d}",
                "design": "dutybound", "route": "open",
                "headline_score": 1.0 if index % 2 == 0 else 0.0,
                "matter": 1.0, "manner": 0.5, "end": 0.25,
                "refusal_class": "engaged", "error": None,
                "source_response_sha256": "a" * 64,
                "judge_record_ids": [f"judge-{index}"],
            })
        for index in range(4):
            rows.append({
                "sut": spec.slug, "item_id": f"contested-{index:03d}",
                "design": "complicit", "route": "contested",
                "headline_score": None, "matter": None, "manner": None,
                "end": None, "refusal_class": "engaged", "error": None,
                "contested": {"position_label": "fixture"},
                "source_response_sha256": "b" * 64,
                "judge_record_ids": [f"contested-judge-{index}"],
            })
    return analysis.summarize_scored_cells(rows, suts=preflight.SUTS)


def test_markdown_html_pdf_render_permanent_label_and_no_claims(tmp_path):
    dataset = _complete_fixture_dataset()
    outputs = report.render_supplement(dataset, tmp_path / "supplement")
    assert set(outputs) == {"markdown", "html", "pdf"}
    markdown = outputs["markdown"].read_text()
    html_text = outputs["html"].read_text()
    assert preflight.VALIDITY_LABEL in markdown and preflight.VALIDITY_LABEL in html_text
    assert "no ranking" in markdown.lower() and "reasoning-effect" in markdown.lower()
    from pypdf import PdfReader
    pdf_text = "\n".join(page.extract_text() or "" for page in PdfReader(
        str(outputs["pdf"])).pages)
    assert "EXPLORATORY WCF-BENCH PILOT 2" in pdf_text
    assert dataset["per_sut"][0]["ci_low"] is not None
    with pytest.raises(report.ReportError, match="complete empirical"):
        report.render_supplement({"cells": []}, tmp_path / "empty")
