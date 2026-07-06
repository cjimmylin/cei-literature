# 2026-07-05 — FruitBench Design Session Handoff

**Session:** Fable main loop (Fable-week). **Task:** brainstorm and scaffold 10 podium-level benchmark paper designs from the fruit of the Spirit (Gal 5:22–23), dual-track (secular conference paper + confessional BIBLEBENCH pack), for future Opus flesh-out.

## What was done

1. **Corpus digestion** (3 Sonnet Explore agents, parallel): the 7 FRUITBENCH source docs (~290KB); the COOKBOOK pipeline/conventions/existing portfolio (6 designs + 8 sketches in `20-DESIGNS/`); the vault's values-benchmarking literature (NormEval, RELIGIOUS-VALUES, ~40 key benchmark papers).
2. **Created `DESIGNS/`** with 11 Fable-authored documents:
   - `00-fruitbench-portfolio.md` — master doc: 9+1 architecture, dual-anchor ground-truth strategy (theologian + secular panels; divergence = contested band, distributional scoring), Seven-Laws instantiation, differentiation table vs. 20-DESIGNS/sketches, build order, Opus flesh-out protocol, risk register.
   - `01`–`10` — full design briefs (~2.5k words each), each with Track A (secular paper: construct axes with falsification conditions, task design, scoring, validity, novelty, risks), Track B (confessional pack: exegetical anchor, dimensions table, scenario families, 0–4 rubric, sketched seed case, evaluator notes), shared spine, and Opus flesh-out instructions.

## The ten designs

| # | Codename | Fruit | Innovation | Headline metric |
|---|---|---|---|---|
| 01 | COSTLY | love | demand curves for values under incentive pressure | moral price elasticity |
| 02 | EVENKEEL | joy | mood-induction as benchmark manipulation; two-sided (despair/toxic positivity) | valence flip-rate; drift slope |
| 03 | SIMMER | peace | counterfactual rollout delta on simulated social systems | de-escalation delta; appeasement-trap pass |
| 04 | LONGFUSE | patience | survival analysis of composure; provocation ladder | composure half-life; hazard ratios |
| 05 | USEFUL | kindness | comprehension-filtered outcome scoring for vulnerable simulated users | realized-benefit rate; warm-ineffective cell |
| 06 | BACKBONE-D′ | goodness | SDT over correction near-twins | d′ and criterion c |
| 07 | LEDGER | faithfulness | machine-checkable commitment ledger; kept/renegotiated/silent/covered | commitment half-life |
| 08 | SOFTPOWER | gentleness | Pettit non-domination; P0→P2 power gradient | option-set contraction; benevolent-override rate |
| 09 | MARSHMALLOW | self-control | temptation dose-response; detection-probability as factor axis | principledness coefficient |
| 10 | ONEFRUIT | singular καρπός | network psychometrics of AI character; conflict trilemmas; stress-spillover matrix | coherence index; weakest-link |

Recommended build order (portfolio §6): 09 → 06 → 07 → 04 → 01 → 05 → 02 → 08 → 03 → 10.

## Addendum (same session, later): test-case authoring guides

Added `DESIGNS/AUTHORING/` — 11 Fable-authored documents giving Opus extensive instructions for writing the actual benchmark test cases:

- `00-authoring-conventions.md` — shared rules: operating mode (EXECUTE, batch-and-gate), file layout under `FRUITBENCH/ITEMS/`, universal YAML item schema, twin/variant discipline (single operative delta, no lexical flags), the 4-beat escalation arc, contamination hygiene, 10-point per-item checklist, bank-level audits (quota, anti-shortcut probe, difficulty smoke test), dual-panel gold-labeling procedure (incl. provisional-model gold rules), Track B surface rules.
- `01`–`10` per-design guides, each with: evaluation-unit definition + schema extensions, bank composition/quota tables (P1 and full-bank sizes), step-by-step authoring recipes, a fully worked example item plus an annotated flawed item to avoid, difficulty-engineering levers, gold-labeling specifics, design-specific pitfalls, and a deliverables checklist.

Verified: all 10 guides contain all 8 required sections (grep-checked).

## What remains (Opus sessions)

- Per-design P1 pilots as specced in each brief's final section (item banks, harnesses, validation studies). Every brief lists its KB docs, verbatim digest numbers, and "do not change" list.
- Novelty re-check against post-2026-07 literature at flesh-out time (each brief §A8).
- Optional: promote Track B packs into full BIBLEBENCH sibling format (they are scaffolded to the CORINTHLOVE/SERMONMOUNT template).

## Verification performed

- All 11 files present; every brief contains Track A, Track B, and Opus flesh-out sections (grep-checked).
- Evidence numbers spot-checked verbatim against `30-EVIDENCE/20260705-digests/`: MORALSIM 7.9%–76.3%; κ 0.69→0.86; NurValues 32.29; r=−0.83; alignment-faking 12%→78%; sycophancy −66.8% — all match.
- No existing FRUITBENCH source docs modified; DESIGNS/ is new.

## Known issues / notes

- Digest-derived numbers were relayed via Explore-agent reports; per COOKBOOK rules Opus must re-cite from the digests directly when drafting papers (paths in portfolio doc and briefs).
- ONEFRUIT has a *soft* dependency on the other nine (standalone reduced forms specced; minimum 5 axes).
- Nothing committed to git this session.
