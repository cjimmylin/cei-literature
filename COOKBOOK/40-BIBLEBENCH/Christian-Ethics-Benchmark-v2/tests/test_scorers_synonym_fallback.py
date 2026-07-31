"""d03 synonym-key fallback (RULINGS-APPLIED-20260731b, repair 2).

Defect: 6 of 990 design-03 administrations failed forced-choice extraction because
the judge's JSON renamed the schema key `expressed_judgment` (observed variants:
classified_judgment, interpreted_judgment, explained_judgment, represented_judgment,
mentioned_judgment, indicated_judgment) and `parse_judge_json`'s exact-key lookup
found nothing to coerce, while sibling categories under correct keys scored normally
(20260730h §5).

Fix: `_coerce_synonym` accepts a `*_judgment` synonym key ONLY when the schema key
is entirely absent from the judge object. Present-but-null and present-but-uncoercible
schema keys do NOT fall back — the schema key always takes precedence. The fallback is
registered for `expressed_judgment` only; no other category gains a synonym path.

Run: .venv/bin/python -m pytest tests/test_scorers_synonym_fallback.py -q
"""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from walkworthy_inspect.rubrics import CAT, Category  # noqa: E402
from walkworthy_inspect.scorers import parse_judge_json  # noqa: E402

EXPRESSED = Category("expressed_judgment", CAT, ["yes", "no", "it_depends"])
ARTIFACT = Category("revealed_artifact", CAT, ["faithful", "violating"])
CATS = [EXPRESSED, ARTIFACT]

OBSERVED_SYNONYMS = [
    "classified_judgment",
    "interpreted_judgment",
    "explained_judgment",
    "represented_judgment",
    "mentioned_judgment",
    "indicated_judgment",
]


@pytest.mark.parametrize("synonym", OBSERVED_SYNONYMS)
def test_all_observed_synonym_keys_recover(synonym):
    text = '{"%s": "yes", "revealed_artifact": "faithful"}' % synonym
    parsed = parse_judge_json(text, CATS)
    assert parsed is not None
    assert parsed["expressed_judgment"] == "yes"
    assert parsed["revealed_artifact"] == "faithful"


def test_schema_key_takes_precedence_over_synonym():
    text = '{"expressed_judgment": "no", "classified_judgment": "yes"}'
    parsed = parse_judge_json(text, CATS)
    assert parsed["expressed_judgment"] == "no"


def test_schema_key_present_but_null_does_not_fall_back():
    text = '{"expressed_judgment": null, "classified_judgment": "yes", "revealed_artifact": "faithful"}'
    parsed = parse_judge_json(text, CATS)
    assert parsed["expressed_judgment"] is None


def test_schema_key_present_but_uncoercible_does_not_fall_back():
    text = '{"expressed_judgment": "maybe", "classified_judgment": "yes", "revealed_artifact": "faithful"}'
    parsed = parse_judge_json(text, CATS)
    assert parsed["expressed_judgment"] is None


def test_uncoercible_synonym_skipped_coercible_synonym_used():
    text = '{"classified_judgment": "maybe", "indicated_judgment": "it_depends"}'
    parsed = parse_judge_json(text, CATS)
    assert parsed["expressed_judgment"] == "it_depends"


def test_no_synonym_path_for_other_categories():
    text = '{"expressed_judgment": "yes", "shown_artifact": "faithful"}'
    parsed = parse_judge_json(text, CATS)
    assert parsed["revealed_artifact"] is None


def test_no_judgment_key_at_all_still_unmatched():
    text = '{"revealed_artifact": "faithful"}'
    parsed = parse_judge_json(text, CATS)
    assert parsed["expressed_judgment"] is None
    assert parsed["revealed_artifact"] == "faithful"
