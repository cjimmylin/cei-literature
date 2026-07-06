# DUPLEX P0 — runner + pre-registered analysis

Vendor-neutral runner and pre-registered gate analysis for the **DUPLEX falsification-first P0
smoke test** (design `COOKBOOK/20-DESIGNS/03-moralpsych-duplex.md` §7). Built fresh inside
COOKBOOK — imports nothing from sibling projects.

> **P0 question:** does the *process* axis discriminate models *at all* (G1/G2/G3, §7) before any
> generator is built? P0 PASS → build the generator; P0 FAIL → DUPLEX loses the build-first slot
> to CRUX and is re-scoped as a universal-signature *measurement* instrument.

## Layout

```
DUPLEX-P0/
  config/p0-roster.yaml     # model roster + resource conditions + gate thresholds (single switchboard)
  runner/
    adapters.py             # AdapterResult + Anthropic / OpenAI-Codex / Gemini adapters (only live-call site)
    roster.py               # load roster, enabled-model list
    judges.py               # cross-family judge routing + judge-neutrality meta-eval
    items.py                # normalize the authored item bank -> runner record shape
    orchestrator.py         # administer x cell, checkpoint/resume, refusal category, per-condition SD, JSONL
  analysis/
    stats.py                # CV (denominator-guarded), Welch p (zero-variance-safe), sign
    gates.py                # G1 process_beats_content, G2 pairwise_separation, G3 greene_direction, run_p0_gates
    shortcut_audit.py       # X2: lexical_length_baseline + FineTuneProbe interface + combined verdict
  items/                    # authored bank (20260706-p0-item-bank.json) — read if present, not required by tests
  results/                  # orchestrator JSONL output lands here
  tests/                    # pytest — mocked adapters + gate fixtures that PASS and FAIL each gate
```

## Run the tests (no creds, no live calls — everything mocked)

```bash
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest \
  COOKBOOK/20-DESIGNS/DUPLEX-P0/tests/ -q
```
Current status: **48 passed**. The suite mocks the Anthropic SDK client and the Codex
subprocess, and drives each gate with synthetic fixtures engineered to pass AND to fail.

## Config choice: YAML

The roster is `config/p0-roster.yaml` (real YAML; `pyyaml` is in the vault venv). `roster.load_roster`
also accepts `.json`, so a dependency-free JSON sidecar can be dropped in later with no code change.

## Design-faithful pieces (map to §3.5 / §4 / §7 / KB04 §6.2 / KB07)

- **Vendor-neutral adapter interface** `administer(prompt, model_id, temperature, seed) -> {text, raw, refusal_flag, latency}` (adapters accept extra per-condition gen kwargs: `max_tokens`, `thinking`, `system`).
- **Generator ≠ subject ≠ judge by family** — `judges.assign_judges(subject_vendor, roster)` returns only cross-vendor judges; a judge never shares a vendor with the subject it scores (§3.5 / KB07 L54). `judges.judge_neutrality_check` is the mirror-image equal-flip meta-eval (KB07 §2).
- **Orchestration** — ≥10 reps/cell, temperature>0 enforced, deterministic per-rep seeds, idempotent checkpointing keyed on `(item_id, model_id, resource_condition, seed)`, resume-from-checkpoint, explicit **refusal category** (§4; refusals get `score=None` and are excluded from distributions), **per-condition SD as a first-class output** (`per_condition_sd`).
- **G1** denominator-guarded cross-model CV (process vs matched content baseline) with per-condition-SD dead-cell exclusion applied **before** the CV (§4).
- **G2** KB04 §6.2 bar: ≥90% of model pairs separated at p<0.01 on ≥1 manipulation, **plus a one-vs-N outlier guard** so a single outlier-vs-rest split does not pass.
- **G3** replication direction vs a parameterized human anchor, with the pre-registered M3 fallback (agent-patient + time-pressure) when no anchor is supplied.
- **X2 shortcut audit** — `lexical_length_baseline` (must sit ≈ chance) + `FineTuneProbe` interface (10%-fine-tune, stubbed) + `combined_shortcut_verdict` (lexical ≈ chance AND probe below parity).

## How to run for real (once creds exist)

```python
import sys; sys.path.insert(0, "COOKBOOK/20-DESIGNS/DUPLEX-P0")
from runner import (load_roster, enabled_models, build_adapter, load_item_bank,
                    Orchestrator, Checkpoint, per_condition_sd, load_results)
from analysis import run_p0_gates

roster  = load_roster("COOKBOOK/20-DESIGNS/DUPLEX-P0/config/p0-roster.yaml")
models  = enabled_models(roster)                        # 3 Anthropic + 2 OpenAI (Gemini disabled)
items   = load_item_bank()                              # normalizes items/20260706-p0-item-bank.json
adapters = {v: build_adapter(v) for v in {m["vendor"] for m in models}}

# scorer must route to a CROSS-FAMILY judge (assign_judges) + a judge adapter — wire a real
# rubric-scored judge here; it must never share a vendor with the subject being scored.
def scorer(text, item, subject_vendor): ...            # TODO(live): implement cross-family judge

orch = Orchestrator(
    adapters=adapters, models=models, item_bank=items,
    conditions=roster["resource_conditions"], scorer=scorer,
    reps=roster["reps_per_cell"], temperature=roster["temperature"],
    base_seed=roster["base_seed"],
    out_path="COOKBOOK/20-DESIGNS/DUPLEX-P0/results/20260706-p0-run.jsonl",
    checkpoint=Checkpoint("COOKBOOK/20-DESIGNS/DUPLEX-P0/results/20260706-p0.ckpt"),
)
records = orch.run()                                    # resumable; safe to re-run
verdict = run_p0_gates(records, roster["p0_gates"])     # {G1, G2, G3, overall_pass}
```

## OPEN ITEMS blocking a live run (must be resolved first)

1. **OpenAI = OAuth Codex CLI presence + auth.** `codex` must be on PATH (found: `codex-cli 0.134.0`)
   **and authenticated** (`codex login`; `shutil.which` alone does not prove auth). The command
   template is `codex exec -m <model> --skip-git-repo-check --ephemeral --color never -o <file> -`
   (prompt on stdin, final message read from `-o`). TODO(live): (a) confirm `-m gpt-5-codex` /
   `-m gpt-5-mini` resolve on the installed codex; (b) `codex exec` is an **agentic** runner, not a
   chat completion — confirm the flags/`-c` config that force a single-turn moral-judgment answer
   (read-only sandbox, no tool use); (c) codex exposes no temperature/seed flags today
   (`temperature`/`seed` are recorded for bookkeeping only).

2. **Gemini DEFERRED.** `GeminiAdapter.administer` raises `NotImplementedError`. The 4 Gemini
   subjects (§3.5) are present-but-disabled in the roster. To enable: implement the adapter
   (google-genai / Vertex), then flip `vendors.google.enabled` + each model's `enabled` to `true`.
   Until then P0 runs on 5 of the 9 subjects — note this in any P0 write-up.

3. **Haiku 3.5 is RETIRED.** The design names `Haiku 3.5` specifically (it is the single model that
   produced the MP-DP effect that motivates DUPLEX), but `claude-3-5-haiku-20241022` was retired
   2026-02-19 (replacement `claude-haiku-4-5`). The roster keeps the design-named ID with a
   `status: RETIRED` flag so the decision is conscious: substitute `claude-haiku-4-5` (changes the
   subject that showed the effect) or pin an available legacy Haiku snapshot. **Decide before a live
   run.**

4. **Human mini-norm for G3.** G3 is anchored to a measured human utilitarian-shift direction
   (§7 G3 / §5 M3). `config g3_human_anchor` is `null` — until the P0 human mini-norm is collected,
   G3 runs in **M3 fallback mode** (agent-patient + time-pressure direction, reported as descriptive
   resource-sensitivity, not an anchored dual-process claim). Collect the mini-norm and set
   `g3_human_anchor` to its sign/effect to run G3 anchored.

5. **Anthropic thinking + temperature.** The `extended_thinking` condition sends
   `thinking={"type":"adaptive"}`; §3 requires temperature>0. Opus 4.6 / Sonnet 4.6 accept
   `temperature` (unlike 4.7/4.8/Fable), but historically extended thinking constrained
   `temperature` on 4.x. TODO(live): verify temperature+thinking is accepted on the installed
   SDK/models; if the API rejects it, drop temperature for the thinking condition only.

6. **G1 content-axis baseline mapping.** G1 compares the process axis to a *matched content-axis
   baseline* (`axis == "content"`). The authored bank labels the §5 non-moral **discriminant
   control** via `is_discriminant_control` (mapped to `axis="discriminant_control"`), which is NOT
   the same construct. The analyst must designate which records constitute G1's content baseline
   (a matched content-benchmark run on the same models, or a relabelled subset) before running G1.
