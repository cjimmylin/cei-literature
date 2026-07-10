"""Provenance stamping helpers.

Every real-token artifact carries provenance class ``cli-oauth-provisional``
plus CLI name+version and the model id as reported in the response, per
INNOVATION/20260709d-cli-oauth-provisional-ruling.md §2.
"""

from __future__ import annotations

from typing import Any

from .core import PROVENANCE_CLASS, ModelResponse


def stamp(response: ModelResponse) -> dict[str, Any]:
    """Return the provenance block for a single response."""
    return {
        "provenance_class": PROVENANCE_CLASS,
        "backend": response.backend,
        "cli_version": response.cli_version,
        "model_id_reported": response.model_id_reported,
        "self_reported_model": response.self_reported_model,
        "timestamp": response.timestamp,
        "note": (
            "Real-model completion via subscription/OAuth CLI (injected vendor "
            "scaffold, no sampling control, model id as self-reported). NOT an "
            "API measurement; may not stand in for one or enter a frozen verdict."
        ),
    }


PROVENANCE_HEADLINE = (
    "All outputs cli-oauth-provisional; nothing here is an API measurement."
)
