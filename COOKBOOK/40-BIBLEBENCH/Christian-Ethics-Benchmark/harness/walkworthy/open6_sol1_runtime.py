"""Fail-closed, offline-testable runtime seams for OPEN6-SOL1.

This module owns attempt accounting and the single registered defect replay.  It
does not load credentials, select PUBLIC items, orchestrate the full surface, or
store response bodies in its ledgers.
"""

from __future__ import annotations

import fcntl
import hashlib
import json
import math
import os
import re
import subprocess
import tempfile
import threading
from contextlib import contextmanager
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Callable, Optional

from .clients import Message, ModelResponse
from .cli_backends import ModelCallError
from .open6_sol1 import (
    HARD_NTE_USD,
    OPENROUTER_HARD_CALL_CAP,
    OPENROUTER_NOMINAL_CALLS,
    OPENROUTER_RESERVE_CALLS,
    OUTPUT_CAP_TOKENS,
    SOL_HARD_TURN_CAP,
    SOL_RESERVE_TURNS,
    _model_manifest,
    canonical_json_bytes,
    sol_runtime_contract,
)
from .openrouter_backend import OpenRouterClient


MAX_CONCURRENCY = 2
INPUT_ENVELOPE = 24_000
SOL_MODEL = "gpt-5.6-sol"


class ContractStop(RuntimeError):
    """The request or persisted custody differs from the frozen pilot."""


class BudgetStop(RuntimeError):
    """The next attempt would exceed a registered cap or reservation."""


class ThreadStop(RuntimeError):
    """A logical task used its one exact replay without a valid result."""


@dataclass(frozen=True)
class ModelSpec:
    slug: str
    role: str
    max_tokens: int
    input_envelope: int
    observed_input_per_m: Decimal
    observed_output_per_m: Decimal
    ceiling_input_per_m: Decimal
    ceiling_output_per_m: Decimal

    @property
    def provider_prefs(self) -> dict:
        return {
            "sort": "price",
            "require_parameters": True,
            "allow_fallbacks": True,
            "max_price": {
                "prompt": float(self.ceiling_input_per_m),
                "completion": float(self.ceiling_output_per_m),
            },
        }

    @property
    def max_call_usd(self) -> Decimal:
        return (
            Decimal(self.input_envelope) * self.ceiling_input_per_m
            + Decimal(self.max_tokens) * self.ceiling_output_per_m
        ) / Decimal(1_000_000)


def _specs_from_frozen_manifest():
    specs = []
    for row in _model_manifest():
        specs.append(ModelSpec(
            slug=row["slug"],
            role="sut",
            max_tokens=OUTPUT_CAP_TOKENS,
            input_envelope=INPUT_ENVELOPE,
            observed_input_per_m=Decimal(row["input_per_m_usd"]),
            observed_output_per_m=Decimal(row["output_per_m_usd"]),
            ceiling_input_per_m=Decimal(
                row["provider_ceiling"]["prompt_per_m_usd"]),
            ceiling_output_per_m=Decimal(
                row["provider_ceiling"]["completion_per_m_usd"]),
        ))
    return tuple(specs)


SUT_SPECS = _specs_from_frozen_manifest()
_SPECS = {spec.slug: spec for spec in SUT_SPECS}


def make_openrouter_client(spec: ModelSpec, api_key: str, transport) -> OpenRouterClient:
    if _SPECS.get(spec.slug) != spec:
        raise ContractStop(f"unauthorized OPEN6-SOL1 model spec: {spec}")
    return OpenRouterClient(
        spec.slug,
        model=spec.slug,
        api_key=api_key,
        transport=transport,
        max_tokens=spec.max_tokens,
        provider_prefs=spec.provider_prefs,
        max_retries=0,
        empty_retries=0,
    )


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _canonical_hash(value) -> str:
    return _sha256_bytes(canonical_json_bytes(value))


def _transport_payload_hash(payload: dict) -> str:
    # Matches openrouter_backend._default_transport exactly.
    return _sha256_bytes(json.dumps(payload).encode("utf-8"))


def _decimal(value):
    if isinstance(value, bool) or not isinstance(value, (int, float, Decimal)):
        return None
    if isinstance(value, float) and not math.isfinite(value):
        return None
    try:
        result = Decimal(str(value))
    except InvalidOperation:
        return None
    return result if result.is_finite() and result >= 0 else None


def _is_hash(value) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


_LOCAL_LOCKS = {}
_LOCAL_LOCKS_GUARD = threading.Lock()


def _local_lock(path: Path):
    key = str(path.resolve())
    with _LOCAL_LOCKS_GUARD:
        return _LOCAL_LOCKS.setdefault(key, threading.RLock())


@contextmanager
def _file_lock(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with _local_lock(path):
        with path.open("a+", encoding="utf-8") as handle:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def _event_hash(event: dict) -> str:
    return _canonical_hash({key: value for key, value in event.items()
                            if key != "event_sha256"})


def _append_event(path: Path, event: dict, previous_hash: Optional[str]) -> dict:
    stored = dict(event)
    stored["previous_sha256"] = previous_hash
    stored["event_sha256"] = _event_hash(stored)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(stored, sort_keys=True, separators=(",", ":")) + "\n")
        handle.flush()
        os.fsync(handle.fileno())
    return stored


class OpenRouterAttemptLedger:
    """Hash-chained, file-locked, body-free OpenRouter attempt ledger."""

    def __init__(self, path, *, hard_nte_usd=Decimal(HARD_NTE_USD),
                 planned_cap=OPENROUTER_NOMINAL_CALLS,
                 max_attempts=OPENROUTER_HARD_CALL_CAP,
                 replay_cap=OPENROUTER_RESERVE_CALLS,
                 max_concurrency=MAX_CONCURRENCY):
        self.path = Path(path)
        self.lock_path = Path(str(self.path) + ".lock")
        self.hard_nte_usd = Decimal(str(hard_nte_usd))
        self.planned_cap = int(planned_cap)
        self.max_attempts = int(max_attempts)
        self.replay_cap = int(replay_cap)
        self.max_concurrency = int(max_concurrency)
        if not (Decimal("0") < self.hard_nte_usd <= Decimal(HARD_NTE_USD)):
            raise ContractStop("invalid OPEN6-SOL1 hard NTE")
        if not (0 < self.max_attempts <= OPENROUTER_HARD_CALL_CAP):
            raise ContractStop("invalid OPEN6-SOL1 call cap")
        if not (0 < self.planned_cap <= OPENROUTER_NOMINAL_CALLS):
            raise ContractStop("invalid OPEN6-SOL1 planned cap")
        if not (0 <= self.replay_cap <= OPENROUTER_RESERVE_CALLS):
            raise ContractStop("invalid OPEN6-SOL1 replay cap")
        if not (1 <= self.max_concurrency <= MAX_CONCURRENCY):
            raise ContractStop("invalid OPEN6-SOL1 concurrency cap")
        self.registration = {
            "event": "ledger_registered",
            "ledger": "openrouter",
            "hard_nte_usd": str(self.hard_nte_usd),
            "planned_cap": self.planned_cap,
            "max_attempts": self.max_attempts,
            "replay_cap": self.replay_cap,
            "max_concurrency": self.max_concurrency,
        }
        with _file_lock(self.lock_path):
            if not self.path.exists():
                _append_event(self.path, self.registration, None)
            self._load(allow_inflight=False)

    def _read_events(self):
        events = []
        previous = None
        try:
            lines = self.path.read_text(encoding="utf-8").splitlines()
        except OSError as exc:
            raise ContractStop("cannot read OPEN6-SOL1 ledger") from exc
        for line_number, line in enumerate(lines, 1):
            try:
                event = json.loads(line)
            except (json.JSONDecodeError, TypeError) as exc:
                raise ContractStop(f"invalid ledger JSON line {line_number}") from exc
            if (not isinstance(event, dict)
                    or event.get("previous_sha256") != previous
                    or not _is_hash(event.get("event_sha256"))
                    or event["event_sha256"] != _event_hash(event)):
                raise ContractStop(f"ledger hash-chain failure at line {line_number}")
            previous = event["event_sha256"]
            events.append(event)
        if not events:
            raise ContractStop("empty OPEN6-SOL1 ledger")
        return events

    def _load(self, *, allow_inflight):
        events = self._read_events()
        expected_registration = dict(self.registration)
        expected_registration.update({
            "previous_sha256": None,
            "event_sha256": events[0].get("event_sha256"),
        })
        if events[0] != expected_registration:
            raise ContractStop("ledger registration contract mismatch")
        self._starts = {}
        self._finishes = {}
        histories = {}
        for event in events[1:]:
            kind = event.get("event")
            attempt = event.get("attempt_id")
            if type(attempt) is not int or attempt < 1:
                raise ContractStop("invalid attempt id")
            if kind == "attempt_started":
                required = {
                    "event", "attempt_id", "logical_key", "role", "requested_model",
                    "payload_sha256", "ceiling_max_usd", "replay",
                    "previous_sha256", "event_sha256",
                }
                spec = _SPECS.get(event.get("requested_model"))
                if (set(event) != required or event.get("role") != "sut"
                        or spec is None or event.get("ceiling_max_usd") != str(spec.max_call_usd)
                        or not isinstance(event.get("logical_key"), str)
                        or not event["logical_key"] or not _is_hash(event.get("payload_sha256"))
                        or type(event.get("replay")) is not bool
                        or attempt != len(self._starts) + 1):
                    raise ContractStop("invalid persisted OpenRouter start")
                history = histories.setdefault(event["logical_key"], [])
                if event["replay"] != bool(history) or len(history) >= 2:
                    raise ContractStop("invalid persisted OpenRouter replay")
                if history:
                    prior = self._finishes.get(history[0])
                    first = self._starts[history[0]]
                    if (prior is None or prior["failure"] is None
                            or event["payload_sha256"] != first["payload_sha256"]
                            or event["requested_model"] != first["requested_model"]):
                        raise ContractStop("non-identical or premature OpenRouter replay")
                self._starts[attempt] = event
                history.append(attempt)
            elif kind == "attempt_finished":
                required = {
                    "event", "attempt_id", "logical_key", "role", "requested_model",
                    "status", "returned_model", "booked_usd", "cost_basis",
                    "prompt_tokens", "completion_tokens", "failure", "error_sha256",
                    "response_sha256", "previous_sha256", "event_sha256",
                }
                start = self._starts.get(attempt)
                if (set(event) != required or start is None or attempt in self._finishes
                        or event["logical_key"] != start["logical_key"]
                        or event["role"] != start["role"]
                        or event["requested_model"] != start["requested_model"]):
                    raise ContractStop("invalid persisted OpenRouter finish")
                self._validate_finish(start, event)
                self._finishes[attempt] = event
            else:
                raise ContractStop("unknown OpenRouter ledger event")
        if len(self._starts) > self.max_attempts:
            raise ContractStop("persisted OpenRouter call cap exceeded")
        if len({start["logical_key"] for start in self._starts.values()}) > self.planned_cap:
            raise ContractStop("persisted OpenRouter planned cap exceeded")
        if sum(start["replay"] for start in self._starts.values()) > self.replay_cap:
            raise ContractStop("persisted OpenRouter replay cap exceeded")
        inflight = set(self._starts) - set(self._finishes)
        if len(inflight) > self.max_concurrency:
            raise ContractStop("persisted OpenRouter concurrency exceeded")
        if inflight and not allow_inflight:
            raise ContractStop(f"unresolved in-flight OpenRouter attempt(s): {sorted(inflight)}")
        if self._booked() + self._inflight() > self.hard_nte_usd:
            raise ContractStop("persisted OpenRouter NTE exceeded")
        self._last_hash = events[-1]["event_sha256"]

    @staticmethod
    def _validate_finish(start, event):
        spec = _SPECS[start["requested_model"]]
        if (event["status"] is not None
                and (type(event["status"]) is not int or not 100 <= event["status"] <= 599)):
            raise ContractStop("invalid persisted status")
        if event["returned_model"] is not None and not isinstance(event["returned_model"], str):
            raise ContractStop("invalid persisted model")
        try:
            booked = Decimal(event["booked_usd"])
        except (InvalidOperation, TypeError):
            raise ContractStop("invalid persisted cost")
        if not booked.is_finite() or booked < 0:
            raise ContractStop("invalid persisted cost")
        if event["cost_basis"] not in ("reported", "registered_max"):
            raise ContractStop("invalid persisted cost basis")
        if event["cost_basis"] == "registered_max" and booked != spec.max_call_usd:
            raise ContractStop("invalid persisted registered maximum")
        for field in ("prompt_tokens", "completion_tokens"):
            if type(event[field]) is not int or event[field] < 0:
                raise ContractStop("invalid persisted token custody")
        if event["failure"] not in (
                None, "http_failure", "empty", "malformed", "wrong_model", "missing_cost"):
            raise ContractStop("invalid persisted failure class")
        for field in ("error_sha256", "response_sha256"):
            if event[field] is not None and not _is_hash(event[field]):
                raise ContractStop("invalid persisted custody hash")
        if event["failure"] is None and not (
                event["status"] == 200 and event["returned_model"] == spec.slug
                and event["cost_basis"] == "reported"):
            raise ContractStop("invalid persisted successful custody")

    def _history(self, logical_key):
        return [attempt for attempt, start in sorted(self._starts.items())
                if start["logical_key"] == logical_key]

    def _booked(self):
        return sum((Decimal(event["booked_usd"])
                    for event in self._finishes.values()), Decimal("0"))

    def _reserved(self):
        return sum((Decimal(event["booked_usd"])
                    for event in self._finishes.values()
                    if event["cost_basis"] == "registered_max"), Decimal("0"))

    def _inflight(self):
        return sum((Decimal(start["ceiling_max_usd"])
                    for attempt, start in self._starts.items()
                    if attempt not in self._finishes), Decimal("0"))

    def begin(self, logical_key: str, spec: ModelSpec, payload: dict) -> int:
        if _SPECS.get(spec.slug) != spec:
            raise ContractStop("unauthorized OpenRouter model spec")
        if (not isinstance(payload, dict) or payload.get("model") != spec.slug
                or payload.get("max_tokens") != spec.max_tokens
                or payload.get("provider") != spec.provider_prefs
                or {"temperature", "top_p", "top_k", "reasoning"} & set(payload)):
            raise ContractStop("OpenRouter payload contract mismatch")
        input_bytes = len(json.dumps({"messages": payload.get("messages")}).encode("utf-8"))
        if input_bytes > spec.input_envelope:
            raise ContractStop("OpenRouter input envelope exceeded")
        digest = _transport_payload_hash(payload)
        with _file_lock(self.lock_path):
            self._load(allow_inflight=True)
            history = self._history(logical_key)
            replay = bool(history)
            if history:
                prior = self._finishes.get(history[-1])
                first = self._starts[history[0]]
                if prior is None:
                    raise ThreadStop(f"OpenRouter key already in flight: {logical_key}")
                if prior["failure"] is None:
                    raise ContractStop(f"duplicate completed OpenRouter key: {logical_key}")
                if len(history) >= 2:
                    raise ThreadStop(f"OpenRouter replay exhausted: {logical_key}")
                if (digest != first["payload_sha256"]
                        or spec.slug != first["requested_model"]):
                    raise ContractStop("OpenRouter replay must be byte-identical")
                if sum(start["replay"] for start in self._starts.values()) >= self.replay_cap:
                    raise BudgetStop("OpenRouter replay reserve exhausted")
            if len(self._starts) >= self.max_attempts:
                raise BudgetStop("OpenRouter call cap exhausted")
            if (not history and len({start["logical_key"]
                                     for start in self._starts.values()})
                    >= self.planned_cap):
                raise BudgetStop("OpenRouter planned call cap exhausted")
            if len(self._starts) - len(self._finishes) >= self.max_concurrency:
                raise BudgetStop("OpenRouter concurrency cap exhausted")
            if self._booked() + self._inflight() + spec.max_call_usd > self.hard_nte_usd:
                raise BudgetStop("OpenRouter hard NTE reservation exceeded")
            attempt = len(self._starts) + 1
            event = {
                "event": "attempt_started", "attempt_id": attempt,
                "logical_key": logical_key, "role": "sut",
                "requested_model": spec.slug, "payload_sha256": digest,
                "ceiling_max_usd": str(spec.max_call_usd), "replay": replay,
            }
            stored = _append_event(self.path, event, self._last_hash)
            self._starts[attempt] = stored
            self._last_hash = stored["event_sha256"]
            return attempt

    def finish(self, attempt: int, status, body) -> Optional[str]:
        with _file_lock(self.lock_path):
            self._load(allow_inflight=True)
            start = self._starts.get(attempt)
            if start is None or attempt in self._finishes:
                raise ContractStop("unknown or duplicate OpenRouter finish")
            spec = _SPECS[start["requested_model"]]
            response = body if isinstance(body, dict) else {}
            usage = response.get("usage") if isinstance(response.get("usage"), dict) else {}
            cost = _decimal(usage.get("cost"))
            returned = response.get("model") if isinstance(response.get("model"), str) else None
            choices = response.get("choices")
            content = None
            if isinstance(choices, list) and choices and isinstance(choices[0], dict):
                message = choices[0].get("message")
                if isinstance(message, dict):
                    content = message.get("content")
            if status != 200:
                failure = "http_failure"
            elif returned != spec.slug:
                failure = "wrong_model"
            elif cost is None:
                failure = "missing_cost"
            elif not isinstance(content, str):
                failure = "malformed"
            elif not content.strip():
                failure = "empty"
            else:
                failure = None
            booked = cost if cost is not None else spec.max_call_usd
            event = {
                "event": "attempt_finished", "attempt_id": attempt,
                "logical_key": start["logical_key"], "role": start["role"],
                "requested_model": spec.slug, "status": status,
                "returned_model": returned, "booked_usd": str(booked),
                "cost_basis": "reported" if cost is not None else "registered_max",
                "prompt_tokens": usage.get("prompt_tokens", 0)
                    if type(usage.get("prompt_tokens", 0)) is int else 0,
                "completion_tokens": usage.get("completion_tokens", 0)
                    if type(usage.get("completion_tokens", 0)) is int else 0,
                "failure": failure,
                "error_sha256": (_canonical_hash(response.get("error"))
                                   if response.get("error") is not None else None),
                "response_sha256": _canonical_hash(response),
            }
            self._validate_finish(start, {**event, "previous_sha256": self._last_hash,
                                          "event_sha256": _event_hash({
                                              **event, "previous_sha256": self._last_hash})})
            stored = _append_event(self.path, event, self._last_hash)
            self._finishes[attempt] = stored
            self._last_hash = stored["event_sha256"]
            if self._booked() + self._inflight() > self.hard_nte_usd:
                raise BudgetStop("OpenRouter hard NTE exceeded after custody")
            return failure

    def snapshot(self) -> dict:
        with _file_lock(self.lock_path):
            self._load(allow_inflight=True)
            return {
                "attempts": len(self._starts),
                "replays": sum(start["replay"] for start in self._starts.values()),
                "booked_usd": self._booked(),
                "reserved_usd": self._reserved(),
                "inflight_usd": self._inflight(),
            }


@dataclass(frozen=True)
class OpenRouterRunResult:
    response: ModelResponse
    body: dict
    payload: dict
    attempt_ids: tuple


class OpenRouterPilotClient:
    """One exact-model OpenRouter client with the pilot-owned single replay."""

    def __init__(self, spec: ModelSpec, api_key: str,
                 ledger: OpenRouterAttemptLedger, transport,
                 response_sink: Optional[Callable] = None):
        self.spec = spec
        self.ledger = ledger
        self.response_sink = response_sink
        self._last_transport = {}

        def capturing_transport(url, headers, payload, timeout=None):
            status, body = transport(url, headers, payload, timeout=timeout)
            self._last_transport = {"status": status, "body": body}
            return status, body

        self.base_client = make_openrouter_client(spec, api_key, capturing_transport)

    def complete(self, logical_key: str, messages, system=None) -> OpenRouterRunResult:
        payload = self.base_client.build_payload(messages, system)
        attempt_ids = []
        for index in range(2):
            attempt = self.ledger.begin(logical_key, self.spec, payload)
            attempt_ids.append(attempt)
            self._last_transport = {}
            response = None
            try:
                response = self.base_client.complete(messages, system=system)
            except ModelCallError:
                pass
            status = self._last_transport.get("status")
            body = self._last_transport.get("body", {})
            if self.response_sink is not None:
                self.response_sink({
                    "logical_key": logical_key,
                    "attempt_id": attempt,
                    "status": status,
                    "body": body,
                })
            failure = self.ledger.finish(attempt, status, body)
            if failure is None and response is not None:
                return OpenRouterRunResult(
                    response=response, body=body, payload=payload,
                    attempt_ids=tuple(attempt_ids),
                )
            if index == 1:
                raise ThreadStop(f"OpenRouter second failure for {logical_key}: {failure}")
        raise AssertionError("unreachable")


class SolTaskLedger:
    """Hash-chained, body-free attempt ledger for Sol OAuth tasks."""

    def __init__(self, path, *, max_attempts=SOL_HARD_TURN_CAP,
                 replay_cap=SOL_RESERVE_TURNS, max_concurrency=MAX_CONCURRENCY):
        self.path = Path(path)
        self.lock_path = Path(str(self.path) + ".lock")
        self.max_attempts = int(max_attempts)
        self.replay_cap = int(replay_cap)
        self.max_concurrency = int(max_concurrency)
        if not (0 < self.max_attempts <= SOL_HARD_TURN_CAP):
            raise ContractStop("invalid Sol attempt cap")
        if not (0 <= self.replay_cap <= SOL_RESERVE_TURNS):
            raise ContractStop("invalid Sol replay cap")
        if not (1 <= self.max_concurrency <= MAX_CONCURRENCY):
            raise ContractStop("invalid Sol concurrency cap")
        self.registration = {
            "event": "ledger_registered", "ledger": "sol",
            "max_attempts": self.max_attempts, "replay_cap": self.replay_cap,
            "max_concurrency": self.max_concurrency,
        }
        with _file_lock(self.lock_path):
            if not self.path.exists():
                _append_event(self.path, self.registration, None)
            self._load(allow_inflight=False)

    def _load(self, *, allow_inflight):
        # Reuse the same hash-chain parser without coupling the accounting types.
        raw = []
        previous = None
        for line_number, line in enumerate(
                self.path.read_text(encoding="utf-8").splitlines(), 1):
            try:
                event = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ContractStop(f"invalid Sol ledger JSON line {line_number}") from exc
            if (not isinstance(event, dict) or event.get("previous_sha256") != previous
                    or not _is_hash(event.get("event_sha256"))
                    or event["event_sha256"] != _event_hash(event)):
                raise ContractStop(f"Sol ledger hash-chain failure at line {line_number}")
            previous = event["event_sha256"]
            raw.append(event)
        expected = {**self.registration, "previous_sha256": None,
                    "event_sha256": raw[0].get("event_sha256") if raw else None}
        if not raw or raw[0] != expected:
            raise ContractStop("Sol ledger registration mismatch")
        self._starts = {}
        self._finishes = {}
        histories = {}
        for event in raw[1:]:
            attempt = event.get("attempt_id")
            if type(attempt) is not int:
                raise ContractStop("invalid Sol attempt id")
            if event.get("event") == "attempt_started":
                required = {
                    "event", "attempt_id", "logical_key", "requested_model",
                    "payload_sha256", "schema_sha256", "replay",
                    "previous_sha256", "event_sha256",
                }
                if (set(event) != required or attempt != len(self._starts) + 1
                        or event.get("requested_model") != SOL_MODEL
                        or not _is_hash(event.get("payload_sha256"))
                        or not _is_hash(event.get("schema_sha256"))
                        or type(event.get("replay")) is not bool):
                    raise ContractStop("invalid persisted Sol start")
                history = histories.setdefault(event.get("logical_key"), [])
                if event["replay"] != bool(history) or len(history) >= 2:
                    raise ContractStop("invalid persisted Sol replay")
                if history:
                    prior = self._finishes.get(history[0])
                    first = self._starts[history[0]]
                    if (prior is None or prior["valid"]
                            or event["payload_sha256"] != first["payload_sha256"]
                            or event["schema_sha256"] != first["schema_sha256"]):
                        raise ContractStop("non-identical or premature Sol replay")
                self._starts[attempt] = event
                history.append(attempt)
            elif event.get("event") == "attempt_finished":
                required = {
                    "event", "attempt_id", "logical_key", "requested_model", "valid",
                    "error_class", "trace_sha256", "response_sha256", "cli_version",
                    "usage", "previous_sha256", "event_sha256",
                }
                start = self._starts.get(attempt)
                if (set(event) != required or start is None or attempt in self._finishes
                        or event["logical_key"] != start["logical_key"]
                        or event["requested_model"] != SOL_MODEL
                        or type(event["valid"]) is not bool
                        or (event["trace_sha256"] is not None
                            and not _is_hash(event["trace_sha256"]))
                        or (event["response_sha256"] is not None
                            and not _is_hash(event["response_sha256"]))
                        or not _valid_usage(event["usage"])):
                    raise ContractStop("invalid persisted Sol finish")
                if event["valid"] and event["error_class"] is not None:
                    raise ContractStop("invalid persisted Sol success")
                if not event["valid"] and not isinstance(event["error_class"], str):
                    raise ContractStop("invalid persisted Sol defect")
                self._finishes[attempt] = event
            else:
                raise ContractStop("unknown Sol ledger event")
        if len(self._starts) > self.max_attempts:
            raise ContractStop("persisted Sol attempt cap exceeded")
        if sum(start["replay"] for start in self._starts.values()) > self.replay_cap:
            raise ContractStop("persisted Sol replay cap exceeded")
        inflight = set(self._starts) - set(self._finishes)
        if len(inflight) > self.max_concurrency:
            raise ContractStop("persisted Sol concurrency exceeded")
        if inflight and not allow_inflight:
            raise ContractStop(f"unresolved in-flight Sol attempt(s): {sorted(inflight)}")
        self._last_hash = raw[-1]["event_sha256"]

    def _history(self, logical_key):
        return [attempt for attempt, start in sorted(self._starts.items())
                if start["logical_key"] == logical_key]

    def begin(self, logical_key, payload_sha256, schema_sha256):
        if not _is_hash(payload_sha256) or not _is_hash(schema_sha256):
            raise ContractStop("invalid Sol task hash")
        with _file_lock(self.lock_path):
            self._load(allow_inflight=True)
            history = self._history(logical_key)
            replay = bool(history)
            if history:
                prior = self._finishes.get(history[-1])
                first = self._starts[history[0]]
                if prior is None:
                    raise ThreadStop(f"Sol key already in flight: {logical_key}")
                if prior["valid"]:
                    raise ContractStop(f"duplicate completed Sol key: {logical_key}")
                if len(history) >= 2:
                    raise ThreadStop(f"Sol replay exhausted: {logical_key}")
                if (payload_sha256 != first["payload_sha256"]
                        or schema_sha256 != first["schema_sha256"]):
                    raise ContractStop("Sol replay must be exact")
                if sum(start["replay"] for start in self._starts.values()) >= self.replay_cap:
                    raise BudgetStop("Sol replay reserve exhausted")
            if len(self._starts) >= self.max_attempts:
                raise BudgetStop("Sol attempt cap exhausted")
            if len(self._starts) - len(self._finishes) >= self.max_concurrency:
                raise BudgetStop("Sol concurrency cap exhausted")
            attempt = len(self._starts) + 1
            event = {
                "event": "attempt_started", "attempt_id": attempt,
                "logical_key": logical_key, "requested_model": SOL_MODEL,
                "payload_sha256": payload_sha256, "schema_sha256": schema_sha256,
                "replay": replay,
            }
            stored = _append_event(self.path, event, self._last_hash)
            self._starts[attempt] = stored
            self._last_hash = stored["event_sha256"]
            return attempt

    def finish(self, attempt, *, valid, error_class=None, trace_sha256=None,
               response_sha256=None, cli_version="unknown", usage=None):
        usage = usage or {}
        if not _valid_usage(usage):
            raise ContractStop("invalid Sol usage custody")
        with _file_lock(self.lock_path):
            self._load(allow_inflight=True)
            start = self._starts.get(attempt)
            if start is None or attempt in self._finishes:
                raise ContractStop("unknown or duplicate Sol finish")
            if type(valid) is not bool:
                raise ContractStop("Sol validity must be boolean")
            event = {
                "event": "attempt_finished", "attempt_id": attempt,
                "logical_key": start["logical_key"], "requested_model": SOL_MODEL,
                "valid": valid, "error_class": None if valid else str(error_class),
                "trace_sha256": trace_sha256, "response_sha256": response_sha256,
                "cli_version": str(cli_version), "usage": usage,
            }
            stored = _append_event(self.path, event, self._last_hash)
            self._finishes[attempt] = stored
            self._last_hash = stored["event_sha256"]

    def snapshot(self):
        with _file_lock(self.lock_path):
            self._load(allow_inflight=True)
            return {
                "attempts": len(self._starts),
                "replays": sum(start["replay"] for start in self._starts.values()),
                "inflight": len(self._starts) - len(self._finishes),
            }


@dataclass(frozen=True)
class SolResult:
    value: dict
    prompt: str
    schema: dict
    final_text: str
    trace_jsonl: str
    cli_version: str
    usage: dict
    attempt_ids: tuple


def _strict_object(value, schema):
    if schema.get("type") != "object" or not isinstance(value, dict):
        return False
    properties = schema.get("properties", {})
    if schema.get("additionalProperties") is False and set(value) - set(properties):
        return False
    if not set(schema.get("required", ())).issubset(value):
        return False
    for key, rule in properties.items():
        if key not in value:
            continue
        if rule.get("type") == "string":
            if not isinstance(value[key], str) or (
                    "enum" in rule and value[key] not in rule["enum"]):
                return False
    return True


_USAGE_FIELDS = {
    "input_tokens", "output_tokens", "total_tokens", "cached_input_tokens",
    "reasoning_tokens",
}


def _valid_usage(usage):
    return (isinstance(usage, dict) and set(usage).issubset(_USAGE_FIELDS)
            and all(type(value) in (int, float) and not isinstance(value, bool)
                    and math.isfinite(value) and value >= 0
                    for value in usage.values()))


def _has_tool_type(value):
    if isinstance(value, dict):
        for key, nested in value.items():
            if (key in ("type", "name") and isinstance(nested, str)
                    and ("tool" in nested.lower()
                         or nested.lower() in ("command_execution", "web_search", "mcp"))):
                return True
            if _has_tool_type(nested):
                return True
    elif isinstance(value, list):
        return any(_has_tool_type(item) for item in value)
    return False


def _trace(trace_text):
    events = []
    for line in trace_text.splitlines():
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError("malformed_trace") from exc
        events.append(event)
        if _has_tool_type(event):
            raise PermissionError("tool_event")
    usage = {}
    for event in events:
        candidate = event.get("usage") if isinstance(event, dict) else None
        if isinstance(candidate, dict):
            usage = {key: value for key, value in candidate.items()
                     if key in _USAGE_FIELDS and type(value) in (int, float)
                     and not isinstance(value, bool) and math.isfinite(value)
                     and value >= 0}
    return usage


class SolExecClient:
    """Strict structured Sol executor using the frozen manifest templates."""

    def __init__(self, ledger: SolTaskLedger, *, runner=None, binary="codex",
                 timeout=600, cli_version=None):
        self.ledger = ledger
        self.runner = runner or subprocess.run
        self.binary = binary
        self.timeout = timeout
        self.cli_version = cli_version or self._detect_version()

    def _detect_version(self):  # pragma: no cover - live-only subprocess seam
        proc = subprocess.run(
            [self.binary, "--version"], capture_output=True, text=True, check=False)
        return (proc.stdout or proc.stderr or "unknown").strip()

    def _argv(self, schema_path, last_path):
        return [
            self.binary, "exec", "-m", SOL_MODEL,
            "-c", 'model_reasoning_effort="medium"',
            "--ignore-user-config", "--ignore-rules", "--ephemeral",
            "--skip-git-repo-check", "--sandbox", "read-only", "--json",
            "--output-schema", str(schema_path),
            "--output-last-message", str(last_path), "-",
        ]

    def run_json(self, logical_key, prompt, schema):
        payload_hash = _sha256_bytes(prompt.encode("utf-8"))
        schema_hash = _canonical_hash(schema)
        attempts = []
        for index in range(2):
            attempt = self.ledger.begin(logical_key, payload_hash, schema_hash)
            attempts.append(attempt)
            final_text = ""
            trace_text = ""
            usage = {}
            error = None
            with tempfile.TemporaryDirectory(prefix="walkworthy-open6-sol1-") as td:
                schema_path = Path(td) / "schema.json"
                last_path = Path(td) / "last-message.json"
                schema_path.write_bytes(canonical_json_bytes(schema))
                try:
                    proc = self.runner(
                        self._argv(schema_path, last_path),
                        input=prompt, text=True, capture_output=True,
                        cwd=td, timeout=self.timeout, check=False,
                    )
                    trace_text = getattr(proc, "stdout", "") or ""
                    if getattr(proc, "returncode", 1) != 0:
                        error = "cli_failure"
                    else:
                        try:
                            usage = _trace(trace_text)
                        except PermissionError:
                            error = "tool_event"
                        except ValueError:
                            error = "malformed_trace"
                        if last_path.exists():
                            final_text = last_path.read_text(encoding="utf-8").strip()
                        if error is None and not final_text:
                            error = "empty"
                        if error is None:
                            try:
                                value = json.loads(final_text)
                            except json.JSONDecodeError:
                                error = "malformed"
                            else:
                                if not _strict_object(value, schema):
                                    error = "schema_invalid"
                except (OSError, subprocess.TimeoutExpired):
                    error = "cli_failure"
            trace_hash = _sha256_bytes(trace_text.encode("utf-8"))
            response_hash = (_sha256_bytes(final_text.encode("utf-8"))
                             if final_text else None)
            self.ledger.finish(
                attempt, valid=error is None, error_class=error,
                trace_sha256=trace_hash, response_sha256=response_hash,
                cli_version=self.cli_version, usage=usage,
            )
            if error is None:
                return SolResult(
                    value=value, prompt=prompt, schema=schema,
                    final_text=final_text, trace_jsonl=trace_text,
                    cli_version=self.cli_version, usage=usage,
                    attempt_ids=tuple(attempts),
                )
            if index == 1:
                raise ThreadStop(f"Sol second failure for {logical_key}: {error}")
        raise AssertionError("unreachable")

    def classify_state(self, logical_key, design, opaque_key,
                       allowed_states, assistant_response):
        if (not allowed_states or len(set(allowed_states)) != len(allowed_states)
                or not all(isinstance(state, str) and state for state in allowed_states)):
            raise ContractStop("classifier states must be unique nonempty strings")
        contract = sol_runtime_contract()["classifier"]
        template = contract["prompt"]["user_template"]
        user = (template
                .replace("{{DESIGN}}", design)
                .replace("{{OPAQUE_KEY}}", opaque_key)
                .replace("{{ALLOWED_STATES_JSON}}", json.dumps(
                    list(allowed_states), ensure_ascii=False, separators=(",", ":")))
                .replace("{{ASSISTANT_RESPONSE_JSON}}", json.dumps(
                    assistant_response, ensure_ascii=False, separators=(",", ":"))))
        prompt = contract["prompt"]["system_text"] + "\n\n" + user
        schema = {
            "type": "object",
            "additionalProperties": False,
            "required": ["state"],
            "properties": {
                "state": {"type": "string", "enum": list(allowed_states)},
            },
        }
        return self.run_json(logical_key, prompt, schema)
