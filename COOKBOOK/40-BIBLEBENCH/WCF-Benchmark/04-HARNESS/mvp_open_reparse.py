#!/usr/bin/env python
"""R49 offline OPEN re-parse of the immutable MVP transcript evidence."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import os
from dataclasses import dataclass
from types import SimpleNamespace
from typing import Any, Dict, List, Optional, Sequence

from wcfbench import load_items
from wcfbench.disagreement import summarize_disagreement
from wcfbench.judge import _UNWILLING_MARKERS
from wcfbench.qualification import OPEN_AWARD
from wcfbench.refusal import _REFUSAL_MARKERS
from wcfbench.triaxial import score_triaxial


HARNESS_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.normpath(os.path.join(HARNESS_ROOT, ".."))
SOURCE_RUN = "07-PILOTS/20260710-mvp-run"
TRANSCRIPTS_PATH = os.path.join(PROJECT_ROOT, SOURCE_RUN, "transcripts.jsonl")
MANIFEST_PATH = os.path.join(
    PROJECT_ROOT, "07-PILOTS", "20260712-artifact-corrected-requal",
    "20260712-artifact-corrected-requal-manifest.json",
)
BANK_DIR = os.path.join(PROJECT_ROOT, "05-BANK-YAML")
RUN_DIR = "07-PILOTS/20260712-mvp-open-reparse"
OUT_DIR = os.path.join(PROJECT_ROOT, RUN_DIR)
TRANSCRIPTS_NAME = "corrected-open-transcripts.jsonl"
DELTA_NAME = "delta-table.json"
DISAGREEMENT_NAME = "disagreement.json"
REPORT_NAME = "20260712-mvp-open-reparse-report.md"


class EvidenceError(RuntimeError):
    """Persisted MVP evidence cannot be replayed exactly."""


class OutputPathError(RuntimeError):
    """The append-only output directory already exists."""


class TranscriptReplay:
    def __init__(self, verdict_texts: Sequence[str]) -> None:
        self.verdict_texts = list(verdict_texts)
        self.index = 0
        self.last_finish_reason = "stop"
        self.last_truncated = False

    def complete(self, _prompt: str, item_id: Optional[str] = None) -> str:
        if self.index >= len(self.verdict_texts):
            raise EvidenceError(f"replay exhausted for {item_id}")
        text = self.verdict_texts[self.index]
        self.index += 1
        return text


@dataclass
class OpenReparseOutcome:
    source_transcripts: str
    manifest_path: str
    manifest_run_dir: str
    corrected_records: List[Dict[str, Any]]
    delta_rows: List[Dict[str, Any]]
    disagreement_cells: List[Dict[str, Any]]
    marker_hit_verdicts: int
    marker_hit_cells: int
    consumed_verdict_texts: int
    available_verdict_texts: int
    r42_known_corrections: List[Dict[str, Any]]
    r42_new_material_candidates: List[Dict[str, Any]]


def _historical_marker_hit(text: str) -> bool:
    low = (text or "").lower()
    return any(marker in low for marker in _UNWILLING_MARKERS + _REFUSAL_MARKERS)


def _score_snapshot(scores: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "matter": scores.get("matter"),
        "manner": scores.get("manner"),
        "end": scores.get("end"),
        "graded": dict(scores.get("graded") or {}),
        "awards": {str(k): v for k, v in (scores.get("awards") or {}).items()},
        "scale_defect": dict(scores.get("scale_defect") or {}),
    }


def _triaxial_scores(score: Any, eligible_surfaces: Sequence[str]) -> Dict[str, Any]:
    return {
        "matter": score.matter,
        "manner": score.manner,
        "end": score.end,
        "graded": dict(score.graded),
        "awards": {str(k): v for k, v in score.awards.items()},
        "award_axis": {str(k): v for k, v in score.award_axis.items()},
        "scale_defect": dict(score.scale_defect),
        "offmap": list(score.offmap),
        "compliance_defects": {str(k): v for k, v in score.compliance_defects.items()},
        "finish_reason": score.finish_reason,
        "retried": score.retried,
        "eligible_surfaces": sorted(eligible_surfaces),
    }


def _aggregate(judges: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    axes: Dict[str, Optional[float]] = {}
    for axis in ("matter", "manner", "end"):
        values = []
        for judge in judges:
            scores = judge.get("scores") or {}
            if OPEN_AWARD not in (scores.get("eligible_surfaces") or []):
                continue
            if (scores.get("scale_defect") or {}).get(axis):
                continue
            value = scores.get(axis)
            if value is not None:
                values.append(float(value))
        axes[axis] = sum(values) / len(values) if values else None
    matter = axes["matter"]
    axes["headline"] = None if matter is None else max(0.0, min(1.0, matter))
    return axes


def _axis_changes(before: Dict[str, Any], after: Dict[str, Any]) -> List[Dict[str, Any]]:
    return [
        {"axis": axis, "before": before.get(axis), "after": after.get(axis)}
        for axis in ("matter", "manner", "end")
        if before.get(axis) != after.get(axis)
    ]


_R42_REFERENCED_CELLS = {
    ("WHOLE-C1-004", "deepseek/deepseek-chat"),
    ("MEND-C5-W204", "meta-llama/llama-3.1-8b-instruct"),
    ("MEND-C1-W201", "deepseek/deepseek-chat"),
    ("MEND-C2-005", "anthropic/claude-haiku-4.5"),
    ("WHOLE-C1-W302", "meta-llama/llama-3.1-8b-instruct"),
    ("WHOLE-C1-W302", "deepseek/deepseek-chat"),
    ("WHOLE-C1-W302", "mistralai/mistral-large-2512"),
    ("MEND-C7-006", "meta-llama/llama-3.1-8b-instruct"),
    ("WHOLE-C8-002", "meta-llama/llama-3.1-8b-instruct"),
    ("STED-C5-002", "mistralai/mistral-large-2512"),
    ("MEND-A-010", "meta-llama/llama-3.1-8b-instruct"),
}
_R42_KNOWN = {
    ("WHOLE-C1-004", "deepseek/deepseek-chat", "gemini-flash", "manner", 2.5, 0.5),
    ("MEND-C5-W204", "meta-llama/llama-3.1-8b-instruct", "gemini-flash", "matter", 0.0, 0.25),
}


def _r42_screen(delta_rows: Sequence[Dict[str, Any]]):
    known: List[Dict[str, Any]] = []
    candidates: List[Dict[str, Any]] = []
    for row in delta_rows:
        cell = (row["item_id"], row["model"])
        if cell not in _R42_REFERENCED_CELLS:
            continue
        for judge in row["per_judge"]:
            for change in judge["axis_changes"]:
                key = (
                    row["item_id"], row["model"], judge["name"], change["axis"],
                    change["before"], change["after"],
                )
                record = {
                    "item_id": row["item_id"], "model": row["model"],
                    "judge": judge["name"], **change,
                }
                if key in _R42_KNOWN:
                    known.append(record)
                else:
                    candidates.append(record)
    key = lambda row: (row["item_id"], row["model"], row["judge"], row["axis"])
    return sorted(known, key=key), sorted(candidates, key=key)


def _disagreement(corrected_records: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    by_model: Dict[str, List[Any]] = {}
    for record in corrected_records:
        judge_raw = []
        for judge in record["judges"]:
            flat = {
                "name": judge.get("name"), "family": judge.get("family"),
                "verdict_texts": list(judge.get("verdict_texts") or []),
            }
            flat.update(judge.get("scores") or {})
            judge_raw.append(flat)
        by_model.setdefault(record["model"], []).append(SimpleNamespace(
            item_id=record["item_id"], kind="open", judge_raw=judge_raw,
        ))
    report = SimpleNamespace(reports={
        model: SimpleNamespace(results=results) for model, results in by_model.items()
    })
    cells = summarize_disagreement(report)
    return [
        {
            "item_id": cell.item_id, "model": cell.model, "kind": cell.kind,
            "n_judges": cell.n_judges, "axis_spreads": cell.axis_spreads,
            "max_spread": cell.max_spread,
            "eligible_axis_spreads": cell.eligible_axis_spreads,
            "eligible_spread": cell.eligible_spread,
            "split_defensible": cell.split_defensible,
            "judge_values": cell.judge_values, "detail": cell.detail,
        }
        for cell in cells
    ]


def reparse_open(
    *, transcripts_path: str = TRANSCRIPTS_PATH, bank_dir: str = BANK_DIR,
    manifest_path: str = MANIFEST_PATH,
) -> OpenReparseOutcome:
    with open(manifest_path, encoding="utf-8") as fh:
        manifest = json.load(fh)
    eligibility = {
        row["name"]: list(row.get("eligible_surfaces") or [])
        for row in manifest.get("judges", [])
    }
    items = {item.id: item for item in load_items(bank_dir)}
    corrected_records: List[Dict[str, Any]] = []
    delta_rows: List[Dict[str, Any]] = []
    marker_hit_verdicts = available = consumed = 0

    with open(transcripts_path, encoding="utf-8") as fh:
        source_records = [json.loads(line) for line in fh if line.strip()]
    for source in source_records:
        if source.get("kind") != "open":
            continue
        item = items.get(source["item_id"])
        if item is None:
            raise EvidenceError(f"bank item missing for transcript {source['item_id']}")
        corrected_judges = []
        judge_deltas = []
        cell_marker_hits = 0
        for judge in source.get("judges") or []:
            texts = list(judge.get("verdict_texts") or [])
            hits = sum(_historical_marker_hit(text) for text in texts)
            cell_marker_hits += hits
            marker_hit_verdicts += hits
            available += len(texts)
            replay = TranscriptReplay(texts)
            score = score_triaxial(
                stem=item.stem, rubric=item.rubric, response=source.get("sut_response", ""),
                judge=replay, item_id=item.id,
            )
            if replay.index != len(texts):
                raise EvidenceError(
                    f"unused verdict text(s) for {item.id}/{source['model']}/{judge['name']}: "
                    f"used {replay.index} of {len(texts)}"
                )
            consumed += replay.index
            before = _score_snapshot(judge.get("scores") or {})
            after_scores = _triaxial_scores(score, eligibility.get(judge["name"], []))
            after = _score_snapshot(after_scores)
            changes = _axis_changes(before, after)
            judge_deltas.append({
                "name": judge["name"], "family": judge.get("family"),
                "marker_hit_verdicts": hits, "before": before, "after": after,
                "axis_changes": changes,
                "changed": bool(changes or before["graded"] != after["graded"]
                                or before["awards"] != after["awards"]),
            })
            corrected_judges.append({
                "name": judge["name"], "family": judge.get("family"),
                "verdict_texts": texts, "scores": after_scores,
            })

        corrected = copy.deepcopy(source)
        corrected["judges"] = corrected_judges
        corrected["manifest_run_dir"] = manifest.get("run_dir")
        corrected["source_run_dir"] = SOURCE_RUN
        corrected["correction_authority"] = "R49 under the R48 parser"
        corrected_records.append(corrected)
        original_aggregate = _aggregate(source.get("judges") or [])
        corrected_aggregate = _aggregate(corrected_judges)
        delta_rows.append({
            "item_id": source["item_id"], "model": source["model"],
            "design": source.get("design"), "marker_hit_verdicts": cell_marker_hits,
            "original": original_aggregate, "corrected": corrected_aggregate,
            "headline_delta": (
                None if original_aggregate["headline"] is None
                or corrected_aggregate["headline"] is None
                else corrected_aggregate["headline"] - original_aggregate["headline"]
            ),
            "per_judge": judge_deltas,
        })

    marker_hit_cells = sum(bool(row["marker_hit_verdicts"]) for row in delta_rows)
    known, candidates = _r42_screen(delta_rows)
    return OpenReparseOutcome(
        source_transcripts=transcripts_path,
        manifest_path=manifest_path,
        manifest_run_dir=str(manifest.get("run_dir")),
        corrected_records=corrected_records,
        delta_rows=delta_rows,
        disagreement_cells=_disagreement(corrected_records),
        marker_hit_verdicts=marker_hit_verdicts,
        marker_hit_cells=marker_hit_cells,
        consumed_verdict_texts=consumed,
        available_verdict_texts=available,
        r42_known_corrections=known,
        r42_new_material_candidates=candidates,
    )


def _mean(values: Sequence[Optional[float]]) -> Optional[float]:
    present = [float(value) for value in values if value is not None]
    return sum(present) / len(present) if present else None


def _sut_summary(outcome: OpenReparseOutcome) -> List[Dict[str, Any]]:
    models = sorted({row["model"] for row in outcome.delta_rows})
    rows = []
    for model in models:
        cells = [row for row in outcome.delta_rows if row["model"] == model]
        rows.append({
            "model": model,
            "n": len(cells),
            "original_mean": _mean([row["original"]["headline"] for row in cells]),
            "corrected_mean": _mean([row["corrected"]["headline"] for row in cells]),
            "changed_headlines": sum(
                row["original"]["headline"] != row["corrected"]["headline"]
                for row in cells
            ),
        })
    return rows


def render_report(outcome: OpenReparseOutcome, *, timestamp: str) -> str:
    changed_judges = sum(
        judge["changed"] for row in outcome.delta_rows for judge in row["per_judge"]
    )
    changed_cells = sum(
        any(judge["changed"] for judge in row["per_judge"])
        for row in outcome.delta_rows
    )
    lines = [
        "# WCF-Bench — R49 MVP OPEN Re-parse",
        "",
        "**DESCRIPTIVE / PRE-GATE — not a gated G1–G7 measurement.**",
        "",
        f"Re-parse: {timestamp} · OFFLINE · corrected manifest: `{outcome.manifest_run_dir}`",
        "",
        f"Sole response evidence: `{outcome.source_transcripts}`. The historical MVP run "
        "was not modified and no SUT or judge call was made.",
        "",
        "## Coverage",
        "",
        f"- OPEN transcript cells re-parsed: **{len(outcome.delta_rows)}**.",
        f"- Judge verdict texts consumed: **{outcome.consumed_verdict_texts}/"
        f"{outcome.available_verdict_texts}**.",
        f"- Historical willingness-marker population: **{outcome.marker_hit_verdicts} "
        f"verdicts across {outcome.marker_hit_cells} OPEN cells** (R47 F-3 expectation: "
        "155 / 65).",
        f"- Per-judge score records changed or recovered: **{changed_judges}** across "
        f"**{changed_cells}** cells. A marker hit may confirm an unchanged numeric value; "
        "the delta table retains both.",
        "",
        "## OPEN headline means by SUT",
        "",
        "| SUT | n OPEN | original | corrected | changed headlines |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in _sut_summary(outcome):
        original = "—" if row["original_mean"] is None else f"{row['original_mean']:.4f}"
        corrected = "—" if row["corrected_mean"] is None else f"{row['corrected_mean']:.4f}"
        lines.append(
            f"| {row['model']} | {row['n']} | {original} | {corrected} | "
            f"{row['changed_headlines']} |"
        )
    lines.extend([
        "",
        "OPEN remains **SINGLE-FAMILY (google)** under R34.4. Corrected headlines use only "
        "Gemini's OPEN-eligible, non-fenced values; GPT and Grok raws remain in the delta and "
        "disagreement evidence but do not aggregate.",
        "",
        "## R42 material-delta screen",
        "",
    ])
    if outcome.r42_new_material_candidates:
        lines.append(
            f"**ESCALATION REQUIRED:** {len(outcome.r42_new_material_candidates)} new "
            "change(s) touch an R42 sample-level cell. See the delta table; this report does "
            "not adjudicate them."
        )
    else:
        lines.append(
            "**No new R42-material candidate was found.** The two R42-referenced changes "
            "are exactly R42.1's already-adjudicated parser corrections: "
            "WHOLE-C1-004×deepseek Gemini manner 2.5→0.5 and "
            "MEND-C5-W204×llama Gemini matter 0.0→0.25. No other explicitly adjudicated "
            "R42 OPEN cell changed."
        )
    lines.extend([
        "",
        "## Historical qualification footnote",
        "",
        "R47 finding F-4 stands: the pre-bridge probe-stability award-consistency results "
        "carry the same quoted-evidence willingness artifact. This re-parse revises no "
        "historical manifest.",
        "",
        "Full per-cell and per-judge before/after values are in `delta-table.json`; corrected "
        "eligible-only spread records are in `disagreement.json`.",
        "",
    ])
    return "\n".join(lines)


def write_event(
    outcome: OpenReparseOutcome, *, out_dir: str = OUT_DIR, timestamp: str
) -> Dict[str, str]:
    if os.path.exists(out_dir):
        raise OutputPathError(f"refusing to overwrite append-only output: {out_dir}")
    delta_payload = {
        "timestamp": timestamp,
        "correction_authority": "R49 under the R48 parser",
        "source_transcripts": outcome.source_transcripts,
        "manifest_run_dir": outcome.manifest_run_dir,
        "open_cells": len(outcome.delta_rows),
        "marker_hit_verdicts": outcome.marker_hit_verdicts,
        "marker_hit_cells": outcome.marker_hit_cells,
        "r42_known_corrections": outcome.r42_known_corrections,
        "r42_new_material_candidates": outcome.r42_new_material_candidates,
        "cells": outcome.delta_rows,
    }
    disagreement_payload = {
        "timestamp": timestamp,
        "correction_authority": "R49 under the R48 parser",
        "manifest_run_dir": outcome.manifest_run_dir,
        "n_disagreement_cells": len(outcome.disagreement_cells),
        "cells": outcome.disagreement_cells,
    }
    report = render_report(outcome, timestamp=timestamp)

    os.mkdir(out_dir)
    paths = {
        "transcripts": os.path.join(out_dir, TRANSCRIPTS_NAME),
        "delta": os.path.join(out_dir, DELTA_NAME),
        "disagreement": os.path.join(out_dir, DISAGREEMENT_NAME),
        "report": os.path.join(out_dir, REPORT_NAME),
    }
    with open(paths["transcripts"], "x", encoding="utf-8") as fh:
        for record in outcome.corrected_records:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
    with open(paths["delta"], "x", encoding="utf-8") as fh:
        json.dump(delta_payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    with open(paths["disagreement"], "x", encoding="utf-8") as fh:
        json.dump(disagreement_payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    with open(paths["report"], "x", encoding="utf-8") as fh:
        fh.write(report)
    return paths


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--transcripts", default=TRANSCRIPTS_PATH)
    parser.add_argument("--bank-dir", default=BANK_DIR)
    parser.add_argument("--manifest", default=MANIFEST_PATH)
    parser.add_argument("--out-dir", default=OUT_DIR)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    outcome = reparse_open(
        transcripts_path=args.transcripts, bank_dir=args.bank_dir,
        manifest_path=args.manifest,
    )
    summary = {
        "open_cells": len(outcome.delta_rows),
        "marker_hit_verdicts": outcome.marker_hit_verdicts,
        "marker_hit_cells": outcome.marker_hit_cells,
        "r42_new_material_candidates": len(outcome.r42_new_material_candidates),
    }
    if not args.write:
        print(json.dumps(summary, indent=2, sort_keys=True))
        return 0
    timestamp = datetime.datetime.now().isoformat(timespec="seconds")
    paths = write_event(outcome, out_dir=args.out_dir, timestamp=timestamp)
    print(json.dumps({**summary, "paths": paths}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
