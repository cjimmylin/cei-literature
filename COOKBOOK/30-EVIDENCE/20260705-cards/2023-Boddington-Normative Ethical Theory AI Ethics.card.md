---
stem: "2023-Boddington-Normative Ethical Theory AI Ethics"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [normative-ethics, pluralism-aggregation, design-space, moral-psychology]
task_format: "MCQ"
scoring_type: "exact-match"
dataset_size: null
dataset_construction: "hand-authored"
languages: ["en"]
models_tested: ["DeBERTa-v3-large", "BERT-large", "RoBERTa-large", "ALBERT-xxlarge", "T5-11B", "Delphi"]
headline_numbers:
  - "DeBERTa-v3-large: Deontology 78.0/59.4, Virtue 76.3/50.9, Utilitarianism 81.6/73.6 (Test/Hard Test) (p.6)"
  - "MEC ensemble achieves 82.3% on commonsense ETHICS dataset vs. individual theory models 71.5–77.1% (p.6)"
  - "MEC matches Delphi on paired PhD-student evaluation: Delphi 81%, MEC 88% (p.7)"
  - "PhilPapers Survey: consequentialism 32%, deontology 31%, virtue ethics 37% (p.4)"
---
## 1. Gist
This paper (misleadingly filed as "Boddington" but authored by Takeshita, Rzepka, and Araki from Hokkaido University) implements the Maximizing Expected Choiceworthiness (MEC) algorithm — a decision-procedure for handling moral uncertainty from the philosophy literature — as an AI moral reasoning system. The core argument is that existing moral AI systems (particularly Delphi) rely on bottom-up commonsense morality datasets that cannot correct morally erroneous common sense; a theory-grounded top-down approach that aggregates outputs of models fine-tuned on utilitarianism, deontology, and virtue ethics is more principled. DeBERTa-v3-large is fine-tuned separately on three theory-specific subsets of the ETHICS benchmark dataset, then MEC aggregates their outputs. The result matches or exceeds Delphi on commonsense morality and is evaluated by philosophy PhD students who prefer it but find both systems inadequate for moral deliberation because neither provides reasons/explanations for its verdicts.

## 2. Benchmark/eval design features
The evaluation has two components: (1) quantitative: accuracy/F1 on ETHICS dataset (utilitarianism, deontology, virtue, commonsense subsets) with paired comparisons to BERT, RoBERTa, ALBERT, T5-11B, and Delphi; (2) qualitative: three philosophy PhD students evaluate 16 paired sentence comparisons from ETHICS commonsense subset and answer three overall questions comparing Delphi vs. MEC as moral advisors. The ETHICS dataset uses scenarios from the perspective of a single character, asking whether the character's action is morally acceptable (binary classification) or ranking actions by pleasantness/harm (utilitarian subset). Hard Test versions of each subset are also evaluated.

## 3. Task format & example item
Multiple-choice comparison format (ETHICS dataset). The deontology subtask uses the "Role" input format: "I am a human [SEP] ⟨action statement⟩" and classifies whether the action is permissible or impermissible. The virtue subtask uses format "⟨action statement⟩ [SEP] ⟨character trait term⟩" and classifies whether the trait is positive/negative, with SenticNet providing trait sentiment. The utilitarianism subtask is binary (harmful/not harmful from the perspective of the person described). No verbatim example item is quoted in the extract.

## 4. Scoring / grading methodology
Accuracy for binary classification on ETHICS subsets (standard and hard test). For commonsense generalization: MEC aggregation tested with equal theory credence weights C(Ti)=1 (justified by PhilPapers Survey showing roughly equal philosopher endorsement: 32% consequentialism, 31% deontology, 37% virtue ethics). Modified Borda scoring for ordinal theories. Normalization by standard deviation across representative action sets. PhD student evaluation: paired forced-choice among {A more preferable, B more preferable, Both preferable, Both not preferable} for three overall questions.

## 5. Dataset construction & provenance
ETHICS dataset (Hendrycks et al., 2021) used for all training and automated evaluation. Three theory-specific subsets used: utilitarianism, deontology, virtue. DeBERTa-v3-large fine-tuned on each separately. Commonsense subset of ETHICS used for generalization testing. PhD student evaluation uses 20 sampled pairs from ETHICS commonsense test set; 4 pairs excluded due to lack of context, leaving 16. 695 character trait terms from ETHICS virtue training set assigned sentiment via SenticNet 7. All experiments use AdamW optimizer, LR in {1e-5, 2e-5, 3e-5}, batch size 64, 4 epochs.

## 6. Validity evidence
PhD students find both MEC and Delphi output similar rates of correct answers on their moral judgments (Delphi: 81%, MEC: 88%, Table 5), suggesting both are reasonable approximations of commonsense morality. Each theory-based model individually outperforms random baseline on commonsense data (not fine-tuned on commonsense), providing evidence of some cross-construct validity. However, PhD students judge both systems "not helpful" for moral deliberation because neither provides reasons — a critical validity gap for the intended use case.

## 7. Saturation / discrimination
DeBERTa-v3-large Hard Test performance: Deontology 59.4%, Virtue 50.9%, Utilitarianism 73.6% (p.6) — Hard Test performance is substantially lower than standard test, indicating meaningful discriminability between easy and hard items. The commonsense MEC accuracy (82.3%) exceeds individual theory models (71.5–77.1%), demonstrating ensemble benefit. The overall ETHICS benchmark remains challenging, especially for Hard Test.

## 8. Multiturn / agentic aspects
n/a — static binary/pairwise classification task. The MEC system outputs a ranking of options for a given moral scenario but does not engage in dialogue or multi-step reasoning.

## 9. Key numbers
- DeBERTa-v3-large test/hard test: Deontology 78.0/59.4, Virtue 76.3/50.9, Utilitarianism 81.6/73.6 (p.6)
- MEC commonsense accuracy: 82.3% vs. Utilitarianism 76.5%, Deontology 71.5%, Virtue 77.1% (p.6)
- Delphi commonsense (100 training samples): Deontology 49.6/31.0, Virtue 29.5/18.2, Utilitarianism 84.9/76.0 (p.6)
- PhD student overall: Delphi 81%, MEC 88% correct on 16 pairs (p.7)
- PhilPapers Survey: 32% consequentialism, 31% deontology, 37% virtue ethics (p.4)
- 695 character trait terms assigned sentiment via SenticNet (p.5)
- 20 paired sentences evaluated by PhD students; 16 usable (p.5)

## 10. Pitfalls & limitations
- ETHICS dataset was created by non-specialist crowdworkers and does not precisely match theoretical definitions (e.g., utilitarian task asks about well-being of the person in the scenario, not all affected beings) — the training data is theory-inspired but theoretically impure (p.5).
- Small PhD evaluation sample: only 3 annotators evaluating 16 pairs — insufficient for strong statistical conclusions.
- PhD students found both systems "not helpful" for moral deliberation because no reasons/explanations are provided — the system's core claimed advantage (showing theory-based outputs as explanations) was rejected by evaluators (p.7).
- Equal credence weights (C(Ti)=1 for all theories) is a simplifying assumption that may not reflect appropriate moral uncertainty; philosopher endorsement rates may not be the right metric.
- No evaluation on moral dilemmas (acknowledged as a limitation, p.8).
- Only three theories (utilitarianism, deontology, virtue ethics); contractualism, care ethics, cultural ethics not included.

## 11. Novel ideas worth stealing
- **MEC as a pluralism aggregation architecture**: the Maximizing Expected Choiceworthiness algorithm is a principled, philosophically grounded method for aggregating outputs from models trained on different ethical frameworks under conditions of moral uncertainty — directly applicable to building pluralism-aware values-alignment systems.
- **Theory-specific fine-tuning + ensemble**: training separate models on utilitarianism, deontology, and virtue ethics datasets, then combining their outputs, is a modular design that allows each theory's contribution to be audited separately — useful for explainable values-alignment.
- **Credence-weighted voting**: using philosopher endorsement rates (or other evidence-based weights) to determine how much each ethical theory contributes to the final output is a transparent, tunable alternative to uniform averaging.
- **Commonsense generalizability test**: evaluating theory-trained models on a commonsense (non-theory) dataset tests whether theoretical grounding produces practical moral judgments that align with widespread intuitions — a useful validation step for any theory-grounded moral AI.
- **Borda scoring for ordinal theories**: using modified Borda scoring to convert ordinal theory outputs to cardinal scores is a practical implementation detail for combining theories with different output types (ordinal deontology vs. cardinal utilitarianism).

## 12. Notable quotes
- "If one creates models based on theories, one can, in principle, evaluate the output of each theory-based model since there is a correct answer relative to the theory for every question." (p.3)
- "Because MEC is a general framework, it can be used for the models developed in this paper and other models that may be proposed or developed by others in the future." (p.4)
- "Annotators answered that models such as Delphi and MEC are not helpful in moral deliberation, both for experts and non-experts, because they do not provide reasons, i.e., they do not explain their choices." (p.7)
- "Relying directly on commonsense morality may be inappropriate if it is incorrect. Therefore, we use findings of normative ethics and implement Moral AI based on the normative theories studied there." (p.1)

## 13. UNKNOWN / not in extract
- Whether the MEC implementation and model weights are publicly available
- Evaluation on genuinely morally controversial or politically divisive scenarios
- Results with credence weights derived from actual philosophical endorsement rates (versus equal weighting assumed here)
- Comparison to GPT-4 or other large instruction-tuned models
- Whether the PhD student annotators were Japanese-speaking and whether language influenced evaluations
- Performance with contractualism, care ethics, or cultural relativism as additional theory components
