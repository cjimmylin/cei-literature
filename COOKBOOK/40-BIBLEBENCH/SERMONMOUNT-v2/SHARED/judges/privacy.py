"""Fail-closed scans for judge-visible packets and WITNESS GEN semantics."""
from __future__ import annotations

import unicodedata
import re
from typing import Any, Iterable, Mapping, Sequence, Tuple

from canonical import content_hash


class PacketPrivacyError(ValueError):
    """A judge-visible object contains a private field or value."""


FORBIDDEN_FIELDS = frozenset(
    {
        "scoring_key",
        "expected_result",
        "expected_answer",
        "expected_action",
        "reference_label",
        "exact_matcher_signals",
        "matcher_signals",
        "action_key",
        "model",
        "model_id",
        "tested_model",
        "tested_model_id",
        "provider",
        "vendor",
        "endpoint",
        "endpoint_version",
        "family",
        "family_id",
        "model_family",
        "tested_model_family",
        "tested_family_id",
        "tested_provider",
        "tested_response_family",
        "tested_response_family_id",
        "material_family",
        "material_family_id",
        "material_generation_family",
        "material_generation_family_id",
        "material_generation_families",
        "excluded_family",
        "arm",
        "arm_label",
        "condition",
        "condition_label",
        "monitoring_status",
        "monitored",
        "holdout",
        "predicted_gap",
        "cross_modality_outcomes",
        "hypothesis",
        "study_hypothesis",
        "study_hypotheses",
    }
)


def _normalized(value: str) -> str:
    return unicodedata.normalize("NFKC", value).casefold()


def _canonical_key(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value)
    camel_split = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", normalized)
    return re.sub(r"[^\w]+|_+", "_", camel_split.casefold()).strip("_")


def _walk(value: Any, path: str = "$") -> Iterable[Tuple[str, Any]]:
    yield path, value
    if isinstance(value, Mapping):
        for key, child in value.items():
            yield from _walk(child, f"{path}.{key}")
    elif isinstance(value, (list, tuple)):
        for index, child in enumerate(value):
            yield from _walk(child, f"{path}[{index}]")


def require_packet_privacy(
    packet: Mapping[str, Any], *, forbidden_values: Sequence[str] = ()
) -> bool:
    """Reject hidden metadata and caller-supplied identity/condition values."""

    if not isinstance(packet, Mapping):
        raise PacketPrivacyError("packet must be an object")
    normalized_forbidden = []
    for value in forbidden_values:
        if not isinstance(value, str) or not value:
            raise PacketPrivacyError("forbidden values must be non-empty strings")
        normalized_forbidden.append((_normalized(value), value))

    for path, value in _walk(packet):
        if isinstance(value, Mapping):
            for key in value:
                if not isinstance(key, str):
                    raise PacketPrivacyError(f"{path}: non-string field")
                if _canonical_key(key) in FORBIDDEN_FIELDS:
                    raise PacketPrivacyError(f"{path}.{key}: forbidden private field {key}")
        if isinstance(value, str):
            normalized = _normalized(value)
            for secret, original in normalized_forbidden:
                if secret in normalized:
                    raise PacketPrivacyError(
                        f"{path}: forbidden value present ({original!r})"
                    )
    return True


def validate_witness_gen_visibility(packet: Mapping[str, Any]) -> bool:
    """Require all four natural-language poles and their committed criteria hash."""

    require_packet_privacy(packet)
    rubric = packet.get("rubric")
    if not isinstance(rubric, Mapping):
        raise PacketPrivacyError("rubric missing")
    criteria = rubric.get("criteria")
    expected_poles = {"gold", "deficient", "counterfeit", "neutral"}
    if not isinstance(criteria, Mapping) or set(criteria) != expected_poles:
        raise PacketPrivacyError("criteria must contain exactly the four WITNESS poles")
    for pole in sorted(expected_poles):
        criterion = criteria[pole]
        if not isinstance(criterion, Mapping) or set(criterion) != {
            "pole_text",
            "paraphrases",
        }:
            raise PacketPrivacyError(f"criteria.{pole}: pole_text/paraphrases required")
        pole_text = criterion["pole_text"]
        paraphrases = criterion["paraphrases"]
        if not isinstance(pole_text, str) or not pole_text.strip():
            raise PacketPrivacyError(f"criteria.{pole}.pole_text must be non-empty")
        if not isinstance(paraphrases, list) or not paraphrases:
            raise PacketPrivacyError(f"criteria.{pole}.paraphrases must be non-empty")
        if any(not isinstance(text, str) or not text.strip() for text in paraphrases):
            raise PacketPrivacyError(
                f"criteria.{pole}.paraphrases must contain non-empty text"
            )
    if packet.get("criteria_hash") != content_hash(dict(criteria)):
        raise PacketPrivacyError("criteria_hash does not commit to visible criteria")
    return True
