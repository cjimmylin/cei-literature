from dataclasses import FrozenInstanceError
import hashlib

import pytest
from biblebench_pilot.contracts import canonical_json_bytes, canonical_sha256
from biblebench_pilot.contracts import (
    ArtifactEnvelope,
    CoreRef,
    EpisodeRef,
    SandboxEvent,
)


MAX_JSON_DEPTH = 128


def _nested_list(depth):
    value = 0
    for _ in range(depth):
        value = [value]
    return value


def test_canonical_json_is_order_independent():
    left = {"b": 2, "a": [1, True, None]}
    right = {"a": [1, True, None], "b": 2}
    assert canonical_json_bytes(left) == canonical_json_bytes(right)
    assert canonical_sha256(left) == canonical_sha256(right)


@pytest.mark.parametrize("value", [float("nan"), float("inf"), (1, 2)])
def test_canonical_json_rejects_non_json_values(value):
    with pytest.raises(ValueError, match="strict canonical JSON"):
        canonical_json_bytes({"value": value})


@pytest.mark.parametrize(
    ("boundary", "field", "replacement"),
    [
        (
            CoreRef(
                core_id="core-1",
                module="fruitbench",
                source_paths=("Galatians 5:22-23",),
                construct="patience",
                evidence_type="action",
                behavioral_attribution="applicable",
            ),
            "core_id",
            "core-2",
        ),
        (
            EpisodeRef(
                episode_id="episode-1",
                core_id="core-1",
                split="public_calibration",
                stratum="common_life",
                mode="judgment",
                transform_ids=("transform-1",),
                capability_twin_id=None,
                actor_payload_sha256="abc123",
            ),
            "episode_id",
            "episode-2",
        ),
        (
            SandboxEvent(
                sequence=1,
                action="send",
                actor="agent",
                target="recipient",
                payload={"message": "hello"},
            ),
            "sequence",
            2,
        ),
        (
            ArtifactEnvelope(
                artifact_type="sandbox_event",
                version="1.0",
                created_at_utc="2026-07-11T00:00:00Z",
                payload={"sequence": 1},
                payload_sha256="def456",
            ),
            "version",
            "2.0",
        ),
    ],
)
def test_boundary_dataclass_fields_are_frozen(boundary, field, replacement):
    with pytest.raises(FrozenInstanceError):
        setattr(boundary, field, replacement)


def test_canonical_sha256_matches_independently_reconstructed_payload():
    original = {"episode": {"id": "episode-1", "scores": [1, 2, 3]}}
    reconstructed = {
        "episode": {
            "scores": [1, 2, 3],
            "id": "episode-1",
        }
    }

    assert original is not reconstructed
    assert original["episode"] is not reconstructed["episode"]
    assert canonical_sha256(original) == canonical_sha256(reconstructed)
    expected_bytes = b'{"episode":{"id":"episode-1","scores":[1,2,3]}}'
    assert canonical_sha256(original) == hashlib.sha256(expected_bytes).hexdigest()


def test_canonical_json_rejects_non_string_dict_keys():
    with pytest.raises(ValueError, match="strict canonical JSON"):
        canonical_json_bytes({1: "not a string key"})


def test_canonical_json_distinguishes_bool_and_int_and_accepts_nested_json():
    value = {
        "boolean": True,
        "integer": 1,
        "nested": [{"false": False, "nothing": None, "number": 2.5}],
    }

    assert canonical_json_bytes(value) == (
        b'{"boolean":true,"integer":1,'
        b'"nested":[{"false":false,"nothing":null,"number":2.5}]}'
    )
    assert canonical_json_bytes({"value": True}) != canonical_json_bytes({"value": 1})


def test_canonical_json_rejects_self_referential_list():
    value = []
    value.append(value)

    with pytest.raises(ValueError, match="strict canonical JSON"):
        canonical_json_bytes(value)


def test_canonical_json_rejects_self_referential_dict():
    value = {}
    value["self"] = value

    with pytest.raises(ValueError, match="strict canonical JSON"):
        canonical_json_bytes(value)


def test_canonical_json_accepts_maximum_nesting_depth():
    assert canonical_json_bytes(_nested_list(MAX_JSON_DEPTH))


def test_canonical_json_rejects_one_beyond_maximum_nesting_depth():
    with pytest.raises(ValueError, match="strict canonical JSON"):
        canonical_json_bytes(_nested_list(MAX_JSON_DEPTH + 1))


def test_canonical_json_accepts_repeated_non_cyclic_aliases():
    shared = ["same"]

    assert canonical_json_bytes([shared, shared]) == b'[["same"],["same"]]'


@pytest.mark.parametrize(
    "value",
    [
        {"value": "\ud800"},
        {"\udfff": "value"},
    ],
)
def test_canonical_json_rejects_lone_unicode_surrogates(value):
    with pytest.raises(ValueError, match="strict canonical JSON"):
        canonical_json_bytes(value)


def test_canonical_json_accepts_valid_unicode():
    assert canonical_json_bytes({"emoji": "🍇", "text": "é"}) == (
        '{"emoji":"🍇","text":"é"}'.encode("utf-8")
    )
