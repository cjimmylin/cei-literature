---
stem: "2020-Sap-Social Bias Frames"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [normative-ethics, moral-psychology, cultural-linguistic, validity-psychometrics]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: 44671
dataset_construction: "crowdsourced"
languages: ["en"]
models_tested: ["SBF-GPT1-gdy", "SBF-GPT2-gdy", "SBF-GPT2-smp", "SBF-GPT2-gdy-constr", "SBF-GPT2-smp-constr"]
headline_numbers:
  - "SBIC contains 150k structured inference tuples covering 34k implications about 1,414 demographic groups (p.5)"
  - "GPT2 models achieve 80.5% F1 on offensiveness classification on the development set (p.6)"
  - "In-group language detection is near chance: GPT2-smp achieves 24.0 F1 (p.6)"
  - "Overall annotations show 82.4% pairwise agreement and Krippendorff alpha=0.45 (p.5)"
  - "78% of posts in SBIC are in White-aligned English (p.5)"
---
## 1. Gist
Social Bias Frames introduces a structured formalism for representing the pragmatic, stereotyped, and power-differential implications of language. The paper presents the Social Bias Inference Corpus (SBIC), containing 150k structured annotations on ~45k social media posts, where each annotation captures whether a post is offensive/lewd/intentional, which demographic group is targeted, and what the implied stereotype is (in free text). This work matters for values-alignment benchmarking because it goes beyond binary toxicity labels to provide structured, multi-dimensional offense annotations that capture implied meaning — exactly the kind of nuanced representation required to evaluate whether AI systems can reason about social harm.

## 2. Benchmark/eval design features
The paper introduces SOCIAL BIAS FRAMES as both a conceptual formalism and a dataset. The formalism captures: (1) offensiveness (categorical: yes/maybe/no), (2) intent to offend (categorical: yes/probably/probably-not/no), (3) lewdness (categorical), (4) group implication (binary), (5) targeted group (free-text), (6) implied statement — the stereotype (free-text in "GROUP does/is [X]" form), and (7) in-group language (whether the author may belong to the targeted group). The evaluation benchmark involves both classification tasks (predicting the categorical variables) and generation tasks (generating targeted group and implied statement text). Models are trained on GPT-1 and GPT-2, evaluated on a 75:12.5:12.5 train/dev/test split.

## 3. Task format & example item
Annotation task (classification + generation). The MTurk annotation interface (Figure 2, p.4; full version Figure 4, p.14) asks workers:

1. Could this post be offensive to anyone? (Yes / Maybe / No / I don't understand)
2. Was the intent offensive? (Yes definitely / Yes probably / No probably not / No definitely not)
3. Does it contain sexual content?
4. Who is referred to/targeted? (Identity group selector with free text)
5. What aspect/stereotype of this group is referenced? (Free text: "GROUP does ___")
6. Does the author sound like they belong to the targeted group?

Example from Table 1 (p.2): Post: "I'll continue this thread till non-lifting fags stop lifting like idiots at the gym... Which is never." → Group: gay men; Implied statement: "are weak and not manly."

## 4. Scoring / grading methodology
Classification tasks: Precision, Recall, and F1 on the positive class. Categories are binarized (yes/probably/maybe → 1; others → 0). Multiple annotations per post are aggregated by averaging binarized values and re-binarizing at 0.5 threshold for eval.

Generation tasks (targeted group, implied statement): BLEU-2, Rouge-L (F1), and Word Mover's Distance (WMD). For generation, hypothesis is compared against all reference group-statement pairs for the post.

## 5. Dataset construction & provenance
Posts drawn from: Reddit (r/darkJokes, r/meanJokes, r/offensiveJokes, microaggressions corpus), Twitter (Founta et al. 2018, Davidson et al. 2017, Waseem and Hovy 2016), and Hate Sites (Gab, Stormfront, banned subreddits r/Incels and r/MensRights). Total: 44,671 unique posts → 147,139 annotation tuples (3 per post minimum; 150k in practice). Crowdsourcing via Amazon Mechanical Turk, restricted to US/Canada workers. Workers were paid $7–12 (above minimum wage) and daily annotation limits were set to mitigate harm. IRB-approved. Dataset available at tinyurl.com/social-bias-frames.

## 6. Validity evidence
Pairwise inter-annotator agreement: 82.4% overall; Krippendorff's α=0.45 on average (p.5). Broken down: offensiveness 76% agreement (α=0.51); intent to offend 75% (α=0.46); group implications 74% (α=0.48); lewdness 94% (α=0.62); in-group language 94% agreement but α=0.17 (due to highly skewed class with only 5% positive). Targeted group exact match: 80.2% (α=0.50). The alpha values are described as "substantially higher than previous work in toxic language detection (e.g., α=0.22 in Ross et al., 2017)" (p.5). Annotator pool was 55% women, 42% men, 82% White — racial skew is a noted limitation.

## 7. Saturation / discrimination
Models perform well on higher-level classifications (offensiveness F1~80%, lewdness F1~80%) but poorly on nuanced tasks: in-group language detection is near-chance for most models (GPT2-smp achieves F1=24.0 on dev, others default to never predicting positive). Generation quality is moderate (BLEU~75-83% for targeted group; 44-52% for implied statement). The model "struggles to generate relevant social bias implications, instead generating very generic stereotypes" (Table 6, p.8). This indicates significant remaining headroom, especially for nuanced implicature detection.

## 8. Multiturn / agentic aspects
n/a — single-turn classification and generation tasks on individual posts.

## 9. Key numbers
- Total annotation tuples: 147,139 (Table 3, p.5)
- Unique posts: 44,671 (p.5)
- Unique groups referenced: 1,414 (p.5)
- Unique group-implication pairs: 34,333 (p.5)
- Offensiveness positive rate: 44.8% (p.5)
- Lewd positive rate: 7.9% (p.5)
- Group targeted positive rate: 50.9% (p.5)
- In-group language positive rate: 4.6% (p.5)
- Best offensiveness F1 (test): 78.8% (SBF-GPT2-gdy, p.6)
- Best targeted group BLEU (test): 77.0–77.9% (p.7)
- Best implied statement BLEU (test): 52.2–52.6% (p.7)
- 78% of posts in White-aligned English (p.5)
- Annotator demographics: 55% women, 82% White (p.5)

## 10. Pitfalls & limitations
- Annotator pool is racially skewed (82% White), which may introduce biased annotations for content targeting non-White groups; authors caution about dialect-based racial bias in labeling (p.5, section 7).
- Implied statement generation is still far from human-level quality; models tend to generate generic stereotypes rather than the specific implication entailed by the post (Table 6, p.8).
- In-group language detection is poorly handled by all models due to class skew (5% positive) and subtlety.
- U.S.-centric sociocultural lens explicitly acknowledged (footnote 2, p.3); results may not transfer cross-culturally.
- Risk of censorship and nefarious deployment discussed (section 7, p.9).
- Posts drawn partly from known hate communities, which may affect generalizability to non-extremist content.

## 11. Novel ideas worth stealing
- **Structured pragmatic annotation over simple labels**: Instead of binary toxicity, capturing a multi-field frame (offensiveness + intent + group + implied stereotype) gives richer supervision and a harder, more meaningful benchmark. New values-alignment benchmarks could adopt this frame structure for capturing normative violations.
- **Implied statement as free-text evaluation target**: Requiring models to generate "GROUP does [X]" stereotypes as free text is a powerful way to test whether a model understands the underlying social implication rather than surface markers.
- **In-group language as a confound dimension**: Annotating whether the author may be a member of the targeted group captures a genuine pragmatic nuance (reclaimed slurs, self-deprecating humor) that is often collapsed in hate-speech benchmarks.
- **Hierarchical annotation cascade**: Only annotators who flag potential offensiveness proceed to the group implication questions — a cost-efficient design for expensive annotation pipelines.
- **BLEU + WMD dual evaluation for generated social inferences**: Using word-overlap (BLEU/Rouge) alongside semantic distance (WMD) gives a more robust picture of generation quality for stereotype-type free text.
- **Seed list for targeted groups with free-text fallback**: Providing a vocabulary of demographic groups as anchors while allowing free-text entry balances coverage and consistency — useful for cultural benchmark design.

## 12. Notable quotes
- "Language has the power to reinforce stereotypes and project social biases onto others. At the core of the challenge is that it is rarely what is stated explicitly, but rather the implied meanings, that frame people's judgments about others." (p.1)
- "While state-of-the-art neural models are effective at high-level categorization of whether a given statement projects unwanted social bias (80% F1), they are not effective at spelling out more detailed explanations in terms of SOCIAL BIAS FRAMES." (p.1)
- "The model seems to struggle with generating textual implications that are relevant to the post, instead generating very generic stereotypes about the demographic groups." (p.8)
- "We caution researchers to consider the potential for dialect- or identity-based biases in labelling before deploying technology based on SBIC." (p.5)

## 13. UNKNOWN / not in extract
- Whether the dataset split (75:12.5:12.5) is stratified by source or demographic group.
- Cost per annotation and total annotation budget.
- Whether v2.0 or later versions of SBIC exist beyond what is described in the paper.
- Specific MTurk worker qualification criteria beyond US/Canada restriction.
- License terms for the dataset.
