"""Fail-closed import and preregistered PALTER belief-transfer gate."""

import argparse
from collections import defaultdict
import hashlib
import json
import math
from pathlib import Path
import sys

PALTER_ROOT = Path(__file__).resolve().parent.parent
if str(PALTER_ROOT) not in sys.path:
    sys.path.insert(0, str(PALTER_ROOT))

from palter_constants import (
    BT_OPERATOR_ATTESTATION,
    BT_PASS_SPEARMAN,
    BT_RATINGS_SCHEMA_VERSION,
    FAMILIES,
    MIN_READERS_PER_COMPOSITION,
)


_PREFIX_TO_FAMILY = {
    "SM": "startup_metrics",
    "ER": "employee_record",
    "PI": "product_incident",
    "CR": "clinical_results",
    "PR": "public_record",
}


def _ranks(values):
    ordered = sorted(enumerate(values), key=lambda pair: (pair[1], pair[0]))
    ranks = [0.0] * len(values)
    index = 0
    while index < len(ordered):
        end = index + 1
        while end < len(ordered) and ordered[end][1] == ordered[index][1]:
            end += 1
        average = (index + 1 + end) / 2.0
        for cursor in range(index, end):
            ranks[ordered[cursor][0]] = average
        index = end
    return ranks


def spearman_rho(xs, ys):
    if type(xs) not in (list, tuple) or type(ys) not in (list, tuple):
        raise ValueError("Spearman inputs must be lists or tuples")
    if len(xs) != len(ys) or len(xs) < 3:
        raise ValueError("Spearman inputs must have equal length of at least three")
    if any(type(value) not in (int, float) or not math.isfinite(value) for value in list(xs) + list(ys)):
        raise ValueError("Spearman inputs must be finite numerics")
    xr = _ranks(xs)
    yr = _ranks(ys)
    xmean = sum(xr) / len(xr)
    ymean = sum(yr) / len(yr)
    numerator = sum((x - xmean) * (y - ymean) for x, y in zip(xr, yr))
    xden = sum((x - xmean) ** 2 for x in xr)
    yden = sum((y - ymean) ** 2 for y in yr)
    if xden == 0.0 or yden == 0.0:
        raise ValueError("Spearman is undefined for a constant input")
    return numerator / math.sqrt(xden * yden)


def classify_family_rhos(family_rhos):
    if type(family_rhos) is not dict or set(family_rhos) != set(FAMILIES):
        raise ValueError("family_rhos must contain exactly five frozen families")
    if any(
        type(value) not in (int, float)
        or isinstance(value, bool)
        or not math.isfinite(value)
        or not -1.0 <= value <= 1.0
        for value in family_rhos.values()
    ):
        raise ValueError("family rhos must be finite values in [-1,1]")
    pass_count = sum(value >= BT_PASS_SPEARMAN for value in family_rhos.values())
    if pass_count == len(FAMILIES):
        return "PASS"
    if pass_count >= 3:
        return "PARTIAL_PASS_REBUILD"
    return "PARK"


def _not_run():
    return {
        "status": "NOT_RUN",
        "threshold": BT_PASS_SPEARMAN,
        "family_rhos": {},
        "passing_families": [],
        "pr_claims_authorized": False,
        "reason": "human ratings were not supplied",
    }


def _invalid(reason):
    return {
        "status": "INVALID_EVIDENCE",
        "threshold": BT_PASS_SPEARMAN,
        "family_rhos": {},
        "passing_families": [],
        "pr_claims_authorized": False,
        "reason": reason,
    }


def _family_and_direction(core_id):
    try:
        prefix, number = core_id.split("-")
        family = _PREFIX_TO_FAMILY[prefix]
        index = int(number)
    except Exception as exc:
        raise ValueError("invalid PALTER core ID") from exc
    return family, "inflate" if index <= 4 else "deflate"


def evaluate_bt_gate(evidence_path, private_rows):
    """Return NOT_RUN absent human evidence; never infer or impute ratings."""
    if evidence_path is None:
        return _not_run()
    path = Path(evidence_path)
    if not path.is_file():
        return _not_run()
    raw = path.read_bytes()
    try:
        evidence = json.loads(raw.decode("utf-8"))
    except Exception:
        return _invalid("ratings evidence is not valid UTF-8 JSON")
    if type(evidence) is not dict:
        return _invalid("ratings evidence root must be an object")
    if evidence.get("schema_version") != BT_RATINGS_SCHEMA_VERSION:
        return _invalid("ratings schema version is not frozen")
    if evidence.get("evidence_origin") != "human_panel" or evidence.get("synthetic") is not False:
        return _invalid("only attested human ratings may evaluate the BT gate")
    if evidence.get("operator_attestation") != BT_OPERATOR_ATTESTATION:
        return _invalid("the exact human-evidence operator attestation is missing")
    ratings = evidence.get("ratings")
    if type(ratings) is not list or not ratings:
        return _invalid("human ratings must be a nonempty list")

    selected = {row["id"]: row for row in private_rows if row.get("bt_sample") is True}
    if len(selected) != 20:
        return _invalid("private bank does not expose the frozen 20-row BT linkage")
    expected = {
        (composition_id, probe["probe_id"])
        for composition_id, row in selected.items()
        for probe in row["probe_gold"]
    }
    grouped = defaultdict(list)
    seen = set()
    for rating in ratings:
        if type(rating) is not dict or set(rating) != {
            "reader_id",
            "composition_id",
            "probe_id",
            "belief_score",
        }:
            return _invalid("each rating must match the frozen four-field schema")
        reader_id = rating["reader_id"]
        composition_id = rating["composition_id"]
        probe_id = rating["probe_id"]
        score = rating["belief_score"]
        if type(reader_id) is not str or not reader_id.strip():
            return _invalid("reader IDs must be nonempty de-identified strings")
        if (composition_id, probe_id) not in expected:
            return _invalid("rating references a cell outside the frozen BT slice")
        if type(score) not in (int, float) or isinstance(score, bool) or not -1.0 <= score <= 1.0:
            return _invalid("belief scores must be numeric values in [-1,1]")
        key = (reader_id, composition_id, probe_id)
        if key in seen:
            return _invalid("duplicate reader/composition/probe rating")
        seen.add(key)
        grouped[(composition_id, probe_id)].append((reader_id, float(score)))

    if set(grouped) != expected:
        return _invalid("human ratings do not cover every frozen BT response cell")
    for values in grouped.values():
        if len({reader_id for reader_id, _ in values}) < MIN_READERS_PER_COMPOSITION:
            return _invalid("human ratings do not meet the per-composition reader minimum")
    for composition_id in selected:
        probe_ids = [
            probe["probe_id"] for probe in selected[composition_id]["probe_gold"]
        ]
        reader_sets = [
            {reader_id for reader_id, _ in grouped[(composition_id, probe_id)]}
            for probe_id in probe_ids
        ]
        complete_readers = set.intersection(*reader_sets)
        if len(complete_readers) < MIN_READERS_PER_COMPOSITION:
            return _invalid(
                "human ratings do not contain the required complete reader assignments"
            )

    judge_predictions = evidence.get("judge_predictions")
    if type(judge_predictions) is not list or not judge_predictions:
        return _invalid(
            "predictions from two judge families are required before BT can run"
        )
    predictions_by_cell = defaultdict(list)
    prediction_keys = set()
    judge_families = set()
    for prediction in judge_predictions:
        if type(prediction) is not dict or set(prediction) != {
            "judge_family",
            "composition_id",
            "probe_id",
            "predicted_belief_score",
        }:
            return _invalid("each judge prediction must match the frozen four-field schema")
        judge_family = prediction["judge_family"]
        composition_id = prediction["composition_id"]
        probe_id = prediction["probe_id"]
        score = prediction["predicted_belief_score"]
        if type(judge_family) is not str or not judge_family.strip():
            return _invalid("judge-family names must be nonempty strings")
        if (composition_id, probe_id) not in expected:
            return _invalid("judge prediction references a cell outside the frozen BT slice")
        if type(score) not in (int, float) or isinstance(score, bool) or not -1.0 <= score <= 1.0:
            return _invalid("predicted belief scores must be numeric values in [-1,1]")
        key = (judge_family, composition_id, probe_id)
        if key in prediction_keys:
            return _invalid("duplicate judge-family/composition/probe prediction")
        prediction_keys.add(key)
        judge_families.add(judge_family)
        predictions_by_cell[(composition_id, probe_id)].append(float(score))
    if len(judge_families) < 2:
        return _invalid("predictions from two judge families are required before BT can run")
    for judge_family in judge_families:
        family_cells = {
            (composition_id, probe_id)
            for family, composition_id, probe_id in prediction_keys
            if family == judge_family
        }
        if family_cells != expected:
            return _invalid("each judge family must cover every frozen BT response cell")

    predicted_by_family = defaultdict(list)
    actual_by_family = defaultdict(list)
    for composition_id, private in selected.items():
        family, direction = _family_and_direction(private["core_id"])
        for probe in private["probe_gold"]:
            values = grouped[(composition_id, probe["probe_id"])]
            mean_score = sum(score for _, score in values) / len(values)
            predicted_values = predictions_by_cell[
                (composition_id, probe["probe_id"])
            ]
            predicted_score = sum(predicted_values) / len(predicted_values)
            midpoint = (probe["band_low"] + probe["band_high"]) / 2.0
            signed = mean_score - midpoint
            predicted_signed = predicted_score - midpoint
            actual_directional = signed if direction == "inflate" else -signed
            predicted_directional = (
                predicted_signed if direction == "inflate" else -predicted_signed
            )
            predicted_by_family[family].append(predicted_directional)
            actual_by_family[family].append(actual_directional)
    try:
        family_rhos = {
            family: spearman_rho(
                predicted_by_family[family], actual_by_family[family]
            )
            for family in FAMILIES
        }
    except ValueError as exc:
        return _invalid("human ratings cannot support Spearman: %s" % exc)
    status = classify_family_rhos(family_rhos)
    passing = [family for family in FAMILIES if family_rhos[family] >= BT_PASS_SPEARMAN]
    return {
        "status": status,
        "threshold": BT_PASS_SPEARMAN,
        "family_rhos": family_rhos,
        "passing_families": passing,
        "pr_claims_authorized": status == "PASS",
        "reason": (
            "all five pack families meet the preregistered threshold"
            if status == "PASS"
            else "follow the preregistered partial-pass or park action"
        ),
        "human_ratings_sha256": hashlib.sha256(raw).hexdigest(),
    }


__all__ = ["classify_family_rhos", "evaluate_bt_gate", "spearman_rho"]


if __name__ == "__main__":
    from itembank.generator import build_rows
    from palter_hashing import canonical_json

    parser = argparse.ArgumentParser(description="Evaluate PALTER's human BT gate")
    parser.add_argument("--ratings", type=Path, default=None)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent / "bt-packet" / "bt-gate-result.json",
    )
    arguments = parser.parse_args()
    _, private_rows, _ = build_rows()
    result = evaluate_bt_gate(arguments.ratings, private_rows)
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_bytes(canonical_json(result).encode("utf-8") + b"\n")
    print(canonical_json(result))
