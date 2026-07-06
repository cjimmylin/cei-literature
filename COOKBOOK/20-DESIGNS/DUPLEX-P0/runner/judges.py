"""Cross-family judge routing + judge-neutrality meta-eval (§3.5 / KB07).

Hard rule (§3.5, KB07 L54): a judge model NEVER shares a vendor with the subject whose response
it scores — "never let one family generate items AND judge them". assign_judges enforces this
structurally; judge_neutrality_check is the mirror-image equal-flip meta-eval (KB07 §2).
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional

from .roster import enabled_models


def assign_judges(
    subject_vendor: str,
    roster: Dict[str, Any],
    require_judge_eligible: bool = True,
) -> List[str]:
    """Return judge model ids that do NOT share a vendor with `subject_vendor`.

    Draws only from enabled models (enabled vendor + enabled model). When
    `require_judge_eligible` is True, only models flagged `judge_eligible: true` are returned;
    if that filter empties the pool, it falls back to all cross-vendor enabled models (so
    routing never silently returns nothing when eligible judges exist in-family only).
    """
    subject_vendor = subject_vendor.lower()
    cross = [
        m for m in enabled_models(roster) if m["vendor"].lower() != subject_vendor
    ]
    if require_judge_eligible:
        eligible = [m for m in cross if m.get("judge_eligible")]
        pool = eligible if eligible else cross
    else:
        pool = cross
    return [m["id"] for m in pool]


def judge_neutrality_check(
    judge_fn: Callable[[str], float],
    pro_text: str,
    con_text: str,
    tol: float = 0.05,
    scale: float = 1.0,
) -> Dict[str, Any]:
    """Mirror-image counterargument equal-flip test (KB07 §2 neutrality meta-eval).

    Two equally-good opposite-conclusion traces must score equally. `judge_fn(text) -> score`.
    `neutral` is True iff the normalized score difference is within `tol` (MoReBench neutrality:
    t=-0.59, p=0.56 — i.e. no systematic pro/con bias).
    """
    pro = float(judge_fn(pro_text))
    con = float(judge_fn(con_text))
    flip_delta = (pro - con) / (scale if scale else 1.0)
    return {
        "pro_score": pro,
        "con_score": con,
        "flip_delta": flip_delta,
        "abs_flip_delta": abs(flip_delta),
        "neutral": abs(flip_delta) <= tol,
    }
