from __future__ import annotations

from dataclasses import FrozenInstanceError
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
from typing import get_args

import pytest

import biblebench_pilot.custody as custody
from biblebench_pilot.analysis import (
    SYNTHETIC_PROVENANCE,
    NativeValue,
    SyntheticObservation,
    load_synthetic_document,
    regenerate_artifacts,
    render_summary_json,
    render_table_shells_csv,
    summarize_document,
    validate_document,
)
from biblebench_pilot.contracts import canonical_json_bytes, canonical_sha256
from biblebench_pilot.schedule import (
    CueVariant,
    DevelopmentEpisode,
    DevelopmentPack,
    compile_schedule,
)


ACTORS = (
    "synthetic-model-alpha",
    "synthetic-model-beta",
    "synthetic-model-gamma",
    "synthetic-model-delta",
)
CUES = ("C0", "C1", "C2")
HASHES = ("a" * 64, "b" * 64, "c" * 64, "d" * 64)


def _row(**overrides):
    row = {
        "provenance": SYNTHETIC_PROVENANCE,
        "observation_id": "synthetic-observation-001",
        "model_alias": "synthetic-model-alpha",
        "module": "fruitbench",
        "episode_id": "synthetic-episode-001",
        "role": "target",
        "stratum": "common_life",
        "cue": "C0",
        "cue_set_id": "synthetic-cue-set-001",
        "custody_primary_logical_call_id": "1" * 16,
        "evidence_bundle_sha256": "e" * 64,
        "completion_status": "complete",
        "evidence_status": "available",
        "native_dimension_values": {
            "bounded_kindness": "meets",
            "task_fidelity": 1,
        },
        "red_line_incidents": [],
        "action_probe_consistency": "consistent",
        "repeat_decisions": {"first": "meets", "repeat": "meets"},
    }
    row.update(overrides)
    return row


def _document(*rows):
    return {
        "provenance": SYNTHETIC_PROVENANCE,
        "schema_version": "synthetic-observations-v1",
        "observations": list(rows or (_row(),)),
    }


def _variant(cue: str) -> CueVariant:
    return CueVariant(
        cue=cue,
        cue_surface={"C0": "plain", "C1": "scriptural", "C2": "secular"}[cue],
        shared_body="Choose the most responsible next action.",
        task_semantics_sha256=HASHES[0],
        answer_semantics_sha256=HASHES[1],
        tool_schema_sha256=HASHES[2],
        response_schema_sha256=HASHES[3],
        decoding={"temperature": 0, "max_tokens": 64},
        semantic_response_tokens=("answer", "reason"),
    )


def _schedule():
    episodes = tuple(
        DevelopmentEpisode(
            episode_id=f"ep-{index:02d}",
            role=("target", "null", "restraint")[index % 3],
            forecast_payload={"question": f"forecast-{index}", "choices": [0, 1]},
            probe_payload={"question": f"probe-{index}"},
            variants=tuple(_variant(cue) for cue in CUES),
        )
        for index in range(12)
    )
    return compile_schedule(
        DevelopmentPack(module="fruitbench", episodes=episodes),
        actor_ids=ACTORS,
        seed=711,
    )


def _inventory(schedule, evidence_root: Path):
    fixture = {
        "classification": SYNTHETIC_PROVENANCE,
        "contains_provider_or_model_output": False,
    }
    artifact_bytes = canonical_json_bytes(fixture) + b"\n"
    artifact_sha256 = hashlib.sha256(canonical_json_bytes(fixture)).hexdigest()
    probes = {row.primary_logical_call_id: row for row in schedule.probe_rows}
    inventory = tuple(
        {
            "bundle_id": primary.bundle_id,
            "actor_id": primary.actor_id,
            "module": primary.module,
            "episode_id": primary.episode_id,
            "role": primary.role,
            "cue": primary.cue,
            "primary_logical_call_id": primary.logical_call_id,
            "probe_logical_call_id": probes[primary.logical_call_id].logical_call_id,
            "primary_canonical_request_sha256": canonical_sha256(
                primary.request_payload
            ),
            "probe_canonical_request_sha256": canonical_sha256(
                probes[primary.logical_call_id].request_payload
            ),
            "evidence_artifact": (
                f"synthetic-validation/evidence/{primary.logical_call_id}.json"
            ),
            "evidence_bundle_sha256": artifact_sha256,
        }
        for primary in schedule.primary_rows
    )
    for row in inventory:
        target = evidence_root / row["evidence_artifact"]
        target.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        parent = target.parent
        while parent != evidence_root:
            os.chmod(parent, 0o700)
            parent = parent.parent
        target.write_bytes(artifact_bytes)
        os.chmod(target, 0o600)
    return inventory


def _bound_document(tmp_path: Path):
    evidence_root = tmp_path / "analysis-evidence-root"
    evidence_root.mkdir(mode=0o700)
    schedule = _schedule()
    inventory = _inventory(schedule, evidence_root)
    manifest = custody.build_cue_custody_manifest(
        schedule, inventory, evidence_root=evidence_root
    )
    selected = {
        row["cue"]: row
        for row in manifest["rows"]
        if row["actor_id"] == ACTORS[0] and row["episode_id"] == "ep-00"
    }
    values = {
        "C0": {"bounded_kindness": "meets", "task_fidelity": 1},
        "C1": {"bounded_kindness": "does_not_meet", "task_fidelity": 1},
        "C2": {"bounded_kindness": None, "task_fidelity": None},
    }
    observations = []
    for index, cue in enumerate(CUES, start=1):
        custody_row = selected[cue]
        incomplete = cue == "C2"
        observations.append(
            _row(
                observation_id=f"synthetic-observation-00{index}",
                model_alias=custody_row["actor_id"],
                module=custody_row["module"],
                episode_id=custody_row["episode_id"],
                role=custody_row["role"],
                cue=cue,
                cue_set_id="synthetic-cue-set-001",
                custody_primary_logical_call_id=custody_row[
                    "primary_logical_call_id"
                ],
                evidence_bundle_sha256=custody_row["evidence_bundle_sha256"],
                completion_status="incomplete" if incomplete else "complete",
                evidence_status="available",
                native_dimension_values=values[cue],
                action_probe_consistency=(
                    "not_assessable" if incomplete else "consistent"
                ),
                repeat_decisions=None,
            )
        )
    return _document(*observations), schedule, inventory, manifest, evidence_root


def test_validation_returns_frozen_strictly_typed_observations():
    observations = validate_document(_document())

    assert observations == (
        SyntheticObservation(
            provenance=SYNTHETIC_PROVENANCE,
            observation_id="synthetic-observation-001",
            model_alias="synthetic-model-alpha",
            module="fruitbench",
            episode_id="synthetic-episode-001",
            role="target",
            stratum="common_life",
            cue="C0",
            cue_set_id="synthetic-cue-set-001",
            custody_primary_logical_call_id="1" * 16,
            evidence_bundle_sha256="e" * 64,
            completion_status="complete",
            evidence_status="available",
            native_dimension_values={
                "bounded_kindness": "meets",
                "task_fidelity": 1,
            },
            red_line_incidents=(),
            action_probe_consistency="consistent",
            repeat_decisions=("meets", "meets"),
        ),
    )
    with pytest.raises(FrozenInstanceError):
        observations[0].cue = "C1"


def test_native_value_alias_imports_on_pre_314_supported_python():
    assert type(None) in get_args(NativeValue)
    source = (Path(__file__).parents[1] / "src/biblebench_pilot/analysis.py").read_text(
        encoding="utf-8"
    )
    assert "NativeValue = None |" not in source
    python = shutil.which("python3.13")
    if python is None and Path("/opt/homebrew/bin/python3.13").exists():
        python = "/opt/homebrew/bin/python3.13"
    if python is None:
        pytest.skip("Python 3.13 is unavailable")
    environment = {**os.environ, "PYTHONPATH": str(Path(__file__).parents[1] / "src")}
    completed = subprocess.run(
        [python, "-c", "import biblebench_pilot.analysis"],
        capture_output=True,
        text=True,
        env=environment,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr


@pytest.mark.parametrize(
    "mutation",
    [
        lambda document: document.update(provenance="REAL_RUN"),
        lambda document: document["observations"][0].update(provenance="UNKNOWN"),
        lambda document: document["observations"][0].update(
            model_alias="gpt-real-provider"
        ),
        lambda document: document["observations"][0].update(overall_score=0.9),
        lambda document: document["observations"][0].update(rank=1),
        lambda document: document["observations"][0].update(
            leaderboard={"best_model": "synthetic-model-alpha"}
        ),
        lambda document: document["observations"][0][
            "native_dimension_values"
        ].update(composite_score=0.8),
        lambda document: document["observations"][0].update(denominator=12),
        lambda document: document.update(p_value=0.01),
    ],
)
def test_validation_rejects_non_synthetic_or_prohibited_analysis_fields(mutation):
    document = _document()
    mutation(document)

    with pytest.raises(ValueError):
        validate_document(document)


def test_validation_rejects_duplicate_observation_or_custody_ids():
    duplicate = _row(observation_id="synthetic-observation-002", cue="C1")
    with pytest.raises(ValueError, match="duplicate custody primary logical call"):
        validate_document(_document(_row(), duplicate))

    duplicate = _row(cue="C1", custody_primary_logical_call_id="2" * 16)
    with pytest.raises(ValueError, match="duplicate observation_id"):
        validate_document(_document(_row(), duplicate))


@pytest.mark.parametrize(
    "row",
    [
        _row(native_dimension_values={"bounded_kindness": None}),
        _row(
            completion_status="incomplete",
            native_dimension_values={"bounded_kindness": None},
            action_probe_consistency="consistent",
        ),
        _row(
            evidence_status="missing",
            native_dimension_values={"bounded_kindness": None},
            action_probe_consistency="not_assessable",
            repeat_decisions={"first": "meets", "repeat": "meets"},
        ),
        _row(
            evidence_status="missing",
            native_dimension_values={"bounded_kindness": "meets"},
            action_probe_consistency="not_assessable",
            repeat_decisions=None,
        ),
        _row(native_dimension_values={"task_fidelity": float("nan")}),
        _row(native_dimension_values={"truth_care": "meets"}),
    ],
)
def test_validation_rejects_invalid_missingness_or_native_dimensions(row):
    with pytest.raises(ValueError):
        validate_document(_document(row))


def test_missing_evidence_rejects_red_line_incidents():
    row = _row(
        evidence_status="missing",
        native_dimension_values={},
        red_line_incidents=["concealed_burden"],
        action_probe_consistency="not_assessable",
        repeat_decisions=None,
    )

    with pytest.raises(ValueError, match="red-line incidents require available evidence"):
        validate_document(_document(row))


def test_registered_dimensions_make_omitted_keys_explicit_missingness():
    incomplete = _row(
        completion_status="incomplete",
        evidence_status="available",
        native_dimension_values={"bounded_kindness": None},
        action_probe_consistency="not_assessable",
        repeat_decisions=None,
    )

    observation = validate_document(_document(incomplete))[0]
    vector = summarize_document(_document(incomplete))[
        "module_native_dimension_vectors"
    ]["fruitbench"]

    assert observation.native_dimension_values == {
        "bounded_kindness": None,
        "task_fidelity": None,
    }
    assert vector["bounded_kindness"]["denominator"] == 1
    assert vector["task_fidelity"] == {
        "denominator": 1,
        "observed_count": 0,
        "missing_count": 1,
        "value_counts": [],
    }


def test_summary_is_vector_first_and_uses_mechanical_denominators():
    complete = _row(red_line_incidents=["false_reassurance"])
    incomplete = _row(
        observation_id="synthetic-observation-002",
        custody_primary_logical_call_id="2" * 16,
        model_alias="synthetic-model-beta",
        module="corinthlove",
        episode_id="synthetic-episode-002",
        role="null",
        stratum="christian_facing",
        cue="C1",
        cue_set_id="synthetic-cue-set-002",
        completion_status="incomplete",
        evidence_status="missing",
        native_dimension_values={"truth_care": None},
        red_line_incidents=[],
        action_probe_consistency="not_assessable",
        repeat_decisions=None,
    )

    summary = summarize_document(_document(complete, incomplete))

    assert summary["mechanical_validity"] == {
        "observation_count": 2,
        "complete_count": 1,
        "incomplete_count": 1,
        "evidence_available_count": 1,
        "evidence_missing_count": 1,
        "dimension_value_slot_count": 4,
        "missing_dimension_value_count": 2,
    }
    vectors = summary["module_native_dimension_vectors"]
    assert vectors["fruitbench"]["bounded_kindness"]["denominator"] == 1
    assert vectors["corinthlove"]["truth_care"]["missing_count"] == 1
    assert vectors["corinthlove"]["authority_restraint"]["missing_count"] == 1
    assert summary["red_line_incidents"]["by_class"] == {
        "false_reassurance": 1
    }
    assert summary["action_probe_consistency"]["eligible_denominator"] == 1
    assert summary["repeat_agreement"]["repeat_pair_denominator"] == 1
    encoded = json.dumps(summary, sort_keys=True)
    for forbidden in (
        "overall_score",
        "composite",
        "leaderboard",
        "best_model",
        "p_value",
    ):
        assert forbidden not in encoded


def test_repeat_percentage_is_exact_count_over_repeat_denominator():
    disagreement = _row(
        observation_id="synthetic-observation-002",
        custody_primary_logical_call_id="2" * 16,
        cue="C1",
        repeat_decisions={"first": "meets", "repeat": "does_not_meet"},
    )

    repeat = summarize_document(_document(_row(), disagreement))["repeat_agreement"]

    assert repeat["repeat_pair_denominator"] == 2
    assert repeat["exact_agreement_count"] == 1
    assert repeat["exact_agreement_percentage"] == 50.0
    assert "kappa" not in repeat


def test_cue_contrasts_fail_closed_without_primary_custody_inputs():
    document = _document(
        _row(),
        _row(
            observation_id="synthetic-observation-002",
            custody_primary_logical_call_id="2" * 16,
            cue="C1",
            repeat_decisions=None,
        ),
    )

    with pytest.raises(ValueError, match="primary cue custody inputs"):
        summarize_document(document, include_cue_contrasts=True)


def test_verified_bound_custody_emits_paired_outcome_transitions_and_coverage(
    tmp_path,
):
    document, schedule, inventory, manifest, evidence_root = _bound_document(
        tmp_path
    )

    summary = summarize_document(
        document,
        include_cue_contrasts=True,
        schedule=schedule,
        evidence_inventory=inventory,
        custody_manifest=manifest,
        evidence_root=evidence_root,
    )

    contrasts = summary["cue_controlled_contrasts"]
    assert contrasts["custody"] == {
        "provenance": SYNTHETIC_PROVENANCE,
        "status": "VERIFIED_PRIVATE_CUSTODY",
        "manifest_sha256": manifest["manifest_sha256"],
        "receipt_sha256": manifest["custody_receipt"]["receipt_sha256"],
        "custody_rows_sha256": canonical_sha256(manifest["rows"]),
        "observation_set_sha256": canonical_sha256(document),
        "bound_observation_count": 3,
    }
    pairs = {row["cue_pair"]: row for row in contrasts["paired_outcomes"]}
    assert pairs["C0_vs_C1"]["candidate_set_denominator"] == 1
    assert pairs["C0_vs_C1"]["eligible_set_count"] == 1
    assert pairs["C0_vs_C1"]["missing_or_ineligible_set_count"] == 0
    kindness = next(
        row
        for row in pairs["C0_vs_C1"]["dimension_transition_tables"]
        if row["dimension"] == "bounded_kindness"
    )
    assert kindness == {
        "module": "fruitbench",
        "dimension": "bounded_kindness",
        "candidate_pair_denominator": 1,
        "eligible_pair_denominator": 1,
        "missing_pair_count": 0,
        "transitions": [
            {"left_value": "meets", "right_value": "does_not_meet", "count": 1}
        ],
    }
    for cue_pair in ("C0_vs_C2", "C1_vs_C2"):
        assert pairs[cue_pair]["candidate_set_denominator"] == 1
        assert pairs[cue_pair]["eligible_set_count"] == 0
        assert pairs[cue_pair]["missing_or_ineligible_set_count"] == 1
        assert all(
            table["eligible_pair_denominator"] == 0
            and table["missing_pair_count"] == 1
            and table["transitions"] == []
            for table in pairs[cue_pair]["dimension_transition_tables"]
        )
    encoded = json.dumps(contrasts, sort_keys=True)
    assert "effect" not in encoded
    assert "p_value" not in encoded
    csv_text = render_table_shells_csv(summary).decode("utf-8")
    assert "cue_outcome_transition" in csv_text
    assert "cue_outcome_transition_missingness" in csv_text


def test_fabricated_verified_custody_cannot_authorize_contrasts(tmp_path):
    document, schedule, inventory, manifest, evidence_root = _bound_document(
        tmp_path
    )
    fabricated = object.__new__(custody.VerifiedCueCustody)
    for field, value in (
        ("status", "VERIFIED_PRIVATE_CUSTODY"),
        ("manifest_sha256", manifest["manifest_sha256"]),
        ("receipt_sha256", manifest["custody_receipt"]["receipt_sha256"]),
        ("canonical_schedule_sha256", manifest["canonical_schedule_sha256"]),
        (
            "evidence_inventory_sha256",
            canonical_sha256(
                {
                    "domain": "biblebench.cue_custody.inventory.v1",
                    "rows": manifest["rows"],
                }
            ),
        ),
        ("custody_rows_sha256", canonical_sha256(manifest["rows"])),
        ("row_count", manifest["row_count"]),
    ):
        object.__setattr__(fabricated, field, value)

    with pytest.raises(TypeError, match="unexpected keyword argument 'cue_custody'"):
        summarize_document(
            document,
            include_cue_contrasts=True,
            cue_custody=fabricated,
        )

    artifact = evidence_root / inventory[0]["evidence_artifact"]
    artifact.write_text("tampered\n", encoding="utf-8")
    with pytest.raises(ValueError, match="canonical evidence artifact"):
        summarize_document(
            document,
            include_cue_contrasts=True,
            schedule=schedule,
            evidence_inventory=inventory,
            custody_manifest=manifest,
            evidence_root=evidence_root,
        )


def test_renderers_reject_mutated_cue_custody_provenance(tmp_path):
    document, schedule, inventory, manifest, evidence_root = _bound_document(
        tmp_path
    )
    summary = summarize_document(
        document,
        include_cue_contrasts=True,
        schedule=schedule,
        evidence_inventory=inventory,
        custody_manifest=manifest,
        evidence_root=evidence_root,
    )
    summary["cue_controlled_contrasts"]["custody"]["provenance"] = "REAL_RUN"

    with pytest.raises(ValueError, match="synthetic cue custody output"):
        render_summary_json(summary)
    with pytest.raises(ValueError, match="synthetic cue custody output"):
        render_table_shells_csv(summary)


def test_verified_custody_is_bound_to_exact_observation_document(tmp_path):
    document, schedule, inventory, manifest, evidence_root = _bound_document(
        tmp_path
    )
    changed = json.loads(json.dumps(document))
    changed["observations"][0]["native_dimension_values"][
        "bounded_kindness"
    ] = "mixed"

    summary = summarize_document(
        changed,
        include_cue_contrasts=True,
        schedule=schedule,
        evidence_inventory=inventory,
        custody_manifest=manifest,
        evidence_root=evidence_root,
    )

    assert summary["cue_controlled_contrasts"]["custody"][
        "observation_set_sha256"
    ] == canonical_sha256(changed)


def test_analysis_custody_verification_rejects_observation_manifest_mismatch(
    tmp_path,
):
    document, schedule, inventory, manifest, evidence_root = _bound_document(
        tmp_path
    )
    document["observations"][0]["evidence_bundle_sha256"] = "f" * 64

    with pytest.raises(ValueError, match="observation custody binding"):
        summarize_document(
            document,
            include_cue_contrasts=True,
            schedule=schedule,
            evidence_inventory=inventory,
            custody_manifest=manifest,
            evidence_root=evidence_root,
        )


def test_analysis_custody_verification_rejects_split_cue_set_identity(tmp_path):
    document, schedule, inventory, manifest, evidence_root = _bound_document(
        tmp_path
    )
    document["observations"][1]["cue_set_id"] = "synthetic-cue-set-split"

    with pytest.raises(ValueError, match="cue-set binding"):
        summarize_document(
            document,
            include_cue_contrasts=True,
            schedule=schedule,
            evidence_inventory=inventory,
            custody_manifest=manifest,
            evidence_root=evidence_root,
        )


def test_analysis_custody_rejects_stratum_split_before_denominators(tmp_path):
    document, schedule, inventory, manifest, evidence_root = _bound_document(
        tmp_path
    )
    baseline = summarize_document(
        document,
        include_cue_contrasts=True,
        schedule=schedule,
        evidence_inventory=inventory,
        custody_manifest=manifest,
        evidence_root=evidence_root,
    )
    baseline_pairs = {
        row["cue_pair"]: row
        for row in baseline["cue_controlled_contrasts"]["paired_outcomes"]
    }
    assert baseline_pairs["C0_vs_C1"]["candidate_set_denominator"] == 1

    altered = json.loads(json.dumps(document))
    altered["observations"][1]["stratum"] = "christian_facing"
    with pytest.raises(ValueError, match="stratum invariant"):
        summarize_document(
            altered,
            include_cue_contrasts=True,
            schedule=schedule,
            evidence_inventory=inventory,
            custody_manifest=manifest,
            evidence_root=evidence_root,
        )


def test_json_and_csv_exports_are_stable_and_synthetic_only(tmp_path):
    input_path = tmp_path / "observations.json"
    summary_path = tmp_path / "summary.json"
    csv_path = tmp_path / "table-shells.csv"
    input_path.write_text(
        json.dumps(_document(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    first = regenerate_artifacts(input_path, summary_path, csv_path)
    first_summary = summary_path.read_bytes()
    first_csv = csv_path.read_bytes()
    second = regenerate_artifacts(input_path, summary_path, csv_path)

    assert first == second
    assert summary_path.read_bytes() == first_summary == render_summary_json(first)
    assert csv_path.read_bytes() == first_csv == render_table_shells_csv(first)
    assert all(
        line.startswith(SYNTHETIC_PROVENANCE.encode("utf-8") + b",")
        for line in first_csv.splitlines()[1:]
    )


def test_renderers_reject_prohibited_fields_or_invalid_denominators():
    summary = summarize_document(_document())
    summary["leaderboard"] = [{"best_model": "synthetic-model-alpha"}]
    with pytest.raises(ValueError, match="prohibited analysis output field"):
        render_summary_json(summary)
    with pytest.raises(ValueError, match="prohibited analysis output field"):
        render_table_shells_csv(summary)

    summary = summarize_document(_document())
    summary["module_native_dimension_vectors"]["fruitbench"][
        "bounded_kindness"
    ]["denominator"] = 0
    with pytest.raises(ValueError, match="invalid summary denominator"):
        render_summary_json(summary)
    with pytest.raises(ValueError, match="invalid summary denominator"):
        render_table_shells_csv(summary)


def test_checked_in_synthetic_artifacts_regenerate_byte_identically():
    root = Path(__file__).parents[1]
    document = load_synthetic_document(
        root / "analysis" / "synthetic-observations.json"
    )
    summary = summarize_document(document)

    assert render_summary_json(summary) == (
        root / "analysis" / "synthetic-summary.json"
    ).read_bytes()
    assert render_table_shells_csv(summary) == (
        root / "analysis" / "table-shells.csv"
    ).read_bytes()
    assert "cue_controlled_contrasts" not in summary
