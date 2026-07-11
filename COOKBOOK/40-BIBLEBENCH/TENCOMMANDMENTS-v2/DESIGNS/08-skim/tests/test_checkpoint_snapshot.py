"""Fail-closed reporting for a preserved provider-limited diagnostic."""

import importlib
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tarfile

import pytest


ROOT = Path(__file__).resolve().parents[1]
BENCH_ROOT = ROOT.parents[2]
SMOKE_DIR = ROOT / "pilots" / "20260711-cheap-openrouter-smoke-r2"
FULL_R1_DIR = ROOT / "pilots" / "20260711-cheap-openrouter-full-r1"
for search_root in (ROOT, BENCH_ROOT):
    if str(search_root) not in sys.path:
        sys.path.insert(0, str(search_root))


def _modules():
    return (
        importlib.import_module("analysis.checkpoint_snapshot"),
        importlib.import_module("harness.run_openrouter_diagnostic"),
    )


def _partial_output(tmp_path):
    snapshot, runner = _modules()
    config, _digest = runner.load_frozen_diagnostic_config()
    clients = tuple(runner._StaticIdentityClient(row, config) for row in config["model_roster"])
    plan = runner.preflight_diagnostic(clients=clients, smoke_dir=SMOKE_DIR)
    output_dir = tmp_path / "partial"
    (output_dir / "checkpoints").mkdir(parents=True)
    (output_dir / "events").mkdir()
    schedule_row = plan.schedule[0]
    episode = {
        "call_metadata": [],
        "cost_accounting_status": "RETURNED_COST_EXACT",
        "cost_usd": 0.0,
        "event_count": 0,
        "event_log": None,
        "failure_code": "MODEL_CALL_ABORTED_NO_AUTOMATIC_RETRY",
        "failure_type": "OpenRouterTransportError",
        "model_family": config["model_roster"][0]["family"],
        "model_id": schedule_row["model_id"],
        "paid_calls": 1,
        "request_id": schedule_row["runtime_request_id"],
        "schedule_index": schedule_row["schedule_index"],
        "seed": schedule_row["seed"],
        "status": "PARKED_MODEL_CALL_ABORT",
        "syntax_repair_used": False,
        "vendor": config["model_roster"][0]["vendor"],
    }
    runner._append_checkpoint(
        output_dir / "checkpoints" / "model-0.jsonl", episode, runner._ZERO_HASH
    )
    return snapshot, runner, plan, output_dir


def test_snapshot_binds_checkpoint_chain_and_reports_remaining_schedule(tmp_path):
    snapshot, _runner, plan, output_dir = _partial_output(tmp_path)

    result = snapshot.build_snapshot(
        plan,
        output_dir,
        closure_reason="REPEATED_PROVIDER_HTTP_429",
    )

    assert result["status"] == "CHEAP_DIAGNOSTIC_PROVIDER_LIMITED_RESUMABLE"
    assert result["eligible_for_empirical_decision"] is False
    assert result["complete"] is False
    assert result["scheduled_requests"] == 2400
    assert result["checkpointed_episodes"] == 1
    assert result["remaining_requests"] == 2399
    assert result["valid_terminal_episodes"] == 0
    assert result["parked_episodes"] == 1
    assert result["blockers"][-1] == "PROVIDER_RATE_LIMIT"
    assert result["streams"][0]["chain_head_sha256"]
    assert result["streams"][0]["next_schedule_index"] == 1
    assert result["streams"][1]["next_schedule_index"] == 800
    assert result["config_sha256"] == plan.config_sha256


def test_snapshot_rejects_checkpoint_tamper(tmp_path):
    snapshot, _runner, plan, output_dir = _partial_output(tmp_path)
    checkpoint = output_dir / "checkpoints" / "model-0.jsonl"
    row = json.loads(checkpoint.read_text())
    row["episode"]["cost_usd"] = 0.5
    checkpoint.write_text(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")

    with pytest.raises(ValueError, match="checkpoint|chain"):
        snapshot.build_snapshot(
            plan,
            output_dir,
            closure_reason="REPEATED_PROVIDER_HTTP_429",
        )


def test_snapshot_refuses_complete_schedule(tmp_path, monkeypatch):
    snapshot, _runner, plan, output_dir = _partial_output(tmp_path)
    monkeypatch.setattr(snapshot, "_validated_episodes", lambda *_args: tuple({
        "status": "VALID_TERMINAL",
        "paid_calls": 1,
        "cost_usd": 0.0,
        "schedule_index": index,
        "model_id": plan.schedule[index]["model_id"],
    } for index in range(len(plan.schedule))))

    with pytest.raises(ValueError, match="complete"):
        snapshot.build_snapshot(
            plan,
            output_dir,
            closure_reason="REPEATED_PROVIDER_HTTP_429",
        )


def test_snapshot_script_is_directly_executable_from_benchmark_root():
    script = ROOT / "analysis" / "checkpoint_snapshot.py"
    completed = subprocess.run(
        [sys.executable, str(script), "--help"],
        cwd=BENCH_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 0, completed.stderr
    assert "--output-dir" in completed.stdout


def test_committed_evidence_archive_preserves_required_event_locks():
    manifest = json.loads((FULL_R1_DIR / "evidence-manifest.json").read_text())
    archive_path = FULL_R1_DIR / manifest["archive_file"]
    raw = archive_path.read_bytes()

    assert hashlib.sha256(raw).hexdigest() == manifest["archive_sha256"]
    assert len(raw) == manifest["archive_size_bytes"]
    with tarfile.open(archive_path, "r:gz") as archive:
        members = {member.name: member for member in archive.getmembers()}
        event_names = {
            name for name in members if name.startswith("events/episode-") and name.endswith(".jsonl")
        }
        lock_names = {
            name for name in members if name.startswith("events/.episode-") and name.endswith(".jsonl.lock")
        }
        assert len(event_names) == len(lock_names) == manifest["event_lock_files"]
        assert all(
            "events/." + name.removeprefix("events/") + ".lock" in lock_names
            for name in event_names
        )
        assert all(members[name].size == 0 for name in lock_names)
        for name, digest_field in (
            ("provider-limited-result.json", "provider_limited_result_sha256"),
            (
                "transport-repair-attestation.json",
                "transport_repair_attestation_sha256",
            ),
        ):
            stream = archive.extractfile(members[name])
            assert stream is not None
            assert hashlib.sha256(stream.read()).hexdigest() == manifest[digest_field]
