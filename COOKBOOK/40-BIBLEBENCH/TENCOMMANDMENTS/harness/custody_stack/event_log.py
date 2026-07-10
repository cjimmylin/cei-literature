"""Immutable SHA-256 event chains with optional durable JSONL storage."""

from contextlib import contextmanager
import fcntl
import os
from pathlib import Path
import stat
import tempfile
import threading

from .schema import (
    CustodyError,
    Event,
    SchemaValidationError,
    ZERO_EVENT_SHA256,
    canonical_json_bytes,
    compute_event_sha256,
    strict_json_loads,
    valid_sha256,
)


class EventLogError(CustodyError, ValueError):
    """Raised when an event log is malformed or violates its chain contract."""


_PATH_MUTEXES = {}
_PATH_MUTEXES_GUARD = threading.Lock()


def _path_mutex(path):
    key = os.path.abspath(str(path))
    with _PATH_MUTEXES_GUARD:
        return _PATH_MUTEXES.setdefault(key, threading.Lock())


@contextmanager
def _writer_guard(path):
    """Serialize target writers within this process and across processes."""

    lock_path = path.with_name(".%s.lock" % path.name)
    flags = os.O_CREAT | os.O_RDWR
    flags |= getattr(os, "O_CLOEXEC", 0)
    flags |= getattr(os, "O_NOFOLLOW", 0)
    with _path_mutex(path):
        lock_fd = None
        try:
            lock_fd = os.open(str(lock_path), flags, 0o600)
            if not stat.S_ISREG(os.fstat(lock_fd).st_mode):
                raise OSError("event-log writer lock must be a regular file")
            fcntl.flock(lock_fd, fcntl.LOCK_EX)
        except OSError as exc:
            if lock_fd is not None:
                try:
                    os.close(lock_fd)
                except OSError:
                    pass
            raise EventLogError("unable to acquire event-log writer lock") from exc
        try:
            yield
        finally:
            if lock_fd is not None:
                try:
                    fcntl.flock(lock_fd, fcntl.LOCK_UN)
                except OSError:
                    pass
                try:
                    os.close(lock_fd)
                except OSError:
                    pass


def _best_effort_fsync_parent(path):
    """Attempt postcommit rename durability without reporting split-brain failure."""

    directory_fd = None
    try:
        flags = os.O_RDONLY
        flags |= getattr(os, "O_CLOEXEC", 0)
        flags |= getattr(os, "O_DIRECTORY", 0)
        directory_fd = os.open(str(path.parent), flags)
        if not stat.S_ISDIR(os.fstat(directory_fd).st_mode):
            return
        os.fsync(directory_fd)
    except OSError:
        # Replacement has already committed. Propagating a later durability error
        # would leave the caller's memory behind a target that contains the event.
        pass
    finally:
        if directory_fd is not None:
            try:
                os.close(directory_fd)
            except OSError:
                pass


def verify_chain(events):
    """Return ``True`` only for an exact zero-root, zero-indexed valid chain."""

    try:
        if type(events) not in (tuple, list):
            return False
        previous = ZERO_EVENT_SHA256
        previous_state_after = None
        chain_metadata = None
        previous_terminal = False
        for expected_index, event in enumerate(events):
            if previous_terminal:
                return False
            if type(event) is not Event:
                return False
            if event.event_index != expected_index:
                return False
            if event.previous_event_sha256 != previous:
                return False
            if (
                previous_state_after is not None
                and event.state_before_sha256 != previous_state_after
            ):
                return False
            event_metadata = (
                event.episode_id,
                event.logical_id,
                event.prompt_sha256,
                event.item_sha256,
                event.template_sha256,
            )
            if chain_metadata is None:
                chain_metadata = event_metadata
            elif event_metadata != chain_metadata:
                return False
            if compute_event_sha256(event) != event.event_sha256:
                return False
            previous = event.event_sha256
            previous_state_after = event.state_after_sha256
            previous_terminal = event.terminal
        return True
    except Exception:
        return False


class EventLog:
    """An append-only in-memory view optionally backed by canonical JSONL."""

    def __init__(self, path=None, events=None):
        concrete_path_type = type(Path())
        if path is not None and type(path) not in (str, concrete_path_type):
            raise EventLogError("event log path must be a string or pathlib Path")
        if path is not None and events is not None:
            raise EventLogError("explicit events cannot be combined with a JSONL path")
        self._path = None if path is None else Path(path)
        self._events = []
        self._append_lock = threading.Lock()
        if events is not None:
            if type(events) not in (tuple, list):
                raise EventLogError("initial events must be an exact list or tuple")
            self._events = list(events)
            if not verify_chain(self._events):
                raise EventLogError("initial events do not form a valid chain")
        if self._path is not None and self._path.exists():
            if events is not None:
                raise EventLogError("cannot combine explicit events with an existing path")
            self._events = self._load_path(self._path)

    @staticmethod
    def _load_path(path):
        loaded = []
        try:
            with path.open("rb") as stream:
                for line_number, raw_line in enumerate(stream, start=1):
                    if not raw_line.endswith(b"\n") or raw_line == b"\n":
                        raise EventLogError(
                            "event log line %d is incomplete or blank" % line_number
                        )
                    try:
                        text = raw_line[:-1].decode("utf-8", errors="strict")
                        payload = strict_json_loads(text)
                        event = Event.from_dict(payload)
                    except (UnicodeError, SchemaValidationError) as exc:
                        raise EventLogError(
                            "event log line %d is invalid" % line_number
                        ) from exc
                    if canonical_json_bytes(event.to_dict()) != raw_line[:-1]:
                        raise EventLogError(
                            "event log line %d is not canonical JSON" % line_number
                        )
                    loaded.append(event)
        except EventLogError:
            raise
        except OSError as exc:
            raise EventLogError("unable to read event log") from exc
        if not verify_chain(loaded):
            raise EventLogError("event log chain verification failed")
        return loaded

    @property
    def path(self):
        return self._path

    @property
    def events(self):
        return tuple(self._events)

    @property
    def next_index(self):
        return len(self._events)

    @property
    def previous_event_sha256(self):
        return self._events[-1].event_sha256 if self._events else ZERO_EVENT_SHA256

    def live_head(self):
        """Return the current durable/in-memory ``(count, head_sha256)`` pair."""

        with self._append_lock:
            if self._path is None:
                events = tuple(self._events)
            else:
                with _writer_guard(self._path):
                    events = (
                        tuple(self._load_path(self._path))
                        if self._path.exists()
                        else ()
                    )
            head = events[-1].event_sha256 if events else ZERO_EVENT_SHA256
            return len(events), head

    def append(self, event, expected_generation=None):
        with self._append_lock:
            if self._path is None:
                return self._append_locked(event, expected_generation)
            with _writer_guard(self._path):
                return self._append_locked(event, expected_generation)

    def _append_locked(self, event, expected_generation):
        """Durably append, then and only then expose the event in memory."""

        if type(event) is not Event:
            raise EventLogError("only Event instances may be appended")
        if expected_generation is not None:
            if (
                type(expected_generation) is not tuple
                or len(expected_generation) != 2
                or type(expected_generation[0]) is not int
                or expected_generation[0] < 0
                or not valid_sha256(expected_generation[1])
            ):
                raise EventLogError("expected generation must be exact (count, head)")
            current_generation = (
                len(self._events),
                self._events[-1].event_sha256
                if self._events
                else ZERO_EVENT_SHA256,
            )
            if expected_generation != current_generation:
                raise EventLogError("event log generation changed before append")
        proposed = self._events + [event]
        if not verify_chain(proposed):
            raise EventLogError("event does not continue the verified chain")
        if self._path is not None:
            line = canonical_json_bytes(event.to_dict()) + b"\n"
            expected_prefix = b"".join(
                canonical_json_bytes(existing.to_dict()) + b"\n"
                for existing in self._events
            )
            try:
                if self._path.exists():
                    with self._path.open("rb") as existing_stream:
                        actual_prefix = existing_stream.read()
                else:
                    actual_prefix = b""
            except OSError as exc:
                raise EventLogError("unable to validate current event-log bytes") from exc
            if actual_prefix != expected_prefix:
                raise EventLogError("event log changed since this writer loaded it")

            candidate = expected_prefix + line
            staging = None
            staging_fd = None
            stream = None
            replaced = False
            try:
                staging_fd, staging_name = tempfile.mkstemp(
                    prefix=".%s." % self._path.name,
                    suffix=".pending",
                    dir=str(self._path.parent),
                )
                staging = Path(staging_name)
                stream = os.fdopen(staging_fd, "w+b")
                staging_fd = None
                written = stream.write(candidate)
                if written != len(candidate):
                    raise OSError("short event-log write")
                stream.flush()
                os.fsync(stream.fileno())
                os.replace(staging, self._path)
                replaced = True
                _best_effort_fsync_parent(self._path)
            except BaseException:
                if stream is not None and not replaced:
                    try:
                        stream.seek(0)
                        stream.truncate(0)
                        stream.flush()
                    except OSError:
                        pass
                if stream is not None:
                    try:
                        stream.close()
                    except OSError:
                        pass
                if staging_fd is not None:
                    try:
                        os.close(staging_fd)
                    except OSError:
                        pass
                if not replaced:
                    try:
                        if staging is not None:
                            staging.unlink()
                    except OSError:
                        pass
                raise
            else:
                try:
                    stream.close()
                except OSError:
                    # The staged bytes were already fsynced and atomically committed.
                    pass
        self._events.append(event)


__all__ = ["EventLog", "EventLogError", "verify_chain"]
