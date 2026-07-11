"""Offline contract tests for CHARITROC panel orchestration."""
from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import uuid

import pytest

import generator
from analysis import analyze as bank_analysis
from pilot import contracts, manifest, openrouter_driver, run_panel


MOCK_PROVENANCE = "harness validation, NOT a measurement"


def test_documented_script_entrypoint_loads_from_bank_root():
    bank_root = Path(run_panel.__file__).resolve().parents[1]
    completed = subprocess.run(
        [sys.executable, "pilot/run_panel.py", "--help"],
        cwd=bank_root,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    assert "Run the frozen CHARITROC Codex/OpenRouter panel" in completed.stdout
    access_help = subprocess.run(
        [sys.executable, "pilot/run_panel.py", "access", "--help"],
        cwd=bank_root,
        capture_output=True,
        text=True,
        check=False,
    )
    assert access_help.returncode == 0, access_help.stderr
    assert "--retry-failed-access" in access_help.stdout


@pytest.fixture(scope="module")
def bank_data():
    episodes, sidecar, _stats, _pairs = generator.generate(20260709)
    judge_map = generator.build_judge_token_map(episodes, 20260709)
    return episodes, sidecar, judge_map


class TickClock:
    def __init__(self):
        self.current = datetime(2026, 7, 10, 12, 0, tzinfo=timezone.utc)

    def __call__(self):
        value = self.current
        self.current += timedelta(seconds=1)
        return value.strftime("%Y-%m-%dT%H:%M:%SZ")


def _response(intent, decision, reason="Fixture response."):
    return json.dumps({
        "reason": reason,
        "INTENT": intent,
        "DECISION": decision,
    }, separators=(",", ":"))


class FakePanelDriver:
    """Provider-neutral fake that emits real validated stage contracts."""

    def __init__(self, sidecar, *, crash_calls=(), unresolved=()):
        self.sidecar = sidecar
        self.crash_calls = set(crash_calls)
        self.unresolved = set(unresolved)
        self.calls = []
        self.provider_stage_calls = []

    def _stage_response(self, item_id, model, stage, call_number):
        if (call_number, stage) in self.unresolved:
            return "not canonical JSON"
        if item_id.startswith("ACCESS-PROBE-"):
            return _response(
                "UNCERTAIN", "VERIFY", "Access probe response."
            )
        hidden = self.sidecar[item_id]
        true_type = hidden["true_type"]
        cue = hidden["cue_variant"]
        if stage in {"stage_1", "stage_2"}:
            return _response("UNCERTAIN", "VERIFY")
        if stage == "stage_3":
            if cue in {"absent", "adversarial"}:
                return _response("UNCERTAIN", "VERIFY")
            if true_type == "benign":
                return _response(
                    "BENIGN", "GRANT" if cue == "strong" else "CONDITIONAL"
                )
            return _response(
                "MALICIOUS", "REFUSE" if cue == "strong" else "RESTRICT"
            )
        if model == "gpt-5.4-mini":
            return _response("UNCERTAIN", "VERIFY")
        if true_type == "benign":
            return _response(
                "BENIGN", "GRANT" if model == "gpt-5.5" else "CONDITIONAL"
            )
        return _response(
            "MALICIOUS", "REFUSE" if model == "gpt-5.5" else "RESTRICT"
        )

    def run_episode(
            self, episode, *, logical_model_id, provider,
            before_stage=None, stage_sink=None):
        call_number = len(self.calls) + 1
        self.calls.append((
            episode["id"], logical_model_id, provider,
        ))
        if call_number in self.crash_calls:
            raise RuntimeError("simulated orchestrator-visible crash")

        panel_row = next(
            row for row in manifest.load_panel()["models"]
            if row["logical_model_id"] == logical_model_id
        )
        provider_row = panel_row["providers"][provider]
        execution_id = str(uuid.UUID(int=call_number + 1, version=4))
        session_id = (
            "thread-" + execution_id if provider == "codex" else None
        )
        requests = []
        results = []
        descriptors = []
        prior = {}
        for index, stage in enumerate(contracts.STAGES):
            request = contracts.build_stage_request(
                episode,
                execution_id=execution_id,
                provider=provider,
                logical_model_id=logical_model_id,
                provider_model_id=provider_row["provider_model_id"],
                configuration_id=provider_row["configuration_id"],
                stage=stage,
                prior_responses=prior,
            )
            raw = self._stage_response(
                episode["id"], logical_model_id, stage, call_number
            )
            descriptor = {
                "fixture": True,
                "provider": provider,
                "request_sha256": request["request_sha256"],
                "stage": stage,
            }
            hook_event = {
                "provider": provider,
                "integrity_session": 1,
                "execution_id": execution_id,
                "stage": stage,
                "request": request,
                "transport_descriptor": descriptor,
                "attestation": None,
            }
            if before_stage is not None:
                before_stage(deepcopy(hook_event))
            self.provider_stage_calls.append(stage)
            transport_hash = contracts.canonical_sha256(descriptor)
            started = f"2026-07-10T12:{call_number % 60:02d}:{index * 2:02d}Z"
            completed = f"2026-07-10T12:{call_number % 60:02d}:{index * 2 + 1:02d}Z"
            attempt = contracts.build_stage_attempt(
                attempt_index=1,
                started_at_utc=started,
                completed_at_utc=completed,
                provider_request_id=f"fixture-{call_number}-{index + 1}",
                token_emission_started=True,
                exit_status=0 if provider == "codex" else None,
                http_status=200 if provider == "openrouter" else None,
                finish_reason="stop",
                usage={
                    "input_tokens": 10,
                    "cached_input_tokens": 0,
                    "output_tokens": 5,
                    "reasoning_tokens": 1,
                    "total_tokens": 15,
                },
                raw_trace=raw,
                raw_final_message=raw,
                reasoning_effort="medium",
                reasoning_details=None,
                error_code=None,
            )
            result = contracts.build_stage_result(
                request,
                run_mode="mock",
                returned_provider_model_id=provider_row["provider_model_id"],
                returned_provider_name="OpenAI",
                session_id=session_id,
                transport_request_sha256=transport_hash,
                attempts=[attempt],
                tool_events=[],
                session_chain_ok=True,
                isolation_ok=True,
                future_text_absent=True,
            )
            requests.append(request)
            results.append(result)
            descriptors.append(descriptor)
            if stage_sink is not None:
                stage_sink({
                    **deepcopy(hook_event),
                    "result": deepcopy(result),
                    "attestation": None,
                })
            prior[stage] = raw

        chain = contracts.build_stage_chain(requests, results, episode)
        status = (
            "complete"
            if all(row["terminal_status"] == "complete" for row in results)
            else "unresolved"
        )
        session = {
            "integrity_session": 1,
            "execution_id": execution_id,
            "status": status,
            "requests": requests,
            "results": results,
            "transport_descriptors": descriptors,
            "attestations": [None] * 4,
            "chain": chain,
        }
        return {
            "status": status,
            "provenance": MOCK_PROVENANCE,
            "integrity_session_count": 1,
            "sessions": [session],
            "requests": requests,
            "results": results,
            "transport_descriptors": descriptors,
            "chain": chain,
        }


class MultiAttemptFirstStageDriver(FakePanelDriver):
    """Expose a three-attempt first stage so ledger recovery is testable."""

    def run_episode(self, episode, *, logical_model_id, provider,
                    before_stage=None, stage_sink=None):
        def expanded_sink(event):
            if event["stage"] != "stage_1":
                return stage_sink(event) if stage_sink is not None else None
            old = event["result"]
            attempts = []
            for index, status in ((1, 429), (2, 503)):
                attempts.append(contracts.build_stage_attempt(
                    attempt_index=index,
                    started_at_utc=f"2026-07-10T12:00:0{2 * index - 2}Z",
                    completed_at_utc=f"2026-07-10T12:00:0{2 * index - 1}Z",
                    provider_request_id=f"retry-{index}",
                    token_emission_started=False,
                    exit_status=None,
                    http_status=status,
                    finish_reason=None,
                    usage={key: None for key in contracts.USAGE_KEYS},
                    raw_trace=json.dumps({"error": status}),
                    raw_final_message=None,
                    reasoning_effort="medium",
                    reasoning_details=None,
                    error_code=f"http_{status}",
                ))
            final = old["attempts"][-1]
            attempts.append(contracts.build_stage_attempt(
                attempt_index=3,
                started_at_utc=final["started_at_utc"],
                completed_at_utc=final["completed_at_utc"],
                provider_request_id=final["provider_request_id"],
                token_emission_started=final["token_emission_started"],
                exit_status=final["exit_status"],
                http_status=final["http_status"],
                finish_reason=final["finish_reason"],
                usage=final["usage"],
                raw_trace=final["raw_trace"],
                raw_final_message=final["raw_final_message"],
                reasoning_effort=final["reasoning_effort"],
                reasoning_details=final["reasoning_details"],
                error_code=final["error_code"],
            ))
            event = deepcopy(event)
            event["result"] = contracts.build_stage_result(
                event["request"],
                run_mode="mock",
                returned_provider_model_id=old[
                    "returned_provider_model_id"
                ],
                returned_provider_name=old["returned_provider_name"],
                session_id=old["session_id"],
                transport_request_sha256=old[
                    "transport_request_sha256"
                ],
                attempts=attempts,
                tool_events=old["tool_events"],
                session_chain_ok=old["integrity"]["session_chain_ok"],
                isolation_ok=old["integrity"]["isolation_ok"],
                future_text_absent=old["integrity"]["future_text_absent"],
            )
            return stage_sink(event) if stage_sink is not None else None

        return super().run_episode(
            episode,
            logical_model_id=logical_model_id,
            provider=provider,
            before_stage=before_stage,
            stage_sink=expanded_sink,
        )


class CrashAfterAccessStartDriver(FakePanelDriver):
    """Crash after the provider-start hook but before terminal evidence."""

    def run_episode(self, episode, *, logical_model_id, provider,
                    before_stage=None, stage_sink=None):
        def crash_after_start(event):
            if before_stage is not None:
                before_stage(event)
            raise RuntimeError("simulated post-start access crash")

        return super().run_episode(
            episode,
            logical_model_id=logical_model_id,
            provider=provider,
            before_stage=crash_after_start,
            stage_sink=stage_sink,
        )


def make_runner(tmp_path, bank_data, driver, *, provider="codex", **kwargs):
    episodes, sidecar, judge_map = bank_data
    return run_panel.PanelOrchestrator(
        bank_root=Path(__file__).resolve().parents[1],
        out_dir=tmp_path,
        provider=provider,
        run_mode="mock",
        driver=driver,
        episodes=episodes,
        sidecar=sidecar,
        judge_token_map=judge_map,
        clock=kwargs.pop("clock", TickClock()),
        bootstrap_draws=kwargs.pop("bootstrap_draws", 100),
        **kwargs,
    )


def test_live_codex_replay_uses_controlled_context_audit_restore():
    class ReplayDriver:
        def __init__(self):
            self.context_audits = {}
            self.fingerprint = self._fingerprint()
            self.restored = []
            self.validated = []

        def _fingerprint(self):
            return contracts.canonical_sha256({
                str(path): audit
                for path, audit in self.context_audits.items()
            })

        def restore_persisted_context_audit(self, isolation_dir, audit):
            self.context_audits[isolation_dir] = deepcopy(audit)
            self.fingerprint = self._fingerprint()
            self.restored.append((isolation_dir, deepcopy(audit)))

        def validate_stage_evidence(self, *args, **kwargs):
            assert self.fingerprint == self._fingerprint()
            self.validated.append((args, kwargs))

    runner = object.__new__(run_panel.PanelOrchestrator)
    runner.run_mode = "live"
    runner.provider = "codex"
    runner._live_codex = ReplayDriver()
    audit = {"audit_sha256": "safe-fixture"}
    payload = {
        "request": {"stage": "stage_1"},
        "result": {"session_id": "thread-fixture"},
        "transport_descriptor": {
            "cwd": "/tmp/cx-replayed",
            "context_audit": audit,
        },
        "attestation": {"source": "fixture"},
    }

    assert runner._validate_provider_evidence(
        payload,
        episode={"multiturn_script": {
            stage: stage for stage in contracts.STAGES
        }},
        prior_artifacts=[],
    ) is True
    assert runner._live_codex.restored == [
        (Path("/tmp/cx-replayed").resolve(), audit)
    ]
    assert len(runner._live_codex.validated) == 1


@pytest.fixture(scope="module")
def completed_smoke(tmp_path_factory, bank_data):
    root = tmp_path_factory.mktemp("completed-smoke")
    runner = make_runner(root, bank_data, FakePanelDriver(bank_data[1]))
    runner.execute("smoke")
    return root


@pytest.fixture(scope="module")
def completed_unresolved_smoke(tmp_path_factory, bank_data):
    root = tmp_path_factory.mktemp("completed-unresolved-smoke")
    driver = FakePanelDriver(bank_data[1], unresolved={(1, "stage_3")})
    runner = make_runner(root, bank_data, driver)
    runner.execute("smoke")
    return root


@pytest.fixture(scope="module")
def completed_calibration_reliability(tmp_path_factory, bank_data):
    root = tmp_path_factory.mktemp("completed-calibration-reliability")
    runner = make_runner(root, bank_data, FakePanelDriver(bank_data[1]))
    runner.execute("calibration")
    runner.execute("reliability")
    return root


def replay_copy(tmp_path, source, bank_data):
    target = tmp_path / "replay"
    shutil.copytree(source, target)
    return target, make_runner(
        target, bank_data, FakePanelDriver(bank_data[1])
    )


def read_json(path):
    return json.loads(Path(path).read_text())


def read_jsonl(path):
    return [json.loads(line) for line in Path(path).read_text().splitlines()]


def test_persistence_helpers_flush_and_fsync_before_return(tmp_path, monkeypatch):
    fsync_calls = []
    monkeypatch.setattr(
        run_panel.os, "fsync", lambda descriptor: fsync_calls.append(descriptor)
    )

    run_panel._write_new_json(tmp_path / "immutable.json", {"value": 1})
    run_panel._append_jsonl(tmp_path / "events.jsonl", {"event": 1})

    assert len(fsync_calls) >= 2


def test_provider_run_mode_and_mock_driver_are_explicit(tmp_path, bank_data):
    episodes, sidecar, judge_map = bank_data
    with pytest.raises(ValueError, match="provider"):
        run_panel.PanelOrchestrator(
            bank_root=Path(__file__).resolve().parents[1],
            out_dir=tmp_path,
            provider="auto",
            run_mode="mock",
            driver=object(),
            episodes=episodes,
            sidecar=sidecar,
            judge_token_map=judge_map,
        )
    with pytest.raises(ValueError, match="mock driver"):
        run_panel.PanelOrchestrator(
            bank_root=Path(__file__).resolve().parents[1],
            out_dir=tmp_path,
            provider="codex",
            run_mode="mock",
            episodes=episodes,
            sidecar=sidecar,
            judge_token_map=judge_map,
        )
    with pytest.raises(ValueError, match="production"):
        run_panel.PanelOrchestrator(
            bank_root=Path(__file__).resolve().parents[1],
            out_dir=tmp_path,
            provider="codex",
            run_mode="live",
            driver=object(),
            episodes=episodes,
            sidecar=sidecar,
            judge_token_map=judge_map,
        )
    with pytest.raises(ValueError, match="bootstrap.*production"):
        run_panel.PanelOrchestrator(
            bank_root=Path(__file__).resolve().parents[1],
            out_dir=tmp_path,
            provider="codex",
            run_mode="live",
            bootstrap_draws=100,
        )


def test_smoke_is_occurrence_major_and_persists_before_completion(
        tmp_path, bank_data):
    driver = FakePanelDriver(bank_data[1])
    runner = make_runner(tmp_path, bank_data, driver)

    report = runner.execute("smoke")
    plan = read_json(tmp_path / "plans" / "smoke.json")
    expected_order = [
        (entry["item_id"], model, "codex")
        for entry in plan["entries"]
        for model in entry["model_execution_order"]
    ]

    assert driver.calls == expected_order
    assert report["provenance"] == MOCK_PROVENANCE
    assert report["harness"]["measurement_ready"] is True
    state = read_jsonl(tmp_path / "state" / "smoke.jsonl")
    ledger = read_jsonl(tmp_path / "ledger" / "smoke.jsonl")
    assert len(state) == 72 * 2
    assert len(ledger) == 72 * 4
    assert all(row["state"] == "persisted" for row in ledger)
    assert all(row["format_repair_count"] == 0 for row in ledger)
    for event in state:
        if event["state"] == "complete":
            bound = [row for row in ledger if (
                row["plan_occurrence_id"] == event["plan_occurrence_id"]
                and row["logical_model_id"] == event["logical_model_id"]
            )]
            assert len(bound) == 4
    assert runner.verify("smoke")["valid"] is True


def test_crash_resume_never_overwrites_completed_artifacts(tmp_path, bank_data):
    first = FakePanelDriver(bank_data[1], crash_calls={2})
    runner = make_runner(tmp_path, bank_data, first)
    with pytest.raises(RuntimeError, match="simulated"):
        runner.execute("smoke")

    completed_path = next((tmp_path / "evidence" / "smoke").rglob("stage_4.json"))
    completed_hash = hashlib.sha256(completed_path.read_bytes()).hexdigest()
    second = FakePanelDriver(bank_data[1])
    resumed = make_runner(tmp_path, bank_data, second)
    resumed.execute("smoke")
    assert hashlib.sha256(completed_path.read_bytes()).hexdigest() == completed_hash
    assert len(second.calls) == 71

    third = FakePanelDriver(bank_data[1])
    make_runner(tmp_path, bank_data, third).execute("smoke")
    assert third.calls == []
    state = read_jsonl(tmp_path / "state" / "smoke.jsonl")
    retried = [row for row in state if row["state"] == "retry"]
    assert len(retried) == 1
    assert retried[0]["attempt"] == 1


def test_unresolved_is_queued_without_repair_or_guess(tmp_path, bank_data):
    driver = FakePanelDriver(bank_data[1], crash_calls={2}, unresolved={(1, "stage_3")})
    runner = make_runner(tmp_path, bank_data, driver)
    with pytest.raises(RuntimeError, match="simulated"):
        runner.execute("smoke")

    queue = read_jsonl(tmp_path / "judge_queue" / "smoke.jsonl")
    assert len(queue) == 1
    assert set(queue[0]) == set(run_panel.JUDGE_QUEUE_KEYS)
    assert queue[0]["provenance"] == MOCK_PROVENANCE
    assert "item_id" not in queue[0]
    score = next((tmp_path / "scores" / "smoke").rglob("*.json"))
    scored = read_json(score)
    assert scored["unresolved"] is True
    assert scored["judge_queued"] is True
    assert scored["mechanically_resolved"] is False
    assert scored["format_repair_count"] == 0
    assert scored["format_repair_flagged"] is False
    assert scored["semantic_response_replaced"] is False


def test_replay_rejects_evidence_ledger_and_state_tamper(tmp_path, bank_data):
    driver = FakePanelDriver(bank_data[1])
    runner = make_runner(tmp_path, bank_data, driver)
    runner.execute("smoke")
    evidence = next((tmp_path / "evidence" / "smoke").rglob("stage_1.json"))
    original = evidence.read_text()
    payload = json.loads(original)
    payload["item_id"] = "CHARITROC-9999"
    evidence.write_text(json.dumps(payload))
    with pytest.raises(ValueError, match="evidence|artifact|item"):
        runner.verify("smoke")
    evidence.write_text(original)

    state_path = tmp_path / "state" / "smoke.jsonl"
    state_original = state_path.read_text()
    first_state_line = state_original.splitlines()[0]
    with state_path.open("a", encoding="utf-8") as handle:
        handle.write(first_state_line + "\n")
    with pytest.raises(ValueError, match="duplicate.*run-state"):
        runner.verify("smoke")
    state_path.write_text(state_original)

    state_rows = [json.loads(line) for line in state_original.splitlines()]
    state_rows[0]["event_id"] = "panel-" + "f" * 64
    state_path.write_text(
        "\n".join(json.dumps(row) for row in state_rows) + "\n"
    )
    with pytest.raises(ValueError, match="event.*id|run-state.*hash"):
        runner.verify("smoke")
    state_path.write_text(state_original)

    ledger_path = tmp_path / "ledger" / "smoke.jsonl"
    first_line = ledger_path.read_text().splitlines()[0]
    with ledger_path.open("a", encoding="utf-8") as handle:
        handle.write(first_line + "\n")
    with pytest.raises(ValueError, match="duplicate"):
        runner.verify("smoke")


def test_calibration_reliability_links_and_analysis_are_separate(
        completed_calibration_reliability, bank_data):
    tmp_path = completed_calibration_reliability
    runner = make_runner(
        tmp_path, bank_data, FakePanelDriver(bank_data[1])
    )

    reliability_scores = list(
        (tmp_path / "scores" / "reliability").rglob("*.json")
    )
    assert len(reliability_scores) == 24 * 3
    for path in reliability_scores:
        score = read_json(path)
        link = score["reliability_primary_link"]
        assert set(link) == {
            "calibration_occurrence_id", "calibration_score_sha256",
        }
        assert len(link["calibration_score_sha256"]) == 64

    report = runner.analyze()
    assert report["provenance"] == MOCK_PROVENANCE
    assert report["bootstrap_draws"] == 100
    assert report["channels_reported_separately"] is True
    assert set(report["summary"]["models"]) == set(manifest.MODEL_LOGICAL_IDS)
    assert all(len(row["family_auc"]) == 12
               for row in report["summary"]["models"].values())
    assert all(len(row["signed_distance_by_cell"]) == 9
               for row in report["summary"]["models"].values())
    assert set(report["repeats"]["dimensions"]) == {
        "stage4_action_score", "stage3_update_correct",
    }
    assert "ambiguity_control_sensitivity" in report
    assert "gate_report" in report


def test_analysis_helpers_persist_explicit_live_provenance():
    provenance = run_panel.LIVE_PROVENANCE["openrouter"]
    primary = []
    for family in ("fixture-family-a", "fixture-family-b"):
        for pair_index, prior in enumerate((0.2, 0.5, 0.8)):
            pair_id = f"{family}-pair-{pair_index}"
            primary.extend([
                {
                    "item_family": family,
                    "label": 0,
                    "stage4_score": 0,
                    "pair_id": pair_id,
                    "base_rate_benign": prior,
                    "provenance": provenance,
                },
                {
                    "item_family": family,
                    "label": 1,
                    "stage4_score": 4,
                    "pair_id": pair_id,
                    "base_rate_benign": prior,
                    "provenance": provenance,
                },
            ])
    analyzed = bank_analysis.analyze_model(
        primary, bootstrap_draws=100, seed=7, provenance=provenance
    )
    update = bank_analysis.aggregate_stage3([
        {
            "update_correct": True,
            "cue_variant": cue,
            "provenance": provenance,
        }
        for cue in ("strong", "weak", "absent", "adversarial")
    ], provenance=provenance)

    assert analyzed["provenance"] == provenance
    assert update["provenance"] == provenance


class FreezeHarness:
    def __init__(self):
        self.validate_calls = []

    def build(self, **_kwargs):
        payload = {
            "fixture": True,
            "provenance": MOCK_PROVENANCE,
        }
        payload["freeze_hash"] = contracts.canonical_sha256(payload)
        return payload

    def validate(self, freeze, **kwargs):
        self.validate_calls.append((freeze["freeze_hash"], kwargs["item_id"]))
        return {"valid": True, "freeze_hash": freeze["freeze_hash"]}


def calibration_analysis_record(runner, *, passing=True):
    families = [f"FAMILY-{index:02d}" for index in range(12)]
    family_triggers = {
        family: {
            "triggered": False,
            "all_models_auc_ceiling_trigger": False,
            "same_terminal_decision_trigger": False,
            "same_terminal_decision_rate": 0.5,
        }
        for family in families
    }
    report = {
        "analysis_version": run_panel.ANALYSIS_VERSION,
        "provenance": runner.provenance,
        "provider": runner.provider,
        "bootstrap_draws": runner.bootstrap_draws,
        "channels_reported_separately": True,
        "harness": {
            "passed": True,
            "sample_cells_complete": True,
            "measurement_ready": True,
        },
        "summary": {"models": {
            model: {"family_auc": {
                family: 0.7 for family in families
            }}
            for model in manifest.MODEL_LOGICAL_IDS
        }},
        "model_reports": {},
        "family_rows": [],
        "operating_point_rows": [],
        "repeats": {},
        "ambiguity_controls": {"passed": True},
        "ambiguity_control_sensitivity": {},
        "gate_report": {
            "measurement_ready": True,
            "channels_reported_separately": True,
            "saturation": {
                "evaluated": True,
                "failed": not passing,
                "family_hardening_triggers": family_triggers,
            },
            "noninformative": {"evaluated": True, "failed": False},
            "discrimination": {"evaluated": True, "passed": passing},
            "monotonic_order": {"descriptive_only": True},
        },
    }
    report["analysis_sha256"] = contracts.canonical_sha256(report)
    return report


@pytest.mark.parametrize(
    "mutation", ["forged_hash", "failed_gate", "family_trigger"]
)
def test_private_freeze_rejects_forged_or_failed_calibration_analysis(
        tmp_path, bank_data, mutation):
    freeze = FreezeHarness()
    runner = make_runner(
        tmp_path, bank_data, FakePanelDriver(bank_data[1]),
        freeze_builder=freeze.build,
        private_validator=freeze.validate,
    )
    report = calibration_analysis_record(
        runner, passing=mutation != "failed_gate"
    )
    if mutation == "forged_hash":
        report["analysis_sha256"] = "0" * 64
    elif mutation == "family_trigger":
        first = sorted(report["gate_report"]["saturation"][
            "family_hardening_triggers"
        ])[0]
        trigger = report["gate_report"]["saturation"][
            "family_hardening_triggers"
        ][first]
        trigger["triggered"] = True
        trigger["same_terminal_decision_trigger"] = True
        trigger["same_terminal_decision_rate"] = 0.95
        report["analysis_sha256"] = contracts.canonical_sha256({
            key: value for key, value in report.items()
            if key != "analysis_sha256"
        })
    run_panel._write_new_json(
        tmp_path / "reports" / "calibration-analysis.json", report
    )

    with pytest.raises(ValueError, match="calibration.*(hash|gate|pass|valid)"):
        runner.freeze()


def test_private_refuses_before_freeze_and_revalidates_before_every_call(
        tmp_path, bank_data):
    driver = FakePanelDriver(bank_data[1])
    freeze = FreezeHarness()
    runner = make_runner(
        tmp_path, bank_data, driver,
        freeze_builder=freeze.build,
        private_validator=freeze.validate,
    )
    with pytest.raises(ValueError, match="freeze"):
        runner.execute("private")
    assert driver.calls == []

    runner.freeze()
    crashing = FakePanelDriver(bank_data[1], crash_calls={4})
    resumed = make_runner(
        tmp_path, bank_data, crashing,
        freeze_builder=freeze.build,
        private_validator=freeze.validate,
    )
    with pytest.raises(RuntimeError, match="simulated"):
        resumed.execute("private")
    assert len(crashing.calls) == 4
    assert len(freeze.validate_calls) == 12
    assert [item for _hash, item in freeze.validate_calls] == [
        item for item, _model, _provider in crashing.calls[:3]
        for _stage in contracts.STAGES
    ]
    plan = read_json(tmp_path / "plans" / "private.json")
    assert plan["extension_entries"]
    state_text = (tmp_path / "state" / "private.jsonl").read_text()
    assert "private-extension" not in state_text


def test_cli_requires_explicit_provider_and_mode_and_has_all_commands():
    parser = run_panel.build_parser()
    for command in (
            "access", "verify-access", "smoke", "calibration",
            "reliability", "analyze", "freeze", "private",
            "analyze-private", "activate-private-extension",
            "private-extension", "verify"):
        with pytest.raises(SystemExit):
            parser.parse_args([command, "--out", "/tmp/x"])
        parsed = parser.parse_args([
            command, "--out", "/tmp/x", "--provider", "codex",
            "--run-mode", "live",
        ])
        assert parsed.command == command
        assert parsed.provider == "codex"
        assert parsed.run_mode == "live"


def test_stage_sink_is_durable_before_next_call_and_retry_never_overwrites(
        tmp_path, bank_data):
    driver = FakePanelDriver(bank_data[1])
    runner = make_runner(tmp_path, bank_data, driver)
    original = runner._persist_stage_event

    def crash_after_durable_sink(*args, **kwargs):
        persisted = original(*args, **kwargs)
        event = kwargs.get("event", args[-1])
        if event["stage"] == "stage_1":
            raise RuntimeError("sink callback crash")
        return persisted

    runner._persist_stage_event = crash_after_durable_sink
    with pytest.raises(RuntimeError, match="sink callback crash"):
        runner.execute("smoke")

    assert driver.provider_stage_calls == ["stage_1"]
    first = next((tmp_path / "evidence" / "smoke").rglob("stage_1.json"))
    assert "orchestration-1" in first.parts
    first_hash = hashlib.sha256(first.read_bytes()).hexdigest()
    assert len(read_jsonl(tmp_path / "ledger" / "smoke.jsonl")) == 1
    assert len(read_jsonl(tmp_path / "invocations" / "smoke.jsonl")) == 1

    resumed_driver = FakePanelDriver(bank_data[1])
    resumed = make_runner(tmp_path, bank_data, resumed_driver)
    resumed.execute("smoke")
    assert hashlib.sha256(first.read_bytes()).hexdigest() == first_hash
    assert next((tmp_path / "evidence" / "smoke").rglob(
        "orchestration-2/session-1/stage_1.json"
    )).is_file()
    journal = read_jsonl(tmp_path / "invocations" / "smoke.jsonl")
    first_payload = read_json(first)
    retried_episode = [row for row in journal if (
        row["plan_occurrence_id"] == first_payload["plan_occurrence_id"]
        and row["logical_model_id"] == first_payload["logical_model_id"]
    )]
    assert not any(
        row["journal_state"] == "abandoned"
        and row["orchestration_attempt"] == 1
        and row["stage"] == "stage_1"
        for row in retried_episode
    )
    assert [row["stage"] for row in retried_episode if (
        row["journal_state"] == "started"
        and row["orchestration_attempt"] == 2
    )] == list(contracts.STAGES)


def test_resume_repairs_partial_multi_attempt_ledger_without_abandoning_evidence(
        tmp_path, bank_data):
    driver = MultiAttemptFirstStageDriver(bank_data[1])
    runner = make_runner(tmp_path, bank_data, driver)
    original_append = runner._append_ledger
    crashed = False

    def crash_after_first_ledger(stage, event, plan):
        nonlocal crashed
        original_append(stage, event, plan)
        if not crashed and event["transport_attempt"] == 1:
            crashed = True
            raise RuntimeError("partial ledger crash")

    runner._append_ledger = crash_after_first_ledger
    with pytest.raises(RuntimeError, match="partial ledger crash"):
        runner.execute("smoke")

    evidence = next((tmp_path / "evidence" / "smoke").rglob(
        "orchestration-1/session-1/stage_1.json"
    ))
    evidence_hash = hashlib.sha256(evidence.read_bytes()).hexdigest()
    assert len(read_jsonl(tmp_path / "ledger" / "smoke.jsonl")) == 1

    resumed = make_runner(
        tmp_path, bank_data, FakePanelDriver(bank_data[1])
    )
    resumed.execute("smoke")
    assert hashlib.sha256(evidence.read_bytes()).hexdigest() == evidence_hash
    first = read_json(evidence)
    old_rows = [row for row in read_jsonl(
        tmp_path / "ledger" / "smoke.jsonl"
    ) if (
        row["plan_occurrence_id"] == first["plan_occurrence_id"]
        and row["logical_model_id"] == first["logical_model_id"]
        and row["orchestration_attempt"] == 1
        and row["stage"] == "stage_1"
    )]
    assert [row["transport_attempt"] for row in old_rows] == [1, 2, 3]
    assert not any(row["journal_state"] == "abandoned" for row in read_jsonl(
        tmp_path / "invocations" / "smoke.jsonl"
    ) if (
        row["plan_occurrence_id"] == first["plan_occurrence_id"]
        and row["logical_model_id"] == first["logical_model_id"]
        and row["orchestration_attempt"] == 1
        and row["stage"] == "stage_1"
    ))
    assert resumed.verify("smoke")["valid"] is True


def test_verify_rejects_missing_ledger_and_evidence_accounting(
        tmp_path, completed_smoke, bank_data):
    root, runner = replay_copy(tmp_path, completed_smoke, bank_data)
    (root / "ledger" / "smoke.jsonl").write_text("")
    shutil.rmtree(root / "evidence" / "smoke")

    with pytest.raises(ValueError, match="accounting|evidence|ledger"):
        runner.verify("smoke")


def test_verify_rederives_sidecar_truth_scores_and_evidence_links(
        tmp_path, completed_smoke, bank_data):
    root, runner = replay_copy(tmp_path, completed_smoke, bank_data)
    score_path = next((root / "scores" / "smoke").rglob("*.json"))
    score = read_json(score_path)
    score["label"] = 1 - score["label"]
    score["true_type"] = (
        "malicious" if score["true_type"] == "benign" else "benign"
    )
    score["stage4_score"] = 999
    score["evidence_sha256s"] = ["0" * 64]
    score["score_sha256"] = contracts.canonical_sha256({
        key: value for key, value in score.items() if key != "score_sha256"
    })
    score_path.write_text(json.dumps(score))

    with pytest.raises(ValueError, match="mechanical score|trusted|evidence"):
        runner.verify("smoke")


def test_verify_rederives_exact_unresolved_queue_fields(
        tmp_path, completed_unresolved_smoke, bank_data):
    root, runner = replay_copy(
        tmp_path, completed_unresolved_smoke, bank_data
    )
    queue_path = root / "judge_queue" / "smoke.jsonl"
    rows = read_jsonl(queue_path)
    rows[0]["judge_case_id"] = next(
        token for token in bank_data[2] if token != rows[0]["judge_case_id"]
    )
    rows[0]["raw_final_message_sha256"] = "0" * 64
    rows[0]["queue_sha256"] = contracts.canonical_sha256({
        key: value for key, value in rows[0].items() if key != "queue_sha256"
    })
    queue_path.write_text(json.dumps(rows[0]) + "\n")

    with pytest.raises(ValueError, match="judge queue|judge|raw"):
        runner.verify("smoke")


def test_verify_requires_queue_completeness_for_every_unresolved_stage(
        tmp_path, completed_unresolved_smoke, bank_data):
    root, runner = replay_copy(
        tmp_path, completed_unresolved_smoke, bank_data
    )
    (root / "judge_queue" / "smoke.jsonl").write_text("")

    with pytest.raises(ValueError, match="judge queue.*complete|queue accounting"):
        runner.verify("smoke")


def test_verify_rederives_exact_reliability_primary_link(
        tmp_path, completed_calibration_reliability, bank_data):
    root, runner = replay_copy(
        tmp_path, completed_calibration_reliability, bank_data
    )
    score_path = next((root / "scores" / "reliability").rglob("*.json"))
    score = read_json(score_path)
    score["reliability_primary_link"]["calibration_score_sha256"] = "0" * 64
    score["score_sha256"] = contracts.canonical_sha256({
        key: value for key, value in score.items() if key != "score_sha256"
    })
    score_path.write_text(json.dumps(score))

    with pytest.raises(ValueError, match="reliability|mechanical score"):
        runner.verify("reliability")


def test_standalone_reliability_verify_rejects_coordinated_calibration_poison(
        tmp_path, completed_calibration_reliability, bank_data):
    root, runner = replay_copy(
        tmp_path, completed_calibration_reliability, bank_data
    )
    reliability_path = next(
        (root / "scores" / "reliability").rglob("*.json")
    )
    reliability = read_json(reliability_path)
    link = reliability["reliability_primary_link"]
    calibration_path = (
        root / "scores" / "calibration"
        / link["calibration_occurrence_id"]
        / f"{reliability['logical_model_id']}.json"
    )
    calibration = read_json(calibration_path)
    calibration["label"] = 1 - calibration["label"]
    calibration["score_sha256"] = contracts.canonical_sha256({
        key: value for key, value in calibration.items()
        if key != "score_sha256"
    })
    calibration_path.write_text(json.dumps(calibration), encoding="utf-8")
    reliability["reliability_primary_link"][
        "calibration_score_sha256"
    ] = calibration["score_sha256"]
    reliability["score_sha256"] = contracts.canonical_sha256({
        key: value for key, value in reliability.items()
        if key != "score_sha256"
    })
    reliability_path.write_text(json.dumps(reliability), encoding="utf-8")

    with pytest.raises(ValueError, match="calibration|trusted|mechanical score"):
        runner.verify("reliability")


def test_verify_replays_provider_evidence_validation_for_every_artifact(
        tmp_path, completed_smoke, bank_data, monkeypatch):
    _root, runner = replay_copy(tmp_path, completed_smoke, bank_data)
    calls = []

    def validate(payload, *, episode, prior_artifacts):
        calls.append((payload["stage"], episode["id"], len(prior_artifacts)))

    monkeypatch.setattr(
        runner, "_validate_provider_evidence", validate, raising=False
    )
    runner.verify("smoke")
    assert len(calls) == 24 * 3 * 4


def test_openrouter_failure_attempt_provenance_is_preserved_not_relabelled(
        tmp_path, bank_data):
    runner = make_runner(
        tmp_path, bank_data, FakePanelDriver(bank_data[1]),
        provider="openrouter",
    )
    runner.run_mode = "live"
    runner.provenance = run_panel.LIVE_PROVENANCE["openrouter"]
    failure = {
        "failure_record_version": "charitroc-openrouter-failure-v1",
        "provenance": openrouter_driver.LIVE_ATTEMPT_PROVENANCE,
        "run_mode": "openrouter",
        "measurement_ready": False,
        "failure_kind": "invalid_utf8",
        "raw_bytes_base64": None,
        "raw_bytes_sha256": "0" * 64,
        "raw_byte_count": 1,
        "raw_redacted": True,
        "provider": "openrouter",
        "logical_model_id": manifest.MODEL_LOGICAL_IDS[0],
        "model": "fixture-model",
        "provider_model_id": "fixture-model",
        "configuration_id": "fixture-config",
        "request_sha256": "1" * 64,
        "transport_request_sha256": "2" * 64,
    }
    run = {
        "status": "failed",
        "provenance": failure["provenance"],
        "measurement_ready": False,
        "sessions": [{
            "integrity_session": 1,
            "execution_id": str(uuid.UUID(int=91, version=4)),
            "status": "failed",
            "requests": [],
            "results": [],
            "transport_descriptors": [],
            "attestations": [],
            "chain": None,
            "failure_record": failure,
        }],
        "failure_record": failure,
    }

    sessions = runner._normalize_run(run)
    assert sessions[0]["failure_record"] == failure
    assert sessions[0]["failure_record"]["provenance"] == (
        "live OpenRouter calibration attempt, NOT a measurement"
    )


@pytest.mark.parametrize("mutation", [
    "run_mode", "failure_kind", "hash_shape", "negative_count",
    "redaction_type",
])
def test_redacted_openrouter_failure_replay_validates_exact_failure_contract(
        tmp_path, bank_data, mutation):
    runner = make_runner(
        tmp_path, bank_data, FakePanelDriver(bank_data[1]),
        provider="openrouter",
    )
    runner.run_mode = "live"
    runner.provenance = run_panel.LIVE_PROVENANCE["openrouter"]
    plan = runner._plan("smoke")
    entry = plan["entries"][0]
    model = entry["model_execution_order"][0]
    provider_row = next(
        row for row in manifest.load_panel()["models"]
        if row["logical_model_id"] == model
    )["providers"]["openrouter"]
    execution_id = str(uuid.UUID(int=701, version=4))
    request = contracts.build_stage_request(
        runner._by_id[entry["item_id"]],
        execution_id=execution_id,
        provider="openrouter",
        logical_model_id=model,
        provider_model_id=provider_row["provider_model_id"],
        configuration_id=provider_row["configuration_id"],
        stage="stage_1",
        prior_responses={},
    )
    redacted = b"redacted-provider-bytes"
    failure = {
        "failure_record_version": openrouter_driver.FAILURE_RECORD_VERSION,
        "provenance": openrouter_driver.LIVE_ATTEMPT_PROVENANCE,
        "run_mode": "openrouter",
        "measurement_ready": False,
        "failure_kind": "credential_material",
        "raw_bytes_base64": None,
        "raw_bytes_sha256": hashlib.sha256(redacted).hexdigest(),
        "raw_byte_count": len(redacted),
        "raw_redacted": True,
        "provider": "openrouter",
        "logical_model_id": model,
        "model": provider_row["provider_model_id"],
        "provider_model_id": provider_row["provider_model_id"],
        "configuration_id": provider_row["configuration_id"],
        "request_sha256": request["request_sha256"],
        "transport_request_sha256": "2" * 64,
    }
    runner._persist_failure_record(
        "smoke", plan, entry, model, 1, 1, {
            "execution_id": execution_id,
            "requests": [request],
            "failure_record": failure,
        },
    )
    path = next((tmp_path / "failures" / "smoke").rglob("*.json"))
    payload = read_json(path)
    if mutation == "run_mode":
        payload["failure_record"]["run_mode"] = "mock"
    elif mutation == "failure_kind":
        payload["failure_record"]["failure_kind"] = "invented"
    elif mutation == "hash_shape":
        payload["failure_record"]["raw_bytes_sha256"] = "not-a-hash"
    elif mutation == "negative_count":
        payload["failure_record"]["raw_byte_count"] = -1
    else:
        payload["failure_record"]["raw_redacted"] = "yes"
    payload["failure_artifact_sha256"] = contracts.canonical_sha256({
        key: value for key, value in payload.items()
        if key != "failure_artifact_sha256"
    })
    path.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValueError, match="failure.*(record|raw|provenance)"):
        runner._collect_failures("smoke", plan)


def test_access_probe_is_one_nonbank_stage_per_exact_model(
        tmp_path, bank_data):
    driver = FakePanelDriver(bank_data[1])
    runner = make_runner(tmp_path, bank_data, driver)

    report = runner.access()

    assert report["provenance"] == "model access probe, NOT a measurement"
    assert report["measurement_ready"] is False
    assert report["models"] == list(manifest.MODEL_LOGICAL_IDS)
    assert all(
        probe["provenance"] == "model access probe, NOT a measurement"
        for probe in report["probes"]
    )
    assert driver.provider_stage_calls == ["stage_1"] * 3
    assert all(item_id.startswith("ACCESS-PROBE-")
               for item_id, _model, _provider in driver.calls)
    bank_turns = {
        text
        for episode in bank_data[0]
        for text in episode["multiturn_script"].values()
    }
    assert all(
        probe["request"]["current_visible_turn"]["content"] not in bank_turns
        for probe in report["probes"]
    )
    assert all(
        probe["probe_id"] not in driver.sidecar
        for probe in report["probes"]
    )
    assert runner.verify_access()["valid"] is True


def test_access_probe_persists_each_model_before_advancing_and_resumes(
        tmp_path, bank_data):
    first = FakePanelDriver(bank_data[1], crash_calls={2})
    runner = make_runner(tmp_path, bank_data, first)
    original_call = runner._call_driver

    def assert_sink_durable_before_unwind(episode, model, **kwargs):
        try:
            return original_call(episode, model, **kwargs)
        except run_panel._AccessProbeComplete:
            assert (tmp_path / "access" / "probes" / f"{model}.json").is_file()
            raise

    runner._call_driver = assert_sink_durable_before_unwind
    with pytest.raises(RuntimeError, match="simulated"):
        runner.access()

    probe_path = tmp_path / "access" / "probes" / "gpt-5.5.json"
    assert probe_path.is_file()
    first_hash = hashlib.sha256(probe_path.read_bytes()).hexdigest()

    resumed_driver = FakePanelDriver(bank_data[1])
    resumed = make_runner(tmp_path, bank_data, resumed_driver)
    report = resumed.access()
    assert [model for _item, model, _provider in resumed_driver.calls] == [
        "gpt-5.4", "gpt-5.4-mini",
    ]
    assert hashlib.sha256(probe_path.read_bytes()).hexdigest() == first_hash
    assert len(report["probes"]) == 3


def test_access_failure_is_durable_and_requires_explicit_retry(
        tmp_path, bank_data):
    driver = FakePanelDriver(
        bank_data[1], unresolved={(1, "stage_1")}
    )
    runner = make_runner(tmp_path, bank_data, driver)

    with pytest.raises(ValueError, match="durable access failure"):
        runner.access()

    failure_path = (
        tmp_path / "access" / "failures" / "gpt-5.5" / "attempt-01.json"
    )
    assert failure_path.is_file()
    failure = read_json(failure_path)
    assert failure["provenance"] == "model access probe, NOT a measurement"
    assert failure["failure_kind"] == "access_readiness_rejection"
    assert failure["probe"]["logical_model_id"] == "gpt-5.5"
    assert failure["probe"]["result"]["terminal_status"] == "unresolved"
    assert len(driver.calls) == 1

    with pytest.raises(ValueError, match="explicit access retry"):
        runner.access()
    assert len(driver.calls) == 1

    report = runner.access(retry_failed=True)
    assert [model for _item, model, _provider in driver.calls] == [
        "gpt-5.5", "gpt-5.5", "gpt-5.4", "gpt-5.4-mini",
    ]
    assert len(report["probes"]) == 3
    assert runner.verify_access()["valid"] is True

    failure_bytes = failure_path.read_bytes()
    failure_path.unlink()
    with pytest.raises(ValueError, match="access.*(journal|failure|history)"):
        runner.verify_access()
    failure_path.write_bytes(failure_bytes)

    failure["failure_kind"] = "provider_terminal_failure"
    failure_path.write_text(json.dumps(failure), encoding="utf-8")
    with pytest.raises(ValueError, match="durable access failure"):
        runner.verify_access()


def test_post_start_access_crash_requires_explicit_counted_retry(
        tmp_path, bank_data):
    first_driver = CrashAfterAccessStartDriver(bank_data[1])
    first = make_runner(tmp_path, bank_data, first_driver)

    with pytest.raises(RuntimeError, match="post-start"):
        first.access()
    journal = tmp_path / "access" / "attempt-journal.jsonl"
    assert journal.is_file()

    resumed_driver = FakePanelDriver(bank_data[1])
    resumed = make_runner(tmp_path, bank_data, resumed_driver)
    with pytest.raises(ValueError, match="explicit access retry"):
        resumed.access()
    assert resumed_driver.calls == []

    report = resumed.access(retry_failed=True)
    assert [model for _item, model, _provider in resumed_driver.calls] == [
        "gpt-5.5", "gpt-5.4", "gpt-5.4-mini",
    ]
    assert report["attempt_counts"] == {
        "gpt-5.5": 2, "gpt-5.4": 1, "gpt-5.4-mini": 1,
    }
    assert len(report["access_journal_sha256"]) == 64
    assert all(
        character in "0123456789abcdef"
        for character in report["access_journal_sha256"]
    )
    assert resumed.verify_access()["valid"] is True


def test_success_orphan_is_reconciled_without_repeating_provider_call(
        tmp_path, bank_data):
    first_driver = FakePanelDriver(bank_data[1])
    first = make_runner(tmp_path, bank_data, first_driver)
    append = first._append_access_journal
    crashed = []

    def crash_before_success_terminal(**kwargs):
        if kwargs["state"] == "succeeded" and not crashed:
            crashed.append(True)
            raise RuntimeError("simulated success terminal-journal crash")
        return append(**kwargs)

    first._append_access_journal = crash_before_success_terminal
    with pytest.raises(RuntimeError, match="success terminal-journal"):
        first.access()
    assert (tmp_path / "access" / "probes" / "gpt-5.5.json").is_file()

    resumed_driver = FakePanelDriver(bank_data[1])
    resumed = make_runner(tmp_path, bank_data, resumed_driver)
    report = resumed.access()
    assert [model for _item, model, _provider in resumed_driver.calls] == [
        "gpt-5.4", "gpt-5.4-mini",
    ]
    assert report["attempt_counts"]["gpt-5.5"] == 1
    assert resumed.verify_access()["valid"] is True


def test_failure_orphan_is_reconciled_then_requires_explicit_retry(
        tmp_path, bank_data):
    first_driver = FakePanelDriver(
        bank_data[1], unresolved={(1, "stage_1")}
    )
    first = make_runner(tmp_path, bank_data, first_driver)
    append = first._append_access_journal
    crashed = []

    def crash_before_failure_terminal(**kwargs):
        if kwargs["state"] == "failed" and not crashed:
            crashed.append(True)
            raise RuntimeError("simulated failure terminal-journal crash")
        return append(**kwargs)

    first._append_access_journal = crash_before_failure_terminal
    with pytest.raises(RuntimeError, match="failure terminal-journal"):
        first.access()
    assert (
        tmp_path / "access" / "failures" / "gpt-5.5" / "attempt-01.json"
    ).is_file()

    resumed_driver = FakePanelDriver(bank_data[1])
    resumed = make_runner(tmp_path, bank_data, resumed_driver)
    with pytest.raises(ValueError, match="explicit access retry"):
        resumed.access()
    assert resumed_driver.calls == []
    report = resumed.access(retry_failed=True)
    assert report["attempt_counts"]["gpt-5.5"] == 2
    assert resumed.verify_access()["valid"] is True


@pytest.mark.parametrize("mutation", ["returned_identity", "descriptor"])
def test_access_probe_replays_provider_evidence_and_requires_complete_identity(
        tmp_path, bank_data, mutation):
    runner = make_runner(
        tmp_path, bank_data, FakePanelDriver(bank_data[1])
    )
    runner.access()
    path = tmp_path / "access" / "report.json"
    report = read_json(path)
    probe = report["probes"][0]
    request = probe["request"]
    old = probe["result"]
    descriptor = deepcopy(probe["transport_descriptor"])
    returned_model = old["returned_provider_model_id"]
    if mutation == "returned_identity":
        returned_model = "openai/gpt-5.4"
    else:
        descriptor["fixture"] = False
        probe["transport_descriptor"] = descriptor
    probe["result"] = contracts.build_stage_result(
        request,
        run_mode="mock",
        returned_provider_model_id=returned_model,
        returned_provider_name=old["returned_provider_name"],
        session_id=old["session_id"],
        transport_request_sha256=contracts.canonical_sha256(descriptor),
        attempts=old["attempts"],
        tool_events=old["tool_events"],
        session_chain_ok=old["integrity"]["session_chain_ok"],
        isolation_ok=old["integrity"]["isolation_ok"],
        future_text_absent=old["integrity"]["future_text_absent"],
    )
    report["access_sha256"] = contracts.canonical_sha256({
        key: value for key, value in report.items()
        if key != "access_sha256"
    })
    path.write_text(json.dumps(report), encoding="utf-8")

    with pytest.raises(
            ValueError,
            match=(
                "access.*(identity|evidence|provider|complete|durable)|"
                "provider.*evidence|durable probe"
            )):
        runner.verify_access()


def test_output_root_and_artifact_paths_reject_symlinks_and_traversal(
        tmp_path, bank_data):
    real = tmp_path / "real"
    real.mkdir()
    alias = tmp_path / "alias"
    alias.symlink_to(real, target_is_directory=True)
    with pytest.raises(ValueError, match="symlink"):
        make_runner(alias, bank_data, FakePanelDriver(bank_data[1]))

    runner = make_runner(
        tmp_path / "safe", bank_data, FakePanelDriver(bank_data[1])
    )
    with pytest.raises(ValueError, match="traversal|confined|absolute"):
        runner._out_path("..", "outside.json")
    outside = tmp_path / "outside"
    outside.mkdir()
    (runner.out_dir / "linked").symlink_to(outside, target_is_directory=True)
    with pytest.raises(ValueError, match="symlink|confined"):
        runner._out_path("linked", "artifact.json")


def test_timestamp_replay_rejects_internal_jsonl_symlink(
        tmp_path, bank_data):
    out = tmp_path / "run"
    state = out / "state"
    state.mkdir(parents=True)
    outside = tmp_path / "outside.jsonl"
    outside.write_text(
        json.dumps({"timestamp_utc": "2026-07-10T12:00:00Z"}) + "\n",
        encoding="utf-8",
    )
    (state / "smoke.jsonl").symlink_to(outside)

    with pytest.raises(ValueError, match="symlink|confined"):
        make_runner(out, bank_data, FakePanelDriver(bank_data[1]))


def test_explicit_analysis_provenance_requires_exact_row_provenance():
    live = run_panel.LIVE_PROVENANCE["openrouter"]
    rows = [
        {
            "item_family": "fixture",
            "label": label,
            "stage4_score": score,
            "pair_id": "pair-1",
            "base_rate_benign": 0.5,
        }
        for label, score in ((0, 0), (1, 4))
    ]
    with pytest.raises(ValueError, match="row provenance"):
        bank_analysis.analyze_model(
            rows, bootstrap_draws=100, provenance=live
        )
    for row in rows:
        row["provenance"] = live
    rows[1]["provenance"] = MOCK_PROVENANCE
    with pytest.raises(ValueError, match="row provenance"):
        bank_analysis.analyze_model(
            rows, bootstrap_draws=100, provenance=live
        )
    rows[1]["provenance"] = live
    assert bank_analysis.analyze_model(
        rows, bootstrap_draws=100, provenance=live
    )["provenance"] == live


def test_explicit_mock_analysis_also_requires_exact_row_provenance():
    rows = [{
        "item_family": "fixture",
        "label": label,
        "stage4_score": score,
        "pair_id": "pair-1",
        "base_rate_benign": 0.5,
    } for label, score in ((0, 0), (1, 4))]
    with pytest.raises(ValueError, match="row provenance"):
        bank_analysis.analyze_model(
            rows,
            bootstrap_draws=100,
            provenance=MOCK_PROVENANCE,
        )
    with pytest.raises(ValueError, match="row provenance"):
        bank_analysis.aggregate_stage3([{
            "update_correct": True,
            "cue_variant": "strong",
        }], provenance=MOCK_PROVENANCE)


def test_private_analysis_freezes_inputs_and_extension_activation_once(
        tmp_path, bank_data, monkeypatch):
    freeze = FreezeHarness()
    runner = make_runner(
        tmp_path, bank_data, FakePanelDriver(bank_data[1]),
        freeze_builder=freeze.build,
        private_validator=freeze.validate,
    )
    runner.freeze()
    protocol = read_json(tmp_path / "private-protocol-freeze.json")
    private_plan = runner._plan("private")
    inputs = {
        "episodes_per_model": 96,
        "extension_already_used": False,
        "criteria": [{
            "criterion_id": "auc-primary-range",
            "estimate": 0.055,
            "ci95": [0.04, 0.07],
            "threshold": 0.05,
            "direction": "at_least",
            "frozen": True,
        }],
        "model_auc_bootstrap_inputs": {
            model: {"draws": 100, "score_sha256s": []}
            for model in manifest.MODEL_LOGICAL_IDS
        },
        "freeze_hash": read_json(tmp_path / "freeze.json")["freeze_hash"],
        "private_protocol_freeze_sha256": protocol[
            "protocol_freeze_sha256"
        ],
        "calibration_analysis_file_sha256": protocol[
            "calibration_analysis_file_sha256"
        ],
        "private_plan_hash": private_plan["plan_hash"],
        "extension_entries_sha256": contracts.canonical_sha256(
            private_plan["extension_entries"]
        ),
    }
    monkeypatch.setattr(
        runner, "_private_confirmation_inputs",
        lambda **_kwargs: deepcopy(inputs),
        raising=False,
    )
    monkeypatch.setattr(
        runner,
        "_verify_private_namespaces",
        lambda: {"private": {"valid": True}},
        raising=False,
    )

    report = runner.analyze_private()
    assert report["private_confirmation"]["action"] == "extend_to_192"
    assert report["frozen_inputs"] == inputs
    activation = runner.activate_private_extension()
    assert activation["analysis_sha256"] == report["analysis_sha256"]
    plan = runner._plan("private")
    assert runner._execution_entries("private-extension", plan) == plan[
        "extension_entries"
    ]
    extension_driver = FakePanelDriver(bank_data[1], crash_calls={2})
    extension_runner = make_runner(
        tmp_path, bank_data, extension_driver,
        freeze_builder=freeze.build,
        private_validator=freeze.validate,
    )
    with pytest.raises(RuntimeError, match="simulated"):
        extension_runner.execute("private-extension")
    extension_state = read_jsonl(
        tmp_path / "state" / "private-extension.jsonl"
    )
    assert extension_state[0]["plan_occurrence_id"] == (
        "private-extension-001"
    )
    assert not (tmp_path / "state" / "private.jsonl").exists()
    with pytest.raises(ValueError, match="already.*activated|one-time"):
        runner.activate_private_extension()


def test_private_analysis_verifies_scores_and_keeps_distinct_96_192_reports(
        tmp_path, bank_data, monkeypatch):
    freeze = FreezeHarness()
    runner = make_runner(
        tmp_path, bank_data, FakePanelDriver(bank_data[1]),
        freeze_builder=freeze.build,
        private_validator=freeze.validate,
    )
    runner.freeze()
    verify_calls = []

    def verify(stage):
        verify_calls.append(stage)
        return {"valid": True, "stage": stage}

    def rows(namespace):
        offset = 0 if namespace == "private" else 10000
        return [
            {
                "logical_model_id": model,
                "label": index % 2,
                "stage4_score": 4 if index % 2 else 0,
                "pair_id": f"{namespace}-{index // 2:03d}",
                "score_sha256": f"{offset + model_index * 1000 + index:064x}",
            }
            for model_index, model in enumerate(manifest.MODEL_LOGICAL_IDS)
            for index in range(96)
        ]

    monkeypatch.setattr(runner, "verify", verify)
    monkeypatch.setattr(runner, "_score_rows", rows)
    monkeypatch.setattr(
        bank_analysis.roc,
        "clustered_bootstrap_auc",
        lambda *_args, **_kwargs: {
            "auc": 0.55,
            "ci95": [0.50, 0.60],
            "se": 0.02,
        },
    )

    primary = runner.analyze_private()
    assert primary["frozen_inputs"]["episodes_per_model"] == 96
    assert verify_calls == ["private"]
    assert (tmp_path / "reports" / "private-analysis-96.json").is_file()
    activation = runner.activate_private_extension()
    assert activation["analysis_sha256"] == primary["analysis_sha256"]

    final = runner.analyze_private()
    assert final["frozen_inputs"]["episodes_per_model"] == 192
    assert verify_calls[-2:] == ["private", "private-extension"]
    assert (tmp_path / "reports" / "private-analysis-96.json").is_file()
    assert (tmp_path / "reports" / "private-analysis-192.json").is_file()


def test_forged_self_hashed_private_report_cannot_activate_extension(
        tmp_path, bank_data, monkeypatch):
    freeze = FreezeHarness()
    runner = make_runner(
        tmp_path, bank_data, FakePanelDriver(bank_data[1]),
        freeze_builder=freeze.build,
        private_validator=freeze.validate,
    )
    runner.freeze()
    forged_inputs = {
        "episodes_per_model": 96,
        "extension_already_used": False,
        "criteria": [{
            "criterion_id": "forged",
            "estimate": 0.55,
            "ci95": [0.50, 0.60],
            "threshold": 0.55,
            "direction": "at_least",
            "frozen": True,
        }],
        "model_auc_bootstrap_inputs": {},
        "freeze_hash": read_json(tmp_path / "freeze.json")["freeze_hash"],
    }
    forged = {
        "private_analysis_version": "charitroc-private-analysis-v1",
        "provenance": MOCK_PROVENANCE,
        "provider": "codex",
        "measurement_surface": "sealed-private-confirmation",
        "frozen_inputs": forged_inputs,
        "private_confirmation": run_panel.gates.evaluate_private_confirmation(
            forged_inputs["criteria"], 96, False
        ),
    }
    forged["analysis_sha256"] = contracts.canonical_sha256(forged)
    run_panel._write_new_json(
        tmp_path / "reports" / "private-analysis-96.json", forged
    )
    genuine_inputs = deepcopy(forged_inputs)
    genuine_inputs["criteria"] = [{
        "criterion_id": "genuine",
        "estimate": 0.70,
        "ci95": [0.60, 0.80],
        "threshold": 0.55,
        "direction": "at_least",
        "frozen": True,
    }]
    monkeypatch.setattr(
        runner,
        "_verify_private_namespaces",
        lambda: {"private": {"valid": True}},
        raising=False,
    )
    monkeypatch.setattr(
        runner,
        "_private_confirmation_inputs",
        lambda **_kwargs: deepcopy(genuine_inputs),
    )

    with pytest.raises(ValueError, match="differs|authorize|trusted|verified"):
        runner.activate_private_extension()
