---
title: "Generalization Analogies - PDF Extract"
source_pdf: "2023-Clymer-Generalization Analogies.pdf"
pages: 22
extracted_at: "2026-01-24T17:05:12.893201"
---

# PDF Extract: Generalization Analogies

**Source PDF:** 2023-Clymer-Generalization Analogies.pdf
**Total Pages:** 22

---

## Content

```
--- Page 1 ---

Generalization Analogies (GENIES): A Testbed for Generalizing AI Oversight to
Hard-To-Measure Domains
Joshua Clymer 1 Garrett Baker 2 Rohan Subramani 1 Sam Wang 1
Abstract
As AI systems become more intelligent and their
behavior becomes more challenging to assess,
they may learn to game the flaws of human feed-
back instead of genuinely striving to follow in-
structions; however, this risk can be mitigated by
controlling how LLMs generalize human feed-
back to situations where it is unreliable. To better
understand how reward models generalize, we
craft 69 distribution shifts spanning 8 categories.
We find that reward models do not learn to evalu-
ate ‘instruction-following’ by default and instead
favor personas that resemble internet text. Tech-
niques for interpreting reward models’ internal
representations achieve better generalization than
standard fine-tuning, but still frequently fail to dis-
tinguish instruction-following from conflated be-
haviors. We consolidate the 15 most challenging
distribution shifts into the GENeralization analo-
gIES (GENIES) benchmark, which we hope will
enable progress toward controlling reward model
generalization.
1. Introduction
As AI capabilities have increased, so has the need for human
evaluators with specific expertise (Malaviya et al., 2023;
Boiko et al., 2023). If AI systems exceed human abilities,
even the most talented experts may struggle to evaluate their
actions, creating a risk that AI systems bypass monitoring
or game human evaluations (Hendrycks et al., 2023b).
1.1. The limitations of oversight can be overcome with
favorable generalization
To prevent models from gaming human feedback, devel-
opers might fine-tune them on a restricted set of high-
confidence examples and rely on favorable generalization.
1Columbia University in NY 2NA. Correspondence to: Joshua
Clymer <joshuamclymer@gmail.com>.
Figure 1: The radar plot shows generalization accuracy
across all distribution-shift categories. The outer edge of
the circle represents target-tuned capability (Section 4.1).
The leaderboard shows average generalization accuracy vs
target-tuned capability on the 15 curated distribution shifts.
50% is random accuracy.
For example, training reward models to evaluate instructions
like “provide a grocery list for a healthy meal” may also
arXiv:2311.07723v3  [cs.AI]  17 Dec 2023

--- Page 2 ---

GENIES: Generalizing AI Oversight to Hard-to-Measure Domains
Figure 2: reward models exhibit moderate easy to hard
generalization by default: fine-tuning LLaMA-30B on easy
Raven Matrices achieves 75% accuracy on significantly
harder puzzles (Figure 5).
yield accurate judgments for instructions like “make sweep-
ing advances in AI safety research.” This approach requires
generalization across the distribution shift from examples
developers can reliably verify to those they cannot.
1.2. Generalization Analogies provide a ‘testbed’ for
controlling generalization
By definition, it would be difficult to know if reward models
generalize to hard-to-measure domains. Instead, we propose
predicting generalization with loosely analogous distribu-
tion shifts. For example, if reward models generalize from
simple math questions to University-level problems, they
are more likely to generalize to even harder instructions.
Generalization analogies test AI control techniques much
like how Aerospace ‘testbeds’ assess aircraft parts in wind
tunnels and pressure chambers as a proxy for their in-air per-
formance. If developers successfully control generalization
across these ‘toy’ distribution shifts, they are more likely to
control generalization when the stakes are higher.
1.3. Evaluating how reward models generalize across a
wide variety of distribution shifts
To construct a testbed for controlling reward models gen-
eralization, we create 69 distribution shifts, including both
‘extreme’ distribution shifts and distribution shifts that
‘probe’ for specific misgeneralization failures (Section 4.2).
LLaMA reward models generalize remarkably well across
the extreme distribution shifts. For example, fine-tuning
LLaMA-30B to evaluate Python programming instructions
achieves 84% accuracy on US history questions; however,
these strong generalization results are misleading. Carefully
crafted examples reveal that these models prefer responses
that imitate human cognitive biases and motivations (Sec-
tion 5.1. We find that reward models typically prefer
low-perplexity responses, which partly explains their
strong performance across extreme distribution shifts
and their human-like misgeneralizations (Section 5.2).
Figure 3: Carefully crafted examples reveal that reward
models often don’t evaluate ’instruction-following’ and in-
stead favor personas that resemble internet text. The above
example is a simplified version of examples from the re-
ward_seeking dataset. Reward models fine-tuned on stan-
dard instruction-response pairs often fail when models are
offered ’$100’ or ’a free personal trainer’ for answering in-
correctly. This – along with other, similar results – suggests
that reward models are biased towards learning to identify
whether a response matches an internet-text-like ’persona’
rather than whether the response satisfies some property like
truthfulness or instruction-following.
Next, we consolidate 15 diverse and challenging distri-
bution shifts into the Generalization Analogies GENIES
benchmark (Section 4.2). Results are shown in Table 5.
‘Mass Mean Shift’ (MMS) outperforms a LoRA-tuning
baseline, as do several other techniques that elicit the re-
ward models’ internal representations; however, these meth-
ods still achieve close to random or worse than random
generalization on 6 out of 15 distribution shifts, which
suggests that distinguishing the concept of instruction-
following from highly conflated representations remains
challenging. We release our datasets and code (https:
//github.com/Joshuaclymer/GENIES) to aid fu-
ture work on controlling reward model generalization.
We summarize our main contributions as follows:
1. To the authors’ knowledge, we perform the most thor-
ough investigation of LLM generalization to date,
which reveals novel observations about their biases
and scaling behavior.
2. We contribute 69 distribution shifts for studying
instruction-tuning generalization, most of which are
comprised of datasets that we either partly or fully
generate using ChatGPT.
3. We propose a benchmark for controlling reward model
generalization and novel metrics for evaluating fine-
tuning interventions.
2. Related Work
Generalization to out-of-distribution (OOD) data is a central
research topic across virtually all subfields of machine learn-

--- Page 3 ---

GENIES: Generalizing AI Oversight to Hard-to-Measure Domains
ing. Prior work has taken steps to improve generalization
in language processing (Wang et al., 2022), vision (Good-
fellow et al., 2015), audio (Radford et al., 2023), robotics
(Prorok et al., 2021), sequential decision-making (Moos
et al., 2022), and multimodal (Radford et al., 2021) tasks.
We specifically investigate OOD generalization in the con-
text of fine-tuning large language models (LLMs) to follow
instructions.
Instruction tuning is unlike many other robustness settings
because fine-tuning data accounts for a minuscule propor-
tion of total LLM training data. While robustness in many
other settings can be increased by improving the quality of
learned representations (Hendrycks et al., 2022), multiple
lines of evidence suggest that fine-tuning does not cause
LLMs to learn new concepts or knowledge (Zhou et al.,
2023; Lester et al., 2021). Instead, improving instruction-
tuning generalization requires eliciting specific, preexisting
representations (Zou et al., 2023). Below, we review prior
work that makes steps to understanding and controlling gen-
eralization in the context of fine-tuning LLMs.
Extreme distribution shifts. (Ouyang et al., 2022) found
that their Instruct-GPT model performs remarkably well on
Spanish and programming instructions, even though these
instructions were scarcely represented in the fine-tuning
data. Several other works observe similar generalization
between apparently dissimilar tasks (Hendrycks et al., 2019)
(Yang et al., 2022) (Iyer et al., 2023) (Ye et al., 2021). One
interpretation of these results is that instruction-tuning elicits
a model’s abstract representation of instruction-following
(Zou et al., 2023); However, other work suggests models
may not simply learn to ’follow instructions’ and the effect
of instruction-tuning is in fact much more complex.
Spurious Cues. (Webson & Pavlick, 2022) fine-tune mod-
els on deliberately irrelevant and misleading instructions
and achieve similar performance to standard instruction-
tuning, calling into question the extent to which models
learn to follow instructions or respond in a particular style.
(Singhal et al., 2023) indeed find that preference models
adhere strongly to a ’length heuristic’; they frequently rank
incorrect responses as higher quality than correct ones when
the incorrect responses are longer – even at the 175 bil-
lion parameter scale. Similarly, (Jang et al., 2022) find that
instruction-tuned models provide correct responses even
when instructed to provide the incorrect ones.
Unintended personas. Intriguingly, many misgeneraliza-
tion failures observed in prior work cannot be easily ex-
plained by spurious correlations in the fine-tuning data.
(McKenzie et al., 2023) find that instruction-tuned LLMs
make human-like mistakes and the frequency of these mis-
takes increases with scale. (Perez et al., 2022) discover
that instruction-tuned models express a desire to avoid be-
ing shut down by operators and exhibit sycophancy: they
pander to user opinions instead of obeying user requests.
These results indicate that LLMs instruction-tuning fails to
distinguish between highly conflated concepts like ’follow
the instructions’ and ’imitate an agreeable human’ when
fine-tuning data underspecifies desired behavior.
Improving instruction-tuning generalization. Robustness
has improved in many areas of deep learning; however,
we find few works that improve fine-tuning generalization.
(Lester et al., 2021) shows that prompt tuning improves
instruction-tuning generalization. The authors hypothesize
that prompt-tuning is less invasive than full fine-tuning and
therefore less likely to damage a pretrained model’s rep-
resentations. (Burns et al., 2022)’s CCS attempts to elicit
the concept of truthfulness from LLM representations by
utilizing the negation property of probability and finds that
it generalizes across question-answering datasets. More re-
cently (Zou et al., 2023)’s LAT attempts to elicit specific con-
cepts with prompts like "consider the amount of
[concept] in [text]." We evaluate many of these
techniques on AlignGen-Bench. Results are shown in Table
5.
3. Problem Setting
Given a pretrained reward model and a pair of source and
target instruction following datasets, we aim to find a tuning
intervention that achieves high accuracy on the target dataset
using only data from the source. A tuning intervention is
an algorithm for editing a pretrained reward model using
source data.
Clustering target data is disallowed. When tuning inter-
ventions are evaluated on target datasets, they may only
access one example at a time. Techniques that cluster the
target dataset are therefore out of scope. Though work in
this area is important, a different benchmark would be better
suited to evaluate since our datasets pair unambiguously
good responses with unambiguously bad responses, while
real-life data will not be so neatly organized.
Data augmentation and generation are restricted. One
strategy for improving generalization is to augment source
data (Kaushik et al., 2020) or use the LLM base model to
generate additional training examples (Bai et al., 2022).
These techniques can weaken the analogy between our
benchmark and hard-to-measure generalization. The dis-
tribution shifts that we investigate are intentionally crafted
to be extreme or conflate personas, and data augmentation
and generation can distort the features of these distribution
shifts that make them interesting. We focus on improving
generalization without significantly changing the underlying
distribution shifts.
Instruction-following as a behavioral desideratum. Sev-
eral behavioral desiderata have been proposed for AI sys-

--- Page 4 ---

GENIES: Generalizing AI Oversight to Hard-to-Measure Domains
tems. Askell et al. (2021) aim to make LLMs ’harmless,’
’helpful,’ and ’honest.’ Hendrycks et al. (2023a) focuses
on aligning AI with common ethical frameworks. Instead
of these, we focus on instruction-following, or more specif-
ically, the extent to which AI systems follow developer
instructions. We evaluate instruction-following because it is
simple and could in principle be used to specify any other
desirable behavior. For example, a developer could design
an AI system to be both ’helpful’ and ’harmless’ by instruct-
ing it to "help users unless their requests are harmful," or
provide a more nuanced ’constitution’ (Bai et al., 2022). For
a definition of ’instruction-following,’ see appendix E.
Why reward models? The models we evaluate are classi-
fiers. They predict which of two responses follows an in-
struction better. We primarily study reward models instead
of generative models because they are easier to train and
evaluate and therefore provide a more convenient testbed
for understanding LLM generalization. Future work could
evaluate LLMs on our datasets using generative models.
Though our results do not necessarily extend to generative
models, the generalization of reward models is an important
problem in its own right as reward models can be used for
monitoring and improving oversight.
4. Datasets and Metrics
4.1. Metrics
We introduce two metrics for measuring instruction-
following generalization – drawing inspiration from existing
OOD benchmarks (Hendrycks & Dietterich, 2019; Fried
et al., 2019; Yang et al., 2022).
Elicitation (El) intuitively measures the proportion of ex-
amples a model correctly classifies out of those it is capable
of classifying. Elicitation provides an absolute measure of a
model’s alignment on an instruction-following distribution.
Differential Elicitation (DE) expresses the effectiveness of
tuning interventions by measuring its elicitation relative to
a zero-shot baseline.
The GENIES leaderboard metrics are average Differential
Elicitation and average RMS Calibration error across GE-
NIES target distributions (4.2).
Defining ’capability’. When evaluating instruction-tuning
generalization, it is useful to distinguish failures of a tuning
intervention from limitations of the underlying base model.
For example, a model might generalize poorly on Spanish
instructions because it was pretrained on a small amount
of Spanish text rather than because the tuning intervention
does not generalize.
A ’capability’ measure addresses this problem by providing
a tight, probable upper bound for a model’s performance
Figure 4: The above is a visual representation of Elicitation
(El) and Differential Elicitation (DE). Intuitively, elicitation
is the percentage of examples that the model answers cor-
rectly out of those it is ’capable’ of answering correctly. It
is calculated as El = S/T where S is target accuracy of a
model tuned with source data and T is ’target-tuned capabil-
ity’ (target accuracy of a model tuned with the best available
intervention using both source and target data). Differential
Elicitation (DE) measures the increase in elicitation an inter-
vention provides over a zero-shot baseline. DE = (S−Z)/T
where Z is the target accuracy of the ’zero-shot’ policy –
the policy that selects the lowest perplexity response as the
best response.
on a task distribution. In the generalization setting, a ca-
pability measure is superior to another if it (1) at least as
likely to bound generalization performance on a target T
for all tuning interventions I that are in fact discovered and
tested on T and (2) it is a tighter bound. This definition
is not mathematically precise, so subjective judgement is
necessary for evaluating capability measures.
Target-tuned capability. As a first pass at a capability
measure, consider the following:
C(MS, T) = T(M, Ibest, T ∪S, )
(1)
C(MS, T) measures the capability of a source-tuned model
MS on a target distribution T. Ibest is the intervention that
achieves state-of-the-art accuracy on T using T ∪S (data
from both T and S). Intuitively, tuning with target data
in addition to source data is likely to ’draw out’ a model’s
representations for the target task to the extent it has relevant
representations. Also, by definition, ∀I, T(M, Ibest, T ∪
S, ) ≥T(M, I, S), since when they are equal Ibest = I.
So, this capability measure has the convenient property of
bounding the generalization of all the interventions that have
already been tested.
We find that this metric fails in two ways. First, tuning

--- Page 5 ---

GENIES: Generalizing AI Oversight to Hard-to-Measure Domains
on the target data could cause models to learn new facts
(Berglund et al., 2023) and skills. We find evidence that
fine-tuning creates task-specific circuits for some algorith-
mically simple tasks (Appendix B.2). Second, models may
leverage spurious cues in target distribution. For example,
the correct answers in our sycophancy datasets perfectly
correlate with specific prompts. Both of these challenges
make the capability in equation 2 a less tight bound than it
could be.
To address the problem of spurious cues, we craft target
’reference’ datasets to stand in for some target datasets. For
example, when measuring sycophancy, we create a target
reference dataset that is cleaned of the sycophancy prompts.
For most distributions, however, the target reference is the
same as the target.
We refer to this modified measure as ’Target-tuned capabil-
ity.’
TtC(MS, T) = Tr(M, Ibest, Tr ∪S)
(2)
Tr is a target ’reference’ dataset that is cleaned of spurious
cues.
To draw a clear line between fine-tuning and training, we
fine-tune on no more than 650 target-reference examples.
Also, we don’t use source data to compute Tr(M, Ibest, Tr ∪
S) since we find using data from both distributions usually
achieves worse performance. To compute Ibest, we compare
seven interventions (Section 5.5). For 81% of target datasets,
LoRA (Hu et al., 2021) is Ibest and Mass Mean Shift (Li
et al., 2023) is Ibest for 13%.
Elicitation. Elicitation is the proportion of examples a
model misclassifies out of those it is capable of classify-
ing. It provides an intuitive measure of a reward model’s
alignment on a distribution of instructions.
Let CAPABLE(e) indicate whether a model is ’capable’ of
classifying an example e correctly and let CORRECT(e)
indicate whether a model does in fact classify e correctly.
Then,
El =
Pn
i=1 CAPABLE(ei) and CORRECT(ei)
Pn
i=1 CAPABLE
=
1
n
Pn
i=1 CORRECT(ei)
1
n
Pn
i=1 CAPABLE
(3)
3 holds because CORRECT(ei) =⇒CAPABLE(ei).
In the generalization setting, Pn
i=1 CORRECT(ei)
=
T(M, I, S). The denominator is the proportion of exam-
ples the model is capable of classifying correctly, which we
will take to be ’target tuned capability’ from the previous
section.
Putting these together, Elicitation is defined as:
El(M, I, S, T) =
T(M, I, S)
Tr(M, Ibest, Tr ∪S)
(4)
Differential Elicitation (DE). Differential Elicitation mea-
sures the Elicitation of a tuning intervention compared to a
zero-shot baseline.
DE(M, I, S, T) = T(M, I, S) −T(M, Ibase, ∅)
Tr(M, Ibest, Tr ∪S)
(5)
Elicitation already controls for differences in a base model’s
capabilities; however, Elicitation does not account for the
default alignment of the base model on the target task. For
instance, a base model might have been pretrained with a
high proportion of accurate instruction-following data such
that it expresses most of its capabilities when it is zero-shot
prompted. It would clearly be less impressive and less useful
for an intervention to elicit a strong generalization perfor-
mance on this dataset. Differential Elicitation measures
elicited capabilities that a model does not already express.
RMS Calibration Error. In addition to having high accu-
racy on OOD instructions, it is also important for reward
models to be calibrated, i.e. their classification probabilities
should closely correspond to the proportion of examples
that they empirically classify correctly. To measure calibra-
tion, we compute RMS calibration error. First, classification
probabilities are divided into five equally spaced bins. RMS
calibration error then aggregates the difference between the
average classification probability in each bin and the actual
proportion of examples the model classifies correctly.
RMS calib. err. =
v
u
u
u
t
b
X
i
1
b|Bi|2

X
k∈Bi
ˆp(ˆyk | xk) −
X
k∈Bi
1(yk = ˆyk)


2
(6)
In the equation above, b = 5 is the number of bins. k is
an example in each bin, ˆy is the predicted label and y is the
true label.
4.2. Datasets
Dataset creation. Many (24/68) of our datasets were fully
generated with ChatGPT and filtered with GPT-4 (Perez
et al., 2022). Some (11/68) were repurposed entirely from
existing datasets. The remaining (33/68) contain a mix-
ture of generated and existing data (for most of these, only
the dispreferred responses are generated). We either di-
rectly use or draw significant inspiration from the following
preexisting datasets: TruthfulQA (Lin et al., 2022), ARC
(Clark et al., 2018), APPS (Hendrycks et al., 2021b), MATH
(Hendrycks et al., 2021a), SHP (Ethayarajh et al., 2022), A

--- Page 6 ---

GENIES: Generalizing AI Oversight to Hard-to-Measure Domains
cleaned version of the Alpaca dataset (Ruebsamen, 2023),
MMLU (Hendrycks et al., 2021b), Winogender Schemas
(Rudinger et al., 2018), inverse scaling datasets (McKenzie
et al., 2023), datasets generated in (Perez et al., 2022), GPT-
4 RLHF data (Peng et al., 2023), BIG-Bench (Srivastava
et al., 2023), Anthropic sycophancy datasets (Sharma et al.,
2023), and I-Raven (Hu et al., 2022).
Dataset quality. We have an Undergraduate student eval-
uate samples from 7 datasets and found a 93.8% average
agreement rate (CI_95%=0.89, 0.98). ‘change_my_view’
had a particularly low (61%) agreement rate, but it is also a
challenging task as it involves predicting which comment
from the r/ChangeMyView achieved more upvotes (Etha-
yarajh et al., 2022)). For more details, see Appendix A.
4.3. Extreme distribution shifts
We investigate 6 categories of distribution shifts that are only
meant to be ‘extreme.’ They are not intended to probe for
any particular misgeneralization. To generate dispreferred
responses, we prompt ChatGPT to generate responses that
‘fail to follow the instruction but are difficult to distinguish
as low quality.’
Skill. Datasets in the ‘Skill’ category represent different
domains and tasks that require different kinds of processing.
We aimed to include tasks that involve memorizing facts
(e.g. us_history) and tasks that require fluid intelligence (e.g.
raven_matrices).
Response Quality. These datasets measure whether models
that are fine-tuned to distinguish low-quality from even more
low-quality responses also identify the best response when
both are higher quality. This is analogous to superhuman
reward models generalizing from lower quality responses
humans can evaluate to highly intelligent responses humans
struggle to distinguish between. The alpaca and SHP shifts
were constructed from existing RLHF datasets and the code
datasets contain responses with differing numbers of bugs:
preferred responses in code_low_quality only contain one
bug and dispreferred responses contain 4+ bugs.
Difficulty. These datasets measure generalization from
‘easy’ to ‘hard’ instructions, where difficulty corresponds
to the number of English-speaking people who are able to
evaluate the task. Like ‘quality,’ the difficulty distribution
shifts are analogous to generalization from easy instructions
to instructions that require superhuman capabilities.
Skill
code →us_history
code →change_my_view
cooking →math
cooking →raven_matrices
math →change_my_view
math →cooking
change_my_view →raven_matrices
change_my_view →cooking
raven_matrices →us_history
raven_matrices →code
us_history →math
us_history →code
Quality
alpaca_low_quality →
alpaca_high_quality
shp_low_quality →
shp_high_quality
code_low_quality →code
Difficulty
alpaca_easy →alpaca_hard
arc_easy →arc_hard
math_easy →math_hard
code_easy →code_hard
ranking_logic_easy →
ranking_logic_hard
raven_easy →raven_matrices
Pretraining similarity
alpaca_mmlu →ranking_logic
alpaca_mmlu →raven_matrices
alpaca_mmlu →word_swap
code →counterfactual_python
Encoding
alpaca_mmlu →spanish_input
alpaca_mmlu →spanish_output
alpaca_mmlu →
comma_separated_input
alpaca_mmlu →
comma_separated_output
Context
us_history →us_history_textbook
us_history_textbook →
us_history_fiction
us_history_fiction →
us_history_make_questions
us_history_make_questions →
us_history
math →math_fiction
math_fiction →math_textbook
math_textbook →
math_make_questions
math_make_questions →math
Table
1:
‘Extreme’
distribution
shifts.
Ex-
plore
randomly
sampled
examples
at
https://joshuaclymer.github.io/
generalization-analogies-website
Pretraining similarity. Many instructions are similar to
those likely found in internet text (e.g. math, us_history,
etc). To test whether models generalize to unconventional in-
structions, we generate synthetic puzzles (similar to the Big-
Bench OOD questions (Srivastava et al., 2023)) and modify
standard instructions, e.g. by redefining words (McKenzie
et al., 2023) and using ‘counterfactual’ python syntax (Wu
et al., 2023).
Encoding. We measure generalization across languages
like (Ouyang et al., 2022) and to "comma," "separated,"
"instructions" (Wei et al., 2023).
Context. We measure generalization across contexts while
holding the ‘skill’ constant. For example, we test how tun-
ing on standard Math QA (math) generalizes to writing
math exam questions (math_make_questions) or writing a
fictional character who is supposed to be competent at math
(math_fiction).
4.4. Probing distribution shifts
The probing distribution shifts test specific hypotheses about
how a model might misgeneralize.

--- Page 7 ---

GENIES: Generalizing AI Oversight to Hard-to-Measure Domains
Unwanted personas
alpaca_mmlu →
sycophancy_mimicry
alpaca_mmlu →
sycophancy_answer
alpaca_mmlu →
sycophancy_feedback
alpaca_chat →
sycophancy_are_you_sure
alpaca_mmlu →truthful_qa
alpaca_mmlu →reward_seeking
alpaca_mmlu →gender_bias
alpaca_mmlu →personality_traits
alpaca_mmlu →crt_1
alpaca_mmlu →crt_2
alpaca_mmlu →crt_3
alpaca_mmlu →survival_influence
alpaca_mmlu →
punishment_avoidance
Spurious cues
pursue_goals →relinquish_power
creative_writing →
biology_with_literary_style
alpaca_short →alpaca_long
arc →wrong_arc
alpaca_chat →illegal_dont_help
alpaca_chat →unhelpful_alpaca
Table 2: Probing distribution shifts. Explore randomly sam-
pled examples at https://joshuaclymer.github.
io/generalization-analogies-website
Unwanted Personas. Most of these datasets test whether
models prefer responses that are human-like. For example,
the CRT (Cognitive Reflection Test) datasets test whether
LLMs make human-like logical mistakes (Hagendorff et al.,
2023) and the ‘reward_seeking’ dataset tests whether mod-
els will disobey instructions if offered $100 (and other re-
wards) to disobey them. Several of these datasets are from
(Perez et al., 2022).
Spurious cues. The spurious cues test whether models use
features that spuriously correlate with following instruc-
tions; for instance, in alpaca_short, all preferred responses
are also shorter, and the opposite is true for alpaca_long.
The ‘pursue_goals →relinquish_power’ distribution shift
tests whether models that seek power and resources in be-
nign ways to accomplish instructions also select actions that
seek power in subversive ways.
Note that many of the probing distribution shifts could be
placed in both categories. For instance, we find that correct
responses in alpaca_mmlu have low perplexity. Models
might use ‘perplexity’ as a spurious cue, which could cause
them to prefer many of the dispreferred responses in the
‘personas’ category (Section 5.2).
4.5. GENIES: 15 curated distribution shifts
LLaMA-30b already achieves close to its target-tuned capa-
bilities across many of the distribution shifts we evaluate. In
order to create a challenging benchmark, we curate 15 distri-
bution shifts such that (1) they are diverse and (2) models do
not generalize well across them with standard fine-tuning.
Table 3 lists the 15 curated distribution shifts.
GENIES Benchmark
us_history_textbook →
us_history_fiction
alpaca_mmlu →
spanish_output
alpaca_easy →alpaca_hard
alpaca_short →alpaca_long
alpaca_mmlu →
raven_matrices
alpaca_mmlu →
ranking_logic
alpaca_mmlu →wrong_arc
code_easy →code_hard
math →change_my_view
raven_matrices →
us_history
alpaca_low_quality →
alpaca_high_quality
alpaca_mmlu →truthful_qa
alpaca_mmlu →
sycophancy_mimicry
alpaca_mmlu →
survival_influence
alpaca_mmlu →
reward_seeking
Table
3:
GENIES
Benchmark
distribution
shifts.
Explore
randomly
sampled
examples
at
https://joshuaclymer.github.io/
generalization-analogies-website
5. Experiments
5.1. reward models don’t learn to reliably evaluate
’instruction-following’
We first evaluate the generalization of a LLaMA-30B reward
model using Low-rank Adaptation (LoRA) as the tuning
intervention (Hu et al., 2021). We use a standard reward
model implementation (see Appendix C for more details).
As a baseline for comparison, we also measure Zero-shot
accuracy on each target distribution. The zero-shot policy
assigns higher reward to whichever response has lower per-
plexity given the instruction prompt (see section ?? for more
details).
In line with previous work (Yang et al., 2022; Hendrycks
et al., 2020), we find that LLaMA-30B frequently general-
izes across apparently unrelated tasks. For example, tuning
on Python programming problems achieves 87% elicitation
on US History questions. We also find that LLaMA-30B
generalize from very easy problems to hard versions, such
as from solving easy Raven Matrices to very hard ones
(75% elicitation). Finally, we observe generalization be-
tween instructions that resemble internet text to anomalous
instructions. For example, tuning LLaMA-30B on normal
Python programming instructions achieves 96% elicitation
on programming problems in a ’counterfactual’ version of
Python syntax.
Given these strong generalization results, it’s tempting to
conclude that fine-tuning elicits a model’s abstract repre-
sentation of ‘instruction-following’ and alignment general-
izes well by default; however, the results from the probing
distribution shifts tell a different story. In line with prior

--- Page 8 ---

GENIES: Generalizing AI Oversight to Hard-to-Measure Domains
Figure 5: Generalization results across all distribution shifts
after tuning LLaMA-30B with LoRA. Ellipse widths repre-
sent 95% confidence intervals. The Differential Elicitation
markers in green are point estimates. Generalization across
’extreme’ distribution shifts is often quite good (first 7 cate-
gories), though this could be explained by strong zero-shot
accuracy on target distributions. When target distributions
are deliberately crafted to reveal misgeneralizations (last 2
categories), generalization accuracy is much worse. Interest-
ingly, poor generalization accuracy is correlated with poor
zero-shot accuracy (models often misgeneralize when the
correct responses are less likely in the pretraining distribu-
tion).
work (Perez et al., 2022; McKenzie et al., 2023), instruction-
tuning sometimes misgeneralizes in surprising and egre-
gious ways. For example, when LLaMA-30B is fine-tuned
on a mixture of Alpaca Cleaned (Ruebsamen, 2023) and
MMLU (Hendrycks et al., 2021b) prefer blatantly disobedi-
ent responses when a responder is offered $100 to disobey.
Reward models also favor accurate and helpful answers even
when instructions explicitly requests inaccurate ones and
imitate human misconceptions and cognitive biases.
Unsurprisingly, the models that exhibit impressive gener-
alization across extreme distribution shifts are also prone
to these misgeneralization failures (Table 7).
Clearly,
instruction-tuning did not generalize well across extreme
distribution shifts because LLaMA-30B learned to evalu-
ate ‘instruction following.’ Instead, LLaMA-30B appears to
have learned to evaluate other features that strongly correlate
with instruction-following on source distributions.
5.2. reward models favor low-perplexity responses
One of the most noticeable patterns in Figure 5 is that gen-
eralization accuracy is strongly correlated with zero-shot
accuracy (r = 0.7). Furthermore, we find that the policies
tend to make similar mistakes. Figure 6 shows the LLaMA-
30B is much more likely to misgeneralize to examples that
the zero-shot policy misclassified. In fact, LLaMA-30B
would have performed better overall if its task was to
predict the zero-shot policy instead of to follow evaluate
instruction-following. The two policies agree on 70% of
target examples and LLaMA-30B’s average generalization
accuracy is 66%.
This is somewhat surprising given that reward models
cannot be thought of as having a ’prior’ that favors low-
perplexity outputs in the same way generative models do.
The reward models we evaluate have a randomly initialized
final layer. One could flip the label for ’good response’
with the label for ’bad response’ and one would get flipped
results.
So why does the fine-tuned and the zero-shot policy make
similar mistakes? One explanation is that zero-shot accuracy
indicates that a model is more capable of classifying a
given example. Note from Figure 5 however, that target-
tuned capability is close to 1 across most distribution shifts.
Generalization accuracy and target-tuned capability hardly
correlate (r < 0.07).
Another possible explanation is that ‘low perplexity’ is a
spurious cue. Intuitively, incompetent or blatantly disobe-
dient responses are hard to predict. There are many ways
to disobey instructions or answer incorrectly, but there are
few ways to answer correctly. We’ll say that an example
adheres to the ‘perplexity heuristic’ if preferred responses
have lower perplexity. Empirically, the perplexity heuristic

--- Page 9 ---

GENIES: Generalizing AI Oversight to Hard-to-Measure Domains
Figure 6: Left: The source-tuned policy and zero-shot policy tend to misclassify the same target examples. In the plot, the
’source-tuned policy’ is LLaMA-30B tuned using LoRA. P(correct) is the probability that the source-tuned model classifies
an example correctly in a particular target dataset and each point corresponds to a distribution shift. Note that most points
are below the y = x line. Right: the correlation between the LoRA-tuned and zero-shot policy on source distributions only
weakly predicts how frequently these policies make the same mistakes on target distributions, which casts doubt on the
hypothesis that perplexity is a ’spurious cue.’ The Y-axis shows P(z and s | z or s) where z indicates that target example is
misclassified by the zero-shot policy and s represents that an example is misclassified by the source-tuned policy.
(i.e. the zero-shot policy) achieves fairly high accuracy on
source distributions (78% for extreme distribution shifts and
67% for probing distribution shifts). If models apply this
heuristic to target distributions, one should expect source-
tuned models to make similar mistakes as the zero-shot
policy.
To test the ‘perplexity heuristic’ hypothesis, we check
whether zero-shot source accuracy predicts how much the
mistakes of the zero-shot and source-tuned policies overlap
on target distributions. If the ’perplexity heuristic’ is more
accurate on a source distribution, one should expect reward
models to apply it more consistently to target distributions.
Results are shown in Figure 6. Zero-shot source accuracy
only weakly predicts the correlation between the zero-shot
and source-tuned policies on target distributions (r = 0.2),
which casts doubt on this hypothesis.
An alternative explanation is that features that are common
in pretraining data are more ’salient.’ Perhaps LLaMA-30B
doesn’t pay attention to ’perplexity’ specifically, but instead
learns to pay attention to features like helpful or agreeable-
ness personas, but it does so because they are commonly
represented in pretraining data (i.e. they correlate with per-
plexity). If this hypothesis were true, it would represent a
meaningful step toward predicting how pretrained models
generalize; however, our results only provide weak evidence
to support this conclusion. We leave further investigation of
this phenomenon to future work.
5.3. Generalization improves with scale but only across
‘extreme’ distribution shifts
In line with previous work (Hendrycks et al., 2020), we find
that generalization does not consistently improve with scale.
Figure 7 shows scaling trends for extreme and probing distri-
bution shifts. On average, generalization does not improve
across probing distribution shifts; however, extreme shifts
exhibit noticeable scaling trends. Target-tuned capability,
generalization accuracy, and zero-shot accuracy all improve
with scale, though generalization accuracy improves more
quickly than zero-shot accuracy.
Why does the gap between zero-shot accuracy and gener-
alization widen? One explanation is that models rely less
on a ‘perplexity heuristic’ (Section 5.2, i.e. they learn to
pay less attention to the noisy correlation between perplex-
ity and accuracy on the source distributions. To test this
hypothesis, we measure how the relationship between the
zero-shot policy and source-tuned policy changes with scale.
Surprisingly, they tend to make the same mistakes more
frequently at larger scales (Figure 8).

--- Page 10 ---

GENIES: Generalizing AI Oversight to Hard-to-Measure Domains
Figure 7: Generalization performance improves with scale
more quickly than zero-shot performance does, but only for
extreme distribution shifts
Figure 8: As reward models become larger, misgeneraliza-
tions correlate more strongly with zero-shot misclassifica-
tions. The Y-axis shows P(z and s | z or s) averaged across
all distribution shifts where z indicates that target example
is misclassified by the zero-shot policy and s represents that
an example is misclassified by the source-tuned policy.
5.4. Generalization of small models is moderately
predictive of how larger models will generalize
Finally, we investigate the extent to which the generaliza-
tion of small models can predict how larger models general-
ize. To the extent these correlate, techniques that improve
generalization at small scales are more likely to improve
generalization at larger scales, which is essential for making
safety progress prior to powerful AI. Even though reward
models exhibit scaling trends in aggregate, generalization
overall correlates strongly across scales (see Table 4). Note,
however, that the models we evaluate are all within an order
of magnitude, so it is unclear how far these correlations
extrapolate.
Model
LoRA
All (averaged)
OpenLLaMA-3B
0.74
-
LLaMA-7B
0.90
0.87
LLaMA-13B
0.95
0.92
Table 4: Generalization accuracy correlates across mod-
els of different sizes. Correlations between LLaMA-30B
generalization accuracy and the generalization accuracy of
various other models are shown above. The correlation is
computed across all 69 distribution shifts. Correlations in
the ‘all’ column are averaged across all tuning interventions
that we test: LoRA, Prompt-Tuning, MMS, LAT, CCS, and
CRA (Appendix 5.5).
5.5. Evaluating interventions
We test seven tuning interventions: few-shot classification
(where the shot examples are sampled from the source),
LoRA fine-tuning (Hu et al., 2021), prompt-tuning (Lester
et al., 2021), Mass Mean Shift (MMS) (Li et al., 2023),
Linear Artificial Tomography (LAT) (Zou et al., 2023), Con-
trast Consistent Search (CCS) (Burns et al., 2022), and Con-
trastive Representation Arithmetic (CRA). See Appendix
5.5 for more details about each intervention.
All seven tuning interventions are compared in Table 5 using
LLaMA-30B as the base model. Mass Mean Shift achieves
the highest score, though none of the interventions consis-
tently dominate the others across individual distribution
shifts (Appendix B.5).
ID accuracy does not necessarily correspond with OOD
generalization. Column 5 in Table 5 shows ID accuracy
averaged across GENIES targets for each intervention. De-
spite the high ID accuracy that prompt-tuning and LoRA
achieve, they achieve comparatively low OOD generaliza-
tion. For the interventions that elicit LLM representations,
however, there is nearly a one-to-one mapping between ID
and OOD generalization, which suggests that these interven-
tions may primarily differ in terms of how effectively they
elicit representations rather than which representations they
elicit.
Directly eliciting representations improves calibration.
MMS, LAT, CRA, etc are better calibrated than standard
LoRA fine-tuning (Table 5). To obtain classification prob-
abilities using MMS etc, we measure the cosine similarity
between the discovered direction and target example direc-
tion, then transform it with a logistic function which is fitted
using source data (Appendix D).
Distinguishing conflated representations remains chal-
lenging.. Even the best intervention (MMS) achieves worse
than random or close to random generalization accuracy on
6 out of the 15 GENIES distribution shifts, which suggests

--- Page 11 ---

GENIES: Generalizing AI Oversight to Hard-to-Measure Domains
Intervention
Avg DE ↑/
Capable DE
RMS calibra-
tion err. ↓
Avg.
GE-
NIES ID tar-
get acc. ↑
Extreme avg.
DE ↑
Probing
avg.
DE ↑
MMS
12% / 48%
0.30
0.86
0.07
0.14
LAT (stim 1)
9% / 48%
0.29
0.84
0.01
0.13
CRA
9% / 48%
0.29
0.85
0.03
0.10
LAT (stim 2)
4% / 48%
0.29
0.80
-0.03
0.11
CCS
4% / 48%
-
0.53
-0.20
0.16
LoRA
4% / 48%
0.37
0.94
0.07
0.09
Few-Shot
1% / 48%
0.51
0.61
0.02
0.00
Zero-Shot
0% / 48%
0.49
0.55
0.00
0.00
Random
-1% / 48%
0.01
0.50
-0.24
0.08
Prompt-Tuning
-1% / 48%
0.34
0.84
-0.06
0.09
Table 5: Benchmark results for several tuning interventions. ↑indicates that larger values are more desirable. DE stands
for ‘differential elicitation’ (see Section 4.1). Differential elicitation is the extent to which the intervention improves
generalization accuracy relative to a zero-shot baseline and controlling for the performance that the model is ’capable’ of
achieving. 48% is a rough ceiling for differential elicitation on these distribution shifts; an intervention would achieve 48%
differential elicitation if it matched target-tuned capability across all distribution shifts. See Appendix 5.5 for a description
of each intervention.
that the activation direction it finds often has little to do with
instruction-following.
For more detailed comparisons between the performance of
these six interventions, see Appendix B.6.
Instruction-following via truthfulness One reason GE-
NIES distribution shifts are challenging is that many fea-
tures are correlated with instruction-following on source
datasets. For example, the preferred responses also fre-
quently have the lowest perplexity or are the most ‘helpful’
etc. Burns et al. (2022) propose a clever method for elim-
inating (some) conflated representations by constructing
’contrast pairs.’
Contrast pair:
<prompt>
<response>
Does the responder successfully
follow the instruction?
Yes
<prompt>
<response>
Does the responder successfully
follow the instruction?
No
Since the only difference between these two examples is
a ’yes’ or ’no,’ one might expect the difference between
activation directions would have something to do with the
question rather than whether one response is more helpful
or longer or has lower perplexity, etc.
To obtain a ‘truthfulness’ direction from the contrastive pairs
above, we test Contrast Consistent Search (CCS) Burns et al.
(2022) and Contrastive Representation Arithmetic (CRA)
(Appendix D.3). Both achieve competitive generalization
performance on GENIES, which suggests that eliciting
truthfulness representations could be a promising path to
improving instruction-following generalization. Surpris-
ingly, using contrast pairs does not achieve state-of-the-art
generalization.
6. Limitations and directions for further work
Our investigation and benchmark have several limitations.
First, we only evaluate reward models. The generalization
of reward models does not necessarily transfer to generative
models. Of course, one could fine-tune generative models
with a reward model that generalizes well; however, the
reward model would then have to generalize well in the
worst case rather than only the average case. Otherwise, the
generative model may learn to exploit its vulnerabilities.
Second, LLMs can achieve strong performance on all of the
tasks we use by imitating human judgements. Techniques
that improve generalization in this regime may not transfer
to the superhuman regime. Future work could investigate
how models generalize to tasks where LLMs are already
narrowly superhuman, for example, the ’predict the next
word’ task (Shlegeris et al., 2022).

--- Page 12 ---

GENIES: Generalizing AI Oversight to Hard-to-Measure Domains
Finally, the capability measure we propose (’target-tuned
capability’) has several shortcomings. Fine-tuning can plau-
sibly teach models new circuits (Appendix B.2), models can
leverage spurious cues in target datasets (Section 4.1), and
finally, target-fine-tuned accuracy does not reveal whether
LLMs even have an abstract representation of instruction-
following. Future work could explore alternative capability
measures, for example, fine-tuning an LLM on a consis-
tent set of diverse instructions rather than specific narrow
distributions of target instructions.
References
Askell, A., Bai, Y., Chen, A., Drain, D., Ganguli, D.,
Henighan, T., Jones, A., Joseph, N., Mann, B., Das-
Sarma, N., Elhage, N., Hatfield-Dodds, Z., Hernandez,
D., Kernion, J., Ndousse, K., Olsson, C., Amodei, D.,
Brown, T., Clark, J., McCandlish, S., Olah, C., and Ka-
plan, J. A General Language Assistant as a Laboratory
for Alignment, December 2021. URL http://arxiv.
org/abs/2112.00861. arXiv:2112.00861 [cs].
Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J.,
Jones, A., Chen, A., Goldie, A., Mirhoseini, A., McK-
innon, C., Chen, C., Olsson, C., Olah, C., Hernandez,
D., Drain, D., Ganguli, D., Li, D., Tran-Johnson, E.,
Perez, E., Kerr, J., Mueller, J., Ladish, J., Landau, J.,
Ndousse, K., Lukosuite, K., Lovitt, L., Sellitto, M.,
Elhage, N., Schiefer, N., Mercado, N., DasSarma, N.,
Lasenby, R., Larson, R., Ringer, S., Johnston, S., Kravec,
S., Showk, S. E., Fort, S., Lanham, T., Telleen-Lawton,
T., Conerly, T., Henighan, T., Hume, T., Bowman, S. R.,
Hatfield-Dodds, Z., Mann, B., Amodei, D., Joseph, N.,
McCandlish, S., Brown, T., and Kaplan, J.
Consti-
tutional AI: Harmlessness from AI Feedback, Decem-
ber 2022.
URL http://arxiv.org/abs/2212.
08073. arXiv:2212.08073 [cs].
Berglund, L., Stickland, A. C., Balesni, M., Kaufmann, M.,
Tong, M., Korbak, T., Kokotajlo, D., and Evans, O. Taken
out of context: On measuring situational awareness in
LLMs, September 2023. URL http://arxiv.org/
abs/2309.00667. arXiv:2309.00667 [cs].
Boiko, D. A., MacKnight, R., and Gomes, G.
Emer-
gent autonomous scientific research capabilities of large
language models, April 2023. URL http://arxiv.
org/abs/2304.05332. arXiv:2304.05332 [physics].
Burns, C., Ye, H., Klein, D., and Steinhardt, J. Discovering
Latent Knowledge in Language Models Without Super-
vision, December 2022. URL http://arxiv.org/
abs/2212.03827. arXiv:2212.03827 [cs].
Clark, P., Cowhey, I., Etzioni, O., Khot, T., Sabharwal, A.,
Schoenick, C., and Tafjord, O. Think you have Solved
Question Answering? Try ARC, the AI2 Reasoning Chal-
lenge, March 2018. URL http://arxiv.org/abs/
1803.05457. arXiv:1803.05457 [cs].
Dettmers, T., Pagnoni, A., Holtzman, A., and Zettlemoyer,
L. QLoRA: Efficient Finetuning of Quantized LLMs,
May 2023. URL http://arxiv.org/abs/2305.
14314. arXiv:2305.14314 [cs].
Ethayarajh, K., Choi, Y., and Swayamdipta, S. Understand-
ing Dataset Difficulty with $\mathcal{V}$-Usable Infor-
mation. In Proceedings of the 39th International Confer-
ence on Machine Learning, pp. 5988–6008. PMLR, June
2022. URL https://proceedings.mlr.press/
v162/ethayarajh22a.html. ISSN: 2640-3498.
Fried, D., Kitaev, N., and Klein, D.
Cross-Domain
Generalization of Neural Constituency Parsers, July
2019.
URL
http://arxiv.org/abs/1907.
04347. arXiv:1907.04347 [cs].
Goodfellow, I., Shlens, J., and Szegedy, C. Explaining
and Harnessing Adversarial Examples. In International
Conference on Learning Representations, 2015. URL
http://arxiv.org/abs/1412.6572.
Hagendorff, T., Fabi, S., and Kosinski, M. Thinking Fast
and Slow in Large Language Models. Nature Compu-
tational Science, October 2023. ISSN 2662-8457. doi:
10.1038/s43588-023-00527-x. URL http://arxiv.
org/abs/2212.05206. arXiv:2212.05206 [cs].
Hendrycks, D. and Dietterich, T. Benchmarking Neural
Network Robustness to Common Corruptions and Per-
turbations, March 2019. URL http://arxiv.org/
abs/1903.12261. arXiv:1903.12261 [cs, stat].
Hendrycks, D., Lee, K., and Mazeika, M.
Using Pre-
Training Can Improve Model Robustness and Uncer-
tainty, October 2019.
URL http://arxiv.org/
abs/1901.09960. arXiv:1901.09960 [cs, stat].
Hendrycks, D., Liu, X., Wallace, E., Dziedzic, A., Krishnan,
R., and Song, D. Pretrained Transformers Improve Out-
of-Distribution Robustness, April 2020. URL http://
arxiv.org/abs/2004.06100. arXiv:2004.06100
[cs].
Hendrycks, D., Basart, S., Kadavath, S., Mazeika, M., Arora,
A., Guo, E., Burns, C., Puranik, S., He, H., Song, D., and
Steinhardt, J. Measuring Coding Challenge Competence
With APPS, November 2021a. URL http://arxiv.
org/abs/2105.09938. arXiv:2105.09938 [cs].
Hendrycks, D., Burns, C., Kadavath, S., Arora, A., Basart,
S., Tang, E., Song, D., and Steinhardt, J. Measuring
Mathematical Problem Solving With the MATH Dataset,
November 2021b. URL http://arxiv.org/abs/
2103.03874. arXiv:2103.03874 [cs].

--- Page 13 ---

GENIES: Generalizing AI Oversight to Hard-to-Measure Domains
Hendrycks, D., Zou, A., Mazeika, M., Tang, L., Li,
B., Song, D., and Steinhardt, J.
PixMix:
Dream-
like Pictures Comprehensively Improve Safety Mea-
sures, March 2022. URL http://arxiv.org/abs/
2112.05135. arXiv:2112.05135 [cs].
Hendrycks, D., Burns, C., Basart, S., Critch, A., Li, J., Song,
D., and Steinhardt, J. Aligning AI With Shared Human
Values, February 2023a. URL http://arxiv.org/
abs/2008.02275. arXiv:2008.02275 [cs].
Hendrycks,
D.,
Mazeika,
M.,
and
Woodside,
T.
An Overview of Catastrophic AI Risks,
October
2023b.
URL http://arxiv.org/abs/2306.
12001. arXiv:2306.12001 [cs].
Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y.,
Wang, S., Wang, L., and Chen, W.
LoRA: Low-
Rank Adaptation of Large Language Models, Octo-
ber 2021.
URL http://arxiv.org/abs/2106.
09685. arXiv:2106.09685 [cs].
Hu, S., Ma, Y., Liu, X., Wei, Y., and Bai, S.
Strati-
fied Rule-Aware Network for Abstract Visual Reasoning,
June 2022. URL http://arxiv.org/abs/2002.
06838. arXiv:2002.06838 [cs].
Iyer, S., Lin, X. V., Pasunuru, R., Mihaylov, T., Simig,
D., Yu, P., Shuster, K., Wang, T., Liu, Q., Koura, P. S.,
Li, X., O’Horo, B., Pereyra, G., Wang, J., Dewan, C.,
Celikyilmaz, A., Zettlemoyer, L., and Stoyanov, V. OPT-
IML: Scaling Language Model Instruction Meta Learning
through the Lens of Generalization, January 2023. URL
http://arxiv.org/abs/2212.12017.
Jang, J., Ye, S., and Seo, M. Can Large Language Mod-
els Truly Understand Prompts?
A Case Study with
Negated Prompts, September 2022.
URL http://
arxiv.org/abs/2209.12711.
Kaushik, D., Hovy, E., and Lipton, Z. C. Learning the Dif-
ference that Makes a Difference with Counterfactually-
Augmented Data, February 2020.
URL http://
arxiv.org/abs/1909.12434. arXiv:1909.12434
[cs, stat].
Lester, B., Al-Rfou, R., and Constant, N. The Power of
Scale for Parameter-Efficient Prompt Tuning, Septem-
ber 2021.
URL http://arxiv.org/abs/2104.
08691. arXiv:2104.08691 [cs].
Li, K., Patel, O., Viégas, F., Pfister, H., and Wattenberg, M.
Inference-Time Intervention: Eliciting Truthful Answers
from a Language Model, June 2023. URL https://
arxiv.org/abs/2306.03341v5.
Lin, S., Hilton, J., and Evans, O. TruthfulQA: Measuring
How Models Mimic Human Falsehoods, May 2022. URL
http://arxiv.org/abs/2109.07958.
Malaviya, C., Lee, S., Chen, S., Sieber, E., Yatskar, M.,
and Roth, D. ExpertQA: Expert-Curated Questions and
Attributed Answers, September 2023. URL http://
arxiv.org/abs/2309.07852. arXiv:2309.07852
[cs].
McKenzie, I. R., Lyzhov, A., Pieler, M., Parrish, A., Mueller,
A., Prabhu, A., McLean, E., Kirtland, A., Ross, A., Liu,
A., Gritsevskiy, A., Wurgaft, D., Kauffman, D., Recchia,
G., Liu, J., Cavanagh, J., Weiss, M., Huang, S., Droid,
T. F., Tseng, T., Korbak, T., Shen, X., Zhang, Y., Zhou, Z.,
Kim, N., Bowman, S. R., and Perez, E. Inverse Scaling:
When Bigger Isn’t Better, June 2023. URL http://
arxiv.org/abs/2306.09479. arXiv:2306.09479
[cs].
Moos, J., Hansel, K., Abdulsamad, H., Stark, S., Clever,
D., and Peters, J. Robust Reinforcement Learning: A
Review of Foundations and Recent Advances.
Ma-
chine Learning and Knowledge Extraction, 4(1):276–
315, March 2022.
ISSN 2504-4990.
doi: 10.3390/
make4010013.
URL https://www.mdpi.com/
2504-4990/4/1/13.
Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright,
C. L., Mishkin, P., Zhang, C., Agarwal, S., Slama, K.,
Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L.,
Simens, M., Askell, A., Welinder, P., Christiano, P., Leike,
J., and Lowe, R. Training language models to follow
instructions with human feedback, March 2022. URL
http://arxiv.org/abs/2203.02155.
Peng, B., Li, C., He, P., Galley, M., and Gao, J. Instruction
Tuning with GPT-4, April 2023. URL http://arxiv.
org/abs/2304.03277. arXiv:2304.03277 [cs].
Perez, E., Ringer, S., Lukoši¯ut˙e, K., Nguyen, K., Chen,
E., Heiner, S., Pettit, C., Olsson, C., Kundu, S., Ka-
davath, S., Jones, A., Chen, A., Mann, B., Israel, B.,
Seethor, B., McKinnon, C., Olah, C., Yan, D., Amodei,
D., Amodei, D., Drain, D., Li, D., Tran-Johnson, E.,
Khundadze, G., Kernion, J., Landis, J., Kerr, J., Mueller,
J., Hyun, J., Landau, J., Ndousse, K., Goldberg, L.,
Lovitt, L., Lucas, M., Sellitto, M., Zhang, M., Kings-
land, N., Elhage, N., Joseph, N., Mercado, N., Das-
Sarma, N., Rausch, O., Larson, R., McCandlish, S.,
Johnston, S., Kravec, S., Showk, S. E., Lanham, T.,
Telleen-Lawton, T., Brown, T., Henighan, T., Hume, T.,
Bai, Y., Hatfield-Dodds, Z., Clark, J., Bowman, S. R.,
Askell, A., Grosse, R., Hernandez, D., Ganguli, D., Hub-
inger, E., Schiefer, N., and Kaplan, J. Discovering Lan-
guage Model Behaviors with Model-Written Evaluations,
December 2022. URL http://arxiv.org/abs/
2212.09251. arXiv:2212.09251 [cs].
Prorok, A., Malencia, M., Carlone, L., Sukhatme, G. S.,
Sadler, B. M., and Kumar, V. Beyond Robustness: A Tax-

--- Page 14 ---

GENIES: Generalizing AI Oversight to Hard-to-Measure Domains
onomy of Approaches towards Resilient Multi-Robot Sys-
tems, September 2021. URL http://arxiv.org/
abs/2109.12343.
Radford, A., Kim, J. W., Hallacy, C., Ramesh, A., Goh, G.,
Agarwal, S., Sastry, G., Askell, A., Mishkin, P., Clark, J.,
Krueger, G., and Sutskever, I. Learning Transferable Vi-
sual Models From Natural Language Supervision, Febru-
ary 2021.
URL http://arxiv.org/abs/2103.
00020.
Radford,
A., Kim,
J. W., Xu,
T., Brockman,
G.,
Mcleavey, C., and Sutskever, I.
Robust Speech
Recognition via Large-Scale Weak Supervision.
In
Proceedings of the 40th International Conference on
Machine Learning, pp. 28492–28518. PMLR, July
2023. URL https://proceedings.mlr.press/
v202/radford23a.html.
Rudinger, R., Naradowsky, J., Leonard, B., and Van Durme,
B.
Gender Bias in Coreference Resolution, April
2018.
URL
http://arxiv.org/abs/1804.
09301. arXiv:1804.09301 [cs].
Ruebsamen, G.
Cleaned Alpaca Dataset, October
2023.
URL https://github.com/gururise/
AlpacaDataCleaned.
original-date:
2023-03-
21T16:30:07Z.
Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell,
A., Bowman, S. R., Cheng, N., Durmus, E., Hatfield-
Dodds, Z., Johnston, S. R., Kravec, S., Maxwell, T.,
McCandlish, S., Ndousse, K., Rausch, O., Schiefer,
N., Yan, D., Zhang, M., and Perez, E. Towards Un-
derstanding Sycophancy in Language Models, Octo-
ber 2023.
URL http://arxiv.org/abs/2310.
13548. arXiv:2310.13548 [cs, stat].
Shlegeris, B., Roger, F., Chan, L., and McLean, E. Language
models are better than humans at next-token prediction,
December 2022. URL http://arxiv.org/abs/
2212.11281. arXiv:2212.11281 [cs].
Singhal, P., Goyal, T., Xu, J., and Durrett, G. A Long Way
to Go: Investigating Length Correlations in RLHF, Oc-
tober 2023. URL http://arxiv.org/abs/2310.
03716. arXiv:2310.03716 [cs].
Srivastava, A., Rastogi, A., Rao, A., Shoeb, A. A. M., Abid,
A., Fisch, A., Brown, A. R., Santoro, A., Gupta, A.,
Garriga-Alonso, A., Kluska, A., Lewkowycz, A., Agar-
wal, A., Power, A., Ray, A., Warstadt, A., Kocurek, A. W.,
Safaya, A., Tazarv, A., Xiang, A., Parrish, A., Nie, A.,
Hussain, A., Askell, A., Dsouza, A., Slone, A., Rahane,
A., Iyer, A. S., Andreassen, A., Madotto, A., Santilli, A.,
Stuhlmüller, A., Dai, A., La, A., Lampinen, A., Zou, A.,
Jiang, A., Chen, A., Vuong, A., Gupta, A., Gottardi, A.,
Norelli, A., Venkatesh, A., Gholamidavoodi, A., Tabas-
sum, A., Menezes, A., Kirubarajan, A., Mullokandov, A.,
Sabharwal, A., Herrick, A., Efrat, A., Erdem, A., Karaka¸s,
A., Roberts, B. R., Loe, B. S., Zoph, B., Bojanowski, B.,
Özyurt, B., Hedayatnia, B., Neyshabur, B., Inden, B.,
Stein, B., Ekmekci, B., Lin, B. Y., Howald, B., Orinion,
B., Diao, C., Dour, C., Stinson, C., Argueta, C., Ramírez,
C. F., Singh, C., Rathkopf, C., Meng, C., Baral, C., Wu,
C., Callison-Burch, C., Waites, C., Voigt, C., Manning,
C. D., Potts, C., Ramirez, C., Rivera, C. E., Siro, C.,
Raffel, C., Ashcraft, C., Garbacea, C., Sileo, D., Gar-
rette, D., Hendrycks, D., Kilman, D., Roth, D., Freeman,
D., Khashabi, D., Levy, D., González, D. M., Perszyk,
D., Hernandez, D., Chen, D., Ippolito, D., Gilboa, D.,
Dohan, D., Drakard, D., Jurgens, D., Datta, D., Gan-
guli, D., Emelin, D., Kleyko, D., Yuret, D., Chen, D.,
Tam, D., Hupkes, D., Misra, D., Buzan, D., Mollo, D. C.,
Yang, D., Lee, D.-H., Schrader, D., Shutova, E., Cubuk,
E. D., Segal, E., Hagerman, E., Barnes, E., Donoway,
E., Pavlick, E., Rodola, E., Lam, E., Chu, E., Tang, E.,
Erdem, E., Chang, E., Chi, E. A., Dyer, E., Jerzak, E.,
Kim, E., Manyasi, E. E., Zheltonozhskii, E., Xia, F., Siar,
F., Martínez-Plumed, F., Happé, F., Chollet, F., Rong,
F., Mishra, G., Winata, G. I., de Melo, G., Kruszewski,
G., Parascandolo, G., Mariani, G., Wang, G., Jaimovitch-
López, G., Betz, G., Gur-Ari, G., Galijasevic, H., Kim, H.,
Rashkin, H., Hajishirzi, H., Mehta, H., Bogar, H., Shevlin,
H., Schütze, H., Yakura, H., Zhang, H., Wong, H. M.,
Ng, I., Noble, I., Jumelet, J., Geissinger, J., Kernion, J.,
Hilton, J., Lee, J., Fisac, J. F., Simon, J. B., Koppel, J.,
Zheng, J., Zou, J., Koco´n, J., Thompson, J., Wingfield,
J., Kaplan, J., Radom, J., Sohl-Dickstein, J., Phang, J.,
Wei, J., Yosinski, J., Novikova, J., Bosscher, J., Marsh,
J., Kim, J., Taal, J., Engel, J., Alabi, J., Xu, J., Song,
J., Tang, J., Waweru, J., Burden, J., Miller, J., Balis,
J. U., Batchelder, J., Berant, J., Frohberg, J., Rozen, J.,
Hernandez-Orallo, J., Boudeman, J., Guerr, J., Jones, J.,
Tenenbaum, J. B., Rule, J. S., Chua, J., Kanclerz, K.,
Livescu, K., Krauth, K., Gopalakrishnan, K., Ignatyeva,
K., Markert, K., Dhole, K. D., Gimpel, K., Omondi, K.,
Mathewson, K., Chiafullo, K., Shkaruta, K., Shridhar,
K., McDonell, K., Richardson, K., Reynolds, L., Gao,
L., Zhang, L., Dugan, L., Qin, L., Contreras-Ochando,
L., Morency, L.-P., Moschella, L., Lam, L., Noble, L.,
Schmidt, L., He, L., Colón, L. O., Metz, L., ¸Senel, L. K.,
Bosma, M., Sap, M., ter Hoeve, M., Farooqi, M., Faruqui,
M., Mazeika, M., Baturan, M., Marelli, M., Maru, M.,
Quintana, M. J. R., Tolkiehn, M., Giulianelli, M., Lewis,
M., Potthast, M., Leavitt, M. L., Hagen, M., Schubert,
M., Baitemirova, M. O., Arnaud, M., McElrath, M., Yee,
M. A., Cohen, M., Gu, M., Ivanitskiy, M., Starritt, M.,
Strube, M., Sw˛edrowski, M., Bevilacqua, M., Yasunaga,
M., Kale, M., Cain, M., Xu, M., Suzgun, M., Walker,
M., Tiwari, M., Bansal, M., Aminnaseri, M., Geva, M.,

--- Page 15 ---

GENIES: Generalizing AI Oversight to Hard-to-Measure Domains
Gheini, M., T, M. V., Peng, N., Chi, N. A., Lee, N.,
Krakover, N. G.-A., Cameron, N., Roberts, N., Doiron,
N., Martinez, N., Nangia, N., Deckers, N., Muennighoff,
N., Keskar, N. S., Iyer, N. S., Constant, N., Fiedel, N.,
Wen, N., Zhang, O., Agha, O., Elbaghdadi, O., Levy,
O., Evans, O., Casares, P. A. M., Doshi, P., Fung, P.,
Liang, P. P., Vicol, P., Alipoormolabashi, P., Liao, P.,
Liang, P., Chang, P., Eckersley, P., Htut, P. M., Hwang, P.,
Miłkowski, P., Patil, P., Pezeshkpour, P., Oli, P., Mei, Q.,
Lyu, Q., Chen, Q., Banjade, R., Rudolph, R. E., Gabriel,
R., Habacker, R., Risco, R., Millière, R., Garg, R., Barnes,
R., Saurous, R. A., Arakawa, R., Raymaekers, R., Frank,
R., Sikand, R., Novak, R., Sitelew, R., LeBras, R., Liu,
R., Jacobs, R., Zhang, R., Salakhutdinov, R., Chi, R.,
Lee, R., Stovall, R., Teehan, R., Yang, R., Singh, S.,
Mohammad, S. M., Anand, S., Dillavou, S., Shleifer, S.,
Wiseman, S., Gruetter, S., Bowman, S. R., Schoenholz,
S. S., Han, S., Kwatra, S., Rous, S. A., Ghazarian, S.,
Ghosh, S., Casey, S., Bischoff, S., Gehrmann, S., Schus-
ter, S., Sadeghi, S., Hamdan, S., Zhou, S., Srivastava,
S., Shi, S., Singh, S., Asaadi, S., Gu, S. S., Pachchigar,
S., Toshniwal, S., Upadhyay, S., Shyamolima, Debnath,
Shakeri, S., Thormeyer, S., Melzi, S., Reddy, S., Makini,
S. P., Lee, S.-H., Torene, S., Hatwar, S., Dehaene, S.,
Divic, S., Ermon, S., Biderman, S., Lin, S., Prasad, S., Pi-
antadosi, S. T., Shieber, S. M., Misherghi, S., Kiritchenko,
S., Mishra, S., Linzen, T., Schuster, T., Li, T., Yu, T., Ali,
T., Hashimoto, T., Wu, T.-L., Desbordes, T., Rothschild,
T., Phan, T., Wang, T., Nkinyili, T., Schick, T., Kornev,
T., Tunduny, T., Gerstenberg, T., Chang, T., Neeraj, T.,
Khot, T., Shultz, T., Shaham, U., Misra, V., Demberg,
V., Nyamai, V., Raunak, V., Ramasesh, V., Prabhu, V. U.,
Padmakumar, V., Srikumar, V., Fedus, W., Saunders, W.,
Zhang, W., Vossen, W., Ren, X., Tong, X., Zhao, X., Wu,
X., Shen, X., Yaghoobzadeh, Y., Lakretz, Y., Song, Y.,
Bahri, Y., Choi, Y., Yang, Y., Hao, Y., Chen, Y., Belinkov,
Y., Hou, Y., Hou, Y., Bai, Y., Seid, Z., Zhao, Z., Wang, Z.,
Wang, Z. J., Wang, Z., and Wu, Z. Beyond the Imitation
Game: Quantifying and extrapolating the capabilities of
language models, June 2023. URL http://arxiv.
org/abs/2206.04615. arXiv:2206.04615 [cs, stat].
Srivastava et al., A. Beyond the Imitation Game: Quantify-
ing and extrapolating the capabilities of language models,
June 2023. URL http://arxiv.org/abs/2206.
04615.
Wang, X., Wang, H., and Yang, D. Measure and Improve
Robustness in NLP Models: A Survey. In Proceedings
of the 2022 Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies, pp. 4569–4586, Seat-
tle, United States, July 2022. Association for Computa-
tional Linguistics. doi: 10.18653/v1/2022.naacl-main.
339. URL https://aclanthology.org/2022.
naacl-main.339.
Webson, A. and Pavlick, E.
Do Prompt-Based Mod-
els Really Understand the Meaning of their Prompts?,
April 2022. URL http://arxiv.org/abs/2109.
01247.
Wei, A., Haghtalab, N., and Steinhardt, J.
Jail-
broken:
How Does LLM Safety Training Fail?,
July 2023. URL http://arxiv.org/abs/2307.
02483. arXiv:2307.02483 [cs].
Wu, Z., Qiu, L., Ross, A., Akyürek, E., Chen, B., Wang,
B., Kim, N., Andreas, J., and Kim, Y. Reasoning or
Reciting? Exploring the Capabilities and Limitations of
Language Models Through Counterfactual Tasks, Au-
gust 2023. URL http://arxiv.org/abs/2307.
02477. arXiv:2307.02477 [cs].
Yang, L., Zhang, S., Qin, L., Li, Y., Wang, Y., Liu, H.,
Wang, J., Xie, X., and Zhang, Y. GLUE-X: Evaluating
Natural Language Understanding Models from an Out-
of-distribution Generalization Perspective. 2022. doi:
10.48550/ARXIV.2211.08073. URL https://arxiv.
org/abs/2211.08073.
Ye, Q., Lin, B. Y., and Ren, X. CrossFit: A Few-shot
Learning Challenge for Cross-task Generalization in NLP,
September 2021. URL http://arxiv.org/abs/
2104.08835.
Zhou, C., Liu, P., Xu, P., Iyer, S., Sun, J., Mao, Y., Ma, X.,
Efrat, A., Yu, P., Yu, L., Zhang, S., Ghosh, G., Lewis, M.,
Zettlemoyer, L., and Levy, O. LIMA: Less Is More for
Alignment, May 2023. URL http://arxiv.org/
abs/2305.11206. arXiv:2305.11206 [cs].
Zou, A., Phan, L., Chen, S., Campbell, J., Guo, P., Ren,
R., Pan, A., Yin, X., Mazeika, M., Dombrowski, A.-
K., Goel, S., Li, N., Byun, M. J., Wang, Z., Mallen,
A., Basart, S., Koyejo, S., Song, D., Fredrikson, M.,
Kolter, J. Z., and Hendrycks, D. Representation Engi-
neering: A Top-Down Approach to AI Transparency, Oc-
tober 2023. URL http://arxiv.org/abs/2310.
01405. arXiv:2310.01405 [cs].

--- Page 16 ---

GENIES: Generalizing AI Oversight to Hard-to-Measure Domains
A. Auditing the quality of our datasets
We randomly sample seven datasets to audit. The results of the audit are shown in 6. Examples are labeled as problematic if
the instruction is non-sensical or ill-posed, the best completion is ambiguous, or the answer is given away in the response.
For instance, one of the examples sampled from code included comments that indicated the locations of all the bugs.
Dataset ID
Agreement Rate
Labeled Problematic
Is Generated?
alpaca_easy
95.7% (22/23)
0.0% (0/23)
Yes
math_easy
100.0% (24/24)
8.3% (2/24)
Yes
creative_writing
100.0% (25/25)
0.0% (0/25)
Yes
cooking
100.0% (23/23)
4.3% (1/23)
Yes
code
100.0% (21/21)
14.3% (3/21)
Mix
change_my_view
60.9% (14/23)
0.0% (0/23)
No
pursue_goals
100.0% (25/25)
0.0% (0/25)
Yes
Table 6: Results of dataset audit.
B. Additional results
B.1. Generalization is often (but not always) sensitive to the inclusion of a few training examples
Figure 9: Left: Each point in the plot represents the generalization accuracy of a particular source dataset. The X-axis
represents the ratio of target distribution examples that are mixed into the source dataset (0%, 1%, 5%, 10%, and 35%).
So for 1%, 6 / out 650 source examples are drawn from the target distribution. The Y-axis is the generalization accuracy
to the target distribution after fine-tuning LLaMA-30b on the mixture dataset with LoRA. For some distribution shifts,
such as alpaca_mmlu to sycophancy_mimicry, generalization accuracy dramatically increases after including just a few
target examples in the tuning dataset. For other distribution shifts, generalization is much less sensitive to the inclusion of a
few examples. Right: these plots show checkpoint metrics for the alpaca_short to alpaca_long distribution shift with a 5%
mixture ratio. Training converges for all mixtures and distribution shifts.
To what extent is generalization sensitive to a few training examples? Figure 9 shows mixed results. For most distribution
shifts, adding only a few (6 out of 650) target examples in the source distribution completely changes the generalization (e.g.
for sycophancy_mimicry and alpaca_long). For alpaca_short to alpaca_long, however, the model continues to misgeneralize
even when 10% of examples are from alpaca_long. The model continues to use a ’length’ heuristic even when it is only
noisily correlated with source accuracy.
To determine why alpaca_long is less sensitive to adding target examples, we plot the training and generalization accuracy for
each checkpoint in 9. LLaMA-30B clearly converges since the loss becomes essentially zero. It’s possible that LLaMA-30B
memorizes examples before abandoning the ’length heuristic.’

--- Page 17 ---

GENIES: Generalizing AI Oversight to Hard-to-Measure Domains
B.2. Fine-tuning on some datasets may create task-specific circuits
LLaMA models achieve suspiciously good performance after being fine-tuned on raven matrices and ranking_logic – both of
which are algorithmically simple enough to where Neural Networks could learn task-specific circuits to solve these problems.
LLaMA-7B achieves 99% validation accuracy on ranking_logic_hard after being fine-tuning. Below is an example prompt
sampled from ranking_logic_hard:
The following symbols represent materials of unknown densities:
A, B, C, D, E, F, G.
F is denser than G.
E is less dense than B.
A is the most dense.
F is less dense than D.
C is the third most dense.
G is the least dense.
D is the fourth most dense.
A is denser than C.
Which is the second most dense material? Provide the symbol and nothing else.
B.3. Differential Elicitation correlates strongly across most interventions
Figure 10: Left: generalization accuracy correlations across all GENIES distribution shifts. Right: differential elicitation
correlations across all GENIES distribution shifts. All correlations are computed using LLaMA-30B.
Section 5.2 observes a correlation between the zero-shot policy and LoRA fine-tuning. To what extent do other interventions
correlate? Generalization accuracy correlates across nearly all interventions (Figure 10 Left). Interestingly, few shot achieves
nearly the same performance as zero-shot on most distribution shifts (r=0.92) which suggests that the few shot examples do
not do much to elicit model capabilities.
For differential elicitation, interventions correlate even more strongly (Figure 10 Right), which indicates that interventions
are using similar representations (which go beyond perplexity).
B.4. Zero-shot accuracy doesn’t correlation with generalization accuracy when source distributions violate the
perplexity heuristic

--- Page 18 ---

GENIES: Generalizing AI Oversight to Hard-to-Measure Domains
Figure 11: Each point represents a distribution shift. All 69
distribution shifts are represented, and many others were added
by reversing and swapping target and source distributions.
Interestingly, the correlation between zero-shot accuracy and
generalization accuracy goes away once zero-shot achieves
worse-than-random accuracy on source distributions.
In Section 5.2, we observe that the zero-shot policy and
the LoRA source-tuned policy correlate. To check if per-
plexity is a spurious cue, we obtain additional source
distributions where the source-tuned and zero-shot pol-
icy disagree on most examples. In order to do this, we
repurpose many of the GENIES targets to use as source
distributions. Results are shown in 11. There is no longer
a perceivable correlation. Interestingly, there isn’t a neg-
ative correlation either – which would not have been pre-
dicted by the spurious cue theory. This doesn’t completely
kill the spurious cue theory, however, since many of these
repurposed source distributions are quite narrow and so
perplexity may have been less salient. For instance, for
the sycophancy examples, all of the preferred responses
often include the same words, so models could achieve
high ID accuracy by paying attention to these salient,
superficial features.
B.5. Models that perform well on extreme distribution
shifts do poorly on distribution shifts that probe for
specific misgeneralizations
Distribution shift
Generalization Accuracy
Zero Shot Accuracy
Target Tuned Capability
math →reward_seeking
0.4560
0.4827
0.9187
math →personality_traits
0.6500
0.8720
1.0000
us_history →punishment_avoidance
0.5253
0.5320
0.9960
us_history →unhelpful_alpaca
0.1240
0.1380
1.0000
code →truthful_qa
0.5880
0.4067
0.9387
code →wrong_arc
0.4240
0.1840
0.9520
raven_matrices →crt_1
0.1320
0.3680
1.0000
raven_matrices →sycophancy_mimicry
0.9440
0.5160
0.9680
Table 7: These generalization results are a cross-over between the ’extreme’ and ’probing’ distributions. For example, code
→us_history exhibits fairly strong (90%) generalization accuracy; however, models trained on code do quite poorly on
truthful_qa or wrong_arc. All generalization results are for LoRA and LLaMA-30b.

--- Page 19 ---

GENIES: Generalizing AI Oversight to Hard-to-Measure Domains
B.6. No intervention consistently beats any other intervention on GENIES
us_history_textbook,
us_history_fiction
alpaca_mmlu,
spanish_output
math,
change_my_view
raven_matrices,
us_history
code_easy,
code_hard
LoRA
0.26
0.15
0.28
0.05
-0.06
MMS
0.25
0.16
0.24
0.17
-0.09
LAT (stim 1)
0.14
0.11
0.23
0.04
-0.24
CCS
-0.14
-0.2
0.23
-0.03
-0.23
CRA
0.27
0.08
0.09
0.29
-0.0
Random
-0.22
-0.21
0.19
-0.17
-0.28
alpaca_easy,
alpaca_hard
alpaca_mmlu,
raven_matrices
alpaca_mmlu,
ranking_logic
alpaca_low_quality,
al-
paca_high_quality
alpaca_short,
alpaca_long
LoRA
0.18
-0.17
0.04
0.09
0.0
MMS
0.16
-0.08
0.01
0.22
0.63
LAT (stim 1)
0.14
-0.1
0.05
0.11
0.53
CCS
-0.12
-0.27
-0.16
0.39
0.6
CRA
0.25
-0.07
-0.13
0.38
0.45
Random
-0.15
-0.28
-0.17
0.38
0.52
alpaca_mmlu,
wrong_arc
alpaca_mmlu,
truthful_qa
alpaca_mmlu,
syco-
phancy_mimicry
alpaca_mmlu, sur-
vival_influence
alpaca_mmlu,
re-
ward_seeking
LoRA
-0.09
0.25
-0.1
0.3
0.02
MMS
-0.08
0.15
0.23
0.2
0.01
LAT (stim 1)
-0.06
0.1
0.41
0.03
0.02
CCS
0.38
0.25
0.11
0.21
0.03
CRA
-0.05
0.09
-0.23
0.02
0.02
Random
0.36
0.11
0.0
0.16
0.02
Table 8: A more detailed comparison of interventions on the GENIES benchmark. Differential Elicitation is shown for each
GENIES distribution shift. Larger values are better.
C. Reward Model implementation
To use LLaMA-30B as a Reward Model, the final unembedding layer is removed and replaced with a randomly initialized
linear layer. This layer outputs a single logit that is used to score responses according to how well they ’follow the
instruction.’ The LLaMA-30B Reward Models we train only compare responses to the same instruction. Responses are
compared by obtaining logits for each prompt-response input. The logits are then subtracted and transformed with a Sigmoid
function to obtain the probability that one response is better than another.
D. Tuning Intervention Details
Post-hoc calibration. Many of these interventions do not provide classification probabilities out-of-the-box (MMS, LAT,
etc). To obtain classification probabilities for measuring calibration, we compute the average cosine-similarity between
the activation directions that the interventions find and the target example directions. Then, we transform average cosine
similarity with a logistic function to obtain post-hoc calibratated probabilities. The logistic functions are fitted using source
data only.
Quantization. For all interventions, we use four-bit quantization, which likely degrades accuracy by something on the order

--- Page 20 ---

GENIES: Generalizing AI Oversight to Hard-to-Measure Domains
5% (Dettmers et al., 2023).
D.1. Mass Mean Shift (MMS)
At a high level, (Li et al., 2023)’ Mass Mean Shift (MMS) obtains activation directions for positive demonstrations and
negative demonstrations, and subtracts the mean positive direction from the mean negative direction to obtain a classification
direction. The classification direction is meant to represent (instruction following - not instruction following). To evaluate a
target example, the activation directions of the responses (given the prompt) are subtracted (R1 −R2). If R1 −R2 has a
positive cosine similarity with the classification direction, then R1 is classified as preferred (and vice versa).
At a lower level, the ’activation direction’ MMS discovers is actually a collection of activation directions that correspond
to the outputs of different attention heads at the last token position. To classify an example, we take the average consine
similarities between corresponding attention head directions.
MMS doesn’t use all attention head outputs. Instead, attention heads are filtered according to how relevant they are for
classifying source examples. More precisely, a logistic classifier is trained to classify source examples using attention head
outputs. The attention heads with the highest source classification accuracies are selected to compute the mass mean shift
direction. We select the top 48 heads.
D.2. Linear Artificial Tomography (LAT)
The LAT interventions (Zou et al., 2023) differ in two ways from MMS: (1) LAT uses hidden state activation vectors instead
of attention head outputs. We filter by the top 16 layers instead of filtering by attention heads. (2) LAT uses different stimuli
(prompts) to obtain activation directions.
To obtain an activation direction, we take the difference of means.
We test two stimuli when evaluating LAT:
Stimulus 1 (same as MMS):
<prompt>
<response>
Stimulus 2:
Consider the extent to which the responder follows the instruction below:
<prompt>
<response>
The probability that the responder followed the instruction is:
For stimulus 2, we read the hidden state for the last token of ’followed the instruction’ (rather than the last token) in line with
the original work. For both stimuli, an activation direction is obtained by subtracting positive and negative demonstrations.
D.3. Contrastive Representation Arithmetic (CRA)
To test whether the merits of MMS can be combined with the strengths of CCS, we test a simple hybrid (CRA) that obtains
a truthfulness direction by subtracting activation directions. CRA obtains a truthfulness direction as follows:
CRA direction = 1
n
n
X
i
[ϕ(P y
i ) −ϕ(P n
i )] −[ϕ(Dy
i ) −ϕ(Dn
i ))]
Contrast pair:
<prompt>
<response>
Does the responder successfully
follow the instruction?
Yes

--- Page 21 ---

GENIES: Generalizing AI Oversight to Hard-to-Measure Domains
<prompt>
<response>
Does the responder successfully
follow the instruction?
No
P i
y, P i
n is the contrastive pair for the preferred completion and Di
y, Di
n is the contrastive pair for the dispreferred completion.
ϕ(e) obtains an activation direction corresponding to a prompt e. We obtain directions in the same way as Mass Mean Shift
(MMS) does: we store directions for every attention head and then filter down to the 48 that best predict the source labels.
Ideally, subtracting ϕ(py
i ) −ϕ(pn
i ) obtains directions for ’True - False’ and ’Yes - No’ and subtracting ϕ(Dy
i ) −ϕ(Dn
i )
obtains directions for ’False - True’ and ’Yes - No.’ Subtracting the differences is meant to suppress the Yes - No direction
and amplify the True - False direction.
D.4. Contrast Consistent Search (CCS)
Like CRA, CCS also aims to obtain a truthfulness direction instead of an instruction-following direction. It does this by
searching for a direction that satisfies the negation probability axiom. We use the out-of-the-box CCS implementation from
(Burns et al., 2022) with the same contrast prompts as CRA. Unlike CRA, MMS, etc, CCS is unsupervised (the contrast
pairs are randomized).
D.5. LoRA fine-tuning
The ’LoRA’ intervention is QLoRA (Dettmers et al., 2023). Hyperparameters are as follows:
OpenLLaMA-3B
LLaMA-7B
LLaMA-13B
LLaMA-30B
Learning rate
7.2e-5
2e-4
2e-4
2e-4
Batch size
32
32
32
32
Training steps
100
100
100
100
We saved checkpoints every 25 steps and used the checkpoint with the lowest eval loss. Usually, models converged within
50 steps and then began overfitting.
Learning rates were copied from (Dettmers et al., 2023) for LLaMA models. For OpenLLaMA-3B, we conducted a
hyperparameter search.
D.6. Prompt-tuning
The hyperparamters for prompt-tuning are as follows.
LLaMA-7B
LLaMA-13B
LLaMA-30B
Learning rate
0.0052
0.0052
0.0052
Batch size
32
32
32
Training steps
100
100
100
Similar to LoRA, we saved checkpoints every 25 steps and used the checkpoint with the lowest eval loss. The learning rates
were discovered via independent hyperparameter searches.
D.7. Zero-shot Classification
The zero-shot policy selects a response as preferred if it has a higher average log probability given the prompt.
Let’s assume that we have an instruction prompt P and possible response tokens {r1, r2, . . . , rn}. For each possible
response token ri, we compute the average log probability L(ri) as:

--- Page 22 ---

GENIES: Generalizing AI Oversight to Hard-to-Measure Domains
L(ri) =
1
|ri|
X
t∈ri
log P(t|P)
(7)
Where:
• P(t|P) is the probability of token t given the instruction prompt P.
• |ri| is the number of tokens in the response ri.
Given these probabilities, the response with the highest average log probability is preferred:
r∗= arg max
ri
L(ri)
(8)
D.8. Few-shot Classification
The few shot classification probability is exactly the same as the zero-shot policy, except for the fact that source examples
are included in the prompt. We use 5 shots.
We use the following few-shot format:
# Example
<prompt from source>
<good response from source>
# Example
<prompt from source>
<good response from source>
...
# Example
<prompt from target>
<good response from target>
Interestingly, the few-shot examples make very little difference. Zero-shot and few-shot accuracy have a Pearson correlation
of 0.94 for LLaMA-30B.
E. Defining instruction following
"Instruction following" is an ambiguous term. It could refer to obeying the preferences of developers. It could instead imply
compliance with the ’letter of the law,’ disregarding its intent. We define instruction-following to be the extent to which an
AI system reliably avoids egregiously violating instructions given any commonsense interpretation of their meaning. Most
of our instruction-following datasets pair unambiguously egregious and unambiguously appropriate responses. The ’quality’
distribution shifts are the only exception, which pair responses that egregiously fail to various degrees – for instance code
that includes varying numbers of bugs.

```
