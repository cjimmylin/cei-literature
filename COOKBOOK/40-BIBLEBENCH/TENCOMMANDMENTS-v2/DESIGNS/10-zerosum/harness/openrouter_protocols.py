"""Immutable transport protocol registry for the OpenRouter diagnostic."""

from dataclasses import dataclass
from types import MappingProxyType
from typing import Mapping, Optional, Tuple


V1_CONFIG_SHA256 = "a22920456868293d51d92814f2daebc9f6de06e6948149c7427097b6291f9f41"
R2_CONFIG_SHA256 = "b2eeb8f436e172bccebb98529e58de21298081ec69fc5846e40339fe5a61f14c"
V1_RUN_ID = "10CB-ZEROSUM-P1-OPENROUTER-FORCED-20260710"
R2_RUN_ID = "10CB-ZEROSUM-P1-OPENROUTER-FORCED-20260710-R2"


@dataclass(frozen=True)
class DiagnosticProtocol:
    revision: str
    config_sha256: str
    run_id: str
    transport: Mapping[str, object]
    provenance_keys: Tuple[str, ...]
    supersedes_config_sha256: Optional[str]

    @property
    def effective_reasoning_effort(self) -> Optional[str]:
        value = self.transport.get("reasoning_effort")
        return value if isinstance(value, str) else None


V1_PROTOCOL = DiagnosticProtocol(
    revision="V1",
    config_sha256=V1_CONFIG_SHA256,
    run_id=V1_RUN_ID,
    transport=MappingProxyType({
        "max_tokens": 512,
        "timeout_seconds": 120,
        "max_attempts": 3,
        "retry_base_seconds": 0.5,
    }),
    provenance_keys=("bank_sha256", "gold_sha256"),
    supersedes_config_sha256=None,
)
R2_PROTOCOL = DiagnosticProtocol(
    revision="R2",
    config_sha256=R2_CONFIG_SHA256,
    run_id=R2_RUN_ID,
    transport=MappingProxyType({
        "max_tokens": 1024,
        "timeout_seconds": 120,
        "max_attempts": 3,
        "retry_base_seconds": 0.5,
        "reasoning_effort": "minimal",
    }),
    provenance_keys=(
        "bank_sha256", "gold_sha256", "supersedes_config_sha256"
    ),
    supersedes_config_sha256=V1_CONFIG_SHA256,
)

PROTOCOLS_BY_CONFIG_SHA256: Mapping[str, DiagnosticProtocol] = MappingProxyType({
    V1_CONFIG_SHA256: V1_PROTOCOL,
    R2_CONFIG_SHA256: R2_PROTOCOL,
})
PROTOCOLS_BY_RUN_ID: Mapping[str, DiagnosticProtocol] = MappingProxyType({
    V1_RUN_ID: V1_PROTOCOL,
    R2_RUN_ID: R2_PROTOCOL,
})


__all__ = [
    "DiagnosticProtocol",
    "PROTOCOLS_BY_CONFIG_SHA256",
    "PROTOCOLS_BY_RUN_ID",
    "R2_CONFIG_SHA256",
    "R2_PROTOCOL",
    "R2_RUN_ID",
    "V1_CONFIG_SHA256",
    "V1_PROTOCOL",
    "V1_RUN_ID",
]
