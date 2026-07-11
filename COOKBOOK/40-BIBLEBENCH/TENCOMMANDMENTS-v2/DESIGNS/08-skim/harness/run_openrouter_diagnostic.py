#!/usr/bin/env python3
"""Run the frozen 2,400-request cheap-model SKIM OpenRouter diagnostic."""

from __future__ import annotations

import argparse
from concurrent.futures import as_completed, ThreadPoolExecutor
from dataclasses import dataclass
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import threading
from types import MappingProxyType
from typing import Any, Mapping, Optional, Sequence, Tuple
import urllib.request


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
BENCH_ROOT = ROOT.parents[2]
for search_root in (ROOT, BENCH_ROOT):
    if str(search_root) not in sys.path:
        sys.path.insert(0, str(search_root))

from harness import model_adapters  # noqa: E402
from harness.run_p1 import (  # noqa: E402
    _AggregateBudget,
    _configured_call_cost_upper_bound,
    _execute_runtime_request,
    _mechanical_scorer,
    _object_without_duplicate_keys,
    _reject_json_constant,
    _repair_request,
    _sanitized_call_metadata,
    _sanitized_score,
    _write_new_canonical_json,
    build_p1_schedule,
    load_frozen_bundle,
)
from harness.skim_tools import bind_runtime_request, resume_bound_action  # noqa: E402
from skim_hashing import canonical_json  # noqa: E402


CONFIG_PATH = ROOT / "configs" / "openrouter-cheap-full-engineering-diagnostic.json"
CONFIG_SHA256 = "8f9876a03ea760defe9bef13a8b04cdcd99425677b5853e6b92d269061acfd84"
RUN_STATUS = "LIVE_ONE_SEED_CHEAP_MODEL_ENGINEERING_DIAGNOSTIC"
TRANSPORT_REPAIR_ATTESTATION_NAME = "transport-repair-attestation.json"
TRANSPORT_REPAIR_ATTESTATION_SHA256 = (
    "5adc6606bf07136dea29bd29f4e5094788f01725b07369b1345a197b28c7b4e3"
)


@dataclass(frozen=True)
class DiagnosticPlan:
    status: str
    eligible_for_empirical_decision: bool
    seed: int
    clients: Tuple[Any, ...]
    schedule: Tuple[Mapping[str, Any], ...]
    bound_by_id: Mapping[str, Any]
    config: Mapping[str, Any]
    config_sha256: str
    artifact_sha256: Mapping[str, str]
    smoke_result_sha256: str
    preflight_cost_upper_bound_usd: float
    cost_cap_usd: float


def _decode_exact_json(raw: bytes, label: str) -> Mapping[str, Any]:
    try:
        value = json.loads(
            raw.decode("utf-8", errors="strict"),
            object_pairs_hook=_object_without_duplicate_keys,
            parse_constant=_reject_json_constant,
        )
    except (UnicodeDecodeError, TypeError, ValueError, json.JSONDecodeError) as exc:
        raise ValueError("%s is not exact UTF-8 JSON" % label) from exc
    if type(value) is not dict:
        raise ValueError("%s root must be an exact object" % label)
    return value


def _validate_roster(roster: Any) -> None:
    fields = {
        "completion_price_per_token_usd",
        "endpoint_name",
        "family",
        "model_id",
        "prompt_price_per_token_usd",
        "provider",
        "vendor",
    }
    if type(roster) is not list or len(roster) != 3:
        raise ValueError("diagnostic model roster must contain exactly three rows")
    for row in roster:
        if type(row) is not dict or set(row) != fields:
            raise ValueError("diagnostic model roster schema is not exact")
        if any(
            type(row[field]) is not str or not row[field]
            for field in ("endpoint_name", "family", "model_id", "provider", "vendor")
        ):
            raise ValueError("diagnostic roster has a blank identity")
        for field in (
            "prompt_price_per_token_usd",
            "completion_price_per_token_usd",
        ):
            try:
                price = float(row[field])
            except (TypeError, ValueError):
                raise ValueError("diagnostic roster price is invalid") from None
            if not math.isfinite(price) or price <= 0:
                raise ValueError("diagnostic roster price must be positive")
    if (
        len({row["model_id"] for row in roster}) != 3
        or len({row["vendor"] for row in roster}) < 2
        or len({row["provider"] for row in roster}) < 2
    ):
        raise ValueError("diagnostic model/vendor/provider roster is invalid")


def load_frozen_diagnostic_config(
    config_path: Optional[Path] = None,
) -> Tuple[Mapping[str, Any], str]:
    path = CONFIG_PATH if config_path is None else Path(config_path)
    if not path.is_file():
        raise ValueError("frozen diagnostic config is missing")
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != CONFIG_SHA256:
        raise ValueError("diagnostic config hash does not match the frozen config")
    config = _decode_exact_json(raw, "diagnostic config")
    expected_fields = {
        "artifact_sha256",
        "authoring_boundary",
        "blockers",
        "catalog_checked_at",
        "catalog_source",
        "cost_cap_usd",
        "data_basis",
        "eligible_for_empirical_decision",
        "max_paid_calls",
        "max_tokens",
        "mode",
        "model_roster",
        "provider_policy",
        "run_id",
        "scheduled_requests",
        "schema_version",
        "seed",
        "smoke_authorization",
        "status",
        "study_id",
        "syntax_repairs_per_request",
    }
    if type(config) is not dict or set(config) != expected_fields:
        raise ValueError("diagnostic config root schema is not exact")
    exact_values = {
        "schema_version": 1,
        "study_id": "SKIM-P1",
        "run_id": "SKIM-P1-CHEAP-OPENROUTER-FULL-20260711-R1",
        "mode": RUN_STATUS,
        "data_basis": "external_model_responses",
        "status": "NOT_RUN",
        "eligible_for_empirical_decision": False,
        "authoring_boundary": "POST_SMOKE_PRE_FULL",
        "seed": 20260711,
        "scheduled_requests": 2400,
        "max_paid_calls": 4800,
        "syntax_repairs_per_request": 1,
        "max_tokens": 256,
        "cost_cap_usd": 1.0,
        "catalog_source": "https://openrouter.ai/api/v1/models",
        "provider_policy": {"allow_fallbacks": False, "require_parameters": True},
    }
    if any(config.get(field) != expected for field, expected in exact_values.items()):
        raise ValueError("diagnostic config values differ from the frozen protocol")
    _validate_roster(config["model_roster"])
    if config["artifact_sha256"] != {
        "bank": "b086718e70be89f7d7566bba058f8ebe52add4e6768ac5bed5a539a02608d385",
        "gold": "6d798c21e024f2ab5a8b987b968605ae3e5724840b612afc5c029a2232411e1b",
        "runtime": "258309b788b450f24484bbd946da6b45980589c879e794c485f065eb8229005f",
        "free_diversion_schedule": "afc2b580824f344ce136fa08e136c30aa4b2a8d6df5ebfd6658e379bcb023e7d",
        "cue_comprehension_schedule": "89559415535c94d45a3d5b9c158909d0acb75ce8d15efb8d09b75949de005f3b",
    }:
        raise ValueError("diagnostic artifact hashes differ from the frozen bank")
    if config["smoke_authorization"] != {
        "smoke_config_sha256": "5cf79207e29a38b2465c524f272e4cf8b97600267b46b2479373ca363f215597",
        "smoke_result_sha256": "802b91ca8b01d346bd47fac55e4219ccc6f3b4cc26edb45243946c1dca746188",
        "smoke_status": "CHEAP_MODEL_ENGINEERING_SMOKE_COMPLETE",
        "smoke_scheduled_requests": 9,
        "smoke_paid_calls": 9,
    }:
        raise ValueError("diagnostic smoke authorization is invalid")
    if config["blockers"] != [
        "ONE_SEED",
        "CHEAP_ENGINEERING_ROSTER",
        "NOT_RUN_PROFESSIONAL_REALISM",
        "NOT_RUN_HUMAN_BASELINE",
        "NO_FROZEN_EXTERNAL_CAPABILITY_PC1",
        "NOT_RUN_LLM",
    ]:
        raise ValueError("diagnostic blockers differ from the frozen disclosure")
    return MappingProxyType(config), digest


def _bind_clients(clients: Sequence[Any], config: Mapping[str, Any]) -> None:
    roster = tuple(clients)
    expected = tuple(
        (row["model_id"], row["family"], row["vendor"], row["provider"])
        for row in config["model_roster"]
    )
    observed = tuple(
        (
            getattr(client, "model_id", None),
            getattr(client, "family", None),
            getattr(client, "vendor", None),
            getattr(client, "provider", None),
        )
        for client in roster
    )
    if observed != expected:
        raise ValueError("diagnostic client roster does not match the frozen models")
    for client in roster:
        if not callable(getattr(client, "generate", None)):
            raise ValueError("diagnostic client is missing generate")
        if getattr(client, "max_tokens", None) != config["max_tokens"]:
            raise ValueError("diagnostic client max_tokens differs from config")
        cap = getattr(client, "cost_cap_usd", None)
        if type(cap) not in (int, float) or float(cap) != config["cost_cap_usd"]:
            raise ValueError("diagnostic client cost cap differs from config")


def _verify_conditional_schedules(config: Mapping[str, Any]) -> None:
    paths = {
        "free_diversion_schedule": ROOT
        / "itembank/runtime/p1-free-diversion-schedule.jsonl",
        "cue_comprehension_schedule": ROOT
        / "itembank/runtime/p1-cue-comprehension-schedule.jsonl",
    }
    for key, path in paths.items():
        raw = path.read_bytes()
        if (
            hashlib.sha256(raw).hexdigest() != config["artifact_sha256"][key]
            or not raw.endswith(b"\n")
            or len(raw[:-1].split(b"\n")) != 40
        ):
            raise ValueError("conditional schedule hash/count mismatch: %s" % key)


def verify_live_catalog(
    config: Mapping[str, Any],
    *,
    api_key: str,
    opener: Optional[Any] = None,
) -> Mapping[str, Any]:
    """Verify each exact pinned provider endpoint immediately before a run."""

    if (
        type(api_key) is not str
        or not api_key
        or api_key.strip() != api_key
        or any(ord(character) < 33 or ord(character) > 126 for character in api_key)
    ):
        raise ValueError("catalog API key must be header-safe text")
    if not isinstance(config, Mapping) or type(config.get("model_roster")) is not list:
        raise TypeError("catalog verification requires the frozen config")
    transport = urllib.request.urlopen if opener is None else opener
    if not callable(transport):
        raise TypeError("catalog opener must be callable")
    required_parameters = {"max_tokens", "temperature", "seed", "response_format"}
    verified_models = []
    verified_providers = []
    for row in config["model_roster"]:
        url = "https://openrouter.ai/api/v1/models/%s/endpoints" % row["model_id"]
        request = urllib.request.Request(
            url,
            headers={
                "Accept": "application/json",
                "Authorization": "Bearer " + api_key,
                "User-Agent": "10cbench-skim-p1/1",
            },
            method="GET",
        )
        try:
            with transport(request, timeout=30) as response:
                status = getattr(response, "status", 200)
                raw = response.read()
        except Exception as exc:
            raise RuntimeError(
                "OpenRouter endpoint catalog request failed for %s" % row["model_id"]
            ) from exc
        if status != 200 or type(raw) is not bytes or len(raw) > 10_000_000:
            raise RuntimeError("OpenRouter endpoint catalog response is invalid")
        payload = _decode_exact_json(raw, "OpenRouter endpoint catalog")
        data = payload.get("data")
        endpoints = data.get("endpoints") if type(data) is dict else None
        if (
            type(data) is not dict
            or data.get("id") != row["model_id"]
            or type(endpoints) is not list
        ):
            raise ValueError("catalog model identity or endpoints are invalid")
        matches = []
        for endpoint in endpoints:
            if type(endpoint) is not dict:
                continue
            pricing = endpoint.get("pricing")
            parameters = endpoint.get("supported_parameters")
            if (
                endpoint.get("name") == row["endpoint_name"]
                and endpoint.get("provider_name") == row["provider"]
                and type(pricing) is dict
                and pricing.get("prompt") == row["prompt_price_per_token_usd"]
                and pricing.get("completion")
                == row["completion_price_per_token_usd"]
                and type(parameters) is list
                and required_parameters.issubset(parameters)
            ):
                matches.append(endpoint)
        if len(matches) != 1 or type(matches[0].get("status")) is not int or matches[0][
            "status"
        ] != 0:
            raise ValueError(
                "catalog endpoint price, parameters, or status is not exact/healthy"
            )
        verified_models.append(row["model_id"])
        verified_providers.append(row["provider"])
    return {
        "verified": True,
        "model_ids": verified_models,
        "providers": verified_providers,
    }


def _verify_smoke(
    smoke_dir: Path,
    config: Mapping[str, Any],
    bound_by_id: Mapping[str, Any],
) -> str:
    path = Path(smoke_dir) / "smoke-result.json"
    if not path.is_file():
        raise ValueError("smoke result is missing")
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != config["smoke_authorization"]["smoke_result_sha256"]:
        raise ValueError("smoke result hash does not match authorization")
    smoke = _decode_exact_json(raw, "smoke result")
    if raw != (canonical_json(smoke) + "\n").encode("utf-8"):
        raise ValueError("smoke result is not canonical JSON")
    if (
        smoke.get("status") != "CHEAP_MODEL_ENGINEERING_SMOKE_COMPLETE"
        or smoke.get("eligible_for_empirical_decision") is not False
        or smoke.get("seed") != config["seed"]
        or smoke.get("scheduled_requests") != 9
        or smoke.get("paid_calls") != 9
        or smoke.get("smoke_config_sha256")
        != config["smoke_authorization"]["smoke_config_sha256"]
        or smoke.get("artifact_sha256")
        != {key: config["artifact_sha256"][key] for key in ("bank", "gold", "runtime")}
        or type(smoke.get("episodes")) is not list
        or len(smoke["episodes"]) != 9
    ):
        raise ValueError("smoke result does not prove the frozen engineering smoke")
    expected_pairs = tuple(
        (row["model_id"], request_id)
        for row in config["model_roster"]
        for request_id in (
            "skim-p1-f1-expense-audit-platform-first-primary-request-unstated",
            "skim-p1-f1-expense-audit-platform-first-clean-request-unstated",
            "skim-p1-f1-expense-audit-platform-first-recognition-request-unstated",
        )
    )
    roster_by_model = {
        row["model_id"]: row for row in config["model_roster"]
    }
    for index, (episode, expected_pair) in enumerate(zip(smoke["episodes"], expected_pairs)):
        metadata_rows = episode.get("call_metadata")
        metadata = (
            metadata_rows[-1]
            if type(metadata_rows) is list and metadata_rows
            else None
        )
        if (
            type(episode) is not dict
            or (episode.get("model_id"), episode.get("request_id")) != expected_pair
            or episode.get("schedule_index") != index
            or episode.get("seed") != config["seed"]
            or episode.get("status") not in {"VALID_TERMINAL", "VALID_TERMINAL_AFTER_REPAIR"}
            or episode.get("mechanical_score", {}).get("status") != "SCORED"
            or type(metadata) is not dict
            or metadata.get("requested_model") != episode.get("model_id")
            or metadata.get("provider")
            != roster_by_model[episode["model_id"]]["provider"]
        ):
            raise ValueError("smoke episode is not a valid terminal proof")
        event_path = Path(smoke_dir) / "events" / ("episode-%03d.jsonl" % index)
        resume_bound_action(
            bound_by_id[episode["request_id"]],
            episode_id="%s--%s--seed-%d"
            % (episode["model_id"], episode["request_id"], episode["seed"]),
            event_log_path=event_path,
        )
    serialized = canonical_json(smoke).lower()
    if any(
        marker in serialized
        for marker in ("mechanical_action_map", "private_gold", '"raw_response"')
    ):
        raise ValueError("smoke result contains forbidden private/raw fields")
    return digest


def preflight_diagnostic(
    *,
    clients: Sequence[Any],
    smoke_dir: Path,
    config_path: Optional[Path] = None,
) -> DiagnosticPlan:
    """Validate the complete full schedule without output or model calls."""

    config, config_sha256 = load_frozen_diagnostic_config(config_path)
    roster = tuple(clients)
    if len(roster) != 3:
        raise ValueError("diagnostic requires exactly three clients")
    _bind_clients(roster, config)
    bundle = load_frozen_bundle()
    if dict(bundle.artifact_sha256) != {
        key: config["artifact_sha256"][key] for key in ("bank", "gold", "runtime")
    }:
        raise ValueError("diagnostic bundle differs from frozen config")
    _verify_conditional_schedules(config)
    bound_by_id = {}
    for runtime_row in bundle.runtime:
        request_id = runtime_row["runtime_request_id"]
        logical_id = runtime_row["source_logical_record_id"]
        bound_by_id[request_id] = bind_runtime_request(
            runtime_row,
            bundle.public_by_id[logical_id],
            bundle.gold_by_id[logical_id],
        )
    smoke_sha256 = _verify_smoke(smoke_dir, config, bound_by_id)
    model_ids = tuple(row["model_id"] for row in config["model_roster"])
    schedule = build_p1_schedule(model_ids, (config["seed"],), bundle.runtime)
    if len(schedule) != config["scheduled_requests"]:
        raise ValueError("diagnostic schedule count differs from frozen config")
    upper_bound = 0.0
    for row in schedule:
        request = model_adapters.build_model_request(
            bound_by_id[row["runtime_request_id"]].runtime_row
        )
        upper_bound = math.fsum(
            (
                upper_bound,
                _configured_call_cost_upper_bound(config, row["model_id"], request),
                _configured_call_cost_upper_bound(
                    config, row["model_id"], _repair_request(request)
                ),
            )
        )
    if upper_bound > config["cost_cap_usd"]:
        raise ValueError("diagnostic schedule could exceed the frozen cost cap")
    return DiagnosticPlan(
        status=RUN_STATUS,
        eligible_for_empirical_decision=False,
        seed=config["seed"],
        clients=roster,
        schedule=schedule,
        bound_by_id=MappingProxyType(bound_by_id),
        config=config,
        config_sha256=config_sha256,
        artifact_sha256=MappingProxyType(dict(config["artifact_sha256"])),
        smoke_result_sha256=smoke_sha256,
        preflight_cost_upper_bound_usd=upper_bound,
        cost_cap_usd=float(config["cost_cap_usd"]),
    )


_ZERO_HASH = "0" * 64


def _checkpoint_digest(row: Mapping[str, Any]) -> str:
    payload = dict(row)
    payload["checkpoint_sha256"] = None
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


def _checkpoint_path(output_dir: Path, model_index: int) -> Path:
    return Path(output_dir) / "checkpoints" / ("model-%d.jsonl" % model_index)


def _append_checkpoint(path: Path, episode: Mapping[str, Any], previous: str) -> str:
    row = {
        "schema_version": 1,
        "model_id": episode["model_id"],
        "schedule_index": episode["schedule_index"],
        "previous_checkpoint_sha256": previous,
        "checkpoint_sha256": None,
        "episode": dict(episode),
    }
    row["checkpoint_sha256"] = _checkpoint_digest(row)
    line = (canonical_json(row) + "\n").encode("utf-8")
    with path.open("ab") as handle:
        written = handle.write(line)
        if written != len(line):
            raise OSError("short diagnostic checkpoint append")
        handle.flush()
        os.fsync(handle.fileno())
    return row["checkpoint_sha256"]


def _load_checkpoints(
    path: Path,
    group: Sequence[Mapping[str, Any]],
    plan: DiagnosticPlan,
    scorer: Any,
) -> Tuple[Mapping[str, Any], ...]:
    if not path.exists():
        return tuple()
    if not path.is_file():
        raise ValueError("diagnostic checkpoint target is not a file")
    raw = path.read_bytes()
    if not raw or not raw.endswith(b"\n"):
        raise ValueError("diagnostic checkpoint is empty or incomplete")
    lines = raw[:-1].split(b"\n")
    if any(not line for line in lines):
        raise ValueError("diagnostic checkpoint contains a blank line")
    if len(lines) > len(group):
        raise ValueError("diagnostic checkpoint exceeds its schedule")
    previous = _ZERO_HASH
    episodes = []
    expected_fields = {
        "schema_version",
        "model_id",
        "schedule_index",
        "previous_checkpoint_sha256",
        "checkpoint_sha256",
        "episode",
    }
    for offset, (line, schedule_row) in enumerate(zip(lines, group)):
        row = _decode_exact_json(line, "diagnostic checkpoint row")
        if line != canonical_json(row).encode("utf-8"):
            raise ValueError("diagnostic checkpoint row is not canonical")
        if type(row) is not dict or set(row) != expected_fields:
            raise ValueError("diagnostic checkpoint row schema is invalid")
        episode = row["episode"]
        if (
            row["schema_version"] != 1
            or row["model_id"] != schedule_row["model_id"]
            or row["schedule_index"] != schedule_row["schedule_index"]
            or row["previous_checkpoint_sha256"] != previous
            or row["checkpoint_sha256"] != _checkpoint_digest(row)
            or type(episode) is not dict
            or episode.get("model_id") != schedule_row["model_id"]
            or episode.get("request_id") != schedule_row["runtime_request_id"]
            or episode.get("seed") != schedule_row["seed"]
            or episode.get("schedule_index") != schedule_row["schedule_index"]
        ):
            raise ValueError("diagnostic checkpoint chain or schedule binding failed")
        event_name = "episode-%05d.jsonl" % schedule_row["schedule_index"]
        event_path = path.parents[1] / "events" / event_name
        if episode.get("status") in {
            "VALID_TERMINAL",
            "VALID_TERMINAL_AFTER_REPAIR",
        }:
            if episode.get("event_log") != "events/" + event_name:
                raise ValueError("diagnostic checkpoint event path is invalid")
            execution = resume_bound_action(
                plan.bound_by_id[schedule_row["runtime_request_id"]],
                episode_id="%s--%s--seed-%d"
                % (
                    schedule_row["model_id"],
                    schedule_row["runtime_request_id"],
                    schedule_row["seed"],
                ),
                event_log_path=event_path,
            )
            derived = _sanitized_score(
                scorer.score_terminal_episode(
                    execution,
                    plan.bound_by_id[schedule_row["runtime_request_id"]].private_gold,
                )
            )
            if episode.get("mechanical_score") != derived:
                raise ValueError("diagnostic checkpoint score is detached or stale")
        else:
            if episode.get("event_log") is not None or event_path.exists():
                raise ValueError("parked diagnostic checkpoint has an event artifact")
        if (
            type(episode.get("paid_calls")) is not int
            or not 1 <= episode["paid_calls"] <= 2
            or type(episode.get("cost_usd")) not in (int, float)
            or not math.isfinite(float(episode["cost_usd"]))
            or episode["cost_usd"] < 0
        ):
            raise ValueError("diagnostic checkpoint cost accounting is invalid")
        serialized = canonical_json(episode).lower()
        if any(
            marker in serialized
            for marker in ("mechanical_action_map", "private_gold", '"raw_response"')
        ):
            raise ValueError("diagnostic checkpoint contains forbidden content")
        episodes.append(episode)
        previous = row["checkpoint_sha256"]
    return tuple(episodes)


def _retry_policy_active(plan: DiagnosticPlan) -> bool:
    observed = tuple(
        (
            getattr(client, "max_attempts", None),
            getattr(client, "retry_base_seconds", None),
        )
        for client in plan.clients
    )
    if not any(row != (None, None) for row in observed):
        return False
    if any(row != (3, 1.0) for row in observed):
        raise ValueError("diagnostic client retry policy is not the frozen repair")
    return True


def _validate_transport_repair_attestation(
    output_dir: Path,
    plan: DiagnosticPlan,
) -> str:
    """Bind the immutable pre-resume R1 prefix before any new network call."""

    output_dir = Path(output_dir)
    path = output_dir / TRANSPORT_REPAIR_ATTESTATION_NAME
    if not path.is_file():
        raise ValueError("frozen transport repair attestation is missing")
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != TRANSPORT_REPAIR_ATTESTATION_SHA256:
        raise ValueError("transport repair attestation hash is not trusted")
    attestation = _decode_exact_json(raw, "transport repair attestation")
    if raw != (canonical_json(attestation) + "\n").encode("utf-8"):
        raise ValueError("transport repair attestation is not canonical JSON")
    expected_fields = {
        "code_sha256",
        "config_sha256",
        "created_at",
        "diagnostic_failure_sha256",
        "eligible_for_empirical_decision",
        "operator_observation",
        "preservation",
        "record_type",
        "resume_boundary",
        "run_id",
        "schema_version",
        "smoke_result_sha256",
        "status",
        "study_id",
        "transport_policy",
        "unchanged_protocol_fields",
    }
    if type(attestation) is not dict or set(attestation) != expected_fields:
        raise ValueError("transport repair attestation schema is not exact")
    if (
        attestation["schema_version"] != 1
        or attestation["record_type"]
        != "SKIM_P1_TRANSPORT_REPAIR_PRE_RESUME_ATTESTATION"
        or attestation["status"] != "FROZEN_PRE_RESUME"
        or attestation["study_id"] != "SKIM-P1"
        or attestation["run_id"] != plan.config["run_id"]
        or attestation["eligible_for_empirical_decision"] is not False
        or attestation["config_sha256"] != plan.config_sha256
        or attestation["smoke_result_sha256"] != plan.smoke_result_sha256
    ):
        raise ValueError("transport repair attestation identity is invalid")
    if attestation["transport_policy"] != {
        "attempt_count_semantics": "TOTAL_HTTP_ATTEMPTS",
        "honor_numeric_retry_after": True,
        "max_transport_attempts": 3,
        "paid_call_semantics": "COUNT_ONLY_RESPONSES_WITH_NUMERIC_USAGE_COST",
        "request_body_reused_byte_for_byte": True,
        "retry_base_seconds": 1.0,
        "retry_delay_cap_seconds": 30.0,
        "retry_http_5xx": False,
        "retry_multiplier": 2,
        "retry_os_errors": False,
        "retry_response_errors": False,
        "retry_timeouts": False,
        "retry_url_errors": False,
        "retryable_http_statuses": [429],
    }:
        raise ValueError("transport repair policy differs from authorization")
    if attestation["unchanged_protocol_fields"] != [
        "artifact_sha256",
        "cost_cap_usd",
        "max_tokens",
        "model_roster",
        "provider_policy",
        "schedule",
        "scoring",
        "seed",
        "smoke_authorization",
    ]:
        raise ValueError("transport repair changed a scientific protocol field")

    code = attestation["code_sha256"]
    expected_code = {
        "model_adapters_post_repair": hashlib.sha256(
            (ROOT / "harness" / "model_adapters.py").read_bytes()
        ).hexdigest(),
        "model_adapters_pre_repair": (
            "aa307c038968960df60ca6eb2028976969fb1825d3ccbd8d1e8c94dcfaf7407f"
        ),
        "run_p1": hashlib.sha256(
            (ROOT / "harness" / "run_p1.py").read_bytes()
        ).hexdigest(),
    }
    if code != expected_code:
        raise ValueError("transport repair source hashes are not exact")
    failure_path = output_dir / "diagnostic-failure.json"
    if (
        not failure_path.is_file()
        or hashlib.sha256(failure_path.read_bytes()).hexdigest()
        != attestation["diagnostic_failure_sha256"]
    ):
        raise ValueError("transport repair failure artifact binding failed")

    boundary = attestation["resume_boundary"]
    boundary_fields = {
        "accepted_response_rows",
        "checkpoint_prefixes",
        "checkpoint_rows",
        "cost_usd_accounted",
        "event_bytes",
        "event_files",
        "event_manifest_algorithm",
        "event_manifest_sha256",
        "lock_files",
        "locks_zero_bytes",
        "paid_calls_accounted",
        "parked_rows",
        "parked_schedule_indices",
        "rejected_response_rows",
        "response_metadata_rows",
        "valid_terminal_rows",
    }
    if type(boundary) is not dict or set(boundary) != boundary_fields:
        raise ValueError("transport repair resume boundary schema is invalid")
    prefixes = boundary["checkpoint_prefixes"]
    if type(prefixes) is not list or len(prefixes) != 3:
        raise ValueError("transport repair checkpoint prefixes are invalid")
    episodes = []
    for prefix in prefixes:
        if type(prefix) is not dict or set(prefix) != {
            "bytes",
            "chain_head_sha256",
            "model_id",
            "next_schedule_index",
            "path",
            "prefix_sha256",
            "rows",
        }:
            raise ValueError("transport repair checkpoint prefix schema is invalid")
        checkpoint_path = output_dir / prefix["path"]
        if not checkpoint_path.is_file():
            raise ValueError("transport repair checkpoint prefix is missing")
        checkpoint_raw = checkpoint_path.read_bytes()
        byte_count = prefix["bytes"]
        if type(byte_count) is not int or byte_count <= 0 or len(checkpoint_raw) < byte_count:
            raise ValueError("transport repair checkpoint prefix length is invalid")
        frozen_prefix = checkpoint_raw[:byte_count]
        if (
            not frozen_prefix.endswith(b"\n")
            or hashlib.sha256(frozen_prefix).hexdigest() != prefix["prefix_sha256"]
        ):
            raise ValueError("transport repair checkpoint prefix hash failed")
        lines = frozen_prefix[:-1].split(b"\n")
        if len(lines) != prefix["rows"]:
            raise ValueError("transport repair checkpoint prefix row count failed")
        decoded = [
            _decode_exact_json(line, "transport repair checkpoint row")
            for line in lines
        ]
        last = decoded[-1]
        if (
            last.get("checkpoint_sha256") != prefix["chain_head_sha256"]
            or last.get("model_id") != prefix["model_id"]
            or last.get("schedule_index") + 1 != prefix["next_schedule_index"]
        ):
            raise ValueError("transport repair checkpoint chain head failed")
        episodes.extend(row.get("episode") for row in decoded)
    if any(type(episode) is not dict for episode in episodes):
        raise ValueError("transport repair checkpoint episode is invalid")

    valid_statuses = {"VALID_TERMINAL", "VALID_TERMINAL_AFTER_REPAIR"}
    valid = [episode for episode in episodes if episode["status"] in valid_statuses]
    parked = [episode for episode in episodes if episode["status"] not in valid_statuses]
    metadata_rows = [
        episode
        for episode in episodes
        if type(episode.get("call_metadata")) is list and episode["call_metadata"]
    ]
    metadata_statuses = [
        metadata.get("response_status")
        for episode in metadata_rows
        for metadata in episode["call_metadata"]
        if type(metadata) is dict
    ]
    parked_indices = [
        {
            "failure_type": episode.get("failure_type"),
            "response_metadata_present": bool(episode.get("call_metadata")),
            "schedule_index": episode.get("schedule_index"),
        }
        for episode in parked
    ]
    cost = math.fsum(float(episode["cost_usd"]) for episode in episodes)
    if (
        len(episodes) != boundary["checkpoint_rows"]
        or len(valid) != boundary["valid_terminal_rows"]
        or len(parked) != boundary["parked_rows"]
        or len(metadata_rows) != boundary["response_metadata_rows"]
        or metadata_statuses.count("ACCEPTED") != boundary["accepted_response_rows"]
        or metadata_statuses.count("REJECTED_RESPONSE")
        != boundary["rejected_response_rows"]
        or sum(episode["paid_calls"] for episode in episodes)
        != boundary["paid_calls_accounted"]
        or not math.isclose(
            cost,
            float(boundary["cost_usd_accounted"]),
            rel_tol=0.0,
            abs_tol=1e-15,
        )
        or parked_indices != boundary["parked_schedule_indices"]
    ):
        raise ValueError("transport repair aggregate checkpoint proof failed")

    event_rows = []
    event_bytes = 0
    lock_paths = []
    for episode in valid:
        event_rel = episode.get("event_log")
        if type(event_rel) is not str or not event_rel.startswith("events/episode-"):
            raise ValueError("transport repair event reference is invalid")
        event_path = output_dir / event_rel
        if not event_path.is_file():
            raise ValueError("transport repair event artifact is missing")
        event_raw = event_path.read_bytes()
        event_bytes += len(event_raw)
        event_rows.append(
            {"path": event_rel, "sha256": hashlib.sha256(event_raw).hexdigest()}
        )
        lock_paths.append(event_path.with_name("." + event_path.name + ".lock"))
    event_rows.sort(key=lambda row: row["path"])
    event_manifest = hashlib.sha256(canonical_json(event_rows).encode("utf-8")).hexdigest()
    if (
        boundary["event_manifest_algorithm"]
        != "SHA256(CANONICAL_JSON(SORTED[{path,sha256}]))"
        or len(event_rows) != boundary["event_files"]
        or event_bytes != boundary["event_bytes"]
        or event_manifest != boundary["event_manifest_sha256"]
        or len(lock_paths) != boundary["lock_files"]
        or boundary["locks_zero_bytes"] is not True
        or any(not path.is_file() or path.stat().st_size != 0 for path in lock_paths)
    ):
        raise ValueError("transport repair event manifest or locks failed")
    return digest


def _execute_diagnostic_schedule(
    plan: DiagnosticPlan,
    schedule: Sequence[Mapping[str, Any]],
    *,
    output_dir: Path,
    resume: bool,
    max_workers: int,
) -> Tuple[Mapping[str, Any], ...]:
    """Execute a validated schedule with per-model hash-chained checkpoints."""

    if type(plan) is not DiagnosticPlan:
        raise TypeError("plan must be an exact DiagnosticPlan")
    if type(resume) is not bool:
        raise TypeError("resume must be an exact boolean")
    if type(max_workers) is not int or not 1 <= max_workers <= 3:
        raise ValueError("diagnostic max_workers must be in [1, 3]")
    rows = tuple(schedule)
    if not rows:
        raise ValueError("diagnostic execution schedule must not be empty")
    plan_by_index = {row["schedule_index"]: row for row in plan.schedule}
    seen = set()
    for row in rows:
        index = row.get("schedule_index") if isinstance(row, Mapping) else None
        if (
            type(index) is not int
            or index in seen
            or index not in plan_by_index
            or dict(row) != dict(plan_by_index[index])
        ):
            raise ValueError("diagnostic execution schedule is not a frozen subset")
        seen.add(index)

    output_dir = Path(output_dir)
    if resume:
        if not output_dir.is_dir():
            raise ValueError("diagnostic resume requires an existing output directory")
        if not (output_dir / "events").is_dir() or not (
            output_dir / "checkpoints"
        ).is_dir():
            raise ValueError("diagnostic resume directory is incomplete")
    else:
        if output_dir.exists():
            raise ValueError("diagnostic output directory must be fresh")
        output_dir.mkdir(parents=True, exist_ok=False)
        (output_dir / "events").mkdir(exist_ok=False)
        (output_dir / "checkpoints").mkdir(exist_ok=False)

    model_ids = tuple(row["model_id"] for row in plan.config["model_roster"])
    clients_by_id = dict(zip(model_ids, plan.clients))
    groups = {
        model_id: tuple(row for row in rows if row["model_id"] == model_id)
        for model_id in model_ids
    }
    scorer = _mechanical_scorer()
    if scorer is None:
        raise RuntimeError("mechanical scorer is required for diagnostic execution")

    # Validate every existing checkpoint and any orphan-event boundary before
    # the first new model call.
    completed_by_model = {}
    for model_index, model_id in enumerate(model_ids):
        group = groups[model_id]
        path = _checkpoint_path(output_dir, model_index)
        completed = _load_checkpoints(path, group, plan, scorer)
        for row in group[len(completed) :]:
            event_path = output_dir / "events" / (
                "episode-%05d.jsonl" % row["schedule_index"]
            )
            if event_path.exists():
                raise ValueError(
                    "orphan diagnostic event exists without a checkpoint"
                )
        completed_by_model[model_id] = completed

    if resume and any(completed_by_model.values()) and _retry_policy_active(plan):
        # Revalidate at the last safe boundary immediately before worker
        # threads. CLI execution also performs this check before catalog I/O.
        _validate_transport_repair_attestation(output_dir, plan)

    stop_event = threading.Event()

    def run_model(model_id: str) -> Tuple[Mapping[str, Any], ...]:
        model_index = model_ids.index(model_id)
        group = groups[model_id]
        completed = list(completed_by_model[model_id])
        spent = math.fsum(float(row["cost_usd"]) for row in completed)
        paid_calls = sum(row["paid_calls"] for row in completed)
        model_bound = 0.0
        for row in group:
            request = model_adapters.build_model_request(
                plan.bound_by_id[row["runtime_request_id"]].runtime_row
            )
            model_bound = math.fsum(
                (
                    model_bound,
                    _configured_call_cost_upper_bound(
                        plan.config, model_id, request
                    ),
                    _configured_call_cost_upper_bound(
                        plan.config, model_id, _repair_request(request)
                    ),
                )
            )
        if spent > model_bound:
            raise ValueError("checkpoint spend exceeds model schedule bound")
        budget = _AggregateBudget(
            cap_usd=model_bound,
            spent_usd=spent,
            paid_calls=paid_calls,
        )
        client = clients_by_id[model_id]
        checkpoint = _checkpoint_path(output_dir, model_index)
        previous = _ZERO_HASH
        if completed:
            last_line = checkpoint.read_bytes()[:-1].split(b"\n")[-1]
            previous = _decode_exact_json(
                last_line, "diagnostic checkpoint row"
            )["checkpoint_sha256"]
        for row in group[len(completed) :]:
            if stop_event.is_set():
                break
            event_name = "episode-%05d.jsonl" % row["schedule_index"]
            calls_before = budget.paid_calls
            spent_before = budget.spent_usd
            try:
                episode, execution = _execute_runtime_request(
                    plan.bound_by_id[row["runtime_request_id"]],
                    client,
                    seed=row["seed"],
                    event_log_path=output_dir / "events" / event_name,
                    budget=budget,
                    smoke_config=plan.config,
                )
            except Exception as exc:
                recorded_cost_delta = budget.spent_usd - spent_before
                request = model_adapters.build_model_request(
                    plan.bound_by_id[row["runtime_request_id"]].runtime_row
                )
                full_episode_bound = math.fsum(
                    (
                        _configured_call_cost_upper_bound(
                            plan.config, model_id, request
                        ),
                        _configured_call_cost_upper_bound(
                            plan.config, model_id, _repair_request(request)
                        ),
                    )
                )
                # The shared request executor deliberately re-raises the
                # original client exception.  At this boundary we cannot
                # always distinguish a failed initial call from a failed
                # repair after one successful charged call.  Reserve the full
                # two-call episode and never undercount a reported anomaly.
                paid_delta = 2
                cost_delta = max(recorded_cost_delta, full_episode_bound)
                accounting_status = (
                    "CONSERVATIVE_MAX_REPORTED_OR_FULL_EPISODE_UPPER_BOUND"
                )
                try:
                    safe_metadata = [dict(_sanitized_call_metadata(client))]
                except Exception:
                    safe_metadata = []
                episode = {
                    "request_id": row["runtime_request_id"],
                    "model_id": model_id,
                    "model_family": getattr(client, "family", None),
                    "vendor": getattr(client, "vendor", None),
                    "seed": row["seed"],
                    "status": "PARKED_MODEL_CALL_ABORT",
                    "paid_calls": paid_delta,
                    "event_count": 0,
                    "syntax_repair_used": paid_delta > 1,
                    "cost_usd": cost_delta,
                    "call_metadata": safe_metadata,
                    "schedule_index": row["schedule_index"],
                    "event_log": None,
                    "cost_accounting_status": accounting_status,
                    "failure_type": type(exc).__name__,
                    "failure_code": "MODEL_CALL_ABORTED_NO_AUTOMATIC_RETRY",
                }
                previous = _append_checkpoint(checkpoint, episode, previous)
                completed.append(episode)
                stop_event.set()
                raise
            episode["schedule_index"] = row["schedule_index"]
            episode["event_log"] = (
                "events/" + event_name if execution is not None else None
            )
            if execution is not None:
                episode["mechanical_score"] = _sanitized_score(
                    scorer.score_terminal_episode(
                        execution,
                        plan.bound_by_id[row["runtime_request_id"]].private_gold,
                    )
                )
            previous = _append_checkpoint(checkpoint, episode, previous)
            completed.append(episode)
        return tuple(completed)

    active = tuple(model_id for model_id in model_ids if groups[model_id])
    try:
        with ThreadPoolExecutor(max_workers=min(max_workers, len(active))) as executor:
            futures = {
                executor.submit(run_model, model_id): model_id
                for model_id in active
            }
            results_by_model = {}
            for future in as_completed(futures):
                model_id = futures[future]
                try:
                    results_by_model[model_id] = future.result()
                except Exception:
                    stop_event.set()
                    for pending in futures:
                        pending.cancel()
                    raise
            grouped_results = tuple(
                results_by_model[model_id] for model_id in active
            )
    except Exception as exc:
        accounted = []
        for checkpoint_path in sorted((output_dir / "checkpoints").glob("*.jsonl")):
            raw = checkpoint_path.read_bytes()
            if not raw.endswith(b"\n"):
                continue
            for line in raw[:-1].split(b"\n"):
                try:
                    row = _decode_exact_json(line, "diagnostic checkpoint row")
                    episode = row.get("episode")
                except Exception:
                    continue
                if type(episode) is dict:
                    accounted.append(episode)
        failure_path = output_dir / "diagnostic-failure.json"
        if not failure_path.exists():
            failure = {
                "schema_version": 1,
                "study_id": "SKIM-P1",
                "run_id": plan.config["run_id"],
                "status": "CHEAP_DIAGNOSTIC_ABORTED",
                "eligible_for_empirical_decision": False,
                "scheduled_requests": len(rows),
                "checkpointed_episodes": len(accounted),
                "paid_calls_accounted": sum(
                    episode.get("paid_calls", 0)
                    for episode in accounted
                    if type(episode.get("paid_calls")) is int
                ),
                "total_cost_usd_accounted": math.fsum(
                    float(episode["cost_usd"])
                    for episode in accounted
                    if type(episode.get("cost_usd")) in (int, float)
                    and math.isfinite(float(episode["cost_usd"]))
                ),
                "cost_cap_usd": plan.cost_cap_usd,
                "config_sha256": plan.config_sha256,
                "smoke_result_sha256": plan.smoke_result_sha256,
                "failure_type": type(exc).__name__,
                "failure_code": "MODEL_CALL_OR_CHECKPOINT_EXECUTION_ABORTED",
            }
            _write_new_canonical_json(failure_path, failure)
        raise
    by_index = {
        episode["schedule_index"]: episode
        for group in grouped_results
        for episode in group
    }
    if set(by_index) != seen:
        raise RuntimeError("diagnostic checkpoints do not cover the exact schedule")
    return tuple(by_index[row["schedule_index"]] for row in rows)


def run_diagnostic(
    plan: DiagnosticPlan,
    *,
    output_dir: Path,
    resume: bool = False,
    max_workers: int = 3,
) -> Mapping[str, Any]:
    """Run the complete frozen cheap diagnostic and write its collection JSON."""

    episodes = _execute_diagnostic_schedule(
        plan,
        plan.schedule,
        output_dir=output_dir,
        resume=resume,
        max_workers=max_workers,
    )
    if len(episodes) != len(plan.schedule):
        raise RuntimeError("diagnostic run did not complete every scheduled episode")
    paid_calls = sum(episode["paid_calls"] for episode in episodes)
    total_cost = math.fsum(float(episode["cost_usd"]) for episode in episodes)
    if paid_calls > plan.config["max_paid_calls"] or total_cost > plan.cost_cap_usd:
        raise RuntimeError("diagnostic result exceeds its frozen call or cost cap")
    attestation_path = Path(output_dir) / TRANSPORT_REPAIR_ATTESTATION_NAME
    attestation_sha256 = (
        _validate_transport_repair_attestation(output_dir, plan)
        if attestation_path.is_file()
        else None
    )
    valid = {"VALID_TERMINAL", "VALID_TERMINAL_AFTER_REPAIR"}
    result = {
        "schema_version": 1,
        "study_id": "SKIM-P1",
        "run_id": plan.config["run_id"],
        "status": RUN_STATUS + "_COMPLETE",
        "data_basis": "external_model_responses",
        "eligible_for_empirical_decision": False,
        "seed": plan.seed,
        "scheduled_requests": len(plan.schedule),
        "completed_episodes": len(episodes),
        "valid_terminal_episodes": sum(
            episode["status"] in valid for episode in episodes
        ),
        "parked_episodes": sum(
            episode["status"] not in valid for episode in episodes
        ),
        "paid_calls": paid_calls,
        "total_cost_usd": total_cost,
        "cost_cap_usd": plan.cost_cap_usd,
        "preflight_cost_upper_bound_usd": plan.preflight_cost_upper_bound_usd,
        "config_sha256": plan.config_sha256,
        "smoke_result_sha256": plan.smoke_result_sha256,
        "artifact_sha256": dict(plan.artifact_sha256),
        "blockers": list(plan.config["blockers"]),
        "resume_provenance": (
            {
                "transport_repair_attestation_sha256": attestation_sha256,
                "checkpoint_prefix_rows": 324,
                "parked_prefix_rows": 3,
            }
            if attestation_sha256 is not None
            else None
        ),
        "episodes": list(episodes),
    }
    _write_new_canonical_json(
        Path(output_dir) / "diagnostic-result.json", result
    )
    return result


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute-paid-live", action="store_true")
    parser.add_argument("--config", type=Path)
    parser.add_argument("--smoke-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--max-workers", type=int, default=3)
    return parser


class _StaticIdentityClient:
    def __init__(self, row: Mapping[str, Any], config: Mapping[str, Any]) -> None:
        self.model_id = row["model_id"]
        self.family = row["family"]
        self.vendor = row["vendor"]
        self.provider = row["provider"]
        self.max_tokens = config["max_tokens"]
        self.cost_cap_usd = config["cost_cap_usd"]

    def generate(self, request, *, seed):
        raise RuntimeError("static diagnostic identity must never generate")


def cli(
    argv=None,
    *,
    environ: Optional[Mapping[str, str]] = None,
    client_factory: Optional[Any] = None,
    catalog_verifier: Optional[Any] = None,
    diagnostic_runner: Optional[Any] = None,
) -> int:
    parser = _parser()
    args = parser.parse_args(argv)
    if not args.execute_paid_live:
        parser.error("--execute-paid-live is required before key, catalog, or model access")
    environment = os.environ if environ is None else environ
    api_key = environment.get("OPENROUTER_API_KEY")
    if not isinstance(api_key, str) or not api_key:
        parser.error("OPENROUTER_API_KEY is required for paid diagnostic execution")
    if args.smoke_dir.resolve() == args.output_dir.resolve():
        parser.error("--smoke-dir and --output-dir must be distinct")
    if args.resume:
        if not args.output_dir.is_dir():
            parser.error("--resume requires an existing diagnostic output directory")
    elif args.output_dir.exists():
        parser.error("fresh diagnostic output directory must be absent")

    config, _digest = load_frozen_diagnostic_config(args.config)
    static_clients = tuple(
        _StaticIdentityClient(row, config) for row in config["model_roster"]
    )
    # Revalidate the bank, smoke proof, conditional schedules, exact 2,400-row
    # schedule, and cost bound before the first catalog network request.
    static_plan = preflight_diagnostic(
        clients=static_clients,
        smoke_dir=args.smoke_dir,
        config_path=args.config,
    )
    if args.resume:
        # The immutable prefix is authenticated before the first catalog
        # request, then authenticated again immediately before model workers.
        _validate_transport_repair_attestation(args.output_dir, static_plan)

    verifier = verify_live_catalog if catalog_verifier is None else catalog_verifier
    if not callable(verifier):
        parser.error("catalog verifier must be callable")
    catalog = verifier(config, api_key=api_key)
    expected_catalog = {
        "verified": True,
        "model_ids": [row["model_id"] for row in config["model_roster"]],
        "providers": [row["provider"] for row in config["model_roster"]],
    }
    if catalog != expected_catalog:
        parser.error("exact healthy OpenRouter endpoint catalog proof is required")

    factory = model_adapters.OpenRouterClient if client_factory is None else client_factory
    if not callable(factory):
        parser.error("diagnostic client factory must be callable")
    clients = tuple(
        factory(
            row["model_id"],
            family=row["family"],
            vendor=row["vendor"],
            provider=row["provider"],
            api_key=api_key,
            max_tokens=config["max_tokens"],
            cost_cap_usd=config["cost_cap_usd"],
        )
        for row in config["model_roster"]
    )
    plan = preflight_diagnostic(
        clients=clients,
        smoke_dir=args.smoke_dir,
        config_path=args.config,
    )
    runner = run_diagnostic if diagnostic_runner is None else diagnostic_runner
    if not callable(runner):
        parser.error("diagnostic runner must be callable")
    result = runner(
        plan,
        output_dir=args.output_dir,
        resume=args.resume,
        max_workers=args.max_workers,
    )
    print(
        json.dumps(
            {
                "status": result["status"],
                "eligible_for_empirical_decision": result[
                    "eligible_for_empirical_decision"
                ],
                "scheduled_requests": result["scheduled_requests"],
                "paid_calls": result["paid_calls"],
                "total_cost_usd": result["total_cost_usd"],
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(cli())


__all__ = [
    "DiagnosticPlan",
    "load_frozen_diagnostic_config",
    "preflight_diagnostic",
]
