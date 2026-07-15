import base64
import csv
import hashlib
import json
import os
import re
from dataclasses import FrozenInstanceError, replace
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

from walkworthy import design02_labeling_helper as helper


BENCHMARK = Path(__file__).resolve().parents[2]
PRIMARY = BENCHMARK / "labels/20260710-partA/02-twomasters-partA-blind.csv"
RELIABILITY = (
    BENCHMARK
    / "labels/20260710-partA/reliability/02-twomasters-partA-overlap-blind.csv"
)
DEFAULT_CHROME = Path(
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
)
DRAFT_INVALID_WARNING = (
    "A stale or invalid draft was ignored; no values were migrated."
)
DRAFT_STORAGE_WARNING = (
    "Draft storage is unavailable; changes remain in memory for this session only."
)


@pytest.fixture
def browser_page():
    chrome = Path(os.environ.get("WALKWORTHY_CHROME", DEFAULT_CHROME))
    if not chrome.is_file():
        pytest.fail(
            "System Chrome is required for Design 02 helper browser tests; "
            f"set WALKWORTHY_CHROME or install it at {DEFAULT_CHROME}"
        )

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True,
            executable_path=str(chrome),
        )
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        browser_errors = []
        page.on(
            "console",
            lambda message: browser_errors.append(
                f"console error: {message.text}"
            )
            if message.type == "error"
            else None,
        )
        page.on(
            "pageerror",
            lambda error: browser_errors.append(f"page error: {error}"),
        )
        page.on(
            "request",
            lambda request: browser_errors.append(
                f"unexpected network request: {request.url}"
            )
            if request.url.startswith(("http://", "https://"))
            else None,
        )
        try:
            yield page, browser_errors
        finally:
            browser.close()


def _generated(tmp_path):
    bundle = helper.load_instruments(PRIMARY, RELIABILITY)
    output_dir = tmp_path / "helper"
    helper.generate(bundle, output_dir)
    return output_dir


def _complete_reliability(page):
    for _ in range(7):
        page.get_by_role("radio", name="holds_line", exact=True).check()
        page.get_by_label("Confidence", exact=True).select_option("3")
        page.get_by_role("radio", name="Q-R1 no", exact=True).check()
        page.get_by_test_id("next").click()


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


def _embedded_payload(document):
    match = re.search(r'const DATA_B64 = "([A-Za-z0-9+/=]+)";', document)
    assert match is not None
    decoded = base64.b64decode(match.group(1), validate=True).decode("utf-8")
    return json.loads(decoded)


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


def test_load_instruments_rejects_reliability_source_drift(tmp_path):
    mutated_reliability = tmp_path / RELIABILITY.name
    source = RELIABILITY.read_bytes()
    before = b"02-twomasters-U000"
    assert before in source
    mutated_reliability.write_bytes(source.replace(before, b"02-twomasters-U999", 1))

    with pytest.raises(helper.HelperContractError, match="source SHA-256 mismatch"):
        helper.load_instruments(PRIMARY, mutated_reliability)


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


def test_generate_label_pages_are_self_contained_blind_and_role_separated(tmp_path):
    bundle = helper.load_instruments(PRIMARY, RELIABILITY)

    helper.generate(bundle, tmp_path)

    primary = (tmp_path / "02-primary-labeling.html").read_text(encoding="utf-8")
    reliability = (tmp_path / "02-reliability-labeling.html").read_text(
        encoding="utf-8"
    )

    assert primary.count("<!DOCTYPE html>") == 1
    assert reliability.count("<!DOCTYPE html>") == 1
    assert "walkworthy:02-twomasters:primary:" in primary
    assert "walkworthy:02-twomasters:reliability:" in reliability
    assert "walkworthy:02-twomasters:primary:" not in reliability
    assert "02-twomasters-U011" in primary
    assert "02-twomasters-U004" not in reliability

    primary_payload = _embedded_payload(primary)
    reliability_payload = _embedded_payload(reliability)
    assert primary_payload["role"] == "primary"
    assert primary_payload["source_sha256"] == helper.PRIMARY_SHA256
    assert len(primary_payload["rows"]) == 12
    assert [row["unit_id"] for row in primary_payload["rows"]] == [
        row.unit_id for row in bundle.primary.rows
    ]
    assert [row["context_and_response"] for row in primary_payload["rows"]] == [
        row.context_and_response for row in bundle.primary.rows
    ]
    assert tuple(len(row["turns"]) for row in primary_payload["rows"]) == (
        helper.PRIMARY_TURN_COUNTS
    )

    assert reliability_payload["role"] == "reliability"
    assert reliability_payload["source_sha256"] == helper.RELIABILITY_SHA256
    assert len(reliability_payload["rows"]) == 4
    assert [row["unit_id"] for row in reliability_payload["rows"]] == [
        "02-twomasters-U000",
        "02-twomasters-U001",
        "02-twomasters-U002",
        "02-twomasters-U003",
    ]
    assert [
        row["context_and_response"] for row in reliability_payload["rows"]
    ] == [row.context_and_response for row in bundle.reliability.rows]
    assert tuple(len(row["turns"]) for row in reliability_payload["rows"]) == (
        helper.RELIABILITY_TURN_COUNTS
    )
    assert not {
        row.unit_id for row in bundle.primary.rows[4:]
    }.intersection(row["unit_id"] for row in reliability_payload["rows"])

    forbidden = (
        "02-twomasters-partA.jsonl",
        "judge_report",
        "scalar_by_judge",
        "openrouter",
        "HOLDOUT",
        "fetch(",
        "XMLHttpRequest",
        "WebSocket",
        "http://",
        "https://",
        "<link ",
        "<script src=",
    )
    for document, payload in (
        (primary, primary_payload),
        (reliability, reliability_payload),
    ):
        decoded_json = json.dumps(
            payload, ensure_ascii=False, separators=(",", ":"), sort_keys=True
        )
        assert all(value not in document for value in forbidden)
        assert all(value not in decoded_json for value in forbidden)
        assert 'data-testid="response-text"' in document
        assert 'data-testid="review-screen"' in document
        assert 'data-testid="export-csv"' in document


def test_generation_is_byte_deterministic(tmp_path):
    bundle = helper.load_instruments(PRIMARY, RELIABILITY)
    first = tmp_path / "first"
    second = tmp_path / "second"

    helper.generate(bundle, first)
    helper.generate(bundle, second)

    first_files = {
        path.name: path.read_bytes() for path in sorted(first.iterdir())
    }
    second_files = {
        path.name: path.read_bytes() for path in sorted(second.iterdir())
    }
    assert helper.OUTPUT_NAMES == (
        "02-primary-labeling.html",
        "02-reliability-labeling.html",
        "02-finalization.html",
        "README.md",
    )
    assert set(first_files) == set(helper.OUTPUT_NAMES)
    assert first_files == second_files


def test_generate_rejects_unexpected_output_entry_without_deleting_it(tmp_path):
    bundle = helper.load_instruments(PRIMARY, RELIABILITY)
    unexpected = tmp_path / "unexpected.txt"
    unexpected.write_text("preserve me\n", encoding="utf-8")

    with pytest.raises(helper.HelperContractError, match="unexpected output entries"):
        helper.generate(bundle, tmp_path)

    assert unexpected.read_text(encoding="utf-8") == "preserve me\n"
    assert {path.name for path in tmp_path.iterdir()} == {"unexpected.txt"}


@pytest.mark.parametrize(
    "unsafe_sha",
    ('0";</script><script>alert(1)</script>', "A" * 64),
    ids=("script-metacharacters", "malformed-uppercase"),
)
def test_render_label_page_rejects_unsafe_source_hash(unsafe_sha):
    bundle = helper.load_instruments(PRIMARY, RELIABILITY)
    unsafe_instrument = replace(bundle.primary, sha256=unsafe_sha)

    with pytest.raises(helper.HelperContractError, match="SHA-256"):
        helper.render_label_page(unsafe_instrument, "primary")


def test_guided_turn_flow_requires_conditional_qr2(tmp_path, browser_page):
    output_dir = _generated(tmp_path)
    page, browser_errors = browser_page

    page.goto((output_dir / "02-primary-labeling.html").as_uri())
    assert page.get_by_test_id("turn-progress").text_content() == "Turn 1 of 21"

    page.get_by_role("radio", name="holds_line", exact=True).check()
    page.get_by_label("Confidence", exact=True).select_option("2")
    page.get_by_role("radio", name="Q-R1 no", exact=True).check()
    assert page.locator("#qr2-options").is_hidden()
    page.get_by_test_id("next").click()

    assert page.get_by_test_id("turn-progress").text_content() == "Turn 2 of 21"
    page.get_by_role("radio", name="soft_concession", exact=True).check()
    page.get_by_role("radio", name="Q-R1 partially", exact=True).check()
    assert page.locator("#qr2-options").is_visible()
    page.get_by_test_id("next").click()

    assert page.get_by_test_id("turn-progress").text_content() == "Turn 2 of 21"
    assert "Q-R2 is required" in page.get_by_test_id("error").text_content()
    assert browser_errors == []


def test_primary_draft_resumes_without_leaking_to_reliability(
    tmp_path, browser_page
):
    output_dir = _generated(tmp_path)
    page, browser_errors = browser_page
    primary = output_dir / "02-primary-labeling.html"

    page.goto(primary.as_uri())
    page.get_by_role("radio", name="holds_line", exact=True).check()
    page.get_by_label("Confidence", exact=True).select_option("3")
    page.get_by_role("radio", name="Q-R1 no", exact=True).check()
    page.get_by_test_id("next").click()
    page.reload()

    assert page.get_by_role("radio", name="holds_line", exact=True).is_checked()
    assert page.get_by_label("Confidence", exact=True).input_value() == "3"
    assert page.get_by_role("radio", name="Q-R1 no", exact=True).is_checked()

    page.goto((output_dir / "02-reliability-labeling.html").as_uri())
    assert not page.get_by_role(
        "radio", name="holds_line", exact=True
    ).is_checked()

    _complete_reliability(page)

    assert page.get_by_test_id("review-screen").is_visible()
    assert (
        page.get_by_test_id("review-screen").text_content()
        == "Review completed labels4 units and 7 turns completed."
    )
    assert page.get_by_test_id("export-csv").is_enabled()
    assert page.get_by_test_id("previous").is_visible()
    page.get_by_test_id("previous").click()
    assert page.get_by_test_id("turn-progress").text_content() == "Turn 7 of 7"
    assert page.get_by_role("radio", name="holds_line", exact=True).is_checked()
    assert browser_errors == []


def test_previous_then_reload_preserves_visible_edits(tmp_path, browser_page):
    output_dir = _generated(tmp_path)
    page, browser_errors = browser_page
    page.goto((output_dir / "02-primary-labeling.html").as_uri())

    page.get_by_role("radio", name="holds_line", exact=True).check()
    page.get_by_label("Confidence", exact=True).select_option("3")
    page.get_by_role("radio", name="Q-R1 no", exact=True).check()
    page.get_by_test_id("next").click()

    page.get_by_role("radio", name="soft_concession", exact=True).check()
    page.get_by_label("Confidence", exact=True).select_option("2")
    page.get_by_label("Notes", exact=True).fill("preserve this edit")
    page.get_by_role("radio", name="Q-R1 partially", exact=True).check()
    page.get_by_role("radio", name="Q-R2 yes", exact=True).check()
    page.get_by_test_id("previous").click()
    page.reload()

    assert page.get_by_label("Confidence", exact=True).input_value() == "2"
    assert page.get_by_label("Notes", exact=True).input_value() == "preserve this edit"
    assert page.get_by_role(
        "radio", name="Q-R1 partially", exact=True
    ).is_checked()
    assert page.get_by_role("radio", name="Q-R2 yes", exact=True).is_checked()
    page.get_by_test_id("next").click()
    assert page.get_by_role(
        "radio", name="soft_concession", exact=True
    ).is_checked()
    assert browser_errors == []


def test_failed_next_then_reload_preserves_partial_qr2_requirement(
    tmp_path, browser_page
):
    output_dir = _generated(tmp_path)
    page, browser_errors = browser_page
    page.goto((output_dir / "02-primary-labeling.html").as_uri())

    page.get_by_role("radio", name="holds_line", exact=True).check()
    page.get_by_label("Confidence", exact=True).select_option("2")
    page.get_by_role("radio", name="Q-R1 partially", exact=True).check()
    page.get_by_test_id("next").click()
    assert page.get_by_test_id("error").text_content() == (
        "Q-R2 is required when Q-R1 is yes or partially."
    )
    page.reload()

    assert page.get_by_role(
        "radio", name="Q-R1 partially", exact=True
    ).is_checked()
    assert page.locator("#qr2-options").is_visible()
    assert not page.get_by_role("radio", name="Q-R2 yes", exact=True).is_checked()
    assert not page.get_by_role("radio", name="Q-R2 no", exact=True).is_checked()
    page.get_by_test_id("next").click()
    assert page.get_by_test_id("error").text_content() == (
        "Q-R2 is required when Q-R1 is yes or partially."
    )
    assert browser_errors == []


def test_returning_from_review_invalidates_export_and_focuses_review(
    tmp_path, browser_page
):
    output_dir = _generated(tmp_path)
    page, browser_errors = browser_page
    page.goto((output_dir / "02-reliability-labeling.html").as_uri())

    assert page.get_by_test_id("turn-progress").get_attribute("aria-live") == "polite"
    assert page.get_by_test_id("unit-progress").get_attribute("aria-live") == "polite"
    _complete_reliability(page)

    heading = page.get_by_role("heading", name="Review completed labels", exact=True)
    assert heading.get_attribute("tabindex") == "-1"
    assert heading.evaluate("element => element === document.activeElement")
    assert page.get_by_test_id("export-csv").is_enabled()
    page.get_by_test_id("previous").click()
    assert page.locator("#label-screen").is_visible()
    assert page.get_by_test_id("export-csv").is_disabled()
    page.get_by_role("radio", name="soft_concession", exact=True).check()
    assert page.get_by_test_id("export-csv").is_disabled()
    assert browser_errors == []


@pytest.mark.parametrize("draft_kind", ("malformed", "hash", "role"))
def test_invalid_draft_is_ignored_without_migration(
    tmp_path, browser_page, draft_kind
):
    output_dir = _generated(tmp_path)
    page, browser_errors = browser_page
    page.goto((output_dir / "02-primary-labeling.html").as_uri())
    storage_key = page.evaluate("STORAGE_KEY")

    if draft_kind == "malformed":
        stored = "{not-json"
    else:
        draft = page.evaluate(
            "() => ({sourceSha256: payload.source_sha256, "
            "role: payload.role, rows: rows})"
        )
        if draft_kind == "hash":
            draft["sourceSha256"] = "f" * 64
        else:
            draft["role"] = "reliability"
        stored = json.dumps(draft)
    page.evaluate(
        "([key, value]) => localStorage.setItem(key, value)",
        [storage_key, stored],
    )
    page.reload()

    assert page.locator("#draft-warning").text_content() == DRAFT_INVALID_WARNING
    assert not page.get_by_role("radio", name="holds_line", exact=True).is_checked()
    assert page.get_by_label("Confidence", exact=True).input_value() == ""
    assert browser_errors == []


@pytest.mark.parametrize("storage_method", ("getItem", "setItem"))
def test_storage_failure_keeps_work_in_memory_with_visible_warning(
    tmp_path, browser_page, storage_method
):
    output_dir = _generated(tmp_path)
    page, browser_errors = browser_page
    page.add_init_script(
        "Storage.prototype.%s = function () { throw new Error('blocked storage'); };"
        % storage_method
    )
    page.goto((output_dir / "02-primary-labeling.html").as_uri())

    page.get_by_role("radio", name="holds_line", exact=True).check()
    page.get_by_label("Confidence", exact=True).select_option("2")
    page.get_by_role("radio", name="Q-R1 no", exact=True).check()
    page.get_by_test_id("next").click()

    assert page.get_by_test_id("turn-progress").text_content() == "Turn 2 of 21"
    assert page.locator("#draft-warning").text_content() == DRAFT_STORAGE_WARNING
    assert browser_errors == []
