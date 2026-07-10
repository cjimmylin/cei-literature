"""Deterministic synthetic fixtures for plumbing checks, never gate evidence."""

import random
from typing import Any, Dict, List

from zerosum_common import ADVICE_CLASSES
from scoring.judge_prompts import JUDGE_FAMILIES


SYNTHETIC_REPORT_BANNER = (
    "SYNTHETIC PLUMBING ONLY — no classifier gate was run and these records "
    "are ineligible for every empirical decision."
)


def _prediction(label: str, fr: bool, evidence: str) -> Dict[str, Any]:
    return {
        "advice_class": label,
        "fr": fr,
        "response_status": "answered",
        "evidence_spans": [evidence],
        "confidence": 0.99,
    }


def generate_synthetic_fixtures(
    count: int = 250, seed: int = 20260709
) -> List[Dict[str, Any]]:
    """Return at least 250 balanced, perfect, explicitly synthetic fixtures."""

    if not isinstance(count, int) or isinstance(count, bool) or count < 250:
        raise ValueError("synthetic calibration fixtures require count >= 250")
    if not isinstance(seed, int) or isinstance(seed, bool) or seed < 0:
        raise ValueError("seed must be a nonnegative integer")
    labels = [ADVICE_CLASSES[index % len(ADVICE_CLASSES)] for index in range(count)]
    rng = random.Random(seed)
    rng.shuffle(labels)
    fixtures = []
    for index, label in enumerate(labels):
        fr = index % 2 == 0
        evidence = "synthetic response evidence %04d" % index
        annotations = [
            {
                "annotator_id": "fixture-coder-a",
                "annotation_basis": "synthetic_fixture",
                "advice_class": label,
                "fr": fr,
                "response_status": "answered",
                "evidence_spans": [evidence],
            },
            {
                "annotator_id": "fixture-coder-b",
                "annotation_basis": "synthetic_fixture",
                "advice_class": label,
                "fr": fr,
                "response_status": "answered",
                "evidence_spans": [evidence],
            },
        ]
        fixtures.append({
            "response_id": "synthetic-%d-%04d" % (seed, index),
            "mode": "synthetic",
            "data_basis": "synthetic",
            "report_banner": SYNTHETIC_REPORT_BANNER,
            "response_text": evidence,
            "fixture_intended_class": label,
            "annotations": annotations,
            "consensus": {
                "advice_class": label,
                "fr": fr,
                "response_status": "answered",
                "adjudicated": False,
                "basis": "synthetic_fixture",
            },
            "judge_predictions": {
                family: _prediction(label, fr, evidence)
                for family in JUDGE_FAMILIES
            },
            "fused_prediction": _prediction(label, fr, evidence),
        })
    return fixtures


def perfect_synthetic_fixture(
    count: int = 250, seed: int = 20260709
) -> List[Dict[str, Any]]:
    """Compatibility alias emphasizing that perfection is plumbing-only."""

    return generate_synthetic_fixtures(count=count, seed=seed)


__all__ = [
    "SYNTHETIC_REPORT_BANNER", "generate_synthetic_fixtures",
    "perfect_synthetic_fixture",
]
