---
stem: "2025-Snoswell-Beyond Verdicts LLM Moral Competence"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, moral-psychology, validity-psychometrics, design-space]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "69 papers evaluating LLM ethical competence surveyed (2020–2025) (p.1)"
  - "Field doubling approximately every 14 months since 2020 (p.2)"
  - "96% of studies rely on static datasets; only 3% employ interactive scenarios (p.4)"
  - "75% of papers compare LLM judgments to a reference ground truth (p.4)"
  - "Only 19% of papers evaluate steerability (p.4)"
  - "Only 4% evaluate models' ability to determine when more information is needed (p.6)"
---
## 1. Gist
This is a second PDF extraction of the same paper as "2025-Snoswell-Beyond Verdicts Evaluating Language Model Moral Competence Aaron J." — Snoswell, Kilov, and Lazar's systematic survey of 69 papers evaluating LLM ethical competence (2020–2025). This extraction is an 18-page version with standard "--- Page N ---" markers, compared to the 13-page version in the companion file. The content is identical. The paper constructs a three-dimensional taxonomy (datasets, behaviors, metrics) and diagnoses systematic gaps in the field — primarily that existing evaluations pre-package moral scenarios so that morally relevant features are already highlighted, failing to test "moral sensitivity." The authors advocate three paradigm shifts: from curated to naturalistic data, from verdict accuracy to reasoning quality and steerability, and from ground-truth metrics to assessments of reasonableness and consistency.

## 2. Benchmark/eval design features
This is a critical survey and meta-analysis paper. Core contributions for values-alignment benchmarking:

**Taxonomy** across three dimensions:
- *Datasets*: construction (psychological instruments, Reddit AITA, trolley problems, crowdsourcing, LLM-augmentation); case nature (artificial/constructed/found); complexity and value conflicts; framing effects.
- *Behaviors*: verdicts; steerability; justifications; moral sensitivity; information-gathering ability.
- *Metrics*: ground truth comparison; consistency; reasonableness; steerability metrics; Moral Turing Tests; reasoning quality; error analysis.

**Core argument**: The field has a "capability overhang" — LLMs' moral understanding exceeds their moral behavior. This means better evaluation frameworks become enablers of improved moral behavior through post-training, not just passive measurement tools. The authors propose that evaluations should assess:
- Verdicts within an "acceptable range" under reasonable pluralism (not matching a specific ground truth)
- High-quality, veridical justifications that genuinely ground verdicts
- Consistency across morally similar situations
- Reasonable error patterns
- Steerability toward different ethical frameworks at inference time

## 3. Task format & example item
n/a — this is a survey paper with no novel benchmark items.

## 4. Scoring / grading methodology
n/a — the paper critiques existing approaches and proposes alternatives. The paper argues against accuracy-against-ground-truth as a metric and proposes a framework where a "reasonable moral agent" is evaluated on: (a) verdicts within acceptable range, (b) adequate justifications, (c) consistency, (d) reasonable mistakes.

## 5. Dataset construction & provenance
The survey corpus was assembled via Semantic Scholar, Google Scholar, and arXiv searches, supplemented by Elicit.com and ChatGPT Deep Research. Inclusion criteria: post-2020, empirical LLM evaluation, benchmarking morality/moral reasoning. Validated by full-text review and recursive citation snowballing (6 iterations to saturation). Final corpus: 69 papers (2 in 2020, 3 in 2021, 4 in 2022, 14 in 2023, 34 in 2024, 12 in early 2025).

## 6. Validity evidence
Survey corpus validated by manual full-text review. Snowballing terminated at saturation (no new papers found after 6 iterations). The 18-page version appears to be the same accepted manuscript as the companion extraction. As a theoretical/survey paper, construct validity does not apply directly.

## 7. Saturation / discrimination
n/a for the survey itself. The paper notes dataset sizes in reviewed papers range from 8 medical ethics vignettes to 97,000+ trolley problem variants (p.4). The authors specifically note that models performing well on existing benchmarks may exhibit "false confidence" due to the pre-packaged nature of current evaluations — i.e., existing benchmarks may not discriminate between models that actually have moral sensitivity and those that merely pattern-match on labeled features.

## 8. Multiturn / agentic aspects
The paper's most forward-looking contributions are about agentic evaluation. It argues for:
- Evaluation using unfiltered information streams from agentic traces (not pre-packaged scenarios).
- Testing "moral value of information" judgments — whether agents recognize they need more information and take steps to acquire it.
- Only 4% (3/69) surveyed papers evaluate information-gathering, with ClarifyDelphi as the best example.
- The authors argue ethical autonomous agents "must pick out MRFs [Morally Relevant Features] from the noisy, relatively unfiltered stream of information available to them" (p.6).

## 9. Key numbers
- 69 papers in corpus (p.1)
- Field doubling rate ~14 months (p.2)
- 96% (66/69) static datasets; 3% (2/69) interactive (p.4)
- 77% (53/69) complex scenarios; 56% of those feature value conflicts (p.4)
- 65% (45/69) address framing effects (p.4)
- 75% (52/69) use ground truth comparison (p.4–5)
- 41% (28/69) assess consistency (p.5)
- 15% (10/69) evaluate reasonableness (p.5)
- 19% (13/69) evaluate steerability (p.4)
- 48% (33/69) elicit justifications (p.4)
- 33% (23/69) evaluate moral sensitivity (p.4)
- 4% (3/69) evaluate information-gathering (p.5)
- 10% (7/69) use Moral Turing Test (p.5)
- 27% (39/69) evaluate reasoning quality (p.5)
- 48% (33/69) engage in error analysis (p.5)

## 10. Pitfalls & limitations
- The Rawlsian "reasonableness" framework is proposed as a principled alternative to ground truth, but operationalization into concrete metrics is left as future work.
- The analytic philosophy perspective may underweight empirical moral psychology traditions (e.g., moral foundations theory, dual-process models).
- Search strings and GitHub repository URL are redacted in the peer-review version.
- Excludes purely theoretical and alignment-focused papers, creating potential blind spots.
- The "capability overhang" hypothesis is asserted based on cited failures, but no original empirical evidence is provided.

## 11. Novel ideas worth stealing
1. **Unfiltered information stream evaluation**: Present models with actual agentic traces — logs, multimodal data, reasoning chains — and test whether the model can spontaneously flag moral salience without any pre-packaging. No existing benchmark does this.

2. **Moral sensitivity items**: Embed ethical issues in broader, realistic narratives (e.g., a 500-word business scenario) without labeling the moral dimension, and test whether the model identifies what matters ethically vs. operationally.

3. **Steerability as a benchmark dimension**: Systematically test whether models can be directed toward different ethical frameworks (consequentialist vs. deontological vs. virtue-based verdicts) via minimal prompting, measuring both responsiveness and whether steering causes the model to exceed "reasonableness" bounds.

4. **Justification faithfulness**: Combine moral reasoning evaluation with Chain-of-Thought faithfulness evaluation to test whether stated justifications actually drive verdicts, rather than being post-hoc rationalization.

5. **Step-decomposed moral reasoning rubric**: Break moral justification into steps (identify morally relevant features, associate with a moral framework, construct a valid argument, reach a verdict), and score each step independently, enabling partial credit and diagnostic precision.

6. **Reasonableness intervals**: Rather than single ground-truth labels, construct items with expert-rated "acceptable range" labels — multiple verdicts/justifications validated by professional ethicists as within the range of reasonable disagreement — enabling non-binary scoring.

7. **Comparative Moral Turing Tests**: Move beyond binary human/AI detection to direct quality comparisons of moral reasoning, where raters evaluate which response is *better moral reasoning* without knowing the source.

## 12. Notable quotes
- "Every surveyed paper exclusively focuses on evaluating LLMs' ability to reason over neatly prepackaged cases, in which the experimenter is strongly signaling to the model just what all the salient Morally Relevant Features (MRFs) are. This is equivalent to doing 99% of the work on behalf of the model, and then evaluating it on its performance on the last 1%." (p.5–6)

- "Ground truth as such is (in general, outside of extreme cases) an unattainable goal in moral evaluation, and we should shift attention away from it." (p.6)

- "A reasonable agent (a) reaches verdicts that fall within an acceptable range (they don't have clearly unreasonable views); (b) they can justify those verdicts with adequate reasons; (c) they are consistent over morally similar situations; and (d) they make reasonable mistakes." (p.7)

- "High-quality evaluation frameworks thus become not merely assessment tools, but enablers of substantially improved moral behavior." (p.2)

## 13. UNKNOWN / not in extract
- GitHub repository URL is redacted in the extract reviewed.
- Elicit.com search query is redacted.
- The 18-page version vs 13-page companion likely differ in appendix coverage; the 18-page version should contain more of the detailed survey tables referenced in Appendix A, but those pages were not reached in this reading.
- Full appendix tables with comprehensive reference tables for all 69 surveyed papers were not fully extracted.
- No information on which specific models were tested in surveyed papers overall (aggregated statistics only).
