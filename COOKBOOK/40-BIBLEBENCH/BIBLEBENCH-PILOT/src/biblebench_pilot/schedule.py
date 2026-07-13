from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, replace
import json
import re
from typing import Any, Literal

from .artifacts import assert_actor_payload_safe
from .contracts import Json, canonical_json_bytes, canonical_sha256


__all__ = (
    "CueVariant",
    "DevelopmentEpisode",
    "DevelopmentPack",
    "EvidenceBundlePlan",
    "LogicalCall",
    "Schedule",
    "compile_schedule",
)


_CUES = ("C0", "C1", "C2")
_ROLES = ("target", "null", "restraint")
_MODULES = ("fruitbench", "corinthlove", "tencommandments", "sermonmount")
_HASH = re.compile(r"[0-9a-f]{64}")
_ID = re.compile(r"[0-9a-f]{16}")
_CUE_LABEL = re.compile(
    r"(?<![A-Za-z0-9])C[0-3](?![A-Za-z0-9])", re.IGNORECASE
)
_RESERVED_C3 = re.compile(
    r"(?<![A-Za-z0-9])C3(?![A-Za-z0-9])", re.IGNORECASE
)
_EMBEDDED_CUE_LABEL = re.compile(r"C[0-3]", re.IGNORECASE)
_OPAQUE_HEX = re.compile(r"(?:[0-9a-f]{16}|[0-9a-f]{64})")
_MAX_VISIBLE_DEPTH = 128
_CAMEL_KEY_BOUNDARY = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")
_NON_ALNUM_KEY = re.compile(r"[^a-z0-9]+")
_ALLOWED_TASK_ROUTE_KEYS = frozenset({"deliveryroute", "evacuationroute"})
_ALLOWED_FACTOR_KEYS = frozenset({"riskfactor"})
_BENIGN_PROTECTED_OCCURRENCES = {
    "actor": (
        ("contractor", 5),
        ("tractor", 2),
        ("extractor", 4),
    ),
    "cue": (("rescue", 3), ("barbecue", 5)),
    "gold": (("golden", 0), ("marigold", 4), ("goldfish", 0)),
    "intervention": (("interventional", 0),),
    "lens": (("lensing", 0), ("glens", 1)),
    "lenses": (("glens", 1),),
    "model": (("modeling", 0), ("remodel", 2)),
    "provider": (("providership", 0),),
    "providers": (("providership", 0),),
    "role": (("parole", 2),),
    "route": (("reroute", 2), ("enroute", 2)),
    "routes": (("reroute", 2), ("enroute", 2)),
    "schedule": (("reschedule", 2),),
}
_LATER_NAMESPACE_TOKENS = frozenset(
    {
        "lens",
        "lenses",
        "intervention",
        "interventions",
        "provider",
        "providers",
        "route",
        "routes",
    }
)
_PHYSICAL_RESERVED_TOKENS = frozenset(
    f"physical{qualifier}"
    for qualifier in (
        "id",
        "ids",
        "identifier",
        "identifiers",
        "call",
        "calls",
        "attempt",
        "attempts",
    )
)
_ATTEMPT_RESERVED_TOKENS = frozenset(
    f"{attempt}{identifier}"
    for attempt in ("attempt", "attempts")
    for identifier in ("id", "ids", "identifier", "identifiers")
)
_LATER_RESERVED_TOKENS = (
    _LATER_NAMESPACE_TOKENS
    | _PHYSICAL_RESERVED_TOKENS
    | _ATTEMPT_RESERVED_TOKENS
)
_BLIND_FORECAST_COMPONENTS = frozenset(
    {
        "cue",
        "condition",
        "actor",
        "model",
        "provider",
        "schedule",
        "bundle",
        "episode",
        "role",
        "expected",
        "gold",
        "private",
    }
)
_IDENTITY_RESERVED_TOKENS = frozenset({"actor", "model"})
_RESULT_RESERVED_TOKENS = frozenset({"expected", "gold", "groundtruth"})
_ACTOR_PRIVATE_RESERVED_TOKENS = frozenset({"role", "private"})


@dataclass(frozen=True)
class CueVariant:
    cue: Literal["C0", "C1", "C2"]
    cue_surface: str
    shared_body: str
    task_semantics_sha256: str
    answer_semantics_sha256: str
    tool_schema_sha256: str
    response_schema_sha256: str
    decoding: dict[str, Json]
    semantic_response_tokens: tuple[str, ...]


@dataclass(frozen=True)
class DevelopmentEpisode:
    episode_id: str
    role: Literal["target", "null", "restraint"]
    forecast_payload: dict[str, Json]
    probe_payload: dict[str, Json]
    variants: tuple[CueVariant, ...]


@dataclass(frozen=True)
class DevelopmentPack:
    module: Literal["fruitbench", "corinthlove", "tencommandments", "sermonmount"]
    episodes: tuple[DevelopmentEpisode, ...]

    @property
    def episode_count(self) -> int:
        return len(self.episodes)

    def role_counts(self) -> dict[str, int]:
        counts = Counter(episode.role for episode in self.episodes)
        return {role: counts[role] for role in _ROLES}


@dataclass(frozen=True)
class EvidenceBundlePlan:
    bundle_id: str
    actor_id: str
    module: Literal["fruitbench", "corinthlove", "tencommandments", "sermonmount"]
    episode_id: str
    role: Literal["target", "null", "restraint"]
    logical_call_ids: tuple[str, ...]


@dataclass(frozen=True)
class LogicalCall:
    logical_call_id: str
    bundle_id: str
    actor_id: str
    module: Literal["fruitbench", "corinthlove", "tencommandments", "sermonmount"]
    episode_id: str
    role: Literal["target", "null", "restraint"]
    call_kind: Literal["forecast", "primary", "probe"]
    cue: Literal["C0", "C1", "C2"] | None
    presentation_position: int
    request_payload: dict[str, Json]


@dataclass(frozen=True)
class Schedule:
    seed: int
    bundles: tuple[EvidenceBundlePlan, ...]
    logical_calls: tuple[LogicalCall, ...]

    @property
    def forecast_rows(self) -> tuple[LogicalCall, ...]:
        return tuple(row for row in self.logical_calls if row.call_kind == "forecast")

    @property
    def primary_rows(self) -> tuple[LogicalCall, ...]:
        return tuple(row for row in self.logical_calls if row.call_kind == "primary")

    @property
    def probe_rows(self) -> tuple[LogicalCall, ...]:
        return tuple(row for row in self.logical_calls if row.call_kind == "probe")

    def to_canonical_json(self) -> str:
        self.assert_counterbalanced()
        value: dict[str, Json] = {
            "seed": self.seed,
            "bundles": [_bundle_json(bundle) for bundle in self.bundles],
            "logical_calls": [_call_json(row) for row in self.logical_calls],
        }
        encoded = canonical_json_bytes(value).decode("utf-8")
        if _RESERVED_C3.search(encoded):
            raise ValueError("schedule contains reserved condition")
        return encoded

    def assert_counterbalanced(self) -> None:
        _assert_schedule_counterbalanced(self)


def _type_error(message: str) -> None:
    raise TypeError(message)


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def _strict_string(value: Any, name: str, *, nonempty: bool = True) -> str:
    if type(value) is not str:
        _type_error(f"{name} must be a string")
    if nonempty and not value.strip():
        raise ValueError(f"{name} must be nonempty")
    return value


def _opaque_hex_is_allowed(field_name: str | None, value: str) -> bool:
    if field_name is None or _OPAQUE_HEX.fullmatch(value) is None:
        return False
    normalized = _normalized_key(field_name)
    components = _key_components(field_name)
    return (
        normalized.endswith("sha256")
        or (bool(components) and components[-1] in {"id", "ids"})
    )


def _assert_no_c3(value: Any) -> None:
    stack: list[tuple[str, Any, int, str | None]] = [
        ("visit", value, 0, None)
    ]
    active: set[int] = set()
    while stack:
        operation, current, depth, field_name = stack.pop()
        if operation == "exit":
            active.remove(id(current))
            continue
        if type(current) is str:
            if field_name == "cue" and current in _CUES:
                continue
            if _opaque_hex_is_allowed(field_name, current):
                continue
            if _EMBEDDED_CUE_LABEL.search(current):
                raise ValueError("value contains a reserved condition label")
            continue
        if current is None or type(current) in {bool, int, float}:
            continue
        if type(current) not in {tuple, list, dict} and not hasattr(
            current, "__dict__"
        ):
            continue
        if depth >= _MAX_VISIBLE_DEPTH or id(current) in active:
            raise ValueError("value exceeds reserved-label traversal limits")
        active.add(id(current))
        stack.append(("exit", current, depth, field_name))
        if type(current) is dict:
            children = []
            for key, child in current.items():
                if type(key) is str and _EMBEDDED_CUE_LABEL.search(key):
                    raise ValueError("field contains a reserved condition label")
                children.append((child, key if type(key) is str else None))
        elif type(current) in {tuple, list}:
            children = [(child, field_name) for child in current]
        else:
            children = []
            for name, child in vars(current).items():
                if _EMBEDDED_CUE_LABEL.search(name):
                    raise ValueError("field contains a reserved condition label")
                children.append((child, name))
        for child, child_field in reversed(children):
            stack.append(("visit", child, depth + 1, child_field))


def _normalized_key(value: str) -> str:
    return "".join(character.casefold() for character in value if character.isalnum())


def _key_components(value: str) -> tuple[str, ...]:
    separated = _CAMEL_KEY_BOUNDARY.sub("_", value)
    return tuple(
        component
        for component in _NON_ALNUM_KEY.split(separated.casefold())
        if component
    )


def _walk_keys(value: Json):
    stack = [value]
    while stack:
        current = stack.pop()
        if type(current) is dict:
            for key, child in current.items():
                yield key
                stack.append(child)
        elif type(current) is list:
            stack.extend(current)


def _protected_occurrence_is_benign(
    normalized: str, protected: str, start: int
) -> bool:
    for context, offset in _BENIGN_PROTECTED_OCCURRENCES.get(protected, ()):
        context_start = start - offset
        if context_start >= 0 and normalized.startswith(context, context_start):
            return True
    return False


def _normalized_key_has_protected_occurrence(
    normalized: str,
    protected: frozenset[str],
    *,
    exact_allowed: frozenset[str] = frozenset(),
) -> bool:
    if not normalized or normalized in exact_allowed:
        return False
    for token in protected:
        start = normalized.find(token)
        while start >= 0:
            if not _protected_occurrence_is_benign(
                normalized, token, start
            ):
                return True
            start = normalized.find(token, start + 1)
    return False


def _assert_no_result_fields(payload: dict[str, Json]) -> None:
    for key in _walk_keys(payload):
        normalized = _normalized_key(key)
        if _normalized_key_has_protected_occurrence(
            normalized, _RESULT_RESERVED_TOKENS
        ):
            raise ValueError("request payload contains an outcome field")


def _assert_no_identity_fields(payload: dict[str, Json]) -> None:
    for key in _walk_keys(payload):
        normalized = _normalized_key(key)
        if _normalized_key_has_protected_occurrence(
            normalized,
            _IDENTITY_RESERVED_TOKENS,
            exact_allowed=_ALLOWED_FACTOR_KEYS,
        ):
            raise ValueError("request payload contains an identity field")


def _normalized_key_is_sealed(normalized: str) -> bool:
    return _normalized_key_has_protected_occurrence(
        normalized,
        _LATER_RESERVED_TOKENS,
        exact_allowed=_ALLOWED_TASK_ROUTE_KEYS,
    )


def _assert_no_later_scope_fields(payload: dict[str, Json]) -> None:
    for key in _walk_keys(payload):
        normalized = _normalized_key(key)
        has_sealed_component = not _LATER_NAMESPACE_TOKENS.isdisjoint(
            _key_components(key)
        )
        if _normalized_key_is_sealed(normalized) or (
            normalized not in _ALLOWED_TASK_ROUTE_KEYS
            and has_sealed_component
        ):
            raise ValueError("request payload contains a later-scope field")


def _assert_no_actor_metadata_fields(payload: dict[str, Json]) -> None:
    for key in _walk_keys(payload):
        normalized = _normalized_key(key)
        if _normalized_key_has_protected_occurrence(
            normalized, _ACTOR_PRIVATE_RESERVED_TOKENS
        ):
            raise ValueError("request payload contains actor-private metadata")


def _assert_blind_forecast(payload: dict[str, Json]) -> None:
    for key in _walk_keys(payload):
        normalized = _normalized_key(key)
        if _normalized_key_has_protected_occurrence(
            normalized,
            _BLIND_FORECAST_COMPONENTS,
            exact_allowed=_ALLOWED_FACTOR_KEYS,
        ):
            raise ValueError("forecast payload contains blinded metadata")


def _validate_payload(value: Any, name: str) -> dict[str, Json]:
    if type(value) is not dict:
        _type_error(f"{name} must be a dictionary")
    canonical_json_bytes(value)
    _assert_no_result_fields(value)
    _assert_no_later_scope_fields(value)
    _assert_no_actor_metadata_fields(value)
    return value


def _detached(value: dict[str, Json]) -> dict[str, Json]:
    detached = json.loads(canonical_json_bytes(value).decode("utf-8"))
    if type(detached) is not dict:
        raise ValueError("detached payload is not an object")
    return detached


def _checked_actor_payload(value: dict[str, Json]) -> dict[str, Json]:
    assert_actor_payload_safe(value)
    _validate_payload(value, "request_payload")
    _assert_no_identity_fields(value)
    return value


def _checked_forecast_payload(value: dict[str, Json]) -> dict[str, Json]:
    _checked_actor_payload(value)
    _assert_blind_forecast(value)
    return value


def _validate_variant(variant: Any) -> CueVariant:
    if type(variant) is not CueVariant:
        _type_error("variants must contain CueVariant values")
    if type(variant.cue) is not str or variant.cue not in _CUES:
        raise ValueError("invalid cue")
    _strict_string(variant.cue_surface, "cue_surface")
    if _CUE_LABEL.search(variant.cue_surface):
        raise ValueError("cue_surface exposes an internal cue label")
    _strict_string(variant.shared_body, "shared_body")
    for name in (
        "task_semantics_sha256",
        "answer_semantics_sha256",
        "tool_schema_sha256",
        "response_schema_sha256",
    ):
        value = getattr(variant, name)
        if type(value) is not str or _HASH.fullmatch(value) is None:
            raise ValueError(f"{name} must be lowercase SHA-256")
    if type(variant.decoding) is not dict:
        _type_error("decoding must be a dictionary")
    canonical_json_bytes(variant.decoding)
    if type(variant.semantic_response_tokens) is not tuple:
        _type_error("semantic_response_tokens must be a tuple")
    if not variant.semantic_response_tokens:
        raise ValueError("semantic_response_tokens must be nonempty")
    for token in variant.semantic_response_tokens:
        _strict_string(token, "semantic response token")
    return variant


def _validate_episode(episode: Any) -> DevelopmentEpisode:
    if type(episode) is not DevelopmentEpisode:
        _type_error("episodes must contain DevelopmentEpisode values")
    _strict_string(episode.episode_id, "episode_id")
    if type(episode.role) is not str or episode.role not in _ROLES:
        raise ValueError("invalid episode role")
    _validate_payload(episode.forecast_payload, "forecast_payload")
    probe_payload = _validate_payload(episode.probe_payload, "probe_payload")
    _assert_no_identity_fields(probe_payload)
    if "primary_logical_call_id" in probe_payload:
        raise ValueError("probe payload reserves primary_logical_call_id")
    if type(episode.variants) is not tuple:
        _type_error("variants must be a tuple")
    if len(episode.variants) != 3:
        raise ValueError("each episode must have exactly three variants")
    variants = tuple(_validate_variant(variant) for variant in episode.variants)
    by_cue = {variant.cue: variant for variant in variants}
    if len(by_cue) != 3 or set(by_cue) != set(_CUES):
        raise ValueError("variants must contain exactly C0, C1, and C2")

    ordered = tuple(by_cue[cue] for cue in _CUES)
    baseline = ordered[0]
    invariant_names = (
        "task_semantics_sha256",
        "answer_semantics_sha256",
        "tool_schema_sha256",
        "response_schema_sha256",
        "semantic_response_tokens",
    )
    baseline_body = baseline.shared_body.encode("utf-8")
    baseline_decoding = canonical_json_bytes(baseline.decoding)
    for variant in ordered[1:]:
        if variant.shared_body.encode("utf-8") != baseline_body:
            raise ValueError("cue variants change the shared body")
        if any(getattr(variant, name) != getattr(baseline, name) for name in invariant_names):
            raise ValueError("cue variants change semantic invariants")
        if canonical_json_bytes(variant.decoding) != baseline_decoding:
            raise ValueError("cue variants change decoding")
    surfaces = [variant.cue_surface for variant in ordered]
    if len(set(surfaces)) != 3:
        raise ValueError("cue surfaces must be distinct")
    return episode


def _validate_pack(pack: Any) -> DevelopmentPack:
    if type(pack) is not DevelopmentPack:
        _type_error("pack must be a DevelopmentPack")
    _assert_no_c3(pack)
    if type(pack.module) is not str or pack.module not in _MODULES:
        raise ValueError("invalid module")
    if type(pack.episodes) is not tuple:
        _type_error("episodes must be a tuple")
    if len(pack.episodes) != 12:
        raise ValueError("development pack must contain exactly 12 episodes")
    episodes = tuple(_validate_episode(episode) for episode in pack.episodes)
    episode_ids = [episode.episode_id for episode in episodes]
    if len(set(episode_ids)) != len(episode_ids):
        raise ValueError("episode IDs must be unique")
    if Counter(episode.role for episode in episodes) != Counter(
        {"target": 4, "null": 4, "restraint": 4}
    ):
        raise ValueError("development roles must be balanced 4/4/4")
    return pack


def _validate_actor_ids(actor_ids: Any) -> tuple[str, ...]:
    if type(actor_ids) is not tuple:
        _type_error("actor_ids must be a tuple")
    if len(actor_ids) != 4:
        raise ValueError("exactly four actor IDs are required")
    for actor_id in actor_ids:
        _strict_string(actor_id, "actor_id")
    if len(set(actor_ids)) != 4:
        raise ValueError("actor IDs must be unique")
    return tuple(sorted(actor_ids))


def _bundle_id(
    *,
    seed: int,
    actor_id: str,
    module: str,
    episode_id: str,
    role: str,
    logical_call_ids: tuple[str, ...],
) -> str:
    material: dict[str, Json] = {
        "domain": "biblebench.bundle.v1",
        "seed": seed,
        "actor_id": actor_id,
        "module": module,
        "episode_id": episode_id,
        "role": role,
        "logical_call_ids": list(logical_call_ids),
    }
    return canonical_sha256(material)[:16]


def _logical_call_id(
    *,
    seed: int,
    actor_id: str,
    module: str,
    episode_id: str,
    role: str,
    call_kind: str,
    cue: str | None,
    presentation_position: int,
    request_payload: dict[str, Json],
) -> str:
    material: dict[str, Json] = {
        "domain": "biblebench.logical_call.v1",
        "seed": seed,
        "actor_id": actor_id,
        "module": module,
        "episode_id": episode_id,
        "role": role,
        "call_kind": call_kind,
        "cue": cue,
        "presentation_position": presentation_position,
        "request_payload_sha256": canonical_sha256(request_payload),
    }
    return canonical_sha256(material)[:16]


def _new_call(
    *,
    seed: int,
    actor_id: str,
    module: str,
    episode_id: str,
    role: str,
    call_kind: Literal["forecast", "primary", "probe"],
    cue: Literal["C0", "C1", "C2"] | None,
    presentation_position: int,
    request_payload: dict[str, Json],
) -> LogicalCall:
    return LogicalCall(
        logical_call_id=_logical_call_id(
            seed=seed,
            actor_id=actor_id,
            module=module,
            episode_id=episode_id,
            role=role,
            call_kind=call_kind,
            cue=cue,
            presentation_position=presentation_position,
            request_payload=request_payload,
        ),
        bundle_id="",
        actor_id=actor_id,
        module=module,
        episode_id=episode_id,
        role=role,
        call_kind=call_kind,
        cue=cue,
        presentation_position=presentation_position,
        request_payload=request_payload,
    )


def compile_schedule(
    pack: DevelopmentPack,
    actor_ids: tuple[str, ...],
    seed: int,
) -> Schedule:
    pack = _validate_pack(pack)
    actors = _validate_actor_ids(actor_ids)
    if type(seed) is not int:
        _type_error("seed must be an integer")

    episodes = tuple(sorted(pack.episodes, key=lambda episode: episode.episode_id))
    actor_index = {actor: index for index, actor in enumerate(actors)}
    role_index = {role: index for index, role in enumerate(_ROLES)}
    role_seen: Counter[str] = Counter()
    role_ordinal: dict[str, int] = {}
    for episode in episodes:
        role_ordinal[episode.episode_id] = role_seen[episode.role]
        role_seen[episode.role] += 1
    bundles: list[EvidenceBundlePlan] = []
    logical_calls: list[LogicalCall] = []

    for episode_index, episode in enumerate(episodes):
        actor_offset = (seed + episode_index) % len(actors)
        actor_order = actors[actor_offset:] + actors[:actor_offset]
        variants = {variant.cue: variant for variant in episode.variants}
        for actor_id in actor_order:
            bundle_calls: list[LogicalCall] = []
            forecast = _new_call(
                seed=seed,
                actor_id=actor_id,
                module=pack.module,
                episode_id=episode.episode_id,
                role=episode.role,
                call_kind="forecast",
                cue=None,
                presentation_position=-1,
                request_payload=_checked_forecast_payload(
                    _detached(episode.forecast_payload)
                ),
            )
            bundle_calls.append(forecast)

            cue_offset = (
                seed
                + actor_index[actor_id]
                + role_index[episode.role]
                + role_ordinal[episode.episode_id]
            ) % 3
            cue_order = _CUES[cue_offset:] + _CUES[:cue_offset]
            for position, cue in enumerate(cue_order):
                variant = variants[cue]
                primary_payload: dict[str, Json] = {
                    "shared_body": variant.shared_body,
                    "cue_surface": variant.cue_surface,
                    "semantic_response_tokens": list(variant.semantic_response_tokens),
                }
                primary = _new_call(
                    seed=seed,
                    actor_id=actor_id,
                    module=pack.module,
                    episode_id=episode.episode_id,
                    role=episode.role,
                    call_kind="primary",
                    cue=cue,
                    presentation_position=position,
                    request_payload=_checked_actor_payload(
                        _detached(primary_payload)
                    ),
                )
                probe_payload = _detached(episode.probe_payload)
                probe_payload["primary_logical_call_id"] = primary.logical_call_id
                _checked_actor_payload(probe_payload)
                probe = _new_call(
                    seed=seed,
                    actor_id=actor_id,
                    module=pack.module,
                    episode_id=episode.episode_id,
                    role=episode.role,
                    call_kind="probe",
                    cue=cue,
                    presentation_position=position,
                    request_payload=probe_payload,
                )
                bundle_calls.extend((primary, probe))

            logical_call_ids = tuple(
                row.logical_call_id for row in bundle_calls
            )
            bundle_id = _bundle_id(
                seed=seed,
                actor_id=actor_id,
                module=pack.module,
                episode_id=episode.episode_id,
                role=episode.role,
                logical_call_ids=logical_call_ids,
            )
            bundle_calls = [
                replace(row, bundle_id=bundle_id) for row in bundle_calls
            ]
            bundles.append(
                EvidenceBundlePlan(
                    bundle_id=bundle_id,
                    actor_id=actor_id,
                    module=pack.module,
                    episode_id=episode.episode_id,
                    role=episode.role,
                    logical_call_ids=logical_call_ids,
                )
            )
            logical_calls.extend(bundle_calls)

    schedule = Schedule(seed=seed, bundles=tuple(bundles), logical_calls=tuple(logical_calls))
    schedule.assert_counterbalanced()
    return schedule


def _bundle_json(bundle: EvidenceBundlePlan) -> dict[str, Json]:
    return {
        "bundle_id": bundle.bundle_id,
        "actor_id": bundle.actor_id,
        "module": bundle.module,
        "episode_id": bundle.episode_id,
        "role": bundle.role,
        "logical_call_ids": list(bundle.logical_call_ids),
    }


def _call_json(row: LogicalCall) -> dict[str, Json]:
    return {
        "logical_call_id": row.logical_call_id,
        "bundle_id": row.bundle_id,
        "actor_id": row.actor_id,
        "module": row.module,
        "episode_id": row.episode_id,
        "role": row.role,
        "call_kind": row.call_kind,
        "cue": row.cue,
        "presentation_position": row.presentation_position,
        "request_payload": row.request_payload,
    }


def _validate_scheduled_bundle(bundle: Any) -> EvidenceBundlePlan:
    if type(bundle) is not EvidenceBundlePlan:
        _type_error("schedule bundles must be EvidenceBundlePlan values")
    for name in ("bundle_id", "actor_id", "module", "episode_id", "role"):
        _strict_string(getattr(bundle, name), name)
    if _ID.fullmatch(bundle.bundle_id) is None:
        raise ValueError("invalid bundle ID")
    if bundle.module not in _MODULES or bundle.role not in _ROLES:
        raise ValueError("invalid bundle metadata")
    if type(bundle.logical_call_ids) is not tuple or len(bundle.logical_call_ids) != 7:
        raise ValueError("bundle must name exactly seven logical calls")
    if any(
        type(identifier) is not str or _ID.fullmatch(identifier) is None
        for identifier in bundle.logical_call_ids
    ):
        raise ValueError("invalid bundled logical call ID")
    return bundle


def _validate_scheduled_call(row: Any) -> LogicalCall:
    if type(row) is not LogicalCall:
        _type_error("schedule calls must be LogicalCall values")
    for name in ("logical_call_id", "bundle_id", "actor_id", "module", "episode_id", "role"):
        _strict_string(getattr(row, name), name)
    if _ID.fullmatch(row.logical_call_id) is None or _ID.fullmatch(row.bundle_id) is None:
        raise ValueError("invalid logical call ID")
    if row.module not in _MODULES or row.role not in _ROLES:
        raise ValueError("invalid logical call metadata")
    if type(row.call_kind) is not str or row.call_kind not in {"forecast", "primary", "probe"}:
        raise ValueError("invalid call kind")
    if row.cue is not None and (type(row.cue) is not str or row.cue not in _CUES):
        raise ValueError("invalid scheduled cue")
    if type(row.presentation_position) is not int:
        _type_error("presentation position must be an integer")
    if row.call_kind == "forecast":
        _checked_forecast_payload(row.request_payload)
    else:
        _checked_actor_payload(row.request_payload)
    return row


def _assert_call_identity(row: LogicalCall, bundle: EvidenceBundlePlan, seed: int) -> None:
    if (
        row.bundle_id,
        row.actor_id,
        row.module,
        row.episode_id,
        row.role,
    ) != (
        bundle.bundle_id,
        bundle.actor_id,
        bundle.module,
        bundle.episode_id,
        bundle.role,
    ):
        raise ValueError("logical call metadata does not match its bundle")
    expected = _logical_call_id(
        seed=seed,
        actor_id=row.actor_id,
        module=row.module,
        episode_id=row.episode_id,
        role=row.role,
        call_kind=row.call_kind,
        cue=row.cue,
        presentation_position=row.presentation_position,
        request_payload=row.request_payload,
    )
    if row.logical_call_id != expected:
        raise ValueError("logical call ID does not match its identity")


def _assert_primary_payload(payload: dict[str, Json]) -> None:
    if set(payload) != {"shared_body", "cue_surface", "semantic_response_tokens"}:
        raise ValueError("primary request payload has unexpected fields")
    _strict_string(payload["shared_body"], "shared_body")
    _strict_string(payload["cue_surface"], "cue_surface")
    if _CUE_LABEL.search(payload["cue_surface"]):
        raise ValueError("primary request exposes an internal cue label")
    tokens = payload["semantic_response_tokens"]
    if type(tokens) is not list or not tokens:
        raise ValueError("primary semantic response tokens must be a nonempty list")
    for token in tokens:
        _strict_string(token, "semantic response token")


def _assert_detached_call_payloads(calls: tuple[LogicalCall, ...]) -> None:
    seen: set[int] = set()

    def visit(value: Json) -> None:
        if type(value) not in {dict, list}:
            return
        identifier = id(value)
        if identifier in seen:
            raise ValueError("logical call payloads must not share mutable aliases")
        seen.add(identifier)
        children = value.values() if type(value) is dict else value
        for child in children:
            visit(child)

    for row in calls:
        visit(row.request_payload)


def _record_cross_actor_semantics(
    baselines: dict[str | tuple[str, str], tuple[bytes, int]],
    key: str | tuple[str, str],
    payload: dict[str, Json],
    message: str,
) -> None:
    encoded = canonical_json_bytes(payload)
    prior = baselines.get(key)
    if prior is None:
        baselines[key] = (encoded, 1)
        return
    prior_bytes, count = prior
    if encoded != prior_bytes:
        raise ValueError(message)
    baselines[key] = (prior_bytes, count + 1)


def _assert_schedule_counterbalanced(schedule: Schedule) -> None:
    if type(schedule) is not Schedule:
        _type_error("value must be a Schedule")
    if type(schedule.seed) is not int:
        _type_error("schedule seed must be an integer")
    if type(schedule.bundles) is not tuple or type(schedule.logical_calls) is not tuple:
        _type_error("schedule collections must be tuples")
    if len(schedule.bundles) != 48 or len(schedule.logical_calls) != 336:
        raise ValueError("schedule must contain 48 bundles and 336 logical calls")
    _assert_no_c3(schedule)

    bundles = tuple(_validate_scheduled_bundle(bundle) for bundle in schedule.bundles)
    calls = tuple(_validate_scheduled_call(row) for row in schedule.logical_calls)
    _assert_detached_call_payloads(calls)
    actors = tuple(sorted({bundle.actor_id for bundle in bundles}))
    episodes = tuple(sorted({bundle.episode_id for bundle in bundles}))
    modules = {bundle.module for bundle in bundles}
    if len(actors) != 4 or len(episodes) != 12 or len(modules) != 1:
        raise ValueError("schedule has invalid actor, episode, or module membership")
    if len({(bundle.actor_id, bundle.episode_id) for bundle in bundles}) != 48:
        raise ValueError("actor/episode bundles must be unique")

    episode_roles: dict[str, str] = {}
    for bundle in bundles:
        prior = episode_roles.setdefault(bundle.episode_id, bundle.role)
        if prior != bundle.role:
            raise ValueError("episode role changes across actors")
    if Counter(episode_roles.values()) != Counter({"target": 4, "null": 4, "restraint": 4}):
        raise ValueError("episode roles are not balanced")

    expected_pairs: list[tuple[str, str]] = []
    for episode_index, episode_id in enumerate(episodes):
        actor_offset = (schedule.seed + episode_index) % 4
        actor_order = actors[actor_offset:] + actors[:actor_offset]
        expected_pairs.extend((actor, episode_id) for actor in actor_order)
    if [(bundle.actor_id, bundle.episode_id) for bundle in bundles] != expected_pairs:
        raise ValueError("global bundle order is not counterbalanced")

    actor_index = {actor: index for index, actor in enumerate(actors)}
    role_index = {role: index for index, role in enumerate(_ROLES)}
    role_seen: Counter[str] = Counter()
    role_ordinal: dict[str, int] = {}
    for episode_id in episodes:
        role = episode_roles[episode_id]
        role_ordinal[episode_id] = role_seen[role]
        role_seen[role] += 1
    cue_position_counts: Counter[tuple[str, int, str]] = Counter()
    role_position_counts: Counter[tuple[str, str, int, str]] = Counter()
    all_ids = [bundle.bundle_id for bundle in bundles]
    forecast_semantics: dict[str | tuple[str, str], tuple[bytes, int]] = {}
    primary_semantics: dict[str | tuple[str, str], tuple[bytes, int]] = {}
    probe_semantics: dict[str | tuple[str, str], tuple[bytes, int]] = {}

    for bundle_number, bundle in enumerate(bundles):
        bundle_calls = calls[bundle_number * 7 : (bundle_number + 1) * 7]
        if bundle.logical_call_ids != tuple(row.logical_call_id for row in bundle_calls):
            raise ValueError("bundle logical call IDs do not match global call order")
        expected_bundle_id = _bundle_id(
            seed=schedule.seed,
            actor_id=bundle.actor_id,
            module=bundle.module,
            episode_id=bundle.episode_id,
            role=bundle.role,
            logical_call_ids=bundle.logical_call_ids,
        )
        if bundle.bundle_id != expected_bundle_id:
            raise ValueError("bundle ID does not match its identity")
        for row in bundle_calls:
            _assert_call_identity(row, bundle, schedule.seed)
            all_ids.append(row.logical_call_id)

        forecast = bundle_calls[0]
        if (
            forecast.call_kind != "forecast"
            or forecast.cue is not None
            or forecast.presentation_position != -1
        ):
            raise ValueError("forecast must be first and condition independent")
        if "primary_logical_call_id" in forecast.request_payload:
            raise ValueError("forecast payload references a condition-specific call")
        _record_cross_actor_semantics(
            forecast_semantics,
            bundle.episode_id,
            forecast.request_payload,
            "forecast semantics change across actors",
        )

        cue_offset = (
            schedule.seed
            + actor_index[bundle.actor_id]
            + role_index[bundle.role]
            + role_ordinal[bundle.episode_id]
        ) % 3
        cue_order = _CUES[cue_offset:] + _CUES[:cue_offset]
        bodies: list[str] = []
        token_sequences: list[tuple[str, ...]] = []
        surfaces: list[str] = []
        for position, cue in enumerate(cue_order):
            primary = bundle_calls[1 + position * 2]
            probe = bundle_calls[2 + position * 2]
            if (
                primary.call_kind != "primary"
                or probe.call_kind != "probe"
                or primary.cue != cue
                or probe.cue != cue
                or primary.presentation_position != position
                or probe.presentation_position != position
            ):
                raise ValueError("primary/probe sequence is not counterbalanced")
            _assert_primary_payload(primary.request_payload)
            _assert_no_identity_fields(probe.request_payload)
            if probe.request_payload.get("primary_logical_call_id") != primary.logical_call_id:
                raise ValueError("probe does not reference its immediately preceding primary")
            semantic_key = (bundle.episode_id, cue)
            _record_cross_actor_semantics(
                primary_semantics,
                semantic_key,
                primary.request_payload,
                "primary semantics change across actors",
            )
            probe_base = {
                key: value
                for key, value in probe.request_payload.items()
                if key != "primary_logical_call_id"
            }
            _record_cross_actor_semantics(
                probe_semantics,
                semantic_key,
                probe_base,
                "probe semantics change across actors",
            )
            bodies.append(primary.request_payload["shared_body"])
            surfaces.append(primary.request_payload["cue_surface"])
            token_sequences.append(tuple(primary.request_payload["semantic_response_tokens"]))
            cue_position_counts[(bundle.actor_id, position, cue)] += 1
            role_position_counts[
                (bundle.actor_id, bundle.role, position, cue)
            ] += 1
        if len(set(bodies)) != 1 or len(set(token_sequences)) != 1 or len(set(surfaces)) != 3:
            raise ValueError("condition payload semantics are not invariant")

    if (
        len(forecast_semantics) != 12
        or len(primary_semantics) != 36
        or len(probe_semantics) != 36
        or any(count != 4 for _, count in forecast_semantics.values())
        or any(count != 4 for _, count in primary_semantics.values())
        or any(count != 4 for _, count in probe_semantics.values())
    ):
        raise ValueError("actor-visible semantics are not complete across actors")

    if len(all_ids) != len(set(all_ids)):
        raise ValueError("schedule identifiers must be globally unique")
    for actor in actors:
        for position in range(3):
            for cue in _CUES:
                if cue_position_counts[(actor, position, cue)] != 4:
                    raise ValueError("cue positions are not balanced within actor")
            for role in _ROLES:
                counts = [
                    role_position_counts[(actor, role, position, cue)]
                    for cue in _CUES
                ]
                if max(counts) - min(counts) > 1 or max(counts) == 4:
                    raise ValueError("cue positions are not balanced within role")
