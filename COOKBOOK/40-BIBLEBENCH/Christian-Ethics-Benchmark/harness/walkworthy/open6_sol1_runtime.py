"""Fail-closed, offline-testable runtime seams for OPEN6-SOL1.

This module owns attempt accounting and the single registered defect replay.  It
does not load credentials, select PUBLIC items, orchestrate the full surface, or
store response bodies in its ledgers.
"""

from __future__ import annotations

import fcntl
import copy
import hashlib
import json
import math
import os
import re
import subprocess
import tempfile
import threading
import urllib.error
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
    SOL_NOMINAL_TURNS,
    SOL_RESERVE_TURNS,
    _model_manifest,
    canonical_json_bytes,
    sol_runtime_contract,
)
from .openrouter_backend import OpenRouterClient


MAX_CONCURRENCY = 2
INPUT_ENVELOPE = 24_000
SOL_MODEL = "gpt-5.6-sol"
DISABLED_CODEX_FEATURES = (
    "shell_tool", "unified_exec", "apps", "enable_mcp_apps", "plugins",
    "plugin_sharing", "remote_plugin", "in_app_browser", "browser_use",
    "browser_use_external", "browser_use_full_cdp_access", "computer_use",
    "multi_agent", "multi_agent_v2", "enable_fanout", "image_generation",
    "workspace_dependencies", "tool_suggest", "tool_call_mcp_elicitation",
    "goals", "hooks", "artifact", "code_mode", "code_mode_only",
    "skill_mcp_dependency_install", "auth_elicitation",
    "request_permissions_tool", "shell_snapshot", "memories",
    "standalone_web_search",
)
DISABLED_CONTEXT_CONFIGS = (
    "skills.include_instructions=false",
    "skills.bundled.enabled=false",
    "skills.config=[]",
    "include_permissions_instructions=false",
    "include_apps_instructions=false",
    "include_collaboration_mode_instructions=false",
    "include_environment_context=false",
)
CODEX_ENV_WHITELIST = frozenset({
    "PATH", "HOME", "CODEX_HOME", "TMPDIR", "LANG", "LC_ALL",
    "SSL_CERT_FILE", "SSL_CERT_DIR",
})
SOL_FAILURES = frozenset({
    "cli_failure", "tool_event", "malformed_trace", "empty", "malformed",
    "schema_invalid", "interrupted", "custody_failure",
})
DEEPSEEK_EXCEPTION_MARKER_NAME = "deepseek-exception-authorization.json"
DEEPSEEK_EXCEPTION_MODEL = "deepseek/deepseek-v4-pro"
DEEPSEEK_EXCEPTION_LOGICAL_KEY = (
    "or:deepseek/deepseek-v4-pro:WW-01-A01:content:001")


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
        return self.max_call_usd_for_input(self.input_envelope)

    def max_call_usd_for_input(self, input_tokens: int) -> Decimal:
        if type(input_tokens) is not int or input_tokens < self.input_envelope:
            raise ContractStop("invalid registered input-token reservation")
        return (
            Decimal(input_tokens) * self.ceiling_input_per_m
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


def _load_deepseek_exception_marker(ledger_path: Path):
    path = ledger_path.parent / DEEPSEEK_EXCEPTION_MARKER_NAME
    if not path.exists():
        return None
    try:
        marker = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ContractStop("invalid DeepSeek exception marker") from exc
    required = {
        "schema_version", "pilot", "authorization_memo_sha256",
        "logical_key", "requested_model", "prior_attempt_ids",
        "prior_statuses", "payload_sha256", "ceiling_max_usd",
        "catalog_revalidation_logical_key",
        "catalog_revalidation_record_sha256", "maximum_additional_attempts",
    }
    if (not isinstance(marker, dict) or set(marker) != required
            or marker.get("schema_version")
            != "walkworthy.open6-sol1.deepseek-exception.v1"
            or marker.get("pilot") != "WALKWORTHY-OPEN6-SOL1"
            or marker.get("logical_key") != DEEPSEEK_EXCEPTION_LOGICAL_KEY
            or marker.get("requested_model") != DEEPSEEK_EXCEPTION_MODEL
            or marker.get("maximum_additional_attempts") != 1
            or not _is_hash(marker.get("authorization_memo_sha256"))
            or not _is_hash(marker.get("payload_sha256"))
            or not _is_hash(marker.get("catalog_revalidation_record_sha256"))
            or not isinstance(marker.get("ceiling_max_usd"), str)
            or re.fullmatch(r"catalog-revalidation:\d{6}",
                            marker.get("catalog_revalidation_logical_key", ""))
            is None
            or not isinstance(marker.get("prior_attempt_ids"), list)
            or len(marker["prior_attempt_ids"]) != 2
            or any(type(value) is not int or value < 1
                   for value in marker["prior_attempt_ids"])
            or marker.get("prior_statuses") != [404, 404]
            or path.read_bytes() != canonical_json_bytes(marker)):
        raise ContractStop("invalid DeepSeek exception marker")
    return marker


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
                 max_concurrency=MAX_CONCURRENCY,
                 _allow_inflight_on_open=False):
        self.path = Path(path)
        self.lock_path = Path(str(self.path) + ".lock")
        self.deepseek_exception = _load_deepseek_exception_marker(self.path)
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
            self._load(allow_inflight=_allow_inflight_on_open)

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
                    "payload_sha256", "reserved_input_tokens", "ceiling_max_usd", "replay",
                    "previous_sha256", "event_sha256",
                }
                spec = _SPECS.get(event.get("requested_model"))
                reserved_input = event.get("reserved_input_tokens")
                if (set(event) != required or event.get("role") != "sut"
                        or spec is None or type(reserved_input) is not int
                        or reserved_input < spec.input_envelope
                        or event.get("ceiling_max_usd")
                        != str(spec.max_call_usd_for_input(reserved_input))
                        or not isinstance(event.get("logical_key"), str)
                        or not event["logical_key"] or not _is_hash(event.get("payload_sha256"))
                        or type(event.get("replay")) is not bool
                        or attempt != len(self._starts) + 1):
                    raise ContractStop("invalid persisted OpenRouter start")
                history = histories.setdefault(event["logical_key"], [])
                if (event["replay"] != bool(history)
                        or len(history) >= self._maximum_history(
                            event["logical_key"])):
                    raise ContractStop("invalid persisted OpenRouter replay")
                if history:
                    prior = self._finishes.get(history[-1])
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
        if self.deepseek_exception is not None:
            history = histories.get(DEEPSEEK_EXCEPTION_LOGICAL_KEY, [])
            marker = self.deepseek_exception
            if (history[:2] != marker["prior_attempt_ids"]
                    or len(history) < 2 or len(history) > 3):
                raise ContractStop("DeepSeek exception prior-attempt mismatch")
            prior_starts = [self._starts[value] for value in history[:2]]
            prior_finishes = [self._finishes.get(value) for value in history[:2]]
            if (any(value is None for value in prior_finishes)
                    or [value["status"] for value in prior_finishes]
                    != marker["prior_statuses"]
                    or any(value["failure"] != "http_failure"
                           for value in prior_finishes)
                    or any(value["requested_model"] != marker["requested_model"]
                           or value["payload_sha256"] != marker["payload_sha256"]
                           or value["ceiling_max_usd"] != marker["ceiling_max_usd"]
                           for value in prior_starts)):
                raise ContractStop("DeepSeek exception evidence mismatch")
        self._last_hash = events[-1]["event_sha256"]

    def _maximum_history(self, logical_key):
        if (self.deepseek_exception is not None
                and logical_key == self.deepseek_exception["logical_key"]):
            return 3
        return 2

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
        if (event["cost_basis"] == "registered_max"
                and booked != Decimal(start["ceiling_max_usd"])):
            raise ContractStop("invalid persisted registered maximum")
        for field in ("prompt_tokens", "completion_tokens"):
            if type(event[field]) is not int or event[field] < 0:
                raise ContractStop("invalid persisted token custody")
        if event["failure"] not in (
                None, "http_failure", "empty", "malformed", "wrong_model",
                "missing_cost", "interrupted", "custody_failure"):
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

    def history(self, logical_key):
        with _file_lock(self.lock_path):
            self._load(allow_inflight=True)
            return tuple(self._history(logical_key))

    def remaining_attempts(self, logical_key):
        with _file_lock(self.lock_path):
            self._load(allow_inflight=True)
            return self._maximum_history(logical_key) - len(
                self._history(logical_key))

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
        payload_bytes = len(json.dumps(payload).encode("utf-8"))
        reserved_input_tokens = max(spec.input_envelope, payload_bytes)
        request_ceiling = spec.max_call_usd_for_input(reserved_input_tokens)
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
                if len(history) >= self._maximum_history(logical_key):
                    raise ThreadStop(f"OpenRouter replay exhausted: {logical_key}")
                if (digest != first["payload_sha256"]
                        or spec.slug != first["requested_model"]
                        or reserved_input_tokens != first["reserved_input_tokens"]
                        or str(request_ceiling) != first["ceiling_max_usd"]):
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
            if self._booked() + self._inflight() + request_ceiling > self.hard_nte_usd:
                raise BudgetStop("OpenRouter hard NTE reservation exceeded")
            attempt = len(self._starts) + 1
            event = {
                "event": "attempt_started", "attempt_id": attempt,
                "logical_key": logical_key, "role": "sut",
                "requested_model": spec.slug, "payload_sha256": digest,
                "reserved_input_tokens": reserved_input_tokens,
                "ceiling_max_usd": str(request_ceiling), "replay": replay,
            }
            stored = _append_event(self.path, event, self._last_hash)
            self._starts[attempt] = stored
            self._last_hash = stored["event_sha256"]
            return attempt

    def finish(self, attempt: int, status, body, *,
               failure_override=None, error_detail=None) -> Optional[str]:
        if failure_override not in (None, "custody_failure", "malformed"):
            raise ContractStop("invalid OpenRouter failure override")
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
            if failure_override is not None:
                failure = failure_override
            booked = cost if cost is not None else Decimal(start["ceiling_max_usd"])
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
                "error_sha256": (
                    _canonical_hash(error_detail)
                    if error_detail is not None
                    else (_canonical_hash(response.get("error"))
                          if response.get("error") is not None else None)
                ),
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

    @classmethod
    def recover_inflight(cls, path, **kwargs):
        """Explicitly close crash-stranded starts; ordinary construction stays strict."""
        ledger = cls(path, _allow_inflight_on_open=True, **kwargs)
        with _file_lock(ledger.lock_path):
            ledger._load(allow_inflight=True)
            for attempt in sorted(set(ledger._starts) - set(ledger._finishes)):
                start = ledger._starts[attempt]
                event = {
                    "event": "attempt_finished", "attempt_id": attempt,
                    "logical_key": start["logical_key"], "role": start["role"],
                    "requested_model": start["requested_model"], "status": None,
                    "returned_model": None,
                    "booked_usd": start["ceiling_max_usd"],
                    "cost_basis": "registered_max", "prompt_tokens": 0,
                    "completion_tokens": 0, "failure": "interrupted",
                    "error_sha256": _sha256_bytes(b"interrupted"),
                    "response_sha256": None,
                }
                stored = _append_event(ledger.path, event, ledger._last_hash)
                ledger._finishes[attempt] = stored
                ledger._last_hash = stored["event_sha256"]
            ledger._load(allow_inflight=False)
        return cls(path, **kwargs)

    def attempt_snapshot(self, attempt):
        with _file_lock(self.lock_path):
            self._load(allow_inflight=True)
            if attempt not in self._starts:
                raise ContractStop("unknown OpenRouter attempt")
            return {
                "start": dict(self._starts[attempt]),
                "finish": (dict(self._finishes[attempt])
                           if attempt in self._finishes else None),
            }

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
        self._transport_state = threading.local()

        def capturing_transport(url, headers, payload, timeout=None):
            status, body = transport(url, headers, payload, timeout=timeout)
            self._transport_state.last = {"status": status, "body": body}
            return status, body

        self.base_client = make_openrouter_client(spec, api_key, capturing_transport)

    def complete(self, logical_key: str, messages, system=None,
                 response_validator=None) -> OpenRouterRunResult:
        payload = self.base_client.build_payload(messages, system)
        attempt_ids = list(self.ledger.history(logical_key))
        remaining = self.ledger.remaining_attempts(logical_key)
        if remaining <= 0:
            raise ThreadStop(f"OpenRouter replay exhausted: {logical_key}")
        for index in range(remaining):
            attempt = self.ledger.begin(logical_key, self.spec, payload)
            attempt_ids.append(attempt)
            self._transport_state.last = {}
            response = None
            try:
                response = self.base_client.complete(messages, system=system)
            except ModelCallError:
                pass
            except (OSError, TimeoutError, urllib.error.URLError) as exc:
                # Full exception custody is returned to the caller sink; only hashes
                # enter the spend ledger.
                self._transport_state.last = {
                    "status": None,
                    "body": {
                        "error": {
                            "type": exc.__class__.__name__,
                            "message": str(exc),
                        },
                    },
                }
            captured = self._transport_state.last
            status = captured.get("status")
            body = copy.deepcopy(captured.get("body", {}))
            sink_error = None
            validation_error = None
            if self.response_sink is not None:
                try:
                    self.response_sink(copy.deepcopy({
                        "logical_key": logical_key,
                        "attempt_id": attempt,
                        "status": status,
                        "body": body,
                    }))
                except Exception as exc:
                    sink_error = {
                        "type": exc.__class__.__name__, "message": str(exc),
                    }
            if response_validator is not None and response is not None:
                try:
                    if response_validator(
                            copy.deepcopy(response), copy.deepcopy(body)) is not True:
                        validation_error = {"type": "response_validation_failed"}
                except Exception as exc:
                    validation_error = {
                        "type": exc.__class__.__name__, "message": str(exc),
                    }
            failure_override = (
                "custody_failure" if sink_error
                else ("malformed" if validation_error else None)
            )
            failure = self.ledger.finish(
                attempt, status, copy.deepcopy(body),
                failure_override=failure_override,
                error_detail=sink_error or validation_error,
            )
            if failure is None and response is not None:
                return OpenRouterRunResult(
                    response=response, body=copy.deepcopy(body), payload=payload,
                    attempt_ids=tuple(attempt_ids),
                )
            if index == remaining - 1:
                label = (
                    "exceptional" if (
                        logical_key == DEEPSEEK_EXCEPTION_LOGICAL_KEY
                        and len(attempt_ids) == 3)
                    else "second")
                raise ThreadStop(
                    f"OpenRouter {label} failure for {logical_key}: {failure}")
        raise ContractStop("invalid OpenRouter attempt-loop state")


class SolTaskLedger:
    """Hash-chained, body-free attempt ledger for Sol OAuth tasks."""

    def __init__(self, path, *, planned_cap=SOL_NOMINAL_TURNS,
                 max_attempts=SOL_HARD_TURN_CAP,
                 replay_cap=SOL_RESERVE_TURNS, max_concurrency=MAX_CONCURRENCY,
                 _allow_inflight_on_open=False):
        self.path = Path(path)
        self.lock_path = Path(str(self.path) + ".lock")
        self.planned_cap = int(planned_cap)
        self.max_attempts = int(max_attempts)
        self.replay_cap = int(replay_cap)
        self.max_concurrency = int(max_concurrency)
        if not (0 < self.max_attempts <= SOL_HARD_TURN_CAP):
            raise ContractStop("invalid Sol attempt cap")
        if not (0 < self.planned_cap <= SOL_NOMINAL_TURNS):
            raise ContractStop("invalid Sol planned cap")
        if not (0 <= self.replay_cap <= SOL_RESERVE_TURNS):
            raise ContractStop("invalid Sol replay cap")
        if not (1 <= self.max_concurrency <= MAX_CONCURRENCY):
            raise ContractStop("invalid Sol concurrency cap")
        self.registration = {
            "event": "ledger_registered", "ledger": "sol",
            "planned_cap": self.planned_cap, "max_attempts": self.max_attempts,
            "replay_cap": self.replay_cap,
            "max_concurrency": self.max_concurrency,
        }
        with _file_lock(self.lock_path):
            if not self.path.exists():
                _append_event(self.path, self.registration, None)
            self._load(allow_inflight=_allow_inflight_on_open)

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
                    "usage", "error_sha256", "previous_sha256", "event_sha256",
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
                        or (event["error_sha256"] is not None
                            and not _is_hash(event["error_sha256"]))
                        or not _valid_usage(event["usage"])):
                    raise ContractStop("invalid persisted Sol finish")
                if event["valid"] and event["error_class"] is not None:
                    raise ContractStop("invalid persisted Sol success")
                if not event["valid"] and event["error_class"] not in SOL_FAILURES:
                    raise ContractStop("invalid persisted Sol defect")
                self._finishes[attempt] = event
            else:
                raise ContractStop("unknown Sol ledger event")
        if len(self._starts) > self.max_attempts:
            raise ContractStop("persisted Sol attempt cap exceeded")
        if len({start["logical_key"] for start in self._starts.values()}) > self.planned_cap:
            raise ContractStop("persisted Sol planned cap exceeded")
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
            if (not history and len({start["logical_key"]
                                     for start in self._starts.values()})
                    >= self.planned_cap):
                raise BudgetStop("Sol planned call cap exhausted")
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
               response_sha256=None, error_sha256=None,
               cli_version="unknown", usage=None):
        usage = usage or {}
        if not _valid_usage(usage):
            raise ContractStop("invalid Sol usage custody")
        if not valid and error_class not in SOL_FAILURES:
            raise ContractStop("invalid Sol failure class")
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
                "error_sha256": error_sha256,
                "cli_version": str(cli_version), "usage": usage,
            }
            stored = _append_event(self.path, event, self._last_hash)
            self._finishes[attempt] = stored
            self._last_hash = stored["event_sha256"]

    @classmethod
    def recover_inflight(cls, path, **kwargs):
        """Explicitly close crash-stranded Sol tasks as invalid interrupted work."""
        ledger = cls(path, _allow_inflight_on_open=True, **kwargs)
        with _file_lock(ledger.lock_path):
            ledger._load(allow_inflight=True)
            for attempt in sorted(set(ledger._starts) - set(ledger._finishes)):
                start = ledger._starts[attempt]
                event = {
                    "event": "attempt_finished", "attempt_id": attempt,
                    "logical_key": start["logical_key"],
                    "requested_model": SOL_MODEL, "valid": False,
                    "error_class": "interrupted", "trace_sha256": None,
                    "response_sha256": None,
                    "error_sha256": _sha256_bytes(b"interrupted"),
                    "cli_version": "crash-recovery",
                    "usage": {},
                }
                stored = _append_event(ledger.path, event, ledger._last_hash)
                ledger._finishes[attempt] = stored
                ledger._last_hash = stored["event_sha256"]
            ledger._load(allow_inflight=False)
        return cls(path, **kwargs)

    def attempt_snapshot(self, attempt):
        with _file_lock(self.lock_path):
            self._load(allow_inflight=True)
            if attempt not in self._starts:
                raise ContractStop("unknown Sol attempt")
            return {
                "start": dict(self._starts[attempt]),
                "finish": (dict(self._finishes[attempt])
                           if attempt in self._finishes else None),
            }

    def snapshot(self):
        with _file_lock(self.lock_path):
            self._load(allow_inflight=True)
            return {
                "attempts": len(self._starts),
                "planned": len({start["logical_key"]
                                for start in self._starts.values()}),
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


def _exact_json_equal(left, right):
    return type(left) is type(right) and left == right


def validate_json_schema(value, schema):
    """Validate the deliberately small, registered JSON-Schema subset."""
    if not isinstance(schema, dict) or not isinstance(schema.get("type"), str):
        return False
    kind = schema["type"]
    type_keywords = {
        "object": {"type", "properties", "required", "additionalProperties",
                   "enum", "const"},
        "array": {"type", "items", "minItems", "maxItems", "enum", "const"},
        "string": {"type", "enum", "const"},
        "integer": {"type", "enum", "const", "minimum", "maximum"},
        "number": {"type", "enum", "const", "minimum", "maximum"},
        "boolean": {"type", "enum", "const"},
        "null": {"type", "enum", "const"},
    }
    if kind not in type_keywords or set(schema) - type_keywords[kind]:
        return False
    if "const" in schema and not _exact_json_equal(value, schema["const"]):
        return False
    if "enum" in schema:
        enum = schema["enum"]
        if (not isinstance(enum, list) or not enum
                or not any(_exact_json_equal(value, candidate) for candidate in enum)):
            return False

    if kind == "object":
        if not isinstance(value, dict):
            return False
        properties = schema.get("properties", {})
        required = schema.get("required", [])
        additional = schema.get("additionalProperties", True)
        if (not isinstance(properties, dict)
                or not isinstance(required, list)
                or not all(isinstance(key, str) and key in properties for key in required)
                or len(set(required)) != len(required)
                or type(additional) is not bool):
            return False
        if not additional and set(value) - set(properties):
            return False
        if not set(required).issubset(value):
            return False
        return all(
            key not in value or validate_json_schema(value[key], child_schema)
            for key, child_schema in properties.items()
        )
    if kind == "array":
        if not isinstance(value, list):
            return False
        items = schema.get("items")
        minimum = schema.get("minItems", 0)
        maximum = schema.get("maxItems")
        if (not isinstance(items, dict)
                or type(minimum) is not int or minimum < 0
                or (maximum is not None
                    and (type(maximum) is not int or maximum < minimum))
                or len(value) < minimum
                or (maximum is not None and len(value) > maximum)):
            return False
        return all(validate_json_schema(item, items) for item in value)
    if kind == "string":
        return isinstance(value, str)
    if kind in ("integer", "number"):
        minimum = schema.get("minimum")
        maximum = schema.get("maximum")
        for key, bound in (("minimum", minimum), ("maximum", maximum)):
            if (key in schema
                    and (type(bound) not in (int, float) or not math.isfinite(bound))):
                return False
        if minimum is not None and maximum is not None and minimum > maximum:
            return False
        if kind == "integer":
            valid_type = type(value) is int
        else:
            valid_type = type(value) in (int, float) and math.isfinite(value)
        return (valid_type
                and (minimum is None or value >= minimum)
                and (maximum is None or value <= maximum))
    if kind == "boolean":
        return type(value) is bool
    return value is None


def validate_batch_result(value, expected_unit_keys, score_schema):
    keys = tuple(expected_unit_keys)
    if (not keys or not all(isinstance(key, str) and key for key in keys)
            or len(set(keys)) != len(keys)):
        return False
    schema = {
        "type": "object", "additionalProperties": False,
        "required": ["verdicts"],
        "properties": {
            "verdicts": {
                "type": "array", "minItems": len(keys), "maxItems": len(keys),
                "items": {
                    "type": "object", "additionalProperties": False,
                    "required": ["unit_key", "scores"],
                    "properties": {
                        "unit_key": {"type": "string", "enum": list(keys)},
                        "scores": score_schema,
                    },
                },
            },
        },
    }
    if not validate_json_schema(value, schema):
        return False
    returned = [verdict["unit_key"] for verdict in value["verdicts"]]
    return len(set(returned)) == len(keys) and set(returned) == set(keys)


_USAGE_FIELDS = {
    "input_tokens", "output_tokens", "total_tokens", "cached_input_tokens",
    "reasoning_tokens",
}


def _valid_usage(usage):
    return (isinstance(usage, dict) and set(usage).issubset(_USAGE_FIELDS)
            and all(type(value) in (int, float) and not isinstance(value, bool)
                    and math.isfinite(value) and value >= 0
                    for value in usage.values()))


_BENIGN_TRACE_EVENTS = {"thread.started", "turn.started", "turn.completed"}
_ITEM_TRACE_EVENTS = {"item.started", "item.updated", "item.completed"}
_BENIGN_ITEM_TYPES = {"agent_message", "reasoning"}


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
        event_type = event.get("type") if isinstance(event, dict) else None
        if event_type in _BENIGN_TRACE_EVENTS:
            pass
        elif event_type in _ITEM_TRACE_EVENTS:
            item = event.get("item")
            if (not isinstance(item, dict)
                    or item.get("type") not in _BENIGN_ITEM_TYPES):
                raise PermissionError("tool_or_unknown_item_event")
        else:
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
                 timeout=600, cli_version=None, attempt_sink=None):
        self.ledger = ledger
        self.runner = runner or subprocess.run
        self.binary = binary
        self.timeout = timeout
        self.cli_version = cli_version or self._detect_version()
        self.attempt_sink = attempt_sink

    def _detect_version(self):  # pragma: no cover - live-only subprocess seam
        proc = subprocess.run(
            [self.binary, "--version"], capture_output=True, text=True, check=False)
        return (proc.stdout or proc.stderr or "unknown").strip()

    def _argv(self, schema_path, last_path):
        argv = [
            self.binary, "exec", "-m", SOL_MODEL,
            "-c", 'model_reasoning_effort="medium"',
        ]
        for feature in DISABLED_CODEX_FEATURES:
            argv.extend(("--disable", feature))
        for config in DISABLED_CONTEXT_CONFIGS:
            argv.extend(("-c", config))
        argv.extend([
            "--ignore-user-config", "--ignore-rules", "--ephemeral",
            "--skip-git-repo-check", "--sandbox", "read-only", "--json",
            "--output-schema", str(schema_path),
            "--output-last-message", str(last_path), "-",
        ])
        return argv

    def run_json(self, logical_key, prompt, schema, value_validator=None):
        payload_hash = _sha256_bytes(prompt.encode("utf-8"))
        schema_hash = _canonical_hash(schema)
        attempts = []
        for index in range(2):
            attempt = self.ledger.begin(logical_key, payload_hash, schema_hash)
            attempts.append(attempt)
            final_text = ""
            trace_text = ""
            stderr = ""
            returncode = None
            usage = {}
            error = None
            validation_error_detail = None
            value = None
            with tempfile.TemporaryDirectory(prefix="walkworthy-open6-sol1-") as td:
                schema_path = Path(td) / "schema.json"
                last_path = Path(td) / "last-message.json"
                schema_path.write_bytes(canonical_json_bytes(schema))
                try:
                    proc = self.runner(
                        self._argv(schema_path, last_path),
                        input=prompt, text=True, capture_output=True,
                        cwd=td, timeout=self.timeout, check=False,
                        env={key: os.environ[key] for key in CODEX_ENV_WHITELIST
                             if key in os.environ},
                    )
                    trace_text = getattr(proc, "stdout", "") or ""
                    stderr = getattr(proc, "stderr", "") or ""
                    returncode = getattr(proc, "returncode", 1)
                    if returncode != 0:
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
                                if not validate_json_schema(value, schema):
                                    error = "schema_invalid"
                                elif value_validator is not None:
                                    try:
                                        if value_validator(copy.deepcopy(value)) is not True:
                                            error = "schema_invalid"
                                            validation_error_detail = {
                                                "type": "value_validation_failed",
                                            }
                                    except Exception as exc:
                                        error = "schema_invalid"
                                        validation_error_detail = {
                                            "type": exc.__class__.__name__,
                                            "message": str(exc),
                                        }
                except (OSError, subprocess.TimeoutExpired):
                    error = "cli_failure"
            trace_hash = _sha256_bytes(trace_text.encode("utf-8"))
            response_hash = (_sha256_bytes(final_text.encode("utf-8"))
                             if final_text else None)
            sink_error = None
            if self.attempt_sink is not None:
                custody = {
                    "logical_key": logical_key, "attempt_id": attempt,
                    "prompt": prompt, "schema": schema, "final_text": final_text,
                    "trace_jsonl": trace_text, "stderr": stderr,
                    "returncode": returncode, "error_class": error,
                    "payload_sha256": payload_hash, "schema_sha256": schema_hash,
                    "trace_sha256": trace_hash, "response_sha256": response_hash,
                    "error_sha256": (_canonical_hash({"type": error})
                                     if error else None),
                    "cli_version": self.cli_version, "usage": usage,
                }
                try:
                    self.attempt_sink(copy.deepcopy(custody))
                except Exception as exc:
                    sink_error = {
                        "type": exc.__class__.__name__, "message": str(exc),
                    }
                    error = "custody_failure"
            error_detail = (sink_error or validation_error_detail
                            or ({"type": error} if error else None))
            self.ledger.finish(
                attempt, valid=error is None, error_class=error,
                trace_sha256=trace_hash, response_sha256=response_hash,
                error_sha256=(_canonical_hash(error_detail)
                              if error_detail is not None else None),
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
