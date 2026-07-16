# DECISION MEMO — design-02 branch-classifier pin for v-next (owner-ruled 2026-07-16)

**Status: DECISION ONLY — no implementation, no re-runs this session** (per
`20260716-boot-prompt-s7-decisions-f7.md` Task 0.3 fence). Ruling recorded in
`20260716-owner-rulings-s7-decision-grid.md` §3.

## Evidence (from F3, `20260716-f3-crossfamily-classifier-results.md`)

- Pilot pin: `openrouter/openai/gpt-4.1-nano` (inherited from the tasks'
  `judge_model` default).
- Cross-family replay of the 1,435 stored classification turns:
  **mistral-small-3.2 vs gemini-2.5-flash-lite agree 0.902** with each other, but
  only 0.721 / 0.685 with the pilot nano route. On **24.4% of turns both alt
  families agree AGAINST nano**. Epicenter: design-02 `refused→complied` swaps —
  nano over-calls "refused" on turns both alternatives read as substantive
  engagement (mistral 256/401, gemini 319/452 of divergent turns).
- Design-07 cross-family agreement is moderate-good (0.77–0.97): the 07 instability
  seen in the offline heuristic replay was the heuristic's, not the models'.

## Ruling

**Switch family for v-next design-02 runs.** The v-next 02 instrument pins a
cross-family-corroborated classifier drawn from the two agreeing families
(mistral-small-3.2 or gemini-2.5-flash-lite), NOT gpt-4.1-nano and NOT any
same-family sibling of nano.

## What the v-next instrument spec must declare (C6, before any run)

1. Exact model slug + provider (candidate default: `mistralai/mistral-small-3.2`
   route used in F3 — final slug choice is part of the v-next spec, weighing cost
   and availability; gemini-2.5-flash-lite is the sanctioned alternate).
2. Prompt template hash (`classifier_rubric`) + route policy
   (`solvers.py::_classify_branch`) — unchanged unless the v-next spec says
   otherwise.
3. Its own spend gate (PF-003) — any new 02 run is v-next work.

## Consequences

- **New instrument version under C6** (`20260716-prereg-comparisons-RATIFIED.md`):
  v-next 02 cells are NOT comparable with nano-pinned pilot 02 cells; no
  cross-classifier pooling ever.
- The existing pilot 02 data remains valid AS the nano-pinned instrument, with
  nano's refused-overcall documented as an instrument property (this memo + F3
  reports are the citation).
- The F11 RULING 1d (freeze-nano on judge-A replacement) governs the CURRENT
  lineage only; it is not contradicted by this v-next re-pin, which is a distinct
  instrument version.
- Design-07 needs no pin change on this evidence (cross-family stable); the v-next
  spec MAY carry nano forward for 07 or align with 02's new pin — to be declared in
  the v-next spec, not here.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
