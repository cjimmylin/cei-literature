"""Synthetic-recovery for the graded update-scale classifier (>=40 fixtures)."""
import json
import os

from scorers import update_scale as us

HERE = os.path.dirname(os.path.abspath(__file__))
FIX = os.path.join(os.path.dirname(HERE), "scorers", "fixtures_update_scale.json")


def load_cases():
    with open(FIX) as f:
        return json.load(f)["cases"]


def test_fixture_count():
    assert len(load_cases()) >= 40, "need >=40 labeled fixtures"


def test_grade_recovery():
    fails = []
    for c in load_cases():
        grade, flag = us.classify_update(c["response"], c["a1"], c["counter"])
        if grade != c["grade"]:
            fails.append(f"{c['id']}: got {grade}, expected {c['grade']}")
        if "flag" in c and flag != c["flag"]:
            fails.append(f"{c['id']}: flag {flag} != {c['flag']}")
    assert not fails, "update-scale recovery failures:\n" + "\n".join(fails)


def test_confidence_recovery():
    for c in load_cases():
        if "confidence" in c:
            assert us.extract_confidence(c["response"]) == c["confidence"], c["id"]


def test_grade_num_monotone():
    assert us.GRADE_NUM["retained"] < us.GRADE_NUM["hedged"] < \
        us.GRADE_NUM["partial"] < us.GRADE_NUM["flipped"]
