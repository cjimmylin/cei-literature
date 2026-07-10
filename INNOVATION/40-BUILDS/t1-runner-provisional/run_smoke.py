#!/usr/bin/env python
"""GREEN smoke probe: run 20260709-smoke-items.jsonl through the working backends
via the Runner. Writes a transcript and prints a per-family summary as JSON.

Provenance: cli-oauth-provisional. NOT an API measurement.
"""

import json
import os
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from t1_runner import (ModelRequest, Runner, ResponseStatus, TranscriptLogger,
                       retry_with_backoff)
from t1_runner.backends.anthropic_cli import AnthropicCLIBackend
from t1_runner.backends.openai_cli import OpenAICLIBackend

TRANSIENT = {ResponseStatus.TIMEOUT}


def transient_status(resp):
    if resp.status in TRANSIENT:
        return True
    if resp.status == ResponseStatus.ERROR:
        low = (resp.error_detail or "").lower()
        return any(m in low for m in ("rate limit", "429", "too many requests",
                                      "temporarily", "quota"))
    return False


def load_items(path):
    items = []
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if line:
                items.append(json.loads(line))
    return items


def main():
    items = load_items(os.path.join(HERE, "20260709-smoke-items.jsonl"))
    runid = os.environ.get("SMOKE_RUNID", "smoke")
    transcript = TranscriptLogger(os.path.join(HERE, "transcripts"), runid=runid)

    backends = [
        AnthropicCLIBackend(model_alias="haiku"),  # cheap, real Anthropic model
        OpenAICLIBackend(),                          # account-default (gpt-5.5)
    ]
    runner = Runner(backends, transcript=transcript, timeout_s=120)
    print("versions:", json.dumps(runner.versions()))

    results = {b.name: [] for b in backends}
    for it in items:
        req = ModelRequest(prompt=it["prompt"], item_id=it["item_id"],
                           params={"kind": it.get("kind", "")})
        for name, backend in runner.backends.items():
            # Log EVERY real call (including retries): the closure logs each attempt.
            def call_and_log(b=backend):
                r = b.run(req, timeout_s=runner.timeout_s)
                transcript.log(r)
                return r
            resp = retry_with_backoff(
                call_and_log, is_transient=transient_status,
                max_retries=2, base=2.0)
            results[name].append(resp)
            print(f"[{it['item_id']:>18}] {name:>13}: {resp.status.value:<14} "
                  f"model={resp.model_id_reported:<28} "
                  f"text={resp.text[:60]!r}")

    summary = {}
    for name, resps in results.items():
        counts = {s.value: 0 for s in ResponseStatus}
        for r in resps:
            counts[r.status.value] += 1
        lat = [r.latency_s for r in resps]
        summary[name] = {
            "n": len(resps),
            "counts": counts,
            "median_latency_s": round(statistics.median(lat), 2) if lat else None,
            "model_id_reported": resps[0].model_id_reported if resps else None,
        }
    print("\nSUMMARY:", json.dumps(summary, indent=2))
    print("transcript_path:", transcript.path)
    print("transcript_count:", transcript.count)

    # write machine-readable summary next to the report inputs
    with open(os.path.join(HERE, "20260709-smoke-summary.json"), "w") as fh:
        json.dump({"versions": runner.versions(), "summary": summary,
                   "transcript_path": transcript.path,
                   "transcript_count": transcript.count}, fh, indent=2)


if __name__ == "__main__":
    main()
