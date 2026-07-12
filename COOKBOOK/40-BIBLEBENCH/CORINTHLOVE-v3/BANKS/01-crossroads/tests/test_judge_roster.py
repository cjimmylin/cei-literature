from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path

import jsonschema
import pytest

from scorers.judge_roster import FrozenJudgeRoster, canonical_roster_sha256


BANK = Path(__file__).resolve().parents[1]
SCHEMA = BANK / "sidecar" / "judge_roster.schema.json"
FIXTURE = BANK / "sidecar" / "judge_roster.mock.json"


def load_fixture() -> dict:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def test_mock_roster_matches_schema_and_is_not_a_measurement():
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    document = load_fixture()
    jsonschema.Draft202012Validator(schema).validate(document)
    assert document["provenance"] == "harness validation, NOT a measurement"
    assert document["human_validation_status"] == (
        "not performed; actual roster is an external dependency"
    )
    roster = FrozenJudgeRoster.from_document(
        document, expected_sha256=canonical_roster_sha256(document)
    )
    assert roster.provenance == "harness validation, NOT a measurement"


def test_roster_hash_freezes_every_identity_binding_and_rejects_mutation():
    document = load_fixture()
    digest = canonical_roster_sha256(document)
    roster = FrozenJudgeRoster.from_document(document, expected_sha256=digest)
    judge_id = document["judges"][0]["judge_id"]
    original = roster.lookup(judge_id, required_role="raw")

    document["judges"][0]["family"] = "rebound-family"
    with pytest.raises(ValueError, match="roster hash mismatch"):
        FrozenJudgeRoster.from_document(document, expected_sha256=digest)
    assert roster.lookup(judge_id, required_role="raw") == original
    with pytest.raises(AttributeError, match="immutable"):
        roster.sha256 = "f" * 64
    with pytest.raises(TypeError):
        roster.lookup(judge_id, required_role="raw")["family"] = "rebound"


def test_rebound_duplicate_unknown_and_wrong_role_identities_fail_loud():
    document = load_fixture()
    rebound = deepcopy(document["judges"][0])
    rebound["family"] = "rebound-family"
    document["judges"].append(rebound)
    with pytest.raises(ValueError, match="rebound or duplicate JUDGE"):
        FrozenJudgeRoster.from_document(
            document, expected_sha256=canonical_roster_sha256(document)
        )

    valid = load_fixture()
    roster = FrozenJudgeRoster.from_document(
        valid, expected_sha256=canonical_roster_sha256(valid)
    )
    with pytest.raises(ValueError, match="unknown JUDGE"):
        roster.lookup(
            "JUDGE-123e4567-e89b-42d3-a456-426614174999",
            required_role="raw",
        )
    adjudicator = next(
        row for row in valid["judges"] if row["role"] == "adjudicator"
    )
    with pytest.raises(ValueError, match="role mismatch"):
        roster.lookup(adjudicator["judge_id"], required_role="raw")


def test_model_and_human_identity_bindings_are_mutually_exclusive():
    document = load_fixture()
    row = document["judges"][0]
    row["human_identity_class"] = "credentialed-human-panel-v1"
    with pytest.raises(ValueError, match="exactly one identity binding"):
        FrozenJudgeRoster.from_document(
            document, expected_sha256=canonical_roster_sha256(document)
        )
