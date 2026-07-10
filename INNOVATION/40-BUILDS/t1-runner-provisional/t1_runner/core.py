"""Vendor-agnostic T1 provisional runner core.

The T1 contract: callers construct a ``ModelRequest``, hand it to a ``Runner``
(which owns one or more ``RunnerBackend`` instances), and receive a
``ModelResponse``. No CLI-specific detail leaks through this interface, so a
future ``*_api`` backend drops in with zero caller changes.

Every real-token completion obtained here is provenance class
``cli-oauth-provisional`` (see INNOVATION/20260709d-cli-oauth-provisional-ruling.md).
It may validate machinery and pilot designs; it may NEVER stand in for an API
measurement.
"""

from __future__ import annotations

import abc
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Optional

PROVENANCE_CLASS = "cli-oauth-provisional"


class ResponseStatus(str, Enum):
    """Outcome classification for a single call. A refusal is *data*, not an error."""

    OK = "ok"
    REFUSAL = "refusal"
    ERROR = "error"
    TIMEOUT = "timeout"
    PARSE_FAILURE = "parse_failure"


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class ModelRequest:
    """A vendor-agnostic request. ``params`` is a free dict (e.g. model alias)."""

    prompt: str
    item_id: str = ""
    params: dict[str, Any] = field(default_factory=dict)
    system: Optional[str] = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ModelResponse:
    """A vendor-agnostic response carrying full provenance.

    Fields required by the T1 spec:
      text, model_id_reported, backend, cli_version, provenance, latency_s,
      raw_output (or raw_output_path), timestamp, status (ok|refusal|error|
      timeout|parse_failure).
    """

    text: str
    status: ResponseStatus
    backend: str
    model_id_reported: str
    cli_version: str
    latency_s: float
    request: ModelRequest
    provenance: str = PROVENANCE_CLASS
    raw_output: str = ""
    raw_output_path: Optional[str] = None
    argv: list[str] = field(default_factory=list)
    error_detail: str = ""
    self_reported_model: str = ""  # model's prose self-report (unreliable; captured separately)
    timestamp: str = field(default_factory=_utc_now_iso)

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["status"] = self.status.value
        return d


class RunnerBackend(abc.ABC):
    """One vendor backend. Subclasses MUST NOT leak CLI details to callers.

    Contract: ``run()`` never raises for model-side outcomes (refusal, error,
    timeout, parse failure) — it returns a classified ``ModelResponse``. It may
    only raise for genuine programmer error (never for a bad completion).
    """

    #: short stable backend name, e.g. "anthropic_cli"
    name: str = "abstract"

    @abc.abstractmethod
    def cli_version(self) -> str:
        """Return the CLI version string, captured once per run by the Runner."""

    @abc.abstractmethod
    def run(self, request: ModelRequest, timeout_s: float) -> ModelResponse:
        """Execute one call and return a fully-classified response."""


# --- refusal detection (shared, conservative) -------------------------------

# Substrings that strongly indicate a soft refusal / safe-completion hedge.
_REFUSAL_MARKERS = (
    "i can't help with that",
    "i cannot help with that",
    "i can't provide",
    "i cannot provide",
    "i'm not able to provide",
    "i am not able to provide",
    "i can't assist",
    "i cannot assist",
    "i won't be able to",
    "i'm unable to help",
    "i am unable to help",
    "i'm sorry, but i can't",
    "i'm sorry, but i cannot",
    "i can't recommend",
    "i cannot recommend a specific",
    "consult a doctor",
    "consult a healthcare",
    "consult your doctor",
    "speak with a healthcare",
    "please seek medical",
    "i can't give medical",
    "i cannot give medical",
    "i'm not a medical professional",
    "against my guidelines",
)


def classify_refusal(text: str) -> bool:
    """True if ``text`` looks like a soft refusal / safe-completion hedge.

    Conservative: only fires on explicit refusal/deferral language. A refusal is
    a valid logged response, not an exception.
    """
    if not text:
        return False
    # Normalize Unicode apostrophes/quotes to ASCII so "I can't" matches whether
    # the model emits U+0027 (') or U+2019 (’). Observed: codex uses U+2019.
    low = (text.lower()
           .replace("’", "'").replace("‘", "'")
           .replace("ʼ", "'"))
    return any(marker in low for marker in _REFUSAL_MARKERS)


@dataclass
class RunResult:
    """Bundle returned by Runner.run_item: one response per backend."""

    request: ModelRequest
    responses: dict[str, ModelResponse]  # backend name -> response


class Runner:
    """Orchestrates one request across one or more backends.

    Captures each backend's CLI version once at construction, logs every call to
    the transcript, and applies backoff via the injected caller of ``run``.
    """

    def __init__(self, backends: list[RunnerBackend], transcript=None,
                 timeout_s: float = 120.0):
        self.backends = {b.name: b for b in backends}
        self.transcript = transcript
        self.timeout_s = timeout_s
        # version captured once per run, stamped on every record
        self._versions = {name: b.cli_version() for name, b in self.backends.items()}

    def versions(self) -> dict[str, str]:
        return dict(self._versions)

    def run_item(self, request: ModelRequest,
                 backends: Optional[list[str]] = None) -> RunResult:
        targets = backends or list(self.backends.keys())
        responses: dict[str, ModelResponse] = {}
        for name in targets:
            backend = self.backends[name]
            start = time.time()
            resp = backend.run(request, timeout_s=self.timeout_s)
            # defensive: ensure latency populated even if backend forgot
            if not resp.latency_s:
                resp.latency_s = time.time() - start
            responses[name] = resp
            if self.transcript is not None:
                self.transcript.log(resp)
        return RunResult(request=request, responses=responses)
