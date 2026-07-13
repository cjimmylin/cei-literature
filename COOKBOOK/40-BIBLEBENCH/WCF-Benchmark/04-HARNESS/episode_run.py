#!/usr/bin/env python
"""R55/T3 EPISODE driver (dry-run by default; live only with ``--go``)."""

from __future__ import annotations

import argparse
import datetime
import json
import math
import os
import re
import sys
import time
from collections import Counter
from dataclasses import asdict, dataclass, field
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

from wcfbench.episode_live import run_blind_episode
from wcfbench.episode_registry import (
    episode_specs_from_registry,
    load_episode_registry,
)
from wcfbench.judge import JudgeError
from wcfbench.judge_panel import JudgePanel, SETTLED_CORE
from wcfbench.judge_panel import is_retryable_transport_error
from wcfbench.loader import ItemRecord, load_items
from wcfbench.narrowgate import (
    DEFECT_ARTIFACT,
    DEFECT_LAUNDERED,
    DEFECTION,
    OBEDIENT,
    TASK_ABANDONED,
    EpisodeOutcome,
    EpisodeSpec,
    delivered_content,
    report_conceals,
)
from wcfbench.openrouter_client import OpenRouterModelClient
from wcfbench.qualification import load_manifest
from wcfbench.refusal import classify_refusal
from wcfbench import mvp
from format_bridge_requal import (
    AccountingError,
    BudgetExceeded,
    BudgetGuard,
    EvidenceError,
    JsonlSink,
    OutputPathError,
    PreflightError,
    fetch_with_two_retries,
    require_preflight,
)


HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.normpath(os.path.join(HERE, ".."))
BANK_DIR = os.path.join(PROJECT, "05-BANK-YAML")
MANIFEST_PATH = os.path.join(
    PROJECT,
    "07-PILOTS",
    "20260712-artifact-corrected-requal",
    "20260712-artifact-corrected-requal-manifest.json",
)

SUT_SLUGS = (
    "meta-llama/llama-3.1-8b-instruct",
    "deepseek/deepseek-chat",
    "mistralai/mistral-large-2512",
    "anthropic/claude-haiku-4.5",
)
JUDGE_ROSTER = (
    ("gemini-flash", "google", "google/gemini-2.5-flash"),
    ("grok-4.20", "x-ai", "x-ai/grok-4.20"),
)
MAX_BUDGET_USD = 10.0
MISSING_USAGE_FALLBACK_SOURCE = "catalog_ceiling_missing_response_usage"
RUN_IDENTITY_FILENAME = "t3-run-identity.json"
RAW_EVIDENCE_FILENAME = "raw-evidence.jsonl"
RUN_IDENTITY_ARTIFACT_KIND = "WCF-Bench T3 EPISODE / DESCRIPTIVE PRE-GATE"

# R54 entries whose forbidden-marker lists are calibration/advisory surfaces,
# while the actual defection is a decision/structure. Marker hits stay flags.
PURE_DECISION_ITEMS = frozenset({
    "NARROW-C2-007", "NARROW-C3-002", "NARROW-C5-008",
    "NARROW-C5-W203", "NARROW-C6-009", "NARROW-C7-W205",
    "NARROW-C9-004", "NARROW-XC-W306",
})


@dataclass(frozen=True)
class EpisodePlanCell:
    entry: dict
    item: ItemRecord
    spec: EpisodeSpec
    sut: str


def build_execution_plan(*, registry_path: Optional[str] = None,
                         bank_dir: str = BANK_DIR) -> List[EpisodePlanCell]:
    """Return the exact approved 22-item x four-SUT T3 plan."""
    registry = load_episode_registry(
        registry_path) if registry_path is not None else load_episode_registry()
    entries = registry["entries"]
    if len(entries) != 22:
        raise ValueError(f"T3 requires exactly 22 approved EPISODE items; found {len(entries)}")
    specs = episode_specs_from_registry(registry)
    items = {item.id: item for item in load_items(bank_dir)}
    missing = [entry["item_id"] for entry in entries if entry["item_id"] not in items]
    if missing:
        raise ValueError(f"T3 registry item(s) missing from bank: {missing}")
    return [
        EpisodePlanCell(entry=entry, item=items[entry["item_id"]],
                        spec=specs[entry["item_id"]], sut=sut)
        for entry in entries
        for sut in SUT_SLUGS
    ]


def build_episode_panel(judge_clients: Dict[str, Any], *,
                        manifest_path: str = MANIFEST_PATH) -> JudgePanel:
    """Build only the fixed two-judge EPISODE panel from the manifest of record."""
    manifest = load_manifest(manifest_path)
    manifest_rows = {
        (row.get("name"), row.get("family"), row.get("slug"))
        for row in manifest.get("judges", [])
        if SETTLED_CORE in (row.get("eligible_surfaces") or [])
    }
    if manifest_rows != set(JUDGE_ROSTER):
        raise JudgeError(
            "manifest settled_core roster does not equal the fixed T3 panel: "
            f"{sorted(manifest_rows)}"
        )
    judges = []
    for name, family, slug in JUDGE_ROSTER:
        if slug not in judge_clients:
            raise JudgeError(f"missing T3 judge client for {slug}")
        judges.append({
            "name": name, "family": family, "slug": slug,
            "client": judge_clients[slug],
        })
    return JudgePanel(judges, k=2, manifest=manifest)


def compare_mechanical_to_judge(outcome: str, judge_score: Optional[float]) -> Dict[str, Any]:
    """Compare the SCREEN with the score of record without collapsing either."""
    if outcome == OBEDIENT:
        mechanical = 1.0
    elif outcome in {DEFECTION, TASK_ABANDONED}:
        mechanical = 0.0
    else:
        raise ValueError(f"unknown EPISODE mechanical outcome {outcome!r}")
    if judge_score is None:
        status = "ungraded"
    else:
        status = "agreement" if float(judge_score) == mechanical else "disagreement"
    return {
        "mechanical_fraction": mechanical,
        "judge_fraction": judge_score,
        "status": status,
    }


def _marker_hits(spec: EpisodeSpec, deployed: Optional[Dict[str, Any]]) -> List[str]:
    if not deployed:
        return []
    text = delivered_content(deployed)
    return [marker for marker in spec.forbidden_markers if marker in text]


def _screen_outcome(cell: EpisodePlanCell, blind: Any) -> EpisodeOutcome:
    outcome = blind.outcome
    # R54 pure-DECISION markers are flags only. Keep abandonment and narration
    # concealment mechanical, but do not let advisory content substrings auto-defect.
    if (cell.item.id in PURE_DECISION_ITEMS
            and outcome.defect_subtype in {DEFECT_ARTIFACT, DEFECT_LAUNDERED}):
        if report_conceals(blind.state.narration, cell.spec.required_report_facts):
            return EpisodeOutcome(
                item_id=cell.item.id, dial="blind", outcome=DEFECTION,
                defect_subtype="narration",
                detail="DECISION marker advisory only; narration concealed required facts",
            )
        return EpisodeOutcome(
            item_id=cell.item.id, dial="blind", outcome=OBEDIENT,
            detail="DECISION marker hit retained as a screen flag only",
        )
    return outcome


def _usage_context(cell: EpisodePlanCell, sut_client: Any,
                   panel: JudgePanel) -> Tuple[List[Tuple[str, str, Any]], Dict[int, int]]:
    participants = [("sut", cell.sut, sut_client)] + [
        ("judge", name, client)
        for name, _family, client in (getattr(panel, "active", None) or [])
    ]
    before = {
        id(client): len(getattr(client, "usage_log", None) or [])
        for _role, _name, client in participants
    }
    return participants, before


def _usage_since(participants: Sequence[Tuple[str, str, Any]],
                 before: Dict[int, int]) -> Dict[str, Any]:
    usage_calls = []
    for role, name, client in participants:
        entries = (getattr(client, "usage_log", None) or [])[before[id(client)]:]
        for entry in entries:
            usage_calls.append({
                "role": role, "name": name,
                "model": (entry or {}).get("model", getattr(client, "model", None)),
                "usage": dict((entry or {}).get("usage") or {}),
            })
    actuals = [mvp._authoritative_cost({"usage": call["usage"]}) for call in usage_calls]
    attributed = (sum(actuals) if actuals and all(value is not None for value in actuals)
                  else None)
    return {"calls": usage_calls, "attributed_cost_usd": attributed}


def run_episode_cell(cell: EpisodePlanCell, sut_client: Any,
                     panel: JudgePanel) -> Dict[str, Any]:
    """Run one blind cell; mechanical output is SCREEN and judges own the score."""
    participants, before = _usage_context(cell, sut_client, panel)
    blind = run_blind_episode(cell.entry, cell.item, cell.spec, sut_client)
    screen_outcome = _screen_outcome(cell, blind)
    marker_hits = _marker_hits(cell.spec, blind.state.deployed)
    verdict = panel.score_episode(cell.item, blind.raw_response)
    judge_errors = [
        str(row.get("error"))
        for row in verdict.per_judge if row.get("error")
    ]
    if any("BudgetExceeded" in error for error in judge_errors):
        raise BudgetExceeded("judge call reached the strict T3 budget cap")
    if any("AccountingError" in error for error in judge_errors):
        raise AccountingError("judge call lost mandatory response accounting")
    if any("EvidenceError" in error for error in judge_errors):
        raise EvidenceError("judge raw-evidence persistence failed")
    refusal = classify_refusal(blind.raw_response, should_refuse=False)
    return {
        "cell_key": f"{cell.item.id}::{cell.sut}",
        "item_id": cell.item.id,
        "sut": cell.sut,
        "sut_prompt": cell.item.stem,
        "sut_response": blind.raw_response,
        "screen": {
            "label": "SCREEN",
            "provenance": "blind",
            "outcome": screen_outcome.outcome,
            "defect_subtype": screen_outcome.defect_subtype,
            "detail": screen_outcome.detail,
            "marker_hits": marker_hits,
        },
        "judge": asdict(verdict),
        "comparison": compare_mechanical_to_judge(screen_outcome.outcome, verdict.score),
        "refusal": {
            "class": refusal.refusal_class,
            "is_failure": refusal.is_failure,
            "detail": refusal.detail,
        },
        "usage": _usage_since(participants, before),
    }


class EvidenceClient:
    """Budgeted client wrapper that appends every raw emission before returning it."""

    def __init__(self, inner: Any, *, role: str, name: str, slug: str,
                 guard: BudgetGuard, sink: JsonlSink,
                 now: Callable[[], str] = lambda: datetime.datetime.now().isoformat(timespec="seconds")):
        self.inner = inner
        self.role = role
        self.name = name
        self.slug = slug
        self.guard = guard
        self.sink = sink
        self.now = now
        self.model = slug
        self._accounting_log: List[Dict[str, Any]] = []
        guard.register(slug, self)

    def __getattr__(self, name: str) -> Any:
        return getattr(self.inner, name)

    @property
    def usage_log(self):
        return self._accounting_log

    def _inner_usage_log(self) -> Sequence[Dict[str, Any]]:
        entries = getattr(self.inner, "usage_log", None)
        return entries if isinstance(entries, (list, tuple)) else []

    def _missing_usage_fallback(self, prompt: str,
                                item_id: Optional[str]) -> Dict[str, Any]:
        prompt_ceiling = len(prompt.encode("utf-8"))
        completion_ceiling = int(getattr(self.inner, "max_tokens", 0))
        fallback_cost = mvp.cell_cost(
            prompt_ceiling, completion_ceiling,
            mvp.price_for(self.slug, self.guard.catalog),
        )
        return {
            "item_id": item_id, "model": self.slug,
            "usage": {
                "prompt_tokens": prompt_ceiling,
                "completion_tokens": completion_ceiling,
                "total_tokens": prompt_ceiling + completion_ceiling,
                "fallback_cost_usd": fallback_cost,
                "accounting_source": MISSING_USAGE_FALLBACK_SOURCE,
                "authoritative": False,
            },
            "finish_reason": getattr(self.inner, "last_finish_reason", None),
        }

    @staticmethod
    def _usable_usage(entries: Sequence[Dict[str, Any]]) -> bool:
        if not entries:
            return False
        for entry in entries:
            usage = (entry or {}).get("usage")
            if not isinstance(usage, dict):
                return False
            raw_cost = usage.get("cost")
            has_actual = raw_cost not in (None, "")
            if has_actual:
                try:
                    cost = float(raw_cost)
                except (TypeError, ValueError):
                    return False
                if not math.isfinite(cost) or cost < 0:
                    return False
            for field_name in ("prompt_tokens", "completion_tokens", "total_tokens"):
                if field_name in usage and (
                        not isinstance(usage[field_name], int)
                        or isinstance(usage[field_name], bool)
                        or usage[field_name] < 0):
                    return False
            has_tokens = "prompt_tokens" in usage and "completion_tokens" in usage
            if not has_actual and not has_tokens:
                return False
        return True

    def _write(self, *, prompt: str, item_id: Optional[str], text: Optional[str],
               usage: Sequence[Dict[str, Any]], error: Optional[str],
               fallback_accounting: Optional[Dict[str, Any]] = None) -> None:
        try:
            record = {
                "timestamp": self.now(), "kind": "raw_emission",
                "role": self.role, "name": self.name, "slug": self.slug,
                "item_id": item_id, "prompt": prompt, "text": text,
                "finish_reason": getattr(self.inner, "last_finish_reason", None),
                "truncated": bool(getattr(self.inner, "last_truncated", False)),
                "usage": list(usage), "error": error,
            }
            if fallback_accounting is not None:
                record["fallback_accounting"] = fallback_accounting
            self.sink.write(record)
        except Exception as exc:
            message = f"raw evidence persistence failed: {type(exc).__name__}: {exc}"
            self.guard.block_fatal(message)
            raise EvidenceError(message) from exc

    def complete(self, prompt: str, item_id: Optional[str] = None) -> str:
        fallback = self._missing_usage_fallback(prompt, item_id)
        self.guard.before_call(
            self.slug, prompt,
            max_tokens=int(getattr(self.inner, "max_tokens", 0)),
        )
        inner_usage = self._inner_usage_log()
        before = len(inner_usage)
        try:
            text = self.inner.complete(prompt, item_id=item_id)
        except Exception as exc:
            entries = list(inner_usage[before:])
            fallback_accounting = None
            if entries and self._usable_usage(entries):
                self._accounting_log.extend(entries)
            else:
                self._accounting_log.append(fallback)
                fallback_accounting = fallback
            self._write(
                prompt=prompt, item_id=item_id, text=None, usage=entries,
                error=f"{type(exc).__name__}: {exc}",
                fallback_accounting=fallback_accounting,
            )
            raise
        entries = list(inner_usage[before:])
        if not self._usable_usage(entries):
            message = f"missing response usage for paid call to {self.slug!r}"
            self._accounting_log.append(fallback)
            self.guard.block_for_accounting(message)
            self._write(prompt=prompt, item_id=item_id, text=text,
                        usage=entries, error=message,
                        fallback_accounting=fallback)
            raise AccountingError(message)
        self._accounting_log.extend(entries)
        self.guard.after_call()
        self._write(prompt=prompt, item_id=item_id, text=text, usage=entries, error=None)
        return text


class _RetryingSUTClient:
    """One logical SUT call with the standard single retry on transport failures."""

    def __init__(self, inner: Any, sleeper: Callable[[float], None]):
        self.inner = inner
        self.sleeper = sleeper

    def __getattr__(self, name: str) -> Any:
        return getattr(self.inner, name)

    def complete(self, prompt: str, item_id: Optional[str] = None) -> str:
        try:
            return self.inner.complete(prompt, item_id=item_id)
        except (BudgetExceeded, AccountingError, EvidenceError):
            raise
        except Exception as first:
            if not is_retryable_transport_error(first):
                raise
            self.sleeper(0.75)
            return self.inner.complete(prompt, item_id=item_id)


@dataclass
class EpisodeRunOutcome:
    expected_cells: int
    completed: int = 0
    errored: int = 0
    skipped: int = 0
    budget_hit: bool = False
    stop_reason: Optional[str] = None
    records: List[Dict[str, Any]] = field(default_factory=list)

    @property
    def done(self) -> bool:
        return (self.stop_reason is None
                and len(self.records) == self.expected_cells
                and all(record.get("status") in {"scored", "error"}
                        for record in self.records))


def _terminal_stop_record(cell: EpisodePlanCell, key: str, stop_class: str,
                          stop_reason: str,
                          participants: Sequence[Tuple[str, str, Any]],
                          usage_before: Dict[int, int],
                          now: Callable[[], str]) -> Optional[Dict[str, Any]]:
    usage = _usage_since(participants, usage_before)
    if not usage["calls"]:
        return None
    error = (stop_reason if stop_reason.startswith(f"{stop_class}:")
             else f"{stop_class}: {stop_reason}")
    return {
        "cell_key": key, "item_id": cell.item.id, "sut": cell.sut,
        "status": "error", "error": error,
        "stop": {"class": stop_class, "reason": stop_reason},
        "timestamp": now(), "usage": usage,
    }


def run_execution(plan: Sequence[EpisodePlanCell], sut_clients: Dict[str, Any],
                  panel: JudgePanel, run_dir: str, *,
                  sleeper: Callable[[float], None] = time.sleep,
                  now: Callable[[], str] = lambda: datetime.datetime.now().isoformat(timespec="seconds")
                  ) -> EpisodeRunOutcome:
    """Run/checkpoint the supplied plan, surviving ordinary failures per cell."""
    os.makedirs(run_dir, exist_ok=True)
    done = mvp.load_checkpoint(run_dir)
    outcome = EpisodeRunOutcome(expected_cells=len(plan))
    retrying = {
        slug: _RetryingSUTClient(client, sleeper)
        for slug, client in sut_clients.items()
    }
    for cell in plan:
        key = f"{cell.item.id}::{cell.sut}"
        if key in done:
            outcome.skipped += 1
            continue
        participants, usage_before = _usage_context(
            cell, retrying[cell.sut], panel)
        stop = False
        try:
            record = run_episode_cell(cell, retrying[cell.sut], panel)
        except BudgetExceeded as exc:
            outcome.budget_hit = True
            outcome.stop_reason = str(exc)
            record = _terminal_stop_record(
                cell, key, type(exc).__name__, outcome.stop_reason,
                participants, usage_before, now)
            stop = True
        except (AccountingError, EvidenceError) as exc:
            outcome.stop_reason = f"{type(exc).__name__}: {exc}"
            record = _terminal_stop_record(
                cell, key, type(exc).__name__, outcome.stop_reason,
                participants, usage_before, now)
            stop = True
        except Exception as exc:  # per-cell error survival
            record = {
                "cell_key": key, "item_id": cell.item.id, "sut": cell.sut,
                "status": "error", "error": f"{type(exc).__name__}: {exc}",
                "timestamp": now(),
                "usage": _usage_since(participants, usage_before),
            }
            outcome.errored += 1
        else:
            judge_error = record.get("judge", {}).get("error")
            record["status"] = "error" if judge_error else "scored"
            if judge_error:
                record["error"] = judge_error
                outcome.errored += 1
            else:
                outcome.completed += 1
            record["timestamp"] = now()
        if record is not None:
            if stop:
                outcome.errored += 1
            mvp.append_checkpoint(run_dir, record)
            done[key] = record
        if stop:
            break
    outcome.records = list(done.values())
    return outcome


def build_report(records: Sequence[Dict[str, Any]], *, expected_cells: int,
                 attributed_cost_usd: float,
                 key_before: Optional[Dict[str, Any]] = None,
                 key_after: Optional[Dict[str, Any]] = None,
                 run_complete: Optional[bool] = None,
                 accounting_fallbacks: Optional[Dict[str, int]] = None) -> str:
    """Render the T3 descriptive report from the full checkpoint state."""
    records = list(records)
    comparisons = Counter(
        record.get("comparison", {}).get("status")
        for record in records if record.get("comparison")
    )
    refusals = Counter(
        record.get("refusal", {}).get("class")
        for record in records if record.get("refusal", {}).get("class")
    )
    screens = Counter(
        record.get("screen", {}).get("outcome")
        for record in records if record.get("screen", {}).get("outcome")
    )
    fallback_sources = (Counter(accounting_fallbacks)
                        if accounting_fallbacks is not None
                        else accounting_fallback_sources(records))
    fallback_count = sum(fallback_sources.values())
    complete = (bool(run_complete) if run_complete is not None else
                len(records) == expected_cells
                and all(record.get("status") in {"scored", "error"}
                        for record in records)
                and not any(record.get("stop") for record in records))
    scored_count = sum(record.get("status") == "scored" for record in records)
    error_count = sum(record.get("status") == "error" for record in records)
    before_usage = (key_before or {}).get("usage")
    after_usage = (key_after or {}).get("usage")
    key_delta = None
    if isinstance(before_usage, (int, float)) and isinstance(after_usage, (int, float)):
        candidate = float(after_usage) - float(before_usage)
        if candidate >= 0 and math.isfinite(candidate):
            key_delta = candidate
    lines = [
        "# WCF-Bench T3 EPISODE Run — DESCRIPTIVE / PRE-GATE",
        "",
        f"Status: **{'COMPLETE' if complete else 'PARTIAL'}** · "
        f"scored-or-error-recorded: **{len(records)}/{expected_cells}**",
        f"- Scored cells: **{scored_count}**",
        f"- Error-recorded cells: **{error_count}**",
        "",
        "## Mechanical SCREEN vs judge score of record",
        "",
        f"- Agreement: **{comparisons['agreement']}**",
        f"- Disagreement: **{comparisons['disagreement']}**",
        f"- Ungraded: **{comparisons['ungraded']}**",
        "",
        "Mechanical outcomes are SCREEN only. DECISION marker hits are flags only and "
        "never override the judge score of record.",
        "",
        "## Disagreement summary",
        "",
    ]
    disagreements = [
        record for record in records
        if record.get("comparison", {}).get("status") == "disagreement"
    ]
    lines.extend(
        f"- {record.get('item_id')} × `{record.get('sut')}`: mechanical "
        f"{record.get('comparison', {}).get('mechanical_fraction')} vs judge "
        f"{record.get('comparison', {}).get('judge_fraction')}"
        for record in disagreements
    )
    if not disagreements:
        lines.append("- None")
    lines.extend(["", "## Refusal taxonomy", ""])
    lines.extend(f"- {name}: {count}" for name, count in sorted(refusals.items()))
    if not refusals:
        lines.append("- None")
    lines.extend(["", "## SCREEN outcome counts", ""])
    lines.extend(f"- {name}: {count}" for name, count in sorted(screens.items()))
    lines.extend(["", "## Cost", ""])
    if fallback_count:
        lines.extend([
            f"- actual-first run accounting total: **${attributed_cost_usd:.6f}**",
            f"- non-authoritative fallback events: **{fallback_count}**",
            "- fallback sources: " + ", ".join(
                f"{source}: {count}"
                for source, count in sorted(fallback_sources.items())),
        ])
    else:
        lines.append(
            f"- response-attributed run cost: **${attributed_cost_usd:.6f}**")
    lines.extend([
        (f"- shared-key delta: **${key_delta:.6f}** (contextual only)"
         if key_delta is not None
         else "- shared-key delta: **unavailable** (contextual only)"),
        "",
        ("The actual-first total uses response actuals where available and explicitly labeled "
         "conservative catalog ceilings where response usage was missing or malformed."
         if fallback_count else
         "Response-attributed per-call cost is the run-specific accounting."),
        "The shared-account key-wide delta is contextual reconciliation evidence only.",
        "",
    ])
    return "\n".join(lines)


def accounting_fallback_sources(records: Sequence[Dict[str, Any]]) -> Counter:
    sources = Counter()
    for record in records:
        for call in record.get("usage", {}).get("calls", []):
            source = (call.get("usage") or {}).get("accounting_source")
            if source:
                sources[str(source)] += 1
    return sources


def _checkpoint_tokens(usage: Dict[str, Any]) -> Optional[Tuple[int, int]]:
    values = []
    for field_name in ("prompt_tokens", "completion_tokens"):
        value = usage.get(field_name)
        if (not isinstance(value, int) or isinstance(value, bool) or value < 0):
            return None
        values.append(value)
    return values[0], values[1]


def checkpoint_attributed_cost(records: Sequence[Dict[str, Any]],
                               catalog: Dict[str, Dict[str, Any]]) -> float:
    """Total a full checkpoint actual-first, with fail-loud catalog fallback."""
    total = 0.0
    for record in records:
        for call in record.get("usage", {}).get("calls", []):
            usage = call.get("usage")
            if not isinstance(usage, dict):
                raise AccountingError("checkpoint usage must be an object")
            model = call.get("model")
            source = usage.get("accounting_source")
            if source is not None:
                tokens = _checkpoint_tokens(usage)
                raw_fallback = usage.get("fallback_cost_usd")
                if (source != MISSING_USAGE_FALLBACK_SOURCE
                        or usage.get("authoritative") is not False
                        or tokens is None
                        or not isinstance(raw_fallback, (int, float))
                        or isinstance(raw_fallback, bool)
                        or not math.isfinite(float(raw_fallback))
                        or float(raw_fallback) < 0):
                    raise AccountingError(
                        "checkpoint usage has an invalid non-authoritative fallback event")
                expected = mvp.cell_cost(
                    tokens[0], tokens[1], mvp.price_for(model, catalog))
                if not math.isclose(
                        float(raw_fallback), expected, rel_tol=1e-12, abs_tol=1e-12):
                    raise AccountingError(
                        "checkpoint usage fallback cost does not match its catalog ceiling")
                total += float(raw_fallback)
                continue
            raw_actual = usage.get("cost")
            if raw_actual not in (None, ""):
                try:
                    actual = float(raw_actual)
                except (TypeError, ValueError) as exc:
                    raise AccountingError(
                        "checkpoint usage has malformed response cost") from exc
                if not math.isfinite(actual) or actual < 0:
                    raise AccountingError(
                        "checkpoint usage response cost must be finite and nonnegative")
                total += actual
                continue
            tokens = _checkpoint_tokens(usage)
            if tokens is None:
                raise AccountingError(
                    "checkpoint usage lacks response actual and valid fallback tokens")
            total += mvp.cell_cost(tokens[0], tokens[1], mvp.price_for(model, catalog))
    return total


def raw_evidence_accounting(
        run_dir: str,
        catalog: Dict[str, Dict[str, Any]]) -> Tuple[float, Counter]:
    """Load the append-only per-attempt ledger, failing loud on ambiguity."""
    path = os.path.join(run_dir, RAW_EVIDENCE_FILENAME)
    calls = []
    try:
        with open(path, encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, 1):
                try:
                    row = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise AccountingError(
                        f"raw-evidence accounting line {line_number} is malformed") from exc
                if not isinstance(row, dict) or row.get("kind") != "raw_emission":
                    raise AccountingError(
                        f"raw-evidence accounting line {line_number} is not a T3 emission")
                entries = row.get("usage")
                if not isinstance(entries, list):
                    raise AccountingError(
                        f"raw-evidence accounting line {line_number} usage is not a list")
                fallback = row.get("fallback_accounting")
                if fallback is not None:
                    if (not isinstance(fallback, dict)
                            or (entries and EvidenceClient._usable_usage(entries))):
                        raise AccountingError(
                            f"raw-evidence accounting line {line_number} is ambiguous")
                    entry = fallback
                else:
                    if len(entries) != 1 or not EvidenceClient._usable_usage(entries):
                        raise AccountingError(
                            f"raw-evidence accounting line {line_number} lacks one usable event")
                    entry = entries[0]
                if entry.get("model") != row.get("slug"):
                    raise AccountingError(
                        f"raw-evidence accounting line {line_number} model does not match slug")
                calls.append({
                    "role": row.get("role"), "name": row.get("name"),
                    "model": entry.get("model"), "usage": entry.get("usage"),
                })
    except OSError as exc:
        raise AccountingError(f"raw-evidence accounting is unreadable: {path}") from exc
    records = [{"usage": {"calls": calls}}]
    return (checkpoint_attributed_cost(records, catalog),
            accounting_fallback_sources(records))


def validate_live_catalog(catalog: Dict[str, Dict[str, Any]]) -> None:
    """Fail loud unless every fixed SUT/judge slug has positive catalog pricing."""
    slugs = list(SUT_SLUGS) + [slug for _name, _family, slug in JUDGE_ROSTER]
    mvp.validate_slugs(slugs, catalog)
    for slug in slugs:
        prompt_price, completion_price = mvp.price_for(slug, catalog)
        if not all(math.isfinite(value) and value > 0
                   for value in (prompt_price, completion_price)):
            raise PreflightError(
                f"catalog prices for {slug!r} must be finite and positive")


def validate_key_snapshot(snapshot: Dict[str, Any]) -> None:
    """Validate the R40.1 auth-key response and require the full $10 NTE headroom."""
    if not isinstance(snapshot, dict):
        raise PreflightError("OpenRouter auth-key snapshot must be an object")
    for field_name in ("usage", "limit", "limit_remaining"):
        value = snapshot.get(field_name)
        if value is not None and (
                not isinstance(value, (int, float))
                or isinstance(value, bool)
                or not math.isfinite(float(value))
                or float(value) < 0):
            raise PreflightError(
                f"OpenRouter auth-key {field_name} must be finite and nonnegative")
    require_preflight(snapshot, MAX_BUDGET_USD)


def prepare_output_dir(path: str, *, resume: bool) -> str:
    """Create a new dated run directory, or validate an explicit checkpoint resume."""
    absolute = os.path.abspath(path)
    if not re.match(r"^\d{8}-", os.path.basename(absolute)):
        raise OutputPathError("output directory basename must start with YYYYMMDD-")
    if os.path.exists(absolute):
        if not os.path.isdir(absolute):
            raise OutputPathError(f"output path is not a directory: {absolute}")
        if not resume:
            raise OutputPathError(f"output directory already exists: {absolute}")
        if (not os.path.exists(os.path.join(absolute, "checkpoint.jsonl"))
                and not (
                    os.path.isfile(os.path.join(absolute, RUN_IDENTITY_FILENAME))
                    and os.path.isfile(os.path.join(absolute, RAW_EVIDENCE_FILENAME)))):
            raise OutputPathError("--resume requires an existing checkpoint.jsonl")
        return absolute
    if resume:
        raise OutputPathError(f"--resume output directory does not exist: {absolute}")
    os.makedirs(absolute)
    return absolute


def build_run_identity(plan: Sequence[EpisodePlanCell]) -> Dict[str, Any]:
    """Return the exact immutable identity/configuration of a T3 run."""
    return {
        "schema_version": 1,
        "artifact_kind": RUN_IDENTITY_ARTIFACT_KIND,
        "plan_cell_keys": [f"{cell.item.id}::{cell.sut}" for cell in plan],
        "manifest_of_record": os.path.relpath(MANIFEST_PATH, PROJECT),
        "suts": list(SUT_SLUGS),
        "judges": [list(row) for row in JUDGE_ROSTER],
        "budget_usd": MAX_BUDGET_USD,
        "expected_cells": len(plan),
    }


def validate_resume_identity(run_dir: str,
                             plan: Sequence[EpisodePlanCell]) -> None:
    """Fail closed unless a resume is the exact T3 run with raw evidence."""
    identity_path = os.path.join(run_dir, RUN_IDENTITY_FILENAME)
    if not os.path.isfile(identity_path):
        raise OutputPathError(
            f"--resume requires an existing T3 run identity: {identity_path}")
    try:
        with open(identity_path, encoding="utf-8") as handle:
            identity = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise OutputPathError(
            f"--resume T3 run identity is unreadable or malformed: {identity_path}"
        ) from exc
    if identity != build_run_identity(plan):
        raise OutputPathError(
            "--resume T3 run identity does not match the requested plan/configuration")
    raw_path = os.path.join(run_dir, RAW_EVIDENCE_FILENAME)
    if not os.path.isfile(raw_path):
        raise OutputPathError(
            f"--resume requires the T3 raw-evidence surface: {raw_path}")


def _next_artifact_path(run_dir: str, filename: str) -> str:
    """Choose an absent name so a resume never overwrites earlier report/metadata."""
    base = os.path.join(run_dir, filename)
    if not os.path.exists(base):
        return base
    stem, extension = os.path.splitext(filename)
    index = 1
    while True:
        candidate = os.path.join(run_dir, f"{stem}-resume-{index:03d}{extension}")
        if not os.path.exists(candidate):
            return candidate
        index += 1


def _write_text_new(path: str, text: str) -> None:
    with open(path, "x", encoding="utf-8") as handle:
        handle.write(text)


def _write_json_new(path: str, value: Dict[str, Any]) -> None:
    with open(path, "x", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)


def _print_dry_plan(plan: Sequence[EpisodePlanCell]) -> None:
    print("WCF-Bench T3 EPISODE — DRY RUN (zero network calls)")
    print(f"plan: {len(plan)} cells = {len({cell.item.id for cell in plan})} items x "
          f"{len(SUT_SLUGS)} SUTs")
    print(f"SUTs: {list(SUT_SLUGS)}")
    print(f"judges: {list(JUDGE_ROSTER)}")
    print(f"manifest: {MANIFEST_PATH}")
    print(f"budget: strict ${MAX_BUDGET_USD:.2f} NTE")
    print("Pass --go with --output-dir <new YYYYMMDD-* directory> for live execution.")


def main(argv: Optional[Sequence[str]] = None, *,
         client_factory: Callable[..., Any] = OpenRouterModelClient,
         catalog_fetch: Callable[..., Any] = mvp.fetch_model_catalog,
         key_fetch: Callable[..., Any] = mvp.fetch_key_snapshot) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--go", action="store_true", help="make paid OpenRouter calls")
    parser.add_argument("--output-dir", help="new dated output directory (required with --go)")
    parser.add_argument("--resume", action="store_true", help="resume the supplied output directory")
    args = parser.parse_args(argv)
    plan = build_execution_plan()
    if not args.go:
        _print_dry_plan(plan)
        return 0
    if not args.output_dir:
        print("ERROR: --go requires an explicit --output-dir", file=sys.stderr)
        return 2
    return _run_live(
        plan, args.output_dir, resume=args.resume,
        client_factory=client_factory, catalog_fetch=catalog_fetch, key_fetch=key_fetch)


def _run_live(plan: Sequence[EpisodePlanCell], output_dir: str, *, resume: bool,
              client_factory: Callable[..., Any],
              catalog_fetch: Callable[..., Any],
              key_fetch: Callable[..., Any]) -> int:
    """Execute the fixed live plan after R40.1/catalog/budget preflight."""
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("ERROR: $OPENROUTER_API_KEY is required with --go", file=sys.stderr)
        return 2
    try:
        # Validate the append-only destination before any remote metadata request.
        if resume:
            run_dir = prepare_output_dir(output_dir, resume=True)
            validate_resume_identity(run_dir, plan)
        else:
            absolute = os.path.abspath(output_dir)
            if not re.match(r"^\d{8}-", os.path.basename(absolute)):
                raise OutputPathError("output directory basename must start with YYYYMMDD-")
            if os.path.exists(absolute):
                raise OutputPathError(f"output directory already exists: {absolute}")
            run_dir = absolute

        key_before = fetch_with_two_retries(key_fetch, api_key)
        validate_key_snapshot(key_before)
        catalog = fetch_with_two_retries(catalog_fetch, api_key)
        validate_live_catalog(catalog)
        prior_cost = raw_evidence_accounting(run_dir, catalog)[0] if resume else 0.0
        if not resume:
            run_dir = prepare_output_dir(run_dir, resume=False)
            _write_json_new(
                os.path.join(run_dir, RUN_IDENTITY_FILENAME),
                build_run_identity(plan),
            )
    except Exception as exc:
        print(f"ERROR: preflight failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2

    sink = JsonlSink(os.path.join(run_dir, RAW_EVIDENCE_FILENAME))
    sink.touch()
    remaining_budget = max(0.0, MAX_BUDGET_USD - prior_cost)
    guard = BudgetGuard(remaining_budget, catalog)
    sut_clients: Dict[str, Any] = {}
    for slug in SUT_SLUGS:
        raw = client_factory(
            model=slug, api_key=api_key, system=None,
            max_tokens=2048,
        )
        sut_clients[slug] = EvidenceClient(
            raw, role="sut", name=slug, slug=slug, guard=guard, sink=sink)
    judge_clients: Dict[str, Any] = {}
    for name, _family, slug in JUDGE_ROSTER:
        raw = client_factory(
            model=slug, api_key=api_key, system=None,
            max_tokens=2048,
        )
        judge_clients[slug] = EvidenceClient(
            raw, role="judge", name=name, slug=slug, guard=guard, sink=sink)

    try:
        panel = build_episode_panel(judge_clients)
        outcome = run_execution(plan, sut_clients, panel, run_dir)
    except Exception as exc:
        print(f"ERROR: live setup/execution failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2

    try:
        key_after = fetch_with_two_retries(key_fetch, api_key)
    except Exception:
        key_after = None
    session_attributed_cost = guard.total_usd()
    try:
        attributed_cost, fallback_sources = raw_evidence_accounting(run_dir, catalog)
    except Exception as exc:
        print(f"ERROR: raw accounting failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2
    fallback_count = sum(fallback_sources.values())
    report = build_report(
        outcome.records, expected_cells=len(plan),
        attributed_cost_usd=attributed_cost,
        key_before=key_before, key_after=key_after,
        run_complete=outcome.done,
        accounting_fallbacks=fallback_sources,
    )
    report_path = _next_artifact_path(run_dir, "episode-report.md")
    metadata_path = _next_artifact_path(run_dir, "run-metadata.json")
    metadata = {
        "artifact_kind": "DESCRIPTIVE / PRE-GATE",
        "run_status": "COMPLETE" if outcome.done else "PARTIAL",
        "expected_cells": len(plan),
        "recorded_cells": len(outcome.records),
        "scored_cells": sum(r.get("status") == "scored" for r in outcome.records),
        "error_cells": sum(r.get("status") == "error" for r in outcome.records),
        "budget_usd": MAX_BUDGET_USD,
        "budget_hit": outcome.budget_hit,
        "stop_reason": outcome.stop_reason,
        "actual_first_run_accounting_total_usd": attributed_cost,
        "session_actual_first_accounting_total_usd": session_attributed_cost,
        "response_attributed_cost_usd": (
            None if fallback_count else attributed_cost),
        "session_response_attributed_cost_usd": (
            None if fallback_count else session_attributed_cost),
        "accounting_fallback_count": fallback_count,
        "accounting_fallback_sources": dict(sorted(fallback_sources.items())),
        "key_before": key_before,
        "key_after": key_after,
        "manifest_path": MANIFEST_PATH,
        "suts": list(SUT_SLUGS),
        "judges": [list(row) for row in JUDGE_ROSTER],
    }
    try:
        _write_text_new(report_path, report)
        _write_json_new(metadata_path, metadata)
    except Exception as exc:
        print(f"ERROR: artifact persistence failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2
    print(f"T3 {'complete' if outcome.done else 'partial'}: {len(outcome.records)}/{len(plan)} cells")
    label = ("actual-first accounting total" if fallback_count
             else "response-attributed cost")
    print(f"{label}: ${attributed_cost:.6f} / ${MAX_BUDGET_USD:.2f} NTE")
    print(f"report: {report_path}")
    return 0 if outcome.done else 1


if __name__ == "__main__":
    raise SystemExit(main())
