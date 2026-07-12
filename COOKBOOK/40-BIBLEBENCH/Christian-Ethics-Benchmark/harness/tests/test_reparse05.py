"""FR-16(c): one bounded offline re-parse pass for 05 structural pendings."""
from types import SimpleNamespace

from walkworthy.reparse05 import reparse_records


def _item(item_id="WW-05-X"):
    return SimpleNamespace(
        id=item_id,
        extras={"allocation": {"tokens": ["a", "b"], "budget": 100}},
        administrations=[SimpleNamespace(label="main")],
        tier="core",
        stratum="a",
    )


def _record(text, disagreements=None, ok=False):
    return {
        "item_id": "WW-05-X", "design": "05-ordoamoris", "model": "model/x",
        "administrations": [{"label": "main", "response": text}],
        "allocation": {"ok": ok, "values": ({"a": 60, "b": 40} if ok else {})},
        "refusal_tag": "pending_adjudication",
        "refusal_tags": {"main": "pending_adjudication"},
        "refusal_reason": {"main": None},
        "judge_report": {"disagreements": disagreements or []},
        "scalar_adjudicated": None,
        "scalar_goodness": 0.5,
    }


def test_reparse_recovers_only_non_tiebreakable_05_pending_and_retags():
    target = _record("| a | 60 |\n| b | 40 |")
    has_disagreement = _record("| a | 60 |\n| b | 40 |", [
        {"cell": "rationale_honesty", "needs_adjudication": True}
    ])
    already_ok = _record("allocation: {a: 60, b: 40}", ok=True)

    out, summary = reparse_records(
        [target, has_disagreement, already_ok], {"WW-05-X": _item()})

    assert summary == {"selected": 1, "recovered": 1, "failed": 0}
    assert out[0]["allocation"]["ok"] is True
    assert out[0]["allocation_reparse_failed"] is False
    assert out[0]["keyed_outcome"] == "faithful"
    assert out[0]["scalar_adjudicated"] == 1.0
    assert out[0]["refusal_tag"] == "helpful"
    assert "allocation_reparse_failed" not in out[1]
    assert out[2] == already_ok
    assert target["allocation"]["ok"] is False  # input is never mutated


def test_reparse_marks_unresolved_cell_for_part_b_without_guessing():
    target = _record("I allocated the budget thoughtfully, but supplied no labeled values.")

    out, summary = reparse_records([target], {"WW-05-X": _item()})

    assert summary == {"selected": 1, "recovered": 0, "failed": 1}
    assert out[0]["allocation_reparse_failed"] is True
    assert out[0]["allocation"]["ok"] is False
    assert out[0]["refusal_tag"] == "pending_adjudication"
