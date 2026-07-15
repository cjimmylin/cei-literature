import csv
import hashlib
import json
from dataclasses import FrozenInstanceError
from pathlib import Path

import pytest

from walkworthy import design02_labeling_helper as helper


BENCHMARK = Path(__file__).resolve().parents[2]
PRIMARY = BENCHMARK / "labels/20260710-partA/02-twomasters-partA-blind.csv"
RELIABILITY = (
    BENCHMARK
    / "labels/20260710-partA/reliability/02-twomasters-partA-overlap-blind.csv"
)


def _source_row(index, context_and_response=None):
    return [
        f"02-twomasters-U{index:03d}",
        "02-twomasters",
        context_and_response
        or f"context {index}{helper.TURN_DELIMITER}response {index}",
        "",
        "",
        "",
        "",
        "",
    ]


def _write_fixture(tmp_path, rows, header=helper.HEADER):
    path = tmp_path / "blind.csv"
    with path.open("w", encoding="utf-8", newline="") as destination:
        writer = csv.writer(destination, lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)
    return path, hashlib.sha256(path.read_bytes()).hexdigest()


def _instrument(rows):
    return helper.Instrument(
        path=Path("blind.csv"),
        sha256="0" * 64,
        fieldnames=helper.HEADER,
        rows=tuple(rows),
    )


def test_load_instruments_freezes_hash_schema_rows_and_turns():
    bundle = helper.load_instruments(PRIMARY, RELIABILITY)

    with PRIMARY.open(encoding="utf-8", newline="") as source:
        assert tuple(csv.DictReader(source).fieldnames or ()) == helper.HEADER

    assert helper.DESIGN == "02-twomasters"
    assert helper.TURN_DELIMITER == " ⟦//⟧ "
    assert helper.HEADER == (
        "unit_id",
        "design",
        "context_and_response",
        "turn_state",
        "confidence_1_3",
        "notes",
        "Q-R1_declines",
        "Q-R2_avoids_keyed_wrong",
    )
    assert helper.TURN_STATES == (
        "holds_line",
        "soft_concession",
        "material_concession",
        "full_compliance",
        "pushback_with_alternative",
    )
    assert (
        helper.PRIMARY_SHA256
        == "1ace34dd8b33b06448c4d712edca4be0f4525e6223820ea4c68101736d2e147a"
    )
    assert (
        helper.RELIABILITY_SHA256
        == "f448b339c1708ee5de252241e2ba03452283a2b965c1b294b9b680cca0669bee"
    )
    expected_primary_turn_counts = (2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2)
    assert helper.PRIMARY_TURN_COUNTS == expected_primary_turn_counts
    assert helper.RELIABILITY_TURN_COUNTS == (2, 2, 1, 2)

    assert bundle.primary.path == PRIMARY
    assert bundle.primary.sha256 == helper.PRIMARY_SHA256
    assert bundle.primary.fieldnames == helper.HEADER
    assert len(bundle.primary.rows) == 12
    assert tuple(
        len(row.turns) for row in bundle.primary.rows
    ) == expected_primary_turn_counts

    assert bundle.reliability.path == RELIABILITY
    assert bundle.reliability.sha256 == helper.RELIABILITY_SHA256
    assert bundle.reliability.fieldnames == helper.HEADER
    assert len(bundle.reliability.rows) == 4
    assert tuple(len(row.turns) for row in bundle.reliability.rows) == (2, 2, 1, 2)
    assert tuple(row.unit_id for row in bundle.reliability.rows) == tuple(
        row.unit_id for row in bundle.primary.rows[:4]
    )
    assert tuple(row.context_and_response for row in bundle.reliability.rows) == tuple(
        row.context_and_response for row in bundle.primary.rows[:4]
    )


@pytest.mark.parametrize(
    ("before", "after"),
    (
        ("02-twomasters-U000", "02-twomasters-U999"),
        (" ⟦//⟧ ", " ⟦/ /⟧ "),
        ("unit_id,design", "unit_ID,design"),
    ),
    ids=("unit-id", "delimiter", "header"),
)
def test_load_instruments_rejects_any_source_drift(tmp_path, before, after):
    mutated_primary = tmp_path / PRIMARY.name
    source = PRIMARY.read_bytes()
    before_bytes = before.encode("utf-8")
    assert before_bytes in source
    mutated_primary.write_bytes(source.replace(before_bytes, after.encode("utf-8"), 1))

    with pytest.raises(helper.HelperContractError, match="source SHA-256 mismatch"):
        helper.load_instruments(mutated_primary, RELIABILITY)


@pytest.mark.parametrize(
    ("mutation", "message"),
    (
        ("header", "source header mismatch"),
        ("row-count", "source row count mismatch"),
        ("unit-id", "source unit ID mismatch"),
        ("row-order", "source unit ID mismatch"),
        ("design", "source design mismatch"),
        ("label", "source label cells must be blank"),
        ("delimiter", "source turn count mismatch"),
        ("empty-turn", "source contains an empty turn"),
        ("surplus-column", "source row cardinality mismatch"),
        ("missing-column", "source row cardinality mismatch"),
    ),
)
def test_load_one_enforces_semantic_contract(tmp_path, mutation, message):
    header = list(helper.HEADER)
    rows = [_source_row(0), _source_row(1)]
    expected_turn_counts = (2, 2)

    if mutation == "header":
        header[0] = "unit_ID"
    elif mutation == "row-count":
        rows.pop()
    elif mutation == "unit-id":
        rows[0][0] = "02-twomasters-U999"
    elif mutation == "row-order":
        rows.reverse()
    elif mutation == "design":
        rows[0][1] = "not-design-02"
    elif mutation == "label":
        rows[0][3] = "holds_line"
    elif mutation == "delimiter":
        rows[0][2] = "context 0 ⟦/ /⟧ response 0"
    elif mutation == "empty-turn":
        rows[0][2] = f"context 0{helper.TURN_DELIMITER}"
    elif mutation == "surplus-column":
        rows[0].append("extra")
    elif mutation == "missing-column":
        rows[0].pop()

    path, actual_sha = _write_fixture(tmp_path, rows, header)
    with pytest.raises(helper.HelperContractError, match=message):
        helper._load_one(path, actual_sha, expected_turn_counts)


@pytest.mark.parametrize(
    ("mutation", "message"),
    (("unit-id", "unit IDs"), ("context", "contexts")),
)
def test_validate_overlap_rejects_first_four_mismatch(mutation, message):
    primary_rows = [
        helper.BlindRow(
            unit_id=f"02-twomasters-U{index:03d}",
            design=helper.DESIGN,
            context_and_response=f"context {index}",
            turns=(f"context {index}",),
        )
        for index in range(5)
    ]
    reliability_rows = list(primary_rows[:4])
    original = reliability_rows[0]
    reliability_rows[0] = helper.BlindRow(
        unit_id="02-twomasters-U999" if mutation == "unit-id" else original.unit_id,
        design=original.design,
        context_and_response=(
            "different context"
            if mutation == "context"
            else original.context_and_response
        ),
        turns=original.turns,
    )

    with pytest.raises(helper.HelperContractError, match=message):
        helper._validate_overlap(
            _instrument(primary_rows), _instrument(reliability_rows)
        )


def test_contract_dataclasses_are_immutable():
    row = helper.BlindRow(
        unit_id="02-twomasters-U000",
        design=helper.DESIGN,
        context_and_response="context",
        turns=("context",),
    )
    instrument = _instrument((row,))
    bundle = helper.InstrumentBundle(primary=instrument, reliability=instrument)

    for value, field in (
        (row, "unit_id"),
        (instrument, "sha256"),
        (bundle, "primary"),
    ):
        with pytest.raises(FrozenInstanceError):
            setattr(value, field, None)
