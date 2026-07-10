"""Google backend via ``gemini`` headless (OAuth).

Empirically-derived invocation (see 20260709-cli-bringup-log.md):
    gemini --skip-trust -o json -p PROMPT </dev/null

STATUS ON THIS ACCOUNT (2026-07-09): BROKEN.
    IneligibleTierError: This client is no longer supported for Gemini Code
    Assist for individuals. Migrate to Antigravity.
The OAuth cred exists but the Code Assist "individuals" tier is server-side
deprecated; no flag recovers it. This backend is fully implemented (drop-in
ready) but is NOT registered by default. If the account is re-provisioned it
will work; when an API key lands a proper google_api backend supersedes it.

Gemini --output-format json returns a single JSON object with a "response"
field (schema per CLI version); we read that, else fall back to raw text.
"""

from __future__ import annotations

import json
import subprocess
import time
from typing import Optional

from ..core import (ModelRequest, ModelResponse, ResponseStatus, RunnerBackend,
                    classify_refusal)

_INELIGIBLE_MARKERS = ("ineligibletiererror", "no longer supported",
                        "migrate to the antigravity")


class GoogleCLIBackend(RunnerBackend):
    name = "google_cli"

    def __init__(self, model_id: str = "gemini-default", cli_path: str = "gemini",
                 runner=None):
        self.model_id = model_id
        self.cli_path = cli_path
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

    def _build_argv(self, request: ModelRequest) -> list[str]:
        argv = [self.cli_path, "--skip-trust", "-o", "json", "-p", request.prompt]
        model = request.params.get("model")
        if model:
            argv += ["-m", model]
        return argv

    def _real_run(self, argv, timeout):
        return subprocess.run(argv, capture_output=True, text=True,
                              timeout=timeout, stdin=subprocess.DEVNULL)

    def run(self, request: ModelRequest, timeout_s: float) -> ModelResponse:
        version = getattr(self, "_cached_version", "")
        argv = self._build_argv(request)
        start = time.time()
        try:
            proc = self._runner(argv, timeout_s)
        except subprocess.TimeoutExpired:
            return ModelResponse(
                text="", status=ResponseStatus.TIMEOUT, backend=self.name,
                model_id_reported=self.model_id, cli_version=version,
                latency_s=time.time() - start, request=request, argv=argv,
                error_detail=f"subprocess timeout after {timeout_s}s")
        latency = time.time() - start
        raw = proc.stdout or ""
        stderr = proc.stderr or ""
        return self._parse(request, argv, raw, stderr, proc.returncode, latency,
                           version)

    def _parse(self, request, argv, raw, stderr, returncode, latency,
               version) -> ModelResponse:
        combined_low = (raw + "\n" + stderr).lower()
        if any(m in combined_low for m in _INELIGIBLE_MARKERS):
            return ModelResponse(
                text="", status=ResponseStatus.ERROR, backend=self.name,
                model_id_reported=self.model_id, cli_version=version,
                latency_s=latency, request=request, argv=argv, raw_output=raw,
                error_detail="IneligibleTierError: account tier deprecated "
                             "(Gemini Code Assist for individuals retired)")

        text = ""
        try:
            data = json.loads(raw)
            if isinstance(data, dict):
                text = (data.get("response") or data.get("text")
                        or data.get("output") or "")
            elif isinstance(data, str):
                text = data
        except Exception:
            text = raw.strip()

        if not text:
            return ModelResponse(
                text="", status=ResponseStatus.PARSE_FAILURE, backend=self.name,
                model_id_reported=self.model_id, cli_version=version,
                latency_s=latency, request=request, argv=argv, raw_output=raw,
                error_detail=f"empty; returncode={returncode}; stderr={stderr[:300]}")

        status = ResponseStatus.REFUSAL if classify_refusal(text) else ResponseStatus.OK
        return ModelResponse(
            text=text, status=status, backend=self.name,
            model_id_reported=self.model_id, cli_version=version,
            latency_s=latency, request=request, argv=argv, raw_output=raw)
