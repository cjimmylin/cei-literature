# 4. Results Part I: The Benchmark Landscape

Our multi-signal extraction pipeline identified 292 benchmark candidates from a vault of 2,099 AI ethics papers. All 292 received full 158-feature characterization using the batch-calibrated protocol (Section 3.2), yielding the first comprehensive map of how moral psychology theory is represented---and misrepresented---at every quality level in the LLM evaluation landscape. We present Claims 1--3 here (theoretical distribution, construct validity, and missing theories); Claims 4--5 (human baselines and format mismatch) follow in Sections 4.4--4.5.

## 4.1 MFT Dominance (Claim 1)

Moral Foundations Theory dominates the LLM moral evaluation landscape by every quantitative measure we examined. Of 292 benchmark candidates extracted through multi-signal detection, 67 engage MFT as a primary or substantial secondary framework---nearly 50% more than the next most represented theory (Schwartz values, 44 candidates) and more than double the third (trolley problems, 29 candidates). At every quality tier---top, high, medium, and low---MFT maintains its plurality (Table 5). This pattern persists despite an explicit theory cap designed to limit over-representation: in the top-tier selection, MFT still occupies the plurality of slots because its benchmark infrastructure (MFQ-30, MFTC, MFRC) enables the kind of psychometric grounding that no other theory currently matches.

**Table 5: Theory Representation and Quality Across the Full 292-Candidate Landscape**

| Theory | Total Candidates | Top | High | Med | Low | Quality Rate |
|--------|-----------------|-----|------|-----|-----|-------------|
| MFT | 67 | 18 | 31 | 13 | 5 | **73%** |
| Schwartz | 44 | 4 | 21 | 14 | 5 | 57% |
| Trolley | 29 | 10 | 4 | 10 | 5 | 48% |
| Kohlberg | 9 | 3 | 2 | 2 | 2 | 56% |
| Islamic | 22 | 3 | 5 | 5 | 9 | 36% |
| Social Intuitionism | 3 | 1 | 2 | 0 | 0 | 100% |
| Buddhist | 16 | 1 | 1 | 3 | 11 | 12% |
| Ubuntu | 13 | 0 | 0 | 2 | 11 | 0% |
| Confucian | 13 | 0 | 0 | 0 | 13 | 0% |
| Dyadic Morality | 2 | 0 | 1 | 0 | 1 | 50% |
| Indigenous | 4 | 0 | 0 | 0 | 4 | 0% |
| Identity | 2 | 0 | 0 | 0 | 2 | 0% |

![Figure 1: Top-15 benchmarks by composite score (PD/PE/CI), with theory affiliation indicated by color. MFT-affiliated benchmarks (red) occupy the highest composite positions, reflecting both genuine psychometric quality and the infrastructure advantages described below.](figures/fig1-composite-scores.png)

![Figure 2: Theory distribution across 222 candidates. The area of each region is proportional to candidate count. MFT's 45% share visually dominates the landscape; the three process-oriented theories (dual process, social intuitionism, dyadic morality) collectively account for fewer candidates than MFT's trolley-problem subfield alone.](figures/fig2-theory-distribution.png)

### Two Sources of Dominance

This concentration reflects not a consensus judgment that MFT is the most comprehensive or important theory of moral cognition, but rather MFT's unique position at the intersection of two computational advantages that no other moral psychology theory currently enjoys.

**Infrastructure advantage.** MFT benefits from a mature computational ecosystem that dramatically lowers the barrier to operationalization. The Moral Foundations Questionnaire (MFQ-30; Graham et al. [2011]) provides a standardized, freely available instrument with established scoring procedures, published population norms spanning dozens of countries, and a well-defined five-factor structure that maps cleanly onto classification labels. The Moral Foundations Twitter Corpus (MFTC; Hoover et al. [2020]), with 35,108 expert-annotated tweets across all five foundations, provides a ready-made training set for NLP classifiers. The more recent Moral Foundations Reddit Corpus (MFRC; Trager et al. [2022]) extends this infrastructure to long-form text. No other moral psychology theory offers anything comparable: there is no "Social Intuitionism Questionnaire" with published norms, no "Dual Process Morality Corpus" with labeled examples, and no "Dyadic Morality Twitter Corpus" for training classifiers. Schwartz's PVQ-RR [Schwartz et al., 2012] comes closest, with validated instruments in 49 cultural groups and 53,472 respondents [Schwartz and Cieciuch, 2022], but it lacks the annotated text corpora that enable corpus-based NLP approaches.

**Vocabulary adoption.** Beyond formal instruments, MFT terminology has permeated the NLP and AI ethics literatures as a default vocabulary for discussing moral content in text. The terms "moral foundations," "care/harm," "fairness/cheating," "loyalty/betrayal," "authority/subversion," and "sanctity/degradation" appear routinely in papers that do not engage MFT as a psychological theory but use its foundation labels as convenient category names for moral content classification [Garten et al., 2018; Lin et al., 2018]. This vocabulary adoption inflates MFT's representation in our keyword-based detection: some of the 101 MFT-detected papers use MFT terminology without testing MFT predictions, measuring MFT constructs, or even citing the foundational papers. The distinction between engaging a theory and borrowing its vocabulary is subtle but consequential---it means MFT dominance in the benchmark landscape is partly an artifact of terminological convention rather than a genuine theoretical commitment.

### Consequences of Theoretical Monoculture

The consequences of this skew are threefold. First, an evaluation landscape dominated by MFT measures whether models can detect or reproduce the five moral foundations---but says nothing about whether models exhibit dual-process moral reasoning (the competition between automatic emotional responses and deliberative utilitarian calculation), intuitionist judgment patterns (judgments preceding and surviving the defeat of supporting reasons), or dyadic harm perception (the systematic amplification of moral wrongness when an intentional agent causes suffering to a vulnerable patient). A model that scores well on MFT benchmarks may be fundamentally misaligned on dimensions that MFT does not capture. This is not a hypothetical concern: Goodhart's Law ("when a measure becomes a target, it ceases to be a good measure"; Strathern [1997]) has been documented in other AI evaluation domains [Liang et al., 2023], and the concentration of moral evaluation on a single theory creates precisely the conditions for metric gaming.

Second, MFT is a theory of moral *content*---it describes what people care about (harm, fairness, loyalty, authority, purity) but not *how* moral judgments form in the moment. The field's reliance on content-level evaluation means that fundamental questions about LLM moral *processing*---Does chain-of-thought prompting shift judgments in the direction that dual-process theory predicts? Do LLMs exhibit anything analogous to the intuition-first, reasoning-second pattern that social intuitionism documents in humans? Is moral cognition in LLMs organized around the agent-patient dyad?---remain entirely unaddressed by the existing benchmark landscape.

**The cultural quality cliff.** The tier analysis reveals a second dimension of the monoculture problem that extends beyond the Western psychological theories addressed in Claims 1--3. Four moral traditions with ancient philosophical roots---Ubuntu ethics, Confucian moral philosophy, Indigenous ethical frameworks, and moral identity theory---collectively account for 32 candidates yet achieve zero representation in the top or high quality tiers. Every Ubuntu, Confucian, Indigenous, and moral identity benchmark in the landscape scores in the med or low tier, meaning none meets the minimum threshold for research-grade LLM moral evaluation. This is not primarily a problem of effort: researchers have attempted to build these benchmarks (32 candidates exist). It is a problem of infrastructure: unlike MFT's MFQ-30 and MFTC, these traditions lack standardized validated instruments, large annotated corpora, and established psychometric norms. The consequence is that the question "does this LLM align with Confucian moral values?" cannot currently be answered at a publication-ready standard using any existing benchmark.

Third, MFT was developed primarily through studies of American and Western European populations [Haidt and Joseph, 2004; Graham et al., 2013]. While subsequent work has explored MFT cross-culturally [Atari et al., 2023], the five-foundation taxonomy may not capture moral concerns central to non-Western contexts---Confucian filial piety, Ubuntu's relational ethics, Indigenous conceptions of reciprocity with the natural world. An evaluation landscape built on MFT thus risks encoding a culturally specific moral ontology as the universal standard for LLM alignment.

As we demonstrate in Section 5, this theoretical monoculture is compounded by a measurement monoculture: when we administered 23 benchmarks to 9 models from 3 independent vendors, all models produced indistinguishable moral response profiles on MFT instruments (profile correlations r > 0.98), making the field's reliance on MFT not merely narrow in theoretical coverage but redundant in discriminative power.

## 4.2 Construct Validity Gap (Claim 2)

Construct validity---the degree to which an instrument measures the theoretical construct it purports to measure [Cronbach and Meehl, 1955; Messick, 1995]---is the foundational requirement for interpretable evaluation. If an MFQ-30 score does not reflect moral foundations in the LLM respondent, then "GPT-4 scored higher on Care/Harm than Authority/Subversion" is not a finding about moral cognition; it is a finding about token prediction probabilities that has been dressed in psychological language. The construct validity landscape we document here suggests that this interpretive leap is, for the majority of benchmarks, unjustified.

### The Distribution

The full-coverage distribution reveals a landscape substantially weaker than the pre-selected 55-benchmark sample suggested. The median validity level across all 292 candidates is Level 2 (face validity only)---a full level below the Level 3 median reported in v2.1. More strikingly, 58% of all candidates fall in Level 1 or 2, having either keyword-level engagement with moral psychology (27%) or face validity only (31%). Only 4% achieve multi-study validation, down from 11% when the sample was limited to established benchmarks.

**Table 6: Construct Validity Distribution (A6) — Full 292-Candidate Landscape**

| A6 Score | Interpretation | v2.1 (n=55) | v3.0 (n=292) |
|----------|---------------|-------------|--------------|
| 5 (multi-study) | 100 pts | 6 (11%) | 13 (4%) |
| 4 (single-study) | 75 pts | 20 (36%) | 61 (21%) |
| 3 (adapts w/o LLM revalidation) | 50 pts | 20 (36%) | 49 (17%) |
| 2 (face validity only) | 30 pts | 7 (13%) | 91 (31%) |
| 1 (keyword-level) | 10 pts | 2 (4%) | 78 (27%) |

![Figure 3: Construct validity (A6) score distribution across 55 assessed benchmarks. The modal score of 3 ("adapts without revalidation") characterizes over a third of the landscape. The 6 benchmarks at A6=5 are labeled individually. The gap between the A6=5 cluster and the A6<=3 majority represents the central validity threat documented in this section.](figures/fig5-construct-validity.png)

### The A6=5 Benchmarks: What Validity Looks Like

The six benchmarks achieving A6=5---the highest construct validity rating---share a distinctive provenance: all derive from instruments with decades of psychometric validation in human populations, and all inherit their validity from this lineage rather than establishing it independently for LLM respondents.

1. **The Moral Machine** [Awad et al., 2018]. The most extensively validated instrument in our landscape, with 40 million decisions from participants in 233 countries. Cross-cultural variation patterns---the Western, Eastern, and Southern clusters identified in the original analysis---provide a granular baseline against which LLM responses can be interpreted.

2. **The MFQ-30** [Graham et al., 2011], as administered by Abdulhai et al. [2024]. Population norms spanning political orientations, cultural groups, and age cohorts make each LLM score interpretable relative to identified human populations.

3. **The Moral Foundations Vignettes** [Clifford et al., 2015]. Scenario-based stimuli validated to elicit foundation-specific moral judgments, with published per-vignette norms.

4. **The Defining Issues Test** [Rest, 1979], in its multilingual adaptation [Khandelwal et al., 2024]. Four decades of developmental norms---from adolescents through adults with graduate education---provide the richest developmental baseline in the landscape.

5. **The World Values Survey adaptation** [Benkler et al., 2023]. Seven waves of cross-national survey data (1981--2022) across 100+ countries provide an unmatched longitudinal and cross-cultural baseline for value measurement.

6. **The 45-country trolley replication** [Bago et al., 2022]. A large-scale pre-registered replication of classic trolley dilemmas across diverse cultural contexts, providing unusually robust cross-cultural baselines for utilitarian versus deontological response patterns.

What is notable about this list is what it implies about validity in the LLM evaluation context: every A6=5 benchmark achieves its rating through *inherited* validity from human psychometric research, not through validation specifically conducted for LLM respondents. No benchmark in our landscape has undergone the kind of LLM-specific validation that Messick's [1995] framework would require---demonstrating, for instance, that LLM responses to the MFQ-30 exhibit the same five-factor structure that validates the instrument's interpretation in human populations, or that known manipulations (persona prompting, instruction framing) produce theoretically predicted shifts in LLM scores. The A6=5 benchmarks are the best the field has, but they are valid *for humans*; the extension to LLMs remains an assumption.

### The Modal Case: Adapts Without Revalidation

The 20 benchmarks scoring A6=3 represent the modal pattern in the landscape: researchers take a validated human instrument, administer it to an LLM with minimal adaptation (typically converting the instrument into a prompt), and report results without addressing whether the instrument measures the same construct in a non-human respondent. This "port-and-report" approach treats validity as a property of the instrument rather than of the score interpretation---precisely the error that Messick [1995] cautioned against.

The validity threat is not merely theoretical. When the MFQ-30 asks an LLM to rate "Whether or not someone showed a lack of respect for authority" on a 6-point Likert scale, the response may reflect the statistical distribution of authority-related sentiment in training data, the RLHF reward model's preference for moderate responses, or the model's representation of "what a helpful AI assistant would say about authority"---none of which corresponds to the moral intuition that the MFQ was designed to elicit in human respondents. The finding that LLM MFQ scores shift substantially with persona prompting [Abdulhai et al., 2024]---a manipulation that should not alter genuine moral foundations if they exist as stable dispositions---provides direct evidence that MFQ scores in LLMs reflect something other than what they measure in humans.

Similarly, when the Defining Issues Test asks an LLM to rank the importance of moral considerations in resolving a dilemma, the resulting P-score (proportion of principled moral reasoning) may index the model's familiarity with post-conventional moral arguments in its training data rather than a developmental stage analogous to Rest's [1979] framework. Khandelwal et al. [2024] found that multilingual DIT administration produces different P-scores depending on the language of administration---a finding consistent with training-data composition effects rather than stable moral development. Taken together, these findings suggest that the A6=3 majority of the landscape may be generating scores that are interpretable only as response statistics, not as measurements of moral psychological constructs.

### The Low End: A6=1 and A6=2

The nine benchmarks scoring A6 <= 2 (16% of the assessed landscape) represent the most acute validity concern. The two A6=1 benchmarks engage moral psychology at the keyword level only---using terms like "moral reasoning" or "ethical judgment" without operationalizing any specific construct from the moral psychology literature. The seven A6=2 benchmarks are theory-inspired but lack any formal validation: they draw on moral psychology concepts to design items or scoring criteria, but neither inherit validity from a source instrument nor establish it through independent psychometric analysis.

These benchmarks are not uninformative---they may reveal interesting patterns in LLM behavior. But the patterns they reveal cannot be interpreted in moral psychological terms without committing the construct validity fallacy: treating a score as measuring what the test name suggests, rather than what the evidence supports.

As we show in Section 5, the construct validity gap has an unexpected empirical dimension: when all 9 tested models produce near-identical scores on instruments of varying validity (A6=3 through A6=5), the benchmarks' ability to distinguish between models collapses regardless of their validity level---suggesting that the field faces not only a validation problem but a discrimination problem.

## 4.3 Missing Theories (Claim 3)

The most consequential finding of our meta-evaluation is the near-complete absence of dedicated LLM benchmarks for three major moral psychology theories that collectively represent the field's most influential work on how moral judgments *form*, as distinct from what moral judgments are *about* (Figure 4).

![Figure 4: Theory coverage heatmap showing 8 theories (rows) against 15 selected benchmarks (columns). Color intensity indicates the depth of engagement (A2 operationalization score). The three process-oriented theories---dual process, social intuitionism, and dyadic morality---show near-zero engagement across the entire benchmark set, visualizing the content/process gap documented in this section.](figures/fig3-theory-heatmap.png)

### Dual Process Theory: 0 Dedicated, 9 Partial

Joshua Greene's [2001] dual-process framework---arguably the most influential paradigm in twenty-first-century moral psychology, with over 10,000 citations for the foundational fMRI paper---proposes that moral judgments arise from the competition between two systems: a fast, automatic, emotionally driven process (System 1) that generates characteristically deontological judgments ("don't push the man off the bridge, even to save five"), and a slower, deliberative, cognitively demanding process (System 2) that generates characteristically utilitarian judgments ("push the man to save five lives, maximizing welfare"). The theory's signature predictions are that (a) moral judgments should differ under conditions that differentially engage automatic versus deliberative processing; (b) cognitive load should shift judgments toward deontological responses by impairing System 2; and (c) response time should correlate with judgment type---deontological responses faster, utilitarian responses slower [Greene et al., 2001, 2004, 2008; Greene, 2014].

Before keyword scorer expansion, the vault detected **zero** papers engaging dual-process theory at the threshold level---a result that itself constitutes a finding about the field's theoretical orientation. After expansion, 9 papers were detected, but examination revealed that none constitutes a dedicated benchmark designed to test the theory's core predictions. The closest approximations are:

- **The Staircase of Ethics** [Wu, 2025], which uses multi-step escalating dilemmas that could in principle differentiate System 1 from System 2 responses by increasing deliberative demand across steps. However, the benchmark does not manipulate cognitive load, does not measure response latency, and does not predict response-type differences across steps based on dual-process theory.

- **UniMoral** [Kumar, 2025], which includes dual-process-inspired scenario contrasts across 6 languages. The multilingual dimension is valuable, but the benchmark does not implement the theory's signature manipulation: comparing moral judgments under conditions that differentially engage automatic versus deliberative processing.

- **Several trolley-variant benchmarks** that present personal versus impersonal dilemmas---the manipulation that launched Greene's research program---but score responses for utilitarian/deontological classification rather than testing the process-level predictions that distinguish dual-process theory from content-level accounts.

The absence of a dedicated dual-process benchmark for LLMs is particularly striking because LLMs offer a natural experimental platform for testing the theory. Chain-of-thought prompting provides a direct analog to the deliberation manipulation: if dual-process theory applies to LLMs, then forcing explicit step-by-step reasoning (engaging something analogous to System 2) should shift judgments in the utilitarian direction, while zero-shot prompting (permitting something analogous to System 1 response) should produce more deontological judgments. That no existing benchmark implements this straightforward test suggests that the field has borrowed dual-process theory's *scenarios* (trolley problems) without engaging its *mechanisms* (the competition between automatic and deliberative processing).

### Social Intuitionism: 0 Dedicated, 18 Partial

Jonathan Haidt's [2001] Social Intuitionist Model makes three claims that are at once more philosophically radical and more empirically tractable than they might appear: (a) moral judgments are driven primarily by quick intuitions rather than by deliberative reasoning; (b) moral reasoning typically serves as *post-hoc rationalization*---constructing justifications for judgments already reached; and (c) *moral dumbfounding* occurs when an individual maintains a strong moral judgment even after every stated reason for the judgment has been defeated [Haidt et al., 2000; Haidt, 2001, 2012].

Detection increased from 1 to 18 papers after keyword scorer expansion, but none represents a dedicated benchmark. The 18 partial engagements fall into two categories: papers that invoke Haidt's framework as theoretical context for MFT-based work (conflating Haidt-the-intuitionist with Haidt-the-foundations-theorist), and papers that discuss intuition-versus-reasoning dynamics without implementing an experimental design capable of testing the theory's predictions.

The absence of a moral dumbfounding protocol for LLMs represents a particularly significant gap. The protocol requires sequential probing: (1) present a harmless taboo scenario (e.g., consensual adult sibling incest with no consequences); (2) elicit a moral judgment; (3) elicit reasons; (4) systematically challenge each reason; (5) test whether the judgment persists after all reasons are defeated. This design is well within the capabilities of multi-turn LLM interaction, and the predictions are specific: an LLM trained on human moral discourse should exhibit dumbfounding (maintaining judgments without reasons), because moral dumbfounding is well-documented in the human data the model was trained on. Conversely, an LLM that abandons judgments when reasons are defeated would diverge from human moral psychology in a theoretically interpretable way---and such a divergence would be invisible to any content-level benchmark.

### Dyadic Morality: 0 Dedicated, 7 Partial

Kurt Gray and colleagues [Gray et al., 2012; Schein and Gray, 2018] propose that all moral cognition reduces to the perception of a *moral dyad*: an intentional agent causing suffering to a vulnerable patient. The Theory of Dyadic Morality makes the parsimonious claim that the diversity of moral judgment documented by MFT's five foundations, Schwartz's ten values, and Kohlberg's six stages can be accounted for by a single cognitive template---harm perception---applied with varying sensitivity across persons and situations. The theory's signature prediction is that scenarios will be judged as more morally wrong to the extent that they activate the agent-patient template: clear intentional agents, identifiable vulnerable patients, and perceivable suffering.

Detection increased from 3 to 7 papers after expansion. The closest engagement is the **ValueCompass** framework [2025], which touches on dyadic dimensions in cross-national value assessment. However, no benchmark directly tests the theory's core prediction by systematically manipulating agent-patient dynamics across otherwise matched scenarios.

The Theory of Dyadic Morality is particularly relevant for LLM evaluation because it offers a *structural* account of moral cognition that could serve as a powerful diagnostic. If LLMs systematically rate scenarios as more morally wrong when an intentional agent causes suffering to a patient---independent of MFT foundation, Schwartz value type, or Kohlberg stage---this would suggest that the dyadic template is encoded in the training data's moral discourse. If they do not, this would indicate a fundamental structural difference between human and LLM moral processing that no content-level benchmark could detect.

### Theory Gap Summary

**Table 7: Theory Gap Summary**

| Theory | Key Prediction | Dedicated LLM Benchmarks | Papers Partially Engaging | Core Prediction Tested? | Citation Impact (Google Scholar) |
|--------|---------------|-------------------------|--------------------------|------------------------|--------------------------------|
| Dual Process Theory | Judgments differ under cognitive load vs. deliberation | 0 | 9 | No---no time-pressure, cognitive load, or CoT manipulation | Greene et al. [2001]: ~10,000 |
| Social Intuitionism | Judgments precede reasoning; dumbfounding occurs | 0 | 18 | No---no moral dumbfounding protocol | Haidt [2001]: ~15,000 |
| Dyadic Morality | Agent-patient template drives wrongness perception | 0 | 7 | No---no agent-patient manipulation | Gray et al. [2012]: ~1,500; Schein and Gray [2018]: ~800 |

### Why These Gaps Matter

The significance of these absences extends beyond incomplete theoretical coverage; it reflects a systematic blind spot regarding the *type* of question being asked about LLM moral cognition. Moral psychology distinguishes between content theories (what people care about), process theories (how judgments form), and structural theories (what constitutes a moral event). The current benchmark landscape is almost exclusively oriented toward content. MFT, Schwartz values, and even Kohlberg's stages (as typically operationalized through the DIT) measure the *substance* of moral judgment---which values are endorsed, which principles are invoked, which foundations are activated. The three missing theories address a fundamentally different question: how does the moral judgment *process* work?

This content/process distinction has particular salience for LLMs. When we measure an LLM's MFT profile, we learn which moral content categories the model tends to endorse---but this tells us nothing about the *mechanism* by which those endorsements are generated. Does the model produce care-oriented responses because it has internalized something analogous to a care/harm foundation (as MFT would predict), because it is reproducing the statistical distribution of care-related sentiment in its training data (a confound), or because RLHF reward models preferentially reinforce responses that human raters perceive as caring (an alignment artifact)? Only process-oriented benchmarks---designed to test whether moral judgments shift under conditions that dual-process theory, social intuitionism, and dyadic morality predict should matter---can begin to distinguish these explanations.

The cumulative citation impact of the missing theories underscores the disjunction between their influence within moral psychology and their absence from LLM evaluation. Greene's dual-process papers have accumulated over 10,000 citations; Haidt's social intuitionist model over 15,000. These are not marginal theories---they represent the central paradigms that have organized moral psychology research for the past two decades. Their complete absence from the LLM benchmark landscape is not a gap at the periphery; it is a gap at the center.

As we demonstrate in Section 5, the missing-theories problem interacts with the cross-vendor convergence finding in an unexpected way: the discovery that all 9 tested models produce indistinguishable moral response profiles on existing (content-level) benchmarks makes the absence of process-level benchmarks more urgent, not less. If content-level instruments cannot discriminate between models, only process-level instruments---testing *how* models arrive at moral judgments, not just *which* judgments they produce---have the potential to reveal meaningful differences in moral cognition across architectures, scales, and alignment strategies.
