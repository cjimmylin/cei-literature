"""Contract tests for durable per-stream hash-chained checkpoints."""

import json
import os

import pytest


def api():
    import TENCOMMANDMENTS.harness.openrouter as openrouter

    return openrouter


def test_append_load_and_verify_canonical_hash_chained_stream(tmp_path):
    module = api()
    path = tmp_path / "model-a.jsonl"

    first = module.append_checkpoint(
        path,
        "model-a",
        {"schedule_index": 0, "status": "complete"},
        expected_head_sha256=module.ZERO_CHECKPOINT_SHA256,
    )
    second = module.append_checkpoint(
        path,
        "model-a",
        {"schedule_index": 1, "status": "parked"},
        expected_head_sha256=first.checkpoint_sha256,
    )
    snapshot = module.load_checkpoint_stream(path, "model-a")

    assert snapshot.head_sha256 == second.checkpoint_sha256
    assert snapshot.next_index == 2
    assert snapshot.payloads == (
        {"schedule_index": 0, "status": "complete"},
        {"schedule_index": 1, "status": "parked"},
    )
    assert snapshot.records[1].previous_checkpoint_sha256 == first.checkpoint_sha256
    assert module.verify_checkpoint_stream(path, "model-a") == snapshot
    raw_lines = path.read_bytes().splitlines()
    assert all(
        line
        == module.canonical_json_bytes(json.loads(line.decode("utf-8")))
        for line in raw_lines
    )


def test_stale_expected_head_fails_without_appending(tmp_path):
    module = api()
    path = tmp_path / "stream.jsonl"
    module.append_checkpoint(path, "stream", {"value": 1})
    before = path.read_bytes()

    with pytest.raises(module.CheckpointError, match="head"):
        module.append_checkpoint(
            path,
            "stream",
            {"value": 2},
            expected_head_sha256=module.ZERO_CHECKPOINT_SHA256,
        )
    assert path.read_bytes() == before


def test_load_rejects_tampering_truncation_and_wrong_stream(tmp_path):
    module = api()
    path = tmp_path / "stream.jsonl"
    module.append_checkpoint(path, "stream", {"value": "original"})
    original = path.read_bytes()

    path.write_bytes(original.replace(b"original", b"tampered"))
    with pytest.raises(module.CheckpointError, match="hash|chain"):
        module.load_checkpoint_stream(path, "stream")

    path.write_bytes(original[:-1])
    with pytest.raises(module.CheckpointError, match="incomplete|newline"):
        module.load_checkpoint_stream(path, "stream")

    path.write_bytes(original)
    with pytest.raises(module.CheckpointError, match="stream"):
        module.load_checkpoint_stream(path, "different-stream")


def test_missing_stream_loads_as_empty_and_payload_must_be_object(tmp_path):
    module = api()
    snapshot = module.load_checkpoint_stream(tmp_path / "missing.jsonl", "stream")

    assert snapshot.records == ()
    assert snapshot.head_sha256 == module.ZERO_CHECKPOINT_SHA256
    assert snapshot.next_index == 0
    with pytest.raises(module.CheckpointError, match="payload"):
        module.append_checkpoint(tmp_path / "bad.jsonl", "stream", [1, 2])


def test_checkpoint_target_rejects_symlink_and_hard_link_aliases(tmp_path):
    module = api()
    path = tmp_path / "stream.jsonl"
    module.append_checkpoint(path, "stream", {"value": 1})
    symlink = tmp_path / "symlink.jsonl"
    hardlink = tmp_path / "hardlink.jsonl"
    symlink.symlink_to(path)
    os.link(str(path), str(hardlink))

    with pytest.raises(module.CheckpointError, match="unsafe|unreadable"):
        module.load_checkpoint_stream(symlink, "stream")
    with pytest.raises(module.CheckpointError, match="unsafe|unreadable"):
        module.load_checkpoint_stream(hardlink, "stream")
