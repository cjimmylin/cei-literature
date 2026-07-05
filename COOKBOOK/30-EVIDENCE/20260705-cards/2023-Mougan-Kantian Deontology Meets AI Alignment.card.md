---
stem: "2023-Mougan-Kantian Deontology Meets AI Alignment"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, design-space, pluralism-aggregation]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "12 out of 14 group fairness metrics in Wachter et al. survey rely on model errors (utilitarian/disparate impact); only 2 rely on model behavior (deontological/disparate treatment) (p.8)"
  - "Racial minorities 40-80% more likely to have mortgage applications denied in The Markup investigation (p.10)"
---
## 1. Gist
This preprint by Mougan and Brand (University of Southampton / Télécom Paris) argues that the dominant paradigm in AI fairness metrics is implicitly utilitarian—focused on outcome disparities across groups—while Kantian deontological ethics, with its emphasis on duties and treating individuals as ends-in-themselves, has been largely neglected. The paper maps standard fairness metrics onto the deontology/utilitarianism divide: disparate impact metrics (equal opportunity, accuracy equality) are utilitarian; disparate treatment metrics (demographic parity, counterfactual fairness, individual fairness) are deontological. Two case studies—mortgage loan approval and the 2020 Ofqual student grading scandal—illustrate the argument. For values-alignment benchmarking, this paper provides a philosophical grounding for why procedural fairness (how AI makes decisions) matters as much as distributive fairness (what outcomes result), and why evaluating AI purely on outcome metrics may be morally inadequate.

## 2. Benchmark/eval design features
Not a benchmark paper. Core theoretical contributions:

1. **Mapping fairness metrics to ethical frameworks**: Disparate impact = utilitarian (focuses on error rates across groups; requires post-deployment labeled data). Disparate treatment = deontological (focuses on model behavior; does not require post-deployment data).

2. **Categorical Imperative as procedural fairness**: The Kantian idea that ethics is procedural (not just consequential) maps onto the concept of procedural fairness in ML—evaluating the data collection, training, and decision pipeline, not just the output.

3. **Three Kantian critiques of utilitarian AI fairness**: (a) Critique of the Impersonal Good—utilitarianism treats individuals as mere vessels for utility; (b) Critique of Aggregation—individuals cannot be harmed for the benefit of the aggregate; (c) Critique of Lack of Robustness—outcome-based standards are unstable because circumstances change consequences.

4. **Empirical observation**: In Wachter et al.'s comprehensive survey, 12 of 14 formalized group fairness metrics rely on model errors (utilitarian), and only 2 rely on model behavior (deontological). (p.8)

## 3. Task format & example item
n/a. Two illustrative case studies are presented:

- **Loan approval** (p.10–11): A Black couple in North Carolina with high credit scores was denied a mortgage because one partner was a contract worker. The Markup's analysis found racial minorities 40–80% more likely to be denied. Kantian analysis: reducing individuals to gig-worker status violates the Formula of Humanity by treating them as mere representatives of group characteristics rather than as ends-in-themselves.

- **Ofqual 2020** (p.12–13): An algorithm assigned UK A-level grades during COVID-19 based on historical school performance, systematically disadvantaging students from low-performing schools. Kantian critique: judging individual students by their school's historical performance treats them as mere means to statistical efficiency.

## 4. Scoring / grading methodology
n/a. Theoretical paper; no empirical scoring.

## 5. Dataset construction & provenance
n/a. The paper cites The Markup's investigative journalism and secondary sources for the two case studies. No original dataset is used.

## 6. Validity evidence
The theoretical argument draws on primary sources (Kant's Groundwork, Metaphysics of Morals), contemporary Kantians (O'Neill, Korsgaard), and established ML fairness literature (Barocas et al., Hardt et al., Wachter et al.). The mapping of fairness metrics to ethical frameworks is a conceptual argument, not empirically tested. The claim that 12/14 group fairness metrics are utilitarian is based on Wachter et al.'s survey of formalized metrics.

## 7. Saturation / discrimination
n/a.

## 8. Multiturn / agentic aspects
n/a.

## 9. Key numbers
- 12 of 14 group fairness metrics in Wachter et al.'s comprehensive survey rely on model errors (utilitarian); only 2 rely on model behavior (deontological) (p.8)
- Racial minorities 40–80% more likely to be denied mortgages in The Markup investigation (p.10)
- Ofqual case: "proportion of girls in England awarded A or above rose from 25% to 28%, overtaking that of boys, who received A or above for 27% of their entries" (p.12, quoting The Guardian)

## 10. Pitfalls & limitations
- The deontology/utilitarianism mapping onto disparate treatment/impact is a simplification; the authors acknowledge deontological principles are not exclusive to disparate treatment
- The paper offers a programmatic argument without a concrete alternative metric or framework with formal properties
- Kantian ethics itself has well-known limitations (inflexibility, empty formalism objection, difficulty handling exceptions) that the paper does not fully address
- The paper focuses on supervised learning classification; applicability to generative AI or LLMs is not discussed
- The authors acknowledge their Western educational background as a potential limitation on universality of Kantian framework
- The paper cautions against uncritical adoption of their framework, acknowledging potential for oversimplification

## 11. Novel ideas worth stealing
1. **Disparate treatment = deontological evaluation**: Designing benchmarks that measure model behavior (what decisions the model makes based on protected attributes) rather than only outcome disparities shifts evaluation toward deontological standards—appropriate when post-deployment data is unavailable.
2. **Procedural fairness as a first-class benchmark dimension**: Evaluating the full pipeline (data collection, training assumptions, algorithmic transparency) as part of fairness assessment, not just final outputs. Could inspire benchmark items that probe whether AI systems can reason about the fairness of their own training process.
3. **The aggregation problem as a benchmark design principle**: Items where utilitarian optimization conflicts with individual rights can stress-test whether AI systems prioritize aggregate welfare over individual dignity—a key distinction in values-alignment work.
4. **Tethered good concept** (Korsgaard): "What is good-for me plus what is good-for you is not necessarily good-for anyone." This relational conception of value challenges aggregate scoring in benchmarks—summing individual judgments may not produce a coherent group value.
5. **Post-deployment data unavailability as a practical argument for deontological metrics**: In many real deployment contexts, gathering labeled outcome data is impractical or illegal. Deontological metrics (measuring model decisions) are computationally tractable without post-deployment observation—a pragmatic argument for their adoption.

## 12. Notable quotes
- "It should be axiomatic that producing some sort of benefit is a necessary condition for the ethical and responsible use of AI." (p.2, quoting London and Heidari)
- "Treating others as ends-in-themselves grants intrinsic worth to each individual. This approach means looking beyond group affiliations or categories to which an individual may belong." (p.10)
- "Kant's categorical imperative thus provides a philosophical foundation for procedural fairness in AI ethics, guiding the development of AI systems that operate within a universal framework of equitable and just procedures." (p.9–10)
- "The Ofqual experience serves as a cautionary tale, highlighting the need for a reflection on whether the usage of AI systems for automation actually improves societal aspects, even when considering 'fairness metrics'." (p.13)

## 13. UNKNOWN / not in extract
- Whether the paper has been formally published (marked "Preprint. Under review." on p.1)
- Empirical validation of the claim that deontological metrics avoid fairness-accuracy trade-offs in practice (beyond the Rodolfa et al. citation)
- How to formally operationalize the Formula of Humanity as a fairness metric
- Application to generative AI systems and LLMs
- Whether the Kantian framework can account for affirmative action or differential treatment of historically disadvantaged groups (the paper briefly mentions this as permissible under the humanity formula but does not develop it fully)
