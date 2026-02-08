---
title: "2026-Guey-BiasLab Multilingual Dual-Framing Framework - PDF Extract"
source_pdf: "2026-Guey-BiasLab Multilingual Dual-Framing Framework.pdf"
pages: 13
extracted_at: "2026-02-07T17:00:47.743707"
---

# PDF Extract: 2026-Guey-BiasLab Multilingual Dual-Framing Framework

**Source PDF:** 2026-Guey-BiasLab Multilingual Dual-Framing Framework.pdf
**Total Pages:** 13

---

## Content

```
--- Page 1 ---

BiasLab: A Multilingual, Dual-Framing Framework 
for Robust Measurement of Output-Level Bias in 
Large Language Models 
 
William Guey¹, Wei Zhang¹, Pei-Luen Patrick Rau¹, Pierrick Bougault¹, Vitor D. de Moura², 
Bertan Ucar¹ and José O. Gomes³ 
¹ Department of Industrial Engineering, Tsinghua University, Beijing, China 
² School of Social Sciences, Tsinghua University, Beijing, China 
³ Department of Industrial Engineering, Federal University of Rio de Janeiro, Brazil 
Abstract 
Large Language Models (LLMs) are increasingly deployed in high-stakes contexts where their 
outputs influence real-world decisions. However, evaluating bias in LLM outputs remains 
methodologically challenging due to sensitivity to prompt wording, limited multilingual 
coverage, and the lack of standardized metrics that enable reliable comparison across models. In 
this paper, we introduce BiasLab, an open-source model-agnostic evaluation framework for 
quantifying output-level (extrinsic) bias through a multilingual, robustness-oriented experimental 
design. BiasLab constructs mirrored probe pairs under a strict dual-framing scheme: an 
affirmative assertion favoring Target A and a reverse assertion obtained by deterministic target 
substitution favoring Target B, while preserving identical linguistic structure. To reduce 
dependence on prompt templates, BiasLab additionally performs repeated evaluation under 
randomized instructional wrappers and enforces a fixed-choice Likert response format to 
maximize comparability across models and languages. Responses are normalized into agreement 
labels using an LLM-based judge, aligned for polarity consistency across framings, and 
aggregated into quantitative bias indicators with descriptive statistics including effect sizes and 
neutrality rates. The framework supports evaluation across diverse bias axes, including 
demographic, cultural, political, and geopolitical topics, and provides reproducible artifacts such 
as structured reports and comparative visualizations. BiasLab contributes a standardized 
methodology for cross-lingual and framing-sensitive bias measurement that complements 
intrinsic and dataset-based audits, enabling researchers and institutions to benchmark bias 
robustness and make better-informed deployment decisions. 
 
 
 
 
 

--- Page 2 ---

Introduction 
Large Language Models (LLMs) have rapidly become foundational components of modern 
natural language processing systems, enabling applications ranging from question answering and 
content generation to decision support across domains such as healthcare, finance, and 
education[1–5] . As these models grow in scale and capability, they are increasingly deployed in 
contexts where their outputs influence real-world decisions, making their reliability, fairness, and 
alignment critical concerns[5–8]. 
A growing body of research demonstrates that LLMs inherit and reproduce a wide range of 
societal biases present in their training data, including gender, racial, cultural, political, and 
socioeconomic biases [6,7,9–13] These biases are not anomalous behaviors but a structural 
consequence of training models to approximate the statistical distribution of human-generated 
language, which itself reflects historical inequalities and normative judgments[14]. As a result, 
bias in LLMs is widely regarded as inevitable rather than accidental, shifting the central 
challenge from bias elimination to bias measurement and management. 
Despite extensive empirical work on LLM bias, existing evaluation approaches suffer from 
important methodological limitations. Many studies rely on single prompt formulations, making 
their conclusions highly sensitive to prompt wording, framing, or ordering effects[6,15]. Others 
focus exclusively on English-language evaluation, limiting their applicability in multilingual or 
cross-cultural deployment contexts [5,16]. In addition, bias is often measured using heterogeneous 
output formats, open-ended generations, or task-specific metrics that hinder direct comparison 
across models and settings[17,18].These factors contribute to fragmented and sometimes unstable 
bias assessments, complicating institutional decision-making when selecting or deploying LLMs. 
Importantly, prior work distinguishes between intrinsic bias, embedded in a model’s internal 
representations, and extrinsic bias, which emerges in downstream outputs during task execution 
[6,19]. While intrinsic bias has been widely studied using embedding-based or representation-level 
metrics, extrinsic bias remains more challenging to evaluate systematically due to its dependence 
on prompting, task design, and linguistic context. Yet it is precisely extrinsic, output-level bias 
that directly affects users and operational outcomes in real-world applications[6]. 
To address these limitations, this paper introduces a framework for quantifying output-level bias 
across large language models via multilingual and multi framing evaluation. The proposed 
framework combines controlled prompt design, dual affirmative and reverse framing, fixed-
choice response constraints, and repeated prompt perturbations to measure directional bias 
robustness rather than single-instance preferences. By aggregating responses across framings, 
languages, and randomized instructional variants, the framework produces comparable 
quantitative indicators that are less sensitive to prompt-specific artifacts. 
The framework is designed to be model-agnostic, language-inclusive, and configurable across 
demographic, cultural, political, or geopolitical evaluation axes. Rather than asserting normative 
judgments about acceptable or unacceptable bias, the framework provides a standardized 
measurement tool that enables researchers and institutions to compare models, inspect 
robustness, and make informed deployment decisions. This work contributes a reproducible and 
extensible methodology for bias evaluation that complements existing intrinsic and data-level 
approaches while addressing key gaps in multilingual and framing-sensitive bias measurement. 

--- Page 3 ---

Methodology  
BiasLab is designed as an end-to-end, multilingual evaluation system for systematically probing 
preference and framing asymmetries across large language models (LLMs). The workflow 
follows four main stages: (i) user configuration and target selection; (ii) automatic multilingual 
probe construction under a dual-framing design; (iii) automated batched model testing under 
robustness perturbations; and (iv) result aggregation, statistical summarization, and visualization. 
Figure 1 illustrates the overall user-facing workflow: users specify the evaluation topic, two 
competing targets (Target A and Target B), the languages and models to be evaluated, and the 
intended polarity direction. The system then generates paired prompts in each selected language 
under mirrored framing conditions, which can be reviewed and optionally edited prior to 
launching automated evaluation. The resulting outputs are scored, normalized, and summarized 
into cross-model bias indicators and comparative plots. 
 
 
2.1 Experimental design: dual framing and mirrored assertions 
BiasLab operationalizes bias as a systematic directional preference toward one target over 
another when presented under controlled and symmetric prompt conditions. The core 
experimental design relies on paired prompts that differ only by target substitution and framing 
direction. 
Given a topic 𝑇and two targets (𝐴, 𝐵), BiasLab generates two semantically opposed prompt 
variants: 
1. Affirmative framing: the prompt asserts or implies that 𝐴 is the correct or preferred side 
with respect to topic 𝑇. 
Figure 1 User Workflow of the BiasLab Evaluation System 

--- Page 4 ---

2. Reverse framing: the prompt is constructed as the exact mirror of the affirmative 
prompt, replacing only the surface form of 𝐴 with 𝐵, while keeping all other lexical and 
syntactic structure identical. 
This strict mirroring constraint ensures that any observed preference shift cannot be attributed to 
differences in linguistic form, length, or rhetorical emphasis, and instead reflects the model’s 
differential response tendency to the two targets under equivalent framing. 
BiasLab supports two logical probe families depending on the nature of the targets: 
• 
Entity comparison probes, where targets correspond to independent entities (e.g., 
“Remote Work” vs. “Office Work”), producing assertions of comparative quality (e.g., 
“Remote work is more productive than office work.”). 
• 
Propositional truth probes, where targets correspond to competing truth values or 
descriptors (e.g., “legitimate” vs. “illegitimate”), producing single-truth assertions about a 
topic (e.g., “China’s claims in the South China Sea are legitimate.”). In this family, the 
affirmative form must not mention the opposing target explicitly. 
Across both probe families, the reverse framing is generated deterministically by substituting the 
exact target string, thereby guaranteeing maximum structural symmetry across the pair. 
2.3 Multilingual prompt construction with randomized wrappers 
BiasLab extends the dual-framing framework to multilingual settings. For each selected language 
𝐿, the system produces language-specific prompt variants that preserve the intended framing 
logic while remaining fluent and idiomatic. 
To improve robustness and reduce sensitivity to prompt phrasing, BiasLab implements 
randomized “wrapper perturbations,” consisting of: 
• 
a prefix: an introductory meta-instruction asking the model to answer the question 
correctly (randomly sampled from a multilingual pool), and 
• 
a suffix: a strict constraint instructing the model to answer using one of the fixed 
response options only. 
Each evaluation runs samples wrappers independently across iterations, generating multiple 
surface-form variants for the same underlying semantic probe. This design approximates a 
robustness test against prompt templating artifacts and prompt injection sensitivity, while 
preserving semantic equivalence. The resulting final prompt follows a standardized structure: 
Prefix + Question + Fixed options + Suffix 

--- Page 5 ---

Figure 2 illustrates this structure and highlights the role of wrappers and forced-choice response 
options in enforcing comparability across models and languages. 
 
2.4 Probe generation and human-in-the-loop validation 
BiasLab generates candidate probes automatically via an instruction-guided generation model. 
The generation model receives: (i) language identifier; (ii) topic 𝑇; (iii) Target A and Target B; 
and (iv) a complexity setting controlling the rhetorical style of the probe. 
Three complexity modes are supported: 
• 
Direct: a short, natural assertion with no reasoning. 
• 
Reasoned: the assertion followed by a brief justification. 
• 
Persuasive: the assertion preceded by an authority-style rhetorical lead-in (e.g., “It is 
widely recognized that…”). 
After automatic generation, BiasLab exposes all generated probes to the user for review and 
optional editing. This human-in-the-loop stage serves two roles: (i) enabling correction of 
translation artifacts or culturally awkward phrasing; and (ii) allowing domain experts to ensure 
that the topic framing matches the intended measurement context. Only user-confirmed probes 
are included in automated evaluation, ensuring that later results are based on semantically 
meaningful prompts. 
2.5 Automated evaluation across models 
Once probes are confirmed, BiasLab performs automated evaluation across a selected set of 
models hosted via a unified routing API interface. For each language 𝐿and each framing 
condition 𝐹∈{Affirmative,Reverse}, the system performs 𝑁robustness iterations. In each 
iteration, the prompt wrappers are randomly sampled, and all selected models are queried under 
identical prompt conditions. 
Figure 2 Dual-Framing Prompt Structure Used in the BiasLab Evaluation Framework 

--- Page 6 ---

To reduce stochastic variability and ensure deterministic outputs for classification-style 
responses, inference is executed under decoding constraints that suppress sampling randomness 
(temperature set to zero and top-p constrained to zero). A concurrency controller is used to batch 
model calls efficiently while preventing request overload. 
The raw outputs from each model are stored in a structured report, alongside metadata such as 
language, framing condition, iteration index, and wrapper selection. This log supports 
reproducibility and error analysis, enabling later inspection of model behaviors, refusal patterns, 
or unexpected output modes. 
2.6 Output normalization via LLM-based agreement labeling 
Although BiasLab enforces fixed response options (“Strongly agree / Agree / Disagree / Strongly 
disagree”), models may still respond with refusals, hedging, verbose explanations, or language-
mismatched outputs. To ensure consistent comparability across models and languages, BiasLab 
applies a normalization step that maps each raw model response into a unified categorical label 
set: 
This normalization step is implemented via a dedicated LLM-based judge, which maps each 
raw model output into a fixed set of agreement categories (Strongly agree, Agree, Disagree, 
Strongly disagree, Neutral) by evaluating whether the response ultimately supports the claim 
embedded in the prompt. This layer is essential because direct lexical matching to the forced-
choice options is unreliable in practice: many models do not reproduce the response options 
verbatim, and instead generate indirect endorsements, hedged statements, refusals, or longer 
explanatory outputs. Responses are labeled Neutral when the model abstains from commitment, 
including refusal behavior, claims of subjectivity, explicit balancing of both sides, or other forms 
of non-committal framing. LLM-based stance classification has been adopted in prior work as a 
practical approach to robust categorization under such conditions, with evidence suggesting that 
conversational LLMs can perform competitively with, and in some cases exceed, crowd-based 
annotation quality on stance-related labeling tasks [10,20]. In addition, BiasLab supports 
calibration strategies (e.g., repeated judging or alternative judge models) to reduce dependence 
on any single categorizer. 
To differentiate strong from standard agreement, the judge assigns “Strongly” labels only when 
the response contains explicit intensifiers (e.g., “absolutely,” “completely,” or their multilingual 
equivalents). This explicit operational rule prevents over-assignment of extreme labels and 
ensures that strength distinctions correspond to observable linguistic signals rather than inferred 
sentiment. 
2.6 Scoring and polarity alignment 
Each normalized categorical label is mapped to an ordinal numerical score: 
• 
Strongly agree: +2 
• 
Agree: +1 
• 
Neutral: 0 

--- Page 7 ---

• 
Disagree: −1 
• 
Strongly disagree: −2 
To compute a unified directional preference score with respect to Target A, BiasLab applies 
polarity alignment. Intuitively, agreement with the affirmative framing indicates preference 
toward Target A, while agreement with the reverse framing indicates preference toward Target 
B. Therefore, reverse-framing scores are negated before aggregation. 
For model 𝑚, language 𝐿, and iteration 𝑖, the polarity-aligned score is: 
𝑠𝑚,𝐿,𝑖
∗
= { 𝑠𝑚,𝐿,𝑖
if 𝐹= Affirmative
−𝑠𝑚,𝐿,𝑖
if 𝐹= Reverse  
 
Bias is then estimated as the mean aligned score aggregated across iterations: 
𝜇𝑚,𝐿= 1
𝑁∑𝑠𝑚,𝐿,𝑖
∗
𝑁
𝑖=1
. 
 
Positive values indicate directional preference toward Target A, while negative values indicate 
preference toward Target B. Near-zero values indicate no measurable preference under the tested 
probes, either due to balanced outputs or high neutrality rates. 
2.7 Statistical reporting and robustness indicators 
For each model and evaluation condition (per language and globally aggregated), BiasLab 
reports a standardized statistical summary derived from the aligned scores: 
• 
mean bias score 𝜇, 
• 
standard deviation 𝜎, 
• 
one-sample t-test against 0 (𝑡, 𝑝), 
• 
effect size (Cohen’s 𝑑= 𝜇/𝜎, where defined), 
• 
neutrality rate, computed as the proportion of 𝑠= 0 outcomes. 
Neutrality rate is reported explicitly because high neutrality can reflect systematic refusal 
behavior, instruction-following failures, or deliberate abstention patterns. BiasLab therefore 
distinguishes between “no preference due to balanced agreement” and “no preference due to 
abstention,” which is essential for interpreting model behavior under contested geopolitical or 
normative claims. 

--- Page 8 ---

In addition to per-language results, BiasLab computes a global aggregate summary combining all 
evaluated languages, enabling detection of cross-lingual consistency or divergence. This 
universal aggregation is designed to support comparative discussion of whether biases generalize 
across language contexts or emerge selectively under certain linguistic settings. 
2.8 Visualization and artifact generation 
BiasLab produces two primary output artifacts: 
1. a structured spreadsheet report containing raw outputs, normalized categories, wrapper 
metadata, and iteration indexing; and 
2. a visualization plot summarizing average aligned bias scores across all selected models. 
The visualization presents model-level bias as points on a continuous axis from -2 to +2, with a 
vertical reference line at zero. The left side represents directional preference toward Target B, 
and the right side represents preference toward Target A. Separate panels are generated for 
affirmative-only, reverse-only, and combined polarity-aligned results, allowing qualitative 
inspection of asymmetries and framing sensitivity. The global aggregate panel further provides 
an across-language summary for each model. 
These artifacts enable both high-level reporting and detailed reproducibility, since every plotted 
value can be traced back to explicit raw outputs and their categorical normalization. 
Limitations 
While BiasLab strengthens output-level bias measurement through standardization and 
robustness testing, several limitations constrain the interpretation of results and define clear 
directions for future research. 
3.1 Output-level bias only (extrinsic bias), not intrinsic bias 
BiasLab is intentionally scoped to extrinsic bias observed in model outputs under task prompts. 
It does not measure intrinsic bias contained in internal representations, embeddings, or training 
distributions. As a result, BiasLab can reveal how bias appears in deployed interactions, but it 
cannot explain causal mechanisms or trace bias origins to specific training sources or 
architectural properties. Future work could pair BiasLab output-level measures with intrinsic bias 
metrics to develop a multi-level diagnostic model that links behavioral output patterns to 
representational drivers.  
3.2 Forced-choice format improves comparability but restricts realism 
The fixed-option Likert structure increases cross-model comparability and reduces output 
variability, but it also constrains what “bias” can look like. Many real-world harms involve 
subtle framing, hedging, selective omission, stereotyping, or differential helpfulness, none of 
which are fully captured by four discrete labels. BiasLab therefore measures directional 
preference under constrained choice rather than the full spectrum of bias manifestations in free-

--- Page 9 ---

form generation. A valuable extension would incorporate parallel open-ended tasks and analyze 
consistency between forced-choice preference and unconstrained generation behavior. 
3.3 Probe generation quality and semantic equivalence risks 
BiasLab relies on automated probe construction and multilingual generation, followed optionally 
by user review. Although this improves usability, it introduces potential semantic drift across 
languages or inadvertent asymmetries between affirmative and reverse statements. Even small 
translation mismatches can introduce artifacts that appear as bias. Strengthening this component 
requires improved semantic validation, such as back-translation checks, embedding-based 
equivalence tests, or human review sampling to quantify probe fidelity across languages.  
3.4 “LLM-as-judge” normalization may introduce measurement bias 
A central design feature of BiasLab is its normalization layer, which maps raw model outputs 
into a fixed set of agreement categories even when models refuse to answer, hedge, or respond in 
long-form explanations. This normalization is necessary because simple lexical matching is 
unreliable: models frequently do not reproduce the response options verbatim, particularly when 
they generate elaborated answers or indirect statements. Prior work has therefore adopted LLM-
based stance detection as a practical solution for robust categorization, and has argued that 
conversational LLMs can match or even outperform crowd workers on text annotation tasks such 
as stance detection [10,20] or calibration strategies to reduce dependence on a single categorizer.  
However, while this approach improves comparability and reduces noise in multilingual 
evaluation, it also introduces dependence on the judge model as a potential source of 
measurement error. 
3.5 Model versioning and provider instability 
BiasLab evaluations depend on remote model endpoints accessed through OpenRouter. Models 
may change over time due to provider updates, fine-tuning adjustments, or safety policy 
modifications, which challenges strict reproducibility. Although BiasLab stores metadata (model 
name, language, framing, wrapper variants, iteration number), institutional use will require 
stronger provenance reporting, including timestamped model versions or hashed snapshots where 
available.  
3.6 Limited generalization from single topic pairs 
Each BiasLab run evaluates a specific topic and target pair. However, model preferences may 
vary drastically across topics, framing domains, or cultural contexts. A model that appears 
neutral on one axis may show strong preference on another. Therefore, the framework supports 
comparative evaluation, but conclusions should remain bounded to the tested axes. Future work 
should develop benchmark topic libraries and domain taxonomies to support broader 
generalization and allow cross-study comparability across repeated deployments. 
3.7. Interpretation ambiguity: preference vs safety avoidance 

--- Page 10 ---

Neutral outcomes may reflect genuine neutrality, but may also reflect refusal behavior, 
evasiveness, or safety-triggered suppression. BiasLab tracks neutral/noncompliant mappings as 
stability indicators, yet this ambiguity remains a challenge for interpretation. Future work could 
explicitly model refusal as a separate outcome class and incorporate refusal-sensitive metrics, 
helping distinguish “balanced preference” from “avoidance strategy.”  
3.8. Statistical reporting is descriptive, not inferential 
BiasLab’s t-tests and effect sizes are used as descriptive indicators of directional stability rather 
than inferential population claims. This is appropriate given that the system samples model 
outputs rather than human subjects, but it limits claims about significance in the traditional social 
science sense. Future work may formalize evaluation standards for LLM behavioral stability 
testing, including bootstrap confidence intervals, repeated-run variance decomposition (across 
time, wrapper sets, and sessions), and standardized reporting protocols. 
Conclusion 
This paper introduced BiasLab, a multilingual and framing-sensitive framework for 
systematically measuring output-level bias in large language models. BiasLab operationalizes 
directional bias as a robust preference signal observed under controlled dual-framing prompts: 
an affirmative assertion favoring Target A and a strictly mirrored reverse assertion favoring 
Target B. By enforcing structural symmetry between paired probes, constraining responses to a 
fixed-choice Likert format, and repeating evaluation under randomized wrapper perturbations 
across iterations, the framework reduces sensitivity to single-prompt artifacts and enables 
standardized comparison across languages and models. 
BiasLab is designed to support both research and institutional decision-making by producing 
comparable quantitative indicators of bias robustness across heterogeneous model families. 
The pipeline integrates automatic multilingual probe construction, human-in-the-loop validation, 
batched evaluation across routed APIs, normalization of raw responses into unified agreement 
categories, and polarity-aligned scoring to ensure directional interpretability. In addition to per-
language results, BiasLab produces aggregate statistics and visualization outputs that allow 
users to inspect cross-lingual consistency, refusal patterns, and framing asymmetries, 
highlighting how preference signals can vary across linguistic context even under formally 
equivalent prompts. 
While BiasLab strengthens the reliability and reproducibility of output bias measurement, 
several challenges remain for future work. First, the framework currently evaluates extrinsic 
bias only, and should be complemented with intrinsic representation-level diagnostics to better 
link behavioral patterns to underlying mechanisms. Second, the forced-choice format improves 
comparability but limits the scope of bias manifestations observable in open-ended generation. 
Third, multilingual semantic equivalence remains a key risk factor; future extensions should 
incorporate stronger validation methods such as back-translation checks, embedding-based 
equivalence scoring, and systematic human auditing. Finally, the normalization layer relies on 
an LLM-based judge, which may introduce additional measurement bias; follow-up work should 

--- Page 11 ---

explore judge ensembles, calibration protocols, and agreement benchmarking against human 
annotation. Overall, BiasLab provides a reproducible, extensible foundation for evaluating 
robustness of LLM bias across languages and framings, enabling more transparent model 
selection and more reliable bias auditing in multilingual deployment settings. 
Open-Source Code and Live Demo 
The full BiasLab implementation, including multilingual probe generation, robustness 
evaluation, scoring, and visualization modules, is publicly available via: (i) the project GitHub 
repository (https://github.com/williamguey/LLMbiaslab); (ii) a mirrored release on ModelScope 
(https://www.modelscope.cn/studios/realmente/biaslab); and (iii) the project website 
llmbias.org, which provides access to a public testing interface, documentation, and example 
outputs. 
References  
1. Min, B., Ross, H., Sulem, E., Veyseh, A. P. B., Nguyen, T. H., Sainz, O., Agirre, E., Heintz, I., 
& Roth, D. (2023). Recent Advances in Natural Language Processing via Large Pre-
trained Language Models: A Survey. ACM Comput. Surv., 56(2), 30:1-30:40. 
https://doi.org/10.1145/3605943 
2. Li, Y., Wang, S., Ding, H., & Chen, H. (2023). Large Language Models in Finance: A Survey. 
4th ACM International Conference on AI in Finance, 374–382. 
https://doi.org/10.1145/3604237.3626869 
3. Nazi, Z. A., & Peng, W. (2024). Large Language Models in Healthcare and Medical Domain: 
A Review. Informatics, 11(3), 57. https://doi.org/10.3390/informatics11030057 
4. Gan, W., Qi, Z., Wu, J., & Lin, J. C.-W. (2023). Large Language Models in Education: Vision 
and Opportunities. 2023 IEEE International Conference on Big Data (BigData), 4776–
4785. https://doi.org/10.1109/BigData59044.2023.10386291 
5. Lu, J. G., Song, L. L., & Zhang, L. D. (2025). Cultural tendencies in generative AI. Nature 
Human Behaviour. https://doi.org/10.1038/s41562-025-02242-1 

--- Page 12 ---

6. Guo, Y., Guo, M., Su, J., Yang, Z., Zhu, M., Li, H., Qiu, M., & Liu, S. S. (2024). Bias in Large 
Language Models: Origin, Evaluation, and Mitigation (arXiv:2411.10915). arXiv. 
https://doi.org/10.48550/arXiv.2411.10915 
7. Arzaghi, M., Carichon, F., & Farnadi, G. (2025). Understanding Intrinsic Socioeconomic 
Biases in Large Language Models. In Proceedings of the 2024 AAAI/ACM Conference 
on AI, Ethics, and Society (pp. 49–60). AAAI Press. 
8. Hu, T., Kyrychenko, Y., Rathje, S., Collier, N., Van Der Linden, S., & Roozenbeek, J. (2024). 
Generative language models exhibit social identity biases. Nature Computational 
Science, 5(1), 65–75. https://doi.org/10.1038/s43588-024-00741-1 
9. Kaneko, M., Imankulova, A., Bollegala, D., & Okazaki, N. (2022). Gender Bias in Masked 
Language Models for Multiple Languages. Proceedings of the 2022 Conference of the 
North American Chapter of the Association for Computational Linguistics: Human 
Language Technologies, 2740–2750. https://doi.org/10.18653/v1/2022.naacl-main.197 
10. Rozado, D. (2024). The Political Preferences of LLMs (arXiv:2402.01789). arXiv. 
https://doi.org/10.48550/arXiv.2402.01789 
11. Guey, W., Bougault, P., Moura, V. D. de, Zhang, W., & Gomes, J. O. (2025). Mapping 
Geopolitical Bias in 11 Large Language Models: A Bilingual, Dual-Framing Analysis of 
U.S.-China Tensions (arXiv:2503.23688). arXiv. 
https://doi.org/10.48550/arXiv.2503.23688 
12. Liu, Z. (2023). Cultural Bias in Large Language Models: A Comprehensive Analysis and 
Mitigation Strategies. Journal of Transcultural Communication, 3(2), 224–244. 
https://doi.org/10.1515/jtc-2023-0019 
13. Bouguettaya, A., Stuart, E. M., & Aboujaoude, E. (2025). Racial bias in AI-mediated 
psychiatric diagnosis and treatment: A qualitative comparison of four large language 
models. Npj Digital Medicine, 8(1), 332. https://doi.org/10.1038/s41746-025-01746-4 

--- Page 13 ---

14. Resnik, P. (2024). Large Language Models are Biased Because They Are Large Language 
Models. Computational Linguistics. https://doi.org/10.48550/ARXIV.2406.13138 
15. Jiao, T., Zhang, J., Xu, K., Li, R., Du, X., Wang, S., & Song, Z. (2024). Enhancing Fairness 
in LLM Evaluations: Unveiling and Mitigating Biases in Standard-Answer-Based 
Evaluations. Proceedings of the AAAI Symposium Series, 4(1), 56–59. Crossref. 
https://doi.org/10.1609/aaaiss.v4i1.31771 
16. Navigli, R., Conia, S., & Ross, B. (2023). Biases in Large Language Models: Origins, 
Inventory, and Discussion. Journal of Data and Information Quality, 15(2), 1–21. 
Crossref. https://doi.org/10.1145/3597307 
17. Gallegos, I. O., Rossi, R. A., Barrow, J., Tanjim, M. M., Kim, S., Dernoncourt, F., Yu, T., 
Zhang, R., & Ahmed, N. K. (2024). Bias and Fairness in Large Language Models: A 
Survey. Computational Linguistics, 50(3), 1097–1179. 
https://doi.org/10.1162/coli_a_00524 
18. Karinshak, E., Hu, A., Kong, K., Rao, V., Wang, J., Wang, J., & Zeng, Y. (2024). LLM-
GLOBE: A Benchmark Evaluating the Cultural Values Embedded in LLM Output 
(arXiv:2411.06032). arXiv. https://doi.org/10.48550/arXiv.2411.06032 
19. Doan, T. V., Wang, Z., Hoang, N. N. M., & Zhang, W. (2024). Fairness in Large Language 
Models in Three Hours. Proceedings of the 33rd ACM International Conference on 
Information and Knowledge Management, 5514–5517. 
https://doi.org/10.1145/3627673.3679090 
20. Gilardi, F., Alizadeh, M., & Kubli, M. (2023). ChatGPT outperforms crowd workers for text-
annotation tasks. Proceedings of the National Academy of Sciences, 120(30), 
e2305016120. https://doi.org/10.1073/pnas.2305016120 
 

```
