"""Create-only artifacts, fsynced hash-chain journal, and whole-root closure."""
from __future__ import annotations

import fcntl
import json
import os
from pathlib import Path, PurePosixPath
import re

from . import contracts


JOURNAL = "journal.jsonl"
_ENTRY_FIELDS = {
    "journal_version", "sequence", "event", "artifact",
    "artifact_sha256", "previous_entry_sha256", "terminal",
}
_ATTEMPT_RE = re.compile(
    r"^(access/[^/]+|episodes/[^/]+/[^/]+)/attempt-([1-3])\.json$"
)


def _strict_loads(raw: bytes, label: str):
    def unique_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"{label} contains duplicate JSON key {key!r}")
            result[key] = value
        return result
    try:
        return json.loads(
            raw.decode("utf-8", errors="strict"),
            object_pairs_hook=unique_pairs,
            parse_constant=lambda _value: (_ for _ in ()).throw(ValueError()),
        )
    except (UnicodeError, json.JSONDecodeError, ValueError):
        raise ValueError(f"{label} is not strict JSON") from None


def _relative_path(value: str) -> str:
    if not isinstance(value, str) or not value or "\\" in value:
        raise ValueError("artifact path must be a normalized relative path")
    pure = PurePosixPath(value)
    if pure.is_absolute() or any(part in {"", ".", ".."} for part in pure.parts):
        raise ValueError("artifact path must be a normalized relative path")
    normalized = pure.as_posix()
    if normalized == JOURNAL:
        raise ValueError("journal cannot be committed as an artifact")
    return normalized


def _reject_symlinks(path: Path) -> None:
    candidate = Path(path).expanduser().absolute()
    for part in (candidate, *candidate.parents):
        if part.is_symlink():
            raise ValueError(f"evidence path contains symlink: {part}")
    if candidate.exists() and candidate.is_dir():
        for child in candidate.rglob("*"):
            if child.is_symlink():
                raise ValueError(f"evidence root contains symlink: {child}")


def _fsync_directory(path: Path) -> None:
    descriptor = os.open(str(path), os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _write_create_only(path: Path, value) -> str:
    contracts.assert_artifact_safe(value)
    data = contracts.canonical_bytes(value)
    path.parent.mkdir(parents=True, exist_ok=True)
    _reject_symlinks(path.parent)
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())
    _fsync_directory(path.parent)
    return contracts.sha256_value(value)


def _read_canonical(path: Path):
    raw = path.read_bytes()
    value = _strict_loads(raw, str(path))
    if raw != contracts.canonical_bytes(value):
        raise ValueError(f"artifact is not canonical JSON: {path}")
    contracts.assert_artifact_safe(value)
    return value


class EvidenceStore:
    """A single qualification evidence root; journal mutation is append-only."""

    def __init__(self, root: Path):
        self.root = Path(root).expanduser().absolute()
        _reject_symlinks(self.root)
        if not self.root.is_dir():
            raise ValueError("evidence root does not exist")

    @classmethod
    def create(cls, root: Path, manifest: dict, canary_selection: dict):
        root = Path(root).expanduser().absolute()
        _reject_symlinks(root.parent)
        root.mkdir(parents=True, exist_ok=False)
        _fsync_directory(root.parent)
        store = cls(root)
        manifest_hash = _write_create_only(root / "manifest.json", manifest)
        store._append_entry("manifest_frozen", "manifest.json", manifest_hash)
        canary_hash = _write_create_only(
            root / "canary_selection.json", canary_selection
        )
        store._append_entry(
            "canary_selection_frozen", "canary_selection.json", canary_hash
        )
        return store

    @classmethod
    def open(cls, root: Path):
        store = cls(root)
        verify_evidence_root(store.root)
        return store

    def read_journal(self) -> list[dict]:
        return _read_journal(self.root / JOURNAL)

    def _append_entry(self, event: str, artifact: str | None,
                      artifact_sha256: str | None) -> dict:
        if not isinstance(event, str) or not event:
            raise ValueError("journal event must be non-empty")
        if artifact is not None:
            artifact = _relative_path(artifact)
            contracts.assert_sha256(artifact_sha256, "artifact_sha256")
        elif artifact_sha256 is not None:
            raise ValueError("journal entry without artifact cannot carry a hash")
        journal = self.root / JOURNAL
        journal.parent.mkdir(parents=True, exist_ok=True)
        with journal.open("a+b") as handle:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
            handle.seek(0)
            raw = handle.read()
            entries = _parse_journal_bytes(raw) if raw else []
            previous = contracts.sha256_value(entries[-1]) if entries else "0" * 64
            entry = {
                "journal_version": "crossroads-evidence-journal-v1",
                "sequence": len(entries) + 1,
                "event": event,
                "artifact": artifact,
                "artifact_sha256": artifact_sha256,
                "previous_entry_sha256": previous,
                "terminal": True,
            }
            data = contracts.canonical_bytes(entry)
            handle.seek(0, os.SEEK_END)
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        _fsync_directory(self.root)
        return entry

    def commit(self, relative: str, payload, *, event: str) -> dict:
        relative = _relative_path(relative)
        path = self.root / relative
        digest = _write_create_only(path, payload)
        self._append_entry(event, relative, digest)
        return payload

    def adopt_orphan(self, relative: str, *, event: str, validator) -> dict:
        relative = _relative_path(relative)
        if not callable(validator):
            raise ValueError("orphan validator must be callable")
        if any(row["artifact"] == relative for row in self.read_journal()):
            raise ValueError("artifact is already journaled")
        path = self.root / relative
        if not path.is_file() or path.is_symlink():
            raise ValueError("orphan artifact is absent or unsafe")
        payload = _read_canonical(path)
        if validator(deepcopy_json(payload)) is not True:
            raise ValueError("orphan artifact failed semantic validation")
        self._append_entry(event, relative, contracts.sha256_value(payload))
        return payload

    def complete_phase(self, phase: str) -> dict:
        if phase not in {"access", "canary", "smoke", "diagnostic", "report"}:
            raise ValueError("unknown qualification phase")
        event = f"phase_complete:{phase}"
        if any(row["event"] == event for row in self.read_journal()):
            raise ValueError(f"phase {phase} is already complete")
        return self._append_entry(event, None, None)


def deepcopy_json(value):
    return json.loads(json.dumps(value))


def _parse_journal_bytes(raw: bytes) -> list[dict]:
    if not raw.endswith(b"\n"):
        raise ValueError("journal is not newline terminated")
    lines = raw.splitlines(keepends=True)
    entries = []
    for index, line in enumerate(lines, 1):
        value = _strict_loads(line, f"journal line {index}")
        if line != contracts.canonical_bytes(value):
            raise ValueError("journal contains non-canonical entry")
        entries.append(value)
    _validate_journal(entries)
    return entries


def _read_journal(path: Path) -> list[dict]:
    if not path.is_file() or path.is_symlink():
        raise ValueError("journal is missing or unsafe")
    return _parse_journal_bytes(path.read_bytes())


def _validate_journal(entries: list[dict]) -> None:
    previous = "0" * 64
    artifact_paths, phases = set(), set()
    for sequence, entry in enumerate(entries, 1):
        if not isinstance(entry, dict) or set(entry) != _ENTRY_FIELDS:
            raise ValueError("journal entry fields changed")
        if entry["journal_version"] != "crossroads-evidence-journal-v1":
            raise ValueError("journal version changed")
        if entry["sequence"] != sequence or entry["terminal"] is not True:
            raise ValueError("journal sequence/terminal state is invalid")
        if entry["previous_entry_sha256"] != previous:
            raise ValueError("journal hash chain is invalid")
        previous = contracts.sha256_value(entry)
        artifact = entry["artifact"]
        if artifact is None:
            if entry["artifact_sha256"] is not None or not entry["event"].startswith(
                    "phase_complete:"):
                raise ValueError("journal non-artifact event is invalid")
            if entry["event"] in phases:
                raise ValueError("journal phase completion is duplicated")
            phases.add(entry["event"])
        else:
            artifact = _relative_path(artifact)
            contracts.assert_sha256(entry["artifact_sha256"], "artifact_sha256")
            if artifact in artifact_paths:
                raise ValueError("journal artifact is referenced more than once")
            artifact_paths.add(artifact)


def _validate_attempt_sequences(root: Path, entries: list[dict]) -> None:
    attempts = {}
    for entry in entries:
        artifact = entry["artifact"]
        if artifact is None:
            continue
        match = _ATTEMPT_RE.fullmatch(artifact)
        if not match:
            continue
        group, attempt_text = match.groups()
        payload = _read_canonical(root / artifact)
        attempts.setdefault(group, []).append((int(attempt_text), payload.get("status")))
    for group, values in attempts.items():
        values.sort()
        if [attempt for attempt, _ in values] != list(range(1, len(values) + 1)):
            raise ValueError(f"attempt sequence is not contiguous: {group}")
        successes = [attempt for attempt, status in values if status == "success"]
        if len(successes) > 1 or (successes and successes[0] != values[-1][0]):
            raise ValueError(f"attempts continue after success: {group}")


def verify_evidence_root(root: Path) -> dict:
    """Verify journal closure: every file exactly once, no missing/extra bytes."""
    root = Path(root).expanduser().absolute()
    _reject_symlinks(root)
    entries = _read_journal(root / JOURNAL)
    referenced = {entry["artifact"] for entry in entries if entry["artifact"] is not None}
    actual = set()
    for path in root.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"evidence root contains symlink: {path}")
        if path.is_file():
            actual.add(path.relative_to(root).as_posix())
    expected = referenced | {JOURNAL}
    missing = expected - actual
    extra = actual - expected
    if missing:
        raise ValueError(f"evidence root has missing referenced artifacts: {sorted(missing)}")
    if extra:
        raise ValueError(f"evidence root has unreferenced artifacts: {sorted(extra)}")
    for entry in entries:
        relative = entry["artifact"]
        if relative is None:
            continue
        payload = _read_canonical(root / relative)
        if contracts.sha256_value(payload) != entry["artifact_sha256"]:
            raise ValueError(f"artifact hash differs: {relative}")
    if not {"manifest.json", "canary_selection.json"} <= referenced:
        raise ValueError("evidence root lacks frozen manifest/canary artifacts")
    manifest = _read_canonical(root / "manifest.json")
    canary = _read_canonical(root / "canary_selection.json")
    if manifest.get("purpose") != "public qualification" or canary.get(
            "purpose") != "public qualification":
        raise ValueError("evidence root purpose differs")
    if manifest.get("canary_item_ids") != canary.get("item_ids"):
        raise ValueError("manifest and frozen canary selection differ")
    _validate_attempt_sequences(root, entries)
    return {
        "valid": True, "artifacts": len(referenced),
        "journal_entries": len(entries),
        "phases_complete": [
            row["event"].split(":", 1)[1] for row in entries
            if row["event"].startswith("phase_complete:")
        ],
    }

