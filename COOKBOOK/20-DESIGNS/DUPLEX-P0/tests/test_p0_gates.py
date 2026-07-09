"""G1/G2/G3 + run_p0_gates — pass AND fail fixtures for each gate (design §7)."""
import fixtures_p0 as fx
from analysis.gates import (
    process_beats_content,
    pairwise_separation,
    greene_direction,
    run_p0_gates,
    _outlier_guard_ok,
)


# --------------------------------------------------------------------------- G1 (ruling G1-a/G1-b)

def test_g1_pass_process_beats_content():
    res = process_beats_content(fx.g1_pass(), epsilon=0.02)
    assert res["pass"] is True
    assert res["provisional"] is False
    assert res["verdict"] == "PASS"
    assert res["process_cv"] is not None and res["content_cv"] is not None
    assert res["process_cv"] > res["content_cv"]
    assert res["dead_cells"] == []
    assert res["n_models_process"] == 3


def test_g1_content_baseline_is_standard_condition_of_same_items():
    """Ruling G1-a: 'the content baseline = cross-model CV of per-item mean stance in the
    `standard` condition ... Same 48 novel items, same models, same run.' There is NO separate
    content axis; the baseline is the standard-condition stance of the SAME process items. The
    fixture carries only axis=='process' records (+ a standard condition) and yet content_means
    must be populated from those standard scores (~0.50 for every model).
    """
    data = fx.g1_pass()
    assert all(r["axis"] == "process" for r in data)  # no separate 'content' axis exists
    assert any(r["resource_condition"] == "standard" for r in data)
    res = process_beats_content(data)
    assert set(res["content_means"]) == {"mA", "mB", "mC"}
    for m in ("mA", "mB", "mC"):
        assert abs(res["content_means"][m] - 0.50) < 0.05


def test_g1_process_signature_is_per_item_delta_no_cancellation():
    """D5 / G1-a: 'process axis = cross-model CV of per-item condition-deltas'; opposite-sign
    items must NOT cancel before abs(). A model with per-item deltas +0.40 and -0.40 has a
    process signature of 0.40 (mean of |per-item delta|), not ~0 (|pooled mean delta|).
    """
    res = process_beats_content(fx.g1_percel_signature())
    assert abs(res["process_signatures"]["mA"] - 0.40) < 0.03, res["process_signatures"]


def test_g1_roster_intersection_same_models(fx_data=None):
    """D4 / G1-a: 'same models' -- the process and content CVs must be computed over the SAME
    model set. A model with process cells but no standard (content) cells is excluded from BOTH.
    """
    res = process_beats_content(fx.g1_roster_mismatch())
    assert set(res["models_used"]) == {"mA", "mB"}
    assert "mC" not in res["process_signatures"]
    assert "mC" not in res["content_means"]


def test_g1_fail_degenerate_denominator():
    # process homogenized -> near-zero cross-model mean -> guarded CV is None -> FAIL
    res = process_beats_content(fx.g1_fail_degenerate(), epsilon=0.02)
    assert res["process_cv"] is None
    assert res["pass"] is False


def test_g1_fail_content_cv_larger():
    res = process_beats_content(fx.g1_fail_cv(), epsilon=0.02)
    assert res["process_cv"] is not None and res["content_cv"] is not None
    assert res["process_cv"] < res["content_cv"]
    assert res["pass"] is False


def test_g1_dead_cell_excluded_before_cv():
    res = process_beats_content(fx.g1_dead_cell(), epsilon=0.02, sd_dead_threshold=1e-6)
    dead_models = {d["model_id"] for d in res["dead_cells"]}
    assert "mC" in dead_models
    assert "mC" not in res["process_signatures"]
    assert res["n_models_process"] == 2


def test_g1b_thin_base_downgrades_to_provisional():
    """Ruling G1-b: 'If the live fraction of process cells falls below 40%, a numeric G1 pass is
    downgraded to PROVISIONAL (thin base).' The gate still computes a numeric pass but the verdict
    is PROVISIONAL and live_cell_fraction < 0.40.
    """
    res = process_beats_content(fx.g1_provisional_thin_base(), epsilon=0.02)
    assert res["pass"] is True                      # numeric pass on the live mA/mB models
    assert res["live_cell_fraction"] < 0.40
    assert res["provisional"] is True
    assert res["verdict"] == "PROVISIONAL"


def test_g1_unmeasurable_cell_excluded_from_both_num_and_denom():
    """Ruling G1-b / V-4: 'Cells coded UNMEASURABLE under V-4 count in neither numerator nor
    denominator.' A constant (SD~0) cell in a temperature-dropped condition is UNMEASURABLE, not
    DEAD -- it must appear in unmeasurable_cells, NOT dead_cells, and must not lower the live
    fraction denominator.
    """
    res = process_beats_content(
        fx.g1_unmeasurable(), epsilon=0.02, unmeasurable_conditions={"extended_thinking"}
    )
    um = {(c["model_id"], c["condition"]) for c in res["unmeasurable_cells"]}
    assert ("mA", "extended_thinking") in um
    dead = {(d["model_id"]) for d in res["dead_cells"]}
    assert "mA" not in dead                          # mA's SD~0 cell is unmeasurable, not dead
    # mA's pair is excluded from the denominator; only mB/mC live pairs remain -> fraction 1.0
    assert res["live_cell_fraction"] == 1.0


# --------------------------------------------------------------------------- G2

def test_g2_pass_all_pairs_separate():
    res = pairwise_separation(fx.g2_pass(), alpha=0.01, sep_threshold=0.90)
    assert res["pass"] is True
    assert res["frac_separated"] >= 0.90
    assert res["per_condition"]["standard"]["outlier_guard_ok"] is True


def test_g2_fail_converged():
    res = pairwise_separation(fx.g2_fail_converged(), alpha=0.01, sep_threshold=0.90)
    assert res["pass"] is False
    assert res["frac_separated"] < 0.90


def test_g2_fail_one_vs_n_outlier():
    res = pairwise_separation(fx.g2_one_vs_n(), alpha=0.01, sep_threshold=0.90)
    assert res["pass"] is False
    assert res["frac_separated"] < 0.90
    assert res["per_condition"]["standard"]["outlier_guard_ok"] is False


def test_outlier_guard_unit():
    models = ["a", "b", "c", "d"]
    # all pairs separate -> guard OK
    all_sep = {(x, y): True for i, x in enumerate(models) for y in models[i + 1:]}
    assert _outlier_guard_ok(models, all_sep, 0.90) is True
    # only 'a' separates from everyone; the rest are mutually non-separated -> guard FAILS
    one_vs_rest = {(x, y): (x == "a") for i, x in enumerate(models) for y in models[i + 1:]}
    assert _outlier_guard_ok(models, one_vs_rest, 0.90) is False


# --------------------------------------------------------------------------- G3

def test_g3_anchored_pass():
    res = greene_direction(fx.g3_anchored_pass(), human_anchor=1.0)
    assert res["pass_or_fallback"] == "anchored"
    assert res["direction"] == 1
    assert res["pass"] is True


def test_g3_anchored_fail_wrong_direction():
    res = greene_direction(fx.g3_anchored_fail(), human_anchor=1.0)
    assert res["pass_or_fallback"] == "anchored"
    assert res["direction"] == -1
    assert res["pass"] is False


def test_g3_fallback_pass_clear_direction():
    res = greene_direction(fx.g3_fallback_pass(), human_anchor=None)
    assert res["pass_or_fallback"] == "fallback"
    assert res["direction"] == 1
    assert res["pass"] is True


def test_g3_fallback_flat_no_direction():
    res = greene_direction(fx.g3_fallback_flat(), human_anchor=None, min_effect=0.02)
    assert res["pass_or_fallback"] == "fallback"
    assert res["pass"] is False


# --------------------------------------------------------------------------- combiner

def test_run_p0_gates_all_pass():
    cfg = {"g1_epsilon": 0.02, "g2_alpha": 0.01, "g2_sep_threshold": 0.90,
           "g3_human_anchor": 1.0}
    out = run_p0_gates(fx.p0_pass(), cfg)
    assert out["G1"]["pass"] is True
    assert out["G2"]["pass"] is True
    assert out["G3"]["pass"] is True
    assert out["overall_pass"] is True


def test_run_p0_gates_all_pass_fallback_g3():
    # No human anchor -> G3 uses the M3 fallback contrast; still holds on p0_pass.
    out = run_p0_gates(fx.p0_pass(), {"g3_human_anchor": None})
    assert out["G3"]["pass_or_fallback"] == "fallback"
    assert out["overall_pass"] is True


def test_run_p0_gates_fail_on_g2():
    # AND-combiner + config wiring: hold the (passing) data constant, make G2 unreachable via
    # config (sep_threshold > 1). G1 and G3 still hold, but overall must FAIL — all three required.
    cfg = {"g3_human_anchor": 1.0, "g2_sep_threshold": 1.01}
    out = run_p0_gates(fx.p0_pass(), cfg)
    assert out["G1"]["pass"] is True
    assert out["G2"]["pass"] is False
    assert out["G3"]["pass"] is True
    assert out["overall_pass"] is False
