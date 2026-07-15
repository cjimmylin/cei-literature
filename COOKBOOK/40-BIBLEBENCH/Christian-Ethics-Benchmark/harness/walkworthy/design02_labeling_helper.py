"""Frozen source contracts for the Design 02 human-labeling helper."""

from __future__ import annotations

import csv
import hashlib
import io
from dataclasses import dataclass
from pathlib import Path
from typing import Tuple


DESIGN = "02-twomasters"
TURN_DELIMITER = " ⟦//⟧ "
HEADER = (
    "unit_id",
    "design",
    "context_and_response",
    "turn_state",
    "confidence_1_3",
    "notes",
    "Q-R1_declines",
    "Q-R2_avoids_keyed_wrong",
)
TURN_STATES = (
    "holds_line",
    "soft_concession",
    "material_concession",
    "full_compliance",
    "pushback_with_alternative",
)
PRIMARY_SHA256 = "1ace34dd8b33b06448c4d712edca4be0f4525e6223820ea4c68101736d2e147a"
RELIABILITY_SHA256 = "f448b339c1708ee5de252241e2ba03452283a2b965c1b294b9b680cca0669bee"
PRIMARY_TURN_COUNTS = (2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2)
RELIABILITY_TURN_COUNTS = (2, 2, 1, 2)


class HelperContractError(RuntimeError):
    """Raised when a blind labeling instrument violates its frozen contract."""


@dataclass(frozen=True)
class BlindRow:
    unit_id: str
    design: str
    context_and_response: str
    turns: Tuple[str, ...]


@dataclass(frozen=True)
class Instrument:
    path: Path
    sha256: str
    fieldnames: Tuple[str, ...]
    rows: Tuple[BlindRow, ...]


@dataclass(frozen=True)
class InstrumentBundle:
    primary: Instrument
    reliability: Instrument


def _load_one(
    path: Path, expected_sha: str, expected_turn_counts: Tuple[int, ...]
) -> Instrument:
    path = Path(path)
    raw = path.read_bytes()
    actual_sha = hashlib.sha256(raw).hexdigest()
    if actual_sha != expected_sha:
        raise HelperContractError(
            f"source SHA-256 mismatch for {path}: expected {expected_sha}, got {actual_sha}"
        )

    reader = csv.DictReader(io.StringIO(raw.decode("utf-8"), newline=""))
    fieldnames = tuple(reader.fieldnames or ())
    if fieldnames != HEADER:
        raise HelperContractError(
            f"source header mismatch for {path}: expected {HEADER!r}, got {fieldnames!r}"
        )

    source_rows = list(reader)
    if len(source_rows) != len(expected_turn_counts):
        raise HelperContractError(
            f"source row count mismatch for {path}: expected "
            f"{len(expected_turn_counts)}, got {len(source_rows)}"
        )

    rows = []
    for index, (source_row, expected_turn_count) in enumerate(
        zip(source_rows, expected_turn_counts)
    ):
        if None in source_row or any(
            source_row.get(fieldname) is None for fieldname in HEADER
        ):
            raise HelperContractError(
                f"source row cardinality mismatch at row {index}"
            )

        expected_unit_id = f"{DESIGN}-U{index:03d}"
        if source_row["unit_id"] != expected_unit_id:
            raise HelperContractError(
                f"source unit ID mismatch at row {index}: expected "
                f"{expected_unit_id!r}, got {source_row['unit_id']!r}"
            )
        if source_row["design"] != DESIGN:
            raise HelperContractError(
                f"source design mismatch at row {index}: expected "
                f"{DESIGN!r}, got {source_row['design']!r}"
            )

        populated_label_fields = [
            fieldname for fieldname in HEADER[3:] if source_row[fieldname] != ""
        ]
        if populated_label_fields:
            raise HelperContractError(
                f"source label cells must be blank at row {index}: "
                f"{populated_label_fields!r}"
            )

        context_and_response = source_row["context_and_response"]
        turns = tuple(context_and_response.split(TURN_DELIMITER))
        if len(turns) != expected_turn_count:
            raise HelperContractError(
                f"source turn count mismatch at row {index}: expected "
                f"{expected_turn_count}, got {len(turns)}"
            )
        if any(not turn.strip() for turn in turns):
            raise HelperContractError(f"source contains an empty turn at row {index}")

        rows.append(
            BlindRow(
                unit_id=source_row["unit_id"],
                design=source_row["design"],
                context_and_response=context_and_response,
                turns=turns,
            )
        )

    return Instrument(
        path=path,
        sha256=actual_sha,
        fieldnames=fieldnames,
        rows=tuple(rows),
    )


def _validate_overlap(primary: Instrument, reliability: Instrument) -> None:
    primary_overlap = primary.rows[:4]
    if tuple(row.unit_id for row in reliability.rows) != tuple(
        row.unit_id for row in primary_overlap
    ):
        raise HelperContractError(
            "reliability unit IDs must equal the first four primary unit IDs"
        )
    if tuple(row.context_and_response for row in reliability.rows) != tuple(
        row.context_and_response for row in primary_overlap
    ):
        raise HelperContractError(
            "reliability contexts must equal the first four primary contexts"
        )


def load_instruments(primary_path: Path, reliability_path: Path) -> InstrumentBundle:
    primary = _load_one(primary_path, PRIMARY_SHA256, PRIMARY_TURN_COUNTS)
    reliability = _load_one(
        reliability_path, RELIABILITY_SHA256, RELIABILITY_TURN_COUNTS
    )

    _validate_overlap(primary, reliability)

    return InstrumentBundle(primary=primary, reliability=reliability)
