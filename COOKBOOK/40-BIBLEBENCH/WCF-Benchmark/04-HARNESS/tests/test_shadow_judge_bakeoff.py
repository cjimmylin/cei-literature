from __future__ import annotations

import hashlib
import importlib


def _runner():
    return importlib.import_module("shadow_judge_bakeoff")


def _record(item_id, model, response, judges, *, kind="contested"):
    return {
        "item_id": item_id,
        "model": model,
        "sut_response": response,
        "kind": kind,
        "template_hash": "47ddb41c355fbf57",
        "judges": judges,
    }


def test_fixed_shadow_roster_counts_and_budget():
    r = _runner()
    assert r.CANDIDATES == (
        ("glm-5.2", "z-ai", "z-ai/glm-5.2"),
        ("deepseek-v4-pro", "deepseek", "deepseek/deepseek-v4-pro"),
    )
    assert r.SURFACE_COUNTS == {
        "open_award": 8,
        "coherence": 8,
        "disclosure": 6,
        "settled_core": 6,
    }
    assert r.MAX_BUDGET == 1.0


def test_contested_source_priority_never_joins_a_different_response():
    r = _runner()
    floor = [
        _record("A", "llama", "floor A", [{"name": "gemini-flash", "scores": {}}]),
        _record("B", "llama", "floor B", [{"name": "grok-4.20", "scores": {}}]),
        _record("C", "deepseek", None, []),
    ]
    r33 = [
        _record("A", "llama", "different A", [{"name": "gemini-flash", "scores": {}}]),
        _record("C", "deepseek", "r33 C", [{"name": "gemini-flash", "scores": {}}]),
    ]
    chosen = r.select_contested_records(floor, r33, expected=3)
    by_key = {(x["item_id"], x["model"]): x for x in chosen}
    assert by_key[("A", "llama")]["sut_response"] == "floor A"
    assert by_key[("C", "deepseek")]["sut_response"] == "r33 C"


def test_seeded_surface_order_is_sha256_and_exact_count():
    r = _runner()
    rows = [_record(f"I{i}", f"M{i}", f"R{i}", [], kind="open") for i in range(12)]
    got = r.take_seeded("open_award", rows, 8)
    expected = sorted(
        rows,
        key=lambda x: hashlib.sha256(
            f"1647|open_award|{x['item_id']}|{x['model']}".encode()
        ).hexdigest(),
    )[:8]
    assert [(x["item_id"], x["model"]) for x in got] == [
        (x["item_id"], x["model"]) for x in expected
    ]
