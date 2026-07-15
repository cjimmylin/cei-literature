#!/usr/bin/env python3
"""Offline-only manifest builder for WCF-Bench Pilot 2.

The module accepts already-fetched public metadata.  It never reads credentials and
has no inference path; a successful packet remains stopped at amount authorization.
"""

from __future__ import annotations

import argparse
import csv
import datetime
import hashlib
import json
import math
from dataclasses import dataclass
from decimal import Decimal, ROUND_CEILING
from pathlib import Path
from typing import Any, Callable, Dict, Mapping, Optional, Sequence, Tuple
from urllib.parse import urljoin

from wcfbench import load_items, scorer_kind, mvp

import open_first_mvp_preflight as pilot1


VALIDITY_LABEL = (
    "EXPLORATORY WCF-BENCH PILOT 2 · FIVE REASONING-ENABLED OPEN-FIRST SUTS · "
    "ONE RUN PER SUT · SINGLE UNQUALIFIED CODEX-OAUTH GPT-5.6 SOL JUDGE · "
    "NON-QUOTABLE"
)
BANK_DIR = pilot1.BANK_DIR
SUT_MAX_TOKENS = 8192
SUT_PROMPT_TOKENS = 2221
JUDGE_MODEL = "gpt-5.6-sol"
JUDGE_REASONING_EFFORT = "medium"
JUDGE_MAX_BATCH_SIZE = 8
JUDGE_MAX_SERIALIZED_BATCH_BYTES = 800_000
JUDGE_MAX_SERIALIZED_RECORD_BYTES = 262_144
SUT_RETRIES_RESERVED_PER_MODEL = 22
SUT_ATTEMPTS_MAX_PER_MODEL = 252
PROPOSED_CAP_USD = 27.03
PLANNING_UTILIZATION = 0.8
MODELS_URL = mvp.MODELS_URL
OPENROUTER_ORIGIN = "https://openrouter.ai"
ENDPOINT_URL = OPENROUTER_ORIGIN + "/api/v1/models/{slug}/endpoints"


@dataclass(frozen=True)
class SutSpec:
    slug: str
    provider: str
    reasoning: Dict[str, Any]
    prompt_price_per_token: float
    completion_price_per_token: float


SUT_SPECS: Tuple[SutSpec, ...] = (
    SutSpec("minimax/minimax-m3", "Minimax", {"enabled": True},
            0.30 / 1_000_000, 1.20 / 1_000_000),
    SutSpec("z-ai/glm-5.2", "StreamLake", {"effort": "high"},
            0.8533 / 1_000_000, 2.6818 / 1_000_000),
    SutSpec("deepseek/deepseek-v4-pro", "DeepSeek", {"effort": "high"},
            0.435 / 1_000_000, 0.87 / 1_000_000),
    SutSpec("qwen/qwen3.7-max", "Alibaba", {"enabled": True},
            1.475 / 1_000_000, 4.425 / 1_000_000),
    SutSpec("google/gemma-4-31b-it", "WandB", {"enabled": True},
            0.12 / 1_000_000, 0.35 / 1_000_000),
)
SUTS = tuple(spec.slug for spec in SUT_SPECS)


class PreflightError(RuntimeError):
    """Public metadata cannot prove the exact Pilot 2 protocol."""


class PreflightOutputError(RuntimeError):
    """The append-only public preflight packet cannot be created."""


def _utc_now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat(
        timespec="seconds").replace("+00:00", "Z")


def _extra(item: Any) -> Mapping[str, Any]:
    return (item.get("extra", {}) if isinstance(item, Mapping)
            else getattr(item, "extra", {})) or {}


def build_geometry(items: Sequence[Any]) -> Dict[str, Any]:
    records = list(items)
    dev = [item for item in records if _extra(item).get("dev_set_only")]
    runnable = [item for item in records if item not in dev]
    if (len(records), len(runnable), len(dev)) != (230, 226, 4):
        raise PreflightError("bank geometry is not the frozen 230/226/4 split")
    routes: Dict[str, list] = {}
    for item in runnable:
        routes.setdefault(scorer_kind(item), []).append(item)
    if {name: len(rows) for name, rows in routes.items()} != {
            "open": 161, "anchor": 23, "episode": 22,
            "ordinal": 16, "contested": 4}:
        raise PreflightError("runnable route geometry drifted")
    return {
        "bank_items": 230,
        "runnable_scorable_items": 226,
        "diagnostic_items": 4,
        "sut_cells": 1150,
        "scorable_sut_cells": 1130,
        "diagnostic_sut_cells": 20,
        "scalar_eligible_per_sut": 222,
        "scalar_eligible_total": 1110,
        "contested_per_sut": 4,
        "contested_total": 20,
        "logical_judge_decisions_per_sut": 348,
        "logical_judge_decisions_total": 1740,
        "expected_judge_tasks": 220,
        "conservative_large_response_tasks": 590,
        "scalar_sufficiency": {"minimum": 200, "denominator": 222},
        "sut_attempts_initial": 1150,
        "sut_retries_reserved_per_model": SUT_RETRIES_RESERVED_PER_MODEL,
        "sut_attempts_max_per_model": SUT_ATTEMPTS_MAX_PER_MODEL,
        "sut_attempts_max_total": SUT_ATTEMPTS_MAX_PER_MODEL * len(SUTS),
    }


def build_schedule(items: Sequence[Any]) -> Dict[str, Any]:
    return pilot1.build_schedule(items)


def derive_prompt_ceiling(items: Sequence[Any]) -> Dict[str, Any]:
    measured = pilot1.derive_sut_prompt_ceiling(items)
    if measured["prompt_tokens"] != SUT_PROMPT_TOKENS:
        raise PreflightError("rendered prompt ceiling drifted")
    measured = dict(measured)
    measured["completion_tokens"] = SUT_MAX_TOKENS
    return measured


def _endpoint_rows(value: Any) -> list:
    if isinstance(value, Mapping):
        value = value.get("data", value)
        if isinstance(value, Mapping):
            value = value.get("endpoints", value)
    return [dict(row) for row in (value or ()) if isinstance(row, Mapping)]


def fetch_public_catalog(
    *, opener: Optional[Callable[[str, Optional[str]], Dict[str, Any]]] = None,
) -> Tuple[Dict[str, Dict[str, Any]], Dict[str, list]]:
    """Fetch only public model and endpoint metadata; never touch auth URLs."""
    get = opener or mvp._http_get_json
    payload = get(MODELS_URL, None)
    catalog = {
        row["id"]: dict(row) for row in (payload.get("data") or ())
        if isinstance(row, Mapping) and row.get("id")
    }
    endpoints = {}
    for slug in SUTS:
        details = ((catalog.get(slug, {}).get("links") or {}).get("details")
                   or ENDPOINT_URL.format(slug=slug))
        endpoints[slug] = _endpoint_rows(
            get(urljoin(OPENROUTER_ORIGIN, details), None))
    return catalog, endpoints


def _price(row: Mapping[str, Any], name: str) -> Tuple[float, float]:
    pricing = row.get("pricing")
    if not isinstance(pricing, Mapping):
        raise PreflightError(f"missing pricing for pinned provider: {name}")
    try:
        pair = float(pricing["prompt"]), float(pricing["completion"])
    except (KeyError, TypeError, ValueError) as exc:
        raise PreflightError(f"invalid pricing for pinned provider: {name}") from exc
    if not all(math.isfinite(value) and value > 0 for value in pair):
        raise PreflightError(f"invalid pricing for pinned provider: {name}")
    return pair


def _validate_model(spec: SutSpec, catalog_row: Any, endpoint_rows: Any) -> Dict[str, Any]:
    if not isinstance(catalog_row, Mapping):
        raise PreflightError(f"missing exact model: {spec.slug}")
    if (not isinstance(catalog_row.get("context_length"), int)
            or catalog_row["context_length"] < SUT_PROMPT_TOKENS + SUT_MAX_TOKENS):
        raise PreflightError(f"insufficient context ceiling: {spec.slug}")
    architecture = catalog_row.get("architecture")
    if (not isinstance(architecture, Mapping)
            or "text" not in (architecture.get("input_modalities") or ())
            or "text" not in (architecture.get("output_modalities") or ())):
        raise PreflightError(f"text capability missing: {spec.slug}")
    top_provider = catalog_row.get("top_provider")
    if (not isinstance(top_provider, Mapping)
            or not isinstance(top_provider.get("context_length"), int)
            or top_provider["context_length"] < SUT_PROMPT_TOKENS + SUT_MAX_TOKENS
            or not isinstance(top_provider.get("max_completion_tokens"), int)
            or top_provider["max_completion_tokens"] < SUT_MAX_TOKENS):
        raise PreflightError(f"top-provider context/completion capability missing: {spec.slug}")
    supported = set(catalog_row.get("supported_parameters") or ())
    if not {"temperature", "max_tokens", "reasoning"} <= supported:
        raise PreflightError(f"reasoning capability missing: {spec.slug}")
    reasoning = catalog_row.get("reasoning")
    if not isinstance(reasoning, Mapping):
        raise PreflightError(f"reasoning capability unknown: {spec.slug}")
    if spec.reasoning.get("effort") == "high" and "high" not in set(
            reasoning.get("supported_efforts") or ()):
        raise PreflightError(f"high effort is unsupported: {spec.slug}")
    candidates = [row for row in _endpoint_rows(endpoint_rows)
                  if row.get("provider_name") == spec.provider]
    if len(candidates) != 1:
        raise PreflightError(f"exact pinned provider is unavailable: {spec.slug}")
    endpoint = candidates[0]
    endpoint_supported = set(endpoint.get("supported_parameters") or ())
    if not {"temperature", "max_tokens", "reasoning"} <= endpoint_supported:
        raise PreflightError(f"pinned provider lacks parameters: {spec.slug}")
    if endpoint.get("data_collection") not in {None, False, "deny", "none"}:
        raise PreflightError(f"pinned provider violates data policy: {spec.slug}")
    if (not isinstance(endpoint.get("context_length"), int)
            or endpoint["context_length"] < SUT_PROMPT_TOKENS + SUT_MAX_TOKENS
            or not isinstance(endpoint.get("max_completion_tokens"), int)
            or endpoint["max_completion_tokens"] < SUT_MAX_TOKENS):
        raise PreflightError(
            f"pinned provider context/completion capability insufficient: {spec.slug}")
    current_prompt, current_completion = _price(endpoint, spec.provider)
    if (current_prompt > spec.prompt_price_per_token
            or current_completion > spec.completion_price_per_token):
        raise PreflightError(f"pinned provider exceeds frozen price: {spec.slug}")
    maximum = (SUT_PROMPT_TOKENS * current_prompt
               + SUT_MAX_TOKENS * current_completion)
    return {
        "slug": spec.slug,
        "canonical_slug": catalog_row.get("canonical_slug"),
        "pinned_provider": spec.provider,
        "request_parameters": {
            "temperature": 0, "max_tokens": SUT_MAX_TOKENS,
            "reasoning": dict(spec.reasoning),
        },
        "provider_policy": {
            "order": [spec.provider],
            "allow_fallbacks": False,
            "require_parameters": True,
            "data_collection": "deny",
            "max_price": {
                "prompt": current_prompt * 1_000_000,
                "completion": current_completion * 1_000_000,
            },
        },
        "prices_per_token": {
            "prompt": current_prompt,
            "completion": current_completion,
        },
        "approved_price_ceiling_per_token": {
            "prompt": spec.prompt_price_per_token,
            "completion": spec.completion_price_per_token,
        },
        "endpoint_context_length": endpoint["context_length"],
        "endpoint_max_completion_tokens": endpoint["max_completion_tokens"],
        "maximum_attempt_cost_usd": maximum,
    }


def _ceil_cents(value: float) -> float:
    return float(Decimal(str(value)).quantize(
        Decimal("0.01"), rounding=ROUND_CEILING))


def build_cost_plan(models: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
    rows = []
    for model in models:
        per_call = float(model["maximum_attempt_cost_usd"])
        rows.append({
            "slug": model["slug"],
            "pinned_provider": model["pinned_provider"],
            "prompt_tokens": SUT_PROMPT_TOKENS,
            "completion_tokens": SUT_MAX_TOKENS,
            "prompt_price_per_token_usd": model["prices_per_token"]["prompt"],
            "completion_price_per_token_usd": model["prices_per_token"]["completion"],
            "per_call_usd": per_call,
            "no_retry_calls": 230,
            "no_retry_230_calls_usd": per_call * 230,
            "attempt_envelope_calls": 252,
            "attempt_envelope_252_calls_usd": per_call * 252,
            "provider_canary_one_attempt_usd": per_call,
            "provider_canary_two_attempt_usd": per_call * 2,
        })
    no_retry = sum(row["no_retry_230_calls_usd"] for row in rows)
    attempts = sum(row["attempt_envelope_252_calls_usd"] for row in rows)
    canary_one = sum(row["provider_canary_one_attempt_usd"] for row in rows)
    canary_two = sum(row["provider_canary_two_attempt_usd"] for row in rows)
    result = {
        "validity_label": VALIDITY_LABEL,
        "rows": rows,
        "totals": {
            "no_retry_230_calls_usd": no_retry,
            "attempt_envelope_252_calls_usd": attempts,
            "provider_canary_one_attempt_usd": canary_one,
            "provider_canary_two_attempt_usd": canary_two,
            "cumulative_attempt_envelope_usd": attempts + canary_two,
            "utilization_fraction": PLANNING_UTILIZATION,
            "proposed_cap_usd": _ceil_cents(
                (attempts + canary_two) / PLANNING_UTILIZATION),
        },
        "auth_balance": {
            "status": "NOT_CHECKED",
            "balance_usd": None,
            "required_balance_usd": None,
            "top_up_usd": None,
        },
    }
    result["auth_balance"]["required_balance_usd"] = (
        result["totals"]["proposed_cap_usd"])
    return result


def build_manifest(
    catalog: Mapping[str, Mapping[str, Any]],
    endpoints: Mapping[str, Sequence[Mapping[str, Any]]],
    *, catalog_retrieved_at: str,
) -> Dict[str, Any]:
    items = load_items(str(BANK_DIR))
    models = [_validate_model(spec, catalog.get(spec.slug), endpoints.get(spec.slug))
              for spec in SUT_SPECS]
    canonical = json.dumps(
        {"catalog": {slug: catalog.get(slug) for slug in SUTS},
         "endpoints": {slug: endpoints.get(slug) for slug in SUTS}},
        sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    cost_plan = build_cost_plan(models)
    return {
        "schema_version": 1,
        "kind": "wcf_bench_pilot2_zero_paid_manifest_input",
        "status": "ZERO-PAID-PREFLIGHT-INPUT",
        "validity_label": VALIDITY_LABEL,
        "catalog_retrieved_at": catalog_retrieved_at,
        "catalog_hash": hashlib.sha256(canonical).hexdigest(),
        "exact_sut_slugs": list(SUTS),
        "models": models,
        "geometry": build_geometry(items),
        "schedule": build_schedule(items),
        "rendered_prompt_ceiling": derive_prompt_ceiling(items),
        "retry_policy": {
            "sut_max_retries_per_cell": 2,
            "sut_reserved_retries_per_model": 22,
            "sut_max_attempts_per_model": 252,
        },
        "concurrency": {"sut_shards": 3, "within_shard": 1, "judge": 1},
        "judge": {
            "model": JUDGE_MODEL,
            "reasoning_effort": JUDGE_REASONING_EFFORT,
            "max_batch_size": JUDGE_MAX_BATCH_SIZE,
            "max_serialized_batch_bytes": JUDGE_MAX_SERIALIZED_BATCH_BYTES,
            "max_serialized_record_bytes": JUDGE_MAX_SERIALIZED_RECORD_BYTES,
            "expected_tasks": 220,
            "conservative_large_response_tasks": 590,
            "max_record_retries": 2,
            "tools": False,
            "web": False,
        },
        "planning_cost": dict(cost_plan["totals"]),
        "call_forecast": {
            "sut_initial": 1150, "sut_attempt_envelope": 1260,
            "provider_canary_initial": 5,
            "provider_canary_attempt_envelope": 10,
            "logical_judge_decisions": 1740,
            "expected_oauth_tasks": 220,
            "conservative_oauth_tasks": 590,
        },
        "runtime_forecast_seconds": {"minimum": 25_200, "maximum": 79_200},
        "auth_balance": dict(cost_plan["auth_balance"]),
        "authorization_gate": {
            "credential_access": False,
            "oauth_canary": False,
            "paid_inference": False,
            "required_next": "AMOUNT_SPECIFIC_OWNER_AUTHORIZATION",
        },
    }


def _prompt_judge_ceilings() -> Dict[str, Any]:
    measured = derive_prompt_ceiling(load_items(str(BANK_DIR)))
    return {
        "sut": measured,
        "judge": {
            "model": JUDGE_MODEL,
            "reasoning_effort": JUDGE_REASONING_EFFORT,
            "max_batch_size": JUDGE_MAX_BATCH_SIZE,
            "max_serialized_batch_bytes": JUDGE_MAX_SERIALIZED_BATCH_BYTES,
            "max_serialized_record_bytes": JUDGE_MAX_SERIALIZED_RECORD_BYTES,
            "expected_tasks": 220,
            "conservative_large_response_tasks": 590,
        },
    }


def _write_json_new(path: Path, value: Any) -> None:
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True, ensure_ascii=False)
        handle.write("\n")


def _write_cost_csv(path: Path, cost_plan: Mapping[str, Any]) -> None:
    fields = [
        "slug", "pinned_provider", "prompt_tokens", "completion_tokens",
        "prompt_price_per_token_usd", "completion_price_per_token_usd",
        "per_call_usd", "no_retry_calls", "no_retry_230_calls_usd",
        "attempt_envelope_calls", "attempt_envelope_252_calls_usd",
        "provider_canary_one_attempt_usd", "provider_canary_two_attempt_usd",
    ]
    with path.open("x", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(cost_plan.get("rows") or ())
        totals = cost_plan.get("totals") or {}
        writer.writerow({
            "slug": "TOTAL",
            "no_retry_calls": 1150,
            "no_retry_230_calls_usd": totals.get("no_retry_230_calls_usd"),
            "attempt_envelope_calls": 1260,
            "attempt_envelope_252_calls_usd": totals.get(
                "attempt_envelope_252_calls_usd"),
            "provider_canary_one_attempt_usd": totals.get(
                "provider_canary_one_attempt_usd"),
            "provider_canary_two_attempt_usd": totals.get(
                "provider_canary_two_attempt_usd"),
        })


def run_public_preflight(
    output_dir: Any, *,
    metadata_fetch: Callable[[], Tuple[Dict[str, Any], Dict[str, Any]]] =
        fetch_public_catalog,
    now: Callable[[], str] = _utc_now,
) -> Dict[str, Any]:
    """Freeze one append-only public-metadata packet; never read auth state."""
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
    _write_json_new(output / "public-catalog-snapshot.json", {
        "retrieved_at": retrieved_at, "source_hash": snapshot_hash,
        "canonical_slugs": canonical_slugs, "models": selected_catalog})
    _write_json_new(output / "public-endpoint-snapshots.json", {
        "retrieved_at": retrieved_at, "source_hash": snapshot_hash,
        "endpoints": selected_endpoints})
    ceilings = _prompt_judge_ceilings()
    _write_json_new(output / "prompt-judge-ceilings.json", ceilings)

    models = []
    for spec in SUT_SPECS:
        try:
            models.append(_validate_model(
                spec, catalog.get(spec.slug), endpoints.get(spec.slug)))
        except PreflightError as exc:
            blockers.append(str(exc))
    cost_plan = build_cost_plan(models) if len(models) == len(SUTS) else {
        "validity_label": VALIDITY_LABEL, "rows": [], "totals": {},
        "auth_balance": {
            "status": "NOT_CHECKED_CREDENTIAL_ACCESS_UNAUTHORIZED",
            "balance_usd": None, "required_balance_usd": None, "top_up_usd": None,
        },
    }
    if len(models) == len(SUTS):
        cost_plan["auth_balance"]["status"] = (
            "NOT_CHECKED_CREDENTIAL_ACCESS_UNAUTHORIZED")
    _write_json_new(output / "cost-plan.json", cost_plan)
    _write_cost_csv(output / "cost-plan.csv", cost_plan)
    if blockers:
        failure = {
            "schema_version": 1, "validity_label": VALIDITY_LABEL,
            "status": "FAILED/NON-EXECUTABLE", "retrieved_at": retrieved_at,
            "blockers": blockers, "public_snapshot_hash": snapshot_hash,
            "canonical_slugs": canonical_slugs,
            "auth_balance": cost_plan["auth_balance"],
            "paid_inference_authorized": False,
        }
        _write_json_new(output / "failed-preflight.json", failure)
        status = failure["status"]
    else:
        manifest = build_manifest(
            catalog, endpoints, catalog_retrieved_at=retrieved_at)
        manifest["public_snapshot_hash"] = snapshot_hash
        manifest["canonical_slugs"] = canonical_slugs
        manifest["rendered_prompt_and_judge_ceilings"] = ceilings
        manifest["auth_balance"] = dict(cost_plan["auth_balance"])
        _write_json_new(output / "pilot2-manifest.json", manifest)
        status = "EXECUTABLE-MANIFEST-INPUT"
    report = "\n".join([
        "# WCF-Bench Pilot 2 public preflight", "",
        f"> **{VALIDITY_LABEL}**", "", f"Status: **{status}**",
        "- Auth/balance: NOT_CHECKED_CREDENTIAL_ACCESS_UNAUTHORIZED",
        f"- Proposed cap: {cost_plan.get('totals', {}).get('proposed_cap_usd')}",
        f"- Snapshot hash: {snapshot_hash}",
        "- Blockers: " + (" | ".join(blockers) if blockers else "none"), "",
    ])
    (output / "preflight-report.md").write_text(report, encoding="utf-8")
    return {"status": status, "output_dir": str(output), "blockers": blockers}


def write_manifest_input(path: Path, manifest: Mapping[str, Any]) -> None:
    path = Path(path)
    if path.exists():
        raise PreflightError("append-only preflight output already exists")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2, sort_keys=True, ensure_ascii=False)
        handle.write("\n")


def main(
    argv: Optional[Sequence[str]] = None, *,
    metadata_fetch: Callable[[], Tuple[Dict[str, Any], Dict[str, Any]]] =
        fetch_public_catalog,
    now: Callable[[], str] = _utc_now,
) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--public-preflight", action="store_true")
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args(argv)
    if not args.public_preflight:
        print("WCF-Bench Pilot 2 preflight — DRY RUN (zero network calls)")
        return 0
    if args.output_dir is None:
        parser.error("--public-preflight requires --output-dir")
    try:
        result = run_public_preflight(
            args.output_dir, metadata_fetch=metadata_fetch, now=now)
    except PreflightOutputError as exc:
        print(f"ERROR: {exc}")
        return 2
    print(f"Pilot 2 public preflight: {result['status']} at {result['output_dir']}")
    return 0 if result["status"] == "EXECUTABLE-MANIFEST-INPUT" else 1


if __name__ == "__main__":
    raise SystemExit(main())
