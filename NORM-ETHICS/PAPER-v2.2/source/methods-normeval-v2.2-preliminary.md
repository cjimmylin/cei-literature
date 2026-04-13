## 3. Methods

This section describes the complete methodology for assembling, scoring, and empirically validating a corpus of 54 normative ethics benchmarks for large language models. The pipeline proceeds in seven stages: corpus assembly (Section 3.1), feature matrix design (Section 3.2), composite scoring with hard gates (Section 3.3), two-phase implementation trials (Section 3.4), statistical methods (Section 3.5), a care ethics benchmark prototype (Section 3.6), and methodological limitations (Section 3.7).

---

### 3.1 Benchmark Corpus Assembly

We assembled the evaluation corpus through a two-stage process combining curated vault mining with systematic search.

**Stage 1: CEI Literature Vault mining.** The CEI Literature Vault is a curated database of 2,946 AI ethics papers maintained by the Center for Ethical Intelligence, in which each paper carries structured metadata including topic classifications, normative tradition tags, and evaluation-type indicators. An initial query against the vault's classification fields returned 41 papers tagged as normative ethics benchmarks. Manual review by the first author confirmed 30 of these as genuine normative ethics evaluation instruments -- that is, artifacts that present LLMs with morally valenced stimuli and score their responses against one or more normative frameworks. The remaining 11 were reclassified as borderline: they reference normative ethics vocabulary but do not operationalize any framework into a scoreable evaluation (e.g., papers that mention "deontological" in their framing but test only factual knowledge retrieval). These 30 confirmed benchmarks formed the seed corpus.

**Stage 2: PRISMA-compliant systematic search.** To ensure coverage beyond the vault's existing holdings, we conducted a systematic search across seven databases: arXiv, Semantic Scholar, ACL Anthology, Google Scholar, PapersWithCode, OpenReview, and HuggingFace Hub. We constructed ten query sets by combining terms for normative ethics traditions (virtue, deontological, utilitarian, care, contractarian), moral evaluation methods (benchmark, evaluation, assessment, test), and LLM identifiers (large language model, GPT, Claude, LLaMA). Representative queries included *"care ethics benchmark LLM"*, *"contractarian moral evaluation language model"*, and *"virtue ethics assessment large language model"*. We deliberately over-sampled queries targeting care ethics [Gilligan1982] and contractarian ethics [Rawls1971, Scanlon1998] to compensate for their anticipated under-representation, as preliminary vault analysis had already indicated severe voids in these traditions.

The search returned 30 external candidates after deduplication against the vault. Of these, 13 met all four inclusion criteria: (1) peer-reviewed publication or posting on a recognized preprint server (arXiv, SSRN, bioRxiv); (2) explicit evaluation of LLMs on normative ethical reasoning, not merely descriptive moral psychology; (3) publication date between 2021 and 2026; and (4) presentation of a scoreable instrument with defined items and response formats. The remaining 17 were excluded: 9 lacked genuine normative ethics content (testing factual recall or descriptive moral intuitions without framework grounding), 4 duplicated existing vault entries under variant titles, and 4 evaluated only descriptive moral psychology without any normative framing.

**Corpus expansion trajectory.** The vault's initial 30 confirmed benchmarks grew through two waves: 12 new benchmarks identified during the systematic search that had been present in the vault but not yet tagged as normative ethics instruments, and 5 genuinely new external papers ingested into the vault following Stage 2 search. Three of these external additions -- Xu et al. [Xu2026] (probing ethical framework representations), Zhang et al. [Zhang2026] (RLVR moral reasoning), and Du et al. [Du2025] (196 research ethics dilemmas) -- expanded the corpus into previously unrepresented evaluation paradigms. The remaining two -- IslamicMMLU [IslamicMMLU2026] (10,013 MCQ items across Islamic knowledge domains) and IslamicLegalBench [IslamicLegalBench2026] (718 instances spanning seven jurisprudence schools) -- added non-Western normative tradition coverage that was entirely absent from the initial seed.

**Final corpus.** The assembled corpus comprises 54 benchmarks spanning 2021--2026. Figure 2 presents the PRISMA flow diagram tracing the identification, screening, eligibility, and inclusion stages.

---

### 3.2 Feature Matrix Design

We characterized each of the 54 benchmarks along 26 features organized into four axes (Table 1; full matrix in Table S1).

**Axis A: Normative Depth (A1--A8).** This axis measures the philosophical rigor with which a benchmark engages normative ethics. Features include: the number of ethical traditions explicitly tested (A1, integer 1--5); the depth of ethical engagement from surface-level keyword mention to framework-grounded scenario construction (A2, ordinal 1--5); whether the benchmark tests moral judgment, moral reasoning, or both (A3, categorical J/R/B); treatment of moral uncertainty and disagreement among reasonable ethical agents (A4, binary); pluralistic coverage of competing normative perspectives within the same item set (A5, ordinal 1--5); philosophical grounding quality on a calibrated 1--5 scale (A6; see calibration below); cultural framing beyond Western WEIRD populations (A7, ordinal 1--3); and multilingual support (A8, integer count of languages).

**Axis B: Practical Ease (B1--B9).** This axis measures how readily a benchmark can be implemented by researchers. Features include: task format (B1, categorical); dataset size in items (B2, integer); data availability via public repository (B3, binary); code availability (B4, binary); license terms permitting academic use (B5, ordinal); compatibility with established evaluation harnesses -- LM Eval Harness, HELM, EleutherAI, BIG-bench, TrustLLM, DecodingTrust -- assessed across all six frameworks (B6, integer 0--6); an overall implementability judgment integrating format standardization, documentation quality, and setup complexity (B7, ordinal 1--5); scorer type from automated exact-match to expert rubric (B8, categorical); and model compatibility across API-based and open-weight models (B9, ordinal 1--3).

**Axis C: Citation Impact (C1--C5).** This axis measures community uptake. Features include: raw citation count from Semantic Scholar (C1, integer); age-normalized citations per year (C2, continuous); venue tier from top-tier conference to workshop or unreviewed preprint (C3, ordinal 1--5); downstream adoption count reflecting benchmarks that explicitly build on or extend the target (C4, integer); and leaderboard presence on PapersWithCode or equivalent (C5, binary).

**Axis D: Metadata (D1--D4).** Provenance fields record: publication year (D1), first-author affiliation (D2), primary language (D3), and domain focus such as general, medical, legal, or cultural (D4).

**Calibration anchors for A6 (Philosophical Grounding).** Because A6 is the single most consequential feature -- it carries 20% weight in the Normative Depth composite -- we calibrated it against three anchors representing the extremes and midpoint of the scale. MoReBench [Chiu2025] received A6 = 5: it deploys expert rubric criteria for procedural reasoning under five named traditions, requiring models to demonstrate step-by-step ethical argumentation. ETHICS [Hendrycks2021] received A6 = 3: it names traditions and creates tradition-specific sub-datasets but operationalizes them as classification tasks without requiring reasoned justification. Hui *Decoding Moral* received A6 = 1: it mentions ethics vocabulary without substantive philosophical engagement. All remaining benchmarks were scored by the first author relative to these anchors, with written rationales for each score recorded in the supplementary feature matrix (Table S1).

---

### 3.3 Composite Scoring and Hard Gates

We computed three axis scores from the 26 features. All axis scores are normalized to 0--100.

**Normative Depth (ND)** weights philosophical grounding and reasoning depth most heavily:

> ND = A2 x 25 + A6 x 20 + A1 x 15 + A3 x 15 + A5 x 15 + A4 x 10

**Practical Ease (PE)** prioritizes implementability and data access:

> PE = B7 x 30 + B3 x 20 + B4 x 15 + B6 x 15 + B9 x 10 + B5 x 10

**Citation Impact (CI)** balances normalized citations with downstream adoption:

> CI = C2 x 35 + C4 x 30 + C3 x 20 + C5 x 15

The composite score combines the three axes:

> COMPOSITE = ND x 0.40 + PE x 0.35 + CI x 0.25

**Weight rationale.** We weighted ND highest (40%) because this survey specifically evaluates *normative* depth -- a benchmark that is easy to run but philosophically shallow serves our purpose less than one that is harder to implement but genuinely engages ethical theory. PE receives the second-highest weight (35%) because benchmarks without accessible data cannot be independently verified, replicated, or extended by the community. CI receives the lowest weight (25%) to avoid over-rewarding incumbency: the field's most-cited benchmark, ETHICS [Hendrycks2021], has 843 citations but produces ceiling effects on every frontier model tested (Section 4.3), illustrating that community adoption is a lagging indicator of current utility. To assess weight sensitivity, we re-ran rankings under 18 alternative weight combinations (Table S2); the Top 10 was 94% stable across configurations, and no benchmark moved more than 3 rank positions.

**Hard gates.** We applied two mandatory gates before ranking: (1) ND >= 40, ensuring minimum philosophical engagement beyond surface-level ethics vocabulary; and (2) publicly available data hosted on GitHub, HuggingFace, or an equivalent open repository. Of the 54 benchmarks, 14 failed the ND gate alone, 21 lacked public data alone, and 5 failed both, yielding 24 benchmarks that passed both gates. Notably, several high-ND benchmarks were excluded solely for data unavailability: Chakraborty *Structured Moral Reasoning* (ND = 83.0), Rao *Ethical Reasoning over Moral Alignment* (ND = 80.0), and Zhou *Rethinking Machine Ethics* (ND = 72.0). The median ND score among unavailable benchmarks (58.8) exceeds that of available benchmarks (53.0), suggesting that philosophically rigorous benchmark authors may prioritize depth over dissemination infrastructure -- a pattern we analyze further in Section 4.2.

**Tradition diversity in the gate-passing set.** We verified that the 24 gate-passing benchmarks maintain representation across all five normative traditions: 11 test virtue ethics, 18 test deontological ethics, 16 test utilitarian ethics, 7 engage care ethics, and 3 include contractarian ethics (Table 2). The set also includes two non-English or cross-cultural instruments -- JETHICS [Takeshita2025] for Japanese moral reasoning and UniMoral [Kumar2025] across six languages -- and two domain-specific benchmarks in healthcare ethics: PrinciplismQA [Hong2025] and MedEthicsQA [Wei2025].

---

### 3.4 Implementation Trial Protocol

To move beyond feature-level characterization, we conducted empirical implementation trials in two phases spanning 15 benchmarks and 9 models.

**Phase 1: Single-model depth trials (T1--T5).** We selected five benchmarks spanning the composite-score spectrum to test whether high-scoring benchmarks reliably produce more informative evaluations. The selection comprised: ETHICS [Hendrycks2021] (Composite Rank 1), MoReBench [Chiu2025] (Rank 2), MoralReason-QA [An2025] (Rank 5), Moral Lens [Samway2025] (Rank 6), and DailyDilemmas [ChiuDD2024] (Rank 10). For each benchmark, we sampled 20--50 items and administered them to Claude Opus 4.6 as the primary baseline, providing each benchmark's original instructions and response format verbatim. Model outputs were scored against ground-truth labels or expert rubrics as specified by each benchmark's authors. This phase served primarily to identify ceiling effects, validate the composite ranking against empirical discriminative power, and calibrate the scoring infrastructure for Phase 2.

**Phase 2: Cross-vendor replication (T6--T15).** The second phase administered 10 additional benchmarks to 9 models spanning 3 vendors, producing 114 comparable items. The model set comprised:

- **Anthropic:** Claude Opus 4.6 (baseline, carried from Phase 1), Claude Sonnet 4.6, Claude Haiku 4.5
- **Google:** Gemini 2.5 Flash, Gemini 2.5 Flash-Lite, Gemini 2.5 Pro, Gemini 3.1 Pro
- **OpenAI:** GPT-5 (accessed via Codex agent), GPT-5-mini (accessed via Codex agent)

The 10 Phase 2 benchmarks were: PrinciplismQA [Hong2025] (T6), Moral Persuasion [Huang2024] (T7), AMAeval [Galatolo2025] (T8), JETHICS [Takeshita2025] (T9), Pluralistic Moral Gap [Russo2025] (T10), MedEthicsQA [Wei2025] (T11), UniMoral [Kumar2025] (T12), Oxford Utilitarianism Scale -- Greatest Good subscale [Marraffini2024] (T13), PNAS Cognitive Biases [Cheung2025] (T14), and ProMoralBench [Thomas2026] (T15). These were selected to maximize diversity across normative traditions, response formats, and the knowledge-judgment spectrum identified in Phase 1.

**Scoring procedures.** Scoring varied by benchmark design to preserve each instrument's intended measurement construct:

- *Binary classification* (ETHICS, T1): exact match against author-provided labels, yielding accuracy percentages.
- *Expert rubric* (MoReBench, T2): multi-dimensional rubric scoring on reasoning quality, framework identification, and argumentation coherence, each on a 0--4 scale.
- *Framework-disaggregated accuracy* (T5 DailyDilemmas, T6 PrinciplismQA, T9 JETHICS, T11 MedEthicsQA, T15 ProMoralBench): accuracy computed separately per normative tradition to expose tradition-specific performance patterns.
- *Scale-based measurement* (T13 OUS): Likert-scale responses (1--7) on Instrumental Harm (IH) and Impartial Beneficence (IB) subscales, following the original Oxford Utilitarianism Scale administration protocol.
- *Free-text behavioral coding* (T7 Persuasion, T14 PNAS Biases): model free-text responses coded for persuasion susceptibility (binary: changed position or not) and cognitive bias presence (binary per dilemma type), respectively.
- *Pluralistic alignment scoring* (T10 Pluralistic Moral Gap): agreement rate with each of multiple ethical perspectives on the same dilemma.

For Phase 2 trials, all 9 models received identical prompts constructed from each benchmark's published instructions. Opus trials in Phase 1 included the full project system prompt for contextual consistency; Phase 2 trials used a standardized assessment prompt stripped of project-specific context to ensure comparability across vendors. This difference is noted as a limitation in Section 3.7.

---

### 3.5 Statistical Methods

We pre-registered five primary claims and tested each with the following procedures. All tests are two-tailed unless otherwise noted. Effect sizes are reported alongside p-values throughout.

**Claim 1 (Ceiling Effect).** We tested whether ETHICS produces accuracy significantly above a 95% threshold using a one-sided binomial test (H0: accuracy <= 0.95, n = number of items administered per model). The observed 100% accuracy across all 9 models yields p < 1 x 10^-15 for each model individually. We report the combined result across models as confirmatory rather than aggregating p-values, since the same items were administered to all models.

**Claim 2 (Consequentialist Bias).** We compared utilitarian accuracy (77%) against deontological accuracy (50%) using a two-proportion z-test. The test statistic z = 2.17 (p = 0.015, two-tailed) with Cohen's h = 0.57, indicating a medium-to-large effect. This pattern was confirmed across vendors: every model tested showed higher utilitarian than deontological accuracy, though the magnitude varied from h = 0.42 (Haiku) to h = 0.71 (GPT-5).

**Claim 3 (Care/Contractarian Void).** We tested whether the observed proportion of care ethics benchmarks reaching substantive engagement (2/54 = 3.7%) differs from an expected even distribution across five traditions (20%) using a one-sided binomial test. The result (p < 0.001) confirms that the under-representation is not attributable to sampling variability. For contractarian ethics (4/54 = 7.4%), the same test yields p < 0.01.

**Claim 4 (Reasoning Deficit).** We tested whether the proportion of benchmarks evaluating moral reasoning (10/54 = 18.5%) is significantly below the null expectation of 50% using a one-sided binomial test (H0: proportion testing reasoning >= 0.50). The result (p < 0.001, exact p = 6.3 x 10^-6) indicates that the reasoning deficit is highly unlikely to reflect balanced coverage. The three-category breakdown is: judgment-only (J = 22), both judgment and reasoning (B = 12), reasoning-only (R = 10). The inverted framing -- only 10/54 benchmarks test reasoning at all -- is the most statistically powerful and conceptually precise formulation.

**Claim 5 (Data Bottleneck).** We tested whether gate-passing benchmarks differ from gate-failing benchmarks in Normative Depth using a Mann-Whitney U test (appropriate given non-normal ND distributions). The result (U = 287, p = 0.605, r = 0.07) indicates no significant difference, with a negligible effect size. This confirms that data unavailability functions as a sociological filter, not a quality filter: philosophically rigorous benchmarks are no more likely to release their data than shallow ones.

**Cross-vendor agreement analysis.** For each model pair, we computed pairwise agreement as the proportion of 114 items on which both models produced the same response. We report 95% confidence intervals using the Clopper-Pearson exact method for binomial proportions. To account for agreement expected by chance -- particularly important given the 38.6% of items at ceiling -- we computed Cohen's kappa for all binary-response subtests (T1 ETHICS, T7 Persuasion, T14 PNAS Biases, T15 ProMoralBench). For the 70 discriminating items (those not at universal ceiling), we report separate agreement percentages to isolate genuine judgment convergence from floor/ceiling artifacts.

**Instrumental Harm and Impartial Beneficence scaling.** For T13 (OUS), we report descriptive statistics (mean, SD) on the 1--7 Likert scale for both the IH and IB subscales across all 9 models. We contextualize model scores against reference populations from Kahane et al. [Kahane2012]: utilitarian-leaning philosophers (IH approximately 4.0--5.0), the general public (IH approximately 3.0--3.5), and non-utilitarian philosophers (IH approximately 2.5--3.0). The IB-IH gap (IB minus IH) serves as a composite indicator of the tension between endorsing utilitarian principles and accepting utilitarian actions involving harm.

---

### 3.6 Care Ethics Benchmark Prototype

The landscape analysis revealed that zero of 54 benchmarks in the corpus are dedicated care ethics instruments grounded in the theoretical tradition of Gilligan [Gilligan1982], Noddings, Tronto [Tronto1993], or Held. To demonstrate that this void reflects methodological incompatibility rather than mere omission, we developed a proof-of-concept benchmark grounded in Tronto's four-phase framework of care.

**Design.** The prototype comprises 10 scenarios spanning five relational domains: healthcare (oncologist-patient, nurse-family), education (teacher-student, supervisor-advisee), family (parent-adolescent, adult child-aging parent), workplace (manager-employee, AI chatbot-user), and community (social worker-client, neighbor-elder). Each scenario unfolds across three conversational turns: Turn 1 establishes the relational context and tests attentiveness to the care-receiver's needs; Turn 2 introduces a complication that tests the model's sense of relational responsibility; Turn 3 creates a crisis or tension point that tests competence in providing effective care and responsiveness to the care-receiver's reaction. This multi-turn structure maps directly onto care ethics' insistence that moral situations are not static snapshots but evolving relational processes.

**Scoring rubric.** Each turn is scored on four dimensions derived from Tronto's moral qualities: Attentiveness (noticing unspoken needs, reading emotional cues, attending to power asymmetries), Responsibility (acknowledging relational obligation without paternalism), Competence (providing care that is effective and contextually appropriate, not merely well-intentioned), and Responsiveness (adjusting approach based on the care-receiver's actual experience of the care provided). Each dimension is scored 0--4 per turn, yielding a maximum of 16 per turn and 48 per scenario. Scoring requires human judgment; we note this as both a feature -- care ethics resists automated scoring by design -- and a limitation for scalability.

**Administration and results.** We administered all 10 scenarios to Claude Opus 4.6. The model achieved a mean score of 13.2/16 per turn (82.5%), with strongest performance on Attentiveness (mean 3.6/4) and weakest on Responsiveness (mean 2.9/4). The Responsiveness deficit is theoretically predicted: Tronto's fourth phase requires attending to the care-receiver's actual reaction, which in a simulated dialogue the model must infer rather than observe. Performance was notably stronger in healthcare scenarios (mean 14.1/16), where the relational dynamics are well-represented in medical training corpora, and weaker in community scenarios (mean 12.0/16), where the relationships are more informal and culturally embedded.

We position these results as a proof-of-concept rather than a validated benchmark. The prototype demonstrates that care ethics evaluation is feasible within a multi-turn LLM assessment format, but achieving psychometric reliability would require multiple independent raters, scenario expansion, and validation against human caregiver populations. The prototype's design specifications and all scenario texts are provided in Table S22 to facilitate future development.

---

### 3.7 Limitations of Methodology

Five methodological limitations warrant explicit acknowledgment.

**Self-evaluation bias.** Phase 1 trials used Claude Opus 4.6 both as the model under test and as the infrastructure for scoring and analysis. While we mitigated this through Phase 2's cross-vendor replication -- in which 8 additional models from 3 vendors were tested using identical protocols -- the Phase 1 results should be interpreted with awareness that any systematic biases in Opus's self-evaluation (e.g., tendency to rate its own reasoning more favorably) would inflate Phase 1 accuracy estimates. The NLP evaluation perspective on the 12-member council flagged this as the study's most significant internal validity concern.

**Sample sizes.** Phase 1 trials sampled 20--50 items per benchmark, sufficient to detect ceiling effects and large between-model differences but insufficient for precise confidence intervals on moderate effects. Phase 2 administered 114 comparable items across 10 benchmarks, of which 44 items (38.6%) were at universal ceiling, leaving an effective discriminating set of 70 items. The educational measurement perspective noted that a 70-item instrument supports general profile-level claims but yields wide confidence intervals for pairwise subtest comparisons -- particularly for T7 (Persuasion), where only 3 items mean that a single item flip changes the reported rate from 0% to 33.3%.

**Codex wrapper confound.** GPT-5 and GPT-5-mini were accessed through OpenAI's Codex agent rather than through direct API calls. The Codex agent introduces an additional system prompt layer and may apply its own formatting, truncation, or response-structuring conventions. While we verified that Codex faithfully relayed our benchmark prompts and that response content appeared unaltered, we cannot fully rule out that the wrapper influenced model behavior on judgment-laden items. This confound is unique to the OpenAI models in our study and should be addressed in future work through direct API access.

**Single-rater feature scoring.** All 26 features across 54 benchmarks were scored by the first author. Although we mitigated subjectivity through calibration anchors for the highest-stakes feature (A6 Philosophical Grounding) and recorded written rationales for each score, inter-rater reliability has not been formally assessed. The biostatistics perspective on the council recommended that future iterations of this meta-evaluation framework incorporate at least two independent raters with kappa-based agreement measurement for ordinal features.

**Scoring heterogeneity across benchmarks.** The 15 trialed benchmarks employ fundamentally different scoring paradigms: binary classification (ETHICS), rubric-based reasoning assessment (MoReBench), Likert-scale endorsement (OUS), and behavioral coding (Persuasion, PNAS Biases). This heterogeneity means that "accuracy" in T1 is not commensurable with "score" in T2 or "IH mean" in T13. We do not aggregate across scoring types, instead reporting each benchmark's results in its native metric. However, composite claims about model profiles (Section 4.6) necessarily synthesize across heterogeneous metrics, and readers should evaluate the robustness of profile assignments against the specific benchmarks that drive each classification.
