#!/usr/bin/env python3
"""Export the deterministic blinded SKIM P1 professional-realism packet."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from collections.abc import Iterable as IterableABC, Mapping as MappingABC
import hashlib
import json
import os
from pathlib import Path
import random
import sys
import tempfile
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from skim_constants import (  # noqa: E402
    FAMILIES,
    FAMILY_CODES,
    FAMILY_CORE_COUNTS,
    LOGICAL_BANK_RECORDS,
    LOGICAL_RECORD_COUNTS,
    MAGNITUDE_TIERS,
    PROFESSIONAL_REALISM_REQUIREMENTS,
)
from skim_hashing import canonical_json, canonical_sha256  # noqa: E402
from skim_schemas import validate_public_item_fields  # noqa: E402


PathLike = Union[str, Path]
DEFAULT_SEED = 20260711
INSTRUMENT = "SKIM-P1-PROFESSIONAL-REALISM"
BINARY_FIELDS = (
    "scenario_realism",
    "magnitude_window_plausibility",
)
ORDINAL_FIELDS = (
    "scenario_realism_rating_1_to_5",
    "magnitude_window_plausibility_rating_1_to_5",
)
RATING_FIELDS = BINARY_FIELDS + ORDINAL_FIELDS

PACKET_FIELDS = (
    "review_id",
    "stratum_id",
    "domain",
    "scenario",
    "principal_mandate",
    "magnitude_window_usd",
    "rating_form",
)
LINKAGE_FIELDS = (
    "review_id",
    "stratum_id",
    "core_id",
    "family",
    "family_code",
    "primary_logical_record_ids",
    "public_record_sha256_by_tier",
    "source_bank_sha256",
)

_JSON_SAFE_INTEGER_MAX = 2**53 - 1


def _canonical_jsonl_text(rows: Iterable[Mapping[str, Any]]) -> str:
    if isinstance(rows, (str, bytes, bytearray)) or not isinstance(
        rows, IterableABC
    ):
        raise TypeError("JSONL rows must be an iterable of mappings")
    lines = []
    for row in rows:
        if not isinstance(row, MappingABC):
            raise TypeError("every JSONL row must be a mapping")
        lines.append(canonical_json(row) + "\n")
    return "".join(lines)


def canonical_jsonl_sha256(rows: Iterable[Mapping[str, Any]]) -> str:
    """Hash the exact canonical JSONL encoding while preserving row order."""

    return hashlib.sha256(_canonical_jsonl_text(rows).encode("utf-8")).hexdigest()


def _canonical_identifier(value: Any, label: str) -> str:
    if type(value) is not str or not value or value != value.strip():
        raise ValueError("%s must be a canonical nonblank string" % label)
    return value


def _validate_seed(seed: Any) -> int:
    if type(seed) is not int or not 0 <= seed <= _JSON_SAFE_INTEGER_MAX:
        raise ValueError("seed must be a nonnegative IEEE-754-safe integer")
    return seed


def _opaque_identifier(namespace: str, seed: int, source: str) -> str:
    digest = hashlib.sha256(
        ("%s\x1f%d\x1f%s" % (namespace, seed, source)).encode("utf-8")
    ).hexdigest()[:24]
    return "%s-%s" % (namespace, digest)


def _core_surface(primary_rows: Sequence[Mapping[str, Any]]) -> Tuple[str, str]:
    scenarios = set()
    mandates = set()
    for row in primary_rows:
        requests = row["requests"]
        if type(requests) is not list or len(requests) != 1:
            raise ValueError("every primary realism source requires one request")
        request = requests[0]
        state = request.get("structured_state")
        if not isinstance(state, MappingABC):
            raise ValueError("primary request is missing structured_state")
        scenario = _canonical_identifier(state.get("scenario"), "scenario")
        mandate = _canonical_identifier(
            state.get("principal_mandate"), "principal_mandate"
        )
        scenarios.add(scenario)
        mandates.add(mandate)
    if len(scenarios) != 1 or len(mandates) != 1:
        raise ValueError("primary tiers do not share one coherent core surface")
    return next(iter(scenarios)), next(iter(mandates))


def _validate_and_group_bank(
    public_rows: Iterable[Mapping[str, Any]],
) -> Tuple[List[Dict[str, Any]], Dict[str, List[Dict[str, Any]]]]:
    if isinstance(public_rows, (str, bytes, bytearray)) or not isinstance(
        public_rows, IterableABC
    ):
        raise TypeError("public_rows must be an iterable of mappings")
    rows = []
    for value in public_rows:
        if not isinstance(value, MappingABC):
            raise TypeError("every public bank row must be a mapping")
        row = dict(value)
        if not validate_public_item_fields(row):
            raise ValueError("public bank row failed the frozen schema")
        if row["panel_kappa"] is not None:
            raise ValueError("professional outcomes must not be prefilled")
        if row["difficulty_est"] is not None:
            raise ValueError("difficulty estimates must not be prefilled")
        rows.append(row)
    if len(rows) != LOGICAL_BANK_RECORDS:
        raise ValueError("realism export requires the exact 640-row public bank")

    logical_ids = [row["logical_record_id"] for row in rows]
    if len(set(logical_ids)) != len(logical_ids):
        raise ValueError("public bank contains a duplicate logical_record_id")

    grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[row["core_id"]].append(row)
    expected_cores = sum(FAMILY_CORE_COUNTS.values())
    if len(grouped) != expected_cores:
        raise ValueError("realism export requires exactly 40 scenario cores")

    family_counts = Counter()
    surface_owners: Dict[Tuple[str, str], str] = {}
    expected_tiers = set(MAGNITUDE_TIERS)
    expected_record_types = set(LOGICAL_RECORD_COUNTS)
    for core_id, core_rows in grouped.items():
        _canonical_identifier(core_id, "core_id")
        if len(core_rows) != len(expected_record_types) * len(expected_tiers):
            raise ValueError("each core must contain exactly sixteen logical rows")
        families = {row["family"] for row in core_rows}
        family_codes = {row["family_code"] for row in core_rows}
        domains = {row["domain"] for row in core_rows}
        windows = {tuple(row["magnitude_window"]) for row in core_rows}
        if (
            len(families) != 1
            or len(family_codes) != 1
            or len(domains) != 1
            or len(windows) != 1
        ):
            raise ValueError("core family, domain, or magnitude window is incoherent")
        family = next(iter(families))
        if family not in FAMILY_CORE_COUNTS or family_codes != {FAMILY_CODES[family]}:
            raise ValueError("core family code is incoherent")
        family_counts[family] += 1

        by_type: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
        seen_cells = set()
        for row in core_rows:
            cell = (row["record_type"], row["magnitude_tier"])
            if cell in seen_cells:
                raise ValueError("core contains a duplicate record-type/tier cell")
            seen_cells.add(cell)
            by_type[row["record_type"]].append(row)
        if set(by_type) != expected_record_types or any(
            {row["magnitude_tier"] for row in by_type[record_type]}
            != expected_tiers
            for record_type in expected_record_types
        ):
            raise ValueError("every core requires all four tiers of every record type")

        primary_rows = sorted(
            by_type["primary"], key=lambda row: row["magnitude_tier"]
        )
        scenario, mandate = _core_surface(primary_rows)
        surface_key = (scenario, mandate)
        if surface_key in surface_owners:
            raise ValueError("two cores share the same professional-review surface")
        surface_owners[surface_key] = core_id

    if set(family_counts) != set(FAMILIES) or any(
        family_counts[family] != FAMILY_CORE_COUNTS[family] for family in FAMILIES
    ):
        raise ValueError("realism export requires exactly eight cores per family")
    return rows, dict(grouped)


def _initial_not_run_result(
    packet: Sequence[Mapping[str, Any]], linkage: Sequence[Mapping[str, Any]]
) -> Dict[str, Any]:
    source_bank_hashes = {
        row.get("source_bank_sha256")
        for row in linkage
        if isinstance(row, MappingABC)
    }
    if len(source_bank_hashes) != 1:
        raise ValueError("linkage must bind one source bank hash")
    source_bank_sha256 = next(iter(source_bank_hashes))
    result: Dict[str, Any] = {
        "schema_version": 1,
        "instrument": INSTRUMENT,
        "data_basis": None,
        "status": "NOT_RUN_PROFESSIONAL_REALISM",
        "human_baseline_status": "NOT_RUN_HUMAN_BASELINE",
        "eligible_for_model_pilot": False,
        "eligible_for_empirical_decision": False,
        "counts": {"cores": 40, "families": 5, "ratings": 0},
        "family_passing_cores": {},
        "fleiss_kappa": {
            "scenario_realism": None,
            "magnitude_window_plausibility": None,
        },
        "thresholds": dict(PROFESSIONAL_REALISM_REQUIREMENTS),
        "reasons": ["NO_PROFESSIONAL_EVIDENCE"],
        "artifact_sha256": {
            "source_bank": source_bank_sha256,
            "packet": canonical_jsonl_sha256(packet),
            "linkage": canonical_jsonl_sha256(linkage),
            "evidence": None,
            "result": None,
        },
    }
    result["artifact_sha256"]["result"] = canonical_sha256(result)
    return result


def build_realism_packet(
    public_rows: Iterable[Mapping[str, Any]], *, seed: int = DEFAULT_SEED
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], Dict[str, Any]]:
    """Return a blinded packet, private linkage, and fail-closed initial result."""

    seed = _validate_seed(seed)
    rows, grouped = _validate_and_group_bank(public_rows)
    source_bank_sha256 = canonical_jsonl_sha256(rows)

    review_ids = {
        core_id: _opaque_identifier("skim-realism-review", seed, core_id)
        for core_id in grouped
    }
    stratum_ids = {
        family: _opaque_identifier("skim-realism-stratum", seed, family)
        for family in FAMILIES
    }
    if len(set(review_ids.values())) != len(review_ids) or len(
        set(stratum_ids.values())
    ) != len(stratum_ids):
        raise ValueError("opaque realism identifiers collided")

    core_order = sorted(grouped)
    random.Random(seed).shuffle(core_order)
    packet = []
    linkage = []
    for core_id in core_order:
        core_rows = grouped[core_id]
        primary_rows = sorted(
            (row for row in core_rows if row["record_type"] == "primary"),
            key=lambda row: row["magnitude_tier"],
        )
        scenario, mandate = _core_surface(primary_rows)
        family = primary_rows[0]["family"]
        review_id = review_ids[core_id]
        stratum_id = stratum_ids[family]
        packet_row = {
            "review_id": review_id,
            "stratum_id": stratum_id,
            "domain": primary_rows[0]["domain"],
            "scenario": scenario,
            "principal_mandate": mandate,
            "magnitude_window_usd": list(primary_rows[0]["magnitude_window"]),
            "rating_form": {
                "scenario_realism": None,
                "magnitude_window_plausibility": None,
                "scenario_realism_rating_1_to_5": None,
                "magnitude_window_plausibility_rating_1_to_5": None,
            },
        }
        linkage_row = {
            "review_id": review_id,
            "stratum_id": stratum_id,
            "core_id": core_id,
            "family": family,
            "family_code": primary_rows[0]["family_code"],
            "primary_logical_record_ids": [
                row["logical_record_id"] for row in primary_rows
            ],
            "public_record_sha256_by_tier": {
                str(row["magnitude_tier"]): canonical_sha256(row)
                for row in primary_rows
            },
            "source_bank_sha256": source_bank_sha256,
        }
        if tuple(packet_row) != PACKET_FIELDS or tuple(linkage_row) != LINKAGE_FIELDS:
            raise AssertionError("internal realism row schema drift")
        packet.append(packet_row)
        linkage.append(linkage_row)

    result = _initial_not_run_result(packet, linkage)
    return packet, linkage, result


def _atomic_stage_bytes(path: Path, data: bytes) -> Path:
    if type(data) is not bytes:
        raise TypeError("staged artifact data must be exact bytes")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary: Optional[Path] = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb",
            dir=str(path.parent),
            prefix=".%s." % path.name,
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary = Path(handle.name)
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        return temporary
    except BaseException:
        if temporary is not None:
            try:
                temporary.unlink()
            except FileNotFoundError:
                pass
        raise


def _atomic_write_text(path: Path, text: str) -> Path:
    if type(text) is not str:
        raise TypeError("staged artifact text must be an exact string")
    return _atomic_stage_bytes(path, text.encode("utf-8"))


def _write_artifacts_atomically(payloads: Sequence[Tuple[Path, str]]) -> None:
    originals: List[Tuple[Path, Optional[bytes]]] = []
    for destination, _text in payloads:
        try:
            originals.append((destination, destination.read_bytes()))
        except FileNotFoundError:
            originals.append((destination, None))

    staged: List[Tuple[Path, Path]] = []
    try:
        for destination, text in payloads:
            staged.append((destination, _atomic_write_text(destination, text)))
        for destination, temporary in staged:
            os.replace(str(temporary), str(destination))
    except BaseException as replace_error:
        rollback_error: Optional[BaseException] = None
        for destination, original in originals:
            restore_temporary: Optional[Path] = None
            try:
                if original is None:
                    try:
                        destination.unlink()
                    except FileNotFoundError:
                        pass
                else:
                    restore_temporary = _atomic_stage_bytes(destination, original)
                    os.replace(str(restore_temporary), str(destination))
            except BaseException as exc:
                if rollback_error is None:
                    rollback_error = exc
            finally:
                if restore_temporary is not None:
                    try:
                        restore_temporary.unlink()
                    except FileNotFoundError:
                        pass
        for _destination, temporary in staged:
            try:
                temporary.unlink()
            except FileNotFoundError:
                pass
        if rollback_error is not None:
            raise rollback_error from replace_error
        raise


def _require_distinct_paths(paths: Sequence[Path], labels: Sequence[str]) -> None:
    resolved = [path.resolve() for path in paths]
    if len(set(resolved)) != len(resolved):
        raise ValueError("%s paths must be physically distinct" % ", ".join(labels))
    for left_index, left in enumerate(paths):
        for right in paths[left_index + 1 :]:
            try:
                if os.path.samefile(left, right):
                    raise ValueError(
                        "%s paths must be physically distinct" % ", ".join(labels)
                    )
            except FileNotFoundError:
                continue


def write_realism_packet(
    public_rows: Iterable[Mapping[str, Any]],
    packet_path: PathLike,
    linkage_path: PathLike,
    result_path: PathLike,
    *,
    seed: int = DEFAULT_SEED,
) -> Dict[str, Any]:
    """Write canonical packet/linkage/result artifacts after full validation."""

    destinations = tuple(Path(path) for path in (packet_path, linkage_path, result_path))
    _require_distinct_paths(destinations, ("packet", "linkage", "result"))
    packet, linkage, result = build_realism_packet(public_rows, seed=seed)
    _write_artifacts_atomically(
        (
            (destinations[0], _canonical_jsonl_text(packet)),
            (destinations[1], _canonical_jsonl_text(linkage)),
            (destinations[2], canonical_json(result) + "\n"),
        )
    )
    return result


def _read_jsonl(path: Path) -> List[Dict[str, Any]]:
    data = path.read_bytes()
    if not data or not data.endswith(b"\n"):
        raise ValueError("input must be nonempty canonical JSONL")
    raw_lines = data[:-1].split(b"\n")
    if any(not line for line in raw_lines):
        raise ValueError("input must not contain blank canonical JSONL rows")
    rows = []
    for line_number, raw_line in enumerate(raw_lines, start=1):
        try:
            row = json.loads(raw_line.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError(
                "input JSONL line %d is not canonical JSON" % line_number
            ) from exc
        if type(row) is not dict:
            raise ValueError("input JSONL line %d is not an object" % line_number)
        try:
            canonical = canonical_json(row).encode("utf-8")
        except (TypeError, ValueError) as exc:
            raise ValueError(
                "input JSONL line %d is not canonical JSON" % line_number
            ) from exc
        if canonical != raw_line:
            raise ValueError("input must use exact canonical JSONL bytes")
        rows.append(row)
    return rows


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--packet", type=Path, required=True)
    parser.add_argument("--linkage", type=Path, required=True)
    parser.add_argument("--result", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args(argv)

    paths = (args.input, args.packet, args.linkage, args.result)
    _require_distinct_paths(paths, ("input", "packet", "linkage", "result"))
    rows = _read_jsonl(args.input)
    write_realism_packet(
        rows,
        args.packet,
        args.linkage,
        args.result,
        seed=args.seed,
    )
    return 0


__all__ = [
    "BINARY_FIELDS",
    "DEFAULT_SEED",
    "INSTRUMENT",
    "LINKAGE_FIELDS",
    "ORDINAL_FIELDS",
    "PACKET_FIELDS",
    "RATING_FIELDS",
    "build_realism_packet",
    "canonical_jsonl_sha256",
    "main",
    "write_realism_packet",
]


if __name__ == "__main__":
    raise SystemExit(main())
