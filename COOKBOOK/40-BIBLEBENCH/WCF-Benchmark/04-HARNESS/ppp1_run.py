#!/usr/bin/env python3
"""Strict-cap PPP-1 runner (dry by default; live only with explicit ``--go``)."""

from __future__ import annotations

import argparse
import datetime
import functools
import hashlib
import json
import math
import os
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple


HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import episode_run  # noqa: E402
import ppp1_preflight  # noqa: E402
from format_bridge_requal import (  # noqa: E402
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
from wcfbench import EXAMINEE_SYSTEM, load_items, manifest_is_fresh, scorer_kind  # noqa: E402
from wcfbench import mvp  # noqa: E402
from wcfbench.judge import JudgeError  # noqa: E402
from wcfbench.judge_panel import (  # noqa: E402
    COHERENCE,
    DISCLOSURE,
    OPEN_AWARD,
    SETTLED_CORE,
    ContestedVerdict,
    EpisodeVerdict,
    JudgePanel,
    OpenVerdict,
    _parse_episode_keypoint_verdicts,
    _score_judge_with_retry,
    build_episode_keypoint_prompt,
)
from wcfbench.openrouter_client import OpenRouterModelClient  # noqa: E402
from wcfbench.qualification import load_manifest  # noqa: E402


PPP1_SUTS = ppp1_preflight.PPP1_SUTS
PPP1_JUDGE = ppp1_preflight.PPP1_JUDGE
VALIDITY_LABEL = ppp1_preflight.VALIDITY_LABEL
SUT_MAX_TOKENS = 2048
JUDGE_MAX_TOKENS = 512
MAX_BUDGET_USD = 23.56
RUN_IDENTITY_FILENAME = "ppp1-run-identity.json"
RAW_EVIDENCE_FILENAME = episode_run.RAW_EVIDENCE_FILENAME
CHECKPOINT_FILENAME = "checkpoint.jsonl"
REPORT_FILENAME = "ppp1-report.md"
METADATA_FILENAME = "run-metadata.json"
FROZEN_CATALOG_HASH = "8aaf8aed304c97244239224bedd4e0677762ea1c69fa8005c429737a49b74268"
PREFLIGHT_DIR = PROJECT / "07-PILOTS" / "20260713-ppp1-zero-paid-preflight"
PREFLIGHT_MANIFEST_PATH = PREFLIGHT_DIR / "ppp1-run-manifest.json"
FROZEN_CATALOG_PATH = PREFLIGHT_DIR / "openrouter-catalog-snapshot.json"
QUALIFICATION_MANIFEST_PATH = (
    PROJECT / "07-PILOTS" / "20260712-artifact-corrected-requal"
    / "20260712-artifact-corrected-requal-manifest.json"
)
BANK_DIR = PROJECT / "05-BANK-YAML"
REQUIRED_GEMINI_SURFACES = {OPEN_AWARD, DISCLOSURE, COHERENCE, SETTLED_CORE}


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat(
        timespec="seconds").replace("+00:00", "Z")


def _read_json(path: Path) -> Dict[str, Any]:
    try:
        with path.open(encoding="utf-8") as handle:
            value = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise PreflightError(f"frozen artifact is unreadable: {path}") from exc
    if not isinstance(value, dict):
        raise PreflightError(f"frozen artifact is not an object: {path}")
    return value


def _sha256(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError as exc:
        raise PreflightError(f"frozen artifact is unreadable: {path}") from exc


def _catalog_hash(catalog: Dict[str, Dict[str, Any]]) -> str:
    try:
        rows = [catalog[slug] for slug in sorted((*PPP1_SUTS, PPP1_JUDGE))]
    except KeyError as exc:
        raise PreflightError(f"missing exact PPP-1 catalog slug: {exc.args[0]}") from exc
    return hashlib.sha256(json.dumps(
        rows, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def load_frozen_catalog() -> Dict[str, Dict[str, Any]]:
    """Load and self-verify the immutable four-model PPP-1 catalog snapshot."""
    snapshot = _read_json(FROZEN_CATALOG_PATH)
    if snapshot.get("validity_label") != VALIDITY_LABEL:
        raise PreflightError("frozen PPP-1 catalog validity label mismatch")
    rows = snapshot.get("models")
    if not isinstance(rows, list):
        raise PreflightError("frozen PPP-1 catalog has no model list")
    catalog = {
        row.get("id"): row for row in rows
        if isinstance(row, dict) and isinstance(row.get("id"), str)
    }
    source_hash = snapshot.get("source_hash")
    computed = _catalog_hash(catalog)
    if source_hash != FROZEN_CATALOG_HASH or computed != FROZEN_CATALOG_HASH:
        raise PreflightError("frozen PPP-1 catalog hash mismatch")
    return catalog


@dataclass(frozen=True)
class PreviewPlan:
    normal_items: Tuple[Any, ...]
    episode_cells: Tuple[episode_run.EpisodePlanCell, ...]
    excluded_dev_set_only_ids: Tuple[str, ...]

    @property
    def cell_keys(self) -> List[str]:
        normal = [
            mvp.cell_key(item.id, sut)
            for item in self.normal_items for sut in PPP1_SUTS
        ]
        return normal + [
            mvp.cell_key(cell.item.id, cell.sut) for cell in self.episode_cells]


@functools.lru_cache(maxsize=1)
def build_execution_plan() -> PreviewPlan:
    """Compose the frozen 204-item MVP path and 22-item blind EPISODE path."""
    items = load_items(str(BANK_DIR))
    normal = mvp.select_bank(str(BANK_DIR), items=items)
    if (len(items), len(normal.runnable), len(normal.excluded_episode),
            len(normal.excluded_dev)) != (230, 204, 22, 4):
        raise PreflightError("PPP-1 bank geometry is not 230/204/22/4")

    base_episode = episode_run.build_execution_plan(bank_dir=str(BANK_DIR))
    first_by_item: Dict[str, episode_run.EpisodePlanCell] = {}
    for cell in base_episode:
        first_by_item.setdefault(cell.item.id, cell)
    if len(first_by_item) != 22:
        raise PreflightError("PPP-1 EPISODE registry does not contain exactly 22 items")
    episode_cells = tuple(
        episode_run.EpisodePlanCell(
            entry=base.entry, item=base.item, spec=base.spec, sut=sut)
        for base in first_by_item.values() for sut in PPP1_SUTS
    )
    plan = PreviewPlan(
        normal_items=tuple(normal.runnable),
        episode_cells=episode_cells,
        excluded_dev_set_only_ids=tuple(sorted(normal.excluded_dev)),
    )
    if len(plan.cell_keys) != 678 or len(set(plan.cell_keys)) != 678:
        raise PreflightError("PPP-1 execution plan must contain 678 unique cells")

    frozen = _read_json(PREFLIGHT_MANIFEST_PATH)
    frozen_items = {
        (row.get("item_id"), row.get("kind"))
        for row in frozen.get("items", []) if isinstance(row, dict)
    }
    current_items = {
        (item.id, scorer_kind(item))
        for item in (*plan.normal_items,
                     *(cell.item for cell in plan.episode_cells[::len(PPP1_SUTS)]))
    }
    if (frozen.get("validity_label") != VALIDITY_LABEL
            or frozen.get("catalog_hash") != FROZEN_CATALOG_HASH
            or frozen.get("sut_roster") != list(PPP1_SUTS)
            or frozen.get("judge") != PPP1_JUDGE
            or frozen_items != current_items
            or frozen.get("excluded_dev_set_only_ids") != list(plan.excluded_dev_set_only_ids)):
        raise PreflightError("current PPP-1 plan does not match the immutable preflight")
    return plan


def _catalog_identity() -> Dict[str, Any]:
    catalog = load_frozen_catalog()
    return {
        "source_hash": FROZEN_CATALOG_HASH,
        "prices": {
            slug: {
                "prompt": catalog[slug]["pricing"]["prompt"],
                "completion": catalog[slug]["pricing"]["completion"],
            }
            for slug in (*PPP1_SUTS, PPP1_JUDGE)
        },
    }


def build_run_identity(plan: PreviewPlan) -> Dict[str, Any]:
    """Return the immutable identity required for a fresh run or exact resume."""
    return {
        "schema_version": 1,
        "artifact_kind": VALIDITY_LABEL,
        "validity_label": VALIDITY_LABEL,
        "runnable_items": 226,
        "normal_items": len(plan.normal_items),
        "episode_items": len({cell.item.id for cell in plan.episode_cells}),
        "expected_cells": len(plan.cell_keys),
        "cell_keys": plan.cell_keys,
        "excluded_dev_set_only_ids": list(plan.excluded_dev_set_only_ids),
        "suts": list(PPP1_SUTS),
        "judge": PPP1_JUDGE,
        "sut_max_tokens": SUT_MAX_TOKENS,
        "judge_max_tokens": JUDGE_MAX_TOKENS,
        "budget_usd": MAX_BUDGET_USD,
        "catalog_identity": _catalog_identity(),
        "preflight_manifest": os.path.relpath(PREFLIGHT_MANIFEST_PATH, PROJECT),
        "preflight_manifest_sha256": _sha256(PREFLIGHT_MANIFEST_PATH),
        "qualification_manifest": os.path.relpath(QUALIFICATION_MANIFEST_PATH, PROJECT),
        "qualification_manifest_sha256": _sha256(QUALIFICATION_MANIFEST_PATH),
        "concurrency": 1,
    }


def validate_preflight(snapshot: Dict[str, Any],
                       catalog: Dict[str, Dict[str, Any]]) -> None:
    """Enforce R40.1 headroom and the immutable catalog identity before inference."""
    if not isinstance(snapshot, dict):
        raise PreflightError("OpenRouter auth-key snapshot must be an object")
    for field_name in ("usage", "limit", "limit_remaining"):
        value = snapshot.get(field_name)
        if value is not None and (
                not isinstance(value, (int, float)) or isinstance(value, bool)
                or not math.isfinite(float(value)) or float(value) < 0):
            raise PreflightError(
                f"OpenRouter auth-key {field_name} must be finite and nonnegative")
    require_preflight(snapshot, MAX_BUDGET_USD)
    frozen = load_frozen_catalog()
    try:
        mvp.validate_slugs((*PPP1_SUTS, PPP1_JUDGE), catalog)
    except mvp.SlugValidationError as exc:
        raise PreflightError(f"exact PPP-1 catalog slug mismatch: {exc}") from exc
    if _catalog_hash(catalog) != FROZEN_CATALOG_HASH:
        raise PreflightError(
            "live catalog hash does not match the immutable PPP-1 preflight")
    for slug in (*PPP1_SUTS, PPP1_JUDGE):
        if mvp.price_for(slug, catalog) != mvp.price_for(slug, frozen):
            raise PreflightError(f"live catalog price mismatch for exact slug {slug}")


class PreviewJudgePanel(JudgePanel):
    """PPP-1-local one-Gemini adapter; production ``JudgePanel`` is unchanged."""

    def __init__(self, judge_client: Any, *,
                 manifest_path: Path = QUALIFICATION_MANIFEST_PATH) -> None:
        manifest = load_manifest(str(manifest_path))
        if not manifest_is_fresh(manifest):
            raise JudgeError("PPP-1 qualification manifest is stale")
        matches = [
            row for row in manifest.get("judges", [])
            if row.get("slug") == PPP1_JUDGE
        ]
        if len(matches) != 1:
            raise JudgeError("PPP-1 Gemini judge is not unique in the manifest")
        row = matches[0]
        surfaces = set(row.get("eligible_surfaces") or [])
        if not REQUIRED_GEMINI_SURFACES <= surfaces:
            raise JudgeError(
                "PPP-1 Gemini lacks a required manifest-eligible surface")
        self.k = 1
        self.manifest = manifest
        self.discarded: List[Tuple[str, str]] = []
        self.eligible = {"gemini-flash": surfaces}
        self.active = [("gemini-flash", "google", judge_client)]

    def _assign(self, _item: Any) -> List[Tuple[str, str, Any]]:
        return list(self.active)

    @staticmethod
    def _raise_terminal(errors: Sequence[str]) -> None:
        joined = " | ".join(str(error) for error in errors)
        for error_class in (BudgetExceeded, AccountingError, EvidenceError):
            if error_class.__name__ in joined:
                raise error_class(joined)

    def score_open(self, item: Any, response: str) -> OpenVerdict:
        before = len(self.discarded)
        verdict = super().score_open(item, response)
        self._raise_terminal([reason for _name, reason in self.discarded[before:]])
        return verdict

    def score_contested(self, item: Any, response: str,
                        ranking: Any = None) -> ContestedVerdict:
        before = len(self.discarded)
        verdict = super().score_contested(item, response, ranking)
        self._raise_terminal([reason for _name, reason in self.discarded[before:]])
        return verdict

    def score_episode(self, item: Any, response: str) -> EpisodeVerdict:
        """Reuse the exact EPISODE prompt/parser and aggregate the sole Gemini vote."""
        prompt = build_episode_keypoint_prompt(item, response)
        name, family, client = self.active[0]
        text, error = _score_judge_with_retry(
            lambda: client.complete(prompt, item_id=item.id))
        if error is not None:
            self._raise_terminal([error])
            per_judge = [{
                "name": name, "family": family, "verdict_text": None,
                "verdicts": {}, "reasonless": [], "error": error,
                "eligible_surfaces": sorted(self.eligible[name]),
            }]
            verdicts: Dict[str, bool] = {}
            reasonless: List[str] = []
            used: List[Tuple[str, str]] = []
        else:
            verdicts, reasonless = _parse_episode_keypoint_verdicts(text, item)
            per_judge = [{
                "name": name, "family": family, "verdict_text": text,
                "verdicts": verdicts, "reasonless": reasonless, "error": None,
                "eligible_surfaces": sorted(self.eligible[name]),
            }]
            used = [(name, family)]
        aggregate = {
            keypoint.criterion: verdicts.get(keypoint.criterion)
            for keypoint in item.rubric
        }
        graded = [
            keypoint for keypoint in item.rubric
            if aggregate[keypoint.criterion] is not None
        ]
        denominator = sum(keypoint.points for keypoint in graded)
        score = None
        if denominator:
            score = sum(
                keypoint.points for keypoint in graded
                if aggregate[keypoint.criterion] is True) / denominator
        if error is not None:
            item_error = f"all EPISODE judges lost for {item.id}"
        elif not verdicts:
            item_error = f"zero parseable EPISODE judge votes for {item.id}"
        else:
            item_error = None
        return EpisodeVerdict(
            score=score, per_keypoint=aggregate, per_judge=per_judge,
            judges_used=used, escalation=False, escalated_keypoints=[],
            error=item_error)


@dataclass
class PreviewRunOutcome:
    expected_cells: int
    records: List[Dict[str, Any]] = field(default_factory=list)
    completed: int = 0
    errored: int = 0
    skipped: int = 0
    stop_reason: Optional[str] = None
    budget_hit: bool = False

    @property
    def done(self) -> bool:
        return (
            self.stop_reason is None
            and len(self.records) == self.expected_cells
            and all(record.get("status") in {"scored", "error"}
                    for record in self.records)
            and not any(record.get("stop") for record in self.records)
        )


def _participants(sut: str, sut_client: Any,
                  panel: PreviewJudgePanel) -> Tuple[List[Tuple[str, str, Any]], Dict[int, int]]:
    values = [("sut", sut, sut_client)] + [
        ("judge", name, client)
        for name, _family, client in (getattr(panel, "active", None) or [])
    ]
    before = {
        id(client): len(getattr(client, "usage_log", None) or [])
        for _role, _name, client in values
    }
    return values, before


def _usage_since(participants: Sequence[Tuple[str, str, Any]],
                 before: Dict[int, int]) -> Dict[str, Any]:
    return episode_run._usage_since(participants, before)


def _terminal_record(key: str, item_id: str, sut: str, exc: BaseException,
                     usage: Dict[str, Any]) -> Dict[str, Any]:
    reason = f"{type(exc).__name__}: {exc}"
    return {
        "cell_key": key, "item_id": item_id, "sut": sut,
        "status": "error", "error": reason, "timestamp": _now(),
        "stop": {"class": type(exc).__name__, "reason": str(exc)},
        "usage": usage,
    }


def normal_result_completeness_error(result: Any) -> Optional[str]:
    """Return a truthful PPP-1 cell error when a routed normal result is incomplete."""
    if result is None:
        return "missing normal-path result"
    kind = str(getattr(result, "kind", "")).lower()
    if kind in {"ordinal", "anchor"}:
        if not getattr(result, "scored", False):
            return f"{kind.upper()} result is unparsed or mechanically unscored"
        return None
    if kind == "open":
        raw = getattr(result, "judge_raw", None) or []
        triaxial = getattr(result, "triaxial", None)
        usable_judge = (
            len(raw) == 1
            and not raw[0].get("error")
            and OPEN_AWARD in (raw[0].get("eligible_surfaces") or [])
        )
        if (not getattr(result, "scored", False)
                or getattr(result, "fraction", None) is None
                or triaxial is None or getattr(triaxial, "matter", None) is None
                or not usable_judge):
            return "OPEN result lacks one usable manifest-eligible Gemini verdict/headline"
        return None
    if kind == "contested":
        raw = getattr(result, "judge_raw", None) or []
        score = getattr(result, "contested_score", None)
        required = {DISCLOSURE, COHERENCE, SETTLED_CORE}
        usable_judge = (
            len(raw) == 1
            and not raw[0].get("error")
            and required <= set(raw[0].get("eligible_surfaces") or [])
        )
        graded = getattr(score, "graded", {}) if score is not None else {}
        if (score is None or not usable_judge
                or not graded.get("disclosure") or not graded.get("coherence")
                or getattr(score, "disclosure", None) is None
                or getattr(score, "coherence", None) is None
                or getattr(score, "settled_core_fraction", None) is None):
            return "CONTESTED result lacks required single-Gemini graded preview surfaces"
        return None
    return f"unsupported normal-path result kind: {kind or 'missing'}"


def run_normal_execution(items: Sequence[Any], suts: Sequence[str],
                         sut_clients: Dict[str, Any], panel: Any,
                         run_dir: str) -> PreviewRunOutcome:
    """Sequential normal-path composition with fatal budget/custody stops."""
    done = mvp.load_checkpoint(run_dir)
    outcome = PreviewRunOutcome(expected_cells=len(items) * len(suts))
    if any(record.get("stop") for record in done.values()):
        stopped = next(record for record in done.values() if record.get("stop"))
        outcome.stop_reason = stopped.get("error")
        outcome.records = list(done.values())
        return outcome
    for item in items:
        for sut in suts:
            key = mvp.cell_key(item.id, sut)
            if key in done:
                outcome.skipped += 1
                continue
            participants, before = _participants(sut, sut_clients[sut], panel)
            try:
                _report, result, _sut_usage = mvp.run_cell(
                    item, sut, sut_clients[sut], panel)
                usage = _usage_since(participants, before)
                if result is not None and result.error:
                    for error_class in (BudgetExceeded, AccountingError, EvidenceError):
                        if result.error.startswith(error_class.__name__ + ":"):
                            raise error_class(result.error.split(":", 1)[1].strip())
                if result is not None and result.error:
                    record = {
                        "cell_key": key, "item_id": item.id, "sut": sut,
                        "status": "error", "error": result.error,
                        "timestamp": _now(), "usage": usage,
                    }
                    outcome.errored += 1
                else:
                    completeness_error = normal_result_completeness_error(result)
                    if completeness_error:
                        record = {
                            "cell_key": key, "item_id": item.id, "sut": sut,
                            "status": "error", "error": completeness_error,
                            "timestamp": _now(), "usage": usage,
                            "scores": (mvp._cell_scores(result)
                                       if result is not None else None),
                            "judge_raw": getattr(result, "judge_raw", None),
                        }
                        outcome.errored += 1
                    else:
                        record = {
                            "cell_key": key, "item_id": item.id, "sut": sut,
                            "status": "scored", "timestamp": _now(), "usage": usage,
                            "scores": mvp._cell_scores(result),
                            "judge_raw": getattr(result, "judge_raw", None),
                        }
                        outcome.completed += 1
            except (BudgetExceeded, AccountingError, EvidenceError) as exc:
                usage = _usage_since(participants, before)
                record = _terminal_record(key, item.id, sut, exc, usage)
                outcome.errored += 1
                outcome.stop_reason = record["error"]
                outcome.budget_hit = isinstance(exc, BudgetExceeded)
                mvp.append_checkpoint(run_dir, record)
                done[key] = record
                outcome.records = list(done.values())
                return outcome
            except Exception as exc:  # per-cell error survival
                record = {
                    "cell_key": key, "item_id": item.id, "sut": sut,
                    "status": "error", "error": f"{type(exc).__name__}: {exc}",
                    "timestamp": _now(), "usage": _usage_since(participants, before),
                }
                outcome.errored += 1
            mvp.append_checkpoint(run_dir, record)
            done[key] = record
    outcome.records = list(done.values())
    return outcome


def _run_episode_execution(cells: Sequence[episode_run.EpisodePlanCell],
                           sut_clients: Dict[str, Any], panel: PreviewJudgePanel,
                           run_dir: str) -> PreviewRunOutcome:
    done = mvp.load_checkpoint(run_dir)
    outcome = PreviewRunOutcome(expected_cells=len(cells))
    retrying = {
        slug: episode_run._RetryingSUTClient(client, episode_run.time.sleep)
        for slug, client in sut_clients.items()
    }
    for cell in cells:
        key = mvp.cell_key(cell.item.id, cell.sut)
        if key in done:
            outcome.skipped += 1
            continue
        participants, before = _participants(cell.sut, retrying[cell.sut], panel)
        try:
            record = episode_run.run_episode_cell(cell, retrying[cell.sut], panel)
            record["timestamp"] = _now()
            if record.get("judge", {}).get("error"):
                record["status"] = "error"
                record["error"] = record["judge"]["error"]
                outcome.errored += 1
            else:
                record["status"] = "scored"
                outcome.completed += 1
        except (BudgetExceeded, AccountingError, EvidenceError) as exc:
            record = _terminal_record(
                key, cell.item.id, cell.sut, exc,
                _usage_since(participants, before))
            outcome.errored += 1
            outcome.stop_reason = record["error"]
            outcome.budget_hit = isinstance(exc, BudgetExceeded)
            mvp.append_checkpoint(run_dir, record)
            done[key] = record
            outcome.records = list(done.values())
            return outcome
        except Exception as exc:  # per-cell error survival
            record = {
                "cell_key": key, "item_id": cell.item.id, "sut": cell.sut,
                "status": "error", "error": f"{type(exc).__name__}: {exc}",
                "timestamp": _now(), "usage": _usage_since(participants, before),
            }
            outcome.errored += 1
        mvp.append_checkpoint(run_dir, record)
        done[key] = record
    outcome.records = list(done.values())
    return outcome


def execute_plan(plan: PreviewPlan, sut_clients: Dict[str, Any],
                 panel: PreviewJudgePanel, run_dir: str) -> PreviewRunOutcome:
    """Run all 678 cells sequentially, normal first and blind EPISODE second."""
    normal = run_normal_execution(
        plan.normal_items, PPP1_SUTS, sut_clients, panel, run_dir)
    if normal.stop_reason:
        normal.expected_cells = len(plan.cell_keys)
        return normal
    episodes = _run_episode_execution(
        plan.episode_cells, sut_clients, panel, run_dir)
    records = list(mvp.load_checkpoint(run_dir).values())
    return PreviewRunOutcome(
        expected_cells=len(plan.cell_keys), records=records,
        completed=sum(record.get("status") == "scored" for record in records),
        errored=sum(record.get("status") == "error" for record in records),
        skipped=normal.skipped + episodes.skipped,
        stop_reason=episodes.stop_reason, budget_hit=episodes.budget_hit,
    )


def prepare_output_dir(path: str, *, resume: bool) -> str:
    absolute = os.path.abspath(path)
    if not re.match(r"^\d{8}-", os.path.basename(absolute)):
        raise OutputPathError("output directory basename must start with YYYYMMDD-")
    if os.path.exists(absolute):
        if not os.path.isdir(absolute):
            raise OutputPathError(f"output path is not a directory: {absolute}")
        if not resume:
            raise OutputPathError(f"output directory already exists: {absolute}")
        return absolute
    if resume:
        raise OutputPathError(f"--resume output directory does not exist: {absolute}")
    os.makedirs(absolute, exist_ok=False)
    return absolute


def validate_resume_identity(run_dir: str, plan: PreviewPlan) -> None:
    identity_path = os.path.join(run_dir, RUN_IDENTITY_FILENAME)
    try:
        with open(identity_path, encoding="utf-8") as handle:
            identity = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise OutputPathError("--resume requires a readable PPP-1 run identity") from exc
    if identity != build_run_identity(plan):
        raise OutputPathError("--resume identity does not match exact PPP-1 configuration")
    for filename in (RAW_EVIDENCE_FILENAME, CHECKPOINT_FILENAME):
        if not os.path.isfile(os.path.join(run_dir, filename)):
            raise OutputPathError(f"--resume requires existing {filename}")
    _validate_resume_surfaces(run_dir, plan, load_frozen_catalog())


def _strict_checkpoint(run_dir: str, plan: PreviewPlan,
                       catalog: Dict[str, Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], float]:
    path = os.path.join(run_dir, CHECKPOINT_FILENAME)
    expected = {
        key: tuple(key.split("::", 1)) for key in plan.cell_keys
    }
    seen = set()
    records: List[Dict[str, Any]] = []
    try:
        with open(path, encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, 1):
                if not line.strip():
                    raise OutputPathError(
                        f"checkpoint line {line_number} is blank")
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise OutputPathError(
                        f"checkpoint line {line_number} is malformed") from exc
                if not isinstance(record, dict):
                    raise OutputPathError(
                        f"checkpoint line {line_number} is not an object")
                key = record.get("cell_key")
                if key in seen:
                    raise OutputPathError(f"duplicate checkpoint key: {key}")
                if key not in expected:
                    raise OutputPathError(f"checkpoint key is foreign: {key}")
                seen.add(key)
                item_id, sut = expected[key]
                if record.get("item_id") != item_id or record.get("sut") != sut:
                    raise OutputPathError(
                        f"checkpoint identity fields do not match key: {key}")
                status = record.get("status")
                if status not in {"scored", "error"}:
                    raise OutputPathError(f"checkpoint status is invalid for {key}")
                if status == "scored" and (record.get("error") or record.get("stop")):
                    raise OutputPathError(f"checkpoint scored status is incoherent for {key}")
                if status == "error" and not isinstance(record.get("error"), str):
                    raise OutputPathError(f"checkpoint error status lacks a reason for {key}")
                if record.get("stop") is not None:
                    raise OutputPathError(
                        "terminal checkpoint state requires owner disposition; refusing resume")
                usage = record.get("usage")
                calls = usage.get("calls") if isinstance(usage, dict) else None
                if not isinstance(calls, list):
                    raise OutputPathError(f"checkpoint usage is invalid for {key}")
                for call in calls:
                    if not isinstance(call, dict) or call.get("role") not in {"sut", "judge"}:
                        raise OutputPathError(f"checkpoint call is invalid for {key}")
                    model = call.get("model")
                    allowed = set(PPP1_SUTS) if call.get("role") == "sut" else {PPP1_JUDGE}
                    if model not in allowed or not isinstance(call.get("usage"), dict):
                        raise OutputPathError(f"checkpoint call is foreign for {key}")
                records.append(record)
    except OSError as exc:
        raise OutputPathError(f"checkpoint is unreadable: {path}") from exc
    try:
        cost = episode_run.checkpoint_attributed_cost(records, catalog)
    except AccountingError as exc:
        raise OutputPathError(f"checkpoint accounting is unreconcilable: {exc}") from exc
    return records, cost


def _strict_raw_ledger(run_dir: str, plan: PreviewPlan,
                       catalog: Dict[str, Dict[str, Any]]) -> float:
    path = os.path.join(run_dir, RAW_EVIDENCE_FILENAME)
    expected_items = {
        key.split("::", 1)[0] for key in plan.cell_keys
    }
    try:
        with open(path, encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, 1):
                if not line.strip():
                    raise OutputPathError(f"raw ledger line {line_number} is blank")
                try:
                    row = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise OutputPathError(
                        f"raw ledger line {line_number} is malformed") from exc
                if not isinstance(row, dict) or row.get("kind") != "raw_emission":
                    raise OutputPathError(
                        f"raw ledger line {line_number} has an invalid kind")
                role = row.get("role")
                slug = row.get("slug")
                allowed = set(PPP1_SUTS) if role == "sut" else {PPP1_JUDGE}
                if (role not in {"sut", "judge"} or slug not in allowed
                        or row.get("item_id") not in expected_items):
                    raise OutputPathError(
                        f"raw ledger line {line_number} is foreign to the PPP-1 identity")
                if not isinstance(row.get("usage"), list):
                    raise OutputPathError(
                        f"raw ledger line {line_number} usage is invalid")
    except OSError as exc:
        raise OutputPathError(f"raw ledger is unreadable: {path}") from exc
    try:
        return episode_run.raw_evidence_accounting(run_dir, catalog)[0]
    except AccountingError as exc:
        raise OutputPathError(f"raw ledger accounting is unreconcilable: {exc}") from exc


def _validate_resume_surfaces(run_dir: str, plan: PreviewPlan,
                              catalog: Dict[str, Dict[str, Any]]) -> float:
    _records, checkpoint_cost = _strict_checkpoint(run_dir, plan, catalog)
    raw_cost = _strict_raw_ledger(run_dir, plan, catalog)
    if not math.isclose(checkpoint_cost, raw_cost, rel_tol=1e-12, abs_tol=1e-12):
        raise OutputPathError(
            "checkpoint/raw paid-attempt accounting does not reconcile")
    return raw_cost


def next_artifact_path(run_dir: str, filename: str) -> str:
    base = os.path.join(run_dir, filename)
    if not os.path.exists(base):
        return base
    stem, extension = os.path.splitext(filename)
    index = 1
    while True:
        candidate = os.path.join(
            run_dir, f"{stem}-resume-{index:03d}{extension}")
        if not os.path.exists(candidate):
            return candidate
        index += 1


def _write_json_new(path: str, value: Dict[str, Any]) -> None:
    with open(path, "x", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)


def _write_text_new(path: str, value: str) -> None:
    with open(path, "x", encoding="utf-8") as handle:
        handle.write(value)


def _key_delta(before: Dict[str, Any], after: Optional[Dict[str, Any]]) -> Optional[float]:
    before_usage = before.get("usage")
    after_usage = (after or {}).get("usage")
    if not isinstance(before_usage, (int, float)) or not isinstance(after_usage, (int, float)):
        return None
    delta = float(after_usage) - float(before_usage)
    return delta if math.isfinite(delta) and delta >= 0 else None


def build_report(outcome: PreviewRunOutcome, *, response_cost: Optional[float],
                 actual_first_cost: float, key_delta: Optional[float],
                 custody_reconciled: bool) -> str:
    status = "COMPLETE" if outcome.done else "PARTIAL"
    return "\n".join([
        "# WCF-Bench PPP-1 run",
        "",
        f"> **{VALIDITY_LABEL}**",
        "",
        f"Status: **{status}**",
        f"- Scored-or-error-recorded: **{len(outcome.records)}/{outcome.expected_cells}**",
        f"- Scored cells: **{sum(row.get('status') == 'scored' for row in outcome.records)}**",
        f"- Error-recorded cells: **{sum(row.get('status') == 'error' for row in outcome.records)}**",
        f"- Terminal stop: **{outcome.stop_reason or 'none'}**",
        "",
        "## Cost",
        "",
        (f"- response-attributed cost: **${response_cost:.6f}**"
         if response_cost is not None else
         "- response-attributed cost: **unavailable (custody unreconciled)**"
         if not custody_reconciled else
         "- response-attributed cost: **unavailable (fallback accounting present)**"),
        f"- actual-first accounting total: **${actual_first_cost:.6f}**",
        ("- evidence custody: **RECONCILED**"
         if custody_reconciled
         else "- evidence custody: **CUSTODY UNRECONCILED** — captured paid-call "
              "accounting retained; response-attributed cost unavailable"),
        (f"- shared-key delta: **${key_delta:.6f}** (contextual only)"
         if key_delta is not None
         else "- shared-key delta: **unavailable** (contextual only)"),
        "",
        "Mechanical ORDINAL/ANCHOR results remain mechanical. CONTESTED/OPEN and "
        "EPISODE judge evidence is raw single-Gemini preview evidence only.",
        "",
    ])


def _run_live(plan: PreviewPlan, output_dir: str, *, resume: bool,
              client_factory: Callable[..., Any], key_fetch: Callable[..., Any],
              catalog_fetch: Callable[..., Any], execute_fn: Callable[..., PreviewRunOutcome]) -> int:
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("ERROR: $OPENROUTER_API_KEY is required with --go", file=sys.stderr)
        return 2
    try:
        absolute = os.path.abspath(output_dir)
        if resume:
            run_dir = prepare_output_dir(absolute, resume=True)
            validate_resume_identity(run_dir, plan)
            prior_cost = _validate_resume_surfaces(
                run_dir, plan, load_frozen_catalog())
        else:
            if not re.match(r"^\d{8}-", os.path.basename(absolute)):
                raise OutputPathError(
                    "output directory basename must start with YYYYMMDD-")
            if os.path.exists(absolute):
                raise OutputPathError(f"output directory already exists: {absolute}")
            run_dir = absolute
            prior_cost = 0.0

        key_before = fetch_with_two_retries(key_fetch, api_key)
        catalog = fetch_with_two_retries(catalog_fetch, api_key)
        validate_preflight(key_before, catalog)
        if prior_cost > MAX_BUDGET_USD:
            raise BudgetExceeded("resumed raw evidence already exceeds the PPP-1 cap")
        if not resume:
            run_dir = prepare_output_dir(run_dir, resume=False)
            _write_json_new(
                os.path.join(run_dir, RUN_IDENTITY_FILENAME),
                build_run_identity(plan))
    except Exception as exc:
        print(f"ERROR: preflight failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2

    sink = JsonlSink(os.path.join(run_dir, RAW_EVIDENCE_FILENAME))
    sink.touch()
    guard = BudgetGuard(MAX_BUDGET_USD - prior_cost, catalog)
    sut_clients: Dict[str, Any] = {}
    for slug in PPP1_SUTS:
        inner = client_factory(
            model=slug, api_key=api_key, system=EXAMINEE_SYSTEM,
            max_tokens=SUT_MAX_TOKENS)
        sut_clients[slug] = episode_run.EvidenceClient(
            inner, role="sut", name=slug, slug=slug, guard=guard, sink=sink)
    judge_inner = client_factory(
        model=PPP1_JUDGE, api_key=api_key, system=None,
        max_tokens=JUDGE_MAX_TOKENS)
    judge_client = episode_run.EvidenceClient(
        judge_inner, role="judge", name="gemini-flash", slug=PPP1_JUDGE,
        guard=guard, sink=sink)
    try:
        panel = PreviewJudgePanel(judge_client)
        outcome = execute_fn(plan, sut_clients, panel, run_dir)
    except Exception as exc:
        print(f"ERROR: execution setup failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2

    try:
        key_after = fetch_with_two_retries(key_fetch, api_key)
    except Exception:
        key_after = None
    custody_reasons = []
    try:
        raw_total, fallback_sources = episode_run.raw_evidence_accounting(
            run_dir, catalog)
    except Exception as exc:
        raw_total = None
        fallback_sources = Counter()
        custody_reasons.append(f"raw ledger: {type(exc).__name__}: {exc}")
    try:
        checkpoint_total = episode_run.checkpoint_attributed_cost(
            outcome.records, catalog)
    except Exception as exc:
        checkpoint_total = None
        custody_reasons.append(f"checkpoint: {type(exc).__name__}: {exc}")
    try:
        captured_total = prior_cost + guard.total_usd()
    except Exception as exc:
        captured_total = prior_cost
        custody_reasons.append(f"guard: {type(exc).__name__}: {exc}")
    known_totals = [
        ("raw", raw_total), ("checkpoint", checkpoint_total),
        ("guard", captured_total),
    ]
    present_totals = [
        (name, float(total)) for name, total in known_totals if total is not None
    ]
    if (len(present_totals) > 1
            and any(not math.isclose(
                present_totals[0][1], value, rel_tol=1e-12, abs_tol=1e-12)
                    for _name, value in present_totals[1:])):
        custody_reasons.append(
            "accounting mismatch: "
            + ", ".join(f"{name}=${value:.12f}" for name, value in present_totals))
    totals = [
        float(total) for total in (raw_total, checkpoint_total, captured_total)
        if total is not None and math.isfinite(float(total)) and float(total) >= 0
    ]
    if not totals:
        print("ERROR: no valid actual-first accounting surface remains", file=sys.stderr)
        return 2
    actual_first = max(totals)
    custody_reconciled = (
        not custody_reasons
        and raw_total is not None and checkpoint_total is not None
        and math.isclose(raw_total, checkpoint_total, rel_tol=1e-12, abs_tol=1e-12)
        and math.isclose(raw_total, captured_total, rel_tol=1e-12, abs_tol=1e-12)
    )
    fallback_count = sum(fallback_sources.values())
    key_usage_delta = _key_delta(key_before, key_after)
    response_cost = (
        actual_first if custody_reconciled and not fallback_count else None)
    report = build_report(
        outcome, response_cost=response_cost,
        actual_first_cost=actual_first, key_delta=key_usage_delta,
        custody_reconciled=custody_reconciled)
    report_path = next_artifact_path(run_dir, REPORT_FILENAME)
    metadata_path = next_artifact_path(run_dir, METADATA_FILENAME)
    metadata = {
        "validity_label": VALIDITY_LABEL,
        "run_status": "COMPLETE" if outcome.done else "PARTIAL",
        "expected_cells": outcome.expected_cells,
        "recorded_cells": len(outcome.records),
        "scored_cells": sum(row.get("status") == "scored" for row in outcome.records),
        "error_cells": sum(row.get("status") == "error" for row in outcome.records),
        "stop_reason": outcome.stop_reason,
        "budget_usd": MAX_BUDGET_USD,
        "budget_hit": outcome.budget_hit,
        "response_attributed_cost_usd": response_cost,
        "actual_first_accounting_total_usd": actual_first,
        "accounting_fallback_count": fallback_count,
        "accounting_fallback_sources": dict(sorted(fallback_sources.items())),
        "custody_reconciled": custody_reconciled,
        "custody_reconciliation_notes": custody_reasons,
        "key_before": key_before,
        "key_after": key_after,
        "key_usage_delta_usd": key_usage_delta,
        "identity": build_run_identity(plan),
    }
    try:
        _write_text_new(report_path, report)
        _write_json_new(metadata_path, metadata)
    except Exception as exc:
        print(f"ERROR: artifact persistence failed: {type(exc).__name__}: {exc}",
              file=sys.stderr)
        return 2
    print(f"PPP-1 {'complete' if outcome.done else 'partial'}: "
          f"{len(outcome.records)}/{outcome.expected_cells} cells")
    print(f"response-attributed cost: "
          f"{'unavailable' if response_cost is None else f'${response_cost:.6f}'}")
    print(f"shared-key delta: "
          f"{'unavailable' if key_usage_delta is None else f'${key_usage_delta:.6f}'}")
    return 0 if outcome.done else 1


def _print_dry(plan: PreviewPlan) -> None:
    print("WCF-Bench PPP-1 — DRY RUN (zero network calls, zero writes)")
    print(f"{VALIDITY_LABEL}")
    print("plan: 226 items = 204 normal + 22 EPISODE; 678 item-SUT cells")
    print(f"SUTs: {list(PPP1_SUTS)}")
    print(f"judge: {PPP1_JUDGE}")
    print(f"caps: SUT={SUT_MAX_TOKENS}, judge={JUDGE_MAX_TOKENS}, "
          f"strict budget=${MAX_BUDGET_USD:.2f}")
    print(f"identity cells: {len(plan.cell_keys)}; concurrency: sequential")
    print("Pass --go with --output-dir <new YYYYMMDD-* directory> for execution.")


def main(argv: Optional[Sequence[str]] = None, *,
         client_factory: Callable[..., Any] = OpenRouterModelClient,
         key_fetch: Callable[..., Any] = mvp.fetch_key_snapshot,
         catalog_fetch: Callable[..., Any] = mvp.fetch_model_catalog,
         execute_fn: Callable[..., PreviewRunOutcome] = execute_plan) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--go", action="store_true", help="make paid OpenRouter calls")
    parser.add_argument("--output-dir", help="new YYYYMMDD-prefixed output directory")
    parser.add_argument("--resume", action="store_true",
                        help="resume only an exact existing PPP-1 identity")
    args = parser.parse_args(argv)
    try:
        plan = build_execution_plan()
    except Exception as exc:
        print(f"ERROR: plan validation failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2
    if not args.go:
        _print_dry(plan)
        return 0
    if not args.output_dir:
        print("ERROR: --go requires an explicit --output-dir", file=sys.stderr)
        return 2
    return _run_live(
        plan, args.output_dir, resume=args.resume,
        client_factory=client_factory, key_fetch=key_fetch,
        catalog_fetch=catalog_fetch, execute_fn=execute_fn)


EvidenceClient = episode_run.EvidenceClient


if __name__ == "__main__":
    raise SystemExit(main())
