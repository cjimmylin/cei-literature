"""Freeze an explicitly incomplete, resumable SKIM provider-limit snapshot."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
from typing import Any, Dict, Mapping, Optional, Sequence, Tuple


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
BENCH_ROOT = ROOT.parents[2]
for search_root in (ROOT, BENCH_ROOT):
    if str(search_root) not in sys.path:
        sys.path.insert(0, str(search_root))

from harness import run_openrouter_diagnostic as diagnostic


STATUS = "CHEAP_DIAGNOSTIC_PROVIDER_LIMITED_RESUMABLE"
CLOSURE_REASON = "REPEATED_PROVIDER_HTTP_429"
VALID_STATUSES = frozenset({"VALID_TERMINAL", "VALID_TERMINAL_AFTER_REPAIR"})


def _canonical_bytes(payload: Any) -> bytes:
    return (diagnostic.canonical_json(payload) + "\n").encode("utf-8")


def _validated_episodes(
    plan: diagnostic.DiagnosticPlan,
    output_dir: Path,
) -> Tuple[Mapping[str, Any], ...]:
    output_dir = Path(output_dir)
    if not output_dir.is_dir():
        raise ValueError("provider-limited output directory does not exist")
    if not (output_dir / "checkpoints").is_dir() or not (
        output_dir / "events"
    ).is_dir():
        raise ValueError("provider-limited output directory is incomplete")
    scorer = diagnostic._mechanical_scorer()
    if scorer is None:
        raise RuntimeError("mechanical scorer is required for checkpoint validation")
    episodes = []
    model_ids = tuple(row["model_id"] for row in plan.config["model_roster"])
    for model_index, model_id in enumerate(model_ids):
        group = tuple(row for row in plan.schedule if row["model_id"] == model_id)
        episodes.extend(
            diagnostic._load_checkpoints(
                diagnostic._checkpoint_path(output_dir, model_index),
                group,
                plan,
                scorer,
            )
        )
    expected_events = {
        Path(episode["event_log"]).name
        for episode in episodes
        if episode.get("status") in VALID_STATUSES
    }
    actual_events = {path.name for path in (output_dir / "events").glob("episode-*.jsonl")}
    if actual_events != expected_events:
        raise ValueError("diagnostic event set does not match checkpoint chains")
    return tuple(sorted(episodes, key=lambda row: row["schedule_index"]))


def _stream_summaries(
    plan: diagnostic.DiagnosticPlan,
    output_dir: Path,
    episodes: Sequence[Mapping[str, Any]],
) -> Sequence[Mapping[str, Any]]:
    summaries = []
    for model_index, roster_row in enumerate(plan.config["model_roster"]):
        model_id = roster_row["model_id"]
        group = tuple(row for row in plan.schedule if row["model_id"] == model_id)
        completed = tuple(row for row in episodes if row["model_id"] == model_id)
        path = diagnostic._checkpoint_path(output_dir, model_index)
        raw = path.read_bytes() if path.exists() else b""
        if completed:
            last = diagnostic._decode_exact_json(
                raw[:-1].split(b"\n")[-1], "diagnostic checkpoint row"
            )
            chain_head = last["checkpoint_sha256"]
        else:
            chain_head = diagnostic._ZERO_HASH
        next_index = (
            group[len(completed)]["schedule_index"]
            if len(completed) < len(group)
            else None
        )
        valid = sum(row["status"] in VALID_STATUSES for row in completed)
        summaries.append(
            {
                "model_id": model_id,
                "vendor": roster_row["vendor"],
                "provider": roster_row["provider"],
                "checkpoint_path": "checkpoints/model-%d.jsonl" % model_index,
                "checkpoint_bytes": len(raw),
                "checkpoint_file_sha256": (
                    hashlib.sha256(raw).hexdigest() if raw else None
                ),
                "chain_head_sha256": chain_head,
                "checkpointed_episodes": len(completed),
                "valid_terminal_episodes": valid,
                "parked_episodes": len(completed) - valid,
                "paid_calls": sum(row["paid_calls"] for row in completed),
                "total_cost_usd": math.fsum(
                    float(row["cost_usd"]) for row in completed
                ),
                "next_schedule_index": next_index,
            }
        )
    return summaries


def build_snapshot(
    plan: diagnostic.DiagnosticPlan,
    output_dir: Path,
    *,
    closure_reason: str,
) -> Dict[str, Any]:
    """Validate all preserved evidence and summarize an unfinished schedule."""

    if closure_reason != CLOSURE_REASON:
        raise ValueError("provider-limit closure reason is not registered")
    output_dir = Path(output_dir)
    episodes = _validated_episodes(plan, output_dir)
    if len(episodes) >= len(plan.schedule):
        raise ValueError("a complete diagnostic must use diagnostic-result.json")
    if not episodes:
        raise ValueError("provider-limit snapshot requires preserved checkpoints")
    streams = list(_stream_summaries(plan, output_dir, episodes))
    valid = sum(row["status"] in VALID_STATUSES for row in episodes)
    blockers = list(plan.config["blockers"])
    if "PROVIDER_RATE_LIMIT" not in blockers:
        blockers.append("PROVIDER_RATE_LIMIT")
    attestation_path = output_dir / diagnostic.TRANSPORT_REPAIR_ATTESTATION_NAME
    attestation_sha256 = (
        diagnostic._validate_transport_repair_attestation(output_dir, plan)
        if attestation_path.is_file()
        else None
    )
    failure_path = output_dir / "diagnostic-failure.json"
    failure_sha256 = (
        hashlib.sha256(failure_path.read_bytes()).hexdigest()
        if failure_path.is_file()
        else None
    )
    return {
        "schema_version": 1,
        "study_id": "SKIM-P1",
        "run_id": plan.config["run_id"],
        "status": STATUS,
        "complete": False,
        "resumable": True,
        "data_basis": "external_model_responses",
        "eligible_for_empirical_decision": False,
        "official_scale_status": "NOT_RUN",
        "closure_reason": closure_reason,
        "observed_http_status": 429,
        "scheduled_requests": len(plan.schedule),
        "checkpointed_episodes": len(episodes),
        "remaining_requests": len(plan.schedule) - len(episodes),
        "valid_terminal_episodes": valid,
        "parked_episodes": len(episodes) - valid,
        "paid_calls": sum(row["paid_calls"] for row in episodes),
        "total_cost_usd": math.fsum(float(row["cost_usd"]) for row in episodes),
        "cost_cap_usd": plan.cost_cap_usd,
        "preflight_cost_upper_bound_usd": plan.preflight_cost_upper_bound_usd,
        "config_sha256": plan.config_sha256,
        "smoke_result_sha256": plan.smoke_result_sha256,
        "artifact_sha256": dict(plan.artifact_sha256),
        "transport_repair_attestation_sha256": attestation_sha256,
        "historical_first_abort_artifact_sha256": failure_sha256,
        "streams": streams,
        "checkpoint_manifest_sha256": hashlib.sha256(
            diagnostic.canonical_json(streams).encode("utf-8")
        ).hexdigest(),
        "blockers": blockers,
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--smoke-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument(
        "--closure-reason", default=CLOSURE_REASON, choices=(CLOSURE_REASON,)
    )
    parser.add_argument(
        "--output-name", default="provider-limited-result.json"
    )
    return parser


def cli(argv: Optional[Sequence[str]] = None) -> int:
    args = _parser().parse_args(argv)
    if Path(args.output_name).name != args.output_name or not args.output_name.endswith(
        ".json"
    ):
        raise ValueError("output name must be a local JSON filename")
    config, _digest = diagnostic.load_frozen_diagnostic_config()
    clients = tuple(
        diagnostic._StaticIdentityClient(row, config)
        for row in config["model_roster"]
    )
    plan = diagnostic.preflight_diagnostic(clients=clients, smoke_dir=args.smoke_dir)
    result = build_snapshot(
        plan,
        args.output_dir,
        closure_reason=args.closure_reason,
    )
    output_path = args.output_dir / args.output_name
    with output_path.open("xb") as handle:
        handle.write(_canonical_bytes(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(cli())
