---
stem: "2025-Snoswell-Beyond Verdicts Evaluating Language Model Moral Competence Aaron J."
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
  - "Only 10% employ some form of Moral Turing Test (p.5)"
---
## 1. Gist
Snoswell, Kilov, and Lazar (2025) present a systematic survey of 69 papers that empirically evaluate LLM moral competence published between 2020 and 2025. Authored from a professional analytic-philosophy perspective, the paper constructs a three-dimensional taxonomy (datasets, behaviors, metrics) and uses it to diagnose systematic gaps in the field. The central argument is that existing evaluations create a false confidence: they pre-package moral dilemmas so that all morally relevant features are already highlighted for the model, failing to test "moral sensitivity" (the ability to identify ethical considerations in noisy, unfiltered contexts). The authors argue for three paradigm shifts — from curated to naturalistic data, from verdict accuracy to reasoning quality and steerability, and from ground-truth metrics to assessments of reasonableness and consistency — that are essential for building AI systems capable of real-world moral agency.

## 2. Benchmark/eval design features
This is a critical survey and meta-analysis paper, not a benchmark. Its core theoretical contributions for values-alignment benchmarking are:

**Taxonomy of LLM ethics evaluations** across three dimensions:
- *Datasets*: construction method (psychological instruments, Reddit AITA, trolley problems, crowdsourcing, LLM-augmented); case type (static vs. interactive); nature (artificial/constructed/found); complexity; framing effects.
- *Behaviors*: verdicts (binary, Likert, free-form); steerability (ability to be guided toward different frameworks at inference time); justifications; moral sensitivity; ability to gather more information.
- *Metrics*: ground truth comparison; consistency; reasonableness; steerability metrics; Moral Turing Tests; reasoning quality; error analysis.

**Key critical claims:**
1. 96% of studies use static datasets; dynamic/interactive evaluation is near-absent.
2. Every surveyed paper presents "pre-packaged" scenarios where morally relevant features are already highlighted — nobody tests whether models can spontaneously extract these features from unfiltered information.
3. Ground truth metrics are philosophically problematic: under reasonable pluralism, there is no single correct answer, and population-level aggregation produces intransitive or inconsistent preferences.
4. The field needs to shift toward evaluating "reasonableness" (verdicts within acceptable pluralistic range), consistency, justification quality, and steerability.
5. LLMs exhibit a "capability overhang": moral understanding exceeds moral behavior, meaning better evaluation frameworks could enable substantially better post-training.

## 3. Task format & example item
n/a — this is a survey/critique paper with no novel benchmark items.

## 4. Scoring / grading methodology
n/a — the paper critiques existing scoring approaches. It argues that accuracy-against-ground-truth is philosophically inadequate and proposes alternatives: (a) verdicts within acceptable range, (b) high-quality justifications, (c) consistency across morally similar situations, (d) reasonable error patterns.

## 5. Dataset construction & provenance
The survey corpus of 69 papers was assembled via searches of Semantic Scholar, Google Scholar, and arXiv using keywords including "Moral Competence," "Moral Reasoning," "Large Language Model." Additional papers found via Elicit.com and ChatGPT Deep Research. Selection criteria required: post-2020 publication, empirical evaluation of LLMs, and application of a benchmark or method to evaluate morality/moral reasoning. Validated by full-text review and recursive forward/backward citation snowballing (6 iterations) until saturation. Distribution: 2 (2020), 3 (2021), 4 (2022), 14 (2023), 34 (2024), 12 (2025 at time of writing).

## 6. Validity evidence
As a survey paper, validity evidence is not directly applicable. The authors validate their corpus through manual full-text review, rejecting papers that focused on alignment or moral/cultural identity rather than moral competence evaluation. The recursive snowballing procedure ran until saturation (no new papers after 6 iterations), providing a plausibility check on corpus completeness.

## 7. Saturation / discrimination
n/a — not a benchmark. However, the paper notes that dataset sizes in the surveyed papers range from 8 vignettes to over 97,000 trolley problem variants (p.4), and most models appear to perform well on existing benchmarks, suggesting possible ceiling effects — a concern the authors directly address in their critique of "false confidence."

## 8. Multiturn / agentic aspects
The paper explicitly advocates for evaluations that test agentic moral competence: models acting "in place of a human user" must pick out morally relevant features from "noisy, relatively unfiltered streams of information" (p.6). Only 3% of surveyed papers use interactive scenarios (Hendrycks et al. 2021; Pan et al. 2023). Only 3 papers (4%) evaluate the ability to recognize when more information is needed — identified as ClarifyDelphi as the closest to correct direction. The authors call for testing "moral value of information" judgments in agentic settings.

## 9. Key numbers
- 69 papers surveyed, 2020–2025 (p.1)
- Field doubling rate: ~14 months (p.2)
- 96% (66/69) use static datasets; 3% (2/69) use interactive scenarios (p.4)
- Dataset sizes: 8 vignettes to 97,000+ trolley variants (p.4)
- 54% (37/69) rely on artificial philosophical scenarios; 35% (24) use constructed everyday scenarios; 20% (14) use found cases (p.4)
- 77% (53/69) employ complex scenarios; 56% of those (30) feature conflicting values (p.4)
- 65% (45/69) address framing effects (p.4)
- 19% (13/69) evaluate steerability (p.4)
- 48% (33/69) elicit justifications for verdicts (p.4)
- 33% (23/69) evaluate moral sensitivity (p.4)
- 4% (3/69) evaluate ability to request more information (p.5)
- 75% (52/69) use ground truth comparison (p.4)
- 41% (28/69) assess consistency of moral judgments (p.5)
- 15% (10/69) evaluate reasonableness rather than ground-truth match (p.5)
- 39% (27/69) evaluate quality of moral reasoning/justifications (p.5)
- 48% (33/69) engage in error analysis (p.5)
- 10% (7/69) employ some form of Moral Turing Test (p.5)

## 10. Pitfalls & limitations
- **Survey scope**: Authors excluded papers focusing on alignment or moral/cultural identity; this boundary is contested and may exclude relevant work.
- **Author perspective**: Explicitly written from analytic philosophy — the authors acknowledge this viewpoint and note it shapes their critique.
- **Redacted details**: The Elicit.com search query and GitHub repository URL are redacted in the reviewed version (peer review anonymization), limiting replication.
- **Normative framing**: The Rawlsian "reasonableness" standard proposed as a replacement for ground truth is itself contested and not operationalized in concrete metrics.
- **Coverage gap**: The survey covers empirical evaluation papers; purely theoretical work and non-benchmark alignment papers are out of scope, creating blind spots in the critique.
- **Positive findings understated**: While the paper focuses on gaps, the finding that "LLMs are on the whole impressively capable moral reasoners" (p.5) deserves more attention.

## 11. Novel ideas worth stealing
1. **Moral sensitivity as a first-class construct**: Designing items that present unfiltered, noisy descriptions of situations (e.g., transcripts, multimodal streams) and ask models to *first identify whether there is a moral issue at all* — without pre-packaging the ethical framing. This is absent from virtually all existing benchmarks.

2. **"Moral value of information" tasks**: Benchmark items where the model must recognize it lacks sufficient information to make a sound ethical judgment and must ask clarifying questions or take information-gathering actions before rendering a verdict.

3. **Steerability evaluation**: Testing whether models can be appropriately guided toward different ethical frameworks (utilitarian, deontological, virtue ethics) at inference time through prompting — not merely checking if the model applies a framework, but if it can be *steered* pluralistically.

4. **Reasonableness metrics over accuracy**: Rather than matching a ground truth, evaluate whether model verdicts fall within the "acceptable range" of verdicts a reasonable person could reach under moral pluralism.

5. **Step-decomposed justification evaluation**: Breaking moral justification into a series of tractable steps (identify MRFs, associate with moral reasons, construct valid argument) and evaluating performance at each step against expert humans — enabling graded partial credit rather than binary correctness.

6. **Generative verifier training loop**: The insight that good-quality moral reasoning examples could train verifiers, which in turn enable reinforcement learning toward better moral generators — pointing to a specific design for synthetic data pipelines.

7. **Capability overhang framing**: The observation that LLM moral understanding exceeds moral behavior suggests benchmarks should separately evaluate (a) understanding/recognition and (b) behavioral conformance, as these can diverge substantially.

## 12. Notable quotes
- "Every surveyed paper exclusively focuses on evaluating LLMs' ability to reason over neatly prepackaged cases, in which the experimenter is strongly signaling to the model just what all the salient Morally Relevant Features (MRFs) are. This is equivalent to doing 99% of the work on behalf of the model, and then evaluating it on its performance on the last 1%." (p.5–6)

- "Ground truth as such is (in general, outside of extreme cases) an unattainable goal in moral evaluation, and we should shift attention away from it." (p.6)

- "In general, in pluralistic societies we expect of other agents not that they hold some particular set of views, but that they are reasonable." (p.7)

- "A language model's ability to understand moral concepts does not predict its ability to conform its behavior to that moral understanding." (p.2)

## 13. UNKNOWN / not in extract
- The GitHub repository URL for the coded dataset is redacted (peer review anonymization) — cannot confirm public availability.
- The Elicit.com search query is also redacted.
- Specific model names evaluated across surveyed papers are not systematically reported in the extract.
- Full appendix tables (Appendix A) listing all 69 papers' detailed coding are referenced but not fully reproduced in the extract.
- No information on whether a preprint or published version exists beyond the AAAI 2026 conference paper indication.
