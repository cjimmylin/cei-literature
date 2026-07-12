#!/usr/bin/env python
"""R47.3 offline re-parse of the immutable Task-4 qualification evidence."""

from __future__ import annotations

import argparse
import datetime
import json
import os
from dataclasses import dataclass
from typing import Any, Dict, List, Sequence, Tuple

import format_bridge_requal as task4
from wcfbench.judge_panel import JudgePanel


HARNESS_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.normpath(os.path.join(HARNESS_ROOT, ".."))
RAW_PATH = os.path.join(
    PROJECT_ROOT, "07-PILOTS", "20260711-format-bridge-requal", "raw_verdicts.jsonl"
)
RUN_DIR = "07-PILOTS/20260712-artifact-corrected-requal"
OUT_DIR = os.path.join(PROJECT_ROOT, RUN_DIR)
MANIFEST_NAME = "20260712-artifact-corrected-requal-manifest.json"
REPORT_NAME = "20260712-artifact-corrected-requal-report.md"


EXPECTED_PASS_COUNTS = {
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


class EvidenceError(RuntimeError):
    """The persisted Task-4 evidence cannot be replayed exactly."""


class DivergenceError(RuntimeError):
    """The R48 re-parse diverges from binding memo F-1/F-2."""


class OutputPathError(RuntimeError):
    """The append-only correction directory already exists."""


class ReplayClient:
    """Replay one judge's final successful response for each recorded invocation."""

    def __init__(self, rows: Sequence[Dict[str, Any]]) -> None:
        self.rows = list(rows)
        self.index = 0
        self.last_finish_reason = None
        self.last_truncated = False

    def complete(self, prompt: str, item_id: str = None) -> str:
        if self.index >= len(self.rows):
            raise EvidenceError("replay requested more calls than the raw evidence contains")
        row = self.rows[self.index]
        self.index += 1
        if item_id is not None and row.get("item_id") != item_id:
            raise EvidenceError(
                f"replay item mismatch: expected {row.get('item_id')!r}, got {item_id!r}"
            )
        if row.get("prompt") is not None and row.get("prompt") != prompt:
            raise EvidenceError(
                f"template drift while replaying {row.get('judge')} invocation "
                f"{row.get('invocation')}"
            )
        self.last_finish_reason = row.get("finish_reason")
        self.last_truncated = bool(row.get("truncated", False))
        return str(row["text"])


@dataclass
class ReparseOutcome:
    source_evidence: str
    results: task4.BatteryResults
    pass_counts: Dict[str, Dict[str, int]]
    eligible_surfaces: Dict[str, set]
    consumed: Dict[str, int]
    available: Dict[str, int]


def load_replay_streams(
    raw_path: str,
) -> Tuple[Dict[str, List[Dict[str, Any]]], Dict[str, Tuple[str, str]]]:
    """Reduce raw attempts to one final successful row per judge invocation."""
    groups: Dict[Tuple[str, int], List[Dict[str, Any]]] = {}
    metadata: Dict[str, Tuple[str, str]] = {}
    with open(raw_path, encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("kind") != "raw_call":
                continue
            judge = str(row["judge"])
            meta = (str(row["family"]), str(row["slug"]))
            if judge in metadata and metadata[judge] != meta:
                raise EvidenceError(f"inconsistent family/slug metadata for {judge}")
            metadata[judge] = meta
            key = (judge, int(row["invocation"]))
            groups.setdefault(key, []).append(row)

    streams: Dict[str, List[Dict[str, Any]]] = {judge: [] for judge in metadata}
    for (judge, invocation), attempts in sorted(groups.items()):
        successes = [row for row in attempts if not row.get("error") and row.get("text") is not None]
        if not successes:
            raise EvidenceError(f"invocation {judge}/{invocation} has no successful response")
        final = max(successes, key=lambda row: int(row.get("attempt", 0)))
        streams[judge].append(final)
    return streams, metadata


def _ordered_qualifications(results: task4.BatteryResults):
    quals = [results.incumbents[name] for name, _family, _slug in task4.INCUMBENT_JUDGES]
    quals.extend(
        results.candidates[name] for name, _family, _aliases in task4.CANDIDATE_ALIASES
    )
    return quals


def reparse_task4(raw_path: str = RAW_PATH) -> ReparseOutcome:
    streams, metadata = load_replay_streams(raw_path)
    required = {name for name, _family, _slug in task4.INCUMBENT_JUDGES}
    required.update(name for name, _family, _aliases in task4.CANDIDATE_ALIASES)
    if set(streams) != required:
        raise EvidenceError(
            f"Task-4 judge set mismatch: expected {sorted(required)}, got {sorted(streams)}"
        )

    clients: Dict[str, ReplayClient] = {}

    def client_factory(name: str, family: str, slug: str) -> ReplayClient:
        if metadata[name] != (family, slug):
            raise EvidenceError(
                f"Task-4 metadata mismatch for {name}: raw={metadata[name]!r}, "
                f"runner={(family, slug)!r}"
            )
        client = ReplayClient(streams[name])
        clients[name] = client
        return client

    candidates = tuple(
        (name, metadata[name][0], metadata[name][1])
        for name, _family, _aliases in task4.CANDIDATE_ALIASES
    )
    results = task4.run_batteries(candidates, client_factory=client_factory)
    qualifications = _ordered_qualifications(results)
    pass_counts = {
        q.name: {probe: reps.n_pass for probe, reps in q.probe_reps.items()}
        for q in qualifications
    }
    if pass_counts != EXPECTED_PASS_COUNTS:
        raise DivergenceError(
            "R47.3 re-parse diverged from memo F-1/F-2: "
            f"expected={EXPECTED_PASS_COUNTS!r}, actual={pass_counts!r}"
        )

    consumed = {name: client.index for name, client in clients.items()}
    available = {name: len(rows) for name, rows in streams.items()}
    if consumed != available:
        raise EvidenceError(
            f"not every successful Task-4 invocation was consumed: "
            f"consumed={consumed!r}, available={available!r}"
        )
    return ReparseOutcome(
        source_evidence=raw_path,
        results=results,
        pass_counts=pass_counts,
        eligible_surfaces={q.name: set(q.surfaces) for q in qualifications},
        consumed=consumed,
        available=available,
    )


def build_corrected_manifest(
    outcome: ReparseOutcome, *, timestamp: str, run_dir: str = RUN_DIR
) -> Dict[str, Any]:
    manifest = task4.build_task4_manifest(
        outcome.results, timestamp=timestamp, run_dir=run_dir
    )
    manifest["memo"] = "R47.3 artifact-corrected manifest event under the R48 parser"
    manifest["source"] = "offline R48 re-parse of immutable Task-4 raw evidence"
    manifest["source_evidence"] = outcome.source_evidence
    manifest["correction_authority"] = "R47.3"
    manifest["supersedes_manifest_of_record"] = (
        "07-PILOTS/20260711-format-bridge-requal/"
        "20260711-format-bridge-requal-manifest.json"
    )
    manifest["open_label"] = "SINGLE-FAMILY (google) — R34.4"
    return manifest


def _result_word(n_pass: int) -> str:
    return "PASS" if n_pass >= task4.THRESHOLD else "FAIL"


def render_report(outcome: ReparseOutcome, *, timestamp: str) -> str:
    lines = [
        "# WCF-Bench — R47.3 Artifact-Corrected Requalification",
        "",
        f"Re-parse: {timestamp} · K={task4.K}, gate >= {task4.THRESHOLD}/{task4.K} · OFFLINE",
        "",
        "This is the **corrected manifest event under R47.3** and it **supersedes the "
        "as-executed Task-4 manifest as manifest of record**. The Task-4 directory remains "
        "an unchanged historical record.",
        "",
        f"Sole evidence source: `{outcome.source_evidence}`. No live calls were made.",
        "",
        "## Corrected K=8 pass/fail table",
        "",
        "| judge | family | probe | n_pass/K | result |",
        "|---|---|---|---:|---|",
    ]
    family_by_name = {
        q.name: q.family for q in _ordered_qualifications(outcome.results)
    }
    for judge, counts in outcome.pass_counts.items():
        for probe, n_pass in counts.items():
            lines.append(
                f"| {judge} | {family_by_name[judge]} | {probe} | "
                f"{n_pass}/{task4.K} | {_result_word(n_pass)} |"
            )
    lines.extend([
        "",
        "## Corrected eligibility",
        "",
        "| judge | eligible surfaces |",
        "|---|---|",
    ])
    for judge, surfaces in outcome.eligible_surfaces.items():
        lines.append(f"| {judge} | {', '.join(sorted(surfaces)) or 'none'} |")
    lines.extend([
        "",
        "## OPEN outcome",
        "",
        "**SINGLE-FAMILY (google)** under R34.4: Gemini Flash is OPEN-eligible; Grok, "
        "Cohere, and Nova are not. The candidate ladder remains CLOSED. No candidate was "
        "rerun or added.",
        "",
        "Both incumbent award-consistency rows correct from 0/8 to 8/8. Grok's "
        "discrimination row remains a substantive 0/8; Cohere and Nova remain ineligible.",
        "",
    ])
    return "\n".join(lines)


class _NoCallClient:
    def complete(self, *_args, **_kwargs):
        raise AssertionError("manifest validation must not make calls")


def _validate_manifest(manifest: Dict[str, Any]) -> None:
    clients = [
        {"name": row["name"], "family": row["family"], "slug": row["slug"],
         "client": _NoCallClient()}
        for row in manifest["judges"]
    ]
    JudgePanel(clients, manifest=manifest)


def write_event(
    outcome: ReparseOutcome, *, out_dir: str = OUT_DIR, timestamp: str
) -> Dict[str, str]:
    if os.path.exists(out_dir):
        raise OutputPathError(f"refusing to overwrite append-only event directory: {out_dir}")
    run_dir = os.path.relpath(out_dir, PROJECT_ROOT)
    manifest = build_corrected_manifest(outcome, timestamp=timestamp, run_dir=run_dir)
    _validate_manifest(manifest)
    report = render_report(outcome, timestamp=timestamp)

    os.mkdir(out_dir)
    manifest_path = os.path.join(out_dir, MANIFEST_NAME)
    report_path = os.path.join(out_dir, REPORT_NAME)
    with open(manifest_path, "x", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2, sort_keys=True)
        fh.write("\n")
    with open(report_path, "x", encoding="utf-8") as fh:
        fh.write(report)
    return {"manifest": manifest_path, "report": report_path}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw", default=RAW_PATH)
    parser.add_argument("--out-dir", default=OUT_DIR)
    parser.add_argument("--write", action="store_true", help="create the dated event")
    args = parser.parse_args()

    outcome = reparse_task4(args.raw)
    if not args.write:
        print(json.dumps(outcome.pass_counts, indent=2, sort_keys=True))
        return 0
    timestamp = datetime.datetime.now().isoformat(timespec="seconds")
    paths = write_event(outcome, out_dir=args.out_dir, timestamp=timestamp)
    print(json.dumps(paths, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
