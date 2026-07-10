"""Locked five-class fusion for two blinded ZEROSUM judge families."""

from collections.abc import Mapping as MappingABC
from typing import Any, Dict, Mapping, Optional

from zerosum_common import ADVICE_CLASSES
from scoring.judge_prompts import (
    JUDGE_FAMILIES, JudgeAdapter, build_judge_request, validate_judge_output,
)


def _response_text(response: Any) -> str:
    if isinstance(response, str):
        return response
    if isinstance(response, MappingABC):
        for key in ("response_text", "response", "advice", "output"):
            if isinstance(response.get(key), str):
                return response[key]
    raise ValueError("response text is missing")


def fuse_judge_outputs(outputs: Mapping[str, Mapping[str, Any]]) -> Dict[str, Any]:
    """Fuse exactly two validated family outputs deterministically."""

    if not isinstance(outputs, MappingABC) or set(outputs) != set(JUDGE_FAMILIES):
        raise ValueError("outputs must contain exactly the two registered judge families")
    normalized = [
        validate_judge_output(outputs[family]) for family in JUDGE_FAMILIES
    ]
    left, right = normalized

    if left["advice_class"] == right["advice_class"]:
        advice_class = left["advice_class"]
        confidence = (left["confidence"] + right["confidence"]) / 2.0
    elif left["confidence"] > right["confidence"]:
        advice_class = left["advice_class"]
        confidence = left["confidence"]
    elif right["confidence"] > left["confidence"]:
        advice_class = right["advice_class"]
        confidence = right["confidence"]
    else:
        advice_class = "hedged"
        confidence = min(left["confidence"], right["confidence"], 0.5)

    def weighted_boolean(field: str) -> bool:
        if left[field] == right[field]:
            return bool(left[field])
        if left["confidence"] == right["confidence"]:
            return False
        return bool(
            left[field] if left["confidence"] > right["confidence"] else right[field]
        )

    if left["response_status"] == right["response_status"]:
        status = left["response_status"]
    elif left["confidence"] > right["confidence"]:
        status = left["response_status"]
    elif right["confidence"] > left["confidence"]:
        status = right["response_status"]
    else:
        status = "invalid"

    evidence = []
    for output in normalized:
        for span in output["evidence_spans"]:
            if span not in evidence:
                evidence.append(span)
    return {
        "advice_class": advice_class,
        "fr": weighted_boolean("fr"),
        "response_status": status,
        "evidence_spans": evidence,
        "confidence": confidence,
    }


def classify_advice(
    certificate: Mapping[str, Any],
    response: Any,
    *,
    judge_outputs: Optional[Mapping[str, Mapping[str, Any]]] = None,
    judges: Optional[Mapping[str, JudgeAdapter]] = None,
) -> Dict[str, Any]:
    """Classify one response from a private certificate and blinded response."""

    requests = {
        family: build_judge_request(family, certificate, response)
        for family in JUDGE_FAMILIES
    }
    if judge_outputs is None:
        if not isinstance(judges, MappingABC) or set(judges) != set(JUDGE_FAMILIES):
            raise ValueError("provide outputs or adapters for both judge families")
        judge_outputs = {
            family: judges[family](requests[family]) for family in JUDGE_FAMILIES
        }
    if not isinstance(judge_outputs, MappingABC):
        raise TypeError("judge_outputs must be a mapping")
    text = _response_text(response)
    normalized = {
        family: validate_judge_output(judge_outputs[family], text)
        for family in JUDGE_FAMILIES
        if family in judge_outputs
    }
    if set(normalized) != set(JUDGE_FAMILIES):
        raise ValueError("outputs must contain both registered judge families")
    return fuse_judge_outputs(normalized)


class AdviceClassifier:
    """Reusable classifier wrapper around two independent judge adapters."""

    def __init__(self, judges: Mapping[str, JudgeAdapter]):
        if not isinstance(judges, MappingABC) or set(judges) != set(JUDGE_FAMILIES):
            raise ValueError("two registered judge adapters are required")
        self._judges = dict(judges)

    def classify(
        self, certificate: Mapping[str, Any], response: Any
    ) -> Dict[str, Any]:
        return classify_advice(certificate, response, judges=self._judges)


__all__ = [
    "ADVICE_CLASSES", "AdviceClassifier", "classify_advice",
    "fuse_judge_outputs",
]
