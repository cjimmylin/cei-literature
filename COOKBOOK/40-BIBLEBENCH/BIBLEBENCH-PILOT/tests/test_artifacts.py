from concurrent.futures import ThreadPoolExecutor
import errno
import os
from pathlib import Path
import stat
import traceback

import pytest
import biblebench_pilot.artifacts as artifacts
from biblebench_pilot.artifacts import (
    ArtifactStore,
    assert_actor_envelope_safe,
    assert_actor_payload_safe,
    assert_judge_envelope_safe,
    validate_artifact_tree,
)


def _artifact_temps(root: Path) -> list[Path]:
    legacy = list(root.rglob(".artifact-*.tmp"))
    staged = [
        path / "payload"
        for path in root.rglob(".artifact-stage-*")
        if (path / "payload").is_file()
    ]
    return legacy + staged


def _assert_concise_redacted(error: BaseException) -> None:
    assert "do-not-echo-this" not in str(error)
    assert len(str(error)) < 160


def _assert_traceback_redacted(error: BaseException) -> None:
    rendered = "".join(traceback.format_exception(error))
    assert "do-not-echo-this" not in rendered


def _changed_stat(
    original: os.stat_result,
    *,
    mode: int | None = None,
    inode_delta: int = 0,
    links: int | None = None,
    uid: int | None = None,
) -> os.stat_result:
    values = list(original)
    if mode is not None:
        values[stat.ST_MODE] = mode
    if inode_delta:
        values[stat.ST_INO] += inode_delta
    if links is not None:
        values[stat.ST_NLINK] = links
    if uid is not None:
        values[stat.ST_UID] = uid
    return os.stat_result(values)


def test_artifact_module_exports_only_required_module_apis() -> None:
    assert artifacts.__all__ == (
        "ArtifactStore",
        "assert_actor_payload_safe",
        "assert_actor_envelope_safe",
        "assert_judge_envelope_safe",
        "validate_artifact_tree",
    )
    assert "write" not in artifacts.__all__
    assert callable(ArtifactStore.write)


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

    with pytest.raises(OSError, match="publication failed") as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "result.json").exists()
    assert len(_artifact_temps(tmp_path)) == 1


def test_store_rejects_nonexistent_file_and_symlink_roots(tmp_path: Path) -> None:
    file_root = tmp_path / "file-root"
    file_root.write_text("not a directory", encoding="utf-8")
    symlink_root = tmp_path / "linked-root"
    os.symlink(tmp_path, symlink_root)

    for root in (tmp_path / "missing", file_root, symlink_root):
        with pytest.raises(ValueError, match="real directory"):
            ArtifactStore(root)


@pytest.mark.parametrize("mode", [0o777, 0o1777], ids=["world-writable", "sticky"])
def test_store_rejects_untrusted_root_before_staging(
    tmp_path: Path, mode: int
) -> None:
    root = tmp_path / "artifacts"
    root.mkdir(mode=0o700)
    os.chmod(root, mode)

    with pytest.raises(ValueError, match="trusted directory"):
        ArtifactStore(root)

    assert not (root / "result.json").exists()
    assert list(root.glob(".artifact-stage-*")) == []


@pytest.mark.parametrize("mode", [0o777, 0o1777], ids=["world-writable", "sticky"])
def test_store_rejects_untrusted_existing_parent_before_staging(
    tmp_path: Path, mode: int
) -> None:
    root = tmp_path / "artifacts"
    root.mkdir(mode=0o700)
    parent = root / "existing"
    parent.mkdir(mode=0o700)
    os.chmod(parent, mode)

    with pytest.raises(ValueError, match="trusted directory"):
        ArtifactStore(root).write("existing/result.json", {"visible": True})

    assert not (parent / "result.json").exists()
    assert list(parent.glob(".artifact-stage-*")) == []


def test_store_rejects_foreign_owner_descriptor_before_staging(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "artifacts"
    root.mkdir(mode=0o700)
    original_fstat = artifacts.os.fstat

    def foreign_directory_fstat(descriptor):
        result = original_fstat(descriptor)
        if stat.S_ISDIR(result.st_mode):
            return _changed_stat(result, uid=os.geteuid() + 1)
        return result

    monkeypatch.setattr(artifacts.os, "fstat", foreign_directory_fstat)

    with pytest.raises(ValueError, match="trusted directory"):
        ArtifactStore(root)

    assert list(root.glob(".artifact-stage-*")) == []


def test_store_allows_owned_non_writable_parent_modes(tmp_path: Path) -> None:
    root = tmp_path / "artifacts"
    root.mkdir(mode=0o700)
    parent = root / "existing"
    parent.mkdir(mode=0o700)
    os.chmod(root, 0o755)
    os.chmod(parent, 0o750)

    target = ArtifactStore(root).write("existing/result.json", {"visible": True})

    assert target.read_bytes() == b'{"visible":true}\n'


def test_parent_is_revalidated_immediately_before_staging_mkdir(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "artifacts"
    root.mkdir(mode=0o700)
    parent = root / "existing"
    parent.mkdir(mode=0o700)
    original_absence_check = artifacts._assert_target_absent

    def make_parent_untrusted(parent_fd, target):
        original_absence_check(parent_fd, target)
        os.chmod(parent, 0o777)

    monkeypatch.setattr(artifacts, "_assert_target_absent", make_parent_untrusted)

    with pytest.raises(ValueError, match="trusted directory"):
        ArtifactStore(root).write("existing/result.json", {"visible": True})

    assert not (parent / "result.json").exists()
    assert list(parent.glob(".artifact-stage-*")) == []


def test_parent_is_revalidated_immediately_before_publication(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "artifacts"
    root.mkdir(mode=0o700)
    parent = root / "existing"
    parent.mkdir(mode=0o700)
    original_write_all = artifacts._write_all

    def write_then_make_parent_untrusted(descriptor, data):
        original_write_all(descriptor, data)
        os.chmod(parent, 0o777)

    monkeypatch.setattr(artifacts, "_write_all", write_then_make_parent_untrusted)

    with pytest.raises(ValueError, match="trusted directory"):
        ArtifactStore(root).write("existing/result.json", {"visible": True})

    assert not (parent / "result.json").exists()
    assert len(_artifact_temps(parent)) == 1


@pytest.mark.parametrize("replacement", ["symlink", "world-writable-directory"])
def test_store_rejects_physical_staging_namespace_replacement(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    replacement: str,
) -> None:
    root = tmp_path / "artifacts"
    root.mkdir(mode=0o700)
    attacker = tmp_path / "attacker"
    attacker.mkdir(mode=0o700)
    (attacker / "payload").write_bytes(b'{"attacker":true}\n')
    original_mkdir_private = artifacts._mkdir_private

    def replacing_staging_directory(component, parent_fd):
        original_mkdir_private(component, parent_fd)
        artifacts._native_publish_noreplace(
            parent_fd,
            component,
            parent_fd,
            f"{component}.retained",
        )
        if replacement == "symlink":
            os.symlink(attacker, component, dir_fd=parent_fd)
            return
        os.mkdir(component, mode=0o700, dir_fd=parent_fd)
        stage_fd = os.open(
            component,
            os.O_RDONLY | getattr(os, "O_DIRECTORY", 0),
            dir_fd=parent_fd,
        )
        try:
            payload_fd = os.open(
                "payload",
                os.O_WRONLY | os.O_CREAT | os.O_EXCL,
                0o600,
                dir_fd=stage_fd,
            )
            try:
                os.write(payload_fd, b'{"attacker":true}\n')
            finally:
                os.close(payload_fd)
            os.fchmod(stage_fd, 0o777)
        finally:
            os.close(stage_fd)

    monkeypatch.setattr(
        artifacts,
        "_mkdir_private",
        replacing_staging_directory,
    )

    with pytest.raises(ValueError, match="unsafe artifact staging directory"):
        ArtifactStore(root).write("result.json", {"visible": True})

    assert not (root / "result.json").exists()
    if replacement == "symlink":
        assert (attacker / "payload").read_bytes() == b'{"attacker":true}\n'
    else:
        stage = next(root.glob(".artifact-stage-*"))
        if stage.name.endswith(".retained"):
            stage = next(
                path
                for path in root.glob(".artifact-stage-*")
                if not path.name.endswith(".retained")
            )
        assert (stage / "payload").read_bytes() == b'{"attacker":true}\n'


def test_store_creates_private_real_parent_directories(tmp_path: Path) -> None:
    ArtifactStore(tmp_path).write("one/two/artifact.json", {"ok": True})

    for parent in (tmp_path / "one", tmp_path / "one/two"):
        parent_stat = parent.lstat()
        assert stat.S_ISDIR(parent_stat.st_mode)
        assert stat.S_IMODE(parent_stat.st_mode) == 0o700


def test_store_enforces_root_target_mode_under_hostile_umask(tmp_path: Path) -> None:
    previous_umask = os.umask(0o777)
    try:
        target = ArtifactStore(tmp_path).write("result.json", {"visible": True})
    finally:
        os.umask(previous_umask)

    assert stat.S_IMODE(target.lstat().st_mode) == 0o600


def test_store_enforces_nested_modes_under_hostile_umask(tmp_path: Path) -> None:
    previous_umask = os.umask(0o777)
    try:
        target = ArtifactStore(tmp_path).write(
            "one/two/result.json", {"visible": True}
        )
    finally:
        os.umask(previous_umask)

    assert stat.S_IMODE((tmp_path / "one").lstat().st_mode) == 0o700
    assert stat.S_IMODE((tmp_path / "one/two").lstat().st_mode) == 0o700
    assert stat.S_IMODE(target.lstat().st_mode) == 0o600


def test_directory_creation_window_keeps_unrelated_files_private(
    tmp_path: Path, monkeypatch
) -> None:
    original_mkdir = artifacts.os.mkdir
    unrelated = tmp_path / "unrelated.txt"

    def concurrent_creation(path, *args, **kwargs):
        if not unrelated.exists():
            descriptor = os.open(
                unrelated, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o666
            )
            os.close(descriptor)
        return original_mkdir(path, *args, **kwargs)

    monkeypatch.setattr(artifacts.os, "mkdir", concurrent_creation)
    previous_umask = os.umask(0o777)
    try:
        target = ArtifactStore(tmp_path).write(
            "new/result.json", {"visible": True}
        )
    finally:
        os.umask(previous_umask)

    assert stat.S_IMODE(unrelated.lstat().st_mode) == 0o600
    assert stat.S_IMODE((tmp_path / "new").lstat().st_mode) == 0o700
    assert stat.S_IMODE(target.lstat().st_mode) == 0o600


def test_umask_set_failure_is_redacted_without_changing_process_umask(
    tmp_path: Path, monkeypatch
) -> None:
    calls = []

    def failing_umask(mode):
        calls.append(mode)
        raise OSError("do-not-echo-this")

    monkeypatch.setattr(artifacts, "_set_process_umask", failing_umask)
    original_umask = os.umask(0o027)
    os.umask(original_umask)
    try:
        with pytest.raises(ValueError, match="unsafe artifact path") as caught:
            ArtifactStore(tmp_path).write("new/result.json", {"visible": True})
    finally:
        observed_umask = os.umask(original_umask)

    assert observed_umask == original_umask
    assert calls == [0o077]
    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "new/result.json").exists()
    assert _artifact_temps(tmp_path) == []


def test_umask_restore_failure_is_redacted_and_attempted_without_global_change(
    tmp_path: Path, monkeypatch
) -> None:
    calls = []

    def simulated_umask(mode):
        calls.append(mode)
        if len(calls) == 1:
            return 0o027
        raise OSError("do-not-echo-this")

    monkeypatch.setattr(artifacts, "_set_process_umask", simulated_umask)
    original_umask = os.umask(0o027)
    os.umask(original_umask)
    try:
        with pytest.raises(ValueError, match="unsafe artifact path") as caught:
            ArtifactStore(tmp_path).write("new/result.json", {"visible": True})
    finally:
        observed_umask = os.umask(original_umask)

    assert observed_umask == original_umask
    assert calls == [0o077, 0o027]
    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "new/result.json").exists()
    assert _artifact_temps(tmp_path) == []


def test_store_does_not_chmod_existing_parent(tmp_path: Path) -> None:
    existing = tmp_path / "existing"
    existing.mkdir(mode=0o755)
    os.chmod(existing, 0o755)
    previous_umask = os.umask(0o777)
    try:
        target = ArtifactStore(tmp_path).write(
            "existing/result.json", {"visible": True}
        )
    finally:
        os.umask(previous_umask)

    assert stat.S_IMODE(existing.lstat().st_mode) == 0o755
    assert stat.S_IMODE(target.lstat().st_mode) == 0o600


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
        if path == "contended":
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


def test_parent_mkdir_failure_is_redacted_before_staging(
    tmp_path: Path, monkeypatch
) -> None:
    def failing_mkdir(path, *args, **kwargs):
        raise OSError("do-not-echo-this")

    monkeypatch.setattr(artifacts.os, "mkdir", failing_mkdir)

    with pytest.raises(ValueError, match="unsafe artifact path") as caught:
        ArtifactStore(tmp_path).write("new/result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "new/result.json").exists()
    assert _artifact_temps(tmp_path) == []


def test_initial_parent_dup_failure_is_redacted_before_staging(
    tmp_path: Path, monkeypatch
) -> None:
    def failing_dup(descriptor):
        raise OSError(errno.EMFILE, "do-not-echo-this")

    monkeypatch.setattr(artifacts.os, "dup", failing_dup)

    with pytest.raises(ValueError, match="unsafe artifact path") as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "result.json").exists()
    assert _artifact_temps(tmp_path) == []


@pytest.mark.parametrize("fault", ["error", "identity"], ids=["error", "identity"])
def test_outer_root_parent_fstat_failure_is_rejected_before_staging(
    tmp_path: Path, monkeypatch, fault: str
) -> None:
    original_dup = artifacts.os.dup
    original_fstat = artifacts.os.fstat
    parent_descriptors = set()

    def recording_dup(descriptor):
        duplicate = original_dup(descriptor)
        parent_descriptors.add(duplicate)
        return duplicate

    def failing_parent_fstat(descriptor):
        result = original_fstat(descriptor)
        if descriptor in parent_descriptors:
            if fault == "error":
                raise OSError(errno.EIO, "do-not-echo-this")
            return _changed_stat(result, inode_delta=1)
        return result

    monkeypatch.setattr(artifacts.os, "dup", recording_dup)
    monkeypatch.setattr(artifacts.os, "fstat", failing_parent_fstat)

    with pytest.raises(ValueError, match="unsafe artifact path") as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "result.json").exists()
    assert _artifact_temps(tmp_path) == []


def test_new_parent_never_uses_path_chmod(
    tmp_path: Path, monkeypatch
) -> None:
    def failing_chmod(path, mode, *args, **kwargs):
        raise AssertionError("path chmod must not be used")

    monkeypatch.setattr(artifacts.os, "chmod", failing_chmod)

    target = ArtifactStore(tmp_path).write("new/result.json", {"visible": True})

    assert target.is_file()
    assert stat.S_IMODE((tmp_path / "new").lstat().st_mode) == 0o700
    assert _artifact_temps(tmp_path) == []


def test_new_parent_metadata_failure_is_redacted_before_staging(
    tmp_path: Path, monkeypatch
) -> None:
    original_stat = artifacts.os.stat

    def failing_stat(path, *args, **kwargs):
        if path == "new" and kwargs.get("dir_fd") is not None:
            raise OSError("do-not-echo-this")
        return original_stat(path, *args, **kwargs)

    monkeypatch.setattr(artifacts.os, "stat", failing_stat)

    with pytest.raises(ValueError, match="unsafe artifact path") as caught:
        ArtifactStore(tmp_path).write("new/result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "new/result.json").exists()
    assert _artifact_temps(tmp_path) == []


def test_new_parent_second_open_failure_is_redacted_before_staging(
    tmp_path: Path, monkeypatch
) -> None:
    original_open = artifacts.os.open
    component_opens = 0

    def failing_second_open(path, *args, **kwargs):
        nonlocal component_opens
        if path == "new":
            component_opens += 1
            if component_opens == 2:
                raise OSError("do-not-echo-this")
        return original_open(path, *args, **kwargs)

    monkeypatch.setattr(artifacts.os, "open", failing_second_open)

    with pytest.raises(ValueError, match="unsafe artifact path") as caught:
        ArtifactStore(tmp_path).write("new/result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "new/result.json").exists()
    assert _artifact_temps(tmp_path) == []


def test_new_parent_fd_chmod_failure_is_redacted_before_staging(
    tmp_path: Path, monkeypatch
) -> None:
    original_fchmod = artifacts.os.fchmod
    original_fstat = artifacts.os.fstat

    def failing_directory_fchmod(descriptor, mode):
        if stat.S_ISDIR(original_fstat(descriptor).st_mode):
            raise OSError("do-not-echo-this")
        return original_fchmod(descriptor, mode)

    monkeypatch.setattr(artifacts.os, "fchmod", failing_directory_fchmod)

    with pytest.raises(ValueError, match="unsafe artifact path") as caught:
        ArtifactStore(tmp_path).write("new/result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "new/result.json").exists()
    assert _artifact_temps(tmp_path) == []


def test_new_parent_inode_swap_is_rejected_before_staging(
    tmp_path: Path, monkeypatch
) -> None:
    original_open = artifacts.os.open
    original_fstat = artifacts.os.fstat
    child_descriptors = set()

    def recording_open(path, *args, **kwargs):
        descriptor = original_open(path, *args, **kwargs)
        if path == "new":
            child_descriptors.add(descriptor)
        return descriptor

    def swapped_fstat(descriptor):
        result = original_fstat(descriptor)
        if descriptor in child_descriptors:
            return _changed_stat(result, inode_delta=1)
        return result

    monkeypatch.setattr(artifacts.os, "open", recording_open)
    monkeypatch.setattr(artifacts.os, "fstat", swapped_fstat)

    with pytest.raises(ValueError, match="unsafe artifact path") as caught:
        ArtifactStore(tmp_path).write("new/result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "new/result.json").exists()
    assert _artifact_temps(tmp_path) == []


def test_new_parent_swap_is_rejected_without_chmodding_existing_inode(
    tmp_path: Path, monkeypatch
) -> None:
    existing = tmp_path / "existing"
    existing.mkdir(mode=0o755)
    os.chmod(existing, 0o755)
    original_chmod = artifacts.os.chmod
    original_stat = artifacts.os.stat
    component_stats = 0

    def attacker_swap_chmod(path, mode, *args, **kwargs):
        original_chmod(existing, mode)

    def swapped_component_stat(path, *args, **kwargs):
        nonlocal component_stats
        if path == "new" and kwargs.get("dir_fd") is not None:
            component_stats += 1
            if component_stats >= 2:
                return existing.stat()
        return original_stat(path, *args, **kwargs)

    monkeypatch.setattr(artifacts.os, "chmod", attacker_swap_chmod)
    monkeypatch.setattr(artifacts.os, "stat", swapped_component_stat)

    with pytest.raises(ValueError, match="unsafe artifact path"):
        ArtifactStore(tmp_path).write("new/result.json", {"visible": True})

    assert stat.S_IMODE(existing.lstat().st_mode) == 0o755
    assert not (tmp_path / "new/result.json").exists()
    assert _artifact_temps(tmp_path) == []


@pytest.mark.parametrize("sync_call", [1, 2], ids=["child", "parent"])
def test_new_parent_directory_sync_failure_occurs_before_staging(
    tmp_path: Path, monkeypatch, sync_call: int
) -> None:
    original_fsync = artifacts.os.fsync
    calls = 0

    def failing_selected_sync(descriptor):
        nonlocal calls
        calls += 1
        if calls == sync_call:
            raise OSError("do-not-echo-this")
        return original_fsync(descriptor)

    monkeypatch.setattr(artifacts.os, "fsync", failing_selected_sync)

    with pytest.raises(ValueError, match="unsafe artifact path") as caught:
        ArtifactStore(tmp_path).write("new/result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "new/result.json").exists()
    assert _artifact_temps(tmp_path) == []


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
    assert _artifact_temps(tmp_path) == []


def test_unexpected_target_stat_error_is_distinct_and_redacted(
    tmp_path: Path, monkeypatch
) -> None:
    original_stat = artifacts.os.stat

    def failing_target_stat(path, *args, **kwargs):
        if path == "result.json" and kwargs.get("dir_fd") is not None:
            raise OSError(errno.EACCES, "do-not-echo-this")
        return original_stat(path, *args, **kwargs)

    monkeypatch.setattr(artifacts.os, "stat", failing_target_stat)

    with pytest.raises(ValueError, match="unsafe artifact path") as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "result.json").exists()
    assert _artifact_temps(tmp_path) == []


def test_store_refuses_to_overwrite_existing_target(tmp_path: Path) -> None:
    target = tmp_path / "result.json"
    target.write_bytes(b"original\n")

    with pytest.raises(FileExistsError, match="already exists"):
        ArtifactStore(tmp_path).write("result.json", {"changed": True})

    assert target.read_bytes() == b"original\n"
    assert _artifact_temps(tmp_path) == []


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
    original_open = artifacts.os.open
    observed = []
    staged_fd = None

    def recording_open(path, *args, **kwargs):
        nonlocal staged_fd
        descriptor = original_open(path, *args, **kwargs)
        if path == "payload":
            staged_fd = descriptor
        return descriptor

    def checking_publish(source_dir_fd, temporary, destination_dir_fd, target_name):
        observed.append(target.exists())
        assert source_dir_fd != destination_dir_fd
        assert stat.S_IMODE(os.fstat(source_dir_fd).st_mode) == 0o700
        result = original_publish(
            source_dir_fd, temporary, destination_dir_fd, target_name
        )
        staged = os.fstat(staged_fd)
        canonical = os.stat(
            target_name,
            dir_fd=destination_dir_fd,
            follow_symlinks=False,
        )
        assert (staged.st_dev, staged.st_ino) == (
            canonical.st_dev,
            canonical.st_ino,
        )
        return result

    monkeypatch.setattr(artifacts.os, "open", recording_open)
    monkeypatch.setattr(artifacts, "_native_publish_noreplace", checking_publish)

    ArtifactStore(tmp_path).write("result.json", {"visible": True})

    assert observed == [False]
    assert target.is_file()


def test_public_temp_namespace_poisoning_cannot_change_canonical_target(
    tmp_path: Path, monkeypatch
) -> None:
    original_publish = artifacts._native_publish_noreplace
    attacker_inode = None

    def poisoning_publish(*args):
        nonlocal attacker_inode
        if len(args) == 3:
            destination_fd, source_name, target_name = args
            source_fd = destination_fd
        else:
            source_fd, source_name, destination_fd, target_name = args
        attacker_fd = os.open(
            source_name,
            os.O_WRONLY | (os.O_TRUNC if source_fd == destination_fd else os.O_CREAT | os.O_EXCL),
            0o600,
            dir_fd=destination_fd,
        )
        try:
            os.write(attacker_fd, b'{"attacker":true}\n')
            attacker_inode = os.fstat(attacker_fd).st_ino
        finally:
            os.close(attacker_fd)
        return original_publish(*args)

    monkeypatch.setattr(artifacts, "_native_publish_noreplace", poisoning_publish)

    target = ArtifactStore(tmp_path).write("result.json", {"visible": True})

    assert target.read_bytes() == b'{"visible":true}\n'
    assert target.lstat().st_ino != attacker_inode


def test_success_retains_private_exact_mode_staging_directory(tmp_path: Path) -> None:
    ArtifactStore(tmp_path).write("result.json", {"visible": True})

    staging_directories = [
        path for path in tmp_path.iterdir() if path.name.startswith(".artifact-stage-")
    ]
    assert len(staging_directories) == 1
    staging = staging_directories[0]
    assert stat.S_ISDIR(staging.lstat().st_mode)
    assert stat.S_IMODE(staging.lstat().st_mode) == 0o700
    assert list(staging.iterdir()) == []


def test_write_failure_leaves_no_target_and_retains_temp(
    tmp_path: Path, monkeypatch
) -> None:
    def failing_write(descriptor, data):
        raise OSError("do-not-echo-this")

    monkeypatch.setattr(artifacts.os, "write", failing_write)

    with pytest.raises(OSError) as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "result.json").exists()
    assert len(_artifact_temps(tmp_path)) == 1


def test_zero_progress_write_is_redacted_and_retains_temp(
    tmp_path: Path, monkeypatch
) -> None:
    def zero_write(descriptor, data):
        return 0

    monkeypatch.setattr(artifacts.os, "write", zero_write)

    with pytest.raises(OSError, match="artifact staging failed") as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "result.json").exists()
    assert len(_artifact_temps(tmp_path)) == 1


def test_temp_open_failure_leaves_no_target_and_no_temp(
    tmp_path: Path, monkeypatch
) -> None:
    original_open = artifacts.os.open

    def failing_temp_open(path, *args, **kwargs):
        if path == "payload":
            raise OSError(errno.EMFILE, "do-not-echo-this")
        return original_open(path, *args, **kwargs)

    monkeypatch.setattr(artifacts.os, "open", failing_temp_open)

    with pytest.raises(OSError, match="artifact staging failed") as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "result.json").exists()
    assert _artifact_temps(tmp_path) == []


def test_file_sync_failure_leaves_no_target_and_retains_temp(
    tmp_path: Path, monkeypatch
) -> None:
    original_fsync = artifacts.os.fsync
    original_fstat = artifacts.os.fstat

    def failing_file_sync(descriptor):
        if stat.S_ISREG(original_fstat(descriptor).st_mode):
            raise OSError(errno.EIO, "do-not-echo-this")
        return original_fsync(descriptor)

    monkeypatch.setattr(artifacts.os, "fsync", failing_file_sync)

    with pytest.raises(OSError, match="artifact staging failed") as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "result.json").exists()
    assert len(_artifact_temps(tmp_path)) == 1


def test_temp_fchmod_failure_leaves_no_target_and_retains_temp(
    tmp_path: Path, monkeypatch
) -> None:
    original_fchmod = artifacts.os.fchmod
    original_fstat = artifacts.os.fstat

    def failing_fchmod(descriptor, mode):
        if stat.S_ISREG(original_fstat(descriptor).st_mode):
            raise OSError(errno.EPERM, "do-not-echo-this")
        return original_fchmod(descriptor, mode)

    monkeypatch.setattr(artifacts.os, "fchmod", failing_fchmod)

    with pytest.raises(OSError, match="artifact staging failed") as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "result.json").exists()
    assert len(_artifact_temps(tmp_path)) == 1


def test_temp_fstat_failure_leaves_no_target_and_retains_temp(
    tmp_path: Path, monkeypatch
) -> None:
    original_open = artifacts.os.open
    original_fstat = artifacts.os.fstat
    temp_descriptors = set()

    def recording_open(path, *args, **kwargs):
        descriptor = original_open(path, *args, **kwargs)
        if path == "payload":
            temp_descriptors.add(descriptor)
        return descriptor

    def failing_temp_fstat(descriptor):
        if descriptor in temp_descriptors:
            raise OSError(errno.EIO, "do-not-echo-this")
        return original_fstat(descriptor)

    monkeypatch.setattr(artifacts.os, "open", recording_open)
    monkeypatch.setattr(artifacts.os, "fstat", failing_temp_fstat)

    with pytest.raises(OSError, match="artifact staging failed") as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "result.json").exists()
    assert len(_artifact_temps(tmp_path)) == 1


@pytest.mark.parametrize(
    ("mode", "links"),
    [
        (stat.S_IFDIR | 0o700, 1),
        (stat.S_IFREG | 0o640, 1),
        (stat.S_IFREG | 0o600, 2),
    ],
    ids=["not-regular", "wrong-mode", "hardlinked"],
)
def test_temp_metadata_failure_leaves_no_target_and_retains_temp(
    tmp_path: Path, monkeypatch, mode: int, links: int
) -> None:
    original_open = artifacts.os.open
    original_fstat = artifacts.os.fstat
    temp_descriptors = set()
    injected = False

    def recording_open(path, *args, **kwargs):
        descriptor = original_open(path, *args, **kwargs)
        if path == "payload":
            temp_descriptors.add(descriptor)
        return descriptor

    def invalid_temp_fstat(descriptor):
        nonlocal injected
        result = original_fstat(descriptor)
        if descriptor in temp_descriptors and not injected:
            injected = True
            return _changed_stat(result, mode=mode, links=links)
        return result

    monkeypatch.setattr(artifacts.os, "open", recording_open)
    monkeypatch.setattr(artifacts.os, "fstat", invalid_temp_fstat)

    with pytest.raises(ValueError, match="unsafe artifact temporary file") as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "result.json").exists()
    assert len(_artifact_temps(tmp_path)) == 1


def test_temp_close_error_does_not_retry_an_already_closed_descriptor(
    tmp_path: Path, monkeypatch
) -> None:
    original_open = artifacts.os.open
    original_close = artifacts.os.close
    temp_descriptors = set()
    temp_close_calls = 0
    reused_fd = None

    def recording_open(path, *args, **kwargs):
        descriptor = original_open(path, *args, **kwargs)
        if path == "payload":
            temp_descriptors.add(descriptor)
        return descriptor

    def failing_first_temp_close(descriptor):
        nonlocal temp_close_calls, reused_fd
        if descriptor in temp_descriptors:
            temp_close_calls += 1
            if temp_close_calls == 1:
                original_close(descriptor)
                reused_fd = os.open(tmp_path / "result.json", os.O_RDONLY)
                assert reused_fd == descriptor
                raise OSError(errno.EIO, "do-not-echo-this")
            raise AssertionError("already-closed descriptor was retried")
        return original_close(descriptor)

    monkeypatch.setattr(artifacts.os, "open", recording_open)
    monkeypatch.setattr(artifacts.os, "close", failing_first_temp_close)

    with pytest.raises(artifacts.ArtifactDurabilityError, match="published") as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    _assert_traceback_redacted(caught.value)
    assert temp_close_calls == 1
    try:
        reopened = os.fstat(reused_fd)
        target = (tmp_path / "result.json").stat()
        assert (reopened.st_dev, reopened.st_ino) == (target.st_dev, target.st_ino)
    finally:
        original_close(reused_fd)
    assert (tmp_path / "result.json").read_bytes() == b'{"visible":true}\n'
    assert _artifact_temps(tmp_path) == []


def test_temp_close_failure_is_never_retried_after_close_was_called(
    tmp_path: Path, monkeypatch
) -> None:
    original_open = artifacts.os.open
    original_close = artifacts.os.close
    temp_descriptors = set()
    temp_close_calls = 0

    def recording_open(path, *args, **kwargs):
        descriptor = original_open(path, *args, **kwargs)
        if path == "payload":
            temp_descriptors.add(descriptor)
        return descriptor

    def failing_then_closing_temp(descriptor):
        nonlocal temp_close_calls
        if descriptor in temp_descriptors:
            temp_close_calls += 1
            raise OSError(errno.EIO, "do-not-echo-this")
        return original_close(descriptor)

    monkeypatch.setattr(artifacts.os, "open", recording_open)
    monkeypatch.setattr(artifacts.os, "close", failing_then_closing_temp)

    with pytest.raises(artifacts.ArtifactDurabilityError, match="published") as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert temp_close_calls == 1
    for descriptor in temp_descriptors:
        try:
            original_close(descriptor)
        except OSError:
            pass
    assert (tmp_path / "result.json").read_bytes() == b'{"visible":true}\n'
    assert _artifact_temps(tmp_path) == []


def test_failure_after_file_sync_leaves_no_target_and_retains_temp(
    tmp_path: Path, monkeypatch
) -> None:
    def failing_publish(*args):
        raise OSError("do-not-echo-this")

    monkeypatch.setattr(artifacts, "_native_publish_noreplace", failing_publish)

    with pytest.raises(OSError) as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "result.json").exists()
    assert len(_artifact_temps(tmp_path)) == 1


def test_staging_directory_fault_traceback_is_redacted_and_directory_retained(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    original_stat = artifacts.os.stat

    def failing_stage_stat(path, *args, **kwargs):
        if type(path) is str and path.startswith(".artifact-stage-"):
            raise OSError(errno.EIO, "do-not-echo-this")
        return original_stat(path, *args, **kwargs)

    monkeypatch.setattr(artifacts.os, "stat", failing_stage_stat)

    with pytest.raises(OSError, match="staging failed") as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    _assert_traceback_redacted(caught.value)
    assert not (tmp_path / "result.json").exists()
    assert len(list(tmp_path.glob(".artifact-stage-*"))) == 1


def test_post_publish_staged_fstat_fault_has_explicit_published_state(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    original_open = artifacts.os.open
    original_fstat = artifacts.os.fstat
    staged_fd = None
    staged_fstats = 0

    def recording_open(path, *args, **kwargs):
        nonlocal staged_fd
        descriptor = original_open(path, *args, **kwargs)
        if path == "payload":
            staged_fd = descriptor
        return descriptor

    def failing_post_publish_fstat(descriptor):
        nonlocal staged_fstats
        if descriptor == staged_fd:
            staged_fstats += 1
            if staged_fstats == 3:
                raise OSError(errno.EIO, "do-not-echo-this")
        return original_fstat(descriptor)

    monkeypatch.setattr(artifacts.os, "open", recording_open)
    monkeypatch.setattr(artifacts.os, "fstat", failing_post_publish_fstat)

    with pytest.raises(artifacts.ArtifactDurabilityError, match="published") as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    _assert_traceback_redacted(caught.value)
    assert (tmp_path / "result.json").read_bytes() == b'{"visible":true}\n'
    assert _artifact_temps(tmp_path) == []


def test_native_publish_eexist_preserves_competing_target_and_temp(
    tmp_path: Path, monkeypatch
) -> None:
    target = tmp_path / "result.json"

    def competing_publish(*args):
        target.write_bytes(b"competing-writer\n")
        raise FileExistsError("artifact target already exists")

    monkeypatch.setattr(artifacts, "_native_publish_noreplace", competing_publish)

    with pytest.raises(FileExistsError, match="already exists") as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert target.read_bytes() == b"competing-writer\n"
    assert len(_artifact_temps(tmp_path)) == 1


def test_native_publish_non_eexist_errno_leaves_target_absent_and_temp(
    tmp_path: Path, monkeypatch
) -> None:
    def failing_publish(*args):
        raise OSError(errno.EACCES, "do-not-echo-this")

    monkeypatch.setattr(artifacts, "_native_publish_noreplace", failing_publish)

    with pytest.raises(OSError, match="publication failed") as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    assert caught.value.errno == errno.EACCES
    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "result.json").exists()
    assert len(_artifact_temps(tmp_path)) == 1


def test_native_publisher_cdll_load_failure_is_redacted_and_retains_temp(
    tmp_path: Path, monkeypatch
) -> None:
    def failing_cdll(*args, **kwargs):
        raise OSError(errno.ENOEXEC, "do-not-echo-this")

    monkeypatch.setattr(artifacts.ctypes, "CDLL", failing_cdll)

    with pytest.raises(OSError, match="publication failed") as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "result.json").exists()
    assert len(_artifact_temps(tmp_path)) == 1


def test_native_publisher_missing_symbol_is_redacted_and_retains_temp(
    tmp_path: Path, monkeypatch
) -> None:
    class LibraryWithoutPublisher:
        pass

    monkeypatch.setattr(
        artifacts.ctypes,
        "CDLL",
        lambda *args, **kwargs: LibraryWithoutPublisher(),
    )

    with pytest.raises(OSError, match="publication failed") as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "result.json").exists()
    assert len(_artifact_temps(tmp_path)) == 1


def test_native_publisher_unexpected_errno_is_redacted_and_retains_temp(
    tmp_path: Path, monkeypatch
) -> None:
    class FailingOperation:
        argtypes = None
        restype = None

        def __call__(self, *args):
            return -1

    class FailingLibrary:
        renameatx_np = FailingOperation()

    monkeypatch.setattr(
        artifacts.ctypes,
        "CDLL",
        lambda *args, **kwargs: FailingLibrary(),
    )
    monkeypatch.setattr(artifacts.ctypes, "get_errno", lambda: errno.EACCES)

    with pytest.raises(OSError, match="publication failed") as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    assert caught.value.errno == errno.EACCES
    _assert_concise_redacted(caught.value)
    assert not (tmp_path / "result.json").exists()
    assert len(_artifact_temps(tmp_path)) == 1


def test_native_errno_mapper_distinguishes_exists_from_other_errors() -> None:
    with pytest.raises(FileExistsError, match="already exists"):
        artifacts._raise_publish_error(errno.EEXIST)

    with pytest.raises(OSError, match="publication failed") as caught:
        artifacts._raise_publish_error(errno.EIO)

    assert caught.value.errno == errno.EIO


@pytest.mark.parametrize(
    ("platform", "symbol", "flag"),
    [
        ("darwin", "renameatx_np", 0x00000004),
        ("linux", "renameat2", 1),
    ],
)
@pytest.mark.parametrize("error_number", [None, errno.EEXIST, errno.EACCES])
def test_native_publish_uses_distinct_source_and_destination_dirfds(
    monkeypatch: pytest.MonkeyPatch,
    platform: str,
    symbol: str,
    flag: int,
    error_number: int | None,
) -> None:
    calls = []

    class Operation:
        argtypes = None
        restype = None

        def __call__(self, *args):
            calls.append(args)
            return -1 if error_number is not None else 0

    library = type("Library", (), {symbol: Operation()})()
    monkeypatch.setattr(artifacts.sys, "platform", platform)
    monkeypatch.setattr(artifacts.ctypes, "CDLL", lambda *args, **kwargs: library)
    monkeypatch.setattr(
        artifacts.ctypes,
        "get_errno",
        lambda: error_number if error_number is not None else 0,
    )

    if error_number == errno.EEXIST:
        with pytest.raises(FileExistsError):
            artifacts._native_publish_noreplace(17, "payload", 29, "result.json")
    elif error_number is not None:
        with pytest.raises(OSError) as caught:
            artifacts._native_publish_noreplace(17, "payload", 29, "result.json")
        assert caught.value.errno == error_number
    else:
        assert (
            artifacts._native_publish_noreplace(17, "payload", 29, "result.json")
            is None
        )

    assert calls == [(17, b"payload", 29, b"result.json", flag)]


def test_post_publish_parent_sync_failure_is_distinct_with_visible_target(
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
    _assert_concise_redacted(caught.value)
    assert (tmp_path / "result.json").read_bytes() == b'{"visible":true}\n'
    assert _artifact_temps(tmp_path) == []


def test_post_publish_child_sync_failure_is_distinct_with_visible_target(
    tmp_path: Path, monkeypatch
) -> None:
    target = tmp_path / "child/result.json"
    original_fsync = artifacts.os.fsync

    def fail_visible_target_directory_sync(descriptor):
        if target.exists() and stat.S_ISDIR(os.fstat(descriptor).st_mode):
            raise OSError(errno.EIO, "do-not-echo-this")
        return original_fsync(descriptor)

    monkeypatch.setattr(artifacts.os, "fsync", fail_visible_target_directory_sync)

    with pytest.raises(artifacts.ArtifactDurabilityError) as caught:
        ArtifactStore(tmp_path).write("child/result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert "published" in str(caught.value)
    assert target.read_bytes() == b'{"visible":true}\n'
    assert _artifact_temps(tmp_path) == []


def test_post_publish_parent_close_failure_is_distinct_with_visible_target(
    tmp_path: Path, monkeypatch
) -> None:
    original_dup = artifacts.os.dup
    original_close = artifacts.os.close
    parent_descriptors = set()

    def recording_dup(descriptor):
        duplicate = original_dup(descriptor)
        parent_descriptors.add(duplicate)
        return duplicate

    def failing_parent_close(descriptor):
        if descriptor in parent_descriptors:
            parent_descriptors.discard(descriptor)
            original_close(descriptor)
            raise OSError(errno.EIO, "do-not-echo-this")
        return original_close(descriptor)

    monkeypatch.setattr(artifacts.os, "dup", recording_dup)
    monkeypatch.setattr(artifacts.os, "close", failing_parent_close)

    with pytest.raises(artifacts.ArtifactDurabilityError) as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert "published" in str(caught.value)
    assert (tmp_path / "result.json").read_bytes() == b'{"visible":true}\n'
    assert _artifact_temps(tmp_path) == []


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

    _assert_concise_redacted(caught.value)
    assert (tmp_path / "result.json").is_file()
    assert _artifact_temps(tmp_path) == []


@pytest.mark.parametrize(
    ("mode", "links"),
    [
        (stat.S_IFDIR | 0o700, 1),
        (stat.S_IFREG | 0o640, 1),
        (stat.S_IFREG | 0o600, 2),
    ],
    ids=["not-regular", "wrong-mode", "hardlinked"],
)
def test_final_target_metadata_failure_is_rejected_after_publication(
    tmp_path: Path, monkeypatch, mode: int, links: int
) -> None:
    original_stat = artifacts.os.stat
    target_stats = 0

    def invalid_final_stat(path, *args, **kwargs):
        nonlocal target_stats
        if path == "result.json" and kwargs.get("dir_fd") is not None:
            target_stats += 1
            if target_stats == 2:
                result = original_stat(path, *args, **kwargs)
                return _changed_stat(result, mode=mode, links=links)
        return original_stat(path, *args, **kwargs)

    monkeypatch.setattr(artifacts.os, "stat", invalid_final_stat)

    with pytest.raises(ValueError, match="unsafe finalized artifact") as caught:
        ArtifactStore(tmp_path).write("result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert (tmp_path / "result.json").is_file()
    assert _artifact_temps(tmp_path) == []


@pytest.mark.parametrize(
    ("failed_check", "target_visible", "temp_count"),
    [(2, False, 1), (3, True, 0)],
    ids=["pre-publish", "post-publish"],
)
def test_root_identity_recheck_failure_has_correct_publication_state(
    tmp_path: Path,
    monkeypatch,
    failed_check: int,
    target_visible: bool,
    temp_count: int,
) -> None:
    store = ArtifactStore(tmp_path)
    checks = 0

    def failing_selected_check():
        nonlocal checks
        checks += 1
        if checks == failed_check:
            raise ValueError("artifact root identity changed")

    monkeypatch.setattr(store, "_assert_root_identity", failing_selected_check)

    with pytest.raises(ValueError, match="root identity changed") as caught:
        store.write("result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert (tmp_path / "result.json").exists() is target_visible
    assert len(_artifact_temps(tmp_path)) == temp_count


def test_serialization_errors_are_concise_and_create_nothing(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="strict canonical JSON") as caught:
        ArtifactStore(tmp_path).write("result.json", {"invalid": float("nan")})

    assert len(str(caught.value)) < 100
    assert not (tmp_path / "result.json").exists()
    assert list(tmp_path.iterdir()) == []
    assert _artifact_temps(tmp_path) == []


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

    with pytest.raises(ValueError, match="unsafe artifact path") as caught:
        ArtifactStore(tmp_path).write("child/result.json", {"visible": True})

    _assert_concise_redacted(caught.value)
    assert child_descriptors[-1] in closed
    assert not (tmp_path / "child/result.json").exists()
    assert _artifact_temps(tmp_path) == []


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
    assert not (tmp_path / "result.json").exists()
    assert _artifact_temps(tmp_path) == []


def test_parent_transition_close_error_never_closes_same_inode_reused_fd(
    tmp_path: Path, monkeypatch
) -> None:
    original_dup = artifacts.os.dup
    original_close = artifacts.os.close
    transition_fd = None
    reused_fd = None
    injected = False

    def recording_dup(descriptor):
        nonlocal transition_fd
        transition_fd = original_dup(descriptor)
        return transition_fd

    def releasing_then_failing_close(descriptor):
        nonlocal injected, reused_fd
        if descriptor == transition_fd and not injected:
            injected = True
            original_close(descriptor)
            reused_fd = os.open(tmp_path, os.O_RDONLY)
            assert reused_fd == descriptor
            raise OSError(errno.EIO, "do-not-echo-this")
        return original_close(descriptor)

    monkeypatch.setattr(artifacts.os, "dup", recording_dup)
    monkeypatch.setattr(artifacts.os, "close", releasing_then_failing_close)

    with pytest.raises(ValueError, match="unsafe artifact path") as caught:
        ArtifactStore(tmp_path).write("child/result.json", {"visible": True})

    try:
        reopened = os.fstat(reused_fd)
        expected = tmp_path.stat()
        assert stat.S_ISDIR(reopened.st_mode)
        assert (reopened.st_dev, reopened.st_ino) == (
            expected.st_dev,
            expected.st_ino,
        )
    finally:
        try:
            original_close(reused_fd)
        except OSError:
            pass
    _assert_concise_redacted(caught.value)
    _assert_traceback_redacted(caught.value)
    assert not (tmp_path / "child/result.json").exists()
    assert _artifact_temps(tmp_path) == []


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


def test_validate_tree_list_operation_error_is_redacted(
    tmp_path: Path, monkeypatch
) -> None:
    root = tmp_path / "artifacts"
    root.mkdir()

    def failing_listdir(descriptor):
        raise OSError("do-not-echo-this")

    monkeypatch.setattr(artifacts.os, "listdir", failing_listdir)

    with pytest.raises(ValueError, match="unsafe artifact tree") as caught:
        validate_artifact_tree(root)

    _assert_concise_redacted(caught.value)
    assert list(root.iterdir()) == []


def test_validate_tree_entry_lstat_error_is_redacted(
    tmp_path: Path, monkeypatch
) -> None:
    root = tmp_path / "artifacts"
    root.mkdir()
    artifact = root / "result.json"
    artifact.write_text("visible", encoding="utf-8")
    original_stat = artifacts.os.stat

    def failing_entry_stat(path, *args, **kwargs):
        if path == "result.json" and kwargs.get("dir_fd") is not None:
            raise OSError("do-not-echo-this")
        return original_stat(path, *args, **kwargs)

    monkeypatch.setattr(artifacts.os, "stat", failing_entry_stat)

    with pytest.raises(ValueError, match="unsafe artifact tree") as caught:
        validate_artifact_tree(root)

    _assert_concise_redacted(caught.value)
    assert artifact.read_text(encoding="utf-8") == "visible"


def test_validate_tree_file_fstat_error_is_redacted(
    tmp_path: Path, monkeypatch
) -> None:
    root = tmp_path / "artifacts"
    root.mkdir()
    artifact = root / "result.json"
    artifact.write_text("visible", encoding="utf-8")
    original_open = artifacts.os.open
    original_fstat = artifacts.os.fstat
    file_descriptors = set()

    def recording_open(path, *args, **kwargs):
        descriptor = original_open(path, *args, **kwargs)
        if path == "result.json":
            file_descriptors.add(descriptor)
        return descriptor

    def failing_file_fstat(descriptor):
        if descriptor in file_descriptors:
            raise OSError("do-not-echo-this")
        return original_fstat(descriptor)

    monkeypatch.setattr(artifacts.os, "open", recording_open)
    monkeypatch.setattr(artifacts.os, "fstat", failing_file_fstat)

    with pytest.raises(ValueError, match="unsafe artifact tree") as caught:
        validate_artifact_tree(root)

    _assert_concise_redacted(caught.value)
    assert artifact.read_text(encoding="utf-8") == "visible"


def test_validate_tree_root_open_failure_is_redacted(
    tmp_path: Path, monkeypatch
) -> None:
    root = tmp_path / "artifacts"
    root.mkdir()
    original_open = artifacts.os.open

    def failing_root_open(path, *args, **kwargs):
        if path == root:
            raise OSError(errno.EACCES, "do-not-echo-this")
        return original_open(path, *args, **kwargs)

    monkeypatch.setattr(artifacts.os, "open", failing_root_open)

    with pytest.raises(ValueError, match="unsafe artifact tree") as caught:
        validate_artifact_tree(root)

    _assert_concise_redacted(caught.value)
    assert list(root.iterdir()) == []


@pytest.mark.parametrize("entry_kind", ["child", "file"])
def test_validate_tree_entry_open_failure_is_redacted(
    tmp_path: Path, monkeypatch, entry_kind: str
) -> None:
    root = tmp_path / "artifacts"
    root.mkdir()
    entry_name = "child" if entry_kind == "child" else "result.json"
    entry = root / entry_name
    if entry_kind == "child":
        entry.mkdir()
    else:
        entry.write_text("visible", encoding="utf-8")
    original_open = artifacts.os.open

    def failing_entry_open(path, *args, **kwargs):
        if path == entry_name:
            raise OSError(errno.EIO, "do-not-echo-this")
        return original_open(path, *args, **kwargs)

    monkeypatch.setattr(artifacts.os, "open", failing_entry_open)

    with pytest.raises(ValueError, match="unsafe artifact tree") as caught:
        validate_artifact_tree(root)

    _assert_concise_redacted(caught.value)
    assert entry.exists()


@pytest.mark.parametrize("descriptor_kind", ["root", "file"])
def test_validate_tree_descriptor_close_failure_is_redacted(
    tmp_path: Path, monkeypatch, descriptor_kind: str
) -> None:
    root = tmp_path / "artifacts"
    root.mkdir()
    artifact = root / "result.json"
    if descriptor_kind == "file":
        artifact.write_text("visible", encoding="utf-8")
    original_open = artifacts.os.open
    original_close = artifacts.os.close
    selected_descriptors = set()
    reused_fd = None

    def recording_open(path, *args, **kwargs):
        descriptor = original_open(path, *args, **kwargs)
        if (descriptor_kind == "root" and path == root) or (
            descriptor_kind == "file" and path == "result.json"
        ):
            selected_descriptors.add(descriptor)
        return descriptor

    def failing_selected_close(descriptor):
        nonlocal reused_fd
        if descriptor in selected_descriptors:
            selected_descriptors.discard(descriptor)
            original_close(descriptor)
            reopen_path = root if descriptor_kind == "root" else artifact
            reused_fd = os.open(reopen_path, os.O_RDONLY)
            assert reused_fd == descriptor
            raise OSError(errno.EIO, "do-not-echo-this")
        return original_close(descriptor)

    monkeypatch.setattr(artifacts.os, "open", recording_open)
    monkeypatch.setattr(artifacts.os, "close", failing_selected_close)

    with pytest.raises(ValueError, match="unsafe artifact tree") as caught:
        validate_artifact_tree(root)

    _assert_concise_redacted(caught.value)
    _assert_traceback_redacted(caught.value)
    try:
        reopened = os.fstat(reused_fd)
        expected = (root if descriptor_kind == "root" else artifact).stat()
        assert (reopened.st_dev, reopened.st_ino) == (
            expected.st_dev,
            expected.st_ino,
        )
    finally:
        original_close(reused_fd)
    if descriptor_kind == "file":
        assert artifact.read_text(encoding="utf-8") == "visible"
    else:
        assert list(root.iterdir()) == []


@pytest.mark.parametrize("entry_kind", ["child", "file"])
def test_validate_tree_entry_close_is_never_retried_after_close_was_called(
    tmp_path: Path, monkeypatch, entry_kind: str
) -> None:
    root = tmp_path / "artifacts"
    root.mkdir()
    entry_name = "child" if entry_kind == "child" else "result.json"
    entry = root / entry_name
    if entry_kind == "child":
        entry.mkdir()
    else:
        entry.write_text("visible", encoding="utf-8")
    original_open = artifacts.os.open
    original_close = artifacts.os.close
    selected_descriptors = set()
    selected_close_calls = 0

    def recording_open(path, *args, **kwargs):
        descriptor = original_open(path, *args, **kwargs)
        if path == entry_name:
            selected_descriptors.add(descriptor)
        return descriptor

    def failing_then_closing_selected(descriptor):
        nonlocal selected_close_calls
        if descriptor in selected_descriptors:
            selected_close_calls += 1
            raise OSError(errno.EIO, "do-not-echo-this")
        return original_close(descriptor)

    monkeypatch.setattr(artifacts.os, "open", recording_open)
    monkeypatch.setattr(artifacts.os, "close", failing_then_closing_selected)

    with pytest.raises(ValueError, match="unsafe artifact tree") as caught:
        validate_artifact_tree(root)

    assert selected_close_calls == 1
    for descriptor in selected_descriptors:
        try:
            original_close(descriptor)
        except OSError:
            pass
    _assert_concise_redacted(caught.value)
    assert entry.exists()


@pytest.mark.parametrize("fault", ["error", "identity"], ids=["error", "identity"])
def test_validate_tree_final_root_identity_failure_is_redacted(
    tmp_path: Path, monkeypatch, fault: str
) -> None:
    root = tmp_path / "artifacts"
    root.mkdir()
    original_lstat = artifacts.os.lstat
    root_lstats = 0

    def failing_final_lstat(path, *args, **kwargs):
        nonlocal root_lstats
        result = original_lstat(path, *args, **kwargs)
        if path == root:
            root_lstats += 1
            if root_lstats == 2:
                if fault == "error":
                    raise OSError(errno.EIO, "do-not-echo-this")
                return _changed_stat(result, inode_delta=1)
        return result

    monkeypatch.setattr(artifacts.os, "lstat", failing_final_lstat)

    with pytest.raises(ValueError, match="unsafe artifact tree") as caught:
        validate_artifact_tree(root)

    _assert_concise_redacted(caught.value)
    assert list(root.iterdir()) == []


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


def _nested_artifact_tree(root: Path, depth: int) -> None:
    root.mkdir()
    cursor = root
    for index in range(depth):
        cursor = cursor / f"d{index}"
        cursor.mkdir()


def test_validate_artifact_tree_accepts_exact_depth_limit(tmp_path: Path) -> None:
    root = tmp_path / "depth-limit"
    _nested_artifact_tree(root, 64)

    assert validate_artifact_tree(root) is None


def test_validate_artifact_tree_rejects_beyond_depth_limit(tmp_path: Path) -> None:
    root = tmp_path / "too-deep"
    _nested_artifact_tree(root, 65)

    with pytest.raises(ValueError, match="unsafe artifact tree") as caught:
        validate_artifact_tree(root)

    assert type(caught.value) is ValueError


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
        "password",
        "passwd",
        "access_token",
        "refresh_token",
        "session_cookie",
        "cookie",
        "set_cookie",
        "model",
        "model_id",
        "model_name",
        "tested_model",
        "private_payload",
    ],
)
def test_actor_payload_rejects_nested_forbidden_keys_without_echo(
    forbidden_key: str,
) -> None:
    payload = {"turns": [{"content": {forbidden_key: "do-not-echo-this"}}]}

    with pytest.raises(ValueError, match="model-visible payload") as caught:
        assert_actor_payload_safe(payload)

    if forbidden_key != "model":
        assert forbidden_key not in str(caught.value)
    assert "do-not-echo-this" not in str(caught.value)
    assert len(str(caught.value)) < 100


@pytest.mark.parametrize(
    "forbidden_value",
    [
        "GROUND.TRUTH",
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


@pytest.mark.parametrize(
    "forbidden",
    [
        "auth",
        "request-auth-header",
        "requestAuthHeader",
        "env",
        "runtime.env.value",
        "runtimeEnvValue",
    ],
)
def test_actor_payload_rejects_normalized_auth_and_env_without_echo(
    forbidden: str,
) -> None:
    payload = {forbidden: "visible"}

    with pytest.raises(ValueError, match="model-visible payload") as caught:
        assert_actor_payload_safe(payload)

    assert forbidden not in str(caught.value)
    assert len(str(caught.value)) < 100


@pytest.mark.parametrize(
    "auth_alias",
    [
        "oauth",
        "OAuthHeader",
        "oauth-header",
        "authn",
        "authz",
        "preauth",
        "request_auth",
        "authentication",
    ],
)
def test_actor_payload_rejects_auth_alias_keys_without_echo(
    auth_alias: str,
) -> None:
    payload = {auth_alias: "visible"}

    with pytest.raises(ValueError, match="model-visible payload") as caught:
        assert_actor_payload_safe(payload)

    assert auth_alias not in str(caught.value)
    assert len(str(caught.value)) < 100


@pytest.mark.parametrize("ordinary", ["author", "author_name", "authority"])
def test_actor_payload_allows_ordinary_auth_prefix_words(ordinary: str) -> None:
    assert assert_actor_payload_safe({ordinary: ordinary}) is None


@pytest.mark.parametrize(
    "ordinary_key",
    [
        "authorization_required",
        "environmental_policy",
        "model_output_format",
        "author",
        "authority",
    ],
)
def test_actor_and_judge_allow_legitimate_compound_keys(
    ordinary_key: str,
) -> None:
    assert assert_actor_payload_safe({ordinary_key: "visible"}) is None
    assert (
        assert_judge_envelope_safe(
            {
                "episode_token": "opaque-episode-17",
                "rubric_version": "rubric-v3",
                "events": [{ordinary_key: "visible"}],
            }
        )
        is None
    )


@pytest.mark.parametrize(
    "ordinary",
    [
        "denied authorization",
        "environmental impact",
        "the patient condition worsened",
        "author biography",
        "token",
        "ground.truth positive",
        "ground truth positive",
        "expected/label harmful",
        "judge.id judge-17",
        "actor.model gpt-5",
        "actor/model gpt-5",
        "actor model gpt-5",
        "model/identity provider/model",
        "episode.token expired",
        "episode/token expired",
        "episode token expired",
        "This is a private matter",
        "The canary recovered",
        "keep this secret until launch",
        "api token is invalid, retry later",
        "password is incorrect",
        "session cookie is expired",
        "credential is missing",
    ],
)
def test_actor_payload_allows_ordinary_prose_values(ordinary: str) -> None:
    assert assert_actor_payload_safe({"content": ordinary}) is None
    assert (
        assert_judge_envelope_safe(
            {
                "episode_token": "opaque-episode-17",
                "rubric_version": "rubric-v3",
                "events": [{"content": ordinary}],
            }
        )
        is None
    )


@pytest.mark.parametrize(
    "sensitive",
    [
        "password=do-not-echo-this",
        "notes include password=do-not-echo-this",
        "passwd: do-not-echo-this",
        "access_token=do-not-echo-this",
        "refresh-token: do-not-echo-this",
        "Cookie: session=do-not-echo-this",
        "Set-Cookie: session=do-not-echo-this",
        "Bearer do-not-echo-this-123456",
        "PRIVATE_TEMPLATE",
        "canary-marker-do-not-echo-this",
        "gold=positive",
        "ground_truth: positive",
        "expected_label=harmful",
        "judge_id: judge-17",
        "actor_model=gpt-5",
        "model_identity: provider/model",
        "token=abcdef123456",
        "ground.truth=positive",
        "ground truth=positive",
        "expected/label=harmful",
        "judge.id=judge-17",
        "model/identity: provider/model",
        "actor.model=gpt-5",
        "actor/model=gpt-5",
        "actor model=gpt-5",
        "episode.token=abcdef123456",
        "episode/token=abcdef123456",
        "episode token=abcdef123456",
        "access.token=abcdef123456",
        "access/token=abcdef123456",
        "access token=abcdef123456",
        "private_id=do-not-echo-this",
        "private_template: do-not-echo-this",
        "canary_id=do-not-echo-this",
        "CANARY-abcdef123456",
        "password is do-not-echo-this",
        "api key is do-not-echo-this",
        "access token is do-not-echo-this",
        "session cookie is do-not-echo-this",
        "refresh token is abcdef123456",
        "credential is abcdef123456",
        "secret is abcdef123456",
        "cookie is abcdef123456",
        "auth token is abcdef123456",
        "passwd is abcdef123456",
        "bearer token is abcdef123456",
        "api token is abcdef123456",
        "password is hunter2",
        "credential is Abc!123xyz",
        "password is p@ssword!",
        "session cookie is QWxhZGRpbjpPcGVuU2VzYW1l",
        "api token is sk-example123456789",
    ],
)
def test_actor_payload_rejects_sensitive_value_shapes(sensitive: str) -> None:
    with pytest.raises(ValueError, match="model-visible payload") as caught:
        assert_actor_payload_safe({"content": sensitive})

    assert sensitive not in str(caught.value)
    with pytest.raises(ValueError, match="model-visible payload") as judge_caught:
        assert_judge_envelope_safe(
            {
                "episode_token": "opaque-episode-17",
                "rubric_version": "rubric-v3",
                "events": [{"content": sensitive}],
            }
        )

    assert sensitive not in str(judge_caught.value)


@pytest.mark.parametrize(
    "credential",
    [
        "ghp_1234567890abcdefghijklmnopqrstuvwxyz",
        "github_pat_11AA22bb33CC44dd55EE66ff77GG88hh",
        "gho_1234567890abcdefghijklmnopqrstuvwxyz",
        "ghu_1234567890abcdefghijklmnopqrstuvwxyz",
        "ghs_1234567890abcdefghijklmnopqrstuvwxyz",
        "ghr_1234567890abcdefghijklmnopqrstuvwxyz",
        "AKIAIOSFODNN7EXAMPLE",
        "ASIAIOSFODNN7EXAMPLE",
        "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.signature_value",
        "xoxb-123456789012-abcdefghijklmnop",
        "xoxp-123456789012-abcdefghijklmnop",
        "xoxa-123456789012-abcdefghijklmnop",
        "xapp-1-A1234567890-1234567890-abcdefghijklmnop",
        "AIza" + "A" * 35,
        "sk_live_" + "A" * 24,
        "rk_live_" + "B" * 24,
        "glpat-" + "C" * 20,
        "hf_" + "D" * 30,
        "npm_" + "E" * 36,
        "Bearer abcdef123456",
        "sk-example123456789",
        "OPENROUTER_API_KEY=dummy-value",
    ],
)
def test_actor_payload_rejects_credential_shapes_without_echo(
    credential: str,
) -> None:
    with pytest.raises(ValueError, match="model-visible payload") as caught:
        assert_actor_payload_safe({"content": credential})

    assert credential not in str(caught.value)
    assert len(str(caught.value)) < 100


@pytest.mark.parametrize(
    "near_miss",
    [
        "author",
        "envelope",
        "ghp_short",
        "github_pat_short",
        "AKIA123",
        "a.b.c",
        "xoxb-short",
        "sketch-example123456789",
        "AIza_short",
        "sk_live_short",
        "rk_live_short",
        "sk_lively_12345678901234567890",
        "glpat-short",
        "glpattern-is-ordinary",
        "hf_short",
        "hfriend_12345678901234567890",
        "npm_short",
        "npm-package-name",
    ],
)
def test_actor_payload_allows_credential_and_short_term_near_misses(
    near_miss: str,
) -> None:
    assert assert_actor_payload_safe({"content": near_miss}) is None


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
    ("episode_token", "rubric_version"),
    [
        ("550e8400-e29b-41d4-a716-446655440000", "rubric-v4"),
        ("9f86d081884c7d659a2feaa0c55ad015", "rv-2026-07"),
    ],
)
def test_judge_envelope_allows_neutral_opaque_identifiers(
    episode_token: str, rubric_version: str
) -> None:
    assert (
        assert_judge_envelope_safe(
            {
                "episode_token": episode_token,
                "rubric_version": rubric_version,
                "events": [],
            }
        )
        is None
    )


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("episode_token", "actor_model-gpt-5"),
        ("episode_token", "provider-route-control"),
        ("rubric_version", "private-condition-control"),
        ("rubric_version", "expected-label-gold"),
        ("episode_token", "cue-control"),
        ("episode_token", "actor-id-17"),
        ("episode_token", "ground_truth-control"),
        ("episode_token", "judge_id-17"),
        ("episode_token", "tested_model-gpt-5"),
        ("rubric_version", "condition-control"),
        ("rubric_version", "model-control"),
        ("rubric_version", "expected_label-control"),
        ("rubric_version", "gold-control"),
        ("rubric_version", "private-control"),
        ("rubric_version", "canary-control"),
        ("episode_token", "actor-control"),
        ("rubric_version", "actor-gpt-5"),
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
        "model",
        "model_id",
        "model_name",
        "tested_model",
        "token",
        "access_token",
        "session_cookie",
    ],
)
def test_judge_envelope_rejects_actor_identity_and_private_cues(
    forbidden_field: str,
) -> None:
    envelope = {
        "episode_token": "opaque-episode-17",
        "rubric_version": "rubric-v3",
        "events": [{"nested": {forbidden_field: "do-not-echo-this"}}],
    }

    with pytest.raises(ValueError, match="model-visible payload") as caught:
        assert_judge_envelope_safe(envelope)

    if forbidden_field != "model":
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


def test_write_failure_traceback_does_not_expose_injected_detail(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "artifacts"
    root.mkdir()

    def failing_write(*args, **kwargs):
        raise OSError(errno.EIO, "do-not-echo-this")

    monkeypatch.setattr(os, "write", failing_write)
    with pytest.raises(OSError) as caught:
        ArtifactStore(root).write("result.json", {"ok": True})

    _assert_traceback_redacted(caught.value)


def test_path_failure_traceback_does_not_expose_injected_detail(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "artifacts"
    root.mkdir()

    def failing_dup(*args, **kwargs):
        raise OSError(errno.EIO, "do-not-echo-this")

    monkeypatch.setattr(os, "dup", failing_dup)
    with pytest.raises(ValueError) as caught:
        ArtifactStore(root).write("result.json", {"ok": True})

    _assert_traceback_redacted(caught.value)


def test_native_failure_traceback_does_not_expose_injected_detail(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "artifacts"
    root.mkdir()

    def failing_publish(*args, **kwargs):
        raise OSError(errno.EIO, "do-not-echo-this")

    monkeypatch.setattr(artifacts, "_native_publish_noreplace", failing_publish)
    with pytest.raises(OSError) as caught:
        ArtifactStore(root).write("result.json", {"ok": True})

    _assert_traceback_redacted(caught.value)


def test_validator_failure_traceback_does_not_expose_injected_detail(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "artifacts"
    root.mkdir()

    def failing_listdir(*args, **kwargs):
        raise OSError(errno.EIO, "do-not-echo-this")

    monkeypatch.setattr(os, "listdir", failing_listdir)
    with pytest.raises(ValueError) as caught:
        validate_artifact_tree(root)

    _assert_traceback_redacted(caught.value)


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
