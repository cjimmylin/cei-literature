from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import math
from typing import Any, Literal

Json = None | bool | int | float | str | list["Json"] | dict[str, "Json"]
_MAX_JSON_DEPTH = 128  # Maximum number of nested list/dict containers.


def _assert_json(value: Any) -> None:
    _assert_json_at_depth(value, active_container_ids=set(), depth=0)


def _assert_json_at_depth(
    value: Any,
    *,
    active_container_ids: set[int],
    depth: int,
) -> None:
    if value is None or type(value) in {bool, int}:
        return
    if type(value) is str:
        if any(0xD800 <= ord(character) <= 0xDFFF for character in value):
            raise ValueError("value is not strict canonical JSON")
        return
    if type(value) is float and math.isfinite(value):
        return

    if type(value) in {list, dict}:
        if depth >= _MAX_JSON_DEPTH or id(value) in active_container_ids:
            raise ValueError("value is not strict canonical JSON")

        if type(value) is dict:
            for key in value:
                if type(key) is not str:
                    raise ValueError("value is not strict canonical JSON")
                _assert_json_at_depth(
                    key,
                    active_container_ids=active_container_ids,
                    depth=depth + 1,
                )

        active_container_ids.add(id(value))
        try:
            children = value if type(value) is list else value.values()
            for child in children:
                _assert_json_at_depth(
                    child,
                    active_container_ids=active_container_ids,
                    depth=depth + 1,
                )
        finally:
            active_container_ids.remove(id(value))
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
