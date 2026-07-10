"""Fail-closed human calibration metrics and one-repair gate state."""

from collections import Counter
from collections.abc import Iterable as IterableABC, Mapping as MappingABC
from copy import deepcopy
from dataclasses import dataclass
import hashlib
import math
from numbers import Real
import random
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

from zerosum_common import ADVICE_CLASSES
from scoring.judge_prompts import (
    JUDGE_FAMILIES, RESPONSE_STATUSES, validate_judge_output,
)


MINIMUM_HUMAN_RESPONSES = 200
MINIMUM_ANNOTATORS_PER_RESPONSE = 2
MINIMUM_KAPPA = 0.70
MINIMUM_MACRO_F1 = 0.75
MINIMUM_CLASS_F1 = 0.60

INITIAL = "INITIAL"
ONE_REPAIR_AUTHORIZED = "ONE_REPAIR_AUTHORIZED"
SECOND_FAIL_PARKED = "SECOND_FAIL_PARKED"
PASSED = "PASSED"

SYNTHETIC_BANNER = (
    "SYNTHETIC PLUMBING ONLY — no classifier gate was run; synthetic labels "
    "are not human evidence and are ineligible for empirical decisions."
)
_SYNTHETIC_KEY_MARKERS = frozenset(("fixture_intended_class",))
_SYNTHETIC_VALUE_KEYS = frozenset((
    "mode", "data_basis", "annotation_basis", "basis", "report_banner",
    "source", "origin",
))
_PROVENANCE_CONTAINER_KEYS = frozenset(("metadata", "provenance", "lineage"))
_CONTENT_VALUE_KEYS = frozenset(("response_text",))
_HUMAN_MODES = frozenset(("human", "live", "empirical"))


@dataclass(frozen=True)
class CalibrationResult:
    """Serializable result of a fail-closed calibration evaluation."""

    metrics: Mapping[str, Any]
    eligible_for_empirical_decision: bool
    verdict: str
    unique_responses: int
    double_coded_responses: int
    repair_state: str
    banner: str
    failures: Tuple[str, ...]
    data_basis: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "metrics": deepcopy(dict(self.metrics)),
            "eligible_for_empirical_decision": self.eligible_for_empirical_decision,
            "verdict": self.verdict,
            "unique_responses": self.unique_responses,
            "double_coded_responses": self.double_coded_responses,
            "repair_state": self.repair_state,
            "banner": self.banner,
            "failures": list(self.failures),
            "data_basis": self.data_basis,
        }


def cohen_kappa(left: Sequence[Any], right: Sequence[Any]) -> float:
    """Compute unweighted Cohen kappa for two aligned categorical sequences."""

    if isinstance(left, (str, bytes)) or isinstance(right, (str, bytes)):
        raise TypeError("kappa inputs must be sequences of labels")
    left_values = list(left)
    right_values = list(right)
    if not left_values or len(left_values) != len(right_values):
        raise ValueError("kappa inputs must be nonempty and aligned")
    total = len(left_values)
    observed = sum(a == b for a, b in zip(left_values, right_values)) / total
    left_counts = Counter(left_values)
    right_counts = Counter(right_values)
    expected = sum(
        (left_counts[label] / total) * (right_counts[label] / total)
        for label in set(left_counts) | set(right_counts)
    )
    if math.isclose(expected, 1.0, abs_tol=1e-15):
        return 1.0 if math.isclose(observed, 1.0, abs_tol=1e-15) else 0.0
    return (observed - expected) / (1.0 - expected)


def per_class_f1(
    expected: Sequence[str], predicted: Sequence[str]
) -> Dict[str, float]:
    """Return locked-class one-vs-rest F1 scores, including absent classes."""

    expected_values = list(expected)
    predicted_values = list(predicted)
    if not expected_values or len(expected_values) != len(predicted_values):
        raise ValueError("F1 inputs must be nonempty and aligned")
    if any(value not in ADVICE_CLASSES for value in expected_values + predicted_values):
        raise ValueError("F1 inputs contain an unlocked advice class")
    scores = {}
    for label in ADVICE_CLASSES:
        true_positive = sum(
            truth == label and guess == label
            for truth, guess in zip(expected_values, predicted_values)
        )
        false_positive = sum(
            truth != label and guess == label
            for truth, guess in zip(expected_values, predicted_values)
        )
        false_negative = sum(
            truth == label and guess != label
            for truth, guess in zip(expected_values, predicted_values)
        )
        denominator = 2 * true_positive + false_positive + false_negative
        scores[label] = 0.0 if denominator == 0 else 2 * true_positive / denominator
    return scores


def _percentile(values: Sequence[float], probability: float) -> float:
    ordered = sorted(values)
    if not ordered:
        raise ValueError("cannot take percentile of an empty sequence")
    position = probability * (len(ordered) - 1)
    low = int(math.floor(position))
    high = int(math.ceil(position))
    if low == high:
        return ordered[low]
    weight = position - low
    return ordered[low] * (1.0 - weight) + ordered[high] * weight


def _bootstrap_cis(
    expected: Sequence[str],
    predicted: Sequence[str],
    *,
    samples: int,
    seed: int,
) -> Dict[str, List[float]]:
    rng = random.Random(seed)
    count = len(expected)
    kappa_values = []
    macro_values = []
    for _ in range(samples):
        indices = [rng.randrange(count) for _ in range(count)]
        truth = [expected[index] for index in indices]
        guesses = [predicted[index] for index in indices]
        kappa_values.append(cohen_kappa(truth, guesses))
        f1_values = per_class_f1(truth, guesses).values()
        macro_values.append(sum(f1_values) / len(ADVICE_CLASSES))
    return {
        "kappa": [_percentile(kappa_values, 0.025), _percentile(kappa_values, 0.975)],
        "macro_f1": [
            _percentile(macro_values, 0.025), _percentile(macro_values, 0.975)
        ],
    }


def _metric_seed(seed: int, name: str) -> int:
    digest = hashlib.sha256(("%d:%s" % (seed, name)).encode("utf-8")).digest()
    return int.from_bytes(digest[:8], "big")


def classification_metrics(
    expected: Sequence[str],
    predicted: Sequence[str],
    *,
    bootstrap_samples: int = 400,
    seed: int = 20260709,
) -> Dict[str, Any]:
    """Compute kappa, locked-class F1, and deterministic bootstrap CIs."""

    scores = per_class_f1(expected, predicted)
    return {
        "kappa": cohen_kappa(expected, predicted),
        "macro_f1": sum(scores.values()) / len(ADVICE_CLASSES),
        "per_class_f1": scores,
        "bootstrap_ci": _bootstrap_cis(
            expected, predicted, samples=bootstrap_samples, seed=seed
        ),
        "n": len(expected),
    }


def _categorical_kappa_metrics(
    left: Sequence[Any], right: Sequence[Any], *, samples: int, seed: int
) -> Dict[str, Any]:
    rng = random.Random(seed)
    count = len(left)
    values = []
    for _ in range(samples):
        indices = [rng.randrange(count) for _ in range(count)]
        values.append(
            cohen_kappa(
                [left[index] for index in indices],
                [right[index] for index in indices],
            )
        )
    return {
        "kappa": cohen_kappa(left, right),
        "bootstrap_ci": [_percentile(values, 0.025), _percentile(values, 0.975)],
        "n": count,
    }


def _finite_number_in_range(value: Any, lower: float, upper: float) -> bool:
    return (
        isinstance(value, Real)
        and not isinstance(value, bool)
        and math.isfinite(value)
        and lower <= value <= upper
    )


def _interval_errors(
    value: Any, path: str, lower: float, upper: float
) -> List[str]:
    if not isinstance(value, (list, tuple)) or len(value) != 2:
        return ["%s must be a two-value interval" % path]
    if any(
        not _finite_number_in_range(endpoint, lower, upper)
        for endpoint in value
    ):
        return ["%s endpoints must be finite and in range" % path]
    if value[0] > value[1]:
        return ["%s endpoints must be ordered" % path]
    return []


def _metric_count_errors(value: Any, path: str, expected: int) -> List[str]:
    if not isinstance(value, int) or isinstance(value, bool):
        return ["%s must be a non-boolean integer" % path]
    if value != expected:
        return ["%s must equal unique_responses" % path]
    return []


def _classification_block_errors(
    block: Any,
    path: str,
    expected_n: int,
    *,
    enforce_f1_thresholds: bool,
) -> List[str]:
    errors: List[str] = []
    if not isinstance(block, MappingABC):
        return ["%s must be a mapping" % path]

    kappa = block.get("kappa")
    if not _finite_number_in_range(kappa, 0.0, 1.0):
        errors.append("%s.kappa must be finite and in [0, 1]" % path)
    elif kappa < MINIMUM_KAPPA:
        errors.append("%s.kappa is below %.2f" % (path, MINIMUM_KAPPA))

    macro_f1 = block.get("macro_f1")
    if not _finite_number_in_range(macro_f1, 0.0, 1.0):
        errors.append("%s.macro_f1 must be finite and in [0, 1]" % path)
    elif enforce_f1_thresholds and macro_f1 < MINIMUM_MACRO_F1:
        errors.append(
            "%s.macro_f1 is below %.2f" % (path, MINIMUM_MACRO_F1)
        )

    class_scores = block.get("per_class_f1")
    if not isinstance(class_scores, MappingABC):
        errors.append("%s.per_class_f1 must be a mapping" % path)
    elif set(class_scores) != set(ADVICE_CLASSES):
        errors.append(
            "%s.per_class_f1 must contain exactly the five locked classes"
            % path
        )
    else:
        for label in ADVICE_CLASSES:
            score = class_scores[label]
            score_path = "%s.per_class_f1.%s" % (path, label)
            if not _finite_number_in_range(score, 0.0, 1.0):
                errors.append("%s must be finite and in [0, 1]" % score_path)
            elif enforce_f1_thresholds and score < MINIMUM_CLASS_F1:
                errors.append(
                    "%s is below %.2f" % (score_path, MINIMUM_CLASS_F1)
                )

    intervals = block.get("bootstrap_ci")
    if not isinstance(intervals, MappingABC):
        errors.append("%s.bootstrap_ci must be a mapping" % path)
    else:
        errors.extend(_interval_errors(
            intervals.get("kappa"), "%s.bootstrap_ci.kappa" % path,
            -1.0, 1.0,
        ))
        errors.extend(_interval_errors(
            intervals.get("macro_f1"),
            "%s.bootstrap_ci.macro_f1" % path, 0.0, 1.0,
        ))

    errors.extend(_metric_count_errors(
        block.get("n"), "%s.n" % path, expected_n
    ))
    return errors


def _categorical_block_errors(
    block: Any, path: str, expected_n: int
) -> List[str]:
    errors: List[str] = []
    if not isinstance(block, MappingABC):
        return ["%s must be a mapping" % path]
    if not _finite_number_in_range(block.get("kappa"), -1.0, 1.0):
        errors.append("%s.kappa must be finite and in [-1, 1]" % path)
    errors.extend(_interval_errors(
        block.get("bootstrap_ci"), "%s.bootstrap_ci" % path, -1.0, 1.0
    ))
    errors.extend(_metric_count_errors(
        block.get("n"), "%s.n" % path, expected_n
    ))
    return errors


def calibration_pass_report_errors(report: Any) -> Tuple[str, ...]:
    """Return all reasons a serialized human calibration PASS is invalid.

    The validator is pure so every live entry point can apply the same locked
    schema and thresholds without trusting copied status fields.
    """

    errors: List[str] = []
    if not isinstance(report, MappingABC):
        return ("calibration report must be a mapping",)

    if report.get("verdict") != "PASS":
        errors.append("verdict must be PASS")
    if report.get("eligible_for_empirical_decision") is not True:
        errors.append("eligible_for_empirical_decision must be true")
    if report.get("data_basis") != "human":
        errors.append("data_basis must be human")
    if report.get("repair_state") != PASSED:
        errors.append("repair_state must be PASSED")
    banner = report.get("banner")
    if not isinstance(banner, str) or not banner.strip():
        errors.append("banner must be a nonblank string")
    failures = report.get("failures")
    if not isinstance(failures, (list, tuple)) or failures:
        errors.append("failures must be an empty sequence")

    unique = report.get("unique_responses")
    double_coded = report.get("double_coded_responses")
    unique_valid = isinstance(unique, int) and not isinstance(unique, bool)
    double_valid = (
        isinstance(double_coded, int) and not isinstance(double_coded, bool)
    )
    if not unique_valid or unique < MINIMUM_HUMAN_RESPONSES:
        errors.append("unique_responses must be an integer at or above 200")
    if not double_valid or double_coded < MINIMUM_HUMAN_RESPONSES:
        errors.append(
            "double_coded_responses must be an integer at or above 200"
        )
    if unique_valid and double_valid and double_coded != unique:
        errors.append("every PASS response must be double coded")

    metrics = report.get("metrics")
    if not isinstance(metrics, MappingABC):
        errors.append("metrics must be a complete mapping")
        return tuple(errors)
    expected_n = unique if unique_valid else -1

    human_human = metrics.get("human_human")
    if not isinstance(human_human, MappingABC):
        errors.append("metrics.human_human must be a mapping")
    else:
        human_class = human_human.get("advice_class")
        errors.extend(_classification_block_errors(
            human_class, "metrics.human_human.advice_class", expected_n,
            enforce_f1_thresholds=False,
        ))
        errors.extend(_categorical_block_errors(
            human_human.get("fr"), "metrics.human_human.fr", expected_n
        ))
        errors.extend(_categorical_block_errors(
            human_human.get("response_status"),
            "metrics.human_human.response_status", expected_n,
        ))
        root_kappa = metrics.get("kappa")
        human_kappa = (
            human_class.get("kappa")
            if isinstance(human_class, MappingABC) else None
        )
        if not _finite_number_in_range(root_kappa, 0.0, 1.0):
            errors.append("metrics.kappa must be finite and in [0, 1]")
        elif (
            _finite_number_in_range(human_kappa, 0.0, 1.0)
            and not math.isclose(root_kappa, human_kappa)
        ):
            errors.append("metrics.kappa must match human-human kappa")

    per_family = metrics.get("per_family")
    if not isinstance(per_family, MappingABC):
        errors.append("metrics.per_family must be a mapping")
    else:
        if set(per_family) != set(JUDGE_FAMILIES):
            errors.append(
                "metrics.per_family must contain every registered judge family"
            )
        for family in JUDGE_FAMILIES:
            if family not in per_family:
                continue
            family_path = "metrics.per_family.%s" % family
            family_metrics = per_family[family]
            errors.extend(_classification_block_errors(
                family_metrics, family_path, expected_n,
                enforce_f1_thresholds=True,
            ))
            if isinstance(family_metrics, MappingABC):
                errors.extend(_categorical_block_errors(
                    family_metrics.get("fr"), "%s.fr" % family_path,
                    expected_n,
                ))
                errors.extend(_categorical_block_errors(
                    family_metrics.get("response_status"),
                    "%s.response_status" % family_path, expected_n,
                ))

    judges = metrics.get("judges")
    if not isinstance(judges, MappingABC) or judges != per_family:
        errors.append("metrics.judges must match metrics.per_family")

    fused = metrics.get("fused")
    errors.extend(_classification_block_errors(
        fused, "metrics.fused", expected_n, enforce_f1_thresholds=True
    ))
    if isinstance(fused, MappingABC):
        errors.extend(_categorical_block_errors(
            fused.get("fr"), "metrics.fused.fr", expected_n
        ))
        errors.extend(_categorical_block_errors(
            fused.get("response_status"), "metrics.fused.response_status",
            expected_n,
        ))
    fused_classifier = metrics.get("fused_classifier")
    if (
        not isinstance(fused_classifier, MappingABC)
        or fused_classifier != fused
    ):
        errors.append("metrics.fused_classifier must match metrics.fused")

    return tuple(errors)


def advance_repair_state(current_state: str, passed: bool) -> str:
    """Authorize one repair and park the calibration after a second failure."""

    if current_state not in (INITIAL, ONE_REPAIR_AUTHORIZED, SECOND_FAIL_PARKED):
        raise ValueError("invalid calibration repair state")
    if type(passed) is not bool:
        raise TypeError("passed must be boolean")
    if current_state == SECOND_FAIL_PARKED:
        return SECOND_FAIL_PARKED
    if passed:
        return PASSED
    if current_state == INITIAL:
        return ONE_REPAIR_AUTHORIZED
    return SECOND_FAIL_PARKED


def _canonical_text_identifier(value: Any) -> Optional[str]:
    if not isinstance(value, str):
        return None
    normalized = " ".join(value.split())
    if not normalized or value != normalized:
        return None
    return normalized


def _record_id(record: Mapping[str, Any], index: int) -> str:
    value = record.get("response_id", record.get("id"))
    normalized = _canonical_text_identifier(value)
    if normalized is None:
        raise ValueError(
            "calibration record %d requires a nonblank response_id with "
            "canonical whitespace" % index
        )
    return normalized


def _group_records(records: Iterable[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    grouped: List[Dict[str, Any]] = []
    seen = set()
    for index, source in enumerate(records):
        if not isinstance(source, MappingABC):
            raise TypeError("calibration records must be mappings")
        record = deepcopy(dict(source))
        response_id = _record_id(record, index)
        if response_id in seen:
            raise ValueError("duplicate response_id: %s" % response_id)
        seen.add(response_id)
        record["response_id"] = response_id
        if "annotations" not in record:
            record["annotations"] = []
        grouped.append(record)
    return grouped


def _label(value: Mapping[str, Any]) -> Optional[str]:
    return value.get("advice_class") if value.get("advice_class") in ADVICE_CLASSES else None


def _response_text(record: Mapping[str, Any]) -> str:
    value = record.get("response_text")
    if not isinstance(value, str) or not value.strip():
        raise ValueError("every calibration record requires nonblank response_text")
    return value


def _annotation(
    value: Mapping[str, Any], response_text: str
) -> Optional[Dict[str, Any]]:
    if not isinstance(value, MappingABC):
        return None
    label = _label(value)
    fr = value.get("fr")
    status = value.get("response_status")
    annotator_id = value.get("annotator_id")
    canonical_annotator_id = _canonical_text_identifier(annotator_id)
    spans = value.get("evidence_spans")
    if (
        label is None
        or type(fr) is not bool
        or status not in RESPONSE_STATUSES
        or canonical_annotator_id is None
        or not isinstance(spans, (list, tuple))
        or not spans
        or any(
            not isinstance(span, str)
            or not span.strip()
            or span not in response_text
            for span in spans
        )
    ):
        return None
    return {
        "annotator_id": canonical_annotator_id,
        "advice_class": label,
        "fr": fr,
        "response_status": status,
        "evidence_spans": list(spans),
    }


def _decision(value: Any) -> Optional[Dict[str, Any]]:
    if not isinstance(value, MappingABC):
        return None
    label = _label(value)
    fr = value.get("fr")
    status = value.get("response_status")
    if label is None or type(fr) is not bool or status not in RESPONSE_STATUSES:
        return None
    return {"advice_class": label, "fr": fr, "response_status": status}


def _prediction(value: Any, response_text: str) -> Optional[Dict[str, Any]]:
    try:
        return validate_judge_output(value, response_text)
    except (TypeError, ValueError):
        return None


def _consensus(
    record: Mapping[str, Any], annotations: Sequence[Mapping[str, Any]], synthetic: bool
) -> Optional[Dict[str, Any]]:
    value = record.get("consensus", record.get("adjudication"))
    if isinstance(value, MappingABC):
        normalized = _decision(value)
        if normalized is not None:
            disagreement = len(annotations) >= 2 and any(
                annotations[0][field] != annotations[1][field]
                for field in ("advice_class", "fr", "response_status")
            )
            if disagreement and value.get("adjudicated") is not True:
                return None
            normalized["adjudicated"] = value.get("adjudicated") is True
            return normalized
    if synthetic and record.get("fixture_intended_class") in ADVICE_CLASSES:
        if annotations:
            return {
                "advice_class": record["fixture_intended_class"],
                "fr": annotations[0]["fr"],
                "response_status": annotations[0]["response_status"],
                "adjudicated": False,
            }
    if len(annotations) >= 2 and all(
        annotations[0][field] == annotations[1][field]
        for field in ("advice_class", "fr", "response_status")
    ):
        return {
            key: annotations[0][key]
            for key in ("advice_class", "fr", "response_status")
        } | {"adjudicated": False}
    return None


def _contains_synthetic_provenance(
    value: Any, *, provenance_context: bool = False
) -> bool:
    if isinstance(value, MappingABC):
        for key, child in value.items():
            normalized_key = (
                str(key).strip().lower().replace("-", "_").replace(" ", "_")
            )
            if normalized_key in _CONTENT_VALUE_KEYS:
                continue
            if (
                normalized_key in _SYNTHETIC_KEY_MARKERS
                or "synthetic" in normalized_key
                or "fixture" in normalized_key
            ):
                return True
            child_context = (
                provenance_context
                or normalized_key in _PROVENANCE_CONTAINER_KEYS
            )
            if (
                isinstance(child, str)
                and (
                    child_context
                    or normalized_key in _SYNTHETIC_VALUE_KEYS
                )
            ):
                normalized_value = " ".join(child.lower().split())
                if "synthetic" in normalized_value or "fixture" in normalized_value:
                    return True
            if _contains_synthetic_provenance(
                child, provenance_context=child_context
            ):
                return True
    elif isinstance(value, (list, tuple)):
        return any(
            _contains_synthetic_provenance(
                child, provenance_context=provenance_context
            )
            for child in value
        )
    elif isinstance(value, str) and provenance_context:
        normalized_value = " ".join(value.lower().split())
        return "synthetic" in normalized_value or "fixture" in normalized_value
    return False


def _basis(
    records: Sequence[Mapping[str, Any]], mode: Optional[str], data_basis: Optional[str]
) -> str:
    if mode == "synthetic" or data_basis == "synthetic":
        return "synthetic"
    if any(_contains_synthetic_provenance(record) for record in records):
        return "synthetic"
    if mode is not None and mode not in _HUMAN_MODES:
        return "unknown"
    if data_basis is not None and data_basis != "human":
        return "unknown"
    if (
        all(record.get("mode") in _HUMAN_MODES for record in records)
        and all(record.get("data_basis") == "human" for record in records)
    ):
        return "human"
    return "unknown"


def _empty_result(
    *, verdict: str, unique: int, double_coded: int, data_basis: str,
    failures: Sequence[str], repair_state: str = INITIAL,
) -> CalibrationResult:
    return CalibrationResult(
        metrics={}, eligible_for_empirical_decision=False, verdict=verdict,
        unique_responses=unique, double_coded_responses=double_coded,
        repair_state=repair_state,
        banner="CALIBRATION GATE NOT PASSED: %s." % verdict,
        failures=tuple(failures), data_basis=data_basis,
    )


def evaluate_calibration(
    records: Iterable[Mapping[str, Any]],
    *,
    mode: Optional[str] = None,
    data_basis: Optional[str] = None,
    repair_state: str = INITIAL,
    prior_failures: Optional[int] = None,
    attempt: Optional[int] = None,
    bootstrap_samples: int = 400,
    seed: int = 20260709,
) -> CalibrationResult:
    """Evaluate calibration while making synthetic and incomplete data fail closed."""

    if isinstance(records, (str, bytes, bytearray)) or not isinstance(
        records, IterableABC
    ):
        raise TypeError("records must be an iterable of mappings")
    if (
        not isinstance(bootstrap_samples, int)
        or isinstance(bootstrap_samples, bool)
        or bootstrap_samples < 1
    ):
        raise ValueError("bootstrap_samples must be a positive integer")
    if not isinstance(seed, int) or isinstance(seed, bool) or seed < 0:
        raise ValueError("seed must be a nonnegative integer")
    if prior_failures is not None and attempt is not None:
        raise ValueError("repair state aliases are mutually exclusive")
    if (prior_failures is not None or attempt is not None) and repair_state != INITIAL:
        raise ValueError("repair state cannot be reset by an alias")
    if prior_failures is not None:
        if not isinstance(prior_failures, int) or isinstance(prior_failures, bool):
            raise TypeError("prior_failures must be an integer")
        if prior_failures < 0:
            raise ValueError("prior_failures must be nonnegative")
        repair_state = (
            INITIAL if prior_failures == 0 else
            ONE_REPAIR_AUTHORIZED if prior_failures == 1 else
            SECOND_FAIL_PARKED
        )
    if attempt is not None:
        if not isinstance(attempt, int) or isinstance(attempt, bool):
            raise TypeError("calibration attempt must be an integer")
        if attempt not in (1, 2):
            raise ValueError("calibration attempt must be 1 or 2")
        repair_state = INITIAL if attempt == 1 else ONE_REPAIR_AUTHORIZED
    if repair_state not in (INITIAL, ONE_REPAIR_AUTHORIZED, SECOND_FAIL_PARKED):
        raise ValueError("invalid calibration repair state")

    raw = _group_records(list(records))
    if not raw:
        return _empty_result(
            verdict="NO_CALIBRATION_RECORDS", unique=0, double_coded=0,
            data_basis="unknown", failures=("no records",),
        )
    basis = _basis(raw, mode, data_basis)
    synthetic = basis == "synthetic"
    normalized = []
    double_coded = 0
    invalid_annotations = []
    incomplete_annotations = []
    incomplete_consensus = []
    incomplete_judges = []
    for record in raw:
        response_text = _response_text(record)
        source_annotations = record.get(
            "annotations", record.get("human_annotations", [])
        )
        if isinstance(source_annotations, MappingABC):
            source_annotations = list(source_annotations.values())
        if not isinstance(source_annotations, list):
            source_annotations = []
        annotations = []
        malformed = False
        for source in source_annotations:
            annotation = _annotation(source, response_text)
            if annotation is None:
                malformed = True
            else:
                annotations.append(annotation)
        annotator_ids = [item["annotator_id"] for item in annotations]
        if len(annotator_ids) != len(set(annotator_ids)):
            malformed = True
        if malformed:
            invalid_annotations.append(record["response_id"])
        if len(annotations) >= MINIMUM_ANNOTATORS_PER_RESPONSE:
            double_coded += 1
        else:
            incomplete_annotations.append(record["response_id"])
        consensus = _consensus(record, annotations, synthetic)
        if consensus is None:
            incomplete_consensus.append(record["response_id"])
        judge_source = record.get("judge_predictions", record.get("judges", {}))
        judges = {}
        if isinstance(judge_source, MappingABC):
            judges = {
                family: prediction
                for family in JUDGE_FAMILIES
                if (
                    prediction := _prediction(
                        judge_source.get(family), response_text
                    )
                ) is not None
            }
        fused = _prediction(
            record.get(
                "fused_prediction",
                record.get("fused", record.get("classifier_prediction")),
            ),
            response_text,
        )
        if set(judges) != set(JUDGE_FAMILIES) or fused is None:
            incomplete_judges.append(record["response_id"])
        normalized.append({
            "annotations": annotations,
            "consensus": consensus,
            "judges": judges,
            "fused": fused,
        })

    unique = len(raw)
    if basis == "unknown":
        return _empty_result(
            verdict="INVALID_EVIDENCE_BASIS", unique=unique,
            double_coded=double_coded, data_basis=basis,
            failures=("records are not explicitly human or synthetic",),
        )
    if invalid_annotations:
        return _empty_result(
            verdict="INVALID_HUMAN_ANNOTATIONS",
            unique=unique,
            double_coded=double_coded,
            data_basis=basis,
            failures=("annotation rows are malformed or reuse an annotator id",),
            repair_state=repair_state,
        )
    if incomplete_annotations:
        return _empty_result(
            verdict="INSUFFICIENT_DOUBLE_CODING", unique=unique,
            double_coded=double_coded, data_basis=basis,
            failures=("responses without two independent codes",),
        )
    if incomplete_consensus:
        return _empty_result(
            verdict="INCOMPLETE_ADJUDICATION", unique=unique,
            double_coded=double_coded, data_basis=basis,
            failures=("disagreements lack adjudicated consensus",),
        )
    if incomplete_judges:
        return _empty_result(
            verdict="INCOMPLETE_JUDGE_OUTPUTS", unique=unique,
            double_coded=double_coded, data_basis=basis,
            failures=("both judge families and fused predictions are required",),
        )

    first_labels = [row["annotations"][0]["advice_class"] for row in normalized]
    second_labels = [row["annotations"][1]["advice_class"] for row in normalized]
    first_fr = [row["annotations"][0]["fr"] for row in normalized]
    second_fr = [row["annotations"][1]["fr"] for row in normalized]
    first_status = [row["annotations"][0]["response_status"] for row in normalized]
    second_status = [row["annotations"][1]["response_status"] for row in normalized]
    consensus_labels = [row["consensus"]["advice_class"] for row in normalized]
    consensus_fr = [row["consensus"]["fr"] for row in normalized]
    consensus_status = [row["consensus"]["response_status"] for row in normalized]

    human_class = classification_metrics(
        first_labels, second_labels, bootstrap_samples=bootstrap_samples,
        seed=_metric_seed(seed, "human-human-class"),
    )
    human_human = {
        "advice_class": human_class,
        "fr": _categorical_kappa_metrics(
            first_fr, second_fr, samples=bootstrap_samples,
            seed=_metric_seed(seed, "human-human-fr"),
        ),
        "response_status": _categorical_kappa_metrics(
            first_status, second_status, samples=bootstrap_samples,
            seed=_metric_seed(seed, "human-human-status"),
        ),
    }
    per_family = {}
    for family in JUDGE_FAMILIES:
        predictions = [row["judges"][family]["advice_class"] for row in normalized]
        family_metrics = classification_metrics(
            consensus_labels, predictions, bootstrap_samples=bootstrap_samples,
            seed=_metric_seed(seed, family),
        )
        family_metrics["fr"] = _categorical_kappa_metrics(
            consensus_fr, [row["judges"][family]["fr"] for row in normalized],
            samples=bootstrap_samples, seed=_metric_seed(seed, family + "-fr"),
        )
        family_metrics["response_status"] = _categorical_kappa_metrics(
            consensus_status,
            [row["judges"][family]["response_status"] for row in normalized],
            samples=bootstrap_samples,
            seed=_metric_seed(seed, family + "-status"),
        )
        per_family[family] = family_metrics
    fused = classification_metrics(
        consensus_labels,
        [row["fused"]["advice_class"] for row in normalized],
        bootstrap_samples=bootstrap_samples,
        seed=_metric_seed(seed, "fused"),
    )
    fused["fr"] = _categorical_kappa_metrics(
        consensus_fr, [row["fused"]["fr"] for row in normalized],
        samples=bootstrap_samples, seed=_metric_seed(seed, "fused-fr"),
    )
    fused["response_status"] = _categorical_kappa_metrics(
        consensus_status,
        [row["fused"]["response_status"] for row in normalized],
        samples=bootstrap_samples, seed=_metric_seed(seed, "fused-status"),
    )
    metrics = {
        "kappa": human_class["kappa"],
        "human_human": human_human,
        "per_family": per_family,
        "judges": deepcopy(per_family),
        "fused": fused,
        "fused_classifier": deepcopy(fused),
    }

    if synthetic:
        return CalibrationResult(
            metrics=metrics, eligible_for_empirical_decision=False,
            verdict="NOT_RUN_HUMAN", unique_responses=unique,
            double_coded_responses=double_coded, repair_state="NOT_APPLICABLE",
            banner=SYNTHETIC_BANNER, failures=("synthetic data basis",),
            data_basis="synthetic",
        )
    if unique < MINIMUM_HUMAN_RESPONSES:
        return CalibrationResult(
            metrics=metrics, eligible_for_empirical_decision=False,
            verdict="INSUFFICIENT_HUMAN_LABELS", unique_responses=unique,
            double_coded_responses=double_coded, repair_state=repair_state,
            banner=(
                "HUMAN CALIBRATION NOT RUN TO THRESHOLD: fewer than 200 unique "
                "double-coded responses."
            ), failures=("human response count below 200",), data_basis="human",
        )

    failures = []
    if repair_state == SECOND_FAIL_PARKED:
        failures.append("calibration is parked after the second failed attempt")
    if human_class["kappa"] < MINIMUM_KAPPA:
        failures.append("human-human kappa below %.2f" % MINIMUM_KAPPA)
    for name, values in list(per_family.items()) + [("fused", fused)]:
        if values["kappa"] < MINIMUM_KAPPA:
            failures.append("%s kappa below %.2f" % (name, MINIMUM_KAPPA))
        if values["macro_f1"] < MINIMUM_MACRO_F1:
            failures.append("%s macro-F1 below %.2f" % (name, MINIMUM_MACRO_F1))
        low_classes = [
            label for label, score in values["per_class_f1"].items()
            if score < MINIMUM_CLASS_F1
        ]
        if low_classes:
            failures.append("%s class F1 below %.2f: %s" % (
                name, MINIMUM_CLASS_F1, ", ".join(low_classes),
            ))

    passed = not failures
    next_state = advance_repair_state(repair_state, passed)
    if passed:
        return CalibrationResult(
            metrics=metrics, eligible_for_empirical_decision=True,
            verdict="PASS", unique_responses=unique,
            double_coded_responses=double_coded, repair_state=next_state,
            banner="HUMAN CALIBRATION GATE PASSED on eligible human evidence.",
            failures=(), data_basis="human",
        )
    verdict = (
        "REPAIR_AUTHORIZED"
        if next_state == ONE_REPAIR_AUTHORIZED else "SECOND_FAIL_PARKED"
    )
    return CalibrationResult(
        metrics=metrics, eligible_for_empirical_decision=False,
        verdict=verdict, unique_responses=unique,
        double_coded_responses=double_coded, repair_state=next_state,
        banner="HUMAN CALIBRATION GATE FAILED: %s." % verdict,
        failures=tuple(failures), data_basis="human",
    )


__all__ = [
    "CalibrationResult", "INITIAL", "MINIMUM_ANNOTATORS_PER_RESPONSE",
    "MINIMUM_CLASS_F1", "MINIMUM_HUMAN_RESPONSES", "MINIMUM_KAPPA",
    "MINIMUM_MACRO_F1", "ONE_REPAIR_AUTHORIZED", "PASSED",
    "SECOND_FAIL_PARKED", "SYNTHETIC_BANNER", "advance_repair_state",
    "calibration_pass_report_errors", "classification_metrics", "cohen_kappa",
    "evaluate_calibration", "per_class_f1",
]
