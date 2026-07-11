"""Exact field and type validation for PALTER bank projections."""

from palter_constants import (
    DIRECTIONS,
    FAMILIES,
    INCENTIVE_TIERS,
    MATERIAL_HARM_FLOOR_TIERS,
    PROBES_PER_CORE,
    RUNTIME_MANIFEST_VERSION,
    SCHEMA_VERSION,
    SOURCE_ATOMS_PER_CORE,
)


PRIVATE_ONLY_FIELDS = frozenset(
    {
        "atom_audit_route",
        "band_high",
        "band_low",
        "bt_sample",
        "gold_label",
        "material_harm",
        "material_harm_floor_tiers",
        "predicted_directional_shift",
        "probe_gold",
        "public_record_sha256",
        "spin_moves",
        "supported_atoms_sha256",
        "twin_id",
    }
)

PUBLIC_FIELDS = frozenset(
    {
        "schema_version",
        "id",
        "core_id",
        "record_type",
        "pack_family",
        "incentive_tier",
        "direction",
        "monitoring_condition",
        "source_atoms",
        "probes",
        "prompt",
        "candidate_composition",
        "response_schema",
        "surface_canary",
        "parent_id",
        "paired_record_ids",
    }
)
PRIVATE_FIELDS = frozenset(
    {
        "schema_version",
        "id",
        "core_id",
        "record_type",
        "public_record_sha256",
        "probe_gold",
        "supported_atoms_sha256",
        "spin_moves",
        "gold_label",
        "bt_sample",
        "atom_audit_route",
        "material_harm_floor_tiers",
        "twin_id",
        "parent_id",
        "paired_record_ids",
    }
)
RUNTIME_FIELDS = frozenset(
    {
        "schema_version",
        "runtime_manifest_version",
        "runtime_request_id",
        "source_record_id",
        "source_public_record_sha256",
        "pack_family",
        "record_type",
        "request_template",
        "response_schema",
        "parent_id",
        "paired_record_ids",
    }
)


def _exact_dict(value, fields, label):
    if type(value) is not dict or set(value) != set(fields):
        raise ValueError("%s fields do not match the frozen schema" % label)


def _nonempty_text(value, label):
    if type(value) is not str or not value.strip():
        raise ValueError("%s must be nonempty text" % label)


def _validate_source_atoms(atoms):
    if type(atoms) is not list or len(atoms) != SOURCE_ATOMS_PER_CORE:
        raise ValueError("source_atoms must contain exactly 12 atoms")
    ids = []
    for atom in atoms:
        _exact_dict(atom, {"atom_id", "text"}, "source atom")
        _nonempty_text(atom["atom_id"], "atom_id")
        _nonempty_text(atom["text"], "atom text")
        ids.append(atom["atom_id"])
    if len(set(ids)) != len(ids):
        raise ValueError("source atom IDs must be unique")


def _validate_public_probes(probes):
    if type(probes) is not list or len(probes) != PROBES_PER_CORE:
        raise ValueError("probes must contain exactly 10 rows")
    ids = []
    for probe in probes:
        _exact_dict(probe, {"probe_id", "question", "scale"}, "public probe")
        _nonempty_text(probe["probe_id"], "probe_id")
        _nonempty_text(probe["question"], "probe question")
        if probe["scale"] != {"min": -1.0, "max": 1.0}:
            raise ValueError("public probe scale must be the frozen [-1,1] scale")
        ids.append(probe["probe_id"])
    if len(set(ids)) != len(ids):
        raise ValueError("probe IDs must be unique")


def validate_public_row(row):
    _exact_dict(row, PUBLIC_FIELDS, "public row")
    if row["schema_version"] != SCHEMA_VERSION:
        raise ValueError("public schema_version is not frozen")
    for field in ("id", "core_id", "prompt", "surface_canary"):
        _nonempty_text(row[field], field)
    if row["record_type"] not in {
        "composition",
        "no_incentive_twin",
        "monitoring_twin",
        "recognition",
        "detection",
    }:
        raise ValueError("unknown record_type")
    if row["pack_family"] not in FAMILIES:
        raise ValueError("unknown pack_family")
    if row["direction"] not in DIRECTIONS:
        raise ValueError("unknown direction")
    allowed_tiers = set(INCENTIVE_TIERS) | {"T0", None}
    if row["incentive_tier"] not in allowed_tiers:
        raise ValueError("public schema has an unknown incentive tier")
    if row["monitoring_condition"] not in {"monitored", "unmonitored"}:
        raise ValueError("unknown monitoring condition")
    _validate_source_atoms(row["source_atoms"])
    _validate_public_probes(row["probes"])
    if row["record_type"] in {"detection", "recognition"}:
        _nonempty_text(row["candidate_composition"], "candidate composition")
    elif row["candidate_composition"] is not None:
        raise ValueError("only detection rows may carry a candidate composition")
    if type(row["response_schema"]) is not dict:
        raise ValueError("response_schema must be an object")
    if row["parent_id"] is not None:
        _nonempty_text(row["parent_id"], "parent_id")
    if type(row["paired_record_ids"]) is not list or not row["paired_record_ids"]:
        raise ValueError("paired_record_ids must be a nonempty exact list")
    if not all(type(record_id) is str and record_id for record_id in row["paired_record_ids"]):
        raise ValueError("paired_record_ids must contain nonempty strings")
    if len(set(row["paired_record_ids"])) != len(row["paired_record_ids"]):
        raise ValueError("paired_record_ids must be unique")
    expected_properties = {
        "composition": {"composition"},
        "no_incentive_twin": {"composition"},
        "monitoring_twin": {"composition"},
        "recognition": {"label"},
        "detection": {"label", "localized_moves"},
    }[row["record_type"]]
    response_properties = row["response_schema"].get("properties")
    if type(response_properties) is not dict or set(response_properties) != expected_properties:
        raise ValueError("response schema does not match record type")
    if set(row["response_schema"].get("required", [])) != expected_properties:
        raise ValueError("response schema required fields do not match record type")
    if row["record_type"] == "monitoring_twin":
        if row["monitoring_condition"] != "monitored" or row["parent_id"] is None:
            raise ValueError("monitoring twins require a monitored condition and parent")
    elif row["monitoring_condition"] != "unmonitored":
        raise ValueError("only monitoring twins may be monitored")
    return True


def validate_private_row(row):
    _exact_dict(row, PRIVATE_FIELDS, "private row")
    if row["schema_version"] != SCHEMA_VERSION:
        raise ValueError("private schema_version is not frozen")
    for field in (
        "id",
        "core_id",
        "public_record_sha256",
        "supported_atoms_sha256",
        "atom_audit_route",
        "twin_id",
    ):
        _nonempty_text(row[field], field)
    if len(row["public_record_sha256"]) != 64 or len(row["supported_atoms_sha256"]) != 64:
        raise ValueError("private hashes must be SHA-256 hex digests")
    if row["record_type"] not in {
        "composition",
        "no_incentive_twin",
        "monitoring_twin",
        "recognition",
        "detection",
    }:
        raise ValueError("unknown private record_type")
    if type(row["probe_gold"]) is not list or len(row["probe_gold"]) != PROBES_PER_CORE:
        raise ValueError("probe_gold must contain exactly 10 rows")
    ids = []
    for probe in row["probe_gold"]:
        _exact_dict(
            probe,
            {
                "probe_id",
                "band_low",
                "band_high",
                "material_harm",
                "predicted_directional_shift",
            },
            "private probe",
        )
        if type(probe["band_low"]) not in (int, float) or type(probe["band_high"]) not in (int, float):
            raise ValueError("probe bands must be numeric")
        if not -1.0 <= probe["band_low"] <= probe["band_high"] <= 1.0:
            raise ValueError("probe bands must be ordered inside [-1,1]")
        if type(probe["material_harm"]) is not bool:
            raise ValueError("material_harm must be boolean")
        shift = probe["predicted_directional_shift"]
        if type(shift) not in (int, float) or not 0.0 <= shift <= 1.0:
            raise ValueError("predicted directional shift must be in [0,1]")
        ids.append(probe["probe_id"])
    if len(set(ids)) != len(ids):
        raise ValueError("private probe IDs must be unique")
    if type(row["spin_moves"]) is not list or not all(
        type(move) is str and move for move in row["spin_moves"]
    ):
        raise ValueError("spin_moves must be nonempty strings")
    if row["gold_label"] not in {None, "faithful", "paltered"}:
        raise ValueError("gold_label is invalid")
    if type(row["bt_sample"]) is not bool:
        raise ValueError("bt_sample must be boolean")
    if row["atom_audit_route"] != "unsupported_claims_to_LY":
        raise ValueError("atom audit route changed")
    if row["material_harm_floor_tiers"] != list(MATERIAL_HARM_FLOOR_TIERS):
        raise ValueError("material-harm floor tiers changed")
    if row["parent_id"] is not None:
        _nonempty_text(row["parent_id"], "private parent_id")
    if type(row["paired_record_ids"]) is not list or not row["paired_record_ids"]:
        raise ValueError("private paired_record_ids must be a nonempty list")
    return True


def validate_runtime_row(row):
    _exact_dict(row, RUNTIME_FIELDS, "runtime row")
    if row["schema_version"] != SCHEMA_VERSION:
        raise ValueError("runtime schema_version is not frozen")
    if row["runtime_manifest_version"] != RUNTIME_MANIFEST_VERSION:
        raise ValueError("runtime manifest version changed")
    for field in (
        "runtime_request_id",
        "source_record_id",
        "source_public_record_sha256",
    ):
        _nonempty_text(row[field], field)
    if len(row["source_public_record_sha256"]) != 64:
        raise ValueError("runtime public linkage must be a SHA-256 digest")
    if row["pack_family"] not in FAMILIES:
        raise ValueError("runtime pack_family is invalid")
    if row["parent_id"] is not None:
        _nonempty_text(row["parent_id"], "runtime parent_id")
    if type(row["paired_record_ids"]) is not list or not row["paired_record_ids"]:
        raise ValueError("runtime paired_record_ids must be a nonempty list")
    if type(row["request_template"]) is not dict or type(row["response_schema"]) is not dict:
        raise ValueError("runtime templates must be objects")
    return True
