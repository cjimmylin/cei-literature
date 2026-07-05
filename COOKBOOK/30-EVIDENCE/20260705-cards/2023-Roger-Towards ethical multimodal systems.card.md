---
stem: "2023-Roger-Towards ethical multimodal systems"
reader_model: "sonnet"
confidence: "medium"
is_benchmark: false
theme_tags: [design-space, validity-psychometrics, ai-lab-practices]
task_format: "preference"
scoring_type: "classifier"
dataset_size: 789
dataset_construction: "crowdsourced"
languages: ["fr", "en"]
models_tested: ["MAGMA (CLIP + GPT-J-6B)", "RoBERTa-large", "MLP classifier"]
headline_numbers:
  - "789 image-question-answer triples retained after filtering from 2,844 initial prompts (p.4)"
  - "RoBERTa-large classifier achieved 52% accuracy when compared to crowd votes (p.5)"
  - "MLP multimodal classifier achieved 55% accuracy on test set (p.5)"
  - "Distribution of labels: 46% ethical, 49% unethical, 5% unclear (p.5)"
---
## 1. Gist
This short workshop paper (NeurIPS 2023) describes a proof-of-concept effort to evaluate the ethical behaviour of a multimodal AI system (MAGMA, which takes image + text question and produces a text answer) and to build the first crowdsourced multimodal ethics dataset. The central argument is that existing ethics evaluation work focuses exclusively on text-only models, leaving image-grounded interactions unstudied. The authors build a Discord-based crowd-evaluation pipeline where volunteers rate MAGMA's responses to ethically loaded image-question pairs as "ethical", "unethical", or "unclear", yielding 789 annotated examples. They then test a text-only RoBERTa classifier and a multimodal MLP on this dataset, with poor results (~52–55%), underscoring that ethical assessment of multimodal outputs is harder than pure text. For values-alignment benchmarking the paper is relevant as an early design case for multimodal ethics datasets and a gamified crowd-annotation pipeline.

## 2. Benchmark/eval design features
The paper constructs a dataset rather than deploying a benchmark in the formal sense. The construct is "ethical vs unethical" output from a multimodal VQA model across domains including economics, medicine, society, and discrimination. Item structure: an image, a question, and MAGMA's generated answer; annotators vote ethical/unethical/unclear. Three classes total. The evaluation pipeline uses majority voting across annotators; items with a majority of "unclear" votes are set aside. Safeguards include user pre/post-tests (5 standardised prompts per batch), user monitoring via Discord IDs for pattern detection, and demographic controls (initially university students, then expanded). Coverage includes human values, greed, exploitation, child labour, provocative advertisements, discrimination (sexism, racism, disability), family settings, abortion, euthanasia, doping, medical experiments, animal experiments, and "extreme" situations.

## 3. Task format & example item
Figure 1 shows an image of what appears to be a workplace scene; MAGMA's response (shown in red) gives an answer to a question about it that fails ethical standards. No verbatim example item text is reproduced in the extract beyond the Figure 1 description on (p.2): "Example of MAGMA's responses (in red) to a question (in grey) on the image above."

## 4. Scoring / grading methodology
Crowd scoring via Discord reactions: thumbs up = ethical, thumbs down = unethical, shrug = unclear. Majority vote across raters determines label. For classifier evaluation, accuracy is measured against the majority-vote crowd label. RoBERTa-large is applied text-only (question + answer concatenated), with scores in [0,1]; <0.4 = ethical, >0.6 = unethical, 0.4–0.6 = unclear threshold applied by authors. MLP classifier trained on CLIP image embeddings + GPT-2 text embeddings, 3 outputs (ethical/unethical/unclear), trained on annotated data.

## 5. Dataset construction & provenance
Images (218) drawn from the Belgian "Banque de cas éthiques" (Enseigner l'éthique, 2021) — a bank of ethical case studies. 14 general prompts crafted to elicit ethically interesting responses; all combinations processed through MAGMA, yielding 2,844 prompts after filtering responses lacking Latin alphabet characters. Initial round: 50 university students evaluated 1,108 prompts. After removing unclear-majority and unevaluated prompts, 789 examples remained for a second evaluation round with expanded annotators (65 by final count). Final dataset: 369 ethical (46%), 386 unethical (49%), 34 unclear (5%) per Table 1 (p.5). No formal licence mentioned; authors state dataset "will be made available" with regular updates.

## 6. Validity evidence
Pre/post-test design: each annotator batch contains 5 standardised pre-test prompts and 5 post-test prompts with known ground truth, enabling trustworthiness assessment. Authors observe that prompts with <10% "unclear" responses achieve >60% agreement on ethical status; prompts with >25% "unclear" responses show near-parity ethical/unethical splits, suggesting "unclear" rate is a useful signal of genuine ambiguity (p.4). No formal inter-rater reliability statistics (kappa etc.) are reported. 52% RoBERTa accuracy is taken as evidence that image context is genuinely required — a form of construct validity showing the dataset is not solvable from text alone.

## 7. Saturation / discrimination
Dataset is small (789 items) and near-balanced by design (46%/49%). Classifier performance is barely above chance (52–55%), indicating the task is genuinely difficult. No ceiling or floor effects in the dataset are discussed; the near-equal split between ethical and unethical is actively maintained as a design goal. No item-difficulty analyses are reported.

## 8. Multiturn / agentic aspects
n/a — the annotation task is single-turn: one image + question + model answer, one vote. MAGMA generates a single text response to each image-question pair.

## 9. Key numbers
- 218 images from Banque de cas éthiques (p.3)
- 14 general prompts crafted by authors (p.3)
- 2,844 prompts after MAGMA generation and filtering (p.3)
- 1,108 prompts evaluated in initial round by 50 students (p.3)
- 789 final annotated examples (p.4)
- 369 ethical / 386 unethical / 34 unclear labels (p.5, Table 1)
- RoBERTa-large: 52% accuracy vs crowd votes (p.5)
- MLP classifier: 55% accuracy on test set (p.5)
- RoBERTa-large prior accuracy on ethics benchmark (Hendrycks et al.): 63.4% on hard test set (p.5)
- ~⅓ of initial prompts rated "unclear" by majority (p.4)

## 10. Pitfalls & limitations
- Very small dataset (789 items) limits statistical power and generalisability.
- All annotators were university students (mostly CS undergraduates), raising concern about demographic and cultural parochialism.
- The underlying VQA model (MAGMA) is described as experimental and outdated; results may not transfer to current multimodal systems.
- Text-only classifiers unsurprisingly fail at a task requiring image understanding — this is informative but not a rigorous model benchmark.
- No formal inter-rater reliability metrics reported.
- Crowd-sourcing platform (Discord) introduces self-selection bias toward tech-savvy users.
- Monetisation concerns: Amazon MTurk was avoided to prevent financial incentives from distorting ethical responses, but this also limits scale.
- The paper is a workshop paper; methods are preliminary and results require validation.

## 11. Novel ideas worth stealing
1. **Gamified Discord pipeline**: Using a chat platform with emoji reactions to collect ethics labels is cheap and engagement-friendly. The "$eval_batch" command with a 5-second inter-prompt gap and three-option reaction scheme (thumbs up/down/shrug) is a reusable micro-annotation UX for ethics datasets.
2. **Pre/post-test trustworthiness gates**: Embedding standardised "gold" prompts at the start and end of each annotation batch to detect disengagement or adversarial labelling is a simple, low-cost integrity check reusable in crowd-sourced annotation pipelines.
3. **Unclear-rate as ambiguity proxy**: Using the fraction of annotators selecting "unclear" as a calibrated proxy for genuine ethical ambiguity, with a proposed 10–25% threshold band, provides a principled way to flag contested items without requiring expert adjudication.
4. **Multimodal ethics construct**: Designing prompts where ethical assessment genuinely requires both image and text (confirmed empirically by text-only classifier failure) is a clean construct validity move that could be extended to video, audio, or embodied contexts.
5. **Demographic-controlled crowd expansion**: Starting with a small controlled demographic (departmental students) and systematically widening to larger groups while maintaining monitoring is a methodological pattern for building representative ethics datasets incrementally.

## 12. Notable quotes
- "None of these initiatives have focused on large multimodal models." (p.1)
- "The prompts did not contain image information, explaining many 'unclear' scores between 0.4 and 0.6. These can be attributed to a lack of context for the evaluation." (p.5)
- "This is the first dataset of its kind and can greatly help research in the field." (p.6)
- "If less than 10% of users found a prompt unclear, over 60% agreed on its ethical status." (p.4)

## 13. UNKNOWN / not in extract
- Exact demographic breakdown of annotators (beyond "university students, primarily CS undergraduates") is not reported.
- No information on inter-rater reliability statistics (Cohen's kappa etc.).
- Specifics of MLP architecture hyperparameters (layer sizes, learning rate, train/test split ratio) are not given.
- Whether the dataset is publicly released and under what license is unclear — authors say it "will be made available."
- Results for other multimodal models beyond MAGMA are described as "ongoing work" and not in this paper.
- The exact 14 prompts used are not listed in the extract.
