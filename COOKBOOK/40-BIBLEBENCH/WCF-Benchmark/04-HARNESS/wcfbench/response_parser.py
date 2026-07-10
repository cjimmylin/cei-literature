"""Robust response parser — tolerant of real-model format drift (Phase 3).

The examinee-prompt builder asks for a specific output shape, but real models
paraphrase the format: session-5b saw ``RANKING: (a) < (b) < (c)`` (parenthesized)
where the smoke's first parser expected bare ``a < b < c`` and silently scored a
correct answer as unparseable. This module is the hardened extraction layer the
runner routes every response through BEFORE scoring, so a format quirk never
masquerades as a wrong answer.

Three extractors, matched to the three machine-scored kinds (spine §4.4):

  - :func:`parse_ranking`   — AGGRAVATE ordinal: returns letters LEAST→MOST
    heinous (normalizing a ``>`` chain), the :data:`INCOMPARABLE` sentinel when
    the model declines a total order, or ``None`` when nothing parses.
  - :func:`extract_citations` — PROOFTEXT: the set of Westminster reference
    tokens the response cites (``Q141``, ``WCF 1.9``), normalized.
  - :func:`parse_choice`    — recognition/MCQ + verdict items: the single-letter
    answer, or ``None``.

Every function is pure and network-free.
"""

from __future__ import annotations

import re
from typing import List, Optional, Set, Union

from .scorers import INCOMPARABLE

# --- ranking ----------------------------------------------------------------

# A chain of >=2 letters (each optionally wrapped in ()/[]) joined by < or >.
# Tolerant of arbitrary whitespace: "a<b<c", "(a) < (b) < (c)", "[b] < [a]".
_CHAIN_RE = re.compile(
    r"[\(\[]?[a-eA-E][\)\]]?(?:\s*[<>]\s*[\(\[]?[a-eA-E][\)\]]?)+"
)
_RANKING_LINE_RE = re.compile(r"RANKING:\s*(.+)", re.IGNORECASE)

# Phrases signalling the model declined a confident total order (incomparable).
_DECLINE_MARKERS = (
    "decline a total order",
    "declines a total order",
    "decline to order",
    "decline to rank",
    "declines to rank",
    "refuse to rank",
    "cannot rank",
    "can't rank",
    "no confident order",
    "no confident total order",
    "no total order",
    "not comparable",
    "incomparable",
    "incommensurable",
)


def _extract_chain(fragment: str) -> Optional[List[str]]:
    """Pull the first letter-chain from ``fragment`` and return it LEAST→MOST.

    ``<`` reads left-to-right as increasing (least→most, kept as written); an
    all-``>`` chain is reversed; a mixed-operator chain is malformed → ``None``.
    """
    m = _CHAIN_RE.search(fragment)
    if not m:
        return None
    chain = m.group(0)
    ops = re.findall(r"[<>]", chain)
    letters = [c.lower() for c in re.findall(r"[a-eA-E]", chain)]
    if len(letters) < 2 or not ops:
        return None
    if all(o == "<" for o in ops):
        return letters
    if all(o == ">" for o in ops):
        return list(reversed(letters))
    return None  # mixed operators — unparseable, do not guess


def parse_ranking(text: Optional[str]) -> Union[List[str], str, None]:
    """Extract a ranking (least→most heinous), the incomparable sentinel, or None.

    Resolution order (documented, load-bearing):
      1. An explicit ``RANKING:`` line wins — parse its tail (declination markers
         there return :data:`INCOMPARABLE`; else its letter chain). This beats a
         stray inequality mentioned rhetorically earlier in the prose.
      2. No ``RANKING:`` line: a declination marker anywhere → :data:`INCOMPARABLE`.
      3. Otherwise the first letter-chain found in the whole text.
      4. Nothing parses → ``None``.
    """
    if not text:
        return None

    line = _RANKING_LINE_RE.search(text)
    if line:
        tail = line.group(1)
        low = tail.lower()
        if any(m in low for m in _DECLINE_MARKERS):
            return INCOMPARABLE
        chain = _extract_chain(tail)
        if chain is not None:
            return chain
        # A RANKING: line that declines can phrase it in the label itself.
        if any(m in text.lower() for m in _DECLINE_MARKERS):
            return INCOMPARABLE
        return None

    low = text.lower()
    if any(m in low for m in _DECLINE_MARKERS):
        return INCOMPARABLE
    return _extract_chain(text)


# --- citations --------------------------------------------------------------

_Q_RE = re.compile(r"Q\s*\.?\s*(\d+)", re.IGNORECASE)
_WCF_RE = re.compile(r"WCF\s*(\d+)\.(\d+)", re.IGNORECASE)


def extract_citations(text: Optional[str]) -> Set[str]:
    """Return the set of normalized Westminster reference tokens cited in ``text``.

    ``Q 141`` / ``Q.141`` → ``Q141``; ``WCF 21 . 7`` → ``WCF 21.7``. This is what
    the model *claims* to cite (telemetry + the anchor scorer's substrate); it
    does NOT judge whether the citation is used correctly (that is the §4.3
    judge-assisted scorer's job).
    """
    if not text:
        return set()
    cites: Set[str] = set()
    for m in _Q_RE.finditer(text):
        cites.add(f"Q{m.group(1)}")
    for m in _WCF_RE.finditer(text):
        cites.add(f"WCF {m.group(1)}.{m.group(2)}")
    return cites


# --- choice / verdict -------------------------------------------------------

_CHOICE_PATTERNS = (
    re.compile(r"ANSWER:\s*[\(\[]?([a-eA-E])[\)\]]?", re.IGNORECASE),
    re.compile(r"answer is\s*[\(\[]?([a-eA-E])[\)\]]?", re.IGNORECASE),
    re.compile(r"\bchoose\s*(?:option\s*)?[\(\[]?([a-eA-E])[\)\]]?", re.IGNORECASE),
    re.compile(r"\boption\s*[\(\[]?([a-eA-E])[\)\]]?\b", re.IGNORECASE),
)


def parse_choice(text: Optional[str]) -> Optional[str]:
    """Extract a single-letter MCQ / verdict answer (``ANSWER: b``, "the answer is
    (c)", "I choose option A"), lower-cased, or ``None`` if none is stated.

    For the recognition (T1) and CROSSWIND-MCQ legs; kept deliberately strict —
    an explicit answer marker only, never a guess from stray letters in prose.
    """
    if not text:
        return None
    for pat in _CHOICE_PATTERNS:
        m = pat.search(text)
        if m:
            return m.group(1).lower()
    return None
