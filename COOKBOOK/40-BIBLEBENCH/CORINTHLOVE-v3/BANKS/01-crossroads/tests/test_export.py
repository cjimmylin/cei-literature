from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator


BANK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BANK))

from export import export_megamatrix as exporter  # noqa: E402


def bank_fixture():
    episodes, sidecar = {}, {}
    for group in range(4):
        item_id = f"CROSSROADS-{group + 1:04d}"
        clauses = [f"C{group * 4 + offset}" for offset in range(1, 5)]
        episodes[item_id] = {
            "id": item_id, "split": "private",
            "template_family": f"family-{group}",
            "canary": f"10CB3-01-123e4567-e89b-42d3-a45{group}-42661417400{group}",
        }
        sidecar[item_id] = {
            "path_keys": {
                "p0": {clause: 1 for clause in clauses},
                "p1": {clause: -1 for clause in clauses},
            }
        }
    public_id = "CROSSROADS-9001"
    episodes[public_id] = {
        "id": public_id, "split": "public", "template_family": "public",
        "canary": "10CB3-01-123e4567-e89b-42d3-a456-426614174099",
    }
    sidecar[public_id] = {"path_keys": {"p0": {"C1": 1}}}
    return episodes, sidecar


def test_frozen_coverage_map_and_loadings_are_native_c1_to_c16():
    coverage = json.loads((BANK / "export/coverage_map.json").read_text())
    assert coverage["fixed_before_pilot"] is True
    assert coverage["declared_coverage"]["clauses"] == [f"C{i}" for i in range(1, 17)]
    assert coverage["episode_table_schema"] == exporter.SCHEMA
    with (BANK / "export/loadings_table.csv").open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 16
    assert {row["clause"] for row in rows} == {f"C{i}" for i in range(1, 17)}
    assert all(row["declared_loading"] == "1" for row in rows)


def test_manifest_and_rows_require_complete_model_item_clause_matrix():
    episodes, sidecar = bank_fixture()
    manifest = exporter.build_expected_manifest(
        episodes, sidecar, expected_models=["mock-a", "mock-b"]
    )
    assert manifest["expected_episode_count"] == 4
    assert manifest["expected_row_count"] == 32
    records = exporter.mock_records(manifest)
    rows = exporter.build_rows(records, episodes, manifest)
    assert len(rows) == 32
    assert all(set(row) == set(exporter.SCHEMA) for row in rows)
    assert {row["rung"] for row in rows} == {"choice"}
    assert {row["clause"] for row in rows} == {f"C{i}" for i in range(1, 17)}


def test_export_rejects_truncation_duplicate_and_unlabeled_mock_rows():
    episodes, sidecar = bank_fixture()
    manifest = exporter.build_expected_manifest(
        episodes, sidecar, expected_models=["mock-a"]
    )
    records = exporter.mock_records(manifest)
    with pytest.raises(ValueError, match="mock rows require"):
        bad = [dict(records[0], provenance="provided")]
        exporter.build_rows(bad, episodes, manifest)
    with pytest.raises(ValueError, match="missing"):
        exporter.build_rows(records[:-1], episodes, manifest)
    with pytest.raises(ValueError, match="duplicate"):
        exporter.build_rows(records + [records[0]], episodes, manifest)


def test_a3_profile_keeps_primary_choice_and_execution_vector_separate():
    aggregate = {
        "clause_scores": {
            f"C{i}": {"score": 0.5, "n_items": 10, "n_structures": 5,
                       "ci": {"lower": 0.2, "upper": 0.8}}
            for i in range(1, 17)
        },
        "execution_vector": {
            f"C{i}": {"score": 0.75, "n_items": 10, "n_structures": 5,
                       "ci": {"lower": 0.4, "upper": 0.9}}
            for i in range(1, 17)
        },
    }
    profile = exporter.build_a3_profile("model@version", aggregate)
    assert profile["method"] == "01-crossroads"
    assert set(profile["clause_scores"]) == {f"C{i}" for i in range(1, 17)}
    assert profile["method_summaries"]["execution_vector"]["C1"]["score"] == 0.75
    assert profile["clause_scores"]["C1"]["score"] == 0.5
    assert profile["megamatrix"] == {
        "loadings_table": "export/loadings_table.csv",
        "calibration_notes": "megamatrix/calibration_notes.md",
    }
    schema = json.loads((BANK / "export/profile.schema.json").read_text())
    Draft202012Validator(schema).validate(profile)
