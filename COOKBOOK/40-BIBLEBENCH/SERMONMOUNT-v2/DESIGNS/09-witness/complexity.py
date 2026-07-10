"""Pure MF-1 tool-contract and moral-complexity primitives.

Nothing in this module reads scoring signals or prose for branch counts.  Complexity is
derived only from split-word situation length, explicit parties, strict tool declarations,
and the inspectable authored ``act_spec.decision_branches`` list.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
from dataclasses import dataclass
from typing import Any, Iterable


POLES = ("gold", "deficient", "counterfeit", "neutral")
BANDS = ("low", "medium", "high")
ONE_TOOL_FLOOR_IDS = frozenset({"W-S16-02", "W-S16-03", "W-S09-01"})
_DECLARATION_RE = re.compile(
    r"^(?P<name>[a-z][a-z0-9_]*)\((?P<args>(?:[a-z][a-z0-9_]*"
    r"(?:,[a-z][a-z0-9_]*)*)?)\)$"
)


class ToolDeclarationError(ValueError):
    """A declared ACT tool is malformed or ambiguous."""


class ComplexityError(ValueError):
    """Authored moral-complexity metadata is missing or invalid."""


@dataclass(frozen=True)
class ToolDeclaration:
    name: str
    args: tuple[str, ...]

    @property
    def arity(self) -> int:
        return len(self.args)

    @property
    def declaration(self) -> str:
        return f"{self.name}({','.join(self.args)})"


def parse_tool_declaration(declaration: str) -> ToolDeclaration:
    """Parse the exact declaration grammar ``name(arg,...)`` including zero arity."""
    if not isinstance(declaration, str):
        raise ToolDeclarationError(
            f"tool declaration must be a string, got {type(declaration).__name__}"
        )
    match = _DECLARATION_RE.fullmatch(declaration)
    if match is None:
        raise ToolDeclarationError(f"malformed tool declaration: {declaration!r}")
    args = tuple(match.group("args").split(",")) if match.group("args") else ()
    duplicates = sorted({arg for arg in args if args.count(arg) > 1})
    if duplicates:
        raise ToolDeclarationError(
            f"duplicate argument name(s) {duplicates} in {declaration!r}"
        )
    return ToolDeclaration(match.group("name"), args)


def parse_tool_declarations(declarations: Iterable[str]) -> tuple[ToolDeclaration, ...]:
    if isinstance(declarations, (str, bytes)) or not isinstance(declarations, Iterable):
        raise ToolDeclarationError("tool declarations must be an iterable of strings")
    parsed = tuple(parse_tool_declaration(value) for value in declarations)
    names = [spec.name for spec in parsed]
    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        raise ToolDeclarationError(f"duplicate tool name(s): {duplicates}")
    return parsed


def split_word_count(text: str) -> int:
    if not isinstance(text, str):
        raise TypeError(f"word-count input must be a string, got {type(text).__name__}")
    return len(text.split())


def inclusive_word_bounds(mean_words: float) -> tuple[int, int]:
    """Return the inclusive integer ±20% gate around a moral mean."""
    if not isinstance(mean_words, (int, float)) or not math.isfinite(mean_words):
        raise ValueError("mean word count must be finite")
    if mean_words <= 0:
        raise ValueError("mean word count must be positive")
    return math.ceil(mean_words * 0.8), math.floor(mean_words * 1.2)


def within_word_gate(word_count: int, mean_words: float) -> bool:
    lower, upper = inclusive_word_bounds(mean_words)
    return isinstance(word_count, int) and not isinstance(word_count, bool) and lower <= word_count <= upper


def validate_decision_branches(core: Any) -> list[str]:
    """Validate explicit branch IDs, poles, declared bare tools, and exact parties."""
    core_id = str(getattr(core, "core_id", "<unknown>"))
    errors: list[str] = []
    act_spec = getattr(core, "act_spec", {})
    tools = act_spec.get("tools", []) if isinstance(act_spec, dict) else []
    try:
        declarations = parse_tool_declarations(tools)
    except ToolDeclarationError as exc:
        return [f"{core_id}: {exc}"]
    declared = {spec.name for spec in declarations}
    parties = getattr(core, "parties", [])
    party_set = set(parties) if isinstance(parties, list) else set()
    branches = act_spec.get("decision_branches") if isinstance(act_spec, dict) else None
    if not isinstance(branches, list) or not branches:
        return [f"{core_id}: act_spec.decision_branches must be a non-empty list"]
    ids: list[str] = []
    action_paths: list[str] = []
    for index, branch in enumerate(branches):
        prefix = f"{core_id}: decision branch[{index}]"
        if not isinstance(branch, dict):
            errors.append(f"{prefix} must be a mapping")
            continue
        branch_id = branch.get("id")
        if not isinstance(branch_id, str) or not branch_id.strip():
            errors.append(f"{prefix} id must be a non-empty string")
        else:
            ids.append(branch_id)
        action_path = branch.get("action_path")
        if not isinstance(action_path, str) or not action_path.strip():
            errors.append(f"{prefix} action_path must be a non-empty string")
        else:
            action_paths.append(action_path)
        tool_mode = branch.get("tool_mode")
        if tool_mode not in {"single", "sequence", "alternative", "conditional"}:
            errors.append(f"{prefix} tool_mode is invalid: {tool_mode!r}")
        pole = branch.get("pole")
        if pole not in POLES:
            errors.append(f"{prefix} pole must be one of {list(POLES)}, got {pole!r}")
        branch_tools = branch.get("tools")
        if not isinstance(branch_tools, list) or not branch_tools:
            errors.append(f"{prefix} tools must be a non-empty list")
        else:
            if len(branch_tools) != len(set(branch_tools)):
                errors.append(f"{prefix} tools contain duplicates")
            if tool_mode == "single" and len(branch_tools) != 1:
                errors.append(f"{prefix} single tool_mode requires exactly one tool")
            if tool_mode in {"sequence", "alternative", "conditional"} and len(branch_tools) < 2:
                errors.append(f"{prefix} {tool_mode} tool_mode requires multiple tools")
            for tool in branch_tools:
                if tool not in declared:
                    errors.append(f"{prefix} references undeclared tool {tool!r}")
        allowed_sequences = branch.get("allowed_tool_sequences")
        if tool_mode == "conditional":
            if not isinstance(allowed_sequences, list) or not allowed_sequences:
                errors.append(
                    f"{prefix} conditional tool_mode requires allowed_tool_sequences"
                )
            else:
                seen_sequences: set[tuple[str, ...]] = set()
                allowed_tools = set(branch_tools) if isinstance(branch_tools, list) else set()
                for sequence_index, sequence in enumerate(allowed_sequences):
                    if not isinstance(sequence, list) or not sequence:
                        errors.append(
                            f"{prefix} allowed_tool_sequences[{sequence_index}] "
                            "must be a non-empty list"
                        )
                        continue
                    marker = tuple(sequence)
                    if marker in seen_sequences:
                        errors.append(f"{prefix} allowed_tool_sequences contain duplicates")
                    seen_sequences.add(marker)
                    undeclared_route_tools = [
                        tool for tool in sequence if tool not in allowed_tools
                    ]
                    if undeclared_route_tools:
                        errors.append(
                            f"{prefix} allowed sequence references tools outside the "
                            f"conditional course: {undeclared_route_tools}"
                        )
        elif allowed_sequences is not None:
            errors.append(
                f"{prefix} allowed_tool_sequences is only valid for conditional courses"
            )
        branch_parties = branch.get("parties")
        if not isinstance(branch_parties, list) or not branch_parties:
            errors.append(f"{prefix} parties must be a non-empty list")
        else:
            if len(branch_parties) != len(set(branch_parties)):
                errors.append(f"{prefix} parties contain duplicates")
            for party in branch_parties:
                if party not in party_set:
                    errors.append(f"{prefix} references unknown party {party!r}")
    duplicates = sorted({branch_id for branch_id in ids if ids.count(branch_id) > 1})
    if duplicates:
        errors.append(f"{core_id}: duplicate decision branch id(s): {duplicates}")
    duplicate_paths = sorted({path for path in action_paths if action_paths.count(path) > 1})
    if duplicate_paths:
        errors.append(f"{core_id}: duplicate decision branch action_path(s)")
    return errors


def validate_act_complexity(core: Any) -> list[str]:
    errors = validate_decision_branches(core)
    if errors and any("tool declaration" in error or "malformed tool" in error
                      for error in errors):
        return errors
    act_spec = getattr(core, "act_spec", {})
    try:
        declared = {spec.name for spec in parse_tool_declarations(act_spec.get("tools", []))}
    except ToolDeclarationError:
        return errors
    signatures = act_spec.get("action_signatures", {})
    primary = signatures.get("tool") if isinstance(signatures, dict) else None
    if not isinstance(primary, str) or primary not in declared:
        errors.append(
            f"{getattr(core, 'core_id', '<unknown>')}: action-signature primary tool "
            f"{primary!r} is not declared"
        )
    return errors


def _profile_id(profile: dict[str, Any]) -> str:
    identity = {
        key: profile[key] for key in (
            "core_id",
            "word_count", "clamped_word_count", "length_tercile", "branch_count", "party_count",
            "tool_count", "tool_arities", "raw_difficulty", "difficulty_band",
        )
    }
    blob = json.dumps(identity, sort_keys=True, separators=(",", ":"))
    return "cx-" + hashlib.sha256(blob.encode("utf-8")).hexdigest()[:12]


def build_moral_profiles(cores: Iterable[Any]) -> dict[str, dict[str, Any]]:
    """Build stable terciles and balanced bands from explicit moral-core structure."""
    source = list(cores)
    if not source:
        raise ComplexityError("cannot profile an empty moral-core set")
    core_ids = [str(getattr(core, "core_id", "")) for core in source]
    if len(core_ids) != len(set(core_ids)):
        raise ComplexityError("moral profile input has duplicate core IDs")
    all_branch_ids: list[str] = []
    provisional: dict[str, dict[str, Any]] = {}
    for core in source:
        errors = validate_act_complexity(core)
        if errors:
            raise ComplexityError("; ".join(errors))
        branches = core.act_spec["decision_branches"]
        all_branch_ids.extend(branch["id"] for branch in branches)
        declarations = parse_tool_declarations(core.act_spec["tools"])
        provisional[core.core_id] = {
            "core_id": core.core_id,
            "word_count": split_word_count(core.situation),
            "branch_count": len(branches),
            "party_count": len(core.parties),
            "tool_count": len(declarations),
            "tool_arities": sorted(spec.arity for spec in declarations),
        }
    duplicate_branch_ids = sorted({value for value in all_branch_ids
                                   if all_branch_ids.count(value) > 1})
    if duplicate_branch_ids:
        raise ComplexityError(f"duplicate global decision branch IDs: {duplicate_branch_ids}")

    mean_words = sum(profile["word_count"] for profile in provisional.values()) / len(provisional)
    lower, upper = inclusive_word_bounds(mean_words)
    for profile in provisional.values():
        profile["clamped_word_count"] = min(upper, max(lower, profile["word_count"]))

    length_order = sorted(provisional.values(), key=lambda p: (p["word_count"], p["core_id"]))
    if len(length_order) % 3:
        raise ComplexityError("moral profile count must divide evenly into three terciles")
    tercile_size = len(length_order) // 3
    for index, profile in enumerate(length_order):
        profile["length_tercile"] = index // tercile_size + 1
        profile["raw_difficulty"] = profile["length_tercile"] * profile["branch_count"]

    band_order = sorted(provisional.values(), key=lambda p: (
        p["raw_difficulty"], p["word_count"], p["branch_count"], p["party_count"],
        p["tool_count"], tuple(p["tool_arities"]), p["core_id"],
    ))
    if len(band_order) % 3:
        raise ComplexityError("moral profile count must divide evenly into three bands")
    band_size = len(band_order) // 3
    for index, profile in enumerate(band_order):
        profile["difficulty_band"] = BANDS[index // band_size]
        profile["complexity_profile_id"] = _profile_id(profile)
    return {core_id: provisional[core_id] for core_id in sorted(provisional)}


def _similarity_key(profile: dict[str, Any]) -> tuple[Any, ...]:
    """Place profiles adjacently by the structure a valid control must actually match."""
    effective_arities = list(profile["tool_arities"])
    if profile["tool_count"] == 1:
        effective_arities += effective_arities
    return (
        profile["branch_count"], max(2, profile["tool_count"]), tuple(effective_arities),
        profile["party_count"], profile["clamped_word_count"], profile["core_id"],
    )


def _hardness_key(profile: dict[str, Any]) -> tuple[Any, ...]:
    return (
        profile["raw_difficulty"], profile["word_count"], profile["branch_count"],
        profile["party_count"], profile["tool_count"], tuple(profile["tool_arities"]),
        profile["core_id"],
    )


def pair_moral_profiles(profiles: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """Pair adjacent similar profiles within bands; the harder member is the anchor."""
    if not isinstance(profiles, dict) or not profiles:
        raise ComplexityError("profiles must be a non-empty mapping")
    clusters: list[dict[str, Any]] = []
    represented: list[str] = []
    for band in BANDS:
        members = sorted(
            (dict(profile) for profile in profiles.values()
             if profile.get("difficulty_band") == band),
            key=_similarity_key,
        )
        if len(members) % 2:
            raise ComplexityError(f"difficulty band {band} has an odd profile count")
        for pair_index in range(0, len(members), 2):
            pair = members[pair_index:pair_index + 2]
            anchor = max(pair, key=_hardness_key)
            moral_ids = [profile["core_id"] for profile in pair]
            represented.extend(moral_ids)
            clusters.append({
                "cluster_id": f"cluster-{band}-{pair_index // 2:02d}",
                "difficulty_band": band,
                "represented_moral_ids": moral_ids,
                "anchor_core_id": anchor["core_id"],
                "anchor_profile": dict(anchor),
            })
    if sorted(represented) != sorted(profiles):
        raise ComplexityError("profile pairing does not represent every moral exactly once")
    return clusters
