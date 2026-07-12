"""Strict public payload projections for CROSSROADS.

Only enacted phase scripts, executable tools/affordances, and consequences
already visible in the simulated world cross the candidate boundary.  Hidden
keys, bank identity, canaries, and simulant branch logic are rejected even when
nested inside otherwise public objects.
"""
from __future__ import annotations

from copy import deepcopy
from collections.abc import Mapping
import json
import re
import uuid

try:
    from .judge_cases import OccurrenceCaseRegistry, canonical_response_sha256
except ImportError:  # direct ``lib`` path execution in focused tests/tools
    from judge_cases import OccurrenceCaseRegistry, canonical_response_sha256


STAGES = ("stage_1", "stage_2", "stage_3", "stage_4")
MODEL_PAYLOAD_KEYS = {
    "stages", "tools", "affordances", "visible_consequences",
}
FORBIDDEN_KEYS = {
    "id", "item_id", "episode_id", "occurrence_id", "design",
    "authoring_seed", "judge_seed", "jseed", "run_id", "execution_id",
    "response_sha256", "scoring_occurrence",
    "model_id", "logical_model_id", "provider_model_id", "configuration_id",
    "candidate_family", "candidate_model_snapshot", "model_snapshot",
    "verse_anchors", "template_family", "split", "canary", "canary_id",
    "judge_id", "judge_ids", "sidecar", "ground_truth", "hidden",
    "hidden_state", "parameter_state", "path_key", "path_keys", "key",
    "key_plus", "key_minus", "clause", "clause_id", "clause_sign",
    "reaction_table", "reaction_tables", "branch_table", "branch_tables",
    "simulant_program", "expected_behavior", "failure_modes",
    "rubric_emphases", "hardness", "hardness_result",
    "option", "option_id", "path_id", "choice_id", "affordance_id",
}
_CANARY_RE = re.compile(r"10CB3-01-[0-9a-f-]+", re.IGNORECASE)
_ITEM_RE = re.compile(r"\bCROSSROADS-[A-Z0-9-]+\b", re.IGNORECASE)
_SCENARIO_RE = re.compile(r"\bXR-SCN-[A-Z0-9-]+\b", re.IGNORECASE)
_PATH_LABEL_RE = re.compile(
    r"\b(?:path|plan|route|option)\s*[- ]?\d+\b", re.IGNORECASE
)
_JUDGE_RE = re.compile(r"\bJUDGE-[0-9a-f-]+\b", re.IGNORECASE)
_JCASE_RE = re.compile(r"\bJCASE-[0-9a-f-]+\b", re.IGNORECASE)
_JSEED_RE = re.compile(r"\bJSEED-[0-9a-f-]+\b", re.IGNORECASE)
_CLAUSE_SIGN_RE = re.compile(
    r"\bC(?:[1-9]|1[0-6])\s*(?:\+|-|plus\b|minus\b)", re.IGNORECASE
)
_JCASE_UUID_RE = re.compile(
    r"^JCASE-[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-"
    r"[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
)


def canonical_text(value) -> str:
    """Return stable JSON text after proving *value* is JSON-safe."""
    try:
        return json.dumps(
            value, sort_keys=True, separators=(",", ":"),
            ensure_ascii=False, allow_nan=False,
        )
    except (TypeError, ValueError):
        raise ValueError("payload must be canonical JSON data") from None


def _assert_public(value, path: str = "payload") -> None:
    if isinstance(value, Mapping):
        for key, item in value.items():
            if not isinstance(key, str):
                raise ValueError(f"forbidden non-string key at {path}")
            if key.strip().lower().replace("-", "_") in FORBIDDEN_KEYS:
                raise ValueError(f"forbidden field at {path}.{key}")
            _assert_public(item, f"{path}.{key}")
    elif isinstance(value, (list, tuple)):
        for index, item in enumerate(value):
            _assert_public(item, f"{path}[{index}]")
    elif isinstance(value, str):
        if any(pattern.search(value) for pattern in (
                _CANARY_RE, _ITEM_RE, _SCENARIO_RE,
                _JUDGE_RE, _JCASE_RE, _JSEED_RE,
                _CLAUSE_SIGN_RE, _PATH_LABEL_RE)):
            raise ValueError(f"forbidden hidden or identifying text at {path}")
    elif value is not None and type(value) not in {bool, int, float}:
        raise ValueError(f"forbidden non-JSON value at {path}")


def _public_turn(value, path: str):
    if isinstance(value, str):
        if not value.strip():
            raise ValueError(f"{path} must be non-empty")
        return value
    if isinstance(value, Mapping):
        if not value:
            raise ValueError(f"{path} must be non-empty")
        return deepcopy(value)
    raise ValueError(f"{path} must be a public turn object or string")


def _stages(episode: Mapping) -> list[dict]:
    script = episode.get("multiturn_script")
    if not isinstance(script, Mapping) or set(script) != set(STAGES):
        raise ValueError("multiturn_script must contain exactly stage_1..stage_4")
    result, total = [], 0
    for stage in STAGES:
        turns = script[stage]
        if not isinstance(turns, list) or not turns:
            raise ValueError(f"{stage} must be a non-empty turn list")
        if stage == "stage_3" and not 3 <= len(turns) <= 8:
            raise ValueError("stage_3 must contain three to eight follow-through turns")
        projected = [
            _public_turn(turn, f"{stage}[{index}]")
            for index, turn in enumerate(turns)
        ]
        total += len(projected)
        result.append({"stage": stage, "turns": projected})
    if not 8 <= total <= 20:
        raise ValueError("episode must contain 8 to 20 public turns")
    return result


def build_model_payload(episode: Mapping) -> dict:
    """Project one authored episode into the complete candidate interface."""
    if not isinstance(episode, Mapping):
        raise TypeError("episode must be a mapping")
    tools = episode.get("tools")
    affordances = episode.get("affordances")
    consequences = episode.get("visible_consequences")
    if not isinstance(tools, list) or not tools:
        raise ValueError("tools must be a non-empty list")
    if not isinstance(affordances, list) or len(affordances) not in {3, 4}:
        raise ValueError("episode must expose exactly three or four affordances")
    if not isinstance(consequences, list):
        raise ValueError("visible_consequences must be a list")
    signatures = []
    for index, affordance in enumerate(affordances):
        if not isinstance(affordance, Mapping) or set(affordance) != {
                "tool", "target", "operation", "arguments", "description"}:
            raise ValueError(
                "every affordance requires exactly tool, target, and operation "
                "plus arguments and description"
            )
        if any(
                not isinstance(affordance[field], str)
                or not affordance[field].strip()
                for field in ("tool", "target", "operation", "description")):
            raise ValueError(f"affordance {index} public strings must be non-empty")
        if not isinstance(affordance["arguments"], Mapping):
            raise ValueError(f"affordance {index} arguments must be a mapping")
        signatures.append(tuple(
            affordance[field] for field in ("tool", "target", "operation")
        ))
    if len(signatures) != len(set(signatures)):
        raise ValueError("affordances require unique tool/target/operation signatures")
    payload = {
        "stages": _stages(episode),
        "tools": deepcopy(tools),
        "affordances": deepcopy(affordances),
        "visible_consequences": deepcopy(consequences),
    }
    if set(payload) != MODEL_PAYLOAD_KEYS:
        raise AssertionError("candidate payload projection changed")
    _assert_public(payload)
    canonical_text(payload)
    return payload


def model_visible_text(episode: Mapping) -> str:
    """Flatten the exact candidate payload for leakage/static audits."""
    return canonical_text(build_model_payload(episode))


def is_opaque_case_id(value: object) -> bool:
    if not isinstance(value, str) or _JCASE_UUID_RE.fullmatch(value) is None:
        return False
    parsed = uuid.UUID(value.removeprefix("JCASE-"))
    return parsed.version == 4 and parsed.variant == uuid.RFC_4122


def build_judge_payload(*, judge_case_id: str, transcript,
                        observable_artifacts,
                        case_registry: OccurrenceCaseRegistry) -> dict:
    """Build a response-bound, condition-blind judge occurrence payload."""
    if not is_opaque_case_id(judge_case_id):
        raise ValueError("judge_case_id must be opaque JCASE-<UUIDv4>")
    if not isinstance(case_registry, OccurrenceCaseRegistry):
        raise TypeError("case_registry must be an OccurrenceCaseRegistry")
    if not isinstance(transcript, list) or not isinstance(
            observable_artifacts, list):
        raise TypeError("judge observables must be lists")
    body = {
        "judge_case_id": judge_case_id,
        "transcript": deepcopy(transcript),
        "observable_artifacts": deepcopy(observable_artifacts),
    }
    _assert_public(body["transcript"], "transcript")
    _assert_public(body["observable_artifacts"], "observable_artifacts")
    response_sha256 = canonical_response_sha256(
        body["transcript"], body["observable_artifacts"]
    )
    case_registry.assert_response_binding(judge_case_id, response_sha256)
    canonical_text(body)
    return body
