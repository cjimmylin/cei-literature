---
stem: "2020-Awad-Universals and variations in moral decisions made"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [moral-psychology, cultural-linguistic, pluralism-aggregation, validity-psychometrics]
task_format: "forced-choice"
scoring_type: "behavioral"
dataset_size: 70000
dataset_construction: "crowdsourced"
languages: ["ar", "zh", "en", "fr", "de", "ja", "ko", "pt", "ru", "es"]
models_tested: []
headline_numbers:
  - "70,000 participants in 10 languages and 42 countries (p.1)"
  - "Universal Switch > Loop > Footbridge ordering held in all 42 countries (p.3)"
  - "Country-level average: Switch 81%, Loop 72%, Footbridge 51% endorsement of sacrifice (p.3)"
  - "Relational mobility correlated with Switch sacrifice: r=0.67, p<0.001 (p.4)"
  - "Asian countries: relational mobility correlation with Switch = 0.95, p=0.004 (p.4)"
---
## 1. Gist
This PNAS paper reports the largest cross-cultural study of moral preferences in sacrificial trolley dilemmas, using data from 70,000 participants in 10 languages and 42 countries collected via the "Classic" mode of the Moral Machine website. The key findings are: (1) the qualitative ordering Switch > Loop > Footbridge in sacrifice acceptability is universal across all 42 countries, suggesting a common cognitive structure; (2) absolute levels of sacrifice endorsement show substantial country-level variation, with a strong association with relational mobility (a socioecological variable measuring how easily people develop new relationships). For values-alignment benchmarking, the paper establishes a foundational empirical baseline for cultural universals and variation in moral judgment, and provides an open dataset and methodology for cross-cultural moral evaluation at scale.

## 2. Benchmark/eval design features
A cross-cultural behavioral dataset rather than an AI model benchmark. Key design elements:
- Three classic trolley problem variants: Switch (redirect trolley to kill 1 instead of 5, death is incidental), Loop (redirect to kill 1 whose body stops trolley, death is instrumental but no personal force), Footbridge (push large person off bridge, death is instrumental and requires personal force).
- Stimuli presented in graphical form with accompanying text (shown in Materials and Methods section, p.5).
- Each user completes all three scenarios in random order.
- Minimum 200 responses per scenario per country required for inclusion.
- Data collected June 2017–March 2019 (20 months).
- Open dataset deposited on Open Science Framework.

The two main theoretical objectives: (1) confirm universality of Switch–Loop–Footbridge qualitative ordering; (2) document cultural predictors of quantitative sacrifice acceptance, specifically relational mobility.

## 3. Task format & example item
Forced choice: "What should the man in blue do?" — presented with two images showing both possible outcomes plus a text description. Verbatim item texts from the Materials section:

Switch: "A man in blue is standing by the railroad tracks when he notices an empty boxcar rolling out of control...If the man in blue flips a switch next to him, it will divert the boxcar to the side track where it will hit the one person, and not hit the five people on the main track." (p.5)

Footbridge: "...There is a large person standing near the man in blue on the footbridge, and this large person weighs enough that the boxcar would slow down if it hit him...If the man in blue pushes the one person, that one person will fall onto the track..." (p.5)

## 4. Scoring / grading methodology
- Binary proportion of participants endorsing sacrifice in each scenario variant.
- Country-level analysis: averages per country per scenario.
- Funnel plots used to assess convergence of effect sizes as a function of sample size.
- Regression models: relational mobility as predictor of sacrifice endorsement, controlling for individualism, GDP, and religiosity.
- Effect sizes: Cohen's h for scenario differences.

## 5. Dataset construction & provenance
- Source: Moral Machine website Classic mode (moralmachine.mit.edu), deployed June 2017.
- 70,000 participants total; 42 countries with n ≥ 200 per scenario per country.
- 10 languages: Arabic, Chinese, English, French, German, Japanese, Korean, Portuguese, Russian, Spanish (translation and back-translation process).
- Country identified via IP geolocation.
- Optional demographic survey completed by ~20,000 users: 75% male, 75% under 32, 73% college-educated, politically left-leaning, religiously secular.
- Sample is a self-selected convenience sample — acknowledged limitation.
- Data and code deposited on Open Science Framework (https://bit.ly/2Y7Brr9).
- Creative Commons Attribution License 4.0.

## 6. Validity evidence
- Convergent validity: Switch–Loop–Footbridge ordering replicated across all 42 countries and consistent with prior smaller studies.
- Funnel plot analysis shows Switch–Loop difference converges to effect size ~0.10 as sample increases, suggesting homogeneity; Loop–Footbridge shows increasing heterogeneity with sample size, suggesting genuine cultural variation.
- Regression robustness: relational mobility predicts sacrifice endorsement controlling for individualism, GDP, and religiosity (p.4).
- Correlation especially strong in Asian subsample: r = 0.95 (Switch), 0.83 (Loop), 0.93 (Footbridge).
- Limitation: relational mobility scores not available for all 42 countries.

## 7. Saturation / discrimination
The instrument shows strong discrimination: country-level averages range widely (e.g., China and Japan among the lowest sacrifice endorsers; US among the highest within its comparison group). The Switch–Loop difference has a small effect size (~Cohen's h = 0.10) suggesting limited discrimination between these two scenarios; the Loop–Footbridge difference is larger and culturally variable. No ceiling effect: Footbridge endorsement averages ~51%, leaving room above and below.

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- Participants: 70,000 (p.1)
- Countries: 42 (p.1)
- Languages: 10 (p.1)
- Country-level averages: Switch 81%, Loop 72%, Footbridge 51% sacrifice endorsement (p.3)
- Switch–Loop effect size: Cohen's h ≈ 0.10 (p.3)
- Relational mobility — Switch correlation: r(21) = 0.67, p < 0.001 (p.4)
- Relational mobility — Loop: r(21) = 0.56, p = 0.005 (p.4)
- Relational mobility — Footbridge: r(21) = 0.64, p < 0.001 (p.4)
- Asian subsample: relational mobility × Switch = 0.95, p = 0.004 (p.4)
- Survey takers: ~20,000 (optional subset) (p.5)
- Survey composition: 75% male, 75% < 32 years, 73% college-educated (p.5)
- Data collection period: June 2017–March 2019 (p.5)

## 10. Pitfalls & limitations
- Strong self-selection bias: ~36% of survey takers were young, college-educated men (p.5); population not nationally representative.
- Viral online design may over-represent those motivated by the topic (tech-literate, ethically interested).
- Relational mobility data not available for all 42 countries, limiting analysis.
- Some scenarios elicited very small samples in certain countries.
- Binary forced-choice does not capture degree of endorsement or moral uncertainty.
- Western vs. Eastern framing may be oversimplified; paper explicitly shows large within-region variation (p.4).
- Hypothetical stated preferences may diverge from actual behavior in real dilemmas.

## 11. Novel ideas worth stealing
- **Funnel plot methodology for cross-cultural homogeneity testing**: plotting effect size against sample size across countries reveals whether between-country variability is sampling noise (converges) or genuine cultural signal (diverges with larger n) — a rigorous approach to distinguishing universal from culturally specific moral judgments in benchmark validation.
- **Qualitative ordering as universality claim**: documenting that a rank ordering of moral acceptability holds in every country is a weaker and more defensible universality claim than claiming a specific numeric level; useful for structuring cross-cultural benchmark standards.
- **Open dataset with public use license**: releasing all responses for researchers to conduct new analyses with new country-level variables is a high-impact knowledge contribution; benchmark developers should follow suit.
- **Relational mobility as a benchmark moderator**: including socioecological moderators when reporting cross-cultural benchmark results goes beyond simple country averages and provides theoretically grounded explanations for variance.
- **Comparing public preferences to expert guidelines**: the direct comparison of MM public preferences to the German AV ethics committee guidelines reveals specific points of disagreement (e.g., age discrimination) — a template for using crowdsourced preference data to audit expert-authored AI guidelines.
- **Multi-scenario within-session design**: having the same participant respond to all three variants (Switch, Loop, Footbridge) within one session enables within-person consistency analysis, which is more informative than purely between-person designs.

## 12. Notable quotes
- "In every country, the three dilemmas displayed the same qualitative ordering of sacrifice acceptability, suggesting that this ordering is best explained by basic cognitive processes rather than cultural norms." (p.1)
- "The quantitative acceptability of each sacrifice, however, showed substantial country-level variations." (p.1)
- "Low relational mobility (where people are more cautious about not alienating their current social partners) is strongly associated with the rejection of sacrifices for the greater good." (p.1)
- "Our sample is large but by no means ideal. We relied on voluntary participation in a viral online experiment, and our sample shows clear signs of self-selection." (p.4–5)

## 13. UNKNOWN / not in extract
- Exact relational mobility scores for each country used in the analysis.
- Full regression coefficient tables (referenced as Fig. 4B but not reproduced verbatim from tables in the extract).
- SI Appendix contents, including zero-order correlations with additional country-level variables (cultural looseness, rule of law, national IQ, military targeting).
- Whether utilitarian vs. deontological individual-level tendencies moderated the relational-mobility association.
- Power analysis justifying the 200-response-per-country threshold.
