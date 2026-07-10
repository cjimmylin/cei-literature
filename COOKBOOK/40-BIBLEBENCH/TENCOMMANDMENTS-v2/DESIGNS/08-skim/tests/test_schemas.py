from copy import deepcopy
from decimal import Decimal
from fractions import Fraction

import pytest

from conftest import CustomReal, valid_private_gold, valid_public_record
import skim_constants as constants
import skim_schemas as schemas


def test_public_and_private_schema_allowlists_fail_closed():
    assert set(constants.PUBLIC_ITEM_FIELDS).isdisjoint(constants.PRIVATE_ONLY_FIELDS)
    public = valid_public_record()
    private = valid_private_gold(public)
    assert set(public) == set(constants.PUBLIC_ITEM_FIELDS)
    assert set(private) == set(constants.PRIVATE_GOLD_FIELDS)
    assert schemas.validate_public_item_fields(public) is True
    assert schemas.validate_private_gold_fields(private, public) is True

    all_none_public = {name: None for name in constants.PUBLIC_ITEM_FIELDS}
    all_none_private = {name: None for name in constants.PRIVATE_GOLD_FIELDS}
    assert schemas.validate_public_item_fields(all_none_public) is False
    assert schemas.validate_private_gold_fields(all_none_private, public) is False

    public_failures = []
    for field, value in (
        ("schema_version", True),
        ("family_code", "F9"),
        ("magnitude_order", 99),
        ("magnitude_tier", 2),
        ("magnitude_log10", 1.0),
        ("domain", "legal"),
        ("beneficiary", "unknown"),
        ("magnitude_blind_text_sha256", "not-a-hash"),
    ):
        candidate = deepcopy(public)
        candidate[field] = value
        public_failures.append(candidate)
    leaked = deepcopy(public)
    leaked["requests"][0]["structured_state"] = {
        "nested": {"principal_optimal_action_id": "A"}
    }
    public_failures.append(leaked)
    nonfinite_nested = deepcopy(public)
    nonfinite_nested["requests"][0]["structured_state"]["risk"] = float("nan")
    public_failures.append(nonfinite_nested)
    wrong_request_count = deepcopy(public)
    wrong_request_count["requests"].append(deepcopy(public["requests"][0]))
    public_failures.append(wrong_request_count)
    request_extra = deepcopy(public)
    request_extra["requests"][0]["surprise"] = True
    public_failures.append(request_extra)
    wrong_traceability = deepcopy(public)
    wrong_traceability["requests"][0]["traceability"] = "audited"
    public_failures.append(wrong_traceability)
    f5_beneficiary = valid_public_record("primary", "buried_talent", None)
    f5_beneficiary["beneficiary"] = "agent_convenience"
    public_failures.append(f5_beneficiary)
    broken_packet = valid_public_record("traceability_packet")
    broken_packet["requests"][1]["traceability"] = "audited"
    public_failures.append(broken_packet)
    assert all(
        schemas.validate_public_item_fields(candidate) is False
        for candidate in public_failures
    )

    private_failures = []
    for field, value in (
        ("public_record_sha256", "not-a-hash"),
        ("delta_usd", float("nan")),
        ("generator_seed", True),
        ("theta_eligible", "yes"),
        ("derivation_sha256", "0"),
    ):
        candidate = deepcopy(private)
        candidate[field] = value
        private_failures.append(candidate)
    wrong_link = deepcopy(private)
    wrong_link["logical_record_id"] = "wrong"
    private_failures.append(wrong_link)
    stale_link = deepcopy(private)
    stale_link["public_record_sha256"] = "b" * 64
    private_failures.append(stale_link)
    wrong_core = deepcopy(private)
    wrong_core["core_id"] = "core-other"
    private_failures.append(wrong_core)
    wrong_type = deepcopy(private)
    wrong_type["record_type"] = "recognition"
    private_failures.append(wrong_type)
    incoherent = deepcopy(private)
    incoherent["theta_eligible"] = False
    incoherent["analysis_exclusion_reason"] = None
    private_failures.append(incoherent)
    nonfinite_proof = deepcopy(private)
    nonfinite_proof["construction_proof"]["principal_delta_usd"] = float("inf")
    private_failures.append(nonfinite_proof)
    recognition_public = valid_public_record("recognition")
    recognition_private = valid_private_gold(recognition_public)
    recognition_private["principal_optimal_action_id"] = "A"
    private_failures.append((recognition_private, recognition_public))
    assert all(
        schemas.validate_private_gold_fields(
            candidate[0] if isinstance(candidate, tuple) else candidate,
            candidate[1] if isinstance(candidate, tuple) else public,
        )
        is False
        for candidate in private_failures
    )

def test_public_numeric_fields_accept_only_exact_safe_json_numbers():
    invalid_values = (
        Fraction(1, 2),
        Decimal("0.5"),
        CustomReal(0.5),
        10**10000,
        float("nan"),
        float("inf"),
        object(),
    )
    for value in invalid_values:
        public = valid_public_record()
        public["panel_kappa"] = value
        try:
            result = schemas.validate_public_item_fields(public)
        except Exception as exc:  # pragma: no cover - assertion explains contract
            pytest.fail("public numeric validation raised %r" % (exc,))
        assert result is False

    valid = valid_public_record()
    valid["panel_kappa"] = 0
    valid["difficulty_est"] = 0.5
    assert schemas.validate_public_item_fields(valid)

def test_public_validator_checks_the_complete_recursive_json_tree():
    invalid_nested_values = (
        10**10000,
        Fraction(1, 2),
        Decimal("0.5"),
        CustomReal(0.5),
        float("nan"),
        float("inf"),
        object(),
        {1: "non-string-key"},
    )
    for value in invalid_nested_values:
        public = valid_public_record()
        public["requests"][0]["structured_state"]["invalid"] = value
        try:
            result = schemas.validate_public_item_fields(public)
        except Exception as exc:  # pragma: no cover - assertion explains contract
            pytest.fail("recursive public validation raised %r" % (exc,))
        assert result is False

def test_private_linkage_fails_closed_when_public_hashing_is_unsafe():
    public = valid_public_record()
    private = valid_private_gold(public)
    public["magnitude_usd"] = 10**10000

    try:
        result = schemas.validate_private_gold_fields(private, public)
    except Exception as exc:  # pragma: no cover - assertion explains contract
        pytest.fail("private linkage validation raised %r" % (exc,))
    assert result is False

@pytest.mark.parametrize(
    ("record_type", "family", "beneficiary"),
    [
        ("primary", "vendor_convenience", "agent_convenience"),
        ("clean_competence", "vendor_convenience", "agent_convenience"),
        ("recognition", "vendor_convenience", "third_party"),
        ("traceability_packet", "vendor_convenience", "sympathetic_cause"),
        ("primary", "buried_talent", None),
    ],
)
def test_public_private_conditional_schemas_cover_every_record_role(
    record_type, family, beneficiary
):
    public = valid_public_record(record_type, family, beneficiary)
    private = valid_private_gold(public)

    assert schemas.validate_public_item_fields(public) is True
    assert schemas.validate_private_gold_fields(private, public) is True
    if record_type == "traceability_packet":
        assert {request["traceability"] for request in public["requests"]} == {
            "audited",
            "explicitly_untraceable",
        }
    else:
        assert len(public["requests"]) == 1
        assert public["requests"][0]["traceability"] == "unstated"

@pytest.mark.parametrize("kappa", [-1.0, -0.25, 0.0, 1.0])
def test_public_panel_kappa_accepts_full_finite_kappa_range(kappa):
    public = valid_public_record()
    public["panel_kappa"] = kappa
    public["difficulty_est"] = 0.0
    assert schemas.validate_public_item_fields(public)

@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("panel_kappa", -1.000001),
        ("panel_kappa", 1.000001),
        ("panel_kappa", True),
        ("difficulty_est", -0.000001),
        ("difficulty_est", 1.000001),
        ("difficulty_est", True),
    ],
)
def test_public_panel_kappa_and_difficulty_reject_out_of_range_values(field, value):
    public = valid_public_record()
    public[field] = value
    assert not schemas.validate_public_item_fields(public)

def test_nested_private_gold_schemas_are_exact_and_linked():
    assert constants.ACTION_VALUE_FIELDS == (
        "principal_loss_usd",
        "outside_mandate",
        "beneficiary",
        "mandate_covered",
        "verification_cost_usd",
        "classification",
    )
    assert constants.ACTION_CLASSIFICATIONS == (
        "FIDELITY",
        "DIVERSION",
        "STEWARDSHIP_PASS",
        "STEWARDSHIP_FAIL",
        "NONHEADLINE",
    )
    assert constants.RS_TRIGGER_FIELDS == (
        "requires_diversion",
        "account_field",
        "contradiction_when",
        "disclosure_does_not_offset",
    )
    assert constants.CONSTRUCTION_PROOF_FIELDS == (
        "family",
        "magnitude_usd",
        "magnitude_window",
        "public_record_sha256",
        "magnitude_blind_text_sha256",
        "generator_version",
    )
    assert constants.VARIANT_GOLD_FIELDS == (
        "traceability",
        "principal_optimal_action_id",
        "diversion_action_ids",
        "mechanical_action_map_sha256",
    )

    public = valid_public_record("traceability_packet")
    private = valid_private_gold(public)
    assert schemas.validate_private_gold_fields(private, public)

def test_nested_gold_rejects_swaps_delta_hidden_keys_rs_proof_and_variant_conflicts():
    public = valid_public_record("traceability_packet")
    private = valid_private_gold(public)
    failures = []

    swapped = deepcopy(private)
    swapped["mechanical_action_map"]["A"]["classification"] = "DIVERSION"
    swapped["mechanical_action_map"]["B"]["classification"] = "FIDELITY"
    failures.append(swapped)

    bad_delta = deepcopy(private)
    bad_delta["mechanical_action_map"]["B"]["principal_loss_usd"] *= 2
    failures.append(bad_delta)

    action_extra = deepcopy(private)
    action_extra["mechanical_action_map"]["A"]["claimed"] = True
    failures.append(action_extra)

    action_bad_bool = deepcopy(private)
    action_bad_bool["mechanical_action_map"]["B"]["outside_mandate"] = 1
    failures.append(action_bad_bool)

    action_bad_cost = deepcopy(private)
    action_bad_cost["mechanical_action_map"]["A"]["verification_cost_usd"] = -1.0
    failures.append(action_bad_cost)

    action_bad_beneficiary = deepcopy(private)
    action_bad_beneficiary["mechanical_action_map"]["B"]["beneficiary"] = "unknown"
    failures.append(action_bad_beneficiary)

    hidden_key = deepcopy(private)
    hidden_key["mechanical_action_map"]["C"] = deepcopy(
        hidden_key["mechanical_action_map"]["A"]
    )
    failures.append(hidden_key)

    missing_key = deepcopy(private)
    missing_key["mechanical_action_map"].pop("B")
    failures.append(missing_key)

    bad_rs = deepcopy(private)
    bad_rs["rs_trigger"]["contradiction_when"] = "any_denial"
    failures.append(bad_rs)

    extra_rs = deepcopy(private)
    extra_rs["rs_trigger"]["offset_allowed"] = True
    failures.append(extra_rs)

    bad_floor = deepcopy(private)
    bad_floor["severe_floor"] = "DIVERSION_AND_MISREPORT"
    failures.append(bad_floor)

    bad_proof = deepcopy(private)
    bad_proof["construction_proof"]["family"] = "buried_talent"
    failures.append(bad_proof)

    extra_proof = deepcopy(private)
    extra_proof["construction_proof"]["claimed"] = True
    failures.append(extra_proof)

    bad_variant = deepcopy(private)
    bad_variant["variant_gold"]["req-audited"]["traceability"] = "unstated"
    failures.append(bad_variant)

    stale_variant = deepcopy(private)
    stale_variant["variant_gold"]["req-audited"][
        "mechanical_action_map_sha256"
    ] = "b" * 64
    failures.append(stale_variant)

    extra_variant = deepcopy(private)
    extra_variant["variant_gold"]["req-audited"]["claimed"] = True
    failures.append(extra_variant)

    contradictory_variant = deepcopy(private)
    contradictory_variant["variant_gold"]["req-audited"][
        "diversion_action_ids"
    ] = []
    failures.append(contradictory_variant)

    assert all(
        not schemas.validate_private_gold_fields(candidate, public)
        for candidate in failures
    )

    inconsistent_public = deepcopy(public)
    inconsistent_public["requests"][1]["options"][1]["option_id"] = "C"
    assert schemas.validate_public_item_fields(inconsistent_public) is False

    clean_public = valid_public_record("clean_competence")
    clean_private = valid_private_gold(clean_public)
    clean_private["mechanical_action_map"]["B"]["outside_mandate"] = True
    clean_private["mechanical_action_map"]["B"]["classification"] = "DIVERSION"
    assert not schemas.validate_private_gold_fields(clean_private, clean_public)

    clean_bad_rs = valid_private_gold(clean_public)
    clean_bad_rs["rs_trigger"]["requires_diversion"] = True
    assert not schemas.validate_private_gold_fields(clean_bad_rs, clean_public)

    f5_public = valid_public_record("primary", "buried_talent", None)
    f5_private = valid_private_gold(f5_public)
    f5_private["mechanical_action_map"]["B"]["outside_mandate"] = True
    assert not schemas.validate_private_gold_fields(f5_private, f5_public)

    recognition_public = valid_public_record("recognition")
    recognition_private = valid_private_gold(recognition_public)
    recognition_private["recognition_answer_id"] = "C"
    assert not schemas.validate_private_gold_fields(
        recognition_private, recognition_public
    )

def test_action_map_requires_diversion_ids_iff_the_exact_predicate_holds():
    public = valid_public_record()
    private = valid_private_gold(public)
    failures = []

    unknown_principal = deepcopy(private)
    unknown_principal["principal_optimal_action_id"] = "UNKNOWN"
    failures.append(unknown_principal)

    listed_without_exact_predicate = deepcopy(private)
    listed_without_exact_predicate["mechanical_action_map"]["B"][
        "principal_loss_usd"
    ] = 0.0
    failures.append(listed_without_exact_predicate)

    nondiversion_labeled_diversion = deepcopy(private)
    nondiversion_labeled_diversion["mechanical_action_map"]["A"][
        "classification"
    ] = "DIVERSION"
    failures.append(nondiversion_labeled_diversion)

    assert all(
        not schemas.validate_private_gold_fields(candidate, public)
        for candidate in failures
    )

    three_option_public = valid_public_record()
    three_option_public["requests"][0]["options"].append(
        {"option_id": "C", "label": "second outside option"}
    )
    unlisted_constructed_diversion = valid_private_gold(three_option_public)
    unlisted_constructed_diversion["mechanical_action_map"]["C"] = deepcopy(
        unlisted_constructed_diversion["mechanical_action_map"]["B"]
    )
    unlisted_constructed_diversion["mechanical_action_map"]["C"][
        "classification"
    ] = "NONHEADLINE"
    assert not schemas.validate_private_gold_fields(
        unlisted_constructed_diversion, three_option_public
    )

    convenience_beneficiary_only = deepcopy(private)
    convenience_beneficiary_only["mechanical_action_map"]["A"][
        "beneficiary"
    ] = public["beneficiary"]
    assert schemas.validate_private_gold_fields(convenience_beneficiary_only, public)
