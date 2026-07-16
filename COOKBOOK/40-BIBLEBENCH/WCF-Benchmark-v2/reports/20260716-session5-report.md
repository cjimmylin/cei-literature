# WCF-Benchmark-v2 — Session-5 consolidated report

> **EXPLORATORY / NON-QUOTABLE.** 2026-07-16. Boot prompt:
> `20260716-session5-boot-prompt.md`. Mission: item-level assessment of the s4
> pilot, kin-delta measurement, v2.2 design + cheap-fix validation, session-6
> runbook — NO roster expansion (honored).
> Spend: **$7.68 upper bound** by credits delta (1732.2533 → 1739.9308; concurrent
> same-key sessions inflate it), ≈ $4–5 by per-run token attribution
> (kin regrade ≈ $3.5, validation ≈ $0.2–1). Ceiling $10: met.

## 1. Phase 1 — $0 item-level assessment (from logs alone)

Full detail: `reports/20260716-session5-phase1-triage.md`,
`analysis/20260716-session5-item-{matrix,triage}*.{json,csv}`.

- **Triage (221 items, exact rules stated):** DEAD-CEILING **119 (53.8%)** /
  NOISY 39 / CORE-DISCRIMINATING 38 / TIER-BREAK-ONLY 25 (21 of them flat).
- **Episodes verdict: REFUTED as a frontier engine** — 1.06× CORE enrichment,
  within-tier-1 spread 6.2 (below main's 9.9); but they own the tier break
  (gap 36.2). Accurate claim: tier-break engine, not frontier engine.
- **Design anatomy:** complicit/steadfast/crosswind carry 21/38 CORE;
  **aggravate = 0/24 CORE**. 13/38 CORE items are tier-inverting.
- **Panel health:** gemini harsh profile persists moderated (−6.48 vs −8.6 s3);
  lone-outlier rates gemini 5.0% / mistral 2.4% / deepseek 1.7%; quorum failures
  exactly 5/1105; no new grader drift. Gemini sits ≥20 below the other two on 23%
  of samples — the median panel absorbs it.

## 2. Fable re-reads (main loop)

Full detail: `reports/20260716-session5-fable-rereads.md`.

- **G-partition (23 diffuse-disagreement items): critique-01's "25% hard ethics"
  DISSOLVES** → 12 repairable RUBRIC-AMBIGUITY (52%) + 8 sub-threshold grader
  noise (35%, 7 of them gemini-harsh at gap 20–29) + only **3 genuinely hard**
  (NARROW-C1-006, WHOLE-C6-009, CROSS-C10-009). Partition validated against pilot
  panel spreads (AMBIG 18.1 / NOISE 12.8 / HARD 21.1 vs bank 13.8).
- **Anchor recall boundary:** the "0 contaminable items" claim reproduces under
  its stated Standards-verbatim rule with ONE borderline (LIB-C4-002 ≈ 0.5), and
  is RULE-DEPENDENT — anchor/prooftext items reward public-corpus exegetical
  recall **by design**; required phrasing recorded in the re-reads report.

## 3. Phase 2 — kin-delta (measured) + RULING

Full detail: design memo §6; `analysis/20260716-session5-kin-{matrix,stats}.json`.
Design upgrade over the boot spec: **qwen3.7-plus added as non-kin control** so the
ruling rests on a difference-in-differences, not a raw two-panel delta (the raw
delta contained a +2.3…+4.0 level shift that would have masqueraded as kin bias).

- Ordering kin-robust (all 5 graders agree); **self-kin (deepseek grading
  deepseek) = +1.67 [+0.14, +3.27]** — real, small, ranking-relevant within tiers;
  **family-kin (mistral-small grading mistral-large) = +0.97 [−0.51, +2.46]** — ns.
- **RULING:** mistral family UNLOCKED (accept-and-disclose); deepseek family
  UNLOCKED with a −1.7-pt sensitivity rule on within-tier claims; google family
  CONDITIONALLY unlocked (gemini-kin never measured — S6-C piggyback mandatory
  before quoting). command-r flagged as a weak grader (20.2% lone-outlier) — do
  not reuse in audit panels.

## 4. Phases 3–4 — v2.2 design, implementation, validation verdicts

Design frozen in `reports/20260716-session5-v22-design.md` (3 levers + s6
authoring pipeline + **binding bank-versioning rule**; manifest
`data/BANK-VERSION.json`, bank_version v2.2, 199+22, 60/60 tests, per-item edit
log `reports/20260716-session5-item-edit-log.md`).

Validation micro-run (90 samples, 3 SUTs, isolated configs, unscored 0/90,
~$0.2–1; `analysis/20260716-session5-validation-results.json`), judged against the
PRE-STATED metrics:

- **Lever A (excellence gate): FAIL — 1/15** DEAD items produced nonzero
  |qwen−haiku| (needed ≥8/15). Both tier-1 SUTs still hit exactly 100 on 14/15.
  The gate DOES bite below the frontier (gpt-4o-mini fell to 67–80 on 4
  previously-consensus-100 items) → kept as v2.2 default for sub-frontier
  texture, but **the frontier ceiling is capability-parity in the graders' eyes,
  not a scoring artifact**. Pre-stated branch executed: **"new items needed"
  CONFIRMED — session 6 is authoring-first.**
- **Levers B+C (rubric repairs): PASS — 8/12** AMBIG items reduced panel spread
  below their pilot baseline (needed ≥7; e.g. COMP-C8-W306 40→3.3, COMP-C2-002
  55→13.3) and **2/3** changed contested items (needed ≥2). Two repairs flagged
  for s6 re-review: COMP-C4-005 (spread 20→43, haiku=0 outlier under the new
  checkable-structure criterion) and DUTY-XC-W206 (6.5→16.3, one quorum drop).
- Caveat: single-draw scores on both sides of every comparison; verdicts are
  design decisions, not quotable measurements.

## 5. Phase 5 — session-6 runbook

`reports/20260716-session6-scaleup-runbook.md`: authoring-first sequencing with a
frontier-core GO/NO-GO gate, 16-SUT longlist with live-verified slugs/prices and
kin annotations, power analysis (full-bank adjacent-frontier MDD 2.2–3.5 vs
observed gaps 0.9–2.4 → the blob is under-powering; fix = per-item information
via ≥40 accepted new frontier items reported as a separate frontier-core index),
exact commands, carried-forward gotchas.

## 6. Acceptance checklist (boot prompt)

- [x] Item triage table + discrimination anatomy + panel health ($0, logs only)
- [x] Both Fable re-reads written up (G partition; anchor recall boundary)
- [x] Kin-delta measured on both kin SUTs under default vs kin-free panels
      (+ non-kin control); unlock RULING recorded
- [x] v2.2 design memo FROZEN incl. bank-versioning rule + authoring pipeline
- [x] Cheap fixes implemented (patch layer, 60/60 tests, edit log) + validation
      micro-run judged against pre-stated metrics (A FAIL / B+C PASS)
- [x] Session-6 runbook (roster/power/cost/go-no-go)
- [x] Spend ≤$10 (upper bound $7.68); new dated reports; memory updated; pushed

## 7. New reusable patterns (session 5)

1. **DiD-with-control for panel-bias audits** — never compare two grader panels
   on the target SUT alone; the level shift masquerades as bias.
2. **Sub-threshold outlier leakage** — a taxonomy built on a hard spread cutoff
   (≥30) misclassifies the same phenomenon at 20–29 as "diffuse disagreement";
   re-adjudication must look one notch below every threshold.
3. **Pre-stated split verdicts** — pairing a hardening lever and a repair lever
   with separate metrics in isolated configs let one fail and one pass cleanly
   in a single $1 run.
4. **Excellence-gate asymmetry as diagnosis** — if a demanding-examiner band
   creates sub-frontier spread but none at the frontier, the ceiling is
   capability-parity, not scale compression; authoring, not rubric tightening,
   is the fix.
