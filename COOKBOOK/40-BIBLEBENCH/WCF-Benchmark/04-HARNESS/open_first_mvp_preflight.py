#!/usr/bin/env python3
"""Offline-testable public-catalog preflight for the Open-First MVP pilot."""

from __future__ import annotations

import argparse
import csv
import datetime
import hashlib
import json
import math
from decimal import Decimal, ROUND_CEILING
from pathlib import Path
from typing import Any, Callable, Dict, Mapping, Optional, Sequence, Tuple
from urllib.parse import urljoin

from wcfbench import load_items, scorer_kind
from wcfbench import mvp
from wcfbench import codex_oauth_judge
from wcfbench.promptbuilder import build_examinee_prompt

import t4_preflight as t4


VALIDITY_LABEL = (
    "EXPLORATORY WCF-BENCH OPEN-FIRST MVP · ONE RUN PER SUT · "
    "SINGLE UNQUALIFIED CODEX-OAUTH GPT-5.6 SOL JUDGE · NON-QUOTABLE"
)
SUTS = (
    "minimax/minimax-m3",
    "z-ai/glm-5.2",
    "deepseek/deepseek-v4-pro",
    "qwen/qwen3.7-max",
    "google/gemma-4-31b-it",
    "meta-llama/llama-4-maverick",
)
JUDGE_MODEL = "gpt-5.6-sol"
MODELS_URL = mvp.MODELS_URL
OPENROUTER_ORIGIN = "https://openrouter.ai"
ENDPOINT_URL = OPENROUTER_ORIGIN + "/api/v1/models/{slug}/endpoints"
BANK_DIR = Path(__file__).resolve().parent.parent / "05-BANK-YAML"
PROMPT_CLASSES = ("sut", "judge_open", "judge_contested", "judge_episode")
SUT_MAX_TOKENS = 2048
JUDGE_BATCH_SIZE = 8
SUT_RETRIES_RESERVED_PER_MODEL = 22
SUT_ATTEMPTS_MAX_PER_MODEL = 252
PLANNING_UTILIZATION = 0.8

SUT_REQUEST_COMMON = {
    "temperature": 0,
    "max_tokens": SUT_MAX_TOKENS,
    "tools": False,
    "web": False,
    "substitutions": False,
    "perturbations": False,
    "model_fallbacks": False,
}


class PreflightError(RuntimeError):
    """Public metadata cannot prove the frozen execution contract."""


class PreflightOutputError(RuntimeError):
    """The append-only preflight output directory cannot be created safely."""


def _utc_now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat(
        timespec="seconds").replace("+00:00", "Z")


def _positive_number(value: Any, label: str) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise PreflightError(f"missing or invalid {label}") from exc
    if not math.isfinite(number) or number <= 0:
        raise PreflightError(f"missing or invalid {label}")
    return number


def _item_extra(item: Any) -> Mapping[str, Any]:
    return (item.get("extra", {}) if isinstance(item, Mapping)
            else getattr(item, "extra", {})) or {}


def build_geometry(items: Sequence[Any]) -> Dict[str, Any]:
    """Derive and freeze the pilot's bank, scoring, batching, and retry counts."""
    all_items = list(items)
    diagnostics = [item for item in all_items if _item_extra(item).get("dev_set_only")]
    runnable = [item for item in all_items if item not in diagnostics]
    if (len(all_items), len(runnable), len(diagnostics)) != (230, 226, 4):
        raise PreflightError("bank geometry is not the frozen 230/226/4 split")
    if any(scorer_kind(item) != "open" for item in diagnostics):
        raise PreflightError("all four diagnostic items must remain dev_set_only OPEN")

    by_kind: Dict[str, list] = {}
    for item in runnable:
        by_kind.setdefault(scorer_kind(item), []).append(item)
    counts = {kind: len(values) for kind, values in by_kind.items()}
    expected = {"open": 161, "anchor": 23, "episode": 22,
                "ordinal": 16, "contested": 4}
    if counts != expected:
        raise PreflightError(f"runnable route geometry drifted: {counts}")
    route_decisions = {
        route: sum(t4._per_judge_call_weight(item) for item in by_kind[route])
        for route in ("open", "contested", "episode")
    }
    if route_decisions != {"open": 310, "contested": 16, "episode": 22}:
        raise PreflightError(f"judge-decision geometry drifted: {route_decisions}")
    tasks = sum(
        math.ceil(count / JUDGE_BATCH_SIZE) for count in route_decisions.values())
    if tasks != 44:
        raise PreflightError(f"same-route judge batching drifted: {tasks}")
    scalar = len(runnable) - len(by_kind["contested"])
    return {
        "bank_items": 230,
        "runnable_scorable_items": 226,
        "diagnostic_items": 4,
        "sut_cells": 230 * len(SUTS),
        "scorable_sut_cells": 226 * len(SUTS),
        "diagnostic_sut_cells": 4 * len(SUTS),
        "scalar_eligible_per_sut": scalar,
        "scalar_eligible_total": scalar * len(SUTS),
        "contested_per_sut": 4,
        "contested_total": 4 * len(SUTS),
        "logical_judge_decisions_per_sut": sum(route_decisions.values()),
        "logical_judge_decisions_total": sum(route_decisions.values()) * len(SUTS),
        "judge_batch_size": JUDGE_BATCH_SIZE,
        "judge_tasks_per_sut": tasks,
        "judge_tasks_total": tasks * len(SUTS),
        "judge_route_decisions_per_sut": route_decisions,
        "sut_attempts_initial": 230 * len(SUTS),
        "sut_retries_reserved_per_model": SUT_RETRIES_RESERVED_PER_MODEL,
        "sut_attempts_max_per_model": SUT_ATTEMPTS_MAX_PER_MODEL,
        "sut_attempts_max_total": SUT_ATTEMPTS_MAX_PER_MODEL * len(SUTS),
    }


def derive_sut_prompt_ceiling(items: Sequence[Any]) -> Dict[str, Any]:
    """Measure the exact frozen-bank user and transport message byte ceilings."""
    user_rows = []
    transport_rows = []
    for item in items:
        if scorer_kind(item) == "episode":
            user = item.stem
            transport_bytes = len(user.encode("utf-8"))
        else:
            prompt = build_examinee_prompt(item)
            user = prompt.user
            # Chat-completions transports these as distinct messages; no separator bytes.
            transport_bytes = len(prompt.system.encode("utf-8")) + len(
                prompt.user.encode("utf-8"))
        user_rows.append((len(user.encode("utf-8")), item.id))
        transport_rows.append((transport_bytes, item.id))
    if len(user_rows) != 230:
        raise PreflightError("SUT prompt derivation requires all 230 frozen bank items")
    max_user, max_user_id = max(user_rows)
    max_transport, max_transport_id = max(transport_rows)
    if (max_user, max_transport, max_user_id, max_transport_id) != (
            1939, 2221, "MEND-C1-W301", "MEND-C1-W301"):
        raise PreflightError("frozen-bank rendered SUT prompt ceiling drifted")
    return {
        "status": "MEASURED_OFFLINE",
        "source": "frozen_bank_rendered_prompts",
        "max_rendered_user_bytes": max_user,
        "max_rendered_transport_bytes": max_transport,
        "max_user_item_id": max_user_id,
        "max_transport_item_id": max_transport_id,
        "prompt_tokens": max_transport,
        "completion_tokens": SUT_MAX_TOKENS,
    }


def build_schedule(items: Sequence[Any]) -> Dict[str, Any]:
    """Freeze exact item-ID partitions used by generation, judging, and aggregation."""
    records = list(items)
    ids = [item.id for item in records]
    if len(records) != 230 or len(set(ids)) != 230:
        raise PreflightError("schedule requires 230 unique frozen bank item IDs")
    dev = sorted(item.id for item in records if _item_extra(item).get("dev_set_only"))
    runnable = sorted(item.id for item in records if item.id not in set(dev))
    contested = sorted(
        item.id for item in records
        if item.id in set(runnable) and scorer_kind(item) == "contested")
    scalar = sorted(item_id for item_id in runnable if item_id not in set(contested))
    judge_routes = {
        route: sorted(
            item.id for item in records
            if item.id in set(runnable) and scorer_kind(item) == route)
        for route in ("open", "contested", "episode")
    }
    if (len(runnable), len(dev), len(scalar), len(contested)) != (226, 4, 222, 4):
        raise PreflightError("frozen schedule partition counts drifted")
    return {
        "all_item_ids": sorted(ids),
        "runnable_item_ids": runnable,
        "dev_set_only_item_ids": dev,
        "scalar_eligible_item_ids": scalar,
        "contested_item_ids": contested,
        "judge_route_item_ids": judge_routes,
    }


def _endpoint_rows(payload: Any) -> list:
    if isinstance(payload, Mapping):
        value = payload.get("data", payload)
        if isinstance(value, Mapping):
            value = value.get("endpoints")
    else:
        value = payload
    return [dict(row) for row in value or () if isinstance(row, Mapping)]


def fetch_public_catalog(
    *, opener: Optional[Callable[[str, Optional[str]], Dict[str, Any]]] = None,
) -> Tuple[Dict[str, Dict[str, Any]], Dict[str, list]]:
    """Fetch only public model/endpoint metadata; never call the auth endpoint."""
    get = opener or mvp._http_get_json
    payload = get(MODELS_URL, None)
    catalog = {
        row["id"]: dict(row) for row in (payload.get("data") or [])
        if isinstance(row, Mapping) and row.get("id")
    }
    endpoints = {}
    for slug in SUTS:
        details = ((catalog.get(slug, {}).get("links") or {}).get("details")
                   or ENDPOINT_URL.format(slug=slug))
        endpoints[slug] = _endpoint_rows(get(urljoin(OPENROUTER_ORIGIN, details), None))
    return catalog, endpoints


def _validate_prompt_ceilings(value: Mapping[str, Mapping[str, Any]]) -> Dict[str, Any]:
    if set(value) != set(PROMPT_CLASSES):
        raise PreflightError("rendered prompt ceilings must cover every route exactly")
    output: Dict[str, Any] = {}
    for name in PROMPT_CLASSES:
        row = dict(value[name])
        try:
            rendered = int(row["max_rendered_prompt_bytes"])
            prompt_tokens = int(row["prompt_tokens"])
            completion = int(row["completion_tokens"])
        except (KeyError, TypeError, ValueError) as exc:
            raise PreflightError(f"invalid rendered prompt ceiling for {name}") from exc
        if (rendered <= 0 or prompt_tokens != rendered or completion < 0
                or row.get("source") != "offline_rendered_prompt_ceiling"):
            raise PreflightError(f"invalid rendered prompt ceiling for {name}")
        output[name] = row
    sut = output["sut"]
    if (sut.get("max_rendered_user_bytes") != 1939
            or sut.get("max_rendered_transport_bytes") != 2221
            or sut["max_rendered_prompt_bytes"] != 2221
            or sut["completion_tokens"] != SUT_MAX_TOKENS):
        raise PreflightError("SUT rendered prompt ceiling is not the frozen 1939/2221 split")
    return output


def _reasoning_parameters(entry: Mapping[str, Any], slug: str) -> Dict[str, Any]:
    reasoning = entry.get("reasoning")
    if reasoning is None:
        if "reasoning" in (entry.get("supported_parameters") or []):
            raise PreflightError(f"reasoning capability is unknown: {slug}")
        return {}
    if not isinstance(reasoning, Mapping):
        raise PreflightError(f"reasoning capability is malformed: {slug}")
    if reasoning.get("mandatory") is not False:
        raise PreflightError(f"reasoning mandatory capability is true or unknown: {slug}")
    return {"reasoning": {"enabled": False}}


def _price_pair(entry: Mapping[str, Any], label: str) -> Tuple[float, float]:
    pricing = entry.get("pricing")
    if not isinstance(pricing, Mapping):
        raise PreflightError(f"missing {label} pricing")
    return (_positive_number(pricing.get("prompt"), f"{label} prompt pricing"),
            _positive_number(pricing.get("completion"), f"{label} completion pricing"))


def _validate_model(
    slug: str, entry: Mapping[str, Any], endpoints: Sequence[Mapping[str, Any]],
) -> Dict[str, Any]:
    architecture = entry.get("architecture")
    supported = entry.get("supported_parameters")
    if (not isinstance(architecture, Mapping)
            or "text" not in (architecture.get("input_modalities") or [])
            or "text" not in (architecture.get("output_modalities") or [])
            or not isinstance(supported, list)):
        raise PreflightError(f"missing text capabilities: {slug}")
    required = {"temperature", "max_tokens"}
    if not required <= set(supported):
        raise PreflightError(f"missing required parameter capability: {slug}")
    context = _positive_number(entry.get("context_length"), f"context for {slug}")
    top_provider = entry.get("top_provider")
    if not isinstance(top_provider, Mapping):
        raise PreflightError(f"missing top-provider context for {slug}")
    provider_context = _positive_number(
        top_provider.get("context_length"), f"top-provider context for {slug}")
    completion_limit = _positive_number(
        top_provider.get("max_completion_tokens"), f"completion capability for {slug}")
    if min(context, provider_context) < 2221 + SUT_MAX_TOKENS or completion_limit < SUT_MAX_TOKENS:
        raise PreflightError(f"insufficient context/completion capability: {slug}")
    prompt_price, completion_price = _price_pair(entry, f"catalog {slug}")
    reasoning_params = _reasoning_parameters(entry, slug)
    if reasoning_params and "reasoning" not in supported:
        raise PreflightError(f"missing required reasoning parameter capability: {slug}")

    eligible = []
    price_blocked = False
    for endpoint in endpoints:
        endpoint_supported = endpoint.get("supported_parameters")
        if not isinstance(endpoint_supported, list):
            continue
        endpoint_required = set(required)
        if reasoning_params:
            endpoint_required.add("reasoning")
        if not endpoint_required <= set(endpoint_supported):
            continue
        if ("data_collection" in endpoint
                and endpoint.get("data_collection") not in {False, "deny", "none"}):
            continue
        endpoint_prompt, endpoint_completion = _price_pair(
            endpoint, f"endpoint {slug}")
        if (endpoint_prompt > prompt_price or endpoint_completion > completion_price):
            price_blocked = True
            continue
        name = endpoint.get("provider_name") or endpoint.get("name") or endpoint.get("provider")
        if name:
            eligible.append(str(name))
    if not eligible:
        if price_blocked:
            raise PreflightError(f"no eligible endpoint within frozen price ceiling: {slug}")
        raise PreflightError(f"no eligible data-policy endpoint: {slug}")

    request_parameters = dict(SUT_REQUEST_COMMON)
    request_parameters.update(reasoning_params)
    return {
        "slug": slug,
        "context_length": int(context),
        "top_provider_context_length": int(provider_context),
        "max_completion_tokens": int(completion_limit),
        "supported_parameters": sorted(set(supported)),
        "reasoning": dict(entry.get("reasoning") or {}),
        "prices": {"prompt": prompt_price, "completion": completion_price},
        "eligible_data_policy_endpoints": sorted(set(eligible)),
        "request_parameters": request_parameters,
        "provider_policy": {
            "sort": "price",
            "require_parameters": True,
            "data_collection": "deny",
            # OpenRouter provider routing expresses max_price in USD / 1M tokens.
            "max_price": {
                "prompt": prompt_price * 1_000_000,
                "completion": completion_price * 1_000_000,
            },
        },
    }


def _ceil_cents(value: float) -> float:
    return float(Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_CEILING))


def build_cost_plan(
    catalog: Mapping[str, Mapping[str, Any]], sut_prompt_ceiling: Mapping[str, Any],
) -> Dict[str, Any]:
    """Price the 230-call base and 252-attempt envelope for each exact SUT."""
    prompt_tokens = int(sut_prompt_ceiling["prompt_tokens"])
    rows = []
    for slug in SUTS:
        if slug not in catalog:
            raise PreflightError(f"missing exact catalog slug for cost plan: {slug}")
        prompt_price, completion_price = _price_pair(catalog[slug], f"catalog {slug}")
        per_call = (prompt_tokens * prompt_price
                    + SUT_MAX_TOKENS * completion_price)
        rows.append({
            "slug": slug,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": SUT_MAX_TOKENS,
            "prompt_price_per_token_usd": prompt_price,
            "completion_price_per_token_usd": completion_price,
            "per_call_usd": per_call,
            "no_retry_calls": 230,
            "no_retry_230_calls_usd": per_call * 230,
            "attempt_envelope_calls": SUT_ATTEMPTS_MAX_PER_MODEL,
            "attempt_envelope_252_calls_usd": per_call * SUT_ATTEMPTS_MAX_PER_MODEL,
        })
    no_retry = sum(row["no_retry_230_calls_usd"] for row in rows)
    envelope = sum(row["attempt_envelope_252_calls_usd"] for row in rows)
    return {
        "validity_label": VALIDITY_LABEL,
        "rows": rows,
        "totals": {
            "no_retry_230_calls_usd": no_retry,
            "attempt_envelope_252_calls_usd": envelope,
            "proposed_cap_usd": _ceil_cents(envelope / PLANNING_UTILIZATION),
        },
        "auth_balance": {
            "status": "NOT_CHECKED_CREDENTIAL_ACCESS_UNAUTHORIZED",
            "balance_usd": None,
            "top_up_usd": None,
        },
    }


def build_manifest(
    catalog: Mapping[str, Mapping[str, Any]],
    endpoints: Mapping[str, Sequence[Mapping[str, Any]]],
    rendered_prompt_ceilings: Mapping[str, Mapping[str, Any]],
    *,
    catalog_retrieved_at: str,
) -> Dict[str, Any]:
    """Build the deterministic zero-credential manifest input, or fail closed."""
    if not catalog_retrieved_at:
        raise PreflightError("catalog retrieval timestamp is required")
    for slug in SUTS:
        if slug not in catalog:
            raise PreflightError(f"missing exact catalog slug: {slug}")
        if slug not in endpoints:
            raise PreflightError(f"missing endpoint metadata: {slug}")
    prompt_ceilings = _validate_prompt_ceilings(rendered_prompt_ceilings)
    models = [_validate_model(slug, catalog[slug], endpoints[slug]) for slug in SUTS]
    geometry = build_geometry(load_items(str(BANK_DIR)))
    catalog_input = {"models": models, "endpoints": {
        slug: [dict(row) for row in endpoints[slug]] for slug in SUTS}}
    catalog_hash = hashlib.sha256(json.dumps(
        catalog_input, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
    ).encode("utf-8")).hexdigest()
    prompt_tokens = int(prompt_ceilings["sut"]["prompt_tokens"])
    envelope = SUT_ATTEMPTS_MAX_PER_MODEL * sum(
        prompt_tokens * row["prices"]["prompt"]
        + SUT_MAX_TOKENS * row["prices"]["completion"]
        for row in models
    )
    return {
        "schema_version": 1,
        "validity_label": VALIDITY_LABEL,
        "catalog_retrieved_at": catalog_retrieved_at,
        "catalog_hash": catalog_hash,
        "exact_sut_slugs": list(SUTS),
        "models": models,
        "sut_request_common": dict(SUT_REQUEST_COMMON),
        "rendered_prompt_ceilings": prompt_ceilings,
        "geometry": geometry,
        "schedule": build_schedule(load_items(str(BANK_DIR))),
        "retry_policy": {
            "sut_reserved_retries_per_model": SUT_RETRIES_RESERVED_PER_MODEL,
            "sut_max_attempts_per_model": SUT_ATTEMPTS_MAX_PER_MODEL,
            "judge_record_retries": 2,
            "errors_are_missing_never_zero": True,
        },
        "concurrency": {"sut_shards": 3, "within_shard": 1, "judge": 1},
        "judge": {
            "model": JUDGE_MODEL,
            "reasoning_effort": "medium",
            "qualified": False,
            "batch_size": JUDGE_BATCH_SIZE,
            "same_sut_and_route_per_batch": True,
        },
        "planning_cost": {
            "sut_attempt_envelope_usd": envelope,
            "utilization_fraction": PLANNING_UTILIZATION,
            "proposed_cap_usd": _ceil_cents(envelope / PLANNING_UTILIZATION),
        },
        "auth_balance": {
            "status": "NOT_CHECKED_CREDENTIAL_ACCESS_UNAUTHORIZED",
            "balance_usd": None,
            "top_up_usd": None,
        },
        "paid_inference_authorized": False,
        "paid_inference_performed": False,
    }


def _manifest_sut_ceiling(measured: Mapping[str, Any]) -> Dict[str, Any]:
    row = dict(measured)
    row.update({
        "source": "offline_rendered_prompt_ceiling",
        "max_rendered_prompt_bytes": measured["max_rendered_transport_bytes"],
    })
    return row


def derive_judge_prompt_ceilings(
    sut_prompt_ceiling: Mapping[str, Any],
) -> Dict[str, Dict[str, Any]]:
    """Render a conservative offline envelope before any SUT response exists."""
    try:
        sut_transport_bytes = int(sut_prompt_ceiling["max_rendered_transport_bytes"])
        response_tokens = int(sut_prompt_ceiling["completion_tokens"])
    except (KeyError, TypeError, ValueError) as exc:
        raise PreflightError("judge ceiling derivation requires the frozen SUT ceiling") from exc
    if sut_transport_bytes != 2221 or response_tokens != SUT_MAX_TOKENS:
        raise PreflightError("judge ceiling derivation cannot relax frozen SUT geometry")

    if (response_tokens != codex_oauth_judge.MAX_SUT_RESPONSE_TOKENS
            or JUDGE_BATCH_SIZE != codex_oauth_judge.MAX_BATCH_SIZE):
        raise PreflightError("judge ceiling derivation cannot relax frozen batch/token geometry")
    rendered = codex_oauth_judge.judge_prompt_byte_ceiling()
    ceilings = {}
    for route in ("judge_open", "judge_contested", "judge_episode"):
        ceilings[route] = {
            "status": "DERIVED_OFFLINE_CONSERVATIVE",
            "route": route,
            "source": "offline_rendered_prompt_ceiling",
            "max_rendered_prompt_bytes": rendered,
            "prompt_tokens": rendered,
            "completion_tokens": 0,
            "batch_size": JUDGE_BATCH_SIZE,
            "max_sut_response_tokens_per_record": response_tokens,
            "max_sut_response_bytes": codex_oauth_judge.MAX_SUT_RESPONSE_BYTES,
            "max_record_id_bytes": codex_oauth_judge.MAX_RECORD_ID_BYTES,
            "max_criterion_id_bytes": codex_oauth_judge.MAX_CRITERION_ID_BYTES,
            "max_judge_input_serialized_bytes": (
                codex_oauth_judge.MAX_JUDGE_INPUT_SERIALIZED_BYTES),
        }
    return ceilings


def _write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(
        value, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def _write_cost_csv(path: Path, cost_plan: Mapping[str, Any]) -> None:
    fieldnames = [
        "slug", "prompt_tokens", "completion_tokens",
        "prompt_price_per_token_usd", "completion_price_per_token_usd",
        "per_call_usd", "no_retry_calls", "no_retry_230_calls_usd",
        "attempt_envelope_calls", "attempt_envelope_252_calls_usd",
    ]
    with path.open("x", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        rows = cost_plan.get("rows") or []
        writer.writerows(rows)
        totals = cost_plan.get("totals") or {}
        writer.writerow({
            "slug": "TOTAL",
            "no_retry_calls": sum(
                int(row["no_retry_calls"]) for row in rows),
            "no_retry_230_calls_usd": totals.get(
                "no_retry_230_calls_usd"),
            "attempt_envelope_calls": sum(
                int(row["attempt_envelope_calls"]) for row in rows),
            "attempt_envelope_252_calls_usd": totals.get(
                "attempt_envelope_252_calls_usd"),
        })


def run_public_preflight(
    output_dir: Any,
    *,
    metadata_fetch: Callable[[], Tuple[Dict[str, Any], Dict[str, Any]]] = fetch_public_catalog,
    now: Callable[[], str],
) -> Dict[str, Any]:
    """Fetch only public metadata and freeze an executable or failed packet."""
    output = Path(output_dir)
    try:
        output.mkdir(parents=False, exist_ok=False)
    except FileExistsError as exc:
        raise PreflightOutputError(f"output directory already exists: {output}") from exc
    except OSError as exc:
        raise PreflightOutputError(f"cannot create output directory: {output}") from exc

    retrieved_at = now()
    catalog: Dict[str, Any] = {}
    endpoints: Dict[str, Any] = {}
    blockers = []
    try:
        catalog, endpoints = metadata_fetch()
    except Exception as exc:
        blockers.append(f"public metadata fetch failed: {type(exc).__name__}: {exc}")

    selected_catalog = {slug: catalog[slug] for slug in SUTS if slug in catalog}
    selected_endpoints = {slug: endpoints.get(slug, []) for slug in SUTS}
    snapshot_input = {"models": selected_catalog, "endpoints": selected_endpoints}
    snapshot_hash = hashlib.sha256(json.dumps(
        snapshot_input, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False).encode("utf-8")).hexdigest()
    canonical_slugs = {
        slug: selected_catalog[slug].get("canonical_slug")
        for slug in SUTS if slug in selected_catalog
    }
    _write_json(output / "public-catalog-snapshot.json", {
        "retrieved_at": retrieved_at, "source_hash": snapshot_hash,
        "canonical_slugs": canonical_slugs, "models": selected_catalog})
    _write_json(output / "public-endpoint-snapshots.json", {
        "retrieved_at": retrieved_at, "source_hash": snapshot_hash,
        "endpoints": selected_endpoints})

    measured_sut = derive_sut_prompt_ceiling(load_items(str(BANK_DIR)))
    prompt_record = {"sut": _manifest_sut_ceiling(measured_sut)}
    prompt_record.update(derive_judge_prompt_ceilings(measured_sut))
    _write_json(output / "prompt-ceilings.json", prompt_record)

    try:
        cost_plan = build_cost_plan(catalog, measured_sut)
    except Exception as exc:
        blockers.append(f"cost plan unavailable: {type(exc).__name__}: {exc}")
        cost_plan = {
            "validity_label": VALIDITY_LABEL, "rows": [], "totals": {},
            "auth_balance": {
                "status": "NOT_CHECKED_CREDENTIAL_ACCESS_UNAUTHORIZED",
                "balance_usd": None, "top_up_usd": None,
            },
        }
    _write_json(output / "cost-plan.json", cost_plan)
    _write_cost_csv(output / "cost-plan.csv", cost_plan)

    for slug in SUTS:
        if slug not in catalog:
            blockers.append(f"missing exact catalog slug: {slug}")
            continue
        try:
            _validate_model(slug, catalog[slug], endpoints.get(slug, []))
        except PreflightError as exc:
            blockers.append(str(exc))
    manifest = None
    if not blockers:
        try:
            manifest = build_manifest(
                catalog, endpoints, prompt_record,
                catalog_retrieved_at=retrieved_at)
            manifest["public_snapshot_hash"] = snapshot_hash
            manifest["canonical_slugs"] = canonical_slugs
        except PreflightError as exc:
            blockers.append(str(exc))

    auth_balance = cost_plan["auth_balance"]
    if blockers:
        failure = {
            "schema_version": 1,
            "validity_label": VALIDITY_LABEL,
            "status": "FAILED/NON-EXECUTABLE",
            "retrieved_at": retrieved_at,
            "blockers": blockers,
            "schedule": build_schedule(load_items(str(BANK_DIR))),
            "catalog_hash": snapshot_hash,
            "canonical_slugs": canonical_slugs,
            "auth_balance": auth_balance,
            "paid_inference_authorized": False,
            "paid_inference_performed": False,
        }
        _write_json(output / "failed-preflight.json", failure)
        status = failure["status"]
    else:
        _write_json(output / "open-first-mvp-manifest.json", manifest)
        status = "EXECUTABLE-MANIFEST-INPUT"
    report = "\n".join([
        "# WCF-Bench Open-First MVP public preflight", "",
        f"> **{VALIDITY_LABEL}**", "", f"Status: **{status}**",
        "- Auth balance: **NOT_CHECKED_CREDENTIAL_ACCESS_UNAUTHORIZED**",
        f"- 230-call no-retry total: {cost_plan.get('totals', {}).get('no_retry_230_calls_usd')}",
        f"- 252-attempt envelope total: {cost_plan.get('totals', {}).get('attempt_envelope_252_calls_usd')}",
        f"- Proposed cap: {cost_plan.get('totals', {}).get('proposed_cap_usd')}",
        f"- Public catalog/endpoint snapshot hash: {snapshot_hash}",
        "- Canonical slugs: " + json.dumps(canonical_slugs, sort_keys=True),
        "- Blockers: " + (" | ".join(blockers) if blockers else "none"), "",
    ])
    (output / "preflight-report.md").write_text(report, encoding="utf-8")
    return {"status": status, "output_dir": str(output), "blockers": blockers}


def main(
    argv: Optional[Sequence[str]] = None,
    *,
    metadata_fetch: Callable[[], Tuple[Dict[str, Any], Dict[str, Any]]] = fetch_public_catalog,
    now: Optional[Callable[[], str]] = None,
) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--public-preflight", action="store_true")
    parser.add_argument("--output-dir")
    args = parser.parse_args(argv)
    if args.public_preflight:
        if not args.output_dir:
            parser.error("--public-preflight requires --output-dir")
        clock = now or _utc_now
        try:
            result = run_public_preflight(
                args.output_dir, metadata_fetch=metadata_fetch, now=clock)
        except PreflightOutputError as exc:
            print(f"ERROR: {exc}")
            return 2
        print(f"Open-First public preflight: {result['status']} at {result['output_dir']}")
        return 0 if result["status"] == "EXECUTABLE-MANIFEST-INPUT" else 1
    print("WCF-Bench Open-First MVP preflight — DRY RUN (zero network calls)")
    print(VALIDITY_LABEL)
    print("Public catalog refresh remains explicit; auth/balance access is unauthorized.")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
