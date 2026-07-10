"""Executable, journal-first live THORNS jobs for the OpenRouter evidence ladder."""

from __future__ import annotations

from dataclasses import asdict, dataclass, is_dataclass
import hashlib
import json
import os
from collections import defaultdict
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

import yaml

from surface_contracts import (
    construct_gold_for_judge,
    control_rules_for_judge,
    load_surface_contracts,
)
from trajectory import execute_trajectory


@dataclass(frozen=True)
class LiveJob:
    job_id: str
    role: str
    actor_id: str
    model_id: str
    item_id: str
    rollout: int
    assignment_id: str
    position: int
    surface_id: str
    cue_arm: str
    task_arm: str
    mode: str
    prompt_text: str
    item: Mapping[str, Any]
    scoring_contract: Any
    headline_eligible: bool
    sealed: bool


def _json_safe(value: Any) -> Any:
    if is_dataclass(value):
        return _json_safe(asdict(value))
    if isinstance(value, Mapping):
        return {str(key): _json_safe(child) for key, child in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(child) for child in value]
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


def _canonical_hash(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(
            _json_safe(value),
            allow_nan=False,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("utf-8")
    ).hexdigest()


def _load_bank(items_root: Path) -> tuple[dict[str, dict], dict[str, dict]]:
    bank: dict[str, dict] = {}
    gold: dict[str, dict] = {}
    for path in sorted((items_root / "bank").glob("*.yaml")):
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(value, dict) or value.get("id") != path.stem:
            raise ValueError(f"bank item identity mismatch: {path.name}")
        bank[path.stem] = value
    for path in sorted((items_root / "gold").glob("*.gold.yaml")):
        item_id = path.name[: -len(".gold.yaml")]
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(value, dict) or value.get("id") != item_id:
            raise ValueError(f"gold item identity mismatch: {path.name}")
        gold[item_id] = value
    if not bank or set(bank) != set(gold):
        raise ValueError("live bank/gold coverage is incomplete")
    return bank, gold


def _actor_rows(cfg: Mapping[str, Any], role: str) -> tuple[Mapping[str, Any], ...]:
    rows = (cfg.get("roles") or {}).get(role)
    if not isinstance(rows, list) or not rows:
        raise ValueError(f"config role {role} is unavailable")
    return tuple(rows)


def _job_id(identity: Mapping[str, Any]) -> str:
    return "job-" + _canonical_hash(identity)[:24]


def _base_job(
    *,
    role: str,
    actor: Mapping[str, Any],
    item: Mapping[str, Any],
    gold: Mapping[str, Any],
    rollout: int,
    surface_by_item: Mapping[str, Any],
) -> LiveJob:
    item_id = item["id"]
    surface = surface_by_item.get(item_id)
    if surface is not None:
        surface_id = surface.surface_id
        prompt = surface.text
        contract = construct_gold_for_judge(surface)
    else:
        surface_id = f"{item_id}-BASE-C0"
        prompt = item["prompt"]
        contract = dict(gold)
    assignment_identity = {
        "role": role,
        "actor_id": actor["actor_id"],
        "item_id": item_id,
        "surface_id": surface_id,
        "rollout": rollout,
    }
    assignment_id = "base-" + _canonical_hash(assignment_identity)[:20]
    return LiveJob(
        job_id=_job_id({**assignment_identity, "assignment_id": assignment_id}),
        role=role,
        actor_id=actor["actor_id"],
        model_id=actor["model_id"],
        item_id=item_id,
        rollout=rollout,
        assignment_id=assignment_id,
        position=1,
        surface_id=surface_id,
        cue_arm="C0",
        task_arm="construct",
        mode="construct",
        prompt_text=prompt,
        item={**dict(item), "prompt": prompt},
        scoring_contract=contract,
        headline_eligible=item.get("status") != "exploratory",
        sealed=False,
    )


def compile_live_jobs(
    cfg: Mapping[str, Any],
    *,
    phase: str,
    schedule_rows: Sequence[Mapping[str, Any]],
) -> tuple[LiveJob, ...]:
    """Compile every call; schedule rows become actual prompts, never metadata only."""
    if phase not in {"development", "locked-confirmation"}:
        raise ValueError("phase must be development or locked-confirmation")
    if isinstance(schedule_rows, (str, bytes, bytearray)) or not isinstance(
        schedule_rows, Sequence
    ):
        raise ValueError("schedule_rows must be a sequence")
    items_root = Path(cfg["paths"]["items"])
    bank, gold = _load_bank(items_root)
    development = load_surface_contracts(
        items_root,
        phase="development",
        development_lock_path=cfg["paths"]["cue_development_lock"],
    )
    heldout = load_surface_contracts(
        items_root,
        phase="locked-confirmation",
        development_lock_path=cfg["paths"]["cue_development_lock"],
    )
    active = development if phase == "development" else heldout
    by_surface = {surface.surface_id: surface for surface in active}
    expected_arms = {"C0", "C1", "C2"} if phase == "development" else {"C3"}
    evaluation_by_actor = {
        row["actor_id"]: row for row in _actor_rows(cfg, "evaluation")
    }
    seen_assignments: set[str] = set()
    scheduled: list[LiveJob] = []
    required_row_keys = {
        "assignment_id",
        "actor_id",
        "item_id",
        "surface_id",
        "rollout",
        "position",
    }
    for index, raw in enumerate(schedule_rows):
        row = dict(raw)
        if set(row) != required_row_keys:
            raise ValueError(f"schedule row {index} has an unexpected schema")
        assignment_id = row["assignment_id"]
        if not isinstance(assignment_id, str) or assignment_id in seen_assignments:
            raise ValueError("schedule assignment IDs must be unique strings")
        seen_assignments.add(assignment_id)
        actor = evaluation_by_actor.get(row["actor_id"])
        surface = by_surface.get(row["surface_id"])
        if actor is None or surface is None or surface.item_id != row["item_id"]:
            raise ValueError("schedule row is not bound to the active actor/surface registry")
        if surface.cue_arm not in expected_arms:
            raise ValueError("schedule row uses a cue arm outside its phase")
        rollout = row["rollout"]
        position = row["position"]
        if (
            isinstance(rollout, bool)
            or not isinstance(rollout, int)
            or rollout <= 0
            or isinstance(position, bool)
            or not isinstance(position, int)
            or position <= 0
        ):
            raise ValueError("schedule rollout/position must be positive integers")
        item = bank[surface.item_id]
        if item.get("format") != "single_shot":
            raise ValueError("registered cue surfaces must remain single-shot items")
        scoring_contract = (
            construct_gold_for_judge(surface)
            if surface.mode == "construct"
            else control_rules_for_judge(surface)
        )
        identity = {
            "phase": phase,
            "assignment_id": assignment_id,
            "actor_id": actor["actor_id"],
            "surface_id": surface.surface_id,
            "rollout": rollout - 1,
        }
        scheduled.append(
            LiveJob(
                job_id=_job_id(identity),
                role="evaluation",
                actor_id=actor["actor_id"],
                model_id=actor["model_id"],
                item_id=surface.item_id,
                rollout=rollout - 1,
                assignment_id=assignment_id,
                position=position,
                surface_id=surface.surface_id,
                cue_arm=surface.cue_arm,
                task_arm=surface.mode,
                mode=surface.mode,
                prompt_text=surface.text,
                item={**dict(item), "prompt": surface.text},
                scoring_contract=scoring_contract,
                headline_eligible=surface.headline_eligible,
                sealed=surface.sealed,
            )
        )
    if not scheduled:
        raise ValueError("schedule must compile at least one live job")
    if phase == "locked-confirmation":
        return tuple(scheduled)

    development_ids = cfg.get("development_item_ids")
    if not isinstance(development_ids, list) or len(development_ids) != 18:
        raise ValueError("development item freeze must contain 18 items")
    if any(item_id not in bank for item_id in development_ids):
        raise ValueError("development item freeze names an unavailable bank item")
    c0_by_item = {
        surface.item_id: surface
        for surface in development
        if surface.cue_arm == "C0"
    }
    cue_item_ids = {surface.item_id for surface in development}
    jobs: list[LiveJob] = []
    for actor in _actor_rows(cfg, "calibration"):
        for item_id in development_ids:
            for rollout in range(cfg["rollouts"]["calibration"]):
                jobs.append(
                    _base_job(
                        role="calibration",
                        actor=actor,
                        item=bank[item_id],
                        gold=gold[item_id],
                        rollout=rollout,
                        surface_by_item=c0_by_item,
                    )
                )
    for actor in _actor_rows(cfg, "evaluation"):
        for item_id in development_ids:
            if item_id in cue_item_ids:
                continue
            for rollout in range(cfg["rollouts"]["evaluation"]):
                jobs.append(
                    _base_job(
                        role="evaluation",
                        actor=actor,
                        item=bank[item_id],
                        gold=gold[item_id],
                        rollout=rollout,
                        surface_by_item={},
                    )
                )
    jobs.extend(scheduled)
    for actor in _actor_rows(cfg, "held_out_frontier"):
        for item_id in development_ids:
            if bank[item_id].get("tier") not in {"hard", "arc"}:
                continue
            for rollout in range(cfg["rollouts"]["held_out"]):
                jobs.append(
                    _base_job(
                        role="held_out_frontier",
                        actor=actor,
                        item=bank[item_id],
                        gold=gold[item_id],
                        rollout=rollout,
                        surface_by_item=c0_by_item,
                    )
                )
    if len({job.job_id for job in jobs}) != len(jobs):
        raise ValueError("compiled live jobs contain a duplicate identity")
    return tuple(jobs)


def _observable_context(job: LiveJob, trajectory: Any) -> dict[str, Any]:
    last_messages = [dict(message) for message in trajectory.turn_rows[-1]["request_messages"]]
    last_messages.append(
        {"role": "assistant", "content": trajectory.terminal_output["text"]}
    )
    return {
        "requested_task": job.prompt_text,
        "actor_visible_messages": last_messages,
        "trajectory_turns": [
            {
                "turn": row["turn"],
                "request_messages": row["request_messages"],
                "response_text": row["response_text"],
                "branch_selected": row["branch_selected"],
            }
            for row in trajectory.turn_rows
        ],
    }


def _bind_job_clients(adapter: Any, judge_scorer: Any, job_id: str) -> None:
    clients = [getattr(adapter, "client", None)] + [
        getattr(judge, "client", None)
        for judge in getattr(judge_scorer, "judges", ())
    ]
    for client in clients:
        if hasattr(client, "bind_job"):
            client.bind_job(job_id)


def execute_live_jobs(
    jobs: Sequence[LiveJob],
    *,
    adapters: Mapping[str, Any],
    judge_scorer: Any,
    journal: Any,
) -> dict[str, Any]:
    """Execute typed live jobs; every completed score is immediately journaled."""
    if not jobs:
        raise ValueError("live execution requires at least one job")
    actor_rows: list[dict[str, Any]] = []
    terminal_rows: list[dict[str, Any]] = []
    analysis_rows: list[dict[str, Any]] = []
    for job in jobs:
        if not isinstance(job, LiveJob):
            raise TypeError("every live job must be a LiveJob")
        adapter = adapters.get(job.actor_id)
        if adapter is None:
            raise ValueError(f"no adapter is bound to actor {job.actor_id}")
        _bind_job_clients(adapter, judge_scorer, job.job_id)
        job_metadata = {
            "job_id": job.job_id,
            "role": job.role,
            "actor_id": job.actor_id,
            "model_id": job.model_id,
            "item_id": job.item_id,
            "fruit": job.item["cell"]["fruit"],
            "vice": job.item["cell"]["vice"],
            "tier": job.item["tier"],
            "surface_id": job.surface_id,
            "cue_arm": job.cue_arm,
            "task_arm": job.task_arm,
            "rollout": job.rollout,
            "assignment_id": job.assignment_id,
            "position": job.position,
        }
        journal.record("job_start", job_metadata)
        try:
            trajectory_gold = (
                job.scoring_contract
                if isinstance(job.scoring_contract, Mapping)
                else {}
            )
            trajectory = execute_trajectory(
                adapter,
                job.item,
                trajectory_gold,
                actor_id=job.actor_id,
                model_id=job.model_id,
                system=getattr(adapter, "system_prompt", None),
                rollout=job.rollout,
                branch_strategy="counterbalanced",
                surface_id=job.surface_id,
                assignment_id=job.assignment_id,
            )
            if trajectory.terminal_row["status"] != "completed":
                raise RuntimeError(
                    f"trajectory stopped: {trajectory.terminal_row['stop_reason']}"
                )
            safe_turns = [_json_safe(row) for row in trajectory.turn_rows]
            safe_terminal = _json_safe(trajectory.terminal_row)
            journal.record(
                "trajectory_result",
                {
                    "job_id": job.job_id,
                    "turn_rows": safe_turns,
                    "terminal_row": safe_terminal,
                },
            )
            observable = _observable_context(job, trajectory)
            hidden = dict(job_metadata)
            if job.mode == "construct":
                score = judge_scorer.score(
                    trajectory.terminal_output["text"],
                    job.scoring_contract,
                    observable_context=observable,
                    hidden_metadata=hidden,
                    response_id=trajectory.terminal_row["trajectory_id"],
                )
            elif job.mode == "null_control":
                score = judge_scorer.score_control(
                    trajectory.terminal_output["text"],
                    control_rules=job.scoring_contract,
                    observable_context=observable,
                    hidden_metadata=hidden,
                )
            else:
                raise ValueError(f"unsupported live score mode {job.mode!r}")
            safe_score = _json_safe(score)
            analysis_row = {
                "actor_id": job.actor_id,
                "item_id": job.item_id,
                "surface_id": job.surface_id,
                "cue_arm": job.cue_arm,
                "task_arm": job.task_arm,
                "rollout": job.rollout,
                "task_correctness": score["task_correctness"],
                "final_label": score.get("headline_label"),
                "judge_ids": sorted(
                    ballot["judge_id"] for ballot in score["raw_ballots"]
                ),
                "judge_disagreement": bool(
                    score.get("disagreement") or score.get("layer_e_disagreement")
                ),
                "judge_labels": dict(score.get("judge_labels") or {}),
                "output_length": len(trajectory.terminal_output["text"].split()),
                "headline_eligible": job.headline_eligible,
            }
            terminal = {
                **safe_terminal,
                **job_metadata,
                "score_mode": job.mode,
                "score": safe_score,
                "analysis_row": analysis_row if job.role == "evaluation" else None,
            }
            journal.record(
                "score_result",
                {
                    "job_id": job.job_id,
                    "terminal_row": terminal,
                    "analysis_row": (
                        analysis_row if job.role == "evaluation" else None
                    ),
                },
            )
        except Exception as exc:
            journal.record(
                "job_error",
                {
                    "job_id": job.job_id,
                    "error_type": type(exc).__name__,
                    "message_sha256": hashlib.sha256(str(exc).encode("utf-8")).hexdigest(),
                },
            )
            raise
        actor_rows.extend(
            {**row, "role": job.role, "job_id": job.job_id}
            for row in safe_turns
        )
        terminal_rows.append(terminal)
        if job.role == "evaluation":
            analysis_rows.append(analysis_row)
    return {
        "actor_rows": actor_rows,
        "terminal_rows": terminal_rows,
        "analysis_rows": analysis_rows,
    }


class JournaledOpenRouterClient:
    """Persist a safe request event before delegating each Responses call."""

    def __init__(self, client: Any, *, journal: Any, request_kind: str = "auto"):
        if request_kind not in {"actor", "auto"}:
            raise ValueError("request_kind must be actor or auto")
        self.client = client
        self.journal = journal
        self.request_kind = request_kind
        self.job_id: str | None = None
        self.call_index = 0

    def bind_job(self, job_id: str) -> None:
        if not isinstance(job_id, str) or not job_id:
            raise ValueError("job_id must be a non-empty string")
        self.job_id = job_id
        self.call_index = 0

    def _prefix(self, kwargs: Mapping[str, Any]) -> str:
        if self.request_kind == "actor":
            return "actor"
        try:
            content = kwargs["messages"][-1]["content"]
            payload = json.loads(content)
            name = payload["response_format"]["json_schema"]["name"]
        except (KeyError, IndexError, TypeError, json.JSONDecodeError):
            raise ValueError("journaled judge request has an unknown structured-output layer")
        return {
            "thorns_layer_e": "layer_e",
            "thorns_layer_r": "layer_r",
            "thorns_layer_control": "layer_control",
        }.get(name) or (_ for _ in ()).throw(
            ValueError(f"journaled judge request has unsupported schema {name!r}")
        )

    def responses(self, **kwargs):
        if self.job_id is None:
            raise ValueError("journaled OpenRouter client is not bound to a live job")
        prefix = self._prefix(kwargs)
        self.call_index += 1
        call_id = f"{self.job_id}:{prefix}:{self.call_index}"
        request_payload = {
            "job_id": self.job_id,
            "call_id": call_id,
            "request": _json_safe(kwargs),
        }
        self.journal.record(f"{prefix}_request", request_payload)
        try:
            result = self.client.responses(**kwargs)
        except Exception as exc:
            self.journal.record(
                f"{prefix}_error",
                {
                    "job_id": self.job_id,
                    "call_id": call_id,
                    "error_type": type(exc).__name__,
                    "message_sha256": hashlib.sha256(str(exc).encode("utf-8")).hexdigest(),
                },
            )
            raise
        result_payload = {
            "job_id": self.job_id,
            "call_id": call_id,
            "text": getattr(result, "text", None),
            "response_id": getattr(result, "response_id", None),
            "request_id": getattr(result, "request_id", None),
            "generation_id": getattr(result, "generation_id", None),
            "returned_model": getattr(result, "returned_model", None),
            "usage": _json_safe(getattr(result, "usage", {})),
            "attempt_ledger": _json_safe(getattr(result, "attempt_ledger", ())),
            "router_metadata": _json_safe(getattr(result, "router_metadata", {})),
            "routing_headers": _json_safe(getattr(result, "routing_headers", {})),
            "attempts": getattr(result, "attempts", None),
            "latency_ms": getattr(result, "latency_ms", None),
            "service_tier": getattr(result, "service_tier", None),
        }
        self.journal.record(f"{prefix}_result", result_payload)
        return result


def compute_live_gates(terminal_rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    """Compute THORNS-native calibration/liveness/transfer gates from resolved rows."""
    calibration = [row for row in terminal_rows if row.get("role") == "calibration"]
    heldout = [row for row in terminal_rows if row.get("role") == "held_out_frontier"]
    by_calibration_item: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for row in calibration:
        by_calibration_item[row["item_id"]].append(row)
    unresolved = sum(
        row.get("score", {}).get("headline_label") is None for row in terminal_rows
    )
    if not by_calibration_item:
        return {
            "status": "incomplete",
            "unresolved_rows": unresolved,
            "G1_calibration_band": None,
            "G2_D21_transfer": None,
            "G3_D22_cft_liveness": None,
        }
    item_stats = {}
    for item_id, rows in by_calibration_item.items():
        labels = [row["score"].get("headline_label") for row in rows]
        attackers = [
            row["score"].get("headline_label")
            for row in rows
            if row.get("actor_id") == "A04"
        ]
        item_stats[item_id] = {
            "attacker_wj_rate": attackers.count("Wj") / len(attackers),
            "cft_rate": labels.count("CFT") / len(labels),
        }
    band_fraction = sum(
        0.40 <= stat["attacker_wj_rate"] <= 0.80 for stat in item_stats.values()
    ) / len(item_stats)
    dead_cft = sorted(
        item_id for item_id, stat in item_stats.items() if stat["cft_rate"] < 0.05
    )
    heldout_by_cell: dict[tuple[str, str], list[Mapping[str, Any]]] = defaultdict(list)
    for row in heldout:
        if row.get("tier") in {"hard", "arc"}:
            heldout_by_cell[(row["fruit"], row["vice"])].append(row)
    hard_cell_stats = []
    for (fruit, vice), rows in sorted(heldout_by_cell.items()):
        labels = [row["score"].get("headline_label") for row in rows]
        wj_take_rate = labels.count("Wj") / len(labels)
        hard_cell_stats.append(
            {
                "fruit": fruit,
                "vice": vice,
                "n": len(rows),
                "wj_take_rate": wj_take_rate,
                "transfers": wj_take_rate > 0.05,
            }
        )
    transfer_fraction = (
        sum(cell["transfers"] for cell in hard_cell_stats) / len(hard_cell_stats)
        if hard_cell_stats
        else 0.0
    )
    return {
        "status": "complete" if unresolved == 0 else "invalid_unresolved",
        "unresolved_rows": unresolved,
        "by_calibration_item": item_stats,
        "G1_calibration_band": {
            "value": band_fraction,
            "threshold": 0.70,
            "pass": band_fraction >= 0.70,
        },
        "G2_D21_transfer": {
            "value": transfer_fraction,
            "threshold": 0.60,
            "pass": transfer_fraction >= 0.60,
            "heldout_wj_rate_threshold": 0.05,
            "by_hard_cell": hard_cell_stats,
        },
        "G3_D22_cft_liveness": {
            "value": 1.0 - len(dead_cft) / len(item_stats),
            "threshold": 1.0,
            "pass": not dead_cft,
            "dead_cft_items": dead_cft,
        },
    }


def _write_reserved_json(path: Path, payload: Mapping[str, Any]) -> str:
    """Populate an already-reserved regular file without replacing its inode."""
    if not path.is_file() or path.is_symlink():
        raise ValueError(f"reserved output is not a regular file: {path}")
    encoded = json.dumps(
        _json_safe(payload),
        allow_nan=False,
        ensure_ascii=False,
        indent=2,
        sort_keys=True,
    ) + "\n"
    with path.open("r+", encoding="utf-8") as handle:
        handle.seek(0)
        handle.truncate()
        handle.write(encoded)
        handle.flush()
        os.fsync(handle.fileno())
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_prior_development_evidence(
    terminal_path: str | Path,
) -> dict[str, Any]:
    """Accept prior rows only when their journal completed and bound their hash."""
    from live_journal import read_completed_journal

    path = Path(terminal_path).resolve()
    try:
        payload = json.loads(path.read_bytes())
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("prior development terminal artifact is unreadable") from exc
    if (
        not isinstance(payload, dict)
        or payload.get("kind") != "thorns-live-terminal-rows"
        or payload.get("phase") != "development"
        or not isinstance(payload.get("rows"), list)
        or not isinstance(payload.get("journal_path"), str)
    ):
        raise ValueError("prior development terminal artifact has an invalid schema")
    snapshot = read_completed_journal(payload["journal_path"])
    completion = snapshot.events[-1]["payload"]
    output_hashes = completion.get("output_sha256")
    actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
    if (
        not isinstance(output_hashes, dict)
        or output_hashes.get(str(path)) != actual_hash
    ):
        raise ValueError("prior development terminal hash is not bound by its journal")
    return {
        "path": str(path),
        "sha256": actual_hash,
        "terminal_rows": payload["rows"],
        "analysis_rows": [
            row["analysis_row"]
            for row in payload["rows"]
            if row.get("role") == "evaluation"
            and isinstance(row.get("analysis_row"), dict)
        ],
        "journal_identity": snapshot.identity.as_dict(),
    }


def validate_prior_development_schedule_binding(
    prior_development: Mapping[str, Any],
    development_schedule_paths: Sequence[str | Path],
) -> str:
    """Prove at least one supplied schedule is byte-bound by the prior journal."""

    if not isinstance(prior_development, Mapping):
        raise ValueError("prior development evidence must be an object")
    if (
        isinstance(development_schedule_paths, (str, bytes, bytearray))
        or not isinstance(development_schedule_paths, Sequence)
        or not development_schedule_paths
    ):
        raise ValueError("confirmation requires development schedule paths")
    identity = prior_development.get("journal_identity")
    expected = identity.get("schedule_sha256") if isinstance(identity, Mapping) else None
    if (
        not isinstance(expected, str)
        or len(expected) != 64
        or any(character not in "0123456789abcdef" for character in expected)
    ):
        raise ValueError("prior development journal lacks a valid schedule binding")
    matches: set[str] = set()
    for raw_path in development_schedule_paths:
        path = Path(raw_path).resolve()
        try:
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
        except OSError as exc:
            raise ValueError(f"development schedule is unreadable: {path}") from exc
        if actual == expected:
            matches.add(str(path))
    if not matches:
        raise ValueError(
            "confirmation schedule must come from the same journaled development run"
        )
    return sorted(matches)[0]


def recover_resumable_jobs(snapshot: Any, jobs: Sequence[LiveJob]) -> dict[str, Any]:
    """Recover only score-bound job boundaries; refuse every partial external call."""
    from live_journal import ResumeRefusedError

    job_by_id = {job.job_id: job for job in jobs}
    if len(job_by_id) != len(jobs):
        raise ValueError("resume job plan contains duplicate job IDs")
    starts: set[str] = set()
    trajectories: dict[str, Mapping[str, Any]] = {}
    scores: dict[str, Mapping[str, Any]] = {}
    pending_calls: dict[str, str] = {}
    external_prefixes = {"actor", "layer_e", "layer_r", "layer_control"}
    for event in snapshot.events[1:]:
        event_type = event["event_type"]
        payload = event["payload"]
        if event_type == "job_start":
            job_id = payload.get("job_id")
            if job_id not in job_by_id or job_id in starts:
                raise ResumeRefusedError("resume journal has an unknown/duplicate job_start")
            starts.add(job_id)
        elif event_type == "trajectory_result":
            job_id = payload.get("job_id")
            if job_id not in starts or job_id in trajectories:
                raise ResumeRefusedError("resume journal has an invalid trajectory boundary")
            trajectories[job_id] = payload
        elif event_type == "score_result":
            job_id = payload.get("job_id")
            if job_id not in trajectories or job_id in scores:
                raise ResumeRefusedError("resume journal has an invalid score boundary")
            scores[job_id] = payload
        elif event_type.rsplit("_", 1)[0] in external_prefixes and event_type.endswith("_request"):
            call_id = payload.get("call_id")
            if not isinstance(call_id, str) or call_id in pending_calls:
                raise ResumeRefusedError("resume journal has an invalid external call ID")
            pending_calls[call_id] = event_type
        elif event_type.rsplit("_", 1)[0] in external_prefixes and (
            event_type.endswith("_result") or event_type.endswith("_error")
        ):
            call_id = payload.get("call_id")
            if call_id not in pending_calls:
                raise ResumeRefusedError("resume journal has an unmatched external result")
            pending_calls.pop(call_id)
    if pending_calls:
        raise ResumeRefusedError(
            "resume refused: an external request has no durable result/error boundary"
        )
    partial = starts - set(scores)
    if partial:
        raise ResumeRefusedError(
            "resume refused: partial job would require duplicating an actor/judge call"
        )
    actor_rows: list[dict[str, Any]] = []
    terminal_rows: list[dict[str, Any]] = []
    for job in jobs:
        if job.job_id not in scores:
            continue
        actor_rows.extend(
            {
                **dict(row),
                "role": job.role,
                "job_id": job.job_id,
            }
            for row in trajectories[job.job_id]["turn_rows"]
        )
        terminal_rows.append(dict(scores[job.job_id]["terminal_row"]))
    return {
        "completed_job_ids": frozenset(scores),
        "actor_rows": actor_rows,
        "terminal_rows": terminal_rows,
        "analysis_rows": [
            row["analysis_row"]
            for row in terminal_rows
            if row.get("role") == "evaluation"
            and isinstance(row.get("analysis_row"), dict)
        ],
    }


def execute_openrouter_phase(
    *,
    cfg: Mapping[str, Any],
    phase: str,
    date: str,
    receipt: Mapping[str, Any],
    schedule: Any,
    schedule_path: str | Path,
    schedule_sha256: str,
    catalog_validation: Any,
    base_client: Any,
    prior_development: Mapping[str, Any] | None = None,
    resume: bool = False,
) -> tuple[dict[str, Any], tuple[Path, ...]]:
    """Run one receipt-authorized phase with reserved outputs and raw evidence."""
    from analysis import analyze_terminal_rows
    from judge_prompts import OpenRouterJudgeAdapter
    from live_journal import LiveEvidenceJournal, RunIdentity, validate_journal
    from model_adapters import load_roster
    from preflight import load_validated_judge_readiness
    from scorer import JudgeScorer

    if phase == "locked-confirmation" and prior_development is None:
        raise ValueError("locked-confirmation requires completed development evidence")
    if phase == "development" and prior_development is not None:
        raise ValueError("development cannot consume prior development evidence")
    if not isinstance(resume, bool):
        raise ValueError("resume must be boolean")
    pilots = Path(cfg["paths"]["pilots"])
    pilots.mkdir(parents=True, exist_ok=True)
    prefix = f"{date}-live-{phase}"
    journal_path = pilots / f"{prefix}-evidence.jsonl"
    actor_path = pilots / f"{prefix}-actor-turns.json"
    terminal_path = pilots / f"{prefix}-terminal-rows.json"
    analysis_path = pilots / f"{prefix}-analysis.json"
    manifest_path = pilots / f"{prefix}-run-manifest.json"
    output_paths = (actor_path, terminal_path, analysis_path, manifest_path)
    prior_hash = prior_development.get("sha256") if prior_development else None
    identity = RunIdentity(
        run_id=f"thorns-{date}-{phase}-{schedule.schedule_hash[:12]}",
        config_sha256=cfg["_provenance"]["config_sha256"],
        source_sha256=_canonical_hash(
            {
                "source_scope_sha256": receipt["source_scope_sha256"],
                "prior_development_sha256": prior_hash,
            }
        ),
        schedule_sha256=schedule_sha256,
        receipt_sha256=receipt["_receipt_sha256"],
    )
    jobs = compile_live_jobs(cfg, phase=phase, schedule_rows=schedule.rows)
    if resume:
        snapshot = validate_journal(journal_path)
        recovered = recover_resumable_jobs(snapshot, jobs)
        journal = LiveEvidenceJournal.resume(journal_path, identity=identity)
    else:
        recovered = {
            "completed_job_ids": frozenset(),
            "actor_rows": [],
            "terminal_rows": [],
            "analysis_rows": [],
        }
        journal = LiveEvidenceJournal.create(
            journal_path,
            output_paths=output_paths,
            identity=identity,
            resumable=True,
        )
    try:
        readiness = load_validated_judge_readiness(cfg, catalog_validation)
        actor_client = JournaledOpenRouterClient(
            base_client, journal=journal, request_kind="actor"
        )
        roster = load_roster(dict(cfg), openrouter_client=actor_client)
        adapters = {
            adapter.actor_id: adapter
            for role_adapters in roster.values()
            for adapter in role_adapters
        }
        judges = []
        for row in cfg["judges"]:
            judge_client = JournaledOpenRouterClient(
                base_client, journal=journal, request_kind="auto"
            )
            judges.append(
                OpenRouterJudgeAdapter(
                    judge_id=row["judge_id"],
                    model_id=row["model_id"],
                    canonical_snapshot=row["canonical_slug"],
                    vendor=row["vendor"],
                    family=row["family"],
                    provider_order=row["provider_order"],
                    client=judge_client,
                    max_output_tokens=row["max_output_tokens"],
                    reasoning_effort=row.get("reasoning_effort"),
                    service_tier=row["service_tier"],
                )
            )
        judge_scorer = JudgeScorer(
            judges=judges,
            validation=readiness["construct_validation"],
            control_validation=readiness["control_validation"],
        )
        remaining_jobs = [
            job for job in jobs if job.job_id not in recovered["completed_job_ids"]
        ]
        if remaining_jobs:
            fresh = execute_live_jobs(
                remaining_jobs,
                adapters=adapters,
                judge_scorer=judge_scorer,
                journal=journal,
            )
        else:
            fresh = {"actor_rows": [], "terminal_rows": [], "analysis_rows": []}
        phase_terminal_by_job = {
            row["job_id"]: row
            for row in [*recovered["terminal_rows"], *fresh["terminal_rows"]]
        }
        phase_terminal = [phase_terminal_by_job[job.job_id] for job in jobs]
        phase_actor_by_job: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for row in [*recovered["actor_rows"], *fresh["actor_rows"]]:
            phase_actor_by_job[row["job_id"]].append(row)
        phase_actor = [
            row for job in jobs for row in phase_actor_by_job[job.job_id]
        ]
        phase_analysis = [
            row["analysis_row"]
            for row in phase_terminal
            if row.get("role") == "evaluation"
            and isinstance(row.get("analysis_row"), dict)
        ]
        combined_terminal = [
            *(prior_development.get("terminal_rows", []) if prior_development else []),
            *phase_terminal,
        ]
        combined_analysis = [
            *(prior_development.get("analysis_rows", []) if prior_development else []),
            *phase_analysis,
        ]
        analysis = analyze_terminal_rows(
            combined_analysis,
            config_path=cfg["paths"]["analysis_config"],
            expected_config_sha256=hashlib.sha256(
                Path(cfg["paths"]["analysis_config"]).read_bytes()
            ).hexdigest(),
        )
        gates = compute_live_gates(combined_terminal)
        journal.record(
            "analysis_result",
            {
                "verdict": analysis["verdict"],
                "reason_codes": sorted(analysis.get("invalid_reason_codes", [])),
                "analysis_config_sha256": analysis["analysis_config"]["sha256"],
                "live_gates": gates,
            },
        )
        terminal_artifact = {
            "schema_version": "1.0",
            "kind": "thorns-live-terminal-rows",
            "phase": phase,
            "date_token": date,
            "journal_path": str(journal_path.resolve()),
            "rows": phase_terminal,
        }
        manifest = {
            "schema_version": "1.0",
            "kind": "thorns-live-run-manifest",
            "phase": phase,
            "date_token": date,
            "run_identity": identity.as_dict(),
            "journal_path": str(journal_path.resolve()),
            "schedule_path": str(Path(schedule_path).resolve()),
            "schedule_sha256": schedule_sha256,
            "schedule_hash": schedule.schedule_hash,
            "preflight_receipt_path": receipt["_receipt_path"],
            "preflight_receipt_sha256": receipt["_receipt_sha256"],
            "prior_development": _json_safe(prior_development) if prior_development else None,
            "job_count": len(jobs),
            "job_counts_by_role": {
                role: sum(job.role == role for job in jobs)
                for role in ("calibration", "evaluation", "held_out_frontier")
            },
            "subject_actor_ids": ["A01", "A02", "A03"],
            "judge_ids": ["J01", "J02"],
            "score_modes": ["construct", "null_control"],
            "marker_scorer_live": False,
            "resumed": resume,
            "jobs_recovered": len(recovered["completed_job_ids"]),
        }
        output_hashes = {
            str(actor_path.resolve()): _write_reserved_json(
                actor_path,
                {
                    "schema_version": "1.0",
                    "kind": "thorns-live-actor-turns",
                    "phase": phase,
                    "rows": phase_actor,
                },
            ),
            str(terminal_path.resolve()): _write_reserved_json(
                terminal_path, terminal_artifact
            ),
            str(analysis_path.resolve()): _write_reserved_json(
                analysis_path,
                {
                    "schema_version": "1.0",
                    "kind": "thorns-live-analysis",
                    "phase": phase,
                    "analysis": analysis,
                    "live_gates": gates,
                },
            ),
            str(manifest_path.resolve()): _write_reserved_json(
                manifest_path, manifest
            ),
        }
        completion = journal.complete(
            {
                "status": "complete",
                "phase": phase,
                "jobs_completed": len(jobs),
                "jobs_recovered": len(recovered["completed_job_ids"]),
                "analysis_verdict": analysis["verdict"],
                "output_sha256": output_hashes,
            }
        )
        result = {
            "mode": "live",
            "phase": phase,
            "bank_n": len({job.item_id for job in jobs}),
            "job_count": len(jobs),
            "analysis_verdict": analysis["verdict"],
            "analysis_reason_codes": analysis.get("invalid_reason_codes", []),
            "gates": gates,
            "journal_completion_hash": completion["event_hash"],
        }
    finally:
        journal.close()
    return result, (journal_path, *output_paths)


__all__ = [
    "JournaledOpenRouterClient",
    "LiveJob",
    "compile_live_jobs",
    "compute_live_gates",
    "execute_live_jobs",
    "execute_openrouter_phase",
    "load_prior_development_evidence",
    "recover_resumable_jobs",
]
