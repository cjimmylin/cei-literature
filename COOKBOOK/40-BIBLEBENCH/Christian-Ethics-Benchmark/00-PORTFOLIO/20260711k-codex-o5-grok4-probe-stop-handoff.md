<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY — O5 Codex handoff: Grok-4 probe failed; STOP trigger 8 active

**Date:** 2026-07-11. **Executor:** Codex. **Scope:** WALKWORTHY only.
**State:** Phase 0 remains complete. W1 adjudication has not started. The frozen Grok-4
reliability probe failed 0/10, so framework §6 STOP trigger 8 now blocks the Mistral
fallback pending Jimmy's Part-B sizing/model-plan ruling.

## 1. Re-entry and baseline

Codex re-read `AGENTS.md`, the living dashboard, the newest prior handoff, the PR-9
entry, Claude/Fable's PR-9 boot prompt, and the frozen W1 probe/STOP instructions. The
shared WALKWORTHY worktree was clean; newer branch commits were unrelated and already
contained the prior Codex transcript-persistence commit. No PR-9 ruling had landed.

Fresh offline baseline before the call: **276/276 tests passed**. The public loader and
existing `walkworthy.probe` CLI were used unchanged. HOLDOUT was never loaded.

## 2. Exact bounded live action

After Jimmy said to continue, Codex executed only the pre-registered reliability probe:

- explicit model: `x-ai/grok-4`;
- sample: one public prompt per design, 10 total;
- reliability floor: 0.90;
- new immutable output:
  `runs/20260711-o5-grok4-probe/probe_report.md`.

Result: **0/10 successful; 0.00; DROP**. Every sampled call returned an OpenRouter HTTP
404 for `x-ai/grok-4`. The probe transport did not report a dollar charge; there were no
successful generations. No other model was called.

## 3. Mechanical consequence

Framework `20260711d-fable-o5-decision-framework.md` §6 trigger 8 applies because the
Grok-4 probe failed and the frozen Mistral fallback would own-family-exclude more than
10% of pending records in every design (minimum already audited: 14/122 = 11.5% on 02).

Codex therefore stopped without:

- calling `mistralai/mistral-large-2512` as the tie-breaker;
- choosing a Part-B increment or a replacement model;
- creating/running the W1 tie-breaker module;
- authorizing or running the ~$10–15 six-SUT 02/07 re-execution;
- running W2, W3, W4, W5, any G4 wave, or any verdict assembly.

The result was appended to PR-9 in `PENDING-RULINGS.md`; the living dashboard was updated
in place. Frozen reports/rules, the O4 run, label CSVs, designs, and HOLDOUT were untouched.

## 4. Decisions still required

PR-9 remains the single active blocker:

1. **Jimmy:** authorize a new immutable 02/07 re-execution that retains full transcripts,
   or supply recovered transcripts.
2. **Fable/Jimmy:** rule whether W1 covers the full §B `needs_adjudication` surface and
   route the 20 non-tie-breakable parse/arbiter pendings.
3. **Jimmy (STOP trigger 8):** accept the Mistral fallback and rule the resulting Part-B
   label increment, or issue a logged §E model-plan amendment.

Do not resume W1 until all three are logged. Then run the fresh test baseline, create the
authorized re-execution under a NEW run directory, verify complete 02/07 turn transcripts,
and resume at W1—never skip to W2.

## 5. Files added/updated

- `runs/20260711-o5-grok4-probe/probe_report.md` (NEW immutable evidence)
- `00-PORTFOLIO/PENDING-RULINGS.md` (PR-9 append-only update)
- `00-PORTFOLIO/project-dashboard.html` (required living update)
- this NEW dated handoff
