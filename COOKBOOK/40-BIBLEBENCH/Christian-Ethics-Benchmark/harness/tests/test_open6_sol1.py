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

    authorization = manifest["authorization"]
    assert authorization["preflight_stage"]["credential_access"] is False
    assert authorization["live_execution"]["authorized"] is True
    assert authorization["live_execution"]["credential_access_at_call_time"] is True
    assert authorization["live_execution"]["unattended"] is True
    assert authorization["live_execution"]["soft_checkpoint_usd"] == "15.00"
    assert authorization["live_execution"]["projection_continue_ceiling_usd"] == "23.00"
    assert authorization["live_execution"]["hard_nte_usd"] == "25.00"
    assert authorization["owner_memos"] == [
        "00-PORTFOLIO/20260714-jimmy-open6-sol1-authorization.md",
        "00-PORTFOLIO/20260714-jimmy-open6-sol1-full-execution-authorization.md",
        "00-PORTFOLIO/20260714-jimmy-open6-sol1-resume-authorization.md",
        "00-PORTFOLIO/20260714-jimmy-open6-sol1-unattended-execution-order.md",
    ]


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


def test_manifest_freezes_normalized_items_rubrics_sources_and_sol_runtime(
        benchmark_root):
    pilot = _module()
    manifest = pilot.build_manifest(benchmark_root)
    frozen = manifest["evaluation_contract_freeze"]

    items = frozen["normalized_public_items"]
    assert items["normalization_version"] == "item-dataclass-canonical-v1"
    assert items["count"] == 344
    assert len(items["payloads"]) == 344
    assert items["sha256"] == (
        "a221a4988ed9d6483b4d41ddba7b7b0eda074a482a2edc13e14f5557d4031335"
    )
    assert {"variables", "administrations", "key", "extras"} <= set(
        items["payloads"][0]
    )
    assert items["payloads"][0]["source_file"].startswith("DESIGNS/")

    rubrics = frozen["rubrics"]
    assert rubrics["contract_version"] == "all-design-rubrics-canonical-v1"
    assert len(rubrics["payloads"]) == 10
    assert rubrics["sha256"] == (
        "abae04e935bc4bf689538a73cd087f9c7cd0c707bdc98e6ea6e07bf5e401211c"
    )

    assert frozen["source_files"] == {
        "hash_algorithm": "sha256_raw_bytes",
        "files": {
            "harness/walkworthy/executors.py": (
                "7405e70e7d7eff489b2b02eaf484823e16c41402bcd077da272ed61184e0a87b"
            ),
            "harness/walkworthy/judges.py": (
                "ce8a1d8f4b82ccc9dfa7bc64887b063fabee1e4ba029d44fe1eab4b31f213392"
            ),
            "harness/walkworthy/loader.py": (
                "07e7b0d871f9ea745b016189c661a395c7965759bbfd95b569911b28caa6064f"
            ),
            "harness/walkworthy/parsers.py": (
                "a936432733520231d9cc2b1b78690c93157494c8f58fa56dc5d85df07f9081ff"
            ),
            "harness/walkworthy/rubrics.py": (
                "603e1c7777060035f17f1e8cdc071f6db6828b8f4a712806017d7e3d7d2eb486"
            ),
            "harness/walkworthy/run.py": (
                "6189b859970918c3d392af9af86d72a116bfe994e836dcb6252f50a8857e6e14"
            ),
        },
    }

    runtime = frozen["sol_runtime"]
    assert runtime["runtime_reuse_required"] is True
    assert runtime["classifier"]["prompt"]["version"] == (
        "open6-sol1-classifier-prompt-v1"
    )
    assert runtime["classifier"]["prompt"]["sha256"] == (
        "fda002fe01748c7af574bd86b96352f5d734af72148a108a220acb62c2c92cbb"
    )
    assert runtime["classifier"]["schema"]["version"] == (
        "open6-sol1-classifier-schema-v1"
    )
    assert runtime["classifier"]["schema"]["sha256"] == (
        "547e6ce88c3714e4a4a4b4ea84e192fbb886182719b435c6abf52cf6a82d9ca5"
    )
    assert runtime["judge"]["prompt"]["version"] == "open6-sol1-judge-prompt-v1"
    assert runtime["judge"]["prompt"]["sha256"] == (
        "325998b712e7d30648b493d52e3072c7d8c59974c52eb07e0903181edbd5ae8b"
    )
    assert runtime["judge"]["schema"]["version"] == "open6-sol1-judge-schema-v1"
    assert runtime["judge"]["schema"]["sha256"] == (
        "0b5a6a451b3d5a2be83a1375c052744d02fa759632f844f5ab689f65963b5c58"
    )
    assert runtime["combined_sha256"] == (
        "c11b48c4b95459b677bbc1267967e8e497f7396354091dfe434057b23ef61a5d"
    )


def test_item_text_and_key_mutations_change_hash_and_fail_closed(benchmark_root):
    pilot = _module()
    items = pilot.select_public_items(benchmark_root)
    payloads = pilot.canonical_item_payloads(items)
    rubrics = pilot.canonical_rubric_payloads()
    sources = pilot.contract_source_hashes(benchmark_root)
    runtime = pilot.sol_runtime_contract()

    text_changed = deepcopy(payloads)
    text_changed[0]["administrations"][0]["turns"][0]["text"] += " mutation"
    assert pilot.canonical_payload_hash(text_changed) != pilot.EXPECTED_ITEM_PAYLOAD_SHA256
    with pytest.raises(pilot.ContractDriftError, match="normalized item payload"):
        pilot._validate_evaluation_contract(text_changed, rubrics, sources, runtime)

    key_changed = deepcopy(payloads)
    key_changed[0]["key"]["__mutation"] = True
    assert pilot.canonical_payload_hash(key_changed) != pilot.EXPECTED_ITEM_PAYLOAD_SHA256
    with pytest.raises(pilot.ContractDriftError, match="normalized item payload"):
        pilot._validate_evaluation_contract(key_changed, rubrics, sources, runtime)


def test_rubric_prompt_schema_and_source_mutations_change_hash_and_fail_closed(
        benchmark_root):
    pilot = _module()
    items = pilot.canonical_item_payloads(pilot.select_public_items(benchmark_root))
    rubrics = pilot.canonical_rubric_payloads()
    sources = pilot.contract_source_hashes(benchmark_root)
    runtime = pilot.sol_runtime_contract()

    rubric_changed = deepcopy(rubrics)
    rubric_changed[0]["categories"][0]["desc"] += " mutation"
    assert pilot.canonical_payload_hash(rubric_changed) != pilot.EXPECTED_RUBRIC_SHA256
    with pytest.raises(pilot.ContractDriftError, match="rubric contract"):
        pilot._validate_evaluation_contract(items, rubric_changed, sources, runtime)

    prompt_changed = deepcopy(runtime)
    prompt_changed["classifier"]["prompt"]["system_text"] += " mutation"
    assert pilot.runtime_component_hash(prompt_changed["classifier"]["prompt"]) != (
        pilot.EXPECTED_SOL_COMPONENT_HASHES["classifier_prompt"]
    )
    with pytest.raises(pilot.ContractDriftError, match="Sol runtime contract"):
        pilot._validate_evaluation_contract(items, rubrics, sources, prompt_changed)

    schema_changed = deepcopy(runtime)
    schema_changed["judge"]["schema"]["template"]["additionalProperties"] = True
    assert pilot.runtime_component_hash(schema_changed["judge"]["schema"]) != (
        pilot.EXPECTED_SOL_COMPONENT_HASHES["judge_schema"]
    )
    with pytest.raises(pilot.ContractDriftError, match="Sol runtime contract"):
        pilot._validate_evaluation_contract(items, rubrics, sources, schema_changed)

    source_changed = dict(sources)
    source_changed["harness/walkworthy/loader.py"] = "0" * 64
    with pytest.raises(pilot.ContractDriftError, match="contract source"):
        pilot._validate_evaluation_contract(items, rubrics, source_changed, runtime)
