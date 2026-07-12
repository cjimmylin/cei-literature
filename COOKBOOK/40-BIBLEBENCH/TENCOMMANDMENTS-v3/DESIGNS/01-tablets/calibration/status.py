"""Immutable evidence-status contract for the credential-free TABLETS P1 bank."""

import json
from pathlib import Path


STATUS_PATH = Path(__file__).with_name("evidence-status.json")


def _not_run_entry():
    return {
        "status": "NOT_RUN",
        "evidence": None,
        "fixture_eligible": False,
        "empirical_eligible": False,
        "official_eligible": False,
        "publication_eligible": False,
    }


def build_evidence_status():
    """Return a fresh copy of the only valid TABLETS P1 evidence status."""
    panel = {
        **_not_run_entry(),
        "minimum_panelists": 5,
        "required_corpora": [
            "rabbinic",
            "catechetical",
            "legal_necessity",
        ],
        "all_required_corpora": True,
        "single_tradition_majority_forbidden": True,
        "kappa_gate": 0.8,
    }
    evidence = {
        "casuistry_panel": panel,
        "edge_judge": _not_run_entry(),
        "human_baseline": _not_run_entry(),
        "professional_baseline": _not_run_entry(),
        "contested_distribution": _not_run_entry(),
        "real_10pct_finetune_probe": _not_run_entry(),
        "official_multiseed_model_run": _not_run_entry(),
    }
    return {
        "schema_version": "tablets-evidence-status.v1",
        "artifact_schema_version": "tablets.p1.v1",
        "benchmark": "TABLETS",
        "overall_status": "NOT_RUN",
        "fixture_promotion_forbidden": True,
        "synthetic_input_promotion_forbidden": True,
        "eligibility": {
            "empirical": False,
            "official": False,
            "publication": False,
        },
        "evidence": evidence,
    }


def canonical_status_bytes():
    """Serialize the frozen status with deterministic keys and whitespace."""
    return (
        json.dumps(
            build_evidence_status(),
            sort_keys=True,
            indent=2,
            ensure_ascii=False,
        )
        + "\n"
    ).encode("utf-8")


def validate_evidence_status(status):
    """Reject any evidence, fixture promotion, relaxed gate, or schema drift."""
    if type(status) is not dict:
        raise ValueError("TABLETS evidence status must be an object")
    if status != build_evidence_status():
        raise ValueError(
            "TABLETS P1 evidence status is frozen NOT_RUN; evidence, fixture or "
            "synthetic promotion, and weakened casuistry gates are forbidden"
        )
    return True


def load_evidence_status(path=STATUS_PATH):
    """Load the canonical disk artifact and require exact deterministic bytes."""
    path = Path(path)
    payload = path.read_bytes()
    if payload != canonical_status_bytes():
        raise ValueError("TABLETS evidence-status artifact has deterministic byte drift")
    try:
        status = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValueError("TABLETS evidence-status artifact is not canonical JSON") from error
    validate_evidence_status(status)
    return status


__all__ = [
    "STATUS_PATH",
    "build_evidence_status",
    "canonical_status_bytes",
    "load_evidence_status",
    "validate_evidence_status",
]
