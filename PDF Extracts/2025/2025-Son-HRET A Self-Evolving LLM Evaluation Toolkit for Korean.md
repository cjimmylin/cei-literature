---
title: "2025-Son-HRET A Self-Evolving LLM Evaluation Toolkit for Korean - PDF Extract"
source_pdf: "2025-Son-HRET A Self-Evolving LLM Evaluation Toolkit for Korean.pdf"
pages: 10
extracted_at: "2026-02-13T09:50:30.666025"
---

# PDF Extract: 2025-Son-HRET A Self-Evolving LLM Evaluation Toolkit for Korean

**Source PDF:** 2025-Son-HRET A Self-Evolving LLM Evaluation Toolkit for Korean.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

Redefining Evaluation Standards: A Unified Framework for Evaluating the
Korean Capabilities of Language Models
Hanwool Lee1,2*, Dasol Choi1,3*, Sooyong Kim1, Ilgyun Jung1,4,
Sangwon Baek1,6, Guijin Son1,7, Inseon Hwang1, Naeun Lee1, Seunghyeok Hong1,5†
1MODULABS, HAERAE LAB
2Shinhan Securities
3Yonsei University
4Catius
5Hankuk University of Foreign Studies
6Korea University
7OneLineAI
gksdnf424@gmail.com
Abstract
Recent advancements in Korean large lan-
guage models (LLMs) have driven numerous
benchmarks and evaluation methods, yet in-
consistent protocols cause up to 10 pp perfor-
mance gaps across institutions. Overcoming
these reproducibility gaps does not mean en-
forcing a one-size-fits-all evaluation. Rather,
effective benchmarking requires diverse exper-
imental approaches and a framework robust
enough to support them. To this end, we in-
troduce HRET (Haerae Evaluation Toolkit),
an open-source, registry-based framework that
unifies Korean LLM assessment. HRET inte-
grates major Korean benchmarks, multiple in-
ference backends, and multi-method evalua-
tion, with language consistency enforcement
to ensure genuine Korean outputs. Its mod-
ular registry design also enables rapid incor-
poration of new datasets, methods, and back-
ends, ensuring the toolkit adapts to evolving
research needs. Beyond standard accuracy met-
rics, HRET incorporates Korean-focused out-
put analyses—morphology-aware Type–Token
Ratio (TTR) for evaluating lexical diversity
and systematic keyword-omission detection for
identifying missing concepts—to provide diag-
nostic insights into language-specific behaviors.
These targeted analyses help researchers pin-
point morphological and semantic shortcom-
ings in model outputs, guiding focused im-
provements in Korean LLM development.
1
Introduction
Recent advances in large language models (LLMs)
demand rigorous, reproducible evaluation, yet real-
world benchmarking often diverges from official
protocols (Liang et al., 2022; Gao et al., 2024). In
Korean NLP, identical models have exhibited per-
formance gaps up to 10 percentage points across
institutions (Research et al., 2024; Bak et al., 2025),
*Equal contribution.
†Corresponding author.
driven by variations in prompt templates, infer-
ence settings, and evaluation criteria. We argue
that true reproducibility arises not from a rigid
framework but from a toolkit that flexibly supports
multiple evaluation paradigms—few-shot versus
log-likelihood scoring, exact-match versus genera-
tive judgment, and test-time scaling techniques—so
that assessments can adapt to both model charac-
teristics and deployment contexts.
Consider KMMLU (Son et al., 2024b), whose
official log-likelihood/direct-generation implemen-
tation in lm-eval-harness is rarely used un-
changed: practitioners often augment it with n-
shot in-context examples (Brown et al., 2020),
inject chain-of-thought prompts, or apply self-
consistency (Wang et al., 2023) to better capture
model reasoning. Such customization highlights
the need for an extensible evaluation framework
that integrates diverse Korean benchmarks and
inference backends while exposing configurable
strategies for prompt design, scoring, and aggrega-
tion.
To meet this need, we present HRET (Haerae
Evaluation Toolkit), an open-source, registry-based
framework for unified Korean LLM assessment.
HRET standardizes data ingestion and result re-
porting, supports string matching, partial match-
ing, log-likelihood, mathematical verification, and
LLM-as-a-judge methods (Zheng et al., 2023), and
applies a language-penalty mechanism to discour-
age non-Korean outputs. Importantly, it embeds
Korean-specific diagnostics—morphology-aware
Type–Token Ratio for lexical diversity and system-
atic keyword-omission detection—to surface lin-
guistic phenomena unique to Korean. Its modular
registry design enables rapid onboarding of new
datasets, methods, and backends, future-proofing
evaluation as the field evolves.
We validate HRET’s robustness and efficiency
across diverse hardware configurations, demonstrat-
ing substantial reductions in evaluation variability
arXiv:2503.22968v4  [cs.CE]  8 Jul 2025

--- Page 2 ---

HAE-RAE 
Bench
KMMLU
CLIcK
KUDGE
K2-Eval
HRM8K
HuggingFace
LiteLLM
OpenAI-
compatible
Model Loading and Configuration
Unified interface for various model backends
Inference with Scaling Methods
Efficient generation strategies for improved performance
Dataset Loading and Preprocessing
Standardized dataset preparation and formatting
Beam Search
Majority Voting
Best-of-N
String Match
Log-Probability
Math-Verify
LLM-as-a-Judge
Runner
Evaluator
Dataset Registry
Backend Registry
Scaling Registry
Evaluation Registry
Comprehensive Evaluation Methods
Multiple evaluation techniques for nuanced assessment
Figure 1: Architecture overview of HRET, showing the registry-based modular design that integrates datasets,
models, inference strategies, and evaluation methods through a unified pipeline.
and improved throughput. HRET thus offers a prac-
tical solution for reproducible, adaptable bench-
marking in Korean LLM research.
2
Related Work and Background
2.1
LLM Benchmarks and Leaderboards
The English LLM ecosystem has established robust
evaluation frameworks like Evalverse (Kim et al.,
2024b) and deepeval (AI, 2025). The lm-evaluation-
harness (Gao et al., 2024) by Upstage has been
particularly influential, powering their Open LLM
Leaderboard which has accelerated global LLM
development. Its success highlights how easy-to-
use evaluation tools can democratize model devel-
opment - lowering barriers for smaller research
labs and startups to participate in advancing the
field. Similarly, Chinese frameworks like FlagEval
(Team, 2025) have adopted this accessibility-first
approach to systematically advance their language-
specific ecosystems.
2.2
Reproducibility Challenges
Evaluations of Korean language models often show
inconsistent results across institutions, with the
same models reporting performance gaps of up
to 10 percentage points. For instance, Gemma2-
27B and Qwen2.5-32B (Qwen et al., 2025) achieve
scores that differ by 1–10 pp on GSM8K, KMMLU,
HumanEval and MBPP when comparing the
EXAONE 3.5 report (Research et al., 2024) and
the Kanana report (Bak et al., 2025) (Table 1). This
variability underscores the absence of consistent
evaluation practices tailored to Korean LLMs, com-
plicating direct comparisons and hindering repro-
ducibility.
These gaps arise from varying inference set-
tings, prompt designs, and evaluation implemen-
tations. On top of that, Korean’s own characteris-
tics—its rich morphology, context-dependent tok-
enization, and honorific system—make consistent
handling difficult without standardized, Korean-
focused guidelines. Together, these factors exacer-
bate result variability and impede reliable bench-
marking across research groups.
2.3
Comparison with Existing Systems
To position HRET within the landscape of LLM
evaluation frameworks, Table 2 compares its fea-
tures with other systems. This comparison high-
lights HRET’s unique contributions to the field,
particularly its focus on Korean language evalua-
tion and its registry-based modular architecture.
HRET differentiates itself through three key
aspects: (1) Korean-specific capabilities includ-

--- Page 3 ---

Report
Model
Datasets
GSM8K
MMLU
KMMLU
HumanEval
MBPP
EXAONE 3.5 Report
(Research et al., 2024)
Qwen2.5-32B
92.00
81.40
62.10
89.00
88.90
Gemma2-27B
84.20
74.80
53.80
79.30
80.70
Kanana Report
(Bak et al., 2025)
Qwen2.5-32B
95.30
84.40
59.37
82.32
71.96
Gemma2-27B
91.05
78.30
49.98
70.12
70.90
Table 1: Performance discrepancies for identical models (Qwen et al., 2025; Team et al., 2024) between EXAONE
3.5 and Kanana technical reports, highlighting reproducibility challenges in Korean NLP evaluations.
Feature
lm-eval-harness
(Biderman et al., 2024)
OpenAI Evals
(Liu et al., 2024)
Evalverse
(Kim et al., 2024b)
DeepEval
(AI, 2025)
HRET (Ours)
Primary Focus
Academic benchmarks
OpenAI model evaluation
Unified evaluation hub
Unit/regression testing
Korean LLM evaluation
Developer
EleutherAI
OpenAI
Upstage
Confident AI
HAERAE
Architecture
Task/Metric modules
Evaluation scripts
Submodule integration
Test case-based
Registry-based plugins
Built-in Benchmarks
60+ general benchmarks
Several public evals
Integrated external benchmarks
Major benchmarks
Korean-focused benchmarks
Evaluation Metrics
Traditional metrics
Task-specific scripts
Integrated metrics
5+ diverse metrics
5+ diverse metrics
User Interface
CLI only
CLI + Dashboard
Slack bot + Web
CLI + Web dashboard
CLI + API
Automation
Script-based
API-based
No-code automation
CI/CD integration
API-based, CI/CD integration
Unique Strength
High reproducibility
OpenAI optimization
Multi-tool integration
Testing-focused
Korean-specific + Registry extensibility
Table 2: Feature comparison of HRET with major existing LLM evaluation frameworks, highlighting its registry-
based extensibility and Korean-specific benchmarks.
ing language consistency enforcement and con-
cise morphological analysis–based output diagnos-
tics, (2) registry-based extensibility that enables
rapid component integration compared to tradi-
tional monolithic architectures, and (3) unified
evaluation pipeline that unifies fragmented Ko-
rean LLM assessment practices. Unlike existing
frameworks that focus on general-purpose evalua-
tion, HRET addresses specific reproducibility chal-
lenges observed in Korean NLP research (Table 1).
3
HRET Framework
HRET (Haerae Evaluation Toolkit) addresses crit-
ical reproducibility and comparability challenges
faced in evaluating Korean large language models
(LLMs). By providing a standardized yet flexible
evaluation environment, HRET fosters consistency,
transparency, and accessibility in Korean NLP re-
search. Figure 1 illustrates its modular and registry-
based architecture, seamlessly integrating datasets,
evaluation methods, inference strategies, and model
backends into a coherent evaluation pipeline.
HRET is explicitly designed for: (1) researchers
who require standardized evaluation methods for
benchmarking Korean language models; (2) devel-
opers looking for robust tools to streamline model
assessment and selection; and (3) industry practi-
tioners aiming to reliably deploy Korean LLMs in
production.
3.1
Design Principles
HRET introduces several innovative approaches to
address the challenges of Korean LLM evaluation:
• Registry-Based Modularity: Core compo-
nents—including dataset loaders, evaluation
methods, scaling strategies, and inference
backends—are individually modularized and
managed through registries, allowing re-
searchers to effortlessly extend the toolkit’s
capabilities with minimal code changes com-
pared to traditional monolithic architectures.
• Unified Standardization: HRET systemati-
cally standardizes fragmented Korean LLM
evaluation practices by providing consistent
interfaces, reproducible workflows, and trans-
parent benchmarking procedures across differ-
ent research environments.
• Korean Language Consistency: Penalizes
any response not in Korean by applying a
score penalty, ensuring evaluation focuses
strictly on Korean outputs.
• Concurrency and Scalability: Leveraging
asynchronous HTTP requests (via httpx) and
multi-threading, HRET significantly enhances
throughput during large-scale evaluations, es-
sential for computationally intensive Korean
benchmarks.

--- Page 4 ---

• Unified API: HRET simplifies interaction
through consistent Evaluator and PipelineRun-
ner interfaces, reducing the entry barrier for
both novice researchers and industry practi-
tioners.
3.2
System Architecture and Components
HRET provides a unified interface for evaluating
major Korean NLP benchmarks including HAE-
RAE Bench, KMMLU, KUDGE, HRM8K, CLIcK,
and others (see Appendix A for complete list), fol-
lowing a standardized five-stage workflow:
1. Dataset Loading: The Dataset Registry uni-
fies Korean NLP datasets with consistent for-
matting, supporting standard benchmarks and
offering a flexible generic_file loader for cus-
tom datasets without dedicated classes.
2. Model Loading: The Backend Registry con-
nects to various backends (HuggingFace,
vLLM, OpenAI-compatible, etc), providing
a unified interface that abstracts provider-
specific details while supporting generation,
judge, and reward functionalities.
3. Inference with Scaling: Scaling Techniques
enhance evaluation quality through (1) Beam
Search for exploring different decoding paths,
(2) Best-of-N Sampling for selecting optimal
outputs, and (3) Majority Voting for enhanc-
ing stability through consensus.
4. Evaluation: Generated predictions are as-
sessed using multiple approaches: (1) String-
matching, (2) Logit-based Evaluation (3)
Mathematical Verification for semantic equiv-
alence in mathematical reasoning tasks, and
(4) LLM-as-a-Judge. Additional enhance-
ments include Language consistency enforce-
ment for detecting non-Korean responses and
Answer extraction for identifying final an-
swers from reasoning chains.
5. Results Reporting: Runtime Components or-
chestrate the pipeline, with the Runner com-
bining components from all registries and the
Evaluator implementing a facade pattern pro-
viding a simplified API.
This architecture ensures consistency across eval-
uations while providing flexibility through plug-
gable components at each stage.
3.3
Advanced Evaluation Pipeline
Beyond the standard Evaluator API, HRET pro-
vides a flexible PipelineRunner for advanced cus-
tomization of evaluation workflows. This interface
enables multi-stage evaluations where outputs from
one model serve as inputs to another, comprehen-
sive model comparisons across different bench-
marks and metrics, custom workflows with spe-
cialized processing steps for Korean-specific evalu-
ations, and ensemble evaluations combining com-
plementary models or methodologies.
3.4
Korean-Specific Analysis Capabilities
HRET extends beyond standard metrics by inte-
grating a Korean-specific morphological analyzer
to deliver four core analyses: (1) Overall Perfor-
mance with detailed accuracy, sample counts, and
prediction distributions; (2) Subset Analysis high-
lighting variations across task types (e.g., reading
comprehension vs. cultural knowledge); (3) Lexi-
cal Diversity via Type–Token Ratio (TTR) compar-
isons between correct and incorrect outputs; and (4)
Error Pattern Detection through keyword-based
inference of frequent failure modes.
Together, these tools form a diagnostic frame-
work tailored to Korean linguistic characteris-
tics—highlighting morphological limitations and
vocabulary gaps that standard accuracy alone can-
not capture, and guiding targeted improvements in
model training and evaluation.
3.5
Usage Examples
HRET provides intuitive command-line and Python
API interfaces. A simple CLI example for evaluat-
ing a Korean LLM on HAE-RAE Bench:
python -m llm_eval.evaluator \
--model huggingface \
--model_params
'{" model_name_or_path ":
"google/gemma -3-1b-it"}' \
--dataset haerae_bench \
--subset csat_geo \
--split test \
--evaluation_method string_match \
--output_file results.json
This command loads the specified dataset and
model, performs string-match evaluation, and out-
puts results in JSON format. Additional usage sce-
narios and advanced functionalities are provided in
Appendix D.

--- Page 5 ---

4
System Evaluation
4.1
Reproducibility Validation
To validate HRET’s ability to address reproducibil-
ity challenges in Korean LLM evaluation, we
conducted cross-institutional experiments across
different hardware configurations and backend
implementations. We evaluated three representa-
tive models (Qwen2.5-3B (Qwen et al., 2025),
Qwen3-8B (Yang et al., 2025), Llama-3.2-3B-
Instruct (Meta AI, 2024)) on Korean benchmarks
using log-likelihood evaluation across four hard-
ware setups with varying CPU architectures, GPU
types, and memory configurations.
Model
Max Variation
Hardware Configs
Qwen2.5-3B
0.0016 (0.56%)
4 setups
Qwen3-8B
0.0028 (1.06%)
4 setups
Llama-3.2-3B
0.0015 (0.62%)
4 setups
Table 3: Hardware robustness summary across environ-
ments (detailed table in Appendix C).
Results demonstrate remarkable consistency de-
spite significant hardware variations. Accuracy
scores remained stable across different CPU ar-
chitectures, GPU types, and batch sizes (1–64),
with standard deviations under 0.003. Cross-
institutional experiments showed identical or near-
identical scores, validating HRET’s ability to elim-
inate evaluation discrepancies observed in Table 1.
Hardware Configuration
HAE-RAE
CLIcK
AMD EPYC 74F3 + H100
0.1806
0.1343
Intel Xeon + A100-80GB
0.1788
0.1298
Intel Xeon + H200
0.1802
0.1308
Standard Deviation
0.0009
0.0023
Table 4: Backend robustness using vLLM for Qwen2.5-
3B.
Backend comparison between HuggingFace and
vLLM shows that while absolute scores differ
due to implementation differences, results remain
highly consistent within each backend (σ < 0.003).
Compared to the 1–10 percentage point discrepan-
cies reported between institutions, HRET achieves
hardware robustness with standard deviations un-
der 0.003 and cross-institutional consistency when
using standardized procedures.
4.2
Multi-Method Evaluation Analysis
Korean language tasks exhibit diverse character-
istics that benefit from different evaluation ap-
proaches. HRET’s multi-method evaluation frame-
work enables researchers to select the most appro-
priate assessment strategy for each task type, lead-
ing to more accurate performance measurements.
Table 5 compares evaluation methods across dif-
ferent Korean benchmarks using EXAONE-3.5-
2.4B (Research et al., 2024) as a case study. The
results demonstrate significant performance vari-
ations depending on the evaluation method em-
ployed, with notable differences between task
types.
Benchmark
String-Match
Math-Verify
LLM-as-judge(w.gpt-4o-2024-11-20)
HRM8K
2.21
14.11
17.60
CLIcK
27.31
28.67
27.76
Table 5: Comparison of evaluation methods for
EXAONE-3.5-2.4B across Korean benchmarks.
Task-Dependent
Sensitivity
Mathematical
reasoning (HRM8K) sees dramatic score in-
creases—from 2.21% (String-Match) to 17.60%
(LLM-as-judge)—highlighting
the
need
for
semantic evaluation over exact matching.
Evaluation Robustness
Cultural and linguistic
tasks (CLIcK) remain consistent (27.31–28.67%)
across methods, indicating lower sensitivity to met-
ric choice.
Methodological Implications
By matching met-
ric to task—semantic methods for reasoning, exact-
match for comprehension—HRET balances accu-
racy and efficiency across diverse Korean language
evaluations.“‘
4.3
Test-Time Scaling Techniques
HRET incorporates advanced test-time scaling
techniques to enhance evaluation quality through
multiple inference strategies. These methods are
particularly valuable for Korean language evalua-
tion, where single predictions may not fully capture
model capabilities due to linguistic complexity and
cultural contexts.
The framework supports three primary ap-
proaches: Best-of-N Sampling, Self-Consistency
with majority voting, and Beam Search for optimal
decoding paths. These techniques can be combined
with various evaluation methods, including LLM-
as-a-judge assessments.
Table 6 demonstrates test-time scaling effective-
ness on HAERAE Reasoning Challenge (HRC),
evaluating Korean reasoning across science, math-
ematics, and quiz domains.

--- Page 6 ---

Model
Benchmark
n=1
n=3
n=5
EXAONE-3.5-2.4B
HRC
3.37
5.04
9.24
Qwen2.5-3B-Instruct
11.76
12.60
13.44
Table 6: Test-time scaling results with LLM-as-a-
judge(w. gpt-4o-2024-11-20) on HRC.
Results show substantial performance gains
through increased sampling, with EXAONE-3.5-
2.4B achieving 2.7x improvement at n=5 versus
single-shot evaluation. This validates test-time scal-
ing effectiveness for complex Korean reasoning
tasks requiring nuanced understanding of context
and cultural references.
4.4
Extensibility
Our registry-based design uses simple Python
decorators to enable seamless extension. New
Models
inherit
from
BaseModel
and
add
@register_model; new Datasets inherit from
BaseDataset and add @register_dataset; new
Evaluators inherit from BaseEvaluator and add
@register_evaluator; and new Test-time scal-
ing methods inherit from BaseScalingMethod
and add @register_scaling_method. All dec-
orated classes are auto-registered at runtime,
allowing users to plug in new components with
zero additional configuration.
To
foster
community-driven
development,
HRET actively welcomes external contributions
and is committed to continuous maintenance
and
expansion.
This
collaborative
approach
ensures the framework evolves with the Korean
LLM landscape while maintaining backward
compatibility for existing users.
5
Conclusion
We introduce HRET, a unified evaluation frame-
work that addresses critical reproducibility chal-
lenges in Korean LLM evaluation. Through its
registry-based architecture and standardized pro-
tocols, HRET significantly improves evaluation
consistency while supporting diverse assessment
strategies. HRET integrates major Korean bench-
marks with multiple inference backends and eval-
uation methods, enabling researchers to select
task-appropriate strategies while maintaining repro-
ducibility. The framework’s extensible design and
community-driven development ensure it evolves
with the Korean LLM landscape, providing a sus-
tainable foundation for reproducible assessment.
Limitations
While HRET provides a standardized evaluation
framework for Korean LLMs, several limitations
remain. Despite integrating major Korean bench-
marks, coverage in specialized domains (Hwang
et al., 2025) remains limited. The language con-
sistency enforcement may struggle with mixed-
language outputs or code-switching common in
technical contexts, and computational requirements
for test-time scaling techniques can be substan-
tial, potentially limiting accessibility for resource-
constrained environments. Current evaluation met-
rics, particularly string matching, may not fully
capture Korean’s rich morphological variations and
honorific systems, and the framework’s effective-
ness depends on the quality of integrated bench-
marks. We are addressing these limitations through
ongoing development and welcome community
contributions to enhance HRET’s capabilities.
References
Confident AI. 2025.
Deepeval: The llm evaluation
framework. Accessed: 2025-01-26.
Yunju Bak, Hojin Lee, Minho Ryu, Jiyeon Ham, Se-
ungjae Jung, Daniel Wontae Nam, Taegyeong Eo,
Donghun Lee, Doohae Jung, Boseop Kim, et al. 2025.
Kanana: Compute-efficient bilingual language mod-
els. arXiv preprint arXiv:2502.18934.
Stella Biderman, Hailey Schoelkopf, Lintang Sutawika,
Leo Gao, Jonathan Tow, Baber Abbasi, Alham Fikri
Aji, Pawan Sasanka Ammanamanchi, Sidney Black,
Jordan Clive, et al. 2024. Lessons from the trenches
on reproducible evaluation of language models.
arXiv preprint arXiv:2405.14782.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, et al. 2020. Language models are few-shot
learners. Advances in neural information processing
systems, 33:1877–1901.
Leo Gao, Jonathan Tow, Baber Abbasi, Stella Biderman,
Sid Black, Anthony DiPofi, Charles Foster, Laurence
Golding, Jeffrey Hsu, Alain Le Noac’h, Haonan Li,
Kyle McDonell, Niklas Muennighoff, Chris Ociepa,
Jason Phang, Laria Reynolds, Hailey Schoelkopf,
Aviya Skowron, Lintang Sutawika, Eric Tang, An-
ish Thite, Ben Wang, Kevin Wang, and Andy Zou.
2024. A framework for few-shot language model
evaluation.
Yewon Hwang, Sungbum Jung, Hanwool Lee, and Sara
Yu. 2025. Twice: What advantages can low-resource
domain-specific embedding model bring? – a case
study on korea financial texts.

--- Page 7 ---

Eunsu Kim, Juyoung Suk, Philhoon Oh, Haneul Yoo,
James Thorne, and Alice Oh. 2024a. Click: A bench-
mark dataset of cultural and linguistic intelligence in
korean. arXiv preprint arXiv:2403.06412.
Jihoo Kim, Wonho Song, Dahyun Kim, Yunsu Kim,
Yungi Kim, and Chanjun Park. 2024b. Evalverse:
Unified and accessible library for large language
model evaluation. arXiv preprint arXiv:2404.00943.
Yeeun Kim, Young Rok Choi, Eunkyung Choi, Jinhwan
Choi, Hai Jin Park, and Wonseok Hwang. 2024c. De-
veloping a pragmatic benchmark for assessing korean
legal language understanding in large language mod-
els.
Hyunwoo Ko, Guijin Son, and Dasol Choi. 2025. Un-
derstand, solve and translate: Bridging the multilin-
gual mathematical reasoning gap. arXiv preprint
arXiv:2501.02448.
Sunjun Kweon, Byungjin Choi, Gyouk Chu, Junyeong
Song, Daeun Hyeon, Sujin Gan, Jueon Kim, Minkyu
Kim, Rae Woong Park, and Edward Choi. 2024. Ko-
rmedmcqa: Multi-choice question answering bench-
mark for korean healthcare professional licensing
examinations.
Percy Liang, Rishi Bommasani, Tony Lee, Dimitris
Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian
Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Ku-
mar, et al. 2022. Holistic evaluation of language
models. arXiv preprint arXiv:2211.09110.
Chuang Liu, Linhao Yu, Jiaxuan Li, Renren Jin, Yufei
Huang, Ling Shi, Junhui Zhang, Xinmeng Ji, Tingt-
ing Cui, Tao Liu, et al. 2024. Openeval: Benchmark-
ing chinese llms across capability, alignment and
safety. arXiv preprint arXiv:2403.12316.
Meta
AI.
2024.
Llama
3.2
3b
instruct.
https://huggingface.co/meta-llama/Llama-3.
2-3B-Instruct. Version release date: 25 Sep 2024.
Qwen, :, An Yang, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li,
Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin,
Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang,
Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang,
Keming Lu, Keqin Bao, Kexin Yang, Le Yu, Mei Li,
Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji
Lin, Tianhao Li, Tianyi Tang, Tingyu Xia, Xingzhang
Ren, Xuancheng Ren, Yang Fan, Yang Su, Yichang
Zhang, Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru
Zhang, and Zihan Qiu. 2025. Qwen2.5 technical
report.
LG Research, Soyoung An, Kyunghoon Bae, Eunbi
Choi, Kibong Choi, Stanley Jungkyu Choi, Seokhee
Hong, Junwon Hwang, Hyojin Jeon, Gerrard Jeong-
won Jo, et al. 2024.
Exaone 3.5: Series of large
language models for real-world use cases. arXiv
preprint arXiv:2412.04862.
Guijin Son, Hyunwoo Ko, and Dasol Choi. 2025. Multi-
step reasoning in korean and the emergent mirage.
arXiv preprint arXiv:2501.05712.
Guijin Son, Hyunwoo Ko, Hoyoung Lee, Yewon Kim,
and Seunghyeok Hong. 2024a. Llm-as-a-judge &
reward model: What they can and cannot do. arXiv
preprint arXiv:2409.11239.
Guijin Son, Hanwool Lee, Sungdong Kim, Seungone
Kim, Niklas Muennighoff, Taekyoon Choi, Cheon-
bok Park, Kang Min Yoo, and Stella Biderman.
2024b. Kmmlu: Measuring massive multitask lan-
guage understanding in korean.
arXiv preprint
arXiv:2402.11548.
Guijin Son, Hanwool Lee, Suwan Kim, Huiseo Kim,
Jaecheol Lee, Je Won Yeom, Jihyu Jung, Jung Woo
Kim, and Songseong Kim. 2023. Hae-rae bench:
Evaluation of korean knowledge in language models.
arXiv preprint arXiv:2309.02706.
FlagEval Team. 2025. Flageval: An open-source evalu-
ation toolkit for large models. Accessed: March 10,
2025.
Gemma Team, Morgane Riviere, Shreya Pathak,
Pier Giuseppe Sessa, Cassidy Hardin, Surya Bhupati-
raju, Léonard Hussenot, Thomas Mesnard, Bobak
Shahriari, Alexandre Ramé, et al. 2024. Gemma 2:
Improving open language models at a practical size.
arXiv preprint arXiv:2408.00118.
Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le,
Ed Chi, Sharan Narang, Aakanksha Chowdhery, and
Denny Zhou. 2023. Self-consistency improves chain
of thought reasoning in language models.
An Yang, Anfeng Li, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao,
Chengen Huang, Chenxu Lv, Chujie Zheng, Dayi-
heng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao Ge,
Haoran Wei, Huan Lin, Jialong Tang, Jian Yang, Jian-
hong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang,
Jing Zhou, Jingren Zhou, Junyang Lin, Kai Dang,
Keqin Bao, Kexin Yang, Le Yu, Lianghao Deng,
Mei Li, Mingfeng Xue, Mingze Li, Pei Zhang, Peng
Wang, Qin Zhu, Rui Men, Ruize Gao, Shixuan Liu,
Shuang Luo, Tianhao Li, Tianyi Tang, Wenbiao Yin,
Xingzhang Ren, Xinyu Wang, Xinyu Zhang, Xu-
ancheng Ren, Yang Fan, Yang Su, Yichang Zhang,
Yinger Zhang, Yu Wan, Yuqiong Liu, Zekun Wang,
Zeyu Cui, Zhenru Zhang, Zhipeng Zhou, and Zihan
Qiu. 2025. Qwen3 technical report.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan
Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin,
Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang,
Joseph E. Gonzalez, and Ion Stoica. 2023. Judging
llm-as-a-judge with mt-bench and chatbot arena.

--- Page 8 ---

A
Supported Benchmarks
HRET provides unified evaluation support for ma-
jor Korean language benchmarks spanning diverse
domains and task types. The framework’s registry-
based architecture enables seamless integration of
these benchmarks with consistent preprocessing,
evaluation protocols, and result formatting. Table 7
provides detailed descriptions of currently sup-
ported benchmarks, organized by evaluation focus.
The benchmark collection covers three primary
categories: General benchmarks assess broad Ko-
rean language understanding and cultural knowl-
edge, Dialogue benchmarks evaluate conversa-
tional capabilities in Korean contexts, and Spe-
cialized benchmarks target domain-specific com-
petencies including mathematical reasoning and
professional knowledge. This comprehensive cov-
erage enables researchers to conduct thorough eval-
uations across the spectrum of Korean language
model capabilities.
B
Performance Comparison with Existing
Tools
Table 8 compares HRET’s computational perfor-
mance with lm-evaluation-harness using Qwen2.5-
3B on identical hardware configurations.
HRET shows mixed performance: faster on
HAE-RAE Bench but slower on KMMLU. Higher
RAM usage stems from loading datasets as editable
objects to enable real-time filtering and experimen-
tal modifications through our system. Higher CPU
utilization (up to 525%) reflects multi-threading
optimization. Both frameworks use <1% of total
system memory, indicating efficient resource uti-
lization despite HRET’s flexibility-oriented design.
C
Detailed Reproducibility Results
To complement the summary presented in Sec-
tion 4.1, we provide the full hardware-wise evalu-
ation results across multiple configurations. This
table reports evaluation scores for three represen-
tative models using the HuggingFace backend un-
der diverse CPU and GPU settings. These include
server-grade (A100, H100) and workstation-grade
(RTX A6000, RTX 3090) environments, reflecting
real-world variance across institutions.
D
Usage Examples and Tutorials
This section provides advanced examples and tuto-
rials for using HRET beyond the basic functionality
introduced in the main paper.
D.1
Advanced Backend Usage
HRET supports multiple backend integrations be-
yond standard HuggingFace models:
D.1.1
LiteLLM and OpenAI-Compatible
APIs
Access over 30 LLM providers and self-hosted
servers:
# Using LiteLLM for cloud -based models
results = evaluator.run(
model="litellm",
model_params ={
"model_name": "gpt -4",
"api_key": "your -api -key -here",
},
dataset="haerae_bench",
evaluation_method="string_match"
)
# Using OpenAI -compatible endpoints for
self -hosted models
results = evaluator.run(
model="openai",
model_params ={
"model_name": "local -llama -2-13b
",
"api_base": "http :// localhost
:8000/ v1",
},
dataset="haerae_bench",
evaluation_method="string_match"
)
D.2
Evaluation Methods
D.2.1
String Match and Log Probability
Evaluation
HRET offers flexible text matching with various
normalization options:
# String matching with normalization
options
results = evaluator.run(
model="huggingface",
model_params ={"model_name_or_path":"
Qwen/Qwen2 .5-3B-Instruct"},
dataset="haerae_bench",
evaluation_method='string_match ',
evaluator_params ={
"ignore_case": True ,
"ignore_punctuation": True ,
"extract_answer": True ,
}
)
# Log probability evaluation for MCQA
results = evaluator.run(
model="huggingface",
dataset="haerae_bench",
evaluation_method='log_likelihood ',
dataset_params ={"
base_prompt_template": "{query}
### Answer:"},
)

--- Page 9 ---

Category
Benchmark
Description
General
HAE-RAE
(Son et al., 2023)
Evaluation of Korean language understanding, focusing on vocabulary, reading compre-
hension, and general knowledge.
KMMLU
(Son et al., 2024b)
Multi-domain knowledge across 45 categories (STEM, humanities, applied sciences) in
Korean.
CLIcK
(Kim et al., 2024a)
Cultural and linguistic proficiency via 1,995 QA pairs from Korean exams/textbooks.
Dialogue
KUDGE
(Son et al., 2024a)
Coherence and contextual appropriateness in Korean dialogue generation.
Specialized
K2-Eval
(Son et al., 2024a)
Tests professional and technical Korean terminology.
HRM8K
(Ko et al., 2025)
Measures math reasoning on 8,011 Korean problems.
HRMCR
(Son et al., 2025)
Multi-step commonsense questions using Korean cultural templates.
HRC
119 Korean reasoning problems across science, mathematics, and quiz domains.
KorMedQA
(Kweon et al., 2024)
7,469 medical licensing MCQs (2012–2024) for Korean healthcare.
KBL
(Kim et al., 2024c)
Legal understanding: knowledge, reasoning, and bar-exam tasks in closed-book and
RAG settings.
Table 7: Descriptions of benchmarks supported in HRET.
Metric
HRET
lm-eval-harness
HAE-RAE Bench
Execution Time (sec)
114.93
142.44
Max RAM (MB)
80.96 (<1%)
54.26 (<1%)
Max CPU (%)
525.84
100.0
KMMLU
Execution Time (sec)
303.93
221.04
Max RAM (MB)
104.81 (<1%)
78.76 (<1%)
Max CPU (%)
458.90
199.0
Table 8: Performance comparison on AMD EPYC 74F3
64-Core + NVIDIA H100 with 193GB RAM. Values
averaged across 3 runs.
These examples demonstrate HRET’s capabili-
ties for Korean language model evaluation beyond
the basic functionality presented in the main paper.
The project repository provides comprehensive tu-
torials and documentation in both Korean and En-
glish, including additional examples, best practices,
and implementation guidelines.
E
Real-World Usage
Beyond academic evaluation frameworks, HRET
has been adopted in production environments
across the Korean NLP industry. Authors’ affiliated
organizations, including Shinhan Securities and
OneLineAI, have integrated HRET into their model
validation and post-training evaluation workflows,
demonstrating the framework’s practical utility in
real-world deployment scenarios. Additionally, the
Haerae Reasoning Challenge (HRC) officially em-
ploys HRET to score all participant submissions
under standardized protocols, ensuring fairness and
transparency in competitive evaluations. This pro-
duction adoption validates HRET’s reliability and
effectiveness beyond controlled research settings,
confirming its value for industry practitioners re-
quiring robust evaluation infrastructure.
Ethics Statement
latexHRET aims to improve reproducibility and
fairness in Korean LLM evaluation. However, we
acknowledge several ethical considerations: (1)
standardized evaluation frameworks may inadver-
tently favor certain model architectures or training
approaches; (2) benchmark selection reflects our re-
search perspectives and may not capture all aspects
of Korean language competency; (3) language con-
sistency enforcement, while promoting Korean lan-
guage assessment, may disadvantage multilingual
models in certain contexts. We encourage the com-
munity to contribute diverse benchmarks and evalu-
ation methods to ensure broad representation of Ko-
rean language capabilities. All integrated datasets
respect original licensing and guidelines.

--- Page 10 ---

Model
Hardware Setup
HAE-RAE
CLIcK
Batch Size
Qwen2.5-3B
AMD EPYC 74F3 + A100×2
0.2847
0.3388
64
AMD EPYC 9354 + RTX A6000
0.2847
0.3388
2
Intel i9-13900K + RTX A6000
0.2847
0.3388
2
Intel Xeon + A100-40GB
0.2863
0.3378
64
Qwen3-8B
AMD EPYC 74F3 + A100×2
0.2645
0.3083
64
AMD EPYC 9354 + RTX A6000
0.2645
0.3083
1–2
Intel i9-13900K + RTX A6000
0.2645
0.3083
2
Intel Xeon + A100-40GB
0.2673
0.3083
64
Llama-3.2-3B
AMD EPYC 74F3 + A100×2
0.2436
0.2922
64
AMD EPYC 7452 + RTX 3090
0.2437
0.2922
2
Intel i9-13900K + RTX A6000
0.2445
0.2922
2
Intel Xeon + A100-40GB
0.2447
0.2907
64
Table 9: Reproducibility validation across different hardware configurations using HuggingFace backend.

```
