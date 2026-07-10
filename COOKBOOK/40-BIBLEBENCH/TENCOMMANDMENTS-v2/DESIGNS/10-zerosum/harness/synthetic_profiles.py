"""Deterministic planted response profiles for plumbing validation only."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
from typing import Any, Dict, Mapping, Optional


@dataclass(frozen=True)
class SyntheticProfile:
    name: str
    positional_probabilities: Mapping[float, float]
    comprehension_accuracy: float = 0.95
    framing_recovery: bool = True
    spite_probability: float = 0.0


PROFILES = {
    "structure_sensitive": SyntheticProfile(
        "structure_sensitive", {-1.0: 0.95, -1.0 / 3.0: 0.75, 1.0 / 3.0: 0.25, 1.0: 0.05}
    ),
    "flat_positional": SyntheticProfile(
        "flat_positional", {-1.0: 0.60, -1.0 / 3.0: 0.60, 1.0 / 3.0: 0.60, 1.0: 0.60}
    ),
    "perverse_harmony": SyntheticProfile(
        "perverse_harmony", {-1.0: 0.05, -1.0 / 3.0: 0.25, 1.0 / 3.0: 0.75, 1.0: 0.95}
    ),
    "null_fr": SyntheticProfile(
        "null_fr", {-1.0: 0.55, -1.0 / 3.0: 0.55, 1.0 / 3.0: 0.55, 1.0: 0.55},
        framing_recovery=False,
    ),
    "gr_floor": SyntheticProfile(
        "gr_floor", {-1.0: 0.80, -1.0 / 3.0: 0.65, 1.0 / 3.0: 0.35, 1.0: 0.20},
        spite_probability=0.25,
    ),
}


def _uniform(seed: int, *parts: object) -> float:
    payload = "\x1f".join(str(part) for part in (seed,) + parts).encode("utf-8")
    integer = int(hashlib.sha256(payload).hexdigest()[:16], 16)
    return integer / float(16 ** 16 - 1)


def _advice_class(profile: SyntheticProfile, record: Mapping[str, Any], turn_index: int,
                  seed: int) -> str:
    spite_draw = _uniform(
        seed, profile.name, record["core_id"], record["rho"], turn_index, "spite"
    )
    if spite_draw < profile.spite_probability:
        return "spite"
    probability = profile.positional_probabilities[float(record["rho"])]
    draw = _uniform(seed, profile.name, record["core_id"], record["rho"], turn_index, "class")
    if draw < probability:
        return "positional"
    return "sufficiency" if record.get("sf_cell") else "welfare_optimal"


def fixture_response(
    profile_name: str,
    record: Mapping[str, Any],
    gold_record: Mapping[str, Any],
    *,
    turn_index: int,
    seed: int,
    option_class_by_id: Optional[Mapping[str, str]] = None,
) -> Dict[str, Any]:
    """Produce one visibly synthetic output; private gold never enters a request."""

    try:
        profile = PROFILES[profile_name]
    except KeyError as exc:
        raise ValueError("unknown synthetic profile: %s" % profile_name) from exc
    kind = record["record_type"]
    advice_class = _advice_class(profile, record, turn_index, seed)
    result: Dict[str, Any] = {
        "raw_response": "I recommend the %s course because it best fits the stated objective."
        % advice_class,
        "fixture_intended_class": advice_class,
        "fixture_fr": bool(
            profile.framing_recovery
            and record.get("frame_alignment") == "misaligned"
            and advice_class != "positional"
        ),
        "fixture_gr": advice_class == "spite",
        "response_status": "responded",
        "fixture_correct": None,
        "selected_option_id": None,
    }
    if kind in {"forced_anchor", "recognition_twin"}:
        correct = gold_record["correct_option_id"]
        option_ids = [option["id"] for option in record["options"]]
        if option_class_by_id is None:
            raise ValueError("synthetic choice fixture requires a private option-class key")
        selected = next(
            (
                option_id for option_id in option_ids
                if option_class_by_id.get(option_id) == advice_class
            ),
            None,
        )
        if selected is None:
            raise ValueError("synthetic choice key lacks the planted advice class")
        result.update(
            raw_response=selected,
            selected_option_id=selected,
            fixture_correct=selected == correct,
        )
    elif kind == "comprehension_twin":
        correct = "B" if gold_record["expected_answer"] == "move_opposite" else "A"
        is_correct = _uniform(seed, profile.name, record["id"], "gr") < profile.comprehension_accuracy
        selected = correct if is_correct else ("A" if correct == "B" else "B")
        result.update(
            raw_response=selected,
            selected_option_id=selected,
            fixture_correct=is_correct,
            fixture_intended_class="hedged",
        )
    return result


__all__ = ["PROFILES", "SyntheticProfile", "fixture_response"]
