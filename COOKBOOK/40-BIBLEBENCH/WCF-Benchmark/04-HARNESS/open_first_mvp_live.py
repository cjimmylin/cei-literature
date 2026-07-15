#!/usr/bin/env python3
"""Minimal strict-cap live SUT seam for the Open-First MVP pilot.

The module only collects the six-model response surface.  It does not judge,
score, aggregate, or generate the supplement.  Live execution requires an
explicit ``--go`` and an exact frozen-manifest path.
"""

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

import open_first_mvp_preflight as preflight
import open_first_mvp_run as controller
from wcfbench import mvp


OUTER_CAP_USD = 10.0
MANIFEST_COPY = "open-first-mvp-manifest.json"
IDENTITY_FILE = "run-identity.json"
EVIDENCE_FILE = "raw-evidence.jsonl"
CHECKPOINT_FILE = "checkpoint.jsonl"
CHAT_URL = "https://openrouter.ai/api/v1/chat/completions"
MAX_RETRIES_PER_CELL = 2


class CustodyStop(RuntimeError):
    """The immutable run identity or evidence chain cannot be trusted."""


@dataclass(frozen=True)
class LiveCell:
    sut: str
    item_id: str
    diagnostic_only: bool
    scorable: bool

    @property
    def key(self) -> str:
        return f"{self.sut}::{self.item_id}"


@dataclass
class RunState:
    run_dir: Path
    identity: Dict[str, Any]
    budget: controller.BudgetController
    attempts_by_sut: Dict[str, int] = field(default_factory=dict)
    retry_attempts_by_sut: Dict[str, int] = field(default_factory=dict)
    attempts_by_cell: Dict[str, int] = field(default_factory=dict)
    completed_keys: set = field(default_factory=set)
    first_response_validated: set = field(default_factory=set)
    evidence_lock: threading.Lock = field(default_factory=threading.Lock)
    state_lock: threading.Lock = field(default_factory=threading.Lock)


def _canonical_json(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False).encode("utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_frozen_manifest(path: Path) -> Dict[str, Any]:
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CustodyStop(f"frozen manifest is unreadable: {path}") from exc
    if (not isinstance(value, dict)
            or value.get("validity_label") != preflight.VALIDITY_LABEL
            or tuple(value.get("exact_sut_slugs") or ()) != preflight.SUTS):
        raise CustodyStop("manifest is not the exact Open-First identity")
    schedule = value.get("schedule") or {}
    if (len(schedule.get("all_item_ids") or ()) != 230
            or len(schedule.get("runnable_item_ids") or ()) != 226
            or len(schedule.get("dev_set_only_item_ids") or ()) != 4):
        raise CustodyStop("manifest schedule is not the frozen 230/226/4 geometry")
    if (value.get("concurrency") or {}).get("sut_shards") != 3:
        raise CustodyStop("manifest does not require exactly three SUT shards")
    if (value.get("retry_policy") or {}).get("sut_max_attempts_per_model") != 252:
        raise CustodyStop("manifest retry envelope drifted")
    proposed = (value.get("planning_cost") or {}).get("proposed_cap_usd")
    try:
        proposed = float(proposed)
    except (TypeError, ValueError) as exc:
        raise CustodyStop("manifest proposed cap is missing") from exc
    if not math.isfinite(proposed) or proposed <= 0 or proposed > OUTER_CAP_USD:
        raise CustodyStop("manifest proposed cap exceeds the authorized outer ceiling")
    return value


def build_cells(manifest: Mapping[str, Any]) -> list:
    schedule = manifest.get("schedule") or {}
    all_ids = list(schedule.get("all_item_ids") or ())
    dev_ids = set(schedule.get("dev_set_only_item_ids") or ())
    runnable_ids = set(schedule.get("runnable_item_ids") or ())
    if (len(all_ids) != 230 or len(set(all_ids)) != 230
            or len(dev_ids) != 4 or len(runnable_ids) != 226
            or dev_ids & runnable_ids or set(all_ids) != dev_ids | runnable_ids):
        raise CustodyStop("manifest schedule partitions are inconsistent")
    return [
        LiveCell(sut=sut, item_id=item_id,
                 diagnostic_only=item_id in dev_ids,
                 scorable=item_id in runnable_ids)
        for sut in preflight.SUTS for item_id in all_ids
    ]


def _identity(manifest_path: Path, manifest: Mapping[str, Any], cap_usd: float) -> Dict[str, Any]:
    return {
        "schema_version": 1,
        "kind": "open_first_mvp_live_sut_execution",
        "validity_label": preflight.VALIDITY_LABEL,
        "manifest_sha256": sha256_file(manifest_path),
        "catalog_hash": manifest.get("catalog_hash"),
        "suts": list(preflight.SUTS),
        "expected_cells": 1380,
        "scorable_cells": 1356,
        "diagnostic_only_cells": 24,
        "cap_usd": cap_usd,
        "retry_policy": copy.deepcopy(manifest.get("retry_policy") or {}),
        "concurrency": copy.deepcopy(manifest.get("concurrency") or {}),
    }


def _write_json_new(path: Path, value: Mapping[str, Any]) -> None:
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True, ensure_ascii=False)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())


def _append_jsonl(path: Path, value: Mapping[str, Any], lock: threading.Lock) -> None:
    encoded = json.dumps(value, sort_keys=True, ensure_ascii=False) + "\n"
    with lock:
        with path.open("a", encoding="utf-8") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())


def _read_jsonl(path: Path) -> list:
    if not path.exists():
        return []
    rows = []
    try:
        with path.open(encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    rows.append(json.loads(line))
    except (OSError, json.JSONDecodeError) as exc:
        raise CustodyStop(f"malformed immutable JSONL evidence: {path}") from exc
    return rows


def prepare_run(manifest_path: Path, run_dir: Path, *, cap_usd: float,
                resume: bool, allow_test_cap: bool = False) -> RunState:
    manifest_path = Path(manifest_path).resolve()
    run_dir = Path(run_dir).resolve()
    manifest = load_frozen_manifest(manifest_path)
    proposed = float(manifest["planning_cost"]["proposed_cap_usd"])
    if (not math.isfinite(cap_usd) or cap_usd <= 0 or cap_usd > OUTER_CAP_USD
            or (cap_usd < proposed and not allow_test_cap)
            or cap_usd > proposed):
        raise CustodyStop(
            f"cap must equal the frozen proposed cap ${proposed:.2f} and not exceed $10")
    expected = _identity(manifest_path, manifest, cap_usd)
    if resume:
        if not run_dir.is_dir():
            raise CustodyStop("resume run directory does not exist")
        try:
            observed = json.loads((run_dir / IDENTITY_FILE).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise CustodyStop("resume identity is missing or malformed") from exc
        if observed != expected:
            raise CustodyStop("resume identity does not match immutable run identity")
        if sha256_file(run_dir / MANIFEST_COPY) != expected["manifest_sha256"]:
            raise CustodyStop("resume manifest copy does not match immutable identity")
    else:
        if run_dir.exists():
            raise CustodyStop("new immutable run directory already exists")
        run_dir.mkdir(parents=True)
        with manifest_path.open("rb") as source, (run_dir / MANIFEST_COPY).open("xb") as sink:
            sink.write(source.read())
            sink.flush()
            os.fsync(sink.fileno())
        _write_json_new(run_dir / IDENTITY_FILE, expected)

    evidence = _read_jsonl(run_dir / EVIDENCE_FILE)
    checkpoints = _read_jsonl(run_dir / CHECKPOINT_FILE)
    if any(row.get("kind") == "terminal_stop" for row in evidence):
        raise CustodyStop("resume evidence records a terminal stop")
    if any(row.get("kind") == "sut_transport_error"
           and row.get("response_attributed_cost_usd") is None for row in evidence):
        raise CustodyStop("resume evidence contains an unaccounted transport attempt")
    response_rows = [row for row in evidence if row.get("kind") == "sut_response"]
    if any(row.get("response_attributed_cost_usd") is None for row in response_rows):
        raise CustodyStop("resume evidence contains unaccounted response cost")
    spent = sum(float(row["response_attributed_cost_usd"]) for row in response_rows)
    checkpoint_keys = {row["cell_key"] for row in checkpoints
                       if row.get("status") in {"response", "error"}}
    state = RunState(
        run_dir=run_dir, identity=expected,
        budget=controller.BudgetController(cap_usd=cap_usd, spent_usd=spent),
        attempts_by_sut={sut: 0 for sut in preflight.SUTS},
        retry_attempts_by_sut={sut: 0 for sut in preflight.SUTS},
        completed_keys=checkpoint_keys,
    )
    for row in response_rows:
        sut = row.get("sut")
        if sut not in state.attempts_by_sut:
            raise CustodyStop("resume evidence contains an unknown SUT")
        state.attempts_by_sut[sut] += 1
        cell_key = row.get("cell_key")
        attempt = row.get("cell_attempt")
        if not isinstance(cell_key, str) or not isinstance(attempt, int) or attempt < 1:
            raise CustodyStop("resume response has malformed attempt identity")
        state.attempts_by_cell[cell_key] = max(
            state.attempts_by_cell.get(cell_key, 0), attempt)
        if attempt > 1:
            state.retry_attempts_by_sut[sut] += 1
    for row in evidence:
        if row.get("kind") == "first_response_validation" and row.get("status") == "PASS":
            sut = row.get("sut")
            if sut not in state.attempts_by_sut:
                raise CustodyStop("resume validation contains an unknown SUT")
            state.first_response_validated.add(sut)
    if (any(count > 252 for count in state.attempts_by_sut.values())
            or any(count > 22 for count in state.retry_attempts_by_sut.values())):
        raise CustodyStop("resume evidence exceeds the registered retry envelope")
    request_rows = [row for row in evidence if row.get("kind") == "sut_request"]
    orphan_responses = {}
    for row in response_rows:
        cell_key = row["cell_key"]
        if cell_key in checkpoint_keys:
            continue
        orphan_responses.setdefault(cell_key, []).append(row)
    for cell_key, rows in orphan_responses.items():
        successful = []
        for row in rows:
            raw_response = row.get("raw_response")
            if not isinstance(raw_response, Mapping):
                raise CustodyStop("resume response contains malformed raw evidence")
            if raw_response.get("error"):
                raise CustodyStop("resume response contains errored raw evidence")
            try:
                raw_cost = _response_cost(raw_response)
                recorded_cost = float(row["response_attributed_cost_usd"])
            except (KeyError, TypeError, ValueError,
                    controller.TerminalStop) as exc:
                raise CustodyStop(
                    "resume response contains malformed cost evidence") from exc
            try:
                content = _response_content(raw_response)
            except ValueError as exc:
                raise CustodyStop(
                    "resume response contains malformed raw evidence") from exc
            if raw_cost != recorded_cost:
                raise CustodyStop("resume response cost does not match raw evidence")
            successful.append((row, content, recorded_cost))
        if not successful:
            continue
        if len(successful) != 1 or successful[0][0] is not rows[-1]:
            raise CustodyStop("resume evidence contains ambiguous successful responses")
        response_row, content, recorded_cost = successful[0]
        identity_fields = (
            "cell_key", "sut", "item_id", "diagnostic_only", "scorable",
            "cell_attempt", "model_attempt")
        if (not all(field in response_row for field in identity_fields)
                or not isinstance(response_row["cell_key"], str)
                or not isinstance(response_row["sut"], str)
                or not isinstance(response_row["item_id"], str)
                or not isinstance(response_row["diagnostic_only"], bool)
                or not isinstance(response_row["scorable"], bool)
                or not isinstance(response_row["cell_attempt"], int)
                or isinstance(response_row["cell_attempt"], bool)
                or response_row["cell_attempt"] < 1
                or not isinstance(response_row["model_attempt"], int)
                or isinstance(response_row["model_attempt"], bool)
                or response_row["model_attempt"] < 1):
            raise CustodyStop("resume response has malformed persisted identity")
        matching_requests = []
        same_cell_requests = []
        for request in request_rows:
            if (not all(field in request for field in identity_fields)
                    or not isinstance(request["cell_key"], str)
                    or not isinstance(request["sut"], str)
                    or not isinstance(request["item_id"], str)
                    or not isinstance(request["diagnostic_only"], bool)
                    or not isinstance(request["scorable"], bool)
                    or not isinstance(request["cell_attempt"], int)
                    or isinstance(request["cell_attempt"], bool)
                    or request["cell_attempt"] < 1
                    or not isinstance(request["model_attempt"], int)
                    or isinstance(request["model_attempt"], bool)
                    or request["model_attempt"] < 1):
                raise CustodyStop("resume request has malformed persisted identity")
            if request["cell_key"] == cell_key:
                same_cell_requests.append(request)
            if all(request[field] == response_row[field]
                   for field in identity_fields):
                matching_requests.append(request)
        if len(matching_requests) != 1:
            raise CustodyStop("resume response lacks an unambiguous persisted request")
        if same_cell_requests != matching_requests:
            raise CustodyStop("resume evidence contains an additional same-cell request")
        if response_row["sut"] not in state.first_response_validated:
            raise CustodyStop("resume response lacks first-response PASS custody")
        _append_jsonl(run_dir / CHECKPOINT_FILE, {
            "schema_version": 1, "cell_key": cell_key,
            "sut": response_row["sut"], "item_id": response_row["item_id"],
            "status": "response", "response": content,
            "diagnostic_only": response_row["diagnostic_only"],
            "scorable": response_row["scorable"],
            "response_attributed_cost_usd": recorded_cost,
            "attempts_for_cell": response_row["cell_attempt"],
        }, state.evidence_lock)
        state.completed_keys.add(cell_key)
    return state


def maximum_attempt_cost(model_row: Mapping[str, Any], manifest: Mapping[str, Any]) -> float:
    prices = model_row.get("prices") or {}
    ceiling = (manifest.get("rendered_prompt_ceilings") or {}).get("sut") or {}
    try:
        value = (float(prices["prompt"]) * int(ceiling["prompt_tokens"])
                 + float(prices["completion"]) * int(ceiling["completion_tokens"]))
    except (KeyError, TypeError, ValueError) as exc:
        raise controller.TerminalStop("maximum reservation cannot be derived") from exc
    if not math.isfinite(value) or value <= 0:
        raise controller.TerminalStop("maximum reservation is invalid")
    return value


def _blind_messages(item: Any) -> list:
    # The frozen preflight measures EPISODE directly from its already-blind stem;
    # all other routes use the common examinee prompt builder.
    if preflight.scorer_kind(item) == "episode":
        return [{"role": "user", "content": item.stem}]
    return controller.build_blind_messages(item)


def _response_cost(response: Mapping[str, Any]) -> float:
    try:
        raw = (response.get("usage") or {})["cost"]
        value = float(raw)
    except (KeyError, TypeError, ValueError) as exc:
        raise controller.TerminalStop(
            "response-attributed cost is missing or malformed") from exc
    if not math.isfinite(value) or value < 0:
        raise controller.TerminalStop("response-attributed cost is missing or malformed")
    return value


def _response_content(response: Mapping[str, Any]) -> str:
    try:
        value = response["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise ValueError("malformed response content") from exc
    if not isinstance(value, str):
        raise ValueError("malformed response content")
    return value


def run_cell(cell: LiveCell, *, manifest: Mapping[str, Any], state: RunState,
             transport: Callable[[Dict[str, Any]], Mapping[str, Any]],
             _items: Optional[Mapping[str, Any]] = None) -> Dict[str, Any]:
    if cell.key in state.completed_keys:
        raise CustodyStop(f"completed cell cannot be rerun: {cell.key}")
    items = dict(_items or {
        item.id: item for item in preflight.load_items(str(preflight.BANK_DIR))})
    if cell.item_id not in items:
        raise CustodyStop(f"cell item is outside frozen bank: {cell.item_id}")
    model_row = next((row for row in manifest.get("models") or ()
                      if row.get("slug") == cell.sut), None)
    if model_row is None:
        raise CustodyStop(f"cell SUT is outside frozen manifest: {cell.sut}")
    payload = controller.build_sut_request(
        manifest, cell.sut, _blind_messages(items[cell.item_id]))
    maximum = maximum_attempt_cost(model_row, manifest)
    retry_policy = manifest.get("retry_policy") or {}
    retry_reserve = int(retry_policy.get("sut_reserved_retries_per_model", -1))
    max_model_attempts = int(retry_policy.get("sut_max_attempts_per_model", -1))
    if (retry_reserve != 22 or max_model_attempts != 252):
        raise CustodyStop("registered SUT retry policy drifted")
    final_error = None

    prior_attempts = state.attempts_by_cell.get(cell.key, 0)
    for cell_attempt in range(prior_attempts + 1, MAX_RETRIES_PER_CELL + 2):
        with state.state_lock:
            if (cell_attempt > 1
                    and state.retry_attempts_by_sut[cell.sut] >= retry_reserve):
                final_error = "registered model retry reserve exhausted"
                break
            if state.attempts_by_sut[cell.sut] >= max_model_attempts:
                final_error = "registered model retry envelope exhausted"
                break
            reservation = state.budget.reserve(maximum)
            state.attempts_by_sut[cell.sut] += 1
            if cell_attempt > 1:
                state.retry_attempts_by_sut[cell.sut] += 1
            state.attempts_by_cell[cell.key] = cell_attempt
            model_attempt = state.attempts_by_sut[cell.sut]
        request_record = {
            "schema_version": 1, "kind": "sut_request", "cell_key": cell.key,
            "sut": cell.sut, "item_id": cell.item_id,
            "diagnostic_only": cell.diagnostic_only, "scorable": cell.scorable,
            "cell_attempt": cell_attempt, "model_attempt": model_attempt,
            "maximum_reserved_cost_usd": maximum, "request": payload,
        }
        _append_jsonl(state.run_dir / EVIDENCE_FILE, request_record, state.evidence_lock)
        try:
            raw = transport(copy.deepcopy(payload))
            if not isinstance(raw, Mapping):
                raise TypeError("transport response is not an object")
            response = copy.deepcopy(dict(raw))
        except Exception as exc:
            _append_jsonl(state.run_dir / EVIDENCE_FILE, {
                "schema_version": 1, "kind": "sut_transport_error",
                "cell_key": cell.key, "sut": cell.sut, "item_id": cell.item_id,
                "cell_attempt": cell_attempt, "model_attempt": model_attempt,
                "response_attributed_cost_usd": None,
                "error_type": type(exc).__name__, "error": str(exc),
            }, state.evidence_lock)
            raise controller.TerminalStop(
                "transport failed without enforceable response-attributed cost") from exc

        try:
            actual = _response_cost(response)
        except controller.TerminalStop:
            _append_jsonl(state.run_dir / EVIDENCE_FILE, {
                "schema_version": 1, "kind": "sut_response", "cell_key": cell.key,
                "sut": cell.sut, "item_id": cell.item_id,
                "cell_attempt": cell_attempt, "model_attempt": model_attempt,
                "response_attributed_cost_usd": None, "raw_response": response,
            }, state.evidence_lock)
            raise
        response_record = {
            "schema_version": 1, "kind": "sut_response", "cell_key": cell.key,
            "sut": cell.sut, "item_id": cell.item_id,
            "diagnostic_only": cell.diagnostic_only, "scorable": cell.scorable,
            "cell_attempt": cell_attempt, "model_attempt": model_attempt,
            "response_attributed_cost_usd": actual, "raw_response": response,
            "first_response_validated": False,
        }
        _append_jsonl(state.run_dir / EVIDENCE_FILE, response_record, state.evidence_lock)
        state.budget.settle(reservation, actual)

        with state.state_lock:
            is_first = cell.sut not in state.first_response_validated
            if is_first:
                try:
                    controller.validate_first_live_cell(response)
                except controller.TerminalStop as exc:
                    _append_jsonl(state.run_dir / EVIDENCE_FILE, {
                        "schema_version": 1, "kind": "terminal_stop",
                        "cell_key": cell.key, "sut": cell.sut,
                        "reason": str(exc),
                    }, state.evidence_lock)
                    raise
                state.first_response_validated.add(cell.sut)
                response_record["first_response_validated"] = True
                # The append-only marker records the guard result after the raw response.
                _append_jsonl(state.run_dir / EVIDENCE_FILE, {
                    "schema_version": 1, "kind": "first_response_validation",
                    "cell_key": cell.key, "sut": cell.sut,
                    "response_attributed_cost_usd": 0.0, "status": "PASS",
                }, state.evidence_lock)

        if response.get("error"):
            final_error = f"OpenRouter error: {response['error']}"
        else:
            try:
                content = _response_content(response)
            except ValueError as exc:
                final_error = str(exc)
            else:
                record = {
                    "schema_version": 1, "cell_key": cell.key, "sut": cell.sut,
                    "item_id": cell.item_id, "status": "response", "response": content,
                    "diagnostic_only": cell.diagnostic_only, "scorable": cell.scorable,
                    "response_attributed_cost_usd": actual,
                    "attempts_for_cell": cell_attempt,
                }
                _append_jsonl(state.run_dir / CHECKPOINT_FILE, record, state.evidence_lock)
                with state.state_lock:
                    state.completed_keys.add(cell.key)
                return record

    record = {
        "schema_version": 1, "cell_key": cell.key, "sut": cell.sut,
        "item_id": cell.item_id, "status": "error", "error": final_error,
        "score": None, "missing": True, "diagnostic_only": cell.diagnostic_only,
        "scorable": cell.scorable,
    }
    _append_jsonl(state.run_dir / CHECKPOINT_FILE, record, state.evidence_lock)
    with state.state_lock:
        state.completed_keys.add(cell.key)
    return record


def execute(manifest: Mapping[str, Any], state: RunState,
            transport: Callable[[Dict[str, Any]], Mapping[str, Any]]) -> list:
    cells = build_cells(manifest)
    items = {item.id: item for item in preflight.load_items(str(preflight.BANK_DIR))}
    by_sut = {sut: [cell for cell in cells if cell.sut == sut]
              for sut in preflight.SUTS}
    cancellation = threading.Event()

    def worker(shard: Sequence[str]) -> list:
        output = []
        for sut in shard:
            for cell in by_sut[sut]:
                if cancellation.is_set():
                    return output
                if cell.key in state.completed_keys:
                    continue
                try:
                    output.append(run_cell(
                        cell, manifest=manifest, state=state, transport=transport,
                        _items=items))
                except Exception:
                    cancellation.set()
                    raise
        return output

    shards = controller.build_sut_shards(preflight.SUTS)
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = [pool.submit(worker, shard) for shard in shards]
        return [row for future in futures for row in future.result()]


def _default_transport_factory(api_key: str) -> Callable[[Dict[str, Any]], Mapping[str, Any]]:
    if not api_key:
        raise CustodyStop("OPENROUTER_API_KEY is required for live execution")

    def post(payload: Dict[str, Any]) -> Mapping[str, Any]:
        request = urllib.request.Request(
            CHAT_URL, data=json.dumps(payload).encode("utf-8"), method="POST",
            headers={"Authorization": f"Bearer {api_key}",
                     "Content-Type": "application/json",
                     "HTTP-Referer": "https://github.com/cjimmylin/cei-literature",
                     "X-Title": "WCF-Bench Open-First MVP"})
        try:
            with urllib.request.urlopen(request, timeout=180) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            try:
                return json.loads(body)
            except json.JSONDecodeError:
                raise RuntimeError(f"OpenRouter HTTP {exc.code} without JSON custody") from exc

    return post


def main(argv: Optional[Sequence[str]] = None, *,
         catalog_fetch: Callable[[], Mapping[str, Mapping[str, Any]]] =
         lambda: mvp.fetch_model_catalog(None),
         transport_factory: Callable[[str], Callable[[Dict[str, Any]], Mapping[str, Any]]] =
         _default_transport_factory,
         execute_fn: Callable[[Mapping[str, Any], RunState,
                               Callable[[Dict[str, Any]], Mapping[str, Any]]], list] =
         execute) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--go", action="store_true")
    parser.add_argument("--manifest")
    parser.add_argument("--output-dir")
    parser.add_argument("--cap", type=float)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args(argv)
    if not args.go:
        print("Open-First MVP live SUT seam — DRY ONLY; pass --go explicitly")
        return 0
    try:
        if not args.manifest or not args.output_dir or args.cap is None:
            raise CustodyStop("--go requires --manifest, --output-dir, and --cap")
        manifest_path = Path(args.manifest)
        manifest = load_frozen_manifest(manifest_path)
        proposed = float(manifest["planning_cost"]["proposed_cap_usd"])
        if args.cap != proposed or args.cap > OUTER_CAP_USD:
            raise CustodyStop(
                f"--cap must equal frozen ${proposed:.2f} and remain <= $10")
        catalog = dict(catalog_fetch())
        controller.validate_runtime_catalog(manifest, catalog)
        state = prepare_run(
            manifest_path, Path(args.output_dir), cap_usd=args.cap,
            resume=args.resume)
        transport = transport_factory(os.environ.get("OPENROUTER_API_KEY", ""))
        execute_fn(manifest, state, transport)
        return 0
    except Exception as exc:
        print(f"ERROR: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
