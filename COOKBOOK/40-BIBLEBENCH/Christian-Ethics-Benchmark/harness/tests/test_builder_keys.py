"""RED: builder extraction of machine-readable keyed answers for the metrics.

03 needs the keyed expressed answer (say-do gap "say" side); 04 needs the keyed motive
direction (positive/zero) for the H headroom statistic. These are PARSED from existing
keyed prose — no item content is edited (FIX-MECHANICS-ONLY).
"""
from walkworthy.loader import load_design


def _by_id(design, benchmark_root):
    return {it.id: it for it in load_design(design, benchmark_root, include_exemplars=True)}


def test_03_keyed_expressed_parsed(benchmark_root):
    d = _by_id("03-quiettongue", benchmark_root)
    assert d["WW-03-A04"].key["keyed_expressed"] == ["yes"]
    assert d["WW-03-B03"].key["keyed_expressed"] == ["no"]
    assert d["WW-03-D03"].key["keyed_expressed"] == ["it_depends"]
    # every runnable item carries the field (possibly [] if unparseable) — never missing
    for it in d.values():
        assert "keyed_expressed" in it.key
        assert set(it.key["keyed_expressed"]) <= {"yes", "no", "it_depends"}


def test_03_it_depends_also_defensible_adds_it_depends(benchmark_root):
    d = _by_id("03-quiettongue", benchmark_root)
    # M02 keys No with "It depends" also defensible -> both accepted
    assert set(d["WW-03-M02"].key["keyed_expressed"]) == {"no", "it_depends"}


def test_04_keyed_motive_direction(benchmark_root):
    d = _by_id("04-innerweight", benchmark_root)
    # explicit delta>0 pair -> positive, alpha-favored
    assert d["WW-04-C02"].extras["keyed_motive"] == {"direction": "positive", "favored": "alpha"}
    # VETO pair -> zero direction (bad motive must not swing the assessment)
    assert d["WW-04-F02"].extras["keyed_motive"]["direction"] == "zero"
    # single 4b item -> no pair-delta motive key
    assert d["WW-04-M01"].extras.get("keyed_motive") is None
