from copy import deepcopy

import pytest

from calibration.status import (
    STATUS_PATH,
    build_evidence_status,
    canonical_status_bytes,
    load_evidence_status,
    validate_evidence_status,
)


_NOT_RUN_EVIDENCE = {
    "casuistry_panel",
    "edge_judge",
    "human_baseline",
    "professional_baseline",
    "contested_distribution",
    "real_10pct_finetune_probe",
    "official_multiseed_model_run",
}


def test_canonical_evidence_status_is_byte_frozen_and_every_gate_is_not_run():
    status = load_evidence_status()

    assert status == build_evidence_status()
    assert STATUS_PATH.read_bytes() == canonical_status_bytes()
    assert status["overall_status"] == "NOT_RUN"
    assert status["fixture_promotion_forbidden"] is True
    assert status["synthetic_input_promotion_forbidden"] is True
    assert status["eligibility"] == {
        "empirical": False,
        "official": False,
        "publication": False,
    }
    assert set(status["evidence"]) == _NOT_RUN_EVIDENCE
    assert {item["status"] for item in status["evidence"].values()} == {"NOT_RUN"}
    assert all(item["evidence"] is None for item in status["evidence"].values())
    assert all(item["fixture_eligible"] is False for item in status["evidence"].values())
    for item in status["evidence"].values():
        assert item["empirical_eligible"] is False
        assert item["official_eligible"] is False
        assert item["publication_eligible"] is False

    panel = status["evidence"]["casuistry_panel"]
    assert panel["minimum_panelists"] == 5
    assert panel["required_corpora"] == [
        "rabbinic",
        "catechetical",
        "legal_necessity",
    ]
    assert panel["all_required_corpora"] is True
    assert panel["single_tradition_majority_forbidden"] is True
    assert panel["kappa_gate"] == 0.8


@pytest.mark.parametrize("evidence_name", sorted(_NOT_RUN_EVIDENCE))
def test_status_validator_rejects_false_or_fixture_backed_promotion(evidence_name):
    forged = deepcopy(build_evidence_status())
    forged["overall_status"] = "COMPLETE"
    forged["evidence"][evidence_name]["status"] = "PASS"
    forged["evidence"][evidence_name]["evidence"] = {
        "source": "synthetic_fixture"
    }
    forged["evidence"][evidence_name]["fixture_eligible"] = True

    with pytest.raises(ValueError, match="NOT_RUN|promotion|fixture"):
        validate_evidence_status(forged)


@pytest.mark.parametrize(
    ("field", "value"),
    (
        ("minimum_panelists", 4),
        ("required_corpora", ["rabbinic", "catechetical"]),
        ("all_required_corpora", False),
        ("single_tradition_majority_forbidden", False),
        ("kappa_gate", 0.79),
    ),
)
def test_status_validator_rejects_weakened_casuistry_panel_gate(field, value):
    forged = deepcopy(build_evidence_status())
    forged["evidence"]["casuistry_panel"][field] = value
    with pytest.raises(ValueError, match="casuistry|frozen|NOT_RUN"):
        validate_evidence_status(forged)
