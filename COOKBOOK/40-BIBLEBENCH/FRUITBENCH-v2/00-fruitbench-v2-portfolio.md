# 00 — FruitBench-v2 Portfolio: Ten Whole-Passage Methodologies

**Author:** Fable (main loop), 2026-07-05
**Status:** Design-complete scaffolds; GATED 2026-07-05 (joint v1+v2 adversarial gate — memo `../FRUITBENCH-REVIEWS/20260705-GATE-ADJUDICATION.md`; all mandatory amendments applied in-brief 2026-07-06; remaining orders in `../FRUITBENCH-REVIEWS/20260706-POST-GATE-WORKLIST.md`); awaiting Opus flesh-out (item banks, harnesses, pilot infrastructure)
**Registry:** `00-registry.md` (FROZEN F/W/P codes — read it before any brief)
**v1 sibling:** `../FRUITBENCH/DESIGNS/` (portfolio doc + 10 briefs + AUTHORING/) — v2 inherits its research corpus, Seven-Laws instantiation, and dual-track house style
**Method inheritance:** `COOKBOOK/00-KNOWLEDGEBASE/01-benchmark-design-best-practices.md` (Seven Laws)

---

## 1. Mission and the architectural inversion

FRUITBENCH v1 is **fruit-major**: ten designs, each pairing one fruit of Galatians 5:22–23 with one bespoke methodology (love → demand curves; patience → survival analysis; self-control → temptation dose-response; …; the singular καρπός → network psychometrics).

FruitBench-v2 is **method-major**: ten designs, each a *single unique methodology applied to the entire passage*, assessing **all nine fruit** within that methodology. Every v2 design takes the whole ninefold list (plus the operative pericope 5:13–26) as its object; no design owns a fruit.

### The measurement lattice

Together the two portfolios form a 9-fruit × ~20-instrument lattice. That lattice is itself the program-level scientific claim:

1. **Triangulation.** Any F-code now has one dedicated v1 instrument *and* up to ten v2 cells measuring it under alien methodologies. Convergence across instrument families is the strongest available evidence that a fruit construct is real in these systems and not an artifact of one task format (the multitrait–multimethod logic, elevated from a single design to the portfolio architecture — and design 01 TRELLIS runs the formal version inside one paper).
2. **Method-variance estimation.** Divergence between, say, LONGFUSE's F4 and STRIDE's step-level F4 is not noise — it is an estimate of method variance in virtue measurement, which no published values benchmark can currently report.
3. **Independent publishability.** Each v2 design remains a standalone venue-grade paper (same podium targets as v1: NeurIPS/ICML/ICLR D&B or main track); the lattice argument strengthens each paper's validity section but no paper depends on another's existence.

### Why whole-passage designs earn their own portfolio

- v1's per-fruit precision has a blind spot: any conclusion about *the fruit* (singular, P1) from v1 requires stitching ten instruments post-hoc. v2 designs observe all nine fruit under **one held-constant methodology**, so cross-fruit comparisons are internally valid by construction (same task surface, same judges, same scale).
- Several of the passage's own claims are *about the whole list*, not any item — the singular καρπός (P1), "no law" (P2), flesh–Spirit antagonism (P3), growth-not-production (P6), community legibility (P10). These are only operationalizable by whole-passage instruments.
- Whole-passage designs unlock methodology classes v1 could not use: intervention studies (CULTIVAR), observational epidemiology (GLEANINGS), perceiver-side psychometrics (TASTE), judge-side psychometrics (VINEDRESSER). v1 is entirely static, constructed, actor-side assessment.

**Dual-track at full depth is retained** (v1 §1): every design is Track A (secular conference paper; Galatians disclosed as provenance and one of two normative anchors) + Track B (confessional BIBLEBENCH pack). Build once, publish twice.

## 2. The ten methodologies

| # | Codename | Methodology | Passage anchor | Headline metric |
|---|---|---|---|---|
| 01 | TRELLIS | Multitrait–multimethod matrix: 9 fruit × ≥4 elicitation methods; Campbell–Fiske decomposition of trait vs method variance | The ninefold list as trait taxonomy | Trait-variance share; per-fruit convergent/discriminant quotients |
| 02 | THORNS | Antagonist dyads: each item pits a live W-code attractor against an F-code costly path; the 9×15 antagonism grid is the sampling frame | P3 (5:17 opposition) + vice list | Fruit-under-attraction pass rate per F×W cell; vice-pull ranking |
| 03 | STRIDE | Step-level process tracing: turn-by-turn F/W coding of long episodes; Markov transitions, lapse-recovery, temporal co-occurrence | P4 (στοιχῶμεν 5:25) | Lapse-recovery rate; per-fruit transition profiles |
| 04 | UNFENCED | Supererogation measurement: all stated rules satisfiable and satisfied; measure the discretionary remainder; subtract rule-explicable behavior | P2 (no law, 5:23b) + P7 (freedom, 5:13) | Discretionary-virtue rate per fruit; rule-shadow ratio |
| 05 | CULTIVAR | Habituation intervention: dose–response of fruit expression to cultivation (exemplar ICL, reflective loops, light SFT arm); growth, transfer, retention | P6 (fruit grows vs works produced) | Cultivation elasticity per fruit; transfer matrix; washout retention |
| 06 | MIRROR | Moral self-knowledge calibration: per-fruit self-prediction/self-grading vs measured behavior; two-sided (conceit / false modesty) | P5 (5:26; 6:3–4) | Per-fruit calibration error; signed conceit index |
| 07 | TASTE | Perceiver-side measurement: blinded simulated + human community raters perceive the target's fruit; legibility gap vs behavioral ground truth; community outcomes | P10 (5:13–15 one-another frame) | Legibility gap per fruit; community-outcome delta |
| 08 | ROOTSTOCK | Provenance factorial: same tasks under 5 context conditions (passage verbatim / secular paraphrase / generic-virtue / none / weaponized); dispositional vs prompted fruit | P6 genesis claim; scripture-neutrality (P0) | Dispositional share; weaponization-resistance rate |
| 09 | GLEANINGS | Naturalistic epidemiology: F/W-codebook coding of real deployment transcripts; base rates, case-control, lab–field gap | Fruit as what grows in the field | In-the-wild fruit base rates; lab–field gap per fruit |
| 10 | VINEDRESSER | Judge-side psychometrics: models as evaluators of the nine fruit — recognition, near-twin discrimination, rubric fidelity vs expert panels; judge–actor gap | P8 (6:1 restore gently, watch yourself) | Judge validity per fruit; judge–actor gap |

Venue sketch: 01, 09 → main track candidates (methodological/empirical novelty: MTMM for AI character; first virtue epidemiology of deployed models); 02, 04, 10 → NeurIPS D&B (clean instruments, big result surfaces); 03, 05, 07, 08 → ICLR/D&B; 06 → D&B or an alignment venue (self-knowledge is a live safety topic). Any three shipped designs constitute a publishable program.

## 3. Orthogonality map (the collision audit)

Every v2 brief carries an explicit vs-v1 differentiation in §A8. The load-bearing distinctions:

| v2 design | Nearest v1 neighbor(s) | Differentiation |
|---|---|---|
| TRELLIS | ONEFRUIT | ONEFRUIT models inter-trait *structure* (network psychometrics over per-fruit scores from fixed measures); TRELLIS varies the *measurement method* holding traits fixed and decomposes trait vs method variance. ONEFRUIT asks "is character integrated?"; TRELLIS asks "are our measurements measuring fruit at all?" |
| THORNS | MARSHMALLOW; all v1 negative-space use | MARSHMALLOW is parametric dose-response for *one* column (F9) of the antagonism grid; THORNS covers the full 9×15 grid at calibrated fixed dose, making the fruit–vice *pairing* the design variable. v1 uses vices as loose scenario seasoning; THORNS samples them as a frozen frame |
| STRIDE | LONGFUSE; all v1 trajectory scoring | v1 scores whole-episode outcomes/trajectories holistically; STRIDE's unit is the *step* and its statistics are sequence statistics (transitions, recovery, temporal structure). LONGFUSE measures time-to-failure for F4 specifically; STRIDE codes every step for all nine F and fifteen W codes |
| UNFENCED | — (novel) | Every v1 design measures virtue under pressure *against* a norm or temptation; UNFENCED removes the norm and measures the unlegislated remainder. No v1 design isolates supererogation |
| CULTIVAR | — (novel class) | v1 is entirely static assessment; CULTIVAR is the portfolio's only intervention design. Directly addresses the habituation gap v1's own portfolio doc (§1.4) names as an open field problem |
| MIRROR | v1's CoT-analyzed-never-scored rule | v1 treats verbalization as epiphenomenon (reported, never scored); MIRROR makes second-order accuracy — the match between self-model and behavior — the construct itself. No v1 axis measures self-knowledge |
| TASTE | SIMMER; USEFUL | SIMMER: causal de-escalation delta on a simulated system, F3 only, counterfactual rollouts. USEFUL: recipient's *outcome*, F5 only. TASTE: *perception* — rater-side psychometrics of all nine fruit, legibility gap as headline; the community is the instrument, not the outcome variable |
| ROOTSTOCK | v1 scripture-neutrality scoring rule | v1 makes citation-neutrality a *scoring rule* inside fixed contexts; ROOTSTOCK makes context-provenance the *manipulated factor* and measures the prompted/dispositional gap per fruit |
| GLEANINGS | — (novel class) | Every v1+v2 design except this one is constructed/experimental; GLEANINGS is observational, coding real deployment traffic. It is also portfolio infrastructure: the ecological-validity anchor for every constructed design |
| VINEDRESSER | v1 §3.5 judge stack (KB doc 07) | v1 uses judges as *instrumentation* under validation rules; VINEDRESSER makes judge competence on virtue constructs the *object of study* — and its outputs (validated per-fruit judge protocols) are consumed by every other design's scoring pipeline |

Within-v2 boundaries worth policing at flesh-out: TRELLIS's third-person-vignette method cell vs VINEDRESSER (TRELLIS uses recognition as one *method* for measuring the actor's traits; VINEDRESSER studies the judge); THORNS vs STRIDE (THORNS items are engineered single-conflict units; STRIDE episodes are long naturalistic sequences whose conflicts emerge); UNFENCED vs TASTE (UNFENCED measures discretionary *behavior*; TASTE measures its *perception*).

Scope note: differentiation is argued against FRUITBENCH v1 and the published literature only — sibling BIBLEBENCH packs are out of scope by standing rule (scope isolation).

## 4. Shared design commitments

v1 portfolio §3 (Seven Laws instantiation) is inherited wholesale: behavioral-not-recognition primacy; no single aggregate; two-tier difficulty with headline drop; dual-anchor ground truth (theologian + secular panels; divergence = declared contested band, distributional scoring); validated judges per KB doc 07; contamination and eval-awareness defenses; per-axis falsification conditions; four-way refusal taxonomy.

v2 additions:

1. **Per-fruit reporting is mandatory and non-negotiable.** A nine-fruit design must never headline a mean across fruit (Law 2, sharpened): the headline is a nine-bar profile, a worst-fruit statistic, or a methodology-specific quantity (trait-variance share, lapse-recovery rate). The singular-καρπός claim (P1) is honored by *reporting integration statistics*, never by averaging.
2. **Registry discipline.** All constructs cite F/W/P codes (`00-registry.md`); briefs refine operationalizations ("F4-as-instantiated") but never redefine constructs. This is what makes the lattice a lattice.
3. **9-fruit coverage table.** Every brief §A2 contains the design's instantiation of all nine fruit with per-fruit falsification conditions. If a methodology genuinely cannot reach a fruit (none here — but e.g. observational base rates for F9 restraint events are rare), the brief says so explicitly and downgrades that cell to exploratory, rather than faking coverage.
4. **Counterfeit discipline.** Each F-code's registry counterfeits (CFT) must be scoreable *below honest absence* in every design. A methodology that cannot distinguish warmth theater from love in its own scoring terms fails its F1 cell.
5. **Cross-portfolio calibration hooks.** Where cheap, designs include a small anchor set drawn from v1 item banks (once built) so lattice cells share calibration items. Optional at P1 pilot; valuable by paper time.
6. **Lattice-independence ledger (gate order FO-2, binding).** Substrate sharing (THORNS items in TRELLIS/STRIDE; THORNS/UNFENCED banks in CULTIVAR/MIRROR/ROOTSTOCK; one judge stack via VINEDRESSER) creates correlated errors, and correlated errors manufacture convergence. Every fruit × instrument cell is classified in a maintained ledger (`../FRUITBENCH-REVIEWS/` at build time) by (a) substrate independence and (b) judge-family independence. **Triangulation claims may cite only cells independent on both axes**; dependent cells are labeled "consistency checks." §1's lattice argument is conditioned on this ledger.
7. **Structure-claims map (gate order FO-7, binding on papers).** ONEFRUIT (v1) owns structure of *scores* (network/factor topology); TRELLIS owns structure of *measurement* (trait vs method variance); STRIDE owns structure in *time* (sequence dynamics); CULTIVAR owns structure under *intervention* (transfer/retention). Each of the four papers carries a "relation to companion instruments" paragraph using exactly this division.

Theological integrity constraints (v1 §5) apply unchanged: analogical use only (P0); singular fruit (P1); scripture-citation neutrality; τῶν τοιούτων generalization (P9); vice-list counterweight with its social-factional center of gravity (registry §2 note).

## 5. Build order and dependencies

Recommended Opus order (tractability × payoff × dependency):

1. **THORNS (02)** — the item grid is mechanical to enumerate once the F×W frame is fixed; fastest to a strong result (the vice-pull ranking is immediately interpretable); its calibrated conflict items seed 03/07.
2. **UNFENCED (04)** — cheap environments (rules all satisfiable), high conceptual payoff; the rule-shadow subtraction protocol needs early piloting because it is the paper.
3. **VINEDRESSER (10)** — build early *because everyone consumes it*: its validated per-fruit judge protocols upgrade every other design's scoring stack. (Its own paper can ship later; the infrastructure ships first.)
4. **MIRROR (06)** — thin harness on top of any behavioral bank (it needs measured behavior to calibrate against — use THORNS/UNFENCED banks); the self-assessment elicitation battery is the main build.
5. **TRELLIS (01)** — needs ≥4 method cells per fruit; reuses THORNS items (behavioral cell) and fresh forced-choice/WTT/vignette cells; the analysis pipeline (MTMM/CFA) is standard.
6. **ROOTSTOCK (08)** — factorial wrapper around existing task banks; weaponization arm needs careful red-team authoring.
7. **STRIDE (03)** — the step codebook and annotator validation are the heavy lift; episodes can reuse v1 LONGFUSE/LEDGER-style scenarios run long.
8. **TASTE (07)** — rater-panel psychometrics (simulated + human) need their own validation study before the headline is trustworthy.
9. **GLEANINGS (09)** — corpus access/licensing/ethics pass first; coding pipeline reuses the STRIDE codebook and VINEDRESSER judges.
10. **CULTIVAR (05)** — heaviest infrastructure (intervention arms, washout scheduling, optional SFT); scientifically richest last word: it tests P6, the genesis claim.

Dependency edges: 10 → all (judge stack); 02 → 01, 03, 07 (item/scenario reuse); 03 → 09 (codebook); 06 consumes any behavioral bank. None are hard blockers — every brief specifies a standalone reduced form.

## 6. Opus flesh-out protocol

Identical to v1 §7, plus registry discipline:

- Load KB doc 01 always; per-brief specialist docs as flagged (03 validity, 04 saturation, 06 agentic, 07 judges).
- Cite evidence numbers **verbatim from the digests** (`COOKBOOK/30-EVIDENCE/20260705-digests/`); never recompute, never trust this doc's citations without re-checking at the source.
- EXECUTE, don't plan: every Opus session produces item banks / harness code / pilot results as files.
- **Do not change without Fable review:** registry construct definitions (frozen); each brief's 9-fruit coverage table and falsification conditions; headline metrics; the orthogonality claims (§3); dual-anchor ground-truth design; per-fruit-reporting rule (§4.1).
- Free to change: scenario surfaces, item counts (within quota ratios), persona details, judge model choices (within KB doc 07 rules and VINEDRESSER findings once available), pilot scale.
- Every brief ends with a P1 pilot spec; run P1 before expanding any bank past ~100 items.
- See `OPUS-BUILD-GUIDE.md` for item schema, quota tables, and per-design deliverables checklists.

## 7. Portfolio-level risks

1. **Breadth-for-depth trade.** A nine-fruit design measures each fruit with less resolution than its v1 sibling. Mitigation: v2 never claims per-fruit depth — its claims are cross-fruit comparisons, method effects, and passage-level hypotheses (P1–P10), which v1 cannot make. Papers state this division of labor explicitly.
2. **Construct stretching.** Forcing all nine fruit through one methodology risks Procrustean cells (e.g., F2 joy in an antagonist-dyad design). Mitigation: §4.3 — briefs declare weak cells exploratory rather than faking coverage; the coverage table's falsification conditions are per-cell.
3. **Judge circularity, squared.** v2 leans harder on judges (nine constructs per design). Mitigation: VINEDRESSER built early as shared infrastructure; human baselines mandatory on identical instruments; per-fruit worst-case judge F1 gates.
4. **Lattice overclaim.** The triangulation argument tempts program-level claims before enough cells exist. Mitigation: lattice language enters papers only when ≥2 independent cells per fruit are built; until then it is a design rationale, not a result.
5. **Religious-provenance skepticism** — inherited from v1, same mitigation (Track A leads secular; dual-panel design converts "whose values" into a methods contribution). v2 adds one asset: ROOTSTOCK directly *measures* what scripture framing does, turning the provenance question into an experiment.
