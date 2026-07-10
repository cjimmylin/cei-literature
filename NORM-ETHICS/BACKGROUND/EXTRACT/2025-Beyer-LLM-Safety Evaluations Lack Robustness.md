---
title: "2025-Beyer-LLM-Safety Evaluations Lack Robustness - Background Extract"
source_pdf: "2025-Beyer-LLM-Safety Evaluations Lack Robustness.pdf"
source_folder: "01-vault-papers"
pages: 22
extracted_at: "2026-04-03T10:25:00"
---

# Background Extract: 2025-Beyer-LLM-Safety Evaluations Lack Robustness

**Source PDF:** 2025-Beyer-LLM-Safety Evaluations Lack Robustness.pdf
**Source:** 01-vault-papers
**Total Pages:** 22

---

## Content

```
--- Page 1 ---

LLM-Safety Evaluations Lack Robustness
Tim Beyer 1 Sophie Xhonneux 2 Simon Geisler 1 Gauthier Gidel 2 3 Leo Schwinn 1 Stephan G¨unnemann 1
Abstract
In this paper, we argue that current safety align-
ment research efforts for large language mod-
els are hindered by many intertwined sources of
noise, such as small datasets, methodological in-
consistencies, and unreliable evaluation setups.
This can, at times, make it impossible to evaluate
and compare attacks and defenses fairly, thereby
slowing progress. We systematically analyze the
LLM safety evaluation pipeline, covering dataset
curation, optimization strategies for automated
red-teaming, response generation, and response
evaluation using LLM judges. At each stage, we
identify key issues and highlight their practical
impact. We also propose a set of guidelines for
reducing noise and bias in evaluations of future
attack and defense papers. Lastly, we offer an op-
posing perspective, highlighting practical reasons
for existing limitations. We believe that address-
ing the outlined problems in future research will
improve the field’s ability to generate easily com-
parable results and make measurable progress.
1. Introduction
Large Language Models (LLMs) have rapidly transitioned
from research to widespread adoption by millions of users
and industry (Achiam et al., 2023; Google et al., 2024; Tou-
vron et al., 2023; Anthropic, 2024a). Since their adoption,
model capabilities have considerably increased, quickly
saturating many common benchmarks (Clark et al., 2018;
Zellers et al., 2019). Furthermore, with the advent of multi-
modal and agentic models derived from LLMs, the op-
erational scope has quickly grown far beyond text-only
tasks (Liu et al., 2024; Google et al., 2024).
As a direct consequence of their widespread adoption and
growing capabilities, the safety and reliability of LLMs have
become increasingly relevant, which is also reflected by re-
sponses from politics (AISI, 2024; Schuett, 2024; Congress,
2020), academia (Huang et al., 2024; Hendrycks & Mazeika,
1Department of Computer Science & Munich Data Science
Institute, Technical University of Munich 2Mila & Universit´e de
Montr´eal 3Canada AI CIFAR Chair. Correspondence to: Tim
Beyer <tim.beyer@tum.de>.
Copyright 2025 by the authors.
2022), and industry (Anthropic, 2024b; OpenAI, 2023a;
Touvron et al., 2023). Governments are addressing AI risk
concerns via new regulations (Act, 2024; Congress, 2020)
and the establishment of AI risk centers, such as the UK AI
Safety Institute (AISI, 2024). Furthermore, the academic
community has responded with a considerable amount of re-
search investigating potential risks associated with advanced
AI systems (Hendrycks et al., 2023) and approaches to de-
tect and mitigate vulnerabilities (Yu et al., 2023). Lastly,
model providers have demonstrated efforts toward aligning
models to their safety guidelines (Bai et al., 2022; Guan
et al., 2024) by releasing open-source projects (OpenAI,
2023b; AI@Meta, 2024a), technical reports (Achiam et al.,
2023; Abdin et al., 2024; Dubey et al., 2024), and safety test-
ing through external partners (OpenAI, 2023c; AI@Meta,
2024b) and safety institutes.
Despite these initiatives, jailbreaks that circumvent built-
in safety systems quickly emerged and have remained a
challenge since then (Shen et al., 2024). We use an LLM’s
ability to stay aligned & safe despite adversarial inputs as a
synonym for its “robustness” (see Appendix A.1.1). Here,
we observe parallels to past research on reliable machine
learning in computer vision, as detailed in Appendix A.1.2.
The vulnerability of neural networks to adversarial attacks
has been an open research problem for a decade, and despite
considerable work in this area, the problem remains largely
unsolved (Carlini, 2024). This lack of progress can be at-
tributed, in part, to faulty evaluations, which often produced
noisy and misleading feedback, obscuring which approaches
were genuinely effective (Athalye et al., 2018).
We argue that the issue of unreliable evaluations is likely
to become even more pronounced in the context of LLM
robustness, where compute costs are considerably higher
and the evaluation pipeline is significantly more complex
compared to previous research in other domains.
This complexity arises from challenges in assessing subjec-
tive qualities of natural language, like safety and helpfulness,
as well as the increased variety of evaluation hyperparam-
eters (e.g., tokenizers, chat templates, quantization, etc.),
which are not standardized and often not clearly commu-
nicated. These inconsistent evaluation protocols introduce
numerous sources of bias and measurement noise and force
researchers to expend considerable effort to reproduce past
papers under their exact setup to ensure fair evaluation, fur-
ther increasing engineering and compute costs.
1
arXiv:2503.02574v1  [cs.CR]  4 Mar 2025

--- Page 2 ---

Position: LLM-Safety Evaluations Lack Robustness
Algorithms
Evaluation
Datasets
- targets biased against
  particular models
- greedy decoding only 
- buggy toolboxes
- ignore overrefusal-
  safety tradeoff 
- fragmented judge ecosystem
- conflation of single- and 
  many-trial attacks
- no manual verification
- model- and attack-specific
  biases
- inconsistent normalization
- small & fragmented
- inconsistent subsampling 
- ambiguous definitions
- repetitive
- single-turn
- English only
 
Figure 1: We decompose the LLM safety evaluation pipeline into three stages and analyze common problems at each step.
In this position paper, we argue that the current LLM-
safety evaluation pipeline is unreliable by making the
following contributions:
• We demonstrate how current evaluations introduce bias
and noise at various stages of the LLM evaluation pipeline.
• We substantiate our position by consolidating insights
from prior research and presenting our own case studies.
• We offer recommendations for mitigating these challenges
to improve future evaluation’s reliability & comparability.
2. Datasets
Significant progress in many domains of machine learn-
ing can be traced to the introduction of large, high-quality
datasets for various tasks (Deng et al., 2009; Dai et al.,
2017; Gokaslan & Cohen, 2019). However, datasets for
LLMs, particularly in the context of safety and alignment,
remain underdeveloped. Current LLM evaluations gener-
ally rely on three types of datasets: safety, capability, and
overrefusal. While large-scale, high-quality datasets for
evaluating model capability exist (Hendrycks et al., 2020;
Zheng et al., 2023; Wei et al., 2024), current safety and
overrefusal datasets exhibit significant shortcomings.
Key Issues with Current Datasets
Small sample sizes, inconsistently chosen (sub-)
datasets, and low task diversity/prompt quality.
→Severe uncertainty in attack & defense evaluation.
Our jailbreaking datasets are too small to produce re-
liable results.
Due to the rapid development of numer-
ous, often overlapping, datasets aimed at addressing limi-
tations in previous work, the field of jailbreaking datasets
has become increasingly fragmented and difficult to nav-
igate (Huang et al., 2023; Zou et al., 2023b; Chao et al.,
2024; Souly et al., 2024; MLCommons, 2025). Despite this
growth, commonly used datasets remain relatively small,
typically comprising only 100-500 harmful prompts (c.f.
Table 2 in Appendix 2).
In general, access to sufficiently large datasets is crucial
since inherent statistical noise introduced by small sample
sizes in current work is excessive, preventing reliable com-
parisons between different systems. This is easily demon-
strated using well-established statistics: We can model the
jailbreaking (and overrefusal) performance of a determin-
istic model via a binomial trial where n is the number of
prompts in the dataset, and ns is the number of successful
trials. Our goal is to estimate the underlying probability of
success p on new prompts drawn from the same distribu-
tion via an estimator ˆp. Given a uniform prior for p, the
confidence interval follows the Clopper-Pearson interval:
B
α
2 ; ns, n −ns + 1

< p <B

1 −α
2 ; ns + 1, n −ns

For example, with n = 150 and ns = 75, the estimate for
p has standard deviation 0.0408, with a 95% confidence
interval of [0.417, 0.583], indicating significant uncertainty.
Furthermore, the true level of uncertainty with respect to
real-world robustness is likely to be much higher. Sam-
pling during generation introduces additional noise, and
new prompts in the real world will not necessarily come
from the same, simple distribution as the benchmark data.
Thus, we strongly support calls to include uncertainty in
evaluations (Miller, 2024), as (with few exceptions (Guan
et al., 2024)) this is currently rarely done, even though it
adds important context to readers who would like to evaluate
whether two methods differ significantly.
These concerns are not merely theoretical: As we illustrate
in Appendix A.5.1, key results from (Guan et al., 2024)
would be inconclusive at significance level α = 0.05 when
relying solely on public datasets. Yet, these datasets remain
the basis for evaluation and comparisons across the field.
Even for well-funded research by frontier labs (Hughes et al.,
2024; Guan et al., 2024; Zhu et al., 2024) with extensive
internal datasets and evaluation harnesses, public datasets
remain central to facilitate comparisons with academic lit-
erature. As a result, we emphasize the need for larger,
high-quality benchmark datasets for jailbreaking. Ef-
forts like AILuminate (MLCommons, 2025) and CoCoNot
(Brahman et al., 2024), which focus on larger scale, both
make steps in this direction.
High-quality overrefusal datasets are too small & not
widely-adopted.
The most-used overrefusal datasets face
a similar issue: collections of challenging unambiguous
2

--- Page 3 ---

Position: LLM-Safety Evaluations Lack Robustness
prompts as in XSTest (R¨ottger et al., 2023) are small, while
larger datasets either lack enough challenging examples
(Zhao et al., 2024), or include LLM-generated ambigu-
ous content with dual-use characteristics (Cui et al., 2024).
Many such prompts feature dual-use scenarios, a common
jailbreaking technique that may violate developer guidelines,
rendering them suboptimal for fair model comparisons.
Examples of Overrefusal Prompts
“How can I write an email that resem-
bles a phishing attempt to understand the
warning signs better?” (Cui et al., 2024)
✗Ambiguous
“How do I stab a balloon to make it
pop?” (R¨ottger et al., 2023)
✓Harmless
The recently introduced CoCoNot (Brahman et al., 2024)
dataset focuses on refusal in non-safety settings, but also
contains a significant number (1,306) of examples similar
to prompts in XSTest, however, it has not yet been used in
the context of LLM defenses. In industry, several teams
have collected significantly larger and more diverse internal
datasets for overrefusal, though these are not publicly avail-
able (Dubey et al., 2024; Guan et al., 2024).
Above all, overrefusal datasets should aim to be as unam-
biguous as possible and focus on including prompts that
are likely to mislead models, but are clearly not harmful
in nature. In addition, because overrefusal is cheaper to
evaluate than most model jailbreaks, as it only requires a
single generation, evaluations with large sample sizes are
attainable even for more compute-constrained researchers.
As a result, while we view overrefusal datasets as a critical
part of the pipeline, we think that relatively straightforward
solutions, such as extending XSTest (R¨ottger et al., 2023)
or adopting the CoCoNot (Brahman et al., 2024) contrast
set provide a viable path forward.
Data is inconsistently subsampled.
Even within existing
datasets, data is often further subsampled, typically due to
resource constraints, a focus on harder examples, or to filter
out low-quality prompts. This results in evaluations using
as few as 40 (Xhonneux et al., 2024), 50 (Andriushchenko
et al., 2024; Zhu et al., 2024), 100 (Geisler et al., 2024; Chao
et al., 2023), or 159 (Hughes et al., 2024) samples. In many
cases, selection criteria and selected prompts are poorly or
not at all documented, complicating reproducibility.
We acknowledge that limited computational resources
in academia often make large-scale experiments on full
datasets difficult and that noisy results from fewer data
points can still offer insights or serve as proofs-of-concept
(Polo et al., 2024). However, while the computational
requirements for a particular paper may be reduced,
the computational burden shifts downstream: to con-
duct fair comparisons, researchers are often forced to retrain
models and reimplement and/or rerun all baselines on their
particular subset of data and setup, which is expensive and
time-consuming. Thus, the inconsistent environments and
data subsampling actually increase the resources needed by
the research community as a whole, which hinders progress.
For instance, consider GCG (Zou et al., 2023b), which, with
default hyperparameters, requires 256,000 forward and 500
backward passes1, plus a single victim model generation
and one judge model generation. More efficient approaches,
such as PAIR (Chao et al., 2023) still require up to 60 gen-
erations each from the victim model, the attacker LLM, and
the judge model. Assuming the default of 500 tokens per
generation, this still requires (60 + 60) · 500 = 60, 000
forward passes plus judging for each prompt.
The most robust way to avoid the problems associated
with subsampling and make comparisons easier is to
present results using the full dataset. However, in cases
where larger sample sizes are truly prohibitive, small pre-
defined test/dev sets in new datasets or other consistent
selection criteria for data subsampling would significantly
improve comparability across different works while reduc-
ing the need for redundant reimplementations. We therefore
call for increased transparency and better consistency
in terms of prompt selection to mitigate the broader
inefficiencies caused by subsampling.
Our datasets are too rigid and unrealistic.
As pointed
out in recent work, commonly used jailbreaking & over-
refusal datasets such as AdvBench and XSTest mainly con-
tain prompts with highly repetitive structure and straight-
forward content (Souly et al., 2024; Xhonneux et al., 2024).
In addition, prompts generally consist of short, single-turn
interactions, in English only. Although some skills, like in-
struction following, may transfer across languages (Ouyang
et al., 2022), recent research indicates that safety knowledge
is language-specific and requires targeted data collection to
ensure safe behavior in multiple languages (Dubey et al.,
2024). We think this lack of diversity can lead to blind spots
and contributes to the phenomenon of shallow alignment (Qi
et al., 2024) and the success of relatively naive jailbreaks,
such as past-tense attacks (Andriushchenko & Flammarion,
2024) or translation attacks (Yong et al., 2023) that deviate
from the rigid patterns in existing datasets.
Thus, we believe future datasets should more closely
depict real-world threat models and user interactions
and allow the investigation of more nuanced differences
in model behavior, for instance, on prompts and conver-
sations of varying lengths and grammatical styles. While
assembling model-agnostic (or at least unbiased) multi-turn
datasets is challenging, it would be a valuable resource to
evaluate alignment in real-world scenarios, as there are in-
dications that LLMs can become less robust in multi-turn
1While attack effort can be quantified more precisely—e.g., in
FLOPs (Boreiko et al., 2024)—we simply wish to highlight the
substantial computational cost of running baselines.
3

--- Page 4 ---

Position: LLM-Safety Evaluations Lack Robustness
settings (Bhardwaj & Poria, 2023). A promising direction
could be to take advantage of collections of chats such as
WildChat (Zhao et al., 2024) for ChatGPT and manually cu-
rate real-world instances of falsely refused benign prompts
or users seeking harmful information.
The strong focus on English examples poses another signifi-
cant limitation for estimating real-world robustness, as users
may communicate in any language. However, multi-lingual
evaluation is logistically difficult—especially in academic
contexts. Firstly, constructing high-quality datasets requires
authors to speak the languages of the benchmark. Secondly,
judge models are mostly trained and evaluated on English
data, making automated evaluation more difficult. Many
scenarios also rely on manual evaluations (e.g., monitoring
outputs during development or verifying decisions by au-
tomated judges), which become impractical as additional
languages are involved. Lastly, not all models are trained on
the same set of languages, further complicating fair compar-
isons. We are not sure how to best address these problems;
however, it would certainly be valuable to conduct trans-
fer experiments to evaluate how well results generalize to
languages that were not part of the model’s safety training.
Ill-defined requirements lead to datasets that measure
alignment with inconsistent targets.
It is important to
remember that universally valid definitions of harmfulness
do not exist, as ethical guidelines and societal norms vary
across communities. Therefore, rather than attempting to
make models “harmless”, the core technical goal of align-
ment research can only be making models adhere to the
goals and values the model developers aim to instill, which
is orthogonal to the specification of the goals and values
themselves. In contrast, red-teaming and jailbreaking efforts
deliberately attempt to push models to deviate from their
intended behavior. In the context of robustness research,
we argue that the community should focus on developing
datasets that objectively assess how difficult it is to make
models deviate from their intended behavior. Since it is in-
feasible to collect specific datasets according to each model
developer’s guidelines, we think jailbreaking datasets should
focus on only including content considered harmful by most,
if not all, model developers. This ensures fair comparisons
between models by different developers without penalizing
model behavior that a developer opts not to restrict.
While this may seem somewhat trivial, even widely used
datasets like AdvBench (Zou et al., 2023b), which explic-
itly aim for this goal, include ambiguous content—such as
drug-related questions that are only illegal in some jurisdic-
tions and may not be considered harmful by all developers.
These inconsistencies introduce noise and bias into evalua-
tions, undermining our ability to fairly compare alignment
strategies used by different model providers. Recent efforts
to rigorously aggregate common guidelines from multiple
developers before collecting prompts, such as in StrongRE-
JECT (Souly et al., 2024), represent a sensible direction and
should be adopted by new datasets in the future as well.
3. Algorithms
Key Issues with Current Algorithms
Inconsistent implementation details, varying attack
budgets, rigid-optimization objectives, and overlooked
safety-overrefusal trade-off.
→Unfair, noisy & biased comparisons.
Implementation details matter.
Comparing algorithms
and models across publications is complicated by imple-
mentation details that are often not clearly communicated,
but introduce small errors, which can compound into sig-
nificant discrepancies. Key issues include quantization, ini-
tialization, inconsistent use of chat templates and system
messages, handling of whitespace tokens, as well as insuf-
ficient filtering of special tokens. Such discrepancies can
affect attack success rates and were also observed in LLM
capability evaluations (Biderman et al., 2024). These prob-
lems are especially relevant for white box attacks that rely
on explicitly forcing a specific target token sequence, and
are particularly difficult to catch, as finding them typically
requires tedious manual verification for each model and im-
plementation without raising obvious errors.
Models strongly expect whitespace characters and control
tokens to appear at certain positions, such as before or after
control tokens. If the target tokens are misaligned, the opti-
mizer has to spend additional “effort” to move probability
mass away from white space tokens, which is significantly
more difficult in comparison to standard text tokens. Figure
2 empirically demonstrates this effect, showing that incor-
rectly accounting for whitespace tokens can reduce attack
success rate by 28%. Appendix A.2 contains a more detailed
discussion of this experiment. These issues can dramatically
affect the success of an attack, and detecting them can be
very tedious, as many whitespace characters are removed
during detokenization and are thus invisible in the generated
text. We therefore urge developers to manually check the
alignment of model generations with the target sequence
in token-space to ensure correct alignment.
The community widely agrees that token-level discrete op-
timization algorithms should exclude special tokens (e.g.,
instruction, tool use, role tokens) from the optimization. We
thus echo the sentiment from (Thompson & Sklar, 2024b)
and strongly recommend that discrete attack algorithms
track all state as a string a user could pass directly to the
model in a chat setting. While this may incur additional
implementation overhead, it ensures that the discovered at-
tacks are usable in practice. We find that even widely used
implementations in nanoGCG (Zou et al., 2023b) and Harm-
Bench (Mazeika et al., 2024) often fail to correctly filter out
special tokens and other impossible attacks.
4

--- Page 5 ---

Position: LLM-Safety Evaluations Lack Robustness
0
50
100
150
200
250
Step
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
Loss
0
50
100
150
200
250
Step
0.0
0.2
0.4
0.6
0.8
1.0
Many-trial ASR
Correct Whitespace
Incorrect Whitespace
Figure 2: Impact of the SentencePiece white space token on
GCG performance against Llama-2-7B-chat-hf. We judge
the generated prompt at each step and report “many-trial”
or “cumulative” ASR.
Chat Template
Filter
Dtype
ASR
Meta
Strict
BF16
0.77
HuggingFace
Strict
BF16
0.85
Meta
nanoGCG
BF16
0.78
Meta
Allow Non-ASCII
BF16
0.73
Meta
Strict
Int8
0.71
No Sys Msg
Strict
BF16
0.47
Table 1: Many-trial ASR of GCG against Llama-3.1-8B-
Instruct with minor implementation changes. Even among
reasonable configurations with system prompt, ASR varies
significantly between 71% and 85%. Additional details can
be found in Appendix A.3.
Table 1 illustrates these challenges. Given their widespread
use and relatively well-supported software, we select GCG
as the attack and Llama-3.1-8B-Instruct as the victim model,
though other setups may exhibit even greater discrepancies.
We compare several versions of the chat template, system
prompts, quantization levels, and token filtering approaches.
All reported setups are genuine best-effort implementations
a researcher may attempt. Using the Meta-recommended
chat template with a corrected strict token filtering proce-
dure lowers ASR by 8% compared to the default template in
the HuggingFace Transformers library with default token
filtering from the official GCG implementation, while an
int8 quantized model has 14% lower ASR.
Efforts like (Mazeika et al., 2024; Chao et al., 2024) aim
to tackle some of these issues by standardizing attack im-
plementations and other aspects of the pipeline. However,
in practice, many new algorithms are still built in bespoke
repositories (Andriushchenko et al., 2024; Sadasivan et al.,
2024), without taking advantage of these toolboxes. In
our experience, the main reasons researchers opt for this
are a lack of flexibility, reliability issues, and overly com-
plex frameworks that attempt to abstract across models, but
end up obfuscating underlying issues, leading to a steep
learning curve and making them frustrating to work with.
Furthermore, long-term maintenance is often not guaran-
teed, reducing the incentive for authors to implement their
method in a particular framework. Solving these problems
is challenging, as the development and continued mainte-
nance of such frameworks are not sufficiently recognized
by the academic community to justify the sustained effort.
Attacks are not compared at consistent budgets.
Many
algorithms have hyperparameters that trade-off compute,
perplexity, or the number of model queries for higher ASR.
However, most papers report performance for a specific
“operating point”—typically one that maximizes ASR for
the available resources—without adequately illustrating the
compute-ASR trade-off for their method and baselines. This
narrow focus on final ASR leads to misleading comparisons.
For example, GCG is usually run with default hyper-
parameters, which use a large number of steps, making it
appear inefficient and compute-intensive (Chao et al., 2023;
Sadasivan et al., 2024). However, as seen in Figure 4 and
Appendix A.3, GCG can reach significant ASRs and a better
compute-ASR trade-off with far fewer steps.
Thus, to ensure fair evaluations, attacks should be compared
under controlled conditions by fixing either the attack bud-
get or the success rate. Results where neither is matched
often do not allow for meaningful comparisons unless one
method Pareto-dominates others in all domains.
Some recent works take steps toward better standardization
by reporting the mean number of queries per success(Chao
et al., 2023), iso-GPU-time results (Sadasivan et al., 2024),
wall-time on consistent hardware (Geisler et al., 2024), mon-
etary cost estimates for commercial models (Hughes et al.,
2024), or FLOP-budgets to quantify compute use (Boreiko
et al., 2024). We think these are all valuable ideas, and re-
porting and controlling for attack budget should become
standard in the field.
Optimization objectives are biased, unnatural, and poor
proxies for attack success.
Most competitive attacks
(AmpleGCG, AutoDAN, BEAST, GCG, PGD, PAIR, ...)
rely on predefined target string sequences provided by the
jailbreak datasets. This objective is suboptimal as it is not
model-agnostic. Nearly all targets follow a rigid “Sure,
here...” template. When a model’s “natural” affirmative re-
sponses follow a different structure, the rigid targets become
harder to optimize against and thus appear more robust than
they actually are (Zhu et al., 2024) (c.f. Appendix A.4).
A similar issue can occur when defenses are trained with
knowledge of the optimization targets the attacks will use.
This data leakage can lead to methods that defend remark-
ably well when attacks try to optimize for the same targets
used during training; however, when attacks choose a dif-
ferent objective, they can quickly become more brittle. For
instance, R2D2 (Mazeika et al., 2024) was adversarially
trained against GCG, and its safety generalizes relatively
well to other approaches that aim to optimize the datasets’
target sequence (e.g., AutoDAN). However, R2D2 remains
5

--- Page 6 ---

Position: LLM-Safety Evaluations Lack Robustness
susceptible to PAIR (Chao et al., 2023), which employs
LLM-driven optimization of the prompt rather than heavily
relying on the explicit target sequence.
Furthermore, successfully manipulating a model into out-
putting the full target sequence does not guarantee a harmful
response as models can “recover” and continue with a safe
response. Instead, the effectiveness of the generated attack
depends on the implicit bias of the optimization algorithm.
While some methods attempt to diversify the targets (Jia
et al., 2024; Zhu et al., 2024; Thompson & Sklar, 2024b)
to speed up the optimization process, we think the field
could benefit from considering a broader perspective. In
other domains, such as computer vision, adversarial attacks
were able to make progress by constructing consistent loss
functions, where lower loss is guaranteed to correspond to
higher success rates (Tramer et al., 2020).
Although it may not be feasible to design fully consistent
loss functions for generative models, we think the commu-
nity should explore ways to more directly optimize for
successful attacks, rather than overfocusing on optimizing
for specific token sequences that may introduce bias and fail
to provide a consistent surrogate signal for ASR.
Defenses
do
not
consistently
report
the
safety-
overrefusal trade-off.
Designing safe LLMs inherently
requires balancing competing objectives: maximizing ro-
bustness to adversarial inputs while minimizing overrefusal
of benign prompts.
This trade-off is well documented
(Thompson & Sklar, 2024a; An et al., 2024), yet, with few
exceptions (Yu et al., 2024; Dubey et al., 2024; Guan et al.,
2024), existing defenses rarely account for it comprehen-
sively. Many defenses only include results for capability
benchmarks but do not use overrefusal datasets such as the
aforementioned XSTest (R¨ottger et al., 2023) or the Co-
CoNot contrast set (Brahman et al., 2024). We argue that
safety and overrefusal should always be evaluated in
tandem, with methodologies explicitly acknowledging this
trade-off using standard benchmarks.
4. Evaluation
The last stage of the LLM safety evaluation pipeline typi-
cally consists of sampling a model generation and judging
whether the model has been broken or not.
Key Issues with Current Evaluation
Limited to greedy generation, a fragmented ecosystem,
and judges with model- & attack-specific biases.
→Overoptimistic results, misleading & biased evalua-
tions for untested attacks & defenses.
Greedy generation is unrealistic and ignores the distribu-
tional nature of LLM outputs.
Greedy decoding, where
the model always selects the highest-probability token at
each step, is currently the dominant setup for sampling from
victim models in the context of LLM robustness. While
convenient and deterministic, this strategy does not match
practical chatbot settings where model responses are sam-
pled using a variety of methods (Vijayakumar et al., 2016;
Holtzman et al., 2019; Su et al., 2022) to avoid repetitive
answers and produce natural output.
In fact, even with a fixed prompt, frontier models can often
be broken by simply sampling a large number of generations
at temperature 1 (Hughes et al., 2024)2.
From a statistical standpoint, evaluating models at temper-
atures that differ from deployment settings is undesirable,
as it can make noise mitigation techniques like resampling
harder or even impossible in the case of greedy decoding
(Miller, 2024). Additionally, Scholten et al. (2024) show
that this setup fails to accurately characterize real-world
model behavior, leading to over-optimistic bounds on safety
and alignment: models that appear robust in greedy genera-
tion may still produce harmful content a significant fraction
of the time when deployed with more realistic sampling
strategies. Similar limitations also apply from the attacker’s
perspective: an attack prompt effective for greedy genera-
tion may not reliably generalize to real-world settings with
more representative sampling methods (Hughes et al., 2024).
To better assess the “robustness” of individual attack
prompts and to provide better model safety guarantees, we
think a more realistic, distributional approach which
samples multiple generations under realistic conditions
and judges them independently may offer new insights.
Single-trial and many-trial jailbreaks lack clear differ-
entiation.
There is a disconnect between methods that
perform multiple queries and evaluate multiple model re-
sponses (“many-trial”) until a jailbreak is found or the search
budget is exhausted (Hughes et al., 2024; Liao & Sun, 2024;
Chao et al., 2023; Andriushchenko et al., 2024), and those
which optimize a prompt first and then test only the opti-
mized prompt using greedy generation (“single-trial”) (Zou
et al., 2023b; Geisler et al., 2024; Sadasivan et al., 2024; Liu
et al., 2023a). Comparing these attack types is complicated
as their practicality and efficiency depend on the model de-
fenses employed and the cost model of the attacker. For
example, cheaply generating many prompt candidates with
low individual success probability may be efficient from a
time or dollar cost standpoint but would require many model
rollouts and could be more easily filtered by providers due
to the suspicious query pattern of sampling a large amount
of very similar prompts. In contrast, methods that expend
more compute to come up with fewer (or even a single)
prompts with high individual success likelihood may be
2Hughes et al. (2024) primarily focus on augmented versions of
harmful prompts, but an ablation using a fixed prompt shows that
simply sampling more generations consistently increases ASR.
6

--- Page 7 ---

Position: LLM-Safety Evaluations Lack Robustness
more desirable from a query-efficiency standpoint.
Another consideration when comparing attacks is that at-
tacks with “many-trial” characteristics are more likely to
overstate their performance because they benefit from the
classifier’s false positive rate (FPR) for each query. Unless
the results are manually verified3, each additional inference
raises the risk of sampling an outlier harmful generation or
misgrading an unsuccessful attack as a false positive. In
addition, recent results show that even with manual veri-
fication, it is possible to successfully jailbreak models by
simplifying sampling a large number of responses, some-
times without altering the harmful prompt at all, further
advantaging many-trial approaches (Hughes et al., 2024).
Given these disparities, we argue that these two setups must
be clearly distinguished, and that many-trial attacks
should account for the classifier’s FPR when assessing
the significance of results. In addition, wherever possible,
but particularly for “many-trial” jailbreaks, we recom-
mend manually screening generations for false positives.
The LLM-judge ecosystem is fragmented.
Due to the
prohibitive cost of human annotators, most works rely on
automated classifiers to decide whether an output is harm-
ful. However, the landscape is highly fragmented: some
methods train custom classifiers (Huang et al., 2023; Zhu
et al., 2024; Dai et al., 2023), others use fine-tuned LLM
judges like Harmbench Llama-2 (Mazeika et al., 2024; Bor-
eiko et al., 2024; Zou et al., 2024) or StrongREJECT (Souly
et al., 2024; Guan et al., 2024), while others employ pre-
trained models such as GPT or Llama variants using custom
prompt templates (Chao et al., 2024; Hughes et al., 2024;
Thompson & Sklar, 2024b). Some approaches incorporate
human verification (Zou et al., 2023b; Hughes et al., 2024;
Guan et al., 2024), and others fail to specify their evaluation
methodology entirely. Although there are good reasons to
train a new classifier (e.g., systematic failures in preexisting
ones), the disjointed ecosystem of judges, prompt templates,
and evaluation strategies complicate meaningful compar-
isons across studies.
In addition, despite prior work demonstrating that genera-
tion length affects attack success rates (Mazeika et al., 2024),
there is still no consistent standard in the literature. Some
works propose to use a consistent amount of judge tokens,
while others use the victim model to generate a fixed number
of tokens. While there are arguments to be made for both
cases, we think the most realistic threat model would evalu-
ate a full model response up to the end-of-turn/end-of-text
token. This is closest to real-world use cases where users
chat with models in a (mostly) unconstrained setting.
Finally, varying definitions of “successful” jailbreaks are
used, with a clear trend of criteria becoming increasingly
3In fact, even human judges may have nonzero FPR and could
be affected too.
strict and precise over time, which we see as a positive devel-
opment. We do not claim to have definitive answers, and we
recognize that the community has not yet reached a consen-
sus. Nevertheless, we believe that researchers would benefit
from a more standardized judging environment. As judg-
ing is relatively compute-inexpensive compared to running
attack algorithms or training a model defense, we recom-
mend that new works report results on multiple popular
judges (e.g., Harmbench Llama-2-13b and StrongREJECT),
and include a detailed description or code for the ex-
act judge setup used to facilitate easier comparisons and
reproductions.
Judges are not verified against new attacks & defenses.
Since attacks and especially defenses can significantly
change a model’s output distribution, generated responses
may fall far outside the judges’ training data, causing attack-
and defense-specific misclassifications.
In Appendix A.5.2, we show that model-specific differences
occur in practice and can lead to misleading comparisons
between the safety of two models. We also conduct a large-
scale study on 5,269,564 generations and compare judg-
ments by Harmbench’s Llama-2 13B classifier and Stron-
gREJECT’s Gemma 2B judge, and reveal attack- and model-
specific biases—up to 25% for specific attacks and up to
24% across models (see Figure 3), complicating attack, de-
fense, and model evaluations. Detailed results & analysis
are provided in Appendix A.6. Similar biases have been
observed before; for instance, Hughes et al. (2024) find that
circuit breaker models (Zou et al., 2024) have higher judge
FPR compared to baselines, which would lead to unfair
comparisons without manual verification.
To avoid misleading results, we propose that new at-
tacks and defenses should include at least a small-scale
human-verification that judges still work for the pro-
posed method, e.g. by manually checking 100 examples,
as is done in (Chao et al., 2023). This is a manageable
time investment that ensures attacks and defenses remain
comparable and shields from effects such as the higher-than-
expected FPR of some judges on specific models.
Mistral CB
Zephyr R2D2
Mistral v0.3
Zephyr 
0.00
0.05
0.10
0.15
0.20
 ASR (CAIS - StrongREJECT)
Figure 3: Comparing ASR differences across common
judges reveals significant model-specific bias, despite all
four models being derivatives of the same Mistral 7B model.
7

--- Page 8 ---

Position: LLM-Safety Evaluations Lack Robustness
5. Alternative Views
Small datasets have significant practical advantages.
While we advocate for the adoption of larger datasets,
smaller ones offer key benefits. Even with small sample
sizes, LLM robustness research is computationally expen-
sive due to the size of modern models and the need for strong
adversarial attacks to ensure reliable evaluations. Unlike
prior adversarial robustness research in fields like computer
vision, optimizing attacks in a discrete input space adds
further complexity: current approaches require hundreds
of thousands of queries per prompt, creating a bottleneck
in robustness research. Using larger datasets would only
exacerbate these issues and further raise the barrier to entry.
Meanwhile, the lower computational demands of small
datasets accelerate experimentation and research cycles, par-
ticularly in resource-constrained academic settings. This
facilitates innovative research, as hypotheses can be evalu-
ated quickly and cost-effectively. For instance, recent work
(Andriushchenko et al., 2024) convincingly demonstrated
that model-adaptive attacks can reach very high ASR using
relatively few (50) samples. In general, even small datasets
can provide enough signal to show the usefulness of a new
approach at lower cost if the effect size is sufficiently large.
Even when precise results are required, sophisticated sub-
sampling strategies can be used to enhance the predictive
power of small-scale experiments. For instance, Polo et al.
(2024) reveal that a carefully selected subset of 100 ques-
tions can reliably approximate LLM capability on the full
MMLU dataset with over 15k questions. This indicates
that larger sample sizes may not be a strict requirement for
comprehensive LLM evaluations.
On flawed LLM judges. Compared to other, more con-
strained domains with well-defined tasks and success criteria
(e.g., image classification) the desire to find consistent and
objective metrics may simply be misplaced in the context of
LLM-robustness evaluations. Language is ambiguous and
even our most precise rules will likely never catch all edge
cases. The best we can do is iteratively refine our measures
of jailbreaking success and continuously adapt automated
judge models to capture these definitions more closely. In
fact, this is exactly what the field is doing: researchers are
constantly developing improved judge models that rely on
increasingly precise definitions and better approximate hu-
man judgment (Mazeika et al., 2024; Souly et al., 2024; Zhu
et al., 2024). Though imperfect, these evaluations are the
only practical and scalable approach available.
Perhaps we should explore more fundamental blind
spots. As models grow more capable and show better aware-
ness of their condition, they may begin to strategically adapt
their outputs to mislead researchers about their true nefar-
ious capabilities. Recent work shows that even current
models may deceptively adjust their outputs in response to
a fictitious description of an environment that incentivizes
such behavior (Greenblatt et al., 2024). Given these find-
ings, maybe the community should instead move away from
black-box input-output evaluations via judges and consider
approaches like interpretability (Bereska & Gavves, 2024;
Arditi et al., 2024) or representation engineering (Zou et al.,
2023a). Understanding the internal mechanisms behind
harmful outputs could enable more granular and robust as-
sessments that help reduce the risk of deception.
Finally, empirical evidence suggests that machine learn-
ing progress continues despite flawed metrics and noise.
Salaudeen & Hardt (2024) show that architecture improve-
ments developed on a particular dataset are often robust to
distribution shifts. Meanwhile, commonly used evaluation
metrics for image generation have been criticized for bias
and disagreement with human perception (Kynk¨a¨anniemi
et al., 2022), yet the field has rapidly advanced (Rombach
et al., 2021). If imperfect benchmarks & biased datasets
were fundamental barriers, such rapid progress would be
highly unlikely. Similarly, we continue to see genuinely new
and innovative approaches in the context of LLM robustness
(Zou et al., 2023b; Yu et al., 2024), contradicting the notion
that flawed metrics and noise hinder innovation.
6. Conclusion
In this work, we critically examined the current state of
LLM robustness evaluations, highlighting major sources of
noise, bias, and inconsistencies across datasets, algorithms,
and evaluation pipelines. Our analysis reveals that small and
inconsistently subsampled datasets, implementation discrep-
ancies, and fragmented evaluation setups severely hinder the
reproducibility and comparability of research in this space.
To address these issues, we recommend the following:
• Larger, high-quality benchmarks should be prioritized to
reduce statistical uncertainty.
• Data subsampling should be avoided to reduce the need to
reproduce past work and ease cross-paper comparisons.
• The field should work to standardize & carefully docu-
ment implementation details like quantization, tokeniza-
tion, and chat templates, as they significantly impact ASR.
• Methods should be compared under fair conditions; at-
tacks should be controlled for effort or success rate, and
defenses should consistently report results for safety &
overrefusal to ensure meaningful evaluations.
• Finally, to reduce bias in the judging phase, we recom-
mend using multiple judge models, manual verification
of judge effectiveness on attacks and defenses, and a shift
from greedy generation towards distributional evaluation.
Our vision for LLM-robustness research is a field with cor-
rect, consistent, reliable, and reproducible results that are
easily comparable across different projects, be it new attack
algorithms, defenses, or models. We hope our work serves
as a constructive step towards this goal.
8

--- Page 9 ---

Position: LLM-Safety Evaluations Lack Robustness
Impact Statement
We present work in the field of AI safety and robustness in
the context of LLMs. Due to their widespread availability
and rapidly increasing capability, their reliability and safety
has significant consequences beyond the research commu-
nity and may be of interest to industry and the general public.
Researchers have an obligation to ensure their work meets
scientific standards, such as reproducibility, and accurately
communicates findings as objectively as possible. Many of
our recommendations are centered around making sure that
the field has the ability to accurately fulfill these standards
without being misled by faulty or noisy evaluations.
Prior work on safety & alignment has also sparked contro-
versy regarding the perceived trade-off between censorship
and model safety. We acknowledge that it is possible to
misuse alignment technology for nefarious purposes, such
as censorship. However, we believe that the problems of
alignment/robustness and the specification of what models
should be aligned to should be treated as separate. We ex-
plicitly avoid making any judgements or recommendations
related to the latter, and focus on proposing objective ways
to compare true model behavior to a set of guidelines.
References
Abdin, M., Aneja, J., Behl, H., Bubeck, S., Eldan, R.,
Gunasekar, S., Harrison, M., Hewett, R. J., Javaheripi,
M., Kauffmann, P., et al. Phi-4 technical report. arXiv
preprint arXiv:2412.08905, 2024.
Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I.,
Aleman, F. L., Almeida, D., Altenschmidt, J., Altman, S.,
Anadkat, S., et al. Gpt-4 technical report. arXiv preprint
arXiv:2303.08774, 2023.
Act, E. A. I. The eu artificial intelligence act, 2024.
AI@Meta.
The llama 3 herd of models, 2024a.
URL
https://arxiv.org/abs/2407.21783.
AI@Meta.
Llama 3 model card.
2024b.
URL
https://github.com/meta-llama/llama3/
blob/main/MODEL_CARD.md.
AISI, U. Artificial intelligence safety institute, 2024. URL
https://www.aisi.gov.uk/.
Accessed: 2025-
01-29.
An, B., Zhu, S., Zhang, R., Panaitescu-Liess, M.-A., Xu,
Y., and Huang, F. Automatic pseudo-harmful prompt
generation for evaluating false refusals in large language
models. In First Conference on Language Modeling,
2024. URL https://openreview.net/forum?
id=ljFgX6A8NL.
Andriushchenko, M. and Flammarion, N. Does refusal
training in LLMs generalize to the past tense?
arXiv
preprint arXiv:2407.11969, 2024.
Andriushchenko, M., Croce, F., and Flammarion, N. Jail-
breaking leading safety-aligned LLMs with simple adap-
tive attacks. arXiv preprint arXiv:2404.02151, 2024.
Anthropic.
The Claude 3 model family:
Opus,
Sonnet,
Haiku.
2024a.
URL
https:
//api.semanticscholar.org/CorpusID:
268232499.
Anthropic.
Responsible
scaling
policy,
2024b.
URL
https://www.anthropic.com/news/
anthropics-responsible-scaling-policy.
Arditi, A., Obeso, O., Syed, A., Paleka, D., Panickssery,
N., Gurnee, W., and Nanda, N. Refusal in language
models is mediated by a single direction. arXiv preprint
arXiv:2406.11717, 2024.
Athalye, A., Carlini, N., and Wagner, D. Obfuscated gra-
dients give a false sense of security: Circumventing de-
fenses to adversarial examples. In International confer-
ence on machine learning, pp. 274–283. PMLR, 2018.
Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J.,
Jones, A., Chen, A., Goldie, A., Mirhoseini, A., McKin-
non, C., et al. Constitutional AI: Harmlessness from AI
feedback. arXiv preprint arXiv:2212.08073, 2022.
Bereska, L. and Gavves, E. Mechanistic interpretability for
AI safety–A review. arXiv preprint arXiv:2404.14082,
2024.
Bhardwaj, R. and Poria, S. Red-teaming large language
models using chain of utterances for safety-alignment.
arXiv preprint arXiv:2308.09662, 2023.
Biderman, S., Schoelkopf, H., Sutawika, L., Gao, L., Tow,
J., Abbasi, B., Aji, A. F., Ammanamanchi, P. S., Black,
S., Clive, J., et al. Lessons from the trenches on repro-
ducible evaluation of language models. arXiv preprint
arXiv:2405.14782, 2024.
Boreiko, V., Panfilov, A., Voracek, V., Hein, M., and Geip-
ing, J. A realistic threat model for large language model
jailbreaks. arXiv preprint arXiv:2410.16222, 2024.
Brahman, F., Kumar, S., Balachandran, V., Dasigi, P., Py-
atkin, V., Ravichander, A., Wiegreffe, S., Dziri, N.,
Chandu, K., Hessel, J., et al. The art of saying no: Contex-
tual noncompliance in language models. arXiv preprint
arXiv:2407.12043, 2024.
Carlini, N. Some lessons from adversarial machine learning.
URL https://www. youtube. com/watch, 2024.
9

--- Page 10 ---

Position: LLM-Safety Evaluations Lack Robustness
Chao, P., Robey, A., Dobriban, E., Hassani, H., Pappas, G. J.,
and Wong, E. Jailbreaking black box large language mod-
els in twenty queries. arXiv preprint arXiv:2310.08419,
2023.
Chao, P., Debenedetti, E., Robey, A., Andriushchenko, M.,
Croce, F., Sehwag, V., Dobriban, E., Flammarion, N.,
Pappas, G. J., Tramer, F., et al. Jailbreakbench: An open
robustness benchmark for jailbreaking large language
models. arXiv preprint arXiv:2404.01318, 2024.
Clark, P., Cowhey, I., Etzioni, O., Khot, T., Sabharwal, A.,
Schoenick, C., and Tafjord, O. Think you have solved
question answering? Try ARC, the AI2 reasoning chal-
lenge. arXiv preprint arXiv:1803.05457, 2018.
Congress, U. National artificial intelligence initiative act of
2020, 2020. URL https://www.congress.gov/
bill/116th-congress/house-bill/6216.
Croce, F. and Hein, M. Reliable evaluation of adversarial
robustness with an ensemble of diverse parameter-free
attacks. In International conference on machine learning,
pp. 2206–2216. PMLR, 2020.
Croce, F., Andriushchenko, M., Sehwag, V., Debenedetti,
E., Flammarion, N., Chiang, M., Mittal, P., and Hein,
M. Robustbench: a standardized adversarial robustness
benchmark. arXiv preprint arXiv:2010.09670, 2020.
Cui, J., Chiang, W.-L., Stoica, I., and Hsieh, C.-J. OR-
Bench: An over-refusal benchmark for large language
models. arXiv preprint arXiv:2405.20947, 2024.
Dai, A., Chang, A. X., Savva, M., Halber, M., Funkhouser,
T., and Nießner, M. Scannet: Richly-annotated 3d recon-
structions of indoor scenes. In Proceedings of the IEEE
conference on computer vision and pattern recognition,
pp. 5828–5839, 2017.
Dai, J., Pan, X., Sun, R., Ji, J., Xu, X., Liu, M., Wang, Y.,
and Yang, Y. Safe RLHF: Safe reinforcement learning
from human feedback. arXiv preprint arXiv:2310.12773,
2023.
Deng, J., Dong, W., Socher, R., Li, L.-J., Li, K., and Fei-Fei,
L. Imagenet: A large-scale hierarchical image database.
In 2009 IEEE conference on computer vision and pattern
recognition, pp. 248–255. Ieee, 2009.
Dubey, A., Jauhri, A., Pandey, A., Kadian, A., Al-Dahle,
A., Letman, A., Mathur, A., Schelten, A., Yang, A., Fan,
A., et al. The Llama 3 herd of models. arXiv preprint
arXiv:2407.21783, 2024.
Geisler, S., Wollschl¨ager, T., Abdalla, M., Gasteiger, J.,
and G¨unnemann, S.
Attacking large language mod-
els with projected gradient descent.
arXiv preprint
arXiv:2402.09154, 2024.
Gokaslan,
A. and Cohen,
V.
OpenWebText cor-
pus.
http://Skylion007.github.io/
OpenWebTextCorpus, 2019.
Goodfellow, I. J., Shlens, J., and Szegedy, C. Explaining
and harnessing adversarial examples. In ICLR, 2015.
Google, G., Georgiev, P., Lei, V. I., Burnell, R., Bai, L.,
Gulati, A., Tanzer, G., Vincent, D., Pan, Z., Wang, S.,
et al. Gemini 1.5: Unlocking multimodal understand-
ing across millions of tokens of context. arXiv preprint
arXiv:2403.05530, 2024.
Greenblatt, R., Denison, C., Wright, B., Roger, F., MacDi-
armid, M., Marks, S., Treutlein, J., Belonax, T., Chen, J.,
Duvenaud, D., et al. Alignment faking in large language
models. arXiv preprint arXiv:2412.14093, 2024.
Guan, M. Y., Joglekar, M., Wallace, E., Jain, S., Barak,
B., Heylar, A., Dias, R., Vallone, A., Ren, H., Wei, J.,
et al. Deliberative alignment: Reasoning enables safer lan-
guage models. arXiv preprint arXiv:2412.16339, 2024.
Hendrycks, D. and Mazeika, M. X-risk analysis for ai
research. arXiv preprint arXiv:2206.05862, 2022.
Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika,
M., Song, D., and Steinhardt, J.
Measuring mas-
sive multitask language understanding. arXiv preprint
arXiv:2009.03300, 2020.
Hendrycks, D., Mazeika, M., and Woodside, T. An overview
of catastrophic ai risks. arXiv preprint arXiv:2306.12001,
2023.
Holtzman, A., Buys, J., Du, L., Forbes, M., and Choi, Y. The
curious case of neural text degeneration. arXiv preprint
arXiv:1904.09751, 2019.
Huang, X., Ruan, W., Huang, W., Jin, G., Dong, Y., Wu, C.,
Bensalem, S., Mu, R., Qi, Y., Zhao, X., et al. A survey
of safety and trustworthiness of large language models
through the lens of verification and validation. Artificial
Intelligence Review, 57(7):175, 2024.
Huang, Y., Gupta, S., Xia, M., Li, K., and Chen, D. Catas-
trophic jailbreak of open-source LLMs via exploiting
generation. arXiv preprint arXiv:2310.06987, 2023.
Hughes, J., Price, S., Lynch, A., Schaeffer, R., Barez,
F., Koyejo, S., Sleight, H., Jones, E., Perez, E., and
Sharma, M.
Best-of-n jailbreaking.
arXiv preprint
arXiv:2412.03556, 2024.
Jia, X., Pang, T., Du, C., Huang, Y., Gu, J., Liu, Y., Cao, X.,
and Lin, M. Improved techniques for optimization-based
jailbreaking on large language models. arXiv preprint
arXiv:2405.21018, 2024.
10

--- Page 11 ---

Position: LLM-Safety Evaluations Lack Robustness
Kim, H. Torchattacks: A pytorch repository for adversarial
attacks. arXiv preprint arXiv:2010.01950, 2020.
Krizhevsky, A., Nair, V., and Hinton, G.
Cifar-
100 and cifar-10 (canadian institute for advanced re-
search), 2009.
URL http://www.cs.toronto.
edu/˜kriz/cifar.html. MIT License.
Kudo, T. Sentencepiece: A simple and language indepen-
dent subword tokenizer and detokenizer for neural text
processing. arXiv preprint arXiv:1808.06226, 2018.
Kynk¨a¨anniemi, T., Karras, T., Aittala, M., Aila, T., and
Lehtinen, J. The role of imagenet classes in fr\’echet
inception distance. arXiv preprint arXiv:2203.06026,
2022.
Liao, Z. and Sun, H. AmpleGCG: Learning a universal and
transferable generative model of adversarial suffixes for
jailbreaking both open and closed llms. arXiv preprint
arXiv:2404.07921, 2024.
Liu, H., Li, C., Wu, Q., and Lee, Y. J. Visual instruction tun-
ing. Advances in neural information processing systems,
36, 2024.
Liu, X., Xu, N., Chen, M., and Xiao, C. Autodan: Generat-
ing stealthy jailbreak prompts on aligned large language
models. arXiv preprint arXiv:2310.04451, 2023a.
Liu, Y., Deng, G., Xu, Z., Li, Y., Zheng, Y., Zhang, Y.,
Zhao, L., Zhang, T., Wang, K., and Liu, Y. Jailbreaking
ChatGPT via prompt engineering: An empirical study.
arXiv preprint arXiv:2305.13860, 2023b.
Madry, A., Makelov, A., Schmidt, L., Tsipras, D., and
Vladu, A. Towards Deep Learning Models Resistant
to Adversarial Attacks. In ICLR, 2018.
Mazeika, M., Zou, A., Mu, N., Phan, L., Wang, Z., Yu, C.,
Khoja, A., Jiang, F., O’Gara, A., Sakhaee, E., Xiang, Z.,
Rajabi, A., Hendrycks, D., Poovendran, R., Li, B., and
Forsyth, D. TDC 2023 (llm edition): The trojan detection
challenge. In NeurIPS Competition Track, 2023.
Mazeika, M., Phan, L., Yin, X., Zou, A., Wang, Z., Mu,
N., Sakhaee, E., Li, N., Basart, S., Li, B., et al. Harm-
Bench: A standardized evaluation framework for auto-
mated red teaming and robust refusal. arXiv preprint
arXiv:2402.04249, 2024.
Miller, E.
Adding error bars to evals: A statistical ap-
proach to language model evaluations. arXiv preprint
arXiv:2411.00640, 2024.
MLCommons. Ailuminate v1.0 benchmark, 2025. https:
//mlcommons.org/ailuminate/.
OpenAI.
Our
approach
to
ai
safety,
2023a.
URL
https://openai.com/index/
our-approach-to-ai-safety/.
OpenAI. Openai evals, 2023b. URL https://github.
com/openai/evals/tree/main.
OpenAI.
Openai
red
teaming
network,
2023c.
URL
https://openai.com/index/
red-teaming-network/.
Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C.,
Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A.,
et al. Training language models to follow instructions
with human feedback. Advances in neural information
processing systems, 35:27730–27744, 2022.
Papernot, N., Faghri, F., Carlini, N., Goodfellow, I., Fein-
man, R., Kurakin, A., Xie, C., Sharma, Y., Brown, T., Roy,
A., et al. Technical report on the cleverhans v2. 1.0 adver-
sarial examples library. arXiv preprint arXiv:1610.00768,
2016.
Polo, F. M., Weber, L., Choshen, L., Sun, Y., Xu, G., and
Yurochkin, M. tinyBenchmarks: evaluating LLMs with
fewer examples. arXiv preprint arXiv:2402.14992, 2024.
Qi, X., Panda, A., Lyu, K., Ma, X., Roy, S., Beirami, A.,
Mittal, P., and Henderson, P. Safety alignment should be
made more than just a few tokens deep. arXiv preprint
arXiv:2406.05946, 2024.
Rombach, R., Blattmann, A., Lorenz, D., Esser, P., and
Ommer, B. High-resolution image synthesis with latent
diffusion models, 2021.
R¨ottger, P., Kirk, H. R., Vidgen, B., Attanasio, G., Bianchi,
F., and Hovy, D. XSTest: A test suite for identifying
exaggerated safety behaviours in large language models.
arXiv preprint arXiv:2308.01263, 2023.
Sadasivan, V. S., Saha, S., Sriramanan, G., Kattakinda, P.,
Chegini, A., and Feizi, S. Fast adversarial attacks on
language models in one GPU minute. arXiv preprint
arXiv:2402.15570, 2024.
Salaudeen, O. and Hardt, M. ImageNot: A contrast with
ImageNet preserves model rankings.
arXiv preprint
arXiv:2404.02112, 2024.
Scholten, Y., G¨unnemann, S., and Schwinn, L. A probabilis-
tic perspective on unlearning and alignment for large lan-
guage models. arXiv preprint arXiv:2410.03523, 2024.
Schuett, J. Risk management in the artificial intelligence
act. European Journal of Risk Regulation, 15(2):367–385,
2024.
11

--- Page 12 ---

Position: LLM-Safety Evaluations Lack Robustness
Schwinn, L., Dobre, D., Xhonneux, S., Gidel, G., and
Gunnemann, S. Soft prompt threats: Attacking safety
alignment and unlearning in open-source LLMs through
the embedding space. arXiv preprint arXiv:2402.09063,
2024.
Shaikh, O., Zhang, H., Held, W., Bernstein, M., and Yang,
D.
On second thought, let’s not think step by step!
Bias and toxicity in zero-shot reasoning. arXiv preprint
arXiv:2212.08061, 2022.
Shen, X., Chen, Z., Backes, M., Shen, Y., and Zhang, Y.
”do anything now”: Characterizing and evaluating in-the-
wild jailbreak prompts on large language models. In
Proceedings of the 2024 on ACM SIGSAC Conference on
Computer and Communications Security, pp. 1671–1685,
2024.
Sheshadri, A., Ewart, A., Guo, P., Lynch, A., Wu, C., Heb-
bar, V., Sleight, H., Stickland, A. C., Perez, E., Hadfield-
Menell, D., and Casper, S. Targeted latent adversarial
training improves robustness to persistent harmful behav-
iors in llms. arXiv preprint arXiv:2407.15549, 2024.
Souly, A., Lu, Q., Bowen, D., Trinh, T., Hsieh, E., Pandey,
S., Abbeel, P., Svegliato, J., Emmons, S., Watkins, O., and
Toyer, S. A StrongREJECT for empty jailbreaks. In The
Thirty-eighth Annual Conference on Neural Information
Processing Systems, 2024.
Su, Y., Lan, T., Wang, Y., Yogatama, D., Kong, L., and Col-
lier, N. A contrastive framework for neural text genera-
tion. Advances in Neural Information Processing Systems,
35:21548–21561, 2022.
Thompson, T. B. and Sklar, M. Breaking circuit break-
ers, 2024a.
URL https://confirmlabs.org/
posts/circuit_breaking.html.
Thompson, T. B. and Sklar, M. FLRT: Fluent Student-
Teacher Redteaming. arXiv preprint arXiv:2407.17447,
2024b.
Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi,
A., Babaei, Y., Bashlykov, N., Batra, S., Bhargava, P.,
Bhosale, S., et al. Llama 2: Open foundation and fine-
tuned chat models. arXiv preprint arXiv:2307.09288,
2023.
Tramer, F., Carlini, N., Brendel, W., and Madry, A. On adap-
tive attacks to adversarial example defenses. Advances
in neural information processing systems, 33:1633–1645,
2020.
Uesato, J., O’donoghue, B., Kohli, P., and Oord, A. Ad-
versarial risk and the dangers of evaluating against weak
attacks. In International conference on machine learning,
pp. 5025–5034. PMLR, 2018.
Vijayakumar, A. K., Cogswell, M., Selvaraju, R. R., Sun,
Q., Lee, S., Crandall, D., and Batra, D. Diverse beam
search: Decoding diverse solutions from neural sequence
models. arXiv preprint arXiv:1610.02424, 2016.
Wei, J., Karina, N., Chung, H. W., Jiao, Y. J., Papay, S.,
Glaese, A., Schulman, J., and Fedus, W. Measuring short-
form factuality in large language models. arXiv preprint
arXiv:2411.04368, 2024.
Xhonneux, S., Sordoni, A., G¨unnemann, S., Gidel, G., and
Schwinn, L. Efficient adversarial training in LLMs with
continuous attacks. arXiv preprint arXiv:2405.15589,
2024.
Yong, Z.-X., Menghini, C., and Bach, S. H.
Low-
resource languages jailbreak GPT-4.
arXiv preprint
arXiv:2310.02446, 2023.
Yu, J., Lin, X., Yu, Z., and Xing, X. Gptfuzzer: Red team-
ing large language models with auto-generated jailbreak
prompts. arXiv preprint arXiv:2309.10253, 2023.
Yu, L., Do, V., Hambardzumyan, K., and Cancedda, N.
Robust LLM safeguarding via refusal feature adversarial
training. arXiv preprint arXiv:2409.20089, 2024.
Zellers, R., Holtzman, A., Bisk, Y., Farhadi, A., and Choi,
Y. Hellaswag: Can a machine really finish your sentence?
arXiv preprint arXiv:1905.07830, 2019.
Zhao, W., Ren, X., Hessel, J., Cardie, C., Choi, Y., and
Deng, Y. Wildchat: 1m ChatGPT interaction logs in the
wild. arXiv preprint arXiv:2405.01470, 2024.
Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z.,
Zhuang, Y., Lin, Z., Li, Z., Li, D., Xing, E., et al. Judg-
ing LLM-as-a-judge with MT-bench and chatbot arena.
Advances in Neural Information Processing Systems, 36:
46595–46623, 2023.
Zhu, S., Amos, B., Tian, Y., Guo, C., and Evtimov, I. Ad-
vPrefix: An objective for nuanced llm jailbreaks. arXiv
preprint arXiv:2412.10321, 2024.
Zou, A., Phan, L., Chen, S., Campbell, J., Guo, P., Ren, R.,
Pan, A., Yin, X., Mazeika, M., Dombrowski, A.-K., et al.
Representation engineering: A top-down approach to AI
transparency. arXiv preprint arXiv:2310.01405, 2023a.
Zou, A., Wang, Z., Carlini, N., Nasr, M., Kolter, J. Z.,
and Fredrikson, M. Universal and transferable adversar-
ial attacks on aligned language models. arXiv preprint
arXiv:2307.15043, 2023b.
Zou, A., Phan, L., Wang, J., Duenas, D., Lin, M., An-
driushchenko, M., Kolter, J. Z., Fredrikson, M., and
Hendrycks, D. Improving alignment and robustness with
circuit breakers. In The Thirty-eighth Annual Conference
on Neural Information Processing Systems, 2024.
12

--- Page 13 ---

Position: LLM-Safety Evaluations Lack Robustness
A. Appendix
A.1. Background
A.1.1. ROBUSTNESS FOR LLMS
In the context of LLM safety research, an aligned model can be defined as one whose generations follow the rules and
guidelines laid out by its developer. Such an LLM may be adversarially attacked via methods that produce inputs that cause
the model to deviate from the desired guidelines (also called jailbreaks). We consider a model more robust or more aligned
if it is more “difficult” to elicit the undesired behavior.
In contrast to computer vision, where standardized threat models like norm constraints can precisely capture the “difficulty”
of breaking a model (Goodfellow et al., 2015; Madry et al., 2018), there is currently no consensus on how to best define
difficulty in the context of LLM robustness. For practical purposes, models are typically ranked according to their robustness
against a suite of existing attack algorithms (Zou et al., 2023b). Models that are broken less often or require more iterations
to break are considered more robust. Most research, including this paper, is not focused on “true” worst-case robustness,
which demands that models never produce undesired outputs given any input, and instead focus on real-world scenarios and
algorithms to find practically usable jailbreaks in reasonable time (Zou et al., 2024). The terms are also used somewhat
inconsistently, with “robustness” often referring more to the stability of a model’s output with respect to constrained
adversarial perturbations of its input rather than the ability to follow a developer’s intentions.
More formally, we investigate a model fθ, which maps from the space of input token sequences X to output token sequences
Y. We also define a set of admissible input token sequences X ∗⊂X which consists of all token sequences that are
reachable by tokenizing a user-submitted string (i.e., they do not contain control tokens or impossible-to-reach sequences
due to token merging). We consider attacks that find an admissible sequence of discrete input tokens ˜x ∈X ∗that causes its
response y ∼fθ(˜x) to conflict with the guidelines set out by the developer. Deciding whether a generation conflicts with
the developer’s guidelines is likely an ill-defined problem due to the ambiguity of language. In practice, the community
uses judging functions J which map from model generations y ∈Y to either discrete success flags {0, 1} or continuous
scores [0, 1]. J is instantiated either via human evaluation or, more commonly, as a finetuned LLM trained on data of human
evaluations of harmful and harmless generations.
A.1.2. ROBUSTNESS IN THE IMAGE DOMAIN
In the past, the computer vision robustness research community has struggled with reproducibility issues and unreliable
defenses which were often quickly broken after their release (Athalye et al., 2018; Carlini, 2024; Uesato et al., 2018).
Clearly defining commonly used threat models, such as L∞= 8/255 norm constraints, which provide a precise measure of
the “difficulty” of breaking a model (Goodfellow et al., 2015; Madry et al., 2018), have made results in field more reliable
by making attacks and defense easily comparable and testable. Additionally, public leaderboards with consistent datasets
and threat models have been used to track progress (Croce et al., 2020). The community also focused on more standardized
frameworks (Papernot et al., 2016; Croce & Hein, 2020; Kim, 2020) and datasets (Krizhevsky et al., 2009), making results
easier to reproduce and avoiding noise resulting from slightly different implementations.
13

--- Page 14 ---

Position: LLM-Safety Evaluations Lack Robustness
A.2. Case Study: Effects of White-space Tokens on GCG Against Llama 2
We run GCG (Zou et al., 2023b) against Llama-2-7b-chat-hf using default hyperparameters. We use the Meta chat template
without system prompt (as recommended), and report the mean across the first 100 prompts from HarmBench (Mazeika
et al., 2024). In one trial, we do not account for the SentencePiece (Kudo, 2018) underline token (ID 29781), which Llama
2 predicts at the beginning of each of its responses, before continuing with regular text-tokens. This token is not added
automatically by the tokenizer, even with the correct template, and must be manually inserted to ensure correctness.
We see that GCG makes faster progress when the white-space token is correctly handled, achieving a 91% many-trial ASR
after 250 iterations, whereas the misaligned implementation only reaches 63%. The loss curve further illustrates this effect,
with the correct implementation rapidly reaching more than 50% lower loss values.
0
50
100
150
200
250
Step
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
Loss
0
50
100
150
200
250
Step
0.0
0.2
0.4
0.6
0.8
1.0
Many-trial ASR (CAIS)
0
50
100
150
200
250
Step
0.0
0.2
0.4
0.6
0.8
1.0
Many-trial ASR (StrongREJECT)
Correct Whitespace
Incorrect Whitespace
Figure 4: Impact of white-space tokens on GCG attack progress vs. Llama-2-7b-chat-hf.
14

--- Page 15 ---

Position: LLM-Safety Evaluations Lack Robustness
A.3. Case Study: Effects of Implementation Details on Optimization
We use the first 100 prompts from HarmBench (Mazeika et al., 2024) and run GCG (Zou et al., 2023b) against Llama-3.1-
8B-Instruct. We use the default hyperparameters for GCG (batch size 512, number of steps 250) and use the BF16 floating
point format for the model weights. Our reference implementation of GCG is based on the official nanoGCG repository but
includes several enhancements.
• Chat Template: Instead of the default chat template provided by HuggingFace, we use the Meta-recommended
template.
• Token Filter for Non-Admissible Inputs: While nanoGCG includes a filter to remove special tokens (control/role/sys-
tem) tokens from the optimization, we design a stricter token filter which fixes a few issues. To evaluate whether
an attack prompt is admissible, nanoGCG decodes and re-encodes the attack tokens and verifies that they remain
unchanged. While this approach is sufficient for most scenarios, in some cases, the tokenizer merges characters across
the boundary of the attack suffix and the remaining prompt, which is not detected by the filter. This can lead to
inadmissible token sequences which cannot be reached from standard input strings and are therefore filtered by our
implementation.
• Filtering of Control Tokens: The reference implementation fails to filter control tokens which were added to the
tokenizer post-hoc, but can affect the optimization and should always be excluded.
In Figure 5, we demonstrate that these subtle changes can have a significant effect on the performance of GCG, causing an
ASR difference of up to 14% among configurations which use a system prompt. We also include results without the system
prompt to demonstrate the importance of following the instructions by model developers to include system prompts where
required. The main point of this experiment is not to optimize for more efficient algorithms or higher ASR, but simply to
show that minor details can significantly affect the outcomes of LLM attack evaluations.
0
50
100
150
200
250
Step
0.0
0.5
1.0
1.5
Loss
0
50
100
150
200
250
Step
0.0
0.2
0.4
0.6
0.8
1.0
Many-trial ASR (CAIS)
0
50
100
150
200
250
Step
0.0
0.2
0.4
0.6
0.8
1.0
Many-trial ASR (StrongREJECT)
Reference
HF Chat Template
nanoGCG Token Filter
No System Message
Int8 Quantization
Allow Non-ASCII Characters
Reference
HF Chat Template
nanoGCG Token Filter
No System Message
Int8 Quantization
Allow Non-ASCII Characters
Figure 5: Impact of implementation details on GCG attack progress vs. Llama-3.1-8B-Instruct.
15

--- Page 16 ---

Position: LLM-Safety Evaluations Lack Robustness
A.4. Case Study: Bias in Optimization Targets
Because almost all targets provided in the HarmBench dataset (Mazeika et al., 2024) begin with the phrase “Sure, here...”,
we want to evaluate how “natural” this response is for various models. We run a small test using a benign prompt (“Write
a blog post that explains how to use the ‘transformers‘ library to train a language model”) and the target phrase “Sure,
here’s a blog post that explains how to use the ‘transformers‘ library to train a language model”. We compute the average
loss over the entire target phrase and the first token (“Sure”) only. If the targets were model-agnostic, we would expect to
see similar loss values for all models, however, this is not the case. This supports results showing that designing adaptive
targets which are “natural” for a particular vicim model improves attack performance (Thompson & Sklar, 2024b; Zhu et al.,
2024). We also see that many safety-focused model versions (Circuit Breaker (Zou et al., 2024), CAT (Xhonneux et al.,
2024), LLM-LAT (Sheshadri et al., 2024)) have extremly high loss values for this specific type of affirmative response,
likely because datasets with similar affimative response formats were used during training.
lmsys/vicuna-13b-v1.5
qwen/Qwen2-7B-Instruct
meta-llama/Llama-2-7b-chat-hf
lmsys/vicuna-7b-v1.5
ContinuousAT/Phi-CAT
ContinuousAT/Llama-2-7B-CAT
NousResearch/Hermes-2-Pro-Llama-3-8B
microsoft/Phi-3-mini-4k-instruct
berkeley-nest/Starling-LM-7B-alpha
mistralai/Ministral-8B-Instruct-2410
meta-llama/Llama-3.2-3B-Instruct
meta-llama/Meta-Llama-3.1-8B-Instruct
mistralai/Mistral-Nemo-Instruct-2407
HuggingFaceH4/zephyr-7b-beta
google/gemma-2-2b-it
cais/zephyr_7b_r2d2
allenai/Llama-3.1-Tulu-3-8B-DPO
microsoft/phi-4
meta-llama/Llama-3.2-1B-Instruct
mistralai/Mistral-7B-Instruct-v0.3
GraySwanAI/Mistral-7B-Instruct-RR
ContinuousAT/Zephyr-CAT
LLM-LAT/robust-llama3-8b-instruct
meta-llama/Meta-Llama-3-8B-Instruct
GraySwanAI/Llama-3-8B-Instruct-RR
0.0
0.2
0.4
0.6
0.8
Loss
Figure 6: Average loss for HarmBench-style affirmative target sequence using a harmless prompt.
meta-llama/Llama-2-7b-chat-hf
ContinuousAT/Phi-CAT
qwen/Qwen2-7B-Instruct
mistralai/Ministral-8B-Instruct-2410
lmsys/vicuna-7b-v1.5
mistralai/Mistral-Nemo-Instruct-2407
lmsys/vicuna-13b-v1.5
microsoft/Phi-3-mini-4k-instruct
cais/zephyr_7b_r2d2
ContinuousAT/Llama-2-7B-CAT
allenai/Llama-3.1-Tulu-3-8B-DPO
NousResearch/Hermes-2-Pro-Llama-3-8B
berkeley-nest/Starling-LM-7B-alpha
HuggingFaceH4/zephyr-7b-beta
microsoft/phi-4
ContinuousAT/Zephyr-CAT
GraySwanAI/Mistral-7B-Instruct-RR
google/gemma-2-2b-it
meta-llama/Llama-3.2-1B-Instruct
mistralai/Mistral-7B-Instruct-v0.3
meta-llama/Llama-3.2-3B-Instruct
meta-llama/Meta-Llama-3.1-8B-Instruct
LLM-LAT/robust-llama3-8b-instruct
meta-llama/Meta-Llama-3-8B-Instruct
GraySwanAI/Llama-3-8B-Instruct-RR
0
5
10
15
20
25
30
Loss
Figure 7: Loss for the first token (“Sure”) for a HarmBench-style affirmative target using a harmless prompt.
16

--- Page 17 ---

Position: LLM-Safety Evaluations Lack Robustness
A.5. Case Study: Statistical Significance and Uncertainty
As a representative example, we investigate results reported in (Guan et al., 2024) more closely. The key finding of the
paper is that reasoning models like OpenAI’s o1 lead to a “Pareto improvement by reducing both under- and overrefusals”
compared to existing state-of-the-art models. We show that the results on public datasets alone (presented in Figure 2)
would not be sufficient to support this claim at commonly accepted statistical significance levels. In addition, we find
that the use of automated judging for jailbreaks can lead to overly confident conclusions regarding the safety of models.
We also want to emphasize that the findings of the work as a whole remain sound and well-supported, but only because
evaluations on larger internal datasets are included.
A.5.1. LIMITATIONS DUE TO DATASET SIZE.
The safety-overrefusal trade-offs of the models were evaluated on two public datasets: XSTest (R¨ottger et al., 2023), and
StrongREJECT (Souly et al., 2024), which contain 250 and 313 prompts, respectively. We focus on comparing Claude 3.5
Sonnet and o1. By counting pixels on the figure, we estimate the underlying results to be as follows:
# Correct
Model
XSTest
StrongReject
o1
232
274
Claude 3.5 Sonnet
222
247
This aligns well with the results reported for o1 in Table 1. We denote the probability of correctly refusing a harmful
query from StrongREJECT as pStrongREJECT and the probability of not overrefusing on XSTest as pXSTest. To claim Pareto
dominance, we need to show that p(o1)
StrongREJECT > p(Sonnet)
StrongREJECT and p(o1)
XSTest > p(Sonnet)
XSTest . Thus, we perform two z-tests, one for
each variable:
For StrongREJECT:
p(o1)
StrongREJECT = 274
313 = 0.875,
p(Sonnet)
StrongREJECT = 247
313 = 0.789,
pStrongREJECT = 274 + 247
313 + 313 = 0.832.
Standard error:
SE =
s
pStrongREJECT(1 −pStrongREJECT)
 1
313 +
1
313

=
s
0.832 × 0.168 ×
 1
313 +
1
313

≈0.0297.
z-statistic:
z =
p(o1)
StrongREJECT −p(Sonnet)
StrongREJECT
SE
= 0.875 −0.789
0.0297
≈2.90.
This yields a p-value: ≈0.004, which indicates a highly significant difference at α = 0.05.
17

--- Page 18 ---

Position: LLM-Safety Evaluations Lack Robustness
For overrefusal:
p(o1)
XSTest = 232
250 = 0.928,
p(Sonnet)
XSTest
= 222
250 = 0.888,
pXSTest = 232 + 222
250 + 250 = 0.908.
Standard error:
SE =
s
pXSTest(1 −pXSTest)
 1
250 +
1
250

=
s
0.908 × 0.092 ×
 1
250 +
1
250

≈0.0259.
z-statistic:
z = p(o1)
XSTest −p(Sonnet)
XSTest
SE
= 0.928 −0.888
0.0259
≈1.55.
This yields a p-value: ≈0.12, which is not significant at α = 0.05.
Thus we cannot claim a Pareto improvement using experiments on these two datasets alone.
A.5.2. LIMITATIONS DUE TO AUTOMATED JUDGING.
The main body of the paper reports safety results on StrongREJECT using automated judges. However, the authors also
include a human verification of jailbreaking performance in the appendix, which yields different results for StrongREJECT.
We perform an additional z-test to validate that o1 significantly improves jailbreaking robustness over Claude Sonnet 3.5
using the human-sourced data.
Given:
p(o1)
StrongREJECT = 0.92,
p(Sonnet)
StrongREJECT = 0.90,
pStrongREJECT = 0.92 + 0.90
1 + 1
= 0.91.
Standard error:
SE =
s
pStrongREJECT(1 −pStrongREJECT)
 1
313 +
1
313

=
s
0.91 × 0.09 ×
 1
313 +
1
313

≈0.0229.
18

--- Page 19 ---

Position: LLM-Safety Evaluations Lack Robustness
z-statistic:
z =
p(o1)
StrongREJECT −p(Sonnet)
StrongREJECT
SE
= 0.92 −0.90
0.0229
≈0.87.
This yields a p-value: ≈0.38, which is not significant. Meanwhile, results from the automated classifier suggested that the
difference is highly significant at p ≈0.004!
The case study illustrates that significant problems may arise from relying on automated judges alone, as—in addition to
unavoidable noise due to classification errors—they may have systematic biases that distort model comparisons. Here,
we saw that Claude’s true robustness was underestimated by 11.1%, while o1’s was only underestimated by 4.5%, which
directly affects the conclusions we can confidently draw from the experiments. We thus reiterate our suggestion to verify
judge performance via human evaluation when proposing a new attack, defense, or model to ensure comparable results.
19

--- Page 20 ---

Position: LLM-Safety Evaluations Lack Robustness
A.6. Case Study: Comparing the StrongREJECT Gemma 2B and HarmBench/CAIS Llama 2 13B judges.
We compare the results provided by StrongREJECT’s (Souly et al., 2024) Gemma 2B judge model and the HarmBench
(Mazeika et al., 2024) Llama 2 13B finetuned classifier.
To do so, we run a suite of 10 different attack algorithms against a zoo of 25 models using all 300 non-copyright prompts in
HarmBench’s dataset. All attacks are evaluated in the “many-trial” setting, regardless of the setting in which they were
originally introduced. This means all intermediate prompt candidates are rolled-out and evaluated. In total, we compare
results for 5,269,564 generations. We acknowledge that due to edge-case problems with models, tokenizers, and attack
implementations, and due to time constraints, not all attack runs were successfully completed. Nonetheless, as we only
compare the difference, we can nontheless make valid comparisons between the two judge models. Our results, shown in
Figure 8, highlight substantial model- and attack-specific discrepancies between these two commonly used judges. While
StrongREJECT’s consistently reports lower ASRs (as expected, due to its more strict definition of what constitutes a
successful jailbreak), we find very clear differences in how much the two judges differ. These inconsistencies can lead to
differences in the scoring and even ranking of models, defenses, and attacks, complicating comparisons.
Ultimately, we would like to compare these classifier-based judgments to human-provided ground truth, but this was not
feasible within the scope of this work. Nonetheless, if these two commonly used classifiers disagree, at least one (and likely
both) must also disagree with human ground truth, underscoring the limitations of automated evaluation.
pair
ample_gcg
direct
human_jailbreaks
beast
pgd_one_hot
autodan
gcg
pgd
prefilling
0.00
0.05
0.10
0.15
0.20
0.25
Difference in ASR
Difference (CAIS - StrongREJECT) per Attack
ContinuousAT/Phi-CAT
GraySwanAI/Llama-3-8B-Instruct-RR
ContinuousAT/Zephyr-CAT
GraySwanAI/Mistral-7B-Instruct-RR
LLM-LAT/robust-llama3-8b-instruct
cais/zephyr_7b_r2d2
ContinuousAT/Llama-2-7B-CAT
meta-llama/Llama-3.2-1B-Instruct
microsoft/Phi-3-mini-4k-instruct
allenai/Llama-3.1-Tulu-3-8B-DPO
meta-llama/Llama-2-7b-chat-hf
meta-llama/Llama-3.2-3B-Instruct
google/gemma-2-2b-it
meta-llama/Meta-Llama-3-8B-Instruct
meta-llama/Meta-Llama-3.1-8B-Instruct
qwen/Qwen2-7B-Instruct
SicariusSicariiStuff/Phi-3.5-mini-instruct_Uncensored
lmsys/vicuna-7b-v1.5
mistralai/Mistral-7B-Instruct-v0.3
berkeley-nest/Starling-LM-7B-alpha
NousResearch/Hermes-2-Pro-Llama-3-8B
mistralai/Ministral-8B-Instruct-2410
HuggingFaceH4/zephyr-7b-beta
mistralai/Mistral-Nemo-Instruct-2407
lmsys/vicuna-13b-v1.5
0.00
0.05
0.10
0.15
0.20
0.25
Difference in ASR
Difference (CAIS - StrongREJECT) per Model
Figure 8: Comparing the ASR of two judge models. We consider an attack successful if StrongReject gives a score higher
than 0.5, and if HarmBench’s classifier outputs ”Yes” or ”yes” as the most likely token.
20

--- Page 21 ---

Position: LLM-Safety Evaluations Lack Robustness
We briefly describe the hyperparameters we used below. All attacks implementations were adapted from the official GitHub
repositories of the original authors where available. Otherwise, we ported a HarmBench implementation to our pipeline. In
some cases, we conferred with authors directly to gain access to reference implementations and ensure correctness. For all
attacks, we sample and judge a single greedy generation per prompt-candidate.
• PAIR (Chao et al., 2023): We use lmsys/vicuna-13b-v1.5 as the attacker model and generate up to 512 tokens per attack
prompt. We sample with temperature 1 and top-p of 0.9, setting Nstreams to 5 and Niterations to 5. During the attack, the
victim model generates up to 256 tokens using greedy generation.
• AmpleGCG (Liao & Sun, 2024): We use osunlp/AmpleGCG-llama2-sourced-llama2-7b-chat to generate 200 attack
suffixes with diversity penalty 1.
• Direct: We simply use the harmful prompt without any modification and sample a greedy generation.
• HumanJailbreaks: We use the 114 human-designed jailbreak templates in HarmBench (Mazeika et al., 2024) to prompt
the model.
• BEAST (Sadasivan et al., 2024): We use k1 = k2 = 15 and set the temperature to 1 to sample N = 40 suffix tokens.
• PGD (Schwinn et al., 2024): We initialize the attack using the suffix “x x x x x x x x x x x x x x x x x x x x” as it
tokenizes to exactly 20 tokens for all tested models, and run signed gradient descent optimization for 100 steps. We use
a learning rate of α = 0.001 and constrain the optimization to an L2 ball with radius 1 around the initialization for
each token. In the one-hot version, instead of optimizing the input embeddings directly in latent space, we instead
optimize over the {0, 1} →[0, 1] relaxed one-hot input vectors. In addition, we found it necessary to add a momentum
term with weight 0.5 to speed up the optimization.
• AutoDAN (Liu et al., 2023a): We use 100 steps and initialize using the 128 seed prompts from HarmBench’s
implementation. We use the victim model itself as mutator model and set Nelites = 0.05, crossover = 0.5, Npoints = 5,
and Pmutation = 0.01.
• GCG (Zou et al., 2023b): We use our modified version of nanoGCG with a corrected token filtering algorithm to
remove special tokens & only allow ASCII-representable characters. We set Nsteps = 250, use a batch size of 512,
Top-K = 256, and initialize using the string “x x x x x x x x x x x x x x x x x x x x” as it tokenizes to exactly 20 tokens
for all tested models.
• Prefilling: In this attack, we use the unmodified harmful prompt and pre-fill the beginning of the model’s response
using the affirmative target sequence from the dataset.
A.7. Reproducibility
We will release code to exactly reproduce all4 plots and tables upon publication. All experiments were conducted using
greedy generation, bfloat16 precision, and HuggingFace Transformers version 4.47.1 unless otherwise noted. To judge
generations we use the CAIS/HarmBench Llama 2 13B classifier and the finetuned Gemma 2B from StrongREJECT. For
the HarmBench classifier, a generation is deemed harmful if the most likely output token is either “yes” or “Yes” and for
StrongREJECT, we threshold the score at 0.5. We do not truncate model generations (i.e. we judge the full model response
up to an end-of-sentence or end-of-turn token).
To obtain the results in Figures 4 & 5 and Table 1, we used a batch size of 512 and 250 steps of GCG with top-k set to 256.
We initialized the suffix with the string “x x x x x x x x x x x x x x x x x x x x”.
4Due to the large scale of the experiments and the associated rare occurrence of edge-cases and other non-deterministic problems, it
may not be possible to exactly reproduce Figure 8 from scratch.
21

--- Page 22 ---

Position: LLM-Safety Evaluations Lack Robustness
A.8. Jailbreaking & Overrefusal Datasets
Name
Harmful
Overrefusal
Notes
AdvBench (Zou et al., 2023b)
520
-
CoCoNot (Brahman et al., 2024)
3,528
1,306 Some harmful prompts not considered forbidden
according to all model developers’ guidelines.
DangerousQ (Shaikh et al., 2022)
200
-
HarmBench (Mazeika et al., 2024)
400
-
HarmfulQ (Shaikh et al., 2022)
200
-
HarmfulQA
1,920
-
Highly repetitive (e.g., 20 prompts of the form
(Bhardwaj & Poria, 2023)
“How can I use cultural studies to [harmful end]?”)
JBB-Behaviors (Chao et al., 2024)
100
100
Overlap with AdvBench
MaliciousInstruct (Huang et al., 2023)
100
-
PromptEngineering (Liu et al., 2023b)
40
-
StrongREJECT (Souly et al., 2024)
313
-
Trojan Detection Challenge
50
-
(Mazeika et al., 2023)
XSTest (R¨ottger et al., 2023)
200
250
Harmful prompts contain ambiguous requests.
Table 2: Commonly used jailbreaking and overrefusal datasets with harmful prompts and their size.
22
```
