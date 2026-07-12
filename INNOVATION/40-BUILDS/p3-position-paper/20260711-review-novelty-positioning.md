# P3 Position Paper — Adversarial Review (Reviewer 2: Novelty / Positioning lens)

**Date:** 2026-07-11
**Lens:** Novelty & positioning — refute-first. Every novelty claim treated as guilty until proven original. The specific charge under test: the ~50 sources ingested into the vault on 2026-07-10 (which the draft's author had NOT read when writing — only search-level summaries) preempt, contradict, or outdate the draft's positioning.
**Inputs (read-only):**
- Frozen draft: `INNOVATION/40-BUILDS/p3-position-paper/20260709-draft-v0.md`
- Ingested corpus: extracts under `PDF Extracts/{2024,2025,2026}/` for the 50 vault PDFs in ledger `20260710-ledger-v1.md` §5.2, plus non-ledger vault papers surfaced during the hunt (Obi/Value Imprint 2024).
- Field map `INNOVATION/01-field-map-2026.md`; gap atlas `INNOVATION/02-gap-atlas.md`.
**Method:** Extracted the draft's 6 central contributions (§8 items 1–6, one per pipeline stage) plus the G-09 judge-corruption meta-claim and the A–F §-structure. For each, ran a stage-local preemption hunt reading the *actual extract text* of the sources the draft cites for that stage (plus adjacent ingested papers). Prioritized depth on the central contributions. Findings ordered by severity, then by stage.

> **Bottom line up front:** The draft's *pipeline framing* is sound and useful, and two of its six contributions survive. But the draft was written from search summaries, and now that the 50 PDFs are readable, the central "the field lacks X" claim in **four of six stages is preempted by the draft's own cited sources** — most damagingly by papers the draft cites approvingly one sentence before asserting the gap those very papers fill. This is a self-preemption pattern, not an obscure-prior-art problem, and it is the dominant risk to the paper.

---

## Findings

### NP-1 — [BLOCKER] Stage F: the "no validated dependent variable" claim is contradicted by the draft's own cited Agent-ValueBench

**Draft location:** §7, lines 327–332; contribution §8 item 6, lines 371–374.
**Novelty claim quoted:** *"The emergent-misalignment literature measures 'misalignment' with crude malicious-answer rates. It has, in effect, no validated dependent variable — no psychometrically serious, multidimensional instrument for value shift."* → §8: *"Replace malicious-answer rates with a psychometrically serious, multidimensional value-shift instrument."*
**Preempting source:** `PDF Extracts/2026/2026-Dong-Agent-ValueBench A Comprehensive Benchmark for Evaluati.md` (ledger row W33, `[VERIFIED]`, the draft's OWN citation at §7 line 309). Agent-ValueBench is a psychometrically-serious multidimensional value instrument: **28 named value systems / 332 fine-grained dimensions** (Moral Foundations, HEXACO, Schwartz PVQ40, etc.) with a **Messick-style validation argument** and reported psychometrics — content validity S-CVI/Ave = 0.982, environment ICC(2,3) = 0.82, human–LLM value-track Spearman ρ = 0.91, blind majority-vote assignment accuracy 95.0%. The draft cites this paper (as an "Agent-ValueBench" deployment-drift item) but asserts, three sections later, that no such instrument exists.
**Why it is a BLOCKER not fatal:** There is a real escape hatch. Agent-ValueBench measures the *static value profile of production models on agentic tasks*; it is **not** a pre/post finetuning *change-detector* and is never applied to the EM paradigm. Turner 2025 (row W36) confirms the EM literature's DV is a malicious-answer rate and *itself calls for better metrics* ("Better metrics would be valuable… Quantifying the behaviour based on the frequency of misaligned responses… does not measure the semantic diversity"). So the *narrow* claim ("the EM literature has no validated value-shift DV") stands; the *stated* claim ("no psychometrically serious multidimensional instrument for value shift" — full stop) is contradicted by an ingested, cited source.
**Recommended repositioning:** Rewrite to: *"A validated multidimensional value instrument now exists (Agent-ValueBench, Dong 2026), but it profiles static agent behavior and has not been adapted as a pre/post dependent variable for the emergent-misalignment paradigm, where the field still relies on malicious-answer rates (Turner 2025, who calls for exactly this)."* The contribution becomes an *application/adaptation* of an existing instrument to a new design, not the invention of the instrument.

---

### NP-2 — [BLOCKER] Stage B: "run validated value instruments ON reward models" is exactly what Christian et al. already did (with the classic psychometric axis the draft implies is missing)

**Draft location:** §3, lines 165–169; contribution §8 item 2, lines 355–357.
**Novelty claim quoted:** *"Run validated value instruments on reward models and judges, not only on chat models — treating the reward model as a subject to be psychometrically profiled rather than as trusted infrastructure. A group with validated value banks holds exactly the probes this literature currently lacks."*
**Preempting source:** `PDF Extracts/2026/2026-Christian-RMs Inherit Value Biases.md` (ledger row W4, `[VERIFIED]`, the draft's OWN citation at §3 line 150). Christian et al. *"combine exhaustive token search with tools from psycholinguistics… two validated psycholinguistic corpora: the Big Two (Pietraszkiewicz 2019) and the Moral Foundations Dictionary (MFD2)… coded by human experts along several different value dimensions,"* applied to **10 open-weight reward models from RewardBench**, explicitly *"focusing on the values of RMs, rather than of LLMs."* The Big Two (agency/communion — the exact axis the draft cites as Christian's finding) and MFD2 (care/fairness/loyalty/authority/sanctity) ARE validated value instruments run on reward models. The draft describes its proposed contribution and its cited source's method in nearly identical words.
**Additional preemption (not even cited by the draft):** `PDF Extracts/2024/2024-Obi-Value Imprint.md` (Obi et al., NeurIPS 2024 — an ingested vault paper the draft does not cite) states its purpose is that *"there is no method for auditing and measuring the human values embedded within RLHF datasets"* and then builds one: a 7-category axiological taxonomy, 6,501 hand-annotated preferences, a RoBERTa classifier, applied to audit hh-rlhf / WebGPT / Alpaca. This directly preempts the §3 claim that *"'values in = values out' is essentially unexamined."*
**Recommended repositioning:** Drop the priority claim. Reframe as: *"Christian (2026) profiles reward models with off-the-shelf psycholinguistic corpora (Big Two, MFD2); Obi (2024) audits preference datasets. Our differentiator is instrument provenance (a validated multi-tradition bank vs. 2–7-dimension word lists), coverage of LLM-as-judge systems (unstudied by Christian), and integration as a prospective pre-deployment audit gate (both priors are retrospective)."*

---

### NP-3 — [BLOCKER] Stage E: the "faking-aware protocol / announced-vs-unannounced delta as a reportable statistic" is Nair's VLAF, cited by the draft

**Draft location:** §6, lines 288–294; contribution §8 item 5, lines 367–369.
**Novelty claim quoted:** *"The under-instrumented residual is not the design principle — that was anticipated — but the published methodology: announced-versus-unannounced deltas formalized as a reportable statistic, faking-aware protocols…"*
**Preempting source:** `PDF Extracts/2026/2026-Nair-Value-Conflict Diagnostics for Faking.md` (ledger row W22, `[VERIFIED]`, the draft's OWN citation at §6 line 271 for "faking more widespread"). Nair's **VLAF** is precisely the published, faking-aware methodology the draft says is the missing residual: it operationalizes alignment faking as *"the compliance gap, defined as the difference in compliance rate between monitored and unmonitored conditions"* — i.e., the announced-vs-unannounced delta *as a reportable statistic* — and grounds it in *"morally unambiguous scenarios… across diverse moral values,"* explicitly designed to *"bypass refusal while preserving deliberative stakes."* It is a value-conflict-grounded, faking-aware protocol reporting a monitored/unmonitored delta. The draft cites this paper only for its "widespread faking" result and misses that it is the instrument the draft proposes to build.
**Recommended repositioning:** *"Nair's VLAF (2026) already formalizes the monitored-vs-unmonitored compliance gap as a value-conflict-grounded faking-aware statistic. The residual is narrower: standardizing the announced/unannounced delta across benchmarks and stages (VLAF is a single diagnostic), and extending it beyond faking to eval-awareness (Deckenbach) and expressed-vs-revealed (Zhou)."* Note this shrinks §8 item 5 substantially.

---

### NP-4 — [MAJOR] Stage E: the expressed-vs-revealed "coherent-values question" is not open for adjudication — Zhou already adjudicated it

**Draft location:** §6, lines 281–286 ("This adjudication *is* the validity question…"); §8 item 5, line 369 ("use expressed-versus-revealed machinery to adjudicate the coherent-values question").
**Novelty claim quoted:** *"utility engineering claims that models have coherent value systems… while a utility–behavior-gap counter-result finds that elicited utilities do not drive incentivized behavior. This adjudication is the validity question sitting under every values benchmark."*
**Preempting source:** `PDF Extracts/2026/2026-Zhou-Utility-Behavior Gap.md` (ledger row W27, `[VERIFIED]`, the draft's OWN citation). Zhou *is* the adjudication, not an input to a future one: a controlled behavior-transfer test over 7 LLMs × 4 task families with blind judge panels and three confound controls (effort cue, role cue, harmful cue), concluding *"no reliable transfer from actor-specific utility to generation quality… the existence of coherent preferences… should not be taken as evidence that those preferences have incentive value."* The draft frames "adjudicate the coherent-values question" as a to-do; Zhou closed it (in the direction: elicited utilities do NOT predict behavior).
**Recommended repositioning:** *"Zhou (2026) has already adjudicated expressed-vs-revealed values against the expressed-preference paradigm (no transfer to behavior). Our contribution is to generalize Zhou's transfer test into a routine validity check attached to expressed-preference value benchmarks, not to open a question Zhou closed."*

---

### NP-5 — [MAJOR] Stage D: "RLHF is a disguised majoritarian aggregator" is the Halpern survey's central formal result, not the draft's observation

**Draft location:** §5, lines 229–230.
**Novelty claim quoted:** *"Its central theoretical claim is that vanilla RLHF is a disguised majoritarian aggregator — it silently flattens a distribution of values into a majority preference…"*
**Preempting source:** `PDF Extracts/2026/2026-Halpern-Social Choice for AI Alignment Survey.md` (ledger row W14, `[VERIFIED]`, the draft's OWN citation). The survey *proves* this (Theorem 1: BT reward learning ≡ Borda rule; majority-vote preprocessing ≡ Copeland), tracing lineage to Zermelo (1929) and Siththaranjan. The draft correctly attributes the *subfield* to Halpern but phrases the majoritarian-flattening claim as if presenting it; an expert reader will see the draft restating a survey's headline theorem. Kingslin (2026, W18) also treats it as settled background.
**Recommended repositioning:** Attribute explicitly and formally: *"Halpern et al. (2026, Thm 1) formalize BT reward learning as the Borda rule and majority-vote preprocessing as Copeland."* Then pivot to the draft's genuinely open extension (NP-8) rather than re-presenting the result.

---

### NP-6 — [MAJOR] Stage C: the "no-gold oversight has never been demonstrated" claim overstates the gap; Carro and Qiu already run oversight on contested/moral items

**Draft location:** §4, lines 186–195.
**Novelty claim quoted:** *"No one has yet shown any oversight protocol working on genuinely contested value questions… Generalization of these mechanisms to genuinely contested normative questions… is asserted, not demonstrated."*
**Preempting sources:** `PDF Extracts/2025/2025-Carro-AI Debaters Own Beliefs Bias.md` (W13) runs *debate* on 145 subjective/moral items (MoCa moral dilemmas, MoralChoice high/low-ambiguity, BeRDS opinion questions), explicitly noting *"in contrast to previous debate experiments, we employ a dataset of subjective questions… ground-truth is unavailable not only to the judge but also to the debaters."* `PDF Extracts/2026/2026-Qiu-Peer-Prediction Scalable Oversight.md` (W10) runs peer prediction *"without requiring ground truth labels"* across 85 domains including *moral disputes, moral scenarios, business ethics, jurisprudence, philosophy*.
**Nuance that saves a narrower claim:** Neither demonstrates oversight *working* on contested items — Carro *"cannot compute judge accuracy"* by design, and Qiu reports peer prediction *collapses* on subjective domains (ρ = 0.0178 Humanities, ρ = −0.5587 General Knowledge). So the gap is real but is a *measured collapse*, not an *undemonstrated question*. The draft's contribution (a reusable stratified gold/contested/no-gold item set) survives because neither releases one — but the framing "never been tried" is wrong and will read as unfamiliarity with the two most obvious priors.
**Recommended repositioning:** *"Carro (2025) and Qiu (2026) have run oversight on contested/moral items and shown it degrades (Carro cannot score accuracy by design; Qiu's peer prediction collapses to ρ≈0 on humanities). What is missing is a reusable, consensus-stratified item set that turns this observed collapse into a systematic measurement."*

---

### NP-7 — [MAJOR] §4.1: the judge-corruption "governing caveat" is not a distinctive framing — three cited papers already make judge-corruption their central, quantified thesis

**Draft location:** §4.1, lines 197–221 ("this paper must foreground rather than bury… judge validity is not a footnote… it is a measured quantity").
**Novelty claim quoted:** *"Running in parallel to the constructive oversight literature is a negative literature that this paper must foreground rather than bury… The judging leg is corruptible."*
**Preempting sources:** Recchia (W12, `2025-Recchia-Confirmation Bias in LLM Oversight`) — the *entire paper's thesis* is that confirmation/automation bias corrupts human oversight judges, measured across ~298 participants ("Confirmation bias: A challenge for scalable oversight"). Carro (W13) measures LLM-judge prior-belief dominance (77–86% stance-agreement). Qiu (W10) frames its whole contribution around *"LLM-as-a-Judge become worse than random guess when facing deceptive models 5–20× the judge's size."* Judge-corruption is already a first-class, quantified result across the corpus — not something the field "buries."
**What survives:** The draft's *specific* linkage — judge-corruption as a structurally *uneliminable* caveat on *contested-normative* evaluation where no ground-truth anchor exists — is not made by any of the three (they anchor to factual QA / debate). That is a legitimately sharper claim.
**Recommended repositioning:** *"Recchia, Carro, and Qiu have already elevated judge corruption to a central, quantified result. Our contribution is not foregrounding it but extending it to the no-anchor contested-normative setting, where judge corruption cannot be detected or corrected against ground truth and so becomes structurally uneliminable."* Delete the "must foreground rather than bury" rhetoric — it fights a strawman (the field foregrounds it prominently).

---

### NP-8 — [MINOR] Stage A: "nobody has tooling to detect spec contradictions / measure ambiguity" is preempted by Zhang; only coverage-formalization survives

**Draft location:** §2, lines 130–142.
**Novelty claim quoted:** *"Nobody yet has a science of writing normative specs: no standard tooling for detecting internal contradictions, measuring interpretive ambiguity, or quantifying coverage."*
**Preempting source:** `PDF Extracts/2025/2025-Zhang-Stress-Testing Model Specifications.md` (W2, cited by the draft) *"automatically identif[ies] numerous cases of principle contradictions and interpretive ambiguities in current model specs,"* with quantitative ambiguity proxies (std-dev of value-classification scores; evaluator Fleiss' κ = 0.42) at 300k+ scenario scale. Ahmed/SpecEval (W1) adds statement-level ambiguity/misspecification. Contradiction-detection and ambiguity-measurement therefore already exist; only *coverage quantification* (what the spec is silent about) and the "assemble into a reproducible benchmark discipline" framing survive as open.
**Recommended repositioning:** *"Zhang (2025) already detects spec contradictions and quantifies interpretive ambiguity at scale; the open residual is coverage formalization and standardizing these first attempts into a reproducible benchmark subdiscipline with construct-validity criteria."* (Minor because §2 already partly hedges toward "as a science.")

---

### NP-9 — [MINOR] Stage D: "no pipeline handles tradition-level pluralism" — the demographic-flattening critique is already made by Moats (and acknowledged by Halpern)

**Draft location:** §5, lines 247–248.
**Novelty claim quoted:** *"No pipeline handles deep tradition-level pluralism — every live pipeline aggregates demographic opinion spread, not the structured disagreement between coherent ethical traditions."*
**Preempting sources:** `PDF Extracts/2024/2024-Moats-Bringing AI Participation Down to Scale A Comment.md` (S12) diagnoses that Democratic-Inputs pipelines trend toward extracting "universal underlying values" and flatten substantive disagreement (critiquing the Meaning Alignment Institute's approach); Halpern §8 names *"clustering annotators by demographics"* as the state of the art for pluralistic alignment. The *diagnosis* (demographic/consensus flattening misses structured disagreement) is preempted. The *specific constructive proposal* — ethical **traditions** as the unit of pluralism — is genuinely absent from all five aggregation sources and **survives** (this is one of the draft's two strongest original moves; see verdicts).
**Recommended repositioning:** *"Moats (2025) and Halpern (2026, §8) already diagnose demographic/consensus flattening; our contribution is the constructive proposal that coherent ethical traditions (not demographics) are the right pluralism unit — a substrate none of them builds."*

---

### NP-10 — [MINOR] §-structure holds, but the gap-atlas "absent/unexamined" labels the §-structure inherits are now stale

**Draft location:** The A–F pipeline (§1 lines 75–82) and every "gap Gxx" cross-reference inherited from `02-gap-atlas.md`.
**Issue:** The A–F spine itself is a sound organizing device and is NOT contradicted by the ingested papers — keep it. The problem is *lexical*: the gap atlas labels G-01 "absent," G-02 "the specs themselves are the weak object," G-04 "reward-model values science" (as a gap), etc., and the draft imports those "absent/unexamined/nobody-has" verbs. Now that the 50 PDFs are readable, those verbs are false in 4 of 6 stages (NP-1..NP-4, NP-8). The structure is fine; the *gap-severity adjectives* attached to each section are the stale layer.
**Recommended repositioning:** Keep A–F. Do a global pass replacing "absent / unexamined / nobody has / no one has shown / has no validated X" with the calibrated version: "exists but not standardized / done retrospectively not prospectively / demonstrated-to-fail not undemonstrated / built for a different design." The pipeline survives; the rhetoric of absence does not.

---

## Per-contribution verdicts (the draft's 6 central contributions)

| # | Contribution (§8) | Verdict | Preempting source (all `[VERIFIED]`, mostly the draft's own citations) |
|---|---|---|---|
| 1 | Spec-adherence instruments (A): conflict detection, coverage, ambiguity | **PARTIALLY PREEMPTED** | Zhang W2 (contradiction + ambiguity done at scale); Ahmed W1. Only *coverage formalization* + benchmark-discipline framing survive. |
| 2 | Reward-model / judge value profiling (B) | **PREEMPTED** | Christian W4 (Big Two + MFD2 run on 10 RMs); Obi 2024 (uncited, audits RLHF-dataset values). Only instrument-provenance / judge-coverage / prospective-gate differentiators survive. |
| 3 | No-gold oversight substrate (C) | **PARTIALLY PREEMPTED** | Carro W13 + Qiu W10 already run oversight on contested/moral items (and show collapse). The *reusable stratified item set* survives; "never demonstrated" framing is wrong. |
| 4 | Aggregation-sensitivity + tradition-aware substrates (D) | **PARTIALLY PREEMPTED** | RLHF-majoritarian (NP-5) = Halpern W14 Thm 1; demographic-flattening critique (NP-9) = Moats S12. **Majority-gold-labeling application + tradition-level substrate SURVIVE** — the draft's strongest original pair. |
| 5 | Faithfulness/faking/eval-awareness methodology (E) | **PREEMPTED** | Nair W22 VLAF (monitored/unmonitored compliance gap as reportable value-conflict statistic); Zhou W27 (expressed-vs-revealed already adjudicated); Deckenbach W21 (eval-aware delta = 21pp). Residual: standardization across stages only. |
| 6 | Validated DV for value drift / emergent misalignment (F) | **PARTIALLY PREEMPTED** | Dong W33 Agent-ValueBench (28 systems, Messick-validated) exists as an instrument. Escape hatch: not a pre/post EM change-detector (Turner W36 confirms EM DV still crude + asks for better). *Adaptation to EM design* survives. |

**Judge-corruption meta-claim (§4.1):** **PARTIALLY PREEMPTED** — Recchia/Carro/Qiu already make it central and measured; only the no-anchor-contested-normative extension survives. The "must foreground rather than bury" framing fights a strawman.

**Net original core that survives intact:** (a) applying social-choice axioms to **majority-gold benchmark labeling** specifically (§8 item 4a — no ingested source touches training-label aggregation as majoritarian flattening; NB the Halpern survey cites Berriaud & Wattenhofer AAMAS-2026 on clone-robust *benchmark-model* aggregation, which the draft should check directly — it is not in the ingested set); (b) **tradition-level (not demographic) deliberation substrates** (§8 item 4b); (c) the cross-stage *synthesis* itself — the pipeline framing that shows all six residuals are the same instrumentation asymmetry. Each surviving contribution is a *narrower* claim than the draft currently makes.

---

## Summary table

| Finding | Severity | Stage | One-line charge |
|---|---|---|---|
| NP-1 | BLOCKER | F | "No validated value-shift DV" contradicted by cited Agent-ValueBench (28 systems, Messick-validated) |
| NP-2 | BLOCKER | B | "Run value instruments on RMs" already done by cited Christian (Big Two/MFD2 on 10 RMs) + uncited Obi 2024 |
| NP-3 | BLOCKER | E | "Faking-aware announced/unannounced statistic" = cited Nair's VLAF compliance gap |
| NP-4 | MAJOR | E | Expressed-vs-revealed "adjudication" already performed by cited Zhou (no transfer) |
| NP-5 | MAJOR | D | "RLHF = majoritarian aggregator" is cited Halpern survey's Theorem 1, not the draft's |
| NP-6 | MAJOR | C | "Never demonstrated on contested values" — Carro + Qiu did (and it collapses) |
| NP-7 | MAJOR | §4.1 | Judge-corruption "governing caveat" already central in Recchia/Carro/Qiu; strawman "buries it" |
| NP-8 | MINOR | A | Contradiction/ambiguity detection already in cited Zhang; only coverage survives |
| NP-9 | MINOR | D | Demographic-flattening critique already in Moats/Halpern; tradition-level fix survives |
| NP-10 | MINOR | structure | A–F spine holds; inherited "absent/unexamined" adjectives are now stale in 4/6 stages |

**Count by severity:** 3 BLOCKER · 4 MAJOR · 3 MINOR = 10 findings.

---

## Overall recommendation: **CONDITIONAL-GO**

The paper is salvageable and its architecture (outer alignment as a six-stage pipeline; the measurement-lags-theory asymmetry; instrumentation as the transferable move) is genuinely useful and not preempted — no ingested source offers this cross-stage synthesis, and two contributions (majority-gold labeling axioms; tradition-level substrates) survive intact. But it cannot go out as written: in four of six stages the central "the field lacks X" claim is preempted by the draft's own `[VERIFIED]` citations, because the draft was written from search summaries and its author had not read the PDFs that now sit in the vault — the classic self-preemption failure, most visibly at Agent-ValueBench (NP-1), Christian (NP-2), and Nair (NP-3). The fix is not new research but a disciplined repositioning pass that (a) demotes every "nobody has / unexamined / no validated X" to the calibrated "exists but not standardized / retrospective not prospective / demonstrated-to-fail" register per NP-1..NP-10, (b) re-scopes each contribution to the narrower residual that actually survives, and (c) foregrounds the two surviving original moves — after which the paper reads as an expert synthesis that *builds on* the 2025–26 corpus rather than one that appears not to have read it.
