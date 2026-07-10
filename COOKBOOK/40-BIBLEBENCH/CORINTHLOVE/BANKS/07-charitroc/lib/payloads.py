"""Explicit model/judge payload boundary; sidecar objects are never accepted."""
from __future__ import annotations

from collections.abc import Mapping
import re
import uuid


STAGES = ("stage_1", "stage_2", "stage_3", "stage_4")
JUDGE_TOKEN_RE = re.compile(
    r"^JUDGE-[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-"
    r"[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
)


def model_turns(episode: Mapping) -> list:
    if not isinstance(episode, Mapping):
        raise TypeError("episode must be a mapping")
    if "multiturn_script" not in episode:
        raise ValueError("episode must contain multiturn_script")
    script = episode["multiturn_script"]
    if not isinstance(script, Mapping):
        raise TypeError("multiturn script must be a mapping")
    if len(script) != len(STAGES) or set(script) != set(STAGES):
        raise ValueError(
            "multiturn script must contain exactly " + ", ".join(STAGES)
        )
    for stage in STAGES:
        if not isinstance(script[stage], str):
            raise TypeError(f"{stage} content must be a string")
    return [{"stage": stage, "content": script[stage]} for stage in STAGES]


def model_visible_text(episode: dict) -> str:
    return "\n".join(turn["content"] for turn in model_turns(episode))


def is_valid_judge_case_id(value: object) -> bool:
    """Return whether *value* is a lowercase RFC-4122 UUIDv4 judge token."""
    if not isinstance(value, str) or JUDGE_TOKEN_RE.fullmatch(value) is None:
        return False
    parsed = uuid.UUID(value.removeprefix("JUDGE-"))
    return parsed.version == 4 and parsed.variant == uuid.RFC_4122


def build_judge_payload(episode: Mapping, responses: Mapping,
                        judge_case_id: str) -> dict:
    if not is_valid_judge_case_id(judge_case_id):
        raise ValueError("judge_case_id must be lowercase JUDGE-<UUIDv4>")
    if not isinstance(responses, Mapping):
        raise TypeError("responses must be a mapping")
    if len(responses) != len(STAGES) or set(responses) != set(STAGES):
        raise ValueError("responses must contain exactly all four response stages")
    for stage in STAGES:
        if not isinstance(responses[stage], str):
            raise TypeError(f"{stage} response must be a string")
    turns = model_turns(episode)
    return {
        "judge_case_id": judge_case_id,
        "turns": turns,
        "responses": [{"stage": stage, "content": responses[stage]}
                      for stage in STAGES],
    }
