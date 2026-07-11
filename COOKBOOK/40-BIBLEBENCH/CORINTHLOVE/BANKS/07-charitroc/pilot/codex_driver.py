"""Fail-closed Codex CLI driver for CHARITROC staged calibration.

The CLI's JSONL stream is preserved byte-for-byte (after strict UTF-8
decoding), while all semantic claims are rebuilt from a deliberately small
0.134.0 event grammar.  Model/provider/isolation claims come from the local
rollout record, because ``codex exec --json`` does not expose them in its
public event stream.
"""
from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import threading
import time
import uuid

from lib.payloads import model_turns
from pilot import contracts, manifest


MODULE_DIR = Path(__file__).resolve().parent
DEFAULT_SCHEMA_PATH = (MODULE_DIR / "response_schema.json").resolve()
EXPECTED_CODEX_CLI_VERSION = "0.134.0"
DISABLED_TOOL_FEATURES = (
    "shell_tool", "unified_exec", "apps", "enable_mcp_apps",
    "plugins", "plugin_sharing", "remote_plugin", "in_app_browser",
    "browser_use", "browser_use_external", "computer_use",
    "multi_agent", "multi_agent_v2", "enable_fanout",
    "child_agents_md", "image_generation", "workspace_dependencies",
    "tool_suggest", "tool_call_mcp_elicitation", "goals", "hooks",
    "artifact", "code_mode", "code_mode_only",
    "skill_mcp_dependency_install", "auth_elicitation",
    "request_permissions_tool", "shell_snapshot", "memories",
    "enable_request_compression",
)
CONTEXT_CONFIG_OVERRIDES = (
    "skills.include_instructions=false",
    "skills.bundled.enabled=false",
    "skills.config=[]",
    "include_permissions_instructions=false",
    "include_apps_instructions=false",
    "include_collaboration_mode_instructions=false",
    "include_environment_context=false",
)
CONTEXT_AUDIT_VERSION = "charitroc-codex-context-audit-v1"
CONTEXT_AUDIT_SENTINEL = "cx-context-audit-8b6f31d04a2e"
EXPECTED_CONTEXT_AUDIT_INPUT = [{
    "type": "message",
    "role": "user",
    "content": [{
        "type": "input_text", "text": CONTEXT_AUDIT_SENTINEL,
    }],
}]
CONTEXT_AUDIT_RECORD_KEYS = {
    "audit_version", "source", "provider_model_id", "isolation_dir",
    "context_profile_sha256", "sentinel_sha256", "argv_sha256",
    "raw_stdout_sha256", "rendered_input_sha256", "passed",
    "audit_sha256",
}
CONTEXT_PROFILE = {
    "strict_config": True,
    "ignore_user_config": True,
    "ignore_rules": True,
    "config_overrides": list(CONTEXT_CONFIG_OVERRIDES),
    "disabled_features": list(DISABLED_TOOL_FEATURES),
}
CONTEXT_PROFILE_SHA256 = contracts.canonical_sha256(CONTEXT_PROFILE)
CONTEXT_AUDIT_CONTRACT_SHA256 = contracts.canonical_sha256({
    "audit_version": CONTEXT_AUDIT_VERSION,
    "record_keys": sorted(CONTEXT_AUDIT_RECORD_KEYS),
    "sentinel_sha256": contracts.sha256_utf8(CONTEXT_AUDIT_SENTINEL),
    "expected_input_sha256": contracts.canonical_sha256(
        EXPECTED_CONTEXT_AUDIT_INPUT
    ),
})


def _live_context_contract_sha256():
    """Hash the live sources behind the frozen context/audit digests."""
    return contracts.canonical_sha256({
        "context_profile": CONTEXT_PROFILE,
        "audit_version": CONTEXT_AUDIT_VERSION,
        "record_keys": sorted(CONTEXT_AUDIT_RECORD_KEYS),
        "sentinel": CONTEXT_AUDIT_SENTINEL,
        "expected_input": EXPECTED_CONTEXT_AUDIT_INPUT,
        "config_overrides": list(CONTEXT_CONFIG_OVERRIDES),
        "disabled_features": list(DISABLED_TOOL_FEATURES),
    })


FROZEN_LIVE_CONTEXT_CONTRACT_SHA256 = _live_context_contract_sha256()
RAW_ATTESTATION_KEYS = {
    "source",
    "thread_id", "returned_provider_model_id", "returned_provider_name",
    "cli_version", "cwd", "sandbox", "reasoning_effort", "turn_count",
    "disabled_features", "rollout_path", "rollout_prefix_size",
    "rollout_prefix_sha256", "rollout_mtime_ns",
    "latest_context_timestamp_utc", "scanned_payload_sha256",
    "future_text_absent", "identifier_absent",
    "stage", "current_prompt_sha256", "current_prompt_linked",
    "final_response_sha256", "final_response_linked",
    "stage_evidence_sha256", "rollout_tools_absent",
    "rollout_tool_evidence_sha256",
}
ATTESTATION_RECORD_KEYS = RAW_ATTESTATION_KEYS | {
    "attestation_version", "invocation_started_at_utc",
    "observed_at_utc", "context_profile_sha256",
    "context_audit_sha256", "attestation_sha256",
}
TRANSPORT_DESCRIPTOR_KEYS = {
    "descriptor_version", "execution_id", "stage", "request_sha256",
    "provider_model_id", "configuration_id", "session_id", "cwd",
    "response_schema_path", "response_schema_sha256", "codex_binary",
    "disabled_features", "argv", "stdin_sha256",
    "run_mode", "runtime_identity", "context_profile_sha256",
    "context_audit",
}
RUNTIME_IDENTITY_KEYS = {
    "run_mode", "codex_binary", "codex_cli_version",
    "codex_binary_sha256", "codex_home", "disabled_features_sha256",
    "home", "context_profile_sha256", "context_audit_contract_sha256",
}
ATTESTATION_VERSION = "charitroc-codex-rollout-attestation-v1"
TRANSPORT_DESCRIPTOR_VERSION = "charitroc-codex-transport-v1"
_UNSET = object()
_THREAD_UUID_RE = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-7[0-9a-f]{3}-"
    r"[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
)
_TRANSPORT_ERROR_RE = re.compile(
    r"(?i)(?:transport|connection|network|timed?\s*out|timeout|"
    r"temporarily unavailable|rate.?limit|usage.?limit|\b429\b|\b503\b|"
    r"stream error)"
)
_FORBIDDEN_DIR_RE = re.compile(r"(?i)(?:CHARITROC|10CB-07|JUDGE-)")
_FORBIDDEN_IDENTIFIER_RE = re.compile(
    r"(?i)(?:10CB-07-|CHARITROC-[0-9]{4}|"
    r"JUDGE-[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-"
    r"[89ab][0-9a-f]{3}-[0-9a-f]{12})"
)
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
_CREDENTIAL_RE = re.compile(
    r"(?i)(?:\b(?:sk|rk)-[A-Za-z0-9_-]{8,}|"
    r"\bBearer\s+[A-Za-z0-9._~+/=-]+|\bOPENROUTER_API_KEY\s*=)"
)


class CodexDriverError(RuntimeError):
    """A safe driver failure whose text never includes provider evidence."""


class CodexPreTokenTransportError(CodexDriverError):
    """An executor-level, explicitly classified pre-token transport error."""


def _sha256_path(path):
    digest = hashlib.sha256()
    try:
        with Path(path).open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
    except OSError:
        raise CodexDriverError("production Codex binary cannot be hashed") from None
    return digest.hexdigest()


def _resolved_codex_home():
    root = os.environ.get("CODEX_HOME") or Path.home() / ".codex"
    return Path(root).expanduser().resolve()


def _resolve_production_codex_binary():
    located = shutil.which("codex")
    if not located:
        raise CodexDriverError("production Codex 0.134.0 is unavailable")
    path = Path(located).expanduser().resolve()
    if not path.is_absolute() or not path.is_file():
        raise CodexDriverError("production Codex 0.134.0 is unavailable")
    try:
        completed = subprocess.run(
            [str(path), "--version"], stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, check=False, timeout=10,
        )
    except (OSError, subprocess.SubprocessError):
        raise CodexDriverError("production Codex version cannot be verified") from None
    try:
        version_line = completed.stdout.decode("utf-8", errors="strict").strip()
    except UnicodeError:
        raise CodexDriverError("production Codex version cannot be verified") from None
    if completed.returncode != 0 or version_line != "codex-cli 0.134.0":
        raise CodexDriverError("production Codex must be exactly 0.134.0")
    return path, EXPECTED_CODEX_CLI_VERSION, _sha256_path(path)


@dataclass(frozen=True)
class ExecutionOutcome:
    """Detached output from one CLI process invocation."""

    stdout_chunks: tuple
    stderr: bytes
    exit_status: int


@dataclass(frozen=True)
class EpisodeAttempt:
    """One fresh-session execution of as much of an episode as is valid."""

    execution_id: str
    isolation_dir: Path
    requests: list
    results: list
    transport_descriptors: list
    attestations: list
    chain: object


@dataclass(frozen=True)
class CodexEpisodeRun:
    """Initial execution and, only when authorized, one integrity rerun."""

    attempts: tuple
    authorization: object = None

    @property
    def final(self):
        return self.attempts[-1]

    @property
    def execution_id(self):
        return self.final.execution_id

    @property
    def isolation_dir(self):
        return self.final.isolation_dir

    @property
    def requests(self):
        return self.final.requests

    @property
    def results(self):
        return self.final.results

    @property
    def transport_descriptors(self):
        return self.final.transport_descriptors

    @property
    def attestations(self):
        return self.final.attestations

    @property
    def chain(self):
        return self.final.chain


@dataclass(frozen=True)
class _ParsedTrace:
    session_id: object
    token_emission_started: bool
    raw_final_message: object
    usage: dict
    reasoning_details: object
    tool_events: list
    error_code: object
    finish_reason: object
    trace_valid: bool
    explicit_pre_token_transport_error: bool


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def _strict_json_line(line):
    try:
        value = json.loads(
            line,
            object_pairs_hook=_unique_object,
            parse_constant=lambda _value: (_ for _ in ()).throw(
                ValueError("non-finite JSON constant")
            ),
        )
    except (json.JSONDecodeError, TypeError, ValueError):
        raise ValueError("invalid unique-key JSON event") from None
    if type(value) is not dict:
        raise ValueError("event is not an object")
    return value


def _strict_json_document(raw):
    if type(raw) is not bytes:
        raise ValueError("JSON document is not binary evidence")
    try:
        text = raw.decode("utf-8", errors="strict")
        return json.loads(
            text,
            object_pairs_hook=_unique_object,
            parse_constant=lambda _value: (_ for _ in ()).throw(
                ValueError("non-finite JSON constant")
            ),
        )
    except (UnicodeError, json.JSONDecodeError, TypeError, ValueError):
        raise ValueError("invalid unique-key JSON document") from None


def _without_context_audit_hash(record):
    return {
        key: value for key, value in record.items()
        if key != "audit_sha256"
    }


def _validate_context_audit(record):
    contracts.canonical_json_bytes(record)
    if type(record) is not dict or set(record) != CONTEXT_AUDIT_RECORD_KEYS:
        raise ValueError("context audit keys are not exact")
    if record["audit_version"] != CONTEXT_AUDIT_VERSION:
        raise ValueError("context audit version differs")
    if record["source"] not in {"mock", "codex-debug-prompt-input"}:
        raise ValueError("context audit source is invalid")
    if record["passed"] is not (
            record["source"] == "codex-debug-prompt-input"):
        raise ValueError("context audit source/pass claim differs")
    if (
        type(record["provider_model_id"]) is not str
        or record["provider_model_id"] not in (
            *manifest.MODEL_LOGICAL_IDS, "unverified"
        )
        or (
            record["source"] == "codex-debug-prompt-input"
            and record["provider_model_id"] == "unverified"
        )
    ):
        raise ValueError("context audit model identity is invalid")
    if (
        type(record["isolation_dir"]) is not str
        or not Path(record["isolation_dir"]).is_absolute()
    ):
        raise ValueError("context audit isolation directory is invalid")
    if record["context_profile_sha256"] != CONTEXT_PROFILE_SHA256:
        raise ValueError("context audit profile hash differs")
    for field in (
            "sentinel_sha256", "argv_sha256", "raw_stdout_sha256",
            "rendered_input_sha256"):
        if (
            type(record[field]) is not str
            or _SHA256_RE.fullmatch(record[field]) is None
        ):
            raise ValueError("context audit digest is invalid")
    if record["sentinel_sha256"] != contracts.sha256_utf8(
            CONTEXT_AUDIT_SENTINEL):
        raise ValueError("context audit sentinel hash differs")
    expected_rendered_hash = contracts.canonical_sha256(
        EXPECTED_CONTEXT_AUDIT_INPUT
        if record["source"] == "codex-debug-prompt-input" else []
    )
    if record["rendered_input_sha256"] != expected_rendered_hash:
        raise ValueError("context audit rendered-input hash differs")
    if record["source"] == "mock" and (
        record["argv_sha256"] != contracts.canonical_sha256([])
        or record["raw_stdout_sha256"] != hashlib.sha256(b"").hexdigest()
    ):
        raise ValueError("mock context audit evidence is not empty")
    if (
        type(record["audit_sha256"]) is not str
        or record["audit_sha256"] != contracts.canonical_sha256(
            _without_context_audit_hash(record)
        )
    ):
        raise ValueError("context audit hash differs")
    return deepcopy(record)


def _usage_or_null():
    return {
        "input_tokens": None,
        "cached_input_tokens": None,
        "output_tokens": None,
        "reasoning_tokens": None,
        "total_tokens": None,
    }


def _valid_thread_id(value):
    if type(value) is not str or _THREAD_UUID_RE.fullmatch(value) is None:
        return False
    try:
        parsed = uuid.UUID(value)
    except (ValueError, AttributeError):
        return False
    return parsed.version == 7 and parsed.variant == uuid.RFC_4122


def _validate_stage_hooks(before_stage, stage_sink):
    for name, callback in (
            ("before_stage", before_stage), ("stage_sink", stage_sink)):
        if callback is not None and not callable(callback):
            raise CodexDriverError(f"{name} must be callable or None")


def _emit_stage_hook(
        callback, *, integrity_session, request, transport_descriptor,
        attestation, result=_UNSET):
    if callback is None:
        return
    event = {
        "provider": "codex",
        "integrity_session": integrity_session,
        "execution_id": request["execution_id"],
        "stage": request["stage"],
        "request": deepcopy(request),
        "transport_descriptor": deepcopy(transport_descriptor),
        "attestation": deepcopy(attestation),
    }
    if result is not _UNSET:
        event["result"] = deepcopy(result)
    callback(event)


def _parse_usage(value, *, response_present):
    expected = {
        "input_tokens", "cached_input_tokens", "output_tokens",
        "reasoning_output_tokens",
    }
    if type(value) is not dict or set(value) != expected:
        raise ValueError("usage keys differ from Codex 0.134.0")
    if any(type(value[key]) is not int or value[key] < 0 for key in expected):
        raise ValueError("usage counts must be non-negative integers")
    if value["cached_input_tokens"] > value["input_tokens"]:
        raise ValueError("cached input exceeds total input")
    if value["reasoning_output_tokens"] > value["output_tokens"]:
        raise ValueError("reasoning output exceeds total output")
    if response_present and value["output_tokens"] <= 0:
        raise ValueError("a final response requires positive output tokens")
    return {
        "input_tokens": value["input_tokens"],
        "cached_input_tokens": value["cached_input_tokens"],
        "output_tokens": value["output_tokens"],
        "reasoning_tokens": value["reasoning_output_tokens"],
        "total_tokens": value["input_tokens"] + value["output_tokens"],
    }


class _IncrementalJsonlParser:
    """Strict state machine for the documented Codex 0.134.0 JSONL shape."""

    def __init__(self):
        self.buffer = b""
        self.events = []
        self.failed = False

    def feed(self, chunk):
        if type(chunk) is not bytes:
            self.failed = True
            return
        self.buffer += chunk
        while b"\n" in self.buffer:
            line, self.buffer = self.buffer.split(b"\n", 1)
            if not line:
                self.failed = True
                continue
            try:
                self.events.append(_strict_json_line(line))
            except ValueError:
                self.failed = True

    def finish(self):
        if self.buffer:
            # A JSONL trace without the final delimiter is incomplete even if
            # the residual text happens to parse as JSON.
            self.failed = True
        return self._project()

    def _project(self):
        session_id = None
        token_started = False
        raw_final = None
        usage = _usage_or_null()
        reasoning = []
        tools = []
        error_code = None
        finish_reason = None
        valid = not self.failed
        phase = "thread"
        terminal_seen = False
        stream_error_message = None
        stream_error_confirmation_seen = False
        item_states = {}
        completed_items = []
        retryable_transport = False

        for event in self.events:
            event_type = event.get("type")
            if terminal_seen:
                # Codex 0.134.0 emits a stream-level ``error`` immediately
                # followed by a matching ``turn.failed`` for quota failures.
                # Treat that exact pair as one terminal failure. Any mismatch
                # or further event revokes retry eligibility.
                matching_turn_failure = (
                    stream_error_message is not None
                    and not stream_error_confirmation_seen
                    and event_type == "turn.failed"
                    and set(event) == {"type", "error"}
                    and type(event.get("error")) is dict
                    and set(event["error"]) == {"message"}
                    and event["error"].get("message")
                    == stream_error_message
                )
                if matching_turn_failure:
                    stream_error_confirmation_seen = True
                    continue
                retryable_transport = False
                valid = False
                continue
            if event_type == "thread.started":
                if (
                    phase != "thread"
                    or set(event) != {"type", "thread_id"}
                    or not _valid_thread_id(event["thread_id"])
                ):
                    valid = False
                else:
                    session_id = event["thread_id"]
                    phase = "turn"
                continue
            if event_type == "turn.started":
                if phase != "turn" or set(event) != {"type"}:
                    valid = False
                else:
                    phase = "items"
                continue
            if event_type in {"item.started", "item.updated", "item.completed"}:
                if phase != "items" or set(event) != {"type", "item"}:
                    valid = False
                    continue
                item = event.get("item")
                if (
                    type(item) is not dict
                    or type(item.get("id")) is not str
                    or not item.get("id")
                    or type(item.get("type")) is not str
                ):
                    valid = False
                    continue
                token_started = True
                item_type = item["type"]
                item_id = item["id"]
                prior_item = item_states.get(item_id)
                lifecycle_ok = True
                if event_type == "item.started":
                    if prior_item is not None:
                        lifecycle_ok = False
                    else:
                        item_states[item_id] = (item_type, "started")
                elif event_type == "item.updated":
                    if (
                        prior_item is None
                        or prior_item[0] != item_type
                        or prior_item[1] != "started"
                    ):
                        lifecycle_ok = False
                else:
                    if prior_item is not None and (
                        prior_item[0] != item_type
                        or prior_item[1] == "completed"
                    ):
                        lifecycle_ok = False
                    item_states[item_id] = (item_type, "completed")
                    completed_items.append((item_id, item_type))
                if not lifecycle_ok:
                    valid = False
                if item_type == "reasoning":
                    if (
                        set(item) != {"id", "type", "text"}
                        or type(item["text"]) is not str
                    ):
                        valid = False
                    elif event_type == "item.completed":
                        reasoning.append(dict(item))
                elif item_type == "agent_message":
                    if (
                        set(item) != {"id", "type", "text"}
                        or type(item["text"]) is not str
                        or event_type != "item.completed"
                        or raw_final is not None
                    ):
                        valid = False
                    else:
                        raw_final = item["text"]
                elif item_type == "error":
                    if (
                        set(item) != {"id", "type", "message"}
                        or type(item["message"]) is not str
                    ):
                        valid = False
                    error_code = "codex_item_error"
                    valid = False
                else:
                    # Any command, patch, MCP, collaboration, web, todo, or
                    # future unknown item is model tool activity and therefore
                    # an integrity failure. Preserve the exact decoded event.
                    tools.append(event)
                continue
            if event_type == "turn.completed":
                if phase != "items" or set(event) != {"type", "usage"}:
                    valid = False
                try:
                    usage = _parse_usage(
                        event.get("usage"), response_present=raw_final is not None
                    )
                except ValueError:
                    valid = False
                if raw_final is None:
                    valid = False
                if any(
                        state != "completed"
                        for _item_type, state in item_states.values()):
                    valid = False
                agent_items = [
                    item for item in completed_items if item[1] == "agent_message"
                ]
                if (
                    len(agent_items) != 1
                    or not completed_items
                    or completed_items[-1] != agent_items[0]
                ):
                    valid = False
                terminal_seen = True
                finish_reason = "stop"
                phase = "terminal"
                continue
            if event_type == "turn.failed":
                message = None
                well_formed_error = (
                    phase == "items"
                    and set(event) == {"type", "error"}
                    and type(event.get("error")) is dict
                    and set(event["error"]) == {"message"}
                    and type(event["error"]["message"]) is str
                )
                if well_formed_error:
                    message = event["error"]["message"]
                else:
                    valid = False
                retryable_transport = bool(
                    valid and well_formed_error and not token_started
                    and _TRANSPORT_ERROR_RE.search(message)
                )
                error_code = (
                    "pre_token_transport_error"
                    if message is not None and not token_started
                    and _TRANSPORT_ERROR_RE.search(message)
                    else "codex_turn_failed"
                )
                terminal_seen = True
                finish_reason = "error"
                valid = False
                phase = "terminal"
                continue
            if event_type == "error":
                message = event.get("message")
                well_formed_error = not (
                    phase != "items"
                    or set(event) != {"type", "message"}
                    or type(message) is not str
                )
                if not well_formed_error:
                    valid = False
                    message = None
                retryable_transport = bool(
                    valid and well_formed_error and not token_started
                    and _TRANSPORT_ERROR_RE.search(message)
                )
                error_code = (
                    "pre_token_transport_error"
                    if message is not None and not token_started
                    and _TRANSPORT_ERROR_RE.search(message)
                    else "codex_stream_error"
                )
                terminal_seen = True
                stream_error_message = message
                finish_reason = "error"
                valid = False
                phase = "terminal"
                continue
            valid = False

        if not terminal_seen or phase != "terminal":
            valid = False
        explicit_transport = (
            retryable_transport
            and error_code == "pre_token_transport_error"
            and not token_started
            and raw_final is None
        )
        return _ParsedTrace(
            session_id=session_id,
            token_emission_started=token_started,
            raw_final_message=raw_final,
            usage=usage,
            reasoning_details=reasoning,
            tool_events=tools,
            error_code=error_code,
            finish_reason=finish_reason,
            trace_valid=valid,
            explicit_pre_token_transport_error=explicit_transport,
        )


class SubprocessExecutor:
    """Default no-shell binary executor; no newline normalization occurs."""

    def __call__(self, argv, *, stdin, cwd):
        process = subprocess.Popen(
            list(argv),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=str(cwd),
        )
        stderr_parts = []

        def drain_stderr():
            try:
                for part in process.stderr:
                    stderr_parts.append(part)
            except OSError:
                stderr_parts.append(b"")

        stderr_thread = threading.Thread(target=drain_stderr, daemon=True)
        stderr_thread.start()
        try:
            process.stdin.write(stdin.encode("utf-8", errors="strict"))
            process.stdin.close()
            chunks = tuple(process.stdout)
            exit_status = process.wait()
            stderr_thread.join()
        except Exception:
            process.kill()
            process.wait()
            stderr_thread.join()
            raise
        return ExecutionOutcome(
            stdout_chunks=chunks,
            stderr=b"".join(stderr_parts),
            exit_status=exit_status,
        )


def _iter_text(value):
    if type(value) is str:
        yield value
    elif type(value) is list:
        for item in value:
            yield from _iter_text(item)
    elif type(value) is dict:
        for key, item in value.items():
            yield key
            yield from _iter_text(item)


def _contains_forbidden_identifier(value):
    return any(_FORBIDDEN_IDENTIFIER_RE.search(text) is not None
               for text in _iter_text(value))


def _parse_rollout_bytes(raw):
    if type(raw) is not bytes or not raw or not raw.endswith(b"\n"):
        raise ValueError("rollout is not complete binary JSONL")
    records = []
    for line in raw.splitlines(keepends=True):
        if not line.endswith(b"\n"):
            raise ValueError("rollout line is incomplete")
        records.append(_strict_json_line(line[:-1]))
    return records


def _stage_rollout_windows(records):
    context_indexes = [
        index for index, record in enumerate(records)
        if record.get("type") == "turn_context"
    ]
    if not context_indexes:
        raise ValueError("rollout has no stage context")
    current_context = context_indexes[-1]
    # Codex 0.134.0 writes the current ``turn_context`` before that turn's
    # user and assistant response items. The stage-local evidence window is
    # therefore the suffix after the latest context, not the prefix before it.
    current_window = records[current_context + 1:]
    return (
        current_window,
        current_window,
        records[current_context:],
    )


def _stage_rollout_segment(records):
    return _stage_rollout_windows(records)[2]


def _contains_exact_text(value, expected):
    return type(expected) is str and any(
        text == expected for text in _iter_text(value)
    )


def _unique_role_message_link(records, role, expected):
    if type(expected) is not str:
        return False
    messages = []
    for record in records:
        payload = record.get("payload")
        if (
            type(payload) is dict
            and payload.get("type") == "message"
            and payload.get("role") == role
        ):
            messages.append(payload)
    return (
        len(messages) == 1
        and _contains_exact_text(messages[0].get("content"), expected)
    )


def _terminal_assistant_response_link(records, expected):
    """Bind the response to the sole terminal assistant response item."""
    if type(expected) is not str:
        return False
    response_items = [
        record for record in records
        if record.get("type") == "response_item"
    ]
    if not response_items:
        return False
    message_payloads = [
        record.get("payload") for record in response_items
        if type(record.get("payload")) is dict
        and record["payload"].get("type") == "message"
    ]
    assistant_messages = [
        payload for payload in message_payloads
        if payload.get("role") == "assistant"
    ]
    terminal = response_items[-1].get("payload")
    return (
        len(assistant_messages) == 1
        and type(terminal) is dict
        and terminal.get("type") == "message"
        and terminal.get("role") == "assistant"
        and terminal is assistant_messages[0]
        and _contains_exact_text(terminal.get("content"), expected)
    )


_TOOL_ACTIVITY_MARKERS = (
    "function_call", "custom_tool_call", "tool_call", "tool_use",
    "function", "command", "command_execution",
    "exec_command", "local_shell", "shell_call", "mcp_call", "mcp_tool",
    "app_call", "app", "browser", "computer", "web_search",
    "workspace_tool",
)
_INERT_TOOL_MARKERS = (
    "definition", "definitions", "schema", "catalog", "available",
    "capability", "config",
)
_TOOL_STRUCTURAL_KEYS = {
    "arguments", "input", "call_id", "tool_name",
    "function", "function_call", "custom_tool_call",
    "tool_call", "tool_calls", "tool_use",
}


def _contains_tool_structure(value):
    if type(value) is dict:
        return bool(set(value) & _TOOL_STRUCTURAL_KEYS) or any(
            _contains_tool_structure(item) for item in value.values()
        )
    if type(value) is list:
        return any(_contains_tool_structure(item) for item in value)
    return False


def _rollout_tool_evidence(records):
    evidence = []
    for index, record in enumerate(records):
        record_type = record.get("type")
        payload = record.get("payload")
        payload = payload if type(payload) is dict else {}
        discriminators = [
            record_type, payload.get("type"), payload.get("kind"),
            payload.get("event_type"), payload.get("name"),
        ]
        normalized = [
            value.lower() for value in discriminators if type(value) is str
        ]
        if record_type in {"session_meta", "turn_context"}:
            normalized = normalized[:1]
        active = payload.get("role") == "tool" or (
            record_type not in {"session_meta", "turn_context"}
            and _contains_tool_structure(payload)
        )
        for value in normalized:
            if any(marker in value for marker in _TOOL_ACTIVITY_MARKERS):
                active = True
        if active:
            evidence.append({
                "record_index": index,
                "record_sha256": contracts.canonical_sha256(record),
            })
            continue
        if any(
                marker in value for value in normalized
                for marker in _INERT_TOOL_MARKERS):
            continue
    return evidence


class CodexRolloutAttestor:
    """Hash-bind and project safe evidence from the persisted rollout prefix."""

    def __init__(self, codex_home=None):
        root = codex_home if codex_home is not None else _resolved_codex_home()
        self.codex_home = Path(root).expanduser().resolve()
        self.sessions_root = self.codex_home / "sessions"

    def _safe_rollout_path(self, path):
        candidate = Path(path).expanduser()
        if not candidate.is_absolute():
            raise CodexDriverError("rollout is outside production root")
        try:
            candidate.relative_to(self.sessions_root)
        except ValueError:
            raise CodexDriverError("rollout is outside production root") from None
        cursor = candidate
        while True:
            if cursor.is_symlink():
                raise CodexDriverError("rollout has a symlink ancestor")
            if cursor == self.sessions_root:
                break
            if cursor.parent == cursor:
                raise CodexDriverError("rollout is outside production root")
            cursor = cursor.parent
        if not candidate.is_file():
            raise CodexDriverError("Codex rollout attestation is unavailable")
        resolved = candidate.resolve()
        try:
            resolved.relative_to(self.sessions_root)
        except ValueError:
            raise CodexDriverError("rollout is outside production root") from None
        return resolved

    def _project(self, path, *, future_turns, current_prompt,
                 expected_response, prefix_size=None):
        resolved = self._safe_rollout_path(path)
        try:
            stat = resolved.stat()
            with resolved.open("rb") as handle:
                raw = handle.read() if prefix_size is None else handle.read(prefix_size)
            if prefix_size is not None and len(raw) != prefix_size:
                raise ValueError("short rollout prefix")
            records = _parse_rollout_bytes(raw)
            payloads = [
                record["payload"] for record in records if "payload" in record
            ]
            meta_rows = [
                record for record in records
                if record.get("type") == "session_meta"
                and type(record.get("payload")) is dict
            ]
            contexts = [
                record for record in records
                if record.get("type") == "turn_context"
                and type(record.get("payload")) is dict
            ]
            if len(meta_rows) != 1 or not contexts:
                raise ValueError("rollout metadata is incomplete")
            meta = meta_rows[0]["payload"]
            current_record = contexts[-1]
            current = current_record["payload"]
            prompt_window, response_window, segment = (
                _stage_rollout_windows(records)
            )
            segment_payloads = [
                record["payload"] for record in segment if "payload" in record
            ]
            tool_evidence = _rollout_tool_evidence(segment)
        except (OSError, ValueError, UnicodeError):
            raise CodexDriverError("Codex rollout attestation is unavailable") from None
        sandbox = current.get("sandbox_policy")
        if type(sandbox) is dict:
            sandbox = sandbox.get("type")
        return {
            "thread_id": meta.get("id"),
            "returned_provider_model_id": (
                current.get("model")
                if type(current.get("model")) is str else "unverified"
            ),
            "returned_provider_name": (
                "OpenAI" if meta.get("model_provider") == "openai"
                else "unverified"
            ),
            "cli_version": meta.get("cli_version"),
            "cwd": current.get("cwd"),
            "sandbox": sandbox,
            "reasoning_effort": current.get("effort"),
            "turn_count": len(contexts),
            "rollout_path": str(resolved),
            "rollout_prefix_size": len(raw),
            "rollout_prefix_sha256": hashlib.sha256(raw).hexdigest(),
            "rollout_mtime_ns": stat.st_mtime_ns,
            "latest_context_timestamp_utc": current_record.get("timestamp"),
            "scanned_payload_sha256": contracts.canonical_sha256(payloads),
            "future_text_absent": not _contains_future_material(
                payloads, future_turns
            ),
            "identifier_absent": not _contains_forbidden_identifier(payloads),
            "current_prompt_sha256": contracts.sha256_utf8(current_prompt),
            "current_prompt_linked": _unique_role_message_link(
                prompt_window, "user", current_prompt
            ),
            "final_response_sha256": (
                contracts.sha256_utf8(expected_response)
                if expected_response is not None else None
            ),
            "final_response_linked": (
                _terminal_assistant_response_link(
                    response_window, expected_response
                )
                if expected_response is not None else False
            ),
            "stage_evidence_sha256": contracts.canonical_sha256(
                segment_payloads
            ),
            "rollout_tools_absent": not tool_evidence,
            "rollout_tool_evidence_sha256": contracts.canonical_sha256(
                tool_evidence
            ),
        }

    def __call__(self, session_id, *, stage, requested_model,
                 isolation_dir, started_at_utc, observed_at_utc,
                 future_turns, required_disabled_features,
                 current_prompt, expected_response):
        del requested_model, isolation_dir, started_at_utc, observed_at_utc
        candidates = list(self.sessions_root.glob(
            "*/*/*/rollout-*{}*.jsonl".format(session_id)
        ))
        if len(candidates) != 1:
            raise CodexDriverError("Codex rollout attestation is unavailable")
        projection = self._project(
            candidates[0], future_turns=future_turns,
            current_prompt=current_prompt, expected_response=expected_response,
        )
        if projection["thread_id"] != session_id:
            raise CodexDriverError("Codex rollout thread differs")
        return {
            "source": "rollout",
            **projection,
            "disabled_features": list(required_disabled_features),
            "stage": stage,
        }

    def rederive_attestation(
            self, record, *, future_turns, current_prompt, expected_response):
        if type(record) is not dict or record.get("source") != "rollout":
            raise CodexDriverError("rollout attestation source differs")
        projection = self._project(
            record.get("rollout_path"), future_turns=future_turns,
            current_prompt=current_prompt, expected_response=expected_response,
            prefix_size=record.get("rollout_prefix_size"),
        )
        path = self._safe_rollout_path(record.get("rollout_path"))
        stat = path.stat()
        if (
            stat.st_size < record["rollout_prefix_size"]
            or stat.st_mtime_ns < record["rollout_mtime_ns"]
            or (
                stat.st_size == record["rollout_prefix_size"]
                and stat.st_mtime_ns != record["rollout_mtime_ns"]
            )
        ):
            raise CodexDriverError("rollout prefix mtime differs")
        projection["rollout_mtime_ns"] = record["rollout_mtime_ns"]
        return projection


def _timestamp(value):
    if not isinstance(value, datetime):
        raise CodexDriverError("clock must return a datetime")
    if value.tzinfo is None:
        raise CodexDriverError("clock must return a timezone-aware datetime")
    return value.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _parse_timestamp(value):
    if type(value) is not str:
        raise ValueError("timestamp is not text")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        raise ValueError("timestamp is invalid") from None
    if parsed.tzinfo is None:
        raise ValueError("timestamp lacks a timezone")
    return parsed.astimezone(timezone.utc)


def _without_attestation_hash(record):
    return {
        key: value for key, value in record.items()
        if key != "attestation_sha256"
    }


def _finalize_attestation(
        raw, started_at_utc, observed_at_utc, *, context_profile_sha256,
        context_audit_sha256):
    if type(raw) is not dict or set(raw) != RAW_ATTESTATION_KEYS:
        raise ValueError("rollout attestation raw keys are not exact")
    contracts.canonical_json_bytes(raw)
    if raw["source"] not in {"mock", "rollout", "unavailable"}:
        raise ValueError("rollout attestation source is invalid")
    if type(raw["disabled_features"]) is not list or raw[
            "disabled_features"] != list(DISABLED_TOOL_FEATURES):
        raise ValueError("rollout attestation feature list differs")
    for field in (
            "future_text_absent", "identifier_absent",
            "current_prompt_linked", "final_response_linked",
            "rollout_tools_absent"):
        if type(raw[field]) is not bool:
            raise ValueError("rollout scan evidence is not boolean")
    for field in (
            "rollout_prefix_sha256", "scanned_payload_sha256",
            "current_prompt_sha256", "stage_evidence_sha256",
            "rollout_tool_evidence_sha256"):
        if type(raw[field]) is not str or _SHA256_RE.fullmatch(raw[field]) is None:
            raise ValueError("rollout attestation digest is invalid")
    if raw["final_response_sha256"] is not None and (
            type(raw["final_response_sha256"]) is not str
            or _SHA256_RE.fullmatch(raw["final_response_sha256"]) is None):
        raise ValueError("rollout response digest is invalid")
    if raw["stage"] not in contracts.STAGES:
        raise ValueError("rollout attestation stage is invalid")
    for field in ("rollout_prefix_size", "rollout_mtime_ns"):
        if type(raw[field]) is not int or raw[field] < 0:
            raise ValueError("rollout attestation integer is invalid")
    if raw["rollout_path"] is not None and type(raw["rollout_path"]) is not str:
        raise ValueError("rollout attestation path is invalid")
    serialized = contracts.canonical_json_bytes(raw).decode("utf-8")
    if _CREDENTIAL_RE.search(serialized) is not None:
        raise ValueError("rollout attestation contains credential material")
    record = dict(raw)
    record.update({
        "attestation_version": ATTESTATION_VERSION,
        "invocation_started_at_utc": started_at_utc,
        "observed_at_utc": observed_at_utc,
        "context_profile_sha256": context_profile_sha256,
        "context_audit_sha256": context_audit_sha256,
    })
    for field in ("context_profile_sha256", "context_audit_sha256"):
        if type(record[field]) is not str or _SHA256_RE.fullmatch(
                record[field]) is None:
            raise ValueError("rollout context digest is invalid")
    record["attestation_sha256"] = contracts.canonical_sha256(record)
    if set(record) != ATTESTATION_RECORD_KEYS:
        raise ValueError("rollout attestation record keys are not exact")
    return record


def _contains_future_material(value, future_turns):
    if value is None:
        return False
    if type(value) is str:
        for turn in future_turns:
            text = turn["content"]
            if text in value or contracts.sha256_utf8(text) in value:
                return True
        return False
    if type(value) is list:
        return any(_contains_future_material(item, future_turns) for item in value)
    if type(value) is dict:
        return any(_contains_future_material(item, future_turns)
                   for item in value.values())
    return False


class CodexDriver:
    """Execute the frozen Codex panel without hidden context or repair turns."""

    def __init__(
            self, *, run_mode="mock", executor=_UNSET, attestor=_UNSET,
            clock=_UNSET, uuid_factory=_UNSET, tempdir_factory=_UNSET,
            sleeper=_UNSET, codex_binary=_UNSET,
            response_schema_path=_UNSET):
        injected = {
            "executor": executor, "attestor": attestor, "clock": clock,
            "uuid_factory": uuid_factory,
            "tempdir_factory": tempdir_factory, "sleeper": sleeper,
            "codex_binary": codex_binary,
            "response_schema_path": response_schema_path,
        }
        if run_mode == "codex":
            if any(value is not _UNSET for value in injected.values()):
                raise CodexDriverError(
                    "production Codex mode forbids injected dependencies"
                )
            binary_path, binary_version, binary_sha256 = (
                _resolve_production_codex_binary()
            )
            codex_home = _resolved_codex_home()
            executor = SubprocessExecutor()
            attestor = CodexRolloutAttestor(codex_home)
            clock = lambda: datetime.now(timezone.utc)
            uuid_factory = uuid.uuid4
            tempdir_factory = lambda: Path(tempfile.mkdtemp(prefix="cx-"))
            sleeper = time.sleep
            codex_binary = str(binary_path)
            response_schema_path = DEFAULT_SCHEMA_PATH
        elif run_mode == "mock":
            if (
                executor is _UNSET or attestor is _UNSET
                or not callable(executor) or not callable(attestor)
            ):
                raise CodexDriverError(
                    "mock mode requires explicit executor and attestor"
                )
            clock = (
                (lambda: datetime.now(timezone.utc))
                if clock is _UNSET else clock
            )
            uuid_factory = uuid.uuid4 if uuid_factory is _UNSET else uuid_factory
            tempdir_factory = (
                (lambda: Path(tempfile.mkdtemp(prefix="cx-")))
                if tempdir_factory is _UNSET else tempdir_factory
            )
            sleeper = (lambda _delay: None) if sleeper is _UNSET else sleeper
            codex_binary = "codex" if codex_binary is _UNSET else codex_binary
            response_schema_path = (
                DEFAULT_SCHEMA_PATH
                if response_schema_path is _UNSET else response_schema_path
            )
        else:
            raise CodexDriverError("run_mode must be mock or codex")

        self.run_mode = run_mode
        self.executor = executor
        self.attestor = attestor
        self.clock = clock
        self.uuid_factory = uuid_factory
        self.tempdir_factory = tempdir_factory
        self.sleeper = sleeper
        self.codex_binary = str(codex_binary)
        self.disabled_features = tuple(DISABLED_TOOL_FEATURES)
        self.codex_cli_version = (
            binary_version if run_mode == "codex" else "mock"
        )
        self.codex_binary_sha256 = (
            binary_sha256 if run_mode == "codex" else None
        )
        self.codex_home = (
            codex_home if run_mode == "codex"
            else (
                self.attestor.codex_home
                if type(self.attestor) is CodexRolloutAttestor else None
            )
        )
        self.home = Path.home().expanduser().resolve()
        self.response_schema_path = Path(response_schema_path).resolve()
        self.runtime_identity = {
            "run_mode": self.run_mode,
            "codex_binary": self.codex_binary,
            "codex_cli_version": self.codex_cli_version,
            "codex_binary_sha256": self.codex_binary_sha256,
            "codex_home": (
                str(self.codex_home) if self.codex_home is not None else None
            ),
            "home": str(self.home),
            "disabled_features_sha256": contracts.canonical_sha256(
                list(self.disabled_features)
            ),
            "context_profile_sha256": CONTEXT_PROFILE_SHA256,
            "context_audit_contract_sha256": CONTEXT_AUDIT_CONTRACT_SHA256,
        }
        self._used_isolation_dirs = set()
        self.context_audits = {}
        self.last_transport_request_sha256 = None
        self.last_transport_descriptor = None
        self.last_rollout_attestation = None
        self._production_fingerprint = None
        if self.run_mode == "codex":
            self._production_fingerprint = self._runtime_fingerprint()
        if not self.response_schema_path.is_file():
            raise CodexDriverError("frozen response schema is unavailable")
        loaded = manifest.load_response_schema()
        if contracts.canonical_sha256(loaded) != contracts.canonical_sha256(
                manifest.EXPECTED_RESPONSE_SCHEMA):
            raise CodexDriverError("frozen response schema is inconsistent")

    def _runtime_fingerprint(self):
        return (
            id(self.executor), id(self.attestor), id(self.clock),
            id(self.uuid_factory), id(self.tempdir_factory), id(self.sleeper),
            self.codex_binary, str(self.response_schema_path),
            type(self.executor), type(self.attestor), self.run_mode,
            self.codex_cli_version, self.codex_binary_sha256,
            str(self.codex_home), str(self.home), self.disabled_features,
            tuple(DISABLED_TOOL_FEATURES),
            tuple(CONTEXT_CONFIG_OVERRIDES), CONTEXT_PROFILE_SHA256,
            CONTEXT_AUDIT_CONTRACT_SHA256, id(self.context_audits),
            FROZEN_LIVE_CONTEXT_CONTRACT_SHA256,
            _live_context_contract_sha256(),
            contracts.canonical_sha256({
                str(path): audit
                for path, audit in self.context_audits.items()
            }),
            str(getattr(self.attestor, "codex_home", None)),
            str(getattr(self.attestor, "sessions_root", None)),
            contracts.canonical_sha256(self.runtime_identity),
        )

    def _assert_production_dependencies(self):
        if self.run_mode == "codex":
            try:
                current_fingerprint = self._runtime_fingerprint()
            except Exception:
                raise CodexDriverError(
                    "production Codex dependencies were mutated"
                ) from None
            if (
                self._production_fingerprint is None
                or current_fingerprint != self._production_fingerprint
                or type(self.executor) is not SubprocessExecutor
                or type(self.attestor) is not CodexRolloutAttestor
                or tuple(DISABLED_TOOL_FEATURES) != self.disabled_features
                or _live_context_contract_sha256()
                != FROZEN_LIVE_CONTEXT_CONTRACT_SHA256
                or self.attestor.codex_home != self.codex_home
                or self.attestor.sessions_root
                != self.codex_home / "sessions"
            ):
                raise CodexDriverError(
                    "production Codex dependencies were mutated"
                )
            located = shutil.which("codex")
            if (
                not located
                or Path(located).resolve() != Path(self.codex_binary)
                or _resolved_codex_home() != self.codex_home
                or Path.home().expanduser().resolve() != self.home
            ):
                raise CodexDriverError(
                    "production Codex binary or root state changed"
                )
            resolved, version, digest = _resolve_production_codex_binary()
            if (
                resolved != Path(self.codex_binary)
                or
                version != self.codex_cli_version
                or digest != self.codex_binary_sha256
            ):
                raise CodexDriverError(
                    "production Codex version or binary changed"
                )
        elif self._production_fingerprint is not None:
            raise CodexDriverError("production Codex run mode was mutated")

    def _new_execution_id(self):
        value = str(self.uuid_factory()).lower()
        # StageRequest validation is the canonical UUIDv4 check.
        return value

    def _context_config_args(self):
        return tuple(
            part for override in CONTEXT_CONFIG_OVERRIDES
            for part in ("-c", override)
        )

    def _finalize_context_audit(self, record):
        record = dict(record)
        record["audit_sha256"] = contracts.canonical_sha256(record)
        return _validate_context_audit(record)

    def _mock_context_audit(self, isolation_dir, provider_model_id):
        return self._finalize_context_audit({
            "audit_version": CONTEXT_AUDIT_VERSION,
            "source": "mock",
            "provider_model_id": provider_model_id or "unverified",
            "isolation_dir": str(isolation_dir),
            "context_profile_sha256": CONTEXT_PROFILE_SHA256,
            "sentinel_sha256": contracts.sha256_utf8(
                CONTEXT_AUDIT_SENTINEL
            ),
            "argv_sha256": contracts.canonical_sha256([]),
            "raw_stdout_sha256": hashlib.sha256(b"").hexdigest(),
            "rendered_input_sha256": contracts.canonical_sha256([]),
            "passed": False,
        })

    def _context_preflight_argv(self, provider_model_id):
        disabled = tuple(
            part for feature in self.disabled_features
            for part in ("--disable", feature)
        )
        return (
            self.codex_binary, "debug", "prompt-input",
            "-c", "model={}".format(json.dumps(provider_model_id)),
            "-c", 'model_reasoning_effort="medium"',
            *self._context_config_args(), *disabled,
            CONTEXT_AUDIT_SENTINEL,
        )

    def _run_context_preflight(self, isolation_dir, provider_model_id):
        argv = self._context_preflight_argv(provider_model_id)
        try:
            completed = subprocess.run(
                list(argv), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                check=False, timeout=10, cwd=str(isolation_dir),
            )
        except (OSError, subprocess.SubprocessError):
            raise CodexDriverError(
                "production context preflight is unavailable"
            ) from None
        try:
            rendered = _strict_json_document(completed.stdout)
        except ValueError:
            raise CodexDriverError(
                "production context preflight evidence is invalid"
            ) from None
        if (
            completed.returncode != 0
            or completed.stderr != b""
            or rendered != EXPECTED_CONTEXT_AUDIT_INPUT
        ):
            raise CodexDriverError(
                "production context preflight found extra model context"
            )
        try:
            if any(Path(isolation_dir).iterdir()):
                raise CodexDriverError(
                    "production context preflight changed isolation state"
                )
        except OSError:
            raise CodexDriverError(
                "production context preflight isolation is unavailable"
            ) from None
        return self._finalize_context_audit({
            "audit_version": CONTEXT_AUDIT_VERSION,
            "source": "codex-debug-prompt-input",
            "provider_model_id": provider_model_id,
            "isolation_dir": str(isolation_dir),
            "context_profile_sha256": CONTEXT_PROFILE_SHA256,
            "sentinel_sha256": contracts.sha256_utf8(
                CONTEXT_AUDIT_SENTINEL
            ),
            "argv_sha256": contracts.canonical_sha256(list(argv)),
            "raw_stdout_sha256": hashlib.sha256(completed.stdout).hexdigest(),
            "rendered_input_sha256": contracts.canonical_sha256(rendered),
            "passed": True,
        })

    def _context_audit_for(self, isolation_dir):
        resolved = Path(isolation_dir).resolve()
        audit = self.context_audits.get(resolved)
        try:
            audit = _validate_context_audit(audit)
        except (TypeError, ValueError):
            raise CodexDriverError("isolation context audit is unavailable") from None
        if audit["isolation_dir"] != str(resolved):
            raise CodexDriverError("isolation context audit root differs")
        expected_live = self.run_mode == "codex"
        if (
            audit["passed"] is not expected_live
            or audit["source"] != (
                "codex-debug-prompt-input" if expected_live else "mock"
            )
        ):
            raise CodexDriverError("isolation context audit mode differs")
        if expected_live and audit["argv_sha256"] != contracts.canonical_sha256(
                list(self._context_preflight_argv(
                    audit["provider_model_id"]
                ))):
            raise CodexDriverError("isolation context audit command differs")
        return audit

    def restore_persisted_context_audit(self, isolation_dir, record):
        """Restore one validated live audit without weakening fingerprinting."""
        self._assert_production_dependencies()
        resolved = Path(isolation_dir).expanduser().resolve()
        try:
            audit = _validate_context_audit(record)
        except (TypeError, ValueError):
            raise CodexDriverError(
                "persisted context audit is invalid"
            ) from None
        if (
            audit["isolation_dir"] != str(resolved)
            or audit["source"] != "codex-debug-prompt-input"
            or audit["passed"] is not True
            or audit["argv_sha256"] != contracts.canonical_sha256(list(
                self._context_preflight_argv(audit["provider_model_id"])
            ))
        ):
            raise CodexDriverError(
                "persisted context audit binding differs"
            )
        existing = self.context_audits.get(resolved)
        if existing is not None and existing != audit:
            raise CodexDriverError(
                "persisted context audit conflicts with restored evidence"
            )
        if existing is None:
            self.context_audits[resolved] = deepcopy(audit)
            self._used_isolation_dirs.add(resolved)
            self._production_fingerprint = self._runtime_fingerprint()
        return deepcopy(audit)

    def create_isolation_dir(self, provider_model_id=None):
        self._assert_production_dependencies()
        if (
            provider_model_id is not None
            and provider_model_id not in manifest.MODEL_LOGICAL_IDS
        ):
            raise CodexDriverError("context preflight model is not frozen")
        if self.run_mode == "codex" and provider_model_id is None:
            raise CodexDriverError("production context preflight requires a model")
        candidate = Path(self.tempdir_factory()).expanduser()
        if _FORBIDDEN_DIR_RE.search(candidate.name):
            raise CodexDriverError("isolation directory name is not opaque")
        if candidate.exists():
            if candidate.is_symlink() or not candidate.is_dir():
                raise CodexDriverError("isolation path is not a real directory")
        else:
            try:
                candidate.mkdir(mode=0o700)
            except OSError:
                raise CodexDriverError("isolation directory cannot be created") from None
        resolved = candidate.resolve()
        if resolved in self._used_isolation_dirs:
            raise CodexDriverError("isolation directory was already used")
        try:
            if any(resolved.iterdir()):
                raise CodexDriverError("isolation directory is not empty")
        except OSError:
            raise CodexDriverError("isolation directory cannot be inspected") from None
        audit = (
            self._run_context_preflight(resolved, provider_model_id)
            if self.run_mode == "codex"
            else self._mock_context_audit(resolved, provider_model_id)
        )
        self.context_audits[resolved] = audit
        self._used_isolation_dirs.add(resolved)
        if self.run_mode == "codex":
            self._production_fingerprint = self._runtime_fingerprint()
        return resolved

    def _initial_argv(self, model, isolation_dir):
        disabled = tuple(
            part for feature in self.disabled_features
            for part in ("--disable", feature)
        )
        return (
            self.codex_binary, "exec", "--strict-config",
            "--ignore-user-config",
            "--ignore-rules", *disabled,
            "--skip-git-repo-check", "--sandbox",
            "read-only", "--json", "--model", model, "-c",
            'model_reasoning_effort="medium"', *self._context_config_args(),
            "--cd",
            str(Path(isolation_dir).resolve()), "--output-schema",
            str(self.response_schema_path), "-",
        )

    def _resume_argv(self, model, session_id):
        if not _valid_thread_id(session_id):
            raise CodexDriverError("resume requires an explicit Codex thread ID")
        disabled = tuple(
            part for feature in self.disabled_features
            for part in ("--disable", feature)
        )
        return (
            self.codex_binary, "exec", "resume", "--strict-config",
            "--ignore-user-config",
            "--ignore-rules", *disabled, "--skip-git-repo-check", "--json",
            "--model", model, "-c", 'model_reasoning_effort="medium"',
            *self._context_config_args(),
            "--output-schema", str(self.response_schema_path), session_id, "-",
        )

    def _transport_descriptor(
            self, request, prompt, isolation_dir, session_id):
        context_audit = self._context_audit_for(isolation_dir)
        if (
            self.run_mode == "codex"
            and context_audit["provider_model_id"]
            != request["provider_model_id"]
        ):
            raise CodexDriverError("context preflight model differs")
        argv = (
            self._initial_argv(request["provider_model_id"], isolation_dir)
            if session_id is None
            else self._resume_argv(request["provider_model_id"], session_id)
        )
        descriptor = {
            "descriptor_version": TRANSPORT_DESCRIPTOR_VERSION,
            "execution_id": request["execution_id"],
            "stage": request["stage"],
            "request_sha256": request["request_sha256"],
            "provider_model_id": request["provider_model_id"],
            "configuration_id": request["configuration_id"],
            "session_id": session_id,
            "cwd": str(Path(isolation_dir).resolve()),
            "response_schema_path": str(self.response_schema_path),
            "response_schema_sha256": request["response_schema_sha256"],
            "codex_binary": self.codex_binary,
            "disabled_features": list(self.disabled_features),
            "argv": list(argv),
            "stdin_sha256": contracts.sha256_utf8(prompt),
            "run_mode": self.run_mode,
            "runtime_identity": deepcopy(self.runtime_identity),
            "context_profile_sha256": CONTEXT_PROFILE_SHA256,
            "context_audit": deepcopy(context_audit),
        }
        if (
            set(descriptor) != TRANSPORT_DESCRIPTOR_KEYS
            or set(descriptor["runtime_identity"]) != RUNTIME_IDENTITY_KEYS
        ):
            raise CodexDriverError("transport descriptor construction failed")
        return descriptor

    def _parse_outcome(self, outcome):
        if not isinstance(outcome, ExecutionOutcome):
            raise CodexDriverError("executor returned an invalid outcome")
        if type(outcome.exit_status) is not int:
            raise CodexDriverError("executor returned an invalid exit status")
        if type(outcome.stderr) is not bytes:
            raise CodexDriverError("executor must preserve binary stderr")
        parser = _IncrementalJsonlParser()
        raw_parts = []
        for chunk in outcome.stdout_chunks:
            if type(chunk) is not bytes:
                raise CodexDriverError("executor must preserve binary stdout")
            raw_parts.append(chunk)
            parser.feed(chunk)
        parsed = parser.finish()
        raw_bytes = b"".join(raw_parts)
        try:
            raw_trace = raw_bytes.decode("utf-8", errors="strict")
        except UnicodeError:
            raise CodexDriverError("Codex stdout is not strict UTF-8") from None
        if outcome.exit_status != 0:
            parsed = _ParsedTrace(
                session_id=parsed.session_id,
                token_emission_started=parsed.token_emission_started,
                raw_final_message=parsed.raw_final_message,
                usage=parsed.usage,
                reasoning_details=parsed.reasoning_details,
                tool_events=parsed.tool_events,
                error_code=parsed.error_code or "nonzero_exit",
                finish_reason=parsed.finish_reason,
                trace_valid=False,
                explicit_pre_token_transport_error=(
                    parsed.explicit_pre_token_transport_error
                ),
            )
        return raw_trace, parsed

    def _attest(self, parsed, request, isolation_dir, started_at_utc,
                observed_at_utc, expected_session_id, future_turns):
        context_audit = self._context_audit_for(isolation_dir)
        fallback = {
            "source": "unavailable",
            "thread_id": parsed.session_id,
            "returned_provider_model_id": "unverified",
            "returned_provider_name": "unverified",
            "cli_version": None,
            "cwd": None,
            "sandbox": None,
            "reasoning_effort": None,
            "turn_count": None,
            "disabled_features": list(self.disabled_features),
            "rollout_path": None,
            "rollout_prefix_size": 0,
            "rollout_prefix_sha256": hashlib.sha256(b"").hexdigest(),
            "rollout_mtime_ns": 0,
            "latest_context_timestamp_utc": None,
            "scanned_payload_sha256": contracts.canonical_sha256([]),
            "future_text_absent": False,
            "identifier_absent": False,
            "stage": request["stage"],
            "current_prompt_sha256": contracts.sha256_utf8(
                request["current_visible_turn"]["content"]
            ),
            "current_prompt_linked": False,
            "final_response_sha256": (
                contracts.sha256_utf8(parsed.raw_final_message)
                if parsed.raw_final_message is not None else None
            ),
            "final_response_linked": False,
            "stage_evidence_sha256": contracts.canonical_sha256([]),
            "rollout_tools_absent": False,
            "rollout_tool_evidence_sha256": contracts.canonical_sha256([]),
        }
        row = fallback
        evidence_loaded = False
        try:
            if _valid_thread_id(parsed.session_id):
                row = self.attestor(
                    parsed.session_id,
                    stage=request["stage"],
                    requested_model=request["provider_model_id"],
                    isolation_dir=isolation_dir,
                    started_at_utc=started_at_utc,
                    observed_at_utc=observed_at_utc,
                    future_turns=future_turns,
                    required_disabled_features=self.disabled_features,
                    current_prompt=request["current_visible_turn"]["content"],
                    expected_response=parsed.raw_final_message,
                )
                if type(row) is not dict or set(row) != RAW_ATTESTATION_KEYS:
                    raise ValueError("attestation keys")
                row = deepcopy(row)
                if row["returned_provider_model_id"] not in (
                        *manifest.MODEL_LOGICAL_IDS, "unverified"):
                    row["returned_provider_model_id"] = "unverified"
                if row["returned_provider_name"] != "OpenAI":
                    row["returned_provider_name"] = "unverified"
                evidence_loaded = True
        except Exception:
            row = fallback
            evidence_loaded = False
        try:
            record = _finalize_attestation(
                row, started_at_utc, observed_at_utc,
                context_profile_sha256=CONTEXT_PROFILE_SHA256,
                context_audit_sha256=context_audit["audit_sha256"],
            )
        except ValueError:
            record = _finalize_attestation(
                fallback, started_at_utc, observed_at_utc,
                context_profile_sha256=CONTEXT_PROFILE_SHA256,
                context_audit_sha256=context_audit["audit_sha256"],
            )
            evidence_loaded = False

        thread_ok = (
            evidence_loaded
            and _valid_thread_id(record["thread_id"])
            and record["thread_id"] == parsed.session_id
            and (
                expected_session_id is None
                or parsed.session_id == expected_session_id
            )
        )
        stage_turn_count = contracts.STAGES.index(request["stage"]) + 1
        freshness_ok = record["source"] == "mock"
        if record["source"] == "rollout":
            try:
                started = _parse_timestamp(started_at_utc)
                context_time = _parse_timestamp(
                    record["latest_context_timestamp_utc"]
                )
                freshness_ok = (
                    record["rollout_mtime_ns"]
                    >= int(started.timestamp() * 1_000_000_000)
                    and context_time >= started
                    and context_time <= _parse_timestamp(
                        observed_at_utc
                    ) + timedelta(seconds=1)
                    and record["rollout_mtime_ns"] <= int(
                        (_parse_timestamp(observed_at_utc).timestamp() + 1)
                        * 1_000_000_000
                    )
                )
            except ValueError:
                freshness_ok = False
        source_ok = (
            record["source"] == "rollout"
            if self.run_mode == "codex"
            else record["source"] in {"mock", "rollout"}
        )
        context_ok = (
            record["context_profile_sha256"] == CONTEXT_PROFILE_SHA256
            and record["context_audit_sha256"]
            == context_audit["audit_sha256"]
        )
        isolation_ok = (
            evidence_loaded and source_ok and freshness_ok and context_ok
            and type(record["cwd"]) is str
            and Path(record["cwd"]).resolve() == Path(isolation_dir).resolve()
            and record["sandbox"] == "read-only"
            and record["reasoning_effort"] == "medium"
            and record["cli_version"] == EXPECTED_CODEX_CLI_VERSION
            and type(record["turn_count"]) is int
            and record["turn_count"] == stage_turn_count
            and record["disabled_features"] == list(self.disabled_features)
        )
        return record, thread_ok, isolation_ok

    def run_stage(
            self, request, *, episode, isolation_dir, session_id,
            _before_stage=None, _integrity_session=1):
        self._assert_production_dependencies()
        request = contracts.validate_stage_request(request)
        if request["provider"] != "codex":
            raise CodexDriverError("Codex driver received a non-Codex request")
        isolation_dir = Path(isolation_dir).resolve()
        if isolation_dir not in self._used_isolation_dirs:
            raise CodexDriverError("stage isolation directory was not registered")
        turns = model_turns(episode)
        stage_index = contracts.STAGES.index(request["stage"])
        if request["current_visible_turn"] != turns[stage_index]:
            raise CodexDriverError("request prompt does not match the episode")
        prompt = request["current_visible_turn"]["content"]
        attempts = []
        final_parsed = None
        first_started = None
        last_completed = None
        descriptor = self._transport_descriptor(
            request, prompt, isolation_dir, session_id
        )
        argv = tuple(descriptor["argv"])
        transport_hash = contracts.canonical_sha256(descriptor)
        self.last_transport_descriptor = deepcopy(descriptor)
        self.last_transport_request_sha256 = transport_hash
        _emit_stage_hook(
            _before_stage,
            integrity_session=_integrity_session,
            request=request,
            transport_descriptor=descriptor,
            attestation=None,
        )

        for attempt_index in range(1, 4):
            started_at = _timestamp(self.clock())
            if first_started is None:
                first_started = started_at
            try:
                outcome = self.executor(
                    argv, stdin=prompt, cwd=isolation_dir
                )
                raw_trace, parsed = self._parse_outcome(outcome)
                exit_status = outcome.exit_status
            except Exception:
                raise CodexDriverError("Codex executor failed safely") from None
            completed_at = _timestamp(self.clock())
            last_completed = completed_at
            try:
                attempt = contracts.build_stage_attempt(
                    attempt_index=attempt_index,
                    started_at_utc=started_at,
                    completed_at_utc=completed_at,
                    provider_request_id=None,
                    token_emission_started=parsed.token_emission_started,
                    exit_status=exit_status,
                    http_status=None,
                    finish_reason=parsed.finish_reason,
                    usage=parsed.usage,
                    raw_trace=raw_trace,
                    raw_final_message=parsed.raw_final_message,
                    reasoning_effort="medium",
                    reasoning_details=parsed.reasoning_details,
                    error_code=parsed.error_code,
                )
            except ValueError as exc:
                if "credential" in str(exc).lower():
                    raise CodexDriverError(
                        "credential material was rejected from Codex evidence"
                    ) from None
                raise CodexDriverError(
                    "Codex evidence failed the stage-attempt contract"
                ) from None
            attempts.append(attempt)
            final_parsed = parsed
            retryable = (
                parsed.explicit_pre_token_transport_error
                and not parsed.token_emission_started
                and parsed.raw_final_message is None
                and bool(raw_trace)
                and attempt_index < 3
            )
            if not retryable:
                break
            self.sleeper(attempt_index)

        future = turns[stage_index + 1:]
        attestation, thread_ok, isolation_ok = self._attest(
            final_parsed, request, isolation_dir, first_started,
            last_completed, session_id, future
        )
        self.last_rollout_attestation = deepcopy(attestation)
        session_chain_ok = (
            final_parsed.trace_valid and thread_ok
            and attestation["identifier_absent"]
            and attestation["stage"] == request["stage"]
            and attestation["current_prompt_sha256"]
            == contracts.sha256_utf8(
                request["current_visible_turn"]["content"]
            )
            and attestation["current_prompt_linked"]
            and attestation["final_response_sha256"] == (
                contracts.sha256_utf8(final_parsed.raw_final_message)
                if final_parsed.raw_final_message is not None else None
            )
            and attestation["final_response_linked"]
        )
        future_text_absent = attestation["future_text_absent"] and not (
            _contains_future_material(
                [attempt["raw_trace"] for attempt in attempts], future
            )
            or _contains_future_material(
                [attempt["raw_final_message"] for attempt in attempts], future
            )
            or _contains_future_material(
                [attempt["reasoning_details"] for attempt in attempts], future
            )
        )
        tool_events = deepcopy(final_parsed.tool_events)
        if not attestation["rollout_tools_absent"]:
            tool_events.append({
                "type": "rollout_tool_activity",
                "evidence_sha256": attestation[
                    "rollout_tool_evidence_sha256"
                ],
            })
        try:
            result = contracts.build_stage_result(
                request,
                run_mode=self.run_mode,
                returned_provider_model_id=(
                    attestation["returned_provider_model_id"]
                    if type(attestation["returned_provider_model_id"]) is str
                    and attestation["returned_provider_model_id"]
                    else "unverified"
                ),
                returned_provider_name=(
                    attestation["returned_provider_name"]
                    if type(attestation["returned_provider_name"]) is str
                    and attestation["returned_provider_name"]
                    else "unverified"
                ),
                session_id=(
                    final_parsed.session_id
                    if _valid_thread_id(final_parsed.session_id) else None
                ),
                transport_request_sha256=transport_hash,
                attempts=attempts,
                tool_events=tool_events,
                session_chain_ok=session_chain_ok,
                isolation_ok=isolation_ok,
                future_text_absent=future_text_absent,
            )
            return result
        except ValueError as exc:
            if "credential" in str(exc).lower():
                raise CodexDriverError(
                    "credential material was rejected from Codex evidence"
                ) from None
            raise

    def _attestation_flags(
            self, record, request, isolation_dir, expected_session_id):
        context_audit = self._context_audit_for(isolation_dir)
        evidence_loaded = record["source"] in {"mock", "rollout"}
        thread_ok = (
            evidence_loaded
            and _valid_thread_id(record["thread_id"])
            and (
                expected_session_id is None
                or record["thread_id"] == expected_session_id
            )
        )
        freshness_ok = record["source"] == "mock"
        if record["source"] == "rollout":
            try:
                started = _parse_timestamp(
                    record["invocation_started_at_utc"]
                )
                context = _parse_timestamp(
                    record["latest_context_timestamp_utc"]
                )
                observed = _parse_timestamp(record["observed_at_utc"])
                freshness_ok = (
                    record["rollout_mtime_ns"]
                    >= int(started.timestamp() * 1_000_000_000)
                    and context >= started
                    and context <= observed + timedelta(seconds=1)
                    and record["rollout_mtime_ns"] <= int(
                        (observed.timestamp() + 1) * 1_000_000_000
                    )
                )
            except ValueError:
                freshness_ok = False
        source_ok = (
            record["source"] == "rollout"
            if self.run_mode == "codex"
            else record["source"] in {"mock", "rollout"}
        )
        context_ok = (
            record["context_profile_sha256"] == CONTEXT_PROFILE_SHA256
            and record["context_audit_sha256"]
            == context_audit["audit_sha256"]
        )
        isolation_ok = (
            evidence_loaded and source_ok and freshness_ok and context_ok
            and type(record["cwd"]) is str
            and Path(record["cwd"]).resolve() == Path(isolation_dir).resolve()
            and record["sandbox"] == "read-only"
            and record["reasoning_effort"] == "medium"
            and record["cli_version"] == EXPECTED_CODEX_CLI_VERSION
            and record["turn_count"] == contracts.STAGES.index(
                request["stage"]
            ) + 1
            and record["disabled_features"] == list(self.disabled_features)
        )
        return thread_ok, isolation_ok

    def validate_stage_evidence(
            self, request, result, descriptor, attestation, episode, *,
            isolation_dir, prior_session_id):
        self._assert_production_dependencies()
        request = contracts.validate_stage_request(request)
        result = contracts.validate_stage_result(result, request)
        if (
            result["run_mode"] != self.run_mode
            or result["provenance"] != contracts.RUN_PROVENANCE[self.run_mode]
        ):
            raise CodexDriverError("result run_mode/provenance differs from driver")
        prompt = request["current_visible_turn"]["content"]
        expected_descriptor = self._transport_descriptor(
            request, prompt, isolation_dir, prior_session_id
        )
        if (
            type(descriptor) is not dict
            or set(descriptor) != TRANSPORT_DESCRIPTOR_KEYS
            or descriptor != expected_descriptor
        ):
            raise CodexDriverError("persisted transport descriptor differs")
        if contracts.canonical_sha256(descriptor) != result[
                "transport_request_sha256"]:
            raise CodexDriverError("transport descriptor hash binding differs")

        if (
            type(attestation) is not dict
            or set(attestation) != ATTESTATION_RECORD_KEYS
            or attestation["attestation_version"] != ATTESTATION_VERSION
            or attestation["attestation_sha256"]
            != contracts.canonical_sha256(
                _without_attestation_hash(attestation)
            )
        ):
            raise CodexDriverError("persisted rollout attestation hash differs")
        if attestation["invocation_started_at_utc"] != result[
                "attempts"][0]["started_at_utc"] or attestation[
                "observed_at_utc"] != result["attempts"][-1][
                    "completed_at_utc"]:
            raise CodexDriverError("rollout attestation chronology differs")
        if (
            attestation["disabled_features"] != descriptor[
                "disabled_features"]
            or attestation["context_profile_sha256"]
            != descriptor["context_profile_sha256"]
            or attestation["context_audit_sha256"]
            != descriptor["context_audit"]["audit_sha256"]
            or attestation["returned_provider_model_id"] != result[
                "returned_provider_model_id"]
            or attestation["returned_provider_name"] != result[
                "returned_provider_name"]
            or (
                attestation["source"] in {"mock", "rollout"}
                and attestation["thread_id"] != result["session_id"]
            )
        ):
            raise CodexDriverError("rollout attestation identity differs")

        turns = model_turns(episode)
        stage_index = contracts.STAGES.index(request["stage"])
        future = turns[stage_index + 1:]
        if attestation["source"] == "rollout":
            if type(self.attestor) is not CodexRolloutAttestor:
                raise CodexDriverError(
                    "rollout source requires production attestor"
                )
            projection = self.attestor.rederive_attestation(
                attestation, future_turns=future,
                current_prompt=request["current_visible_turn"]["content"],
                expected_response=result["attempts"][-1][
                    "raw_final_message"
                ],
            )
            for field, value in projection.items():
                if attestation[field] != value:
                    raise CodexDriverError(
                        "rollout attestation projection differs"
                    )
        elif attestation["source"] == "mock":
            if self.run_mode != "mock" or result["run_mode"] != "mock":
                raise CodexDriverError("mock attestation cannot support live result")
        elif attestation["source"] != "unavailable":
            raise CodexDriverError("rollout attestation source differs")

        parsed_attempts = []
        for index, attempt in enumerate(result["attempts"]):
            parsed_raw, parsed_attempt = self._parse_outcome(ExecutionOutcome(
                stdout_chunks=(attempt["raw_trace"].encode("utf-8"),),
                stderr=b"", exit_status=attempt["exit_status"] or 0,
            ))
            if parsed_raw != attempt["raw_trace"] or (
                parsed_attempt.token_emission_started
                != attempt["token_emission_started"]
                or parsed_attempt.raw_final_message != attempt[
                    "raw_final_message"]
                or parsed_attempt.usage != attempt["usage"]
                or parsed_attempt.reasoning_details != attempt[
                    "reasoning_details"]
                or parsed_attempt.error_code != attempt["error_code"]
                or parsed_attempt.finish_reason != attempt["finish_reason"]
            ):
                raise CodexDriverError("rollout trace-derived evidence differs")
            if index < len(result["attempts"]) - 1 and not (
                parsed_attempt.explicit_pre_token_transport_error
                and not parsed_attempt.token_emission_started
                and parsed_attempt.raw_final_message is None
            ):
                raise CodexDriverError("transport retry evidence differs")
            parsed_attempts.append(parsed_attempt)
        parsed = parsed_attempts[-1]
        thread_ok, isolation_ok = self._attestation_flags(
            attestation, request, isolation_dir, prior_session_id
        )
        expected_session_ok = (
            parsed.trace_valid and thread_ok
            and parsed.session_id == attestation["thread_id"]
            and attestation["identifier_absent"]
            and attestation["stage"] == request["stage"]
            and attestation["current_prompt_sha256"]
            == contracts.sha256_utf8(
                request["current_visible_turn"]["content"]
            )
            and attestation["current_prompt_linked"]
            and attestation["final_response_sha256"] == (
                contracts.sha256_utf8(parsed.raw_final_message)
                if parsed.raw_final_message is not None else None
            )
            and attestation["final_response_linked"]
        )
        stdout_future_absent = not any(
            _contains_future_material(attempt[field], future)
            for attempt in result["attempts"]
            for field in (
                "raw_trace", "raw_final_message", "reasoning_details"
            )
        )
        expected_future_absent = (
            attestation["future_text_absent"] and stdout_future_absent
        )
        expected_tool_events = deepcopy(parsed.tool_events)
        if not attestation["rollout_tools_absent"]:
            expected_tool_events.append({
                "type": "rollout_tool_activity",
                "evidence_sha256": attestation[
                    "rollout_tool_evidence_sha256"
                ],
            })
        if (
            result["integrity"]["session_chain_ok"] != expected_session_ok
            or result["integrity"]["isolation_ok"] != isolation_ok
            or result["integrity"]["future_text_absent"]
            != expected_future_absent
            or result["tool_events"] != expected_tool_events
        ):
            raise CodexDriverError("rollout attestation claims differ")
        return True

    def validate_episode_attempt(self, attempt, episode):
        self._assert_production_dependencies()
        if not isinstance(attempt, EpisodeAttempt):
            raise CodexDriverError("episode evidence is not an EpisodeAttempt")
        lengths = {
            len(attempt.requests), len(attempt.results),
            len(attempt.transport_descriptors), len(attempt.attestations),
        }
        if len(lengths) != 1 or not attempt.requests:
            raise CodexDriverError("episode evidence list lengths differ")
        prior_session_id = None
        for request, result, descriptor, attestation in zip(
                attempt.requests, attempt.results,
                attempt.transport_descriptors, attempt.attestations):
            self.validate_stage_evidence(
                request, result, descriptor, attestation, episode,
                isolation_dir=attempt.isolation_dir,
                prior_session_id=prior_session_id,
            )
            if prior_session_id is None and _valid_thread_id(result["session_id"]):
                prior_session_id = result["session_id"]
        if attempt.chain is not None:
            contracts.validate_stage_chain(
                attempt.chain, attempt.requests, attempt.results, episode
            )
        return attempt

    def _identity(self, logical_model_id):
        panel = manifest.load_panel()
        for row in panel["models"]:
            if row["logical_model_id"] == logical_model_id:
                provider = row["providers"]["codex"]
                if row["reasoning_effort"] != "medium":
                    break
                return {
                    "provider": "codex",
                    "logical_model_id": logical_model_id,
                    "provider_model_id": provider["provider_model_id"],
                    "configuration_id": provider["configuration_id"],
                }
        raise CodexDriverError("logical model is not in the frozen Codex panel")

    def _run_once(
            self, episode, logical_model_id, *, execution_id=None,
            first_request=None, integrity_session=1, before_stage=None,
            stage_sink=None):
        identity = self._identity(logical_model_id)
        execution_id = execution_id or self._new_execution_id()
        isolation_dir = self.create_isolation_dir(
            provider_model_id=identity["provider_model_id"]
        )
        requests = []
        results = []
        transport_descriptors = []
        attestations = []
        prior = {}
        session_id = None

        for index, stage in enumerate(contracts.STAGES):
            if index == 0 and first_request is not None:
                request = contracts.validate_stage_request(first_request)
            else:
                request = contracts.build_stage_request(
                    episode,
                    execution_id=execution_id,
                    stage=stage,
                    prior_responses=prior,
                    **identity,
                )
            result = self.run_stage(
                request,
                episode=episode,
                isolation_dir=isolation_dir,
                session_id=session_id,
                _before_stage=before_stage,
                _integrity_session=integrity_session,
            )
            descriptor = deepcopy(self.last_transport_descriptor)
            attestation = deepcopy(self.last_rollout_attestation)
            requests.append(request)
            results.append(result)
            transport_descriptors.append(descriptor)
            attestations.append(attestation)
            self.validate_stage_evidence(
                request,
                result,
                descriptor,
                attestation,
                episode,
                isolation_dir=isolation_dir,
                prior_session_id=session_id,
            )
            _emit_stage_hook(
                stage_sink,
                integrity_session=integrity_session,
                request=request,
                transport_descriptor=descriptor,
                attestation=attestation,
                result=result,
            )
            if session_id is None and type(result["session_id"]) is str:
                session_id = result["session_id"]
            final_message = result["attempts"][-1]["raw_final_message"]
            if result["terminal_status"] == "invalidated" or final_message is None:
                break
            prior[stage] = final_message

        chain = None
        if len(requests) == 4 and all(
                result["terminal_status"] not in {"invalidated", "failed"}
                for result in results):
            chain = contracts.build_stage_chain(requests, results, episode)
        attempt = EpisodeAttempt(
            execution_id=execution_id,
            isolation_dir=isolation_dir,
            requests=requests,
            results=results,
            transport_descriptors=transport_descriptors,
            attestations=attestations,
            chain=chain,
        )
        self.validate_episode_attempt(attempt, episode)
        return attempt

    def run_episode(
            self, episode, *, logical_model_id, allow_integrity_rerun=False,
            before_stage=None, stage_sink=None):
        _validate_stage_hooks(before_stage, stage_sink)
        self._assert_production_dependencies()
        first = self._run_once(
            episode,
            logical_model_id,
            integrity_session=1,
            before_stage=before_stage,
            stage_sink=stage_sink,
        )
        if not allow_integrity_rerun or not first.results:
            return CodexEpisodeRun((first,))
        final_result = first.results[-1]
        allowed_violations = {
            "provider_identity", "session_chain", "isolation",
            "future_text", "tool_event", "trace_incomplete",
            "forbidden_identifier_echo",
        }
        violations = set(final_result["integrity"]["violations"])
        final_attempt = final_result["attempts"][-1]
        rerun_eligible = (
            final_result["terminal_status"] == "invalidated"
            and not final_result["integrity"]["integrity_valid"]
            and bool(violations)
            and violations <= allowed_violations
            and "transport_error" not in violations
            and final_attempt["error_code"] is None
            and final_attempt["exit_status"] == 0
            and final_attempt["http_status"] is None
            and bool(final_attempt["raw_trace"])
        )
        if not rerun_eligible:
            return CodexEpisodeRun((first,))

        new_execution_id = self._new_execution_id()
        new_stage_1 = contracts.build_stage_request(
            episode,
            execution_id=new_execution_id,
            stage="stage_1",
            prior_responses={},
            **self._identity(logical_model_id),
        )
        authorization = contracts.validate_integrity_rerun(
            first.requests, first.results, [new_stage_1]
        )
        second = self._run_once(
            episode,
            logical_model_id,
            execution_id=new_execution_id,
            first_request=new_stage_1,
            integrity_session=2,
            before_stage=before_stage,
            stage_sink=stage_sink,
        )
        return CodexEpisodeRun((first, second), authorization=authorization)
