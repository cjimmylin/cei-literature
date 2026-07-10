"""Subprocess-backed live model clients for the O3 mechanics SMOKE.

Two thin `ModelClient` backends that shell out to the vendors' *subscription*
CLIs — NO API key, NO SDK:

  - `ClaudeCLIClient`  -> `claude -p` (Claude Code subscription OAuth). Prints the
    final text to stdout. family = "anthropic".
  - `CodexCLIClient`   -> `codex exec` (Codex / ChatGPT subscription OAuth). Writes
    the final agent message to a `--output-last-message` file (stdout is agent
    activity noise). family = "openai".

These are DISTINCT from `clients.AnthropicAdapter` / `OpenAIAdapter` (the keyed SDK
stubs), which stay deferred to the sanctioned Developer-Platform API path (O4).

ToS: subscription-CLI automation is defensible ONLY at smoke scale. The measurement
path (full P0 pilot + O4 panel) must use the sanctioned API on both vendors.

Validity caveats (documented, not fixed — this is a smoke):
  - `claude -p` runs inside the Claude Code default frame unless `--system-prompt`
    REPLACES it; we replace when a system prompt is given, but tool-availability
    framing is not fully stripped. A clean measurement wants the bare SDK
    `/v1/messages` call (README auth table).
  - Multi-turn is flattened into a single rendered transcript per `complete()` call
    (the executor drives turn-by-turn and hands us the growing history). This loses
    true multi-turn API state; O4 should use `--resume`/stream-json or the SDK.
  - NEVER send temperature/top_p/top_k — Opus 4.7+/Fable 400 on them (adaptive
    thinking only); decoding is pinned via the prompt.
"""
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path
from typing import Callable, List, Optional

from .clients import Message, ModelClient, ModelResponse


class ModelCallError(RuntimeError):
    """A live CLI call failed (nonzero exit, timeout, or empty output)."""


# --------------------------------------------------------------------------- #
# conversation rendering (system handled per-backend, NOT here)
# --------------------------------------------------------------------------- #
_ROLE_LABEL = {"user": "User", "assistant": "Assistant"}
_CONTINUE_INSTRUCTION = (
    "Continue the following conversation as the Assistant. Reply to the final "
    "User message only; do not repeat prior turns.\n\n"
)


def render_conversation(messages: List[Message]) -> str:
    """Flatten a message list into one prompt string (no system frame).

    A lone user message is passed verbatim; a multi-turn history is rendered as a
    labeled transcript ending on the final User turn.
    """
    if len(messages) == 1 and messages[0].role == "user":
        return messages[0].content
    lines = [_CONTINUE_INSTRUCTION.rstrip("\n")]
    lines.append("")
    for m in messages:
        label = _ROLE_LABEL.get(m.role, m.role.capitalize())
        lines.append(f"{label}: {m.content}")
    return "\n".join(lines)


def _default_runner(argv: List[str], timeout: Optional[float] = None):
    """Real subprocess runner. Injected fakes replace this in tests."""
    return subprocess.run(argv, capture_output=True, text=True, timeout=timeout)


Runner = Callable[..., object]


# --------------------------------------------------------------------------- #
# Claude family — `claude -p`
# --------------------------------------------------------------------------- #
class ClaudeCLIClient(ModelClient):
    family = "anthropic"

    def __init__(self, name: str, model: str = "sonnet", binary: str = "claude",
                 timeout: float = 180.0, runner: Optional[Runner] = None):
        super().__init__(name)
        self.model = model
        self.binary = binary
        self.timeout = timeout
        self._runner = runner or _default_runner

    def build_argv(self, prompt: str, system: Optional[str]) -> List[str]:
        argv = [self.binary, "-p", prompt, "--model", self.model]
        if system:
            # REPLACE the default Claude Code frame (not --append) for a cleaner smoke.
            argv += ["--system-prompt", system]
        return argv  # deliberately NO temperature/top_p/top_k

    def complete(self, messages: List[Message], system: Optional[str] = None,
                 **kwargs) -> ModelResponse:
        prompt = render_conversation(messages)
        argv = self.build_argv(prompt, system)
        try:
            proc = self._runner(argv, timeout=self.timeout)
        except subprocess.TimeoutExpired as e:  # pragma: no cover - live-only path
            raise ModelCallError(f"{self.binary} -p timed out after {self.timeout}s") from e
        if getattr(proc, "returncode", 1) != 0:
            raise ModelCallError(
                f"{self.binary} -p exited {proc.returncode}: "
                f"{(getattr(proc, 'stderr', '') or '')[:400]}"
            )
        text = (getattr(proc, "stdout", "") or "").strip()
        if not text:
            raise ModelCallError(f"{self.binary} -p returned empty output")
        return ModelResponse(text=text, model=self.model, family=self.family,
                             raw={"backend": "claude-cli", "argv0": self.binary})


# --------------------------------------------------------------------------- #
# GPT family — `codex exec`
# --------------------------------------------------------------------------- #
class CodexCLIClient(ModelClient):
    family = "openai"

    def __init__(self, name: str, model: Optional[str] = None, binary: str = "codex",
                 timeout: float = 300.0, runner: Optional[Runner] = None,
                 workdir: Optional[str] = None):
        super().__init__(name)
        self.model = model
        self.binary = binary
        self.timeout = timeout
        self.workdir = workdir
        self._runner = runner or _default_runner

    def build_argv(self, prompt: str, out_path: str) -> List[str]:
        argv = [self.binary, "exec", prompt,
                "--skip-git-repo-check", "-s", "read-only", "--color", "never",
                "--output-last-message", out_path]
        if self.model:
            argv += ["-m", self.model]
        if self.workdir:
            argv += ["-C", self.workdir]
        return argv  # deliberately NO temperature/top_p/top_k

    def complete(self, messages: List[Message], system: Optional[str] = None,
                 **kwargs) -> ModelResponse:
        prompt = render_conversation(messages)
        if system:
            # codex exec has no system flag; the frame rides inside the prompt.
            prompt = (f"System instructions (follow these strictly):\n{system}\n\n"
                      f"{prompt}")
        with tempfile.TemporaryDirectory(prefix="wcf_codex_") as td:
            out_path = str(Path(td) / "last_message.txt")
            argv = self.build_argv(prompt, out_path)
            try:
                proc = self._runner(argv, timeout=self.timeout)
            except subprocess.TimeoutExpired as e:  # pragma: no cover - live-only path
                raise ModelCallError(
                    f"{self.binary} exec timed out after {self.timeout}s") from e
            if getattr(proc, "returncode", 1) != 0:
                raise ModelCallError(
                    f"{self.binary} exec exited {proc.returncode}: "
                    f"{(getattr(proc, 'stderr', '') or '')[:400]}"
                )
            text = ""
            if Path(out_path).exists():
                text = Path(out_path).read_text(encoding="utf-8").strip()
        if not text:
            raise ModelCallError(f"{self.binary} exec produced no final message")
        return ModelResponse(text=text, model=self.model or "codex-default",
                             family=self.family,
                             raw={"backend": "codex-cli", "argv0": self.binary})
