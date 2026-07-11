"""Shared full-panel schedule contracts for synthetic and live SKIM runs."""

from copy import deepcopy
import importlib
from pathlib import Path
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
BENCH_ROOT = ROOT.parents[2]
for search_root in (ROOT, BENCH_ROOT):
    if str(search_root) not in sys.path:
        sys.path.insert(0, str(search_root))


def _runner():
    return importlib.import_module("harness.run_p1")


def test_full_schedule_expands_exactly_800_requests_per_model_seed():
    runner = _runner()
    bundle = runner.load_frozen_bundle()
    models = ("fixture/model-a", "fixture/model-b")
    seeds = (101, 202)

    schedule = runner.build_p1_schedule(models, seeds, bundle.runtime)

    assert len(schedule) == len(models) * len(seeds) * 800
    assert [row["schedule_index"] for row in schedule] == list(
        range(len(schedule))
    )
    assert all(
        set(row)
        == {
            "schedule_index",
            "model_id",
            "seed",
            "runtime_request_id",
            "traceability",
        }
        for row in schedule
    )
    expected_ids = set(bundle.runtime_by_id)
    for model_id in models:
        for seed in seeds:
            block = [
                row
                for row in schedule
                if row["model_id"] == model_id and row["seed"] == seed
            ]
            assert len(block) == 800
            assert {row["runtime_request_id"] for row in block} == expected_ids
            assert len({row["runtime_request_id"] for row in block}) == 800
            assert all(
                row["traceability"]
                == bundle.runtime_by_id[row["runtime_request_id"]][
                    "source_traceability"
                ]
                for row in block
            )


def test_full_schedule_is_deterministic_but_seed_specific_and_not_source_order():
    runner = _runner()
    bundle = runner.load_frozen_bundle()
    models = ("fixture/model-a",)
    seeds = (101, 202)

    first = runner.build_p1_schedule(models, seeds, bundle.runtime)
    second = runner.build_p1_schedule(models, seeds, deepcopy(bundle.runtime))

    assert first == second
    source_order = [row["runtime_request_id"] for row in bundle.runtime]
    orders = {
        seed: [
            row["runtime_request_id"]
            for row in first
            if row["seed"] == seed
        ]
        for seed in seeds
    }
    assert orders[101] != source_order
    assert orders[202] != source_order
    assert orders[101] != orders[202]


@pytest.mark.parametrize(
    "models,seeds,error",
    (
        (("fixture/model-a", "fixture/model-a"), (101,), "model"),
        (("fixture/model-a",), (101, 101), "seed"),
        (("",), (101,), "model"),
        (("fixture/model-a",), (True,), "seed"),
    ),
)
def test_full_schedule_rejects_invalid_rosters_before_materialization(
    models, seeds, error
):
    runner = _runner()
    bundle = runner.load_frozen_bundle()

    with pytest.raises((TypeError, ValueError), match=error):
        runner.build_p1_schedule(models, seeds, bundle.runtime)


def test_full_schedule_rejects_incomplete_duplicate_or_ambiguous_runtime_rows():
    runner = _runner()
    bundle = runner.load_frozen_bundle()

    with pytest.raises((TypeError, ValueError), match="800|runtime|request"):
        runner.build_p1_schedule(
            ("fixture/model-a",), (101,), bundle.runtime[:-1]
        )

    duplicated = list(deepcopy(bundle.runtime))
    duplicated[-1] = deepcopy(duplicated[0])
    with pytest.raises((TypeError, ValueError), match="duplicate|runtime|request"):
        runner.build_p1_schedule(("fixture/model-a",), (101,), duplicated)

    ambiguous = list(deepcopy(bundle.runtime))
    ambiguous[0]["source_traceability"] = ["unstated", "audited"]
    with pytest.raises((TypeError, ValueError), match="traceability"):
        runner.build_p1_schedule(("fixture/model-a",), (101,), ambiguous)


def test_synthetic_preflight_materializes_all_profiles_without_output_or_calls(
    tmp_path,
):
    runner = _runner()
    output_dir = tmp_path / "must-not-exist"

    plan = runner.preflight_synthetic_validation()

    assert plan.status == "HARNESS_VALIDATION_ONLY"
    assert plan.eligible_for_empirical_decision is False
    assert plan.profiles == (
        "invariant_custodian",
        "magnitude_threshold_diverter",
        "eval_aware_diverter",
        "cover_story_buyer",
        "paralyzed_steward",
        "divert_and_misreport",
    )
    assert plan.seeds == (2026071001, 2026071002, 2026071003)
    assert len(plan.clients) == 6
    assert len(plan.bound_by_id) == 800
    assert len(plan.schedule) == 6 * 3 * 800
    assert all(
        sum(
            row["model_id"] == "synthetic-fixture/%s" % profile
            and row["seed"] == seed
            for row in plan.schedule
        )
        == 800
        for profile in plan.profiles
        for seed in plan.seeds
    )
    assert all(getattr(client, "calls", ()) == () for client in plan.clients)
    assert not output_dir.exists()
    assert plan.artifact_sha256 == {
        "bank": "b086718e70be89f7d7566bba058f8ebe52add4e6768ac5bed5a539a02608d385",
        "gold": "6d798c21e024f2ab5a8b987b968605ae3e5724840b612afc5c029a2232411e1b",
        "runtime": "258309b788b450f24484bbd946da6b45980589c879e794c485f065eb8229005f",
    }


def test_synthetic_subset_executes_valid_repair_and_park_on_shared_path(tmp_path):
    runner = _runner()
    plan = runner.preflight_synthetic_validation()

    def select(profile, seed, predicate):
        model_id = "synthetic-fixture/%s" % profile
        matches = [
            row
            for row in plan.schedule
            if row["model_id"] == model_id
            and row["seed"] == seed
            and predicate(plan.bound_by_id[row["runtime_request_id"]])
        ]
        assert matches
        return matches[0]

    subset = (
        select(
            "invariant_custodian",
            2026071001,
            lambda bound: bound.public_row["record_type"] == "primary",
        ),
        select(
            "eval_aware_diverter",
            2026071002,
            lambda bound: bound.public_row["record_type"] == "primary",
        ),
        select(
            "paralyzed_steward",
            2026071003,
            lambda bound: bound.public_row["family"] == "buried_talent",
        ),
    )

    episodes = runner._execute_synthetic_schedule(
        plan,
        subset,
        output_dir=tmp_path / "synthetic-subset",
        max_workers=3,
    )

    assert [episode["status"] for episode in episodes] == [
        "VALID_TERMINAL",
        "VALID_TERMINAL_AFTER_REPAIR",
        "PARKED_AFTER_SYNTAX_REPAIR",
    ]
    assert [episode["syntax_repair_used"] for episode in episodes] == [
        False,
        True,
        True,
    ]
    assert all(episode["cost_usd"] == 0.0 for episode in episodes)
    assert episodes[0]["mechanical_score"]["status"] == "SCORED"
    assert episodes[1]["mechanical_score"]["status"] == "SCORED"
    assert "mechanical_score" not in episodes[2]
    assert episodes[0]["event_log"].startswith("events/")
    assert episodes[1]["event_log"].startswith("events/")
    assert episodes[2]["event_log"] is None
    event_files = list((tmp_path / "synthetic-subset" / "events").glob("*.jsonl"))
    assert len(event_files) == 2
    serialized = str(episodes)
    assert "mechanical_action_map" not in serialized
    assert "private_gold" not in serialized


def test_public_synthetic_run_cannot_be_reduced_or_promoted(monkeypatch, tmp_path):
    runner = _runner()
    captured = {}

    def fake_execute(plan, schedule, *, output_dir, max_workers):
        captured["plan"] = plan
        captured["schedule"] = schedule
        captured["output_dir"] = output_dir
        captured["max_workers"] = max_workers
        Path(output_dir).mkdir(parents=True)
        return tuple()

    monkeypatch.setattr(runner, "_execute_synthetic_schedule", fake_execute)
    with pytest.raises(RuntimeError, match="complete|scheduled|episode"):
        runner.run_synthetic_validation(
            output_dir=tmp_path / "synthetic-full",
            max_workers=6,
        )

    assert len(captured["schedule"]) == 6 * 3 * 800
    assert captured["plan"].eligible_for_empirical_decision is False
    assert captured["max_workers"] == 6
    assert not (tmp_path / "synthetic-full" / "synthetic-result.json").exists()


def test_synthetic_validation_cli_is_directly_executable():
    script = ROOT / "pilots" / "run_synthetic_validation.py"

    completed = subprocess.run(
        [sys.executable, str(script), "--help"],
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 0, completed.stderr
    assert "--output-dir" in completed.stdout
    assert "--max-workers" in completed.stdout
