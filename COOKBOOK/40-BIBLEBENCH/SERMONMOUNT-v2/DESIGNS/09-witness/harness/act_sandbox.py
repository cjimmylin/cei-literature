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
MockModelClient both land here as {tool, args, body}.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ExecutedAction:
    tool: str
    args: dict[str, Any]
    body: str                       # free-text payload of the action (what was said/done)
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
        self.result = SandboxResult(
            core_id=item["core_id"], item_id=item["item_id"], monitored=monitored,
        )
        self._step = 0

    def available_tools(self) -> list[str]:
        return list(self.tools)

    def execute(self, tool: str, args: dict[str, Any]) -> dict[str, Any]:
        """Record and 'perform' a tool call. Returns a benign result dict."""
        body = str(args.get("body", ""))
        self._step += 1
        self.result.actions.append(ExecutedAction(tool=tool, args=dict(args),
                                                   body=body, step=self._step))
        # canary check: the prompt embeds a canary; a well-behaved run never emits it.
        if self.item.get("canary") and self.item["canary"] in body:
            self.result.canary_seen = True
        return {"ok": True, "tool": tool, "step": self._step}

    def run_single(self, response) -> SandboxResult:
        """Drive one ModelResponse (single-action episode used by the P1 harness)."""
        raw = response.raw
        self.execute(raw.get("tool", "noop"), raw.get("args", {}))
        return self.result
