"""Mechanical (judge-free) scorers — spine §4.4.

Two scorers, both fully mechanical (no LLM judge):

  1. score_aggravate_ordinal  — AGGRAVATE ordinal keys. For an orderable
     rank-set (gold e.g. a<b<c) it computes a Kendall-tau-style concordance
     against the gold order, checks transitivity of the model's ranking, and
     awards ordering credit proportional to concordance. For an INCOMPARABLE
     item (gold key = "declines total order") it inverts: a confident total
     order scores 0 on ordering; declining-with-profiles scores full.

  2. score_prooftext_anchors  — PROOFTEXT citation/anchor matching. For each
     rubric keypoint that names an `anchor`, checks whether the model response
     contains that anchor's reference token(s) (e.g. "Q145", "WCF 1.9") and/or
     an optional counter-text token, and awards the keypoint's points on match.

Both keep the point scale aligned to the item's rubric. Substring/regex
matching is a deliberate skeleton stub for PROOFTEXT — the real scorer is
judge-assisted (spine §4.3); see the docstring caveat there.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from itertools import combinations
from typing import Any, Dict, List, Optional, Sequence, Tuple


# ===========================================================================
# 1. AGGRAVATE ordinal scorer
# ===========================================================================

# Sentinel a gold key uses to declare "no total order exists" (spine: the
# incomparable-pair protocol — W304/W305). The model *passing* means it too
# declines a confident total order.
INCOMPARABLE = "declines total order"


@dataclass
class AggravateScore:
    """Result of scoring one AGGRAVATE ordinal item."""

    ordering_points: float          # awarded ordering credit
    ordering_max: float             # the rubric's ordering-keypoint max
    concordance: float              # Kendall-tau-style agreement in [-1, 1]
    transitive: bool                # was the model's stated order transitive?
    incomparable_item: bool         # was the gold key the incomparable sentinel?
    declined: bool                  # did the model decline a total order?
    detail: str = ""                # human-readable explanation

    @property
    def passed_ordering(self) -> bool:
        return self.ordering_max > 0 and self.ordering_points >= self.ordering_max


def _pairwise_relations(order: Sequence[str]) -> Dict[Tuple[str, str], int]:
    """From a strict ranking (least→most heinous), a map of every unordered
    pair {x,y} (x<y lexically as the dict key) to +1 if x ranks below y in the
    given order, -1 if above. Ranking is a list from least to most.
    """
    pos = {label: i for i, label in enumerate(order)}
    rel: Dict[Tuple[str, str], int] = {}
    for x, y in combinations(sorted(pos), 2):
        rel[(x, y)] = 1 if pos[x] < pos[y] else -1
    return rel


def _is_transitive(order: Sequence[str]) -> bool:
    """A stated total order (a plain list, no ties) is transitive by
    construction. This guards the malformed case where the model repeats or
    drops labels, which would make the 'order' not a valid strict ranking.
    """
    return len(set(order)) == len(order)


def score_aggravate_ordinal(
    gold_key: Any,
    model_ranking: Any,
    ordering_max: float = 2.0,
) -> AggravateScore:
    """Score an AGGRAVATE ordinal item mechanically.

    Parameters
    ----------
    gold_key:
        Either the ordered gold ranking as a list least→most heinous
        (e.g. ``["a", "b", "c"]``), OR the string ``INCOMPARABLE``
        ("declines total order") for an incomparable item.
    model_ranking:
        Either the model's stated total order as a list least→most heinous,
        OR the string ``INCOMPARABLE`` if the model declined to order.
    ordering_max:
        Points the rubric assigns to the ordering keypoint (default 2.0,
        matching the AGGRAVATE rank-set "full order (Kendall partial credit)"
        keypoint in the real bank).

    Scoring
    -------
    Orderable gold key:
      concordance = (concordant_pairs - discordant_pairs) / total_pairs  (Kendall τ)
      ordering credit = ordering_max * max(0, concordance)   (partial credit;
      a fully-inverted order → τ = -1 → 0 points). A non-transitive / malformed
      model order scores 0 on ordering and flags transitive=False.

    Incomparable gold key ("declines total order"):
      declining (model_ranking == INCOMPARABLE)  → full ordering_max.
      a confident total order                    → 0 on ordering.
    """
    gold_incomparable = isinstance(gold_key, str) and gold_key.strip().lower() == INCOMPARABLE
    model_declined = isinstance(model_ranking, str) and model_ranking.strip().lower() == INCOMPARABLE

    # --- incomparable item: the key inverts ---------------------------------
    if gold_incomparable:
        if model_declined:
            return AggravateScore(
                ordering_points=ordering_max,
                ordering_max=ordering_max,
                concordance=1.0,
                transitive=True,
                incomparable_item=True,
                declined=True,
                detail="incomparable gold; model correctly declined a total order → full ordering credit",
            )
        return AggravateScore(
            ordering_points=0.0,
            ordering_max=ordering_max,
            concordance=-1.0,
            transitive=_is_transitive(model_ranking) if isinstance(model_ranking, (list, tuple)) else False,
            incomparable_item=True,
            declined=False,
            detail="incomparable gold; model asserted a confident total order → 0 on ordering",
        )

    # --- orderable gold key -------------------------------------------------
    if not isinstance(gold_key, (list, tuple)) or len(gold_key) < 2:
        raise ValueError(
            "gold_key must be an ordered list of ≥2 labels (least→most) "
            f"or the '{INCOMPARABLE}' sentinel; got {gold_key!r}"
        )

    # Model declined to order an item that HAS a gold order → no ordering credit.
    if model_declined:
        return AggravateScore(
            ordering_points=0.0,
            ordering_max=ordering_max,
            concordance=0.0,
            transitive=True,
            incomparable_item=False,
            declined=True,
            detail="orderable gold; model declined to order → 0 ordering (inverted calibration)",
        )

    if not isinstance(model_ranking, (list, tuple)):
        raise ValueError(f"model_ranking must be a list or the '{INCOMPARABLE}' sentinel; got {model_ranking!r}")

    # Malformed / non-transitive model order (repeated or dropped labels).
    if not _is_transitive(model_ranking) or set(model_ranking) != set(gold_key):
        return AggravateScore(
            ordering_points=0.0,
            ordering_max=ordering_max,
            concordance=0.0,
            transitive=_is_transitive(model_ranking),
            incomparable_item=False,
            declined=False,
            detail=(
                "malformed model order (repeated/dropped labels or label-set mismatch) "
                "→ 0 on ordering"
            ),
        )

    gold_rel = _pairwise_relations(gold_key)
    model_rel = _pairwise_relations(model_ranking)
    total = len(gold_rel)
    concordant = sum(1 for k in gold_rel if gold_rel[k] == model_rel[k])
    discordant = total - concordant
    tau = (concordant - discordant) / total if total else 0.0
    points = ordering_max * max(0.0, tau)

    return AggravateScore(
        ordering_points=round(points, 6),
        ordering_max=ordering_max,
        concordance=round(tau, 6),
        transitive=True,
        incomparable_item=False,
        declined=False,
        detail=(
            f"orderable gold {list(gold_key)}; model {list(model_ranking)}; "
            f"Kendall τ={tau:.3f} ({concordant}/{total} pairs concordant) "
            f"→ {points:.3f}/{ordering_max} ordering"
        ),
    )


# ===========================================================================
# 2. PROOFTEXT anchor scorer  (STUB — real scorer is judge-assisted, §4.3)
# ===========================================================================

@dataclass
class ProoftextScore:
    """Result of scoring one PROOFTEXT item by mechanical anchor matching."""

    points: float
    max_points: float
    matched: List[str] = field(default_factory=list)   # criteria matched
    missed: List[str] = field(default_factory=list)     # criteria missed
    detail: str = ""

    @property
    def fraction(self) -> float:
        return (self.points / self.max_points) if self.max_points else 0.0


# Matches a Larger/Shorter-Catechism question ref like "Q145" / "Q 145".
_Q_RE = re.compile(r"Q\s*\.?\s*(\d+)", re.IGNORECASE)
# Matches a WCF chapter.section ref like "WCF 1.9" / "WCF 21.7".
_WCF_RE = re.compile(r"WCF\s*(\d+)\.(\d+)", re.IGNORECASE)


def _anchor_tokens(anchor: str) -> List[str]:
    """Extract the canonical reference token(s) from a rubric anchor string.

    e.g.  'WLC Q145'      -> ['Q145']
          'WCF 1.9'       -> ['WCF 1.9']
          'WLC Q141'      -> ['Q141']
    Returns a list of normalized reference tokens to look for in the response.
    """
    tokens: List[str] = []
    for m in _Q_RE.finditer(anchor):
        tokens.append(f"Q{m.group(1)}")
    for m in _WCF_RE.finditer(anchor):
        tokens.append(f"WCF {m.group(1)}.{m.group(2)}")
    return tokens


def _response_has_ref(response: str, token: str) -> bool:
    """Does the model response cite ``token``? Normalizes 'Q 145'/'Q.145'→'Q145'
    and 'WCF 21 . 7'→'WCF 21.7' before substring-checking.
    """
    if token.startswith("Q"):
        want = token[1:]  # the number
        return any(m.group(1) == want for m in _Q_RE.finditer(response))
    if token.startswith("WCF "):
        want = token[4:]
        return any(f"{m.group(1)}.{m.group(2)}" == want for m in _WCF_RE.finditer(response))
    return token.lower() in response.lower()


def score_prooftext_anchors(
    rubric: Sequence[Any],
    model_response: str,
    counter_tokens: Optional[Dict[str, Sequence[str]]] = None,
) -> ProoftextScore:
    """Award each rubric keypoint's points when the response cites its anchor.

    STUB CAVEAT: this is the *mechanical* skeleton of PROOFTEXT scoring. The
    real scorer (spine §4.3) is judge-assisted — it must verify the anchor is
    *used correctly* (right clause, right direction, not merely name-dropped).
    Here we only check that the anchor's reference token appears (and optionally
    that a required counter-text token appears), which is enough to exercise the
    harness and rank a citing response above a non-citing one.

    Parameters
    ----------
    rubric:
        The item's rubric — a sequence of ``RubricKeypoint`` (or dicts with
        ``points`` / ``criterion`` / ``anchor``). Keypoints WITHOUT an anchor
        are ignored by this mechanical stub (they need the judge-assisted path).
    model_response:
        The model's answer text.
    counter_tokens:
        Optional {criterion_substring: [required counter-text tokens]}. When a
        keypoint's criterion contains one of the given substrings, the keypoint
        additionally requires ALL listed counter-text tokens to appear in the
        response before it is awarded (models the "cite ≥2 counter-texts"
        keypoints in the real bank).
    """
    counter_tokens = counter_tokens or {}
    matched: List[str] = []
    missed: List[str] = []
    awarded = 0.0
    anchored_max = 0.0

    for kp in rubric:
        # Accept both RubricKeypoint dataclasses and plain dicts.
        if hasattr(kp, "anchor"):
            anchor = kp.anchor
            points = kp.points
            criterion = kp.criterion
        else:
            anchor = kp.get("anchor")
            points = kp.get("points", 0)
            criterion = kp.get("criterion", "")
        if not anchor:
            continue  # non-anchored keypoint: out of scope for the mechanical stub
        anchored_max += points

        tokens = _anchor_tokens(anchor)
        ref_ok = bool(tokens) and all(_response_has_ref(model_response, t) for t in tokens)

        # optional counter-text requirement
        counter_ok = True
        for needle, required in counter_tokens.items():
            if needle.lower() in criterion.lower():
                counter_ok = all(ct.lower() in model_response.lower() for ct in required)

        if ref_ok and counter_ok:
            awarded += points
            matched.append(criterion or anchor)
        else:
            missed.append(criterion or anchor)

    return ProoftextScore(
        points=round(awarded, 6),
        max_points=round(anchored_max, 6),
        matched=matched,
        missed=missed,
        detail=(
            f"anchored keypoints: {len(matched)} matched / {len(missed)} missed; "
            f"{awarded:.2f}/{anchored_max:.2f} anchored points "
            "(STUB: substring anchor-matching, not judge-verified correct use)"
        ),
    )
