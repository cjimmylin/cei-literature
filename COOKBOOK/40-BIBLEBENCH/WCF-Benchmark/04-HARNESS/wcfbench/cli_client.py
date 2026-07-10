"""CLIModelClient — a REAL model backend via the Claude Code CLI (subscription OAuth).

This is the first real implementation of the `MockModelClient` seam (README "the
mock-first contract"). It shells out to the `claude` CLI in headless mode
(`claude -p ... --output-format json`), so it uses the machine's existing
subscription OAuth login — **no Anthropic API key required** (probe confirmed
`apiKeySource: none`). It exposes the exact same method the scorers/runner call:

    client = CLIModelClient(model="claude-haiku-4-5-20251001")
    text = client.complete("Rank these ...", item_id="AGG-C6-W301")

HONESTY CAVEATS (read before trusting ANY number this produces):
  * **Terms of service.** Subscription OAuth is intended for *ordinary individual*
    use; Anthropic's terms steer bulk/automated evaluation to API-key auth. Keep
    CLI-OAuth to small SMOKE PILOTS / harness bring-up; the real gated run wants
    the Messages API (also for the two reasons below).
  * **No sampling control.** The CLI exposes no temperature/seed flag — not
    reproducible at API grade.
  * **Per-call overhead + context leakage.** Claude Code injects a system prompt
    (~10k cache-creation tokens), so even a trivial call costs ~$0.02 AND the
    system prompt loads the project's CLAUDE.md. This client therefore runs from a
    CLEAN cwd (no CLAUDE.md) so the vault's memory does not steer the model.

This module uses `subprocess` (a process boundary), NOT a network SDK — the core
scorers / tensor / perturbation / refusal modules stay import-clean. Nothing here
runs during the test suite unless explicitly invoked (tests monkeypatch
`subprocess.run`; no real calls in CI).
"""

from __future__ import annotations

import json
import os
import subprocess
import tempfile
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

#: Cheap default for smoke pilots. Always pin a FULL model id (aliases like
#: "haiku"/"opus" float to the newest in-family and silently change what you
#: measure — bad for a benchmark).
DEFAULT_MODEL = "claude-haiku-4-5-20251001"

#: Single-turn hygiene flags, verified against claude 2.1.183: no built-in tools,
#: zero MCP servers, no settings/hooks/skills leakage, exactly one turn, and never
#: pause for a permission prompt. This makes `-p` behave like a clean chat turn
#: (measuring the model, not an agent loop).
_HYGIENE_FLAGS: Tuple[str, ...] = (
    "--tools", "",
    "--strict-mcp-config",
    "--permission-mode", "dontAsk",
    "--max-turns", "1",
    "--setting-sources", "",
)


class CLIClientError(RuntimeError):
    """Raised when the claude CLI call fails, errors, times out, or returns no result."""


@dataclass
class CLIModelClient:
    """Drives the `claude` CLI headless as a single-turn completion backend.

    Interface-compatible with ``MockModelClient`` — the scorers and the
    perturbation runner only ever call ``.complete(prompt, item_id=None) -> str``.
    """

    model: str = DEFAULT_MODEL
    timeout_s: float = 180.0
    binary: str = "claude"
    cwd: Optional[str] = None          # default: a neutral, CLAUDE.md-free temp dir
    force_oauth: bool = True           # unset ANTHROPIC_API_KEY so subscription OAuth is used
    _calls: int = field(default=0, init=False, repr=False)
    _cost_usd: float = field(default=0.0, init=False, repr=False)

    # -- environment / working dir -----------------------------------------
    def _env(self) -> Dict[str, str]:
        env = dict(os.environ)
        if self.force_oauth:
            # These would switch billing to API pay-as-you-go; drop them so the
            # subscription OAuth login (apiKeySource: none) is used instead.
            env.pop("ANTHROPIC_API_KEY", None)
            env.pop("ANTHROPIC_AUTH_TOKEN", None)
        return env

    def _resolve_cwd(self) -> str:
        if self.cwd:
            return self.cwd
        clean = os.path.join(tempfile.gettempdir(), "wcfbench-cli-clean")
        os.makedirs(clean, exist_ok=True)
        return clean

    # -- the seam ----------------------------------------------------------
    def complete(self, prompt: str, item_id: Optional[str] = None) -> str:
        """Run one headless `claude -p` turn and return the completion text."""
        cmd: List[str] = [
            self.binary, "-p", prompt,
            "--model", self.model,
            "--output-format", "json",
            *_HYGIENE_FLAGS,
        ]
        try:
            proc = subprocess.run(
                cmd, capture_output=True, text=True,
                timeout=self.timeout_s, cwd=self._resolve_cwd(), env=self._env(),
            )
        except subprocess.TimeoutExpired as exc:
            raise CLIClientError(
                f"claude CLI timed out after {self.timeout_s}s for item {item_id!r}"
            ) from exc
        except OSError as exc:  # binary missing, etc.
            raise CLIClientError(f"could not invoke {self.binary!r}: {exc}") from exc

        self._calls += 1
        if proc.returncode != 0:
            raise CLIClientError(
                f"claude CLI exited {proc.returncode} for item {item_id!r}: "
                f"{(proc.stderr or '').strip()[:400]}"
            )
        text, cost = self._parse_result(proc.stdout)
        self._cost_usd += cost
        return text

    # -- output parsing ----------------------------------------------------
    @staticmethod
    def _parse_result(stdout: str) -> Tuple[str, float]:
        """Extract (result_text, cost_usd) from `--output-format json` stdout.

        The CLI returns EITHER a single result object OR (observed on 2.1.183) a
        JSON array of stream events whose final ``type == "result"`` element
        carries the answer in ``.result`` and the cost in ``.total_cost_usd``.
        """
        stdout = (stdout or "").strip()
        if not stdout:
            raise CLIClientError("claude CLI produced empty stdout")
        try:
            data = json.loads(stdout)
        except json.JSONDecodeError as exc:
            raise CLIClientError(f"claude CLI stdout was not valid JSON: {exc}") from exc

        events = data if isinstance(data, list) else [data]
        for ev in reversed(events):
            if isinstance(ev, dict) and ev.get("type") == "result":
                if ev.get("is_error"):
                    raise CLIClientError(
                        f"claude CLI result error: {ev.get('subtype')}/{ev.get('api_error_status')}"
                    )
                return str(ev.get("result", "")), float(ev.get("total_cost_usd") or 0.0)
        # a bare result object with no event wrapper
        if isinstance(data, dict) and "result" in data:
            return str(data["result"]), float(data.get("total_cost_usd") or 0.0)
        raise CLIClientError("no `type: result` element found in claude CLI json output")

    # -- bookkeeping -------------------------------------------------------
    @property
    def calls_made(self) -> int:
        return self._calls

    @property
    def cost_usd(self) -> float:
        return round(self._cost_usd, 6)

    @classmethod
    def check_available(cls, binary: str = "claude") -> bool:
        """True if the `claude` CLI is invocable (does not make a model call)."""
        try:
            proc = subprocess.run(
                [binary, "--version"], capture_output=True, text=True, timeout=15,
            )
            return proc.returncode == 0
        except (OSError, subprocess.SubprocessError):
            return False
