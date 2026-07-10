"""Immutable SHA-256 event chains with optional durable JSONL storage."""

from contextlib import contextmanager
import fcntl
import os
from pathlib import Path
import secrets
import stat
import threading

from .schema import (
    CustodyError,
    Event,
    MAX_EVENT_LOG_BYTES,
    MAX_JSON_BYTES,
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
    key = str(path)
    with _PATH_MUTEXES_GUARD:
        return _PATH_MUTEXES.setdefault(key, threading.Lock())


def _close_best_effort(fd):
    if fd is None:
        return
    try:
        os.close(fd)
    except BaseException:
        pass


def _bound_target(path):
    try:
        raw = Path(path)
        if not raw.name:
            raise EventLogError("event log path must name a target file")
        parent = raw.parent.resolve(strict=True)
        parent_stat = parent.stat()
    except EventLogError:
        raise
    except (OSError, RuntimeError) as exc:
        raise EventLogError("event log parent directory must already exist") from exc
    if not stat.S_ISDIR(parent_stat.st_mode):
        raise EventLogError("event log parent must be a directory")
    return parent / raw.name, (parent_stat.st_dev, parent_stat.st_ino)


def _open_bound_parent(path, expected_identity):
    flags = os.O_RDONLY
    flags |= getattr(os, "O_CLOEXEC", 0)
    flags |= getattr(os, "O_DIRECTORY", 0)
    flags |= getattr(os, "O_NOFOLLOW", 0)
    fd = os.open(str(path.parent), flags)
    try:
        opened = os.fstat(fd)
        if not stat.S_ISDIR(opened.st_mode):
            raise OSError("event-log parent is not a directory")
        if (opened.st_dev, opened.st_ino) != expected_identity:
            raise OSError("event-log parent identity changed")
        return fd
    except BaseException:
        _close_best_effort(fd)
        raise


def _read_all(fd):
    try:
        chunks = []
        total = 0
        while True:
            remaining = MAX_EVENT_LOG_BYTES - total
            chunk = os.read(fd, min(1024 * 1024, remaining + 1))
            if not chunk:
                return b"".join(chunks)
            if len(chunk) > remaining:
                raise EventLogError("event log exceeds maximum event-log byte size")
            chunks.append(chunk)
            total += len(chunk)
    except EventLogError:
        raise
    except (MemoryError, RecursionError) as exc:
        raise EventLogError("event-log read exceeds bounded resources") from exc


def _canonical_event_line(event):
    try:
        return canonical_json_bytes(event.to_dict()) + b"\n"
    except (SchemaValidationError, MemoryError, RecursionError) as exc:
        raise EventLogError("unable to encode bounded event-log line") from exc


def _bounded_event_log_size(events):
    """Return canonical JSONL byte size while enforcing the episode budget."""

    try:
        total = 0
        for event in events:
            line_size = len(_canonical_event_line(event))
            if line_size > MAX_EVENT_LOG_BYTES - total:
                raise EventLogError("event log exceeds maximum event-log byte size")
            total += line_size
        return total
    except EventLogError:
        raise
    except (SchemaValidationError, MemoryError, RecursionError) as exc:
        raise EventLogError("unable to size bounded event log") from exc


def _target_bytes(parent_fd, target_name):
    flags = os.O_RDONLY
    flags |= getattr(os, "O_CLOEXEC", 0)
    flags |= getattr(os, "O_NOFOLLOW", 0)
    flags |= getattr(os, "O_NONBLOCK", 0)
    try:
        fd = os.open(target_name, flags, dir_fd=parent_fd)
    except FileNotFoundError:
        return None
    except OSError as exc:
        raise EventLogError("event-log target is unsafe or unreadable") from exc
    try:
        target_stat = os.fstat(fd)
        if not stat.S_ISREG(target_stat.st_mode) or target_stat.st_nlink != 1:
            raise EventLogError(
                "event-log target must be a regular single-link file"
            )
        try:
            return _read_all(fd)
        except OSError as exc:
            raise EventLogError("unable to read event log") from exc
    finally:
        _close_best_effort(fd)


def _name_matches_identity(parent_fd, name, identity):
    try:
        current = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except (FileNotFoundError, OSError):
        return False
    return (current.st_dev, current.st_ino) == identity


def _unlink_if_owned(parent_fd, name, identity):
    if not _name_matches_identity(parent_fd, name, identity):
        return
    try:
        os.unlink(name, dir_fd=parent_fd)
    except BaseException:
        pass


def _create_staging(parent_fd, target_name):
    flags = os.O_CREAT | os.O_EXCL | os.O_RDWR
    flags |= getattr(os, "O_CLOEXEC", 0)
    flags |= getattr(os, "O_NOFOLLOW", 0)
    for _attempt in range(128):
        name = ".%s.%s.pending" % (target_name, secrets.token_hex(12))
        try:
            fd = os.open(name, flags, 0o600, dir_fd=parent_fd)
        except FileExistsError:
            continue
        identity = None
        try:
            opened = os.fstat(fd)
            identity = (opened.st_dev, opened.st_ino)
            if not stat.S_ISREG(opened.st_mode) or opened.st_nlink != 1:
                raise EventLogError("event-log staging target is unsafe")
            return fd, name, identity
        except BaseException:
            try:
                if identity is None:
                    try:
                        opened = os.stat(fd)
                        identity = (opened.st_dev, opened.st_ino)
                    except BaseException:
                        pass
                if identity is not None:
                    try:
                        _unlink_if_owned(parent_fd, name, identity)
                    except BaseException:
                        pass
            finally:
                _close_best_effort(fd)
            raise
    raise EventLogError("unable to allocate exclusive event-log staging file")


@contextmanager
def _writer_guard(path, parent_identity):
    """Serialize target writers within this process and across processes."""

    lock_name = ".%s.lock" % path.name
    flags = os.O_CREAT | os.O_RDWR
    flags |= getattr(os, "O_CLOEXEC", 0)
    flags |= getattr(os, "O_NOFOLLOW", 0)
    with _path_mutex(path):
        parent_fd = None
        lock_fd = None
        try:
            parent_fd = _open_bound_parent(path, parent_identity)
            lock_fd = os.open(lock_name, flags, 0o600, dir_fd=parent_fd)
            lock_stat = os.fstat(lock_fd)
            if not stat.S_ISREG(lock_stat.st_mode) or lock_stat.st_nlink != 1:
                raise OSError(
                    "event-log writer lock must be a regular single-link file"
                )
            fcntl.flock(lock_fd, fcntl.LOCK_EX)
        except OSError as exc:
            if lock_fd is not None:
                try:
                    fcntl.flock(lock_fd, fcntl.LOCK_UN)
                except BaseException:
                    pass
            _close_best_effort(lock_fd)
            _close_best_effort(parent_fd)
            raise EventLogError("unable to acquire event-log writer lock") from exc
        except BaseException:
            if lock_fd is not None:
                try:
                    fcntl.flock(lock_fd, fcntl.LOCK_UN)
                except BaseException:
                    pass
            _close_best_effort(lock_fd)
            _close_best_effort(parent_fd)
            raise
        try:
            yield parent_fd
        finally:
            if lock_fd is not None:
                try:
                    fcntl.flock(lock_fd, fcntl.LOCK_UN)
                except BaseException:
                    pass
            _close_best_effort(lock_fd)
            _close_best_effort(parent_fd)


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
    except BaseException:
        # Replacement has already committed. Propagating a later durability error
        # would leave the caller's memory behind a target that contains the event.
        pass
    finally:
        if directory_fd is not None:
            try:
                os.close(directory_fd)
            except BaseException:
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
        if path is None:
            self._path = None
            self._parent_identity = None
        else:
            self._path, self._parent_identity = _bound_target(path)
        self._events = []
        self._append_lock = threading.Lock()
        if events is not None:
            if type(events) not in (tuple, list):
                raise EventLogError("initial events must be an exact list or tuple")
            self._events = list(events)
            if not verify_chain(self._events):
                raise EventLogError("initial events do not form a valid chain")
            _bounded_event_log_size(self._events)
        if self._path is not None:
            if events is not None:
                raise EventLogError("cannot combine explicit events with a JSONL path")
            parent_fd = None
            try:
                parent_fd = _open_bound_parent(self._path, self._parent_identity)
                raw = _target_bytes(parent_fd, self._path.name)
            except EventLogError:
                raise
            except OSError as exc:
                raise EventLogError("unable to inspect event-log target") from exc
            finally:
                _close_best_effort(parent_fd)
            if raw is not None:
                self._events = self._load_bytes(raw)

    @staticmethod
    def _load_bytes(raw):
        if type(raw) is not bytes:
            raise EventLogError("event log input must be exact bytes")
        if len(raw) > MAX_EVENT_LOG_BYTES:
            raise EventLogError("event log exceeds maximum event-log byte size")
        try:
            loaded = []
            offset = 0
            line_number = 1
            while offset < len(raw):
                newline = raw.find(b"\n", offset)
                line_end = len(raw) if newline < 0 else newline
                line_size = line_end - offset
                if line_size > MAX_JSON_BYTES:
                    raise EventLogError(
                        "event log line %d exceeds maximum JSON byte size"
                        % line_number
                    )
                if newline < 0 or line_size == 0:
                    raise EventLogError(
                        "event log line %d is incomplete or blank" % line_number
                    )
                raw_line = raw[offset:newline]
                try:
                    text = raw_line.decode("utf-8", errors="strict")
                    payload = strict_json_loads(text)
                    event = Event.from_dict(payload)
                    canonical = canonical_json_bytes(event.to_dict())
                except (UnicodeError, SchemaValidationError) as exc:
                    raise EventLogError(
                        "event log line %d is invalid" % line_number
                    ) from exc
                except (MemoryError, RecursionError) as exc:
                    raise EventLogError(
                        "event log line %d exceeds bounded resources" % line_number
                    ) from exc
                if canonical != raw_line:
                    raise EventLogError(
                        "event log line %d is not canonical JSON" % line_number
                    )
                loaded.append(event)
                offset = newline + 1
                line_number += 1
            if not verify_chain(loaded):
                raise EventLogError("event log chain verification failed")
            return loaded
        except EventLogError:
            raise
        except (MemoryError, RecursionError) as exc:
            raise EventLogError("event-log load exceeds bounded resources") from exc

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
                with _writer_guard(self._path, self._parent_identity) as parent_fd:
                    raw = _target_bytes(parent_fd, self._path.name)
                    events = () if raw is None else tuple(self._load_bytes(raw))
            head = events[-1].event_sha256 if events else ZERO_EVENT_SHA256
            return len(events), head

    def append(self, event, expected_generation=None):
        with self._append_lock:
            if self._path is None:
                return self._append_locked(event, expected_generation, None)
            with _writer_guard(self._path, self._parent_identity) as parent_fd:
                return self._append_locked(event, expected_generation, parent_fd)

    def _append_locked(self, event, expected_generation, parent_fd):
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
        line = _canonical_event_line(event)
        current_size = _bounded_event_log_size(self._events)
        if len(line) > MAX_EVENT_LOG_BYTES - current_size:
            raise EventLogError("event log exceeds maximum event-log byte size")
        deferred_error = None
        deferred_traceback = None
        if self._path is not None:
            expected_prefix = b"".join(
                _canonical_event_line(existing) for existing in self._events
            )
            actual_target = _target_bytes(parent_fd, self._path.name)
            actual_prefix = b"" if actual_target is None else actual_target
            if actual_prefix != expected_prefix:
                raise EventLogError("event log changed since this writer loaded it")

            candidate = expected_prefix + line
            staging_fd = None
            staging_name = None
            staging_identity = None
            stream = None
            committed = False
            try:
                staging_fd, staging_name, staging_identity = _create_staging(
                    parent_fd, self._path.name
                )
                stream = os.fdopen(staging_fd, "w+b")
                staging_fd = None
                written = stream.write(candidate)
                if written != len(candidate):
                    raise OSError("short event-log write")
                stream.flush()
                os.fsync(stream.fileno())
                rechecked = _target_bytes(parent_fd, self._path.name)
                rechecked_prefix = b"" if rechecked is None else rechecked
                if rechecked_prefix != expected_prefix:
                    raise EventLogError(
                        "event log changed before atomic replacement"
                    )
                try:
                    os.replace(
                        staging_name,
                        self._path.name,
                        src_dir_fd=parent_fd,
                        dst_dir_fd=parent_fd,
                    )
                except BaseException as exc:
                    try:
                        observed = _target_bytes(parent_fd, self._path.name)
                    except BaseException as classification_exc:
                        _close_best_effort(staging_fd)
                        if stream is not None:
                            try:
                                stream.close()
                            except BaseException:
                                pass
                        if staging_name is not None:
                            _unlink_if_owned(
                                parent_fd, staging_name, staging_identity
                            )
                        raise EventLogError(
                            "ambiguous event-log replacement outcome"
                        ) from classification_exc
                    observed_bytes = b"" if observed is None else observed
                    if observed is not None and observed_bytes == candidate:
                        committed = True
                        deferred_error = exc
                        deferred_traceback = exc.__traceback__
                    elif observed_bytes == expected_prefix:
                        if (
                            stream is not None
                            and staging_name is not None
                            and _name_matches_identity(
                                parent_fd, staging_name, staging_identity
                            )
                        ):
                            try:
                                stream.seek(0)
                                stream.truncate(0)
                                stream.flush()
                            except BaseException:
                                pass
                        if stream is not None:
                            try:
                                stream.close()
                            except BaseException:
                                pass
                            stream = None
                        _close_best_effort(staging_fd)
                        staging_fd = None
                        if staging_name is not None:
                            _unlink_if_owned(
                                parent_fd, staging_name, staging_identity
                            )
                        raise
                    else:
                        if stream is not None:
                            try:
                                stream.close()
                            except BaseException:
                                pass
                            stream = None
                        _close_best_effort(staging_fd)
                        staging_fd = None
                        if staging_name is not None:
                            _unlink_if_owned(
                                parent_fd, staging_name, staging_identity
                            )
                        raise EventLogError(
                            "ambiguous event-log replacement outcome"
                        ) from exc
                else:
                    committed = True
                if committed:
                    _best_effort_fsync_parent(self._path)
            except BaseException:
                if (
                    not committed
                    and stream is not None
                    and staging_name is not None
                    and _name_matches_identity(
                        parent_fd, staging_name, staging_identity
                    )
                ):
                    try:
                        stream.seek(0)
                        stream.truncate(0)
                        stream.flush()
                    except BaseException:
                        pass
                if stream is not None:
                    try:
                        stream.close()
                    except BaseException:
                        pass
                    stream = None
                if staging_fd is not None:
                    _close_best_effort(staging_fd)
                    staging_fd = None
                if not committed and staging_name is not None:
                    _unlink_if_owned(parent_fd, staging_name, staging_identity)
                raise
            else:
                if stream is not None:
                    try:
                        stream.close()
                    except BaseException:
                        # The staged bytes were already fsynced and committed.
                        pass
                _close_best_effort(staging_fd)
            finally:
                if committed:
                    try:
                        self._events = proposed
                    except BaseException:
                        # A one-shot interruption at the publication line must not
                        # leave memory behind an already replaced durable target.
                        self._events = proposed
                        raise
        else:
            self._events = proposed
        if deferred_error is not None:
            raise deferred_error.with_traceback(deferred_traceback)

    def _committed_event(self, event, expected_generation):
        """Return whether this exact append committed despite an interruption."""

        with self._append_lock:
            if self._path is not None:
                try:
                    with _writer_guard(
                        self._path, self._parent_identity
                    ) as parent_fd:
                        raw = _target_bytes(parent_fd, self._path.name)
                        durable = [] if raw is None else self._load_bytes(raw)
                except (EventLogError, MemoryError, RecursionError):
                    return False
                self._events = durable
            expected_index = expected_generation[0]
            return (
                expected_index < len(self._events)
                and self._events[expected_index].event_sha256 == event.event_sha256
            )


__all__ = ["EventLog", "EventLogError", "verify_chain"]
