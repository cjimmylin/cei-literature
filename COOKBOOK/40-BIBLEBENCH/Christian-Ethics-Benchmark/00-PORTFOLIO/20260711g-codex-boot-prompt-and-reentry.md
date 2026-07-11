<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY — Codex Boot Prompt & Continuation Protocol (any future agent)

**Issued:** 2026-07-11, Fable transition-prep session (thread closed in Claude Code;
work handed to Codex). This file is the single entry point for WHOEVER continues —
Codex, a future Claude/Anthropic model, or Jimmy. It duplicates the boot prompt from
`20260711e-fable-codex-transition-package.md` so it can be pasted without opening the
package first.

---

## 1. Paste-ready Codex boot prompt

```
You are Codex executing WALKWORTHY session O5 (mechanical; zero judgment). Work ONLY in
CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/. Read, in order:
AGENTS.md; 00-PORTFOLIO/20260711e-fable-codex-transition-package.md (your execution
plan); 20260711d-fable-o5-decision-framework.md (pre-made decisions FR-1..FR-15, branch
tables, release formula, STOP-AND-ASK triggers); 20260711c-fable-o4-validity-review.md;
20260710-fable-gate-prereg-pilot-adjudication.md (§B/§C/§E — FROZEN, never edit);
20260710-human-label-protocol.md; 20260710-fable-PR3-ruling.md; PENDING-RULINGS.md.
Then execute the package phases in order: Phase 0 pre-flight; Phase 1 (W1 tie-breaker →
W2 Δ(J) → W3 recompute → W4 G5 → W5 G7 — all label-free); Phase 2 G4 per label wave IF
filled label CSVs exist (if none, stop after Phase 1 and report O5-blocked-on-labels);
Phase 3 verdict assembly strictly via the framework §4 formula. Obey every guardrail in
the package verbatim (no deletes; report immutability; HOLDOUT never loaded; explicit
judge models; explicit git pathspecs; TDD). Anything not covered by the framework →
append to PENDING-RULINGS and stop that thread; never guess. End with a NEW dated
handoff + commit + fast-forward push of WALKWORTHY paths only.
```

Multi-session note for Codex: the phases are checkpointed by their artifacts. If a prior
Codex session already produced a Phase-1 output (a `runs/*-o5-tiebreak/` dir, a
`home_advantage` module + report, a post-adjudication readings file, G5/G7 reports),
do NOT redo it — verify it, then continue from the next undone step. Always start by
listing `00-PORTFOLIO/2026*` and reading the LATEST dated handoff.

## 2. Re-entry protocol for a future Claude / Anthropic model

Codex may have progressed since this thread closed. Before doing ANYTHING:

1. `git log --oneline -15 -- COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/` and
   list `00-PORTFOLIO/2026*` — read the newest handoff(s) FIRST. This 2026-07-11 state
   is a floor, not the present.
2. Your role is NOT to redo or re-litigate O5 execution — it is to (a) adjudicate
   anything Codex appended to `PENDING-RULINGS.md` or flagged STOP-AND-ASK, and
   (b) adversarially review the O5 gate-adjudication report once it exists (the
   master-plan §1/O5 Fable-preferred items: neutrality-gate failures, kill disputes,
   stratum fights, prevalence-paradox cases).
3. The frozen stack still binds you: §B/§C/§E (gate memo) + FR-1…FR-15 (framework §2).
   Changing any of them requires a logged Jimmy ruling — including for a Fable-tier
   model. If labels have landed and verdicts exist, verify they trace to the framework
   tables before endorsing them.
4. All standing safety rules apply and are MANUAL for non-Claude-Code agents (AGENTS.md
   §Safety): never delete, report immutability, HOLDOUT never loaded, shared git index
   (explicit pathspecs, `git log -1` first, fast-forward only), FIX-MECHANICS-ONLY.

## 3. State snapshot at handoff (2026-07-11, commit `8eb371db3`)

- Panel COMPLETE: `runs/20260711-o4-panel/` 2064/2064, report `20260711b-o4-panel-report.md`
  (descriptive only). Harness 261 pytest green.
- Judgment layer FROZEN: validity review `…c`, decision framework `…d` (FR-1…FR-15),
  transition package `…e`, session handoff `…f`, PENDING-RULINGS PR-1…PR-8.
- NOT yet done (Codex Phase 1, label-free): tie-breaker adjudication of the 609
  `pending_adjudication` cells; §E Δ(J) judge home-advantage test; post-adjudication
  recompute; G5 driver; G7 batteries. Phase 2+ needs Jimmy's labels.
- Jimmy owes: Part-A labels (wave 1 = 02/07/01) + 2nd labeler or declared test–retest;
  ratification one-liners (framework §7); W4 06-reference fix ratification; release
  sign-off (always Jimmy-only).

## 4. Escalation path

Anything judgment-shaped → append a new PR-N to `00-PORTFOLIO/PENDING-RULINGS.md`
(current PROVISIONAL behavior stated, options laid out, NO guessed disposition) and stop
that thread. Jimmy rules; a future Fable window may rule delegated items per master-plan
§1/O5, logging the ruling and flagging it for ratification.
