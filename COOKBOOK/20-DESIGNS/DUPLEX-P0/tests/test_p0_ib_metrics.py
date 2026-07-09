"""IB-1a / IB-3a / IB-4 / IB-5 wiring (item-bank adversarial-read dispositions; WS-1 §1)."""
from analysis.ib_metrics import (
    affect_primed_pooled,
    within_polarity_cross_domain,
    control_shift_metric,
    PS_DIR_DEFINITION,
)


def _rec(**kw):
    base = dict(refusal=False, score=3.0, monitoring_frame=None, greene_subset=False,
                stance_polarity="affirmative_intervene", content_tags=["harm"],
                is_discriminant_control=False, resource_condition="standard",
                item_id="i1", model_id="m", axis="process")
    base.update(kw)
    return base


def test_ib1a_affect_primed_pooled_only_no_cell_breakdown():
    """IB-1(a): affect_primed enters P0 ONLY as one undifferentiated resource condition (the Ekman
    prime is perfectly aliased with severity×ambiguity); NO by-cell breakdown is produced."""
    recs = [_rec(resource_condition="affect_primed", score=4.0) for _ in range(6)]
    res = affect_primed_pooled(recs)
    assert res["n"] == 6
    assert res["mean_stance"] == 4.0
    assert res["by_cell_breakdown"] is None


def test_ib3a_within_polarity_restricts_to_intervene_keyed():
    """IB-3(a): cross-domain PS-stability must be checked WITHIN polarity class (intervene-keyed
    items only), because stance polarity is aliased with content domain."""
    recs = []
    for c, s in (("extended_thinking", 5.0), ("forced_immediate", 3.0)):
        recs += [_rec(resource_condition=c, score=s, content_tags=["harm"], item_id="h1")
                 for _ in range(4)]
    # a preserve-keyed purity item that must be EXCLUDED from the within-polarity sensitivity
    for c, s in (("extended_thinking", 1.0), ("forced_immediate", 5.0)):
        recs += [_rec(resource_condition=c, score=s, stance_polarity="affirmative_preserve",
                      content_tags=["purity"], item_id="p1") for _ in range(4)]
    res = within_polarity_cross_domain(recs)
    assert res["polarity_class"] == "affirmative_intervene"
    assert "harm" in res["per_domain_process_signature"]
    assert "purity" not in res["per_domain_process_signature"]


def test_ib5_control_shift_metric_over_controls_only():
    """IB-5: a pre-defined COMMENSURABLE shift metric for discriminant-control items (they answer
    on categorical/numeric scales, not the moral 1..5 ordinal)."""
    recs = []
    for c in ("extended_thinking", "forced_immediate"):
        recs += [_rec(resource_condition=c, score=2.0, is_discriminant_control=True, item_id="c1")
                 for _ in range(5)]
    # a moral (non-control) item that must NOT enter the control metric
    recs += [_rec(resource_condition="extended_thinking", score=5.0, item_id="m1") for _ in range(5)]
    res = control_shift_metric(recs)
    assert res["mean_control_shift"] is not None
    assert res["n_control_cells"] == 1  # only the single control cell (c1, m)


def test_ib4_ps_dir_definition_is_intervene_pole():
    """IB-4: PS-dir is defined as shift toward the stance-5 (intervene) pole."""
    assert "intervene" in PS_DIR_DEFINITION.lower()
    assert "greene" in PS_DIR_DEFINITION.lower()
