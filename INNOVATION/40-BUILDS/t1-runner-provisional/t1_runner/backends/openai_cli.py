"""OpenAI backend via ``codex exec`` headless (ChatGPT-account OAuth).

Empirically-derived invocation (see 20260709-cli-bringup-log.md):
    codex exec --json --skip-git-repo-check --sandbox read-only \
        -C <workdir> -o <lastfile> PROMPT </dev/null

- do NOT pass -m: explicit model ids (e.g. gpt-5) are rejected 400 on a ChatGPT
  account; let it use the account default (config: gpt-5.5).
- stdin=DEVNULL (codex otherwise appends stdin and can hang).
- --output-last-message writes the clean final text to a file.
- --json stream: {"type":"item.completed","item":{"type":"agent_message","text":...}}
  is the answer; {"type":"turn.failed"|"error"} means a failure.
"""

from __future__ import annotations

import json
import os
import subprocess
import tempfile
import time
from typing import Optional

from ..core import (ModelRequest, ModelResponse, ResponseStatus, RunnerBackend,
                    classify_refusal)

# Config default recorded as authoritative model id (prose self-report unreliable).
DEFAULT_MODEL_ID = "gpt-5.5"

_RATE_LIMIT_MARKERS = ("rate limit", "429", "too many requests", "quota")


class OpenAICLIBackend(RunnerBackend):
    name = "openai_cli"

    def __init__(self, model_id: str = DEFAULT_MODEL_ID, cli_path: str = "codex",
                 workdir: Optional[str] = None, runner=None):
        self.model_id = model_id
        self.cli_path = cli_path
        self.workdir = workdir or tempfile.gettempdir()
        self._runner = runner or self._real_run

    def cli_version(self) -> str:
        try:
            out = subprocess.run([self.cli_path, "--version"], capture_output=True,
                                 text=True, timeout=30)
            version = out.stdout.strip() or out.stderr.strip() or "unknown"
        except Exception as exc:  # pragma: no cover
            version = f"unknown ({exc})"
        self._cached_version = version
        return version

    def _build_argv(self, request: ModelRequest, last_file: str) -> list[str]:
        # Deliberately NO -m (see module docstring).
        return [self.cli_path, "exec", "--json", "--skip-git-repo-check",
                "--sandbox", "read-only", "-C", self.workdir,
                "-o", last_file, request.prompt]

    def _real_run(self, argv, timeout):
        return subprocess.run(argv, capture_output=True, text=True,
                              timeout=timeout, stdin=subprocess.DEVNULL)

    def run(self, request: ModelRequest, timeout_s: float) -> ModelResponse:
        version = getattr(self, "_cached_version", "")
        last_fd, last_file = tempfile.mkstemp(prefix="codex_last_", suffix=".txt")
        os.close(last_fd)
        argv = self._build_argv(request, last_file)
        start = time.time()
        try:
            proc = self._runner(argv, timeout_s)
        except subprocess.TimeoutExpired:
            self._safe_read_and_forget(last_file)
            return ModelResponse(
                text="", status=ResponseStatus.TIMEOUT, backend=self.name,
                model_id_reported=self.model_id, cli_version=version,
                latency_s=time.time() - start, request=request, argv=argv,
                error_detail=f"subprocess timeout after {timeout_s}s")
        latency = time.time() - start
        raw = proc.stdout or ""
        last_msg = self._safe_read_and_forget(last_file)
        return self._parse(request, argv, raw, proc.stderr or "",
                           proc.returncode, latency, version, last_msg)

    @staticmethod
    def _safe_read_and_forget(path) -> Optional[str]:
        try:
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as fh:
                    content = fh.read()
                os.remove(path)  # os.remove of a private tmp scratch file (not vault data)
                return content
        except Exception:
            return None
        return None

    def _parse(self, request, argv, raw, stderr, returncode, latency, version,
               last_msg) -> ModelResponse:
        # Detect explicit failure events first.
        failed = False
        error_detail = ""
        agent_texts = []
        for line in raw.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                evt = json.loads(line)
            except Exception:
                continue
            etype = evt.get("type")
            if etype == "error" or etype == "turn.failed":
                failed = True
                error_detail = json.dumps(evt.get("message") or evt.get("error") or evt)
            elif etype == "item.completed":
                item = evt.get("item", {})
                if item.get("type") == "agent_message" and item.get("text"):
                    agent_texts.append(item["text"])

        text = (last_msg or "").strip() or ("\n".join(agent_texts)).strip()

        if failed:
            low = error_detail.lower()
            status = ResponseStatus.ERROR
            return ModelResponse(
                text=text, status=status, backend=self.name,
                model_id_reported=self.model_id, cli_version=version,
                latency_s=latency, request=request, argv=argv, raw_output=raw,
                error_detail=error_detail[:600])

        if not text:
            return ModelResponse(
                text="", status=ResponseStatus.PARSE_FAILURE, backend=self.name,
                model_id_reported=self.model_id, cli_version=version,
                latency_s=latency, request=request, argv=argv, raw_output=raw,
                error_detail=f"no agent_message/last-message; returncode={returncode}; "
                             f"stderr={stderr[:300]}")

        status = ResponseStatus.REFUSAL if classify_refusal(text) else ResponseStatus.OK
        return ModelResponse(
            text=text, status=status, backend=self.name,
            model_id_reported=self.model_id, cli_version=version,
            latency_s=latency, request=request, argv=argv, raw_output=raw)
