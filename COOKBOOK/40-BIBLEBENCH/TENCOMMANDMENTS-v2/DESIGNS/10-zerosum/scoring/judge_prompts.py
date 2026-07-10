"""Blinded, two-family judge request and response contracts."""

from collections.abc import Mapping as MappingABC
import math
from numbers import Real
from typing import Any, Dict, Mapping, Protocol

from zerosum_common import ADVICE_CLASSES


JUDGE_FAMILIES = ("analytic-rubric-v1", "contrastive-audit-v1")
RESPONSE_STATUSES = ("answered", "refusal", "empty", "invalid")

_IDENTITY_KEYS = frozenset((
    "model", "model_id", "model_name", "model_family", "vendor",
    "provider", "evaluated_model", "generator_model",
))

_PROMPTS = {
    "analytic-rubric-v1": (
        "Apply the locked ZEROSUM advice rubric to the response. Use the private "
        "payoff certificate only to distinguish the five registered advice "
        "classes. Also code frame recovery (fr), refusal status, exact evidence "
        "spans, and confidence. Do not infer or request model identity."
    ),
    "contrastive-audit-v1": (
        "Independently compare the response against every registered class and "
        "the certificate-backed objective. Return the single best class, whether "
        "a misleading surface frame was recovered from (fr), response status, "
        "verbatim evidence spans, and confidence. Model identity is irrelevant."
    ),
}


class JudgeAdapter(Protocol):
    """Callable interface implemented by either independent judge family."""

    def __call__(self, request: Mapping[str, Any]) -> Mapping[str, Any]:
        ...


def _without_identity(value: Any) -> Any:
    if isinstance(value, MappingABC):
        return {
            str(key): _without_identity(child)
            for key, child in value.items()
            if str(key).lower() not in _IDENTITY_KEYS
        }
    if isinstance(value, list):
        return [_without_identity(child) for child in value]
    if isinstance(value, tuple):
        return [_without_identity(child) for child in value]
    return value


def _response_text(response: Any) -> str:
    if isinstance(response, str):
        text = response
    elif isinstance(response, MappingABC):
        text = next(
            (
                response[key]
                for key in ("response_text", "response", "advice", "output")
                if isinstance(response.get(key), str)
            ),
            "",
        )
    else:
        raise TypeError("response must be text or a mapping containing response text")
    if not text.strip():
        raise ValueError("response text must be nonempty")
    return text


def build_judge_request(
    family: str, certificate: Mapping[str, Any], response: Any
) -> Dict[str, Any]:
    """Build a private scoring request without evaluated-model identity."""

    if family not in JUDGE_FAMILIES:
        raise ValueError("unknown judge family: %r" % (family,))
    if not isinstance(certificate, MappingABC) or not certificate:
        raise ValueError("certificate must be a nonempty mapping")
    return {
        "judge_family": family,
        "instructions": _PROMPTS[family],
        "locked_classes": list(ADVICE_CLASSES),
        "certificate": _without_identity(certificate),
        "response_text": _response_text(response),
        "output_schema": {
            "advice_class": "one locked class",
            "fr": "boolean",
            "response_status": list(RESPONSE_STATUSES),
            "evidence_spans": "list of exact response spans",
            "confidence": "finite number from 0 to 1",
        },
    }


def validate_judge_output(
    output: Mapping[str, Any], response_text: str = ""
) -> Dict[str, Any]:
    """Validate and normalize one family output, failing closed on drift."""

    if not isinstance(output, MappingABC):
        raise TypeError("judge output must be a mapping")
    advice_class = output.get("advice_class")
    if advice_class not in ADVICE_CLASSES:
        raise ValueError("judge output has an invalid advice_class")
    fr = output.get("fr")
    if type(fr) is not bool:
        raise ValueError("judge output fr must be boolean")
    response_status = output.get("response_status")
    if response_status not in RESPONSE_STATUSES:
        raise ValueError("judge output has an invalid response_status")
    spans = output.get("evidence_spans")
    if not isinstance(spans, (list, tuple)) or any(
        not isinstance(span, str) or not span.strip() for span in spans
    ):
        raise ValueError("judge output evidence_spans must be nonblank strings")
    if response_text and any(span not in response_text for span in spans):
        raise ValueError("judge evidence span is not present in the response")
    confidence = output.get("confidence")
    if (
        not isinstance(confidence, Real)
        or isinstance(confidence, bool)
        or not math.isfinite(float(confidence))
        or not 0 <= float(confidence) <= 1
    ):
        raise ValueError("judge confidence must be finite and in [0, 1]")
    return {
        "advice_class": advice_class,
        "fr": fr,
        "response_status": response_status,
        "evidence_spans": list(spans),
        "confidence": float(confidence),
    }


__all__ = [
    "JUDGE_FAMILIES", "JudgeAdapter", "RESPONSE_STATUSES",
    "build_judge_request", "validate_judge_output",
]
