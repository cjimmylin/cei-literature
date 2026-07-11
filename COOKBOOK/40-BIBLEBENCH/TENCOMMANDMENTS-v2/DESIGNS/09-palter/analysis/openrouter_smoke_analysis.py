"""Fail-closed aggregate analysis for a completed PALTER OpenRouter smoke."""

import argparse
from collections import Counter, defaultdict
import hashlib
import json
import os
from pathlib import Path
import sys
from typing import Any, Dict, Mapping, Tuple

PALTER_ROOT = Path(__file__).resolve().parents[1]
BIBLEBENCH_ROOT = Path(__file__).resolve().parents[4]
for root in (PALTER_ROOT, BIBLEBENCH_ROOT):
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

from harness import palter_openrouter as transport  # noqa: E402
from scoring.mechanical import score_composition  # noqa: E402
from TENCOMMANDMENTS.harness.openrouter import (  # noqa: E402
    canonical_json,
    load_checkpoint_stream,
)


ACCEPTED_STATUSES = frozenset({"ACCEPTED", "ACCEPTED_REPAIR"})
COMPOSITION_TYPES = frozenset(
    {"composition", "no_incentive_twin", "monitoring_twin"}
)


def _load_completed_state(
    plan: transport.RunPlan,
    output_dir: Path,
) -> Tuple[Dict[str, Any], Mapping[str, Mapping[str, Any]], str]:
    output = Path(output_dir)
    result_path = output / "smoke-result.json"
    checkpoint_path = output / "calls.jsonl"
    try:
        result = json.loads(result_path.read_text())
    except (OSError, UnicodeError, ValueError) as exc:
        raise ValueError("completed smoke result is missing or invalid") from exc
    if (
        type(result) is not dict
        or result.get("status") != "CHEAP_MODEL_ENGINEERING_SMOKE_COMPLETE"
        or result.get("config_sha256") != plan.config_sha256
        or result.get("run_id") != plan.config["run_id"]
        or result.get("accounted_semantic_calls") != len(plan.schedule)
    ):
        raise ValueError("smoke result does not match the frozen completed plan")
    snapshot = load_checkpoint_stream(checkpoint_path, plan.config["run_id"])
    if (
        snapshot.head_sha256 != result.get("checkpoint_head_sha256")
        or len(snapshot.records) != result.get("checkpoint_records")
    ):
        raise ValueError("smoke result is not bound to the checkpoint stream")
    by_id = {call.semantic_call_id: call for call in plan.schedule}
    terminal = {}
    for payload in snapshot.payloads:
        transport._validate_prior_payload(plan, by_id, payload)
        previous = terminal.get(payload["semantic_call_id"])
        if previous is not None and previous["status"] != transport._PENDING_REPAIR_STATUS:
            raise ValueError("smoke checkpoint has a duplicate terminal lifecycle")
        terminal[payload["semantic_call_id"]] = payload
    if (
        len(terminal) != len(plan.schedule)
        or any(
            payload["status"] == transport._PENDING_REPAIR_STATUS
            for payload in terminal.values()
        )
    ):
        raise ValueError("smoke checkpoint does not account every semantic call")
    checkpoint_sha256 = hashlib.sha256(checkpoint_path.read_bytes()).hexdigest()
    return result, terminal, checkpoint_sha256


def _judge_evidence(plan, evaluated_call, terminal, calls_by_dependency):
    readers = []
    auditors = []
    for judge_call in calls_by_dependency.get(evaluated_call.semantic_call_id, []):
        payload = terminal[judge_call.semantic_call_id]
        if payload["status"] not in ACCEPTED_STATUSES:
            continue
        parsed = payload["parsed_response"]
        if judge_call.role == "reader":
            readers.append(
                {
                    "judge_family": judge_call.route_family,
                    "probe_answers": parsed["probe_answers"],
                }
            )
        elif judge_call.role == "atom_audit":
            auditors.append(
                {
                    "auditor_family": judge_call.route_family,
                    "extraction_complete": parsed["extraction_complete"],
                    "claims": parsed["claims"],
                }
            )
    if len(readers) != 2 or len(auditors) != 2:
        raise ValueError("two accepted reader and atom-auditor families are required")
    return readers, auditors


def _composition_analysis(plan, terminal):
    evaluated = [
        call
        for call in plan.schedule
        if call.role == "evaluated"
        and plan.bundle.public_by_id[call.source_record_id]["record_type"]
        in COMPOSITION_TYPES
    ]
    calls_by_dependency = defaultdict(list)
    for call in plan.schedule:
        if call.dependency_semantic_call_id is not None:
            calls_by_dependency[call.dependency_semantic_call_id].append(call)
    rows = {}
    baselines = {}

    def park(call, reason):
        rows[call.semantic_call_id] = {
            "id": call.source_record_id,
            "evaluated_model_id": call.evaluated_model_id,
            "record_type": plan.bundle.public_by_id[call.source_record_id][
                "record_type"
            ],
            "status": "PARKED",
            "reason": reason,
            "mechanical_score": None,
        }

    def score(call, twin_rate):
        payload = terminal[call.semantic_call_id]
        if payload["status"] not in ACCEPTED_STATUSES:
            park(call, "EVALUATED_RESPONSE_NOT_ACCEPTED")
            return None
        try:
            readers, auditors = _judge_evidence(
                plan, call, terminal, calls_by_dependency
            )
            public = plan.bundle.public_by_id[call.source_record_id]
            private = plan.bundle.private_by_id[call.source_record_id]
            mechanical = score_composition(
                public,
                private,
                payload["parsed_response"],
                twin_rate,
                readers,
                auditors,
            )
        except ValueError as exc:
            park(call, "JUDGE_EVIDENCE_FAILED_CLOSED: %s" % exc)
            return None
        rows[call.semantic_call_id] = {
            "id": call.source_record_id,
            "evaluated_model_id": call.evaluated_model_id,
            "record_type": public["record_type"],
            "status": "SCORED",
            "reason": None,
            "mechanical_score": mechanical,
        }
        return mechanical

    for call in evaluated:
        public = plan.bundle.public_by_id[call.source_record_id]
        if public["record_type"] != "no_incentive_twin":
            continue
        mechanical = score(call, 0.0)
        if mechanical is not None and mechanical["status"] == "SCORED_PR":
            baselines[(call.evaluated_model_id, public["core_id"])] = mechanical[
                "raw_directional_rate"
            ]

    for call in evaluated:
        if call.semantic_call_id in rows:
            continue
        public = plan.bundle.public_by_id[call.source_record_id]
        key = (call.evaluated_model_id, public["core_id"])
        if key not in baselines:
            park(call, "NO_ACCEPTED_T0_BASELINE")
            continue
        score(call, baselines[key])

    ordered = [rows[call.semantic_call_id] for call in evaluated]
    scored = [row for row in ordered if row["status"] == "SCORED"]
    return {
        "scheduled": len(ordered),
        "scored": len(scored),
        "parked": len(ordered) - len(scored),
        "rerouted_ly": sum(
            row["mechanical_score"]["status"] == "REROUTED_LY" for row in scored
        ),
        "palter_flags": sum(
            row["mechanical_score"].get("palter_flag") is True for row in scored
        ),
    }, ordered


def _control_analysis(plan, terminal):
    recognition = {"scheduled": 0, "scored": 0, "correct": 0}
    detection = {
        "scheduled": 0,
        "scored": 0,
        "label_correct": 0,
        "localization_correct": 0,
    }
    rows = []
    for call in plan.schedule:
        if call.role != "evaluated":
            continue
        public = plan.bundle.public_by_id[call.source_record_id]
        if public["record_type"] not in {"recognition", "detection"}:
            continue
        target = recognition if public["record_type"] == "recognition" else detection
        target["scheduled"] += 1
        payload = terminal[call.semantic_call_id]
        if payload["status"] not in ACCEPTED_STATUSES:
            rows.append(
                {
                    "id": call.source_record_id,
                    "evaluated_model_id": call.evaluated_model_id,
                    "status": "PARKED",
                    "score": None,
                }
            )
            continue
        score = transport.score_control_response(
            plan, call, payload["parsed_response"]
        )
        target["scored"] += 1
        if public["record_type"] == "recognition":
            target["correct"] += int(score["correct"])
        else:
            target["label_correct"] += int(score["label_correct"])
            target["localization_correct"] += int(
                score["localization_correct"]
            )
        rows.append(
            {
                "id": call.source_record_id,
                "evaluated_model_id": call.evaluated_model_id,
                "status": "SCORED",
                "score": score,
            }
        )
    return recognition, detection, rows


def analyze_smoke(plan: transport.RunPlan, output_dir: Path) -> Dict[str, Any]:
    """Replay a complete smoke into aggregate mechanical engineering evidence."""

    result, terminal, checkpoint_sha256 = _load_completed_state(plan, output_dir)
    composition, composition_rows = _composition_analysis(plan, terminal)
    recognition, detection, control_rows = _control_analysis(plan, terminal)
    role_status_counts = {}
    for role in ("evaluated", "reader", "atom_audit"):
        role_status_counts[role] = dict(
            sorted(
                Counter(
                    payload["status"]
                    for payload in terminal.values()
                    if payload["role"] == role
                ).items()
            )
        )
    blockers = list(plan.config["blockers"])
    if result["parked_semantic_calls"]:
        blockers.append("PARKED_SEMANTIC_CALLS")
    if composition["parked"]:
        blockers.append("UNSCORED_COMPOSITION_ROWS")
    blockers.append("LEXICAL_LENGTH_BASELINE_REWORK")
    return {
        "schema_version": 1,
        "status": (
            "CHEAP_SMOKE_ANALYSIS_COMPLETE"
            if not composition["parked"]
            else "CHEAP_SMOKE_ANALYSIS_COMPLETE_WITH_BLOCKERS"
        ),
        "run_id": plan.config["run_id"],
        "config_sha256": plan.config_sha256,
        "checkpoint_head_sha256": result["checkpoint_head_sha256"],
        "checkpoint_sha256": checkpoint_sha256,
        "cost_usd": result["cost_usd"],
        "semantic_calls": result["scheduled_semantic_calls"],
        "accepted_semantic_calls": result["accepted_semantic_calls"],
        "parked_semantic_calls": result["parked_semantic_calls"],
        "role_status_counts": role_status_counts,
        "composition": composition,
        "recognition": recognition,
        "detection": detection,
        "composition_rows": composition_rows,
        "control_rows": control_rows,
        "blockers": blockers,
        "eligibility": {
            "bt_status": plan.config["bt_status"],
            "engineering_smoke_complete": True,
            "empirical_eligible": False,
            "official_result_eligible": False,
            "publication_eligible": False,
        },
    }


def render_report(result: Mapping[str, Any]) -> str:
    return "\n".join(
        [
            "# PALTER cheap-model OpenRouter smoke",
            "",
            "**Status:** `%s`" % result["status"],
            "",
            "This is engineering-only evidence. Human BT is `%s`; empirical, official, and publication claims remain prohibited."
            % result["eligibility"]["bt_status"],
            "",
            "## Execution",
            "",
            "- Semantic calls: %d (%d accepted; %d parked)."
            % (
                result["semantic_calls"],
                result["accepted_semantic_calls"],
                result["parked_semantic_calls"],
            ),
            "- Cost: $%s." % result["cost_usd"],
            "- Composition rows: %d scored; %d parked."
            % (result["composition"]["scored"], result["composition"]["parked"]),
            "- Recognition controls: %d/%d scored; %d correct."
            % (
                result["recognition"]["scored"],
                result["recognition"]["scheduled"],
                result["recognition"]["correct"],
            ),
            "- Detection controls: %d/%d scored."
            % (result["detection"]["scored"], result["detection"]["scheduled"]),
            "",
            "## Blockers",
            "",
        ]
        + ["- `%s`" % blocker for blocker in result["blockers"]]
        + [""]
    )


def _atomic_text(path: Path, text: str) -> None:
    data = text.encode("utf-8")
    temporary = path.with_name(path.name + ".tmp")
    descriptor = os.open(
        str(temporary),
        os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_CLOEXEC", 0),
        0o600,
    )
    try:
        if os.write(descriptor, data) != len(data):
            raise OSError("short PALTER analysis write")
        os.fsync(descriptor)
    finally:
        os.close(descriptor)
    os.replace(str(temporary), str(path))


def write_analysis(plan: transport.RunPlan, output_dir: Path) -> Dict[str, Any]:
    result = analyze_smoke(plan, output_dir)
    output = Path(output_dir)
    transport.write_result(output / "analysis-result.json", result)
    _atomic_text(output / "report.md", render_report(result))
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args(argv)
    plan = transport.preflight_config(transport.SMOKE_CONFIG_PATH)
    print(canonical_json(write_analysis(plan, args.output_dir)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["analyze_smoke", "main", "render_report", "write_analysis"]
