"""Source-contract fixtures for canonical, orthogonal hashes."""
from __future__ import annotations

import copy

import pytest

from canonical import (
    CanonicalSnapshot,
    CanonicalizationError,
    assignment_hash,
    build_packet,
    content_hash,
    evidence_hash,
    rubric_hash,
    source_hash,
    verify_packet,
)
from transforms import mask_identity_spans


VIEW = {
    "parent_evidence_hash": None,
    "task": {"prompt": "Choose."},
    "response": {"text": "Proceed.", "events": []},
    "transform": None,
}
ASSIGNMENT = {
    "assignment_id": "opaque-1",
    "judge_ids": ["j-1", "j-2"],
    "order": 0,
}
RUBRIC = {
    "rubric_id": "pole",
    "rubric_version": "v1",
    "criteria": {"gold": "does good", "neutral": "other"},
}


def test_hand_computed_canonical_hash_fixtures() -> None:
    assert source_hash("alpha\n") == (
        "b6a98d9ce9a2d9149288fa3df42d377c3e42737afdcdaf714e33c0a100b51060"
    )
    assert content_hash({"b": 2, "a": ["é", True, None]}) == (
        "cd65b255fd4e15fcccfb74ed4bc0ddc9ac4e7437aa195404ba9d0ec02552ebee"
    )
    assert evidence_hash(VIEW) == (
        "9076000557c527e814611737020b94faeb0ac7352456571bc63f3a7f75e196bb"
    )
    assert assignment_hash(ASSIGNMENT) == (
        "f49346dec0c800b8f7d5137799396427c4e5838e83f71d17bdc122eedd4ed959"
    )
    assert rubric_hash(RUBRIC) == (
        "8be7786f20979f420167835e4b1b064ee2adf599f48a251b5420b0e8a07d9b72"
    )


def test_hash_functions_reject_their_self_referential_field() -> None:
    fixtures = (
        (content_hash, {"content_hash": "0" * 64}),
        (evidence_hash, {**VIEW, "evidence_hash": "0" * 64}),
        (assignment_hash, {**ASSIGNMENT, "assignment_hash": "0" * 64}),
        (rubric_hash, {**RUBRIC, "rubric_hash": "0" * 64}),
    )
    for function, value in fixtures:
        with pytest.raises(CanonicalizationError, match="self-referential"):
            function(value)


def test_snapshot_is_immune_to_mutation_of_input_or_serialized_copy() -> None:
    source = {"items": [1, 2]}
    snapshot = CanonicalSnapshot.capture(source)
    source["items"].append(3)
    serialized = snapshot.to_object()
    serialized["items"].append(4)

    assert snapshot.to_object() == {"items": [1, 2]}
    assert snapshot.sha256 == content_hash({"items": [1, 2]})


def test_packet_hashes_are_orthogonal_and_verified_fail_closed() -> None:
    baseline = build_packet(VIEW, ASSIGNMENT, RUBRIC)
    assignment_changed = build_packet(
        VIEW, {**ASSIGNMENT, "judge_ids": ["j-1", "j-3"]}, RUBRIC
    )
    rubric_changed = build_packet(
        VIEW, ASSIGNMENT, {**RUBRIC, "rubric_version": "v2"}
    )
    evidence_changed = build_packet(
        {**VIEW, "response": {"text": "Wait.", "events": []}}, ASSIGNMENT, RUBRIC
    )
    identity_parent = {
        **VIEW,
        "response": {"text": "Model-X", "events": []},
    }
    transformed_view = mask_identity_spans(
        identity_parent,
        [
            {
                "path": "response.text",
                "source_start": 0,
                "source_end": 7,
                "replacement": "<MODEL_ID>",
            }
        ],
        transform_version="mask-v1",
        identity_tokens={"<MODEL_ID>": ["Model-X"]},
    )
    transform_changed = build_packet(
        transformed_view,
        ASSIGNMENT,
        RUBRIC,
        parent_view=identity_parent,
        identity_tokens={"<MODEL_ID>": ["Model-X"]},
    )

    assert assignment_changed["evidence_hash"] == baseline["evidence_hash"]
    assert rubric_changed["evidence_hash"] == baseline["evidence_hash"]
    assert assignment_changed["packet_hash"] != baseline["packet_hash"]
    assert rubric_changed["packet_hash"] != baseline["packet_hash"]
    assert evidence_changed["evidence_hash"] != baseline["evidence_hash"]
    assert transform_changed["evidence_hash"] != baseline["evidence_hash"]
    assert evidence_changed["packet_hash"] != baseline["packet_hash"]
    assert transform_changed["packet_hash"] != baseline["packet_hash"]
    assert verify_packet(baseline, ASSIGNMENT) is True

    tampered = copy.deepcopy(baseline)
    tampered["view"]["response"]["text"] = "Tampered."
    with pytest.raises(CanonicalizationError, match="evidence_hash"):
        verify_packet(tampered, ASSIGNMENT)


def test_non_json_values_and_non_finite_numbers_fail_canonicalization() -> None:
    with pytest.raises(CanonicalizationError):
        content_hash({"bad": {1, 2}})
    with pytest.raises(CanonicalizationError):
        content_hash({"bad": float("nan")})
