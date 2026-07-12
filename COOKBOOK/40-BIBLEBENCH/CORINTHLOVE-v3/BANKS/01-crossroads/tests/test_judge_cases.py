from __future__ import annotations

import json
from pathlib import Path
import stat
import uuid

import pytest

from lib.judge_cases import (
    JCASE_RE,
    JSEED_RE,
    OccurrenceCaseRegistry,
    canonical_response_sha256,
)


SEED = "JSEED-123e4567-e89b-42d3-a456-426614174000"
ITEM = "CROSSROADS-0001"
CASE_UUIDS = iter(
    uuid.UUID(value)
    for value in (
        "223e4567-e89b-42d3-a456-426614174000",
        "323e4567-e89b-42d3-a456-426614174000",
        "423e4567-e89b-42d3-a456-426614174000",
    )
)


def response_hash() -> str:
    return canonical_response_sha256(
        [{"role": "assistant", "content": "I enacted the repair."}],
        [{"path": "report", "sha256": "a" * 64}],
    )


def issue(registry: OccurrenceCaseRegistry, **updates) -> str:
    values = {
        "authoring_seed": SEED,
        "run_id": "run-20260711-a",
        "execution_id": "execution-0001",
        "candidate_model_snapshot": "provider/model-20260711",
        "candidate_family": "candidate-openai",
        "response_sha256": response_hash(),
        "scoring_occurrence": 1,
    }
    values.update(updates)
    return registry.issue_case(**values)


def test_occurrence_cases_are_random_unlinkable_and_never_reused(tmp_path: Path):
    registry_path = tmp_path / "private" / "judge_case_registry.jsonl"
    registry = OccurrenceCaseRegistry(
        registry_path,
        {SEED: ITEM},
        uuid_factory=lambda: next(CASE_UUIDS),
    )

    first = issue(registry)
    same_response_new_occurrence = issue(registry, scoring_occurrence=2)
    same_response_new_run = issue(
        registry,
        run_id="run-20260711-b",
        execution_id="execution-0002",
    )

    assert len({first, same_response_new_occurrence, same_response_new_run}) == 3
    assert all(JCASE_RE.fullmatch(value) for value in {
        first, same_response_new_occurrence, same_response_new_run
    })
    assert all(ITEM not in value and "model" not in value for value in {
        first, same_response_new_occurrence, same_response_new_run
    })
    with pytest.raises(ValueError, match="scoring occurrence was already issued"):
        issue(registry)

    reopened = OccurrenceCaseRegistry(registry_path, {SEED: ITEM})
    assert reopened.lookup(first)["item_id"] == ITEM
    assert reopened.lookup(first)["response_sha256"] == response_hash()
    assert stat.S_IMODE(registry_path.stat().st_mode) == 0o600


def test_case_token_collision_fails_loud_instead_of_reusing_identity(tmp_path: Path):
    repeated = uuid.UUID("223e4567-e89b-42d3-a456-426614174000")
    registry = OccurrenceCaseRegistry(
        tmp_path / "cases.jsonl",
        {SEED: ITEM},
        uuid_factory=lambda: repeated,
    )
    issue(registry)
    with pytest.raises(ValueError, match="JCASE collision"):
        issue(registry, scoring_occurrence=2)


@pytest.mark.parametrize(
    "bad_seed",
    [
        "JCASE-123e4567-e89b-42d3-a456-426614174000",
        "JUDGE-123e4567-e89b-42d3-a456-426614174000",
        "CROSSROADS-0001",
    ],
)
def test_seed_case_and_judge_namespaces_cannot_be_conflated(
        tmp_path: Path, bad_seed: str):
    with pytest.raises(ValueError, match="JSEED"):
        OccurrenceCaseRegistry(tmp_path / "cases.jsonl", {bad_seed: ITEM})
    assert JSEED_RE.fullmatch(SEED)


def test_response_hash_binding_and_unknown_case_are_fail_closed(tmp_path: Path):
    registry = OccurrenceCaseRegistry(
        tmp_path / "cases.jsonl",
        {SEED: ITEM},
        uuid_factory=lambda: uuid.UUID(
            "223e4567-e89b-42d3-a456-426614174000"
        ),
    )
    case_id = issue(registry)
    registry.assert_response_binding(case_id, response_hash())
    with pytest.raises(ValueError, match="response hash does not match"):
        registry.assert_response_binding(case_id, "f" * 64)
    with pytest.raises(ValueError, match="unknown JCASE"):
        registry.lookup("JCASE-523e4567-e89b-42d3-a456-426614174000")
    with pytest.raises(ValueError, match="JCASE"):
        registry.lookup(SEED)


def test_registry_hash_chain_detects_private_crosswalk_mutation(tmp_path: Path):
    path = tmp_path / "cases.jsonl"
    registry = OccurrenceCaseRegistry(
        path,
        {SEED: ITEM},
        uuid_factory=lambda: uuid.UUID(
            "223e4567-e89b-42d3-a456-426614174000"
        ),
    )
    issue(registry)
    record = json.loads(path.read_text(encoding="utf-8"))
    record["candidate_family"] = "rebound-family"
    path.write_text(json.dumps(record, sort_keys=True) + "\n", encoding="utf-8")
    with pytest.raises(ValueError, match="record hash"):
        OccurrenceCaseRegistry(path, {SEED: ITEM})


def test_existing_registry_with_public_permissions_is_rejected(tmp_path: Path):
    path = tmp_path / "cases.jsonl"
    path.write_text("", encoding="utf-8")
    path.chmod(0o644)
    with pytest.raises(ValueError, match="mode 0600"):
        OccurrenceCaseRegistry(path, {SEED: ITEM})
