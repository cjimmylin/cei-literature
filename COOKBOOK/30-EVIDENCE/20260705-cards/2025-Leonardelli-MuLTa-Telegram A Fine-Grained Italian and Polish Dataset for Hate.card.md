---
stem: "2025-Leonardelli-MuLTa-Telegram A Fine-Grained Italian and Polish Dataset for Hate"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, design-space, validity-psychometrics]
task_format: "free-text"
scoring_type: "classifier"
dataset_size: 3936
dataset_construction: "crowdsourced"
languages: ["it", "pl"]
models_tested: ["LLaMA 3.1 70B Instruct", "Llama-Guard-3-8B"]
headline_numbers:
  - "In-domain BERT (Exp2) vs. out-of-domain (Exp1): Italian F1 0.717 vs. 0.672; Polish F1 0.846 vs. 0.50 (p.7)"
  - "Multilingual BERT trained on human annotations: Italian 0.589, Polish 0.564 F1 (p.7)"
  - "Best Polish result: multitask BERT-cb-pl F1=0.871 (p.13)"
  - "Italian IAA Krippendorff's alpha=0.68; Polish=0.41 on 200-sample subset (p.4)"
---
## 1. Gist
MuLTa-Telegram introduces a 4,000-message Italian/Polish dataset of Telegram content annotated for hate speech and its target identity groups, covering 9 minority categories adapted from the Measuring Hate Speech corpus to a European context. The paper fills two gaps: the scarcity of hate speech resources for Polish, and the near-total absence of Telegram-specific (vs. Twitter-based) datasets. The core empirical finding—that models trained on existing out-of-domain Twitter data perform substantially worse than those trained on in-domain Telegram data—demonstrates domain specificity in hate speech detection. For values-alignment benchmarking, the paper offers a methodological model for multi-target, multilingual content annotation with explicit cross-domain degradation evidence, and a comparison of LLM-as-annotator vs. expert human annotation quality.

## 2. Benchmark/eval design features
Three-label annotation scheme per message:
1. Hate Speech: binary (Hate / No Hate)
2. Target of Hate: categorical from 9 predefined groups (LGBTQ+, Ethnicity/POC, Romani, Other/Migrants, Jews, Muslims, Christians, Women, Disability) + Other + No Target
3. Target Group Mention: multi-label presence of any of the 9 identity groups regardless of hateful intent

The multi-task setup (Experiment 5) jointly predicts hate speech and targets, using target mention as auxiliary signal. Seven experiments tested: out-of-domain BERT baselines, in-domain BERT fine-tuning, LLM-annotated training data, multilingual BERT, multi-task BERT, LLaMA 3.1 70B prompting, and LLaMA Guard zero-shot.

## 3. Task format & example item
Messages from Telegram channels annotated by native-speaker experts. Example from qualitative analysis (p.8):
- Hateful but missed by models: "i roma [...] non sono veri esseri umani, punto" ["the Roma [...] are not real human beings, period"] — dehumanization without explicit profanity
- Model false positive: "Una pacca sul sedere non autorizzata è una molestia sessuale" ["An unwarranted slap on the butt is sexual harassment"] — controversial opinion, not hate speech

Annotation guideline example (p.11):
"Classify as Hate Speech if it contains slurs or hostile language, motivated by bias or reinforcing stereotypes, targeted at a group or individual because of their actual or perceived innate characteristics."

## 4. Scoring / grading methodology
Binary classification evaluated via macro-F1. Target detection evaluated via per-category F1 (reported per model). Inter-annotator agreement: Krippendorff's alpha on 200-message subsets annotated by two native speakers per language. Final test set: 35% of data per language (~700 messages); training set: 65% (~1,300 per language).

## 5. Dataset construction & provenance
Data collected from public Telegram channels (Jan 2022–Jan 2023) using seed channels known to spread disinformation/hate (from Hatedemics project experts), expanded via snowballing using Telegram's channel recommendation feature. ~2.5M Italian messages and ~1.1M Polish collected. Pre-selection: 75% of annotated data chose using 145-keyword matrix (≥2 keywords per target group); 25% random sampling. Total: 2,002 Italian and 1,934 Polish messages, expertly annotated by 4 native speakers (2 Italian, 2 Polish). Anonymous: PII removed via regex, channel metadata deleted. Available at github.com/dhfbk/MuLTa-Telegram.

## 6. Validity evidence
IAA Krippendorff's alpha: Italian 0.68, Polish 0.41 (on 200-message subsets). Authors note these are in-line with comparable hate speech annotation work (e.g., Basile et al. 0.47 for Spanish). The qualitative error analysis (29 Italian + 30 Polish false negatives, 70 Italian + 3 Polish false positives) provides construct validity by identifying specific failure modes: implied hate, idiomatic disability references, anti-hate critiques misclassified as hate.

## 7. Saturation / discrimination
Binary hate speech detection is feasible (best macro-F1 ~0.87 for Polish, ~0.76 for Italian). Target identification is highly skewed: 9 of 11 target categories achieve F1=0.00 for most models in Italian. Only Ethnicity/POC (~0.66 Italian) and LGBTQ+ (~0.52 Polish) are reliably detectable. This reveals genuine difficulty for fine-grained hate target classification with currently available data volumes—a saturation floor, not a ceiling effect.

## 8. Multiturn / agentic aspects
n/a. Single-turn classification. LLaMA 3.1 70B used for annotation (Exp. 3) and classification (Exp. 6) but in single-turn inference mode.

## 9. Key numbers
- 2,002 Italian messages; 1,934 Polish messages; total ~3,936 (p.4)
- Italian hate speech: 411 messages (20.5%); Polish: 249 (12.9%) (p.4)
- IAA: Italian α=0.68; Polish α=0.41 (Krippendorff's, n=200 each) (p.4)
- Out-of-domain baseline: Italian F1=0.672, Polish F1=0.50 (Exp1) (p.7)
- In-domain BERT: Italian F1=0.717, Polish F1=0.846 (Exp2) (p.7)
- Multitask BERT (best): Italian F1=0.732, Polish F1=0.801 (Exp5) (p.7)
- Multilingual BERT: Italian 0.589, Polish 0.564 (Exp4) (p.7)
- LLM-annotated training data: Italian F1=0.705, Polish F1=0.658 (Exp3) (p.7)
- LLaMA 3.1 70B prompted: Italian F1=0.732, Polish F1=0.678 (Exp6) (p.7)
- LLaMA Guard zero-shot: Italian F1=0.712, Polish F1=0.58 (Exp7) (p.7)
- Target F1: Italian Ethnicity/POC=0.66, LGBTQ+=0.24; all others ≈0.00 (p.7)
- Polish LGBTQ+ target F1: 0.52 (highest for Polish) (p.7)
- Multilingual BERT on LLM-annotated data: Italian 0.674, Polish 0.657 (vs. 0.589/0.564 on human) (p.8)

## 10. Pitfalls & limitations
Author-admitted:
- Low Polish IAA (0.41) suggests annotation inconsistency (p.4)
- Very few examples for most target groups; target identification remains unsolved (p.9)
- LLM (LLaMA) weak on Polish due to limited Polish coverage in pretraining (p.9)
- Multilingual BERT degraded by cross-language annotation inconsistency (p.8)

Additional observations:
- 75% keyword-pre-selected sampling over-represents hate speech and specific targets, so the dataset is not representative of natural Telegram content distributions
- Annotators worked asynchronously without inter-annotator discussion, likely reducing agreement
- "Other" target category (115 Italian, 55 Polish hateful messages) is large and heterogeneous, limiting interpretability
- False negative qualitative analysis shows models still poorly handle implicit hate, idiomatic language, and slurs in non-standard varieties

## 11. Novel ideas worth stealing
1. **Target mention as auxiliary task**: Annotating target identity group mentions separately from target-of-hate (even in non-hateful messages) provides richer training signal and enables multi-task learning that improves main task performance. This decoupled annotation is generalizable to any content safety benchmark needing fine-grained group sensitivity.
2. **In-domain vs. out-of-domain degradation as benchmark validity evidence**: Explicitly measuring performance drop when training on Twitter data vs. Telegram data provides principled motivation for new datasets. This "domain gap proof" should be a standard component of dataset papers.
3. **LLM-as-annotator comparison**: Testing LLaMA 3.1 70B as a label-generator for training data (Exp3) vs. human expert annotations (Exp2) provides a direct quality comparison within the same evaluation framework. Using LLM-annotated multilingual data (Exp4 variant) also revealed that annotation consistency—not just data volume—drives multilingual performance.
4. **Snowball channel discovery**: The snowballing strategy using Telegram's recommendation network is a principled data collection approach for finding related extremist content without relying on keyword search alone.
5. **Annotating non-hate content for target mentions**: Including target-group mentions in non-hateful messages (75% of dataset has target keywords) prevents models from conflating topic and hatred, a common failure mode in hate speech datasets.

## 12. Notable quotes
"Training on existing out-of-domain data leads to poor results on Telegram data, underscoring the necessity of in-domain datasets for effective hate speech detection." (p.1)

"Models seem unable to detect hateful content when not presented in a standard explicitly offensive form. Performance tends to be low when examples include hashtags [...]; dehumanization being implied [...]; slurs in non-standard language varieties." (p.8)

"LLaMA Guard, despite its safety orientation, performs poorly in this out-of-domain context, while LLaMA shows strong performance on Italian, but its accuracy drops on Polish data, likely due to limited language coverage during pretraining." (p.9)

"While the vast majority of hate speech research has been conducted on English, we focused on underrepresented languages." (p.9)

## 13. UNKNOWN / not in extract
- Details on seed channel selection criteria beyond "known to spread disinformation or hate"
- Full keyword matrix (145 keywords referenced, available on GitHub but not in extract)
- Number of channels collected from (only total message counts given)
- Exact compensation or conditions for expert annotators
- Whether Polish and Italian annotation guidelines had language-specific divergences beyond the Russia-Ukraine war exceptions shown
- Full annotation guidelines for Mention of Target Group Detection (partial reproduction in appendix)
