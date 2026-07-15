import csv
import json
from pathlib import Path

import pytest

from walkworthy import design02_labeling_helper as helper


BENCHMARK = Path(__file__).resolve().parents[2]
PRIMARY = BENCHMARK / "labels/20260710-partA/02-twomasters-partA-blind.csv"
RELIABILITY = (
    BENCHMARK
    / "labels/20260710-partA/reliability/02-twomasters-partA-overlap-blind.csv"
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
    expected_primary_turn_counts = tuple(
        json.loads("[2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2]")
    )
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
