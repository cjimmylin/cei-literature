"""SMOKE-ONLY CLI-OAuth adapter — NOT for the validity-bearing P0 run.

The Session-A review memo's V-2 addendum PROHIBITS administering Anthropic subjects via the Claude
Code CLI (`claude -p`): no max_tokens/thinking/temperature control, no `stop_reason`, and harness
contamination (the CLI loads project/global CLAUDE.md, tools, etc. into the subject's context).

This module exists ONLY to plumb-test the pipeline end-to-end over the operator's CLI-OAuth
subscriptions without minting API keys. It is deliberately kept OUT of `runner.adapters.build_adapter`
and OUT of `run_p0.py`, so the validity-bearing run can never pick it up — `run_p0.py` continues to
administer Anthropic subjects through the SDK adapter only. Any records this produces are
SMOKE-PILOT records, not a valid measurement.

Design mirrors `OpenAICodexAdapter` (which is CLI-OAuth by design, `codex exec`): a non-zero exit is
an ADMINISTRATION error (bounded retry → RAISE fail-loud, F-1 semantics), never a refusal;
`refusal_flag` is ALWAYS False (no structured refusal signal — a content refusal is the
scorer-returns-None path).
"""
from __future__ import annotations

import shutil
import subprocess
import time
from typing import Any, Callable, List, Optional

from .adapters import AdapterResult, AdministrationError, BaseAdapter, _retry

# Loud marker so no caller mistakes this for a validity backend.
SMOKE_ONLY = True


class _CLITransient(RuntimeError):
    """Internal: a single `claude -p` attempt failed transiently (non-zero exit or timeout)."""


class AnthropicCLIAdapter(BaseAdapter):
    """SMOKE-ONLY: administer Anthropic subjects via `claude -p` (Claude Code CLI, subscription
    OAuth — no API key). No sampling/thinking/stop_reason control (V-2), so those kwargs are
    absorbed and ignored. `runner` is injectable (subprocess.run-shaped) so tests mock the
    subprocess — NO live calls in the test suite."""

    vendor = "anthropic"

    def __init__(
        self,
        claude_bin: Optional[str] = None,
        runner: Optional[Callable[..., Any]] = None,
        timeout: float = 120.0,
        cwd: str = "/tmp",
        output_format: str = "text",
        max_retries: int = 2,
        backoff_base: float = 0.5,
        sleep: Optional[Callable[[float], None]] = None,
    ):
        self._runner = runner or subprocess.run
        self._explicit_bin = claude_bin
        self._timeout = timeout
        # Run from a neutral cwd (no project CLAUDE.md) to reduce — not eliminate — the V-2 harness
        # contamination; the global ~/.claude/CLAUDE.md still loads, which is why this is smoke-only.
        self._cwd = cwd
        self._output_format = output_format
        self._max_retries = max_retries
        self._backoff_base = backoff_base
        self._sleep = sleep or time.sleep

    @property
    def claude_bin(self) -> Optional[str]:
        return self._explicit_bin or shutil.which("claude")

    def available(self) -> bool:
        return self.claude_bin is not None

    def build_command(self, model_id: str, prompt: str) -> List[str]:
        # `claude -p <prompt> --model <id> --output-format text` — one-shot print mode.
        return [
            self.claude_bin or "claude",
            "-p",
            prompt,
            "--model",
            model_id,
            "--output-format",
            self._output_format,
        ]

    def administer(
        self,
        prompt: str,
        model_id: str,
        temperature: float,
        seed: int,
        system: Optional[str] = None,
        **_: Any,   # absorbs omit_sampling_params / thinking / max_tokens — no CLI control (V-2)
    ) -> AdapterResult:
        if not self.available():
            raise RuntimeError(
                "claude CLI not found on PATH — Anthropic CLI (smoke) adapter unavailable. "
                "Log in to Claude Code (subscription OAuth) before the smoke."
            )
        full_prompt = prompt if not system else (system + "\n\n" + prompt)

        def _attempt() -> AdapterResult:
            cmd = self.build_command(model_id, full_prompt)
            try:
                proc = self._runner(
                    cmd, capture_output=True, text=True, timeout=self._timeout, cwd=self._cwd,
                )
            except subprocess.TimeoutExpired as e:
                raise _CLITransient(f"claude -p timed out after {self._timeout}s") from e
            returncode = getattr(proc, "returncode", 0)
            text = (getattr(proc, "stdout", "") or "").strip()
            if returncode != 0:
                # A non-zero exit is an ADMINISTRATION error (auth/CLI crash), not a model refusal
                # (F-1 / SA-5 semantics). Retry; on persistent failure _retry raises fail-loud.
                raise _CLITransient(
                    f"claude -p returncode={returncode}: "
                    f"{(getattr(proc, 'stderr', '') or '')[:500]}"
                )
            raw = {
                "cmd": cmd,
                "returncode": returncode,
                "stderr": getattr(proc, "stderr", ""),
                "smoke_only": True,
                "backend": "claude -p",
            }
            # No structured refusal signal (no stop_reason) → refusal_flag ALWAYS False.
            return AdapterResult(text=text, raw=raw, refusal_flag=False, latency=0.0)

        t0 = time.monotonic()
        result = _retry(
            _attempt, max_retries=self._max_retries, backoff_base=self._backoff_base,
            sleep=self._sleep, is_transient=lambda e: isinstance(e, _CLITransient),
            vendor=self.vendor,
        )
        result.latency = time.monotonic() - t0
        return result
