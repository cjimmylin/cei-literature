#!/usr/bin/env python3
"""Pilot 2 byte-envelope specialization of the existing isolated OAuth judge."""

from __future__ import annotations

from typing import Any, Mapping, Sequence

from wcfbench.codex_oauth_judge import (  # re-exported for callers
    CodexOAuthJudge,
    JudgeAdapterError,
    MAX_CRITERION_ID_BYTES,
    MAX_RECORD_ID_BYTES,
    serialize_judge_records,
)

import pilot2_preflight as preflight


class Pilot2CodexOAuthJudge(CodexOAuthJudge):
    """Keep the reviewed Sol/OAuth process contract; widen only registered inputs."""

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
        if len({(row.get("sut"), row.get("route")) for row in records}) != 1:
            raise JudgeAdapterError("judge batch must contain the same SUT and route")
        if records[0].get("route") not in {"open", "contested", "episode"}:
            raise JudgeAdapterError("judge batch route is unsupported")
        for row in records:
            payload = row.get("payload")
            criterion_id = payload.get("criterion_id") if isinstance(payload, Mapping) else None
            response = payload.get("response") if isinstance(payload, Mapping) else None
            if (not isinstance(payload, Mapping)
                    or set(payload) != {"criterion_id", "response"}
                    or not isinstance(criterion_id, str) or not criterion_id
                    or len(criterion_id.encode("utf-8")) > MAX_CRITERION_ID_BYTES
                    or not isinstance(response, str)):
                raise JudgeAdapterError(
                    "judge input payload is outside the exact schema/byte envelope")
            projected = {"record_id": row.get("record_id"), "payload": dict(payload)}
            if len(serialize_judge_records([projected]).encode("utf-8")) \
                    > preflight.JUDGE_MAX_SERIALIZED_RECORD_BYTES:
                raise JudgeAdapterError("judge record exceeds Pilot 2 byte envelope")
        if len(serialize_judge_records(records).encode("utf-8")) \
                > preflight.JUDGE_MAX_SERIALIZED_BATCH_BYTES:
            raise JudgeAdapterError("judge input serialized byte envelope exceeded")


def main() -> int:
    print("Pilot 2 OAuth judge is implementation-only; no task is invoked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
