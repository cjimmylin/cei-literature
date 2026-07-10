#!/usr/bin/env python3
"""Deterministic blinded annotation sampling and separate private linkage."""

import argparse
from collections import defaultdict
from collections.abc import Iterable as IterableABC, Mapping as MappingABC
from copy import deepcopy
import hashlib
import json
import math
import os
from pathlib import Path
import random
import sys
import tempfile
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from zerosum_common import ADVICE_CLASSES, RHO_GRID, read_jsonl, write_jsonl  # noqa: E402


PathLike = Union[str, Path]
MINIMUM_UNIQUE_RESPONSES = 200
REQUIRED_ANNOTATORS_PER_RESPONSE = 2
STRATIFICATION_FIELDS = (
    "domain", "rho", "opacity_tier", "dose_turn", "provisional_class",
)
CODING_FORBIDDEN_FIELDS = frozenset((
    "model", "model_id", "model_name", "model_family", "vendor", "provider",
    "evaluated_model", "generator_model",
    "judge", "judge_label", "judge_labels", "judge_output", "judge_outputs",
    "judges", "human_label",
    "gold", "expected_class", "fixture_intended_class", "rho",
    "payoff_correlation", "certificate", "certificate_id",
    "correct_option_id", "welfare_optimal_option_id", "provisional_class",
    "response_id", "item_id",
))
CODER_VISIBLE_CONTEXT_FIELDS = frozenset((
    "surface", "scenario", "situation", "setup", "escalation",
    "agentic_action", "messages", "role", "content", "user", "turn",
    "changes", "text", "question", "options", "trajectory_turn",
))

_TEXT_FIELDS = ("response_text", "response", "advice", "output")
_OPTIONAL_SURFACE_FIELDS = (
    "model_prompt", "prompt", "context", "trajectory_turn", "domain",
)
_OPEN_RECORD_TYPES = frozenset((
    "advice_primary", "monitoring_twin", "no_frame_twin", "open_advice",
))


def _canonical_identifier(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("%s must be a nonblank string" % label)
    normalized = " ".join(value.split())
    if value != normalized:
        raise ValueError("%s must use canonical whitespace" % label)
    return normalized


def _response_id(record: Mapping[str, Any]) -> str:
    value = next(
        (record[key] for key in ("response_id", "id") if key in record), None
    )
    return _canonical_identifier(value, "response_id")


def _response_text(record: Mapping[str, Any]) -> str:
    value = next(
        (
            record[key]
            for key in _TEXT_FIELDS
            if isinstance(record.get(key), str)
        ),
        "",
    )
    if not value.strip():
        raise ValueError("every response requires nonblank response text")
    return value


def _is_open_response(record: Mapping[str, Any]) -> bool:
    record_type = record.get("record_type")
    return record_type is None or record_type in _OPEN_RECORD_TYPES


def _stratum(record: Mapping[str, Any]) -> Tuple[Any, ...]:
    return tuple(record[field] for field in STRATIFICATION_FIELDS)


def _annotation_id(seed: int, response_id: str) -> str:
    digest = hashlib.sha256(
        ("zerosum-annotation\x1f%d\x1f%s" % (seed, response_id)).encode("utf-8")
    ).hexdigest()[:20]
    return "zs-ann-%s" % digest


def _blinded_surface(value: Any) -> Any:
    """Recursively retain only registered coder-visible context fields."""

    if isinstance(value, MappingABC):
        return {
            str(key): _blinded_surface(child)
            for key, child in value.items()
            if str(key).lower() in CODER_VISIBLE_CONTEXT_FIELDS
        }
    if isinstance(value, list):
        return [_blinded_surface(child) for child in value]
    if isinstance(value, tuple):
        return [_blinded_surface(child) for child in value]
    return deepcopy(value)


def _validate_stratification(record: Mapping[str, Any]) -> None:
    domain = record.get("domain")
    if not isinstance(domain, str) or not domain.strip():
        raise ValueError("stratification field domain must be a nonblank string")
    rho = record.get("rho")
    if (
        not isinstance(rho, (int, float))
        or isinstance(rho, bool)
        or not math.isfinite(rho)
        or not any(rho == registered for registered in RHO_GRID)
    ):
        raise ValueError("stratification field rho is outside the registered grid")
    opacity = record.get("opacity_tier")
    if type(opacity) is not int or opacity not in (1, 2, 3, 4):
        raise ValueError("stratification field opacity_tier must be 1, 2, 3, or 4")
    dose_turn = record.get("dose_turn")
    if type(dose_turn) is not int or dose_turn not in (0, 1, 2, 3):
        raise ValueError("stratification field dose_turn must be 0, 1, 2, or 3")
    if record.get("provisional_class") not in ADVICE_CLASSES:
        raise ValueError("stratification field provisional_class is invalid")


def _select_stratified(
    records: Sequence[Mapping[str, Any]], sample_size: int, seed: int
) -> List[Mapping[str, Any]]:
    buckets = defaultdict(list)
    for record in records:
        buckets[_stratum(record)].append(record)
    rng = random.Random(seed)
    for key in sorted(buckets):
        rng.shuffle(buckets[key])

    selected = []
    keys = sorted(buckets)
    while len(selected) < sample_size:
        progressed = False
        for key in keys:
            if buckets[key]:
                selected.append(buckets[key].pop())
                progressed = True
                if len(selected) == sample_size:
                    break
        if not progressed:
            raise ValueError("not enough unique responses for requested sample")
    rng.shuffle(selected)
    return selected


def build_annotation_packet(
    responses: Iterable[Mapping[str, Any]],
    *,
    sample_size: int = MINIMUM_UNIQUE_RESPONSES,
    seed: int = 20260709,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], Dict[str, Any]]:
    """Return coder views, private linkage, and a non-empirical packet manifest."""

    if not isinstance(sample_size, int) or isinstance(sample_size, bool):
        raise TypeError("sample_size must be an integer")
    if sample_size < MINIMUM_UNIQUE_RESPONSES:
        raise ValueError("annotation packet requires at least 200 unique responses")
    if not isinstance(seed, int) or isinstance(seed, bool) or seed < 0:
        raise ValueError("seed must be a nonnegative integer")
    if isinstance(responses, (str, bytes, bytearray)) or not isinstance(
        responses, IterableABC
    ):
        raise TypeError("responses must be an iterable of mappings")
    records = []
    seen = set()
    for value in responses:
        if not isinstance(value, MappingABC):
            raise TypeError("every response must be a mapping")
        record = dict(value)
        if not _is_open_response(record):
            continue
        response_id = _response_id(record)
        _response_text(record)
        _validate_stratification(record)
        if response_id in seen:
            raise ValueError("duplicate response_id: %s" % response_id)
        seen.add(response_id)
        records.append(record)
    if len(records) < sample_size:
        raise ValueError("not enough unique responses for requested sample")

    selected = _select_stratified(records, sample_size, seed)
    coding_records = []
    linkage_records = []
    for position, source in enumerate(selected):
        response_id = _response_id(source)
        annotation_id = _annotation_id(seed, response_id)
        coding = {
            "annotation_id": annotation_id,
            "response_text": _response_text(source),
            "annotation_form": {
                "advice_class": None,
                "fr": None,
                "response_status": None,
                "evidence_spans": [],
            },
        }
        for key in _OPTIONAL_SURFACE_FIELDS:
            if key in source and key != "domain":
                coding[key] = _blinded_surface(source[key])
        coding_records.append(coding)
        linkage = deepcopy(source)
        linkage.update({
            "annotation_id": annotation_id,
            "packet_position": position,
            "response_id": response_id,
        })
        linkage_records.append(linkage)

    manifest = {
        "schema_version": "zerosum-annotation-v1",
        "seed": seed,
        "unique_responses": len(coding_records),
        "required_annotators_per_response": REQUIRED_ANNOTATORS_PER_RESPONSE,
        "stratification_fields": list(STRATIFICATION_FIELDS),
        "strata_represented": len({_stratum(record) for record in selected}),
        "coding_packet_contains_private_linkage": False,
        "eligible_for_empirical_decision": False,
        "gate_status": "PENDING_HUMAN_ANNOTATION",
    }
    return coding_records, linkage_records, manifest


def write_annotation_packet(
    responses: Iterable[Mapping[str, Any]],
    coding_path: PathLike,
    linkage_path: PathLike,
    *,
    sample_size: int = MINIMUM_UNIQUE_RESPONSES,
    seed: int = 20260709,
) -> Dict[str, Any]:
    """Write physically separate coding and linkage JSONL artifacts."""

    coding_destination = Path(coding_path)
    linkage_destination = Path(linkage_path)
    if coding_destination.resolve() == linkage_destination.resolve():
        raise ValueError("coding and linkage paths must be physically separate")
    coding_destination.parent.mkdir(parents=True, exist_ok=True)
    linkage_destination.parent.mkdir(parents=True, exist_ok=True)
    coding, linkage, manifest = build_annotation_packet(
        responses, sample_size=sample_size, seed=seed
    )
    write_jsonl(coding_destination, coding)
    write_jsonl(linkage_destination, linkage)
    return manifest


def _write_manifest(path: Path, manifest: Mapping[str, Any]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", newline="\n", dir=str(path.parent),
            prefix=".%s." % path.name, suffix=".tmp", delete=False,
        ) as handle:
            temporary = Path(handle.name)
            json.dump(
                manifest, handle, ensure_ascii=False, sort_keys=True,
                separators=(",", ":"), allow_nan=False,
            )
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


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--coding", type=Path, required=True)
    parser.add_argument("--linkage", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--sample-size", type=int, default=MINIMUM_UNIQUE_RESPONSES)
    parser.add_argument("--seed", type=int, default=20260709)
    args = parser.parse_args(argv)

    paths = (args.input, args.coding, args.linkage, args.manifest)
    if len({path.resolve() for path in paths}) != len(paths):
        raise ValueError(
            "input, coding, linkage, and manifest paths must be physically separate"
        )
    manifest = write_annotation_packet(
        read_jsonl(args.input),
        args.coding,
        args.linkage,
        sample_size=args.sample_size,
        seed=args.seed,
    )
    _write_manifest(args.manifest, manifest)
    return 0


def validate_annotation_rows(rows: Iterable[Mapping[str, Any]]) -> None:
    """Validate completed human rows before any private relinking occurs."""

    seen = set()
    for row in rows:
        if not isinstance(row, MappingABC):
            raise TypeError("annotation rows must be mappings")
        pair = (
            _canonical_identifier(row.get("annotation_id"), "annotation_id"),
            _canonical_identifier(row.get("annotator_id"), "annotator_id"),
        )
        if pair in seen:
            raise ValueError("duplicate annotation row")
        seen.add(pair)
        if row.get("advice_class") not in ADVICE_CLASSES:
            raise ValueError("invalid advice class")
        if type(row.get("fr")) is not bool:
            raise ValueError("fr must be boolean")
        if row.get("response_status") not in (
            "answered", "refusal", "empty", "invalid"
        ):
            raise ValueError("invalid response status")
        spans = row.get("evidence_spans")
        if (
            not isinstance(spans, (list, tuple))
            or not spans
            or any(not isinstance(span, str) or not span.strip() for span in spans)
        ):
            raise ValueError("evidence_spans must contain nonblank verbatim spans")


__all__ = [
    "CODER_VISIBLE_CONTEXT_FIELDS", "CODING_FORBIDDEN_FIELDS",
    "MINIMUM_UNIQUE_RESPONSES",
    "REQUIRED_ANNOTATORS_PER_RESPONSE",
    "STRATIFICATION_FIELDS", "build_annotation_packet",
    "main", "validate_annotation_rows", "write_annotation_packet",
]


if __name__ == "__main__":
    raise SystemExit(main())
