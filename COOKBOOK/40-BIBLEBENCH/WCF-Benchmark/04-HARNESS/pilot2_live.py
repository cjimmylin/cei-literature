#!/usr/bin/env python3
"""Immutable custody and strict-cap primitives for a future authorized Pilot 2 run."""

from __future__ import annotations

import hashlib
import json
import math
import os
import threading
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Mapping

import pilot2_preflight as preflight


MANIFEST_COPY = "pilot2-manifest.json"
IDENTITY_FILE = "run-identity.json"
EVIDENCE_FILE = "raw-evidence.jsonl"
CHECKPOINT_FILE = "checkpoint.jsonl"


class CustodyStop(RuntimeError):
    """The immutable evidence chain or strict cap cannot be trusted."""


def _hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _write_new(path: Path, value: Mapping[str, Any]) -> None:
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True, ensure_ascii=False)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())


def _append(path: Path, value: Mapping[str, Any], lock: threading.Lock) -> None:
    with lock:
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(value, sort_keys=True, ensure_ascii=False) + "\n")
            handle.flush()
            os.fsync(handle.fileno())


@dataclass
class RunState:
    run_dir: Path
    cap_usd: float
    spent_usd: float = 0.0
    reservations: Dict[str, float] = field(default_factory=dict)
    lock: threading.Lock = field(default_factory=threading.Lock)

    def reserve(self, request_id: str, maximum_usd: float) -> None:
        if not isinstance(request_id, str) or not request_id:
            raise CustodyStop("reservation request ID is invalid")
        if (not math.isfinite(maximum_usd) or maximum_usd <= 0):
            raise CustodyStop("reservation amount is invalid")
        with self.lock:
            if request_id in self.reservations:
                raise CustodyStop("request already has a reservation")
            committed = self.spent_usd + sum(self.reservations.values())
            if committed + maximum_usd > self.cap_usd + 1e-12:
                raise CustodyStop("strict Pilot 2 cap would be exceeded")
            self.reservations[request_id] = maximum_usd
        _append(self.run_dir / EVIDENCE_FILE, {
            "kind": "reservation", "request_id": request_id,
            "maximum_usd": maximum_usd,
        }, self.lock)

    def settle(self, request_id: str, actual_usd: float) -> None:
        if not math.isfinite(actual_usd) or actual_usd < 0:
            raise CustodyStop("response-attributed cost is missing or invalid")
        with self.lock:
            maximum = self.reservations.get(request_id)
            if maximum is None:
                raise CustodyStop("settlement lacks reservation custody")
            if actual_usd > maximum + 1e-12:
                raise CustodyStop("response cost exceeds conservative reservation")
            self.spent_usd += actual_usd
            del self.reservations[request_id]
        _append(self.run_dir / EVIDENCE_FILE, {
            "kind": "cost_settlement", "request_id": request_id,
            "response_attributed_cost_usd": actual_usd,
            "cumulative_spend_usd": self.spent_usd,
        }, self.lock)

    def checkpoint_missing(self, cell_key: str, reason: str, *, attempts: int) -> None:
        if not isinstance(attempts, int) or isinstance(attempts, bool) or attempts < 1:
            raise CustodyStop("missing checkpoint attempts are invalid")
        _append(self.run_dir / CHECKPOINT_FILE, {
            "kind": "pilot2_cell", "cell_key": cell_key,
            "status": "error", "missing": True, "score": None,
            "reason": reason, "attempts": attempts,
        }, self.lock)


def prepare_run(manifest_path: Path, run_dir: Path, *, cap_usd: float) -> RunState:
    manifest_path = Path(manifest_path).resolve()
    run_dir = Path(run_dir).resolve()
    if run_dir.exists():
        raise CustodyStop("immutable run directory already exists")
    if (not math.isfinite(cap_usd) or cap_usd <= 0
            or cap_usd > preflight.PROPOSED_CAP_USD):
        raise CustodyStop("run cap is invalid or above the proposed Pilot 2 cap")
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CustodyStop("manifest is unreadable") from exc
    if (manifest.get("validity_label") != preflight.VALIDITY_LABEL
            or tuple(manifest.get("exact_sut_slugs") or ()) != preflight.SUTS
            or (manifest.get("geometry") or {}).get("sut_cells") != 1150):
        raise CustodyStop("manifest is not the exact Pilot 2 identity")
    run_dir.mkdir(parents=True)
    manifest_copy = run_dir / MANIFEST_COPY
    with manifest_path.open("rb") as source, manifest_copy.open("xb") as target:
        target.write(source.read())
        target.flush()
        os.fsync(target.fileno())
    _write_new(run_dir / IDENTITY_FILE, {
        "schema_version": 1,
        "kind": "wcf_bench_pilot2_immutable_run",
        "validity_label": preflight.VALIDITY_LABEL,
        "manifest_sha256": _hash(manifest_copy),
        "exact_sut_slugs": list(preflight.SUTS),
        "expected_cells": 1150,
        "scorable_cells": 1130,
        "diagnostic_only_cells": 20,
        "cap_usd": cap_usd,
    })
    return RunState(run_dir=run_dir, cap_usd=cap_usd)


def main() -> int:
    print("Pilot 2 live custody is implementation-only; no inference is invoked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
