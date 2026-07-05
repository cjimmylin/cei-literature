---
stem: "2023-Maile-The choice of deontological, virtue ethical, and"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, moral-psychology, design-space]
task_format: "forced-choice"
scoring_type: "human-rating"
dataset_size: 571
dataset_construction: "survey-derived"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Deontological reasoning was most often chosen overall: 47.9% (p.11)"
  - "Virtue ethical reasoning was second: 36.6% overall (p.16)"
  - "N = 571 pre- and in-service UK police officers completed the survey (p.7)"
  - "93.7% of experienced officers (Cohort 3) chose to oppose colleague and insist on positive action in domestic violence dilemma (p.11)"
  - "Degree-educated participants significantly more likely to use virtue ethical reasoning (Mann-Whitney U p < .001, rank biserial effect size .2055) (p.15)"
---
## 1. Gist
This empirical study by Maile et al. (2023) investigates which moral reasoning strategies—deontological, virtue ethical, or consequentialist—are preferred by 571 pre- and in-service UK police officers when responding to work-relevant ethical dilemmas. Using a cross-sectional online survey with six police-specific moral dilemmas, the study finds that deontological (rule-based) reasoning dominates (47.9%), followed by virtue ethical (36.6%), with consequentialist approaches rare. Importantly, officers with undergraduate degrees show significantly higher rates of virtue ethical and consequentialist-utilitarian reasoning. For values-alignment benchmarking, this paper is relevant as a real-world empirical mapping of which ethical frameworks professionals actually invoke in specific dilemmatic contexts—directly informing how benchmark items should be constructed and how responses should be coded for ethical frameworks.

## 2. Benchmark/eval design features
Not a benchmark for AI systems. Rather, an empirical moral psychology study using six police-specific ethical dilemmas. Key design features:

- **Six hypothetical ethical dilemmas** collaboratively designed with an Expert Panel, representing realistic scenarios of police work: domestic violence, murder investigation (PACE violation), whistleblowing on racism, plus three others (detailed results available online)
- **Forced-choice response structure**: Each dilemma offers two action options, each with six pre-coded justifications: two deontological, two virtue ethical, one consequentialist-utilitarian, one consequentialist-self-serving
- **Ranking of top three justifications**: Participants rank their top 3 reasons (scored 3/2/1), allowing frequency and magnitude of preference
- **Cross-cohort design**: Three cohorts—first-year pre-join students/PCDAs, second-year students/experienced PCDAs, experienced officers (≥5 years)
- **Comparison with other professions**: Results on the whistleblowing dilemma are compared to prior studies of doctors, teachers, nurses, lawyers, and business/finance professionals from the same research center

## 3. Task format & example item
Forced-choice dilemma with ranked justification selection. Example (domestic violence dilemma, p.8):

"You and another officer are sent to a 999 call from a female caller, who states that her partner is acting aggressively. On arrival, it is apparent that the woman is uninjured, but the woman's partner has a black eye. The partner says that 'he deserved it' because he was acting like a fool. The Force policy is that 'positive action' must be taken in all domestic violence cases. Your colleague says to you that because there had been no prior calls, the victim did not want to press charges and the woman had been the complainant to 999, then this call is best resolved by giving an informal resolution. [...] What would you do?" Options: (1) Oppose colleague and insist on arrest; (2) Agree on informal resolution. Followed by six pre-coded justifications to rank.

## 4. Scoring / grading methodology
Justifications selected first = 3 points, second = 2 points, third = 1 point. Total scores per justification summed across all respondents; percentage of total score shown per reason. Final analysis reports frequency of each ethical reasoning type (deontological, virtue ethical, consequentialist-utilitarian, consequentialist-self-serving) as percentage of weighted selections. Inferential analysis uses Mann-Whitney U tests (non-parametric, given Shapiro-Wilk and Levene violations) to compare reasoning strategies between degree-holders and non-degree-holders.

## 5. Dataset construction & provenance
N = 571 adult participants: Cohort 1 (n=110 first-year students/PCDAs), Cohort 2 (n=126 second-year+), Cohort 3 (n=335 experienced officers). 3.5% BAME; mean age 35.83 (SD=13.23); 30.7% female. Recruited through ethics committee leads at 43 UK police forces and 12 universities (out of 36 CoP-accredited institutions). Self-selected, voluntary participation. 361 incomplete surveys excluded. Survey instrument derived from prior work on character virtues in professions (Arthur & Earl, 2020). Ethical approval from University of Birmingham Ethics Committee (ERN_20-1635).

## 6. Validity evidence
- Dilemmas co-designed with Expert Panel (named in acknowledgments); reviewed for face validity by practitioners
- Derives from neo-Kohlbergian moral psychology tradition (Rest et al., 1999) for measuring moral reasoning via hypothetical scenarios
- Cross-professional comparison validates discriminant validity: police show higher deontological rates than most professions but similar to nurses
- Shapiro-Wilk and Levene tests conducted prior to inferential analysis; appropriate non-parametric tests used
- Bayes factors reported alongside p-values (Bayes factor for virtue ethical difference = 467.455, very strong evidence) (p.15)
- Limitation: self-report; social desirability, self-confirmation, and self-deception biases acknowledged

## 7. Saturation / discrimination
The scale discriminates well between cohorts and education levels. The degree-education effect is statistically strong for virtue ethical reasoning (p < .001, effect size .2055) but not for deontological (p = .148). The three dilemmas analyzed show different dominant ethical frameworks, demonstrating item-level discrimination. Self-serving consequentialist reasoning is very rare throughout (1–3%), indicating floor effects for that category.

## 8. Multiturn / agentic aspects
n/a. Single-turn hypothetical scenario responses.

## 9. Key numbers
- N = 571 total participants; 110 Cohort 1, 126 Cohort 2, 335 Cohort 3 (p.7)
- 361 incomplete surveys excluded (p.7)
- 3.5% BAME; mean age 35.83 (SD=13.23); 30.7% female (p.7)
- Overall moral reasoning: deontological 47.9%, virtue ethical 36.6% (p.11, p.16)
- 93.7% of Cohort 3 chose to oppose colleague (domestic violence) (p.11)
- 85.1% of Cohort 3 judged it wrong to violate PACE (murder investigation) (p.12)
- 61.4% overall chose private word over formal reporting (racism dilemma) (p.12)
- 52.5% deontological justification for Option 2 in murder dilemma (p.12)
- Virtue ethical Mann-Whitney U = 33,645, p < .001, rank biserial = .2055 (p.15)
- Bayes factor for virtue ethical difference = 467.455 (p.15)
- Degree-holders: VE Mdn=14, non-degree: VE Mdn=12 (p.15–16)

## 10. Pitfalls & limitations
- Self-selection bias; participants likely more interested in ethics than average officer
- Self-report measures subject to social desirability, self-confirmation, and self-deception bias
- Cross-sectional design cannot establish causality; education difference may reflect selection effects not development
- Three of six dilemmas not fully reported in paper (available online supplement)
- Does not capture actual behavior, only stated reasoning preferences
- UK-specific context limits generalizability
- The coded justifications constrain response options; participants may have had reasoning not captured by any of the six options
- Demographic underrepresentation: only 3.5% BAME vs. 7.6% in actual workforce

## 11. Novel ideas worth stealing
1. **Paired action + justification design**: For each dilemma, requiring participants to (a) choose an action and (b) rank their justifications from a theory-coded list provides richer data than either alone. Values-alignment benchmarks could adopt this structure: not just "what would you/the AI do?" but "why?"
2. **Theory-coded forced-choice justifications**: Pre-coding justifications into ethical frameworks (deontological, virtue ethical, consequentialist-utilitarian, self-serving) allows quantitative measurement of ethical theory usage. Directly applicable to coding LLM outputs by ethical framework.
3. **Rank-weighted scoring**: Scoring first-choice = 3, second = 2, third = 1 allows nuanced measurement of preference strength beyond binary selection.
4. **Cross-professional comparison design**: Including comparison groups from other professions contextualizes findings and enables discriminant validity checks.
5. **Phronesis as the target construct**: The paper argues that the real goal is developing practical wisdom (phronesis)—context-sensitive, discretionary moral reasoning. Benchmarks that only test rule-following miss this dimension entirely.
6. **Dilemma co-design with Expert Panel**: Involving domain practitioners in dilemma creation increases ecological validity—a design principle applicable to LLM ethics benchmarks.

## 12. Notable quotes
- "The dominant form of moral reasoning in dealing with those dilemmas was deontological (rule-based). The second most frequently selected reasoning strategy was virtue ethical." (p.2)
- "The finding that graduates are more likely than non-graduates to make use of virtue ethical reasoning in their handling of ethical dilemmas is encouraging for those who are sympathetic to virtue ethics." (p.17)
- "Only by delving carefully into the combinations of action choices and theoretical motivations can we begin to understand what drives the moral behavior of police officers and how/why they are likely to respond in similar situations in the future." (p.17)
- "The overarching duty of the police officer is to uphold the 'Queen's Peace.' However, that concept is not a legally operationalizable one... it is a matter for determination through police phronesis." (p.4)

## 13. UNKNOWN / not in extract
- Full results for the three remaining dilemmas (available online at jubileecentre.ac.uk/policing but not in extract)
- Interview data from qualitative follow-up (Maile et al., under submission)
- Details of the expert panel beyond names in acknowledgments
- Whether any AI systems were used in the study
- Whether the survey instrument is publicly available in full
