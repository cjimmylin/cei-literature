---
title: "2025-Liu-JailBench A Comprehensive Chinese Security Assessment Benchmark for - PDF Extract"
source_pdf: "2025-Liu-JailBench A Comprehensive Chinese Security Assessment Benchmark for.pdf"
pages: 12
extracted_at: "2026-02-15T17:54:26.714756"
---

# PDF Extract: 2025-Liu-JailBench A Comprehensive Chinese Security Assessment Benchmark for

**Source PDF:** 2025-Liu-JailBench A Comprehensive Chinese Security Assessment Benchmark for.pdf
**Total Pages:** 12

---

## Content

```
--- Page 1 ---

JailBench: A Comprehensive Chinese Security
Assessment Benchmark for Large Language
Models
Shuyi Liu, Simiao Cui, Haoran Bu, Yuming Shang, and Xi Zhang⋆
Key Laboratory of Trustworthy Distributed Computing and Service (MoE),
Beijing University of Posts and Telecommunications, China
{liushuyi111,csim,buhaoran2002,shangym,zhangx}@bupt.edu.cn
Abstract. Large language models (LLMs) have demonstrated remark-
able capabilities across various applications, highlighting the urgent need
for comprehensive safety evaluations. In particular, the enhanced Chi-
nese language proficiency of LLMs, combined with the unique charac-
teristics and complexity of Chinese expressions, has driven the emer-
gence of Chinese-specific benchmarks for safety assessment. However,
these benchmarks generally fall short in effectively exposing LLM safety
vulnerabilities. To address the gap, we introduce JailBench, the first
comprehensive Chinese benchmark for evaluating deep-seated vulnera-
bilities in LLMs, featuring a refined hierarchical safety taxonomy tailored
to the Chinese context. To improve generation efficiency, we employ a
novel Automatic Jailbreak Prompt Engineer (AJPE) framework for Jail-
Bench construction, which incorporates jailbreak techniques to enhance
assessing effectiveness and leverages LLMs to automatically scale up the
dataset through context-learning. The proposed JailBench is extensively
evaluated over 13 mainstream LLMs and achieves the highest attack suc-
cess rate against ChatGPT compared to existing Chinese benchmarks,
underscoring its efficacy in identifying latent vulnerabilities in LLMs, as
well as illustrating the substantial room for improvement in the security
and trustworthiness of LLMs within the Chinese context. Our benchmark
is publicly available at https://github.com/STAIR-BUPT/JailBench.
Keywords: Large language models · Chinese benchmark · Security as-
sessment · Jailbreak attack.
1
Introduction
Large language models have achieved remarkable progress across numerous do-
mains, exhibiting unprecedented capabilities and vast knowledge repositories
that have captivated extensive scholarly inquiry [1,17]. Alongside their impres-
sive capabilities, there are also significant concerns regarding the safety and
trustworthiness of these models, such as their ability to generate harmful or
⋆Corresponding author.
arXiv:2502.18935v1  [cs.CL]  26 Feb 2025

--- Page 2 ---

2
S. Liu et al.
Table 1: Comparison of existing Chinese
safety assessment benchmarks and our
JailBench. Here we measure the Attack
Success Rate (ASR) of the benchmark
on ChatGPT as a measure of its effec-
tiveness for LLMs safety evaluations.
Benchmarks
Size Classification
ASR
Do-Not-Answer [19]
0.9k
6-17
-
Safety-prompts [15]
100k
7
1.63%
CValues [23]
3.9k
10
3.10%
Multilingual [18]
2.8k
8
15.90%
SafetyBench [29]
11k
7
19.60%
Flames [7]
2.2k
5-12
53.09%
JailBench(Ours)
10.8k
5-40
73.86%
Fig. 1: Illustration of the overall con-
struction process and methodologi-
cal framework of JailBench.
malicious content, potentially escalating to uncontrollable threats against social
values and individual rights [16,21]. Therefore, it is indispensable to conduct
comprehensive evaluations of LLM safety, as several researchers have already
focused on benchmarking their ethical values and safety features [14,6,20,9].
The expansion of Chinese training corpora significantly enhances LLMs’ pro-
ficiency, coupled with the characteristics and complexity of Chinese expressions,
spurring the development of several benchmarks specifically designed for evalu-
ating LLM safety within the Chinese linguistic context [23,29,7].
However, these benchmarks still exhibit several limitations: Firstly, most
benchmarks employ inconsistent categorization criteria, leading to incomplete
coverage of the entire safety domain, particularly in Chinese-specific contexts.
Secondly, the construction of many benchmarks lacks automated prompt gen-
eration and rapid scaling methods, thereby raising the construction cost and
restricting their comprehensiveness. Thirdly, existing benchmarks struggle to
uncover potential vulnerabilities as their harmful queries can be easily deflected
by safety-equipped LLMs, necessitating more robust and efficient evaluations.
To address the above limitations of existing benchmarks, we propose Jail-
Bench, the first comprehensive benchmark for evaluating deep-seated safety vul-
nerabilities in LLMs within the Chinese linguistic context. As shown in Table 1,
JailBench offers three distinct advantages: (1) Unified Safety Taxonomy. Jail-
Bench incorporates an extensive and refined hierarchical safety taxonomy, which
encompasses a wide range of potentially harmful scenarios unique to the Chinese
linguistic and cultural context, ensuring a thorough evaluation of LLMs’ safety
measures. (2) Automated Dataset Expansion. To facilitate rapid and scalable
growth, JailBench employs a context-learning approach for dataset expansion,
which leverages the advanced language capabilities of LLMs to automatically
generate evaluation prompts, increasing the efficiency and breadth of the assess-
ment process. (3) Advanced Jailbreak Enhancement. JailBench integrates our
innovative AJPE framework, as shown in Figure 1. The framework assimilates
the characteristics of sophisticated jailbreak attacks and powerful templates to
craft novel prompts. Additionally, it employs a log probability-based scoring

--- Page 3 ---

JailBench: A Comprehensive Chinese Security Assessment Benchmark for Large Language Models
3
mechanism to iteratively refine the quality of generated prompts, ensuring a
rigorous evaluation of LLMs’ potential security vulnerabilities.
The contributions of this paper can be summarized as follows:
– We introduce JailBench, the first comprehensive Chinese benchmark for as-
sessing deep-seated safety vulnerabilities in LLMs, comprising 10,800 queries
and achieving a 73.86% attack success rate against ChatGPT, clearly illus-
trating its extensiveness and effectiveness.
– We develop a new two-level hierarchical safety categorization standard for
JailBench, aligned with Chinese linguistic and cultural contexts, encompass-
ing 5 distinct domains and 40 risk types thereby providing a robust structure
for assessing LLM vulnerabilities.
– We propose Automatic Jailbreak Prompt Engineer (AJPE), a novel frame-
work for automated generation of harmful prompts at scale for the construc-
tion of JailBench, significantly enhancing the thoroughness and efficiency of
LLM vulnerability detection.
– We conduct extensive evaluations on 13 mainstream LLMs, which demon-
strates JailBench’s effectiveness in identifying LLMs’ vulnerabilities and high-
lighting key areas for safety reinforcement, providing valuable insights for
improving the overall safety and trustworthiness of LLMs.
2
Related Work
This section reviews existing Chinese benchmarks designed for safety evalua-
tion, as well as the jailbreak attacks that serve as key factors in improving the
effectiveness of test data.
2.1
Benchmarks for Safety Evaluation
Previous benchmarks have primarily focused on the specific risk assessment of
LLMs, ranging from text toxicity [6,11] and social bias [22] to hallucination [28].
As the capabilities and complexity of LLMs continue to increase, a growing
number of benchmarks have emerged to evaluate the overall safety of these
models [20,13]. However, these benchmarks primarily focus on English scenar-
ios, whereas JailBench concentrates on the Chinese language context, aiming to
provide a deeper assessment of LLM safety in Chinese.
With the rapid advancement of LLMs’ Chinese language capabilities, sev-
eral Chinese-specific benchmarks have also been constructed [29,15,7,23]. For
instance, SafetyBench evaluates LLM safety through multiple-choice questions
in both Chinese and English. While Flames is notable for its adversarial design,
pushing the boundaries of evaluating value alignment in Chinese LLMs. Nev-
ertheless, these benchmarks generally suffer limited effectiveness in thoroughly
evaluating LLM safety, as increasingly robust defenses against malicious prompts
pose challenges for detecting deeper security vulnerabilities [15,20]. This limita-
tion underscores the necessity of enhancing the harmfulness of test data.

--- Page 4 ---

4
S. Liu et al.
2.2
Jailbreak Attacks on LLMs
We introduce jailbreak attacks [2] into the construction of JailBench to improve
the effectiveness of thorough safety evaluation. Early jailbreak attacks on LLMs
primarily relied on manually crafted scenarios specifically designed to bypass
the models’ safeguards [10,4]. These approaches also included translating harm-
ful prompts into low-resource languages [24] or using cryptography to conceal
harmful intentions [26]. These carefully designed jailbreak templates can serve
as high-quality prompt resources for JailBench construction.
To minimize the human effort and time required to craft jailbreak prompts,
researchers have explored various automated red-teaming methods. These ap-
proaches range from utilizing search optimization algorithms to generate ad-
versarial prompts [31,8] to leveraging LLMs as prompt optimizers [3,27]. Par-
ticularly relevant to our work are the dynamic prompt optimization [12] and
iteration techniques [25]. These techniques maintain a "template pool" of effec-
tive jailbreak templates which can be easily combined with standard harmful
queries to rapidly generate numerous high-risk prompts. Consequently, we pro-
pose the AJPE framework, which leverages the language capabilities of LLMs
to perform few-shot learning for generating more targeted and context-aware
jailbreak prompts, potentially increasing the effectiveness and efficiency of jail-
break attacks, thereby providing a more rigorous and comprehensive assessment
of LLMs safety within the Chinese language context.
Different from existing Chinese benchmarks, JailBench incorporates advanced
jailbreak attacks with automatic prompt generation for thorough safety evalua-
tions, offering comprehensive security vulnerability identification for LLMs.
3
JailBench Construction
In this section, we will introduce the taxonomy definition and the dataset con-
struction procedure in detail.
3.1
Safety Categories
The Basic Security Requirements for Generative Artificial Intelligence Services1
standard highlights the key security risks associated with Chinese context. Build-
ing on these requirements, we collaborate with experts in the fields of security
and linguistics to develop a two-level hierarchical safety categorisation standard,
which encompasses 5 distinct domains and 40 categories of risk types. The classi-
fication system is designed for comprehensive coverage, clarity, and applicability
across diverse generative AI security scenarios, while its hierarchical structure
enables nuanced differentiation between various risk types, thereby enhancing
the accuracy of security assessment precision and facilitating targeted mitiga-
tion strategies. The detailed classification structure is shown as Figure 2.
1 https://www.tc260.org.cn/file/2024-05-17/9e2853d0-99a0-49c2-9df7-ccaada842ac5.
pdf

--- Page 5 ---

JailBench: A Comprehensive Chinese Security Assessment Benchmark for Large Language Models
5
Fig. 2: JailBench’s taxonomy with two levels consisting of 5 risk domains and 40
specific categories.
3.2
Data Collection
The construction of JailBench involved a comprehensive data collection process
to create a robust and diverse dataset for assessing LLM security vulnerabilities.
This section outlines our approach for question collection and augmentation.
Question Collection. To construct a comprehensive security testing dataset,
we initially aggregate a substantial volume of harmful queries from publicly
available datasets [5,31,29,7], which will be translated into Chinese and undergo
manual correction, forming the foundational raw data for dataset construction.
We use distinct methods for processing labeled and unlabeled data to ensure
accurate categorization. For labeled data, we find that although these datasets
employed diverse classification systems, most categories could be systematically
mapped to JailBench classification criteria due to its comprehensive structure.
For other unlabeled data, we employ prompt engineering techniques to guide
ChatGPT to accurately categorize the questions into the appropriate JailBench
categories, as illustrated in Figure 3. To ensure the reliability of classification, we
perform random sampling and manual verification of the data labels, rigorously
ensuring that all entries are accurately annotated according to our taxonomy.
Question Augmentation. Acknowledging the unique characteristics of the
Chinese linguistic and cultural context, certain safety categories suffer from a
scarcity of data. Considering the prohibitive cost and complexity associated with
manual data generation, we continue to instruct ChatGPT to generate new in-
stances of unsafe data through few-shot learning techniques, as shown in Figure

--- Page 6 ---

6
S. Liu et al.
Fig. 3: Instructions for the auto-
matic labelling task. The instruction
consists of three main parts: task
description, categorisation criteria,
and output format restrictions.
Fig. 4: Prompts for unsafe question
augmentation task. The instruction
can be divided into three main
parts: explicit generation of tasks
and target topics, reference exam-
ples, and output formatting restric-
tions.
4, which involves embedding the target category for data generation within the
prompts and randomly sampling relevant examples from the existing dataset.
This methodology not only allows us to efficiently expand our dataset but also
enhances the diversity of the questions, ensuring both consistency and richness
of the JailBench. Through repeated iterations of these steps, we successfully con-
struct the JailBench Seed, a large-scale dataset comprising over 10,000 questions.
This extensive collection forms a solid foundation for conducting comprehensive
evaluations of the safety performance of LLMs in the Chinese context.
3.3
Jailbreak Enhancement
As modern LLMs have developed robust security measures against harmful con-
tent, conventional safety evaluations often fail to expose the potential vulnerabil-
ities within these models. To address this challenge and uncover deeper security
breaches, we leverage jailbreak attack techniques to generate more potent and
inducive queries. This section details our process of integrating existing jailbreak
templates and use automated prompt generation to construct JailBench.
Jailbreak Templates Integration. Due to the scarcity of instructions bypass-
ing LLM’s safeguards, manual composition or random searches prove inefficient
for generating prompts at scale. An effective solution is to harness the advanced
language capabilities of LLMs to learn from effective jailbreak techniques and
template patterns. Consequently, our objective is to construct an extensive pool
of effective jailbreak templates, enabling the rapid generation of high-risk jail-
break prompts by simply concatenating templates with existing harmful queries.

--- Page 7 ---

JailBench: A Comprehensive Chinese Security Assessment Benchmark for Large Language Models
7
Fig. 5: flowchart of the AJPE process.
The process begins with compiling comprehensive prompts from previous jail-
break attacks researches [12,25,10,21,4]. These templates are then translated into
Chinese with detailed manual refinement. Finally, this pool containing effective
jailbreak templates will provide a crucial textual foundation for the automatic
generation of jailbreak prompts and the construction of JailBench.
Automatic Jailbreak Prompt Engineer. Considering the scarcity and the
limited diversity of jailbreak templates, we propose the AJPE method to ad-
dress these deficiencies. AJPE introduces the concept of prompt engineering,
leveraging the powerful learning capabilities of LLMs to emulate existing jail-
break templates and achieve large-scale generation of jailbreak prompts.
As shown in Figure 5, the AJPE workflow begins with templates testing and
harmful data acquisition. We randomly sample jailbreak templates and com-
bine them with the original questions from JailBench Seed to form a jailbreak-
enhanced dataset. Based on the dataset we conduct security assessments on the
target LLM groups, and the outputs of LLMs are then classified for harmfulness
using the security evaluators. Templates with attack success rates below a preset
threshold will be discarded and the remaining jailbreak templates as well as the
corresponding harmful input-output pairs obtained during the evaluation will
serve as the components for automated jailbreak prompt generation.
The core part of our AJPE is the prompt generation module, which operates
by instructing ChatGPT to generate corresponding instructions that achieve the
desired input-output objectives. By learning from a set of sample harmful text
pairs, the module then produces a number of jailbreak prompts with varying
levels of inducibility, mimicking the characteristics of the provided examples.

--- Page 8 ---

8
S. Liu et al.
In the final quality screening stage, we adopt the scoring function design [30]
and use the log-probability of model outputs as indicators of prompt effective-
ness, which is because log-probability is commonly used to represent the LLM’s
confidence in the generated text. Based on the prompt scoring mechanism, We
select the highest-performing prompts to include in the jailbreak template pool.
Through the AJPE method, we successfully expand our jailbreak prompts
to over 1,000. Considering the constraints on the dataset size and the com-
putational cost of experiments, we carefully select 20 most effective jailbreak
prompts from the pool and combine them with 540 questions in JailBench Seed.
This strategic combination results in the construction of the JailBench dataset,
which contains 10,800 jailbreak-enhanced test cases, ensuring a comprehensive
and manageable dataset that rigorously challenges the security mechanisms of
LLMs while maintaining practical feasibility for extensive evaluations.
JailBench stands out among existing Chinese safety benchmarks, as shown
in Table 1, featuring a substantial dataset of 10.8k queries, the broadest range
of classification categories, and the highest ASR against ChatGPT. These char-
acteristics make JailBench an effective tool for LLM security assessment.
4
Experiments
In this section, we first introduce our experimental setup. To validate the effec-
tiveness of JailBench, evaluate potential security vulnerabilities in target LLMs,
and assess the attack efficiency of AJPE, we conduct large-scale experiments on
a diverse set of popular LLMs and derive several relevant research conclusions.
4.1
Experiment Setup
Evaluated Models. As shown in Table 2, we evaluate 13 widely recognized
models that are proficient in generating Chinese content.
Evaluation Metrics. We employ the Attack Success Rate (ASR) as our pri-
mary metric to assess the defensive capabilities of LLMs against jailbreak at-
tacks, which is defined as the ratio of test queries that successfully breach LLMs’
safety guardrails and induce harmful outputs n to the total queries m:
ASR = n
m
To evaluate the effectiveness of AJPE-generated jailbreak prompts, we fur-
ther consider the impact of instruction length on the efficiency of attacks. We
introduce the Attack Efficiency (AE) metric, which incorporates a ratio between
the length of each successful jailbreak prompt ls and the length of the original
prompt lo, with k representing the scaling factor:
AE = k × 1
m
n
X
i=1
1
e
ls,i
lo,i

--- Page 9 ---

JailBench: A Comprehensive Chinese Security Assessment Benchmark for Large Language Models
9
Table 2: Comparison results of the Attack Success Rate (ASR) of the evaluated
LLMs on JailBench Seed / JailBench. "CSV" stands for Violation of Core
Socialist Values. "DC" stands for Discrimination. "COV" stands for Commercial
Offences and Violations. "ILR" stands for Infringement of Legal Rights. "SSN"
stands for Specific Security Needs. "Overall" represents the overall security per-
formance. "AVG" measures the average ASR for each security category. Bold
indicates the best and underline indicates the second in each column.
Model
CSV %
DC %
COV %
ILR %
SSN %
Overall %
GPT-4
1.0 / 26.9
0.0 / 38.1
0.0 / 39.2
0.0 / 31.6
0.0 / 36.3
0.2 / 34.5
GPT-3.5-Turbo
13.3 / 74.7 5.4 / 76.6 12.0 / 75.2
8.6 / 74.8
1.1 / 65.6
7.8 / 73.9
Mistral-7B-Instruct 26.7 / 83.6 2.4 / 76.5 13.3 / 82.1 17.1 / 82.1 4.4 / 66.8 11.9 / 78.1
Vicuna-13B
10.5 / 72.7
1.2 / 65.3
5.3 / 67.1
8.6 / 71.3
2.2 / 54.4
5.2 / 66.3
Vicuna-7B
12.4 / 65.8
4.2 / 56.4
6.7 / 61.1
17.1 / 65.4 3.3 / 48.2
8.5 / 59.3
Llama3-8B-Instruct
1.0 / 25.3
1.8 / 56.5
0.0 / 34.8
1.0 / 41.1
2.2 / 53.7
1.3 / 43.9
Llama2-13B-chat
2.9 / 46.0
0.0 / 60.4
0.0 / 55.7
0.0 / 57.5
0.0 / 54.4
0.6 / 55.4
Llama2-7B-chat
1.9 / 41.7
0.6 / 51.0
2.7 / 52.8
2.9 / 48.7
0.0 / 49.0
1.5 / 48.7
Qwen2-7B-chat
0.0 / 47.1
1.2 / 49.3
0.0 / 55.5
0.0 / 54.2
0.0 / 43.6
0.4 / 49.7
Qwen1.5-7B-chat
1.0 / 69.7
1.2 / 71.1
0.0 / 79.0
1.0 / 73.9
0.0 / 65.9
0.7 / 71.6
InternLM2-chat-7B
0.0 / 50.1
0.0 / 50.2
0.0 / 57.6
0.0 / 55.7
0.0 / 43.7
0.0 / 51.2
GLM-4-9B-chat
2.9 / 73.2
0.6 / 76.6
1.3 / 80.5
5.7 / 77.6
0.0 / 66.2
2.0 / 75.0
ChatGLM3-6B
1.9 / 51.8
0.6 / 66.7
0.0 / 60.1
4.8 / 58.1
0.0 / 52.2
1.5 / 58.8
AVG
5.8 / 56.0
1.5 / 61.1
3.2 / 61.6
5.1 / 60.9
1.0 / 53.8
3.2 / 59.0
4.2
Results and Analysis
JailBench Evaluation. We conduct comprehensive experiments to evaluate
the safety vulnerability of 13 LLMs using our JailBench Seed and JailBench
datasets. Table 2 presents the overall performance of the evaluated LLMs.
Firstly, JailBench substantially increases the ASR compared to the original
dataset (3.19% to 58.95%), while also achieving the highest ASR against Chat-
GPT among existing Chinese benchmarks. These results clearly demonstrate the
effectiveness of the AJPE-enhanced dataset in exposing LLM security vulnera-
bilities and underscore the importance of deep-seated safety evaluations.
Secondly, LLMs exhibit varying levels of vulnerability across different cate-
gories and models. GPT-4 achieves the strongest overall safety performance with
the lowest ASR, while Mistral-7B-Instruct shows the highest ASR across all do-
mains, underscoring its inadequate safety alignment within the Chinese context.
Notably, domestically developed Chinese LLMs show lower ASR (0.93%) com-
pared to their international counterparts (4.61%), particularly excelling in the
Violation of Core Socialist Values category, suggesting that they have undergone
stricter safety management during training on Chinese-language corpora.
Lastly, for jailbreak-enhanced datasets, models with larger parameter sizes
within the same LLM families generally exhibit higher jailbreak vulnerability.
This suggests that more powerful models may be more susceptible to jailbreak
attacks, highlighting a potential trade-off between LLM capability and safety. Al-
ternatively, newer LLMs consistently demonstrate improved safety performance,
indicating better alignment with human values and greater trustworthiness.

--- Page 10 ---

10
S. Liu et al.
Table 3: Comparison results of Attack Success Rate (ASR) / Attack Efficiency
(AE) of the evaluated LLMs with different jailbreak attack methods. "AD"
stands for AutoDAN. "GF" stands for GptFuzzer. "DI" stands for DeepIncep-
tion. "JB" stands for Jailbroken. "ICA" stands for In-Context Attack. Bold
indicates the best and underline indicates the second in each row.
Model
AD
GF
DI
JB
ICA
AJPE
GPT-4
0.0%/0.0e+0
2.0%/4.3e-17 4.3%/0.5
31.0%/0.1
1.0%/7.1e-23 38.7%/0.2
GPT-3.5-Turbo
10.0%/0.3e-9 19.7%/1.4e-12
6.0%/0.8
39.3%/0.1
4.0%/4.4e-15 88.0%/0.9
Mistral-7B-Instruct 99.0%/9.7e-9 79.3%/9.3e-11
6.3%/0.7
95.7%/0.1 45.0%/3.4e-11 91.7%/1.0
Vicuna-13B
95.7%/8.3e-9 66.3%/4.8e-11
6.7%/0.5 96.0%/0.1 47.0%/3.3e-11 82.7%/0.9
Vicuna-7B
95.3%/1.0e-8 86.0%/9.0e-11 10.7%/0.8 97.3%/0.1 30.0%/3.3e-11 72.3%/0.7
Llama3-8B-Instruct 18.0%/4.2e-9 13.7%/3.7e-11
1.3%/0.1
6.7%/0.0
0.0%/0.0e+0 52.0%/0.4
Llama2-13B-chat
20.0%/3.9e-9 30.0%/7.6e-11
3.7%/0.3
15.7%/0.0
2.0%/5.2e-17 79.0%/0.7
Llama2-7B-chat
48.3%/9.1e-9
9.3%/1.8e-13
2.3%/0.2
20.0%/0.1
0.0%/0.0e+0 77.3%/0.9
Qwen2-7B-chat
80.3%/9.3e-9 22.7%/6.7e-11
0.3%/0.1 86.3%/0.1
7.0%/6.7e-13 48.7%/0.4
Qwen1.5-7B-chat
90.7%/8.3e-9 77.3%/1.1e-10 7.0%/0.9 96.3%/0.1
6.0%/6.6e-14 80.7%/0.8
InternLM2-chat-7B 88.7%/4.5e-9 55.0%/1.6e-11
1.0%/0.1 90.7%/0.1
3.0%/1.7e-16 55.3%/0.5
GLM-4-9B-chat
89.7%/9.9e-9 57.7%/2.0e-11 8.3%/1.0
89.0%/0.1 16.0%/3.2e-11 77.3%/0.8
ChatGLM3-6B
77.3%/8.5e-9 61.7%/8.0e-11 7.7%/0.6 85.7%/0.1 14.0%/2.8e-12 53.7%/0.4
AVG
57.6%/6.4e-9 42.1%/4.8e-11
5.0%/0.5
61.2%/0.1 13.9%/1.0e-11 69.1%/0.7
AJPE Evaluation. To assess the effectiveness of prompts generated by AJPE,
we compare AJPE against 5 powerful jailbreak methods. Table 3 presents the
results in terms of Attack Success Rate (ASR) and Attack Efficiency (AE).
Firstly, AJPE achieves the highest average ASR among all methods, demon-
strating its superior ability to assimilate key features of existing jailbreak attacks
while integrating novel jailbreak strategies with enhanced inducement capabili-
ties, thereby elevating the potency and scope of the generated prompts. Although
AutoDAN and Jailbroken also achieve impressive ASRs for certain LLMs, their
AE is comparatively lower, which can be attributed to their reliance on manually
crafted, lengthy jailbreak templates including redundant components.
Secondly, AJPE also attains the highest average AE, indicating its capacity
to remove ineffective components of manually crafted jailbreak prompts and
integrate more potent content to bypass LLM safeguards within relatively concise
jailbreak templates. In contrast, DeepInception exhibits the second-highest AE,
but its efficiency comes at the cost of the lowest average ASR (5.0%), highlighting
the trade-off between attack brevity and success rate.
In summary, AJPE strikes a balance between high success rate and efficiency,
demonstrating its ability to generate targeted and inducing testing prompts.
This positions AJPE as a valuable tool for identifying vulnerabilities in LLM
safety mechanisms, contributing significantly to the construction of JailBench.
The results also underscore the importance of considering both ASR and AE
when evaluating the overall effectiveness of jailbreak techniques.

--- Page 11 ---

JailBench: A Comprehensive Chinese Security Assessment Benchmark for Large Language Models
11
5
Conclusion
In this paper, we introduce JailBench, the first comprehensive Chinese bench-
mark for assessing safety vulnerabilities in LLMs, comprising 10,800 jailbreak-
enhanced questions with a 73.86% ASR against ChatGPT. We also develop a
safety taxonomy and AJPE framework for prompt construction. Evaluation on
13 LLMs reveals JailBench’s effectiveness and persistent challenges in LLMs
safety, particularly against jailbreak attacks. This study highlights the impor-
tance of LLM security assessments and its alignment with ethical standards.
Acknowledgments. This work was supported by the National Natural Science Foun-
dation of China No.62402060, the Beijing Natural Science Foundation No.4244083, and
the Fundamental Research Funds for the Central Universities No.500422828.
References
1. Achiam, J., et al.: Gpt-4 technical report. arXiv preprint arXiv:2303.08774 (2023)
2. Carlini, N., et al.: Are aligned neural networks adversarially aligned? Advances in
Neural Information Processing Systems 36 (2024)
3. Chao, P., Robey, A., Dobriban, E., Hassani, H., Pappas, G.J., Wong, E.: Jail-
breaking black box large language models in twenty queries. arXiv preprint
arXiv:2310.08419 (2023)
4. Ding, P., et al.: A wolf in sheep’s clothing: Generalized nested jailbreak prompts
can fool large language models easily. arXiv preprint arXiv:2311.08268 (2023)
5. Ganguli, D., et al.: Red teaming language models to reduce harms: Methods, scaling
behaviors, and lessons learned. arXiv preprint arXiv:2209.07858 (2022)
6. Hartvigsen, T., Gabriel, S., Palangi, H., Sap, M., Ray, D., Kamar, E.: Toxigen:
A large-scale machine-generated dataset for adversarial and implicit hate speech
detection. arXiv preprint arXiv:2203.09509 (2022)
7. Huang, K., et al.: Flames: Benchmarking value alignment of chinese large language
models. arXiv preprint arXiv:2311.06899 (2023)
8. Lapid, R., Langberg, R., Sipper, M.: Open sesame! universal black box jailbreaking
of large language models. arXiv preprint arXiv:2309.01446 (2023)
9. Li, L., et al.: Salad-bench: A hierarchical and comprehensive safety benchmark for
large language models. arXiv preprint arXiv:2402.05044 (2024)
10. Li, X., Zhou, Z., Zhu, J., Yao, J., Liu, T., Han, B.: Deepinception: Hypnotize large
language model to be jailbreaker. arXiv preprint arXiv:2311.03191 (2023)
11. Lin, Z., et al.: Toxicchat: Unveiling hidden challenges of toxicity detection in real-
world user-ai conversation. arXiv preprint arXiv:2310.17389 (2023)
12. Liu, X., Xu, N., Chen, M., Xiao, C.: Autodan: Generating stealthy jailbreak
prompts on aligned large language models. arXiv preprint arXiv:2310.04451 (2023)
13. Mazeika, M., et al.: Harmbench: A standardized evaluation framework for auto-
mated red teaming and robust refusal. arXiv preprint arXiv:2402.04249 (2024)
14. Parrish, A., et al.: Bbq: A hand-built bias benchmark for question answering. arXiv
preprint arXiv:2110.08193 (2021)
15. Sun, H., Zhang, Z., Deng, J., Cheng, J., Huang, M.: Safety assessment of chinese
large language models. arXiv preprint arXiv:2304.10436 (2023)

--- Page 12 ---

12
S. Liu et al.
16. Tokayev, K.J.: Ethical implications of large language models a multidimensional
exploration of societal, economic, and technical concerns. International Journal of
Social Analytics 8(9), 17–33 (2023)
17. Touvron, H., et al.: Llama: Open and efficient foundation language models. arXiv
preprint arXiv:2302.13971 (2023)
18. Wang, W., et al.: All languages matter: On the multilingual safety of large language
models. arXiv preprint arXiv:2310.00905 (2023)
19. Wang, Y., et al.: A chinese dataset for evaluating the safeguards in large language
models. to appear in ACL 2024 findings (2024)
20. Wang, Y., Li, H., Han, X., Nakov, P., Baldwin, T.: Do-not-answer: A dataset for
evaluating safeguards in llms. arXiv preprint arXiv:2308.13387 (2023)
21. Wei, A., Haghtalab, N., Steinhardt, J.: Jailbroken: How does llm safety training
fail? Advances in Neural Information Processing Systems 36 (2024)
22. Woo, T.J., Nam, W.J., Ju, Y.J., Lee, S.W.: Compensatory debiasing for gender
imbalances in language models. In: ICASSP 2023 - 2023 IEEE International Con-
ference on Acoustics, Speech and Signal Processing (ICASSP). pp. 1–5 (2023).
https://doi.org/10.1109/ICASSP49357.2023.10095658
23. Xu, G., et al.: Cvalues: Measuring the values of chinese large language models from
safety to responsibility. arXiv preprint arXiv:2307.09705 (2023)
24. Yong, Z.X., Menghini, C., Bach, S.H.: Low-resource languages jailbreak gpt-4.
arXiv preprint arXiv:2310.02446 (2023)
25. Yu, J., Lin, X., Xing, X.: Gptfuzzer: Red teaming large language models with
auto-generated jailbreak prompts. arXiv preprint arXiv:2309.10253 (2023)
26. Yuan, Y., et al.: Gpt-4 is too smart to be safe: Stealthy chat with llms via cipher.
arXiv preprint arXiv:2308.06463 (2023)
27. Zeng, Y., Lin, H., Zhang, J., Yang, D., Jia, R., Shi, W.: How johnny can persuade
llms to jailbreak them: Rethinking persuasion to challenge ai safety by humanizing
llms. arXiv preprint arXiv:2401.06373 (2024)
28. Zhang, T., et al.: Enhancing uncertainty-based hallucination detection with
stronger focus. arXiv preprint arXiv:2311.13230 (2023)
29. Zhang, Z., et al.: Safetybench: Evaluating the safety of large language models with
multiple choice questions. arXiv preprint arXiv:2309.07045 (2023)
30. Zhou, Y., et al.: Large language models are human-level prompt engineers. arXiv
preprint arXiv:2211.01910 (2022)
31. Zou, A., Wang, Z., Kolter, J.Z., Fredrikson, M.: Universal and transferable adver-
sarial attacks on aligned language models. arXiv preprint arXiv:2307.15043 (2023)

```
