from __future__ import annotations

import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest


HARNESS_ROOT = Path(__file__).resolve().parent.parent
if str(HARNESS_ROOT) not in sys.path:
    sys.path.insert(0, str(HARNESS_ROOT))

import pilot2_analysis as analysis  # noqa: E402
import pilot2_live as live  # noqa: E402
import pilot2_oauth_canary as oauth_canary  # noqa: E402
import pilot2_preflight as preflight  # noqa: E402
import pilot2_report as report  # noqa: E402
import pilot2_run as controller  # noqa: E402
from wcfbench import load_items  # noqa: E402

from test_pilot2_protocol import _catalog_and_endpoints  # noqa: E402


def _metadata(price_factor=1.0):
    catalog, endpoints = _catalog_and_endpoints()
    for spec in preflight.SUT_SPECS:
        endpoint = endpoints[spec.slug][0]
        endpoint["pricing"] = {
            "prompt": str(spec.prompt_price_per_token * price_factor),
            "completion": str(spec.completion_price_per_token * price_factor),
        }
    return catalog, endpoints


def _authorized_manifest(price_factor=1.0):
    catalog, endpoints = _metadata(price_factor)
    manifest = preflight.build_manifest(
        catalog, endpoints, catalog_retrieved_at="2026-07-15T00:00:00Z")
    manifest["authorization_gate"]["paid_inference"] = True
    manifest["authorization_gate"]["credential_access"] = True
    manifest["auth_balance"]["required_balance_usd"] = (
        manifest["planning_cost"]["proposed_cap_usd"])
    return manifest


def _write_manifest(path, manifest):
    path.write_text(json.dumps(manifest), encoding="utf-8")
    return path


def test_lower_refreshed_prices_are_the_frozen_request_max_price():
    manifest = _authorized_manifest(price_factor=0.5)
    for spec in preflight.SUT_SPECS:
        row = next(row for row in manifest["models"] if row["slug"] == spec.slug)
        request = controller.build_sut_request(
            manifest, spec.slug, [{"role": "user", "content": "blind"}])
        assert request["provider"] == row["provider_policy"]
        assert request["provider"]["max_price"] == {
            "prompt": spec.prompt_price_per_token * 500_000,
            "completion": spec.completion_price_per_token * 500_000,
        }


def test_zero_paid_preflight_returns_required_balance_without_account_access(tmp_path):
    catalog, endpoints = _metadata(price_factor=0.5)
    result = preflight.run_public_preflight(
        tmp_path / "packet", metadata_fetch=lambda: (catalog, endpoints),
        now=lambda: "2026-07-15T12:00:00Z")
    assert result["status"] == "EXECUTABLE-MANIFEST-INPUT"
    manifest = json.loads(
        (tmp_path / "packet" / "pilot2-manifest.json").read_text())
    auth = manifest["auth_balance"]
    assert auth["balance_usd"] is None and auth["top_up_usd"] is None
    assert auth["required_balance_usd"] == pytest.approx(
        manifest["planning_cost"]["proposed_cap_usd"])


def test_internal_prepare_and_execute_reject_unpaid_manifest_before_action(
    tmp_path, monkeypatch,
):
    catalog, endpoints = _metadata()
    manifest = preflight.build_manifest(
        catalog, endpoints, catalog_retrieved_at="2026-07-15T00:00:00Z")
    path = _write_manifest(tmp_path / "manifest.json", manifest)
    with pytest.raises(live.CustodyStop, match="paid authorization"):
        live.prepare_run(
            path, tmp_path / "must-not-exist",
            cap_usd=manifest["planning_cost"]["proposed_cap_usd"])
    assert not (tmp_path / "must-not-exist").exists()
    touched = []
    monkeypatch.setattr(
        live, "run_provider_canaries", lambda *_args: touched.append("canary"))
    with pytest.raises(live.CustodyStop, match="paid authorization"):
        live.execute(manifest, SimpleNamespace(), lambda _payload: touched.append("transport"))
    assert touched == []


def test_live_cli_checks_registered_balance_before_transport_construction(
    tmp_path, monkeypatch,
):
    manifest = _authorized_manifest(price_factor=0.5)
    path = _write_manifest(tmp_path / "manifest.json", manifest)
    cap = manifest["planning_cost"]["proposed_cap_usd"]
    events = []
    monkeypatch.setenv("OPENROUTER_API_KEY", "fixture-secret")
    result = live.main(
        ["--go", "--manifest", str(path), "--output-dir", str(tmp_path / "run"),
         "--cap", str(cap)],
        runtime_fetch=lambda: _metadata(price_factor=0.5),
        balance_fetch=lambda _key: events.append("balance") or {
            "limit_remaining": cap},
        transport_factory=lambda _key: events.append("transport") or (lambda _p: {}),
        execute_fn=lambda *_args: events.append("execute"))
    assert result == 0
    assert events == ["balance", "transport", "execute"]


def test_all_five_first_cells_must_pass_before_shards(monkeypatch):
    manifest = _authorized_manifest()
    state = SimpleNamespace(first_validated=set(), completed={})
    events = []
    monkeypatch.setattr(live, "run_provider_canaries", lambda *_args: [])

    def fake_run_cell(cell, **_kwargs):
        events.append(cell.key)
        if cell.sut != preflight.SUTS[-1]:
            state.first_validated.add(cell.sut)
            return {"status": "response"}
        return {"status": "error", "missing": True}

    monkeypatch.setattr(live, "run_cell", fake_run_cell)
    with pytest.raises(live.CustodyStop, match="five first real cells"):
        live.execute(manifest, state, lambda _payload: {})
    assert len(events) == 5


def test_full_run_judge_driver_builds_1740_calls_and_persists_each_valid_result(
    tmp_path,
):
    items = load_items(str(preflight.BANK_DIR))
    responses = []
    for sut in preflight.SUTS:
        for item in items:
            responses.append({
                "kind": "pilot2_cell", "cell_key": f"{sut}::{item.id}",
                "sut": sut, "item_id": item.id, "status": "response",
                "final_answer": "WLC Q145 and WCF 1.9. RANKING: a < b.",
                "response_sha256": "a" * 64,
                "diagnostic_only": bool(item.extra.get("dev_set_only")),
                "scorable": not bool(item.extra.get("dev_set_only")),
            })
    evidence_dir = tmp_path / "evidence"
    evidence_dir.mkdir()
    manifest = _authorized_manifest()
    (evidence_dir / live.MANIFEST_COPY).write_text(
        json.dumps(manifest), encoding="utf-8")
    canary_report = tmp_path / "canary-report.json"
    canary_report.write_text(json.dumps({
        "schema_version": 1,
        "validity_label": preflight.VALIDITY_LABEL,
        "status": "PASS", "record_count": 16,
        "unique_record_count": 16, "missing_record_ids": [],
        "stop_kind": None, "stop_reason": None,
        "input_sha256": oauth_canary.build_fixture_packet()["input_sha256"],
    }), encoding="utf-8")
    (evidence_dir / live.CHECKPOINT_FILE).write_text(
        "".join(json.dumps(row) + "\n" for row in responses), encoding="utf-8")
    persisted_sizes = []

    class FixtureJudge:
        def __init__(self, persist):
            self.persist = persist

        def judge(self, batch):
            returned = []
            for call in batch:
                row = {
                    "record_id": call["record_id"],
                    "result": analysis.synthetic_structured_result(
                        call["call_kind"], call["payload"]),
                }
                self.persist(row)
                persisted_sizes.append(
                    (evidence_dir / "judge-verdicts.jsonl").stat().st_size)
                returned.append(row)
            return {"records": returned, "missing_record_ids": [], "attempts": 1}

    result = analysis.run_judge_driver(
        evidence_dir, items=items, oauth_canary_report=canary_report,
        judge_factory=lambda persist: FixtureJudge(persist))
    verdicts = [json.loads(line) for line in
                (evidence_dir / "judge-verdicts.jsonl").read_text().splitlines()]
    assert result["logical_judge_calls"] == result["persisted_verdicts"] == 1740
    assert len(verdicts) == len({row["record_id"] for row in verdicts}) == 1740
    assert len(persisted_sizes) == 1740
    assert all(right > left for left, right in zip(persisted_sizes, persisted_sizes[1:]))


def test_report_accepts_1130_scorable_cells_with_20_contested_separate(tmp_path):
    rows = []
    for sut in preflight.SUTS:
        for index in range(222):
            rows.append({
                "sut": sut, "item_id": f"scalar-{index:03d}",
                "design": "dutybound", "route": "open",
                "headline_score": float(index % 2),
                "matter": 1.0, "manner": .5, "end": .25,
                "refusal_class": "engaged", "error": None,
                "source_response_sha256": "a" * 64,
                "judge_record_ids": [f"judge-{index}"],
            })
        for index in range(4):
            rows.append({
                "sut": sut, "item_id": f"contested-{index:03d}",
                "design": "complicit", "route": "contested",
                "headline_score": None, "matter": None, "manner": None,
                "end": None, "refusal_class": "engaged", "error": None,
                "contested": {"position_label": "fixture"},
                "source_response_sha256": "b" * 64,
                "judge_record_ids": [f"contested-judge-{index}"],
            })
    dataset = analysis.summarize_scored_cells(rows, suts=preflight.SUTS)
    assert len(dataset["cells"]) == 1130
    assert len(dataset["contested_summary"]) == 20
    assert len(dataset["errors_missing"]) == 0
    outputs = report.render_supplement(dataset, tmp_path / "supplement")
    assert set(outputs) == {"markdown", "html", "pdf"}
