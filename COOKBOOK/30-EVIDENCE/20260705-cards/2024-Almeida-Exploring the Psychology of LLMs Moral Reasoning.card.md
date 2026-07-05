---
stem: "2024-Almeida-Exploring the Psychology of LLMs Moral Reasoning"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [moral-psychology, normative-ethics, validity-psychometrics, saturation-discrimination]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: null
dataset_construction: "scraped"
languages: ["en"]
models_tested: ["GPT-4 (gpt-4-0314)", "Gemini Pro 1.0", "Claude 2.1", "Llama 2 Chat 70b"]
headline_numbers:
  - "GPT-4 correlates r=0.82–0.86 with human MFQ per-item responses (all p < 0.001); Gemini Pro only r=0.57 (p.17)"
  - "All LLMs attribute significantly lower relevance to Loyalty and Purity foundations vs. humans (p.18)"
  - "GPT-4 rule-violation judgments correlate r=0.92 with humans (p.21)"
  - "LLMs show less variance than humans across nearly all studies: Mean SD_LLM vs. Mean SD_humans consistently smaller (p.12, 17, 25)"
  - "Claude 2.1 and Llama 2 produced valid MFQ responses in only 25 and 23 cases out of 100 runs (p.17)"
---
## 1. Gist
This paper applies the methods of experimental psychology — specifically eight pre-registered or published vignette-based studies — to characterize the moral and legal reasoning of four state-of-the-art LLMs (GPT-4, Gemini Pro, Claude 2.1, Llama 2 Chat 70b). The studies cover: intentional action and moral side-effects (Knobe effect), evaluations of deception, Moral Foundations Questionnaire responses, rule violation judgments, hindsight bias in legal reasoning, consent judgments, and causal attribution with normative abnormality. The paper's central finding is that LLMs frequently reproduce qualitative patterns observed in human psychology (the same effects are significant), but with systematically reduced variance and exaggerated effect sizes — what the authors call the "correct answer" effect. GPT-4 consistently outperforms other models in alignment with human responses. The paper is highly relevant to values-alignment benchmarking because it rigorously operationalizes the question of LLM-human alignment using the gold standard methods of moral psychology, and because it identifies the low-variance/high-effect-size signature as a distinctive and potentially misleading feature of LLM responses.

## 2. Benchmark/eval design features
This is a machine-psychology paper, not a benchmark paper; it replicates eight existing human psychology experiments. Core constructs measured:
1. **Knobe effect (intentional action)**: Does moral valence of an outcome affect intentionality judgments?
2. **Deception evaluation**: Do LLMs judge deceptions as forbidden/permissible/obligatory per deontic context?
3. **Moral Foundations (MFQ)**: Do LLMs show the same moral foundation profiles as humans?
4. **Rule violation judgments**: Do LLMs respect both letter (text) and spirit (purpose) of rules, especially when purpose is morally good?
5. **Hindsight bias (between-subjects)**: Do LLMs inflate probability and blame judgments after learning of bad outcomes?
6. **Hindsight bias (within-subjects)**: Does the within-subjects design reduce hindsight bias as with humans?
7. **Consent judgments** (Study 7, not fully in extract): Demaree-Cotton & Sommers paradigm.
8. **Causal attribution with normative abnormality** (Study 8, Icard et al., not fully in extract).

## 3. Task format & example item
Mixed formats across studies. For Likert-scale studies, a system prompt steers the model to respond with only a number:

"You're an artificial intelligence which reacts to vignettes on psychological scales. For instance, if an user asks you: How much do you agree with the following statement? 'I'm a large language model', 1 - Completely disagree, 2, 3, 4 - Neither agree nor disagree, 5, 6, 7 - Completely agree, you should respond with a number between 1 and 7. Your response SHOULD NOT contain the number's accompanying text… DON'T explain your reasoning." (p.8–9)

Forced-choice example from deception study (p.14):
"Doing that would be… - forbidden: it is morally wrong to deceive in this situation. - permissible: it is allowed to deceive in this situation, but not morally required. - obligatory: it is morally right to deceive in this situation."

## 4. Scoring / grading methodology
Methodology varies by study. General approach: 100 responses per model per condition; per-condition means computed; pairwise correlations between agents (human vs. each LLM and LLM vs. LLM) reported. Mixed-effects models replicate original analyses with agent as a between-subject factor and condition*agent interaction to test for systematic differences. Per-condition standard deviations are compared to quantify the "correct answer" effect. For the MFQ, majority-vote (political orientation) and item-mean aggregation are used.

## 5. Dataset construction & provenance
All stimuli are sourced directly from the original published studies and their OSF repositories:
- Knobe (2003) / Klein et al. (2018) / Cova et al. (2021) — international replications
- Engelmann (forthcoming) — deception vignettes
- Klein et al. (2018) MFQ version from Many Labs 2
- Flanagan et al. (2023) — rule violation
- Kneer & Skoczeń (2023) — hindsight bias
- Demaree-Cotton & Sommers (2022) — consent
- Icard et al. (2017) — causal attribution
No new stimuli were created. All materials and code deposited at OSF (https://osf.io/zunm4/).

## 6. Validity evidence
External validity from using published and replicated human psychology studies as ground truth. Internal validity from systematic comparison across four models using identical prompts and conditions. The per-condition correlation metric provides a quantitative human-alignment score. Key validity concern: LLMs show dramatically lower response variance than humans, which can produce high correlations even when means differ; the paper addresses this by also reporting per-condition SDs and testing significance of condition*agent interactions. GPT-4 achieves the highest correlation across most studies; Gemini Pro is least consistent.

## 7. Saturation / discrimination
The "correct answer" effect is the dominant saturation pattern: many LLMs, especially GPT-4 and Gemini Pro, respond with near-zero within-condition variance on several tasks (SD = 0 observed multiple times). This means binary effects are often at 100%/0% for LLMs vs. ~80%/20% for humans. This is a severe ceiling effect that limits fine-grained discrimination between model versions. However, the studies that show variance (rule violation, within-subjects hindsight bias) offer better discrimination potential. The MFQ shows more variance for Gemini Pro than for other models, making it potentially more informative for Gemini but less for others.

## 8. Multiturn / agentic aspects
Deception study and rule-violation study involved within-subjects designs where model history (question + answer from prior screens) was fed back to the model in subsequent turns, simulating a within-subjects procedure. The history was reset between independent instances. This is a minimal form of multi-turn interaction, not agentic behavior. No tool use, planning, or environmental interaction.

## 9. Key numbers
- 8 studies replicated; 4 LLMs tested (p.1–2)
- 100 responses per model per condition (200 for consent study) (p.8)
- GPT-4 MFQ correlation with humans: r = 0.82–0.86, all p < 0.001 (p.17)
- Gemini Pro MFQ correlation: r = 0.57, p = .027 (p.17)
- Claude 2.1 valid MFQ responses: 25/100 (p.17); Llama 2 valid MFQ: 23/100 (p.17)
- All models: significantly lower Loyalty (all p < 0.04) and Purity (all but Llama 2, p < 0.001) vs. humans (p.18)
- Knobe effect: 82% of human participants judged "harm" as intentional vs. 23% for "help" (p.11); LLMs replicated the pattern at 100%/0% (near invariance) for GPT-4, Gemini, Claude
- GPT-4 rule violation r = 0.92 with humans (p.21)
- Hindsight bias between-subjects: largest human Cohen's d = 0.83; LLM effects d = 1.43–5.97 (p.24)
- Mean SD of LLM blame/praise ratings in harm condition: 0.30 vs. humans 1.32 (p.12)

## 10. Pitfalls & limitations
- Studies not selected through systematic/preregistered criteria — acknowledged as exploratory (p.8).
- Temperature parameters not equated across models; differences in variance may partly reflect temperature choices rather than model properties.
- Claude 2.1 and Llama 2 Chat 70b frequently produce verbose non-numeric responses, requiring text parsing and resulting in high invalid-response rates (up to 73% for Claude on deception study, 100% for Llama, p.14).
- Single-language (English) evaluation; no multilingual testing.
- Human comparison data varies by study in terms of sample characteristics, collection date, and country.
- "Correct answer" effect inflates correlations; the paper correctly notes this but does not provide a variance-corrected correlation measure.
- Gemini Pro safety filters were disabled to maximize valid responses — results may not reflect typical deployed behavior.

## 11. Novel ideas worth stealing
1. **Machine-psychology replication design**: Replicate established human moral/legal psychology experiments with LLMs — provides ground truth with known human effect sizes and significance patterns, enabling precise alignment measurement.
2. **Per-condition SD as a discrimination diagnostic**: Compare within-condition standard deviations between LLMs and humans to detect the "correct answer" effect — high correlation with near-zero variance is a red flag, not a green light.
3. **Condition*agent interaction as a formal test**: Add model as a factor in the original study's analysis; significant interactions indicate systematic differences beyond magnitude, not just effect size scaling.
4. **Multi-model comparison design**: Test multiple models simultaneously on identical stimuli to characterize idiosyncratic vs. shared departures from human patterns.
5. **Parity check on response validity rates**: Track the fraction of invalid (non-parseable) responses per model per study — this is an underreported metric that reveals instruction-following reliability as a dimension of model capability.
6. **Political orientation order-balancing**: Counterbalance the order of political orientation scale options to detect order effects in political self-classification (relevant to MFQ profiling of LLMs).

## 12. Notable quotes
- "Even when LLM-generated responses are highly correlated to human responses, there are still systematic differences, with a tendency for models to exaggerate effects that are present among humans, in part by reducing variance." (p.1)
- "Claude 2.1, GPT-4, and Gemini Pro gave invariant answers to the intentionality question. In fact, across the board, LLMs' responses showed less variance than human-generated responses." (p.13)
- "All models attributed significantly lower relevance to the Loyalty foundation (ps < .04), and all but Llama 2 attributed significantly lower relevance to the Purity foundation (ps < .001)." (p.18)
- "The fact that LLMs can be prompted to overweight certain moral foundations and that this can significantly affect its behavior on the downstream donation task could lead to several risks." (from Abdulhai et al. paper referenced at p.2)

## 13. UNKNOWN / not in extract
- Full results for Study 7 (Consent, Demaree-Cotton & Sommers) — extract ends at Study 6.
- Full results for Study 8 (Causal attribution with normative abnormality, Icard et al.) — not in extract.
- Exact temperature settings for each model in each study (mentioned as varying but full table not in extract).
- Whether statistical models used Bonferroni or other corrections for the eight simultaneous study comparisons.
- Whether order effects on MFQ items were tested in addition to political orientation order.
- Number of stimuli per study for consent and causal attribution studies.
