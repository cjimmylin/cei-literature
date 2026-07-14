import csv
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace

import pytest

import ppp1_packet as packet


def _items():
    designs = list(packet.DESIGN_ORDER)
    items = []
    for index in range(226):
        design = designs[index % len(designs)]
        extra = {"contested": True} if index < 4 else {}
        if 4 <= index < 26:
            design = "narrowgate"
            extra = {"episode": True}
        items.append(SimpleNamespace(
            id=f"ITEM-{index:03d}", design=design, extra=extra,
            commandments=["C1"], tier="T2", track="A"))
    return items


def _write_final_run(run_dir: Path, items):
    run_dir.mkdir(exist_ok=True)
    cell_keys = []
    records = []
    raw_rows = []
    for item_index, item in enumerate(items):
        for sut_index, sut in enumerate(packet.SUT_ORDER):
            key = f"{item.id}::{sut}"
            cell_keys.append(key)
            if item.extra.get("contested"):
                verdicts = ["contested disclosure", "contested position",
                            "contested coherence", "contested settled core"]
                record = {
                    "cell_key": key, "item_id": item.id, "sut": sut,
                    "status": "scored", "scores": {
                        "kind": "contested", "fraction": None,
                        "contested": {"disclosure": 1.0, "coherence": 0.5,
                                      "settled_core_fraction": 0.75}},
                    "judge_raw": [{"verdict_texts": verdicts}]}
            elif item.extra.get("episode"):
                verdicts = ["episode verdict"]
                record = {
                    "cell_key": key, "item_id": item.id, "sut": sut,
                    "status": "scored", "judge": {
                        "score": (sut_index + 1) / 4,
                        "per_judge": [{"verdict_text": verdicts[0]}]}}
            elif item_index == 26 and sut_index == 1:
                record = {
                    "cell_key": key, "item_id": item.id, "sut": sut,
                    "status": "error", "error": "JudgeError: retained, not imputed"}
            else:
                kind = "anchor" if item_index < 49 else "open"
                verdicts = ["open verdict"] if kind == "open" else []
                record = {
                    "cell_key": key, "item_id": item.id, "sut": sut,
                    "status": "scored", "scores": {
                        "kind": kind, "fraction": (item_index % 5) / 4,
                        "scored": True,
                        "triaxial": ({"matter": 0.25, "manner": 0.5, "end": 0.75}
                                     if kind == "open" else None)},
                    "judge_raw": ([{"verdict_texts": verdicts}] if verdicts else None)}
            calls = [{"role": "sut", "name": sut, "model": sut,
                      "usage": {"cost": 0.001}}]
            texts = ["sut emission"]
            for verdict in locals().get("verdicts", []):
                calls.append({"role": "judge", "name": "gemini-flash",
                              "model": packet.JUDGE, "usage": {"cost": 0.002}})
                texts.append(verdict)
            record["usage"] = {
                "calls": calls,
                "attributed_cost_usd": sum(call["usage"]["cost"] for call in calls),
            }
            for call, text in zip(calls, texts):
                raw_rows.append({
                    "kind": "raw_emission", "role": call["role"],
                    "name": call["name"], "slug": call["model"],
                    "item_id": item.id, "text": text,
                    "usage": [{"model": call["model"], "usage": call["usage"]}],
                    "error": None,
                })
            records.append(record)
            verdicts = []
    identity = {
        "validity_label": packet.VALIDITY_LABEL,
        "artifact_kind": packet.VALIDITY_LABEL,
        "expected_cells": 678, "runnable_items": 226,
        "suts": list(packet.SUT_ORDER), "judge": packet.JUDGE,
        "sut_max_tokens": 2048, "judge_max_tokens": 512,
        "budget_usd": 23.56, "cell_keys": cell_keys,
    }
    metadata = {
        "validity_label": packet.VALIDITY_LABEL,
        "run_status": "COMPLETE", "expected_cells": 678,
        "recorded_cells": 678,
        "scored_cells": 677, "error_cells": 1,
        "identity": identity,
    }
    (run_dir / "ppp1-run-identity.json").write_text(
        json.dumps(identity), encoding="utf-8")
    (run_dir / "run-metadata.json").write_text(
        json.dumps(metadata), encoding="utf-8")
    (run_dir / "checkpoint.jsonl").write_text(
        "".join(json.dumps(record) + "\n" for record in records), encoding="utf-8")
    (run_dir / "raw-evidence.jsonl").write_text(
        "".join(json.dumps(record) + "\n" for record in raw_rows), encoding="utf-8")
    (run_dir / "ppp1-report.md").write_text(
        f"> **{packet.VALIDITY_LABEL}**\n", encoding="utf-8")


def _manuscript_sources(root: Path):
    root.mkdir()
    for name in packet.MANUSCRIPT_SOURCE_NAMES:
        (root / name).write_text(f"# {name}\n\nBase prose.\n", encoding="utf-8")


def _bank_source(root: Path):
    root.mkdir()
    (root / "frozen.yaml").write_text("frozen: true\n", encoding="utf-8")


def test_packet_requires_final_metadata_and_refuses_existing_destination(tmp_path):
    run_dir = tmp_path / "run"
    run_dir.mkdir()
    output = tmp_path / "packet"
    with pytest.raises(packet.PacketError, match="run-metadata"):
        packet.build_packet(run_dir, output, _items(), tmp_path)

    _write_final_run(run_dir, _items())
    _manuscript_sources(tmp_path / "paper")
    output.mkdir()
    with pytest.raises(packet.PacketError, match="already exists"):
        packet.build_packet(run_dir, output, _items(), tmp_path / "paper")


def test_builds_labeled_traceable_packet_without_imputing_errors_or_copying_raw(tmp_path):
    items = _items()
    run_dir = tmp_path / "run"
    paper = tmp_path / "paper"
    output = tmp_path / "packet"
    _write_final_run(run_dir, items)
    _manuscript_sources(paper)
    bank = tmp_path / "bank"
    _bank_source(bank)

    packet.build_packet(run_dir, output, items, paper, bank)

    expected = {
        "00-README.md", "01-source-manifest.json", "02-normalized-cells.csv",
        "03-traceability.csv", "04-traceability.md", "05-preview-results.md",
        "06-preview-discussion.md", "07-preview-limitations.md",
        "08-assembled-manuscript-preview.md",
        "tables/01-per-design-per-sut.csv", "tables/01-per-design-per-sut.md",
        "tables/02-per-sut-aggregate.csv", "tables/02-per-sut-aggregate.md",
        "tables/03-overall-aggregate.csv", "tables/03-overall-aggregate.md",
        "figures/01-design-by-sut.svg", "figures/02-per-sut-aggregate.svg",
    }
    files = {str(path.relative_to(output)) for path in output.rglob("*") if path.is_file()}
    assert files == expected
    for path in output.rglob("*"):
        if path.is_file():
            assert packet.VALIDITY_LABEL in path.read_text(encoding="utf-8")

    with (output / "02-normalized-cells.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 678
    required = {
        "raw_line_start", "raw_line_end", "raw_line_count", "raw_span_sha256",
        "raw_call_hashes", "call_count", "cell_cost_usd", "judge_text_sha256s",
        "judge_hashes_match", "matter", "manner", "end",
    }
    assert required <= set(rows[0])
    assert [int(row["raw_line_start"]) for row in rows] == [
        1 + sum(int(prior["call_count"]) for prior in rows[:index])
        for index in range(len(rows))]
    open_row = next(row for row in rows if row["kind"] == "open")
    assert (open_row["matter"], open_row["manner"], open_row["end"]) == (
        "0.25", "0.5", "0.75")
    assert open_row["judge_hashes_match"] == "True"
    error = next(row for row in rows if row["status"] == "error")
    assert error["headline_score"] == ""
    assert error["score_path"] == ""
    assert "retained, not imputed" in error["error"]
    assert all("sut_prompt" not in row and "sut_response" not in row for row in rows)

    with (output / "tables/02-per-sut-aggregate.csv").open(
            newline="", encoding="utf-8") as handle:
        aggregates = list(csv.DictReader(handle))
    deepseek = next(row for row in aggregates if row["sut"] == packet.SUT_ORDER[1])
    assert deepseek["expected_n"] == "226"
    assert deepseek["headline_expected_n"] == "222"
    assert deepseek["numeric_n"] == "221"
    assert deepseek["error_n"] == "1"
    assert deepseek["contested_n"] == "4"
    assert float(deepseek["coverage"]) == pytest.approx(221 / 222)
    assert deepseek["ci_method"].startswith("design-stratified item bootstrap")
    assert deepseek["open_matter_n"] != "0"
    assert deepseek["open_matter_mean"] == "0.25"

    manifest = json.loads((output / "01-source-manifest.json").read_text())
    assert len(manifest["input_artifacts"]) == 10
    assert all({"path", "sha256", "bytes", "selected_version"} <= set(row)
               for row in manifest["input_artifacts"])
    assert {row["artifact_kind"] for row in manifest["input_artifacts"]} >= {
        "run_identity", "checkpoint", "raw_evidence", "final_metadata",
        "final_report", "frozen_bank", "manuscript_source"}

    trace = (output / "03-traceability.csv").read_text(encoding="utf-8")
    assert "checkpoint.jsonl" in trace
    assert "scores.fraction" in trace
    assert "judge.score" in trace
    trace_rows = list(csv.DictReader((output / "03-traceability.csv").open(
        newline="", encoding="utf-8")))
    assert {"displayed_value", "value_reference"} <= set(trace_rows[0])
    assert any(row["displayed_field"] == "headline_missing_n" for row in trace_rows)
    assert any(row["displayed_field"] == "design_sut_row_count" for row in trace_rows)
    assembled = (output / "08-assembled-manuscript-preview.md").read_text(
        encoding="utf-8")
    assert "Base prose." in assembled
    assert "\n> single Gemini judge" in assembled
    assert "uses a > single" not in assembled
    forbidden = ("gate pass", "release-ready", "cross-family consensus", "T4 complete")
    assert not any(term in assembled for term in forbidden)


def test_rejects_foreign_roster_and_duplicate_or_missing_checkpoint_cells(tmp_path):
    items = _items()
    run_dir = tmp_path / "run"
    _write_final_run(run_dir, items)
    identity_path = run_dir / "ppp1-run-identity.json"
    identity = json.loads(identity_path.read_text())
    identity["judge"] = "substitute/judge"
    identity_path.write_text(json.dumps(identity), encoding="utf-8")
    with pytest.raises(packet.PacketError, match="identity"):
        packet.build_packet(run_dir, tmp_path / "out-a", items, tmp_path)

    _write_final_run(tmp_path / "run-b", items)
    checkpoint = tmp_path / "run-b" / "checkpoint.jsonl"
    lines = checkpoint.read_text().splitlines()
    checkpoint.write_text("\n".join(lines[:-1] + [lines[0]]) + "\n", encoding="utf-8")
    with pytest.raises(packet.PacketError, match="checkpoint"):
        packet.build_packet(tmp_path / "run-b", tmp_path / "out-b", items, tmp_path)
