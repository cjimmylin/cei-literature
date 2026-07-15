#!/usr/bin/env python3
"""Offline-only manifest builder for WCF-Bench Pilot 2.

The module accepts already-fetched public metadata.  It never reads credentials and
has no inference path; a successful packet remains stopped at amount authorization.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Mapping, Optional, Sequence, Tuple

from wcfbench import load_items, scorer_kind

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


@dataclass(frozen=True)
class SutSpec:
    slug: str
    provider: str
    reasoning: Dict[str, Any]
    prompt_price_per_token: float
    completion_price_per_token: float


SUT_SPECS: Tuple[SutSpec, ...] = (
    SutSpec("minimax/minimax-m3", "MiniMax", {"enabled": True},
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
    current_prompt, current_completion = _price(endpoint, spec.provider)
    if (current_prompt > spec.prompt_price_per_token
            or current_completion > spec.completion_price_per_token):
        raise PreflightError(f"pinned provider exceeds frozen price: {spec.slug}")
    maximum = (SUT_PROMPT_TOKENS * spec.prompt_price_per_token
               + SUT_MAX_TOKENS * spec.completion_price_per_token)
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
                "prompt": spec.prompt_price_per_token * 1_000_000,
                "completion": spec.completion_price_per_token * 1_000_000,
            },
        },
        "prices_per_token": {
            "prompt": spec.prompt_price_per_token,
            "completion": spec.completion_price_per_token,
        },
        "maximum_attempt_cost_usd": maximum,
    }


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
    attempt_envelope = sum(row["maximum_attempt_cost_usd"]
                           * SUT_ATTEMPTS_MAX_PER_MODEL for row in models)
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
        "planning_cost": {
            "attempt_envelope_usd": attempt_envelope,
            "provider_canary_retry_envelope_usd": sum(
                row["maximum_attempt_cost_usd"] * 2 for row in models),
            "proposed_cap_usd": PROPOSED_CAP_USD,
        },
        "auth_balance": {"status": "NOT_CHECKED", "balance_usd": None,
                         "top_up_usd": None},
        "authorization_gate": {
            "credential_access": False,
            "oauth_canary": False,
            "paid_inference": False,
            "required_next": "AMOUNT_SPECIFIC_OWNER_AUTHORIZATION",
        },
    }


def write_manifest_input(path: Path, manifest: Mapping[str, Any]) -> None:
    path = Path(path)
    if path.exists():
        raise PreflightError("append-only preflight output already exists")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2, sort_keys=True, ensure_ascii=False)
        handle.write("\n")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog-json", type=Path, required=True)
    parser.add_argument("--endpoints-json", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--retrieved-at", required=True)
    args = parser.parse_args(argv)
    catalog = json.loads(args.catalog_json.read_text(encoding="utf-8"))
    endpoints = json.loads(args.endpoints_json.read_text(encoding="utf-8"))
    write_manifest_input(args.output, build_manifest(
        catalog, endpoints, catalog_retrieved_at=args.retrieved_at))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
