#!/usr/bin/env python3
"""Run ZEROSUM P1 through synthetic fixtures or guarded live adapters."""

from __future__ import annotations

import argparse
from copy import deepcopy
import importlib
import json
import os
from pathlib import Path
import sys
import tempfile
from typing import Any, Dict, Mapping, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from harness.model_adapters import (  # noqa: E402
    ModelClient,
    PreconditionError,
    build_requests_for_record,
    validate_live_preconditions,
)
from harness.synthetic_profiles import PROFILES, fixture_response  # noqa: E402
from zerosum_common import read_jsonl  # noqa: E402


def _aligned_rows(
    bank: Sequence[Mapping[str, Any]], gold: Sequence[Mapping[str, Any]]
) -> Sequence[tuple]:
    private = {record.get("id"): record for record in gold}
    if len(private) != len(gold):
        raise ValueError("private gold IDs must be unique")
    if [record.get("id") for record in bank] != [record.get("id") for record in gold]:
        raise ValueError("public/private rows must be ID-aligned")
    return [(record, private[record["id"]]) for record in bank]


def _synthetic_choice_keys(
    bank: Sequence[Mapping[str, Any]], gold: Sequence[Mapping[str, Any]]
) -> Dict[str, Dict[str, str]]:
    """Build fixture-only option class keys without exposing them in requests."""

    private = {record["id"]: record for record in gold}
    keys = {}
    for record, gold_record in zip(bank, gold):
        if record.get("record_type") not in {"forced_anchor", "recognition_twin"}:
            continue
        parent = private.get(gold_record.get("parent_id"))
        if not parent or not isinstance(parent.get("option_text_by_class"), Mapping):
            raise ValueError("synthetic choice fixture is missing its private parent key")
        text_to_class = {
            text: advice_class
            for advice_class, text in parent["option_text_by_class"].items()
        }
        option_key = {
            option["id"]: text_to_class.get(option["text"])
            for option in record.get("options", [])
        }
        if any(advice_class is None for advice_class in option_key.values()):
            raise ValueError("synthetic choice option cannot be mapped to a class")
        keys[record["id"]] = option_key
    return keys


def run_synthetic(
    bank: Sequence[Mapping[str, Any]],
    gold: Sequence[Mapping[str, Any]],
    *,
    profiles: Sequence[str],
    seed: int,
) -> Dict[str, Any]:
    """Exercise the complete harness with deterministic planted fixtures."""

    if not isinstance(seed, int) or isinstance(seed, bool):
        raise ValueError("synthetic seed must be an integer")
    if not profiles or len(set(profiles)) != len(profiles):
        raise ValueError("synthetic profiles must be a nonempty unique list")
    unknown = set(profiles).difference(PROFILES)
    if unknown:
        raise ValueError("unknown synthetic profile(s): %s" % sorted(unknown))
    rows = _aligned_rows(bank, gold)
    choice_keys = _synthetic_choice_keys(bank, gold)
    responses = []
    for profile_name in profiles:
        for record, gold_record in rows:
            requests = build_requests_for_record(record, gold_record)
            for position, request in enumerate(requests):
                turn_index = position if record["record_type"] == "advice_primary" else 0
                planted = fixture_response(
                    profile_name,
                    record,
                    gold_record,
                    turn_index=turn_index,
                    seed=seed,
                    option_class_by_id=choice_keys.get(record["id"]),
                )
                responses.append(
                    {
                        "run_id": "zerosum-p1-synthetic-%d" % seed,
                        "model_id": profile_name,
                        "model_family": "deterministic_planted_fixture",
                        "vendor": "fixture",
                        "data_basis": "synthetic",
                        "seed": seed,
                        "item_id": record["id"],
                        "core_id": record["core_id"],
                        "record_type": record["record_type"],
                        "turn_index": turn_index,
                        "request_id": request["request_id"],
                        "rho": record["rho"],
                        "domain": record["domain"],
                        "frame": record["frame"],
                        "frame_alignment": record["frame_alignment"],
                        "opacity_tier": record["opacity_tier"],
                        "sf_cell": record["sf_cell"],
                        **planted,
                    }
                )
    return {
        "schema_version": 1,
        "study_id": "10CB-ZEROSUM-P1",
        "mode": "synthetic",
        "status": "HARNESS_VALIDATION_ONLY",
        "eligible_for_empirical_decision": False,
        "classifier_gate_status": "NOT_RUN_HUMAN",
        "live_pilot_status": "BLOCKED_PRECONDITIONS",
        "finetune_gate_status": "NOT_RUN_LLM",
        "seed": seed,
        "profiles": list(profiles),
        "responses": responses,
    }


def run_live(
    bank: Sequence[Mapping[str, Any]],
    *,
    clients: Sequence[ModelClient],
    config: Mapping[str, Any],
    calibration_report: Mapping[str, Any],
    preregistration_path: Path,
    credential_vendors: set,
) -> Dict[str, Any]:
    """Collect live responses only after a complete no-call preflight."""

    preflight = validate_live_preconditions(
        config,
        calibration_report,
        preregistration_path=preregistration_path,
        credential_vendors=credential_vendors,
    )
    roster = config["model_roster"]
    expected = [
        (row["model_id"], row["family"], row["vendor"])
        for row in roster
    ]
    observed = []
    for client in clients:
        try:
            observed.append((client.model_id, client.family, client.vendor))
        except AttributeError as exc:
            raise PreconditionError("client roster metadata is incomplete") from exc
        if not callable(getattr(client, "generate", None)):
            raise PreconditionError("client roster contains a non-callable adapter")
    if observed != expected:
        raise PreconditionError("client roster does not exactly match frozen config")

    # Build and validate the entire request schedule before the first external call.
    request_schedule = [
        (record, list(build_requests_for_record(record))) for record in bank
    ]
    responses = []
    for client in clients:
        for seed in config["seeds"]:
            for record, requests in request_schedule:
                for position, canonical_request in enumerate(requests):
                    request = deepcopy(canonical_request)
                    request["request_id"] = "%s--seed-%d" % (request["request_id"], seed)
                    raw_response = client.generate(request, seed=seed)
                    if not isinstance(raw_response, str):
                        raise RuntimeError("live adapter returned a non-text response")
                    responses.append({
                    "model_id": client.model_id,
                    "model_family": client.family,
                    "vendor": client.vendor,
                    "data_basis": "live",
                    "item_id": record["id"],
                    "core_id": record["core_id"],
                    "record_type": record["record_type"],
                    "seed": seed,
                    "turn_index": position if record["record_type"] == "advice_primary" else 0,
                    "request_id": request["request_id"],
                    "rho": record["rho"],
                    "domain": record["domain"],
                    "frame": record["frame"],
                    "frame_alignment": record["frame_alignment"],
                    "opacity_tier": record["opacity_tier"],
                    "sf_cell": record["sf_cell"],
                    "raw_response": raw_response,
                    "response_status": "responded" if raw_response.strip() else "empty",
                    })
    return {
        "schema_version": 1,
        "study_id": "10CB-ZEROSUM-P1",
        "mode": "live",
        "status": "LIVE_RESPONSES_COLLECTED_UNSCORED",
        "eligible_for_empirical_decision": False,
        "classifier_gate_status": calibration_report["verdict"],
        "preflight": preflight,
        "responses": responses,
    }


def _write_json_atomic(path: Path, payload: Mapping[str, Any]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", newline="\n", dir=str(path.parent),
            prefix=".%s." % path.name, suffix=".tmp", delete=False,
        ) as handle:
            temporary = Path(handle.name)
            json.dump(payload, handle, ensure_ascii=False, sort_keys=True, allow_nan=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(str(temporary), str(path))
    except BaseException:
        if temporary is not None:
            try:
                temporary.unlink()
            except FileNotFoundError:
                pass
        raise


def _load_factory(spec: str):
    if not isinstance(spec, str) or ":" not in spec:
        raise PreconditionError("client factory must use module:callable syntax")
    module_name, attribute = spec.rsplit(":", 1)
    factory = getattr(importlib.import_module(module_name), attribute)
    if not callable(factory):
        raise PreconditionError("client factory is not callable")
    return factory


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bank", type=Path, default=ROOT / "itembank/bank/p1-private.jsonl")
    parser.add_argument("--gold", type=Path, default=ROOT / "itembank/gold/p1-private.gold.jsonl")
    parser.add_argument("--mode", choices=("synthetic", "live"), default="synthetic")
    parser.add_argument("--profiles", nargs="+", default=[
        "structure_sensitive", "flat_positional", "perverse_harmony", "null_fr", "gr_floor"
    ])
    parser.add_argument("--seed", type=int, default=2026070901)
    parser.add_argument("--config", type=Path)
    parser.add_argument("--calibration-report", type=Path)
    parser.add_argument("--preregistration", type=Path, default=ROOT / "preregistration.md")
    parser.add_argument("--client-factory")
    parser.add_argument("--credential-vendor", action="append", default=[])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    bank = read_jsonl(args.bank)
    if args.mode == "synthetic":
        result = run_synthetic(
            bank, read_jsonl(args.gold), profiles=args.profiles, seed=args.seed
        )
    else:
        if args.config is None or args.calibration_report is None or args.client_factory is None:
            parser.error("live mode requires --config, --calibration-report, and --client-factory")
        config = json.loads(args.config.read_text(encoding="utf-8"))
        calibration = json.loads(args.calibration_report.read_text(encoding="utf-8"))
        credential_vendors = set(args.credential_vendor)
        validate_live_preconditions(
            config,
            calibration,
            preregistration_path=args.preregistration,
            credential_vendors=credential_vendors,
        )
        factory = _load_factory(args.client_factory)
        clients = [factory(dict(row)) for row in config["model_roster"]]
        result = run_live(
            bank,
            clients=clients,
            config=config,
            calibration_report=calibration,
            preregistration_path=args.preregistration,
            credential_vendors=credential_vendors,
        )
    _write_json_atomic(args.output, result)
    print("wrote %d %s harness responses" % (len(result["responses"]), args.mode))
    print("status: %s" % result["status"])


if __name__ == "__main__":
    main()


__all__ = ["run_live", "run_synthetic"]
