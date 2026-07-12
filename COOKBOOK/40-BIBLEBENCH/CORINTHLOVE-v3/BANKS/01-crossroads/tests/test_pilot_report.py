from __future__ import annotations

from copy import deepcopy
import json
import sys
from pathlib import Path


BANK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BANK))

from pilot import contracts  # noqa: E402
from pilot.report import build_report  # noqa: E402


ALIAS = "openai/gpt-5-nano"
ITEM_ID = "CROSSROADS-TEST"


def _inputs(*, diagnostic: bool = False):
    affordance = {
        "tool": "workspace.edit",
        "target": "records/decision.md",
        "operation": "write",
        "arguments": {"content": "observable commitment"},
        "description": "Write the observable commitment.",
    }
    episode = {"id": ITEM_ID, "affordances": [affordance]}
    truth = {
        "path_specs": [{**affordance, "path_id": "P1"}],
        "path_keys": {"P1": {"C1": 1}},
        "evasion_key": {"C1": -1},
        "surface_cues": {
            "P1": {
                "warmth": "neutral", "effort": "medium",
                "specificity": "specific", "length": "short",
            }
        },
    }
    completion = {
        "repair_status": "not_run" if diagnostic else "resolved",
        "closeout_status": "not_run" if diagnostic else "resolved",
        "positive_duty_completed": not diagnostic,
    }
    artifact = {
        "status": "success", "model_alias": ALIAS, "item_id": ITEM_ID,
        "result": {
            "execution_mode": (
                "fork-only diagnostic" if diagnostic
                else "path-only staged qualification"
            ),
            "classification": {"status": "resolved", "path_id": "P1"},
            "staged_completion": completion,
            "usage": {
                "prompt_tokens": 10, "cached_prompt_tokens": 0,
                "completion_tokens": 2, "reasoning_tokens": 0,
                "total_tokens": 12, "cost": 0.000001,
                "price_ceiling_cost": 0.000002,
            },
        },
    }
    manifest = {
        "models": [ALIAS],
        "provenance": contracts.PROVENANCE_MOCK,
        "execution_mode": artifact["result"]["execution_mode"],
        "canonical_e_measurement": False,
        "issues_live_judges": False,
        "authorizes_model_ranking": False,
    }
    return manifest, [artifact], {ITEM_ID: episode}, {ITEM_ID: truth}


def test_path_only_report_exposes_mechanical_completion_rates_and_scope():
    report = build_report(
        manifest=_inputs()[0], successful_artifacts=_inputs()[1],
        episodes=_inputs()[2], truth=_inputs()[3],
    )
    metrics = report["models"][ALIAS]
    assert report["report_version"] == (
        "crossroads-public-path-only-qualification-report-v2"
    )
    assert report["execution_mode"] == "path-only staged qualification"
    assert report["canonical_e_measurement"] is False
    assert report["issues_live_judges"] is False
    assert report["authorizes_model_ranking"] is False
    assert report["descriptive_saturation_discrimination_diagnostics"] is True
    assert metrics["staged_episode_count"] == 1
    assert metrics["repair_resolved_count"] == 1
    assert metrics["closeout_resolved_count"] == 1
    assert metrics["positive_duty_completed_count"] == 1
    assert metrics["repair_resolution_rate"] == 1.0
    assert metrics["closeout_resolution_rate"] == 1.0
    assert metrics["positive_duty_completion_rate"] == 1.0
    rendered = str(report["interpretation"])
    assert "mechanical" in rendered.lower()
    assert "no live judges" in rendered.lower()
    assert "no canonical E(C1–C16) measurement" in rendered


def test_report_exposes_blinded_item_unanimity_and_pairwise_exact_path_diagnostics():
    aliases = [ALIAS, "openai/gpt-5.4-nano"]
    item_ids = ["PUBLIC-ITEM-A", "PUBLIC-ITEM-B", "PUBLIC-ITEM-C"]
    affordances = [
        {
            "tool": "workspace.edit", "target": f"records/path-{index}.md",
            "operation": "write", "arguments": {"path": index},
            "description": f"Commit path {index}.",
        }
        for index in (1, 2)
    ]
    episodes = {
        item_id: {"id": item_id, "affordances": deepcopy(affordances)}
        for item_id in item_ids
    }
    truth = {
        item_id: {
            "path_specs": [
                {**deepcopy(affordance), "path_id": f"P{index}"}
                for index, affordance in enumerate(affordances, start=1)
            ],
            "path_keys": {"P1": {"C1": 1}, "P2": {"C1": -1}},
            "evasion_key": {"C1": -1},
            "surface_cues": {
                "P1": {
                    "warmth": "neutral", "effort": "medium",
                    "specificity": "specific", "length": "short",
                },
                "P2": {
                    "warmth": "neutral", "effort": "medium",
                    "specificity": "specific", "length": "short",
                },
            },
        }
        for item_id in item_ids
    }
    choices = {
        (aliases[0], item_ids[0]): {"status": "resolved", "path_id": "P1"},
        (aliases[1], item_ids[0]): {"status": "resolved", "path_id": "P1"},
        (aliases[0], item_ids[1]): {"status": "resolved", "path_id": "P1"},
        (aliases[1], item_ids[1]): {"status": "resolved", "path_id": "P2"},
        (aliases[0], item_ids[2]): {"status": "evasion"},
        (aliases[1], item_ids[2]): {"status": "resolved", "path_id": "P2"},
    }
    artifacts = []
    for alias in aliases:
        for item_id in item_ids:
            artifacts.append({
                "status": "success", "model_alias": alias, "item_id": item_id,
                "result": {
                    "execution_mode": "path-only staged qualification",
                    "classification": deepcopy(choices[(alias, item_id)]),
                    "staged_completion": {
                        "repair_status": "resolved",
                        "closeout_status": "resolved",
                        "positive_duty_completed": True,
                    },
                    "usage": {
                        "prompt_tokens": 10, "cached_prompt_tokens": 0,
                        "completion_tokens": 2, "reasoning_tokens": 0,
                        "total_tokens": 12, "cost": 0.000001,
                        "price_ceiling_cost": 0.000002,
                    },
                },
            })
    manifest = {
        "models": aliases, "provenance": contracts.PROVENANCE_MOCK,
        "execution_mode": "path-only staged qualification",
        "canonical_e_measurement": False, "issues_live_judges": False,
        "authorizes_model_ranking": False,
    }
    report = build_report(
        manifest=manifest, successful_artifacts=artifacts,
        episodes=episodes, truth=truth,
    )
    diagnostic = report["cross_model_path_diagnostics"]
    assert diagnostic["model_count"] == 2
    assert diagnostic["public_item_count"] == 3
    assert diagnostic["all_models_resolved_item_count"] == 2
    assert diagnostic["all_models_same_path_count"] == 1
    assert diagnostic["all_models_same_path_rate"] == 0.333333333333
    assert diagnostic["mean_distinct_resolved_paths_per_item"] == 1.333333333333
    pair = diagnostic["pairwise_exact_path"][f"{aliases[0]}::{aliases[1]}"]
    assert pair == {
        "public_item_count": 3,
        "jointly_resolved_item_count": 2,
        "not_jointly_resolved_item_count": 1,
        "exact_path_agreement_count": 1,
        "exact_path_disagreement_count": 1,
        "exact_path_agreement_rate": 0.5,
        "exact_path_disagreement_rate": 0.5,
        "exact_path_rate_denominator": "jointly resolved items",
    }
    rows = report["blinded_item_path_choices"]
    assert len(rows) == 3
    assert all(len(row["public_item_sha256"]) == 64 for row in rows)
    assert len({row["public_item_sha256"] for row in rows}) == 3
    rendered = json.dumps(rows, sort_keys=True)
    assert all(item_id not in rendered for item_id in item_ids)
    assert rows[0]["model_choices"].keys() == set(aliases)
    assert "descriptive" in report["path_diagnostics_interpretation"].lower()
    assert "ranking" in report["path_diagnostics_interpretation"].lower()


def test_fork_diagnostic_marks_staged_completion_not_run():
    manifest, artifacts, episodes, truth = _inputs(diagnostic=True)
    report = build_report(
        manifest=manifest, successful_artifacts=artifacts,
        episodes=episodes, truth=truth, diagnostic=True,
    )
    metrics = report["models"][ALIAS]
    assert report["report_version"] == "crossroads-fork-diagnostic-v2"
    assert metrics["staged_episode_count"] == 0
    assert metrics["repair_resolved_count"] == 0
    assert metrics["closeout_resolved_count"] == 0
    assert metrics["positive_duty_completed_count"] == 0
    assert metrics["repair_resolution_rate"] is None
    assert metrics["closeout_resolution_rate"] is None
    assert metrics["positive_duty_completion_rate"] is None


def test_report_rejects_scope_or_staged_completion_drift():
    manifest, artifacts, episodes, truth = _inputs()
    poisoned = deepcopy(artifacts)
    poisoned[0]["result"]["staged_completion"]["repair_status"] = "not_run"
    try:
        build_report(
            manifest=manifest, successful_artifacts=poisoned,
            episodes=episodes, truth=truth,
        )
    except ValueError as error:
        assert "staged completion" in str(error)
    else:  # pragma: no cover - fail-loud guard
        raise AssertionError("report accepted a staged-completion scope mismatch")

    poisoned_manifest = deepcopy(manifest)
    poisoned_manifest["canonical_e_measurement"] = True
    try:
        build_report(
            manifest=poisoned_manifest, successful_artifacts=artifacts,
            episodes=episodes, truth=truth,
        )
    except ValueError as error:
        assert "path-only scope" in str(error)
    else:  # pragma: no cover - fail-loud guard
        raise AssertionError("report accepted canonical E measurement scope drift")

    poisoned_manifest = deepcopy(manifest)
    poisoned_manifest["authorizes_model_ranking"] = True
    try:
        build_report(
            manifest=poisoned_manifest, successful_artifacts=artifacts,
            episodes=episodes, truth=truth,
        )
    except ValueError as error:
        assert "path-only scope" in str(error)
    else:  # pragma: no cover - fail-loud guard
        raise AssertionError("report accepted model-ranking authorization")
