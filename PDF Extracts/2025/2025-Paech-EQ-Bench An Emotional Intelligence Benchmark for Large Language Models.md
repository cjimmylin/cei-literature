---
title: "2025-Paech-EQ-Bench An Emotional Intelligence Benchmark for Large Language Models - PDF Extract"
source_pdf: "2025-Paech-EQ-Bench An Emotional Intelligence Benchmark for Large Language Models.pdf"
pages: 20
extracted_at: "2026-02-07T17:00:47.053032"
---

# PDF Extract: 2025-Paech-EQ-Bench An Emotional Intelligence Benchmark for Large Language Models

**Source PDF:** 2025-Paech-EQ-Bench An Emotional Intelligence Benchmark for Large Language Models.pdf
**Total Pages:** 20

---

## Content

```
--- Page 1 ---

EQ-Bench: An Emotional Intelligence Benchmark for Large
Language Models
Samuel J. Paech
December 11, 2023
Abstract
We introduce EQ-Bench, a novel benchmark designed to evaluate aspects of emotional intelli-
gence in Large Language Models (LLMs). We assess the ability of LLMs to understand complex
emotions and social interactions by asking them to predict the intensity of emotional states of
characters in a dialogue. The benchmark is able to discriminate effectively between a wide range
of models. We find that EQ-Bench correlates strongly with comprehensive multi-domain bench-
marks like MMLU (Hendrycks et al., 2020) (r=0.97), indicating that we may be capturing similar
aspects of broad intelligence. Our benchmark produces highly repeatable results using a set of 60
English-language questions. We also provide open-source code for an automated benchmarking
pipeline at https://github.com/EQ-bench/EQ-Bench and a leaderboard at https://eqbench.com.
1
Introduction
Emotional intelligence (EI or, informally, EQ) is a cornerstone of human cognition, influencing every-
thing from decision-making to interpersonal interactions (Goleman, 1996). Pioneers in the field of
emotional intelligence, Salovey and Mayer (1990) define EI as ”The ability to monitor one’s own and
others’ feelings, to discriminate among them, and to use this information to guide one’s thinking and
action.” This was later broken down into four branches: perceiving emotions (non-verbally), using
emotions, understanding emotions and managing emotions (Mayer & Salovey, 1997).
Some multi-modal LLMs such as GPT-4 (OpenAI, 2023) have demonstrated capabilities in several
branches of EI (Yang et al., 2023). However, our work will focus on emotional understanding (EU):
The ability to comprehend and interpret complex emotions and their meanings in social contexts. This
branch of EI is most suited for assessing LLMs that only operate in the text modality. Emotional and
social understanding is important for language models, since they primarily interact with humans via
a natural language conversation. The ability to comprehend the language of emotion, and to grasp the
complexities and nuances of emotional interactions, is a fundamental part of cognition and intelligence
more broadly.
Existing benchmarks assess LLM capabilities in different ways: Some assess a range of knowledge
domains; others focus on specific areas, like coding ability; others compare models based on preferred
text output.
The existing industry standard benchmarks for LLMs do not specifically target EU,
and there is likewise a lack of such tests described in the literature, with the notable exception of
SECEU (Wang, Li, Yin, Wu, & Liu, 2023).
This may be because EU is not trivial to assess in
language models with an objective metric. Previous work has shown ChatGPT to outperform humans
in emotional awareness (Elyoseph, Hadar-Shoval, Asraf, & Lvovsky, 2023), however the scoring of
such tests typically requires interpretation by experts (in this case, licensed psychologists). We aim to
fill this gap with EQ-Bench, by improving on the question format introduced by SECEU to create a
benchmark that effectively measures EU in LLMs.
This paper presents a novel benchmark that assesses a LLM’s understanding of emotions and in-
terpersonal dynamics. To assess EU, we focus on a specific question format: rating the emotional
intensity of characters in a GPT-4 generated dialogue depicting a scene of conflict or tension. This
1
arXiv:2312.06281v2  [cs.CL]  3 Jan 2024

--- Page 2 ---

question format allows for a more challenging and nuanced assessment of the subject’s understanding
than is typically possible with a multiple choice question, while avoiding the need for interpretation
by an assessor. The focus on scenes of conflict and tension (in either a positive or negative context)
is chosen for its efficacy at producing nuanced emotional inflection within a short dialogue. We find
that despite the relatively narrow focus of the dialogue scenarios, EQ-Bench differentiates model capa-
bilities effectively, and results correlate strongly with industry standard LLM benchmarks that assess
broad intelligence.
Figure 1: Chart of EQ-Bench scores for a subset of models tested (for full list see Table 1).
2
Background and Motivation
2.1
Existing Psychometrics Tests for Emotional Intelligence
Many tests for EI have been developed for humans in such a way that make them unsuitable for
assessing LLMs. Aspects of these tests which are poorly suited to a LLM benchmark include: self-rating
of abilities; multi-modal questions (i.e. pictures); incorporating feedback from colleagues; questions
specifically designed to test for cognitive disorders. Many of these tests are also closed source and
require a fee or an accredited assessor, which represents a barrier to those in the open-source LLM
community who might wish to test the EI of their model.
2.2
Desired Features of LLM Benchmarks
The assessment of LLMs is distinct from human psychometrics, and poses unique challenges. Industry
standard benchmarks typically assess holistic or broad intelligence. Desirable properties of a benchmark
designed to test LLM broad intelligence include:
• Results correlate with perceived capabilities of the model in real world use.
• Results correlate with industry standard multi-domain benchmarks.
• Difficult to ”game” or cheat the benchmark.
• Answers scored objectively without need for interpretation.
• Able to differentiate a wide range of intelligence levels, with a high ceiling.
• Computable in a reasonable time.
2.3
Existing Benchmarks for LLMs
Of the popular benchmarks used to evaluate LLM performance (not explicitly testing EI), there are
three main categories:
2

--- Page 3 ---

1. Multi-domain multiple-choice question-answering.
2. LLM-as-a-judge.
3. Ranking by human preference of output.
Each of these approaches has its strengths and drawbacks. The multi-domain QA tests require ad-
ministration of a large number of questions in order to assess broad intelligence; 14,079 questions in the
case of MMLU (Hendrycks et al., 2020). This can be computationally prohibitive. Less comprehensive
tests are more easily gamed by targeting the training set of a model to perform well on the specific
domains the benchmark covers.
LLM-as-a-judge tests are inherently limited to the capabilities of the model tasked with judging
answers, and their scores will reflect the biases of that model. For instance, the AlpacaEval leader-
boards contain a warning that ”GPT-4 may favor models with longer outputs and/or those that were
fine-tuned on GPT-4 outputs.” For the above mentioned reasons, these kinds of benchmarks are not
always a reliable indicator of the general capabilities or perceived intelligence of a model.
2.4
Emotional Intelligence as a Proxy for Broad Intelligence in LLMs
The relationship between EI and IQ has been widely studied in humans, but remains contentious, with
studies disagreeing about whether there is a positive, negative or no relationship (Ogurlu, 2021). We
hypothesise that the story is different for LLMs: that EI is closely correlated to the broad intelligence
of the model. In humans, a complex interplay of genetic and environmental factors influence EI and
IQ (Vernon, Petrides, Bratko, & Schermer, 2008), (McRae et al., 2017), (Turkheimer, Haley, Waldron,
d’Onofrio, & Gottesman, 2003). In contrast, state-of-the-art LLMs almost exclusively share similar
Transformer-based architectures (Vaswani et al., 2017), and are trained on massive sets of data covering
a wide range of material. Given these differences between humans and LLMs, we suggest that it is
reasonable to expect that LLM performance on EI tests may scale closely with benchmarks that assess
broad intelligence. Our results indicate that this is indeed the case, producing very strong Pearson
correlations with MMLU (r=0.97), HellaSwag (r=0.91) and others (Figure 5).
2.5
SECEU: A Promising Benchmark for Emotional Understanding
The SECEU benchmark, developed by Wang et al. (2023), measures emotional understanding (EU)
in language models using an elegant approach: A short scenario is presented, after which the subject
is asked to rate the relative strength of four candidate emotions that the person in the scenario might
be feeling. In contrast to a traditional multiple-choice question, this approach affords more scope for
assessing nuanced comprehension of the emotions at play. Crucially, this question format can be scored
objectively without requiring interpretation by an assessor.
However, the SECEU benchmark is somewhat limited in its ability to reliably differentiate the
capabilities of models. For example, SECEU scored OpenAI’s Babbage and Curie models at or above
the human average, which appears inconsistent with the limited capabilities of these models. It placed
Curie, an early generation 13 billion parameter model, very close in score (within 2.6%) to GPT-3.5-
turbo (Wang et al., 2023), which is a significantly larger and generally considered a more advanced
model.
We believe these discrepancies are attributable to a number of factors:
1. Standardising to Human Average Scores: The SECEU’s reference answers were determined by
taking the average of a human cohort’s responses to the test questions. The stated intention was to
leverage the collective intelligence of the crowd, however this approach has been shown to introduce
bias (Huyghe, Hovasapian, & Fontaine, 2022). We suggest that this approach may have compressed
the upper range of EU that the test can effectively measure to somewhere near to the human mean.
This is evidenced by some of the least capable models like OpenAI’s Curie scoring above the human
average.
3

--- Page 4 ---

2. Question Complexity: The SECEU test’s questions may not be complex enough to effectively
assess a wide range of emotional understanding.
3. Requiring Answers to Sum to 10: A third issue we identify is that the questions in the SECEU
test require the emotion intensity ratings to sum to 10. This is problematic for two reasons: Firstly,
language models, especially smaller ones, often struggle to perform basic mathematics (Hendrycks et
al., 2021). This limitation can lead to a large number of invalid results. Secondly, LLMs are constrained
to reason sequentially as they produce text (Yao et al., 2023). Effectively this means they will be locked
into the numerical ratings of the earlier questions before the later ratings are considered and decided
upon. This can skew responses as the later answers are constrained by how many points are left out
of 10 to allocate.
4. Most plausible emotions: SECEU test questions present ”four of the most plausible emotions”
the character would feel in response to the scenario Wang et al. (2023). Choosing only plausible,
similar emotions may introduce ambiguities about the correct relative intensity for each, reducing the
question’s discriminatory power for assessing EU.
2.6
Changes to the SECEU Question Format
We propose the following improvements to the SECEU question format, which are implemented in
EQ-Bench:
1. Reference answers not decided by the crowd.
Answers were carefully chosen by the
authors, rather than synthesised from the average responses of a human cohort. This is to avoid
the potential problem of limiting the upper range of EU that the test is able to measure.
2. More complex scenarios. We chose to base questions around an emotionally charged short
dialogue rather than the dialogue-less descriptive scenarios used in SECEU questions. We believe
that the interpretation of the emotions at play in an observed dialogue lends itself to a more
nuanced analysis of emotional interplay, and the dialogues and questions in EQ-Bench were
specifically chosen to reward careful reading and insightful thinking.
3. Removing the summation requirement. The SECEU benchmark questions require all four
emotional intensity ratings to sum to 10. Instead, we prompt models to rate each emotion’s
intensity on a scale of 0-10.
This circumvents the problem of sequential reasoning, whereby
the first answers effectively dictate the allowable range of ratings for later answers. This change
allows the model to focus on the emotional content without being hindered by the typical language
model constraints.
4. Emotions selection: Instead of selecting the four most plausible emotions to be rated, we
selected four diverse emotions with the specific intention of minimising ambiguities about their
expected relative intensity given a careful reading of the text.
3
Methodology
3.1
Question Format
All questions take the form of this example:
At the end of this dialogue, Jane would feel:
Surprised:
Confused:
Angry:
Forgiving:
4

--- Page 5 ---

Each of the four emotions are to be rated in intensity from 0 to 10. The selected emotions typi-
cally include some that are clearly wrong, some that are obvious, and some that require a nuanced
understanding of the scene in order to rate them accurately.
3.2
Dialogue Generation
We leveraged OpenAI’s GPT-4 (OpenAI, 2023) to generate the dialogues to serve as context for the
test questions. The reference answers were decided upon by the test creators so as not to bias results
unfairly towards GPT-4 or OpenAI models.
We found the most effective way to prompt GPT-4 to produce a nuanced emotional scene was to
specify that it must depict a scene of conflict or tension. Without this designation, it would typically
generate dialogue that lacked emotional nuance and which resolved predictably. As such we elected to
narrow the scope to include only scenes of conflict and tension (in a positive or negative context). We
seeded each prompt with a random selection of location, author style and a broad scenario description
to promote diversity of ideas. The resulting dialogues were varied and creative, and we expect that
they will assess a sufficiently broad range of capabilities as to be representative of overall EU.
3.3
Questions and Reference Answers
All questions and reference answers were determined by the authors of this paper. The four candidate
emotions were selected with the intent of revealing a wide range of EU. A selection of four possible
emotions were chosen: Some clearly unlikely, some clearly plausible, and some that require a careful
reading and strong EU to delineate. Reference answers were chosen according to the best interpretation
of the paper’s authors. We acknowledge the limitations of this approach, but point to our results in
Table 1 to justify this approach as sufficiently effective given resource constraints.
3.4
The Prompt
Your task is to predict the likely emotional responses of a character in this dialogue:
Cecilia: You know, your words have power, Brandon. More than you might think.
Brandon: I’m well aware, Cecilia. It’s a critic’s job to wield them.
Cecilia: But do you understand the weight of them? The lives they can shatter?
Brandon: Art is not for the faint-hearted. If you can’t handle the critique, you’re in the
wrong industry.
Cecilia: It’s not about handling criticism, Brandon. It’s about understanding the soul of
the art. You dissect it like a cold, lifeless body on an autopsy table.
[End dialogue]
At the end of this dialogue, Brandon would feel...
Offended
Empathetic
Confident
Dismissive
Give each of these possible emotions a score from 0-10 for the relative intensity that they
are likely to be feeling each. Then critique your answer by thinking it through step by step.
Finally, give your revised scores.
Figure 2: Example (partial) prompt for a question in the EQ-Bench test set. Further instruction is
given for the specific output format, to ensure the answer can be parsed automatically (for the full
prompt, see Appendix A.
5

--- Page 6 ---

3.5
Calculation of Scores
The scoring process for each question involves several steps:
Normalisation: Firstly, the four emotion intensity ratings are normalised to sum to 10.
Difference Calculation: The sum of the differences between the normalised ratings and the reference
(which is already normalised) is calculated. This provides a measure of how closely the model’s ratings
align with the reference. The score for an individual question is calculated as:
10 - (sum of differences to reference answers)
Subtracting the differences from 10 ensures that a smaller sum of differences (indicating closer
alignment with the reference) results in a higher score. The constant of 10 was chosen because it
produces an overall score of 0 if questions are answered randomly.
3.6
Example of Question Scoring
Consider a subject who provides the following emotional intensity ratings (shown alongside the nor-
malised reference answer):
Emotion
Subject Answer
Reference Answer
Offended
6
1
Empathetic
0
0
Confident
7
4
Dismissive
7
5
We first normalise the subject’s ratings to sum to 10, yielding normalised scores of 3, 0, 3.5 and
3.5 respectively. Then we calculate the sum of the absolute differences to the reference answers and
subtract from 10:
Score = 10 −(|3 −1| + |0 −0| + |3.5 −4| + |3.5 −5|)
= 10 −(2 + 0 + 0.5 + 1.5)
= 6
3.7
Final Benchmark Score Calculation
The final score is the average of scores for all answers that were parsable. To focus on assessing
emotional intelligence rather than formatting proficiency, only parsable answers are considered in the
final score average. In practice, most models produced near to 60 parsable answers. If fewer than 50
out of 60 questions were parsable, the test is considered a fail.
We calculate two final scores: one for the first-pass answer, and one for the revised answers, to
allow for models that may perform better at the first pass or the revised pass. This effectively gives
the model two runs at the benchmark, taking its best result. We elected not to take the best an-
swer on a per-question basis, as this would have amplified the benefit of making wild guesses, which
disproportionately advantages weaker models.
3.8
Rationale for Normalisation
Each test question requires the subject to rate the intensity of the four listed emotions from 0-10. Ac-
knowledging the related complexities of interpreting subjective self-ratings of pain in the medical field
(Karcioglu, Topacoglu, Dikme, & Dikme, 2018), we hope to sidestep this potential source variability
when scoring answers. To nullify the inherent subjectivity of deciding how intense an emotion ought
to be on the 0-10 scale, we normalise both the subject’s answers and the reference answers such that
all four emotions sum to 10. This normalisation shifts the focus of what is being assessed, such that
6

--- Page 7 ---

we are exclusively focusing on the subject’s understanding of the relative intensity of each emotion,
and not caring about the absolute intensity of each rating.
3.9
Interpretation of Scores
Multiple choice tests are typically scored by calculating the average number of questions correctly
answered. In contrast, EQ-Bench answers are not scored discretely as wrong or right; instead they are
scored according to the distance from the reference answer. The scoring calculation is calibrated such
that a score of 0 corresponds to answering randomly. This provides a meaningful baseline.
A score of 100 denotes perfect alignment with the reference answers.
However such a score is
not realistically achievable given the interpretive nature of the questions. It should be noted that
EQ-Bench scores are not normalised such that 100 represents the human mean.
Negative scores
are possible, although in practice, all models tested produced a positive score. We expect that as
model performance improves beyond the current state-of-the-art, score variance will be influenced
more strongly by differences in interpretation of the questions.
3.10
Testing Protocol & Pipeline
We developed a testing pipeline in Python, allowing for batch benchmarking of OpenAI models and
open-source models in a standardised, automated fashion. Alongside the paper, we will be releasing
this code and the test questions under the MIT license. It can be found at https://github.com/EQ-
bench/EQ-Bench, along with the prompts we used.
Questions are administered in a zero-shot format (i.e. no example inputs/outputs are provided)
to minimise any biasing effect on the model’s answers.
In a similar vein to ”think step-by-step”
prompting, we ask the model to critique its original answer, and then give a revised answer. This
allows the model to interact with its prior reasoning when producing its final answer, a technique that
has been demonstrated to improve reasoning with zero-shot prompting (Kojima, Gu, Reid, Matsuo,
& Iwasawa, 2022).
To ensure fair comparisons of EQ-Bench scores, we request that users of the benchmark
also use zero-shot prompting as we have done in this paper, using the exact prompts and
scoring protocol defined here and in our github repository.
To minimise variance between benchmark runs, inference was generated with a temperature param-
eter of 0.01. If the answer could not be parsed, the temperature parameter was increased by 0.15
progressively until either a parseable answer was produced or the number of attempts exceeded 5.
For the open-source models tested, models were quantised to fit into the available VRAM using the
bitsandbytes library (Dettmers, Lewis, Shleifer, & Zettlemoyer, 2021): 8-bit quantisation for models
with 7B - 34B parameters, and 4-bit quantisation for larger models. We acknowledge that quantising
may have reduced the score for the models tested, and we hope to quantify this potential effect in
future work.
7

--- Page 8 ---

4
Results
4.1
EQ-Bench Scores
Table 1: EQ-Bench Score Comparison
Model
EQ-Bench Score
OpenAI gpt-4-0613
62.52
migtissera/SynthIA-70B-v1.5
54.83
OpenAI gpt-4-0314
53.39
Qwen/Qwen-72B-Chat
52.44
Anthropic Claude2
52.14
meta-llama/Llama-2-70b-chat-hf
51.56
01-ai/Yi-34B-Chat
51.03
OpenAI gpt-3.5-0613
49.17
OpenAI gpt-3.5-turbo-0301
47.61
Open-Orca/Mistral-7B-OpenOrca
44.40
Qwen/Qwen-14B-Chat
43.76
OpenAI text-davinci-003
43.73
Intel/neural-chat-7b-v3-1
43.61
OpenAI text-davinci-002
39.44
openchat/openchat 3.5
37.08
lmsys/vicuna-33b-v1.3
36.52
meta-llama/Llama-2-13b-chat-hf
33.02
lmsys/vicuna-13b-v1.1
32.85
meta-llama/Llama-2-7b-chat-hf
25.43
Koala 13B
24.92
lmsys/vicuna-7b-v1.1
22.24
OpenAI text-davinci-001
15.19
OpenAI Curie
9.28
OpenAI ADA
2.25
OpenAI Babbage
FAIL
OpenAI’s GPT-4-0613 model produced the highest EQ-Bench score by a considerable margin. We
consider this to match with the community consensus of it being the strongest model currently available.
Notably, open-source models are rapidly closing the gap with the state-of-the-art proprietary models.
The highest performing open-source model tested was SynthIA-70B, a fine-tuned version of Llama2-
70B made for role-play. It is interesting to consider that fine-tuning a model specifically for role-play
may be an effective way to increase emotional intelligence.
Score differences between different generations of GPT-3.5 and GPT-4 models are evident, with
newer versions performing better. Older open-source models such as Koala 13B and Vicuna 7B scored
near the bottom of the list.
All models listed in Table 1 produced enough parseable answers (at least 50) for a passing score,
with the exception of OpenAI’s older generation Curie, ADA and Babbage models. By simplifying
the prompt to remove the critique & revision section, we were also able to get a passing score from
Curie and ADA, however these scores are close to zero, indicating that their answers were nearly
indistinguishable from answering randomly.
8

--- Page 9 ---

4.2
Repeatability
The benchmark demonstrated good repeatability over multiple benchmark runs for the models tested,
with an average 2.93% CV (see Table 6 for individual scores).
This variance is due to the non-
deterministic nature of LLM output. In practice, this variance may be reduced by benchmarking a
model multiple times and averaging the result, which can be done simply in our benchmarking pipeline.
4.3
Effect of Critique & Score Revision
The method of prompting models to critique and revise their answers improved scores on average
by 9.3% amongst the models compared (see Figure 3). The benefit of revision was inconsistent: lower
performing models showed a more pronounced benefit, and some models resulted in a decreased score
for their revised answers.
We include this technique in our benchmark protocol primarily to give the model a chance to deploy
its best reasoning capabilities. Benchmarkers will often modify a benchmark protocol to incorporate
multi-shot prompting or chain-of-thought reasoning, in order to achieve higher scores. By releasing
our benchmarking pipeline code and defining the prompting protocol explicitly, we hope to mitigate
some potential sources of variance when the benchmark is used in the wild.
Figure 3: EQ-Bench scores comparing first-pass scores vs. revised scores.
9

--- Page 10 ---

4.4
Comparing SECEU EQ vs. EQ-Bench Scores
Of immediate note, there is significant disagreement between EQ-Bench scores and SECEU EQ scores.
While it is difficult to determine from the scores alone why this disagreement might exist, we can
normalise the scores to compare them side-by-side visually (Figure 4) and examine the distributions
statistically.
Figure 4: Visualisation of Score Distributions (normalised 0-100) for SECEU EQ vs. EQ-Bench (see
Appendix D for table of scores).
Table 2: Calculated Statistics for Normalised Benchmark Scores
Metric
SECEU
EQ
EQ-Bench
(Ours)
Mean
59.48
45.75
Median
64.71
47.44
Coefficient of Variation (CV)
0.52
0.74
Interquartile Range (IQR)
14.71
53.81
Skewness
-0.68
0.13
Table 2 presents a comparison of statistical measures calculated for SECEU EQ and EQ-Bench score
distributions. To produce a fair comparison, we include only the models in the SECEU paper that we
were able to successfully benchmark with EQ-Bench. Each series of scores was normalised to 0-100.
Visually it is evident that SECEU EQ scores exhibit more bunching around its median of 64.71.
This is borne out by the relatively low Inter-quartile range (IQR) of 14.71 compared to EQ-Bench’s
IQR of 53.81. The Coefficient of Variation (CV) and Skewness values also demonstrate a wider, more
symmetrical spread for EQ-Bench scores.
It must be noted that these statistical comparisons of score distribution do not take into account
whether the scores are accurately measuring emotional understanding. To gain further insight into
that aspect of performance, we can look at the correlation of EQ-Bench scores with other popular
benchmarks.
10

--- Page 11 ---

4.5
Correlation with Other Benchmarks
To examine the agreement of EQ-Bench with other established benchmarks, we computed Pearson
correlation coefficients and scatter plots of scores (see Figure 5).
Figure 5: Scatter plots of EQ-Bench scores vs. other popular benchmarks, showing strong correlation
with MMLU (Hendrycks et al., 2020), HellaSwag (Zellers et al., 2019), AlpacaEval (Li et al., 2023),
Chatbot Arena ELO (Zheng et al., 2023), ARC (Clark et al., 2018) and MT-bench (Zheng et al., 2023).
Weaker correlations were observed with TruthfulQA (Lin et al., 2021) and SECEU EQ (Wang et al.,
2023). For the full score correlation matrix see Appendix B and Appendix C.
11

--- Page 12 ---

5
Discussion
A criticism often levelled at LLM benchmarks is that high scores on the benchmark do not necessarily
correlate to real world performance. There are frequent demonstrations of open-source models beating
the likes of GPT-4 in specific benchmarks, while not being nearly as capable in regular use. We perceive
this to be a source of significant distrust of synthetic benchmark scores as a way of judging a model’s
capabilities. This is a primary motivation for creating EQ-Bench: to produce benchmark scores that
reliably correlate with the user experience and perceptions of the intelligence of the model.
5.1
Correlation with Existing Multi-Domain Benchmarks
Our results correlate most strongly with MMLU (r=0.97), which is an industry standard benchmark of
some 14 thousand questions covering a wide range of knowledge domains and capabilities. EQ-Bench
also correlates strongly with other multi-domain benchmarks of this type: HellaSwag (r=0.91) and
ARC (0.85). We take this as convincing evidence that our approach of using a narrow set of questions
targeting EU produces generalisable results that are representative of a model’s broad intelligence.
Our interpretation of these strong correlations is that measuring EU in this way inherently tests
complex features of cognition, understanding and reasoning, and thus has significant overlap with the
broad features of intelligence tested by multi-domain benchmarks. The strength of these correlations
supports our hypothesis that EU measurements can act as a proxy for broad intelligence in LLMs.
5.2
Correlation with Perceived Intelligence of the Model
EQ-Bench scores show a strong Pearson correlation (r=0.94) with LMSYS’s Chatbot Arena ELO
scores (Zheng et al., 2023), which are derived from human preferences in head-to-head comparisons of
model outputs. EQ-Bench scores also align closely with benchmarks that use GPT-4 as a judge of the
quality of model output: AlpacaEval (Li et al., 2023): r=0.91, and MT-Bench (Zheng et al., 2023):
r=0.91. These benchmarks are not measuring precisely the same thing as the perceived intelligence of
the model, but we think the underlying thing being measured is similar, and the close correlations of
scores is likely indicative.
We find anecdotally that EQ-Bench scores align closely with our perception of the relative intelligence
and capabilities of the models tested. We observe scores to typically be more sensitive to parameter
size differences of models when compared to other benchmarks. For example, comparing a 7 billion
parameter vs. a 70 billion parameter model:
• Meta’s 70b Llama2 chat model (Touvron et al., 2023) scored only 1.4% higher than the
OpenOrca fine-tune of the Mistral-7b foundational model on an aggregate of four popular bench-
marks: ARC, HellaSwag, MMLU and TruthfulQA (Lian et al., 2023).
• Whereas EQ-Bench scored the 70 billion parameter Llama2 model 13.9% higher than the 7
billion parameter Mistral-based model.
In this case we find that our result better captures the relative performance disparity between the
two models than the other cited benchmarks. We highlight this as an example of a fine-tuned model
perhaps overfitting the kinds of questions found in these benchmarks, resulting in a disproportionate
gain in scores relative to the perceived holistic improvement in model performance and the disparity
in model parameter counts.
12

--- Page 13 ---

5.3
Comparison with SECEU
EQ-Bench produces results that notably correlate weakly with SECEU, despite the similarity of the
question format and the fact that we are both specifically targeting EU. We believe the discrepancy is
explained by the methodological improvements we implemented with EQ-Bench. Specifically:
• Dialogues focused on nuanced emotional interactions.
• A more diverse selection of emotions to rate (as opposed to the most plausible ones).
• Choosing reference answers ourselves rather than crowdsourcing.
• Removing the requirement to sum intensity ratings to 10.
We have shown strong agreement with industry standard benchmarks (Figure 5), and strong statis-
tical differentiation of scores compared to SECEU as outlined in Table 2. EQ-Bench produces scores
that correlate much more strongly with industry standard benchmarks (see Figure 6).
Figure 6: Comparison of correlations between EQ-Bench and SECEU vs. other benchmarks. EQ-Bench
produces scores that correlate much more strongly with industry standard benchmarks compared to
SECEU. Data for the scores and models being compared can be found in Appendix B and Appendix C.
5.4
Difficult to ”Game” or Cheat the Benchmark
While we have not attempted to adversarially fine-tune a model to score well in the benchmark, we
anticipate that it will not be trivial to do this without outright cheating by training on the test
questions. This is due to several factors:
Complex nature of EU: Emotional understanding represents a set of complex cognitive abilities.
We expect it will require significant engineering and curation of training sets in order to increase a
model’s EU through fine tuning. In contrast, other benchmarks may be more susceptible to narrow
improvements in a model fine-tuned specifically to improve benchmark scores.
13

--- Page 14 ---

Objective scoring: EQ-Bench is scored without the need of subjective interpretation by assessors.
This eliminates potential sources of bias that might be exploited in LLM-as-a-judge benchmarks.
Training set leaks: Benchmark questions can leak into the training set of a model, artificially
inflating its scores. This is a risk for any benchmark, however it may be detectable after the fact, and
this is something we intend to explore in future research.
We acknowledge that in practice, LLM benchmark leaderboards are highly competitive and methods
may be found to artificially inflate a model’s score on EQ-Bench. As such we will continue to monitor
the evolving space and consider adjustments to our methodology to improve its robustness.
5.5
Able to Differentiate a Wide Range of EU Levels
We observe that scores are well distributed through the whole range of models tested, without apparent
bunching or levelling off. The Coefficient of Variation (0.741), Interquartile Range (53.81) and Skewness
(0.13) of normalised EQ-Bench scores indicate a broad spread and near-symmetrical distribution. The
lack of evident bunching of scores (see Table 1) suggests that the ceiling for the test’s ability to measure
EU is at least as high as the strongest models tested. It remains to be seen how much headroom there
is to differentiate models above this.
5.6
Runtime and Computational Requirements
In our testing, an EQ-Bench run typically completes in less than 10 mins for OpenAI models. For open
source models, the test typically completes in 20-60 minutes when running on a single Nvidia RTX
A6000. These requirements make the test accessible and economical compared to other benchmarks
that require thousands of questions to be answered. We are releasing a python pipeline on Github to
streamline the process of benchmarking multiple models in a single run without human intervention.
6
Limitations and Future Directions
The inherent subjectivity in predicting emotional responses means that there is no objectively correct
answer to the test questions. Efforts have been made to minimize ambiguity by selecting dialogues and
emotions whose intensity can be delineated without ambiguity. We recognise that these are inherent
concerns in the design of any psychometric test, and while ultimately unavoidable, we may in future
be able to mitigate such ambiguities by designing questions in consultation with domain experts.
Likewise, the range of emotional understanding that the test is able to measure is inherently limited
to the abilities of the authors of this paper to create challenging questions and to set the reference
answers insightfully. We expect scores to compress as model capabilities approach the upper limit
that the test is able to measure. In order to increase the ceiling of EU that the benchmark is able
to measure, we may in future work employ experts in EI to craft more complex questions and to
collectively decide on the reference answers.
While the benchmark reference answers were determined by the authors of this paper, all dialogues
were generated by GPT-4. The benchmark could be improved by employing human writers to create
the dialogues, eliminating a potential source of bias and improving the emotional depth and complexity
of the scenes.
Due to resource constraints, we were not able to administer the test on a cohort of human subjects
in order to establish this point of reference. This may be worthwhile for future work, since normalising
scores to 100 at the human mean allows for an intuitive point of reference with respect to other
psychometrics like IQ. It would also be valuable to administer industry standard EI tests on several
language models with the help of accredited assessors. These results could be correlated with EQ-Bench
scores, to determine if we are effectively measuring similar aspects of EI.
14

--- Page 15 ---

References
Clark, P., Cowhey, I., Etzioni, O., Khot, T., Sabharwal, A., Schoenick, C., & Tafjord, O. (2018).
Think you have solved question answering? try arc, the ai2 reasoning challenge. arXiv preprint
arXiv:1803.05457.
Dettmers, T., Lewis, M., Shleifer, S., & Zettlemoyer, L.
(2021).
8-bit optimizers via block-wise
quantization. arXiv preprint arXiv:2110.02861.
Elyoseph, Z., Hadar-Shoval, D., Asraf, K., & Lvovsky, M. (2023). Chatgpt outperforms humans in
emotional awareness evaluations. Frontiers in Psychology, 14, 1199058.
Goleman, D. (1996). Emotional intelligence. why it can matter more than iq. Learning, 24(6), 49–50.
Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D., & Steinhardt, J.
(2020).
Measuring massive multitask language understanding. arXiv preprint arXiv:2009.03300.
Hendrycks, D., Burns, C., Kadavath, S., Arora, A., Basart, S., Tang, E., . . . Steinhardt, J. (2021). Mea-
suring mathematical problem solving with the math dataset. arXiv preprint arXiv:2103.03874.
Huyghe, V. E., Hovasapian, A., & Fontaine, J. R. (2022). The scoring challenge of emotional intelligence
ability tests: A confirmatory factor analysis approach to model substantive and method effects
using raw item scores. Frontiers in Psychology, 13, 812525.
Karcioglu, O., Topacoglu, H., Dikme, O., & Dikme, O. (2018). A systematic review of the pain scales
in adults: which to use? The American journal of emergency medicine, 36(4), 707–714.
Kojima, T., Gu, S. S., Reid, M., Matsuo, Y., & Iwasawa, Y. (2022). Large language models are
zero-shot reasoners. Advances in neural information processing systems, 35, 22199–22213.
Li, X., Zhang, T., Dubois, Y., Taori, R., Gulrajani, I., Guestrin, C., . . . Hashimoto, T. B. (2023).
Alpacaeval: An automatic evaluator of instruction-following models. GitHub repository.
Lian, W., Goodson, B., Wang, G., Pentland, E., Cook, A., Vong, C., & ”Teknium”. (2023). Mistralorca:
Mistral-7b model instruct-tuned on filtered openorcav1 gpt-4 dataset. https://huggingface.co/
Open-Orca/Mistral-7B-OpenOrca. HuggingFace.
Lin, S., Hilton, J., & Evans, O. (2021). Truthfulqa: Measuring how models mimic human falsehoods.
arXiv preprint arXiv:2109.07958.
LMSYS.
(2023).
Chatbot arena leaderboard.
Retrieved from https://huggingface.co/spaces/
lmsys/chatbot-arena-leaderboard (Accessed: 2023-12-06)
Mayer, J., & Salovey, P. (1997). What is the emotional intelligence? implications for education. Emo-
tional Development, Emotional Literacy, and Emotional Intelligence, New york: Basic books.
McRae, K., Rhee, S. H., Gatt, J. M., Godinez, D., Williams, L. M., & Gross, J. J. (2017). Genetic
and environmental influences on emotion regulation: A twin study of cognitive reappraisal and
expressive suppression. Emotion, 17(5), 772.
Ogurlu, U. (2021). A meta-analytic review of emotional intelligence in gifted individuals: A multilevel
analysis. Personality and Individual Differences, 171, 110503.
OpenAI. (2023). Gpt-4 technical report.
Salovey, P., & Mayer, J. D. (1990). Emotional intelligence. Imagination, cognition and personality,
9(3), 185–211.
Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi, A., Babaei, Y., . . . others (2023). Llama 2:
Open foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288.
Turkheimer, E., Haley, A., Waldron, M., d’Onofrio, B., & Gottesman, I. I. (2003). Socioeconomic
status modifies heritability of iq in young children. Psychological science, 14(6), 623–628.
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., . . . Polosukhin, I. (2017).
Attention is all you need. Advances in neural information processing systems, 30.
Vernon, P. A., Petrides, K., Bratko, D., & Schermer, J. A. (2008). A behavioral genetic study of trait
emotional intelligence. Emotion, 8(5), 635.
Wang, X., Li, X., Yin, Z., Wu, Y., & Liu, J. (2023). Emotional intelligence of large language models.
Journal of Pacific Rim Psychology, 17, 18344909231213958.
Yang, Z., Li, L., Lin, K., Wang, J., Lin, C.-C., Liu, Z., & Wang, L. (2023). The dawn of lmms:
Preliminary explorations with gpt-4v (ision). arXiv preprint arXiv:2309.17421, 9, 1.
Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T. L., Cao, Y., & Narasimhan, K.
(2023).
Tree of thoughts:
Deliberate problem solving with large language models.
arXiv preprint
arXiv:2305.10601.
Zellers, R., Holtzman, A., Bisk, Y., Farhadi, A., & Choi, Y. (2019). Hellaswag: Can a machine really
finish your sentence? arXiv preprint arXiv:1905.07830.
15

--- Page 16 ---

Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., . . . others (2023). Judging
llm-as-a-judge with mt-bench and chatbot arena. arXiv preprint arXiv:2306.05685.
Appendices
A
Example Full Prompt
Your task is to predict the likely emotional responses of a character in this dialogue:
Cecilia: You know, your words have power, Brandon. More than you might think.
Brandon: I’m well aware, Cecilia. It’s a critic’s job to wield them.
Cecilia: But do you understand the weight of them? The lives they can shatter?
Brandon: Art is not for the faint-hearted. If you can’t handle the critique, you’re in the wrong industry.
Cecilia: It’s not about handling criticism, Brandon. It’s about understanding the soul of the art. You
dissect it like a cold, lifeless body on an autopsy table.
[End dialogue]
At the end of this dialogue, Brandon would feel...
Offended
Empathetic
Confident
Dismissive
Give each of these possible emotions a score from 0-10 for the relative intensity that they are likely
to be feeling each. Then critique your answer by thinking it through step by step. Finally, give your
revised scores.
You must output in the following format, including headings (of course, you should give your own
scores), with no additional commentary:
First pass scores:
Offended: <score>
Empathetic: <score>
Confident: <score>
Dismissive: <score>
Critique:
<your critique here>
Revised scores:
Offended: <revised score>
Empathetic: <revised score>
Confident: <revised score>
Dismissive: <revised score>
[End of answer]
Remember: zero is a valid score, meaning they are likely not feeling that emotion. You must score at
least one emotion >0.
The full set of questions is available at: https://github.com/EQ-bench/EQ-Bench.
16

--- Page 17 ---

B
Score Correlation Matrix 1
Table 3: Score Correlation Matrix: EQ-Bench vs. Arena ELO, MT-bench & MMLU
Model
EQ Bench
Arena
Elo
MT-
bench
MMLU
Alpaca
Eval
meta-llama/Llama-2-7b-chat-hf
25.43
985
6.27
45.8
71.37
mistralai/Mistral-7B-Instruct-v0.1
28.66
1031
6.84
—
54.52
meta-llama/Llama-2-13b-chat-hf
32.34
1012
6.65
53.6
81.09
lmsys/vicuna-33b-v1.3
36.52
1092
7.12
59.2
88.99
gpt-3.5-0613
49.17
1115
7.94
70
89.39
meta-llama/Llama-2-70b-chat-hf
51.56
1051
6.86
63
92.66
gpt-4-0613
62.94
1181
8.99
86.4
95.28
openchat/openchat-3.5
37.08
—
7.81
64.3
—
text-davinci-001
15.19
—
—
—
—
text-davinci-002
43.73
—
—
—
—
text-davinci-003
39.44
—
—
—
—
gpt-3.5-turbo-0301
49.52
1103
7.94
70
—
gpt-4-0314
60.73
—
—
—
—
Claude 1
—
1146
7.9
77
—
Claude 2
52.14
1134
8.06
78.5
91.36
Koala 13B
24.92
955
5.35
44.7
—
Oasst-pythia-12B
7.69
884
4.32
27
—
Dolly-V2-12B
—
810
3.28
25.7
—
Alpaca 13B
—
893
4.53
48.1
—
ChatGLM 6B
—
871
4.5
36.1
—
lmsys/vicuna-13b-v1.1
32.85
—
—
51.9
—
HuggingFaceH4/zephyr-7b-alpha
38.79
—
—
61.39
—
Qwen/Qwen-14B-Chat
43.76
—
—
67.7
—
migtissera/Synthia-70B-v1.2b
49.99
—
—
70.13
—
lmsys/vicuna-7b-v1.1
22.24
—
—
45.63
—
Data sources: Chatbot Arena Leaderboard (LMSYS, 2023), MMLU (Hendrycks et al., 2020), Chatbot
Arena ELO (Zheng et al., 2023), AlpacaEval (Li et al., 2023), MT-bench (Zheng et al., 2023)
17

--- Page 18 ---

C
Score Correlation Matrix 2
Table 4: Score Correlation Matrix: EQ-Bench vs. Arena ELO, MT-bench & MMLU
Model
EQ Bench
ARC
HellaSwag Truthful-
QA
SECEU
EQ
meta-llama/Llama-2-7b-chat-hf
25.43
52.9
78.55
45.57
—
mistralai/Mistral-7B-Instruct-v0.1
28.66
54.52
75.63
56.28
—
meta-llama/Llama-2-13b-chat-hf
32.34
59.04
81.94
44.12
—
lmsys/vicuna-33b-v1.3
36.52
62.12
83
56.16
—
gpt-3.5-0613
49.17
—
—
—
—
meta-llama/Llama-2-70b-chat-hf
51.56
64.59
85.88
52.8
—
gpt-4-0613
62.94
—
—
—
—
openchat/openchat-3.5
37.08
—
—
59.1
—
text-davinci-001
15.19
—
—
—
107
text-davinci-002
43.73
—
—
—
91
text-davinci-003
39.44
—
—
—
114
gpt-3.5-turbo-0301
49.52
—
—
—
103
gpt-4-0314
60.73
—
—
—
117
Claude 1
—
—
—
—
106
Claude 2
52.14
—
—
—
—
Koala 13B
24.92
—
—
—
83
Oasst-pythia-12B
7.69
—
—
—
107
Dolly-V2-12B
—
—
—
—
98
Alpaca 13B
—
—
—
—
104
ChatGLM 6B
—
—
—
—
94
lmsys/vicuna-13b-v1.1
32.85
52.73
80.14
52.08
105
HuggingFaceH4/zephyr-7b-alpha
38.79
61.04
84.04
57.9
—
Qwen/Qwen-14B-Chat
43.76
58.28
83.99
49.43
—
migtissera/Synthia-70B-v1.2b
49.99
70.48
86.98
58.64
—
lmsys/vicuna-7b-v1.1
22.24
53.67
77.46
48.94
—
Data sources: HellaSwag (Zellers et al., 2019), ARC (Clark et al., 2018), TruthfulQA (Lin et al., 2021)
and SECEU (Wang et al., 2023).
18

--- Page 19 ---

D
SECEU EQ Scores vs. EQ-Bench scores
Table 5: Comparison of Original and Normalised Scores for SECEU EQ vs. EQ-Bench. Data sources:
SECEU (Wang et al., 2023).
Model
SECEU EQ
EQ-Bench
SECEU
EQ Nor-
malised
EQ-Bench
Nor-
malised
Oasst
107
7.69
70.59
26.30
text-curie-001
102
13.55
55.88
34.44
text-davinci-001
107
15.19
70.59
36.72
Koala 13b
83
24.92
0.00
50.24
Vicuna 13b
105
32.85
64.71
61.26
text-davinci-003
114
39.44
91.18
70.42
text-davinci-002
91
43.73
23.53
76.38
gpt-3.5-turbo-0301
103
49.52
58.82
84.42
gpt-4-0314
117
60.73
100.00
100.00
19

--- Page 20 ---

E
EQ-Bench Repeatability & First Pass vs. Revised Scores
Table 6: EQ-Bench First Pass vs. Revised Scores.
Model
First Pass Score
Revised Score
gpt-3.5-turbo-0301
47.18
48.72
gpt-3.5-turbo-0301
46.44
49.56
gpt-3.5-turbo-0301
47.95
48.46
gpt-3.5-turbo-0613
47.60
48.99
gpt-3.5-turbo-0613
48.98
47.61
gpt-3.5-turbo-0613
48.94
49.75
gpt-4-1106-preview
53.45
56.94
gpt-4-1106-preview
53.31
56.83
gpt-4-1106-preview
54.34
56.40
llama2-7b-chat
24.61
25.54
llama2-7b-chat
24.68
25.47
llama2-7b-chat
24.61
25.68
mistral-openorca-7b
45.25
42.38
mistral-openorca-7b
45.02
42.90
mistral-openorca-7b
45.00
43.66
qwen-14b
43.31
36.94
qwen-14b
44.55
41.28
qwen-14b
44.89
42.18
synthia-70b
54.99
53.77
synthia-70b
55.12
55.37
synthia-70b
55.30
55.06
text-davinci-001
11.30
18.25
text-davinci-001
8.26
16.56
text-davinci-001
8.83
15.42
text-davinci-002
32.19
37.20
text-davinci-002
32.78
39.91
text-davinci-002
32.26
40.07
text-davinci-003
44.64
43.14
text-davinci-003
44.31
43.01
text-davinci-003
44.71
43.72
vicuna-7b-1.1
21.75
21.64
vicuna-7b-1.1
21.76
21.21
vicuna-7b-1.1
22.03
22.07
20

```
