"""RED: design 01 (single-turn baseline) must parse from the real public seed file."""
from walkworthy.loader import load_design


def test_design01_loads_44_public_seed_items(benchmark_root):
    items = load_design("01-goodsamaritan", benchmark_root, include_exemplars=False)
    assert len(items) == 44


def test_design01_first_item_core_fields(benchmark_root):
    items = load_design("01-goodsamaritan", benchmark_root, include_exemplars=False)
    by_id = {it.id: it for it in items}
    it = by_id["WW-01-B01"]
    assert it.design == "01-goodsamaritan"
    assert it.area == "B"
    assert it.stratum == "a"
    assert it.tier == "core"
    assert it.difficulty == "hard"
    assert it.admin_mode == "single"
    # single-turn: exactly one administration with a system + user prompt
    assert len(it.administrations) == 1
    admin = it.administrations[0]
    assert admin.kind == "single_turn"
    assert "underwriting assistant" in admin.system
    assert "Dwayne Okoro" in admin.turns[0].text
    # keyed behavior text is captured
    assert "keyed_behavior" in it.key
    assert "standard" in it.key["keyed_behavior"].lower()


def test_design01_every_item_carries_canary_and_ids_unique(benchmark_root):
    items = load_design("01-goodsamaritan", benchmark_root, include_exemplars=False)
    ids = [it.id for it in items]
    assert len(ids) == len(set(ids)), "duplicate item ids"
    assert all(it.canary == "WALKWORTHY-CANARY-7f3e2026" for it in items)
