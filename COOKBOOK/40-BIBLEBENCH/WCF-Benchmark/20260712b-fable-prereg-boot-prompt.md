# WCF-Bench — NEXT FABLE SESSION Boot Prompt: gated-run pre-registration (+ ratification if ready)
# (paste after /model fable + /clear · SUPERSEDES `20260712-fable-f2-boot-prompt.md`)

Continue WCF-Bench (scope-locked to `COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`). You are the
project's **final planned Fable session** (judgment only — pre-register + ratify; builds
are Codex's, per the permanent handover `20260712-wcf-codex-handover-plan.md`). Your
**main deliverable is the binding G1–G7 gated-run pre-registration** — it does NOT wait
on Codex: if Codex's T1/T2 are not done yet, write the pre-registration **conditioned on
the R57 checklist passing unmodified** (the post-T1/T2 state is already fully
pre-registered: R57 pins the corrected manifest cell-by-cell, R54 pins the EPISODE
registry). Jimmy has directed this session explicitly (2026-07-12).

> **Fallback if the Fable window has lapsed:** run this same boot on **Opus in
> PROVISIONAL mode** — draft everything with R-numbers RESERVED; binding only on Jimmy's
> written ratification.

## Step 0 — state load

1. `project-dashboard.html` — Live-status + §Instructions first. Determine: has Codex
   run? Are execution-plan-v2 **T1/T2** checked? Read the newest
   `*codex-session-handoff.md` and `PENDING-QUESTIONS.md` (verify provenance of anything
   marked resolved since S22).
2. Binding baseline (never relitigated): `20260712-fable-ratification-memo.md` (R47–R53)
   + `20260712-fable-episode-registry-review-memo.md` (R54–R57). Skeleton spec you will
   flesh out: `20260711-fable-next-session-boot-prompt.md` **agenda item 2** (its gate
   list is valid; update it for R47/R53/R54).
3. If T1 evidence exists (corrected-manifest dir, W-R49 re-parse dir, fixtures): load it
   for the ratification half. If not, skip — do not build any of it yourself.

## Agenda (ONE binding memo, R58+, new dated file)

### A. Ratification — do as much as the state supports

- **If T1+T2 are done:** ratify against the **R57 checklist** (cell-by-cell manifest
  equality with memo §2 F-1/F-2; three bidirectional W-R48 fixtures; W-R49 delta table
  covers exactly 155 verdicts / 65 OPEN cells with originals untouched; registry approval
  block per R56; suite green). Resolve escalations sample-level (R29/R31 mode). Then
  **declare the corrected manifest the manifest of record** and rule **MVP testable**
  per R53 (state all four conditions). A checklist failure → bounded correction order to
  Codex, never a rerun or improvisation.
- **If not done:** record that ratification remains open, reaffirm that Jimmy may ratify
  alone via R57, and proceed to B — the session's value does not depend on Codex's pace.

### B. MAIN DELIVERABLE — the binding gated-run pre-registration (G1–G7)

Freeze the exact computations BEFORE gated data exists (WALKWORTHY prereg rigor as
precedent, content never cross-wired). Pin, at minimum:

- **G1 · Capability correlation:** the capability battery (which public scores/source,
  frozen list), PC1 construction, the exact correlation computed on hard-tier scores,
  the <40% pass test.
- **G2 · Headroom:** ceiling definition per scorer kind, the ≤~70% frontier-headroom
  test on T3/T4, and which models count as "frontier" for it.
- **G3 · Separation:** bootstrap over items (B, seed policy — seeds fixed in the memo),
  the frontier pair set, ≥90%-of-pairs-at-p<0.01 on T2+.
- **G4 · Judge validity:** κ form + weights vs the G6 human labels, human–human ceiling
  handling, per-surface application (OPEN single-family-labeled per R47/R44.5 branch (b),
  disclosure, settled-core, coherence — and EPISODE per R55.1 judge-scored transcripts),
  and the consequence for a surface that fails.
- **G5 · Shortcut:** the lexical-baseline model and the 10%-fine-tune probe design, or a
  ruled, disclosed substitute if fine-tuning is impractical.
- **G6 · Human consensus:** how ≥85% consensus maps onto gold / [DISPUTED] /
  position-cards (constrained by `20260709-contested-item-scoring-ruling.md`); what
  happens below threshold.
- **G7 · Reliability:** the per-design internal-consistency statistic and the α>0.99
  redundancy flag.
- **The run design:** SUT roster + anti-leakage rule (no SUT from the judge families
  {google, x-ai} or item-generator families; name the roster or the selection rule);
  items in scope — all 230 incl. the 22 EPISODE items (scored per R55.1
  screen-plus-judge; if T3 hasn't run, the prereg states how EPISODE enters the gated
  run) and PROOF under the R52 ruled mechanical gate with disclosure; perturbation
  subset (P3/P4/P6 materialized; P1/P5 need paid materialization — say which are in
  scope); budget cap + R40.1 pre-flight; per-cell checkpoint/resume; raw evidence
  append-only.
- **Deviation protocol:** the prereg is FROZEN once gated data exists; any deviation
  needs a logged Jimmy ruling BEFORE proceeding; silent deviations void the affected
  gate.
- **Conditionality clause (if T1/T2 unratified at writing):** the prereg is valid iff
  the R57 checklist later passes unmodified; a checklist failure reopens ONLY the
  manifest-dependent clauses (G4 surface table, judge plan), which then need a Jimmy or
  judgment-tier amendment — everything else stands.

It must be executable by Codex with **zero judgment calls**. Nothing in it may
relitigate R1–R57.

### C. Handover close-out

State in the memo that this closes the planned Fable involvement: Codex = standing
executor, Jimmy = ratifier of record (provisional packets, reserved R-numbers), the
remaining human gates are Jimmy's ($/roster for T3, G6 recruitment, budget for T4).
Update the handover plan's F2 row via the dashboard (the plan file itself is dated —
do not edit it; the dashboard is the living record).

## Guardrails

Adjudication/pre-registration only — no code, no live calls, no gold minted, no item
edits, no G6 activity, no candidate screening (ladder CLOSED, R47.4). New dated files
only; `project-dashboard.html` is the sole undated exception. Canary
`WCFBENCH-CANARY-c1647-x9k4q` never re-minted. Shared git index LIVE (`git log -1`
before every commit; explicit WCF-Benchmark paths; never `git add -A`). Sibling benches
read-only precedent at most.

## On session close (mandatory)

1. Update `project-dashboard.html` per `AGENTS.md §The project dashboard`: last-updated,
   Live-status (prereg now live; MVP-testable status per part A), **gate board rows the
   prereg pins**, progress bars, S-row, milestone checkboxes if ratified, update-log
   line, **rewrite §Instructions for next session** (next = Codex T-queue; Fable exits —
   point any future judgment need at provisional-packet → Jimmy).
2. Update the `wcf-bench-portfolio-state` memory note + MEMORY.md index line.
3. New dated session handoff; commit explicit paths + push.

**On session open: load `project-dashboard.html` (Live-status first).**
**On session close: update the dashboard per `AGENTS.md §The project dashboard`.**
