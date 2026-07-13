"""Pure offline MVP request-shape adapters.

The adapters only transform strict dictionaries.  They deliberately contain no
transport, credential, environment, or provider SDK integration.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any


PROVENANCE = "SYNTHETIC_VALIDATION_ONLY"
_FAMILIES = frozenset(
    {"generic_messages", "generic_responses", "generic_content"}
)
_NEUTRAL_FIELDS = frozenset(
    {
        "provenance",
        "prompt",
        "response_schema",
        "tools",
        "temperature",
        "max_output_tokens",
    }
)


def _strict_neutral_request(request: Any) -> dict[str, Any]:
    if type(request) is not dict or set(request) != _NEUTRAL_FIELDS:
        raise ValueError("unsupported neutral request parameter")
    if request.get("provenance") != PROVENANCE:
        raise ValueError("request must be synthetic validation only")
    if type(request.get("prompt")) is not str or not request["prompt"]:
        raise ValueError("invalid neutral request")
    if type(request.get("response_schema")) is not dict:
        raise ValueError("invalid neutral request")
    if type(request.get("tools")) is not dict:
        raise ValueError("invalid neutral request")
    if type(request.get("temperature")) not in {int, float}:
        raise ValueError("invalid neutral request")
    if type(request.get("max_output_tokens")) is not int or not (
        1 <= request["max_output_tokens"] <= 4096
    ):
        raise ValueError("invalid neutral request")
    return deepcopy(request)


def adapt_request(provider_family: str, request: dict[str, Any]) -> dict[str, Any]:
    """Return one provider-family-shaped dictionary without performing I/O."""

    if provider_family not in _FAMILIES:
        raise ValueError("unsupported provider family")
    neutral = _strict_neutral_request(request)
    prompt = neutral["prompt"]
    temperature = neutral["temperature"]
    maximum = neutral["max_output_tokens"]
    tools = neutral["tools"]
    response_schema = neutral["response_schema"]
    if provider_family == "generic_messages":
        return {
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": maximum,
            "temperature": temperature,
            "tools": tools,
            "response_schema": response_schema,
        }
    if provider_family == "generic_responses":
        return {
            "input": [{"role": "user", "content": prompt}],
            "max_output_tokens": maximum,
            "temperature": temperature,
            "tools": tools,
            "response_format": response_schema,
        }
    return {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generation_config": {
            "temperature": temperature,
            "max_output_tokens": maximum,
        },
        "tools": tools,
        "response_schema": response_schema,
    }


__all__ = ("PROVENANCE", "adapt_request")
