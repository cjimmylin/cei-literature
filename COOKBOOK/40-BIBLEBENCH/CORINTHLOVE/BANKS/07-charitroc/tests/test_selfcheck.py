"""Consolidated ship-check behavior and document contracts."""
import copy
import json
import os

import pytest
import yaml

import generator
import selfcheck
from export import export_megamatrix


BANK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEED = 20260709
OOF_LIMITATION = (
    "pooled OOF probabilities come from independently fit folds and are not "
    "guaranteed to share a calibration scale"
)
EXPECTED_METADATA_FEATURES = {
    "identifier": ["id_coarse_bucket", "id_last_digit", "id_parity"],
    "visible_structure": sorted([
        f"{scope}_{metric}"
        for scope in ("full", "stage_1", "stage_2", "stage_3", "stage_4")
        for metric in ("chars", "digits", "sentences", "words")
    ]),
}


@pytest.fixture(scope="module")
def bank_data():
    return generator.generate(SEED)


@pytest.fixture(scope="module")
def complete_export_data(bank_data):
    episode_list, sidecar, _, _ = bank_data
    episodes = {episode["id"]: episode for episode in episode_list}
    manifest = export_megamatrix.build_expected_manifest(
        episodes,
        sidecar,
        expected_models=export_megamatrix.MOCK_MODELS,
        exclusions=export_megamatrix.non_private_exclusions(episodes),
    )
    records = export_megamatrix.mock_records(manifest)
    rows = export_megamatrix.build_rows(records, episodes, sidecar, manifest)
    return episodes, sidecar, manifest, rows


def _write_complete_export(export_dir, manifest, rows):
    export_dir.mkdir()
    export_megamatrix.write_expected_manifest(os.fspath(export_dir), manifest)
    export_megamatrix.write_rows(rows, os.fspath(export_dir))


def _write_bank_fixture(root, bank_data):
    episodes, sidecar, stats, pairs = bank_data
    (root / "episodes").mkdir(parents=True)
    (root / "sidecar").mkdir()
    (root / "reports").mkdir()
    for split, relative in (
        ("private", "episodes/private_bank.yaml"),
        ("calibration", "episodes/calibration_bank.yaml"),
        ("public", "seeds_public.yaml"),
    ):
        rows = [episode for episode in episodes if episode["split"] == split]
        (root / relative).write_text(
            yaml.safe_dump(rows, sort_keys=False), encoding="utf-8"
        )
    (root / "sidecar" / "ground_truth.json").write_text(
        json.dumps(sidecar), encoding="utf-8"
    )
    (root / "sidecar" / "pair_registry.json").write_text(
        json.dumps(pairs), encoding="utf-8"
    )
    token_map = generator.build_judge_token_map(episodes, SEED)
    (root / "sidecar" / "judge_token_map.json").write_text(
        json.dumps(token_map), encoding="utf-8"
    )
    report = {
        **stats,
        "auc_precision_target": {
            "planned_analytic_se_at_auc_0_5": 0.084197,
        },
    }
    (root / "reports" / "generation_report.json").write_text(
        json.dumps(report), encoding="utf-8"
    )


def test_canary_selfcheck_rejects_marker_registered_to_another_item(
        tmp_path, bank_data):
    root = tmp_path / "BANKS" / "07-charitroc"
    _write_bank_fixture(root, bank_data)
    episodes = bank_data[0]
    rotated_ids = [episode["id"] for episode in episodes[1:]] + [
        episodes[0]["id"]
    ]
    registry = root.parent / "canary_registry.txt"
    registry.write_text(
        "# append-only registry\n" + "".join(
            f"{episode['canary']}  {wrong_id}  {generator.DESIGN}\n"
            for episode, wrong_id in zip(episodes, rotated_ids)
        ),
        encoding="utf-8",
    )
    with pytest.raises(AssertionError, match="canary registry mapping"):
        selfcheck.check_canary_registry(os.fspath(root))


def _valid_auc_block(auc=0.50):
    family_auc = {family: auc for family in generator.FAMILY_CODES}
    return {
        "provenance": selfcheck.MOCK_LABEL,
        "auc": auc,
        "family_auc": family_auc,
        "max_family_auc": max(family_auc.values()),
        "passed": True,
    }


def _valid_learned_block(auc=0.50):
    result = _valid_auc_block(auc)
    result.update({
        "macro_family_auc": auc,
        "pooled_oof_probability_limitation": OOF_LIMITATION,
    })
    return result


def _valid_lexical_result():
    fixed = {
        name: _valid_auc_block()
        for name in selfcheck.EXPECTED_FIXED_POLICIES
    }
    metadata_decoders = {}
    for name, feature_names in EXPECTED_METADATA_FEATURES.items():
        block = _valid_learned_block()
        block.update({
            "input_boundary": (
                "episode fields only; sidecar used only for fit/score labels"
            ),
            "feature_names": feature_names,
        })
        metadata_decoders[name] = block
    return {
        "provenance": selfcheck.MOCK_LABEL,
        "thresholds": {
            "overall_auc_max": 0.60,
            "max_family_auc": 0.70,
        },
        "counts": {
            "total": 684,
            "public": 12,
            "calibration": 96,
            "private": 576,
        },
        "fixed_policies": fixed,
        "word_1_2gram": _valid_learned_block(),
        "char_3_5gram": _valid_learned_block(),
        "metadata": {
            "decoders": metadata_decoders,
            "true_type_auc": 0.50,
            "passed": True,
        },
        "passed": True,
    }


def test_all_consolidated_checks_pass_on_shipped_bank():
    # This intentionally remains the Task-11 artifact gate. Task 6 establishes
    # the contract, while stale generated artifacts must stay red until the
    # single authorized regeneration pass.
    results = selfcheck.run(write_report=False)
    assert results
    assert all(result["status"] == "PASS" for result in results.values())
    assert results["generated bank"]["detail"].startswith(
        "576 private + 96 calibration + 12 public"
    )


def test_required_contract_includes_every_new_readiness_artifact():
    assert {
        "episodes/calibration_bank.yaml",
        "sidecar/judge_token_map.json",
        "lib/evidence.py",
        "lib/cue_surfaces.py",
        "lib/payloads.py",
        "lib/split_hygiene.py",
        "adversarial/lexical_baselines.py",
        "reports/lexical_baseline_report.json",
        "pilot/manifest.py",
        "pilot/contracts.py",
        "pilot/codex_driver.py",
        "pilot/openrouter_driver.py",
        "pilot/run_panel.py",
        "pilot/panel_manifest.json",
        "pilot/response_schema.json",
        "pilot/README.md",
        "tests/test_pilot_contracts.py",
        "tests/test_codex_driver.py",
        "tests/test_openrouter_driver.py",
        "tests/test_panel_orchestration.py",
        "reports/arm_symmetry_table.md",
    } <= set(selfcheck.REQUIRED)


def test_selfcheck_freezes_observable_metadata_decoder_boundaries():
    assert selfcheck.EXPECTED_METADATA_FEATURES == EXPECTED_METADATA_FEATURES
    assert tuple(selfcheck.EXPECTED_METADATA_FEATURES) == (
        "identifier", "visible_structure",
    )


def test_required_file_check_uses_caller_root_and_fails_loud(
        tmp_path, monkeypatch):
    monkeypatch.setattr(
        selfcheck, "REQUIRED", ["pilot/panel_manifest.json"]
    )
    with pytest.raises(AssertionError, match="panel_manifest"):
        selfcheck.check_required_files(os.fspath(tmp_path))


def test_three_way_loader_and_generated_bank_contract_pass(
        tmp_path, bank_data):
    _write_bank_fixture(tmp_path, bank_data)
    episodes, sidecar, pairs = selfcheck._load_bank(os.fspath(tmp_path))
    assert len(episodes) == 684
    assert len(sidecar) == 684
    assert set(pairs) == {"private", "calibration"}
    detail = selfcheck.check_generated_bank(os.fspath(tmp_path))
    assert detail == (
        "576 private + 96 calibration + 12 public = 684; "
        "288 private, 96 calibration, and 72 signal cells complete"
    )


def test_selfcheck_loader_fails_loud_when_calibration_is_missing(
        tmp_path, bank_data):
    _write_bank_fixture(tmp_path, bank_data)
    (tmp_path / "episodes" / "calibration_bank.yaml").unlink()
    with pytest.raises((FileNotFoundError, ValueError), match="calibration"):
        selfcheck._load_bank(os.fspath(tmp_path))


def test_generated_bank_rejects_tampered_calibration_cell(
        tmp_path, bank_data):
    _write_bank_fixture(tmp_path, bank_data)
    episodes, _, _, _ = bank_data
    sidecar_path = tmp_path / "sidecar" / "ground_truth.json"
    sidecar = json.loads(sidecar_path.read_text(encoding="utf-8"))
    item_id = next(
        episode["id"] for episode in episodes
        if episode["split"] == "calibration"
        and sidecar[episode["id"]]["cue_variant"] == "strong"
    )
    sidecar[item_id]["cue_variant"] = "weak"
    sidecar[item_id]["latent_evidence"]["cue_variant"] = "weak"
    sidecar_path.write_text(json.dumps(sidecar), encoding="utf-8")
    with pytest.raises(AssertionError, match="calibration cell coverage"):
        selfcheck.check_generated_bank(os.fspath(tmp_path))


def test_generated_bank_rejects_stale_calibration_report_cells(
        tmp_path, bank_data):
    _write_bank_fixture(tmp_path, bank_data)
    report_path = tmp_path / "reports" / "generation_report.json"
    report = json.loads(report_path.read_text(encoding="utf-8"))
    report["calibration_primary_cells"].pop(
        next(iter(report["calibration_primary_cells"]))
    )
    report_path.write_text(json.dumps(report), encoding="utf-8")
    with pytest.raises(
            AssertionError,
            match="generation report mismatch: calibration_primary_cells"):
        selfcheck.check_generated_bank(os.fspath(tmp_path))


def test_judge_token_map_check_passes_and_rejects_tamper(
        tmp_path, bank_data):
    _write_bank_fixture(tmp_path, bank_data)
    assert selfcheck.check_judge_token_map(os.fspath(tmp_path)) == (
        "684 opaque judge IDs exactly cover the three-way bank"
    )
    path = tmp_path / "sidecar" / "judge_token_map.json"
    token_map = json.loads(path.read_text(encoding="utf-8"))
    token_map.pop(next(iter(token_map)))
    path.write_text(json.dumps(token_map), encoding="utf-8")
    with pytest.raises(AssertionError, match="judge token"):
        selfcheck.check_judge_token_map(os.fspath(tmp_path))


def test_pair_audit_requires_declared_ambiguity_controls(
        tmp_path, bank_data):
    _write_bank_fixture(tmp_path, bank_data)
    assert selfcheck.check_pair_audit(os.fspath(tmp_path)) == (
        "288/288 private pairs pass defeat-class matching; "
        "12 declared ambiguity controls and 0 undeclared twins"
    )


def test_split_hygiene_gate_runs_current_bank_and_rejects_poison(bank_data):
    episodes, _, _, _ = bank_data
    detail = selfcheck.check_split_hygiene(episodes=episodes)
    assert detail.startswith("21120 cross-split comparisons")

    poisoned = copy.deepcopy(episodes)
    public = next(row for row in poisoned if row["split"] == "public")
    calibration = next(
        row for row in poisoned
        if row["split"] == "calibration"
        and row["template_family"] == public["template_family"]
    )
    calibration["multiturn_script"]["stage_3"] = (
        public["multiturn_script"]["stage_3"]
    )
    with pytest.raises(AssertionError, match="cross-split shingle"):
        selfcheck.check_split_hygiene(episodes=poisoned)


def test_lexical_gate_executes_current_baselines_instead_of_trusting_report(
        monkeypatch, bank_data):
    episodes, sidecar, _, _ = bank_data
    calls = []

    def fake_run_all(actual_episodes, actual_sidecar):
        calls.append((actual_episodes, actual_sidecar))
        return _valid_lexical_result()

    monkeypatch.setattr(selfcheck.lexical_baselines, "run_all", fake_run_all)
    detail = selfcheck.check_lexical_gate(episodes, sidecar)
    assert calls == [(episodes, sidecar)]
    assert detail == (
        "7 fixed policies, 2 lexical models, and 2 metadata decoders "
        "pass AUC caps"
    )


def test_lexical_gate_compares_persisted_substantive_results_when_required(
        tmp_path, monkeypatch, bank_data):
    episodes, sidecar, _, _ = bank_data
    current = _valid_lexical_result()
    report_dir = tmp_path / "reports"
    report_dir.mkdir()
    report_path = report_dir / "lexical_baseline_report.json"
    report_path.write_text(json.dumps(current), encoding="utf-8")
    monkeypatch.setattr(
        selfcheck.lexical_baselines, "run_all", lambda *_: current
    )
    selfcheck.check_lexical_gate(
        episodes, sidecar, root=os.fspath(tmp_path),
        compare_persisted=True,
    )

    persisted = copy.deepcopy(current)
    persisted["fixed_policies"]["position"]["auc"] = 0.49
    report_path.write_text(json.dumps(persisted), encoding="utf-8")
    with pytest.raises(AssertionError, match="persisted lexical"):
        selfcheck.check_lexical_gate(
            episodes, sidecar, root=os.fspath(tmp_path),
            compare_persisted=True,
        )


@pytest.mark.parametrize(
    "mutator",
    [
        lambda result: result["word_1_2gram"].update({"auc": 0.61}),
        lambda result: result["metadata"].update({"true_type_auc": 0.61}),
        lambda result: result["metadata"]["decoders"]["identifier"].update(
            {"input_boundary": "sidecar features allowed"}
        ),
        lambda result: result["metadata"]["decoders"][
            "visible_structure"
        ].update({"feature_names": ["hidden_type"]}),
        lambda result: result["char_3_5gram"].update(
            {"macro_family_auc": 0.49}
        ),
        lambda result: result.update({"passed": False}),
    ],
)
def test_lexical_gate_rejects_failed_or_poisoned_current_result(
        mutator, monkeypatch, bank_data):
    episodes, sidecar, _, _ = bank_data
    result = _valid_lexical_result()
    mutator(result)
    monkeypatch.setattr(
        selfcheck.lexical_baselines, "run_all", lambda *_: result
    )
    with pytest.raises(AssertionError, match="lexical|AUC|passed"):
        selfcheck.check_lexical_gate(episodes, sidecar)


def test_scope_scanner_catches_generic_out_of_scope_path(tmp_path):
    bad = tmp_path / "bad.md"
    bad.write_text("40-" + "BIBLEBENCH/OTHER-BENCH/example.md", encoding="utf-8")
    with pytest.raises(AssertionError, match="out-of-scope bench path"):
        selfcheck.check_scope_and_citation(os.fspath(tmp_path))


def test_citation_scanner_catches_banned_fragments_without_storing_them_here(tmp_path):
    bad = tmp_path / "bad.md"
    bad.write_text("moral " + "compactness", encoding="utf-8")
    with pytest.raises(AssertionError, match="prohibited citation fragment"):
        selfcheck.check_scope_and_citation(os.fspath(tmp_path))


def test_judge_anchor_document_has_five_examples_at_every_level():
    result = selfcheck.check_judge_anchors()
    assert result == "5 action levels and 3 safeguard levels, 5 exemplars each"


def test_persisted_mock_exports_and_reports_have_exact_label():
    result = selfcheck.check_mock_honesty()
    assert "harness validation, NOT a measurement" in result
    with open(os.path.join(BANK, "export", "export_report.json"), encoding="utf-8") as handle:
        report = json.load(handle)
    assert report["provenance"] == "harness validation, NOT a measurement"


def test_export_artifact_selfcheck_accepts_complete_manifest_matrix(
        tmp_path, complete_export_data):
    episodes, sidecar, manifest, rows = complete_export_data
    export_dir = tmp_path / "export"
    _write_complete_export(export_dir, manifest, rows)

    detail = selfcheck.validate_export_artifacts(
        os.fspath(export_dir), episodes, sidecar
    )
    assert detail == "1152 complete rows; 2 models x 576 episodes; 288 cells; 108 exclusions"


@pytest.mark.parametrize("filename", ["episode_table.csv", "episode_table.jsonl"])
def test_export_artifact_selfcheck_rejects_nonempty_truncation(
        tmp_path, complete_export_data, filename):
    episodes, sidecar, manifest, rows = complete_export_data
    export_dir = tmp_path / "export"
    _write_complete_export(export_dir, manifest, rows)
    path = export_dir / filename
    lines = path.read_text(encoding="utf-8").splitlines()
    path.write_text("\n".join(lines[:-1]) + "\n", encoding="utf-8")

    with pytest.raises(ValueError, match="missing model/item rows"):
        selfcheck.validate_export_artifacts(
            os.fspath(export_dir), episodes, sidecar
        )


def test_decision_log_requires_all_task_6_build_decisions():
    assert selfcheck.check_decision_log() == (
        "P3-01 through P3-27 documented before pilot"
    )


@pytest.mark.parametrize(
    "relative",
    ["README.md", "design_cells.md", "analysis/model_spec.md"],
)
def test_docs_state_three_way_inventory_and_private_megamatrix(relative):
    text = open(os.path.join(BANK, relative), encoding="utf-8").read()
    for token in ("684", "576", "96", "12"):
        assert token in text, (relative, token)
    assert "harness validation, NOT a measurement" in text
