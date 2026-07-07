# WCF-Bench — Session Handoff

**Date:** 2026-07-06 · **Session:** Fable design session (one-day Fable window)
**Project:** WCF-Benchmark — 10 method-major benchmark designs for Westminster-Standards values alignment
**Location:** `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`

## What was done (all in this session)

1. **Sources digested** (Sonnet Explore agents): the Westminster Standards texts in `../WCF/` (ethical map: WLC Q91–152 casuistry, Q99 rules, Q151 aggravations, WCF 15/16/19/20/22) + the full COOKBOOK/00-KNOWLEDGEBASE design doctrine. Per Jimmy's directive: **Westminster texts only** — the Christian-Ethics-Books folder was explicitly excluded.
2. **Foundation docs (Fable):** `00-OVERVIEW/` — master spec (the 10 designs + suite architecture), shared spine (construct, tracks, tiers, scoring, perturbations P1–P6, contamination + canary, gates G1–G7, item schema), Westminster anchor registry (citation format + full domain map).
3. **10 design specs (Fable), each with 4–5 worked exemplars** (49 total): `01-DESIGNS/01-dutybound.md … 10-narrowgate.md` — DUTYBOUND (omissions), COMPLICIT (participation gradients), AGGRAVATE (Q151 severity calculus), STEADFAST (pressure ladders), CROSSWIND (say-do triples), LIBERTY (conscience triage), PROOFTEXT (grounding + twist refutation), MENDING (repair arcs), WHOLEHEART (matter/manner/end), NARROWGATE (obedience-cost dials). Method-major: every design covers the full Decalogue; methodology is the only differentiator.
4. **Opus authoring guide:** `03-OPUS-GUIDE/20260706-item-authoring-guide.md` — binding protocol for writing more items (non-negotiables, checklist, worked bad→repaired contrast, difficulty moves, escalation rules).
5. **Opus expansion (delegated, 4 agents):** `01-DESIGNS/expansions/` — 50 new items (5/design), filling coverage to 10/10 primary commandments for 8 designs, 9/10 for CROSSWIND (C7 queued) and MENDING (C1 queued). The guide was validated by this dry run (zero Fable rewrites needed).
6. **PRD + build plan (delegated, Opus):** `00-OVERVIEW/20260706-prd.md`, `20260706-build-plan.md` (4-phase roadmap, mock-first — the vault has no API keys or live runner).
7. **HTML deck (delegated, Sonnet):** `02-DECK/20260706-wcf-benchmark-deck.html` — 17 slides, self-contained, arrow-key nav, dark theme. Structurally verified; **browser visual check still pending**.
8. **Fable review memo:** `20260706-fable-review-memo.md` — flag adjudications R1–R7 (BINDING), honest coverage accounting (3/10 expansion files deep-read; 7 provisionally accepted on structural verification + self-audit protocol), post-window Fable queue.

## State: 99 items banked · all judgment-heavy design work front-loaded · no Fable dependency remains for build-out

## Next session (Opus) — start here, in order

1. Read: master spec → shared spine → registry → review memo (adjudications R1–R7 are binding) → authoring guide.
2. Apply the two errata from the review memo §3: registry source-file note (LC layout file begins ~Q114); NARROW-C5-008 Q130 secondary-anchor errata note (append, don't edit shipped blocks).
3. Deck visual check: `python3 -m http.server 8765` from `02-DECK/` + Playwright; fix rendering nits.
4. Item build-out per `20260706-build-plan.md` Phase 1: fill CROSS-C7 and MEND-C1 gaps first, then expand toward 60–120 items/design **starting with the mechanical-scoring designs (03 AGGRAVATE → 10 NARROWGATE → 07 PROOFTEXT)**; treat the 7 not-deep-read expansion files' self-audit lines as the standing review queue; park `[NEEDS-RULING]` items rather than guessing keys.
5. Phase 2 (still credential-free): mock-first harness skeleton per build plan (YAML loader, NARROWGATE state machines, mechanical scorers, judge templates).

## Blocked on Jimmy

- **API keys** (no live runner exists in the vault) — gates Phase 3 pilots. If keys arrive before the Fable window closes (~2026-07-11), best Fable use = adjudicating the first pilot's judge-disagreement clusters.
- **G6 confessional rater panel** — the construct-validity linchpin; recruitment decision is Jimmy's.
- Final rulings R1/R3/R4 once panel data exists.

## Known issues / honest caveats

- All empirical claims about difficulty are pre-registered predictions, not measurements — nothing has run against a live model.
- 7 of 10 expansion files accepted provisionally (structural verification + self-audit protocol, not item-level Fable read) — see review memo §1.
- The suite's theology is single-author (Fable) + single-reviewer (Fable) until the G6 panel exists; `[DISPUTED]`/anti-trap keys in LIBERTY are the highest-exposure surface.
- Scope isolation honored: no sibling-bench material consulted (BIBLEBENCH memory rule); knowledgebase only from 00-KNOWLEDGEBASE.
