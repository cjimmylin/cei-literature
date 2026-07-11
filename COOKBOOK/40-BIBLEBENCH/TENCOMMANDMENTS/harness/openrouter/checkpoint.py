"""Durable canonical JSONL checkpoints with one SHA-256 chain per stream."""

from dataclasses import dataclass
import fcntl
import os
from pathlib import Path
import stat
from typing import Any, Dict, Optional, Tuple

from .canonical import (
    CanonicalJSONError,
    canonical_json_bytes,
    canonical_sha256,
    is_sha256,
    load_canonical_json,
)


CHECKPOINT_SCHEMA_VERSION = 1
ZERO_CHECKPOINT_SHA256 = "0" * 64
MAX_CHECKPOINT_STREAM_BYTES = 256 * 1024 * 1024
_CHECKPOINT_FIELDS = {
    "schema_version",
    "stream_id",
    "checkpoint_index",
    "previous_checkpoint_sha256",
    "checkpoint_sha256",
    "payload",
}


class CheckpointError(ValueError):
    """Raised when a checkpoint target or chain fails closed."""


def _stream_id(value: Any) -> str:
    if type(value) is not str or not value.strip() or value.strip() != value:
        raise CheckpointError("stream_id must be nonblank exact text")
    return value


def _bound_path(value: Any) -> Path:
    try:
        raw = Path(value)
        if not raw.name:
            raise CheckpointError("checkpoint path must name a file")
        parent = raw.parent.resolve(strict=True)
        parent_status = parent.stat()
    except CheckpointError:
        raise
    except (OSError, RuntimeError, TypeError) as exc:
        raise CheckpointError("checkpoint parent directory must exist") from exc
    if not stat.S_ISDIR(parent_status.st_mode):
        raise CheckpointError("checkpoint parent must be a directory")
    return parent / raw.name


def _open_target(path: Path, *, create: bool) -> int:
    flags = os.O_RDWR if create else os.O_RDONLY
    if create:
        flags |= os.O_CREAT | os.O_APPEND
    flags |= getattr(os, "O_CLOEXEC", 0)
    flags |= getattr(os, "O_NOFOLLOW", 0)
    flags |= getattr(os, "O_NONBLOCK", 0)
    try:
        descriptor = os.open(str(path), flags, 0o600)
        target = os.fstat(descriptor)
        if not stat.S_ISREG(target.st_mode) or target.st_nlink != 1:
            raise OSError("checkpoint target is not a regular single-link file")
        return descriptor
    except BaseException:
        try:
            os.close(descriptor)
        except (NameError, OSError):
            pass
        raise


def _read_descriptor(descriptor: int) -> bytes:
    os.lseek(descriptor, 0, os.SEEK_SET)
    chunks = []
    total = 0
    while True:
        remaining = MAX_CHECKPOINT_STREAM_BYTES - total
        chunk = os.read(descriptor, min(1024 * 1024, remaining + 1))
        if not chunk:
            return b"".join(chunks)
        if len(chunk) > remaining:
            raise CheckpointError("checkpoint stream exceeds maximum byte size")
        chunks.append(chunk)
        total += len(chunk)


def _checkpoint_digest(row: Dict[str, Any]) -> str:
    candidate = dict(row)
    candidate["checkpoint_sha256"] = None
    return canonical_sha256(candidate)


@dataclass(frozen=True)
class CheckpointRecord:
    """One immutable checkpoint row; payload access returns a fresh object."""

    schema_version: int
    stream_id: str
    checkpoint_index: int
    previous_checkpoint_sha256: str
    checkpoint_sha256: str
    _payload_bytes: bytes

    @property
    def payload(self) -> Dict[str, Any]:
        return load_canonical_json(self._payload_bytes)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "stream_id": self.stream_id,
            "checkpoint_index": self.checkpoint_index,
            "previous_checkpoint_sha256": self.previous_checkpoint_sha256,
            "checkpoint_sha256": self.checkpoint_sha256,
            "payload": self.payload,
        }


@dataclass(frozen=True)
class CheckpointSnapshot:
    """Verified immutable view of one entire checkpoint stream."""

    stream_id: str
    records: Tuple[CheckpointRecord, ...]

    @property
    def payloads(self) -> Tuple[Dict[str, Any], ...]:
        return tuple(record.payload for record in self.records)

    @property
    def head_sha256(self) -> str:
        if not self.records:
            return ZERO_CHECKPOINT_SHA256
        return self.records[-1].checkpoint_sha256

    @property
    def next_index(self) -> int:
        return len(self.records)


def _record_from_row(
    row: Dict[str, Any],
    *,
    expected_stream_id: str,
    expected_index: int,
    expected_previous: str,
) -> CheckpointRecord:
    if type(row) is not dict or set(row) != _CHECKPOINT_FIELDS:
        raise CheckpointError("checkpoint row schema is invalid")
    payload = row.get("payload")
    if (
        type(row.get("schema_version")) is not int
        or row["schema_version"] != CHECKPOINT_SCHEMA_VERSION
        or row.get("stream_id") != expected_stream_id
        or type(row.get("checkpoint_index")) is not int
        or row["checkpoint_index"] != expected_index
        or row.get("previous_checkpoint_sha256") != expected_previous
        or not is_sha256(row.get("checkpoint_sha256"))
        or type(payload) is not dict
    ):
        raise CheckpointError("checkpoint stream identity, index, or chain is invalid")
    try:
        expected_digest = _checkpoint_digest(row)
    except CanonicalJSONError as exc:
        raise CheckpointError("checkpoint row is not bounded canonical JSON") from exc
    if row["checkpoint_sha256"] != expected_digest:
        raise CheckpointError("checkpoint hash chain verification failed")
    return CheckpointRecord(
        row["schema_version"],
        row["stream_id"],
        row["checkpoint_index"],
        row["previous_checkpoint_sha256"],
        row["checkpoint_sha256"],
        canonical_json_bytes(payload),
    )


def _parse_stream(
    raw: bytes, stream_id: str, *, allow_empty: bool
) -> CheckpointSnapshot:
    if not raw:
        if allow_empty:
            return CheckpointSnapshot(stream_id, tuple())
        raise CheckpointError("checkpoint stream is empty or incomplete")
    if not raw.endswith(b"\n"):
        raise CheckpointError("checkpoint stream is incomplete (missing final newline)")
    lines = raw[:-1].split(b"\n")
    if any(not line for line in lines):
        raise CheckpointError("checkpoint stream contains a blank line")
    previous = ZERO_CHECKPOINT_SHA256
    records = []
    for index, line in enumerate(lines):
        try:
            row = load_canonical_json(line)
        except CanonicalJSONError as exc:
            raise CheckpointError("checkpoint row is not canonical JSON") from exc
        record = _record_from_row(
            row,
            expected_stream_id=stream_id,
            expected_index=index,
            expected_previous=previous,
        )
        records.append(record)
        previous = record.checkpoint_sha256
    return CheckpointSnapshot(stream_id, tuple(records))


def load_checkpoint_stream(path: Any, stream_id: str) -> CheckpointSnapshot:
    """Load and verify an existing stream; a missing target is an empty stream."""

    resolved_stream = _stream_id(stream_id)
    bound = _bound_path(path)
    try:
        os.lstat(str(bound))
    except FileNotFoundError:
        return CheckpointSnapshot(resolved_stream, tuple())
    except OSError as exc:
        raise CheckpointError("checkpoint target cannot be inspected") from exc
    descriptor = None
    try:
        descriptor = _open_target(bound, create=False)
        fcntl.flock(descriptor, fcntl.LOCK_SH)
        raw = _read_descriptor(descriptor)
        return _parse_stream(raw, resolved_stream, allow_empty=False)
    except CheckpointError:
        raise
    except OSError as exc:
        raise CheckpointError("checkpoint target is unsafe or unreadable") from exc
    finally:
        if descriptor is not None:
            try:
                fcntl.flock(descriptor, fcntl.LOCK_UN)
            except OSError:
                pass
            try:
                os.close(descriptor)
            except OSError:
                pass


def verify_checkpoint_stream(path: Any, stream_id: str) -> CheckpointSnapshot:
    """Verify and return one stream (explicit alias for audit call sites)."""

    return load_checkpoint_stream(path, stream_id)


def append_checkpoint(
    path: Any,
    stream_id: str,
    payload: Any,
    *,
    expected_head_sha256: Optional[str] = None,
) -> CheckpointRecord:
    """Atomically append one canonical row after verifying the entire stream."""

    resolved_stream = _stream_id(stream_id)
    if type(payload) is not dict:
        raise CheckpointError("checkpoint payload must be an exact JSON object")
    try:
        payload_bytes = canonical_json_bytes(payload)
        frozen_payload = load_canonical_json(payload_bytes)
    except CanonicalJSONError as exc:
        raise CheckpointError("checkpoint payload is not bounded canonical JSON") from exc
    if expected_head_sha256 is not None and not is_sha256(expected_head_sha256):
        raise CheckpointError("expected checkpoint head must be a SHA-256 digest")
    bound = _bound_path(path)
    descriptor = None
    try:
        descriptor = _open_target(bound, create=True)
        fcntl.flock(descriptor, fcntl.LOCK_EX)
        snapshot = _parse_stream(
            _read_descriptor(descriptor),
            resolved_stream,
            allow_empty=True,
        )
        if (
            expected_head_sha256 is not None
            and expected_head_sha256 != snapshot.head_sha256
        ):
            raise CheckpointError("checkpoint head changed before append")
        row = {
            "schema_version": CHECKPOINT_SCHEMA_VERSION,
            "stream_id": resolved_stream,
            "checkpoint_index": snapshot.next_index,
            "previous_checkpoint_sha256": snapshot.head_sha256,
            "checkpoint_sha256": None,
            "payload": frozen_payload,
        }
        row["checkpoint_sha256"] = _checkpoint_digest(row)
        line = canonical_json_bytes(row) + b"\n"
        os.lseek(descriptor, 0, os.SEEK_END)
        written = os.write(descriptor, line)
        if written != len(line):
            raise OSError("short checkpoint append")
        os.fsync(descriptor)
        return _record_from_row(
            row,
            expected_stream_id=resolved_stream,
            expected_index=snapshot.next_index,
            expected_previous=snapshot.head_sha256,
        )
    except CheckpointError:
        raise
    except OSError as exc:
        raise CheckpointError("checkpoint append failed") from exc
    finally:
        if descriptor is not None:
            try:
                fcntl.flock(descriptor, fcntl.LOCK_UN)
            except OSError:
                pass
            try:
                os.close(descriptor)
            except OSError:
                pass


__all__ = [
    "CHECKPOINT_SCHEMA_VERSION",
    "MAX_CHECKPOINT_STREAM_BYTES",
    "ZERO_CHECKPOINT_SHA256",
    "CheckpointError",
    "CheckpointRecord",
    "CheckpointSnapshot",
    "append_checkpoint",
    "load_checkpoint_stream",
    "verify_checkpoint_stream",
]
