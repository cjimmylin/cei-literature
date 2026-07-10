"""Anthropic backend via ``claude -p`` headless (subscription OAuth).

Empirically-derived invocation (see 20260709-cli-bringup-log.md):
    claude -p PROMPT --model <alias> --output-format json </dev/null

- inherited env (env -i breaks subscription auth)
- stdin=DEVNULL so a closed/piped stdin never hangs
- output is a JSON *array* of events; the last object has type=="result"
- text = result.result ; is_error = result.is_error
- model id = the sole key of result.modelUsage (authoritative resolved id)
"""

from __future__ import annotations

import json
import subprocess
import time
from typing import Optional

from ..core import (ModelRequest, ModelResponse, ResponseStatus, RunnerBackend,
                    classify_refusal)

_NOT_LOGGED_IN_MARKERS = ("not logged in", "please run /login")


class AnthropicCLIBackend(RunnerBackend):
    name = "anthropic_cli"

    def __init__(self, model_alias: str = "opus", cli_path: str = "claude",
                 runner=None):
        self.model_alias = model_alias
        self.cli_path = cli_path
        # ``runner`` injectable for tests: a callable(argv, timeout) ->
        # subprocess.CompletedProcess-like (has returncode, stdout, stderr).
        self._runner = runner or self._real_run

    def cli_version(self) -> str:
        try:
            out = subprocess.run([self.cli_path, "--version"], capture_output=True,
                                 text=True, timeout=30)
            version = out.stdout.strip() or out.stderr.strip() or "unknown"
        except Exception as exc:  # pragma: no cover - defensive
            version = f"unknown ({exc})"
        self._cached_version = version
        return version

    def _build_argv(self, request: ModelRequest) -> list[str]:
        model = request.params.get("model", self.model_alias)
        argv = [self.cli_path, "-p", request.prompt, "--model", model,
                "--output-format", "json"]
        if request.system:
            argv += ["--append-system-prompt", request.system]
        return argv

    def _real_run(self, argv, timeout):
        return subprocess.run(argv, capture_output=True, text=True,
                              timeout=timeout, stdin=subprocess.DEVNULL)

    def run(self, request: ModelRequest, timeout_s: float) -> ModelResponse:
        argv = self._build_argv(request)
        version = getattr(self, "_cached_version", None)
        start = time.time()
        try:
            proc = self._runner(argv, timeout_s)
        except subprocess.TimeoutExpired:
            return ModelResponse(
                text="", status=ResponseStatus.TIMEOUT, backend=self.name,
                model_id_reported=request.params.get("model", self.model_alias),
                cli_version=version or "", latency_s=time.time() - start,
                request=request, argv=argv, raw_output="",
                error_detail=f"subprocess timeout after {timeout_s}s")
        latency = time.time() - start
        raw = proc.stdout or ""
        return self._parse(request, argv, raw, proc.stderr or "",
                           proc.returncode, latency, version or "")

    def _parse(self, request, argv, raw, stderr, returncode, latency,
               version) -> ModelResponse:
        model_fallback = request.params.get("model", self.model_alias)
        try:
            data = json.loads(raw)
        except Exception as exc:
            return ModelResponse(
                text="", status=ResponseStatus.PARSE_FAILURE, backend=self.name,
                model_id_reported=model_fallback, cli_version=version,
                latency_s=latency, request=request, argv=argv, raw_output=raw,
                error_detail=f"json parse failed: {exc}; stderr={stderr[:400]}")

        result_obj = None
        if isinstance(data, list):
            for obj in reversed(data):
                if isinstance(obj, dict) and obj.get("type") == "result":
                    result_obj = obj
                    break
        elif isinstance(data, dict):
            result_obj = data
        if result_obj is None:
            return ModelResponse(
                text="", status=ResponseStatus.PARSE_FAILURE, backend=self.name,
                model_id_reported=model_fallback, cli_version=version,
                latency_s=latency, request=request, argv=argv, raw_output=raw,
                error_detail="no result object in claude json array")

        text = result_obj.get("result", "") or ""
        model_usage = result_obj.get("modelUsage") or {}
        model_id = next(iter(model_usage.keys()), model_fallback)

        low = text.lower()
        if result_obj.get("is_error") or any(m in low for m in _NOT_LOGGED_IN_MARKERS):
            return ModelResponse(
                text=text, status=ResponseStatus.ERROR, backend=self.name,
                model_id_reported=model_id, cli_version=version,
                latency_s=latency, request=request, argv=argv, raw_output=raw,
                error_detail=f"is_error/auth; returncode={returncode}")

        status = ResponseStatus.REFUSAL if classify_refusal(text) else ResponseStatus.OK
        return ModelResponse(
            text=text, status=status, backend=self.name,
            model_id_reported=model_id, cli_version=version, latency_s=latency,
            request=request, argv=argv, raw_output=raw,
            self_reported_model="")
