from __future__ import annotations

import ctypes
import errno
import math
import os
from pathlib import Path
import re
import stat
import sys
import threading
import uuid
from typing import Any

from .contracts import Json, canonical_json_bytes


__all__ = (
    "ArtifactStore",
    "assert_actor_payload_safe",
    "assert_actor_envelope_safe",
    "assert_judge_envelope_safe",
    "validate_artifact_tree",
)


_DIRECTORY_FLAGS = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
_NOFOLLOW = getattr(os, "O_NOFOLLOW", 0)
_UMASK_LOCK = threading.Lock()
_MAX_VISIBLE_DEPTH = 128
_VISIBLE_ERROR = "unsafe model-visible payload"
_ACTOR_FORBIDDEN_TERMS = frozenset(
    {
        "private",
        "gold",
        "ground_truth",
        "expected_label",
        "judge_id",
        "actor_model",
        "model_identity",
        "canary",
        "api_key",
        "authorization",
        "authentication",
        "auth",
        "bearer",
        "credential",
        "secret",
        "token",
        "environment",
        "env",
        "env_dump",
        "rubric",
    }
)
_JUDGE_FORBIDDEN_TERMS = frozenset(
    {
        "private",
        "gold",
        "ground_truth",
        "expected_label",
        "judge_id",
        "actor",
        "actor_model",
        "model_identity",
        "provider",
        "route",
        "cue",
        "condition",
        "canary",
        "api_key",
        "authorization",
        "authentication",
        "auth",
        "bearer",
        "credential",
        "secret",
        "environment",
        "env",
        "env_dump",
    }
)
_NON_ALNUM = re.compile(r"[^a-z0-9]+")
_CAMEL_BOUNDARY = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")
# These are standalone normalized protocol aliases, not arbitrary "auth" prefixes.
_AUTH_ALIAS_TOKENS = frozenset({"auth", "oauth", "authn", "authz", "preauth"})
_CREDENTIAL_SHAPE = re.compile(
    r"(?:"
    r"\bsk-[A-Za-z0-9_-]{6,}"
    r"|\b(?i:basic|digest)\s+[A-Za-z0-9+/=_-]{6,}"
    r"|(?<![A-Za-z0-9_])gh[pousr]_[A-Za-z0-9]{20,}(?![A-Za-z0-9])"
    r"|(?<![A-Za-z0-9_])github_pat_[A-Za-z0-9_]{20,}(?![A-Za-z0-9])"
    r"|(?<![A-Z0-9])(?:AKIA|ASIA)[A-Z0-9]{16}(?![A-Z0-9])"
    r"|(?<![A-Za-z0-9_-])(?:[A-Za-z0-9_-]{4,}\.){2}"
    r"[A-Za-z0-9_-]{4,}(?![A-Za-z0-9_-])"
    r"|(?<![A-Za-z0-9_-])xox[bpa]-[A-Za-z0-9-]{8,}"
    r"|(?<![A-Za-z0-9_-])xapp-[A-Za-z0-9-]{8,}"
    r"|(?<![A-Za-z0-9_])AIza[A-Za-z0-9_-]{30,}"
    r"|(?<![A-Za-z0-9_])(?:sk|rk)_live_[A-Za-z0-9]{16,}"
    r"|(?<![A-Za-z0-9_-])glpat-[A-Za-z0-9_-]{16,}"
    r"|(?<![A-Za-z0-9_])hf_[A-Za-z0-9]{20,}"
    r"|(?<![A-Za-z0-9_])npm_[A-Za-z0-9_-]{20,}"
    r")"
)
_ENV_ASSIGNMENT = re.compile(r"(?m)^[ \t]*[A-Z][A-Z0-9_]{1,63}=")


class ArtifactDurabilityError(OSError):
    """Publication succeeded, but its directory durability sync did not."""


def _normalized_policy_text(value: str) -> tuple[str, str]:
    separated = _CAMEL_BOUNDARY.sub("_", value)
    normalized = _NON_ALNUM.sub("_", separated.casefold()).strip("_")
    return normalized, normalized.replace("_", "")


def _string_is_forbidden(
    value: str,
    forbidden_terms: frozenset[str],
    *,
    allow_token_count: bool,
) -> bool:
    normalized, compact = _normalized_policy_text(value)
    normalized_parts = frozenset(normalized.split("_"))
    allowed_token_count = allow_token_count and normalized == "token_count"
    for term in forbidden_terms:
        if term == "token" and allowed_token_count:
            continue
        if term == "auth":
            if _AUTH_ALIAS_TOKENS & normalized_parts:
                return True
            continue
        if term == "env":
            if normalized == term or term in normalized_parts:
                return True
            continue
        term_compact = term.replace("_", "")
        if term in normalized or term_compact in compact:
            return True
    if _CREDENTIAL_SHAPE.search(value):
        return True
    return bool(_ENV_ASSIGNMENT.search(value))


def _inspect_visible_tree(
    value: Any,
    forbidden_terms: frozenset[str],
    *,
    active: set[int],
    depth: int,
) -> None:
    if value is None or type(value) in {bool, int}:
        return
    if type(value) is float:
        if math.isfinite(value):
            return
        raise ValueError(_VISIBLE_ERROR)
    if type(value) is str:
        if (
            any(0xD800 <= ord(character) <= 0xDFFF for character in value)
            or _string_is_forbidden(
                value,
                forbidden_terms,
                allow_token_count=True,
            )
        ):
            raise ValueError(_VISIBLE_ERROR)
        return
    if type(value) not in {dict, list}:
        raise ValueError(_VISIBLE_ERROR)
    if depth >= _MAX_VISIBLE_DEPTH or id(value) in active:
        raise ValueError(_VISIBLE_ERROR)

    active.add(id(value))
    try:
        if type(value) is dict:
            for key, child in value.items():
                if type(key) is not str or _string_is_forbidden(
                    key,
                    forbidden_terms,
                    allow_token_count=True,
                ) or any(
                    0xD800 <= ord(character) <= 0xDFFF for character in key
                ):
                    raise ValueError(_VISIBLE_ERROR)
                _inspect_visible_tree(
                    child,
                    forbidden_terms,
                    active=active,
                    depth=depth + 1,
                )
        else:
            for child in value:
                _inspect_visible_tree(
                    child,
                    forbidden_terms,
                    active=active,
                    depth=depth + 1,
                )
    finally:
        active.discard(id(value))


def assert_actor_payload_safe(payload: Any) -> None:
    _inspect_visible_tree(
        payload,
        _ACTOR_FORBIDDEN_TERMS,
        active=set(),
        depth=0,
    )


def assert_actor_envelope_safe(envelope: Any) -> None:
    if (
        type(envelope) is not dict
        or set(envelope) != {"turns", "tool_contracts"}
        or type(envelope["turns"]) is not list
        or type(envelope["tool_contracts"]) is not dict
    ):
        raise ValueError(_VISIBLE_ERROR)
    assert_actor_payload_safe(envelope)


def _assert_safe_opaque_string(value: Any) -> None:
    if (
        type(value) is not str
        or not value.strip()
        or any(0xD800 <= ord(character) <= 0xDFFF for character in value)
        or _string_is_forbidden(
            value,
            _JUDGE_FORBIDDEN_TERMS,
            allow_token_count=False,
        )
        or _CREDENTIAL_SHAPE.search(value)
        or _ENV_ASSIGNMENT.search(value)
    ):
        raise ValueError(_VISIBLE_ERROR)


def assert_judge_envelope_safe(envelope: Any) -> None:
    if (
        type(envelope) is not dict
        or set(envelope) != {"episode_token", "rubric_version", "events"}
        or type(envelope["events"]) is not list
    ):
        raise ValueError(_VISIBLE_ERROR)
    _assert_safe_opaque_string(envelope["episode_token"])
    _assert_safe_opaque_string(envelope["rubric_version"])
    _inspect_visible_tree(
        envelope["events"],
        _JUDGE_FORBIDDEN_TERMS,
        active=set(),
        depth=0,
    )


def _safe_root_fd(root: Path) -> tuple[int, tuple[int, int]]:
    descriptor: int | None = None
    try:
        before = os.lstat(root)
        if stat.S_ISLNK(before.st_mode) or not stat.S_ISDIR(before.st_mode):
            raise ValueError("artifact root must be a real directory")
        descriptor = os.open(root, _DIRECTORY_FLAGS | _NOFOLLOW)
        after = os.fstat(descriptor)
    except ValueError:
        if descriptor is not None:
            os.close(descriptor)
        raise
    except OSError as exc:
        if descriptor is not None:
            os.close(descriptor)
        raise ValueError("artifact root must be a real directory") from exc
    identity = (after.st_dev, after.st_ino)
    if identity != (before.st_dev, before.st_ino) or not stat.S_ISDIR(after.st_mode):
        os.close(descriptor)
        raise ValueError("artifact root must be a real directory")
    return descriptor, identity


def _path_parts(relative: Any) -> tuple[str, ...]:
    if type(relative) is not str or not relative or "\x00" in relative:
        raise ValueError("unsafe artifact path")
    try:
        relative.encode("utf-8", errors="strict")
    except UnicodeError as exc:
        raise ValueError("unsafe artifact path") from exc
    if relative.startswith("/") or relative.startswith("\\"):
        raise ValueError("unsafe artifact path")
    if len(relative) >= 2 and relative[0].isalpha() and relative[1] == ":":
        raise ValueError("unsafe artifact path")
    if "\\" in relative:
        raise ValueError("unsafe artifact path")
    parts = tuple(relative.split("/"))
    if any(not part or part in {".", ".."} for part in parts):
        raise ValueError("unsafe artifact path")
    return parts


def _set_process_umask(mode: int) -> int:
    return os.umask(mode)


def _mkdir_private(component: str, parent_fd: int) -> None:
    # umask is process-global; 077 keeps unrelated concurrent creations private.
    # The lock serializes stores, and the caller documents residual mode narrowing.
    with _UMASK_LOCK:
        previous_umask = _set_process_umask(0o077)
        try:
            os.mkdir(component, mode=0o700, dir_fd=parent_fd)
        finally:
            _set_process_umask(previous_umask)


def _open_parent(root_fd: int, parts: tuple[str, ...]) -> int:
    try:
        current = os.dup(root_fd)
    except OSError as exc:
        raise ValueError("unsafe artifact path") from exc
    try:
        for component in parts[:-1]:
            needs_directory_sync = False
            created_identity: tuple[int, int] | None = None
            try:
                child = os.open(
                    component,
                    _DIRECTORY_FLAGS | _NOFOLLOW,
                    dir_fd=current,
                )
            except FileNotFoundError:
                needs_directory_sync = True
                try:
                    _mkdir_private(component, current)
                except FileExistsError:
                    pass
                else:
                    created = os.stat(
                        component,
                        dir_fd=current,
                        follow_symlinks=False,
                    )
                    if stat.S_ISLNK(created.st_mode) or not stat.S_ISDIR(
                        created.st_mode
                    ):
                        raise ValueError("unsafe artifact path")
                    created_identity = (created.st_dev, created.st_ino)
                child = os.open(
                    component,
                    _DIRECTORY_FLAGS | _NOFOLLOW,
                    dir_fd=current,
                )
            try:
                child_stat = os.fstat(child)
                if not stat.S_ISDIR(child_stat.st_mode):
                    raise ValueError("unsafe artifact path")
                if created_identity is not None:
                    if (child_stat.st_dev, child_stat.st_ino) != created_identity:
                        raise ValueError("unsafe artifact path")
                    os.fchmod(child, 0o700)
                    child_stat = os.fstat(child)
                    current_entry = os.stat(
                        component,
                        dir_fd=current,
                        follow_symlinks=False,
                    )
                    if (
                        not stat.S_ISDIR(child_stat.st_mode)
                        or stat.S_IMODE(child_stat.st_mode) != 0o700
                        or (child_stat.st_dev, child_stat.st_ino)
                        != created_identity
                        or stat.S_ISLNK(current_entry.st_mode)
                        or not stat.S_ISDIR(current_entry.st_mode)
                        or (current_entry.st_dev, current_entry.st_ino)
                        != created_identity
                    ):
                        raise ValueError("unsafe artifact path")
                if needs_directory_sync:
                    os.fsync(child)
                    os.fsync(current)
            except (OSError, ValueError):
                os.close(child)
                raise
            os.close(current)
            current = child
        return current
    except (ValueError, FileExistsError):
        os.close(current)
        raise
    except OSError as exc:
        os.close(current)
        raise ValueError("unsafe artifact path") from exc


def _raise_publish_error(error_number: int) -> None:
    if error_number == errno.EEXIST:
        raise FileExistsError("artifact target already exists")
    raise OSError(error_number, "atomic artifact publication failed")


def _native_publish_noreplace(parent_fd: int, temporary: str, target: str) -> None:
    library = ctypes.CDLL(None, use_errno=True)
    source = temporary.encode("utf-8")
    destination = target.encode("utf-8")
    if sys.platform == "darwin":
        try:
            operation = library.renameatx_np
        except AttributeError as exc:
            raise OSError(
                errno.ENOTSUP, "atomic no-replace publication unavailable"
            ) from exc
        operation.argtypes = [
            ctypes.c_int,
            ctypes.c_char_p,
            ctypes.c_int,
            ctypes.c_char_p,
            ctypes.c_uint,
        ]
        operation.restype = ctypes.c_int
        result = operation(parent_fd, source, parent_fd, destination, 0x00000004)
    elif sys.platform.startswith("linux"):
        try:
            operation = library.renameat2
        except AttributeError as exc:
            raise OSError(errno.ENOTSUP, "atomic no-replace publication unavailable") from exc
        operation.argtypes = [
            ctypes.c_int,
            ctypes.c_char_p,
            ctypes.c_int,
            ctypes.c_char_p,
            ctypes.c_uint,
        ]
        operation.restype = ctypes.c_int
        result = operation(parent_fd, source, parent_fd, destination, 1)
    else:
        raise OSError(errno.ENOTSUP, "atomic no-replace publication unavailable")
    if result != 0:
        _raise_publish_error(ctypes.get_errno())


def _write_all(descriptor: int, data: bytes) -> None:
    view = memoryview(data)
    written = 0
    while written < len(view):
        count = os.write(descriptor, view[written:])
        if count <= 0:
            raise OSError(errno.EIO, "artifact write made no progress")
        written += count


def _assert_target_absent(parent_fd: int, target: str) -> None:
    try:
        target_stat = os.stat(target, dir_fd=parent_fd, follow_symlinks=False)
    except FileNotFoundError:
        return
    except OSError as exc:
        raise ValueError("unsafe artifact path") from exc
    if stat.S_ISLNK(target_stat.st_mode):
        raise ValueError("unsafe artifact path")
    raise FileExistsError("artifact target already exists")


def _close_owned_descriptor(
    descriptor: int,
    expected_identity: tuple[int, int],
    error_message: str,
) -> None:
    try:
        os.close(descriptor)
    except OSError as exc:
        try:
            current = os.fstat(descriptor)
        except OSError:
            pass
        else:
            if (current.st_dev, current.st_ino) == expected_identity:
                try:
                    os.close(descriptor)
                except OSError:
                    pass
        raise OSError(
            exc.errno or errno.EIO, error_message
        ) from exc


def _close_staged_file(
    descriptor: int, expected_identity: tuple[int, int]
) -> None:
    _close_owned_descriptor(
        descriptor,
        expected_identity,
        "artifact staging close failed",
    )


class ArtifactStore:
    def __init__(self, root: Path) -> None:
        self.root = Path(root)
        self._root_fd, self._root_identity = _safe_root_fd(self.root)

    def __del__(self) -> None:
        descriptor = getattr(self, "_root_fd", None)
        if descriptor is not None:
            try:
                os.close(descriptor)
            except OSError:
                pass
            self._root_fd = None

    def _assert_root_identity(self) -> None:
        try:
            current = os.lstat(self.root)
        except OSError as exc:
            raise ValueError("artifact root identity changed") from exc
        if (
            stat.S_ISLNK(current.st_mode)
            or not stat.S_ISDIR(current.st_mode)
            or (current.st_dev, current.st_ino) != self._root_identity
        ):
            raise ValueError("artifact root identity changed")

    def write(self, relative: str, payload: dict[str, Json]) -> Path:
        parts = _path_parts(relative)
        if type(payload) is not dict:
            raise ValueError("artifact payload must be a strict JSON object")
        serialized = canonical_json_bytes(payload) + b"\n"
        self._assert_root_identity()
        parent_fd = _open_parent(self._root_fd, parts)
        try:
            parent_stat = os.fstat(parent_fd)
        except OSError as exc:
            os.close(parent_fd)
            raise ValueError("unsafe artifact path") from exc
        parent_identity = (parent_stat.st_dev, parent_stat.st_ino)
        if (
            not stat.S_ISDIR(parent_stat.st_mode)
            or (len(parts) == 1 and parent_identity != self._root_identity)
        ):
            os.close(parent_fd)
            raise ValueError("unsafe artifact path")
        descriptor: int | None = None
        published = False
        try:
            _assert_target_absent(parent_fd, parts[-1])
            temporary = f".artifact-{uuid.uuid4().hex}.tmp"
            try:
                descriptor = os.open(
                    temporary,
                    os.O_WRONLY | os.O_CREAT | os.O_EXCL | _NOFOLLOW,
                    0o600,
                    dir_fd=parent_fd,
                )
                os.fchmod(descriptor, 0o600)
                temporary_stat = os.fstat(descriptor)
                if (
                    not stat.S_ISREG(temporary_stat.st_mode)
                    or stat.S_IMODE(temporary_stat.st_mode) != 0o600
                    or temporary_stat.st_nlink != 1
                ):
                    raise ValueError("unsafe artifact temporary file")
                _write_all(descriptor, serialized)
                os.fsync(descriptor)
                temporary_stat = os.fstat(descriptor)
                if (
                    not stat.S_ISREG(temporary_stat.st_mode)
                    or stat.S_IMODE(temporary_stat.st_mode) != 0o600
                    or temporary_stat.st_nlink != 1
                ):
                    raise ValueError("unsafe artifact temporary file")
            except ValueError:
                raise
            except OSError as exc:
                raise OSError(
                    exc.errno or errno.EIO, "artifact staging failed"
                ) from exc
            staged_descriptor = descriptor
            descriptor = None
            _close_staged_file(
                staged_descriptor,
                (temporary_stat.st_dev, temporary_stat.st_ino),
            )
            self._assert_root_identity()
            try:
                _native_publish_noreplace(parent_fd, temporary, parts[-1])
                published = True
            except FileExistsError:
                raise
            except OSError as exc:
                raise OSError(
                    exc.errno or errno.EIO, "atomic artifact publication failed"
                ) from exc
            try:
                os.fsync(parent_fd)
            except OSError as exc:
                raise ArtifactDurabilityError(
                    exc.errno or errno.EIO,
                    "artifact published but directory durability sync failed",
                ) from exc
            try:
                final = os.stat(
                    parts[-1], dir_fd=parent_fd, follow_symlinks=False
                )
            except OSError as exc:
                raise ValueError("published artifact verification failed") from exc
            if (
                not stat.S_ISREG(final.st_mode)
                or stat.S_IMODE(final.st_mode) != 0o600
                or final.st_nlink != 1
                or (final.st_dev, final.st_ino)
                != (temporary_stat.st_dev, temporary_stat.st_ino)
            ):
                raise ValueError("unsafe finalized artifact")
            self._assert_root_identity()
        finally:
            pending_error = sys.exc_info()[0] is not None
            if descriptor is not None:
                os.close(descriptor)
            try:
                _close_owned_descriptor(
                    parent_fd,
                    parent_identity,
                    "artifact parent descriptor close failed",
                )
            except OSError as exc:
                if not pending_error:
                    if published:
                        raise ArtifactDurabilityError(
                            exc.errno or errno.EIO,
                            "artifact published but parent descriptor close failed",
                        ) from exc
                    raise
        return self.root.joinpath(*parts)


def _scan_artifact_directory(
    directory_fd: int, seen: set[tuple[int, int]]
) -> None:
    for name in os.listdir(directory_fd):
        if type(name) is not str:
            raise ValueError("unsafe artifact tree")
        entry = os.stat(name, dir_fd=directory_fd, follow_symlinks=False)
        identity = (entry.st_dev, entry.st_ino)
        if identity in seen or stat.S_ISLNK(entry.st_mode):
            raise ValueError("unsafe artifact tree")
        seen.add(identity)

        if stat.S_ISDIR(entry.st_mode):
            child_fd = os.open(
                name, _DIRECTORY_FLAGS | _NOFOLLOW, dir_fd=directory_fd
            )
            try:
                opened = os.fstat(child_fd)
                if (
                    not stat.S_ISDIR(opened.st_mode)
                    or (opened.st_dev, opened.st_ino) != identity
                ):
                    raise ValueError("unsafe artifact tree")
                _scan_artifact_directory(child_fd, seen)
            finally:
                _close_owned_descriptor(
                    child_fd,
                    identity,
                    "artifact tree child descriptor close failed",
                )
            continue

        if stat.S_ISREG(entry.st_mode):
            if entry.st_nlink != 1:
                raise ValueError("unsafe artifact tree")
            file_fd = os.open(name, os.O_RDONLY | _NOFOLLOW, dir_fd=directory_fd)
            try:
                opened = os.fstat(file_fd)
                if (
                    not stat.S_ISREG(opened.st_mode)
                    or opened.st_nlink != 1
                    or (opened.st_dev, opened.st_ino) != identity
                ):
                    raise ValueError("unsafe artifact tree")
            finally:
                _close_owned_descriptor(
                    file_fd,
                    identity,
                    "artifact tree file descriptor close failed",
                )
            continue

        raise ValueError("unsafe artifact tree")


def validate_artifact_tree(root: Path) -> None:
    root_path = Path(root)
    try:
        descriptor, identity = _safe_root_fd(root_path)
    except (OSError, ValueError) as exc:
        raise ValueError("unsafe artifact tree") from exc
    try:
        _scan_artifact_directory(descriptor, set())
        current = os.lstat(root_path)
        if (
            stat.S_ISLNK(current.st_mode)
            or not stat.S_ISDIR(current.st_mode)
            or (current.st_dev, current.st_ino) != identity
        ):
            raise ValueError("unsafe artifact tree")
    except ValueError:
        raise
    except OSError as exc:
        raise ValueError("unsafe artifact tree") from exc
    finally:
        pending_error = sys.exc_info()[0] is not None
        try:
            _close_owned_descriptor(
                descriptor,
                identity,
                "artifact tree root descriptor close failed",
            )
        except OSError as exc:
            if not pending_error:
                raise ValueError("unsafe artifact tree") from exc
