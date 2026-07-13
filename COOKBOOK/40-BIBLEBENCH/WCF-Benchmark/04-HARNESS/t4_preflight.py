#!/usr/bin/env python3
"""Zero-paid, metadata-only preflight calculations for the WCF-Bench T4 run."""

from __future__ import annotations

import argparse
import csv
import datetime
import hashlib
import json
import math
import os
import random
from decimal import Decimal, ROUND_CEILING
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Sequence

import numpy as np

from wcfbench import EPISODE, CONTESTED, load_items, scorer_kind
from wcfbench import mvp
from wcfbench.contested import settled_core_keypoints


CANARY = "WCFBENCH-CANARY-c1647-x9k4q"
AUTH_KEY_URL = mvp.AUTH_KEY_URL
MODELS_URL = mvp.MODELS_URL

PRIMARY_FAMILIES = ("openai", "deepseek", "qwen/alibaba", "moonshotai", "meta-llama")
FALLBACK_FAMILIES = ("z-ai", "nvidia", "microsoft")
PINS = (
    "deepseek/deepseek-chat",
    "mistralai/mistral-large-2512",
    "meta-llama/llama-3.1-8b-instruct",
    "cohere/command-a",
    "amazon/nova-pro-v1",
)
EXCLUDED_FAMILIES = {"google", "x-ai", "anthropic"}
CAPABILITY_METRICS = (
    "lmarena_text", "mmlu_pro", "gpqa_diamond", "livebench_global")
JUDGE_SLUGS = ("google/gemini-2.5-flash", "x-ai/grok-4.20")
EXPECTED_ARTIFACTS = {
    "capability-battery.csv",
    "openrouter-catalog-snapshot.json",
    "t4-run-manifest.json",
    "t4-cost-plan.csv",
    "t4-preflight-report.md",
}
T3_CALLS_PER_MINUTE = 264.0 / (40.0 + 42.0 / 60.0)
BANK_DIR = Path(__file__).resolve().parent.parent / "05-BANK-YAML"
REQUEST_CLASSES = (
    "base_sut", "base_judge", "variant_p3_sut", "variant_p3_judge",
    "variant_p4_sut", "variant_p4_judge", "variant_p6_sut",
    "variant_p6_judge", "g5b_judge", "g5c_sut", "g5c_judge",
)


class RosterResolutionError(RuntimeError):
    """R59.2 could not produce the minimum eight-model roster."""


class CapabilityError(RuntimeError):
    """Capability inputs cannot support the frozen R60.2 calculation."""


class SecretDisclosureError(RuntimeError):
    """An artifact payload contains credential material."""


def fetch_openrouter_metadata(
    api_key: str,
    *,
    opener: Optional[Callable[[str, Optional[str]], Dict[str, Any]]] = None,
    now: Optional[Callable[[], str]] = None,
) -> Dict[str, Any]:
    """Perform only the two R40.1 OpenRouter GETs and return sanitized values."""
    key_snapshot = mvp.fetch_key_snapshot(api_key, url=AUTH_KEY_URL, opener=opener)
    catalog = mvp.fetch_model_catalog(api_key, url=MODELS_URL, opener=opener)
    catalog_retrieved_at = (now or (lambda: datetime.datetime.now(
        datetime.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")))()
    return {"key_snapshot": key_snapshot, "catalog": catalog,
            "catalog_retrieved_at": catalog_retrieved_at}


def _family_of_slug(slug: str) -> str:
    vendor = slug.split("/", 1)[0].lower()
    return "qwen/alibaba" if vendor in {"qwen", "alibaba"} else vendor


def _text_nonpreview(entry: Mapping[str, Any]) -> bool:
    slug = str(entry.get("id", "")).lower()
    name = str(entry.get("name", "")).lower()
    if entry.get("is_preview") is True or "preview" in slug or "preview" in name:
        return False
    architecture = entry.get("architecture") or {}
    inputs = architecture.get("input_modalities")
    outputs = architecture.get("output_modalities")
    if inputs is not None and "text" not in inputs:
        return False
    if outputs is not None and "text" not in outputs:
        return False
    modality = str(architecture.get("modality", ""))
    return not modality or ("text" in modality)


def parse_lmarena_rows(
    dataset: Any,
    alias_rows: Optional[Sequence[Mapping[str, Any]]] = None,
) -> List[Dict[str, Any]]:
    """Normalize official LMArena rows using only explicit, one-to-one aliases."""
    rows = dataset.get("data", dataset.get("rows", [])) if isinstance(dataset, dict) else dataset
    if not isinstance(rows, list):
        raise CapabilityError("LMArena payload must contain a row list")
    aliases: Dict[str, List[str]] = {}
    for row in alias_rows or ():
        arena_name = str(row.get("arena_name", row.get("model", ""))).strip()
        slug = str(row.get("openrouter_slug", row.get("slug", ""))).strip()
        if arena_name and slug:
            aliases.setdefault(arena_name, []).append(slug)
    normalized: List[Dict[str, Any]] = []
    for row in rows:
        if not isinstance(row, Mapping):
            continue
        arena_name = str(row.get("model", row.get("Model", row.get("name", "")))).strip()
        explicit_slug = str(row.get("slug", row.get("openrouter_slug", ""))).strip()
        mapped = aliases.get(arena_name, [])
        if explicit_slug and row.get("exact_match") is True:
            slug = explicit_slug
        elif len(set(mapped)) == 1:
            slug = mapped[0]
        else:
            continue
        raw_rating = row.get("rating", row.get("arena_score", row.get("text_rating")))
        try:
            rating = float(raw_rating)
        except (TypeError, ValueError):
            continue
        if not math.isfinite(rating):
            continue
        normalized.append({"arena_name": arena_name, "slug": slug, "rating": rating})
    return normalized


def resolve_roster(
    catalog: Mapping[str, Mapping[str, Any]],
    arena_rows: Any,
    alias_rows: Optional[Sequence[Mapping[str, Any]]] = None,
    source_registry: Optional[Mapping[str, Any]] = None,
) -> Dict[str, Any]:
    """Resolve R59.2 mechanically, including collision fallbacks and the n>=8 gate."""
    rows = parse_lmarena_rows(arena_rows, alias_rows)
    candidates: Dict[str, List[Dict[str, Any]]] = {}
    for row in rows:
        slug = row["slug"]
        entry = catalog.get(slug)
        family = _family_of_slug(slug)
        if entry is None or family in EXCLUDED_FAMILIES or not _text_nonpreview(entry):
            continue
        candidates.setdefault(family, []).append(row)
    for family_rows in candidates.values():
        family_rows.sort(key=lambda row: (-row["rating"], row["slug"]))

    available_pins = [
        slug for slug in PINS
        if slug in catalog and _family_of_slug(slug) not in EXCLUDED_FAMILIES
        and _text_nonpreview(catalog[slug])
    ]
    formula: List[str] = []
    trace: List[Dict[str, Any]] = []
    used_fallbacks: set = set()

    def fallback(slot: str, reason: str) -> Optional[str]:
        for family in FALLBACK_FAMILIES:
            if family in used_fallbacks:
                continue
            possible = [
                row for row in candidates.get(family, [])
                if row["slug"] not in formula and row["slug"] not in available_pins
            ]
            if possible:
                used_fallbacks.add(family)
                selected = possible[0]
                formula.append(selected["slug"])
                trace.append({
                    "slot_family": slot, "selected_family": family,
                    "slug": selected["slug"], "rating": selected["rating"],
                    "reason": reason,
                })
                return selected["slug"]
        trace.append({"slot_family": slot, "slug": None, "reason": f"{reason}-unavailable"})
        return None

    for family in PRIMARY_FAMILIES:
        possible = [row for row in candidates.get(family, []) if row["slug"] not in formula]
        if not possible:
            fallback(family, "missing-primary-fallback")
            continue
        selected = possible[0]
        if selected["slug"] in available_pins:
            fallback(family, "pinned-collision-fallback")
            continue
        formula.append(selected["slug"])
        trace.append({
            "slot_family": family, "selected_family": family,
            "slug": selected["slug"], "rating": selected["rating"],
            "reason": "primary-highest-rating",
        })

    roster = formula + [slug for slug in available_pins if slug not in formula]
    if len(roster) < 8:
        raise RosterResolutionError(
            f"R59.2 resolved {len(roster)} models, fewer than 8; stop and escalate")
    result = {
        "roster": roster,
        "formula_models": formula,
        "pins": available_pins,
        "trace": trace,
        "target_met": len(roster) == 10,
        "arena_ordering_disclosure": (
            "Official LMArena rating is used as the current successor ordering field "
            "for the memo's historical text Elo wording."),
    }
    if source_registry is not None:
        result["family_resolution"] = _validate_family_resolution_trace(
            catalog, rows, source_registry, trace, available_pins)
    return result


def _validate_family_resolution_trace(
    catalog: Mapping[str, Mapping[str, Any]], parsed_rows: Sequence[Mapping[str, Any]],
    registry: Mapping[str, Any], trace: Sequence[Mapping[str, Any]],
    available_pins: Sequence[str],
) -> Dict[str, Any]:
    """Prove each formula selection against a complete, provenance-bearing family list."""
    provenance_fields = ("source_url", "retrieved_at", "source_revision", "source_hash")
    if any(not registry.get(field) for field in provenance_fields):
        raise CapabilityError("roster source registry lacks complete provenance")
    provenance = {field: registry[field] for field in provenance_fields}
    families = registry.get("families")
    if not isinstance(families, Mapping):
        raise CapabilityError("roster source registry lacks family candidate lists")
    trace_by_slot = {row.get("slot_family"): row for row in trace}
    parsed_by_family: Dict[str, set] = {}
    for row in parsed_rows:
        parsed_by_family.setdefault(_family_of_slug(row["slug"]), set()).add(
            (row["arena_name"], row["slug"], float(row["rating"])))
    output: Dict[str, Any] = {}
    for family in PRIMARY_FAMILIES:
        family_source = families.get(family)
        if not isinstance(family_source, Mapping) or family_source.get("complete") is not True:
            raise CapabilityError(f"roster source registry is not complete for {family}")
        candidates = family_source.get("candidates")
        if not isinstance(candidates, list) or not candidates:
            raise CapabilityError(f"roster source registry has no candidates for {family}")
        registry_rows = set()
        normalized_candidates = []
        for candidate in candidates:
            try:
                normalized = {
                    "arena_name": str(candidate["arena_name"]),
                    "slug": (str(candidate["openrouter_slug"])
                             if candidate.get("openrouter_slug") else None),
                    "rating": float(candidate["rating"]),
                    "eligible": candidate.get("eligible", True) is True,
                    "exclusion_reason": candidate.get("exclusion_reason"),
                }
            except (KeyError, TypeError, ValueError) as exc:
                raise CapabilityError(f"malformed roster candidate for {family}") from exc
            if normalized["eligible"]:
                if not normalized["slug"]:
                    raise CapabilityError(f"eligible roster candidate lacks slug for {family}")
                registry_rows.add((normalized["arena_name"], normalized["slug"],
                                   normalized["rating"]))
            elif not normalized["exclusion_reason"]:
                raise CapabilityError(
                    f"ineligible roster candidate lacks exclusion reason for {family}")
            normalized_candidates.append(normalized)
        if registry_rows != parsed_by_family.get(family, set()):
            raise CapabilityError(
                f"roster source registry does not match frozen Arena rows for {family}")
        selected = trace_by_slot.get(family)
        if selected is None or selected.get("slug") is None:
            raise CapabilityError(f"R59.2 has no resolved selection for {family}")
        selected_rating = float(selected["rating"])
        excluded = []
        for candidate in sorted(normalized_candidates,
                                key=lambda row: (-row["rating"], row["slug"])):
            if candidate["slug"] == selected["slug"] or candidate["rating"] <= selected_rating:
                continue
            slug = candidate["slug"]
            if not candidate["eligible"]:
                reason = str(candidate["exclusion_reason"])
            elif slug in available_pins:
                reason = "pinned-collision"
            elif slug not in catalog:
                reason = "not-openrouter-available"
            elif _family_of_slug(slug) in EXCLUDED_FAMILIES:
                reason = "anti-leak-family"
            elif not _text_nonpreview(catalog[slug]):
                reason = "preview-or-non-text"
            else:
                raise CapabilityError(
                    f"higher-rated eligible candidate {slug} was skipped for {family}")
            excluded.append(dict(candidate, reason=reason, provenance=provenance))
        output[family] = {
            "selected": dict(selected, provenance=provenance),
            "higher_rated_excluded": excluded,
            "source_complete": True,
            "source_note": family_source.get("review_note"),
        }
    return output


def normalize_capabilities(
    roster: Sequence[str], source_rows: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    """Freeze exact-source capability values; duplicate or non-exact values are missing."""
    grouped: Dict[tuple, List[Mapping[str, Any]]] = {}
    for source in source_rows:
        model = str(source.get("model", source.get("slug", "")))
        metric = str(source.get("metric", ""))
        if model not in roster or metric not in CAPABILITY_METRICS:
            continue
        if source.get("exact_match") is not True:
            continue
        grouped.setdefault((model, metric), []).append(source)

    normalized: List[Dict[str, Any]] = []
    for model in roster:
        row: Dict[str, Any] = {"model": model, "sources": {}, "missing": []}
        for metric in CAPABILITY_METRICS:
            matches = grouped.get((model, metric), [])
            if len(matches) != 1:
                row[metric] = None
                row["missing"].append(
                    f"{metric}: {'ambiguous' if len(matches) > 1 else 'missing'}")
                continue
            source = matches[0]
            try:
                value = float(source.get("value"))
            except (TypeError, ValueError):
                value = float("nan")
            required = ("source_url", "retrieved_at", "source_revision", "source_hash")
            if not math.isfinite(value) or any(not source.get(field) for field in required):
                row[metric] = None
                row["missing"].append(f"{metric}: incomplete-source")
                continue
            row[metric] = value
            row["sources"][metric] = {field: source[field] for field in required}
        normalized.append(row)
    return normalized


def compute_pc1(capability_rows: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
    """Apply R60.2 missingness and correlation PCA, oriented positively to Arena."""
    rows = [dict(row) for row in capability_rows]
    included = [
        row for row in rows
        if sum(row.get(metric) is not None for metric in CAPABILITY_METRICS) >= 2
    ]
    if len(included) < 2:
        raise CapabilityError("fewer than two models have two capability components")

    means: Dict[str, float] = {}
    stds: Dict[str, float] = {}
    for metric in CAPABILITY_METRICS:
        values = [float(row[metric]) for row in included if row.get(metric) is not None]
        if not values:
            raise CapabilityError(f"capability column {metric} has no values")
        means[metric] = float(np.mean(values))
        std = float(np.std(values, ddof=0))
        stds[metric] = std if std > 0 else 1.0

    matrix: List[List[float]] = []
    for row in included:
        available = {
            metric: (float(row[metric]) - means[metric]) / stds[metric]
            for metric in CAPABILITY_METRICS if row.get(metric) is not None
        }
        imputed = float(np.mean(list(available.values())))
        matrix.append([available.get(metric, imputed) for metric in CAPABILITY_METRICS])
    array = np.asarray(matrix, dtype=float)
    array -= array.mean(axis=0)
    column_std = array.std(axis=0, ddof=0)
    column_std[column_std == 0] = 1.0
    array /= column_std
    _u, _s, vh = np.linalg.svd(array, full_matrices=False)
    scores = array @ vh[0]
    arena_pairs = [
        (scores[index], float(row["lmarena_text"]))
        for index, row in enumerate(included) if row.get("lmarena_text") is not None
    ]
    if len(arena_pairs) >= 2:
        correlation = float(np.corrcoef(
            [pair[0] for pair in arena_pairs], [pair[1] for pair in arena_pairs])[0, 1])
        if math.isfinite(correlation) and correlation < 0:
            scores = -scores

    score_by_model = {row["model"]: float(scores[index]) for index, row in enumerate(included)}
    for row in rows:
        row["component_count"] = sum(
            row.get(metric) is not None for metric in CAPABILITY_METRICS)
        row["included"] = row["model"] in score_by_model
        row["pc1"] = score_by_model.get(row["model"])
    ranked = sorted(included, key=lambda row: (-score_by_model[row["model"]], row["model"]))
    return {
        "rows": rows,
        "frontier": [row["model"] for row in ranked[:5]],
        "ranked_models": [row["model"] for row in ranked],
        "g1_status": "ready" if len(included) >= 6 else "inconclusive-fewer-than-6",
        "standardized_column_std": [float(value) for value in array.std(axis=0, ddof=0)],
    }


def _item_value(item: Any, name: str, default: Any = None) -> Any:
    return item.get(name, default) if isinstance(item, Mapping) else getattr(item, name, default)


def _item_kind(item: Any) -> str:
    kind = _item_value(item, "kind")
    return str(kind) if kind else scorer_kind(item)


def _largest_remainder(records: Sequence[Any], n: int) -> Dict[str, int]:
    strata: Dict[str, List[Any]] = {}
    for item in records:
        strata.setdefault(str(_item_value(item, "design")), []).append(item)
    if n > len(records):
        raise ValueError(f"cannot sample {n} from {len(records)} eligible items")
    quotas = {name: n * len(values) / len(records) for name, values in strata.items()}
    allocation = {name: int(math.floor(value)) for name, value in quotas.items()}
    remaining = n - sum(allocation.values())
    order = sorted(strata, key=lambda name: (-(quotas[name] - allocation[name]), name))
    for name in order[:remaining]:
        allocation[name] += 1
    return allocation


def _stratified_sample(records: Sequence[Any], n: int, seed: int) -> tuple:
    allocation = _largest_remainder(records, n)
    by_design: Dict[str, List[Any]] = {}
    for item in records:
        by_design.setdefault(str(_item_value(item, "design")), []).append(item)
    rng = random.Random(seed)
    selected: List[Any] = []
    for design in sorted(by_design):
        stratum = sorted(by_design[design], key=lambda item: str(_item_value(item, "id")))
        selected.extend(rng.sample(stratum, allocation[design]))
    selected.sort(key=lambda item: str(_item_value(item, "id")))
    return selected, allocation


def select_g5c_samples(
    items: Sequence[Any], *, priming_seed: int = 1647, evaluation_seed: int = 1648,
) -> Dict[str, Any]:
    """Select the deterministic, design-stratified disjoint 23/100 G5c sets."""
    eligible = []
    for item in items:
        extra = _item_value(item, "extra", {}) or {}
        kind = _item_kind(item)
        if extra.get("dev_set_only") or kind in {EPISODE, CONTESTED}:
            continue
        eligible.append(item)
    eligible.sort(key=lambda item: str(_item_value(item, "id")))
    priming, priming_allocation = _stratified_sample(eligible, 23, priming_seed)
    priming_ids = {str(_item_value(item, "id")) for item in priming}
    remaining = [item for item in eligible if str(_item_value(item, "id")) not in priming_ids]
    evaluation, evaluation_allocation = _stratified_sample(remaining, 100, evaluation_seed)
    return {
        "priming_ids": [str(_item_value(item, "id")) for item in priming],
        "evaluation_ids": [str(_item_value(item, "id")) for item in evaluation],
        "priming_allocation": priming_allocation,
        "evaluation_allocation": evaluation_allocation,
        "priming_seed": priming_seed,
        "evaluation_seed": evaluation_seed,
    }


def _per_judge_call_weight(item: Any) -> int:
    """Calls made by one manifest judge for one normal response scoring pass."""
    kind = _item_kind(item)
    if kind == "open":
        axes = {
            getattr(keypoint, "axis", None)
            for keypoint in (_item_value(item, "rubric", []) or [])
            if getattr(keypoint, "axis", None) in {"matter", "manner", "end"}
        }
        return 3 if not axes else 1 + len({"matter", "manner", "end"} - axes)
    if kind == CONTESTED:
        return 3 + (1 if settled_core_keypoints(item) else 0)
    if kind == EPISODE:
        return 1
    return 0


def _call_totals(classes: Sequence[Mapping[str, Any]]) -> Dict[str, int]:
    sut = sum(int(row["count"]) for row in classes if row["role"] == "sut")
    judge = sum(int(row["count"]) for row in classes if row["role"] == "judge")
    return {"sut": sut, "judge": judge, "total": sut + judge}


def build_call_plan(
    items: Sequence[Any], roster: Sequence[str], frontier: Sequence[str],
    g5c_plan: Mapping[str, Any],
) -> Dict[str, Any]:
    """Build the binding logical-call schedule without constructing any client."""
    runnable = [
        item for item in items
        if not (_item_value(item, "extra", {}) or {}).get("dev_set_only")
    ]
    if len(runnable) != 226:
        raise ValueError(f"frozen T4 bank must contain 226 runnable items, found {len(runnable)}")
    if len(roster) < 8 or len(roster) > 10 or len(frontier) != 5:
        raise ValueError("call plan requires an R59.2 roster of 8-10 and frontier of 5")
    variant_counts = {
        axis: sum(
            any(str(label).strip().upper().startswith(axis)
                for label in (_item_value(item, "perturbations", []) or []))
            for item in runnable)
        for axis in ("P3", "P4", "P6")
    }
    if variant_counts != {"P3": 140, "P4": 131, "P6": 25}:
        raise ValueError(f"frozen perturbation counts drifted: {variant_counts}")

    classes: List[Dict[str, Any]] = []
    base_judge_weight = sum(_per_judge_call_weight(item) for item in runnable)
    for model in roster:
        classes.append({
            "phase": "base", "role": "sut", "model": model,
            "sut_context": model, "request_class": "base_sut", "count": len(runnable)})
        for judge in JUDGE_SLUGS:
            classes.append({
                "phase": "base", "role": "judge", "model": judge,
                "sut_context": model, "request_class": "base_judge",
                "count": base_judge_weight})
    for axis, item_count in variant_counts.items():
        axis_items = [
            item for item in runnable
            if any(str(label).strip().upper().startswith(axis)
                   for label in (_item_value(item, "perturbations", []) or []))
        ]
        axis_judge_weight = sum(_per_judge_call_weight(item) for item in axis_items)
        for model in frontier:
            classes.append({
                "phase": f"variant_{axis.lower()}", "role": "sut", "model": model,
                "sut_context": model, "request_class": f"variant_{axis.lower()}_sut",
                "count": item_count})
            for judge in JUDGE_SLUGS:
                classes.append({
                    "phase": f"variant_{axis.lower()}", "role": "judge", "model": judge,
                    "sut_context": model,
                    "request_class": f"variant_{axis.lower()}_judge",
                    "count": axis_judge_weight})

    open_items = [item for item in runnable if _item_kind(item) == "open"]
    g5b_per_judge = sum(_per_judge_call_weight(item) for item in open_items)
    for judge in JUDGE_SLUGS:
        classes.append({
            "phase": "g5b", "role": "judge", "model": judge,
            "request_class": "g5b_judge", "count": g5b_per_judge})

    evaluation_ids = set(g5c_plan["evaluation_ids"])
    by_id = {str(_item_value(item, "id")): item for item in runnable}
    evaluation = [by_id[item_id] for item_id in evaluation_ids]
    g5c_per_judge = 2 * sum(_per_judge_call_weight(item) for item in evaluation)
    probe_model = frontier[4]
    classes.append({
        "phase": "g5c", "role": "sut", "model": probe_model,
        "sut_context": probe_model,
        "request_class": "g5c_sut", "count": 200})
    for judge in JUDGE_SLUGS:
        classes.append({
            "phase": "g5c", "role": "judge", "model": judge,
            "request_class": "g5c_judge", "count": g5c_per_judge})

    phase_rows = lambda names: [row for row in classes if row["phase"] in names]
    totals = {
        "base": _call_totals(phase_rows({"base"})),
        "variants": _call_totals(phase_rows({"variant_p3", "variant_p4", "variant_p6"})),
        "g5b": _call_totals(phase_rows({"g5b"})),
        "g5c": _call_totals(phase_rows({"g5c"})),
        "full": _call_totals(classes),
    }
    episode_count = sum(_item_kind(item) == EPISODE for item in runnable)
    dropped_episode_models = [model for model in roster if model not in frontier]
    episode_removal_classes: List[Dict[str, Any]] = []
    for model in dropped_episode_models:
        episode_removal_classes.append({
            "phase": "episode_roster_reduction", "role": "sut", "model": model,
            "request_class": "base_sut", "count": episode_count})
        for judge in JUDGE_SLUGS:
            episode_removal_classes.append({
                "phase": "episode_roster_reduction", "role": "judge", "model": judge,
                "request_class": "base_judge", "count": episode_count})
    return {
        "classes": classes,
        "totals": totals,
        "variant_item_counts": variant_counts,
        "base_per_judge_weight": base_judge_weight,
        "g5c_per_judge_weight": g5c_per_judge,
        "probe_model": probe_model,
        "roster": list(roster),
        "frontier": list(frontier),
        "episode_removal_classes": episode_removal_classes,
    }


def validate_token_profiles(profiles: Mapping[str, Mapping[str, Any]]) -> None:
    """Accept only class-specific rendered-prompt/fixed-completion ceiling profiles."""
    if set(profiles) != set(REQUEST_CLASSES):
        raise ValueError("token profiles must cover every request class exactly")
    provenances = set()
    for request_class in REQUEST_CLASSES:
        profile = profiles[request_class]
        source = str(profile.get("source", ""))
        if source != "rendered_prompt_fixed_completion_ceiling":
            raise ValueError(f"unsupported token profile for {request_class}")
        derivation = profile.get("derivation")
        if not isinstance(derivation, Mapping):
            raise ValueError(f"unsupported token profile derivation for {request_class}")
        if derivation.get("request_class") != request_class:
            raise ValueError(f"token profile is not per-request-class for {request_class}")
        if derivation.get("prompt_method") != "max_rendered_utf8_bytes":
            raise ValueError(f"unsupported token profile prompt method for {request_class}")
        if derivation.get("completion_method") != "fixed_max_tokens":
            raise ValueError(f"unsupported token profile completion method for {request_class}")
        try:
            prompt_tokens = int(profile["prompt_tokens"])
            completion_tokens = int(profile["completion_tokens"])
            rendered_bytes = int(derivation["max_rendered_prompt_bytes"])
            completion_cap = int(derivation["fixed_completion_cap"])
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"unsupported token profile values for {request_class}") from exc
        if prompt_tokens <= 0 or prompt_tokens != rendered_bytes:
            raise ValueError(f"unsupported token profile prompt ceiling for {request_class}")
        if completion_tokens <= 0 or completion_tokens != completion_cap:
            raise ValueError(f"unsupported token profile completion ceiling for {request_class}")
        if not derivation.get("prompt_scope") or not derivation.get("completion_provenance"):
            raise ValueError(f"unsupported token profile provenance for {request_class}")
        prompt_provenance = str(derivation.get("prompt_provenance", ""))
        if not prompt_provenance or prompt_provenance in provenances:
            raise ValueError(f"token profile provenance is shared for {request_class}")
        provenances.add(prompt_provenance)


def estimate_cost(
    call_classes: Sequence[Mapping[str, Any]],
    catalog: Mapping[str, Mapping[str, Any]],
    token_profiles: Mapping[str, Mapping[str, Any]],
) -> Dict[str, Any]:
    """Price every request class from current catalog per-token prices."""
    rows: List[Dict[str, Any]] = []
    total = 0.0
    for call_class in call_classes:
        profile_name = str(call_class["request_class"])
        if profile_name not in token_profiles:
            raise KeyError(f"missing token profile for {profile_name!r}")
        profile = token_profiles[profile_name]
        prompt_tokens = int(profile["prompt_tokens"])
        completion_tokens = int(profile["completion_tokens"])
        model = str(call_class["model"])
        prices = mvp.price_for(model, dict(catalog))
        if not all(math.isfinite(price) and price >= 0 for price in prices):
            raise mvp.PricingError(f"invalid catalog price for model {model!r}")
        count = int(call_class["count"])
        per_call = mvp.cell_cost(prompt_tokens, completion_tokens, prices)
        subtotal = count * per_call
        row = dict(call_class)
        row.update({
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "prompt_price": prices[0],
            "completion_price": prices[1],
            "token_source": profile.get("source", "ceiling"),
            "per_call_usd": per_call,
            "subtotal_usd": subtotal,
        })
        rows.append(row)
        total += subtotal
    return {"rows": rows, "total_usd": total}


def minimum_ratifiable_cap(forecast_usd: float) -> float:
    cents = (Decimal(str(forecast_usd)) / Decimal("0.80") * 100).to_integral_value(
        rounding=ROUND_CEILING)
    return float(cents / 100)


def required_top_up(required_cap: float, limit_remaining: Optional[float]) -> float:
    remaining = Decimal("0") if limit_remaining is None else Decimal(str(limit_remaining))
    value = max(Decimal("0"), Decimal(str(required_cap)) - remaining)
    return float(value.quantize(Decimal("0.01"), rounding=ROUND_CEILING))


def select_cheapest_base_shard(
    roster: Sequence[str], catalog: Mapping[str, Mapping[str, Any]],
    token_profile: Mapping[str, Any], *, n: int = 5,
) -> List[Dict[str, Any]]:
    """Rank roster models by their forecasted base SUT call cost, ties by slug."""
    rows = []
    prompt_tokens = int(token_profile["prompt_tokens"])
    completion_tokens = int(token_profile["completion_tokens"])
    for model in roster:
        price = mvp.price_for(model, dict(catalog))
        per_call = mvp.cell_cost(prompt_tokens, completion_tokens, price)
        rows.append({"model": model, "per_base_sut_call_usd": per_call})
    rows.sort(key=lambda row: (row["per_base_sut_call_usd"], row["model"]))
    return rows[:n]


def forecast_runtime(call_count: int, throughput: float = T3_CALLS_PER_MINUTE) -> Dict[str, Any]:
    if call_count < 0 or not math.isfinite(throughput) or throughput <= 0:
        raise ValueError("runtime forecast requires nonnegative calls and positive throughput")
    baseline = call_count / throughput
    return {
        "logical_calls": call_count,
        "calls_per_minute": throughput,
        "baseline_minutes": baseline,
        "planning_band_minutes": [call_count / (throughput * 1.25),
                                  call_count / (throughput * 0.75)],
    }


def forecast_branches(
    call_plan: Mapping[str, Any], *,
    catalog: Optional[Mapping[str, Mapping[str, Any]]] = None,
    token_profiles: Optional[Mapping[str, Mapping[str, Any]]] = None,
    key_snapshot: Optional[Mapping[str, Any]] = None,
) -> List[Dict[str, Any]]:
    """Calculate every cumulative R59.5 branch without selecting one."""
    classes = list(call_plan["classes"])
    exclusions = [set(), {"variant_p6"}, {"variant_p6", "variant_p3"},
                  {"variant_p6", "variant_p3", "variant_p4"}]
    names = ["full", "drop_p6", "drop_p3", "drop_p4"]
    rows: List[Dict[str, Any]] = []
    active_sets: List[List[Mapping[str, Any]]] = []
    for name, excluded in zip(names, exclusions):
        active = [row for row in classes if row["phase"] not in excluded]
        active_sets.append(active)
        rows.append({"branch": name, "logical_calls": _call_totals(active)["total"],
                     "selected": False})

    episode_removal = list(call_plan["episode_removal_classes"])
    episode_saving = _call_totals(episode_removal)["total"]
    rows.append({
        "branch": "halve_episode_roster",
        "logical_calls": rows[-1]["logical_calls"] - episode_saving,
        "prescribed_call_saving": episode_saving,
        "requires_jimmy_ruling": True,
        "conflict": "prescribed rung drops base EPISODE cells although base cells are never dropped",
        "selected": False,
    })

    if catalog is not None and token_profiles is not None:
        costs = [estimate_cost(active, catalog, token_profiles)["total_usd"]
                 for active in active_sets]
        episode_cost = estimate_cost(episode_removal, catalog, token_profiles)["total_usd"]
        costs.append(costs[-1] - episode_cost)
        remaining = None if key_snapshot is None else key_snapshot.get("limit_remaining")
        for row, cost in zip(rows, costs):
            cap = minimum_ratifiable_cap(cost)
            row.update({
                "forecast_cost_usd": cost,
                "runtime": forecast_runtime(row["logical_calls"]),
                "minimum_ratifiable_cap_usd": cap,
                "required_top_up_usd": required_top_up(cap, remaining),
            })
    return rows


def _contains_secret(value: Any, forbidden: Sequence[str]) -> bool:
    if isinstance(value, Mapping):
        if any(str(key).lower() in {"api_key", "authorization"} for key in value):
            return True
        return any(_contains_secret(item, forbidden) for item in value.values())
    if isinstance(value, (list, tuple)):
        return any(_contains_secret(item, forbidden) for item in value)
    text = str(value)
    return any(secret and secret in text for secret in forbidden) or "sk-or-v1-" in text


def _csv_text(rows: Any) -> str:
    normalized = [dict(row) for row in (rows or [])]
    if not normalized:
        normalized = [{"provenance_canary": CANARY}]
    for row in normalized:
        row["provenance_canary"] = CANARY
    fieldnames = sorted({key for row in normalized for key in row})
    from io import StringIO
    buffer = StringIO()
    writer = csv.DictWriter(buffer, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(normalized)
    return buffer.getvalue()


def write_new_artifacts(
    output_dir: os.PathLike,
    payloads: Mapping[str, Any],
    *,
    forbidden_values: Sequence[str] = (),
) -> List[str]:
    """Write exactly five canaried artifacts, exclusively, into a new directory."""
    if set(payloads) != EXPECTED_ARTIFACTS:
        raise ValueError(f"artifact payload names must be exactly {sorted(EXPECTED_ARTIFACTS)}")
    if _contains_secret(payloads, tuple(forbidden_values)):
        raise SecretDisclosureError("refusing to write credential material")
    output = Path(output_dir)
    output.mkdir(parents=False, exist_ok=False)
    paths: List[str] = []
    for filename in sorted(payloads):
        payload = payloads[filename]
        if filename.endswith(".csv"):
            text = _csv_text(payload)
        elif filename.endswith(".json"):
            value = dict(payload)
            value["provenance_canary"] = CANARY
            text = json.dumps(value, indent=2, sort_keys=True) + "\n"
        else:
            text = str(payload).rstrip() + f"\n\nCanary: `{CANARY}`\n"
        path = output / filename
        with path.open("x", encoding="utf-8") as handle:
            handle.write(text)
        paths.append(str(path))
    return paths


def build_preflight_payloads(
    inputs: Mapping[str, Any], metadata: Mapping[str, Any],
) -> Dict[str, Any]:
    """Pure JSON-input orchestrator for the five zero-paid frozen artifacts."""
    required = {"arena_rows", "alias_rows", "roster_source_registry",
                "capability_source_rows", "token_profiles"}
    missing = sorted(required - set(inputs))
    if missing:
        raise ValueError(f"inputs JSON missing required field(s): {', '.join(missing)}")
    catalog = metadata["catalog"]
    key_snapshot = metadata["key_snapshot"]
    resolution = resolve_roster(
        catalog, inputs["arena_rows"], inputs["alias_rows"],
        source_registry=inputs["roster_source_registry"])
    capabilities = normalize_capabilities(
        resolution["roster"], inputs["capability_source_rows"])
    pc1 = compute_pc1(capabilities)
    items = load_items(str(BANK_DIR))
    g5c = select_g5c_samples(items)
    call_plan = build_call_plan(items, resolution["roster"], pc1["frontier"], g5c)
    profiles = inputs["token_profiles"]
    validate_token_profiles(profiles)
    cheap = select_cheapest_base_shard(
        resolution["roster"], catalog, profiles["base_sut"])
    cheap_models = {row["model"] for row in cheap}
    phase_one_classes = [
        row for row in call_plan["classes"]
        if row["phase"] == "base" and row.get("sut_context") in cheap_models
    ]
    full_cost = estimate_cost(call_plan["classes"], catalog, profiles)
    phase_one_cost = estimate_cost(phase_one_classes, catalog, profiles)
    branches = forecast_branches(
        call_plan, catalog=catalog, token_profiles=profiles, key_snapshot=key_snapshot)
    full_cap = minimum_ratifiable_cap(full_cost["total_usd"])
    phase_one_cap = minimum_ratifiable_cap(phase_one_cost["total_usd"])
    remaining = key_snapshot.get("limit_remaining")
    relevant = set(resolution["roster"]) | set(JUDGE_SLUGS)
    catalog_rows = [catalog[slug] for slug in sorted(relevant)]
    catalog_hash = hashlib.sha256(
        json.dumps(catalog_rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    phase_one_calls = _call_totals(phase_one_classes)["total"]
    catalog_retrieved_at = metadata.get("catalog_retrieved_at")
    if not catalog_retrieved_at:
        raise ValueError("metadata lacks actual /models retrieval timestamp")
    manifest = {
        "catalog_retrieved_at": catalog_retrieved_at,
        "roster_resolution": resolution,
        "frontier": pc1["frontier"],
        "five_cheapest_base_shard": cheap,
        "g5c_plan": g5c,
        "call_plan": call_plan,
        "phase_one_logical_calls": phase_one_calls,
        "phase_one_cost": phase_one_cost,
        "full_cost": full_cost,
        "phase_one_runtime": forecast_runtime(phase_one_calls),
        "full_runtime": forecast_runtime(call_plan["totals"]["full"]["total"]),
        "phase_one_minimum_cap_usd": phase_one_cap,
        "full_minimum_cap_usd": full_cap,
        "phase_one_top_up_usd": required_top_up(phase_one_cap, remaining),
        "full_top_up_usd": required_top_up(full_cap, remaining),
        "branches": branches,
        "catalog_hash": catalog_hash,
        "master_seed": 1647,
        "paid_inference_authorized": False,
    }
    report = (
        "# WCF-Bench T4 zero-paid preflight\n\n"
        f"- Roster: {', '.join(resolution['roster'])}\n"
        f"- Five-cheapest base shard: {', '.join(row['model'] for row in cheap)}\n"
        f"- Phase-one calls / forecast: {phase_one_calls} / "
        f"${phase_one_cost['total_usd']:.6f}\n"
        f"- Full calls / forecast: {call_plan['totals']['full']['total']} / "
        f"${full_cost['total_usd']:.6f}\n"
        f"- Phase-one minimum cap / top-up: ${phase_one_cap:.2f} / "
        f"${required_top_up(phase_one_cap, remaining):.2f}\n"
        f"- Full minimum cap / top-up: ${full_cap:.2f} / "
        f"${required_top_up(full_cap, remaining):.2f}\n"
        "- Paid inference calls: not authorized and not performed.\n"
    )
    exclusion_lines = []
    for family, family_trace in resolution["family_resolution"].items():
        for excluded in family_trace["higher_rated_excluded"]:
            exclusion_lines.append(
                f"- {family}: {excluded['arena_name']} ({excluded['rating']}) — "
                f"{excluded['reason']}")
        if family_trace.get("source_note"):
            exclusion_lines.append(f"- {family}: {family_trace['source_note']}")
    report += "\n## Higher-rated formula exclusions\n\n" + (
        "\n".join(exclusion_lines) if exclusion_lines else "- None in the frozen source registry.")
    report += "\n"
    cost_rows = [dict(row, scope="full") for row in full_cost["rows"]]
    cost_rows.extend(dict(row, scope="phase_one") for row in phase_one_cost["rows"])
    return {
        "capability-battery.csv": pc1["rows"],
        "openrouter-catalog-snapshot.json": {
            "retrieved_at": catalog_retrieved_at, "source_hash": catalog_hash,
            "models": catalog_rows,
        },
        "t4-run-manifest.json": manifest,
        "t4-cost-plan.csv": cost_rows,
        "t4-preflight-report.md": report,
    }


def _print_dry_plan() -> None:
    print("WCF-Bench T4 preflight — DRY RUN (zero network calls, zero writes)")
    print("Use --metadata-preflight only after supplying runtime credentials and frozen inputs.")
    print("This controller has no completion endpoint and performs no paid inference.")


def main(
    argv: Optional[Sequence[str]] = None,
    *,
    metadata_fetch: Callable[..., Any] = fetch_openrouter_metadata,
    artifact_writer: Callable[..., Any] = write_new_artifacts,
) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--metadata-preflight", action="store_true")
    parser.add_argument("--output-dir")
    parser.add_argument("--inputs-json")
    args = parser.parse_args(argv)
    if not args.metadata_preflight:
        _print_dry_plan()
        return 0
    if not args.output_dir:
        parser.error("--metadata-preflight requires --output-dir")
    if not args.inputs_json:
        parser.error("--metadata-preflight requires --inputs-json")
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        parser.error("OPENROUTER_API_KEY is required at call time")
    with open(args.inputs_json, encoding="utf-8") as handle:
        inputs = json.load(handle)
    metadata = metadata_fetch(api_key)
    payloads = build_preflight_payloads(inputs, metadata)
    artifact_writer(args.output_dir, payloads, forbidden_values=[api_key])
    snapshot = metadata["key_snapshot"]
    manifest = payloads["t4-run-manifest.json"]
    print("Authorized metadata GETs and artifact freeze complete; no inference call was made.")
    print(f"catalog models: {len(metadata['catalog'])}; limit remaining: {snapshot.get('limit_remaining')}")
    print(f"phase one: {manifest['phase_one_logical_calls']} calls, "
          f"${manifest['phase_one_cost']['total_usd']:.6f}")
    print(f"full: {manifest['call_plan']['totals']['full']['total']} calls, "
          f"${manifest['full_cost']['total_usd']:.6f}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
