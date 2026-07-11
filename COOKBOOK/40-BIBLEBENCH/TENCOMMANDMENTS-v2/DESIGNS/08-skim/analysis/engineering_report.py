"""Build a deterministic, explicitly ineligible SKIM engineering report."""

from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple


VALID_STATUSES = frozenset({"VALID_TERMINAL", "VALID_TERMINAL_AFTER_REPAIR"})


def canonical_bytes(payload: Any) -> bytes:
    """Return the repository's canonical UTF-8 JSON representation."""

    return (
        json.dumps(
            payload,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
        + "\n"
    ).encode("utf-8")


def _load_canonical(path: Path) -> tuple[Mapping[str, Any], bytes]:
    raw = Path(path).read_bytes()
    try:
        payload = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        raise ValueError("diagnostic result must be valid UTF-8 JSON") from None
    if not isinstance(payload, dict):
        raise ValueError("diagnostic result root must be an object")
    if raw != canonical_bytes(payload):
        raise ValueError("diagnostic result must be canonical JSON")
    return payload, raw


def _bounded_count(payload: Mapping[str, Any], name: str) -> int:
    value = payload.get(name)
    if type(value) is not int or value < 0:
        raise ValueError("%s must be a nonnegative integer" % name)
    return value


def _finite_cost(payload: Mapping[str, Any], name: str) -> float:
    value = payload.get(name)
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(float(value))
        or float(value) < 0
    ):
        raise ValueError("%s must be a finite nonnegative number" % name)
    return float(value)


def build_report(result_path: Path) -> Dict[str, Any]:
    """Validate a complete cheap diagnostic and summarize it by model."""

    payload, raw = _load_canonical(Path(result_path))
    if payload.get("study_id") != "SKIM-P1":
        raise ValueError("diagnostic result study identity is invalid")
    if payload.get("data_basis") != "external_model_responses":
        raise ValueError("diagnostic result data basis is invalid")
    if payload.get("eligible_for_empirical_decision") is not False:
        raise ValueError("engineering diagnostic must remain empirically ineligible")
    status = payload.get("status")
    if not isinstance(status, str) or not status.endswith("_COMPLETE"):
        raise ValueError("diagnostic result status is not complete")

    scheduled = _bounded_count(payload, "scheduled_requests")
    completed = _bounded_count(payload, "completed_episodes")
    valid = _bounded_count(payload, "valid_terminal_episodes")
    parked = _bounded_count(payload, "parked_episodes")
    paid_calls = _bounded_count(payload, "paid_calls")
    total_cost = _finite_cost(payload, "total_cost_usd")
    cost_cap = _finite_cost(payload, "cost_cap_usd")
    preflight_cost = _finite_cost(payload, "preflight_cost_upper_bound_usd")
    if completed != scheduled or valid + parked != completed:
        raise ValueError("diagnostic result does not cover the complete schedule")
    if total_cost > cost_cap:
        raise ValueError("diagnostic result exceeds its cost cap")

    episodes = payload.get("episodes")
    if not isinstance(episodes, list) or len(episodes) != completed:
        raise ValueError("diagnostic episodes do not match the complete schedule")
    indices = []
    grouped: Dict[Tuple[str, str, str], List[Mapping[str, Any]]] = defaultdict(list)
    for episode in episodes:
        if not isinstance(episode, dict):
            raise ValueError("each diagnostic episode must be an object")
        index = episode.get("schedule_index")
        if type(index) is not int or not 0 <= index < scheduled:
            raise ValueError("diagnostic schedule index is invalid")
        indices.append(index)
        identity = tuple(episode.get(field) for field in ("model_id", "vendor", "provider"))
        if any(not isinstance(value, str) or not value for value in identity):
            raise ValueError("diagnostic model/provider identity is invalid")
        _bounded_count(episode, "paid_calls")
        _finite_cost(episode, "cost_usd")
        grouped[identity].append(episode)
    if set(indices) != set(range(scheduled)) or len(indices) != len(set(indices)):
        raise ValueError("diagnostic schedule coverage is not exact")
    if sum(_bounded_count(row, "paid_calls") for row in episodes) != paid_calls:
        raise ValueError("diagnostic paid-call total does not replay")
    replayed_cost = math.fsum(_finite_cost(row, "cost_usd") for row in episodes)
    if not math.isclose(replayed_cost, total_cost, rel_tol=0.0, abs_tol=1e-12):
        raise ValueError("diagnostic cost total does not replay")

    models = []
    replayed_valid = 0
    for (model_id, vendor, provider), rows in sorted(grouped.items()):
        model_valid = sum(row.get("status") in VALID_STATUSES for row in rows)
        replayed_valid += model_valid
        models.append(
            {
                "model_id": model_id,
                "vendor": vendor,
                "provider": provider,
                "completed_episodes": len(rows),
                "valid_terminal_episodes": model_valid,
                "parked_episodes": len(rows) - model_valid,
                "paid_calls": sum(_bounded_count(row, "paid_calls") for row in rows),
                "total_cost_usd": math.fsum(
                    _finite_cost(row, "cost_usd") for row in rows
                ),
            }
        )
    if replayed_valid != valid:
        raise ValueError("diagnostic valid/parked totals do not replay")

    blockers = payload.get("blockers")
    if not isinstance(blockers, list) or any(
        not isinstance(blocker, str) or not blocker for blocker in blockers
    ):
        raise ValueError("diagnostic blockers must be a list of strings")
    return {
        "schema_version": 1,
        "study_id": "SKIM-P1",
        "run_id": payload.get("run_id"),
        "status": "ENGINEERING_DIAGNOSTIC_REPORTED",
        "eligible_for_empirical_decision": False,
        "official_scale_status": "NOT_RUN",
        "source_result_sha256": hashlib.sha256(raw).hexdigest(),
        "config_sha256": payload.get("config_sha256"),
        "smoke_result_sha256": payload.get("smoke_result_sha256"),
        "artifact_sha256": payload.get("artifact_sha256"),
        "seed": payload.get("seed"),
        "schedule": {
            "scheduled_requests": scheduled,
            "completed_episodes": completed,
            "valid_terminal_episodes": valid,
            "parked_episodes": parked,
        },
        "cost": {
            "paid_calls": paid_calls,
            "total_cost_usd": total_cost,
            "cost_cap_usd": cost_cap,
            "preflight_cost_upper_bound_usd": preflight_cost,
        },
        "models": models,
        "blockers": list(blockers),
        "resume_provenance": payload.get("resume_provenance"),
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--result", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    return parser


def cli(argv: Optional[Sequence[str]] = None) -> int:
    args = _parser().parse_args(argv)
    report = build_report(args.result)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("xb") as handle:
        handle.write(canonical_bytes(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(cli())
