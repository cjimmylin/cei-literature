"""T1 provisional runner shim — vendor-agnostic CLI-OAuth backends.

Provenance of all real-token output: cli-oauth-provisional (see
INNOVATION/20260709d-cli-oauth-provisional-ruling.md). NOT an API measurement.
"""

from .core import (ModelRequest, ModelResponse, ResponseStatus, RunnerBackend,
                   Runner, RunResult, classify_refusal, PROVENANCE_CLASS)
from .transcript import TranscriptLogger
from .backoff import retry_with_backoff, compute_delay
from .provenance import stamp, PROVENANCE_HEADLINE
from .backends import (AnthropicCLIBackend, OpenAICLIBackend, GoogleCLIBackend)

__all__ = [
    "ModelRequest", "ModelResponse", "ResponseStatus", "RunnerBackend",
    "Runner", "RunResult", "classify_refusal", "PROVENANCE_CLASS",
    "TranscriptLogger", "retry_with_backoff", "compute_delay", "stamp",
    "PROVENANCE_HEADLINE", "AnthropicCLIBackend", "OpenAICLIBackend",
    "GoogleCLIBackend",
]
