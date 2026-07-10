"""Append-only JSONL transcript logger.

One file per run: ``transcripts/20260709-<runid>.jsonl``. Every real call writes
the FULL request (prompt, params, exact argv) and FULL raw response, plus the
provenance block, as one JSON line.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from typing import Any, Optional

from .core import ModelResponse
from .provenance import stamp


def _default_runid() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")


class TranscriptLogger:
    """Append-only JSONL logger. Never truncates; opens in append mode per write."""

    def __init__(self, transcripts_dir: str, runid: Optional[str] = None):
        self.dir = transcripts_dir
        os.makedirs(self.dir, exist_ok=True)
        self.runid = runid or _default_runid()
        self.path = os.path.join(self.dir, f"20260709-{self.runid}.jsonl")
        self._count = 0

    @property
    def count(self) -> int:
        return self._count

    def _record(self, response: ModelResponse) -> dict[str, Any]:
        return {
            "runid": self.runid,
            "logged_at": datetime.now(timezone.utc).isoformat(),
            "provenance": stamp(response),
            "request": {
                "item_id": response.request.item_id,
                "prompt": response.request.prompt,
                "system": response.request.system,
                "params": response.request.params,
                "argv": response.argv,
            },
            "response": {
                "status": response.status.value,
                "text": response.text,
                "latency_s": response.latency_s,
                "error_detail": response.error_detail,
                "raw_output": response.raw_output,
                "raw_output_path": response.raw_output_path,
            },
        }

    def log(self, response: ModelResponse) -> None:
        record = self._record(response)
        with open(self.path, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
        self._count += 1

    def read_all(self) -> list[dict[str, Any]]:
        """Parse the transcript back (used by the report to verify counts)."""
        if not os.path.exists(self.path):
            return []
        out = []
        with open(self.path, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    out.append(json.loads(line))
        return out
