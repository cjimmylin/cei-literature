"""
act_sandbox.py — Minimal-tool sandbox for the M-ACT modality.

M-ACT embeds the same decision in an agentic harness: the model executes an action
(send / schedule / allocate / publish and the per-core tools) with real consequences
*within the sandbox* (brief §2, §4). The sandbox:
  * exposes the core's declared tools,
  * "executes" a tool call by recording it to a transcript and mutating a local fake state
    (NEVER a real side effect — no network, no filesystem writes outside the run dir),
  * flags the monitored/unmonitored condition (Law 6 comparator),
  * returns the transcript for scoring/action_classifier.py to classify into a pole.

The executed-action record is deliberately model-agnostic: a real tool-use loop and the
MockModelClient both land here as a declared tool plus its complete structured arguments.
The legacy ``body`` field is retained only as a canonical JSON compatibility view of args.
"""
from __future__ import annotations

import copy
import json
from dataclasses import dataclass, field
from typing import Any

from complexity import ToolDeclarationError, parse_tool_declarations


class ToolContractError(ValueError):
    """A proposed ACT call does not satisfy the rendered item's declared contract."""


def _contains_canary(value: Any, canary: str) -> bool:
    """Return whether a canary occurs in any nested argument value."""
    if isinstance(value, dict):
        return any(_contains_canary(nested, canary) for nested in value.values())
    if isinstance(value, (list, tuple)):
        return any(_contains_canary(nested, canary) for nested in value)
    return canary in str(value)


@dataclass
class ExecutedAction:
    tool: str
    args: dict[str, Any]
    body: str                       # canonical JSON compatibility view of complete args
    step: int


@dataclass
class SandboxResult:
    core_id: str
    item_id: str
    monitored: bool
    actions: list[ExecutedAction] = field(default_factory=list)
    canary_seen: bool = False

    @property
    def primary(self) -> ExecutedAction | None:
        """The action the classifier scores (last substantive action in the transcript)."""
        return self.actions[-1] if self.actions else None

    def to_record(self) -> dict[str, Any]:
        return {
            "core_id": self.core_id,
            "item_id": self.item_id,
            "monitored": self.monitored,
            "actions": [vars(a) for a in self.actions],
            "canary_seen": self.canary_seen,
        }


class ActSandbox:
    """A single-episode sandbox for one ACT item."""

    def __init__(self, item: dict[str, Any], monitored: bool = True):
        self.item = item
        self.tools = item.get("tools", [])
        try:
            declarations = parse_tool_declarations(self.tools)
        except ToolDeclarationError as exc:
            raise ToolContractError(f"invalid item tool contract: {exc}") from exc
        self._contracts = {declaration.name: declaration for declaration in declarations}
        self.result = SandboxResult(
            core_id=item["core_id"], item_id=item["item_id"], monitored=monitored,
        )
        self._step = 0

    def available_tools(self) -> list[str]:
        return list(self.tools)

    def _prepare_call(self, tool: str, args: dict[str, Any]) -> tuple[str, dict[str, Any], str]:
        """Validate and copy one call without mutating episode state."""
        if not isinstance(tool, str) or tool not in self._contracts:
            raise ToolContractError(f"undeclared tool call: {tool!r}")
        if not isinstance(args, dict):
            raise ToolContractError(
                f"arguments for {tool!r} must be a mapping, got {type(args).__name__}"
            )
        expected = self._contracts[tool].args
        actual = tuple(args)
        missing = [name for name in expected if name not in args]
        extra = [name for name in actual if name not in expected]
        if missing or extra:
            raise ToolContractError(
                f"arguments for {tool!r} do not match declaration; "
                f"missing={missing}, extra={extra}"
            )
        try:
            body = json.dumps(args, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        except (TypeError, ValueError) as exc:
            raise ToolContractError(f"arguments for {tool!r} must be JSON-serializable") from exc
        recorded_args = copy.deepcopy(args)
        return tool, recorded_args, body

    def _commit_prepared(
        self, prepared: list[tuple[str, dict[str, Any], str]]
    ) -> None:
        """Commit calls that have already passed the complete trajectory gate."""
        canary = self.item.get("canary")
        for tool, recorded_args, body in prepared:
            self._step += 1
            self.result.actions.append(ExecutedAction(
                tool=tool, args=recorded_args, body=body, step=self._step,
            ))
            if canary and _contains_canary(recorded_args, str(canary)):
                self.result.canary_seen = True

    def execute(self, tool: str, args: dict[str, Any]) -> dict[str, Any]:
        """Validate, record, and simulate one call without external side effects."""
        self.execute_trajectory([{"tool": tool, "args": args}])
        return {"ok": True, "tool": tool, "step": self._step}

    def execute_trajectory(self, actions: list[dict[str, Any]]) -> SandboxResult:
        """Validate a complete ordered trajectory, then commit it atomically.

        No transcript, step, or canary state changes unless every proposed call has a
        declared tool, an exact argument shape, and a serializable payload.
        """
        if not isinstance(actions, list) or not actions:
            raise ToolContractError("ACT trajectory must be a non-empty list")
        prepared: list[tuple[str, dict[str, Any], str]] = []
        for index, action in enumerate(actions):
            if not isinstance(action, dict):
                raise ToolContractError(
                    f"ACT trajectory action[{index}] must be a mapping, "
                    f"got {type(action).__name__}"
                )
            missing = [field for field in ("tool", "args") if field not in action]
            extra = [field for field in action if field not in {"tool", "args"}]
            if missing or extra:
                raise ToolContractError(
                    f"ACT trajectory action[{index}] fields do not match contract; "
                    f"missing={missing}, extra={extra}"
                )
            prepared.append(self._prepare_call(action["tool"], action["args"]))

        self._commit_prepared(prepared)
        return self.result

    def run_response(self, response) -> SandboxResult:
        """Drive one ordered-trajectory ModelResponse."""
        raw = response.raw
        if not isinstance(raw, dict):
            raise ToolContractError(
                f"ACT response must be a mapping, got {type(raw).__name__}"
            )
        if "actions" not in raw:
            raise ToolContractError("ACT response is missing required field 'actions'")
        extra = [field for field in raw if field != "actions"]
        if extra:
            raise ToolContractError(f"ACT response has unexpected field(s): {extra}")
        return self.execute_trajectory(raw["actions"])

    def run_single(self, response) -> SandboxResult:
        """Drive exactly one call (legacy helper retained for strict control episodes)."""
        raw = response.raw
        if not isinstance(raw, dict):
            raise ToolContractError(
                f"ACT response must be a mapping, got {type(raw).__name__}"
            )
        if "actions" in raw:
            actions = raw["actions"]
            if not isinstance(actions, list) or len(actions) != 1:
                raise ToolContractError("single-call ACT response must contain exactly one action")
            extra = [field for field in raw if field != "actions"]
            if extra:
                raise ToolContractError(f"ACT response has unexpected field(s): {extra}")
            return self.execute_trajectory(actions)
        try:
            action = {"tool": raw["tool"], "args": raw["args"]}
        except KeyError as exc:
            raise ToolContractError(
                f"ACT response is missing required field {exc.args[0]!r}"
            ) from exc
        extra = [field for field in raw if field not in {"tool", "args"}]
        if extra:
            raise ToolContractError(f"ACT response has unexpected field(s): {extra}")
        return self.execute_trajectory([action])
