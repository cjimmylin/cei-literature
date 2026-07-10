#!/usr/bin/env python
"""RP-04 S1 pilot — full judge run (80 records x 2 families).

For each sampled (scenario, response) pair, calls both judge families through the
T1 Runner, parses the JSON verdict, and on a parse failure retries ONCE with a
stricter reminder appended, then records parse_failure. Every call (incl. retries)
is logged to the transcript. Writes per-family verdict rows to disk.

Provenance: judges = cli-oauth-provisional. Subjects = synthetic-mock (frozen).
Volume: 80 x 2 = 160 base calls (+ <=1 retry per parse failure). Cap 300/family.
"""
from __future__ import annotations

import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
T1 = os.path.abspath(os.path.join(HERE, "..", "..", "t1-runner-provisional"))
sys.path.insert(0, T1)

from t1_runner import ModelRequest, Runner, ResponseStatus, TranscriptLogger  # noqa: E402
from t1_runner.backends.anthropic_cli import AnthropicCLIBackend  # noqa: E402
from t1_runner.backends.openai_cli import OpenAICLIBackend  # noqa: E402

from judge_prompt import build_prompt, parse_judge_output, STRICT_REMINDER  # noqa: E402

TIMEOUT_S = 260  # codex is slow/tail-heavy per smoke report


def load_manifest():
    path = os.path.join(HERE, "20260709-sample-manifest.jsonl")
    with open(path) as fh:
        return [json.loads(l) for l in fh if l.strip()]


def judge_one(backend, base_prompt, sample_id, transcript, timeout_s):
    """One judge call + parse; retry once on parse failure with stricter reminder.
    Returns (verdict_row_partial, model_response). model-side statuses (refusal/
    error/timeout) short-circuit (no retry — those are data)."""
    req = ModelRequest(prompt=base_prompt, item_id=sample_id,
                       params={"model": "haiku", "sample_id": sample_id})
    resp = backend.run(req, timeout_s=timeout_s)
    transcript.log(resp)
    calls = 1
    status = resp.status.value
    parsed, perr = (None, "not-ok status")
    if resp.status == ResponseStatus.OK:
        parsed, perr = parse_judge_output(resp.text)
        if parsed is None:
            # retry once, stricter
            req2 = ModelRequest(prompt=base_prompt + STRICT_REMINDER,
                                item_id=sample_id,
                                params={"model": "haiku", "sample_id": sample_id,
                                        "retry": 1})
            resp2 = backend.run(req2, timeout_s=timeout_s)
            transcript.log(resp2)
            calls += 1
            if resp2.status == ResponseStatus.OK:
                parsed, perr = parse_judge_output(resp2.text)
                resp = resp2  # report the retry's status/model
                status = resp2.status.value
            else:
                resp = resp2
                status = resp2.status.value
    # final classification for stats:
    if resp.status == ResponseStatus.REFUSAL:
        final = "refusal"
    elif resp.status == ResponseStatus.TIMEOUT:
        final = "timeout"
    elif resp.status == ResponseStatus.ERROR:
        final = "error"
    elif parsed is None:
        final = "parse_failure"
    else:
        final = "ok"
    row = {
        "sample_id": sample_id,
        "family": backend.name,
        "calls": calls,
        "final_status": final,
        "raw_status": status,
        "model_id": resp.model_id_reported,
        "latency_s": round(resp.latency_s, 1),
        "parse_error": perr if parsed is None else None,
        "gold_signal": parsed.get("gold_signal") if parsed else None,
        "confidence": parsed.get("confidence") if parsed else None,
        "rationale": parsed.get("rationale") if parsed else None,
        "framework_affinity": parsed.get("framework_affinity") if parsed else None,
        "refusal_flag": parsed.get("refusal") if parsed else None,
    }
    return row, calls


def main():
    manifest = load_manifest()
    transcript = TranscriptLogger(os.path.join(HERE, "transcripts"),
                                  runid="s1-run")
    backends = [AnthropicCLIBackend(model_alias="haiku"), OpenAICLIBackend()]
    runner = Runner(backends, transcript=transcript, timeout_s=TIMEOUT_S)
    versions = runner.versions()
    print("versions:", json.dumps(versions))
    print(f"records: {len(manifest)}  families: {len(backends)}  "
          f"timeout: {TIMEOUT_S}s")

    verdicts = []
    call_totals = {b.name: 0 for b in backends}
    t0 = time.time()
    for i, m in enumerate(manifest):
        base_prompt = build_prompt(m["prompt"], m["response_text"])
        for name, backend in runner.backends.items():
            row, calls = judge_one(backend, base_prompt, m["sample_id"],
                                    transcript, TIMEOUT_S)
            # attach held-out truth (for downstream stats ONLY; not sent anywhere)
            row["_truth_gold_signal"] = m["_truth_gold_signal"]
            row["_truth_pole"] = m["_truth_pole"]
            row["modality"] = m["modality"]
            row["tier"] = m["tier"]
            row["mock_model"] = m["model"]
            verdicts.append(row)
            call_totals[name] += calls
            print(f"[{i+1:>2}/{len(manifest)}] {m['sample_id']} [{name:>13}] "
                  f"{row['final_status']:<13} pred={row['gold_signal']} "
                  f"truth={m['_truth_gold_signal']} calls={calls} "
                  f"lat={row['latency_s']:.0f}s")

    elapsed = round(time.time() - t0, 1)
    out = {
        "versions": versions,
        "n_records": len(manifest),
        "call_totals": call_totals,
        "transcript_path": transcript.path,
        "transcript_count": transcript.count,
        "elapsed_s": elapsed,
        "verdicts": verdicts,
    }
    vpath = os.path.join(HERE, "20260709-judge-verdicts.json")
    with open(vpath, "w") as fh:
        json.dump(out, fh, indent=2)
    print("\nwrote", vpath)
    print("call_totals:", call_totals, "transcript_count:", transcript.count,
          "elapsed_s:", elapsed)


if __name__ == "__main__":
    main()
