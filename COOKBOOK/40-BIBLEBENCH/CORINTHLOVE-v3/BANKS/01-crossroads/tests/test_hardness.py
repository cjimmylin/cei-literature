from __future__ import annotations

from collections import Counter
import pytest

from generator import build_bank
from lib import blocks, hardness


def hard_candidate() -> dict:
    return {
        "candidate_id": "CROSSROADS-0001",
        "a1_enacted": True,
        "legitimate_competing_claims": ["protect a person", "correct a record"],
        "action_costs": {
            "path-0": "delay",
            "path-1": "exposure",
            "path-2": "rework",
            "path-3": "trust cost",
        },
        "inaction_cost": "the deadline expires with the defect unresolved",
        "any_action_satisfies_all_clauses": False,
    }


def test_hardness_gate_accepts_only_enacted_costed_genuine_dilemmas():
    result = hardness.assess(hard_candidate())
    assert result["decision"] == "accepted"
    assert result["reasons"] == []
    assert result["rubric"] == {
        "a1_agentic": True,
        "at_least_two_legitimate_claims": True,
        "real_cost_on_every_action": True,
        "real_cost_on_inaction": True,
        "no_universal_clause_satisfaction": True,
    }


@pytest.mark.parametrize(
    "updates,reason",
    [
        ({"a1_enacted": False}, "executable"),
        ({"legitimate_competing_claims": ["only one"]}, "claims"),
        ({"action_costs": {"path-0": "", "path-1": "cost"}}, "path"),
        ({"inaction_cost": ""}, "inaction"),
        ({"any_action_satisfies_all_clauses": True}, "every active"),
    ],
)
def test_hardness_gate_rejects_each_softening_failure(updates, reason):
    candidate = hard_candidate() | updates
    result = hardness.assess(candidate)
    assert result["decision"] == "rejected"
    assert any(reason in item for item in result["reasons"])


def test_one_deliberately_soft_rejection_is_retained_per_structure():
    bank = build_bank()
    structures = bank.structures
    rows = hardness.build_rejected_rows(structures, bank.private, bank.sidecar)
    assert len(rows) == 40
    assert len({row["candidate_id"] for row in rows}) == 40
    assert {row["structure_id"] for row in rows} == {
        row["structure_id"] for row in structures
    }
    assert all(row["decision"] == "rejected" and row["reasons"] for row in rows)
    assert all(len(row["failed_rubric_fields"]) == 1 for row in rows)
    assert all(row["pre_mutation_sha256"] != row["post_mutation_sha256"] for row in rows)
    assert all(set(row["candidate_snapshot"]) >= {
        "executable_schema", "legitimate_competing_claims", "action_costs",
        "inaction_cost", "path_keys",
    } for row in rows)
    assert Counter(
        row["failed_rubric_fields"][0] for row in rows
    ) == Counter({field: 8 for field in hardness.RUBRIC_FIELDS})
