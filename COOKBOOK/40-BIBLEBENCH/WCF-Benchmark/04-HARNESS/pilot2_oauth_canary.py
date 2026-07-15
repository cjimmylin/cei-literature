#!/usr/bin/env python3
"""Immutable 16-record Pilot 2 Codex-OAuth canary with task custody."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Callable, Dict, Mapping, Optional, Sequence

import pilot2_run as controller
import pilot2_preflight as preflight
from pilot2_judge import Pilot2CodexOAuthJudge, JudgeAdapterError


ROUTE_COUNTS = (("open", 8), ("contested", 4), ("episode", 4))


class CanaryError(RuntimeError):
    """The registered 16-record zero-dollar judge canary failed."""


class OAuthQuotaStop(CanaryError):
    pass


class EvidenceCustodyStop(CanaryError):
    pass


_QUOTA_PATTERN = re.compile(
    r"quota|allowance|usage limit|rate limit|credits? remaining|nearly exhausted",
    re.IGNORECASE)


def _canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":")).encode("utf-8")


def _write_json_new(path: Path, value: Any) -> None:
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True, ensure_ascii=False)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())


def _append_jsonl(path: Path, value: Any) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(_canonical(value).decode("utf-8") + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def build_fixture_records() -> list:
    """Create synthetic, non-bank judge records with exact route geometry."""
    records = []
    index = 0
    contested_kinds = (
        "contested_disclosure", "contested_position",
        "contested_coherence", "contested_settled_core")
    for route, count in ROUTE_COUNTS:
        for _ in range(count):
            index += 1
            if route == "open":
                call_kind = "open_award"
            elif route == "contested":
                call_kind = contested_kinds[index - 9]
            else:
                call_kind = "episode_keypoints"
            judge_prompt = "Synthetic non-bank scorer prompt."
            if index == 1:
                judge_prompt = "N" * 250_000
            criteria = [{
                "criterion_id": f"FIXTURE-{route.upper()}-{index:02d}",
                "points": 1.0,
            }]
            records.append({
                "record_id": f"pilot2-canary-{index:02d}",
                "sut": "pilot2-synthetic-canary",
                "route": route,
                "call_kind": call_kind,
                "points": 1.0,
                "payload": {
                    "judge_prompt": judge_prompt,
                    "response": "Synthetic non-bank answer.",
                    "criteria": criteria,
                },
            })
    return records


def build_fixture_packet() -> Dict[str, Any]:
    records = build_fixture_records()
    return {
        "schema_version": 1,
        "validity_label": preflight.VALIDITY_LABEL,
        "source": "synthetic_non_bank_fixture_only",
        "input_sha256": hashlib.sha256(_canonical(records)).hexdigest(),
        "records": records,
    }


def run_fixture_canary(
    judge_batch: Callable[[Sequence[Mapping[str, Any]]], Mapping[str, Any]],
) -> Dict[str, Any]:
    """Run injected OAuth judging sequentially; the caller owns live authorization."""
    records = build_fixture_records()
    all_batches = []
    missing = []
    for route, _count in ROUTE_COUNTS:
        route_records = [row for row in records if row["route"] == route]
        batches, oversized = controller.build_dynamic_judge_batches(route_records)
        if oversized:
            raise CanaryError("registered near-ceiling record exceeded byte contract")
        all_batches.extend(batches)
    returned = []
    for batch in all_batches:  # concurrency one by construction
        result = judge_batch(batch)
        rows = result.get("records") if isinstance(result, Mapping) else None
        unresolved = result.get("missing_record_ids") if isinstance(result, Mapping) else None
        if not isinstance(rows, list) or unresolved:
            raise CanaryError("OAuth canary lost or malformed records")
        returned.extend(rows)
    expected = {row["record_id"] for row in records}
    observed = [row.get("record_id") for row in returned if isinstance(row, Mapping)]
    if len(observed) != 16 or set(observed) != expected or len(set(observed)) != 16:
        raise CanaryError("OAuth canary did not return 16 unique registered IDs")
    return {"status": "PASS", "records": 16, "batches": len(all_batches)}


class EvidenceProcessRunner:
    """Persist every Codex task stream and stderr before interpretation."""

    def __init__(self, output_dir: Path, runner: Callable[..., Any]) -> None:
        self.tasks_dir = output_dir / "tasks"
        self.runner = runner
        self.task_count = 0
        self.total_elapsed_seconds = 0.0

    def __call__(self, command: Sequence[str], **kwargs: Any) -> Any:
        self.task_count += 1
        task_id = f"task-{self.task_count:03d}"
        started = time.monotonic()
        try:
            process = self.runner(command, **kwargs)
            stdout = getattr(process, "stdout", "") or ""
            stderr = getattr(process, "stderr", "") or ""
            returncode = getattr(process, "returncode", None)
            caught = None
        except BaseException as exc:
            process, stdout, returncode, caught = None, "", None, exc
            stderr = f"{type(exc).__name__}: {exc}"
        elapsed = time.monotonic() - started
        self.total_elapsed_seconds += elapsed
        try:
            (self.tasks_dir / f"{task_id}.events.jsonl").write_text(
                stdout, encoding="utf-8")
            (self.tasks_dir / f"{task_id}.stderr.txt").write_text(
                stderr, encoding="utf-8")
            _write_json_new(self.tasks_dir / f"{task_id}.metadata.json", {
                "task_id": task_id, "elapsed_seconds": round(elapsed, 6),
                "returncode": returncode,
                "command_sha256": hashlib.sha256(
                    "\0".join(str(part) for part in command).encode()).hexdigest(),
                "stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
                "stderr_sha256": hashlib.sha256(stderr.encode()).hexdigest(),
            })
        except OSError as exc:
            raise EvidenceCustodyStop(
                f"could not persist Codex task evidence: {task_id}") from exc
        if caught is not None:
            raise caught
        if _QUOTA_PATTERN.search(stdout + "\n" + stderr):
            raise OAuthQuotaStop("Codex OAuth quota or allowance warning observed")
        return process


def _result_satisfied(call_kind: str, result: Mapping[str, Any]) -> Optional[bool]:
    if call_kind == "open_award":
        values = [row.get("satisfied") for row in result.get("awards") or ()]
        return all(values) if values else None
    if call_kind.startswith("open_axis_") or call_kind == "contested_coherence":
        return float(result.get("score", 0)) > 0
    if call_kind == "contested_disclosure":
        return bool(result.get("avoided_settled") and result.get("located_divide"))
    if call_kind == "contested_position":
        return result.get("position_defensible") is True
    if call_kind in {"contested_settled_core", "episode_keypoints"}:
        values = [row.get("satisfied") for row in result.get("verdicts") or ()]
        return all(values) if values else None
    return None


def calculate_weighted_arithmetic(
    records: Sequence[Mapping[str, Any]], verdicts: Sequence[Mapping[str, Any]],
) -> Dict[str, Any]:
    source = {row["record_id"]: row for row in records}
    buckets = {route: {"earned": 0.0, "graded": 0.0, "possible": 0.0}
               for route, _ in ROUTE_COUNTS}
    for row in records:
        buckets[row["route"]]["possible"] += float(row["points"])
    for row in verdicts:
        original = source.get(row.get("record_id"))
        if original is None:
            raise CanaryError("verdict has unknown record ID")
        satisfied = _result_satisfied(original["call_kind"], row.get("result") or {})
        if satisfied is None:
            continue
        points = float(original["points"])
        bucket = buckets[original["route"]]
        bucket["graded"] += points
        if satisfied:
            bucket["earned"] += points
    rendered: Dict[str, Any] = {}
    total = {"earned": 0.0, "graded": 0.0, "possible": 0.0}
    for route, _ in ROUTE_COUNTS:
        values = buckets[route]
        rendered[route] = {
            "earned_points": values["earned"],
            "graded_points": values["graded"],
            "possible_points": values["possible"],
            "weighted_fraction": (
                values["earned"] / values["graded"] if values["graded"] else None),
        }
        for name in total:
            total[name] += values[name]
    rendered["total"] = {
        "earned_points": total["earned"],
        "graded_points": total["graded"],
        "possible_points": total["possible"],
        "weighted_fraction": total["earned"] / total["graded"] if total["graded"] else None,
    }
    return rendered


def run_canary(
    selected: Mapping[str, Any], output_dir: Path, *,
    process_runner: Callable[..., Any] = subprocess.run,
) -> Dict[str, Any]:
    output_dir = Path(output_dir)
    if output_dir.exists():
        raise CanaryError("canary output directory must be new and absent")
    output_dir.mkdir(parents=True)
    (output_dir / "tasks").mkdir()
    _write_json_new(output_dir / "canary-inputs.json", dict(selected))
    records = [dict(row) for row in selected.get("records") or ()]
    if (len(records) != 16
            or [row.get("route") for row in records]
            != ["open"] * 8 + ["contested"] * 4 + ["episode"] * 4
            or len({row.get("record_id") for row in records}) != 16):
        raise CanaryError("canary input is not exact 8/4/4 geometry")
    evidence_runner = EvidenceProcessRunner(output_dir, process_runner)
    persisted: Dict[str, Dict[str, Any]] = {}
    verdict_path = output_dir / "verdicts.jsonl"

    def persist(row: Dict[str, Any]) -> None:
        record_id = str(row.get("record_id"))
        if record_id in persisted:
            raise EvidenceCustodyStop(f"duplicate verdict persistence: {record_id}")
        _append_jsonl(verdict_path, row)
        persisted[record_id] = dict(row)

    stop_kind = stop_reason = None
    start = time.monotonic()
    try:
        grouped: Dict[tuple, list] = {}
        for row in records:
            grouped.setdefault((row["route"], row["call_kind"]), []).append(row)
        for rows in grouped.values():
            batches, oversized = controller.build_dynamic_judge_batches(rows)
            if oversized:
                raise CanaryError("registered near-ceiling canary exceeded byte limit")
            for batch in batches:
                result = Pilot2CodexOAuthJudge(
                    runner=evidence_runner, persist=persist).judge(batch)
                if result["missing_record_ids"]:
                    raise CanaryError("OAuth canary lost records after registered retries")
    except OAuthQuotaStop as exc:
        stop_kind, stop_reason = "OAUTH_QUOTA", str(exc)
    except EvidenceCustodyStop as exc:
        stop_kind, stop_reason = "EVIDENCE_CUSTODY", str(exc)
    except JudgeAdapterError as exc:
        stop_kind = ("FORBIDDEN_TOOL" if "forbidden tool event" in str(exc)
                     else "MECHANICAL_FAILURE")
        stop_reason = str(exc)
    except Exception as exc:
        stop_kind, stop_reason = "MECHANICAL_FAILURE", f"{type(exc).__name__}: {exc}"
    verdicts = list(persisted.values())
    missing = [row["record_id"] for row in records if row["record_id"] not in persisted]
    try:
        arithmetic = calculate_weighted_arithmetic(records, verdicts)
    except Exception as exc:
        arithmetic = None
        stop_kind = stop_kind or "ARITHMETIC_FAILURE"
        stop_reason = stop_reason or str(exc)
    status = "PASS" if not stop_kind and not missing and len(verdicts) == 16 else "FAIL"
    report = {
        "schema_version": 1, "validity_label": preflight.VALIDITY_LABEL,
        "status": status, "record_count": len(verdicts),
        "unique_record_count": len(persisted), "missing_record_ids": missing,
        "task_count": evidence_runner.task_count,
        "elapsed_seconds": round(time.monotonic() - start, 6),
        "stop_kind": stop_kind, "stop_reason": stop_reason,
        "input_sha256": selected.get("input_sha256"), "arithmetic": arithmetic,
    }
    _write_json_new(output_dir / "canary-report.json", report)
    (output_dir / "canary-report.md").write_text("\n".join([
        "# WCF-Bench Pilot 2 OAuth Canary", "",
        f"> **{preflight.VALIDITY_LABEL}**", "",
        f"Status: **{status}**", f"Records: {len(verdicts)}/16",
        f"Stop: {stop_kind or 'none'}", "",
    ]), encoding="utf-8")
    return report


def main(
    argv: Optional[Sequence[str]] = None, *,
    process_runner: Callable[..., Any] = subprocess.run,
) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--go", action="store_true")
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args(argv)
    if not args.go:
        print("refusing OAuth invocation without explicit --go", file=sys.stderr)
        return 2
    report = run_canary(
        build_fixture_packet(), args.output_dir, process_runner=process_runner)
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
