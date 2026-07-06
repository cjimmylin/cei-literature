# 20260706h — Fable Discretionary-Spend Session Handoff (#1 item-bank read, #2 stress test, #3 pre-registrations)

**Session model:** Fable 5. Executed the three approved discretionary items before window
close, in parallel (Fable main loop on #1/#2; Sonnet gathering agent for #3 inputs).

## Deliverables (all new dated files, this session)

1. **#1 — `20-DESIGNS/REVIEWS/20260706-p0-item-bank-adversarial-read.md`** — full Fable
   read of all 65 items + wrappers (supersedes the F2 ~15-item sample as item-level
   record). **Verdict: APPROVED FOR P0 SPEND, zero KILL, no item rewrites.** Binding
   rulings IB-1…IB-5: affect-emotion×cell aliasing (disclose; no affect-by-cell inference
   at P0; randomize at P1); Greene-subset pole alignment (M030 pole-collapsed, M004
   consent-weakened → M030 sensitivity row in G3 fallback); stance-polarity×content
   aliasing (cross-domain PS-stability caveat + within-polarity sensitivity; balance at
   P1); PS-dir gloss fix; control-shift commensurability metric to be defined pre-run.
2. **#2 — `COOKBOOK/20260706-protocol-stress-test.md`** — 16 simulated outcomes run
   against the full protocol stack; 13 resolved cleanly. Binding amendments PS-1…PS-6.
   **Most serious catch: G3-a (per-item ≥4/5 sign consistency, both frames) vs
   `analysis/gates.py` (pooled |delta|≥0.02) compute DIFFERENT fallback verdicts — PS-2
   makes the per-item implementation a P0 precondition alongside R-1.** PS-3 fixes a
   precedence ambiguity in the exit-sequencing memo (§3 label-conversion governs the
   meaning of all "wait for Fable" labels vault-wide; per-track docs win on substance
   only; "Jimmy decides" includes deciding to wait).
3. **#3a — `20-DESIGNS/DUPLEX-P0/20260706-g3-mininorm-preregistration.md`** — the G3
   human mini-norm, fully pre-registered (within-subject speeded+load vs deliberation on
   the 5 Greene base prompts; N=150→≥120; anchor rule: signed pooled Δ enters
   `g3_human_anchor` iff CI excludes 0, else fallback mode; M030-excluded sensitivity
   governs on sign disagreement). Jimmy runs recruitment; Opus builds materials/scripts.
4. **#3b — `20-DESIGNS/20260706-06-crux-p1-validation-survey-prereg.md`** — the CRUX §7
   P1 gate operationalized (~400 instances × 3 raters; instance pass = 2/3 coherent AND
   2/3 conflictual; gate ≥80%; per-cell <50% → re-template; Q2 α≥0.4 instrument floor;
   Q3 targeting thresholds gate P2 spend, not P1). Runs after the D-3 prose-enrichment
   pass; cost ≈ $1.5–2.5k.

## New Opus-executable work created by this session (add to post-window queue)

- **PS-2 implementation** (P0 precondition): per-item × per-frame G3 fallback table in
  `DUPLEX-P0/analysis/`, with tests; pooled fallback demoted to descriptive.
- IB-1(a)/IB-3(a) analysis restrictions + IB-5 control-shift metric: config/analysis
  wiring before P0 scoring (all listed in the item-read Disposition section).
- Survey materials + analysis scripts for both pre-registrations (verbatim builds).

## For Jimmy

- The two pre-registrations are ready to launch on your greenlight (mini-norm: recruit
  N=150; CRUX survey: after prose enrichment). Both name you as launcher.
- Remaining in-window Fable value is now ONLY live-result adjudication if credentials
  land (exit memo §2.4). The pre-registered surface has no other open Fable dependency.

## Cautions

Parallel-session git discipline held (path-scoped commit, `git log -1` checked). The
CORINTHLOVE c–f uncommitted set is still untouched and still awaiting your commit call.
