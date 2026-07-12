"""R49 offline OPEN re-parse from the immutable MVP transcripts."""

from __future__ import annotations

import hashlib
import importlib
import json
import os
import sys
from pathlib import Path

import pytest

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)


PROJECT = Path(HARNESS).parent
TRANSCRIPTS = PROJECT / "07-PILOTS/20260710-mvp-run/transcripts.jsonl"
MANIFEST = PROJECT / (
    "07-PILOTS/20260712-artifact-corrected-requal/"
    "20260712-artifact-corrected-requal-manifest.json"
)
BANK = PROJECT / "05-BANK-YAML"


def _module():
    return importlib.import_module("mvp_open_reparse")


def _digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


@pytest.fixture(scope="module")
def outcome():
    return _module().reparse_open(
        transcripts_path=str(TRANSCRIPTS), bank_dir=str(BANK), manifest_path=str(MANIFEST)
    )


def test_reparse_covers_all_open_cells_and_exact_r48_marker_population(outcome):
    assert len(outcome.corrected_records) == 309
    assert len(outcome.delta_rows) == 309
    assert outcome.marker_hit_verdicts == 155
    assert outcome.marker_hit_cells == 65
    assert outcome.consumed_verdict_texts == outcome.available_verdict_texts == 1688
    assert sum(row["marker_hit_verdicts"] for row in outcome.delta_rows) == 155
    assert sum(bool(row["marker_hit_verdicts"]) for row in outcome.delta_rows) == 65


def test_reparse_is_read_only_against_historical_transcripts():
    before = _digest(TRANSCRIPTS)
    _module().reparse_open(
        transcripts_path=str(TRANSCRIPTS), bank_dir=str(BANK), manifest_path=str(MANIFEST)
    )
    assert _digest(TRANSCRIPTS) == before


def test_delta_rows_include_corrected_headlines_and_per_judge_scores(outcome):
    row = next(
        row for row in outcome.delta_rows
        if row["item_id"] == "DUTY-C3-008"
        and row["model"] == "meta-llama/llama-3.1-8b-instruct"
    )
    assert row["marker_hit_verdicts"] > 0
    assert row["corrected"]["headline"] is not None
    assert {j["name"] for j in row["per_judge"]} == {
        "gpt4omini", "gemini-flash", "grok-4.20"
    }
    gemini = next(j for j in row["per_judge"] if j["name"] == "gemini-flash")
    assert gemini["before"]["matter"] is None
    assert gemini["after"]["matter"] == pytest.approx(0.125)


def test_r42_screen_contains_only_the_two_already_adjudicated_corrections(outcome):
    assert outcome.r42_known_corrections == [
        {
            "item_id": "MEND-C5-W204",
            "model": "meta-llama/llama-3.1-8b-instruct",
            "judge": "gemini-flash",
            "axis": "matter",
            "before": 0.0,
            "after": 0.25,
        },
        {
            "item_id": "WHOLE-C1-004",
            "model": "deepseek/deepseek-chat",
            "judge": "gemini-flash",
            "axis": "manner",
            "before": 2.5,
            "after": 0.5,
        },
    ]
    assert outcome.r42_new_material_candidates == []


def test_disagreement_is_recomputed_from_corrected_eligibility(outcome):
    assert len(outcome.disagreement_cells) == 309
    assert all(cell["kind"] == "open" for cell in outcome.disagreement_cells)
    assert all(cell["eligible_spread"] == 0.0 for cell in outcome.disagreement_cells)
    assert all(
        [value["name"] for value in values if value["eligible"]] == ["gemini-flash"]
        for cell in outcome.disagreement_cells
        for values in cell["judge_values"].values() if values
    )


def test_report_is_descriptive_and_carries_f4_historical_footnote(outcome):
    report = _module().render_report(outcome, timestamp="2026-07-12T12:00:00")
    assert "DESCRIPTIVE / PRE-GATE" in report
    assert "155" in report and "65" in report
    assert "pre-bridge probe-stability" in report
    assert "F-4" in report
    assert "No new R42-material candidate" in report


def test_write_event_is_create_only_and_preserves_source(tmp_path, outcome):
    module = _module()
    before = _digest(TRANSCRIPTS)
    out = tmp_path / "event"
    paths = module.write_event(
        outcome, out_dir=str(out), timestamp="2026-07-12T12:00:00"
    )
    assert set(Path(path).name for path in paths.values()) == {
        module.TRANSCRIPTS_NAME,
        module.DELTA_NAME,
        module.DISAGREEMENT_NAME,
        module.REPORT_NAME,
    }
    assert len(Path(paths["transcripts"]).read_text().splitlines()) == 309
    delta = json.loads(Path(paths["delta"]).read_text())
    assert delta["marker_hit_verdicts"] == 155
    assert delta["marker_hit_cells"] == 65
    assert _digest(TRANSCRIPTS) == before
    with pytest.raises(module.OutputPathError):
        module.write_event(outcome, out_dir=str(out), timestamp="2026-07-12T12:00:00")
