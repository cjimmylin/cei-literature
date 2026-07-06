# 2026-07-05 — FruitBench-v2 Design Session Handoff

**Session:** Fable main loop (Fable-week). **Task:** scaffold FRUITBENCH-v2 — ten NEW benchmark designs, each a **unique whole-passage methodology assessing all nine fruit** of Galatians 5:22–23 (architectural inversion of v1: v1 = fruit-major, one method per fruit; v2 = method-major, one method across all fruit). Fable-authored at full depth for future Opus flesh-out. Scope strictly FRUITBENCH (v1 folder + published lit); sibling benches untouched per scope-isolation rule.

## What was done

Created `FRUITBENCH-v2/` (nothing in `FRUITBENCH/` v1 modified) with 14 files:

1. **`00-registry.md`** — FROZEN construct registry: F1–F9 (nine fruit: construct definition, v1 owner design, POS indicators, counterfeits), W1–W15 + W-open (works of the flesh as closed negative-space taxonomy, AI-behavioral translations, social-factional weighting note), P0–P10 (passage-level claims: analogical-use constraint, singular καρπός, no-law, flesh–Spirit antagonism, keep-in-step, anti-conceit, growth-vs-works, freedom-for-service, restore-gently, representative-lists, community-legibility). Citation rules. Registry is the triangulation backbone — all briefs cite codes, never re-derive.
2. **`00-fruitbench-v2-portfolio.md`** — master doc: the measurement-lattice argument (v1×v2 = 9-fruit × ~20-instrument grid; convergence/divergence across instrument families as program-level science), the ten-design table, orthogonality map vs all ten v1 designs (collision audit), shared commitments (v1 §3 inherited + per-fruit-reporting mandate, registry discipline, coverage-table rule, CFT-below-honest-absence, calibration hooks), build order with dependency edges, Opus protocol, risk register.
3. **`DESIGNS/01–10`** — ten full dual-track briefs (~2.2–2.9k words each; v1 house skeleton: Pitch / Track A §A1–A9 with 9-fruit coverage table + falsification conditions / Track B §B1–B6 with exegetical anchor, families, 0–4 rubric, seed case / shared spine / Opus flesh-out instructions with P1 pilot spec + do-not-change ledger):

| # | Codename | Methodology | Headline |
|---|---|---|---|
| 01 | TRELLIS | MTMM matrix (9 fruit × ≥4 elicitation methods, Campbell–Fiske trait/method decomposition) | trait-variance share |
| 02 | THORNS | antagonist dyads over the 9×15 F×W grid, calibrated-attraction items | per-cell pass heatmap; vice-pull ranking |
| 03 | STRIDE | step-level process tracing, F/W codebook, sequence statistics | unprompted lapse-recovery rate |
| 04 | UNFENCED | supererogation: all rules satisfied, measure discretionary remainder, V0–V3 rule-ablation identification | discretionary-virtue rate; rule-shadow ratio |
| 05 | CULTIVAR | habituation intervention: dose–response, 9×9 transfer matrix, washout; growth-vs-performance signatures | cultivation elasticity; transfer |
| 06 | MIRROR | moral self-knowledge calibration (prospective/concurrent/retrospective vs measured behavior; own/other control) | per-fruit ECE; signed conceit index |
| 07 | TASTE | perceiver-side psychometrics: blinded community raters vs behavioral gold | legibility gap; charisma gap |
| 08 | ROOTSTOCK | provenance factorial: C1 passage / C2 certified secular paraphrase / C3 generic / C4 none / C5 weaponized | dispositional share; weaponization resistance |
| 09 | GLEANINGS | naturalistic epidemiology of real deployment transcripts, opportunity-conditioned rates, case-control | wild base rates; lab–field gap |
| 10 | VINEDRESSER | judge-side psychometrics: per-fruit judge validity, counterfeit d′, judge–actor gap | judge certification tables |

4. **`OPUS-BUILD-GUIDE.md`** — v2 deltas over v1 authoring conventions: file layout (ITEMS/HARNESS/PILOTS/PANELS/SUBSTRATE), item-schema extensions (F/W/P tags, kernel_id, reuse_tags, arms), nine-fruit quota table (8% floor, ≥50% social-factional W-weighting, CFT coverage, P9 quota), P1 deliverables/gates table for all ten, evidence-citation rules, global do-not-change ledger.

**Build order:** 02 THORNS → 04 UNFENCED → 10 VINEDRESSER → 06 MIRROR → 01 TRELLIS → 08 ROOTSTOCK → 03 STRIDE → 07 TASTE → 09 GLEANINGS → 05 CULTIVAR. (VINEDRESSER third because its judge certifications are consumed by all subsequent scoring stacks; GLEANINGS is paperwork-first — governance memo gates coding; CULTIVAR last, heaviest infrastructure.)

## Verification performed

- File census: 13 content files present (2 root docs + 10 briefs + build guide) + this handoff = 14.
- grep section checks: every brief contains "Track A", "Track B", "Opus flesh-out", "9-fruit coverage", "Falsification condition" — all pass.
- Registry citations: every brief cites ≥12 unique F/W/P codes (range 12–28).
- Stray-character sweep (CJK): clean (three strays introduced during drafting were caught and fixed).
- `git status`: only the new untracked `FRUITBENCH-v2/` folder; no v1 files modified.
- Orthogonality audit (Fable, inline): v2 table checked against v1 §2 — the three highest-risk collisions each have explicit differentiation in §A8 and portfolio §3 (TRELLIS vs ONEFRUIT: method-variance vs trait-structure; THORNS vs MARSHMALLOW: full grid at fixed dose vs one column parametric; TASTE vs SIMMER: perception/legibility across nine vs causal rollout delta for peace only).

## What remains (Opus sessions)

- Per-design P1 pilots per each brief's final section and the build-guide gates table. EXECUTE mode: files, not plans.
- Per-design deep authoring guides (v1's `AUTHORING/01–10` analogue) — deliberately deferred; the briefs' flesh-out sections + build guide §3–4 carry enough for P1. Write them per-design at bank-authoring time if needed.
- Novelty re-check vs post-2026-07 literature at flesh-out (§A8 each brief).
- Track B translation choice (ESV-style used in briefs) — confirm with user before first confessional pack ships (build guide §9).
- Fable adversarial gate after Opus builds (as done for other portfolios).
- Nothing committed to git this session (deliberate; commit decision with user).

## Addendum (same session, later): Fable adversarial gate — ALL VERSIONS

Fable gate performed over **both portfolios** (all 20 briefs read in full): memo at `../FRUITBENCH-REVIEWS/20260705-GATE-ADJUDICATION.md`. Result: **20/20 pass, no design killed; 5 MANDATORY brief amendments** (Opus incorporates as first action of the affected build session):

- **D-12 SOFTPOWER (v1):** P0→P2 gradient conflates opportunity with disposition — common disposition scale (or opportunity-conditioned rates) across power conditions.
- **D-18 TRELLIS (v2):** unit-of-analysis section required (within-model across-kernels primary; engineered kernel elicitation-strength variance).
- **D-21 THORNS (v2):** calibration-band transfer check on held-out frontier-class models (items gated, norming principle preserved).
- **D-25 UNFENCED (v2):** V3 arm re-specified — notice+surface+comply is the fitting act; acting unrequested under V3 = scope violation (resolves contradiction with SOFTPOWER/LEDGER/MARSHMALLOW).
- **D-31 ROOTSTOCK (v2):** familiarity/memorization control for the C1−C2 form effect (C1′ low-frequency rendering + perplexity covariate) + D-32 C5′ secular-weaponization arm.

Plus 29 non-blocking D-orders, 8 cross-cutting findings (FO-1 unit-of-analysis, FO-2 lattice-independence ledger, FO-3 panel-capacity bottleneck, FO-4 capability-gate reinterpretation, FO-5 shared human-substitution protocol, FO-6 contested-band cap, FO-7 structure-claims map, FO-8 self-review limitation + second-pass gate after 3 P1s), and 10 cross-version boundary adjudications (X-1…X-10). Build orders unchanged.

## Known issues / notes

- Evidence numbers in briefs were carried from v1 documents (which were verified against `30-EVIDENCE/20260705-digests/` in the v1 session); Opus must re-cite verbatim from the digests directly (build guide §7).
- Registry is FROZEN: construct edits require Fable review; novel-vice discoveries (GLEANINGS) go to a review log, never silent registry edits.
- Cross-design dependencies are all soft (standalone reduced forms specced), but SUBSTRATE/ sharing (VINEDRESSER/TASTE/MIRROR) and THORNS reuse-tagging are the economics to respect.
- ROOTSTOCK C5 (weaponized-scripture arm) needs theologian-panel authorship of the attack library early — flagged as its main ethical-sensitivity item.
