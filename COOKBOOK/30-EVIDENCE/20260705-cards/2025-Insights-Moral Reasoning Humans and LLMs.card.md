---
stem: "2025-Insights-Moral Reasoning Humans and LLMs"
reader_model: "sonnet"
confidence: "low"
is_benchmark: false
theme_tags: [moral-psychology, normative-ethics, cultural-linguistic]
task_format: "mixed"
scoring_type: "behavioral"
dataset_size: null
dataset_construction: "survey-derived"
languages: ["en"]
models_tested: []
headline_numbers: []
---
## 1. Gist
Published in Journal of Media Ethics (2025), this comparative study examines moral reasoning differences between humans and LLMs. Drawing on Moral Foundations Theory (MFT) and Dual Process Theory, the paper contrasts how humans and AI systems approach ethical judgment. Published in a media ethics context, this work is relevant to values-alignment benchmarking as an empirical examination of where LLM moral reasoning diverges from human moral cognition — pointing to which dimensions of moral judgment remain underevaluated in existing benchmarks.

## 2. Benchmark/eval design features
The paper is an empirical comparative study (not a benchmark itself). It applies two established frameworks: Moral Foundations Theory (MFT, measuring harm/care, fairness, loyalty, authority, purity foundations) and Dual Process Theory (System 1 intuitive vs. System 2 deliberate reasoning). The study compares human participants to LLMs on moral reasoning tasks. Key research questions likely include: Do LLMs activate the same moral foundations as humans? Do they show the same intuitive-vs-deliberate reasoning patterns? How do media-related ethical scenarios reveal gaps?

## 3. Task format & example item
Full text unavailable — specific example items cannot be provided. Based on MFT and dual process frameworks, tasks likely include moral vignettes, the Moral Foundations Questionnaire (MFQ), or dilemma scenarios designed to activate specific moral foundations.

## 4. Scoring / grading methodology
Behavioral scoring: categorizing LLM responses by moral foundation activated and/or reasoning style (intuitive vs. deliberate). Specific coding scheme unknown without full text.

## 5. Dataset construction & provenance
Likely survey-derived, using established MFT instruments (MFQ) and moral dilemma stimuli. Specific datasets, human participant demographics, and LLM versions unknown without full text.

## 6. Validity evidence
Use of established, validated instruments (MFT, MFQ) provides construct validity grounding. Comparison with human baselines provides criterion validity. Specific reliability statistics unknown without full text.

## 7. Saturation / discrimination
Unknown — full text unavailable.

## 8. Multiturn / agentic aspects
n/a — standard single-turn moral reasoning evaluation.

## 9. Key numbers
- Published in Journal of Media Ethics (2025).
- DOI: 10.1080/23736992.2025.2553146.
- mp_mft score: 60, mp_dual_process score: 60 (vault metadata indicating strong relevance to both frameworks).

## 10. Pitfalls & limitations
- MFT is itself a WEIRD-biased framework; using it as the primary lens may miss non-Western moral foundations.
- Human participants in media ethics studies are often WEIRD college students, limiting generalizability.
- LLM responses to MFQ/moral dilemmas may not reflect underlying "moral reasoning" but training-data pattern-matching.
- Journal of Media Ethics context suggests focus on journalism/media scenarios, limiting generalizability.

## 11. Novel ideas worth stealing
- MFT as a multi-dimensional scoring framework for values-alignment benchmarks: instead of single right/wrong scores, evaluate which moral foundations a model activates and whether the foundation mix matches human patterns.
- Human-LLM comparison design: using the same instruments on both human participants and LLMs creates directly interpretable gaps that can guide benchmark design.
- Dual-process operationalization: using time pressure, distractor tasks, or few-shot prompting to manipulate System 1 vs. System 2 engagement in LLMs.

## 12. Notable quotes
Full text unavailable — no quotes recoverable.

## 13. UNKNOWN / not in extract
- Full text unavailable; all specific findings, quantitative results, and methodology details are unknown.
- Specific LLMs evaluated.
- Human participant sample size and demographics.
- Which moral foundations showed the largest human-LLM gaps.
- Media-specific scenarios used.
