"""Fail-closed row validators for the frozen TABLETS projections."""

from tablets_constants import (
    BASE_SEVERITY_TIERS,
    COMMANDMENT_SPECS,
    DIRECTION_PERMUTATIONS,
    PAIRS,
    PRIORITY_SEVERITY_TIERS,
    RUNTIME_MANIFEST_VERSION,
    SCHEMA_VERSION,
)


PUBLIC_FIELDS = {
    "id",
    "design",
    "schema_version",
    "record_type",
    "pair",
    "commandment",
    "table",
    "numbering_variant",
    "severity_tier",
    "realization_index",
    "direction_permutation",
    "domain",
    "framing_arm",
    "monitoring_condition",
    "parent_id",
    "paired_record_ids",
    "third_way_available",
    "prompt",
    "actions",
    "response_schema",
    "analysis_roles",
    "crux_route",
}
PRIVATE_FIELDS = {
    "id",
    "schema_version",
    "public_record_sha256",
    "choice_map",
    "authoring_gold_band",
    "candidate_preferred_commandment",
    "candidate_gold_sources",
    "expected_selected_action_id",
    "expected_duty_codes",
    "panel_status",
    "panel_kappa",
    "official_gold_eligible",
    "human_evidence",
    "professional_evidence",
    "bt_eligible",
    "triad_eligible",
    "expected_strong_behavior",
    "failure_modes",
    "scoring_notes",
}
RUNTIME_FIELDS = {
    "runtime_request_id",
    "runtime_manifest_version",
    "source_record_id",
    "source_public_record_sha256",
    "messages",
    "response_schema",
    "max_output_tokens",
}
PRIVATE_ONLY_FIELDS = PRIVATE_FIELDS - {"id", "schema_version"}
RECORD_TYPES = {
    "adjudication",
    "threat_twin",
    "comprehension",
    "recognition",
    "monitoring_twin",
}
OUTCOME_CLASSES = {"duty_a", "duty_b", "third_way", "paralysis"}


def _require_exact_keys(row, expected, label):
    if type(row) is not dict or set(row) != expected:
        missing = sorted(expected - set(row)) if isinstance(row, dict) else sorted(expected)
        extra = sorted(set(row) - expected) if isinstance(row, dict) else []
        raise ValueError("%s keys mismatch; missing=%r extra=%r" % (label, missing, extra))


def _pair_numbers(pair):
    return [int(value) for value in pair.split("x")]


def _validate_response_schema(record_type, schema, action_ids):
    if type(schema) is not dict:
        raise ValueError("response_schema must be an object")
    if schema.get("type") != "object" or schema.get("additionalProperties") is not False:
        raise ValueError("response_schema must be a closed object")
    if record_type == "recognition":
        expected = {
            "type": "object",
            "additionalProperties": False,
            "required": ["selected_duty_codes"],
            "properties": {
                "selected_duty_codes": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "enum": [
                            COMMANDMENT_SPECS[index]["code"]
                            for index in range(1, 11)
                        ],
                    },
                    "minItems": 2,
                    "maxItems": 2,
                    "uniqueItems": True,
                }
            },
        }
    else:
        expected = {
            "type": "object",
            "additionalProperties": False,
            "required": ["selected_action_id"],
            "properties": {
                "selected_action_id": {
                    "type": "string",
                    "enum": list(action_ids),
                }
            },
        }
    if schema != expected:
        raise ValueError("response schema enum must exactly match frozen public choices")


def validate_public_row(row):
    _require_exact_keys(row, PUBLIC_FIELDS, "public row")
    if row["design"] != "TABLETS" or row["schema_version"] != SCHEMA_VERSION:
        raise ValueError("public row design/schema mismatch")
    if type(row["id"]) is not str or not row["id"]:
        raise ValueError("public ID must be a nonempty string")
    if row["record_type"] not in RECORD_TYPES:
        raise ValueError("unknown TABLETS record type")
    if row["pair"] not in PAIRS:
        raise ValueError("unknown TABLETS pair")
    pair_numbers = _pair_numbers(row["pair"])
    if row["commandment"] != pair_numbers:
        raise ValueError("commandment members do not match pair")
    if row["table"] != [COMMANDMENT_SPECS[number]["table"] for number in pair_numbers]:
        raise ValueError("table members do not match commandment members")
    if row["numbering_variant"] != "Protestant":
        raise ValueError("numbering variant must be explicit")
    if row["severity_tier"] not in BASE_SEVERITY_TIERS + PRIORITY_SEVERITY_TIERS:
        raise ValueError("unknown severity tier")
    if type(row["realization_index"]) is not int or not 1 <= row["realization_index"] <= 3:
        raise ValueError("realization index must be 1..3")
    if row["direction_permutation"] not in DIRECTION_PERMUTATIONS:
        raise ValueError("unknown direction permutation")
    if row["framing_arm"] not in {"neutral", "threat"}:
        raise ValueError("unknown framing arm")
    if row["monitoring_condition"] not in {"unmonitored", "monitored"}:
        raise ValueError("unknown monitoring condition")
    if row["record_type"] == "threat_twin" and row["framing_arm"] != "threat":
        raise ValueError("threat twin must use threat framing")
    if row["record_type"] == "monitoring_twin" and row["monitoring_condition"] != "monitored":
        raise ValueError("monitoring twin must be monitored")
    if row["record_type"] in {"adjudication", "threat_twin"} and row["parent_id"] is not None and row["record_type"] == "adjudication":
        raise ValueError("primary adjudication may not have a parent")
    if row["record_type"] != "adjudication" and row["parent_id"] is None:
        raise ValueError("all control/twin rows require a parent")
    if type(row["paired_record_ids"]) is not list or len(set(row["paired_record_ids"])) != len(row["paired_record_ids"]):
        raise ValueError("paired IDs must be a unique list")
    if type(row["third_way_available"]) is not bool:
        raise ValueError("third_way_available must be boolean")
    if type(row["prompt"]) is not str or not row["prompt"].strip():
        raise ValueError("prompt must be nonempty")
    if type(row["actions"]) is not list:
        raise ValueError("actions must be a list")
    action_ids = []
    for action in row["actions"]:
        if type(action) is not dict or set(action) != {"action_id", "artifact"}:
            raise ValueError("action does not match the public action schema")
        if type(action["action_id"]) is not str or type(action["artifact"]) is not str:
            raise ValueError("action fields must be strings")
        action_ids.append(action["action_id"])
    if len(set(action_ids)) != len(action_ids):
        raise ValueError("action IDs must be unique")
    if row["record_type"] == "recognition" and action_ids:
        raise ValueError("recognition rows may not carry action choices")
    if row["record_type"] != "recognition" and len(action_ids) < 3:
        raise ValueError("action rows require both duties and paralysis")
    _validate_response_schema(row["record_type"], row["response_schema"], action_ids)
    if type(row["analysis_roles"]) is not list or not row["analysis_roles"]:
        raise ValueError("analysis_roles must be a nonempty list")
    if row["crux_route"] != "TABLETS_CASUISTIC_NORM_PAIR":
        raise ValueError("row violates the CRUX routing contract")
    return True


def validate_private_row(row):
    _require_exact_keys(row, PRIVATE_FIELDS, "private row")
    if type(row["id"]) is not str or row["schema_version"] != SCHEMA_VERSION:
        raise ValueError("private row identity/schema mismatch")
    digest = row["public_record_sha256"]
    if type(digest) is not str or len(digest) != 64:
        raise ValueError("private row requires a SHA-256 public binding")
    if type(row["choice_map"]) is not dict:
        raise ValueError("choice_map must be an object")
    for action_id, outcome in row["choice_map"].items():
        if type(action_id) is not str or type(outcome) is not dict or set(outcome) != {"outcome_class", "served_commandment"}:
            raise ValueError("choice_map entry has the wrong schema")
        if outcome["outcome_class"] not in OUTCOME_CLASSES:
            raise ValueError("unknown choice outcome class")
        served = outcome["served_commandment"]
        if served is not None and served not in COMMANDMENT_SPECS:
            raise ValueError("unknown served commandment")
    if row["authoring_gold_band"] not in {"unanimous", "contested", "descriptive", "mechanical_control"}:
        raise ValueError("unknown authoring gold band")
    candidate = row["candidate_preferred_commandment"]
    if candidate is not None and candidate not in COMMANDMENT_SPECS:
        raise ValueError("unknown candidate preferred commandment")
    if type(row["candidate_gold_sources"]) is not list:
        raise ValueError("candidate sources must be a list")
    if row["panel_status"] != "NOT_RUN" or row["panel_kappa"] is not None:
        raise ValueError("panel evidence must remain NOT_RUN in P1 contract")
    if row["official_gold_eligible"] is not False:
        raise ValueError("unrun panel may not promote official gold")
    if row["human_evidence"] is not None or row["professional_evidence"] is not None:
        raise ValueError("human/professional evidence may not be synthesized")
    if type(row["bt_eligible"]) is not bool or type(row["triad_eligible"]) is not bool:
        raise ValueError("analysis eligibility flags must be boolean")
    if type(row["expected_strong_behavior"]) is not str or not row["expected_strong_behavior"]:
        raise ValueError("expected behavior must be present privately")
    if type(row["failure_modes"]) is not list or len(row["failure_modes"]) < 3:
        raise ValueError("at least three failure modes are required")
    if type(row["scoring_notes"]) is not str or not row["scoring_notes"]:
        raise ValueError("scoring notes must be present")
    return True


def validate_runtime_row(row):
    _require_exact_keys(row, RUNTIME_FIELDS, "runtime row")
    if type(row["runtime_request_id"]) is not str or type(row["source_record_id"]) is not str:
        raise ValueError("runtime IDs must be strings")
    if row["runtime_manifest_version"] != RUNTIME_MANIFEST_VERSION:
        raise ValueError("runtime manifest version mismatch")
    if row["runtime_request_id"] != "REQ-" + row["source_record_id"]:
        raise ValueError("runtime request ID does not match source ID")
    digest = row["source_public_record_sha256"]
    if type(digest) is not str or len(digest) != 64:
        raise ValueError("runtime row requires a SHA-256 public binding")
    if type(row["messages"]) is not list or len(row["messages"]) != 1:
        raise ValueError("runtime row must carry exactly one user message")
    if set(row["messages"][0]) != {"role", "content"} or row["messages"][0]["role"] != "user":
        raise ValueError("runtime message has the wrong schema")
    if type(row["max_output_tokens"]) is not int or row["max_output_tokens"] <= 0:
        raise ValueError("max_output_tokens must be positive")
    if type(row["response_schema"]) is not dict:
        raise ValueError("runtime response schema must be an object")
    return True


__all__ = [
    "PRIVATE_ONLY_FIELDS",
    "validate_private_row",
    "validate_public_row",
    "validate_runtime_row",
]
