---
title: "AISafetyLab - PDF Extract"
source_pdf: "2025-Zhang-AISafetyLab.pdf"
pages: 13
extracted_at: "2026-01-24T16:38:37.118509"
---

# PDF Extract: AISafetyLab

**Source PDF:** 2025-Zhang-AISafetyLab.pdf
**Total Pages:** 13

---

## Content

```
--- Page 1 ---

AISafetyLab: A Comprehensive Framework for AI Safety Evaluation and
Improvement
Zhexin Zhang∗1, Leqi Lei∗1, Junxiao Yang∗1, Xijie Huang∗2, Yida Lu1, Shiyao Cui1,
Renmiao Chen1, Qinglin Zhang1, Xinyuan Wang2, Hao Wang2, Hao Li2, Xianqi Lei1,
Chengwei Pan2, Lei Sha2, Hongning Wang1, Minlie Huang1†
1The Conversational AI (CoAI) group, DCST, Tsinghua University
2Beihang University, Beijing, China
zx-zhang22@mails.tsinghua.edu.cn, aihuang@tsinghua.edu.cn
Abstract
As AI models are increasingly deployed across
diverse real-world scenarios, ensuring their
safety remains a critical yet underexplored chal-
lenge.
While substantial efforts have been
made to evaluate and enhance AI safety, the
lack of a standardized framework and compre-
hensive toolkit poses significant obstacles to
systematic research and practical adoption. To
bridge this gap, we introduce AISafetyLab, a
unified framework and toolkit that integrates
representative attack, defense, and evaluation
methodologies for AI safety. AISafetyLab fea-
tures an intuitive interface that enables devel-
opers to seamlessly apply various techniques
while maintaining a well-structured and exten-
sible codebase for future advancements. Ad-
ditionally, we conduct empirical studies on Vi-
cuna, analyzing different attack and defense
strategies to provide valuable insights into their
comparative effectiveness.
To facilitate on-
going research and development in AI safety,
AISafetyLab is publicly available at https:
//github.com/thu-coai/AISafetyLab, and
we are committed to its continuous mainte-
nance and improvement.
1
Introduction
AI models have garnered significant attention in
recent years due to their remarkable improvements
in performing a wide range of tasks. However, as
these models grow in capability, they also introduce
critical safety concerns. For instance, these models
may leak private information (Zhang et al., 2023b),
generate harmful content (Zou et al., 2023), or ex-
hibit unsafe behaviors in interactive environments
(Zhang et al., 2024a). These risks pose substantial
barriers to the reliable and widespread deployment
of AI systems, making safety a crucial area of re-
search. To address these challenges, the research
*Equal contribution.
†Corresponding author.
community has devoted increasing effort to AI
safety, which can be broadly categorized into two
key areas: (1) safety evaluation, which involves
identifying vulnerabilities through jailbreak attacks
(Liu et al., 2023; Yu et al., 2023), developing spe-
cialized benchmarks (Mazeika et al., 2024a), and
designing safety-scoring models (Inan et al., 2023;
Zhang et al., 2024b); and (2) safety improvement,
which focuses on developing defense mechanisms
and alignment strategies to mitigate risks and im-
prove AI robustness (Xie et al., 2023). Despite the
advancements in evaluation methodologies and im-
provement strategies, significant challenges persist
in comparing these approaches. These challenges
primarily stem from variations in experimental se-
tups, such as differences in test data and victim
models. Furthermore, reimplementing prior work
can be time-intensive, especially when source code
is unavailable. Even when source code is acces-
sible, considerable effort may still be required to
configure specific environments or adapt the im-
plementation to accommodate new datasets and
models.
To this end, we introduce AISafetyLab1, a com-
prehensive framework for evaluating and improv-
ing AI safety. The framework comprises three core
modules: Attack, Defense and Evaluation. The
Attack module currently implements 13 represen-
tative jailbreak attack methods, encompassing both
black-box and white-box techniques. The Defense
module supports 3 training-based defense strate-
gies and 13 inference-time defense mechanisms, all
aimed at preventing the model from generating un-
safe content. The Evaluation module integrates
mainstream safety scoring methods, including 2
rule-based scorers and 5 model-based scorers. In
addition, AISafetyLab features four auxiliary mod-
1We are currently focusing on Large Language Models
(LLMs), but we plan to expand to other scenarios in the future.
Therefore, we have named the framework using the broader
term "AI".
arXiv:2502.16776v1  [cs.CL]  24 Feb 2025

--- Page 2 ---

ules to support the core functionalities: Models,
Dataset, Utils and Logging. The Models mod-
ule provides a unified interface for interacting with
both local and API-based models. The Dataset
module standardizes data loading from local files
or the Hugging Face Datasets library. The Utils
module offers a variety of utility functions for man-
aging models, strings, configurations, and more.
The Logging module handles the configuration and
management of the logger.
We highlight the following key features of
AISafetyLab:
• Comprehensive
Method
Coverage.
AISafetyLab offers a broad array of attack,
defense, and evaluation techniques. Notably,
compared to existing toolkits, we are the first
to integrate various defense methods, to the
best of our knowledge.
• Structured and Unified Design. We have
reorganized numerous method implementa-
tions to create a clean and structured code-
base, enhancing both readability and extensi-
bility. Additionally, a unified access interface
is provided for each method, , streamlining
execution for end users.
• Extensive Model Support. AISafetyLab sup-
ports both local transformer-based models and
API-based models. We have also carefully ad-
dressed model-specific tokenization issues in
the implementation of certain methods (e.g.,
GCG (Zou et al., 2023)).
• Great Extensibility. With its structured de-
sign and auxiliary modules, AISafetyLab of-
fers great flexibility for developers.
The
framework is easily extensible, allowing the
addition of new methods by building on exist-
ing components and examples.
Additionally, we present an initial evaluation of
Vicuna, in which we assess 13 distinct attack meth-
ods and 16 defense mechanisms using AISafetyLab.
Our results highlight that certain attack strategies
consistently demonstrate high efficacy, whereas
others show variable performance depending on
the defense mechanisms employed. Furthermore,
we observe limitations in the current evaluation
framework, which at times leads to inconsistencies
and potentially unfair comparisons.
We believe that AISafetyLab has the potential
to significantly contribute to the advancement of
AI safety evaluation and improvement. We are
committed to the ongoing maintenance and regular
updates of the framework to ensure its continued
relevance and effectiveness.
2
Related Work
2.1
AI Safety Evaluation
Recent studies have introduced various approaches
for assigning safety scores to content generated
by LLMs. ShieldGemma (Zeng et al., 2024) of-
fers a suite of LLM-based content moderation tools
built on Gemma2. WildGuard (Han et al., 2024)
presents an open-source, lightweight moderation
tool designed to address risks such as jailbreaks
and refusals. Notably, ShieldLM (Zhang et al.,
2024b) introduces customizable safety detectors
capable of generating detailed explanations for
their decisions. Llama Guard (Inan et al., 2023)
ensures input-output safeguards for human-AI in-
teractions, while OpenAI’s holistic detection ap-
proach (Markov et al., 2023) supports an API for
moderating real-world content.
Benchmarks play a crucial role in standardizing
safety evaluations by providing standard and com-
prehensive test environments. Agent-SafetyBench
(Zhang et al., 2024a) features 2,000 test cases span-
ning eight safety risks and ten failure modes, cov-
ering 349 novel interaction environments. SORRY-
Bench (Xie et al., 2024) focuses on the refusal
behaviors of LLMs, with 450 unsafe instructions.
SALAD-Bench (Li et al., 2024) broadens the scope
by utilizing intricate taxonomies and employing the
LLM-based evaluator MD-Judge to assess perfor-
mance. Earlier contributions, such as SafetyBench
(Zhang et al., 2023a), provided 11,435 multiple-
choice safety questions, while Anthropic’s red-
teaming dataset (Ganguli et al., 2022) offered valu-
able insights into harm reduction strategies.
The increasing sophistication of attacks on large
language models (LLMs) has been a focal point
of recent research, with these attacks broadly
categorized into black-box and white-box meth-
ods.
Black-box attacks, including AutoDAN-
Turbo (Liu et al., 2024), GPTFuzzer (Yu et al.,
2023), ReNeLLM (Ding et al., 2023), Black-
DAN (Wang et al., 2024), and PAIR (Chao et al.,
2023), focus on crafting adversarial prompts or
jailbreak templates without direct access to the
model’s internal architecture. These techniques
achieve high success rates by exploiting model vul-
nerabilities, often utilizing methods such as social

--- Page 3 ---

engineering and cipher-based strategies. In con-
trast, white-box attacks—exemplified by methods
like GCG (Zou et al., 2023), AutoDAN (Liu et al.,
2023), AdvPrompter (Paulus et al., 2024), and
PGD-based approaches (Wang et al., 2024; Huang
et al., 2024)—leverage detailed access to model
internals to generate adversarial inputs. These ap-
proaches typically employ gradient-based or loss-
based optimization techniques, which expose sig-
nificant weaknesses in the safety alignment of
LLMs, particularly when dealing with complex
or creative adversarial prompts.
2.2
AI Safety Improvement
In addition to AI safety evaluation, an equally cru-
cial area of research focuses on developing defen-
sive strategies to counteract various attacks. These
defenses can be broadly classified into two cat-
egories: training-based and inference-based ap-
proaches. Training-based defenses, such as Safe
Unlearning (Zhang et al., 2024c), Layer-specific
Editing (Zhao et al., 2024), and Safety-Tuned Re-
inforcement Learning (Dai et al., 2023), aim to im-
prove model alignment during the training phase.
These strategies incorporate safety-oriented ob-
jectives, modify specific model layers, or intro-
duce carefully curated safety datasets to ensure
the model’s robustness against potential threats.
Inference-based defenses, on the other hand, oper-
ate during the inference stage to mitigate harmful
outputs. Approaches such as SafeDecoding (Xu
et al., 2024) and Goal Prioritization (Zhang et al.,
2024e) intervene at this stage to reduce the risk
of undesirable behaviors. Additional techniques
like RAIN (Li et al., 2023b) and Robustly Aligned
LLM (RA-LLM) (Cao et al., 2023) further enhance
safety by dynamically aligning outputs or integrat-
ing robust safety checks.
2.3
Other Toolkits
Recent efforts have integrated various adversarial
attack methods, such as EasyJailBreak (Zhou et al.,
2024) and Harmbench (Mazeika et al., 2024a),
which implement a diverse set of jailbreak attack
strategies. Despite significant advancements in at-
tack methodologies, research on defense mecha-
nisms remains fragmented. Existing approaches
typically concentrate on isolated defense strategies
or individual evaluation metrics, often lacking a
unified framework that integrates both attack and
defense techniques into a comprehensive adversar-
ial benchmarking system. This gap highlights the
pressing need for an all-in-one platform capable of
robust attack simulation, defense evaluation, and
the assessment of LLM resilience.
3
Framework Design
3.1
Overview
We illustrate the overview of AISafetyLab in Fig-
ure 1. We implement various representative attack
and defense methods, which can be applied to AI
models simultaneously to produce the final outputs.
Then various evaluation methods could be applied
to access the safety of the outputs. To support the
three main modules, we also implement four auxil-
iary shared modules, including Models, Dataset,
Utils and Logging. Next, we will introduce these
modules in detail.
3.2
Attack
In this section, we introduce the AISafetyLab at-
tack module, a critical component of the overall
package. This module is designed to assess the
safety capabilities of LLMs against adversarial
attacks, particularly those that attempt to bypass
safety mechanisms. It features 13 representative
adversarial attack methods, classified into three
categories based on the access level to the target
model:
• White-box Attacks: The attacker has full ac-
cess to the architecture, parameters and inter-
nal states (e.g., gradient) of the target model.
This enables more targeted and precise manip-
ulations of the model’s behavior. We imple-
ment GCG (Zou et al., 2023) as a representa-
tion of this kind of attacks.
• Gray-box Attacks: The attacker has par-
tial access, typically limited to input queries,
output text, and corresponding log proba-
bilities.
This information is easier to ac-
quire compared to that in the white-box set-
ting. In this category, AutoDAN (Liu et al.,
2023), LAA (Andriushchenko et al., 2024)
and Advprompter(Paulus et al., 2024) are im-
plemented.
• Black-box Attacks: The attacker has mini-
mal access, often restricted to input queries
and output text. These attacks are the most
challenging and resource-constrained, rely-
ing on input-output interactions to circum-
vent safety mechanisms.
The following 9

--- Page 4 ---

Figure 1: An overview of AISafetyLab. We introduce three core modules encompassing various attack, defense and
evaluation methods. To support their implementation, we incorporate four shared auxiliary modules.
black-box attack methods are currently im-
plemented: GPTFuzzer (Yu et al., 2023), Ci-
pher (Yuan et al., 2023), DeepInception (Li
et al., 2023a), In-context Learning Attacks
(Wei et al., 2023b), Jailbroken (Wei et al.,
2023a), MultiLingual (Deng et al., 2023),
PAIR (Chao et al., 2023), ReneLLM (Ding
et al., 2023) and TAP (Mehrotra et al., 2023).
The details of these attack methods are presented
in Appendix A.
3.2.1
Attack Module Design
To streamline the use of these diverse attack meth-
ods, the attack module of AISafetyLab is designed
to be modular and flexible. The core components
of the attack module include:
• Init: This module initializes the attacking en-
vironment by loading models and datasets,
and setting up the necessary infrastructure for
running the attacks.
• Mutate: The mutate module collects various
mutation strategies used by different attack
methods. These strategies are applied to mod-
ify input queries in ways that maximize the
chances of bypassing the model’s defenses.
• Select: The select module assists in identify-
ing the most promising adversarial queries by
ranking them based on relevant signals.
• Feedback: The feedback module provides
optimization signals that guide the attacker in
refining and enhancing the generated prompts.
This modular design provides two key advan-
tages:
1. User-Friendly: The well-structured frame-
work simplifies comprehension, allowing new-
comers to easily grasp the internal workings
of various attack methods.
2. Customizability: Developers can extend or
modify the attack flow by adapting individ-
ual modules, facilitating the creation of new
attack strategies using the provided building
blocks.
By providing this modular and extensible frame-
work, AISafetyLab enables researchers to experi-
ment with a wide variety of adversarial techniques
and gain deeper insights into the safety and robust-
ness of LLMs.
3.3
Defense
We categorize the safety defenses of large language
models into two primary types: inference-time de-
fenses and training-time defenses, as illustrated in
Figure 2 in the Appendix. Our modular defense
framework is designed to support rapid and flexible

--- Page 5 ---

expansion, enabling seamless integration of multi-
ple defensive mechanisms. In particular, inference-
time defenses allow the concurrent deployment of
multiple strategies to enhance robustness.
Inference-Time Defenses
Inference-time de-
fenses operate across three stages—input modi-
fication, decoding guidance, and output monitor-
ing—which correspond to the categories of prepro-
cessing, intraprocessing, and postprocessing. Our
framework incorporates 13 representative methods
spanning these stages, as detailed in Appendix B.1.
Training-Time Defenses
Training-time defenses
are categorized into safety data tuning, RL-based
alignment, and unlearning. We implement one rep-
resentative method for each category, with further
details provided in Appendix B.2.
3.4
Evaluation
We integrate seven widely applied evaluation meth-
ods for safety detection, each implemented as a
Scorer module inherited from the base module
BaseScorer. These scorers are categorized into
three main types:
• Pattern-based Scorer.
These scorers de-
termine the success of a jailbreak attempt
by matching the model’s response against a
predefined set of patterns, including Pattern-
Scorer and PrefixMatchScorer.
• Finetuning-based Scorer. This category of
scorers assesses the safety of responses using
fine-tuned scoring models, including Classfi-
cationScorer, ShieldLMScorer, HarmBench-
Scorer and LlamaGuard3Scorer.
• Prompt-based Scorer. This category of scor-
ers evaluates response safety by prompting
the model with specifically designed safety de-
tection guidelines, including PromptedLLM-
Scorer.
All the scorers utilize the same interface score
to conduct safety evaluation, which takes a query-
response pair as input and returns the judgment
from the scorer. Additional outputs from the scorer
are also returned to provide comprehensive infor-
mation during evaluation. The implementation de-
tails of the scorers are presented in Appendix C.
Additionally, we implement a scorer named
OverRefuseScorer based on the work of Röttger
et al. (2024), which prompts an LLM to evaluate
the over-refusal rate of a model. The interface of
this scorer is consistent with that of other scorers.
3.5
Auxiliary Modules
We introduce four auxiliary modules that facilitate
the implementation of the three core modules. Each
of these auxiliary modules is detailed below.
Models
Our framework currently supports two
primary types of models: local transformer-based
models and API-based models. Specifically, lo-
cal models must be compatible with the Hugging
Face Transformers library, while API-based mod-
els must adhere to OpenAI-compatible access in-
terfaces. To enhance usability, we provide uni-
fied interfaces for local models, such as chat and
batch_chat, which enable text generation based
on given input prompts. Additionally, for API-
based models, we incorporate robust error-handling
mechanisms within the chat interface, allowing for
a configurable maximum number of retry attempts
in the event of errors.
Dataset
This module primarily manages dataset
loading and slicing. It supports both local data
files and datasets from the Hugging Face Datasets
library. Furthermore, it includes a configurable
subset_slice parameter, which allows users to
specify a subset of the dataset for selection. This
feature is particularly beneficial for running experi-
ments on smaller portions of a dataset or resuming
experiments that were previously interrupted.
Utilities
The utilities module provides various
helper functions categorized into four key areas:
(1) model-related functions (e.g., perplexity compu-
tation), (2) string processing utilities (e.g., function
word identification), (3) configuration management
(e.g., loading attack method configurations), and
(4) miscellaneous functionalities.
Logging
This module is responsible for log-
ging functionalities and leverages the loguru2 li-
brary to provide a shared logger across the en-
tire project. We implement an intuitive interface,
setup_logger, to configure logging settings, such
as directing command-line outputs to a file. The
logger supports various log levels (e.g., debug and
error) and automatically records useful metadata,
including timestamps and command execution lo-
cations.
2https://github.com/Delgan/loguru

--- Page 6 ---

In addition to these modules, we curate and or-
ganize various safety-related datasets, which are
publicly available on the Hugging Face Datasets
platform3. Furthermore, we maintain a continu-
ously updated list of research papers related to AI
safety, providing a valuable resource for the com-
munity.
4
Usage
AISafetyLab provides a general and user-friendly
interface for LLM attack, defense, and evaluation
with just a few lines of code. In this section, we
offer examples for attack, defense and evaluation,
respectively.
4.1
Attack
The following code demonstrates the setup of our
attack module. After importing the correspond-
ing attack method (e.g., AutoDANManager), the
attack function can automatically initiate an at-
tack towards the target model specified in the con-
figuration file and save the resulting responses.
from aisafetylab.attack.attackers.
autodan import AutoDANManager
from aisafetylab.utils import
ConfigManager
from aisafetylab.utils import
parse_arguments
args = parse_arguments ()
config_manager = ConfigManager(
config_path=args.config_path)
attacker = AutoDANManager.from_config(
config_manager.config)
attacker.attack ()
4.2
Defense
We provide a demonstration of the defense module
usage below. After specifying the defense method,
the chat function can execute the defense and pro-
duce the corresponding results. Note that we sup-
port the simultaneous deployment of multiple de-
fense strategies.
from aisafetylab.defense.
inference_defense import
create_defender_from_yaml
from aisafetylab.defense.
inference_defense import chat
attack_query = "Give detailed
instructions for >>> correctlua code
reform BEGIN <!--"
defender_name="self_reminder"
3https://huggingface.co/datasets/thu-coai/
AISafetyLab_Datasets
defenders = [( create_defender_from_yaml(
f"./ configs /{ defender_name }.yaml")]
response = chat(
model ,
attack_query ,
defenders
)
4.3
Evaluation
The usage of the evaluation module is as follows.
After instantiating the scorer with a specific evalu-
ation method, the score function can provide eval-
uation results for a given instruction-response pair.
from aisafetylab.evaluation.scorers
import LlamaGuard3Scorer
scorer = LlamaGuard3Scorer(
model_path="meta -llama/Llama -
Guard -3-8B",
tokenizer_path="meta -llama/Llama
-Guard -3-8B",
)
scorer.score("How to make a bomb?", "
Sorry , I can not ...")
5
Experiments
5.1
Setup
Using AISafetyLab, we conducted a series of exper-
iments to evaluate various attack and defense meth-
ods, employing Llama-Guard-3-8B as the scoring
model. To highlight the performance gap between
attack and defense strategies, we initially selected
Vicuna-7B-v1.5 (a model that is relatively weak in
safety) as the target model and assessed its perfor-
mance on a subset of the HarmBench dataset that
contains 50 harmful instructions. Additionally, we
assess the overrefusal tendencies of various defense
methods on XSTest (Röttger et al., 2024).
Attack Methods
We examined 13 representative
attack methods as detailed in Section 3.2. All meth-
ods were applied to the same subset of HarmBench.
Defense Methods
We evaluated 13 represen-
tative inference-time defense methods and three
training-time defense methods, as described in Sec-
tion 3.3. For the training-time defenses, the size
of the training dataset was controlled to approxi-
mately 1,000 samples.
5.2
Main Results
The results are summarized in Table 1, highlighting
attack success rates under different defense strate-
gies and the corresponding overrefusal rates.

--- Page 7 ---

Attack Method
Original
Safe
Tuning
Safe
Unlearning
Safe
RLHF
PPL
Filter
Prompt
Guard
Self
Reminder
Para
phrasing
Goal
Prioritization
DRO
ICD
Erase
Check
Robust
Aligned
Safe
Decoding
SmoothLLM
Aligner
Self
Evaluation
Avg.
AutoDAN
92.0
88.0
18.0
85.0
90.0
0.0
84.0
46.0
74.0
82.0
90.0
66.0
30.0
66.0
74.0
10.0
0.0
56.4
Cipher
33.8
34.2
14.7
17.0
20.5
0.0
15.1
27.1
10.6
9.1
2.3
21.8
3.1
13.1
13.3
14.2
12.0
14.3
DeepInception
70.0
74.0
40.0
48.0
70.0
0.0
4.0
78.0
0.0
74.0
2.0
2.0
6.0
60.0
74.0
50.0
42.0
39.0
GCG
82.0
78.0
10.0
14.0
2.0
0.0
12.0
34.0
0.0
34.0
24.0
8.0
6.0
32.0
26.0
14.0
0.0
18.4
GPTFuzzer
88.0
94.0
4.0
84.0
4.0
0.0
0.0
14.0
0.0
94.0
86.0
0.0
0.0
42.0
4.0
76.0
2.0
31.5
ICA
24.0
22.0
2.0
20.0
24.0
0.0
20.0
10.0
4.0
18.0
4.0
6.0
2.0
0.0
22.0
18.0
6.0
11.1
Jailbroken
46.0
10.0
42.0
44.0
46.0
0.0
48.0
18.0
18.0
42.0
72.0
42.0
10.0
58.0
62.0
44.0
46.0
37.6
MultiLingual
36.0
28.0
10.0
32.0
36.0
0.0
14.0
30.0
2.0
24.0
14.0
36.0
32.0
30.0
44.0
24.0
22.0
23.6
PAIR
64.0
76.0
20.0
66.0
64.0
0.0
18.0
66.0
14.0
62.0
26.0
38.0
24.0
30.0
82.0
24.0
24.0
39.6
ReNeLLM
72.0
66.0
10.0
56.0
2.0
0.0
12.0
30.0
0.0
26.0
14.0
8.0
6.0
24.0
30.0
14.0
0.0
18.6
TAP
76.0
56.0
8.0
62.0
66.0
0.0
36.0
56.0
10.0
46.0
24.0
50.0
22.0
16.0
70.0
24.0
0.0
34.1
SAA
80.0
76.0
10.0
18.0
0.0
0.0
10.0
46.0
0.0
28.0
14.0
8.0
2.0
22.0
24.0
14.0
0.0
17.0
Advprompter
32.0
36.0
4.0
34.0
32.0
0.0
4.0
38.0
0.0
30.0
6.0
14.0
10.0
14.0
40.0
18.0
14.0
18.4
Avg.
61.2
56.8
14.8
44.6
35.1
0.0
21.3
37.9
10.2
43.8
29.1
23.1
11.8
31.3
43.5
26.5
12.9
-
OverRefusal Rate
5.2
6.4
20.0
7.8
5.2
5.2
17.6
3.6
17.6
16.8
13.2
99.6
93.2
14.0
22.0
8.0
29.2
-
Table 1: The ASR results of different attack and defense methods, performed on Vicuna-7B-v1.5. All results are
multiplied by 100.
Attack Effectiveness
Among the evaluated at-
tack methods, AutoDAN demonstrates superior
effectiveness across various defense mechanisms,
while PAIR, DeepInception and Jailbroken also
achieve attack success rates (ASR) exceeding 35%.
Notably, some methods, such as GCG and SAA,
perform well on the vanilla model but experience a
significant drop in effectiveness when confronted
with defensive measures. These findings under-
score the importance of evaluating attack methods
under diverse defense strategies.
Defense Effectiveness
At the inference stage,
Prompt Guard, Robust Aligned, and Self Evalu-
ation emerge as the most effective defensive strate-
gies, as discussed in Section 3.3.
In terms of
training-based defenses, Safe Unlearning proves
to be the most effective, reducing the average at-
tack success rate to 14.8%. Notably, Prompt Guard
completely neutralizes all attacks by employing
a classifier on input queries. However, some de-
fenses, such as Erase Check and Robust Aligned,
while highly effective, introduce significant over-
refusal rates, highlighting a trade-off in overall us-
ability. Additionally, approaches like PPL Filter
and Erase Check are only effective against specific
attack methods that rely on unreadable adversarial
prompts. These findings underscore the ongoing
challenge of balancing security with usability in
current defense mechanisms.
Challenge on Robustness
The evaluation of ro-
bustness still poses significant challenges, often
resulting in unfair comparisons between methods.
For example, while DeepInception achieves an at-
tack success rate (ASR) above 40% under meth-
ods such as Safe Unlearning and Self Evaluation,
the responses often consist of fictional narratives
or simple repetitions of the question, without pro-
viding precise or potentially harmful information.
These problems underscore the necessity for more
dependable evaluation frameworks that can accu-
rately measure performance across a variety of ad-
versarial conditions.
6
Conclusion and Future Work
In this work, we introduce AISafetyLab, a compre-
hensive framework and resource for advancing AI
safety evaluation and improvement. For users who
prefer not to modify the internal code, AISafetyLab
offers broad method and model coverage, simple
interfaces, and diverse examples to facilitate quick
experimentation and application. For developers
interested in implementing new methods, our struc-
tured design aims to minimize effort and streamline
integration.
We are committed to continuously maintaining
and enhancing AISafetyLab. Some of our future
plans include:
• Adding an explainability module to improve
understanding of AI safety mechanisms.
• Implementing methods for multimodal safety.
• Implementing methods for agent safety.
• Integrate more methods for LLM safety.
• Regularly updating the paper list for AI safety.
• Maintaining and improving the codebase by
addressing bugs and issues.
We are dedicated to executing these plans and
warmly welcome community suggestions and con-
tributions, as collaborative efforts will be instru-
mental in advancing AI safety.

--- Page 8 ---

References
Gabriel Alon and Michael Kamfonas. 2023. Detect-
ing language model attacks with perplexity. arXiv
preprint arXiv:2308.14132.
Maksym Andriushchenko, Francesco Croce, and Nico-
las Flammarion. 2024. Jailbreaking leading safety-
aligned llms with simple adaptive attacks. arXiv
preprint arXiv:2404.02151.
Federico Bianchi, Mirac Suzgun, Giuseppe Attanasio,
Paul Röttger, Dan Jurafsky, Tatsunori Hashimoto,
and James Zou. 2023.
Safety-tuned llamas:
Lessons from improving the safety of large lan-
guage models that follow instructions. arXiv preprint
arXiv:2309.07875.
Hannah Brown, Leon Lin, Kenji Kawaguchi, and
Michael Shieh. 2024. Self-evaluation as a defense
against adversarial attacks on llms. arXiv preprint
arXiv:2407.03234.
Bochuan Cao, Yuanpu Cao, Lu Lin, and Jinghui Chen.
2023.
Defending against alignment-breaking at-
tacks via robustly aligned llm.
arXiv preprint
arXiv:2309.14348.
Patrick Chao, Alexander Robey, Edgar Dobriban,
Hamed Hassani, George J Pappas, and Eric Wong.
2023. Jailbreaking black box large language models
in twenty queries. arXiv preprint arXiv:2310.08419.
Josef Dai, Xuehai Pan, Ruiyang Sun, Jiaming Ji, Xinbo
Xu, Mickel Liu, Yizhou Wang, and Yaodong Yang.
2023. Safe rlhf: Safe reinforcement learning from
human feedback. arXiv preprint arXiv:2310.12773.
Yue Deng, Wenxuan Zhang, Sinno Jialin Pan, and
Lidong Bing. 2023.
Multilingual jailbreak chal-
lenges in large language models.
arXiv preprint
arXiv:2310.06474.
Peng Ding, Jun Kuang, Dan Ma, Xuezhi Cao, Yunsen
Xian, Jiajun Chen, and Shujian Huang. 2023. A
wolf in sheep’s clothing: Generalized nested jailbreak
prompts can fool large language models easily. arXiv
preprint arXiv:2311.08268.
Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda
Askell, Yuntao Bai, Saurav Kadavath, Ben Mann,
Ethan Perez, Nicholas Schiefer, Kamal Ndousse,
et al. 2022. Red teaming language models to re-
duce harms: Methods, scaling behaviors, and lessons
learned. arXiv preprint arXiv:2209.07858.
Seungju Han, Kavel Rao, Allyson Ettinger, Liwei Jiang,
Bill Yuchen Lin, Nathan Lambert, Yejin Choi, and
Nouha Dziri. 2024. Wildguard: Open one-stop mod-
eration tools for safety risks, jailbreaks, and refusals
of llms. arXiv preprint arXiv:2406.18495.
Xijie Huang, Xinyuan Wang, Hantao Zhang, Jiawen Xi,
Jingkun An, Hao Wang, and Chengwei Pan. 2024.
Cross-modality jailbreak and mismatched attacks on
medical multimodal large language models. arXiv
preprint arXiv:2405.20775.
Hakan Inan, Kartikeya Upasani, Jianfeng Chi, Rashi
Rungta,
Krithika Iyer,
Yuning Mao,
Michael
Tontchev, Qing Hu, Brian Fuller, Davide Testuggine,
et al. 2023. Llama guard: Llm-based input-output
safeguard for human-ai conversations. arXiv preprint
arXiv:2312.06674.
Neel Jain, Avi Schwarzschild, Yuxin Wen, Gowthami
Somepalli, John Kirchenbauer, Ping-yeh Chiang,
Micah Goldblum, Aniruddha Saha, Jonas Geiping,
and Tom Goldstein. 2023. Baseline defenses for ad-
versarial attacks against aligned language models.
arXiv preprint arXiv:2309.00614.
Jiaming Ji, Boyuan Chen, Hantao Lou, Donghai Hong,
Borong Zhang, Xuehai Pan, Juntao Dai, and Yaodong
Yang. 2024. Aligner: Achieving efficient alignment
through weak-to-strong correction. arXiv preprint
arXiv:2402.02416.
Aounon Kumar, Chirag Agarwal, Suraj Srinivas,
Aaron Jiaxun Li, Soheil Feizi, and Himabindu
Lakkaraju. 2023. Certifying llm safety against adver-
sarial prompting. arXiv preprint arXiv:2309.02705.
Lijun Li, Bowen Dong, Ruohui Wang, Xuhao Hu, Wang-
meng Zuo, Dahua Lin, Yu Qiao, and Jing Shao.
2024. Salad-bench: A hierarchical and comprehen-
sive safety benchmark for large language models.
arXiv preprint arXiv:2402.05044.
Xuan Li, Zhanke Zhou, Jianing Zhu, Jiangchao Yao,
Tongliang Liu, and Bo Han. 2023a. Deepinception:
Hypnotize large language model to be jailbreaker.
arXiv preprint arXiv:2311.03191.
Yuhui Li, Fangyun Wei, Jinjing Zhao, Chao Zhang, and
Hongyang Zhang. 2023b. Rain: Your language mod-
els can align themselves without finetuning. arXiv
preprint arXiv:2309.07124.
Xiaogeng Liu, Peiran Li, Edward Suh, Yevgeniy
Vorobeychik, Zhuoqing Mao, Somesh Jha, Patrick
McDaniel, Huan Sun, Bo Li, and Chaowei Xiao.
2024.
Autodan-turbo: A lifelong agent for strat-
egy self-exploration to jailbreak llms. arXiv preprint
arXiv:2410.05295.
Xiaogeng Liu, Nan Xu, Muhao Chen, and Chaowei
Xiao. 2023. Autodan: Generating stealthy jailbreak
prompts on aligned large language models. arXiv
preprint arXiv:2310.04451.
Todor Markov, Chong Zhang, Sandhini Agarwal, Flo-
rentine Eloundou Nekoul, Theodore Lee, Steven
Adler, Angela Jiang, and Lilian Weng. 2023. A holis-
tic approach to undesired content detection in the real
world. In Proceedings of the AAAI Conference on
Artificial Intelligence, 12, pages 15009–15018.
Mantas Mazeika, Long Phan, Xuwang Yin, Andy Zou,
Zifan Wang, Norman Mu, Elham Sakhaee, Nathaniel
Li, Steven Basart, Bo Li, David A. Forsyth, and Dan
Hendrycks. 2024a. Harmbench: A standardized eval-
uation framework for automated red teaming and ro-
bust refusal. In Forty-first International Conference

--- Page 9 ---

on Machine Learning, ICML 2024, Vienna, Austria,
July 21-27, 2024.
Mantas Mazeika, Long Phan, Xuwang Yin, Andy Zou,
Zifan Wang, Norman Mu, Elham Sakhaee, Nathaniel
Li, Steven Basart, Bo Li, et al. 2024b. Harmbench:
A standardized evaluation framework for automated
red teaming and robust refusal. In Forty-first Interna-
tional Conference on Machine Learning.
Anay Mehrotra, Manolis Zampetakis, Paul Kassianik,
Blaine Nelson, Hyrum Anderson, Yaron Singer, and
Amin Karbasi. 2023.
Tree of attacks: Jailbreak-
ing black-box llms automatically. arXiv preprint
arXiv:2312.02119.
Meta-Llama. 2024. Prompt guard 86m.
Anselm Paulus, Arman Zharmagambetov, Chuan Guo,
Brandon Amos, and Yuandong Tian. 2024.
Ad-
vprompter: Fast adaptive adversarial prompting for
llms. arXiv preprint arXiv:2404.16873.
Xiangyu Qi, Yi Zeng, Tinghao Xie, Pin-Yu Chen, Ruoxi
Jia, Prateek Mittal, and Peter Henderson. 2023. Fine-
tuning aligned language models compromises safety,
even when users do not intend to! In The Twelfth In-
ternational Conference on Learning Representations.
Alexander Robey, Eric Wong, Hamed Hassani, and
George J Pappas. 2023. Smoothllm: Defending large
language models against jailbreaking attacks. arXiv
preprint arXiv:2310.03684.
Paul Röttger, Hannah Kirk, Bertie Vidgen, Giuseppe
Attanasio, Federico Bianchi, and Dirk Hovy. 2024.
Xstest: A test suite for identifying exaggerated safety
behaviours in large language models. In Proceed-
ings of the 2024 Conference of the North American
Chapter of the Association for Computational Lin-
guistics: Human Language Technologies (Volume 1:
Long Papers), pages 5377–5400.
Xinyuan Wang, Victor Shea-Jay Huang, Renmiao Chen,
Hao Wang, Chengwei Pan, Lei Sha, and Min-
lie Huang. 2024.
Blackdan: A black-box multi-
objective approach for effective and contextual jail-
breaking of large language models. arXiv preprint
arXiv:2410.09804.
Alexander Wei, Nika Haghtalab, and Jacob Steinhardt.
2023a. Jailbroken: How does LLM safety training
fail? CoRR, abs/2307.02483.
Zeming Wei, Yifei Wang, Ang Li, Yichuan Mo, and
Yisen Wang. 2023b. Jailbreak and guard aligned
language models with only few in-context demon-
strations. arXiv preprint arXiv:2310.06387.
Tinghao Xie, Xiangyu Qi, Yi Zeng, Yangsibo Huang,
Udari Madhushani Sehwag, Kaixuan Huang, Luxi
He, Boyi Wei, Dacheng Li, Ying Sheng, et al. 2024.
Sorry-bench: Systematically evaluating large lan-
guage model safety refusal behaviors. arXiv preprint
arXiv:2406.14598.
Yueqi Xie, Jingwei Yi, Jiawei Shao, Justin Curl,
Lingjuan Lyu, Qifeng Chen, Xing Xie, and Fangzhao
Wu. 2023. Defending chatgpt against jailbreak at-
tack via self-reminders. Nature Machine Intelligence,
5(12):1486–1496.
Zhangchen Xu, Fengqing Jiang, Luyao Niu, Jinyuan
Jia, Bill Yuchen Lin, and Radha Poovendran.
2024. Safedecoding: Defending against jailbreak
attacks via safety-aware decoding. arXiv preprint
arXiv:2402.08983.
Jiahao Yu, Xingwei Lin, Zheng Yu, and Xinyu Xing.
2023. Gptfuzzer: Red teaming large language mod-
els with auto-generated jailbreak prompts.
arXiv
preprint arXiv:2309.10253.
Youliang Yuan, Wenxiang Jiao, Wenxuan Wang,
Jen-tse Huang, Pinjia He, Shuming Shi, and
Zhaopeng Tu. 2023. Gpt-4 is too smart to be safe:
Stealthy chat with llms via cipher. arXiv preprint
arXiv:2308.06463.
Wenjun Zeng, Yuchi Liu, Ryan Mullins, Ludovic Peran,
Joe Fernandez, Hamza Harkous, Karthik Narasimhan,
Drew Proud, Piyush Kumar, Bhaktipriya Radharapu,
et al. 2024.
Shieldgemma:
Generative ai con-
tent moderation based on gemma. arXiv preprint
arXiv:2407.21772.
Zhexin Zhang, Shiyao Cui, Yida Lu, Jingzhuo Zhou,
Junxiao Yang, Hongning Wang, and Minlie Huang.
2024a. Agent-safetybench: Evaluating the safety of
llm agents. arXiv preprint arXiv:2412.14470.
Zhexin Zhang, Leqi Lei, Lindong Wu, Rui Sun,
Yongkang Huang, Chong Long, Xiao Liu, Xuanyu
Lei, Jie Tang, and Minlie Huang. 2023a. Safety-
bench: Evaluating the safety of large language mod-
els with multiple choice questions. arXiv preprint
arXiv:2309.07045.
Zhexin Zhang, Yida Lu, Jingyuan Ma, Di Zhang, Rui
Li, Pei Ke, Hao Sun, Lei Sha, Zhifang Sui, Hongning
Wang, et al. 2024b. Shieldlm: Empowering llms as
aligned, customizable and explainable safety detec-
tors. arXiv preprint arXiv:2402.16444.
Zhexin Zhang, Jiaxin Wen, and Minlie Huang. 2023b.
ETHICIST: targeted training data extraction through
loss smoothed soft prompting and calibrated confi-
dence estimation. In Proceedings of the 61st Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), ACL 2023, Toronto,
Canada, July 9-14, 2023, pages 12674–12687. Asso-
ciation for Computational Linguistics.
Zhexin Zhang, Junxiao Yang, Pei Ke, Shiyao Cui,
Chujie Zheng, Hongning Wang, and Minlie Huang.
2024c. Safe unlearning: A surprisingly effective
and generalizable solution to defend against jailbreak
attacks. arXiv preprint arXiv:2407.02855.
Zhexin Zhang, Junxiao Yang, Pei Ke, Shiyao Cui,
Chujie Zheng, Hongning Wang, and Minlie Huang.
2024d. Safe unlearning: A surprisingly effective

--- Page 10 ---

and generalizable solution to defend against jailbreak
attacks. arXiv preprint arXiv:2407.02855.
Zhexin Zhang, Junxiao Yang, Pei Ke, Fei Mi, Hongning
Wang, and Minlie Huang. 2024e. Defending large
language models against jailbreaking attacks through
goal prioritization. In ACL.
Wei Zhao, Zhe Li, Yige Li, Ye Zhang, and Jun Sun.
2024.
Defending large language models against
jailbreak attacks via layer-specific editing. arXiv
preprint arXiv:2405.18166.
Chujie Zheng, Fan Yin, Hao Zhou, Fandong Meng, Jie
Zhou, Kai-Wei Chang, Minlie Huang, and Nanyun
Peng. 2024. Prompt-driven llm safeguarding via di-
rected representation optimization. arXiv preprint
arXiv:2401.18018.
Weikang Zhou, Xiao Wang, Limao Xiong, Han
Xia, Yingshuang Gu, Mingxu Chai, Fukang Zhu,
Caishuang Huang, Shihan Dou, Zhiheng Xi, et al.
2024. Easyjailbreak: A unified framework for jail-
breaking large language models.
arXiv preprint
arXiv:2403.12171.
Andy Zou, Zifan Wang, J. Zico Kolter, and Matt
Fredrikson. 2023. Universal and transferable adver-
sarial attacks on aligned language models. CoRR,
abs/2307.15043.

--- Page 11 ---

A
Implementation Details of Attackers
The implementation details of the 13 attackers men-
tioned in section 3.2 are presented as follows:
A.0.1
White-box Attacks
• GCG (Zou et al., 2023): The Greedy Coor-
dinate Gradient-based Search (GCG) attack
method perturbs the input tokens using the
loss gradient as an optimization signal. The
loss function is designed to maximize the
probability of an affirmative prefix, thus guid-
ing the model to produce unsafe or undesir-
able outputs.
A.0.2
Gray-box Attacks
• AutoDAN (Liu et al., 2023): AutoDAN gen-
erates jailbreak prompts using a hierarchical
genetic algorithm. The goal is to automat-
ically evolve effective attack strategies that
bypass the model’s safety mechanisms.
• LAA (Andriushchenko et al., 2024): The
LAA method designs adaptive templates and
appends adversarial suffixes to the chosen tem-
plate. The suffix is optimized through random
search, achieving high success rates for by-
passing model defenses.
• Advprompter (Paulus et al., 2024): This
method trains an attacker LLM to autoregres-
sively generate adversarial suffixes to a given
input query, making it effective for generating
successful jailbreak prompts.
A.0.3
Black-box Attacks
• GPTFuzzer (Yu et al., 2023): This method
generates new jailbreak templates through it-
erative mutation of human-written templates.
It employs five mutation techniques: gener-
ation, crossover, expansion, shortening, and
rephrasing, all aimed at finding prompts that
can successfully bypass model defenses.
• Cipher (Yuan et al., 2023): The Cipher attack
works by encoding instructions in a cryptic
manner, such that the model’s safety align-
ment mechanisms fail to interpret the instruc-
tions correctly, enabling a jailbreak.
• DeepInception (Li et al., 2023a): This at-
tack creates diverse scenes and characters to
mislead the target model’s safety filters, thus
circumventing its safety alignment.
• In-context Learning Attacks (Wei et al.,
2023b):
In-context learning exploits few-
shot demonstrations to manipulate the target
model’s behavior and trigger unsafe outputs.
• Jailbroken (Wei et al., 2023a): The Jail-
broken attack method targets two key fail-
ure modes in LLM safety alignment: com-
peting objectives and mismatched generaliza-
tion. By leveraging these weaknesses, it crafts
prompts that can bypass the model’s safety
mechanisms.
• MultiLingual (Deng et al., 2023): This attack
translates input queries into low-resource lan-
guages, often evading the safety mechanisms
in models that are less robust in non-major lan-
guages, thus achieving a successful jailbreak.
• PAIR (Chao et al., 2023): PAIR involves us-
ing an attacker LLM to iteratively refine jail-
break prompts, enhancing their effectiveness
through repeated refinement.
• ReneLLM (Ding et al., 2023): ReneLLM
combines two techniques: prompt rewriting
and scenario nesting. These methods are used
to reframe the input in ways that bypass the
model’s defenses.
• TAP (Mehrotra et al., 2023): The Tree of At-
tacks with Pruning (TAP) method maintains
a structured flow in the form of a tree to it-
eratively optimize the jailbreak prompt. The
attack continues until a successful jailbreak
prompt is found.
B
Implementation Details of Defenders
B.1
Inference Time Defense
We selected 13 inference-time defense methods,
categorized into three main strategies, and pro-
vide a unified interface for these defense methods,
which can be utilized in the defend_chat function,
as illustrated in Table 2.
B.2
Training Time Defense
The Training Time Defense is applied during the
training process of large language models. It in-
cludes three categories: Safety Data Tuning, RL-
based Alignment and Unlearning. And we imple-
ment a method for each category.
• Safety Data Tuning: Safety-Tuning (Bianchi
et al., 2023)

--- Page 12 ---

Figure 2: Overview of the categorization of safety defense methods.
Type
Description
Usage
Methods
Preprocess
The input is preprocessed to de-
tect or guard against harmful
content before the generation
process.
defend(self,
message)
→(defended_message,
if_reject)
PPL (Alon and Kamfonas, 2023)
Self Reminder (Xie et al., 2023)
Prompt Guard (Meta-Llama, 2024)
Goal Prioritization (Zhang et al., 2024e)
Paraphrase (Jain et al., 2023)
ICD (Wei et al., 2023b)
Intraprocess
Utilizes safer decoding or gen-
eration strategies to ensure the
outputs are secure and adhere to
safety guidelines.
defend(self,
model,
messages) →response
SmoothLLM (Robey et al., 2023)
SafeDecoding (Xu et al., 2024)
DRO (Zheng et al., 2024)
Erase and Check (Kumar et al., 2023)
Robust Aligned (Cao et al., 2023)
Postprocess
The output is postprocessed to
enhance safety.
defend(self, response)
→defended_response
Self Evaluation (Brown et al., 2024)
Aligner (Ji et al., 2024)
Table 2: Overview of Inference-Time Defense Types and Their Components
• RL-based Alignment: Safe RLHF (Dai et al.,
2023)
• Unlearning: Safe Unlearning (Zhang et al.,
2024d)
Organized into key directories such as config,
data, model, train, and utils, the training framework
ensures modularity and ease of management. The
data directory handles preprocessing and dataset
management, while train encompasses specialized
subfolders for different training methods, includ-
ing trainers and workflows, which is flexible and
customizable.
C
Implementation Details of Scorers
The implementation details of the seven scorers
mentioned in section 3.4 are presented as follows:
• PatternScorer. This scorer judges the success
of a jailbreak attempt by examining whether
the response matches predefined jailbreaking
failure patterns. A response is considered safe
if it includes a certain failure pattern.
• PrefixMatchScorer. This scorer judges the
success of a jailbreak by checking the prefix of
the response. A response is considered unsafe
if it starts with a jailbreaking target.
• ClassficationScorer. This scorer uses a clas-
sification model to assess the safety of the re-
sponse. The scorer is initialized by a Roberta
model from Yu et al. (2023), and it is also
acceptable to init this scorer with any cus-
tomized classification model.
• ShieldLMScorer. This scorer uses ShieldLM
to assess the safety of the response, which in-
corporates an analysis alongside its judgment
explaining the reason behind its decision.
• HarmBenchScorer.
This scorer uses the

--- Page 13 ---

HarmBench-Llama-2-13b-cls classification
model (Mazeika et al., 2024b) to assess the
safety of the response.
• LlamaGuard3Scorer.
This scorer uses
Llama-Guard-3-8B to assess the safety of the
response. It also provides the unsafe category
if the response is judged as unsafe.
• PromptedLLMScorer. This scorer prompts
a model to assess the safety of the response.
We incorporate four judge prompts from Qi
et al. (2023), Zhang et al. (2024b), Mehrotra
et al. (2023) and Chao et al. (2023).

```
