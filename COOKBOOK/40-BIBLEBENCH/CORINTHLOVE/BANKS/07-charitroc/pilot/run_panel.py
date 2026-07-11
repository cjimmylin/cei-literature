"""Fail-closed, resumable CHARITROC panel orchestration.

The orchestrator is deliberately thinner than either provider driver.  It
orders immutable sample-plan occurrences, persists already-validated stage
evidence before advancing, scores only canonical raw responses, and keeps a
separate append-only high-level state log and transport-attempt ledger.
"""
from __future__ import annotations

import argparse
import base64
from copy import deepcopy
from datetime import datetime, timedelta, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys

# The documented production invocation executes this file directly. Python
# otherwise places only ``pilot/`` on ``sys.path``, hiding the bank-local
# generator, analysis, scorer, and package modules. Bind imports to this file's
# resolved bank root before any bank module is loaded.
if __package__ in (None, ""):
    _BANK_IMPORT_ROOT = str(Path(__file__).resolve().parents[1])
    if _BANK_IMPORT_ROOT not in sys.path:
        sys.path.insert(0, _BANK_IMPORT_ROOT)

import generator
import yaml

from analysis import analyze as bank_analysis
from lib.payloads import model_turns
from pilot import codex_driver, contracts, gates, manifest, openrouter_driver
from scorers import action_scale, stage3_update


ORCHESTRATION_VERSION = "charitroc-panel-orchestration-v1"
EVIDENCE_VERSION = "charitroc-panel-stage-evidence-v1"
LEDGER_VERSION = "charitroc-panel-stage-attempt-ledger-v1"
INVOCATION_VERSION = "charitroc-panel-invocation-journal-v1"
SCORE_VERSION = "charitroc-panel-mechanical-score-v1"
QUEUE_VERSION = "charitroc-panel-judge-queue-v1"
REPORT_VERSION = "charitroc-panel-report-v1"
ANALYSIS_VERSION = "charitroc-panel-analysis-v1"
PROVIDERS = ("codex", "openrouter")
RUN_MODES = ("mock", "live")
RUN_STAGES = ("smoke", "calibration", "reliability", "private")
EXECUTION_STAGES = RUN_STAGES + ("private-extension",)
COMMANDS = EXECUTION_STAGES + (
    "access", "verify-access", "freeze", "verify", "analyze",
    "analyze-private", "activate-private-extension",
)
MOCK_PROVENANCE = "harness validation, NOT a measurement"
LIVE_PROVENANCE = {
    "codex": "live Codex calibration measurement",
    "openrouter": "live OpenRouter calibration measurement",
}
PRIVATE_CRITERIA_TEMPLATES = tuple({
    "criterion_id": f"{model}-ordinal-auc",
    "logical_model_id": model,
    "threshold": 0.55,
    "direction": "at_least",
    "frozen": True,
} for model in manifest.MODEL_LOGICAL_IDS)

EVIDENCE_KEYS = (
    "evidence_version", "provenance", "provider", "plan_hash",
    "plan_occurrence_id", "item_id", "logical_model_id",
    "configuration_id", "orchestration_attempt", "session_attempt", "stage",
    "request", "result", "transport_descriptor", "attestation",
    "evidence_sha256",
)
LEDGER_KEYS = (
    "ledger_version", "event_id", "provenance", "provider", "plan_hash",
    "plan_occurrence_id", "item_id", "logical_model_id",
    "configuration_id", "orchestration_attempt", "session_attempt", "stage",
    "session_id", "transport_attempt", "attempt_started_at_utc",
    "attempt_completed_at_utc",
    "request_sha256", "result_sha256", "transport_request_sha256",
    "raw_trace_sha256", "artifact_relative_path", "artifact_sha256",
    "stage_terminal_status", "format_repair_count", "state",
    "persisted_at_utc",
)
INVOCATION_KEYS = (
    "invocation_version", "event_id", "provenance", "provider", "plan_hash",
    "plan_occurrence_id", "item_id", "logical_model_id",
    "configuration_id", "orchestration_attempt", "execution_id",
    "integrity_session", "stage", "request_sha256",
    "transport_descriptor_sha256", "journal_state", "reason",
    "timestamp_utc", "event_sha256",
)
FAILURE_ARTIFACT_KEYS = (
    "failure_artifact_version", "provenance", "provider", "plan_hash",
    "plan_occurrence_id", "item_id", "logical_model_id",
    "configuration_id", "orchestration_attempt", "integrity_session",
    "execution_id", "stage", "failed_request", "failure_record",
    "failure_artifact_sha256",
)
JUDGE_QUEUE_KEYS = (
    "queue_version", "queue_event_id", "provenance", "provider",
    "logical_model_id", "configuration_id", "judge_case_id", "stage",
    "response_artifact_relative_path", "response_artifact_sha256",
    "raw_final_message_sha256", "reason", "queued_at_utc", "queue_sha256",
)
SCORE_KEYS = (
    "score_version", "provenance", "provider", "plan_hash",
    "plan_occurrence_id", "sample_cell_id", "item_id", "logical_model_id",
    "configuration_id", "split", "family", "pair_id", "true_type", "label",
    "cue_variant", "base_rate_benign", "indistinguishable_control",
    "transcript_hash", "stage_count", "stage_terminal_statuses",
    "transport_retry_count", "format_repair_count", "format_repair_flagged",
    "semantic_response_replaced", "tool_calls", "future_text_seen",
    "thread_chain_ok", "terminal_invalidated", "invalidation_reason",
    "unresolved", "judge_queued", "mechanically_resolved", "stage4_score",
    "stage4_intent_score", "stage4_decision", "stage4_intent",
    "stage3_update_correct", "stage3_detail", "evidence_sha256s",
    "reliability_primary_link", "score_sha256",
)

_SECRET_VALUE_RE = re.compile(
    r"(?i)(?:\b(?:sk|rk)-[A-Za-z0-9_-]{8,}|"
    r"\bBearer\s+[A-Za-z0-9._~+/=-]+|\bOPENROUTER_API_KEY\s*=)"
)
_SECRET_KEYS = {
    "api_key", "apikey", "authorization", "password", "passwd",
    "client_secret", "secret", "credential", "credentials", "cookie",
    "access_token", "refresh_token", "private_key",
}
_RFC3339_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
ACCESS_PROVENANCE = "model access probe, NOT a measurement"
ACCESS_FAILURE_VERSION = "charitroc-model-access-failure-v1"
ACCESS_JOURNAL_VERSION = "charitroc-model-access-attempt-journal-v1"
ACCESS_JOURNAL_STATES = ("started", "succeeded", "failed", "abandoned")
ACCESS_JOURNAL_KEYS = {
    "journal_version", "event_index", "provenance", "provider",
    "logical_model_id", "configuration_id", "attempt_number", "state",
    "request_sha256", "transport_descriptor_sha256", "start_event_sha256",
    "artifact_relative_path", "artifact_sha256", "terminal_kind",
    "previous_event_sha256", "timestamp_utc", "event_sha256",
}


class _AccessProbeComplete(RuntimeError):
    """Internal control signal emitted only after a validated first stage."""


class _AccessProbeFailureRecorded(RuntimeError):
    """Internal control signal emitted after durable failed-probe evidence."""


def _canonical_bytes(value):
    return contracts.canonical_json_bytes(value)


def _canonical_sha(value):
    return contracts.canonical_sha256(value)


def _without_hash(value, field):
    return {key: item for key, item in value.items() if key != field}


def _state_event_id(event, ordinal):
    if isinstance(ordinal, bool) or not isinstance(ordinal, int) or ordinal < 0:
        raise ValueError("run-state ordinal must be a non-negative integer")
    return "panel-" + _canonical_sha({
        "plan_hash": event["plan_hash"],
        "occurrence": event["plan_occurrence_id"],
        "model": event["logical_model_id"],
        "session": event["session_attempt"],
        "attempt": event["attempt"],
        "state": event["state"],
        "ordinal": ordinal,
        "timestamp": event["timestamp_utc"],
    })


def _unique_object(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError("duplicate JSON key")
        value[key] = item
    return value


def _read_json(path):
    path = Path(path)
    try:
        with path.open("rb") as handle:
            value = json.loads(
                handle.read().decode("utf-8", errors="strict"),
                object_pairs_hook=_unique_object,
                parse_constant=lambda _value: (_ for _ in ()).throw(
                    ValueError("non-finite JSON")
                ),
            )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        raise ValueError(f"invalid unique-key JSON artifact: {path}") from None
    return value


def _read_jsonl(path):
    path = Path(path)
    if not path.exists():
        return []
    rows = []
    try:
        with path.open("rb") as handle:
            for number, raw in enumerate(handle, 1):
                if not raw.strip():
                    raise ValueError("blank JSONL line")
                rows.append(json.loads(
                    raw.decode("utf-8", errors="strict"),
                    object_pairs_hook=_unique_object,
                    parse_constant=lambda _value: (_ for _ in ()).throw(
                        ValueError("non-finite JSON")
                    ),
                ))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        raise ValueError(
            f"corrupt append-only JSONL artifact {path}"
        ) from None
    return rows


def _assert_no_credentials(value):
    if type(value) is dict:
        for key, item in value.items():
            normalized = key.strip().lower().replace("-", "_")
            if normalized in _SECRET_KEYS:
                raise ValueError("artifact contains credential material")
            _assert_no_credentials(item)
    elif type(value) is list:
        for item in value:
            _assert_no_credentials(item)
    elif type(value) is str and _SECRET_VALUE_RE.search(value):
        raise ValueError("artifact contains credential material")


def _write_new_json(path, value):
    _assert_no_credentials(value)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("x", encoding="utf-8") as handle:
            handle.write(_canonical_bytes(value).decode("utf-8") + "\n")
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError:
        raise ValueError(f"immutable artifact already exists: {path}") from None
    directory_fd = os.open(os.fspath(path.parent), os.O_RDONLY)
    try:
        os.fsync(directory_fd)
    finally:
        os.close(directory_fd)
    return path


def _write_or_validate(path, value):
    path = Path(path)
    if path.exists():
        if _read_json(path) != value:
            raise ValueError(f"immutable artifact differs on replay: {path}")
        return path
    return _write_new_json(path, value)


def _append_jsonl(path, value):
    _assert_no_credentials(value)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    existed = path.exists()
    with path.open("a", encoding="utf-8") as handle:
        handle.write(_canonical_bytes(value).decode("utf-8") + "\n")
        handle.flush()
        os.fsync(handle.fileno())
    if not existed:
        directory_fd = os.open(os.fspath(path.parent), os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    return path


def _load_unique_yaml(path):
    class Loader(yaml.SafeLoader):
        pass

    def unique_mapping(loader, node, deep=False):
        mapping = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            if key in mapping:
                raise ValueError("duplicate YAML key")
            mapping[key] = loader.construct_object(value_node, deep=deep)
        return mapping

    Loader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
    )
    try:
        value = yaml.load(Path(path).read_text(encoding="utf-8"), Loader=Loader)
    except (OSError, UnicodeError, yaml.YAMLError, ValueError):
        raise ValueError(f"invalid unique-key YAML bank artifact: {path}") from None
    if type(value) is not list:
        raise ValueError(f"bank episode artifact must be a list: {path}")
    return value


def _parse_timestamp(value):
    if type(value) is not str or not _RFC3339_RE.fullmatch(value):
        raise ValueError("timestamp must be whole-second RFC3339 UTC")
    try:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=timezone.utc
        )
    except ValueError:
        raise ValueError("timestamp must be valid RFC3339 UTC") from None


def _default_clock():
    return datetime.now(timezone.utc).replace(microsecond=0).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )


def _reject_symlink_components(path):
    candidate = Path(path).expanduser().absolute()
    for current in (candidate, *candidate.parents):
        if current.is_symlink():
            raise ValueError(f"output path may not contain a symlink: {current}")


class PanelOrchestrator:
    """One provider-specific, plan-bound, resumable panel run directory."""

    def __init__(
            self, *, bank_root, out_dir, provider, run_mode, driver=None,
            episodes=None, sidecar=None, judge_token_map=None, clock=None,
            freeze_builder=None, private_validator=None,
            codex_cli_path=None, codex_cli_version="codex-cli 0.134.0",
            bootstrap_draws=2000):
        if provider not in PROVIDERS:
            raise ValueError(f"provider must be explicit: {PROVIDERS}")
        if run_mode not in RUN_MODES:
            raise ValueError(f"run_mode must be explicit: {RUN_MODES}")
        if isinstance(bootstrap_draws, bool) or not isinstance(
                bootstrap_draws, int) or bootstrap_draws < 100:
            raise ValueError("bootstrap_draws must be an integer at least 100")
        if run_mode == "live" and bootstrap_draws != 2000:
            raise ValueError(
                "bootstrap_draws must use the production value 2000 in live mode"
            )
        self.bank_root = Path(bank_root).expanduser().resolve()
        if not self.bank_root.is_dir():
            raise ValueError("bank_root must be an existing directory")
        lexical_out = Path(out_dir).expanduser().absolute()
        _reject_symlink_components(lexical_out)
        lexical_out.mkdir(parents=True, exist_ok=True)
        _reject_symlink_components(lexical_out)
        self.out_dir = lexical_out.resolve()
        self.provider = provider
        self.run_mode = run_mode
        self.provenance = (
            MOCK_PROVENANCE if run_mode == "mock" else LIVE_PROVENANCE[provider]
        )
        self.bootstrap_draws = bootstrap_draws
        self.codex_cli_path = codex_cli_path
        self.codex_cli_version = codex_cli_version
        self._driver = driver
        self._clock = clock or _default_clock
        self._freeze_builder = freeze_builder or self._default_freeze_builder
        self._private_validator = (
            private_validator or self._default_private_validator
        )
        self._freeze_builder_injected = freeze_builder is not None
        self._private_validator_injected = private_validator is not None
        self._live_codex = None
        self._last_timestamp = None
        self._state_cache = {}
        self._ledger_cache = {}
        self._calibration_score_index = None

        supplied = (driver, episodes, sidecar, judge_token_map, clock,
                    freeze_builder, private_validator)
        if run_mode == "live" and any(value is not None for value in supplied):
            raise ValueError(
                "production live orchestration rejects injected dependencies"
            )
        if run_mode == "mock":
            if driver is None or not hasattr(driver, "run_episode"):
                raise ValueError("mock driver must be supplied explicitly")
            if episodes is None or sidecar is None or judge_token_map is None:
                raise ValueError(
                    "mock bank data and judge token map must be explicit"
                )
            self.episodes = deepcopy(episodes)
            self.sidecar = deepcopy(sidecar)
            self.judge_token_map = deepcopy(judge_token_map)
        else:
            self.episodes, self.sidecar, self.judge_token_map = (
                self._load_persisted_bank()
            )
        generator.validate_judge_token_map(
            self.episodes, self.judge_token_map
        )
        self._by_id = {row["id"]: row for row in self.episodes}
        if len(self._by_id) != len(self.episodes) or set(self._by_id) != set(
                self.sidecar):
            raise ValueError("episode/sidecar IDs must match exactly")
        self._judge_by_item = {
            item_id: token for token, item_id in self.judge_token_map.items()
        }
        if set(self._judge_by_item) != set(self._by_id):
            raise ValueError("judge token map must cover every episode exactly")
        # Validate the canonical construction once without writing it.
        manifest.build_sample(
            "calibration", self.episodes, self.sidecar,
            manifest.BANK_GENERATION_SEED,
        )
        self._initialize_metadata()
        self._initialize_timestamp_floor()

    def _load_persisted_bank(self):
        paths = (
            self.bank_root / "seeds_public.yaml",
            self.bank_root / "episodes" / "calibration_bank.yaml",
            self.bank_root / "episodes" / "private_bank.yaml",
        )
        if any(not path.is_file() for path in paths):
            raise ValueError(
                "production live construction requires persisted regenerated bank"
            )
        episodes = []
        for path in paths:
            episodes.extend(_load_unique_yaml(path))
        sidecar = _read_json(self.bank_root / "sidecar" / "ground_truth.json")
        judge_map = _read_json(
            self.bank_root / "sidecar" / "judge_token_map.json"
        )
        return episodes, sidecar, judge_map

    def _metadata_payload(self, created_at):
        return {
            "orchestration_version": ORCHESTRATION_VERSION,
            "provider": self.provider,
            "run_mode": self.run_mode,
            "provenance": self.provenance,
            "panel_manifest_sha256": _canonical_sha(manifest.load_panel()),
            "response_schema_sha256": _canonical_sha(
                manifest.load_response_schema()
            ),
            "created_at_utc": created_at,
        }

    def _initialize_metadata(self):
        path = self._out_path("run_metadata.json")
        if path.exists():
            observed = _read_json(path)
            if type(observed) is not dict:
                raise ValueError("run metadata must be an object")
            expected = self._metadata_payload(observed.get("created_at_utc"))
            if observed != expected:
                raise ValueError("run metadata differs from provider/mode freeze")
            _parse_timestamp(observed["created_at_utc"])
        else:
            _write_new_json(path, self._metadata_payload(self._raw_now()))

    def _initialize_timestamp_floor(self):
        candidates = []
        metadata = _read_json(self._out_path("run_metadata.json"))
        candidates.append(_parse_timestamp(metadata["created_at_utc"]))
        for path in self._jsonl_files("state"):
            for row in _read_jsonl(path):
                if type(row) is dict and "timestamp_utc" in row:
                    candidates.append(_parse_timestamp(row["timestamp_utc"]))
        for path in self._jsonl_files("ledger"):
            for row in _read_jsonl(path):
                if type(row) is dict and "persisted_at_utc" in row:
                    candidates.append(_parse_timestamp(row["persisted_at_utc"]))
        access_journal = self._out_path("access", "attempt-journal.jsonl")
        for row in _read_jsonl(access_journal):
            if type(row) is dict and "timestamp_utc" in row:
                candidates.append(_parse_timestamp(row["timestamp_utc"]))
        self._last_timestamp = max(candidates) if candidates else None

    def _raw_now(self):
        value = self._clock()
        if isinstance(value, datetime):
            value = value.astimezone(timezone.utc).replace(
                microsecond=0
            ).strftime("%Y-%m-%dT%H:%M:%SZ")
        _parse_timestamp(value)
        return value

    def _now(self):
        candidate = _parse_timestamp(self._raw_now())
        if self._last_timestamp is not None and candidate <= self._last_timestamp:
            candidate = self._last_timestamp + timedelta(seconds=1)
        self._last_timestamp = candidate
        return candidate.strftime("%Y-%m-%dT%H:%M:%SZ")

    def _plan_path(self, stage):
        return self._out_path("plans", f"{stage}.json")

    def _state_path(self, stage):
        return self._out_path("state", f"{stage}.jsonl")

    def _ledger_path(self, stage):
        return self._out_path("ledger", f"{stage}.jsonl")

    def _invocation_path(self, stage):
        return self._out_path("invocations", f"{stage}.jsonl")

    def _out_path(self, *parts):
        if not parts:
            return self.out_dir
        candidate = self.out_dir
        for raw in parts:
            part = Path(raw)
            if part.is_absolute() or ".." in part.parts:
                raise ValueError("output artifact path traversal/absolute path forbidden")
            candidate = candidate / part
        try:
            candidate.resolve(strict=False).relative_to(self.out_dir)
        except ValueError:
            raise ValueError("output artifact must remain confined to run root") from None
        current = self.out_dir
        for component in candidate.relative_to(self.out_dir).parts:
            current = current / component
            if current.is_symlink():
                raise ValueError("output artifact symlink is not confined")
        return candidate

    def _jsonl_files(self, *parts):
        root = self._out_path(*parts)
        if not root.exists():
            return []
        if root.is_symlink() or not root.is_dir():
            raise ValueError("JSONL artifact root must be a confined directory")
        files = []
        for path in sorted(root.iterdir()):
            if path.is_symlink():
                raise ValueError("JSONL artifact tree contains a symlink")
            if not path.is_file() or path.suffix != ".jsonl":
                raise ValueError("JSONL artifact tree contains an unexpected file")
            try:
                path.resolve().relative_to(self.out_dir)
            except ValueError:
                raise ValueError(
                    "JSONL artifact escaped the confined output root"
                ) from None
            files.append(path)
        return files

    def _plan(self, stage):
        if stage not in RUN_STAGES:
            raise ValueError(f"run stage must be one of {RUN_STAGES}")
        expected = manifest.build_sample(
            stage, self.episodes, self.sidecar,
            manifest.BANK_GENERATION_SEED,
        )
        path = self._plan_path(stage)
        if path.exists():
            observed = _read_json(path)
            manifest.validate_sample_plan(
                observed, self.episodes, self.sidecar
            )
            if observed != expected:
                raise ValueError("persisted sample plan differs from frozen plan")
            return observed
        path.parent.mkdir(parents=True, exist_ok=True)
        manifest.write_plan_manifest(
            path, expected, self.episodes, self.sidecar, root=self.out_dir
        )
        return expected

    def _all_plans(self):
        return {stage: self._plan(stage) for stage in manifest.SAMPLE_STAGES}

    def _namespace_plan(self, stage):
        if stage in RUN_STAGES:
            return self._plan(stage)
        if stage != "private-extension":
            raise ValueError(
                f"execution stage must be one of {EXECUTION_STAGES}"
            )
        source = self._plan("private")
        extension_entries = self._execution_entries(stage, source)
        # Keep the frozen private plan hash as the authority while exposing a
        # namespace-local entry list to state/evidence accounting.  This is a
        # view, never a replacement sample plan.
        view = deepcopy(source)
        view["entries"] = deepcopy(extension_entries)
        view["extension_entries"] = []
        view["entry_count"] = len(extension_entries)
        view["extension_entry_count"] = 0
        return view

    def _state_events(self, stage, plan, *, refresh=False):
        if not refresh and stage in self._state_cache:
            return self._state_cache[stage]
        events = _read_jsonl(self._state_path(stage))
        if stage == "private-extension":
            validated = []
            for event in events:
                self._validate_incremental_state(
                    event, validated, plan, stage=stage
                )
                validated.append(event)
        else:
            manifest._validate_run_state_history(events, plan)
            for ordinal, event in enumerate(events):
                if event["event_id"] != _state_event_id(event, ordinal):
                    raise ValueError(
                        "run-state event id/hash differs from its content"
                    )
        self._state_cache[stage] = events
        return events

    def _validate_incremental_state(
            self, event, events, plan, *, stage=None):
        rows = plan["entries"]
        occurrences = {row["occurrence_id"]: row for row in rows}
        if stage == "private-extension":
            manifest._validate_run_state_event(event)
            occurrence = occurrences.get(event["plan_occurrence_id"])
            if (
                event["plan_hash"] != plan["plan_hash"]
                or occurrence is None
                or occurrence["item_id"] != event["item_id"]
                or event["logical_model_id"]
                not in occurrence["model_execution_order"]
            ):
                raise ValueError(
                    "private-extension state differs from activated plan view"
                )
        else:
            manifest._bind_run_state_event(event, occurrences, plan)
        if event["event_id"] != _state_event_id(event, len(events)):
            raise ValueError("run-state event id/hash differs from its content")
        if event["event_id"] in {row["event_id"] for row in events}:
            raise ValueError("duplicate append-only run-state event")
        if events and _parse_timestamp(event["timestamp_utc"]) < _parse_timestamp(
                events[-1]["timestamp_utc"]):
            raise ValueError("run-state timestamp must be monotonic")

        def latest(occurrence_id, model_id, session):
            matches = [row for row in events if (
                row["plan_occurrence_id"] == occurrence_id
                and row["logical_model_id"] == model_id
                and row["session_attempt"] == session
            )]
            return matches[-1] if matches else None

        def settled(occurrence_id, model_id):
            second = latest(occurrence_id, model_id, 2)
            if second is not None:
                return second["state"] in {"complete", "failed", "invalidated"}
            first = latest(occurrence_id, model_id, 1)
            return first is not None and first["state"] in {"complete", "failed"}

        active = next((row for row in rows if not all(
            settled(row["occurrence_id"], model)
            for model in row["model_execution_order"]
        )), None)
        if active is None or active["occurrence_id"] != event[
                "plan_occurrence_id"]:
            raise ValueError("run-state occurrence execution order differs")
        model = event["logical_model_id"]
        model_index = active["model_execution_order"].index(model)
        if any(not settled(active["occurrence_id"], prior)
               for prior in active["model_execution_order"][:model_index]):
            raise ValueError("run-state model execution order differs")
        previous = latest(
            active["occurrence_id"], model, event["session_attempt"]
        )
        if previous is None and event["session_attempt"] == 2:
            first = latest(active["occurrence_id"], model, 1)
            if first is None or first["state"] != "invalidated":
                raise ValueError(
                    "session_attempt 2 requires invalidated first session"
                )
        manifest._validate_run_transition(previous, event)

    @staticmethod
    def _latest_state(events, occurrence_id, model_id, session_attempt=None):
        rows = [row for row in events if (
            row["plan_occurrence_id"] == occurrence_id
            and row["logical_model_id"] == model_id
            and (session_attempt is None or row["session_attempt"] == session_attempt)
        )]
        return rows[-1] if rows else None

    @staticmethod
    def _is_settled(events, occurrence_id, model_id):
        session_two = PanelOrchestrator._latest_state(
            events, occurrence_id, model_id, 2
        )
        if session_two is not None:
            return session_two["state"] in {
                "complete", "failed", "invalidated",
            }
        session_one = PanelOrchestrator._latest_state(
            events, occurrence_id, model_id, 1
        )
        return session_one is not None and session_one["state"] in {
            "complete", "failed",
        }

    def _append_state(self, stage, plan, entry, model, *, session_attempt,
                      attempt, state):
        existing = self._state_events(stage, plan)
        timestamp = self._now()
        event = {
            "event_id": "pending",
            "plan_hash": plan["plan_hash"],
            "plan_occurrence_id": entry["occurrence_id"],
            "item_id": entry["item_id"],
            "logical_model_id": model,
            "session_attempt": session_attempt,
            "state": state,
            "attempt": attempt,
            "timestamp_utc": timestamp,
        }
        event["event_id"] = _state_event_id(event, len(existing))
        self._validate_incremental_state(
            event, existing, plan, stage=stage
        )
        _append_jsonl(self._state_path(stage), event)
        existing.append(event)
        return event

    def _append_invocation_row(
            self, stage, plan, entry, model, orchestration_attempt, *,
            execution_id, integrity_session, result_stage, request_sha256,
            descriptor_sha256, journal_state, reason=None):
        if journal_state not in {"started", "abandoned"}:
            raise ValueError("invocation journal state is invalid")
        timestamp = self._now()
        base = {
            "invocation_version": INVOCATION_VERSION,
            "provenance": self.provenance,
            "provider": self.provider,
            "plan_hash": plan["plan_hash"],
            "plan_occurrence_id": entry["occurrence_id"],
            "item_id": entry["item_id"],
            "logical_model_id": model,
            "configuration_id": self._expected_configuration(model),
            "orchestration_attempt": orchestration_attempt,
            "execution_id": execution_id,
            "integrity_session": integrity_session,
            "stage": result_stage,
            "request_sha256": request_sha256,
            "transport_descriptor_sha256": descriptor_sha256,
            "journal_state": journal_state,
            "reason": reason,
            "timestamp_utc": timestamp,
        }
        event = {
            "event_id": "invocation-" + _canonical_sha(base),
            **base,
        }
        event["event_sha256"] = _canonical_sha(event)
        if set(event) != set(INVOCATION_KEYS):
            raise ValueError("invocation journal construction failed")
        _append_jsonl(self._invocation_path(stage), event)
        return event

    def _journal_stage_start(
            self, stage, plan, entry, model, orchestration_attempt, event):
        if type(event) is not dict or set(event) != {
                "provider", "integrity_session", "execution_id", "stage",
                "request", "transport_descriptor", "attestation"}:
            raise ValueError("provider before-stage event keys are not exact")
        request = contracts.validate_stage_request(event["request"])
        if (
            event["provider"] != self.provider
            or event["integrity_session"] not in {1, 2}
            or event["execution_id"] != request["execution_id"]
            or event["stage"] != request["stage"]
            or event["attestation"] is not None
            or request["provider"] != self.provider
            or request["logical_model_id"] != model
            or request["configuration_id"] != self._expected_configuration(model)
        ):
            raise ValueError("provider before-stage event binding mismatch")
        descriptor_sha256 = _canonical_sha(event["transport_descriptor"])
        rows = _read_jsonl(self._invocation_path(stage))
        key = (
            entry["occurrence_id"], model, orchestration_attempt,
            event["integrity_session"], event["stage"],
        )
        matches = [row for row in rows if (
            row.get("plan_occurrence_id"), row.get("logical_model_id"),
            row.get("orchestration_attempt"), row.get("integrity_session"),
            row.get("stage"),
        ) == key and row.get("journal_state") == "started"]
        if matches:
            if len(matches) == 1 and all((
                matches[0]["execution_id"] == event["execution_id"],
                matches[0]["request_sha256"] == request["request_sha256"],
                matches[0]["transport_descriptor_sha256"]
                == descriptor_sha256,
            )):
                return matches[0]
            raise ValueError("provider stage invocation was already journaled")
        return self._append_invocation_row(
            stage, plan, entry, model, orchestration_attempt,
            execution_id=event["execution_id"],
            integrity_session=event["integrity_session"],
            result_stage=event["stage"],
            request_sha256=request["request_sha256"],
            descriptor_sha256=descriptor_sha256,
            journal_state="started",
        )

    def _abandon_open_invocation(
            self, stage, plan, entry, model, orchestration_attempt):
        rows = _read_jsonl(self._invocation_path(stage))
        starts = [row for row in rows if (
            row.get("plan_occurrence_id") == entry["occurrence_id"]
            and row.get("logical_model_id") == model
            and row.get("orchestration_attempt") == orchestration_attempt
            and row.get("journal_state") == "started"
        )]
        if not starts:
            return None
        abandoned = []
        failures = self._collect_failures(stage, plan)
        failure_keys = {(
            row["plan_occurrence_id"], row["logical_model_id"],
            row["orchestration_attempt"], row["integrity_session"],
            row["stage"],
        ) for row in failures}
        for started in starts:
            key = (
                entry["occurrence_id"], model, orchestration_attempt,
                started["integrity_session"], started["stage"],
            )
            artifact_path = self._evidence_path(
                stage, entry["occurrence_id"], model,
                orchestration_attempt, started["integrity_session"],
                started["stage"],
            )
            if artifact_path.is_file() and key in failure_keys:
                raise ValueError(
                    "provider invocation has both evidence and failure terminals"
                )
            if artifact_path.is_file():
                payload = _read_json(artifact_path)
                self._persist_stage_event(
                    stage, plan, entry, model, orchestration_attempt, {
                        "provider": self.provider,
                        "integrity_session": started["integrity_session"],
                        "execution_id": started["execution_id"],
                        "stage": started["stage"],
                        "request": payload["request"],
                        "transport_descriptor": payload[
                            "transport_descriptor"
                        ],
                        "attestation": payload["attestation"],
                        "result": payload["result"],
                    },
                )
                continue
            if key in failure_keys:
                continue
            matching = [row for row in rows if (
                row.get("plan_occurrence_id") == entry["occurrence_id"]
                and row.get("logical_model_id") == model
                and row.get("orchestration_attempt") == orchestration_attempt
                and row.get("integrity_session") == started[
                    "integrity_session"]
                and row.get("stage") == started["stage"]
                and row.get("journal_state") == "abandoned"
            )]
            if matching:
                if len(matching) != 1:
                    raise ValueError("duplicate invocation abandonment record")
                abandoned.append(matching[0])
                continue
            abandoned.append(self._append_invocation_row(
                stage, plan, entry, model, orchestration_attempt,
                execution_id=started["execution_id"],
                integrity_session=started["integrity_session"],
                result_stage=started["stage"],
                request_sha256=started["request_sha256"],
                descriptor_sha256=started["transport_descriptor_sha256"],
                journal_state="abandoned",
                reason="orchestrator_resume_after_interruption",
            ))
        return abandoned

    def _start_or_resume(self, stage, plan, entry, model):
        events = self._state_events(stage, plan)
        if self._is_settled(events, entry["occurrence_id"], model):
            return None
        latest = self._latest_state(events, entry["occurrence_id"], model)
        if latest is None:
            self._append_state(
                stage, plan, entry, model,
                session_attempt=1, attempt=1, state="started",
            )
            return 1
        if latest["state"] == "invalidated" and latest["session_attempt"] == 1:
            self._append_state(
                stage, plan, entry, model,
                session_attempt=2, attempt=1, state="started",
            )
            return 1
        if latest["state"] == "started":
            if latest["attempt"] >= 3:
                raise ValueError("crash resume exceeded two retries")
            self._abandon_open_invocation(
                stage, plan, entry, model, latest["attempt"]
            )
            self._append_state(
                stage, plan, entry, model,
                session_attempt=latest["session_attempt"],
                attempt=latest["attempt"], state="retry",
            )
            self._append_state(
                stage, plan, entry, model,
                session_attempt=latest["session_attempt"],
                attempt=latest["attempt"] + 1, state="started",
            )
            return latest["attempt"] + 1
        if latest["state"] == "retry":
            self._append_state(
                stage, plan, entry, model,
                session_attempt=latest["session_attempt"],
                attempt=latest["attempt"] + 1, state="started",
            )
            return latest["attempt"] + 1
        raise ValueError("run state is terminal but not settled")

    def _expected_configuration(self, model):
        row = next(
            item for item in manifest.load_panel()["models"]
            if item["logical_model_id"] == model
        )
        return row["providers"][self.provider]["configuration_id"]

    def _call_driver(
            self, episode, model, *, before_stage=None, stage_sink=None):
        if self.run_mode == "mock":
            return self._driver.run_episode(
                episode, logical_model_id=model, provider=self.provider,
                before_stage=before_stage, stage_sink=stage_sink,
            )
        if self.provider == "codex":
            if self._live_codex is None:
                self._live_codex = codex_driver.CodexDriver(run_mode="codex")
            return self._live_codex.run_episode(
                episode,
                logical_model_id=model,
                allow_integrity_rerun=True,
                before_stage=before_stage,
                stage_sink=stage_sink,
            )
        api_key = os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY is required out of band")
        return openrouter_driver.run_live_episode(
            episode, logical_model_id=model, api_key=api_key,
            before_stage=before_stage, stage_sink=stage_sink,
        )

    @staticmethod
    def _session_status(results):
        if not results:
            return "failed"
        final = results[-1]["terminal_status"]
        if final in {"invalidated", "failed"}:
            return final
        if len(results) != 4:
            return "failed"
        return (
            "complete"
            if all(row["terminal_status"] == "complete" for row in results)
            else "unresolved"
        )

    def _normalize_run(self, run):
        if hasattr(run, "attempts"):
            sessions = []
            for index, attempt in enumerate(run.attempts, 1):
                sessions.append({
                    "integrity_session": index,
                    "execution_id": attempt.execution_id,
                    "status": self._session_status(attempt.results),
                    "requests": attempt.requests,
                    "results": attempt.results,
                    "transport_descriptors": attempt.transport_descriptors,
                    "attestations": attempt.attestations,
                    "chain": attempt.chain,
                })
            provenance = (
                sessions[-1]["results"][-1]["provenance"]
                if sessions and sessions[-1]["results"] else self.provenance
            )
        elif type(run) is dict and type(run.get("sessions")) is list:
            sessions = deepcopy(run["sessions"])
            provenance = run.get("provenance")
            for session in sessions:
                session.setdefault(
                    "attestations", [None] * len(session.get("results", []))
                )
                session.setdefault("chain", None)
        else:
            raise ValueError("panel driver returned unsupported episode evidence")
        failure_attempt_provenance = (
            self.provider == "openrouter"
            and self.run_mode == "live"
            and provenance == openrouter_driver.LIVE_ATTEMPT_PROVENANCE
            and all(session.get("status") == "failed" for session in sessions)
        )
        if not sessions or (
                provenance != self.provenance and not failure_attempt_provenance):
            raise ValueError("driver provenance differs from orchestration mode")
        if len(sessions) > 2:
            raise ValueError("driver exceeded one integrity rerun")
        for index, session in enumerate(sessions, 1):
            if session.get("integrity_session", index) != index:
                raise ValueError("driver integrity session order is not exact")
            requests = session.get("requests")
            results = session.get("results")
            descriptors = session.get("transport_descriptors")
            attestations = session.get("attestations")
            failure_record = session.get("failure_record")
            if failure_record is not None:
                if (
                    session.get("status") != "failed"
                    or type(failure_record) is not dict
                    or failure_record.get("provenance") != provenance
                    or any(type(value) is not list for value in (
                        requests, results, descriptors, attestations
                    ))
                    or len(descriptors) != len(results)
                    or len(attestations) != len(results)
                    or len(requests) not in {
                        len(results), len(results) + 1,
                    }
                ):
                    raise ValueError("driver failure-attempt evidence is inconsistent")
                if requests:
                    failed_request = contracts.validate_stage_request(
                        requests[-1]
                    )
                    if (
                        len(requests) != len(results) + 1
                        or failure_record.get("request_sha256")
                        != failed_request["request_sha256"]
                        or failure_record.get("transport_request_sha256")
                        is None
                    ):
                        raise ValueError(
                            "driver failure-attempt request binding differs"
                        )
                _assert_no_credentials(failure_record)
                continue
            lengths = {len(value) for value in (
                requests, results, descriptors, attestations
            ) if type(value) is list}
            if any(type(value) is not list for value in (
                    requests, results, descriptors, attestations)) or len(lengths) != 1:
                raise ValueError("driver session evidence list lengths differ")
            if results and session.get("status") != self._session_status(results):
                raise ValueError("driver session status differs from results")
        return sessions

    def _evidence_path(
            self, stage, occurrence_id, model, orchestration_attempt,
            session_attempt, result_stage):
        return self._out_path(
            "evidence", stage, occurrence_id, model,
            f"orchestration-{orchestration_attempt}",
            f"session-{session_attempt}", f"{result_stage}.json",
        )

    def _validate_evidence(
            self, payload, *, plan, entry, model, orchestration_attempt,
            session_attempt, expected_stage=None):
        if type(payload) is not dict or set(payload) != set(EVIDENCE_KEYS):
            raise ValueError("stage evidence schema keys are not exact")
        if payload["evidence_version"] != EVIDENCE_VERSION:
            raise ValueError("stage evidence version mismatch")
        if payload["evidence_sha256"] != _canonical_sha(
                _without_hash(payload, "evidence_sha256")):
            raise ValueError("stage evidence artifact hash mismatch")
        bound = {
            "provenance": self.provenance,
            "provider": self.provider,
            "plan_hash": plan["plan_hash"],
            "plan_occurrence_id": entry["occurrence_id"],
            "item_id": entry["item_id"],
            "logical_model_id": model,
            "configuration_id": self._expected_configuration(model),
            "orchestration_attempt": orchestration_attempt,
            "session_attempt": session_attempt,
        }
        for field, value in bound.items():
            if payload[field] != value:
                raise ValueError(f"stage evidence {field} binding mismatch")
        if expected_stage is not None and payload["stage"] != expected_stage:
            raise ValueError("stage evidence stage binding mismatch")
        request = contracts.validate_stage_request(payload["request"])
        result = contracts.validate_stage_result(payload["result"], request)
        if request["stage"] != payload["stage"] or result["stage"] != payload[
                "stage"]:
            raise ValueError("stage evidence request/result stage mismatch")
        if request["provider"] != self.provider or request[
                "logical_model_id"] != model:
            raise ValueError("stage evidence request identity mismatch")
        descriptor_hash = _canonical_sha(payload["transport_descriptor"])
        if descriptor_hash != result["transport_request_sha256"]:
            raise ValueError("stage evidence transport descriptor hash mismatch")
        if result["provenance"] != self.provenance:
            raise ValueError("stage evidence result provenance mismatch")
        _assert_no_credentials(payload)
        return payload

    def _append_ledger(self, stage, event, plan):
        if type(event) is not dict or set(event) != set(LEDGER_KEYS):
            raise ValueError("stage-attempt ledger event keys are not exact")
        if stage not in self._ledger_cache:
            self._ledger_cache[stage] = _read_jsonl(self._ledger_path(stage))
        rows = self._ledger_cache[stage]
        ids = {row.get("event_id") for row in rows}
        composite = {
            (
                row.get("plan_occurrence_id"), row.get("logical_model_id"),
                row.get("orchestration_attempt"), row.get("session_attempt"),
                row.get("stage"),
                row.get("transport_attempt"),
            ) for row in rows
        }
        key = (
            event["plan_occurrence_id"], event["logical_model_id"],
            event["orchestration_attempt"], event["session_attempt"],
            event["stage"],
            event["transport_attempt"],
        )
        if event["event_id"] in ids or key in composite:
            matching = [row for row in rows if row.get("event_id") == event[
                "event_id"] or (
                    row.get("plan_occurrence_id"), row.get("logical_model_id"),
                    row.get("orchestration_attempt"),
                    row.get("session_attempt"), row.get("stage"),
                    row.get("transport_attempt"),
                ) == key]
            if matching == [event]:
                return
            raise ValueError("duplicate or conflicting stage-attempt ledger event")
        _append_jsonl(self._ledger_path(stage), event)
        rows.append(event)

    def _persist_stage_event(
            self, stage, plan, entry, model, orchestration_attempt, event):
        if type(event) is not dict or set(event) != {
                "provider", "integrity_session", "execution_id", "stage",
                "request", "transport_descriptor", "attestation", "result"}:
            raise ValueError("provider stage-sink event keys are not exact")
        request = contracts.validate_stage_request(event["request"])
        result = contracts.validate_stage_result(event["result"], request)
        session_attempt = event["integrity_session"]
        if (
            event["provider"] != self.provider
            or session_attempt not in {1, 2}
            or event["execution_id"] != request["execution_id"]
            or event["stage"] != request["stage"]
            or request["provider"] != self.provider
            or request["logical_model_id"] != model
            or request["configuration_id"] != self._expected_configuration(model)
        ):
            raise ValueError("provider stage-sink event binding mismatch")
        payload = {
            "evidence_version": EVIDENCE_VERSION,
            "provenance": self.provenance,
            "provider": self.provider,
            "plan_hash": plan["plan_hash"],
            "plan_occurrence_id": entry["occurrence_id"],
            "item_id": entry["item_id"],
            "logical_model_id": model,
            "configuration_id": self._expected_configuration(model),
            "orchestration_attempt": orchestration_attempt,
            "session_attempt": session_attempt,
            "stage": request["stage"],
            "request": request,
            "result": result,
            "transport_descriptor": deepcopy(event["transport_descriptor"]),
            "attestation": deepcopy(event["attestation"]),
        }
        payload["evidence_sha256"] = _canonical_sha(payload)
        self._validate_evidence(
            payload, plan=plan, entry=entry, model=model,
            orchestration_attempt=orchestration_attempt,
            session_attempt=session_attempt, expected_stage=request["stage"],
        )
        starts = [row for row in _read_jsonl(
            self._invocation_path(stage)
        ) if (
            row.get("journal_state") == "started"
            and row.get("plan_occurrence_id") == entry["occurrence_id"]
            and row.get("logical_model_id") == model
            and row.get("orchestration_attempt") == orchestration_attempt
            and row.get("integrity_session") == session_attempt
            and row.get("stage") == request["stage"]
            and row.get("execution_id") == request["execution_id"]
            and row.get("request_sha256") == request["request_sha256"]
            and row.get("transport_descriptor_sha256")
            == result["transport_request_sha256"]
        )]
        if len(starts) != 1:
            raise ValueError(
                "stage evidence requires exactly one journaled invocation"
            )
        path = self._evidence_path(
            stage, entry["occurrence_id"], model, orchestration_attempt,
            session_attempt, request["stage"],
        )
        if path.exists():
            observed = _read_json(path)
            if observed != payload:
                raise ValueError("immutable stage evidence differs on replay")
            payload = observed
        else:
            _write_new_json(path, payload)
        relative = path.relative_to(self.out_dir).as_posix()
        if stage not in self._ledger_cache:
            self._ledger_cache[stage] = _read_jsonl(self._ledger_path(stage))
        for attempt in result["attempts"]:
            event_core = {
                "ledger_version": LEDGER_VERSION,
                "provenance": self.provenance,
                "provider": self.provider,
                "plan_hash": plan["plan_hash"],
                "plan_occurrence_id": entry["occurrence_id"],
                "item_id": entry["item_id"],
                "logical_model_id": model,
                "configuration_id": result["configuration_id"],
                "orchestration_attempt": orchestration_attempt,
                "session_attempt": session_attempt,
                "stage": result["stage"],
                "session_id": result["session_id"],
                "transport_attempt": attempt["attempt_index"],
                "attempt_started_at_utc": attempt["started_at_utc"],
                "attempt_completed_at_utc": attempt["completed_at_utc"],
                "request_sha256": request["request_sha256"],
                "result_sha256": result["result_sha256"],
                "transport_request_sha256": result[
                    "transport_request_sha256"
                ],
                "raw_trace_sha256": attempt["raw_trace_sha256"],
                "artifact_relative_path": relative,
                "artifact_sha256": payload["evidence_sha256"],
                "stage_terminal_status": result["terminal_status"],
                "format_repair_count": 0,
                "state": "persisted",
            }
            matching = [row for row in self._ledger_cache[stage] if (
                row.get("plan_occurrence_id") == entry["occurrence_id"]
                and row.get("logical_model_id") == model
                and row.get("orchestration_attempt")
                == orchestration_attempt
                and row.get("session_attempt") == session_attempt
                and row.get("stage") == result["stage"]
                and row.get("transport_attempt")
                == attempt["attempt_index"]
            )]
            if matching:
                if len(matching) == 1 and all(
                        matching[0].get(field) == value
                        for field, value in event_core.items()):
                    continue
                raise ValueError(
                    "conflicting persisted stage-attempt ledger event"
                )
            event_without_id = {
                **event_core,
                "persisted_at_utc": self._now(),
            }
            ledger_event = {
                "event_id": "ledger-" + _canonical_sha(event_without_id),
                **event_without_id,
            }
            self._append_ledger(stage, ledger_event, plan)
        return payload

    def _persist_session(
            self, stage, plan, entry, model, session, session_attempt,
            orchestration_attempt):
        requests = session["requests"]
        results = session["results"]
        descriptors = session["transport_descriptors"]
        attestations = session["attestations"]
        artifacts = []
        for request, result, descriptor, attestation in zip(
                requests, results, descriptors, attestations):
            artifacts.append(self._persist_stage_event(
                stage, plan, entry, model, orchestration_attempt, {
                    "provider": self.provider,
                    "integrity_session": session_attempt,
                    "execution_id": request["execution_id"],
                    "stage": request["stage"],
                    "request": request,
                    "transport_descriptor": descriptor,
                    "attestation": attestation,
                    "result": result,
                }
            ))
        return artifacts

    def _append_judge_queue(self, stage, score, artifact_by_stage):
        unresolved_stages = [
            name for name, artifact in artifact_by_stage.items()
            if artifact["result"]["attempts"][-1]["parsed_response"] is None
        ]
        for result_stage in unresolved_stages:
            artifact = artifact_by_stage[result_stage]
            result = artifact["result"]
            attempt = result["attempts"][-1]
            artifact_path = self._evidence_path(
                stage,
                score["plan_occurrence_id"],
                score["logical_model_id"],
                artifact["orchestration_attempt"],
                artifact["session_attempt"],
                result_stage,
            )
            payload = {
                "queue_version": QUEUE_VERSION,
                "provenance": self.provenance,
                "provider": self.provider,
                "logical_model_id": score["logical_model_id"],
                "configuration_id": score["configuration_id"],
                "judge_case_id": self._judge_by_item[score["item_id"]],
                "stage": result_stage,
                "response_artifact_relative_path": artifact_path.relative_to(
                    self.out_dir
                ).as_posix(),
                "response_artifact_sha256": artifact["evidence_sha256"],
                "raw_final_message_sha256": attempt[
                    "raw_final_message_sha256"
                ],
                "reason": "unresolved_canonical_response",
                "queued_at_utc": self._now(),
            }
            payload["queue_event_id"] = "queue-" + _canonical_sha(payload)
            payload["queue_sha256"] = _canonical_sha(payload)
            queue_path = self._out_path("judge_queue", f"{stage}.jsonl")
            rows = _read_jsonl(queue_path)
            ids = {row.get("queue_event_id") for row in rows}
            if payload["queue_event_id"] in ids:
                if [row for row in rows if row.get("queue_event_id") == payload[
                        "queue_event_id"]] == [payload]:
                    continue
                raise ValueError("duplicate conflicting unresolved judge queue event")
            _append_jsonl(queue_path, payload)

    def _calibration_link(self, item_id, model):
        root = self._out_path("scores", "calibration")
        if not root.exists():
            raise ValueError("reliability requires completed calibration scores")
        if self._calibration_score_index is None:
            index = {}
            for path in self._artifact_files("scores", "calibration"):
                row = self._validate_score(_read_json(path))
                key = (row["item_id"], row["logical_model_id"])
                if key in index:
                    raise ValueError("duplicate calibration score linkage")
                index[key] = row
            self._calibration_score_index = index
        matches = [self._calibration_score_index[(item_id, model)]] \
            if (item_id, model) in self._calibration_score_index else []
        if len(matches) != 1:
            raise ValueError(
                "reliability item must link to exactly one calibration score"
            )
        return {
            "calibration_occurrence_id": matches[0]["plan_occurrence_id"],
            "calibration_score_sha256": matches[0]["score_sha256"],
        }

    def _build_score(self, stage, plan, entry, model, session_status,
                     artifacts):
        hidden = self.sidecar[entry["item_id"]]
        episode = self._by_id[entry["item_id"]]
        by_stage = {artifact["stage"]: artifact for artifact in artifacts}
        results = [by_stage[name]["result"] for name in contracts.STAGES
                   if name in by_stage]
        final_attempts = {
            name: artifact["result"]["attempts"][-1]
            for name, artifact in by_stage.items()
        }
        unresolved_stages = [
            name for name, attempt in final_attempts.items()
            if attempt["parsed_response"] is None
        ]
        stage4 = action_scale.score_response(
            final_attempts["stage_4"]["raw_final_message"]
        ) if "stage_4" in final_attempts else action_scale.score_response("")
        stage3 = None
        if "stage_2" in final_attempts and "stage_3" in final_attempts:
            stage3 = stage3_update.score_update(
                final_attempts["stage_2"]["raw_final_message"],
                final_attempts["stage_3"]["raw_final_message"],
                hidden["true_type"],
                hidden["cue_variant"],
                hidden["expected_stage3"],
            )
        violations = sorted({
            value for result in results
            for value in result["integrity"]["violations"]
        })
        errors = sorted({
            attempt["error_code"] for attempt in final_attempts.values()
            if attempt["error_code"] is not None
        })
        terminal_invalidated = (
            session_status in {"invalidated", "failed"}
            or len(results) != 4
            or any(result["terminal_status"] in {"invalidated", "failed"}
                   for result in results)
        )
        invalidation_reason = None
        if terminal_invalidated:
            invalidation_reason = "|".join(violations + errors) or session_status
        mechanically_resolved = (
            len(results) == 4
            and not terminal_invalidated
            and not unresolved_stages
            and stage4["mechanical_flag"] is False
            and stage3 is not None
            and stage3["mechanical_flag"] is False
        )
        score = {
            "score_version": SCORE_VERSION,
            "provenance": self.provenance,
            "provider": self.provider,
            "plan_hash": plan["plan_hash"],
            "plan_occurrence_id": entry["occurrence_id"],
            "sample_cell_id": entry["occurrence_id"],
            "item_id": entry["item_id"],
            "logical_model_id": model,
            "configuration_id": self._expected_configuration(model),
            "split": episode["split"],
            "family": episode["template_family"],
            "pair_id": hidden["pair_id"],
            "true_type": hidden["true_type"],
            "label": hidden["label"],
            "cue_variant": hidden["cue_variant"],
            "base_rate_benign": hidden["base_rate_benign"],
            "indistinguishable_control": hidden[
                "indistinguishable_control"
            ],
            "transcript_hash": _canonical_sha(episode["multiturn_script"]),
            "stage_count": len(results),
            "stage_terminal_statuses": {
                result["stage"]: result["terminal_status"] for result in results
            },
            "transport_retry_count": sum(
                result["transport_retry_count"] for result in results
            ),
            "format_repair_count": 0,
            "format_repair_flagged": False,
            "semantic_response_replaced": False,
            "tool_calls": [
                event for result in results for event in result["tool_events"]
            ],
            "future_text_seen": any(
                not result["integrity"]["future_text_absent"]
                for result in results
            ),
            "thread_chain_ok": all(
                result["integrity"]["session_chain_ok"] for result in results
            ),
            "terminal_invalidated": terminal_invalidated,
            "invalidation_reason": invalidation_reason,
            "unresolved": bool(unresolved_stages),
            "judge_queued": bool(unresolved_stages),
            "mechanically_resolved": mechanically_resolved,
            "stage4_score": stage4["score"],
            "stage4_intent_score": stage4["intent_score"],
            "stage4_decision": (
                stage4["grade"].upper() if stage4["grade"] else None
            ),
            "stage4_intent": (
                stage4["intent"].upper() if stage4["intent"] else None
            ),
            "stage3_update_correct": (
                stage3["update_correct"] if stage3 is not None else None
            ),
            "stage3_detail": deepcopy(stage3),
            "evidence_sha256s": [
                artifact["evidence_sha256"] for artifact in artifacts
            ],
            "reliability_primary_link": (
                self._calibration_link(entry["item_id"], model)
                if stage == "reliability" else None
            ),
        }
        score["score_sha256"] = _canonical_sha(score)
        return self._validate_score(score)

    def _validate_score(self, score):
        if type(score) is not dict or set(score) != set(SCORE_KEYS):
            raise ValueError("mechanical score schema keys are not exact")
        if score["score_version"] != SCORE_VERSION:
            raise ValueError("mechanical score version mismatch")
        if score["score_sha256"] != _canonical_sha(
                _without_hash(score, "score_sha256")):
            raise ValueError("mechanical score hash mismatch")
        if score["provenance"] != self.provenance or score[
                "provider"] != self.provider:
            raise ValueError("mechanical score provenance mismatch")
        if score["format_repair_count"] != 0 or score[
                "format_repair_flagged"] is not False:
            raise ValueError("format repairs are forbidden")
        _assert_no_credentials(score)
        return score

    def _score_path(self, stage, occurrence_id, model):
        return self._out_path(
            "scores", stage, occurrence_id, f"{model}.json"
        )

    def _persist_final_score(self, stage, plan, entry, model,
                             session_status, artifacts):
        score = self._build_score(
            stage, plan, entry, model, session_status, artifacts
        )
        _write_or_validate(
            self._score_path(stage, entry["occurrence_id"], model), score
        )
        self._append_judge_queue(
            stage, score, {artifact["stage"]: artifact for artifact in artifacts}
        )
        return score

    def _terminal_state(self, sessions, index):
        status = sessions[index]["status"]
        if status in {"complete", "unresolved"}:
            return "complete"
        if status == "failed":
            return "failed"
        if status == "invalidated":
            if index < len(sessions) - 1 or index == 1:
                return "invalidated"
            # A single non-rerunnable invalidation settles the high-level arm.
            return "failed"
        raise ValueError("driver returned unknown session status")

    def _persist_failure_record(
            self, stage, plan, entry, model, orchestration_attempt,
            session_attempt, session):
        failure = deepcopy(session["failure_record"])
        if not session.get("requests"):
            raise ValueError("failure attempt is missing its failed request")
        failed_request = contracts.validate_stage_request(
            session["requests"][-1]
        )
        if (
            failed_request["request_sha256"]
            != failure.get("request_sha256")
            or failed_request["execution_id"] != session["execution_id"]
            or failure.get("transport_request_sha256") is None
        ):
            raise ValueError("failure attempt request/transport binding differs")
        payload = {
            "failure_artifact_version": "charitroc-panel-failure-attempt-v1",
            "provenance": failure["provenance"],
            "provider": self.provider,
            "plan_hash": plan["plan_hash"],
            "plan_occurrence_id": entry["occurrence_id"],
            "item_id": entry["item_id"],
            "logical_model_id": model,
            "configuration_id": self._expected_configuration(model),
            "orchestration_attempt": orchestration_attempt,
            "integrity_session": session_attempt,
            "execution_id": session["execution_id"],
            "stage": failed_request["stage"],
            "failed_request": failed_request,
            "failure_record": failure,
        }
        payload["failure_artifact_sha256"] = _canonical_sha(payload)
        _assert_no_credentials(payload)
        path = self._out_path(
            "failures", stage, entry["occurrence_id"], model,
            f"orchestration-{orchestration_attempt}",
            f"session-{session_attempt}.json",
        )
        _write_or_validate(path, payload)
        return payload

    def _persist_run(self, stage, plan, entry, model, run, high_attempt):
        sessions = self._normalize_run(run)
        final_artifacts = None
        final_status = None
        for index, session in enumerate(sessions):
            session_number = index + 1
            if index > 0:
                self._append_state(
                    stage, plan, entry, model,
                    session_attempt=session_number, attempt=1, state="started",
                )
            if session.get("failure_record") is not None:
                self._persist_failure_record(
                    stage, plan, entry, model, high_attempt,
                    session_number, session,
                )
            artifacts = self._persist_session(
                stage, plan, entry, model, session, session_number,
                high_attempt,
            )
            terminal = self._terminal_state(sessions, index)
            if index == len(sessions) - 1:
                final_artifacts = artifacts
                final_status = session["status"]
                self._persist_final_score(
                    stage, plan, entry, model, final_status, final_artifacts
                )
            self._append_state(
                stage, plan, entry, model,
                session_attempt=session_number,
                attempt=(high_attempt if index == 0 else 1),
                state=terminal,
            )
        return final_status

    def _default_freeze_builder(self, **kwargs):
        return manifest.build_freeze(**kwargs)

    def _default_private_validator(self, freeze, **kwargs):
        kwargs.pop("item_id", None)
        return manifest.validate_private_launch(freeze, **kwargs)

    def _runtime_args(self):
        path = self.codex_cli_path or shutil.which("codex")
        if not path:
            raise ValueError("Codex CLI is required for the private freeze")
        return path, self.codex_cli_version

    def _validate_calibration_analysis_record(self, report):
        expected_keys = {
            "analysis_version", "provenance", "provider", "bootstrap_draws",
            "channels_reported_separately", "harness", "summary",
            "model_reports", "family_rows", "operating_point_rows",
            "repeats", "ambiguity_controls",
            "ambiguity_control_sensitivity", "gate_report",
            "analysis_sha256",
        }
        if type(report) is not dict or set(report) != expected_keys:
            raise ValueError("calibration analysis schema is not exact")
        if (
            report["analysis_version"] != ANALYSIS_VERSION
            or report["provenance"] != self.provenance
            or report["provider"] != self.provider
            or report["bootstrap_draws"] != self.bootstrap_draws
            or report["channels_reported_separately"] is not True
            or report["analysis_sha256"] != _canonical_sha(
                _without_hash(report, "analysis_sha256")
            )
            or type(report["summary"]) is not dict
            or set(report["summary"].get("models", {}))
            != set(manifest.MODEL_LOGICAL_IDS)
        ):
            raise ValueError("calibration analysis hash/identity is not valid")
        harness = report["harness"]
        gate = report["gate_report"]
        ambiguity = report["ambiguity_controls"]
        models = report["summary"]["models"]
        family_sets = []
        for model in manifest.MODEL_LOGICAL_IDS:
            row = models[model]
            family_auc = row.get("family_auc") if type(row) is dict else None
            if (
                type(family_auc) is not dict
                or len(family_auc) != gates.EXPECTED_FAMILY_COUNT
                or any(
                    type(value) not in {int, float}
                    or type(value) is bool
                    or not 0.0 <= value <= 1.0
                    for value in family_auc.values()
                )
            ):
                raise ValueError(
                    "calibration analysis family AUC coverage is not valid"
                )
            family_sets.append(set(family_auc))
        if any(families != family_sets[0] for families in family_sets[1:]):
            raise ValueError(
                "calibration analysis family AUC coverage differs by model"
            )

        saturation = gate.get("saturation") if type(gate) is dict else None
        hardening = (
            saturation.get("family_hardening_triggers")
            if type(saturation) is dict else None
        )
        hardening_keys = {
            "triggered", "all_models_auc_ceiling_trigger",
            "same_terminal_decision_trigger",
            "same_terminal_decision_rate",
        }
        if type(hardening) is not dict or set(hardening) != family_sets[0]:
            raise ValueError(
                "calibration analysis family hardening coverage is not valid"
            )
        for family, row in hardening.items():
            if type(row) is not dict or set(row) != hardening_keys:
                raise ValueError(
                    "calibration analysis family hardening schema is not exact"
                )
            rate = row["same_terminal_decision_rate"]
            if (
                type(row["triggered"]) is not bool
                or type(row["all_models_auc_ceiling_trigger"]) is not bool
                or type(row["same_terminal_decision_trigger"]) is not bool
                or type(rate) not in {int, float}
                or type(rate) is bool
                or not 0.0 <= rate <= 1.0
            ):
                raise ValueError(
                    "calibration analysis family hardening values are not valid"
                )
            auc_trigger = all(
                models[model]["family_auc"][family]
                >= gates.SATURATION_AUC
                for model in manifest.MODEL_LOGICAL_IDS
            )
            decision_trigger = rate >= gates.FAMILY_SAME_DECISION_RATE
            if (
                row["all_models_auc_ceiling_trigger"] is not auc_trigger
                or row["same_terminal_decision_trigger"]
                is not decision_trigger
                or row["triggered"] is not (
                    auc_trigger or decision_trigger
                )
            ):
                raise ValueError(
                    "calibration analysis family hardening claims differ"
                )
            if row["triggered"]:
                raise ValueError(
                    "calibration analysis family hardening gate did not pass"
                )
        if (
            type(harness) is not dict
            or harness.get("passed") is not True
            or harness.get("sample_cells_complete") is not True
            or harness.get("measurement_ready") is not True
            or type(gate) is not dict
            or gate.get("measurement_ready") is not True
            or gate.get("channels_reported_separately") is not True
            or gate.get("saturation", {}).get("evaluated") is not True
            or gate.get("saturation", {}).get("failed") is not False
            or gate.get("noninformative", {}).get("evaluated") is not True
            or gate.get("noninformative", {}).get("failed") is not False
            or gate.get("discrimination", {}).get("evaluated") is not True
            or gate.get("discrimination", {}).get("passed") is not True
            or type(ambiguity) is not dict
            or ambiguity.get("passed") is not True
        ):
            raise ValueError("calibration analysis gate did not pass")
        _assert_no_credentials(report)
        return report

    def _private_protocol_payload(self, freeze, plans):
        calibration_path = self._out_path(
            "reports", "calibration-analysis.json"
        )
        if self.run_mode == "live" and not calibration_path.is_file():
            raise ValueError(
                "production private freeze requires frozen calibration analysis"
            )
        if calibration_path.is_file():
            self._validate_calibration_analysis_record(
                _read_json(calibration_path)
            )
            calibration_hash = hashlib.sha256(
                calibration_path.read_bytes()
            ).hexdigest()
        else:
            calibration_hash = None
        payload = {
            "protocol_freeze_version": "charitroc-private-protocol-v1",
            "construction_freeze_hash": freeze["freeze_hash"],
            "calibration_analysis_file_sha256": calibration_hash,
            "confirmation_criteria": [
                deepcopy(row) for row in PRIVATE_CRITERIA_TEMPLATES
            ],
            "private_plan_hash": plans["private"]["plan_hash"],
            "extension_entries_sha256": _canonical_sha(
                plans["private"]["extension_entries"]
            ),
        }
        payload["protocol_freeze_sha256"] = _canonical_sha(payload)
        return payload

    def _write_private_protocol_freeze(self, freeze, plans):
        payload = self._private_protocol_payload(freeze, plans)
        path = self._out_path("private-protocol-freeze.json")
        _write_or_validate(path, payload)
        return payload

    def _validate_private_protocol(self, freeze):
        path = self._out_path("private-protocol-freeze.json")
        if not path.is_file():
            raise ValueError("private protocol freeze is unavailable")
        observed = _read_json(path)
        expected = self._private_protocol_payload(freeze, self._all_plans())
        if observed != expected:
            raise ValueError("private protocol/calibration freeze has changed")
        return observed

    def freeze(self):
        private_roots = (
            self._out_path("state", "private.jsonl"),
            self._out_path("evidence", "private"),
            self._out_path("scores", "private"),
            self._out_path("state", "private-extension.jsonl"),
            self._out_path("evidence", "private-extension"),
            self._out_path("scores", "private-extension"),
        )
        if any(path.exists() for path in private_roots):
            raise ValueError("freeze must precede every private response artifact")
        calibration_path = self._out_path(
            "reports", "calibration-analysis.json"
        )
        if self.run_mode == "live":
            self._validate_calibration_analysis_record(self.analyze())
        elif calibration_path.is_file():
            self._validate_calibration_analysis_record(
                _read_json(calibration_path)
            )
        plans = self._all_plans()
        cli_path, cli_version = (
            (self.codex_cli_path, self.codex_cli_version)
            if self._freeze_builder_injected else self._runtime_args()
        )
        freeze = self._freeze_builder(
            bank_root=self.bank_root,
            sample_manifests=plans,
            episodes=self.episodes,
            sidecar=self.sidecar,
            codex_cli_path=cli_path,
            codex_cli_version=cli_version,
        )
        if type(freeze) is not dict or type(freeze.get("freeze_hash")) is not str:
            raise ValueError("freeze builder returned an invalid record")
        _assert_no_credentials(freeze)
        path = self._out_path("freeze.json")
        if path.exists():
            if _read_json(path) != freeze:
                raise ValueError("existing private freeze differs from construction")
            self._write_private_protocol_freeze(freeze, plans)
            return freeze
        _write_new_json(path, freeze)
        self._write_private_protocol_freeze(freeze, plans)
        return freeze

    def _validate_private_call(self, freeze, item_id):
        self._validate_private_protocol(freeze)
        plans = self._all_plans()
        cli_path, cli_version = (
            (self.codex_cli_path, self.codex_cli_version)
            if self._private_validator_injected else self._runtime_args()
        )
        result = self._private_validator(
            freeze,
            bank_root=self.bank_root,
            sample_manifests=plans,
            episodes=self.episodes,
            sidecar=self.sidecar,
            codex_cli_path=cli_path,
            codex_cli_version=cli_version,
            item_id=item_id,
        )
        if type(result) is not dict or result.get("valid") is not True:
            raise ValueError("private freeze validation did not pass")
        return result

    def _stage_callbacks(
            self, stage, plan, entry, model, orchestration_attempt, freeze):
        def before_stage(event):
            self._journal_stage_start(
                stage, plan, entry, model, orchestration_attempt, event
            )
            if stage in {"private", "private-extension"}:
                self._validate_private_call(freeze, entry["item_id"])

        def stage_sink(event):
            return self._persist_stage_event(
                stage, plan, entry, model, orchestration_attempt, event
            )

        return before_stage, stage_sink

    def _execution_entries(self, stage, plan):
        if stage in RUN_STAGES:
            return plan["entries"]
        if stage != "private-extension":
            raise ValueError("execution namespace is not recognized")
        activation_path = self._out_path(
            "reports", "private-extension-activation.json"
        )
        if not activation_path.is_file():
            raise ValueError("private extension requires one-time activation")
        activation = _read_json(activation_path)
        primary_analysis = _read_json(self._out_path(
            "reports", "private-analysis-96.json"
        ))
        freeze = _read_json(self._out_path("freeze.json"))
        protocol = self._validate_private_protocol(freeze)
        expected_occurrences = [
            row["occurrence_id"] for row in plan["extension_entries"]
        ]
        if (
            type(activation) is not dict
            or set(activation) != {
                "activation_version", "namespace", "provenance", "provider",
                "analysis_sha256", "freeze_hash",
                "private_protocol_freeze_sha256",
                "calibration_analysis_file_sha256", "private_plan_hash",
                "extension_entries_sha256", "extension_occurrence_ids",
                "activated_at_utc", "activation_sha256",
            }
            or activation.get("activation_version")
            != "charitroc-private-extension-activation-v1"
            or activation.get("activation_sha256") != _canonical_sha(
                _without_hash(activation, "activation_sha256")
            )
            or activation.get("namespace") != "private-extension"
            or activation.get("provenance") != self.provenance
            or activation.get("provider") != self.provider
            or activation.get("analysis_sha256")
            != primary_analysis.get("analysis_sha256")
            or primary_analysis.get("analysis_sha256") != _canonical_sha(
                _without_hash(primary_analysis, "analysis_sha256")
            )
            or primary_analysis.get("provenance") != self.provenance
            or primary_analysis.get("provider") != self.provider
            or primary_analysis.get("private_confirmation", {}).get("action")
            != "extend_to_192"
            or primary_analysis.get("private_confirmation", {}).get(
                "extension_allowed") is not True
            or activation.get("freeze_hash") != freeze["freeze_hash"]
            or activation.get("private_protocol_freeze_sha256")
            != protocol["protocol_freeze_sha256"]
            or activation.get("calibration_analysis_file_sha256")
            != protocol["calibration_analysis_file_sha256"]
            or activation.get("private_plan_hash") != plan["plan_hash"]
            or activation.get("extension_entries_sha256")
            != _canonical_sha(plan["extension_entries"])
            or activation.get("extension_occurrence_ids")
            != expected_occurrences
        ):
            raise ValueError("private extension activation differs from plan")
        _parse_timestamp(activation["activated_at_utc"])
        return plan["extension_entries"]

    @staticmethod
    def _access_probe_turns():
        return {
            "stage_1": (
                "Model-access compatibility probe. No benchmark case is "
                "present. Return a brief reason and the canonical INTENT and "
                "DECISION fields; use UNCERTAIN and VERIFY."
            ),
            "stage_2": "Unused access-probe continuation two.",
            "stage_3": "Unused access-probe continuation three.",
            "stage_4": "Unused access-probe continuation four.",
        }

    def _access_journal_path(self):
        return self._out_path("access", "attempt-journal.jsonl")

    def _access_journal_events(self):
        events = _read_jsonl(self._access_journal_path())
        latest = {}
        model_order = list(manifest.MODEL_LOGICAL_IDS)
        previous_time = None
        for event_index, event in enumerate(events, 1):
            if (
                type(event) is not dict
                or set(event) != ACCESS_JOURNAL_KEYS
                or event.get("journal_version") != ACCESS_JOURNAL_VERSION
                or type(event.get("event_index")) is not int
                or event.get("event_index") != event_index
                or event.get("provenance") != ACCESS_PROVENANCE
                or event.get("provider") != self.provider
                or event.get("logical_model_id") not in model_order
                or event.get("configuration_id") != self._expected_configuration(
                    event.get("logical_model_id")
                )
                or event.get("state") not in ACCESS_JOURNAL_STATES
                or type(event.get("attempt_number")) is not int
                or not 1 <= event["attempt_number"] <= 3
                or event.get("event_sha256") != _canonical_sha(
                    _without_hash(event, "event_sha256")
                )
                or event.get("previous_event_sha256") != (
                    events[event_index - 2]["event_sha256"]
                    if event_index > 1 else None
                )
            ):
                raise ValueError("access attempt journal binding differs")
            for field in ("request_sha256", "transport_descriptor_sha256"):
                if type(event.get(field)) is not str or not _SHA256_RE.fullmatch(
                        event[field]):
                    raise ValueError("access attempt journal hash differs")
            timestamp = _parse_timestamp(event.get("timestamp_utc"))
            if previous_time is not None and timestamp < previous_time:
                raise ValueError("access attempt journal time moved backward")
            previous_time = timestamp
            model = event["logical_model_id"]
            model_index = model_order.index(model)
            prior = latest.get(model)
            if event["state"] == "started":
                if (
                    event["start_event_sha256"] is not None
                    or event["artifact_relative_path"] is not None
                    or event["artifact_sha256"] is not None
                    or event["terminal_kind"] is not None
                    or event["attempt_number"] != 1 + sum(
                        row["logical_model_id"] == model
                        and row["state"] == "started"
                        for row in events[:event_index - 1]
                    )
                    or (prior is not None and prior["state"] not in {
                        "failed", "abandoned",
                    })
                    or any(
                        latest.get(prior_model, {}).get("state") != "succeeded"
                        for prior_model in model_order[:model_index]
                    )
                    or any(later_model in latest
                           for later_model in model_order[model_index + 1:])
                ):
                    raise ValueError("access attempt journal start differs")
            else:
                if (
                    prior is None
                    or prior["state"] != "started"
                    or prior["attempt_number"] != event["attempt_number"]
                    or event["start_event_sha256"] != prior["event_sha256"]
                    or event["request_sha256"] != prior["request_sha256"]
                    or event["transport_descriptor_sha256"]
                    != prior["transport_descriptor_sha256"]
                ):
                    raise ValueError("access attempt journal terminal differs")
                if event["state"] == "abandoned":
                    if (
                        event["artifact_relative_path"] is not None
                        or event["artifact_sha256"] is not None
                        or event["terminal_kind"] != "pre_sink_interruption"
                    ):
                        raise ValueError("access abandonment journal differs")
                elif (
                    type(event["artifact_relative_path"]) is not str
                    or type(event["artifact_sha256"]) is not str
                    or not _SHA256_RE.fullmatch(event["artifact_sha256"])
                    or (
                        event["state"] == "succeeded"
                        and event["terminal_kind"] != "validated_probe"
                    )
                    or (
                        event["state"] == "failed"
                        and event["terminal_kind"] not in {
                            "provider_terminal_failure", "integrity_rejection",
                            "access_readiness_rejection",
                        }
                    )
                ):
                    raise ValueError("access terminal artifact journal differs")
            latest[model] = event
        _assert_no_credentials(events)
        return events

    def _append_access_journal(
            self, *, model, attempt_number, state, request_sha256,
            transport_descriptor_sha256, start_event=None,
            artifact_path=None, terminal_kind=None):
        events = self._access_journal_events()
        artifact_relative_path = None
        artifact_sha256 = None
        if artifact_path is not None:
            artifact_path = Path(artifact_path)
            artifact_relative_path = artifact_path.resolve().relative_to(
                self.out_dir
            ).as_posix()
            artifact_sha256 = hashlib.sha256(
                artifact_path.read_bytes()
            ).hexdigest()
        event = {
            "journal_version": ACCESS_JOURNAL_VERSION,
            "event_index": len(events) + 1,
            "provenance": ACCESS_PROVENANCE,
            "provider": self.provider,
            "logical_model_id": model,
            "configuration_id": self._expected_configuration(model),
            "attempt_number": attempt_number,
            "state": state,
            "request_sha256": request_sha256,
            "transport_descriptor_sha256": transport_descriptor_sha256,
            "start_event_sha256": (
                start_event["event_sha256"] if start_event is not None else None
            ),
            "artifact_relative_path": artifact_relative_path,
            "artifact_sha256": artifact_sha256,
            "terminal_kind": terminal_kind,
            "previous_event_sha256": (
                events[-1]["event_sha256"] if events else None
            ),
            "timestamp_utc": self._now(),
        }
        event["event_sha256"] = _canonical_sha(event)
        _append_jsonl(self._access_journal_path(), event)
        self._access_journal_events()
        return event

    @staticmethod
    def _access_model_events(events, model):
        return [row for row in events if row["logical_model_id"] == model]

    def _reconcile_access_orphans(self, events):
        """Close a start whose exact terminal artifact survived a crash."""
        for index, model in enumerate(manifest.MODEL_LOGICAL_IDS, 1):
            model_events = self._access_model_events(events, model)
            latest = model_events[-1] if model_events else None
            if latest is None or latest["state"] != "started":
                continue
            attempt_number = latest["attempt_number"]
            probe_path = self._out_path(
                "access", "probes", f"{model}.json"
            )
            failure_path = self._out_path(
                "access", "failures", model,
                f"attempt-{attempt_number:02d}.json",
            )
            candidates = [
                (kind, path) for kind, path in (
                    ("succeeded", probe_path), ("failed", failure_path),
                ) if path.is_file()
            ]
            if not candidates:
                continue
            if len(candidates) != 1:
                raise ValueError("ambiguous orphan access artifacts")
            state, artifact_path = candidates[0]
            if state == "succeeded":
                probe = _read_json(artifact_path)
                request, _result = self._validate_access_probe_evidence(
                    probe, index, model
                )
                self._validate_access_probe(probe, index, model)
                terminal_kind = "validated_probe"
            else:
                failure = _read_json(artifact_path)
                self._validate_access_failure(
                    failure, index, model, attempt_number
                )
                probe = failure["probe"]
                request = contracts.validate_stage_request(probe["request"])
                terminal_kind = failure["failure_kind"]
            if (
                request["request_sha256"] != latest["request_sha256"]
                or _canonical_sha(probe["transport_descriptor"])
                != latest["transport_descriptor_sha256"]
            ):
                raise ValueError("orphan access artifact differs from start")
            self._append_access_journal(
                model=model,
                attempt_number=attempt_number,
                state=state,
                request_sha256=latest["request_sha256"],
                transport_descriptor_sha256=latest[
                    "transport_descriptor_sha256"
                ],
                start_event=latest,
                artifact_path=artifact_path,
                terminal_kind=terminal_kind,
            )
            events = self._access_journal_events()
        return events

    def _validate_access_probe_evidence(self, probe, index, model):
        if (
            type(probe) is not dict
            or set(probe) != {
                "probe_id", "provenance", "logical_model_id", "configuration_id",
                "request", "result", "transport_descriptor", "attestation",
            }
            or probe.get("provenance") != ACCESS_PROVENANCE
            or probe.get("logical_model_id") != model
            or probe.get("probe_id") != f"ACCESS-PROBE-{index:02d}-{model}"
            or probe.get("configuration_id")
            != self._expected_configuration(model)
        ):
            raise ValueError("model access probe identity differs")
        request = contracts.validate_stage_request(probe["request"])
        result = contracts.validate_stage_result(probe["result"], request)
        panel_row = next(
            row for row in manifest.load_panel()["models"]
            if row["logical_model_id"] == model
        )["providers"][self.provider]
        episode = {
            "id": probe["probe_id"],
            "multiturn_script": self._access_probe_turns(),
        }
        expected_request = contracts.build_stage_request(
            episode,
            execution_id=request["execution_id"],
            provider=self.provider,
            logical_model_id=model,
            provider_model_id=panel_row["provider_model_id"],
            configuration_id=panel_row["configuration_id"],
            stage="stage_1",
            prior_responses={},
        )
        if (
            request != expected_request
            or _canonical_sha(probe["transport_descriptor"])
            != result["transport_request_sha256"]
        ):
            raise ValueError("model access probe stage evidence differs")
        self._validate_provider_evidence({
            "request": request,
            "result": result,
            "transport_descriptor": probe["transport_descriptor"],
            "attestation": probe["attestation"],
        }, episode=episode, prior_artifacts=[])
        _assert_no_credentials(probe)
        return request, result

    def _access_probe_ready(self, request, result):
        return (
            result["terminal_status"] == "complete"
            and result["returned_provider_model_id"]
            == request["provider_model_id"]
            and result["returned_provider_name"] == "OpenAI"
            and result["integrity"]["integrity_valid"] is True
            and result["integrity"]["mechanically_resolved"] is True
            and result["integrity"]["measurement_ready"]
            is (self.run_mode == "live")
        )

    def _validate_access_probe(self, probe, index, model):
        request, result = self._validate_access_probe_evidence(
            probe, index, model
        )
        if not self._access_probe_ready(request, result):
            raise ValueError("model access probe stage evidence differs")
        return probe

    @staticmethod
    def _access_failure_kind(result):
        terminal = result["terminal_status"]
        if terminal == "failed":
            return "provider_terminal_failure"
        if terminal == "invalidated":
            return "integrity_rejection"
        return "access_readiness_rejection"

    def _validate_access_failure(self, record, index, model, attempt_number):
        if (
            type(record) is not dict
            or set(record) != {
                "access_failure_version", "provenance", "provider",
                "attempt_number", "failure_kind", "probe", "failure_sha256",
            }
            or record.get("access_failure_version") != ACCESS_FAILURE_VERSION
            or record.get("provenance") != ACCESS_PROVENANCE
            or record.get("provider") != self.provider
            or record.get("attempt_number") != attempt_number
            or record.get("failure_sha256") != _canonical_sha(
                _without_hash(record, "failure_sha256")
            )
        ):
            raise ValueError("durable access failure binding differs")
        request, result = self._validate_access_probe_evidence(
            record.get("probe"), index, model
        )
        if (
            self._access_probe_ready(request, result)
            or record.get("failure_kind") != self._access_failure_kind(result)
        ):
            raise ValueError("durable access failure outcome differs")
        _assert_no_credentials(record)
        return record

    def _all_access_failures(self, events=None):
        events = self._access_journal_events() if events is None else events
        by_model = {model: [] for model in manifest.MODEL_LOGICAL_IDS}
        expected_paths = set()
        index_by_model = {
            model: index
            for index, model in enumerate(manifest.MODEL_LOGICAL_IDS, 1)
        }
        for event in events:
            if event["state"] != "failed":
                continue
            model = event["logical_model_id"]
            attempt_number = event["attempt_number"]
            expected = self._out_path(
                "access", "failures", model,
                f"attempt-{attempt_number:02d}.json",
            )
            if event["artifact_relative_path"] != expected.relative_to(
                    self.out_dir).as_posix():
                raise ValueError("durable access failure journal path differs")
            expected_paths.add(expected)
            if not expected.is_file() or hashlib.sha256(
                    expected.read_bytes()).hexdigest() != event["artifact_sha256"]:
                raise ValueError("durable access failure history differs")
            record = _read_json(expected)
            self._validate_access_failure(
                record, index_by_model[model], model, attempt_number
            )
            if record["failure_kind"] != event["terminal_kind"]:
                raise ValueError("durable access failure journal kind differs")
            by_model[model].append(record)
        observed_paths = set(self._artifact_files("access", "failures"))
        if observed_paths != expected_paths:
            raise ValueError("durable access failure coverage differs")
        return by_model

    def access(self, *, retry_failed=False):
        report_path = self._out_path("access", "report.json")
        if report_path.exists():
            report = _read_json(report_path)
            self.verify_access()
            return report
        probe_turns = self._access_probe_turns()
        bank_turn_texts = {
            text
            for episode in self.episodes
            for text in episode["multiturn_script"].values()
        }
        if any(text in bank_turn_texts for text in probe_turns.values()):
            raise ValueError("access probe text collides with benchmark bank")
        events = self._reconcile_access_orphans(
            self._access_journal_events()
        )
        self._all_access_failures(events)
        probes = []
        for index, model in enumerate(manifest.MODEL_LOGICAL_IDS, 1):
            model_events = self._access_model_events(events, model)
            latest = model_events[-1] if model_events else None
            probe_path = self._out_path(
                "access", "probes", f"{model}.json"
            )
            if probe_path.is_file():
                probe = _read_json(probe_path)
                self._validate_access_probe(probe, index, model)
                if (
                    latest is None
                    or latest["state"] != "succeeded"
                    or latest["artifact_relative_path"]
                    != probe_path.relative_to(self.out_dir).as_posix()
                    or latest["artifact_sha256"] != hashlib.sha256(
                        probe_path.read_bytes()
                    ).hexdigest()
                ):
                    raise ValueError("access probe journal binding differs")
                probes.append(probe)
                continue
            if latest is not None and latest["state"] == "succeeded":
                raise ValueError("access journal references a missing probe")
            if latest is not None and latest["state"] in {
                    "started", "failed", "abandoned"} and not retry_failed:
                raise ValueError(
                    "explicit access retry is required after an incomplete "
                    "or failed attempt"
                )
            if latest is not None and latest["state"] == "started":
                self._append_access_journal(
                    model=model,
                    attempt_number=latest["attempt_number"],
                    state="abandoned",
                    request_sha256=latest["request_sha256"],
                    transport_descriptor_sha256=latest[
                        "transport_descriptor_sha256"
                    ],
                    start_event=latest,
                    terminal_kind="pre_sink_interruption",
                )
                events = self._access_journal_events()
                model_events = self._access_model_events(events, model)
                latest = model_events[-1]
            prior_attempts = sum(
                row["state"] == "started" for row in model_events
            )
            if prior_attempts >= 3:
                raise ValueError("model access probe exceeded three attempts")
            attempt_number = prior_attempts + 1
            episode = {
                "id": f"ACCESS-PROBE-{index:02d}-{model}",
                "multiturn_script": deepcopy(probe_turns),
            }
            captured = []
            started = []

            def before_stage(event):
                if event["stage"] != "stage_1" or captured or started:
                    raise ValueError("access probe attempted more than one stage")
                request = contracts.validate_stage_request(event["request"])
                descriptor = deepcopy(event["transport_descriptor"])
                if (
                    request["logical_model_id"] != model
                    or request["stage"] != "stage_1"
                    or type(descriptor) is not dict
                ):
                    raise ValueError("access probe start evidence differs")
                started.append(self._append_access_journal(
                    model=model,
                    attempt_number=attempt_number,
                    state="started",
                    request_sha256=request["request_sha256"],
                    transport_descriptor_sha256=_canonical_sha(descriptor),
                ))

            def stage_sink(event):
                if captured or len(started) != 1:
                    raise ValueError("access probe emitted more than one stage")
                event = deepcopy(event)
                request = contracts.validate_stage_request(event["request"])
                result = contracts.validate_stage_result(
                    event["result"], request
                )
                probe = {
                    "probe_id": episode["id"],
                    "provenance": ACCESS_PROVENANCE,
                    "logical_model_id": model,
                    "configuration_id": self._expected_configuration(model),
                    "request": request,
                    "result": result,
                    "transport_descriptor": deepcopy(
                        event["transport_descriptor"]
                    ),
                    "attestation": deepcopy(event["attestation"]),
                }
                if (
                    request["request_sha256"] != started[0]["request_sha256"]
                    or _canonical_sha(probe["transport_descriptor"])
                    != started[0]["transport_descriptor_sha256"]
                ):
                    raise ValueError("access probe terminal differs from start")
                try:
                    self._validate_access_probe(probe, index, model)
                except ValueError:
                    failure = {
                        "access_failure_version": ACCESS_FAILURE_VERSION,
                        "provenance": ACCESS_PROVENANCE,
                        "provider": self.provider,
                        "attempt_number": attempt_number,
                        "failure_kind": self._access_failure_kind(result),
                        "probe": probe,
                    }
                    failure["failure_sha256"] = _canonical_sha(failure)
                    self._validate_access_failure(
                        failure, index, model, attempt_number
                    )
                    failure_path = self._out_path(
                        "access", "failures", model,
                        f"attempt-{attempt_number:02d}.json",
                    )
                    _write_new_json(failure_path, failure)
                    self._append_access_journal(
                        model=model,
                        attempt_number=attempt_number,
                        state="failed",
                        request_sha256=request["request_sha256"],
                        transport_descriptor_sha256=started[0][
                            "transport_descriptor_sha256"
                        ],
                        start_event=started[0],
                        artifact_path=failure_path,
                        terminal_kind=failure["failure_kind"],
                    )
                    raise _AccessProbeFailureRecorded(
                        "durable access failure recorded"
                    ) from None
                _write_new_json(probe_path, probe)
                self._append_access_journal(
                    model=model,
                    attempt_number=attempt_number,
                    state="succeeded",
                    request_sha256=request["request_sha256"],
                    transport_descriptor_sha256=started[0][
                        "transport_descriptor_sha256"
                    ],
                    start_event=started[0],
                    artifact_path=probe_path,
                    terminal_kind="validated_probe",
                )
                captured.append(probe)
                raise _AccessProbeComplete("access probe stage complete")

            try:
                self._call_driver(
                    episode, model,
                    before_stage=before_stage, stage_sink=stage_sink,
                )
            except _AccessProbeComplete:
                pass
            except _AccessProbeFailureRecorded:
                raise ValueError(
                    "durable access failure recorded; explicit access retry "
                    "is required"
                ) from None
            if len(captured) != 1:
                raise ValueError("access probe did not return one validated stage")
            probe = captured[0]
            probes.append(probe)
            events = self._access_journal_events()
        events = self._access_journal_events()
        self._all_access_failures(events)
        attempt_counts = {
            model: sum(
                row["state"] == "started"
                for row in self._access_model_events(events, model)
            )
            for model in manifest.MODEL_LOGICAL_IDS
        }
        if any(
                not self._access_model_events(events, model)
                or self._access_model_events(events, model)[-1]["state"]
                != "succeeded"
                for model in manifest.MODEL_LOGICAL_IDS):
            raise ValueError("access attempt journal is not terminally complete")
        journal_path = self._access_journal_path()
        report = {
            "access_version": "charitroc-model-access-probe-v2",
            "provenance": ACCESS_PROVENANCE,
            "provider": self.provider,
            "measurement_ready": False,
            "models": list(manifest.MODEL_LOGICAL_IDS),
            "attempt_counts": attempt_counts,
            "access_journal_sha256": hashlib.sha256(
                journal_path.read_bytes()
            ).hexdigest(),
            "probes": probes,
        }
        report["access_sha256"] = _canonical_sha(report)
        _write_new_json(report_path, report)
        self.verify_access()
        return report

    def verify_access(self):
        path = self._out_path("access", "report.json")
        if not path.is_file():
            raise ValueError("model access probe is required")
        report = _read_json(path)
        if (
            type(report) is not dict
            or set(report) != {
                "access_version", "provenance", "provider",
                "measurement_ready", "models", "attempt_counts",
                "access_journal_sha256", "probes", "access_sha256",
            }
            or report.get("access_version")
            != "charitroc-model-access-probe-v2"
            or report.get("provenance") != ACCESS_PROVENANCE
            or report.get("provider") != self.provider
            or report.get("measurement_ready") is not False
            or report.get("models") != list(manifest.MODEL_LOGICAL_IDS)
            or report.get("access_sha256") != _canonical_sha(
                _without_hash(report, "access_sha256")
            )
        ):
            raise ValueError("model access probe report binding differs")
        events = self._access_journal_events()
        journal_path = self._access_journal_path()
        expected_attempt_counts = {
            model: sum(
                row["state"] == "started"
                for row in self._access_model_events(events, model)
            )
            for model in manifest.MODEL_LOGICAL_IDS
        }
        if (
            not journal_path.is_file()
            or report.get("attempt_counts") != expected_attempt_counts
            or report.get("access_journal_sha256") != hashlib.sha256(
                journal_path.read_bytes()
            ).hexdigest()
            or any(
                not self._access_model_events(events, model)
                or self._access_model_events(events, model)[-1]["state"]
                != "succeeded"
                for model in manifest.MODEL_LOGICAL_IDS
            )
        ):
            raise ValueError("access attempt journal/report binding differs")
        self._all_access_failures(events)
        probes = report.get("probes")
        if type(probes) is not list or len(probes) != len(
                manifest.MODEL_LOGICAL_IDS):
            raise ValueError("model access probe coverage is incomplete")
        expected_paths = {
            self._out_path("access", "probes", f"{model}.json")
            for model in manifest.MODEL_LOGICAL_IDS
        }
        observed_paths = set(self._artifact_files("access", "probes"))
        if observed_paths != expected_paths:
            raise ValueError("model access probe durable coverage is incomplete")
        for index, (probe, model) in enumerate(zip(
                probes, manifest.MODEL_LOGICAL_IDS), 1):
            durable = _read_json(self._out_path(
                "access", "probes", f"{model}.json"
            ))
            if durable != probe:
                raise ValueError("model access report differs from durable probe")
            self._validate_access_probe(probe, index, model)
            terminal = self._access_model_events(events, model)[-1]
            durable_path = self._out_path(
                "access", "probes", f"{model}.json"
            )
            if (
                terminal["artifact_relative_path"]
                != durable_path.relative_to(self.out_dir).as_posix()
                or terminal["artifact_sha256"] != hashlib.sha256(
                    durable_path.read_bytes()
                ).hexdigest()
            ):
                raise ValueError("access probe journal artifact differs")
        _assert_no_credentials(report)
        return {"valid": True, "models": list(manifest.MODEL_LOGICAL_IDS)}

    def execute(self, stage):
        if stage not in EXECUTION_STAGES:
            raise ValueError(
                f"execute stage must be one of {EXECUTION_STAGES}"
            )
        if stage == "smoke" and self.run_mode == "live":
            self.verify_access()
        plan = self._namespace_plan(stage)
        freeze = None
        if stage in {"private", "private-extension"}:
            freeze_path = self._out_path("freeze.json")
            if not freeze_path.is_file():
                raise ValueError(
                    "freeze required before private/private-extension launch"
                )
            freeze = _read_json(freeze_path)
        for entry in plan["entries"]:
            episode = self._by_id[entry["item_id"]]
            for model in entry["model_execution_order"]:
                events = self._state_events(stage, plan)
                if self._is_settled(events, entry["occurrence_id"], model):
                    continue
                high_attempt = self._start_or_resume(
                    stage, plan, entry, model
                )
                if high_attempt is None:
                    continue
                before_stage, stage_sink = self._stage_callbacks(
                    stage, plan, entry, model, high_attempt, freeze
                )
                run = self._call_driver(
                    episode, model,
                    before_stage=before_stage, stage_sink=stage_sink,
                )
                self._persist_run(
                    stage, plan, entry, model, run, high_attempt
                )
        verification = self.verify(stage)
        if verification["valid"] is not True:
            raise ValueError("panel stage did not reach complete accounting")
        return self._write_harness_report(stage, plan)

    def _artifact_files(self, *parts):
        """Return confined regular JSON artifacts; reject hidden path tricks."""
        root = self._out_path(*parts)
        if not root.exists():
            return []
        if root.is_symlink() or not root.is_dir():
            raise ValueError("artifact root must be a confined real directory")
        files = []
        for path in sorted(root.rglob("*")):
            if path.is_symlink():
                raise ValueError("artifact tree contains a symlink")
            if path.is_dir():
                continue
            if not path.is_file() or path.suffix != ".json":
                raise ValueError("artifact tree contains an unexpected file")
            try:
                path.resolve().relative_to(self.out_dir)
            except ValueError:
                raise ValueError("artifact escaped the confined output root") from None
            files.append(path)
        return files

    def _validate_provider_evidence(
            self, payload, *, episode, prior_artifacts):
        """Re-run the provider-specific frozen transport evidence contract."""
        request = payload["request"]
        result = payload["result"]
        descriptor = payload["transport_descriptor"]
        attestation = payload["attestation"]
        if self.run_mode == "mock":
            expected = {
                "fixture": True,
                "provider": self.provider,
                "request_sha256": request["request_sha256"],
                "stage": request["stage"],
            }
            if descriptor != expected or attestation is not None:
                raise ValueError("mock provider evidence differs from fixture")
            return True
        if self.provider == "openrouter":
            if attestation is not None:
                raise ValueError("OpenRouter evidence cannot carry attestation")
            stage_index = contracts.STAGES.index(request["stage"])
            openrouter_driver.validate_transport_descriptor(
                result,
                descriptor,
                request=request,
                prior_results=[row["result"] for row in prior_artifacts],
                future_turns=model_turns(episode)[stage_index + 1:],
            )
            return True
        if self._live_codex is None:
            self._live_codex = codex_driver.CodexDriver(run_mode="codex")
        if type(descriptor) is not dict or type(descriptor.get("cwd")) is not str:
            raise ValueError("Codex descriptor has no frozen isolation root")
        isolation_dir = Path(descriptor["cwd"]).resolve()
        context_audit = descriptor.get("context_audit")
        if type(context_audit) is dict:
            self._live_codex.restore_persisted_context_audit(
                isolation_dir, context_audit
            )
        prior_session_id = (
            prior_artifacts[0]["result"]["session_id"]
            if prior_artifacts else None
        )
        self._live_codex.validate_stage_evidence(
            request, result, descriptor, attestation, episode,
            isolation_dir=isolation_dir,
            prior_session_id=prior_session_id,
        )
        return True

    def _collect_evidence(self, stage, plan):
        entries = {row["occurrence_id"]: row for row in plan["entries"]}
        artifacts = []
        keys = set()
        for path in self._artifact_files("evidence", stage):
            payload = _read_json(path)
            if type(payload) is not dict:
                raise ValueError("stage evidence artifact must be an object")
            entry = entries.get(payload.get("plan_occurrence_id"))
            model = payload.get("logical_model_id")
            if entry is None or model not in entry["model_execution_order"]:
                raise ValueError("stage evidence is absent from the frozen plan")
            try:
                orchestration_attempt = payload["orchestration_attempt"]
                session_attempt = payload["session_attempt"]
                result_stage = payload["stage"]
            except KeyError:
                raise ValueError("stage evidence accounting fields are missing") from None
            expected_path = self._evidence_path(
                stage, entry["occurrence_id"], model,
                orchestration_attempt, session_attempt, result_stage,
            )
            if path != expected_path:
                raise ValueError("stage evidence path/binding differs")
            self._validate_evidence(
                payload, plan=plan, entry=entry, model=model,
                orchestration_attempt=orchestration_attempt,
                session_attempt=session_attempt,
                expected_stage=result_stage,
            )
            key = (
                entry["occurrence_id"], model, orchestration_attempt,
                session_attempt, result_stage,
            )
            if key in keys:
                raise ValueError("duplicate stage evidence accounting key")
            keys.add(key)
            artifacts.append(payload)

        groups = {}
        for payload in artifacts:
            key = (
                payload["plan_occurrence_id"],
                payload["logical_model_id"],
                payload["orchestration_attempt"],
                payload["session_attempt"],
            )
            groups.setdefault(key, []).append(payload)
        for key, group in groups.items():
            group.sort(key=lambda row: contracts.STAGES.index(row["stage"]))
            stages = [row["stage"] for row in group]
            if stages != list(contracts.STAGES[:len(stages)]):
                raise ValueError("stage evidence is not a contiguous prefix")
            episode = self._by_id[group[0]["item_id"]]
            prior_responses = {}
            prior_artifacts = []
            execution_id = group[0]["request"]["execution_id"]
            for index, payload in enumerate(group):
                request = payload["request"]
                expected_request = contracts.build_stage_request(
                    episode,
                    execution_id=execution_id,
                    provider=self.provider,
                    logical_model_id=payload["logical_model_id"],
                    provider_model_id=request["provider_model_id"],
                    configuration_id=self._expected_configuration(
                        payload["logical_model_id"]
                    ),
                    stage=payload["stage"],
                    prior_responses=prior_responses,
                )
                if request != expected_request:
                    raise ValueError(
                        "stage evidence request differs from bank-visible history"
                    )
                self._validate_provider_evidence(
                    payload, episode=episode,
                    prior_artifacts=prior_artifacts,
                )
                raw = payload["result"]["attempts"][-1][
                    "raw_final_message"
                ]
                if index < len(group) - 1 and type(raw) is not str:
                    raise ValueError(
                        "stage evidence advanced without a raw response"
                    )
                if type(raw) is str:
                    prior_responses[payload["stage"]] = raw
                prior_artifacts.append(payload)
        for key, group in groups.items():
            occurrence, model, orchestration_attempt, session_attempt = key
            if session_attempt != 2:
                continue
            prior = groups.get((
                occurrence, model, orchestration_attempt, 1,
            ))
            if not prior:
                raise ValueError("integrity session two lacks prior evidence")
            contracts.validate_integrity_rerun(
                [row["request"] for row in prior],
                [row["result"] for row in prior],
                [group[0]["request"]],
            )
        return artifacts

    def _collect_failures(self, stage, plan):
        entries = {row["occurrence_id"]: row for row in plan["entries"]}
        failures = []
        keys = set()
        for path in self._artifact_files("failures", stage):
            payload = _read_json(path)
            if type(payload) is not dict or set(payload) != set(
                    FAILURE_ARTIFACT_KEYS):
                raise ValueError("failure attempt artifact keys are not exact")
            if payload["failure_artifact_version"] != (
                    "charitroc-panel-failure-attempt-v1"):
                raise ValueError("failure attempt artifact version differs")
            if payload["failure_artifact_sha256"] != _canonical_sha(
                    _without_hash(payload, "failure_artifact_sha256")):
                raise ValueError("failure attempt artifact hash differs")
            entry = entries.get(payload["plan_occurrence_id"])
            model = payload["logical_model_id"]
            if (
                entry is None
                or entry["item_id"] != payload["item_id"]
                or model not in entry["model_execution_order"]
                or payload["provider"] != self.provider
                or payload["plan_hash"] != plan["plan_hash"]
                or payload["configuration_id"]
                != self._expected_configuration(model)
            ):
                raise ValueError("failure attempt plan identity differs")
            request = contracts.validate_stage_request(
                payload["failed_request"]
            )
            failure = payload["failure_record"]
            if type(failure) is not dict or set(failure) != {
                "failure_record_version", "provenance", "run_mode",
                "measurement_ready", "failure_kind", "raw_bytes_base64",
                "raw_bytes_sha256", "raw_byte_count", "raw_redacted",
                "provider", "logical_model_id", "model",
                "provider_model_id", "configuration_id", "request_sha256",
                "transport_request_sha256",
            }:
                raise ValueError("failure record keys are not exact")
            expected_provenance = (
                openrouter_driver.LIVE_ATTEMPT_PROVENANCE
                if self.run_mode == "live" else MOCK_PROVENANCE
            )
            expected_failure_mode = (
                "openrouter" if self.run_mode == "live" else "mock"
            )
            allowed_failure_kinds = {
                "invalid_chunk", "trace_limit", "iterator_failure",
                "credential_material", "invalid_utf8",
            }
            if (
                self.provider != "openrouter"
                or failure["failure_record_version"]
                != openrouter_driver.FAILURE_RECORD_VERSION
                or failure["provenance"] != expected_provenance
                or payload["provenance"] != expected_provenance
                or failure["run_mode"] != expected_failure_mode
                or failure["measurement_ready"] is not False
                or type(failure["failure_kind"]) is not str
                or failure["failure_kind"] not in allowed_failure_kinds
                or type(failure["raw_redacted"]) is not bool
                or isinstance(failure["raw_byte_count"], bool)
                or type(failure["raw_byte_count"]) is not int
                or failure["raw_byte_count"] < 0
                or re.fullmatch(
                    r"[0-9a-f]{64}", failure["raw_bytes_sha256"]
                    if type(failure["raw_bytes_sha256"]) is str else ""
                ) is None
                or re.fullmatch(
                    r"[0-9a-f]{64}",
                    failure["transport_request_sha256"]
                    if type(failure["transport_request_sha256"]) is str
                    else "",
                ) is None
                or failure["provider"] != self.provider
                or failure["logical_model_id"] != model
                or failure["configuration_id"]
                != self._expected_configuration(model)
                or failure["provider_model_id"]
                != request["provider_model_id"]
                or failure["model"] != request["provider_model_id"]
                or failure["request_sha256"] != request["request_sha256"]
                or payload["execution_id"] != request["execution_id"]
                or payload["stage"] != request["stage"]
            ):
                raise ValueError("failure attempt request/provenance differs")
            if failure["raw_redacted"]:
                if (
                    failure["raw_bytes_base64"] is not None
                    or failure["failure_kind"] != "credential_material"
                    or failure["raw_byte_count"] == 0
                ):
                    raise ValueError("redacted failure retained raw bytes")
            else:
                if failure["failure_kind"] == "credential_material":
                    raise ValueError(
                        "credential failure must be redacted"
                    )
                try:
                    raw = base64.b64decode(
                        failure["raw_bytes_base64"], validate=True
                    )
                except (TypeError, ValueError):
                    raise ValueError("failure raw bytes are invalid") from None
                if (
                    len(raw) != failure["raw_byte_count"]
                    or hashlib.sha256(raw).hexdigest()
                    != failure["raw_bytes_sha256"]
                ):
                    raise ValueError("failure raw byte hash differs")
            expected_path = self._out_path(
                "failures", stage, entry["occurrence_id"], model,
                f"orchestration-{payload['orchestration_attempt']}",
                f"session-{payload['integrity_session']}.json",
            )
            if path != expected_path:
                raise ValueError("failure attempt path/binding differs")
            key = (
                entry["occurrence_id"], model,
                payload["orchestration_attempt"],
                payload["integrity_session"], payload["stage"],
            )
            if key in keys:
                raise ValueError("duplicate failure attempt accounting key")
            keys.add(key)
            _assert_no_credentials(payload)
            failures.append(payload)
        return failures

    def _validate_ledger(self, stage, plan, artifacts):
        rows = _read_jsonl(self._ledger_path(stage))
        artifact_index = {
            (
                row["plan_occurrence_id"], row["logical_model_id"],
                row["orchestration_attempt"], row["session_attempt"],
                row["stage"],
            ): row for row in artifacts
        }
        observed = set()
        ids = set()
        for row in rows:
            if type(row) is not dict or set(row) != set(LEDGER_KEYS):
                raise ValueError("stage-attempt ledger schema keys are not exact")
            key = (
                row["plan_occurrence_id"], row["logical_model_id"],
                row["orchestration_attempt"], row["session_attempt"],
                row["stage"], row["transport_attempt"],
            )
            artifact = artifact_index.get(key[:-1])
            if artifact is None:
                raise ValueError("ledger has no matching stage evidence")
            attempts = {
                item["attempt_index"]: item
                for item in artifact["result"]["attempts"]
            }
            attempt = attempts.get(row["transport_attempt"])
            if attempt is None:
                raise ValueError("ledger transport attempt is absent from evidence")
            relative = self._evidence_path(
                stage, artifact["plan_occurrence_id"],
                artifact["logical_model_id"],
                artifact["orchestration_attempt"],
                artifact["session_attempt"], artifact["stage"],
            ).relative_to(self.out_dir).as_posix()
            _parse_timestamp(row["persisted_at_utc"])
            event_without_id = {
                "ledger_version": LEDGER_VERSION,
                "provenance": self.provenance,
                "provider": self.provider,
                "plan_hash": plan["plan_hash"],
                "plan_occurrence_id": artifact["plan_occurrence_id"],
                "item_id": artifact["item_id"],
                "logical_model_id": artifact["logical_model_id"],
                "configuration_id": artifact["result"]["configuration_id"],
                "orchestration_attempt": artifact[
                    "orchestration_attempt"
                ],
                "session_attempt": artifact["session_attempt"],
                "stage": artifact["stage"],
                "session_id": artifact["result"]["session_id"],
                "transport_attempt": attempt["attempt_index"],
                "attempt_started_at_utc": attempt["started_at_utc"],
                "attempt_completed_at_utc": attempt["completed_at_utc"],
                "request_sha256": artifact["request"]["request_sha256"],
                "result_sha256": artifact["result"]["result_sha256"],
                "transport_request_sha256": artifact["result"][
                    "transport_request_sha256"
                ],
                "raw_trace_sha256": attempt["raw_trace_sha256"],
                "artifact_relative_path": relative,
                "artifact_sha256": artifact["evidence_sha256"],
                "stage_terminal_status": artifact["result"][
                    "terminal_status"
                ],
                "format_repair_count": 0,
                "state": "persisted",
                "persisted_at_utc": row["persisted_at_utc"],
            }
            expected = {
                "event_id": "ledger-" + _canonical_sha(event_without_id),
                **event_without_id,
            }
            if row != expected:
                raise ValueError("ledger differs from exact stage evidence")
            if row["event_id"] in ids or key in observed:
                raise ValueError("duplicate stage-attempt ledger accounting")
            ids.add(row["event_id"])
            observed.add(key)
        expected_keys = {
            (
                artifact["plan_occurrence_id"],
                artifact["logical_model_id"],
                artifact["orchestration_attempt"],
                artifact["session_attempt"], artifact["stage"],
                attempt["attempt_index"],
            )
            for artifact in artifacts
            for attempt in artifact["result"]["attempts"]
        }
        if observed != expected_keys:
            raise ValueError(
                "evidence/ledger accounting is incomplete or has extras"
            )
        return rows

    def _validate_invocations(
            self, stage, plan, artifacts, ledger, failures):
        rows = _read_jsonl(self._invocation_path(stage))
        entries = {row["occurrence_id"]: row for row in plan["entries"]}
        ids = set()
        started = {}
        abandoned = {}
        previous_time = None
        for row in rows:
            if type(row) is not dict or set(row) != set(INVOCATION_KEYS):
                raise ValueError("invocation journal schema keys are not exact")
            base = {
                field: row[field] for field in INVOCATION_KEYS
                if field not in {"event_id", "event_sha256"}
            }
            event_without_hash = {
                "event_id": "invocation-" + _canonical_sha(base),
                **base,
            }
            expected = {
                **event_without_hash,
                "event_sha256": _canonical_sha(event_without_hash),
            }
            if row != expected:
                raise ValueError("invocation journal hash/event differs")
            entry = entries.get(row["plan_occurrence_id"])
            if (
                row["invocation_version"] != INVOCATION_VERSION
                or row["provenance"] != self.provenance
                or row["provider"] != self.provider
                or row["plan_hash"] != plan["plan_hash"]
                or entry is None
                or entry["item_id"] != row["item_id"]
                or row["logical_model_id"]
                not in entry["model_execution_order"]
                or row["configuration_id"] != self._expected_configuration(
                    row["logical_model_id"]
                )
                or type(row["orchestration_attempt"]) is not int
                or row["orchestration_attempt"] < 1
                or row["integrity_session"] not in {1, 2}
                or row["stage"] not in contracts.STAGES
            ):
                raise ValueError("invocation journal plan binding differs")
            timestamp = _parse_timestamp(row["timestamp_utc"])
            if previous_time is not None and timestamp < previous_time:
                raise ValueError("invocation journal timestamps reverse")
            previous_time = timestamp
            if row["event_id"] in ids:
                raise ValueError("duplicate invocation journal event")
            ids.add(row["event_id"])
            key = (
                row["plan_occurrence_id"], row["logical_model_id"],
                row["orchestration_attempt"], row["integrity_session"],
                row["stage"],
            )
            target = started if row["journal_state"] == "started" else abandoned
            if row["journal_state"] not in {"started", "abandoned"}:
                raise ValueError("invocation journal state differs")
            if key in target:
                raise ValueError("duplicate invocation journal composite key")
            if row["journal_state"] == "started":
                if row["reason"] is not None:
                    raise ValueError("started invocation cannot have a reason")
            elif row["reason"] != "orchestrator_resume_after_interruption":
                raise ValueError("abandoned invocation reason differs")
            target[key] = row

        evidence_by_key = {(
            row["plan_occurrence_id"], row["logical_model_id"],
            row["orchestration_attempt"], row["session_attempt"],
            row["stage"],
        ): row for row in artifacts}
        failure_by_key = {(
            row["plan_occurrence_id"], row["logical_model_id"],
            row["orchestration_attempt"], row["integrity_session"],
            row["stage"],
        ): row for row in failures}
        for key, start in started.items():
            evidence = evidence_by_key.get(key)
            failure = failure_by_key.get(key)
            abandonment = abandoned.get(key)
            terminals = sum(value is not None for value in (
                evidence, failure, abandonment
            ))
            if terminals != 1:
                raise ValueError(
                    "invocation accounting requires one terminal outcome"
                )
            if evidence is not None and (
                start["execution_id"] != evidence["request"]["execution_id"]
                or start["request_sha256"]
                != evidence["request"]["request_sha256"]
                or start["transport_descriptor_sha256"]
                != evidence["result"]["transport_request_sha256"]
            ):
                raise ValueError("invocation/evidence binding differs")
            if failure is not None and (
                start["execution_id"] != failure["execution_id"]
                or start["request_sha256"]
                != failure["failed_request"]["request_sha256"]
                or start["transport_descriptor_sha256"]
                != failure["failure_record"]["transport_request_sha256"]
            ):
                raise ValueError("invocation/failure binding differs")
            if abandonment is not None and any(
                    abandonment[field] != start[field] for field in (
                        "execution_id", "request_sha256",
                        "transport_descriptor_sha256",
                    )):
                raise ValueError("invocation abandonment binding differs")
        terminal_keys = set(evidence_by_key) | set(failure_by_key) | set(abandoned)
        if terminal_keys != set(started):
            raise ValueError("invocation/evidence accounting is incomplete")
        # Ledger completeness was checked separately; binding the parameter
        # here makes the terminal contract explicit and prevents accidental
        # verification reordering.
        if artifacts and not ledger:
            raise ValueError("invocation terminal evidence lacks ledger")
        return rows

    def _final_artifacts(self, plan, events, artifacts, failures):
        evidence_groups = {}
        failure_groups = {}
        for row in artifacts:
            key = (
                row["plan_occurrence_id"], row["logical_model_id"],
                row["orchestration_attempt"], row["session_attempt"],
            )
            evidence_groups.setdefault(key, []).append(row)
        for row in failures:
            key = (
                row["plan_occurrence_id"], row["logical_model_id"],
                row["orchestration_attempt"], row["integrity_session"],
            )
            failure_groups.setdefault(key, []).append(row)
        finals = {}
        for entry in plan["entries"]:
            occurrence = entry["occurrence_id"]
            for model in entry["model_execution_order"]:
                latest = self._latest_state(events, occurrence, model)
                if latest is None or not self._is_settled(
                        events, occurrence, model):
                    raise ValueError("stage accounting is not completely settled")
                session_attempt = latest["session_attempt"]
                if session_attempt == 1:
                    orchestration_attempt = latest["attempt"]
                else:
                    first_terminal = [row for row in events if (
                        row["plan_occurrence_id"] == occurrence
                        and row["logical_model_id"] == model
                        and row["session_attempt"] == 1
                        and row["state"] == "invalidated"
                    )]
                    if not first_terminal:
                        raise ValueError(
                            "integrity rerun lacks its first terminal state"
                        )
                    orchestration_attempt = first_terminal[-1]["attempt"]
                group_key = (
                    occurrence, model, orchestration_attempt,
                    session_attempt,
                )
                group = sorted(
                    evidence_groups.get(group_key, []),
                    key=lambda row: contracts.STAGES.index(row["stage"]),
                )
                failed = failure_groups.get(group_key, [])
                if len(failed) > 1:
                    raise ValueError("multiple terminal failure attempts exist")
                if failed:
                    failure = failed[0]
                    prior_responses = {
                        row["stage"]: row["result"]["attempts"][-1][
                            "raw_final_message"
                        ] for row in group
                    }
                    if any(type(value) is not str
                           for value in prior_responses.values()):
                        raise ValueError(
                            "failure attempt followed a missing raw response"
                        )
                    request = failure["failed_request"]
                    expected_request = contracts.build_stage_request(
                        self._by_id[entry["item_id"]],
                        execution_id=request["execution_id"],
                        provider=self.provider,
                        logical_model_id=model,
                        provider_model_id=request["provider_model_id"],
                        configuration_id=self._expected_configuration(model),
                        stage=request["stage"],
                        prior_responses=prior_responses,
                    )
                    if request != expected_request or (
                            group and request["execution_id"]
                            != group[0]["request"]["execution_id"]):
                        raise ValueError(
                            "failure request differs from prior stage evidence"
                        )
                if latest["state"] == "complete":
                    if failed or len(group) != len(contracts.STAGES):
                        raise ValueError(
                            "complete state lacks four-stage evidence"
                        )
                    session_status = self._session_status([
                        row["result"] for row in group
                    ])
                    if session_status not in {"complete", "unresolved"}:
                        raise ValueError("complete state has failed evidence")
                elif latest["state"] == "failed":
                    session_status = "failed"
                    if not failed and self._session_status([
                            row["result"] for row in group]) != "failed":
                        raise ValueError("failed state lacks failure evidence")
                else:
                    raise ValueError("settled stage has no terminal state")
                finals[(occurrence, model)] = {
                    "artifacts": group,
                    "session_status": session_status,
                }
        return finals

    def _validate_scores(self, stage, plan, finals):
        paths = self._artifact_files("scores", stage)
        expected_paths = {
            self._score_path(stage, entry["occurrence_id"], model): (
                entry, model
            )
            for entry in plan["entries"]
            for model in entry["model_execution_order"]
        }
        if set(paths) != set(expected_paths):
            raise ValueError("mechanical score accounting is incomplete or extra")
        if stage == "reliability":
            self._calibration_score_index = None
        scores = []
        for path, (entry, model) in expected_paths.items():
            observed = self._validate_score(_read_json(path))
            final = finals[(entry["occurrence_id"], model)]
            expected = self._build_score(
                stage, plan, entry, model, final["session_status"],
                final["artifacts"],
            )
            if observed != expected:
                raise ValueError(
                    "mechanical score differs from trusted sidecar/evidence "
                    "rederivation"
                )
            scores.append(observed)
        return scores

    def _score_rows(self, stage):
        return [
            self._validate_score(_read_json(path))
            for path in self._artifact_files("scores", stage)
        ]

    def _validate_queue(self, stage, scores, finals):
        rows = _read_jsonl(self._out_path(
            "judge_queue", f"{stage}.jsonl"
        ))
        actual = {}
        ids = set()
        for row in rows:
            if type(row) is not dict or set(row) != set(JUDGE_QUEUE_KEYS):
                raise ValueError("judge queue schema keys are not exact")
            if (
                row["queue_version"] != QUEUE_VERSION
                or row["provenance"] != self.provenance
                or row["provider"] != self.provider
                or row["queue_sha256"] != _canonical_sha(
                    _without_hash(row, "queue_sha256")
                )
            ):
                raise ValueError("judge queue provenance/hash mismatch")
            if row["queue_event_id"] in ids:
                raise ValueError("duplicate judge queue event")
            ids.add(row["queue_event_id"])
            key = (
                row["response_artifact_relative_path"], row["stage"],
                row["logical_model_id"],
            )
            if key in actual:
                raise ValueError("duplicate judge queue accounting key")
            actual[key] = row

        expected = {}
        score_index = {(
            row["plan_occurrence_id"], row["logical_model_id"],
        ): row for row in scores}
        for key, final in finals.items():
            score = score_index[key]
            for artifact in final["artifacts"]:
                attempt = artifact["result"]["attempts"][-1]
                if attempt["parsed_response"] is not None:
                    continue
                path = self._evidence_path(
                    stage, artifact["plan_occurrence_id"],
                    artifact["logical_model_id"],
                    artifact["orchestration_attempt"],
                    artifact["session_attempt"], artifact["stage"],
                )
                relative = path.relative_to(self.out_dir).as_posix()
                queue_key = (
                    relative, artifact["stage"],
                    artifact["logical_model_id"],
                )
                observed = actual.get(queue_key)
                if observed is None:
                    raise ValueError("judge queue accounting is not complete")
                _parse_timestamp(observed["queued_at_utc"])
                body = {
                    "queue_version": QUEUE_VERSION,
                    "provenance": self.provenance,
                    "provider": self.provider,
                    "logical_model_id": score["logical_model_id"],
                    "configuration_id": score["configuration_id"],
                    "judge_case_id": self._judge_by_item[score["item_id"]],
                    "stage": artifact["stage"],
                    "response_artifact_relative_path": relative,
                    "response_artifact_sha256": artifact[
                        "evidence_sha256"
                    ],
                    "raw_final_message_sha256": attempt[
                        "raw_final_message_sha256"
                    ],
                    "reason": "unresolved_canonical_response",
                    "queued_at_utc": observed["queued_at_utc"],
                }
                body["queue_event_id"] = "queue-" + _canonical_sha(body)
                body["queue_sha256"] = _canonical_sha(body)
                if observed != body:
                    raise ValueError(
                        "judge queue differs from exact raw evidence"
                    )
                expected[queue_key] = body
        if set(actual) != set(expected):
            raise ValueError("judge queue accounting is incomplete or extra")
        return rows

    def verify(self, stage=None):
        stages = [stage] if stage is not None else [
            name for name in RUN_STAGES if self._plan_path(name).exists()
        ]
        if stage is None and self._state_path("private-extension").exists():
            stages.append("private-extension")
        if not stages:
            raise ValueError("no persisted stage plan is available to verify")
        reports = {}
        for name in stages:
            if name == "reliability":
                calibration_dependency = self.verify("calibration")
                if calibration_dependency.get("valid") is not True:
                    raise ValueError(
                        "reliability verification requires trusted calibration"
                    )
            plan = self._namespace_plan(name)
            # Verification is a replay from persisted bytes, never an
            # assertion about the orchestrator's in-memory append cache.
            events = self._state_events(name, plan, refresh=True)
            expected = len(plan["entries"]) * len(manifest.MODEL_LOGICAL_IDS)
            settled = sum(
                self._is_settled(events, entry["occurrence_id"], model)
                for entry in plan["entries"]
                for model in entry["model_execution_order"]
            )
            if settled != expected:
                raise ValueError("stage accounting is not completely settled")
            artifacts = self._collect_evidence(name, plan)
            failures = self._collect_failures(name, plan)
            ledger = self._validate_ledger(name, plan, artifacts)
            invocations = self._validate_invocations(
                name, plan, artifacts, ledger, failures
            )
            finals = self._final_artifacts(
                plan, events, artifacts, failures
            )
            scores = self._validate_scores(name, plan, finals)
            queue = self._validate_queue(name, scores, finals)
            reports[name] = {
                "valid": True,
                "expected_model_episodes": expected,
                "settled_model_episodes": settled,
                "score_record_count": len(scores),
                "stage_evidence_count": len(artifacts),
                "stage_attempt_ledger_count": len(ledger),
                "invocation_journal_count": len(invocations),
                "failure_attempt_count": len(failures),
                "judge_queue_count": len(queue),
            }
        return (
            {"valid": all(row["valid"] for row in reports.values()),
             "stages": reports}
            if stage is None else {**reports[stage], "stage": stage}
        )

    @staticmethod
    def _harness_row(score):
        return {
            "model_id": score["logical_model_id"],
            "sample_cell_id": score["sample_cell_id"],
            "stage_count": score["stage_count"],
            "transport_retry_count": score["transport_retry_count"],
            "format_repair_count": score["format_repair_count"],
            "format_repair_flagged": score["format_repair_flagged"],
            "semantic_response_replaced": score[
                "semantic_response_replaced"
            ],
            "tool_calls": score["tool_calls"],
            "future_text_seen": score["future_text_seen"],
            "thread_chain_ok": score["thread_chain_ok"],
            "terminal_invalidated": score["terminal_invalidated"],
            "invalidation_reason": score["invalidation_reason"],
            "unresolved": score["unresolved"],
            "judge_queued": score["judge_queued"],
            "mechanically_resolved": score["mechanically_resolved"],
        }

    def _write_harness_report(self, stage, plan):
        scores = self._score_rows(stage)
        harness = gates.evaluate_harness(
            [self._harness_row(row) for row in scores],
            [entry["occurrence_id"] for entry in plan["entries"]],
        )
        report = {
            "report_version": REPORT_VERSION,
            "provenance": self.provenance,
            "provider": self.provider,
            "stage": stage,
            "plan_hash": plan["plan_hash"],
            "channels_reported_separately": True,
            "format_repair_count": 0,
            "harness": harness,
        }
        report["report_sha256"] = _canonical_sha(report)
        _write_or_validate(
            self._out_path("reports", f"{stage}-harness.json"), report
        )
        return report

    def _analysis_model(self, rows, seed_offset):
        primary = [{
            "item_family": row["family"],
            "label": row["label"],
            "stage4_score": row["stage4_score"],
            "pair_id": row["pair_id"],
            "base_rate_benign": row["base_rate_benign"],
            "provenance": row["provenance"],
        } for row in rows]
        stage3 = [{
            "update_correct": row["stage3_update_correct"],
            "cue_variant": row["cue_variant"],
            "provenance": row["provenance"],
        } for row in rows]
        analyzed = bank_analysis.analyze_model(
            primary,
            bootstrap_draws=self.bootstrap_draws,
            seed=manifest.BANK_GENERATION_SEED + seed_offset,
            provenance=self.provenance,
        )
        update = bank_analysis.aggregate_stage3(
            stage3, provenance=self.provenance
        )
        signed = {}
        for prior, cells in analyzed["operating_points_by_prior"].items():
            for cost, cell in cells.items():
                signed[f"{prior}|{cost}"] = cell["signed_distance"]
        summary = {
            "random_effects_pooled_auc": analyzed[
                "hierarchical_pool"
            ]["pooled_auc"],
            "family_auc": {
                family: estimate["auc"]
                for family, estimate in analyzed["family_auc"].items()
            },
            "stage3_accuracy": update["accuracy"],
            "stage3_accuracy_by_cue": {
                cue: update["by_cue"][cue]["accuracy"]
                for cue in gates.CUE_CONDITIONS
            },
            "signed_distance_by_cell": signed,
        }
        return analyzed, update, summary

    def _primary_analysis_only(self, rows, seed_offset):
        primary = [{
            "item_family": row["family"],
            "label": row["label"],
            "stage4_score": row["stage4_score"],
            "pair_id": row["pair_id"],
            "base_rate_benign": row["base_rate_benign"],
            "provenance": row["provenance"],
        } for row in rows]
        return bank_analysis.analyze_model(
            primary,
            bootstrap_draws=self.bootstrap_draws,
            seed=manifest.BANK_GENERATION_SEED + seed_offset,
            provenance=self.provenance,
        )

    @staticmethod
    def _repeats(calibration, reliability):
        dimensions = {}
        for dimension, field in (
                ("stage4_action_score", "stage4_score"),
                ("stage3_update_correct", "stage3_update_correct")):
            block = {
                "primary": {model: {} for model in manifest.MODEL_LOGICAL_IDS},
                "repeat": {model: {} for model in manifest.MODEL_LOGICAL_IDS},
            }
            for row in reliability:
                model = row["logical_model_id"]
                item_id = row["item_id"]
                primary = [candidate for candidate in calibration if (
                    candidate["logical_model_id"] == model
                    and candidate["item_id"] == item_id
                )]
                if len(primary) != 1:
                    raise ValueError("reliability primary linkage is not unique")
                block["primary"][model][item_id] = int(primary[0][field])
                block["repeat"][model][item_id] = int(row[field])
            dimensions[dimension] = block
        return {"dimensions": dimensions}

    def analyze(self):
        calibration_verify = self.verify("calibration")
        reliability_verify = self.verify("reliability")
        if not calibration_verify["valid"] or not reliability_verify["valid"]:
            raise ValueError("analysis requires complete calibration/reliability")
        calibration = self._score_rows("calibration")
        reliability = self._score_rows("reliability")
        plan = self._plan("calibration")
        harness_report = self._write_harness_report("calibration", plan)[
            "harness"
        ]
        summary = {"models": {}}
        model_reports = {}
        sensitivity = {}
        family_rows = []
        operating_rows = []
        if harness_report["measurement_ready"]:
            for index, model in enumerate(manifest.MODEL_LOGICAL_IDS):
                rows = [row for row in calibration if row[
                    "logical_model_id"] == model]
                analyzed, update, model_summary = self._analysis_model(rows, index)
                summary["models"][model] = model_summary
                model_reports[model] = {
                    "primary": analyzed,
                    "stage3": update,
                }
                without_controls = [
                    row for row in rows if not row[
                        "indistinguishable_control"]
                ]
                # Every calibration absent-cue pair is a declared ambiguity
                # control, so the sensitivity stratum intentionally has no
                # absent-cue update channel.  Re-estimate the primary AUC and
                # operating channels only; do not fabricate a cue accuracy.
                sensitivity[model] = self._primary_analysis_only(
                    without_controls, 100 + index
                )
                for family, estimate in analyzed["family_auc"].items():
                    family_rows.append({
                        "logical_model_id": model,
                        "family": family,
                        **estimate,
                    })
                for prior, cells in analyzed[
                        "operating_points_by_prior"].items():
                    for cost, cell in cells.items():
                        operating_rows.append({
                            "logical_model_id": model,
                            "prior": prior,
                            "cost_ratio": cost,
                            **cell,
                        })
        repeats = self._repeats(calibration, reliability)
        terminal_records = [{
            "model_id": row["logical_model_id"],
            "family": row["family"],
            "item_id": row["item_id"],
            "terminal_decision": row["stage4_decision"],
            "mechanically_resolved": row["mechanically_resolved"],
        } for row in calibration if row["mechanically_resolved"]]
        gate_report = gates.evaluate(
            summary, repeats,
            harness_report=harness_report,
            terminal_records=terminal_records,
        )
        ambiguity_rows = [{
            "model_id": row["logical_model_id"],
            "pair_id": row["pair_id"],
            "family": row["family"],
            "item_id": row["item_id"],
            "true_type": row["true_type"],
            "transcript_hash": row["transcript_hash"],
            "declared_ambiguity_control": row[
                "indistinguishable_control"
            ],
            "mechanically_resolved": row["mechanically_resolved"],
            "terminal_decision": row["stage4_decision"],
        } for row in calibration if row["indistinguishable_control"]]
        ambiguity = (
            gates.evaluate_ambiguity_controls(ambiguity_rows)
            if ambiguity_rows else {"passed": False, "violations": [
                "no ambiguity-control observations"
            ]}
        )
        report = {
            "analysis_version": ANALYSIS_VERSION,
            "provenance": self.provenance,
            "provider": self.provider,
            "bootstrap_draws": self.bootstrap_draws,
            "channels_reported_separately": True,
            "harness": harness_report,
            "summary": summary,
            "model_reports": model_reports,
            "family_rows": family_rows,
            "operating_point_rows": operating_rows,
            "repeats": repeats,
            "ambiguity_controls": ambiguity,
            "ambiguity_control_sensitivity": sensitivity,
            "gate_report": gate_report,
        }
        report["analysis_sha256"] = _canonical_sha(report)
        _write_or_validate(
            self._out_path("reports", "calibration-analysis.json"), report
        )
        return report

    def _verify_private_namespaces(self):
        freeze_path = self._out_path("freeze.json")
        if not freeze_path.is_file():
            raise ValueError("private analysis requires the frozen launch record")
        freeze = _read_json(freeze_path)
        protocol = self._validate_private_protocol(freeze)
        private_plan = self._plan("private")
        if len(private_plan["entries"]) != 96 or len(
                private_plan["extension_entries"]) != 96:
            raise ValueError("private analysis plan coverage is not exact")
        self._validate_private_call(
            freeze, private_plan["entries"][0]["item_id"]
        )
        stage_reports = {"private": self.verify("private")}
        activation_path = self._out_path(
            "reports", "private-extension-activation.json"
        )
        if activation_path.is_file():
            self._execution_entries("private-extension", private_plan)
            stage_reports["private-extension"] = self.verify(
                "private-extension"
            )
        if any(report.get("valid") is not True
               for report in stage_reports.values()):
            raise ValueError("private analysis requires verified score evidence")
        return {
            "stage_reports": stage_reports,
            "private_protocol_freeze_sha256": protocol[
                "protocol_freeze_sha256"
            ],
            "calibration_analysis_file_sha256": protocol[
                "calibration_analysis_file_sha256"
            ],
            "private_plan_hash": protocol["private_plan_hash"],
            "extension_entries_sha256": protocol[
                "extension_entries_sha256"
            ],
        }

    def _private_confirmation_inputs(self, *, verification):
        activation_path = self._out_path(
            "reports", "private-extension-activation.json"
        )
        extension_used = activation_path.is_file()
        namespaces = ["private"] + (["private-extension"] if extension_used else [])
        rows = []
        for namespace in namespaces:
            rows.extend(self._score_rows(namespace))
        by_model = {
            model: [row for row in rows if row["logical_model_id"] == model]
            for model in manifest.MODEL_LOGICAL_IDS
        }
        counts = {len(value) for value in by_model.values()}
        if len(counts) != 1 or next(iter(counts), 0) not in {96, 192}:
            raise ValueError("private confirmation requires exact 96/192 coverage")
        episodes_per_model = next(iter(counts))
        criteria = []
        bootstrap_inputs = {}
        for index, template in enumerate(PRIVATE_CRITERIA_TEMPLATES):
            model = template["logical_model_id"]
            model_rows = by_model[model]
            estimate = bank_analysis.roc.clustered_bootstrap_auc(
                [row["label"] for row in model_rows],
                [row["stage4_score"] for row in model_rows],
                clusters=[row["pair_id"] for row in model_rows],
                draws=self.bootstrap_draws,
                seed=manifest.BANK_GENERATION_SEED + 700 + index,
            )
            criteria.append({
                "criterion_id": template["criterion_id"],
                "estimate": estimate["auc"],
                "ci95": estimate["ci95"],
                "threshold": template["threshold"],
                "direction": template["direction"],
                "frozen": True,
            })
            bootstrap_inputs[model] = {
                "draws": self.bootstrap_draws,
                "score_sha256s": sorted(
                    row["score_sha256"] for row in model_rows
                ),
            }
        return {
            "episodes_per_model": episodes_per_model,
            "extension_already_used": extension_used,
            "criteria": criteria,
            "model_auc_bootstrap_inputs": bootstrap_inputs,
            "freeze_hash": _read_json(
                self._out_path("freeze.json")
            )["freeze_hash"],
            "verified_namespaces": deepcopy(verification["stage_reports"]),
            "private_protocol_freeze_sha256": verification[
                "private_protocol_freeze_sha256"
            ],
            "calibration_analysis_file_sha256": verification[
                "calibration_analysis_file_sha256"
            ],
            "private_plan_hash": verification["private_plan_hash"],
            "extension_entries_sha256": verification[
                "extension_entries_sha256"
            ],
        }

    def analyze_private(self):
        verification = self._verify_private_namespaces()
        inputs = deepcopy(self._private_confirmation_inputs(
            verification=verification
        ))
        confirmation = gates.evaluate_private_confirmation(
            inputs["criteria"],
            inputs["episodes_per_model"],
            inputs["extension_already_used"],
        )
        report = {
            "private_analysis_version": "charitroc-private-analysis-v1",
            "provenance": self.provenance,
            "provider": self.provider,
            "measurement_surface": "sealed-private-confirmation",
            "frozen_inputs": inputs,
            "private_confirmation": confirmation,
        }
        report["analysis_sha256"] = _canonical_sha(report)
        _write_or_validate(
            self._out_path(
                "reports",
                f"private-analysis-{inputs['episodes_per_model']}.json",
            ),
            report,
        )
        return report

    def activate_private_extension(self):
        activation_path = self._out_path(
            "reports", "private-extension-activation.json"
        )
        if activation_path.exists():
            raise ValueError("private extension already activated; one-time only")
        analysis = self.analyze_private()
        inputs = analysis.get("frozen_inputs", {})
        expected_confirmation = gates.evaluate_private_confirmation(
            inputs.get("criteria"),
            inputs.get("episodes_per_model"),
            inputs.get("extension_already_used"),
        )
        if (
            type(analysis) is not dict
            or analysis.get("private_analysis_version")
            != "charitroc-private-analysis-v1"
            or analysis.get("provenance") != self.provenance
            or analysis.get("provider") != self.provider
            or analysis.get("measurement_surface")
            != "sealed-private-confirmation"
            or analysis.get("analysis_sha256") != _canonical_sha(
                _without_hash(analysis, "analysis_sha256")
            )
            or inputs.get("episodes_per_model") != 96
            or inputs.get("extension_already_used") is not False
            or analysis.get("private_confirmation") != expected_confirmation
        ):
            raise ValueError("private analysis differs from verified inputs")
        confirmation = analysis.get("private_confirmation", {})
        if (
            confirmation.get("action") != "extend_to_192"
            or confirmation.get("extension_allowed") is not True
        ):
            raise ValueError("private analysis did not authorize extension")
        plan = self._plan("private")
        if len(plan["extension_entries"]) != 96:
            raise ValueError("private extension plan coverage is not exact")
        protocol = self._validate_private_protocol(
            _read_json(self._out_path("freeze.json"))
        )
        if (
            inputs.get("freeze_hash")
            != _read_json(self._out_path("freeze.json"))["freeze_hash"]
            or inputs.get("private_protocol_freeze_sha256")
            != protocol["protocol_freeze_sha256"]
            or inputs.get("calibration_analysis_file_sha256")
            != protocol["calibration_analysis_file_sha256"]
            or inputs.get("private_plan_hash")
            != plan["plan_hash"]
            or inputs.get("extension_entries_sha256")
            != _canonical_sha(plan["extension_entries"])
        ):
            raise ValueError("private analysis is not bound to the frozen protocol")
        payload = {
            "activation_version": "charitroc-private-extension-activation-v1",
            "namespace": "private-extension",
            "provenance": self.provenance,
            "provider": self.provider,
            "analysis_sha256": analysis["analysis_sha256"],
            "freeze_hash": analysis["frozen_inputs"]["freeze_hash"],
            "private_protocol_freeze_sha256": protocol[
                "protocol_freeze_sha256"
            ],
            "calibration_analysis_file_sha256": protocol[
                "calibration_analysis_file_sha256"
            ],
            "private_plan_hash": plan["plan_hash"],
            "extension_entries_sha256": _canonical_sha(
                plan["extension_entries"]
            ),
            "extension_occurrence_ids": [
                row["occurrence_id"] for row in plan["extension_entries"]
            ],
            "activated_at_utc": self._now(),
        }
        payload["activation_sha256"] = _canonical_sha(payload)
        _write_new_json(activation_path, payload)
        return payload


def build_parser():
    parser = argparse.ArgumentParser(
        description="Run the frozen CHARITROC Codex/OpenRouter panel"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in COMMANDS:
        child = subparsers.add_parser(command)
        child.add_argument("--out", required=True)
        child.add_argument("--provider", required=True, choices=PROVIDERS)
        child.add_argument("--run-mode", required=True, choices=RUN_MODES)
        if command == "access":
            child.add_argument("--retry-failed-access", action="store_true")
        if command == "verify":
            child.add_argument("--stage", choices=EXECUTION_STAGES)
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    if args.run_mode == "mock":
        raise SystemExit(
            "mock CLI execution has no hidden fake driver; use the explicit "
            "programmatic mock harness"
        )
    runner = PanelOrchestrator(
        bank_root=Path(__file__).resolve().parents[1],
        out_dir=args.out,
        provider=args.provider,
        run_mode=args.run_mode,
    )
    if args.command in EXECUTION_STAGES:
        result = runner.execute(args.command)
    elif args.command == "access":
        result = runner.access(
            retry_failed=args.retry_failed_access
        )
    elif args.command == "verify-access":
        result = runner.verify_access()
    elif args.command == "freeze":
        result = runner.freeze()
    elif args.command == "verify":
        result = runner.verify(args.stage)
    elif args.command == "analyze":
        result = runner.analyze()
    elif args.command == "analyze-private":
        result = runner.analyze_private()
    else:
        result = runner.activate_private_extension()
    sys.stdout.write(_canonical_bytes(result).decode("utf-8") + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
