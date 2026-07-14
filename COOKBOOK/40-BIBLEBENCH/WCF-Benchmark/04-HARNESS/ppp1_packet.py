#!/usr/bin/env python3
"""Build the offline, non-quotable PPP-1 exploratory manuscript packet."""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import math
import random
import statistics
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

from wcfbench import load_items, scorer_kind


HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent
VALIDITY_LABEL = "EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE"
SUT_ORDER = (
    "meta-llama/llama-3.1-8b-instruct",
    "deepseek/deepseek-chat",
    "qwen/qwen3.7-plus",
)
JUDGE = "google/gemini-2.5-flash"
DESIGN_ORDER = (
    "dutybound", "complicit", "aggravate", "steadfast", "crosswind",
    "liberty", "prooftext", "mending", "wholeheart", "narrowgate",
)
MANUSCRIPT_SOURCE_NAMES = (
    "02-introduction.md", "03-related-work.md", "04-benchmark-design.md",
    "05-methods-validity.md",
)
PACKET_FILE_NAMES = (
    "00-README.md", "01-source-manifest.json", "02-normalized-cells.csv",
    "03-traceability.csv", "04-traceability.md", "05-preview-results.md",
    "06-preview-discussion.md", "07-preview-limitations.md",
    "08-assembled-manuscript-preview.md",
    "tables/01-per-design-per-sut.csv", "tables/01-per-design-per-sut.md",
    "tables/02-per-sut-aggregate.csv", "tables/02-per-sut-aggregate.md",
    "tables/03-overall-aggregate.csv", "tables/03-overall-aggregate.md",
    "figures/01-design-by-sut.svg", "figures/02-per-sut-aggregate.svg",
)
EXPECTED_CELLS = 678
EXPECTED_ITEMS = 226
EXPECTED_HEADLINE_PER_SUT = 222


class PacketError(RuntimeError):
    """The immutable run cannot support a valid PPP-1 packet."""


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _display_path(path: Path) -> str:
    return str(path.relative_to(PROJECT)) if path.is_relative_to(PROJECT) else str(path)


def _source_entry(kind: str, path: Path, selected_version: str) -> Dict[str, Any]:
    return {
        "artifact_kind": kind, "path": _display_path(path),
        "sha256": _sha256(path), "bytes": path.stat().st_size,
        "selected_version": selected_version,
    }


def _bank_source_entry(bank_dir: Path, bank_items: Sequence[Any]) -> Dict[str, Any]:
    paths = sorted((*bank_dir.glob("*.yaml"), *bank_dir.glob("*.yml")))
    if not paths:
        raise PacketError("frozen bank source has no YAML files")
    digest = hashlib.sha256()
    total_bytes = 0
    for path in paths:
        data = path.read_bytes()
        digest.update(path.name.encode("utf-8") + b"\0" + data)
        total_bytes += len(data)
    return {
        "artifact_kind": "frozen_bank",
        "path": f"{_display_path(bank_dir)}/*.yaml|*.yml",
        "sha256": digest.hexdigest(), "bytes": total_bytes,
        "selected_version": (f"sorted aggregate of {len(paths)} frozen YAML files; "
                             f"{len(bank_items)} loaded / {EXPECTED_ITEMS} runnable"),
    }


def _read_json(path: Path) -> Dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise PacketError(f"unreadable JSON artifact: {path}") from exc
    if not isinstance(value, dict):
        raise PacketError(f"JSON artifact is not an object: {path}")
    return value


def _identity_contract(identity: Dict[str, Any]) -> bool:
    return (
        identity.get("validity_label") == VALIDITY_LABEL
        and identity.get("artifact_kind") == VALIDITY_LABEL
        and identity.get("expected_cells") == EXPECTED_CELLS
        and identity.get("runnable_items") == EXPECTED_ITEMS
        and identity.get("suts") == list(SUT_ORDER)
        and identity.get("judge") == JUDGE
        and identity.get("sut_max_tokens") == 2048
        and identity.get("judge_max_tokens") == 512
        and math.isclose(float(identity.get("budget_usd", -1)), 23.56)
        and len(identity.get("cell_keys") or []) == EXPECTED_CELLS
        and len(set(identity.get("cell_keys") or [])) == EXPECTED_CELLS
    )


def _load_final_run(run_dir: Path) -> Tuple[Dict[str, Any], Dict[str, Any], List[Dict[str, Any]]]:
    metadata_path = run_dir / "run-metadata.json"
    identity_path = run_dir / "ppp1-run-identity.json"
    checkpoint_path = run_dir / "checkpoint.jsonl"
    if not metadata_path.is_file():
        raise PacketError("final run-metadata.json does not exist")
    required = (identity_path, checkpoint_path, run_dir / "raw-evidence.jsonl",
                run_dir / "ppp1-report.md")
    if not all(path.is_file() for path in required):
        raise PacketError("final PPP-1 identity/checkpoint/raw/report artifacts are incomplete")
    metadata = _read_json(metadata_path)
    identity = _read_json(identity_path)
    if not _identity_contract(identity):
        raise PacketError("PPP-1 identity does not match the frozen packet contract")
    if metadata.get("validity_label") != VALIDITY_LABEL:
        raise PacketError("run metadata validity label is wrong")
    if metadata.get("run_status") not in {"COMPLETE", "PARTIAL"}:
        raise PacketError("run metadata is not final")
    if metadata.get("expected_cells") != EXPECTED_CELLS:
        raise PacketError("run metadata expected-cell count is wrong")
    if metadata.get("identity") != identity:
        raise PacketError("run metadata identity does not match the immutable identity")

    records: List[Dict[str, Any]] = []
    seen = set()
    try:
        for line_number, line in enumerate(checkpoint_path.open(encoding="utf-8"), 1):
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise PacketError(f"checkpoint line {line_number} is malformed") from exc
            if not isinstance(record, dict):
                raise PacketError(f"checkpoint line {line_number} is not an object")
            key = record.get("cell_key")
            if key in seen or key not in identity["cell_keys"]:
                raise PacketError("checkpoint has duplicate or foreign cells")
            if record.get("status") not in {"scored", "error"}:
                raise PacketError("checkpoint has a nonterminal cell")
            seen.add(key)
            records.append(record)
    except OSError as exc:
        raise PacketError("checkpoint is unreadable") from exc
    if metadata.get("recorded_cells") != len(records):
        raise PacketError("checkpoint count does not match final metadata")
    scored = sum(row.get("status") == "scored" for row in records)
    errors = sum(row.get("status") == "error" for row in records)
    if metadata.get("scored_cells") != scored or metadata.get("error_cells") != errors:
        raise PacketError("checkpoint statuses do not match final metadata")
    if metadata["run_status"] == "COMPLETE" and seen != set(identity["cell_keys"]):
        raise PacketError("COMPLETE checkpoint is missing cells")
    return metadata, identity, records


def _text_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _call_cost(call: Dict[str, Any]) -> float:
    usage = call.get("usage") if isinstance(call.get("usage"), dict) else {}
    for field in ("cost", "fallback_cost_usd"):
        value = _number(usage.get(field))
        if value is not None:
            return value
    raise PacketError("call custody lacks actual-first cost")


def _checkpoint_judge_hashes(record: Dict[str, Any]) -> List[str]:
    texts = []
    for row in record.get("judge_raw") or []:
        texts.extend(text for text in row.get("verdict_texts") or []
                     if isinstance(text, str))
    for row in (record.get("judge") or {}).get("per_judge") or []:
        text = row.get("verdict_text")
        if isinstance(text, str):
            texts.append(text)
    return [_text_hash(text) for text in texts]


def _raw_custody(run_dir: Path, records: Sequence[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    path = run_dir / "raw-evidence.jsonl"
    try:
        raw_bytes = path.read_bytes().splitlines(keepends=True)
    except OSError as exc:
        raise PacketError("raw-evidence ledger is unreadable") from exc
    raw_rows = []
    for line_number, raw_line in enumerate(raw_bytes, 1):
        try:
            row = json.loads(raw_line)
        except json.JSONDecodeError as exc:
            raise PacketError(f"raw-evidence line {line_number} is malformed") from exc
        if not isinstance(row, dict) or row.get("kind") != "raw_emission":
            raise PacketError(f"raw-evidence line {line_number} is not an emission")
        raw_rows.append(row)

    custody = {}
    cursor = 0
    for record in records:
        calls = (record.get("usage") or {}).get("calls") or []
        if not isinstance(calls, list):
            raise PacketError("checkpoint call custody is malformed")
        span_rows = raw_rows[cursor:cursor + len(calls)]
        span_bytes = raw_bytes[cursor:cursor + len(calls)]
        if len(span_rows) != len(calls):
            raise PacketError("raw-evidence ledger ends before checkpoint custody")
        for call, raw in zip(calls, span_rows):
            if (raw.get("item_id") != record.get("item_id")
                    or raw.get("role") != call.get("role")
                    or raw.get("slug") != call.get("model")):
                raise PacketError("raw/checkpoint call sequence does not reconcile")
        checkpoint_cost = sum(_call_cost(call) for call in calls)
        raw_cost = 0.0
        for raw in span_rows:
            entries = raw.get("usage") or []
            source = entries[0] if len(entries) == 1 else raw.get("fallback_accounting")
            if not isinstance(source, dict):
                raise PacketError("raw call custody lacks one accounting source")
            raw_cost += _call_cost({"usage": source.get("usage", source)})
        if not math.isclose(checkpoint_cost, raw_cost, rel_tol=1e-12, abs_tol=1e-12):
            raise PacketError("raw/checkpoint cell costs do not reconcile")
        checkpoint_hashes = _checkpoint_judge_hashes(record)
        raw_judge_hashes = [_text_hash(row["text"]) for row in span_rows
                            if row.get("role") == "judge" and isinstance(row.get("text"), str)]
        if checkpoint_hashes and Counter(checkpoint_hashes) != Counter(raw_judge_hashes):
            raise PacketError("raw/checkpoint judge text hashes do not reconcile")
        hash_status: Any = (
            True if checkpoint_hashes
            else "not_applicable_checkpoint_has_no_judge_text"
            if raw_judge_hashes else True
        )
        start = cursor + 1 if calls else ""
        end = cursor + len(calls) if calls else ""
        custody[record["cell_key"]] = {
            "source_run": _display_path(run_dir),
            "checkpoint_file": _display_path(run_dir / "checkpoint.jsonl"),
            "raw_evidence_file": _display_path(path),
            "raw_line_start": start, "raw_line_end": end,
            "raw_line_count": len(calls),
            "raw_span_sha256": hashlib.sha256(b"".join(span_bytes)).hexdigest(),
            "raw_call_hashes": ";".join(hashlib.sha256(line).hexdigest()
                                           for line in span_bytes),
            "call_count": len(calls), "cell_cost_usd": checkpoint_cost,
            "judge_text_sha256s": ";".join(raw_judge_hashes),
            "checkpoint_judge_text_sha256s": ";".join(checkpoint_hashes),
            "judge_hashes_match": hash_status,
        }
        cursor += len(calls)
    if cursor != len(raw_rows):
        raise PacketError("raw-evidence ledger has unassigned calls")
    return custody


def _number(value: Any) -> Optional[float]:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        number = float(value)
        return number if math.isfinite(number) else None
    return None


def _kind_and_values(record: Dict[str, Any], bank_kind: str) -> Dict[str, Any]:
    scores = record.get("scores") if isinstance(record.get("scores"), dict) else {}
    judge = record.get("judge") if isinstance(record.get("judge"), dict) else {}
    kind = str(scores.get("kind") or ("episode" if judge else bank_kind))
    value = None
    path = ""
    if record.get("status") == "scored":
        if kind in {"ordinal", "anchor", "open"}:
            value = _number(scores.get("fraction"))
            path = "scores.fraction" if value is not None else ""
        elif kind == "episode":
            value = _number(judge.get("score"))
            path = "judge.score" if value is not None else ""
    contested = scores.get("contested") if isinstance(scores.get("contested"), dict) else {}
    triaxial = scores.get("triaxial") if isinstance(scores.get("triaxial"), dict) else {}
    return {
        "kind": kind,
        "headline_score": value,
        "score_path": path,
        "disclosure": _number(contested.get("disclosure")),
        "coherence": _number(contested.get("coherence")),
        "settled_core_fraction": _number(contested.get("settled_core_fraction")),
        "matter": _number(triaxial.get("matter")),
        "manner": _number(triaxial.get("manner")),
        "end": _number(triaxial.get("end")),
    }


def _normalized_rows(identity: Dict[str, Any], records: Sequence[Dict[str, Any]],
                     bank_items: Sequence[Any],
                     custody: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    by_id = {item.id: item for item in bank_items if not item.extra.get("dev_set_only")}
    if len(by_id) != EXPECTED_ITEMS:
        raise PacketError("bank mapping does not contain the exact 226 runnable items")
    by_key = {record["cell_key"]: (line, record)
              for line, record in enumerate(records, 1)}
    rows = []
    for key in identity["cell_keys"]:
        item_id, separator, sut = key.partition("::")
        if not separator or sut not in SUT_ORDER or item_id not in by_id:
            raise PacketError("identity cell cannot be mapped to the frozen bank/roster")
        item = by_id[item_id]
        line_record = by_key.get(key)
        if line_record is None:
            rows.append({
                "validity_label": VALIDITY_LABEL, "source_file": "checkpoint.jsonl",
                "source_line": "", "cell_key": key, "item_id": item_id, "sut": sut,
                "source_run": "", "checkpoint_file": "checkpoint.jsonl",
                "checkpoint_line": "", "raw_evidence_file": "raw-evidence.jsonl",
                "design": item.design, "kind": scorer_kind(item), "status": "unrecorded",
                "score_path": "", "headline_score": None, "disclosure": None,
                "coherence": None, "settled_core_fraction": None, "error": "",
                "matter": None, "manner": None, "end": None,
                "raw_line_start": "", "raw_line_end": "", "raw_line_count": 0,
                "raw_span_sha256": "", "raw_call_hashes": "", "call_count": 0,
                "cell_cost_usd": 0.0, "judge_text_sha256s": "",
                "checkpoint_judge_text_sha256s": "",
                "judge_hashes_match": True,
            })
            continue
        line, record = line_record
        if record.get("item_id") != item_id or record.get("sut") != sut:
            raise PacketError("checkpoint identity fields do not match cell key")
        values = _kind_and_values(record, scorer_kind(item))
        rows.append({
            "validity_label": VALIDITY_LABEL, "source_file": "checkpoint.jsonl",
            "source_line": line, "cell_key": key, "item_id": item_id, "sut": sut,
            "checkpoint_line": line,
            "design": item.design, "kind": values["kind"], "status": record["status"],
            "score_path": values["score_path"],
            "headline_score": values["headline_score"],
            "disclosure": values["disclosure"], "coherence": values["coherence"],
            "settled_core_fraction": values["settled_core_fraction"],
            "matter": values["matter"], "manner": values["manner"], "end": values["end"],
            "error": str(record.get("error") or ""),
            **custody[key],
        })
    return rows


def _bootstrap_ci(rows: Sequence[Dict[str, Any]], seed_text: str,
                  mode: str) -> Tuple[Optional[float], Optional[float]]:
    values = [row["headline_score"] for row in rows if row["headline_score"] is not None]
    if not values:
        return None, None
    if len(values) == 1:
        return values[0], values[0]
    seed = int(hashlib.sha256(seed_text.encode("utf-8")).hexdigest()[:16], 16)
    rng = random.Random(seed)
    if mode == "design_stratified":
        groups: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
        for row in rows:
            groups[row["design"]].append(row)
        strata = list(groups.values())
    elif mode == "item_cluster":
        groups = defaultdict(list)
        for row in rows:
            groups[row["item_id"]].append(row)
        strata = [list(groups.values())]
    else:
        strata = [[row] for row in rows]
    means = []
    for _ in range(1000):
        sample = []
        if mode == "design_stratified":
            for stratum in strata:
                for _index in range(len(stratum)):
                    value = stratum[rng.randrange(len(stratum))]["headline_score"]
                    if value is not None:
                        sample.append(value)
        elif mode == "item_cluster":
            units = strata[0]
            for _index in range(len(units)):
                sample.extend(row["headline_score"] for row in units[rng.randrange(len(units))]
                              if row["headline_score"] is not None)
        else:
            units = strata
            for _index in range(len(units)):
                value = units[rng.randrange(len(units))][0]["headline_score"]
                if value is not None:
                    sample.append(value)
        if sample:
            means.append(sum(sample) / len(sample))
    means.sort()
    return means[24], means[974]


def _summary(rows: Sequence[Dict[str, Any]], key: str, value: str,
             bootstrap_mode: str) -> Dict[str, Any]:
    numeric = [row["headline_score"] for row in rows if row["headline_score"] is not None]
    contested = [row for row in rows if row["kind"] == "contested"]
    headline_expected = len(rows) - len(contested)
    low, high = _bootstrap_ci(rows, f"{key}:{value}", bootstrap_mode)
    ci_method = {
        "item": "item bootstrap within design; 1000 deterministic resamples",
        "design_stratified": "design-stratified item bootstrap; 1000 deterministic resamples",
        "item_cluster": "item-cluster bootstrap across all SUT observations; 1000 deterministic resamples",
    }[bootstrap_mode]
    return {
        key: value,
        "expected_n": len(rows),
        "headline_expected_n": headline_expected,
        "recorded_n": sum(row["status"] != "unrecorded" for row in rows),
        "status_scored_n": sum(row["status"] == "scored" for row in rows),
        "numeric_n": len(numeric),
        "error_n": sum(row["status"] == "error" for row in rows),
        "ungraded_n": sum(row["status"] == "scored" and row["kind"] != "contested"
                          and row["headline_score"] is None for row in rows),
        "unrecorded_n": sum(row["status"] == "unrecorded" for row in rows),
        "contested_n": len(contested),
        "mechanical_numeric_n": sum(row["headline_score"] is not None
                                    and row["kind"] in {"ordinal", "anchor"} for row in rows),
        "judge_numeric_n": sum(row["headline_score"] is not None
                               and row["kind"] in {"open", "episode"} for row in rows),
        "coverage": (len(numeric) / headline_expected if headline_expected else None),
        "mean": (sum(numeric) / len(numeric) if numeric else None),
        "sd": (statistics.stdev(numeric) if len(numeric) > 1 else 0.0 if numeric else None),
        "ci95_low": low, "ci95_high": high,
        "ci_method": ci_method,
        **{
            f"open_{axis}_n": sum(row[axis] is not None for row in rows if row["kind"] == "open")
            for axis in ("matter", "manner", "end")
        },
        **{
            f"open_{axis}_mean": (
                sum(row[axis] for row in rows if row["kind"] == "open" and row[axis] is not None)
                / sum(row[axis] is not None for row in rows if row["kind"] == "open")
                if any(row["kind"] == "open" and row[axis] is not None for row in rows)
                else None)
            for axis in ("matter", "manner", "end")
        },
        "source_cells": ";".join(row["cell_key"] for row in rows),
    }


def _summaries(rows: Sequence[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]],
                                                       List[Dict[str, Any]],
                                                       List[Dict[str, Any]]]:
    grouped: Dict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)
    by_sut: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[(row["design"], row["sut"])].append(row)
        by_sut[row["sut"]].append(row)
    per_design = []
    for design in DESIGN_ORDER:
        for sut in SUT_ORDER:
            summary = _summary(grouped[(design, sut)], "design", design, "item")
            summary = {"design": design, "sut": sut,
                       **{k: v for k, v in summary.items() if k != "design"}}
            per_design.append(summary)
    per_sut = [_summary(by_sut[sut], "sut", sut, "design_stratified")
               for sut in SUT_ORDER]
    overall = [_summary(rows, "scope", "all-three-suts", "item_cluster")]
    return per_design, per_sut, overall


SUMMARY_FIELDS = (
    "expected_n", "headline_expected_n", "recorded_n", "status_scored_n",
    "numeric_n", "error_n", "ungraded_n", "unrecorded_n", "contested_n",
    "mechanical_numeric_n", "judge_numeric_n", "coverage", "mean", "sd",
    "ci95_low", "ci95_high", "ci_method",
    "open_matter_n", "open_matter_mean", "open_manner_n", "open_manner_mean",
    "open_end_n", "open_end_mean",
)


def _display(value: Any) -> str:
    if value is None or value == "":
        return "—"
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def _write_csv(path: Path, rows: Sequence[Dict[str, Any]], fields: Sequence[str]) -> None:
    with path.open("x", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _markdown_table(title: str, rows: Sequence[Dict[str, Any]], fields: Sequence[str]) -> str:
    lines = [f"# {title}", "", f"> **{VALIDITY_LABEL}**", "",
             "Errors and ungraded cells are missing values, never zero-imputed.", "",
             "| " + " | ".join(fields) + " |",
             "|" + "|".join("---" for _ in fields) + "|"]
    for row in rows:
        lines.append("| " + " | ".join(_display(row.get(field)) for field in fields) + " |")
    return "\n".join(lines) + "\n"


def _trace_rows(per_design: Sequence[Dict[str, Any]], per_sut: Sequence[Dict[str, Any]],
                overall: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    traces = []
    groups = [
        ("tables/01-per-design-per-sut", per_design, ("design", "sut")),
        ("tables/02-per-sut-aggregate", per_sut, ("sut",)),
        ("tables/03-overall-aggregate", overall, ("scope",)),
    ]
    for artifact, summaries, keys in groups:
        for row in summaries:
            row_key = " × ".join(str(row[key]) for key in keys)
            for field in SUMMARY_FIELDS:
                traces.append({
                    "validity_label": VALIDITY_LABEL, "artifact": artifact,
                    "row_key": row_key, "displayed_field": field,
                    "displayed_value": row[field],
                    "value_reference": f"{artifact}#{row_key}:{field}",
                    "formula": (row["ci_method"] if field in {"ci95_low", "ci95_high"}
                                else "direct count over expected identity cells"
                                if field.endswith("_n")
                                else "numeric checkpoint values only; no imputation"),
                    "source_file": "checkpoint.jsonl",
                    "source_fields": ("status;scores.fraction;scores.triaxial.*;judge.score;"
                                      "scores.contested.*"),
                    "source_cells": row["source_cells"],
                })
    for row in per_sut:
        for artifact in ("figures/02-per-sut-aggregate.svg", "05-preview-results.md",
                         "08-assembled-manuscript-preview.md"):
            for field in ("mean", "ci95_low", "ci95_high", "numeric_n",
                          "headline_expected_n", "error_n"):
                traces.append({
                    "validity_label": VALIDITY_LABEL, "artifact": artifact,
                    "row_key": row["sut"], "displayed_field": field,
                    "displayed_value": row[field],
                    "value_reference": f"{artifact}#{row['sut']}:{field}",
                    "formula": (row["ci_method"] if field in {"ci95_low", "ci95_high"}
                                else "numeric checkpoint values only; no imputation"),
                    "source_file": "checkpoint.jsonl",
                    "source_fields": "status;scores.fraction;judge.score",
                    "source_cells": row["source_cells"],
                })
    for row in per_design:
        traces.append({
            "validity_label": VALIDITY_LABEL,
            "artifact": "figures/01-design-by-sut.svg",
            "row_key": f"{row['design']} × {row['sut']}",
            "displayed_field": "mean",
            "displayed_value": row["mean"],
            "value_reference": (f"figures/01-design-by-sut.svg#"
                                f"{row['design']}×{row['sut']}:mean"),
            "formula": "numeric checkpoint values only; no imputation",
            "source_file": "checkpoint.jsonl",
            "source_fields": "status;scores.fraction;judge.score",
            "source_cells": row["source_cells"],
        })
    root = overall[0]
    for artifact in ("05-preview-results.md", "08-assembled-manuscript-preview.md"):
        for field in ("expected_n", "recorded_n", "headline_expected_n", "numeric_n",
                      "error_n", "contested_n"):
            traces.append({
                "validity_label": VALIDITY_LABEL, "artifact": artifact,
                "row_key": root["scope"], "displayed_field": field,
                "displayed_value": root[field],
                "value_reference": f"{artifact}#{root['scope']}:{field}",
                "formula": "direct count over expected identity cells",
                "source_file": "checkpoint.jsonl",
                "source_fields": "status;scores.kind",
                "source_cells": root["source_cells"],
            })
    headline_missing = root["headline_expected_n"] - root["numeric_n"]
    for artifact in ("05-preview-results.md", "08-assembled-manuscript-preview.md"):
        traces.append({
            "validity_label": VALIDITY_LABEL, "artifact": artifact,
            "row_key": root["scope"], "displayed_field": "headline_missing_n",
            "displayed_value": headline_missing,
            "value_reference": f"{artifact}#{root['scope']}:headline_missing_n",
            "formula": "headline_expected_n - numeric_n",
            "source_file": "checkpoint.jsonl",
            "source_fields": "status;scores.kind;scores.fraction;judge.score",
            "source_cells": root["source_cells"],
        })
    errorful_cells = ";".join(
        row["source_cells"] for row in per_design if row["error_n"] > 0)
    errorful = sum(row["error_n"] > 0 for row in per_design)
    for artifact in ("06-preview-discussion.md", "08-assembled-manuscript-preview.md"):
        traces.append({
            "validity_label": VALIDITY_LABEL, "artifact": artifact,
            "row_key": "design-by-SUT rows", "displayed_field": "errorful_row_count",
            "displayed_value": errorful,
            "value_reference": f"{artifact}#design-by-SUT:errorful_row_count",
            "formula": "count of 30 design-by-SUT rows with error_n > 0",
            "source_file": "checkpoint.jsonl", "source_fields": "status",
            "source_cells": errorful_cells,
        })
        traces.append({
            "validity_label": VALIDITY_LABEL, "artifact": artifact,
            "row_key": "design-by-SUT rows", "displayed_field": "design_sut_row_count",
            "displayed_value": len(per_design),
            "value_reference": f"{artifact}#design-by-SUT:design_sut_row_count",
            "formula": "10 frozen designs × 3 frozen SUTs",
            "source_file": "ppp1-run-identity.json;05-BANK-YAML/*.yaml",
            "source_fields": "suts;design", "source_cells": root["source_cells"],
        })
    return traces


def _svg(title: str, labels: Sequence[str], series: Sequence[Tuple[str, Sequence[Optional[float]]]]) -> str:
    width, height = 1100, 520
    left, top, plot_w, plot_h = 110, 115, 920, 315
    colors = ("#2563eb", "#dc2626", "#059669")
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="{width/2}" y="32" text-anchor="middle" font-family="sans-serif" '
        f'font-size="20" font-weight="bold">{html.escape(title)}</text>',
        f'<text x="{width/2}" y="60" text-anchor="middle" font-family="sans-serif" '
        f'font-size="13" fill="#991b1b">{html.escape(VALIDITY_LABEL)}</text>',
    ]
    for tick in range(6):
        value = tick / 5
        y = top + plot_h * (1 - value)
        parts.extend([
            f'<line x1="{left}" y1="{y:.1f}" x2="{left+plot_w}" y2="{y:.1f}" '
            'stroke="#e5e7eb"/>',
            f'<text x="{left-12}" y="{y+4:.1f}" text-anchor="end" '
            f'font-family="sans-serif" font-size="11">{value:.1f}</text>',
        ])
    group_w = plot_w / max(1, len(labels))
    for index, label in enumerate(labels):
        x = left + group_w * (index + 0.5)
        parts.append(f'<text x="{x:.1f}" y="{top+plot_h+28}" text-anchor="middle" '
                     f'font-family="sans-serif" font-size="10">{html.escape(label)}</text>')
        for series_index, (_name, values) in enumerate(series):
            value = values[index]
            if value is None:
                continue
            px = x + (series_index - (len(series) - 1) / 2) * 11
            py = top + plot_h * (1 - value)
            parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" '
                         f'fill="{colors[series_index % len(colors)]}"/>')
    legend_x = left
    for index, (name, _values) in enumerate(series):
        x = legend_x + index * 310
        parts.extend([
            f'<circle cx="{x}" cy="92" r="5" fill="{colors[index % len(colors)]}"/>',
            f'<text x="{x+10}" y="96" font-family="sans-serif" font-size="11">'
            f'{html.escape(name)}</text>',
        ])
    parts.append('<text x="110" y="500" font-family="sans-serif" font-size="11" '
                 'fill="#4b5563">Means use numeric headline values only; errors are not imputed.</text>')
    parts.append("</svg>\n")
    return "\n".join(parts)


def _results(per_sut: Sequence[Dict[str, Any]], overall: Dict[str, Any]) -> str:
    lines = [
        "# PPP-1 Preview Results", "", f"> **{VALIDITY_LABEL}**", "",
        "PPP-1 recorded " + f"{overall['recorded_n']} of {overall['expected_n']} expected cells. "
        + f"Across all cells, {overall['error_n']} were error-recorded. Of "
        + f"{overall['headline_expected_n']} headline-eligible cells, "
        + f"{overall['numeric_n']} yielded numeric values and "
        + f"{overall['headline_expected_n'] - overall['numeric_n']} lacked a numeric headline; "
        f"errors were not imputed as zero. The {overall['contested_n']} "
        "contested cells are "
        "reported on their separate disclosure, coherence, and settled-core fields and are "
        f"excluded from the headline mean.", "", "Observed summaries in the frozen roster order:", "",
    ]
    for row in per_sut:
        lines.append(
            f"- `{row['sut']}`: mean {_display(row['mean'])}, 95% design-stratified "
            "item-bootstrap interval "
            f"[{_display(row['ci95_low'])}, {_display(row['ci95_high'])}], numeric "
            f"n={row['numeric_n']}/{row['headline_expected_n']}, errors={row['error_n']}.")
    lines.extend([
        "", "These are descriptive preview values under one Gemini judge where judging was "
        "required. They do not support model rankings, judge-family robustness, gate decisions, "
        "or release claims. Per-design values and their missingness denominators are in the "
        "linked tables; figures preserve the frozen roster and design order.", "",
    ])
    return "\n".join(lines)


def _discussion(per_design: Sequence[Dict[str, Any]]) -> str:
    errorful = sum(row["error_n"] > 0 for row in per_design)
    return "\n".join([
        "# PPP-1 Preview Discussion", "", f"> **{VALIDITY_LABEL}**", "",
        "The preview establishes a paper-facing descriptive scaffold, not a comparative verdict. "
        "Its most consequential analytic feature is missingness: "
        f"{errorful} of the {len(per_design)} design-by-SUT rows contain at least one recorded error. "
        "Accordingly, every mean travels with its expected, numeric, error, ungraded, and "
        "unrecorded denominators. This prevents differential parser or judge failures from being "
        "mistaken for substantive performance differences.", "",
        "The method-major layout remains useful for the confirmatory study because it shows where "
        "evidence coverage is strong enough to interpret and where additional validation would be "
        "needed. PPP-1 does not resolve those questions: it uses three inexpensive SUTs, one judge, "
        "base items only, and no perturbation or gate evidence. The registered confirmatory study "
        "therefore remains separate and unchanged.", "",
    ])


def _limitations() -> str:
    return "\n".join([
        "# PPP-1 Preview Limitations", "", f"> **{VALIDITY_LABEL}**", "",
        "> **Limitations box.** This packet covers exactly three inexpensive SUTs and uses a",
        "> single Gemini judge for judge-required surfaces. It is an exploratory manuscript",
        "> preview, contains no perturbation battery or G1–G7 evidence, and provides no",
        "> cross-family, consensus, release, or external-quotation basis. Mechanical ORDINAL",
        "> and citation-gated ANCHOR scores retain their existing contracts. Errors and",
        "> ungraded cells remain missing and are never imputed. Contested items have no",
        "> headline composite and remain separate disclosure/coherence/settled-core evidence.",
        "",
    ])


def build_packet(run_dir: Path, output_dir: Path, bank_items: Sequence[Any],
                 manuscript_root: Path, bank_dir: Optional[Path] = None) -> None:
    """Validate one finalized immutable run and create one new packet directory."""
    bank_dir = bank_dir or PROJECT / "05-BANK-YAML"
    run_dir, output_dir, manuscript_root, bank_dir = (
        Path(path).resolve() for path in (run_dir, output_dir, manuscript_root, bank_dir)
    )
    if output_dir.exists():
        raise PacketError(f"packet destination already exists: {output_dir}")
    metadata, identity, records = _load_final_run(run_dir)
    source_texts = {}
    for name in MANUSCRIPT_SOURCE_NAMES:
        path = manuscript_root / name
        try:
            source_texts[name] = path.read_text(encoding="utf-8").rstrip()
        except OSError as exc:
            raise PacketError(f"manuscript source is unreadable: {path}") from exc
    custody = _raw_custody(run_dir, records)
    rows = _normalized_rows(identity, records, bank_items, custody)
    per_design, per_sut, overall = _summaries(rows)
    if any(row["expected_n"] != EXPECTED_ITEMS for row in per_sut):
        raise PacketError("per-SUT expected denominator is not 226")
    if any(row["headline_expected_n"] != EXPECTED_HEADLINE_PER_SUT for row in per_sut):
        raise PacketError("per-SUT headline denominator is not 222")
    trace_rows = _trace_rows(per_design, per_sut, overall)

    output_dir.mkdir(parents=True)
    (output_dir / "tables").mkdir()
    (output_dir / "figures").mkdir()
    normalized_fields = (
        "validity_label", "source_run", "source_file", "source_line",
        "checkpoint_file", "checkpoint_line", "raw_evidence_file",
        "raw_line_start", "raw_line_end", "raw_line_count", "raw_span_sha256",
        "raw_call_hashes", "call_count", "cell_cost_usd", "judge_text_sha256s",
        "checkpoint_judge_text_sha256s", "judge_hashes_match", "cell_key", "item_id", "sut",
        "design", "kind", "status", "score_path", "headline_score", "disclosure",
        "coherence", "settled_core_fraction", "matter", "manner", "end", "error",
    )
    _write_csv(output_dir / "02-normalized-cells.csv", rows, normalized_fields)
    trace_fields = (
        "validity_label", "artifact", "row_key", "displayed_field", "displayed_value",
        "value_reference", "formula", "source_file", "source_fields", "source_cells",
    )
    _write_csv(output_dir / "03-traceability.csv", trace_rows, trace_fields)

    design_fields = ("design", "sut", *SUMMARY_FIELDS)
    sut_fields = ("sut", *SUMMARY_FIELDS)
    overall_fields = ("scope", *SUMMARY_FIELDS)
    table_specs = [
        ("01-per-design-per-sut", "PPP-1 per-design × per-SUT", per_design, design_fields),
        ("02-per-sut-aggregate", "PPP-1 per-SUT aggregate", per_sut, sut_fields),
        ("03-overall-aggregate", "PPP-1 overall aggregate", overall, overall_fields),
    ]
    for stem, title, data, fields in table_specs:
        labeled = [{"validity_label": VALIDITY_LABEL, **row} for row in data]
        _write_csv(output_dir / "tables" / f"{stem}.csv", labeled,
                   ("validity_label", *fields))
        (output_dir / "tables" / f"{stem}.md").write_text(
            _markdown_table(title, data, fields), encoding="utf-8")

    design_means = {
        (row["design"], row["sut"]): row["mean"] for row in per_design
    }
    design_series = [(sut, [design_means[(design, sut)] for design in DESIGN_ORDER])
                     for sut in SUT_ORDER]
    (output_dir / "figures" / "01-design-by-sut.svg").write_text(
        _svg("PPP-1 design-by-SUT observed means", DESIGN_ORDER, design_series),
        encoding="utf-8")
    (output_dir / "figures" / "02-per-sut-aggregate.svg").write_text(
        _svg("PPP-1 per-SUT observed means", ("all base items",),
             [(row["sut"], (row["mean"],)) for row in per_sut]), encoding="utf-8")

    results = _results(per_sut, overall[0])
    discussion = _discussion(per_design)
    limitations = _limitations()
    (output_dir / "05-preview-results.md").write_text(results, encoding="utf-8")
    (output_dir / "06-preview-discussion.md").write_text(discussion, encoding="utf-8")
    (output_dir / "07-preview-limitations.md").write_text(limitations, encoding="utf-8")

    trace_md = "\n".join([
        "# PPP-1 Traceability", "", f"> **{VALIDITY_LABEL}**", "",
        "Every empirical value in the packet is derived from `checkpoint.jsonl` through "
        "`02-normalized-cells.csv`. `scores.fraction` supplies ORDINAL, ANCHOR, and OPEN "
        "headline values; `judge.score` supplies EPISODE values; contested fields remain "
        "separate. `03-traceability.csv` enumerates each summary field and its contributing "
        "cell keys. Every normalized row also records its sequential raw-ledger line span, "
        "exact line/span hashes, paid-call count, actual-first cell cost, and judge-text hashes. "
        "Where parsed checkpoint judge text exists its hashes are reconciled to the raw ledger; "
        "error cells without persisted parsed judge text are labeled not-applicable rather than "
        "silently treated as a match. No raw prompt or response text is copied. Errors are "
        "retained without imputation.", "",
    ])
    (output_dir / "04-traceability.md").write_text(trace_md, encoding="utf-8")

    assembled_parts = [
        "# WCF-Bench — PPP-1 Assembled Manuscript Preview", "",
        f"> **{VALIDITY_LABEL}**", "",
        "This assembled review copy snapshots the unchanged manuscript foundation, then adds "
        "the PPP-1 preview Results, Discussion, and limitations. It does not modify the "
        "release-labeled manuscript source files.", "",
    ]
    for name in MANUSCRIPT_SOURCE_NAMES:
        assembled_parts.extend([f"> **{VALIDITY_LABEL}**", "", source_texts[name], ""])
    assembled_parts.extend([results, discussion, limitations])
    assembled = "\n".join(assembled_parts).rstrip() + "\n"
    (output_dir / "08-assembled-manuscript-preview.md").write_text(
        assembled, encoding="utf-8")

    source_manifest = {
        "validity_label": VALIDITY_LABEL,
        "run_status": metadata["run_status"],
        "input_artifacts": [
            _source_entry("run_identity", run_dir / "ppp1-run-identity.json",
                          "only frozen run identity"),
            _source_entry("checkpoint", run_dir / "checkpoint.jsonl",
                          f"final COMPLETE checkpoint; {len(records)} cells"),
            _source_entry("raw_evidence", run_dir / "raw-evidence.jsonl",
                          "final append-only raw ledger selected by run identity"),
            _source_entry("final_metadata", run_dir / "run-metadata.json",
                          "unsuffixed final metadata selected; run_status COMPLETE"),
            _source_entry("final_report", run_dir / "ppp1-report.md",
                          "unsuffixed final report selected"),
            _bank_source_entry(bank_dir, bank_items),
            *[
                _source_entry("manuscript_source", manuscript_root / name,
                              f"exact unchanged source selected: {name}")
                for name in MANUSCRIPT_SOURCE_NAMES
            ],
        ],
        "score_contract": {
            "ordinal_anchor_open": "checkpoint.jsonl:scores.fraction",
            "episode": "checkpoint.jsonl:judge.score",
            "contested": "checkpoint.jsonl:scores.contested.* (no headline composite)",
            "missingness": "errors/ungraded/unrecorded are not imputed",
        },
        "roster": {"suts": list(SUT_ORDER), "judge": JUDGE},
        "generated_files": list(PACKET_FILE_NAMES),
    }
    (output_dir / "01-source-manifest.json").write_text(
        json.dumps(source_manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    readme = "\n".join([
        "# PPP-1 Exploratory Manuscript Packet", "", f"> **{VALIDITY_LABEL}**", "",
        f"Final run status: **{metadata['run_status']}**. This directory was generated offline "
        "from the immutable PPP-1 identity, final metadata/report, checkpoint, raw-evidence "
        "custody ledger, frozen bank aggregate, and unchanged manuscript-source hashes. It "
        "contains normalized "
        "cells, denominator-explicit tables, two self-contained SVG figures, preview prose, an "
        "assembled review copy, and field-level traceability.", "",
        "No raw prompt or response text is copied into this packet. No error is imputed. No "
        "model ranking, gate, release, family-level, consensus, T4-completion, or external-quotation "
        "claim is supported.", "",
    ])
    (output_dir / "00-README.md").write_text(readme, encoding="utf-8")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--bank-dir", type=Path, default=PROJECT / "05-BANK-YAML")
    parser.add_argument("--manuscript-root", type=Path, default=PROJECT / "08-PAPER")
    args = parser.parse_args(argv)
    try:
        build_packet(args.run_dir, args.output_dir, load_items(str(args.bank_dir)),
                     args.manuscript_root, args.bank_dir)
    except PacketError as exc:
        parser.error(str(exc))
    print(f"PPP-1 packet created: {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
