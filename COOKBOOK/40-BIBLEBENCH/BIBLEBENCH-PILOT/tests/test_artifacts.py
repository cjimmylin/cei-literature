from concurrent.futures import ThreadPoolExecutor
import os
from pathlib import Path
import stat

import pytest
import biblebench_pilot.artifacts as artifacts
from biblebench_pilot.artifacts import (
    ArtifactStore,
    assert_actor_envelope_safe,
    assert_actor_payload_safe,
    assert_judge_envelope_safe,
    validate_artifact_tree,
)


def test_store_writes_canonical_json_with_newline(tmp_path: Path) -> None:
    store = ArtifactStore(tmp_path)

    target = store.write("runs/result.json", {"z": 2, "a": "visible"})

    assert target == tmp_path / "runs/result.json"
    assert target.read_bytes() == b'{"a":"visible","z":2}\n'


@pytest.mark.parametrize(
    "relative",
    [
        "",
        "/absolute.json",
        "//server/share.json",
        "C:relative.json",
        "C:/rooted.json",
        "folder\\child.json",
        "folder//child.json",
        "folder/./child.json",
        "folder/../child.json",
        "folder/",
        "bad\x00name.json",
        "bad\ud800name.json",
    ],
)
def test_store_rejects_ambiguous_or_unsafe_paths(
    tmp_path: Path, relative: str
) -> None:
    with pytest.raises(ValueError, match="unsafe artifact path") as caught:
        ArtifactStore(tmp_path).write(relative, {"visible": True})

    if relative:
        assert relative not in str(caught.value)


def test_store_fails_closed_when_native_no_replace_is_unavailable(
    tmp_path: Path, monkeypatch
) -> None:
    monkeypatch.setattr(artifacts.sys, "platform", "unsupported")

    with pytest.raises(OSError, match="publication failed"):
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    assert not (tmp_path / "result.json").exists()
    assert len(list(tmp_path.glob(".artifact-*.tmp"))) == 1


def test_store_rejects_nonexistent_file_and_symlink_roots(tmp_path: Path) -> None:
    file_root = tmp_path / "file-root"
    file_root.write_text("not a directory", encoding="utf-8")
    symlink_root = tmp_path / "linked-root"
    os.symlink(tmp_path, symlink_root)

    for root in (tmp_path / "missing", file_root, symlink_root):
        with pytest.raises(ValueError, match="real directory"):
            ArtifactStore(root)


def test_store_creates_private_real_parent_directories(tmp_path: Path) -> None:
    ArtifactStore(tmp_path).write("one/two/artifact.json", {"ok": True})

    for parent in (tmp_path / "one", tmp_path / "one/two"):
        parent_stat = parent.lstat()
        assert stat.S_ISDIR(parent_stat.st_mode)
        assert stat.S_IMODE(parent_stat.st_mode) == 0o700


def test_store_syncs_new_directory_and_its_parent(tmp_path: Path, monkeypatch) -> None:
    original_fsync = artifacts.os.fsync
    synced_directories = []

    def recording_sync(descriptor):
        descriptor_stat = os.fstat(descriptor)
        if stat.S_ISDIR(descriptor_stat.st_mode):
            synced_directories.append((descriptor_stat.st_dev, descriptor_stat.st_ino))
        return original_fsync(descriptor)

    monkeypatch.setattr(artifacts.os, "fsync", recording_sync)

    ArtifactStore(tmp_path).write("new/result.json", {"visible": True})

    root_stat = tmp_path.stat()
    child_stat = (tmp_path / "new").stat()
    assert (root_stat.st_dev, root_stat.st_ino) in synced_directories
    assert (child_stat.st_dev, child_stat.st_ino) in synced_directories


def test_store_syncs_parent_when_another_creator_wins_mkdir_race(
    tmp_path: Path, monkeypatch
) -> None:
    original_mkdir = artifacts.os.mkdir
    original_fsync = artifacts.os.fsync
    synced_directories = []

    def racing_mkdir(path, *args, **kwargs):
        original_mkdir(path, *args, **kwargs)
        raise FileExistsError("simulated competing creator")

    def recording_sync(descriptor):
        descriptor_stat = os.fstat(descriptor)
        if stat.S_ISDIR(descriptor_stat.st_mode):
            synced_directories.append((descriptor_stat.st_dev, descriptor_stat.st_ino))
        return original_fsync(descriptor)

    monkeypatch.setattr(artifacts.os, "mkdir", racing_mkdir)
    monkeypatch.setattr(artifacts.os, "fsync", recording_sync)

    ArtifactStore(tmp_path).write("contended/result.json", {"visible": True})

    root_stat = tmp_path.stat()
    assert (root_stat.st_dev, root_stat.st_ino) in synced_directories


def test_store_rejects_symlink_and_non_directory_parents(tmp_path: Path) -> None:
    real_parent = tmp_path / "real"
    real_parent.mkdir()
    os.symlink(real_parent, tmp_path / "linked")
    (tmp_path / "plain").write_text("file", encoding="utf-8")

    for relative in ("linked/result.json", "plain/result.json"):
        with pytest.raises(ValueError, match="unsafe artifact path"):
            ArtifactStore(tmp_path).write(relative, {"ok": True})


def test_store_rejects_target_symlink(tmp_path: Path) -> None:
    outside = tmp_path / "outside.json"
    outside.write_text("unchanged", encoding="utf-8")
    os.symlink(outside, tmp_path / "result.json")

    with pytest.raises(ValueError, match="unsafe artifact path"):
        ArtifactStore(tmp_path).write("result.json", {"changed": True})

    assert outside.read_text(encoding="utf-8") == "unchanged"


def test_store_refuses_to_overwrite_existing_target(tmp_path: Path) -> None:
    target = tmp_path / "result.json"
    target.write_bytes(b"original\n")

    with pytest.raises(FileExistsError, match="already exists"):
        ArtifactStore(tmp_path).write("result.json", {"changed": True})

    assert target.read_bytes() == b"original\n"


def test_store_serializes_payload_exactly_once(tmp_path: Path, monkeypatch) -> None:
    calls = 0
    original = artifacts.canonical_json_bytes

    def counting_serializer(payload):
        nonlocal calls
        calls += 1
        return original(payload)

    monkeypatch.setattr(artifacts, "canonical_json_bytes", counting_serializer)

    ArtifactStore(tmp_path).write("result.json", {"visible": [1, 2]})

    assert calls == 1


def test_concurrent_writers_publish_exactly_one_artifact(tmp_path: Path) -> None:
    store = ArtifactStore(tmp_path)

    def attempt(number: int):
        try:
            return store.write("shared.json", {"writer": number})
        except FileExistsError:
            return None

    with ThreadPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(attempt, range(16)))

    assert sum(result is not None for result in results) == 1
    assert (tmp_path / "shared.json").read_bytes().endswith(b"}\n")


def test_store_handles_short_writes_without_reserializing(
    tmp_path: Path, monkeypatch
) -> None:
    original_write = artifacts.os.write
    calls = 0

    def short_write(descriptor, data):
        nonlocal calls
        calls += 1
        return original_write(descriptor, data[:3])

    monkeypatch.setattr(artifacts.os, "write", short_write)

    target = ArtifactStore(tmp_path).write(
        "short.json", {"message": "a longer visible value"}
    )

    assert calls > 1
    assert target.read_bytes() == b'{"message":"a longer visible value"}\n'


def test_target_is_absent_until_native_publication(tmp_path: Path, monkeypatch) -> None:
    target = tmp_path / "result.json"
    original_publish = artifacts._native_publish_noreplace
    observed = []

    def checking_publish(parent_fd, temporary, target_name):
        observed.append(target.exists())
        return original_publish(parent_fd, temporary, target_name)

    monkeypatch.setattr(artifacts, "_native_publish_noreplace", checking_publish)

    ArtifactStore(tmp_path).write("result.json", {"visible": True})

    assert observed == [False]
    assert target.is_file()


def test_failure_before_file_sync_leaves_no_target_and_retains_temp(
    tmp_path: Path, monkeypatch
) -> None:
    def failing_write(descriptor, data):
        raise OSError("do-not-echo-this")

    monkeypatch.setattr(artifacts.os, "write", failing_write)

    with pytest.raises(OSError) as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    assert "do-not-echo-this" not in str(caught.value)
    assert not (tmp_path / "result.json").exists()
    assert len(list(tmp_path.glob(".artifact-*.tmp"))) == 1


def test_failure_after_file_sync_leaves_no_target_and_retains_temp(
    tmp_path: Path, monkeypatch
) -> None:
    def failing_publish(parent_fd, temporary, target_name):
        raise OSError("do-not-echo-this")

    monkeypatch.setattr(artifacts, "_native_publish_noreplace", failing_publish)

    with pytest.raises(OSError) as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    assert "do-not-echo-this" not in str(caught.value)
    assert not (tmp_path / "result.json").exists()
    assert len(list(tmp_path.glob(".artifact-*.tmp"))) == 1


def test_directory_sync_failure_is_distinct_and_target_remains_published(
    tmp_path: Path, monkeypatch
) -> None:
    original_fsync = artifacts.os.fsync
    calls = 0

    def fail_second_sync(descriptor):
        nonlocal calls
        calls += 1
        if calls == 2:
            raise OSError("do-not-echo-this")
        return original_fsync(descriptor)

    monkeypatch.setattr(artifacts.os, "fsync", fail_second_sync)

    with pytest.raises(artifacts.ArtifactDurabilityError) as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    assert "published" in str(caught.value)
    assert "do-not-echo-this" not in str(caught.value)
    assert (tmp_path / "result.json").read_bytes() == b'{"visible":true}\n'


def test_final_verification_failure_is_redacted_after_publication(
    tmp_path: Path, monkeypatch
) -> None:
    original_stat = artifacts.os.stat
    target_stats = 0

    def fail_final_stat(path, *args, **kwargs):
        nonlocal target_stats
        if path == "result.json" and kwargs.get("dir_fd") is not None:
            target_stats += 1
            if target_stats == 2:
                raise OSError("do-not-echo-this")
        return original_stat(path, *args, **kwargs)

    monkeypatch.setattr(artifacts.os, "stat", fail_final_stat)

    with pytest.raises(ValueError, match="verification failed") as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    assert "do-not-echo-this" not in str(caught.value)
    assert (tmp_path / "result.json").is_file()


def test_serialization_errors_are_concise_and_create_nothing(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="strict canonical JSON") as caught:
        ArtifactStore(tmp_path).write("result.json", {"invalid": float("nan")})

    assert len(str(caught.value)) < 100
    assert not (tmp_path / "result.json").exists()
    assert list(tmp_path.iterdir()) == []


def test_final_artifact_is_private_regular_and_unaliased(tmp_path: Path) -> None:
    target = ArtifactStore(tmp_path).write("result.json", {"visible": True})

    target_stat = target.lstat()
    assert stat.S_ISREG(target_stat.st_mode)
    assert stat.S_IMODE(target_stat.st_mode) == 0o600
    assert target_stat.st_nlink == 1


def test_root_descriptor_is_closed_when_identity_check_faults(
    tmp_path: Path, monkeypatch
) -> None:
    original_open = artifacts.os.open
    original_close = artifacts.os.close
    opened = []
    closed = []

    def recording_open(*args, **kwargs):
        descriptor = original_open(*args, **kwargs)
        opened.append(descriptor)
        return descriptor

    def recording_close(descriptor):
        closed.append(descriptor)
        return original_close(descriptor)

    def failing_fstat(descriptor):
        raise OSError("injected")

    monkeypatch.setattr(artifacts.os, "open", recording_open)
    monkeypatch.setattr(artifacts.os, "close", recording_close)
    monkeypatch.setattr(artifacts.os, "fstat", failing_fstat)

    with pytest.raises(ValueError, match="real directory"):
        ArtifactStore(tmp_path)

    assert opened[-1] in closed


def test_child_descriptor_is_closed_when_recheck_faults(
    tmp_path: Path, monkeypatch
) -> None:
    original_open = artifacts.os.open
    original_close = artifacts.os.close
    original_fstat = artifacts.os.fstat
    child_descriptors = []
    closed = []

    def recording_open(path, *args, **kwargs):
        descriptor = original_open(path, *args, **kwargs)
        if path == "child":
            child_descriptors.append(descriptor)
        return descriptor

    def recording_close(descriptor):
        closed.append(descriptor)
        return original_close(descriptor)

    def selective_fstat(descriptor):
        if descriptor in child_descriptors:
            raise OSError("injected")
        return original_fstat(descriptor)

    monkeypatch.setattr(artifacts.os, "open", recording_open)
    monkeypatch.setattr(artifacts.os, "close", recording_close)
    monkeypatch.setattr(artifacts.os, "fstat", selective_fstat)

    with pytest.raises(ValueError, match="unsafe artifact path"):
        ArtifactStore(tmp_path).write("child/result.json", {"visible": True})

    assert child_descriptors[-1] in closed


def test_parent_descriptor_is_closed_when_temp_name_generation_faults(
    tmp_path: Path, monkeypatch
) -> None:
    original_dup = artifacts.os.dup
    original_close = artifacts.os.close
    duplicated = []
    closed = []

    def recording_dup(descriptor):
        duplicate = original_dup(descriptor)
        duplicated.append(duplicate)
        return duplicate

    def recording_close(descriptor):
        closed.append(descriptor)
        return original_close(descriptor)

    def failing_uuid():
        raise RuntimeError("injected")

    monkeypatch.setattr(artifacts.os, "dup", recording_dup)
    monkeypatch.setattr(artifacts.os, "close", recording_close)
    monkeypatch.setattr(artifacts.uuid, "uuid4", failing_uuid)

    with pytest.raises(RuntimeError, match="injected"):
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    assert duplicated[-1] in closed


def test_validate_artifact_tree_accepts_real_directories_and_regular_files(
    tmp_path: Path,
) -> None:
    root = tmp_path / "artifacts"
    root.mkdir()
    ArtifactStore(root).write("nested/result.json", {"visible": True})
    before = sorted(str(path.relative_to(root)) for path in root.rglob("*"))

    assert validate_artifact_tree(root) is None

    after = sorted(str(path.relative_to(root)) for path in root.rglob("*"))
    assert after == before


@pytest.mark.parametrize("link_directory", [False, True])
def test_validate_artifact_tree_rejects_symlinks(
    tmp_path: Path, link_directory: bool
) -> None:
    root = tmp_path / "artifacts"
    root.mkdir()
    destination = tmp_path / "destination"
    if link_directory:
        destination.mkdir()
    else:
        destination.write_text("outside", encoding="utf-8")
    os.symlink(destination, root / "unsafe-link")

    with pytest.raises(ValueError, match="unsafe artifact tree"):
        validate_artifact_tree(root)


def test_validate_artifact_tree_rejects_hardlinks_and_inode_aliases(
    tmp_path: Path,
) -> None:
    root = tmp_path / "artifacts"
    root.mkdir()
    first = root / "first.json"
    first.write_text("same inode", encoding="utf-8")
    os.link(first, root / "second.json")

    with pytest.raises(ValueError, match="unsafe artifact tree"):
        validate_artifact_tree(root)


def test_validate_artifact_tree_rejects_external_hardlink(tmp_path: Path) -> None:
    root = tmp_path / "artifacts"
    root.mkdir()
    outside = tmp_path / "outside.json"
    outside.write_text("same inode", encoding="utf-8")
    os.link(outside, root / "alias.json")

    with pytest.raises(ValueError, match="unsafe artifact tree"):
        validate_artifact_tree(root)


def test_validate_artifact_tree_rejects_special_files(tmp_path: Path) -> None:
    root = tmp_path / "artifacts"
    root.mkdir()
    os.mkfifo(root / "pipe")

    with pytest.raises(ValueError, match="unsafe artifact tree"):
        validate_artifact_tree(root)


def test_validate_artifact_tree_rejects_symlink_root(tmp_path: Path) -> None:
    root = tmp_path / "artifacts"
    root.mkdir()
    linked_root = tmp_path / "linked-artifacts"
    os.symlink(root, linked_root)

    with pytest.raises(ValueError, match="unsafe artifact tree"):
        validate_artifact_tree(linked_root)


@pytest.mark.parametrize(
    "forbidden_key",
    [
        "ground_truth",
        "Ground-Truth",
        "judge_id",
        "judge.id",
        "canary",
        "api_key",
        "actorModel",
        "model_identity",
        "expected/label",
        "private-template",
    ],
)
def test_actor_payload_rejects_nested_forbidden_keys_without_echo(
    forbidden_key: str,
) -> None:
    payload = {"turns": [{"content": {forbidden_key: "do-not-echo-this"}}]}

    with pytest.raises(ValueError, match="model-visible payload") as caught:
        assert_actor_payload_safe(payload)

    assert forbidden_key not in str(caught.value)
    assert "do-not-echo-this" not in str(caught.value)
    assert len(str(caught.value)) < 100


@pytest.mark.parametrize(
    "forbidden_value",
    [
        "contains GROUND.TRUTH metadata",
        "Bearer abcdef123456",
        "sk-example123456789",
        "OPENROUTER_API_KEY=dummy-value",
        "Authorization: Basic abcdef",
        "PATH=/bin\nHOME=/tmp\nUSER=runner",
        "${PRIVATE_TEMPLATE}",
    ],
)
def test_actor_payload_rejects_nested_forbidden_values_without_echo(
    forbidden_value: str,
) -> None:
    with pytest.raises(ValueError, match="model-visible payload") as caught:
        assert_actor_payload_safe({"turns": [{"content": forbidden_value}]})

    assert forbidden_value not in str(caught.value)
    assert len(str(caught.value)) < 100


def test_actor_payload_allows_visible_content_and_explicit_token_count() -> None:
    payload = {
        "turns": [
            {
                "role": "user",
                "content": "Please send the public update.",
                "public_id": "episode-public-17",
            }
        ],
        "tool_contracts": {"send_update": {"token_count": 12}},
    }

    assert assert_actor_payload_safe(payload) is None


def test_actor_payload_rejects_cycles_and_extreme_depth() -> None:
    cyclic = []
    cyclic.append(cyclic)
    deep = []
    cursor = deep
    for _ in range(140):
        child = []
        cursor.append(child)
        cursor = child

    for payload in (cyclic, deep):
        with pytest.raises(ValueError, match="model-visible payload"):
            assert_actor_payload_safe(payload)


def test_actor_payload_rejects_invalid_unicode_keys_and_single_env_assignment() -> None:
    for payload in ({"bad\ud800key": "value"}, {"content": "PATH=/usr/bin"}):
        with pytest.raises(ValueError, match="model-visible payload"):
            assert_actor_payload_safe(payload)


def test_actor_envelope_accepts_only_visible_turns_and_tool_contracts() -> None:
    envelope = {
        "turns": [{"role": "user", "content": "A visible request"}],
        "tool_contracts": {"send_update": {"fields": ["message"]}},
    }

    assert assert_actor_envelope_safe(envelope) is None


@pytest.mark.parametrize(
    "envelope",
    [
        {"turns": [], "tool_contracts": {}, "episode_token": "opaque"},
        {"turns": []},
        {"turns": {}, "tool_contracts": {}},
        {"turns": [], "tool_contracts": []},
        {"turns": [{"rubric_version": "rv1"}], "tool_contracts": {}},
        {"turns": [{"gold": "label-a"}], "tool_contracts": {}},
        {"turns": [{"model_identity": "actor-a"}], "tool_contracts": {}},
    ],
)
def test_actor_envelope_rejects_private_or_wrong_shapes(envelope) -> None:
    with pytest.raises(ValueError, match="model-visible payload"):
        assert_actor_envelope_safe(envelope)


def test_judge_envelope_allows_opaque_token_rubric_and_events() -> None:
    envelope = {
        "episode_token": "opaque-episode-17",
        "rubric_version": "rubric-v3",
        "events": [{"sequence": 1, "action": "visible_action"}],
    }

    assert assert_judge_envelope_safe(envelope) is None


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("episode_token", "actor_model-gpt-5"),
        ("episode_token", "provider-route-control"),
        ("rubric_version", "private-condition-control"),
        ("rubric_version", "expected-label-gold"),
    ],
)
def test_judge_envelope_rejects_private_terms_in_opaque_fields(
    field: str, value: str
) -> None:
    envelope = {
        "episode_token": "opaque-episode-17",
        "rubric_version": "rubric-v3",
        "events": [],
    }
    envelope[field] = value

    with pytest.raises(ValueError, match="model-visible payload") as caught:
        assert_judge_envelope_safe(envelope)

    assert value not in str(caught.value)


@pytest.mark.parametrize(
    "forbidden_field",
    [
        "actor_model",
        "actor-id",
        "provider",
        "route",
        "cue",
        "condition",
        "expected_label",
        "ground_truth",
        "gold",
        "private_payload",
    ],
)
def test_judge_envelope_rejects_actor_identity_and_private_cues(
    forbidden_field: str,
) -> None:
    envelope = {
        "episode_token": "opaque-episode-17",
        "rubric_version": "rubric-v3",
        "events": [{forbidden_field: "do-not-echo-this"}],
    }

    with pytest.raises(ValueError, match="model-visible payload") as caught:
        assert_judge_envelope_safe(envelope)

    assert forbidden_field not in str(caught.value)
    assert "do-not-echo-this" not in str(caught.value)


@pytest.mark.parametrize(
    "envelope",
    [
        {"episode_token": "opaque", "rubric_version": "rv1", "events": [], "x": 1},
        {"episode_token": "", "rubric_version": "rv1", "events": []},
        {"episode_token": "opaque", "rubric_version": " ", "events": []},
        {"episode_token": "opaque", "rubric_version": "rv1", "events": {}},
    ],
)
def test_judge_envelope_rejects_wrong_shapes(envelope) -> None:
    with pytest.raises(ValueError, match="model-visible payload"):
        assert_judge_envelope_safe(envelope)


def test_artifact_implementation_has_no_destructive_or_overwriting_calls() -> None:
    source = Path(artifacts.__file__).read_text(encoding="utf-8")
    forbidden = (
        "os." + "rename(",
        "os." + "replace(",
        "Path." + "rename(",
        "un" + "link(",
        "re" + "move(",
        "rmt" + "ree(",
    )

    assert not any(pattern in source for pattern in forbidden)
