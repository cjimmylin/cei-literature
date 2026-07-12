# CORINTHLOVE Status

Last updated: 2026-07-11 (America/Los_Angeles)

## Active workstream

`Consolidated core Tier-0 implementation — planned, not started`

Goal: implement the approved offline-only modular suite core and read-only
adapters for DIMGLASS, CHARITROC, and CROSSROADS without altering source banks
or starting a live run.

OpenRouter authorization: cheap models only. Do not run GPT-5.4 full, GPT-5.5,
GPT-5.6 Sol, Opus, or another flagship/frontier model unless the user changes
that instruction.

## Last completed checkpoint

`07-charitroc` is **GO for cheap-model qualification scale-readiness**.

- bank: 684 episodes = 576 private + 96 calibration + 12 public;
- matched pairs: 288/288 pass defeat-class matching;
- full suite: 1009/1009;
- static adversarial, generator dry-run, export, and self-check: PASS;
- public AUCs: 0.4444, 0.6389, 0.6528, 0.7361 (range 0.2917);
- all four models mechanically resolved 12/12 public episodes;
- combined reconstructed provider usage: approximately `$0.1714778`;
- exact-key matches in the bank: 0;
- review: `CORINTHLOVE-REVIEWS/20260711-charitroc-bank-review.md` (GO);
- handoff: `COOKBOOK/20260711a-corinthlove-charitroc-build-handoff.md`.

Verified roots:

- `CORINTHLOVE/BANKS/07-charitroc/pilot/runs/20260711-openrouter-cheap-azure-v1-live-v2`
- `CORINTHLOVE/BANKS/07-charitroc/pilot/runs/20260711-gpt54-mini-azure-v1-live-v1`

Rubric B5 frontier filtering remains a standing pre-calibration condition. It
does not invalidate the completed cheap qualification or block consolidated
design work. CHARITROC changes, live artifacts, review, handoff, and memory
update are uncommitted.

`01-crossroads` is **GO for offline construct and future cheap public
qualification**, but its reviewed v6 root was not created after the strategy
switch.

- bank: 600 private + 30 public enacted episodes;
- retained hardness evidence: 40 rejected candidates;
- protocol-only stated pairs: 60;
- pilot suite: 76/76; full suite: 233/233;
- synthetic recovery: correlation 0.979832, RMSE 0.124106;
- construct review: `20260711-crossroads-bank-rereview.md` (GO);
- live-protocol review: `20260711-crossroads-live-completion-evidence-addendum.md`,
  Final disposition revision 2 (GO);
- immutable v5 state: four successful access artifacts, one failed nano
  canary, no canary-complete event;
- v6 live state: absent by design.

## Current blocker

`none` for the offline Tier-0 slice. The prior bank-specific technical blockers
are closed:

- CHARITROC is review-GO and cheap-live-qualified without saturation;
- CROSSROADS is construct-GO and live-protocol-GO at 76/76 pilot and 233/233
  full tests;
- the controlling CROSSROADS completion-evidence review is Final disposition
  revision 2, GO;
- the independent exception-boundary audit is PASS.

The consolidated design and offline Tier-0 implementation plan are approved.
The strategy changed before a fresh CROSSROADS v6 root was created, and the old
one-bank queue remains retired. No paid call or new method-bank build is part of
Tier 0. Human norming, expert key
validation, frontier filtering, canonical live judges/E, private execution,
calibration, ranking, and freeze remain separate, unauthorized gates.

## Next action

Execute the approved offline Tier-0 plan in
`COOKBOOK/20260711e-corinthlove-consolidated-core-implementation-plan.md`,
starting at Task 1 and preserving its TDD, read-only source, no-live, and
no-commit gates. Design authority is
`COOKBOOK/20260711d-corinthlove-consolidated-benchmark-design.md`. Do not create
a CROSSROADS v6 root or resume AGAPEGAME/WITNESS/MANYMIRRORS as independent
queue items.

Never retry, modify, or reuse the preserved protocol roots:

- `pilot/runs/20260711-openrouter-cheap-azure-v1-live-v1`
- `pilot/runs/20260711-openrouter-cheap-azure-v2-live-v1`
- `pilot/runs/20260711-openrouter-cheap-azure-v3-live-v1`
- `pilot/runs/20260711-openrouter-cheap-azure-v4-live-v1`
- `pilot/runs/20260711-openrouter-cheap-azure-v5-live-v1`

Prior catalog-protocol addendum:
`CORINTHLOVE-REVIEWS/20260711-crossroads-live-protocol-addendum.md` (GO).

Direct-attestation addendum:
`CORINTHLOVE-REVIEWS/20260711-crossroads-live-direct-attestation-addendum.md`
(GO).

Parameter-compatibility addendum:
`CORINTHLOVE-REVIEWS/20260711-crossroads-live-parameter-compatibility-addendum.md`
(GO).

Tool-schema compatibility addendum:
`CORINTHLOVE-REVIEWS/20260711-crossroads-live-tool-schema-compatibility-addendum.md`
(GO; C6 PASS).

Completion-evidence addendum:
`CORINTHLOVE-REVIEWS/20260711-crossroads-live-completion-evidence-addendum.md`
(Final disposition revision 2: GO).

## Archived CROSSROADS binding additions

- use the v3 guide, including its §7 interim hardness gate;
- preserve frozen C1–C16 clause tags verbatim;
- use `10CB3-` canaries;
- honor design order D-18 and propagation orders P-1…P-3;
- keep generator/sidecar/judge/export/live evidence disciplines from
  CHARITROC without copying its design-specific metrics;
- its offline and review gates pass, but the consolidation strategy now pauses
  the otherwise authorized fresh v6 access/canary/public-smoke sequence.
