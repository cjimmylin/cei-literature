# WCF-Bench — Next-Session Boot Prompt (Opus build: R42–R45 execution; paste after /model opus + /clear)

Continue WCF-Bench (scope-locked to `COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`). You are an
**Opus build session** executing the binding directives of the session-16 Fable memo
`20260711-fable-mvp-disagreement-adjudication-memo.md` (R42–R46) — read it FIRST and in
full; every judgment call you might face is already ruled there. Mock-first TDD throughout;
suite baseline 444 green. No re-litigating rulings; deviations stop the work and surface
to Jimmy/Fable.

## Ordered worklist (R45.5 sequencing — one manifest event, no wasted re-qual)

1. **R45.4 + R45.3 harness fixes (template-free; no re-qual triggered):**
   - `_AXIS_SCORE_RE` final-answer parse: LAST match, preferring a line-anchored terminal
     `SCORE:` line (triaxial.py:275 uses first-match `.search` today). Regression fixtures =
     the two persisted gemini verdicts named in R42.1(1)/(2), verbatim from
     `07-PILOTS/20260710-mvp-run/transcripts.jsonl` (WHOLE-C1-004×deepseek manner: arithmetic
     `Score: 2.5 / 5.0 = 0.5` then final `SCORE: 0.5` → must parse 0.5; MEND-C5-W204×llama
     matter: per-KP `*Score: 0.0*` lines then final `SCORE: 0.25` → must parse 0.25).
   - `disagreement.py`: spread over eligible+non-fenced values (or parallel
     `eligible_spread`), per-judge eligibility/fence annotations, `split_defensible`
     documented contested-only (R42.5).
   - Cost estimator (R45.3): prefer per-request actuals; missing price = FAIL-LOUD, never
     silent 0; `--budget` enforces max(estimate, actuals); post-run reconciliation line.
   - Optional: award-quote grounding defect log (diagnostic only, not a gate) per R45.4(iii).
2. **R44 format-bridge + R43 roster drop → NEW COMBINED MANIFEST:**
   - Build the few-shot OPEN-award exemplar per R44.1 (non-bank, non-holdout, theologically
     neutral, canary-free, frozen into fixtures, rides the template hash).
   - Drop gpt-4o-mini from the panel (R43): panel of record = gemini-flash + grok-4.20.
     No gpt re-qual; its persisted raws stay untouched.
   - Full K=8 re-qual of gemini + grok on ALL their surfaces under the new hashes (R35
     semantics, ≥5/8), then re-screen EXACTLY grok / cohere-command-a / amazon-nova-pro on
     the OPEN-award gate under the bridged template (discrimination bar NOT relaxed); ride
     a K=8 coherence battery for cohere+nova on the same run (R43.4). Budget cap $10;
     R40.1 key pre-flight first (`GET /api/v1/auth/key`; ~$30 remained on the key
     2026-07-10). New dated pilot dir; new manifest of record supersedes
     `20260710-settled-requal`.
3. **R45.2 EPISODE live runs** — 22 NARROWGATE items × 4 SUTs (88 cells) via
   `episode_live.py` under the NEW manifest: checkpoint/resume, per-cell error survival,
   R27 transcripts, disagreement records, refusal taxonomy, budget cap, DESCRIPTIVE/PRE-GATE
   report labeling (R34.4 language as applicable post-screen).
4. **R45.1 PROOFTEXT judge-assisted upgrade** (`judge_score_anchor_use` path) + persisted
   re-read of MVP-run PROOF responses in a NEW dated dir (no new SUT calls); acceptance
   criteria and delta-reporting exactly per R45.1. PROOF numbers stay non-quotable until
   this lands.

Item 1 may ship alone if the session runs short; 2→3→4 are strictly ordered.

## Guardrails (unchanged)

No deletions (mv to RECYCLE-BIN only). Report immutability — all `07-PILOTS/` dirs
append-only; new dated dirs/reports only. Canary `WCFBENCH-CANARY-c1647-x9k4q` never
re-minted into new item/exemplar content. Shared git index LIVE: `git log -1` before every
commit, explicit paths, never `git add -A` (sibling sessions' dirty files off-limits).
Secrets runtime-only (`~/.codex/secrets/openrouter.env` pattern), never committed. Validate
with the full pytest suite before each commit. End with a dated handoff + update the
`wcf-bench-portfolio-state` memory note.

> Standing context: G6 (Jimmy's raters) still gates the gated G1–G7 run, H-DISC promotion,
> W304/W305 position maps, and the 4 LIB `[DISPUTED]` legs. Earlier-wave transcription
> backfill stays deferred (fabrication-sensitive). Nothing is Fable-blocked.
