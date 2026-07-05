---
stem: "2023-Maity-Ex-ThaiHate A Generative Multi-task Framework for"
reader_model: "sonnet"
confidence: "low"
is_benchmark: true
theme_tags: [cultural-linguistic, design-space, validity-psychometrics]
task_format: "generative"
scoring_type: "classifier"
dataset_size: null
dataset_construction: "crowdsourced"
languages: ["th"]
models_tested: []
headline_numbers: []
---
## 1. Gist
Ex-ThaiHate (ECML PKDD 2023, Springer) introduces the first benchmark hate speech corpus in Thai with four simultaneous annotation types: hate speech classification, sentiment, emotion, and rationale (explainability markers indicating which phrases trigger the classification). The paper also proposes GenX, a unified generative framework that reframes multi-task hate speech detection as a text-to-text generation problem. For values-alignment benchmarking, this paper is significant because it demonstrates multi-label annotation at the sub-sentence level (rationales) for a Southeast Asian language, and because the generative reframing of hate detection anticipates the kind of open-ended model evaluation relevant to LLM-based values assessment.

## 2. Benchmark/eval design features
The Ex-ThaiHate corpus annotates Thai social media posts across four tasks simultaneously:
1. Hate speech binary label (hate / not-hate).
2. Sentiment label (positive / negative / neutral).
3. Emotion label (multiple emotion categories).
4. Rationale spans — sub-sentence annotations marking which phrases justify the hate speech classification (explainability).

GenX treats all four tasks as a single seq2seq problem: the model generates a structured output that contains hate label, sentiment, emotion, and rationale in a single pass. This multi-task generative design is novel because it elicits explanations alongside classifications.

## 3. Task format & example item
Generative: given a Thai social media post, generate a structured output containing hate label, sentiment, emotion, and rationale. No verbatim example item available (full text unavailable).

## 4. Scoring / grading methodology
Multi-task classification performance. Since output is generative, scoring likely uses structured extraction from generated text compared against gold annotations. Specific metrics not confirmed from extract.

## 5. Dataset construction & provenance
Source: Thai social media posts. Annotation: crowdsourced with four label types including rationale spans. First Thai hate speech corpus with explainability annotations. Dataset size not confirmed.

## 6. Validity evidence
Full text unavailable; inter-annotator agreement not confirmed.

## 7. Saturation / discrimination
Full text unavailable; not confirmed.

## 8. Multiturn / agentic aspects
n/a — single-turn generative classification.

## 9. Key numbers
- Full text unavailable; no page-referenced numbers can be confirmed.

## 10. Pitfalls & limitations
- Full text unavailable; limitations not confirmed.
- Crowdsourced annotation of emotion and rationale in a low-resource language may have lower inter-annotator reliability than expert annotation.
- GenX performance likely depends on Thai-language generative model availability, which is limited compared to English.
- The four-task simultaneous annotation may introduce label dependencies (e.g., hate label influencing emotion annotation).

## 11. Novel ideas worth stealing
- Rationale/span annotation as a benchmark design principle: annotating not just the label but which phrases justify the label makes evaluation richer and enables evaluation of model explanations, not just predictions.
- Multi-task generative framing as an eval paradigm: instead of separate classifiers per dimension, a single generative model produces a structured multi-field output — this is directly applicable to values-alignment evaluation where you want to know not just a verdict but the moral reasoning behind it.
- Thai-specific benchmark demonstrates that low-resource, tonal languages can support sophisticated multi-label annotation — a template for other Southeast Asian language benchmarks.

## 12. Notable quotes
- Full text unavailable; no verbatim quotes can be confirmed.

## 13. UNKNOWN / not in extract
- Full paper text unavailable (extract_quality: missing).
- Dataset size.
- Performance numbers for GenX vs. baseline models.
- Inter-annotator agreement statistics.
- Whether the corpus is publicly released.
- Page numbers for all claims.
