"""WCF-Benchmark-v2 — grading pipeline hardening (EXPLORATORY).

This module holds the grade-parse pattern, the SUT-answer sanitizer, the
range-guarded grader wrapper, and the panel-median reducer used by
``wcf_tasks.py``. It exists so the fixes for session-4 critique-02
(GP-01/02/04/05/06/07/08) live in importable, unit-testable functions rather
than inline in the task file.

Design decisions (pinned by tests/test_grading.py):

* ``GRADE_PATTERN`` binds the LAST ``GRADE: N`` in the grader output (matching
  Inspect's ``DEFAULT_GRADE_PATTERN`` design and ``analysis/regrade_graders.py``
  last-match semantics), with a word-boundary guard so ``downGRADE:`` is not a
  verdict and a trailing ``(?!\\d)`` guard so ``GRADE: 1000`` does NOT truncate
  to ``100`` — a 4+-digit run simply fails to match and routes to unscored.
* Out-of-range parses (``0 <= v <= 100`` violated) and non-numeric values
  become ``Score.unscored()`` (NaN), mirroring ``regrade_graders.py:58`` — never
  a counted number and never coerced to ``0.0`` by ``value_to_float``.
* The WCF grading template uses CUSTOM structural markers ([BEGIN/END MODEL
  RESPONSE], [BEGIN/END SCENARIO/QUESTION], [BEGIN/END GOLD KEY AND RUBRIC],
  [BEGIN/END TRANSCRIPT]). Inspect's ``neutralize_structural_delimiters`` only
  rewrites [BEGIN/END DATA], so those custom markers pass through a SUT answer
  verbatim. ``defang_wcf_markers`` rewrites them (space -> dash) in the SUT
  answer (and, for episodes, in every assistant turn feeding the transcript)
  BEFORE the grader prompt is assembled, so a SUT cannot forge a second rubric
  block or close the response block early.
* The panel median records ``metadata["panel"] = {"n_valid": k, "values": [...]}``
  so the effective panel size and each grader's raw parsed value survive the
  reduction (GP-06 quorum signal + GP-07 provenance) without re-running graders.
"""

from __future__ import annotations

import copy
import math
import re
import statistics
from typing import Sequence

from inspect_ai.model import ChatMessageAssistant
from inspect_ai.scorer import Score, Scorer, Target, scorer, score_reducer
from inspect_ai.scorer import accuracy, stderr
from inspect_ai.scorer._reducer.types import ScoreReducer
from inspect_ai.solver import TaskState

# --------------------------------------------------------------------------- #
# GP-01 + GP-05 + GP-08 : last-match, word-bounded grade pattern.
# --------------------------------------------------------------------------- #
# Leading ``(?is).*`` (DOTALL) makes ``re.search`` bind to the LAST ``GRADE: N``
# (the grader is instructed to END with the grade). ``(?<!\w)GRADE(?!\w)`` blocks
# ``downGRADE:`` / ``upGRADE:`` prose. The trailing ``(?!\d)`` blocks 4+-digit
# runs from silently truncating to a valid-looking 3-digit grade (``GRADE: 1000``
# fails to match -> unscored, rather than becoming ``100``).
GRADE_PATTERN = r"(?is).*(?<!\w)GRADE(?!\w)\s*:\s*(\d{1,3})(?!\d)"

_GRADE_RE = re.compile(GRADE_PATTERN)

# --------------------------------------------------------------------------- #
# GP-02 : WCF template's custom structural markers (NOT covered by Inspect's
# neutralize_structural_delimiters, which only touches [BEGIN/END DATA]).
# --------------------------------------------------------------------------- #
# Match the literal marker words the WCF template uses to frame the grader
# prompt. A literal space (not \s) is intentional — matching \s would also match
# U+00A0 (NBSP) and let a SUT pre-neutralize its own output to dodge the guard,
# the same subtlety Inspect notes for its own delimiter regex. We rewrite the
# space to a dash so the marker can no longer close/open a structural block.
_WCF_MARKER_RE = re.compile(
    r"\[(BEGIN|END) (MODEL FINAL RESPONSE|MODEL RESPONSE|SCENARIO/QUESTION|"
    r"GOLD KEY AND RUBRIC|TRANSCRIPT)\]",
    re.IGNORECASE,
)


def defang_wcf_markers(text: str) -> str:
    """Rewrite the WCF template's own structural markers so a SUT answer cannot
    forge them. ``[END MODEL RESPONSE]`` -> ``[END-MODEL-RESPONSE]`` etc.

    Idempotent: the dash form no longer matches ``_WCF_MARKER_RE``.
    """
    if not text:
        return text
    return _WCF_MARKER_RE.sub(lambda m: m.group(0).replace(" ", "-"), text)


def parse_grade(text: str) -> int | None:
    """Return the LAST in-range ``GRADE: N`` (0..100) in ``text``, else None.

    Single source of truth for grade parsing. Combines GP-01/05/08 (last match,
    word boundary, no digit-truncation) with GP-04 (0..100 range guard).
    """
    m = _GRADE_RE.search(text or "")
    if not m:
        return None
    val = int(m.group(1))
    return val if 0 <= val <= 100 else None


def _score_to_grade(score: Score) -> int | None:
    """Coerce a grader Score's value to an in-range int grade, or None.

    Handles both the string values Inspect's ``model_graded_qa`` returns
    (``match.group(1)``) and any already-numeric value. Non-numeric or
    out-of-range -> None (so it becomes unscored rather than ``value_to_float``'s
    silent ``0.0``).
    """
    v = score.value
    if isinstance(v, bool):  # bool is an int subclass; reject explicitly
        return None
    if isinstance(v, (int, float)):
        if isinstance(v, float) and math.isnan(v):
            return None
        fv = float(v)
        if fv.is_integer() and 0 <= fv <= 100:
            return int(fv)
        return None
    if isinstance(v, str):
        s = v.strip()
        if re.fullmatch(r"\d{1,3}", s):
            iv = int(s)
            return iv if 0 <= iv <= 100 else None
        return None
    return None


# --------------------------------------------------------------------------- #
# GP-02 : sanitize the SUT answer (and episode transcript) before grading.
# --------------------------------------------------------------------------- #
def _sanitize_state_for_grading(state: TaskState) -> TaskState:
    """Return a deep copy of ``state`` with the WCF markers defanged in the SUT
    output completion and in every assistant message (so an episode transcript
    injected mid-turn is also neutralized). The original state is untouched.
    """
    s = copy.deepcopy(state)
    try:
        s.output.completion = defang_wcf_markers(s.output.completion)
    except Exception:  # pragma: no cover - defensive; output always present here
        pass
    for msg in s.messages:
        if isinstance(msg, ChatMessageAssistant) and isinstance(msg.text, str):
            msg.text = defang_wcf_markers(msg.text)
    return s


# Session-7 grader-transient rule (Phase-0, 2026-07-16): the gemini-2.5-flash
# g1 grader dropped ~4% of samples in s6 and 8.7% in the s7 gate run — a
# provider transient, evenly spread. Per the pre-stated rule, a grader whose
# parsed grade comes back invalid is retried up to 2 more times (fresh calls)
# before it is recorded as unscored. Grading SEMANTICS are unchanged: valid
# grades are never re-rolled, and a persistent failure still yields unscored
# (dropped from the panel median, never coerced to 0).
GRADER_ATTEMPTS = 3


def bounded_grader(inner: Scorer) -> Scorer:
    """Wrap a ``model_graded_qa`` scorer so that (a) the SUT answer is sanitized
    against WCF-marker injection before grading (GP-02) and (b) the parsed grade
    is range-guarded to 0..100 -> else ``Score.unscored()`` (GP-04/06 non-numeric
    and out-of-range never become a counted 0 or an inflating >100), with (c) up
    to ``GRADER_ATTEMPTS-1`` retries of the inner scorer on an invalid grade or
    provider exception (s7 Phase-0 transient rule) before unscored is recorded.

    The grading transcript metadata from the inner scorer is preserved so audit
    still works; only the value is replaced with NaN when invalid.
    """

    @scorer(metrics=[accuracy(), stderr()])
    def _wrapped() -> Scorer:
        async def score(state: TaskState, target: Target) -> Score:
            sanitized = _sanitize_state_for_grading(state)
            inner_score, grade, err = None, None, None
            for attempt in range(GRADER_ATTEMPTS):
                try:
                    inner_score = await inner(sanitized, target)
                except Exception as exc:  # provider transient — retry
                    err = exc
                    continue
                grade = _score_to_grade(inner_score)
                if grade is not None:
                    break
            if inner_score is None:  # every attempt raised
                return Score.unscored(
                    metadata={"unscored_reason": f"grader_exception: {err!r}"}
                )
            if grade is None:
                return Score.unscored(
                    answer=inner_score.answer,
                    explanation=inner_score.explanation,
                    metadata={
                        **(inner_score.metadata or {}),
                        "unscored_reason": (inner_score.metadata or {}).get(
                            "unscored_reason", "grade_out_of_range_or_nonnumeric"
                        ),
                    },
                )
            return Score(
                value=grade,
                answer=inner_score.answer,
                explanation=inner_score.explanation,
                metadata=inner_score.metadata,
            )

        return score

    return _wrapped()


# --------------------------------------------------------------------------- #
# GP-06 + GP-07 : explicit panel-median reducer with provenance metadata.
# --------------------------------------------------------------------------- #
def panel_median_reduce(scores: Sequence[Score]) -> Score:
    """Reduce a panel of grader Scores to their median, recording panel
    provenance in ``metadata["panel"]``. Plain function (no registry) so tests
    call it directly; the registered reducer ``panel_median`` wraps it.

    * Non-numeric / NaN / out-of-range values are treated as unscored (dropped
      from the median), NEVER coerced to 0.0 (GP-06).
    * ``metadata["panel"] = {"n_valid": k, "values": [...]}`` records the
      effective panel size and each grader's parsed value (None for dropped
      graders) so a degraded panel is visible and per-grader values survive the
      reduction without a re-run (GP-06 quorum signal + GP-07 provenance).
    * Median semantics are identical to Inspect's ``median`` reducer for the
      all-valid case (``statistics.median`` — mean of the middle two for even n).
    """
    scores = list(scores)
    per_grader: list[int | None] = [_score_to_grade(s) for s in scores]
    valid = [g for g in per_grader if g is not None]

    base_meta = dict(scores[0].metadata or {}) if scores else {}
    base_meta["panel"] = {"n_valid": len(valid), "values": per_grader}

    if not valid:
        return Score(
            value=float("nan"),
            answer=scores[0].answer if scores else None,
            explanation=scores[0].explanation if scores else None,
            metadata=base_meta,
        )

    med = statistics.median(valid)
    return Score(
        value=med,
        answer=scores[0].answer if scores else None,
        explanation=scores[0].explanation if scores else None,
        metadata=base_meta,
    )


@score_reducer(name="panel_median")
def panel_median() -> ScoreReducer:
    """Registered ``median`` panel reducer with WCF quorum/provenance metadata.

    Explicit median (NOT Inspect's ``model=[...]`` mode reducer — mode is
    degenerate on continuous 0..100 grades). ``multi_scorer(scorers,
    panel_median())`` uses this.
    """

    def reduce(scores: list[Score]) -> Score:
        return panel_median_reduce(scores)

    return reduce
