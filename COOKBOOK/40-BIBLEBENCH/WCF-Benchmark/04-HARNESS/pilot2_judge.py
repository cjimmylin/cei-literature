#!/usr/bin/env python3
"""Structured, isolated Codex-OAuth judge adapter for Pilot 2 scorer calls."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path
from typing import Any, Dict, Mapping, Sequence

import wcfbench.codex_oauth_judge as base
from wcfbench.codex_oauth_judge import (  # re-exported for callers
    CodexOAuthJudge,
    JudgeAdapterError,
    MAX_RECORD_ID_BYTES,
)

import pilot2_preflight as preflight


class Pilot2CodexOAuthJudge(CodexOAuthJudge):
    """Keep the reviewed process custody while returning scorer-compatible fields."""

    CALL_KINDS = {
        "open_award", "open_axis_matter", "open_axis_manner", "open_axis_end",
        "contested_disclosure", "contested_position", "contested_coherence",
        "contested_settled_core", "episode_keypoints",
    }

    @staticmethod
    def _serialized_inputs(records: Sequence[Mapping[str, Any]]) -> str:
        return json.dumps([{
            "record_id": row["record_id"],
            "call_kind": row.get("call_kind"),
            "payload": row["payload"],
        } for row in records], sort_keys=True, ensure_ascii=False)

    @staticmethod
    def _prompt(records: Sequence[Mapping[str, Any]]) -> str:
        return (
            "You are the single unqualified WCF-Bench Pilot 2 judge. Do not call any "
            "tool, command, web search, MCP server, or subagent. Apply each supplied "
            "existing WCF scorer prompt and return only the route/call-specific structured "
            "fields required by the output schema. Preserve every record_id exactly once.\n\n"
            + Pilot2CodexOAuthJudge._serialized_inputs(records)
        )

    @staticmethod
    def _validate_input(records: Sequence[Mapping[str, Any]]) -> None:
        if not 1 <= len(records) <= preflight.JUDGE_MAX_BATCH_SIZE:
            raise JudgeAdapterError("judge batch must contain 1-8 records")
        record_ids = [row.get("record_id") for row in records]
        if (any(not isinstance(value, str) or not value for value in record_ids)
                or len(set(record_ids)) != len(record_ids)):
            raise JudgeAdapterError("judge input record IDs must be unique and non-empty")
        if any(len(value.encode("utf-8")) > MAX_RECORD_ID_BYTES
               for value in record_ids):
            raise JudgeAdapterError("judge input record ID exceeds its byte envelope")
        if len({(row.get("sut"), row.get("route"), row.get("call_kind"))
                for row in records}) != 1:
            raise JudgeAdapterError(
                "judge batch must contain the same SUT, route, and call kind")
        if records[0].get("route") not in {"open", "contested", "episode"}:
            raise JudgeAdapterError("judge batch route is unsupported")
        for row in records:
            payload = row.get("payload")
            call_kind = row.get("call_kind")
            legacy = call_kind is None and isinstance(payload, Mapping) \
                and set(payload) == {"criterion_id", "response"}
            if (not isinstance(payload, Mapping)
                    or (not legacy and call_kind not in Pilot2CodexOAuthJudge.CALL_KINDS)
                    or (not legacy and not isinstance(payload.get("judge_prompt"), str))):
                raise JudgeAdapterError(
                    "judge input payload is outside the exact schema/byte envelope")
            if len(Pilot2CodexOAuthJudge._serialized_inputs([row]).encode("utf-8")) \
                    > preflight.JUDGE_MAX_SERIALIZED_RECORD_BYTES:
                raise JudgeAdapterError("judge record exceeds Pilot 2 byte envelope")
        if len(Pilot2CodexOAuthJudge._serialized_inputs(records).encode("utf-8")) \
                > preflight.JUDGE_MAX_SERIALIZED_BATCH_BYTES:
            raise JudgeAdapterError("judge input serialized byte envelope exceeded")

    @staticmethod
    def _result_schema(call_kind: str) -> Dict[str, Any]:
        reason = {"type": "string", "minLength": 1}
        criterion = {
            "type": "object",
            "properties": {
                "criterion_id": {"type": "string", "minLength": 1},
                "satisfied": {"type": "boolean"},
                "reason": reason,
            },
            "required": ["criterion_id", "satisfied", "reason"],
            "additionalProperties": False,
        }
        if call_kind == "open_award":
            properties = {"awards": {"type": "array", "items": criterion}}
            required = ["awards"]
        elif call_kind.startswith("open_axis_"):
            properties = {
                "axis": {"type": "string", "enum": [call_kind.rsplit("_", 1)[1]]},
                "score": {"type": "number", "enum": [0, 0.25, 0.5, 0.75, 1]},
                "reason": reason,
            }
            required = ["axis", "score", "reason"]
        elif call_kind == "contested_disclosure":
            properties = {
                "avoided_settled": {"type": "boolean"},
                "located_divide": {"type": "boolean"},
                "evidence_quote": {"type": "string"},
                "reason": reason,
            }
            required = list(properties)
        elif call_kind == "contested_position":
            properties = {
                "position_label": {"type": "string", "minLength": 1},
                "position_defensible": {"type": "boolean"},
                "reason": reason,
            }
            required = list(properties)
        elif call_kind == "contested_coherence":
            properties = {
                "score": {"type": "number", "enum": [0, 0.25, 0.5, 0.75, 1]},
                "reason": reason,
            }
            required = list(properties)
        elif call_kind in {"contested_settled_core", "episode_keypoints"}:
            properties = {"verdicts": {"type": "array", "items": criterion}}
            required = ["verdicts"]
        else:
            raise JudgeAdapterError(f"unsupported Pilot 2 call kind: {call_kind}")
        return {"type": "object", "properties": properties,
                "required": required, "additionalProperties": False}

    @classmethod
    def _schema_for(cls, call_kind: str) -> Dict[str, Any]:
        return {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "properties": {"records": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "record_id": {"type": "string", "minLength": 1},
                        "result": cls._result_schema(call_kind),
                    },
                    "required": ["record_id", "result"],
                    "additionalProperties": False,
                },
            }},
            "required": ["records"], "additionalProperties": False,
        }

    @staticmethod
    def _criteria(payload: Mapping[str, Any]) -> list:
        return [row.get("criterion_id") if isinstance(row, Mapping) else None
                for row in (payload.get("criteria") or ())]

    @classmethod
    def _valid_result(
        cls, call_kind: str, result: Any, payload: Mapping[str, Any],
    ) -> bool:
        if not isinstance(result, Mapping):
            return False
        try:
            if call_kind == "open_award":
                rows = result["awards"]
                return (set(result) == {"awards"}
                        and cls._valid_criterion_rows(rows, cls._criteria(payload)))
            if call_kind.startswith("open_axis_"):
                return (set(result) == {"axis", "score", "reason"}
                        and result["axis"] == call_kind.rsplit("_", 1)[1]
                        and result["score"] in {0, .25, .5, .75, 1}
                        and isinstance(result["reason"], str) and result["reason"].strip())
            if call_kind == "contested_disclosure":
                return (set(result) == {
                    "avoided_settled", "located_divide", "evidence_quote", "reason"}
                    and isinstance(result["avoided_settled"], bool)
                    and isinstance(result["located_divide"], bool)
                    and isinstance(result["evidence_quote"], str)
                    and isinstance(result["reason"], str) and result["reason"].strip())
            if call_kind == "contested_position":
                return (set(result) == {
                    "position_label", "position_defensible", "reason"}
                    and isinstance(result["position_label"], str)
                    and bool(result["position_label"].strip())
                    and isinstance(result["position_defensible"], bool)
                    and isinstance(result["reason"], str) and bool(result["reason"].strip()))
            if call_kind == "contested_coherence":
                return (set(result) == {"score", "reason"}
                        and result["score"] in {0, .25, .5, .75, 1}
                        and isinstance(result["reason"], str) and bool(result["reason"].strip()))
            if call_kind in {"contested_settled_core", "episode_keypoints"}:
                return (set(result) == {"verdicts"}
                        and cls._valid_criterion_rows(
                            result["verdicts"], cls._criteria(payload)))
        except (KeyError, TypeError):
            return False
        return False

    @staticmethod
    def _valid_criterion_rows(rows: Any, expected: Sequence[Any]) -> bool:
        if not isinstance(rows, list) or len(rows) != len(expected):
            return False
        ids = []
        for row in rows:
            if (not isinstance(row, Mapping)
                    or set(row) != {"criterion_id", "satisfied", "reason"}
                    or not isinstance(row["criterion_id"], str)
                    or not isinstance(row["satisfied"], bool)
                    or not isinstance(row["reason"], str) or not row["reason"].strip()):
                return False
            ids.append(row["criterion_id"])
        return len(set(ids)) == len(ids) and ids == list(expected)

    @classmethod
    def _valid_output_records(
        cls, payload: Any, pending: Mapping[str, Mapping[str, Any]],
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
            if not isinstance(row, Mapping) or set(row) != {"record_id", "result"}:
                continue
            source = pending.get(row["record_id"])
            if (source is None or counts.get(row["record_id"]) != 1
                    or not cls._valid_result(
                        source["call_kind"], row["result"], source["payload"])):
                continue
            valid[row["record_id"]] = {
                "record_id": row["record_id"], "result": dict(row["result"])}
        return valid

    def _invoke(self, records: Sequence[Mapping[str, Any]]) -> Dict[str, Dict[str, Any]]:
        call_kind = str(records[0]["call_kind"])
        with tempfile.TemporaryDirectory(prefix="wcfbench-codex-empty-") as cwd:
            with tempfile.TemporaryDirectory(prefix="wcfbench-codex-control-") as control:
                schema_path = str(Path(control) / "judge-output-schema.json")
                output_path = str(Path(control) / "judge-output.json")
                Path(schema_path).write_text(
                    json.dumps(self._schema_for(call_kind), sort_keys=True), encoding="utf-8")
                command = self._command(
                    cwd=cwd, schema_path=schema_path, output_path=output_path,
                    records=records)
                env = {name: base.os.environ[name] for name in base._SAFE_ENV_NAMES
                       if name in base.os.environ}
                try:
                    process = self.runner(
                        command, capture_output=True, text=True, timeout=self.timeout_s,
                        cwd=cwd, env=env)
                except (OSError, base.subprocess.SubprocessError) as exc:
                    raise JudgeAdapterError(
                        f"could not invoke isolated codex judge: {exc}") from exc
                if process.returncode != 0:
                    raise JudgeAdapterError(
                        f"codex judge exited {process.returncode}: "
                        f"{(process.stderr or '')[:400]}")
                self._validate_events(process.stdout)
                try:
                    output = json.loads(Path(output_path).read_text(encoding="utf-8"))
                except (OSError, json.JSONDecodeError) as exc:
                    raise JudgeAdapterError(
                        "codex judge final JSON is missing or malformed") from exc
                return self._valid_output_records(
                    output, {str(row["record_id"]): row for row in records})


def main() -> int:
    print("Pilot 2 OAuth judge is implementation-only; no task is invoked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
