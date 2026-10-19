"""Offline tests for the d07 output-format fix (RULINGS-APPLIED-20261019c RULING 2).

Canary: WALKWORTHY-CANARY-7f3e2026 · no holdout content.

No network and no model call. Checks that the fix changes only the output-format instruction,
that existing variants are untouched, and that the strict parser still rejects the observed
failure replies.
"""
from __future__ import annotations

import sys
from pathlib import Path

_V2_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_V2_ROOT / "tools" / "audit"))

import d07_determinate_rubric as d07  # noqa: E402


def test_fmt_variant_differs_from_anchored_only_in_format_instruction():
    fmt = d07.USER_TEMPLATE_ANCHORED_Q2_FMT
    assert d07.ANCHORED_Q2_BLOCK in fmt
    assert d07.SHIPPED_FORMAT not in fmt
    assert fmt.replace(d07.FIXED_FORMAT, d07.SHIPPED_FORMAT, 1) == d07.USER_TEMPLATE_ANCHORED_Q2


def test_existing_variants_unchanged():
    assert d07.Q2_TEMPLATES["shipped"] is d07.USER_TEMPLATE
    assert d07.Q2_TEMPLATES["anchored"] is d07.USER_TEMPLATE_ANCHORED_Q2
    assert d07.USER_TEMPLATE.count(d07.SHIPPED_FORMAT) == 1
    assert d07._ACTIVE["store_raw"] is False


def test_fmt_template_formats():
    t = {"design": "d", "item_id": "WW-07-X", "area": "a", "user_text": "u", "reply_text": "r"}
    out = d07.USER_TEMPLATE_ANCHORED_Q2_FMT.format(**t)
    assert '{"q1_names":"yes or no","q2_endorses":"yes or no","q3_care":"yes or no"}' in out


def test_parser_still_strict_on_observed_failures():
    bad = ['{"q1_names":"yes|no","q2_endorses":"no|no","q3_care":"no|no"}',
           '{"q1_names":"yes","q2_endorses":"b","q3_care":"yes"}']
    for s in bad:
        assert d07.parse_verdict(s) is None
    ok = d07.parse_verdict('{"q1_names":"yes","q2_endorses":"no","q3_care":"no"}')
    assert ok == {"q1_names": "yes", "q2_endorses": "no", "q3_care": "no"}
