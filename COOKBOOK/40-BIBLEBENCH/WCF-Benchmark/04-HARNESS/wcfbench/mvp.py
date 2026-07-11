"""MVP full-bank runner logic — resumable, per-cell descriptive pilot (session-13 build).

This module is the LOGIC layer behind ``run_mvp.py``. It is a NEW file (the concurrent
session owns the existing harness modules): it WRAPS ``wcfbench.run`` / ``JudgePanel`` /
``write_run_transcripts`` / ``summarize_disagreement`` per (item × SUT) cell, and adds the
one capability the existing one-shot pipeline lacks — **per-cell checkpoint/resume**.

Why a per-cell loop instead of one ``run(all_items, all_clients)`` call: the existing
``run()`` scores the whole cartesian product in a single pass with no per-cell hook, so an
interrupted or budget-capped run loses everything. Here we call ``run([item], {sut: client})``
one cell at a time — reusing the *exact* scoring path (prompt build → SUT call → route →
panel/refusal) — and after each cell append one JSON line to ``checkpoint.jsonl``. On restart
against the same run dir we load the checkpoint and SKIP completed cells (idempotent resume).
A cell-level exception is caught, recorded ``status=error``, and the run CONTINUES.

Descriptive / PRE-GATE only. No gold minted, examinee blind. The report carries the R34.4
single-family label on OPEN-award numbers when <2 open_award-eligible families are in the
manifest, and lists every settled-core ``0.0`` / ``False`` keypoint under "flagged for
sample-level review (R39(e))" as a SCREEN — never asserted as a model failure.

NO NETWORK is opened by importing or unit-testing this module; the OpenRouter seam is only
touched under ``--go`` with real clients (or a monkeypatched client in tests).
"""

from __future__ import annotations

import datetime
import json
import os
import threading
import urllib.request
from collections import defaultdict
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

from wcfbench import (
    load_items,
    run,
    scorer_kind,
    EPISODE,
    OPEN,
    CONTESTED,
    JudgePanel,
    OpenRouterModelClient,
    OpenRouterError,
    EXAMINEE_SYSTEM,
    summarize_disagreement,
    template_hash,
    write_run_transcripts,
    OPEN_AWARD,
    DISCLOSURE,
    COHERENCE,
    SETTLED_CORE,
)

CANARY = "WCFBENCH-CANARY-c1647-x9k4q"
MODELS_URL = "https://openrouter.ai/api/v1/models"
AUTH_KEY_URL = "https://openrouter.ai/api/v1/auth/key"

#: default SUT roster — deliberately NON-judge families (judges are openai/google/x-ai),
#: so the §4.3 same-family-exclusion never thins a cell's panel.
DEFAULT_SUTS: Tuple[str, ...] = (
    "meta-llama/llama-3.1-8b-instruct",
    "deepseek/deepseek-chat",
    "mistralai/mistral-large-2411",
    "anthropic/claude-3.5-haiku",
)

DEFAULT_BUDGET_USD = 25.0
JUDGE_MAX_TOKENS = 2048
SUT_MAX_TOKENS = 2048


# ---------------------------------------------------------------------------
# bank selection + exclusions
# ---------------------------------------------------------------------------
@dataclass
class BankPlan:
    """The runnable bank after exclusions, plus the audit trail of what was dropped."""

    runnable: List[Any] = field(default_factory=list)
    excluded_dev: List[str] = field(default_factory=list)     # ids dropped for dev_set_only
    excluded_episode: List[str] = field(default_factory=list)  # ids dropped as EPISODE-kind
    total_loaded: int = 0


def select_bank(bank_dir: str, items: Optional[Sequence[Any]] = None) -> BankPlan:
    """Load the bank and split it into runnable vs excluded.

    EXCLUDE ``extra dev_set_only=true`` items (recorded, not run) and EPISODE-kind items
    (they use the separate live-episode machinery). Everything else is runnable. Nothing
    here hardcodes a count — the bank is being expanded from 69 toward 230 concurrently.
    """
    if items is None:
        items = load_items(bank_dir)
    plan = BankPlan(total_loaded=len(items))
    for it in items:
        if it.extra.get("dev_set_only") is True:
            plan.excluded_dev.append(it.id)
            continue
        if scorer_kind(it) == EPISODE:
            plan.excluded_episode.append(it.id)
            continue
        plan.runnable.append(it)
    return plan


# ---------------------------------------------------------------------------
# manifest inspection — how many families can validly award each surface (R34.4)
# ---------------------------------------------------------------------------
def eligible_families(manifest: Dict[str, Any], surface: str) -> List[str]:
    """Distinct judge FAMILIES the manifest qualified for ``surface`` (sorted)."""
    fams = {
        j.get("family")
        for j in manifest.get("judges", [])
        if surface in (j.get("eligible_surfaces") or [])
        and j.get("family")
    }
    return sorted(fams)


def manifest_roster(manifest: Dict[str, Any]) -> List[Tuple[str, str, str]]:
    """Judges the manifest qualified for >=1 surface: (name, family, slug)."""
    return [
        (j["name"], j["family"], j["slug"])
        for j in manifest.get("judges", [])
        if j.get("eligible_surfaces")
    ]


# ---------------------------------------------------------------------------
# OpenRouter model catalog + pricing (cost tracking)
# ---------------------------------------------------------------------------
def fetch_model_catalog(api_key: Optional[str], url: str = MODELS_URL,
                        opener: Optional[Callable[[str, Optional[str]], Dict[str, Any]]] = None
                        ) -> Dict[str, Dict[str, Any]]:
    """Return ``{model_id: model_dict}`` from GET /api/v1/models.

    ``opener`` is an injectable ``(url, api_key) -> parsed-json`` seam so tests never open a
    socket; the default uses urllib. The returned dicts carry OpenRouter's ``pricing`` block
    (``prompt`` / ``completion`` as per-token USD strings).
    """
    data = (opener or _http_get_json)(url, api_key)
    out: Dict[str, Dict[str, Any]] = {}
    for m in data.get("data", []):
        if isinstance(m, dict) and "id" in m:
            out[m["id"]] = m
    return out


def _http_get_json(url: str, api_key: Optional[str]) -> Dict[str, Any]:
    headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
    req = urllib.request.Request(url, headers=headers, method="GET")
    with urllib.request.urlopen(req, timeout=30) as resp:  # pragma: no cover - network
        return json.loads(resp.read().decode("utf-8"))


class SlugValidationError(RuntimeError):
    """Raised (FAIL LOUD) when a requested SUT/judge slug is absent from the live catalog."""


def _nearest(slug: str, catalog_ids: Sequence[str], n: int = 3) -> List[str]:
    """Cheap nearest-match suggestions: same vendor prefix first, then substring overlap."""
    vendor = slug.split("/", 1)[0]
    same_vendor = [c for c in catalog_ids if c.split("/", 1)[0] == vendor]
    tail = slug.split("/", 1)[-1]
    stem = tail.split("-")[0] if tail else tail
    scored = sorted(
        (same_vendor or list(catalog_ids)),
        key=lambda c: (stem not in c, abs(len(c) - len(slug)), c),
    )
    return scored[:n]


def validate_slugs(slugs: Sequence[str], catalog: Dict[str, Dict[str, Any]]) -> None:
    """FAIL LOUD if any slug is not in the live catalog, with nearest-match suggestions.

    Model IDs drift on OpenRouter; a silent 404 mid-run wastes a launch. This is called at
    ``--go`` time (never at import). Tests monkeypatch the catalog.
    """
    catalog_ids = list(catalog.keys())
    missing = [s for s in slugs if s not in catalog]
    if missing:
        lines = ["Unknown OpenRouter model slug(s) — model IDs drift; check GET /api/v1/models:"]
        for s in missing:
            sugg = _nearest(s, catalog_ids)
            lines.append(f"  - {s!r} not found. Nearest: {sugg or '(catalog empty)'}")
        raise SlugValidationError("\n".join(lines))


def price_for(model_id: str, catalog: Dict[str, Dict[str, Any]]) -> Tuple[float, float]:
    """Return ``(prompt_usd_per_token, completion_usd_per_token)`` for ``model_id``.

    Missing/blank pricing → (0.0, 0.0) so cost tracking degrades gracefully rather than
    crashing a run (an unpriced model just contributes 0 to the estimate; flagged in report).
    """
    m = catalog.get(model_id) or {}
    pricing = m.get("pricing") or {}

    def _f(v: Any) -> float:
        try:
            return float(v)
        except (TypeError, ValueError):
            return 0.0

    return _f(pricing.get("prompt")), _f(pricing.get("completion"))


def cell_cost(prompt_tokens: int, completion_tokens: int,
              price: Tuple[float, float]) -> float:
    """Dollar cost of one call: prompt_tokens*p_prompt + completion_tokens*p_completion.

    (This is the cost-projection formula used throughout: OpenRouter prices are per-token
    USD strings from /api/v1/models; total run cost = Σ over calls of this.)
    """
    p_prompt, p_completion = price
    return prompt_tokens * p_prompt + completion_tokens * p_completion


# ---------------------------------------------------------------------------
# checkpoint / resume
# ---------------------------------------------------------------------------
def cell_key(item_id: str, sut_slug: str) -> str:
    return f"{item_id}::{sut_slug}"


def load_checkpoint(run_dir: str) -> Dict[str, Dict[str, Any]]:
    """Load completed cells from ``<run_dir>/checkpoint.jsonl`` → ``{cell_key: record}``.

    Idempotent-resume seam: a cell whose key is present (any status, scored OR error) is
    considered done and is SKIPPED on restart. Last write wins on duplicate keys. A missing
    file is an empty dict (fresh run). Malformed lines are skipped (robust to a torn tail).
    """
    path = os.path.join(run_dir, "checkpoint.jsonl")
    done: Dict[str, Dict[str, Any]] = {}
    if not os.path.exists(path):
        return done
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            k = rec.get("cell_key")
            if k:
                done[k] = rec
    return done


def append_checkpoint(run_dir: str, record: Dict[str, Any]) -> None:
    """Append one cell record as a JSON line, flushed to disk before the run moves on.

    SIGINT-safe: the line is written + flushed + fsync'd before the next cell starts, so an
    interrupt after a completed cell never loses it (the whole point of the checkpoint).
    """
    os.makedirs(run_dir, exist_ok=True)
    path = os.path.join(run_dir, "checkpoint.jsonl")
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")
        fh.flush()
        os.fsync(fh.fileno())


# ---------------------------------------------------------------------------
# per-cell scoring (wraps run() for a single item × single SUT)
# ---------------------------------------------------------------------------
def _cell_scores(result: Any) -> Dict[str, Any]:
    """Extract a compact score summary from a PerItemResult for the checkpoint line."""
    scores: Dict[str, Any] = {
        "kind": result.kind,
        "fraction": result.fraction,
        "scored": result.scored,
        "needs_judge": result.needs_judge,
        "refusal_class": result.refusal_class,
        "refusal_is_failure": result.refusal_is_failure,
    }
    tri = getattr(result, "triaxial", None)
    if tri is not None:
        scores["triaxial"] = {
            "matter": getattr(tri, "matter", None),
            "manner": getattr(tri, "manner", None),
            "end": getattr(tri, "end", None),
        }
    cs = getattr(result, "contested_score", None)
    if cs is not None:
        scores["contested"] = {
            "disclosure": cs.disclosure,
            "coherence": cs.coherence,
            "settled_core_fraction": cs.settled_core_fraction,
            "settled_core": dict(cs.settled_core),
            "position_label": cs.position_label,
            "position_defensible": cs.position_defensible,
        }
    return scores


def _usage_delta(client: Any, before_count: int) -> Dict[str, int]:
    """Sum prompt/completion/total tokens from the client's usage_log entries added
    since ``before_count`` (per-cell token accounting)."""
    log = getattr(client, "usage_log", None) or []
    prompt = completion = total = 0
    for entry in log[before_count:]:
        u = (entry or {}).get("usage") or {}
        prompt += int(u.get("prompt_tokens") or 0)
        completion += int(u.get("completion_tokens") or 0)
        total += int(u.get("total_tokens") or 0)
    return {"prompt_tokens": prompt, "completion_tokens": completion, "total_tokens": total}


def run_cell(item: Any, sut_slug: str, client: Any, panel: Any) -> Tuple[Any, Any, Dict[str, int]]:
    """Score ONE (item, SUT) cell via the existing ``run()`` pipeline.

    Returns ``(run_report, per_item_result, usage_delta)``. ``run()`` itself already survives
    a SUT call error (records it on ``result.error``); this wrapper additionally survives a
    panel/scoring exception so a single bad cell never aborts the whole run.
    """
    before = len(getattr(client, "usage_log", None) or [])
    report = run([item], {sut_slug: client}, panel=panel)
    result = report.result(sut_slug, item.id)
    usage = _usage_delta(client, before)
    return report, result, usage


# ---------------------------------------------------------------------------
# the run loop
# ---------------------------------------------------------------------------
@dataclass
class MVPRunOutcome:
    run_dir: str
    completed: int = 0
    skipped: int = 0
    errored: int = 0
    est_cost_usd: float = 0.0
    total_tokens: int = 0
    budget_hit: bool = False
    per_item_results: List[Any] = field(default_factory=list)  # for transcripts/disagreement
    cell_records: List[Dict[str, Any]] = field(default_factory=list)


def _score_one_cell(
    item: Any, sut: str, client: Any, panel: Any, *,
    ts: str, client_lock: threading.Lock,
) -> Tuple[Dict[str, Any], Optional[Any]]:
    """Do ALL of a single cell's work OFF the shared-state path and return
    ``(checkpoint_record, per_item_result_or_None)``.

    This function is the unit dispatched to worker threads under ``--concurrency N>1``. It
    NEVER touches the ``outcome`` accumulators, the checkpoint file, or the progress logger —
    those are mutated only by the driver under the shared lock. The one shared object it does
    touch is the SUT ``client``: ``run_cell`` snapshots ``client.usage_log`` before/after to
    compute this cell's token delta, so concurrent cells for the SAME SUT would tear that slice
    and the socket/``usage_log`` are not thread-safe. We therefore serialize per-SUT work on a
    per-client lock — parallelism is REAL across distinct SUTs (the roster's 4 families run
    concurrently), and cells for one SUT run one-at-a-time on that client. The panel's judge
    clients are shared across all cells but are never read for per-cell cost accounting, so a
    torn judge log cannot corrupt the checkpoint. Retry/backoff (R40.2) lives inside the
    judge/client path and is inherited unchanged.
    """
    key = cell_key(item.id, sut)
    try:
        with client_lock:
            _report, result, usage = run_cell(item, sut, client, panel)
        if result is not None and result.error:
            record = {
                "cell_key": key, "item_id": item.id, "sut": sut, "status": "error",
                "error": result.error, "usage": usage, "timestamp": ts,
            }
        else:
            record = {
                "cell_key": key, "item_id": item.id, "sut": sut, "status": "scored",
                "scores": _cell_scores(result) if result is not None else None,
                "usage": usage, "timestamp": ts,
            }
        return record, result
    except Exception as e:  # noqa: BLE001 - per-cell error survival is the contract
        # A scoring/panel exception escaped run() — attribute no tokens to it (the SUT-call
        # path is already error-survived inside run(); this catches the rarer panel/scorer
        # crash) and keep the run going.
        record = {
            "cell_key": key, "item_id": item.id, "sut": sut, "status": "error",
            "error": f"{type(e).__name__}: {e}",
            "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
            "timestamp": ts,
        }
        return record, None


def run_bank(
    plan: BankPlan,
    suts: Sequence[str],
    sut_clients: Dict[str, Any],
    panel: Any,
    run_dir: str,
    *,
    catalog: Optional[Dict[str, Dict[str, Any]]] = None,
    budget_usd: float = DEFAULT_BUDGET_USD,
    print_every: int = 10,
    concurrency: int = 1,
    logger: Callable[[str], None] = print,
    now: Callable[[], str] = lambda: datetime.datetime.now().isoformat(timespec="seconds"),
) -> MVPRunOutcome:
    """Drive every runnable (item × SUT) cell with checkpoint/resume, cost tracking, and
    per-cell error survival. Reuses any existing ``checkpoint.jsonl`` in ``run_dir`` to skip
    done cells. Aborts cleanly (checkpointed) if the running $ estimate crosses ``budget_usd``.

    ``concurrency`` (default ``1`` = the exact original sequential behavior) sets the
    ``ThreadPoolExecutor`` worker count. With ``N>1`` cells are scored in parallel, but all
    shared state — the ``checkpoint.jsonl`` append (one fsync'd line per cell, never
    interleaved), the cost/token accumulator, the ``outcome`` tallies, and the progress
    print — is mutated only under a single lock, and each SUT's client is serialized on its
    own lock (see ``_score_one_cell``). Semantics preserved from the sequential path: completed
    cells (any status) skip on startup; a worker exception records ``status=error`` for THAT
    cell only and the run continues; when the running estimate crosses ``budget_usd`` we stop
    SUBMITTING new cells and let in-flight cells finish + checkpoint (clean capped stop);
    ``KeyboardInterrupt`` stops submitting, drains in-flight, and checkpoints what finished.
    """
    os.makedirs(run_dir, exist_ok=True)
    done = load_checkpoint(run_dir)
    catalog = catalog or {}
    prices = {s: price_for(s, catalog) for s in suts}

    outcome = MVPRunOutcome(run_dir=run_dir)
    outcome.est_cost_usd = sum(
        cell_cost(r.get("usage", {}).get("prompt_tokens", 0),
                  r.get("usage", {}).get("completion_tokens", 0),
                  prices.get(r.get("sut", ""), (0.0, 0.0)))
        for r in done.values()
    )
    outcome.total_tokens = sum(r.get("usage", {}).get("total_tokens", 0) for r in done.values())

    # the pending cell plan, in the SAME order as the sequential loop (item-major, SUT-minor).
    pending: List[Tuple[Any, str]] = []
    for item in plan.runnable:
        for sut in suts:
            key = cell_key(item.id, sut)
            if key in done:
                outcome.skipped += 1
                continue
            pending.append((item, sut))

    # one lock guards ALL shared state (checkpoint file, cost/token accumulator, outcome
    # tallies, progress print); one lock PER SUT client serializes that client's usage-log
    # window. In the N=1 path both are uncontended, so behavior is byte-for-byte the original.
    state_lock = threading.Lock()
    client_locks: Dict[str, threading.Lock] = defaultdict(threading.Lock)
    n_seen = 0  # closed over by _commit

    def _commit(record: Dict[str, Any], result: Optional[Any], sut: str) -> None:
        """Fold one finished cell into the shared state — checkpoint + accounting + print.
        Called ONLY under ``state_lock``."""
        nonlocal n_seen
        if record["status"] == "error":
            outcome.errored += 1
        else:
            outcome.completed += 1
        if result is not None:
            outcome.per_item_results.append((sut, result))

        u = record.get("usage", {})
        outcome.est_cost_usd += cell_cost(u.get("prompt_tokens", 0),
                                          u.get("completion_tokens", 0),
                                          prices.get(sut, (0.0, 0.0)))
        outcome.total_tokens += u.get("total_tokens", 0)

        # SIGINT-safe: one fsync'd line per cell, serialized so lines never interleave.
        append_checkpoint(run_dir, record)
        outcome.cell_records.append(record)
        done[record["cell_key"]] = record

        n_seen += 1
        if print_every and n_seen % print_every == 0:
            logger(f"  {n_seen} new cells · est ${outcome.est_cost_usd:.4f} · "
                   f"{outcome.total_tokens} tok · {outcome.errored} err")

    def _budget_exceeded() -> bool:
        return outcome.est_cost_usd >= budget_usd

    # ---- sequential path (N<=1): byte-for-byte the original loop ----
    if concurrency is None or concurrency <= 1:
        for item, sut in pending:
            with state_lock:  # uncontended; keeps the accounting/print path identical
                if _budget_exceeded():
                    outcome.budget_hit = True
                    logger(f"BUDGET CAP ${budget_usd:.2f} reached (est ${outcome.est_cost_usd:.4f}) "
                           f"— aborting cleanly; {outcome.completed} new cells checkpointed.")
                    return outcome
            record, result = _score_one_cell(
                item, sut, sut_clients[sut], panel,
                ts=now(), client_lock=client_locks[sut])
            with state_lock:
                _commit(record, result, sut)
        return outcome

    # ---- concurrent path (N>1) ----
    it = iter(pending)
    in_flight: Dict[Any, str] = {}  # future -> sut

    def _submit_next(executor: ThreadPoolExecutor) -> bool:
        """Submit the next pending cell if the budget still allows. Returns False when
        nothing more will be submitted (exhausted OR budget capped)."""
        with state_lock:
            if _budget_exceeded():
                if not outcome.budget_hit:
                    outcome.budget_hit = True
                    logger(f"BUDGET CAP ${budget_usd:.2f} reached "
                           f"(est ${outcome.est_cost_usd:.4f}) — no longer submitting; "
                           f"draining in-flight cells.")
                return False
        try:
            item, sut = next(it)
        except StopIteration:
            return False
        fut = executor.submit(
            _score_one_cell, item, sut, sut_clients[sut], panel,
            ts=now(), client_lock=client_locks[sut])
        in_flight[fut] = sut
        return True

    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        try:
            # prime the pool up to `concurrency` in-flight cells.
            for _ in range(concurrency):
                if not _submit_next(executor):
                    break
            while in_flight:
                finished, _ = wait(list(in_flight), return_when=FIRST_COMPLETED)
                for fut in finished:
                    sut = in_flight.pop(fut)
                    record, result = fut.result()  # _score_one_cell never re-raises
                    with state_lock:
                        _commit(record, result, sut)
                    # backfill one new cell per completed cell (steady-state pipeline).
                    _submit_next(executor)
        except KeyboardInterrupt:
            # stop submitting; DRAIN in-flight cells and checkpoint what finished, then
            # re-raise so the caller's interrupt semantics are preserved.
            logger("KeyboardInterrupt — draining in-flight cells before exit …")
            for fut in wait(list(in_flight)).done:
                sut = in_flight.pop(fut, None)
                if sut is None:
                    continue
                try:
                    record, result = fut.result()
                except Exception:  # noqa: BLE001 - drain best-effort; _score_one_cell shouldn't raise
                    continue
                with state_lock:
                    _commit(record, result, sut)
            raise

    return outcome


# ---------------------------------------------------------------------------
# report generation (descriptive / pre-gate)
# ---------------------------------------------------------------------------
def _flagged_settled_core(cell_records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Cells with settled_core_fraction 0.0 OR any keypoint False → sample-level review.

    Per R39(e): the raw aggregate is a SCREEN, not a claim. Never assert a model failure
    here — only flag for adjudication against the persisted response text.
    """
    flagged: List[Dict[str, Any]] = []
    for rec in cell_records:
        scores = rec.get("scores") or {}
        cs = scores.get("contested")
        if not cs:
            continue
        scf = cs.get("settled_core_fraction")
        core = cs.get("settled_core") or {}
        false_kps = [crit for crit, ok in core.items() if ok is False]
        if (scf == 0.0) or false_kps:
            flagged.append({
                "item_id": rec["item_id"], "sut": rec["sut"],
                "settled_core_fraction": scf, "false_keypoints": false_kps,
            })
    return flagged


def build_report_md(
    outcome: MVPRunOutcome,
    plan: BankPlan,
    suts: Sequence[str],
    manifest: Dict[str, Any],
    *,
    timestamp: str,
    budget_usd: float,
    dry_run: bool = False,
) -> str:
    """Render the DESCRIPTIVE / PRE-GATE markdown report (R34.4 + R39(e) language binding)."""
    open_fams = eligible_families(manifest, OPEN_AWARD)
    disc_fams = eligible_families(manifest, DISCLOSURE)
    core_fams = eligible_families(manifest, SETTLED_CORE)
    single_family_open = len(open_fams) < 2

    L: List[str] = []
    L.append(f"<!-- {CANARY} -->")
    L.append("# WCF-Bench — MVP full-bank run")
    L.append("")
    L.append("**DESCRIPTIVE / PRE-GATE — not a gated G1–G7 measurement.**")
    L.append("")
    L.append(f"Canary: `{CANARY}` · Run: {timestamp} · manifest: "
             f"`{manifest.get('run_dir')}` (memo: {manifest.get('memo')})")
    if dry_run:
        L.append("")
        L.append("> DRY-RUN plan (no network) — counts, roster, cell plan, cost projection.")
    L.append("")

    # --- coverage summary ---
    L.append("## Run summary")
    L.append("")
    L.append(f"- Bank loaded: **{plan.total_loaded}** items "
             f"(runnable: **{len(plan.runnable)}**; "
             f"excluded dev_set_only: {len(plan.excluded_dev)}; "
             f"excluded EPISODE: {len(plan.excluded_episode)}).")
    L.append(f"- SUT roster ({len(suts)}): {', '.join(suts)}")
    n_cells_planned = len(plan.runnable) * len(suts)
    L.append(f"- Cell plan: {len(plan.runnable)} items × {len(suts)} SUTs = "
             f"**{n_cells_planned}** cells.")
    if not dry_run:
        L.append(f"- Cells this session: {outcome.completed} scored, "
                 f"{outcome.errored} errored, {outcome.skipped} skipped (resumed).")
        if outcome.budget_hit:
            L.append(f"- **BUDGET CAP ${budget_usd:.2f} HIT** — run aborted cleanly "
                     f"(checkpointed; resumable).")
    L.append("")

    # --- cost + tokens ---
    L.append("## Cost + tokens")
    L.append("")
    L.append(f"- Estimated cost: **${outcome.est_cost_usd:.4f}** (budget ${budget_usd:.2f}).")
    L.append(f"- Total tokens: **{outcome.total_tokens}**.")
    L.append("- Cost formula: Σ_calls (prompt_tokens·price_prompt + "
             "completion_tokens·price_completion), per-token USD from GET /api/v1/models.")
    L.append("")

    # --- cross-family coverage / R34.4 label ---
    L.append("## Cross-family award coverage (R34.4)")
    L.append("")
    L.append(f"- OPEN-award-eligible families: {open_fams or '[]'} "
             + ("(**≥2 → cross-family**)" if not single_family_open
                else "(**<2 → SINGLE-FAMILY**)"))
    L.append(f"- DISCLOSURE-eligible families: {disc_fams or '[]'}")
    L.append(f"- SETTLED-CORE-eligible families: {core_fams or '[]'}")
    if single_family_open:
        fam = open_fams[0] if open_fams else "none"
        L.append("")
        L.append(f"> **OPEN-award numbers below are SINGLE-FAMILY ({fam}) — not quotable "
                 f"as a measurement (R34.4).**")
    L.append("")

    # --- per-design × per-SUT tables ---
    L.append("## Per-design × per-SUT (descriptive)")
    L.append("")
    L.extend(_per_design_tables(outcome, suts))

    # --- refusal taxonomy ---
    L.append("## Refusal taxonomy summary")
    L.append("")
    L.extend(_refusal_summary(outcome, suts))

    # --- settled-core screen / flagged review (R39(e)) ---
    L.append("## Settled-core — flagged for sample-level review (R39(e))")
    L.append("")
    L.append("The raw settled-core aggregate is a **SCREEN, not the claim** (R39(e)). Any "
             "cell with `settled_core_fraction` 0.0 or a keypoint `False` is listed here for "
             "sample-level review against the persisted response text — **never asserted as a "
             "model failure**. A lone per-judge `wrong` is a disagreement record, not a floor "
             "break.")
    L.append("")
    flagged = _flagged_settled_core(outcome.cell_records)
    if not flagged:
        L.append("- No settled-core cell flagged this run.")
    else:
        L.append("| item | SUT | settled_core_fraction | false keypoint(s) |")
        L.append("|---|---|---|---|")
        for f in flagged:
            kps = "; ".join(f["false_keypoints"])[:80] or "—"
            L.append(f"| {f['item_id']} | {f['sut']} | {f['settled_core_fraction']} | {kps} |")
    L.append("")

    # --- excluded items appendix ---
    L.append("## Excluded items (appendix)")
    L.append("")
    L.append(f"- dev_set_only ({len(plan.excluded_dev)}): "
             + (", ".join(plan.excluded_dev) or "none"))
    L.append(f"- EPISODE-kind ({len(plan.excluded_episode)}): "
             + (", ".join(plan.excluded_episode) or "none")
             + "  _(run via the separate live-episode machinery.)_")
    L.append("")

    return "\n".join(L) + "\n"


def _per_design_tables(outcome: MVPRunOutcome, suts: Sequence[str]) -> List[str]:
    """Per-design mean fraction (OPEN/ORDINAL/ANCHOR proxy) × per-SUT."""
    # design -> sut -> [fractions]
    agg: Dict[str, Dict[str, List[float]]] = {}
    for sut, r in outcome.per_item_results:
        if r.fraction is None:
            continue
        agg.setdefault(r.design, {}).setdefault(sut, []).append(r.fraction)
    if not agg:
        return ["_No mechanically/panel-scored fractions this session._", ""]
    lines = ["| design | " + " | ".join(suts) + " |",
             "|---|" + "|".join(["---"] * len(suts)) + "|"]
    for design in sorted(agg):
        row = [design]
        for sut in suts:
            vals = agg[design].get(sut)
            row.append(f"{sum(vals)/len(vals):.2f} (n={len(vals)})" if vals else "—")
        lines.append("| " + " | ".join(row) + " |")
    lines.append("")
    lines.append("_(OPEN uses the Matter-proxy headline; contested items are adherence-only "
                 "and carry no fraction — see the settled-core screen above.)_")
    lines.append("")
    return lines


def _refusal_summary(outcome: MVPRunOutcome, suts: Sequence[str]) -> List[str]:
    """Refusal-class tallies per SUT."""
    tally: Dict[str, Dict[str, int]] = {s: {} for s in suts}
    for sut, r in outcome.per_item_results:
        rc = r.refusal_class or "none"
        tally.setdefault(sut, {})
        tally[sut][rc] = tally[sut].get(rc, 0) + 1
    classes = sorted({c for d in tally.values() for c in d})
    if not classes:
        return ["_No refusal classifications this session._", ""]
    lines = ["| SUT | " + " | ".join(classes) + " |",
             "|---|" + "|".join(["---"] * len(classes)) + "|"]
    for sut in suts:
        row = [sut] + [str(tally.get(sut, {}).get(c, 0)) for c in classes]
        lines.append("| " + " | ".join(row) + " |")
    lines.append("")
    return lines


# ---------------------------------------------------------------------------
# output assembly (transcripts + disagreement + report)
# ---------------------------------------------------------------------------
def _rebuild_run_report(outcome: MVPRunOutcome, suts: Sequence[str]) -> Any:
    """Assemble a RunReport-shaped object from the per-cell results for transcripts +
    disagreement (reuses the existing ``write_run_transcripts`` / ``summarize_disagreement``,
    which only touch ``.reports[model].results`` + attributes)."""
    from wcfbench import RunReport, ModelRunReport
    reports: Dict[str, Any] = {}
    for sut in suts:
        rs = [r for s, r in outcome.per_item_results if s == sut]
        reports[sut] = ModelRunReport(model=sut, results=rs, tensor=None, usage={})
    return RunReport(reports=reports)


def write_outputs(
    outcome: MVPRunOutcome,
    plan: BankPlan,
    suts: Sequence[str],
    manifest: Dict[str, Any],
    panel: Any,
    *,
    timestamp: str,
    budget_usd: float,
    report_name: str,
) -> Dict[str, str]:
    """Write transcripts.jsonl, disagreement.json, and the report .md into the run dir.

    checkpoint.jsonl is already written incrementally by ``run_bank``. Returns the paths.
    """
    run_dir = outcome.run_dir
    os.makedirs(run_dir, exist_ok=True)
    paths: Dict[str, str] = {"checkpoint": os.path.join(run_dir, "checkpoint.jsonl")}

    report = _rebuild_run_report(outcome, suts)
    th = template_hash()
    run_meta = {
        "canary": CANARY,
        "suts": list(suts),
        "manifest_run_dir": manifest.get("run_dir"),
        "judges_active": [(n, f) for n, f, _ in getattr(panel, "active", [])] if panel else [],
    }
    paths["transcripts"] = write_run_transcripts(
        report, run_dir, template_hash=th, timestamp=timestamp, run_meta=run_meta)

    cells = summarize_disagreement(report)
    dis = {
        "canary": CANARY,
        "timestamp": timestamp,
        "manifest_run_dir": manifest.get("run_dir"),
        "cells": [
            {"item_id": c.item_id, "model": c.model, "kind": c.kind, "n_judges": c.n_judges,
             "max_spread": c.max_spread, "split_defensible": c.split_defensible,
             "axis_spreads": c.axis_spreads, "judge_values": c.judge_values, "detail": c.detail}
            for c in cells
        ],
    }
    dpath = os.path.join(run_dir, "disagreement.json")
    with open(dpath, "w", encoding="utf-8") as fh:
        json.dump(dis, fh, indent=2)
    paths["disagreement"] = dpath

    md = build_report_md(outcome, plan, suts, manifest,
                         timestamp=timestamp, budget_usd=budget_usd, dry_run=False)
    mpath = os.path.join(run_dir, report_name)
    with open(mpath, "w", encoding="utf-8") as fh:
        fh.write(md)
    paths["report"] = mpath
    return paths


# ---------------------------------------------------------------------------
# client builders (only touched under --go)
# ---------------------------------------------------------------------------
def build_sut_clients(suts: Sequence[str], *, max_tokens: int = SUT_MAX_TOKENS
                      ) -> Dict[str, Any]:
    """Construct one OpenRouterModelClient per SUT with the shared examinee framing."""
    return {s: OpenRouterModelClient(model=s, system=EXAMINEE_SYSTEM, max_tokens=max_tokens)
            for s in suts}


def build_panel(manifest: Dict[str, Any], *, max_tokens: int = JUDGE_MAX_TOKENS) -> Any:
    """Build the MANIFEST-DRIVEN JudgePanel (no probes re-run at construction — R35.4).

    Only judges the manifest qualified for >=1 surface become clients; the panel consumes the
    frozen manifest so per-surface eligibility cannot flip at construction.
    """
    roster = manifest_roster(manifest)
    clients = [{"name": n, "family": f, "slug": s,
                "client": OpenRouterModelClient(model=s, max_tokens=max_tokens)}
               for n, f, s in roster]
    return JudgePanel(clients, k=len(clients), manifest=manifest)
