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
from typing import Any, Dict, List, Optional, Sequence, Tuple

from .judge import (
    build_judge_prompt,
    parse_judge_verdict,
    willingness_to_grade,
    build_award_prompt,
    parse_award_verdict,
)

#: the three axes, in canonical order (never reordered; never summed).
AXES = ("matter", "manner", "end")

#: pinned anchor levels for the numeric-axis fallback prompt (R24 defense-in-depth).
_PINNED_LEVELS = "0.0, 0.25, 0.5, 0.75, or 1.0"

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
    #: R24: per-axis off-scale flag — a numeric-fallback value outside [0,1] is kept
    #: RAW here but flagged, so aggregation EXCLUDES it (never clamps it in).
    scale_defect: Dict[str, bool] = field(default_factory=dict)
    #: R24 award path: 1-based KP index -> award(True)/deny(False), and the axis each
    #: keypoint belongs to (the keypoint-level disagreement payload).
    awards: Dict[int, bool] = field(default_factory=dict)
    award_axis: Dict[int, str] = field(default_factory=dict)
    #: author-conformity notes (OFFMAP) — reported, never scored.
    offmap: List[str] = field(default_factory=list)
    #: R27: the judge's verbatim verdict text(s) for this item (transcript persistence).
    raw_verdicts: List[str] = field(default_factory=list)

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
    """Grade ``response`` on Matter, Manner, and End (spine §4.2), R24 award-first.

    If the rubric carries axis-tagged keypoints, the primary path is **per-keypoint
    award scoring**: ONE award call (:func:`~wcfbench.judge.build_award_prompt`), the
    judge emits ``KP<n>: award|deny`` per keypoint, and each axis fraction is computed
    mechanically = Σ awarded points / Σ *graded* points for that axis. An unparseable
    keypoint line is excluded from its axis denominator (never silently denied); an
    axis whose keypoints all came back ungraded is ``None`` (surfaced). Axes with no
    tagged keypoints fall back to the hardened numeric prompt.

    If the rubric has NO axis tags at all, every axis uses the numeric fallback:
    the judge emits a 0–1 ``SCORE:`` on pinned levels; a value outside [0,1] is kept
    RAW and flagged ``scale_defect`` (excluded at aggregation, never clamped in) — the
    R24 raw-preservation hygiene.
    """
    score = TriaxialScore()
    tagged = [(i, kp) for i, kp in enumerate(rubric) if getattr(kp, "axis", None) in AXES]

    if tagged:
        _score_award_path(score, tagged, stem=stem, rubric=rubric, response=response,
                          judge=judge, item_id=item_id)
    else:
        for axis in AXES:
            _score_numeric_axis(score, axis, stem=stem, rubric=rubric, response=response,
                                judge=judge, item_id=item_id)
    return score


def _score_award_path(
    score: TriaxialScore,
    tagged: List[Tuple[int, Any]],
    *,
    stem: str,
    rubric: Sequence[Any],
    response: str,
    judge,
    item_id: Optional[str],
) -> None:
    """The R24 primary path: one award call, mechanical per-axis fractions."""
    prompt = build_award_prompt(stem=stem, rubric=rubric, response=response)
    text = judge.complete(prompt, item_id=item_id)
    score.raw_verdicts.append(text)
    # KP index (1-based over the tagged keypoints, rubric order) -> (points, axis).
    kp_meta: Dict[int, Tuple[float, str]] = {
        n: (float(kp.points), kp.axis) for n, (_, kp) in enumerate(tagged, 1)
    }
    for n, (_, kp) in enumerate(tagged, 1):
        score.award_axis[n] = kp.axis

    if not willingness_to_grade(text):
        for axis in AXES:
            if any(a == axis for _, a in kp_meta.values()):
                score.graded[axis] = False
                score.detail[axis] = "judge declined the award grading (surfaced ungraded, not 0)"
        # Axes with no tagged keypoints still fall back to numeric even if the award
        # call was declined: a judge may refuse the award FORMAT yet grade a numeric
        # axis, so this makes one intentional extra .complete() call per untagged axis
        # on mixed-coverage rubrics. Per-axis willingness is re-checked inside.
        for axis in AXES:
            if not any(a == axis for _, a in kp_meta.values()):
                _score_numeric_axis(score, axis, stem=stem, rubric=rubric, response=response,
                                    judge=judge, item_id=item_id)
        return

    verdict = parse_award_verdict(text)
    score.awards = dict(verdict.awards)
    score.offmap = list(verdict.offmap)

    for axis in AXES:
        axis_kps = [(n, pts) for n, (pts, a) in kp_meta.items() if a == axis]
        if not axis_kps:
            # bullet 4: an axis with no tagged keypoints falls back to the numeric prompt.
            _score_numeric_axis(score, axis, stem=stem, rubric=rubric, response=response,
                                judge=judge, item_id=item_id)
            continue
        graded_pts = 0.0
        awarded_pts = 0.0
        ungraded: List[int] = []
        for n, pts in axis_kps:
            if n in verdict.awards:
                graded_pts += pts
                if verdict.awards[n]:
                    awarded_pts += pts
            else:
                ungraded.append(n)   # unparseable KP line — excluded, NOT denied
        if graded_pts <= 0.0:
            score.graded[axis] = False
            setattr(score, axis, None)
            score.detail[axis] = (f"no keypoint line parsed for {axis} "
                                  f"(KP{ungraded} ungraded) — surfaced, not scored 0")
            continue
        setattr(score, axis, awarded_pts / graded_pts)
        score.graded[axis] = True
        note = f"{axis} = {awarded_pts:.2f}/{graded_pts:.2f} awarded points"
        if ungraded:
            note += f"; KP{ungraded} ungraded (excluded from denominator)"
        score.detail[axis] = note


def _score_numeric_axis(
    score: TriaxialScore,
    axis: str,
    *,
    stem: str,
    rubric: Sequence[Any],
    response: str,
    judge,
    item_id: Optional[str],
) -> None:
    """Hardened numeric fallback for an axis with no award coverage (R24 bullet 4/5).

    Pinned levels in the prompt; a value outside [0,1] is stored RAW and flagged
    ``scale_defect`` (excluded at aggregation, never clamped). Unwilling / unparseable
    leaves the axis ``None`` + ``graded=False`` (surfaced, never silently 0)."""
    prompt = build_judge_prompt(category=axis, stem=stem, rubric=rubric, response=response)
    text = judge.complete(prompt, item_id=item_id)
    score.raw_verdicts.append(text)
    if not willingness_to_grade(text):
        score.graded[axis] = False
        score.detail[axis] = "judge declined this axis (surfaced ungraded, not scored 0)"
        return
    value: Optional[float] = None
    m = _AXIS_SCORE_RE.search(text)
    if m:
        value = float(m.group(1))
    else:
        verdict = parse_judge_verdict(text)
        value = verdict.scores.get("score")
        if value is None and verdict.scores:
            value = next(iter(verdict.scores.values()))
    if value is None:
        score.graded[axis] = False
        score.detail[axis] = "graded but no parseable numeric — surfaced ungraded"
        return
    setattr(score, axis, float(value))
    score.graded[axis] = True
    if value < 0.0 or value > 1.0:
        score.scale_defect[axis] = True
        score.detail[axis] = (f"{axis} = {value} OFF-SCALE (raw, flagged scale_defect; "
                             f"excluded from aggregate, not clamped)")
    else:
        score.detail[axis] = f"{axis} = {value}"
