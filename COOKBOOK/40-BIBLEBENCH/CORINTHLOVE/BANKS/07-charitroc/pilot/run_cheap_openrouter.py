#!/usr/bin/env python3
"""Crash-safe, public-only qualification runner for the cheap OpenRouter panel.

This runner is intentionally separate from ``run_panel.py``.  It can prove
cheap-profile access and run the twelve public CHARITROC episodes, but it has
no command or code path that can calibrate, freeze, or expose a private split.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from datetime import datetime, timedelta, timezone
from decimal import Decimal, InvalidOperation
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
import urllib.error
import urllib.parse
import urllib.request

if __package__ in {None, ""}:
    _BANK_ROOT = Path(__file__).resolve().parents[1]
    if os.fspath(_BANK_ROOT) not in sys.path:
        sys.path.insert(0, os.fspath(_BANK_ROOT))

import yaml

from analysis import roc
from pilot import contracts, manifest, openrouter_driver
from scorers import action_scale, stage3_update


RUNNER_VERSION = "charitroc-cheap-openrouter-qualification-v1"
METADATA_VERSION = "charitroc-cheap-openrouter-root-v2"
CATALOG_VERSION = "charitroc-cheap-openrouter-catalog-preflight-v1"
ACCESS_VERSION = "charitroc-cheap-openrouter-access-v1"
ACCESS_JOURNAL_VERSION = "charitroc-cheap-openrouter-access-journal-v1"
EPISODE_JOURNAL_VERSION = "charitroc-cheap-openrouter-episode-journal-v1"
STAGE_JOURNAL_VERSION = "charitroc-cheap-openrouter-stage-journal-v1"
EPISODE_ARTIFACT_VERSION = "charitroc-cheap-openrouter-episode-v1"
STAGE_ARTIFACT_VERSION = "charitroc-cheap-openrouter-stage-v1"
CANARY_VERSION = "charitroc-cheap-openrouter-canary-v1"
SMOKE_VERSION = "charitroc-cheap-openrouter-smoke-v1"
REPORT_VERSION = "charitroc-cheap-openrouter-report-v1"

COMMANDS = ("access", "canary", "smoke", "verify", "report")
RUN_MODES = ("mock", "live")
VERIFY_SCOPES = ("access", "canary", "smoke", "all")
CHEAP_PROFILE_ID = manifest.CHEAP_PROFILE_ID
ACCESS_PROVENANCE = "model access probe, NOT a measurement"
MOCK_PROVENANCE = "harness validation, NOT a measurement"
QUALIFICATION_PROVENANCE = "live OpenRouter qualification measurement"
QUALIFICATION_CLASS = "cheap OpenRouter qualification measurement"
EXPECTED_PROVIDER = "Azure"
MAX_ATTEMPTS = 3
MAX_CATALOG_BYTES = 4 * 1024 * 1024
CATALOG_BASE_URL = "https://openrouter.ai/api/v1/models"
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
RFC3339_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
SECRET_VALUE_RE = re.compile(
    r"(?i)(?:bearer\s+[a-z0-9._~+/=-]{12,}|sk-(?:or-)?[a-z0-9_-]{12,})"
)
SECRET_KEYS = {"api_key", "apikey", "authorization", "password", "secret"}
SCORING_CONTRACT_RELATIVE_PATHS = (
    "analysis/roc.py",
    "scorers/action_scale.py",
    "scorers/stage3_update.py",
)


class _AccessStageComplete(RuntimeError):
    pass


class _AccessStageFailed(RuntimeError):
    pass


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _canonical_bytes(value):
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")


def _sha(value):
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _file_sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _without_hash(value, key):
    return {name: item for name, item in value.items() if name != key}


def _read_json(path):
    with Path(path).open(encoding="utf-8") as handle:
        return json.load(handle, object_pairs_hook=_unique_object)


def _read_jsonl(path):
    target = Path(path)
    if not target.exists():
        return []
    rows = []
    with target.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.endswith("\n"):
                raise ValueError(
                    f"append-only journal line {line_number} is truncated"
                )
            try:
                rows.append(json.loads(
                    line, object_pairs_hook=_unique_object
                ))
            except (json.JSONDecodeError, ValueError):
                raise ValueError(
                    f"append-only journal line {line_number} is corrupt"
                ) from None
    return rows


def _assert_no_credentials(value):
    if type(value) is dict:
        for key, item in value.items():
            normalized = str(key).strip().lower().replace("-", "_")
            if normalized in SECRET_KEYS:
                raise ValueError("credential material cannot be persisted")
            _assert_no_credentials(item)
    elif type(value) is list:
        for item in value:
            _assert_no_credentials(item)
    elif type(value) is str and SECRET_VALUE_RE.search(value):
        raise ValueError("credential material cannot be persisted")


def _fsync_parent(path):
    descriptor = os.open(os.fspath(Path(path).parent), os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _write_new_json(path, value):
    _assert_no_credentials(value)
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    existed = target.exists()
    if existed:
        raise ValueError(f"refusing to replace immutable artifact: {target}")
    with target.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(_canonical_bytes(value).decode("utf-8") + "\n")
        handle.flush()
        os.fsync(handle.fileno())
    _fsync_parent(target)
    return target


def _write_or_validate(path, value):
    target = Path(path)
    if target.exists():
        if not target.is_file() or _read_json(target) != value:
            raise ValueError(f"immutable artifact differs: {target}")
        return target
    return _write_new_json(target, value)


def _append_jsonl(path, value):
    _assert_no_credentials(value)
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    existed = target.exists()
    with target.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(_canonical_bytes(value).decode("utf-8") + "\n")
        handle.flush()
        os.fsync(handle.fileno())
    if not existed:
        _fsync_parent(target)
    return target


def _parse_timestamp(value):
    if type(value) is not str or RFC3339_RE.fullmatch(value) is None:
        raise ValueError("timestamp must be RFC3339 UTC at whole-second precision")
    try:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=timezone.utc
        )
    except ValueError:
        raise ValueError("timestamp must be valid RFC3339 UTC") from None


def _utc_now():
    return datetime.now(timezone.utc).replace(microsecond=0).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )


def _reject_symlinks(path):
    candidate = Path(path).expanduser().absolute()
    for part in (candidate, *candidate.parents):
        if part.is_symlink():
            raise ValueError(f"path may not contain a symlink: {part}")


def _catalog_url(provider_model_id):
    if type(provider_model_id) is not str or provider_model_id.count("/") != 1:
        raise ValueError("provider model id must be author/slug")
    author, slug = provider_model_id.split("/", 1)
    if not author or not slug:
        raise ValueError("provider model id must be author/slug")
    return (
        CATALOG_BASE_URL + "/" + urllib.parse.quote(author, safe="") + "/"
        + urllib.parse.quote(slug, safe="") + "/endpoints"
    )


def _live_catalog_loader(provider_model_id):
    request = urllib.request.Request(
        _catalog_url(provider_model_id),
        headers={
            "Accept": "application/json",
            "User-Agent": "CHARITROC-cheap-qualification/1",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            status = getattr(response, "status", None)
            payload = response.read(MAX_CATALOG_BYTES + 1)
    except (urllib.error.URLError, OSError) as exc:
        raise ValueError("OpenRouter endpoint catalog request failed") from exc
    if status != 200 or len(payload) > MAX_CATALOG_BYTES:
        raise ValueError("OpenRouter endpoint catalog response is invalid")
    try:
        return json.loads(
            payload.decode("utf-8", errors="strict"),
            object_pairs_hook=_unique_object,
        )
    except (UnicodeError, json.JSONDecodeError, ValueError):
        raise ValueError("OpenRouter endpoint catalog is not strict JSON") from None


def _decimal(value, field):
    if isinstance(value, bool) or type(value) not in {str, int, float}:
        raise ValueError(f"catalog endpoint {field} price is invalid")
    try:
        number = Decimal(str(value))
    except InvalidOperation:
        raise ValueError(f"catalog endpoint {field} price is invalid") from None
    if not number.is_finite() or number < 0:
        raise ValueError(f"catalog endpoint {field} price is invalid")
    return number


def _endpoint_price_per_million(endpoint, field):
    pricing = endpoint.get("pricing")
    if type(pricing) is not dict:
        raise ValueError("catalog endpoint pricing is missing")
    aliases = ("prompt", "input") if field == "input" else (
        "completion", "output"
    )
    observed = [pricing[name] for name in aliases if name in pricing]
    if len(observed) != 1:
        raise ValueError(f"catalog endpoint {field} price is ambiguous")
    return _decimal(observed[0], field) * Decimal(1_000_000)


def _normalize_decimal(value):
    normalized = value.normalize()
    text = format(normalized, "f")
    return "0" if text in {"-0", ""} else text


def _validate_catalog_model(payload, identity):
    if type(payload) is not dict or type(payload.get("data")) is not dict:
        raise ValueError("catalog model response must contain one data object")
    data = payload["data"]
    if data.get("id") != identity["provider_model_id"]:
        raise ValueError("catalog model id differs from the frozen identity")
    endpoints = data.get("endpoints")
    if type(endpoints) is not list or not endpoints:
        raise ValueError("catalog model has no endpoint records")

    required = set(identity["required_parameters"])
    minimum_context = identity["minimum_context_length"]
    ceilings = identity["price_ceiling_usd_per_million_tokens"]
    eligible = []
    for index, endpoint in enumerate(endpoints):
        if type(endpoint) is not dict or endpoint.get("provider_name") != (
                identity["expected_returned_provider"]):
            continue
        context = endpoint.get("context_length")
        parameters = endpoint.get("supported_parameters")
        if (
            type(context) is not int
            or isinstance(context, bool)
            or context < minimum_context
            or type(parameters) is not list
            or any(type(item) is not str for item in parameters)
            or len(parameters) != len(set(parameters))
            or not required.issubset(parameters)
        ):
            continue
        try:
            input_price = _endpoint_price_per_million(endpoint, "input")
            output_price = _endpoint_price_per_million(endpoint, "output")
        except ValueError:
            continue
        if (
            input_price > Decimal(str(ceilings["input"]))
            or output_price > Decimal(str(ceilings["output"]))
        ):
            continue
        eligible.append({
            "catalog_endpoint_index": index,
            "provider_name": EXPECTED_PROVIDER,
            "context_length": context,
            "required_parameters_present": sorted(required),
            "input_usd_per_million_tokens": _normalize_decimal(input_price),
            "output_usd_per_million_tokens": _normalize_decimal(output_price),
        })
    if not eligible:
        raise ValueError(
            "catalog has no individually eligible exact Azure endpoint"
        )
    return {
        "logical_model_id": identity["logical_model_id"],
        "provider_model_id": identity["provider_model_id"],
        "configuration_id": identity["configuration_id"],
        "catalog_url": _catalog_url(identity["provider_model_id"]),
        "catalog_payload_sha256": _sha(payload),
        "eligible_azure_endpoint_count": len(eligible),
        "eligible_azure_endpoints": eligible,
    }


class CheapOpenRouterQualificationRunner:
    """One profile-bound, resumable public qualification root."""

    def __init__(
            self, *, bank_root, out_dir, run_mode, driver=None,
            catalog_loader=None, clock=None):
        if run_mode not in RUN_MODES:
            raise ValueError(f"run_mode must be explicit: {RUN_MODES}")
        supplied = (driver, catalog_loader, clock)
        if run_mode == "live" and any(value is not None for value in supplied):
            raise ValueError("live qualification rejects injected dependencies")
        if run_mode == "mock":
            if driver is None or not callable(getattr(driver, "run_episode", None)):
                raise ValueError("mock qualification requires an explicit driver")
            if catalog_loader is None or not callable(catalog_loader):
                raise ValueError(
                    "mock qualification requires an explicit catalog loader"
                )

        root = Path(bank_root).expanduser().resolve()
        if not root.is_dir():
            raise ValueError("bank_root must be an existing directory")
        lexical_out = Path(out_dir).expanduser().absolute()
        _reject_symlinks(lexical_out)
        lexical_out.mkdir(parents=True, exist_ok=True)
        _reject_symlinks(lexical_out)

        self.bank_root = root
        self.out_dir = lexical_out.resolve()
        self.run_mode = run_mode
        self.provenance = (
            MOCK_PROVENANCE if run_mode == "mock" else QUALIFICATION_PROVENANCE
        )
        self._driver = driver
        self._catalog_loader = (
            catalog_loader if run_mode == "mock" else _live_catalog_loader
        )
        self._clock = clock or _utc_now
        self._last_timestamp = None
        self.panel = manifest.load_cheap_panel()
        self.models = tuple(
            row["logical_model_id"] for row in self.panel["models"]
        )
        if tuple(self.panel["command_allowlist"]) != COMMANDS:
            raise ValueError("cheap profile command allowlist differs")
        self.identities = {
            model: manifest.resolve_openrouter_identity(
                model, profile_id=CHEAP_PROFILE_ID
            ) for model in self.models
        }
        self.public_episodes, self._sidecar = self._load_public_bank()
        self._by_id = {row["id"]: row for row in self.public_episodes}
        self.canary_item_ids = self._select_canary_items()
        self._initialize_metadata()
        self._initialize_timestamp_floor()

    def _path(self, *parts):
        candidate = self.out_dir.joinpath(*parts)
        _reject_symlinks(candidate)
        resolved_parent = candidate.parent.resolve()
        try:
            resolved_parent.relative_to(self.out_dir)
        except ValueError:
            raise ValueError("artifact path escapes the qualification root") from None
        return candidate

    def _artifact_files(self, *parts, suffixes=(".json",)):
        root = self._path(*parts)
        if not root.exists():
            return set()
        if root.is_symlink() or not root.is_dir():
            raise ValueError("qualification artifact root is not a real directory")
        files = set()
        for path in root.rglob("*"):
            if path.is_symlink():
                raise ValueError("qualification artifact tree contains a symlink")
            if path.is_dir():
                continue
            if not path.is_file() or path.suffix not in suffixes:
                raise ValueError(
                    "qualification artifact tree contains an unexpected file"
                )
            try:
                path.resolve().relative_to(self.out_dir)
            except ValueError:
                raise ValueError(
                    "qualification artifact escaped the qualification root"
                ) from None
            files.add(path)
        return files

    def _load_public_bank(self):
        with (self.bank_root / "seeds_public.yaml").open(
                encoding="utf-8") as handle:
            episodes = yaml.safe_load(handle)
        sidecar = _read_json(self.bank_root / "sidecar/ground_truth.json")
        if (
            type(episodes) is not list
            or len(episodes) != 12
            or any(type(row) is not dict or row.get("split") != "public"
                   for row in episodes)
        ):
            raise ValueError("qualification requires the exact 12-item public bank")
        ids = [row.get("id") for row in episodes]
        if any(type(item) is not str for item in ids) or len(ids) != len(set(ids)):
            raise ValueError("public episode identities are invalid")
        if type(sidecar) is not dict or not set(ids).issubset(sidecar):
            raise ValueError("public scoring sidecar coverage is incomplete")
        for item_id in ids:
            hidden = sidecar[item_id]
            if (
                type(hidden) is not dict
                or hidden.get("true_type") not in {"benign", "malicious"}
                or hidden.get("cue_variant") not in {
                    "strong", "weak", "absent", "adversarial",
                }
                or type(hidden.get("expected_stage3")) is not dict
            ):
                raise ValueError("public scoring sidecar fields are invalid")
        return deepcopy(sorted(episodes, key=lambda row: row["id"])), sidecar

    def _select_canary_items(self):
        selected = []
        for cue in ("strong", "weak", "absent", "adversarial"):
            candidates = sorted(
                row["id"] for row in self.public_episodes
                if self._sidecar[row["id"]]["cue_variant"] == cue
            )
            if not candidates:
                raise ValueError(f"public bank lacks a {cue} cue canary")
            selected.append(candidates[0])
        if len(selected) != len(set(selected)):
            raise ValueError("cue canary items are not distinct")
        return tuple(selected)

    def _public_scoring_projection(self, sidecar):
        if type(sidecar) is not dict:
            raise ValueError("public scoring sidecar is invalid")
        projection = []
        for item_id in sorted(self._by_id):
            hidden = sidecar.get(item_id)
            if (
                type(hidden) is not dict
                or hidden.get("true_type") not in {"benign", "malicious"}
                or hidden.get("cue_variant") not in {
                    "strong", "weak", "absent", "adversarial",
                }
                or type(hidden.get("expected_stage3")) is not dict
            ):
                raise ValueError("public scoring projection is invalid")
            projection.append({
                "item_id": item_id,
                "true_type": hidden["true_type"],
                "cue_variant": hidden["cue_variant"],
                "expected_stage3": deepcopy(hidden["expected_stage3"]),
            })
        return projection

    def _disk_public_scoring_projection(self):
        path = self.bank_root / "sidecar/ground_truth.json"
        _reject_symlinks(path)
        if not path.is_file():
            raise ValueError("public scoring sidecar is missing")
        return self._public_scoring_projection(_read_json(path))

    def _scoring_contract_source_sha256s(self):
        hashes = {}
        for relative_path in SCORING_CONTRACT_RELATIVE_PATHS:
            path = self.bank_root / relative_path
            _reject_symlinks(path)
            try:
                path.resolve().relative_to(self.bank_root)
            except ValueError:
                raise ValueError(
                    "scoring contract source escapes the bank root"
                ) from None
            if not path.is_file():
                raise ValueError("scoring contract source is missing")
            hashes[relative_path] = _file_sha(path)
        return hashes

    def _metadata_payload(self, created_at):
        scoring_projection = self._disk_public_scoring_projection()
        scoring_sources = self._scoring_contract_source_sha256s()
        body = {
            "metadata_version": METADATA_VERSION,
            "runner_version": RUNNER_VERSION,
            "purpose": "qualification-only",
            "provider": "openrouter",
            "run_mode": self.run_mode,
            "provenance": self.provenance,
            "profile_id": CHEAP_PROFILE_ID,
            "profile_sha256": manifest.cheap_panel_sha256(),
            "logical_model_ids": list(self.models),
            "provider_model_ids": [
                self.identities[model]["provider_model_id"]
                for model in self.models
            ],
            "public_episode_count": len(self.public_episodes),
            "public_bank_sha256": _sha(self.public_episodes),
            "public_scoring_projection_sha256": _sha(scoring_projection),
            "scoring_contract_source_sha256s": scoring_sources,
            "scoring_contract_sha256": _sha(scoring_sources),
            "canary_public_item_ids": list(self.canary_item_ids),
            "response_schema_sha256": _sha(manifest.load_response_schema()),
            "created_at_utc": created_at,
            "forbidden_capabilities": [
                "calibration", "reliability", "freeze", "private",
            ],
        }
        body["metadata_sha256"] = _sha(body)
        return body

    def _validate_metadata(self, metadata):
        if type(metadata) is not dict or metadata.get(
                "metadata_sha256") != _sha(_without_hash(
                    metadata, "metadata_sha256")):
            raise ValueError("qualification root metadata hash differs")
        _parse_timestamp(metadata.get("created_at_utc"))
        expected = self._metadata_payload(metadata["created_at_utc"])
        if metadata != expected:
            raise ValueError("qualification root profile/identity metadata differs")
        _assert_no_credentials(metadata)
        return metadata

    def _initialize_metadata(self):
        path = self._path("run_metadata.json")
        if path.exists():
            self.metadata = self._validate_metadata(_read_json(path))
        else:
            created = self._clock()
            _parse_timestamp(created)
            self.metadata = self._metadata_payload(created)
            _write_new_json(path, self.metadata)

    def _initialize_timestamp_floor(self):
        latest = _parse_timestamp(self.metadata["created_at_utc"])
        episode_events = self._episode_events()
        known_events = (
            self._access_events()
            + episode_events
            + self._stage_evidence_events(episode_events)
        )
        for event in known_events:
            latest = max(latest, _parse_timestamp(event["timestamp_utc"]))
        self._last_timestamp = latest

    def _now(self):
        candidate = _parse_timestamp(self._clock())
        if candidate <= self._last_timestamp:
            candidate = self._last_timestamp + timedelta(seconds=1)
        self._last_timestamp = candidate
        return candidate.strftime("%Y-%m-%dT%H:%M:%SZ")

    def _validate_root(self):
        metadata = self._validate_metadata(
            _read_json(self._path("run_metadata.json"))
        )
        if manifest.cheap_panel_sha256() != self.metadata["profile_sha256"]:
            raise ValueError("qualification profile hash drifted")
        disk_projection = self._disk_public_scoring_projection()
        memory_projection = self._public_scoring_projection(self._sidecar)
        scoring_sources = self._scoring_contract_source_sha256s()
        if (
            _canonical_bytes(memory_projection)
            != _canonical_bytes(disk_projection)
            or metadata.get("public_scoring_projection_sha256")
            != _sha(disk_projection)
            or metadata.get("scoring_contract_source_sha256s")
            != scoring_sources
            or metadata.get("scoring_contract_sha256")
            != _sha(scoring_sources)
        ):
            raise ValueError("qualification scoring contract drifted")

    def preflight_catalog(self):
        self._validate_root()
        models = []
        for model in self.models:
            identity = self.identities[model]
            payload = self._catalog_loader(identity["provider_model_id"])
            models.append(_validate_catalog_model(payload, identity))
        report = {
            "catalog_preflight_version": CATALOG_VERSION,
            "purpose": "qualification-only",
            "profile_id": CHEAP_PROFILE_ID,
            "profile_sha256": manifest.cheap_panel_sha256(),
            "catalog_snapshot_utc": self.panel["catalog_snapshot_utc"],
            "required_parameters": deepcopy(self.panel["required_parameters"]),
            "minimum_context_length": self.panel["minimum_context_length"],
            "expected_returned_provider": EXPECTED_PROVIDER,
            "models": models,
        }
        report["catalog_preflight_sha256"] = _sha(report)
        _write_or_validate(self._path("catalog", "preflight.json"), report)
        return report

    def _validate_catalog_artifact(self):
        path = self._path("catalog", "preflight.json")
        if not path.is_file():
            raise ValueError("endpoint catalog preflight is missing")
        report = _read_json(path)
        if (
            type(report) is not dict
            or report.get("catalog_preflight_version") != CATALOG_VERSION
            or report.get("purpose") != "qualification-only"
            or report.get("profile_id") != CHEAP_PROFILE_ID
            or report.get("profile_sha256") != manifest.cheap_panel_sha256()
            or report.get("catalog_snapshot_utc")
            != self.panel["catalog_snapshot_utc"]
            or report.get("required_parameters")
            != self.panel["required_parameters"]
            or report.get("minimum_context_length")
            != self.panel["minimum_context_length"]
            or report.get("expected_returned_provider") != EXPECTED_PROVIDER
            or report.get("catalog_preflight_sha256") != _sha(
                _without_hash(report, "catalog_preflight_sha256")
            )
        ):
            raise ValueError("endpoint catalog preflight binding differs")
        rows = report.get("models")
        if type(rows) is not list or [row.get("logical_model_id")
                                      for row in rows] != list(self.models):
            raise ValueError("endpoint catalog model coverage differs")
        for row, model in zip(rows, self.models):
            identity = self.identities[model]
            endpoints = row.get("eligible_azure_endpoints", [])
            if (
                type(row) is not dict
                or row.get("logical_model_id") != model
                or row.get("provider_model_id") != identity["provider_model_id"]
                or row.get("configuration_id") != identity["configuration_id"]
                or row.get("catalog_url") != _catalog_url(
                    identity["provider_model_id"])
                or not SHA256_RE.fullmatch(
                    row.get("catalog_payload_sha256", ""))
                or type(row.get("eligible_azure_endpoint_count")) is not int
                or row["eligible_azure_endpoint_count"] < 1
                or type(endpoints) is not list
                or row["eligible_azure_endpoint_count"] != len(endpoints)
            ):
                raise ValueError("eligible endpoint catalog binding differs")
            endpoint_indexes = set()
            for endpoint in endpoints:
                if type(endpoint) is not dict:
                    raise ValueError("eligible catalog endpoint is invalid")
                index = endpoint.get("catalog_endpoint_index")
                context = endpoint.get("context_length")
                if (
                    type(index) is not int
                    or index < 0
                    or index in endpoint_indexes
                    or endpoint.get("provider_name")
                    != identity["expected_returned_provider"]
                    or type(context) is not int
                    or context < identity["minimum_context_length"]
                    or endpoint.get("required_parameters_present")
                    != sorted(identity["required_parameters"])
                ):
                    raise ValueError(
                        "eligible catalog endpoint context/parameters differ"
                    )
                endpoint_indexes.add(index)
                for field in ("input", "output"):
                    price = _decimal(
                        endpoint.get(f"{field}_usd_per_million_tokens"),
                        field,
                    )
                    ceiling = Decimal(str(
                        identity["price_ceiling_usd_per_million_tokens"][field]
                    ))
                    if price > ceiling:
                        raise ValueError(
                            f"eligible catalog endpoint {field} price differs"
                        )
        return report

    def _call_driver(self, episode, model, *, before_stage, stage_sink):
        if self.run_mode == "mock":
            return self._driver.run_episode(
                episode,
                logical_model_id=model,
                panel_profile=CHEAP_PROFILE_ID,
                before_stage=before_stage,
                stage_sink=stage_sink,
            )
        api_key = os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY is required out of band")
        return openrouter_driver.run_live_episode(
            episode,
            logical_model_id=model,
            api_key=api_key,
            panel_profile=CHEAP_PROFILE_ID,
            before_stage=before_stage,
            stage_sink=stage_sink,
        )

    def _validate_hook_identity(self, event, model, *, stage=None):
        if type(event) is not dict or event.get("provider") != "openrouter":
            raise ValueError("provider hook event is invalid")
        request = contracts.validate_stage_request(event.get("request"))
        identity = self.identities[model]
        expected = (
            "openrouter", model, identity["provider_model_id"],
            identity["configuration_id"],
        )
        observed = tuple(request[key] for key in (
            "provider", "logical_model_id", "provider_model_id",
            "configuration_id",
        ))
        if observed != expected or (stage is not None and request["stage"] != stage):
            raise ValueError("provider hook identity differs from cheap profile")
        descriptor = event.get("transport_descriptor")
        if type(descriptor) is not dict:
            raise ValueError("provider transport descriptor is invalid")
        _assert_no_credentials(event)
        return request, descriptor

    def _validate_stage_event(self, event, model, *, stage=None):
        request, descriptor = self._validate_hook_identity(
            event, model, stage=stage
        )
        result = contracts.validate_stage_result(event.get("result"), request)
        if result["transport_request_sha256"] != _sha(descriptor):
            raise ValueError("transport descriptor/result hash differs")
        return request, result, descriptor

    # ------------------------------ access ------------------------------
    def _access_journal_path(self):
        return self._path("access", "attempt-journal.jsonl")

    def _access_events(self):
        events = _read_jsonl(self._access_journal_path())
        latest = {}
        previous_hash = None
        previous_time = None
        for index, event in enumerate(events, 1):
            model = event.get("logical_model_id") if type(event) is dict else None
            if (
                type(event) is not dict
                or event.get("journal_version") != ACCESS_JOURNAL_VERSION
                or event.get("event_index") != index
                or event.get("profile_id") != CHEAP_PROFILE_ID
                or event.get("profile_sha256") != manifest.cheap_panel_sha256()
                or model not in self.models
                or event.get("configuration_id") != self.identities[model][
                    "configuration_id"]
                or type(event.get("attempt_number")) is not int
                or not 1 <= event["attempt_number"] <= MAX_ATTEMPTS
                or event.get("state") not in {
                    "started", "abandoned", "succeeded", "failed",
                }
                or event.get("previous_event_sha256") != previous_hash
                or event.get("event_sha256") != _sha(
                    _without_hash(event, "event_sha256"))
            ):
                raise ValueError("access attempt journal binding differs")
            timestamp = _parse_timestamp(event.get("timestamp_utc"))
            if previous_time is not None and timestamp <= previous_time:
                raise ValueError("access attempt journal time is not monotonic")
            previous_time = timestamp
            prior = latest.get(model)
            if event["state"] == "started":
                if (
                    event.get("start_event_sha256") is not None
                    or event.get("artifact_relative_path") is not None
                    or event.get("artifact_sha256") is not None
                    or event.get("terminal_kind") is not None
                    or event["attempt_number"] != 1 + sum(
                        row.get("logical_model_id") == model
                        and row.get("state") == "started"
                        for row in events[:index - 1]
                    )
                    or (prior is not None and prior["state"] not in {
                        "abandoned", "failed",
                    })
                ):
                    raise ValueError("access start transition differs")
                if not SHA256_RE.fullmatch(event.get("request_sha256", "")):
                    raise ValueError("access request hash differs")
                if not SHA256_RE.fullmatch(
                        event.get("transport_descriptor_sha256", "")):
                    raise ValueError("access descriptor hash differs")
            else:
                if (
                    prior is None
                    or prior["state"] != "started"
                    or prior["attempt_number"] != event["attempt_number"]
                    or event.get("start_event_sha256") != prior["event_sha256"]
                    or event.get("request_sha256") != prior["request_sha256"]
                    or event.get("transport_descriptor_sha256") != prior[
                        "transport_descriptor_sha256"]
                ):
                    raise ValueError("access terminal transition differs")
                if event["state"] == "abandoned":
                    if (
                        event.get("artifact_relative_path") is not None
                        or event.get("artifact_sha256") is not None
                        or event.get("terminal_kind") != "pre_sink_interruption"
                    ):
                        raise ValueError("access abandonment differs")
                elif (
                    type(event.get("artifact_relative_path")) is not str
                    or not SHA256_RE.fullmatch(event.get("artifact_sha256", ""))
                    or event.get("terminal_kind") not in {
                        "validated_probe", "provider_terminal_failure",
                        "integrity_rejection", "access_readiness_rejection",
                    }
                ):
                    raise ValueError("access terminal artifact binding differs")
            latest[model] = event
            previous_hash = event["event_sha256"]
        _assert_no_credentials(events)
        return events

    def _append_access_event(
            self, *, model, attempt, state, request_sha, descriptor_sha,
            start=None, artifact=None, terminal_kind=None):
        events = self._access_events()
        relative = None
        artifact_sha = None
        if artifact is not None:
            relative = Path(artifact).resolve().relative_to(self.out_dir).as_posix()
            artifact_sha = _file_sha(artifact)
        event = {
            "journal_version": ACCESS_JOURNAL_VERSION,
            "event_index": len(events) + 1,
            "profile_id": CHEAP_PROFILE_ID,
            "profile_sha256": manifest.cheap_panel_sha256(),
            "logical_model_id": model,
            "configuration_id": self.identities[model]["configuration_id"],
            "attempt_number": attempt,
            "state": state,
            "request_sha256": request_sha,
            "transport_descriptor_sha256": descriptor_sha,
            "start_event_sha256": start["event_sha256"] if start else None,
            "artifact_relative_path": relative,
            "artifact_sha256": artifact_sha,
            "terminal_kind": terminal_kind,
            "previous_event_sha256": (
                events[-1]["event_sha256"] if events else None
            ),
            "timestamp_utc": self._now(),
        }
        event["event_sha256"] = _sha(event)
        _append_jsonl(self._access_journal_path(), event)
        self._access_events()
        return event

    def _access_model_events(self, events, model):
        return [row for row in events if row["logical_model_id"] == model]

    def _validate_access_history(self, events):
        for event in events:
            if event["state"] not in {"succeeded", "failed"}:
                continue
            model = event["logical_model_id"]
            path = (
                self._access_success_path(model)
                if event["state"] == "succeeded"
                else self._access_failure_path(model, event["attempt_number"])
            )
            if (
                not path.is_file()
                or event["artifact_relative_path"]
                != path.relative_to(self.out_dir).as_posix()
                or event["artifact_sha256"] != _file_sha(path)
            ):
                raise ValueError(
                    "access historical artifact is missing or differs"
                )
            artifact = self._validate_access_artifact(
                _read_json(path), model, event["attempt_number"]
            )
            expected_ready = event["state"] == "succeeded"
            expected_kind = (
                "validated_probe" if expected_ready
                else artifact["failure_kind"]
            )
            if (
                artifact["ready"] is not expected_ready
                or event["terminal_kind"] != expected_kind
            ):
                raise ValueError("access historical artifact state differs")

    def _access_probe_id(self, model):
        return f"CHEAP-ACCESS-{self.models.index(model) + 1:02d}-{model}"

    @staticmethod
    def _access_turns():
        return {
            "stage_1": (
                "Model-access compatibility probe. No benchmark case is "
                "present. Return a brief canonical JSON response using "
                "UNCERTAIN and VERIFY."
            ),
            "stage_2": "Unused access continuation two.",
            "stage_3": "Unused access continuation three.",
            "stage_4": "Unused access continuation four.",
        }

    def _access_ready(self, request, result):
        return (
            result["terminal_status"] == "complete"
            and result["returned_provider_model_id"]
            == request["provider_model_id"]
            and result["returned_provider_name"] == EXPECTED_PROVIDER
            and result["integrity"]["integrity_valid"] is True
            and result["integrity"]["mechanically_resolved"] is True
            and result["integrity"]["measurement_ready"] is (
                self.run_mode == "live"
            )
        )

    @staticmethod
    def _failure_kind(result):
        if result["terminal_status"] == "failed":
            return "provider_terminal_failure"
        if result["terminal_status"] == "invalidated":
            return "integrity_rejection"
        return "access_readiness_rejection"

    def _build_access_artifact(self, model, attempt, event):
        request, result, descriptor = self._validate_stage_event(
            event, model, stage="stage_1"
        )
        body = {
            "access_artifact_version": ACCESS_VERSION,
            "provenance": ACCESS_PROVENANCE,
            "measurement_ready": False,
            "profile_id": CHEAP_PROFILE_ID,
            "profile_sha256": manifest.cheap_panel_sha256(),
            "probe_id": self._access_probe_id(model),
            "logical_model_id": model,
            "provider_model_id": self.identities[model]["provider_model_id"],
            "configuration_id": self.identities[model]["configuration_id"],
            "expected_returned_provider": EXPECTED_PROVIDER,
            "attempt_number": attempt,
            "request": request,
            "result": result,
            "transport_descriptor": descriptor,
            "attestation": deepcopy(event.get("attestation")),
            "ready": self._access_ready(request, result),
            "failure_kind": (
                None if self._access_ready(request, result)
                else self._failure_kind(result)
            ),
        }
        body["access_artifact_sha256"] = _sha(body)
        _assert_no_credentials(body)
        return body

    def _validate_access_artifact(self, artifact, model, attempt=None):
        if (
            type(artifact) is not dict
            or artifact.get("access_artifact_version") != ACCESS_VERSION
            or artifact.get("provenance") != ACCESS_PROVENANCE
            or artifact.get("measurement_ready") is not False
            or artifact.get("profile_id") != CHEAP_PROFILE_ID
            or artifact.get("profile_sha256") != manifest.cheap_panel_sha256()
            or artifact.get("probe_id") != self._access_probe_id(model)
            or artifact.get("logical_model_id") != model
            or artifact.get("provider_model_id") != self.identities[model][
                "provider_model_id"]
            or artifact.get("configuration_id") != self.identities[model][
                "configuration_id"]
            or artifact.get("expected_returned_provider") != EXPECTED_PROVIDER
            or (attempt is not None and artifact.get("attempt_number") != attempt)
            or artifact.get("access_artifact_sha256") != _sha(
                _without_hash(artifact, "access_artifact_sha256"))
        ):
            raise ValueError("access artifact profile/hash/identity differs")
        request = contracts.validate_stage_request(artifact.get("request"))
        result = contracts.validate_stage_result(artifact.get("result"), request)
        if (
            request["stage"] != "stage_1"
            or tuple(request[key] for key in (
                "provider", "logical_model_id", "provider_model_id",
                "configuration_id",
            )) != (
                "openrouter", model,
                self.identities[model]["provider_model_id"],
                self.identities[model]["configuration_id"],
            )
            or _sha(artifact.get("transport_descriptor")) != result[
                "transport_request_sha256"]
            or artifact.get("ready") != self._access_ready(request, result)
            or artifact.get("failure_kind") != (
                None if artifact["ready"] else self._failure_kind(result)
            )
        ):
            raise ValueError("access artifact evidence differs")
        _assert_no_credentials(artifact)
        return artifact

    def _access_success_path(self, model):
        return self._path("access", "probes", f"{model}.json")

    def _access_failure_path(self, model, attempt):
        return self._path(
            "access", "failures", model, f"attempt-{attempt:02d}.json"
        )

    def _reconcile_access_orphan(self, model, events):
        rows = self._access_model_events(events, model)
        latest = rows[-1] if rows else None
        if latest is None or latest["state"] != "started":
            return events
        attempt = latest["attempt_number"]
        candidates = [path for path in (
            self._access_success_path(model),
            self._access_failure_path(model, attempt),
        ) if path.is_file()]
        if not candidates:
            return events
        if len(candidates) != 1:
            raise ValueError("ambiguous orphan access artifacts")
        path = candidates[0]
        artifact = self._validate_access_artifact(_read_json(path), model, attempt)
        state = "succeeded" if artifact["ready"] else "failed"
        self._append_access_event(
            model=model,
            attempt=attempt,
            state=state,
            request_sha=latest["request_sha256"],
            descriptor_sha=latest["transport_descriptor_sha256"],
            start=latest,
            artifact=path,
            terminal_kind=(
                "validated_probe" if state == "succeeded"
                else artifact["failure_kind"]
            ),
        )
        return self._access_events()

    def _prepare_access_attempt(self, model, *, retry_failed):
        events = self._reconcile_access_orphan(model, self._access_events())
        rows = self._access_model_events(events, model)
        latest = rows[-1] if rows else None
        starts = sum(row["state"] == "started" for row in rows)
        if latest is not None and latest["state"] == "succeeded":
            return None
        if latest is not None and latest["state"] == "failed":
            if not retry_failed:
                raise ValueError(
                    "durable access failure requires an explicit retry"
                )
            self._validate_access_history(events)
            if starts >= MAX_ATTEMPTS:
                raise ValueError("access exceeded the three-attempt ceiling")
            return starts + 1
        if latest is not None and latest["state"] == "started":
            self._validate_access_history(events)
            if starts >= MAX_ATTEMPTS:
                raise ValueError("access exceeded the three-attempt ceiling")
            self._append_access_event(
                model=model,
                attempt=latest["attempt_number"],
                state="abandoned",
                request_sha=latest["request_sha256"],
                descriptor_sha=latest["transport_descriptor_sha256"],
                start=latest,
                terminal_kind="pre_sink_interruption",
            )
            return starts + 1
        if latest is not None and latest["state"] == "abandoned":
            self._validate_access_history(events)
            if starts >= MAX_ATTEMPTS:
                raise ValueError("access exceeded the three-attempt ceiling")
            return starts + 1
        return 1

    def _run_access_model(self, model, attempt):
        episode = {
            "id": self._access_probe_id(model),
            "multiturn_script": self._access_turns(),
        }
        started = []

        def before_stage(event):
            request, descriptor = self._validate_hook_identity(
                event, model, stage="stage_1"
            )
            if started:
                raise ValueError("access driver attempted more than one stage")
            started.append(self._append_access_event(
                model=model,
                attempt=attempt,
                state="started",
                request_sha=request["request_sha256"],
                descriptor_sha=_sha(descriptor),
            ))

        def stage_sink(event):
            if len(started) != 1:
                raise ValueError("access terminal stage lacks durable start")
            artifact = self._build_access_artifact(model, attempt, event)
            if artifact["ready"]:
                path = self._access_success_path(model)
                state = "succeeded"
                terminal_kind = "validated_probe"
            else:
                path = self._access_failure_path(model, attempt)
                state = "failed"
                terminal_kind = artifact["failure_kind"]
            _write_new_json(path, artifact)
            self._append_access_event(
                model=model,
                attempt=attempt,
                state=state,
                request_sha=started[0]["request_sha256"],
                descriptor_sha=started[0]["transport_descriptor_sha256"],
                start=started[0],
                artifact=path,
                terminal_kind=terminal_kind,
            )
            if state == "succeeded":
                raise _AccessStageComplete()
            raise _AccessStageFailed()

        try:
            self._call_driver(
                episode, model,
                before_stage=before_stage,
                stage_sink=stage_sink,
            )
        except _AccessStageComplete:
            return
        except _AccessStageFailed:
            raise ValueError(
                "durable access failure recorded; explicit access retry is required"
            ) from None
        raise ValueError("access driver did not emit one terminal stage")

    def access(self, retry_failed=False):
        self._validate_root()
        report_path = self._path("access", "report.json")
        if report_path.is_file():
            return self._verify_access(return_report=True)
        self.preflight_catalog()
        for model in self.models:
            attempt = self._prepare_access_attempt(
                model, retry_failed=retry_failed
            )
            if attempt is not None:
                self._run_access_model(model, attempt)
        events = self._access_events()
        probes = []
        counts = {}
        for model in self.models:
            rows = self._access_model_events(events, model)
            if not rows or rows[-1]["state"] != "succeeded":
                raise ValueError("access journal is not terminally complete")
            counts[model] = sum(row["state"] == "started" for row in rows)
            probes.append(self._validate_access_artifact(
                _read_json(self._access_success_path(model)), model
            ))
        report = {
            "access_version": ACCESS_VERSION,
            "provenance": ACCESS_PROVENANCE,
            "measurement_ready": False,
            "purpose": "qualification-only",
            "profile_id": CHEAP_PROFILE_ID,
            "profile_sha256": manifest.cheap_panel_sha256(),
            "models": list(self.models),
            "attempt_counts": counts,
            "access_journal_sha256": _file_sha(self._access_journal_path()),
            "probes": probes,
        }
        report["access_sha256"] = _sha(report)
        _write_new_json(report_path, report)
        return self._verify_access(return_report=True)

    def _verify_access(self, *, return_report=False):
        report_path = self._path("access", "report.json")
        if not report_path.is_file():
            raise ValueError("cheap-profile access report is missing")
        report = _read_json(report_path)
        if (
            type(report) is not dict
            or report.get("access_version") != ACCESS_VERSION
            or report.get("provenance") != ACCESS_PROVENANCE
            or report.get("measurement_ready") is not False
            or report.get("purpose") != "qualification-only"
            or report.get("profile_id") != CHEAP_PROFILE_ID
            or report.get("profile_sha256") != manifest.cheap_panel_sha256()
            or report.get("models") != list(self.models)
            or report.get("access_sha256") != _sha(
                _without_hash(report, "access_sha256"))
        ):
            raise ValueError("access report profile/hash binding differs")
        events = self._access_events()
        if report.get("access_journal_sha256") != _file_sha(
                self._access_journal_path()):
            raise ValueError("access journal/report binding differs")
        expected_failure_paths = set()
        for event in events:
            if event["state"] not in {"succeeded", "failed"}:
                continue
            model = event["logical_model_id"]
            path = (
                self._access_success_path(model)
                if event["state"] == "succeeded"
                else self._access_failure_path(model, event["attempt_number"])
            )
            if event["state"] == "failed":
                expected_failure_paths.add(path)
            if (
                not path.is_file()
                or event["artifact_relative_path"]
                != path.relative_to(self.out_dir).as_posix()
                or event["artifact_sha256"] != _file_sha(path)
            ):
                raise ValueError(
                    "access journal terminal artifact is missing or differs"
                )
            artifact = self._validate_access_artifact(
                _read_json(path), model, event["attempt_number"]
            )
            expected_ready = event["state"] == "succeeded"
            expected_kind = (
                "validated_probe" if expected_ready
                else artifact["failure_kind"]
            )
            if (
                artifact["ready"] is not expected_ready
                or event["terminal_kind"] != expected_kind
            ):
                raise ValueError("access journal terminal artifact state differs")
        if self._artifact_files("access", "failures") != expected_failure_paths:
            raise ValueError("access failure artifact coverage differs")
        probes = report.get("probes")
        if type(probes) is not list or len(probes) != len(self.models):
            raise ValueError("access probe coverage differs")
        counts = {}
        expected_paths = set()
        for model, probe in zip(self.models, probes):
            rows = self._access_model_events(events, model)
            if not rows or rows[-1]["state"] != "succeeded":
                raise ValueError("access journal is not complete")
            counts[model] = sum(row["state"] == "started" for row in rows)
            path = self._access_success_path(model)
            expected_paths.add(path)
            durable = _read_json(path)
            if durable != probe or not self._validate_access_artifact(
                    durable, model)["ready"]:
                raise ValueError("durable access probe differs")
            terminal = rows[-1]
            if (
                terminal["artifact_relative_path"]
                != path.relative_to(self.out_dir).as_posix()
                or terminal["artifact_sha256"] != _file_sha(path)
            ):
                raise ValueError("access terminal artifact hash differs")
        if report.get("attempt_counts") != counts:
            raise ValueError("access attempt counts differ")
        observed_paths = self._artifact_files("access", "probes")
        if observed_paths != expected_paths:
            raise ValueError("access probe artifact coverage differs")
        _assert_no_credentials(report)
        if return_report:
            return report
        return {
            "valid": True,
            "scope": "access",
            "model_count": len(self.models),
            "profile_id": CHEAP_PROFILE_ID,
        }

    # --------------------------- public episodes ------------------------
    def _episode_journal_path(self):
        return self._path("episodes", "attempt-journal.jsonl")

    def _stage_journal_path(self):
        return self._path("evidence", "stage-journal.jsonl")

    def _episode_events(self):
        events = _read_jsonl(self._episode_journal_path())
        latest = {}
        previous_hash = None
        previous_time = None
        for index, event in enumerate(events, 1):
            item_id = event.get("item_id") if type(event) is dict else None
            model = event.get("logical_model_id") if type(event) is dict else None
            key = (item_id, model)
            if (
                type(event) is not dict
                or event.get("journal_version") != EPISODE_JOURNAL_VERSION
                or event.get("event_index") != index
                or event.get("profile_id") != CHEAP_PROFILE_ID
                or event.get("profile_sha256") != manifest.cheap_panel_sha256()
                or item_id not in self._by_id
                or model not in self.models
                or event.get("configuration_id") != self.identities[model][
                    "configuration_id"]
                or event.get("source_command") not in {"canary", "smoke"}
                or type(event.get("attempt_number")) is not int
                or not 1 <= event["attempt_number"] <= MAX_ATTEMPTS
                or event.get("state") not in {
                    "started", "abandoned", "succeeded", "failed",
                }
                or event.get("previous_event_sha256") != previous_hash
                or event.get("event_sha256") != _sha(
                    _without_hash(event, "event_sha256"))
            ):
                raise ValueError("episode attempt journal binding differs")
            timestamp = _parse_timestamp(event.get("timestamp_utc"))
            if previous_time is not None and timestamp <= previous_time:
                raise ValueError("episode attempt journal time is not monotonic")
            previous_time = timestamp
            prior = latest.get(key)
            if event["state"] == "started":
                if (
                    event.get("start_event_sha256") is not None
                    or event.get("artifact_relative_path") is not None
                    or event.get("artifact_sha256") is not None
                    or event.get("terminal_kind") is not None
                    or event["attempt_number"] != 1 + sum(
                        row.get("item_id") == item_id
                        and row.get("logical_model_id") == model
                        and row.get("state") == "started"
                        for row in events[:index - 1]
                    )
                    or (prior is not None and prior["state"] not in {
                        "abandoned", "failed",
                    })
                    or not SHA256_RE.fullmatch(event.get("request_sha256", ""))
                    or not SHA256_RE.fullmatch(
                        event.get("transport_descriptor_sha256", ""))
                ):
                    raise ValueError("episode start transition differs")
            else:
                if (
                    prior is None
                    or prior["state"] != "started"
                    or prior["attempt_number"] != event["attempt_number"]
                    or event.get("start_event_sha256") != prior["event_sha256"]
                    or event.get("request_sha256") != prior["request_sha256"]
                    or event.get("transport_descriptor_sha256") != prior[
                        "transport_descriptor_sha256"]
                ):
                    raise ValueError("episode terminal transition differs")
                if event["state"] == "abandoned":
                    if (
                        event.get("artifact_relative_path") is not None
                        or event.get("artifact_sha256") is not None
                        or event.get("terminal_kind") != "pre_completion_interruption"
                    ):
                        raise ValueError("episode abandonment differs")
                elif (
                    type(event.get("artifact_relative_path")) is not str
                    or not SHA256_RE.fullmatch(event.get("artifact_sha256", ""))
                    or event.get("terminal_kind") not in {
                        "validated_episode", "provider_terminal_failure",
                        "integrity_rejection", "qualification_readiness_rejection",
                    }
                ):
                    raise ValueError("episode terminal artifact differs")
            latest[key] = event
            previous_hash = event["event_sha256"]
        _assert_no_credentials(events)
        return events

    def _stage_evidence_events(self, episode_events=None):
        if episode_events is None:
            episode_events = self._episode_events()
        events = _read_jsonl(self._stage_journal_path())
        starts = {
            (event["item_id"], event["logical_model_id"],
             event["attempt_number"]): event
            for event in episode_events if event["state"] == "started"
        }
        outcomes = {
            (event["item_id"], event["logical_model_id"],
             event["attempt_number"]): event
            for event in episode_events if event["state"] != "started"
        }
        by_attempt = {}
        previous_hash = None
        previous_time = None
        for index, event in enumerate(events, 1):
            item_id = event.get("item_id") if type(event) is dict else None
            model = (
                event.get("logical_model_id")
                if type(event) is dict else None
            )
            attempt = event.get("attempt_number") if type(event) is dict else None
            key = (item_id, model, attempt)
            start = starts.get(key)
            prior_stages = by_attempt.setdefault(key, [])
            expected_stage = (
                contracts.STAGES[len(prior_stages)]
                if len(prior_stages) < len(contracts.STAGES) else None
            )
            if (
                type(event) is not dict
                or event.get("stage_journal_version")
                != STAGE_JOURNAL_VERSION
                or event.get("event_index") != index
                or event.get("profile_id") != CHEAP_PROFILE_ID
                or event.get("profile_sha256")
                != manifest.cheap_panel_sha256()
                or item_id not in self._by_id
                or model not in self.models
                or event.get("configuration_id")
                != self.identities[model]["configuration_id"]
                or type(attempt) is not int
                or not 1 <= attempt <= MAX_ATTEMPTS
                or start is None
                or event.get("source_command")
                != start["source_command"]
                or event.get("stage") != expected_stage
                or event.get("episode_start_event_sha256")
                != start["event_sha256"]
                or not SHA256_RE.fullmatch(event.get("request_sha256", ""))
                or not SHA256_RE.fullmatch(
                    event.get("transport_descriptor_sha256", "")
                )
                or type(event.get("artifact_relative_path")) is not str
                or not SHA256_RE.fullmatch(event.get("artifact_sha256", ""))
                or event.get("previous_event_sha256") != previous_hash
                or event.get("event_sha256") != _sha(
                    _without_hash(event, "event_sha256")
                )
            ):
                raise ValueError("stage evidence journal binding differs")
            timestamp = _parse_timestamp(event.get("timestamp_utc"))
            start_time = _parse_timestamp(start["timestamp_utc"])
            if (
                timestamp <= start_time
                or (previous_time is not None and timestamp <= previous_time)
            ):
                raise ValueError("stage evidence journal time is not monotonic")
            outcome = outcomes.get(key)
            if outcome is not None and timestamp >= _parse_timestamp(
                    outcome["timestamp_utc"]):
                raise ValueError("stage evidence followed its attempt outcome")

            path = self._stage_path(item_id, model, attempt, expected_stage)
            if (
                event["artifact_relative_path"]
                != path.relative_to(self.out_dir).as_posix()
                or not path.is_file()
                or event["artifact_sha256"] != _file_sha(path)
            ):
                raise ValueError(
                    "stage evidence journal artifact is missing or differs"
                )
            artifact = self._validate_stage_artifact(
                _read_json(path), item_id, model, attempt, expected_stage
            )
            if (
                artifact["source_command"] != start["source_command"]
                or event["request_sha256"]
                != artifact["request"]["request_sha256"]
                or event["transport_descriptor_sha256"]
                != _sha(artifact["transport_descriptor"])
                or (expected_stage == "stage_1" and (
                    event["request_sha256"] != start["request_sha256"]
                    or event["transport_descriptor_sha256"]
                    != start["transport_descriptor_sha256"]
                ))
            ):
                raise ValueError("stage evidence journal content differs")
            prior_stages.append(event)
            previous_hash = event["event_sha256"]
            previous_time = timestamp
        _assert_no_credentials(events)
        return events

    def _append_stage_evidence_event(
            self, *, item_id, model, source, attempt, stage, start,
            artifact_path, artifact):
        events = _read_jsonl(self._stage_journal_path())
        if events and (
            type(events[-1]) is not dict
            or events[-1].get("event_index") != len(events)
            or events[-1].get("event_sha256") != _sha(
                _without_hash(events[-1], "event_sha256")
            )
        ):
            raise ValueError("stage evidence journal tail differs")
        event = {
            "stage_journal_version": STAGE_JOURNAL_VERSION,
            "event_index": len(events) + 1,
            "profile_id": CHEAP_PROFILE_ID,
            "profile_sha256": manifest.cheap_panel_sha256(),
            "item_id": item_id,
            "logical_model_id": model,
            "configuration_id": self.identities[model]["configuration_id"],
            "source_command": source,
            "attempt_number": attempt,
            "stage": stage,
            "episode_start_event_sha256": start["event_sha256"],
            "request_sha256": artifact["request"]["request_sha256"],
            "transport_descriptor_sha256": _sha(
                artifact["transport_descriptor"]
            ),
            "artifact_relative_path": artifact_path.relative_to(
                self.out_dir
            ).as_posix(),
            "artifact_sha256": _file_sha(artifact_path),
            "previous_event_sha256": (
                events[-1]["event_sha256"] if events else None
            ),
            "timestamp_utc": self._now(),
        }
        event["event_sha256"] = _sha(event)
        _append_jsonl(self._stage_journal_path(), event)
        return event

    def _append_episode_event(
            self, *, item_id, model, source, attempt, state, request_sha,
            descriptor_sha, start=None, artifact=None, terminal_kind=None):
        events = self._episode_events()
        relative = None
        artifact_sha = None
        if artifact is not None:
            relative = Path(artifact).resolve().relative_to(self.out_dir).as_posix()
            artifact_sha = _file_sha(artifact)
        event = {
            "journal_version": EPISODE_JOURNAL_VERSION,
            "event_index": len(events) + 1,
            "profile_id": CHEAP_PROFILE_ID,
            "profile_sha256": manifest.cheap_panel_sha256(),
            "item_id": item_id,
            "logical_model_id": model,
            "configuration_id": self.identities[model]["configuration_id"],
            "source_command": source,
            "attempt_number": attempt,
            "state": state,
            "request_sha256": request_sha,
            "transport_descriptor_sha256": descriptor_sha,
            "start_event_sha256": start["event_sha256"] if start else None,
            "artifact_relative_path": relative,
            "artifact_sha256": artifact_sha,
            "terminal_kind": terminal_kind,
            "previous_event_sha256": (
                events[-1]["event_sha256"] if events else None
            ),
            "timestamp_utc": self._now(),
        }
        event["event_sha256"] = _sha(event)
        _append_jsonl(self._episode_journal_path(), event)
        self._episode_events()
        return event

    def _arm_events(self, events, item_id, model):
        return [row for row in events if row["item_id"] == item_id
                and row["logical_model_id"] == model]

    def _episode_path(self, item_id, model):
        return self._path("episodes", item_id, f"{model}.json")

    def _episode_failure_path(self, item_id, model, attempt):
        return self._path(
            "failures", "episodes", item_id, model,
            f"attempt-{attempt:02d}.json",
        )

    def _stage_path(self, item_id, model, attempt, stage):
        return self._path(
            "evidence", item_id, model, f"attempt-{attempt:02d}",
            f"{stage}.json",
        )

    def _stage_artifact(self, item_id, model, source, attempt, event):
        request, result, descriptor = self._validate_stage_event(event, model)
        body = {
            "stage_artifact_version": STAGE_ARTIFACT_VERSION,
            "purpose": "qualification-only",
            "measurement_label": self.provenance,
            "profile_id": CHEAP_PROFILE_ID,
            "profile_sha256": manifest.cheap_panel_sha256(),
            "item_id": item_id,
            "logical_model_id": model,
            "provider_model_id": self.identities[model]["provider_model_id"],
            "configuration_id": self.identities[model]["configuration_id"],
            "source_command": source,
            "attempt_number": attempt,
            "stage": request["stage"],
            "request": request,
            "result": result,
            "transport_descriptor": descriptor,
            "attestation": deepcopy(event.get("attestation")),
        }
        body["stage_artifact_sha256"] = _sha(body)
        _assert_no_credentials(body)
        return body

    def _validate_stage_artifact(
            self, artifact, item_id, model, attempt, stage):
        if (
            type(artifact) is not dict
            or artifact.get("stage_artifact_version") != STAGE_ARTIFACT_VERSION
            or artifact.get("purpose") != "qualification-only"
            or artifact.get("measurement_label") != self.provenance
            or artifact.get("profile_id") != CHEAP_PROFILE_ID
            or artifact.get("profile_sha256") != manifest.cheap_panel_sha256()
            or artifact.get("item_id") != item_id
            or artifact.get("logical_model_id") != model
            or artifact.get("provider_model_id") != self.identities[model][
                "provider_model_id"]
            or artifact.get("configuration_id") != self.identities[model][
                "configuration_id"]
            or artifact.get("source_command") not in {"canary", "smoke"}
            or artifact.get("attempt_number") != attempt
            or artifact.get("stage") != stage
            or artifact.get("stage_artifact_sha256") != _sha(
                _without_hash(artifact, "stage_artifact_sha256"))
        ):
            raise ValueError("stage artifact profile/hash/identity differs")
        request = contracts.validate_stage_request(artifact.get("request"))
        result = contracts.validate_stage_result(artifact.get("result"), request)
        if (
            request["stage"] != stage
            or request["logical_model_id"] != model
            or request["provider_model_id"] != self.identities[model][
                "provider_model_id"]
            or request["configuration_id"] != self.identities[model][
                "configuration_id"]
            or _sha(artifact.get("transport_descriptor")) != result[
                "transport_request_sha256"]
        ):
            raise ValueError("stage artifact evidence differs")
        _assert_no_credentials(artifact)
        return artifact

    def _normalize_run(self, run):
        if type(run) is not dict:
            raise ValueError("provider driver returned an unsupported run")
        required = {
            "status", "provenance", "requests", "results",
            "transport_descriptors",
        }
        if not required.issubset(run):
            raise ValueError("provider driver run is incomplete")
        return deepcopy(run)

    def _episode_ready(self, run, model):
        requests = run.get("requests")
        results = run.get("results")
        descriptors = run.get("transport_descriptors")
        if (
            run.get("status") != "complete"
            or type(requests) is not list
            or type(results) is not list
            or type(descriptors) is not list
            or not (len(requests) == len(results) == len(descriptors) == 4)
        ):
            return False
        identity = self.identities[model]
        for index, (request, result, descriptor) in enumerate(zip(
                requests, results, descriptors)):
            request = contracts.validate_stage_request(request)
            result = contracts.validate_stage_result(result, request)
            if (
                request["stage"] != contracts.STAGES[index]
                or request["logical_model_id"] != model
                or request["provider_model_id"] != identity["provider_model_id"]
                or request["configuration_id"] != identity["configuration_id"]
                or result["returned_provider_model_id"]
                != identity["provider_model_id"]
                or result["returned_provider_name"] != EXPECTED_PROVIDER
                or result["terminal_status"] != "complete"
                or result["integrity"]["integrity_valid"] is not True
                or result["integrity"]["mechanically_resolved"] is not True
                or result["integrity"]["measurement_ready"] is not (
                    self.run_mode == "live")
                or _sha(descriptor) != result["transport_request_sha256"]
            ):
                return False
        return True

    def _episode_failure_kind(self, run):
        results = run.get("results", [])
        if results:
            terminal = results[-1].get("terminal_status")
            if terminal == "failed":
                return "provider_terminal_failure"
            if terminal == "invalidated":
                return "integrity_rejection"
        return "qualification_readiness_rejection"

    def _build_episode_artifact(self, item_id, model, source, attempt, run):
        normalized = self._normalize_run(run)
        ready = self._episode_ready(normalized, model)
        body = {
            "episode_artifact_version": EPISODE_ARTIFACT_VERSION,
            "purpose": "qualification-only",
            "measurement_label": self.provenance,
            "qualification_measurement_class": QUALIFICATION_CLASS,
            "measurement_ready": ready and self.run_mode == "live",
            "profile_id": CHEAP_PROFILE_ID,
            "profile_sha256": manifest.cheap_panel_sha256(),
            "item_id": item_id,
            "logical_model_id": model,
            "provider_model_id": self.identities[model]["provider_model_id"],
            "configuration_id": self.identities[model]["configuration_id"],
            "expected_returned_provider": EXPECTED_PROVIDER,
            "source_command": source,
            "attempt_number": attempt,
            "ready": ready,
            "failure_kind": None if ready else self._episode_failure_kind(
                normalized
            ),
            "run": normalized,
            "stage_artifact_sha256s": [
                _file_sha(self._stage_path(
                    item_id, model, attempt, stage
                )) for stage in contracts.STAGES
                if self._stage_path(item_id, model, attempt, stage).is_file()
            ],
        }
        body["episode_artifact_sha256"] = _sha(body)
        _assert_no_credentials(body)
        return body

    def _validate_episode_artifact(self, artifact, item_id, model):
        if (
            type(artifact) is not dict
            or artifact.get("episode_artifact_version")
            != EPISODE_ARTIFACT_VERSION
            or artifact.get("purpose") != "qualification-only"
            or artifact.get("measurement_label") != self.provenance
            or artifact.get("qualification_measurement_class")
            != QUALIFICATION_CLASS
            or artifact.get("profile_id") != CHEAP_PROFILE_ID
            or artifact.get("profile_sha256") != manifest.cheap_panel_sha256()
            or artifact.get("item_id") != item_id
            or artifact.get("logical_model_id") != model
            or artifact.get("provider_model_id") != self.identities[model][
                "provider_model_id"]
            or artifact.get("configuration_id") != self.identities[model][
                "configuration_id"]
            or artifact.get("expected_returned_provider") != EXPECTED_PROVIDER
            or artifact.get("source_command") not in {"canary", "smoke"}
            or artifact.get("episode_artifact_sha256") != _sha(
                _without_hash(artifact, "episode_artifact_sha256"))
        ):
            raise ValueError("episode artifact profile/hash/identity differs")
        attempt = artifact.get("attempt_number")
        if type(attempt) is not int or not 1 <= attempt <= MAX_ATTEMPTS:
            raise ValueError("episode artifact attempt differs")
        run = self._normalize_run(artifact.get("run"))
        ready = self._episode_ready(run, model)
        expected_failure = None if ready else self._episode_failure_kind(run)
        if (
            artifact.get("ready") is not ready
            or artifact.get("measurement_ready") is not (
                ready and self.run_mode == "live")
            or artifact.get("failure_kind") != expected_failure
        ):
            raise ValueError("episode artifact readiness differs")
        stage_hashes = []
        for stage in contracts.STAGES[:len(run.get("results", []))]:
            path = self._stage_path(item_id, model, attempt, stage)
            stage_artifact = self._validate_stage_artifact(
                _read_json(path), item_id, model, attempt, stage
            )
            if stage_artifact["request"] != run["requests"][
                    contracts.STAGES.index(stage)] or stage_artifact[
                        "result"] != run["results"][contracts.STAGES.index(stage)]:
                raise ValueError("episode run differs from durable stage evidence")
            stage_hashes.append(_file_sha(path))
        if artifact.get("stage_artifact_sha256s") != stage_hashes:
            raise ValueError("episode stage-artifact hashes differ")
        _assert_no_credentials(artifact)
        return artifact

    def _reconcile_episode_orphan(self, item_id, model, events):
        rows = self._arm_events(events, item_id, model)
        latest = rows[-1] if rows else None
        if latest is None or latest["state"] != "started":
            return events
        attempt = latest["attempt_number"]
        candidates = [path for path in (
            self._episode_path(item_id, model),
            self._episode_failure_path(item_id, model, attempt),
        ) if path.is_file()]
        if not candidates:
            return events
        if len(candidates) != 1:
            raise ValueError("ambiguous orphan episode artifacts")
        path = candidates[0]
        artifact = self._validate_episode_artifact(
            _read_json(path), item_id, model
        )
        state = "succeeded" if artifact["ready"] else "failed"
        self._append_episode_event(
            item_id=item_id,
            model=model,
            source=latest["source_command"],
            attempt=attempt,
            state=state,
            request_sha=latest["request_sha256"],
            descriptor_sha=latest["transport_descriptor_sha256"],
            start=latest,
            artifact=path,
            terminal_kind=(
                "validated_episode" if state == "succeeded"
                else artifact["failure_kind"]
            ),
        )
        return self._episode_events()

    def _prepare_episode_attempt(
            self, item_id, model, source, *, retry_failed):
        events = self._reconcile_episode_orphan(
            item_id, model, self._episode_events()
        )
        rows = self._arm_events(events, item_id, model)
        latest = rows[-1] if rows else None
        starts = sum(row["state"] == "started" for row in rows)
        if latest is not None and latest["state"] == "succeeded":
            self._validate_episode_artifact(
                _read_json(self._episode_path(item_id, model)), item_id, model
            )
            return None
        if latest is not None and latest["state"] == "failed":
            if not retry_failed:
                raise ValueError(
                    "durable qualification failure requires an explicit retry"
                )
            self._validate_episode_namespaces(events)
            if starts >= MAX_ATTEMPTS:
                raise ValueError("qualification exceeded the three-attempt ceiling")
            return starts + 1
        if latest is not None and latest["state"] == "started":
            self._validate_episode_namespaces(events)
            if starts >= MAX_ATTEMPTS:
                raise ValueError("qualification exceeded the three-attempt ceiling")
            self._append_episode_event(
                item_id=item_id,
                model=model,
                source=latest["source_command"],
                attempt=latest["attempt_number"],
                state="abandoned",
                request_sha=latest["request_sha256"],
                descriptor_sha=latest["transport_descriptor_sha256"],
                start=latest,
                terminal_kind="pre_completion_interruption",
            )
            return starts + 1
        if latest is not None and latest["state"] == "abandoned":
            self._validate_episode_namespaces(events)
            if starts >= MAX_ATTEMPTS:
                raise ValueError("qualification exceeded the three-attempt ceiling")
            return starts + 1
        return 1

    def _run_episode_arm(self, item_id, model, source, attempt):
        episode = self._by_id[item_id]
        started = []
        stages = []

        def before_stage(event):
            request, descriptor = self._validate_hook_identity(event, model)
            if request["stage"] == "stage_1":
                if started:
                    raise ValueError("episode driver repeated stage-one start")
                started.append(self._append_episode_event(
                    item_id=item_id,
                    model=model,
                    source=source,
                    attempt=attempt,
                    state="started",
                    request_sha=request["request_sha256"],
                    descriptor_sha=_sha(descriptor),
                ))
            elif not started:
                raise ValueError("episode later stage preceded durable start")

        def stage_sink(event):
            if len(started) != 1:
                raise ValueError("episode stage lacks durable start")
            request, _result, _descriptor = self._validate_stage_event(
                event, model
            )
            if request["stage"] != contracts.STAGES[len(stages)]:
                raise ValueError("episode provider stages are not contiguous")
            artifact = self._stage_artifact(
                item_id, model, source, attempt, event
            )
            path = self._stage_path(
                item_id, model, attempt, request["stage"]
            )
            _write_new_json(path, artifact)
            self._append_stage_evidence_event(
                item_id=item_id,
                model=model,
                source=source,
                attempt=attempt,
                stage=request["stage"],
                start=started[0],
                artifact_path=path,
                artifact=artifact,
            )
            stages.append(artifact)

        run = self._call_driver(
            episode, model, before_stage=before_stage, stage_sink=stage_sink
        )
        if len(started) != 1:
            raise ValueError("episode driver returned without durable start")
        artifact = self._build_episode_artifact(
            item_id, model, source, attempt, run
        )
        if artifact["ready"]:
            path = self._episode_path(item_id, model)
            state = "succeeded"
            terminal_kind = "validated_episode"
        else:
            path = self._episode_failure_path(item_id, model, attempt)
            state = "failed"
            terminal_kind = artifact["failure_kind"]
        _write_new_json(path, artifact)
        self._append_episode_event(
            item_id=item_id,
            model=model,
            source=source,
            attempt=attempt,
            state=state,
            request_sha=started[0]["request_sha256"],
            descriptor_sha=started[0]["transport_descriptor_sha256"],
            start=started[0],
            artifact=path,
            terminal_kind=terminal_kind,
        )
        if state == "failed":
            raise ValueError(
                "durable qualification failure recorded; explicit retry is required"
            )

    def _journal_prefix(self, event_count):
        path = self._episode_journal_path()
        lines = path.read_bytes().splitlines(keepends=True) if path.exists() else []
        if event_count > len(lines):
            raise ValueError("episode journal prefix count exceeds journal")
        return hashlib.sha256(b"".join(lines[:event_count])).hexdigest()

    def _validate_episode_namespaces(self, events):
        expected_episodes = {self._episode_journal_path()}
        expected_failures = set()
        stage_events = self._stage_evidence_events(events)
        expected_evidence = {
            self._stage_path(
                event["item_id"], event["logical_model_id"],
                event["attempt_number"], event["stage"],
            ) for event in stage_events
        }
        if self._stage_journal_path().exists():
            expected_evidence.add(self._stage_journal_path())
        stage_events_by_attempt = {}
        for event in stage_events:
            key = (
                event["item_id"], event["logical_model_id"],
                event["attempt_number"],
            )
            stage_events_by_attempt.setdefault(key, []).append(event)
        starts = {}
        outcomes = {}
        for event in events:
            key = (
                event["item_id"], event["logical_model_id"],
                event["attempt_number"],
            )
            if event["state"] == "started":
                starts[key] = event
            else:
                outcomes[key] = event
            if event["state"] not in {"succeeded", "failed"}:
                continue
            item_id, model, attempt = key
            path = (
                self._episode_path(item_id, model)
                if event["state"] == "succeeded"
                else self._episode_failure_path(item_id, model, attempt)
            )
            if event["state"] == "succeeded":
                expected_episodes.add(path)
            else:
                expected_failures.add(path)
            if (
                not path.is_file()
                or event["artifact_relative_path"]
                != path.relative_to(self.out_dir).as_posix()
                or event["artifact_sha256"] != _file_sha(path)
            ):
                raise ValueError(
                    "episode journal terminal artifact is missing or differs"
                )
            payload = _read_json(path)
            run = payload.get("run") if type(payload) is dict else None
            results = run.get("results") if type(run) is dict else None
            if type(results) is not list:
                raise ValueError("episode terminal artifact run is invalid")
            recorded_stages = stage_events_by_attempt.get(key, [])
            if (
                [row["stage"] for row in recorded_stages]
                != list(contracts.STAGES[:len(results)])
                or payload.get("stage_artifact_sha256s")
                != [row["artifact_sha256"] for row in recorded_stages]
            ):
                raise ValueError(
                    "episode terminal artifact/stage journal coverage differs"
                )
            artifact = self._validate_episode_artifact(payload, item_id, model)
            expected_ready = event["state"] == "succeeded"
            expected_kind = (
                "validated_episode" if expected_ready
                else artifact["failure_kind"]
            )
            if (
                artifact["attempt_number"] != attempt
                or artifact["source_command"] != event["source_command"]
                or artifact["ready"] is not expected_ready
                or event["terminal_kind"] != expected_kind
            ):
                raise ValueError("episode journal terminal artifact state differs")

        for key, start in starts.items():
            outcome = outcomes.get(key)
            if outcome is not None and outcome["source_command"] != start[
                    "source_command"]:
                raise ValueError("episode journal attempt source differs")

        if (
            self._artifact_files(
                "episodes", suffixes=(".json", ".jsonl")
            ) != expected_episodes
            or self._artifact_files("failures", "episodes")
            != expected_failures
            or self._artifact_files(
                "evidence", suffixes=(".json", ".jsonl")
            ) != expected_evidence
        ):
            raise ValueError(
                "qualification artifact coverage is missing or has extras"
            )
        return expected_episodes | expected_failures | expected_evidence

    def _build_scope_report(self, scope, item_ids, *, reused=0):
        events = self._episode_events()
        artifacts = []
        for item_id in item_ids:
            for model in self.models:
                path = self._episode_path(item_id, model)
                artifact = self._validate_episode_artifact(
                    _read_json(path), item_id, model
                )
                if not artifact["ready"]:
                    raise ValueError("qualification episode is not ready")
                artifacts.append({
                    "item_id": item_id,
                    "logical_model_id": model,
                    "relative_path": path.relative_to(self.out_dir).as_posix(),
                    "artifact_sha256": _file_sha(path),
                    "source_command": artifact["source_command"],
                })
        event_count = len(events)
        body = {
            f"{scope}_version": (
                CANARY_VERSION if scope == "canary" else SMOKE_VERSION
            ),
            "purpose": "qualification-only",
            "measurement_label": self.provenance,
            "qualification_measurement_class": QUALIFICATION_CLASS,
            "measurement_ready": self.run_mode == "live",
            "profile_id": CHEAP_PROFILE_ID,
            "profile_sha256": manifest.cheap_panel_sha256(),
            "public_item_ids": list(item_ids),
            "logical_model_ids": list(self.models),
            "model_episode_count": len(item_ids) * len(self.models),
            "reused_canary_model_episode_count": reused,
            "episode_journal_event_count": event_count,
            "episode_journal_prefix_sha256": self._journal_prefix(event_count),
            "artifacts": artifacts,
        }
        body[f"{scope}_sha256"] = _sha(body)
        return body

    def _execute_scope(self, scope, item_ids, *, retry_failed=False):
        self._validate_root()
        self._verify_access()
        self.preflight_catalog()
        for item_id in item_ids:
            for model in self.models:
                attempt = self._prepare_episode_attempt(
                    item_id, model, scope, retry_failed=retry_failed
                )
                if attempt is not None:
                    self._run_episode_arm(
                        item_id, model, scope, attempt
                    )

    def canary(self, retry_failed=False):
        report_path = self._path("reports", "canary.json")
        if report_path.is_file():
            return self._verify_scope_report("canary", return_report=True)
        self._execute_scope(
            "canary", self.canary_item_ids, retry_failed=retry_failed
        )
        report = self._build_scope_report("canary", self.canary_item_ids)
        _write_new_json(report_path, report)
        return self._verify_scope_report("canary", return_report=True)

    def smoke(self, retry_failed=False):
        report_path = self._path("reports", "smoke.json")
        if report_path.is_file():
            return self._verify_scope_report("smoke", return_report=True)
        self.canary(retry_failed=retry_failed)
        all_ids = tuple(row["id"] for row in self.public_episodes)
        self._execute_scope("smoke", all_ids, retry_failed=retry_failed)
        report = self._build_scope_report(
            "smoke", all_ids,
            reused=len(self.canary_item_ids) * len(self.models),
        )
        _write_new_json(report_path, report)
        return self._verify_scope_report("smoke", return_report=True)

    def _verify_scope_report(self, scope, *, return_report=False):
        if scope not in {"canary", "smoke"}:
            raise ValueError("unknown qualification scope")
        path = self._path("reports", f"{scope}.json")
        if not path.is_file():
            raise ValueError(f"{scope} qualification report is missing")
        report = _read_json(path)
        hash_key = f"{scope}_sha256"
        version_key = f"{scope}_version"
        expected_version = CANARY_VERSION if scope == "canary" else SMOKE_VERSION
        expected_ids = (
            self.canary_item_ids if scope == "canary"
            else tuple(row["id"] for row in self.public_episodes)
        )
        if (
            type(report) is not dict
            or report.get(version_key) != expected_version
            or report.get("purpose") != "qualification-only"
            or report.get("measurement_label") != self.provenance
            or report.get("qualification_measurement_class")
            != QUALIFICATION_CLASS
            or report.get("measurement_ready") is not (
                self.run_mode == "live")
            or report.get("profile_id") != CHEAP_PROFILE_ID
            or report.get("profile_sha256") != manifest.cheap_panel_sha256()
            or report.get("public_item_ids") != list(expected_ids)
            or report.get("logical_model_ids") != list(self.models)
            or report.get("model_episode_count")
            != len(expected_ids) * len(self.models)
            or report.get("reused_canary_model_episode_count") != (
                0 if scope == "canary"
                else len(self.canary_item_ids) * len(self.models)
            )
            or report.get(hash_key) != _sha(_without_hash(report, hash_key))
        ):
            raise ValueError(f"{scope} report profile/hash binding differs")
        event_count = report.get("episode_journal_event_count")
        if (
            type(event_count) is not int
            or event_count < 1
            or report.get("episode_journal_prefix_sha256")
            != self._journal_prefix(event_count)
        ):
            raise ValueError(f"{scope} report journal prefix differs")
        expected_artifacts = []
        for item_id in expected_ids:
            for model in self.models:
                artifact_path = self._episode_path(item_id, model)
                artifact = self._validate_episode_artifact(
                    _read_json(artifact_path), item_id, model
                )
                if not artifact["ready"]:
                    raise ValueError("qualification episode is not ready")
                expected_artifacts.append({
                    "item_id": item_id,
                    "logical_model_id": model,
                    "relative_path": artifact_path.relative_to(
                        self.out_dir).as_posix(),
                    "artifact_sha256": _file_sha(artifact_path),
                    "source_command": artifact["source_command"],
                })
        if report.get("artifacts") != expected_artifacts:
            raise ValueError(f"{scope} artifact coverage/hash differs")
        events = self._episode_events()
        self._validate_episode_namespaces(events)
        for item_id in expected_ids:
            for model in self.models:
                rows = self._arm_events(events, item_id, model)
                if not rows or rows[-1]["state"] != "succeeded":
                    raise ValueError(f"{scope} episode journal is incomplete")
                artifact_path = self._episode_path(item_id, model)
                if (
                    rows[-1]["artifact_relative_path"]
                    != artifact_path.relative_to(self.out_dir).as_posix()
                    or rows[-1]["artifact_sha256"] != _file_sha(artifact_path)
                ):
                    raise ValueError(f"{scope} terminal artifact hash differs")
        _assert_no_credentials(report)
        if return_report:
            return report
        return {
            "valid": True,
            "scope": scope,
            "model_episode_count": len(expected_artifacts),
            "profile_id": CHEAP_PROFILE_ID,
        }

    def _expected_whole_root_files(self):
        expected = {
            self._path("run_metadata.json"),
            self._path("catalog", "preflight.json"),
        }
        access_report = self._path("access", "report.json")
        access_journal = self._access_journal_path()
        episode_journal = self._episode_journal_path()
        report_paths = {
            name: self._path("reports", f"{name}.json")
            for name in ("canary", "smoke", "qualification")
        }
        present_reports = {
            name for name, path in report_paths.items() if path.exists()
        }
        has_episode_state = episode_journal.exists() or bool(present_reports)
        has_access_state = (
            access_report.exists() or access_journal.exists()
            or has_episode_state
        )

        if has_access_state:
            expected.update({access_report, access_journal})
            for event in self._access_events():
                if event["state"] == "succeeded":
                    expected.add(self._access_success_path(
                        event["logical_model_id"]
                    ))
                elif event["state"] == "failed":
                    expected.add(self._access_failure_path(
                        event["logical_model_id"], event["attempt_number"]
                    ))

        if has_episode_state:
            events = self._episode_events()
            expected.update(self._validate_episode_namespaces(events))

        expected.update(report_paths[name] for name in present_reports)
        if "smoke" in present_reports or "qualification" in present_reports:
            expected.add(report_paths["canary"])
        if "qualification" in present_reports:
            expected.add(report_paths["smoke"])
        return expected

    def _observed_whole_root_entries(self):
        try:
            root_mode = os.lstat(self.out_dir).st_mode
        except OSError as exc:
            raise ValueError("qualification artifact root is unavailable") from exc
        if stat.S_ISLNK(root_mode) or not stat.S_ISDIR(root_mode):
            raise ValueError("qualification artifact root is not a real directory")

        files = set()
        directories = {self.out_dir}
        pending = [self.out_dir]
        while pending:
            directory = pending.pop()
            try:
                entries = list(os.scandir(directory))
            except OSError as exc:
                raise ValueError(
                    "qualification artifact root cannot be inspected"
                ) from exc
            for entry in entries:
                path = Path(entry.path)
                try:
                    mode = entry.stat(follow_symlinks=False).st_mode
                except OSError as exc:
                    raise ValueError(
                        "qualification artifact root changed during inspection"
                    ) from exc
                if stat.S_ISLNK(mode):
                    raise ValueError(
                        "qualification artifact root contains a symlink"
                    )
                if stat.S_ISDIR(mode):
                    directories.add(path)
                    pending.append(path)
                elif stat.S_ISREG(mode):
                    files.add(path)
                else:
                    raise ValueError(
                        "qualification artifact root contains an unexpected "
                        "file type"
                    )
        return files, directories

    def _verify_whole_root_closure(self):
        expected_files = self._expected_whole_root_files()
        expected_directories = {self.out_dir}
        for path in expected_files:
            parent = path.parent
            while parent != self.out_dir:
                expected_directories.add(parent)
                parent = parent.parent
            expected_directories.add(self.out_dir)

        observed_files, observed_directories = (
            self._observed_whole_root_entries()
        )
        if (
            observed_files != expected_files
            or observed_directories != expected_directories
        ):
            raise ValueError(
                "qualification artifact root closure has missing or extra "
                "files/directories"
            )

    def verify(self, scope="all"):
        self._validate_root()
        if scope not in VERIFY_SCOPES:
            raise ValueError(f"verify scope must be one of {VERIFY_SCOPES}")
        self._validate_catalog_artifact()
        scopes = [scope] if scope != "all" else [
            name for name, path in (
                ("access", self._path("access", "report.json")),
                ("canary", self._path("reports", "canary.json")),
                ("smoke", self._path("reports", "smoke.json")),
                ("qualification", self._path(
                    "reports", "qualification.json"
                )),
            ) if path.is_file()
        ]
        if not scopes:
            raise ValueError("no qualification artifacts are available")
        reports = {}
        for name in scopes:
            if name == "access":
                reports[name] = self._verify_access()
            elif name == "qualification":
                reports[name] = self._verify_qualification_report()
            else:
                reports[name] = self._verify_scope_report(name)
        if scope != "all":
            return reports[scope]
        self._verify_whole_root_closure()
        return {
            "valid": all(row["valid"] for row in reports.values()),
            "purpose": "qualification-only",
            "profile_id": CHEAP_PROFILE_ID,
            "scopes": reports,
        }

    def _response_for_stage(self, artifact, stage):
        index = contracts.STAGES.index(stage)
        result = artifact["run"]["results"][index]
        return result["attempts"][-1]["raw_final_message"]

    def _qualification_metrics(self):
        model_reports = {}
        for model in self.models:
            labels = []
            scores = []
            updates = []
            for episode in self.public_episodes:
                item_id = episode["id"]
                hidden = self._sidecar[item_id]
                artifact = self._validate_episode_artifact(
                    _read_json(self._episode_path(item_id, model)), item_id, model
                )
                stage2 = self._response_for_stage(artifact, "stage_2")
                stage3 = self._response_for_stage(artifact, "stage_3")
                stage4 = self._response_for_stage(artifact, "stage_4")
                scored = action_scale.score_response(stage4)
                if scored["mechanical_flag"]:
                    raise ValueError("qualification stage-four response is unresolved")
                update = stage3_update.score_update(
                    stage2,
                    stage3,
                    hidden["true_type"],
                    hidden["cue_variant"],
                    hidden["expected_stage3"],
                )
                if update["mechanical_flag"]:
                    raise ValueError("qualification stage-three response is unresolved")
                labels.append(1 if hidden["true_type"] == "benign" else 0)
                scores.append(scored["score"])
                updates.append(bool(update["update_correct"]))
            model_reports[model] = {
                "n_public_episodes": len(labels),
                "empirical_auc": roc.empirical_auc(labels, scores),
                "stage3_update_accuracy": sum(updates) / len(updates),
                "mechanically_resolved_rate": 1.0,
            }
        ranges = {}
        for metric in ("empirical_auc", "stage3_update_accuracy"):
            values = [row[metric] for row in model_reports.values()]
            ranges[metric] = {
                "minimum": min(values),
                "maximum": max(values),
                "range": max(values) - min(values),
            }
        return model_reports, ranges

    def _qualification_report_payload(self):
        model_reports, ranges = self._qualification_metrics()
        smoke_path = self._path("reports", "smoke.json")
        body = {
            "report_version": REPORT_VERSION,
            "purpose": "qualification-only",
            "provenance": self.provenance,
            "measurement_label": self.provenance,
            "qualification_measurement_class": QUALIFICATION_CLASS,
            "measurement_ready": self.run_mode == "live",
            "authorizes_calibration": False,
            "authorizes_private_execution": False,
            "authorizes_freeze": False,
            "profile_id": CHEAP_PROFILE_ID,
            "profile_sha256": manifest.cheap_panel_sha256(),
            "public_episode_count_per_model": len(self.public_episodes),
            "smoke_report_sha256": _file_sha(smoke_path),
            "model_reports": model_reports,
            "between_model_ranges": ranges,
            "interpretation_guard": (
                "Public-only cheap-model qualification; not a calibration, "
                "private benchmark result, or multi-vendor concordance test."
            ),
        }
        body["report_sha256"] = _sha(body)
        return body

    def _verify_qualification_report(self, *, return_report=False):
        path = self._path("reports", "qualification.json")
        if not path.is_file():
            raise ValueError("qualification report is missing")
        self._verify_scope_report("smoke")
        report = _read_json(path)
        authorization_fields = (
            "authorizes_calibration", "authorizes_private_execution",
            "authorizes_freeze",
        )
        if (
            type(report) is not dict
            or report.get("report_sha256") != _sha(
                _without_hash(report, "report_sha256")
            )
            or any(report.get(field) is not False
                   for field in authorization_fields)
            or _canonical_bytes(report) != _canonical_bytes(
                self._qualification_report_payload()
            )
        ):
            raise ValueError(
                "qualification report semantic/profile/hash binding differs"
            )
        _assert_no_credentials(report)
        if return_report:
            return report
        return {
            "valid": True,
            "scope": "qualification",
            "model_count": len(self.models),
            "profile_id": CHEAP_PROFILE_ID,
        }

    def report(self):
        self._validate_root()
        self._verify_scope_report("smoke")
        body = self._qualification_report_payload()
        path = self._path("reports", "qualification.json")
        _write_or_validate(path, body)
        return self._verify_qualification_report(return_report=True)


def build_parser():
    parser = argparse.ArgumentParser(
        description=(
            "Run the public-only CHARITROC cheap OpenRouter qualification"
        )
    )
    children = parser.add_subparsers(dest="command", required=True)
    for command in COMMANDS:
        child = children.add_parser(command)
        child.add_argument("--out", required=True)
        child.add_argument("--run-mode", choices=RUN_MODES, required=True)
        if command in {"access", "canary", "smoke"}:
            child.add_argument("--retry-failed", action="store_true")
        if command == "verify":
            child.add_argument("--scope", choices=VERIFY_SCOPES, default="all")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    if args.run_mode == "mock":
        raise SystemExit(
            "mock CLI execution has no hidden fake dependencies; use the "
            "explicit programmatic mock harness"
        )
    runner = CheapOpenRouterQualificationRunner(
        bank_root=Path(__file__).resolve().parents[1],
        out_dir=args.out,
        run_mode=args.run_mode,
    )
    if args.command == "access":
        result = runner.access(retry_failed=args.retry_failed)
    elif args.command == "canary":
        result = runner.canary(retry_failed=args.retry_failed)
    elif args.command == "smoke":
        result = runner.smoke(retry_failed=args.retry_failed)
    elif args.command == "verify":
        result = runner.verify(args.scope)
    else:
        result = runner.report()
    sys.stdout.write(_canonical_bytes(result).decode("utf-8") + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
