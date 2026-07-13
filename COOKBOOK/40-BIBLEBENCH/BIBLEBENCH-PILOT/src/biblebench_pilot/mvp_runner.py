"""Deterministic, no-spend PF-002 runner contracts and synthetic MVP runner.

This module has no live transport path. It validates a closed real-roster
proposal plus separately hash-bound owner authorization before transport could
be constructed. Its executable path remains restricted to the strict synthetic
manifest and produces only local, immutable, hash-chained synthetic artifacts.
"""

from __future__ import annotations

import argparse
from collections import Counter
from copy import deepcopy
from datetime import date
from decimal import Decimal
import hashlib
import json
import os
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator
import yaml

from .contracts import canonical_json_bytes, canonical_sha256
from .mvp_adapters import adapt_request
from .synthetic_provider import SCENARIOS, SyntheticProvider


PROVENANCE = "SYNTHETIC_VALIDATION_ONLY"
_ROOT = Path(__file__).resolve().parents[2]
_FIXTURE = _ROOT / "tests" / "fixtures" / "mvp-manifest-synthetic.json"
_MANIFEST_SCHEMA = _ROOT / "schemas" / "mvp-manifest.schema.json"
_PROPOSAL_SCHEMA = _ROOT / "schemas" / "mvp-proposal.schema.json"
_AUTHORIZATION_SCHEMA = _ROOT / "schemas" / "mvp-authorization.schema.json"
_OWNER_RECORD_SCHEMA = _ROOT / "schemas" / "mvp-owner-record.schema.json"
_ARTIFACT_SCHEMA = _ROOT / "schemas" / "mvp-artifact.schema.json"
_MODULES = ("fruitbench", "corinthlove", "tencommandments", "sermonmount")
_OUTPUT_FILES = (
    "manifest.json",
    "calls.json",
    "requests.json",
    "responses.json",
    "usage.json",
    "receipts.json",
    "missingness.json",
    "summary.json",
)

_REAL_ROUTE_ROSTER = {
    "actor-alpha": {
        "provider": "OpenAI",
        "model_id": "gpt-5-nano-2025-08-07",
        "route": {
            "provider_family": "generic_responses",
            "route_id": "openai/first-party/responses",
            "api_family": "responses",
            "first_party": True,
            "fallback_enabled": False,
        },
    },
    "actor-beta": {
        "provider": "Google",
        "model_id": "gemini-2.5-flash-lite",
        "route": {
            "provider_family": "generic_content",
            "route_id": "google/first-party/generate-content",
            "api_family": "generate_content",
            "first_party": True,
            "fallback_enabled": False,
        },
    },
    "actor-gamma": {
        "provider": "Anthropic",
        "model_id": "claude-haiku-4-5-20251001",
        "route": {
            "provider_family": "generic_messages",
            "route_id": "anthropic/first-party/messages",
            "api_family": "messages",
            "first_party": True,
            "fallback_enabled": False,
        },
    },
}


def _reject_duplicate_members(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate JSON member: {key}")
        value[key] = item
    return value


def _decode_json(source: str, *, label: str) -> dict[str, Any]:
    try:
        value = json.loads(source, object_pairs_hook=_reject_duplicate_members)
    except json.JSONDecodeError as error:
        raise ValueError(f"invalid {label}") from error
    if type(value) is not dict:
        raise ValueError(f"invalid {label}")
    return value


def _read_json(path: Path, *, label: str) -> dict[str, Any]:
    try:
        source = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise ValueError(f"invalid {label}") from error
    return _decode_json(source, label=label)


def _schema(path: Path) -> dict[str, Any]:
    schema = _read_json(path, label="schema")
    Draft202012Validator.check_schema(schema)
    return schema


def load_manifest(path: str | Path) -> dict[str, Any]:
    """Load a strict JSON manifest without granting it authority."""

    return _read_json(Path(path), label="MVP manifest")


def load_proposal(path: str | Path) -> dict[str, Any]:
    """Load a proposal contract with duplicate-member rejection."""

    return _read_json(Path(path), label="MVP proposal")


def load_authorization(path: str | Path) -> dict[str, Any]:
    """Load an authorization contract with duplicate-member rejection."""

    return _read_json(Path(path), label="MVP authorization")


def load_owner_record(path: str | Path) -> dict[str, Any]:
    """Load an external owner record with duplicate-member rejection."""

    return _read_json(Path(path), label="MVP owner record")


def _manifest_core(manifest: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in manifest.items() if key != "manifest_sha256"}


def _authorization_core(authorization: dict[str, Any]) -> dict[str, Any]:
    return {
        key: value
        for key, value in authorization.items()
        if key != "authorization_sha256"
    }


def _file_sha256(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError as error:
        raise ValueError("snapshot source missing") from error


def _combined_file_sha256(paths: tuple[Path, ...]) -> str:
    rows = [
        {
            "path": path.relative_to(_ROOT).as_posix(),
            "sha256": _file_sha256(path),
        }
        for path in paths
    ]
    return canonical_sha256(rows)


def _expected_snapshot_hashes(proposal: dict[str, Any]) -> dict[str, str]:
    banks = proposal["banks"]
    surface_rows = [
        {
            "module": bank["module"],
            "c1_surface_registry_sha256": bank["c1_surface_registry_sha256"],
        }
        for bank in banks
    ]
    request_rows = [
        {
            "module": bank["module"],
            "primary_request_registry_sha256": bank[
                "primary_request_registry_sha256"
            ],
            "probe_request_registry_sha256": bank["probe_request_registry_sha256"],
        }
        for bank in banks
    ]
    return {
        "bank_set_sha256": canonical_sha256(banks),
        "surface_registry_set_sha256": canonical_sha256(surface_rows),
        "request_registry_set_sha256": canonical_sha256(request_rows),
        "compiler_sha256": _file_sha256(
            _ROOT / "src" / "biblebench_pilot" / "mvp_runner.py"
        ),
        "adapter_sha256": _file_sha256(
            _ROOT / "src" / "biblebench_pilot" / "mvp_adapters.py"
        ),
        "proposal_schema_sha256": _file_sha256(_PROPOSAL_SCHEMA),
        "artifact_schema_sha256": _file_sha256(_ARTIFACT_SCHEMA),
        "analysis_contract_sha256": _combined_file_sha256(
            (
                _ROOT / "analysis" / "final-table-shells.csv",
                _ROOT / "analysis" / "figure-contracts.json",
            )
        ),
        "adjudication_contract_sha256": _file_sha256(
            _ROOT / "schemas" / "provisional-gold-review.schema.json"
        ),
    }


def _strict_decimal(value: Any, *, label: str) -> Decimal:
    if type(value) not in {int, float}:
        raise ValueError(f"invalid {label}")
    result = Decimal(str(value))
    if not result.is_finite() or result < 0:
        raise ValueError(f"invalid {label}")
    return result


def _parse_date(value: Any, *, label: str) -> date:
    try:
        return date.fromisoformat(value)
    except (TypeError, ValueError) as error:
        raise ValueError(f"invalid {label}") from error


def _decimal_text(value: Decimal) -> str:
    normalized = value.normalize()
    if normalized == 0:
        return "0"
    return format(normalized, "f")


def _proposal_costs(
    proposal: dict[str, Any],
) -> tuple[dict[str, Decimal], Decimal]:
    geometry = proposal["geometry"]
    actor_count = geometry["actor_count"]
    logical_calls = geometry["logical_call_count"]
    if logical_calls % actor_count:
        raise ValueError("invalid PF-002 geometry")
    calls_per_actor = logical_calls // actor_count
    attempts = proposal["retry_rule"]["maximum_attempts_per_logical_call"]
    route_costs: dict[str, Decimal] = {}
    total = Decimal("0")
    for actor in proposal["actors"]:
        caps = actor["token_caps"]
        price = actor["price"]
        input_price = _strict_decimal(price["input_usd"], label="input price")
        output_price = _strict_decimal(price["output_usd"], label="output price")
        cost = Decimal(calls_per_actor * attempts) * (
            Decimal(caps["max_input_tokens"]) * input_price
            + Decimal(caps["max_output_tokens"]) * output_price
        ) / Decimal("1000000")
        route_costs[actor["actor_alias"]] = cost
        total += cost
    return route_costs, total


def validate_proposal_contract(
    proposal: dict[str, Any],
    *,
    bank_root: Path,
    today: date | None = None,
) -> Decimal:
    """Validate a closed real-roster proposal without granting authority."""

    if type(proposal) is not dict:
        raise ValueError("invalid proposal manifest")
    if proposal.get("manifest_sha256") != canonical_sha256(_manifest_core(proposal)):
        raise ValueError("proposal manifest hash mismatch")
    if proposal.get("fallback_enabled") is not False or any(
        type(actor) is dict
        and type(actor.get("route")) is dict
        and actor["route"].get("fallback_enabled") is not False
        for actor in proposal.get("actors", [])
    ):
        raise ValueError("fallback must be disabled")
    budget = proposal.get("budget")
    if type(budget) is dict:
        if budget.get("hard_cap_usd") != 5:
            raise ValueError("hard cap must equal five dollars")
        if budget.get("not_to_exceed_usd") != 5:
            raise ValueError("proposal NTE must equal five dollars")
    errors = sorted(
        Draft202012Validator(_schema(_PROPOSAL_SCHEMA)).iter_errors(proposal),
        key=lambda error: list(error.path),
    )
    if errors:
        raise ValueError(f"invalid proposal schema: {errors[0].message}")
    current = today or date.today()
    proposal_expires = _parse_date(proposal["expires_on"], label="proposal expiry")
    if proposal_expires < current:
        raise ValueError("proposal expired")
    if proposal["geometry"] != {
        "actor_count": 3,
        "capability_twins": False,
        "episode_count": 48,
        "logical_call_count": 288,
        "primary_count": 144,
        "probe_count": 144,
    }:
        raise ValueError("invalid PF-002 geometry")
    if proposal["retry_rule"] != {
        "max_retries": 1,
        "maximum_attempts_per_logical_call": 2,
        "retryable_statuses": ["rate_limit"],
        "unknown_delivery_terminal": True,
    }:
        raise ValueError("invalid retry exposure")

    actors = proposal["actors"]
    registered_routes = {
        actor["actor_alias"]: {
            "provider": actor["provider"],
            "model_id": actor["model_id"],
            "route": actor["route"],
        }
        for actor in actors
    }
    if registered_routes != _REAL_ROUTE_ROSTER:
        raise ValueError("provider/model/adapter route mismatch")
    forbidden_identity_fragments = (
        "synthetic",
        "placeholder",
        "example",
        "unknown",
        "tbd",
        "wildcard",
        "*",
    )
    identity_rows = [
        (
            actor["provider"].casefold(),
            actor["model_id"].casefold(),
            actor["route"]["route_id"].casefold(),
        )
        for actor in actors
    ]
    if (
        len(set(identity_rows)) != 3
        or len({row[1] for row in identity_rows}) != 3
        or len({actor["actor_alias"] for actor in actors}) != 3
        or any(
            fragment in " ".join(row)
            for row in identity_rows
            for fragment in forbidden_identity_fragments
        )
    ):
        raise ValueError("exact real roster is required")
    for actor in actors:
        caps = actor["token_caps"]
        evidence_date = _parse_date(
            actor["price"]["evidence_date"], label="price evidence date"
        )
        if evidence_date > current or evidence_date > proposal_expires:
            raise ValueError("invalid price evidence date")
        if (
            caps["max_input_tokens"] > actor["context_window_tokens"]
            or caps["max_output_tokens"] > actor["maximum_supported_output_tokens"]
        ):
            raise ValueError("registered token cap exceeds model support")

    if [bank["module"] for bank in proposal["banks"]] != list(_MODULES):
        raise ValueError("invalid bank order")
    for bank in proposal["banks"]:
        payload = _load_bank(bank_root, bank)
        computed = _bank_registries(payload)
        if any(bank.get(field) != value for field, value in computed.items()):
            raise ValueError("bank request registry hash mismatch")
    expected_snapshot = _expected_snapshot_hashes(proposal)
    if proposal["snapshot_hashes"] != expected_snapshot:
        raise ValueError("snapshot hash mismatch")

    route_costs, total = _proposal_costs(proposal)
    for actor in actors:
        recorded = _strict_decimal(
            actor["route_worst_case_usd"], label="route worst-case cost"
        )
        if recorded != route_costs[actor["actor_alias"]]:
            raise ValueError("route worst-case cost mismatch")
    if _strict_decimal(
        budget["calculated_worst_case_usd"], label="calculated worst-case cost"
    ) != total:
        raise ValueError("calculated worst-case cost mismatch")
    if _strict_decimal(budget["forecast_usd"], label="forecast") != total:
        raise ValueError("cost forecast mismatch")
    if total > Decimal("3"):
        raise ValueError("forecast exceeds three dollars")
    return total


def validate_pretransport_authorization(
    proposal: dict[str, Any],
    authorization: dict[str, Any],
    *,
    bank_root: Path,
    today: date | None = None,
    owner_record_path: Path | None = None,
    expected_owner_record_sha256: str | None = None,
    consumption_dir: Path | None = None,
) -> dict[str, str]:
    """Fail closed before transport construction, with no network or provider I/O."""

    total = validate_proposal_contract(proposal, bank_root=bank_root, today=today)
    if type(authorization) is not dict:
        raise ValueError("invalid authorization")
    if authorization.get("authorization_sha256") != canonical_sha256(
        _authorization_core(authorization)
    ):
        raise ValueError("authorization hash mismatch")
    if authorization.get("not_to_exceed_usd") != 5:
        raise ValueError("authorization NTE must equal five dollars")
    errors = sorted(
        Draft202012Validator(_schema(_AUTHORIZATION_SCHEMA)).iter_errors(
            authorization
        ),
        key=lambda error: list(error.path),
    )
    if errors:
        raise ValueError(f"invalid authorization schema: {errors[0].message}")
    if authorization["authorization_schema_sha256"] != _file_sha256(
        _AUTHORIZATION_SCHEMA
    ):
        raise ValueError("authorization schema hash mismatch")
    if authorization["status"] != "APPROVED":
        raise ValueError("owner authorization required")
    if authorization["proposal_manifest_sha256"] != proposal["manifest_sha256"]:
        raise ValueError("authorization proposal hash mismatch")
    current = today or date.today()
    expires = _parse_date(authorization["expires_on"], label="authorization expiry")
    approved = _parse_date(
        authorization["approved_on"], label="authorization approval date"
    )
    if expires < current:
        raise ValueError("authorization expired")
    if approved > current or approved > expires:
        raise ValueError("authorization approval date is invalid")
    if authorization["expires_on"] != proposal["expires_on"]:
        raise ValueError("authorization expiry mismatch")
    if owner_record_path is None or expected_owner_record_sha256 is None:
        raise ValueError("trusted owner record required")
    try:
        owner_record_bytes = Path(owner_record_path).read_bytes()
        owner_record_source = owner_record_bytes.decode("utf-8")
    except (OSError, UnicodeError) as error:
        raise ValueError("trusted owner record unavailable") from error
    owner_record_sha256 = hashlib.sha256(owner_record_bytes).hexdigest()
    if owner_record_sha256 != expected_owner_record_sha256:
        raise ValueError("owner record trust-anchor hash mismatch")
    owner_record = _decode_json(owner_record_source, label="MVP owner record")
    owner_errors = sorted(
        Draft202012Validator(_schema(_OWNER_RECORD_SCHEMA)).iter_errors(
            owner_record
        ),
        key=lambda error: list(error.path),
    )
    if owner_errors:
        raise ValueError(f"invalid owner record schema: {owner_errors[0].message}")
    if owner_record["owner_record_schema_sha256"] != _file_sha256(
        _OWNER_RECORD_SCHEMA
    ):
        raise ValueError("owner record schema hash mismatch")
    owner_binding = {
        "owner_record_id": authorization["owner_record_id"],
        "owner": authorization["owner"],
        "approval_reference": authorization["approval_reference"],
        "approved_on": authorization["approved_on"],
        "expires_on": authorization["expires_on"],
        "proposal_manifest_sha256": authorization["proposal_manifest_sha256"],
        "authorization_sha256": authorization["authorization_sha256"],
        "run_id": authorization["run_id"],
        "authorization_nonce": authorization["authorization_nonce"],
        "not_to_exceed_usd": authorization["not_to_exceed_usd"],
    }
    if any(owner_record.get(key) != value for key, value in owner_binding.items()):
        raise ValueError("owner record authorization binding mismatch")
    if consumption_dir is None:
        raise ValueError("consumption state unavailable")
    state_root = Path(consumption_dir)
    try:
        if not state_root.is_dir() or state_root.is_symlink():
            raise ValueError("consumption state unavailable")
    except OSError as error:
        raise ValueError("consumption state unavailable") from error
    receipt = {
        "consumption_version": "pf002-authorization-consumption-v1",
        "proposal_manifest_sha256": proposal["manifest_sha256"],
        "authorization_sha256": authorization["authorization_sha256"],
        "owner_record_sha256": owner_record_sha256,
        "run_id": authorization["run_id"],
        "authorization_nonce": authorization["authorization_nonce"],
    }
    receipt_path = state_root / (
        f'{authorization["run_id"]}-{authorization["authorization_nonce"]}.consumed.json'
    )
    try:
        descriptor = os.open(
            receipt_path,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL,
            0o600,
        )
    except FileExistsError as error:
        raise ValueError("authorization already consumed") from error
    except OSError as error:
        raise ValueError("consumption state unavailable") from error
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(_pretty_bytes(receipt))
            stream.flush()
            os.fsync(stream.fileno())
        directory_descriptor = os.open(state_root, os.O_RDONLY)
        try:
            os.fsync(directory_descriptor)
        finally:
            os.close(directory_descriptor)
    except OSError as error:
        raise ValueError("consumption state unavailable") from error
    return {
        "proposal_manifest_sha256": proposal["manifest_sha256"],
        "authorization_sha256": authorization["authorization_sha256"],
        "owner_record_sha256": owner_record_sha256,
        "run_id": authorization["run_id"],
        "authorization_nonce": authorization["authorization_nonce"],
        "worst_case_cost_usd": _decimal_text(total),
        "not_to_exceed_usd": "5",
    }


def _neutral_request(episode: dict[str, Any], phase: str, actor: dict[str, Any]) -> dict[str, Any]:
    if phase == "primary":
        prompt = f'{episode["cue_surfaces"]["C1"]}\n\n{episode["shared_body"]}'
    elif phase == "probe":
        prompt = json.dumps(
            episode["probe_payload"],
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
    else:
        raise ValueError("invalid MVP phase")
    authored_maximum = episode["decoding"]["max_tokens"]
    return {
        "provenance": PROVENANCE,
        "prompt": prompt,
        "response_schema": deepcopy(episode["response_schema"]),
        "tools": deepcopy(episode["tool_schema"]),
        "temperature": actor["temperature"],
        "max_output_tokens": min(actor["max_output_tokens"], authored_maximum),
    }


def _registry_request(episode: dict[str, Any], phase: str) -> dict[str, Any]:
    registration_actor = {"temperature": 0, "max_output_tokens": 700}
    return _neutral_request(episode, phase, registration_actor)


def _load_bank(bank_root: Path, bank: dict[str, Any]) -> dict[str, Any]:
    expected_path = f'modules/{bank["module"]}/episodes.yaml'
    if bank.get("path") != expected_path or bank["module"] not in _MODULES:
        raise ValueError("invalid bank path")
    path = bank_root / expected_path
    try:
        source = path.read_bytes()
        payload = yaml.safe_load(source.decode("utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as error:
        raise ValueError("invalid frozen bank") from error
    if hashlib.sha256(source).hexdigest() != bank.get("sha256"):
        raise ValueError("bank hash mismatch")
    if (
        type(payload) is not dict
        or payload.get("module") != bank["module"]
        or payload.get("manifest_version") != "episode-bank-v1"
        or type(payload.get("episodes")) is not list
        or len(payload["episodes"]) != 12
    ):
        raise ValueError("invalid frozen bank")
    return payload


def _bank_registries(payload: dict[str, Any]) -> dict[str, str]:
    surface_rows: list[dict[str, str]] = []
    primary_rows: list[dict[str, str]] = []
    probe_rows: list[dict[str, str]] = []
    for episode in payload["episodes"]:
        episode_id = episode["episode_id"]
        surface_rows.append(
            {
                "episode_id": episode_id,
                "sha256": canonical_sha256(episode["cue_surfaces"]["C1"]),
            }
        )
        primary_rows.append(
            {
                "episode_id": episode_id,
                "sha256": canonical_sha256(_registry_request(episode, "primary")),
            }
        )
        probe_rows.append(
            {
                "episode_id": episode_id,
                "sha256": canonical_sha256(_registry_request(episode, "probe")),
            }
        )
    return {
        "c1_surface_registry_sha256": canonical_sha256(surface_rows),
        "primary_request_registry_sha256": canonical_sha256(primary_rows),
        "probe_request_registry_sha256": canonical_sha256(probe_rows),
    }


def _compute_bank_registries(bank_root: Path, manifest: dict[str, Any]) -> dict[str, dict[str, str]]:
    return {
        bank["module"]: _bank_registries(_load_bank(bank_root, bank))
        for bank in manifest["banks"]
    }


def validate_manifest(
    manifest: dict[str, Any],
    *,
    bank_root: Path,
    today: date | None = None,
) -> None:
    """Fail closed on every PF-002 synthetic authorization and budget gate."""

    if type(manifest) is not dict:
        raise ValueError("invalid MVP manifest")
    supplied_hash = manifest.get("manifest_sha256")
    if supplied_hash != canonical_sha256(_manifest_core(manifest)):
        raise ValueError("manifest hash mismatch")
    if manifest.get("provenance") != PROVENANCE:
        raise ValueError("manifest must be synthetic")
    if manifest.get("authorized") is not False:
        raise ValueError("synthetic manifest cannot be authorized")
    if manifest.get("fallback_enabled") is not False:
        raise ValueError("fallback must be disabled")
    budget = manifest.get("budget")
    if type(budget) is not dict or type(budget.get("forecast_usd")) not in {int, float}:
        raise ValueError("invalid forecast")
    if budget["forecast_usd"] != 0:
        raise ValueError("synthetic forecast must be zero")
    if budget.get("forecast_limit_usd") != 3:
        raise ValueError("forecast exceeds limit")
    if budget.get("hard_cap_usd") != 5:
        raise ValueError("hard cap must equal five dollars")
    actors = manifest.get("actors")
    if type(actors) is not list or len(actors) != 3:
        raise ValueError("exactly three synthetic actors are required")
    for actor in actors:
        if (
            type(actor) is not dict
            or not str(actor.get("actor_alias", "")).startswith("synthetic-actor-")
            or not str(actor.get("model_id", "")).startswith("synthetic-model-")
        ):
            raise ValueError("actor and model identities must be synthetic")
        if (
            actor.get("input_price_per_million_usd") != 0
            or actor.get("output_price_per_million_usd") != 0
        ):
            raise ValueError("synthetic actors require zero price")
    if manifest.get("retry_rule") != {
        "max_retries": 1,
        "retryable_statuses": ["rate_limit"],
        "unknown_delivery_terminal": True,
    }:
        raise ValueError("invalid retry rule")
    errors = sorted(
        Draft202012Validator(_schema(_MANIFEST_SCHEMA)).iter_errors(manifest),
        key=lambda error: list(error.path),
    )
    if errors:
        raise ValueError(f"invalid MVP manifest schema: {errors[0].message}")
    current = today or date.today()
    try:
        expires = date.fromisoformat(manifest["expires_on"])
    except (TypeError, ValueError) as error:
        raise ValueError("invalid manifest expiry") from error
    if expires < current:
        raise ValueError("manifest expired")
    if manifest.get("cue") != "C1":
        raise ValueError("PF-002 requires C1 only")
    if manifest.get("geometry") != {
        "actor_count": 3,
        "capability_twins": False,
        "episode_count": 48,
        "logical_call_count": 288,
        "primary_count": 144,
        "probe_count": 144,
    }:
        raise ValueError("invalid PF-002 geometry")
    if [bank.get("module") for bank in manifest["banks"]] != list(_MODULES):
        raise ValueError("invalid bank order")
    for bank in manifest["banks"]:
        payload = _load_bank(bank_root, bank)
        computed = _bank_registries(payload)
        if any(bank.get(field) != value for field, value in computed.items()):
            raise ValueError("bank request registry hash mismatch")


def compile_mvp_calls(
    manifest: dict[str, Any], *, bank_root: Path
) -> tuple[dict[str, Any], ...]:
    """Compile 48 × 3 × (C1 primary + matched probe) logical calls."""

    validate_manifest(manifest, bank_root=bank_root)
    calls: list[dict[str, Any]] = []
    for bank in manifest["banks"]:
        payload = _load_bank(bank_root, bank)
        for episode in payload["episodes"]:
            episode_sha256 = canonical_sha256(episode)
            surface_sha256 = canonical_sha256(episode["cue_surfaces"]["C1"])
            for actor in manifest["actors"]:
                pair_core = {
                    "domain": "biblebench.pf002.pair.v1",
                    "manifest_sha256": manifest["manifest_sha256"],
                    "bank_sha256": bank["sha256"],
                    "episode_sha256": episode_sha256,
                    "episode_id": episode["episode_id"],
                    "surface_sha256": surface_sha256,
                    "actor_alias": actor["actor_alias"],
                }
                pair_id = canonical_sha256(pair_core)[:16]
                primary_id: str | None = None
                for phase in ("primary", "probe"):
                    request = _neutral_request(episode, phase, actor)
                    request_sha256 = canonical_sha256(request)
                    logical_id = canonical_sha256(
                        {
                            "domain": "biblebench.pf002.logical_call.v1",
                            "pair_id": pair_id,
                            "phase": phase,
                            "request_sha256": request_sha256,
                            "actor_alias": actor["actor_alias"],
                        }
                    )[:16]
                    if phase == "primary":
                        primary_id = logical_id
                    core = {
                        "provenance": PROVENANCE,
                        "logical_call_id": logical_id,
                        "pair_id": pair_id,
                        "primary_logical_call_id": (
                            None if phase == "primary" else primary_id
                        ),
                        "phase": phase,
                        "actor_alias": actor["actor_alias"],
                        "provider_family": actor["provider_family"],
                        "model_id": actor["model_id"],
                        "module": bank["module"],
                        "bank_sha256": bank["sha256"],
                        "episode_id": episode["episode_id"],
                        "episode_sha256": episode_sha256,
                        "cue": "C1",
                        "surface_sha256": surface_sha256,
                        "request": request,
                        "request_sha256": request_sha256,
                    }
                    calls.append({**core, "binding_sha256": canonical_sha256(core)})
    if (
        len(calls) != 288
        or Counter(call["phase"] for call in calls)
        != Counter(primary=144, probe=144)
        or len({call["logical_call_id"] for call in calls}) != 288
        or len({call["pair_id"] for call in calls}) != 144
    ):
        raise ValueError("compiled geometry is not PF-002")
    return tuple(calls)


def _record_envelopes(record_type: str, payloads: list[dict[str, Any]]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    previous: str | None = None
    for sequence, payload in enumerate(payloads, start=1):
        if payload.get("provenance") != PROVENANCE:
            raise ValueError("synthetic record provenance is required")
        core = {
            "provenance": PROVENANCE,
            "record_type": record_type,
            "sequence": sequence,
            "previous_record_sha256": previous,
            "payload": payload,
            "payload_sha256": canonical_sha256(payload),
        }
        record = {**core, "record_sha256": canonical_sha256(core)}
        records.append(record)
        previous = record["record_sha256"]
    if not records:
        raise ValueError("synthetic artifact cannot be empty")
    return records


def _artifact(
    artifact_type: str,
    payloads: list[dict[str, Any]],
    previous_artifact_sha256: str,
) -> dict[str, Any]:
    records = _record_envelopes(
        "missingness" if artifact_type == "missingness" else artifact_type.rstrip("s"),
        payloads,
    )
    core = {
        "provenance": PROVENANCE,
        "artifact_version": "pf002-mvp-artifact-v1",
        "artifact_type": artifact_type,
        "record_count": len(records),
        "previous_artifact_sha256": previous_artifact_sha256,
        "records_sha256": canonical_sha256(records),
        "records": records,
    }
    return {**core, "artifact_sha256": canonical_sha256(core)}


def _pretty_bytes(value: dict[str, Any]) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
            allow_nan=False,
        )
        + "\n"
    ).encode("utf-8")


def _require_empty_output(output_dir: Path) -> None:
    if output_dir.exists():
        if not output_dir.is_dir() or any(output_dir.iterdir()):
            raise ValueError("runner requires an empty output directory")
    else:
        output_dir.mkdir(parents=False)


def run_synthetic_mvp(
    *,
    manifest_path: Path,
    bank_root: Path,
    output_dir: Path,
) -> dict[str, Any]:
    """Execute all 288 logical calls through the local synthetic provider."""

    manifest = load_manifest(manifest_path)
    validate_manifest(manifest, bank_root=bank_root)
    _require_empty_output(output_dir)
    calls = list(compile_mvp_calls(manifest, bank_root=bank_root))
    provider = SyntheticProvider()
    request_payloads: list[dict[str, Any]] = []
    response_payloads: list[dict[str, Any]] = []
    usage_payloads: list[dict[str, Any]] = []
    receipt_payloads: list[dict[str, Any]] = []
    missing_payloads: list[dict[str, Any]] = []

    for index, call in enumerate(calls):
        scenario = SCENARIOS[index % len(SCENARIOS)]
        adapted = adapt_request(call["provider_family"], call["request"])
        attempts = 2 if scenario in {"rate_limit_once", "retry_exhausted"} else 1
        final_response: dict[str, Any] | None = None
        for attempt in range(1, attempts + 1):
            request_payload = {
                "provenance": PROVENANCE,
                "logical_call_id": call["logical_call_id"],
                "attempt": attempt,
                "actor_alias": call["actor_alias"],
                "provider_family": call["provider_family"],
                "model_id": call["model_id"],
                "request_sha256": call["request_sha256"],
                "adapted_request": adapted,
                "adapted_request_sha256": canonical_sha256(adapted),
            }
            request_payloads.append(request_payload)
            result = provider.attempt(
                {
                    "provenance": PROVENANCE,
                    "logical_call_id": call["logical_call_id"],
                    "request_sha256": call["request_sha256"],
                },
                scenario=scenario,
                attempt=attempt,
            )
            response_payload = {
                "provenance": PROVENANCE,
                "logical_call_id": call["logical_call_id"],
                "attempt": attempt,
                "scenario": scenario,
                **result,
            }
            response_payloads.append(response_payload)
            usage_payloads.append(
                {
                    "provenance": PROVENANCE,
                    "logical_call_id": call["logical_call_id"],
                    "attempt": attempt,
                    "input_tokens": result["input_tokens"],
                    "output_tokens": result["output_tokens"],
                    "estimated_cost_usd": 0,
                }
            )
            final_response = response_payload
        if final_response is None:
            raise ValueError("synthetic provider produced no response")
        terminal_status = final_response["status"]
        if scenario == "retry_exhausted":
            terminal_status = "retry_exhausted"
        receipt = {
            "provenance": PROVENANCE,
            "logical_call_id": call["logical_call_id"],
            "pair_id": call["pair_id"],
            "actor_alias": call["actor_alias"],
            "provider_family": call["provider_family"],
            "model_id": call["model_id"],
            "scenario": scenario,
            "terminal_status": terminal_status,
            "attempt_count": attempts,
            "fallback_used": False,
            "request_sha256": call["request_sha256"],
            "response_sha256": final_response["synthetic_response_sha256"],
            "estimated_cost_usd": 0,
        }
        receipt_payloads.append(receipt)
        if terminal_status != "success":
            missing_payloads.append(
                {
                    "provenance": PROVENANCE,
                    "logical_call_id": call["logical_call_id"],
                    "actor_alias": call["actor_alias"],
                    "phase": call["phase"],
                    "reason": terminal_status,
                    "terminal": True,
                }
            )

    terminal_counts = Counter(row["terminal_status"] for row in receipt_payloads)
    scenario_counts = Counter(row["scenario"] for row in receipt_payloads)
    summary_payload = {
        "provenance": PROVENANCE,
        "logical_call_count": len(calls),
        "primary_count": sum(call["phase"] == "primary" for call in calls),
        "probe_count": sum(call["phase"] == "probe" for call in calls),
        "actor_count": len(manifest["actors"]),
        "cue": "C1",
        "fallback_used": False,
        "retry_attempt_count": len(request_payloads) - len(calls),
        "terminal_status_counts": dict(sorted(terminal_counts.items())),
        "scenario_counts": dict(sorted(scenario_counts.items())),
        "missingness_count": len(missing_payloads),
        "estimated_cost_usd": 0,
        "hard_cap_usd": 5,
        "authorized": False,
    }

    documents: list[tuple[str, dict[str, Any]]] = [("manifest.json", manifest)]
    previous = manifest["manifest_sha256"]
    for name, artifact_type, payloads in (
        ("calls.json", "calls", calls),
        ("requests.json", "requests", request_payloads),
        ("responses.json", "responses", response_payloads),
        ("usage.json", "usage", usage_payloads),
        ("receipts.json", "receipts", receipt_payloads),
        ("missingness.json", "missingness", missing_payloads),
        ("summary.json", "summary", [summary_payload]),
    ):
        document = _artifact(artifact_type, payloads, previous)
        documents.append((name, document))
        previous = document["artifact_sha256"]
    for name, document in documents:
        (output_dir / name).write_bytes(_pretty_bytes(document))
    verify_run_tree(output_dir)
    return summary_payload


def verify_run_tree(root: Path) -> None:
    """Recompute the complete file, artifact, and record hash chain."""

    if not root.is_dir() or tuple(sorted(path.name for path in root.iterdir())) != tuple(
        sorted(_OUTPUT_FILES)
    ):
        raise ValueError("invalid synthetic MVP artifact tree")
    manifest = _read_json(root / "manifest.json", label="run manifest")
    validate_manifest(manifest, bank_root=_ROOT)
    if (
        manifest.get("provenance") != PROVENANCE
        or manifest.get("manifest_sha256") != canonical_sha256(_manifest_core(manifest))
    ):
        raise ValueError("invalid run manifest hash")
    previous = manifest["manifest_sha256"]
    validator = Draft202012Validator(_schema(_ARTIFACT_SCHEMA))
    for name in _OUTPUT_FILES[1:]:
        document = _read_json(root / name, label="MVP artifact")
        errors = sorted(validator.iter_errors(document), key=lambda error: list(error.path))
        if errors:
            raise ValueError("invalid MVP artifact schema")
        artifact_hash = document.pop("artifact_sha256")
        if artifact_hash != canonical_sha256(document):
            raise ValueError("invalid MVP artifact hash")
        document["artifact_sha256"] = artifact_hash
        if document["previous_artifact_sha256"] != previous:
            raise ValueError("invalid MVP artifact chain")
        records = document["records"]
        if document["record_count"] != len(records) or document["records_sha256"] != canonical_sha256(records):
            raise ValueError("invalid MVP record collection")
        prior_record: str | None = None
        for sequence, record in enumerate(records, start=1):
            if (
                record["sequence"] != sequence
                or record["previous_record_sha256"] != prior_record
                or record["payload_sha256"] != canonical_sha256(record["payload"])
            ):
                raise ValueError("invalid MVP record chain")
            record_hash = record.pop("record_sha256")
            if record_hash != canonical_sha256(record):
                raise ValueError("invalid MVP record hash")
            record["record_sha256"] = record_hash
            prior_record = record_hash
        previous = artifact_hash


def main(argv: list[str] | None = None) -> int:
    """CLI restricted to the repository's bundled synthetic fixture."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=_FIXTURE)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    if args.manifest.resolve() != _FIXTURE.resolve():
        raise ValueError("CLI accepts only the bundled synthetic fixture")
    run_synthetic_mvp(
        manifest_path=_FIXTURE,
        bank_root=_ROOT,
        output_dir=args.output,
    )
    return 0


__all__ = (
    "PROVENANCE",
    "compile_mvp_calls",
    "load_authorization",
    "load_manifest",
    "load_owner_record",
    "load_proposal",
    "main",
    "run_synthetic_mvp",
    "validate_manifest",
    "validate_pretransport_authorization",
    "validate_proposal_contract",
    "verify_run_tree",
)
