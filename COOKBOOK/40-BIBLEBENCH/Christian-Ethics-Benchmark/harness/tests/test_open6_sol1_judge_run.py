"""Offline execution/resume tests for the OPEN6-SOL1 descriptive judge."""

from __future__ import annotations

import json
import hashlib
import threading
import time
from collections import Counter
from dataclasses import asdict

import pytest

from walkworthy.executors import AdministrationResult, ItemExecution, TurnResult
from walkworthy.open6_sol1_runtime import BudgetStop, ThreadStop


def _module():
    from walkworthy import open6_sol1_judge_run

    return open6_sol1_judge_run


def _manifest(benchmark_root, tmp_path):
    from walkworthy.open6_sol1 import build_manifest, write_or_validate_manifest

    path = tmp_path / "frozen-manifest.json"
    write_or_validate_manifest(path, build_manifest(benchmark_root))
    return path


def _execution(item, model):
    from walkworthy.executors import permuted_order
    from walkworthy.manifest import FIXED_PERMUTATION_SEEDS

    labels = [admin.label for admin in item.administrations]
    axis = {
        "03-quiettongue": "twin_order",
        "08-vocationfork": "twin_order",
        "04-innerweight": "variant_order",
        "10-strangergate": "variant_order",
        "09-doubleedge": "seat_order",
        "05-ordoamoris": "claimant_order",
    }.get(item.design, "twin_order")
    order = (
        permuted_order(labels, FIXED_PERMUTATION_SEEDS.get(axis, 0), item.id)
        if item.order_permuted or item.isolation_required else labels
    )
    source_by_label = {admin.label: admin for admin in item.administrations}
    administrations = []
    for label in order:
        admin = source_by_label[label]
        turns = [
            TurnResult(
                index=turn.index,
                user_text=(
                    turn.text
                    or next(iter((turn.branches or {"": ""}).values()))
                ),
                response=(
                    f"offline response for {model} {item.id} "
                    f"{admin.label} turn {turn.index}"
                ),
                branch_state=(next(iter(turn.branches)) if turn.branches else None),
            )
            for turn in admin.turns
        ]
        administrations.append(AdministrationResult(
            label=admin.label,
            kind=admin.kind,
            system=admin.system,
            turns=turns,
            terminal_response=(
                f"offline terminal for {model} {item.id} {admin.label}"
                if admin.terminal_ask else None
            ),
            terminal_user_text=admin.terminal_ask,
        ))
    return ItemExecution(
        item_id=item.id,
        design=item.design,
        model=model,
        order=order,
        administrations=administrations,
        isolation_used=item.isolation_required,
    )


def _seed_full_surface(benchmark_root, tmp_path, *, unresolved_key=None):
    from walkworthy.open6_sol1 import select_public_items
    from walkworthy.open6_sol1_run import AppendOnlyStore, prepare_run

    manifest_path = _manifest(benchmark_root, tmp_path)
    run_dir = tmp_path / "20260714-open6-sol1"
    manifest = prepare_run(benchmark_root, manifest_path, run_dir)
    executions = AppendOnlyStore(run_dir / "executions.jsonl", "executions")
    items = select_public_items(benchmark_root)
    payloads = []
    for model_row in manifest["openrouter"]["models"]:
        model = model_row["slug"]
        for item in items:
            logical_key = f"item:{model}:{item.id}"
            if logical_key == unresolved_key:
                unresolved = AppendOnlyStore(
                    run_dir / "terminal-unresolved-sut.jsonl",
                    "terminal-unresolved-sut")
                row = _terminal_row(item, model, failure="malformed")
                row["attempt_ids"] = [9001, 9002]
                unresolved.append(row)
                continue
            execution = _execution(item, model)
            record = {
                "logical_key": logical_key,
                "status": "complete",
                "item_id": item.id,
                "design": item.design,
                "model": model,
                "execution": asdict(execution),
            }
            if item.design == "05-ordoamoris":
                allocation = item.extras["allocation"]
                amount = (allocation["budget"] / len(allocation["tokens"])
                          if allocation["tokens"] else 0.0)
                values = {token: amount for token in allocation["tokens"]}
                response = "allocation: {" + ", ".join(
                    f"{token}: {amount}" for token in allocation["tokens"]
                ) + "}"
                record["allocation"] = {
                    "ok": True,
                    "values": values,
                    "total": allocation["budget"],
                    "sum_ok": True,
                    "tokens_missing": [],
                    "extra_tokens": [],
                    "non_compliant": False,
                    "response": response,
                    "logical_key": f"offline:{model}:{item.id}:allocation",
                    "attempt_ids": [1],
                }
            payloads.append(record)
    # Seed a production-valid chain in one write; the store's fsync behavior is
    # tested by its own suite and per-record fsync would dominate this judge test.
    stored = []
    previous = None
    for sequence, payload in enumerate(payloads, 1):
        row = dict(payload)
        row.update({
            "store_kind": "executions",
            "sequence": sequence,
            "previous_sha256": previous,
        })
        row["record_sha256"] = executions._record_hash(row)
        previous = row["record_sha256"]
        stored.append(row)
    executions.path.write_text("".join(
        json.dumps(row, ensure_ascii=False, sort_keys=True,
                   separators=(",", ":")) + "\n"
        for row in stored
    ), encoding="utf-8")
    assert len(executions.records()) == 2064 - bool(unresolved_key)
    return manifest_path, run_dir


def _first_allowed(schema):
    if "enum" in schema:
        return schema["enum"][0]
    if schema["type"] == "integer":
        return schema.get("minimum", 0)
    raise AssertionError(schema)


class FakeSolJudge:
    """Offline Sol seam that honors attempt custody and semantic validation."""

    def __init__(self, *, crash_once=None, fail_twice=None,
                 failure_class="schema_invalid", failure_stderr=""):
        self.attempt_sink = None
        self.crash_once = crash_once
        self.fail_twice = fail_twice
        self.failure_class = failure_class
        self.failure_stderr = failure_stderr
        self.crashed = False
        self.calls = []
        self.valid_by_key = Counter()
        self.active = 0
        self.max_active = 0
        self._attempt = 0
        self._lock = threading.Lock()

    def _custody(self, logical_key, prompt, schema, value, error_class,
                 *, stderr=""):
        with self._lock:
            self._attempt += 1
            attempt = self._attempt
        if self.attempt_sink is not None:
            final = "" if value is None else json.dumps(value, sort_keys=True)
            trace = ("" if stderr else
                     '{"type":"turn.completed","usage":{}}\n')
            self.attempt_sink({
                "logical_key": logical_key,
                "attempt_id": attempt,
                "prompt": prompt,
                "schema": schema,
                "final_text": final,
                "trace_jsonl": trace,
                "stderr": stderr,
                "returncode": 1 if stderr else 0,
                "error_class": error_class,
                "payload_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
                "schema_sha256": hashlib.sha256(
                    (json.dumps(schema, ensure_ascii=False, sort_keys=True,
                                separators=(",", ":")) + "\n").encode()
                ).hexdigest(),
                "trace_sha256": hashlib.sha256(trace.encode()).hexdigest(),
                "response_sha256": (None if value is None else
                                    hashlib.sha256(final.encode()).hexdigest()),
                "error_sha256": None if error_class is None else "5" * 64,
                "cli_version": "fake-sol",
                "usage": {},
            })
        return attempt

    def run_json(self, logical_key, prompt, schema, value_validator=None):
        with self._lock:
            self.active += 1
            self.max_active = max(self.max_active, self.active)
            self.calls.append(logical_key)
        try:
            time.sleep(0.0002)
            if logical_key == self.crash_once and not self.crashed:
                self.crashed = True
                raise RuntimeError("simulated process crash")
            keys = schema["properties"]["verdicts"]["items"]["properties"][
                "unit_key"
            ]["enum"]
            score_schema = schema["properties"]["verdicts"]["items"][
                "properties"
            ]["scores"]
            value = {"verdicts": [{
                "unit_key": key,
                "scores": {
                    name: _first_allowed(category)
                    for name, category in score_schema["properties"].items()
                },
            } for key in keys]}
            if logical_key == self.fail_twice:
                self._custody(
                    logical_key, prompt, schema, None, self.failure_class,
                    stderr=self.failure_stderr)
                self._custody(
                    logical_key, prompt, schema, None, self.failure_class,
                    stderr=self.failure_stderr)
                raise ThreadStop(
                    f"Sol second failure for {logical_key}: "
                    f"{self.failure_class}")
            assert value_validator is not None and value_validator(value) is True
            attempt = self._custody(logical_key, prompt, schema, value, None)
            with self._lock:
                self.valid_by_key[logical_key] += 1
            return type("Result", (), {
                "value": value,
                "prompt": prompt,
                "schema": schema,
                "final_text": json.dumps(value, sort_keys=True),
                "trace_jsonl": '{"type":"turn.completed","usage":{}}\n',
                "cli_version": "fake-sol",
                "usage": {},
                "attempt_ids": (attempt,),
            })()
        finally:
            with self._lock:
                self.active -= 1


def test_full_surface_plan_fake_judging_crash_resume_and_no_valid_rerun(
        benchmark_root, tmp_path):
    judge_run = _module()
    manifest_path, run_dir = _seed_full_surface(benchmark_root, tmp_path)

    plan = judge_run.prepare_judge_plan(
        benchmark_root, manifest_path, run_dir)
    assert plan["execution_records"] == 2064
    assert plan["units"] == 5370
    assert plan["category_cells"] == 10008
    assert plan["batches"] == 227
    assert all(row["logical_key"].startswith("sol:judge:")
               for row in judge_run.load_batch_plan(run_dir))
    assert plan["batch_sizes"][-1] <= 24
    assert len(judge_run.load_batch_plan(run_dir)) == 227

    crash_key = judge_run.load_batch_plan(run_dir)[0]["request"]["logical_key"]
    sol = FakeSolJudge(crash_once=crash_key)
    with pytest.raises(RuntimeError, match="simulated process crash"):
        judge_run.run_judging(
            benchmark_root, manifest_path, run_dir,
            sol_client=sol, max_workers=2,
        )
    assert len(sol.calls) <= 2

    after_crash = judge_run.status(benchmark_root, manifest_path, run_dir)
    assert 0 <= after_crash["valid_batches"] < 227
    assert after_crash["verdict_records"] == 0

    completed = judge_run.run_judging(
        benchmark_root, manifest_path, run_dir,
        sol_client=sol, max_workers=2,
    )
    assert completed["terminal_batches"] == 227
    assert completed["valid_batches"] == 227
    assert completed["unresolved_batches"] == 0
    assert completed["verdict_records"] == 2064
    assert completed["complete_verdict_records"] == 2064
    assert completed["unresolved_verdict_records"] == 0
    assert completed["judge_complete"] is True
    assert sol.max_active == 2
    assert set(sol.valid_by_key.values()) == {1}

    before = len(sol.calls)
    resumed = judge_run.run_judging(
        benchmark_root, manifest_path, run_dir,
        sol_client=sol, max_workers=2,
    )
    assert resumed["new_batches"] == 0
    assert len(sol.calls) == before
    assert len(judge_run.load_single_judge_verdicts(run_dir)) == 2064
    assert len(judge_run.load_attempt_custody(run_dir)) == 227


def test_second_failure_is_terminal_and_reassembles_exact_missingness(
        benchmark_root, tmp_path):
    judge_run = _module()
    manifest_path, run_dir = _seed_full_surface(benchmark_root, tmp_path)
    judge_run.prepare_judge_plan(benchmark_root, manifest_path, run_dir)
    failed = judge_run.load_batch_plan(run_dir)[0]
    failed_key = failed["request"]["logical_key"]
    failed_units = {row["unit_key"] for row in failed["units"]}
    sol = FakeSolJudge(fail_twice=failed_key)

    summary = judge_run.run_judging(
        benchmark_root, manifest_path, run_dir,
        sol_client=sol, max_workers=2,
    )

    assert summary["terminal_batches"] == 227
    assert summary["valid_batches"] == 226
    assert summary["unresolved_batches"] == 1
    assert summary["terminal_complete"] is True
    assert summary["judge_complete"] is False
    unresolved = judge_run.load_unresolved_batches(run_dir)
    assert len(unresolved) == 1
    assert set(unresolved[0]["unit_keys"]) == failed_units
    assert len(judge_run.load_attempt_custody(run_dir)) == 228

    verdicts = judge_run.load_single_judge_verdicts(run_dir)
    affected = [row for row in verdicts if row["status"] == "unresolved"]
    assert affected
    assert sum(row["missing_category_cells"] for row in affected) == sum(
        len(unit["category_names"]) for unit in failed["units"]
    )
    assert {
        missing["unit_key"]
        for row in affected for missing in row["missing_units"]
    } == failed_units
    assert all(row["verdict"] is None for row in affected)
    assert all(row["scored_units"] + len(row["missing_units"])
               == row["total_units"] for row in affected)

    before = len(sol.calls)
    repeated = judge_run.run_judging(
        benchmark_root, manifest_path, run_dir,
        sol_client=sol, max_workers=2,
    )
    assert repeated["new_batches"] == 0
    assert len(sol.calls) == before


def test_mixed_upstream_and_judge_failure_persists_available_units_only(
        benchmark_root, tmp_path):
    judge_run = _module()
    missing_execution_key = "item:minimax/minimax-m3:WW-01-A01"
    manifest_path, run_dir = _seed_full_surface(
        benchmark_root, tmp_path, unresolved_key=missing_execution_key)
    judge_run.prepare_judge_plan(benchmark_root, manifest_path, run_dir)
    surface = judge_run._derive_surface(
        benchmark_root, manifest_path, run_dir)
    plan = next(row for row in surface["plan_payloads"]
                if row["upstream_missing_unit_keys"]
                and row["available_unit_keys"])
    request = next(row for row in surface["requests"]
                   if row.logical_key == plan["logical_key"])
    client = FakeSolJudge(fail_twice=request.logical_key)
    judge_run._bind_attempt_custody(client, run_dir)

    result = judge_run._execute_one(
        client, request, plan, judge_run._result_store(run_dir),
        judge_run._unresolved_store(run_dir),
        judge_run._attempt_store(run_dir))

    assert result == "unresolved"
    unresolved = judge_run.load_unresolved_batches(run_dir)
    assert len(unresolved) == 1
    row = unresolved[0]
    assert row["unit_keys"] == list(request.expected_unit_keys)
    assert not (set(row["unit_keys"]) & set(plan["upstream_missing_unit_keys"]))
    assert row["category_cells"] == (
        plan["category_cells"] - plan["upstream_missing_category_cells"])
    assert row["category_cells"] < plan["category_cells"]
    judge_run._validate_terminal_stores(surface, run_dir)


def test_rejects_incomplete_execution_surface_and_tampered_plan(
        benchmark_root, tmp_path):
    from walkworthy.open6_sol1_run import AppendOnlyStore, prepare_run

    judge_run = _module()
    manifest_path = _manifest(benchmark_root, tmp_path)
    run_dir = tmp_path / "20260714-open6-sol1"
    prepare_run(benchmark_root, manifest_path, run_dir)
    AppendOnlyStore(run_dir / "executions.jsonl", "executions")

    with pytest.raises(judge_run.ContractStop, match="exactly 2,064"):
        judge_run.prepare_judge_plan(benchmark_root, manifest_path, run_dir)

    manifest_path, run_dir = _seed_full_surface(
        benchmark_root, tmp_path / "complete")
    judge_run.prepare_judge_plan(benchmark_root, manifest_path, run_dir)
    path = run_dir / judge_run.JUDGE_PLAN_NAME
    lines = path.read_text().splitlines()
    first = json.loads(lines[0])
    first["design"] = "tampered"
    lines[0] = json.dumps(first, sort_keys=True, separators=(",", ":"))
    path.write_text("\n".join(lines) + "\n")
    with pytest.raises(judge_run.ContractStop, match="hash-chain"):
        judge_run.prepare_judge_plan(benchmark_root, manifest_path, run_dir)


def test_non_second_failure_thread_stop_is_not_mislabeled_unresolved(
        benchmark_root, tmp_path):
    from walkworthy.open6_sol1 import select_public_items
    from walkworthy.open6_sol1_judge import (
        batch_scoring_units, build_judge_request, build_scoring_units,
    )
    from walkworthy.open6_sol1_run import AppendOnlyStore

    judge_run = _module()
    item = select_public_items(benchmark_root)[0]
    model = "minimax/minimax-m3"
    units = build_scoring_units(
        item, _execution(item, model), model, "manifest-sha")
    batch = batch_scoring_units(units)[0]
    request = build_judge_request(batch)
    plan = {
        "request_sha256": "1" * 64,
        "category_cells": sum(len(unit.category_names) for unit in batch.units),
    }

    class InflightSol:
        def run_json(self, *_args, **_kwargs):
            raise ThreadStop("Sol key already in flight")

    results = AppendOnlyStore(tmp_path / "results.jsonl", "test-results")
    unresolved = AppendOnlyStore(tmp_path / "unresolved.jsonl", "test-unresolved")
    with pytest.raises(
            judge_run.JudgeRunStop, match="unregistered_judge_failure"):
        judge_run._execute_one(
            InflightSol(), request, plan, results, unresolved,
            judge_run._attempt_store(tmp_path / "attempts"))
    assert unresolved.records() == []


@pytest.mark.parametrize(("failure_class", "stderr", "reason_code"), [
    ("cli_failure", "You've hit your OAuth usage limit.",
     "oauth_quota_or_usage_limit"),
    ("unregistered_failure", "unexpected judge backend failure",
     "unregistered_judge_failure"),
])
def test_global_or_unknown_sol_failure_stops_with_resumable_checkpoint(
        benchmark_root, tmp_path, failure_class, stderr, reason_code):
    judge_run = _module()
    manifest_path, run_dir = _seed_full_surface(
        benchmark_root, tmp_path / reason_code)
    judge_run.prepare_judge_plan(benchmark_root, manifest_path, run_dir)
    target = next(
        row["logical_key"] for row in judge_run.load_batch_plan(run_dir)
        if row["available_unit_keys"])
    client = FakeSolJudge(
        fail_twice=target, failure_class=failure_class,
        failure_stderr=stderr)

    with pytest.raises(ThreadStop):
        judge_run.run_judging(
            benchmark_root, manifest_path, run_dir,
            sol_client=client, max_workers=1)

    assert judge_run.load_unresolved_batches(run_dir) == []
    checkpoints = judge_run.load_stop_checkpoints(run_dir)
    assert len(checkpoints) == 1
    checkpoint = checkpoints[0]
    assert checkpoint["reason_code"] == reason_code
    assert checkpoint["stopped_batch_key"] == target
    assert checkpoint["completed_batch_keys"] == []
    assert len(checkpoint["missing_batch_keys"]) == 227
    assert target in checkpoint["missing_batch_keys"]
    assert checkpoint["sol_attempt_count"] == 2
    assert checkpoint["sol_completed_turn_count"] == 0
    assert checkpoint["safest_next_command"] == [
        "python", "-m", "walkworthy.open6_sol1_judge_run", "status",
        "--benchmark-root", str(benchmark_root),
        "--manifest", str(manifest_path),
        "--run-dir", str(run_dir),
    ]


@pytest.mark.parametrize(("failure_class", "stderr", "reason_code"), [
    ("cli_failure", "OAuth usage limit reached.",
     "oauth_quota_or_usage_limit"),
    ("unregistered_failure", "unexpected systemic failure",
     "unregistered_judge_failure"),
])
def test_crash_reconciliation_applies_live_failure_disposition_and_checkpoints(
        benchmark_root, tmp_path, failure_class, stderr, reason_code):
    judge_run = _module()
    manifest_path, run_dir = _seed_full_surface(
        benchmark_root, tmp_path / reason_code)
    judge_run.prepare_judge_plan(benchmark_root, manifest_path, run_dir)
    surface = judge_run._derive_surface(
        benchmark_root, manifest_path, run_dir)
    request = surface["requests"][0]
    attempt_store = judge_run._attempt_store(run_dir)
    for attempt_id in (1, 2):
        attempt_store.append({
            "logical_key": request.logical_key,
            "attempt_id": attempt_id,
            "prompt": request.prompt,
            "schema": request.schema,
            "final_text": "",
            "trace_jsonl": "",
            "stderr": stderr,
            "returncode": 1,
            "error_class": failure_class,
            "payload_sha256": judge_run._text_hash(request.prompt),
            "schema_sha256": judge_run._hash(request.schema),
            "trace_sha256": judge_run._text_hash(""),
            "response_sha256": None,
            "error_sha256": "5" * 64,
            "cli_version": "fake-sol",
            "usage": {},
        })

    class FinishedLedger:
        def attempt_snapshot(self, attempt_id):
            return {
                "start": {
                    "attempt_id": attempt_id,
                    "logical_key": request.logical_key,
                },
                "finish": {
                    "valid": False,
                    "error_class": failure_class,
                },
            }

    client = type("Client", (), {
        "ledger": FinishedLedger(),
        "attempt_sink": None,
    })()
    with pytest.raises(judge_run.JudgeRunStop) as caught:
        judge_run._reconcile_attempt_custody(surface, run_dir, client)
    assert caught.value.reason_code == reason_code
    assert judge_run.load_unresolved_batches(run_dir) == []

    with pytest.raises(judge_run.JudgeRunStop) as caught:
        judge_run.run_judging(
            benchmark_root, manifest_path, run_dir,
            sol_client=client, max_workers=1)
    assert caught.value.reason_code == reason_code
    checkpoints = judge_run.load_stop_checkpoints(run_dir)
    assert len(checkpoints) == 1
    assert checkpoints[0]["reason_code"] == reason_code
    assert checkpoints[0]["stopped_batch_key"] == request.logical_key
    assert request.logical_key in checkpoints[0]["missing_batch_keys"]


@pytest.mark.parametrize("message", [
    "Sol replay reserve exhausted",
    "Sol attempt cap exhausted",
    "Sol planned call cap exhausted",
    "Sol turn cap exhausted",
])
def test_sol_turn_or_replay_budget_stop_is_normalized(
        benchmark_root, tmp_path, message):
    from walkworthy.open6_sol1 import select_public_items
    from walkworthy.open6_sol1_judge import (
        batch_scoring_units, build_judge_request, build_scoring_units,
    )
    from walkworthy.open6_sol1_run import AppendOnlyStore

    judge_run = _module()
    item = select_public_items(benchmark_root)[0]
    model = "minimax/minimax-m3"
    units = build_scoring_units(
        item, _execution(item, model), model, "manifest-sha")
    batch = batch_scoring_units(units)[0]
    request = build_judge_request(batch)
    plan = judge_run._batch_plan_payload(batch, request)

    class CappedSol:
        def run_json(self, *_args, **_kwargs):
            raise BudgetStop(message)

    with pytest.raises(judge_run.JudgeRunStop) as caught:
        judge_run._execute_one(
            CappedSol(), request, plan,
            AppendOnlyStore(tmp_path / "results.jsonl", "test-results"),
            AppendOnlyStore(tmp_path / "unresolved.jsonl", "test-unresolved"),
            judge_run._attempt_store(tmp_path / "attempts"))
    assert caught.value.reason_code == "sol_turn_or_replay_cap"


def test_sol_attempt_cap_persists_resumable_checkpoint(
        benchmark_root, tmp_path):
    judge_run = _module()
    manifest_path, run_dir = _seed_full_surface(benchmark_root, tmp_path)
    judge_run.prepare_judge_plan(benchmark_root, manifest_path, run_dir)
    target = next(
        row["logical_key"] for row in judge_run.load_batch_plan(run_dir)
        if row["available_unit_keys"])

    class CappedSol:
        attempt_sink = None

        def run_json(self, *_args, **_kwargs):
            raise BudgetStop("Sol attempt cap exhausted")

    with pytest.raises(judge_run.JudgeRunStop) as caught:
        judge_run.run_judging(
            benchmark_root, manifest_path, run_dir,
            sol_client=CappedSol(), max_workers=1)
    assert caught.value.reason_code == "sol_turn_or_replay_cap"
    checkpoints = judge_run.load_stop_checkpoints(run_dir)
    assert len(checkpoints) == 1
    assert checkpoints[0]["reason_code"] == "sol_turn_or_replay_cap"
    assert checkpoints[0]["stopped_batch_key"] == target
    assert target in checkpoints[0]["missing_batch_keys"]
    assert checkpoints[0]["sol_attempt_count"] == 0


def test_reconciles_finished_valid_and_second_failure_attempt_custody(
        benchmark_root, tmp_path):
    from walkworthy.open6_sol1 import select_public_items
    from walkworthy.open6_sol1_judge import (
        batch_scoring_units, build_judge_request, build_scoring_units,
    )

    judge_run = _module()
    item = select_public_items(benchmark_root)[0]
    model = "minimax/minimax-m3"
    units = build_scoring_units(
        item, _execution(item, model), model, "manifest-sha")
    batch = batch_scoring_units(units)[0]
    request = build_judge_request(batch)
    plan = judge_run._batch_plan_payload(batch, request)
    surface = {"requests": (request,), "plan_payloads": (plan,)}

    score_schema = request.score_schema["properties"]
    good = {"verdicts": [{
        "unit_key": key,
        "scores": {name: _first_allowed(schema)
                   for name, schema in score_schema.items()},
    } for key in request.expected_unit_keys]}

    class FinishedLedger:
        def __init__(self, finishes):
            self.finishes = finishes

        def attempt_snapshot(self, attempt):
            return {"start": {"attempt_id": attempt},
                    "finish": self.finishes[attempt]}

    valid_client = type("Client", (), {
        "ledger": FinishedLedger({1: {"valid": True, "error_class": None}}),
    })()
    valid_store = judge_run._attempt_store(tmp_path / "valid")
    final_text = json.dumps(good, sort_keys=True)
    valid_store.append({
        "logical_key": request.logical_key,
        "attempt_id": 1,
        "prompt": request.prompt,
        "schema": request.schema,
        "final_text": final_text,
        "trace_jsonl": "",
        "stderr": "",
        "returncode": 0,
        "error_class": None,
        "payload_sha256": judge_run._text_hash(request.prompt),
        "schema_sha256": judge_run._hash(request.schema),
        "trace_sha256": judge_run._text_hash(""),
        "response_sha256": judge_run._text_hash(final_text),
        "error_sha256": None,
        "cli_version": "fake-sol",
        "usage": {},
    })
    judge_run._reconcile_attempt_custody(surface, tmp_path / "valid", valid_client)
    results = judge_run._result_store(tmp_path / "valid").records()
    assert len(results) == 1
    assert results[0]["value"] == good
    assert results[0]["attempt_ids"] == [1]
    parked = tmp_path / "valid" / "parked-attempt-custody.jsonl"
    valid_store.path.rename(parked)
    with pytest.raises(
            judge_run.ContractStop, match="attempt custody|invalid persisted"):
        judge_run._validate_terminal_stores(surface, tmp_path / "valid")
    parked.rename(valid_store.path)

    failure_client = type("Client", (), {
        "ledger": FinishedLedger({
            1: {"valid": False, "error_class": "schema_invalid"},
            2: {"valid": False, "error_class": "schema_invalid"},
        }),
    })()
    failure_store = judge_run._attempt_store(tmp_path / "failure")
    for attempt in (1, 2):
        failure_store.append({
            "logical_key": request.logical_key,
            "attempt_id": attempt,
            "prompt": request.prompt,
            "schema": request.schema,
            "final_text": "",
            "trace_jsonl": "",
            "stderr": "",
            "returncode": 0,
            "error_class": "schema_invalid",
            "payload_sha256": judge_run._text_hash(request.prompt),
            "schema_sha256": judge_run._hash(request.schema),
            "trace_sha256": judge_run._text_hash(""),
            "response_sha256": None,
            "error_sha256": "5" * 64,
            "cli_version": "fake-sol",
            "usage": {},
        })
    judge_run._reconcile_attempt_custody(
        surface, tmp_path / "failure", failure_client)
    unresolved = judge_run._unresolved_store(tmp_path / "failure").records()
    assert len(unresolved) == 1
    assert unresolved[0]["unit_keys"] == list(request.expected_unit_keys)
    assert unresolved[0]["attempt_ids"] == [1, 2]


def test_inflight_custody_is_finalized_before_valid_recovery_or_exact_replay(
        benchmark_root, tmp_path):
    from walkworthy.open6_sol1 import select_public_items
    from walkworthy.open6_sol1_judge import (
        batch_scoring_units, build_judge_request, build_scoring_units,
    )

    judge_run = _module()
    item = select_public_items(benchmark_root)[0]
    model = "minimax/minimax-m3"
    units = build_scoring_units(
        item, _execution(item, model), model, "manifest-sha")
    batch = batch_scoring_units(units)[0]
    request = build_judge_request(batch)
    plan = judge_run._batch_plan_payload(batch, request)
    surface = {"requests": (request,), "plan_payloads": (plan,)}
    score_schema = request.score_schema["properties"]
    good = {"verdicts": [{
        "unit_key": key,
        "scores": {name: _first_allowed(schema)
                   for name, schema in score_schema.items()},
    } for key in request.expected_unit_keys]}
    final = json.dumps(good, sort_keys=True)

    class InflightLedger:
        def __init__(self):
            self.finish_event = None

        def _history(self, logical_key):
            return [1] if logical_key == request.logical_key else []

        def attempt_snapshot(self, attempt):
            return {
                "start": {"attempt_id": attempt,
                          "logical_key": request.logical_key},
                "finish": self.finish_event,
            }

        def finish(self, attempt, **kwargs):
            assert attempt == 1
            self.finish_event = dict(kwargs)

    ledger = InflightLedger()
    client = type("Client", (), {"ledger": ledger})()
    store = judge_run._attempt_store(tmp_path)
    store.append({
        "logical_key": request.logical_key,
        "attempt_id": 1,
        "prompt": request.prompt,
        "schema": request.schema,
        "final_text": final,
        "trace_jsonl": "",
        "stderr": "",
        "returncode": 0,
        "error_class": None,
        "payload_sha256": judge_run._text_hash(request.prompt),
        "schema_sha256": judge_run._hash(request.schema),
        "trace_sha256": judge_run._text_hash(""),
        "response_sha256": judge_run._text_hash(final),
        "error_sha256": None,
        "cli_version": "fake-sol",
        "usage": {},
    })

    judge_run._finalize_inflight_attempts(surface, tmp_path, client)
    assert ledger.finish_event["valid"] is True
    judge_run._reconcile_attempt_custody(surface, tmp_path, client)
    assert len(judge_run._result_store(tmp_path).records()) == 1

    from walkworthy.open6_sol1_runtime import SolTaskLedger

    replay_dir = tmp_path / "invalid-inflight"
    replay_dir.mkdir()
    replay_ledger = SolTaskLedger(
        replay_dir / "sol-attempts.jsonl", planned_cap=1,
        max_attempts=2, replay_cap=1, max_concurrency=1,
        _allow_inflight_on_open=True,
    )
    payload_hash = judge_run._text_hash(request.prompt)
    schema_hash = judge_run._hash(request.schema)
    first = replay_ledger.begin(request.logical_key, payload_hash, schema_hash)
    assert first == 1
    replay_client = type("Client", (), {"ledger": replay_ledger})()
    judge_run._finalize_inflight_attempts(surface, replay_dir, replay_client)
    retained = judge_run._attempt_store(replay_dir).records()
    assert len(retained) == 1
    assert retained[0]["attempt_id"] == first
    assert retained[0]["error_class"] == "interrupted"
    second = replay_ledger.begin(request.logical_key, payload_hash, schema_hash)
    assert second == 2
    assert replay_ledger.attempt_snapshot(second)["start"]["replay"] is True
    replay_ledger.finish(
        second, valid=False, error_class="interrupted",
        trace_sha256=None, response_sha256=None,
        error_sha256="6" * 64, cli_version="test", usage={},
    )


def test_explicit_terminal_unresolved_item_model_becomes_upstream_missingness(
        benchmark_root, tmp_path):
    judge_run = _module()
    missing_execution_key = "item:minimax/minimax-m3:WW-01-A01"
    manifest_path, run_dir = _seed_full_surface(
        benchmark_root, tmp_path, unresolved_key=missing_execution_key)

    plan = judge_run.prepare_judge_plan(
        benchmark_root, manifest_path, run_dir)
    assert plan["expected_execution_records"] == 2064
    assert plan["available_execution_records"] == 2063
    assert plan["expected_units"] == 5370
    assert plan["expected_category_cells"] == 10008
    assert plan["expected_batches"] == 227
    assert plan["upstream_missing_execution_records"] == 1
    assert plan["upstream_missing_units"] == 1
    assert plan["upstream_missing_category_cells"] == 2

    sol = FakeSolJudge()
    summary = judge_run.run_judging(
        benchmark_root, manifest_path, run_dir,
        sol_client=sol, max_workers=2)
    assert summary["terminal_complete"] is True
    assert summary["judge_complete"] is False
    assert summary["upstream_missing_execution_records"] == 1
    assert summary["upstream_missing_units"] == 1
    assert summary["upstream_missing_category_cells"] == 2
    assert summary["expected_batches"] == 227
    assert summary["terminal_batches"] == 227

    verdicts = judge_run.load_single_judge_verdicts(run_dir)
    missing = next(row for row in verdicts
                   if row["source_execution_key"] == missing_execution_key)
    assert missing["status"] == "unresolved"
    assert missing["verdict"] is None
    assert missing["total_units"] == 1
    assert missing["scored_units"] == 0
    assert missing["missing_category_cells"] == 2
    assert {row["missing_reason"] for row in missing["missing_units"]} == {
        "upstream_item_model_unresolved"
    }


def _terminal_row(item, model, *, source_role="sut", phase=None,
                  failure="interrupted"):
    phase = phase or ("classifier" if source_role == "classifier" else "content")
    source_key = (
        f"sol:classifier:{model}:{item.id}:001"
        if source_role == "classifier" else
        f"or:{model}:{item.id}:{phase}:001")
    return {
        "schema_version": (
            "walkworthy.open6-sol1.terminal-unresolved-item-model.v2"),
        "logical_key": f"item:{model}:{item.id}",
        "status": "terminal_unresolved",
        "item_id": item.id,
        "design": item.design,
        "model": model,
        "source_role": source_role,
        "source_logical_key": source_key,
        "phase": phase,
        "call_index": 1,
        "failure_class": failure,
        "attempt_ids": [1, 2],
    }


def test_terminal_unresolved_accepts_producer_valid_interrupted(
        benchmark_root, tmp_path):
    from walkworthy.open6_sol1 import select_public_items
    from walkworthy.open6_sol1_run import AppendOnlyStore

    judge_run = _module()
    item = select_public_items(benchmark_root)[0]
    model = "minimax/minimax-m3"
    AppendOnlyStore(
        tmp_path / judge_run.TERMINAL_UNRESOLVED_SUT_NAME,
        "terminal-unresolved-sut").append(_terminal_row(item, model))
    loaded = judge_run._load_terminal_unresolved(
        tmp_path, {f"item:{model}:{item.id}"}, {item.id: item}, [model])
    assert loaded[f"item:{model}:{item.id}"]["failure_class"] == "interrupted"


def test_terminal_unresolved_accepts_producer_valid_classifier_failure(
        benchmark_root, tmp_path):
    from walkworthy.open6_sol1 import select_public_items
    from walkworthy.open6_sol1_run import AppendOnlyStore

    judge_run = _module()
    item = select_public_items(benchmark_root)[0]
    model = "minimax/minimax-m3"
    AppendOnlyStore(
        tmp_path / judge_run.TERMINAL_UNRESOLVED_SUT_NAME,
        "terminal-unresolved-sut").append(
            _terminal_row(item, model, source_role="classifier"))
    loaded = judge_run._load_terminal_unresolved(
        tmp_path, {f"item:{model}:{item.id}"}, {item.id: item}, [model])
    row = loaded[f"item:{model}:{item.id}"]
    assert row["source_role"] == "classifier"
    assert row["phase"] == "classifier"


def test_terminal_unresolved_rejects_allocation_outside_design05(
        benchmark_root, tmp_path):
    from walkworthy.open6_sol1 import select_public_items
    from walkworthy.open6_sol1_run import AppendOnlyStore

    judge_run = _module()
    item = next(item for item in select_public_items(benchmark_root)
                if item.design != "05-ordoamoris")
    model = "minimax/minimax-m3"
    AppendOnlyStore(
        tmp_path / judge_run.TERMINAL_UNRESOLVED_SUT_NAME,
        "terminal-unresolved-sut").append(
            _terminal_row(item, model, phase="allocation", failure="malformed"))
    with pytest.raises(judge_run.ContractStop, match="terminal-unresolved"):
        judge_run._load_terminal_unresolved(
            tmp_path, {f"item:{model}:{item.id}"}, {item.id: item}, [model])
