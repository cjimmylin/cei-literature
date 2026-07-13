"""Isolated module-native lenses over frozen observable evidence."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import hashlib
from importlib.resources import files
import json
import os
from pathlib import Path
import re
from typing import Any, Literal
import unicodedata

from jsonschema import Draft202012Validator, SchemaError, ValidationError
import yaml

from .contracts import Json, canonical_json_bytes
from .events import (
    FrozenObservableEvidence,
    observable_evidence_to_json,
    observable_event_to_json,
    observable_events_sha256,
)


__all__ = (
    "LensApplicability",
    "NOT_APPLICABLE",
    "LensRule",
    "LensSpec",
    "LensRouteContext",
    "NativeScorerRoute",
    "load_lens_manifest",
    "build_lens_packet",
    "select_native_scorer",
    "assert_lens_packet_safe",
)


Module = Literal[
    "fruitbench", "corinthlove", "tencommandments", "sermonmount"
]
EpisodeRole = Literal["target", "null", "restraint"]
BehavioralAttribution = Literal[
    "applicable", "not_behaviorally_attributable"
]

_MODULES = frozenset(
    {"fruitbench", "corinthlove", "tencommandments", "sermonmount"}
)
_MODULE_PREFIX = {
    "fruitbench": "F",
    "corinthlove": "L",
    "tencommandments": "T",
    "sermonmount": "S",
}
_CORE_ID = re.compile(
    r"(?:F(?:0[1-9]|1[0-2])|L0[1-8]|T(?:0[1-9]|1[0-2])|S(?:0[1-9]|10))\Z"
)
_LENS_ID = re.compile(
    r"(?:fruitbench|corinthlove|tencommandments|sermonmount)\."
    r"[a-z0-9][a-z0-9._-]{0,127}\Z"
)
_SCORER_ID = re.compile(
    r"(?:fruitbench|corinthlove|tencommandments|sermonmount)\.native\."
    r"[a-z0-9][a-z0-9._-]{0,127}\Z"
)
_RULE_ID = re.compile(r"R(?:00[1-9]|0[1-9][0-9]|[1-9][0-9]{2})\Z")
_RUBRIC_VERSION = re.compile(r"rv-[0-9][a-z0-9._-]{0,63}\Z")
_HASH = re.compile(r"[0-9a-f]{64}\Z")
_ACTION_ID = re.compile(r"[a-z][a-z0-9_]{0,63}\Z")
_METADATA_NAME = re.compile(r"[a-z][a-z0-9_]*\Z")
_EVIDENCE_ID = re.compile(r"[SE](?:00[1-9]|0[1-9][0-9]|[1-9][0-9]{2})\Z")
_CAMEL_BOUNDARY = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")
_NON_ALNUM = re.compile(r"[^a-z0-9]+")
_CONFUSABLE_TRANSLATION = str.maketrans(
    {
        "а": "a",
        "в": "b",
        "е": "e",
        "ё": "e",
        "ԁ": "d",
        "ԍ": "g",
        "о": "o",
        "р": "p",
        "с": "c",
        "т": "t",
        "у": "y",
        "х": "x",
        "і": "i",
        "ј": "j",
        "к": "k",
        "ӏ": "l",
        "л": "l",
        "м": "m",
        "п": "n",
        "ѕ": "s",
        "һ": "h",
        "ԝ": "w",
        "α": "a",
        "β": "b",
        "δ": "d",
        "ε": "e",
        "ϵ": "e",
        "ϝ": "f",
        "ι": "i",
        "κ": "k",
        "λ": "l",
        "μ": "m",
        "η": "n",
        "τ": "t",
        "ο": "o",
        "ρ": "p",
        "σ": "c",
        "ς": "c",
        "υ": "y",
        "χ": "x",
        "ν": "v",
        "ζ": "z",
    }
)
_EVENT_FIELDS = frozenset(
    {
        "task_correctness",
        "registered_actions",
        "registered_omissions",
        "refusal",
        "evasion",
        "uncertainty",
        "consequence_summaries",
        "evidence_ids",
    }
)
_RULE_FIELDS = frozenset(
    {
        "rule_id",
        "criterion",
        "required_event_fields",
        "assessment_target",
        "doctrinal_status",
        "contestability",
    }
)
_REQUIRED_FORBIDDEN_METADATA = frozenset(
    {
        "actor",
        "actor_id",
        "actor_model",
        "ballot",
        "bundle",
        "canary",
        "condition",
        "core",
        "core_id",
        "cue",
        "episode",
        "expected",
        "expected_label",
        "forecast",
        "fruit",
        "gold",
        "ground_truth",
        "lens",
        "lens_id",
        "lens_name",
        "model",
        "model_id",
        "model_identity",
        "module",
        "private",
        "provider",
        "role",
        "route",
        "schedule",
        "scorer",
        "self_forecast",
        "strategy",
    }
)
_PRIVATE_CONCEPTS = frozenset(
    {
        "actor",
        "ballot",
        "bundle",
        "canary",
        "condition",
        "core",
        "cue",
        "episode",
        "expected",
        "forecast",
        "fruit",
        "gold",
        "groundtruth",
        "lens",
        "model",
        "module",
        "private",
        "provider",
        "role",
        "route",
        "schedule",
        "scorer",
        "strategy",
    }
)
_PRIVATE_EXACT_VALUES = frozenset(
    set(_PRIVATE_CONCEPTS)
    | {f"{concept}s" for concept in _PRIVATE_CONCEPTS}
    | {
        f"{concept}es"
        for concept in _PRIVATE_CONCEPTS
        if concept.endswith(("s", "x", "z", "ch", "sh"))
    }
    | {
        f"{concept[:-1]}ies"
        for concept in _PRIVATE_CONCEPTS
        if concept.endswith("y")
    }
)
_PRIVATE_ASSIGNMENT = re.compile(
    r"(?<![a-z0-9])(?:"
    r"actors?|actor[\W_]*models?|models?|providers?|provider[\W_]*routes?|"
    r"routes?|cues?|conditions?|episode[\W_]*roles?|roles?|modules?|cores?|"
    r"schedules?|bundles?|gold|ground[\W_]*truth|expected[\W_]*labels?|"
    r"privates?|lens(?:es)?|scorers?|strateg(?:y|ies)|fruits?|"
    r"self[\W_]*forecasts?|forecasts?|other[\W_]*ballots?|ballots?|canar(?:y|ies)"
    r")(?:[\W_]*(?:ids?|identit(?:y|ies)|names?|labels?|scores?|results?|"
    r"values?|cop(?:y|ies)|types?|keys?|tokens?|targets?))?[\W_]*(?::|=|\bis\b)",
    re.IGNORECASE,
)
_INWARD_INFERENCE = re.compile(
    r"\b(?:assess|infer|score|determine|evaluate|judge|classify|rate|decide|"
    r"conclude|verify|detect|identify)\w*\b.{0,200}(?:"
    r"genuine[\W_]+faith|faith.{0,30}genuine|has[\W_]+faith|"
    r"shows?[\W_]+regenerat\w*|is[\W_]+regenerat\w*|"
    r"spiritual[\W_]+illuminat\w*|is[\W_]+illuminat\w*|"
    r"is[\W_]+sanctif\w*|(?:model|system|assistant)'?s?[\W_]+sanctification|"
    r"shows?[\W_]+repent\w*|is[\W_]+repent\w*|"
    r"spiritual[\W_]+persever\w*|persever\w*[\W_]+in[\W_]+faith|"
    r"union[\W_]+with[\W_]+christ|inward[\W_]+love|"
    r"genuine[\W_]+virtue|inward[\W_]+virtue|"
    r"spirit[\W_]+produced[\W_]+fruit|genuine[\W_]+worship|"
    r"is[\W_]+worship\w*|inward[\W_]+motive|"
    r"(?:model|system|assistant)'?s?[\W_]+motive|"
    r"christian[\W_]+(?:moral[\W_]+)?agency)",
    re.IGNORECASE | re.DOTALL,
)
_INWARD_STATE_ATTRIBUTION = re.compile(
    r"\b(?:model|system|assistant|response|answer)\b.{0,80}"
    r"\b(?:is|as|has|shows?|demonstrat\w*|possess\w*|exhibit\w*|"
    r"treated|regarded|declared)\b.{0,50}(?:"
    r"genuine[\W_]+faith|regenerat\w*|sanctif\w*|repent\w*|"
    r"spiritual[\W_]+illuminat\w*|persever\w*[\W_]+in[\W_]+faith|"
    r"union[\W_]+with[\W_]+christ|inward[\W_]+(?:love|motive|virtue)|"
    r"genuine[\W_]+(?:virtue|worship)|christian[\W_]+(?:moral[\W_]+)?"
    r"agency)",
    re.IGNORECASE | re.DOTALL,
)
_CONFESSIONAL_IDENTITY_GATE = re.compile(
    r"\b(?:requir\w*|must|pass\w*|accept\w*|reject\w*|fail\w*|"
    r"exclud\w*|disqualif\w*|only)\b.{0,180}"
    r"(?:"
    r"\b(?:affirm\w*|subscrib\w*|assent\w*|deny\w*|reject\w*|"
    r"accept\w*|agree\w*)\b.{0,120}"
    r"(?:westminster|three[\W_]+forms|confession)|"
    r"(?:westminster|three[\W_]+forms|confession).{0,120}"
    r"\b(?:affirm\w*|subscrib\w*|assent\w*|deny\w*|reject\w*|"
    r"accept\w*|agree\w*)\b"
    r")|"
    r"\b(?:affirm\w*|subscrib\w*|assent\w*)\b.{0,120}"
    r"(?:westminster|three[\W_]+forms|confession).{0,180}"
    r"\b(?:requir\w*|must|pass\w*|accept\w*|reject\w*|fail\w*|"
    r"exclud\w*|disqualif\w*)\b",
    re.IGNORECASE | re.DOTALL,
)
_DENOMINATIONAL_IDENTITY_GATE = re.compile(
    r"\b(?:only|accept\w*|reject\w*|pass\w*|fail\w*|exclud\w*|"
    r"disqualif\w*)\b.{0,160}\b(?:westminster\w*|reformed|baptist|"
    r"lutheran|methodist|anglican|pentecostal|presbyterian|calvinist|"
    r"arminian|catholic|orthodox)\b|"
    r"\b(?:westminster\w*|reformed|baptist|lutheran|methodist|anglican|"
    r"pentecostal|presbyterian|calvinist|arminian|catholic|orthodox)\b"
    r".{0,120}\b(?:answers?|responses?)\b.{0,80}"
    r"\b(?:qualif\w*|pass\w*|accept\w*|reject\w*|fail\w*)\b",
    re.IGNORECASE | re.DOTALL,
)
_FORBIDDEN_SCORING_INSTRUCTION = re.compile(
    r"\b(?:scores?|scored|scoring|composites?|rank|ranks|ranked|rankings?|"
    r"leaderboards?)\b|"
    r"\b(?:assign|award|give|allocate)\w*\b.{0,160}\bpoints?\b|"
    r"\b(?:numeric|numerical|rating)[\W_]+scale\b|"
    r"\b(?:one|two|three|four|five|six|seven|eight|nine|ten|[0-9]+)"
    r"[\W_]+to[\W_]+(?:one|two|three|four|five|six|seven|eight|nine|ten|"
    r"[0-9]+)[\W_]+scale\b|"
    r"\b(?:order|sort)\w*\b.{0,160}\bresponses?\b.{0,160}"
    r"\b(?:best|worst)\b",
    re.IGNORECASE | re.DOTALL,
)
_MAX_MANIFEST_BYTES = 1024 * 1024
_MAX_YAML_DEPTH = 64
_MAX_LENSES = 256
_MAX_RULES = 256
_MAX_CRITERION_LENGTH = 4096
_MAX_CONSTRUCT_LENGTH = 4096
_MAX_PACKET_BYTES = 512 * 1024
_FIREWALL_ERROR = "lens firewall rejected packet"
_SPEC_ERROR = "invalid lens specification"
_CONTEXT_ERROR = "invalid lens routing context"
_ROUTE_ERROR = "invalid native scorer route"
_MANIFEST_ERROR = "invalid lens manifest"


class LensApplicability(str, Enum):
    """A typed non-score result for a preregistered scope mismatch."""

    NOT_APPLICABLE = "NOT_APPLICABLE"


NOT_APPLICABLE = LensApplicability.NOT_APPLICABLE


@dataclass(frozen=True)
class LensRule:
    rule_id: str
    criterion: str
    required_event_fields: tuple[str, ...]
    assessment_target: Literal[
        "observable_behavior",
        "passage_interpretation",
        "pastoral_counsel",
        "role_boundary",
    ]
    doctrinal_status: Literal[
        "not_theological",
        "scripture_primary",
        "broad_evangelical_protestant_core",
        "declared_protestant_contested",
    ]
    contestability: Literal["clear", "contested"]


@dataclass(frozen=True)
class LensSpec:
    lens_id: str
    module_owner: Module
    pillar: Literal["ethical_reliability", "biblical_pastoral_fidelity"]
    normative_profile: Literal[
        "observable_ethics", "broad_evangelical_protestant"
    ]
    construct: str
    applicable_core_ids: tuple[str, ...]
    applicable_episode_roles: tuple[EpisodeRole, ...]
    required_event_fields: tuple[str, ...]
    native_scorer_adapter: str
    rubric_version: str
    behavioral_attribution_states: tuple[BehavioralAttribution, ...]
    forbidden_metadata: tuple[str, ...]
    rules: tuple[LensRule, ...]


@dataclass(frozen=True)
class LensRouteContext:
    module: Module
    core_id: str
    episode_role: EpisodeRole
    behavioral_attribution: BehavioralAttribution


@dataclass(frozen=True)
class NativeScorerRoute:
    adapter_id: str
    module_owner: Module
    evidence_namespace: Literal["native"]


def _safe_string(
    value: Any,
    *,
    max_bytes: int | None = None,
    max_chars: int | None = None,
) -> bool:
    if (
        type(value) is not str
        or not value
        or (max_bytes is None and max_chars is None)
        or (max_bytes is not None and max_bytes < 1)
        or (max_chars is not None and max_chars < 1)
    ):
        return False
    try:
        return (
            not any(0xD800 <= ord(character) <= 0xDFFF for character in value)
            and (max_chars is None or len(value) <= max_chars)
            and (
                max_bytes is None
                or len(value.encode("utf-8")) <= max_bytes
            )
        )
    except UnicodeEncodeError:
        return False


def _policy_text(value: str, *, join_controls: bool = False) -> str:
    normalized = unicodedata.normalize("NFKC", value)
    separated = _CAMEL_BOUNDARY.sub("_", normalized).casefold()
    decomposed = unicodedata.normalize("NFKD", separated).translate(
        _CONFUSABLE_TRANSLATION
    )
    cleaned: list[str] = []
    for character in decomposed:
        category = unicodedata.category(character)
        if category in {"Cf", "Mn", "Me"}:
            continue
        if category == "Cc":
            if not join_controls:
                cleaned.append(" ")
            continue
        cleaned.append(character)
    return "".join(cleaned)


def _components(value: str) -> tuple[str, ...]:
    return tuple(
        component for component in _NON_ALNUM.split(_policy_text(value)) if component
    )


def _contains_private_assignment(value: str) -> bool:
    return any(
        _PRIVATE_ASSIGNMENT.search(normalized)
        for normalized in (
            _policy_text(value),
            _policy_text(value, join_controls=True),
        )
    )


def _contains_mixed_script_assignment(value: str) -> bool:
    for normalized in (
        _policy_text(value),
        _policy_text(value, join_controls=True),
    ):
        for marker in re.finditer(r"(?::|=|\bis\b)", normalized):
            candidate = re.search(
                r"([\w-]+)[\W_]*\Z", normalized[: marker.start()]
            )
            if candidate is None:
                continue
            identifier = candidate.group(1)
            has_ascii_letter = any(
                character.isascii() and character.isalpha()
                for character in identifier
            )
            has_non_ascii_letter = any(
                not character.isascii() and character.isalpha()
                for character in identifier
            )
            if has_ascii_letter and has_non_ascii_letter:
                return True
    return False


def _declared_metadata_assignment_pattern(
    names: tuple[str, ...] | frozenset[str],
) -> re.Pattern[str]:
    fragments = []
    for name in sorted(names):
        components = _components(name)
        if not components:
            raise ValueError
        fragments.append(r"[\W_]*".join(map(re.escape, components)))
    suffix = (
        r"(?:[\W_]*(?:ids?|identit(?:y|ies)|names?|labels?|scores?|"
        r"results?|values?|cop(?:y|ies)|types?|keys?|tokens?|targets?))?"
    )
    return re.compile(
        r"(?<![a-z0-9])(?:"
        + "|".join(fragments)
        + r")(?:s|es)?"
        + suffix
        + r"[\W_]*(?::|=|\bis\b)",
        re.IGNORECASE,
    )


def _declared_metadata_reference_pattern(
    names: tuple[str, ...] | frozenset[str],
) -> re.Pattern[str]:
    fragments = []
    for name in sorted(names):
        components = _components(name)
        if not components:
            raise ValueError
        fragments.append(r"[\W_]*".join(map(re.escape, components)))
    return re.compile(
        r"(?<![a-z0-9])(?:"
        + "|".join(fragments)
        + r")(?:s|es)?(?![a-z0-9])",
        re.IGNORECASE,
    )
def _is_private_exact_value(value: str) -> bool:
    components = _components(value)
    return len(components) == 1 and components[0] in _PRIVATE_EXACT_VALUES


def _criterion_breaks_claim_boundary(
    value: str, *, defer_private_scoring: bool = False
) -> bool:
    normalized = _policy_text(value)
    scoring = bool(_FORBIDDEN_SCORING_INSTRUCTION.search(normalized))
    return bool(
        _INWARD_INFERENCE.search(normalized)
        or _INWARD_STATE_ATTRIBUTION.search(normalized)
        or _CONFESSIONAL_IDENTITY_GATE.search(normalized)
        or _DENOMINATIONAL_IDENTITY_GATE.search(normalized)
        or (
            scoring
            and not (
                defer_private_scoring
                and _contains_private_assignment(value)
            )
        )
    )


def _rule_to_json(rule: LensRule) -> dict[str, Json]:
    return {
        "rule_id": rule.rule_id,
        "criterion": rule.criterion,
        "required_event_fields": list(rule.required_event_fields),
        "assessment_target": rule.assessment_target,
        "doctrinal_status": rule.doctrinal_status,
        "contestability": rule.contestability,
    }


def _spec_to_private_json(spec: LensSpec) -> dict[str, Json]:
    return {
        "lens_id": spec.lens_id,
        "module_owner": spec.module_owner,
        "pillar": spec.pillar,
        "normative_profile": spec.normative_profile,
        "construct": spec.construct,
        "applicable_core_ids": list(spec.applicable_core_ids),
        "applicable_episode_roles": list(spec.applicable_episode_roles),
        "required_event_fields": list(spec.required_event_fields),
        "native_scorer_adapter": spec.native_scorer_adapter,
        "rubric_version": spec.rubric_version,
        "behavioral_attribution_states": list(
            spec.behavioral_attribution_states
        ),
        "forbidden_metadata": list(spec.forbidden_metadata),
        "rules": [_rule_to_json(rule) for rule in spec.rules],
    }


def _core_matches_module(core_id: str, module: str) -> bool:
    return bool(
        type(core_id) is str
        and _CORE_ID.fullmatch(core_id)
        and core_id.startswith(_MODULE_PREFIX[module])
    )


def _valid_unique_tuple(
    value: Any,
    allowed: frozenset[str],
    *,
    nonempty: bool = True,
) -> bool:
    return bool(
        type(value) is tuple
        and (not nonempty or value)
        and all(type(item) is str and item in allowed for item in value)
        and len(value) == len(set(value))
    )


def _validate_rule(rule: Any, *, pillar: str) -> None:
    if type(rule) is not LensRule:
        raise ValueError(_SPEC_ERROR)
    if (
        type(rule.rule_id) is not str
        or _RULE_ID.fullmatch(rule.rule_id) is None
        or not _safe_string(
            rule.criterion, max_chars=_MAX_CRITERION_LENGTH
        )
        or not _valid_unique_tuple(
            rule.required_event_fields, _EVENT_FIELDS
        )
        or rule.assessment_target
        not in {
            "observable_behavior",
            "passage_interpretation",
            "pastoral_counsel",
            "role_boundary",
        }
        or rule.doctrinal_status
        not in {
            "not_theological",
            "scripture_primary",
            "broad_evangelical_protestant_core",
            "declared_protestant_contested",
        }
        or rule.contestability not in {"clear", "contested"}
        or _criterion_breaks_claim_boundary(
            rule.criterion, defer_private_scoring=True
        )
    ):
        raise ValueError(_SPEC_ERROR)
    contested = rule.doctrinal_status == "declared_protestant_contested"
    if contested != (rule.contestability == "contested"):
        raise ValueError(_SPEC_ERROR)
    if pillar == "ethical_reliability":
        if (
            rule.assessment_target
            not in {"observable_behavior", "role_boundary"}
            or rule.doctrinal_status != "not_theological"
        ):
            raise ValueError(_SPEC_ERROR)
    elif pillar == "biblical_pastoral_fidelity":
        if (
            rule.assessment_target
            not in {
                "passage_interpretation",
                "pastoral_counsel",
                "role_boundary",
            }
            or rule.doctrinal_status == "not_theological"
        ):
            raise ValueError(_SPEC_ERROR)
    else:
        raise ValueError(_SPEC_ERROR)


def _validate_spec(spec: Any) -> LensSpec:
    try:
        if type(spec) is not LensSpec:
            raise ValueError
        if (
            type(spec.lens_id) is not str
            or _LENS_ID.fullmatch(spec.lens_id) is None
            or spec.module_owner not in _MODULES
            or not spec.lens_id.startswith(f"{spec.module_owner}.")
            or spec.pillar
            not in {"ethical_reliability", "biblical_pastoral_fidelity"}
            or spec.normative_profile
            not in {"observable_ethics", "broad_evangelical_protestant"}
            or not _safe_string(
                spec.construct, max_chars=_MAX_CONSTRUCT_LENGTH
            )
            or _criterion_breaks_claim_boundary(spec.construct)
            or type(spec.applicable_core_ids) is not tuple
            or not spec.applicable_core_ids
            or len(spec.applicable_core_ids)
            != len(set(spec.applicable_core_ids))
            or any(
                not _core_matches_module(core_id, spec.module_owner)
                for core_id in spec.applicable_core_ids
            )
            or not _valid_unique_tuple(
                spec.applicable_episode_roles,
                frozenset({"target", "null", "restraint"}),
            )
            or not _valid_unique_tuple(
                spec.required_event_fields, _EVENT_FIELDS
            )
            or type(spec.native_scorer_adapter) is not str
            or _SCORER_ID.fullmatch(spec.native_scorer_adapter) is None
            or not spec.native_scorer_adapter.startswith(
                f"{spec.module_owner}.native."
            )
            or type(spec.rubric_version) is not str
            or _RUBRIC_VERSION.fullmatch(spec.rubric_version) is None
            or not _valid_unique_tuple(
                spec.behavioral_attribution_states,
                frozenset(
                    {"applicable", "not_behaviorally_attributable"}
                ),
            )
            or type(spec.forbidden_metadata) is not tuple
            or not spec.forbidden_metadata
            or len(spec.forbidden_metadata) > 128
            or any(
                type(item) is not str
                or not _safe_string(item, max_bytes=128)
                or _METADATA_NAME.fullmatch(item) is None
                for item in spec.forbidden_metadata
            )
            or len(spec.forbidden_metadata)
            != len(set(spec.forbidden_metadata))
            or not _REQUIRED_FORBIDDEN_METADATA.issubset(
                spec.forbidden_metadata
            )
            or type(spec.rules) is not tuple
            or not spec.rules
            or len(spec.rules) > _MAX_RULES
        ):
            raise ValueError
        if spec.pillar == "ethical_reliability":
            if (
                spec.normative_profile != "observable_ethics"
                or spec.behavioral_attribution_states != ("applicable",)
            ):
                raise ValueError
        elif spec.normative_profile != "broad_evangelical_protestant":
            raise ValueError
        for rule in spec.rules:
            _validate_rule(rule, pillar=spec.pillar)
            if not set(rule.required_event_fields).issubset(
                spec.required_event_fields
            ):
                raise ValueError
        if len({rule.rule_id for rule in spec.rules}) != len(spec.rules):
            raise ValueError
        canonical_json_bytes(_spec_to_private_json(spec))
        return spec
    except (AttributeError, KeyError, TypeError, UnicodeError, ValueError):
        raise ValueError(_SPEC_ERROR) from None


def _validate_context(context: Any) -> LensRouteContext:
    try:
        if (
            type(context) is not LensRouteContext
            or context.module not in _MODULES
            or not _core_matches_module(context.core_id, context.module)
            or context.episode_role not in {"target", "null", "restraint"}
            or context.behavioral_attribution
            not in {"applicable", "not_behaviorally_attributable"}
        ):
            raise ValueError
        return context
    except (AttributeError, KeyError, TypeError, ValueError):
        raise ValueError(_CONTEXT_ERROR) from None


def _context_to_private_json(context: LensRouteContext) -> dict[str, Json]:
    return {
        "module": context.module,
        "core_id": context.core_id,
        "episode_role": context.episode_role,
        "behavioral_attribution": context.behavioral_attribution,
    }


def _validated_visible_events(
    evidence: Any,
) -> tuple[FrozenObservableEvidence, list[Json]]:
    if type(evidence) is not FrozenObservableEvidence:
        raise ValueError("invalid lens evidence")
    try:
        public = observable_evidence_to_json(evidence)
        if evidence.status != "COMPLETE":
            raise RuntimeError("incomplete")
        if (
            evidence.missing_evidence
            or not evidence.events
            or observable_events_sha256(evidence.events)
            != evidence.event_record_sha256
            or public["event_record_sha256"] != evidence.event_record_sha256
            or public["evidence_bundle_sha256"]
            != evidence.evidence_bundle_sha256
        ):
            raise ValueError
        events = [observable_event_to_json(event) for event in evidence.events]
        if events != public["events"]:
            raise ValueError
        return evidence, events
    except RuntimeError:
        raise ValueError("incomplete lens evidence") from None
    except (AttributeError, KeyError, TypeError, UnicodeError, ValueError):
        raise ValueError("invalid lens evidence") from None


def _validate_event_projection(row: Any) -> None:
    if type(row) is not dict or set(row) != _EVENT_FIELDS:
        raise ValueError
    if (
        row["task_correctness"]
        not in {"correct", "partial", "incorrect", "not_assessable"}
        or type(row["refusal"]) is not bool
        or type(row["evasion"]) is not bool
        or row["uncertainty"]
        not in {"none", "expressed", "material_unresolved", "not_assessable"}
    ):
        raise ValueError
    for name in ("registered_actions", "registered_omissions"):
        value = row[name]
        if (
            type(value) is not list
            or len(value) > 128
            or any(
                type(item) is not str
                or _ACTION_ID.fullmatch(item) is None
                or bool(set(_components(item)) & _PRIVATE_CONCEPTS)
                for item in value
            )
            or len(value) != len(set(value))
            or value != sorted(value)
        ):
            raise ValueError
    summaries = row["consequence_summaries"]
    if (
        type(summaries) is not list
        or len(summaries) > 32
        or any(
            not _safe_string(item, max_bytes=1024) for item in summaries
        )
    ):
        raise ValueError
    evidence_ids = row["evidence_ids"]
    if (
        type(evidence_ids) is not list
        or not evidence_ids
        or len(evidence_ids) > 256
        or any(
            type(item) is not str or _EVIDENCE_ID.fullmatch(item) is None
            for item in evidence_ids
        )
        or len(evidence_ids) != len(set(evidence_ids))
    ):
        raise ValueError


def _validate_rule_projection(row: Any) -> None:
    if type(row) is not dict or set(row) != _RULE_FIELDS:
        raise ValueError
    if (
        type(row["rule_id"]) is not str
        or _RULE_ID.fullmatch(row["rule_id"]) is None
        or not _safe_string(
            row["criterion"], max_chars=_MAX_CRITERION_LENGTH
        )
        or type(row["required_event_fields"]) is not list
        or not row["required_event_fields"]
        or len(row["required_event_fields"])
        != len(set(row["required_event_fields"]))
        or any(
            type(item) is not str or item not in _EVENT_FIELDS
            for item in row["required_event_fields"]
        )
        or row["assessment_target"]
        not in {
            "observable_behavior",
            "passage_interpretation",
            "pastoral_counsel",
            "role_boundary",
        }
        or row["doctrinal_status"]
        not in {
            "not_theological",
            "scripture_primary",
            "broad_evangelical_protestant_core",
            "declared_protestant_contested",
        }
        or row["contestability"] not in {"clear", "contested"}
    ):
        raise ValueError
    projected = LensRule(
        rule_id=row["rule_id"],
        criterion=row["criterion"],
        required_event_fields=tuple(row["required_event_fields"]),
        assessment_target=row["assessment_target"],
        doctrinal_status=row["doctrinal_status"],
        contestability=row["contestability"],
    )
    inferred_pillar = (
        "ethical_reliability"
        if projected.doctrinal_status == "not_theological"
        else "biblical_pastoral_fidelity"
    )
    _validate_rule(projected, pillar=inferred_pillar)


def _scan_visible_strings(
    value: Any,
    forbidden_metadata: tuple[str, ...] | frozenset[str],
    *,
    strict_forbidden_metadata: tuple[str, ...] | frozenset[str] = frozenset(),
) -> None:
    declared_assignment = _declared_metadata_assignment_pattern(
        forbidden_metadata
    )
    declared_reference = (
        _declared_metadata_reference_pattern(strict_forbidden_metadata)
        if strict_forbidden_metadata
        else None
    )
    pending = [value]
    seen: set[int] = set()
    nodes = 0
    while pending:
        current = pending.pop()
        nodes += 1
        if nodes > 32768:
            raise ValueError
        if type(current) is str:
            policy_forms = (
                _policy_text(current),
                _policy_text(current, join_controls=True),
            )
            if (
                not _safe_string(current, max_bytes=64 * 1024)
                or _contains_private_assignment(current)
                or _contains_mixed_script_assignment(current)
                or any(
                    declared_assignment.search(normalized)
                    for normalized in policy_forms
                )
                or (
                    declared_reference is not None
                    and any(
                        declared_reference.search(normalized)
                        for normalized in policy_forms
                    )
                )
                or _is_private_exact_value(current)
            ):
                raise ValueError
        elif current is None or type(current) in {bool, int, float}:
            continue
        elif type(current) is dict:
            identity = id(current)
            if identity in seen:
                raise ValueError
            seen.add(identity)
            pending.extend(current.keys())
            pending.extend(current.values())
        elif type(current) is list:
            identity = id(current)
            if identity in seen:
                raise ValueError
            seen.add(identity)
            pending.extend(current)
        else:
            raise ValueError


def assert_lens_packet_safe(packet: dict[str, Json]) -> None:
    """Validate the exact judge-visible lens packet without echoing failures."""

    try:
        if (
            type(packet) is not dict
            or set(packet)
            != {"packet_id", "events", "rules", "rubric_version"}
            or type(packet["packet_id"]) is not str
            or _HASH.fullmatch(packet["packet_id"]) is None
            or type(packet["rubric_version"]) is not str
            or _RUBRIC_VERSION.fullmatch(packet["rubric_version"]) is None
            or type(packet["events"]) is not list
            or not packet["events"]
            or len(packet["events"]) > 256
            or type(packet["rules"]) is not list
            or not packet["rules"]
            or len(packet["rules"]) > _MAX_RULES
        ):
            raise ValueError
        for row in packet["events"]:
            _validate_event_projection(row)
        for row in packet["rules"]:
            _validate_rule_projection(row)
        rule_ids = [row["rule_id"] for row in packet["rules"]]
        if len(rule_ids) != len(set(rule_ids)):
            raise ValueError
        _scan_visible_strings(packet, _REQUIRED_FORBIDDEN_METADATA)
        if len(canonical_json_bytes(packet)) > _MAX_PACKET_BYTES:
            raise ValueError
    except (AttributeError, KeyError, TypeError, UnicodeError, ValueError):
        raise ValueError(_FIREWALL_ERROR) from None


def build_lens_packet(
    evidence: FrozenObservableEvidence,
    spec: LensSpec,
    context: LensRouteContext,
) -> dict[str, Json] | LensApplicability:
    """Build one isolated packet or return typed preregistered inapplicability."""

    checked_spec = _validate_spec(spec)
    checked_context = _validate_context(context)
    checked_evidence, events = _validated_visible_events(evidence)
    if (
        checked_context.module != checked_spec.module_owner
        or checked_context.core_id not in checked_spec.applicable_core_ids
        or checked_context.episode_role
        not in checked_spec.applicable_episode_roles
        or checked_context.behavioral_attribution
        not in checked_spec.behavioral_attribution_states
    ):
        return NOT_APPLICABLE
    if any(
        not set(checked_spec.required_event_fields).issubset(event)
        for event in events
    ):
        raise ValueError("incomplete lens evidence")
    rules: list[Json] = [_rule_to_json(rule) for rule in checked_spec.rules]
    packet_id_input: dict[str, Json] = {
        "event_record_sha256": checked_evidence.event_record_sha256,
        "evidence_bundle_sha256": checked_evidence.evidence_bundle_sha256,
        "lens_spec": _spec_to_private_json(checked_spec),
        "routing_context": _context_to_private_json(checked_context),
        "rubric_version": checked_spec.rubric_version,
    }
    packet: dict[str, Json] = {
        "packet_id": hashlib.sha256(
            canonical_json_bytes(packet_id_input)
        ).hexdigest(),
        "events": json.loads(canonical_json_bytes(events)),
        "rules": json.loads(canonical_json_bytes(rules)),
        "rubric_version": checked_spec.rubric_version,
    }
    assert_lens_packet_safe(packet)
    try:
        strict_metadata = tuple(
            sorted(
                set(checked_spec.forbidden_metadata)
                - _REQUIRED_FORBIDDEN_METADATA
            )
        )
        _scan_visible_strings(
            packet,
            checked_spec.forbidden_metadata,
            strict_forbidden_metadata=strict_metadata,
        )
    except (AttributeError, KeyError, TypeError, UnicodeError, ValueError):
        raise ValueError(_FIREWALL_ERROR) from None
    return packet


def _validate_route(route: Any) -> NativeScorerRoute:
    try:
        if (
            type(route) is not NativeScorerRoute
            or type(route.adapter_id) is not str
            or _SCORER_ID.fullmatch(route.adapter_id) is None
            or route.module_owner not in _MODULES
            or not route.adapter_id.startswith(f"{route.module_owner}.native.")
            or route.evidence_namespace != "native"
        ):
            raise ValueError
        return route
    except (AttributeError, TypeError, ValueError):
        raise ValueError(_ROUTE_ERROR) from None


def select_native_scorer(
    spec: LensSpec,
    routes: tuple[NativeScorerRoute, ...],
) -> NativeScorerRoute:
    """Select the one exact native scorer route without fallback."""

    try:
        checked_spec = _validate_spec(spec)
        if type(routes) is not tuple or not routes or len(routes) > 1024:
            raise ValueError
        checked = tuple(_validate_route(route) for route in routes)
        adapter_ids = tuple(route.adapter_id for route in checked)
        if len(adapter_ids) != len(set(adapter_ids)):
            raise ValueError
        matches = tuple(
            route
            for route in checked
            if route.adapter_id == checked_spec.native_scorer_adapter
        )
        if (
            len(matches) != 1
            or matches[0].module_owner != checked_spec.module_owner
            or matches[0].evidence_namespace != "native"
        ):
            raise ValueError
        return matches[0]
    except (AttributeError, KeyError, TypeError, ValueError):
        raise ValueError(_ROUTE_ERROR) from None


class _DuplicateKeyError(yaml.YAMLError):
    pass


class _YamlGraphError(yaml.YAMLError):
    pass


def _validate_yaml_graph(
    node: yaml.Node,
    *,
    depth: int,
    active: set[int],
    complete: set[int],
) -> None:
    if depth > _MAX_YAML_DEPTH or id(node) in active:
        raise _YamlGraphError
    if id(node) in complete:
        return
    active.add(id(node))
    try:
        if isinstance(node, yaml.MappingNode):
            keys: set[str] = set()
            for key_node, value_node in node.value:
                if (
                    not isinstance(key_node, yaml.ScalarNode)
                    or key_node.tag != "tag:yaml.org,2002:str"
                    or key_node.value in keys
                ):
                    raise _DuplicateKeyError
                keys.add(key_node.value)
                _validate_yaml_graph(
                    value_node,
                    depth=depth + 1,
                    active=active,
                    complete=complete,
                )
        elif isinstance(node, yaml.SequenceNode):
            for child in node.value:
                _validate_yaml_graph(
                    child,
                    depth=depth + 1,
                    active=active,
                    complete=complete,
                )
    finally:
        active.discard(id(node))
    complete.add(id(node))


class _StrictLensLoader(yaml.SafeLoader):
    def get_single_data(self) -> Any:
        node = self.get_single_node()
        if node is None:
            return None
        _validate_yaml_graph(
            node, depth=0, active=set(), complete=set()
        )
        return self.construct_document(node)


def _load_schema() -> dict[str, Any]:
    try:
        raw = (
            files("biblebench_pilot.schemas")
            .joinpath("lens.schema.json")
            .read_text(encoding="utf-8")
        )
        schema = json.loads(raw)
        Draft202012Validator.check_schema(schema)
        return schema
    except (OSError, UnicodeError, json.JSONDecodeError, SchemaError, RecursionError):
        raise ValueError(_MANIFEST_ERROR) from None


def _spec_from_row(row: dict[str, Any]) -> LensSpec:
    rules = tuple(
        LensRule(
            rule_id=rule["rule_id"],
            criterion=rule["criterion"],
            required_event_fields=tuple(rule["required_event_fields"]),
            assessment_target=rule["assessment_target"],
            doctrinal_status=rule["doctrinal_status"],
            contestability=rule["contestability"],
        )
        for rule in row["rules"]
    )
    return LensSpec(
        lens_id=row["lens_id"],
        module_owner=row["module_owner"],
        pillar=row["pillar"],
        normative_profile=row["normative_profile"],
        construct=row["construct"],
        applicable_core_ids=tuple(row["applicable_core_ids"]),
        applicable_episode_roles=tuple(row["applicable_episode_roles"]),
        required_event_fields=tuple(row["required_event_fields"]),
        native_scorer_adapter=row["native_scorer_adapter"],
        rubric_version=row["rubric_version"],
        behavioral_attribution_states=tuple(
            row["behavioral_attribution_states"]
        ),
        forbidden_metadata=tuple(row["forbidden_metadata"]),
        rules=rules,
    )


def load_lens_manifest(path: Path) -> tuple[LensSpec, ...]:
    """Load one closed, bounded lens manifest using the packaged schema."""

    try:
        with Path(path).open("rb") as handle:
            if os.fstat(handle.fileno()).st_size > _MAX_MANIFEST_BYTES:
                raise ValueError
            data = handle.read(_MAX_MANIFEST_BYTES + 1)
            if len(data) > _MAX_MANIFEST_BYTES:
                raise ValueError
        text = data.decode("utf-8", errors="strict")
        manifest = yaml.load(text, Loader=_StrictLensLoader)
        if (
            type(manifest) is not dict
            or set(manifest) != {"manifest_version", "lenses"}
            or manifest["manifest_version"] != "lens-manifest-v1"
            or type(manifest["lenses"]) is not list
            or not manifest["lenses"]
            or len(manifest["lenses"]) > _MAX_LENSES
        ):
            raise ValueError
        validator = Draft202012Validator(_load_schema())
        specs: list[LensSpec] = []
        for row in manifest["lenses"]:
            validator.validate(row)
            specs.append(_validate_spec(_spec_from_row(row)))
        if len({spec.lens_id for spec in specs}) != len(specs):
            raise ValueError
        return tuple(specs)
    except (
        AttributeError,
        KeyError,
        OSError,
        TypeError,
        UnicodeError,
        ValueError,
        ValidationError,
        yaml.YAMLError,
        RecursionError,
    ):
        raise ValueError(_MANIFEST_ERROR) from None
