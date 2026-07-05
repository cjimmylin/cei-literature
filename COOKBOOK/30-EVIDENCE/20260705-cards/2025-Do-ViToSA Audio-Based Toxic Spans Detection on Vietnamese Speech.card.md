---
stem: "2025-Do-ViToSA Audio-Based Toxic Spans Detection on Vietnamese Speech"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, saturation-discrimination]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: 11802
dataset_construction: "scraped"
languages: [vi]
models_tested: [Whisper, wav2vec2-base-vi-vlsp2020, wav2vec2-base-vietnamese-250h, PhoWhisper, XLM-R, mBERT, DistilBERT, PhoBERT, ViSoBERT, CafeBERT, ViHateT5]
headline_numbers: ["11,802 audio-transcript pairs, 24.75 hours (p.2)", "Whisper WER drops 1.149→0.289 overall after VITOSA fine-tuning (p.4)", "PhoBERT best TSD Macro-F1 0.837 (p.4)", "1,000 held-out test samples (p.2)"]
---
## 1. Gist
ViToSA (Vietnamese Toxic Spans Audio) is the first dataset and benchmark for fine-grained toxic-span detection in Vietnamese *speech*, comprising ~11,802 human-transcribed audio clips (24.75 hours) scraped from Facebook/YouTube/TikTok. It couples an ASR stage (transcribe speech) with a text Toxic-Spans-Detection stage (localize toxic words). For values-alignment benchmarking it matters as a low-resource, non-English, multimodal safety benchmark: it operationalizes "toxicity" not as an utterance-level label but as precise span localization within transcribed speech, and it demonstrates that general ASR models systematically mis-transcribe toxic vocabulary — an under-appreciated failure mode for audio content moderation.

## 2. Benchmark/eval design features
Two chained tasks over the same audio: (1) ASR — spoken utterance → normalized transcript, scored by WER separately for toxic vs. non-toxic vs. all segments; (2) TSD — transcript → labeled toxic spans (character/word positions), scored by Accuracy, Weighted-F1, Macro-F1. Test set (1,000 samples) is a triplet of {audio, human transcript, annotated toxic spans}, constructed *before* the training set to serve as a reliable benchmark (p.2). Answer space for TSD is a per-token toxic/non-toxic labeling scheme. Clips range 1–14 seconds; <1s discarded (insufficient context), >14s split (annotator cognitive load) (p.2).

## 3. Task format & example item
ASR ground-truth example (p.2): "thì đéo nói địt mẹ mày nó đến bốn năm lần thì đỡ thế lồn nào được" (English gloss provided: "hadn't fucking said anything, but your fucking mother came four or five times, how the fuck could it be better?"). TSD output: transcript with predicted toxic spans highlighted (bold red in Fig 4, p.3). The utterance is deliberately profane social-media speech.

## 4. Scoring / grading methodology
ASR: Word Error Rate (WER), reported split by toxic/non-toxic/all. TSD: following Hoang et al. (ViHOS) methodology — Accuracy, Macro-F1 (MF1), Weighted-F1 (WF1) (p.4). Human annotation quality itself was scored via inter-annotator WER during a calibration "challenge" (threshold 8%). No LLM-judge; scoring is exact-match/reference-based for ASR and classifier-metric for TSD.

## 5. Dataset construction & provenance
Videos manually gathered from Facebook, YouTube, TikTok; audio extracted via SoundFile, segmented with Audio Cutter (p.2). Paid undergraduate annotators (local minimum wage). Transcription calibration: 50 files, annotators paired blind, three rounds until pair-WER <8%. Quality control: group B re-checks 20% of each group-A annotator's output against ground truth at 8% WER threshold; failures re-transcribe (p.2). Final: 24.75 hours, 11,802 pairs; 1,000 for test, remainder split 8:2 train/val (p.2). TSD models fine-tuned on the *external* ViHOS text dataset, then evaluated on ViToSA. Public on HuggingFace (ViToSAResearch/ViToSA_Dataset) and GitHub (p.1-2).

## 6. Validity evidence
Inter-annotator reliability enforced via WER<8% across three calibration rounds plus a 20% double-check pass — a concrete reliability control (p.2). Criterion signal: fine-tuning on ViToSA reduces toxic-word WER dramatically, and post-fine-tuning outputs (Table 4) correctly recover nearly all toxic words, validating the dataset's coverage of toxic vocabulary. Cross-model comparison (7 TSD models, 4 ASR models) provides discrimination evidence. No human baseline on the TSD task itself beyond the annotation gold.

## 7. Saturation / discrimination
TSD scores are high and somewhat compressed at the top: Accuracy 0.927–0.951, WF1 0.932–0.955 across strong models, but Macro-F1 spreads more (0.500 for ViHateT5 up to 0.837 PhoBERT) (p.4) — MF1 is the discriminating metric because minority toxic-span classes are harder. ASR WER remains "relatively high" even after fine-tuning (~0.29–0.31 overall), leaving clear headroom (p.4). Authors note full-sentence ASR is still imperfect but toxic-word recovery is the objective.

## 8. Multiturn / agentic aspects
n/a — a two-stage batch pipeline (ASR then TSD), no interaction, tools, or multiturn dialogue.

## 9. Key numbers
- Dataset: 11,802 audio-transcript pairs, 24.75 hours; test=1,000, rest 8:2 train/val (p.2)
- ASR WER without VITOSA (toxic/non/all): Whisper 1.660/0.593/1.149; PhoWhisper 0.615/0.212/0.418 (p.4)
- ASR WER with VITOSA: Whisper 0.325/0.264/0.289 (↓0.860 all); wav2vec2-vlsp 0.319/0.302/0.310 (↓0.676); PhoWhisper 0.302/0.192/0.257 (p.4)
- TSD Macro-F1: PhoBERT 0.837, ViSoBERT 0.817, CafeBERT 0.807, XLM-R 0.790, BERT 0.768, DistilBERT 0.732, ViHateT5 0.500 (p.4)
- TSD Accuracy: PhoBERT 0.951 (best), ViHateT5 0.765 (worst) (p.4)
- ViHOS original best PhoBERT-large MF1 0.772, exceeded by ViToSA normalized-text results (p.4)
- Clip length 1–14s; calibration WER threshold 8% (p.2)
- ASR trained 10 epochs, lr 5e-5; TSD 4 epochs, lr 2e-5; single A100 (p.3-4)

## 10. Pitfalls & limitations
Author-noted: ASR WER remains high, causing some full-sentence inaccuracies (p.4). Observed flaws: TSD models are fine-tuned on ViHOS text, not on ViToSA transcripts, so the "benchmark" for TSD is a transfer setting; error propagation from ASR into TSD is not isolated (a wrong transcription cannot yield a correct span, but that interaction is not decomposed). ViHateT5's poor MF1 (0.500) may reflect a domain-shift artifact (social-media vs normalized text) rather than model weakness — a confound the authors acknowledge. Toxicity is defined operationally by annotators without a published taxonomy in the extract. Vietnamese-only; single-dialect coverage unclear. Ethical: contains real offensive content by design.

## 11. Novel ideas worth stealing
- **Span-level rather than utterance-level safety labels for audio**: localizing exactly which words are toxic is far more informative for moderation and for measuring model precision than binary utterance classification — portable to any values benchmark that wants graded, localizable harm.
- **Toxic vs. non-toxic WER decomposition**: reporting recognition error *stratified by the sensitive category* exposes that general models silently fail exactly on the safety-critical tokens — a reusable "does the model even perceive the harmful content?" diagnostic.
- **Test-set-first construction**: building and freezing the evaluation set before the training set to guarantee a clean benchmark and reduce contamination.
- **Blind-paired annotator calibration with a WER gate + 20% QC resample**: a cheap, quantitative inter-annotator reliability protocol adaptable to any transcription/labeling benchmark.
- **Cross-corpus transfer eval** (fine-tune on ViHOS text, test on ViToSA speech transcripts) as a generalization stress-test.

## 12. Notable quotes
- "existing studies often focus on utterance-level classification and lack the ability to detect toxic segments within speech." (p.1)
- "these models are typically trained on datasets with limited coverage of toxic vocabulary, leading to subpar performance in recognizing toxic speech" (p.2)
- "After three rounds, all pairs achieved WER below 8%, ensuring high-quality data." (p.2)
- "the first benchmark for detecting toxic spans in Vietnamese speech, addressing the gap in audio-based toxicity detection for low-resource languages." (p.4)

## 13. UNKNOWN / not in extract
- The toxicity definition/taxonomy and annotation guideline details.
- Number of unique annotators and demographic composition.
- Licensing terms of the released dataset.
- Whether span boundaries are character- or token-level, and exact labeling scheme format.
- Statistical significance / variance of the reported metrics (single-run numbers).
- End-to-end pipeline score combining ASR error with TSD (only components reported separately).
