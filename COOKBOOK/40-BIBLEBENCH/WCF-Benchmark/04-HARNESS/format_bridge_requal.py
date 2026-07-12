#!/usr/bin/env python
"""R43/R44 format-bridge panel requalification (live only with ``--go``).

The two operational incumbents receive the complete K=8 qualification battery. Grok's
incumbent result is reused for its OPEN-candidate screen; Cohere Command A and Amazon Nova
Pro receive only G4, award-consistency, and discrimination, also at K=8. The default mode
is a hermetic dry plan: it performs no HTTP request and creates no output directory.
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import sys
import time
from dataclasses import dataclass
from typing import Any, Callable, Dict, Optional, Sequence, Tuple


HARNESS_ROOT = os.path.dirname(os.path.abspath(__file__))
if HARNESS_ROOT not in sys.path:
    sys.path.insert(0, HARNESS_ROOT)

from wcfbench import OpenRouterError, OpenRouterModelClient  # noqa: E402
from wcfbench import mvp  # noqa: E402
from wcfbench.judge_panel import JudgePanel  # noqa: E402
from wcfbench.qualification import (  # noqa: E402
    DEFAULT_K,
    DEFAULT_THRESHOLD,
    OPEN_AWARD,
    PROBES,
    SURFACE_PROBES,
    JudgeQualification,
    current_template_hashes,
    load_manifest,
    manifest_from_pass_table,
    qualify_judge,
    run_probe_reps,
)


RUN_DIR_LABEL = "07-PILOTS/20260711-format-bridge-requal"
OUT_DIR = os.path.normpath(os.path.join(HARNESS_ROOT, "..", RUN_DIR_LABEL))
RAW_NAME = "raw_verdicts.jsonl"
MANIFEST_NAME = "20260711-format-bridge-requal-manifest.json"
REPORT_NAME = "20260711-format-bridge-requal-report.md"

K = DEFAULT_K
THRESHOLD = DEFAULT_THRESHOLD
JUDGE_MAX_TOKENS = 2048
DEFAULT_BUDGET = 10.0
MAX_BUDGET = 10.0
RETRIES = 2

INCUMBENT_JUDGES = (
    ("gemini-flash", "google", "google/gemini-2.5-flash"),
    ("grok-4.20", "x-ai", "x-ai/grok-4.20"),
)

CANDIDATE_PROBES = ("g4", "award_consistency", "discrimination")

# Only aliases of the SAME named models are permitted. Deliberately absent: Command R/R+
# and Nova Premier; those are different logical models and cannot substitute on slug drift.
CANDIDATE_ALIASES = (
    ("cohere-command-a", "cohere", ("cohere/command-a", "cohere/command-a-03-2025")),
    ("amazon-nova-pro", "amazon", ("amazon/nova-pro", "amazon/nova-pro-v1")),
)


class PreflightError(RuntimeError):
    """A live run cannot safely start."""


class OutputPathError(RuntimeError):
    """The fixed append-only output directory already exists."""


class BudgetExceeded(RuntimeError):
    """The live accounting total has reached the configured cap."""


class AccountingError(RuntimeError):
    """A paid response did not expose enough usage data to account for it."""


class EvidenceError(RuntimeError):
    """A raw-evidence persistence failure forbids every subsequent paid call."""


class JsonlSink:
    """Append and flush one raw-evidence record at a time."""

    def __init__(self, path: str) -> None:
        self.path = path

    def touch(self) -> None:
        with open(self.path, "a", encoding="utf-8"):
            pass

    def write(self, record: Dict[str, Any]) -> None:
        with open(self.path, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
            fh.flush()
            os.fsync(fh.fileno())


class BudgetGuard:
    """Actual-first, strict-price-fallback accounting checked before every live call."""

    def __init__(self, budget: float, catalog: Dict[str, Dict[str, Any]]) -> None:
        self.budget = budget
        self.catalog = catalog
        self.clients = []
        self.hit = False
        self.accounting_error: Optional[str] = None
        self.fatal_error: Optional[str] = None

    def register(self, model: str, client: Any) -> None:
        self.clients.append((model, client))

    def total_usd(self) -> float:
        return mvp._accounted_client_cost(self.clients, self.catalog)

    def before_call(self, model: Optional[str] = None, prompt: str = "", *,
                    max_tokens: int = 0) -> None:
        if self.fatal_error:
            raise EvidenceError(self.fatal_error)
        if self.accounting_error:
            raise AccountingError(self.accounting_error)
        current = self.total_usd()
        if current > self.budget:
            self.hit = True
            raise BudgetExceeded(
                f"internal total ${current:.4f} exceeded budget ${self.budget:.2f}")
        if model is not None:
            # A UTF-8 byte count is a conservative tokenizer-independent upper bound for
            # prompt tokens. Completion is bounded by the live client's fixed max_tokens.
            prompt_token_ceiling = len(prompt.encode("utf-8"))
            reservation = mvp.cell_cost(
                prompt_token_ceiling, max_tokens, mvp.price_for(model, self.catalog))
            if current + reservation > self.budget:
                self.hit = True
                raise BudgetExceeded(
                    f"current ${current:.4f} + next-call ceiling ${reservation:.4f} "
                    f"would exceed budget ${self.budget:.2f}")

    def after_call(self) -> None:
        if self.total_usd() > self.budget:
            self.hit = True

    def block_for_accounting(self, message: str) -> None:
        self.accounting_error = message

    def block_fatal(self, message: str) -> None:
        self.fatal_error = message


class CapturingClient:
    """Two-retry OpenRouter wrapper with immediate raw-call and budget accounting."""

    def __init__(self, inner: Any, *, name: str, family: str, slug: str,
                 guard: BudgetGuard, sink: JsonlSink, now: Callable[[], str],
                 sleeper: Callable[[float], None] = time.sleep) -> None:
        self.inner = inner
        self.name = name
        self.family = family
        self.slug = slug
        self.guard = guard
        self.sink = sink
        self.now = now
        self.sleeper = sleeper
        self.last_finish_reason = None
        self.last_truncated = False
        self._invocation = 0

    @property
    def usage_log(self):
        return getattr(self.inner, "usage_log", [])

    def _record(self, *, prompt: str, item_id: Optional[str], invocation: int,
                attempt: int, text: Optional[str], usage: Sequence[Dict[str, Any]],
                error: Optional[str]) -> None:
        try:
            self.sink.write({
                "timestamp": self.now(), "kind": "raw_call",
                "judge": self.name, "family": self.family, "slug": self.slug,
                "item_id": item_id, "invocation": invocation, "attempt": attempt,
                "prompt": prompt, "text": text,
                "finish_reason": getattr(self.inner, "last_finish_reason", None),
                "truncated": bool(getattr(self.inner, "last_truncated", False)),
                "usage": list(usage), "error": error,
            })
        except Exception as exc:
            self.guard.block_fatal(
                f"raw evidence persistence failed: {type(exc).__name__}: {exc}")
            raise

    @staticmethod
    def _usable_usage(entries: Sequence[Dict[str, Any]]) -> bool:
        if not entries:
            return False
        for entry in entries:
            usage = (entry or {}).get("usage")
            if not isinstance(usage, dict):
                return False
            has_actual = usage.get("cost") not in (None, "")
            has_tokens = "prompt_tokens" in usage and "completion_tokens" in usage
            if not has_actual and not has_tokens:
                return False
        return True

    def complete(self, prompt: str, item_id: Optional[str] = None) -> str:
        self._invocation += 1
        invocation = self._invocation
        last_error: Optional[Exception] = None
        for attempt in range(RETRIES + 1):
            self.guard.before_call(
                self.slug, prompt,
                max_tokens=int(getattr(self.inner, "max_tokens", JUDGE_MAX_TOKENS)))
            before = len(self.usage_log)
            try:
                text = self.inner.complete(prompt, item_id=item_id)
            except OpenRouterError as exc:
                last_error = exc
                self._record(prompt=prompt, item_id=item_id, invocation=invocation,
                             attempt=attempt, text=None, usage=(), error=str(exc))
                if attempt < RETRIES:
                    self.sleeper(2.0 * (attempt + 1))
                    continue
                raise
            except Exception as exc:
                self._record(prompt=prompt, item_id=item_id, invocation=invocation,
                             attempt=attempt, text=None, usage=(),
                             error=f"{type(exc).__name__}: {exc}")
                raise

            self.last_finish_reason = getattr(self.inner, "last_finish_reason", None)
            self.last_truncated = bool(getattr(self.inner, "last_truncated", False))
            entries = self.usage_log[before:]
            if not self._usable_usage(entries):
                message = f"missing response usage for paid call to {self.slug!r}"
                self.guard.block_for_accounting(message)
                self._record(prompt=prompt, item_id=item_id, invocation=invocation,
                             attempt=attempt, text=text, usage=entries, error=message)
                raise AccountingError(message)
            self.guard.after_call()
            self._record(prompt=prompt, item_id=item_id, invocation=invocation,
                         attempt=attempt, text=text, usage=entries, error=None)
            return text
        raise last_error or RuntimeError("unreachable retry state")


@dataclass
class BatteryResults:
    incumbents: Dict[str, JudgeQualification]
    candidates: Dict[str, JudgeQualification]


@dataclass
class LiveOutcome:
    paths: Dict[str, str]
    manifest: Dict[str, Any]
    results: Optional[BatteryResults]
    internal_total_usd: float
    budget_hit: bool
    accounting_error: Optional[str]
    partial_reason: Optional[str] = None


def resolve_candidate_slugs(
    catalog: Dict[str, Dict[str, Any]],
) -> Tuple[Tuple[str, str, str], ...]:
    """Resolve Command A and Nova Pro only through their predeclared same-model aliases."""
    resolved = []
    missing = []
    for name, family, aliases in CANDIDATE_ALIASES:
        slug = next((candidate for candidate in aliases if candidate in catalog), None)
        if slug is None:
            missing.append(f"{name}: expected one of {list(aliases)}")
        else:
            resolved.append((name, family, slug))
    if missing:
        raise mvp.SlugValidationError(
            "Required Task 4 logical model absent; no cross-model substitution allowed:\n  - "
            + "\n  - ".join(missing))
    return tuple(resolved)


def _surfaces_for(reps: Dict[str, Any]) -> set:
    passed = {probe: reps.get(probe) is not None and reps[probe].n_pass >= THRESHOLD
              for probe in PROBES}
    return {surface for surface, gate in SURFACE_PROBES.items()
            if all(passed[probe] for probe in gate)}


def _record_probe_reps(sink: Optional[JsonlSink], qualification: JudgeQualification,
                       now: Callable[[], str]) -> None:
    if sink is None:
        return
    for probe, probe_reps in qualification.probe_reps.items():
        for rep in probe_reps.reps:
            sink.write({
                "timestamp": now(), "kind": "probe_rep",
                "judge": qualification.name, "family": qualification.family,
                "slug": qualification.slug, "probe": probe,
                "rep": rep.get("rep"), "passed": rep.get("passed"),
                "cause": rep.get("cause"), "detail": rep.get("detail"),
            })


def run_batteries(
    resolved_candidates: Sequence[Tuple[str, str, str]], *,
    client_factory: Callable[[str, str, str], Any],
    qualify_fn: Optional[Callable[..., JudgeQualification]] = None,
    probe_fn: Optional[Callable[..., Any]] = None,
    raw_sink: Optional[JsonlSink] = None,
    now: Callable[[], str] = lambda: datetime.datetime.now().isoformat(timespec="seconds"),
) -> BatteryResults:
    """Run the fixed Task 4 matrix, with no early stop and no duplicate Grok calls."""
    qualify_fn = qualify_fn or qualify_judge
    probe_fn = probe_fn or run_probe_reps

    incumbents: Dict[str, JudgeQualification] = {}
    for name, family, slug in INCUMBENT_JUDGES:
        client = client_factory(name, family, slug)
        result = qualify_fn(client, name=name, family=family, slug=slug,
                            k=K, threshold=THRESHOLD)
        incumbents[name] = result
        _record_probe_reps(raw_sink, result, now)

    candidates: Dict[str, JudgeQualification] = {
        "grok-4.20": incumbents["grok-4.20"]}
    for name, family, slug in resolved_candidates:
        client = client_factory(name, family, slug)
        reps = {probe: probe_fn(client, probe, k=K) for probe in CANDIDATE_PROBES}
        result = JudgeQualification(
            name=name, family=family, slug=slug, k=K, threshold=THRESHOLD,
            probe_reps=reps, surfaces=_surfaces_for(reps),
        )
        candidates[name] = result
        _record_probe_reps(raw_sink, result, now)

    return BatteryResults(incumbents=incumbents, candidates=candidates)


def build_task4_manifest(results: BatteryResults, *, timestamp: str,
                         run_dir: str = RUN_DIR_LABEL) -> Dict[str, Any]:
    """Build one fresh combined manifest; no pass count is carried from earlier runs."""
    ordered = [results.incumbents[name] for name, _family, _slug in INCUMBENT_JUDGES]
    ordered.extend(results.candidates[name] for name, _family, _aliases in CANDIDATE_ALIASES)
    rows = [
        {"name": q.name, "family": q.family, "slug": q.slug,
         "pass_counts": {probe: reps.n_pass for probe, reps in q.probe_reps.items()}}
        for q in ordered
    ]
    manifest = manifest_from_pass_table(
        rows, run_dir=run_dir, timestamp=timestamp,
        memo="R43 panel change + R44 OPEN format bridge and full panel requalification",
        k=K, threshold=THRESHOLD, template_hashes=current_template_hashes(),
    )
    qualifications = {q.name: q for q in ordered}
    for row in manifest["judges"]:
        q = qualifications[row["name"]]
        full = row["name"] in results.incumbents
        row["battery_scope"] = list(PROBES if full else CANDIDATE_PROBES)
        row["not_run_probes"] = [] if full else [p for p in PROBES if p not in CANDIDATE_PROBES]
        row["candidate_open_screen"] = row["name"] in results.candidates
        for probe, reps in q.probe_reps.items():
            row["cause_tally"][probe] = reps.cause_tally()
    manifest["candidate_open_gate"] = {
        "probes": list(CANDIDATE_PROBES), "threshold": THRESHOLD, "k": K}
    manifest["source"] = "live Task 4 pass table (no carried-forward counts)"
    assert all("gpt" not in row["name"].lower() and "gpt" not in row["slug"].lower()
               for row in manifest["judges"])
    return manifest


def _remaining(snapshot: Dict[str, Optional[float]]) -> Optional[float]:
    remaining = snapshot.get("limit_remaining")
    if remaining is None and snapshot.get("limit") is not None and snapshot.get("usage") is not None:
        remaining = snapshot["limit"] - snapshot["usage"]  # type: ignore[operator]
    return remaining


def require_preflight(snapshot: Dict[str, Optional[float]], budget: float) -> None:
    remaining = _remaining(snapshot)
    if remaining is None:
        raise PreflightError("OpenRouter remaining credit unavailable; stop before spending")
    if remaining < budget:
        raise PreflightError(
            f"OpenRouter remaining credit ${remaining:.2f} is below ${budget:.2f} budget")


def fetch_with_two_retries(fetch: Callable[[str], Any], api_key: str, *,
                           sleeper: Callable[[float], None] = time.sleep) -> Any:
    """Run one metadata GET with the project-wide initial attempt + two retries."""
    for attempt in range(RETRIES + 1):
        try:
            return fetch(api_key)
        except Exception:
            if attempt >= RETRIES:
                raise
            sleeper(2.0 * (attempt + 1))
    raise RuntimeError("unreachable metadata retry state")


def reconciliation_line(internal_total: float,
                        before: Dict[str, Optional[float]],
                        after: Optional[Dict[str, Optional[float]]]) -> str:
    before_usage = before.get("usage")
    after_usage = after.get("usage") if after else None
    if before_usage is None or after_usage is None:
        return (f"Cost reconciliation: internal total **${internal_total:.4f}** vs key-side "
                "usage delta **unavailable** — within ±20%: unavailable.")
    delta = after_usage - before_usage
    if delta < 0:
        return (f"Cost reconciliation: internal total **${internal_total:.4f}** vs key-side "
                "usage delta **unavailable** — within ±20%: unavailable.")
    within = abs(internal_total - delta) <= (0.2 * delta if delta else 1e-9)
    return (f"Cost reconciliation: internal total **${internal_total:.4f}** vs key-side "
            f"usage delta **${delta:.4f}** — within ±20%: {'YES' if within else 'NO'}.")


def _write_text_new(path: str, text: str) -> None:
    """Create one new text artifact; refuse to overwrite any existing evidence."""
    with open(path, "x", encoding="utf-8") as fh:
        fh.write(text)


def _write_json_new(path: str, value: Dict[str, Any]) -> None:
    """Create one new JSON artifact; refuse to overwrite any existing evidence."""
    with open(path, "x", encoding="utf-8") as fh:
        json.dump(value, fh, indent=2, sort_keys=True)


class _NoCallClient:
    def complete(self, *_args, **_kwargs):
        raise AssertionError("manifest validation must not run qualification calls")


def _load_and_validate_manifest(path: str) -> Dict[str, Any]:
    """Load a pending manifest through the production JudgePanel path, without live calls."""
    manifest = load_manifest(path)
    clients = [
        {"name": row["name"], "family": row["family"], "slug": row["slug"],
         "client": _NoCallClient()}
        for row in manifest.get("judges", [])
    ]
    JudgePanel(clients, k=len(clients), manifest=manifest)
    return manifest


def _publish_new(source: str, destination: str) -> None:
    """Move a validated pending artifact into a still-absent canonical path."""
    if os.path.exists(destination):
        raise OutputPathError(f"refusing to overwrite published artifact: {destination}")
    os.rename(source, destination)


def _minimal_partial_report(*, timestamp: str, reason: str, internal_total: float,
                            key_before: Dict[str, Optional[float]],
                            key_after: Optional[Dict[str, Optional[float]]]) -> str:
    return "\n".join([
        "# WCF-Bench — R43/R44 Format-Bridge Requalification",
        "",
        f"Run: {timestamp}",
        "",
        f"> **PARTIAL / STOPPED:** {reason} · `qualification_complete=false`",
        "",
        "## OPEN outcome",
        "",
        "**OPEN outcome: UNDETERMINED.** No family outcome or ladder disposition is recorded.",
        "",
        "## Cost",
        "",
        reconciliation_line(internal_total, key_before, key_after),
        "",
        "Raw evidence remains append-only in `raw_verdicts.jsonl`.",
        "",
    ])


def _persist_partial_report(report_path: str, *, timestamp: str, reason: str,
                            internal_total: float,
                            key_before: Dict[str, Optional[float]],
                            key_after: Optional[Dict[str, Optional[float]]]) -> None:
    """Publish or append a final PARTIAL marker without overwriting prior evidence."""
    if os.path.exists(report_path):
        with open(report_path, "a", encoding="utf-8") as fh:
            fh.write("\n\n> **FINAL STATUS OVERRIDE — PARTIAL / STOPPED:** "
                     f"{reason} · `qualification_complete=false`\n\n"
                     "**OPEN outcome: UNDETERMINED.** Any earlier outcome label is "
                     "non-operative because no canonical manifest was published.\n")
        return
    _write_text_new(report_path, _minimal_partial_report(
        timestamp=timestamp, reason=reason, internal_total=internal_total,
        key_before=key_before, key_after=key_after))


def build_report(results: BatteryResults, manifest: Dict[str, Any], *, timestamp: str,
                 internal_total: float, key_before: Dict[str, Optional[float]],
                 key_after: Optional[Dict[str, Optional[float]]], budget: float,
                 partial_reason: Optional[str] = None) -> str:
    """Render the required K=8 table, outcome disclosure, and one reconciliation line."""
    qualifications = dict(results.incumbents)
    qualifications.update(results.candidates)
    lines = [
        "# WCF-Bench — R43/R44 Format-Bridge Requalification",
        "",
        f"Run: {timestamp} · K={K}, gate >= {THRESHOLD}/{K} · max_tokens={JUDGE_MAX_TOKENS} "
        f"· budget ${budget:.2f}",
        "",
        "The award prompt now contains the frozen neutral format exemplar. Results under this "
        "bridged template are **not directly comparable to the pre-bridge MVP**.",
        "",
    ]
    if partial_reason:
        lines.extend([
            f"> **PARTIAL / STOPPED:** {partial_reason} · `qualification_complete=false`",
            "",
        ])

    lines.extend(["## Resolved logical models", ""])
    for row in manifest["judges"]:
        role = "full incumbent" if row["name"] in results.incumbents else "partial candidate"
        if row["name"] == "grok-4.20":
            role += "; OPEN candidate battery reused"
        lines.append(f"- {row['name']} ({row['family']}): `{row['slug']}` — {role}")

    lines.extend([
        "",
        "## K=8 pass/fail table per judge × surface/probe",
        "",
        "| judge | family | resolved slug | probe | gated surface(s) | n_pass/K | result |",
        "|---|---|---|---|---|---|---|",
    ])
    for row in manifest["judges"]:
        q = qualifications[row["name"]]
        scope = PROBES if row["name"] in results.incumbents else CANDIDATE_PROBES
        for probe in scope:
            reps = q.probe_reps[probe]
            surfaces = ", ".join(s for s, gate in SURFACE_PROBES.items() if probe in gate)
            passed = reps.n_pass >= THRESHOLD
            lines.append(
                f"| {q.name} | {q.family} | `{q.slug}` | {probe} | {surfaces or '—'} | "
                f"{reps.n_pass}/{reps.k} | {'PASS' if passed else 'FAIL'} |")
    lines.extend([
        "",
        "Cohere and Nova intentionally have no disclosure or settled-core calls; their G4 result "
        "is the coherence battery. Grok's candidate row is its full incumbent result, not a rerun.",
        "",
        "## Manifest eligibility",
        "",
        "| judge | family | eligible surfaces |",
        "|---|---|---|",
    ])
    for row in manifest["judges"]:
        lines.append(f"| {row['name']} | {row['family']} | "
                     f"{', '.join(row['eligible_surfaces']) or 'none'} |")

    lines.extend(["", "## OPEN outcome", ""])
    if partial_reason:
        lines.append("**OPEN outcome: UNDETERMINED.** A budget/accounting stop interrupted "
                     "the prescribed batteries; no family outcome or ladder disposition is recorded.")
    else:
        open_families = sorted({row["family"] for row in manifest["judges"]
                                if OPEN_AWARD in row["eligible_surfaces"]})
        non_google = [family for family in open_families if family != "google"]
        if len(open_families) >= 2:
            lines.append("**CROSS-FAMILY:** at least one non-Google OPEN family passed: "
                         + ", ".join(non_google) + ".")
        elif non_google:
            lines.append("**SINGLE-FAMILY / NON-GOOGLE-ONLY:** the actual OPEN-eligible "
                         f"family set is {open_families}; a non-Google candidate passed but "
                         "Gemini did not. The ladder is not closed; record this exceptional "
                         "outcome for later escalation.")
        elif open_families:
            lines.append("**SINGLE-FAMILY:** the actual OPEN-eligible family set is "
                         f"{open_families}. Zero non-Google candidates passed; the pre-G6 "
                         "candidate ladder is **CLOSED**.")
        else:
            lines.append("**NO OPEN-ELIGIBLE FAMILY:** zero non-Google candidates passed; "
                         "the completed pre-G6 candidate ladder is **CLOSED**. This unusable "
                         "OPEN outcome requires escalation.")

    lines.extend([
        "",
        "## Cost", "",
        reconciliation_line(internal_total, key_before, key_after),
        "",
        "Internal accounting is actual-first; any response without authoritative cost uses "
        "strict live-catalog prompt/completion prices. Missing accounting fails loud.",
        "",
        "Raw calls and per-rep evidence are append-only in `raw_verdicts.jsonl`; no prior pilot "
        "directory or report was modified.",
        "",
    ])
    return "\n".join(lines)


def _validate_options(k: int, budget: float) -> None:
    if k != K:
        raise PreflightError(f"Task 4 is fixed at K={K}; received K={k}")
    if budget <= 0 or budget > MAX_BUDGET:
        raise PreflightError(
            f"Task 4 budget must be >$0 and <=${MAX_BUDGET:.2f}; received ${budget:.2f}")


def execute_live(
    api_key: str, *, out_dir: str = OUT_DIR, budget: float = DEFAULT_BUDGET,
    key_fetch: Callable[[str], Dict[str, Optional[float]]] = mvp.fetch_key_snapshot,
    catalog_fetch: Callable[[str], Dict[str, Dict[str, Any]]] = mvp.fetch_model_catalog,
    client_builder: Callable[..., Any] = OpenRouterModelClient,
    qualify_fn: Optional[Callable[..., JudgeQualification]] = None,
    probe_fn: Optional[Callable[..., Any]] = None,
    now: Callable[[], str] = lambda: datetime.datetime.now().isoformat(timespec="seconds"),
) -> LiveOutcome:
    """Execute the fixed live matrix after structured preflight and strict validation."""
    _validate_options(K, budget)
    if os.path.exists(out_dir):
        raise OutputPathError(f"append-only output path already exists: {out_dir}")

    try:
        key_before = fetch_with_two_retries(key_fetch, api_key)
    except Exception as exc:
        raise PreflightError(
            f"OpenRouter key preflight failed after two retries: {type(exc).__name__}") from exc
    require_preflight(key_before, budget)
    try:
        catalog = fetch_with_two_retries(catalog_fetch, api_key)
    except Exception as exc:
        raise PreflightError(
            f"OpenRouter catalog fetch failed after two retries: {type(exc).__name__}") from exc
    incumbent_slugs = [slug for _name, _family, slug in INCUMBENT_JUDGES]
    mvp.validate_slugs(incumbent_slugs, catalog)  # includes exact Grok slug validation
    resolved = resolve_candidate_slugs(catalog)
    all_slugs = incumbent_slugs + [slug for _name, _family, slug in resolved]
    for slug in all_slugs:
        mvp.price_for(slug, catalog)  # strict fallback prices validated before spending

    os.makedirs(out_dir, exist_ok=False)
    raw_path = os.path.join(out_dir, RAW_NAME)
    manifest_path = os.path.join(out_dir, MANIFEST_NAME)
    report_path = os.path.join(out_dir, REPORT_NAME)
    guard = BudgetGuard(budget, catalog)
    timestamp = datetime.datetime.now().isoformat(timespec="seconds")
    results: Optional[BatteryResults] = None
    manifest: Dict[str, Any] = {}
    internal_total = 0.0
    key_after = None
    paths = {"report": report_path}
    partial_reason: Optional[str] = None

    try:
        timestamp = now()
        sink = JsonlSink(raw_path)
        sink.touch()
        paths["raw"] = raw_path

        def client_factory(name: str, family: str, slug: str) -> CapturingClient:
            inner = client_builder(model=slug, api_key=api_key, temperature=0.0,
                                   max_tokens=JUDGE_MAX_TOKENS)
            guard.register(slug, inner)
            return CapturingClient(inner, name=name, family=family, slug=slug,
                                   guard=guard, sink=sink, now=now)

        results = run_batteries(
            resolved, client_factory=client_factory, qualify_fn=qualify_fn,
            probe_fn=probe_fn, raw_sink=sink, now=now)
        internal_total = guard.total_usd()

        try:
            key_after = fetch_with_two_retries(key_fetch, api_key)
        except Exception:
            pass  # two retries exhausted; reconciliation is explicitly unavailable

        run_dir = os.path.relpath(
            out_dir, os.path.normpath(os.path.join(HARNESS_ROOT, "..")))
        manifest = build_task4_manifest(results, timestamp=timestamp, run_dir=run_dir)
        manifest["qualification_complete"] = (
            not guard.hit and guard.accounting_error is None and guard.fatal_error is None)
        manifest["resolved_slugs"] = all_slugs

        if guard.fatal_error:
            partial_reason = guard.fatal_error
        elif guard.accounting_error:
            partial_reason = guard.accounting_error
        elif guard.hit:
            partial_reason = f"budget cap ${budget:.2f} reached"

        report = build_report(
            results, manifest, timestamp=timestamp, internal_total=internal_total,
            key_before=key_before, key_after=key_after, budget=budget,
            partial_reason=partial_reason)

        if partial_reason:
            _write_text_new(report_path, report)
        else:
            # Build + validate both pending artifacts. Publish the report first and the
            # canonical manifest LAST so a manifest can never exist without its report.
            pending_report = report_path + ".pending"
            pending_manifest = manifest_path + ".pending"
            _write_text_new(pending_report, report)
            _write_json_new(pending_manifest, manifest)
            _load_and_validate_manifest(pending_manifest)
            _publish_new(pending_report, report_path)
            _publish_new(pending_manifest, manifest_path)
            paths["manifest"] = manifest_path
    except Exception as exc:
        partial_reason = f"{type(exc).__name__}: {exc}"
        if manifest:
            manifest["qualification_complete"] = False
        try:
            internal_total = guard.total_usd()
        except Exception:
            pass
        if key_after is None:
            try:
                key_after = fetch_with_two_retries(key_fetch, api_key)
            except Exception:
                pass
        _persist_partial_report(
            report_path, timestamp=timestamp, reason=partial_reason,
            internal_total=internal_total, key_before=key_before, key_after=key_after)

    return LiveOutcome(
        paths=paths, manifest=manifest, results=results,
        internal_total_usd=internal_total, budget_hit=guard.hit,
        accounting_error=guard.accounting_error, partial_reason=partial_reason)


def _print_plan(budget: float) -> None:
    print("WCF-Bench R43/R44 format-bridge requalification — DRY RUN (0 network calls)")
    print(f"K={K}, threshold={THRESHOLD}, max_tokens={JUDGE_MAX_TOKENS}, budget=${budget:.2f}")
    print(f"full incumbents: {INCUMBENT_JUDGES}")
    print("OPEN candidates: Grok 4.20 (reuse), Cohere Command A, Amazon Nova Pro")
    print(f"Cohere/Nova probes only: {CANDIDATE_PROBES}; both always screened")
    print(f"live output (created only with --go): {OUT_DIR}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--go", action="store_true", help="make live paid calls")
    parser.add_argument("--k", "-k", type=int, default=K, help="fixed at 8; other values fail")
    parser.add_argument("--budget", type=float, default=DEFAULT_BUDGET,
                        help="live cap in USD (default and hard maximum: 10)")
    args = parser.parse_args(argv)
    try:
        _validate_options(args.k, args.budget)
    except PreflightError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if not args.go:
        _print_plan(args.budget)
        return 0

    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("ERROR: $OPENROUTER_API_KEY is required with --go.", file=sys.stderr)
        return 2
    try:
        outcome = execute_live(api_key, out_dir=OUT_DIR, budget=args.budget)
    except (PreflightError, OutputPathError, mvp.SlugValidationError, mvp.PricingError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(f"wrote {outcome.paths}")
    if outcome.partial_reason or outcome.budget_hit or outcome.accounting_error:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
