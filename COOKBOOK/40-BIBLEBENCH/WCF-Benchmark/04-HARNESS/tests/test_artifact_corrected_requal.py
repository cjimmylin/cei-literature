"""R47.3 offline correction event from the immutable Task-4 evidence."""

from __future__ import annotations

import importlib
import json
import os
import sys
from pathlib import Path

import pytest

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)

from wcfbench.judge_panel import JudgePanel  # noqa: E402


RAW = Path(HARNESS).parent / "07-PILOTS/20260711-format-bridge-requal/raw_verdicts.jsonl"

EXPECTED = {
    "gemini-flash": {
        "g4": 8, "award_consistency": 8, "discrimination": 8,
        "disclosure_inversion": 8, "negative_disclosure": 8, "settled_core": 8,
    },
    "grok-4.20": {
        "g4": 8, "award_consistency": 8, "discrimination": 0,
        "disclosure_inversion": 8, "negative_disclosure": 8, "settled_core": 8,
    },
    "cohere-command-a": {
        "g4": 0, "award_consistency": 8, "discrimination": 0,
    },
    "amazon-nova-pro": {
        "g4": 1, "award_consistency": 8, "discrimination": 1,
    },
}


def _module():
    return importlib.import_module("artifact_corrected_requal")


def test_reparse_matches_r47_expected_table_and_consumes_every_successful_invocation():
    module = _module()
    outcome = module.reparse_task4(str(RAW))
    assert outcome.pass_counts == EXPECTED
    assert outcome.consumed == outcome.available
    assert outcome.eligible_surfaces == {
        "gemini-flash": {"open_award", "coherence", "disclosure", "settled_core"},
        "grok-4.20": {"coherence", "disclosure", "settled_core"},
        "cohere-command-a": set(),
        "amazon-nova-pro": set(),
    }


def test_corrected_manifest_cites_sole_evidence_and_loads_production_panel():
    module = _module()
    outcome = module.reparse_task4(str(RAW))
    manifest = module.build_corrected_manifest(
        outcome, timestamp="2026-07-12T12:00:00", run_dir="07-PILOTS/test-correction"
    )
    assert manifest["source_evidence"] == str(RAW)
    assert manifest["source"] == "offline R48 re-parse of immutable Task-4 raw evidence"
    assert manifest["correction_authority"] == "R47.3"

    class NoCall:
        def complete(self, *_args, **_kwargs):
            raise AssertionError("manifest load must be offline")

    clients = [
        {"name": row["name"], "family": row["family"], "slug": row["slug"],
         "client": NoCall()}
        for row in manifest["judges"]
    ]
    panel = JudgePanel(clients, manifest=manifest)
    assert {name for name, _family, _client in panel.active} == {
        "gemini-flash", "grok-4.20"
    }
    assert panel.eligible["gemini-flash"] >= {"open_award"}
    assert "open_award" not in panel.eligible["grok-4.20"]


def test_report_has_single_family_label_exact_table_and_supersession_statement():
    module = _module()
    outcome = module.reparse_task4(str(RAW))
    report = module.render_report(outcome, timestamp="2026-07-12T12:00:00")
    assert "corrected manifest event under R47.3" in report
    assert "supersedes the as-executed Task-4 manifest as manifest of record" in report
    assert "SINGLE-FAMILY (google)" in report
    for judge, counts in EXPECTED.items():
        for probe, count in counts.items():
            assert f"| {judge} |" in report
            assert f"| {probe} | {count}/8 |" in report


def test_write_event_is_create_only_and_writes_no_raw_copy(tmp_path):
    module = _module()
    outcome = module.reparse_task4(str(RAW))
    out = tmp_path / "event"
    paths = module.write_event(
        outcome, out_dir=str(out), timestamp="2026-07-12T12:00:00"
    )
    assert set(Path(p).name for p in paths.values()) == {
        module.MANIFEST_NAME, module.REPORT_NAME
    }
    assert not any("raw" in p.name.lower() for p in out.iterdir())
    with pytest.raises(module.OutputPathError):
        module.write_event(outcome, out_dir=str(out), timestamp="2026-07-12T12:00:00")


def test_failed_or_retried_raw_attempts_reduce_to_final_success_per_invocation(tmp_path):
    module = _module()
    raw = tmp_path / "raw.jsonl"
    rows = [
        {"kind": "raw_call", "judge": "j", "family": "f", "slug": "f/j",
         "invocation": 1, "attempt": 0, "error": "temporary", "text": None},
        {"kind": "raw_call", "judge": "j", "family": "f", "slug": "f/j",
         "invocation": 1, "attempt": 1, "error": None, "text": "A: 3\nB: 1",
         "finish_reason": "stop", "truncated": False},
    ]
    raw.write_text("\n".join(json.dumps(row) for row in rows) + "\n")
    streams, metadata = module.load_replay_streams(str(raw))
    assert metadata == {"j": ("f", "f/j")}
    assert [row["text"] for row in streams["j"]] == ["A: 3\nB: 1"]
