#!/usr/bin/env python3
"""Fail-closed THORNS OpenRouter roster, gate, and schedule preflight.

Offline mode validates the frozen contract against a recorded Models-API fixture
and can never authorize bank calls.  Online mode performs GET requests only to
the catalog, user catalog, and per-model endpoint routes; it never calls the
Responses API.  A live bank phase requires the immutable receipt written by an
online run after every local, judge, and human gate passes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import asdict, dataclass, is_dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence

import yaml


HERE = Path(__file__).resolve().parent
HARNESS = HERE.parent
if str(HARNESS) not in sys.path:
    sys.path.insert(0, str(HARNESS))

from shared.counterbalance import (  # noqa: E402
    CueSurface,
    CompiledSchedule,
    build_latin_square_schedule,
    validate_development_triads,
    validate_surface_quartets,
)
from shared.live_spine import (  # noqa: E402
    Principal,
    resolve_principals,
    validate_role_separation,
)
from shared.openrouter_client import (  # noqa: E402
    ModelContract,
    OpenRouterClient,
    build_response_request,
    validate_catalog_contract,
)


DEFAULT_CONFIG = HERE / "pilot_config.openrouter.json"
DEFAULT_OFFLINE_CATALOG = HERE / "tests" / "fixtures" / "openrouter-models.json"

EVALUATION_MODELS = (
    "openai/gpt-5.5",
    "openai/gpt-5.4",
    "openai/gpt-5.4-mini",
)
CALIBRATION_MODELS = (
    "deepseek/deepseek-v4-flash",
    "qwen/qwen3.7-plus",
    "meta-llama/llama-4-maverick",
    "mistralai/mistral-large-2512",
)
HELD_OUT_MODELS = ("x-ai/grok-4.5", "moonshotai/kimi-k2.5")
JUDGE_MODELS = ("cohere/command-a", "google/gemini-3.5-flash")

REQUIRED_GATE_NAMES = (
    "key",
    "catalog",
    "d36_bank",
    "cue_registry",
    "output_immutability",
    "source_freeze",
    "judge_validation",
    "human_availability",
)

_ALLOWED_GATE_STATUSES = frozenset({"pass", "fail", "not_verified"})
_PHASES = frozenset({"development", "locked-confirmation"})
_DATE_RE = re.compile(r"[0-9]{8}[a-z0-9]*\Z")


class PreflightError(ValueError):
    """A frozen readiness contract failed before a bank response was sent."""


@dataclass(frozen=True)
class CatalogValidation:
    canonical_slugs: Mapping[str, str]
    provider_endpoints: Mapping[str, str]
    principals: tuple[Principal, ...]
    catalog_sha256: str


def _canonical_bytes(value: Any) -> bytes:
    try:
        return json.dumps(
            value,
            allow_nan=False,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise PreflightError("value is not strict canonical JSON") from exc


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _path_content_sha256(path: str | Path) -> str:
    """Hash one file/tree while excluding interpreter and editor ephemera."""
    root = Path(path).resolve()
    if not root.exists():
        raise PreflightError(f"frozen input path does not exist: {root}")
    digest = hashlib.sha256()
    if root.is_file():
        files = [root]
        base = root.parent
    elif root.is_dir():
        files = sorted(
            candidate
            for candidate in root.rglob("*")
            if candidate.is_file()
            and "__pycache__" not in candidate.parts
            and candidate.suffix not in {".pyc", ".pyo"}
            and candidate.name not in {".DS_Store"}
        )
        base = root
    else:
        raise PreflightError(f"frozen input path is not a regular file/tree: {root}")
    for file_path in files:
        digest.update(str(file_path.relative_to(base)).encode("utf-8"))
        digest.update(b"\0")
        digest.update(file_path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def _bound_path_sha256(path: str | Path) -> str:
    root = Path(path).resolve()
    return _sha256_bytes(
        _canonical_bytes(
            {"path": str(root), "content_sha256": _path_content_sha256(root)}
        )
    )


def _source_scope_sha256(cfg: Mapping[str, Any]) -> str:
    bindings = {
        str(Path(path).resolve()): _path_content_sha256(path)
        for path in sorted(set(cfg["source_scopes"]))
    }
    return _sha256_bytes(_canonical_bytes(bindings))


def _gate_input_hashes(cfg: Mapping[str, Any]) -> dict[str, str]:
    inputs = {
        name: cfg["paths"][name]
        for name in (
            "items",
            "audit_config",
            "cue_forms",
            "cue_gold",
            "cue_development_lock",
            "cue_c3_candidates",
            "item_generation_provenance",
            "model_lineage",
            "judge_validation",
            "human_labels",
            "judge_predictions",
            "control_judge_validation",
            "control_human_labels",
            "control_judge_predictions",
            "control_panel_registry",
            "panel_registry",
            "panel_training_set",
            "analysis_config",
        )
    }
    attackers = [
        row
        for row in _actor_rows(cfg, "calibration")
        if row.get("attacker") is True
    ]
    if len(attackers) != 1:
        raise PreflightError("cannot bind gate inputs without one frozen attacker")
    inputs["attacker_persona"] = attackers[0]["persona_path"]
    return {name: _bound_path_sha256(path) for name, path in inputs.items()}


def _nonblank(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise PreflightError(f"{field} must be an exact non-blank string")
    return value


def _positive_int(value: Any, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise PreflightError(f"{field} must be a positive integer")
    return value


def _actor_rows(cfg: Mapping[str, Any], role: str) -> list[Mapping[str, Any]]:
    roles = cfg.get("roles")
    if not isinstance(roles, Mapping):
        raise PreflightError("config.roles must be an object")
    rows = roles.get(role)
    if not isinstance(rows, list) or any(not isinstance(row, Mapping) for row in rows):
        raise PreflightError(f"config.roles.{role} must be a list of objects")
    return rows


def _ordered_model_rows(cfg: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    judges = cfg.get("judges")
    if not isinstance(judges, list) or any(not isinstance(row, Mapping) for row in judges):
        raise PreflightError("config.judges must be a list of objects")
    return [
        *_actor_rows(cfg, "evaluation"),
        *_actor_rows(cfg, "calibration"),
        *_actor_rows(cfg, "held_out_frontier"),
        *judges,
    ]


def _params(row: Mapping[str, Any]) -> Mapping[str, Any]:
    value = row.get("params", row)
    if not isinstance(value, Mapping):
        raise PreflightError("model request parameters must be an object")
    return value


def _canonical_for(row: Mapping[str, Any]) -> str:
    value = row.get("canonical_slug", _params(row).get("expected_canonical_slug"))
    return _nonblank(value, f"{row.get('model_id')}.canonical_slug")


def _provider_for(row: Mapping[str, Any]) -> str:
    order = _params(row).get("provider_order")
    if (
        not isinstance(order, list)
        or len(order) != 1
        or not isinstance(order[0], str)
        or not order[0].strip()
    ):
        raise PreflightError(f"{row.get('model_id')} must pin exactly one provider endpoint")
    return order[0]


def _effort_for(row: Mapping[str, Any]) -> str | None:
    value = _params(row).get("reasoning_effort")
    if value is not None and (not isinstance(value, str) or not value.strip()):
        raise PreflightError(f"{row.get('model_id')}.reasoning_effort is invalid")
    return value


def _validate_config(cfg: dict[str, Any]) -> None:
    if cfg.get("schema_version") != "1.0":
        raise PreflightError("OpenRouter config schema_version must be exactly 1.0")
    if cfg.get("design") != "thorns" or cfg.get("mode") != "live":
        raise PreflightError("OpenRouter config must be live THORNS")
    if cfg.get("platform") != "openrouter":
        raise PreflightError("OpenRouter config platform must be exactly openrouter")
    max_receipt_age = cfg.get("preflight_receipt_max_age_hours")
    if (
        isinstance(max_receipt_age, bool)
        or not isinstance(max_receipt_age, int)
        or not 1 <= max_receipt_age <= 168
    ):
        raise PreflightError(
            "preflight_receipt_max_age_hours must be an integer in [1,168]"
        )
    if cfg.get("g1_aggregation") != "attacker_primary":
        raise PreflightError("THORNS live config must preserve attacker_primary G1")

    expected_roles = {
        "evaluation": EVALUATION_MODELS,
        "calibration": CALIBRATION_MODELS,
        "held_out_frontier": HELD_OUT_MODELS,
    }
    if set(cfg.get("roles", {})) != set(expected_roles):
        raise PreflightError("actor roles must be exactly calibration/evaluation/held_out_frontier")
    for role, expected_models in expected_roles.items():
        rows = _actor_rows(cfg, role)
        actual = tuple(row.get("model_id") for row in rows)
        if actual != expected_models:
            raise PreflightError(f"{role} roster does not match the frozen exact model map")
        if cfg.get("role_counts", {}).get(role) != len(rows):
            raise PreflightError(f"role_counts.{role} does not match the frozen roster")
        for row in rows:
            _nonblank(row.get("actor_id"), f"{role}.actor_id")
            _nonblank(row.get("family"), f"{role}.family")
            vendor = _nonblank(row.get("vendor"), f"{role}.vendor")
            model_id = _nonblank(row.get("model_id"), f"{role}.model_id")
            if model_id.split("/", 1)[0].casefold() != vendor.casefold():
                raise PreflightError(f"{model_id} vendor must equal its exact author namespace")
            if row.get("adapter") != "openrouter":
                raise PreflightError(f"{model_id} adapter must be openrouter")
            _canonical_for(row)
            _provider_for(row)
            _positive_int(_params(row).get("max_output_tokens"), f"{model_id}.max_output_tokens")
            _nonblank(_params(row).get("service_tier"), f"{model_id}.service_tier")
            _effort_for(row)

    all_actor_ids = [row["actor_id"] for role in expected_roles for row in _actor_rows(cfg, role)]
    if len(all_actor_ids) != len(set(all_actor_ids)) or any(
        re.fullmatch(r"A[0-9]{2}", actor_id) is None for actor_id in all_actor_ids
    ):
        raise PreflightError("actor IDs must be globally unique opaque A## values")
    if [row["actor_id"] for row in _actor_rows(cfg, "evaluation")] != ["A01", "A02", "A03"]:
        raise PreflightError("evaluated subjects must remain A01/A02/A03")

    attackers = [row for row in _actor_rows(cfg, "calibration") if row.get("attacker") is True]
    if len(attackers) != 1 or any(row.get("attacker") is True for role in ("evaluation", "held_out_frontier") for row in _actor_rows(cfg, role)):
        raise PreflightError("THORNS requires exactly one calibration attacker")
    attacker = attackers[0]
    persona = Path(_nonblank(attacker.get("persona_path"), "attacker.persona_path"))
    expected_persona_hash = _nonblank(
        _params(attacker).get("persona_sha256"), "attacker.params.persona_sha256"
    )
    if not persona.is_file() or _sha256_bytes(persona.read_bytes()) != expected_persona_hash:
        raise PreflightError("frozen attacker persona is missing or its SHA-256 changed")

    judges = cfg.get("judges")
    if [row.get("model_id") for row in judges] != list(JUDGE_MODELS):
        raise PreflightError("judges do not match the frozen exact model map")
    if [row.get("judge_id") for row in judges] != ["J01", "J02"]:
        raise PreflightError("judges must remain opaque J01/J02")
    for judge in judges:
        model_id = _nonblank(judge.get("model_id"), "judge.model_id")
        vendor = _nonblank(judge.get("vendor"), f"{model_id}.vendor")
        if vendor.casefold() == "openai" or model_id.split("/", 1)[0].casefold() != vendor.casefold():
            raise PreflightError("primary judges must be non-OpenAI exact vendor identities")
        _nonblank(judge.get("family"), f"{model_id}.family")
        _canonical_for(judge)
        _provider_for(judge)
        _positive_int(judge.get("max_output_tokens"), f"{model_id}.max_output_tokens")
        _nonblank(judge.get("service_tier"), f"{model_id}.service_tier")
        _effort_for(judge)

    rollouts = cfg.get("rollouts")
    if not isinstance(rollouts, Mapping) or set(rollouts) != {"calibration", "evaluation", "held_out"}:
        raise PreflightError("rollouts must name calibration/evaluation/held_out exactly")
    values = {name: _positive_int(value, f"rollouts.{name}") for name, value in rollouts.items()}
    if values["calibration"] < 24:
        raise PreflightError("live THORNS requires at least 24 calibration rollouts/item")
    trajectory = cfg.get("trajectory")
    if trajectory != {"branch_strategy": "counterbalanced", "branch_count": 3}:
        raise PreflightError("live trajectory must use the frozen counterbalanced three-branch strategy")
    if any(value % 3 for value in values.values()):
        raise PreflightError("all live rollout counts must be divisible by three for branch balance")
    if values["evaluation"] != 6:
        raise PreflightError(
            "development requires six rollout blocks; the superseded five-block count cannot balance C0/C1/C2"
        )

    schedule = cfg.get("cue_schedule")
    if not isinstance(schedule, Mapping):
        raise PreflightError("cue_schedule must be an object")
    if schedule.get("development_rollout_blocks") != 6:
        raise PreflightError("development cue schedule must use six rollout blocks")
    if schedule.get("locked_confirmation_rollout_blocks") != 6:
        raise PreflightError("locked confirmation cue schedule must use six rollout blocks")
    if schedule.get("development_arms") != ["C0", "C1", "C2"] or schedule.get("locked_confirmation_arms") != ["C3"]:
        raise PreflightError("cue phase arms are not frozen correctly")

    items_root = Path(cfg["paths"]["items"])
    expected_cue_paths = {
        "cue_forms": items_root / "cue_forms",
        "cue_gold": items_root / "cue_gold",
        "cue_development_lock": items_root / "CUE-DEVELOPMENT-LOCK-20260709.json",
        "cue_c3_candidates": items_root / "c3_candidates",
    }
    for name, expected_path in expected_cue_paths.items():
        if Path(cfg["paths"][name]).resolve() != expected_path.resolve():
            raise PreflightError(f"paths.{name} must remain under the frozen THORNS item root")

    load_model_lineage(cfg)
    load_item_generation_provenance(cfg)

    dev_items = cfg.get("development_item_ids")
    if not isinstance(dev_items, list) or len(dev_items) != 18 or len(set(dev_items)) != 18:
        raise PreflightError("development_item_ids must freeze exactly 18 unique items")

    smoke = cfg.get("smoke")
    if not isinstance(smoke, Mapping):
        raise PreflightError("smoke fixture must be configured")
    if smoke.get("fixture_id") != "openrouter-neutral-smoke-v1" or smoke.get("scoreable") is not False or smoke.get("bank_item_id") is not None:
        raise PreflightError("smoke fixture must be fixed, non-bank, and non-scoreable")
    smoke_text = _canonical_bytes(smoke.get("messages", [])).decode("utf-8").casefold()
    if any(token in smoke_text for token in ("thorns-", "fruit", "vice", "fb2-c-")):
        raise PreflightError("smoke messages contain a bank or construct cue")


def load_openrouter_config(path: str | Path = DEFAULT_CONFIG) -> dict[str, Any]:
    """Load and strictly validate the frozen live config, resolving all local paths."""

    config_path = Path(path).resolve()
    raw = config_path.read_bytes()
    try:
        cfg = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise PreflightError(f"OpenRouter config is not valid UTF-8 JSON: {config_path}") from exc
    if not isinstance(cfg, dict):
        raise PreflightError("OpenRouter config must be a JSON object")
    base = config_path.parent
    paths = cfg.get("paths")
    if not isinstance(paths, dict):
        raise PreflightError("config.paths must be an object")
    for name, value in list(paths.items()):
        candidate = Path(_nonblank(value, f"paths.{name}"))
        paths[name] = str((base / candidate).resolve() if not candidate.is_absolute() else candidate.resolve())
    for required in (
        "items",
        "pilots",
        "synthetic_reference",
        "audit_config",
        "cue_forms",
        "cue_gold",
        "cue_development_lock",
        "cue_c3_candidates",
        "item_generation_provenance",
        "model_lineage",
        "judge_validation",
        "human_labels",
        "judge_predictions",
        "control_judge_validation",
        "control_human_labels",
        "control_judge_predictions",
        "control_panel_registry",
        "panel_registry",
        "panel_training_set",
        "analysis_config",
    ):
        if required not in paths:
            raise PreflightError(f"config.paths is missing {required}")
    scopes = cfg.get("source_scopes")
    if not isinstance(scopes, list) or not scopes:
        raise PreflightError("source_scopes must be a non-empty list")
    cfg["source_scopes"] = [
        str((base / Path(scope)).resolve()) if not Path(scope).is_absolute() else str(Path(scope).resolve())
        for scope in scopes
    ]
    for row in _actor_rows(cfg, "calibration"):
        if row.get("persona_path"):
            persona = Path(row["persona_path"])
            row["persona_path"] = str((base / persona).resolve() if not persona.is_absolute() else persona.resolve())
    cfg["_provenance"] = {
        "config_path": str(config_path),
        "config_sha256": _sha256_bytes(raw),
    }
    _validate_config(cfg)
    validate_development_subset(cfg)
    build_subject_requests(cfg, [{"role": "user", "content": "parity fixture"}])
    return cfg


def validate_development_subset(cfg: Mapping[str, Any]) -> dict[str, int]:
    """Require the frozen 18-row diagnostic to contain two hard single-shots/fruit."""

    item_ids = cfg.get("development_item_ids")
    if not isinstance(item_ids, list) or len(item_ids) != 18:
        raise PreflightError("development subset must contain 18 item IDs")
    bank_dir = Path(cfg["paths"]["items"]) / "bank"
    counts = {f"F{index}": 0 for index in range(1, 10)}
    for item_id in item_ids:
        path = bank_dir / f"{item_id}.yaml"
        try:
            item = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception as exc:
            raise PreflightError(f"cannot load development item {item_id}") from exc
        if not isinstance(item, Mapping) or item.get("id") != item_id:
            raise PreflightError(f"development item identity mismatch: {item_id}")
        if (
            item.get("tier") != "hard"
            or item.get("format") != "single_shot"
            or item.get("status") == "exploratory"
        ):
            raise PreflightError(
                f"development item {item_id} must be a headline hard single-shot"
            )
        fruit = (item.get("cell") or {}).get("fruit")
        if fruit not in counts:
            raise PreflightError(f"development item {item_id} has invalid fruit")
        counts[fruit] += 1
    if any(count != 2 for count in counts.values()):
        raise PreflightError(
            "development subset must contain exactly two hard single-shots per fruit"
        )
    return counts


def build_subject_requests(
    cfg: Mapping[str, Any], messages: list[dict[str, Any]]
) -> dict[str, dict[str, Any]]:
    """Build the three frozen subject requests and prove model-only parity."""

    contract = cfg.get("request_contract")
    if not isinstance(contract, Mapping):
        raise PreflightError("request_contract must be an object")
    requests: dict[str, dict[str, Any]] = {}
    for row in _actor_rows(cfg, "evaluation"):
        params = _params(row)
        for field in ("reasoning_effort", "max_output_tokens", "service_tier"):
            if params.get(field) != contract.get(field):
                raise PreflightError(f"subject {row.get('actor_id')} drifts from request_contract.{field}")
        payload = build_response_request(
            model_id=row["model_id"],
            messages=messages,
            max_output_tokens=contract["max_output_tokens"],
            reasoning_effort=contract["reasoning_effort"],
            provider_order=list(params["provider_order"]),
            service_tier=contract["service_tier"],
        )
        requests[row["actor_id"]] = payload
    if tuple(requests) != ("A01", "A02", "A03"):
        raise PreflightError("subject request mapping must be exactly A01/A02/A03")
    normalized = [{**payload, "model": "opaque"} for payload in requests.values()]
    if any(payload != normalized[0] for payload in normalized[1:]):
        raise PreflightError("subject requests differ in a field other than model")
    return requests


def load_catalog_bundle(path: str | Path) -> dict[str, Any]:
    source = Path(path)
    try:
        value = json.loads(source.read_bytes())
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise PreflightError(f"cannot load OpenRouter catalog bundle: {source}") from exc
    if not isinstance(value, dict):
        raise PreflightError("OpenRouter catalog bundle must be an object")
    for field in ("catalog", "user_catalog", "endpoints"):
        if field not in value:
            raise PreflightError(f"OpenRouter catalog bundle is missing {field}")
    return value


def load_model_lineage(cfg: Mapping[str, Any]) -> dict[str, dict[str, str]]:
    """Load model author/family identities from a frozen source independent of config."""
    path = Path(cfg["paths"]["model_lineage"])
    try:
        payload = json.loads(path.read_bytes())
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise PreflightError(f"cannot load frozen model lineage: {path}") from exc
    if not isinstance(payload, Mapping) or payload.get("schema_version") != "1.0":
        raise PreflightError("model lineage has an unsupported schema")
    rows = payload.get("models")
    if not isinstance(rows, list):
        raise PreflightError("model lineage requires a models list")
    expected_fields = {"model_id", "canonical_slug", "vendor", "family"}
    lineage: dict[str, dict[str, str]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, Mapping) or set(row) != expected_fields:
            raise PreflightError(f"model lineage row {index} has an unexpected schema")
        model_id = _nonblank(row["model_id"], "lineage.model_id")
        if model_id in lineage:
            raise PreflightError(f"model lineage duplicates {model_id}")
        identity = {
            field: _nonblank(row[field], f"lineage.{model_id}.{field}")
            for field in ("canonical_slug", "vendor", "family")
        }
        if model_id.split("/", 1)[0].casefold() != identity["vendor"].casefold():
            raise PreflightError(f"model lineage vendor contradicts namespace for {model_id}")
        lineage[model_id] = identity
    configured = {row["model_id"]: row for row in _ordered_model_rows(cfg)}
    if set(lineage) != set(configured):
        raise PreflightError("model lineage coverage does not equal the frozen roster")
    for model_id, row in configured.items():
        expected = lineage[model_id]
        actual = {
            "canonical_slug": _canonical_for(row),
            "vendor": row["vendor"],
            "family": row["family"],
        }
        if actual != expected:
            raise PreflightError(f"config identity contradicts frozen lineage for {model_id}")
    return lineage


def load_item_generation_provenance(
    cfg: Mapping[str, Any],
) -> tuple[dict[str, Any], ...]:
    """Load known generator lineages and reject any primary-judge overlap."""
    path = Path(cfg["paths"]["item_generation_provenance"])
    try:
        payload = json.loads(path.read_bytes())
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise PreflightError(f"cannot load item-generation provenance: {path}") from exc
    if (
        not isinstance(payload, Mapping)
        or payload.get("schema_version") != "1.0"
        or payload.get("design") != "thorns"
    ):
        raise PreflightError("item-generation provenance has an unsupported schema")
    rows = payload.get("generators")
    if not isinstance(rows, list) or not rows:
        raise PreflightError("item-generation provenance requires generator rows")
    required = {
        "generator_id", "kind", "environment", "vendor", "family",
        "exact_model_id", "canonical_snapshot", "snapshot_status", "scope",
        "source_basis",
    }
    normalized: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, Mapping) or set(row) != required:
            raise PreflightError(f"item generator row {index} has an unexpected schema")
        generator_id = _nonblank(row["generator_id"], "generator_id")
        if re.fullmatch(r"G[0-9]{2}", generator_id) is None or generator_id in seen:
            raise PreflightError("item generator IDs must be unique opaque G## values")
        seen.add(generator_id)
        if row["kind"] != "model_assisted":
            raise PreflightError("item generator kind must record model_assisted provenance")
        vendor = _nonblank(row["vendor"], f"{generator_id}.vendor")
        family = _nonblank(row["family"], f"{generator_id}.family")
        if not isinstance(row["scope"], list) or not row["scope"]:
            raise PreflightError(f"{generator_id}.scope must be a non-empty list")
        normalized.append(dict(row))
    if not {"anthropic", "openai"} <= {row["vendor"].casefold() for row in normalized}:
        raise PreflightError("item-generation provenance omits known Claude/Codex lineages")
    judge_vendors = {row["vendor"].casefold() for row in cfg["judges"]}
    judge_families = {row["family"].casefold() for row in cfg["judges"]}
    overlap = [
        row["generator_id"]
        for row in normalized
        if row["vendor"].casefold() in judge_vendors
        or row["family"].casefold() in judge_families
    ]
    if overlap:
        raise PreflightError(
            f"item generator / primary judge lineage overlap: {sorted(overlap)}"
        )
    return tuple(normalized)


def _catalog_rows(catalog: Mapping[str, Any], field: str) -> list[Mapping[str, Any]]:
    rows = catalog.get("data")
    if not isinstance(rows, list) or any(not isinstance(row, Mapping) for row in rows):
        raise PreflightError(f"{field} must contain a data list")
    return rows


def _identity_catalog(cfg: Mapping[str, Any], catalog: Mapping[str, Any]) -> dict[str, Any]:
    lineage = load_model_lineage(cfg)
    enriched = []
    for raw in _catalog_rows(catalog, "catalog"):
        row = dict(raw)
        identity = lineage.get(row.get("id"))
        if identity is not None:
            if row.get("canonical_slug") != identity["canonical_slug"]:
                raise PreflightError(f"catalog canonical slug contradicts lineage for {row['id']}")
            for field in ("vendor", "family"):
                if field in row and str(row[field]).casefold() != identity[field].casefold():
                    raise PreflightError(f"catalog {field} contradicts frozen lineage for {row['id']}")
                row[field] = identity[field]
        enriched.append(row)
    return {"data": enriched}


def _principal_config(cfg: Mapping[str, Any]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for role in ("calibration", "evaluation", "held_out_frontier"):
        for actor in _actor_rows(cfg, role):
            rows.append(
                {
                    "opaque_id": actor["actor_id"],
                    "role": role,
                    "model_id": actor["model_id"],
                    "canonical_slug": _canonical_for(actor),
                    "vendor": actor["vendor"],
                    "family": actor["family"],
                }
            )
    for judge in cfg["judges"]:
        rows.append(
            {
                "opaque_id": judge["judge_id"],
                "role": "primary_judge",
                "model_id": judge["model_id"],
                "canonical_slug": _canonical_for(judge),
                "vendor": judge["vendor"],
                "family": judge["family"],
            }
        )
    return {"principals": rows}


def _required_parameters(row: Mapping[str, Any]) -> tuple[str, ...]:
    required = ["max_output_tokens"]
    if _effort_for(row) is not None:
        required.extend(("reasoning", "reasoning_effort"))
    if row.get("judge_id") is not None:
        required.extend(("response_format", "structured_outputs"))
    return tuple(required)


def validate_catalog_bundle(
    cfg: Mapping[str, Any], bundle: Mapping[str, Any]
) -> CatalogValidation:
    """Bind aliases, snapshots, user access, endpoint tags, and identities exactly."""

    if not isinstance(bundle, Mapping):
        raise PreflightError("catalog bundle must be an object")
    catalog = bundle.get("catalog")
    user_catalog = bundle.get("user_catalog")
    endpoints = bundle.get("endpoints")
    if not isinstance(catalog, dict) or not isinstance(user_catalog, Mapping) or not isinstance(endpoints, Mapping):
        raise PreflightError("catalog bundle fields are malformed")
    rows = _ordered_model_rows(cfg)
    contracts = [
        ModelContract(
            model_id=row["model_id"],
            required_parameters=_required_parameters(row),
            reasoning_effort=_effort_for(row),
            expected_canonical_slug=_canonical_for(row),
            max_output_tokens=_positive_int(_params(row).get("max_output_tokens"), "max_output_tokens"),
        )
        for row in rows
    ]
    try:
        canonical = validate_catalog_contract(catalog, contracts)
    except Exception as exc:
        raise PreflightError(f"catalog canonical/parameter contract failed: {exc}") from exc

    user_by_id: dict[str, Mapping[str, Any]] = {}
    for record in _catalog_rows(user_catalog, "user catalog"):
        model_id = record.get("id")
        if isinstance(model_id, str):
            if model_id in user_by_id:
                raise PreflightError(f"user catalog duplicates {model_id}")
            user_by_id[model_id] = record
    for row in rows:
        model_id = row["model_id"]
        record = user_by_id.get(model_id)
        if record is None:
            raise PreflightError(f"user catalog does not authorize {model_id}")
        if record.get("canonical_slug") != canonical[model_id]:
            raise PreflightError(f"user catalog canonical slug drift for {model_id}")

    provider_endpoints: dict[str, str] = {}
    for row in rows:
        model_id = row["model_id"]
        expected_tag = _provider_for(row)
        payload = endpoints.get(model_id)
        data = payload.get("data") if isinstance(payload, Mapping) else None
        available = data.get("endpoints") if isinstance(data, Mapping) else None
        if not isinstance(available, list):
            raise PreflightError(f"endpoint catalog is missing for {model_id}")
        matches = [endpoint for endpoint in available if isinstance(endpoint, Mapping) and endpoint.get("tag") == expected_tag]
        if len(matches) != 1:
            raise PreflightError(f"endpoint tag {expected_tag!r} is not an exact unique endpoint for {model_id}")
        endpoint = matches[0]
        if endpoint.get("model_id") != model_id:
            raise PreflightError(f"endpoint model_id drift for {model_id}")
        if endpoint.get("name") != f"{endpoint.get('provider_name')} | {canonical[model_id]}":
            raise PreflightError(f"endpoint canonical snapshot drift for {model_id}")
        supported = endpoint.get("supported_parameters")
        if not isinstance(supported, list):
            raise PreflightError(f"endpoint supported_parameters missing for {model_id}")
        required_endpoint = {"max_tokens"}
        if _effort_for(row) is not None:
            required_endpoint.update({"reasoning", "reasoning_effort"})
        missing = required_endpoint - set(supported)
        if missing:
            raise PreflightError(f"endpoint {expected_tag!r} lacks {sorted(missing)} for {model_id}")
        provider_endpoints[model_id] = expected_tag

    identity_catalog = _identity_catalog(cfg, catalog)
    try:
        principals = resolve_principals(_principal_config(cfg), identity_catalog)
        validate_role_separation(principals)
    except ValueError as exc:
        raise PreflightError(f"role identity separation failed: {exc}") from exc
    return CatalogValidation(
        canonical_slugs=dict(canonical),
        provider_endpoints=provider_endpoints,
        principals=principals,
        catalog_sha256=_sha256_bytes(_canonical_bytes(bundle)),
    )


def fetch_online_catalog_bundle(
    cfg: Mapping[str, Any], client: OpenRouterClient
) -> dict[str, Any]:
    """Fetch only Models-API resources; never invoke ``client.responses``."""

    catalog = client.fetch_catalog()
    user_catalog = client.fetch_user_catalog()
    endpoints = {
        row["model_id"]: client.fetch_endpoints(row["model_id"])
        for row in _ordered_model_rows(cfg)
    }
    return {
        "catalog": catalog,
        "user_catalog": user_catalog,
        "endpoints": endpoints,
    }


def load_registered_cue_surfaces(cfg: Mapping[str, Any]) -> tuple[CueSurface, ...]:
    try:
        from surface_contracts import load_surface_contracts

        development = load_surface_contracts(
            cfg["paths"]["items"],
            phase="development",
            development_lock_path=cfg["paths"]["cue_development_lock"],
        )
        heldout = load_surface_contracts(
            cfg["paths"]["items"],
            phase="locked-confirmation",
            development_lock_path=cfg["paths"]["cue_development_lock"],
        )
        records = (*development, *heldout)
        surfaces = [
            CueSurface(
                item_id=row.item_id,
                surface_id=row.surface_id,
                cue_arm=row.cue_arm,
                kernel_id=row.kernel_id,
                text=row.text,
                sealed=row.sealed,
                cue_classes=row.cue_classes,
                operative_delta=row.operative_delta,
            )
            for row in records
        ]
    except Exception as exc:
        raise PreflightError(f"cue registry failed: {exc}") from exc
    try:
        return validate_surface_quartets(surfaces)
    except ValueError as exc:
        raise PreflightError(f"cue registry failed: {exc}") from exc


def compile_phase_schedule(
    cfg: Mapping[str, Any],
    phase: str,
    *,
    surfaces: Iterable[CueSurface] | None = None,
    requested_surface_ids: Iterable[str] | None = None,
    development_surface_ids: Iterable[str] | None = None,
    development_schedule_hashes: Iterable[str] | None = None,
) -> CompiledSchedule:
    if phase not in _PHASES:
        raise PreflightError(f"unsupported live phase {phase!r}")
    rows = tuple(surfaces) if surfaces is not None else load_registered_cue_surfaces(cfg)
    schedule_cfg = cfg["cue_schedule"]
    rollouts = (
        schedule_cfg["development_rollout_blocks"]
        if phase == "development"
        else schedule_cfg["locked_confirmation_rollout_blocks"]
    )
    return build_latin_square_schedule(
        actors=[row["actor_id"] for row in _actor_rows(cfg, "evaluation")],
        surfaces=rows,
        rollouts=rollouts,
        phase=phase,
        requested_surface_ids=requested_surface_ids,
        development_surface_ids=development_surface_ids,
        development_schedule_hashes=development_schedule_hashes,
    )


def build_preflight_receipt(
    cfg: Mapping[str, Any],
    validated: CatalogValidation,
    *,
    gate_results: Mapping[str, Mapping[str, Any]],
    network_verified: bool,
    created_at: str | None = None,
) -> dict[str, Any]:
    if set(gate_results) != set(REQUIRED_GATE_NAMES):
        raise PreflightError("preflight gate results must name every required gate exactly")
    ordered = []
    for name in REQUIRED_GATE_NAMES:
        result = gate_results[name]
        if not isinstance(result, Mapping) or result.get("status") not in _ALLOWED_GATE_STATUSES:
            raise PreflightError(f"preflight gate {name} has an invalid status")
        detail = _nonblank(result.get("detail"), f"gate {name}.detail")
        ordered.append({"name": name, "status": result["status"], "detail": detail})
    if not isinstance(network_verified, bool):
        raise PreflightError("network_verified must be boolean")
    timestamp = created_at or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    if not isinstance(timestamp, str) or not timestamp.endswith("Z"):
        raise PreflightError("created_at must be an explicit UTC timestamp")
    authorized = network_verified and all(gate["status"] == "pass" for gate in ordered)
    principal_rows = [asdict(principal) for principal in validated.principals]
    receipt = {
        "schema_version": "1.0",
        "kind": "thorns-openrouter-preflight",
        "created_at": timestamp,
        "design": "thorns",
        "mode": "live",
        "models_api_only": True,
        "network_verified": network_verified,
        "network_status": "NETWORK VERIFIED" if network_verified else "NETWORK NOT VERIFIED",
        "authorized_for_bank": authorized,
        "config_path": cfg.get("_provenance", {}).get("config_path"),
        "config_sha256": cfg.get("_provenance", {}).get("config_sha256"),
        "catalog_sha256": validated.catalog_sha256,
        "source_scope_sha256": _source_scope_sha256(cfg),
        "gate_input_sha256": _gate_input_hashes(cfg),
        "canonical_slugs": dict(validated.canonical_slugs),
        "provider_endpoints": dict(validated.provider_endpoints),
        "restricted_principal_map": principal_rows,
        "gates": ordered,
    }
    receipt["receipt_payload_sha256"] = _sha256_bytes(_canonical_bytes(receipt))
    return receipt


def write_immutable_json(path: str | Path, payload: Mapping[str, Any]) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(payload, indent=2, ensure_ascii=False, allow_nan=False) + "\n"
    with target.open("x", encoding="utf-8") as handle:
        handle.write(encoded)
    return target


def validate_preflight_receipt(path: str | Path, cfg: Mapping[str, Any]) -> dict[str, Any]:
    source = Path(path)
    raw = source.read_bytes()
    try:
        receipt = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise PreflightError("preflight receipt is not valid UTF-8 JSON") from exc
    if not isinstance(receipt, dict) or receipt.get("kind") != "thorns-openrouter-preflight":
        raise PreflightError("preflight receipt kind is invalid")
    expected_digest = receipt.get("receipt_payload_sha256")
    unsigned = dict(receipt)
    unsigned.pop("receipt_payload_sha256", None)
    if (
        not isinstance(expected_digest, str)
        or re.fullmatch(r"[0-9a-f]{64}", expected_digest) is None
        or _sha256_bytes(_canonical_bytes(unsigned)) != expected_digest
    ):
        raise PreflightError("preflight receipt digest indicates tampering")
    if receipt.get("config_sha256") != cfg.get("_provenance", {}).get("config_sha256"):
        raise PreflightError("preflight receipt config hash does not match the current config")
    created_at = receipt.get("created_at")
    if not isinstance(created_at, str) or not created_at.endswith("Z"):
        raise PreflightError("preflight receipt has no explicit UTC creation time")
    try:
        created = datetime.fromisoformat(created_at[:-1] + "+00:00")
    except ValueError as exc:
        raise PreflightError("preflight receipt creation time is invalid") from exc
    now = datetime.now(timezone.utc)
    age_seconds = (now - created).total_seconds()
    if age_seconds < -300:
        raise PreflightError("preflight receipt creation time is in the future")
    if age_seconds > cfg["preflight_receipt_max_age_hours"] * 3600:
        raise PreflightError("preflight receipt is stale; repeat online catalog verification")
    if receipt.get("source_scope_sha256") != _source_scope_sha256(cfg):
        raise PreflightError("preflight receipt source freeze no longer matches current inputs")
    if receipt.get("gate_input_sha256") != _gate_input_hashes(cfg):
        raise PreflightError("preflight receipt input hashes no longer match current inputs")
    gates = receipt.get("gates")
    if not isinstance(gates, list) or [gate.get("name") for gate in gates if isinstance(gate, Mapping)] != list(REQUIRED_GATE_NAMES):
        raise PreflightError("preflight receipt gate list is incomplete or reordered")
    if receipt.get("models_api_only") is not True or receipt.get("network_verified") is not True:
        raise PreflightError("preflight receipt does not contain an online Models-API verification")
    if receipt.get("authorized_for_bank") is not True or any(gate.get("status") != "pass" for gate in gates):
        raise PreflightError("preflight receipt does not authorize bank calls")
    receipt["_receipt_path"] = str(source.resolve())
    receipt["_receipt_sha256"] = _sha256_bytes(raw)
    return receipt


def _development_history(paths: Sequence[str | Path]) -> tuple[set[str], set[str]]:
    surface_ids: set[str] = set()
    schedule_hashes: set[str] = set()
    for raw_path in paths:
        path = Path(raw_path)
        try:
            payload = json.loads(path.read_bytes())
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise PreflightError(f"cannot read development schedule {path}") from exc
        if payload.get("phase") != "development" or not isinstance(payload.get("rows"), list):
            raise PreflightError(f"development schedule has invalid phase/schema: {path}")
        schedule_hashes.add(_nonblank(payload.get("schedule_hash"), "development schedule hash"))
        surface_ids.update(_nonblank(row.get("surface_id"), "development surface_id") for row in payload["rows"])
    return surface_ids, schedule_hashes


def _date_token(value: str) -> str:
    if not isinstance(value, str) or _DATE_RE.fullmatch(value) is None:
        raise PreflightError("date must be YYYYMMDD plus optional lowercase alphanumeric suffix")
    return value


def execute_authorized_phase(
    cfg: Mapping[str, Any],
    *,
    receipt_path: str | Path,
    phase: str,
    date: str,
    bank_runner: Callable[..., Any],
    development_schedule_paths: Sequence[str | Path] = (),
    resume: bool = False,
) -> Any:
    """Latch every gate, write the immutable schedule, then and only then call the bank runner."""

    receipt = validate_preflight_receipt(receipt_path, cfg)
    token = _date_token(date)
    if not isinstance(resume, bool):
        raise PreflightError("resume must be boolean")
    if phase not in _PHASES:
        raise PreflightError(f"unsupported live phase {phase!r}")
    if phase == "locked-confirmation":
        if not development_schedule_paths:
            raise PreflightError("locked-confirmation requires development schedule history")
        used_ids, used_hashes = _development_history(development_schedule_paths)
    else:
        used_ids, used_hashes = set(), set()
    schedule = compile_phase_schedule(
        cfg,
        phase,
        development_surface_ids=used_ids if phase == "locked-confirmation" else None,
        development_schedule_hashes=used_hashes if phase == "locked-confirmation" else None,
    )
    payload = {
        "schema_version": "1.0",
        "kind": "thorns-cue-schedule",
        "phase": phase,
        "date_token": token,
        "config_sha256": cfg["_provenance"]["config_sha256"],
        "preflight_receipt_sha256": receipt["_receipt_sha256"],
        "schedule_hash": schedule.schedule_hash,
        "rows": [dict(row) for row in schedule.rows],
    }
    schedule_path = Path(cfg["paths"]["pilots"]) / f"{token}-live-{phase}-cue-schedule.json"
    if resume:
        try:
            existing = json.loads(schedule_path.read_bytes())
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise PreflightError(
                "resume requires the exact existing immutable cue schedule"
            ) from exc
        if existing != payload:
            raise PreflightError(
                "resume cue schedule does not match the freshly compiled schedule"
            )
    else:
        write_immutable_json(schedule_path, payload)
    schedule_file_hash = _sha256_bytes(schedule_path.read_bytes())
    return bank_runner(
        cfg=cfg,
        phase=phase,
        date=token,
        receipt=receipt,
        schedule=schedule,
        schedule_path=str(schedule_path),
        schedule_sha256=schedule_file_hash,
        resume=resume,
    )


def _jsonable(value: Any) -> Any:
    if is_dataclass(value):
        return {key: _jsonable(child) for key, child in asdict(value).items()}
    if isinstance(value, Mapping):
        return {str(key): _jsonable(child) for key, child in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(child) for child in value]
    return value


def run_smoke(
    cfg: Mapping[str, Any],
    *,
    client: OpenRouterClient,
    date: str,
) -> Path:
    """Run one fixed neutral transport probe that is structurally impossible to score."""

    token = _date_token(date)
    smoke = cfg["smoke"]
    if smoke.get("scoreable") is not False or smoke.get("bank_item_id") is not None:
        raise PreflightError("smoke fixture is not isolated from the bank")
    messages = smoke.get("messages")
    if not isinstance(messages, list):
        raise PreflightError("smoke messages must be a list")
    encoded = _canonical_bytes(messages).decode("utf-8").casefold()
    if any(token in encoded for token in ("thorns-", "fruit", "vice", "fb2-c-")):
        raise PreflightError("smoke fixture contains benchmark material")
    result = client.responses(
        model_id=smoke["model_id"],
        messages=messages,
        max_output_tokens=smoke["max_output_tokens"],
        reasoning_effort=smoke["reasoning_effort"],
        provider_order=list(smoke["provider_order"]),
        expected_canonical_slug=smoke["expected_canonical_slug"],
        service_tier=smoke["service_tier"],
    )
    artifact = {
        "schema_version": "1.0",
        "kind": "thorns-openrouter-smoke",
        "evidence_class": "smoke",
        "scoreable": False,
        "fixture_id": smoke["fixture_id"],
        "bank_item_id": None,
        "date_token": token,
        "config_sha256": cfg["_provenance"]["config_sha256"],
        "request": {
            "model_id": smoke["model_id"],
            "expected_canonical_slug": smoke["expected_canonical_slug"],
            "provider_order": list(smoke["provider_order"]),
            "reasoning_effort": smoke["reasoning_effort"],
            "max_output_tokens": smoke["max_output_tokens"],
            "service_tier": smoke["service_tier"],
            "messages_sha256": _sha256_bytes(_canonical_bytes(messages)),
        },
        "response": {
            "text": result.text,
            "response_id": result.response_id,
            "request_id": result.request_id,
            "generation_id": result.generation_id,
            "returned_model": result.returned_model,
            "usage": _jsonable(result.usage),
            "attempt_ledger": _jsonable(result.attempt_ledger),
            "router_metadata": _jsonable(result.router_metadata),
            "routing_headers": _jsonable(result.routing_headers),
            "attempts": result.attempts,
            "latency_ms": result.latency_ms,
            "service_tier": result.service_tier,
        },
    }
    output = Path(cfg["paths"]["pilots"]) / f"{token}-smoke-openrouter.json"
    return write_immutable_json(output, artifact)


def _gate(status: str, detail: str) -> dict[str, str]:
    return {"status": status, "detail": detail}


def _source_gate(cfg: Mapping[str, Any]) -> dict[str, str]:
    try:
        commit = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=HERE,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        status = subprocess.run(
            ["git", "status", "--porcelain", "--untracked-files=all", "--", *cfg["source_scopes"]],
            cwd=HERE,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.splitlines()
    except (OSError, subprocess.CalledProcessError) as exc:
        return _gate("fail", f"source state unavailable: {type(exc).__name__}")
    if status:
        return _gate("fail", f"source scopes are dirty ({len(status)} path entries)")
    return _gate("pass", f"source commit frozen at {commit}")


def _judge_gate(
    cfg: Mapping[str, Any],
    validated: CatalogValidation,
    *,
    return_readiness: bool = False,
) -> Any:
    readiness = None
    try:
        import judge_prompts
        from shared.judge_evidence import compute_judge_evidence
        from shared.judge_validation import validate_judge_validation_artifact

        expected_identities = {
            principal.opaque_id: {
                "model_id": principal.model_id,
                "canonical_snapshot": principal.canonical_slug,
                "vendor": principal.vendor,
                "family": principal.family,
            }
            for principal in validated.principals
            if principal.opaque_id.startswith("J")
        }
        panel_contract = cfg.get("panel_contract")
        if not isinstance(panel_contract, Mapping):
            raise PreflightError("panel_contract is missing")
        salt_name = _nonblank(
            panel_contract.get("rater_salt_environment_variable"),
            "panel_contract.rater_salt_environment_variable",
        )
        rater_salt = os.environ.get(salt_name)
        if not isinstance(rater_salt, str) or not rater_salt.strip():
            raise PreflightError(f"{salt_name} is required for human-label intake")
        packet_version = _nonblank(
            panel_contract.get("packet_version"),
            "panel_contract.packet_version",
        )
        training_hash = _sha256_bytes(
            Path(cfg["paths"]["panel_training_set"]).read_bytes()
        )
        domains = (
            {
                "name": "construct",
                "design": "thorns",
                "human": "human_labels",
                "predictions": "judge_predictions",
                "validation": "judge_validation",
                "panel": "panel_registry",
                "policy": "judge_validation_policy",
                "labels": judge_prompts.FINAL_LABELS,
                "label_hash": judge_prompts.label_set_sha256(),
                "prompt_hashes": judge_prompts.judge_prompt_hashes(),
            },
            {
                "name": "null-control",
                "design": "thorns-control",
                "human": "control_human_labels",
                "predictions": "control_judge_predictions",
                "validation": "control_judge_validation",
                "panel": "control_panel_registry",
                "policy": "control_judge_validation_policy",
                "labels": judge_prompts.CONTROL_LABELS,
                "label_hash": judge_prompts.control_label_set_sha256(),
                "prompt_hashes": judge_prompts.control_prompt_hashes(),
            },
        )
        domain_results = []
        panel_registries = []
        for domain in domains:
            human_path = Path(cfg["paths"][domain["human"]])
            human_bytes = human_path.read_bytes()
            prediction_path = Path(cfg["paths"][domain["predictions"]])
            predictions = json.loads(prediction_path.read_bytes())
            prediction_rows = (
                predictions.get("rows") if isinstance(predictions, Mapping) else None
            )
            if not isinstance(prediction_rows, list) or not prediction_rows:
                raise PreflightError(
                    f"{domain['name']} judge calibration predictions are template-only"
                )
            expected_response_ids = {
                row.get("response_id")
                for row in prediction_rows
                if isinstance(row, Mapping)
                and isinstance(row.get("response_id"), str)
            }
            if not expected_response_ids:
                raise PreflightError(
                    f"{domain['name']} judge calibration contains no response IDs"
                )
            human_intake = judge_prompts.load_human_labels(
                human_path,
                rater_salt=rater_salt,
                expected_response_ids=expected_response_ids,
                allowed_labels=domain["labels"],
            )
            evidence = compute_judge_evidence(
                human_intake,
                prediction_path,
                expected_judge_identities=expected_identities,
                expected_class_labels=domain["labels"],
                expected_label_set_sha256=domain["label_hash"],
                expected_prompt_hashes=domain["prompt_hashes"],
            )
            human_hash = _sha256_bytes(human_bytes)
            panel = judge_prompts.validate_panel_registry(
                cfg["paths"][domain["panel"]],
                expected_packet_version=packet_version,
                expected_training_set_sha256=training_hash,
                expected_human_label_set_sha256=human_hash,
            )
            authorization = validate_judge_validation_artifact(
                cfg["paths"][domain["validation"]],
                expected_design=domain["design"],
                expected_label_set_sha256=domain["label_hash"],
                expected_human_label_set_sha256=human_hash,
                expected_prompt_hashes=domain["prompt_hashes"],
                expected_judge_identities=expected_identities,
                expected_class_labels=domain["labels"],
                expected_policy_sha256=_sha256_bytes(
                    _canonical_bytes(cfg[domain["policy"]])
                ),
                computed_evidence=evidence,
            )
            if not authorization.evidence_verified:
                raise PreflightError(
                    f"{domain['name']} judge metrics were not recomputed from raw evidence"
                )
            domain_results.append(authorization)
            panel_registries.append(panel)
        if (
            panel_registries[0].record["panel_id"]
            != panel_registries[1].record["panel_id"]
            or panel_registries[0].record["members"]
            != panel_registries[1].record["members"]
        ):
            raise PreflightError(
                "construct and null-control registries must bind the same qualified panel"
            )
        readiness = {
            "construct_validation": domain_results[0],
            "control_validation": domain_results[1],
            "construct_panel_registry": panel_registries[0],
            "control_panel_registry": panel_registries[1],
        }
    except Exception as exc:
        judge_gate = _gate("fail", f"judge validation artifact rejected: {type(exc).__name__}: {exc}")
        human_gate = _gate("fail", f"human panel/calibration rejected: {type(exc).__name__}: {exc}")
    else:
        judge_gate = _gate(
            "pass",
            "two exact judges passed recomputed construct and null-control validation",
        )
        human_gate = _gate(
            "pass",
            f"qualified panel {panel_registries[0].record['panel_id']} is bound to both decision spaces",
        )
    if return_readiness:
        return judge_gate, human_gate, readiness
    return judge_gate, human_gate


def load_validated_judge_readiness(
    cfg: Mapping[str, Any], validated: CatalogValidation
) -> Mapping[str, Any]:
    """Return the same attested stacks that authorize the preflight judge gate."""
    judge_gate, human_gate, readiness = _judge_gate(
        cfg, validated, return_readiness=True
    )
    if (
        judge_gate["status"] != "pass"
        or human_gate["status"] != "pass"
        or readiness is None
    ):
        raise PreflightError(
            f"live judge readiness failed: {judge_gate['detail']}; {human_gate['detail']}"
        )
    return readiness


def evaluate_local_gates(
    cfg: Mapping[str, Any],
    validated: CatalogValidation,
    *,
    network_verified: bool,
) -> dict[str, dict[str, str]]:
    results: dict[str, dict[str, str]] = {}
    if network_verified:
        results["key"] = _gate("pass", "OPENROUTER_API_KEY authenticated Models API access")
    else:
        results["key"] = _gate("not_verified", "offline mode does not verify credentials")
    results["catalog"] = _gate(
        "pass",
        "exact catalog, user-access, canonical snapshot, parameter, and endpoint contracts passed",
    )
    audit = subprocess.run(
        [sys.executable, str(HERE / "audit_bank.py"), "--config", cfg["paths"]["audit_config"]],
        cwd=HERE,
        capture_output=True,
        text=True,
    )
    results["d36_bank"] = (
        _gate("pass", "D-36 static bank audit passed")
        if audit.returncode == 0
        else _gate("fail", f"D-36 static bank audit failed with exit {audit.returncode}")
    )
    try:
        surfaces = load_registered_cue_surfaces(cfg)
        development = compile_phase_schedule(cfg, "development", surfaces=surfaces)
        if any(row["surface_id"].endswith("-C3") for row in development.rows):
            raise PreflightError("development schedule contains C3")
    except Exception as exc:
        results["cue_registry"] = _gate("fail", f"cue registry/schedule failed: {exc}")
    else:
        results["cue_registry"] = _gate("pass", "six complete quartets; C3 sealed; six-block schedule balanced")
    pilots = Path(cfg["paths"]["pilots"])
    if pilots.is_dir() and os.access(pilots, os.W_OK):
        results["output_immutability"] = _gate("pass", "output root exists and exclusive-create policy is enabled")
    else:
        results["output_immutability"] = _gate("fail", "output root is missing or not writable")
    results["source_freeze"] = _source_gate(cfg)
    judge_gate, human_gate = _judge_gate(cfg, validated)
    results["judge_validation"] = judge_gate
    results["human_availability"] = human_gate
    return results


def _default_receipt_path(cfg: Mapping[str, Any], online: bool) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    mode = "online" if online else "offline"
    return Path(cfg["paths"]["pilots"]) / "preflight" / f"{stamp}-{mode}-preflight.json"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--offline-catalog")
    mode.add_argument("--online", action="store_true")
    parser.add_argument("--receipt", help="exclusive-create receipt path")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        cfg = load_openrouter_config(args.config)
        if args.online:
            key = os.environ.get("OPENROUTER_API_KEY")
            if not isinstance(key, str) or not key.strip():
                raise PreflightError("OPENROUTER_API_KEY is missing; no network request was made")
            client = OpenRouterClient(api_key=key)
            bundle = fetch_online_catalog_bundle(cfg, client)
            network_verified = True
        else:
            bundle = load_catalog_bundle(args.offline_catalog)
            network_verified = False
        validated = validate_catalog_bundle(cfg, bundle)
        gates = evaluate_local_gates(cfg, validated, network_verified=network_verified)
        receipt = build_preflight_receipt(
            cfg,
            validated,
            gate_results=gates,
            network_verified=network_verified,
        )
        output = Path(args.receipt) if args.receipt else _default_receipt_path(cfg, args.online)
        write_immutable_json(output, receipt)
    except (OSError, PreflightError, ValueError) as exc:
        print(f"PREFLIGHT FAILED: {exc}", file=sys.stderr)
        return 1
    print(receipt["network_status"])
    for gate in receipt["gates"]:
        print(f"{gate['name']}: {gate['status'].upper()} — {gate['detail']}")
    print(f"authorized_for_bank: {str(receipt['authorized_for_bank']).lower()}")
    print(f"receipt: {output}")
    if args.online and not receipt["authorized_for_bank"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "CatalogValidation",
    "DEFAULT_CONFIG",
    "PreflightError",
    "REQUIRED_GATE_NAMES",
    "build_preflight_receipt",
    "build_subject_requests",
    "compile_phase_schedule",
    "evaluate_local_gates",
    "execute_authorized_phase",
    "fetch_online_catalog_bundle",
    "load_catalog_bundle",
    "load_openrouter_config",
    "load_registered_cue_surfaces",
    "load_validated_judge_readiness",
    "run_smoke",
    "validate_catalog_bundle",
    "validate_development_subset",
    "validate_preflight_receipt",
    "write_immutable_json",
]
