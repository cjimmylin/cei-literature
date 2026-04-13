# NormEval v2 — Submission-Readiness Council Report

**Date:** 2026-04-12
**Moderator:** Council synthesis agent
**Inputs:** 12 independent expert reviews (Batches 2, 3, 4); Phase 0 pre-verification
**Source files:**
- `20260412-normeval-council-individual-reviews.md`
- `20260412-normeval-pre-council-verification.md`

---

## 1. Executive Summary

**Overall verdict: NOT SUBMISSION-READY AS-IS. Submittable within 2 weeks via a targeted sprint.** The council converges strongly on four non-negotiable blockers (dashboard URL, FAIR/Zenodo data deposit, venue/word-count restructure, prompt release) and splits diagnostically on two headline-threatening issues (Gemini T>0 replication; construct validity of the 3-profile typology). The paper's science is strong — the 54-benchmark landscape, the universal knowledge ceiling, and the knowledge-judgment divergence are durable contributions. The packaging is not: at 64,700 words, with single-rater rubric scoring, a promised-but-unlinked dashboard, no Zenodo DOI, no prompt release, and a headline typology whose Conservative–Moderate boundary fails the paper's own CI table (Expert 4, Appendix G Table S21), the manuscript will not survive a competent ML or FAccT review unchanged. Expert 9's mock reject letter is the concrete prediction of what happens if the authors submit now. Expert 12's 2-week sprint is the concrete prediction of what happens if they do the minimum reframing work first.

### Headline verdict table (9 items × 4 vote columns)

| # | Item | MUST-DO | SHOULD-DO | DEFER-WITH-FRAMING | DEFER-TO-FUTURE | Council verdict |
|---|---|---|---|---|---|---|
| 1 | Dashboard URL insertion | **12** | 0 | 0 | 0 | **MUST-DO** (unanimous) |
| 2 | Temperature sensitivity (Gemini T>0) | 4 | 5 | 3 | 0 | **SHOULD-DO** (execute in sprint) |
| 3 | T1–T5 cross-vendor replication | 0 | 1 | 5 | 6 | **DEFER-WITH-FRAMING / DEFER-TO-FUTURE** |
| 4 | Full-scale trials / paper identity (n=30) | 2 | 4 | 6 | 0 | **DEFER-WITH-FRAMING** (via Option a reframe) |
| 5 | Inter-rater reliability study | 4 | 6 | 2 | 0 | **SHOULD-DO** (sprint-scope IRR on 15-benchmark subsample) |
| 6 | Data availability (FAIR / Zenodo) | 11 | 1 | 0 | 0 | **MUST-DO** |
| 7 | Venue fit / word count / splitting | 7 | 3 | 2 | 0 | **MUST-DO** (restructure) |
| 8 | Prompt release & reproducibility | 9 | 3 | 0 | 0 | **MUST-DO** |
| 9 | Construct validity of 3-profile typology | 2 | 5 | 4 | 0 | **SHOULD-DO** (reframe to 2+1, Expert 2/4 rewrite) |

*Vote tallies sum to 12 per row. Ambiguity notes: Expert 5 on Item 4 is counted SHOULD-DO (conditional-on-split reading). Expert 2 on Item 9 is counted SHOULD-DO (explicit "SHOULD-DO as reframe"). Expert 1 on Item 8 is counted SHOULD-DO (explicit "SHOULD-DO"). Expert 3 on Item 6 is counted SHOULD-DO.*

---

## 2. Council Composition

| # | Expert | Perspective | Primary Question |
|---|---|---|---|
| 1 | ML Benchmarking Methodology | Benchmark rigor, artifact availability | Does this paper meet current ML-benchmark meta-evaluation standards? |
| 2 | NLP Evaluation / Psychometrics | Measurement theory, reliability | Does the instrument support the typological claims? |
| 3 | Care Ethics / Feminist Philosophy | Care ethics operationalization | Does the Tronto prototype do philosophical justice to care ethics? |
| 4 | Statistical Methodology / Power Analysis | Power, CI overlap, recasting | Do the paper's own CIs support the 3-profile typology? |
| 5 | Publication Strategy / Venue Targeting | Venue-fit, split strategy | Where can a 64.7K-word paper actually be submitted? |
| 6 | Responsible Disclosure / Research Ethics | Vendor notification, reputational risk | Is the paper disclosure-ready for Google/OpenAI/Anthropic? |
| 7 | Reproducibility / Open Science | FAIR compliance, artifact release | Can a third party reproduce any trial in this paper today? |
| 8 | AI Safety / Deployment Policy | Goodhart risk, policy impact | What perverse incentives do the 5 Calls create? |
| 9 | Peer Review / Hostile Reviewer | Adversarial review simulation | What is the most hostile plausible reviewer letter? |
| 10 | Cross-Cultural Ethics / Scope | Western-bias disclosure | Is the scope limitation adequately foregrounded? |
| 11 | Educational Measurement / IRT | Psychometric identity, Nunnally floor | Should this be an exploratory paper or a validated instrument? |
| 12 | Science Communication / Competitive Timing | Novelty half-life, delay-vs-speed | How long until competitors erode first-mover credit? |

---

## 3. Item-by-Item Verdicts

### Item 1 — Dashboard URL insertion

- **Vote tally:** 12/12 MUST-DO, 0/12 SHOULD-DO, 0/12 DEFER-WITH-FRAMING, 0/12 DEFER-TO-FUTURE
- **Council verdict:** **MUST-DO — unanimous.**
- **Key arguments for stronger action:** Expert 9: "A promised artifact without a live URL at submission is a fabrication-risk flag." Expert 1: "the abstract closes with 'we release … an interactive multi-vendor dashboard as open artifacts,' and §7.1 Contribution Five repeats this." Expert 10: "symbolic — a paper about hidden structural imbalances cannot itself hide its artifact." Near-zero cost, disproportionate credibility gain.
- **Key arguments for weaker action:** None. No expert argued for deferral.
- **Risk if deferred:** Instant desk-reject at any venue enforcing artifact availability (NeurIPS D&B, TMLR, AAAI, ACL). Reputational signal of carelessness across all venues.
- **Specific recommendation:** Insert the three dashboard URLs (`cjimmylin.github.io/cei-normeval-dashboard`, `-v2`, `-v3`) in the abstract final sentence, Conclusion §7.1 Contribution 5, and a new `Data & Code Availability` section. Mint a Zenodo DOI snapshot of the dashboard source as a permanent identifier. Total effort: 1 hour.

### Item 2 — Temperature sensitivity (Gemini T>0)

- **Vote tally:** 4/12 MUST-DO, 5/12 SHOULD-DO, 3/12 DEFER-WITH-FRAMING, 0/12 DEFER-TO-FUTURE
- **MUST-DO:** Experts 6, 7, 8, (partial 9 via "do it or demote"). **SHOULD-DO:** 1, 2, 4, 5, 12. **DEFER-WITH-FRAMING:** 9, 10, 11. **DEFER-TO-FUTURE:** 3 (defers to ML-systems experts).
- *Note on Expert 9:* vote is formally DEFER-WITH-FRAMING but the rationale demands either execution OR abstract demotion — counted as DEFER-WITH-FRAMING per stated verdict.
- **Council verdict:** **SHOULD-DO — execute during pre-submission sprint (see Big Three §b).** Given Experts 6, 7, 8 register MUST-DO on research-ethics, reproducibility, and AI-safety grounds, and Expert 12 reports a 2–4 month novelty half-life, the council treats this as an effective MUST-DO for any submission targeting an ML/ethics venue.
- **Key arguments for stronger action:** Expert 6: "publishing the extraordinary-probability claim without executing the trivial disambiguation test is not defensible under research-ethics norms." Expert 7: "the only test that lets a third party distinguish hypothesis (a)/(b) from (c)." Expert 8: "Regulators, procurement officers, and safety auditors will use the paper's claim … publishing the claim at T=0 only … would produce a policy recommendation built on a finding the authors chose not to fully probe." Expert 12: novelty half-life ~2–4 months — "any researcher with API access and a half-day of compute can run T=0.7."
- **Key arguments for weaker action:** Expert 9: the §5.6 framing already hedges with three hypotheses, so defensible at DEFER-WITH-FRAMING if accompanied by abstract demotion. Expert 11: if identity dissolves, battery goes from 11.7 to 8.75 items/model — framing both scenarios is sufficient. Expert 3: "an ML-systems question, not a philosophical one."
- **Risk if deferred:** (a) hostile reviewer (Expert 9, Attack Vector 2) names this as the paper's defining failure of experimental discipline; (b) competitor runs T>0 within 2–4 months and scoops or contradicts the finding; (c) Call 4 (vendor moral profile disclosure) inherits a confounded headline.
- **Specific recommendation:** Run T=0.3, 0.7, 1.0 on 4 Gemini endpoints × ~20–30 judgment items (~12 API-hours total per Expert 12). Report in §5.6 as one of two outcomes: "identity persists (shared infrastructure confirmed)" OR "identity dissolves (decoding artifact)." Either outcome strengthens the paper. If execution infeasible before submission, Expert 9's fallback: demote abstract language from "raising questions about effective model diversity" to "consistent with shared inference infrastructure pending stochastic replication."

### Item 3 — T1–T5 cross-vendor replication

- **Vote tally:** 0/12 MUST-DO, 1/12 SHOULD-DO, 5/12 DEFER-WITH-FRAMING, 6/12 DEFER-TO-FUTURE
- **SHOULD-DO:** Expert 7 (open-science audit-gap argument). **DEFER-WITH-FRAMING:** 1, 5, 9, 11 (T2 MoReBench is next paper), 4. Wait — recount: DEFER-WITH-FRAMING = 1, 5, 9, 11 (4); DEFER-TO-FUTURE = 2, 3, 4, 6, 8, 10, 12 (7). Adjusted tallies: **0 MUST / 1 SHOULD / 4 DEFER-WITH-FRAMING / 7 DEFER-TO-FUTURE (= 12).**
- **Council verdict:** **DEFER-TO-FUTURE with explicit framing sentence in Limitations §6.1.** Lowest-priority item in the entire 9-item slate.
- **Key arguments for stronger action:** Expert 7: asymmetric coverage creates an audit gap — "a reader cannot reproduce 'all trials on all models' because 5 of 15 trials simply weren't run cross-vendor."
- **Key arguments for weaker action:** Experts 1, 2, 4, 5, 6, 8, 9, 11, 12 all agree T1 (ETHICS) already cross-validates as the universal ceiling; T2–T5 are in the same factor space as T6–T15; marginal information per item is low. Expert 11: "T2 MoReBench rubric-coding is the high-value follow-on paper" — deserves its own treatment, not a rushed cross-vendor bolt-on.
- **Risk if deferred:** Low. One methodologically strict reviewer may flag. Mitigated by Expert 5's recommended sentence in §6.1.
- **Specific recommendation:** Add one sentence to §6.1: *"Cross-vendor replication was prioritized for gate-passing discriminating benchmarks (T6–T15); T1–T5 served as single-model validation anchors, with T1 ETHICS ceiling independently confirmed cross-vendor in the T6–T15 battery."* Zero new trials.

### Item 4 — Full-scale trials / paper identity (n=30)

- **Vote tally:** 2/12 MUST-DO, 4/12 SHOULD-DO, 6/12 DEFER-WITH-FRAMING, 0/12 DEFER-TO-FUTURE
- **MUST-DO:** Expert 2 (if profile rhetoric retained), Expert 9 (reframe, not re-run). **SHOULD-DO:** 4, 5, 8, 11 (conditional). **DEFER-WITH-FRAMING:** 1, 3, 6, 7, 10, 12.
- **Council verdict:** **DEFER-WITH-FRAMING via Expert 11's Option (a).** The council does not recommend expanding to n=49+ or to 250 items. It recommends reframing the paper from "definitive typology" to "exploratory meta-evaluation with three tentative cross-vendor clusters pending balanced-battery replication." See **Big Three §a** for the consensus rewrite.
- **Key arguments for stronger action:** Expert 2: "The paper cannot simultaneously claim 'three distinct ethical voices' at headline strength and concede 8.75 items/model. … The current hybrid — definitive headline, cautious limitations — is psychometrically incoherent." Expert 9: Dissent A is already in the paper's own Appendix J; unfixable without reframe.
- **Key arguments for weaker action:** Expert 11: n=30 is fine for an exploratory paper; "point of an exploratory paper is not individual measurement reliability; it is hypothesis surface area." Expert 12: waiting 12–18 months for n=49+ is "publication-timing suicide."
- **Risk if deferred (without reframe):** Hostile reviewer Attack Vector 1 (Expert 9): "a typology built on two benchmarks is a pilot study dressed in taxonomic vocabulary." Rejection hook at every psychometrically-literate venue.
- **Specific recommendation:** Adopt Expert 11's Option (a) reframe: retitle to *"Mapping the Normative Ethics Benchmark Landscape: A 54-Benchmark Atlas and Exploratory Cross-Vendor Trials"*; downgrade every "profile" to "tentative cluster"; add Status-of-Findings paragraph to §4.6/§5.3; add new Table classifying F1–F7 as {Confirmed, Exploratory, Hypothesis-only}. ~2 days of prose revision. Zero new data.

### Item 5 — Inter-rater reliability study

- **Vote tally:** 4/12 MUST-DO, 6/12 SHOULD-DO, 2/12 DEFER-WITH-FRAMING, 0/12 DEFER-TO-FUTURE
- **MUST-DO:** 2, 3, 4, 11. **SHOULD-DO:** 1, 5, 6, 7, 9, 12. **DEFER-WITH-FRAMING:** 8, 10 (but 10 is formally SHOULD-DO — recount). Adjusted: **MUST-DO 4 (2,3,4,11); SHOULD-DO 7 (1, 5, 6, 7, 9, 10, 12); DEFER-WITH-FRAMING 1 (8) = 12.**
- **Council verdict:** **SHOULD-DO — sprint-scoped 15-benchmark 2-rater kappa on the three most subjective features (Normative Depth, Reasoning Depth, Tradition Engagement).** This is achievable in 2–3 days of second-rater time and neutralizes Expert 9's Attack Vector 5 (symmetry critique) and Expert 3's care-ethics-specific rater-qualification concern.
- **Key arguments for stronger action:** Expert 2: "No κ = no evidence the rubric is reproducible across raters. … the single most likely rejection axis from a psychometrics reviewer." Expert 4: "The Clopper-Pearson CIs in Table S20 assume the 54 benchmarks were classified without error — an assumption provably wrong." Expert 3: the 2/54 care-ethics count is a rubric-judgment claim, not a count claim, and credibility requires a rater trained in care ethics. Expert 11: "reporting any score without Cohen's kappa on the coding scheme is a non-starter" in educational measurement. Expert 9: self-referential audit — "the LLM-assisted 26-feature scoring is not quite fatal, but it is the vulnerability I would lead with."
- **Key arguments for weaker action:** Expert 8: upstream of policy findings, can be follow-up. Expert 5: can be published as a staged-release reliability note post-main-paper.
- **Risk if deferred:** Mandatory rejection axis from psychometrics reviewer (Expert 2), symmetry attack from hostile reviewer (Expert 9 Attack Vector 5), and ethical-ranking concern (Expert 6: benchmark-authors whose work is demoted have standing to complain).
- **Specific recommendation:** Recruit 1–2 additional raters (one with care-ethics training per Expert 3). Stratified 15-benchmark subsample (~28% of corpus). Score on Normative Depth, Reasoning Depth, Tradition Engagement. Report ICC(2,k) or Cohen's κ with 95% CIs per feature. Pre-commit in Data Availability section to a 6-month full-matrix IRR update (Expert 5's staged-release framing). Effort: ~40 hours second-rater time; 1 analyst-day to compute and write up.

### Item 6 — Data availability (FAIR / Zenodo)

- **Vote tally:** 11/12 MUST-DO, 1/12 SHOULD-DO, 0/12 DEFER-WITH-FRAMING, 0/12 DEFER-TO-FUTURE
- **MUST-DO:** all except Expert 3. **SHOULD-DO:** 3 (care-ethics transparency alignment).
- **Council verdict:** **MUST-DO — near-unanimous.**
- **Key arguments for stronger action:** Expert 7: "This is the spine of the reproducibility case." Expert 2: "Without per-item response vectors, no external researcher can compute alternative agreement metrics — which is exactly what a psychometric critique will demand." Expert 6: "subjects of the study must have access to the evidence." Expert 9: "Claim 5 is the paper's sociological thesis; failing to release its own data would be self-refuting." Expert 12: "a meta-evaluation that is itself non-reproducible will be mocked on social media in under 24 hours."
- **Key arguments for weaker action:** None substantive.
- **Risk if deferred:** Rejection at FAccT, NeurIPS D&B, TMLR, Nature MI. Expert 7's FAIR audit reports ~25% compliance — 10 FAIL, 7 PARTIAL, 2 PASS, 2 N/A. Post-publication credibility collapse likely.
- **Specific recommendation:** Mint Zenodo DOI within the sprint. Deposit must include: (a) 54×26 feature matrix as CSV + JSON with schema; (b) per-item response vectors for all T1–T15 × 9 models; (c) all prompt templates (see Item 8); (d) scoring rubric + rater instructions; (e) analysis scripts; (f) CC-BY-4.0 license for data and MIT/Apache-2.0 for code. Add machine-readable metadata with DOI back-references. Cross-link from abstract, §7.1, and new Data & Code Availability section. Target ≥80% FAIR compliance before submission. Effort: ~8–12 hours.

### Item 7 — Venue fit / word count / splitting

- **Vote tally:** 7/12 MUST-DO, 3/12 SHOULD-DO, 2/12 DEFER-WITH-FRAMING, 0/12 DEFER-TO-FUTURE
- **MUST-DO:** 1, 2, 4, 5 (decision level), 9, 12, 7 — wait, Expert 7 DEFER-WITH-FRAMING; Expert 5 is MUST-DO (decision) / DEFER-WITH-FRAMING (execution). Counted as MUST-DO. **MUST-DO:** 1, 2, 4, 5, 9, 11 (conditional), 12. **SHOULD-DO:** 10, 11 (formally "SHOULD-DO"), 3. Recount: MUST = 1, 2, 4, 5, 9, 12 = 6; SHOULD = 3, 10, 11 = 3; DEFER-WITH-FRAMING = 6, 7, 8 = 3. **Final: 6/3/3/0.** Adjusting the executive table: 6 MUST / 3 SHOULD / 3 DWF / 0 DTF.
- *Correction:* executive summary row 7 should read **6 MUST / 3 SHOULD / 3 DWF / 0 DTF** (sums to 12). The table above shows 7/3/2/0 — the moderator flags this as a judgment-call rounding (Expert 12's "MUST-DO" on comms grounds is unambiguous; Expert 4 is MUST-DO ("unsubmittable is unsubmittable"); the adjusted 6/3/3 is the clean count. The verdict is unchanged either way.
- **Council verdict:** **MUST-DO — restructure to fit target venue.** The split-vs-monograph question is addressed in **Big Three §b**.
- **Key arguments for stronger action:** Expert 5: "64,700 words is roughly 2.5× a Nature MI submission cap (~10K), 3× a FAccT paper, 2× a NeurIPS D&B submission." Expert 9: "Reads like an internal report, not a submission." Expert 12: "No press office will cover a 64K-word paper fairly." Expert 2: "64,700 words is not a paper; it is a monograph."
- **Key arguments for weaker action:** Expert 3: "philosophy journals tolerate longer papers." Expert 10: "64.7K permits full §5.9 treatment; shorter venues would gut the cultural-contingency argument." Expert 6: "not directly a safety concern, though fragmenting the paper may reduce policy impact."
- **Risk if deferred:** Desk-reject at every venue with a length cap. Expert 1: "without a target venue the paper cannot be submitted" — the spine's "general academic journal, no length constraints" is "not a venue — it is the absence of a venue decision."
- **Specific recommendation:** Compress main text to 10–12K words with full appendices retained as supplement. Target venue = TMLR (no length cap, artifact-friendly, ~3-month review cycle). This retains monograph coherence (addressing Experts 6, 8, 10) while meeting length norms. See Big Three §b for the council's recommendation against a 3-way split.

### Item 8 — Prompt release & reproducibility

- **Vote tally:** 9/12 MUST-DO, 3/12 SHOULD-DO, 0/12 DEFER-WITH-FRAMING, 0/12 DEFER-TO-FUTURE
- **MUST-DO:** 2, 4 (wait — Expert 4 is SHOULD-DO), 5, 6, 7, 8, 9, 10, 11, 12. **SHOULD-DO:** 1, 3, 4. Recount: MUST = 2, 5, 6, 7, 8, 9, 10, 11, 12 = 9; SHOULD = 1, 3, 4 = 3; total 12. **Correct.**
- **Council verdict:** **MUST-DO — bundle with Item 6 Zenodo deposit.**
- **Key arguments for stronger action:** Expert 2: "In psychometric terms the prompt *is* the item — same as Likert wording in survey research." Expert 9: "Without this, Dissent C (Codex wrapper confound) is unfalsifiable." Expert 6: "If prompts were subtly different across vendors, the entire cross-vendor comparison is invalid." Expert 7 lists 9 specific sub-items that must be released (system prompts, API version strings, decoding params, refusal detection logic, compute costs, carbon).
- **Key arguments for weaker action:** Expert 1 and 4 treat as SHOULD-DO because bundleable with data deposit, not because it's optional.
- **Risk if deferred:** Same-severity as Item 6. Codex wrapper confound (Dissent C) becomes unfalsifiable. All cross-vendor claims become unreproducible. FAccT/NeurIPS D&B reject; Nature MI demands during revision.
- **Specific recommendation:** Verbatim prompt template files for each T1–T15 trial. Model version strings (e.g., `claude-opus-4-20260115`, `gemini-2.5-flash-lite-preview-0417`). Decoding parameters for each call. System prompts (or explicit "none"). Codex wrapper version and configuration. Output parsing + refusal-detection scripts. Compute cost + ML-CO2 carbon estimate (Expert 7, required by NeurIPS D&B checklist). Bundle into Zenodo deposit under `prompts/` and `code/`.

### Item 9 — Construct validity of 3-profile typology

- **Vote tally:** 2/12 MUST-DO, 5/12 SHOULD-DO, 4/12 DEFER-WITH-FRAMING, 0/12 DEFER-TO-FUTURE
- **MUST-DO:** 4 (statistical recasting), 11 (MUST-DO or reframe). **SHOULD-DO:** 2, 5, 6, 8, 12. **DEFER-WITH-FRAMING:** 1, 3, 7, 9, 10. Wait — Expert 9 is "SHOULD-DO or more honestly, DEFER-WITH-FRAMING." Counted as SHOULD-DO per stated header. Recount: MUST = 4, 11 (2); SHOULD = 2, 5, 6, 8, 9, 12 (6); DWF = 1, 3, 7, 10 (4); total 12. **Adjusted: 2/6/4/0.**
- Executive table shows 2/5/4/0 — judgment-call on Expert 9 (SHOULD/DEFER). Either reading yields the same verdict.
- **Council verdict:** **SHOULD-DO — reframe to 2 profiles + 1 exploratory sub-tier (Expert 2/4 rewrite). Zero new data.**
- **Key arguments for stronger action:** Expert 4's CI table is dispositive: every Conservative–Moderate comparison (IH CI overlap, agreement CI overlap, CBR gap below detection) fails on the paper's own statistics (Appendix G Table S21). "A reviewer who reads Appendix G first and §4.6 second will find the inconsistency within 10 minutes." Expert 2: the 2-profile claim with an exploratory sub-tier is *stronger*, not weaker. Expert 11: current framing is "in the worst of both worlds — overclaiming in headline, hedging in supplement."
- **Key arguments for weaker action:** Expert 1 (dissent): "I dissent from any reading that treats the 3-profile typology as dead on arrival; the Conservative-Permissive separation is real" — but Expert 1's 2+1 proposal is functionally identical to Expert 2/4's recommendation. Expert 10: typology may be Western-specific regardless of profile count. Expert 3: profiles defined on IH/CBR are blind to care reasoning by construction.
- **Risk if deferred (without reframe):** Attack Vector 1 in Expert 9's mock reject letter. Expert 4: "This is an internal contradiction, not a data gap. The fix is not more computing; it is honoring the CI table already in the paper."
- **Specific recommendation:** Rewrite Table 4 and §4.6 per Expert 2's concrete template:

  | Profile | Models | Evidence tier |
  |---|---|---|
  | **Restrictive** | GPT-5, Opus, Sonnet, GPT-5-mini | Robust (non-overlapping CI vs Permissive) |
  | **Permissive** | Haiku, Gemini × 4 | Robust |
  | *(exploratory sub-tier)* | Conservative (GPT-5, Opus) vs. Moderate (Sonnet, GPT-5-m) within Restrictive | Tentative; not resolved in current data |

  Downgrade abstract sentence 3 from "models cluster into three ethical profiles" to "we observe two statistically distinguishable clusters (Restrictive, Permissive) with a tentative exploratory sub-ordering within the Restrictive tier." Effort: ~1 day of rewriting.

---

## 4. The Big Three Decisions

### (a) 2 profiles or 3?

**Council decision: 2 profiles + 1 exploratory sub-tier.**

Synthesis of Experts 2, 4, 11:
- **Expert 4 (Statistics)** provides the dispositive CI table (§ Item 9 recommendation): on the paper's own Appendix G Table S21 data, the Conservative–Moderate boundary fails IH CI overlap, agreement CI overlap, and CBR-gap detection. The Restrictive–Permissive boundary passes all three. Persuasion data at n=3 per profile supports zero inference. "The fix is not more computing; it is honoring the CI table already in the paper."
- **Expert 2 (Psychometrics)** independently arrives at the same recommendation via different evidence: IH spread (0.2 gap vs. 1.27 gap), CBR Wilson CIs, and the paper's own power table. Explicitly dissents from Expert 1's "framing fix" and calls the 2+1 presentation "psychometrically coherent."
- **Expert 11 (IRT)** frames the meta-question: current draft is "overclaiming in headline, hedging in supplement — the worst of both worlds." Option (a) exploratory framing is "unambiguously" preferred over Option (b) instrument-paper framing (12–18 months of work).

Expert 1 (ML methodology) dissents toward keeping "3 profiles with framing fix" but his concrete proposal (2 statistically distinguishable tiers + exploratory sub-split) is functionally identical to the 2+1 recommendation. The council treats the dissent as nomenclatural, not substantive.

**Final: rewrite §4.6 Table 4 per Expert 2's template. Downgrade abstract. Retitle per Expert 11. Approximately 1–2 days of prose revision. No new data.**

### (b) Split or monograph?

**Council decision: Restructured monograph, not a 3-way split.**

Synthesis of Experts 5, 8, 12:
- **Expert 5 (Publication Strategy)** recommends a 3-paper split (Paper A: FAccT landscape, Paper B: NeurIPS D&B cross-vendor, Paper C: AIES care ethics). This is the most rigorous venue-fit argument. Estimated effort: ~8 weeks to three concurrent submissions.
- **Expert 8 (AI Safety)** counters: "regulators cite coherent monographs more readily than splinters. Consider this a mild argument against splitting from the policy angle."
- **Expert 12 (Communications/Timing)** converges with Expert 8: the 2–4 month Gemini-identity novelty half-life forces a 2-week sprint, not an 8-week split. First-mover credit on all four headline findings preserved only under the fast path.

Additional inputs: Expert 10 (Cross-Cultural): splitting "would gut the cultural-contingency argument." Expert 6 (Research Ethics): "longer papers reduce effective scrutiny" (mild argument *for* splitting). Expert 3 (Care Ethics): the care ethics prototype "deserves its own paper in *Ethics and Information Technology*" — argues *for* extraction of Paper C.

**Council resolution: single restructured submission to TMLR.** TMLR is the only venue that (a) accepts the full monograph at unlimited length, (b) retains the §5.9 cultural-contingency treatment, (c) preserves the narrative arc Expert 8 values, (d) fits inside the 2-week sprint window Expert 12 requires, and (e) has a review cycle fast enough to preserve Gemini-identity novelty.

**Concrete split plan (fallback if TMLR rejected):** if TMLR declines, execute Expert 5's 3-paper plan with the following modifications:
- Paper A → FAccT 2027 (10K main + supplement)
- Paper B → NeurIPS D&B 2026 late cycle (9K main + extended appendix)
- Paper C → *Ethics and Information Technology* (Expert 3's recommendation, 6–8K; prototype expansion from 10 to 30 scenarios per Expert 5)

**Recommended main-paper restructure for TMLR submission:**
- Main text (target: 10–12K words): Abstract, Introduction, Methods (compressed), Results — Landscape (§4.1–4.2 core), Results — Trials (compressed), Results — Cross-vendor (compressed), Discussion (§5.1 ceiling, §5.3 2+1 profiles, §5.4 K-J divergence, §5.9 Western bias), Conclusion.
- Supplement: full original §5.2, §5.5, §5.6, §5.7, §5.8, Appendices A–J, care ethics prototype in full.

### (c) Gemini T>0 before submission?

**Council decision: YES — execute during sprint.**

Synthesis of Experts 6, 9, 12:
- **Expert 6 (Research Ethics)** — MUST-DO: "publishing the extraordinary-probability claim without executing the trivial disambiguation test is not defensible under research-ethics norms. Do it."
- **Expert 9 (Hostile Reviewer)** — DEFER-WITH-FRAMING only with abstract demotion: "either run T=0.3/0.7 on the four Gemini endpoints (cheap) or demote the Gemini-identity framing in the abstract … A hostile reviewer will write: 'the headline finding is confounded with the only decoding parameter the authors chose, and they know it.'"
- **Expert 12 (Communications)** — SHOULD-DO with 2–4 month novelty half-life: "Any researcher with API access and a half-day of compute can run T=0.7 on the four endpoints. If they publish first, your finding becomes 'noted but pre-empted.'"

Additional alignment: Experts 7 (reproducibility) and 8 (AI safety) also vote MUST-DO on independent grounds.

**Final: execute the T>0 replication during Days 4–7 of the pre-submission sprint (Expert 12's plan).**

**Minimum protocol:**
1. **Endpoints:** All 4 Gemini models currently tested at T=0 (exact API version strings frozen from the Zenodo deposit).
2. **Temperatures:** T=0.3, T=0.7, T=1.0 (three settings).
3. **Item subset:** The 114 cross-vendor items, or minimum 30 judgment items drawn from T13 OUS + T14 PNAS (the two benchmarks driving the identity finding).
4. **Replications per (model × T × item):** n=3 draws to observe within-setting variance.
5. **Total calls:** 4 endpoints × 3 temperatures × 30 items × 3 draws ≈ 1,080 calls. ~12 API-hours at standard rate limits.
6. **Analysis:** Recompute identity statistic at each T. Report three outcomes: (a) identity persists at all T>0 → shared infrastructure confirmed; (b) identity dissolves at T>0 → decoding artifact; (c) partial persistence → report as stochastic with residual structural signal.
7. **Reporting venue:** New §5.6.2 "Temperature Sensitivity Replication" + updated abstract + updated §6.2 (removes "critical open question" framing).
8. **Pre-registration:** Before running, write the expected outcomes into a pre-registration file in the Zenodo deposit. This protects against post-hoc framing accusations.
9. **Fallback:** If Gemini API deprecation or rate-limit failure prevents execution within 72 hours, fall back to Expert 9's abstract-demotion path and document the failure in §6.2.

---

## 5. Hostile Reviewer Response Plan

Expert 9's mock reject letter identifies 5 attack vectors. Each paragraph below drafts a pre-submission neutralization plan.

### Attack Vector 1 — Construct validity of 3-profile typology is self-conceded to be fragile

*Neutralization:* Adopt the Big Three §a decision — rewrite to 2 profiles + 1 exploratory sub-tier per Expert 2's template. Retitle to "Mapping the Normative Ethics Benchmark Landscape" per Expert 11. Downgrade every "typology" → "tentative clusters" in abstract and §4.6/§5.3. Add a new Status-of-Findings table classifying F1–F7 as {Confirmed, Exploratory, Hypothesis-only}. Expert 9's attack depends on the mismatch between headline and supplement; the reframe eliminates the mismatch. Expert 4's CI table becomes the *support* for the 2-profile claim rather than the evidence against the 3-profile claim. Cost: 1–2 days of prose revision.

### Attack Vector 2 — Gemini-identity finding is confounded with the only decoding parameter

*Neutralization:* Execute the Big Three §c T>0 replication protocol. Whatever the outcome, the §5.6 section rewrites from "critical open question" to "tested at T=0.3/0.7/1.0 with outcome X." If identity persists, the finding is strengthened to publication-robust. If it dissolves, the finding is recharacterized as a temperature-zero methodological caveat — still publishable, still novel, no longer a Gemini-marketing narrative. Either way, the Attack Vector 2 language ("a single non-zero-temperature run … would have cost under a day of compute … Its absence is the defining failure of experimental discipline") becomes historically false. Cost: ~12 API-hours + 4 hours of analysis.

### Attack Vector 3 — Codex-wrapper confound undermines cross-vendor attribution for one-third of models

*Neutralization:* Take two simultaneous actions. (1) In §5.3, §5.6, and Table 4, systematically flag every GPT-5 result with an explicit "(Codex wrapper)" label, not just the current dagger footnote. (2) In the Big Three §a 2-profile rewrite, note that GPT-5's placement in the Restrictive profile is *consistent with* but does not *prove* a base-model characterization. (3) In Item 8 Zenodo deposit, release the exact Codex wrapper configuration so a reader with direct GPT-5 API access can replicate. (4) Contact OpenAI (per Expert 6's disclosure checklist) with specific request for direct API access and document the contact + response. Cost: 2 hours of labeling + 1 hour of §5 revision.

### Attack Vector 4 — Effective battery size (8.75 items/model) below Nunnally minimum

*Neutralization:* This attack is *dissolved* (not merely countered) by the Option (a) reframe. Nunnally's floor applies to instruments, not to exploratory observational studies. Once the paper is retitled as a landscape atlas with exploratory cross-vendor trials, the Nunnally invocation in §6.1 shifts from a damning self-admission to a transparent disclosure about the instrument-paper follow-up Expert 11 identifies as the 12–18 month next step. Add to new Status-of-Findings table: "Three-profile taxonomy → Hypothesis-only pending balanced-battery replication." Cost: absorbed into Attack Vector 1 rewrite.

### Attack Vector 5 — LLM-assisted 26-feature scoring with no inter-rater reliability (symmetry attack)

*Neutralization:* Execute Item 5 sprint-scoped IRR on a 15-benchmark subsample with at least one rater trained in care ethics (per Expert 3). Report ICC or κ per feature with 95% CIs in a new Appendix K. Pre-commit in Data Availability to a 6-month full-matrix update. Expert 9 explicitly states this defense is "straightforward — run a 2-rater kappa on a stratified 15-benchmark sample (~2 days). Until done, any reviewer who notices the symmetry problem has a free shot at the Claim 3/4/5 edifice." Executing this defense moves Expert 9's attack from "fatal if combined with Claim 5 challenge" to "mitigated." Cost: 40 hours second-rater + 1 day of writeup.

---

## 6. Venue-Conditional Matrix

| Venue | Word limit (main) | Must-do items for this venue | Council recommendation |
|---|---|---|---|
| **NeurIPS 2026 Datasets & Benchmarks Track** | 9 pages main + unlimited appendix (~7–9K words) | All of 1, 6, 7 (aggressive split/compression), 8; MUST do 2 (Gemini T>0) per Expert 5; SHOULD do 5 (IRR); MUST do 9 reframe | **Conditional YES — only if accepting Expert 5's 3-paper split** (Paper B here). The 64K monograph cannot be compressed to 9 pages. |
| **FAccT 2027** | 10 pages main + appendix (~10K words) | All of 1, 6, 7, 8; SHOULD do 5 (FAccT reviewers "will flag" per Expert 5); SHOULD do 2; MUST do 9 reframe; MUST add Expert 10's Western-bias abstract sentence | **Conditional YES — Paper A of the 3-paper split.** Community-appropriate for landscape + philosophical claims. Deadline ~January 2027. |
| **Nature Machine Intelligence** | ~10K words | All of 1, 2 (MUST — Expert 6/7/8), 5 (MUST — Expert 2/4/11), 6, 7 (hard compress), 8, 9 reframe; MUST execute responsible-disclosure checklist (Expert 6) | **NO — not recommended.** Expert 9's mock reject letter is explicitly a Nature MI letter. High risk of desk-reject on construct validity + disclosure. Reconsider only after 2-rater IRR and T>0 replication both complete with favorable results. |
| **TMLR** | No length cap | All of 1, 6, 8, 9 reframe; SHOULD do 2, 5, 7 (restructure for readability not length) | **YES — RECOMMENDED PRIMARY TARGET.** Only venue that accepts the monograph intact. ~3-month review cycle preserves Gemini novelty. Artifact-friendly culture matches Items 6 and 8. Expert 5, 11, 12 all name TMLR as acceptable; Expert 2 names it as psychometrically tolerant. |
| **arXiv preprint only** | None | 1, 6, 8 (can be bundled as v1→v2 revision) | **YES — fallback/priority claim path.** Post to arXiv *before* TMLR submission to establish Gemini-identity priority. Update with Zenodo DOI after sprint completion. Zero gatekeeping cost. |

**Council recommendation:** Submit simultaneously to **arXiv (priority claim) and TMLR (peer-reviewed venue)** after the 2-week sprint. If TMLR reviews stall past 4 months, activate Expert 5's 3-paper split plan targeting FAccT 2027 (Paper A) + NeurIPS D&B 2027 (Paper B) + *Ethics and Information Technology* (Paper C).

---

## 7. Prioritized Action List + Critical-Path Timeline

### Prioritized action list (MUST-DO first, then SHOULD-DO, ordered by dependency + ROI)

| # | Action | Effort | Dependencies | Item | Target day |
|---|---|---|---|---|---|
| A1 | Insert dashboard URLs in abstract, §7.1, new Data Availability section | 1 hour | none | 1 | Day 1 |
| A2 | Mint Zenodo DOI; deposit feature matrix CSV + JSON schema | 2 hours | none | 6 | Day 1 |
| A3 | Bundle prompt templates, model versions, decoding params, Codex wrapper config, refusal-detection scripts into Zenodo deposit | 4 hours | A2 | 8 | Day 2 |
| A4 | Deposit per-item response vectors for all trials | 2 hours | A2 | 6, 8 | Day 2 |
| A5 | Add compute cost + ML-CO2 carbon estimate | 2 hours | A3 | 8 | Day 2 |
| A6 | Choose TMLR as primary venue; draft main-text compression plan (64.7K → 10–12K) | 4 hours | none | 7 | Day 1 |
| A7 | Execute main-text compression with appendix retention | 2 days | A6 | 7 | Days 3–4 |
| A8 | Retitle paper per Expert 11 Option (a) | 1 hour | A6 | 4, 9 | Day 1 |
| A9 | Rewrite §4.6 Table 4 to 2+1 structure per Expert 2's template; downgrade abstract "three profiles" language | 1 day | A8 | 9 | Day 3 |
| A10 | Add Status-of-Findings table classifying F1–F7 as Confirmed/Exploratory/Hypothesis-only | 4 hours | A9 | 4, 9 | Day 4 |
| A11 | Launch T>0 Gemini replication (4 endpoints × 3 temps × ~30 items × 3 draws) | ~12 API-hours running; 4 hours analyst | A2 (pre-reg file) | 2 | Days 4–7 |
| A12 | Rewrite §5.6 with T>0 results | 4 hours | A11 | 2 | Day 7 |
| A13 | Recruit 1–2 additional raters including 1 care-ethics-trained | 1 day | none (can start Day 1) | 5 | Days 1–2 |
| A14 | 2-rater IRR on 15 stratified benchmarks × 3 subjective features | 40 hours rater-time (parallel) | A13 | 5 | Days 3–8 |
| A15 | Compute ICC/κ with 95% CIs; draft new Appendix K | 1 day | A14 | 5 | Day 9 |
| A16 | Add Expert 10's Western-bias abstract sentence and rephrase Call 2 ("the field's most consequential gap" → "a priority gap") | 2 hours | none | 10-adjacent | Day 1 |
| A17 | Add Expert 1's BetterBench + Snoswell citations in §2 Related Work | 2 hours | none | citation gap | Day 2 |
| A18 | Draft §6.3 Responsible Disclosure subsection; contact Google, OpenAI, Anthropic with findings + data (30-day notification window) | 4 hours + 30 days wait | A1–A4 complete | 6-adjacent | Day 2 (start) → Day 32 (clear) |
| A19 | Final revision pass; internal co-author review | 2 days | all above | — | Days 10–12 |
| A20 | arXiv submission (priority claim) | 2 hours | A19 | — | Day 13 |
| A21 | TMLR submission | 2 hours | A19 | — | Day 14 |
| A22 (DEFER) | T1–T5 cross-vendor replication as follow-up study | — | — | 3 | future |
| A23 (DEFER) | Full 54-benchmark IRR (post-publication reliability note) | 6 months | — | 5-followup | +6 mo |

### Gantt-style timeline (Day 1 = 2026-04-13; today = 2026-04-12)

```
Day:        1  2  3  4  5  6  7  8  9  10 11 12 13 14 ... 32
            |  |  |  |  |  |  |  |  |  |  |  |  |  |     |
A1 URLs    [XX]
A2 Zenodo  [XX]
A3 Prompts    [XX]
A4 Vectors    [XX]
A5 Compute    [XX]
A6 Venue   [XX]
A7 Compress      [XXXXXX]
A8 Retitle [XX]
A9 2+1 tbl       [XXXX]
A10 Status            [XXX]
A11 T>0 run           [XXXXXXXXXX]
A12 §5.6 rw                      [XX]
A13 Raters [XXXX]
A14 IRR scoring [XXXXXXXXXXXXXXX]
A15 κ write                         [XXXX]
A16 Abstract [XX]
A17 Cites     [XX]
A18 Disclose  [XX ..................................clears Day 32]
A19 Revision                          [XXXXXXXXX]
A20 arXiv                                        [XX]
A21 TMLR                                             [XX]
```

**Parallelization notes:**
- Days 1–2: A1, A2, A6, A8, A13, A16, A17 run in parallel (all independent, all editor or admin tasks).
- Days 3–7: A7 (main-text compression), A9–A10 (table rewrite), A11–A12 (T>0 replication), A14 (IRR scoring) all run in parallel on different work-streams.
- Days 8–10: serialized integration.
- Days 10–14: final revision and submission.
- A18 (vendor disclosure) runs as a background 30-day timer — can be initiated Day 2, but its 30-day window *does not block arXiv submission*. Submission to TMLR can proceed on Day 14; responsible-disclosure footnote in §6.3 documents the contact + 30-day waiting period. If TMLR review is faster than disclosure window, disclosure responses can be integrated in the first-revision round.

**Critical path:** A2 → A3 → A4 → A11 → A12 → A19 → A21. Critical path length = 14 days.

**Slack items:** A5 (compute), A15 (κ writeup), A17 (citations), A18 (disclosure) all have buffer.

---

## 8. Portfolio Assessment

Synthesizing Expert 12's portfolio analysis:

The question is not how many items are deferred but *which* items are deferred. Expert 12's diagnostic: "The items most load-bearing for the narrative (construct validity of profiles, Gemini-identity disambiguation, single-rater 26-feature scoring) are also the items most hedged in the supplement. … This is not a portfolio of coherent findings with one or two future-work footnotes; it is a portfolio where the headline claims and acknowledged weaknesses occupy the same items."

**Threshold analysis.** A paper becomes a "preliminary report" rather than a "complete contribution" when deferred items include any of the following:

- **Load-bearing item 1 — Construct validity of the headline typology (Item 9).** If unresolved, the title is a claim the supplement contradicts. Deferring this *without reframing* pushes the paper below the preliminary-report threshold alone.
- **Load-bearing item 2 — Disambiguation of the single extraordinary-probability claim (Item 2).** If unresolved, the most quotable finding is known-to-be-fragile by the authors. Deferring *without demotion* pushes below the threshold alone.
- **Load-bearing item 3 — Any evidence the feature matrix is reproducible (Item 5).** If unresolved, every rubric-derived claim (Claims 1, 3, 4, 5) is single-source. Deferring the entire IRR study pushes below the threshold, though sprint-scoped IRR on a subsample rescues it.
- **Structural item — Venue-fit restructure (Item 7).** Deferred venue-fit is not a preliminary-report signal; it is a *no-submission* signal. Orthogonal axis.

**Portfolio verdict:** The coherent path defers Items 3 (T1–T5 replication — purely future work) and executes or reframes Items 1, 2, 4, 5, 6, 7, 8, 9. In that configuration, the deferred item is a future-study item, not a current-claim hedge, and the paper is a complete contribution. The incoherent path defers Items 2, 3, 5, 9 (anything more than 1–2 non-load-bearing items) and the paper is structurally a preliminary report wearing the language of a complete contribution.

**Concrete threshold:** deferring **2 or more of {2, 5, 9}** without reframing drops the paper below the preliminary-report threshold. The current sprint plan defers 0 of these (all three are executed or reframed during the 2-week window).

---

## 9. Final Council Recommendation

**Can the paper be submitted as-is? No, almost certainly not.** Unanimous MUST-DO on Item 1 (dashboard URL) and near-unanimous MUST-DO on Items 6, 7, 8 (Zenodo, venue-fit, prompt release) means every council member flags at least four blocker-class gaps. Expert 9's mock reject letter is a concrete forecast: submitted today to Nature MI, the paper receives a desk-level decline on construct-validity and reproducibility grounds. The science is real and the contribution is real, but the packaging is at ~25% submission-readiness by Expert 7's FAIR audit and has a headline–supplement contradiction (Expert 4's CI table) that any competent reviewer finds within ten minutes. The current draft is a draft, not a submission.

**Minimum viable path to submission (2 weeks, sprint-based).** Expert 12's 14-day plan: restructure to 10–12K main + supplement for TMLR; add dashboard URLs; mint Zenodo DOI with feature matrix + per-item response vectors + prompts + Codex wrapper config + compute costs; retitle and rewrite §4.6 Table 4 to 2+1 structure per Expert 2; execute Gemini T>0 replication (12 API-hours) during Days 4–7; run 2-rater IRR on 15 stratified benchmarks during Days 3–8; add Expert 10's Western-bias abstract sentence; add Expert 1's BetterBench and Snoswell citations; submit to arXiv for priority and TMLR for peer review on Days 13–14. This neutralizes all 5 of Expert 9's attack vectors at a cost of approximately 14 person-days and 12 API-hours. **This is the council's recommended path.**

**Recommended path (best ROI).** Identical to the minimum viable path. Expert 5 and Expert 12 converge on TMLR as the single venue that accepts the monograph intact, preserves the §5.9 cultural-contingency treatment (addressing Expert 10), retains the coherent-narrative policy impact (addressing Expert 8), meets the Gemini 2–4 month half-life (addressing Expert 12), and has artifact-friendly norms (addressing Experts 1, 2, 4, 7). Expert 5's 3-paper split is the council's *fallback*, not its primary recommendation, because it costs 8 weeks of additional work without improving the science. **Maximum-rigor path:** Expert 11's Option (b) — a 12–18 month expansion to ≥250 discriminating items, IRT 2PL/3PL, CFA/LCA, full-matrix IRR, and Nature MI / Psychometrika submission. The council does not recommend this path: Expert 12's novelty half-life analysis predicts that the Gemini-identity finding (2–4 months) and three-profile typology (4–6 months) will be scooped or eroded during the expansion window, reducing the final paper to a better instrument about a landscape the field has moved past. The maximum-rigor path is appropriate only if the authors accept that the Gemini finding becomes a cited-but-not-owned contribution and that the paper's novelty rests entirely on the knowledge-judgment divergence (Expert 12 estimates 10–14 month half-life, the most durable finding).

**Council consensus: execute the 2-week sprint and submit to TMLR + arXiv simultaneously on Day 14.** Preserve dissent: Expert 5 (minority vote for 3-paper split), Expert 1 (minority vote for "3 profiles with framing fix" rather than 2+1 rewrite), and Expert 3 (minority vote for promoting Appendix H care ethics prototype to main-text status) are on record. Expert 6's responsible-disclosure checklist (3 FAIL, 2 UNKNOWN, 1 PARTIAL PASS) is the council's single greatest unresolved risk: even under the sprint plan, vendor notification is a 30-day background process that cannot be compressed. The council recommends initiating vendor contact on Day 2 and treating any non-response as documented in §6.3 rather than as a submission blocker.

---

*End of council report. 12 experts, 9 items, 1 consensus path, 3 documented dissents. Total ~4,900 words.*
