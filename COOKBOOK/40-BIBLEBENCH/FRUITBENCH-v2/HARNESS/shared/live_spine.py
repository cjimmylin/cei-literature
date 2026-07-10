"""Immutable live-run identities, blind judge envelopes, and role firewalls.

The public/scoring side of FRUITBENCH uses opaque principal IDs.  Exact model
identity stays catalog-bound and restricted, while Layer E receives only the
response and observable task evidence needed to code events.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
import json
import re
from typing import Any


_ACTOR_ROLES = frozenset(
    {
        "actor",
        "calibration",
        "evaluation",
        "held_out",
        "held_out_frontier",
        "item_generator",
    }
)
_JUDGE_ROLES = frozenset(
    {"judge", "primary_judge", "sensitivity_judge"}
)
_PRIMARY_JUDGE_ROLES = frozenset({"judge", "primary_judge"})
_HUMAN_ROLES = frozenset(
    {"adjudicator", "human", "human_judge", "human_rater", "panelist"}
)
_ROLE_ALIASES = {
    "actors": "actor",
    "evaluated_actor": "evaluation",
    "evaluated_actors": "evaluation",
    "heldout": "held_out_frontier",
    "held_out": "held_out_frontier",
    "human_raters": "human_rater",
    "humans": "human_rater",
    "item_generators": "item_generator",
    "judges": "primary_judge",
    "primary_judges": "primary_judge",
}
_OPAQUE_PATTERNS = {
    "actor": re.compile(r"A[0-9]{2}\Z"),
    "judge": re.compile(r"J[0-9]{2}\Z"),
    "human": re.compile(r"H[0-9]{3}\Z"),
}
_DIRECT_HIDDEN_TOKENS = frozenset(
    {
        "actor",
        "calibration",
        "canonical",
        "condition",
        "expected",
        "family",
        "fruit",
        "gold",
        "model",
        "opaque",
        "snapshot",
        "vendor",
        "version",
    }
)
_COMPACT_HIDDEN_PREFIXES = (
    "actorid",
    "actormodel",
    "calibration",
    "canonicalslug",
    "cuearm",
    "expected",
    "family",
    "fruit",
    "gold",
    "modelid",
    "modelsnapshot",
    "opaqueid",
    "snapshot",
    "taskarm",
    "vendor",
)
_SENSITIVE_ASSIGNMENT = re.compile(
    r"\b(?:actor|judge|human|rater|model|vendor|family|fruit|gold|cue[ _-]*arm|"
    r"task[ _-]*arm|condition|version)\b\s*[:=]",
    re.IGNORECASE,
)


def _nonblank(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a non-blank exact identity")
    if value != value.strip():
        raise ValueError(f"{field} must not contain surrounding whitespace")
    return value


def _normalise_role(role: Any) -> str:
    raw = _nonblank(role, "role")
    normalised = re.sub(r"[^a-z0-9]+", "_", raw.casefold()).strip("_")
    return _ROLE_ALIASES.get(normalised, normalised)


def _principal_kind(role: str) -> str:
    if role in _ACTOR_ROLES:
        return "actor"
    if role in _JUDGE_ROLES:
        return "judge"
    if role in _HUMAN_ROLES:
        return "human"
    raise ValueError(f"role is not a supported principal role: {role!r}")


@dataclass(frozen=True)
class Principal:
    """Restricted exact identity associated with one opaque public ID."""

    opaque_id: str
    role: str
    model_id: str
    canonical_slug: str
    vendor: str
    family: str

    def __post_init__(self) -> None:
        role = _normalise_role(self.role)
        kind = _principal_kind(role)
        opaque_id = _nonblank(self.opaque_id, "opaque_id")
        if _OPAQUE_PATTERNS[kind].fullmatch(opaque_id) is None:
            expected = {"actor": "A##", "judge": "J##", "human": "H###"}[kind]
            raise ValueError(
                f"opaque_id {opaque_id!r} does not match role {self.role!r}; "
                f"expected {expected}"
            )
        for field in ("model_id", "canonical_slug", "vendor", "family"):
            _nonblank(getattr(self, field), field)


def _key_tokens(key: str) -> tuple[str, ...]:
    with_acronyms = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", key)
    with_words = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", with_acronyms)
    return tuple(re.findall(r"[a-z0-9]+", with_words.casefold()))


def _hidden_key(tokens: tuple[str, ...], path: tuple[str, ...]) -> bool:
    if _DIRECT_HIDDEN_TOKENS.intersection(tokens):
        return True
    compact = "".join(tokens)
    if compact.startswith(_COMPACT_HIDDEN_PREFIXES):
        return True
    token_set = set(tokens)
    if {"cue", "arm"}.issubset(token_set) or {"task", "arm"}.issubset(token_set):
        return True
    if "judge" in token_set and "id" in token_set:
        return True
    if "human" in token_set and "id" in token_set:
        return True
    if "rater" in token_set and "id" in token_set:
        return True

    full_path = set(path).union(tokens)
    has_prior = bool({"earlier", "previous", "prior"}.intersection(full_path))
    has_ballot = bool({"ballot", "ballots", "vote", "votes"}.intersection(full_path))
    return has_prior and has_ballot


def _hidden_scalar_tokens(value: Any) -> frozenset[str]:
    tokens: set[str] = set()
    if isinstance(value, Mapping):
        for child in value.values():
            tokens.update(_hidden_scalar_tokens(child))
    elif isinstance(value, (list, tuple)):
        for child in value:
            tokens.update(_hidden_scalar_tokens(child))
    elif isinstance(value, str) and len(value.strip()) >= 2:
        tokens.add(value.strip().casefold())
    return frozenset(tokens)


def _sensitive_value(value: str, hidden_tokens: frozenset[str]) -> bool:
    if _SENSITIVE_ASSIGNMENT.search(value):
        return True
    folded = value.casefold()
    return any(
        re.search(rf"(?<![a-z0-9]){re.escape(token)}(?![a-z0-9])", folded)
        for token in hidden_tokens
    )


def _blind_value(
    value: Any,
    path: tuple[str, ...] = (),
    hidden_tokens: frozenset[str] = frozenset(),
) -> Any:
    if isinstance(value, Mapping):
        blinded: dict[str, Any] = {}
        for key in sorted(value):
            if not isinstance(key, str):
                raise ValueError("observable_context object keys must be strings")
            tokens = _key_tokens(key)
            if _hidden_key(tokens, path):
                continue
            blinded[key] = _blind_value(
                value[key], path + tokens, hidden_tokens
            )
        return blinded
    if isinstance(value, (list, tuple)):
        return [_blind_value(element, path, hidden_tokens) for element in value]
    if isinstance(value, str) and _sensitive_value(value, hidden_tokens):
        raise ValueError(
            "observable_context contains a sensitive hidden value under an allowed key"
        )
    return value


def blind_event_payload(
    *,
    response_text: str,
    observable_context: dict[str, Any],
    hidden_metadata: dict[str, Any],
) -> dict[str, Any]:
    """Build the label-free Layer-E envelope.

    ``hidden_metadata`` is deliberately never merged.  The observable context
    is independently sanitized as a defense in depth against misplaced nested
    metadata or case-style variations.
    """

    if not isinstance(response_text, str):
        raise ValueError("response_text must be a string")
    if not isinstance(observable_context, Mapping):
        raise ValueError("observable_context must be an object")
    if not isinstance(hidden_metadata, Mapping):
        raise ValueError("hidden_metadata must be an object")
    hidden_tokens = _hidden_scalar_tokens(hidden_metadata)
    return {
        "observable_context": _blind_value(
            observable_context, hidden_tokens=hidden_tokens
        ),
        "response_text": response_text,
    }


def canonical_json_bytes(value: Any) -> bytes:
    """Serialize a JSON value with a single deterministic byte representation."""

    try:
        text = json.dumps(
            value,
            allow_nan=False,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        )
    except (TypeError, ValueError) as exc:
        raise ValueError("value is not canonical JSON data") from exc
    return text.encode("utf-8")


def _catalog_index(catalog: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    data = catalog.get("data")
    if not isinstance(data, Sequence) or isinstance(data, (str, bytes, bytearray)):
        raise ValueError("catalog must contain a data list")
    records: dict[str, Mapping[str, Any]] = {}
    for index, raw in enumerate(data):
        if not isinstance(raw, Mapping):
            raise ValueError(f"catalog data[{index}] must be an object")
        model_id = _nonblank(raw.get("id"), f"catalog data[{index}].id")
        if model_id in records:
            raise ValueError(f"catalog has duplicate model_id {model_id!r}")
        records[model_id] = raw
    return records


def _role_from_group(group: Any) -> str:
    return _normalise_role(group)


def _config_rows(config: Mapping[str, Any]) -> list[tuple[str | None, Mapping[str, Any]]]:
    if "principals" in config:
        rows = config["principals"]
        if not isinstance(rows, Sequence) or isinstance(rows, (str, bytes, bytearray)):
            raise ValueError("config.principals must be a list")
        result: list[tuple[str | None, Mapping[str, Any]]] = []
        for index, row in enumerate(rows):
            if not isinstance(row, Mapping):
                raise ValueError(f"config.principals[{index}] must be an object")
            result.append((None, row))
        return result

    roles = config.get("roles")
    if not isinstance(roles, Mapping):
        raise ValueError("config must contain principals or roles")
    grouped: list[tuple[str | None, Mapping[str, Any]]] = []
    for group, rows in roles.items():
        if not isinstance(rows, Sequence) or isinstance(rows, (str, bytes, bytearray)):
            raise ValueError(f"config role {group!r} must be a list")
        role = _role_from_group(group)
        for index, row in enumerate(rows):
            if not isinstance(row, Mapping):
                raise ValueError(f"config role {group!r}[{index}] must be an object")
            grouped.append((role, row))
    return grouped


def _opaque_id(row: Mapping[str, Any]) -> Any:
    for key in ("opaque_id", "actor_id", "judge_id", "human_rater_id"):
        if key in row:
            return row[key]
    return None


def _same_label(configured: str, catalogued: str) -> bool:
    return configured.strip().casefold() == catalogued.strip().casefold()


def resolve_principals(
    config: Mapping[str, Any], catalog: Mapping[str, Any]
) -> tuple[Principal, ...]:
    """Resolve exact principal identities from the catalog and reject label drift."""

    if not isinstance(config, Mapping):
        raise ValueError("config must be an object")
    if not isinstance(catalog, Mapping):
        raise ValueError("catalog must be an object")
    records = _catalog_index(catalog)
    resolved: list[Principal] = []
    for grouped_role, row in _config_rows(config):
        model_id = _nonblank(row.get("model_id"), "model_id")
        record = records.get(model_id)
        if record is None:
            raise ValueError(f"model_id {model_id!r} is missing from the exact catalog")

        catalog_identity = {
            field: _nonblank(record.get(field), f"catalog {model_id}.{field}")
            for field in ("canonical_slug", "vendor", "family")
        }
        for field, catalogued in catalog_identity.items():
            if field not in row:
                continue
            configured = _nonblank(row[field], field)
            if not _same_label(configured, catalogued):
                raise ValueError(
                    f"config {field} {configured!r} contradicts catalog-derived "
                    f"{catalogued!r} for {model_id}"
                )

        row_role = row.get("role")
        if grouped_role is None:
            role = _normalise_role(row_role)
        elif row_role is None:
            role = grouped_role
        else:
            role = _normalise_role(row_role)
            if role != grouped_role:
                raise ValueError(
                    f"config role {row_role!r} contradicts role group {grouped_role!r}"
                )

        resolved.append(
            Principal(
                opaque_id=_opaque_id(row),
                role=role,
                model_id=model_id,
                canonical_slug=catalog_identity["canonical_slug"],
                vendor=catalog_identity["vendor"],
                family=catalog_identity["family"],
            )
        )
    return tuple(resolved)


def _identity_values(principals: Sequence[Principal], attribute: str) -> set[str]:
    return {
        getattr(principal, attribute).strip().casefold()
        for principal in principals
    }


def _role_members(
    principals: Sequence[Principal], roles: set[str] | frozenset[str]
) -> list[Principal]:
    return [
        principal
        for principal in principals
        if _normalise_role(principal.role) in roles
    ]


def _is_openai(principal: Principal) -> bool:
    vendor = principal.vendor.strip().casefold()
    namespace = principal.model_id.partition("/")[0].strip().casefold()
    canonical_namespace = principal.canonical_slug.partition("/")[0].strip().casefold()
    return "openai" in {vendor, namespace, canonical_namespace}


def validate_role_separation(principals: Sequence[Principal]) -> None:
    """Fail closed on THORNS actor, generator, and primary-judge overlap."""

    if not isinstance(principals, Sequence) or isinstance(
        principals, (str, bytes, bytearray)
    ):
        raise ValueError("principals must be a sequence")
    if any(not isinstance(principal, Principal) for principal in principals):
        raise ValueError("principals must contain only Principal records")
    opaque_ids = [principal.opaque_id for principal in principals]
    if len(set(opaque_ids)) != len(opaque_ids):
        raise ValueError("principals contain a duplicate opaque_id")

    actor_roles = ("calibration", "evaluation", "held_out_frontier")
    by_role = {
        role: _role_members(principals, {role})
        for role in actor_roles
    }
    for left_index, left_role in enumerate(actor_roles):
        for right_role in actor_roles[left_index + 1 :]:
            for attribute in ("vendor", "family"):
                overlap = _identity_values(by_role[left_role], attribute).intersection(
                    _identity_values(by_role[right_role], attribute)
                )
                if overlap:
                    raise ValueError(
                        f"THORNS {attribute} overlap between {left_role} and "
                        f"{right_role}: {sorted(overlap)}"
                    )

    primary_judges = _role_members(principals, _PRIMARY_JUDGE_ROLES)
    if len(primary_judges) < 2:
        raise ValueError("live scoring requires at least two primary judges")
    if any(_is_openai(judge) for judge in primary_judges):
        raise ValueError(
            "primary judges must be non-OpenAI by exact model and catalog vendor identity"
        )
    for attribute in ("vendor", "family"):
        values = _identity_values(primary_judges, attribute)
        if len(values) != len(primary_judges):
            raise ValueError(f"primary judges must be mutually {attribute}-disjoint")

    judges = _role_members(principals, _JUDGE_ROLES)
    protected_actors = _role_members(principals, {"evaluation", "item_generator"})
    for attribute in ("vendor", "family"):
        overlap = _identity_values(protected_actors, attribute).intersection(
            _identity_values(judges, attribute)
        )
        if overlap:
            raise ValueError(
                "evaluated actors and item generators must be "
                f"{attribute}-disjoint from judges: {sorted(overlap)}"
            )


__all__ = [
    "Principal",
    "blind_event_payload",
    "canonical_json_bytes",
    "resolve_principals",
    "validate_role_separation",
]
