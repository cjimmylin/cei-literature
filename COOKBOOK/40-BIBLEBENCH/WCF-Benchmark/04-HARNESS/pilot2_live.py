#!/usr/bin/env python3
"""Immutable custody and strict-cap primitives for a future authorized Pilot 2 run."""

from __future__ import annotations

import argparse
import copy
import fcntl
import hashlib
import json
import math
import os
import sys
import tempfile
import threading
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
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
STRICT_CAP_USD = 28.13
V3_MANIFEST_SHA256 = "b5227988f67a5eca563e7f76b78e36613e8665d433fda9c37fb1efa048a05870"
OWNER_RECORD_NAME = "20260715ai-jimmy-pilot2-s62-28-13-execution-authorization-record.md"
OWNER_RECORD_SHA256 = "ec49e5cbbf5670c55d78a3d3d9ebf30ded38fb9aa26ff66032ad0793eba60c71"
WCF_ROOT = Path(__file__).resolve().parent.parent
V3_MANIFEST_PATH = (
    WCF_ROOT / "07-PILOTS" / "20260715-pilot2-public-preflight-v3"
    / "pilot2-manifest.json"
)
OWNER_RECORD_PATH = WCF_ROOT / OWNER_RECORD_NAME
PHASE_PROVIDER_CANARIES = "provider-canaries"
PHASE_FIRST_CELLS = "first-cells"
PHASE_REMAINING_RUN = "remaining-run"
PHASES = (PHASE_PROVIDER_CANARIES, PHASE_FIRST_CELLS, PHASE_REMAINING_RUN)


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


def _read_json(path: Path, message: str) -> Dict[str, Any]:
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CustodyStop(message) from exc
    if not isinstance(value, dict):
        raise CustodyStop(message)
    return value


def _run_lease_path(run_dir: Path) -> Path:
    lexical = os.path.abspath(os.fspath(run_dir))
    identity = hashlib.sha256(lexical.encode("utf-8")).hexdigest()[:24]
    return Path(tempfile.gettempdir()).resolve() / (
        f".wcfbench-pilot2-{identity}.lease")


@contextmanager
def exclusive_run_lease(run_dir: Path):
    """Hold the one nonblocking process lease for a Pilot 2 run directory."""
    lease_path = _run_lease_path(run_dir)
    try:
        handle = lease_path.open("a+", encoding="utf-8")
    except OSError as exc:
        raise CustodyStop("Pilot 2 process lease is unavailable") from exc
    try:
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except (BlockingIOError, OSError) as exc:
            raise CustodyStop(
                "another Pilot 2 process holds the run lease") from exc
        try:
            yield
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
    finally:
        handle.close()


def _validate_authority_sources(
    source_manifest: Path, owner_record: Path, cap_usd: float,
) -> Dict[str, Any]:
    source_manifest = Path(source_manifest)
    owner_record = Path(owner_record)
    if cap_usd != STRICT_CAP_USD:
        raise CustodyStop("authorization cap must be exactly 28.13 USD")
    try:
        source_hash = _hash(source_manifest)
        owner_hash = _hash(owner_record)
        owner_text = owner_record.read_text(encoding="utf-8")
    except OSError as exc:
        raise CustodyStop("authorization source record is unreadable") from exc
    if source_hash != V3_MANIFEST_SHA256:
        raise CustodyStop("source manifest is not the exact immutable v3 hash")
    if (owner_record.name != OWNER_RECORD_NAME
            or owner_hash != OWNER_RECORD_SHA256):
        raise CustodyStop("owner authorization record is not the exact dated record")
    if ("Owner ruling:** `PROCEED`" not in owner_text
            or "Strict cumulative OpenRouter NTE: **`$28.13`**" not in owner_text):
        raise CustodyStop("owner authorization record does not grant the exact cap")
    manifest = _load_manifest(source_manifest)
    gate = manifest.get("authorization_gate") or {}
    if any(gate.get(name) is not False for name in (
            "credential_access", "oauth_canary", "paid_inference")):
        raise CustodyStop("v3 authorization gates are not the registered false state")
    try:
        proposed = float(manifest["planning_cost"]["proposed_cap_usd"])
        required = float(manifest["auth_balance"]["required_balance_usd"])
    except (KeyError, TypeError, ValueError) as exc:
        raise CustodyStop("v3 manifest lacks the exact strict cap") from exc
    if proposed != STRICT_CAP_USD or required != STRICT_CAP_USD:
        raise CustodyStop("v3 manifest lacks the exact strict cap")
    return manifest


def bind_authorization(
    source_manifest: Path, owner_record: Path, output_manifest: Path, *,
    cap_usd: float,
) -> Dict[str, Any]:
    """Bind the exact owner authority into a new manifest without editing v3."""
    output_manifest = Path(output_manifest)
    if output_manifest.exists():
        raise CustodyStop("authorized output manifest already exists")
    manifest = _validate_authority_sources(
        source_manifest, owner_record, cap_usd)
    bound = copy.deepcopy(manifest)
    bound["authorization_gate"].update({
        "credential_access": True,
        "oauth_canary": True,
        "paid_inference": True,
    })
    bound["authorization_binding"] = {
        "kind": "wcf_bench_pilot2_amount_specific_authorization",
        "source_manifest_sha256": V3_MANIFEST_SHA256,
        "owner_record": OWNER_RECORD_NAME,
        "owner_record_sha256": OWNER_RECORD_SHA256,
        "strict_cap_usd": STRICT_CAP_USD,
    }
    try:
        _write_new(output_manifest, bound)
    except FileExistsError as exc:
        raise CustodyStop("authorized output manifest already exists") from exc
    if _hash(Path(source_manifest)) != V3_MANIFEST_SHA256:
        raise CustodyStop("immutable v3 manifest changed during authorization binding")
    return bound


def require_bound_authorization(manifest: Mapping[str, Any]) -> None:
    """Fail closed unless a manifest differs from exact v3 only by the binding."""
    source = _validate_authority_sources(
        V3_MANIFEST_PATH, OWNER_RECORD_PATH, STRICT_CAP_USD)
    observed = copy.deepcopy(dict(manifest))
    binding = observed.pop("authorization_binding", None)
    expected_binding = {
        "kind": "wcf_bench_pilot2_amount_specific_authorization",
        "source_manifest_sha256": V3_MANIFEST_SHA256,
        "owner_record": OWNER_RECORD_NAME,
        "owner_record_sha256": OWNER_RECORD_SHA256,
        "strict_cap_usd": STRICT_CAP_USD,
    }
    if binding != expected_binding:
        raise CustodyStop("manifest lacks the exact amount-specific authorization binding")
    gate = observed.get("authorization_gate") or {}
    if any(gate.get(name) is not True for name in (
            "credential_access", "oauth_canary", "paid_inference")):
        raise CustodyStop("manifest lacks all registered authorization transitions")
    gate.update({
        "credential_access": False,
        "oauth_canary": False,
        "paid_inference": False,
    })
    if observed != source:
        raise CustodyStop("authorized manifest changes fields outside the registered binding")


def _append_unlocked(path: Path, value: Mapping[str, Any]) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(value, sort_keys=True, ensure_ascii=False) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def _append(path: Path, value: Mapping[str, Any], lock: threading.Lock) -> None:
    with lock:
        _append_unlocked(path, value)


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
            _append_unlocked(self.run_dir / EVIDENCE_FILE, {
                "kind": "cost_settlement", "request_id": request_id,
                "response_attributed_cost_usd": actual_usd,
                "cumulative_spend_usd": cumulative,
            })

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
    reservations: Dict[str, list] = {}
    settlements: Dict[str, list] = {}
    for row in evidence:
        if row.get("kind") == "reservation":
            reservations.setdefault(row["request_id"], []).append(
                float(row["maximum_usd"]))
        elif row.get("kind") == "cost_settlement":
            settlements.setdefault(row["request_id"], []).append(
                float(row["response_attributed_cost_usd"]))
    raw_by_request = {row.get("request_id"): row for row in evidence
                      if row.get("kind") in {
                          "sut_response", "sut_transport_error",
                          "provider_canary_response", "provider_canary_transport_error"}}
    lock = threading.Lock()
    spent = 0.0
    for request_id, actuals in settlements.items():
        maximums = reservations.get(request_id, [])
        if len(actuals) > len(maximums):
            raise CustodyStop("resume has settlement without reservation")
        for actual, maximum in zip(actuals, maximums):
            if actual < 0 or actual > maximum:
                raise CustodyStop("resume response cost exceeds reservation")
            spent += actual
    # An observed response/known no-cost transport failure may close one interrupted
    # reservation; a request with no terminal evidence is ambiguous and cannot resume.
    for request_id, maximums in reservations.items():
        actuals = settlements.get(request_id, [])
        unresolved = maximums[len(actuals):]
        if not unresolved:
            continue
        if len(unresolved) != 1:
            raise CustodyStop("resume has ambiguous duplicate paid requests")
        maximum = unresolved[0]
        raw = raw_by_request.get(request_id)
        if raw is None or raw.get("response_attributed_cost_usd") is None:
            raise CustodyStop("resume has an ambiguous paid request without cost custody")
        actual = float(raw["response_attributed_cost_usd"])
        if actual < 0 or actual > maximum:
            raise CustodyStop("resume response cost exceeds reservation")
        _append(run_dir / EVIDENCE_FILE, {
            "kind": "cost_settlement", "request_id": request_id,
            "response_attributed_cost_usd": actual,
            "cumulative_spend_usd": spent + actual,
            "recovered_after_interruption": True,
        }, lock)
        settlements.setdefault(request_id, []).append(actual)
        spent += actual
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
    canaries_passed = {row.get("sut") for row in evidence
                       if row.get("kind") == "provider_canary_validation"
                       and row.get("status") == "PASS"}
    for raw in evidence:
        if (raw.get("kind") != "provider_canary_response"
                or raw.get("sut") in canaries_passed
                or raw.get("request_id") not in settlements):
            continue
        response = raw.get("raw_response")
        spec = next((value for value in preflight.SUT_SPECS
                     if value.slug == raw.get("sut")), None)
        if spec is None or not isinstance(response, Mapping):
            raise CustodyStop("resume provider canary evidence is malformed")
        try:
            controller.validate_provider_response(spec, response)
        except controller.TerminalStop as exc:
            raise CustodyStop(str(exc)) from exc
        _append(run_dir / EVIDENCE_FILE, {
            "kind": "provider_canary_validation", "sut": spec.slug,
            "status": "PASS", "attempt": raw.get("attempt"),
            "response_sha256": raw.get("response_sha256"),
            "recovered_after_interruption": True,
        }, lock)
        canaries_passed.add(spec.slug)
    return RunState(
        run_dir=run_dir, cap_usd=cap_usd, spent_usd=spent,
        attempts_by_sut=attempts_by_sut, retries_by_sut=retries_by_sut,
        attempts_by_cell=attempts_by_cell, completed=completed,
        first_validated={row.get("sut") for row in evidence
                         if row.get("kind") == "first_cell_validation"
                         and row.get("status") == "PASS"},
        canaries_passed=canaries_passed,
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
                known_free = exc.request_definitely_not_submitted
                _append(state.run_dir / EVIDENCE_FILE, {
                    "kind": "provider_canary_transport_error", "request_id": request_id,
                    "sut": spec.slug, "attempt": attempt,
                    "error": f"{type(exc).__name__}: {exc}",
                    "response_attributed_cost_usd": 0.0 if known_free else None,
                }, state.lock)
                if not known_free:
                    reason = "ambiguous post-submit provider canary transport failure"
                    _terminal(state, reason, sut=spec.slug, request_id=request_id)
                    raise CustodyStop(reason) from exc
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
    cancellation: Optional[threading.Event] = None,
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
        if cancellation is not None and cancellation.is_set():
            raise CustodyStop("peer shard cancelled before further transport")
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
            known_free = exc.request_definitely_not_submitted
            _append(state.run_dir / EVIDENCE_FILE, {
                "kind": "sut_transport_error", "request_id": request_id,
                "cell_key": cell.key, "sut": cell.sut, "item_id": cell.item_id,
                "cell_attempt": attempt, "error": last_error,
                "response_attributed_cost_usd": 0.0 if known_free else None,
            }, state.lock)
            if not known_free:
                reason = "ambiguous post-submit SUT transport failure"
                _terminal(state, reason, cell_key=cell.key, request_id=request_id)
                raise CustodyStop(reason) from exc
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


def _phase_is_passed(state: RunState, phase: str) -> bool:
    rows = _read_jsonl(state.run_dir / EVIDENCE_FILE)
    matches = [row for row in rows if row.get("kind") == "phase_completion"
               and row.get("phase") == phase]
    if len(matches) > 1 or any(row.get("status") != "PASS" for row in matches):
        raise CustodyStop(f"{phase} phase evidence is duplicated or malformed")
    return len(matches) == 1


def _persist_phase_pass(state: RunState, phase: str, **counts: Any) -> None:
    if not _phase_is_passed(state, phase):
        _append(state.run_dir / EVIDENCE_FILE, {
            "kind": "phase_completion", "phase": phase, "status": "PASS",
            **counts,
        }, state.lock)


def execute_provider_canaries(
    manifest: Mapping[str, Any], state: RunState,
    transport: Callable[[Dict[str, Any]], Mapping[str, Any]],
) -> list:
    _require_paid_authorization(manifest)
    results = run_provider_canaries(manifest, state, transport)
    if state.canaries_passed != set(preflight.SUTS):
        raise CustodyStop("all five provider canaries must PASS")
    _persist_phase_pass(state, PHASE_PROVIDER_CANARIES, passed=5)
    return results


def execute_first_cells(
    manifest: Mapping[str, Any], state: RunState,
    transport: Callable[[Dict[str, Any]], Mapping[str, Any]],
) -> list:
    _require_paid_authorization(manifest)
    if (state.canaries_passed != set(preflight.SUTS)
            or not _phase_is_passed(state, PHASE_PROVIDER_CANARIES)):
        raise CustodyStop("all five provider canaries require persisted PASS evidence")
    items = {item.id: item for item in preflight.load_items(str(preflight.BANK_DIR))}
    cells = build_cells(manifest)
    by_sut = {sut: [cell for cell in cells if cell.sut == sut]
              for sut in preflight.SUTS}
    outcomes = []
    for sut in preflight.SUTS:
        first = by_sut[sut][0]
        outcome = run_cell(
            first, manifest=manifest, state=state, transport=transport,
            items=items, require_reasoning_gate=True)
        outcomes.append(outcome)
        if outcome.get("status") != "response" or sut not in state.first_validated:
            if hasattr(state, "run_dir") and hasattr(state, "lock"):
                _terminal(state, "five first real cells did not all PASS", sut=sut)
            raise CustodyStop("five first real cells must all PASS before shards")
    if state.first_validated != set(preflight.SUTS):
        raise CustodyStop("all five first real cells must PASS")
    _persist_phase_pass(state, PHASE_FIRST_CELLS, passed=5)
    return outcomes


def execute_remaining_run(
    manifest: Mapping[str, Any], state: RunState,
    transport: Callable[[Dict[str, Any]], Mapping[str, Any]],
) -> list:
    _require_paid_authorization(manifest)
    if (state.first_validated != set(preflight.SUTS)
            or not _phase_is_passed(state, PHASE_FIRST_CELLS)):
        raise CustodyStop("all five first real cells require persisted PASS evidence")
    items = {item.id: item for item in preflight.load_items(str(preflight.BANK_DIR))}
    cells = build_cells(manifest)
    by_sut = {sut: [cell for cell in cells if cell.sut == sut]
              for sut in preflight.SUTS}
    shards = controller.build_sut_shards(preflight.SUTS)
    cancelled = threading.Event()

    def shard_worker(shard: Sequence[str]) -> None:
        try:
            for sut in shard:
                for cell in by_sut[sut][1:]:
                    if cancelled.is_set():
                        return
                    run_cell(cell, manifest=manifest, state=state,
                             transport=transport, items=items,
                             cancellation=cancelled)
        except CustodyStop:
            cancelled.set()
            raise

    with ThreadPoolExecutor(max_workers=3) as pool:
        list(pool.map(shard_worker, shards))
    expected_keys = {cell.key for cell in cells}
    if set(state.completed) != expected_keys:
        raise CustodyStop("remaining run did not complete all 1,150 registered cells")
    _persist_phase_pass(
        state, PHASE_REMAINING_RUN, completed_cells=1150,
        scorable_cells=1130, diagnostic_only_cells=20)
    return list(state.completed.values())


def execute(
    manifest: Mapping[str, Any], state: RunState,
    transport: Callable[[Dict[str, Any]], Mapping[str, Any]],
) -> list:
    """Compatibility wrapper retained for offline tests; live CLI uses phases."""
    _require_paid_authorization(manifest)
    run_provider_canaries(manifest, state, transport)
    items = {item.id: item for item in preflight.load_items(str(preflight.BANK_DIR))}
    cells = build_cells(manifest)
    by_sut = {sut: [cell for cell in cells if cell.sut == sut]
              for sut in preflight.SUTS}
    for sut in preflight.SUTS:
        outcome = run_cell(
            by_sut[sut][0], manifest=manifest, state=state,
            transport=transport, items=items, require_reasoning_gate=True)
        if outcome.get("status") != "response" or sut not in state.first_validated:
            if hasattr(state, "run_dir") and hasattr(state, "lock"):
                _terminal(state, "five first real cells did not all PASS", sut=sut)
            raise CustodyStop("five first real cells must all PASS before shards")
    shards = controller.build_sut_shards(preflight.SUTS)
    cancelled = threading.Event()

    def shard_worker(shard: Sequence[str]) -> None:
        try:
            for sut in shard:
                for cell in by_sut[sut][1:]:
                    if cancelled.is_set():
                        return
                    run_cell(cell, manifest=manifest, state=state,
                             transport=transport, items=items,
                             cancellation=cancelled)
        except CustodyStop:
            cancelled.set()
            raise

    with ThreadPoolExecutor(max_workers=3) as pool:
        list(pool.map(shard_worker, shards))
    return list(state.completed.values())


def require_completed_run_evidence(
    run_dir: Path, manifest: Mapping[str, Any],
) -> list:
    """Validate completed append-only run custody without mutating it."""
    run_dir = Path(run_dir)
    manifest_path = run_dir / MANIFEST_COPY
    try:
        manifest_sha256 = _hash(manifest_path)
    except OSError as exc:
        raise CustodyStop("immutable completed run manifest is unreadable") from exc
    identity = _read_json(
        run_dir / IDENTITY_FILE, "immutable completed run identity is unreadable")
    expected_identity = {
        "schema_version": 1,
        "kind": "wcf_bench_pilot2_immutable_run",
        "validity_label": preflight.VALIDITY_LABEL,
        "manifest_sha256": manifest_sha256,
        "exact_sut_slugs": list(preflight.SUTS),
        "expected_cells": 1150,
        "scorable_cells": 1130,
        "diagnostic_only_cells": 20,
        "cap_usd": STRICT_CAP_USD,
    }
    if identity != expected_identity:
        raise CustodyStop("immutable completed run identity is invalid")
    if _read_json(manifest_path, "run manifest is unreadable") != dict(manifest):
        raise CustodyStop("run manifest does not match authorized manifest")
    evidence = _read_jsonl(run_dir / EVIDENCE_FILE)
    if any(row.get("kind") == "terminal_stop" for row in evidence):
        raise CustodyStop("immutable completed run records a terminal stop")
    phase_rows = [row for row in evidence if row.get("kind") == "phase_completion"]
    if [(row.get("phase"), row.get("status")) for row in phase_rows] != [
            (PHASE_PROVIDER_CANARIES, "PASS"),
            (PHASE_FIRST_CELLS, "PASS"),
            (PHASE_REMAINING_RUN, "PASS")]:
        raise CustodyStop("immutable completed run lacks exact phase PASS evidence")
    if {row.get("sut") for row in evidence
            if row.get("kind") == "provider_canary_validation"
            and row.get("status") == "PASS"} != set(preflight.SUTS):
        raise CustodyStop("immutable completed run lacks five provider canary PASS records")
    expected_cells = {cell.key: cell for cell in build_cells(manifest)}
    expected_first = {cell.key for cell in expected_cells.values()
                      if cell.item_id == (manifest.get("schedule") or {})[
                          "all_item_ids"][0]}
    if {row.get("cell_key") for row in evidence
            if row.get("kind") == "first_cell_validation"
            and row.get("status") == "PASS"} != expected_first:
        raise CustodyStop("immutable completed run lacks five first-cell PASS records")
    indexed = list(enumerate(evidence))
    request_kinds = {"provider_canary_request", "sut_request"}
    outcome_kinds = {
        "provider_canary_response", "provider_canary_transport_error",
        "sut_response", "sut_transport_error",
    }

    def unique_by_request(kinds: set, label: str) -> Dict[str, tuple]:
        found: Dict[str, tuple] = {}
        for index, row in indexed:
            if row.get("kind") not in kinds:
                continue
            request_id = row.get("request_id")
            if not isinstance(request_id, str) or not request_id:
                raise CustodyStop(f"immutable run {label} request identity is invalid")
            if request_id in found:
                raise CustodyStop(f"immutable run {label} evidence is duplicated")
            found[request_id] = (index, row)
        return found

    reservations = unique_by_request({"reservation"}, "reservation")
    requests = unique_by_request(request_kinds, "request")
    outcomes = unique_by_request(outcome_kinds, "response/error")
    settlements = unique_by_request({"cost_settlement"}, "settlement")
    request_ids = set(requests)
    if (not request_ids or set(reservations) != request_ids
            or set(outcomes) != request_ids or set(settlements) != request_ids):
        raise CustodyStop(
            "immutable run request/response/settlement evidence is not exact")
    spent = 0.0
    for request_id in request_ids:
        reservation_index, reservation = reservations[request_id]
        request_index, _request = requests[request_id]
        outcome_index, _outcome = outcomes[request_id]
        settlement_index, settlement = settlements[request_id]
        maximum = reservation.get("maximum_usd")
        actual = settlement.get("response_attributed_cost_usd")
        if (not isinstance(maximum, (int, float)) or isinstance(maximum, bool)
                or not math.isfinite(float(maximum)) or maximum <= 0):
            raise CustodyStop("immutable run reservation evidence is invalid")
        if (not isinstance(actual, (int, float)) or isinstance(actual, bool)
                or not math.isfinite(float(actual)) or actual < 0
                or actual > float(maximum) + 1e-12):
            raise CustodyStop("immutable run settlement cost is invalid")
        if not (reservation_index < request_index < outcome_index < settlement_index):
            raise CustodyStop("immutable run request custody order is invalid")
    for _index, settlement in sorted(settlements.values()):
        actual = float(settlement["response_attributed_cost_usd"])
        spent += actual
        cumulative = settlement.get("cumulative_spend_usd")
        if (not isinstance(cumulative, (int, float))
                or isinstance(cumulative, bool)
                or not math.isfinite(float(cumulative))
                or abs(float(cumulative) - spent) > 1e-12):
            raise CustodyStop(
                "immutable run cumulative settlement cost is invalid")
    if spent > STRICT_CAP_USD + 1e-12:
        raise CustodyStop("immutable run has over-cap custody")

    items = {item.id: item for item in preflight.load_items(str(preflight.BANK_DIR))}
    spec_by_sut = {spec.slug: spec for spec in preflight.SUT_SPECS}
    cell_attempts: Dict[str, list] = {}
    model_attempts: Dict[str, list] = {sut: [] for sut in preflight.SUTS}
    retry_attempts: Dict[str, int] = {sut: 0 for sut in preflight.SUTS}
    terminal_error_by_request: Dict[str, str] = {}
    successful_by_request: Dict[str, Dict[str, Any]] = {}

    for request_id, (_index, request) in requests.items():
        outcome = outcomes[request_id][1]
        settlement = settlements[request_id][1]
        reservation = reservations[request_id][1]
        kind = request.get("kind")
        sut = request.get("sut")
        spec = spec_by_sut.get(sut)
        if spec is None:
            raise CustodyStop("immutable run request SUT is invalid")
        if abs(float(reservation["maximum_usd"])
               - _maximum_cost(manifest, sut)) > 1e-12:
            raise CustodyStop("immutable run reservation/model cost linkage is invalid")
        if kind == "provider_canary_request":
            attempt = request.get("attempt")
            if (not isinstance(attempt, int) or isinstance(attempt, bool)
                    or attempt not in {1, 2}
                    or request_id != f"canary::{sut}::{attempt}"
                    or not isinstance(request.get("payload"), Mapping)
                    or request["payload"].get("model") != sut
                    or outcome.get("sut") != sut
                    or outcome.get("attempt") != attempt):
                raise CustodyStop("immutable provider canary request linkage is invalid")
        elif kind == "sut_request":
            cell_key = request.get("cell_key")
            cell = expected_cells.get(cell_key)
            attempt = request.get("cell_attempt")
            model_attempt = request.get("model_attempt")
            if (cell is None or sut != cell.sut
                    or request.get("item_id") != cell.item_id
                    or not isinstance(attempt, int) or isinstance(attempt, bool)
                    or attempt < 1 or attempt > MAX_RETRIES_PER_CELL + 1
                    or request_id != f"cell::{cell_key}::{attempt}"
                    or not isinstance(model_attempt, int)
                    or isinstance(model_attempt, bool) or model_attempt < 1
                    or request.get("diagnostic_only") is not cell.diagnostic_only
                    or request.get("scorable") is not cell.scorable):
                raise CustodyStop("immutable SUT request identity is invalid")
            expected_payload = controller.build_sut_request(
                manifest, sut, build_blind_messages(items[cell.item_id]))
            if request.get("payload") != expected_payload:
                raise CustodyStop("immutable SUT request model/payload linkage is invalid")
            for field in ("cell_key", "sut", "item_id", "cell_attempt"):
                if outcome.get(field) != request.get(field):
                    raise CustodyStop("immutable SUT response identity is invalid")
            if outcome.get("kind") == "sut_response":
                if (outcome.get("model_attempt") != model_attempt
                        or outcome.get("diagnostic_only") is not cell.diagnostic_only
                        or outcome.get("scorable") is not cell.scorable):
                    raise CustodyStop("immutable SUT response model linkage is invalid")
            cell_attempts.setdefault(cell_key, []).append((attempt, request_id))
            model_attempts[sut].append(model_attempt)
            if attempt > 1:
                retry_attempts[sut] += 1
        else:
            raise CustodyStop("immutable completed run request kind is invalid")

        if outcome.get("kind") in {
                "provider_canary_transport_error", "sut_transport_error"}:
            if (not isinstance(outcome.get("error"), str)
                    or not outcome["error"]
                    or outcome.get("response_attributed_cost_usd") != 0.0
                    or settlement.get("response_attributed_cost_usd") != 0.0):
                raise CustodyStop("immutable transport error custody is invalid")
            terminal_error_by_request[request_id] = outcome["error"]
            continue
        expected_response_kind = (
            "provider_canary_response" if kind == "provider_canary_request"
            else "sut_response")
        raw_response = outcome.get("raw_response")
        if (outcome.get("kind") != expected_response_kind
                or not isinstance(raw_response, Mapping)
                or raw_response.get("provider") != spec.provider
                or outcome.get("response_sha256") != _response_hash(raw_response)):
            raise CustodyStop("immutable raw response identity is invalid")
        raw_cost = _cost(raw_response)
        outcome_cost = outcome.get("response_attributed_cost_usd")
        if (not isinstance(outcome_cost, (int, float))
                or isinstance(outcome_cost, bool)
                or not math.isfinite(float(outcome_cost))
                or abs(float(outcome_cost) - raw_cost) > 1e-12
                or abs(float(settlement["response_attributed_cost_usd"]) - raw_cost)
                > 1e-12):
            raise CustodyStop("immutable response/settlement cost linkage is invalid")
        if kind == "provider_canary_request":
            continue
        cell = expected_cells[request["cell_key"]]
        if outcome.get("status") == "response":
            if raw_response.get("error"):
                raise CustodyStop("immutable successful response contains an error")
            try:
                parsed = _ordinary_validation(
                    spec, raw_response,
                    reasoning_gate=cell.item_id == (manifest.get("schedule") or {})[
                        "all_item_ids"][0])
            except (CustodyStop, ValueError) as exc:
                raise CustodyStop("immutable successful response is invalid") from exc
            if (outcome.get("final_answer") != parsed["final_answer"]
                    or outcome.get("private_reasoning") != parsed["private_reasoning"]
                    or outcome.get("reasoning_tokens") != parsed["reasoning_tokens"]):
                raise CustodyStop("immutable successful response content is invalid")
            successful_by_request[request_id] = outcome
        elif outcome.get("status") == "upstream_error":
            if not raw_response.get("error"):
                raise CustodyStop("immutable upstream error response is invalid")
            terminal_error_by_request[request_id] = str(raw_response["error"])
        elif outcome.get("status") == "ordinary_error":
            if raw_response.get("error"):
                raise CustodyStop("immutable ordinary error response is invalid")
            try:
                _ordinary_validation(
                    spec, raw_response,
                    reasoning_gate=cell.item_id == (manifest.get("schedule") or {})[
                        "all_item_ids"][0])
            except ValueError as exc:
                terminal_error_by_request[request_id] = str(exc)
            except CustodyStop as exc:
                raise CustodyStop("immutable ordinary error response is terminal") from exc
            else:
                raise CustodyStop("immutable ordinary error response is valid")
        else:
            raise CustodyStop("immutable SUT response status is invalid")

    for sut, attempts in model_attempts.items():
        if sorted(attempts) != list(range(1, len(attempts) + 1)):
            raise CustodyStop("immutable model attempt sequence is invalid")

    canary_validations = [row for row in evidence
                          if row.get("kind") == "provider_canary_validation"]
    if len(canary_validations) != len(preflight.SUTS):
        raise CustodyStop("immutable provider canary validation is duplicated")
    for row in canary_validations:
        request_id = f"canary::{row.get('sut')}::{row.get('attempt')}"
        response = outcomes.get(request_id, (None, {}))[1]
        if (row.get("status") != "PASS"
                or response.get("kind") != "provider_canary_response"
                or row.get("response_sha256") != response.get("response_sha256")):
            raise CustodyStop("immutable provider canary PASS linkage is invalid")

    checkpoints = _read_jsonl(run_dir / CHECKPOINT_FILE)
    by_key = {row.get("cell_key"): row for row in checkpoints}
    if (len(checkpoints) != 1150 or len(by_key) != 1150
            or set(by_key) != set(expected_cells)):
        raise CustodyStop("immutable completed run lacks 1,150 unique checkpoints")
    for key, row in by_key.items():
        cell = expected_cells[key]
        attempts = sorted(cell_attempts.get(key, []))
        attempt_numbers = [attempt for attempt, _request_id in attempts]
        if (row.get("kind") != "pilot2_cell"
                or row.get("sut") != cell.sut or row.get("item_id") != cell.item_id
                or row.get("diagnostic_only") is not cell.diagnostic_only
                or row.get("scorable") is not cell.scorable
                or row.get("score") is not None
                or row.get("status") not in {"response", "error"}
                or attempt_numbers != list(range(1, len(attempts) + 1))
                or not attempts or row.get("attempts") != len(attempts)):
            raise CustodyStop("immutable completed run checkpoint identity is invalid")
        final_request_id = attempts[-1][1]
        successes = [request_id for _attempt, request_id in attempts
                     if request_id in successful_by_request]
        if row["status"] == "response":
            if (row.get("missing") is not False
                    or not isinstance(row.get("final_answer"), str)
                    or not row["final_answer"]
                    or successes != [final_request_id]):
                raise CustodyStop("completed response checkpoint is invalid")
            response = successful_by_request[final_request_id]
            if (row.get("response_sha256") != response.get("response_sha256")
                    or row.get("final_answer") != response.get("final_answer")):
                raise CustodyStop("completed response checkpoint linkage is invalid")
        else:
            if row.get("missing") is not True or successes:
                raise CustodyStop("completed missing checkpoint is invalid")
            expected_error = terminal_error_by_request.get(final_request_id)
            actual_error = row.get("error")
            exhausted = (
                actual_error == "registered model attempt envelope exhausted"
                and len(model_attempts[cell.sut]) == 252) or (
                actual_error == "registered model retry reserve exhausted"
                and retry_attempts[cell.sut] == 22
                and len(model_attempts[cell.sut]) < 252)
            if (not isinstance(actual_error, str) or not actual_error
                    or (actual_error != expected_error and not exhausted)):
                raise CustodyStop("completed missing checkpoint linkage is invalid")
    return checkpoints


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
    authorization_validator: Callable[[Mapping[str, Any]], None] =
        require_bound_authorization,
    phase_functions: Optional[Mapping[str, Callable[
        [Mapping[str, Any], RunState,
         Callable[[Dict[str, Any]], Mapping[str, Any]]], Any]]] = None,
) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--go", action="store_true")
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--cap", type=float, required=True)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument(
        "--phase", choices=PHASES, required=True,
        help="exactly one registered live gate phase")
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
        authorization_validator(manifest)
        gate = manifest.get("authorization_gate") or {}
        if gate.get("paid_inference") is not True:
            raise CustodyStop("manifest lacks amount-specific paid authorization")
        proposed = float((manifest.get("planning_cost") or {})["proposed_cap_usd"])
        if args.cap != proposed:
            raise CustodyStop("CLI cap must equal the amount-specific authorized cap")
        catalog, endpoints = runtime_fetch()
        validate_runtime_catalog(manifest, catalog, endpoints)
        with exclusive_run_lease(args.output_dir):
            _require_sufficient_balance(manifest, key, balance_fetch)
            state = prepare_run(
                args.manifest, args.output_dir, cap_usd=args.cap,
                resume=args.resume or args.phase in {
                    PHASE_FIRST_CELLS, PHASE_REMAINING_RUN})
            transport = transport_factory(key)
            phases = phase_functions or {
                PHASE_PROVIDER_CANARIES: execute_provider_canaries,
                PHASE_FIRST_CELLS: execute_first_cells,
                PHASE_REMAINING_RUN: execute_remaining_run,
            }
            if set(phases) != set(PHASES):
                raise CustodyStop("live phase dispatch does not match registered phases")
            phases[args.phase](manifest, state, transport)
    except (CustodyStop, controller.TerminalStop) as exc:
        print(f"Pilot 2 stopped: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
