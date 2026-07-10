"""Phase-3 runner — bank + models -> scored items -> reporting tensor.

`run(items, clients)` is the integration spine: for each model, it drives every
item through the full chain —

    build examinee prompt  (promptbuilder, no gold leakage)
      -> client.complete   (the mock/OpenRouter/CLI seam)
        -> parse           (response_parser, tolerant of format drift)
          -> route to a scorer by kind (routing.scorer_kind)
            -> refusal co-score (§4.5, everywhere)

— assembles a :class:`~wcfbench.tensor.ReportingTensor` from the mechanically
scored items, records per-model usage/cost, and **survives per-item errors**
(a failed call or an unparseable response is recorded, never fatal).

Scoring by kind (spine §4.4):
  - ORDINAL   -> parse_ranking + score_aggravate_ordinal (judge-free).
  - ANCHOR    -> score_prooftext_anchors (judge-free stub).
  - OPEN      -> the ``panel`` (triaxial §4.3) if supplied, else the legacy
                ``judge`` float hook, else recorded ``needs_judge`` (NEVER fabricates
                a number).
  - CONTESTED -> the ``panel``'s position/coherence scorer (adherence, not
                correctness — binding ruling ``20260709-contested-item-scoring-
                ruling.md``). It is **never** τ-scored against a ``gold_order`` and
                contributes NOTHING to the correct/incorrect tensor; its adherence
                axes + settled-core live on ``PerItemResult.contested_score`` and the
                per-judge disagreement on ``.judge_raw``. Without a panel it is
                recorded ``needs_judge``.
  - EPISODE   -> skipped from the single-completion path (NARROWGATE T4 is driven
                by the episode state machine; see openrouter_pilot.py).

Design note: the runner passes ``prompt.user`` to the seam; the shared
``EXAMINEE_SYSTEM`` framing is applied at the client boundary (construct real
clients with ``system=EXAMINEE_SYSTEM``). MockModelClient ignores it (keyed by
item id), so the suite stays hermetic. Every number this produces on mock
responses is NOT a measurement (build-plan Phase-2 exit note).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional

from .loader import ItemRecord
from .promptbuilder import build_examinee_prompt
from .response_parser import parse_ranking
from .routing import (
    scorer_kind,
    infer_should_refuse,
    ordinal_max,
    ORDINAL,
    ANCHOR,
    EPISODE,
    OPEN,
    CONTESTED,
)
from .scorers import score_aggravate_ordinal, score_prooftext_anchors
from .refusal import classify_refusal
from .tensor import ScoredItem, ReportingTensor, build_tensor

#: the OPEN judge seam — (item, response) -> fraction in [0,1], or None if the
#: judge is unwilling / declines to grade (the item then stays ``needs_judge``).
JudgeFn = Callable[[ItemRecord, str], Optional[float]]


def _require(cond: bool, msg: str) -> None:
    if not cond:
        raise ValueError(msg)


@dataclass
class PerItemResult:
    """One item's outcome for one model."""

    model: str
    item_id: str
    design: str
    commandment: str
    tier: str
    track: str
    kind: str
    fraction: Optional[float] = None
    scored: bool = False
    needs_judge: bool = False
    contested: bool = False
    refusal_class: Optional[str] = None
    refusal_is_failure: Optional[bool] = None
    error: Optional[str] = None
    detail: str = ""
    response_excerpt: Optional[str] = None
    #: OPEN items graded by the panel carry their Matter/Manner/End here (§4.2).
    triaxial: Optional[Any] = None
    #: CONTESTED items carry their adherence axes + settled-core here (never a gold).
    contested_score: Optional[Any] = None
    #: per-judge raw scores — the cross-judge disagreement a Fable session adjudicates.
    judge_raw: Optional[List[Dict[str, Any]]] = None


@dataclass
class ModelRunReport:
    """All results for one model + the assembled tensor + usage accounting."""

    model: str
    results: List[PerItemResult] = field(default_factory=list)
    tensor: Optional[ReportingTensor] = None
    usage: Dict[str, Any] = field(default_factory=dict)

    def result(self, item_id: str) -> Optional[PerItemResult]:
        for r in self.results:
            if r.item_id == item_id:
                return r
        return None


@dataclass
class RunReport:
    """The full run: per-model reports."""

    reports: Dict[str, ModelRunReport] = field(default_factory=dict)

    def result(self, model: str, item_id: str) -> Optional[PerItemResult]:
        rep = self.reports.get(model)
        return rep.result(item_id) if rep else None


def _excerpt(text: str, n: int = 160) -> str:
    text = (text or "").strip()
    return text if len(text) <= n else text[:n] + "…"


def _score_item(
    item: ItemRecord,
    model: str,
    client: Any,
    judge: Optional[JudgeFn],
    panel: Any = None,
) -> PerItemResult:
    """Run + score one item for one model. Never raises; records errors inline."""
    kind = scorer_kind(item)
    base = dict(
        model=model, item_id=item.id, design=item.design,
        commandment=item.commandments[0], tier=item.tier, track=item.track, kind=kind,
    )

    # EPISODE: not a single-completion item — the episode state machine drives it.
    if kind == EPISODE:
        return PerItemResult(
            **base,
            detail="episode (NARROWGATE T4) — routed to the state-machine path, not the completion path",
        )

    prompt = build_examinee_prompt(item)
    try:
        response = client.complete(prompt.user, item.id)
    except Exception as e:  # per-item error survival (upstream 5xx, timeout, ...)
        return PerItemResult(**base, error=f"{type(e).__name__}: {e}",
                             detail="model call failed — item recorded, run continues")

    excerpt = _excerpt(response)
    should_refuse = infer_should_refuse(item)
    rf = classify_refusal(response, should_refuse=should_refuse)

    result = PerItemResult(**base, refusal_class=rf.refusal_class,
                           refusal_is_failure=rf.is_failure, response_excerpt=excerpt)

    if kind == ORDINAL:
        ranking = parse_ranking(response)
        if ranking is None:
            result.detail = "no parseable RANKING (ordinal unscored)"
            return result
        omax = ordinal_max(item)
        s = score_aggravate_ordinal(item.extra.get("gold_order"), ranking, ordering_max=omax)
        result.fraction = (s.ordering_points / s.ordering_max) if s.ordering_max else 0.0
        result.scored = True
        result.detail = s.detail
        return result

    if kind == ANCHOR:
        s = score_prooftext_anchors(item.rubric, response)
        if s.max_points <= 0:
            result.detail = "no anchored keypoints to score (anchor unscored)"
            return result
        result.fraction = s.fraction
        result.scored = True
        result.detail = s.detail
        return result

    # CONTESTED: adherence, not correctness (binding ruling). NEVER τ-scored; never
    # in the accuracy tensor. The panel's position/coherence scorer grades it.
    if kind == CONTESTED:
        result.contested = True
        if panel is None:
            result.needs_judge = True
            result.detail = ("contested item — needs the position/coherence judge panel "
                             "(adherence, not correct/incorrect); unscored")
            return result
        ranking = parse_ranking(response)   # the occupied position, handed to the scorer
        verdict = panel.score_contested(item, response, ranking)
        result.contested_score = verdict.score
        result.judge_raw = verdict.per_judge
        # fraction stays None: a contested item contributes NOTHING to the
        # correct/incorrect tensor — its adherence axes live on contested_score.
        scf = verdict.score.settled_core_fraction
        result.detail = ("contested — position-scored (adherence); settled-core "
                         f"{scf:.2f}" if scf is not None else "contested — position-scored (adherence)")
        return result

    # OPEN: the triaxial judge path (§4.3). Panel wins; else the legacy float hook.
    if panel is not None:
        verdict = panel.score_open(item, response)
        result.triaxial = verdict.triaxial
        result.judge_raw = verdict.per_judge
        if verdict.headline is not None:
            result.fraction = float(verdict.headline)
            result.scored = True
            result.detail = "open response scored via the triaxial panel (Matter proxy → tensor)"
        else:
            result.detail = "open response judged (triaxial recorded) but Matter axis ungraded"
        return result
    if judge is not None:
        verdict = judge(item, response)
        if verdict is not None:
            _require(0.0 <= float(verdict) <= 1.0,
                     f"[{item.id}] judge returned {verdict!r}; a fraction must be in [0,1]")
            result.fraction = float(verdict)
            result.scored = True
            result.detail = "open response scored via the judge hook"
            return result
    result.needs_judge = True
    result.detail = "open response — needs a cross-family judge (triaxial §4.3); unscored"
    return result


def _model_usage(client: Any, results: List[PerItemResult]) -> Dict[str, Any]:
    return {
        "total_tokens": getattr(client, "total_tokens", None),
        "call_count": getattr(client, "call_count", None),
        "n_items": len(results),
        "n_scored": sum(1 for r in results if r.scored),
        "n_needs_judge": sum(1 for r in results if r.needs_judge),
        "n_episode": sum(1 for r in results if r.kind == EPISODE),
        "n_contested": sum(1 for r in results if r.contested),
        "n_triaxial": sum(1 for r in results if r.triaxial is not None),
        "n_errors": sum(1 for r in results if r.error),
    }


def run(
    items: List[ItemRecord],
    clients: Dict[str, Any],
    *,
    judge: Optional[JudgeFn] = None,
    panel: Any = None,
) -> RunReport:
    """Run ``items`` through each model in ``clients`` and assemble a RunReport.

    Parameters
    ----------
    items:
        Loaded :class:`ItemRecord`s (e.g. ``load_items('05-BANK-YAML')``).
    clients:
        ``{model_id: client}`` where each client implements the seam
        ``.complete(prompt, item_id=None) -> str`` (MockModelClient in tests;
        OpenRouterModelClient constructed with ``system=EXAMINEE_SYSTEM`` live).
    panel:
        Optional :class:`~wcfbench.judge_panel.JudgePanel` (or any object exposing
        ``.score_open(item, response) -> OpenVerdict`` and
        ``.score_contested(item, response, ranking) -> ContestedVerdict``). This is
        the real §4.3 wiring: OPEN items get triaxial Matter/Manner/End and CONTESTED
        items get the position/coherence scorer. Takes precedence over ``judge``.
    judge:
        Optional legacy OPEN-item float hook ``(item, response) -> fraction|None``
        (kept for simple tests). Ignored for CONTESTED items. When neither ``panel``
        nor ``judge`` handles an OPEN/CONTESTED item, it is recorded ``needs_judge``.

    Fails loud on empty ``items`` or empty ``clients``.
    """
    _require(bool(items), "run() requires a non-empty item list")
    _require(bool(clients), "run() requires at least one model client")

    reports: Dict[str, ModelRunReport] = {}
    for model, client in clients.items():
        results = [_score_item(item, model, client, judge, panel) for item in items]
        scored = [
            ScoredItem(design=r.design, commandment=r.commandment, tier=r.tier,
                       track=r.track, fraction=r.fraction)
            for r in results if r.scored and r.fraction is not None
        ]
        tensor = build_tensor(scored) if scored else None
        reports[model] = ModelRunReport(
            model=model, results=results, tensor=tensor,
            usage=_model_usage(client, results),
        )
    return RunReport(reports=reports)
