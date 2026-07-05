---
stem: "2024-Karpov-Inducing Human-like Biases in Moral Reasoning"
reader_model: "opus"
confidence: "high"
is_benchmark: false
theme_tags: [moral-psychology, validity-psychometrics, normative-ethics]
task_format: "MCQ"
scoring_type: "exact-match"
dataset_size: null
dataset_construction: "n/a"
languages: [en]
models_tested: ["BERT-base-cased", "BERT-large-cased", "RoBERTa-large", "DeBERTa-v2-xlarge"]
headline_numbers: ["RoBERTa-large best ETHICS CS test 80.6% mean / 91.4% max (p.3)", "Brain scores 0.14-0.27 PCC, not improved by fMRI fine-tuning (p.4)", "450 fine-tuning runs, 292 GPU-hours, 1,082 models (p.2)", "fMRI atlas = 1,024 DiFuMo ROIs (p.2)"]
---
## 1. Gist
This is a NeuroAI methods paper, not a benchmark. It fine-tunes encoder LLMs (BERT/RoBERTa/DeBERTa) on the Commonsense split of the ETHICS moral-reasoning benchmark and/or on human fMRI data from a moral-judgment task, then measures both ETHICS accuracy and "BrainScore" (correlation between model activations and human brain activity). The central (negative) result: fine-tuning on moral-reasoning fMRI data did NOT significantly improve brain-model alignment nor ETHICS accuracy beyond fine-tuning on ETHICS alone. Its relevance to values-alignment benchmarking is peripheral but conceptually interesting: it probes whether grounding moral-reasoning models in human neural representations is a viable alignment signal, and it reuses ETHICS as the moral-reasoning task.

## 2. Benchmark/eval design features
Two evaluation axes: (1) accuracy on ETHICS Commonsense split (multiple-choice moral judgment, via a CLS classification head); (2) BrainScore = Pearson correlation between predicted and held-out fMRI activity across 1,024 DiFuMo ROIs, computed per-layer and aggregated. Human fMRI from Koster-Hale et al. 2013 ("Moral judgments of intentional and accidental moral violations across Harm and Purity domains"), subjects rated actions 1-4 on morality. NeuroSynth meta-analysis isolates four ROI themes: Theory of Mind, moral reasoning, language, and vision (control). Multiple fMRI sampling strategies tested (AVG/LAST/MIDDLE/SENTENCES).

## 3. Task format & example item
Uses ETHICS Commonsense multiple-choice moral judgment items (not authored here); no verbatim item reproduced in extract. "n/a" for a quoted example.

## 4. Scoring / grading methodology
ETHICS: exact-match classification via linear head on [CLS] token, reported as % accuracy on CS Hard Set and CS Test Set with 95% CIs. BrainScore: Pearson correlation coefficient between regression-predicted and actual held-out fMRI ROI activity, sampled at time points accounting for hemodynamic lag; also visualized via Coefficient of Determination on cortical surface (negative-log-transformed, probabilistic-atlas weighted). Significance via one-tailed Bonferroni-corrected tests (Figs 13-20).

## 5. Dataset construction & provenance
No new dataset created. ETHICS benchmark (Hendrycks et al. 2020) for behavioral moral data. fMRI: Koster-Hale et al. 2013 (IRB-approved, consented, paid subjects), preprocessed by Thomas et al. 2023 with DiFuMo 1,024-ROI atlas. NeuroSynth for ROI-theme mapping. Code released on GitHub.

## 6. Validity evidence
BrainScore methodology inherits from established NeuroAI (Schrimpf Brain-Score, Aw & Toneva). Vision ROIs used as a control group — models did not beat control, indicating the fine-tuning failed to achieve targeted neural alignment (a clean negative control design). Larger models scored higher on both accuracy and BrainScore, consistent with Hendrycks et al. Confidence intervals (two-SD) reported for accuracy.

## 7. Saturation / discrimination
Accuracy spreads widely by model (DeBERTa CS test mean 52.9% to RoBERTa 80.6%, p.3) with high max values (up to 92.3%). BrainScores are low and narrow (0.14-0.27 PCC, p.4) with substantial SD, showing limited discrimination and large remaining headroom for brain alignment. Some fine-tuned accuracies exceeded originally reported ETHICS numbers (bolded, Table 1).

## 8. Multiturn / agentic aspects
n/a — static classification and representational-similarity analysis.

## 9. Key numbers
- ETHICS CS Test mean/max: BERT-base 57.0/73.7, BERT-large 62.0/85.4, RoBERTa-large 80.6/91.4, DeBERTa 52.9/70.0 (ETHICS-only) (Table 1, p.3).
- Adding fMRI did not beat ETHICS-only for RoBERTa (79.0 vs 80.6) (p.3).
- Brain scores (PCC, LAST sampling): BERT-large 0.217 (no-FT) vs 0.213 (ETHICS+fMRI); RoBERTa 0.173 no-FT vs 0.156; DeBERTa 0.271 no-FT vs 0.273 (Table 2, p.4).
- 450 fine-tuning runs, 292 hours, 1,082 models (p.2).
- 4 models: BERT-base 108M, BERT-large 333M, RoBERTa-large 355M, DeBERTa-v2-xlarge 864M (p.2).
- DiFuMo atlas 1,024 ROIs (p.2); LAST sampling gave best accuracy (p.3).

## 10. Pitfalls & limitations
Author-admitted: fine-tuning did not significantly increase brain alignment or beat control (vision) ROIs (p.8); attribute failure to small fMRI dataset and possibly ineffective fine-tuning methods; call for larger neural datasets. Reader-observed: single small fMRI study limits generalization; only encoder models (compute constraints), so findings may not transfer to modern decoder LLMs; brain-score improvements not disentangled from accuracy improvements; ETHICS accuracy variance is huge (wide CIs, small run counts for some cells, e.g. DeBERTa+fMRI n=3), weakening claims; the paper is a preprint from a research camp, preliminary by its own framing.

## 11. Novel ideas worth stealing
- Using a vision-ROI control group as a negative baseline for representational-alignment claims — directly transferable rigor for any "model matches human X" values claim: always include a control dimension you expect NOT to move.
- BrainScore as an auxiliary alignment target: the idea of grounding moral-reasoning evaluation in human neural (not just behavioral) representations, decomposed into Theory-of-Mind vs moral-reasoning vs language ROIs.
- Systematically varying temporal sampling (AVG/LAST/MIDDLE/SENTENCES) of a noisy human signal and reporting which best predicts behavior — analogous to testing multiple aggregation windows when deriving human ground truth from surveys.
- Reporting per-layer alignment to locate where moral representations live, rather than a single scalar.
- Honest publication of a negative result with released code — useful for a knowledgebase on what does NOT work for alignment grounding.

## 12. Notable quotes
- "we undertake the first such measurement (BrainScore) of the similarity of the internal representations of biological brains... and large language models (LLMs), in the domain of moral reasoning" (p.1).
- "While our attempts here proved unsuccessful, we think this is an important problem to study and that increasing said alignment might be important for the AI alignment problem" (p.1).
- "our models were not able to achieve better brain scores than the control group, meaning that our experiment did not achieve the desired effect." (p.8).
- "our work is ample evidence for the importance of gathering more data on moral reasoning... if future researchers want to increase brain-model alignment" (p.3).

## 13. UNKNOWN / not in extract
- Number of ETHICS items / fMRI scenarios (dataset sizes not stated numerically here).
- Exact BrainScore significance p-values (shown only as asterisks in figures).
- Number of human subjects in the Koster-Hale fMRI dataset.
- Whether any decoder/generative LLMs were tried beyond encoder models.
