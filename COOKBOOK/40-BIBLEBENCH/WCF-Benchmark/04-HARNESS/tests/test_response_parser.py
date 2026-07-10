"""Tests for response_parser.py — tolerant extraction from real model text.

Session-5b lesson: claude-3-haiku wrote `RANKING: (a) < (b) < (c)`, not bare
`a < b < c`. A brittle parser silently zeroes a correct answer, so these tests
pin the observed drift: parenthesized/bracketed letters, `>`-reversed chains,
declination phrasing, and unparseable tails.
"""

import os
import sys

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)

from wcfbench.response_parser import (  # noqa: E402
    parse_ranking,
    extract_citations,
    parse_choice,
)
from wcfbench.scorers import INCOMPARABLE  # noqa: E402


# --- parse_ranking ----------------------------------------------------------

def test_bare_ranking_line():
    assert parse_ranking("...reasoning...\nRANKING: a < b < c") == ["a", "b", "c"]


def test_parenthesized_letters_the_haiku_case():
    # The exact session-5b format that broke the smoke's first parser.
    assert parse_ranking("RANKING: (a) < (b) < (c)") == ["a", "b", "c"]


def test_bracketed_letters():
    assert parse_ranking("RANKING: [b] < [a] < [c]") == ["b", "a", "c"]


def test_greater_than_is_normalized_to_least_first():
    # A model writing most>least must come back least->most for the scorer.
    assert parse_ranking("RANKING: c > b > a") == ["a", "b", "c"]


def test_two_letter_ranking():
    assert parse_ranking("RANKING: a < b") == ["a", "b"]


def test_ranking_without_the_label_still_found():
    assert parse_ranking("So my ordering is a < c < b overall.") == ["a", "c", "b"]


def test_declination_returns_incomparable_sentinel():
    txt = "The Q151 calculus is incomparable here; I decline a total order and profile each."
    assert parse_ranking(txt) == INCOMPARABLE


def test_ranking_line_beats_a_stray_inequality_in_prose():
    txt = "Some say a > b in stakes, but that is not a Q151 head.\nRANKING: a < b < c"
    assert parse_ranking(txt) == ["a", "b", "c"]


def test_mixed_operators_is_unparseable():
    assert parse_ranking("RANKING: a < b > c") is None


def test_no_ranking_no_declination_is_none():
    assert parse_ranking("I think this is a hard question with no clean answer letters.") is None


def test_empty_is_none():
    assert parse_ranking("") is None
    assert parse_ranking(None) is None


# --- extract_citations ------------------------------------------------------

def test_extract_q_and_wcf_citations():
    txt = "Under WLC Q141 and Q 142 (see WCF 1.9), the duty stands; cf. WCF 21.7."
    cites = extract_citations(txt)
    assert "Q141" in cites
    assert "Q142" in cites          # 'Q 142' normalizes
    assert "WCF 1.9" in cites
    assert "WCF 21.7" in cites


def test_extract_citations_empty():
    assert extract_citations("no references here") == set()
    assert extract_citations("") == set()


# --- parse_choice -----------------------------------------------------------

def test_parse_choice_answer_line():
    assert parse_choice("Reasoning...\nANSWER: b") == "b"


def test_parse_choice_prose_forms():
    assert parse_choice("The answer is (c).") == "c"
    assert parse_choice("I choose option A.") == "a"


def test_parse_choice_none_when_absent():
    assert parse_choice("I am not sure which to pick.") is None
    assert parse_choice("") is None
