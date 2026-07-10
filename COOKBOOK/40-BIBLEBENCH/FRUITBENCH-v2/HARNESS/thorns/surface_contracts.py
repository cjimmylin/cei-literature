"""Hash-bound THORNS cue surfaces and arm-typed private scoring contracts."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
from types import MappingProxyType
from typing import Any, Mapping, Sequence

import yaml


_SHA256_RE = re.compile(r"[0-9a-f]{64}\Z")
_CANARY_RE = re.compile(r"fb2-c-[0-9a-f]{12}\Z")
_DEVELOPMENT_ARMS = ("C0", "C1", "C2")
_CONSTRUCT_PATHS = ("fruit", "vice", "cft")
_CONTROL_LABELS = (
    "foil_correct",
    "target_action_false_positive",
    "indeterminate",
)
_REGISTERED_TARGET_FACTORS = {
    "construct_or_benchmark_label",
    "narrated_motive_or_polarity",
    "permission_prohibition_or_target_action",
    "authority_or_group_identity",
    "order_or_position",
    "register_or_style",
    "provenance_or_disclosure",
    "salience_or_retrieval_distance",
    "monitoring_or_evaluation_awareness",
}


@dataclass(frozen=True)
class SurfaceContract:
    item_id: str
    kernel_id: str
    surface_id: str
    cue_arm: str
    mode: str
    text: str
    text_sha256: str
    word_count: int
    c0_word_count: int
    headline_eligible: bool
    sealed: bool
    cue_classes: tuple[str, ...]
    operative_delta: str
    scoring_contract: Mapping[str, Any]
    development_lock_sha256: str
    author_provenance: Mapping[str, Any] | None = None


def _canonical(value: Any) -> bytes:
    return json.dumps(
        value,
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise ValueError(f"{field} must be an exact non-blank string")
    return value


def _sha(value: Any, field: str) -> str:
    if not isinstance(value, str) or _SHA256_RE.fullmatch(value) is None:
        raise ValueError(f"{field} must be a lowercase SHA-256")
    return value


def _load_yaml(path: Path, name: str) -> dict[str, Any]:
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValueError(f"cannot parse {name} {path.name}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{name} {path.name} must be an object")
    return value


def _freeze(value: Any) -> Any:
    if isinstance(value, Mapping):
        return MappingProxyType({str(key): _freeze(child) for key, child in value.items()})
    if isinstance(value, list):
        return tuple(_freeze(child) for child in value)
    return value


def validate_development_lock(
    lock_path: str | Path, items_root: str | Path
) -> Mapping[str, Any]:
    path = Path(lock_path).resolve()
    root = Path(items_root).resolve()
    try:
        lock = json.loads(path.read_bytes())
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("development lock is not valid JSON") from exc
    required = {
        "schema_version",
        "kind",
        "created_at",
        "status",
        "development_arms",
        "heldout_arm",
        "live_result_inputs",
        "files",
        "active_surface_bindings",
        "lock_payload_sha256",
    }
    if not isinstance(lock, dict) or set(lock) != required:
        raise ValueError("development lock has an unexpected schema")
    if (
        lock["schema_version"] != "1.0"
        or lock["kind"] != "thorns-cue-development-lock"
        or lock["status"] != "locked_before_any_live_development_result"
        or lock["development_arms"] != list(_DEVELOPMENT_ARMS)
        or lock["heldout_arm"] != "C3"
        or lock["live_result_inputs"] != []
    ):
        raise ValueError("development lock is not a pre-results C0/C1/C2 lock")
    digest = _sha(lock["lock_payload_sha256"], "lock_payload_sha256")
    unsigned = dict(lock)
    unsigned.pop("lock_payload_sha256")
    if hashlib.sha256(_canonical(unsigned)).hexdigest() != digest:
        raise ValueError("development lock payload hash indicates drift")
    files = lock["files"]
    if not isinstance(files, list) or len(files) != 12:
        raise ValueError("development lock must bind six sidecars and six cue-gold files")
    expected_paths: set[str] = set()
    for index, row in enumerate(files):
        if not isinstance(row, dict) or set(row) != {"path", "sha256"}:
            raise ValueError(f"development lock file row {index} is invalid")
        relative = _text(row["path"], f"files[{index}].path")
        if relative in expected_paths or Path(relative).is_absolute() or ".." in Path(relative).parts:
            raise ValueError("development lock file paths must be unique and relative")
        expected_paths.add(relative)
        expected_hash = _sha(row["sha256"], f"files[{index}].sha256")
        candidate = root / relative
        if not candidate.is_file() or hashlib.sha256(candidate.read_bytes()).hexdigest() != expected_hash:
            raise ValueError(f"development lock file hash drift: {relative}")
    if len([path for path in expected_paths if path.startswith("cue_forms/")]) != 6 or len(
        [path for path in expected_paths if path.startswith("cue_gold/")]
    ) != 6:
        raise ValueError("development lock file scope is incomplete")
    bindings = lock["active_surface_bindings"]
    if not isinstance(bindings, list) or len(bindings) != 18:
        raise ValueError("development lock must bind exactly 18 active surfaces")
    return _freeze(lock)


def _construct_contract(contract: Mapping[str, Any], field: str) -> dict[str, Any]:
    required = {
        "mode",
        "surface_id",
        "surface_text_sha256",
        "observable_path_markers",
        "trichotomous_rule",
        "rubric_0_4",
        "integration_flag",
    }
    if set(contract) != required or contract.get("mode") != "construct":
        raise ValueError(f"{field} construct contract has an unexpected schema")
    markers = contract["observable_path_markers"]
    if not isinstance(markers, dict) or set(markers) != set(_CONSTRUCT_PATHS):
        raise ValueError(f"{field} must define exactly fruit/vice/cft markers")
    for path_name, values in markers.items():
        if (
            not isinstance(values, list)
            or not values
            or any(not isinstance(value, str) or not value.strip() for value in values)
        ):
            raise ValueError(f"{field}.{path_name} markers must be non-empty strings")
    rubric = contract["rubric_0_4"]
    if not isinstance(rubric, dict) or {int(key) for key in rubric} != set(range(5)):
        raise ValueError(f"{field}.rubric_0_4 must contain exact anchors 0..4")
    if any(not isinstance(value, str) or not value.strip() for value in rubric.values()):
        raise ValueError(f"{field}.rubric_0_4 anchors must be non-empty strings")
    _text(contract["trichotomous_rule"], f"{field}.trichotomous_rule")
    if not isinstance(contract["integration_flag"], bool):
        raise ValueError(f"{field}.integration_flag must be boolean")
    _sha(contract["surface_text_sha256"], f"{field}.surface_text_sha256")
    return dict(contract)


def _null_contract(contract: Mapping[str, Any], field: str) -> dict[str, Any]:
    required = {
        "mode",
        "surface_id",
        "surface_text_sha256",
        "expected",
        "task_success_requirements",
        "observable_rules",
        "original_construct_labels_inapplicable",
        "integration_flag",
    }
    if set(contract) != required or contract.get("mode") != "null_control":
        raise ValueError(f"{field} null-control contract has an unexpected schema")
    if (
        contract["expected"] != "target_absent"
        or contract["original_construct_labels_inapplicable"] is not True
        or not isinstance(contract["integration_flag"], bool)
    ):
        raise ValueError(f"{field} does not declare a target-absent null control")
    requirements = contract["task_success_requirements"]
    if not isinstance(requirements, list) or not requirements or any(
        not isinstance(value, str) or not value.strip() for value in requirements
    ):
        raise ValueError(f"{field}.task_success_requirements must be non-empty strings")
    rules = contract["observable_rules"]
    if not isinstance(rules, dict) or tuple(rules) != _CONTROL_LABELS:
        raise ValueError(f"{field}.observable_rules must use the exact control labels")
    if any(
        not isinstance(values, list)
        or not values
        or any(not isinstance(value, str) or not value.strip() for value in values)
        for values in rules.values()
    ):
        raise ValueError(f"{field}.observable_rules must contain non-empty strings")
    _sha(contract["surface_text_sha256"], f"{field}.surface_text_sha256")
    return dict(contract)


def _word_count(text: str) -> int:
    return len(text.split())


def _binding_index(lock: Mapping[str, Any]) -> dict[str, str]:
    output: dict[str, str] = {}
    for row in lock["active_surface_bindings"]:
        if not isinstance(row, Mapping) or set(row) != {
            "item_id",
            "surface_id",
            "cue_arm",
            "text_sha256",
        }:
            raise ValueError("development lock contains an invalid surface binding")
        surface_id = _text(row["surface_id"], "lock surface_id")
        if surface_id in output:
            raise ValueError("development lock contains duplicate surface IDs")
        output[surface_id] = _sha(row["text_sha256"], "lock surface text hash")
    return output


def load_surface_contracts(
    items_root: str | Path,
    *,
    phase: str,
    development_lock_path: str | Path,
) -> tuple[SurfaceContract, ...]:
    root = Path(items_root).resolve()
    if phase not in {"development", "locked-confirmation"}:
        raise ValueError("phase must be development or locked-confirmation")
    lock = validate_development_lock(development_lock_path, root)
    lock_hash = lock["lock_payload_sha256"]
    locked_bindings = _binding_index(lock)
    sidecars = sorted((root / "cue_forms").glob("*.cue.yaml"))
    gold_files = sorted((root / "cue_gold").glob("*.cue.gold.yaml"))
    if len(sidecars) != 6 or len(gold_files) != 6:
        raise ValueError("THORNS requires six cue sidecars and six cue-gold files")
    gold_by_item = {
        path.name[: -len(".cue.gold.yaml")]: _load_yaml(path, "cue gold")
        for path in gold_files
    }
    development: list[SurfaceContract] = []
    metadata_by_item: dict[str, dict[str, Any]] = {}
    c0_counts: dict[str, int] = {}

    for sidecar_path in sidecars:
        sidecar = _load_yaml(sidecar_path, "cue sidecar")
        item_id = _text(sidecar.get("item_id"), f"{sidecar_path.name}.item_id")
        kernel_id = _text(sidecar.get("kernel_id"), f"{sidecar_path.name}.kernel_id")
        if sidecar.get("development_arms") != list(_DEVELOPMENT_ARMS):
            raise ValueError(f"{item_id} must declare exact development arms C0/C1/C2")
        status = sidecar.get("status")
        headline = sidecar.get("headline_eligible")
        if (status, headline) not in {("checked", True), ("exploratory", False)}:
            raise ValueError(f"{item_id} status/headline eligibility is inconsistent")
        targeted_factor = _text(
            sidecar.get("targeted_cue_factor"), f"{item_id}.targeted_cue_factor"
        )
        if targeted_factor not in _REGISTERED_TARGET_FACTORS:
            raise ValueError(f"{item_id} uses an unregistered targeted cue factor")
        levels = sidecar.get("factor_levels")
        if not isinstance(levels, dict) or tuple(levels) != _DEVELOPMENT_ARMS:
            raise ValueError(f"{item_id}.factor_levels must define C0/C1/C2")
        for arm, level in levels.items():
            base_level_keys = {
                "level_id",
                "realization",
                "salience_or_retrieval_distance",
            }
            position_keys = {"paragraph_span_1_based", "canary_whitespace_token_index_1_based"}
            if (
                not isinstance(level, dict)
                or set(level) - base_level_keys not in (
                    {"paragraph_span_1_based"},
                    {"canary_whitespace_token_index_1_based"},
                )
                or not base_level_keys <= set(level)
            ):
                raise ValueError(f"{item_id}.factor_levels.{arm} is invalid")
            for key in base_level_keys:
                value = level[key]
                _text(value, f"{item_id}.factor_levels.{arm}.{key}")
            extra_key = next(iter(set(level) & position_keys))
            position = level[extra_key]
            if extra_key == "paragraph_span_1_based":
                if (
                    not isinstance(position, list)
                    or len(position) != 2
                    or any(
                        isinstance(value, bool)
                        or not isinstance(value, int)
                        or value <= 0
                        for value in position
                    )
                    or position[0] > position[1]
                ):
                    raise ValueError(f"{item_id}.{arm} paragraph span is invalid")
            elif isinstance(position, bool) or not isinstance(position, int) or position <= 0:
                raise ValueError(f"{item_id}.{arm} canary token position is invalid")
        declared = sidecar.get("declared_cue_classes")
        if not isinstance(declared, dict) or targeted_factor not in declared or "salience_or_retrieval_distance" not in declared:
            raise ValueError(f"{item_id} does not declare its targeted factor and salience")
        canary_block = declared.get("construct_or_benchmark_label")
        canary = canary_block.get("canary") if isinstance(canary_block, dict) else None
        if not isinstance(canary, str) or _CANARY_RE.fullmatch(canary) is None:
            raise ValueError(f"{item_id} lacks one opaque canary")
        cue_gold = gold_by_item.get(item_id)
        if cue_gold is None or cue_gold.get("item_id") != item_id or cue_gold.get("kernel_id") != kernel_id:
            raise ValueError(f"{item_id} cue-gold identity mismatch")
        base_gold = cue_gold.get("base_gold")
        if not isinstance(base_gold, dict) or set(base_gold) != {
            "relative_path",
            "sha256",
            "hash_scope",
        } or base_gold.get("hash_scope") != "exact_file_bytes":
            raise ValueError(f"{item_id} base-gold binding is invalid")
        base_gold_path = (root / "cue_gold" / base_gold["relative_path"]).resolve()
        if root not in base_gold_path.parents or not base_gold_path.is_file() or hashlib.sha256(base_gold_path.read_bytes()).hexdigest() != _sha(base_gold["sha256"], f"{item_id}.base_gold.sha256"):
            raise ValueError(f"{item_id} base-gold hash drift")
        bank_path = root / "bank" / f"{item_id}.yaml"
        bank = _load_yaml(bank_path, "bank item")
        if bank.get("id") != item_id or bank.get("kernel_id") != kernel_id:
            raise ValueError(f"{item_id} bank identity mismatch")
        surfaces = sidecar.get("surfaces")
        if not isinstance(surfaces, list) or [row.get("cue_arm") for row in surfaces if isinstance(row, dict)] != list(_DEVELOPMENT_ARMS):
            raise ValueError(f"{item_id} must expose one ordered C0/C1/C2 development triad")
        contracts = cue_gold.get("contracts")
        if not isinstance(contracts, dict) or set(contracts) != {"C0", "C1", "C2", "C3"}:
            raise ValueError(f"{item_id} cue-gold contracts are incomplete")
        c0_text = surfaces[0].get("text")
        if c0_text != bank.get("prompt"):
            raise ValueError(f"{item_id} C0 text diverges from the bank prompt")
        c0_count = _word_count(c0_text)
        c0_counts[item_id] = c0_count
        metadata_by_item[item_id] = {
            "kernel_id": kernel_id,
            "headline": headline,
            "canary": canary,
            "targeted_factor": targeted_factor,
        }
        for surface in surfaces:
            if not isinstance(surface, dict):
                raise ValueError(f"{item_id} surface is not an object")
            arm = surface.get("cue_arm")
            surface_id = _text(surface.get("surface_id"), f"{item_id}.{arm}.surface_id")
            if surface.get("item_id") != item_id or surface.get("kernel_id") != kernel_id:
                raise ValueError(f"{surface_id} identity mismatch")
            text = surface.get("text")
            if not isinstance(text, str) or not text.strip() or text.count(canary) != 1:
                raise ValueError(f"{surface_id} must contain its canary exactly once")
            text_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
            if locked_bindings.get(surface_id) != text_hash:
                raise ValueError(f"{surface_id} text hash does not match the development lock")
            cue_classes = surface.get("cue_classes")
            if not isinstance(cue_classes, list) or targeted_factor not in cue_classes or "salience_or_retrieval_distance" not in cue_classes:
                raise ValueError(f"{surface_id} cue classes omit factor/salience controls")
            if len(cue_classes) != len(set(cue_classes)) or set(cue_classes) - _REGISTERED_TARGET_FACTORS:
                raise ValueError(f"{surface_id} cue classes are invalid")
            if surface.get("sealed") is not False:
                raise ValueError(f"{surface_id} development surface cannot be sealed")
            operative_delta = _text(surface.get("operative_delta"), f"{surface_id}.operative_delta")
            raw_contract = contracts[arm]
            if not isinstance(raw_contract, dict) or raw_contract.get("surface_id") != surface_id:
                raise ValueError(f"{surface_id} has no matching private contract")
            contract = (
                _null_contract(raw_contract, f"{item_id}.contracts.{arm}")
                if arm == "C2"
                else _construct_contract(raw_contract, f"{item_id}.contracts.{arm}")
            )
            if contract["surface_text_sha256"] != text_hash:
                raise ValueError(f"{surface_id} cue-gold surface hash drift")
            words = _word_count(text)
            if not 0.85 <= words / c0_count <= 1.15:
                raise ValueError(f"{surface_id} length is not within 15% of C0")
            development.append(
                SurfaceContract(
                    item_id=item_id,
                    kernel_id=kernel_id,
                    surface_id=surface_id,
                    cue_arm=arm,
                    mode=contract["mode"],
                    text=text,
                    text_sha256=text_hash,
                    word_count=words,
                    c0_word_count=c0_count,
                    headline_eligible=headline,
                    sealed=False,
                    cue_classes=tuple(cue_classes),
                    operative_delta=operative_delta,
                    scoring_contract=_freeze(contract),
                    development_lock_sha256=lock_hash,
                )
            )

    if set(gold_by_item) != set(metadata_by_item) or len(development) != 18:
        raise ValueError("development surface registry coverage is incomplete")
    if phase == "development":
        return tuple(sorted(development, key=lambda row: (row.item_id, row.cue_arm)))

    candidate_dir = root / "c3_candidates"
    candidates = sorted(candidate_dir.glob("*.yaml")) if candidate_dir.is_dir() else []
    if len(candidates) != 6:
        raise ValueError("locked-confirmation requires six independent C3 held-out candidates")
    heldout: list[SurfaceContract] = []
    for path in candidates:
        candidate = _load_yaml(path, "C3 candidate")
        item_id = candidate.get("item_id")
        metadata = metadata_by_item.get(item_id)
        if metadata is None:
            raise ValueError(f"unknown C3 held-out item {item_id!r}")
        expected_keys = {
            "schema_version",
            "item_id",
            "kernel_id",
            "cue_arm",
            "surface_id",
            "sealed",
            "status",
            "runnable",
            "headline_eligible",
            "canary",
            "author_provenance",
            "prompt",
            "word_count",
            "private_contract",
        }
        if set(candidate) != expected_keys:
            raise ValueError(f"{item_id} C3 candidate has an unexpected schema")
        surface_id = f"{item_id}-C3"
        if (
            candidate["schema_version"] != "1.0"
            or candidate["kernel_id"] != metadata["kernel_id"]
            or candidate["cue_arm"] != "C3"
            or candidate["surface_id"] != surface_id
            or candidate["sealed"] is not True
            or candidate["status"] != "independently_authored_heldout"
            or candidate["runnable"] is not True
            or candidate["headline_eligible"] is not metadata["headline"]
            or candidate["canary"] != metadata["canary"]
        ):
            raise ValueError(f"{item_id} C3 candidate identity/provenance fields drift")
        provenance = candidate["author_provenance"]
        if not isinstance(provenance, dict) or provenance.get("author_id") != "C3A01" or provenance.get("authoring_environment") != "independent_codex_agent" or provenance.get("development_lock_sha256") != lock_hash or provenance.get("authored_after_development_lock") is not True or provenance.get("live_results_observed") is not False:
            raise ValueError(f"{item_id} C3 was not independently authored after the lock")
        sources = provenance.get("source_files_read")
        if not isinstance(sources, list) or any("cue_forms" in str(value) or "cue_gold" in str(value) or "PILOTS" in str(value) for value in sources):
            raise ValueError(f"{item_id} C3 provenance includes prohibited development sources")
        text = candidate["prompt"]
        if not isinstance(text, str) or not text.strip() or text.count(metadata["canary"]) != 1:
            raise ValueError(f"{item_id} C3 must contain its canary exactly once")
        words = _word_count(text)
        if candidate["word_count"] != words or not 0.85 <= words / c0_counts[item_id] <= 1.15:
            raise ValueError(f"{item_id} C3 word count is not matched to C0")
        raw_contract = candidate["private_contract"]
        if not isinstance(raw_contract, dict):
            raise ValueError(f"{item_id} C3 contract must be an object")
        text_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        contract_with_binding = {
            **raw_contract,
            "surface_id": surface_id,
            "surface_text_sha256": text_hash,
        }
        contract = _construct_contract(contract_with_binding, f"{item_id}.C3.contract")
        heldout.append(
            SurfaceContract(
                item_id=item_id,
                kernel_id=metadata["kernel_id"],
                surface_id=surface_id,
                cue_arm="C3",
                mode="construct",
                text=text,
                text_sha256=text_hash,
                word_count=words,
                c0_word_count=c0_counts[item_id],
                headline_eligible=metadata["headline"],
                sealed=True,
                cue_classes=(
                    metadata["targeted_factor"],
                    "salience_or_retrieval_distance",
                    "provenance_or_disclosure",
                ),
                operative_delta="heldout: independently authored post-lock realization",
                scoring_contract=_freeze(contract),
                development_lock_sha256=lock_hash,
                author_provenance=_freeze(provenance),
            )
        )
    if len({row.item_id for row in heldout}) != 6:
        raise ValueError("C3 held-out candidates do not cover the six cue kernels")
    return tuple(sorted(heldout, key=lambda row: row.item_id))


def construct_gold_for_judge(surface: SurfaceContract) -> dict[str, Any]:
    if surface.mode != "construct":
        raise ValueError("construct gold is unavailable for a null-control surface")
    contract = surface.scoring_contract
    markers = contract["observable_path_markers"]
    return {
        "paths": {
            path_name: {"markers": list(markers[path_name])}
            for path_name in _CONSTRUCT_PATHS
        },
        "rubric_0_4": {
            int(score): description
            for score, description in contract["rubric_0_4"].items()
        },
        "integration_check": contract["integration_flag"],
    }


def control_rules_for_judge(surface: SurfaceContract) -> tuple[dict[str, str], ...]:
    if surface.mode != "null_control":
        raise ValueError("control rules are unavailable for a construct surface")
    rules = surface.scoring_contract["observable_rules"]
    return tuple(
        {
            "rule_id": f"N{index}",
            "control_label": label,
            "observable_basis": " | ".join(rules[label]),
        }
        for index, label in enumerate(_CONTROL_LABELS, start=1)
    )


__all__ = [
    "SurfaceContract",
    "construct_gold_for_judge",
    "control_rules_for_judge",
    "load_surface_contracts",
    "validate_development_lock",
]
