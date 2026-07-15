"""Resumable OPEN6-SOL1 single-judge execution with exact missingness.

This layer is descriptive only: it has no two-judge, adjudication, gate,
release, or cross-design aggregation path.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from pathlib import Path

from .executors import AdministrationResult, ItemExecution, TurnResult, permuted_order
from .manifest import FIXED_PERMUTATION_SEEDS
from .open6_sol1 import canonical_json_bytes, select_public_items
from .open6_sol1_judge import (
    JudgeBatch, JudgeRequest, ScoringUnit, batch_scoring_units,
    build_judge_request, build_scoring_units, execute_judge_batch,
    reassemble_single_judge_verdict, scores_by_unit, validate_judge_result,
)
from .open6_sol1_run import (
    AppendOnlyStore, EXECUTION_NAME, execution_from_dict,
    load_execution_records, prepare_run, TERMINAL_UNRESOLVED_NAME,
    _validate_terminal_unresolved_record,
)
from .open6_sol1_runtime import (
    BudgetStop, ContractStop, MAX_CONCURRENCY, SOL_FAILURES, ThreadStop,
)


JUDGE_PLAN_NAME = "sol-judge-batch-plan.jsonl"
JUDGE_ATTEMPT_CUSTODY_NAME = "sol-judge-attempt-custody.jsonl"
JUDGE_RESULT_NAME = "sol-judge-batch-results.jsonl"
JUDGE_UNRESOLVED_NAME = "sol-judge-unresolved-batches.jsonl"
JUDGE_STOP_CHECKPOINT_NAME = "sol-judge-stop-checkpoints.jsonl"
SINGLE_JUDGE_VERDICT_NAME = "sol-single-judge-verdicts.jsonl"
TERMINAL_UNRESOLVED_SUT_NAME = TERMINAL_UNRESOLVED_NAME

EXPECTED_EXECUTION_RECORDS = 2_064
EXPECTED_UNITS = 5_370
EXPECTED_CATEGORY_CELLS = 10_008
EXPECTED_BATCHES = 227

_STORE_METADATA = {
    "store_kind", "sequence", "previous_sha256", "record_sha256",
}

_QUOTA_OR_USAGE_PATTERNS = tuple(re.compile(pattern, re.IGNORECASE) for pattern in (
    r"\boauth\s+usage[\s_-]+limit\b",
    r"\busage[\s_-]+limit(?:\s+(?:reached|exceeded|exhausted))?\b",
    r"\bquota\s+(?:reached|exceeded|exhausted|depleted)\b",
    r"\binsufficient\s+(?:quota|credits?)\b",
    r"\bcredits?\s+(?:exhausted|depleted)\b",
))
_SOL_TURN_OR_REPLAY_CAPS = frozenset({
    "Sol replay reserve exhausted",
    "Sol attempt cap exhausted",
    "Sol planned call cap exhausted",
    "Sol turn cap exhausted",
})


class JudgeRunStop(ThreadStop):
    """A non-key-local Sol failure that stops the resumable judge run."""

    def __init__(self, reason_code, stopped_batch_key):
        self.reason_code = reason_code
        self.stopped_batch_key = stopped_batch_key
        super().__init__(
            f"Sol judge stopped for {reason_code} at {stopped_batch_key}")


def _hash(value) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def _text_hash(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _payload(record):
    return {key: copy.deepcopy(value) for key, value in record.items()
            if key not in _STORE_METADATA}


def _unit_payload(unit: ScoringUnit, *, include_prompt=True) -> dict:
    return {
        "unit_key": unit.unit_key,
        "record_key": unit.record_key,
        "design": unit.design,
        "item_id": unit.item_id,
        "unit_kind": unit.unit_kind,
        "locator": unit.locator_dict,
        "category_names": list(unit.category_names),
        "score_schema_sha256": unit.score_schema_sha256,
        "rubric_and_response": (
            unit.rubric_and_response if include_prompt else None),
    }


def _request_payload(request: JudgeRequest) -> dict:
    return {
        "logical_key": request.logical_key,
        "batch_id": request.batch_id,
        "design": request.design,
        "prompt": request.prompt,
        "schema": copy.deepcopy(request.schema),
        "expected_unit_keys": list(request.expected_unit_keys),
        "score_schema": copy.deepcopy(request.score_schema),
    }


def _batch_plan_payload(batch: JudgeBatch, request, available_by_key=None) -> dict:
    if available_by_key is None:
        available_by_key = {unit.unit_key: unit for unit in batch.units}
    request_payload = _request_payload(request) if request is not None else None
    available_keys = set(available_by_key)
    return {
        "logical_key": "sol:judge:" + batch.batch_id,
        "batch_id": batch.batch_id,
        "design": batch.design,
        "score_schema_sha256": batch.score_schema_sha256,
        "request_sha256": (
            _hash(request_payload) if request_payload is not None else None),
        "request": request_payload,
        "units": [
            _unit_payload(
                available_by_key.get(unit.unit_key, unit),
                include_prompt=unit.unit_key in available_keys)
            for unit in batch.units
        ],
        "unit_keys": [unit.unit_key for unit in batch.units],
        "available_unit_keys": [
            unit.unit_key for unit in batch.units
            if unit.unit_key in available_keys],
        "upstream_missing_unit_keys": [
            unit.unit_key for unit in batch.units
            if unit.unit_key not in available_keys],
        "category_cells": sum(len(unit.category_names) for unit in batch.units),
        "upstream_missing_category_cells": sum(
            len(unit.category_names) for unit in batch.units
            if unit.unit_key not in available_keys),
    }


def _topology_execution(item, model):
    labels = [admin.label for admin in item.administrations]
    axis = {
        "03-quiettongue": "twin_order", "08-vocationfork": "twin_order",
        "04-innerweight": "variant_order", "10-strangergate": "variant_order",
        "09-doubleedge": "seat_order", "05-ordoamoris": "claimant_order",
    }.get(item.design, "twin_order")
    order = (permuted_order(
        labels, FIXED_PERMUTATION_SEEDS.get(axis, 0), item.id)
        if item.order_permuted or item.isolation_required else labels)
    by_label = {admin.label: admin for admin in item.administrations}
    administrations = []
    for label in order:
        source = by_label[label]
        turns = []
        for turn in source.turns:
            state = next(iter(turn.branches)) if turn.branches else None
            text = turn.branches[state] if state is not None else (turn.text or "")
            turns.append(TurnResult(
                index=turn.index, user_text=text,
                response="[UPSTREAM SUT RESPONSE UNAVAILABLE]",
                branch_state=state,
            ))
        administrations.append(AdministrationResult(
            label=source.label, kind=source.kind, system=source.system,
            turns=turns,
            terminal_response=(
                "[UPSTREAM SUT RESPONSE UNAVAILABLE]"
                if source.terminal_ask else None),
            terminal_user_text=source.terminal_ask,
        ))
    return ItemExecution(
        item_id=item.id, design=item.design, model=model, order=order,
        administrations=administrations,
        isolation_used=item.isolation_required,
    )


def _load_terminal_unresolved(run_dir, expected_keys, items_by_id, models):
    store = AppendOnlyStore(
        Path(run_dir) / TERMINAL_UNRESOLVED_SUT_NAME,
        "terminal-unresolved-sut")
    rows = store.records()
    allowed_models = set(models)
    result = {}
    for stored in rows:
        logical_key = stored.get("logical_key")
        item = items_by_id.get(stored.get("item_id"))
        if logical_key not in expected_keys or item is None:
            raise ContractStop("invalid terminal-unresolved SUT custody")
        result[logical_key] = _validate_terminal_unresolved_record(
            stored, item, allowed_models)
    return result


def _derive_surface(benchmark_root, manifest_path, run_dir):
    manifest = prepare_run(benchmark_root, manifest_path, run_dir)
    items = select_public_items(benchmark_root)
    items_by_id = {item.id: item for item in items}
    models = [row["slug"] for row in manifest["openrouter"]["models"]]
    records = load_execution_records(
        Path(run_dir) / EXECUTION_NAME, benchmark_root, manifest_path)
    expected_keys = {
        f"item:{model}:{item.id}" for model in models for item in items
    }
    by_key = {record["logical_key"]: record for record in records}
    terminal_unresolved = _load_terminal_unresolved(
        run_dir, expected_keys, items_by_id, models)
    if (len(by_key) != len(records) or set(by_key) & set(terminal_unresolved)
            or set(by_key) | set(terminal_unresolved) != expected_keys):
        raise ContractStop(
            "OPEN6-SOL1 judging requires exactly 2,064 execution-or-"
            "terminal-unresolved keys")

    namespace = hashlib.sha256(
        (Path(run_dir) / "manifest.json").read_bytes()).hexdigest()
    expected_units = []
    available_by_unit_key = {}
    upstream_missing_unit_keys = set()
    source_records = {}
    units_by_record = {}
    for logical_key in sorted(expected_keys):
        if logical_key in by_key:
            record = by_key[logical_key]
            model = record["model"]
            item = items_by_id[record["item_id"]]
        else:
            unresolved = terminal_unresolved[logical_key]
            model = unresolved["model"]
            item = items_by_id[unresolved["item_id"]]
        topology_units = build_scoring_units(
            item, _topology_execution(item, model), model, namespace)
        if not topology_units:
            raise ContractStop(f"execution produced no judge units: {logical_key}")
        record_key = topology_units[0].record_key
        if record_key in source_records:
            raise ContractStop("duplicate opaque judge record key")
        source_records[record_key] = {
            "logical_key": logical_key, "item": item, "item_id": item.id,
            "design": item.design, "model": model,
            "upstream_terminal_unresolved": logical_key in terminal_unresolved,
        }
        units_by_record[record_key] = tuple(topology_units)
        expected_units.extend(topology_units)
        if logical_key in by_key:
            available_units = build_scoring_units(
                item, execution_from_dict(by_key[logical_key]["execution"]),
                model, namespace)
            if ([unit.unit_key for unit in available_units]
                    != [unit.unit_key for unit in topology_units]):
                raise ContractStop("available execution changes registered topology")
            available_by_unit_key.update(
                {unit.unit_key: unit for unit in available_units})
        else:
            upstream_missing_unit_keys.update(
                unit.unit_key for unit in topology_units)

    batches = batch_scoring_units(expected_units)
    requests = []
    plan_payloads = []
    for batch in batches:
        available = tuple(
            available_by_unit_key[unit.unit_key]
            for unit in batch.units if unit.unit_key in available_by_unit_key)
        request = None
        if available:
            request = build_judge_request(JudgeBatch(
                batch.batch_id, batch.design, batch.score_schema_sha256,
                available))
            requests.append(request)
        plan_payloads.append(_batch_plan_payload(
            batch, request, available_by_unit_key))
    category_cells = sum(len(unit.category_names) for unit in expected_units)
    if (len(expected_units) != EXPECTED_UNITS
            or category_cells != EXPECTED_CATEGORY_CELLS
            or len(batches) != EXPECTED_BATCHES
            or len({unit.unit_key for unit in expected_units}) != EXPECTED_UNITS
            or len({batch.batch_id for batch in batches}) != EXPECTED_BATCHES):
        raise ContractStop("OPEN6-SOL1 judge geometry differs from registration")
    return {
        "manifest": manifest,
        "records": records,
        "terminal_unresolved": terminal_unresolved,
        "source_records": source_records,
        "units_by_record": units_by_record,
        "upstream_missing_unit_keys": frozenset(upstream_missing_unit_keys),
        "batches": tuple(batches),
        "requests": tuple(requests),
        "plan_payloads": tuple(plan_payloads),
    }


def _plan_store(run_dir):
    return AppendOnlyStore(Path(run_dir) / JUDGE_PLAN_NAME, "sol-judge-batch-plan")


def _attempt_store(run_dir):
    return AppendOnlyStore(
        Path(run_dir) / JUDGE_ATTEMPT_CUSTODY_NAME,
        "sol-judge-attempt-custody", key_field="attempt_id")


def _result_store(run_dir):
    return AppendOnlyStore(
        Path(run_dir) / JUDGE_RESULT_NAME, "sol-judge-batch-results")


def _unresolved_store(run_dir):
    return AppendOnlyStore(
        Path(run_dir) / JUDGE_UNRESOLVED_NAME,
        "sol-judge-unresolved-batches")


def _stop_store(run_dir):
    return AppendOnlyStore(
        Path(run_dir) / JUDGE_STOP_CHECKPOINT_NAME,
        "sol-judge-stop-checkpoints", key_field="checkpoint_id")


def _verdict_store(run_dir):
    return AppendOnlyStore(
        Path(run_dir) / SINGLE_JUDGE_VERDICT_NAME,
        "sol-single-judge-verdicts")


def _append_or_validate(store, payloads):
    expected = {payload["logical_key"]: payload for payload in payloads}
    existing = store.by_key()
    if set(existing) - set(expected):
        raise ContractStop(f"{store.store_kind} contains an unregistered key")
    for logical_key, payload in expected.items():
        present = existing.get(logical_key)
        if present is None:
            store.append(payload)
        elif _payload(present) != payload:
            raise ContractStop(f"{store.store_kind} contract mismatch: {logical_key}")


def prepare_judge_plan(benchmark_root, manifest_path, run_dir) -> dict:
    """Materialize or validate the complete deterministic 227-batch plan."""
    surface = _derive_surface(benchmark_root, manifest_path, run_dir)
    payloads = list(surface["plan_payloads"])
    _append_or_validate(_plan_store(run_dir), payloads)
    sizes = [len(payload["unit_keys"]) for payload in payloads]
    missing_units = sum(
        len(payload["upstream_missing_unit_keys"]) for payload in payloads)
    missing_cells = sum(
        payload["upstream_missing_category_cells"] for payload in payloads)
    return {
        "execution_records": len(surface["records"]),
        "units": sum(sizes),
        "category_cells": sum(payload["category_cells"] for payload in payloads),
        "batches": len(payloads),
        "batch_sizes": sizes,
        "expected_execution_records": EXPECTED_EXECUTION_RECORDS,
        "available_execution_records": len(surface["records"]),
        "upstream_missing_execution_records": len(
            surface["terminal_unresolved"]),
        "expected_units": EXPECTED_UNITS,
        "upstream_missing_units": missing_units,
        "expected_category_cells": EXPECTED_CATEGORY_CELLS,
        "upstream_missing_category_cells": missing_cells,
        "expected_batches": EXPECTED_BATCHES,
        "planned_judge_batches": len(surface["requests"]),
    }


def load_batch_plan(run_dir):
    return _plan_store(run_dir).records()


def load_attempt_custody(run_dir):
    return _attempt_store(run_dir).records()


def load_unresolved_batches(run_dir):
    return _unresolved_store(run_dir).records()


def load_stop_checkpoints(run_dir):
    return _stop_store(run_dir).records()


def load_single_judge_verdicts(run_dir):
    return _verdict_store(run_dir).records()


def _validated_attempt_groups(surface, run_dir):
    requests = {request.logical_key: request for request in surface["requests"]}
    groups = {}
    for stored in _attempt_store(run_dir).records():
        row = _payload(stored)
        logical_key = row.get("logical_key")
        request = requests.get(logical_key)
        if request is None:
            raise ContractStop("judge attempt custody contains an unregistered key")
        final_text = row.get("final_text")
        trace_text = row.get("trace_jsonl")
        if (not isinstance(final_text, str) or not isinstance(trace_text, str)
                or row.get("prompt") != request.prompt
                or row.get("schema") != request.schema
                or row.get("payload_sha256") != _text_hash(request.prompt)
                or row.get("schema_sha256") != _hash(request.schema)
                or row.get("trace_sha256") != _text_hash(trace_text)
                or row.get("response_sha256")
                != (_text_hash(final_text) if final_text else None)):
            raise ContractStop("judge attempt custody hash/request mismatch")
        groups.setdefault(logical_key, []).append(stored)
    for logical_key, rows in groups.items():
        rows.sort(key=lambda row: row["attempt_id"])
        if not 1 <= len(rows) <= 2:
            raise ContractStop("judge attempt custody exceeds one replay")
        if len({row["attempt_id"] for row in rows}) != len(rows):
            raise ContractStop("judge attempt custody repeats an attempt id")
    return groups


def _terminal_attempt_link(row, request, groups, *, unresolved):
    attempts = groups.get(request.logical_key, [])
    ids = [attempt["attempt_id"] for attempt in attempts]
    hashes = [attempt["record_sha256"] for attempt in attempts]
    recovered = row.get("recovered_interrupted_attempt_ids", [])
    if (row.get("attempt_ids") != ids
            or row.get("attempt_record_sha256") != hashes
            or not isinstance(recovered, list)
            or not set(recovered).issubset(ids)):
        return False
    if unresolved:
        return (len(attempts) == 2
                and all(attempt.get("error_class") is not None
                        or attempt["attempt_id"] in recovered
                        for attempt in attempts))
    if not attempts or attempts[-1].get("error_class") is not None:
        return False
    try:
        value = json.loads(attempts[-1]["final_text"])
    except (json.JSONDecodeError, TypeError):
        return False
    return (validate_judge_result(request, value)
            and value == row.get("value")
            and all(attempt.get("error_class") is not None
                    or attempt["attempt_id"] in recovered
                    for attempt in attempts[:-1]))


def _request_category_cells(plan, request):
    expected = list(request.expected_unit_keys)
    if plan.get("available_unit_keys") != expected:
        raise ContractStop("judge request differs from available batch plan")
    by_key = {unit["unit_key"]: unit for unit in plan["units"]}
    if len(by_key) != len(plan["units"]) or any(key not in by_key for key in expected):
        raise ContractStop("judge plan has invalid available-unit geometry")
    return sum(len(by_key[key]["category_names"]) for key in expected)


def _validate_terminal_stores(surface, run_dir):
    plans = {payload["logical_key"]: payload
             for payload in surface["plan_payloads"]}
    requests = {request.logical_key: request for request in surface["requests"]}
    results = _result_store(run_dir).by_key()
    unresolved = _unresolved_store(run_dir).by_key()
    attempt_groups = _validated_attempt_groups(surface, run_dir)
    if (set(results) - set(plans) or set(unresolved) - set(plans)
            or set(results) & set(unresolved)):
        raise ContractStop("judge terminal stores disagree with frozen batch plan")
    for logical_key, stored in results.items():
        row = _payload(stored)
        plan = plans[logical_key]
        request = requests[logical_key]
        if (row.get("batch_id") != plan["batch_id"]
                or row.get("design") != plan["design"]
                or row.get("request_sha256") != plan["request_sha256"]
                or not isinstance(row.get("attempt_ids"), list)
                or not row["attempt_ids"]
                or not _terminal_attempt_link(
                    row, request, attempt_groups, unresolved=False)
                or not validate_judge_result(request, row.get("value"))
                or row.get("scores_by_unit")
                != scores_by_unit(request, row["value"])):
            raise ContractStop(f"invalid persisted judge result: {logical_key}")
    for logical_key, stored in unresolved.items():
        row = _payload(stored)
        plan = plans[logical_key]
        request = requests[logical_key]
        if (row.get("batch_id") != plan["batch_id"]
                or row.get("design") != plan["design"]
                or row.get("request_sha256") != plan["request_sha256"]
                or row.get("error_type") != "ThreadStop"
                or not _terminal_attempt_link(
                    row, request, attempt_groups, unresolved=True)
                or row.get("unit_keys") != list(request.expected_unit_keys)
                or row.get("category_cells")
                != _request_category_cells(plan, request)):
            raise ContractStop(f"invalid unresolved judge batch: {logical_key}")
    return plans, results, unresolved


def _bind_attempt_custody(sol_client, run_dir):
    if not hasattr(sol_client, "attempt_sink"):
        raise ContractStop("Sol client does not expose the registered attempt sink")
    store = _attempt_store(run_dir)
    binding = str(store.path.resolve())
    prior_binding = getattr(sol_client, "_open6_judge_sink_binding", None)
    if prior_binding is not None:
        if prior_binding != binding:
            raise ContractStop("Sol client already bound to another judge run")
        return
    previous_sink = sol_client.attempt_sink

    def sink(record):
        if previous_sink is not None:
            previous_sink(copy.deepcopy(record))
        store.append_sink(copy.deepcopy(record))

    sol_client.attempt_sink = sink
    sol_client._open6_judge_sink_binding = binding


def _finalize_inflight_attempts(surface, run_dir, sol_client):
    """Close crash-stranded attempts from complete custody before resuming."""
    ledger = getattr(sol_client, "ledger", None)
    if ledger is None or not hasattr(ledger, "attempt_snapshot"):
        return
    groups = _validated_attempt_groups(surface, run_dir)
    attempt_store = _attempt_store(run_dir)
    recovered = set(getattr(
        sol_client, "_open6_recovered_interrupted_attempt_ids", set()))
    for request in surface["requests"]:
        if hasattr(ledger, "_history"):
            attempt_ids = list(ledger._history(request.logical_key))
        else:
            attempt_ids = [row["attempt_id"]
                           for row in groups.get(request.logical_key, [])]
        custody = {row["attempt_id"]: row
                   for row in groups.get(request.logical_key, [])}
        for attempt_id in attempt_ids:
            snapshot = ledger.attempt_snapshot(attempt_id)
            if snapshot.get("finish") is not None:
                continue
            row = custody.get(attempt_id)
            if row is None:
                row = attempt_store.append({
                    "logical_key": request.logical_key,
                    "attempt_id": attempt_id,
                    "prompt": request.prompt,
                    "schema": request.schema,
                    "final_text": "",
                    "trace_jsonl": "",
                    "stderr": "",
                    "returncode": None,
                    "error_class": "interrupted",
                    "payload_sha256": _text_hash(request.prompt),
                    "schema_sha256": _hash(request.schema),
                    "trace_sha256": _text_hash(""),
                    "response_sha256": None,
                    "error_sha256": _hash({"type": "interrupted"}),
                    "cli_version": "crash-recovery",
                    "usage": {},
                })
                custody[attempt_id] = row
            valid = False
            value = None
            if row is not None and row.get("error_class") is None:
                try:
                    value = json.loads(row.get("final_text", ""))
                except (json.JSONDecodeError, TypeError):
                    value = None
                valid = validate_judge_result(request, value)
            if valid:
                ledger.finish(
                    attempt_id, valid=True,
                    trace_sha256=row.get("trace_sha256"),
                    response_sha256=row.get("response_sha256"),
                    error_sha256=None,
                    cli_version=row.get("cli_version", "unknown"),
                    usage=copy.deepcopy(row.get("usage", {})),
                )
            else:
                if row.get("error_class") is None:
                    recovered.add(attempt_id)
                ledger.finish(
                    attempt_id, valid=False, error_class="interrupted",
                    trace_sha256=row.get("trace_sha256"),
                    response_sha256=row.get("response_sha256"),
                    error_sha256=(row.get("error_sha256") or _hash({
                        "type": "interrupted"})),
                    cli_version=row.get("cli_version", "crash-recovery"),
                    usage=copy.deepcopy(row.get("usage", {})),
                )
    sol_client._open6_recovered_interrupted_attempt_ids = recovered


def _attempt_terminal_fields(sol_client, request, attempt_store):
    rows = [row for row in attempt_store.records()
            if row.get("logical_key") == request.logical_key]
    rows.sort(key=lambda row: row["attempt_id"])
    if not 1 <= len(rows) <= 2:
        raise ContractStop("terminal judge batch lacks exact attempt custody")
    recovered = set(getattr(
        sol_client, "_open6_recovered_interrupted_attempt_ids", set()))
    return {
        "attempt_ids": [row["attempt_id"] for row in rows],
        "attempt_record_sha256": [row["record_sha256"] for row in rows],
        "recovered_interrupted_attempt_ids": sorted(
            recovered & {row["attempt_id"] for row in rows}),
    }


def _reconcile_attempt_custody(surface, run_dir, sol_client):
    """Recover terminal Sol work after a crash between finish and result append."""
    ledger = getattr(sol_client, "ledger", None)
    if ledger is None or not hasattr(ledger, "attempt_snapshot"):
        return
    plans = {row["logical_key"]: row for row in surface["plan_payloads"]}
    requests = {row.logical_key: row for row in surface["requests"]}
    results = _result_store(run_dir).by_key()
    unresolved = _unresolved_store(run_dir).by_key()
    attempt_store = _attempt_store(run_dir)
    grouped = _validated_attempt_groups(surface, run_dir)

    for logical_key, stored_rows in grouped.items():
        if logical_key in results or logical_key in unresolved:
            continue
        rows = [_payload(row) for row in stored_rows]
        rows.sort(key=lambda row: row["attempt_id"])
        if len(rows) > 2:
            raise ContractStop("judge attempt custody exceeds one replay")
        request = requests[logical_key]
        plan = plans[logical_key]
        finalized = []
        for row in rows:
            if (row.get("prompt") != request.prompt
                    or row.get("schema") != request.schema
                    or row.get("payload_sha256") != _text_hash(request.prompt)
                    or row.get("schema_sha256") != _hash(request.schema)):
                raise ContractStop("judge attempt custody differs from frozen request")
            snapshot = ledger.attempt_snapshot(row["attempt_id"])
            start = snapshot.get("start") if isinstance(snapshot, dict) else None
            finish = snapshot.get("finish") if isinstance(snapshot, dict) else None
            if (not isinstance(start, dict)
                    or (start.get("logical_key") is not None
                        and start.get("logical_key") != logical_key)):
                raise ContractStop("judge ledger/custody identity mismatch")
            if finish is not None:
                if not isinstance(finish, dict) or type(finish.get("valid")) is not bool:
                    raise ContractStop("judge ledger finish is malformed")
                finalized.append((row, finish))
        valid = [(row, finish) for row, finish in finalized if finish["valid"]]
        if valid:
            if len(valid) != 1 or finalized[-1] != valid[0]:
                raise ContractStop("judge ledger has work after a valid result")
            row, _finish = valid[0]
            if row.get("error_class") is not None:
                raise ContractStop("valid judge ledger finish has defective custody")
            try:
                value = json.loads(row.get("final_text", ""))
            except (json.JSONDecodeError, TypeError) as exc:
                raise ContractStop("valid judge custody has malformed final JSON") from exc
            if not validate_judge_result(request, value):
                raise ContractStop("valid judge custody fails registered semantics")
            _result_store(run_dir).append({
                "logical_key": logical_key,
                "batch_id": request.batch_id,
                "design": request.design,
                "request_sha256": plan["request_sha256"],
                "value": value,
                "scores_by_unit": scores_by_unit(request, value),
                "cli_version": row.get("cli_version", "unknown"),
                "usage": copy.deepcopy(row.get("usage", {})),
                **_attempt_terminal_fields(
                    sol_client, request, attempt_store),
            })
        elif len(finalized) == 2:
            failure = rows[-1].get("error_class")
            recovered_stop = ThreadStop(
                f"Sol second failure for {logical_key}: {failure}")
            disposition = _thread_stop_disposition(
                recovered_stop, request, attempt_store)
            if disposition != "registered_key_local_second_failure":
                raise JudgeRunStop(disposition, logical_key) from recovered_stop
            _unresolved_store(run_dir).append({
                "logical_key": logical_key,
                "batch_id": request.batch_id,
                "design": request.design,
                "request_sha256": plan["request_sha256"],
                "unit_keys": list(request.expected_unit_keys),
                "category_cells": _request_category_cells(plan, request),
                "error_type": "ThreadStop",
                "error": "recovered two finished invalid Sol attempts",
                **_attempt_terminal_fields(
                    sol_client, request, attempt_store),
            })


def _thread_stop_disposition(exc, request, attempt_store):
    rows = [row for row in attempt_store.records()
            if row.get("logical_key") == request.logical_key]
    inspected = [str(exc)]
    inspected.extend(str(row.get(field) or "") for row in rows
                     for field in ("stderr", "error_class"))
    if any(pattern.search(text) for pattern in _QUOTA_OR_USAGE_PATTERNS
           for text in inspected):
        return "oauth_quota_or_usage_limit"

    prefix = f"Sol second failure for {request.logical_key}:"
    if not str(exc).startswith(prefix):
        return "unregistered_judge_failure"
    reported_failure = str(exc)[len(prefix):].strip()
    custody_failures = [row.get("error_class") for row in rows]
    if (len(rows) != 2 or reported_failure not in SOL_FAILURES
            or custody_failures[-1:] != [reported_failure]
            or any(failure not in SOL_FAILURES
                   for failure in custody_failures)):
        return "unregistered_judge_failure"
    return "registered_key_local_second_failure"


def _execute_one(sol_client, request, plan, result_store, unresolved_store,
                 attempt_store):
    try:
        result = execute_judge_batch(sol_client, request)
    except BudgetStop as exc:
        reason = ("sol_turn_or_replay_cap"
                  if str(exc) in _SOL_TURN_OR_REPLAY_CAPS
                  else "unregistered_judge_failure")
        raise JudgeRunStop(reason, request.logical_key) from exc
    except ThreadStop as exc:
        disposition = _thread_stop_disposition(
            exc, request, attempt_store)
        if disposition != "registered_key_local_second_failure":
            raise JudgeRunStop(disposition, request.logical_key) from exc
        unresolved_store.append({
            "logical_key": request.logical_key,
            "batch_id": request.batch_id,
            "design": request.design,
            "request_sha256": plan["request_sha256"],
            "unit_keys": list(request.expected_unit_keys),
            "category_cells": _request_category_cells(plan, request),
            "error_type": "ThreadStop",
            "error": str(exc),
            **_attempt_terminal_fields(sol_client, request, attempt_store),
        })
        return "unresolved"
    value = copy.deepcopy(result.value)
    if not validate_judge_result(request, value):
        raise ContractStop("Sol result escaped semantic replay validation")
    result_store.append({
        "logical_key": request.logical_key,
        "batch_id": request.batch_id,
        "design": request.design,
        "request_sha256": plan["request_sha256"],
        "value": value,
        "scores_by_unit": scores_by_unit(request, value),
        "cli_version": result.cli_version,
        "usage": copy.deepcopy(result.usage),
        **_attempt_terminal_fields(sol_client, request, attempt_store),
    })
    return "valid"


def _sol_completed_turn_count(attempt_rows):
    completed = 0
    for row in attempt_rows:
        for line in str(row.get("trace_jsonl") or "").splitlines():
            try:
                event = json.loads(line)
            except (json.JSONDecodeError, TypeError):
                continue
            if isinstance(event, dict) and event.get("type") == "turn.completed":
                completed += 1
    return completed


def _persist_stop_checkpoint(surface, run_dir, stop, *, benchmark_root,
                             manifest_path):
    plans = {row["logical_key"]: row for row in surface["plan_payloads"]}
    empty = {logical_key for logical_key, plan in plans.items()
             if not plan["available_unit_keys"]}
    completed = (set(_result_store(run_dir).by_key())
                 | set(_unresolved_store(run_dir).by_key()) | empty)
    missing = set(plans) - completed
    attempts = _attempt_store(run_dir).records()
    store = _stop_store(run_dir)
    payload = {
        "checkpoint_id": f"judge-stop:{len(store.records()) + 1:04d}",
        "status": "stopped_resumable",
        "reason": stop.reason_code,
        "reason_code": stop.reason_code,
        "stopped_batch_key": stop.stopped_batch_key,
        "completed_batch_keys": sorted(completed),
        "missing_batch_keys": sorted(missing),
        "sol_attempt_count": len(attempts),
        "sol_completed_turn_count": _sol_completed_turn_count(attempts),
        "safest_next_command": [
            "python", "-m", "walkworthy.open6_sol1_judge_run", "status",
            "--benchmark-root", str(benchmark_root),
            "--manifest", str(manifest_path),
            "--run-dir", str(run_dir),
        ],
    }
    store.append(payload)
    return payload


def _materialize_verdicts(surface, run_dir, results, unresolved):
    plan_by_key = {payload["logical_key"]: payload
                   for payload in surface["plan_payloads"]}
    unit_to_batch = {
        unit["unit_key"]: logical_key
        for logical_key, plan in plan_by_key.items()
        for unit in plan["units"]
    }
    unit_payloads = {
        unit["unit_key"]: unit
        for plan in plan_by_key.values() for unit in plan["units"]
    }
    scored = {}
    for row in results.values():
        scored.update(row["scores_by_unit"])
    unresolved_keys = {
        unit_key for row in unresolved.values() for unit_key in row["unit_keys"]
    }
    upstream_keys = set(surface["upstream_missing_unit_keys"])
    if (set(scored) & (unresolved_keys | upstream_keys)
            or unresolved_keys & upstream_keys):
        raise ContractStop("judge unit is both scored and unresolved")
    if set(scored) | unresolved_keys | upstream_keys != set(unit_payloads):
        raise ContractStop("terminal judge batches do not cover the exact unit surface")

    verdict_payloads = []
    for record_key, source in sorted(
            surface["source_records"].items(),
            key=lambda pair: pair[1]["logical_key"]):
        units = surface["units_by_record"][record_key]
        missing_units = []
        for unit in units:
            if unit.unit_key in unresolved_keys or unit.unit_key in upstream_keys:
                payload = unit_payloads[unit.unit_key]
                missing_units.append({
                    "unit_key": unit.unit_key,
                    "unit_kind": payload["unit_kind"],
                    "locator": copy.deepcopy(payload["locator"]),
                    "category_names": list(payload["category_names"]),
                    "batch_id": plan_by_key[
                        unit_to_batch[unit.unit_key]]["batch_id"],
                    "missing_reason": (
                        "upstream_item_model_unresolved"
                        if unit.unit_key in upstream_keys
                        else "judge_second_failure"),
                })
        available = {
            unit.unit_key: copy.deepcopy(scored[unit.unit_key])
            for unit in units if unit.unit_key in scored
        }
        unresolved_batch_ids = sorted(
            {row["batch_id"] for row in missing_units})
        verdict = None
        status_value = "unresolved"
        if not missing_units:
            verdict = reassemble_single_judge_verdict(
                source["item"], units, available)
            status_value = "complete"
        verdict_payloads.append({
            "logical_key": (
                "verdict:" + source["logical_key"].removeprefix("item:")),
            "source_execution_key": source["logical_key"],
            "record_key": record_key,
            "item_id": source["item_id"],
            "design": source["design"],
            "model": source["model"],
            "judge": "gpt-5.6-sol",
            "judge_family": "openai",
            "status": status_value,
            "total_units": len(units),
            "scored_units": len(available),
            "missing_units": missing_units,
            "missing_category_cells": sum(
                len(row["category_names"]) for row in missing_units),
            "unresolved_batch_ids": unresolved_batch_ids,
            "available_scores_by_unit": available,
            "verdict": verdict,
        })
    if len(verdict_payloads) != EXPECTED_EXECUTION_RECORDS:
        raise ContractStop("single-judge verdict roster is incomplete")
    _append_or_validate(_verdict_store(run_dir), verdict_payloads)


def run_judging(benchmark_root, manifest_path, run_dir, *, sol_client,
                max_workers=MAX_CONCURRENCY) -> dict:
    """Execute only missing batches and never rerun a valid Sol result."""
    if type(max_workers) is not int or not 1 <= max_workers <= MAX_CONCURRENCY:
        raise ContractStop("OPEN6-SOL1 Sol concurrency must be one or two")
    prepare_judge_plan(benchmark_root, manifest_path, run_dir)
    surface = _derive_surface(benchmark_root, manifest_path, run_dir)
    plans, results, unresolved = _validate_terminal_stores(surface, run_dir)
    _bind_attempt_custody(sol_client, run_dir)
    try:
        _finalize_inflight_attempts(surface, run_dir, sol_client)
        _reconcile_attempt_custody(surface, run_dir, sol_client)
    except JudgeRunStop as exc:
        _persist_stop_checkpoint(
            surface, run_dir, exc,
            benchmark_root=benchmark_root,
            manifest_path=manifest_path,
        )
        raise
    plans, results, unresolved = _validate_terminal_stores(surface, run_dir)
    pending = [
        (request, plans[request.logical_key])
        for request in surface["requests"]
        if request.logical_key not in results
        and request.logical_key not in unresolved
    ]
    new_batches = 0
    if pending:
        result_store = _result_store(run_dir)
        unresolved_store = _unresolved_store(run_dir)
        attempt_store = _attempt_store(run_dir)
        pool = ThreadPoolExecutor(max_workers=max_workers)
        iterator = iter(pending)
        futures = {}

        def submit_one():
            try:
                request, plan = next(iterator)
            except StopIteration:
                return False
            future = pool.submit(
                _execute_one, sol_client, request, plan,
                result_store, unresolved_store, attempt_store)
            futures[future] = request.logical_key
            return True

        try:
            for _ in range(max_workers):
                if not submit_one():
                    break
            while futures:
                done, _ = wait(tuple(futures), return_when=FIRST_COMPLETED)
                completed = 0
                for future in done:
                    futures.pop(future)
                    future.result()
                    new_batches += 1
                    completed += 1
                for _ in range(completed):
                    submit_one()
        except Exception as exc:
            for future in futures:
                future.cancel()
            pool.shutdown(wait=True, cancel_futures=True)
            if isinstance(exc, JudgeRunStop):
                _persist_stop_checkpoint(
                    surface, run_dir, exc,
                    benchmark_root=benchmark_root,
                    manifest_path=manifest_path,
                )
            raise
        else:
            pool.shutdown(wait=True)
    _, results, unresolved = _validate_terminal_stores(surface, run_dir)
    upstream_empty_batches = sum(
        not payload["available_unit_keys"]
        for payload in surface["plan_payloads"])
    if (len(results) + len(unresolved) + upstream_empty_batches
            == EXPECTED_BATCHES):
        _materialize_verdicts(surface, run_dir, results, unresolved)
    summary = status(benchmark_root, manifest_path, run_dir)
    summary["new_batches"] = new_batches
    return summary


def status(benchmark_root, manifest_path, run_dir) -> dict:
    prepare_judge_plan(benchmark_root, manifest_path, run_dir)
    surface = _derive_surface(benchmark_root, manifest_path, run_dir)
    _, results, unresolved = _validate_terminal_stores(surface, run_dir)
    verdicts = _verdict_store(run_dir).records()
    allowed = {
        "verdict:" + source["logical_key"].removeprefix("item:")
        for source in surface["source_records"].values()
    }
    if ({row["logical_key"] for row in verdicts} - allowed
            or len({row["logical_key"] for row in verdicts}) != len(verdicts)):
        raise ContractStop("single-judge verdict store has invalid roster")
    complete = sum(row.get("status") == "complete" for row in verdicts)
    unresolved_verdicts = sum(
        row.get("status") == "unresolved" for row in verdicts)
    upstream_empty_batches = sum(
        not payload["available_unit_keys"]
        for payload in surface["plan_payloads"])
    terminal = len(results) + len(unresolved) + upstream_empty_batches
    upstream_units = len(surface["upstream_missing_unit_keys"])
    upstream_cells = sum(
        payload["upstream_missing_category_cells"]
        for payload in surface["plan_payloads"])
    return {
        "expected_batches": EXPECTED_BATCHES,
        "valid_batches": len(results),
        "unresolved_batches": len(unresolved),
        "upstream_empty_batches": upstream_empty_batches,
        "terminal_batches": terminal,
        "pending_batches": EXPECTED_BATCHES - terminal,
        "attempt_custody_records": len(_attempt_store(run_dir).records()),
        "expected_verdict_records": EXPECTED_EXECUTION_RECORDS,
        "verdict_records": len(verdicts),
        "complete_verdict_records": complete,
        "unresolved_verdict_records": unresolved_verdicts,
        "missing_category_cells": sum(
            row.get("missing_category_cells", 0) for row in verdicts),
        "upstream_missing_execution_records": len(
            surface["terminal_unresolved"]),
        "upstream_missing_units": upstream_units,
        "upstream_missing_category_cells": upstream_cells,
        "terminal_complete": (
            terminal == EXPECTED_BATCHES
            and len(verdicts) == EXPECTED_EXECUTION_RECORDS),
        "judge_complete": (
            len(results) == EXPECTED_BATCHES
            and not unresolved
            and not surface["terminal_unresolved"]
            and len(verdicts) == EXPECTED_EXECUTION_RECORDS
            and unresolved_verdicts == 0),
        "single_judge_only": True,
        "holdout_loaded": False,
    }


def _parser():
    parser = argparse.ArgumentParser(
        description="WALKWORTHY OPEN6-SOL1 judge plan/status")
    phases = parser.add_subparsers(dest="phase", required=True)
    for phase in ("plan", "status"):
        command = phases.add_parser(phase)
        command.add_argument("--benchmark-root", required=True)
        command.add_argument("--manifest", required=True)
        command.add_argument("--run-dir", required=True)
    return parser


def main(argv=None):
    args = _parser().parse_args(argv)
    function = prepare_judge_plan if args.phase == "plan" else status
    result = function(args.benchmark_root, args.manifest, args.run_dir)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
