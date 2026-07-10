"""RED: every design's PUBLIC seed bank parses to the handoff-verified count and
the structural invariants each design family requires (single / multi-turn /
paired / allocation)."""
import pytest

from walkworthy.loader import load_design

# Public-seed header counts verified against the O1 handoff §3 (2026-07-09).
EXPECTED_PUBLIC_SEED_COUNTS = {
    "01-goodsamaritan": 44, "02-twomasters": 36, "03-quiettongue": 29,
    "04-innerweight": 29, "05-ordoamoris": 28, "06-crookedpath": 27,
    "07-seventyseven": 27, "08-vocationfork": 29, "09-doubleedge": 34,
    "10-strangergate": 32,
}


@pytest.mark.parametrize("design,count", EXPECTED_PUBLIC_SEED_COUNTS.items())
def test_public_seed_count(design, count, benchmark_root):
    items = load_design(design, benchmark_root, include_exemplars=False)
    assert len(items) == count, f"{design}: got {len(items)} expected {count}"


@pytest.mark.parametrize("design", EXPECTED_PUBLIC_SEED_COUNTS)
def test_every_item_has_admin_and_canary(design, benchmark_root):
    items = load_design(design, benchmark_root, include_exemplars=False)
    for it in items:
        assert it.administrations, f"{it.id}: no administrations"
        assert it.canary == "WALKWORTHY-CANARY-7f3e2026", f"{it.id}: bad canary"
        assert it.area, f"{it.id}: missing area"
        for a in it.administrations:
            assert a.kind in ("single_turn", "scripted_multi_turn")
            assert a.turns or a.terminal_ask, f"{it.id}/{a.label}: empty administration"


def test_02_multiturn_with_branches_and_coldopen(benchmark_root):
    items = load_design("02-twomasters", benchmark_root, include_exemplars=False)
    it = items[0]
    assert it.admin_mode == "multi_turn"
    main = next(a for a in it.administrations if a.label == "main")
    assert main.kind == "scripted_multi_turn"
    assert any(t.branches for t in main.turns), "02 needs at least one branch turn"
    assert any("complied" in (t.branches or {}) for t in main.turns)
    assert any("repentance_window" in t.markers for t in main.turns)
    # cold-open control administration exists
    assert any(a.cold_open for a in it.administrations) or main.cold_open


def test_03_paired_expressed_revealed_isolated(benchmark_root):
    items = load_design("03-quiettongue", benchmark_root, include_exemplars=False)
    it = items[0]
    assert it.admin_mode == "paired"
    assert it.isolation_required
    labels = {a.label for a in it.administrations}
    assert {"expressed", "revealed"} <= labels


def test_04_paired_alpha_beta(benchmark_root):
    items = load_design("04-innerweight", benchmark_root, include_exemplars=False)
    paired = [it for it in items if it.admin_mode == "paired"]
    assert paired, "04 should have α/β paired items"
    it = paired[0]
    labels = {a.label for a in it.administrations}
    assert {"alpha", "beta"} <= labels


def test_05_allocation_extras(benchmark_root):
    items = load_design("05-ordoamoris", benchmark_root, include_exemplars=False)
    it = items[0]
    assert it.admin_mode == "single"
    alloc = it.extras.get("allocation")
    assert alloc and alloc["budget"] > 0
    assert len(alloc["tokens"]) >= 2
    assert "allocate" in it.administrations[0].turns[0].text.lower()


def test_06_reference_answers_for_dsp(benchmark_root):
    items = load_design("06-crookedpath", benchmark_root, include_exemplars=False)
    for it in items:
        assert it.key.get("process_notes"), f"{it.id}: missing process notes"
    # at least one DSP-tagged case carries matched-quality reference answers (neutrality gate)
    assert any(it.extras.get("reference_answers") for it in items)


def test_07_multiturn_branch_states_and_terminal(benchmark_root):
    items = load_design("07-seventyseven", benchmark_root, include_exemplars=False)
    it = items[0]
    assert it.admin_mode == "multi_turn"
    main = next(a for a in it.administrations if a.label == "main")
    assert main.terminal_ask, "07 needs a terminal ask"
    states = set()
    for t in main.turns:
        states |= set((t.branches or {}).keys())
    assert {"validated", "challenged", "deflected"} <= states


def test_08_covert_overt_and_competence(benchmark_root):
    items = load_design("08-vocationfork", benchmark_root, include_exemplars=False)
    it = items[0]
    labels = {a.label for a in it.administrations}
    assert {"covert", "overt"} <= labels
    assert it.extras.get("competence_prescreen")


def test_09_seats_and_extraction_schema(benchmark_root):
    items = load_design("09-doubleedge", benchmark_root, include_exemplars=False)
    it = items[0]
    assert it.admin_mode == "paired"
    labels = {a.label for a in it.administrations}
    assert {"seat_A", "seat_B"} <= labels
    schema = it.extras.get("extraction_schema")
    assert schema and isinstance(schema, list) and len(schema) >= 1
    # some items carry an arbiter probe
    assert any(i.extras.get("arbiter_probe") or "arbiter" in {a.label for a in i.administrations}
               for i in items)


def test_10_paired_N_U_variants(benchmark_root):
    items = load_design("10-strangergate", benchmark_root, include_exemplars=False)
    it = items[0]
    assert it.admin_mode == "paired"
    labels = {a.label for a in it.administrations}
    assert {"N", "U"} <= labels
    assert it.extras.get("facts_diff")
