#!/usr/bin/env python
"""RP-04 S1 pilot — codex arm RE-RUN with config overrides.

The first full run's codex arm was invalidated by external config drift on the
shared machine: another session set `model_reasoning_effort = "ultra"` (invalid;
codex 0.134.0 rejects it) and `model = "gpt-5.6-sol"` (too new for this CLI).
codex then exited returncode=1 with empty output BEFORE any model call — a
config-parse error mis-surfacing as parse_failure (0.1s latency = dead giveaway).

We do NOT edit the shared ~/.codex/config.toml. Instead we subclass the OpenAI
backend to inject per-invocation `-c` overrides restoring a known-good model +
effort, so the codex arm re-runs cleanly. Anthropic verdicts are unchanged.

Result is merged into a fresh combined verdicts file; the broken codex run is
kept in the transcript as immutable evidence of the fault.
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
T1 = os.path.abspath(os.path.join(HERE, "..", "..", "t1-runner-provisional"))
sys.path.insert(0, T1)

from t1_runner import ModelRequest, Runner, ResponseStatus, TranscriptLogger  # noqa: E402
from t1_runner.backends.openai_cli import OpenAICLIBackend  # noqa: E402

from judge_prompt import build_prompt, parse_judge_output, STRICT_REMINDER  # noqa: E402
from run_judges import judge_one, TIMEOUT_S  # noqa: E402

# Known-good overrides for the installed codex 0.134.0 on this account.
CODEX_MODEL = "gpt-5.5"
CODEX_EFFORT = "high"


class OpenAICLIBackendOverride(OpenAICLIBackend):
    """codex exec with explicit -c overrides to bypass drifted shared config."""

    def _build_argv(self, request, last_file):
        return [self.cli_path, "exec", "--json", "--skip-git-repo-check",
                "--sandbox", "read-only",
                "-c", f"model_reasoning_effort={CODEX_EFFORT}",
                "-c", f"model={CODEX_MODEL}",
                "-C", self.workdir, "-o", last_file, request.prompt]


def load_manifest():
    with open(os.path.join(HERE, "20260709-sample-manifest.jsonl")) as fh:
        return [json.loads(l) for l in fh if l.strip()]


def main():
    manifest = load_manifest()
    transcript = TranscriptLogger(os.path.join(HERE, "transcripts"),
                                  runid="s1-run-codex-rerun")
    backend = OpenAICLIBackendOverride(model_id=CODEX_MODEL)
    runner = Runner([backend], transcript=transcript, timeout_s=TIMEOUT_S)
    print("versions:", json.dumps(runner.versions()))
    print(f"codex overrides: model={CODEX_MODEL} effort={CODEX_EFFORT}")

    verdicts = []
    total_calls = 0
    for i, m in enumerate(manifest):
        base_prompt = build_prompt(m["prompt"], m["response_text"])
        row, calls = judge_one(backend, base_prompt, m["sample_id"],
                                transcript, TIMEOUT_S)
        row["_truth_gold_signal"] = m["_truth_gold_signal"]
        row["_truth_pole"] = m["_truth_pole"]
        row["modality"] = m["modality"]
        row["tier"] = m["tier"]
        row["mock_model"] = m["model"]
        # record the effective model id (override, not the drifted config default)
        row["model_id"] = CODEX_MODEL
        verdicts.append(row)
        total_calls += calls
        print(f"[{i+1:>2}/{len(manifest)}] {m['sample_id']} "
              f"{row['final_status']:<13} pred={row['gold_signal']} "
              f"truth={m['_truth_gold_signal']} calls={calls} lat={row['latency_s']:.0f}s")

    out = {"versions": runner.versions(), "codex_overrides":
           {"model": CODEX_MODEL, "reasoning_effort": CODEX_EFFORT},
           "n_records": len(manifest), "calls": total_calls,
           "transcript_path": transcript.path,
           "transcript_count": transcript.count, "verdicts": verdicts}
    p = os.path.join(HERE, "20260709-codex-rerun-verdicts.json")
    with open(p, "w") as fh:
        json.dump(out, fh, indent=2)
    print("\nwrote", p, "calls:", total_calls)


if __name__ == "__main__":
    main()
