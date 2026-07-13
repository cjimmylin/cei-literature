"""Mechanical primitives for the ratified WALKWORTHY MVP-A1 pilot.

This module deliberately contains no import-time credential access. It pins the
public item surface and model contract, supplies the append-only paid-attempt ledger,
and provides a phase-separated live runner that reads credentials only after the
offline preflight and test gates have been completed by the operator.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Optional

from .clients import Message
from .executors import AdministrationResult, ItemExecution, TurnResult
from .judges import Judge, Verdict
from .loader import DESIGN_CODES, load_public_split
from .openrouter_backend import OpenRouterClient
from .run import _run_05_allocation, _serialize_administration, score_item


MANIFEST_SHA256 = "6874ae265588d3b10c6ef11c4b554e21e82c2f1e5d212f9e9254c150d2f40345"
HARD_NTE_USD = 5.0
MAX_ATTEMPTS = 1834
BASE_WORST_CALLS = 1667
RESERVE_CALLS = MAX_ATTEMPTS - BASE_WORST_CALLS
MVP_DISCLAIMER = (
    "Small exploratory panel; inexpensive, unvalidated judges; descriptive only; "
    "not release-grade evidence."
)

MVP_ITEM_IDS = (
    "WW-01-B03", "WW-01-D04", "WW-01-A01", "WW-01-A05", "WW-01-A05-P", "WW-01-B01",
    "WW-02-B03", "WW-02-C02", "WW-02-A02", "WW-02-A05", "WW-02-B02", "WW-02-B04",
    "WW-03-B03", "WW-03-B05", "WW-03-A01", "WW-03-A04", "WW-03-A05", "WW-03-B01",
    "WW-04-D01", "WW-04-D05", "WW-04-A03", "WW-04-A04", "WW-04-B01", "WW-04-B04",
    "WW-05-A01", "WW-05-C05", "WW-05-A03", "WW-05-B01", "WW-05-B02", "WW-05-B06",
    "WW-06-A05", "WW-06-D03", "WW-06-A01", "WW-06-A06", "WW-06-B02", "WW-06-B04",
    "WW-07-A02", "WW-07-C02", "WW-07-A03", "WW-07-B02", "WW-07-B04", "WW-07-C01",
    "WW-08-B02", "WW-08-D02", "WW-08-A02", "WW-08-A04", "WW-08-B01", "WW-08-B04",
    "WW-09-A04", "WW-09-A05", "WW-09-B01", "WW-09-B04", "WW-09-C01", "WW-09-C04",
    "WW-10-A05", "WW-10-B05", "WW-10-A01", "WW-10-A03", "WW-10-B01", "WW-10-B04",
)
MVP_IDS_BY_DESIGN = {
    design: tuple(item_id for item_id in MVP_ITEM_IDS
                  if item_id.startswith(f"WW-{design.split('-', 1)[0]}-"))
    for design in DESIGN_CODES
}


@dataclass(frozen=True)
class ModelSpec:
    """One exact MVP-A1 role/model price-and-cap contract."""

    slug: str
    role: str
    max_tokens: int
    input_per_m: float
    output_per_m: float
    input_envelope: int

    @property
    def max_call_usd(self) -> float:
        return (
            self.input_envelope * self.input_per_m
            + self.max_tokens * self.output_per_m
        ) / 1_000_000

    @property
    def provider_prefs(self) -> dict:
        return {
            "sort": "price",
            "require_parameters": True,
            "allow_fallbacks": True,
            "max_price": {
                "prompt": self.input_per_m,
                "completion": self.output_per_m,
            },
        }


SUT_SPECS = (
    ModelSpec("mistralai/mistral-small-3.2-24b-instruct", "sut", 2048,
              0.075, 0.20, 24_000),
    ModelSpec("google/gemini-2.5-flash-lite", "sut", 2048,
              0.10, 0.40, 24_000),
    ModelSpec("qwen/qwen3-8b", "sut", 2048,
              0.117, 0.455, 24_000),
)
JUDGE_SPECS = (
    ModelSpec("openai/gpt-4.1-nano", "judge", 256,
              0.10, 0.40, 24_000),
    ModelSpec("meta-llama/llama-3.3-70b-instruct", "judge", 256,
              0.10, 0.32, 24_000),
)
CLASSIFIER_SPEC = ModelSpec("openai/gpt-4.1-nano", "classifier", 16,
                            0.10, 0.40, 2_048)
ALL_MODEL_SPECS = SUT_SPECS + JUDGE_SPECS


def probe_spec(spec: ModelSpec) -> ModelSpec:
    """The one-call probe uses its separately authorized 256/1,024 envelope."""
    return ModelSpec(spec.slug, "probe", 256, spec.input_per_m,
                     spec.output_per_m, 1_024)


PROBE_SPECS = tuple(probe_spec(spec) for spec in ALL_MODEL_SPECS)
MVP_EXPECTED_KEYS = {
    (item_id, spec.slug) for spec in SUT_SPECS for item_id in MVP_ITEM_IDS
}

META_JUDGE_CALLS = 480
META_JUDGE_ENVELOPE_USD = JUDGE_SPECS[1].max_call_usd * META_JUDGE_CALLS
HIGHEST_DUPLICATE_CALL_USD = SUT_SPECS[2].max_call_usd
RESERVE_ENVELOPE_USD = RESERVE_CALLS * HIGHEST_DUPLICATE_CALL_USD


class BudgetStop(RuntimeError):
    """Raised before a request that would exceed the authorized call/cost surface."""


class ContractStop(RuntimeError):
    """Raised when persisted or requested state deviates from MVP-A1."""


class ProbeStop(RuntimeError):
    """Raised when one of the five registered reliability probes fails."""


def ordered_item_hash(items) -> str:
    payload = "".join(f"{item.id}\n" for item in items).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def select_mvp_items(benchmark_root) -> list:
    """Return the exact PUBLIC 2-easy + 4-hard surface in registered order."""
    all_items = load_public_split(
        benchmark_root, include_exemplars=True, runnable_only=True)
    selected = []
    for design in DESIGN_CODES:
        pool = sorted(
            (item for item in all_items if item.design == design),
            key=lambda item: item.id,
        )
        easy = [item for item in pool if item.difficulty == "easy"][:2]
        hard = [item for item in pool if item.difficulty == "hard"][:4]
        if len(easy) != 2 or len(hard) != 4:
            raise ValueError(
                f"MVP-A1 selector requires 2 easy + 4 hard for {design}; "
                f"found {len(easy)} easy + {len(hard)} hard")
        selected.extend(easy + hard)
    digest = ordered_item_hash(selected)
    if tuple(item.id for item in selected) != MVP_ITEM_IDS or digest != MANIFEST_SHA256:
        raise ValueError(
            f"MVP-A1 PUBLIC manifest mismatch: n={len(selected)} sha256={digest}")
    return selected


def _authorized_spec(spec: ModelSpec) -> bool:
    return spec in SUT_SPECS + JUDGE_SPECS + (CLASSIFIER_SPEC,) + PROBE_SPECS


def make_client(spec: ModelSpec, api_key: str, transport) -> OpenRouterClient:
    """Build one explicitly capped, price-sorted OpenRouter client."""
    if not _authorized_spec(spec):
        raise ContractStop(f"unauthorized MVP-A1 model spec: {spec}")
    return OpenRouterClient(
        spec.slug,
        model=spec.slug,
        api_key=api_key,
        transport=transport,
        max_tokens=spec.max_tokens,
        provider_prefs=spec.provider_prefs,
    )


def _append_jsonl(path: Path, event: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


class AttemptLedger:
    """Strict append-only begin/finish custody for every outbound HTTP attempt.

    Only a hash of the request payload is stored here.  Complete transcripts belong
    in the phase execution/verdict artifacts; authorization headers and prompts never
    enter this spend-control ledger.
    """

    def __init__(self, path, hard_nte_usd: float = HARD_NTE_USD,
                 max_attempts: int = MAX_ATTEMPTS):
        self.path = Path(path)
        self.hard_nte_usd = float(hard_nte_usd)
        self.max_attempts = int(max_attempts)
        if self.hard_nte_usd > HARD_NTE_USD + 1e-12:
            raise ValueError("MVP hard NTE cannot exceed authorized $5.00")
        if self.max_attempts > MAX_ATTEMPTS:
            raise ValueError("MVP call cap cannot exceed authorized 1,834")
        if self.hard_nte_usd <= 0 or self.max_attempts <= 0:
            raise ValueError("MVP caps must be positive")
        self._starts: dict[int, dict] = {}
        self._finishes: dict[int, dict] = {}
        self._load()

    def _load(self) -> None:
        if not self.path.exists():
            return
        for line_no, line in enumerate(
                self.path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"invalid MVP attempt ledger JSON at line {line_no}") from exc
            attempt_id = event.get("attempt_id")
            if not isinstance(attempt_id, int) or attempt_id < 1:
                raise ValueError(f"invalid MVP attempt id at line {line_no}")
            kind = event.get("event")
            if kind == "attempt_started":
                if attempt_id in self._starts:
                    raise ValueError(f"duplicate MVP attempt start: {attempt_id}")
                self._starts[attempt_id] = event
            elif kind == "attempt_finished":
                if attempt_id in self._finishes:
                    raise ValueError(f"duplicate MVP attempt finish: {attempt_id}")
                self._finishes[attempt_id] = event
            else:
                raise ValueError(f"unknown MVP attempt event at line {line_no}")
        if set(self._finishes) - set(self._starts):
            raise ValueError("MVP attempt finish without matching start")
        expected = set(range(1, len(self._starts) + 1))
        if set(self._starts) != expected:
            raise ValueError("MVP attempt ids are not contiguous")
        unresolved = sorted(set(self._starts) - set(self._finishes))
        if unresolved:
            raise ContractStop(f"MVP unresolved attempt(s) on resume: {unresolved}")
        for attempt_id in sorted(self._starts):
            self._validate_persisted_pair(
                self._starts[attempt_id], self._finishes[attempt_id])
        if self.actual_usd > self.hard_nte_usd + 1e-12:
            raise ContractStop("invalid persisted attempt ledger: spend exceeds hard NTE")

    @staticmethod
    def _role_spec(role: str, model: str) -> Optional[ModelSpec]:
        groups = {
            "probe": PROBE_SPECS,
            "sut": SUT_SPECS,
            "classifier": (CLASSIFIER_SPEC,),
            "judge": JUDGE_SPECS,
        }
        return next((spec for spec in groups.get(role, ()) if spec.slug == model), None)

    @classmethod
    def _validate_persisted_pair(cls, start: dict, finish: dict) -> None:
        start_fields = {
            "event", "attempt_id", "requested_model", "role", "max_call_usd",
            "payload_sha256",
        }
        finish_fields = {
            "event", "attempt_id", "requested_model", "returned_model", "role",
            "status", "actual_usd", "cost_basis", "prompt_tokens",
            "completion_tokens",
        }
        if set(start) != start_fields or set(finish) != finish_fields:
            raise ContractStop("invalid persisted attempt field set")
        if (finish["attempt_id"] != start["attempt_id"]
                or finish["requested_model"] != start["requested_model"]
                or finish["role"] != start["role"]):
            raise ContractStop("invalid persisted attempt identity")
        spec = cls._role_spec(start["role"], start["requested_model"])
        if spec is None:
            raise ContractStop("invalid persisted attempt model/role")
        max_call = start["max_call_usd"]
        if (not isinstance(max_call, (int, float)) or isinstance(max_call, bool)
                or not math.isfinite(float(max_call))
                or abs(float(max_call) - spec.max_call_usd) > 1e-12):
            raise ContractStop("invalid persisted attempt price envelope")
        payload_hash = start["payload_sha256"]
        if (not isinstance(payload_hash, str)
                or re.fullmatch(r"[0-9a-f]{64}", payload_hash) is None):
            raise ContractStop("invalid persisted attempt payload hash")
        status = finish["status"]
        if status is not None and (not isinstance(status, int) or isinstance(status, bool)
                                   or status < 100 or status > 599):
            raise ContractStop("invalid persisted attempt status")
        actual = finish["actual_usd"]
        if (not isinstance(actual, (int, float)) or isinstance(actual, bool)
                or not math.isfinite(float(actual)) or float(actual) < 0):
            raise ContractStop("invalid persisted attempt cost")
        for field in ("prompt_tokens", "completion_tokens"):
            value = finish[field]
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                raise ContractStop("invalid persisted attempt token count")
        returned = finish["returned_model"]
        if returned is not None and not isinstance(returned, str):
            raise ContractStop("invalid persisted attempt returned model")
        if status == 200:
            model_match = (
                isinstance(returned, str)
                and (returned == spec.slug or returned.startswith(spec.slug + "-"))
            )
            if not model_match:
                raise ContractStop("invalid persisted attempt returned model substitution")
        basis = finish["cost_basis"]
        if basis == "reported":
            return
        if (basis != "reserved_max_on_unknown_failure" or status == 200
                or abs(float(actual) - spec.max_call_usd) > 1e-12):
            raise ContractStop("invalid persisted attempt cost basis")

    @property
    def actual_usd(self) -> float:
        return sum(float(event.get("actual_usd") or 0.0)
                   for event in self._finishes.values())

    @property
    def unresolved_reserved_usd(self) -> float:
        unresolved = set(self._starts) - set(self._finishes)
        return sum(float(self._starts[attempt].get("max_call_usd") or 0.0)
                   for attempt in unresolved)

    def snapshot(self, attempt_limit: Optional[int] = None) -> dict:
        if attempt_limit is None:
            attempt_ids = set(self._starts)
        else:
            if (not isinstance(attempt_limit, int) or attempt_limit < 0
                    or attempt_limit > len(self._starts)):
                raise ContractStop("invalid persisted checkpoint attempt boundary")
            attempt_ids = {attempt for attempt in self._starts if attempt <= attempt_limit}
        finish_ids = attempt_ids & set(self._finishes)
        return {
            "attempts_started": len(attempt_ids),
            "completed_responses": len(finish_ids),
            "actual_usd": sum(float(self._finishes[attempt]["actual_usd"])
                              for attempt in finish_ids),
            "unresolved_reserved_usd": sum(
                float(self._starts[attempt]["max_call_usd"])
                for attempt in attempt_ids - finish_ids
            ),
            "unresolved_attempts": sorted(attempt_ids - finish_ids),
        }

    def starts_after(self, attempt_id: int) -> list:
        return [self._starts[index] for index in sorted(self._starts)
                if index > attempt_id]

    def finishes_after(self, attempt_id: int) -> list:
        return [self._finishes[index] for index in sorted(self._finishes)
                if index > attempt_id]

    def begin(self, model: str, role: str, max_call_usd: float,
              payload: dict) -> int:
        if len(self._starts) >= self.max_attempts:
            raise BudgetStop(
                f"MVP-A1 call envelope exhausted ({self.max_attempts} attempts)")
        if (self.actual_usd + self.unresolved_reserved_usd + float(max_call_usd)
                > self.hard_nte_usd + 1e-12):
            raise BudgetStop(
                f"MVP-A1 hard NTE ${self.hard_nte_usd:.2f} would be exceeded")
        attempt_id = len(self._starts) + 1
        payload_bytes = json.dumps(
            payload, ensure_ascii=False, sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
        event = {
            "event": "attempt_started",
            "attempt_id": attempt_id,
            "requested_model": model,
            "role": role,
            "max_call_usd": float(max_call_usd),
            "payload_sha256": hashlib.sha256(payload_bytes).hexdigest(),
        }
        _append_jsonl(self.path, event)
        self._starts[attempt_id] = event
        return attempt_id

    def finish(self, attempt_id: int, status: Optional[int], response: dict) -> None:
        if attempt_id not in self._starts:
            raise ValueError(f"unknown MVP attempt: {attempt_id}")
        if attempt_id in self._finishes:
            raise ValueError(f"MVP attempt already finished: {attempt_id}")
        start = self._starts[attempt_id]
        usage = response.get("usage") if isinstance(response, dict) else None
        usage = usage if isinstance(usage, dict) else {}
        raw_cost = usage.get("cost")
        if raw_cost is None:
            if status == 200:
                raise ContractStop("MVP response missing usage.cost")
            actual_usd = float(start["max_call_usd"])
            cost_basis = "reserved_max_on_unknown_failure"
        else:
            try:
                actual_usd = float(raw_cost)
            except (TypeError, ValueError) as exc:
                raise ContractStop("invalid MVP response usage.cost") from exc
            if not math.isfinite(actual_usd) or actual_usd < 0:
                raise ContractStop("invalid MVP response usage.cost")
            cost_basis = "reported"
        event = {
            "event": "attempt_finished",
            "attempt_id": attempt_id,
            "requested_model": start["requested_model"],
            "returned_model": (response.get("model")
                               if isinstance(response, dict) else None),
            "role": start["role"],
            "status": status,
            "actual_usd": actual_usd,
            "cost_basis": cost_basis,
            "prompt_tokens": int(usage.get("prompt_tokens") or 0),
            "completion_tokens": int(usage.get("completion_tokens") or 0),
        }
        _append_jsonl(self.path, event)
        self._finishes[attempt_id] = event


def guarded_transport(base_transport, ledger: AttemptLedger,
                      spec: ModelSpec, role: str):
    """Wrap an injected transport with pre-call authorization and custody."""
    def transport(url, headers, payload, timeout=None):
        if (payload.get("model") != spec.slug
                or payload.get("max_tokens") != spec.max_tokens
                or payload.get("provider") != spec.provider_prefs):
            raise ContractStop(f"MVP payload contract mismatch for {spec.slug}")
        attempt = ledger.begin(
            model=spec.slug, role=role,
            max_call_usd=spec.max_call_usd, payload=payload)
        try:
            status, response = base_transport(
                url, headers, payload, timeout=timeout)
        except Exception as exc:
            ledger.finish(attempt, None, {"error": type(exc).__name__, "usage": {}})
            raise
        ledger.finish(attempt, status, response)
        if status == 200:
            returned_model = response.get("model") if isinstance(response, dict) else None
            model_match = (
                isinstance(returned_model, str)
                and (returned_model == spec.slug
                     or returned_model.startswith(spec.slug + "-"))
            )
            if not model_match:
                raise ContractStop(
                    f"MVP returned model substitution for {spec.slug}: "
                    f"{returned_model!r}")
        return status, response
    return transport


def execution_to_dict(execution: ItemExecution) -> dict:
    return {
        "item_id": execution.item_id,
        "design": execution.design,
        "model": execution.model,
        "order": list(execution.order),
        "isolation_used": execution.isolation_used,
        "administrations": [
            _serialize_administration(admin)
            for admin in execution.administrations
        ],
    }


def execution_from_dict(data: dict) -> ItemExecution:
    admins = []
    for raw_admin in data.get("administrations") or []:
        admin = AdministrationResult(
            label=raw_admin.get("label"),
            kind=raw_admin.get("kind"),
            system=raw_admin.get("system"),
            terminal_response=raw_admin.get("terminal_response"),
            terminal_user_text=raw_admin.get("terminal_user_text"),
        )
        admin.turns = [
            TurnResult(
                index=turn.get("index"),
                user_text=turn.get("user_text"),
                response=turn.get("response"),
                branch_state=turn.get("branch_state"),
                refused_hint=bool(turn.get("refused_hint", False)),
            )
            for turn in raw_admin.get("turns") or []
        ]
        admins.append(admin)
    return ItemExecution(
        item_id=data.get("item_id"),
        design=data.get("design"),
        model=data.get("model"),
        order=list(data.get("order") or []),
        administrations=admins,
        isolation_used=bool(data.get("isolation_used", False)),
    )


def _model_row(spec: ModelSpec) -> dict:
    return {
        "slug": spec.slug,
        "role": spec.role,
        "family": spec.slug.split("/", 1)[0],
        "max_tokens": spec.max_tokens,
        "input_per_m": spec.input_per_m,
        "output_per_m": spec.output_per_m,
        "input_envelope": spec.input_envelope,
        "provider": spec.provider_prefs,
    }


def _write_or_validate_json(path, data: dict, label: str) -> dict:
    out = Path(path)
    # JSON object keys are strings on disk. Normalize before both comparison and
    # return so integer-keyed metric maps remain exactly resumable.
    normalized = json.loads(json.dumps(data, ensure_ascii=False, sort_keys=True))
    if out.exists():
        try:
            existing = json.loads(out.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ContractStop(f"{label} is invalid JSON") from exc
        if existing != normalized:
            raise ContractStop(f"MVP {label} mismatch; existing artifact is immutable")
        return existing
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(normalized, indent=2, ensure_ascii=False,
                                sort_keys=True) + "\n")
        handle.flush()
        os.fsync(handle.fileno())
    return normalized


def write_or_validate_manifest(path, benchmark_root) -> dict:
    items = select_mvp_items(benchmark_root)
    manifest = {
        "order": "MVP-A1",
        "authority": "00-PORTFOLIO/20260713-jimmy-mvp-a1-authorization.md",
        "scope": "PUBLIC-only descriptive MVP; never O5 evidence",
        "item_ids": [item.id for item in items],
        "ordered_item_sha256": ordered_item_hash(items),
        "suts": [_model_row(spec) for spec in SUT_SPECS],
        "judges": [_model_row(spec) for spec in JUDGE_SPECS],
        "classifier": _model_row(CLASSIFIER_SPEC),
        "probes": [_model_row(spec) for spec in PROBE_SPECS],
        "max_attempts": MAX_ATTEMPTS,
        "reserve_calls": RESERVE_CALLS,
        "hard_nte_usd": HARD_NTE_USD,
        "disclaimer": MVP_DISCLAIMER,
    }
    return _write_or_validate_json(path, manifest, "manifest")


def _read_jsonl_strict(path, label: str) -> list:
    source = Path(path)
    if not source.exists():
        return []
    rows = []
    for line_no, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ContractStop(f"invalid {label} JSON at line {line_no}") from exc
        if not isinstance(row, dict):
            raise ContractStop(f"invalid {label} row at line {line_no}")
        rows.append(row)
    return rows


def run_probes(path, clients_by_slug: dict) -> dict:
    """Run/resume one parse-checked probe for each of the five unique slugs."""
    from .live_judges import extract_json_object, parse_verdict
    from .rubrics import spec_for

    rows = _read_jsonl_strict(path, "probe ledger")
    by_model = {}
    expected = [spec.slug for spec in ALL_MODEL_SPECS]
    for row in rows:
        model = row.get("model")
        if model not in expected or model in by_model:
            raise ContractStop(f"invalid or duplicate MVP probe key: {model}")
        if not row.get("ok"):
            raise ProbeStop(f"MVP-A1 probe previously failed: {model}")
        by_model[model] = row

    for spec in ALL_MODEL_SPECS:
        if spec.slug in by_model:
            continue
        client = clients_by_slug.get(spec.slug)
        if client is None or getattr(client, "name", None) != spec.slug:
            raise ContractStop(f"missing exact MVP probe client: {spec.slug}")
        registered_probe = probe_spec(spec)
        if (getattr(client, "max_tokens", None) != registered_probe.max_tokens
                or getattr(client, "provider_prefs", None)
                != registered_probe.provider_prefs):
            raise ContractStop(f"MVP probe client contract mismatch: {spec.slug}")
        is_judge = spec in JUDGE_SPECS
        prompt = (
            'Return ONLY JSON: {"action_class":"partial",'
            '"rationale_quality":1,"classifier_state":"mutual"}'
            if is_judge else "Reply with a nonempty acknowledgement for MVP-A1."
        )
        try:
            response = client.complete([Message("user", prompt)])
            returned_family = getattr(response, "family", "")
            returned_model = getattr(response, "model", "")
            expected_family = spec.slug.split("/", 1)[0]
            model_match = (returned_model == spec.slug
                           or returned_model.startswith(spec.slug + "-"))
            ok = bool((response.text or "").strip() and model_match
                      and returned_family == expected_family)
            if is_judge:
                parsed = extract_json_object(response.text)
                scores, defects = parse_verdict(response.text, spec_for("01-goodsamaritan"))
                ok = bool(ok and parsed and not defects
                          and parsed.get("classifier_state") == "mutual"
                          and all(value is not None for value in scores.values()))
            if not ok:
                raise ValueError("nonempty/parse/model contract failed")
        except Exception as exc:
            failure = {"model": spec.slug, "ok": False,
                       "error_type": type(exc).__name__}
            _append_jsonl(Path(path), failure)
            raise ProbeStop(f"MVP-A1 probe failed for {spec.slug}") from exc
        row = {
            "model": spec.slug,
            "family": getattr(response, "family", spec.slug.split("/", 1)[0]),
            "returned_model": response.model,
            "ok": True,
            "response_sha256": hashlib.sha256(response.text.encode("utf-8")).hexdigest(),
        }
        _append_jsonl(Path(path), row)
        by_model[spec.slug] = row
    return {"complete": True, "models": expected}


def _validate_execution_record(record: dict) -> tuple[str, str]:
    key = (record.get("item_id"), record.get("model"))
    if key not in MVP_EXPECTED_KEYS:
        raise ContractStop(f"invalid MVP execution key: {key}")
    design = next(d for d, ids in MVP_IDS_BY_DESIGN.items() if key[0] in ids)
    if record.get("design") != design:
        raise ContractStop(f"MVP execution design mismatch: {key}")
    raw = record.get("execution")
    if not isinstance(raw, dict) or raw.get("item_id") != key[0] or raw.get("model") != key[1]:
        raise ContractStop(f"MVP execution identity mismatch: {key}")
    admins = raw.get("administrations") or []
    if not admins:
        raise ContractStop(f"MVP execution lacks administrations: {key}")
    for admin in admins:
        turns = admin.get("turns") or []
        if not turns or any(not (turn.get("response") or "").strip() for turn in turns):
            raise ContractStop(f"MVP execution transcript incomplete: {key}")
        if admin.get("terminal_user_text") and not (admin.get("terminal_response") or "").strip():
            raise ContractStop(f"MVP execution terminal incomplete: {key}")
    if design == "05-ordoamoris" and "allocation" not in record:
        raise ContractStop(f"MVP 05 execution lacks allocation: {key}")
    return key


def load_execution_records(path) -> list:
    rows = _read_jsonl_strict(path, "execution ledger")
    seen = set()
    for row in rows:
        key = _validate_execution_record(row)
        if key in seen:
            raise ContractStop(f"duplicate MVP execution key: {key}")
        seen.add(key)
    return rows


def run_sut_phase(benchmark_root, execution_path, spec: ModelSpec,
                  sut_client, state_classifier) -> dict:
    if spec not in SUT_SPECS or getattr(sut_client, "name", None) != spec.slug:
        raise ContractStop(f"unauthorized MVP SUT phase: {getattr(spec, 'slug', spec)}")
    items = select_mvp_items(benchmark_root)
    existing = load_execution_records(execution_path)
    done = {(row["item_id"], row["model"]) for row in existing}
    new = 0
    from .manifest import FIXED_PERMUTATION_SEEDS
    for item in items:
        key = (item.id, spec.slug)
        if key in done:
            continue
        allocation = None
        if item.design == "05-ordoamoris":
            allocation, _ = _run_05_allocation(item, sut_client)
        from .executors import execute_item
        execution = execute_item(item, sut_client, FIXED_PERMUTATION_SEEDS,
                                 state_classifier=state_classifier)
        row = {
            "item_id": item.id,
            "design": item.design,
            "model": spec.slug,
            "execution": execution_to_dict(execution),
        }
        if allocation is not None:
            row["allocation"] = allocation
        _validate_execution_record(row)
        _append_jsonl(Path(execution_path), row)
        done.add(key)
        new += 1
    complete = sum(1 for key in done if key[1] == spec.slug)
    return {"model": spec.slug, "complete": complete, "new": new}


def load_verdict_records(path) -> list:
    rows = _read_jsonl_strict(path, "verdict ledger")
    expected_judges = {spec.slug for spec in JUDGE_SPECS}
    seen = set()
    for row in rows:
        key = (row.get("item_id"), row.get("model"), row.get("judge"))
        if (key[:2] not in MVP_EXPECTED_KEYS or key[2] not in expected_judges
                or key in seen):
            raise ContractStop(f"invalid or duplicate MVP verdict key: {key}")
        verdict = row.get("verdict") or {}
        if verdict.get("judge") != key[2] or not verdict.get("unit"):
            raise ContractStop(f"MVP verdict identity mismatch: {key}")
        seen.add(key)
    return rows


def replay_path_for(verdict_path) -> Path:
    """Return PR-20's append-only replay ledger beside the base verdict ledger."""
    source = Path(verdict_path)
    return source.with_name(f"{source.stem}-replays{source.suffix}")


def _verdict_key(row: dict) -> tuple:
    return (row.get("item_id"), row.get("model"), row.get("judge"))


def load_replay_records(path, base_records: Optional[list] = None) -> list:
    """Validate the one-replay-per-defective-key PR-20 ledger."""
    rows = _read_jsonl_strict(path, "judge replay ledger")
    base_records = base_records if base_records is not None else []
    base = {_verdict_key(row): row for row in base_records}
    seen = set()
    for row in rows:
        key = _verdict_key(row)
        original = base.get(key)
        verdict = row.get("verdict") or {}
        if (original is None or not original.get("defects") or key in seen
                or row.get("replay_attempt") != 1
                or row.get("authority") != "PR-20 option 1"
                or verdict.get("judge") != key[2]
                or verdict.get("unit") != (original.get("verdict") or {}).get("unit")
                or row.get("call_units") != original.get("call_units")
                or int(row.get("replay_call_units") or 0) < 1):
            raise ContractStop(f"invalid or duplicate MVP judge replay key: {key}")
        replayed_units = row.get("replayed_units")
        if (not isinstance(replayed_units, list)
                or len(replayed_units) != row["replay_call_units"]
                or len(set(replayed_units)) != len(replayed_units)):
            raise ContractStop(f"invalid MVP judge replay units: {key}")
        seen.add(key)
    return rows


def load_resolved_verdict_records(verdict_path) -> list:
    """Resolve successful PR-20 replays without erasing the retained first defect."""
    base = load_verdict_records(verdict_path)
    replays = load_replay_records(replay_path_for(verdict_path), base)
    replay_by_key = {_verdict_key(row): row for row in replays}
    return [replay_by_key.get(_verdict_key(row), row) for row in base]


def _score_verdict_row(item, record: dict, spec: ModelSpec, judge: Judge,
                       scoring_spec) -> dict:
    execution = execution_from_dict(record["execution"])
    before_defects = len(getattr(judge, "defects", []))
    verdict = judge.score(item, execution, scoring_spec)
    defects = list(getattr(judge, "defects", []))[before_defects:]
    return {
        "item_id": record["item_id"],
        "design": record["design"],
        "model": record["model"],
        "judge": spec.slug,
        "call_units": len(verdict.per_unit) if verdict.per_unit else 1,
        "verdict": asdict(verdict),
        "defects": defects,
    }


def _replay_verdict_row(item, record: dict, spec: ModelSpec, judge: Judge,
                        scoring_spec, original: dict) -> dict:
    execution = execution_from_dict(record["execution"])
    prior = Verdict(**original["verdict"])
    before_defects = len(getattr(judge, "defects", []))
    replay_method = getattr(judge, "replay_defective_units", None)
    if callable(replay_method):
        verdict, replayed_units = replay_method(
            item, execution, scoring_spec, prior, list(original["defects"]))
    elif (scoring_spec.unit == "item"
          and {row.get("unit") for row in original["defects"]} <= {None, "item"}):
        verdict = judge.score(item, execution, scoring_spec)
        replayed_units = ["item"]
    else:
        raise ContractStop(
            f"MVP judge cannot replay exact malformed units for {_verdict_key(original)}")
    defects = list(getattr(judge, "defects", []))[before_defects:]
    return {
        "item_id": record["item_id"],
        "design": record["design"],
        "model": record["model"],
        "judge": spec.slug,
        "call_units": original["call_units"],
        "verdict": asdict(verdict),
        "defects": defects,
        "replay_attempt": 1,
        "replay_call_units": len(replayed_units),
        "replayed_units": replayed_units,
        "authority": "PR-20 option 1",
    }


def run_judge_phase(benchmark_root, execution_path, verdict_path,
                    spec: ModelSpec, judge: Judge) -> dict:
    if (spec not in JUDGE_SPECS or getattr(judge, "name", None) != spec.slug
            or getattr(judge, "family", None) != spec.slug.split("/", 1)[0]):
        raise ContractStop(f"unauthorized MVP judge phase: {getattr(spec, 'slug', spec)}")
    items = {item.id: item for item in select_mvp_items(benchmark_root)}
    executions = require_all_executions(execution_path)
    existing = load_verdict_records(verdict_path)
    replay_path = replay_path_for(verdict_path)
    replays = load_replay_records(replay_path, existing)
    replay_by_key = {_verdict_key(row): row for row in replays}
    exhausted = [row for row in replays
                 if row.get("judge") == spec.slug and row.get("defects")]
    if exhausted:
        raise ContractStop(
            f"MVP judge replay exhausted for {spec.slug}: {len(exhausted)}")
    existing_by_key = {_verdict_key(row): row for row in existing}
    resolved = load_resolved_verdict_records(verdict_path)
    done = {_verdict_key(row) for row in resolved if not row.get("defects")}
    new = 0
    from .rubrics import spec_for
    for record in executions:
        key = (record["item_id"], record["model"], spec.slug)
        if key in done:
            continue
        scoring_spec = spec_for(record["design"])
        original = existing_by_key.get(key)
        if original is None:
            original = _score_verdict_row(
                items[record["item_id"]], record, spec, judge, scoring_spec)
            _append_jsonl(Path(verdict_path), original)
            existing_by_key[key] = original
        if original.get("defects"):
            replay = replay_by_key.get(key)
            if replay is None:
                replay = _replay_verdict_row(
                    items[record["item_id"]], record, spec, judge,
                    scoring_spec, original)
                _append_jsonl(replay_path, replay)
                replay_by_key[key] = replay
            if replay.get("defects"):
                raise ContractStop(
                    f"MVP judge reliability failure for {spec.slug}: replay exhausted")
        done.add(key)
        new += 1
    complete = sum(1 for key in done if key[2] == spec.slug)
    return {"judge": spec.slug, "complete": complete, "new": new}


def require_all_executions(path) -> list:
    rows = load_execution_records(path)
    keys = {(row["item_id"], row["model"]) for row in rows}
    if keys != MVP_EXPECTED_KEYS or len(rows) != 180:
        raise ContractStop(
            f"MVP-A1 requires exact 180 executions; found {len(rows)}")
    return rows


class _ReplayJudge(Judge):
    def __init__(self, spec: ModelSpec, verdicts: dict):
        super().__init__(spec.slug, spec.slug.split("/", 1)[0])
        self._verdicts = verdicts

    def score(self, item, execution, spec):
        raw = self._verdicts[(item.id, execution.model, self.name)]
        return Verdict(**raw)


def _write_jsonl_once(path, rows: list, label: str) -> None:
    out = Path(path)
    payload = "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n"
                      for row in rows)
    if out.exists():
        if out.read_text(encoding="utf-8") != payload:
            raise ContractStop(f"MVP {label} mismatch; artifact is immutable")
        return
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("x", encoding="utf-8") as handle:
        handle.write(payload)
        handle.flush()
        os.fsync(handle.fileno())


def finalize_pilot(benchmark_root, execution_path, verdict_path,
                   scored_path, summary_path, runtime: Optional[dict] = None) -> dict:
    executions = require_all_executions(execution_path)
    base_verdict_rows = load_verdict_records(verdict_path)
    replay_rows = load_replay_records(
        replay_path_for(verdict_path), base_verdict_rows)
    verdict_rows = load_resolved_verdict_records(verdict_path)
    expected = {
        (item_id, sut.slug, judge.slug)
        for item_id in MVP_ITEM_IDS for sut in SUT_SPECS for judge in JUDGE_SPECS
    }
    verdict_map = {
        (row["item_id"], row["model"], row["judge"]): row["verdict"]
        for row in verdict_rows
    }
    if set(verdict_map) != expected or len(verdict_rows) != 360:
        raise ContractStop(
            f"MVP-A1 requires exact 360 cached verdicts; found {len(verdict_rows)}")
    for spec in JUDGE_SPECS:
        units = sum(int(row.get("call_units") or 0) for row in verdict_rows
                    if row["judge"] == spec.slug)
        if units != 480:
            raise ContractStop(
                f"MVP-A1 judge {spec.slug} requires exact 480 call units; found {units}")
    judge_defects = sum(len(row.get("defects") or []) for row in verdict_rows)
    if judge_defects:
        raise ContractStop(
            f"MVP-A1 validated completion refuses {judge_defects} judge defects")
    judges = [_ReplayJudge(spec, verdict_map) for spec in JUDGE_SPECS]
    items = {item.id: item for item in select_mvp_items(benchmark_root)}
    scored = []
    for record in executions:
        item = items[record["item_id"]]
        execution = execution_from_dict(record["execution"])
        scored.append(score_item(item, execution, judges,
                                 allocation=record.get("allocation")))
    _write_jsonl_once(scored_path, scored, "scored record")

    from . import metrics
    primary = {}
    for design in DESIGN_CODES:
        subset = [row for row in scored if row["design"] == design]
        primary[design] = metrics.serialize_design(
            metrics.compute_design(design, subset, items))
    schema_errors = sum(len(row.get("schema_errors") or []) for row in scored)
    summary = {
        "order": "MVP-A1",
        "complete": len(scored) == 180 and schema_errors == 0,
        "n_records": len(scored),
        "schema_errors": schema_errors,
        "coverage": coverage_table(executions),
        "primary_metrics": primary,
        "judge_units": {
            spec.slug: sum(row.get("call_units", 0) for row in verdict_rows
                           if row["judge"] == spec.slug)
            for spec in JUDGE_SPECS
        },
        "judge_defects": {
            spec.slug: sum(len(row.get("defects") or []) for row in verdict_rows
                           if row["judge"] == spec.slug)
            for spec in JUDGE_SPECS
        },
        "historical_judge_defects": {
            spec.slug: sum(len(row.get("defects") or []) for row in base_verdict_rows
                           if row["judge"] == spec.slug)
            for spec in JUDGE_SPECS
        },
        "judge_replays": {
            spec.slug: sum(int(row.get("replay_call_units") or 0)
                           for row in replay_rows if row["judge"] == spec.slug)
            for spec in JUDGE_SPECS
        },
        "disclaimer": MVP_DISCLAIMER,
    }
    if runtime:
        summary.update(runtime)
    _write_or_validate_json(summary_path, summary, "summary")
    return summary


def build_live_components(api_key: str, ledger: AttemptLedger, base_transport) -> dict:
    """Wire the exact role-specific clients without reading credentials implicitly."""
    from .live_judges import CLIJudge, make_cli_state_classifier
    from .references import bank_reference_provider

    probes = {}
    for base_spec, spec in zip(ALL_MODEL_SPECS, PROBE_SPECS):
        probes[base_spec.slug] = make_client(
            spec, api_key, guarded_transport(base_transport, ledger, spec, "probe"))
    suts = {
        spec.slug: make_client(
            spec, api_key, guarded_transport(base_transport, ledger, spec, "sut"))
        for spec in SUT_SPECS
    }
    classifier_client = make_client(
        CLASSIFIER_SPEC, api_key,
        guarded_transport(base_transport, ledger, CLASSIFIER_SPEC, "classifier"))
    classifier = make_cli_state_classifier(classifier_client)
    judges = {}
    for spec in JUDGE_SPECS:
        client = make_client(
            spec, api_key,
            guarded_transport(base_transport, ledger, spec, "judge"))
        judges[spec.slug] = CLIJudge(
            spec.slug, client, family=spec.slug.split("/", 1)[0],
            reference_provider=bank_reference_provider)
    return {"probes": probes, "suts": suts,
            "classifier": classifier, "judges": judges}


def _read_errors(path) -> list:
    return _read_jsonl_strict(path, "phase error ledger")


def _load_json_object(path, label: str) -> dict:
    source = Path(path)
    try:
        data = json.loads(source.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ContractStop(f"invalid or missing MVP {label}") from exc
    if not isinstance(data, dict):
        raise ContractStop(f"invalid MVP {label}")
    return data


class _LedgerSnapshotView:
    """Read-only ledger view used to reconstruct an immutable checkpoint boundary."""

    def __init__(self, ledger: AttemptLedger, snapshot: dict):
        self.hard_nte_usd = ledger.hard_nte_usd
        self.max_attempts = ledger.max_attempts
        self._snapshot = snapshot

    def snapshot(self) -> dict:
        return dict(self._snapshot)


def _validate_or_create_pre_meta_checkpoint(
        path, ledger: AttemptLedger, execution_records: list,
        verdict_records: list, probe_records: list, errors: list) -> dict:
    checkpoint_path = Path(path)
    if not checkpoint_path.exists():
        return write_pre_meta_checkpoint(
            checkpoint_path, ledger, execution_records, verdict_records,
            probe_records=probe_records, errors=errors,
        )

    existing = _load_json_object(checkpoint_path, "pre-Meta checkpoint")
    boundary = existing.get("attempts_started")
    prefix = ledger.snapshot(boundary)
    expected = _build_pre_meta_checkpoint(
        _LedgerSnapshotView(ledger, prefix), execution_records, verdict_records,
        probe_records=probe_records, errors=errors,
    )
    if existing != expected:
        raise ContractStop(
            "MVP pre-Meta checkpoint mismatch; persisted boundary is immutable")
    if not existing.get("continue_meta"):
        raise BudgetStop(
            "persisted MVP pre-Meta checkpoint does not authorize continuation")

    post_starts = ledger.starts_after(boundary)
    if any(row.get("role") != "judge"
           or row.get("requested_model") != JUDGE_SPECS[1].slug
           for row in post_starts):
        raise ContractStop("invalid paid attempt after MVP pre-Meta checkpoint")
    meta_rows = [row for row in verdict_records
                 if row.get("judge") == JUDGE_SPECS[1].slug]
    meta_units = sum(int(row.get("call_units") or 0) for row in meta_rows)
    if meta_units < 0 or meta_units > META_JUDGE_CALLS:
        raise ContractStop("invalid persisted Meta judge unit count")
    meta_defects = sum(len(row.get("defects") or []) for row in meta_rows)
    if meta_defects:
        raise ContractStop(
            f"MVP Meta reliability failure: {meta_defects} judge defects")
    remaining_units = META_JUDGE_CALLS - meta_units
    current = ledger.snapshot()
    available = ledger.max_attempts - current["attempts_started"]
    if available < remaining_units:
        raise BudgetStop("MVP reserve exhausted before remaining Meta judge units")
    reserve_used = max(
        0, current["attempts_started"] + remaining_units - BASE_WORST_CALLS)
    unused_reserve_calls = max(0, RESERVE_CALLS - reserve_used)
    projected = (
        current["actual_usd"]
        + remaining_units * JUDGE_SPECS[1].max_call_usd
        + unused_reserve_calls * HIGHEST_DUPLICATE_CALL_USD
    )
    if projected > ledger.hard_nte_usd + 1e-12:
        raise BudgetStop("MVP projected cap breach before remaining Meta judge units")
    return existing


def run_live(benchmark_root, out_dir, api_key: str, base_transport,
             phase: str = "all") -> dict:
    """Run/resume the exact probe -> SUT -> OpenAI -> checkpoint -> Meta order."""
    if phase not in {"all", "through-checkpoint", "finish"}:
        raise ValueError(f"unknown MVP phase: {phase}")
    root = Path(benchmark_root)
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    write_or_validate_manifest(out / "manifest.json", root)
    ledger = AttemptLedger(out / "attempts.jsonl")
    components = build_live_components(api_key, ledger, base_transport)

    probe_summary = run_probes(out / "probes.jsonl", components["probes"])
    for spec in SUT_SPECS:
        run_sut_phase(root, out / "executions.jsonl", spec,
                      components["suts"][spec.slug], components["classifier"])
    require_all_executions(out / "executions.jsonl")
    run_judge_phase(root, out / "executions.jsonl", out / "verdicts.jsonl",
                    JUDGE_SPECS[0], components["judges"][JUDGE_SPECS[0].slug])

    checkpoint = _validate_or_create_pre_meta_checkpoint(
        out / "pre_meta_checkpoint.json", ledger,
        load_execution_records(out / "executions.jsonl"),
        load_resolved_verdict_records(out / "verdicts.jsonl"),
        _read_jsonl_strict(out / "probes.jsonl", "probe ledger"),
        _read_errors(out / "phase_errors.jsonl"),
    )
    if not checkpoint["continue_meta"]:
        raise BudgetStop("MVP pre-Meta checkpoint failed")

    if phase == "through-checkpoint":
        return {"complete": False, "phase": "pre-meta-checkpoint",
                "checkpoint": checkpoint, "spend": ledger.snapshot(),
                "probe_summary": probe_summary}

    run_judge_phase(root, out / "executions.jsonl", out / "verdicts.jsonl",
                    JUDGE_SPECS[1], components["judges"][JUDGE_SPECS[1].slug])
    return finalize_pilot(
        root, out / "executions.jsonl", out / "verdicts.jsonl",
        out / "scored_items.jsonl", out / "summary.json",
        runtime={"spend": ledger.snapshot(), "probe_summary": probe_summary,
                 "pre_meta_checkpoint": checkpoint},
    )


def main(argv=None) -> int:
    """CLI entry point; `preflight` never reads the key or calls the network."""
    import argparse
    from . import openrouter_backend as orb

    parser = argparse.ArgumentParser(description="WALKWORTHY MVP-A1 exact paid runner")
    parser.add_argument("--benchmark-root", default=str(Path(__file__).resolve().parents[2]))
    parser.add_argument("--out", required=True)
    parser.add_argument("--phase", choices=["preflight", "through-checkpoint", "finish", "all"],
                        default="all")
    args = parser.parse_args(argv)
    if args.phase == "preflight":
        write_or_validate_manifest(Path(args.out) / "manifest.json", args.benchmark_root)
        print(f"[MVP-A1] preflight manifest -> {args.out}")
        return 0
    key = orb.load_openrouter_key()
    if not key:
        raise SystemExit("MVP-A1: no OpenRouter key available")
    result = run_live(args.benchmark_root, args.out, key, orb._default_transport,
                      phase=args.phase)
    print(json.dumps({"complete": result.get("complete"),
                      "phase": result.get("phase", "complete"),
                      "spend": result.get("spend", {})}, sort_keys=True))
    return 0


def coverage_table(records: list) -> list:
    """Return registered 6-cell completeness for all 10 design x 3 SUT rows."""
    keys: dict[tuple[str, str], set[str]] = {}
    seen = set()
    for record in records:
        execution_key = (record.get("item_id"), record.get("model"))
        if execution_key not in MVP_EXPECTED_KEYS or execution_key in seen:
            raise ContractStop(f"invalid or duplicate MVP execution key: {execution_key}")
        seen.add(execution_key)
        design = next(d for d, ids in MVP_IDS_BY_DESIGN.items()
                      if execution_key[0] in ids)
        if record.get("design") != design:
            raise ContractStop(f"MVP execution design mismatch: {execution_key}")
        key = (design, record.get("model"))
        keys.setdefault(key, set()).add(record.get("item_id"))
    rows = []
    for design in DESIGN_CODES:
        for spec in SUT_SPECS:
            complete = len(keys.get((design, spec.slug), set()) - {None})
            percent = 100.0 * complete / 6
            rows.append({
                "design": design,
                "model": spec.slug,
                "registered": 6,
                "complete": complete,
                "percent": percent,
                "status": "COMPLETE" if percent >= 90.0 else "INCOMPLETE",
            })
    return rows


def _build_pre_meta_checkpoint(ledger: AttemptLedger,
                               execution_records: list, verdict_records: list,
                               probe_records: Optional[list] = None,
                               errors: Optional[list] = None) -> dict:
    """Build the exact immutable checkpoint payload from one ledger snapshot."""
    snapshot = ledger.snapshot()
    probe_records = probe_records or []
    errors = errors or []
    reserve_used = max(
        0, snapshot["attempts_started"] + META_JUDGE_CALLS - BASE_WORST_CALLS)
    unused_reserve_calls = max(0, RESERVE_CALLS - reserve_used)
    unused_reserve = unused_reserve_calls * HIGHEST_DUPLICATE_CALL_USD
    projected = snapshot["actual_usd"] + META_JUDGE_ENVELOPE_USD + unused_reserve
    coverage = coverage_table(execution_records)
    probe_ok = ({row.get("model") for row in probe_records if row.get("ok")}
                == {spec.slug for spec in ALL_MODEL_SPECS}
                and len(probe_records) == 5)
    openai_units = sum(int(row.get("call_units") or 0) for row in verdict_records
                       if row.get("judge") == JUDGE_SPECS[0].slug)
    openai_defects = sum(
        len(row.get("defects") or []) for row in verdict_records
        if row.get("judge") == JUDGE_SPECS[0].slug
    )
    max_attempts = int(getattr(ledger, "max_attempts", MAX_ATTEMPTS))
    available_attempts = max_attempts - snapshot["attempts_started"]
    prerequisites = {
        "five_probes": probe_ok,
        "executions_180": (len(execution_records) == 180
                           and all(row["status"] == "COMPLETE" for row in coverage)),
        "openai_units_480": openai_units == 480,
        "openai_judge_defects_zero": openai_defects == 0,
        "no_unresolved_attempts": not snapshot.get("unresolved_attempts"),
        "no_errors": not errors,
        "remaining_call_capacity": available_attempts >= META_JUDGE_CALLS,
    }
    return {
        **snapshot,
        "coverage": coverage,
        "probe_models": sorted(row.get("model") for row in probe_records
                                if row.get("ok")),
        "openai_judge_units": openai_units,
        "openai_judge_defects": openai_defects,
        "errors": list(errors),
        "available_attempts": available_attempts,
        "prerequisites": prerequisites,
        "remaining_meta_envelope_usd": META_JUDGE_ENVELOPE_USD,
        "unused_reserve_calls": unused_reserve_calls,
        "unused_reserve_usd": unused_reserve,
        "projected_total_usd": projected,
        "hard_nte_usd": ledger.hard_nte_usd,
        "continue_meta": (all(prerequisites.values())
                          and projected <= ledger.hard_nte_usd + 1e-12),
    }


def write_pre_meta_checkpoint(path, ledger: AttemptLedger,
                              execution_records: list, verdict_records: list,
                              probe_records: Optional[list] = None,
                              errors: Optional[list] = None) -> dict:
    """Persist the mandatory checkpoint immediately before the Meta judge."""
    checkpoint = _build_pre_meta_checkpoint(
        ledger, execution_records, verdict_records,
        probe_records=probe_records, errors=errors,
    )
    return _write_or_validate_json(path, checkpoint, "pre-Meta checkpoint")


if __name__ == "__main__":
    raise SystemExit(main())
