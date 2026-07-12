from analysis.synth_recovery import run_recovery


def test_known_theta_recovery_is_build_blocking_and_passes_thresholds():
    report = run_recovery(seed=20260711, repeats_per_structure=15)
    assert report["provenance"] == "harness validation, NOT a measurement"
    assert report["thresholds"] == {
        "minimum_theta_correlation": 0.90,
        "maximum_theta_rmse": 0.30,
        "minimum_information_rank": 15,
    }
    assert report["information_rank"] >= 15
    assert report["n_rows"] == 600
    assert report["actual_structure_count"] == 40
    assert report["design_source"] == "lib.blocks.build_deep_structures"
    assert report["theta_correlation"] >= 0.90
    assert report["theta_rmse"] <= 0.30
    assert report["build_gate_pass"] is True
    assert abs(sum(report["estimated_theta"].values())) < 1e-8


def test_recovery_is_deterministic_for_a_fixed_seed():
    first = run_recovery(seed=17, repeats_per_structure=15)
    second = run_recovery(seed=17, repeats_per_structure=15)
    assert first == second
