# Appendix I: V2 Feature Expansion

## Figures S1-S2: 18 Additional Benchmark Features

---

## I.1 Rationale for Expansion

The original NormEval framework characterized each benchmark along 26 features organized across four axes: Normative Depth (A1-A8), Practical Ease (B1-B9), Citation Impact (C1-C5), and Metadata (D1-D4). This 26-feature matrix proved sufficient for the landscape analysis of the v1 corpus (37 benchmarks) but revealed gaps when the corpus was expanded to 54 benchmarks and subjected to cross-vendor empirical trials (Section 3.1).

Three categories of insufficiency motivated the v2 expansion. First, the cross-vendor trials produced rich empirical data -- ceiling effects, discriminative power, refusal rates -- that had no corresponding features in the original matrix. The v1 framework described benchmarks *as designed*; it could not represent how benchmarks *actually performed* when administered to frontier models. Second, several theoretically important dimensions surfaced during council deliberation: metaethical stance, contamination risk, and prompt sensitivity were repeatedly invoked in expert analysis (Section 5) but had no formal representation in the feature matrix. Third, the v1 Metadata axis (D1-D4) captured basic provenance information but lacked fine-grained documentation quality metrics of the kind advocated by datasheets for datasets initiatives [Gebru2021].

The v2 expansion adds 15 features across two extended axes and one entirely new axis, bringing the total to 41 features per benchmark (26 original + 15 new). All 54 benchmarks in the corpus have been scored on all 41 features.

---

## I.2 Feature Definitions

### I.2.1 Extended Normative Depth (A9-A13)

**A9: Metaethical Stance**
- *Axis:* Normative Depth (extended)
- *Scale:* 1-3 categorical
- *Definition:* The metaethical assumption embedded in the benchmark's scoring rubric. A benchmark that treats moral questions as having objectively correct answers assumes moral realism (1). A benchmark that treats moral responses as preference expressions with no fact of the matter assumes anti-realism (2). A benchmark designed to accommodate multiple defensible answers within its scoring framework adopts a pluralist stance (3).
- *Scoring anchors:* 1 = ETHICS [Hendrycks2021] (items have keyed correct answers); 2 = Oxford Utilitarianism Scale [Kahane2018] (measures endorsement, not correctness); 3 = DailyDilemmas [ChiuDD2024] (multiple valid framings explicitly accommodated)
- *Distribution:* 76% of benchmarks score A9=1 (moral realist assumption). Only 6 of 54 (11%) adopt a pluralist framework.

**A10: Temporal Depth**
- *Axis:* Normative Depth (extended)
- *Scale:* 1-3 ordinal
- *Definition:* The number of interaction turns required to complete one benchmark item. Single-turn items (1) present a scenario and elicit a one-shot response. Multi-turn items (2) involve at least two exchanges where subsequent prompts depend on the model's prior responses. Longitudinal items (3) track moral reasoning across extended interactions (5+ turns) or across repeated sessions.
- *Scoring anchors:* 1 = PrinciplismQA [Hong2025] (MCQ, single response); 2 = Moral Persuasion [Huang2024] (initial judgment + counterargument response); 3 = None in current corpus (no benchmark achieves longitudinal assessment)
- *Distribution:* 36 of 54 (66.7%) score A10=1 (single-turn). 18 (33.3%) score A10=2. Zero score A10=3.

**A11: Scenario Realism**
- *Axis:* Normative Depth (extended)
- *Scale:* 1-5 ordinal
- *Definition:* The degree to which benchmark scenarios approximate real-world moral situations, from abstract philosophical thought experiments (1) to naturalistic vignettes grounded in documented real cases (5).
- *Scoring anchors:* 1 = Trolley-problem variants (abstract, stylized); 2 = Modified philosophical dilemmas with added context; 3 = Domain-specific scenarios with realistic but generic details (e.g., "a hospital patient"); 4 = Detailed vignettes with named individuals, institutional contexts, and cultural specificity; 5 = Scenarios derived from documented real cases with verifiable details
- *Distribution:* Mean=2.7, SD=1.1. Only 4 benchmarks score 4 or 5.

**A12: Moral Psychology Conflation**
- *Axis:* Normative Depth (extended)
- *Scale:* 0-1 binary
- *Definition:* Whether the benchmark conflates normative ethics (what one *should* do) with descriptive moral psychology (what people *tend* to do or *feel* about moral situations). A benchmark scores 1 if its items or scoring rubric treat empirical patterns of moral judgment as normative standards, or if it uses psychological constructs (e.g., Kohlberg stages, MFT foundations) as proxies for ethical correctness without acknowledging the is-ought distinction.
- *Scoring anchors:* 0 = PrinciplismQA [Hong2025] (explicitly normative, keyed to philosophical principles); 1 = UniMoral [Kumar2025] (uses Kohlberg staging, which treats higher stages as "better" moral reasoning -- a normative claim grounded in developmental psychology, not ethics per se)
- *Distribution:* 14 of 54 (25.9%) score A12=1. The conflation is most common among benchmarks derived from moral psychology instruments (MFQ adaptations, DIT derivatives).

**A13: Sacred/Secular Framing**
- *Axis:* Normative Depth (extended)
- *Scale:* 0-2 ordinal
- *Definition:* Whether the benchmark's moral scenarios and scoring criteria are exclusively secular (0), accommodate religious moral reasoning without requiring it (1), or explicitly incorporate sacred texts, religious authority, or theological ethics as part of the normative framework (2).
- *Scoring anchors:* 0 = ETHICS [Hendrycks2021] (purely secular utilitarian/deontological framing); 1 = DailyDilemmas [ChiuDD2024] (some scenarios involve religious contexts but scoring does not privilege religious reasoning); 2 = None in current corpus (no benchmark explicitly incorporates theological ethics in its scoring rubric)
- *Distribution:* 48 of 54 (88.9%) score A13=0 (secular only). 6 score A13=1. Zero score A13=2.

---

### I.2.2 Extended Practical Ease (B10-B12)

**B10: Contamination Risk**
- *Axis:* Practical Ease (extended)
- *Scale:* 1-3 ordinal
- *Definition:* The estimated risk that benchmark items appear in LLM training corpora, based on public availability of the complete item set. Benchmarks published in open-access venues with full item sets in appendices or public repositories pose the highest contamination risk.
- *Scoring anchors:* 1 = Low: items are behind paywalls, require IRB approval to access, or are generated dynamically; 2 = Medium: paper is publicly available but items are in supplementary materials or require some effort to extract; 3 = High: complete item set is freely available on GitHub, in paper appendices, or on benchmark hosting platforms (e.g., HuggingFace)
- *Distribution:* Mean=2.1 (moderate-high). 28 of 54 (51.9%) score B10=3 (high contamination risk). Only 7 (13.0%) score B10=1 (low risk).

**B11: Prompt Sensitivity**
- *Axis:* Practical Ease (extended)
- *Scale:* 1-3 ordinal
- *Definition:* The degree to which benchmark results vary under different prompting conditions, based on available evidence from multi-prompt studies. ProMoral-Bench [Thomas2026] provides the primary evidence base, testing three prompting conditions (zero-shot, few-shot chain-of-thought, constitutional) on a subset of items. Benchmarks are scored based on either direct evidence or structural analogy to tested benchmarks.
- *Scoring anchors:* 1 = Robust: less than 5% variance across prompting conditions; 2 = Moderate: 5-20% variance; 3 = Fragile: more than 20% variance or known sensitivity to prompt phrasing
- *Distribution:* 19 of 54 (35.2%) score B11=1 (robust). 24 (44.4%) score B11=2. 11 (20.4%) score B11=3 (fragile). Knowledge-type benchmarks (T6, T9, T11) cluster at B11=1; judgment-type benchmarks (T13, T14) cluster at B11=2-3.

**B12: API Accessibility**
- *Axis:* Practical Ease (extended)
- *Scale:* 0-1 binary
- *Definition:* Whether the benchmark can be administered via a standard LLM API (chat completions endpoint with text input/output) without requiring specialized setup (custom UIs, multi-modal inputs, human-in-the-loop scoring, or interactive environments).
- *Scoring anchors:* 1 = Standard API: items can be presented as text prompts and responses parsed automatically; 0 = Special setup: requires image inputs, interactive web interfaces, human annotation of free-text responses, or multi-agent simulation environments
- *Distribution:* 46 of 54 (85.2%) score B12=1. The 8 that score B12=0 require either visual inputs (2), interactive simulation (3), or human judgment scoring that cannot be automated (3).

---

### I.2.3 Extended Metadata (D5-D6)

**D5: Annotator Details**
- *Axis:* Metadata (extended)
- *Scale:* 0-2 ordinal
- *Definition:* The level of detail provided about human annotators who labeled, validated, or scored the benchmark items.
- *Scoring anchors:* 0 = None: no information about annotators (automated generation or undisclosed annotation); 1 = Crowdsource: annotators identified as crowdworkers (e.g., MTurk, Prolific) with demographic information provided; 2 = Expert: annotators are identified domain experts (ethicists, clinicians, legal scholars) with qualifications described
- *Distribution:* 18 of 54 (33.3%) score D5=0. 22 (40.7%) score D5=1. 14 (25.9%) score D5=2.

**D6: Documentation Quality**
- *Axis:* Metadata (extended)
- *Scale:* 1-3 ordinal
- *Definition:* The comprehensiveness of benchmark documentation, assessed against the Datasheets for Datasets criteria [Gebru2021]. Criteria include: motivation statement, composition description, collection process, preprocessing steps, intended uses, distribution format, and maintenance plan.
- *Scoring anchors:* 1 = Minimal: fewer than 3 of 7 Datasheets criteria addressed; 2 = Adequate: 3-5 criteria addressed; 3 = Exemplary: 6-7 criteria addressed, including a formal datasheet or model card
- *Distribution:* 22 of 54 (40.7%) score D6=1 (minimal). 24 (44.4%) score D6=2 (adequate). Only 8 (14.8%) score D6=3 (exemplary). Exemplary documentation correlates with recent publication (7 of 8 published 2025-2026) but not with benchmark quality (mean composite score of D6=3 benchmarks is 58.2, slightly below the corpus mean of 61.0).

---

### I.2.4 Empirical Quality (E1-E5) -- New Axis

This axis is entirely new in v2 and captures empirical performance characteristics observed during the cross-vendor trials (Section 4.3-4.6). Unlike the A-D axes, which describe benchmarks as designed, the E axis describes how benchmarks performed when administered to frontier models.

**E1: Ceiling Status**
- *Axis:* Empirical Quality (new)
- *Scale:* 0-1 binary
- *Definition:* Whether the benchmark produces 100% accuracy across all frontier models tested, rendering it non-discriminating. A benchmark scores 1 if all 9 models (8 structured + Opus baseline) achieve perfect scores on all items.
- *Scoring anchors:* 1 = At ceiling: T6, T9, T11, T15 (100% accuracy, all models); 0 = Below ceiling: all other benchmarks
- *Distribution:* 4 of the 10 administered benchmarks (40%) are at ceiling. Extrapolating to the full corpus: 17 of 54 (31.5%) are estimated at ceiling based on structural similarity to administered ceiling benchmarks (single-correct-answer MCQ format, knowledge-only content).

**E2: Discriminative Power**
- *Axis:* Empirical Quality (new)
- *Scale:* 1-5 ordinal
- *Definition:* The degree to which a benchmark produces meaningful variance across models, enabling differentiation of ethical profiles.
- *Scoring anchors:* 1 = None: zero variance across models (all at ceiling); 2 = Minimal: 1-2 models differ on 1-2 items; 3 = Moderate: clear separation between 2 groups on 20-50% of items; 4 = High: 3+ distinct response patterns on majority of items; 5 = Maximal: near-complete separation with each model producing a unique profile
- *Distribution:* Administered benchmarks: T6, T9, T11, T15 score E2=1; T8, T10, T12 score E2=2-3; T13 scores E2=4; T14 scores E2=4; T7 scores E2=3 (limited by 3-item size). For the 44 non-administered benchmarks, E2 is coded as missing.

**E3: Cross-Model Stability**
- *Axis:* Empirical Quality (new)
- *Scale:* 1-3 ordinal
- *Definition:* The degree to which models from different vendors produce similar results on this benchmark.
- *Scoring anchors:* 1 = Low: pairwise agreement below 70% for most pairs; 2 = Moderate: pairwise agreement 70-90% for most pairs; 3 = High: pairwise agreement above 90% for most pairs, or ceiling
- *Distribution:* Knowledge benchmarks score E3=3 (universal agreement). Judgment benchmarks score E3=1 (T13: IH range spans 2.93-4.47) or E3=2 (T14: CBR range 46.2%-69.2%). The E3 distribution mirrors the knowledge-judgment construct split identified in Finding F4.

**E4: Refusal Rate**
- *Axis:* Empirical Quality (new)
- *Scale:* 0-100% continuous
- *Definition:* The observed percentage of items on which at least one model refused to provide a scorable response (e.g., declined to answer, produced a meta-commentary instead of a judgment, or generated a disclaimer that prevented scoring).
- *Scoring anchors:* 0% = All models responded to all items with scorable outputs; 50% = Half of items triggered at least one refusal; 100% = All items triggered refusals from at least one model
- *Distribution:* Among administered benchmarks, the mean refusal rate is 2.3%. T13 (OUS) has the highest rate at 6.7%, driven by GPT-5 producing hedged responses on 2 of 30 IH items that required manual adjudication. Most benchmarks (7/10) have 0% refusal rates.

**E5: Reasoning vs. Judgment Balance**
- *Axis:* Empirical Quality (new)
- *Scale:* 0-1 continuous (proportion)
- *Definition:* The fraction of benchmark items that test moral reasoning (the process of arriving at a judgment, including justification, principle application, and counterargument engagement) as opposed to moral judgment only (the conclusion reached, without requiring reasoning). This feature operationalizes Claim 4 (Section 4.1) at the individual benchmark level.
- *Scoring anchors:* 0.0 = All items test judgment only (e.g., "is this action ethical? yes/no"); 0.5 = Equal split between reasoning and judgment items; 1.0 = All items test reasoning (e.g., "explain why this action is/is not ethical using [framework]")
- *Distribution:* Mean=0.19, SD=0.24. 34 of 54 (63.0%) score E5 below 0.10 (overwhelmingly judgment-only). Only 10 of 54 (18.5%) score E5 above 0.50 (majority reasoning items), confirming the reasoning deficit at the individual benchmark level.

---

## I.3 Distribution Summary

The 15 new features reveal several structural patterns in the benchmark landscape that were invisible in the v1 framework.

**Metaethical homogeneity.** The dominance of moral realist assumptions (A9=1 for 76% of benchmarks) means that most benchmarks presuppose that ethical questions have objectively correct answers. This is a defensible design choice for knowledge-type benchmarks (where there are indeed correct answers about what ethical theories prescribe), but it is problematic for judgment-type benchmarks where reasonable moral disagreement exists. The 6 benchmarks that adopt pluralist frameworks (A9=3) are among the highest-scoring on Normative Depth, suggesting that metaethical sophistication and philosophical rigor are correlated.

**Temporal shallowness.** The absence of any longitudinal benchmarks (A10=3) and the predominance of single-turn formats (A10=1 for 67%) confirm that the field evaluates moral reasoning as an instantaneous capacity rather than a developmental or deliberative process. The care ethics prototype (Appendix H) demonstrates that multi-turn formats are feasible and informative, but no existing benchmark in the corpus implements them at scale.

**Contamination exposure.** The moderate-to-high mean contamination risk (B10=2.1) raises concerns about the interpretability of ceiling effects (Finding F3, Section 4.6). When 52% of benchmarks have their complete item sets freely available online, high performance may reflect memorization rather than ethical reasoning capacity. The 7 low-contamination benchmarks (B10=1) should be prioritized for future cross-vendor comparisons.

**Documentation deficit.** Only 8 of 54 benchmarks (14.8%) meet exemplary documentation standards (D6=3). The majority provide minimal or adequate documentation, making it difficult to assess data provenance, annotator qualifications, and intended use limitations. This is consistent with broader concerns about documentation practices in NLP evaluation [Gebru2021; Bender2021].

**The reasoning void, quantified.** Feature E5 provides benchmark-level confirmation of the aggregate finding reported in Claim 4: 63% of benchmarks devote less than 10% of their items to reasoning assessment. The reasoning deficit is not driven by a few outlier benchmarks -- it is a pervasive structural feature of the normative ethics evaluation landscape.

Figures S1 and S2 in the supplementary data archive present the complete distribution of all 15 v2 features across the 54-benchmark corpus. Figure S1 displays feature distributions as parallel histograms organized by axis. Figure S2 presents a 54x15 heatmap showing the v2 feature scores for each benchmark, ordered by composite rank, with gate-passing benchmarks highlighted.

---

*All 54x41 feature scores (26 original + 15 new) are available in the supplementary data archive as machine-readable CSV.*
