"""Dependency-injected, offline-testable Codex-OAuth judge process adapter."""

from __future__ import annotations

import json
import os
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Callable, Dict, Mapping, Optional, Sequence


MODEL = "gpt-5.6-sol"
REASONING_EFFORT = "medium"
MAX_BATCH_SIZE = 8
MAX_RECORD_RETRIES = 2
MAX_RECORD_ID_BYTES = 256
MAX_CRITERION_ID_BYTES = 256
MAX_SUT_RESPONSE_TOKENS = 2048
MAX_SUT_RESPONSE_BYTES = 65536
MAX_JUDGE_INPUT_SERIALIZED_BYTES = MAX_BATCH_SIZE * (
    MAX_RECORD_ID_BYTES + MAX_CRITERION_ID_BYTES + MAX_SUT_RESPONSE_BYTES + 128
)
_ALLOWED_ITEM_TYPES = {"agent_message", "reasoning"}
_SAFE_ENV_NAMES = (
    "PATH", "HOME", "TMPDIR", "LANG", "SSL_CERT_FILE", "CODEX_HOME",
)
_PROMPT_PREFIX = (
    "You are the single unqualified WCF-Bench Open-First judge. "
    "Do not call any tool, command, web search, MCP server, or subagent. "
    "Judge only the supplied records. Return strict schema-conforming JSON, "
    "preserve every record_id exactly once, and invent no IDs.\n\n"
)


def serialize_judge_records(records: Sequence[Mapping[str, Any]]) -> str:
    payload = [{
        "record_id": row["record_id"],
        "payload": row["payload"],
    } for row in records]
    return json.dumps(payload, sort_keys=True, ensure_ascii=False)


def render_judge_prompt(records: Sequence[Mapping[str, Any]]) -> str:
    return _PROMPT_PREFIX + serialize_judge_records(records)


def judge_prompt_byte_ceiling() -> int:
    """Exact upper bound enforced by input validation before subprocess launch."""
    return len(_PROMPT_PREFIX.encode("utf-8")) + MAX_JUDGE_INPUT_SERIALIZED_BYTES


class JudgeAdapterError(RuntimeError):
    """The isolated judge process or its record/evidence contract failed."""


class CodexOAuthJudge:
    """Invoke isolated ``codex exec`` batches through an injectable process seam.

    No process runs during construction or import.  The default runner is used only
    when a separately authorized caller explicitly invokes :meth:`judge`.
    """

    def __init__(
        self,
        *,
        runner: Callable[..., Any] = subprocess.run,
        persist: Callable[[Dict[str, Any]], Any],
        binary: str = "codex",
        timeout_s: float = 600.0,
        max_record_retries: int = MAX_RECORD_RETRIES,
    ) -> None:
        self.runner = runner
        self.persist = persist
        self.binary = binary
        self.timeout_s = timeout_s
        if max_record_retries != MAX_RECORD_RETRIES:
            raise ValueError("Open-First judge retry policy is fixed at two retries")
        self.max_record_retries = max_record_retries

    @staticmethod
    def _validate_input(records: Sequence[Mapping[str, Any]]) -> None:
        if not 1 <= len(records) <= MAX_BATCH_SIZE:
            raise JudgeAdapterError("judge batch must contain 1-8 records")
        record_ids = [row.get("record_id") for row in records]
        if (any(not isinstance(value, str) or not value for value in record_ids)
                or len(set(record_ids)) != len(record_ids)):
            raise JudgeAdapterError("judge input record IDs must be unique and non-empty")
        if any(len(value.encode("utf-8")) > MAX_RECORD_ID_BYTES
               for value in record_ids):
            raise JudgeAdapterError("judge input record ID exceeds its byte envelope")
        identities = {(row.get("sut"), row.get("route")) for row in records}
        if len(identities) != 1:
            raise JudgeAdapterError("judge batch must contain the same SUT and route")
        route = records[0].get("route")
        if route not in {"open", "contested", "episode"}:
            raise JudgeAdapterError("judge batch route is unsupported")
        for row in records:
            payload = row.get("payload")
            criterion_id = payload.get("criterion_id") if isinstance(payload, Mapping) else None
            response = payload.get("response") if isinstance(payload, Mapping) else None
            if (not isinstance(payload, Mapping)
                    or set(payload) != {"criterion_id", "response"}
                    or not isinstance(criterion_id, str) or not criterion_id
                    or len(criterion_id.encode("utf-8")) > MAX_CRITERION_ID_BYTES
                    or not isinstance(response, str)
                    or len(response.encode("utf-8")) > MAX_SUT_RESPONSE_BYTES):
                raise JudgeAdapterError(
                    "judge input payload is outside the exact serialized schema/byte envelope")
        if (len(serialize_judge_records(records).encode("utf-8"))
                > MAX_JUDGE_INPUT_SERIALIZED_BYTES):
            raise JudgeAdapterError("judge input serialized byte envelope exceeded")

    @staticmethod
    def _schema(route: str) -> Dict[str, Any]:
        verdict_properties: Dict[str, Any] = {
            "criterion_id": {"type": "string", "minLength": 1},
            "reason": {"type": "string", "minLength": 1},
        }
        if route == "contested":
            verdict_properties["verdict"] = {
                "type": "string",
                "enum": ["satisfied", "not_satisfied", "ungraded"],
            }
            verdict_required = ["criterion_id", "verdict", "reason"]
        elif route in {"open", "episode"}:
            verdict_properties["satisfied"] = {"type": "boolean"}
            verdict_required = ["criterion_id", "satisfied", "reason"]
        else:
            raise JudgeAdapterError(f"unsupported judge route: {route}")
        return {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "properties": {
                "records": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "record_id": {"type": "string", "minLength": 1},
                            "verdict": {
                                "type": "object",
                                "properties": verdict_properties,
                                "required": verdict_required,
                                "additionalProperties": False,
                            },
                        },
                        "required": ["record_id", "verdict"],
                        "additionalProperties": False,
                    },
                },
            },
            "required": ["records"],
            "additionalProperties": False,
        }

    @staticmethod
    def _prompt(records: Sequence[Mapping[str, Any]]) -> str:
        return render_judge_prompt(records)

    def _command(
        self, *, cwd: str, schema_path: str, output_path: str,
        records: Sequence[Mapping[str, Any]],
    ) -> list:
        return [
            self.binary, "exec",
            "--ephemeral",
            "--ignore-user-config",
            "--ignore-rules",
            "--sandbox", "read-only",
            "--skip-git-repo-check",
            "--model", MODEL,
            "-c", f'model_reasoning_effort="{REASONING_EFFORT}"',
            "-c", 'web_search="disabled"',
            "-c", "features.multi_agent=false",
            "--json",
            "--output-schema", schema_path,
            "-o", output_path,
            "-C", cwd,
            self._prompt(records),
        ]

    @staticmethod
    def _validate_events(stdout: str) -> None:
        completed = False
        for line in (stdout or "").splitlines():
            if not line.strip():
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError as exc:
                raise JudgeAdapterError("codex JSONL event stream is malformed") from exc
            if not isinstance(event, Mapping):
                raise JudgeAdapterError("codex JSONL event is not an object")
            event_type = event.get("type")
            if event_type in {"error", "turn.failed"}:
                raise JudgeAdapterError(f"codex judge event failed: {event}")
            if str(event_type).startswith("item."):
                item = event.get("item")
                item_type = item.get("type") if isinstance(item, Mapping) else None
                if item_type not in _ALLOWED_ITEM_TYPES:
                    raise JudgeAdapterError(
                        f"codex judge emitted forbidden tool event: {item_type}")
            if event_type == "turn.completed":
                completed = True
        if not completed:
            raise JudgeAdapterError("codex judge event stream lacks turn.completed")

    @staticmethod
    def _valid_output_records(
        payload: Any, pending: Mapping[str, Mapping[str, Any]],
    ) -> Dict[str, Dict[str, Any]]:
        if not isinstance(payload, Mapping) or set(payload) != {"records"}:
            return {}
        rows = payload.get("records")
        if not isinstance(rows, list):
            return {}
        counts: Dict[str, int] = {}
        for row in rows:
            if isinstance(row, Mapping) and isinstance(row.get("record_id"), str):
                counts[row["record_id"]] = counts.get(row["record_id"], 0) + 1
        valid = {}
        for row in rows:
            if not isinstance(row, Mapping) or set(row) != {"record_id", "verdict"}:
                continue
            record_id = row["record_id"]
            verdict = row["verdict"]
            source = pending.get(record_id)
            if (source is None or counts.get(record_id) != 1
                    or not isinstance(verdict, Mapping)):
                continue
            source_payload = source.get("payload")
            criterion_id = (source_payload.get("criterion_id")
                            if isinstance(source_payload, Mapping) else None)
            route = source.get("route")
            if not CodexOAuthJudge._valid_verdict(route, verdict, criterion_id):
                continue
            valid[record_id] = {"record_id": record_id, "verdict": dict(verdict)}
        return valid

    @staticmethod
    def _valid_verdict(route: Any, verdict: Mapping[str, Any], criterion_id: Any) -> bool:
        if (not isinstance(criterion_id, str)
                or verdict.get("criterion_id") != criterion_id
                or not isinstance(verdict.get("reason"), str)
                or not verdict["reason"].strip()):
            return False
        if route == "contested":
            return (
                set(verdict) == {"criterion_id", "verdict", "reason"}
                and verdict.get("verdict") in {
                    "satisfied", "not_satisfied", "ungraded"}
            )
        if route in {"open", "episode"}:
            return (
                set(verdict) == {"criterion_id", "satisfied", "reason"}
                and isinstance(verdict.get("satisfied"), bool)
            )
        return False

    def _invoke(self, records: Sequence[Mapping[str, Any]]) -> Dict[str, Dict[str, Any]]:
        with tempfile.TemporaryDirectory(prefix="wcfbench-codex-empty-") as cwd:
            with tempfile.TemporaryDirectory(prefix="wcfbench-codex-control-") as control:
                schema_path = str(Path(control) / "judge-output-schema.json")
                output_path = str(Path(control) / "judge-output.json")
                route = str(records[0]["route"])
                Path(schema_path).write_text(
                    json.dumps(self._schema(route), sort_keys=True), encoding="utf-8")
                command = self._command(
                    cwd=cwd, schema_path=schema_path, output_path=output_path,
                    records=records)
                # Reuse only the local CLI's OAuth location and process essentials.
                # No unrelated parent configuration or credential can cross this boundary.
                env = {name: os.environ[name] for name in _SAFE_ENV_NAMES
                       if name in os.environ}
                try:
                    process = self.runner(
                        command, capture_output=True, text=True, timeout=self.timeout_s,
                        cwd=cwd, env=env)
                except (OSError, subprocess.SubprocessError) as exc:
                    raise JudgeAdapterError(f"could not invoke isolated codex judge: {exc}") from exc
                if process.returncode != 0:
                    raise JudgeAdapterError(
                        f"codex judge exited {process.returncode}: "
                        f"{(process.stderr or '')[:400]}")
                self._validate_events(process.stdout)
                try:
                    payload = json.loads(Path(output_path).read_text(encoding="utf-8"))
                except (OSError, json.JSONDecodeError) as exc:
                    raise JudgeAdapterError("codex judge final JSON is missing or malformed") from exc
                return self._valid_output_records(
                    payload, {str(row["record_id"]): row for row in records})

    def judge(self, records: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
        """Persist each valid record now; retry only still-missing IDs, at most twice."""
        self._validate_input(records)
        pending = {str(row["record_id"]): dict(row) for row in records}
        persisted = []
        attempts = 0
        for _attempt in range(1 + self.max_record_retries):
            if not pending:
                break
            attempts += 1
            valid = self._invoke(list(pending.values()))
            for record_id in list(pending):
                row = valid.get(record_id)
                if row is None:
                    continue
                try:
                    self.persist(row)
                except Exception as exc:
                    raise JudgeAdapterError(
                        f"valid judge record could not be persisted: {record_id}") from exc
                persisted.append(row)
                del pending[record_id]
        return {
            "records": persisted,
            "missing_record_ids": list(pending),
            "attempts": attempts,
        }
