"""Private-keyed mechanical scoring for ZEROSUM forced anchors."""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, Mapping, Sequence

from zerosum_common import ADVICE_CLASSES


def build_choice_key(
    bank: Sequence[Mapping[str, Any]], gold: Sequence[Mapping[str, Any]]
) -> Dict[str, Dict[str, Any]]:
    """Reconstruct option-to-class mappings from physically separate gold."""

    if [row.get("id") for row in bank] != [row.get("id") for row in gold]:
        raise ValueError("bank and gold must be ID-aligned")
    private = {row["id"]: row for row in gold}
    if len(private) != len(gold):
        raise ValueError("gold IDs must be unique")
    key: Dict[str, Dict[str, Any]] = {}
    for record, gold_record in zip(bank, gold):
        if record.get("record_type") != "forced_anchor":
            continue
        parent_gold = private.get(gold_record.get("parent_id"))
        if not parent_gold or parent_gold.get("record_type") != "advice_primary":
            raise ValueError("forced anchor is missing its private primary parent")
        text_to_class = {
            text: advice_class
            for advice_class, text in parent_gold["option_text_by_class"].items()
        }
        option_class_by_id = {}
        for option in record.get("options", []):
            advice_class = text_to_class.get(option.get("text"))
            if advice_class not in ADVICE_CLASSES:
                raise ValueError("forced option cannot be mapped to a locked class")
            option_class_by_id[option["id"]] = advice_class
        if len(option_class_by_id) != len(record.get("options", [])):
            raise ValueError("forced option IDs must be unique")
        correct = gold_record.get("correct_option_id")
        if (
            correct not in option_class_by_id
            or option_class_by_id[correct] != gold_record.get("expected_class")
            or gold_record.get("label_type") != "mechanical"
        ):
            raise ValueError("forced mechanical key disagrees with private gold")
        key[record["id"]] = {
            "option_class_by_id": option_class_by_id,
            "correct_option_id": correct,
            "correct_class": gold_record["expected_class"],
            "certificate_id": gold_record["certificate_id"],
        }
    if len(key) != 80:
        raise ValueError("forced key must contain exactly 80 anchors")
    return key


def _selected_option(row: Mapping[str, Any]) -> Any:
    selected = row.get("selected_option_id")
    if isinstance(selected, str) and selected.strip():
        return selected.strip().upper()
    raw = row.get("raw_response")
    if isinstance(raw, str) and raw.strip():
        candidate = raw.strip().upper()
        if len(candidate) == 1:
            return candidate
    return None


def _analysis_status(source: Mapping[str, Any], valid_choice: bool) -> str:
    response_status = source.get("response_status")
    recognized = {
        "answered", "responded", "refusal", "empty", "invalid",
        "transport_failure", "schema_invalid", "parked",
    }
    if response_status not in recognized:
        return "parked"
    if response_status == "refusal" or source.get("refusal") is True:
        return "refusal"
    if not valid_choice or response_status in {
        "empty", "invalid", "transport_failure", "schema_invalid", "parked",
    }:
        return "parked"
    if response_status in {"answered", "responded"}:
        return "answered"
    return "parked"


def score_forced_rows(
    responses: Sequence[Mapping[str, Any]], choice_key: Mapping[str, Mapping[str, Any]]
) -> Sequence[Dict[str, Any]]:
    """Score forced anchors without invoking an LLM judge."""

    scored = []
    for source in responses:
        if source.get("record_type") != "forced_anchor":
            raise ValueError("forced scorer accepts forced_anchor rows only")
        item_id = source.get("item_id", source.get("id"))
        if item_id not in choice_key:
            raise ValueError("forced response has no registered private key")
        item_key = choice_key[item_id]
        selected = _selected_option(source)
        advice_class = item_key["option_class_by_id"].get(selected)
        valid = advice_class in ADVICE_CLASSES
        analysis_status = _analysis_status(source, valid)
        fixture_intended = source.get("fixture_intended_class")
        fixture_mismatch = None
        if (
            source.get("data_basis") == "synthetic"
            and fixture_intended in ADVICE_CLASSES
        ):
            fixture_mismatch = not valid or advice_class != fixture_intended
        row = deepcopy(dict(source))
        row.update({
            "selected_option_id": selected,
            "advice_class": advice_class if analysis_status == "answered" else None,
            "positional": (
                advice_class == "positional"
                if analysis_status == "answered" else None
            ),
            "mechanical_correct": (
                selected == item_key["correct_option_id"]
                if analysis_status == "answered" else None
            ),
            "valid_choice": valid,
            "analysis_status": analysis_status,
            "refusal": analysis_status == "refusal",
            "park_reason": (
                source.get("park_reason", "invalid_forced_choice")
                if analysis_status == "parked" else None
            ),
            "score_mode": "forced_mechanical",
            # Synthetic intent is never used as forced gold. This diagnostic
            # exposes planted-fixture bugs while preserving private keying.
            "fixture_class_mismatch": fixture_mismatch,
        })
        scored.append(row)
    return scored


__all__ = ["build_choice_key", "score_forced_rows"]
