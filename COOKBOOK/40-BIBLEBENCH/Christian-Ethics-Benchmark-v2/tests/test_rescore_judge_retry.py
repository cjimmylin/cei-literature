"""v4-A 2(a) — judge-B parse hardening in the rescore tool (retry-on-parse-failure).

Defect (20260731o §6.1): judge-B parse failure became UNSCORABLE data on the first
miss; raw parse-failure rates ran 0.0-17.1 pct by design, enough to void the
ratified >= 85 pct complete-case retention gate on its own. The v4-T tier probe
(20260802c) reproduced the failure out-of-sample: 5 of 294 fresh d01 judge-B calls
returned degenerate output (### repetition loops, empty text, phrase loops) and
each ALSO failed an identical same-prompt retry — so the hardened path appends a
format reminder on retries (the d05 solver F9 convention ported to the judge
path: remedial prompt fires only after the plain prompt already failed).

Fixture: tests/fixtures/judgeB_degenerate_20260802.jsonl — the 5 degenerate raw
outputs, extracted from the gitignored v4-T run tree so the regression is
committed. No model calls anywhere in this file ($0).

Run: .venv/bin/python -m pytest tests/test_rescore_judge_retry.py -q
"""
import asyncio
import json
import sys
from pathlib import Path
from types import SimpleNamespace

_V2_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_V2_ROOT))
sys.path.insert(0, str(_V2_ROOT / "tools" / "rescore"))

import rescore  # noqa: E402
from walkworthy_inspect.rubrics import judge_categories, spec_for  # noqa: E402
from walkworthy_inspect.scorers import UNSCORABLE, parse_judge_json  # noqa: E402

FIXTURE = _V2_ROOT / "tests" / "fixtures" / "judgeB_degenerate_20260802.jsonl"
CATS = judge_categories(spec_for("01"))  # action_class + rationale_quality
GOOD = '{"action_class": "full_obedience", "rationale_quality": 2}'


def _degenerate_raws():
    return [json.loads(l)["raw"] for l in FIXTURE.open(encoding="utf-8") if l.strip()]


class ScriptedModel:
    """Judge stub: yields scripted completions/exceptions, records prompts."""

    def __init__(self, outputs):
        self.outputs = list(outputs)
        self.prompts = []

    async def generate(self, prompt, config=None):
        self.prompts.append(prompt)
        item = self.outputs.pop(0)
        if isinstance(item, Exception):
            raise item
        return SimpleNamespace(completion=item)


def _judge(outputs, max_attempts=3):
    model = ScriptedModel(outputs)
    result = asyncio.run(
        rescore._judge_one(model, "PROMPT", CATS, max_attempts=max_attempts))
    return model, result


# --------------------------------------------------------------------------- #
# fixture regression: the v4-T degenerate outputs MUST route to retry
# --------------------------------------------------------------------------- #
def test_fixture_has_five_rows():
    assert len(_degenerate_raws()) == 5


def test_degenerate_raws_are_unparseable():
    # If parse_judge_json ever starts accepting these, the retry seam silently
    # stops firing on the known failure mode — fail loudly instead.
    for raw in _degenerate_raws():
        assert parse_judge_json(raw, CATS) is None


# --------------------------------------------------------------------------- #
# retry behavior
# --------------------------------------------------------------------------- #
def test_first_attempt_success_is_byte_identical_path():
    model, result = _judge([GOOD])
    assert len(model.prompts) == 1
    assert model.prompts[0] == "PROMPT"  # no reminder on the plain first attempt
    assert result["action_class"] == "full_obedience"
    assert result["_attempts"] == 1


def test_degenerate_then_good_recovers_with_reminder():
    for raw in _degenerate_raws():
        model, result = _judge([raw, GOOD])
        assert len(model.prompts) == 2
        assert model.prompts[0] == "PROMPT"
        assert model.prompts[1].startswith("PROMPT")
        assert rescore._JUDGE_FORMAT_REMINDER in model.prompts[1]
        assert result["action_class"] == "full_obedience"
        assert result["_attempts"] == 2


def test_all_attempts_degenerate_is_unparseable_data():
    raw = _degenerate_raws()[0]
    model, result = _judge([raw, raw, raw])
    assert len(model.prompts) == 3
    assert result["_unparseable"] is True
    assert result["_attempts"] == 3
    assert result["_raw"]  # evidence preserved for audit


def test_empty_completion_counts_as_parse_failure():
    model, result = _judge(["", GOOD])
    assert len(model.prompts) == 2
    assert result["action_class"] == "full_obedience"


def test_transport_error_then_good_recovers(monkeypatch):
    monkeypatch.setattr(rescore, "_ERROR_BACKOFF_BASE_S", 0)
    model, result = _judge([RuntimeError("boom"), GOOD])
    assert result["action_class"] == "full_obedience"
    assert result["_attempts"] == 2


def test_persistent_transport_error_is_judge_error(monkeypatch):
    monkeypatch.setattr(rescore, "_ERROR_BACKOFF_BASE_S", 0)
    model, result = _judge([RuntimeError("a"), RuntimeError("b"), RuntimeError("c")])
    assert result["_judge_error"] == "c"
    assert result["_attempts"] == 3


def test_max_attempts_one_reproduces_prehardening_semantics():
    raw = _degenerate_raws()[0]
    model, result = _judge([raw], max_attempts=1)
    assert len(model.prompts) == 1
    assert result["_unparseable"] is True


def test_missing_category_still_unscorable_not_retried():
    # Parsed reply with one coercible category is judge DATA (any_ok semantics
    # of the pinned parse_judge_json) — no retry burns spend on it.
    partial = '{"action_class": "full_obedience"}'
    model, result = _judge([partial])
    assert len(model.prompts) == 1
    assert result["action_class"] == "full_obedience"
    assert result["rationale_quality"] == UNSCORABLE


# --------------------------------------------------------------------------- #
# retention accounting
# --------------------------------------------------------------------------- #
def _row(design, meta=None, **jb):
    judge_b = dict(jb)
    if meta is not None:
        judge_b["_judge_meta"] = meta
    return {"design": design, "judge_b": judge_b}


def test_retention_by_design_counts_parse_failures_only():
    rows = [
        _row("01-obedience", meta={"_attempts": 1}, action_class="full_obedience"),
        _row("01-obedience", meta={"_unparseable": True, "_attempts": 3}),
        # genuine UNSCORABLE verdict from a parsed reply = data, not attrition
        _row("01-obedience", meta={"_attempts": 2}, action_class=UNSCORABLE),
        _row("06-process", meta={"_judge_error": "x", "_attempts": 3}),
    ]
    stats = rescore.retention_by_design(rows)
    assert stats["01-obedience"]["rows"] == 3
    assert stats["01-obedience"]["complete"] == 2
    assert abs(stats["01-obedience"]["retention"] - 2 / 3) < 1e-9
    assert stats["06-process"]["retention"] == 0.0


def test_retention_per_turn_rows_require_all_turns():
    rows = [
        _row("02-pressure", meta={"turn_attempts": [1, 1, 1],
                                  "turn_failures": [False, False, False]}),
        _row("02-pressure", meta={"turn_attempts": [1, 3, 1],
                                  "turn_failures": [False, True, False]}),
    ]
    stats = rescore.retention_by_design(rows)
    assert stats["02-pressure"]["complete"] == 1
    assert stats["02-pressure"]["retention"] == 0.5
