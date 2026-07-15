#!/usr/bin/env python3
"""Offline-testable controller, canary, judge packing, and scoring seams for Pilot 2."""

from __future__ import annotations

import copy
import json
import math
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Callable, Dict, Mapping, Sequence, Tuple

import pilot2_preflight as preflight


class TerminalStop(RuntimeError):
    """A registered semantic, validity, or accounting gate failed."""


class TransportFailure(RuntimeError):
    """A retryable provider transport/HTTP failure occurred."""


def _spec(slug: str) -> preflight.SutSpec:
    matches = [spec for spec in preflight.SUT_SPECS if spec.slug == slug]
    if len(matches) != 1:
        raise TerminalStop(f"SUT is outside exact Pilot 2 roster: {slug}")
    return matches[0]


def _model_row(manifest: Mapping[str, Any], slug: str) -> Mapping[str, Any]:
    rows = [row for row in manifest.get("models", ()) if row.get("slug") == slug]
    if len(rows) != 1 or slug not in preflight.SUTS:
        raise TerminalStop(f"manifest lacks exact Pilot 2 model: {slug}")
    return rows[0]


def build_sut_request(
    manifest: Mapping[str, Any], slug: str,
    messages: Sequence[Mapping[str, str]],
) -> Dict[str, Any]:
    spec = _spec(slug)
    row = _model_row(manifest, slug)
    parameters = row.get("request_parameters")
    policy = row.get("provider_policy")
    prices = row.get("prices_per_token") or {}
    try:
        frozen_max_price = {
            "prompt": float(policy["max_price"]["prompt"]),
            "completion": float(policy["max_price"]["completion"]),
        }
        frozen_prices = {
            "prompt": float(prices["prompt"]) * 1_000_000,
            "completion": float(prices["completion"]) * 1_000_000,
        }
    except (KeyError, TypeError, ValueError) as exc:
        raise TerminalStop(f"request price contract drifted: {slug}") from exc
    expected_policy = {
        "order": [spec.provider],
        "allow_fallbacks": False,
        "require_parameters": True,
        "data_collection": "deny",
        "max_price": frozen_max_price,
    }
    if parameters != {
            "temperature": 0, "max_tokens": 8192,
            "reasoning": spec.reasoning} or policy != expected_policy \
            or frozen_max_price != frozen_prices \
            or frozen_max_price["prompt"] > spec.prompt_price_per_token * 1_000_000 \
            or frozen_max_price["completion"] > spec.completion_price_per_token * 1_000_000 \
            or not all(math.isfinite(value) and value > 0
                       for value in frozen_max_price.values()):
        raise TerminalStop(f"request contract drifted: {slug}")
    return {
        "model": slug,
        "messages": [dict(message) for message in messages],
        "temperature": 0,
        "max_tokens": 8192,
        "reasoning": dict(spec.reasoning),
        "provider": dict(policy),
    }


def _reasoning_tokens(response: Mapping[str, Any]) -> float:
    usage = response.get("usage")
    if not isinstance(usage, Mapping):
        raise TerminalStop("valid usage is missing")
    values = [usage.get("reasoning_tokens")]
    for name in ("completion_tokens_details", "output_tokens_details"):
        details = usage.get(name)
        if isinstance(details, Mapping):
            values.append(details.get("reasoning_tokens"))
    observed = []
    for value in values:
        if value is None:
            continue
        try:
            parsed = float(value)
        except (TypeError, ValueError) as exc:
            raise TerminalStop("reasoning usage is malformed") from exc
        if not math.isfinite(parsed) or parsed < 0:
            raise TerminalStop("reasoning usage is malformed")
        observed.append(parsed)
    return max(observed) if observed else 0.0


def _ignored_parameter(response: Mapping[str, Any]) -> bool:
    if response.get("ignored_parameters") or response.get("ignored_params"):
        return True
    warnings = response.get("warnings") or []
    if not isinstance(warnings, list):
        raise TerminalStop("warnings are malformed")
    return any("ignored parameter" in json.dumps(value).lower()
               or "ignored_parameter" in json.dumps(value).lower()
               for value in warnings)


def validate_provider_response(
    spec: preflight.SutSpec, response: Mapping[str, Any],
) -> Dict[str, Any]:
    if not isinstance(response, Mapping):
        raise TerminalStop("provider response is not an object")
    if response.get("provider") != spec.provider:
        raise TerminalStop(
            f"provider mismatch: expected {spec.provider}, got {response.get('provider')}")
    if _ignored_parameter(response):
        raise TerminalStop("provider reported ignored parameter")
    try:
        choice = response["choices"][0]
        message = choice["message"]
        content = message["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise TerminalStop("nonempty final answer is missing") from exc
    if not isinstance(content, str) or not content.strip():
        raise TerminalStop("nonempty final answer is required")
    if choice.get("finish_reason") == "length":
        raise TerminalStop("finish_reason length failed the canary gate")
    usage = response.get("usage")
    if not isinstance(usage, Mapping):
        raise TerminalStop("valid usage is missing")
    for name in ("prompt_tokens", "completion_tokens"):
        value = usage.get(name)
        if not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0:
            raise TerminalStop("valid usage is missing")
    cost = usage.get("cost")
    if not isinstance(cost, (int, float)) or isinstance(cost, bool):
        raise TerminalStop("response-attributed cost is missing")
    if not math.isfinite(float(cost)) or float(cost) < 0:
        raise TerminalStop("response-attributed cost is invalid")
    reasoning_tokens = _reasoning_tokens(response)
    if reasoning_tokens <= 0:
        raise TerminalStop("positive reasoning evidence is required")
    return {
        "final_answer": content,
        "private_reasoning": message.get("reasoning"),
        "reasoning_tokens": reasoning_tokens,
        "response_attributed_cost_usd": float(cost),
        "provider": spec.provider,
        "finish_reason": choice.get("finish_reason"),
    }


def run_provider_canary(
    spec: preflight.SutSpec,
    transport: Callable[[Dict[str, Any]], Mapping[str, Any]],
) -> Dict[str, Any]:
    payload = {
        "model": spec.slug,
        "messages": [{
            "role": "user",
            "content": "Synthetic non-bank check: explain whether 17 is prime, briefly.",
        }],
        "temperature": 0,
        "max_tokens": 8192,
        "reasoning": dict(spec.reasoning),
        "provider": {
            "order": [spec.provider], "allow_fallbacks": False,
            "require_parameters": True, "data_collection": "deny",
            "max_price": {
                "prompt": spec.prompt_price_per_token * 1_000_000,
                "completion": spec.completion_price_per_token * 1_000_000,
            },
        },
    }
    for attempt in (1, 2):
        try:
            response = transport(payload)
        except TransportFailure:
            if attempt == 1:
                continue
            raise
        result = validate_provider_response(spec, response)
        return {"status": "PASS", "attempts": attempt, "result": result}
    raise AssertionError("unreachable")


def build_sut_shards(suts: Sequence[str]) -> Tuple[Tuple[str, ...], ...]:
    if tuple(suts) != preflight.SUTS:
        raise TerminalStop("sharding requires the exact Pilot 2 roster order")
    return tuple(tuple(suts[index::3]) for index in range(3))


def execute_registered_sequence(
    *, item_ids: Sequence[str], run_cell: Callable[[str, str], Mapping[str, Any]],
    suts: Sequence[str] = preflight.SUTS,
) -> Dict[str, Any]:
    if not item_ids or len(set(item_ids)) != len(item_ids):
        raise TerminalStop("execution requires unique item IDs")
    if tuple(suts) != preflight.SUTS:
        raise TerminalStop("execution roster drifted")
    first = item_ids[0]
    for sut in suts:
        outcome = run_cell(sut, first)
        if outcome.get("status") != "response":
            raise TerminalStop(f"first real cell failed: {sut}")
    shards = build_sut_shards(suts)

    def run_shard(shard: Sequence[str]) -> int:
        count = 0
        for sut in shard:
            for item_id in item_ids[1:]:
                run_cell(sut, item_id)
                count += 1
        return count

    with ThreadPoolExecutor(max_workers=3) as pool:
        completed = list(pool.map(run_shard, shards))
    return {
        "first_cells_validated": len(suts),
        "shards": [list(shard) for shard in shards],
        "remaining_attempted": sum(completed),
    }


def project_final_answer_to_judge(
    *, sut: str, route: str, item_id: str, criterion_id: str,
    persisted_response: Mapping[str, Any],
) -> Dict[str, Any]:
    if route not in {"open", "contested", "episode"}:
        raise TerminalStop("unsupported judge route")
    final = persisted_response.get("final_answer")
    if not isinstance(final, str) or not final:
        raise TerminalStop("persisted final answer is missing")
    return {
        "record_id": f"{sut}::{item_id}::{criterion_id}",
        "sut": sut,
        "route": route,
        "payload": {"criterion_id": criterion_id, "response": final},
    }


def _judge_projection(row: Mapping[str, Any]) -> Dict[str, Any]:
    payload = row.get("payload")
    if not isinstance(payload, Mapping):
        raise TerminalStop("judge record payload is malformed")
    projected = {
        "record_id": row.get("record_id"),
        "sut": row.get("sut"),
        "route": row.get("route"),
        "payload": copy.deepcopy(dict(payload)),
    }
    if row.get("call_kind") is not None:
        projected["call_kind"] = row.get("call_kind")
    return projected


def serialize_judge_record(row: Mapping[str, Any]) -> bytes:
    return json.dumps(_judge_projection(row), sort_keys=True,
                      ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def serialize_judge_batch(rows: Sequence[Mapping[str, Any]]) -> str:
    projected = [_judge_projection(row) for row in rows]
    return json.dumps(projected, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"))


def build_dynamic_judge_batches(
    records: Sequence[Mapping[str, Any]],
) -> Tuple[list, list]:
    if not records:
        return [], []
    identities = {(row.get("sut"), row.get("route"), row.get("call_kind"))
                  for row in records}
    if len(identities) != 1:
        raise TerminalStop("judge records may not mix SUT or route")
    ids = [row.get("record_id") for row in records]
    if any(not isinstance(value, str) or not value for value in ids) \
            or len(set(ids)) != len(ids):
        raise TerminalStop("judge record IDs must be unique")
    batches, missing, current = [], [], []
    for source in records:
        projected = _judge_projection(source)
        response = projected["payload"].get(
            "response", projected["payload"].get("judge_prompt"))
        if not isinstance(response, str):
            raise TerminalStop("judge response is malformed")
        if len(serialize_judge_record(source)) > preflight.JUDGE_MAX_SERIALIZED_RECORD_BYTES:
            missing.append({
                "record_id": source["record_id"],
                "status": "missing",
                "score": None,
                "reason": "judge_record_byte_ceiling_exceeded",
                "response": response,
            })
            continue
        candidate = current + [projected]
        if (len(candidate) > preflight.JUDGE_MAX_BATCH_SIZE
                or len(serialize_judge_batch(candidate).encode("utf-8"))
                > preflight.JUDGE_MAX_SERIALIZED_BATCH_BYTES):
            if current:
                batches.append(current)
            current = [projected]
        else:
            current = candidate
    if current:
        batches.append(current)
    return batches, missing


def aggregate_scalar_scores(rows: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
    numeric = [float(row["score"]) for row in rows
               if row.get("status") == "numeric"
               and isinstance(row.get("score"), (int, float))
               and not isinstance(row.get("score"), bool)]
    if len(rows) != 222:
        raise TerminalStop("scalar aggregation requires 222 eligible rows")
    return {
        "numeric": len(numeric),
        "errors": 222 - len(numeric),
        "mean": sum(numeric) / len(numeric) if len(numeric) >= 200 else None,
        "coverage_status": ("SUFFICIENT_DESCRIPTIVE" if len(numeric) >= 200
                            else "INCOMPLETE"),
    }


def main() -> int:
    print("Pilot 2 controller is implementation-only; use a separately authorized driver.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
