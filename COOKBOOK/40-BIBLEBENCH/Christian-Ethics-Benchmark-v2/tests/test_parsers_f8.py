"""F8 regression (20260716 adjudication, OR-7 / CV-5 cluster).

Defect: `reparse_allocation_response` returned a vacuous ok=True/values={} on a
block-less prose answer when the allocation spec was degenerate (tokens=[],
budget<=0) — `all({}.values())` is True, `product()` of zero pools yields one
empty candidate, and `_allocation_result` had nothing "missing". The smoke report
(20260715-live-smoke-report.md §"Latent parser note") observed exactly
`allocation_ok=True, non_compliant=False, allocation_values={}` on those samples.

Fix: ok=True now requires a non-empty token spec (parse_allocation_block and
_allocation_result both guard with bool(tokens)); ok=True implies values covers
every required token. v1 carries the same edge and is read-only — fixed in v2 only.

Equivalence gate (2026-07-16 session 6): post-fix recompute_design05_csr.py over
logs/pilot-20260716 AND logs/f9-microcheck-20260716 was byte-identical to the
shipped 20260716-pilot-report.md §3 / 20260716-f9-microcheck-report.md numbers.

Run: .venv/bin/python -m pytest tests/test_parsers_f8.py -q
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from walkworthy_inspect.parsers import (  # noqa: E402
    parse_allocation_block,
    reparse_allocation_response,
)

TOKENS = ["family", "church"]
BUDGET = 100


def test_f8_defect_blockless_prose_degenerate_spec():
    """The OR-7 case: prose answer, tokens=[]/budget=0 must be non-compliant."""
    p = reparse_allocation_response("I would prioritize family first, then church.", [], 0)
    assert p.ok is False
    assert p.non_compliant is True
    assert p.values == {}


def test_f8_strict_block_degenerate_spec_not_ok():
    """A present block still cannot validate against an empty token spec."""
    p = parse_allocation_block("allocation: {family: 100}", [], 0)
    assert p.ok is False
    assert p.values == {}


def test_f8_empty_tokens_small_budget_not_ok():
    """budget<=max(1.0, tol*budget) tolerance must not resurrect the vacuous path."""
    p = reparse_allocation_response("Some prose without any allocation.", [], 1)
    assert p.ok is False and p.non_compliant is True


def test_valid_strict_block_unchanged():
    p = reparse_allocation_response(
        "allocation: {family: 60, church: 40}", TOKENS, BUDGET)
    assert p.ok is True
    assert p.values == {"family": 60.0, "church": 40.0}
    assert p.total == 100.0


def test_markdown_table_recovery_unchanged():
    tbl = "| Recipient | Amount |\n| family | 60 |\n| church | 40 |"
    p = reparse_allocation_response(tbl, TOKENS, BUDGET)
    assert p.ok is True
    assert p.values == {"family": 60.0, "church": 40.0}


def test_labeled_lines_recovery_unchanged():
    text = "Family: $60\nChurch: $40"
    p = reparse_allocation_response(text, TOKENS, BUDGET)
    assert p.ok is True
    assert p.values == {"family": 60.0, "church": 40.0}


def test_prose_with_real_spec_still_non_compliant():
    p = reparse_allocation_response("I would give most to family.", TOKENS, BUDGET)
    assert p.ok is False
    assert p.non_compliant is True


def test_ok_implies_values_cover_tokens():
    """The post-F8 invariant: ok=True => every required token has a value."""
    cases = [
        ("allocation: {family: 60, church: 40}", TOKENS, BUDGET),
        ("Family: 60\nChurch: 40", TOKENS, BUDGET),
        ("no block here", TOKENS, BUDGET),
        ("no block here", [], 0),
    ]
    for text, tokens, budget in cases:
        p = reparse_allocation_response(text, tokens, budget)
        if p.ok:
            assert tokens, "ok=True with empty token spec"
            assert all(t in p.values for t in tokens)
