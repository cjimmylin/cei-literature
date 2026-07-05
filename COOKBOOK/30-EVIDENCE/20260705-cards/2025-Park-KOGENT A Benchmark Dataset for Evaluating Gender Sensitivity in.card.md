---
stem: "2025-Park-KOGENT A Benchmark Dataset for Evaluating Gender Sensitivity in"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, llm-judges-scoring]
task_format: "MCQ"
scoring_type: "exact-match"
dataset_size: 6024
dataset_construction: "scraped"
languages: [ko, en]
models_tested: ["GPT-4o (gpt-4o-2024-11-20)", "GPT-4.1 (gpt-4.1-2025-04-14)"]
headline_numbers: ["GPT-4.1 F1 for H label 87.5% zero-shot, 91.2% 18-shot (p.2)", "GPT-4o F1 for H label 90.4% zero-shot, 91.1% 18-shot (p.2)", "6,024 annotated utterances from 1,222 transcripts (p.2)", "Krippendorff's Alpha 0.983 at 0.9 cosine threshold (p.6)"]
---
## 1. Gist
KOGENT (KOrean GENder-sensitivity Tagged dataset) is a human-annotated benchmark of 6,024 utterances drawn from 1,222 Korean National Assembly transcripts spanning 1948-2024, each labeled High or Low in gender sensitivity and tagged with the target group. It matters for values-alignment benchmarking because it tests whether multilingual LLMs can detect *culturally grounded, context-dependent* gender bias in formal, self-monitored political discourse — a "challenging flavor" where overt discrimination is rare and biases hide in nuance. It also uniquely includes positive/inclusive language (not just hate speech), and probes sociocultural alignment of LLMs in a non-Anglophone, gender-charged context (South Korea ranks 122/193 in female legislators).

## 2. Benchmark/eval design features
Construct measured: "gender sensitivity" — capacity to recognize gender-based differences, inequalities, biases, and reflect awareness through language. Binary label: High (recognizes discrimination, affirms diversity, empathetic cross-gender framing) vs Low (denies inequality, rejects diversity, gender-stereotyped expressions). Each utterance also tagged with target group (women, men, sexual minorities, all genders). Technical validation adds a third "Irrelevant" (I) class extracted from a separate parliamentary corpus, making the model task a 3-way classification (H/L/I). Answer space is a single categorical label.

## 3. Task format & example item
The model receives a system prompt with a Korean definition of gender sensitivity and, per input, the user prompt format: "문장 (Sentence): [input sentence]\n판단 (Label):" requiring output of one label H, L, or I (p.8). Example (verbatim, English gloss): a Low-labeled challenge — "Women inevitably take parental leave due to childcare responsibilities, but even taking a single day can be burdensome…" was intended as H (reflecting disproportionate burden) but models misread as stereotype (p.8).

## 4. Scoring / grading methodology
Exact-match classification of predicted label against ground-truth human label. Metrics reported: precision, recall, F1 per label (H, I, L). Four experimental conditions: zero-shot GPT-4o, 18-shot GPT-4o, zero-shot GPT-4.1, 18-shot GPT-4.1. Temperature 0.0, max_tokens 2, each utterance classified independently (no memory) via OpenAI API (p.8).

## 5. Dataset construction & provenance
Source: Open Assembly Data Portal, all sessions 1948-2024 (29,309 meeting records, ~13.75M speech turns). Keyword-based sampling: 1,222 transcripts each with ≥20 gender-related keyword occurrences (p.4). 15 trained annotators (poli-sci / Korean-studies students) segmented turns into utterances, dual-coded each transcript. 6,024 utterances: 3,868 H, 2,156 L. English-translated 600-utterance subset (professionally human-translated to avoid model contamination). I-labels: 2,889 finalized from NIKL Korean Parliamentary Corpus 2021, non-overlapping, manually filtered. Publicly available on Figshare (DOI 10.6084/m9.figshare.30413125.v4); code on GitHub. License CC BY-NC-ND 4.0.

## 6. Validity evidence
Intercoder reliability computed via cosine-similarity-thresholded agreement: at 0.9 threshold, 590 matches / 5 disagreements, mean 0.992, Cohen's Kappa 0.983, Krippendorff's Alpha 0.983 (p.6). At 0.3 threshold Kappa still 0.943. All 77 disagreed utterances adjudicated by first author. Annotators trained for diachronic variation (period-specific norms) with calibration sessions. Construct grounded in gender-studies definition (ref 12).

## 7. Saturation / discrimination
Models already achieve high F1 on H (90-91%) and I (85-87%), but L (Low sensitivity) remains hardest: F1 76-81%, with recall for L only ~68-74% (Tables 3-4, p.8) — substantial headroom on detecting subtle/embedded discriminatory language. Few-shot gains modest (H +0.79% GPT-4o, +4.16% GPT-4.1), suggesting the benchmark is not yet saturated for nuanced cases especially in extended contexts.

## 8. Multiturn / agentic aspects
n/a — single-turn independent classification.

## 9. Key numbers
- 6,024 annotated utterances from 1,222 transcripts; 3,868 H / 2,156 L (p.6)
- Target groups: women 4,844; men 416; sexual minorities 269 (185 L vs 84 H); all genders 495 (p.6)
- GPT-4o F1: H 90.39→91.10, I 86.97→87.34, L 77.99→81.13 (zero→18-shot) (p.8)
- GPT-4.1 F1: H 87.51→91.15, I 84.26→85.48, L 76.83→76.25 (zero→18-shot) (p.8)
- Krippendorff's Alpha 0.983 (0.9), 0.961 (0.7), 0.952 (0.5), 0.944 (0.3) (p.6)
- Source corpus: 29,309 meetings, ~13.75M speech turns (p.4); 2,889 I-labels (p.8)

## 10. Pitfalls & limitations
Author-admitted: models fail to distinguish criticisms vs reinforcements of inequality; miss recent/low-frequency terminology (e.g., cechwulsayng "low birth"); fail to detect discriminatory terms embedded in longer contexts (semantic-flow prioritization over subtle bias) (p.9). Temporal/institutional confounds (7-decade span, keyword sampling bias, 2002 Gender Equality Committee) may distort longitudinal trends (p.10). Seen flaws: binary H/L collapses gradations; heavy class imbalance (women dominate); reliability computed only on high-similarity utterance pairs may overstate agreement; only two closed GPT models tested.

## 11. Novel ideas worth stealing
- **Include inclusive/positive language, not just harmful** — labeling High-sensitivity (affirming) utterances alongside Low, enabling measurement of a values *spectrum* rather than harm-detection only.
- **"Challenging flavor" corpus design**: deliberately sampling formal, self-monitored discourse where bias is indirect — a robustness stress-test for detectors that over-rely on overt toxicity cues.
- **Diachronic calibration**: training annotators to judge items within their own historical era's norms, with cross-decade calibration sessions — reusable for any values benchmark spanning shifting norms.
- **Separate annotation of quoted vs original speech** to preserve stance (criticizing a bias vs endorsing it) — directly addresses a failure mode models exhibit.
- **Cosine-similarity-stratified reliability matrix** as a transparent IRR reporting device.
- **Culturally untranslatable terms** kept in-language with native-language prompts to preserve pragmatic nuance — a template for non-English values evals.

## 12. Notable quotes
- "legislative discourse a 'challenging flavor' for bias detection - precisely the kind that robust NLP systems should be able to handle." (p.3)
- "LLMs often fail to reflect the values, norms, and moral reasoning embedded in non-Anglophone contexts" (p.4)
- "the model, while adept at contextual comprehension, sometimes prioritizes overall semantic flow over the detection of subtle gender bias" (p.9)
- "we finalized a set of 2,889 I-labeled utterances for use in the classification experiment." (p.8)

## 13. UNKNOWN / not in extract
Exact prompt wording (only format shown); Table S1/S2 contents; supplementary Cohen's Kappa/Alpha formulas; per-model accuracy breakdown by target group; cost of API experiments; whether translation subset was used in scoring; annotator demographics beyond field of study; licensing details of the I-label source corpus for redistribution.
