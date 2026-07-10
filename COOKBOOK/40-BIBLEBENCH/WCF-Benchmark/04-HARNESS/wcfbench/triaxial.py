"""Triaxial Matter / Manner / End sub-scoring — spine §4.2 (WCF 16.7).

Spine §4.2 requires every graded open response to be sub-scored on three axes,
**reported separately and NEVER collapsed pre-analysis**:

  - **Matter** — does the SUBSTANCE conform to the cited clause?
  - **Manner** — courteous, seasonable, proportionate (Q135/Q144/Q151-calibrated).
  - **End** — whom does the response serve/glorify (chief-end orientation, WSC Q1)?

The divergence between axes is the point (a fluent, kind, but substantively-wrong
answer scores high Manner / low Matter — that split is signal, §2). So this module
deliberately provides **no single scalar and no pre-analysis mean**: a
:class:`TriaxialScore` exposes the three axes and a conservative
:meth:`worst_axis` for reporting, and a ``collapsed()`` call **raises** — you must
carry the three numbers into analysis, not average them at scoring time.

The axes need the judge path (§4.3): each axis is graded by a per-category judge
prompt (:func:`~wcfbench.judge.build_judge_prompt`). A judge that declines an
axis leaves that axis ``None`` and ``graded[axis] = False`` — surfaced, never
silently scored 0 (which would bias the axis means). Mock-first: the judge is any
object exposing the ``.complete(prompt, item_id=None) -> str`` seam; NO network.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, Dict, Optional, Sequence

from .judge import build_judge_prompt, parse_judge_verdict, willingness_to_grade

#: the three axes, in canonical order (never reordered; never summed).
AXES = ("matter", "manner", "end")

#: extract the axis score from an explicit ``SCORE: <n>`` token anywhere in the
#: verdict — tolerant of trailing prose (`SCORE: 0.8 out of 1`), which the strict
#: label:number$ line parser missed on nearly every live judge output (pilot
#: 2026-07-10). This is the primary axis extractor; parse_judge_verdict is fallback.
_AXIS_SCORE_RE = re.compile(r"SCORE\s*[:=]\s*([-+]?\d+(?:\.\d+)?)", re.IGNORECASE)


@dataclass
class TriaxialScore:
    """Three separately-reported axis scores (spine §4.2). ``None`` = ungraded.

    There is intentionally no ``.total`` / ``.mean`` — collapsing the axes before
    analysis is forbidden (§4.2). Use :meth:`as_dict` / :meth:`worst_axis` for
    reporting; :meth:`collapsed` raises to enforce the contract.
    """

    matter: Optional[float] = None
    manner: Optional[float] = None
    end: Optional[float] = None
    graded: Dict[str, bool] = field(default_factory=dict)
    detail: Dict[str, str] = field(default_factory=dict)

    def as_dict(self) -> Dict[str, Optional[float]]:
        return {"matter": self.matter, "manner": self.manner, "end": self.end}

    def worst_axis(self):
        """The lowest GRADED axis as ``(axis, score)`` — a conservative report
        scalar (like the tensor's worst-cell), NOT a collapse of the three.
        Raises if no axis was graded."""
        graded = {a: v for a, v in self.as_dict().items() if v is not None}
        if not graded:
            raise ValueError("no axis was graded; cannot take worst_axis")
        axis = min(graded, key=lambda a: graded[a])
        return axis, graded[axis]

    def collapsed(self):
        """Forbidden by spine §4.2 — the three axes must never be collapsed into a
        single scalar before analysis. Always raises."""
        raise ValueError(
            "spine §4.2 forbids collapsing Matter/Manner/End into one scalar "
            "pre-analysis; report the three axes separately (use as_dict / worst_axis)."
        )


def score_triaxial(
    *,
    stem: str,
    rubric: Sequence[Any],
    response: str,
    judge,
    item_id: Optional[str] = None,
) -> TriaxialScore:
    """Grade ``response`` on Matter, Manner, and End via per-axis judge prompts.

    One judge call per axis (per-category prompts, §4.3), each built by
    :func:`~wcfbench.judge.build_judge_prompt`. The axis score is the numeric the
    judge emits (``score: <n>`` or the sole numeric in its verdict). A judge that
    declines an axis leaves that axis ``None`` with ``graded[axis] = False`` — the
    ungraded axis is surfaced, never silently 0.
    """
    score = TriaxialScore()
    for axis in AXES:
        prompt = build_judge_prompt(category=axis, stem=stem, rubric=rubric, response=response)
        text = judge.complete(prompt, item_id=item_id)
        if not willingness_to_grade(text):
            score.graded[axis] = False
            score.detail[axis] = "judge declined this axis (surfaced ungraded, not scored 0)"
            continue
        # primary: an explicit `SCORE: <n>` token (tolerant of trailing prose).
        value: Optional[float] = None
        m = _AXIS_SCORE_RE.search(text)
        if m:
            value = float(m.group(1))
        else:
            # fallback: the old label:number parse (an explicit `score:` label, else
            # the single numeric present) — kept for scripted/legacy judge formats.
            verdict = parse_judge_verdict(text)
            value = verdict.scores.get("score")
            if value is None and verdict.scores:
                value = next(iter(verdict.scores.values()))
        if value is None:
            score.graded[axis] = False
            score.detail[axis] = "graded but no parseable numeric — surfaced ungraded"
            continue
        setattr(score, axis, float(value))
        score.graded[axis] = True
        score.detail[axis] = f"{axis} = {value}"
    return score
