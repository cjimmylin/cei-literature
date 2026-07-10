#!/usr/bin/env python3
"""Message-first trajectory execution for THORNS actors.

Single-shot items issue one request.  Escalation arcs issue one request per authored
beat and carry forward only already-observed user/assistant history.  Conditional
user replies are selected from the item's explicit branch map by the deterministic
marker rule below; the executor never invents a branch or exposes a future beat.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, is_dataclass
from typing import Any, Mapping, Sequence

from scorer import MarkerScorer


# Deliberately public and frozen: branch routing is evidence-generating behavior.
# A mixed response follows the authored CFT clarification rather than an invented
# compromise.  An unclassified response has no declared route and stops the arc.
BRANCH_BY_LABEL = {
    "Fi": "fruit_path",
    "Wj": "vice_path",
    "CFT": "cft_path",
    "mixed": "cft_path",
}
COUNTERBALANCED_BRANCHES = ("fruit_path", "vice_path", "cft_path")
BRANCH_STRATEGIES = frozenset({"synthetic_marker", "counterbalanced"})


@dataclass(frozen=True)
class TrajectoryResult:
    """One rollout's immutable actor rows, terminal row, and final adapter output."""

    turn_rows: tuple[dict[str, Any], ...]
    terminal_row: dict[str, Any]
    terminal_output: dict[str, Any]


def _json_safe(value: Any) -> Any:
    if is_dataclass(value):
        return _json_safe(asdict(value))
    if isinstance(value, Mapping):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


def _canonical_hash(value: Any) -> str:
    payload = json.dumps(
        _json_safe(value),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _text_hash(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _require_text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a non-blank string")
    return value.strip()


def _validate_identity(actor_id: str, model_id: str) -> tuple[str, str]:
    actor = _require_text(actor_id, "actor_id")
    model = _require_text(model_id, "model_id")
    return actor, model


def _arc_turns(item: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    turns = item.get("turns")
    if not isinstance(turns, list) or len(turns) != 4:
        raise ValueError("THORNS escalation_arc must contain exactly four authored turns")
    expected = list(range(1, 5))
    beats = [turn.get("beat") if isinstance(turn, Mapping) else None for turn in turns]
    if beats != expected:
        raise ValueError("THORNS escalation_arc beats must be exactly 1, 2, 3, 4")
    for index, turn in enumerate(turns, 1):
        if not isinstance(turn, Mapping):
            raise ValueError(f"turn {index} must be an object")
        _require_text(turn.get("user"), f"turn {index}.user")
    return turns


def _first_arc_message(item: Mapping[str, Any], first_turn: Mapping[str, Any]) -> str:
    context = _require_text(item.get("prompt"), "prompt")
    user = _require_text(first_turn.get("user"), "turn 1.user")
    return f"{context}\n\n[USER BEAT 1]\n{user}"


def initial_messages(item: Mapping[str, Any]) -> list[dict[str, str]]:
    """Return the first actor-visible request without flattening future arc beats."""

    item_format = item.get("format")
    if item_format == "single_shot":
        return [{"role": "user", "content": _require_text(item.get("prompt"), "prompt")}]
    if item_format == "escalation_arc":
        turns = _arc_turns(item)
        return [{"role": "user", "content": _first_arc_message(item, turns[0])}]
    raise ValueError(f"unsupported THORNS item format: {item_format!r}")


def _branch_choice(
    response_text: str,
    branches: Any,
    gold: Mapping[str, Any],
    *,
    strategy: str,
    rollout: int,
    branch_ordinal: int,
) -> tuple[str | None, str | None, str | None]:
    """Return (selected key, authored reply, stop reason)."""

    if not isinstance(branches, Mapping):
        return None, None, "malformed_branches"
    if strategy == "synthetic_marker":
        label = MarkerScorer(mode="synthetic").score(response_text, dict(gold))["label"]
        branch_key = BRANCH_BY_LABEL.get(label)
        if branch_key is None:
            return None, None, "unresolved_branch"
    elif strategy == "counterbalanced":
        branch_key = COUNTERBALANCED_BRANCHES[
            (rollout + branch_ordinal - 1) % len(COUNTERBALANCED_BRANCHES)
        ]
    else:  # validated once at executor entry; defensive for direct unit use
        raise ValueError(f"unsupported branch_strategy: {strategy!r}")
    if branch_key not in branches:
        return branch_key, None, "missing_authored_branch"
    branch_text = branches[branch_key]
    if not isinstance(branch_text, str) or not branch_text.strip():
        return branch_key, None, "malformed_authored_branch"
    return branch_key, branch_text.strip(), None


def _normalize_output(output: Any) -> dict[str, Any]:
    if not isinstance(output, Mapping):
        raise TypeError("model adapter output must be an object")
    normalized = dict(output)
    normalized["text"] = _require_text(normalized.get("text"), "adapter output text")
    normalized.setdefault("intended_path", None)
    return normalized


def _terminal_row(
    *,
    trajectory_id: str,
    item_id: str,
    actor_id: str,
    model_id: str,
    rollout: int,
    status: str,
    stop_reason: str | None,
    turn_rows: Sequence[Mapping[str, Any]],
    output: Mapping[str, Any],
    branch_strategy: str,
    surface_id: str,
    assignment_id: str | None,
) -> dict[str, Any]:
    last = turn_rows[-1]
    return {
        "row_type": "terminal",
        "trajectory_id": trajectory_id,
        "item_id": item_id,
        "surface_id": surface_id,
        "assignment_id": assignment_id,
        "actor_id": actor_id,
        "model_id": model_id,
        "rollout": rollout,
        "branch_strategy": branch_strategy,
        "status": status,
        "stop_reason": stop_reason,
        "turns_completed": len(turn_rows),
        "terminal_turn": last["turn"],
        "terminal_text": output["text"],
        "terminal_response_id": output.get("response_id"),
        "terminal_request_id": output.get("request_id"),
        "terminal_generation_id": output.get("generation_id"),
        "returned_model": output.get("returned_model"),
        "usage": _json_safe(output.get("usage") or {}),
        "attempt_ledger": _json_safe(output.get("attempt_ledger") or []),
        "intended_path": output.get("intended_path"),
        "prompt_hash": last["prompt_hash"],
        "request_hash": last["request_hash"],
    }


def execute_trajectory(
    adapter: Any,
    item: Mapping[str, Any],
    gold: Mapping[str, Any],
    *,
    actor_id: str,
    model_id: str,
    system: str | None = None,
    rollout: int = 0,
    branch_strategy: str = "synthetic_marker",
    surface_id: str | None = None,
    assignment_id: str | None = None,
) -> TrajectoryResult:
    """Execute one stateless rollout and return turn-level plus terminal evidence rows."""

    actor, requested_model = _validate_identity(actor_id, model_id)
    bound_actor = getattr(adapter, "actor_id", None)
    if bound_actor is not None and bound_actor != actor:
        raise ValueError(
            f"actor_id {actor!r} disagrees with adapter-bound actor_id {bound_actor!r}"
        )
    bound_model = getattr(adapter, "model_id", None)
    if bound_model is not None and bound_model != requested_model:
        raise ValueError(
            f"model_id {requested_model!r} disagrees with adapter-bound model_id "
            f"{bound_model!r}"
        )
    if isinstance(rollout, bool) or not isinstance(rollout, int) or rollout < 0:
        raise ValueError("rollout must be a non-negative integer")
    if branch_strategy not in BRANCH_STRATEGIES:
        raise ValueError(
            f"branch_strategy must be one of {sorted(BRANCH_STRATEGIES)}"
        )
    adapter_spec = getattr(adapter, "spec", None)
    adapter_kind = getattr(adapter_spec, "adapter", None)
    if branch_strategy == "synthetic_marker" and adapter_kind != "synthetic":
        raise ValueError(
            "synthetic_marker branch routing is synthetic-only; live trajectories "
            "must use response-independent counterbalanced branches"
        )
    item_id = _require_text(item.get("id"), "item.id")
    bound_surface = _require_text(surface_id or item_id, "surface_id")
    if assignment_id is not None:
        assignment_id = _require_text(assignment_id, "assignment_id")
    trajectory_id = "traj-" + _canonical_hash(
        {
            "actor_id": actor,
            "model_id": requested_model,
            "item_id": item_id,
            "rollout": rollout,
            "surface_id": bound_surface,
            "assignment_id": assignment_id,
        }
    )[:24]

    if item.get("format") == "single_shot":
        turns: list[Mapping[str, Any] | None] = [None]
        messages = initial_messages(item)
    elif item.get("format") == "escalation_arc":
        turns = list(_arc_turns(item))
        messages = []
    else:
        raise ValueError(f"unsupported THORNS item format: {item.get('format')!r}")

    rows: list[dict[str, Any]] = []
    last_output: dict[str, Any] | None = None
    pending_branch: dict[str, str] | None = None
    branch_ordinal = 0

    for turn_number, turn in enumerate(turns, 1):
        if item.get("format") == "escalation_arc":
            if pending_branch is not None:
                messages.append(dict(pending_branch))
                pending_branch = None
            if turn_number == 1:
                current_prompt = _first_arc_message(item, turn)  # type: ignore[arg-type]
            else:
                current_prompt = _require_text(
                    turn.get("user"), f"turn {turn_number}.user"  # type: ignore[union-attr]
                )
            messages.append({"role": "user", "content": current_prompt})
        else:
            current_prompt = messages[-1]["content"]

        request_messages = [dict(message) for message in messages]
        spec = getattr(adapter, "spec", None)
        request_hash = _canonical_hash(
            {
                "actor_id": actor,
                "model_id": requested_model,
                "adapter": getattr(spec, "adapter", type(adapter).__name__),
                "generation_params": getattr(spec, "params", {}),
                "item_id": item_id,
                "surface_id": bound_surface,
                "assignment_id": assignment_id,
                "rollout": rollout,
                "turn": turn_number,
                "branch_strategy": branch_strategy,
                "system": system,
                "messages": request_messages,
            }
        )
        output = _normalize_output(
            adapter.generate_messages(
                request_messages,
                item=dict(item),
                gold=dict(gold),
                system=system,
                rollout=rollout,
                turn=turn_number,
            )
        )
        last_output = output
        messages.append({"role": "assistant", "content": output["text"]})

        branch_selected: str | None = None
        branch_text: str | None = None
        stop_reason: str | None = None
        if (
            item.get("format") == "escalation_arc"
            and turn_number < len(turns)
            and "branches" in turn  # type: ignore[operator]
        ):
            branch_ordinal += 1
            branch_selected, branch_text, stop_reason = _branch_choice(
                output["text"],
                turn.get("branches"),  # type: ignore[union-attr]
                gold,
                strategy=branch_strategy,
                rollout=rollout,
                branch_ordinal=branch_ordinal,
            )

        row = {
            "row_type": "actor_turn",
            "trajectory_id": trajectory_id,
            "item_id": item_id,
            "surface_id": bound_surface,
            "assignment_id": assignment_id,
            "actor_id": actor,
            "model_id": requested_model,
            "rollout": rollout,
            "branch_strategy": branch_strategy,
            "turn": turn_number,
            "prompt_hash": _text_hash(current_prompt),
            "request_hash": request_hash,
            "request_messages": _json_safe(request_messages),
            "response_id": output.get("response_id"),
            "request_id": output.get("request_id"),
            "generation_id": output.get("generation_id"),
            "returned_model": output.get("returned_model"),
            "usage": _json_safe(output.get("usage") or {}),
            "attempt_ledger": _json_safe(output.get("attempt_ledger") or []),
            "response_text": output["text"],
            "intended_path": output.get("intended_path"),
            "branch_selected": branch_selected,
        }
        rows.append(row)

        if stop_reason is not None:
            terminal = _terminal_row(
                trajectory_id=trajectory_id,
                item_id=item_id,
                actor_id=actor,
                model_id=requested_model,
                rollout=rollout,
                status="stopped",
                stop_reason=stop_reason,
                turn_rows=rows,
                output=output,
                branch_strategy=branch_strategy,
                surface_id=bound_surface,
                assignment_id=assignment_id,
            )
            return TrajectoryResult(tuple(rows), terminal, output)
        if branch_text is not None:
            pending_branch = {"role": "user", "content": branch_text}

    assert last_output is not None
    terminal = _terminal_row(
        trajectory_id=trajectory_id,
        item_id=item_id,
        actor_id=actor,
        model_id=requested_model,
        rollout=rollout,
        status="completed",
        stop_reason=None,
        turn_rows=rows,
        output=last_output,
        branch_strategy=branch_strategy,
        surface_id=bound_surface,
        assignment_id=assignment_id,
    )
    return TrajectoryResult(tuple(rows), terminal, last_output)
