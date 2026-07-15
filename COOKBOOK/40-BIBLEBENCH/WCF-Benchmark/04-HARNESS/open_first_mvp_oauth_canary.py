#!/usr/bin/env python3
"""Registered 16-record, zero-dollar Codex-OAuth judge canary."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Callable, Dict, Mapping, Optional, Sequence

from wcfbench.codex_oauth_judge import CodexOAuthJudge, JudgeAdapterError
from wcfbench.loader import load_items
from wcfbench.routing import scorer_kind


PROJECT = Path(__file__).resolve().parent.parent
PPP1_DIR = PROJECT / "07-PILOTS" / "20260713-ppp1-exploratory-preview"
BANK_DIR = PROJECT / "05-BANK-YAML"
CANARY_SUT = "meta-llama/llama-3.1-8b-instruct"
VALIDITY_LABEL = (
    "EXPLORATORY WCF-BENCH OPEN-FIRST MVP · ONE RUN PER SUT · "
    "SINGLE UNQUALIFIED CODEX-OAUTH GPT-5.6 SOL JUDGE · NON-QUOTABLE"
)
ROUTE_COUNTS = (("open", 8), ("contested", 4), ("episode", 4))
_QUOTA_PATTERN = re.compile(
    r"\b(quota|usage limit|rate limit|allowance exhausted|"
    r"credits? (?:exhausted|remaining|warning)|insufficient credits?)\b",
    re.IGNORECASE,
)


class CanaryError(RuntimeError):
    """The immutable source, output custody, or registered canary contract failed."""


class OAuthQuotaStop(CanaryError):
    """The saved ChatGPT OAuth session emitted a quota or allowance warning."""


class EvidenceCustodyStop(CanaryError):
    """A task event stream, stderr, or verdict could not be persisted."""


def _now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(
        timespec="seconds").replace("+00:00", "Z")


def _canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
    ).encode("utf-8")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _bank_tree_sha256(bank_dir: Path) -> str:
    digest = hashlib.sha256()
    paths = sorted((*bank_dir.glob("*.yaml"), *bank_dir.glob("*.yml")))
    if not paths:
        raise CanaryError(f"frozen bank is empty: {bank_dir}")
    for path in paths:
        digest.update(path.name.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def _read_jsonl(path: Path) -> list:
    rows = []
    try:
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise CanaryError(f"non-object JSONL row at {path}:{number}")
            rows.append(value)
    except (OSError, json.JSONDecodeError) as exc:
        raise CanaryError(f"immutable source is unreadable: {path}") from exc
    return rows


def _successful_ppp1_responses(ppp1_dir: Path) -> Dict[str, str]:
    checkpoint_path = ppp1_dir / "checkpoint.jsonl"
    evidence_path = ppp1_dir / "raw-evidence.jsonl"
    checkpoint = {}
    for row in _read_jsonl(checkpoint_path):
        if row.get("sut") != CANARY_SUT:
            continue
        item_id = row.get("item_id")
        if not isinstance(item_id, str) or item_id in checkpoint:
            raise CanaryError("PPP-1 checkpoint has duplicate or invalid canary SUT cells")
        calls = (row.get("usage") or {}).get("calls") or []
        has_persisted_sut_call = any(
            isinstance(call, Mapping)
            and call.get("role") == "sut"
            and call.get("name") == CANARY_SUT
            for call in calls
        )
        checkpoint[item_id] = has_persisted_sut_call
    responses: Dict[str, str] = {}
    for row in _read_jsonl(evidence_path):
        if row.get("role") != "sut" or row.get("name") != CANARY_SUT:
            continue
        item_id = row.get("item_id")
        text = row.get("text")
        if (not isinstance(item_id, str) or item_id in responses
                or row.get("error") is not None or not isinstance(text, str) or not text):
            raise CanaryError("PPP-1 raw evidence has invalid canary SUT custody")
        if checkpoint.get(item_id) is not True:
            raise CanaryError(f"PPP-1 source cell is not successfully persisted: {item_id}")
        responses[item_id] = text
    return responses


def select_canary_records(
    *, ppp1_dir: Path = PPP1_DIR, bank_dir: Path = BANK_DIR,
) -> Dict[str, Any]:
    """Select a stable 8/4/4 set from successful immutable PPP-1 cells."""
    responses = _successful_ppp1_responses(ppp1_dir)
    items = sorted(load_items(str(bank_dir)), key=lambda item: item.id)
    records = []
    for route, target in ROUTE_COUNTS:
        selected = 0
        for item in items:
            if scorer_kind(item) != route or item.id not in responses:
                continue
            for rubric_index, keypoint in enumerate(item.rubric, 1):
                criterion = keypoint.criterion
                if len(criterion.encode("utf-8")) > 256:
                    continue
                records.append({
                    "record_id": (
                        f"canary::{route}::{item.id}::kp{rubric_index:02d}"),
                    "sut": CANARY_SUT,
                    "route": route,
                    "item_id": item.id,
                    "rubric_index": rubric_index,
                    "points": float(keypoint.points),
                    "payload": {
                        "criterion_id": criterion,
                        "response": responses[item.id],
                    },
                })
                selected += 1
                if selected == target:
                    break
            if selected == target:
                break
        if selected != target:
            raise CanaryError(
                f"PPP-1 source cannot supply {target} legal {route} records")
    source_hashes = {
        "ppp1_raw_evidence_sha256": _sha256(ppp1_dir / "raw-evidence.jsonl"),
        "ppp1_checkpoint_sha256": _sha256(ppp1_dir / "checkpoint.jsonl"),
        "bank_tree_sha256": _bank_tree_sha256(bank_dir),
    }
    input_sha256 = hashlib.sha256(_canonical_bytes(records)).hexdigest()
    return {
        "schema_version": 1,
        "validity_label": VALIDITY_LABEL,
        "selected_at": "deterministic-from-immutable-sources",
        "selection_rule": (
            "exact PPP-1 Llama SUT; item-id order; bank rubric order; "
            "criteria within the adapter's 256-byte ceiling"),
        "source_hashes": source_hashes,
        "input_sha256": input_sha256,
        "records": records,
    }


def _write_json_new(path: Path, value: Any) -> None:
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, sort_keys=True, ensure_ascii=False, indent=2)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())


def _append_jsonl(path: Path, value: Any) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(_canonical_bytes(value).decode("utf-8") + "\n")
        handle.flush()
        os.fsync(handle.fileno())


class EvidenceProcessRunner:
    """Persist each Codex task's event stream and stderr before interpretation."""

    def __init__(self, output_dir: Path, runner: Callable[..., Any]) -> None:
        self.tasks_dir = output_dir / "tasks"
        self.runner = runner
        self.task_count = 0
        self.total_elapsed_seconds = 0.0

    def __call__(self, command: Sequence[str], **kwargs: Any) -> Any:
        self.task_count += 1
        task_id = f"task-{self.task_count:03d}"
        started = time.monotonic()
        process = None
        caught: Optional[BaseException] = None
        try:
            process = self.runner(command, **kwargs)
            returncode = getattr(process, "returncode", None)
            stdout = getattr(process, "stdout", "") or ""
            stderr = getattr(process, "stderr", "") or ""
        except BaseException as exc:
            caught = exc
            returncode = None
            stdout = ""
            stderr = f"{type(exc).__name__}: {exc}"
        elapsed = time.monotonic() - started
        self.total_elapsed_seconds += elapsed
        try:
            (self.tasks_dir / f"{task_id}.events.jsonl").write_text(
                stdout, encoding="utf-8")
            (self.tasks_dir / f"{task_id}.stderr.txt").write_text(
                stderr, encoding="utf-8")
            _write_json_new(self.tasks_dir / f"{task_id}.metadata.json", {
                "task_id": task_id,
                "recorded_at": _now(),
                "elapsed_seconds": round(elapsed, 6),
                "returncode": returncode,
                "command_sha256": hashlib.sha256(
                    "\0".join(str(part) for part in command).encode("utf-8")).hexdigest(),
                "stdout_sha256": hashlib.sha256(stdout.encode("utf-8")).hexdigest(),
                "stderr_sha256": hashlib.sha256(stderr.encode("utf-8")).hexdigest(),
            })
        except OSError as exc:
            raise EvidenceCustodyStop(
                f"could not persist Codex task evidence: {task_id}") from exc
        if caught is not None:
            raise caught
        if _QUOTA_PATTERN.search(stdout + "\n" + stderr):
            raise OAuthQuotaStop("Codex OAuth quota or allowance warning observed")
        return process


def calculate_weighted_arithmetic(
    records: Sequence[Mapping[str, Any]], verdicts: Sequence[Mapping[str, Any]],
) -> Dict[str, Any]:
    """Compute deterministic point-weighted canary checks; ungraded stays missing."""
    source = {str(row["record_id"]): row for row in records}
    buckets = {route: {"earned": 0.0, "graded": 0.0, "possible": 0.0}
               for route, _count in ROUTE_COUNTS}
    for row in records:
        buckets[str(row["route"])]["possible"] += float(row["points"])
    for row in verdicts:
        record_id = str(row.get("record_id"))
        if record_id not in source:
            raise CanaryError(f"verdict has an unknown record ID: {record_id}")
        record = source[record_id]
        route = str(record["route"])
        points = float(record["points"])
        verdict = row.get("verdict") or {}
        if route == "contested":
            value = verdict.get("verdict")
            if value == "ungraded":
                continue
            satisfied = value == "satisfied"
        else:
            satisfied = verdict.get("satisfied") is True
        buckets[route]["graded"] += points
        if satisfied:
            buckets[route]["earned"] += points
    rendered: Dict[str, Any] = {}
    total = {"earned": 0.0, "graded": 0.0, "possible": 0.0}
    for route, _count in ROUTE_COUNTS:
        values = buckets[route]
        rendered[route] = {
            "earned_points": values["earned"],
            "graded_points": values["graded"],
            "possible_points": values["possible"],
            "weighted_fraction": (
                values["earned"] / values["graded"] if values["graded"] else None),
        }
        for key in total:
            total[key] += values[key]
    rendered["total"] = {
        "earned_points": total["earned"],
        "graded_points": total["graded"],
        "possible_points": total["possible"],
        "weighted_fraction": (
            total["earned"] / total["graded"] if total["graded"] else None),
    }
    return rendered


def _render_report(report: Mapping[str, Any]) -> str:
    return "\n".join([
        "# WCF-Bench Open-First MVP OAuth Canary",
        "",
        f"> **{VALIDITY_LABEL}**",
        "",
        f"- Status: **{report['status']}**",
        f"- Records: {report['record_count']}/16",
        f"- Codex tasks: {report['task_count']}",
        f"- Elapsed: {report['elapsed_seconds']:.6f} seconds",
        f"- OPEN four-record fallback used: {report['open_fallback_used']}",
        f"- Stop kind: {report.get('stop_kind') or 'none'}",
        f"- Missing IDs: {', '.join(report['missing_record_ids']) or 'none'}",
        "",
        "This canary checks only the registered mechanical OAuth judge interface. "
        "It is not judge qualification and creates no quotable benchmark result.",
        "",
    ])


def _is_forbidden_tool_error(exc: BaseException) -> bool:
    return isinstance(exc, JudgeAdapterError) and "forbidden tool event" in str(exc)


def _is_evidence_custody_error(exc: BaseException) -> bool:
    return isinstance(exc, JudgeAdapterError) and "could not be persisted" in str(exc)


def run_canary(
    selected: Mapping[str, Any], output_dir: Path,
    *, process_runner: Callable[..., Any] = subprocess.run,
) -> Dict[str, Any]:
    """Run once into a new directory and always write a terminal PASS/FAIL report."""
    output_dir = Path(output_dir)
    if output_dir.exists():
        raise CanaryError("canary output directory must be new and absent")
    output_dir.mkdir(parents=True)
    tasks_dir = output_dir / "tasks"
    tasks_dir.mkdir()
    _write_json_new(output_dir / "canary-inputs.json", dict(selected))
    records = [dict(row) for row in selected.get("records") or []]
    if (len(records) != 16
            or [row.get("route") for row in records] !=
            ["open"] * 8 + ["contested"] * 4 + ["episode"] * 4):
        raise CanaryError("canary input is not the exact registered 8/4/4 geometry")

    evidence_runner = EvidenceProcessRunner(output_dir, process_runner)
    verdict_path = output_dir / "verdicts.jsonl"
    persisted: Dict[str, Dict[str, Any]] = {}

    def persist(row: Dict[str, Any]) -> None:
        record_id = str(row.get("record_id"))
        if record_id in persisted:
            raise CanaryError(f"duplicate verdict persistence: {record_id}")
        _append_jsonl(verdict_path, row)
        persisted[record_id] = dict(row)

    def judge(rows: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
        adapter = CodexOAuthJudge(runner=evidence_runner, persist=persist)
        return adapter.judge(rows)

    start = time.monotonic()
    open_fallback_used = False
    stop_kind = None
    stop_reason = None
    try:
        open_rows = records[:8]
        try:
            result = judge(open_rows)
        except OAuthQuotaStop:
            raise
        except EvidenceCustodyStop:
            raise
        except Exception as exc:
            if _is_forbidden_tool_error(exc):
                raise CanaryError("FORBIDDEN_TOOL") from exc
            if _is_evidence_custody_error(exc):
                raise CanaryError("EVIDENCE_CUSTODY") from exc
            if evidence_runner.task_count != 1:
                raise CanaryError("OPEN_RETRY_FAILED") from exc
            open_fallback_used = True
            pending = [row for row in open_rows
                       if row["record_id"] not in persisted]
            for offset in range(0, len(pending), 4):
                result = judge(pending[offset:offset + 4])
                if result["missing_record_ids"]:
                    raise CanaryError("OPEN_FALLBACK_FAILED")
        else:
            if result["missing_record_ids"]:
                raise CanaryError("OPEN_MISSING_RECORDS")
        for route, rows in (
            ("contested", records[8:12]), ("episode", records[12:16]),
        ):
            result = judge(rows)
            if result["missing_record_ids"]:
                raise CanaryError(f"{route.upper()}_MISSING_RECORDS")
    except OAuthQuotaStop as exc:
        stop_kind = "OAUTH_QUOTA"
        stop_reason = str(exc)
    except EvidenceCustodyStop as exc:
        stop_kind = "EVIDENCE_CUSTODY"
        stop_reason = str(exc)
    except Exception as exc:
        if str(exc) == "FORBIDDEN_TOOL" or _is_forbidden_tool_error(exc.__cause__ or exc):
            stop_kind = "FORBIDDEN_TOOL"
        elif (str(exc) == "EVIDENCE_CUSTODY"
              or _is_evidence_custody_error(exc.__cause__ or exc)):
            stop_kind = "EVIDENCE_CUSTODY"
        else:
            stop_kind = "MECHANICAL_FAILURE"
        stop_reason = f"{type(exc).__name__}: {exc}"

    missing = [row["record_id"] for row in records
               if row["record_id"] not in persisted]
    verdicts = list(persisted.values())
    try:
        arithmetic = calculate_weighted_arithmetic(records, verdicts)
    except Exception as exc:
        arithmetic = None
        stop_kind = stop_kind or "ARITHMETIC_FAILURE"
        stop_reason = stop_reason or f"{type(exc).__name__}: {exc}"
    status = "PASS" if not stop_kind and not missing and len(persisted) == 16 else "FAIL"
    if status == "FAIL" and stop_kind is None:
        stop_kind = "MISSING_RECORDS"
        stop_reason = "one or more registered record IDs were not persisted"
    report = {
        "schema_version": 1,
        "validity_label": VALIDITY_LABEL,
        "completed_at": _now(),
        "status": status,
        "record_count": len(persisted),
        "unique_record_count": len(set(persisted)),
        "missing_record_ids": missing,
        "task_count": evidence_runner.task_count,
        "elapsed_seconds": round(time.monotonic() - start, 6),
        "task_elapsed_seconds": round(evidence_runner.total_elapsed_seconds, 6),
        "open_fallback_used": open_fallback_used,
        "stop_kind": stop_kind,
        "stop_reason": stop_reason,
        "input_sha256": selected.get("input_sha256"),
        "source_hashes": selected.get("source_hashes"),
        "arithmetic": arithmetic,
    }
    _write_json_new(output_dir / "canary-report.json", report)
    (output_dir / "canary-report.md").write_text(
        _render_report(report), encoding="utf-8")
    return report


def main(
    argv: Optional[Sequence[str]] = None,
    *, process_runner: Callable[..., Any] = subprocess.run,
) -> int:
    parser = argparse.ArgumentParser(
        description="Run the registered zero-dollar Codex-OAuth mechanical canary")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--go", action="store_true", help="invoke saved OAuth via codex exec")
    args = parser.parse_args(argv)
    if not args.go:
        print("refusing OAuth invocation without explicit --go", file=sys.stderr)
        return 2
    selected = select_canary_records()
    report = run_canary(selected, args.output_dir, process_runner=process_runner)
    print(json.dumps({
        "status": report["status"],
        "records": report["record_count"],
        "tasks": report["task_count"],
        "output_dir": str(args.output_dir),
    }, sort_keys=True))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
