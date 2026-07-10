#!/usr/bin/env python3
"""Crash-safe append-only evidence journal for live THORNS runs.

The journal owns path reservation and durable event appends.  It intentionally
does not make API calls: callers record a request before a call and record its
result or error before beginning the next call.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import math
import os
from pathlib import Path
import re
import stat
import threading
from typing import Any, Dict, Iterable, Mapping, Optional, Sequence, Tuple, Union

try:  # ``fcntl`` is stdlib on the Unix platforms used by the live harness.
    import fcntl
except ImportError:  # pragma: no cover - defensive fallback for non-Unix hosts.
    fcntl = None  # type: ignore[assignment]


EVENT_SCHEMA = "fruitbench.thorns.live-journal.event.v1"
GENESIS_HASH = "0" * 64
HASH_FIELDS = (
    "config_sha256",
    "source_sha256",
    "schedule_sha256",
    "receipt_sha256",
)
LIVE_EVENT_TYPES = frozenset(
    {
        "actor_request",
        "actor_result",
        "actor_error",
        "layer_e_request",
        "layer_e_result",
        "layer_e_error",
        "layer_r_request",
        "layer_r_result",
        "layer_r_error",
        "layer_control_request",
        "layer_control_result",
        "layer_control_error",
        "human_adjudication",
        "job_start",
        "trajectory_result",
        "score_result",
        "job_error",
        "analysis_result",
    }
)
_ALL_EVENT_TYPES = LIVE_EVENT_TYPES | {"run_start", "completion"}
_ROW_FIELDS = {
    "schema",
    "sequence",
    "previous_hash",
    "event_type",
    "payload",
    "event_hash",
}
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
_API_KEY_VALUE_RE = re.compile(
    r"(?i)(?:\bbearer\s+[A-Za-z0-9._~+/=-]{4,}|"
    r"\bsk-(?:or-v1-|proj-)?[A-Za-z0-9_-]{8,})"
)
_SECRET_KEYS = frozenset(
    {
        "api_key",
        "apikey",
        "authorization",
        "client_secret",
        "openai_api_key",
        "openrouter_api_key",
        "password",
        "proxy_authorization",
        "refresh_token",
        "secret",
        "token",
        "access_token",
        "x_api_key",
    }
)
_SECRET_KEYS_COLLAPSED = frozenset(
    {
        "accesstoken",
        "apikey",
        "authorization",
        "clientsecret",
        "credential",
        "credentials",
        "openaiapikey",
        "openrouterapikey",
        "password",
        "privatekey",
        "proxyauthorization",
        "refreshtoken",
        "secret",
        "secretkey",
        "token",
        "xapikey",
    }
)


class LiveJournalError(Exception):
    """Base class for journal failures."""


class JournalIntegrityError(LiveJournalError):
    """The on-disk journal or its reservations failed validation."""


class PathReservationError(LiveJournalError):
    """One or more intended paths could not be reserved exclusively."""


class ResumeRefusedError(LiveJournalError):
    """An existing journal is valid but is not eligible for this resume."""


class CompletedJournalError(ResumeRefusedError):
    """A completed journal cannot receive additional events."""


class IncompleteJournalError(LiveJournalError):
    """Aggregation was attempted before a journal completed."""


class SecretMaterialError(LiveJournalError, ValueError):
    """Potential credential material was rejected before serialization."""


class JournalStateError(LiveJournalError):
    """The journal is closed or faulted and cannot accept an event."""


@dataclass(frozen=True)
class RunIdentity:
    """Immutable hashes that bind a journal to one exact live run."""

    run_id: str
    config_sha256: str
    source_sha256: str
    schedule_sha256: str
    receipt_sha256: str

    def __post_init__(self) -> None:
        if (
            not isinstance(self.run_id, str)
            or not self.run_id.strip()
            or self.run_id != self.run_id.strip()
        ):
            raise ValueError("run_id must be a non-empty trimmed string")
        for field_name in HASH_FIELDS:
            value = getattr(self, field_name)
            if not isinstance(value, str) or not _SHA256_RE.fullmatch(value):
                raise ValueError(
                    "{} must be an exact lowercase SHA-256 hex digest".format(
                        field_name
                    )
                )

    def as_dict(self) -> Dict[str, str]:
        return {
            "run_id": self.run_id,
            "config_sha256": self.config_sha256,
            "source_sha256": self.source_sha256,
            "schedule_sha256": self.schedule_sha256,
            "receipt_sha256": self.receipt_sha256,
        }


@dataclass(frozen=True)
class _Reservation:
    path: str
    device: int
    inode: int

    def as_dict(self) -> Dict[str, Union[str, int]]:
        return {"path": self.path, "device": self.device, "inode": self.inode}


@dataclass(frozen=True)
class JournalSnapshot:
    """Result of fully validating a journal and its reserved paths."""

    events: Tuple[Mapping[str, Any], ...]
    identity: RunIdentity
    resumable: bool
    reservations: Tuple[_Reservation, ...]
    completed: bool


Pathish = Union[str, os.PathLike]


def _normalise_path(path: Pathish) -> Path:
    if not isinstance(path, (str, os.PathLike)):
        raise TypeError("journal and output paths must be path-like")
    lexical = os.fspath(path)
    if not isinstance(lexical, str):
        raise TypeError("journal and output paths must resolve to text paths")
    # Keep the final lexical component intact so O_EXCL rejects even a dangling
    # symlink instead of following it and creating the symlink's target.
    return Path(os.path.abspath(os.path.expanduser(lexical)))


def _canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def _normalised_secret_key(key: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", key.lower()).strip("_")


def _contains_secret_material(value: Any) -> bool:
    if isinstance(value, dict):
        for key, nested in value.items():
            if not isinstance(key, str):
                continue
            normalised = _normalised_secret_key(key)
            collapsed = normalised.replace("_", "")
            if (
                normalised in _SECRET_KEYS
                or normalised.endswith("_api_key")
                or collapsed in _SECRET_KEYS_COLLAPSED
            ):
                return True
            if _contains_secret_material(nested):
                return True
        return False
    if isinstance(value, list):
        return any(_contains_secret_material(item) for item in value)
    return isinstance(value, str) and bool(_API_KEY_VALUE_RE.search(value))


def _validate_json_shape(value: Any) -> None:
    if value is None or isinstance(value, (bool, int, str)):
        return
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("payload must contain only canonical JSON values")
        return
    if isinstance(value, list):
        for item in value:
            _validate_json_shape(item)
        return
    if isinstance(value, dict):
        for key, nested in value.items():
            if not isinstance(key, str):
                raise ValueError("payload must contain only string JSON object keys")
            _validate_json_shape(nested)
        return
    raise ValueError("payload must contain only canonical JSON values")


def _normalise_payload(payload: Mapping[str, Any]) -> Dict[str, Any]:
    if not isinstance(payload, dict):
        raise ValueError("payload must be a JSON object")
    _validate_json_shape(payload)
    if _contains_secret_material(payload):
        raise SecretMaterialError(
            "payload contains secret material and was not journaled"
        )
    try:
        # The round trip detaches the durable row from caller-owned mutable data.
        return json.loads(_canonical_json_bytes(payload).decode("utf-8"))
    except (TypeError, ValueError, UnicodeError) as exc:
        raise ValueError("payload must contain only canonical JSON values") from exc


def _build_row(
    sequence: int,
    previous_hash: str,
    event_type: str,
    payload: Mapping[str, Any],
) -> Dict[str, Any]:
    material: Dict[str, Any] = {
        "schema": EVENT_SCHEMA,
        "sequence": sequence,
        "previous_hash": previous_hash,
        "event_type": event_type,
        "payload": _normalise_payload(payload),
    }
    material["event_hash"] = hashlib.sha256(
        _canonical_json_bytes(material)
    ).hexdigest()
    return material


def _sync_directories(paths: Iterable[Path]) -> None:
    flags = os.O_RDONLY
    if hasattr(os, "O_DIRECTORY"):
        flags |= os.O_DIRECTORY
    for directory in sorted({path.parent for path in paths}, key=str):
        descriptor = os.open(str(directory), flags)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)


def _reservation(path: Path, descriptor: int) -> _Reservation:
    metadata = os.fstat(descriptor)
    if not stat.S_ISREG(metadata.st_mode):
        raise PathReservationError("intended paths must be regular files")
    return _Reservation(str(path), metadata.st_dev, metadata.st_ino)


def _cleanup_created(
    opened: Sequence[Tuple[Path, int, _Reservation]],
) -> None:
    for _, descriptor, _ in opened:
        try:
            os.close(descriptor)
        except OSError:
            pass
    removed = []
    for path, _, reservation in reversed(opened):
        try:
            current = os.lstat(str(path))
            if (
                stat.S_ISREG(current.st_mode)
                and current.st_dev == reservation.device
                and current.st_ino == reservation.inode
            ):
                os.unlink(str(path))
                removed.append(path)
        except FileNotFoundError:
            pass
    if removed:
        _sync_directories(removed)


def _acquire_lock(descriptor: int, *, exclusive: bool) -> None:
    if fcntl is None:  # pragma: no cover - non-Unix fallback.
        return
    operation = fcntl.LOCK_EX if exclusive else fcntl.LOCK_SH
    try:
        fcntl.flock(descriptor, operation | fcntl.LOCK_NB)
    except BlockingIOError as exc:
        raise ResumeRefusedError("journal is already open by another process") from exc


def _release_lock(descriptor: int) -> None:
    if fcntl is not None:
        try:
            fcntl.flock(descriptor, fcntl.LOCK_UN)
        except OSError:
            pass


def _reject_duplicate_keys(pairs: Sequence[Tuple[str, Any]]) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise JournalIntegrityError("journal row contains duplicate JSON keys")
        result[key] = value
    return result


def _decode_canonical_row(raw_line: bytes, index: int) -> Dict[str, Any]:
    if not raw_line.endswith(b"\n"):
        raise JournalIntegrityError(
            "journal row {} is missing its terminating newline".format(index)
        )
    body = raw_line[:-1]
    if not body:
        raise JournalIntegrityError("journal row {} is empty".format(index))
    try:
        decoded = json.loads(
            body.decode("utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=lambda value: (_raise_nonfinite_json(value)),
        )
    except JournalIntegrityError:
        raise
    except (UnicodeError, ValueError, TypeError, json.JSONDecodeError) as exc:
        raise JournalIntegrityError(
            "journal row {} is not valid JSON".format(index)
        ) from exc
    if not isinstance(decoded, dict):
        raise JournalIntegrityError("journal row {} is not a JSON object".format(index))
    try:
        canonical = _canonical_json_bytes(decoded) + b"\n"
    except (TypeError, ValueError) as exc:
        raise JournalIntegrityError(
            "journal row {} is not canonical JSON".format(index)
        ) from exc
    if raw_line != canonical:
        raise JournalIntegrityError(
            "journal row {} is not canonical JSON".format(index)
        )
    return decoded


def _raise_nonfinite_json(value: str) -> None:
    raise JournalIntegrityError("journal contains non-finite JSON: {}".format(value))


def _parse_reservations(value: Any) -> Tuple[_Reservation, ...]:
    if not isinstance(value, list) or not value:
        raise JournalIntegrityError("run_start reservations must be a non-empty list")
    reservations = []
    paths = set()
    for entry in value:
        if not isinstance(entry, dict) or set(entry) != {"path", "device", "inode"}:
            raise JournalIntegrityError("run_start contains an invalid reservation")
        path = entry["path"]
        device = entry["device"]
        inode = entry["inode"]
        if (
            not isinstance(path, str)
            or not path
            or not isinstance(device, int)
            or isinstance(device, bool)
            or device < 0
            or not isinstance(inode, int)
            or isinstance(inode, bool)
            or inode < 0
        ):
            raise JournalIntegrityError("run_start contains an invalid reservation")
        if path in paths:
            raise JournalIntegrityError("run_start contains duplicate reservations")
        paths.add(path)
        reservations.append(_Reservation(path, device, inode))
    return tuple(reservations)


def _parse_start_payload(
    payload: Mapping[str, Any],
) -> Tuple[RunIdentity, bool, Tuple[_Reservation, ...]]:
    if set(payload) != {"identity", "resumable", "reservations"}:
        raise JournalIntegrityError("run_start payload has an invalid schema")
    identity_value = payload["identity"]
    if not isinstance(identity_value, dict) or set(identity_value) != {
        "run_id",
        *HASH_FIELDS,
    }:
        raise JournalIntegrityError("run_start identity has an invalid schema")
    try:
        identity = RunIdentity(**identity_value)
    except (TypeError, ValueError) as exc:
        raise JournalIntegrityError("run_start identity is invalid") from exc
    resumable = payload["resumable"]
    if not isinstance(resumable, bool):
        raise JournalIntegrityError("run_start resumable must be boolean")
    reservations = _parse_reservations(payload["reservations"])
    return identity, resumable, reservations


def _validate_stream(stream) -> JournalSnapshot:
    events = []
    expected_previous = GENESIS_HASH
    completion_seen = False
    for index, raw_line in enumerate(stream):
        row = _decode_canonical_row(raw_line, index)
        if set(row) != _ROW_FIELDS:
            raise JournalIntegrityError(
                "journal row {} has an invalid event schema".format(index)
            )
        if row["schema"] != EVENT_SCHEMA:
            raise JournalIntegrityError(
                "journal row {} has an unknown schema".format(index)
            )
        if (
            not isinstance(row["sequence"], int)
            or isinstance(row["sequence"], bool)
            or row["sequence"] != index
        ):
            raise JournalIntegrityError(
                "journal row {} has an invalid sequence".format(index)
            )
        if row["previous_hash"] != expected_previous:
            raise JournalIntegrityError(
                "journal row {} has an invalid previous hash".format(index)
            )
        event_hash = row["event_hash"]
        if not isinstance(event_hash, str) or not _SHA256_RE.fullmatch(event_hash):
            raise JournalIntegrityError(
                "journal row {} has an invalid event hash".format(index)
            )
        material = {key: value for key, value in row.items() if key != "event_hash"}
        expected_hash = hashlib.sha256(_canonical_json_bytes(material)).hexdigest()
        if event_hash != expected_hash:
            raise JournalIntegrityError(
                "journal row {} has an invalid event hash".format(index)
            )
        event_type = row["event_type"]
        if not isinstance(event_type, str) or event_type not in _ALL_EVENT_TYPES:
            raise JournalIntegrityError(
                "journal row {} has an invalid event_type".format(index)
            )
        if not isinstance(row["payload"], dict):
            raise JournalIntegrityError(
                "journal row {} payload is not an object".format(index)
            )
        if _contains_secret_material(row["payload"]):
            raise JournalIntegrityError("journal contains forbidden secret material")
        if index == 0 and event_type != "run_start":
            raise JournalIntegrityError("the first journal event must be run_start")
        if index > 0 and event_type == "run_start":
            raise JournalIntegrityError("run_start may appear only once")
        if completion_seen:
            raise JournalIntegrityError("completion must be the final journal event")
        if event_type == "completion":
            completion_seen = True
        events.append(row)
        expected_previous = event_hash

    if not events:
        raise JournalIntegrityError("journal is empty")
    identity, resumable, reservations = _parse_start_payload(events[0]["payload"])
    return JournalSnapshot(
        events=tuple(events),
        identity=identity,
        resumable=resumable,
        reservations=reservations,
        completed=completion_seen,
    )


def _validate_reservations(
    snapshot: JournalSnapshot, journal_path: Path, journal_stat: os.stat_result
) -> None:
    journal_matches = 0
    for reservation in snapshot.reservations:
        path = Path(reservation.path)
        try:
            current = os.stat(str(path), follow_symlinks=False)
        except (FileNotFoundError, OSError) as exc:
            raise JournalIntegrityError(
                "a reserved path is missing or unreadable"
            ) from exc
        if (
            not stat.S_ISREG(current.st_mode)
            or current.st_dev != reservation.device
            or current.st_ino != reservation.inode
        ):
            raise JournalIntegrityError("a reserved path no longer matches its reservation")
        if path == journal_path:
            journal_matches += 1
            if (
                current.st_dev != journal_stat.st_dev
                or current.st_ino != journal_stat.st_ino
            ):
                raise JournalIntegrityError("journal path no longer matches its reservation")
    if journal_matches != 1:
        raise JournalIntegrityError("run_start does not contain the journal reservation")


def _snapshot_from_descriptor(descriptor: int, journal_path: Path) -> JournalSnapshot:
    metadata = os.fstat(descriptor)
    if not stat.S_ISREG(metadata.st_mode):
        raise JournalIntegrityError("journal path is not a regular file")
    os.lseek(descriptor, 0, os.SEEK_SET)
    duplicate = os.dup(descriptor)
    try:
        with os.fdopen(duplicate, "rb", closefd=True) as stream:
            snapshot = _validate_stream(stream)
    finally:
        # fdopen normally closes it; this covers failures constructing the stream.
        try:
            os.close(duplicate)
        except OSError:
            pass
    _validate_reservations(snapshot, journal_path, metadata)
    return snapshot


class LiveEvidenceJournal:
    """An exclusively-owned, append-only live evidence journal."""

    def __init__(
        self,
        path: Path,
        stream,
        identity: RunIdentity,
        sequence: int,
        previous_hash: str,
        *,
        resumable: bool,
        completed: bool,
    ) -> None:
        self.path = path
        self.identity = identity
        self.resumable = resumable
        self._stream = stream
        self._sequence = sequence
        self._previous_hash = previous_hash
        self._completed = completed
        self._closed = False
        self._faulted = False
        self._mutex = threading.Lock()

    @classmethod
    def create(
        cls,
        journal_path: Pathish,
        *,
        output_paths: Iterable[Pathish],
        identity: RunIdentity,
        resumable: bool,
    ) -> "LiveEvidenceJournal":
        if not isinstance(identity, RunIdentity):
            raise TypeError("identity must be a RunIdentity")
        if not isinstance(resumable, bool):
            raise TypeError("resumable must be boolean")
        journal = _normalise_path(journal_path)
        outputs = sorted((_normalise_path(path) for path in output_paths), key=str)
        all_paths = [journal, *outputs]
        if len(set(all_paths)) != len(all_paths):
            raise PathReservationError("intended paths must be unique")

        opened = []
        current_path: Optional[Path] = None
        flags = os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_EXCL
        if hasattr(os, "O_CLOEXEC"):
            flags |= os.O_CLOEXEC
        try:
            for current_path in all_paths:
                descriptor = os.open(str(current_path), flags, 0o600)
                reservation = _reservation(current_path, descriptor)
                opened.append((current_path, descriptor, reservation))
                os.fsync(descriptor)
            _sync_directories(all_paths)
        except FileExistsError as exc:
            _cleanup_created(opened)
            raise PathReservationError(
                "intended path already exists: {}".format(current_path)
            ) from exc
        except BaseException:
            _cleanup_created(opened)
            raise

        journal_descriptor = opened[0][1]
        try:
            _acquire_lock(journal_descriptor, exclusive=True)
            for _, descriptor, _ in opened[1:]:
                os.close(descriptor)
            stream = os.fdopen(journal_descriptor, "ab", buffering=0, closefd=True)
            instance = cls(
                journal,
                stream,
                identity,
                -1,
                GENESIS_HASH,
                resumable=resumable,
                completed=False,
            )
            instance._append_internal(
                "run_start",
                {
                    "identity": identity.as_dict(),
                    "resumable": resumable,
                    "reservations": [entry.as_dict() for _, _, entry in opened],
                },
            )
            return instance
        except BaseException:
            try:
                instance.close()  # type: ignore[possibly-undefined]
            except (NameError, OSError):
                try:
                    _release_lock(journal_descriptor)
                    os.close(journal_descriptor)
                except OSError:
                    pass
            _cleanup_created(opened)
            raise

    @classmethod
    def resume(
        cls, journal_path: Pathish, *, identity: RunIdentity
    ) -> "LiveEvidenceJournal":
        if not isinstance(identity, RunIdentity):
            raise TypeError("identity must be a RunIdentity")
        path = _normalise_path(journal_path)
        flags = os.O_RDWR | os.O_APPEND
        if hasattr(os, "O_CLOEXEC"):
            flags |= os.O_CLOEXEC
        descriptor = os.open(str(path), flags)
        stream = None
        try:
            _acquire_lock(descriptor, exclusive=True)
            snapshot = _snapshot_from_descriptor(descriptor, path)
            if snapshot.completed:
                raise CompletedJournalError("completed journal cannot be resumed")
            if not snapshot.resumable:
                raise ResumeRefusedError("journal is not explicitly resumable")
            for field_name in ("run_id", *HASH_FIELDS):
                if getattr(snapshot.identity, field_name) != getattr(identity, field_name):
                    raise ResumeRefusedError(
                        "resume identity mismatch: {}".format(field_name)
                    )
            os.lseek(descriptor, 0, os.SEEK_END)
            stream = os.fdopen(descriptor, "ab", buffering=0, closefd=True)
            final = snapshot.events[-1]
            return cls(
                path,
                stream,
                identity,
                final["sequence"],
                final["event_hash"],
                resumable=True,
                completed=False,
            )
        except BaseException:
            if stream is None:
                _release_lock(descriptor)
                os.close(descriptor)
            else:
                stream.close()
            raise

    def _append_internal(
        self, event_type: str, payload: Mapping[str, Any]
    ) -> Dict[str, Any]:
        if self._closed:
            raise JournalStateError("journal is closed")
        if self._faulted:
            raise JournalStateError("journal is faulted")
        if self._completed:
            raise CompletedJournalError("completion is final; no further writes allowed")
        row = _build_row(
            self._sequence + 1,
            self._previous_hash,
            event_type,
            payload,
        )
        encoded = _canonical_json_bytes(row) + b"\n"
        view = memoryview(encoded)
        try:
            while view:
                written = self._stream.write(view)
                if written is None or written <= 0:
                    raise OSError("journal append made no progress")
                view = view[written:]
            self._stream.flush()
            os.fsync(self._stream.fileno())
        except BaseException:
            self._faulted = True
            raise
        self._sequence = row["sequence"]
        self._previous_hash = row["event_hash"]
        if event_type == "completion":
            self._completed = True
        return row

    def record(
        self, event_type: str, payload: Mapping[str, Any]
    ) -> Dict[str, Any]:
        if not isinstance(event_type, str) or event_type not in LIVE_EVENT_TYPES:
            raise ValueError("event_type is not a supported live evidence event")
        with self._mutex:
            return self._append_internal(event_type, payload)

    def complete(self, payload: Optional[Mapping[str, Any]] = None) -> Dict[str, Any]:
        with self._mutex:
            return self._append_internal("completion", payload or {})

    def close(self) -> None:
        with self._mutex:
            if self._closed:
                return
            descriptor = self._stream.fileno()
            _release_lock(descriptor)
            self._stream.close()
            self._closed = True

    def __enter__(self) -> "LiveEvidenceJournal":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        self.close()
        return False


def validate_journal(journal_path: Pathish) -> JournalSnapshot:
    """Validate a journal's canonical rows, full chain, and reservations."""

    path = _normalise_path(journal_path)
    flags = os.O_RDONLY
    if hasattr(os, "O_CLOEXEC"):
        flags |= os.O_CLOEXEC
    descriptor = os.open(str(path), flags)
    try:
        _acquire_lock(descriptor, exclusive=False)
        return _snapshot_from_descriptor(descriptor, path)
    finally:
        _release_lock(descriptor)
        os.close(descriptor)


def read_completed_journal(journal_path: Pathish) -> JournalSnapshot:
    """Return validated evidence for aggregation, but only after completion."""

    snapshot = validate_journal(journal_path)
    if not snapshot.completed:
        raise IncompleteJournalError(
            "aggregation requires a validated completed journal"
        )
    return snapshot


__all__ = [
    "CompletedJournalError",
    "IncompleteJournalError",
    "JournalIntegrityError",
    "JournalSnapshot",
    "JournalStateError",
    "LiveEvidenceJournal",
    "LiveJournalError",
    "PathReservationError",
    "ResumeRefusedError",
    "RunIdentity",
    "SecretMaterialError",
    "read_completed_journal",
    "validate_journal",
]
