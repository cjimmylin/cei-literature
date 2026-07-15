#!/usr/bin/env python3
"""Immutable custody and strict-cap primitives for a future authorized Pilot 2 run."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import os
import sys
import threading
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Dict, Mapping, Optional, Sequence

import pilot2_preflight as preflight
import pilot2_run as controller
from wcfbench.promptbuilder import build_examinee_prompt
from wcfbench import scorer_kind
from wcfbench.mvp import fetch_key_snapshot


MANIFEST_COPY = "pilot2-manifest.json"
IDENTITY_FILE = "run-identity.json"
EVIDENCE_FILE = "raw-evidence.jsonl"
CHECKPOINT_FILE = "checkpoint.jsonl"
CHAT_URL = "https://openrouter.ai/api/v1/chat/completions"
MAX_RETRIES_PER_CELL = 2


class CustodyStop(RuntimeError):
    """The immutable evidence chain or strict cap cannot be trusted."""


TransportFailure = controller.TransportFailure


@dataclass(frozen=True)
class LiveCell:
    sut: str
    item_id: str
    diagnostic_only: bool
    scorable: bool

    @property
    def key(self) -> str:
        return f"{self.sut}::{self.item_id}"


def _hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _write_new(path: Path, value: Mapping[str, Any]) -> None:
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True, ensure_ascii=False)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())


def _append(path: Path, value: Mapping[str, Any], lock: threading.Lock) -> None:
    with lock:
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(value, sort_keys=True, ensure_ascii=False) + "\n")
            handle.flush()
            os.fsync(handle.fileno())


@dataclass
class RunState:
    run_dir: Path
    cap_usd: float
    spent_usd: float = 0.0
    reservations: Dict[str, float] = field(default_factory=dict)
    attempts_by_sut: Dict[str, int] = field(default_factory=dict)
    retries_by_sut: Dict[str, int] = field(default_factory=dict)
    attempts_by_cell: Dict[str, int] = field(default_factory=dict)
    completed: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    first_validated: set = field(default_factory=set)
    canaries_passed: set = field(default_factory=set)
    lock: threading.Lock = field(default_factory=threading.Lock)

    def reserve(self, request_id: str, maximum_usd: float) -> None:
        if not isinstance(request_id, str) or not request_id:
            raise CustodyStop("reservation request ID is invalid")
        if (not math.isfinite(maximum_usd) or maximum_usd <= 0):
            raise CustodyStop("reservation amount is invalid")
        with self.lock:
            if request_id in self.reservations:
                raise CustodyStop("request already has a reservation")
            committed = self.spent_usd + sum(self.reservations.values())
            if committed + maximum_usd > self.cap_usd + 1e-12:
                raise CustodyStop("strict Pilot 2 cap would be exceeded")
            self.reservations[request_id] = maximum_usd
        _append(self.run_dir / EVIDENCE_FILE, {
            "kind": "reservation", "request_id": request_id,
            "maximum_usd": maximum_usd,
        }, self.lock)

    def settle(self, request_id: str, actual_usd: float) -> None:
        if not math.isfinite(actual_usd) or actual_usd < 0:
            raise CustodyStop("response-attributed cost is missing or invalid")
        with self.lock:
            maximum = self.reservations.get(request_id)
            if maximum is None:
                raise CustodyStop("settlement lacks reservation custody")
            if actual_usd > maximum + 1e-12:
                raise CustodyStop("response cost exceeds conservative reservation")
            self.spent_usd += actual_usd
            del self.reservations[request_id]
            cumulative = self.spent_usd
        _append(self.run_dir / EVIDENCE_FILE, {
            "kind": "cost_settlement", "request_id": request_id,
            "response_attributed_cost_usd": actual_usd,
            "cumulative_spend_usd": cumulative,
        }, self.lock)

    def checkpoint_missing(self, cell_key: str, reason: str, *, attempts: int) -> None:
        if not isinstance(attempts, int) or isinstance(attempts, bool) or attempts < 1:
            raise CustodyStop("missing checkpoint attempts are invalid")
        _append(self.run_dir / CHECKPOINT_FILE, {
            "kind": "pilot2_cell", "cell_key": cell_key,
            "status": "error", "missing": True, "score": None,
            "reason": reason, "attempts": attempts,
        }, self.lock)


def _read_jsonl(path: Path) -> list:
    if not path.exists():
        return []
    rows = []
    try:
        with path.open(encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    value = json.loads(line)
                    if not isinstance(value, dict):
                        raise ValueError("row is not an object")
                    rows.append(value)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise CustodyStop(f"immutable JSONL evidence is malformed: {path}") from exc
    return rows


def _load_manifest(path: Path) -> Dict[str, Any]:
    try:
        manifest = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CustodyStop("manifest is unreadable") from exc
    if (not isinstance(manifest, dict)
            or manifest.get("validity_label") != preflight.VALIDITY_LABEL
            or tuple(manifest.get("exact_sut_slugs") or ()) != preflight.SUTS
            or (manifest.get("geometry") or {}).get("sut_cells") != 1150):
        raise CustodyStop("manifest is not the exact Pilot 2 identity")
    return manifest


def _require_paid_authorization(manifest: Mapping[str, Any]) -> None:
    if (manifest.get("authorization_gate") or {}).get("paid_inference") is not True:
        raise CustodyStop("manifest lacks amount-specific paid authorization")


def build_cells(manifest: Mapping[str, Any]) -> list:
    schedule = manifest.get("schedule") or {}
    all_ids = list(schedule.get("all_item_ids") or ())
    runnable = set(schedule.get("runnable_item_ids") or ())
    dev = set(schedule.get("dev_set_only_item_ids") or ())
    if (len(all_ids) != 230 or len(set(all_ids)) != 230
            or len(runnable) != 226 or len(dev) != 4
            or runnable & dev or set(all_ids) != runnable | dev):
        raise CustodyStop("manifest schedule is not the frozen 230/226/4 split")
    return [LiveCell(sut, item_id, item_id in dev, item_id in runnable)
            for sut in preflight.SUTS for item_id in all_ids]


def build_blind_messages(item: Any) -> list:
    if scorer_kind(item) == "episode":
        return [{"role": "user", "content": item.stem}]
    prompt = build_examinee_prompt(item)
    return [{"role": "system", "content": prompt.system},
            {"role": "user", "content": prompt.user}]


def validate_runtime_catalog(
    manifest: Mapping[str, Any], catalog: Mapping[str, Mapping[str, Any]],
    endpoints: Mapping[str, Sequence[Mapping[str, Any]]],
) -> None:
    for spec in preflight.SUT_SPECS:
        row = next((value for value in manifest.get("models", ())
                    if value.get("slug") == spec.slug), None)
        if not isinstance(row, Mapping) or spec.slug not in catalog:
            raise CustodyStop(f"runtime catalog lacks exact model: {spec.slug}")
        policy = row.get("provider_policy") or {}
        candidates = [value for value in endpoints.get(spec.slug, ())
                      if value.get("provider_name") == spec.provider]
        if len(candidates) != 1:
            raise CustodyStop(f"runtime pinned provider unavailable: {spec.slug}")
        endpoint = candidates[0]
        supported = set(endpoint.get("supported_parameters") or ())
        if not {"temperature", "max_tokens", "reasoning"} <= supported:
            raise CustodyStop(f"runtime pinned provider parameter drift: {spec.slug}")
        if endpoint.get("data_collection") not in {None, False, "deny", "none"}:
            raise CustodyStop(f"runtime pinned provider data-policy drift: {spec.slug}")
        if (not isinstance(endpoint.get("context_length"), int)
                or endpoint["context_length"] < 10413
                or not isinstance(endpoint.get("max_completion_tokens"), int)
                or endpoint["max_completion_tokens"] < 8192):
            raise CustodyStop(f"runtime pinned provider context/completion drift: {spec.slug}")
        try:
            prices = endpoint["pricing"]
            current = float(prices["prompt"]), float(prices["completion"])
            ceilings = (float(policy["max_price"]["prompt"]) / 1_000_000,
                        float(policy["max_price"]["completion"]) / 1_000_000)
        except (KeyError, TypeError, ValueError) as exc:
            raise CustodyStop(f"runtime pinned provider price is unverifiable: {spec.slug}") from exc
        if (not all(math.isfinite(value) and value > 0 for value in current)
                or current[0] > ceilings[0] or current[1] > ceilings[1]):
            raise CustodyStop(f"runtime pinned provider exceeds price ceiling: {spec.slug}")


def prepare_run(
    manifest_path: Path, run_dir: Path, *, cap_usd: float, resume: bool = False,
) -> RunState:
    manifest_path = Path(manifest_path).resolve()
    run_dir = Path(run_dir).resolve()
    manifest = _load_manifest(manifest_path)
    _require_paid_authorization(manifest)
    try:
        proposed = float((manifest.get("planning_cost") or {})["proposed_cap_usd"])
    except (KeyError, TypeError, ValueError) as exc:
        raise CustodyStop("manifest proposed cap is missing") from exc
    if (not math.isfinite(cap_usd) or cap_usd <= 0 or cap_usd > proposed):
        raise CustodyStop("run cap is invalid or above the refreshed proposed cap")
    expected_identity = {
        "schema_version": 1,
        "kind": "wcf_bench_pilot2_immutable_run",
        "validity_label": preflight.VALIDITY_LABEL,
        "manifest_sha256": _hash(manifest_path),
        "exact_sut_slugs": list(preflight.SUTS),
        "expected_cells": 1150,
        "scorable_cells": 1130,
        "diagnostic_only_cells": 20,
        "cap_usd": cap_usd,
    }
    if resume:
        if not run_dir.is_dir():
            raise CustodyStop("resume run directory does not exist")
        try:
            observed = json.loads((run_dir / IDENTITY_FILE).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise CustodyStop("resume identity is missing or malformed") from exc
        if observed != expected_identity or _hash(run_dir / MANIFEST_COPY) != _hash(manifest_path):
            raise CustodyStop("resume identity does not match immutable Pilot 2 run")
    else:
        if run_dir.exists():
            raise CustodyStop("immutable run directory already exists")
        run_dir.mkdir(parents=True)
        manifest_copy = run_dir / MANIFEST_COPY
        with manifest_path.open("rb") as source, manifest_copy.open("xb") as target:
            target.write(source.read())
            target.flush()
            os.fsync(target.fileno())
        _write_new(run_dir / IDENTITY_FILE, expected_identity)

    evidence = _read_jsonl(run_dir / EVIDENCE_FILE)
    checkpoints = _read_jsonl(run_dir / CHECKPOINT_FILE)
    if any(row.get("kind") == "terminal_stop" for row in evidence):
        raise CustodyStop("resume evidence records a terminal stop")
    reservations = {row["request_id"]: float(row["maximum_usd"])
                    for row in evidence if row.get("kind") == "reservation"}
    settlements = {row["request_id"]: float(row["response_attributed_cost_usd"])
                   for row in evidence if row.get("kind") == "cost_settlement"}
    raw_by_request = {row.get("request_id"): row for row in evidence
                      if row.get("kind") in {
                          "sut_response", "sut_transport_error",
                          "provider_canary_response", "provider_canary_transport_error"}}
    lock = threading.Lock()
    # An observed response/known no-cost transport failure may close an interrupted
    # reservation; a request with no terminal evidence is ambiguous and cannot resume.
    for request_id, maximum in reservations.items():
        if request_id in settlements:
            continue
        raw = raw_by_request.get(request_id)
        if raw is None or raw.get("response_attributed_cost_usd") is None:
            raise CustodyStop("resume has an ambiguous paid request without cost custody")
        actual = float(raw["response_attributed_cost_usd"])
        if actual < 0 or actual > maximum:
            raise CustodyStop("resume response cost exceeds reservation")
        _append(run_dir / EVIDENCE_FILE, {
            "kind": "cost_settlement", "request_id": request_id,
            "response_attributed_cost_usd": actual,
            "cumulative_spend_usd": sum(settlements.values()) + actual,
            "recovered_after_interruption": True,
        }, lock)
        settlements[request_id] = actual
    if set(settlements) - set(reservations):
        raise CustodyStop("resume has settlement without reservation")
    spent = sum(settlements.values())
    if spent > cap_usd:
        raise CustodyStop("resume evidence exceeds strict cap")
    completed = {row["cell_key"]: row for row in checkpoints
                 if row.get("kind") == "pilot2_cell"
                 and row.get("status") in {"response", "error"}}
    response_rows = [row for row in evidence if row.get("kind") == "sut_response"
                     and row.get("status") == "response"]
    for raw in response_rows:
        key = raw.get("cell_key")
        if key in completed:
            continue
        if raw.get("request_id") not in settlements:
            raise CustodyStop("successful response lacks settled cost custody")
        checkpoint = {
            "kind": "pilot2_cell", "cell_key": key,
            "sut": raw["sut"], "item_id": raw["item_id"],
            "status": "response", "missing": False, "score": None,
            "final_answer": raw["final_answer"],
            "response_sha256": raw["response_sha256"],
            "attempts": raw["cell_attempt"],
            "recovered_after_interruption": True,
        }
        _append(run_dir / CHECKPOINT_FILE, checkpoint, lock)
        completed[key] = checkpoint
    attempts_by_sut = {slug: 0 for slug in preflight.SUTS}
    retries_by_sut = {slug: 0 for slug in preflight.SUTS}
    attempts_by_cell: Dict[str, int] = {}
    for row in evidence:
        if row.get("kind") != "sut_request":
            continue
        sut, key, attempt = row.get("sut"), row.get("cell_key"), row.get("cell_attempt")
        if sut not in attempts_by_sut or not isinstance(attempt, int):
            raise CustodyStop("resume request identity is malformed")
        attempts_by_sut[sut] += 1
        if attempt > 1:
            retries_by_sut[sut] += 1
        attempts_by_cell[key] = max(attempts_by_cell.get(key, 0), attempt)
    if any(value > 252 for value in attempts_by_sut.values()) \
            or any(value > 22 for value in retries_by_sut.values()):
        raise CustodyStop("resume evidence exceeds retry envelope")
    return RunState(
        run_dir=run_dir, cap_usd=cap_usd, spent_usd=spent,
        attempts_by_sut=attempts_by_sut, retries_by_sut=retries_by_sut,
        attempts_by_cell=attempts_by_cell, completed=completed,
        first_validated={row.get("sut") for row in evidence
                         if row.get("kind") == "first_cell_validation"
                         and row.get("status") == "PASS"},
        canaries_passed={row.get("sut") for row in evidence
                         if row.get("kind") == "provider_canary_validation"
                         and row.get("status") == "PASS"},
    )


def _maximum_cost(manifest: Mapping[str, Any], sut: str) -> float:
    row = next((row for row in manifest.get("models", ()) if row.get("slug") == sut), None)
    if not isinstance(row, Mapping):
        raise CustodyStop(f"manifest lacks model cost: {sut}")
    try:
        value = float(row["maximum_attempt_cost_usd"])
    except (KeyError, TypeError, ValueError) as exc:
        raise CustodyStop(f"manifest model cost is invalid: {sut}") from exc
    if not math.isfinite(value) or value <= 0:
        raise CustodyStop(f"manifest model cost is invalid: {sut}")
    return value


def _cost(response: Mapping[str, Any]) -> float:
    try:
        value = float((response.get("usage") or {})["cost"])
    except (KeyError, TypeError, ValueError) as exc:
        raise CustodyStop("response-attributed cost is missing") from exc
    if not math.isfinite(value) or value < 0:
        raise CustodyStop("response-attributed cost is invalid")
    return value


def _response_hash(response: Mapping[str, Any]) -> str:
    return hashlib.sha256(json.dumps(
        response, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False).encode("utf-8")).hexdigest()


def _terminal(state: RunState, reason: str, **identity: Any) -> None:
    _append(state.run_dir / EVIDENCE_FILE, {
        "kind": "terminal_stop", "reason": reason, **identity,
    }, state.lock)


def run_provider_canaries(
    manifest: Mapping[str, Any], state: RunState,
    transport: Callable[[Dict[str, Any]], Mapping[str, Any]],
) -> list:
    results = []
    for spec in preflight.SUT_SPECS:
        if spec.slug in state.canaries_passed:
            results.append({"sut": spec.slug, "status": "PASS", "resumed": True})
            continue
        payload = {
            "model": spec.slug,
            "messages": [{"role": "user", "content": (
                "Synthetic non-bank check: explain whether 17 is prime, briefly.")}],
            "temperature": 0, "max_tokens": 8192,
            "reasoning": dict(spec.reasoning),
            "provider": copy.deepcopy(next(
                row["provider_policy"] for row in manifest["models"]
                if row["slug"] == spec.slug)),
        }
        for attempt in (1, 2):
            request_id = f"canary::{spec.slug}::{attempt}"
            state.reserve(request_id, _maximum_cost(manifest, spec.slug))
            _append(state.run_dir / EVIDENCE_FILE, {
                "kind": "provider_canary_request", "request_id": request_id,
                "sut": spec.slug, "attempt": attempt, "payload": payload,
            }, state.lock)
            try:
                response = transport(copy.deepcopy(payload))
            except TransportFailure as exc:
                _append(state.run_dir / EVIDENCE_FILE, {
                    "kind": "provider_canary_transport_error", "request_id": request_id,
                    "sut": spec.slug, "attempt": attempt,
                    "error": f"{type(exc).__name__}: {exc}",
                    "response_attributed_cost_usd": 0.0,
                }, state.lock)
                state.settle(request_id, 0.0)
                if attempt == 1:
                    continue
                _terminal(state, "provider canary transport retry exhausted", sut=spec.slug)
                raise CustodyStop("provider canary transport retry exhausted") from exc
            actual = _cost(response)
            raw = {
                "kind": "provider_canary_response", "request_id": request_id,
                "sut": spec.slug, "attempt": attempt,
                "raw_response": copy.deepcopy(dict(response)),
                "response_sha256": _response_hash(response),
                "response_attributed_cost_usd": actual,
            }
            _append(state.run_dir / EVIDENCE_FILE, raw, state.lock)
            state.settle(request_id, actual)
            try:
                validated = controller.validate_provider_response(spec, response)
            except controller.TerminalStop as exc:
                _terminal(state, str(exc), sut=spec.slug, request_id=request_id)
                raise CustodyStop(str(exc)) from exc
            _append(state.run_dir / EVIDENCE_FILE, {
                "kind": "provider_canary_validation", "sut": spec.slug,
                "status": "PASS", "attempt": attempt,
                "response_sha256": raw["response_sha256"],
            }, state.lock)
            state.canaries_passed.add(spec.slug)
            results.append({"sut": spec.slug, "status": "PASS", "result": validated})
            break
    return results


def _ordinary_validation(
    spec: preflight.SutSpec, response: Mapping[str, Any], *, reasoning_gate: bool,
) -> Dict[str, Any]:
    if response.get("provider") != spec.provider:
        raise CustodyStop(
            f"provider mismatch: expected {spec.provider}, got {response.get('provider')}")
    if controller._ignored_parameter(response):
        raise CustodyStop("provider reported ignored parameter")
    try:
        choice = response["choices"][0]
        content = choice["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise ValueError("malformed final answer") from exc
    if not isinstance(content, str) or not content.strip():
        raise ValueError("empty final answer")
    if reasoning_gate:
        if choice.get("finish_reason") == "length":
            raise CustodyStop("first cell finish_reason length")
        if controller._reasoning_tokens(response) <= 0:
            raise CustodyStop("first cell lacks positive reasoning evidence")
    elif choice.get("finish_reason") == "length":
        raise ValueError("ordinary response truncated at length")
    return {"final_answer": content,
            "private_reasoning": choice["message"].get("reasoning"),
            "reasoning_tokens": controller._reasoning_tokens(response)}


def run_cell(
    cell: LiveCell, *, manifest: Mapping[str, Any], state: RunState,
    transport: Callable[[Dict[str, Any]], Mapping[str, Any]],
    items: Mapping[str, Any], require_reasoning_gate: bool = False,
) -> Dict[str, Any]:
    if cell.key in state.completed:
        return copy.deepcopy(state.completed[cell.key])
    if cell.item_id not in items:
        raise CustodyStop("cell item is outside frozen bank")
    spec = next((spec for spec in preflight.SUT_SPECS if spec.slug == cell.sut), None)
    if spec is None:
        raise CustodyStop("cell SUT is outside frozen roster")
    payload = controller.build_sut_request(
        manifest, cell.sut, build_blind_messages(items[cell.item_id]))
    first_attempt = state.attempts_by_cell.get(cell.key, 0) + 1
    last_error = "ordinary response failed"
    for attempt in range(first_attempt, MAX_RETRIES_PER_CELL + 2):
        with state.lock:
            if state.attempts_by_sut.get(cell.sut, 0) >= 252:
                last_error = "registered model attempt envelope exhausted"
                break
            if attempt > 1 and state.retries_by_sut.get(cell.sut, 0) >= 22:
                last_error = "registered model retry reserve exhausted"
                break
            state.attempts_by_sut[cell.sut] = state.attempts_by_sut.get(cell.sut, 0) + 1
            if attempt > 1:
                state.retries_by_sut[cell.sut] = state.retries_by_sut.get(cell.sut, 0) + 1
            state.attempts_by_cell[cell.key] = attempt
            model_attempt = state.attempts_by_sut[cell.sut]
        request_id = f"cell::{cell.key}::{attempt}"
        state.reserve(request_id, _maximum_cost(manifest, cell.sut))
        _append(state.run_dir / EVIDENCE_FILE, {
            "kind": "sut_request", "request_id": request_id,
            "cell_key": cell.key, "sut": cell.sut, "item_id": cell.item_id,
            "cell_attempt": attempt, "model_attempt": model_attempt,
            "diagnostic_only": cell.diagnostic_only, "scorable": cell.scorable,
            "payload": copy.deepcopy(payload),
        }, state.lock)
        try:
            response = transport(copy.deepcopy(payload))
        except TransportFailure as exc:
            last_error = f"{type(exc).__name__}: {exc}"
            _append(state.run_dir / EVIDENCE_FILE, {
                "kind": "sut_transport_error", "request_id": request_id,
                "cell_key": cell.key, "sut": cell.sut, "item_id": cell.item_id,
                "cell_attempt": attempt, "error": last_error,
                "response_attributed_cost_usd": 0.0,
            }, state.lock)
            state.settle(request_id, 0.0)
            continue
        try:
            actual = _cost(response)
        except CustodyStop as exc:
            _append(state.run_dir / EVIDENCE_FILE, {
                "kind": "sut_response", "request_id": request_id,
                "cell_key": cell.key, "sut": cell.sut, "item_id": cell.item_id,
                "cell_attempt": attempt, "raw_response": copy.deepcopy(dict(response)),
                "response_attributed_cost_usd": None,
            }, state.lock)
            _terminal(state, str(exc), cell_key=cell.key, request_id=request_id)
            raise
        raw = {
            "kind": "sut_response", "request_id": request_id,
            "cell_key": cell.key, "sut": cell.sut, "item_id": cell.item_id,
            "cell_attempt": attempt, "model_attempt": model_attempt,
            "diagnostic_only": cell.diagnostic_only, "scorable": cell.scorable,
            "raw_response": copy.deepcopy(dict(response)),
            "response_sha256": _response_hash(response),
            "response_attributed_cost_usd": actual,
        }
        if response.get("error"):
            raw["status"] = "upstream_error"
            _append(state.run_dir / EVIDENCE_FILE, raw, state.lock)
            state.settle(request_id, actual)
            last_error = str(response["error"])
            continue
        try:
            parsed = _ordinary_validation(
                spec, response, reasoning_gate=require_reasoning_gate)
        except CustodyStop as exc:
            _append(state.run_dir / EVIDENCE_FILE, raw, state.lock)
            state.settle(request_id, actual)
            _terminal(state, str(exc), cell_key=cell.key, request_id=request_id)
            raise
        except ValueError as exc:
            raw["status"] = "ordinary_error"
            _append(state.run_dir / EVIDENCE_FILE, raw, state.lock)
            state.settle(request_id, actual)
            last_error = str(exc)
            continue
        raw.update({
            "status": "response", "final_answer": parsed["final_answer"],
            "private_reasoning": parsed["private_reasoning"],
            "reasoning_tokens": parsed["reasoning_tokens"],
        })
        _append(state.run_dir / EVIDENCE_FILE, raw, state.lock)
        state.settle(request_id, actual)
        checkpoint = {
            "kind": "pilot2_cell", "cell_key": cell.key,
            "sut": cell.sut, "item_id": cell.item_id,
            "status": "response", "missing": False, "score": None,
            "final_answer": parsed["final_answer"],
            "response_sha256": raw["response_sha256"], "attempts": attempt,
            "diagnostic_only": cell.diagnostic_only, "scorable": cell.scorable,
        }
        _append(state.run_dir / CHECKPOINT_FILE, checkpoint, state.lock)
        state.completed[cell.key] = checkpoint
        if require_reasoning_gate:
            _append(state.run_dir / EVIDENCE_FILE, {
                "kind": "first_cell_validation", "sut": cell.sut,
                "cell_key": cell.key, "status": "PASS",
            }, state.lock)
            state.first_validated.add(cell.sut)
        return copy.deepcopy(checkpoint)
    checkpoint = {
        "kind": "pilot2_cell", "cell_key": cell.key,
        "sut": cell.sut, "item_id": cell.item_id,
        "status": "error", "missing": True, "score": None,
        "error": last_error,
        "attempts": state.attempts_by_cell.get(cell.key, 0),
        "diagnostic_only": cell.diagnostic_only, "scorable": cell.scorable,
    }
    _append(state.run_dir / CHECKPOINT_FILE, checkpoint, state.lock)
    state.completed[cell.key] = checkpoint
    return copy.deepcopy(checkpoint)


def execute(
    manifest: Mapping[str, Any], state: RunState,
    transport: Callable[[Dict[str, Any]], Mapping[str, Any]],
) -> list:
    _require_paid_authorization(manifest)
    run_provider_canaries(manifest, state, transport)
    items = {item.id: item for item in preflight.load_items(str(preflight.BANK_DIR))}
    cells = build_cells(manifest)
    by_sut = {sut: [cell for cell in cells if cell.sut == sut]
              for sut in preflight.SUTS}
    for sut in preflight.SUTS:
        first = by_sut[sut][0]
        outcome = run_cell(
            first, manifest=manifest, state=state, transport=transport,
            items=items, require_reasoning_gate=True)
        if outcome.get("status") != "response" or sut not in state.first_validated:
            if hasattr(state, "run_dir") and hasattr(state, "lock"):
                _terminal(state, "five first real cells did not all PASS", sut=sut)
            raise CustodyStop("five first real cells must all PASS before shards")
    shards = controller.build_sut_shards(preflight.SUTS)

    def shard_worker(shard: Sequence[str]) -> None:
        for sut in shard:
            for cell in by_sut[sut][1:]:
                run_cell(cell, manifest=manifest, state=state,
                         transport=transport, items=items)

    with ThreadPoolExecutor(max_workers=3) as pool:
        list(pool.map(shard_worker, shards))
    return list(state.completed.values())


def _default_transport(api_key: str) -> Callable[[Dict[str, Any]], Mapping[str, Any]]:
    def transport(payload: Dict[str, Any]) -> Mapping[str, Any]:
        request = urllib.request.Request(
            CHAT_URL, data=json.dumps(payload).encode("utf-8"), method="POST",
            headers={"Authorization": f"Bearer {api_key}",
                     "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=180) as response:
                return json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            raise TransportFailure(str(exc)) from exc
    return transport


def _require_sufficient_balance(
    manifest: Mapping[str, Any], api_key: str,
    balance_fetch: Callable[[str], Mapping[str, Any]],
) -> float:
    try:
        required = float((manifest.get("auth_balance") or {})[
            "required_balance_usd"])
        snapshot = balance_fetch(api_key)
        remaining = float(snapshot["limit_remaining"])
    except (KeyError, TypeError, ValueError, OSError) as exc:
        raise CustodyStop("registered OpenRouter balance is unavailable") from exc
    if (not math.isfinite(required) or required <= 0
            or not math.isfinite(remaining) or remaining < required):
        raise CustodyStop("insufficient registered OpenRouter balance")
    return remaining


def main(
    argv: Optional[Sequence[str]] = None, *,
    runtime_fetch: Callable[[], Any] = preflight.fetch_public_catalog,
    balance_fetch: Callable[[str], Mapping[str, Any]] = fetch_key_snapshot,
    transport_factory: Callable[[str], Callable[[Dict[str, Any]], Mapping[str, Any]]] =
        _default_transport,
    execute_fn: Callable[[Mapping[str, Any], RunState,
                          Callable[[Dict[str, Any]], Mapping[str, Any]]], Any] = execute,
) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--go", action="store_true")
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--cap", type=float, required=True)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args(argv)
    if not args.go:
        print("refusing Pilot 2 inference without explicit --go", file=sys.stderr)
        return 2
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        print("OPENROUTER_API_KEY is required at runtime", file=sys.stderr)
        return 2
    try:
        manifest = _load_manifest(args.manifest)
        gate = manifest.get("authorization_gate") or {}
        if gate.get("paid_inference") is not True:
            raise CustodyStop("manifest lacks amount-specific paid authorization")
        proposed = float((manifest.get("planning_cost") or {})["proposed_cap_usd"])
        if args.cap != proposed:
            raise CustodyStop("CLI cap must equal the amount-specific authorized cap")
        catalog, endpoints = runtime_fetch()
        validate_runtime_catalog(manifest, catalog, endpoints)
        _require_sufficient_balance(manifest, key, balance_fetch)
        state = prepare_run(
            args.manifest, args.output_dir, cap_usd=args.cap, resume=args.resume)
        transport = transport_factory(key)
        execute_fn(manifest, state, transport)
    except (CustodyStop, controller.TerminalStop) as exc:
        print(f"Pilot 2 stopped: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
