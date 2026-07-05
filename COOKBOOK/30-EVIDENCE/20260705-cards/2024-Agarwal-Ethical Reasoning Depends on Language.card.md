---
stem: "2024-Agarwal-Ethical Reasoning Depends on Language"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, normative-ethics, pluralism-aggregation, validity-psychometrics]
task_format: "forced-choice"
scoring_type: "exact-match"
dataset_size: 108
dataset_construction: "hand-authored"
languages: ["en", "es", "ru", "zh", "hi", "ar", "sw"]
models_tested: ["GPT-4", "ChatGPT (GPT-3.5-turbo)", "Llama2-70B-Chat"]
headline_numbers:
  - "GPT-4 achieves 93.3% accuracy on English ethical policy resolution; drops to 62.7% on Hindi (p.8, Table 2)"
  - "Llama2-70B-Chat achieves 78.0% on English but only 41.2% on Swahili (p.8, Table 2)"
  - "ChatGPT accuracy: 58.8% English vs. 49.8% Hindi and Swahili (p.8, Table 2)"
  - "All models perform worst on Hindi and Swahili; best on English and Russian (p.7)"
---
## 1. Gist
This paper extends an ethical-reasoning framework originally proposed by Rao et al. (2023) — where LLMs are given explicit ethical policies (moral stances from deontology, virtue ethics, or consequentialism) and asked to resolve moral dilemmas — from English to six additional languages: Spanish, Russian, Chinese, Hindi, Arabic, and Swahili. The core question is whether LLMs exhibit a "Foreign Language Effect" analogous to humans, changing their moral judgments when confronted with dilemmas in a non-native language. The study demonstrates that LLMs show significant language-dependent moral bias — performing well on English and Russian but struggling with Hindi and Swahili — and that the nature of this bias is dilemma-specific, not simply a uniform performance degradation. For values-alignment benchmarking, this paper is essential evidence that measuring moral reasoning in English alone gives a misleading picture of model alignment across a multilingual world.

## 2. Benchmark/eval design features
The framework is built around four moral dilemmas (Heinz, Monica, Rajesh, Timmy) — each involving interpersonal vs. professional value conflicts — sourced from Rao et al. (2023). Each dilemma has 18 policies (9 paired contrasting stances at 3 levels of abstraction: Level 2 = abstract principle, Level 1 = role-specific, Level 0 = concrete named-entity version). The model is given the dilemma text + one policy and must resolve it as "should", "shouldn't", or "can't decide". Ideal resolutions were annotated by Rao et al. Three ethical frameworks are represented: Virtue, Deontology, and Consequentialism. Key metrics: accuracy (% matching ideal resolution), bias (fraction of times model ignores opposing policy), and confusion (fraction of times model deviates from its own baseline when it shouldn't).

## 3. Task format & example item
Forced-choice resolution task. Each prompt contains: (1) a dilemma narrative, (2) an ethical policy specifying which value should take precedence, (3) three response options. Example policy (abstraction Level 2, virtue ethics):

"Prioritize loyalty over objective impartiality." — then the model must resolve whether the protagonist should take the action or not (p.4–5, describing Level 2 policies).

Baseline experiment: model prompted with dilemma alone (no policy) to reveal inherent bias. Policy experiment: 432 prompts per language per model (18 policies × 4 dilemmas × 6 option-order permutations), each permutation run 5 times to control positional bias.

## 4. Scoring / grading methodology
Accuracy = % of responses matching the ideal resolution annotated by Rao et al. Bias = fraction of "wrong-direction" responses when the model's baseline stance conflicts with the policy (measures how often the model ignores the given policy). Confusion = fraction of "wrong-direction" responses when the model's baseline stance aligns with the policy (measures unpredictable deviations). Six option-order permutations × 5 runs per permutation give 30 samples per policy-dilemma-language combination; majority is used for baseline resolution.

## 5. Dataset construction & provenance
Dilemmas and ideal resolutions from Rao et al. (2023) — 4 dilemmas, 9 policy pairs each. English versions were machine-translated to 6 languages using Google Translate API, then back-translated to English and manually inspected by native speakers for meaning fidelity. Seven languages total (including source English). No new dilemmas were created. Limitations: only 4 dilemmas (low item count); dilemmas authored by a potentially ethnically homogeneous team (acknowledged, p.8–9); Google Translate may introduce cultural translation errors.

## 6. Validity evidence
Baseline experiment reveals model-specific default resolutions that are consistent within English, providing a useful internal validity check. The study replicates and extends Rao et al. (2023) finding that GPT-4 can follow ethical policies in English (~93% accuracy). The finding that English ≈ Spanish and Hindi ≈ Chinese in bias patterns hints at cultural/linguistic clustering beyond pure resource effects, though this is not formally tested. No human participant comparison is reported for the non-English languages; ideal resolutions are defined by an English-language annotation process and may not reflect non-Western moral intuitions.

## 7. Saturation / discrimination
GPT-4 shows near-ceiling performance on English (93.3%) and Spanish (88.4%), leaving little room to discriminate among high-performing models in those languages. Hindi and Swahili provide the most discrimination headroom: GPT-4 drops to 62.7% / 71.5% respectively, and Llama2 drops to 50.7% / 41.2%. ChatGPT and Llama2 are near chance performance on low-resource languages for some dilemmas, suggesting the task may be too hard for them in those languages rather than revealing fine-grained value alignment differences.

## 8. Multiturn / agentic aspects
All interactions are single-turn: one prompt containing dilemma + policy + instructions, one response. No multiturn dialogue, tool use, or environment interaction. The study isolates one decision point per instance.

## 9. Key numbers
- 4 moral dilemmas, 18 policy variants each = 72 policy-dilemma pairs per language (p.5)
- 432 model queries per language per model in policy experiments (p.5)
- 120 baseline queries per language per model (4 dilemmas × 6 permutations × 5 runs, p.5)
- 7 languages total (English + 6 additional) (p.1)
- GPT-4 English accuracy: 93.3%; Hindi: 62.7%; Swahili: 71.5% (p.8, Table 2)
- ChatGPT English accuracy: 58.8%; Hindi/Swahili: 49.8% (p.8, Table 2)
- Llama2-70B English accuracy: 78.0%; Swahili: 41.2% (p.8, Table 2)
- GPT-4 Monica dilemma: 100% agreement across all languages; GPT-4 Rajesh dilemma: opposite resolutions for most non-English languages vs. English (p.6, Table 1)

## 10. Pitfalls & limitations
- Only 4 dilemmas — extremely low item count limits statistical power and generalizability.
- Ideal resolutions annotated from English-centric perspective; what counts as "correct" may not generalize cross-culturally.
- Machine translation of moral dilemmas may alter semantic nuances that drive moral judgments (acknowledged, p.8).
- Dilemma content may be culturally unfamiliar to Hindi/Swahili speakers, conflating cultural unfamiliarity with ethical reasoning failure.
- No human performance baseline in non-English languages, so it's impossible to know whether "lower accuracy" reflects genuine ethical reasoning failure or appropriate cultural disagreement with the English-defined ideal resolution.
- Results cannot generalize beyond the three tested model families.
- Arabic included in the abstract but the paper refers to six non-English languages while listing Spanish, Russian, Chinese, Hindi, Arabic, Swahili — and some results tables show seven columns including Arabic, creating a minor inconsistency.

## 11. Novel ideas worth stealing
1. **Policy-in-prompt architecture**: Rather than encoding a fixed moral stance into model weights, inject an explicit ethical policy at inference time and measure whether the model can follow it — this is a direct evaluation of value pluralism handling without training new models.
2. **Bias/confusion decomposition**: Separate "ignores-opposing-policy" (bias) from "ignores-aligned-policy" (confusion) as distinct failure modes — different interventions may be needed for each.
3. **Multilingual moral drift measurement**: Use the same dilemmas translated into multiple languages to measure how much moral judgment shifts with language — directly quantifies cross-lingual value alignment gaps.
4. **Abstraction-level gradient**: Testing the same moral stance at three levels of abstraction (abstract principle → role-specific → concrete instance) reveals whether models fail at generalization or at concretization.
5. **Baseline-resolution profiling**: Measure each model's unprompted default resolution per dilemma per language before administering policy prompts; this characterizes the model's "prior" moral stance as a confound-control step.
6. **Language-pair clustering**: Visualize which languages produce similar bias profiles across models — may reveal culturally meaningful groupings (e.g., English ≈ Spanish, Hindi ≈ Chinese) that could inform multilingual dataset design.

## 12. Notable quotes
- "The ethical reasoning ability (or conversely the bias) is dilemma-specific, which makes us conclude that the LLMs have strong value alignment biases in languages beyond English." (p.2)
- "Across all models, the reasoning is poorest for Hindi and Swahili, while best for unsurprisingly, English, and also Russian." (p.2)
- "Languages and values are strongly intertwined, as is language and culture... it is not clear whether these biases are a reflection of cultural differences across the languages, or simply an artifact of poor performance." (p.7)
- "Use of LLMs for ethical reasoning support across cultures, values and languages can be a very promising use-case with significant large scale positive impact." (p.7–8)

## 13. UNKNOWN / not in extract
- Whether Arabic results are reported separately (the abstract mentions 6 languages but the main results section appears to use 7, with some inconsistency).
- Whether any debiasing or cross-lingual prompting strategies were explored.
- Exact translation protocol and how many native speakers reviewed each language translation.
- Whether the same ideal resolutions were used for all languages (likely yes, but whether any language-specific overrides were applied is unclear).
- Specific dilemma content for all four dilemmas — only partial descriptions appear in the extract.
