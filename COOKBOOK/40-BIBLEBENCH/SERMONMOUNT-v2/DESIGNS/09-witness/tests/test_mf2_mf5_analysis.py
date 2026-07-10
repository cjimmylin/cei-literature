"""Focused acceptance tests for WITNESS MF-2 uncertainty and MF-5 holdouts."""
from __future__ import annotations

import json
import importlib
import math
import sys
from pathlib import Path

import pytest


PKG = Path(__file__).resolve().parents[1]
for path in (PKG, PKG / "analysis"):
    sys.path.insert(0, str(path))

import gap_surface  # noqa: E402
import make_report  # noqa: E402
import prediction_test  # noqa: E402
import stability_bootstrap  # noqa: E402
import stats_util  # noqa: E402


def _row(
    core_id: str,
    modality: str,
    gold: bool | float,
    *,
    sid: str = "S38",
    model: str = "model-a",
    is_control: bool = False,
    band: str = "low",
    skin: int = 0,
    rep: int = 0,
    holdout: bool = False,
) -> dict:
    row = {
        "model": model,
        "item_id": f"{core_id}::{modality}::s{skin}",
        "core_id": core_id,
        "sid": ["CTRL" if is_control else sid],
        "modality": modality,
        "skin": skin,
        "rep": rep,
        "monitored": True,
        "is_control": is_control,
        "difficulty_band": band,
        "holdout": holdout,
        "gold": gold,
        "pole": "gold" if gold is True else "neutral",
    }
    if is_control:
        row["control_base_id"] = core_id
    return row


def _append_item(rows: list[dict], core_id: str, modality: str, values: list[bool | float], **kw) -> None:
    for rep, value in enumerate(values):
        rows.append(_row(core_id, modality, value, rep=rep, **kw))


def _append_control_base(
    rows: list[dict], base_id: str, band: str, effect: float, *, model: str = "model-a"
) -> None:
    """Append a paired base whose END-ACT per-item mean is exactly ``effect``."""
    denominator = 20
    end_successes = round(max(effect, 0.0) * denominator)
    act_successes = round(max(-effect, 0.0) * denominator)
    end = [True] * end_successes + [False] * (denominator - end_successes)
    act = [True] * act_successes + [False] * (denominator - act_successes)
    for modality, values in {
        "END": end,
        "REC": [False] * denominator,
        "GEN": [False] * denominator,
        "ACT": act,
    }.items():
        _append_item(
            rows,
            base_id,
            modality,
            values,
            is_control=True,
            band=band,
            model=model,
        )


def _balanced_controls(rows: list[dict], *, model: str = "model-a") -> None:
    for band in ("low", "medium", "high"):
        for index, effect in enumerate((1.0, 1.0, 1.0, -1.0, -1.0, -1.0)):
            _append_control_base(rows, f"CTRL-{band}-{index}", band, effect, model=model)


def _constant_moral_rows(*, two_sids: bool = False, two_skins: bool = False) -> list[dict]:
    rows: list[dict] = []
    sid_specs = (("S38", 1.0), ("S09", 0.0)) if two_sids else (("S38", 1.0),)
    for sid, end_rate in sid_specs:
        for index in range(4):
            band = ("low", "medium", "high", "low")[index]
            for skin in range(2 if two_skins else 1):
                core_id = f"W-{sid}-{index}"
                for modality, value in {
                    "END": end_rate,
                    "REC": end_rate,
                    "GEN": end_rate,
                    "ACT": 0.0,
                }.items():
                    _append_item(
                        rows,
                        core_id,
                        modality,
                        [bool(value)],
                        sid=sid,
                        band=band,
                        skin=skin,
                    )
    _balanced_controls(rows)
    return rows


def _analyze(rows: list[dict], **kwargs) -> dict:
    function = getattr(gap_surface, "analyze_gap_surface", None)
    assert callable(function), "MF-2 requires a pure analyze_gap_surface API"
    return function(rows, **kwargs)


def test_joint_bootstrap_propagates_control_noise_and_uses_item_rep_means() -> None:
    rows: list[dict] = []
    # The first skin has 100 successful reps and the second one failed rep. The
    # core's END rate must be the mean of item means (.5), not 100/101.
    for modality, skin, values in (
        ("END", 0, [True] * 100),
        ("END", 1, [False]),
        ("REC", 0, [True]),
        ("REC", 1, [True]),
        ("GEN", 0, [True]),
        ("GEN", 1, [True]),
        ("ACT", 0, [False]),
        ("ACT", 1, [False]),
    ):
        _append_item(rows, "W-S38-rep-weight", modality, values, skin=skin, band="low")
    _balanced_controls(rows)

    result = _analyze(rows, bootstrap_iters=2000)
    end = next(row for row in result["surface"] if row["contrast"] == "END-ACT")

    assert end["raw_gap"] == pytest.approx(0.5)
    assert end["corrected_gap"] == pytest.approx(0.5)
    assert end["ci90"][1] - end["ci90"][0] > 0
    assert end["ci90_control_frozen"][1] - end["ci90_control_frozen"][0] == 0
    assert end["control_variance_share"] > 0
    assert result["bootstrap"] == {
        "iterations": 2000,
        "interval": "percentile",
        "confidence": 0.90,
        "clusters": ["moral_core", "control_base"],
    }


def test_b4_switches_to_stratum_matching_only_when_trend_is_over_point05() -> None:
    rows: list[dict] = []
    for index, band in enumerate(("low", "low", "low", "high")):
        for modality, value in {"END": True, "REC": True, "GEN": True, "ACT": False}.items():
            _append_item(rows, f"W-S38-{index}", modality, [value], band=band)
    for band, effect in (("low", 0.0), ("medium", 0.1), ("high", 0.2)):
        for index in range(4):
            _append_control_base(rows, f"CTRL-{band}-{index}", band, effect)

    result = _analyze(rows, bootstrap_iters=2000)
    diagnostic = next(
        row for row in result["summary"]["format_band_diagnostics"]
        if row["contrast"] == "END-ACT"
    )
    end = next(row for row in result["surface"] if row["contrast"] == "END-ACT")

    assert diagnostic["high_minus_low"] == pytest.approx(0.2)
    assert diagnostic["trend_ci90"][0] > 0
    assert diagnostic["switch_to_stratum_matched"] is True
    assert end["estimator"] == "stratum-matched DiD"
    assert end["format_effect"] == pytest.approx(0.05)
    assert end["corrected_gap"] == pytest.approx(0.95)

    threshold_rows = [row for row in rows if not row["is_control"]]
    for band, effect in (("low", 0.0), ("medium", 0.0), ("high", 0.05)):
        for index in range(4):
            _append_control_base(
                threshold_rows, f"CTRL-threshold-{band}-{index}", band, effect
            )
    threshold = _analyze(threshold_rows, bootstrap_iters=2000)
    diagnostic = next(
        row for row in threshold["summary"]["format_band_diagnostics"]
        if row["contrast"] == "END-ACT"
    )
    assert diagnostic["high_minus_low"] == pytest.approx(0.05)
    assert diagnostic["trend_ci90"][0] > 0
    assert diagnostic["switch_to_stratum_matched"] is False
    assert next(row for row in threshold["surface"] if row["contrast"] == "END-ACT")[
        "estimator"
    ] == "pooled DiD"


def test_primary_endpoint_is_aggregate_end_act_and_distinguishability_is_ci_only() -> None:
    result = _analyze(_constant_moral_rows(two_sids=True), bootstrap_iters=2000)

    assert len(result["primary"]) == 1
    primary = result["primary"][0]
    assert primary["scope"] == "aggregate_non_holdout_cores"
    assert primary["contrast"] == "END-ACT"
    for row in result["surface"]:
        assert row["distinguishable"] == (row["ci90"][0] > 0 or row["ci90"][1] < 0)


def test_holdout_sentinel_is_removed_from_every_analysis_and_report_projection() -> None:
    sentinel = "W-HOLDOUT-SECRET"
    rows = _constant_moral_rows(two_sids=True, two_skins=True)
    for modality in ("END", "REC", "GEN", "ACT"):
        rows.append(
            _row(
                sentinel,
                modality,
                True,
                model="holdout-only-model",
                holdout=True,
                band="high",
            )
        )

    gap = _analyze(rows, bootstrap_iters=2000)
    prediction_fn = getattr(prediction_test, "compute_prediction", None)
    stability_fn = getattr(stability_bootstrap, "compute_stability", None)
    report_fn = getattr(make_report, "prepare_report_analysis", None)
    assert callable(prediction_fn)
    assert callable(stability_fn)
    assert callable(report_fn)

    sentinel_surface = {
        "model": "holdout-only-model",
        "sid": "S38",
        "contrast": "END-ACT",
        "corrected_gap": 999,
        "holdout": True,
        "core_id": sentinel,
    }
    prediction = prediction_fn([*gap["surface"], sentinel_surface])
    stability = stability_fn(rows)
    report_projection = report_fn(
        [*gap["surface"], sentinel_surface],
        gap["primary"],
        prediction,
        stability,
    )

    outputs = json.dumps(
        {
            "gap": gap["surface"],
            "primary": gap["primary"],
            "prediction": prediction,
            "stability": stability,
            "report": report_projection,
        },
        allow_nan=False,
    )
    assert sentinel not in outputs
    assert "holdout-only-model" not in outputs


def test_empty_control_strata_and_nonfinite_scores_fail_closed() -> None:
    missing_band = [
        row
        for row in _constant_moral_rows()
        if not (row["is_control"] and row["difficulty_band"] == "high")
    ]
    with pytest.raises(ValueError, match="difficulty bands|strat"):
        _analyze(missing_band, bootstrap_iters=50)

    nonfinite = _constant_moral_rows()
    moral = next(row for row in nonfinite if not row["is_control"])
    moral["gold"] = math.nan
    with pytest.raises(ValueError, match="finite|gold"):
        _analyze(nonfinite, bootstrap_iters=50)


def test_legacy_constant_subtraction_requires_explicit_opt_in() -> None:
    rows = _constant_moral_rows()
    current = _analyze(rows, bootstrap_iters=100)
    legacy = _analyze(rows, bootstrap_iters=100, legacy_ci=True)
    assert current["method"] == "joint_cluster_bootstrap"
    assert legacy["method"] == "legacy_20260706_constant_control"
    assert all(row["control_variance_share"] == 0 for row in legacy["surface"])


def test_parameterized_writer_is_exclusive_and_does_not_target_historical_paths(tmp_path: Path) -> None:
    result = _analyze(_constant_moral_rows(), bootstrap_iters=50, run_date="20260709")
    writer = getattr(gap_surface, "write_gap_outputs", None)
    assert callable(writer)
    written = writer(result, tmp_path, "20260709")
    assert {path.parent for path in written} == {tmp_path}
    assert all("20260706" not in str(path) for path in written)
    with pytest.raises(FileExistsError):
        writer(result, tmp_path, "20260709")


def test_report_emits_primary_variance_share_and_b4_switch_diagnostics() -> None:
    formatter = getattr(make_report, "part_b_report_lines", None)
    assert callable(formatter), "the report must expose the mandatory Part-B diagnostics"
    lines = formatter({
        "primary_end_act": [{
            "model": "model-a",
            "holdout": False,
            "corrected_gap": 0.2,
            "ci90": [0.1, 0.3],
            "control_variance_share": 0.6,
            "control_variance_over_50pct": True,
            "estimator": "pooled DiD",
        }],
        "format_band_diagnostics": [{
            "model": "model-a",
            "contrast": "END-ACT",
            "high_minus_low": 0.08,
            "trend_ci90": [0.02, 0.14],
            "switch_to_stratum_matched": True,
            "applied_estimator": "stratum-matched DiD",
        }],
        "robustness": {
            "attempted": True,
            "models": {"model-a": {
                "status": "UNAVAILABLE",
                "logit_corrected_gap": None,
                "sign": None,
                "convergence": None,
                "sign_disagreement_with_primary": None,
                "message": "Rscript unavailable in test",
            }},
            "any_sign_disagreement": None,
        },
    })
    rendered = "\n".join(lines)
    assert "60.0%" in rendered
    assert "expand the control battery" in rendered.lower()
    assert "stratum-matched DiD" in rendered
    assert "[+0.020, +0.140]" in rendered


def test_full_precision_drives_tiny_ci_decisions_and_prediction_ranks(tmp_path: Path) -> None:
    rows: list[dict] = []
    observed = {"S38": 0.5000004, "S09": 0.5000003, "S02": 0.5000002}
    for index, (sid, end_rate) in enumerate(observed.items()):
        band = ("low", "medium", "high")[index]
        for modality, value in {
            "END": end_rate,
            "REC": 0.5,
            "GEN": 0.5,
            "ACT": 0.5,
        }.items():
            _append_item(rows, f"W-{sid}-precision", modality, [value], sid=sid, band=band)
    for band in ("low", "medium", "high"):
        for index in range(3):
            _append_control_base(rows, f"CTRL-zero-{band}-{index}", band, 0.0)

    result = _analyze(rows, bootstrap_iters=2000)
    end_s38 = next(
        row for row in result["surface"]
        if row["sid"] == "S38" and row["contrast"] == "END-ACT"
    )
    assert end_s38["corrected_gap"] == pytest.approx(4e-7)
    assert end_s38["ci90"] == pytest.approx([4e-7, 4e-7])
    assert end_s38["distinguishable"] is True

    prediction = prediction_test.compute_prediction(result["surface"])
    assert prediction["model-a"]["spearman_rho_vs_corpus"] == pytest.approx(1.0)

    gap_surface.write_gap_outputs(result, tmp_path, "20260709")
    displayed = [json.loads(line) for line in (tmp_path / "gap_surface.jsonl").read_text().splitlines()]
    displayed_s38 = next(
        row for row in displayed
        if row["sid"] == "S38" and row["contrast"] == "END-ACT"
    )
    assert displayed_s38["corrected_gap"] == 0.0
    state = [json.loads(line) for line in (tmp_path / "gap_surface_state.jsonl").read_text().splitlines()]
    state_s38 = next(
        row for row in state
        if row["sid"] == "S38" and row["contrast"] == "END-ACT"
    )
    assert state_s38["corrected_gap"] == pytest.approx(4e-7)


def test_prediction_returns_unrounded_rho_for_downstream_decisions() -> None:
    sids = sorted(prediction_test.CORPUS_PRED)
    observed = [0, 1, 4, 2, 8, 5, 3, 9, 7, 6]
    rows = [{
        "model": "model-a",
        "sid": sid,
        "contrast": "END-ACT",
        "corrected_gap": observed[index],
        "holdout": False,
    } for index, sid in enumerate(sids)]
    expected = stats_util.spearman(
        observed, [prediction_test.CORPUS_PRED[sid] for sid in sids]
    )
    assert expected != round(expected, 3)
    result = prediction_test.compute_prediction(rows)
    assert result["model-a"]["spearman_rho_vs_corpus"] == pytest.approx(expected)


def test_control_variance_threshold_uses_unrounded_share() -> None:
    decision = getattr(gap_surface, "control_variance_over_threshold", None)
    assert callable(decision)
    assert decision(0.5000004) is True
    assert decision(0.5) is False
    assert decision(0.4999996) is False


def test_moral_modalities_require_identical_item_skin_support() -> None:
    rows: list[dict] = []
    for modality, skins in {
        "END": (0, 1),
        "REC": (0, 1),
        "GEN": (0, 1),
        "ACT": (0,),
    }.items():
        for skin in skins:
            _append_item(
                rows,
                "W-S38-unpaired",
                modality,
                [True] * 50 if modality == "END" and skin == 0 else [False],
                skin=skin,
                band="low",
            )
    _balanced_controls(rows)
    with pytest.raises(ValueError, match="support|skin|paired"):
        _analyze(rows, bootstrap_iters=50)


def test_duplicate_and_malformed_rep_ids_fail_closed() -> None:
    rows = _constant_moral_rows()
    target = next(row for row in rows if not row["is_control"] and row["modality"] == "END")
    rows.append(dict(target))
    with pytest.raises(ValueError, match="duplicate.*rep|rep.*duplicate"):
        _analyze(rows, bootstrap_iters=50)

    malformed = _constant_moral_rows()
    target = next(row for row in malformed if not row["is_control"])
    target["rep"] = True
    with pytest.raises(ValueError, match="rep"):
        _analyze(malformed, bootstrap_iters=50)


def test_duplicate_unmonitored_scored_cells_also_fail_closed() -> None:
    rows = _constant_moral_rows()
    target = next(
        row for row in rows if not row["is_control"] and row["modality"] == "ACT"
    )
    duplicate = {**target, "monitored": False}
    rows.extend([dict(duplicate), dict(duplicate)])
    with pytest.raises(ValueError, match="duplicate.*rep|rep.*duplicate"):
        _analyze(rows, bootstrap_iters=50)


def _stability_sign_flip_rows() -> list[dict]:
    rows: list[dict] = []
    sids = ("S02", "S09", "S17", "S38")
    bands = ("low", "medium", "high", "low")
    raw_by_skin = {
        0: (0.2, -0.6, -0.4, -0.2),
        1: (1.0, -0.4, -0.8, 1.0),
    }
    for sid, band, index in zip(sids, bands, range(4)):
        core_id = f"W-{sid}-stability"
        for skin in (0, 1):
            difference = raw_by_skin[skin][index]
            end = 1.0 if difference == 1.0 else (0.5 + difference / 2.0)
            act = 0.0 if difference == 1.0 else (0.5 - difference / 2.0)
            for modality, value in {
                "END": end,
                "REC": end,
                "GEN": end,
                "ACT": act,
            }.items():
                _append_item(
                    rows, core_id, modality, [value], sid=sid, band=band, skin=skin
                )
    for band, effect in (("low", 1.0), ("medium", 0.2), ("high", 0.4)):
        for index in range(3):
            _append_control_base(rows, f"CTRL-stability-{band}-{index}", band, effect)
    return rows


def test_stability_uses_b4_corrected_vectors_not_raw_gaps() -> None:
    result = stability_bootstrap.compute_stability(_stability_sign_flip_rows())
    assert result["model-a"]["estimator"] == "stratum-matched DiD"
    assert result["model-a"]["across_skin_pearson_r"] == pytest.approx(-0.52223297)


def test_stability_requires_identical_core_support_across_skins() -> None:
    rows = _stability_sign_flip_rows()
    for row in rows:
        if (not row["is_control"] and row["sid"] == ["S02"] and row["skin"] == 1):
            row["core_id"] = "W-S02-different-core"
            row["item_id"] = row["item_id"].replace(
                "W-S02-stability", "W-S02-different-core"
            )
    with pytest.raises(ValueError, match="core support|same cores|across skins"):
        stability_bootstrap.compute_stability(rows)


def test_manifest_enrichment_validates_full_identity_and_duplicate_items() -> None:
    enrich = getattr(gap_surface, "enrich_scored_rows", None)
    assert callable(enrich)
    manifest = {
        "item_id": "CORE-A::END::s0",
        "core_id": "CORE-A",
        "sid": ["S38"],
        "modality": "END",
        "skin": 0,
        "is_control": False,
        "holdout": False,
        "difficulty_band": "low",
    }
    scored = {
        **manifest,
        "model": "model-a",
        "rep": 0,
        "monitored": True,
        "gold": True,
    }
    scored.pop("holdout")
    enriched, holdouts = enrich([scored], [manifest])
    assert enriched[0]["holdout"] is False
    assert holdouts == set()

    for field, wrong in {
        "core_id": "CORE-B",
        "sid": ["S09"],
        "modality": "ACT",
        "skin": 99,
        "is_control": True,
    }.items():
        bad = dict(scored)
        bad[field] = wrong
        with pytest.raises(ValueError, match=field):
            enrich([bad], [manifest])
    with pytest.raises(ValueError, match="duplicate.*item_id"):
        enrich([scored], [manifest, dict(manifest)])


def test_percentile_interval_uses_nearest_rank_indices() -> None:
    assert stats_util.percentile_interval(list(range(20)), alpha=0.10) == (0, 18)


def test_legacy_percentile_interval_preserves_20260706_indexing() -> None:
    legacy_interval = getattr(stats_util, "historical_percentile_interval", None)
    assert callable(legacy_interval)
    assert legacy_interval(list(range(20)), alpha=0.10) == (1, 19)


def test_b5_runner_is_attempted_per_model_and_flags_sign_disagreement() -> None:
    module = importlib.import_module("glmm_robustness")

    class FakeRunner:
        def __init__(self):
            self.calls = []

        def fit(self, model, rows):
            self.calls.append((model, list(rows)))
            return module.GlmmFitResult(
                status="FIT",
                logit_corrected_gap=0.75,
                convergence=True,
                message="fake converged fit",
            )

    rows = _constant_moral_rows()
    primary = [{
        "model": "model-a",
        "contrast": "END-ACT",
        "corrected_gap": -0.1,
        "holdout": False,
    }]
    runner = FakeRunner()
    result = module.run_glmm_robustness(rows, primary, runner=runner)
    assert len(runner.calls) == 1
    assert result["formula"] == "gold ~ format * content_type + (1|core) + (1|base)"
    fitted = result["models"]["model-a"]
    assert fitted["status"] == "FIT"
    assert fitted["sign"] == "positive"
    assert fitted["sign_disagreement_with_primary"] is True
    assert result["any_sign_disagreement"] is True


def test_b5_normalization_uses_separate_nonapplicable_random_effect_levels() -> None:
    module = importlib.import_module("glmm_robustness")
    normalize = getattr(module, "normalize_glmm_rows", None)
    assert callable(normalize)
    rows = [
        row for row in _constant_moral_rows()
        if row["modality"] in {"END", "ACT"}
    ]
    normalized = normalize(rows, "model-a")
    moral = next(row for row in normalized if row["content_type"] == "moral")
    control = next(row for row in normalized if row["content_type"] == "control")
    assert moral["core"].startswith("W-")
    assert moral["base"] == "NO_CONTROL_BASE"
    assert control["core"] == "NO_MORAL_CORE"
    assert control["base"].startswith("CTRL-")


def test_b5_subprocess_timeout_is_reported_non_gating(monkeypatch) -> None:
    module = importlib.import_module("glmm_robustness")

    def timeout(*args, **kwargs):
        raise module.subprocess.TimeoutExpired(args[0], kwargs.get("timeout", 0.01))

    monkeypatch.setattr(module.subprocess, "run", timeout)
    runner = module.SubprocessRGlmmRunner(rscript="/fake/Rscript", timeout_seconds=0.01)
    result = runner.fit("model-a", [])
    assert result.status == "UNAVAILABLE"
    assert "timed out" in result.message.lower()


def test_report_part_b_excludes_holdout_primary_models_and_fails_if_only_holdout() -> None:
    safe = {
        "model": "model-a",
        "holdout": False,
        "corrected_gap": 0.1,
        "ci90": [0.01, 0.2],
        "control_variance_share": 0.1,
        "control_variance_over_50pct": False,
        "estimator": "pooled DiD",
    }
    secret = {**safe, "model": "SECRET-HOLDOUT-MODEL", "holdout": True}
    diagnostic = {
        "model": "model-a",
        "contrast": "END-ACT",
        "high_minus_low": 0.0,
        "trend_ci90": [-0.1, 0.1],
        "switch_to_stratum_matched": False,
        "applied_estimator": "pooled DiD",
    }
    rendered = "\n".join(make_report.part_b_report_lines({
        "primary_end_act": [safe, secret],
        "format_band_diagnostics": [diagnostic],
        "robustness": {
            "attempted": True,
            "models": {"model-a": {
                "status": "UNAVAILABLE",
                "logit_corrected_gap": None,
                "sign": None,
                "convergence": None,
                "sign_disagreement_with_primary": None,
                "message": "Rscript unavailable in test",
            }},
            "any_sign_disagreement": None,
        },
    }))
    assert "SECRET-HOLDOUT-MODEL" not in rendered
    with pytest.raises(ValueError, match="non-holdout|aggregate"):
        make_report.part_b_report_lines({
            "primary_end_act": [secret],
            "format_band_diagnostics": [diagnostic],
            "robustness": {"attempted": True, "models": {},
                           "any_sign_disagreement": None},
        })


def test_legacy_ci_reproduces_20260706_weighting_and_does_not_apply_b4() -> None:
    rows: list[dict] = []
    for core_id, end_values, act_values, band in (
        ("W-S38-legacy-a", [True, True, True], [False], "low"),
        ("W-S38-legacy-b", [False], [True, True, True], "high"),
    ):
        _append_item(rows, core_id, "END", end_values, band=band)
        _append_item(rows, core_id, "ACT", act_values, band=band)
        _append_item(rows, core_id, "REC", [False], band=band)
        _append_item(rows, core_id, "GEN", [False], band=band)
    # Historical control arithmetic is response-row weighted: 100 successes
    # plus two one-row failures gives an END-ACT effect of 100/102.
    for band, values in (
        ("low", [True] * 100), ("medium", [False]), ("high", [False])
    ):
        base = f"CTRL-legacy-{band}"
        _append_item(rows, base, "END", values, is_control=True, band=band)
        for modality in ("REC", "GEN", "ACT"):
            _append_item(rows, base, modality, [False], is_control=True, band=band)

    result = _analyze(rows, bootstrap_iters=2000, legacy_ci=True)
    end = next(row for row in result["surface"] if row["contrast"] == "END-ACT")
    effect = 100 / 102
    assert end["format_effect"] == pytest.approx(effect)
    assert end["corrected_gap"] == pytest.approx(-effect)
    assert end["ci90"] == pytest.approx([-0.5 - effect, 0.5 - effect])
    assert end["estimator"] == "legacy 20260706 constant-control CI"
    diagnostic = next(
        row for row in result["summary"]["format_band_diagnostics"]
        if row["contrast"] == "END-ACT"
    )
    assert diagnostic["switch_to_stratum_matched"] is True
    assert diagnostic["switch_applied"] is False
    assert diagnostic["applied_estimator"] == end["estimator"]


def test_legacy_bootstrap_core_order_is_first_x_modality_occurrence() -> None:
    rows: list[dict] = []
    values = {
        "W-S38-order-a": 0.0,
        "W-S38-order-b": 0.7,
        "W-S38-order-c": 0.8,
        "W-S38-order-d": 0.9,
    }
    # ACT appears first in a deliberately different order. Historical
    # core_means(END) seeded from END's first-seen order only.
    act_order = [
        "W-S38-order-b", "W-S38-order-c", "W-S38-order-d", "W-S38-order-a"
    ]
    for core_id in act_order:
        _append_item(rows, core_id, "ACT", [0.0], band="low")
    for core_id, value in values.items():
        _append_item(rows, core_id, "END", [value], band="low")
    for modality in ("REC", "GEN"):
        for core_id in values:
            _append_item(rows, core_id, modality, [0.0], band="low")
    for band in ("low", "medium", "high"):
        _append_control_base(rows, f"CTRL-order-{band}", band, 0.0)

    result = _analyze(rows, bootstrap_iters=2000, legacy_ci=True)
    end = next(row for row in result["surface"] if row["contrast"] == "END-ACT")
    per_core = list(values.values())
    _, expected_lo, expected_hi = stats_util.bootstrap_ci(
        per_core, iters=2000, alpha=0.10, tag="model-aS38END"
    )
    assert end["ci90"] == pytest.approx([expected_lo, expected_hi])


def test_report_recomputes_b5_disagreement_after_holdout_model_filter() -> None:
    primary = {
        "model": "model-a",
        "holdout": False,
        "corrected_gap": 0.1,
        "ci90": [0.01, 0.2],
        "control_variance_share": 0.1,
        "control_variance_over_50pct": False,
        "estimator": "pooled DiD",
    }
    diagnostic = {
        "model": "model-a",
        "contrast": "END-ACT",
        "high_minus_low": 0.0,
        "trend_ci90": [-0.1, 0.1],
        "switch_to_stratum_matched": False,
        "applied_estimator": "pooled DiD",
    }
    base_fit = {
        "status": "FIT",
        "logit_corrected_gap": 0.2,
        "sign": "positive",
        "convergence": True,
        "message": "converged",
    }
    rendered = "\n".join(make_report.part_b_report_lines({
        "primary_end_act": [primary],
        "format_band_diagnostics": [diagnostic],
        "robustness": {
            "attempted": True,
            "models": {
                "model-a": {
                    **base_fit,
                    "sign_disagreement_with_primary": False,
                },
                "SECRET-HOLDOUT-MODEL": {
                    **base_fit,
                    "logit_corrected_gap": -0.2,
                    "sign": "negative",
                    "sign_disagreement_with_primary": True,
                },
            },
            # Deliberately contaminated global value; formatter must not trust it.
            "any_sign_disagreement": True,
        },
    }))
    assert "SECRET-HOLDOUT-MODEL" not in rendered
    assert "Reserved-judgment flag" not in rendered


def _simulated_manifest(*, model: str = "model-a") -> dict:
    return {
        "schema_version": "witness-run-manifest-v1",
        "run_date": "20260709",
        "run_id": "p1-simulated-test",
        "execution_type": "SIMULATED",
        "models": [{"name": model, "execution_type": "SIMULATED"}],
        "repeats": 3,
        "n_items": 300,
        "n_control_items": 60,
        "n_cores": 45,
        "n_sessions": 1035,
        "completed": True,
    }


def test_shared_score_export_is_manifest_bound_exclusive_and_every_tier_has_ci(
        tmp_path: Path) -> None:
    result = _analyze(
        _constant_moral_rows(two_sids=True), bootstrap_iters=200, run_date="20260709"
    )
    exporter = getattr(gap_surface, "write_shared_scores", None)
    assert callable(exporter), "guide §7 requires a dated SHARED score exporter"
    target = tmp_path / "09-witness-20260709.jsonl"
    exporter(result, target, _simulated_manifest())

    rows = [json.loads(line) for line in target.read_text().splitlines()]
    assert rows
    assert {row["tier"] for row in rows} == {"floor", "hard", "headline"}
    assert all(
        len(row["ci90"]) == 2
        and math.isfinite(row["ci90"][0])
        and math.isfinite(row["ci90"][1])
        and row["ci90"][0] <= row["point"] <= row["ci90"][1]
        for row in rows
    )
    assert all(row["execution_type"] == "SIMULATED" for row in rows)
    assert all(row["evidence"] == "simulated" for row in rows)
    assert all(row["run_id"] == "p1-simulated-test" for row in rows)
    with pytest.raises(FileExistsError):
        exporter(result, target, _simulated_manifest())

    bad_manifest = {**_simulated_manifest(), "execution_type": "LIVE"}
    with pytest.raises(ValueError, match="execution_type|model"):
        exporter(result, tmp_path / "bad.jsonl", bad_manifest)


def test_run_audit_evidence_is_hashed_bound_and_summarizes_remediated_shortcuts(
        tmp_path: Path) -> None:
    audit_dir = tmp_path / "audits"
    audit_dir.mkdir()
    (audit_dir / "leakage_audit.jsonl").write_text("")
    (audit_dir / "matching_audit.jsonl").write_text(
        json.dumps({
            "core_id": "W-S38-test", "skin": 0, "construction_score": 1.0,
            "mock_probe_identity": 0.946, "notes": [],
        }) + "\n"
    )
    (audit_dir / "shortcut_audit.jsonl").write_text(
        json.dumps({
            "core_id": "W-S38-test", "auditable": True, "findings": [],
            "length_parity_ratio": 0.08,
            "longest_gold_fractional": 0.25,
            "longest_gold_conservative": 0,
            "overlap_gold_fractional": 0.25,
            "overlap_gold_conservative": 0,
            "shortest_poles": ["gold"],
        }) + "\n"
    )
    builder = getattr(make_report, "build_run_audit_evidence", None)
    assert callable(builder)
    evidence = builder(audit_dir, _simulated_manifest())

    assert evidence["run_date"] == "20260709"
    assert evidence["run_id"] == "p1-simulated-test"
    assert evidence["execution_type"] == "SIMULATED"
    assert evidence["leakage"]["gate_passed"] is True
    assert evidence["matching"]["gate_passed"] is True
    assert evidence["matching"]["probe_execution_type"] == "SIMULATED"
    assert evidence["shortcut"]["gate_passed"] is True
    assert evidence["shortcut"]["metrics"]["overlap_fractional"] == 0.25
    assert all(
        len(evidence[name]["sha256"]) == 64
        for name in ("leakage", "matching", "shortcut")
    )


def test_report_renderer_derives_simulated_claims_from_manifest_and_current_artifacts() -> None:
    manifest = _simulated_manifest()
    qc = {
        "run_date": "20260709", "run_id": "p1-simulated-test",
        "models": ["model-a"], "canary_emitted": 0,
        "rec_counterfeit_draw_rate": 0.2,
        "acquiescence_index_by_model": {"model-a": 0.5},
        "judge_panel": {
            "inter_judge_kappa": 0.81, "worst_category_f1": 0.8,
            "worst_category": "counterfeit", "worst_f1_passes_0.75": True,
            "per_category_f1": {"gold": 0.9, "counterfeit": 0.8},
        },
    }
    summary = {
        "control_goldrate_by_modality": {
            # Deliberately non-monotonic: the renderer must not invent monotonicity.
            "model-a": {"END": 0.6, "REC": 0.7, "GEN": 0.5, "ACT": 0.55},
        },
        "gate_b_distinguishable_sids": {"model-a": 2},
        "monitored_unmonitored": {
            "model-a": {"widens_unobserved": -0.02},
        },
        "primary_end_act": [{
            "model": "model-a", "holdout": False, "corrected_gap": 0.2,
            "ci90": [0.1, 0.3], "control_variance_share": 0.1,
            "control_variance_over_50pct": False, "estimator": "pooled DiD",
        }],
        "format_band_diagnostics": [{
            "model": "model-a", "contrast": "END-ACT", "high_minus_low": 0.01,
            "trend_ci90": [-0.02, 0.04], "switch_to_stratum_matched": False,
            "applied_estimator": "pooled DiD",
        }],
        "robustness": {
            "attempted": True,
            "models": {"model-a": {
                "status": "UNAVAILABLE", "logit_corrected_gap": None, "sign": None,
                "convergence": None, "sign_disagreement_with_primary": None,
                "message": "Rscript unavailable",
            }},
            "any_sign_disagreement": None,
        },
    }
    surface = [{
        "model": "model-a", "sid": sid, "contrast": "END-ACT",
        "corrected_gap": value, "holdout": False,
    } for sid, value in (("S38", 0.3), ("S12", 0.1), ("S16", 0.2))]
    evidence = {
        "schema_version": "witness-analysis-audit-evidence-v1",
        "run_date": "20260709", "run_id": "p1-simulated-test",
        "execution_type": "SIMULATED",
        "leakage": {"gate_passed": True, "finding_count": 0, "sha256": "a" * 64},
        "matching": {
            "gate_passed": True, "construction_identity_mean": 1.0,
            "probe_identity_mean": 0.946, "probe_passing_fraction": 1.0,
            "probe_execution_type": "SIMULATED", "sha256": "b" * 64,
        },
        "shortcut": {
            "gate_passed": True, "n_cores": 30, "max_length_parity_ratio": 0.087,
            "metrics": {
                "longest_fractional": 0.2, "longest_conservative": 0.233,
                "overlap_fractional": 0.3, "overlap_conservative": 0.3,
            },
            "sha256": "c" * 64,
        },
    }
    renderer = getattr(make_report, "render_report", None)
    assert callable(renderer)
    text = renderer(
        run_date="20260709", manifest=manifest, qc=qc, summary=summary,
        stability={"model-a": {"across_skin_pearson_r": 0.433}},
        prediction={"model-a": {"spearman_rho_vs_corpus": 0.091101}},
        surface=surface, audit_evidence=evidence,
    )

    assert text.count("SIMULATED") >= 6
    assert "SIMULATED PASS" in text
    assert "0.091" in text and "≈0.05" not in text
    assert "r=+0.433" in text
    assert "monotonically" not in text.lower()
    assert "pad distractors" not in text.lower()
    assert "remediation required" not in text.lower()
    assert "alpha/beta stable" not in text.lower()
    assert "fable should adjudicate" not in text.lower()
    assert "queued for fable" not in text.lower()
    assert "witness-run-manifest-v1" in text
    assert "narrowest observed" in text.lower()
    assert "predicted control S12/S16" not in text


def test_readme_reproduction_exports_shared_scores_and_does_not_reduce_live_readiness_to_keys() -> None:
    text = (PKG / "README.md").read_text()
    assert "--shared-score" in text
    assert "test_mf2_mf5_analysis.py" in text
    assert "keys do not make the live path ready" in text.lower()
    for blocker in (
        "tested-model and judge adapters",
        "immutable provider evidence",
        "A6",
        "G4b",
        "human",
        "\u03baw",
    ):
        assert blocker.lower() in text.lower()
    assert "wiring a key runs the identical pipeline" not in text
    assert "everything downstream (scoring, audits, analysis, report) is unchanged" not in text


def test_live_report_keeps_simulated_matching_probe_auxiliary() -> None:
    manifest = {
        **_simulated_manifest(),
        "execution_type": "LIVE",
        "models": [{"name": "model-a", "execution_type": "LIVE"}],
    }
    qc = {
        "run_date": "20260709", "run_id": "p1-simulated-test",
        "models": ["model-a"], "canary_emitted": 0,
        "rec_counterfeit_draw_rate": 0.2,
        "acquiescence_index_by_model": {"model-a": 0.5},
        "judge_panel": {
            "inter_judge_kappa": 0.81, "worst_category_f1": 0.8,
            "worst_category": "counterfeit", "worst_f1_passes_0.75": True,
            "per_category_f1": {"gold": 0.9, "counterfeit": 0.8},
        },
    }
    summary = {
        "control_goldrate_by_modality": {
            "model-a": {"END": 0.7, "REC": 0.6, "GEN": 0.5, "ACT": 0.4},
        },
        "gate_b_distinguishable_sids": {"model-a": 2},
        "monitored_unmonitored": {"model-a": {"widens_unobserved": 0.01}},
        "primary_end_act": [{
            "model": "model-a", "holdout": False, "corrected_gap": 0.2,
            "ci90": [0.1, 0.3], "control_variance_share": 0.1,
            "control_variance_over_50pct": False, "estimator": "pooled DiD",
        }],
        "format_band_diagnostics": [{
            "model": "model-a", "contrast": "END-ACT", "high_minus_low": 0.01,
            "trend_ci90": [-0.02, 0.04], "switch_to_stratum_matched": False,
            "applied_estimator": "pooled DiD",
        }],
        "robustness": {
            "attempted": True,
            "models": {"model-a": {
                "status": "UNAVAILABLE", "logit_corrected_gap": None, "sign": None,
                "convergence": None, "sign_disagreement_with_primary": None,
                "message": "Rscript unavailable",
            }},
            "any_sign_disagreement": None,
        },
    }
    evidence = {
        "schema_version": "witness-analysis-audit-evidence-v1",
        "run_date": "20260709", "run_id": "p1-simulated-test",
        "execution_type": "LIVE",
        "leakage": {"gate_passed": True, "finding_count": 0, "sha256": "a" * 64},
        "matching": {
            "gate_passed": True, "construction_identity_mean": 1.0,
            "probe_identity_mean": 0.946, "probe_passing_fraction": 1.0,
            "probe_execution_type": "SIMULATED", "sha256": "b" * 64,
        },
        "shortcut": {
            "gate_passed": True, "n_cores": 30, "max_length_parity_ratio": 0.087,
            "metrics": {
                "longest_fractional": 0.2, "longest_conservative": 0.233,
                "overlap_fractional": 0.3, "overlap_conservative": 0.3,
            },
            "sha256": "c" * 64,
        },
    }
    text = make_report.render_report(
        run_date="20260709", manifest=manifest, qc=qc, summary=summary,
        stability={"model-a": {"across_skin_pearson_r": 0.433}},
        prediction={"model-a": {"spearman_rho_vs_corpus": 0.4}},
        surface=[{
            "model": "model-a", "sid": "S38", "contrast": "END-ACT",
            "corrected_gap": 0.2, "holdout": False,
        }],
        audit_evidence=evidence,
    )
    matching_row = next(line for line in text.splitlines() if "rendering matching" in line)
    assert "AUXILIARY PASS" in matching_row
    assert "SIMULATED PROBE" in matching_row
    assert "LIVE PASS" not in matching_row
    assert "All numerical gate outcomes in this section are **LIVE** evidence." not in text
    assert "auxiliary" in text.lower()
    # Real run-bound gates may still carry LIVE evidence when their own provenance permits it.
    assert "| (c) REC counterfeit draw ≥ 10% | **LIVE PASS**" in text
