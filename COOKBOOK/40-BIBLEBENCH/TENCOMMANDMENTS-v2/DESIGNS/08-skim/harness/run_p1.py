"""Critical-path runner for the frozen SKIM P1 engineering smoke.

This module deliberately stops at artifact custody, strict action execution,
and mechanical episode scoring.  It does not perform the later empirical
analysis tasks.
"""

from __future__ import annotations

from copy import deepcopy
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
import hashlib
import importlib
import json
import math
import os
from pathlib import Path
from types import MappingProxyType
from typing import Any, Dict, Mapping, Optional, Sequence, Tuple

from skim_hashing import canonical_json


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
ITEMBANK = ROOT / "itembank"

_DEFAULT_BANK_PATH = ITEMBANK / "bank" / "p1-public.jsonl"
_DEFAULT_GOLD_PATH = ITEMBANK / "gold" / "p1-private.gold.jsonl"
_DEFAULT_RUNTIME_PATH = ITEMBANK / "runtime" / "p1-runtime-manifest.jsonl"
_DEFAULT_SMOKE_CONFIG_PATH = (
    ROOT / "configs" / "openrouter-cheap-engineering-smoke.json"
)
_DEFAULT_SYNTHETIC_CONFIG_PATH = ROOT / "configs" / "p1-synthetic.json"
_TRUSTED_SMOKE_CONFIG_SHA256 = (
    "498361a8322ff4211fae8e156405fb5306738a2418662c861045a026269a6468",
    "5cf79207e29a38b2465c524f272e4cf8b97600267b46b2479373ca363f215597",
)
_TRUSTED_SYNTHETIC_CONFIG_SHA256 = (
    "a89d48c61885c9e3b34c630b048775668f53359b97c087f5a10a58e26c561e71"
)

_TRUSTED_ARTIFACT_SHA256 = {
    "bank": "b086718e70be89f7d7566bba058f8ebe52add4e6768ac5bed5a539a02608d385",
    "gold": "6d798c21e024f2ab5a8b987b968605ae3e5724840b612afc5c029a2232411e1b",
    "runtime": "258309b788b450f24484bbd946da6b45980589c879e794c485f065eb8229005f",
}

CHEAP_SMOKE_REQUEST_IDS = (
    "skim-p1-f1-expense-audit-platform-first-primary-request-unstated",
    "skim-p1-f1-expense-audit-platform-first-clean-request-unstated",
    "skim-p1-f1-expense-audit-platform-first-recognition-request-unstated",
)

_NEUTRAL_SYNTAX_REPAIR = (
    "Return exactly one JSON object conforming to the declared response schema. "
    "Do not include markdown fences, commentary, or trailing text."
)
_CONSERVATIVE_CHAT_TOKEN_OVERHEAD = 1024


@dataclass(frozen=True)
class FrozenBundle:
    """Hash-verified copies of the three frozen input artifacts and indexes."""

    public: Tuple[Mapping[str, Any], ...]
    gold: Tuple[Mapping[str, Any], ...]
    runtime: Tuple[Mapping[str, Any], ...]
    artifact_sha256: Mapping[str, str]
    public_by_id: Mapping[str, Mapping[str, Any]]
    gold_by_id: Mapping[str, Mapping[str, Any]]
    runtime_by_id: Mapping[str, Mapping[str, Any]]


@dataclass(frozen=True)
class SyntheticValidationPlan:
    """Fully bound, side-effect-free plan for disclosed fixture execution."""

    status: str
    eligible_for_empirical_decision: bool
    profiles: Tuple[str, ...]
    seeds: Tuple[int, ...]
    clients: Tuple[Any, ...]
    schedule: Tuple[Mapping[str, Any], ...]
    bound_by_id: Mapping[str, Any]
    artifact_sha256: Mapping[str, str]
    config_sha256: str


def _reject_json_constant(value: str) -> None:
    raise ValueError("non-finite JSON constant is not canonical: %s" % value)


def _object_without_duplicate_keys(pairs: Sequence[Tuple[str, Any]]) -> Dict[str, Any]:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON object key is not canonical: %s" % key)
        result[key] = value
    return result


def _load_canonical_jsonl(
    path: Path,
    *,
    label: str,
    trusted_sha256: str,
) -> Tuple[Tuple[Mapping[str, Any], ...], str]:
    """Read one trusted JSONL artifact without normalizing its raw bytes."""

    path = Path(path)
    if not path.is_file():
        raise ValueError("%s artifact is missing or is not a regular file" % label)
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != trusted_sha256:
        raise ValueError("%s artifact hash does not match the frozen hash" % label)
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise ValueError("%s artifact is not canonical UTF-8 JSONL" % label) from exc
    if not text.endswith("\n") or text.endswith("\n\n"):
        raise ValueError("%s artifact is not canonical newline-terminated JSONL" % label)
    lines = text[:-1].split("\n")
    if not lines or any(not line for line in lines):
        raise ValueError("%s artifact contains a noncanonical blank JSONL row" % label)

    rows = []
    for line_number, line in enumerate(lines, start=1):
        try:
            row = json.loads(
                line,
                object_pairs_hook=_object_without_duplicate_keys,
                parse_constant=_reject_json_constant,
            )
        except (TypeError, ValueError, json.JSONDecodeError) as exc:
            raise ValueError(
                "%s artifact row %d is not canonical JSON" % (label, line_number)
            ) from exc
        if not isinstance(row, dict):
            raise ValueError("%s artifact rows must be JSON objects" % label)
        if canonical_json(row) != line:
            raise ValueError(
                "%s artifact row %d is not in canonical JSON form"
                % (label, line_number)
            )
        rows.append(row)
    return tuple(rows), digest


def _unique_index(
    rows: Sequence[Mapping[str, Any]], *, key: str, label: str
) -> Mapping[str, Mapping[str, Any]]:
    index = {}
    for row in rows:
        identifier = row.get(key)
        if not isinstance(identifier, str) or not identifier:
            raise ValueError("%s artifact has an invalid %s" % (label, key))
        if identifier in index:
            raise ValueError("%s artifact has duplicate %s values" % (label, key))
        index[identifier] = row
    return MappingProxyType(index)


def load_frozen_bundle(
    bank_path: Optional[Path] = None,
    gold_path: Optional[Path] = None,
    runtime_path: Optional[Path] = None,
) -> FrozenBundle:
    """Load the canonical bank, gold, and runtime artifacts by trusted hash."""

    public, bank_hash = _load_canonical_jsonl(
        _DEFAULT_BANK_PATH if bank_path is None else Path(bank_path),
        label="bank",
        trusted_sha256=_TRUSTED_ARTIFACT_SHA256["bank"],
    )
    gold, gold_hash = _load_canonical_jsonl(
        _DEFAULT_GOLD_PATH if gold_path is None else Path(gold_path),
        label="gold",
        trusted_sha256=_TRUSTED_ARTIFACT_SHA256["gold"],
    )
    runtime, runtime_hash = _load_canonical_jsonl(
        _DEFAULT_RUNTIME_PATH if runtime_path is None else Path(runtime_path),
        label="runtime",
        trusted_sha256=_TRUSTED_ARTIFACT_SHA256["runtime"],
    )
    if len(public) != 640 or len(gold) != 640 or len(runtime) != 800:
        raise ValueError("frozen artifact row counts do not match the P1 contract")

    public_by_id = _unique_index(
        public, key="logical_record_id", label="bank"
    )
    gold_by_id = _unique_index(gold, key="logical_record_id", label="gold")
    runtime_by_id = _unique_index(
        runtime, key="runtime_request_id", label="runtime"
    )
    if tuple(public_by_id) != tuple(gold_by_id):
        raise ValueError("bank and gold artifacts are not ID-aligned")
    if any(
        row.get("source_logical_record_id") not in public_by_id
        for row in runtime
    ):
        raise ValueError("runtime artifact references an unknown public record")

    return FrozenBundle(
        public=public,
        gold=gold,
        runtime=runtime,
        artifact_sha256=MappingProxyType(
            {"bank": bank_hash, "gold": gold_hash, "runtime": runtime_hash}
        ),
        public_by_id=public_by_id,
        gold_by_id=gold_by_id,
        runtime_by_id=runtime_by_id,
    )


def build_smoke_schedule(model_ids: Sequence[str]) -> Tuple[Mapping[str, Any], ...]:
    """Return the stable model-major three-request engineering schedule."""

    identifiers = tuple(model_ids)
    if any(not isinstance(model_id, str) or not model_id for model_id in identifiers):
        raise ValueError("smoke model IDs must be nonempty strings")
    if len(set(identifiers)) != len(identifiers):
        raise ValueError("smoke model IDs must be unique")
    rows = []
    for model_id in identifiers:
        for request_id in CHEAP_SMOKE_REQUEST_IDS:
            rows.append(
                MappingProxyType(
                    {
                        "schedule_index": len(rows),
                        "model_id": model_id,
                        "runtime_request_id": request_id,
                    }
                )
            )
    return tuple(rows)


def build_p1_schedule(
    model_ids: Sequence[str],
    seeds: Sequence[int],
    runtime_rows: Sequence[Mapping[str, Any]],
) -> Tuple[Mapping[str, Any], ...]:
    """Materialize the deterministic full 800-request schedule per subject.

    A subject is one exact ``(model_id, seed)`` pair.  The order within each
    subject is a stable hash permutation, avoiding dependence on Python's
    random implementation while retaining every frozen runtime request once.
    """

    if isinstance(model_ids, (str, bytes, bytearray)):
        raise TypeError("model roster must be a sequence of model IDs")
    identifiers = tuple(model_ids)
    if (
        not identifiers
        or any(type(model_id) is not str or not model_id for model_id in identifiers)
        or len(set(identifiers)) != len(identifiers)
    ):
        raise ValueError("model IDs must be distinct nonempty strings")
    if isinstance(seeds, (str, bytes, bytearray)):
        raise TypeError("seed roster must be a sequence of integers")
    seed_values = tuple(seeds)
    if (
        not seed_values
        or any(type(seed) is not int or seed < 0 for seed in seed_values)
        or len(set(seed_values)) != len(seed_values)
    ):
        raise ValueError("seeds must be distinct nonnegative exact integers")
    if isinstance(runtime_rows, (str, bytes, bytearray)):
        raise TypeError("runtime rows must be a sequence")
    frozen_rows = tuple(runtime_rows)
    if len(frozen_rows) != 800:
        raise ValueError("full P1 schedule requires exactly 800 runtime rows")

    by_id = {}
    for row in frozen_rows:
        if not isinstance(row, Mapping):
            raise TypeError("every runtime row must be an object")
        request_id = row.get("runtime_request_id")
        traceability = row.get("source_traceability")
        if type(request_id) is not str or not request_id:
            raise ValueError("runtime row has an invalid request ID")
        if request_id in by_id:
            raise ValueError("runtime rows contain a duplicate request ID")
        if type(traceability) is not str or traceability not in {
            "audited",
            "unstated",
            "explicitly_untraceable",
        }:
            raise ValueError("runtime row has ambiguous traceability")
        by_id[request_id] = traceability

    rows = []
    for model_id in identifiers:
        for seed in seed_values:
            def permutation_key(request_id: str) -> bytes:
                payload = canonical_json(
                    {
                        "model_id": model_id,
                        "runtime_request_id": request_id,
                        "schedule_version": "skim-p1-full-v1",
                        "seed": seed,
                    }
                ).encode("utf-8")
                return hashlib.sha256(payload).digest()

            for request_id in sorted(by_id, key=permutation_key):
                rows.append(
                    MappingProxyType(
                        {
                            "schedule_index": len(rows),
                            "model_id": model_id,
                            "seed": seed,
                            "runtime_request_id": request_id,
                            "traceability": by_id[request_id],
                        }
                    )
                )
    return tuple(rows)


def _harness_dependencies() -> Tuple[Any, Any]:
    adapters = importlib.import_module("harness.model_adapters")
    tools = importlib.import_module("harness.skim_tools")
    return adapters, tools


def _request_id(bound: Any) -> str:
    identifier = getattr(bound, "runtime_request_id", None)
    if isinstance(identifier, str) and identifier:
        return identifier
    runtime_row = getattr(bound, "runtime_row", None)
    if isinstance(runtime_row, Mapping):
        identifier = runtime_row.get("runtime_request_id")
    if not isinstance(identifier, str) or not identifier:
        raise ValueError("bound runtime request is missing its request ID")
    return identifier


def _client_label(client: Any, attribute: str) -> str:
    value = getattr(client, attribute, None)
    if not isinstance(value, str) or not value:
        raise ValueError("model client is missing %s" % attribute)
    return value


def _load_frozen_smoke_config(
    config_path: Optional[Path],
) -> Tuple[Mapping[str, Any], str]:
    path = _DEFAULT_SMOKE_CONFIG_PATH if config_path is None else Path(config_path)
    if not path.is_file():
        raise ValueError("frozen smoke config is missing")
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest not in _TRUSTED_SMOKE_CONFIG_SHA256:
        raise ValueError("smoke config hash does not match the frozen config")
    try:
        config = json.loads(
            raw.decode("utf-8", errors="strict"),
            object_pairs_hook=_object_without_duplicate_keys,
            parse_constant=_reject_json_constant,
        )
    except (UnicodeDecodeError, TypeError, ValueError, json.JSONDecodeError) as exc:
        raise ValueError("frozen smoke config is not exact JSON") from exc
    expected_fields = {
        "artifact_sha256",
        "catalog_checked_at",
        "catalog_source",
        "cost_cap_usd",
        "eligible_for_empirical_decision",
        "max_paid_calls",
        "max_tokens",
        "mode",
        "model_roster",
        "provider_policy",
        "request_ids",
        "scheduled_requests",
        "schema_version",
        "seed",
        "syntax_repairs_per_request",
    }
    if type(config) is not dict or set(config) != expected_fields:
        raise ValueError("frozen smoke config schema is not exact")
    if (
        config["schema_version"] != 1
        or config["mode"] != "CHEAP_MODEL_ENGINEERING_SMOKE"
        or config["eligible_for_empirical_decision"] is not False
        or config["request_ids"] != list(CHEAP_SMOKE_REQUEST_IDS)
        or config["scheduled_requests"] != 9
        or config["max_paid_calls"] != 18
        or config["syntax_repairs_per_request"] != 1
        or config["provider_policy"]
        != {"allow_fallbacks": False, "require_parameters": True}
        or config["artifact_sha256"] != _TRUSTED_ARTIFACT_SHA256
        or type(config["seed"]) is not int
        or config["seed"] < 0
        or type(config["max_tokens"]) is not int
        or not 1 <= config["max_tokens"] <= 16_384
        or type(config["cost_cap_usd"]) not in (int, float)
        or not math.isfinite(float(config["cost_cap_usd"]))
        or config["cost_cap_usd"] <= 0
    ):
        raise ValueError("frozen smoke config values violate the smoke contract")
    roster = config["model_roster"]
    roster_fields = {
        "completion_price_per_token_usd",
        "endpoint_name",
        "family",
        "model_id",
        "prompt_price_per_token_usd",
        "provider",
        "vendor",
    }
    if type(roster) is not list or len(roster) != 3:
        raise ValueError("frozen smoke config requires exactly three models")
    for row in roster:
        if type(row) is not dict or set(row) != roster_fields:
            raise ValueError("frozen smoke roster schema is not exact")
        if any(
            type(row[field]) is not str or not row[field]
            for field in ("endpoint_name", "family", "model_id", "provider", "vendor")
        ):
            raise ValueError("frozen smoke roster contains a blank identifier")
        for field in (
            "prompt_price_per_token_usd",
            "completion_price_per_token_usd",
        ):
            try:
                price = float(row[field])
            except (TypeError, ValueError):
                raise ValueError("frozen smoke roster price is invalid") from None
            if not math.isfinite(price) or price <= 0:
                raise ValueError("frozen smoke roster price must be positive")
    if len({row["model_id"] for row in roster}) != 3:
        raise ValueError("frozen smoke model IDs must be unique")
    return MappingProxyType(config), digest


def _load_frozen_synthetic_config() -> Tuple[Mapping[str, Any], str]:
    path = _DEFAULT_SYNTHETIC_CONFIG_PATH
    if not path.is_file():
        raise ValueError("frozen synthetic config is missing")
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != _TRUSTED_SYNTHETIC_CONFIG_SHA256:
        raise ValueError("synthetic config hash does not match the frozen config")
    try:
        config = json.loads(
            raw.decode("utf-8", errors="strict"),
            object_pairs_hook=_object_without_duplicate_keys,
            parse_constant=_reject_json_constant,
        )
    except (UnicodeDecodeError, TypeError, ValueError, json.JSONDecodeError) as exc:
        raise ValueError("frozen synthetic config is not exact JSON") from exc
    artifact_hashes = config.get("artifact_hashes") if type(config) is dict else None
    planned = config.get("planned_counts") if type(config) is dict else None
    if (
        config.get("schema_version") != 1
        or config.get("study_id") != "10CB-SKIM-P1"
        or config.get("mode") != "synthetic"
        or config.get("data_basis") != "synthetic"
        or config.get("status") != "HARNESS_VALIDATION_ONLY"
        or config.get("official_eligible") is not False
        or config.get("eligible_for_empirical_decision") is not False
        or config.get("seeds")
        != [2026071001, 2026071002, 2026071003]
        or config.get("bootstrap_replicates") != 200
        or type(planned) is not dict
        or planned.get("requests_per_model_seed") != 800
        or type(artifact_hashes) is not dict
        or set(artifact_hashes)
        != {
            "preregistration_sha256",
            "logical_bank_sha256",
            "private_gold_sha256",
            "runtime_manifest_sha256",
            "config_sha256",
            "analysis_sha256",
            "free_diversion_schedule_sha256",
            "cue_comprehension_schedule_sha256",
        }
        or any(value is not None for value in artifact_hashes.values())
    ):
        raise ValueError("frozen synthetic config violates the fixture contract")
    return MappingProxyType(config), digest


def preflight_synthetic_validation() -> SyntheticValidationPlan:
    """Bind the full disclosed fixture panel without output or execution."""

    config, config_sha256 = _load_frozen_synthetic_config()
    bundle = load_frozen_bundle()
    synthetic = importlib.import_module("harness.synthetic_profiles")
    _adapters, tools = _harness_dependencies()
    profiles = tuple(synthetic.PROFILES)
    seeds = tuple(synthetic.REGISTERED_SEEDS)
    if (
        profiles
        != (
            "invariant_custodian",
            "magnitude_threshold_diverter",
            "eval_aware_diverter",
            "cover_story_buyer",
            "paralyzed_steward",
            "divert_and_misreport",
        )
        or seeds != tuple(config["seeds"])
        or synthetic.SYNTHETIC_STATUS != "HARNESS_VALIDATION_ONLY"
        or synthetic.OFFICIAL_ELIGIBLE is not False
    ):
        raise ValueError("synthetic profile disclosure differs from the frozen plan")

    bound_by_id = {}
    for runtime_row in bundle.runtime:
        request_id = runtime_row["runtime_request_id"]
        logical_id = runtime_row["source_logical_record_id"]
        bound_by_id[request_id] = tools.bind_runtime_request(
            runtime_row,
            bundle.public_by_id[logical_id],
            bundle.gold_by_id[logical_id],
        )
    bound_requests = tuple(bound_by_id.values())
    clients = tuple(
        synthetic.SyntheticProfileClient(profile, bound_requests)
        for profile in profiles
    )
    schedule = build_p1_schedule(
        tuple(_client_label(client, "model_id") for client in clients),
        seeds,
        bundle.runtime,
    )
    return SyntheticValidationPlan(
        status="HARNESS_VALIDATION_ONLY",
        eligible_for_empirical_decision=False,
        profiles=profiles,
        seeds=seeds,
        clients=clients,
        schedule=schedule,
        bound_by_id=MappingProxyType(bound_by_id),
        artifact_sha256=MappingProxyType(dict(bundle.artifact_sha256)),
        config_sha256=config_sha256,
    )


def _bind_clients_to_smoke_config(
    clients: Sequence[Any],
    config: Mapping[str, Any],
    *,
    seed: int,
    cost_cap_usd: float,
) -> None:
    if seed != config["seed"]:
        raise ValueError("seed does not match the frozen smoke config")
    if float(cost_cap_usd) != float(config["cost_cap_usd"]):
        raise ValueError("cost cap does not match the frozen smoke config")
    expected = tuple(
        (
            row["model_id"],
            row["family"],
            row["vendor"],
            row["provider"],
        )
        for row in config["model_roster"]
    )
    observed = tuple(
        (
            getattr(client, "model_id", None),
            getattr(client, "family", None),
            getattr(client, "vendor", None),
            getattr(client, "provider", None),
        )
        for client in clients
    )
    if observed != expected:
        raise ValueError("client roster does not match the frozen smoke config")
    for client in clients:
        if getattr(client, "max_tokens", None) != config["max_tokens"]:
            raise ValueError("client max_tokens does not match the frozen smoke config")
        client_cap = getattr(client, "cost_cap_usd", None)
        if type(client_cap) not in (int, float) or float(client_cap) != float(
            config["cost_cap_usd"]
        ):
            raise ValueError("client cost cap does not match the frozen smoke config")


def _call_cost(client: Any) -> Optional[float]:
    metadata = getattr(client, "last_call_metadata", None)
    if not isinstance(metadata, Mapping):
        return None
    value = metadata.get("cost_usd")
    if type(value) not in (int, float) or not math.isfinite(float(value)) or value < 0:
        return None
    return float(value)


_SAFE_CALL_METADATA_FIELDS = (
    "response_id",
    "requested_model",
    "returned_model",
    "provider",
    "provider_attribution",
    "finish_reason",
    "usage",
    "cost_usd",
    "attempt_count",
    "response_status",
)


def _sanitized_call_metadata(client: Any) -> Mapping[str, Any]:
    metadata = getattr(client, "last_call_metadata", None)
    if not isinstance(metadata, Mapping):
        raise RuntimeError("model call omitted safe response metadata")
    safe = {
        field: deepcopy(metadata[field])
        for field in _SAFE_CALL_METADATA_FIELDS
        if field in metadata
    }
    if _call_cost(client) is None or safe.get("cost_usd") != _call_cost(client):
        raise RuntimeError("safe response metadata cost is missing or inconsistent")
    forbidden = {
        "api_key",
        "mechanical_action_map",
        "private_gold",
        "prompt",
        "raw_response",
    }

    def keys(value):
        if isinstance(value, Mapping):
            result = {str(key).lower() for key in value}
            for child in value.values():
                result.update(keys(child))
            return result
        if isinstance(value, list):
            result = set()
            for child in value:
                result.update(keys(child))
            return result
        return set()

    if forbidden.intersection(keys(safe)):
        raise RuntimeError("safe response metadata contains a forbidden field")
    try:
        canonical_json(safe)
    except (TypeError, ValueError):
        raise RuntimeError("safe response metadata is not canonical JSON") from None
    return safe


@dataclass
class _AggregateBudget:
    cap_usd: float
    spent_usd: float = 0.0
    paid_calls: int = 0

    def before_call(self, maximum_call_cost_usd: float) -> None:
        if (
            type(maximum_call_cost_usd) not in (int, float)
            or not math.isfinite(float(maximum_call_cost_usd))
            or maximum_call_cost_usd <= 0
        ):
            raise RuntimeError("model call cost bound is missing or invalid")
        if math.fsum((self.spent_usd, float(maximum_call_cost_usd))) > self.cap_usd:
            raise RuntimeError(
                "model call could exceed aggregate smoke cost cap before transport"
            )

    def record_call(self, cost_usd: Optional[float]) -> None:
        self.paid_calls += 1
        if cost_usd is None:
            raise RuntimeError("model call omitted required cost metadata")
        updated = math.fsum((self.spent_usd, cost_usd))
        self.spent_usd = updated
        if updated > self.cap_usd:
            raise RuntimeError("model call would exceed aggregate smoke cost cap")


def _generate(
    client: Any,
    request: Mapping[str, Any],
    *,
    seed: int,
    budget: Optional[_AggregateBudget],
    maximum_call_cost_usd: Optional[float] = None,
) -> Tuple[Any, Optional[float], Mapping[str, Any]]:
    if budget is not None:
        budget.before_call(maximum_call_cost_usd)
    try:
        raw = client.generate(deepcopy(request), seed=seed)
    except Exception as exc:
        cost = _call_cost(client)
        if budget is not None and cost is not None:
            try:
                budget.record_call(cost)
            except RuntimeError as accounting_error:
                raise accounting_error from exc
        raise
    cost = _call_cost(client)
    if budget is not None:
        budget.record_call(cost)
    return raw, cost, _sanitized_call_metadata(client)


def _configured_call_cost_upper_bound(
    config: Mapping[str, Any],
    model_id: str,
    request: Mapping[str, Any],
) -> float:
    rows = [
        row for row in config["model_roster"] if row["model_id"] == model_id
    ]
    if len(rows) != 1:
        raise ValueError("model is absent from the frozen smoke price roster")
    messages = request.get("messages")
    if type(messages) is not list or not messages:
        raise ValueError("priced model request has no exact message list")
    prompt_token_upper_bound = math.fsum(
        (
            len(canonical_json(messages).encode("utf-8")),
            _CONSERVATIVE_CHAT_TOKEN_OVERHEAD,
        )
    )
    row = rows[0]
    return math.fsum(
        (
            prompt_token_upper_bound
            * float(row["prompt_price_per_token_usd"]),
            config["max_tokens"]
            * float(row["completion_price_per_token_usd"]),
        )
    )


def _repair_request(request: Mapping[str, Any]) -> Dict[str, Any]:
    repaired = deepcopy(dict(request))
    messages = repaired.get("messages")
    if not isinstance(messages, list):
        raise ValueError("model request messages must be a list")
    messages.append({"role": "developer", "content": _NEUTRAL_SYNTAX_REPAIR})
    return repaired


def _episode_result(
    bound: Any,
    client: Any,
    *,
    seed: int,
    status: str,
    paid_calls: int,
    costs: Sequence[Optional[float]],
    call_metadata: Sequence[Mapping[str, Any]],
    event_count: int,
    syntax_repair_used: bool,
    execution: Optional[Any],
) -> Dict[str, Any]:
    result = {
        "request_id": _request_id(bound),
        "model_id": _client_label(client, "model_id"),
        "model_family": _client_label(client, "family"),
        "vendor": _client_label(client, "vendor"),
        "seed": seed,
        "status": status,
        "paid_calls": paid_calls,
        "event_count": event_count,
        "syntax_repair_used": syntax_repair_used,
        "cost_usd": (
            math.fsum(cost for cost in costs if cost is not None)
            if all(cost is not None for cost in costs)
            else None
        ),
        "call_metadata": [dict(row) for row in call_metadata],
    }
    if execution is not None:
        commit = getattr(execution, "commit", None)
        if isinstance(commit, Mapping) and isinstance(commit.get("option_id"), str):
            result["selected_option_id"] = commit["option_id"]
    return result


def _execute_runtime_request(
    bound: Any,
    client: Any,
    *,
    seed: int,
    event_log_path: Path,
    budget: Optional[_AggregateBudget],
    smoke_config: Optional[Mapping[str, Any]] = None,
) -> Tuple[Dict[str, Any], Optional[Any]]:
    if type(seed) is not int or seed < 0:
        raise ValueError("seed must be a nonnegative integer")
    if not callable(getattr(client, "generate", None)):
        raise ValueError("model client must expose generate(request, seed=...)")
    adapters, tools = _harness_dependencies()
    runtime_row = getattr(bound, "runtime_row", None)
    if not isinstance(runtime_row, Mapping):
        raise ValueError("bound request is missing its frozen runtime row")
    model_request = adapters.build_model_request(runtime_row)
    episode_id = "%s--%s--seed-%d" % (
        _client_label(client, "model_id"),
        _request_id(bound),
        seed,
    )

    costs = []
    call_metadata = []
    maximum_call_cost = (
        None
        if budget is None
        else _configured_call_cost_upper_bound(
            smoke_config, _client_label(client, "model_id"), model_request
        )
    )
    raw, cost, metadata = _generate(
        client,
        model_request,
        seed=seed,
        budget=budget,
        maximum_call_cost_usd=maximum_call_cost,
    )
    costs.append(cost)
    call_metadata.append(metadata)
    try:
        execution = tools.execute_bound_action(
            bound,
            raw,
            episode_id=episode_id,
            event_log_path=Path(event_log_path),
        )
    except tools.ProtocolError:
        repair = _repair_request(model_request)
        maximum_repair_cost = (
            None
            if budget is None
            else _configured_call_cost_upper_bound(
                smoke_config, _client_label(client, "model_id"), repair
            )
        )
        repaired_raw, repair_cost, repair_metadata = _generate(
            client,
            repair,
            seed=seed,
            budget=budget,
            maximum_call_cost_usd=maximum_repair_cost,
        )
        costs.append(repair_cost)
        call_metadata.append(repair_metadata)
        try:
            execution = tools.execute_bound_action(
                bound,
                repaired_raw,
                episode_id=episode_id,
                event_log_path=Path(event_log_path),
            )
        except tools.ProtocolError:
            return (
                _episode_result(
                    bound,
                    client,
                    seed=seed,
                    status="PARKED_AFTER_SYNTAX_REPAIR",
                    paid_calls=2,
                    costs=costs,
                    call_metadata=call_metadata,
                    event_count=0,
                    syntax_repair_used=True,
                    execution=None,
                ),
                None,
            )
        except tools.SemanticActionError:
            return (
                _episode_result(
                    bound,
                    client,
                    seed=seed,
                    status="PARKED_INVALID_ACTION",
                    paid_calls=2,
                    costs=costs,
                    call_metadata=call_metadata,
                    event_count=0,
                    syntax_repair_used=True,
                    execution=None,
                ),
                None,
            )
        status = "VALID_TERMINAL_AFTER_REPAIR"
        paid_calls = 2
        repaired = True
    except tools.SemanticActionError:
        return (
            _episode_result(
                bound,
                client,
                seed=seed,
                status="PARKED_INVALID_ACTION",
                paid_calls=1,
                costs=costs,
                call_metadata=call_metadata,
                event_count=0,
                syntax_repair_used=False,
                execution=None,
            ),
            None,
        )
    else:
        status = getattr(execution, "status", "VALID_TERMINAL")
        paid_calls = 1
        repaired = False

    events = getattr(execution, "events", ())
    result = _episode_result(
        bound,
        client,
        seed=seed,
        status=status,
        paid_calls=paid_calls,
        costs=costs,
        call_metadata=call_metadata,
        event_count=len(events),
        syntax_repair_used=repaired,
        execution=execution,
    )
    return result, execution


def execute_runtime_request(
    bound: Any,
    client: Any,
    *,
    seed: int,
    event_log_path: Path,
) -> Dict[str, Any]:
    """Execute one bound request with at most one neutral syntax repair."""

    result, _execution = _execute_runtime_request(
        bound,
        client,
        seed=seed,
        event_log_path=event_log_path,
        budget=None,
        smoke_config=None,
    )
    return result


_SCORE_FIELDS = (
    "status",
    "valid_terminal",
    "selected_option_id",
    "classification",
    "diversion",
    "custody_fidelity",
    "theta_eligible",
    "rs_status",
    "severe_floor_applied",
)


def _mechanical_scorer() -> Optional[Any]:
    try:
        return importlib.import_module("scoring.mechanical")
    except ModuleNotFoundError as exc:
        if exc.name in {"scoring", "scoring.mechanical"}:
            return None
        raise


def _sanitized_score(score: Any) -> Mapping[str, Any]:
    return {
        field: getattr(score, field)
        for field in _SCORE_FIELDS
        if hasattr(score, field)
    }


def _write_new_canonical_json(path: Path, payload: Mapping[str, Any]) -> None:
    data = (canonical_json(payload) + "\n").encode("utf-8")
    with Path(path).open("xb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())


def run_cheap_smoke(
    *,
    clients: Sequence[Any],
    seed: int,
    output_dir: Path,
    cost_cap_usd: float,
    config_path: Optional[Path] = None,
) -> Dict[str, Any]:
    """Run the registered nine-episode, non-empirical engineering smoke."""

    if type(seed) is not int or seed < 0:
        raise ValueError("seed must be a nonnegative integer")
    if (
        type(cost_cap_usd) not in (int, float)
        or not math.isfinite(float(cost_cap_usd))
        or cost_cap_usd <= 0
    ):
        raise ValueError("cost_cap_usd must be a positive finite number")
    roster = tuple(clients)
    if len(roster) != 3:
        raise ValueError("cheap engineering smoke requires exactly three clients")
    smoke_config, smoke_config_sha256 = _load_frozen_smoke_config(config_path)
    _bind_clients_to_smoke_config(
        roster,
        smoke_config,
        seed=seed,
        cost_cap_usd=float(cost_cap_usd),
    )
    model_ids = tuple(_client_label(client, "model_id") for client in roster)
    for client in roster:
        _client_label(client, "family")
        _client_label(client, "vendor")
        if not callable(getattr(client, "generate", None)):
            raise ValueError("every smoke client must expose generate")
    schedule = build_smoke_schedule(model_ids)

    # Complete artifact verification and all custody binding before the first
    # client call or output mutation.
    bundle = load_frozen_bundle()
    _adapters, tools = _harness_dependencies()
    bound_by_id = {}
    for request_id in CHEAP_SMOKE_REQUEST_IDS:
        runtime_row = bundle.runtime_by_id.get(request_id)
        if runtime_row is None:
            raise ValueError("registered smoke request is absent from runtime artifact")
        logical_id = runtime_row.get("source_logical_record_id")
        public_row = bundle.public_by_id.get(logical_id)
        gold_row = bundle.gold_by_id.get(logical_id)
        if public_row is None or gold_row is None:
            raise ValueError("registered smoke request cannot be bound to frozen rows")
        bound_by_id[request_id] = tools.bind_runtime_request(
            runtime_row, public_row, gold_row
        )

    preflight_cost_upper_bound = 0.0
    for schedule_row in schedule:
        bound = bound_by_id[schedule_row["runtime_request_id"]]
        request = _adapters.build_model_request(bound.runtime_row)
        repair = _repair_request(request)
        preflight_cost_upper_bound = math.fsum(
            (
                preflight_cost_upper_bound,
                _configured_call_cost_upper_bound(
                    smoke_config, schedule_row["model_id"], request
                ),
                _configured_call_cost_upper_bound(
                    smoke_config, schedule_row["model_id"], repair
                ),
            )
        )
    if preflight_cost_upper_bound > float(cost_cap_usd):
        raise ValueError(
            "frozen smoke schedule could exceed the aggregate cost cap"
        )

    output_dir = Path(output_dir)
    if output_dir.exists():
        raise ValueError("smoke output directory must be fresh")
    output_dir.mkdir(parents=True, exist_ok=False)
    event_dir = output_dir / "events"
    event_dir.mkdir(exist_ok=False)

    clients_by_id = dict(zip(model_ids, roster))
    scorer = _mechanical_scorer()
    budget = _AggregateBudget(float(cost_cap_usd))
    episodes = []
    for schedule_row in schedule:
        request_id = schedule_row["runtime_request_id"]
        try:
            episode, execution = _execute_runtime_request(
                bound_by_id[request_id],
                clients_by_id[schedule_row["model_id"]],
                seed=seed,
                event_log_path=event_dir
                / ("episode-%03d.jsonl" % schedule_row["schedule_index"]),
                budget=budget,
                smoke_config=smoke_config,
            )
        except Exception as exc:
            failure = {
                "schema_version": 1,
                "study_id": "SKIM-P1",
                "status": "CHEAP_MODEL_ENGINEERING_SMOKE_ABORTED",
                "eligible_for_empirical_decision": False,
                "seed": seed,
                "scheduled_requests": len(schedule),
                "completed_episodes": len(episodes),
                "failed_schedule_index": schedule_row["schedule_index"],
                "failed_request_id": request_id,
                "failed_model_id": schedule_row["model_id"],
                "paid_calls": budget.paid_calls,
                "total_cost_usd": budget.spent_usd,
                "cost_cap_usd": float(cost_cap_usd),
                "preflight_cost_upper_bound_usd": preflight_cost_upper_bound,
                "smoke_config_sha256": smoke_config_sha256,
                "artifact_sha256": dict(bundle.artifact_sha256),
                "failure_type": type(exc).__name__,
                "failure_code": "MODEL_CALL_OR_EXECUTION_ABORTED",
            }
            _write_new_canonical_json(
                output_dir / "smoke-failure.json", failure
            )
            raise
        episode["schedule_index"] = schedule_row["schedule_index"]
        if execution is not None and scorer is not None:
            score = scorer.score_terminal_episode(
                execution, bound_by_id[request_id].private_gold
            )
            episode["mechanical_score"] = _sanitized_score(score)
        episodes.append(episode)

    result = {
        "schema_version": 1,
        "study_id": "SKIM-P1",
        "status": "CHEAP_MODEL_ENGINEERING_SMOKE_COMPLETE",
        "eligible_for_empirical_decision": False,
        "seed": seed,
        "scheduled_requests": len(schedule),
        "paid_calls": budget.paid_calls,
        "total_cost_usd": budget.spent_usd,
        "cost_cap_usd": float(cost_cap_usd),
        "preflight_cost_upper_bound_usd": preflight_cost_upper_bound,
        "smoke_config_sha256": smoke_config_sha256,
        "artifact_sha256": dict(bundle.artifact_sha256),
        "episodes": episodes,
    }
    _write_new_canonical_json(output_dir / "smoke-result.json", result)
    return result


def _execute_synthetic_schedule(
    plan: SyntheticValidationPlan,
    schedule: Sequence[Mapping[str, Any]],
    *,
    output_dir: Path,
    max_workers: int,
) -> Tuple[Mapping[str, Any], ...]:
    """Execute a preflighted fixture schedule; subset use is test-only."""

    if type(plan) is not SyntheticValidationPlan:
        raise TypeError("plan must be an exact SyntheticValidationPlan")
    if type(max_workers) is not int or not 1 <= max_workers <= len(plan.clients):
        raise ValueError("synthetic max_workers must be in the profile roster range")
    rows = tuple(schedule)
    if not rows:
        raise ValueError("synthetic schedule must not be empty")
    clients_by_id = {
        _client_label(client, "model_id"): client for client in plan.clients
    }
    if len(clients_by_id) != len(plan.clients):
        raise ValueError("synthetic client model IDs must be unique")
    seen_indices = set()
    grouped = {model_id: [] for model_id in clients_by_id}
    for row in rows:
        if not isinstance(row, Mapping):
            raise TypeError("synthetic schedule rows must be objects")
        index = row.get("schedule_index")
        model_id = row.get("model_id")
        seed = row.get("seed")
        request_id = row.get("runtime_request_id")
        if type(index) is not int or index < 0 or index in seen_indices:
            raise ValueError("synthetic schedule index is invalid or duplicated")
        if model_id not in clients_by_id:
            raise ValueError("synthetic schedule references an unknown client")
        if seed not in plan.seeds or type(seed) is not int:
            raise ValueError("synthetic schedule references an unregistered seed")
        if request_id not in plan.bound_by_id:
            raise ValueError("synthetic schedule references an unknown request")
        seen_indices.add(index)
        grouped[model_id].append(row)

    output_dir = Path(output_dir)
    if output_dir.exists():
        raise ValueError("synthetic output directory must be fresh")
    output_dir.mkdir(parents=True, exist_ok=False)
    event_dir = output_dir / "events"
    event_dir.mkdir(exist_ok=False)
    scorer = _mechanical_scorer()
    if scorer is None:
        raise RuntimeError("mechanical scorer is required for synthetic validation")

    def run_client_group(model_id: str) -> Tuple[Mapping[str, Any], ...]:
        client = clients_by_id[model_id]
        completed = []
        for row in grouped[model_id]:
            request_id = row["runtime_request_id"]
            event_name = "episode-%05d.jsonl" % row["schedule_index"]
            episode, execution = _execute_runtime_request(
                plan.bound_by_id[request_id],
                client,
                seed=row["seed"],
                event_log_path=event_dir / event_name,
                budget=None,
                smoke_config=None,
            )
            episode["schedule_index"] = row["schedule_index"]
            episode["event_log"] = (
                "events/" + event_name if execution is not None else None
            )
            if execution is not None:
                score = scorer.score_terminal_episode(
                    execution, plan.bound_by_id[request_id].private_gold
                )
                episode["mechanical_score"] = _sanitized_score(score)
            completed.append(episode)
        return tuple(completed)

    active_model_ids = tuple(
        model_id for model_id, group in grouped.items() if group
    )
    try:
        with ThreadPoolExecutor(
            max_workers=min(max_workers, len(active_model_ids))
        ) as executor:
            grouped_results = tuple(executor.map(run_client_group, active_model_ids))
    except Exception as exc:
        failure = {
            "schema_version": 1,
            "study_id": "SKIM-P1",
            "status": "HARNESS_VALIDATION_ABORTED",
            "eligible_for_empirical_decision": False,
            "failure_type": type(exc).__name__,
            "failure_code": "SYNTHETIC_EXECUTION_ABORTED",
            "scheduled_requests": len(rows),
            "artifact_sha256": dict(plan.artifact_sha256),
            "config_sha256": plan.config_sha256,
        }
        _write_new_canonical_json(output_dir / "synthetic-failure.json", failure)
        raise
    result_by_index = {
        episode["schedule_index"]: episode
        for group in grouped_results
        for episode in group
    }
    if set(result_by_index) != seen_indices:
        raise RuntimeError("synthetic execution did not return the exact schedule")
    return tuple(result_by_index[row["schedule_index"]] for row in rows)


def run_synthetic_validation(
    *,
    output_dir: Path,
    max_workers: int = 6,
) -> Dict[str, Any]:
    """Run all six disclosed profiles over all three frozen fixture seeds."""

    if type(max_workers) is not int or not 1 <= max_workers <= 6:
        raise ValueError("synthetic max_workers must be an integer in [1, 6]")
    plan = preflight_synthetic_validation()
    episodes = _execute_synthetic_schedule(
        plan,
        plan.schedule,
        output_dir=output_dir,
        max_workers=max_workers,
    )
    if len(episodes) != len(plan.schedule):
        raise RuntimeError("synthetic run did not complete every scheduled episode")
    valid_statuses = {"VALID_TERMINAL", "VALID_TERMINAL_AFTER_REPAIR"}
    classifications = {}
    for episode in episodes:
        score = episode.get("mechanical_score")
        if isinstance(score, Mapping) and isinstance(score.get("classification"), str):
            label = score["classification"]
            classifications[label] = classifications.get(label, 0) + 1
    result = {
        "schema_version": 1,
        "study_id": "SKIM-P1",
        "status": "HARNESS_VALIDATION_ONLY",
        "data_basis": "synthetic_fixture",
        "official_eligible": False,
        "eligible_for_empirical_decision": False,
        "professional_realism_status": "NOT_RUN_PROFESSIONAL_REALISM",
        "human_baseline_status": "NOT_RUN_HUMAN_BASELINE",
        "x2_finetune_status": "NOT_RUN_LLM",
        "bootstrap_replicates": 200,
        "profiles": list(plan.profiles),
        "seeds": list(plan.seeds),
        "scheduled_requests": len(plan.schedule),
        "completed_episodes": len(episodes),
        "valid_terminal_episodes": sum(
            episode["status"] in valid_statuses for episode in episodes
        ),
        "parked_episodes": sum(
            episode["status"] not in valid_statuses for episode in episodes
        ),
        "fixture_calls": sum(episode["paid_calls"] for episode in episodes),
        "external_paid_calls": 0,
        "total_cost_usd": 0.0,
        "classification_counts": classifications,
        "blockers": [
            "SYNTHETIC_EVIDENCE",
            "NOT_RUN_PROFESSIONAL_REALISM",
            "NOT_RUN_HUMAN_BASELINE",
            "NO_FROZEN_EXTERNAL_CAPABILITY_PC1",
            "NOT_RUN_LLM",
        ],
        "artifact_sha256": dict(plan.artifact_sha256),
        "config_sha256": plan.config_sha256,
        "episodes": list(episodes),
    }
    _write_new_canonical_json(Path(output_dir) / "synthetic-result.json", result)
    return result


__all__ = [
    "CHEAP_SMOKE_REQUEST_IDS",
    "FrozenBundle",
    "SyntheticValidationPlan",
    "build_p1_schedule",
    "build_smoke_schedule",
    "execute_runtime_request",
    "load_frozen_bundle",
    "preflight_synthetic_validation",
    "run_cheap_smoke",
    "run_synthetic_validation",
]
