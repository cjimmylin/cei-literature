#!/usr/bin/env python
"""RP-04 S1 pilot — calibration probes (<=5 per family).

Sends a handful of sampled (scenario, response) pairs through both judge families
to verify the rubric template parses and both CLIs emit usable JSON, BEFORE the
full run. Real-token GREEN-lane calls; all logged to a transcript.
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
T1 = os.path.abspath(os.path.join(HERE, "..", "..", "t1-runner-provisional"))
sys.path.insert(0, T1)

from t1_runner import ModelRequest, Runner, ResponseStatus, TranscriptLogger  # noqa: E402
from t1_runner.backends.anthropic_cli import AnthropicCLIBackend  # noqa: E402
from t1_runner.backends.openai_cli import OpenAICLIBackend  # noqa: E402

from judge_prompt import build_prompt, parse_judge_output  # noqa: E402

N_PROBES = 5


def load_manifest():
    path = os.path.join(HERE, "20260709-sample-manifest.jsonl")
    with open(path) as fh:
        return [json.loads(l) for l in fh if l.strip()]


def main():
    manifest = load_manifest()
    # pick 5 diverse probes: spread modality and gold/nongold
    picks, seen = [], set()
    for m in manifest:
        key = (m["modality"], m["_truth_gold_signal"])
        if key not in seen:
            seen.add(key)
            picks.append(m)
        if len(picks) >= N_PROBES:
            break
    # top up to 5 if fewer distinct keys
    for m in manifest:
        if len(picks) >= N_PROBES:
            break
        if m not in picks:
            picks.append(m)

    transcript = TranscriptLogger(os.path.join(HERE, "transcripts"),
                                  runid="s1-calibrate")
    backends = [AnthropicCLIBackend(model_alias="haiku"), OpenAICLIBackend()]
    runner = Runner(backends, transcript=transcript, timeout_s=260)
    print("versions:", json.dumps(runner.versions()))

    rows = []
    for m in picks:
        prompt = build_prompt(m["prompt"], m["response_text"])
        req = ModelRequest(prompt=prompt, item_id=m["sample_id"],
                           params={"model": "haiku", "sample_id": m["sample_id"]})
        for name, backend in runner.backends.items():
            resp = backend.run(req, timeout_s=runner.timeout_s)
            transcript.log(resp)
            parsed, err = parse_judge_output(resp.text)
            rows.append({
                "sample_id": m["sample_id"], "modality": m["modality"],
                "family": name, "status": resp.status.value,
                "model_id": resp.model_id_reported, "latency_s": round(resp.latency_s, 1),
                "parsed_ok": parsed is not None, "parse_err": err,
                "gold_signal": parsed.get("gold_signal") if parsed else None,
                "truth_gold": m["_truth_gold_signal"],
            })
            print(f"[{m['sample_id']}][{name:>13}] {resp.status.value:<12} "
                  f"parsed={parsed is not None} "
                  f"pred={parsed.get('gold_signal') if parsed else None} "
                  f"truth={m['_truth_gold_signal']} lat={resp.latency_s:.0f}s")

    summary = {"transcript": transcript.path, "count": transcript.count,
               "versions": runner.versions(), "rows": rows}
    with open(os.path.join(HERE, "20260709-calibration-summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2)
    print("\ncalibration transcript:", transcript.path, "count:", transcript.count)
    # parse-rate per family
    for fam in ("anthropic_cli", "openai_cli"):
        fr = [r for r in rows if r["family"] == fam]
        okp = sum(1 for r in fr if r["parsed_ok"])
        print(f"  {fam}: {okp}/{len(fr)} parseable")


if __name__ == "__main__":
    main()
