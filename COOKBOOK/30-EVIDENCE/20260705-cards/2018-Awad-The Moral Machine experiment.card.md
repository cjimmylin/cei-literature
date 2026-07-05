---
stem: "2018-Awad-The Moral Machine experiment"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, cultural-linguistic, pluralism-aggregation, normative-ethics]
task_format: "forced-choice"
scoring_type: "behavioral"
dataset_size: 39610000
dataset_construction: "crowdsourced"
languages: ["en", "ar", "zh", "fr", "de", "ja", "ko", "pt", "ru", "es"]
models_tested: []
headline_numbers:
  - "39.61 million decisions collected from over 2.3 million people in 233 countries (p.4)"
  - "Strongest preferences: sparing humans over animals, sparing more lives, sparing young lives (p.5)"
  - "Three moral clusters identified: Western, Eastern, Southern (p.7)"
  - "Cultural distance from US correlates with Moral Machine distance at ρ = 0.49 (p.9)"
  - "N = 492,921 users completed the optional demographic survey (p.7)"
  - "Individual demographic variations had no sizable impact on any preference (all below 0.1) (p.7)"
---
## 1. Gist
The Moral Machine experiment is a landmark large-scale empirical study of cross-cultural moral preferences regarding autonomous vehicle (AV) ethical dilemmas. Awad et al. deployed an online "serious game" that presents forced-choice trolley-problem variants — users select which outcome an AV should produce when a crash is unavoidable. Collecting 39.61 million decisions from 2.3+ million participants across 233 countries and territories in ten languages, the study quantifies global, demographic, and cultural moral preferences across nine dimensions (sparing humans vs. pets, more vs. fewer lives, young vs. old, lawful vs. jaywalking pedestrians, passengers vs. pedestrians, males vs. females, fit vs. unfit, high vs. low social status, staying course vs. swerving). The paper is foundational for values-alignment benchmarking because it demonstrates both that broad cross-cultural consensus exists on some moral dimensions (sparing lives, sparing the young, sparing humans) and that significant cross-cultural divergence exists on others, posing real obstacles to universal machine ethics. It also validates a scalable crowdsourcing methodology for eliciting moral preferences at global scale.

## 2. Benchmark/eval design features
The Moral Machine is a 9-factorial conjoint experiment embedded in a viral online platform. Nine binary preference dimensions are simultaneously varied across scenarios presented as graphical two-outcome crash dilemmas. The platform uses a purposive exploration strategy to efficiently sample the approximately 26 million possible dilemma configurations; within a session of 13 dilemmas, 12 are drawn from this design space and one is entirely random. Preference measurement uses Average Marginal Component Effect (AMCE) computed via conjoint analysis — this yields the probability difference of sparing a character type aggregated over all other attributes.

Core findings: (1) Global preferences favor sparing humans over animals, more lives over fewer, and younger characters — these are identified as candidate building blocks for machine ethics. (2) Weaker preferences exist for sparing pedestrians, females, the fit, and the lawful; these are more culturally contested. (3) Hierarchical clustering of 130 countries (≥100 respondents each) reveals three clusters — Western (North America + Protestant/Catholic/Orthodox Europe), Eastern (Confucian + Islamic countries), and Southern (Latin America + French-influenced territories). (4) Country-level cultural/economic variables (individualism, GDP, Gini coefficient, rule of law, gender-health gap) predict Moral Machine preferences.

## 3. Task format & example item
Forced-choice dilemma: the AV has brake failure and must either stay on course or swerve. Each outcome kills a group of 1–5 characters.

From the paper (p.4): "Staying on course would result in the death of two elderly men and an elderly woman, crossing on a 'do not cross' signal (left). Swerving would result in the death of three passengers, an adult man, an adult woman, and a boy (right)."

The user clicks their preferred outcome in response to the question "What should the self-driving car do?" A "see description" button provides full text of the characters and their fates.

## 4. Scoring / grading methodology
Decisions are logged per user per dilemma. Analysis uses conjoint analysis to compute Average Marginal Component Effects (AMCEs): the difference in probability of sparing characters with attribute X versus attribute Y, averaged over the joint distribution of all other attributes. For individual variation analysis, regression-based estimators of each of the nine preference dimensions are computed with six demographic variables (age, education, gender, income, political views, religiosity) as covariates. For cultural clustering, each country's 9 AMCEs are standardized and subjected to hierarchical clustering (Euclidean distance, Ward variance minimization). Country-level correlates use Spearman's ρ.

## 5. Dataset construction & provenance
The Moral Machine website was deployed in June 2016. Demographic survey functionality added October 2016. Translated progressively into nine additional languages (November 2016–March 2017): Arabic, Chinese, French, German, Japanese, Korean, Portuguese, Russian, Spanish. Participants are geolocated via IP address. Data collection is self-selected and Internet-based; the sample over-represents tech-savvy, Internet-connected populations. 130 countries with ≥100 respondents were selected for the clustering analysis (range: 101–448,125 respondents per country). All data are publicly available at https://goo.gl/JXRrBP. The paper reports post-stratification analyses to address sample non-representativeness (details in SI).

## 6. Validity evidence
External validity is supported by substantial correlation (ρ = 0.49) between cultural distance from the US (World Values Survey-based) and Moral Machine moral distance from the US (p.9). The three identified cultural clusters are broadly consistent with the Inglehart-Welzel Cultural Map 2010–2014. Country-level economic and institutional variables (GDP, Gini, Rule of Law, gender health gap, individualism) predict Moral Machine preferences in theoretically coherent directions. Robustness of the clustering was verified by restricting to participants who used only pictorial (not textual) representations (p.9). Post-stratification analyses reported in supplementary information. No human baseline or inter-rater reliability figures are reported (not applicable given the design).

## 7. Saturation / discrimination
The design achieves very tight confidence intervals given N = 39.61 million decisions — 95% CIs for AMCEs are described as "insignificant width" (p.5). Strong preferences (humans over animals, more lives, young lives) are clearly distinguishable from weak preferences (pedestrians vs. passengers, staying on course). Some preferences (gender, social status) show substantial cross-cultural variation, meaning they are discriminating at the country level. The nine-dimension design prevents ceiling effects by presenting multi-factor scenarios where preferences compete.

## 8. Multiturn / agentic aspects
n/a. The task is a single-session series of independent forced-choice dilemmas. Users can complete additional sessions but each dilemma is statistically independent.

## 9. Key numbers
- 39.61 million decisions collected (p.4)
- 2.3 million+ participants from 233 countries/territories (p.2)
- 10 languages (p.4)
- 13 dilemmas per session; 12 drawn from ~26 million possible configurations (p.14)
- 492,921 users completed optional demographic survey (p.7)
- 130 countries selected for clustering analysis (≥100 respondents each) (p.7)
- Strongest AMCE for age: probability of sparing young is 0.49 (SE = 0.0008) greater than sparing older (p.5)
- Individual demographic impacts all below 0.1 on any attribute (p.7)
- Cultural distance correlation: ρ = 0.49 (p.9)
- 3 major cultural clusters: Western, Eastern, Southern (p.7)

## 10. Pitfalls & limitations
**Author-admitted:** (1) Self-selected, non-representative sample — skews toward Internet-connected, tech-savvy populations, not nationally representative. (2) No uncertainty about character classification or outcomes — all death/survival outcomes are 100% certain, which is technologically unrealistic. (3) No manipulation of respondent–character relationship (relatives, spouses). (4) Preferences captured before AV deployment; may change once AVs make real ethical decisions with identified victims. (5) Cannot do justice to all complexity of AV dilemmas even at this scale.

**Additional observations:** (1) The nine dimensions were preselected by researchers, potentially missing other morally relevant dimensions. (2) The gaming/viral deployment mode may attract self-selected populations with specific moral views or gaming motivations. (3) The forced-choice format does not capture indifference or principled abstention. (4) No AI/LLM models were tested — this is human preference data for informing AI ethics, not an evaluation of AI moral reasoning.

## 11. Novel ideas worth stealing
1. **Conjoint AMCE design for moral preferences**: The 9-factorial conjoint design with AMCE as the primary statistic is directly transferable to LLM moral benchmarks. Instead of asking a model to rate scenarios, vary attributes systematically and measure response probability differences — this decouples effects cleanly and handles confounding.

2. **Session-level exploration strategy**: The algorithm that samples ~26 million possible dilemmas while ensuring no repetition within a user session could be applied to LLM evaluation — dynamically generate diverse items rather than a fixed test set to prevent memorization.

3. **Post-session summary with social comparison**: Showing participants how their decisions compare to the global average drives engagement and sharing (viral growth). For LLM evals, a similar "model vs. human distribution" visualization could drive adoption.

4. **Multilingual deployment from the start**: Running the platform in 10 languages allows cultural-linguistic decomposition. Values-alignment benchmarks should do this systematically rather than defaulting to English.

5. **Country-level cultural predictor analysis**: Linking benchmark results to external cultural indicators (Hofstede, World Values Survey, Gini, Rule of Law) validates the benchmark and reveals drivers. Any cross-cultural values benchmark should include this external correlation step.

6. **Three-cluster moral geography**: The Western/Eastern/Southern taxonomy is a ready-made stratification variable for sampling participants or interpreting between-group differences in future cultural benchmarks.

7. **Pictorial vs. textual version as robustness check**: The finding that clusters are stable even when only pictorial descriptions were used (excluding language effects) is a methodological template for separating content from linguistic framing.

## 12. Notable quotes
- "Never in the history of humanity have we allowed a machine to autonomously decide who should live and who should die, in a fraction of a second, outside of real-time supervision." (p.11)
- "Any attempt to devise AI ethics must be at least cognizant of public morality." (p.3)
- "Our data helped us identify three strong preferences that can serve as building blocks for discussions of universal machine ethics, even if they are not ultimately endorsed by policymakers: the preference for sparing human lives, the preference for sparing more lives, and the preference for sparing young lives." (p.12)
- "We might not reach universal agreement: even the strongest preferences expressed through the Moral Machine showed substantial cultural variations." (p.12)

## 13. UNKNOWN / not in extract
- Full supplementary information details (robustness checks, post-stratification analysis, regression tables S3)
- Exact breakdown of decisions by country (only partial information in extract)
- Details of the dilemma generation algorithm beyond what is described in Methods
- Whether demographic survey was completed before or after viewing the session summary (described as randomized but no split reported)
- Specific IRB approval protocol details beyond MIT approval statement
