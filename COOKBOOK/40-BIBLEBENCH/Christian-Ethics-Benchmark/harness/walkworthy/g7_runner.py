"""Offline custody primitives for the ratified WALKWORTHY G7-A1 run.

No orchestration or credential loading lives here.  Every POST must be represented by
an append-only start before transport and one finish after transport.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import re
import threading
from contextlib import contextmanager
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path

import fcntl

from .openrouter_backend import OpenRouterClient


PRODUCTION_MANIFEST_SHA256 = "616d2e93491adcb8da9fc00664693cd8c4685a95fc36b6fc09816c32414edf0e"
ROLE_MANIFEST_SHA256 = "013600bd2f1c34b7353319e98395aa8b1b5b921796d73a840e5ddc2138027480"
L7_INVENTORY_SHA256 = "73711dd6ae89989ae0dfdad67a7a9516b84518eff0366e30fa061c70496b70b0"
EXCLUSION_MANIFEST_SHA256 = "a6ebbe8f81f236033779c9d6113923ba7419de16e2d142ca622bc37c98fa0366"
PLANNED_LOGICAL_CALLS = 9709
REPLAY_RESERVE_CALLS = 971
MAX_POSTS = 10680
MAX_CONCURRENCY = 2
HARD_NTE_USD = Decimal("30.00")


class ContractStop(RuntimeError):
    """Persisted or requested work differs from the ratified contract."""


class BudgetStop(RuntimeError):
    """The next request would exceed a ratified count or spend cap."""


class ThreadStop(RuntimeError):
    """A logical key used its single replay without a valid response."""


@dataclass(frozen=True)
class RoleSpec:
    role: str
    slug: str
    max_tokens: int
    input_envelope: int
    input_per_m: Decimal
    output_per_m: Decimal
    max_missing_cost: Decimal

    @property
    def provider_prefs(self) -> dict:
        return {
            "sort": "price",
            "require_parameters": True,
            "allow_fallbacks": True,
            "max_price": {
                "prompt": float(self.input_per_m),
                "completion": float(self.output_per_m),
            },
        }


def _spec(role, slug, cap, envelope, input_rate, output_rate, maximum):
    return RoleSpec(role, slug, cap, envelope, Decimal(input_rate),
                    Decimal(output_rate), Decimal(maximum))


ROLE_SPECS = (
    _spec("sut", "openai/gpt-4.1", 32768, 24000, "2.00", "8.00", "0.310144000"),
    _spec("sut", "google/gemini-2.5-pro", 32768, 24000, "1.25", "10.00", "0.357680000"),
    _spec("sut", "anthropic/claude-sonnet-4", 32768, 24000, "3.00", "15.00", "0.563520000"),
    _spec("sut", "deepseek/deepseek-chat", 32768, 24000, "0.2002", "0.8001", "0.031022477"),
    _spec("sut", "mistralai/mistral-large-2512", 32768, 24000, "0.50", "1.50", "0.061152000"),
    _spec("sut", "meta-llama/llama-3.3-70b-instruct", 32768, 24000, "0.10", "0.32", "0.012885760"),
    _spec("judge", "openai/gpt-4.1-mini", 256, 24000, "0.40", "1.60", "0.010009600"),
    _spec("judge", "google/gemini-2.5-flash", 256, 24000, "0.30", "2.50", "0.007840000"),
    _spec("classifier", "openai/gpt-5.6-terra", 16, 2048, "2.50", "15.00", "0.005360000"),
    _spec("paraphrase_author", "mistralai/mistral-large-2512", 4096, 24000, "0.50", "1.50", "0.018144000"),
    _spec("tie_breaker", "mistralai/mistral-large-2512", 256, 24000, "0.50", "1.50", "0.012384000"),
)
_SPECS = {(spec.role, spec.slug): spec for spec in ROLE_SPECS}


def spec_for(role: str, slug: str) -> RoleSpec:
    try:
        return _SPECS[(role, slug)]
    except KeyError as exc:
        raise ContractStop(f"unauthorized G7 role/model: {role}/{slug}") from exc


def make_client(spec: RoleSpec, api_key: str, transport) -> OpenRouterClient:
    if _SPECS.get((spec.role, spec.slug)) != spec:
        raise ContractStop(f"unauthorized G7 role spec: {spec}")
    return OpenRouterClient(
        spec.slug, model=spec.slug, api_key=api_key, transport=transport,
        max_tokens=spec.max_tokens, provider_prefs=spec.provider_prefs,
        max_retries=0, empty_retries=0,
    )


def _append(path: Path, event: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, sort_keys=True, separators=(",", ":")) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def default_transport_request_bytes(payload: dict) -> bytes:
    """Return exactly the bytes OpenRouter's default transport sends."""
    return json.dumps(payload).encode("utf-8")


_LOCAL_LOCKS: dict[str, threading.RLock] = {}
_LOCAL_LOCKS_GUARD = threading.Lock()


def _local_lock(path: Path) -> threading.RLock:
    key = str(path.resolve())
    with _LOCAL_LOCKS_GUARD:
        return _LOCAL_LOCKS.setdefault(key, threading.RLock())


@contextmanager
def _exclusive_file_lock(lock_path: Path):
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with _local_lock(lock_path):
        with lock_path.open("a+", encoding="utf-8") as handle:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def conservative_input_bytes(payload: dict) -> int:
    """Conservative tokenizer-independent bound for request input.

    UTF-8 bytes in the default JSON encoding of messages/system are no fewer than
    content tokens for ordinary provider tokenizers, while also counting framing.
    """
    input_payload = {"messages": payload.get("messages")}
    if "system" in payload:
        input_payload["system"] = payload["system"]
    return len(json.dumps(input_payload).encode("utf-8"))


def _decimal(value) -> Decimal | None:
    if isinstance(value, bool) or not isinstance(value, (int, float, Decimal)):
        return None
    if isinstance(value, float) and not math.isfinite(value):
        return None
    try:
        result = Decimal(str(value))
    except InvalidOperation:
        return None
    return result if result.is_finite() and result >= 0 else None


class AttemptLedger:
    """Append-only exact-key, exact-payload attempt and conservative-cost ledger."""

    def __init__(self, path, expected_keys, *, hard_nte_usd=HARD_NTE_USD,
                 planned_cap=PLANNED_LOGICAL_CALLS,
                 replay_cap=REPLAY_RESERVE_CALLS, post_cap=MAX_POSTS,
                 max_concurrency=MAX_CONCURRENCY):
        self.path = Path(path)
        self.lock_path = Path(str(self.path) + ".lock")
        self.expected_keys = tuple(expected_keys)
        if len(set(self.expected_keys)) != len(self.expected_keys):
            raise ContractStop("duplicate expected logical key")
        self._expected = set(self.expected_keys)
        self.hard_nte_usd = Decimal(str(hard_nte_usd))
        self.planned_cap = int(planned_cap)
        self.replay_cap = int(replay_cap)
        self.post_cap = int(post_cap)
        self.max_concurrency = int(max_concurrency)
        if not (Decimal("0") < self.hard_nte_usd <= HARD_NTE_USD):
            raise ContractStop("invalid G7 hard NTE")
        if not (0 <= self.planned_cap <= PLANNED_LOGICAL_CALLS
                and 0 <= self.replay_cap <= REPLAY_RESERVE_CALLS
                and 0 <= self.post_cap <= MAX_POSTS):
            raise ContractStop("invalid G7 call caps")
        if not 1 <= self.max_concurrency <= MAX_CONCURRENCY:
            raise ContractStop("invalid G7 concurrency cap")
        self.registration = {
            "event": "ledger_registered",
            "expected_keys": list(self.expected_keys),
            "hard_nte_usd": str(self.hard_nte_usd),
            "planned_cap": self.planned_cap,
            "replay_cap": self.replay_cap,
            "post_cap": self.post_cap,
            "max_concurrency": self.max_concurrency,
        }
        self._starts: dict[int, dict] = {}
        self._finishes: dict[int, dict] = {}
        with self._locked():
            if self.path.exists():
                self._load()
            else:
                _append(self.path, self.registration)

    @contextmanager
    def _locked(self):
        with _exclusive_file_lock(self.lock_path):
            yield

    def _load(self) -> None:
        self._starts = {}
        self._finishes = {}
        histories: dict[str, list[int]] = {}
        saw_registration = False
        for line_number, line in enumerate(
                self.path.read_text(encoding="utf-8").splitlines(), 1):
            try:
                event = json.loads(line)
            except (json.JSONDecodeError, TypeError) as exc:
                raise ContractStop(f"invalid G7 ledger JSON line {line_number}") from exc
            kind = event.get("event") if isinstance(event, dict) else None
            if kind == "ledger_registered":
                if line_number != 1 or set(event) != set(self.registration):
                    raise ContractStop("invalid G7 registration contract")
                if event["expected_keys"] != self.registration["expected_keys"]:
                    raise ContractStop("G7 expected key set differs in registration contract")
                if event != self.registration:
                    raise ContractStop("invalid G7 registration contract")
                saw_registration = True
                continue
            if line_number == 1:
                raise ContractStop("G7 chronological violation: registration must be first")
            attempt = event.get("attempt_id") if isinstance(event, dict) else None
            if not isinstance(attempt, int) or isinstance(attempt, bool) or attempt < 1:
                raise ContractStop(f"invalid G7 attempt at line {line_number}")
            if kind == "attempt_started":
                if attempt in self._starts:
                    raise ContractStop(f"duplicate attempt event: {attempt}/attempt_started")
                if attempt != len(self._starts) + 1:
                    raise ContractStop("G7 chronological violation: noncontiguous start")
                self._validate_start(event)
                key = event["logical_key"]
                history = histories.setdefault(key, [])
                if history:
                    prior = history[-1]
                    if prior not in self._finishes or self._finishes[prior]["failure"] is None:
                        raise ContractStop("G7 chronological violation: replay before failure")
                    first = self._starts[history[0]]
                    if (event["payload_sha256"] != first["payload_sha256"]
                            or event["role"] != first["role"]
                            or event["requested_model"] != first["requested_model"]):
                        raise ContractStop("G7 replay is not identical")
                if len(history) >= 2:
                    raise ContractStop(f"too many G7 attempts for {key}")
                if len(self._starts) - len(self._finishes) >= self.max_concurrency:
                    raise ContractStop("persisted G7 in-flight concurrency exceeded")
                self._starts[attempt] = event
                history.append(attempt)
                continue
            if kind == "attempt_finished":
                if attempt not in self._starts or attempt in self._finishes:
                    raise ContractStop("G7 chronological violation: finish before/after start")
                self._validate_finish(self._starts[attempt], event)
                self._finishes[attempt] = event
                continue
            if kind not in ("attempt_started", "attempt_finished"):
                raise ContractStop(f"invalid G7 ledger event at line {line_number}")
        if not saw_registration:
            raise ContractStop("invalid G7 registration contract")
        self._validate_loaded()

    def _validate_start(self, start: dict) -> None:
        fields = {"event", "attempt_id", "logical_key", "role",
                  "requested_model", "max_call_usd", "payload_sha256"}
        key = start.get("logical_key")
        if set(start) != fields or key not in self._expected:
            raise ContractStop("invalid G7 start contract")
        spec = spec_for(start["role"], start["requested_model"])
        if (start["max_call_usd"] != str(spec.max_missing_cost)
                or not isinstance(start["payload_sha256"], str)
                or re.fullmatch(r"[0-9a-f]{64}", start["payload_sha256"]) is None):
            raise ContractStop("invalid G7 start contract")

    @staticmethod
    def _validate_finish(start: dict, finish: dict) -> None:
        fields = {"event", "attempt_id", "logical_key", "status",
                  "returned_model", "booked_usd", "cost_basis", "failure"}
        spec = spec_for(start["role"], start["requested_model"])
        status = finish.get("status")
        failure = finish.get("failure")
        returned = finish.get("returned_model")
        basis = finish.get("cost_basis")
        try:
            booked = Decimal(finish.get("booked_usd", ""))
        except InvalidOperation:
            booked = Decimal("NaN")
        valid_status = (status is None or (isinstance(status, int)
                        and not isinstance(status, bool) and 100 <= status <= 599))
        if (set(finish) != fields
                or finish.get("attempt_id") != start["attempt_id"]
                or finish.get("logical_key") != start["logical_key"]
                or not valid_status
                or (returned is not None and not isinstance(returned, str))
                or failure not in (None, "http_failure", "missing_cost",
                                   "model_or_cost", "malformed", "empty")
                or basis not in ("reported", "registered_max")
                or not booked.is_finite() or booked < 0):
            raise ContractStop("invalid G7 finish contract")
        if basis == "registered_max" and booked != spec.max_missing_cost:
            raise ContractStop("invalid G7 finish contract")
        combinations = {
            None: (status == 200 and returned == spec.slug and basis == "reported"
                   and booked <= spec.max_missing_cost),
            "http_failure": status is None or status != 200,
            "missing_cost": (status == 200 and returned == spec.slug
                             and basis == "registered_max"),
            "empty": (status == 200 and returned == spec.slug and basis == "reported"
                      and booked <= spec.max_missing_cost),
            "malformed": (status == 200 and returned == spec.slug
                          and basis == "reported" and booked <= spec.max_missing_cost),
            "model_or_cost": (status == 200 and
                              (returned != spec.slug or basis == "registered_max"
                               or booked > spec.max_missing_cost)),
        }
        if not combinations[failure]:
            raise ContractStop("invalid G7 finish contract")

    def _validate_loaded(self) -> None:
        if (self._planned_cached() > self.planned_cap
                or self._replay_cached() > self.replay_cap
                or len(self._starts) > self.post_cap):
            raise ContractStop("persisted G7 call cap exceeded")
        if (self._actual_cached() + self._reserved_cached() + self._inflight_cached()
                > self.hard_nte_usd):
            raise ContractStop("persisted G7 hard NTE exceeded")

    def _history(self, key: str) -> list[int]:
        return [attempt for attempt, start in sorted(self._starts.items())
                if start["logical_key"] == key]

    def _planned_cached(self) -> int:
        return len({start["logical_key"] for start in self._starts.values()})

    def _replay_cached(self) -> int:
        return len(self._starts) - self._planned_cached()

    def _actual_cached(self) -> Decimal:
        return sum((Decimal(finish["booked_usd"])
                    for finish in self._finishes.values()
                    if finish["cost_basis"] == "reported"), Decimal("0"))

    def _reserved_cached(self) -> Decimal:
        return sum((Decimal(finish["booked_usd"])
                    for finish in self._finishes.values()
                    if finish["cost_basis"] == "registered_max"), Decimal("0"))

    def _inflight_cached(self) -> Decimal:
        return sum((Decimal(start["max_call_usd"])
                    for attempt, start in self._starts.items()
                    if attempt not in self._finishes), Decimal("0"))

    def snapshot(self) -> dict:
        """Return one atomic, freshly reloaded accounting view."""
        with self._locked():
            self._load()
            return {
                "planned": self._planned_cached(),
                "replay": self._replay_cached(),
                "posts": len(self._starts),
                "actual": self._actual_cached(),
                "reserved": self._reserved_cached(),
                "inflight": self._inflight_cached(),
            }

    @property
    def planned_count(self) -> int:
        return self.snapshot()["planned"]

    @property
    def replay_count(self) -> int:
        return self.snapshot()["replay"]

    @property
    def actual_usd(self) -> Decimal:
        return self.snapshot()["actual"]

    @property
    def reserved_usd(self) -> Decimal:
        return self.snapshot()["reserved"]

    @property
    def inflight_usd(self) -> Decimal:
        return self.snapshot()["inflight"]

    def begin(self, logical_key: str, spec: RoleSpec, payload: dict) -> int:
        if not isinstance(payload, dict) or (
                payload.get("model") != spec.slug
                or payload.get("max_tokens") != spec.max_tokens
                or payload.get("provider") != spec.provider_prefs):
            raise ContractStop("G7 payload contract mismatch")
        if conservative_input_bytes(payload) > spec.input_envelope:
            raise ContractStop("G7 request exceeds conservative input envelope")
        request_bytes = default_transport_request_bytes(payload)
        digest = hashlib.sha256(request_bytes).hexdigest()
        with self._locked():
            self._load()
            return self._begin_locked(logical_key, spec, digest)

    def _begin_locked(self, logical_key: str, spec: RoleSpec, digest: str) -> int:
        if logical_key not in self._expected:
            raise ContractStop(f"unregistered logical key: {logical_key}")
        if _SPECS.get((spec.role, spec.slug)) != spec:
            raise ContractStop("unauthorized G7 role spec")
        history = self._history(logical_key)
        if history:
            last_finish = self._finishes.get(history[-1])
            if last_finish is None:
                raise ThreadStop(f"G7 key already in flight: {logical_key}")
            if last_finish["failure"] is None:
                raise ContractStop(f"duplicate completed key: {logical_key}")
            if len(history) >= 2:
                raise ThreadStop(f"G7 replay exhausted for {logical_key}")
            first = self._starts[history[0]]
            if (digest != first["payload_sha256"] or spec.role != first["role"]
                    or spec.slug != first["requested_model"]):
                raise ContractStop("G7 replay requires identical payload/model/role")
            if self._replay_cached() >= self.replay_cap:
                raise BudgetStop("G7 replay reserve exhausted")
        elif self._planned_cached() >= self.planned_cap:
            raise BudgetStop("G7 planned logical call cap exhausted")
        if len(self._starts) >= self.post_cap:
            raise BudgetStop("G7 POST cap exhausted")
        if len(self._starts) - len(self._finishes) >= self.max_concurrency:
            raise BudgetStop("G7 in-flight concurrency cap exhausted")
        projected = (self._actual_cached() + self._reserved_cached()
                     + self._inflight_cached()
                     + spec.max_missing_cost)
        if projected > self.hard_nte_usd:
            raise BudgetStop("G7 hard NTE would be exceeded")
        attempt = len(self._starts) + 1
        event = {
            "event": "attempt_started", "attempt_id": attempt,
            "logical_key": logical_key, "role": spec.role,
            "requested_model": spec.slug,
            "max_call_usd": str(spec.max_missing_cost),
            "payload_sha256": digest,
        }
        _append(self.path, event)
        self._starts[attempt] = event
        return attempt

    def finish(self, attempt: int, status, response) -> str:
        with self._locked():
            self._load()
            return self._finish_locked(attempt, status, response)

    def _finish_locked(self, attempt: int, status, response) -> str:
        if attempt not in self._starts:
            raise ContractStop(f"unknown G7 attempt: {attempt}")
        if attempt in self._finishes:
            raise ContractStop(f"duplicate G7 finish: {attempt}")
        start = self._starts[attempt]
        spec = spec_for(start["role"], start["requested_model"])
        body = response if isinstance(response, dict) else {}
        usage = body.get("usage") if isinstance(body.get("usage"), dict) else {}
        raw_cost = usage.get("cost")
        reported = _decimal(raw_cost)
        returned_model = body.get("model")
        choices = body.get("choices")
        content = None
        if isinstance(choices, list) and choices and isinstance(choices[0], dict):
            message = choices[0].get("message")
            if isinstance(message, dict):
                content = message.get("content")
        if status != 200:
            failure = "http_failure"
        elif returned_model != spec.slug or reported is None:
            failure = "missing_cost" if returned_model == spec.slug and raw_cost is None else "model_or_cost"
        elif reported > spec.max_missing_cost:
            failure = "model_or_cost"
        elif not isinstance(content, str):
            failure = "malformed"
        elif not content.strip():
            failure = "empty"
        else:
            failure = None
        booked = reported if reported is not None else spec.max_missing_cost
        event = {
            "event": "attempt_finished", "attempt_id": attempt,
            "logical_key": start["logical_key"], "status": status,
            "returned_model": returned_model if isinstance(returned_model, str) else None,
            "booked_usd": str(booked),
            "cost_basis": "reported" if reported is not None else "registered_max",
            "failure": failure,
        }
        self._validate_finish(start, event)
        _append(self.path, event)
        self._finishes[attempt] = event
        if (self._actual_cached() + self._reserved_cached() + self._inflight_cached()
                > self.hard_nte_usd):
            raise BudgetStop("G7 hard NTE exceeded after reported cost custody")
        if failure is not None and len(self._history(start["logical_key"])) >= 2:
            raise ThreadStop(f"G7 second failure for {start['logical_key']}")
        return "complete" if failure is None else "replay_required"


def write_once_json(path, payload: dict) -> dict:
    """Create an immutable manifest/checkpoint, or validate an identical prior file."""
    path = Path(path)
    with _exclusive_file_lock(Path(str(path) + ".lock")):
        if path.exists():
            try:
                existing = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                raise ContractStop(f"invalid immutable JSON: {path}") from exc
            if existing != payload:
                raise ContractStop(f"immutable JSON differs: {path}")
            return existing
        with path.open("x", encoding="utf-8") as handle:
            json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
    return payload
