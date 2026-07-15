#!/usr/bin/env python3
"""Offline controller seam for the WCF-Bench Open-First MVP pilot.

This module deliberately has no live execution mode.  It freezes request, schedule,
resume, first-cell, aggregation, and budget behavior for a separately authorized run.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import threading
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, Mapping, MutableMapping, Optional, Sequence, Tuple

from wcfbench import mvp
from wcfbench.promptbuilder import build_examinee_prompt

import open_first_mvp_preflight as preflight


SCALAR_DENOMINATOR = 222
SCALAR_MINIMUM_NUMERIC = 200
SUT_SHARD_CONCURRENCY = 3
JUDGE_CONCURRENCY = 1


class TerminalStop(RuntimeError):
    """A frozen validity, price, or budget guard requires the run to stop."""


class ResumeError(RuntimeError):
    """Resume state is not the one immutable execution identity."""


def _model_row(manifest: Mapping[str, Any], slug: str) -> Dict[str, Any]:
    rows = [row for row in (manifest.get("models") or []) if row.get("slug") == slug]
    if len(rows) != 1 or slug not in preflight.SUTS:
        raise TerminalStop(f"model is outside the exact Open-First identity: {slug}")
    return dict(rows[0])


def build_sut_request(
    manifest: Mapping[str, Any], slug: str,
    messages: Sequence[Mapping[str, str]],
) -> Dict[str, Any]:
    """Render one exact-model request; provider fallback is not model substitution."""
    row = _model_row(manifest, slug)
    parameters = row.get("request_parameters")
    if not isinstance(parameters, Mapping):
        raise TerminalStop(f"manifest lacks request parameters for {slug}")
    request = {
        "model": slug,
        "messages": [dict(message) for message in messages],
        "temperature": parameters.get("temperature"),
        "max_tokens": parameters.get("max_tokens"),
        "provider": dict(row.get("provider_policy") or {}),
    }
    if "reasoning" in parameters:
        request["reasoning"] = dict(parameters["reasoning"])
    if (request["temperature"] != 0 or request["max_tokens"] != 2048
            or request["provider"].get("sort") != "price"
            or request["provider"].get("require_parameters") is not True
            or request["provider"].get("data_collection") != "deny"):
        raise TerminalStop(f"request contract drifted for {slug}")
    return request


def build_blind_messages(item: Any) -> list:
    """Reuse the frozen blindness-preserving examinee prompt builder."""
    prompt = build_examinee_prompt(item)
    return [
        {"role": "system", "content": prompt.system},
        {"role": "user", "content": prompt.user},
    ]


def validate_runtime_catalog(
    manifest: Mapping[str, Any], catalog: Mapping[str, Mapping[str, Any]],
) -> None:
    """Reject missing models, missing prices, or drift above any frozen ceiling."""
    for slug in preflight.SUTS:
        if slug not in catalog:
            raise TerminalStop(f"runtime catalog lacks exact slug: {slug}")
        frozen = _model_row(manifest, slug).get("prices")
        if not isinstance(frozen, Mapping):
            raise TerminalStop(f"manifest lacks price ceiling: {slug}")
        try:
            current_prompt, current_completion = mvp.price_for(slug, dict(catalog))
            ceilings = (float(frozen["prompt"]), float(frozen["completion"]))
        except (KeyError, TypeError, ValueError, mvp.PricingError) as exc:
            raise TerminalStop(f"runtime price ceiling cannot be verified: {slug}") from exc
        if (not all(math.isfinite(value) and value > 0
                    for value in (current_prompt, current_completion, *ceilings))
                or current_prompt > ceilings[0]
                or current_completion > ceilings[1]):
            raise TerminalStop(f"runtime price ceiling exceeded: {slug}")


def _reasoning_tokens(response: Mapping[str, Any]) -> float:
    usage = response.get("usage")
    if not isinstance(usage, Mapping):
        return 0.0
    values = [usage.get("reasoning_tokens")]
    for details_name in ("completion_tokens_details", "output_tokens_details"):
        details = usage.get(details_name)
        if isinstance(details, Mapping):
            values.append(details.get("reasoning_tokens"))
    total = 0.0
    for value in values:
        if value is None:
            continue
        try:
            total += float(value)
        except (TypeError, ValueError) as exc:
            raise TerminalStop("first cell has malformed reasoning-token accounting") from exc
    return total


def validate_first_live_cell(response: Mapping[str, Any]) -> None:
    """Stop immediately if reasoning occurred or a request parameter was ignored."""
    if not isinstance(response, Mapping):
        raise TerminalStop("first cell response is not an object")
    if _reasoning_tokens(response) > 0:
        raise TerminalStop("first cell reported reasoning tokens")
    for field in ("ignored_parameters", "ignored_params"):
        if response.get(field):
            raise TerminalStop(f"first cell reported ignored parameter: {response[field]}")
    warnings = response.get("warnings") or []
    if not isinstance(warnings, list):
        raise TerminalStop("first cell warnings are malformed")
    for warning in warnings:
        text = json.dumps(warning, sort_keys=True).lower()
        if "ignored_parameter" in text or "ignored parameter" in text:
            raise TerminalStop(f"first cell reported ignored parameter: {warning}")


def custody_first_sut_response(
    *, sut: str, response: Mapping[str, Any],
    persist: Callable[[Dict[str, Any]], Any],
    state: MutableMapping[str, Dict[str, Any]],
) -> Dict[str, Any]:
    """Persist exactly one immutable first response before applying its terminal guard."""
    if sut not in preflight.SUTS:
        raise TerminalStop(f"first response SUT is outside the frozen roster: {sut}")
    if sut in state:
        raise TerminalStop(f"first response already recorded for {sut}")
    if not isinstance(response, Mapping):
        raise TerminalStop("first response is not an object")
    frozen_response = copy.deepcopy(dict(response))
    response_hash = hashlib.sha256(json.dumps(
        frozen_response, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False).encode("utf-8")).hexdigest()
    record = {
        "schema_version": 1,
        "kind": "open_first_mvp_first_sut_response",
        "validity_label": preflight.VALIDITY_LABEL,
        "sut": sut,
        "response_sha256": response_hash,
        "response": frozen_response,
    }
    try:
        persist(copy.deepcopy(record))
    except Exception as exc:
        raise TerminalStop(f"first response persistence failed for {sut}: {exc}") from exc
    state[sut] = {
        "status": "PERSISTED_PENDING_VALIDATION",
        "response_sha256": response_hash,
    }
    try:
        validate_first_live_cell(frozen_response)
    except TerminalStop:
        state[sut]["status"] = "PERSISTED_TERMINAL_GUARD_FAILURE"
        raise
    state[sut]["status"] = "PERSISTED_AND_VALIDATED"
    return copy.deepcopy(record)


def require_validated_first_response(
    sut: str, state: Mapping[str, Mapping[str, Any]],
) -> None:
    """Block later schedule work until that SUT's persisted first response passed."""
    if (state.get(sut) or {}).get("status") != "PERSISTED_AND_VALIDATED":
        raise TerminalStop(f"validated first response is required before scheduling {sut}")


def build_sut_shards(suts: Sequence[str]) -> Tuple[Tuple[str, ...], ...]:
    """Create exactly three stable, balanced model shards."""
    if tuple(suts) != preflight.SUTS:
        raise TerminalStop("SUT shard input is not the exact frozen roster")
    return tuple(tuple(suts[index::SUT_SHARD_CONCURRENCY])
                 for index in range(SUT_SHARD_CONCURRENCY))


def _run_shard(
    shard: Sequence[str], item_ids: Sequence[str],
    run_cell: Callable[[str, str, Callable[[], None]], Any],
    cancellation: threading.Event,
    start_lock: threading.Lock,
    budget: "BudgetController",
    maximum_cost_usd: Callable[[str, str], float],
    actual_cost_usd: Callable[[Any], float],
) -> list:
    output = []
    for sut in shard:
        for item_id in item_ids:
            start_lock.acquire()
            if cancellation.is_set():
                start_lock.release()
                return output
            try:
                reservation = budget.reserve(maximum_cost_usd(sut, item_id))
            except TerminalStop:
                cancellation.set()
                start_lock.release()
                raise

            acknowledged = False
            gate_held = True

            def acknowledge_start() -> None:
                nonlocal acknowledged, gate_held
                if acknowledged:
                    raise TerminalStop("cell start was acknowledged more than once")
                acknowledged = True
                gate_held = False
                start_lock.release()

            result = None
            error: Optional[Exception] = None
            try:
                result = run_cell(sut, item_id, acknowledge_start)
                if not acknowledged:
                    error = TerminalStop("cell did not acknowledge its gated start")
            except Exception as exc:
                error = exc
            finally:
                if gate_held:
                    gate_held = False
                    start_lock.release()

            if isinstance(error, TerminalStop):
                with start_lock:
                    cancellation.set()
            outcome = error if error is not None else result
            try:
                budget.settle(reservation, actual_cost_usd(outcome))
            except Exception as exc:
                settlement_error = TerminalStop(
                    f"cell budget settlement failed: {exc}")
                with start_lock:
                    cancellation.set()
                if error is not None:
                    raise settlement_error from error
                raise settlement_error from exc
            if error is not None:
                raise error
            output.append(result)
    return output


def execute_sut_shards(
    shards: Sequence[Sequence[str]], item_ids: Sequence[str],
    run_cell: Callable[[str, str, Callable[[], None]], Any],
    *, budget: "BudgetController",
    maximum_cost_usd: Callable[[str, str], float],
    actual_cost_usd: Callable[[Any], float],
    executor_factory: Callable[..., Any] = ThreadPoolExecutor,
    cancellation_event: Optional[threading.Event] = None,
) -> list:
    """Run three shard workers concurrently; each worker is strictly sequential."""
    if len(shards) != SUT_SHARD_CONCURRENCY:
        raise TerminalStop("Open-First execution requires exactly three SUT shards")
    cancellation = cancellation_event or threading.Event()
    start_lock = threading.Lock()
    with executor_factory(max_workers=SUT_SHARD_CONCURRENCY) as executor:
        futures = [executor.submit(
            _run_shard, shard, item_ids, run_cell, cancellation, start_lock,
            budget, maximum_cost_usd, actual_cost_usd)
                   for shard in shards]
        return [value for future in futures for value in future.result()]


def build_judge_batches(
    decisions: Sequence[Mapping[str, Any]],
    *, schedule: Optional[Mapping[str, Any]] = None,
) -> list:
    """Batch unique decisions by SUT and route, never crossing either boundary."""
    frozen = dict(schedule or preflight.build_schedule(
        preflight.load_items(str(preflight.BANK_DIR))))
    grouped: Dict[Tuple[str, str], list] = {}
    seen = set()
    for decision in decisions:
        record_id = decision.get("record_id")
        sut = decision.get("sut")
        route = decision.get("route")
        item_id = decision.get("item_id")
        if not isinstance(record_id, str) or not record_id or record_id in seen:
            raise TerminalStop("judge decisions require unique non-empty record IDs")
        if sut not in preflight.SUTS or route not in {"open", "contested", "episode"}:
            raise TerminalStop("judge decision is outside the frozen SUT/route identity")
        route_ids = set((frozen.get("judge_route_item_ids") or {}).get(str(route), []))
        if not isinstance(item_id, str) or item_id not in route_ids:
            raise TerminalStop("judge decision item is missing or outside its frozen route")
        seen.add(record_id)
        grouped.setdefault((str(sut), str(route)), []).append(dict(decision))
    batches = []
    for sut in preflight.SUTS:
        for route in ("open", "contested", "episode"):
            rows = grouped.get((sut, route), [])
            batches.extend(rows[index:index + preflight.JUDGE_BATCH_SIZE]
                           for index in range(0, len(rows), preflight.JUDGE_BATCH_SIZE))
    return batches


def execute_judge_batches(
    batches: Sequence[Sequence[Mapping[str, Any]]],
    judge_batch: Callable[[Sequence[Mapping[str, Any]]], Any],
) -> list:
    """The sole judge has fixed concurrency one."""
    return [judge_batch(batch) for batch in batches]


def aggregate_scalar_scores(
    records: Sequence[Mapping[str, Any]], sut: str,
    *, schedule: Optional[Mapping[str, Any]] = None,
) -> Dict[str, Any]:
    """Aggregate only numeric scalar records; errors stay missing and never become zero."""
    frozen = dict(schedule or preflight.build_schedule(
        preflight.load_items(str(preflight.BANK_DIR))))
    eligible_ids = set(frozen.get("scalar_eligible_item_ids") or [])
    numeric = []
    seen = set()
    for record in records:
        item_id = record.get("item_id")
        if (record.get("sut") != sut or item_id not in eligible_ids
                or item_id in seen):
            continue
        seen.add(item_id)
        if record.get("error"):
            continue
        score = record.get("score")
        if (isinstance(score, (int, float)) and not isinstance(score, bool)
                and math.isfinite(float(score))):
            numeric.append(float(score))
    count = len(numeric)
    eligible = count >= SCALAR_MINIMUM_NUMERIC
    return {
        "eligible": eligible,
        "numeric": count,
        "denominator": SCALAR_DENOMINATOR,
        "missing": max(0, SCALAR_DENOMINATOR - count),
        "mean": sum(numeric) / count if eligible else None,
    }


def build_execution_identity(
    manifest: Mapping[str, Any], *, execution_id: str,
) -> Dict[str, Any]:
    """Bind one execution/resume custody identity to the full deterministic manifest."""
    if not execution_id:
        raise ResumeError("execution identity must be non-empty")
    manifest_hash = hashlib.sha256(json.dumps(
        manifest, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
    ).encode("utf-8")).hexdigest()
    return {
        "schema_version": 1,
        "execution_id": execution_id,
        "validity_label": preflight.VALIDITY_LABEL,
        "manifest_hash": manifest_hash,
        "catalog_hash": manifest.get("catalog_hash"),
        "suts": list(preflight.SUTS),
        "judge": preflight.JUDGE_MODEL,
        "retry_policy": dict(manifest.get("retry_policy") or {}),
        "concurrency": dict(manifest.get("concurrency") or {}),
        "budget_cap_usd": (manifest.get("planning_cost") or {}).get("proposed_cap_usd"),
    }


def validate_resume_identity(
    expected: Mapping[str, Any], observed: Mapping[str, Any],
) -> None:
    if dict(expected) != dict(observed):
        raise ResumeError("resume identity does not match the immutable execution identity")


@dataclass
class BudgetController:
    """Strict pre-attempt budget stop with actual-cost custody."""

    cap_usd: float
    spent_usd: float = 0.0
    reserved_usd: float = 0.0
    _lock: threading.Lock = field(default_factory=threading.Lock, init=False, repr=False)
    _reservations: Dict[int, float] = field(default_factory=dict, init=False, repr=False)
    _next_reservation: int = field(default=1, init=False, repr=False)

    def __post_init__(self) -> None:
        if (not math.isfinite(self.cap_usd) or self.cap_usd <= 0
                or not math.isfinite(self.spent_usd) or self.spent_usd < 0
                or self.spent_usd > self.cap_usd
                or self.reserved_usd != 0):
            raise ValueError("budget cap must be finite and positive")

    def reserve(self, maximum_usd: float) -> int:
        """Atomically reserve one call's maximum cost against available funds."""
        with self._lock:
            if (not math.isfinite(maximum_usd) or maximum_usd < 0
                    or self.spent_usd + self.reserved_usd + maximum_usd
                    > self.cap_usd):
                raise TerminalStop("strict Open-First budget cap would be exceeded")
            reservation = self._next_reservation
            self._next_reservation += 1
            self._reservations[reservation] = maximum_usd
            self.reserved_usd += maximum_usd
            return reservation

    def settle(self, reservation: Any, actual_usd: float) -> None:
        """Record actual cost and release only that reservation's unused capacity."""
        with self._lock:
            maximum_usd = self._reservations.get(reservation)
            if maximum_usd is None:
                raise TerminalStop("budget reservation is missing or already settled")
            del self._reservations[reservation]
            self.reserved_usd -= maximum_usd
            if (not math.isfinite(actual_usd) or actual_usd < 0
                    or actual_usd > maximum_usd):
                raise TerminalStop("actual cost exceeds its maximum reservation")
            if self.spent_usd + actual_usd > self.cap_usd:
                raise TerminalStop("strict Open-First budget cap was exceeded")
            self.spent_usd += actual_usd


# Explicit reuse points for an authorized controller; neither makes a call by itself.
cell_key = mvp.cell_key
append_checkpoint = mvp.append_checkpoint


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)
    print("WCF-Bench Open-First MVP controller — OFFLINE ONLY")
    print(preflight.VALIDITY_LABEL)
    print("No live execution mode is implemented or authorized.")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
