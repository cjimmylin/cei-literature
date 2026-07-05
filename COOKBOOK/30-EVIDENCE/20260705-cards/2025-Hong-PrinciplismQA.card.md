---
stem: "2025-Hong-PrinciplismQA"
reader_model: "sonnet"
confidence: "low"
is_benchmark: true
theme_tags: [normative-ethics, best-practices, validity-psychometrics, design-space]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: 3648
dataset_construction: "scraped"
languages: ["en"]
models_tested: ["GPT-4.1", "o3", "Claude Sonnet 4", "Gemini 2.5 Flash", "DeepSeek", "Qwen", "Llama"]
headline_numbers: ["3,648 questions total", "2,182 multiple-choice questions", "1,466 open-ended questions", "350 medical ethics textbooks and JAMA Ethics cases sourced", "20+ LLMs evaluated", "12 medical expert annotators"]
---
## 1. Gist
PrinciplismQA is a comprehensive benchmark for evaluating LLMs on medical ethics, grounded in the Beauchamp-Childress four principles of biomedical ethics: autonomy, beneficence, non-maleficence, and justice. With 3,648 questions sourced from 350 medical ethics textbooks and JAMA Ethics cases, it is the first benchmark explicitly organized around this dominant framework in clinical bioethics. The benchmark reveals that LLMs struggle most with beneficence reasoning. For values-alignment benchmarking, it is a model case of using an established normative framework to organize evaluation, combining MCQ and open-ended formats, and drawing on expert-annotated real-world materials.

## 2. Benchmark/eval design features
PrinciplismQA is organized by four ethical principles from Beauchamp-Childress biomedical ethics: autonomy, beneficence, non-maleficence, and justice. It contains 3,648 questions: 2,182 MCQ and 1,466 open-ended. Sources include 350 medical ethics textbooks and JAMA Ethics cases. Annotated by 12 medical experts. Tests 20+ LLMs including frontier models (GPT-4.1, o3, Claude Sonnet 4, Gemini 2.5 Flash) and domain-specific medical models (DeepSeek, Qwen, Llama variants). Key finding: significant performance gaps across models, with beneficence reasoning being the hardest.

## 3. Task format & example item
Mixed format: 2,182 MCQ and 1,466 open-ended questions. Full text unavailable — verbatim example items cannot be provided. Based on the abstract, items likely present clinical scenarios requiring application of one or more of the four principles, with MCQ options representing different ethical stances.

## 4. Scoring / grading methodology
MCQ: likely exact-match or near-exact-match scoring. Open-ended: likely LLM-judge or rubric-based scoring. Mixed scoring methodology. Specific rubric details unknown without full text.

## 5. Dataset construction & provenance
- Source: 350 medical ethics textbooks and JAMA Ethics cases
- Size: 3,648 questions (2,182 MCQ + 1,466 open-ended)
- Annotation: 12 medical expert annotators
- License: CC BY 4.0
- Splits: unknown without full text
- Contamination controls: unknown without full text

## 6. Validity evidence
Expert annotation by 12 medical ethics professionals provides content validity. Grounding in Beauchamp-Childress framework provides construct validity through alignment with the dominant bioethics framework. Differential performance across principles (beneficence hardest) suggests discriminant validity. Specific inter-rater reliability statistics unknown without full text.

## 7. Saturation / discrimination
Performance gaps described as "significant" across models. Beneficence-related reasoning is hardest — suggesting meaningful ceiling variation. Full discrimination statistics unknown without full text.

## 8. Multiturn / agentic aspects
n/a — standard single-turn QA benchmark format based on available metadata.

## 9. Key numbers
- 3,648 total questions
- 2,182 MCQ, 1,466 open-ended
- 350 source documents (textbooks + JAMA Ethics cases)
- 20+ LLMs evaluated
- 12 medical expert annotators
- CC BY 4.0 license

## 10. Pitfalls & limitations
- Beauchamp-Childress framework reflects Western liberal bioethics — may not capture Islamic, Confucian, or other bioethical traditions.
- Sourcing from English-language textbooks and JAMA limits cultural diversity.
- Open-ended scoring methodology (LLM-judge or rubric) introduces reliability concerns.
- Medical ethics edge cases may not generalize to everyday values-alignment evaluation.

## 11. Novel ideas worth stealing
- Organizing a benchmark explicitly around a named normative framework (Beauchamp-Childress) with one section per principle is a reusable template: any well-structured normative framework can scaffold a benchmark with principled coverage.
- Combining MCQ (for reliable scoring) with open-ended questions (for depth) in the same benchmark is a good hybrid design.
- Expert annotation by domain specialists (12 medical ethicists) rather than crowdworkers raises quality — worth the cost for high-stakes ethical domains.
- Using JAMA Ethics cases as a source provides real-world, authoritative material with known provenance.

## 12. Notable quotes
Full text unavailable — no quotes recoverable.

## 13. UNKNOWN / not in extract
- Full text unavailable; detailed methodology, dataset splits, and quantitative results per principle are unknown.
- Exact scoring rubric for open-ended questions.
- Inter-rater reliability statistics among the 12 expert annotators.
- Performance numbers per model and per principle.
- How beneficence was operationalized differently from non-maleficence.
