"""Offline freeze/preflight contract for the OPEN6-SOL1 descriptive pilot.

This module intentionally has no credential or live-backend imports.  Its only CLI
phase materializes (or byte-validates) a deterministic manifest derived from the
complete runnable PUBLIC item surface.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from decimal import Decimal
from pathlib import Path
from typing import Iterable

from .loader import DESIGN_CODES, load_public_split
from .rubrics import spec_for


SCHEMA_VERSION = "walkworthy.open6-sol1.preflight.v1"
MANIFEST_DATE = "2026-07-14"
EXPECTED_ITEM_COUNT = 344
EXPECTED_ORDERED_ITEM_SHA256 = (
    "6db7d83dd5e24cf689e0eaf1fe7f8a1a09b6f5e4c2229018b63e241b39238839"
)
MODEL_COUNT = 6
OUTPUT_CAP_TOKENS = 2048
HARD_NTE_USD = "25.00"
OPENROUTER_NOMINAL_CALLS = 5886
OPENROUTER_RESERVE_CALLS = 295
OPENROUTER_HARD_CALL_CAP = 6181
SOL_CLASSIFIER_TURNS = 1722
SOL_JUDGE_UNITS = 5370
SOL_BATCH_MAX_UNITS = 24
SOL_JUDGE_BATCHES = 227
SOL_NOMINAL_TURNS = 1949
SOL_RESERVE_TURNS = 98
SOL_HARD_TURN_CAP = 2047
TOTAL_CATEGORY_CELLS = 10008

_ROSTER = (
    ("minimax/minimax-m3", "0.30", "1.20"),
    ("z-ai/glm-5.2", "0.903", "2.838"),
    ("deepseek/deepseek-v4-pro", "0.435", "0.87"),
    ("qwen/qwen3.5-397b-a17b", "0.385", "2.45"),
    ("google/gemma-4-31b-it", "0.12", "0.35"),
    ("meta-llama/llama-4-maverick", "0.20", "0.80"),
)

DISCLAIMER = (
    "Descriptive single-judge MVP only; no O5 verdict, G4 validation, release "
    "determination, judge-reliability claim, repeated-run stability claim, or "
    "universal best-model claim is authorized."
)


class ManifestMismatchError(RuntimeError):
    """Raised when an existing immutable manifest differs from the frozen bytes."""


class GeometryDriftError(RuntimeError):
    """Raised when the current PUBLIC surface no longer matches the authorized plan."""


def select_public_items(benchmark_root) -> list:
    """Load exactly the runnable PUBLIC surface and return canonical item-id order."""
    items = load_public_split(
        benchmark_root,
        include_exemplars=True,
        runnable_only=True,
    )
    return sorted(items, key=lambda item: (item.design, item.id))


def ordered_item_hash(items: Iterable) -> str:
    payload = "".join(f"{item.id}\n" for item in items).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _judge_units(item) -> int:
    spec = spec_for(item.design)
    if spec.unit == "item":
        return 1
    if spec.unit == "per_admin":
        return len(item.administrations)
    if spec.unit == "per_seat":
        return sum(admin.label.startswith("seat") for admin in item.administrations)
    if spec.unit == "per_turn":
        main = next(
            (admin for admin in item.administrations if admin.label == "main"),
            item.administrations[0],
        )
        return len(main.turns) + (1 if main.terminal_ask else 0)
    raise GeometryDriftError(f"unsupported scoring unit: {spec.unit!r}")


def _classifier_turns(item) -> int:
    return sum(
        1
        for admin in item.administrations
        for turn in admin.turns
        if turn.branches
    )


def derive_geometry(items: Iterable) -> dict:
    """Derive all call, judge-unit, category-cell, and batching counts."""
    items = list(items)
    by_design = []
    for design in DESIGN_CODES:
        design_items = [item for item in items if item.design == design]
        spec = spec_for(design)
        content_calls = sum(item.n_model_calls_single_pass() for item in design_items)
        allocation_calls = len(design_items) if design == "05-ordoamoris" else 0
        classifier_turns = sum(_classifier_turns(item) for item in design_items)
        judge_units = sum(_judge_units(item) for item in design_items)
        category_cells = judge_units * len(spec.categories)
        batches = math.ceil((judge_units * MODEL_COUNT) / SOL_BATCH_MAX_UNITS)
        by_design.append({
            "design": design,
            "item_count": len(design_items),
            "scoring_unit": spec.unit,
            "category_count": len(spec.categories),
            "sut_content_calls_per_model": content_calls,
            "design05_allocation_calls_per_model": allocation_calls,
            "classifier_turns_per_model": classifier_turns,
            "judge_units_per_model": judge_units,
            "category_cells_per_model": category_cells,
            "same_design_judge_batches": batches,
        })

    content_per_model = sum(row["sut_content_calls_per_model"] for row in by_design)
    allocation_per_model = sum(
        row["design05_allocation_calls_per_model"] for row in by_design
    )
    classifier_per_model = sum(row["classifier_turns_per_model"] for row in by_design)
    units_per_model = sum(row["judge_units_per_model"] for row in by_design)
    cells_per_model = sum(row["category_cells_per_model"] for row in by_design)
    return {
        "item_count": len(items),
        "model_count": MODEL_COUNT,
        "item_model_records": len(items) * MODEL_COUNT,
        "sut_content_calls_per_model": content_per_model,
        "design05_allocation_calls_per_model": allocation_per_model,
        "openrouter_nominal_calls": (
            content_per_model + allocation_per_model
        ) * MODEL_COUNT,
        "classifier_turns_per_model": classifier_per_model,
        "classifier_turns": classifier_per_model * MODEL_COUNT,
        "judge_units_per_model": units_per_model,
        "judge_units": units_per_model * MODEL_COUNT,
        "category_cells_per_model": cells_per_model,
        "category_cells": cells_per_model * MODEL_COUNT,
        "same_design_judge_batches": sum(
            row["same_design_judge_batches"] for row in by_design
        ),
        "by_design": by_design,
    }


def _decimal_product(value: str, multiplier: str = "1.10") -> str:
    return format((Decimal(value) * Decimal(multiplier)).normalize(), "f")


def _model_manifest() -> list[dict]:
    return [
        {
            "slug": slug,
            "input_per_m_usd": input_price,
            "output_per_m_usd": output_price,
            "provider_ceiling": {
                "formula": "observed_price_per_m_usd * 1.10",
                "prompt_per_m_usd": _decimal_product(input_price),
                "completion_per_m_usd": _decimal_product(output_price),
            },
        }
        for slug, input_price, output_price in _ROSTER
    ]


def _validate_authorized_geometry(items: list, geometry: dict) -> None:
    checks = {
        "item_count": (len(items), EXPECTED_ITEM_COUNT),
        "ordered_item_sha256": (
            ordered_item_hash(items), EXPECTED_ORDERED_ITEM_SHA256
        ),
        "openrouter_nominal_calls": (
            geometry["openrouter_nominal_calls"], OPENROUTER_NOMINAL_CALLS
        ),
        "classifier_turns": (geometry["classifier_turns"], SOL_CLASSIFIER_TURNS),
        "judge_units": (geometry["judge_units"], SOL_JUDGE_UNITS),
        "judge_batches": (
            geometry["same_design_judge_batches"], SOL_JUDGE_BATCHES
        ),
        "category_cells": (geometry["category_cells"], TOTAL_CATEGORY_CELLS),
    }
    drift = {
        name: {"actual": actual, "expected": expected}
        for name, (actual, expected) in checks.items()
        if actual != expected
    }
    if drift:
        raise GeometryDriftError(
            "OPEN6-SOL1 PUBLIC geometry drift: "
            + json.dumps(drift, sort_keys=True)
        )


def build_manifest(benchmark_root) -> dict:
    """Build the deterministic documentation-only OPEN6-SOL1 manifest."""
    items = select_public_items(benchmark_root)
    geometry = derive_geometry(items)
    _validate_authorized_geometry(items, geometry)
    return {
        "schema_version": SCHEMA_VERSION,
        "manifest_date": MANIFEST_DATE,
        "pilot": "WALKWORTHY-OPEN6-SOL1",
        "surface": {
            "split": "PUBLIC",
            "holdout_loaded": False,
            "include_exemplars": True,
            "runnable_only": True,
            "item_count": len(items),
            "ordered_item_ids": [item.id for item in items],
            "ordered_item_sha256": ordered_item_hash(items),
        },
        "geometry": geometry,
        "openrouter": {
            "role": "sut_only",
            "models": _model_manifest(),
            "model_count": MODEL_COUNT,
            "output_cap_tokens": OUTPUT_CAP_TOKENS,
            "provider_order": "price_sorted_within_exact_model",
            "provider_ceiling_multiplier": "1.10",
            "substitution_allowed": False,
            "reasoning_parameter": None,
            "max_concurrency": 2,
            "nominal_calls": OPENROUTER_NOMINAL_CALLS,
            "defect_replay_reserve_calls": OPENROUTER_RESERVE_CALLS,
            "hard_call_cap": OPENROUTER_HARD_CALL_CAP,
            "hard_nte_usd": HARD_NTE_USD,
            "retry_policy": "one_byte_identical_defect_replay_only",
        },
        "sol_oauth": {
            "role": "adaptive_router_and_single_judge",
            "model": "gpt-5.6-sol",
            "reasoning_effort": "medium",
            "classifier_turns": SOL_CLASSIFIER_TURNS,
            "judge_units": SOL_JUDGE_UNITS,
            "judge_batch_scope": "same_design_and_scoring_schema_only",
            "judge_batch_max_units": SOL_BATCH_MAX_UNITS,
            "judge_batches": SOL_JUDGE_BATCHES,
            "nominal_turns": SOL_NOMINAL_TURNS,
            "defect_replay_reserve_turns": SOL_RESERVE_TURNS,
            "hard_turn_cap": SOL_HARD_TURN_CAP,
            "automatic_credit_purchase": False,
            "substitution_allowed": False,
            "retry_policy": "one_byte_identical_defect_replay_only",
        },
        "claims_boundary": {
            "evidence_class": "descriptive_single_judge_mvp",
            "disclaimer": DISCLAIMER,
            "o5_verdict_authorized": False,
            "g4_validation_authorized": False,
            "release_claim_authorized": False,
            "standalone_supplement": True,
            "frozen_mvp_v0_1_unchanged": True,
        },
        "authorization": {
            "owner": "Jimmy Lin",
            "owner_memo": (
                "00-PORTFOLIO/20260714-jimmy-open6-sol1-authorization.md"
            ),
            "preflight_order": (
                "00-PORTFOLIO/20260714-open6-sol1-preflight-order.md"
            ),
            "preflight_only": True,
            "credential_access": False,
        },
    }


def canonical_json_bytes(value: dict) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def file_sha256(path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_or_validate_manifest(path, manifest: dict) -> str:
    """Create one immutable manifest, or validate its exact existing bytes."""
    path = Path(path)
    expected = canonical_json_bytes(manifest)
    if path.exists():
        if path.read_bytes() != expected:
            raise ManifestMismatchError(
                f"immutable manifest mismatch: {path}"
            )
        return "validated"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(expected)
    return "written"


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="WALKWORTHY OPEN6-SOL1 offline preflight"
    )
    subparsers = parser.add_subparsers(dest="phase", required=True)
    preflight = subparsers.add_parser(
        "preflight", help="write or validate the immutable PUBLIC manifest"
    )
    preflight.add_argument("--benchmark-root", required=True)
    preflight.add_argument("--manifest", required=True)
    return parser


def main(argv=None) -> int:
    args = _parser().parse_args(argv)
    if args.phase != "preflight":  # argparse makes this unreachable, deliberately fail closed.
        raise ValueError(f"unauthorized OPEN6-SOL1 phase: {args.phase!r}")
    manifest = build_manifest(args.benchmark_root)
    path = Path(args.manifest).resolve()
    action = write_or_validate_manifest(path, manifest)
    print(json.dumps({
        "action": action,
        "credential_access": False,
        "item_count": manifest["surface"]["item_count"],
        "manifest": str(path),
        "manifest_sha256": file_sha256(path),
        "phase": "preflight",
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
