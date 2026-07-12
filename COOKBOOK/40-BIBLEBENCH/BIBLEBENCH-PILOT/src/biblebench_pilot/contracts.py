from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import math
from typing import Any, Literal

Json = None | bool | int | float | str | list["Json"] | dict[str, "Json"]


def _assert_json(value: Any) -> None:
    if value is None or type(value) in {bool, int, str}:
        return
    if type(value) is float and math.isfinite(value):
        return
    if type(value) is list:
        for child in value:
            _assert_json(child)
        return
    if type(value) is dict and all(type(key) is str for key in value):
        for child in value.values():
            _assert_json(child)
        return
    raise ValueError("value is not strict canonical JSON")


def canonical_json_bytes(value: Json) -> bytes:
    _assert_json(value)
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")


def canonical_sha256(value: Json) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


@dataclass(frozen=True)
class CoreRef:
    core_id: str
    module: Literal["fruitbench", "corinthlove", "tencommandments", "sermonmount"]
    source_paths: tuple[str, ...]
    construct: str
    evidence_type: Literal["action", "artifact", "interpretation"]
    behavioral_attribution: Literal["applicable", "not_behaviorally_attributable"]


@dataclass(frozen=True)
class EpisodeRef:
    episode_id: str
    core_id: str
    split: Literal["public_calibration", "private_evaluation"]
    stratum: Literal["common_life", "christian_facing"]
    mode: Literal["judgment", "advice", "action"]
    transform_ids: tuple[str, ...]
    capability_twin_id: str | None
    actor_payload_sha256: str


@dataclass(frozen=True)
class SandboxEvent:
    sequence: int
    action: str
    actor: str
    target: str
    payload: dict[str, Json]


@dataclass(frozen=True)
class ArtifactEnvelope:
    artifact_type: str
    version: str
    created_at_utc: str
    payload: dict[str, Json]
    payload_sha256: str
