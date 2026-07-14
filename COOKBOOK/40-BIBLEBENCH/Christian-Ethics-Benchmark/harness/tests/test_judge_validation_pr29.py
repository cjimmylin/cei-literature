"""PR-29: complete, reliability-backed, fail-closed G4 label intake."""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import pytest

from walkworthy import judge_validation as jv


DESIGN = "01-goodsamaritan"
FIELDS = [
    "unit_id", "design", "context_and_response", "action_class",
    "rationale_quality", "confidence_1_3", "notes", "Q-R1_declines",
    "Q-R2_avoids_keyed_wrong",
]


def _verdict(judge: str, action_class: str) -> dict:
    return {
        "judge": judge,
        "unit": "item",
        "scores": {"action_class": action_class, "rationale_quality": 1},
        "per_unit": [],
        "refused": False,
    }


def _write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def _read_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _bundle(tmp_path: Path, primary_rows: list[dict]) -> tuple[Path, Path]:
    labels = tmp_path / "labels"
    _write_csv(labels / f"{DESIGN}-partA-blind.csv", primary_rows)
    provenance = []
    panel_rows = []
    for index, row in enumerate(primary_rows):
        item_id = f"WW-01-PR29-{index}"
        provenance.append({
            "unit_id": row["unit_id"], "design": DESIGN,
            "item_id": item_id, "model": "mock/sut",
        })
        action = "full_obedience" if index == 0 else "objective_first"
        panel_rows.append({
            "design": DESIGN, "item_id": item_id, "model": "mock/sut",
            "refusal_tag": ("appropriate_refusal" if index else "helpful"),
            "refusal_reason": ({"main": "principled_noncompliance"} if index else
                               {"main": None}),
            "refusal_lexical": {"main": {"is_refusal": bool(index)}},
            "judge_report": {"verdicts": [
                _verdict("judge-a", action), _verdict("judge-b", action),
            ]},
        })
    (labels / f"{DESIGN}-partA.jsonl").write_text(
        "".join(json.dumps(row) + "\n" for row in provenance), encoding="utf-8")
    panel = tmp_path / "scored_items.jsonl"
    panel.write_text(
        "".join(json.dumps(row) + "\n" for row in panel_rows), encoding="utf-8")
    return labels, panel


def _row(index: int, action: str = "", *, q1: str = "", q2: str = "",
         confidence: str = "") -> dict:
    return {
        "unit_id": f"{DESIGN}-U{index:03d}", "design": DESIGN,
        "context_and_response": f"blind response {index}",
        "action_class": action,
        "rationale_quality": ("1" if action else ""),
        "confidence_1_3": confidence, "notes": "",
        "Q-R1_declines": q1, "Q-R2_avoids_keyed_wrong": q2,
    }


def test_materializes_first_blind_rows_and_hashes_source_template(tmp_path):
    labels, _ = _bundle(tmp_path, [_row(0), _row(1), _row(2)])
    out = tmp_path / "reliability"

    result = jv.materialize_reliability_instruments(
        labels, out, overlap_counts={DESIGN: 2})

    manifest = json.loads(result["manifest"].read_text(encoding="utf-8"))
    entry = manifest["designs"][DESIGN]
    assert entry["unit_ids"] == [f"{DESIGN}-U000", f"{DESIGN}-U001"]
    assert entry["row_count"] == 3
    assert entry["overlap_count"] == 2
    source = labels / f"{DESIGN}-partA-blind.csv"
    assert entry["source_csv_sha256"] == hashlib.sha256(source.read_bytes()).hexdigest()
    reliability = _read_csv(out / f"{DESIGN}-partA-overlap-blind.csv")
    reliability_path = out / f"{DESIGN}-partA-overlap-blind.csv"
    assert entry["reliability_instrument_sha256"] == hashlib.sha256(
        reliability_path.read_bytes()).hexdigest()
    assert [row["context_and_response"] for row in reliability] == [
        "blind response 0", "blind response 1"]
    assert all(not row["action_class"] and not row["Q-R1_declines"]
               for row in reliability)


def test_rejects_partially_filled_primary_design(tmp_path):
    labels, panel = _bundle(
        tmp_path,
        [_row(0, "full_obedience", q1="no", q2="n-a", confidence="3"), _row(1)],
    )

    with pytest.raises(jv.JudgeValidationError, match="partial design submission"):
        jv.collect_comparisons(labels, panel)


def test_reliability_declaration_enforces_test_retest_washout_and_ratification():
    declaration = {
        "mode": "test_retest", "primary_labeler_id": "labeler-a",
        "reliability_labeler_id": "labeler-a",
        "primary_completed_at": "2026-07-01T00:00:00+00:00",
        "reliability_completed_at": "2026-07-10T00:00:00+00:00",
        "test_retest_ratified": True,
    }
    with pytest.raises(jv.JudgeValidationError, match="14 elapsed days"):
        jv.validate_reliability_declaration(declaration)

    declaration["reliability_completed_at"] = "2026-07-15T00:00:00+00:00"
    declaration["test_retest_ratified"] = False
    with pytest.raises(jv.JudgeValidationError, match="ratification"):
        jv.validate_reliability_declaration(declaration)


def test_rejects_manifest_overlap_count_drift(tmp_path, monkeypatch):
    monkeypatch.setattr(jv, "OVERLAP_COUNTS", {DESIGN: 2})
    primary = [
        _row(0, "full_obedience", q1="no", q2="n-a", confidence="3"),
        _row(1, "objective_first", q1="no", q2="n-a", confidence="3"),
    ]
    labels, panel = _bundle(tmp_path, primary)
    reliability = tmp_path / "reliability"
    generated = jv.materialize_reliability_instruments(
        labels, reliability, overlap_counts={DESIGN: 2})
    second = _read_csv(reliability / f"{DESIGN}-partA-overlap-blind.csv")
    second[0].update({
        "action_class": "full_obedience", "rationale_quality": "1",
        "confidence_1_3": "3", "Q-R1_declines": "no",
        "Q-R2_avoids_keyed_wrong": "n-a",
    })
    _write_csv(reliability / f"{DESIGN}-partA-overlap-blind.csv", second[:1])
    manifest = json.loads(generated["manifest"].read_text(encoding="utf-8"))
    manifest["designs"][DESIGN]["overlap_count"] = 1
    manifest["designs"][DESIGN]["unit_ids"] = manifest["designs"][DESIGN]["unit_ids"][:1]
    generated["manifest"].write_text(json.dumps(manifest), encoding="utf-8")
    declaration = reliability / "reliability-declaration.json"
    declaration.write_text(json.dumps({
        "mode": "second_labeler", "primary_labeler_id": "labeler-a",
        "reliability_labeler_id": "labeler-b",
        "primary_completed_at": "2026-07-14T08:00:00+00:00",
        "reliability_completed_at": "2026-07-14T09:00:00+00:00",
    }), encoding="utf-8")
    adjudications = reliability / "adjudications.jsonl"
    adjudications.write_text("", encoding="utf-8")

    with pytest.raises(jv.JudgeValidationError, match="overlap_count mismatch"):
        jv.collect_g4_inputs(
            labels, panel, generated["manifest"], reliability,
            declaration, adjudications)


def test_complete_bundle_computes_ceiling_gold_detector_and_cli_report(
        tmp_path, monkeypatch):
    monkeypatch.setattr(jv, "OVERLAP_COUNTS", {DESIGN: 2})
    primary = [
        _row(0, "full_obedience", q1="no", q2="n-a", confidence="3"),
        _row(1, "objective_first", q1="yes", q2="yes", confidence="2"),
    ]
    labels, panel = _bundle(tmp_path, primary)
    reliability = tmp_path / "reliability"
    generated = jv.materialize_reliability_instruments(
        labels, reliability, overlap_counts={DESIGN: 2})
    second = _read_csv(reliability / f"{DESIGN}-partA-overlap-blind.csv")
    second[0].update({"action_class": "full_obedience", "rationale_quality": "1",
                      "confidence_1_3": "3", "Q-R1_declines": "no",
                      "Q-R2_avoids_keyed_wrong": "n-a"})
    second[1].update({"action_class": "partial", "rationale_quality": "1",
                      "confidence_1_3": "2", "Q-R1_declines": "yes",
                      "Q-R2_avoids_keyed_wrong": "yes"})
    _write_csv(reliability / f"{DESIGN}-partA-overlap-blind.csv", second)
    declaration = reliability / "reliability-declaration.json"
    declaration.write_text(json.dumps({
        "mode": "second_labeler", "primary_labeler_id": "labeler-a",
        "reliability_labeler_id": "labeler-b",
        "primary_completed_at": "2026-07-14T08:00:00+00:00",
        "reliability_completed_at": "2026-07-14T09:00:00+00:00",
    }), encoding="utf-8")
    adjudications = reliability / "adjudications.jsonl"
    adjudications.write_text(json.dumps({
        "unit_id": f"{DESIGN}-U001", "category": "action_class", "member": None,
        "primary_value": "objective_first", "reliability_value": "partial",
        "gold_value": "partial", "adjudicator": "Jimmy", "adjudicated": True,
    }) + "\n", encoding="utf-8")

    bundle = jv.collect_g4_inputs(
        labels, panel, generated["manifest"], reliability, declaration, adjudications)

    assert bundle["ceilings"][(DESIGN, "action_class")] is not None
    changed = [row for row in bundle["comparisons"]
               if row["unit_id"].endswith("U001")]
    assert changed and {row["human_label"] for row in changed} == {"partial"}
    detector = bundle["detectors"][DESIGN]
    assert detector["precision"] == 1.0 and detector["recall"] == 1.0
    assert detector["q_r2_yes_contradiction_rate"] == 0.0

    results = jv.compute_results(bundle["comparisons"], bundle["ceilings"])
    assert all(not row.get("pending_ceiling") for row in results.values())
    report = jv.render_report(
        results, "20260714", detector_results=bundle["detectors"],
        reliability=bundle["reliability"])
    assert "second_labeler" in report
    assert "Q-R1/Q-R2 detector validation" in report

    out = tmp_path / "g4-report.md"
    assert jv.main([
        "--labels", str(labels), "--run-path", str(panel), "--out", str(out),
        "--date", "20260714", "--reliability-manifest", str(generated["manifest"]),
        "--reliability-labels", str(reliability),
        "--reliability-declaration", str(declaration),
        "--adjudications", str(adjudications),
    ]) == 0
    assert "PENDING-CEILING" not in out.read_text(encoding="utf-8")
