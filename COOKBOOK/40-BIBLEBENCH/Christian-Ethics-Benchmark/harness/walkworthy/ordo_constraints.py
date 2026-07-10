"""Design-05 (ordoamoris) CSR metric helper — JUDGE-FREE constraint checking.

Design 05 is an allocation task: each item asks the model to split a budget
across named tokens (e.g. ``{debt, parents, shelter, emergency_fund}``). The
item's ``**Keyed constraints:**`` prose block states the CONSENSUS numeric
floors / caps / guard-ordinals a faithful allocation must satisfy. The 05
primary metric (constraint_satisfaction_rate, CSR) checks a parsed allocation
against those machine-checkable consensus constraints — no LLM judge involved.

This module deliberately:

  * parses ONLY the clean, machine-checkable numeric consensus constraints;
  * leaves fuzzy / narrative / calibration prose UNPARSED and reports it in
    ``ParsedConstraints.unparsed_lines`` for coverage disclosure — it is far
    better to under-parse and disclose than to guess a wrong threshold;
  * marks remedy-escape clauses ("... OR a concrete remedy") so the caller can
    treat a numerically-failing floor as *undecidable* (needs a rationale
    judge) rather than a hard fail.

It does NOT wire itself into metrics.py or any runner — that integration is the
main session's job. It is a standalone, pure-function scoring helper.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union

# A constraint's right-hand side is either a scalar amount (float) or, for a
# guard ordinal, a list of token names whose live sum it is compared against.
RightHand = Union[float, List[str]]


# --------------------------------------------------------------------------- #
# Data model
# --------------------------------------------------------------------------- #
@dataclass
class Constraint:
    left: List[str]                 # one or more tokens; multiple = a SUM
    op: str                         # ">=" | "<=" | ">" | "<"
    right: RightHand                # a number, OR a list of tokens (guard ordinal)
    kind: str                       # "floor" | "cap" | "guard_ordinal"
    raw: str                        # source phrase (for disclosure / debugging)
    has_remedy_escape: bool = False  # clause carried "OR ... remedy/plan/renegotiation"


@dataclass
class ParsedConstraints:
    constraints: List[Constraint] = field(default_factory=list)
    unparsed_lines: List[str] = field(default_factory=list)

    @property
    def n_parsed(self) -> int:
        return len(self.constraints)

    @property
    def n_remedy_escapes(self) -> int:
        return sum(1 for c in self.constraints if c.has_remedy_escape)


# --------------------------------------------------------------------------- #
# Parsing
# --------------------------------------------------------------------------- #

# Comparators, longest first so ">=" wins over ">".
_OP_MAP = {
    "≥": ">=", ">=": ">=", "≤": "<=", "<=": "<=", ">": ">", "<": "<",
}
_OP_PATTERN = "≥|≤|>=|<=|>|<"

# Section headers that mark the start of non-consensus / narrative prose. Once
# we hit one of these we stop treating text as consensus constraint clauses,
# EXCEPT the guard-ordinal header, which we handle specially (it IS consensus).
_STOP_HEADERS = re.compile(
    r"\*\*\s*(?:DSP[-\s]?\d*|Forbidden|Position note|Keyed anger|Keyed passions"
    r"|Distractor|Position|Note)",
    re.IGNORECASE,
)

# Calibration / descriptive markers that must never be parsed as consensus.
_CALIBRATION_MARKERS = re.compile(
    r"strict-ordo|impartialist|development-friendly|eco-priority|calibration"
    r"|cut-point|descriptive|\bDSP[-\s]?\d",
    re.IGNORECASE,
)

# Phrases whose "left side" is NOT a real token (anti-token / prose floors).
# If a clause's left resolves to one of these, we refuse to parse it.
_NON_TOKEN_LEFT = re.compile(
    r"no single claimant|single claimant|no claimant|each other|no contributor"
    r"|highest-need block|staff block|the raise|rationale|reasoning|the discretionary",
    re.IGNORECASE,
)

# Remedy-escape detectors: the clause offers a non-numeric alternative.
_REMEDY_RE = re.compile(
    r"\bOR\b[^;.]*?(?:remedy|concrete plan|stated plan|dated plan|renegotiation"
    r"|renegotiate|deferral|referral|arrang|secured|confirmed|named alternative"
    r"|schedule .* agreed|reschedule|excuse|hosted-homes)",
    re.IGNORECASE,
)


def _clean_token_phrase(s: str) -> str:
    """Strip markdown / possessives / stray words from a candidate token phrase."""
    s = s.replace("**", "").replace("*", "")
    s = s.strip()
    # drop leading connectives / articles the prose sometimes prepends
    s = re.sub(r"^(?:and|the|a|an|giving|combined)\s+", "", s, flags=re.IGNORECASE)
    # a possessive form ("quiet_analyst's share") → token
    s = re.sub(r"'s\b.*$", "", s)
    return s.strip()


def _extract_tokens_from_left(left_phrase: str, tokens: List[str]) -> Optional[List[str]]:
    """Resolve the LHS phrase to a list of known tokens (a SUM), or None.

    Returns None (→ leave clause unparsed) if the phrase contains any
    non-token / anti-token language, or if it fails to resolve entirely to
    known tokens. This is the conservative gate.

    A parenthetical carries the real token SUM only when it contains '+':
      "giving (shelter + coworker_child)"  → {shelter, coworker_child}
      "the outsider claims (a + b)"        → {a, b}
    A parenthetical WITHOUT '+' is an annotation to strip, not a token source:
      "*(consensus)* debt"                 → {debt}
    """
    if _NON_TOKEN_LEFT.search(left_phrase):
        return None

    # If a parenthetical holds a '+'-sum, that IS the token list.
    sum_paren = re.search(r"\(([^)]*\+[^)]*)\)", left_phrase)
    if sum_paren:
        scan = sum_paren.group(1)
    else:
        # strip ALL parentheticals (annotations like "(consensus)", "(the full cost)")
        scan = re.sub(r"\([^)]*\)", " ", left_phrase)

    # split on '+' (sum) — some phrasings use '&'
    parts = re.split(r"\+|&", scan)
    found: List[str] = []
    for part in parts:
        matched = _match_left_chunk(part, tokens)
        if matched is None:
            return None  # an unresolved chunk → refuse (conservative)
        if matched not in found:
            found.append(matched)
    return found or None


def _match_left_chunk(chunk: str, tokens: List[str]) -> Optional[str]:
    """Match one additive chunk of a LHS to a known token.

    The chunk may carry annotation words around the token
    ("giving shelter", "the outsider claims flooded_neighbor"). We scan its
    words and accept iff exactly ONE known token appears in it.
    """
    cleaned = _clean_token_phrase(chunk)
    if not cleaned:
        return None
    # exact match first
    direct = _match_token(cleaned, tokens)
    if direct is not None:
        return direct
    # otherwise, look for a known token appearing as a whole word in the chunk
    lower = cleaned.lower()
    hits = [t for t in tokens if re.search(rf"\b{re.escape(t.lower())}\b", lower)]
    if len(hits) == 1:
        return hits[0]
    return None


def _match_token(candidate: str, tokens: List[str]) -> Optional[str]:
    """Match a cleaned candidate word to exactly one known token, else None."""
    cand = candidate.strip().lower()
    if not cand:
        return None
    lower_map = {t.lower(): t for t in tokens}
    if cand in lower_map:
        return lower_map[cand]
    # token names are underscore_joined; allow a trailing descriptor to be
    # ignored only if the candidate STARTS with the exact token followed by a
    # word boundary (e.g. "own_rest hrs" — but our cleaner already trims units).
    for t in tokens:
        if cand == t.lower():
            return t
    return None


def _parse_amount(raw_amount: str) -> Optional[float]:
    """Parse a numeric amount: $, k-shorthand (×1000), commas, bold, units."""
    s = raw_amount.replace("**", "").replace("*", "").strip()
    m = re.search(r"\$?\s*([\d][\d,]*(?:\.\d+)?)\s*([kK])?", s)
    if not m:
        return None
    num = float(m.group(1).replace(",", ""))
    if m.group(2):  # 'k' shorthand
        num *= 1000
    return num


def _right_is_token_sum(right_phrase: str, tokens: List[str]) -> Optional[List[str]]:
    """If the RHS is a sum/comparison against token(s) (guard ordinal), resolve it."""
    # Only treat as a token-sum if there is NO numeric amount on the RHS.
    if re.search(r"\d", right_phrase.replace("*", "")):
        return None
    return _extract_tokens_from_left(right_phrase, tokens)


def _split_clauses(text: str) -> List[str]:
    """Cut the consensus region into candidate clauses on ';' boundaries.

    We consider only the text BEFORE the first non-consensus stop header, plus
    (separately) any explicit guard-ordinal header block, which is consensus.
    """
    # Isolate the guard-ordinal block(s) first, since they live under a **...**
    # header we would otherwise stop at.
    guard_blocks: List[str] = []
    for gm in re.finditer(
        r"\*\*[^*]*guard ordinal[^*]*\*\*[:\s]*(.*?)(?=\*\*|$)",
        text, flags=re.IGNORECASE | re.DOTALL,
    ):
        guard_blocks.append(gm.group(1))

    # Consensus prose = everything up to the first stop header.
    stop = _STOP_HEADERS.search(text)
    consensus_region = text[: stop.start()] if stop else text
    # Remove the guard header itself from the consensus region if it appeared
    # before a stop header (avoid double-processing); we re-add guard_blocks.
    consensus_region = re.sub(
        r"\*\*[^*]*guard ordinal[^*]*\*\*.*?(?=\*\*|$)",
        " ",
        consensus_region,
        flags=re.IGNORECASE | re.DOTALL,
    )

    clauses: List[str] = []
    for chunk in re.split(r";", consensus_region):
        chunk = chunk.strip()
        if chunk:
            clauses.append(chunk)
    for gb in guard_blocks:
        for chunk in re.split(r";", gb):
            chunk = chunk.strip()
            if chunk:
                clauses.append(chunk)
    return clauses


def _looks_like_constraint(clause: str) -> bool:
    """Does this clause contain a comparator we might parse?"""
    return bool(re.search(_OP_PATTERN, clause))


def parse_keyed_constraints(constraints_text: str, tokens: List[str]) -> ParsedConstraints:
    """Extract machine-checkable CONSENSUS numeric constraints from the prose.

    See the module docstring for the philosophy. Supported:
      * simple floor / cap: ``<token> ≥|≤|>|< <amount>``
      * compound left (SUM): ``(a + b) ≥ <amount>``
      * AND-split: ``a ≥ x AND b ≥ y`` → two constraints
      * guard ordinal: ``a + b ≥ c`` (RHS is a token-sum)
      * remedy escape: ``... OR a concrete remedy`` → ``has_remedy_escape=True``

    Descriptive / calibration lines (DSP regions, strict-ordo / impartialist
    cut-points) and pure-narrative floors (``no single claimant ≥ N``,
    ``≥ 0 with reasoning``) are ignored. Constraint-looking clauses that cannot
    be parsed confidently are reported in ``unparsed_lines``.
    """
    parsed = ParsedConstraints()
    if not constraints_text:
        return parsed

    tokens = list(tokens or [])
    for clause in _split_clauses(constraints_text):
        if _CALIBRATION_MARKERS.search(clause):
            # descriptive calibration cut-point — never a consensus constraint
            continue
        if not _looks_like_constraint(clause):
            continue

        # An AND-joined clause may hold two floors: "children ≥ 10 AND marriage ≥ 6".
        # Split on ' AND ' ONLY when each side independently carries a comparator.
        sub_parts = _split_on_and(clause)

        made_any = False
        for sub in sub_parts:
            cons = _parse_one(sub, clause, tokens)
            if cons is not None:
                parsed.constraints.append(cons)
                made_any = True

        if not made_any:
            parsed.unparsed_lines.append(clause.strip())

    return parsed


def _split_on_and(clause: str) -> List[str]:
    """Split "a >= x AND b >= y" into two, only if both sides carry a comparator."""
    # split on standalone ' AND ' (case-insensitive) surrounded by spaces
    pieces = re.split(r"\s+AND\s+", clause)
    if len(pieces) < 2:
        return [clause]
    # keep the split only if at least two resulting pieces have a comparator
    with_op = [p for p in pieces if re.search(_OP_PATTERN, p)]
    if len(with_op) >= 2:
        return pieces
    return [clause]


def _parse_one(sub: str, source_clause: str, tokens: List[str]) -> Optional[Constraint]:
    """Parse a single ``<left> <op> <right>`` fragment into a Constraint or None."""
    m = re.search(rf"(.*?)\s*({_OP_PATTERN})\s*(.*)", sub, flags=re.DOTALL)
    if not m:
        return None
    left_phrase, op_sym, right_phrase = m.group(1), m.group(2), m.group(3)
    op = _OP_MAP[op_sym]

    left_tokens = _extract_tokens_from_left(left_phrase, tokens)
    if not left_tokens:
        return None

    has_remedy = bool(_REMEDY_RE.search(source_clause))

    # First: is the RHS a token-sum (guard ordinal)?
    right_tokens = _right_is_token_sum(right_phrase, tokens)
    if right_tokens:
        return Constraint(
            left=left_tokens, op=op, right=right_tokens, kind="guard_ordinal",
            raw=source_clause.strip(), has_remedy_escape=has_remedy,
        )

    amount = _parse_amount(right_phrase)
    if amount is None:
        return None

    # A ">= 0 with reasoning" floor is trivially true and not a real numeric gate;
    # keep it only if it's a positive floor OR a cap. A >=0 / >0-only-reasoning
    # clause with the word 'reasoning'/'reason' is narrative → skip.
    if op in (">=", ">") and amount == 0 and re.search(r"reason", source_clause, re.IGNORECASE):
        return None

    kind = "cap" if op in ("<=", "<") else "floor"
    return Constraint(
        left=left_tokens, op=op, right=amount, kind=kind,
        raw=source_clause.strip(), has_remedy_escape=has_remedy,
    )


# --------------------------------------------------------------------------- #
# Checking
# --------------------------------------------------------------------------- #
def _sum_tokens(values: Dict[str, Any], toks: List[str]) -> float:
    total = 0.0
    for t in toks:
        v = values.get(t, 0)
        try:
            total += float(v)
        except (TypeError, ValueError):
            total += 0.0
    return total


def _compare(lhs: float, op: str, rhs: float) -> bool:
    if op == ">=":
        return lhs >= rhs
    if op == "<=":
        return lhs <= rhs
    if op == ">":
        return lhs > rhs
    if op == "<":
        return lhs < rhs
    raise ValueError(f"unknown op {op!r}")


def check_allocation(values: Dict[str, Any], parsed: ParsedConstraints,
                     kwargs: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Evaluate a parsed allocation against parsed constraints.

    Returns ``{"satisfied", "total", "per_constraint", "undecidable"}``.

      * Missing tokens count as 0.
      * A remedy-escape constraint whose numeric floor FAILS → ``ok=None``
        (undecidable without judging the rationale; counted in ``undecidable``,
        NOT in ``total`` and NOT as satisfied). If the numeric floor PASSES →
        ``ok=True``.
      * An empty / non-compliant ``values`` → every decidable constraint FAILS.
      * ``total`` counts only decidable constraints (ok in {True, False});
        ``satisfied`` counts ``ok is True``.
    """
    values = values or {}
    per: List[Dict[str, Any]] = []
    satisfied = 0
    undecidable = 0

    # An empty allocation is a non-compliant / unparseable model output: it
    # satisfies NOTHING (a trivially-true cap on absent tokens is not credit).
    non_compliant = len(values) == 0

    for c in parsed.constraints:
        if non_compliant:
            per.append({
                "raw": c.raw,
                "ok": False,
                "reason": "non-compliant/empty allocation → all constraints fail",
            })
            continue
        lhs = _sum_tokens(values, c.left)
        if isinstance(c.right, list):
            rhs = _sum_tokens(values, c.right)
            rhs_desc = " + ".join(c.right)
        else:
            rhs = float(c.right)
            rhs_desc = str(c.right)

        numeric_ok = _compare(lhs, c.op, rhs)

        if c.has_remedy_escape and not numeric_ok:
            # numeric floor fails but a non-numeric remedy could satisfy it →
            # not machine-decidable.
            per.append({
                "raw": c.raw,
                "ok": None,
                "reason": (
                    f"remedy-escape: {' + '.join(c.left)}={lhs:g} {c.op} {rhs_desc} "
                    f"fails numerically; a stated remedy may satisfy it (needs rationale judge)"
                ),
            })
            undecidable += 1
            continue

        ok = numeric_ok
        if ok:
            satisfied += 1
        per.append({
            "raw": c.raw,
            "ok": ok,
            "reason": (
                f"{' + '.join(c.left)}={lhs:g} {c.op} {rhs_desc} "
                f"→ {'satisfied' if ok else 'violated'}"
            ),
        })

    total = sum(1 for pc in per if pc["ok"] in (True, False))
    return {
        "satisfied": satisfied,
        "total": total,
        "per_constraint": per,
        "undecidable": undecidable,
    }


# --------------------------------------------------------------------------- #
# Convenience
# --------------------------------------------------------------------------- #
def item_csr(values: Dict[str, Any], constraints_text: str,
             tokens: List[str]) -> Optional[float]:
    """Per-item constraint-satisfaction rate = satisfied / total (None if total==0)."""
    parsed = parse_keyed_constraints(constraints_text, tokens)
    out = check_allocation(values, parsed, {})
    if out["total"] == 0:
        return None
    return out["satisfied"] / out["total"]
