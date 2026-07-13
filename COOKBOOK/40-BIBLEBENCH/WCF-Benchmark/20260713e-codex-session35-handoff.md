# WCF-Bench — Codex Session 35 Handoff

**Date:** 2026-07-13

**Paper-facing close:** T3 empirical evidence complete; controlling result remains
**DESCRIPTIVE/PRE-GATE**.

**Next milestone:** T4 gate-computation evidence, still blocked on task-specific Jimmy
authorization. No T4 paid call is authorized.

## 1. Authorization and implementation record

Jimmy authorized exactly one T3 run in
`20260713d-jimmy-t3-authorization-record.md`: 22 approved EPISODE items × four fixed
SUTs, scored by the manifest-of-record Gemini + Grok panel, under a strict `$10.00` NTE
cap. The authorization excluded T4, reruns, substitute models, prompt changes, panel or
manifest changes, G6 work, and bank edits.

The offline runner and bounded review/fix sequence is recorded in these WCF-Bench commits:

- `aa00c7009` — build offline T3 EPISODE runner
- `e3f11f9b4` — retain T3 error-cell usage
- `d3e579bf2` — checkpoint paid T3 stop cells
- `7006973da` — account for missing T3 usage
- `550903034` — align T3 report completion status
- `af6bafb82` — secure T3 retry accounting and resume
- `fd8d6a69c` — make T3 raw ledger crash safe

Offline validation reached **676 passing tests**. The exact R40.1 pre-flight completed in
seconds before the live invocation; it is not included in the source-observed run interval
reported below.

## 2. Live run and controlling correction

The single authorized live run finished **COMPLETE** with all 88 planned cell records.
Its original immutable artifacts report **88 scored, 0 error-recorded**. An independent
artifact audit found one anomaly:
`NARROW-C7-010::anthropic/claude-haiku-4.5` had an incomplete Gemini emission
(`finish_reason="error"`, zero usage, 1/5 required verdicts, no retry emission) but was
recorded as scored.

Shared-worktree custody is explicit: commit `910b5c013` captured `t3-run-identity.json`
plus the active partial snapshot at 33 checkpoints / 100 raw emissions; immediately
following commit `296bdcc97` appended 1 checkpoint / 2 emissions, leaving the committed
HEAD snapshot at 34 / 102 while the authorized process was still running. The final
Session 35 close commit append-completes that same run to 88 / 264 and adds the final
report/metadata, without rewriting either earlier commit or the original evidence.

No paid rerun or model-behavior debugging followed. A new, zero-cost offline correction
preserves the original artifacts as primary evidence and controls the T3 descriptive
summary:

- **87 scored + 1 error-recorded** across 88 recorded cells
- **80 graded + 7 wholly ungraded**
- mechanical/judge **agreement 36 · disagreement 44**
- overall graded mean **0.50375**
- `meta-llama/llama-3.1-8b-instruct`: n=20, mean **0.19167**; 2 wholly ungraded
- `deepseek/deepseek-chat`: n=20, mean **0.34833**; 2 wholly ungraded
- `mistralai/mistral-large-2512`: n=19, mean **0.50000**; 3 wholly ungraded
- `anthropic/claude-haiku-4.5`: n=21, mean **0.95238**; 1 error-recorded

The original 88-scored report remains immutable provenance; it is superseded only for
descriptive status and summary by the offline correction. No benchmark claim, gate
adjudication, ruling, R-number, judge-panel change, or manifest change is made.

## 3. Cost, timing, and disclosed limitations

- Response-attributed T3 cost: **`$0.4393786622`**; 0 accounting fallbacks; under the
  `$10.00` cap.
- Shared-key usage delta: **`$2.439582089`**, from usage `$1432.872705984` to
  `$1435.312288073`. This interval is contextual/contaminated by shared-account activity
  and is not attributed to T3.
- Source-observed wall interval: **41m58s**, labeled exactly as run-directory birth
  (`2026-07-13 07:16:28 -0700`) to final run artifacts
  (`2026-07-13 07:58:26 -0700`). The seconds-long pre-flight occurred before this and is
  not included; no more precise controller wall-time claim is made.
- Exactly three length truncations remain preserved evidence and were not reclassified:
  `NARROW-C7-W205 × deepseek/deepseek-chat`,
  `NARROW-C7-W205 × mistralai/mistral-large-2512`, and
  `NARROW-XC-W306 × mistralai/mistral-large-2512`.

## 4. Artifact map

Primary immutable run artifacts:

- `07-PILOTS/20260713-t3-episode-run/raw-evidence.jsonl`
- `07-PILOTS/20260713-t3-episode-run/checkpoint.jsonl`
- `07-PILOTS/20260713-t3-episode-run/run-metadata.json`
- `07-PILOTS/20260713-t3-episode-run/episode-report.md`
- `07-PILOTS/20260713-t3-episode-run/t3-run-identity.json`

Controlling offline correction:

- `07-PILOTS/20260713-t3-episode-offline-correction/20260713-t3-episode-offline-correction.json`
- `07-PILOTS/20260713-t3-episode-offline-correction/20260713-t3-episode-offline-correction.md`

Authorization and standing state:

- `20260713d-jimmy-t3-authorization-record.md`
- `20260712-codex-execution-plan-v2.md`
- `PENDING-QUESTIONS.md`
- `project-dashboard.html`

## 5. Remaining gates and next safe action

T3 is complete and its exact authorization is consumed. T4 is the first unchecked
execution task, but no T4 paid calls are authorized. Jimmy must still provide a
task-specific written T4 roster, budget, cap, and paid-call authorization; R40.1 pre-flight
then remains mandatory. G6 recruitment/co-labeling and R67.4 gate adjudication remain
Jimmy-owned. Paper P3 waits for the T4 gate report plus R67.4; P4 waits for P3. Task 6
remains deferred under R52.

**Next safe action:** request Jimmy's bounded T4 authorization or record an explicit
escalation. Do not start a new implementation/review loop, run T4, rerun T3, or investigate
isolated model behavior without new authority.

Session allocation estimate: **empirical execution 40% · paper work 0% · infrastructure
50% · governance/admin 10%**.

## 6. Dashboard verification limitation

The established in-app browser policy blocks local `file://` dashboard pages and prohibits
retry/workaround/alternate-surface bypass after the prior rejection. Final rendered visual
verification was therefore unavailable. The close used source/structural HTML validation,
verified the banner, Live status, S35 row, newest update-log row, and next-session block,
and preserved the required open/close instructions. No browser verification claim is made.
