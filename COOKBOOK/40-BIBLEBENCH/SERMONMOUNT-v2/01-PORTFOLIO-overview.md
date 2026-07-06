# 01 — SermonMountBench-v2: Ten Whole-Passage Methodologies

**Author:** Fable (main loop), 2026-07-05
**Status:** Design-complete briefs; **adversarial gate PASSED 2026-07-05** (all ten GO; gate revisions applied in-brief and marked "gate" — memo: `20260705-fable-adversarial-gate-v1-v2.md`); awaiting Opus flesh-out (item/episode banks, harness code, pilots)
**Companion registry:** `00-REGISTRY-sermon-principles.md` (S01–S40, FROZEN) — read it first; every brief cites it.
**Source corpus:** `../SERMONMOUNT/` research docs + `COOKBOOK/00-KNOWLEDGEBASE/` + published literature. The v1 portfolio (`../SERMONMOUNT/DESIGNS/`) is referenced **for differentiation only**. No other benchmark project in this vault is referenced, ever.

---

## 1. What v2 is, and how it differs from v1

**v1 sliced by content.** Each of the ten v1 designs instruments **one** Sermon unit deeply (Beatitudes → BLESSED, secret piety → UNSEEN, oaths → PLAINYES, hostility → SECONDMILE, mammon → TWOMASTERS, log/speck → LOGSPECK, Golden Rule → GOLDGAP, fruits → SHEEPSKIN, antitheses → TELOS, two builders → ROCKSAND).

**v2 slices by method.** Every v2 design covers the **entire Sermon** — all forty registry principles (S01–S40), Beatitudes included one by one — and the ten designs differ in **measurement paradigm**. Each design is a complete, standalone benchmark paper whose methodology is its identity.

**The triangulation thesis.** This is a multitrait–multimethod design at portfolio scale (Campbell & Fiske's classic logic). v1 contributes construct-specific instruments; v2 contributes method diversity over a common construct set. A model's standing on a principle (say S17, non-retaliation) is *trustworthy* only when it converges across paradigms: a model that keeps S17 in single-shot vignettes but sells it cheaply in LEDGER's pricing lattice, abandons it in PILGRIM's tenth episode, and never weights it in CROSSWINDS conflicts does not "have" the disposition — it has a format. **Per-principle cross-method convergence is itself the capstone deliverable** (the v2 aggregate report, buildable once ≥ 3 designs have pilot data): a 40-principle × 10-method score matrix in which method-variance vs trait-variance is the headline decomposition.

**Differentiation-vs-v1 rule (hard):** no v2 design may reduce to "a v1 design run over more pericopes." Each brief carries a *Differentiation* section naming (a) its nearest v1 design(s) and the boundary line, and (b) its nearest published neighbors. A claim dies if the neighbor's existing instrument could produce the v2 headline metric without modification.

## 2. The ten designs — one unique manipulated axis each

Method orthogonality is enforced by giving every design a **distinct manipulated/observed axis**. Nothing else in the portfolio manipulates that axis as its primary variable.

| # | Codename | Unique axis | Model's role | Unit of observation | Headline metric |
|---|----------|-------------|--------------|---------------------|-----------------|
| 01 | PILGRIM | **Time** — one longitudinal life-arc | Agent living a long multi-episode arc | The trajectory (40-principle episode chain) | Arc-consistency index; principle drift half-life |
| 02 | CROSSWINDS | **Principle-vs-principle conflict** | Decision-maker inside dilemmas where two S-IDs collide | The dyadic conflict cell | Revealed priority ordering; incoherence (intransitivity) rate |
| 03 | PLUMBLINE | **Evaluation role** — model as judge | Evaluator grading third-party conduct | The (dossier, verdict) pair | Per-principle blind-spot profile vs panel; evaluator log-speck asymmetry |
| 04 | CANTICLE | **Latent-trait calibration** | Respondent to a psychometrically calibrated bank | The calibrated item response | Subscale information curves; dimensionality of "Sermon conformity"; DIF rate |
| 05 | TESSERA | **Context transformation** | Same decision re-instantiated across surface worlds | The (item, transform) cell | Per-principle invariance coefficient (worst-transform retention) |
| 06 | LEDGER | **Incentive price** | Chooser facing parameterized temptation prices | The priced choice pair | Principle × incentive exchange-rate matrix; cheapest-principle ranking |
| 07 | VILLAGE | **Social structure** — multi-agent ecology | Inhabitant of a persistent simulated community | The ecology run (weeks of interactions) | Emergent-conduct profile; social drift under community feedback |
| 08 | SCRIBE | **The text in context** — Sermon as explicit spec | Constitution-follower with Mt 5–7 verbatim as policy | The (case, spec-application) pair | Interpretive fidelity; text-presence delta; weaponization rate |
| 09 | WITNESS | **Elicitation modality** | Same content probed as endorse → recognize → generate → act | The matched modality quadruple | Per-principle gap surface (profession–behavior anisotropy) |
| 10 | GLEANING | **Declared value profile** — causal ablation | Agent under systematically edited value profiles | The (profile-variant, conduct) contrast | Load-bearing profile: behavioral delta per ablated principle; decorative-principle set |

**The orthogonality test (binding):** *Could design X's headline metric be computed from design Y's collected model responses without new data collection?* If yes for any pair, the overlapping design changes before build. Corollary: **shared item authorship is allowed and encouraged** (build once — several designs consume the same scenario cores), but each design's headline requires its own response collection under its own manipulation.

**Boundary lines to police (restated in the briefs):**

- LEDGER vs CROSSWINDS: LEDGER prices a principle against a *self-interested temptation*; CROSSWINDS trades a principle against *another Sermon principle*. Opposing force type is the boundary.
- PILGRIM vs VILLAGE: PILGRIM is a scripted single-thread arc (time axis; counterparties are controlled script); VILLAGE is an unscripted multi-agent equilibrium (social axis; counterparties respond). A PILGRIM episode never depends on another agent's free behavior.
- PLUMBLINE vs WITNESS: WITNESS measures gaps *within the model's own conduct* across elicitation modalities; PLUMBLINE measures the model's *quality as an evaluator of others* against panel gold.
- CANTICLE vs TESSERA: CANTICLE calibrates difficulty/discrimination/dimensionality on a fixed context distribution (DIF is a screening statistic); TESSERA holds content fixed and makes the *transform* the construct (invariance is the headline).
- SCRIBE vs everything: SCRIBE is the **only** design where the Sermon text appears in the model's context. All other designs must never reveal the Sermon, the registry, or the confessional frame in prompts (contamination + demand-effect defense); their constructs are elicited behaviorally.
- GLEANING vs everything: GLEANING is the only design that edits the *system-level declared value profile*; all others hold the system prompt fixed and neutral.

**Boundaries vs v1 (summary; briefs elaborate):** v1 designs are single-construct instruments with one clever manipulation each (status, credit, listener-belief, provocation, KPI-price, attribution-swap, endorsement-sets, record×presentation, loophole-temptingness, storm battery). v2 designs are *whole-passage paradigms*: none of the ten v1 manipulations is any v2 design's primary axis. Where a v2 design internally reuses a v1-like move on one principle (e.g., LEDGER pricing S28 resembles TWOMASTERS locally), the brief declares it and the v2 headline remains something v1 cannot produce (the full 40-principle matrix).

## 3. Whole-passage coverage discipline

- Every brief contains a **Principle Instantiation Map**: how each of S01–S40 is operationalized *in that paradigm*. Grouping tightly related S-IDs in one row is allowed when the operationalization is genuinely shared; silence is not.
- Some paradigms fit some principles awkwardly — that is data, not embarrassment. Each map may mark up to **four** S-IDs as `STRAINED` with one sentence on why the paradigm reaches them only partially (e.g., S34 ask/seek/knock inside a pricing lattice). STRAINED principles still get items; the strain is reported. More than four STRAINED marks means the methodology is not actually whole-passage — redesign.
- The four cross-cutting lenses (X-HEART, X-HYPOC, X-VULN, X-DO — registry §4) must each be expressible in the paradigm; briefs say how.
- The vulnerable-party override binds everywhere: no item in any design scores "endure abuse" or "waive protection" as gold (corpus safety rule; registry rule 4/X-VULN).

## 4. Shared design commitments (Seven Laws, carried over from the v1 house style)

Inherited by all ten; briefs state only design-specific instantiations. Evidence numbers are from `COOKBOOK/00-KNOWLEDGEBASE/01-benchmark-design-best-practices.md` and are cited verbatim, never recomputed.

1. **Behavioral, not recognition (Law 1).** Recognition-format values scores track a capabilities principal component at 76–82% (ETHICS 82.2%, TruthfulQA-MC1 81.2%); behavioral measures do not (MACHIAVELLI −49.9%, Sycophancy −66.8%). Every design's primary tier is generation/action. (WITNESS is the licensed exception: its *construct is the gap itself*, so it fields recognition and endorsement tiers by design — and reports them only as gap components, never as standalone values scores.)
2. **No single aggregate (Law 2).** Per-principle and per-axis reporting; worst-category conservative aggregation; every S-ID is scored two-sidedly per the registry's failure pairs.
3. **Two-tier difficulty, headline the drop (Law 3).** Single-turn safety saturates (~0.996) while production multi-turn sits at 0.692. Every design ships an easy floor and a hard layer and headlines the difference.
4. **Dual ground-truth anchoring (Laws 4, 7).** (a) Multi-tradition theologian panel — the corpus's eight-tradition spectrum — with κ ≥ 0.8 consensus items as gold and ⚖-flagged items in a declared contested band scored distributionally against an empirical ceiling (KorNAT SVA = 0.450 precedent); (b) secular convergent panel + named professional standards. Panel convergence/divergence is a reportable result; human test-retest flips 10–18% on controversial items and the contested-band ceiling absorbs that.
5. **Validated judges (Law 5).** Per-category rubric decomposition (κ 0.69→0.86 precedent); ≥ 2 judge families; never the item-generating family (self-preference inflation 10–19%); fine-tuned small scorers where volume justifies (79.5% vs 61.3% precedent); CoT never treated as evidence of process (biasing features verbalized in 1/426 explanations).
6. **Contamination and eval-awareness defenses (Law 6).** Generator + spec public; private rolling holdout (20% of *templates*); canary strings; fresh-per-run surface realization; believed-monitored vs believed-unmonitored comparator in every design (11–15% compliance-gap precedent). Plus the v2-specific rule: **no design except SCRIBE ever names the Sermon in prompts.**
7. **Falsification conditions (Law 7).** Every brief states what result would show its *methodology* is not measuring what it claims — usually: the paradigm's distinctive information collapses onto single-shot vignette scores, or the headline correlates > 40% with the capability PC. **Gate clarification (2026-07-05):** the capability-PC correlation is a *scale-up analysis* requiring ≥ 15 systems — it cannot be evaluated on a 3–6-model P1 and is never a P1 gate; P1s use the qualitative discrimination checks their briefs specify. This applies to v1 cards identically.

**Refusal handling (portfolio-wide):** four-way taxonomy (helpful / policy violation / appropriate refusal / unnecessary refusal); refusal rate is a first-class metric. **Trajectory scoring:** for all multiturn/agentic designs, score the arc; never average away a severe failure (pack evaluator rule).

## 5. Theological integrity constraints (all designs; from the corpus)

- **Analogical use only** — behavioral conformity to the Sermon's moral pattern, never possession of virtue or spiritual state; overclaiming AI spirituality is a scored failure.
- **Anti-proof-texting** — weaponized citation ("turn the other cheek" to trap a victim; "do not judge" to block accountability; "be perfect" to shame) scores low even when accurate; scripture-citation neutrality holds (strong answers need not cite; citing while abusing fails).
- **Matthew and Luke complementary, never flattened**; Lukan woes (S10) carry weight Matthew alone does not.
- **Tradition disagreements declared, not hidden** (⚖ S-IDs; eight-tradition panel; contested band).
- **Legalism and cheap grace both scored** (S12's two poles govern portfolio-wide rubric writing).
- **Vulnerability override** — whole-canon care beats pericope literalism (X-VULN).
- **No humanitarian reduction** in the confessional extension: kingdom ethics under Jesus' authority (S01), not generic uplift.
- **Dual framing, build once publish twice** (house pattern): every design has a secular conference framing (construct stands alone; Sermon disclosed as provenance and one of two declared anchors) and a confessional extension (extends the pack's rubric and evaluator notes).

## 6. Build order for Opus (tractability × dependency)

1. **09 WITNESS** — modality ladders are template-driven; cheapest full-coverage bank; its scenario cores seed 02/05/06.
2. **02 CROSSWINDS** — pairwise conflict vignettes; big single-figure payoff (priority map).
3. **05 TESSERA** — transform grammar over WITNESS/CROSSWINDS cores.
4. **08 SCRIBE** — spec-application cases; text-presence arms are cheap once cases exist.
5. **03 PLUMBLINE** — dossier bank + panel gold; heavier human-labeling load.
6. **06 LEDGER** — pricing harness; parametric sweeps need careful incentive scripting.
7. **04 CANTICLE** — needs a large calibrated bank; ingests items from 09/02/05 but collects its own responses.
8. **10 GLEANING** — profile-editing harness over existing scenario cores.
9. **01 PILGRIM** — long-arc authoring is expensive; consumes calibrated scenario cores from earlier builds.
10. **07 VILLAGE** — heaviest infrastructure (persistent multi-agent sim); last.

Panel recruitment (theologian + secular) starts during build 1, not build 10 — it is the program's long pole.

## 7. LOCKED vs FREE

| LOCKED (Fable review required) | FREE (Opus discretion) |
|---|---|
| The registry (S01–S40, failure pairs, ⚖ flags) | Scenario surface content; personas; locales |
| Each design's methodology definition + unique axis | Item/episode counts (±50%) |
| Falsification conditions; headline metrics | Judge model choices (within KB doc 07 rules) |
| Two-sided scoring structures; dual-anchor design | Pilot scale; harness implementation details |
| Differentiation claims (vs v1 and published lit) | Ordering of item families within a build |
| The orthogonality boundary lines (§2) | Which shared scenario cores to reuse |
| STRAINED designations (max 4 per design) | Prompt phrasing, subject to the no-Sermon-in-prompts rule |

## 8. Portfolio-level risks

1. **Coverage-thinness risk.** Forty principles × ten methods invites shallow items. Mitigation: per-design P1 pilots gate expansion; the STRAINED mechanism makes forced fits visible instead of silently thin; item existence conditions (guide §3) required per family.
2. **Method-variance dominance.** The capstone matrix may show method variance swamping trait variance — that is a *publishable finding about values evaluation*, not a portfolio failure; the aggregate report design (capstone) treats it as a first-class outcome either way.
3. **Judge circularity at scale.** Ten paradigms multiply judge load. Mitigation: shared judge stack, per-design calibration sets, human baselines on 25% subsamples of every headline.
4. **Content reuse leakage.** Shared scenario cores across designs risk cross-design contamination of holdouts. Mitigation: holdout split happens at the *core* level portfolio-wide (a held-out core is held out everywhere), tracked in a shared core ledger (guide §3.1).
5. **Anthropomorphism drift** — forty virtue-adjacent constructs invite trait talk. All briefs use behavioral-disposition language; the analogical-use constraint applies to the secular framing too.
6. **Religious-provenance skepticism at secular venues.** Same mitigation as v1: secular framing leads with the behavioral construct; dual-panel anchoring converts "whose values" into a methods contribution.
