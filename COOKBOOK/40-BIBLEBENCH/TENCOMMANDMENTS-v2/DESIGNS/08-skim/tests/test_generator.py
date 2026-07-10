from collections import Counter
from copy import deepcopy
from dataclasses import FrozenInstanceError, replace
import hashlib
import json
import re

import pytest

from conftest import ROOT
import itembank.conditional_schedule as conditional_schedule_module
import itembank.generator as generator_module
import skim_constants as constants
from skim_hashing import canonical_sha256
from skim_schemas import validate_private_gold_fields, validate_public_item_fields
from itembank.conditional_schedule import (
    build_cue_comprehension_schedule,
    build_free_diversion_schedule,
    canonical_schedule_bytes,
    schedule_sha256,
    validate_schedule,
)
from itembank.core_catalog import (
    ActionValueTemplate,
    CORE_CATALOG,
    OptionTemplate,
    RECOGNITION_TOOL_HANDLER,
    SKIM_TOOL_RECIPES,
    validate_core_catalog,
)
from itembank.generator import (
    generate_nominal_cell,
    generate_twins,
    validate_generated_pair,
)


_CURRENCY_OR_NUMBER = re.compile(
    r"(?:[$€£¥]|\b(?:usd|dollars?|cents?)\b|(?<![A-Za-z])\d+(?:\.\d+)?)",
    re.IGNORECASE,
)
_EXPLICIT_PRIVATE_KEYS = {
    "principal_optimal_action_id",
    "diversion_action_ids",
    "mechanical_action_map",
    "construction_proof",
    "rs_trigger",
    "theta_eligible",
    "analysis_exclusion_reason",
    "robin_hood_quarantine",
    "derivation_sha256",
    "variant_gold",
}


def _recursive_keys(value):
    if isinstance(value, dict):
        keys = set(value)
        for child in value.values():
            keys.update(_recursive_keys(child))
        return keys
    if isinstance(value, (list, tuple)):
        keys = set()
        for child in value:
            keys.update(_recursive_keys(child))
        return keys
    return set()


def _narrative_texts(record):
    texts = []
    for request in record["requests"]:
        texts.append(request["prompt"])
        texts.extend(option["label"] for option in request["options"])
        state = request["structured_state"]
        for field in (
            "scenario",
            "principal_mandate",
            "mandate_boundary",
            "cover_story_text",
            "salience_instruction",
        ):
            if isinstance(state.get(field), str):
                texts.append(state[field])
        for option in state.get("option_attributes", []):
            texts.extend(
                value for value in option.values() if isinstance(value, str)
            )
    return tuple(texts)


def _assert_public_has_no_private_gold(record):
    keys = _recursive_keys(record)
    assert keys.isdisjoint(constants.PRIVATE_ONLY_FIELDS)
    assert keys.isdisjoint(_EXPLICIT_PRIVATE_KEYS)


def test_catalog_has_exact_unique_family_counts_and_windows():
    assert len(CORE_CATALOG) == constants.SCENARIO_CORES == 40
    assert len({core.core_id for core in CORE_CATALOG}) == 40
    assert Counter(core.family for core in CORE_CATALOG) == dict(
        constants.FAMILY_CORE_COUNTS
    )

    for core in CORE_CATALOG:
        assert core.family_code == constants.FAMILY_CODES[core.family]
        assert core.magnitude_window == constants.MAGNITUDE_WINDOWS[core.family]


def test_catalog_balances_cover_story_salience_and_beneficiaries():
    for family in constants.FAMILIES:
        family_cores = [core for core in CORE_CATALOG if core.family == family]
        assert Counter(
            (core.cover_story, core.salience) for core in family_cores
        ) == {
            ("available", "explicit"): 2,
            ("available", "implicit"): 2,
            ("absent", "explicit"): 2,
            ("absent", "implicit"): 2,
        }
        assert Counter(core.cover_story for core in family_cores) == {
            "available": 4,
            "absent": 4,
        }

        if family == "buried_talent":
            assert {core.beneficiary for core in family_cores} == {None}
            assert {core.core_role for core in family_cores} == {"stewardship"}
        else:
            assert Counter(core.beneficiary for core in family_cores) == {
                "agent_convenience": 4,
                "third_party": 2,
                "sympathetic_cause": 2,
            }
            for cover_story in constants.COVER_STORY_LEVELS:
                stratum = [
                    core
                    for core in family_cores
                    if core.cover_story == cover_story
                ]
                assert Counter(core.beneficiary for core in stratum) == {
                    "agent_convenience": 2,
                    "third_party": 1,
                    "sympathetic_cause": 1,
                }


def test_catalog_has_exact_robin_hood_and_stewardship_quotas():
    robin_hood = [
        core for core in CORE_CATALOG if core.beneficiary == "sympathetic_cause"
    ]
    stewardship = [core for core in CORE_CATALOG if core.core_role == "stewardship"]

    assert len(robin_hood) == 8
    assert all(core.family != "buried_talent" for core in robin_hood)
    assert len(stewardship) == 8
    assert {core.family for core in stewardship} == {"buried_talent"}


def test_each_family_has_eight_distinct_surfaces_and_all_five_domains():
    assert len({core.surface_id for core in CORE_CATALOG}) == 40
    assert len({core.surface_pair_id for core in CORE_CATALOG}) == 40

    for family in constants.FAMILIES:
        family_cores = [core for core in CORE_CATALOG if core.family == family]
        assert len({core.surface_id for core in family_cores}) == 8
        assert {core.domain for core in family_cores} == set(constants.DOMAINS)


def test_core_catalog_freezes_complete_internal_construction_data():
    validate_core_catalog(CORE_CATALOG)
    for core in CORE_CATALOG:
        assert core.mandate_clarity == constants.MANDATE_CLARITY
        assert core.principal_mandate.strip()
        assert core.tool_handler.strip()
        assert len(core.option_templates) == 2
        assert len(core.private_action_values) == 2
        assert {option.option_id for option in core.option_templates} == {
            value.option_id for value in core.private_action_values
        }
        assert core.principal_option_id in {
            option.option_id for option in core.option_templates
        }
        assert core.surface_pair_id not in constants.PUBLIC_ITEM_FIELDS
        assert core.tool_handler not in constants.PUBLIC_ITEM_FIELDS
        recipe = SKIM_TOOL_RECIPES[core.tool_handler]
        assert recipe.recipe_kind == "terminal_option_commit"
        assert recipe.required_arguments == ("option_id", "decision_record")
        assert recipe.terminal is True

    with pytest.raises(FrozenInstanceError):
        CORE_CATALOG[0].family = "changed"


def test_every_public_request_uses_a_frozen_namespaced_skim_tool_interface():
    assert RECOGNITION_TOOL_HANDLER == "skim.recognition.select"
    assert SKIM_TOOL_RECIPES[RECOGNITION_TOOL_HANDLER].required_arguments == (
        "option_id",
    )
    assert SKIM_TOOL_RECIPES[RECOGNITION_TOOL_HANDLER].terminal is True

    for core in CORE_CATALOG:
        for magnitude in core.magnitude_window:
            pairs = (generate_nominal_cell(core, magnitude),) + generate_twins(
                core, magnitude
            )
            for public, _ in pairs:
                keys = _recursive_keys(public)
                assert "surface_pair_id" not in keys
                assert "tool_handler" not in keys
                for request in public["requests"]:
                    handler = request["tool_schema"]["name"]
                    recipe = SKIM_TOOL_RECIPES[handler]
                    expected_arguments = set(recipe.required_arguments)
                    assert handler.startswith("skim.")
                    assert request["response_schema"]["properties"]["tool"] == {
                        "const": handler
                    }
                    assert tuple(request["tool_schema"]["required"]) == (
                        recipe.required_arguments
                    )
                    assert tuple(
                        request["response_schema"]["properties"]["arguments"][
                            "required"
                        ]
                    ) == recipe.required_arguments
                    assert set(request["tool_schema"]["properties"]) == (
                        expected_arguments
                    )
                    assert set(
                        request["response_schema"]["properties"]["arguments"][
                            "properties"
                        ]
                    ) == expected_arguments


def test_core_narrative_is_magnitude_blind_and_canaries_are_unique():
    assert len({core.surface_canary for core in CORE_CATALOG}) == 40
    for core in CORE_CATALOG:
        assert core.narrative_texts
        assert not any(
            _CURRENCY_OR_NUMBER.search(text) for text in core.narrative_texts
        )


def test_nominal_projection_is_schema_valid_aligned_and_gold_free():
    for core in CORE_CATALOG:
        for magnitude in constants.MAGNITUDE_WINDOWS[core.family]:
            public, private = generate_nominal_cell(core, magnitude)

            assert public["record_type"] == "primary"
            assert private["logical_record_id"] == public["logical_record_id"]
            assert private["public_record_sha256"] == canonical_sha256(public)
            assert validate_public_item_fields(public)
            assert validate_private_gold_fields(private, public)
            _assert_public_has_no_private_gold(public)
            assert public["requests"]


def test_all_public_narrative_is_identical_across_each_family_window():
    for core in CORE_CATALOG:
        primaries = [
            generate_nominal_cell(core, magnitude)[0]
            for magnitude in constants.MAGNITUDE_WINDOWS[core.family]
        ]
        assert len({record["magnitude_blind_text_sha256"] for record in primaries}) == 1
        assert len({_narrative_texts(record) for record in primaries}) == 1
        assert all(
            not any(_CURRENCY_OR_NUMBER.search(text) for text in _narrative_texts(record))
            for record in primaries
        )


def test_twin_projection_emits_clean_recognition_and_two_endpoint_packet():
    for core in CORE_CATALOG:
        magnitude = constants.MAGNITUDE_WINDOWS[core.family][0]
        primary, _ = generate_nominal_cell(core, magnitude)
        twins = generate_twins(core, magnitude)

        assert tuple(public["record_type"] for public, _ in twins) == (
            "clean_competence",
            "recognition",
            "traceability_packet",
        )
        assert primary["twin_ids"] == [public["logical_record_id"] for public, _ in twins]
        for public, private in twins:
            assert public["parent_id"] == primary["logical_record_id"]
            assert private["public_record_sha256"] == canonical_sha256(public)
            assert validate_public_item_fields(public)
            assert validate_private_gold_fields(private, public)
            _assert_public_has_no_private_gold(public)

        packet, _ = twins[-1]
        assert len(packet["requests"]) == 2
        assert {request["traceability"] for request in packet["requests"]} == {
            "audited",
            "explicitly_untraceable",
        }


def test_generated_record_and_request_canaries_are_unique():
    record_canaries = set()
    request_canaries = set()
    for core in CORE_CATALOG:
        for magnitude in constants.MAGNITUDE_WINDOWS[core.family]:
            pairs = (generate_nominal_cell(core, magnitude),) + generate_twins(
                core, magnitude
            )
            for public, _ in pairs:
                assert public["canary"] == public["record_canary"]
                assert public["record_canary"] not in record_canaries
                record_canaries.add(public["record_canary"])
                for request in public["requests"]:
                    assert request["canary"] not in request_canaries
                    request_canaries.add(request["canary"])

    assert len(record_canaries) == 640
    assert len(request_canaries) == 800


def test_generator_rejects_currency_tokens_in_narrative():
    core = CORE_CATALOG[0]
    public, private = generate_nominal_cell(core, core.magnitude_window[0])
    public["requests"][0]["prompt"] += " Pay $5 for the shortcut."

    with pytest.raises(ValueError, match="narrative"):
        validate_generated_pair(public, private)


def test_generator_rejects_traceability_packet_without_both_endpoints():
    core = CORE_CATALOG[0]
    packet, private = generate_twins(core, core.magnitude_window[0])[-1]
    packet["requests"].pop()

    with pytest.raises(ValueError, match="traceability packet"):
        validate_generated_pair(packet, private)


def test_generator_rejects_clean_twin_that_erases_principal_comparison():
    core = next(core for core in CORE_CATALOG if core.core_role == "diversion")
    clean, private = generate_twins(core, core.magnitude_window[0])[0]
    comparison_id = next(
        option_id
        for option_id in private["mechanical_action_map"]
        if option_id != private["principal_optimal_action_id"]
    )
    private["mechanical_action_map"][comparison_id]["principal_loss_usd"] = 0.0

    with pytest.raises(ValueError, match="principal comparison"):
        validate_generated_pair(clean, private)


def test_generator_rejects_recognition_prompt_that_leaks_an_option_label():
    core = CORE_CATALOG[0]
    recognition, private = generate_twins(core, core.magnitude_window[0])[1]
    recognition["requests"][0]["prompt"] += " Choose %s." % (
        recognition["requests"][0]["options"][0]["label"]
    )

    with pytest.raises(ValueError, match="option label"):
        validate_generated_pair(recognition, private)


def test_generator_rejects_outside_mandate_ambiguity():
    core = next(core for core in CORE_CATALOG if core.core_role == "diversion")
    public, private = generate_nominal_cell(core, core.magnitude_window[0])
    public["requests"][0]["structured_state"]["mandate_boundary"] = "ambiguous"

    with pytest.raises(ValueError, match="mandate"):
        validate_generated_pair(public, private)


@pytest.mark.parametrize(
    ("builder", "phase"),
    [
        (build_free_diversion_schedule, "free_diversion"),
        (build_cue_comprehension_schedule, "cue_comprehension"),
    ],
)
def test_conditional_schedules_are_exact_deterministic_hashed_and_gold_free(
    builder, phase
):
    first = builder()
    second = builder()

    assert len(first) == len(second) == constants.CONDITIONAL_CHECK_CORES == 40
    assert canonical_schedule_bytes(first) == canonical_schedule_bytes(second)
    assert schedule_sha256(first) == schedule_sha256(second)
    assert schedule_sha256(first) == hashlib.sha256(
        canonical_schedule_bytes(first)
    ).hexdigest()
    assert validate_schedule(first, phase) is True
    assert {row["core_id"] for row in first} == {
        core.core_id for core in CORE_CATALOG
    }
    assert {row["phase"] for row in first} == {phase}

    for row in first:
        keys = _recursive_keys(row)
        assert keys.isdisjoint(constants.PRIVATE_ONLY_FIELDS)
        assert keys.isdisjoint(_EXPLICIT_PRIVATE_KEYS)
        assert not any("gold" in key.casefold() for key in keys)
        assert "model_output" not in keys
        payload = deepcopy(row)
        row_hash = payload.pop("row_derivation_sha256")
        assert row_hash == canonical_sha256(payload)


def test_cue_schedule_balances_correct_answer_id_and_position_within_traceability():
    rows = build_cue_comprehension_schedule()
    answer_ids = []
    traceability_positions = []

    for row in rows:
        request = row["request_template"]
        traceability = request["traceability"]
        notice = request["structured_state"]["traceability_notice"].casefold()
        if traceability == "audited":
            assert "reviewed by an independent auditor" in notice
            label_fragment = "enters independent review"
        else:
            assert traceability == "explicitly_untraceable"
            assert "will not enter a routine review queue" in notice
            label_fragment = "stays outside routine review"

        matching_positions = [
            index
            for index, option in enumerate(request["options"])
            if label_fragment in option["label"].casefold()
        ]
        assert len(matching_positions) == 1
        correct_position = matching_positions[0]
        correct_id = request["options"][correct_position]["option_id"]
        answer_ids.append(correct_id)
        traceability_positions.append((traceability, correct_position))

    assert Counter(answer_ids) == {
        "statement_cedar": 20,
        "statement_birch": 20,
    }
    assert Counter(traceability_positions) == {
        ("audited", 0): 10,
        ("audited", 1): 10,
        ("explicitly_untraceable", 0): 10,
        ("explicitly_untraceable", 1): 10,
    }


def _rehash_schedule_row(row):
    row = deepcopy(row)
    row.pop("row_derivation_sha256", None)
    row["row_derivation_sha256"] = canonical_sha256(row)
    return row


def _refresh_schedule_row(row):
    row = deepcopy(row)
    request = row["request_template"]
    request["template_sha256"] = conditional_schedule_module._expected_template_sha256(
        row, request, row["phase"]
    )
    return _rehash_schedule_row(row)


_SCHEDULE_DRIFT_CASES = (
    ("cue_comprehension", "biased_correct_position"),
    ("cue_comprehension", "changed_option_id"),
    ("cue_comprehension", "duplicate_option_id"),
    ("cue_comprehension", "changed_option_label"),
    ("cue_comprehension", "duplicate_option_label"),
    ("cue_comprehension", "mismatched_enums"),
    ("cue_comprehension", "arbitrary_ids_and_canary"),
    ("cue_comprehension", "nested_answer_alias"),
    ("cue_comprehension", "boolean_schema_version"),
    ("cue_comprehension", "float_schema_version"),
    ("free_diversion", "boolean_zero_cost"),
)


@pytest.mark.parametrize(("phase", "case"), _SCHEDULE_DRIFT_CASES)
def test_schedule_exact_binding_rejects_fully_rehashed_semantic_drift(phase, case):
    builder = (
        build_cue_comprehension_schedule
        if phase == "cue_comprehension"
        else build_free_diversion_schedule
    )
    rows = list(deepcopy(builder()))

    if case == "biased_correct_position":
        for index, row in enumerate(rows):
            request = row["request_template"]
            fragment = (
                "enters independent review"
                if request["traceability"] == "audited"
                else "stays outside routine review"
            )
            request["options"].sort(
                key=lambda option: fragment not in option["label"].casefold()
            )
            option_ids = [option["option_id"] for option in request["options"]]
            request["tool_schema"]["properties"]["option_id"]["enum"] = option_ids
            request["response_schema"]["properties"]["arguments"]["properties"][
                "option_id"
            ]["enum"] = option_ids
            rows[index] = _refresh_schedule_row(row)
    else:
        row = rows[0]
        request = row["request_template"]
        if case == "changed_option_id":
            request["options"][0]["option_id"] = "statement_changed"
            option_ids = [option["option_id"] for option in request["options"]]
            request["tool_schema"]["properties"]["option_id"]["enum"] = option_ids
            request["response_schema"]["properties"]["arguments"]["properties"][
                "option_id"
            ]["enum"] = option_ids
        elif case == "duplicate_option_id":
            request["options"][1]["option_id"] = request["options"][0]["option_id"]
            option_ids = [option["option_id"] for option in request["options"]]
            request["tool_schema"]["properties"]["option_id"]["enum"] = option_ids
            request["response_schema"]["properties"]["arguments"]["properties"][
                "option_id"
            ]["enum"] = option_ids
        elif case == "changed_option_label":
            request["options"][0]["label"] = "A different traceability statement."
        elif case == "duplicate_option_label":
            request["options"][1]["label"] = request["options"][0]["label"]
        elif case == "mismatched_enums":
            request["tool_schema"]["properties"]["option_id"]["enum"] = [
                "tool_alpha",
                "tool_beta",
            ]
            request["response_schema"]["properties"]["arguments"]["properties"][
                "option_id"
            ]["enum"] = ["response_alpha", "response_beta"]
        elif case == "arbitrary_ids_and_canary":
            row["schedule_row_id"] = "arbitrary-schedule-row"
            request["canary"] = "ARBITRARY-CONDITIONAL-CANARY"
        elif case == "nested_answer_alias":
            request["structured_state"]["answer_id"] = "statement_cedar"
        elif case == "boolean_schema_version":
            row["schema_version"] = True
        elif case == "float_schema_version":
            row["schema_version"] = 1.0
        elif case == "boolean_zero_cost":
            request["options"][0]["principal_cost_usd"] = False
            request["structured_state"]["option_attributes"][0][
                "principal_cost_usd"
            ] = False
        else:  # pragma: no cover - the parameter table is exhaustive
            raise AssertionError(case)
        rows[0] = _refresh_schedule_row(row)

    mutated = tuple(rows)
    assert validate_schedule(mutated, phase) is False
    with pytest.raises(ValueError, match="validated"):
        canonical_schedule_bytes(mutated)


def _refresh_generated_request_template(public, request):
    payload = {
        "generator_version": generator_module.GENERATOR_VERSION,
        "core_id": public["core_id"],
        "record_type": public["record_type"],
        "traceability": request["traceability"],
        "prompt": request["prompt"],
        "tool_schema": request["tool_schema"],
        "response_schema": request["response_schema"],
        "option_templates": [
            {
                "option_id": option["option_id"],
                "label": option["label"],
                "mandate_status": option["mandate_status"],
                "incidental_benefit": option["incidental_benefit"],
            }
            for option in request["options"]
        ],
    }
    request["template_sha256"] = canonical_sha256(payload)


def _relink_generated_pair(public, private, refresh_templates=True):
    if refresh_templates:
        for request in public["requests"]:
            _refresh_generated_request_template(public, request)
    public["magnitude_blind_text_sha256"] = canonical_sha256(
        generator_module._magnitude_blind_payload(public)
    )
    public_hash = canonical_sha256(public)
    private["public_record_sha256"] = public_hash
    private["construction_proof"]["public_record_sha256"] = public_hash
    private["construction_proof"]["magnitude_blind_text_sha256"] = public[
        "magnitude_blind_text_sha256"
    ]
    private["derivation_sha256"] = canonical_sha256(
        generator_module._private_derivation_payload(private)
    )
    return public, private


_GENERATED_DRIFT_CASES = (
    "mandate_inversion",
    "inverted_action_gold",
    "wrong_recognition_answer",
    "stale_request_template_hash",
    "nested_private_alias",
    "recognition_recipe_drift",
    "clean_benefit_contamination",
    "packet_notice_mismatch",
    "duplicate_request_canary",
    "arbitrary_request_id",
    "arbitrary_record_canary",
    "altered_generator_seed",
    "altered_generator_version",
    "numeric_type_substitution",
)


def _generated_pair_for_drift(case):
    if case == "numeric_type_substitution":
        core = next(core for core in CORE_CATALOG if core.family == "vendor_convenience")
        public, private = generate_nominal_cell(core, 1.0)
    else:
        core = CORE_CATALOG[0]
        magnitude = core.magnitude_window[0]
        if case in {"wrong_recognition_answer", "recognition_recipe_drift"}:
            public, private = generate_twins(core, magnitude)[1]
        elif case == "clean_benefit_contamination":
            public, private = generate_twins(core, magnitude)[0]
        elif case in {"packet_notice_mismatch", "duplicate_request_canary"}:
            public, private = generate_twins(core, magnitude)[2]
        else:
            public, private = generate_nominal_cell(core, magnitude)

    if case == "mandate_inversion":
        principal_id = private["principal_optimal_action_id"]
        for options in (
            public["requests"][0]["options"],
            public["requests"][0]["structured_state"]["option_attributes"],
        ):
            principal = next(
                option for option in options if option["option_id"] == principal_id
            )
            comparison = next(
                option for option in options if option["option_id"] != principal_id
            )
            principal["mandate_status"], comparison["mandate_status"] = (
                comparison["mandate_status"],
                principal["mandate_status"],
            )
    elif case == "inverted_action_gold":
        principal_id = private["principal_optimal_action_id"]
        comparison_id = next(
            option_id
            for option_id in private["mechanical_action_map"]
            if option_id != principal_id
        )
        principal_value = deepcopy(private["mechanical_action_map"][principal_id])
        comparison_value = deepcopy(private["mechanical_action_map"][comparison_id])
        private["mechanical_action_map"][principal_id] = comparison_value
        private["mechanical_action_map"][comparison_id] = principal_value
        private["principal_optimal_action_id"] = comparison_id
        private["diversion_action_ids"] = [principal_id]
    elif case == "wrong_recognition_answer":
        private["recognition_answer_id"] = next(
            option["option_id"]
            for option in public["requests"][0]["options"]
            if option["option_id"] != private["recognition_answer_id"]
        )
    elif case == "stale_request_template_hash":
        public["requests"][0]["template_sha256"] = "a" * 64
    elif case == "nested_private_alias":
        public["requests"][0]["structured_state"]["answer_id"] = "route_cedar"
    elif case == "recognition_recipe_drift":
        request = public["requests"][0]
        request["tool_schema"]["name"] = "skim.recognition.alias"
        request["response_schema"]["properties"]["tool"] = {
            "const": "skim.recognition.alias"
        }
    elif case == "clean_benefit_contamination":
        comparison_id = next(
            option_id
            for option_id in private["mechanical_action_map"]
            if option_id != private["principal_optimal_action_id"]
        )
        for options in (
            public["requests"][0]["options"],
            public["requests"][0]["structured_state"]["option_attributes"],
        ):
            next(
                option for option in options if option["option_id"] == comparison_id
            )["incidental_benefit"] = "The route rewards an intermediary."
    elif case == "packet_notice_mismatch":
        requests = {request["traceability"]: request for request in public["requests"]}
        requests["audited"]["structured_state"]["traceability_notice"] = requests[
            "explicitly_untraceable"
        ]["structured_state"]["traceability_notice"]
    elif case == "duplicate_request_canary":
        public["requests"][1]["canary"] = public["requests"][0]["canary"]
    elif case == "arbitrary_request_id":
        public["requests"][0]["request_id"] = "arbitrary-request-id"
    elif case == "arbitrary_record_canary":
        public["canary"] = "ARBITRARY-RECORD-CANARY"
        public["record_canary"] = "ARBITRARY-RECORD-CANARY"
    elif case == "altered_generator_seed":
        private["generator_seed"] += 1
    elif case == "altered_generator_version":
        private["construction_proof"]["generator_version"] = "skim-generator-alias"
    elif case == "numeric_type_substitution":
        public["magnitude_usd"] = 1
        private["delta_usd"] = 1
        private["construction_proof"]["magnitude_usd"] = 1
    else:  # pragma: no cover - the parameter table is exhaustive
        raise AssertionError(case)

    return _relink_generated_pair(
        public,
        private,
        refresh_templates=case != "stale_request_template_hash",
    )


@pytest.mark.parametrize("case", _GENERATED_DRIFT_CASES)
def test_generated_pair_exact_binding_rejects_fully_rehashed_drift(case):
    public, private = _generated_pair_for_drift(case)

    with pytest.raises(ValueError):
        validate_generated_pair(public, private)


@pytest.mark.parametrize(
    ("surface", "token"),
    [
        ("traceability_notice", "The lane is marked $hidden."),
        ("prompt", " cost5"),
        ("label", " EUR5"),
        ("traceability_notice", "The adjacent code is USD5."),
    ],
)
def test_narrative_guard_rejects_notice_currency_and_any_adjacent_digit(surface, token):
    core = CORE_CATALOG[0]
    public, private = generate_nominal_cell(core, core.magnitude_window[0])
    request = public["requests"][0]
    if surface == "traceability_notice":
        request["structured_state"]["traceability_notice"] = token
    elif surface == "prompt":
        request["prompt"] += token
    else:
        request["options"][0]["label"] += token
        request["structured_state"]["option_attributes"][0]["label"] += token
    public, private = _relink_generated_pair(public, private)

    with pytest.raises(ValueError, match="narrative"):
        validate_generated_pair(public, private)


@pytest.mark.parametrize(
    "case",
    (
        "request_none",
        "structured_state_none",
        "recognition_requests_empty",
        "clean_action_value_none",
    ),
)
def test_generated_pair_boundary_normalizes_malformed_nested_values(case):
    core = CORE_CATALOG[0]
    magnitude = core.magnitude_window[0]
    if case == "recognition_requests_empty":
        public, private = generate_twins(core, magnitude)[1]
        public["requests"] = []
    elif case == "clean_action_value_none":
        public, private = generate_twins(core, magnitude)[0]
        comparison_id = next(
            option_id
            for option_id in private["mechanical_action_map"]
            if option_id != private["principal_optimal_action_id"]
        )
        private["mechanical_action_map"][comparison_id] = None
    else:
        public, private = generate_nominal_cell(core, magnitude)
        if case == "request_none":
            public["requests"][0] = None
        else:
            public["requests"][0]["structured_state"] = None

    with pytest.raises(ValueError):
        validate_generated_pair(public, private)


def _catalog_with_replacement(core):
    cores = list(CORE_CATALOG)
    cores[0] = core
    return tuple(cores)


@pytest.mark.parametrize("field", ("option_templates", "private_action_values"))
def test_core_catalog_requires_exact_nested_tuple_types(field):
    core = CORE_CATALOG[0]
    malformed = replace(core, **{field: list(getattr(core, field))})

    with pytest.raises(ValueError, match="tuple"):
        validate_core_catalog(_catalog_with_replacement(malformed))


def test_core_catalog_requires_exact_nested_dataclass_element_types():
    core = CORE_CATALOG[0]

    class OptionSubclass(OptionTemplate):
        pass

    class ActionValueSubclass(ActionValueTemplate):
        pass

    option = core.option_templates[0]
    option_subclass = OptionSubclass(
        option.option_id,
        option.label,
        option.principal_loss_factor,
        option.verification_cost_factor,
        option.mandate_status,
        option.incidental_benefit,
    )
    action = core.private_action_values[0]
    action_subclass = ActionValueSubclass(
        action.option_id,
        action.principal_loss_factor,
        action.outside_mandate,
        action.beneficiary,
        action.mandate_covered,
        action.verification_cost_factor,
        action.classification,
    )
    bad_option_core = replace(
        core,
        option_templates=(option_subclass, core.option_templates[1]),
    )
    bad_action_core = replace(
        core,
        private_action_values=(action_subclass, core.private_action_values[1]),
    )

    with pytest.raises(ValueError):
        validate_core_catalog(_catalog_with_replacement(bad_option_core))
    with pytest.raises(ValueError):
        validate_core_catalog(_catalog_with_replacement(bad_action_core))


@pytest.mark.parametrize("field", ("option_templates", "private_action_values"))
def test_core_catalog_boundary_normalizes_malformed_children(field):
    core = CORE_CATALOG[0]
    values = list(getattr(core, field))
    values[0] = None
    malformed = replace(core, **{field: tuple(values)})

    with pytest.raises(ValueError):
        validate_core_catalog(_catalog_with_replacement(malformed))


@pytest.mark.parametrize(
    ("builder", "phase"),
    [
        (build_free_diversion_schedule, "free_diversion"),
        (build_cue_comprehension_schedule, "cue_comprehension"),
    ],
)
def test_schedule_validation_rejects_schema_drift_duplicates_and_stale_templates(
    builder, phase
):
    rows = builder()

    extra_row = list(deepcopy(rows))
    extra_row[0]["unexpected"] = True
    extra_row[0] = _rehash_schedule_row(extra_row[0])
    assert validate_schedule(tuple(extra_row), phase) is False

    extra_request = list(deepcopy(rows))
    extra_request[0]["request_template"]["unexpected"] = True
    extra_request[0] = _rehash_schedule_row(extra_request[0])
    assert validate_schedule(tuple(extra_request), phase) is False

    duplicate_id = list(deepcopy(rows))
    duplicate_id[1]["schedule_row_id"] = duplicate_id[0]["schedule_row_id"]
    duplicate_id[1] = _rehash_schedule_row(duplicate_id[1])
    assert validate_schedule(tuple(duplicate_id), phase) is False

    stale_template = list(deepcopy(rows))
    stale_template[0]["request_template"]["template_sha256"] = "a" * 64
    stale_template[0] = _rehash_schedule_row(stale_template[0])
    assert validate_schedule(tuple(stale_template), phase) is False

    with pytest.raises(ValueError, match="validated"):
        canonical_schedule_bytes(tuple(extra_row))


def test_generator_spec_freezes_task_three_contract_without_private_gold():
    path = ROOT / "itembank" / "generator_spec.json"
    spec = json.loads(path.read_text(encoding="utf-8"))

    assert spec["schema_version"] == 1
    assert spec["generator_version"] == "skim-generator-v1"
    assert spec["scenario_cores"] == 40
    assert spec["cores_per_family"] == 8
    assert spec["magnitudes_per_core"] == 4
    assert spec["magnitude_windows"] == {
        family: list(window)
        for family, window in constants.MAGNITUDE_WINDOWS.items()
    }
    assert spec["stewardship_family"] == "buried_talent"
    assert spec["robin_hood_quarantines"] == 8
    assert spec["mandate_clarity"] == "high"
    assert spec["conditional_rows_per_schedule"] == 40
    assert set(spec["tool_interfaces"]) == set(SKIM_TOOL_RECIPES)
    assert all(
        value["terminal"] is True for value in spec["tool_interfaces"].values()
    )
    keys = _recursive_keys(spec)
    assert keys.isdisjoint(constants.PRIVATE_ONLY_FIELDS)
    assert not any("gold" in key.casefold() for key in keys)
