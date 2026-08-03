"""v4-A 2(c) — ranked-sacrifice scorer for hardened d05 allocation items (spec §2.2).

Spec 20260731j §2.2 (ratified `-20260731n`): hardened items are
infeasible-by-design — the budget cannot satisfy all constraints, so ≥ 1
constraint is always violated. The keyed object is a TOTAL PRIORITY ORDER over
the item's constraints ("sacrifice-first" order), independently double-keyed by
two authors; the disagreement rate is recorded and disclosed as an instrument
property, and disagreements are adjudicated before freeze.

Read-outs:
  PRIMARY   binary first-sacrifice match — defined whenever ≥ 1 constraint is
            violated; a fully compliant allocation on an infeasible-by-design
            item flags the ITEM, not the model.
  SECONDARY Kendall τ-b between the keyed sacrifice order and the observed
            sacrifice order, computed only where ≥ 3 constraints are violated;
            degenerate cases (0–2 violations, empty/non-compliant allocation)
            are excluded from the secondary and reported as counts.

Observed sacrifice order = violated constraints ranked by RELATIVE VIOLATION
SEVERITY (normalized shortfall against the constraint bound, most-violated =
sacrificed first). This is deterministic and judge-free: the model's single
allocation reveals how deeply each constraint was cut, and depth-of-cut is the
observable ordering of sacrifice. Ties in severity are kept as ties (τ-b
handles them; the primary accepts any member of the maximal-severity set).

Constraint identity: "C1".."Cn" = 1-based position in the parse order of the
pinned `ordo_constraints.parse_keyed_constraints` (authoring asserts
`unparsed_lines == []`, so positions are total and stable in a frozen bank).

Remedy-escape clauses whose numeric floor fails are UNDECIDABLE here exactly as
in the pinned checker (the rationale judge owns the escape): they join neither
the violated nor the satisfied set and are disclosed as a count. §2.2 requires
every hardened item to carry ≥ 1 hard NON-remedy-escaped floor, so the violated
set cannot be emptied by escapes on a spec-conformant item.

Pinned v3 components are imported read-only; this module is v4.0-line code
(spec §5.1) and becomes part of the next instrument id at freeze.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Tuple

from walkworthy_inspect.ordo_constraints import (
    Constraint,
    ParsedConstraints,
    parse_keyed_constraints,
)

KEY_FIELD = "ranked_sacrifice"  # lives at metadata.keyed.extras.ranked_sacrifice


# --------------------------------------------------------------------------- #
# keyed-object schema and double-keying discipline
# --------------------------------------------------------------------------- #
def constraint_ids(parsed: ParsedConstraints) -> List[str]:
    return [f"C{i + 1}" for i in range(parsed.n_parsed)]


def validate_key(ranked_key: Dict[str, Any], n_constraints: int) -> List[str]:
    """Authoring-time validation. Returns a list of defects (empty = valid).

    Required shape:
      {"keys": {"author1": [...], "author2": [...]}, "adjudicated": [...]}
    with every order a permutation of C1..Cn (a TOTAL order — spec §2.2).
    """
    errors: List[str] = []
    expected = set(f"C{i + 1}" for i in range(n_constraints))
    keys = (ranked_key or {}).get("keys") or {}
    for author in ("author1", "author2"):
        order = keys.get(author)
        if not order:
            errors.append(f"missing independent key: keys.{author}")
        elif set(order) != expected or len(order) != n_constraints:
            errors.append(
                f"keys.{author} is not a permutation of C1..C{n_constraints}: {order}")
    adjudicated = (ranked_key or {}).get("adjudicated")
    if not adjudicated:
        errors.append("missing adjudicated order")
    elif set(adjudicated) != expected or len(adjudicated) != n_constraints:
        errors.append(
            f"adjudicated is not a permutation of C1..C{n_constraints}: {adjudicated}")
    return errors


def key_disagreement(order1: Sequence[str], order2: Sequence[str]) -> Dict[str, Any]:
    """Disagreement between the two independent author keys (one item).

    pairwise_disagreement = normalized Kendall distance: the fraction of
    constraint pairs the two authors order differently.
    """
    if set(order1) != set(order2) or len(order1) != len(order2):
        raise ValueError("author keys must order the same constraint set")
    pos1 = {c: i for i, c in enumerate(order1)}
    pos2 = {c: i for i, c in enumerate(order2)}
    items = list(order1)
    n = len(items)
    discordant = 0
    npairs = n * (n - 1) // 2
    for i in range(n):
        for j in range(i + 1, n):
            a, b = items[i], items[j]
            if (pos1[a] - pos1[b]) * (pos2[a] - pos2[b]) < 0:
                discordant += 1
    return {
        "identical": list(order1) == list(order2),
        "first_sacrifice_agree": order1[0] == order2[0],
        "pairwise_disagreement": (discordant / npairs) if npairs else 0.0,
    }


def bank_key_disagreement(ranked_keys: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    """Instrument-property disclosure across a bank (spec §2.2: recorded and
    disclosed; disagreements adjudicated before freeze)."""
    per_item = []
    for rk in ranked_keys:
        keys = (rk or {}).get("keys") or {}
        per_item.append(key_disagreement(keys["author1"], keys["author2"]))
    n = len(per_item)
    return {
        "n_items": n,
        "identical_rate": (sum(1 for d in per_item if d["identical"]) / n) if n else None,
        "first_sacrifice_agreement_rate":
            (sum(1 for d in per_item if d["first_sacrifice_agree"]) / n) if n else None,
        "mean_pairwise_disagreement":
            (sum(d["pairwise_disagreement"] for d in per_item) / n) if n else None,
    }


# --------------------------------------------------------------------------- #
# Kendall tau-b (tie-aware; no scipy dependency)
# --------------------------------------------------------------------------- #
def kendall_tau_b(x: Sequence[float], y: Sequence[float]) -> Optional[float]:
    """τ-b = (nc − nd) / sqrt((n0 − n1)(n0 − n2)); None when undefined
    (fewer than 2 pairs, or either variable fully tied)."""
    n = len(x)
    if n != len(y) or n < 2:
        return None
    nc = nd = tx = ty = 0
    for i in range(n):
        for j in range(i + 1, n):
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            if dx == 0:
                tx += 1
            if dy == 0:
                ty += 1
            if dx != 0 and dy != 0:
                if dx * dy > 0:
                    nc += 1
                else:
                    nd += 1
    n0 = n * (n - 1) // 2
    denom = math.sqrt((n0 - tx) * (n0 - ty))
    if denom == 0:
        return None
    return (nc - nd) / denom


# --------------------------------------------------------------------------- #
# scoring
# --------------------------------------------------------------------------- #
@dataclass(frozen=True)
class RankedSacrificeResult:
    first_sacrifice_match: Optional[bool]     # PRIMARY (None = excluded/flag)
    primary_excluded_reason: Optional[str]
    tau_b: Optional[float]                    # SECONDARY (None = excluded)
    tau_excluded_reason: Optional[str]
    n_violated: int
    n_undecidable: int
    violated_ids: List[str] = field(default_factory=list)
    observed_order: List[str] = field(default_factory=list)  # most-violated first
    keyed_order: List[str] = field(default_factory=list)
    item_flag: Optional[str] = None           # authoring defect signal, not a model score


def _bound(values: Dict[str, Any], c: Constraint) -> Tuple[float, float]:
    """(lhs, rhs) mirroring the pinned checker: missing tokens count as 0."""
    def tok_sum(toks: Sequence[str]) -> float:
        total = 0.0
        for t in toks:
            v = values.get(t, 0)
            try:
                total += float(v)
            except (TypeError, ValueError):
                total += 0.0
        return total

    lhs = tok_sum(c.left)
    rhs = tok_sum(c.right) if isinstance(c.right, list) else float(c.right)
    return lhs, rhs


def _violation_severity(lhs: float, rhs: float, op: str) -> Optional[float]:
    """Normalized depth-of-cut; None when the constraint is satisfied."""
    if op in (">=", ">"):
        gap = rhs - lhs
        violated = (lhs < rhs) if op == ">=" else (lhs <= rhs)
    else:  # "<=" | "<"
        gap = lhs - rhs
        violated = (lhs > rhs) if op == "<=" else (lhs >= rhs)
    if not violated:
        return None
    return gap / max(abs(rhs), 1.0)


def score_ranked_sacrifice(values: Optional[Dict[str, Any]],
                           constraints_text: str,
                           tokens: List[str],
                           ranked_key: Dict[str, Any]) -> RankedSacrificeResult:
    """Score one allocation response against a ranked-sacrifice key.

    `values` is the parsed allocation (from the pinned
    `parsers.reparse_allocation_response(...).values`); empty/None means the
    response was non-compliant and both read-outs are excluded as counts.
    """
    parsed = parse_keyed_constraints(constraints_text, tokens)
    ids = constraint_ids(parsed)
    keyed_order = list((ranked_key or {}).get("adjudicated") or [])

    key_errors = validate_key(ranked_key, parsed.n_parsed)
    if key_errors:
        return RankedSacrificeResult(
            None, "invalid ranked-sacrifice key: " + "; ".join(key_errors),
            None, "invalid ranked-sacrifice key",
            0, 0, keyed_order=keyed_order,
            item_flag="invalid_key")

    if not values:
        return RankedSacrificeResult(
            None, "non_compliant_allocation", None, "non_compliant_allocation",
            0, 0, keyed_order=keyed_order)

    severities: Dict[str, float] = {}
    n_undecidable = 0
    for cid, c in zip(ids, parsed.constraints):
        lhs, rhs = _bound(values, c)
        sev = _violation_severity(lhs, rhs, c.op)
        if sev is None:
            continue
        if c.has_remedy_escape:
            # pinned-checker semantics: a failing remedy-escape floor is
            # UNDECIDABLE (the rationale judge owns the escape) — neither
            # violated nor satisfied here.
            n_undecidable += 1
            continue
        severities[cid] = sev

    violated = sorted(severities, key=lambda cid: (-severities[cid], ids.index(cid)))
    n_violated = len(violated)

    if n_violated == 0:
        # infeasible-by-design items cannot be fully satisfied: a compliant
        # allocation (or one whose every shortfall escaped to a remedy) flags
        # the ITEM, not the model (spec §2.2).
        flag = ("all_shortfalls_undecidable" if n_undecidable
                else "fully_compliant_on_infeasible_item")
        return RankedSacrificeResult(
            None, flag, None, "fewer_than_3_violations",
            0, n_undecidable, keyed_order=keyed_order, item_flag=flag)

    max_sev = severities[violated[0]]
    top_set = {cid for cid, s in severities.items() if s == max_sev}
    first_match = keyed_order[0] in top_set

    if n_violated >= 3:
        keyed_rank = {cid: i for i, cid in enumerate(keyed_order)}
        xs = [float(keyed_rank[cid]) for cid in violated]
        ys = [-severities[cid] for cid in violated]  # earlier sacrifice = deeper cut
        tau = kendall_tau_b(xs, ys)
        tau_reason = "tau_b_undefined_all_tied" if tau is None else None
    else:
        tau, tau_reason = None, "fewer_than_3_violations"

    return RankedSacrificeResult(
        first_match, None, tau, tau_reason,
        n_violated, n_undecidable,
        violated_ids=violated, observed_order=violated,
        keyed_order=keyed_order)
