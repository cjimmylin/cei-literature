"""Perturbation flip-rate / invariance runner — spine §5.

Spine §5 makes the P1–P6 perturbation battery mandatory and — the folded-in
PLUMBLINE machinery — treats **inconsistency as itself a scored metric**:
semantically-identical variants of an item must receive consistent verdicts,
and the per-model **flip-rate league table** is a reported result, not a
robustness check to be waved at.

This module is the mechanical engine for that:

  - :func:`run_perturbations` takes an item's authored variants (label -> prompt,
    one label MUST be ``"base"``), completes each against the mock-first client
    seam, reduces every response to a hashable **verdict** via a caller-supplied
    ``verdict_fn``, and computes **flip_rate** = fraction of NON-base variants
    whose verdict differs from the base verdict. It runs entirely against the
    :class:`~wcfbench.mock_client.MockModelClient` seam — no network.
  - :class:`InvarianceLeagueTable` accumulates :class:`FlipResult` s per model
    and exposes a table sorted best-first (lowest mean flip-rate = most
    invariant = best), mirroring §5's league-table framing.

SPINE §5 / Q99 RULE 5 CAVEAT (documented, load-bearing): the variants passed in
MUST be **meaning-preserving** rewrites (paraphrase, option-order, register,
persona, pushback, monitoring-frame — P1–P6). A perturbation that changes a
Westminster-relevant *fact* — the time, place, or calling that legitimately
changes the duty — is a **new item, not a variant**, and must NOT be fed to this
runner: it would score a warranted verdict change as a spurious flip. This
runner assumes that discipline upstream and does not (cannot) re-check it.

Every verdict here is a MOCK on canned responses, not a measurement.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List

# The one label every variant set must contain (the reference verdict).
BASE_LABEL = "base"


def _require(cond: bool, msg: str) -> None:
    """Fail-loud guard, mirroring loader.py."""
    if not cond:
        raise ValueError(msg)


@dataclass
class FlipResult:
    """One item's per-variant verdicts + its flip-rate against the base variant.

    ``verdicts`` maps every variant label (including ``"base"``) to its verdict;
    ``base_verdict`` is the reference; ``flip_rate`` is the fraction of non-base
    variants whose verdict differs from the base (0.0 = perfectly invariant,
    1.0 = every variant flipped). ``item_id`` is carried for traceability.
    """

    item_id: Any
    base_verdict: Any
    verdicts: Dict[str, Any]
    flip_rate: float

    @property
    def n_variants(self) -> int:
        """Number of NON-base variants compared against the base."""
        return len(self.verdicts) - 1


def run_perturbations(
    prompts: Dict[str, str],
    client,
    verdict_fn: Callable[[str], Any],
    item_id: Any = None,
) -> FlipResult:
    """Run an item's variants and compute its flip-rate.

    Parameters
    ----------
    prompts:
        ``{variant_label: prompt_text}``. Exactly one label MUST be ``"base"``
        (the reference verdict); the rest are meaning-preserving perturbations
        (see the module caveat — fact-changing rewrites are new items, not
        variants). Must be non-empty.
    client:
        Any object exposing ``.complete(prompt, item_id=None) -> str`` — the
        mock-first seam. No SDK / socket is ever touched here.
    verdict_fn:
        ``response_text -> hashable verdict`` (e.g. a PASS/FAIL label, an award
        bucket). The reduction from free text to a comparable verdict is the
        caller's; this runner only compares verdicts for equality.
    item_id:
        Passed through to ``client.complete`` and stored on the result for
        traceability.

    Returns
    -------
    FlipResult

    Raises
    ------
    ValueError
        If ``prompts`` is empty or has no ``"base"`` label.
    """
    _require(isinstance(prompts, dict) and len(prompts) > 0, "prompts must be a non-empty mapping")
    _require(
        BASE_LABEL in prompts,
        f"prompts must contain a {BASE_LABEL!r} label (the reference variant); "
        f"got labels {sorted(prompts)}",
    )

    verdicts: Dict[str, Any] = {}
    for label, prompt in prompts.items():
        response = client.complete(prompt, item_id=item_id)
        verdicts[label] = verdict_fn(response)

    base_verdict = verdicts[BASE_LABEL]
    others = [lbl for lbl in verdicts if lbl != BASE_LABEL]
    if others:
        flipped = sum(1 for lbl in others if verdicts[lbl] != base_verdict)
        flip_rate = flipped / len(others)
    else:
        # Only a base variant: nothing to flip against -> perfectly invariant.
        flip_rate = 0.0

    return FlipResult(
        item_id=item_id,
        base_verdict=base_verdict,
        verdicts=verdicts,
        flip_rate=flip_rate,
    )


@dataclass
class InvarianceLeagueTable:
    """Accumulates :class:`FlipResult` s per model → the §5 flip-rate league.

    Add each item's :class:`FlipResult` under its model name; :meth:`table`
    returns rows sorted best-first (lowest mean flip-rate first — most
    invariant model wins). Higher flip-rate = worse invariance.
    """

    # model name -> list of per-item flip rates
    _by_model: Dict[str, List[float]] = field(default_factory=dict)

    def add(self, model: str, result: FlipResult) -> None:
        """Record one item's :class:`FlipResult` under ``model``."""
        _require(
            isinstance(model, str) and model.strip() != "",
            f"model name must be a non-empty string, got {model!r}",
        )
        _require(
            isinstance(result, FlipResult),
            f"result must be a FlipResult, got {type(result).__name__}",
        )
        self._by_model.setdefault(model, []).append(result.flip_rate)

    def mean_flip_rate(self, model: str) -> float:
        """Mean flip-rate for one model across all its recorded items."""
        rates = self._by_model.get(model, [])
        _require(bool(rates), f"no flip results recorded for model {model!r}")
        return sum(rates) / len(rates)

    def table(self) -> List[Dict[str, Any]]:
        """League table rows, best (lowest mean flip-rate) first.

        Each row: ``{"model", "mean_flip_rate", "n_items"}``. Ties broken by
        model name for deterministic ordering.
        """
        rows = [
            {
                "model": model,
                "mean_flip_rate": sum(rates) / len(rates),
                "n_items": len(rates),
            }
            for model, rates in self._by_model.items()
        ]
        rows.sort(key=lambda r: (r["mean_flip_rate"], r["model"]))
        return rows
