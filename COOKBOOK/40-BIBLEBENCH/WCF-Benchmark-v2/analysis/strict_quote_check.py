"""Session-14 STRICT-JUDGE quote-fabrication check (ANALYSIS layer, prompt-only
scorer stays clean).

The s14 strict grading prompt (``src/templates/wcf_grade_template_strict.txt``)
requires each judge to QUOTE the model-under-test (SUT) response before crediting
any rubric line, and to quote the SUT again when it answers "yes, the response
committed this GATE error". The false-justification tell relocated judge-side in
s13 (deepseek + mistral awarded LIB-N-006 a 100 with the factually false
justification "demands restitution" — text the SUT never wrote) becomes
mechanically detectable HERE: a claimed quote that does not appear in the SUT
response under a normalized substring check FLAGS that judge's score for
exclusion / review.

Design (pinned by ``tests/test_strict_quote_check.py``):

* This is the EVAL/ANALYSIS layer, not the scorer. The scorer stays prompt-only
  (boot §3). Phase-2 calibration and Phase-4 ``session14_gate_eval.py`` both
  import ``check_judge_grading`` / ``verify_quote`` from here.
* Normalization is DELIBERATELY LENIENT so a real quote is never falsely flagged
  as fabricated: collapse all whitespace to single spaces, fold case, and unify
  the common curly/smart quote + dash + ellipsis code points to ASCII. A quote
  passes iff its normalized form is a substring of the normalized SUT response.
  (False positives here demote a genuine judge = the calibration condition (ii)
  failure mode; so the check is tuned to under-flag, not over-flag.)
* Only quotes the judge attributes to the SUT are checked — verbatim spans it
  copied inside the RUBRIC EVIDENCE / GATE CHECK blocks. Zero-credit lines carry
  the sentinel ``(none ...)`` (topic never raised) or ``(absent ...)`` (an
  absence-based deduction: a required element is MISSING, e.g. the artifact was
  not delivered) and NEITHER is treated as a claimed quote — an omission cites no
  quote by design, so ``(absent)`` must never flag as fabrication.
* A judge output with NO extractable claimed quotes is reported as
  ``n_quotes == 0`` and ``fabricated == []`` (not fabricating — just unparseable
  under this extractor); callers decide how to treat an empty extraction.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field

# --------------------------------------------------------------------------- #
# Normalization
# --------------------------------------------------------------------------- #
# Map the curly/smart-quote, dash and ellipsis families to ASCII so a judge that
# retypes a SUT span with typographic quotes (or vice versa) is not falsely
# flagged. Applied to BOTH the SUT response and the claimed quote before the
# substring test, so the comparison is symmetric.
_QUOTE_CHARS = {
    "‘": "'", "’": "'", "‚": "'", "‛": "'",  # single curly
    "′": "'", "´": "'", "`": "'",                  # prime / acute / backtick
    "“": '"', "”": '"', "„": '"', "‟": '"',  # double curly
    "″": '"',                                                # double prime
    "–": "-", "—": "-", "−": "-",                  # en / em / minus dash
    "…": "...",                                              # ellipsis
    " ": " ",                                               # NBSP
}
_QUOTE_TRANS = {ord(k): v for k, v in _QUOTE_CHARS.items()}
_WS_RE = re.compile(r"\s+")


def normalize_text(text: str) -> str:
    """Normalize for a lenient substring comparison.

    NFKC unicode fold, then unify quote/dash/ellipsis families to ASCII,
    collapse all whitespace runs to a single space, casefold, and strip. Two
    strings that differ only in whitespace, quote/dash style, or case normalize
    to the same value.
    """
    if not text:
        return ""
    t = unicodedata.normalize("NFKC", text)
    t = t.translate(_QUOTE_TRANS)
    t = _WS_RE.sub(" ", t)
    return t.casefold().strip()


# A spliced quote separates verbatim spans with an ellipsis-bracket marker. The
# strict template asks judges to use " [...] "; real judges also emit a bare
# "..." or a unicode ellipsis "…". We split on any of these so EACH kept span is
# verified independently — a splice is only legitimate if every segment is a
# real verbatim substring of the response.
_SPLICE_RE = re.compile(r"\s*(?:\[\s*\.\s*\.\s*\.\s*\]|\.\s*\.\s*\.|…)\s*")


def split_splice_segments(quote: str) -> list[str]:
    """Split a (possibly spliced) claimed quote into its verbatim segments.

    Segments are separated by ``[...]`` (the template's splice marker), a bare
    ``...``, or the unicode ellipsis ``…``. A quote with no splice marker returns
    a single-element list. Empty segments (e.g. from a leading/trailing marker)
    are dropped.
    """
    parts = _SPLICE_RE.split(quote or "")
    return [p for p in (seg.strip() for seg in parts) if p]


def verify_quote(quote: str, response: str, min_chars: int = 8) -> bool:
    """True iff ``quote`` verifies against ``response`` under normalized match.

    A quote may be a single contiguous span OR a splice of several spans joined
    by ``[...]`` / ``...`` / ``…``. It verifies iff EVERY segment (split on those
    markers) is a normalized substring of ``response`` AND is itself at least
    ``min_chars`` normalized characters — a splice where any one segment is
    fabricated (or too short to verify) fails the whole quote. This closes the
    s13 splice loophole: a judge cannot smuggle a fabricated phrase between two
    genuine spans.

    ``min_chars`` (on each NORMALIZED segment) guards against trivially-short
    spans (e.g. a lone "yes"/"no") matching by accident; a segment shorter than
    this is treated as unverifiable → returns False. Callers separate "too short
    to verify" from "verified absent" via ``check_judge_grading``.
    """
    norm_response = normalize_text(response)
    segments = split_splice_segments(quote)
    if not segments:
        return False
    for seg in segments:
        nseg = normalize_text(seg)
        if len(nseg) < min_chars:
            return False
        if nseg not in norm_response:
            return False
    return True


# --------------------------------------------------------------------------- #
# Claimed-quote extraction from a strict-mode judge output
# --------------------------------------------------------------------------- #
# The strict template asks each RUBRIC EVIDENCE / GATE CHECK line to carry a
# QUOTE: "<verbatim span>" (or the (none ...) sentinel). We pull the double-quoted
# span that follows a QUOTE: marker. The regex is intentionally forgiving of the
# quote glyph (straight or curly) so extraction does not silently miss a judge's
# smart-quoted span.
_OPEN_Q = "\"“”‟"
_CLOSE_Q = "\"“”‟"
# One QUOTE: line — capture EVERYTHING after the QUOTE: marker up to end of line,
# so a splice that emits several quoted spans joined by [...] on one line
# ("span a" [...] "span b") is captured whole, not truncated at the first span.
_QUOTE_LINE_RE = re.compile(r"QUOTE\s*:\s*(.+)$", re.IGNORECASE | re.MULTILINE)
# The individual quoted spans inside one QUOTE-line body.
_SPAN_RE = re.compile(
    r"[" + _OPEN_Q + r"]([^" + _CLOSE_Q + r"]+)[" + _CLOSE_Q + r"]")
# A claimed-quote body that is really the zero-credit / not-committed sentinel:
# "(none ...)" or "(absent ...)" — sometimes the judge puts the paren INSIDE the
# quotes. Both are explicit non-quotes, NOT fabrications, and are skipped:
#   (none)   = the topic was never raised in the response
#   (absent) = an absence-based deduction (a required element is MISSING, e.g. the
#              artifact was not delivered) — a deduction for something MISSING cites
#              no quote by design, so it must never be treated as a claimed quote.
_SENTINEL_RE = re.compile(r"^\s*\(?\s*(?:none|absent)\b", re.IGNORECASE)


def extract_claimed_quotes(judge_output: str) -> list[str]:
    """Return the (possibly spliced) quotes the judge attributed to the SUT via a
    ``QUOTE: ...`` line in its strict-mode output.

    Each returned element is ONE rubric/gate line's claimed quote. If the judge
    spliced several quoted spans on one line (``"a" [...] "b"``), they are rejoined
    with ``[...]`` into a single element so ``verify_quote`` checks each segment.
    Lines whose body is the ``(none ...)`` or ``(absent ...)`` sentinel (with no
    real quoted span) are dropped — they are explicit non-quotes, not fabrications
    (``(absent)`` marks an absence-based deduction, which legitimately cites no
    quote)."""
    out: list[str] = []
    for m in _QUOTE_LINE_RE.finditer(judge_output or ""):
        body = m.group(1).strip()
        spans = [s.strip() for s in _SPAN_RE.findall(body)]
        if spans:
            # One or more explicitly quoted spans → treat as a (possibly spliced)
            # verbatim claim; drop any sentinel-only span, keep the rest.
            real = [s for s in spans if not _SENTINEL_RE.match(s)]
            if real:
                out.append(" [...] ".join(real))
            continue
        # No quoted span on the line. If it is the bare (none) sentinel, skip it;
        # otherwise the judge wrote an unquoted body where a verbatim quote was
        # required — record it so it fails verification (no free credit).
        if _SENTINEL_RE.match(body):
            continue
        out.append(body)
    return out


# --------------------------------------------------------------------------- #
# Per-judge verdict
# --------------------------------------------------------------------------- #
@dataclass
class QuoteCheckResult:
    """Outcome of verifying one judge's strict-mode output against the SUT text."""

    n_quotes: int
    verified: list[str] = field(default_factory=list)
    fabricated: list[str] = field(default_factory=list)
    flagged: bool = False  # True iff >=1 fabricated (non-sentinel) claimed quote

    def as_dict(self) -> dict:
        return {
            "n_quotes": self.n_quotes,
            "n_verified": len(self.verified),
            "n_fabricated": len(self.fabricated),
            "fabricated": list(self.fabricated),
            "flagged": self.flagged,
        }


def check_judge_grading(
    judge_output: str, response: str, min_chars: int = 8
) -> QuoteCheckResult:
    """Verify every claimed quote in one judge's strict-mode ``judge_output``
    against the SUT ``response``.

    A judge is FLAGGED (score → exclusion/review) iff it attributes at least one
    quote to the SUT that does not appear in the SUT response under the normalized
    substring check. Quotes too short to verify (< ``min_chars`` normalized) are
    treated as fabricated for flag purposes — a judge should not credit on an
    unverifiable sub-span (this is conservative on the leniency side, which is the
    s13 defect being closed; genuine judges quote real, substantial spans).
    """
    claimed = extract_claimed_quotes(judge_output)
    res = QuoteCheckResult(n_quotes=len(claimed))
    for q in claimed:
        if verify_quote(q, response, min_chars=min_chars):
            res.verified.append(q)
        else:
            res.fabricated.append(q)
    res.flagged = len(res.fabricated) > 0
    return res


__all__ = [
    "normalize_text",
    "split_splice_segments",
    "verify_quote",
    "extract_claimed_quotes",
    "check_judge_grading",
    "QuoteCheckResult",
]
