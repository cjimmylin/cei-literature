#!/usr/bin/env python3
"""Zero-paid, metadata-only preflight for the WCF-Bench PPP-1 preview."""

from __future__ import annotations

import argparse
import copy
import datetime
import hashlib
import json
import math
import os
from pathlib import Path
from typing import Any, Callable, Dict, Mapping, Optional, Sequence

from wcfbench import EPISODE, load_items, scorer_kind

import t4_preflight as t4


PPP1_SUTS = (
    "meta-llama/llama-3.1-8b-instruct",
    "deepseek/deepseek-chat",
    "qwen/qwen3.7-plus",
)
PPP1_JUDGE = "google/gemini-2.5-flash"
VALIDITY_LABEL = "EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE"
STRATEGY_CAP_USD = 5.0
EXPECTED_ARTIFACTS = {
    "auth-snapshot.json",
    "openrouter-catalog-snapshot.json",
    "ppp1-run-manifest.json",
    "ppp1-cost-plan.csv",
    "ppp1-preflight-report.md",
}
CORRECTION_ARTIFACTS = {
    "ppp1-retry-correction.json",
    "ppp1-retry-cost-plan.csv",
    "ppp1-retry-correction-report.md",
}
BRANCH_ADDENDUM_ARTIFACTS = {
    "ppp1-branch-addendum.json",
    "ppp1-branch-cost-plan.csv",
    "ppp1-branch-addendum-report.md",
}
BRANCH_JUDGE_COMPLETION_TOKENS = (2048, 1024, 512, 256, 0)
BANK_DIR = Path(__file__).resolve().parent.parent / "05-BANK-YAML"
SecretDisclosureError = t4.SecretDisclosureError


def _utc_now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat(
        timespec="seconds").replace("+00:00", "Z")


def fetch_openrouter_metadata(
    api_key: str,
    *,
    opener: Optional[Callable[[str, Optional[str]], Dict[str, Any]]] = None,
    now: Callable[[], str] = _utc_now,
) -> Dict[str, Any]:
    """Reuse the two authorized GETs and timestamp each completed response."""
    timestamps: Dict[str, str] = {}

    def timestamping_opener(url: str, key: Optional[str]) -> Dict[str, Any]:
        payload = (opener or t4.mvp._http_get_json)(url, key)
        timestamps[url] = now()
        return payload

    metadata = t4.fetch_openrouter_metadata(
        api_key, opener=timestamping_opener,
        now=lambda: timestamps.get(t4.MODELS_URL, now()))
    metadata["auth_retrieved_at"] = timestamps[t4.AUTH_KEY_URL]
    metadata["catalog_retrieved_at"] = timestamps[t4.MODELS_URL]
    return metadata


def _token_profile_subset(token_profiles: Mapping[str, Mapping[str, Any]]) -> Dict[str, Any]:
    profiles = {}
    for request_class in ("base_sut", "base_judge"):
        if request_class not in token_profiles:
            raise ValueError(f"missing token profile for {request_class}")
        profile = copy.deepcopy(dict(token_profiles[request_class]))
        try:
            prompt_tokens = int(profile["prompt_tokens"])
            completion_tokens = int(profile["completion_tokens"])
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"invalid token profile for {request_class}") from exc
        if prompt_tokens <= 0 or completion_tokens != 2048:
            raise ValueError(f"unsupported token ceiling for {request_class}")
        if profile.get("source") != "rendered_prompt_fixed_completion_ceiling":
            raise ValueError(f"unsupported token source for {request_class}")
        derivation = profile.get("derivation") or {}
        if derivation.get("request_class") != request_class:
            raise ValueError(f"token profile is not per-request-class for {request_class}")
        profiles[request_class] = profile
    return profiles


def _validate_catalog(catalog: Mapping[str, Mapping[str, Any]]) -> list:
    capability_rows = []
    for slug in (*PPP1_SUTS, PPP1_JUDGE):
        entry = catalog.get(slug)
        if entry is None:
            raise ValueError(f"missing exact PPP-1 catalog slug: {slug}")
        if not t4._text_nonpreview(entry):
            raise ValueError(f"PPP-1 model is not current non-preview text I/O: {slug}")
        try:
            prompt_price, completion_price = t4.mvp.price_for(slug, dict(catalog))
        except Exception as exc:
            raise ValueError(f"missing exact PPP-1 catalog price: {slug}") from exc
        if not all(math.isfinite(value) and value > 0
                   for value in (prompt_price, completion_price)):
            raise ValueError(f"nonpositive PPP-1 catalog price: {slug}")
        supported = sorted(set(entry.get("supported_parameters") or []))
        for required_parameter in ("max_tokens", "response_format"):
            if required_parameter not in supported:
                raise ValueError(
                    f"missing required parameter {required_parameter}: {slug}")
        capability_rows.append({
            "model": slug,
            "context_length": entry.get("context_length"),
            "supported_parameters": supported,
            "declares_max_tokens": "max_tokens" in supported,
            "declares_response_format": True,
            "prompt_price": prompt_price,
            "completion_price": completion_price,
        })
    return capability_rows


def build_call_plan(items: Sequence[Any]) -> Dict[str, Any]:
    runnable = [
        item for item in items
        if not (t4._item_value(item, "extra", {}) or {}).get("dev_set_only")
    ]
    if len(runnable) != 226:
        raise ValueError(f"PPP-1 requires 226 runnable items, found {len(runnable)}")
    judge_calls_per_sut = sum(t4._per_judge_call_weight(item) for item in runnable)
    if judge_calls_per_sut != 348:
        raise ValueError(
            f"PPP-1 single-judge weight drifted: expected 348, found {judge_calls_per_sut}")
    classes = []
    for sut in PPP1_SUTS:
        classes.append({
            "phase": "base", "role": "sut", "model": sut,
            "sut_context": sut, "request_class": "base_sut", "count": 226,
        })
        classes.append({
            "phase": "base", "role": "judge", "model": PPP1_JUDGE,
            "sut_context": sut, "request_class": "base_judge",
            "count": judge_calls_per_sut,
        })
    totals = t4._call_totals(classes)
    if totals != {"sut": 678, "judge": 1044, "total": 1722}:
        raise ValueError(f"PPP-1 call geometry drifted: {totals}")
    episode_items = [item for item in runnable if scorer_kind(item) == EPISODE]
    normal_items = [item for item in runnable if scorer_kind(item) != EPISODE]
    if (len(normal_items), len(episode_items)) != (204, 22):
        raise ValueError(
            "PPP-1 runner coverage must be 204 normal + 22 EPISODE items")
    item_manifest = [{
        "item_id": str(t4._item_value(item, "id")),
        "design": str(t4._item_value(item, "design")),
        "kind": scorer_kind(item),
        "execution_path": ("episode_run" if scorer_kind(item) == EPISODE else "run_mvp"),
    } for item in sorted(runnable, key=lambda value: str(t4._item_value(value, "id")))]
    excluded = sorted(
        str(t4._item_value(item, "id")) for item in items
        if (t4._item_value(item, "extra", {}) or {}).get("dev_set_only"))
    return {
        "runnable_items": len(runnable),
        "normal_items": len(normal_items),
        "episode_items": len(episode_items),
        "excluded_dev_set_only_ids": excluded,
        "item_manifest": item_manifest,
        "judge_calls_per_sut": judge_calls_per_sut,
        "classes": classes,
        "totals": totals,
        "initial_api_attempts": totals["total"],
        "retry_reserved_api_attempts": totals["total"] * 2,
        "retry_reservation_increment": totals["total"],
        "retry_policy": (
            "conservative reservation of one retry per logical request; "
            "a retry is not selected spend"),
    }


def build_retry_geometry(items: Sequence[Any]) -> Dict[str, Any]:
    """Derive maximum API attempts from the existing runner/scorer retry seams."""
    runnable = [
        item for item in items
        if not (t4._item_value(item, "extra", {}) or {}).get("dev_set_only")
    ]
    normal = [item for item in runnable if scorer_kind(item) != EPISODE]
    episodes = [item for item in runnable if scorer_kind(item) == EPISODE]
    open_items = [item for item in runnable if scorer_kind(item) == "open"]
    contested = [item for item in runnable if scorer_kind(item) == "contested"]
    if (len(normal), len(episodes), len(open_items), len(contested)) != (204, 22, 161, 4):
        raise ValueError("PPP-1 retry geometry requires frozen 204/22/161/4 item counts")

    open_groups = {
        "tagged_all_axes": {"items": 0, "initial_per_item": 1, "maximum_per_item": 4},
        "tagged_two_axes": {"items": 0, "initial_per_item": 2, "maximum_per_item": 6},
        "tagged_one_axis": {"items": 0, "initial_per_item": 3, "maximum_per_item": 8},
        "numeric_three_axes": {"items": 0, "initial_per_item": 3, "maximum_per_item": 6},
    }
    for item in open_items:
        axes = {
            getattr(keypoint, "axis", None)
            for keypoint in (t4._item_value(item, "rubric", []) or [])
            if getattr(keypoint, "axis", None) in {"matter", "manner", "end"}
        }
        if not axes:
            group = "numeric_three_axes"
        elif len(axes) == 3:
            group = "tagged_all_axes"
        elif len(axes) == 2:
            group = "tagged_two_axes"
        else:
            group = "tagged_one_axis"
        open_groups[group]["items"] += 1
    expected_open_groups = {
        "tagged_all_axes": 49, "tagged_two_axes": 75,
        "tagged_one_axis": 4, "numeric_three_axes": 33,
    }
    if {name: row["items"] for name, row in open_groups.items()} != expected_open_groups:
        raise ValueError(f"PPP-1 OPEN retry geometry drifted: {open_groups}")

    open_initial_per_sut = sum(
        row["items"] * row["initial_per_item"] for row in open_groups.values())
    open_maximum_per_sut = sum(
        row["items"] * row["maximum_per_item"] for row in open_groups.values())
    contested_initial_per_sut = sum(t4._per_judge_call_weight(item) for item in contested)
    contested_maximum_per_sut = len(contested) * 10
    initial = {
        "normal_sut": len(normal) * len(PPP1_SUTS),
        "episode_sut": len(episodes) * len(PPP1_SUTS),
        "open_judge": open_initial_per_sut * len(PPP1_SUTS),
        "contested_judge": contested_initial_per_sut * len(PPP1_SUTS),
        "episode_judge": len(episodes) * len(PPP1_SUTS),
    }
    maximum = {
        "normal_sut": initial["normal_sut"],
        "episode_sut": initial["episode_sut"] * 2,
        "open_judge": open_maximum_per_sut * len(PPP1_SUTS),
        "contested_judge": contested_maximum_per_sut * len(PPP1_SUTS),
        "episode_judge": initial["episode_judge"] * 2,
    }
    initial["total"] = sum(initial.values())
    maximum["total"] = sum(maximum.values())
    if initial["total"] != 1722 or maximum["total"] != 3624:
        raise ValueError(f"PPP-1 retry attempt totals drifted: {initial} / {maximum}")
    return {
        "initial_api_attempts": initial,
        "maximum_api_attempts": maximum,
        "maximum_retry_increment": maximum["total"] - initial["total"],
        "open_item_geometry": open_groups,
        "per_sut_judge_attempts": {
            "initial": {
                "open": open_initial_per_sut,
                "contested": contested_initial_per_sut,
                "episode": len(episodes),
                "total": open_initial_per_sut + contested_initial_per_sut + len(episodes),
            },
            "maximum": {
                "open": open_maximum_per_sut,
                "contested": contested_maximum_per_sut,
                "episode": len(episodes) * 2,
                "total": open_maximum_per_sut + contested_maximum_per_sut + len(episodes) * 2,
            },
        },
        "derivation": {
            "normal_sut": (
                "wcfbench.runner._score_item: one completion; exceptions are recorded, "
                "not retried"),
            "episode_sut": (
                "episode_run._RetryingSUTClient.complete: one conditional transport retry"),
            "open_judge": (
                "JudgePanel.score_open whole-score transport replay plus triaxial award "
                "truncation retry; numeric-only items have whole-score replay only"),
            "contested_judge": (
                "JudgePanel.score_contested whole-score transport replay plus disclosure "
                "complete_with_retry; four logical calls become at most ten attempts"),
            "episode_judge": (
                "JudgePanel.score_episode uses _score_judge_with_retry around one emission"),
        },
    }


def build_budget_branches(
    classes: Sequence[Mapping[str, Any]],
    catalog: Mapping[str, Mapping[str, Any]],
    token_profiles: Mapping[str, Mapping[str, Any]],
) -> list:
    profiles = _token_profile_subset(token_profiles)
    rows = []
    for judge_tokens in BRANCH_JUDGE_COMPLETION_TOKENS:
        branch_profiles = copy.deepcopy(profiles)
        branch_profiles["base_judge"]["completion_tokens"] = judge_tokens
        executable = judge_tokens > 0
        if not executable:
            branch_profiles["base_sut"]["completion_tokens"] = 0
        cost = t4.estimate_cost(classes, catalog, branch_profiles)["total_usd"]
        cap = t4.minimum_ratifiable_cap(cost)
        rows.append({
            "branch": (f"judge_max_tokens_{judge_tokens}" if executable
                       else "zero_completion_price_floor"),
            "sut_completion_tokens": int(
                branch_profiles["base_sut"]["completion_tokens"]),
            "judge_completion_tokens": judge_tokens,
            "executable": executable,
            "forecast_cost_usd": cost,
            "minimum_ratifiable_cap_usd": cap,
            "within_strategy_cap": cap <= STRATEGY_CAP_USD,
        })
    return rows


def build_preflight_payloads(
    token_profiles: Mapping[str, Mapping[str, Any]],
    metadata: Mapping[str, Any],
) -> Dict[str, Any]:
    catalog = metadata.get("catalog")
    if not isinstance(catalog, Mapping):
        raise ValueError("metadata lacks normalized OpenRouter catalog")
    retrieved_at = metadata.get("catalog_retrieved_at")
    if not retrieved_at:
        raise ValueError("metadata lacks actual catalog retrieval timestamp")
    key_snapshot = metadata.get("key_snapshot")
    if not isinstance(key_snapshot, Mapping):
        raise ValueError("metadata lacks sanitized auth snapshot")

    profiles = _token_profile_subset(token_profiles)
    capabilities = _validate_catalog(catalog)
    call_plan = build_call_plan(load_items(str(BANK_DIR)))
    current_cost = t4.estimate_cost(call_plan["classes"], catalog, profiles)
    forecast = current_cost["total_usd"]
    minimum_cap = t4.minimum_ratifiable_cap(forecast)
    remaining = key_snapshot.get("limit_remaining")
    branches = build_budget_branches(call_plan["classes"], catalog, profiles)
    runtime = t4.forecast_runtime(call_plan["totals"]["total"])

    relevant_entries = [catalog[slug] for slug in sorted((*PPP1_SUTS, PPP1_JUDGE))]
    catalog_hash = hashlib.sha256(json.dumps(
        relevant_entries, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()
    auth_retrieved_at = metadata.get("auth_retrieved_at") or retrieved_at
    auth_snapshot = {
        "validity_label": VALIDITY_LABEL,
        "retrieved_at": auth_retrieved_at,
        "usage": key_snapshot.get("usage"),
        "limit": key_snapshot.get("limit"),
        "limit_remaining": remaining,
    }
    manifest = {
        "validity_label": VALIDITY_LABEL,
        "sut_roster": list(PPP1_SUTS),
        "judge": PPP1_JUDGE,
        "runnable_items": call_plan["runnable_items"],
        "normal_items": call_plan["normal_items"],
        "episode_items": call_plan["episode_items"],
        "excluded_dev_set_only_ids": call_plan["excluded_dev_set_only_ids"],
        "items": call_plan["item_manifest"],
        "call_plan": call_plan,
        "logical_calls": call_plan["totals"]["total"],
        "sut_calls": call_plan["totals"]["sut"],
        "judge_calls": call_plan["totals"]["judge"],
        "initial_api_attempts": call_plan["initial_api_attempts"],
        "retry_reserved_api_attempts": call_plan["retry_reserved_api_attempts"],
        "retry_reservation_increment": call_plan["retry_reservation_increment"],
        "retry_policy": call_plan["retry_policy"],
        "token_profiles": profiles,
        "catalog_capabilities": capabilities,
        "catalog_retrieved_at": retrieved_at,
        "auth_retrieved_at": auth_retrieved_at,
        "catalog_hash": catalog_hash,
        "forecast_cost_usd": forecast,
        "minimum_ratifiable_cap_usd": minimum_cap,
        "strategy_cap_usd": STRATEGY_CAP_USD,
        "strategy_cap_feasible": minimum_cap <= STRATEGY_CAP_USD,
        "proposed_nte_cap_usd": (
            STRATEGY_CAP_USD if minimum_cap <= STRATEGY_CAP_USD else None),
        "required_top_up_usd": t4.required_top_up(minimum_cap, remaining),
        "runtime": runtime,
        "budget_branches": branches,
        "paid_inference_authorized": False,
        "paid_inference_performed": False,
        "perturbations_included": False,
        "gate_claims_included": False,
        "runner_coverage": {
            "run_mvp_existing_path": call_plan["normal_items"],
            "episode_run_existing_path": call_plan["episode_items"],
            "total": call_plan["runnable_items"],
            "live_adapter_status": "BLOCKED_SINGLE_JUDGE_STRICT_CAP_SEAM",
        },
        "truncation_stop_branch": {
            "judge": ("registered retry once; post-retry loss is recorded per cell "
                      "and the run continues"),
            "sut": "surface truncation and never silently mark it complete",
            "budget": ("stop before paid execution until Jimmy ratifies an exact "
                       "branch and NTE cap"),
        },
        "pre_run_blockers": [
            "The existing 204-item and 22-EPISODE runners do not expose a shared "
            "single-Gemini strict-pre-call-cap path without bypassing production "
            "panel qualification semantics."
        ],
    }

    report_lines = [
        "# WCF-Bench PPP-1 zero-paid preflight",
        "",
        f"> **{VALIDITY_LABEL}**",
        "",
        f"- SUT roster: {', '.join(PPP1_SUTS)}",
        f"- Sole judge: {PPP1_JUDGE}",
        f"- Calls: {manifest['logical_calls']} total = {manifest['sut_calls']} SUT + "
        f"{manifest['judge_calls']} judge",
        f"- Initial / retry-reserved API attempts: "
        f"{manifest['initial_api_attempts']} / {manifest['retry_reserved_api_attempts']}",
        f"- Conservative forecast: ${forecast:.6f}",
        f"- Minimum 80%-safe cap: ${minimum_cap:.2f}",
        f"- Ratified strategy ceiling: ${STRATEGY_CAP_USD:.2f}",
        f"- Strategy ceiling feasible: {str(manifest['strategy_cap_feasible']).lower()}",
        f"- Current balance: ${float(remaining):.6f}" if remaining is not None
        else "- Current balance: unavailable",
        f"- Required top-up: ${manifest['required_top_up_usd']:.2f}",
        f"- Runtime baseline: {runtime['baseline_minutes']:.1f} minutes",
        f"- Runtime planning band: {runtime['planning_band_minutes'][0]:.1f}–"
        f"{runtime['planning_band_minutes'][1]:.1f} minutes",
        "- Paid inference calls: not authorized and not performed.",
        "",
        "## Completion-cap branches",
        "",
        "| Branch | SUT cap | Judge cap | Executable | Forecast | Minimum cap | Within $5 |",
        "|---|---:|---:|:---:|---:|---:|:---:|",
    ]
    for row in branches:
        report_lines.append(
            f"| {row['branch']} | {row['sut_completion_tokens']} | "
            f"{row['judge_completion_tokens']} | {str(row['executable']).lower()} | "
            f"${row['forecast_cost_usd']:.6f} | "
            f"${row['minimum_ratifiable_cap_usd']:.2f} | "
            f"{str(row['within_strategy_cap']).lower()} |")
    report_lines.extend([
        "",
        "The zero-completion row is a non-executable price floor. No branch is selected by "
        "this preflight.",
    ])

    cost_rows = [dict(row, row_type="request_class", scope="current_2048",
                      validity_label=VALIDITY_LABEL)
                 for row in current_cost["rows"]]
    cost_rows.extend(dict(row, row_type="completion_cap_branch",
                          validity_label=VALIDITY_LABEL) for row in branches)
    return {
        "auth-snapshot.json": auth_snapshot,
        "openrouter-catalog-snapshot.json": {
            "validity_label": VALIDITY_LABEL,
            "retrieved_at": retrieved_at,
            "source_hash": catalog_hash,
            "models": relevant_entries,
        },
        "ppp1-run-manifest.json": manifest,
        "ppp1-cost-plan.csv": cost_rows,
        "ppp1-preflight-report.md": "\n".join(report_lines) + "\n",
    }


def build_retry_correction_payloads(source_dir: os.PathLike) -> Dict[str, Any]:
    """Build a zero-network correction from the immutable original metadata packet."""
    source = Path(source_dir)

    def load_json(name: str) -> Dict[str, Any]:
        with (source / name).open(encoding="utf-8") as handle:
            value = json.load(handle)
        if not isinstance(value, dict):
            raise ValueError(f"original PPP-1 artifact is not an object: {name}")
        return value

    original = load_json("ppp1-run-manifest.json")
    auth = load_json("auth-snapshot.json")
    catalog_snapshot = load_json("openrouter-catalog-snapshot.json")
    for name, value in (
        ("ppp1-run-manifest.json", original),
        ("auth-snapshot.json", auth),
        ("openrouter-catalog-snapshot.json", catalog_snapshot),
    ):
        if value.get("validity_label") != VALIDITY_LABEL:
            raise ValueError(f"original PPP-1 artifact has wrong validity label: {name}")
    catalog = {
        row["id"]: row for row in (catalog_snapshot.get("models") or [])
        if isinstance(row, dict) and row.get("id")
    }
    _validate_catalog(catalog)
    profiles = _token_profile_subset(original.get("token_profiles") or {})
    geometry = build_retry_geometry(load_items(str(BANK_DIR)))
    call_plan = build_call_plan(load_items(str(BANK_DIR)))
    logical_cost = t4.estimate_cost(call_plan["classes"], catalog, profiles)

    per_sut_maximum = geometry["per_sut_judge_attempts"]["maximum"]
    maximum_classes = []
    for sut in PPP1_SUTS:
        maximum_classes.extend([
            {
                "phase": "maximum_retry_reserved", "role": "sut", "model": sut,
                "sut_context": sut, "request_class": "base_sut",
                "attempt_class": "normal_sut", "count": 204,
            },
            {
                "phase": "maximum_retry_reserved", "role": "sut", "model": sut,
                "sut_context": sut, "request_class": "base_sut",
                "attempt_class": "episode_sut", "count": 44,
            },
            {
                "phase": "maximum_retry_reserved", "role": "judge", "model": PPP1_JUDGE,
                "sut_context": sut, "request_class": "base_judge",
                "attempt_class": "open_judge", "count": per_sut_maximum["open"],
            },
            {
                "phase": "maximum_retry_reserved", "role": "judge", "model": PPP1_JUDGE,
                "sut_context": sut, "request_class": "base_judge",
                "attempt_class": "contested_judge", "count": per_sut_maximum["contested"],
            },
            {
                "phase": "maximum_retry_reserved", "role": "judge", "model": PPP1_JUDGE,
                "sut_context": sut, "request_class": "base_judge",
                "attempt_class": "episode_judge", "count": per_sut_maximum["episode"],
            },
        ])
    maximum_cost = t4.estimate_cost(maximum_classes, catalog, profiles)
    logical_forecast = logical_cost["total_usd"]
    maximum_forecast = maximum_cost["total_usd"]
    logical_cap = t4.minimum_ratifiable_cap(logical_forecast)
    maximum_cap = t4.minimum_ratifiable_cap(maximum_forecast)
    remaining = auth.get("limit_remaining")
    source_display = str(source)
    correction = {
        "validity_label": VALIDITY_LABEL,
        "status": "SUPERSEDING_CORRECTION",
        "source_packet": source_display,
        "network_calls": 0,
        "paid_inference_authorized": False,
        "paid_inference_performed": False,
        "roster": list(PPP1_SUTS),
        "judge": PPP1_JUDGE,
        "runnable_items": 226,
        "normal_items": 204,
        "episode_items": 22,
        "retry_geometry": geometry,
        "supersedes": {
            "retry_reserved_api_attempts": {
                "original": original.get("retry_reserved_api_attempts"),
                "corrected": geometry["maximum_api_attempts"]["total"],
            },
            "retry_reservation_increment": {
                "original": original.get("retry_reservation_increment"),
                "corrected": geometry["maximum_retry_increment"],
            },
            "retry_policy": {
                "original": original.get("retry_policy"),
                "corrected": "actual per-seam maximum geometry in retry_geometry",
            },
            "cap_fields": (
                "original logical-only forecast/cap remain valid; this correction adds "
                "the distinct maximum retry-reserved forecast/cap"),
        },
        "logical_forecast_cost_usd": logical_forecast,
        "logical_minimum_ratifiable_cap_usd": logical_cap,
        "maximum_retry_reserved_forecast_cost_usd": maximum_forecast,
        "maximum_retry_reserved_minimum_cap_usd": maximum_cap,
        "strategy_cap_usd": STRATEGY_CAP_USD,
        "strategy_cap_feasible": logical_cap <= STRATEGY_CAP_USD,
        "maximum_retry_reserved_top_up_usd": t4.required_top_up(maximum_cap, remaining),
        "balance": {
            "retrieved_at": auth.get("retrieved_at"),
            "limit_remaining": remaining,
        },
        "catalog": {
            "retrieved_at": catalog_snapshot.get("retrieved_at"),
            "source_hash": catalog_snapshot.get("source_hash"),
        },
    }
    cost_rows = [
        dict(row, scope="logical", validity_label=VALIDITY_LABEL)
        for row in logical_cost["rows"]
    ]
    cost_rows.extend(
        dict(row, scope="maximum_retry_reserved", validity_label=VALIDITY_LABEL)
        for row in maximum_cost["rows"]
    )
    report = (
        "# WCF-Bench PPP-1 retry-geometry correction\n\n"
        f"> **{VALIDITY_LABEL}**\n\n"
        f"Status: **SUPERSEDING CORRECTION** to `{source_display}` for retry and "
        "retry-inclusive cap fields only.\n\n"
        f"- Initial logical/API attempts: {geometry['initial_api_attempts']['total']}.\n"
        f"- Correct maximum API attempts: {geometry['maximum_api_attempts']['total']}.\n"
        f"- Maximum retry increment: {geometry['maximum_retry_increment']}.\n"
        f"- Original blanket maximum superseded: "
        f"{original.get('retry_reserved_api_attempts')}.\n"
        f"- Logical forecast / minimum cap: ${logical_forecast:.9f} / ${logical_cap:.2f}.\n"
        f"- Maximum retry-reserved forecast / minimum cap: "
        f"${maximum_forecast:.9f} / ${maximum_cap:.2f}.\n"
        f"- Current persisted balance / maximum-cap top-up: "
        f"${float(remaining or 0):.9f} / "
        f"${correction['maximum_retry_reserved_top_up_usd']:.2f}.\n"
        "- Network calls for this correction: 0. Paid inference: not authorized or performed.\n\n"
        "The original roster, 226-item scope, current prices, logical-call forecast, and "
        "validity label remain unchanged. This packet supersedes only the blanket retry "
        "count and adds the distinct maximum retry-reserved cost/cap.\n"
    )
    return {
        "ppp1-retry-correction.json": correction,
        "ppp1-retry-cost-plan.csv": cost_rows,
        "ppp1-retry-correction-report.md": report,
    }


def build_branch_addendum_payloads(
    source_dir: os.PathLike, correction_dir: os.PathLike,
) -> Dict[str, Any]:
    """Qualify every logical branch and add its current-scorer retry envelope."""
    source = Path(source_dir)
    correction_path = Path(correction_dir) / "ppp1-retry-correction.json"
    with (source / "ppp1-run-manifest.json").open(encoding="utf-8") as handle:
        original = json.load(handle)
    with (source / "auth-snapshot.json").open(encoding="utf-8") as handle:
        auth = json.load(handle)
    with (source / "openrouter-catalog-snapshot.json").open(encoding="utf-8") as handle:
        catalog_snapshot = json.load(handle)
    with correction_path.open(encoding="utf-8") as handle:
        correction = json.load(handle)
    if any(value.get("validity_label") != VALIDITY_LABEL for value in (
            original, auth, catalog_snapshot, correction)):
        raise ValueError("PPP-1 branch addendum source label mismatch")
    if correction.get("network_calls") != 0:
        raise ValueError("PPP-1 retry correction is not zero-network")
    geometry = correction.get("retry_geometry") or {}
    if (geometry.get("maximum_api_attempts") or {}).get("total") != 3624:
        raise ValueError("PPP-1 retry correction lacks the reviewed 3624 envelope")
    catalog = {
        row["id"]: row for row in (catalog_snapshot.get("models") or [])
        if isinstance(row, dict) and row.get("id")
    }
    _validate_catalog(catalog)
    profiles = _token_profile_subset(original.get("token_profiles") or {})
    logical_classes = (original.get("call_plan") or {}).get("classes")
    if not isinstance(logical_classes, list):
        raise ValueError("PPP-1 original manifest lacks call classes")

    per_sut_maximum = geometry["per_sut_judge_attempts"]["maximum"]
    maximum_classes = []
    for sut in PPP1_SUTS:
        maximum_classes.extend([
            {"phase": "maximum_retry_envelope", "role": "sut", "model": sut,
             "sut_context": sut, "request_class": "base_sut",
             "attempt_class": "normal_sut", "count": 204},
            {"phase": "maximum_retry_envelope", "role": "sut", "model": sut,
             "sut_context": sut, "request_class": "base_sut",
             "attempt_class": "episode_sut", "count": 44},
            {"phase": "maximum_retry_envelope", "role": "judge", "model": PPP1_JUDGE,
             "sut_context": sut, "request_class": "base_judge",
             "attempt_class": "open_judge", "count": per_sut_maximum["open"]},
            {"phase": "maximum_retry_envelope", "role": "judge", "model": PPP1_JUDGE,
             "sut_context": sut, "request_class": "base_judge",
             "attempt_class": "contested_judge", "count": per_sut_maximum["contested"]},
            {"phase": "maximum_retry_envelope", "role": "judge", "model": PPP1_JUDGE,
             "sut_context": sut, "request_class": "base_judge",
             "attempt_class": "episode_judge", "count": per_sut_maximum["episode"]},
        ])
    remaining = auth.get("limit_remaining")
    branches = []
    cost_rows = []
    for judge_tokens in BRANCH_JUDGE_COMPLETION_TOKENS:
        branch_profiles = copy.deepcopy(profiles)
        branch_profiles["base_judge"]["completion_tokens"] = judge_tokens
        executable = judge_tokens > 0
        if not executable:
            branch_profiles["base_sut"]["completion_tokens"] = 0
        logical_cost = t4.estimate_cost(logical_classes, catalog, branch_profiles)
        maximum_cost = t4.estimate_cost(maximum_classes, catalog, branch_profiles)
        logical_forecast = logical_cost["total_usd"]
        maximum_forecast = maximum_cost["total_usd"]
        logical_cap = t4.minimum_ratifiable_cap(logical_forecast)
        maximum_cap = t4.minimum_ratifiable_cap(maximum_forecast)
        row = {
            "branch": (f"judge_max_tokens_{judge_tokens}" if executable
                       else "zero_completion_price_floor"),
            "sut_completion_tokens": branch_profiles["base_sut"]["completion_tokens"],
            "judge_completion_tokens": judge_tokens,
            "executable": executable,
            "logical_forecast_classification": "LOGICAL-CALL-ONLY",
            "logical_forecast_retry_inclusive": False,
            "logical_forecast_is_live_nte": False,
            "live_nte_condition": (
                "NOT A LIVE NTE unless retries are disabled; otherwise runtime must "
                "enforce a separately ratified strict cap"),
            "logical_forecast_usd": logical_forecast,
            "logical_minimum_cap_usd": logical_cap,
            "maximum_retry_envelope_attempts": geometry["maximum_api_attempts"]["total"],
            "maximum_retry_envelope_forecast_usd": maximum_forecast,
            "maximum_retry_envelope_minimum_cap_usd": maximum_cap,
            "maximum_retry_envelope_top_up_usd": t4.required_top_up(maximum_cap, remaining),
            "within_strategy_cap_logical": logical_cap <= STRATEGY_CAP_USD,
            "within_strategy_cap_maximum_retry_envelope": maximum_cap <= STRATEGY_CAP_USD,
        }
        branches.append(row)
        cost_rows.extend(
            dict(cost_row, branch=row["branch"], scope="LOGICAL-CALL-ONLY",
                 retry_inclusive=False, live_nte=False, validity_label=VALIDITY_LABEL)
            for cost_row in logical_cost["rows"])
        cost_rows.extend(
            dict(cost_row, branch=row["branch"], scope="MAXIMUM-RETRY-ENVELOPE",
                 retry_inclusive=True, live_nte=False, validity_label=VALIDITY_LABEL)
            for cost_row in maximum_cost["rows"])
    addendum = {
        "validity_label": VALIDITY_LABEL,
        "status": "FINAL BRANCH-INTERPRETATION ADDENDUM",
        "source_packet": str(source),
        "retry_correction_packet": str(correction_dir),
        "network_calls": 0,
        "paid_inference_authorized": False,
        "paid_inference_performed": False,
        "supersedes_or_qualifies": [
            "original completion-cap branch forecast/cap interpretation"],
        "branch_rule": (
            "Every original branch is LOGICAL-CALL-ONLY, NON-RETRY-INCLUSIVE, and "
            "NOT A LIVE NTE unless retries are disabled. With retries enabled, use the "
            "maximum-retry envelope only as a conservative planning bound and enforce "
            "the separately ratified cap strictly at runtime."),
        "initial_api_attempts": geometry["initial_api_attempts"]["total"],
        "maximum_retry_envelope_attempts": geometry["maximum_api_attempts"]["total"],
        "balance": {"retrieved_at": auth.get("retrieved_at"),
                    "limit_remaining": remaining},
        "branches": branches,
    }
    report_lines = [
        "# WCF-Bench PPP-1 completion-cap branch addendum", "",
        f"> **{VALIDITY_LABEL}**", "",
        "Status: **FINAL BRANCH-INTERPRETATION ADDENDUM**", "",
        "Every original completion-cap forecast is **LOGICAL-CALL-ONLY · "
        "NON-RETRY-INCLUSIVE · NOT A LIVE NTE unless retries are disabled**. With "
        "retries enabled, a separately ratified cap must be enforced strictly at runtime.",
        "", "| Branch | Executable | Logical forecast / cap | Maximum-retry envelope / cap | Top-up |",
        "|---|:---:|---:|---:|---:|",
    ]
    for row in branches:
        report_lines.append(
            f"| {row['branch']} | {str(row['executable']).lower()} | "
            f"${row['logical_forecast_usd']:.9f} / ${row['logical_minimum_cap_usd']:.2f} | "
            f"${row['maximum_retry_envelope_forecast_usd']:.9f} / "
            f"${row['maximum_retry_envelope_minimum_cap_usd']:.2f} | "
            f"${row['maximum_retry_envelope_top_up_usd']:.2f} |")
    report_lines.extend([
        "", "The zero-completion row remains nonexecutable. No branch or paid run is selected.",
        "This addendum made zero network or inference calls.",
    ])
    return {
        "ppp1-branch-addendum.json": addendum,
        "ppp1-branch-cost-plan.csv": cost_rows,
        "ppp1-branch-addendum-report.md": "\n".join(report_lines) + "\n",
    }


def render_artifact(filename: str, payload: Any) -> str:
    """Render one canaried artifact with the exact visible validity label."""
    if filename.endswith(".csv"):
        text = t4._csv_text(payload)
    elif filename.endswith(".json"):
        value = dict(payload)
        value["provenance_canary"] = t4.CANARY
        text = json.dumps(
            value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    else:
        text = str(payload).rstrip() + f"\n\nCanary: `{t4.CANARY}`\n"
    if VALIDITY_LABEL not in text:
        raise ValueError(f"PPP-1 artifact lacks validity label: {filename}")
    return text


def write_new_artifacts(
    output_dir: os.PathLike,
    payloads: Mapping[str, Any],
    *,
    forbidden_values: Sequence[str] = (),
) -> list:
    artifact_names = set(payloads)
    if artifact_names not in (
            EXPECTED_ARTIFACTS, CORRECTION_ARTIFACTS, BRANCH_ADDENDUM_ARTIFACTS):
        raise ValueError(
            "PPP-1 artifacts must be exactly an original or correction packet")
    if t4._contains_secret(payloads, tuple(forbidden_values)):
        raise SecretDisclosureError("refusing to write credential material")
    output = Path(output_dir)
    output.mkdir(parents=False, exist_ok=False)
    paths = []
    for filename in sorted(payloads):
        text = render_artifact(filename, payloads[filename])
        path = output / filename
        with path.open("x", encoding="utf-8") as handle:
            handle.write(text)
        paths.append(str(path))
    return paths


def _print_dry_plan() -> None:
    print("WCF-Bench PPP-1 preflight — DRY RUN (zero network calls, zero writes)")
    print("The metadata mode performs two GETs and has no inference endpoint.")


def main(
    argv: Optional[Sequence[str]] = None,
    *,
    metadata_fetch: Callable[..., Any] = fetch_openrouter_metadata,
    artifact_writer: Callable[..., Any] = write_new_artifacts,
) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--metadata-preflight", action="store_true")
    parser.add_argument("--offline-retry-correction", action="store_true")
    parser.add_argument("--offline-branch-addendum", action="store_true")
    parser.add_argument("--output-dir")
    parser.add_argument("--inputs-json")
    parser.add_argument("--source-dir")
    parser.add_argument("--correction-dir")
    args = parser.parse_args(argv)
    if sum(bool(value) for value in (
            args.metadata_preflight, args.offline_retry_correction,
            args.offline_branch_addendum)) > 1:
        parser.error("select only one PPP-1 preflight mode")
    if args.offline_branch_addendum:
        if not args.output_dir:
            parser.error("--offline-branch-addendum requires --output-dir")
        if not args.source_dir:
            parser.error("--offline-branch-addendum requires --source-dir")
        if not args.correction_dir:
            parser.error("--offline-branch-addendum requires --correction-dir")
        payloads = build_branch_addendum_payloads(
            args.source_dir, args.correction_dir)
        artifact_writer(args.output_dir, payloads, forbidden_values=[])
        rows = payloads["ppp1-branch-addendum.json"]["branches"]
        print("Offline PPP-1 branch addendum frozen; zero network or inference calls.")
        for row in rows:
            print(f"{row['branch']}: logical ${row['logical_forecast_usd']:.6f} / "
                  f"envelope ${row['maximum_retry_envelope_forecast_usd']:.6f}")
        return 0
    if args.offline_retry_correction:
        if not args.output_dir:
            parser.error("--offline-retry-correction requires --output-dir")
        if not args.source_dir:
            parser.error("--offline-retry-correction requires --source-dir")
        payloads = build_retry_correction_payloads(args.source_dir)
        artifact_writer(args.output_dir, payloads, forbidden_values=[])
        correction = payloads["ppp1-retry-correction.json"]
        print("Offline PPP-1 retry correction frozen; zero network or inference calls.")
        print(f"attempts: {correction['retry_geometry']['initial_api_attempts']['total']} "
              f"initial / {correction['retry_geometry']['maximum_api_attempts']['total']} maximum")
        print(f"maximum retry-reserved forecast: "
              f"${correction['maximum_retry_reserved_forecast_cost_usd']:.6f}; "
              f"minimum cap ${correction['maximum_retry_reserved_minimum_cap_usd']:.2f}")
        return 0
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
    payloads = build_preflight_payloads(inputs["token_profiles"], metadata)
    artifact_writer(args.output_dir, payloads, forbidden_values=[api_key])
    manifest = payloads["ppp1-run-manifest.json"]
    print("Authorized metadata GETs and PPP-1 artifact freeze complete; no inference call was made.")
    print(f"catalog timestamp: {manifest['catalog_retrieved_at']}; "
          f"limit remaining: {metadata['key_snapshot'].get('limit_remaining')}")
    print(f"PPP-1: {manifest['logical_calls']} calls, "
          f"${manifest['forecast_cost_usd']:.6f}, "
          f"minimum cap ${manifest['minimum_ratifiable_cap_usd']:.2f}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
