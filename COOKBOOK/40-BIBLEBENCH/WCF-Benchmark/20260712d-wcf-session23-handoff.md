<!-- WCFBENCH-CANARY-c1647-x9k4q -->
# WCF-Bench — Session 23 Handoff (F2: gated-run pre-registration; FINAL planned Fable session)

**Date:** 2026-07-12 · **Model:** Claude (Fable) · **Session:** S23, run from
`20260712b-fable-prereg-boot-prompt.md` (Jimmy-directed). **Fable exits after this
session (R68).**

## What was done

1. **State verified (Step 0):** Codex T1/T2 **not started** — no commits after
   `d7e534aa8` on `codex/wcfbench-mvp-testable`, no handoff newer than `20260711d`, no
   corrected-manifest / re-parse directories, execution-plan-v2 boxes unchecked,
   PENDING-QUESTIONS unchanged since S22. Nothing to adjudicate; Part A taken on the
   not-done branch.
2. **MAIN DELIVERABLE — `20260712c-fable-gated-run-prereg-memo.md` (BINDING, R58–R68):**
   the complete G1–G7 gated-run (T4) pre-registration, written **conditional on the R57
   checklist passing unmodified** (R58.3: a checklist failure reopens ONLY the G4 surface
   table + judge plan; everything else stands). Highlights:
   - **R58** ratification remains open; **Jimmy may ratify T1/T2 alone via the R57
     checklist**; MVP testable stays NO until then.
   - **R59** run design: items (204 core + 22 EPISODE conditional on T2/R55 build; 4
     dev-set-only stay out; 4 contested excluded from gold-accuracy scopes); 10-SUT
     roster **by formula** (LMArena-strongest per family; anti-leakage excludes
     {google, x-ai, anthropic}; 3 MVP-continuity pins + cohere/nova); frontier = top-5
     by capability PC1; perturbation scope P3/P4/P6 only (P1/P2/P5 → T5); **$300 NTE**
     + R40.1 pre-flight + pre-registered truncation ladder; master seed **1647**;
     EPISODE judge scoring pinned to the settled-core contract (flagged interpretation
     of R55.1, amendable pre-data).
   - **R60–R66** exact gate computations: G1 (frozen 4-component battery → PC1, PASS
     r² < 0.40), G2 (ceiling 1.0/cell, best roster-frontier ≤ 0.70, construct
     disclosure), G3 (paired item bootstrap B=10k seeds 1647+k, ≥9/10 pairs p<0.01 —
     bank has **no T1**, so "T2+" = whole gold-scored bank), G4 (5 surfaces, n=40 blind
     units each, κ ≥ 0.60 ∧ ≥ 0.75× human ceiling), G5 (TF-IDF key-prediction +
     NN-key-transplant ≤ 0.20 + **ruled ICL substitute** for the impractical 10%-FT
     probe, disclosed), G6 (⌈0.85·n⌉ consensus, n≥3; contested ruling constrains the 8
     pre-identified items; release bar = 100% confirmation of quoted golds), G7
     (Cronbach's α per design + redundancy flag, no release veto).
   - **R67** freeze at first paid call; deviations need a logged Jimmy ruling BEFORE
     proceeding; silent deviation voids the gate; **labels gate RELEASE, not execution**
     (refines the execution-plan-v2 T4 gate line); Codex computes / Jimmy adjudicates.
   - **R68** close-out: Codex = standing executor, Jimmy = ratifier of record; no
     further Fable session planned.
3. **Dashboard updated** per AGENTS.md protocol: banner, Live-status (phase / owner /
   next-milestone / blockers), rulings 68, sessions 23, progress bar, **gate board
   G1–G7 → PRE-REGISTERED with pinned computations**, S23 row, YOU-ARE-HERE, Milestone
   B, critical path, docs table, update log, §Instructions (Fable paragraph → EXITED +
   Jimmy queue).

## What remains (none of it Fable's)

| Owner | Item |
|---|---|
| Codex | T1 (W-R48 → W-R47.3 → W-R49 → W-R52.2) → T2 (R54/R56 registry application) — standing boot prompt unchanged |
| Jimmy | R57-checklist ratification (alone suffices) → MVP testable per R53 |
| Jimmy | Paid-call reauth + T3 roster confirmation; T4 budget (≤ $300 NTE) |
| Jimmy | G6 rater recruitment (R65) + G4 co-labeling (R63) — gate release, not the run |
| Jimmy | Gate PASS/FAIL adjudication from Codex's gate-computation report (R67.4) |
| Codex | T4 executes `20260712c-fable-gated-run-prereg-memo.md` EXACTLY (zero judgment calls) once its execution gates open |

## Known issues / notes for the next reader

- The prereg's validity is **conditional** (R58.3) — if the R57 checklist ever fails,
  only R59.4 + R63 reopen, and that amendment is Jimmy's (or a ratified provisional).
- The G5c fine-tune substitute and the R59.4 EPISODE-judging interpretation are the two
  clauses explicitly flagged as pinned interpretations, amendable **pre-data** without
  voiding anything.
- Untracked `screenshots/` dir under WCF-Benchmark predates this session; not touched.
- No live calls, no code, no bank/gold edits, no immutable file modified this session.

**Entry points unchanged:** Codex every session → `20260712-codex-standing-boot-prompt.md`;
project state → `project-dashboard.html` (open on start, update on close).

**Canary:** `WCFBENCH-CANARY-c1647-x9k4q` (never re-minted).
