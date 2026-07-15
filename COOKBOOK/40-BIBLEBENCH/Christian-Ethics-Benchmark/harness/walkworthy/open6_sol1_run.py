"""Resumable full-PUBLIC SUT orchestration for the OPEN6-SOL1 pilot.

This module deliberately stops at execution custody.  It does not judge, score,
aggregate, or make gate/release claims.  All network-bearing clients are injected;
the same code therefore supports a complete offline fake-backend dry run.
"""

from __future__ import annotations

import argparse
import copy
import fcntl
import hashlib
import json
import os
import re
import sys
import threading
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import contextmanager
from dataclasses import asdict
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Optional

from .clients import Message, ModelResponse
from .executors import (
    AdministrationResult,
    ItemExecution,
    TurnResult,
    execute_item,
    permuted_order,
)
from .manifest import FIXED_PERMUTATION_SEEDS
from .open6_sol1 import (
    build_manifest,
    canonical_json_bytes,
    select_public_items,
    sol_runtime_contract,
)
from .open6_sol1_runtime import (
    BudgetStop,
    ContractStop,
    MAX_CONCURRENCY,
    SOL_FAILURES,
    SUT_SPECS,
    ThreadStop,
)
from .parsers import AllocationParse


MANIFEST_NAME = "manifest.json"
CALL_CACHE_NAME = "sut-calls.jsonl"
ROUTING_CACHE_NAME = "sol-routing.jsonl"
EXECUTION_NAME = "executions.jsonl"
FAILURE_NAME = "failures.jsonl"
CHECKPOINT_NAME = "checkpoints.jsonl"
CATALOG_SNAPSHOT_NAME = "catalog-snapshot.json"
CATALOG_REVALIDATION_NAME = "catalog-revalidations.jsonl"
OPENROUTER_ATTEMPT_CUSTODY_NAME = "openrouter-attempt-custody.jsonl"
SOL_ATTEMPT_CUSTODY_NAME = "sol-attempt-custody.jsonl"
RUN_MODE_NAME = "run-mode.json"
TERMINAL_UNRESOLVED_NAME = "terminal-unresolved-sut.jsonl"

TERMINAL_SUT_FAILURES = frozenset({
    "http_failure", "empty", "malformed", "wrong_model", "missing_cost",
    "interrupted", "custody_failure",
})


class UnattendedStop(RuntimeError):
    """A registered systemic condition that must halt unattended execution."""


def _registered_sol_attempt_role(logical_key):
    if isinstance(logical_key, str) and logical_key.startswith("sol:classifier:"):
        return "classifier"
    if isinstance(logical_key, str) and logical_key.startswith("sol:judge:"):
        return "judge"
    raise ContractStop("unregistered Sol attempt prefix")


def _raise_if_systemic_terminal(source_role, custody_records, failure_class=None):
    """Halt only on the owner's narrow provider/OAuth systemic patterns."""
    if source_role == "sut":
        for record in custody_records:
            status = record.get("status")
            body_text = json.dumps(
                record.get("body", {}), ensure_ascii=False,
                sort_keys=True).casefold()
            if status in (401, 402, 403):
                raise UnattendedStop(
                    f"OpenRouter authorization/credit stop: HTTP {status}")
            if any(pattern in body_text for pattern in (
                    "no endpoints found", "no eligible provider",
                    "model unavailable", "model not found")):
                raise UnattendedStop(
                    "OpenRouter exact-model/provider unavailability stop")
            if (status is not None and status != 200
                    and status not in (408, 409, 425, 429)
                    and not (type(status) is int and 500 <= status <= 599)):
                raise UnattendedStop(
                    f"unregistered OpenRouter HTTP stop: {status}")
        if failure_class == "wrong_model":
            raise UnattendedStop("OpenRouter exact-model mismatch stop")
        return None
    if source_role == "classifier":
        for record in custody_records:
            stderr = record.get("stderr", "")
            error_class = record.get("error_class")
            if not isinstance(stderr, str):
                raise UnattendedStop("unregistered Sol stderr custody")
            lowered = stderr.casefold()
            if any(pattern in lowered for pattern in (
                    "usage limit", "usage_limit", "quota exceeded",
                    "insufficient quota")):
                raise UnattendedStop("Sol OAuth quota/usage-limit stop")
            if error_class == "cli_failure":
                raise UnattendedStop("unregistered Sol CLI failure stop")
        return None
    raise ContractStop("invalid terminal source role")


def _canonical_line(value) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True,
                       separators=(",", ":")) + "\n").encode("utf-8")


def _hash(value) -> str:
    return hashlib.sha256(_canonical_line(value)).hexdigest()


def text_sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def value_sha256(value) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def transport_payload_hash(payload) -> str:
    """Match the registered OpenRouter transport's exact JSON-byte hashing."""
    return hashlib.sha256(json.dumps(payload).encode("utf-8")).hexdigest()


def _ledger_attempts_for_key(ledger, logical_key, candidate_ids=()):
    """Return every persisted attempt for one key using the ledger's public API."""
    ids = {attempt for attempt in candidate_ids if type(attempt) is int}
    snapshot_method = getattr(ledger, "snapshot", None)
    if callable(snapshot_method):
        summary = snapshot_method()
        total = summary.get("attempts") if isinstance(summary, dict) else None
        if type(total) is not int or total < 0:
            raise ContractStop("invalid attempt-ledger snapshot")
        persisted_starts = getattr(ledger, "_starts", None)
        if not isinstance(persisted_starts, dict):
            persisted_starts = getattr(ledger, "starts", None)
        if isinstance(persisted_starts, dict):
            for attempt, start in persisted_starts.items():
                if (type(attempt) is int and isinstance(start, dict)
                        and start.get("logical_key") == logical_key):
                    ids.add(attempt)
        else:
            for attempt in range(1, total + 1):
                snapshot = ledger.attempt_snapshot(attempt)
                if (snapshot.get("start") or {}).get("logical_key") == logical_key:
                    ids.add(attempt)
    return [(attempt, ledger.attempt_snapshot(attempt))
            for attempt in sorted(ids)]


def _merge_attempt_ids(prefix, current):
    attempt_ids = list(prefix) + list(current)
    if (not attempt_ids or any(type(attempt) is not int for attempt in attempt_ids)
            or len(attempt_ids) != len(set(attempt_ids))):
        raise ContractStop("invalid recovered attempt lineage")
    return attempt_ids


def _raise_recovered_second_failure(source_role, logical_key, attempts):
    """Convert a crash-stranded exhausted replay into the registered stop seam."""
    if len(attempts) > 2:
        raise ContractStop(f"too many recovered attempts for {logical_key}")
    if len(attempts) < 2:
        return None
    finishes = [snapshot.get("finish") for _, snapshot in attempts]
    if source_role == "sut":
        if any(finish is None or finish.get("failure") is None
               for finish in finishes):
            raise ContractStop(
                f"recovered OpenRouter replay is not exhausted: {logical_key}")
        failure = finishes[-1].get("failure")
        raise ThreadStop(
            f"OpenRouter second failure for {logical_key}: {failure}")
    if source_role == "classifier":
        if any(finish is None or finish.get("valid") is not False
               or finish.get("error_class") is None for finish in finishes):
            raise ContractStop(
                f"recovered Sol replay is not exhausted: {logical_key}")
        failure = finishes[-1].get("error_class")
        raise ThreadStop(f"Sol second failure for {logical_key}: {failure}")
    raise ContractStop("invalid recovered-attempt source role")


_LOCKS = {}
_LOCKS_GUARD = threading.Lock()


def _local_lock(path: Path):
    key = str(path.resolve())
    with _LOCKS_GUARD:
        return _LOCKS.setdefault(key, threading.RLock())


class AppendOnlyStore:
    """Strict, fsynced, hash-chained JSONL storage with unique logical keys.

    ``key_field`` can be changed to ``attempt_id`` for replay-bearing attempt
    custody, or set to ``None`` when uniqueness is not part of that artifact's
    contract.  ``append_sink`` is directly compatible with runtime custody sinks.
    """

    def __init__(self, path, store_kind: str, key_field: Optional[str] = "logical_key"):
        self.path = Path(path)
        self.lock_path = Path(str(self.path) + ".lock")
        if not isinstance(store_kind, str) or not store_kind:
            raise ContractStop("invalid append-only store kind")
        if key_field is not None and (not isinstance(key_field, str) or not key_field):
            raise ContractStop("invalid append-only key field")
        self.store_kind = store_kind
        self.key_field = key_field
        self.lock_path.parent.mkdir(parents=True, exist_ok=True)
        self._lock_handle = self.lock_path.open("a+", encoding="utf-8")
        self._local = _local_lock(self.lock_path)
        self._append_fd = None
        self._cache = None
        self._key_index = None
        self._loaded_size = None

    @contextmanager
    def _locked(self):
        with self._local:
            fcntl.flock(self._lock_handle.fileno(), fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(self._lock_handle.fileno(), fcntl.LOCK_UN)

    @staticmethod
    def _record_hash(record):
        return _hash({key: value for key, value in record.items()
                      if key != "record_sha256"})

    def _read_unlocked(self):
        if not self.path.exists():
            self._cache = []
            self._key_index = {} if self.key_field is not None else None
            self._loaded_size = 0
            return self._cache
        try:
            lines = self.path.read_text(encoding="utf-8").splitlines()
        except OSError as exc:
            raise ContractStop(f"cannot read {self.store_kind}") from exc
        records = []
        previous = None
        seen = set()
        for sequence, line in enumerate(lines, 1):
            try:
                record = json.loads(line)
            except (json.JSONDecodeError, TypeError) as exc:
                raise ContractStop(
                    f"{self.store_kind} invalid JSON at line {sequence}") from exc
            if (not isinstance(record, dict)
                    or record.get("store_kind") != self.store_kind
                    or record.get("sequence") != sequence
                    or record.get("previous_sha256") != previous
                    or record.get("record_sha256") != self._record_hash(record)):
                raise ContractStop(
                    f"{self.store_kind} hash-chain failure at line {sequence}")
            if self.key_field is not None:
                key = record.get(self.key_field)
                if key is None or isinstance(key, (dict, list)) or key in seen:
                    raise ContractStop(
                        f"{self.store_kind} invalid or duplicate {self.key_field}")
                seen.add(key)
            records.append(record)
            previous = record["record_sha256"]
        self._cache = records
        self._key_index = ({record[self.key_field]: record for record in records}
                           if self.key_field is not None else None)
        self._loaded_size = self.path.stat().st_size
        return records

    def _refresh_unlocked(self):
        size = self.path.stat().st_size if self.path.exists() else 0
        if self._cache is None or self._loaded_size != size:
            return self._read_unlocked()
        return self._cache

    def records(self):
        with self._locked():
            return copy.deepcopy(self._refresh_unlocked())

    def by_key(self):
        if self.key_field is None:
            raise ContractStop(f"{self.store_kind} has no unique key")
        with self._locked():
            self._refresh_unlocked()
            return copy.deepcopy(self._key_index)

    def get(self, key):
        if self.key_field is None:
            raise ContractStop(f"{self.store_kind} has no unique key")
        with self._locked():
            self._refresh_unlocked()
            return copy.deepcopy(self._key_index.get(key))

    def append(self, record: dict):
        if not isinstance(record, dict):
            raise ContractStop(f"{self.store_kind} record must be an object")
        record = copy.deepcopy(record)
        if self.store_kind == "openrouter-attempt-custody" and "body" in record:
            declared = record.get("body_sha256")
            actual = value_sha256(record["body"])
            if declared is not None and declared != actual:
                raise ContractStop("OpenRouter custody body hash mismatch")
            record["body_sha256"] = actual
        reserved = {"store_kind", "sequence", "previous_sha256", "record_sha256"}
        if reserved & set(record):
            raise ContractStop(f"{self.store_kind} record uses reserved fields")
        with self._locked():
            records = self._refresh_unlocked()
            if self.key_field is not None:
                key = record.get(self.key_field)
                if key is None or isinstance(key, (dict, list)):
                    raise ContractStop(
                        f"{self.store_kind} missing valid {self.key_field}")
                if key in self._key_index:
                    raise ContractStop(
                        f"{self.store_kind} duplicate {self.key_field}: {key}")
            stored = copy.deepcopy(record)
            stored.update({
                "store_kind": self.store_kind,
                "sequence": len(records) + 1,
                "previous_sha256": (
                    records[-1]["record_sha256"] if records else None),
            })
            stored["record_sha256"] = self._record_hash(stored)
            self.path.parent.mkdir(parents=True, exist_ok=True)
            if self._append_fd is None:
                self._append_fd = os.open(
                    self.path, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600)
            encoded = _canonical_line(stored)
            pending = memoryview(encoded)
            while pending:
                written = os.write(self._append_fd, pending)
                if written <= 0:
                    raise OSError(f"short append to {self.store_kind}")
                pending = pending[written:]
            os.fsync(self._append_fd)
            records.append(stored)
            if self._key_index is not None:
                self._key_index[stored[self.key_field]] = stored
            self._loaded_size = self.path.stat().st_size
            return copy.deepcopy(stored)

    def append_sink(self, record):
        return self.append(record)


class SoftBudgetGuard:
    """Owner-registered $15 checkpoint and conservative $23 continuation guard."""

    BOOKED_TRIGGER = Decimal("15.00")
    PROJECTED_TOTAL_CAP = Decimal("23.00")

    def __init__(self, expected_calls, call_store, terminal_store, ledger,
                 checkpoint_store):
        self.expected_calls = frozenset(expected_calls)
        self.call_store = call_store
        self.terminal_store = terminal_store
        self.ledger = ledger
        self.checkpoint_store = checkpoint_store
        self._lock = threading.Lock()
        self._persisted = False

    def projection(self):
        specs = {spec.slug: spec for spec in SUT_SPECS}
        if any(spec.input_envelope != 24000 or spec.max_tokens != 2048
               for spec in specs.values()):
            raise ContractStop("soft-budget projection envelope drift")
        terminal_prefixes = set()
        for row in self.terminal_store.records():
            model, item_id = row.get("model"), row.get("item_id")
            if not isinstance(model, str) or not isinstance(item_id, str):
                raise ContractStop("invalid terminal surface in budget projection")
            prefix = f"or:{model}:{item_id}:"
            if (row.get("logical_key") != f"item:{model}:{item_id}"
                    or not any(key.startswith(prefix) for key in self.expected_calls)):
                raise ContractStop("unregistered terminal budget exclusion")
            terminal_prefixes.add(prefix)
        active_expected = {
            key for key in self.expected_calls
            if not any(key.startswith(prefix) for prefix in terminal_prefixes)
        }
        completed = {row.get("logical_key") for row in self.call_store.records()}
        if not completed.issubset(self.expected_calls):
            raise ContractStop("unregistered SUT call in budget projection")
        remaining = active_expected - completed
        by_model = Counter()
        for logical_key in remaining:
            parts = logical_key.split(":", 4)
            if len(parts) != 5 or parts[0] != "or" or parts[1] not in specs:
                raise ContractStop("invalid nominal call in budget projection")
            by_model[parts[1]] += 1
        ceilings = {
            slug: specs[slug].max_call_usd_for_input(specs[slug].input_envelope)
            for slug in by_model
        }
        nominal_projection = sum((
            ceilings[slug] * count for slug, count in by_model.items()
        ), Decimal("0"))
        snapshot = self.ledger.snapshot()
        try:
            booked = Decimal(str(snapshot["booked_usd"]))
        except (KeyError, InvalidOperation) as exc:
            raise ContractStop("invalid booked spend in soft-budget projection") from exc
        replays = snapshot.get("replays")
        replay_cap = getattr(self.ledger, "replay_cap", None)
        if (not booked.is_finite() or booked < 0
                or type(replays) is not int or replays < 0
                or type(replay_cap) is not int or not 0 <= replays <= replay_cap):
            raise ContractStop("invalid ledger state in soft-budget projection")
        unused_replays = replay_cap - replays
        max_remaining_ceiling = max(ceilings.values(), default=Decimal("0"))
        replay_projection = max_remaining_ceiling * unused_replays
        conservative_projection = nominal_projection + replay_projection
        projected_total = booked + conservative_projection
        threshold = booked >= self.BOOKED_TRIGGER
        authorized = not threshold or projected_total <= self.PROJECTED_TOTAL_CAP
        return {
            "schema_version": "walkworthy.open6-sol1.soft-budget-projection.v1",
            "soft_booked_trigger_usd": str(self.BOOKED_TRIGGER),
            "soft_projected_total_cap_usd": str(self.PROJECTED_TOTAL_CAP),
            "booked_usd": str(booked),
            "remaining_nominal_calls": len(remaining),
            "remaining_nominal_calls_by_model": dict(sorted(by_model.items())),
            "remaining_nominal_projection_usd": str(nominal_projection),
            "unused_replay_slots": unused_replays,
            "maximum_remaining_call_ceiling_usd": str(max_remaining_ceiling),
            "replay_projection_usd": str(replay_projection),
            "conservative_projection_usd": str(conservative_projection),
            "projected_total_usd": str(projected_total),
            "threshold_triggered": threshold,
            "continue_authorized": authorized,
        }

    def before_request(self):
        with self._lock:
            projection = self.projection()
            if projection["threshold_triggered"] and not self._persisted:
                sequence = len(self.checkpoint_store.records()) + 1
                self.checkpoint_store.append({
                    "logical_key": f"soft-budget-check:{sequence:06d}",
                    "checkpoint_type": "soft_budget_pre_request",
                    **projection,
                })
                self._persisted = True
            if not projection["continue_authorized"]:
                raise BudgetStop(
                    "OPEN6-SOL1 soft projected-total cap blocks pre-request")
            return projection


def prepare_run(benchmark_root, manifest_path, run_dir) -> dict:
    """Validate the exact frozen manifest and copy it immutably into the run."""
    expected = canonical_json_bytes(build_manifest(benchmark_root))
    source = Path(manifest_path)
    if not source.is_file() or source.read_bytes() != expected:
        raise ContractStop("OPEN6-SOL1 immutable manifest mismatch")
    out = Path(run_dir)
    out.mkdir(parents=True, exist_ok=True)
    target = out / MANIFEST_NAME
    if target.exists():
        if target.read_bytes() != expected:
            raise ContractStop("OPEN6-SOL1 run manifest mismatch")
    else:
        with target.open("xb") as handle:
            handle.write(expected)
    return json.loads(expected)


def _catalog_decimal(value, field):
    if isinstance(value, bool) or not isinstance(value, (str, int, float, Decimal)):
        raise ContractStop(f"invalid catalog {field}")
    try:
        parsed = Decimal(str(value))
    except InvalidOperation as exc:
        raise ContractStop(f"invalid catalog {field}") from exc
    if not parsed.is_finite() or parsed < 0:
        raise ContractStop(f"invalid catalog {field}")
    return parsed


def _catalog_artifact(manifest, raw_snapshot):
    if (not isinstance(raw_snapshot, dict)
            or not isinstance(raw_snapshot.get("fetched_at"), str)
            or not raw_snapshot["fetched_at"]
            or not isinstance(raw_snapshot.get("source_urls"), list)
            or not raw_snapshot["source_urls"]
            or not all(isinstance(url, str) and url.startswith("https://")
                       for url in raw_snapshot["source_urls"])
            or not isinstance(raw_snapshot.get("raw_api_responses"), list)
            or not isinstance(raw_snapshot.get("models"), list)):
        raise ContractStop("invalid OpenRouter catalog snapshot envelope")
    registered = {row["slug"]: row for row in manifest["openrouter"]["models"]}
    observed = {}
    eligible = []
    for row in raw_snapshot["models"]:
        if (not isinstance(row, dict) or set(row) != {"slug", "providers"}
                or row.get("slug") in observed
                or not isinstance(row.get("providers"), list)
                or not row["providers"]):
            raise ContractStop("invalid or duplicate catalog model")
        slug = row["slug"]
        if slug not in registered:
            raise ContractStop(f"catalog contains unregistered model: {slug}")
        observed[slug] = row
        ceiling = registered[slug]["provider_ceiling"]
        model_eligible = []
        for provider in row["providers"]:
            if (not isinstance(provider, dict)
                    or set(provider) != {
                        "provider", "input_per_m_usd", "output_per_m_usd"}
                    or not isinstance(provider.get("provider"), str)
                    or not provider["provider"]):
                raise ContractStop(f"invalid catalog provider for {slug}")
            input_price = _catalog_decimal(
                provider["input_per_m_usd"], "input price")
            output_price = _catalog_decimal(
                provider["output_per_m_usd"], "output price")
            if (input_price <= Decimal(ceiling["prompt_per_m_usd"])
                    and output_price <= Decimal(
                        ceiling["completion_per_m_usd"])):
                model_eligible.append({
                    "slug": slug,
                    "provider": provider["provider"],
                    "input_per_m_usd": str(input_price),
                    "output_per_m_usd": str(output_price),
                })
        if not model_eligible:
            raise ContractStop(f"catalog has no eligible provider for {slug}")
        eligible.extend(model_eligible)
    if set(observed) != set(registered):
        missing = sorted(set(registered) - set(observed))
        raise ContractStop(f"catalog missing exact registered models: {missing}")
    raw_hash = _hash(raw_snapshot)
    return {
        "schema_version": "walkworthy.open6-sol1.catalog-snapshot.v1",
        "pilot": manifest["pilot"],
        "fetched_at": raw_snapshot["fetched_at"],
        "source_urls": raw_snapshot["source_urls"],
        "raw_canonical_sha256": raw_hash,
        "raw_snapshot": copy.deepcopy(raw_snapshot),
        "validated_model_count": len(observed),
        "eligible_providers": eligible,
    }


def register_catalog_snapshot(benchmark_root, manifest_path, run_dir, raw_snapshot):
    """Freeze an already-fetched catalog observation; this function never networks."""
    manifest = prepare_run(benchmark_root, manifest_path, run_dir)
    artifact = _catalog_artifact(manifest, raw_snapshot)
    path = Path(run_dir) / CATALOG_SNAPSHOT_NAME
    expected = canonical_json_bytes(artifact)
    if path.exists():
        if path.read_bytes() != expected:
            raise ContractStop("immutable OpenRouter catalog snapshot mismatch")
    else:
        with path.open("xb") as handle:
            handle.write(expected)
    return artifact


def validate_catalog_snapshot(benchmark_root, manifest_path, run_dir):
    manifest = prepare_run(benchmark_root, manifest_path, run_dir)
    path = Path(run_dir) / CATALOG_SNAPSHOT_NAME
    if not path.is_file():
        raise ContractStop("OpenRouter catalog snapshot is not registered")
    try:
        artifact = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ContractStop("invalid OpenRouter catalog snapshot JSON") from exc
    expected = _catalog_artifact(manifest, artifact.get("raw_snapshot"))
    if path.read_bytes() != canonical_json_bytes(expected):
        raise ContractStop("OpenRouter catalog snapshot hash mismatch")
    return artifact


def _catalog_revalidation_record(manifest, frozen_catalog_sha256,
                                 recovery_trigger, artifact, sequence):
    if recovery_trigger not in ("provider_recovery", "oauth_recovery"):
        raise ContractStop("invalid catalog revalidation trigger")
    ceilings = [{
        "slug": row["slug"],
        "provider_ceiling": copy.deepcopy(row["provider_ceiling"]),
    } for row in manifest["openrouter"]["models"]]
    return {
        "schema_version": "walkworthy.open6-sol1.catalog-revalidation.v1",
        "logical_key": f"catalog-revalidation:{sequence:06d}",
        "pilot": manifest["pilot"],
        "recovery_trigger": recovery_trigger,
        "frozen_catalog_sha256": frozen_catalog_sha256,
        "registered_roster": [
            row["slug"] for row in manifest["openrouter"]["models"]],
        "provider_ceilings_sha256": _hash(ceilings),
        "fetched_at": artifact["fetched_at"],
        "source_urls": copy.deepcopy(artifact["source_urls"]),
        "raw_canonical_sha256": artifact["raw_canonical_sha256"],
        "raw_snapshot": copy.deepcopy(artifact["raw_snapshot"]),
        "validated_model_count": artifact["validated_model_count"],
        "eligible_providers": copy.deepcopy(artifact["eligible_providers"]),
    }


def validate_catalog_revalidations(benchmark_root, manifest_path, run_dir):
    """Validate every append-only recovery observation without networking."""
    manifest = prepare_run(benchmark_root, manifest_path, run_dir)
    validate_catalog_snapshot(benchmark_root, manifest_path, run_dir)
    frozen_path = Path(run_dir) / CATALOG_SNAPSHOT_NAME
    frozen_hash = hashlib.sha256(frozen_path.read_bytes()).hexdigest()
    store = AppendOnlyStore(
        Path(run_dir) / CATALOG_REVALIDATION_NAME, "catalog-revalidations")
    rows = store.records()
    envelope = {"store_kind", "sequence", "previous_sha256", "record_sha256"}
    for sequence, row in enumerate(rows, 1):
        artifact = _catalog_artifact(manifest, row.get("raw_snapshot"))
        expected = _catalog_revalidation_record(
            manifest, frozen_hash, row.get("recovery_trigger"),
            artifact, sequence)
        if {key: value for key, value in row.items()
                if key not in envelope} != expected:
            raise ContractStop("catalog revalidation contract mismatch")
    return rows


def register_catalog_revalidation(benchmark_root, manifest_path, run_dir,
                                  raw_snapshot, *, recovery_trigger):
    """Append one roster/ceiling-preserving post-recovery catalog observation."""
    manifest = prepare_run(benchmark_root, manifest_path, run_dir)
    validate_catalog_snapshot(benchmark_root, manifest_path, run_dir)
    existing = validate_catalog_revalidations(
        benchmark_root, manifest_path, run_dir)
    artifact = _catalog_artifact(manifest, raw_snapshot)
    frozen_hash = hashlib.sha256(
        (Path(run_dir) / CATALOG_SNAPSHOT_NAME).read_bytes()).hexdigest()
    record = _catalog_revalidation_record(
        manifest, frozen_hash, recovery_trigger, artifact, len(existing) + 1)
    return AppendOnlyStore(
        Path(run_dir) / CATALOG_REVALIDATION_NAME,
        "catalog-revalidations").append(record)


def _register_run_mode(run_dir, offline_fake):
    path = Path(run_dir) / RUN_MODE_NAME
    payload = {
        "schema_version": "walkworthy.open6-sol1.run-mode.v1",
        "mode": "offline_fake" if offline_fake else "live",
    }
    expected = canonical_json_bytes(payload)
    if path.exists():
        if path.read_bytes() != expected:
            raise ContractStop("OPEN6-SOL1 run mode cannot change")
    else:
        with path.open("xb") as handle:
            handle.write(expected)
    return payload["mode"]


def _read_run_mode(run_dir):
    path = Path(run_dir) / RUN_MODE_NAME
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ContractStop("invalid OPEN6-SOL1 run mode") from exc
    if payload not in (
            {"schema_version": "walkworthy.open6-sol1.run-mode.v1",
             "mode": "offline_fake"},
            {"schema_version": "walkworthy.open6-sol1.run-mode.v1",
             "mode": "live"}):
        raise ContractStop("invalid OPEN6-SOL1 run mode")
    if path.read_bytes() != canonical_json_bytes(payload):
        raise ContractStop("noncanonical OPEN6-SOL1 run mode")
    return payload["mode"]


def _message_payload(messages, system):
    return {
        "system": system,
        "messages": [{"role": message.role, "content": message.content}
                     for message in messages],
    }


def _response_payload(response: ModelResponse):
    return {
        "text": response.text,
        "model": response.model,
        "family": response.family,
        "refused_hint": bool(response.refused_hint),
        "usage": copy.deepcopy(response.usage),
        "raw": copy.deepcopy(response.raw),
    }


def _response_from_payload(payload):
    required = {"text", "model", "family", "refused_hint", "usage", "raw"}
    if (not isinstance(payload, dict) or set(payload) != required
            or not isinstance(payload["text"], str) or not payload["text"].strip()
            or not isinstance(payload["model"], str)
            or not isinstance(payload["family"], str)
            or type(payload["refused_hint"]) is not bool
            or not isinstance(payload["usage"], dict)
            or not isinstance(payload["raw"], dict)):
        raise ContractStop("invalid cached SUT response")
    return ModelResponse(**copy.deepcopy(payload))


class CachedSutClient:
    """Executor-compatible SUT client with deterministic call-level resume."""

    def __init__(self, slug: str, delegate, cache: AppendOnlyStore, *,
                 attempt_custody: Optional[AppendOnlyStore] = None, ledger=None,
                 budget_guard=None):
        self.name = slug
        self.family = slug.split("/", 1)[0]
        self.delegate = delegate
        self.cache = cache
        self.attempt_custody = attempt_custody
        self.ledger = ledger
        self.budget_guard = budget_guard
        self._context = threading.local()
        self._last_record = threading.local()

    @contextmanager
    def item_context(self, item, phase):
        if phase not in ("content", "allocation"):
            raise ContractStop(f"invalid SUT call phase: {phase}")
        if getattr(self._context, "active", False):
            raise ContractStop("nested SUT item context")
        self._context.active = True
        self._context.item_id = item.id
        self._context.design = item.design
        self._context.phase = phase
        self._context.call_index = 0
        try:
            yield self
        finally:
            self._context.active = False

    @property
    def last_call_record(self):
        return copy.deepcopy(getattr(self._last_record, "value", None))

    def complete(self, messages, system=None, *, response_validator=None, **_kwargs):
        if not getattr(self._context, "active", False):
            raise ContractStop("SUT call outside item context")
        self._context.call_index += 1
        logical_key = (
            f"or:{self.name}:{self._context.item_id}:"
            f"{self._context.phase}:{self._context.call_index:03d}"
        )
        request = _message_payload(messages, system)
        request_sha256 = _hash(request)
        existing = self.cache.get(logical_key)
        if existing is not None:
            if (existing.get("model") != self.name
                    or existing.get("item_id") != self._context.item_id
                    or existing.get("design") != self._context.design
                    or existing.get("phase") != self._context.phase
                    or existing.get("call_index") != self._context.call_index
                    or existing.get("request_sha256") != request_sha256
                    or existing.get("request") != request):
                raise ContractStop(f"SUT call-cache contract mismatch: {logical_key}")
            response = _response_from_payload(existing.get("response"))
            if response_validator is not None:
                if response_validator(copy.deepcopy(response),
                                      copy.deepcopy(existing.get("body"))) is not True:
                    raise ContractStop(f"cached response validator drift: {logical_key}")
            self._last_record.value = existing
            return response

        self._recovery_attempt_ids = getattr(
            self, "_recovery_attempt_ids", threading.local())
        self._recovery_attempt_ids.value = []
        recovered = self._recover_attempt(
            logical_key, request, request_sha256, messages, system,
            response_validator,
        )
        if recovered is not None:
            self._last_record.value = recovered
            return _response_from_payload(recovered["response"])

        if self.budget_guard is not None:
            self.budget_guard.before_request()
        result = self.delegate.complete(
            logical_key, messages, system=system,
            response_validator=response_validator,
        )
        response = getattr(result, "response", None)
        if not isinstance(response, ModelResponse) or response.model != self.name:
            raise ContractStop(f"invalid exact-model SUT result: {logical_key}")
        record = self.cache.append({
            "logical_key": logical_key,
            "model": self.name,
            "item_id": self._context.item_id,
            "design": self._context.design,
            "phase": self._context.phase,
            "call_index": self._context.call_index,
            "request_sha256": request_sha256,
            "request": request,
            "response": _response_payload(response),
            "body": copy.deepcopy(getattr(result, "body", {})),
            "payload": copy.deepcopy(getattr(result, "payload", {})),
            "attempt_ids": _merge_attempt_ids(
                self._recovery_attempt_ids.value,
                getattr(result, "attempt_ids", ())),
        })
        self._last_record.value = record
        return response

    def _recover_attempt(self, logical_key, request, request_sha256, messages,
                         system, response_validator):
        """Reconcile crash-stranded paid work before considering one exact replay."""
        if self.attempt_custody is None or self.ledger is None:
            return None
        base = getattr(self.delegate, "base_client", None)
        if base is None or not callable(getattr(base, "build_payload", None)):
            raise ContractStop("SUT attempt recovery lacks exact payload builder")
        payload = base.build_payload(messages, system)
        payload_hash = transport_payload_hash(payload)
        candidates = [record for record in self.attempt_custody.records()
                      if record.get("logical_key") == logical_key]
        custody_by_id = {}
        for custody in candidates:
            attempt_id = custody.get("attempt_id")
            if type(attempt_id) is not int or attempt_id in custody_by_id:
                raise ContractStop(
                    f"invalid OpenRouter attempt custody id: {logical_key}")
            custody_by_id[attempt_id] = custody
        attempts = _ledger_attempts_for_key(
            self.ledger, logical_key, custody_by_id)
        for attempt_id, snapshot in attempts:
            start = snapshot.get("start") or {}
            finish = snapshot.get("finish")
            if (start.get("logical_key") != logical_key
                    or start.get("requested_model") != self.name
                    or start.get("payload_sha256") != payload_hash):
                raise ContractStop(
                    f"OpenRouter attempt start does not cross-bind: {attempt_id}")
            custody = custody_by_id.get(attempt_id)
            if custody is None:
                if finish is None:
                    self.ledger.finish(
                        attempt_id, None, {}, failure_override="custody_failure",
                        error_detail={"type": "missing_attempt_custody"},
                    )
                    finish = self.ledger.attempt_snapshot(attempt_id).get("finish")
                if finish is None or finish.get("failure") is None:
                    raise ContractStop(
                        f"valid OpenRouter finish lacks custody: {attempt_id}")
                continue
            body = custody.get("body")
            status = custody.get("status")
            if ((status is not None
                 and (type(status) is not int or not 100 <= status <= 599))
                    or not isinstance(body, dict)
                    or custody.get("body_sha256") != value_sha256(body)):
                raise ContractStop(
                    f"OpenRouter attempt custody integrity failure: {attempt_id}")
            usage = body.get("usage")
            choices = body.get("choices")
            required_valid = (
                status == 200
                and body.get("model") == self.name
                and isinstance(usage, dict)
                and not isinstance(usage.get("cost"), bool)
                and isinstance(usage.get("cost"), (int, float))
                and isinstance(choices, list) and bool(choices)
                and isinstance(choices[0], dict)
                and isinstance(choices[0].get("message"), dict)
                and isinstance(choices[0]["message"].get("content"), str)
                and bool(choices[0]["message"]["content"].strip())
            )
            response = None
            if required_valid:
                try:
                    reported_cost = Decimal(str(usage["cost"]))
                except (KeyError, InvalidOperation):
                    required_valid = False
                else:
                    required_valid = reported_cost.is_finite() and reported_cost >= 0
            if required_valid:
                response = ModelResponse(
                    text=choices[0]["message"]["content"], model=self.name,
                    family=self.family, usage=copy.deepcopy(usage),
                    raw={"backend": "openrouter", "model": self.name},
                )
            validation_error = None
            if required_valid and response_validator is not None:
                try:
                    accepted = response_validator(
                        copy.deepcopy(response), copy.deepcopy(body))
                except Exception as exc:
                    validation_error = {
                        "type": exc.__class__.__name__, "message": str(exc),
                    }
                    required_valid = False
                else:
                    if accepted is not True:
                        validation_error = {
                            "type": "response_validation_failed",
                        }
                        required_valid = False
            if finish is None:
                kwargs = {}
                if (status == 200 and body.get("model") == self.name
                        and isinstance(usage, dict)
                        and not isinstance(usage.get("cost"), bool)
                        and isinstance(usage.get("cost"), (int, float))
                        and isinstance(choices, list) and choices
                        and isinstance(choices[0], dict)
                        and isinstance(choices[0].get("message"), dict)
                        and isinstance(choices[0]["message"].get("content"), str)
                        and choices[0]["message"]["content"].strip()
                        and not required_valid):
                    kwargs = {
                        "failure_override": "malformed",
                        "error_detail": validation_error,
                    }
                self.ledger.finish(
                    attempt_id, status, copy.deepcopy(body), **kwargs)
                finish = self.ledger.attempt_snapshot(attempt_id).get("finish")
            if (finish is None
                    or finish.get("status") != status
                    or finish.get("response_sha256") != value_sha256(body)
                    or finish.get("returned_model")
                    != (body.get("model")
                        if isinstance(body.get("model"), str) else None)):
                raise ContractStop(
                    f"OpenRouter ledger/custody finish mismatch: {attempt_id}")
            if finish.get("failure") is not None:
                self._recovery_attempt_ids.value.append(attempt_id)
                continue
            if not required_valid or response is None:
                raise ContractStop(
                    f"successful OpenRouter finish has invalid output: {attempt_id}")
            if (not isinstance(usage, dict)
                    or isinstance(usage.get("cost"), bool)
                    or not isinstance(usage.get("cost"), (int, float))
                    or not isinstance(choices, list) or not choices):
                raise ContractStop(
                    f"invalid successful OpenRouter custody: {attempt_id}")
            try:
                reported_cost = Decimal(str(usage["cost"]))
                booked_cost = Decimal(str(finish.get("booked_usd")))
            except (KeyError, InvalidOperation):
                raise ContractStop(
                    f"invalid OpenRouter cost custody: {attempt_id}")
            if (not reported_cost.is_finite() or reported_cost < 0
                    or booked_cost != reported_cost
                    or finish.get("cost_basis") != "reported"
                    or finish.get("returned_model") != body.get("model")
                    or finish.get("prompt_tokens") != usage.get("prompt_tokens", 0)
                    or finish.get("completion_tokens")
                    != usage.get("completion_tokens", 0)):
                raise ContractStop(
                    f"OpenRouter cost custody does not cross-bind: {attempt_id}")
            return self.cache.append({
                "logical_key": logical_key,
                "model": self.name,
                "item_id": self._context.item_id,
                "design": self._context.design,
                "phase": self._context.phase,
                "call_index": self._context.call_index,
                "request_sha256": request_sha256,
                "request": request,
                "response": _response_payload(response),
                "body": copy.deepcopy(body),
                "payload": copy.deepcopy(payload),
                "attempt_ids": [attempt_id],
                "recovered_from_attempt_id": attempt_id,
            })
        orphan_ids = set(custody_by_id) - {attempt for attempt, _ in attempts}
        if orphan_ids:
            raise ContractStop(
                f"orphan OpenRouter attempt custody: {sorted(orphan_ids)}")
        _raise_recovered_second_failure("sut", logical_key, attempts)
        return None


def classifier_contract_payload(design, opaque_key, allowed_states,
                                assistant_response):
    contract = sol_runtime_contract()["classifier"]
    user = (contract["prompt"]["user_template"]
            .replace("{{DESIGN}}", design)
            .replace("{{OPAQUE_KEY}}", opaque_key)
            .replace("{{ALLOWED_STATES_JSON}}", json.dumps(
                list(allowed_states), ensure_ascii=False, separators=(",", ":")))
            .replace("{{ASSISTANT_RESPONSE_JSON}}", json.dumps(
                assistant_response, ensure_ascii=False, separators=(",", ":"))))
    prompt = contract["prompt"]["system_text"] + "\n\n" + user
    schema = {
        "type": "object", "additionalProperties": False,
        "required": ["state"],
        "properties": {
            "state": {"type": "string", "enum": list(allowed_states)},
        },
    }
    return prompt, schema


class CachedSolClassifier:
    """Strict Sol-only state router with deterministic result-level resume."""

    def __init__(self, model: str, sol_client, cache: AppendOnlyStore, *,
                 attempt_custody: Optional[AppendOnlyStore] = None, ledger=None):
        self.model = model
        self.sol_client = sol_client
        self.cache = cache
        self.attempt_custody = attempt_custody
        self.ledger = ledger
        self._context = threading.local()

    @contextmanager
    def item_context(self, item):
        if getattr(self._context, "active", False):
            raise ContractStop("nested classifier item context")
        self._context.active = True
        self._context.item_id = item.id
        self._context.design = item.design
        self._context.index = 0
        try:
            yield self
        finally:
            self._context.active = False

    def __call__(self, assistant_response, allowed_states, design):
        if not getattr(self._context, "active", False):
            raise ContractStop("classifier call outside item context")
        if design != self._context.design:
            raise ContractStop("classifier design context mismatch")
        states = list(allowed_states)
        if (not states or len(states) != len(set(states))
                or not all(isinstance(state, str) and state for state in states)):
            raise ContractStop("invalid classifier states")
        self._context.index += 1
        logical_key = (
            f"sol:classifier:{self.model}:{self._context.item_id}:"
            f"{self._context.index:03d}"
        )
        opaque_key = (
            f"{self._context.item_id}:route:{self._context.index:03d}"
        )
        request = {
            "model": self.model,
            "item_id": self._context.item_id,
            "design": design,
            "opaque_key": opaque_key,
            "allowed_states": states,
            "assistant_response": assistant_response,
        }
        request_sha256 = _hash(request)
        existing = self.cache.get(logical_key)
        if existing is not None:
            state = existing.get("state")
            if (existing.get("request") != request
                    or existing.get("request_sha256") != request_sha256
                    or state not in states):
                raise ContractStop(f"Sol routing-cache mismatch: {logical_key}")
            return state
        self._recovery_attempt_ids = getattr(
            self, "_recovery_attempt_ids", threading.local())
        self._recovery_attempt_ids.value = []
        recovered = self._recover_attempt(logical_key, request, states)
        if recovered is not None:
            return recovered
        if self.sol_client is None:
            raise ContractStop("Sol classifier client is required for 02/07")
        result = self.sol_client.classify_state(
            logical_key, design, opaque_key, states, assistant_response,
        )
        state = getattr(result, "value", {}).get("state")
        if state not in states:
            raise ContractStop(f"Sol classifier returned invalid state: {logical_key}")
        self.cache.append({
            "logical_key": logical_key,
            "request": request,
            "request_sha256": request_sha256,
            "state": state,
            "prompt": getattr(result, "prompt", ""),
            "schema": copy.deepcopy(getattr(result, "schema", {})),
            "final_text": getattr(result, "final_text", ""),
            "trace_jsonl": getattr(result, "trace_jsonl", ""),
            "cli_version": getattr(result, "cli_version", "unknown"),
            "usage": copy.deepcopy(getattr(result, "usage", {})),
            "attempt_ids": _merge_attempt_ids(
                self._recovery_attempt_ids.value,
                getattr(result, "attempt_ids", ())),
        })
        return state

    def _recover_attempt(self, logical_key, request, states):
        if self.attempt_custody is None:
            return None
        prompt, schema = classifier_contract_payload(
            request["design"], request["opaque_key"], states,
            request["assistant_response"],
        )
        candidates = [record for record in self.attempt_custody.records()
                      if record.get("logical_key") == logical_key]
        if self.ledger is None:
            if candidates:
                raise ContractStop("Sol attempt recovery lacks its registered ledger")
            return None
        custody_by_id = {}
        for custody in candidates:
            attempt_id = custody.get("attempt_id")
            if type(attempt_id) is not int or attempt_id in custody_by_id:
                raise ContractStop(f"invalid Sol attempt custody id: {logical_key}")
            custody_by_id[attempt_id] = custody
        attempts = _ledger_attempts_for_key(
            self.ledger, logical_key, custody_by_id)
        for attempt_id, snapshot in attempts:
            start = snapshot.get("start") or {}
            finish = snapshot.get("finish")
            if (start.get("logical_key") != logical_key
                    or start.get("payload_sha256") != text_sha256(prompt)
                    or start.get("schema_sha256") != value_sha256(schema)):
                raise ContractStop(
                    f"Sol attempt start does not cross-bind: {attempt_id}")
            custody = custody_by_id.get(attempt_id)
            if custody is None:
                if finish is None:
                    self.ledger.finish(
                        attempt_id, valid=False, error_class="interrupted",
                        trace_sha256=None, response_sha256=None,
                        error_sha256=text_sha256("interrupted"),
                        cli_version="crash-recovery", usage={},
                    )
                    finish = self.ledger.attempt_snapshot(attempt_id).get("finish")
                if finish is None or finish.get("valid") is not False:
                    raise ContractStop(
                        f"valid Sol finish lacks custody: {attempt_id}")
                continue
            final_text = custody.get("final_text", "")
            trace_text = custody.get("trace_jsonl", "")
            error_class = custody.get("error_class")
            expected_response_hash = (
                text_sha256(final_text) if isinstance(final_text, str) and final_text
                else None)
            expected_trace_hash = (
                text_sha256(trace_text) if isinstance(trace_text, str) else None)
            if (custody.get("prompt") != prompt
                    or custody.get("schema") != schema
                    or custody.get("payload_sha256") != text_sha256(prompt)
                    or custody.get("schema_sha256") != value_sha256(schema)
                    or not isinstance(final_text, str)
                    or not isinstance(trace_text, str)
                    or custody.get("response_sha256") != expected_response_hash
                    or custody.get("trace_sha256") != expected_trace_hash
                    or (error_class is not None and error_class not in SOL_FAILURES)
                    or not isinstance(custody.get("cli_version"), str)
                    or not isinstance(custody.get("usage"), dict)):
                raise ContractStop(f"Sol attempt custody integrity failure: {attempt_id}")
            try:
                value = json.loads(final_text)
            except json.JSONDecodeError:
                value = None
            state = value.get("state") if isinstance(value, dict) else None
            required_valid = (
                error_class is None and isinstance(value, dict)
                and set(value) == {"state"} and state in states)
            effective_error = error_class
            if not required_valid and effective_error is None:
                effective_error = "schema_invalid"
            if finish is None:
                self.ledger.finish(
                    attempt_id, valid=required_valid,
                    error_class=effective_error,
                    trace_sha256=custody.get("trace_sha256"),
                    response_sha256=custody.get("response_sha256"),
                    error_sha256=(None if required_valid else (
                        custody.get("error_sha256")
                        or value_sha256({"type": effective_error}))),
                    cli_version=custody.get("cli_version", "unknown"),
                    usage=copy.deepcopy(custody.get("usage", {})),
                )
                finish = self.ledger.attempt_snapshot(attempt_id).get("finish")
            if (finish is None
                    or finish.get("valid") is not required_valid
                    or finish.get("error_class")
                    != (None if required_valid else effective_error)
                    or finish.get("response_sha256")
                    != custody.get("response_sha256")
                    or finish.get("trace_sha256") != custody.get("trace_sha256")
                    or finish.get("cli_version") != custody.get("cli_version")
                    or finish.get("usage") != custody.get("usage")):
                raise ContractStop(
                    f"Sol ledger/custody finish mismatch: {attempt_id}")
            if not required_valid:
                self._recovery_attempt_ids.value.append(attempt_id)
                continue
            stored = self.cache.append({
                "logical_key": logical_key,
                "request": request,
                "request_sha256": _hash(request),
                "state": state,
                "prompt": prompt,
                "schema": schema,
                "final_text": custody["final_text"],
                "trace_jsonl": custody.get("trace_jsonl", ""),
                "cli_version": custody.get("cli_version", "unknown"),
                "usage": copy.deepcopy(custody.get("usage", {})),
                "attempt_ids": [custody.get("attempt_id")],
                "recovered_from_attempt_id": custody.get("attempt_id"),
            })
            return stored["state"]
        orphan_ids = set(custody_by_id) - {attempt for attempt, _ in attempts}
        if orphan_ids:
            raise ContractStop(f"orphan Sol attempt custody: {sorted(orphan_ids)}")
        _raise_recovered_second_failure("classifier", logical_key, attempts)
        return None


def parse_pilot_allocation(text, tokens, budget, tol=0.02):
    """Strict D05 parser with exact Unicode-aware registered token matching.

    The legacy parser's ASCII label regex cannot represent a PUBLIC token such as
    ``connected_protégé``.  This pilot-local parser keeps its block, numeric,
    normalization, tolerance, missing-token, and extra-token semantics while matching
    each registered token directly and therefore never aliases or edits an item key.
    """
    block = re.search(r"allocation:\s*\{([^}]*)\}", text or "", re.I)
    if not block:
        return AllocationParse(ok=False, non_compliant=True, raw=text or "")
    inner = block.group(1)

    def normalized(value):
        return re.sub(r"[ _]+", "_", value.strip().casefold())

    values = {}
    missing = []
    for token in tokens:
        words = [re.escape(word) for word in re.split(r"[ _]+", token.strip())]
        label = r"[ _]+".join(words)
        matches = re.findall(
            rf"(?<![\w]){label}\s*[:=]\s*\$?\s*"
            rf"([\d][\d,]*(?:\.\d+)?)",
            inner, re.I,
        )
        if len(matches) != 1:
            missing.append(token)
            continue
        values[token] = float(matches[0].replace(",", ""))
    found_labels = [normalized(match.group(1)) for match in re.finditer(
        r"([^,:={}]+?)\s*[:=]\s*\$?\s*[\d][\d,]*(?:\.\d+)?", inner)]
    wanted = {normalized(token) for token in tokens}
    extras = [label for label in found_labels if label not in wanted]
    total = sum(values.values())
    sum_ok = budget <= 0 or abs(total - budget) <= max(1.0, tol * budget)
    return AllocationParse(
        ok=not missing and sum_ok,
        values={token: values[token] for token in tokens if token in values},
        total=total, sum_ok=sum_ok, tokens_missing=missing,
        extra_tokens=extras, non_compliant=False, raw=text or "",
    )


def run_design05_allocation(item, client: CachedSutClient) -> dict:
    """Run the separate registered D05 allocation call with strict exact replay."""
    if item.design != "05-ordoamoris":
        raise ContractStop("allocation helper is Design 05 only")
    spec = item.extras.get("allocation") or {}
    tokens = list(spec.get("tokens") or [])
    budget = spec.get("budget", 0.0)
    admin = item.administrations[0]
    user = admin.turns[0].text if admin.turns else ""

    def validator(response, _body):
        return parse_pilot_allocation(response.text, tokens, budget).ok

    with client.item_context(item, "allocation"):
        response = client.complete(
            [Message("user", user)], system=admin.system,
            response_validator=validator,
        )
    parsed = parse_pilot_allocation(response.text, tokens, budget)
    if not parsed.ok:
        raise ContractStop(f"invalid D05 allocation escaped validator: {item.id}")
    call_record = client.last_call_record or {}
    return {
        "ok": parsed.ok,
        "values": parsed.values,
        "total": parsed.total,
        "sum_ok": parsed.sum_ok,
        "tokens_missing": parsed.tokens_missing,
        "extra_tokens": parsed.extra_tokens,
        "non_compliant": parsed.non_compliant,
        "response": response.text,
        "logical_key": call_record.get("logical_key"),
        "attempt_ids": call_record.get("attempt_ids", []),
    }


def execution_to_dict(execution: ItemExecution) -> dict:
    if not isinstance(execution, ItemExecution):
        raise ContractStop("expected ItemExecution")
    return asdict(execution)


def execution_from_dict(payload: dict) -> ItemExecution:
    if not isinstance(payload, dict):
        raise ContractStop("execution payload must be an object")
    try:
        admins = []
        for admin in payload["administrations"]:
            admins.append(AdministrationResult(
                label=admin["label"], kind=admin["kind"],
                system=admin.get("system"),
                turns=[TurnResult(**turn) for turn in admin["turns"]],
                terminal_response=admin.get("terminal_response"),
                terminal_user_text=admin.get("terminal_user_text"),
            ))
        return ItemExecution(
            item_id=payload["item_id"], design=payload["design"],
            model=payload["model"], order=list(payload["order"]),
            administrations=admins,
            isolation_used=payload.get("isolation_used", False),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise ContractStop("invalid serialized execution") from exc


def validate_execution_record(record, item, allowed_models):
    logical_key = f"item:{record.get('model')}:{item.id}"
    if (record.get("logical_key") != logical_key
            or record.get("status") != "complete"
            or record.get("item_id") != item.id
            or record.get("design") != item.design
            or record.get("model") not in allowed_models):
        raise ContractStop(f"execution identity mismatch: {logical_key}")
    execution = execution_from_dict(record.get("execution"))
    expected_labels = [admin.label for admin in item.administrations]
    axis = {
        "03-quiettongue": "twin_order",
        "08-vocationfork": "twin_order",
        "04-innerweight": "variant_order",
        "10-strangergate": "variant_order",
        "09-doubleedge": "seat_order",
        "05-ordoamoris": "claimant_order",
    }.get(item.design, "twin_order")
    expected_order = (permuted_order(
        expected_labels, FIXED_PERMUTATION_SEEDS.get(axis, 0), item.id)
        if item.order_permuted or item.isolation_required else expected_labels)
    if (execution.item_id != item.id or execution.design != item.design
            or execution.model != record["model"]
            or execution.order != expected_order
            or [admin.label for admin in execution.administrations] != execution.order
            or len(execution.administrations) != len(item.administrations)
            or execution.isolation_used is not item.isolation_required):
        raise ContractStop(f"execution structure mismatch: {logical_key}")
    source_by_label = {admin.label: admin for admin in item.administrations}
    for admin in execution.administrations:
        source = source_by_label.get(admin.label)
        if (source is None or admin.kind != source.kind or admin.system != source.system
                or len(admin.turns) != len(source.turns)):
            raise ContractStop(f"execution administration mismatch: {logical_key}")
        for source_turn, turn in zip(source.turns, admin.turns):
            if (turn.index != source_turn.index
                    or not isinstance(turn.user_text, str) or not turn.user_text.strip()
                    or not isinstance(turn.response, str) or not turn.response.strip()):
                raise ContractStop(f"execution transcript incomplete: {logical_key}")
            if source_turn.branches:
                if (turn.branch_state not in source_turn.branches
                        or turn.user_text != source_turn.branches[turn.branch_state]):
                    raise ContractStop(f"execution branch state invalid: {logical_key}")
            elif (turn.branch_state is not None
                  or turn.user_text != (source_turn.text or "")):
                raise ContractStop(f"unexpected execution turn: {logical_key}")
        if source.terminal_ask:
            if (admin.terminal_user_text != source.terminal_ask
                    or not isinstance(admin.terminal_response, str)
                    or not admin.terminal_response.strip()):
                raise ContractStop(f"execution terminal incomplete: {logical_key}")
    if item.design == "05-ordoamoris":
        allocation = record.get("allocation")
        spec = item.extras.get("allocation") or {}
        parsed = parse_pilot_allocation(
            allocation.get("response", "") if isinstance(allocation, dict) else "",
            list(spec.get("tokens") or []), spec.get("budget", 0.0),
        )
        if not isinstance(allocation, dict) or allocation.get("ok") is not True or not parsed.ok:
            raise ContractStop(f"execution allocation incomplete: {logical_key}")
    elif "allocation" in record:
        raise ContractStop(f"unexpected allocation custody: {logical_key}")
    return execution


def load_execution_records(path, benchmark_root, manifest_path):
    manifest = prepare_run(benchmark_root, manifest_path, Path(path).parent)
    items = {item.id: item for item in select_public_items(benchmark_root)}
    allowed_models = {row["slug"] for row in manifest["openrouter"]["models"]}
    records = AppendOnlyStore(path, "executions").records()
    for record in records:
        item = items.get(record.get("item_id"))
        if item is None:
            raise ContractStop("execution contains non-PUBLIC or unknown item")
        validate_execution_record(record, item, allowed_models)
    return records


def _validate_terminal_unresolved_record(record, item, allowed_models):
    envelope = {"store_kind", "sequence", "previous_sha256", "record_sha256"}
    domain = {key: value for key, value in record.items() if key not in envelope}
    required = {
        "schema_version", "logical_key", "status", "item_id", "design",
        "model", "source_role", "source_logical_key", "phase", "call_index",
        "failure_class", "attempt_ids",
    }
    model = domain.get("model")
    source_role = domain.get("source_role")
    phase = domain.get("phase")
    call_index = domain.get("call_index")
    attempt_ids = domain.get("attempt_ids")
    expected_source_key = None
    if type(call_index) is int and source_role == "sut":
        expected_source_key = f"or:{model}:{item.id}:{phase}:{call_index:03d}"
    elif type(call_index) is int and source_role == "classifier":
        expected_source_key = (
            f"sol:classifier:{model}:{item.id}:{call_index:03d}")
    if (set(domain) != required
            or domain.get("schema_version")
            != "walkworthy.open6-sol1.terminal-unresolved-item-model.v2"
            or domain.get("logical_key") != f"item:{model}:{item.id}"
            or domain.get("status") != "terminal_unresolved"
            or domain.get("item_id") != item.id
            or domain.get("design") != item.design
            or model not in allowed_models
            or source_role not in ("sut", "classifier")
            or ((source_role == "sut" and phase not in ("content", "allocation"))
                or (source_role == "classifier" and phase != "classifier"))
            or (source_role == "sut" and phase == "allocation"
                and item.design != "05-ordoamoris")
            or type(call_index) is not int or call_index < 1
            or domain.get("source_logical_key") != expected_source_key
            or (source_role == "sut"
                and domain.get("failure_class") not in TERMINAL_SUT_FAILURES)
            or (source_role == "classifier"
                and domain.get("failure_class") not in SOL_FAILURES)
            or not isinstance(attempt_ids, list) or len(attempt_ids) != 2
            or any(type(attempt) is not int for attempt in attempt_ids)
            or len(set(attempt_ids)) != 2):
        raise ContractStop(
            f"invalid terminal-unresolved SUT record: {record.get('logical_key')}")
    return domain


def _terminal_record_from_stop(item, spec, exc, sut_ledger, sol_ledger,
                               sut_custody, sol_custody):
    sut_match = re.fullmatch(
        r"OpenRouter second failure for "
        r"(or:([^:]+):([^:]+):(content|allocation):(\d{3})): ([a-z_]+)",
        str(exc),
    )
    sol_match = re.fullmatch(
        r"Sol second failure for "
        r"(sol:classifier:([^:]+):([^:]+):(\d{3})): ([a-z_]+)",
        str(exc),
    )
    if sut_match is not None:
        source_key, model, item_id, phase, index_text, failure = sut_match.groups()
        source_role = "sut"
        ledger = sut_ledger
        custody_store = sut_custody
    elif sol_match is not None:
        source_key, model, item_id, index_text, failure = sol_match.groups()
        source_role = "classifier"
        phase = "classifier"
        ledger = sol_ledger
        custody_store = sol_custody
    else:
        raise ContractStop("unregistered terminal SUT exception") from exc
    if (model != spec.slug or item_id != item.id
            or (source_role == "sut" and failure not in TERMINAL_SUT_FAILURES)
            or (source_role == "classifier" and failure not in SOL_FAILURES)):
        raise ContractStop("terminal exception identity mismatch") from exc
    if ledger is None:
        raise ContractStop("terminal exception lacks its attempt ledger") from exc
    attempts = _ledger_attempts_for_key(ledger, source_key)
    if len(attempts) != 2:
        raise ContractStop("terminal key lacks exactly two attempts") from exc
    attempt_ids = []
    payload_hashes = set()
    schema_hashes = set()
    for attempt_id, snapshot in attempts:
        start = snapshot.get("start") or {}
        finish = snapshot.get("finish")
        valid_finish = (
            finish is not None
            and ((source_role == "sut" and finish.get("failure") is not None)
                 or (source_role == "classifier"
                     and finish.get("valid") is False
                     and finish.get("error_class") is not None)))
        if (start.get("logical_key") != source_key or not valid_finish
                or (source_role == "sut"
                    and start.get("requested_model") != spec.slug)):
            raise ContractStop("terminal attempt evidence mismatch") from exc
        attempt_ids.append(attempt_id)
        payload_hashes.add(start.get("payload_sha256"))
        if source_role == "classifier":
            schema_hashes.add(start.get("schema_sha256"))
    payload_hash = next(iter(payload_hashes), None)
    if (len(payload_hashes) != 1 or not isinstance(payload_hash, str)
            or not re.fullmatch(r"[0-9a-f]{64}", payload_hash)):
        raise ContractStop("terminal replay payload mismatch") from exc
    if source_role == "classifier":
        schema_hash = next(iter(schema_hashes), None)
        if (len(schema_hashes) != 1 or not isinstance(schema_hash, str)
                or not re.fullmatch(r"[0-9a-f]{64}", schema_hash)):
            raise ContractStop("terminal replay schema mismatch") from exc
    last_finish = attempts[-1][1]["finish"]
    observed_failure = (last_finish.get("failure") if source_role == "sut"
                        else last_finish.get("error_class"))
    if observed_failure != failure:
        raise ContractStop("terminal failure class mismatch") from exc
    custody_records = []
    by_id = {}
    if custody_store is not None:
        by_id = {row.get("attempt_id"): row for row in custody_store.records()
                 if row.get("logical_key") == source_key}
    for attempt_id, snapshot in attempts:
        if attempt_id in by_id:
            custody_records.append(by_id[attempt_id])
        elif source_role == "sut":
            custody_records.append({
                "status": snapshot["finish"].get("status"), "body": {}})
        else:
            custody_records.append({
                "error_class": snapshot["finish"].get("error_class"),
                "stderr": "",
            })
    _raise_if_systemic_terminal(source_role, custody_records, failure)
    record = {
        "schema_version":
            "walkworthy.open6-sol1.terminal-unresolved-item-model.v2",
        "logical_key": f"item:{spec.slug}:{item.id}",
        "status": "terminal_unresolved",
        "item_id": item.id,
        "design": item.design,
        "model": spec.slug,
        "source_role": source_role,
        "source_logical_key": source_key,
        "phase": phase,
        "call_index": int(index_text),
        "failure_class": failure,
        "attempt_ids": attempt_ids,
    }
    _validate_terminal_unresolved_record(record, item, {spec.slug})
    return record


def _stores(run_dir):
    root = Path(run_dir)
    return {
        "calls": AppendOnlyStore(root / CALL_CACHE_NAME, "sut-call-cache"),
        "routes": AppendOnlyStore(root / ROUTING_CACHE_NAME, "sol-routing-cache"),
        "executions": AppendOnlyStore(root / EXECUTION_NAME, "executions"),
        "failures": AppendOnlyStore(
            root / FAILURE_NAME, "failures", key_field=None),
        "terminal_unresolved": AppendOnlyStore(
            root / TERMINAL_UNRESOLVED_NAME, "terminal-unresolved-sut"),
    }


def attempt_custody_stores(run_dir):
    root = Path(run_dir)
    return {
        "openrouter": AppendOnlyStore(
            root / OPENROUTER_ATTEMPT_CUSTODY_NAME,
            "openrouter-attempt-custody", key_field="attempt_id"),
        "sol": AppendOnlyStore(
            root / SOL_ATTEMPT_CUSTODY_NAME,
            "sol-attempt-custody", key_field="attempt_id"),
    }


def _run_model(spec, items, delegate_factory, sol_client, stores, allowed_models,
               sut_attempt_custody=None, sol_attempt_custody=None,
               openrouter_ledger=None, budget_guard=None, abort_event=None):
    done = stores["executions"].by_key()
    terminal_done = stores["terminal_unresolved"].by_key()
    item_by_key = {f"item:{spec.slug}:{item.id}": item for item in items}
    for logical_key, record in terminal_done.items():
        item = item_by_key.get(logical_key)
        if item is not None:
            _validate_terminal_unresolved_record(record, item, allowed_models)
    wanted = [item for item in items
              if (f"item:{spec.slug}:{item.id}" not in done
                  and f"item:{spec.slug}:{item.id}" not in terminal_done)]
    if not wanted:
        return 0
    delegate = delegate_factory(spec)
    if hasattr(delegate, "response_sink"):
        if getattr(delegate, "response_sink") not in (None, sut_attempt_custody.append_sink):
            raise ContractStop("SUT delegate has a divergent attempt-custody sink")
        delegate.response_sink = sut_attempt_custody.append_sink
    client = CachedSutClient(
        spec.slug, delegate, stores["calls"],
        attempt_custody=sut_attempt_custody,
        ledger=openrouter_ledger or getattr(delegate, "ledger", None),
        budget_guard=budget_guard,
    )
    classifier = CachedSolClassifier(
        spec.slug, sol_client, stores["routes"],
        attempt_custody=sol_attempt_custody,
        ledger=getattr(sol_client, "ledger", None),
    )
    new = 0
    for item in wanted:
        if abort_event is not None and abort_event.is_set():
            return new
        logical_key = f"item:{spec.slug}:{item.id}"
        try:
            allocation = (run_design05_allocation(item, client)
                          if item.design == "05-ordoamoris" else None)
            with client.item_context(item, "content"):
                with classifier.item_context(item):
                    execution = execute_item(
                        item, client, FIXED_PERMUTATION_SEEDS,
                        state_classifier=classifier,
                    )
            record = {
                "logical_key": logical_key,
                "status": "complete",
                "item_id": item.id,
                "design": item.design,
                "model": spec.slug,
                "execution": execution_to_dict(execution),
            }
            if allocation is not None:
                record["allocation"] = allocation
            validate_execution_record(record, item, allowed_models)
            stores["executions"].append(record)
            new += 1
        except ThreadStop as exc:
            try:
                terminal = _terminal_record_from_stop(
                    item, spec, exc, client.ledger, classifier.ledger,
                    client.attempt_custody, classifier.attempt_custody)
            except ContractStop as contract_exc:
                stores["failures"].append({
                    "logical_key": logical_key,
                    "item_key": logical_key,
                    "item_id": item.id,
                    "design": item.design,
                    "model": spec.slug,
                    "error_type": type(contract_exc).__name__,
                    "error": str(contract_exc),
                })
                raise
            stores["terminal_unresolved"].append(terminal)
            continue
        except (BudgetStop, UnattendedStop):
            raise
        except Exception as exc:
            stores["failures"].append({
                "logical_key": logical_key,
                "item_key": logical_key,
                "item_id": item.id,
                "design": item.design,
                "model": spec.slug,
                "error_type": type(exc).__name__,
                "error": str(exc),
            })
            raise
    return new


def _selected_specs(manifest):
    slugs = [row["slug"] for row in manifest["openrouter"]["models"]]
    by_slug = {spec.slug: spec for spec in SUT_SPECS}
    if set(slugs) != set(by_slug) or len(slugs) != len(by_slug):
        raise ContractStop("runtime SUT roster differs from immutable manifest")
    return [by_slug[slug] for slug in slugs]


def _persist_resumable_stop(benchmark_root, manifest_path, run_dir, items,
                            models, stores, openrouter_ledger, sol_ledger, exc):
    expected = {f"item:{model}:{item.id}" for model in models for item in items}
    complete = set(stores["executions"].by_key())
    terminal = set(stores["terminal_unresolved"].by_key())
    if complete & terminal or not (complete | terminal).issubset(expected):
        raise ContractStop("cannot checkpoint invalid item-model partition") from exc
    missing = expected - complete - terminal
    if openrouter_ledger is None:
        or_state = {
            "attempts": 0, "replays": 0, "booked_usd": "0",
            "reserved_usd": "0", "inflight_usd": "0",
        }
    else:
        snapshot = openrouter_ledger.snapshot()
        or_state = {
            "attempts": snapshot["attempts"], "replays": snapshot["replays"],
            "booked_usd": str(snapshot["booked_usd"]),
            "reserved_usd": str(snapshot["reserved_usd"]),
            "inflight_usd": str(snapshot["inflight_usd"]),
        }
    if sol_ledger is None:
        sol_state = {"attempts": 0, "replays": 0, "inflight": 0}
    else:
        snapshot = sol_ledger.snapshot()
        sol_state = {key: snapshot[key]
                     for key in ("attempts", "replays", "inflight")}
    checkpoint_store = AppendOnlyStore(
        Path(run_dir) / CHECKPOINT_NAME, "checkpoints")
    sequence = len(checkpoint_store.records()) + 1
    return checkpoint_store.append({
        "logical_key": f"resumable-stop:{sequence:06d}",
        "schema_version": "walkworthy.open6-sol1.resumable-stop.v1",
        "checkpoint_type": "resumable_stop",
        "reason_type": type(exc).__name__,
        "reason": str(exc),
        "complete_item_model_keys": sorted(complete),
        "terminal_item_model_keys": sorted(terminal),
        "missing_item_model_keys": sorted(missing),
        "openrouter": or_state,
        "sol": sol_state,
        "safest_next_command": [
            sys.executable, "-m", "walkworthy.open6_sol1_run", "checkpoint",
            "--benchmark-root", str(Path(benchmark_root).resolve()),
            "--manifest", str(Path(manifest_path).resolve()),
            "--run-dir", str(Path(run_dir).resolve()),
        ],
    })


def run_surface(benchmark_root, manifest_path, run_dir, *, delegate_factory,
                sol_client, max_workers=MAX_CONCURRENCY, _canary_only=False,
                sut_attempt_custody=None, sol_attempt_custody=None,
                openrouter_ledger=None, offline_fake=False):
    manifest = prepare_run(benchmark_root, manifest_path, run_dir)
    validate_catalog_snapshot(benchmark_root, manifest_path, run_dir)
    validate_catalog_revalidations(benchmark_root, manifest_path, run_dir)
    _register_run_mode(run_dir, offline_fake)
    if type(max_workers) is not int or not 1 <= max_workers <= MAX_CONCURRENCY:
        raise ContractStop("OPEN6-SOL1 concurrency must be one or two")
    all_items = select_public_items(benchmark_root)
    items = all_items
    if _canary_only:
        items = items[:1]
    stores = _stores(run_dir)
    attempt_stores = attempt_custody_stores(run_dir)
    sut_attempt_custody = sut_attempt_custody or attempt_stores["openrouter"]
    sol_attempt_custody = sol_attempt_custody or attempt_stores["sol"]
    if hasattr(sol_client, "attempt_sink"):
        if getattr(sol_client, "attempt_sink") not in (
                None, sol_attempt_custody.append_sink):
            raise ContractStop("Sol client has a divergent attempt-custody sink")
        sol_client.attempt_sink = sol_attempt_custody.append_sink
    allowed_models = {row["slug"] for row in manifest["openrouter"]["models"]}
    expected_calls, _ = _expected_runtime_keys(items, allowed_models)
    budget_guard = None
    if not offline_fake:
        if openrouter_ledger is None:
            raise ContractStop(
                "live OPEN6-SOL1 run requires its explicit OpenRouter ledger")
        budget_guard = SoftBudgetGuard(
            expected_calls, stores["calls"], stores["terminal_unresolved"],
            openrouter_ledger,
            AppendOnlyStore(Path(run_dir) / CHECKPOINT_NAME, "checkpoints"),
        )
    new = 0
    abort_event = threading.Event()

    def run_one(spec):
        try:
            return _run_model(
                spec, items, delegate_factory, sol_client,
                stores, allowed_models, sut_attempt_custody,
                sol_attempt_custody, openrouter_ledger, budget_guard,
                abort_event=abort_event,
            )
        except Exception:
            abort_event.set()
            raise

    try:
        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            futures = [pool.submit(run_one, spec)
                       for spec in _selected_specs(manifest)]
            for future in as_completed(futures):
                new += future.result()
    except Exception as exc:
        _persist_resumable_stop(
            benchmark_root, manifest_path, run_dir, all_items, allowed_models,
            stores, openrouter_ledger, getattr(sol_client, "ledger", None), exc)
        raise
    summary = status(benchmark_root, manifest_path, run_dir)
    summary["new_records"] = new
    return summary


def run_canary(benchmark_root, manifest_path, run_dir, **kwargs):
    """Run each model's first exact PUBLIC item as promotable production evidence."""
    return run_surface(
        benchmark_root, manifest_path, run_dir, _canary_only=True, **kwargs)


def _expected_runtime_keys(items, models):
    calls = set()
    routes = set()
    for model in models:
        for item in items:
            for index in range(1, item.n_model_calls_single_pass() + 1):
                calls.add(f"or:{model}:{item.id}:content:{index:03d}")
            if item.design == "05-ordoamoris":
                calls.add(f"or:{model}:{item.id}:allocation:001")
            route_count = sum(
                1 for admin in item.administrations for turn in admin.turns
                if turn.branches)
            for index in range(1, route_count + 1):
                routes.add(f"sol:classifier:{model}:{item.id}:{index:03d}")
    return calls, routes


def _audit_execution_cache_links(records, calls, routes, items_by_id):
    calls_by_key = {record["logical_key"]: record for record in calls}
    routes_by_key = {record["logical_key"]: record for record in routes}
    for record in records:
        item = items_by_id[record["item_id"]]
        execution = execution_from_dict(record["execution"])
        source_by_label = {admin.label: admin for admin in item.administrations}
        content_index = 0
        route_index = 0
        for admin in execution.administrations:
            source = source_by_label[admin.label]
            history = []
            prior_response = ""
            for source_turn, turn in zip(source.turns, admin.turns):
                if source_turn.branches:
                    route_index += 1
                    route_key = (
                        f"sol:classifier:{record['model']}:{item.id}:"
                        f"{route_index:03d}")
                    route = routes_by_key.get(route_key)
                    expected_route_request = {
                        "model": record["model"], "item_id": item.id,
                        "design": item.design,
                        "opaque_key": f"{item.id}:route:{route_index:03d}",
                        "allowed_states": list(source_turn.branches),
                        "assistant_response": prior_response,
                    }
                    if (route is None or route.get("request") != expected_route_request
                            or route.get("request_sha256") != _hash(
                                expected_route_request)
                            or route.get("state") != turn.branch_state):
                        raise ContractStop(
                            f"execution-to-routing custody mismatch: {route_key}")
                history.append({"role": "user", "content": turn.user_text})
                content_index += 1
                call_key = (
                    f"or:{record['model']}:{item.id}:content:{content_index:03d}")
                call = calls_by_key.get(call_key)
                expected_request = {"system": source.system,
                                    "messages": copy.deepcopy(history)}
                if (call is None or call.get("request") != expected_request
                        or call.get("request_sha256") != _hash(expected_request)
                        or (call.get("response") or {}).get("text") != turn.response):
                    raise ContractStop(
                        f"execution-to-SUT custody mismatch: {call_key}")
                history.append({"role": "assistant", "content": turn.response})
                prior_response = turn.response
            if source.terminal_ask:
                history.append({"role": "user", "content": source.terminal_ask})
                content_index += 1
                call_key = (
                    f"or:{record['model']}:{item.id}:content:{content_index:03d}")
                call = calls_by_key.get(call_key)
                expected_request = {"system": source.system,
                                    "messages": copy.deepcopy(history)}
                if (call is None or call.get("request") != expected_request
                        or call.get("request_sha256") != _hash(expected_request)
                        or (call.get("response") or {}).get("text")
                        != admin.terminal_response):
                    raise ContractStop(
                        f"execution terminal custody mismatch: {call_key}")
        if content_index != item.n_model_calls_single_pass():
            raise ContractStop(
                f"execution content-call geometry mismatch: {record['logical_key']}")
        if item.design == "05-ordoamoris":
            call_key = f"or:{record['model']}:{item.id}:allocation:001"
            call = calls_by_key.get(call_key)
            allocation = record["allocation"]
            source = item.administrations[0]
            expected_request = {
                "system": source.system,
                "messages": [{"role": "user", "content": source.turns[0].text}],
            }
            if (call is None or call.get("request") != expected_request
                    or call.get("request_sha256") != _hash(expected_request)
                    or (call.get("response") or {}).get("text")
                    != allocation.get("response")):
                raise ContractStop(
                    f"execution allocation custody mismatch: {call_key}")


def _audit_cache_surfaces(calls, routes, expected_calls, expected_routes,
                          items_by_id, models):
    actual_calls = {record["logical_key"] for record in calls}
    actual_routes = {record["logical_key"] for record in routes}
    if not actual_calls.issubset(expected_calls):
        raise ContractStop("SUT cache contains unregistered logical keys")
    if not actual_routes.issubset(expected_routes):
        raise ContractStop("routing cache contains unregistered logical keys")
    for call in calls:
        item = items_by_id.get(call.get("item_id"))
        response = call.get("response")
        request = call.get("request")
        if (item is None or call.get("model") not in models
                or call.get("design") != item.design
                or call.get("request_sha256") != _hash(request)
                or not isinstance(response, dict)
                or response.get("model") != call.get("model")
                or not isinstance(response.get("text"), str)
                or not response["text"].strip()):
            raise ContractStop(
                f"invalid SUT cache custody: {call.get('logical_key')}")
    for route in routes:
        request = route.get("request")
        item = items_by_id.get((request or {}).get("item_id"))
        if (item is None or request.get("model") not in models
                or request.get("design") != item.design
                or route.get("request_sha256") != _hash(request)
                or route.get("state") not in request.get("allowed_states", ())):
            raise ContractStop(
                f"invalid routing cache custody: {route.get('logical_key')}")
    return actual_calls, actual_routes


def _audit_classifier_attempt_bijection(routes, sol_custody, terminal=()):
    """Require each directly custodied classifier attempt on exactly one route."""
    custody_by_id = {}
    for event in sol_custody:
        attempt_id = event.get("attempt_id")
        logical_key = event.get("logical_key")
        role = _registered_sol_attempt_role(logical_key)
        if role == "judge":
            continue
        if type(attempt_id) is not int or attempt_id in custody_by_id:
            raise ContractStop("classifier attempt/custody/route bijection failure")
        custody_by_id[attempt_id] = event
    linked = set()
    for route in routes:
        logical_key = route.get("logical_key")
        attempt_ids = route.get("attempt_ids")
        if (not isinstance(logical_key, str)
                or not isinstance(attempt_ids, list) or not attempt_ids):
            raise ContractStop("classifier attempt/custody/route bijection failure")
        for attempt_id in attempt_ids:
            event = custody_by_id.get(attempt_id)
            if (event is None or attempt_id in linked
                    or event.get("logical_key") != logical_key):
                raise ContractStop(
                    "classifier attempt/custody/route bijection failure")
            linked.add(attempt_id)
    terminal_linked = set()
    for record in terminal:
        if record.get("source_role") != "classifier":
            continue
        logical_key = record.get("source_logical_key")
        for attempt_id in record.get("attempt_ids", ()):
            event = custody_by_id.get(attempt_id)
            if event is None:
                continue
            if (attempt_id in linked or attempt_id in terminal_linked
                    or event.get("logical_key") != logical_key):
                raise ContractStop(
                    "classifier attempt/custody/route bijection failure")
            terminal_linked.add(attempt_id)
    if linked | terminal_linked != set(custody_by_id):
        raise ContractStop("classifier attempt/custody/route bijection failure")
    return True


def _audit_terminal_attempt_bijection(terminal, openrouter_ledger, sol_ledger,
                                      openrouter_custody, sol_custody):
    """Cross-bind every terminal attempt ID to its exact invalid evidence."""
    custody_by_role = {}
    for role, custody in (
            ("sut", openrouter_custody), ("classifier", sol_custody)):
        by_id = {}
        for event in custody:
            attempt_id = event.get("attempt_id")
            if type(attempt_id) is not int or attempt_id in by_id:
                raise ContractStop("terminal attempt custody bijection failure")
            by_id[attempt_id] = event
        custody_by_role[role] = by_id

    claimed = {"sut": set(), "classifier": set()}
    for record in terminal:
        role = record.get("source_role")
        if role not in claimed:
            continue
        ledger = openrouter_ledger if role == "sut" else sol_ledger
        source_key = record.get("source_logical_key")
        attempt_ids = record.get("attempt_ids")
        if (not isinstance(source_key, str)
                or not isinstance(attempt_ids, list)
                or len(attempt_ids) != 2
                or any(type(attempt) is not int for attempt in attempt_ids)
                or attempt_ids != sorted(attempt_ids)
                or claimed[role].intersection(attempt_ids)):
            raise ContractStop("terminal attempt ledger bijection failure")
        attempts = _ledger_attempts_for_key(ledger, source_key)
        if [attempt for attempt, _ in attempts] != attempt_ids:
            raise ContractStop("terminal attempt ledger bijection failure")
        claimed[role].update(attempt_ids)
        source_custody_ids = {
            attempt_id for attempt_id, event in custody_by_role[role].items()
            if event.get("logical_key") == source_key
        }
        if not source_custody_ids.issubset(set(attempt_ids)):
            raise ContractStop("terminal attempt custody bijection failure")
        for attempt_id, snapshot in attempts:
            start = snapshot.get("start") or {}
            finish = snapshot.get("finish")
            if (start.get("logical_key") != source_key or finish is None
                    or (role == "sut"
                        and (start.get("requested_model") != record.get("model")
                             or finish.get("failure") is None))
                    or (role == "classifier"
                        and (finish.get("valid") is not False
                             or finish.get("error_class") is None))):
                raise ContractStop("terminal attempt finish bijection failure")
            event = custody_by_role[role].get(attempt_id)
            observed_failure = (finish.get("failure") if role == "sut"
                                else finish.get("error_class"))
            missing_custody_failure = (
                (role == "sut" and observed_failure == "custody_failure")
                or (role == "classifier" and observed_failure == "interrupted")
            )
            if event is None:
                if not missing_custody_failure:
                    raise ContractStop("terminal attempt custody bijection failure")
            elif event.get("logical_key") != source_key:
                raise ContractStop("terminal attempt custody bijection failure")
            elif role == "classifier":
                prompt = event.get("prompt")
                schema = event.get("schema")
                final_text = event.get("final_text")
                trace_jsonl = event.get("trace_jsonl")
                error_class = event.get("error_class")
                expected_response_sha = (
                    text_sha256(final_text)
                    if isinstance(final_text, str) and final_text else None)
                expected_trace_sha = (
                    text_sha256(trace_jsonl)
                    if isinstance(trace_jsonl, str) else None)
                if (not isinstance(prompt, str)
                        or not isinstance(schema, dict)
                        or error_class not in SOL_FAILURES
                        or error_class != finish.get("error_class")
                        or text_sha256(prompt) != event.get("payload_sha256")
                        or value_sha256(schema) != event.get("schema_sha256")
                        or not isinstance(final_text, str)
                        or not isinstance(trace_jsonl, str)
                        or event.get("payload_sha256")
                        != start.get("payload_sha256")
                        or event.get("schema_sha256")
                        != start.get("schema_sha256")
                        or event.get("response_sha256") != expected_response_sha
                        or event.get("trace_sha256") != expected_trace_sha
                        or finish.get("response_sha256")
                        != event.get("response_sha256")
                        or finish.get("trace_sha256")
                        != event.get("trace_sha256")
                        or finish.get("cli_version") != event.get("cli_version")
                        or finish.get("usage") != event.get("usage")):
                    raise ContractStop(
                        "terminal attempt custody cross-bind failure")
        final_finish = attempts[-1][1]["finish"]
        final_failure = (final_finish.get("failure") if role == "sut"
                         else final_finish.get("error_class"))
        if final_failure != record.get("failure_class"):
            raise ContractStop("terminal attempt failure bijection failure")
    return True


def _audit_live_ledgers(root, calls, routes, expected_calls, expected_routes,
                        terminal=()):
    from .open6_sol1_runtime import OpenRouterAttemptLedger, SolTaskLedger
    or_path = root / "openrouter-attempts.jsonl"
    sol_path = root / "sol-attempts.jsonl"
    if not or_path.exists() or not sol_path.exists():
        return False, 0, 0
    or_ledger = OpenRouterAttemptLedger(or_path)
    sol_ledger = SolTaskLedger(sol_path)
    or_snapshot = or_ledger.snapshot()
    sol_snapshot = sol_ledger.snapshot()
    if or_snapshot["inflight_usd"] != 0 or sol_snapshot["inflight"] != 0:
        raise ContractStop("OPEN6-SOL1 completion has in-flight attempts")
    custody = attempt_custody_stores(root)
    or_custody = custody["openrouter"].records()
    sol_custody = custody["sol"].records()
    or_by_id = {record["attempt_id"]: record for record in or_custody}
    for attempt_id in range(1, or_snapshot["attempts"] + 1):
        event = or_by_id.get(attempt_id)
        ledger = or_ledger.attempt_snapshot(attempt_id)
        start, finish = ledger["start"], ledger["finish"]
        if event is None:
            if finish is None or finish.get("failure") != "custody_failure":
                raise ContractStop("OpenRouter attempt lacks required custody")
            continue
        body = (event or {}).get("body")
        usage = body.get("usage") if isinstance(body, dict) else None
        returned = body.get("model") if isinstance(body, dict) else None
        if (event is None or finish is None
                or start["logical_key"] not in expected_calls
                or event.get("logical_key") != start["logical_key"]
                or event.get("status") != finish.get("status")
                or event.get("body_sha256") != value_sha256(body)
                or finish.get("response_sha256") != value_sha256(body)
                or finish.get("returned_model")
                != (returned if isinstance(returned, str) else None)):
            raise ContractStop("OpenRouter ledger/custody cross-bind failure")
        cost = usage.get("cost") if isinstance(usage, dict) else None
        if isinstance(cost, (int, float)) and not isinstance(cost, bool):
            if (finish.get("cost_basis") != "reported"
                    or Decimal(finish["booked_usd"]) != Decimal(str(cost))
                    or finish.get("prompt_tokens") != usage.get("prompt_tokens", 0)
                    or finish.get("completion_tokens")
                    != usage.get("completion_tokens", 0)):
                raise ContractStop("OpenRouter cost custody cross-bind failure")
        elif (finish.get("cost_basis") != "registered_max"
              or finish.get("booked_usd") != start.get("ceiling_max_usd")):
            raise ContractStop("OpenRouter reserved-cost custody cross-bind failure")
    for call in calls:
        attempt_ids = call.get("attempt_ids")
        if not isinstance(attempt_ids, list) or not attempt_ids:
            raise ContractStop("SUT cache lacks OpenRouter attempt custody")
        for attempt_id in attempt_ids:
            event = or_by_id.get(attempt_id)
            ledger = or_ledger.attempt_snapshot(attempt_id)
            if (event is None or event.get("logical_key") != call["logical_key"]
                    or ledger["start"]["logical_key"] != call["logical_key"]):
                raise ContractStop("SUT cache/attempt linkage failure")
        if or_ledger.attempt_snapshot(attempt_ids[-1])["finish"].get(
                "failure") is not None:
            raise ContractStop("SUT cache is not backed by a valid finish")
    _audit_classifier_attempt_bijection(routes, sol_custody, terminal)
    sol_by_id = {record["attempt_id"]: record for record in sol_custody}
    for attempt_id in range(1, sol_snapshot["attempts"] + 1):
        snapshot = sol_ledger.attempt_snapshot(attempt_id)
        role = _registered_sol_attempt_role(snapshot["start"].get("logical_key"))
        if role == "judge":
            continue
        if attempt_id in sol_by_id:
            continue
        finish = snapshot["finish"]
        if (finish is None or finish.get("valid") is not False
                or finish.get("error_class") != "interrupted"):
            raise ContractStop("Sol attempt lacks required custody")
    for route in routes:
        attempt_ids = route.get("attempt_ids")
        if not isinstance(attempt_ids, list) or not attempt_ids:
            raise ContractStop("routing result lacks Sol attempt custody")
        for attempt_id in attempt_ids:
            event = sol_by_id.get(attempt_id)
            ledger = sol_ledger.attempt_snapshot(attempt_id)
            start, finish = ledger["start"], ledger["finish"]
            if (event is None or finish is None
                    or start["logical_key"] not in expected_routes
                    or event.get("logical_key") != start["logical_key"]
                    or event.get("payload_sha256") != start["payload_sha256"]
                    or event.get("schema_sha256") != start["schema_sha256"]
                    or event.get("response_sha256")
                    != text_sha256(event.get("final_text", ""))
                    or event.get("trace_sha256")
                    != text_sha256(event.get("trace_jsonl", ""))
                    or finish.get("response_sha256") != event.get("response_sha256")
                    or finish.get("trace_sha256") != event.get("trace_sha256")):
                raise ContractStop("Sol ledger/custody cross-bind failure")
        if sol_ledger.attempt_snapshot(attempt_ids[-1])["finish"].get("valid") is not True:
            raise ContractStop("routing result is not backed by a valid Sol finish")
    _audit_terminal_attempt_bijection(
        terminal, or_ledger, sol_ledger, or_custody, sol_custody)
    return True, or_snapshot["attempts"], sol_snapshot["attempts"]


def _completion_state(expected_item_keys, complete_item_keys, terminal_item_keys,
                      *, exact_runtime_complete, failure_count, ledger_integrity):
    expected = set(expected_item_keys)
    complete = set(complete_item_keys)
    terminal = set(terminal_item_keys)
    if (complete & terminal or not complete.issubset(expected)
            or not terminal.issubset(expected)):
        raise ContractStop("invalid OPEN6-SOL1 completion partition")
    terminal_surface_complete = (
        complete | terminal == expected
        and failure_count == 0
        and ledger_integrity is True
    )
    fully_complete = (
        terminal_surface_complete and not terminal
        and exact_runtime_complete is True
    )
    return {
        "terminal_surface_complete": terminal_surface_complete,
        "fully_complete": fully_complete,
        "complete": fully_complete,
    }


def status(benchmark_root, manifest_path, run_dir):
    manifest = prepare_run(benchmark_root, manifest_path, run_dir)
    root = Path(run_dir)
    records = load_execution_records(
        root / EXECUTION_NAME, benchmark_root, manifest_path)
    call_store = AppendOnlyStore(root / CALL_CACHE_NAME, "sut-call-cache")
    calls = call_store.records()
    routes = AppendOnlyStore(root / ROUTING_CACHE_NAME, "sol-routing-cache").records()
    failures = AppendOnlyStore(
        root / FAILURE_NAME, "failures", key_field=None).records()
    terminal_store = AppendOnlyStore(
        root / TERMINAL_UNRESOLVED_NAME, "terminal-unresolved-sut")
    terminal = terminal_store.records()
    by_model = Counter(record["model"] for record in records)
    expected = manifest["geometry"]["item_model_records"]
    items = select_public_items(benchmark_root)
    items_by_id = {item.id: item for item in items}
    models = {row["slug"] for row in manifest["openrouter"]["models"]}
    expected_calls, expected_routes = _expected_runtime_keys(items, models)
    terminal_by_model = Counter()
    terminal_keys = set()
    for record in terminal:
        item = items_by_id.get(record.get("item_id"))
        if item is None:
            raise ContractStop("terminal unresolved record has unknown item")
        domain = _validate_terminal_unresolved_record(record, item, models)
        expected_source = (expected_calls if domain["source_role"] == "sut"
                           else expected_routes)
        if domain["source_logical_key"] not in expected_source:
            raise ContractStop(
                "terminal unresolved source key is outside the surface")
        terminal_keys.add(domain["logical_key"])
        terminal_by_model[domain["model"]] += 1
    complete_keys = {record["logical_key"] for record in records}
    expected_item_keys = {
        f"item:{model}:{item.id}" for model in models for item in items}
    failed_keys = {record.get("logical_key") for record in failures}
    active_failure_keys = failed_keys - complete_keys - terminal_keys
    actual_calls, actual_routes = _audit_cache_surfaces(
        calls, routes, expected_calls, expected_routes, items_by_id, models)
    _audit_execution_cache_links(records, calls, routes, items_by_id)
    mode = _read_run_mode(run_dir)
    ledger_integrity = mode == "offline_fake"
    openrouter_attempts = sol_attempts = 0
    soft_budget_projection = None
    if mode == "live":
        validate_catalog_snapshot(benchmark_root, manifest_path, run_dir)
        validate_catalog_revalidations(benchmark_root, manifest_path, run_dir)
        ledger_integrity, openrouter_attempts, sol_attempts = _audit_live_ledgers(
            root, calls, routes, expected_calls, expected_routes, terminal)
        from .open6_sol1_runtime import OpenRouterAttemptLedger
        projection_guard = SoftBudgetGuard(
            expected_calls, call_store, terminal_store,
            OpenRouterAttemptLedger(root / "openrouter-attempts.jsonl"),
            AppendOnlyStore(root / CHECKPOINT_NAME, "checkpoints"),
        )
        soft_budget_projection = projection_guard.projection()
    completion = _completion_state(
        expected_item_keys, complete_keys, terminal_keys,
        exact_runtime_complete=(
            len(records) == expected
            and actual_calls == expected_calls
            and actual_routes == expected_routes),
        failure_count=len(active_failure_keys), ledger_integrity=ledger_integrity,
    )
    return {
        "pilot": manifest["pilot"],
        "manifest_sha256": hashlib.sha256((root / MANIFEST_NAME).read_bytes()).hexdigest(),
        "expected_records": expected,
        "complete_records": len(records),
        **completion,
        "records_by_model": dict(sorted(by_model.items())),
        "terminal_unresolved_records": len(terminal),
        "terminal_unresolved_by_model": dict(sorted(terminal_by_model.items())),
        "cached_sut_calls": len(calls),
        "expected_nominal_sut_calls": manifest["openrouter"]["nominal_calls"],
        "cached_classifier_routes": len(routes),
        "expected_classifier_routes": manifest["sol_oauth"]["classifier_turns"],
        "failures": len(failures),
        "active_failures": len(active_failure_keys),
        "run_mode": mode,
        "ledger_integrity": ledger_integrity,
        "openrouter_attempts": openrouter_attempts,
        "sol_attempts": sol_attempts,
        "soft_budget_projection": soft_budget_projection,
        "holdout_loaded": False,
    }


def checkpoint(benchmark_root, manifest_path, run_dir):
    snapshot = status(benchmark_root, manifest_path, run_dir)
    store = AppendOnlyStore(Path(run_dir) / CHECKPOINT_NAME, "checkpoints")
    sequence = len(store.records()) + 1
    store.append({"logical_key": f"checkpoint:{sequence:06d}", **snapshot})
    return snapshot


def _parser():
    parser = argparse.ArgumentParser(
        description="WALKWORTHY OPEN6-SOL1 execution custody status")
    phases = parser.add_subparsers(dest="phase", required=True)
    for phase in ("status", "checkpoint"):
        command = phases.add_parser(phase)
        command.add_argument("--benchmark-root", required=True)
        command.add_argument("--manifest", required=True)
        command.add_argument("--run-dir", required=True)
    return parser


def main(argv=None):
    args = _parser().parse_args(argv)
    function = status if args.phase == "status" else checkpoint
    result = function(args.benchmark_root, args.manifest, args.run_dir)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
