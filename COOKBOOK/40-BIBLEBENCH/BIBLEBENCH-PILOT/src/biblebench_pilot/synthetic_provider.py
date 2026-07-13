"""Deterministic no-I/O synthetic provider for runner verification."""

from __future__ import annotations

from typing import Any

from .contracts import canonical_sha256


PROVENANCE = "SYNTHETIC_VALIDATION_ONLY"
SCENARIOS = (
    "success",
    "refusal",
    "malformed",
    "truncated",
    "rate_limit_once",
    "unknown_delivery",
    "retry_exhausted",
)


class SyntheticProvider:
    """Generate registered synthetic outcomes from local dictionaries only."""

    def attempt(
        self,
        request: dict[str, Any],
        *,
        scenario: str,
        attempt: int,
    ) -> dict[str, Any]:
        if scenario not in SCENARIOS:
            raise ValueError("unknown synthetic scenario")
        if type(attempt) is not int or attempt not in {1, 2}:
            raise ValueError("invalid synthetic attempt")
        if (
            type(request) is not dict
            or request.get("provenance") != PROVENANCE
            or type(request.get("logical_call_id")) is not str
            or type(request.get("request_sha256")) is not str
        ):
            raise ValueError("invalid synthetic request")

        status = scenario
        terminal = True
        content: dict[str, Any] | str | None
        input_tokens = 17 + int(request["logical_call_id"][:2], 16) % 23
        output_tokens = 0
        if scenario == "success" or (
            scenario == "rate_limit_once" and attempt == 2
        ):
            status = "success"
            content = {
                "synthetic_answer": "registered-success",
                "request_binding": request["request_sha256"],
            }
            output_tokens = 11
        elif scenario == "refusal":
            content = "SYNTHETIC_REFUSAL"
            output_tokens = 3
        elif scenario == "malformed":
            content = "{synthetic-malformed"
            output_tokens = 4
        elif scenario == "truncated":
            content = "SYNTHETIC_TRUNCATED…"
            output_tokens = 5
        elif scenario == "rate_limit_once":
            status = "rate_limit"
            terminal = False
            content = None
        elif scenario == "unknown_delivery":
            content = None
        else:
            status = "rate_limit"
            terminal = attempt == 2
            content = None

        core = {
            "provenance": PROVENANCE,
            "status": status,
            "terminal": terminal,
            "content": content,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
        }
        return {**core, "synthetic_response_sha256": canonical_sha256(core)}


__all__ = ("PROVENANCE", "SCENARIOS", "SyntheticProvider")
