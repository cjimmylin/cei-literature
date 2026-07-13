"""Private authenticated cue-to-evidence custody manifests."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import re
import stat
from typing import Any

from .artifacts import ArtifactStore
from .contracts import Json, canonical_json_bytes, canonical_sha256
from .schedule import LogicalCall, Schedule


CUSTODY_SURFACE_POLICY = (
    "PRIVATE_CUSTODY_ONLY_PROHIBITED_FROM_MODEL_AND_JUDGE_SURFACES"
)

__all__ = (
    "CUSTODY_SURFACE_POLICY",
    "VerifiedCueCustody",
    "build_cue_custody_manifest",
    "verify_cue_custody_manifest",
    "export_cue_custody_manifest",
)


_MANIFEST_VERSION = "cue-custody-v1"
_MANIFEST_STATUS = "AUTHENTICATED_COMPLETE"
_RECEIPT_VERSION = "cue-custody-receipt-v1"
_RECEIPT_STATUS = "VERIFIED_PRIVATE_CUSTODY"
_HASH = re.compile(r"[0-9a-f]{64}\Z")
_LOGICAL_ID = re.compile(r"[0-9a-f]{16}\Z")
_DIRECTORY_FLAGS = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
_NOFOLLOW = getattr(os, "O_NOFOLLOW", 0)
_MAX_EVIDENCE_OBJECT_BYTES = 8 * 1024 * 1024
_INVENTORY_FIELDS = frozenset(
    {
        "bundle_id",
        "actor_id",
        "module",
        "episode_id",
        "role",
        "cue",
        "primary_logical_call_id",
        "probe_logical_call_id",
        "primary_canonical_request_sha256",
        "probe_canonical_request_sha256",
        "evidence_artifact",
        "evidence_bundle_sha256",
    }
)
_TOP_LEVEL_FIELDS = frozenset(
    {
        "manifest_version",
        "status",
        "private",
        "surface_policy",
        "canonical_schedule_sha256",
        "row_count",
        "rows",
        "manifest_sha256",
        "custody_receipt",
    }
)
_RECEIPT_FIELDS = frozenset(
    {
        "receipt_version",
        "status",
        "surface_policy",
        "manifest_sha256",
        "canonical_schedule_sha256",
        "row_count",
        "receipt_sha256",
    }
)


@dataclass(frozen=True, init=False)
class VerifiedCueCustody:
    """Immutable summary returned by verification, not provenance authority."""

    status: str
    manifest_sha256: str
    receipt_sha256: str
    canonical_schedule_sha256: str
    evidence_inventory_sha256: str
    custody_rows_sha256: str
    row_count: int

    def __new__(cls):
        raise TypeError("verified custody is issued only by the verifier")


def _inventory_error() -> None:
    raise ValueError("invalid evidence inventory")


def _manifest_error() -> None:
    raise ValueError("invalid custody manifest")


def _evidence_root_error() -> None:
    raise ValueError("invalid evidence root")


def _evidence_artifact_error() -> None:
    raise ValueError("invalid evidence artifact")


def _canonical_evidence_error() -> None:
    raise ValueError("invalid canonical evidence artifact")


def _is_safe_evidence_artifact(value: Any) -> bool:
    if type(value) is not str or not value:
        return False
    if "\x00" in value or "\\" in value or value.startswith("/"):
        return False
    if len(value) >= 2 and value[0].isalpha() and value[1] == ":":
        return False
    try:
        encoded = value.encode("utf-8", errors="strict")
    except UnicodeError:
        return False
    if len(encoded) > 512:
        return False
    parts = value.split("/")
    return all(part and part not in {".", ".."} for part in parts)


def _validate_inventory_row(value: Any) -> dict[str, str]:
    if type(value) is not dict or set(value) != _INVENTORY_FIELDS:
        _inventory_error()
    if any(type(item) is not str for item in value.values()):
        _inventory_error()
    for name in (
        "bundle_id",
        "primary_logical_call_id",
        "probe_logical_call_id",
    ):
        if _LOGICAL_ID.fullmatch(value[name]) is None:
            _inventory_error()
    for name in (
        "primary_canonical_request_sha256",
        "probe_canonical_request_sha256",
        "evidence_bundle_sha256",
    ):
        if _HASH.fullmatch(value[name]) is None:
            _inventory_error()
    if value["cue"] not in {"C0", "C1", "C2"}:
        _inventory_error()
    if value["role"] not in {"target", "null", "restraint"}:
        _inventory_error()
    if value["module"] not in {
        "fruitbench",
        "corinthlove",
        "tencommandments",
        "sermonmount",
    }:
        _inventory_error()
    if not value["actor_id"] or not value["episode_id"]:
        _inventory_error()
    if not _is_safe_evidence_artifact(value["evidence_artifact"]):
        _inventory_error()
    return {name: value[name] for name in _INVENTORY_FIELDS}


def _assert_private_owned_directory(info: os.stat_result) -> None:
    if (
        not stat.S_ISDIR(info.st_mode)
        or info.st_uid != os.geteuid()
        or stat.S_IMODE(info.st_mode) & 0o077
    ):
        _evidence_root_error()


def _open_evidence_root(root: Path) -> tuple[int, tuple[int, int]]:
    if not isinstance(root, Path):
        raise TypeError("evidence_root must be a Path")
    descriptor: int | None = None
    try:
        before = os.lstat(root)
        if stat.S_ISLNK(before.st_mode):
            _evidence_root_error()
        _assert_private_owned_directory(before)
        descriptor = os.open(root, _DIRECTORY_FLAGS | _NOFOLLOW)
        after = os.fstat(descriptor)
        _assert_private_owned_directory(after)
        identity = (after.st_dev, after.st_ino)
        if identity != (before.st_dev, before.st_ino):
            _evidence_root_error()
        return descriptor, identity
    except (TypeError, ValueError):
        if descriptor is not None:
            os.close(descriptor)
        raise
    except OSError:
        if descriptor is not None:
            os.close(descriptor)
        _evidence_root_error()


def _read_exact_file(descriptor: int, size: int) -> bytes:
    chunks: list[bytes] = []
    remaining = size
    while remaining:
        chunk = os.read(descriptor, min(remaining, 1024 * 1024))
        if not chunk:
            _evidence_artifact_error()
        chunks.append(chunk)
        remaining -= len(chunk)
    if os.read(descriptor, 1):
        _evidence_artifact_error()
    return b"".join(chunks)


def _canonical_evidence_sha256(root_fd: int, relative: str) -> str:
    parts = relative.split("/")
    current = os.dup(root_fd)
    file_fd: int | None = None
    try:
        for component in parts[:-1]:
            child: int | None = None
            try:
                child = os.open(
                    component,
                    _DIRECTORY_FLAGS | _NOFOLLOW,
                    dir_fd=current,
                )
                child_info = os.fstat(child)
                _assert_private_owned_directory(child_info)
            except BaseException:
                if child is not None:
                    os.close(child)
                raise
            os.close(current)
            current = child
        file_fd = os.open(parts[-1], os.O_RDONLY | _NOFOLLOW, dir_fd=current)
        before = os.fstat(file_fd)
        if (
            not stat.S_ISREG(before.st_mode)
            or before.st_uid != os.geteuid()
            or stat.S_IMODE(before.st_mode) & 0o077
            or before.st_nlink != 1
            or before.st_size <= 0
            or before.st_size > _MAX_EVIDENCE_OBJECT_BYTES
        ):
            _evidence_artifact_error()
        source = _read_exact_file(file_fd, before.st_size)
        after = os.fstat(file_fd)
        if (
            (after.st_dev, after.st_ino) != (before.st_dev, before.st_ino)
            or after.st_size != before.st_size
            or after.st_mtime_ns != before.st_mtime_ns
            or after.st_ctime_ns != before.st_ctime_ns
        ):
            _evidence_artifact_error()
    except ValueError:
        raise
    except OSError:
        _evidence_artifact_error()
    finally:
        if file_fd is not None:
            os.close(file_fd)
        os.close(current)

    try:
        parsed = json.loads(source)
        if type(parsed) is not dict:
            _canonical_evidence_error()
        canonical = canonical_json_bytes(parsed)
        if source != canonical + b"\n":
            _canonical_evidence_error()
    except (
        TypeError,
        UnicodeError,
        json.JSONDecodeError,
        OverflowError,
        RecursionError,
        ValueError,
    ):
        _canonical_evidence_error()
    return hashlib.sha256(canonical).hexdigest()


def _derived_rows(schedule: Schedule) -> tuple[dict[str, str], ...]:
    if type(schedule) is not Schedule:
        raise TypeError("schedule must be a Schedule")
    # This validates the frozen schedule, including canonical request hashes,
    # logical-call identities, and bundle membership, before custody is built.
    schedule.to_canonical_json()
    probes_by_primary: dict[str, LogicalCall] = {}
    for probe in schedule.probe_rows:
        primary_id = probe.primary_logical_call_id
        if primary_id is None or primary_id in probes_by_primary:
            _inventory_error()
        probes_by_primary[primary_id] = probe

    rows: list[dict[str, str]] = []
    for primary in schedule.primary_rows:
        probe = probes_by_primary.get(primary.logical_call_id)
        if probe is None:
            _inventory_error()
        rows.append(
            {
                "bundle_id": primary.bundle_id,
                "actor_id": primary.actor_id,
                "module": primary.module,
                "episode_id": primary.episode_id,
                "role": primary.role,
                "cue": primary.cue,
                "primary_logical_call_id": primary.logical_call_id,
                "probe_logical_call_id": probe.logical_call_id,
                "primary_canonical_request_sha256": canonical_sha256(
                    primary.request_payload
                ),
                "probe_canonical_request_sha256": canonical_sha256(
                    probe.request_payload
                ),
            }
        )
    if len(rows) != 144 or len(probes_by_primary) != 144:
        _inventory_error()
    return tuple(rows)


def _bind_inventory(
    schedule: Schedule,
    evidence_inventory: tuple[dict[str, str], ...],
    *,
    evidence_root: Path,
) -> tuple[dict[str, str], ...]:
    if type(evidence_inventory) is not tuple:
        raise TypeError("evidence_inventory must be a tuple")
    validated = tuple(
        _validate_inventory_row(row) for row in evidence_inventory
    )
    by_primary: dict[str, dict[str, str]] = {}
    evidence_artifacts: set[str] = set()
    for row in validated:
        primary_id = row["primary_logical_call_id"]
        artifact = row["evidence_artifact"]
        if primary_id in by_primary or artifact in evidence_artifacts:
            _inventory_error()
        by_primary[primary_id] = row
        evidence_artifacts.add(artifact)

    derived = _derived_rows(schedule)
    expected_ids = {
        row["primary_logical_call_id"] for row in derived
    }
    if set(by_primary) != expected_ids or len(validated) != len(derived):
        _inventory_error()

    root_fd, _ = _open_evidence_root(evidence_root)
    try:
        bound: list[dict[str, str]] = []
        for relationship in derived:
            inventory_row = by_primary[relationship["primary_logical_call_id"]]
            for name, expected in relationship.items():
                if inventory_row[name] != expected:
                    _inventory_error()
            actual_evidence_sha256 = _canonical_evidence_sha256(
                root_fd, inventory_row["evidence_artifact"]
            )
            if (
                inventory_row["evidence_bundle_sha256"]
                != actual_evidence_sha256
            ):
                _inventory_error()
            bound.append(
                {
                    **relationship,
                    "evidence_artifact": inventory_row["evidence_artifact"],
                    "evidence_bundle_sha256": actual_evidence_sha256,
                }
            )
        return tuple(bound)
    finally:
        os.close(root_fd)


def _schedule_sha256(schedule: Schedule) -> str:
    return hashlib.sha256(
        schedule.to_canonical_json().encode("utf-8")
    ).hexdigest()


def _manifest_core(
    schedule_sha256: str,
    rows: tuple[dict[str, str], ...],
) -> dict[str, Json]:
    return {
        "manifest_version": _MANIFEST_VERSION,
        "status": _MANIFEST_STATUS,
        "private": True,
        "surface_policy": CUSTODY_SURFACE_POLICY,
        "canonical_schedule_sha256": schedule_sha256,
        "row_count": len(rows),
        "rows": [dict(row) for row in rows],
    }


def _receipt(
    manifest_sha256: str,
    schedule_sha256: str,
    row_count: int,
) -> dict[str, Json]:
    receipt: dict[str, Json] = {
        "receipt_version": _RECEIPT_VERSION,
        "status": _RECEIPT_STATUS,
        "surface_policy": CUSTODY_SURFACE_POLICY,
        "manifest_sha256": manifest_sha256,
        "canonical_schedule_sha256": schedule_sha256,
        "row_count": row_count,
    }
    receipt["receipt_sha256"] = canonical_sha256(receipt)
    return receipt


def build_cue_custody_manifest(
    schedule: Schedule,
    evidence_inventory: tuple[dict[str, str], ...],
    *,
    evidence_root: Path,
) -> dict[str, Json]:
    """Bind a complete exact inventory to relationships derived from Schedule."""

    rows = _bind_inventory(
        schedule, evidence_inventory, evidence_root=evidence_root
    )
    schedule_sha256 = _schedule_sha256(schedule)
    core = _manifest_core(schedule_sha256, rows)
    manifest_sha256 = canonical_sha256(core)
    return {
        **core,
        "manifest_sha256": manifest_sha256,
        "custody_receipt": _receipt(
            manifest_sha256, schedule_sha256, len(rows)
        ),
    }


def _assert_authentication(manifest: dict[str, Json]) -> None:
    if set(manifest) != _TOP_LEVEL_FIELDS:
        _manifest_error()
    manifest_hash = manifest.get("manifest_sha256")
    if type(manifest_hash) is not str or _HASH.fullmatch(manifest_hash) is None:
        _manifest_error()
    core = {
        key: value
        for key, value in manifest.items()
        if key not in {"manifest_sha256", "custody_receipt"}
    }
    try:
        if canonical_sha256(core) != manifest_hash:
            _manifest_error()
    except (TypeError, ValueError, OverflowError, RecursionError):
        _manifest_error()

    receipt = manifest.get("custody_receipt")
    if type(receipt) is not dict or set(receipt) != _RECEIPT_FIELDS:
        _manifest_error()
    receipt_hash = receipt.get("receipt_sha256")
    if type(receipt_hash) is not str or _HASH.fullmatch(receipt_hash) is None:
        _manifest_error()
    receipt_core = {
        key: value for key, value in receipt.items() if key != "receipt_sha256"
    }
    try:
        if canonical_sha256(receipt_core) != receipt_hash:
            _manifest_error()
    except (TypeError, ValueError, OverflowError, RecursionError):
        _manifest_error()
    if (
        receipt.get("receipt_version") != _RECEIPT_VERSION
        or receipt.get("status") != _RECEIPT_STATUS
        or receipt.get("surface_policy") != CUSTODY_SURFACE_POLICY
        or receipt.get("manifest_sha256") != manifest_hash
        or receipt.get("canonical_schedule_sha256")
        != manifest.get("canonical_schedule_sha256")
        or receipt.get("row_count") != manifest.get("row_count")
    ):
        _manifest_error()


def verify_cue_custody_manifest(
    schedule: Schedule,
    evidence_inventory: tuple[dict[str, str], ...],
    manifest: dict[str, Json],
    *,
    evidence_root: Path,
) -> VerifiedCueCustody:
    """Recompute and verify every authenticated custody field exactly."""

    if type(manifest) is not dict:
        _manifest_error()
    _assert_authentication(manifest)
    expected = build_cue_custody_manifest(
        schedule, evidence_inventory, evidence_root=evidence_root
    )
    try:
        if canonical_json_bytes(manifest) != canonical_json_bytes(expected):
            _manifest_error()
    except (TypeError, ValueError, OverflowError, RecursionError):
        _manifest_error()
    rows = manifest["rows"]
    receipt = manifest["custody_receipt"]
    if type(rows) is not list or type(receipt) is not dict:
        _manifest_error()
    verified = object.__new__(VerifiedCueCustody)
    object.__setattr__(verified, "status", _RECEIPT_STATUS)
    object.__setattr__(
        verified, "manifest_sha256", manifest["manifest_sha256"]
    )
    object.__setattr__(
        verified, "receipt_sha256", receipt["receipt_sha256"]
    )
    object.__setattr__(
        verified,
        "canonical_schedule_sha256",
        manifest["canonical_schedule_sha256"],
    )
    object.__setattr__(
        verified,
        "evidence_inventory_sha256",
        canonical_sha256(
            {
                "domain": "biblebench.cue_custody.inventory.v1",
                "rows": rows,
            }
        ),
    )
    object.__setattr__(
        verified, "custody_rows_sha256", canonical_sha256(rows)
    )
    object.__setattr__(verified, "row_count", manifest["row_count"])
    return verified


def export_cue_custody_manifest(
    destination: Path,
    schedule: Schedule,
    evidence_inventory: tuple[dict[str, str], ...],
    *,
    evidence_root: Path,
) -> Path:
    """Exclusively publish one canonical private ``0600`` JSON manifest."""

    if not isinstance(destination, Path) or destination.name != destination.name.strip():
        raise ValueError("invalid custody destination")
    if destination.suffix != ".json":
        raise ValueError("invalid custody destination")
    manifest = build_cue_custody_manifest(
        schedule, evidence_inventory, evidence_root=evidence_root
    )
    target = ArtifactStore(destination.parent).write(destination.name, manifest)
    if target != destination:
        raise ValueError("invalid custody destination")
    return target
