# 00 — Design Rationale and Portfolio Map

> **CEI COOKBOOK · 20-DESIGNS.** Fable-authored (2026-07-05). This folder contains six full benchmark
> designs and eight concept sketches, each grounded in the evidence layer (677 cards → 13 dossiers →
> 13 knowledgebase docs) and the four completed CEI meta-evaluations (965 benchmark characterizations).
> Every design targets a **documented void** with a **documented discrimination mechanism**. Novelty
> and discrimination claims were re-scoped at the 2026-07-05 adversarial gate (see status section
> below): voids are stated relative to the 965 characterized benchmarks, with named nearest neighbors
> and [beyond-corpus] frontier work cited in each design's novelty statement.

---

## The selection logic

The evidence supports exactly one strategic conclusion (KB docs 01, 04, 06): **static, announced,
single-turn, content-level, English, majority-gold moral testing is saturated and largely invalid;
the unclaimed territory is behavioral, unannounced, interactive, process-level, plural, and
contamination-proof.** Six findings force the portfolio's shape:

1. Expressed ≠ revealed values — the best-replicated phenomenon in the corpus, and almost no
   infrastructure measures it (96% static; 3% interactive) → **Design 01**.
2. Only 10/54 normative benchmarks test reasoning; care/contractarian voids; consequentialist
   attractor → **Design 02**.
3. Moral-psych content instruments converge (43% zero cross-model variance; quality↔convergence
   r=−0.83); process manipulations discriminate; dual-process and moral identity have ZERO usable
   instruments despite >25k citations → **Design 03**.
4. Religious benchmarks test recall not reasoning (27.7%); 8/14 traditions uncovered; 93.75% treat
   traditions as monoliths; the one discriminative recipe is known → **Design 04**.
5. Cultural benchmarks: 0/218 measurement invariance; knowledge-about ≠ reasoning-within (92.5% gap);
   <7% substance×usability intersection; adaptation-in-situ untested → **Design 05**.
6. No instrument scores value-conflict adjudication with consensus-stratified ground truth, coherence
   auditing, and procedural generation together → **Design 06**.

## Portfolio at a glance

| # | Codename | Domain | Core construct | Primary void filled | Discrimination mechanism |
|---|---|---|---|---|---|
| 01 | **UNMARKED** | agentic (flagship) | unprompted moral behavior in realistic tasks | announced-test artifact; moral attention; expressed-revealed gap | incidental embedding + incentive conflict + fresh-per-run worlds |
| 02 | **FRAMESHIFT** | normative ethics | framework-conditioned reasoning & steerability | reasoning deficit; care/contractarian voids | procedural rubrics + framework-conditional gold + switching agility |
| 03 | **DUPLEX** | moral psychology | how judgments form (process signature + identity) | dual-process & moral-identity zero-coverage | resource manipulation — the only proven discriminator |
| 04 | **INTRA** | religious values | reasoning-within traditions, denominationally resolved | reasoning void; zero-coverage traditions; monolith problem | computable liturgical-language items (T2 recipe) |
| 05 | **CULTIVATE** | cultural/linguistic | in-situ cultural adaptation | static-QA paradigm; invariance void; divergent-value handling | emergent-context multiturn + divergent items |
| 06 | **CRUX** | cross-cutting | value-conflict adjudication under uncertainty | conflict handling; calibrated pluralism; coherence | factorial procedural generation + consensus stratification |

Sketches (SKETCHES/): S1 value drift over long horizons · S2 sycophancy vs legitimate updating ·
S3 multi-agent moral coordination · S4 care-ethics relational instrument · S5 contractarian bargaining
games · S6 moral attention "needle-in-haystack" · S7 population-distribution simulation fidelity ·
S8 honesty under goal pressure.

## Shared design commitments (inherited by every design; from KB doc 01)

All six designs comply with the Seven Laws and the pre-registration checklist. In particular, every
design ships: behavioral primary measures with a paired recognition baseline (Law 1); two-tier
difficulty with the drop as headline + capability-correlation gating stat (Laws 1, 3); harm/over-refusal
Pareto + four-way refusal taxonomy; consensus-stratified ground truth (gold above ~85% consensus,
distributional below); validated cross-family judges with per-item keypoint rubrics; the perturbation
battery with flip-rates; private rolling holdout + fresh-per-run generation + canaries; annotator-level
labels with psychometric value vectors; human baselines on the identical instrument; and explicit
"whose values" datasheets.

## Sequencing recommendation (for the post-Fable Opus sessions; revised at the 2026-07-05 gate)

1. **Start with Design 03 (DUPLEX) — via its new P0 falsification gate.** Smallest infrastructure and
   the fastest path to a decisive result either way. Honest framing (corrected at the gate): the
   r=−0.83 result shows *content* instruments converge — it motivates process probes but does not
   guarantee they discriminate; the direct discrimination evidence is a single instrument (MP-DP),
   a single unreplicated effect on the weakest subject (Haiku 3.5). DUPLEX's rewritten pilot
   therefore runs a cheap pre-registered P0 smoke test **before** any generator build.
2. **P0 pass → continue DUPLEX; P0 fail → Design 06 (CRUX) takes the build-first slot** (and DUPLEX
   is re-scoped as universal-signature measurement). CRUX second either way — its procedural
   generation core is reusable by all other designs.
3. **Then Design 01 (UNMARKED)** — the flagship; highest impact, highest harness cost; reuses CRUX's
   generator and DUPLEX's process instrumentation.
4. Designs 02/04/05 can proceed in parallel with community/expert partnerships as the long pole
   (04 and 05 require co-design pipelines that should start early).

## 2026-07-05 adversarial review gate — status

The deferred Phase-5 gate ran on 2026-07-05: 12 refute-first Opus reviews (novelty + validity per
design), adjudicated in `REVIEWS/20260705-adjudication-memo.md`. Outcomes: all six novelty reviews
PASS-WITH-FIXES; all six validity reviews BLOCK; adjudicated result **REVISE-AND-PROCEED for all six**
(no understudy promotions) plus the DUPLEX P0 restructure above. Six cross-cutting standards (X1–X6:
numeric go/no-go rules, shortcut audits, eval-awareness comparator arms, power corrections,
sub-project disclosures, novelty-statement hygiene) were applied to every design; each design file
ends with a revision log mapping defects to changes. Sketch S6 (moral attention) was partially
absorbed into Design 01 as its MA-identifiability mechanism; S6 remains listed as a (now narrower)
standalone sketch. Related: the `40-BIBLEBENCH/` packs were audited against the cookbook the same
day (`40-BIBLEBENCH/AUDITS/`), with a FRUITBENCH↔DUPLEX/INTRA overlap map reconciling the virtue
designs with this portfolio.

Each full design ends with a **pilot protocol** sized to be executable by Opus-tier sessions with
~9-model cross-vendor trials, and a **novelty statement** checked against the four feature matrices
(54 + 292 + 401 + 218 characterized benchmarks).
