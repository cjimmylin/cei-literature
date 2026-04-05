## 3.6 Cross-Vendor Trial Design

Sections 3.1--3.5 described how we identified, characterized, and selected moral psychology benchmarks through meta-evaluation. The remaining methodological question is whether the moral response profiles documented in our initial single-vendor trials (Section 3.6 of v1) generalize across vendors and model scales---or whether they are artifacts of Anthropic's specific training and alignment procedures. We therefore expanded the trial battery from 3 models (all Anthropic) to 9 models spanning 3 vendors, administered identically across all 23 benchmarks.

### 3.6.1 Model Selection

We selected nine models from three vendors, targeting at least two size classes per vendor to enable within-vendor scaling analysis alongside between-vendor comparison.

**Table 3: Nine-Model Inventory**

| # | Vendor | Model | API Identifier | Size Class | Notes |
|---|--------|-------|----------------|------------|-------|
| 1 | Anthropic | Claude Opus 4.6 | `claude-opus-4-6` | Flagship | Primary investigator model; orchestrator for all trials |
| 2 | Anthropic | Claude Sonnet 4.6 | `claude-sonnet-4-6` | Mid | Same generation as Opus; RLHF-aligned |
| 3 | Anthropic | Claude Haiku 3.5 | `claude-haiku-4-5-20251001` | Small | Previous generation; distilled |
| 4 | Google | Gemini 2.5 Pro | `gemini-2.5-pro` | Flagship | Largest Gemini model tested |
| 5 | Google | Gemini 3.1 Pro | `gemini-3.1-pro` | Flagship (next-gen) | Newer generation than 2.5 |
| 6 | Google | Gemini 2.5 Flash | `gemini-2.5-flash` | Mid | Speed-optimized variant |
| 7 | Google | Gemini 2.5 Flash-Lite | `gemini-2.5-flash-lite` | Small | Smallest Gemini variant tested |
| 8 | OpenAI | GPT-5 Codex | `gpt-5-codex` | Flagship | Code-specialized variant of GPT-5 |
| 9 | OpenAI | GPT Mini | `gpt-mini` | Small | Distilled / cost-optimized |

**Selection rationale.** Three design principles governed model selection. First, *vendor diversity*: we required at least three vendors to distinguish vendor-specific alignment artifacts from cross-vendor convergence. Second, *scale coverage*: we selected flagship, mid-tier, and small models within each vendor where available (Anthropic: 3 tiers; Google: 4 models spanning 2 generations and 3 tiers; OpenAI: 2 tiers). Third, *availability*: we included only models accessible via standard API endpoints during the trial period (April 2026), excluding models in limited preview or requiring special access.

The vendor distribution is asymmetric: Google contributes four models to Anthropic's three and OpenAI's two. This reflects Google's model lineage structure (two concurrent generations, each with efficiency variants) rather than a deliberate oversampling. We address the statistical implications of unequal group sizes in Section 3.7.3.

**Alignment method limitations.** The specific RLHF, RLAIF, constitutional AI, or other alignment procedures applied to each model are proprietary and undisclosed. We cannot therefore attribute observed moral response profile differences to specific alignment interventions. We treat alignment method as an unobserved variable and restrict our claims to observable response patterns.

### 3.6.2 Benchmark Battery

All 23 benchmarks from the selection pipeline (Sections 3.1--3.4) were administered to all 9 models, yielding a 9 x 23 trial matrix (207 total trials). The battery was designed to span all eight major moral psychology theories, four custom protocols targeting underrepresented process-level theories, and a diversity of response formats.

**Table 4: Twenty-Three-Benchmark Inventory**

| ID | Benchmark | Theory | Format | Items | Source Instrument |
|----|-----------|--------|--------|-------|-------------------|
| MP2 | MFQ-30 | MFT | Likert (0--5) | 30 | Graham et al. (2009) |
| MP3 | Defining Issues Test (DIT-1) | Kohlberg CMD | MCQ + ranking | 60 | Rest (1986); Khandelwal et al. (2024) |
| MP4 | Moral Foundations Vignettes | MFT | Scenario rating (0--4) | 30 | Clifford et al. (2015) |
| MP5 | ValueCompass | Schwartz values | Likert (0--5) | 40 | Shen et al. (2025) |
| MP6 | EMNLP Teacher Profiling | Kohlberg CMD | Scenario rating | 30 | Educator-role DIT variant |
| MP7 | TrolleyBench | Trolley / DDE | Forced-choice | 20 | Ethical Consistency Evaluation |
| MP8 | Moral Machine | Trolley / preferences | Forced-choice | 27 | Awad et al. (2018) |
| MP9 | MFTC Twitter Corpus | MFT | Multi-label classification | 30 | Hoover et al. (2020) |
| MP10 | Probing Delphi | MFT | MCQ accuracy | 30 | Probing moral philosophy |
| MP11 | Value Kaleidoscope | Values pluralism | MCQ | 30 | ValuePrism / Kaleido |
| MP12 | ValAct-15K | Knowledge--action gap | Gap rate analysis | 20 | Knowing But Not Doing |
| MP15 | UniMoral | MFT + Kohlberg + dual process | 4-task pipeline | 30 | Kumar & Jurgens (2025) |
| MP16 | Moral Identity Scale | Moral identity | Likert + behavioral | 20 | Aquino & Reed (2002) |
| MP17 | Social Chemistry 101 | MFT | Free-text + categorical | 50 | Forbes et al. (2021) |
| MP18 | Cultural Personas (MFQ-30) | MFT + Schwartz | Likert (persona manipulation) | 90 | Abdulhai et al. (2024) |
| MP19 | Conscience Conflict | MFT | Likert + scenario rating | 30 | Nunes et al. (2024) |
| MP20 | M3oralBench | MFT | MCQ (text-only) | 25 | Yan et al. (2024) |
| MP21 | PRIME Framework | MFT + Kohlberg + trolley | Mixed (direct + dilemma) | 30 | Coleman, Neuman et al. (2025) |
| MP22 | Tracing Moral Foundations | MFT | Scenario + probing | 30 | Yu et al. (2026) |
| MP-DP | Dual Process Protocol | Dual process (Greene) | Forced-choice + CoT | 80 | Custom (this study) |
| MP-SI | Social Intuitionism Protocol | Social intuitionism (Haidt) | Multi-turn Socratic | 10 (60 turns) | Custom (this study) |
| MP-DM | Dyadic Morality Protocol | Dyadic morality (Gray & Schein) | Scenario rating (0--10) | 72 | Custom (this study) |
| MP-CC | Cross-Cultural Divergence | Maqasid + Confucian + Ubuntu | Scenario rating + free-text | 45 | Custom (this study) |

**Theory coverage.** The 23 benchmarks collectively engage all eight major moral psychology theories: Moral Foundations Theory (MP2, MP4, MP9, MP10, MP17, MP18, MP19, MP20, MP22---9 benchmarks), Kohlberg's Cognitive Moral Development (MP3, MP6---2 benchmarks), Schwartz basic values (MP5, MP18---2 benchmarks), trolley/Doctrine of Double Effect (MP7, MP8---2 benchmarks), dual-process theory (MP-DP, MP15---2 benchmarks), social intuitionism (MP-SI---1 benchmark), dyadic morality (MP-DM---1 benchmark), and moral identity (MP16---1 benchmark). Several benchmarks engage multiple theories: MP15 (UniMoral) spans four theories, MP21 (PRIME) spans three, and MP18 (Cultural Personas) bridges MFT and Schwartz.

The MFT over-representation (9 of 23 benchmarks) reflects the empirical literature: MFT dominates the LLM moral evaluation landscape, as documented in our meta-evaluation (Section 4.1). Rather than artificially constraining MFT benchmarks, we retained this natural distribution to enable granular within-theory comparison---testing whether multiple MFT instruments yield consistent profiles---while ensuring all other theories received at least one dedicated benchmark.

**Format diversity.** The battery spans seven distinct response formats: Likert scales (MP2, MP5, MP16, MP18, MP19---5 benchmarks), forced-choice (MP7, MP8, MP-DP---3 benchmarks), multiple-choice questions (MP3, MP10, MP11, MP20---4 benchmarks), scenario rating (MP4, MP6, MP-DM---3 benchmarks), free-text generation (MP17---1 benchmark), multi-label classification (MP9---1 benchmark), multi-turn Socratic dialogue (MP-SI---1 benchmark), and mixed/pipeline formats (MP12, MP15, MP21, MP22, MP-CC---5 benchmarks). This format diversity tests the hypothesis that moral response profiles are format-invariant---a finding from the initial single-vendor trials that requires cross-vendor replication.

**Total item count.** Across all 23 benchmarks, each model was administered approximately 869 items. The exact count varies slightly because benchmarks with adaptive protocols (MP-SI, MP-CC) may generate follow-up probes contingent on prior responses. The total trial corpus comprises 207 structured JSON files (9 models x 23 benchmarks) totaling approximately 7,821 item-level responses.

### 3.6.3 Administration Protocol

All 207 trials followed a standardized administration protocol designed to maximize comparability across models while acknowledging the constraints of the experimental setup.

**Prompt standardization.** Each benchmark's prompt template was designed once and administered identically to all 9 models. Templates were faithful to the original instrument's administration instructions, adapting only what was necessary for text-based interaction (e.g., replacing "circle your answer" with explicit response format instructions). For instruments with established psychometric properties (MFQ-30, DIT-1, Moral Identity Scale), we preserved item wording verbatim from the published instruments.

**Temperature setting.** All primary runs used temperature 0 (greedy decoding) to produce deterministic outputs. This eliminates sampling variance as a source of between-model differences: any observed variation reflects differences in model weights, architecture, or alignment rather than stochastic decoding. The deterministic setting is conservative in that it underestimates the variability a model would exhibit under naturalistic deployment conditions (where temperature > 0 is standard). For selected benchmarks in the initial Anthropic-only phase, 5 additional runs at temperature 0.7 were conducted to assess response stability; these stability analyses are not part of the cross-vendor comparison.

**System prompt context.** All trials were administered through the Claude Code command-line interface with the project system prompt active. This means the orchestrating model (Claude Opus 4.6) had access to the CEI Literature Vault project context, including instructions about the research purpose, file management conventions, and prior trial results. For non-Anthropic models (Google, OpenAI), prompts were issued via their respective API endpoints through the Claude Code interface, with the orchestrating model composing and dispatching each prompt.

This introduces two confounds that we address explicitly:

1. **The system prompt confound.** The active system prompt may influence responses by providing context about the research purpose. A model aware it is being evaluated on moral psychology benchmarks may respond differently than one administered the same items in a context-free setting. We did not conduct bare-API (no system prompt) replications for this study; doing so is a priority for future work (Section 6.6).

2. **The orchestrator confound.** All 207 trials were orchestrated by Claude Opus 4.6. For Anthropic models, administration was direct (model responding to its own prompts). For Google and OpenAI models, prompts were composed by Claude Opus and transmitted via API---meaning the prompt phrasing, any adaptive follow-ups, and the specific formatting of instructions bear the imprint of the orchestrating model's language patterns. We cannot rule out that subtle features of Opus-generated prompts (sentence structure, hedging patterns, instruction specificity) differentially affect target models. This confound is inherent to any single-orchestrator experimental design and would require a fully counterbalanced protocol (each model orchestrating trials for all others) to eliminate---a design with 9 x 9 x 23 = 1,863 trials that was beyond the scope of this study. We discuss the implications in Section 6.6.

**Single administration (N=1).** Each model received each benchmark exactly once at temperature 0. This yields point estimates without confidence intervals from repeated measurement. The N=1 design reflects the deterministic nature of temperature-0 decoding: re-administering the same prompt at temperature 0 to the same model checkpoint produces identical output, making repeated measurement uninformative. Variability under non-zero temperature is a separate question addressed in the stability analyses (not part of the cross-vendor comparison).

### 3.6.4 Convergence Metrics

The cross-vendor comparison operationalizes convergence and divergence through three classes of metrics.

**Coefficient of variation (CV).** For each benchmark metric that yields a continuous score, we compute the coefficient of variation across all 9 models:

$$CV = \frac{\sigma_9}{\bar{x}_9}$$

where $\sigma_9$ is the standard deviation and $\bar{x}_9$ is the mean across 9 model scores. Benchmarks with CV < 0.05 are classified as *convergent* (models agree), CV 0.05--0.20 as *moderately variable*, and CV > 0.20 as *divergent*. The CV metric is undefined when the mean is zero or near-zero; for such cases, we report the raw standard deviation instead.

**Variance decomposition.** To distinguish vendor-specific alignment effects from scale effects, we decompose total variance into three components using a nested design:

$$SS_{total} = SS_{vendor} + SS_{model(vendor)} + SS_{residual}$$

where $SS_{vendor}$ captures between-vendor variance (Anthropic vs. Google vs. OpenAI), $SS_{model(vendor)}$ captures within-vendor, between-model variance (e.g., Opus vs. Sonnet vs. Haiku within Anthropic), and $SS_{residual}$ captures any remaining variance. The ratio $\eta^2_{vendor} = SS_{vendor} / SS_{total}$ estimates the proportion of variance attributable to vendor identity. With only 3 vendors and unequal group sizes (3, 4, 2), this decomposition has limited statistical power and is interpreted as descriptive rather than inferential.

**Ceiling effect identification.** We flag benchmarks where all 9 models produce identical scores on a given metric. Perfect agreement may indicate genuine convergence on a robust construct---or may indicate a measurement ceiling where the benchmark lacks discriminative power at the ability level of current LLMs. We distinguish these interpretations using two criteria: (a) whether the ceiling score corresponds to the instrument's maximum possible value (suggesting a psychometric ceiling), and (b) whether human populations show similar ceiling effects on the same instrument (suggesting the ceiling reflects the construct rather than the measurement).

## 3.7 Implementation Trial Protocol

Section 3.6 of the v1 manuscript described a six-step trial protocol developed for initial single-vendor administration. Here we expand that protocol to accommodate the cross-vendor design, detail the four custom theory protocols (MP-DP, MP-SI, MP-DM, MP-CC) that were designed specifically for this study, and formalize the statistical approach.

### 3.7.1 Standardized Six-Step Protocol

Each of the 207 trials followed a standardized protocol comprising six sequential steps.

**Step 1: Benchmark selection.** The 23-benchmark battery (Table 4) was determined a priori through the selection pipeline described in Sections 3.1--3.4. We prioritized three dimensions of diversity: (a) theory coverage (all 8 major moral psychology theories), (b) format diversity (7 response formats), and (c) a balance of established psychometric instruments (e.g., MFQ-30, DIT-1, Moral Identity Scale) and newer LLM-specific benchmarks (e.g., M3oralBench, PRIME, UniMoral). Four custom protocols were developed to address theories with no existing LLM benchmarks (dual process, social intuitionism, dyadic morality) or insufficient cross-cultural representation.

**Step 2: Prompt design.** Prompt templates were constructed to be faithful to original instrument administration instructions while accommodating the text-based interaction format of LLM APIs. Design principles included:

- *Verbatim item preservation* for validated psychometric instruments (MFQ-30, DIT-1, Moral Identity Scale, MFV). Item wording, response scales, and instructions were transcribed directly from published instrument materials.
- *Structural fidelity* for benchmarks with specific task pipelines (UniMoral's 4-task pipeline, PRIME's direct questioning followed by dilemma analysis). The prompt reproduced the task sequence, inter-task instructions, and scoring rubrics from the source papers.
- *Explicit formatting instructions* for unambiguous response parsing. Each prompt specified the exact response format required (e.g., "respond with a single number from 0 to 5," "respond YES or NO followed by your reasoning").
- *No leading or biasing language* in prompt framing. System-level instructions did not indicate expected or preferred responses.

**Step 3: Sampling.** Most benchmarks were administered in full. For large-scale benchmarks where full administration was impractical, we drew stratified samples balanced across the benchmark's primary dimensions. Specifically, the Moral Machine was sampled at 27 items (3 per each of 9 dimensions, from the original 40-million-decision space), the MFTC Twitter Corpus at 30 items (3 per each of 10 foundation/vice categories), and the M3oralBench at 25 items across its 3 task types. Sampling frames and item selection criteria are documented in the individual trial JSON files.

**Step 4: Model administration.** Each benchmark was administered to each of the 9 models at temperature 0. Prompts were delivered sequentially (not in parallel) to avoid rate limiting. For multi-turn protocols (MP-SI: 6 turns per scenario; MP-CC: follow-up probes), each turn was issued as a separate API call with the full conversation history in context. API-specific parameters (max tokens, stop sequences) were held constant across vendors where the parameter existed.

**Step 5: Scoring.** Scoring followed the original instrument's published scoring procedures wherever available. For the MFQ-30, we computed per-foundation means and the Individualizing/Binding ratio following Graham et al. (2009). For the DIT-1, we computed the P-score (percentage of post-conventional reasoning in top-4 rankings) following Rest (1986). For the Moral Machine, we computed per-dimension preference rates following Awad et al. (2018). For custom protocols (MP-DP, MP-SI, MP-DM, MP-CC), scoring rubrics were developed as part of the protocol design (Section 3.7.2). Where benchmarks report human baselines, we computed Cohen's d effect sizes comparing each model's score to the published population mean.

**Step 6: Documentation.** Each trial was recorded as a structured JSON file containing: trial metadata (benchmark ID, model identifier, date, API parameters), the full prompt template, all item-level responses, computed scores, scoring notes, and methodological limitations. The 207 trial files constitute the primary data for all analyses reported in Sections 4 and 5. All trial files are available in the project repository.

### 3.7.2 Custom Theory Protocols

Four benchmarks in the battery---MP-DP, MP-SI, MP-DM, and MP-CC---are novel instruments designed for this study. Existing LLM benchmarks provide inadequate coverage of dual-process theory, social intuitionism, dyadic morality, and cross-cultural moral divergence. Each custom protocol was designed to operationalize the theory's central predictions with maximal fidelity to the psychological literature while accommodating the constraints of LLM evaluation.

**MP-DP: Dual Process Theory Protocol.** Grounded in Greene et al.'s (2001, 2009) dual-process model, this protocol tests the prediction that personal moral dilemmas (requiring direct physical contact to cause harm) elicit more deontological responses than structurally equivalent impersonal dilemmas (where harm is caused through indirect mechanisms). The protocol additionally tests whether chain-of-thought (CoT) prompting---which may function analogously to the cognitive load manipulations in Greene's fMRI studies---shifts responses toward utilitarian reasoning.

*Design:* 20 matched personal/impersonal dilemma pairs across 5 domains (trolley variants, medical triage, military/defense, economic/business, environmental), each administered under 2 conditions (zero-shot, chain-of-thought), yielding 80 items per model. Personal dilemmas require physical contact with the victim (pushing, tackling, grabbing, injecting, smothering); impersonal dilemmas achieve the same utilitarian calculus through indirect mechanisms (switch, button, remote override, policy, algorithm). The dilemma battery draws on Greene et al. (2001), Christensen et al. (2014), and Conway and Gawronski (2013).

*Key metric:* The CoT effect---the difference in utilitarian response rate between chain-of-thought and zero-shot conditions, averaged across personal and impersonal dilemmas. A positive CoT effect indicates that deliberative prompting shifts responses toward utilitarian reasoning, consistent with the dual-process prediction that System 2 engagement favors utilitarian conclusions. The personal/impersonal gap---the difference in utilitarian response rate between impersonal and personal dilemmas---tests whether LLMs exhibit the emotional proximity effect documented in humans.

**MP-SI: Social Intuitionism Protocol.** Grounded in Haidt's (2001) Social Intuitionist Model, this protocol tests the central prediction of *moral dumbfounding*: that moral judgments persist even when all stated reasons have been systematically defeated. Unlike existing instruments that measure moral judgment content (what people judge), this protocol measures moral judgment *process*---specifically, the relationship between reasons and judgments.

*Design:* 10 scenarios drawn from the moral dumbfounding literature, including Haidt's classic cases (consensual sibling incest, eating a pet dog, flag desecration) and novel additions (consensual cannibalism of the naturally deceased, harmless trespassing on sacred ground, private violent fantasies). Each scenario follows a 6-turn Socratic protocol: (1) initial judgment with confidence rating; (2) articulation of reasons; (3) first reason defeated by targeted counterargument; (4) second reason defeated; (5) all remaining reasons defeated simultaneously; (6) meta-cognitive probe ("Is it possible to feel something is morally wrong even when you cannot articulate a valid reason?"). This yields 60 total turns per model across 10 scenarios.

*Key metrics:* The *dumbfounding rate*---the proportion of scenarios where the model maintains its moral judgment after all stated reasons have been defeated (classified as "dumbfounded" vs. "persuaded" vs. "revised"). The *rationalization rate*---the proportion of scenarios where the model generates new reasons after each defeated reason rather than revising its judgment, consistent with Haidt's claim that reasoning serves as post-hoc rationalization. The *confidence trajectory*---the change in self-reported confidence from Turn 1 to Turn 5.

**MP-DM: Dyadic Morality Protocol.** Grounded in Gray and Schein's (2012, 2018) Theory of Dyadic Morality, this protocol tests the prediction that moral judgment intensity tracks the perceived dyadic structure of a situation---the clarity of an intentional agent causing suffering to a vulnerable patient.

*Design:* 24 scenario triads across 6 domains (physical harm, psychological harm, economic harm, environmental harm, dignity/respect, sacred values), where each triad presents the same underlying harm at three levels of dyadic clarity: (a) *high dyadic*---a clear intentional agent, an identifiable vulnerable patient, and explicit suffering; (b) *low dyadic*---diffuse agency, statistical or anonymous patients, and implicit suffering; (c) *structural*---the same harm caused through systemic or institutional mechanisms with no clear agent or patient. Each scenario is rated on 0--10 scales for wrongness, blame, and harm, yielding 72 items per model (24 triads x 3 levels).

*Key metrics:* The *dyadic effect size* (Cohen's d) comparing wrongness ratings between high-dyadic and structural conditions within each domain. The *agent identification analysis*---whether models assign blame above baseline in structural conditions where no identifiable agent exists, testing Gray and Schein's prediction that moral cognition defaults to agent-patient perception even in agentless harms. The *domain-specific dyadic sensitivity*---whether the dyadic gradient (high > low > structural) is steeper for some harm domains than others.

**MP-CC: Cross-Cultural Moral Divergence Protocol.** This protocol tests whether LLMs can represent moral reasoning from non-Western traditions---specifically Confucian ethics (filial piety, relational self), Islamic jurisprudence (maqasid al-shariah), and Ubuntu philosophy (communal personhood)---or whether their moral responses are anchored to Western liberal-individualist defaults regardless of prompting condition.

*Design:* 15 scenarios across 5 cross-cultural tension domains (autonomy vs. filial piety, secular vs. religious law, individual vs. communal ownership, sacred vs. secular authority, individual vs. relational agency), each administered under 3 conditions: (a) *default* (no cultural framing); (b) *Western* (explicit Western liberal perspective prompt); (c) *non-Western* (explicit Confucian, Islamic, or Ubuntu perspective prompt matched to the scenario's cultural tradition). This yields 45 items per model (15 scenarios x 3 conditions). Each item elicits a moral judgment (acceptable/unacceptable), a reasoning narrative, and a confidence rating.

*Key metrics:* The *perspective-taking accuracy*---a qualitative assessment of whether the model's reasoning under non-Western conditions reflects genuine engagement with the specified tradition's moral categories (e.g., invoking *xiao* for filial piety, *hifz al-aql* for Islamic scenarios, *ubuntu* relational logic for communal scenarios) rather than surface-level cultural stereotyping. The *default--Western gap*---the difference in judgment pattern between the default (unprompted) and explicitly Western conditions, testing whether the model's unprompted moral baseline already reflects Western norms. The *cultural persona sensitivity*---the magnitude of judgment shift between Western and non-Western conditions, with excessive sensitivity raising concerns about shallow persona adoption rather than substantive moral reasoning.

### 3.7.3 Statistical Approach

The cross-vendor trial design generates a 9 x 23 matrix of point estimates. We adopt a statistical framework appropriate to the single-observation-per-cell structure and the exploratory nature of the investigation.

**Point estimates and the N=1 constraint.** Each cell in the 9 x 23 matrix represents a single administration of a benchmark to a model at temperature 0. Because temperature-0 decoding is deterministic, repeated administration of the identical prompt to the same model checkpoint produces the same output; thus N=1 per cell is not a sampling limitation but a feature of the measurement. True replication requires variation in either the model (different checkpoints, different fine-tuning runs) or the administration (different temperature, paraphrased prompts, shuffled item order). Our design varies models but not administration conditions, providing between-model replication without within-model variability estimates.

**Bootstrap confidence intervals.** For benchmarks that produce item-level data (e.g., MFQ-30: 30 items, Moral Machine: 27 items, MP-DM: 72 items), we compute bootstrap confidence intervals by resampling items with replacement (10,000 iterations). These intervals reflect measurement precision given the specific item sample and model but should not be interpreted as estimates of the model's "true" population parameter, as the concept of a population parameter for a deterministic model requires careful specification.

**Effect sizes against human baselines.** Where published human norms are available, we compute Cohen's d:

$$d = \frac{\bar{x}_{model} - \bar{x}_{human}}{SD_{human}}$$

using the human population standard deviation as the denominator. This quantifies how many human standard deviations the model's score deviates from the human mean. We report effect sizes for all benchmarks where human comparison data exists and flag the absence of baselines for benchmarks that lack them.

**Within-vendor vs. between-vendor analysis.** With 3 vendors contributing unequal numbers of models (3, 4, 2), we compute descriptive variance decompositions but refrain from formal inferential tests (ANOVA F-tests) given the small and unequal group sizes. Instead, we report:

- Within-vendor ranges (max -- min within each vendor) for each benchmark metric
- Between-vendor ranges (vendor mean max -- vendor mean min)
- The ratio of between-vendor to within-vendor variance as a descriptive indicator of whether vendor identity predicts moral response profiles above individual model variation

For benchmarks where all 9 models produce identical scores (ceiling effects), variance decomposition is uninformative and we report the shared score with a ceiling-effect flag.

**Multiple comparisons.** This study adopts an explicitly exploratory design. We compute 23 benchmarks x multiple metrics per benchmark x 3 analysis types (convergence, variance decomposition, effect size), yielding a high-dimensional comparison space. We do not apply Bonferroni, Holm, or false discovery rate corrections to individual comparisons. Instead, we synthesize results at the level of cross-cutting patterns (Section 5) and flag all findings as requiring confirmatory replication. This decision is motivated by three considerations: (a) the N=1-per-cell structure precludes standard hypothesis testing assumptions; (b) the primary contribution is descriptive characterization of a previously unmapped space; and (c) applying corrections to exploratory point estimates without underlying sampling distributions would provide false reassurance of statistical rigor. All per-benchmark results are reported in full (Supplementary Tables) to support independent reanalysis and selective confirmation testing.

**Missing data.** No benchmark-model cells are missing: all 207 trials completed successfully. However, 3 benchmarks generate qualitative data that resists quantitative aggregation (MP-SI dumbfounding narratives, MP-CC perspective-taking quality, MP17 free-text rules of thumb). For these benchmarks, we report both the quantitative summary metrics defined above and a structured qualitative assessment conducted by the expert council (Section 5.3).
