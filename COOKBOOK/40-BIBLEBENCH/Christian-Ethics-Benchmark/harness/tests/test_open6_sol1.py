"""Offline contract tests for the OPEN6-SOL1 freeze/preflight layer."""

from __future__ import annotations

import json
import os
from copy import deepcopy
from decimal import Decimal
from pathlib import Path
import subprocess
import sys

import pytest


def _module():
    from walkworthy import open6_sol1

    return open6_sol1


def test_selects_the_complete_ordered_runnable_public_surface(benchmark_root):
    pilot = _module()
    items = pilot.select_public_items(benchmark_root)

    assert len(items) == 344
    assert len({item.id for item in items}) == 344
    assert all(item.runnable for item in items)
    assert [item.id for item in items] == sorted(item.id for item in items)
    assert pilot.ordered_item_hash(items) == (
        "6db7d83dd5e24cf689e0eaf1fe7f8a1a09b6f5e4c2229018b63e241b39238839"
    )


def test_freezes_exact_roster_prices_provider_ceilings_and_limits(benchmark_root):
    pilot = _module()
    manifest = pilot.build_manifest(benchmark_root)

    expected = [
        ("minimax/minimax-m3", "0.30", "1.20"),
        ("z-ai/glm-5.2", "0.903", "2.838"),
        ("deepseek/deepseek-v4-pro", "0.435", "0.87"),
        ("qwen/qwen3.5-397b-a17b", "0.385", "2.45"),
        ("google/gemma-4-31b-it", "0.12", "0.35"),
        ("meta-llama/llama-4-maverick", "0.20", "0.80"),
    ]
    models = manifest["openrouter"]["models"]
    assert [(m["slug"], m["input_per_m_usd"], m["output_per_m_usd"])
            for m in models] == expected
    for model in models:
        assert Decimal(model["provider_ceiling"]["prompt_per_m_usd"]) == (
            Decimal(model["input_per_m_usd"]) * Decimal("1.10")
        )
        assert Decimal(model["provider_ceiling"]["completion_per_m_usd"]) == (
            Decimal(model["output_per_m_usd"]) * Decimal("1.10")
        )

    assert manifest["openrouter"]["output_cap_tokens"] == 2048
    assert manifest["openrouter"]["nominal_calls"] == 5886
    assert manifest["openrouter"]["defect_replay_reserve_calls"] == 295
    assert manifest["openrouter"]["hard_call_cap"] == 6181
    assert manifest["openrouter"]["hard_nte_usd"] == "25.00"
    assert manifest["openrouter"]["substitution_allowed"] is False

    sol = manifest["sol_oauth"]
    assert sol["model"] == "gpt-5.6-sol"
    assert sol["reasoning_effort"] == "medium"
    assert sol["classifier_turns"] == 1722
    assert sol["judge_units"] == 5370
    assert sol["judge_batch_max_units"] == 24
    assert sol["judge_batches"] == 227
    assert sol["nominal_turns"] == 1949
    assert sol["defect_replay_reserve_turns"] == 98
    assert sol["hard_turn_cap"] == 2047
    assert sol["automatic_credit_purchase"] is False

    boundary = manifest["claims_boundary"]
    assert boundary["evidence_class"] == "descriptive_single_judge_mvp"
    assert boundary["o5_verdict_authorized"] is False
    assert boundary["g4_validation_authorized"] is False
    assert boundary["release_claim_authorized"] is False


def test_geometry_is_derived_from_item_structures_and_scoring_specs(benchmark_root):
    pilot = _module()
    items = pilot.select_public_items(benchmark_root)
    geometry = pilot.derive_geometry(items)

    assert geometry["item_count"] == 344
    assert geometry["model_count"] == 6
    assert geometry["item_model_records"] == 2064
    assert geometry["sut_content_calls_per_model"] == 949
    assert geometry["design05_allocation_calls_per_model"] == 32
    assert geometry["openrouter_nominal_calls"] == 5886
    assert geometry["classifier_turns_per_model"] == 287
    assert geometry["classifier_turns"] == 1722
    assert geometry["judge_units_per_model"] == 895
    assert geometry["judge_units"] == 5370
    assert geometry["category_cells_per_model"] == 1668
    assert geometry["category_cells"] == 10008
    assert geometry["same_design_judge_batches"] == 227

    by_design = {row["design"]: row for row in geometry["by_design"]}
    assert by_design["02-twomasters"]["classifier_turns_per_model"] == 178
    assert by_design["07-seventyseven"]["classifier_turns_per_model"] == 109
    assert by_design["06-crookedpath"]["category_cells_per_model"] == 217
    assert sum(row["item_count"] for row in geometry["by_design"]) == 344


def test_every_per_design_geometry_field_is_frozen_and_compensating_drift_stops(
        benchmark_root):
    pilot = _module()
    expected = {
        "01-goodsamaritan": {
            "item_count": 49, "scoring_unit": "item", "category_count": 2,
            "sut_content_calls_per_model": 49,
            "design05_allocation_calls_per_model": 0,
            "classifier_turns_per_model": 0, "judge_units_per_model": 49,
            "category_cells_per_model": 98, "same_design_judge_batches": 13,
        },
        "02-twomasters": {
            "item_count": 36, "scoring_unit": "per_turn", "category_count": 1,
            "sut_content_calls_per_model": 322,
            "design05_allocation_calls_per_model": 0,
            "classifier_turns_per_model": 178, "judge_units_per_model": 286,
            "category_cells_per_model": 286, "same_design_judge_batches": 72,
        },
        "03-quiettongue": {
            "item_count": 33, "scoring_unit": "per_admin", "category_count": 3,
            "sut_content_calls_per_model": 66,
            "design05_allocation_calls_per_model": 0,
            "classifier_turns_per_model": 0, "judge_units_per_model": 66,
            "category_cells_per_model": 198, "same_design_judge_batches": 17,
        },
        "04-innerweight": {
            "item_count": 33, "scoring_unit": "per_admin", "category_count": 3,
            "sut_content_calls_per_model": 60,
            "design05_allocation_calls_per_model": 0,
            "classifier_turns_per_model": 0, "judge_units_per_model": 60,
            "category_cells_per_model": 180, "same_design_judge_batches": 15,
        },
        "05-ordoamoris": {
            "item_count": 32, "scoring_unit": "item", "category_count": 1,
            "sut_content_calls_per_model": 32,
            "design05_allocation_calls_per_model": 32,
            "classifier_turns_per_model": 0, "judge_units_per_model": 32,
            "category_cells_per_model": 32, "same_design_judge_batches": 8,
        },
        "06-crookedpath": {
            "item_count": 31, "scoring_unit": "item", "category_count": 7,
            "sut_content_calls_per_model": 31,
            "design05_allocation_calls_per_model": 0,
            "classifier_turns_per_model": 0, "judge_units_per_model": 31,
            "category_cells_per_model": 217, "same_design_judge_batches": 8,
        },
        "07-seventyseven": {
            "item_count": 27, "scoring_unit": "per_turn", "category_count": 1,
            "sut_content_calls_per_model": 163,
            "design05_allocation_calls_per_model": 0,
            "classifier_turns_per_model": 109, "judge_units_per_model": 163,
            "category_cells_per_model": 163, "same_design_judge_batches": 41,
        },
        "08-vocationfork": {
            "item_count": 33, "scoring_unit": "per_admin", "category_count": 1,
            "sut_content_calls_per_model": 66,
            "design05_allocation_calls_per_model": 0,
            "classifier_turns_per_model": 0, "judge_units_per_model": 66,
            "category_cells_per_model": 66, "same_design_judge_batches": 17,
        },
        "09-doubleedge": {
            "item_count": 34, "scoring_unit": "per_seat", "category_count": 2,
            "sut_content_calls_per_model": 88,
            "design05_allocation_calls_per_model": 0,
            "classifier_turns_per_model": 0, "judge_units_per_model": 70,
            "category_cells_per_model": 140, "same_design_judge_batches": 18,
        },
        "10-strangergate": {
            "item_count": 36, "scoring_unit": "per_admin", "category_count": 4,
            "sut_content_calls_per_model": 72,
            "design05_allocation_calls_per_model": 0,
            "classifier_turns_per_model": 0, "judge_units_per_model": 72,
            "category_cells_per_model": 288, "same_design_judge_batches": 18,
        },
    }
    assert pilot.EXPECTED_GEOMETRY_BY_DESIGN == expected

    items = pilot.select_public_items(benchmark_root)
    geometry = pilot.derive_geometry(items)
    actual = {
        row["design"]: {key: value for key, value in row.items() if key != "design"}
        for row in geometry["by_design"]
    }
    assert actual == expected

    numeric_fields = [field for field in next(iter(expected.values()))
                      if field != "scoring_unit"]
    designs = list(expected)
    for design in designs:
        for field in numeric_fields:
            changed = deepcopy(geometry)
            rows = {row["design"]: row for row in changed["by_design"]}
            compensator = next(
                (other for other in designs
                 if other != design and rows[other][field] > 0),
                None,
            )
            if compensator is not None:
                rows[design][field] += 1
                rows[compensator][field] -= 1
            else:
                compensator = next(other for other in designs if other != design)
                rows[design][field] -= 1
                rows[compensator][field] += 1
            with pytest.raises(pilot.GeometryDriftError, match="per-design"):
                pilot._validate_authorized_geometry(items, changed)

        changed = deepcopy(geometry)
        rows = {row["design"]: row for row in changed["by_design"]}
        compensator = next(
            other for other in designs
            if expected[other]["scoring_unit"] != expected[design]["scoring_unit"]
        )
        rows[design]["scoring_unit"], rows[compensator]["scoring_unit"] = (
            rows[compensator]["scoring_unit"], rows[design]["scoring_unit"]
        )
        with pytest.raises(pilot.GeometryDriftError, match="per-design"):
            pilot._validate_authorized_geometry(items, changed)


def test_manifest_write_is_canonical_immutable_and_validates_existing_file(
        benchmark_root, tmp_path):
    pilot = _module()
    manifest = pilot.build_manifest(benchmark_root)
    path = tmp_path / "manifest.json"

    assert pilot.write_or_validate_manifest(path, manifest) == "written"
    first = path.read_bytes()
    assert first == pilot.canonical_json_bytes(manifest)
    assert pilot.write_or_validate_manifest(path, manifest) == "validated"
    assert path.read_bytes() == first

    changed = json.loads(first)
    changed["openrouter"]["hard_nte_usd"] = "25.01"
    path.write_bytes(pilot.canonical_json_bytes(changed))
    with pytest.raises(pilot.ManifestMismatchError, match="immutable manifest mismatch"):
        pilot.write_or_validate_manifest(path, manifest)


def test_preflight_cli_writes_manifest_without_credentials(benchmark_root, tmp_path):
    pilot = _module()
    path = tmp_path / "manifest.json"
    env = os.environ.copy()
    for name in ("OPENROUTER_API_KEY", "OPENAI_API_KEY", "ANTHROPIC_API_KEY"):
        env.pop(name, None)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "walkworthy.open6_sol1",
            "preflight",
            "--benchmark-root",
            str(benchmark_root),
            "--manifest",
            str(path),
        ],
        cwd=Path(pilot.__file__).resolve().parents[1],
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    summary = json.loads(result.stdout)
    assert summary == {
        "action": "written",
        "credential_access": False,
        "item_count": 344,
        "manifest": str(path.resolve()),
        "manifest_sha256": pilot.file_sha256(path),
        "phase": "preflight",
    }
    assert json.loads(path.read_text(encoding="utf-8"))["surface"]["split"] == "PUBLIC"
