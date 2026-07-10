"""Megamatrix schema, metric separation, and fail-loud completeness."""
import copy
import json
import os

import pytest
import yaml

import generator
from export import export_megamatrix


BANK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS = ("mock-model-A", "mock-model-B")


@pytest.fixture(scope="module")
def bank_data():
    episode_list, sidecar, _, _ = generator.generate(20260709)
    return {episode["id"]: episode for episode in episode_list}, sidecar


def _non_private_exclusions(episodes):
    return export_megamatrix.non_private_exclusions(episodes)


def _manifest(episodes, sidecar):
    return export_megamatrix.build_expected_manifest(
        episodes,
        sidecar,
        expected_models=MODELS,
        exclusions=_non_private_exclusions(episodes),
    )


def _complete_records(manifest):
    return [
        {
            "model_id": model_id,
            "item_id": item_id,
            "stage4_score": 3,
            "stage3_update_score": 0,
            "mechanical_flag": False,
            "judge_ids": [],
            "provenance": export_megamatrix.MOCK_LABEL,
        }
        for model_id in manifest["expected_models"]
        for item_id in manifest["expected_episode_ids"]
    ]


def test_episode_export_uses_only_stage4_primary_score(bank_data):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)
    rows = export_megamatrix.build_rows(
        _complete_records(manifest), episodes, sidecar, manifest
    )
    assert len(rows) == 1152
    assert set(rows[0]) == set(export_megamatrix.SCHEMA)
    assert rows[0]["score"] == 3
    assert rows[0]["rung"] == "stage_4"
    assert rows[0]["clause"] == "CHARITROC:CALIBRATED_CHARITY"
    assert rows[0]["mechanical_flag"] == 0
    assert rows[0]["judge_ids"] == "mechanical"


def test_export_rejects_unlabeled_mock_input(bank_data):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)
    records = _complete_records(manifest)
    records[0].pop("provenance")
    with pytest.raises(ValueError, match="harness validation, NOT a measurement"):
        export_megamatrix.build_rows(records, episodes, sidecar, manifest)


def test_manifest_pins_models_episodes_cells_and_exclusions(bank_data):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)

    assert manifest["expected_models"] == list(MODELS)
    assert manifest["manifest_version"] == "CHARITROC-export-manifest-v2"
    assert export_megamatrix.MANIFEST_VERSION == (
        "CHARITROC-export-manifest-v2"
    )
    assert manifest["method_id"] == "charitroc"
    assert len(export_megamatrix.SCHEMA) == 10
    assert manifest["bank_episode_count"] == 684
    assert manifest["expected_episode_count"] == 576
    assert manifest["excluded_episode_count"] == 108
    assert manifest["split_counts"] == {
        "private": 576, "calibration": 96, "public": 12,
    }
    assert manifest["exclusion_counts_by_split"] == {
        "calibration": 96, "public": 12,
    }
    assert manifest["expected_row_count"] == 1152
    assert len(manifest["expected_cells"]) == 288
    assert set(map(len, manifest["expected_cells"].values())) == {2}
    assert {cell.split("|")[0] for cell in manifest["expected_cells"]} == set(
        export_megamatrix.EXPECTED_FAMILIES
    )
    assert {cell.split("|")[1] for cell in manifest["expected_cells"]} == {
        "benign", "malicious"
    }
    assert {cell.split("|")[2] for cell in manifest["expected_cells"]} == {
        "strong", "weak", "absent", "adversarial"
    }
    assert {cell.split("|")[3] for cell in manifest["expected_cells"]} == {
        "0.2", "0.5", "0.8"
    }


def test_export_rejects_truncated_model_episode_matrix(bank_data):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)
    records = _complete_records(manifest)[:-1]
    with pytest.raises(ValueError, match="missing model/item rows"):
        export_megamatrix.build_rows(records, episodes, sidecar, manifest)


def test_export_rejects_missing_expected_model(bank_data):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)
    records = [
        record for record in _complete_records(manifest)
        if record["model_id"] != "mock-model-B"
    ]
    with pytest.raises(ValueError, match="model set mismatch"):
        export_megamatrix.build_rows(records, episodes, sidecar, manifest)


def test_export_rejects_unexpected_model(bank_data):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)
    records = _complete_records(manifest)
    records[0]["model_id"] = "mock-model-C"
    with pytest.raises(ValueError, match="model set mismatch"):
        export_megamatrix.build_rows(records, episodes, sidecar, manifest)


def test_export_rejects_duplicate_model_episode_row(bank_data):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)
    records = _complete_records(manifest)
    records.append(copy.deepcopy(records[0]))
    with pytest.raises(ValueError, match="duplicate model/item export row"):
        export_megamatrix.build_rows(records, episodes, sidecar, manifest)


@pytest.mark.parametrize(
    "bad_flag", [0, 1, None, "false", "true", [], {}]
)
def test_build_rows_requires_mechanical_flag_to_be_exact_bool(
        bank_data, bad_flag):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)
    records = _complete_records(manifest)
    records[0]["mechanical_flag"] = bad_flag
    with pytest.raises(ValueError, match="mechanical_flag.*exact bool"):
        export_megamatrix.build_rows(records, episodes, sidecar, manifest)


@pytest.mark.parametrize("bad_judge_ids", ["judge-A", {"judge-A": True}])
def test_build_rows_requires_judge_ids_list_or_tuple(
        bank_data, bad_judge_ids):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)
    records = _complete_records(manifest)
    records[0]["judge_ids"] = bad_judge_ids
    with pytest.raises(ValueError, match="judge_ids.*list or tuple"):
        export_megamatrix.build_rows(records, episodes, sidecar, manifest)


@pytest.mark.parametrize(
    "bad_judge_ids",
    [
        [""], ["   "], ["judge|other"], ["mechanical"],
        [" judge-A"], ["judge-A "],
    ],
)
def test_build_rows_rejects_noncanonical_judge_id_components(
        bank_data, bad_judge_ids):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)
    records = _complete_records(manifest)
    records[0].update({
        "mechanical_flag": True,
        "judge_ids": bad_judge_ids,
    })
    with pytest.raises(
            ValueError, match="judge_ids.*non-empty delimiter-free"):
        export_megamatrix.build_rows(records, episodes, sidecar, manifest)


@pytest.mark.parametrize(
    ("mechanical_flag", "judge_ids"),
    [(False, ["judge-A"]), (True, [])],
)
def test_build_rows_rejects_flag_judge_mismatch(
        bank_data, mechanical_flag, judge_ids):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)
    records = _complete_records(manifest)
    records[0].update({
        "mechanical_flag": mechanical_flag,
        "judge_ids": judge_ids,
    })
    with pytest.raises(ValueError, match="mechanical_flag.*judge_ids"):
        export_megamatrix.build_rows(records, episodes, sidecar, manifest)


def test_build_rows_serializes_flagged_judge_ids_and_unflagged_sentinel(
        bank_data):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)
    records = _complete_records(manifest)
    records[0].update({
        "mechanical_flag": True,
        "judge_ids": ("judge-A", "judge-B"),
    })
    rows = export_megamatrix.build_rows(
        records, episodes, sidecar, manifest
    )
    assert rows[0]["mechanical_flag"] == 1
    assert rows[0]["judge_ids"] == "judge-A|judge-B"
    assert rows[1]["mechanical_flag"] == 0
    assert rows[1]["judge_ids"] == "mechanical"


def test_mock_records_obey_flag_judge_relation(bank_data):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)
    records = export_megamatrix.mock_records(manifest)
    assert all(type(record["mechanical_flag"]) is bool for record in records)
    assert all(
        (record["mechanical_flag"] and record["judge_ids"])
        or (not record["mechanical_flag"] and record["judge_ids"] == [])
        for record in records
    )
    export_megamatrix.build_rows(records, episodes, sidecar, manifest)


@pytest.mark.parametrize("bad_score", [True, 1.0, 1.5, "1"])
def test_build_rows_rejects_noncanonical_stage4_score(
        bank_data, bad_score):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)
    records = _complete_records(manifest)
    records[0]["stage4_score"] = bad_score
    with pytest.raises(ValueError, match="stage4_score.*integer 0..4"):
        export_megamatrix.build_rows(records, episodes, sidecar, manifest)


@pytest.mark.parametrize("bad_score", [True, 1.0, 1.5, "1", None])
def test_json_export_rejects_non_integer_score_representation(
        bank_data, bad_score):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)
    rows = export_megamatrix.build_rows(
        _complete_records(manifest), episodes, sidecar, manifest
    )
    rows[0]["score"] = bad_score
    with pytest.raises(ValueError, match="JSON score.*integer 0..4"):
        export_megamatrix.validate_export_rows(
            rows, episodes, sidecar, manifest, row_format="json"
        )


@pytest.mark.parametrize("bad_score", ["01", "1.0", " 1", "5", 1])
def test_csv_export_rejects_noncanonical_digit_score(
        bank_data, bad_score):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)
    rows = export_megamatrix.build_rows(
        _complete_records(manifest), episodes, sidecar, manifest
    )
    csv_rows = [
        {
            **row,
            "score": str(row["score"]),
            "mechanical_flag": str(row["mechanical_flag"]),
        }
        for row in rows
    ]
    csv_rows[0]["score"] = bad_score
    with pytest.raises(ValueError, match="CSV score.*exact digit 0..4"):
        export_megamatrix.validate_export_rows(
            csv_rows, episodes, sidecar, manifest, row_format="csv"
        )


@pytest.mark.parametrize("bad_judge_ids", [None, "", "   ", []])
def test_export_rejects_blank_or_non_string_judge_ids(
        bank_data, bad_judge_ids):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)
    rows = export_megamatrix.build_rows(
        _complete_records(manifest), episodes, sidecar, manifest
    )
    rows[0]["judge_ids"] = bad_judge_ids
    with pytest.raises(ValueError, match="judge_ids.*non-empty string"):
        export_megamatrix.validate_export_rows(
            rows, episodes, sidecar, manifest, row_format="json"
        )


@pytest.mark.parametrize("bad_flag", ["0", "1", True, False, 0.0, 1.0])
def test_json_export_requires_exact_integer_mechanical_flag(
        bank_data, bad_flag):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)
    rows = export_megamatrix.build_rows(
        _complete_records(manifest), episodes, sidecar, manifest
    )
    rows[0]["mechanical_flag"] = bad_flag
    with pytest.raises(
            ValueError, match="JSON mechanical_flag.*integer 0 or 1"):
        export_megamatrix.validate_export_rows(
            rows, episodes, sidecar, manifest, row_format="json"
        )


@pytest.mark.parametrize("bad_flag", [0, 1, True, False, 0.0, 1.0, "00"])
def test_csv_export_requires_exact_string_mechanical_flag(
        bank_data, bad_flag):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)
    rows = export_megamatrix.build_rows(
        _complete_records(manifest), episodes, sidecar, manifest
    )
    csv_rows = [
        {
            **row,
            "score": str(row["score"]),
            "mechanical_flag": str(row["mechanical_flag"]),
        }
        for row in rows
    ]
    csv_rows[0]["mechanical_flag"] = bad_flag
    with pytest.raises(
            ValueError, match="CSV mechanical_flag.*'0' or '1'"):
        export_megamatrix.validate_export_rows(
            csv_rows, episodes, sidecar, manifest, row_format="csv"
        )


@pytest.mark.parametrize(
    ("flag", "judge_ids"),
    [
        (0, "judge-A"),
        (1, "mechanical"),
        (1, ""),
        (1, "   "),
        (1, "|"),
        (1, "judge-A|"),
        (1, "|judge-A"),
        (1, "judge-A||judge-B"),
        (1, "judge-A| |judge-B"),
        (1, " judge-A"),
        (1, "judge-A "),
    ],
)
@pytest.mark.parametrize("row_format", ["json", "csv"])
def test_persisted_export_rejects_flag_judge_mismatch_and_bad_segments(
        bank_data, row_format, flag, judge_ids):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)
    rows = export_megamatrix.build_rows(
        _complete_records(manifest), episodes, sidecar, manifest
    )
    if row_format == "csv":
        rows = [
            {
                **row,
                "score": str(row["score"]),
                "mechanical_flag": str(row["mechanical_flag"]),
            }
            for row in rows
        ]
        flag = str(flag)
    rows[0].update({"mechanical_flag": flag, "judge_ids": judge_ids})
    with pytest.raises(ValueError, match="judge_ids|mechanical_flag"):
        export_megamatrix.validate_export_rows(
            rows, episodes, sidecar, manifest, row_format=row_format
        )


@pytest.mark.parametrize("row_format", ["json", "csv"])
def test_persisted_export_accepts_only_canonical_flag_judge_pairs(
        bank_data, row_format):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)
    records = _complete_records(manifest)
    records[0].update({
        "mechanical_flag": True,
        "judge_ids": ["judge-A", "judge-B"],
    })
    rows = export_megamatrix.build_rows(
        records, episodes, sidecar, manifest
    )
    if row_format == "csv":
        rows = [
            {
                **row,
                "score": str(row["score"]),
                "mechanical_flag": str(row["mechanical_flag"]),
            }
            for row in rows
        ]
    export_megamatrix.validate_export_rows(
        rows, episodes, sidecar, manifest, row_format=row_format
    )


def test_manifest_rejects_missing_declared_cell(bank_data):
    episodes, sidecar = bank_data
    broken_episodes = dict(episodes)
    broken_sidecar = dict(sidecar)
    target_ids = [
        item_id for item_id, episode in episodes.items()
        if episode["split"] == "private"
        and episode["template_family"] == export_megamatrix.EXPECTED_FAMILIES[0]
        and sidecar[item_id]["true_type"] == "benign"
        and sidecar[item_id]["cue_variant"] == "strong"
        and sidecar[item_id]["base_rate_benign"] == 0.2
    ]
    assert len(target_ids) == 2
    for item_id in target_ids:
        broken_episodes.pop(item_id)
        broken_sidecar.pop(item_id)
    with pytest.raises(ValueError, match="declared cell coverage"):
        export_megamatrix.build_expected_manifest(
            broken_episodes,
            broken_sidecar,
            expected_models=MODELS,
            exclusions=_non_private_exclusions(broken_episodes),
        )


def test_manifest_rejects_inexact_exclusion_accounting(bank_data):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)
    broken = copy.deepcopy(manifest)
    broken["excluded_episode_count"] += 1
    with pytest.raises(ValueError, match="exclusion accounting"):
        export_megamatrix.validate_expected_manifest(
            broken, episodes, sidecar
        )


def test_export_rejects_row_for_explicitly_excluded_episode(bank_data):
    episodes, sidecar = bank_data
    manifest = _manifest(episodes, sidecar)
    records = _complete_records(manifest)
    excluded_id = manifest["exclusions"][0]["item_id"]
    records[0]["item_id"] = excluded_id
    with pytest.raises(ValueError, match="unexpected model/item rows"):
        export_megamatrix.build_rows(records, episodes, sidecar, manifest)


@pytest.mark.parametrize("models", [[], ["mock-model-A", "mock-model-A"]])
def test_manifest_requires_explicit_unique_model_set(bank_data, models):
    episodes, sidecar = bank_data
    with pytest.raises(ValueError, match="expected_models"):
        export_megamatrix.build_expected_manifest(
            episodes,
            sidecar,
            expected_models=models,
            exclusions=_non_private_exclusions(episodes),
        )


def test_manifest_refuses_pilot_slice_as_complete_megamatrix(bank_data):
    episodes, sidecar = bank_data
    private_ids = [
        item_id for item_id, episode in episodes.items()
        if episode["split"] == "private"
    ][:96]
    sliced_ids = {
        *private_ids,
        *(item_id for item_id, episode in episodes.items()
          if episode["split"] != "private"),
    }
    sliced_episodes = {
        item_id: episodes[item_id] for item_id in sliced_ids
    }
    sliced_sidecar = {item_id: sidecar[item_id] for item_id in sliced_ids}
    with pytest.raises(
            ValueError, match="split inventory|576|declared cell coverage"):
        export_megamatrix.build_expected_manifest(
            sliced_episodes,
            sliced_sidecar,
            expected_models=MODELS,
            exclusions=_non_private_exclusions(sliced_episodes),
        )


def test_manifest_requires_every_non_private_episode_as_explicit_exclusion(
        bank_data):
    episodes, sidecar = bank_data
    exclusions = _non_private_exclusions(episodes)
    exclusions.pop(next(
        item_id for item_id, episode in episodes.items()
        if episode["split"] == "calibration"
    ))
    with pytest.raises(ValueError, match="non-private|exclusion"):
        export_megamatrix.build_expected_manifest(
            episodes, sidecar, expected_models=MODELS,
            exclusions=exclusions,
        )


def _write_loader_fixture(root, episodes, sidecar):
    (root / "episodes").mkdir()
    by_split = {
        split: [
            episode for episode in episodes.values()
            if episode["split"] == split
        ]
        for split in ("private", "calibration", "public")
    }
    for split, rel in (
        ("private", "private_bank.yaml"),
        ("calibration", "calibration_bank.yaml"),
    ):
        (root / "episodes" / rel).write_text(
            yaml.safe_dump(by_split[split], sort_keys=False), encoding="utf-8"
        )
    (root / "seeds_public.yaml").write_text(
        yaml.safe_dump(by_split["public"], sort_keys=False), encoding="utf-8"
    )
    (root / "sidecar").mkdir()
    (root / "sidecar" / "ground_truth.json").write_text(
        json.dumps(sidecar), encoding="utf-8"
    )


def test_loader_reads_and_validates_all_three_splits(tmp_path, bank_data):
    episodes, sidecar = bank_data
    _write_loader_fixture(tmp_path, episodes, sidecar)
    loaded, loaded_sidecar = export_megamatrix.load_bank(os.fspath(tmp_path))
    assert loaded == episodes
    assert loaded_sidecar == sidecar


def test_loader_fails_loud_when_calibration_file_is_missing(
        tmp_path, bank_data):
    episodes, sidecar = bank_data
    _write_loader_fixture(tmp_path, episodes, sidecar)
    (tmp_path / "episodes" / "calibration_bank.yaml").unlink()
    with pytest.raises((FileNotFoundError, ValueError), match="calibration"):
        export_megamatrix.load_bank(os.fspath(tmp_path))


def test_loader_fails_loud_when_one_calibration_row_is_missing(
        tmp_path, bank_data):
    episodes, sidecar = bank_data
    _write_loader_fixture(tmp_path, episodes, sidecar)
    path = tmp_path / "episodes" / "calibration_bank.yaml"
    rows = yaml.safe_load(path.read_text(encoding="utf-8"))
    path.write_text(yaml.safe_dump(rows[:-1], sort_keys=False), encoding="utf-8")
    with pytest.raises(ValueError, match="split inventory|calibration"):
        export_megamatrix.load_bank(os.fspath(tmp_path))


def test_coverage_map_is_frozen_family_code_crosswalk_only():
    path = os.path.join(BANK, "export", "coverage_map.json")
    with open(path, encoding="utf-8") as handle:
        coverage = json.load(handle)
    assert coverage["fixed_before_pilot"] is True
    assert coverage["version"] == "v1"
    assert coverage["declared_coverage"]["clauses"] == [
        "CHARITROC:CALIBRATED_CHARITY"
    ]
    assert coverage["declared_coverage"]["mapping_status"] == "crosswalk-mapped only"
    assert coverage["episode_table_schema"] == export_megamatrix.SCHEMA
