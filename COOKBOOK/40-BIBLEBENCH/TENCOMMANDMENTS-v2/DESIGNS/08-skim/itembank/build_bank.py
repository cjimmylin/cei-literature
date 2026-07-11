"""Build and transactionally install the deterministic SKIM P1 item bank."""

from collections import Counter
from collections.abc import Mapping as MappingABC
from contextlib import contextmanager
import fcntl
import hashlib
import json
import os
from pathlib import Path
import stat
import sys
import tempfile
from types import MappingProxyType


ITEMBANK_ROOT = Path(__file__).resolve().parent
SKIM_ROOT = ITEMBANK_ROOT.parent
if str(SKIM_ROOT) not in sys.path:
    sys.path.insert(0, str(SKIM_ROOT))

from skim_constants import (  # noqa: E402
    FAMILIES,
    FAMILY_CODES,
    GLOBAL_MAGNITUDE_FREQUENCIES,
    LOGICAL_BANK_RECORDS,
    LOGICAL_RECORD_COUNTS,
    MAGNITUDE_ORDER,
    PRIVATE_GOLD_RECORDS,
    PRIVATE_ONLY_FIELDS,
    REQUESTS_PER_MODEL_SEED,
)
from skim_hashing import canonical_json, canonical_sha256  # noqa: E402
from itembank.conditional_schedule import (  # noqa: E402
    SCHEDULE_VERSION,
    build_cue_comprehension_schedule,
    build_free_diversion_schedule,
    canonical_schedule_bytes,
    validate_schedule,
)
from itembank.core_catalog import CORE_CATALOG  # noqa: E402
from itembank.generator import (  # noqa: E402
    GENERATOR_SEED,
    GENERATOR_VERSION,
    generate_nominal_cell,
    generate_twins,
    validate_generated_pair,
)


BANK_BUILDER_VERSION = "skim-bank-builder-v1"
RUNTIME_MANIFEST_VERSION = "skim-runtime-manifest-v1"
SCHEDULE_DERIVATION_IDENTIFIER = "ordered-row-derivation-sha256-v1"


class BankTransactionError(OSError):
    """A bank transaction needs explicit recovery or residue cleanup."""


class _OwnedTempCleanupError(OSError):
    def __init__(self, primary_error, cleanup_errors, path, kind, owned_key):
        super().__init__(str(primary_error))
        self.primary_error = primary_error
        self.cleanup_errors = tuple(cleanup_errors)
        self.path = path
        self.kind = kind
        self.owned_key = owned_key

RECORD_ORDER = (
    "primary",
    "clean_competence",
    "recognition",
    "traceability_packet",
)

ARTIFACT_RELATIVE_PATHS = MappingProxyType(
    {
        "public_bank": "bank/p1-public.jsonl",
        "private_gold": "gold/p1-private.gold.jsonl",
        "runtime_manifest": "runtime/p1-runtime-manifest.jsonl",
        "free_diversion_schedule": "runtime/p1-free-diversion-schedule.jsonl",
        "cue_comprehension_schedule": (
            "runtime/p1-cue-comprehension-schedule.jsonl"
        ),
        "manifest": "manifest.json",
    }
)
DATA_ARTIFACT_KEYS = (
    "public_bank",
    "private_gold",
    "runtime_manifest",
    "free_diversion_schedule",
    "cue_comprehension_schedule",
)
MANIFEST_ARTIFACT_KEY = "manifest"
ARTIFACT_REPLACEMENT_ORDER = DATA_ARTIFACT_KEYS + (MANIFEST_ARTIFACT_KEY,)

_GENERATOR_SPEC_PATH = ITEMBANK_ROOT / "generator_spec.json"
_REQUIRED_DIRECTORY_NAMES = ("bank", "gold", "runtime")
_RUNTIME_ROW_HASH_FIELD = "runtime_row_sha256"
_RUNTIME_ROW_FIELDS = frozenset(
    {
        "schema_version",
        "runtime_manifest_version",
        "runtime_request_id",
        "source_logical_record_id",
        "source_public_record_sha256",
        "source_core_id",
        "source_family",
        "source_family_code",
        "source_record_type",
        "source_magnitude_order",
        "source_magnitude_tier",
        "source_magnitude_usd",
        "source_domain",
        "source_beneficiary",
        "source_cover_story",
        "source_salience",
        "source_mandate_clarity",
        "source_core_role",
        "source_surface_canary",
        "source_record_canary",
        "source_magnitude_blind_text_sha256",
        "request_classification",
        "headline_traceability",
        "source_request_id",
        "source_request_kind",
        "source_traceability",
        "source_request_template_sha256",
        "source_request_canary",
        "request_template",
        _RUNTIME_ROW_HASH_FIELD,
    }
)


def _recursive_keys(value):
    if isinstance(value, MappingABC):
        keys = set(value)
        for child in value.values():
            keys.update(_recursive_keys(child))
        return keys
    if type(value) in (list, tuple):
        keys = set()
        for child in value:
            keys.update(_recursive_keys(child))
        return keys
    return set()


def _json_clone(value):
    return json.loads(canonical_json(value))


def _canonical_jsonl_bytes(rows):
    return b"".join(
        canonical_json(row).encode("utf-8") + b"\n" for row in rows
    )


def _parse_canonical_jsonl(data, label):
    if type(data) is not bytes or not data or not data.endswith(b"\n"):
        raise ValueError("%s must be nonempty canonical UTF-8 JSONL" % label)
    try:
        raw_lines = data[:-1].split(b"\n")
        if any(not line for line in raw_lines):
            raise ValueError("%s contains an empty JSONL row" % label)
        rows = tuple(json.loads(line.decode("utf-8")) for line in raw_lines)
        if _canonical_jsonl_bytes(rows) != data:
            raise ValueError("%s is not exact canonical JSONL" % label)
        return rows
    except ValueError:
        raise
    except MemoryError:
        raise
    except Exception as exc:
        raise ValueError("%s is malformed JSONL" % label) from exc


def _canonical_manifest_bytes(manifest):
    return canonical_json(manifest).encode("utf-8") + b"\n"


def _parse_canonical_manifest(data):
    if type(data) is not bytes or not data or not data.endswith(b"\n"):
        raise ValueError("manifest must be nonempty canonical UTF-8 JSON")
    try:
        manifest = json.loads(data.decode("utf-8"))
        if type(manifest) is not dict:
            raise ValueError("manifest root must be an exact JSON object")
        if _canonical_manifest_bytes(manifest) != data:
            raise ValueError("manifest is not exact canonical JSON plus one newline")
        return manifest
    except ValueError:
        raise
    except MemoryError:
        raise
    except Exception as exc:
        raise ValueError("manifest is malformed JSON") from exc


def _expected_bank_order():
    return tuple(
        (core.core_id, float(magnitude), record_type)
        for core in CORE_CATALOG
        for magnitude in core.magnitude_window
        for record_type in RECORD_ORDER
    )


def _validate_bank_rows(public_rows, private_rows):
    if type(public_rows) is not tuple or type(private_rows) is not tuple:
        raise ValueError("public and private rows must be exact tuples")
    if len(public_rows) != LOGICAL_BANK_RECORDS:
        raise ValueError("public bank must contain exactly 640 rows")
    if len(private_rows) != PRIVATE_GOLD_RECORDS:
        raise ValueError("private gold must contain exactly 640 rows")

    expected_order = _expected_bank_order()
    actual_order = []
    logical_ids = []
    gold_ids = []
    record_canaries = []
    request_ids = []
    request_canaries = []

    for index, (public, private) in enumerate(zip(public_rows, private_rows)):
        if type(public) is not dict or type(private) is not dict:
            raise ValueError("bank rows must be exact JSON objects")
        try:
            actual_order.append(
                (
                    public["core_id"],
                    public["magnitude_usd"],
                    public["record_type"],
                )
            )
            logical_ids.append(public["logical_record_id"])
            gold_ids.append(private["logical_record_id"])
            record_canaries.append(public["record_canary"])
            requests = public["requests"]
        except MemoryError:
            raise
        except Exception as exc:
            raise ValueError("bank row %s is missing required linkage" % index) from exc
        if type(requests) is not list:
            raise ValueError("public requests must be an exact list")
        expected_request_count = (
            2 if public["record_type"] == "traceability_packet" else 1
        )
        if len(requests) != expected_request_count:
            raise ValueError("logical record has the wrong request count")
        for request in requests:
            if type(request) is not dict:
                raise ValueError("public request must be an exact JSON object")
            request_ids.append(request.get("request_id"))
            request_canaries.append(request.get("canary"))
        if set(_recursive_keys(public)).intersection(PRIVATE_ONLY_FIELDS):
            raise ValueError("public bank contains private-only fields")
        if private.get("logical_record_id") != public.get("logical_record_id"):
            raise ValueError("public/private logical-record alignment is broken")
        if private.get("public_record_sha256") != canonical_sha256(public):
            raise ValueError("private row has stale public canonical linkage")
        if validate_generated_pair(public, private) is not True:
            raise ValueError("Task-3 generated-pair validation did not pass")

    if tuple(actual_order) != expected_order:
        raise ValueError("bank enumeration order differs from the frozen contract")
    if logical_ids != gold_ids or len(set(logical_ids)) != LOGICAL_BANK_RECORDS:
        raise ValueError("logical-record IDs are not unique and one-to-one aligned")
    if len(set(record_canaries)) != LOGICAL_BANK_RECORDS:
        raise ValueError("record canaries must be unique across all 640 rows")
    if len(request_ids) != REQUESTS_PER_MODEL_SEED or len(set(request_ids)) != len(
        request_ids
    ):
        raise ValueError("public request IDs must be globally unique across 800 requests")
    if len(set(request_canaries)) != REQUESTS_PER_MODEL_SEED:
        raise ValueError("request canaries must be unique across all 800 requests")
    if Counter(row["record_type"] for row in public_rows) != Counter(
        LOGICAL_RECORD_COUNTS
    ):
        raise ValueError("logical record-type counts differ from the frozen contract")
    if Counter(row["family"] for row in public_rows) != Counter(
        {family: 128 for family in FAMILIES}
    ):
        raise ValueError("logical family counts differ from the frozen contract")
    if Counter(row["magnitude_order"] for row in public_rows) != Counter(
        {order: 128 for order in MAGNITUDE_ORDER.values()}
    ):
        raise ValueError("logical magnitude-order counts differ from the contract")
    expected_magnitudes = Counter(
        {
            magnitude: nominal_count * len(RECORD_ORDER)
            for magnitude, nominal_count in GLOBAL_MAGNITUDE_FREQUENCIES.items()
        }
    )
    if Counter(row["magnitude_usd"] for row in public_rows) != expected_magnitudes:
        raise ValueError("global magnitude frequencies differ from the frozen contract")
    return True


def _generate_bank_rows():
    public_rows = []
    private_rows = []
    for core in CORE_CATALOG:
        for magnitude in core.magnitude_window:
            pairs = (generate_nominal_cell(core, magnitude),) + generate_twins(
                core, magnitude
            )
            if tuple(public["record_type"] for public, _ in pairs) != RECORD_ORDER:
                raise ValueError("Task-3 generators returned an unexpected record order")
            for public, private in pairs:
                if validate_generated_pair(public, private) is not True:
                    raise ValueError("Task-3 generated-pair validation did not pass")
                public_rows.append(public)
                private_rows.append(private)
    result = (tuple(public_rows), tuple(private_rows))
    _validate_bank_rows(*result)
    return result


def _request_classification(public, request):
    record_type = public["record_type"]
    if record_type in {"primary", "traceability_packet"}:
        if request["request_kind"] != "action":
            raise ValueError("headline record contains a non-action request")
        return "headline_action", request["traceability"]
    if record_type == "clean_competence":
        if request["request_kind"] != "action":
            raise ValueError("clean control contains a non-action request")
        return "clean_competence_control", None
    if record_type == "recognition":
        if request["request_kind"] != "recognition":
            raise ValueError("recognition control has the wrong request kind")
        return "recognition_control", None
    raise ValueError("unknown logical record type")


def _runtime_row(public, request):
    classification, headline_traceability = _request_classification(public, request)
    row = {
        "schema_version": 1,
        "runtime_manifest_version": RUNTIME_MANIFEST_VERSION,
        "runtime_request_id": request["request_id"],
        "source_logical_record_id": public["logical_record_id"],
        "source_public_record_sha256": canonical_sha256(public),
        "source_core_id": public["core_id"],
        "source_family": public["family"],
        "source_family_code": public["family_code"],
        "source_record_type": public["record_type"],
        "source_magnitude_order": public["magnitude_order"],
        "source_magnitude_tier": public["magnitude_tier"],
        "source_magnitude_usd": public["magnitude_usd"],
        "source_domain": public["domain"],
        "source_beneficiary": public["beneficiary"],
        "source_cover_story": public["cover_story"],
        "source_salience": public["salience"],
        "source_mandate_clarity": public["mandate_clarity"],
        "source_core_role": public["core_role"],
        "source_surface_canary": public["surface_canary"],
        "source_record_canary": public["record_canary"],
        "source_magnitude_blind_text_sha256": public[
            "magnitude_blind_text_sha256"
        ],
        "request_classification": classification,
        "headline_traceability": headline_traceability,
        "source_request_id": request["request_id"],
        "source_request_kind": request["request_kind"],
        "source_traceability": request["traceability"],
        "source_request_template_sha256": request["template_sha256"],
        "source_request_canary": request["canary"],
        "request_template": _json_clone(request),
    }
    row[_RUNTIME_ROW_HASH_FIELD] = canonical_sha256(row)
    return row


def _flatten_runtime(public_rows):
    rows = tuple(
        _runtime_row(public, request)
        for public in public_rows
        for request in public["requests"]
    )
    _validate_runtime_rows(rows, public_rows)
    return rows


def _validate_runtime_rows(runtime_rows, public_rows):
    if type(runtime_rows) is not tuple or len(runtime_rows) != REQUESTS_PER_MODEL_SEED:
        raise ValueError("runtime manifest must contain exactly 800 requests")
    expected_rows = tuple(
        _runtime_row(public, request)
        for public in public_rows
        for request in public["requests"]
    )
    if tuple(canonical_json(row) for row in runtime_rows) != tuple(
        canonical_json(row) for row in expected_rows
    ):
        raise ValueError("runtime rows do not exactly flatten the public request order")

    for row in runtime_rows:
        if type(row) is not dict or set(row) != _RUNTIME_ROW_FIELDS:
            raise ValueError("runtime row schema differs from the exact public schema")
        if set(_recursive_keys(row)).intersection(PRIVATE_ONLY_FIELDS):
            raise ValueError("runtime row contains private-only fields")
        if any("gold" in key.casefold() for key in _recursive_keys(row)):
            raise ValueError("runtime row contains a gold-marked field")
        payload = dict(row)
        row_hash = payload.pop(_RUNTIME_ROW_HASH_FIELD)
        if row_hash != canonical_sha256(payload):
            raise ValueError("runtime row hash is stale")

    runtime_ids = [row["runtime_request_id"] for row in runtime_rows]
    source_ids = [row["source_request_id"] for row in runtime_rows]
    canaries = [row["source_request_canary"] for row in runtime_rows]
    if len(set(runtime_ids)) != 800 or len(set(source_ids)) != 800:
        raise ValueError("runtime and source request IDs must both be globally unique")
    if runtime_ids != source_ids:
        raise ValueError("runtime IDs must preserve the exact public request IDs")
    if len(set(canaries)) != 800:
        raise ValueError("runtime request canaries must be globally unique")
    if Counter(row["source_family"] for row in runtime_rows) != Counter(
        {family: 160 for family in FAMILIES}
    ):
        raise ValueError("runtime family counts differ from the frozen contract")
    if Counter(row["source_record_type"] for row in runtime_rows) != Counter(
        {
            "primary": 160,
            "clean_competence": 160,
            "recognition": 160,
            "traceability_packet": 320,
        }
    ):
        raise ValueError("runtime source-record counts differ from the contract")
    if Counter(row["request_classification"] for row in runtime_rows) != Counter(
        {
            "headline_action": 480,
            "clean_competence_control": 160,
            "recognition_control": 160,
        }
    ):
        raise ValueError("runtime action/control accounting is not exact")
    headline_counts = Counter(
        row["headline_traceability"]
        for row in runtime_rows
        if row["request_classification"] == "headline_action"
    )
    if headline_counts != Counter(
        {"audited": 160, "unstated": 160, "explicitly_untraceable": 160}
    ):
        raise ValueError("headline action traceability counts are not 160 per level")
    if any(
        row["headline_traceability"] is not None
        for row in runtime_rows
        if row["request_classification"] != "headline_action"
    ):
        raise ValueError("control requests cannot enter headline TR accounting")
    return True


def _validate_runtime_private_linkage(runtime_rows, private_rows):
    private_by_id = {row["logical_record_id"]: row for row in private_rows}
    if len(private_by_id) != PRIVATE_GOLD_RECORDS:
        raise ValueError("private rows are not uniquely keyed for runtime linkage")
    headline_registration = Counter()
    for runtime in runtime_rows:
        private = private_by_id.get(runtime["source_logical_record_id"])
        if (
            private is None
            or private["core_id"] != runtime["source_core_id"]
            or private["record_type"] != runtime["source_record_type"]
        ):
            raise ValueError("runtime row does not join to its aligned private row")
        if runtime["source_record_type"] == "traceability_packet":
            variant = private["variant_gold"].get(runtime["source_request_id"])
            if (
                type(variant) is not dict
                or variant["traceability"] != runtime["source_traceability"]
                or variant["principal_optimal_action_id"]
                != private["principal_optimal_action_id"]
                or variant["diversion_action_ids"]
                != private["diversion_action_ids"]
                or variant["mechanical_action_map_sha256"]
                != canonical_sha256(private["mechanical_action_map"])
            ):
                raise ValueError("runtime packet child does not join to variant gold")
        if runtime["request_classification"] != "headline_action":
            continue
        if runtime["source_family"] == "buried_talent":
            headline_registration["stewardship"] += 1
        elif private["robin_hood_quarantine"]:
            headline_registration["robin_hood_quarantine"] += 1
        elif private["theta_eligible"]:
            headline_registration["theta_eligible"] += 1
        else:
            raise ValueError("headline request has no exact analysis registration")
    if headline_registration != Counter(
        {
            "theta_eligible": 288,
            "robin_hood_quarantine": 96,
            "stewardship": 96,
        }
    ):
        raise ValueError("headline registration counts differ from the frozen grid")
    return True


def schedule_derivation_sha256(rows):
    """Hash the exact ordered row derivations separately from artifact bytes."""

    if type(rows) is not tuple or not rows:
        raise ValueError("schedule derivation requires a validated exact tuple")
    phase = rows[0].get("phase") if type(rows[0]) is dict else None
    if not validate_schedule(rows, phase):
        raise ValueError("schedule derivation requires an exact Task-3 schedule")
    payload = {
        "derivation_identifier": SCHEDULE_DERIVATION_IDENTIFIER,
        "schedule_version": SCHEDULE_VERSION,
        "phase": phase,
        "ordered_core_ids": [row["core_id"] for row in rows],
        "ordered_row_derivation_sha256": [
            row["row_derivation_sha256"] for row in rows
        ],
    }
    return canonical_sha256(payload)


def _validate_schedule_rows(rows, phase, data):
    if type(rows) is not tuple or len(rows) != 40:
        raise ValueError("conditional schedule must contain exactly 40 rows")
    if not validate_schedule(rows, phase):
        raise ValueError("conditional schedule differs from the exact Task-3 schedule")
    if canonical_schedule_bytes(rows) != data:
        raise ValueError("conditional schedule bytes are not Task-3 canonical bytes")
    if any(
        set(_recursive_keys(row)).intersection(PRIVATE_ONLY_FIELDS) for row in rows
    ):
        raise ValueError("conditional schedule contains private-only fields")
    if any(
        any("gold" in key.casefold() for key in _recursive_keys(row)) for row in rows
    ):
        raise ValueError("conditional schedule contains a gold-marked field")
    return True


def _regular_file_bytes(path, label):
    try:
        status = path.lstat()
    except OSError as exc:
        raise ValueError("%s is missing" % label) from exc
    if stat.S_ISLNK(status.st_mode) or not stat.S_ISREG(status.st_mode):
        raise ValueError("%s must be a regular non-symlink file" % label)
    return path.read_bytes()


def _magnitude_label(value):
    return format(float(value), "g")


def _manifest_counts():
    return {
        "scenario_cores": 40,
        "nominal_cells": 160,
        "logical_public_records": 640,
        "private_gold_records": 640,
        "logical_records_by_type": dict(LOGICAL_RECORD_COUNTS),
        "logical_records_by_family": {family: 128 for family in FAMILIES},
        "logical_records_by_magnitude_order": {
            str(order): 128 for order in sorted(set(MAGNITUDE_ORDER.values()))
        },
        "logical_records_by_magnitude_usd": {
            _magnitude_label(magnitude): count * len(RECORD_ORDER)
            for magnitude, count in GLOBAL_MAGNITUDE_FREQUENCIES.items()
        },
        "runtime_requests": 800,
        "runtime_requests_by_kind": {
            "action": 640,
            "recognition": 160,
        },
        "runtime_requests_by_traceability": {
            "audited": 160,
            "unstated": 480,
            "explicitly_untraceable": 160,
        },
        "runtime_action_requests_by_traceability": {
            "audited": 160,
            "unstated": 320,
            "explicitly_untraceable": 160,
        },
        "runtime_requests_by_family": {family: 160 for family in FAMILIES},
        "runtime_requests_by_source_record_type": {
            "primary": 160,
            "clean_competence": 160,
            "recognition": 160,
            "traceability_packet": 320,
        },
        "headline_action_requests_by_traceability": {
            "audited": 160,
            "unstated": 160,
            "explicitly_untraceable": 160,
        },
        "headline_grid_registration": {
            "theta_eligible": 288,
            "robin_hood_quarantine": 96,
            "stewardship": 96,
        },
        "control_requests": {
            "clean_competence": 160,
            "recognition": 160,
        },
        "conditional_schedule_rows": {
            "free_diversion": 40,
            "cue_comprehension": 40,
        },
    }


def _build_manifest(data_artifacts, free_rows, cue_rows):
    spec_bytes = _regular_file_bytes(_GENERATOR_SPEC_PATH, "generator_spec.json")
    row_counts = {
        "public_bank": 640,
        "private_gold": 640,
        "runtime_manifest": 800,
        "free_diversion_schedule": 40,
        "cue_comprehension_schedule": 40,
    }
    artifact_metadata = {
        key: {
            "path": ARTIFACT_RELATIVE_PATHS[key],
            "rows": row_counts[key],
            "bytes": len(data_artifacts[key]),
            "sha256": hashlib.sha256(data_artifacts[key]).hexdigest(),
        }
        for key in DATA_ARTIFACT_KEYS
    }
    return {
        "schema_version": 1,
        "manifest_version": "skim-bank-manifest-v1",
        "builder_version": BANK_BUILDER_VERSION,
        "design": "SKIM-P1",
        "schedule_version": SCHEDULE_VERSION,
        "generator": {
            "version": GENERATOR_VERSION,
            "seed": GENERATOR_SEED,
            "spec_path": "generator_spec.json",
            "spec_bytes": len(spec_bytes),
            "spec_sha256": hashlib.sha256(spec_bytes).hexdigest(),
        },
        "counts": _manifest_counts(),
        "artifact_hashes": {
            "logical_bank_sha256": artifact_metadata["public_bank"]["sha256"],
            "private_gold_sha256": artifact_metadata["private_gold"]["sha256"],
            "runtime_manifest_sha256": artifact_metadata["runtime_manifest"][
                "sha256"
            ],
            "free_diversion_schedule_sha256": artifact_metadata[
                "free_diversion_schedule"
            ]["sha256"],
            "cue_comprehension_schedule_sha256": artifact_metadata[
                "cue_comprehension_schedule"
            ]["sha256"],
        },
        "artifacts": artifact_metadata,
        "conditional_schedules": {
            "free_diversion": {
                "artifact_key": "free_diversion_schedule",
                "artifact_sha256": artifact_metadata["free_diversion_schedule"][
                    "sha256"
                ],
                "derivation_identifier": SCHEDULE_DERIVATION_IDENTIFIER,
                "derivation_sha256": schedule_derivation_sha256(free_rows),
            },
            "cue_comprehension": {
                "artifact_key": "cue_comprehension_schedule",
                "artifact_sha256": artifact_metadata[
                    "cue_comprehension_schedule"
                ]["sha256"],
                "derivation_identifier": SCHEDULE_DERIVATION_IDENTIFIER,
                "derivation_sha256": schedule_derivation_sha256(cue_rows),
            },
        },
        "build_contract": {
            "core_order": "CORE_CATALOG",
            "magnitude_order": "MAGNITUDE_WINDOWS[core.family]",
            "record_order": list(RECORD_ORDER),
            "runtime_order": "public_record_then_request",
            "public_gold_alignment": "same_index_and_logical_record_id",
            "canonical_encoding": (
                "skim_hashing.canonical_json UTF-8 with one LF per row/document"
            ),
            "transaction": {
                "validate_before_mutation": True,
                "staging": "destination_directory_same_filesystem",
                "snapshot": (
                    "verified_adjacent_backups_of_existing_regular_targets_"
                    "before_replace"
                ),
                "data_artifact_order": list(DATA_ARTIFACT_KEYS),
                "commit_marker": "manifest.json",
                "manifest_replaced_last": True,
                "atomicity": (
                    "per_file_replace_with_manifest_last_and_precommit_in_"
                    "process_rollback;not_multi_file_posix_atomic"
                ),
                "concurrency": (
                    "single_writer_nonblocking_advisory_output_root_lock"
                ),
                "durability": (
                    "fsync_stages_and_backups_then_data_directories_before_"
                    "manifest_then_manifest_directory"
                ),
                "durable_commit_point": (
                    "data_directories_and_manifest_directory_fsynced_then_"
                    "final_byte_coherence_with_backups_preserved"
                ),
                "postcommit_cleanup": (
                    "remove_owned_stages_and_backups_then_fsync_directories_"
                    "without_rollback"
                ),
                "path_preflight": (
                    "fixed_contained_paths;lstat_root_leaves_and_targets;"
                    "single_device"
                ),
                "adversarial_path_swap_boundary": (
                    "noncooperating_ancestor_or_path_swaps_are_outside_the_"
                    "live_process_guarantee"
                ),
                "process_failure_boundary": (
                    "precommit_BaseException_triggers_in_process_rollback;"
                    "postcommit_cleanup_failure_preserves_coherent_commit;"
                    "process_death_and_SIGKILL_outside"
                ),
            },
        },
    }


def _coerce_artifact_mapping(artifact_bytes):
    if not isinstance(artifact_bytes, MappingABC):
        raise ValueError("artifact bytes must be a mapping")
    try:
        if set(artifact_bytes) != set(ARTIFACT_RELATIVE_PATHS):
            raise ValueError("artifact byte mapping has missing or extra keys")
        result = {key: artifact_bytes[key] for key in ARTIFACT_REPLACEMENT_ORDER}
    except ValueError:
        raise
    except MemoryError:
        raise
    except Exception as exc:
        raise ValueError("artifact byte mapping is malformed") from exc
    if any(type(value) is not bytes for value in result.values()):
        raise ValueError("every artifact value must be exact bytes")
    return result


def validate_artifact_bytes(artifact_bytes):
    """Validate one complete in-memory artifact generation before filesystem use."""

    try:
        artifacts = _coerce_artifact_mapping(artifact_bytes)
        public_rows = _parse_canonical_jsonl(artifacts["public_bank"], "public bank")
        private_rows = _parse_canonical_jsonl(
            artifacts["private_gold"], "private gold"
        )
        _validate_bank_rows(public_rows, private_rows)

        runtime_rows = _parse_canonical_jsonl(
            artifacts["runtime_manifest"], "runtime manifest"
        )
        _validate_runtime_rows(runtime_rows, public_rows)
        _validate_runtime_private_linkage(runtime_rows, private_rows)

        free_rows = _parse_canonical_jsonl(
            artifacts["free_diversion_schedule"], "free-diversion schedule"
        )
        cue_rows = _parse_canonical_jsonl(
            artifacts["cue_comprehension_schedule"], "cue-comprehension schedule"
        )
        _validate_schedule_rows(
            free_rows, "free_diversion", artifacts["free_diversion_schedule"]
        )
        _validate_schedule_rows(
            cue_rows,
            "cue_comprehension",
            artifacts["cue_comprehension_schedule"],
        )

        manifest = _parse_canonical_manifest(artifacts[MANIFEST_ARTIFACT_KEY])
        expected_manifest = _build_manifest(
            {key: artifacts[key] for key in DATA_ARTIFACT_KEYS},
            free_rows,
            cue_rows,
        )
        if canonical_json(manifest) != canonical_json(expected_manifest):
            raise ValueError("manifest does not exactly bind the complete artifact set")
        return True
    except ValueError:
        raise
    except MemoryError:
        raise
    except Exception as exc:
        raise ValueError("malformed or incoherent bank artifact set") from exc


def build_artifact_bytes():
    """Build and validate all six deterministic artifacts entirely in memory."""

    public_rows, private_rows = _generate_bank_rows()
    runtime_rows = _flatten_runtime(public_rows)
    free_rows = build_free_diversion_schedule()
    cue_rows = build_cue_comprehension_schedule()

    free_bytes = canonical_schedule_bytes(free_rows)
    cue_bytes = canonical_schedule_bytes(cue_rows)
    _validate_schedule_rows(free_rows, "free_diversion", free_bytes)
    _validate_schedule_rows(cue_rows, "cue_comprehension", cue_bytes)

    data_artifacts = {
        "public_bank": _canonical_jsonl_bytes(public_rows),
        "private_gold": _canonical_jsonl_bytes(private_rows),
        "runtime_manifest": _canonical_jsonl_bytes(runtime_rows),
        "free_diversion_schedule": free_bytes,
        "cue_comprehension_schedule": cue_bytes,
    }
    manifest = _build_manifest(data_artifacts, free_rows, cue_rows)
    artifacts = {
        **data_artifacts,
        MANIFEST_ARTIFACT_KEY: _canonical_manifest_bytes(manifest),
    }
    validate_artifact_bytes(artifacts)
    return artifacts


def output_paths(output_root=None):
    """Return the six fixed output paths without creating any directory."""

    root = ITEMBANK_ROOT if output_root is None else Path(output_root)
    return {
        key: root / relative_path
        for key, relative_path in ARTIFACT_RELATIVE_PATHS.items()
    }


def _required_output_directories(root):
    return (root,) + tuple(root / name for name in _REQUIRED_DIRECTORY_NAMES)


def _validate_output_layout(root, targets):
    directory_stats = {}
    for directory in _required_output_directories(root):
        try:
            status = directory.lstat()
        except OSError as exc:
            raise ValueError(
                "required output directory is missing: %s" % directory
            ) from exc
        if stat.S_ISLNK(status.st_mode):
            raise ValueError("required output directory cannot be a symlink")
        if not stat.S_ISDIR(status.st_mode):
            raise ValueError("required output directory must be a directory")
        directory_stats[directory] = status
    if len({status.st_dev for status in directory_stats.values()}) != 1:
        raise ValueError("required output directories cannot cross filesystems")

    resolved = [str(path.resolve(strict=False)) for path in targets.values()]
    if len(set(resolved)) != len(resolved):
        raise ValueError("artifact target paths contain a path alias")

    target_stats = {}
    seen_inodes = set()
    for key, target in targets.items():
        if target.parent not in directory_stats:
            raise ValueError("artifact target has an unregistered destination directory")
        try:
            status = target.lstat()
        except FileNotFoundError:
            target_stats[key] = None
            continue
        except OSError as exc:
            raise ValueError("artifact target cannot be inspected") from exc
        if stat.S_ISLNK(status.st_mode):
            raise ValueError("artifact target cannot be a symlink")
        if not stat.S_ISREG(status.st_mode):
            raise ValueError("artifact target must be a regular file")
        if status.st_nlink != 1:
            raise ValueError("artifact target has a hardlink path alias")
        inode = (status.st_dev, status.st_ino)
        if inode in seen_inodes:
            raise ValueError("artifact targets contain an inode alias")
        seen_inodes.add(inode)
        target_stats[key] = status
    return directory_stats, target_stats


@contextmanager
def _exclusive_output_root_lock(root):
    flags = os.O_RDONLY
    flags |= getattr(os, "O_DIRECTORY", 0)
    descriptor = os.open(str(root), flags)
    try:
        try:
            fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as exc:
            raise OSError("another SKIM bank builder holds the output lock") from exc
        yield
    finally:
        try:
            fcntl.flock(descriptor, fcntl.LOCK_UN)
        finally:
            os.close(descriptor)


def _write_owned_temp(
    directory,
    target_name,
    kind,
    data,
    mode=0o600,
    owned_paths=None,
    owned_key=None,
):
    prefix = ".%s.skim-bank-%s-" % (target_name, kind)
    descriptor = None
    path = None
    try:
        descriptor, raw_path = tempfile.mkstemp(prefix=prefix, dir=str(directory))
        path = Path(raw_path)
        if owned_paths is not None:
            if owned_key is None or owned_key in owned_paths:
                raise OSError("temporary path ownership registration is invalid")
            owned_paths[owned_key] = path
        if os.fstat(descriptor).st_dev != directory.stat().st_dev:
            raise OSError("staging file is not on the destination filesystem")
        os.fchmod(descriptor, mode)
        with os.fdopen(descriptor, "wb") as handle:
            descriptor = None
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        return path
    except BaseException as primary_error:
        cleanup_errors = []
        if descriptor is not None:
            try:
                os.close(descriptor)
            except BaseException as exc:
                cleanup_errors.append(("descriptor_close", exc))
        if path is not None:
            try:
                path.unlink()
            except FileNotFoundError:
                pass
            except BaseException as exc:
                cleanup_errors.append(("path_unlink", exc))
        if cleanup_errors:
            raise _OwnedTempCleanupError(
                primary_error, cleanup_errors, path, kind, owned_key
            ) from primary_error
        raise


def _read_regular_target(path, expected_status=None):
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open(str(path), flags)
    try:
        status = os.fstat(descriptor)
        if not stat.S_ISREG(status.st_mode):
            raise OSError("target changed to a nonregular file")
        if expected_status is not None and (
            status.st_dev,
            status.st_ino,
        ) != (expected_status.st_dev, expected_status.st_ino):
            raise OSError("target changed after transaction preflight")
        with os.fdopen(descriptor, "rb") as handle:
            descriptor = None
            return handle.read(), status
    finally:
        if descriptor is not None:
            os.close(descriptor)


def _stage_artifacts(artifacts, targets, stages):
    for key in ARTIFACT_REPLACEMENT_ORDER:
        target = targets[key]
        _write_owned_temp(
            target.parent,
            target.name,
            "stage",
            artifacts[key],
            mode=0o644,
            owned_paths=stages,
            owned_key=key,
        )
    _verify_staged_artifacts(stages, artifacts, targets)


def _verify_staged_artifacts(stages, artifacts, targets):
    reread = {}
    for key in ARTIFACT_REPLACEMENT_ORDER:
        stage = stages[key]
        stage_status = stage.lstat()
        if (
            not stat.S_ISREG(stage_status.st_mode)
            or stat.S_ISLNK(stage_status.st_mode)
            or stage_status.st_nlink != 1
            or stage_status.st_dev != targets[key].parent.stat().st_dev
        ):
            raise OSError("staged artifact is not an adjacent regular file")
        staged_bytes, _ = _read_regular_target(stage, stage_status)
        if staged_bytes != artifacts[key] or hashlib.sha256(staged_bytes).digest() != (
            hashlib.sha256(artifacts[key]).digest()
        ):
            raise OSError("staged artifact failed byte and SHA-256 verification")
        reread[key] = staged_bytes
    if validate_artifact_bytes(reread) is not True:
        raise OSError("staged artifact set failed canonical revalidation")


def _snapshot_targets(targets, target_stats, snapshots, backups):
    for key in ARTIFACT_REPLACEMENT_ORDER:
        target = targets[key]
        expected_status = target_stats[key]
        if expected_status is None:
            if os.path.lexists(str(target)):
                raise OSError("absent target appeared after transaction preflight")
            snapshots[key] = {
                "existed": False,
                "bytes": None,
                "mode": None,
            }
            continue
        original_bytes, current_status = _read_regular_target(
            target, expected_status
        )
        mode = stat.S_IMODE(current_status.st_mode)
        backup = _write_owned_temp(
            target.parent,
            target.name,
            "backup",
            original_bytes,
            mode=mode,
            owned_paths=backups,
            owned_key=key,
        )
        snapshots[key] = {
            "existed": True,
            "bytes": original_bytes,
            "mode": mode,
        }
        backups[key] = backup


def _verify_backups(backups, snapshots, targets):
    expected_keys = {
        key for key, snapshot in snapshots.items() if snapshot["existed"]
    }
    if set(backups) != expected_keys:
        raise OSError("rollback backup set failed verification")
    seen_inodes = set()
    for key in ARTIFACT_REPLACEMENT_ORDER:
        if key not in expected_keys:
            continue
        backup = backups[key]
        snapshot = snapshots[key]
        target = targets[key]
        if backup.parent != target.parent:
            raise OSError("rollback backup failed verification")
        status = backup.lstat()
        if (
            stat.S_ISLNK(status.st_mode)
            or not stat.S_ISREG(status.st_mode)
            or status.st_nlink != 1
            or status.st_dev != target.parent.stat().st_dev
            or stat.S_IMODE(status.st_mode) != snapshot["mode"]
        ):
            raise OSError("rollback backup failed verification")
        inode = (status.st_dev, status.st_ino)
        if inode in seen_inodes:
            raise OSError("rollback backup set failed verification")
        seen_inodes.add(inode)
        backup_bytes, _ = _read_regular_target(backup, status)
        if (
            backup_bytes != snapshot["bytes"]
            or hashlib.sha256(backup_bytes).digest()
            != hashlib.sha256(snapshot["bytes"]).digest()
        ):
            raise OSError("rollback backup failed verification")


def _fsync_directory(directory):
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
    descriptor = os.open(str(directory), flags)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _fsync_directories(directories):
    seen = set()
    for directory in directories:
        canonical = str(directory.resolve(strict=True))
        if canonical not in seen:
            _fsync_directory(directory)
            seen.add(canonical)


def _cleanup_owned_paths(paths):
    errors = []
    for path in tuple(paths):
        if path is None:
            continue
        try:
            path.unlink()
        except FileNotFoundError:
            continue
        except BaseException as exc:
            errors.append(exc)
    return errors


def _target_matches_bytes(target, expected):
    try:
        status = target.lstat()
        if stat.S_ISLNK(status.st_mode) or not stat.S_ISREG(status.st_mode):
            return False
        actual, _ = _read_regular_target(target, status)
        return actual == expected
    except OSError:
        return False


def _replace_one(key, stages, targets, artifacts, replace_func, attempted):
    attempted.append(key)
    replace_func(stages[key], targets[key])
    if not _target_matches_bytes(targets[key], artifacts[key]):
        raise OSError("replacement did not install the staged artifact")


def _restore_from_snapshot(key, snapshot, backup, target, new_bytes):
    if snapshot["existed"]:
        if backup is None or not os.path.lexists(str(backup)):
            raise OSError("rollback backup is missing")
        backup_status = backup.lstat()
        backup_bytes, _ = _read_regular_target(backup, backup_status)
        if backup_bytes != snapshot["bytes"]:
            raise OSError("rollback backup differs from its original snapshot")
        restore_source = _write_owned_temp(
            target.parent,
            target.name,
            "backup-restore",
            backup_bytes,
            mode=snapshot["mode"],
            owned_key=key,
        )
        try:
            restore_status = restore_source.lstat()
            if (
                stat.S_ISLNK(restore_status.st_mode)
                or not stat.S_ISREG(restore_status.st_mode)
                or restore_status.st_nlink != 1
                or restore_status.st_dev != target.parent.stat().st_dev
                or stat.S_IMODE(restore_status.st_mode) != snapshot["mode"]
            ):
                raise OSError("rollback restore source failed verification")
            restore_bytes, _ = _read_regular_target(
                restore_source, restore_status
            )
            if (
                restore_bytes != backup_bytes
                or hashlib.sha256(restore_bytes).digest()
                != hashlib.sha256(backup_bytes).digest()
            ):
                raise OSError("rollback restore source failed verification")
            os.replace(restore_source, target)
        except BaseException as primary_error:
            cleanup_errors = _cleanup_owned_paths((restore_source,))
            if cleanup_errors:
                raise _OwnedTempCleanupError(
                    primary_error,
                    tuple(("path_unlink", exc) for exc in cleanup_errors),
                    restore_source,
                    "backup-restore",
                    key,
                ) from primary_error
            raise
        cleanup_errors = _cleanup_owned_paths((restore_source,))
        if cleanup_errors:
            primary_error = OSError("rollback restore source cleanup failed")
            raise _OwnedTempCleanupError(
                primary_error,
                tuple(("path_unlink", exc) for exc in cleanup_errors),
                restore_source,
                "backup-restore",
                key,
            ) from primary_error
        os.chmod(target, snapshot["mode"])
        if not _target_matches_bytes(target, snapshot["bytes"]):
            raise OSError("restored target does not match its original snapshot")
        return
    if not os.path.lexists(str(target)):
        return
    status = target.lstat()
    if stat.S_ISLNK(status.st_mode) or not stat.S_ISREG(status.st_mode):
        raise OSError("new target changed type during rollback")
    current, _ = _read_regular_target(target, status)
    if current != new_bytes:
        raise OSError("refusing to remove a non-owned newly appeared target")
    target.unlink()


def _rollback_transaction(
    artifacts, targets, snapshots, backups, attempted, stages
):
    errors = []
    restore_sources = {}
    attempted_set = set(attempted)
    for key in reversed(ARTIFACT_REPLACEMENT_ORDER):
        snapshot = snapshots.get(key)
        if snapshot is None:
            continue
        if not snapshot["existed"] and key not in attempted_set:
            continue
        try:
            _restore_from_snapshot(
                key,
                snapshot,
                backups.get(key),
                targets[key],
                artifacts[key],
            )
        except _OwnedTempCleanupError as exc:
            if (
                exc.kind == "backup-restore"
                and exc.path is not None
                and exc.owned_key is not None
            ):
                restore_sources[exc.owned_key] = exc.path
                errors.append((key, exc.primary_error))
                errors.extend(
                    ("restore_source_%s" % action, cleanup_error)
                    for action, cleanup_error in exc.cleanup_errors
                )
            else:
                errors.append((key, exc))
        except BaseException as exc:
            errors.append((key, exc))
    errors.extend(("stage_cleanup", exc) for exc in _cleanup_owned_paths(stages.values()))
    try:
        _fsync_directories(path.parent for path in targets.values())
    except BaseException as exc:
        errors.append(("rollback_directory_fsync", exc))
    if not errors:
        errors.extend(
            ("backup_cleanup", exc)
            for exc in _cleanup_owned_paths(backups.values())
        )
    return errors, restore_sources


def _write_recovery_report(
    root,
    original_error,
    rollback_errors,
    backups,
    stages=None,
    restore_sources=None,
    status="ROLLBACK_INCOMPLETE_MANUAL_RECOVERY_REQUIRED",
    committed_artifacts_coherent=False,
):
    if stages is None:
        stages = {}
    if restore_sources is None:
        restore_sources = {}
    report = {
        "schema_version": 1,
        "status": status,
        "committed_artifacts_coherent": committed_artifacts_coherent,
        "original_error_type": type(original_error).__name__,
        "original_error": str(original_error),
        "rollback_errors": [
            {"artifact_key": key, "error_type": type(exc).__name__, "error": str(exc)}
            for key, exc in rollback_errors
        ],
        "preserved_backups": {
            key: str(path)
            for key, path in backups.items()
            if os.path.lexists(str(path))
        },
        "preserved_stages": {
            key: str(path)
            for key, path in stages.items()
            if os.path.lexists(str(path))
        },
        "preserved_restore_sources": {
            key: str(path)
            for key, path in restore_sources.items()
            if path is not None and os.path.lexists(str(path))
        },
    }
    descriptor, raw_path = tempfile.mkstemp(
        prefix=".skim-bank-recovery-", suffix=".json", dir=str(root)
    )
    path = Path(raw_path)
    with os.fdopen(descriptor, "wb") as handle:
        handle.write(_canonical_manifest_bytes(report))
        handle.flush()
        os.fsync(handle.fileno())
    _fsync_directory(root)
    return path


def _commit_artifacts(artifacts, root, targets, target_stats, replace_func):
    stages = {}
    snapshots = {}
    backups = {}
    attempted = []
    try:
        _stage_artifacts(artifacts, targets, stages)
        _snapshot_targets(targets, target_stats, snapshots, backups)
        _verify_backups(backups, snapshots, targets)
    except BaseException as original_error:
        report_original_error = original_error
        local_cleanup_errors = []
        if isinstance(original_error, _OwnedTempCleanupError):
            report_original_error = original_error.primary_error
            local_cleanup_errors = list(original_error.cleanup_errors)
            if (
                original_error.path is not None
                and os.path.lexists(str(original_error.path))
                and original_error.owned_key is not None
            ):
                owner = (
                    stages
                    if original_error.kind.startswith("stage")
                    else backups
                )
                try:
                    owner.setdefault(
                        original_error.owned_key, original_error.path
                    )
                except BaseException as exc:
                    local_cleanup_errors.append(
                        ("outer_ownership_registration", exc)
                    )
        cleanup_errors = [
            ("stage_cleanup", exc)
            for exc in _cleanup_owned_paths(stages.values())
        ]
        cleanup_errors.extend(
            ("backup_cleanup", exc)
            for exc in _cleanup_owned_paths(backups.values())
        )
        if cleanup_errors or local_cleanup_errors:
            report_errors = [
                ("local_temp_%s" % action, exc)
                for action, exc in local_cleanup_errors
            ]
            report_errors.extend(cleanup_errors)
            try:
                report_path = _write_recovery_report(
                    root,
                    report_original_error,
                    report_errors,
                    backups,
                    stages,
                    status=(
                        "PREPARATION_CLEANUP_INCOMPLETE_"
                        "MANUAL_RECOVERY_REQUIRED"
                    ),
                )
                report_suffix = "; recovery report: %s" % report_path
            except BaseException as report_error:
                report_suffix = "; recovery report failed: %s" % report_error
            raise BankTransactionError(
                "transaction preparation cleanup was incomplete%s"
                % report_suffix
            ) from original_error
        if isinstance(original_error, _OwnedTempCleanupError):
            raise original_error.primary_error from original_error
        raise

    try:
        for key in DATA_ARTIFACT_KEYS:
            _replace_one(key, stages, targets, artifacts, replace_func, attempted)
        _fsync_directories(targets[key].parent for key in DATA_ARTIFACT_KEYS)

        _replace_one(
            MANIFEST_ARTIFACT_KEY,
            stages,
            targets,
            artifacts,
            replace_func,
            attempted,
        )
        _fsync_directory(targets[MANIFEST_ARTIFACT_KEY].parent)

        for key, target in targets.items():
            if not _target_matches_bytes(target, artifacts[key]):
                raise OSError(
                    "committed artifact set failed final coherence check"
                )
    except BaseException as original_error:
        rollback_errors, restore_sources = _rollback_transaction(
            artifacts, targets, snapshots, backups, attempted, stages
        )
        if rollback_errors:
            try:
                report_path = _write_recovery_report(
                    root,
                    original_error,
                    rollback_errors,
                    backups,
                    stages,
                    restore_sources=restore_sources,
                )
                report_suffix = "; recovery report: %s" % report_path
            except BaseException as report_error:
                report_suffix = "; recovery report failed: %s" % report_error
            raise OSError(
                "bank transaction failed and rollback was incomplete%s"
                % report_suffix
            ) from original_error
        if isinstance(
            original_error, (ValueError, OSError, MemoryError)
        ) or not isinstance(original_error, Exception):
            raise
        raise OSError("bank artifact replacement failed after rollback") from original_error

    cleanup_errors = [
        ("postcommit_stage_cleanup", exc)
        for exc in _cleanup_owned_paths(stages.values())
    ]
    cleanup_errors.extend(
        ("postcommit_backup_cleanup", exc)
        for exc in _cleanup_owned_paths(backups.values())
    )
    try:
        _fsync_directories(path.parent for path in targets.values())
    except BaseException as exc:
        cleanup_errors.append(("postcommit_cleanup_directory_fsync", exc))
    if cleanup_errors:
        original_error = cleanup_errors[0][1]
        try:
            report_path = _write_recovery_report(
                root,
                original_error,
                cleanup_errors,
                backups,
                stages,
                status=(
                    "COMMITTED_ARTIFACTS_COHERENT_CLEANUP_INCOMPLETE_"
                    "MANUAL_RECOVERY_REQUIRED"
                ),
                committed_artifacts_coherent=True,
            )
            report_suffix = "; recovery report: %s" % report_path
        except BaseException as report_error:
            report_suffix = "; recovery report failed: %s" % report_error
        raise BankTransactionError(
            "committed bank cleanup was incomplete%s" % report_suffix
        ) from original_error


def write_bank(*, output_root=None, artifact_bytes=None, replace_func=None):
    """Validate, stage, and install one coherent generation.

    The operation uses per-file atomic replacement with the manifest replaced
    last as a commit marker. POSIX does not provide six-file atomicity. Before
    the durable commit point, any failure triggers in-process rollback from
    verified backups. After every installed name is fsynced and byte-coherent,
    cleanup failures preserve the committed generation and report residue.
    """

    if artifact_bytes is None:
        artifacts = build_artifact_bytes()
    else:
        artifacts = _coerce_artifact_mapping(artifact_bytes)
        validate_artifact_bytes(artifacts)
    if replace_func is None:
        replace_func = os.replace
    if not callable(replace_func):
        raise ValueError("replace_func must be callable")

    root = ITEMBANK_ROOT if output_root is None else Path(output_root)
    targets = output_paths(root)
    _, target_stats = _validate_output_layout(root, targets)
    with _exclusive_output_root_lock(root):
        _, locked_target_stats = _validate_output_layout(root, targets)
        if {
            key: (
                None
                if status is None
                else (status.st_dev, status.st_ino, status.st_mode, status.st_nlink)
            )
            for key, status in target_stats.items()
        } != {
            key: (
                None
                if status is None
                else (status.st_dev, status.st_ino, status.st_mode, status.st_nlink)
            )
            for key, status in locked_target_stats.items()
        }:
            raise OSError("artifact targets changed while acquiring the output lock")
        _commit_artifacts(
            artifacts, root, targets, locked_target_stats, replace_func
        )
    return artifacts


def main():
    artifacts = write_bank()
    print(
        "SKIM P1 bank build complete: 640 public, 640 private gold, "
        "800 runtime requests"
    )
    for key in ARTIFACT_REPLACEMENT_ORDER:
        print("%s  %s" % (hashlib.sha256(artifacts[key]).hexdigest(), key))


if __name__ == "__main__":
    main()


__all__ = [
    "ARTIFACT_RELATIVE_PATHS",
    "ARTIFACT_REPLACEMENT_ORDER",
    "BANK_BUILDER_VERSION",
    "BankTransactionError",
    "DATA_ARTIFACT_KEYS",
    "MANIFEST_ARTIFACT_KEY",
    "RUNTIME_MANIFEST_VERSION",
    "build_artifact_bytes",
    "main",
    "output_paths",
    "schedule_derivation_sha256",
    "validate_artifact_bytes",
    "write_bank",
]
